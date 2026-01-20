#!/usr/bin/env python3
#
#  __main__.py
"""
Command-line entry point.
"""
#
#  Copyright © 2021 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#  DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
#  OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
#  OR OTHER DEALINGS IN THE SOFTWARE.
#

# stdlib
import sys
from typing import Callable, Optional

# 3rd party
import click
import cloup
from cloup.constraints import mutually_exclusive
from consolekit import click_command, option
from consolekit.options import flag_option
from domdf_python_tools.utils import stderr_writer

# this package
from highlight import __version__

__all__ = ["main"]


def option_group(
		title: str,
		*options: Callable,
		constraint: Optional[cloup.constraints.Constraint] = None,
		) -> Callable:
	return cloup.option_group(title, *options, constraint=constraint)


@click.version_option(__version__)  # type: ignore
@click_command(cls=cloup.Command)
@option_group(
		"Filetype Options",
		option(
				"-m",
				"--mime",
				help="The MIME time to use for highlighting.",
				type=click.STRING,
				default=None,
				),
		option(
				"-l",
				"--lexer",
				help="The Pygments lexer to use for highlighting.",
				type=click.STRING,
				default=None,
				),
		constraint=mutually_exclusive,
		)
@flag_option("-T", "--show-tabs", help="Display TAB characters as ^I.")
@flag_option("-E", "--show-ends", help="Display $ at the end of each line.")
@flag_option("-n", "--number", help="Number all output lines.")
@flag_option("-D", "--debug", help="Print the lexer name to stderr.")
@click.argument(
		"file",
		type=click.STRING,
		required=False,
		)
def main(
		file: Optional[str] = None,
		mime: Optional[str] = None,
		lexer: Optional[str] = None,
		number: bool = False,
		show_ends: bool = False,
		show_tabs: bool = False,
		debug: bool = False,
		):
	"""
	Print the content of FILE with syntax highlighting.

	With no FILE, or when FILE is -, read standard input.
	"""

	# stdlib
	from contextlib import suppress

	# 3rd party
	import pygments  # type: ignore[import-untyped]
	from pygments.lexer import Lexer  # type: ignore[import-untyped]
	from pygments.lexers import (  # type: ignore[import-untyped]
			get_lexer_by_name,
			get_lexer_for_filename,
			get_lexer_for_mimetype,
			guess_lexer
			)
	from pygments.util import ClassNotFound  # type: ignore[import-untyped]

	# this package
	from highlight import _TerminalFormatter, joinlines, splitlines

	lexer_cls: Optional[Lexer] = None
	end_char = '$' if show_ends else ''

	def echo(string, **kwargs):
		if show_tabs:
			string = string.replace('\t', "^I")
		return click.echo(f"{string}{end_char}", color=True, **kwargs)

	if file in {None, '-'}:
		# read from stdin
		text = sys.stdin.read()

	else:
		assert file is not None

		with suppress(ClassNotFound):
			# If there's no lexer for the file, just ignore it
			lexer_cls = get_lexer_for_filename(file, ensurenl=False, tabsize=0)

		with open(file, encoding="UTF-8") as fp:
			text = fp.read()

	if lexer is not None:
		try:
			lexer_cls = get_lexer_by_name(lexer, ensurenl=False, tabsize=0)
		except ClassNotFound as e:
			# We do care if the lexer is missing when given by name
			raise click.BadOptionUsage("--lexer", str(e))

	elif mime is not None:
		try:
			# If there's no lexer for the MIME type, warn and ignore it
			lexer_cls = get_lexer_for_mimetype(mime, ensurenl=False, tabsize=0)
		except ClassNotFound as e:
			stderr_writer(f"WARNING: {e}")

	if lexer_cls is None:
		# Last ditch effort
		with suppress(ClassNotFound):
			lexer_cls = guess_lexer(text, ensurenl=False, tabsize=0)

	lines = splitlines(text)
	if not lines[-1][1]:
		lastline_empty = True
	else:
		lastline_empty = False

	if lexer_cls is None:
		if debug:
			stderr_writer("Unable to determine lexer")
	else:
		if debug:
			stderr_writer(f"Using lexer {lexer_cls!r}")

		tokens = lexer_cls.get_tokens(joinlines(lines))
		lines = splitlines(pygments.format(
				tokens,
				formatter=_TerminalFormatter(linenos=number),
				))

	for line in lines[:-1]:
		echo(line[0])

	echo(lines[-1][0], nl=not lastline_empty)

	sys.exit(0)


if __name__ == "__main__":
	sys.exit(main())

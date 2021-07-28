#!/usr/bin/env python3
#
#  __init__.py
"""
Highlight text on the command line.
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
from itertools import chain
from typing import List, Tuple

# 3rd party
from pygments.formatters.terminal import TerminalFormatter

__author__: str = "Dominic Davis-Foster"
__copyright__: str = "2021 Dominic Davis-Foster"
__license__: str = "MIT License"
__version__: str = "0.1.0"
__email__: str = "dominic@davis-foster.co.uk"

__all__ = ["joinlines", "splitlines"]

LF = '\n'


class _TerminalFormatter(TerminalFormatter):

	def _write_lineno(self, outfile):
		self._lineno += 1
		outfile.write(f"{self._lineno != 1 and LF or ''}{self._lineno: >6}\t")


def splitlines(string: str) -> List[Tuple[str, str]]:
	# Translated and adapted from https://github.com/python/cpython/blob/main/Objects/stringlib/split.h

	str_len: int = len(string)
	i: int = 0
	j: int = 0
	eol: int
	the_list = []

	while i < str_len:

		# Find a line and append it
		while i < str_len and not string[i] in "\n\r":
			i += 1

		# Skip the line break reading CRLF as one line break
		eol = i
		if i < str_len:
			if (string[i] == '\r') and (i + 1 < str_len) and (string[i + 1] == '\n'):
				i += 2
			else:
				i += 1

		if j == 0 and eol == str_len and type(string) is str:
			# No whitespace in string, so just use it as the_list[0]
			the_list.append(string)
			break

		the_list.append((string[j:eol], string[eol:i]))
		j = i

	return the_list


def joinlines(lines: List[Tuple[str, str]]) -> str:
	return ''.join(chain.from_iterable(lines))

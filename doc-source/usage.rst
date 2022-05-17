=====================
highlight
=====================

.. click:: highlight.__main__:main
	:prog: highlight
	:nested: none

:bold-title:`Notes`

* :option:`--lexer <-l>` and :option:`--mime <-m>` are mutually exclusive.
* If no :option:`--lexer <-l>` or :option:`--mime <-m>` option is given,
  the lexer is determined from ``FILE``. If reading from standard input,
  of if the file extension is unknown, the lexer is determined by examining the file's contents.
* If the :option:`--mime <-m>` option is given but no lexer can be found for that mime type the mime type is ignored.
* See https://pygments.org/docs/lexers/ for a list of available lexers.

Examples
-----------

:bold-title:`Highlight a Python source code file.`

.. code-block:: bash

	highlight code.py

:bold-title:`Highlight a Ruby source code file with the` :class:`~pygments.lexers.ruby.RubyConsoleLexer`.

.. code-block:: bash

	highlight code.rb --lexer rbcon

:bold-title:`Highlight a Rust source code file with line numbers.`

.. code-block:: bash

	highlight main.rs --number

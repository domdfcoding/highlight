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
* See https://pygments.org/docs/lexers/ for a list of available lexers.

Examples
-----------

.. TODO:: add some examples

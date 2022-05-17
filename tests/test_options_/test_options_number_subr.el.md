     1	[37m;;; subr.el --- basic lisp subroutines for Emacs  -*- coding: utf-8; lexical-binding:t -*-[39;49;00m[37m[39;49;00m
     2	[37m[39;49;00m
     3	[37m;; Copyright (C) 1985-1986, 1992, 1994-1995, 1999-2015 Free Software[39;49;00m[37m[39;49;00m
     4	[37m;; Foundation, Inc.[39;49;00m[37m[39;49;00m
     5	[37m[39;49;00m
     6	[37m;; Maintainer: emacs-devel@gnu.org[39;49;00m[37m[39;49;00m
     7	[37m;; Keywords: internal[39;49;00m[37m[39;49;00m
     8	[37m;; Package: emacs[39;49;00m[37m[39;49;00m
     9	[37m[39;49;00m
    10	[37m;; This file is part of GNU Emacs.[39;49;00m[37m[39;49;00m
    11	[37m[39;49;00m
    12	[37m;; GNU Emacs is free software: you can redistribute it and/or modify[39;49;00m[37m[39;49;00m
    13	[37m;; it under the terms of the GNU General Public License as published by[39;49;00m[37m[39;49;00m
    14	[37m;; the Free Software Foundation, either version 3 of the License, or[39;49;00m[37m[39;49;00m
    15	[37m;; (at your option) any later version.[39;49;00m[37m[39;49;00m
    16	[37m[39;49;00m
    17	[37m;; GNU Emacs is distributed in the hope that it will be useful,[39;49;00m[37m[39;49;00m
    18	[37m;; but WITHOUT ANY WARRANTY; without even the implied warranty of[39;49;00m[37m[39;49;00m
    19	[37m;; MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the[39;49;00m[37m[39;49;00m
    20	[37m;; GNU General Public License for more details.[39;49;00m[37m[39;49;00m
    21	[37m[39;49;00m
    22	[37m;; You should have received a copy of the GNU General Public License[39;49;00m[37m[39;49;00m
    23	[37m;; along with GNU Emacs.  If not, see <http://www.gnu.org/licenses/>.[39;49;00m[37m[39;49;00m
    24	[37m[39;49;00m
    25	[37m;;; Commentary:[39;49;00m[37m[39;49;00m
    26	[37m[39;49;00m
    27	[37m;;; Code:[39;49;00m[37m[39;49;00m
    28	[37m[39;49;00m
    29	[37m;; Beware: while this file has tag `utf-8', before it's compiled, it gets[39;49;00m[37m[39;49;00m
    30	[37m;; loaded as "raw-text", so non-ASCII chars won't work right during bootstrap.[39;49;00m[37m[39;49;00m
    31	[37m[39;49;00m
    32	([36mdefmacro[39;49;00m[37m [39;49;00m[36mdeclare-function[39;49;00m[37m [39;49;00m([31m_fn[39;49;00m[37m [39;49;00m[31m_file[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31m_arglist[39;49;00m[37m [39;49;00m[31m_fileonly[39;49;00m)[37m[39;49;00m
    33	[37m  [39;49;00m[33m"[39;49;00m[33mTell the byte-compiler that function FN is defined, in FILE.[39;49;00m
    34	[33mOptional ARGLIST is the argument list used by the function.[39;49;00m
    35	[33mThe FILE argument is not used by the byte-compiler, but by the[39;49;00m
    36	[33m`check-declare'[39;49;00m[33m package, which checks that FILE contains a[39;49;00m
    37	[33mdefinition for FN.  ARGLIST is used by both the byte-compiler[39;49;00m
    38	[33mand [39;49;00m[33m`check-declare'[39;49;00m[33m to check for consistency.[39;49;00m
    39	[33m[39;49;00m
    40	[33mFILE can be either a Lisp file (in which case the [39;49;00m[33m\"[39;49;00m[33m.el[39;49;00m[33m\"[39;49;00m[33m[39;49;00m
    41	[33mextension is optional), or a C file.  C files are expanded[39;49;00m
    42	[33mrelative to the Emacs [39;49;00m[33m\"[39;49;00m[33msrc/[39;49;00m[33m\"[39;49;00m[33m directory.  Lisp files are[39;49;00m
    43	[33msearched for using [39;49;00m[33m`locate-library'[39;49;00m[33m, and if that fails they are[39;49;00m
    44	[33mexpanded relative to the location of the file containing the[39;49;00m
    45	[33mdeclaration.  A FILE with an [39;49;00m[33m\"[39;49;00m[33mext:[39;49;00m[33m\"[39;49;00m[33m prefix is an external file.[39;49;00m
    46	[33m`check-declare'[39;49;00m[33m will check such files if they are found, and skip[39;49;00m
    47	[33mthem without error if they are not.[39;49;00m
    48	[33m[39;49;00m
    49	[33mFILEONLY non-nil means that [39;49;00m[33m`check-declare'[39;49;00m[33m will only check that[39;49;00m
    50	[33mFILE exists, not that it defines FN.  This is intended for[39;49;00m
    51	[33mfunction-definitions that [39;49;00m[33m`check-declare'[39;49;00m[33m does not recognize, e.g.[39;49;00m
    52	[33m`defstruct'[39;49;00m[33m.[39;49;00m
    53	[33m[39;49;00m
    54	[33mTo specify a value for FILEONLY without passing an argument list,[39;49;00m
    55	[33mset ARGLIST to t.  This is necessary because nil means an[39;49;00m
    56	[33mempty argument list, rather than an unspecified one.[39;49;00m
    57	[33m[39;49;00m
    58	[33mNote that for the purposes of [39;49;00m[33m`check-declare'[39;49;00m[33m, this statement[39;49;00m
    59	[33mmust be the first non-whitespace on a line.[39;49;00m
    60	[33m[39;49;00m
    61	[33mFor more information, see Info node [39;49;00m[33m`[39;49;00m[33m(elisp)Declaring Functions'.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
    62	[37m  [39;49;00m[37m;; Does nothing - byte-compile-declare-function does the work.[39;49;00m[37m[39;49;00m
    63	[37m  [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m
    64	[37m[39;49;00m
    65	[37m[39;49;00m[37m[39;49;00m
    66	[37m;;;; Basic Lisp macros.[39;49;00m[37m[39;49;00m
    67	[37m[39;49;00m
    68	([36mdefalias[39;49;00m[37m [39;49;00m[33m'not[39;49;00m[37m [39;49;00m[33m'null[39;49;00m)[37m[39;49;00m
    69	[37m[39;49;00m
    70	([36mdefmacro[39;49;00m[37m [39;49;00m[36mnoreturn[39;49;00m[37m [39;49;00m([31mform[39;49;00m)[37m[39;49;00m
    71	[37m  [39;49;00m[33m"[39;49;00m[33mEvaluate FORM, expecting it not to return.[39;49;00m
    72	[33mIf FORM does return, signal an error.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
    73	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m
    74	[37m  [39;49;00m`([34mprog1[39;49;00m[37m [39;49;00m,[31mform[39;49;00m[37m[39;49;00m
    75	[37m     [39;49;00m([36merror[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mForm marked with [39;49;00m[33m`noreturn'[39;49;00m[33m did return[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m
    76	[37m[39;49;00m
    77	([36mdefmacro[39;49;00m[37m [39;49;00m[31m1value[39;49;00m[37m [39;49;00m([31mform[39;49;00m)[37m[39;49;00m
    78	[37m  [39;49;00m[33m"[39;49;00m[33mEvaluate FORM, expecting a constant return value.[39;49;00m
    79	[33mThis is the global do-nothing version.  There is also [39;49;00m[33m`testcover-1value'[39;49;00m[33m[39;49;00m
    80	[33mthat complains if FORM ever does return differing values.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
    81	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m
    82	[37m  [39;49;00m[31mform[39;49;00m)[37m[39;49;00m
    83	[37m[39;49;00m
    84	([36mdefmacro[39;49;00m[37m [39;49;00m[36mdef-edebug-spec[39;49;00m[37m [39;49;00m([31msymbol[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)[37m[39;49;00m
    85	[37m  [39;49;00m[33m"[39;49;00m[33mSet the [39;49;00m[33m`edebug-form-spec'[39;49;00m[33m property of SYMBOL according to SPEC.[39;49;00m
    86	[33mBoth SYMBOL and SPEC are unevaluated.  The SPEC can be:[39;49;00m
    87	[33m0 (instrument no arguments); t (instrument all arguments);[39;49;00m
    88	[33ma symbol (naming a function with an Edebug specification); or a list.[39;49;00m
    89	[33mThe elements of the list describe the argument types; see[39;49;00m
    90	[33mInfo node [39;49;00m[33m`[39;49;00m[33m(elisp)Specification List' for details.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
    91	[37m  [39;49;00m`([32mput[39;49;00m[37m [39;49;00m([34mquote[39;49;00m[37m [39;49;00m,[31msymbol[39;49;00m)[37m [39;49;00m[33m'edebug-form-spec[39;49;00m[37m [39;49;00m([34mquote[39;49;00m[37m [39;49;00m,[31mspec[39;49;00m)))[37m[39;49;00m
    92	[37m[39;49;00m
    93	([36mdefmacro[39;49;00m[37m [39;49;00m[36mlambda[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[32mcdr[39;49;00m)[37m[39;49;00m
    94	[37m  [39;49;00m[33m"[39;49;00m[33mReturn a lambda expression.[39;49;00m
    95	[33mA call of the form (lambda ARGS DOCSTRING INTERACTIVE BODY) is[39;49;00m
    96	[33mself-quoting; the result of evaluating the lambda expression is the[39;49;00m
    97	[33mexpression itself.  The lambda expression may then be treated as a[39;49;00m
    98	[33mfunction, i.e., stored as the function value of a symbol, passed to[39;49;00m
    99	[33m`funcall'[39;49;00m[33m or [39;49;00m[33m`mapcar'[39;49;00m[33m, etc.[39;49;00m
   100	[33m[39;49;00m
   101	[33mARGS should take the same form as an argument list for a [39;49;00m[33m`defun'[39;49;00m[33m.[39;49;00m
   102	[33mDOCSTRING is an optional documentation string.[39;49;00m
   103	[33m If present, it should describe how to call the function.[39;49;00m
   104	[33m But documentation strings are usually not useful in nameless functions.[39;49;00m
   105	[33mINTERACTIVE should be a call to the function [39;49;00m[33m`interactive'[39;49;00m[33m, which see.[39;49;00m
   106	[33mIt may also be omitted.[39;49;00m
   107	[33mBODY should be a list of Lisp expressions.[39;49;00m
   108	[33m[39;49;00m
   109	[33m\([39;49;00m[33mfn ARGS [DOCSTRING] [INTERACTIVE] BODY)[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   110	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdoc-string[39;49;00m[37m [39;49;00m[34m2[39;49;00m)[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[36mdefun[39;49;00m)[37m[39;49;00m
   111	[37m           [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m([31m&define[39;49;00m[37m [39;49;00m[31mlambda-list[39;49;00m[37m[39;49;00m
   112	[37m                           [39;49;00m[[34m&optional[39;49;00m[37m [39;49;00m[32mstringp[39;49;00m][37m[39;49;00m
   113	[37m                           [39;49;00m[[34m&optional[39;49;00m[37m [39;49;00m([33m"[39;49;00m[33minteractive[39;49;00m[33m"[39;49;00m[37m [39;49;00m[34minteractive[39;49;00m)][37m[39;49;00m
   114	[37m                           [39;49;00m[31mdef-body[39;49;00m)))[37m[39;49;00m
   115	[37m  [39;49;00m[37m;; Note that this definition should not use backquotes; subr.el should not[39;49;00m[37m[39;49;00m
   116	[37m  [39;49;00m[37m;; depend on backquote.el.[39;49;00m[37m[39;49;00m
   117	[37m  [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'function[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[33m'lambda[39;49;00m[37m [39;49;00m[32mcdr[39;49;00m)))[37m[39;49;00m
   118	[37m[39;49;00m
   119	([36mdefmacro[39;49;00m[37m [39;49;00m[36msetq-local[39;49;00m[37m [39;49;00m([31mvar[39;49;00m[37m [39;49;00m[31mval[39;49;00m)[37m[39;49;00m
   120	[37m  [39;49;00m[33m"[39;49;00m[33mSet variable VAR to value VAL in current buffer.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   121	[37m  [39;49;00m[37m;; Can't use backquote here, it's too early in the bootstrap.[39;49;00m[37m[39;49;00m
   122	[37m  [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'set[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'make-local-variable[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'quote[39;49;00m[37m [39;49;00m[31mvar[39;49;00m))[37m [39;49;00m[31mval[39;49;00m))[37m[39;49;00m
   123	[37m[39;49;00m
   124	([36mdefmacro[39;49;00m[37m [39;49;00m[36mdefvar-local[39;49;00m[37m [39;49;00m([31mvar[39;49;00m[37m [39;49;00m[31mval[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mdocstring[39;49;00m)[37m[39;49;00m
   125	[37m  [39;49;00m[33m"[39;49;00m[33mDefine VAR as a buffer-local variable with default value VAL.[39;49;00m
   126	[33mLike [39;49;00m[33m`defvar'[39;49;00m[33m but additionally marks the variable as being automatically[39;49;00m
   127	[33mbuffer-local wherever it is set.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   128	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[34mdefvar[39;49;00m)[37m [39;49;00m([31mdoc-string[39;49;00m[37m [39;49;00m[34m3[39;49;00m))[37m[39;49;00m
   129	[37m  [39;49;00m[37m;; Can't use backquote here, it's too early in the bootstrap.[39;49;00m[37m[39;49;00m
   130	[37m  [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'progn[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'defvar[39;49;00m[37m [39;49;00m[31mvar[39;49;00m[37m [39;49;00m[31mval[39;49;00m[37m [39;49;00m[31mdocstring[39;49;00m)[37m[39;49;00m
   131	[37m        [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'make-variable-buffer-local[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'quote[39;49;00m[37m [39;49;00m[31mvar[39;49;00m))))[37m[39;49;00m
   132	[37m[39;49;00m
   133	([36mdefun[39;49;00m[37m [39;49;00m[31mapply-partially[39;49;00m[37m [39;49;00m([31mfun[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31margs[39;49;00m)[37m[39;49;00m
   134	[37m  [39;49;00m[33m"[39;49;00m[33mReturn a function that is a partial application of FUN to ARGS.[39;49;00m
   135	[33mARGS is a list of the first N arguments to pass to FUN.[39;49;00m
   136	[33mThe result is a new function which does the same as FUN, except that[39;49;00m
   137	[33mthe first N arguments are fixed at the values with which this function[39;49;00m
   138	[33mwas called.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   139	[37m  [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31margs2[39;49;00m)[37m[39;49;00m
   140	[37m    [39;49;00m([32mapply[39;49;00m[37m [39;49;00m[31mfun[39;49;00m[37m [39;49;00m([32mappend[39;49;00m[37m [39;49;00m[31margs[39;49;00m[37m [39;49;00m[31margs2[39;49;00m))))[37m[39;49;00m
   141	[37m[39;49;00m
   142	([36mdefmacro[39;49;00m[37m [39;49;00m[36mpush[39;49;00m[37m [39;49;00m([31mnewelt[39;49;00m[37m [39;49;00m[31mplace[39;49;00m)[37m[39;49;00m
   143	[37m  [39;49;00m[33m"[39;49;00m[33mAdd NEWELT to the list stored in the generalized variable PLACE.[39;49;00m
   144	[33mThis is morally equivalent to (setf PLACE (cons NEWELT PLACE)),[39;49;00m
   145	[33mexcept that PLACE is only evaluated once (after NEWELT).[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   146	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m([31mform[39;49;00m[37m [39;49;00m[31mgv-place[39;49;00m)))[37m[39;49;00m
   147	[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32msymbolp[39;49;00m[37m [39;49;00m[31mplace[39;49;00m)[37m[39;49;00m
   148	[37m      [39;49;00m[37m;; Important special case, to avoid triggering GV too early in[39;49;00m[37m[39;49;00m
   149	[37m      [39;49;00m[37m;; the bootstrap.[39;49;00m[37m[39;49;00m
   150	[37m      [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'setq[39;49;00m[37m [39;49;00m[31mplace[39;49;00m[37m[39;49;00m
   151	[37m            [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'cons[39;49;00m[37m [39;49;00m[31mnewelt[39;49;00m[37m [39;49;00m[31mplace[39;49;00m))[37m[39;49;00m
   152	[37m    [39;49;00m([36mrequire[39;49;00m[37m [39;49;00m[33m'macroexp[39;49;00m)[37m[39;49;00m
   153	[37m    [39;49;00m([31mmacroexp-let2[39;49;00m[37m [39;49;00m[31mmacroexp-copyable-p[39;49;00m[37m [39;49;00m[31mv[39;49;00m[37m [39;49;00m[31mnewelt[39;49;00m[37m[39;49;00m
   154	[37m      [39;49;00m([31mgv-letplace[39;49;00m[37m [39;49;00m([31mgetter[39;49;00m[37m [39;49;00m[31msetter[39;49;00m)[37m [39;49;00m[31mplace[39;49;00m[37m[39;49;00m
   155	[37m        [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31msetter[39;49;00m[37m [39;49;00m`([32mcons[39;49;00m[37m [39;49;00m,[31mv[39;49;00m[37m [39;49;00m,[31mgetter[39;49;00m))))))[37m[39;49;00m
   156	[37m[39;49;00m
   157	([36mdefmacro[39;49;00m[37m [39;49;00m[36mpop[39;49;00m[37m [39;49;00m([31mplace[39;49;00m)[37m[39;49;00m
   158	[37m  [39;49;00m[33m"[39;49;00m[33mReturn the first element of PLACE's value, and remove it from the list.[39;49;00m
   159	[33mPLACE must be a generalized variable whose value is a list.[39;49;00m
   160	[33mIf the value is nil, [39;49;00m[33m`pop'[39;49;00m[33m returns nil but does not actually[39;49;00m
   161	[33mchange the list.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   162	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m([31mgv-place[39;49;00m)))[37m[39;49;00m
   163	[37m  [39;49;00m[37m;; We use `car-safe' here instead of `car' because the behavior is the same[39;49;00m[37m[39;49;00m
   164	[37m  [39;49;00m[37m;; (if it's not a cons cell, the `cdr' would have signaled an error already),[39;49;00m[37m[39;49;00m
   165	[37m  [39;49;00m[37m;; but `car-safe' is total, so the byte-compiler can safely remove it if the[39;49;00m[37m[39;49;00m
   166	[37m  [39;49;00m[37m;; result is not used.[39;49;00m[37m[39;49;00m
   167	[37m  [39;49;00m`([32mcar-safe[39;49;00m[37m[39;49;00m
   168	[37m    [39;49;00m,([34mif[39;49;00m[37m [39;49;00m([32msymbolp[39;49;00m[37m [39;49;00m[31mplace[39;49;00m)[37m[39;49;00m
   169	[37m         [39;49;00m[37m;; So we can use `pop' in the bootstrap before `gv' can be used.[39;49;00m[37m[39;49;00m
   170	[37m         [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'prog1[39;49;00m[37m [39;49;00m[31mplace[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'setq[39;49;00m[37m [39;49;00m[31mplace[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'cdr[39;49;00m[37m [39;49;00m[31mplace[39;49;00m)))[37m[39;49;00m
   171	[37m       [39;49;00m([31mgv-letplace[39;49;00m[37m [39;49;00m([31mgetter[39;49;00m[37m [39;49;00m[31msetter[39;49;00m)[37m [39;49;00m[31mplace[39;49;00m[37m[39;49;00m
   172	[37m         [39;49;00m([31mmacroexp-let2[39;49;00m[37m [39;49;00m[31mmacroexp-copyable-p[39;49;00m[37m [39;49;00m[31mx[39;49;00m[37m [39;49;00m[31mgetter[39;49;00m[37m[39;49;00m
   173	[37m           [39;49;00m`([34mprog1[39;49;00m[37m [39;49;00m,[31mx[39;49;00m[37m [39;49;00m,([32mfuncall[39;49;00m[37m [39;49;00m[31msetter[39;49;00m[37m [39;49;00m`([32mcdr[39;49;00m[37m [39;49;00m,[31mx[39;49;00m))))))))[37m[39;49;00m
   174	[37m[39;49;00m
   175	([36mdefmacro[39;49;00m[37m [39;49;00m[36mwhen[39;49;00m[37m [39;49;00m([34mcond[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m
   176	[37m  [39;49;00m[33m"[39;49;00m[33mIf COND yields non-nil, do BODY, else return nil.[39;49;00m
   177	[33mWhen COND yields non-nil, eval BODY forms sequentially and return[39;49;00m
   178	[33mvalue of last one, or nil if there are none.[39;49;00m
   179	[33m[39;49;00m
   180	[33m\([39;49;00m[33mfn COND BODY...)[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   181	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m
   182	[37m  [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'if[39;49;00m[37m [39;49;00m[34mcond[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[33m'progn[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)))[37m[39;49;00m
   183	[37m[39;49;00m
   184	([36mdefmacro[39;49;00m[37m [39;49;00m[36munless[39;49;00m[37m [39;49;00m([34mcond[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m
   185	[37m  [39;49;00m[33m"[39;49;00m[33mIf COND yields nil, do BODY, else return nil.[39;49;00m
   186	[33mWhen COND yields nil, eval BODY forms sequentially and return[39;49;00m
   187	[33mvalue of last one, or nil if there are none.[39;49;00m
   188	[33m[39;49;00m
   189	[33m\([39;49;00m[33mfn COND BODY...)[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   190	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m
   191	[37m  [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[33m'if[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[34mcond[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mbody[39;49;00m))))[37m[39;49;00m
   192	[37m[39;49;00m
   193	([36mdefmacro[39;49;00m[37m [39;49;00m[36mdolist[39;49;00m[37m [39;49;00m([31mspec[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m
   194	[37m  [39;49;00m[33m"[39;49;00m[33mLoop over a list.[39;49;00m
   195	[33mEvaluate BODY with VAR bound to each car from LIST, in turn.[39;49;00m
   196	[33mThen evaluate RESULT to get return value, default nil.[39;49;00m
   197	[33m[39;49;00m
   198	[33m\([39;49;00m[33mfn (VAR LIST [RESULT]) BODY...)[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   199	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m(([32msymbolp[39;49;00m[37m [39;49;00m[31mform[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mform[39;49;00m)[37m [39;49;00m[31mbody[39;49;00m)))[37m[39;49;00m
   200	[37m  [39;49;00m[37m;; It would be cleaner to create an uninterned symbol,[39;49;00m[37m[39;49;00m
   201	[37m  [39;49;00m[37m;; but that uses a lot more space when many functions in many files[39;49;00m[37m[39;49;00m
   202	[37m  [39;49;00m[37m;; use dolist.[39;49;00m[37m[39;49;00m
   203	[37m  [39;49;00m[37m;; FIXME: This cost disappears in byte-compiled lexical-binding files.[39;49;00m[37m[39;49;00m
   204	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtemp[39;49;00m[37m [39;49;00m[33m'--dolist-tail--[39;49;00m))[37m[39;49;00m
   205	[37m    [39;49;00m[37m;; This is not a reliable test, but it does not matter because both[39;49;00m[37m[39;49;00m
   206	[37m    [39;49;00m[37m;; semantics are acceptable, tho one is slightly faster with dynamic[39;49;00m[37m[39;49;00m
   207	[37m    [39;49;00m[37m;; scoping and the other is slightly faster (and has cleaner semantics)[39;49;00m[37m[39;49;00m
   208	[37m    [39;49;00m[37m;; with lexical scoping.[39;49;00m[37m[39;49;00m
   209	[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mlexical-binding[39;49;00m[37m[39;49;00m
   210	[37m        [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m((,[31mtemp[39;49;00m[37m [39;49;00m,([32mnth[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)))[37m[39;49;00m
   211	[37m           [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m,[31mtemp[39;49;00m[37m[39;49;00m
   212	[37m             [39;49;00m([34mlet[39;49;00m[37m [39;49;00m((,([32mcar[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m,[31mtemp[39;49;00m)))[37m[39;49;00m
   213	[37m               [39;49;00m,@[31mbody[39;49;00m[37m[39;49;00m
   214	[37m               [39;49;00m([34msetq[39;49;00m[37m [39;49;00m,[31mtemp[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m,[31mtemp[39;49;00m))))[37m[39;49;00m
   215	[37m           [39;49;00m,@([32mcdr[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)))[37m[39;49;00m
   216	[37m      [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m((,[31mtemp[39;49;00m[37m [39;49;00m,([32mnth[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mspec[39;49;00m))[37m[39;49;00m
   217	[37m             [39;49;00m,([32mcar[39;49;00m[37m [39;49;00m[31mspec[39;49;00m))[37m[39;49;00m
   218	[37m         [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m,[31mtemp[39;49;00m[37m[39;49;00m
   219	[37m           [39;49;00m([34msetq[39;49;00m[37m [39;49;00m,([32mcar[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m,[31mtemp[39;49;00m))[37m[39;49;00m
   220	[37m           [39;49;00m,@[31mbody[39;49;00m[37m[39;49;00m
   221	[37m           [39;49;00m([34msetq[39;49;00m[37m [39;49;00m,[31mtemp[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m,[31mtemp[39;49;00m)))[37m[39;49;00m
   222	[37m         [39;49;00m,@([34mif[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mspec[39;49;00m))[37m[39;49;00m
   223	[37m               [39;49;00m`(([34msetq[39;49;00m[37m [39;49;00m,([32mcar[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)[37m [39;49;00m[31mnil[39;49;00m)[37m [39;49;00m,@([32mcdr[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mspec[39;49;00m))))))))[37m[39;49;00m
   224	[37m[39;49;00m
   225	([36mdefmacro[39;49;00m[37m [39;49;00m[36mdotimes[39;49;00m[37m [39;49;00m([31mspec[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m
   226	[37m  [39;49;00m[33m"[39;49;00m[33mLoop a certain number of times.[39;49;00m
   227	[33mEvaluate BODY with VAR bound to successive integers running from 0,[39;49;00m
   228	[33minclusive, to COUNT, exclusive.  Then evaluate RESULT to get[39;49;00m
   229	[33mthe return value (nil if RESULT is omitted).[39;49;00m
   230	[33m[39;49;00m
   231	[33m\([39;49;00m[33mfn (VAR COUNT [RESULT]) BODY...)[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   232	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[36mdolist[39;49;00m))[37m[39;49;00m
   233	[37m  [39;49;00m[37m;; It would be cleaner to create an uninterned symbol,[39;49;00m[37m[39;49;00m
   234	[37m  [39;49;00m[37m;; but that uses a lot more space when many functions in many files[39;49;00m[37m[39;49;00m
   235	[37m  [39;49;00m[37m;; use dotimes.[39;49;00m[37m[39;49;00m
   236	[37m  [39;49;00m[37m;; FIXME: This cost disappears in byte-compiled lexical-binding files.[39;49;00m[37m[39;49;00m
   237	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtemp[39;49;00m[37m [39;49;00m[33m'--dotimes-limit--[39;49;00m)[37m[39;49;00m
   238	[37m	[39;49;00m([31mstart[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m
   239	[37m	[39;49;00m([31mend[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)))[37m[39;49;00m
   240	[37m    [39;49;00m[37m;; This is not a reliable test, but it does not matter because both[39;49;00m[37m[39;49;00m
   241	[37m    [39;49;00m[37m;; semantics are acceptable, tho one is slightly faster with dynamic[39;49;00m[37m[39;49;00m
   242	[37m    [39;49;00m[37m;; scoping and the other has cleaner semantics.[39;49;00m[37m[39;49;00m
   243	[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mlexical-binding[39;49;00m[37m[39;49;00m
   244	[37m        [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mcounter[39;49;00m[37m [39;49;00m[33m'--dotimes-counter--[39;49;00m))[37m[39;49;00m
   245	[37m          [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m((,[31mtemp[39;49;00m[37m [39;49;00m,[31mend[39;49;00m)[37m[39;49;00m
   246	[37m                 [39;49;00m(,[31mcounter[39;49;00m[37m [39;49;00m,[31mstart[39;49;00m))[37m[39;49;00m
   247	[37m             [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m,[31mcounter[39;49;00m[37m [39;49;00m,[31mtemp[39;49;00m)[37m[39;49;00m
   248	[37m               [39;49;00m([34mlet[39;49;00m[37m [39;49;00m((,([32mcar[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)[37m [39;49;00m,[31mcounter[39;49;00m))[37m[39;49;00m
   249	[37m                 [39;49;00m,@[31mbody[39;49;00m)[37m[39;49;00m
   250	[37m               [39;49;00m([34msetq[39;49;00m[37m [39;49;00m,[31mcounter[39;49;00m[37m [39;49;00m([32m1+[39;49;00m[37m [39;49;00m,[31mcounter[39;49;00m)))[37m[39;49;00m
   251	[37m             [39;49;00m,@([34mif[39;49;00m[37m [39;49;00m([31mcddr[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)[37m[39;49;00m
   252	[37m                   [39;49;00m[37m;; FIXME: This let often leads to "unused var" warnings.[39;49;00m[37m[39;49;00m
   253	[37m                   [39;49;00m`(([34mlet[39;49;00m[37m [39;49;00m((,([32mcar[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)[37m [39;49;00m,[31mcounter[39;49;00m))[37m [39;49;00m,@([31mcddr[39;49;00m[37m [39;49;00m[31mspec[39;49;00m))))))[37m[39;49;00m
   254	[37m      [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m((,[31mtemp[39;49;00m[37m [39;49;00m,[31mend[39;49;00m)[37m[39;49;00m
   255	[37m             [39;49;00m(,([32mcar[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)[37m [39;49;00m,[31mstart[39;49;00m))[37m[39;49;00m
   256	[37m         [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m,([32mcar[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)[37m [39;49;00m,[31mtemp[39;49;00m)[37m[39;49;00m
   257	[37m           [39;49;00m,@[31mbody[39;49;00m[37m[39;49;00m
   258	[37m           [39;49;00m([34msetq[39;49;00m[37m [39;49;00m,([32mcar[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)[37m [39;49;00m([32m1+[39;49;00m[37m [39;49;00m,([32mcar[39;49;00m[37m [39;49;00m[31mspec[39;49;00m))))[37m[39;49;00m
   259	[37m         [39;49;00m,@([32mcdr[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mspec[39;49;00m))))))[37m[39;49;00m
   260	[37m[39;49;00m
   261	([36mdefmacro[39;49;00m[37m [39;49;00m[36mdeclare[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31m_specs[39;49;00m)[37m[39;49;00m
   262	[37m  [39;49;00m[33m"[39;49;00m[33mDo not evaluate any arguments, and return nil.[39;49;00m
   263	[33mIf a [39;49;00m[33m`declare'[39;49;00m[33m form appears as the first form in the body of a[39;49;00m
   264	[33m`defun'[39;49;00m[33m or [39;49;00m[33m`defmacro'[39;49;00m[33m form, SPECS specifies various additional[39;49;00m
   265	[33minformation about the function or macro; these go into effect[39;49;00m
   266	[33mduring the evaluation of the [39;49;00m[33m`defun'[39;49;00m[33m or [39;49;00m[33m`defmacro'[39;49;00m[33m form.[39;49;00m
   267	[33m[39;49;00m
   268	[33mThe possible values of SPECS are specified by[39;49;00m
   269	[33m`defun-declarations-alist'[39;49;00m[33m and [39;49;00m[33m`macro-declarations-alist'[39;49;00m[33m.[39;49;00m
   270	[33m[39;49;00m
   271	[33mFor more information, see info node [39;49;00m[33m`[39;49;00m[33m(elisp)Declare Form'.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   272	[37m  [39;49;00m[37m;; FIXME: edebug spec should pay attention to defun-declarations-alist.[39;49;00m[37m[39;49;00m
   273	[37m  [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m
   274	[37m[39;49;00m
   275	([36mdefmacro[39;49;00m[37m [39;49;00m[36mignore-errors[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m
   276	[37m  [39;49;00m[33m"[39;49;00m[33mExecute BODY; if an error occurs, return nil.[39;49;00m
   277	[33mOtherwise, return result of last form in BODY.[39;49;00m
   278	[33mSee also [39;49;00m[33m`with-demoted-errors'[39;49;00m[33m that does something similar[39;49;00m
   279	[33mwithout silencing all errors.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   280	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m
   281	[37m  [39;49;00m`([34mcondition-case[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m([34mprogn[39;49;00m[37m [39;49;00m,@[31mbody[39;49;00m)[37m [39;49;00m([36merror[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)))[37m[39;49;00m
   282	[37m[39;49;00m[37m[39;49;00m
   283	[37m;;;; Basic Lisp functions.[39;49;00m[37m[39;49;00m
   284	[37m[39;49;00m
   285	([36mdefun[39;49;00m[37m [39;49;00m[31mignore[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31m_ignore[39;49;00m)[37m[39;49;00m
   286	[37m  [39;49;00m[33m"[39;49;00m[33mDo nothing and return nil.[39;49;00m
   287	[33mThis function accepts any number of arguments, but ignores them.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   288	[37m  [39;49;00m([34minteractive[39;49;00m)[37m[39;49;00m
   289	[37m  [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m
   290	[37m[39;49;00m
   291	[37m;; Signal a compile-error if the first arg is missing.[39;49;00m[37m[39;49;00m
   292	([36mdefun[39;49;00m[37m [39;49;00m[36merror[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31margs[39;49;00m)[37m[39;49;00m
   293	[37m  [39;49;00m[33m"[39;49;00m[33mSignal an error, making error message by passing all args to [39;49;00m[33m`format'[39;49;00m[33m.[39;49;00m
   294	[33mIn Emacs, the convention is that error messages start with a capital[39;49;00m
   295	[33mletter but *do not* end with a period.  Please follow this convention[39;49;00m
   296	[33mfor the sake of consistency.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   297	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31madvertised-calling-convention[39;49;00m[37m [39;49;00m([32mstring[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31margs[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m23.1[39;49;00m[33m"[39;49;00m))[37m[39;49;00m
   298	[37m  [39;49;00m([32msignal[39;49;00m[37m [39;49;00m[33m'error[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m([32mapply[39;49;00m[37m [39;49;00m[33m'format[39;49;00m[37m [39;49;00m[31margs[39;49;00m))))[37m[39;49;00m
   299	[37m[39;49;00m
   300	([36mdefun[39;49;00m[37m [39;49;00m[36muser-error[39;49;00m[37m [39;49;00m([32mformat[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31margs[39;49;00m)[37m[39;49;00m
   301	[37m  [39;49;00m[33m"[39;49;00m[33mSignal a pilot error, making error message by passing all args to [39;49;00m[33m`format'[39;49;00m[33m.[39;49;00m
   302	[33mIn Emacs, the convention is that error messages start with a capital[39;49;00m
   303	[33mletter but *do not* end with a period.  Please follow this convention[39;49;00m
   304	[33mfor the sake of consistency.[39;49;00m
   305	[33mThis is just like [39;49;00m[33m`error'[39;49;00m[33m except that [39;49;00m[33m`user-error'[39;49;00m[33ms are expected to be the[39;49;00m
   306	[33mresult of an incorrect manipulation on the part of the user, rather than the[39;49;00m
   307	[33mresult of an actual problem.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   308	[37m  [39;49;00m([32msignal[39;49;00m[37m [39;49;00m[33m'user-error[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m([32mapply[39;49;00m[37m [39;49;00m[32m#'[39;49;00m[32mformat[39;49;00m[37m [39;49;00m[32mformat[39;49;00m[37m [39;49;00m[31margs[39;49;00m))))[37m[39;49;00m
   309	[37m[39;49;00m
   310	([36mdefun[39;49;00m[37m [39;49;00m[31mdefine-error[39;49;00m[37m [39;49;00m([31mname[39;49;00m[37m [39;49;00m[32mmessage[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mparent[39;49;00m)[37m[39;49;00m
   311	[37m  [39;49;00m[33m"[39;49;00m[33mDefine NAME as a new error signal.[39;49;00m
   312	[33mMESSAGE is a string that will be output to the echo area if such an error[39;49;00m
   313	[33mis signaled without being caught by a [39;49;00m[33m`condition-case'[39;49;00m[33m.[39;49;00m
   314	[33mPARENT is either a signal or a list of signals from which it inherits.[39;49;00m
   315	[33mDefaults to [39;49;00m[33m`error'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   316	[37m  [39;49;00m([36munless[39;49;00m[37m [39;49;00m[31mparent[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mparent[39;49;00m[37m [39;49;00m[33m'error[39;49;00m))[37m[39;49;00m
   317	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mconditions[39;49;00m[37m[39;49;00m
   318	[37m         [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mparent[39;49;00m)[37m[39;49;00m
   319	[37m             [39;49;00m([32mapply[39;49;00m[37m [39;49;00m[32m#'[39;49;00m[32mappend[39;49;00m[37m[39;49;00m
   320	[37m                    [39;49;00m([32mmapcar[39;49;00m[37m [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31mparent[39;49;00m)[37m[39;49;00m
   321	[37m                              [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mparent[39;49;00m[37m[39;49;00m
   322	[37m                                    [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mget[39;49;00m[37m [39;49;00m[31mparent[39;49;00m[37m [39;49;00m[33m'error-conditions[39;49;00m)[37m[39;49;00m
   323	[37m                                        [39;49;00m([36merror[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mUnknown signal [39;49;00m[33m`%s'[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mparent[39;49;00m))))[37m[39;49;00m
   324	[37m                            [39;49;00m[31mparent[39;49;00m))[37m[39;49;00m
   325	[37m           [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mparent[39;49;00m[37m [39;49;00m([32mget[39;49;00m[37m [39;49;00m[31mparent[39;49;00m[37m [39;49;00m[33m'error-conditions[39;49;00m)))))[37m[39;49;00m
   326	[37m    [39;49;00m([32mput[39;49;00m[37m [39;49;00m[31mname[39;49;00m[37m [39;49;00m[33m'error-conditions[39;49;00m[37m[39;49;00m
   327	[37m         [39;49;00m([31mdelete-dups[39;49;00m[37m [39;49;00m([32mcopy-sequence[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mname[39;49;00m[37m [39;49;00m[31mconditions[39;49;00m))))[37m[39;49;00m
   328	[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[32mmessage[39;49;00m[37m [39;49;00m([32mput[39;49;00m[37m [39;49;00m[31mname[39;49;00m[37m [39;49;00m[33m'error-message[39;49;00m[37m [39;49;00m[32mmessage[39;49;00m))))[37m[39;49;00m
   329	[37m[39;49;00m
   330	[37m;; We put this here instead of in frame.el so that it's defined even on[39;49;00m[37m[39;49;00m
   331	[37m;; systems where frame.el isn't loaded.[39;49;00m[37m[39;49;00m
   332	([36mdefun[39;49;00m[37m [39;49;00m[31mframe-configuration-p[39;49;00m[37m [39;49;00m([31mobject[39;49;00m)[37m[39;49;00m
   333	[37m  [39;49;00m[33m"[39;49;00m[33mReturn non-nil if OBJECT seems to be a frame configuration.[39;49;00m
   334	[33mAny list whose car is [39;49;00m[33m`frame-configuration'[39;49;00m[33m is assumed to be a frame[39;49;00m
   335	[33mconfiguration.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   336	[37m  [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mobject[39;49;00m)[37m[39;49;00m
   337	[37m       [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mobject[39;49;00m)[37m [39;49;00m[33m'frame-configuration[39;49;00m)))[37m[39;49;00m
   338	[37m[39;49;00m
   339	[37m[39;49;00m[37m[39;49;00m
   340	[37m;;;; List functions.[39;49;00m[37m[39;49;00m
   341	[37m[39;49;00m
   342	([36mdefsubst[39;49;00m[37m [39;49;00m[31mcaar[39;49;00m[37m [39;49;00m([31mx[39;49;00m)[37m[39;49;00m
   343	[37m  [39;49;00m[33m"[39;49;00m[33mReturn the car of the car of X.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   344	[37m  [39;49;00m([32mcar[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mx[39;49;00m)))[37m[39;49;00m
   345	[37m[39;49;00m
   346	([36mdefsubst[39;49;00m[37m [39;49;00m[31mcadr[39;49;00m[37m [39;49;00m([31mx[39;49;00m)[37m[39;49;00m
   347	[37m  [39;49;00m[33m"[39;49;00m[33mReturn the car of the cdr of X.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   348	[37m  [39;49;00m([32mcar[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mx[39;49;00m)))[37m[39;49;00m
   349	[37m[39;49;00m
   350	([36mdefsubst[39;49;00m[37m [39;49;00m[31mcdar[39;49;00m[37m [39;49;00m([31mx[39;49;00m)[37m[39;49;00m
   351	[37m  [39;49;00m[33m"[39;49;00m[33mReturn the cdr of the car of X.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   352	[37m  [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mx[39;49;00m)))[37m[39;49;00m
   353	[37m[39;49;00m
   354	([36mdefsubst[39;49;00m[37m [39;49;00m[31mcddr[39;49;00m[37m [39;49;00m([31mx[39;49;00m)[37m[39;49;00m
   355	[37m  [39;49;00m[33m"[39;49;00m[33mReturn the cdr of the cdr of X.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   356	[37m  [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mx[39;49;00m)))[37m[39;49;00m
   357	[37m[39;49;00m
   358	([36mdefun[39;49;00m[37m [39;49;00m[31mlast[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mn[39;49;00m)[37m[39;49;00m
   359	[37m  [39;49;00m[33m"[39;49;00m[33mReturn the last link of LIST.  Its car is the last element.[39;49;00m
   360	[33mIf LIST is nil, return nil.[39;49;00m
   361	[33mIf N is non-nil, return the Nth-to-last link of LIST.[39;49;00m
   362	[33mIf N is bigger than the length of LIST, return LIST.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   363	[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mn[39;49;00m[37m[39;49;00m
   364	[37m      [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32m>=[39;49;00m[37m [39;49;00m[31mn[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m
   365	[37m           [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mm[39;49;00m[37m [39;49;00m([32msafe-length[39;49;00m[37m [39;49;00m[32mlist[39;49;00m)))[37m[39;49;00m
   366	[37m             [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m[31mn[39;49;00m[37m [39;49;00m[31mm[39;49;00m)[37m [39;49;00m([32mnthcdr[39;49;00m[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m[31mm[39;49;00m[37m [39;49;00m[31mn[39;49;00m)[37m [39;49;00m[32mlist[39;49;00m)[37m [39;49;00m[32mlist[39;49;00m)))[37m[39;49;00m
   367	[37m    [39;49;00m([34mand[39;49;00m[37m [39;49;00m[32mlist[39;49;00m[37m[39;49;00m
   368	[37m         [39;49;00m([32mnthcdr[39;49;00m[37m [39;49;00m([32m1-[39;49;00m[37m [39;49;00m([32msafe-length[39;49;00m[37m [39;49;00m[32mlist[39;49;00m))[37m [39;49;00m[32mlist[39;49;00m))))[37m[39;49;00m
   369	[37m[39;49;00m
   370	([36mdefun[39;49;00m[37m [39;49;00m[31mbutlast[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mn[39;49;00m)[37m[39;49;00m
   371	[37m  [39;49;00m[33m"[39;49;00m[33mReturn a copy of LIST with the last N elements removed.[39;49;00m
   372	[33mIf N is omitted or nil, the last element is removed from the[39;49;00m
   373	[33mcopy.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   374	[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mn[39;49;00m[37m [39;49;00m([32m<=[39;49;00m[37m [39;49;00m[31mn[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m [39;49;00m[32mlist[39;49;00m[37m[39;49;00m
   375	[37m    [39;49;00m([31mnbutlast[39;49;00m[37m [39;49;00m([32mcopy-sequence[39;49;00m[37m [39;49;00m[32mlist[39;49;00m)[37m [39;49;00m[31mn[39;49;00m)))[37m[39;49;00m
   376	[37m[39;49;00m
   377	([36mdefun[39;49;00m[37m [39;49;00m[31mnbutlast[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mn[39;49;00m)[37m[39;49;00m
   378	[37m  [39;49;00m[33m"[39;49;00m[33mModifies LIST to remove the last N elements.[39;49;00m
   379	[33mIf N is omitted or nil, remove the last element.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   380	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mm[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[32mlist[39;49;00m)))[37m[39;49;00m
   381	[37m    [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mn[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mn[39;49;00m[37m [39;49;00m[34m1[39;49;00m))[37m[39;49;00m
   382	[37m    [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m[31mn[39;49;00m[37m [39;49;00m[31mm[39;49;00m)[37m[39;49;00m
   383	[37m	 [39;49;00m([34mprogn[39;49;00m[37m[39;49;00m
   384	[37m	   [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m[31mn[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m([32msetcdr[39;49;00m[37m [39;49;00m([32mnthcdr[39;49;00m[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m([32m1-[39;49;00m[37m [39;49;00m[31mm[39;49;00m)[37m [39;49;00m[31mn[39;49;00m)[37m [39;49;00m[32mlist[39;49;00m)[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m
   385	[37m	   [39;49;00m[32mlist[39;49;00m))))[37m[39;49;00m
   386	[37m[39;49;00m
   387	([36mdefun[39;49;00m[37m [39;49;00m[31mzerop[39;49;00m[37m [39;49;00m([31mnumber[39;49;00m)[37m[39;49;00m
   388	[37m  [39;49;00m[33m"[39;49;00m[33mReturn t if NUMBER is zero.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   389	[37m  [39;49;00m[37m;; Used to be in C, but it's pointless since (= 0 n) is faster anyway because[39;49;00m[37m[39;49;00m
   390	[37m  [39;49;00m[37m;; = has a byte-code.[39;49;00m[37m[39;49;00m
   391	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mcompiler-macro[39;49;00m[37m [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31m_[39;49;00m)[37m [39;49;00m`([32m=[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m,[31mnumber[39;49;00m))))[37m[39;49;00m
   392	[37m  [39;49;00m([32m=[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[31mnumber[39;49;00m))[37m[39;49;00m
   393	[37m[39;49;00m
   394	([36mdefun[39;49;00m[37m [39;49;00m[31mdelete-dups[39;49;00m[37m [39;49;00m([32mlist[39;49;00m)[37m[39;49;00m
   395	[37m  [39;49;00m[33m"[39;49;00m[33mDestructively remove [39;49;00m[33m`equal'[39;49;00m[33m duplicates from LIST.[39;49;00m
   396	[33mStore the result in LIST and return it.  LIST must be a proper list.[39;49;00m
   397	[33mOf several [39;49;00m[33m`equal'[39;49;00m[33m occurrences of an element in LIST, the first[39;49;00m
   398	[33mone is kept.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   399	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtail[39;49;00m[37m [39;49;00m[32mlist[39;49;00m))[37m[39;49;00m
   400	[37m    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m[39;49;00m
   401	[37m      [39;49;00m([32msetcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([32mdelete[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)))[37m[39;49;00m
   402	[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))))[37m[39;49;00m
   403	[37m  [39;49;00m[32mlist[39;49;00m)[37m[39;49;00m
   404	[37m[39;49;00m
   405	[37m;; See http://lists.gnu.org/archive/html/emacs-devel/2013-05/msg00204.html[39;49;00m[37m[39;49;00m
   406	([36mdefun[39;49;00m[37m [39;49;00m[31mdelete-consecutive-dups[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mcircular[39;49;00m)[37m[39;49;00m
   407	[37m  [39;49;00m[33m"[39;49;00m[33mDestructively remove [39;49;00m[33m`equal'[39;49;00m[33m consecutive duplicates from LIST.[39;49;00m
   408	[33mFirst and last elements are considered consecutive if CIRCULAR is[39;49;00m
   409	[33mnon-nil.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   410	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtail[39;49;00m[37m [39;49;00m[32mlist[39;49;00m)[37m [39;49;00m[31mlast[39;49;00m)[37m[39;49;00m
   411	[37m    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)[37m[39;49;00m
   412	[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mequal[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)[37m [39;49;00m([31mcadr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))[37m[39;49;00m
   413	[37m	  [39;49;00m([32msetcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([31mcddr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))[37m[39;49;00m
   414	[37m	[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mlast[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)[37m[39;49;00m
   415	[37m	      [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))))[37m[39;49;00m
   416	[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mcircular[39;49;00m[37m[39;49;00m
   417	[37m	     [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[32mlist[39;49;00m)[37m[39;49;00m
   418	[37m	     [39;49;00m([32mequal[39;49;00m[37m [39;49;00m[31mlast[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[32mlist[39;49;00m)))[37m[39;49;00m
   419	[37m	[39;49;00m([31mnbutlast[39;49;00m[37m [39;49;00m[32mlist[39;49;00m)[37m[39;49;00m
   420	[37m      [39;49;00m[32mlist[39;49;00m)))[37m[39;49;00m
   421	[37m[39;49;00m
   422	([36mdefun[39;49;00m[37m [39;49;00m[31mnumber-sequence[39;49;00m[37m [39;49;00m([31mfrom[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mto[39;49;00m[37m [39;49;00m[31minc[39;49;00m)[37m[39;49;00m
   423	[37m  [39;49;00m[33m"[39;49;00m[33mReturn a sequence of numbers from FROM to TO (both inclusive) as a list.[39;49;00m
   424	[33mINC is the increment used between numbers in the sequence and defaults to 1.[39;49;00m
   425	[33mSo, the Nth element of the list is (+ FROM (* N INC)) where N counts from[39;49;00m
   426	[33mzero.  TO is only included if there is an N for which TO = FROM + N * INC.[39;49;00m
   427	[33mIf TO is nil or numerically equal to FROM, return (FROM).[39;49;00m
   428	[33mIf INC is positive and TO is less than FROM, or INC is negative[39;49;00m
   429	[33mand TO is larger than FROM, return nil.[39;49;00m
   430	[33mIf INC is zero and TO is neither nil nor numerically equal to[39;49;00m
   431	[33mFROM, signal an error.[39;49;00m
   432	[33m[39;49;00m
   433	[33mThis function is primarily designed for integer arguments.[39;49;00m
   434	[33mNevertheless, FROM, TO and INC can be integer or float.  However,[39;49;00m
   435	[33mfloating point arithmetic is inexact.  For instance, depending on[39;49;00m
   436	[33mthe machine, it may quite well happen that[39;49;00m
   437	[33m\([39;49;00m[33mnumber-sequence 0.4 0.6 0.2) returns the one element list (0.4),[39;49;00m
   438	[33mwhereas (number-sequence 0.4 0.8 0.2) returns a list with three[39;49;00m
   439	[33melements.  Thus, if some of the arguments are floats and one wants[39;49;00m
   440	[33mto make sure that TO is included, one may have to explicitly write[39;49;00m
   441	[33mTO as (+ FROM (* N INC)) or use a variable whose value was[39;49;00m
   442	[33mcomputed with this exact expression.  Alternatively, you can,[39;49;00m
   443	[33mof course, also replace TO with a slightly larger value[39;49;00m
   444	[33m\([39;49;00m[33mor a slightly more negative value if INC is negative).[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   445	[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m[31mto[39;49;00m)[37m [39;49;00m([32m=[39;49;00m[37m [39;49;00m[31mfrom[39;49;00m[37m [39;49;00m[31mto[39;49;00m))[37m[39;49;00m
   446	[37m      [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[31mfrom[39;49;00m)[37m[39;49;00m
   447	[37m    [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31minc[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31minc[39;49;00m[37m [39;49;00m[34m1[39;49;00m))[37m[39;49;00m
   448	[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([31mzerop[39;49;00m[37m [39;49;00m[31minc[39;49;00m)[37m [39;49;00m([36merror[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mThe increment can not be zero[39;49;00m[33m"[39;49;00m))[37m[39;49;00m
   449	[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m([31mseq[39;49;00m[37m [39;49;00m([31mn[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m([31mnext[39;49;00m[37m [39;49;00m[31mfrom[39;49;00m))[37m[39;49;00m
   450	[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m[31minc[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m
   451	[37m          [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32m<=[39;49;00m[37m [39;49;00m[31mnext[39;49;00m[37m [39;49;00m[31mto[39;49;00m)[37m[39;49;00m
   452	[37m            [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mseq[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mnext[39;49;00m[37m [39;49;00m[31mseq[39;49;00m)[37m[39;49;00m
   453	[37m                  [39;49;00m[31mn[39;49;00m[37m [39;49;00m([32m1+[39;49;00m[37m [39;49;00m[31mn[39;49;00m)[37m[39;49;00m
   454	[37m                  [39;49;00m[31mnext[39;49;00m[37m [39;49;00m([32m+[39;49;00m[37m [39;49;00m[31mfrom[39;49;00m[37m [39;49;00m([32m*[39;49;00m[37m [39;49;00m[31mn[39;49;00m[37m [39;49;00m[31minc[39;49;00m))))[37m[39;49;00m
   455	[37m        [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32m>=[39;49;00m[37m [39;49;00m[31mnext[39;49;00m[37m [39;49;00m[31mto[39;49;00m)[37m[39;49;00m
   456	[37m          [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mseq[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mnext[39;49;00m[37m [39;49;00m[31mseq[39;49;00m)[37m[39;49;00m
   457	[37m                [39;49;00m[31mn[39;49;00m[37m [39;49;00m([32m1+[39;49;00m[37m [39;49;00m[31mn[39;49;00m)[37m[39;49;00m
   458	[37m                [39;49;00m[31mnext[39;49;00m[37m [39;49;00m([32m+[39;49;00m[37m [39;49;00m[31mfrom[39;49;00m[37m [39;49;00m([32m*[39;49;00m[37m [39;49;00m[31mn[39;49;00m[37m [39;49;00m[31minc[39;49;00m)))))[37m[39;49;00m
   459	[37m      [39;49;00m([32mnreverse[39;49;00m[37m [39;49;00m[31mseq[39;49;00m))))[37m[39;49;00m
   460	[37m[39;49;00m
   461	([36mdefun[39;49;00m[37m [39;49;00m[31mcopy-tree[39;49;00m[37m [39;49;00m([31mtree[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mvecp[39;49;00m)[37m[39;49;00m
   462	[37m  [39;49;00m[33m"[39;49;00m[33mMake a copy of TREE.[39;49;00m
   463	[33mIf TREE is a cons cell, this recursively copies both its car and its cdr.[39;49;00m
   464	[33mContrast to [39;49;00m[33m`copy-sequence'[39;49;00m[33m, which copies only along the cdrs.  With second[39;49;00m
   465	[33margument VECP, this copies vectors as well as conses.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   466	[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mtree[39;49;00m)[37m[39;49;00m
   467	[37m      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m([31mresult[39;49;00m)[37m[39;49;00m
   468	[37m	[39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mtree[39;49;00m)[37m[39;49;00m
   469	[37m	  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mnewcar[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mtree[39;49;00m)))[37m[39;49;00m
   470	[37m	    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mtree[39;49;00m))[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mvecp[39;49;00m[37m [39;49;00m([32mvectorp[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mtree[39;49;00m))))[37m[39;49;00m
   471	[37m		[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mnewcar[39;49;00m[37m [39;49;00m([31mcopy-tree[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mtree[39;49;00m)[37m [39;49;00m[31mvecp[39;49;00m)))[37m[39;49;00m
   472	[37m	    [39;49;00m([36mpush[39;49;00m[37m [39;49;00m[31mnewcar[39;49;00m[37m [39;49;00m[31mresult[39;49;00m))[37m[39;49;00m
   473	[37m	  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mtree[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtree[39;49;00m)))[37m[39;49;00m
   474	[37m	[39;49;00m([32mnconc[39;49;00m[37m [39;49;00m([32mnreverse[39;49;00m[37m [39;49;00m[31mresult[39;49;00m)[37m [39;49;00m[31mtree[39;49;00m))[37m[39;49;00m
   475	[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mvecp[39;49;00m[37m [39;49;00m([32mvectorp[39;49;00m[37m [39;49;00m[31mtree[39;49;00m))[37m[39;49;00m
   476	[37m	[39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mi[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mtree[39;49;00m[37m [39;49;00m([32mcopy-sequence[39;49;00m[37m [39;49;00m[31mtree[39;49;00m)))))[37m[39;49;00m
   477	[37m	  [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32m>=[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mi[39;49;00m[37m [39;49;00m([32m1-[39;49;00m[37m [39;49;00m[31mi[39;49;00m))[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m
   478	[37m	    [39;49;00m([32maset[39;49;00m[37m [39;49;00m[31mtree[39;49;00m[37m [39;49;00m[31mi[39;49;00m[37m [39;49;00m([31mcopy-tree[39;49;00m[37m [39;49;00m([32maref[39;49;00m[37m [39;49;00m[31mtree[39;49;00m[37m [39;49;00m[31mi[39;49;00m)[37m [39;49;00m[31mvecp[39;49;00m)))[37m[39;49;00m
   479	[37m	  [39;49;00m[31mtree[39;49;00m)[37m[39;49;00m
   480	[37m      [39;49;00m[31mtree[39;49;00m)))[37m[39;49;00m
   481	[37m[39;49;00m[37m[39;49;00m
   482	[37m;;;; Various list-search functions.[39;49;00m[37m[39;49;00m
   483	[37m[39;49;00m
   484	([36mdefun[39;49;00m[37m [39;49;00m[31massoc-default[39;49;00m[37m [39;49;00m([31mkey[39;49;00m[37m [39;49;00m[31malist[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mtest[39;49;00m[37m [39;49;00m[31mdefault[39;49;00m)[37m[39;49;00m
   485	[37m  [39;49;00m[33m"[39;49;00m[33mFind object KEY in a pseudo-alist ALIST.[39;49;00m
   486	[33mALIST is a list of conses or objects.  Each element[39;49;00m
   487	[33m (or the element's car, if it is a cons) is compared with KEY by[39;49;00m
   488	[33m calling TEST, with two arguments: (i) the element or its car,[39;49;00m
   489	[33m and (ii) KEY.[39;49;00m
   490	[33mIf that is non-nil, the element matches; then [39;49;00m[33m`assoc-default'[39;49;00m[33m[39;49;00m
   491	[33m returns the element's cdr, if it is a cons, or DEFAULT if the[39;49;00m
   492	[33m element is not a cons.[39;49;00m
   493	[33m[39;49;00m
   494	[33mIf no element matches, the value is nil.[39;49;00m
   495	[33mIf TEST is omitted or nil, [39;49;00m[33m`equal'[39;49;00m[33m is used.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   496	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m([31mfound[39;49;00m[37m [39;49;00m([31mtail[39;49;00m[37m [39;49;00m[31malist[39;49;00m)[37m [39;49;00m[31mvalue[39;49;00m)[37m[39;49;00m
   497	[37m    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m[31mfound[39;49;00m))[37m[39;49;00m
   498	[37m      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([32melt[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)))[37m[39;49;00m
   499	[37m	[39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mtest[39;49;00m[37m [39;49;00m[33m'equal[39;49;00m)[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[32melt[39;49;00m)[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[32melt[39;49;00m)[37m [39;49;00m[32melt[39;49;00m)[37m [39;49;00m[31mkey[39;49;00m)[37m[39;49;00m
   500	[37m	  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mfound[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m[31mvalue[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[32melt[39;49;00m)[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[32melt[39;49;00m)[37m [39;49;00m[31mdefault[39;49;00m))))[37m[39;49;00m
   501	[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)))[37m[39;49;00m
   502	[37m    [39;49;00m[31mvalue[39;49;00m))[37m[39;49;00m
   503	[37m[39;49;00m
   504	([36mdefun[39;49;00m[37m [39;49;00m[31massoc-ignore-case[39;49;00m[37m [39;49;00m([31mkey[39;49;00m[37m [39;49;00m[31malist[39;49;00m)[37m[39;49;00m
   505	[37m  [39;49;00m[33m"[39;49;00m[33mLike [39;49;00m[33m`assoc'[39;49;00m[33m, but ignores differences in case and text representation.[39;49;00m
   506	[33mKEY must be a string.  Upper-case and lower-case letters are treated as equal.[39;49;00m
   507	[33mUnibyte strings are converted to multibyte for comparison.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   508	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mobsolete[39;49;00m[37m [39;49;00m[32massoc-string[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m22.1[39;49;00m[33m"[39;49;00m))[37m[39;49;00m
   509	[37m  [39;49;00m([32massoc-string[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m[31malist[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m
   510	[37m[39;49;00m
   511	([36mdefun[39;49;00m[37m [39;49;00m[31massoc-ignore-representation[39;49;00m[37m [39;49;00m([31mkey[39;49;00m[37m [39;49;00m[31malist[39;49;00m)[37m[39;49;00m
   512	[37m  [39;49;00m[33m"[39;49;00m[33mLike [39;49;00m[33m`assoc'[39;49;00m[33m, but ignores differences in text representation.[39;49;00m
   513	[33mKEY must be a string.[39;49;00m
   514	[33mUnibyte strings are converted to multibyte for comparison.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   515	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mobsolete[39;49;00m[37m [39;49;00m[32massoc-string[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m22.1[39;49;00m[33m"[39;49;00m))[37m[39;49;00m
   516	[37m  [39;49;00m([32massoc-string[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m[31malist[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m
   517	[37m[39;49;00m
   518	([36mdefun[39;49;00m[37m [39;49;00m[31mmember-ignore-case[39;49;00m[37m [39;49;00m([32melt[39;49;00m[37m [39;49;00m[32mlist[39;49;00m)[37m[39;49;00m
   519	[37m  [39;49;00m[33m"[39;49;00m[33mLike [39;49;00m[33m`member'[39;49;00m[33m, but ignore differences in case and text representation.[39;49;00m
   520	[33mELT must be a string.  Upper-case and lower-case letters are treated as equal.[39;49;00m
   521	[33mUnibyte strings are converted to multibyte for comparison.[39;49;00m
   522	[33mNon-strings in LIST are ignored.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   523	[37m  [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[32mlist[39;49;00m[37m[39;49;00m
   524	[37m	      [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[32mlist[39;49;00m))[37m[39;49;00m
   525	[37m			[39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m([32mcompare-strings[39;49;00m[37m [39;49;00m[32melt[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[32mlist[39;49;00m)[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mt[39;49;00m)))))[37m[39;49;00m
   526	[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[32mlist[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[32mlist[39;49;00m)))[37m[39;49;00m
   527	[37m  [39;49;00m[32mlist[39;49;00m)[37m[39;49;00m
   528	[37m[39;49;00m
   529	([36mdefun[39;49;00m[37m [39;49;00m[31massq-delete-all[39;49;00m[37m [39;49;00m([31mkey[39;49;00m[37m [39;49;00m[31malist[39;49;00m)[37m[39;49;00m
   530	[37m  [39;49;00m[33m"[39;49;00m[33mDelete from ALIST all elements whose car is [39;49;00m[33m`eq'[39;49;00m[33m to KEY.[39;49;00m
   531	[33mReturn the modified alist.[39;49;00m
   532	[33mElements of ALIST that are not conses are ignored.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   533	[37m  [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31malist[39;49;00m))[37m[39;49;00m
   534	[37m	      [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31malist[39;49;00m))[37m [39;49;00m[31mkey[39;49;00m))[37m[39;49;00m
   535	[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31malist[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31malist[39;49;00m)))[37m[39;49;00m
   536	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtail[39;49;00m[37m [39;49;00m[31malist[39;49;00m)[37m [39;49;00m[31mtail-cdr[39;49;00m)[37m[39;49;00m
   537	[37m    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mtail-cdr[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))[37m[39;49;00m
   538	[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mtail-cdr[39;49;00m))[37m[39;49;00m
   539	[37m	       [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mtail-cdr[39;49;00m))[37m [39;49;00m[31mkey[39;49;00m))[37m[39;49;00m
   540	[37m	  [39;49;00m([32msetcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail-cdr[39;49;00m))[37m[39;49;00m
   541	[37m	[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m[31mtail-cdr[39;49;00m))))[37m[39;49;00m
   542	[37m  [39;49;00m[31malist[39;49;00m)[37m[39;49;00m
   543	[37m[39;49;00m
   544	([36mdefun[39;49;00m[37m [39;49;00m[31mrassq-delete-all[39;49;00m[37m [39;49;00m([31mvalue[39;49;00m[37m [39;49;00m[31malist[39;49;00m)[37m[39;49;00m
   545	[37m  [39;49;00m[33m"[39;49;00m[33mDelete from ALIST all elements whose cdr is [39;49;00m[33m`eq'[39;49;00m[33m to VALUE.[39;49;00m
   546	[33mReturn the modified alist.[39;49;00m
   547	[33mElements of ALIST that are not conses are ignored.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   548	[37m  [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31malist[39;49;00m))[37m[39;49;00m
   549	[37m	      [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31malist[39;49;00m))[37m [39;49;00m[31mvalue[39;49;00m))[37m[39;49;00m
   550	[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31malist[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31malist[39;49;00m)))[37m[39;49;00m
   551	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtail[39;49;00m[37m [39;49;00m[31malist[39;49;00m)[37m [39;49;00m[31mtail-cdr[39;49;00m)[37m[39;49;00m
   552	[37m    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mtail-cdr[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))[37m[39;49;00m
   553	[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mtail-cdr[39;49;00m))[37m[39;49;00m
   554	[37m	       [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mtail-cdr[39;49;00m))[37m [39;49;00m[31mvalue[39;49;00m))[37m[39;49;00m
   555	[37m	  [39;49;00m([32msetcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail-cdr[39;49;00m))[37m[39;49;00m
   556	[37m	[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m[31mtail-cdr[39;49;00m))))[37m[39;49;00m
   557	[37m  [39;49;00m[31malist[39;49;00m)[37m[39;49;00m
   558	[37m[39;49;00m
   559	([36mdefun[39;49;00m[37m [39;49;00m[31malist-get[39;49;00m[37m [39;49;00m([31mkey[39;49;00m[37m [39;49;00m[31malist[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mdefault[39;49;00m[37m [39;49;00m[31mremove[39;49;00m)[37m[39;49;00m
   560	[37m  [39;49;00m[33m"[39;49;00m[33mGet the value associated to KEY in ALIST.[39;49;00m
   561	[33mDEFAULT is the value to return if KEY is not found in ALIST.[39;49;00m
   562	[33mREMOVE, if non-nil, means that when setting this element, we should[39;49;00m
   563	[33mremove the entry if the new value is [39;49;00m[33m`eql'[39;49;00m[33m to DEFAULT.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   564	[37m  [39;49;00m([31mignore[39;49;00m[37m [39;49;00m[31mremove[39;49;00m)[37m [39;49;00m[37m;;Silence byte-compiler.[39;49;00m[37m[39;49;00m
   565	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mx[39;49;00m[37m [39;49;00m([32massq[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m[31malist[39;49;00m)))[37m[39;49;00m
   566	[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mx[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mx[39;49;00m)[37m [39;49;00m[31mdefault[39;49;00m)))[37m[39;49;00m
   567	[37m[39;49;00m
   568	([36mdefun[39;49;00m[37m [39;49;00m[31mremove[39;49;00m[37m [39;49;00m([32melt[39;49;00m[37m [39;49;00m[31mseq[39;49;00m)[37m[39;49;00m
   569	[37m  [39;49;00m[33m"[39;49;00m[33mReturn a copy of SEQ with all occurrences of ELT removed.[39;49;00m
   570	[33mSEQ must be a list, vector, or string.  The comparison is done with [39;49;00m[33m`equal'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   571	[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mnlistp[39;49;00m[37m [39;49;00m[31mseq[39;49;00m)[37m[39;49;00m
   572	[37m      [39;49;00m[37m;; If SEQ isn't a list, there's no need to copy SEQ because[39;49;00m[37m[39;49;00m
   573	[37m      [39;49;00m[37m;; `delete' will return a new object.[39;49;00m[37m[39;49;00m
   574	[37m      [39;49;00m([32mdelete[39;49;00m[37m [39;49;00m[32melt[39;49;00m[37m [39;49;00m[31mseq[39;49;00m)[37m[39;49;00m
   575	[37m    [39;49;00m([32mdelete[39;49;00m[37m [39;49;00m[32melt[39;49;00m[37m [39;49;00m([32mcopy-sequence[39;49;00m[37m [39;49;00m[31mseq[39;49;00m))))[37m[39;49;00m
   576	[37m[39;49;00m
   577	([36mdefun[39;49;00m[37m [39;49;00m[31mremq[39;49;00m[37m [39;49;00m([32melt[39;49;00m[37m [39;49;00m[32mlist[39;49;00m)[37m[39;49;00m
   578	[37m  [39;49;00m[33m"[39;49;00m[33mReturn LIST with all occurrences of ELT removed.[39;49;00m
   579	[33mThe comparison is done with [39;49;00m[33m`eq'[39;49;00m[33m.  Contrary to [39;49;00m[33m`delq'[39;49;00m[33m, this does not use[39;49;00m
   580	[33mside-effects, and the argument LIST is not modified.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   581	[37m  [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[32melt[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[32mlist[39;49;00m))[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[32mlist[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[32mlist[39;49;00m))))[37m[39;49;00m
   582	[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[32melt[39;49;00m[37m [39;49;00m[32mlist[39;49;00m)[37m[39;49;00m
   583	[37m      [39;49;00m([32mdelq[39;49;00m[37m [39;49;00m[32melt[39;49;00m[37m [39;49;00m([32mcopy-sequence[39;49;00m[37m [39;49;00m[32mlist[39;49;00m))[37m[39;49;00m
   584	[37m    [39;49;00m[32mlist[39;49;00m))[37m[39;49;00m
   585	[37m[39;49;00m[37m[39;49;00m
   586	[37m;;;; Keymap support.[39;49;00m[37m[39;49;00m
   587	[37m[39;49;00m
   588	([36mdefun[39;49;00m[37m [39;49;00m[31mkbd[39;49;00m[37m [39;49;00m([31mkeys[39;49;00m)[37m[39;49;00m
   589	[37m  [39;49;00m[33m"[39;49;00m[33mConvert KEYS to the internal Emacs key representation.[39;49;00m
   590	[33mKEYS should be a string constant in the format used for[39;49;00m
   591	[33msaving keyboard macros (see [39;49;00m[33m`edmacro-mode'[39;49;00m[33m).[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   592	[37m  [39;49;00m[37m;; Don't use a defalias, since the `pure' property is only true for[39;49;00m[37m[39;49;00m
   593	[37m  [39;49;00m[37m;; the calling convention of `kbd'.[39;49;00m[37m[39;49;00m
   594	[37m  [39;49;00m([31mread-kbd-macro[39;49;00m[37m [39;49;00m[31mkeys[39;49;00m))[37m[39;49;00m
   595	([32mput[39;49;00m[37m [39;49;00m[33m'kbd[39;49;00m[37m [39;49;00m[33m'pure[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m
   596	[37m[39;49;00m
   597	([36mdefun[39;49;00m[37m [39;49;00m[31mundefined[39;49;00m[37m [39;49;00m()[37m[39;49;00m
   598	[37m  [39;49;00m[33m"[39;49;00m[33mBeep to tell the user this binding is undefined.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   599	[37m  [39;49;00m([34minteractive[39;49;00m)[37m[39;49;00m
   600	[37m  [39;49;00m([32mding[39;49;00m)[37m[39;49;00m
   601	[37m  [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m%s is undefined[39;49;00m[33m"[39;49;00m[37m [39;49;00m([32mkey-description[39;49;00m[37m [39;49;00m([32mthis-single-command-keys[39;49;00m)))[37m[39;49;00m
   602	[37m  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mdefining-kbd-macro[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m
   603	[37m  [39;49;00m([32mforce-mode-line-update[39;49;00m)[37m[39;49;00m
   604	[37m  [39;49;00m[37m;; If this is a down-mouse event, don't reset prefix-arg;[39;49;00m[37m[39;49;00m
   605	[37m  [39;49;00m[37m;; pass it to the command run by the up event.[39;49;00m[37m[39;49;00m
   606	[37m  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mprefix-arg[39;49;00m[37m[39;49;00m
   607	[37m        [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[33m'down[39;49;00m[37m [39;49;00m([31mevent-modifiers[39;49;00m[37m [39;49;00m[31mlast-command-event[39;49;00m))[37m[39;49;00m
   608	[37m          [39;49;00m[31mcurrent-prefix-arg[39;49;00m)))[37m[39;49;00m
   609	[37m[39;49;00m
   610	[37m;; Prevent the \{...} documentation construct[39;49;00m[37m[39;49;00m
   611	[37m;; from mentioning keys that run this command.[39;49;00m[37m[39;49;00m
   612	([32mput[39;49;00m[37m [39;49;00m[33m'undefined[39;49;00m[37m [39;49;00m[33m'suppress-keymap[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m
   613	[37m[39;49;00m
   614	([36mdefun[39;49;00m[37m [39;49;00m[31msuppress-keymap[39;49;00m[37m [39;49;00m([31mmap[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mnodigits[39;49;00m)[37m[39;49;00m
   615	[37m  [39;49;00m[33m"[39;49;00m[33mMake MAP override all normally self-inserting keys to be undefined.[39;49;00m
   616	[33mNormally, as an exception, digits and minus-sign are set to make prefix args,[39;49;00m
   617	[33mbut optional second arg NODIGITS non-nil treats them like other chars.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   618	[37m  [39;49;00m([32mdefine-key[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m[[31mremap[39;49;00m[37m [39;49;00m[32mself-insert-command[39;49;00m][37m [39;49;00m[33m'undefined[39;49;00m)[37m[39;49;00m
   619	[37m  [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mnodigits[39;49;00m[37m[39;49;00m
   620	[37m      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m([36mloop[39;49;00m)[37m[39;49;00m
   621	[37m	[39;49;00m([32mdefine-key[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m-[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m'negative-argument[39;49;00m)[37m[39;49;00m
   622	[37m	[39;49;00m[37m;; Make plain numbers do numeric args.[39;49;00m[37m[39;49;00m
   623	[37m	[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[36mloop[39;49;00m[37m [39;49;00m[33m?0[39;49;00m)[37m[39;49;00m
   624	[37m	[39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32m<=[39;49;00m[37m [39;49;00m[36mloop[39;49;00m[37m [39;49;00m[33m?9[39;49;00m)[37m[39;49;00m
   625	[37m	  [39;49;00m([32mdefine-key[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m([32mchar-to-string[39;49;00m[37m [39;49;00m[36mloop[39;49;00m)[37m [39;49;00m[33m'digit-argument[39;49;00m)[37m[39;49;00m
   626	[37m	  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[36mloop[39;49;00m[37m [39;49;00m([32m1+[39;49;00m[37m [39;49;00m[36mloop[39;49;00m))))))[37m[39;49;00m
   627	[37m[39;49;00m
   628	([36mdefun[39;49;00m[37m [39;49;00m[31mmake-composed-keymap[39;49;00m[37m [39;49;00m([31mmaps[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mparent[39;49;00m)[37m[39;49;00m
   629	[37m  [39;49;00m[33m"[39;49;00m[33mConstruct a new keymap composed of MAPS and inheriting from PARENT.[39;49;00m
   630	[33mWhen looking up a key in the returned map, the key is looked in each[39;49;00m
   631	[33mkeymap of MAPS in turn until a binding is found.[39;49;00m
   632	[33mIf no binding is found in MAPS, the lookup continues in PARENT, if non-nil.[39;49;00m
   633	[33mAs always with keymap inheritance, a nil binding in MAPS overrides[39;49;00m
   634	[33many corresponding binding in PARENT, but it does not override corresponding[39;49;00m
   635	[33mbindings in other keymaps of MAPS.[39;49;00m
   636	[33mMAPS can be a list of keymaps or a single keymap.[39;49;00m
   637	[33mPARENT if non-nil should be a keymap.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   638	[37m  [39;49;00m`([31mkeymap[39;49;00m[37m[39;49;00m
   639	[37m    [39;49;00m,@([34mif[39;49;00m[37m [39;49;00m([32mkeymapp[39;49;00m[37m [39;49;00m[31mmaps[39;49;00m)[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[31mmaps[39;49;00m)[37m [39;49;00m[31mmaps[39;49;00m)[37m[39;49;00m
   640	[37m    [39;49;00m,@[31mparent[39;49;00m))[37m[39;49;00m
   641	[37m[39;49;00m
   642	([36mdefun[39;49;00m[37m [39;49;00m[31mdefine-key-after[39;49;00m[37m [39;49;00m([31mkeymap[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m[31mdefinition[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mafter[39;49;00m)[37m[39;49;00m
   643	[37m  [39;49;00m[33m"[39;49;00m[33mAdd binding in KEYMAP for KEY => DEFINITION, right after AFTER's binding.[39;49;00m
   644	[33mThis is like [39;49;00m[33m`define-key'[39;49;00m[33m except that the binding for KEY is placed[39;49;00m
   645	[33mjust after the binding for the event AFTER, instead of at the beginning[39;49;00m
   646	[33mof the map.  Note that AFTER must be an event type (like KEY), NOT a command[39;49;00m
   647	[33m\([39;49;00m[33mlike DEFINITION).[39;49;00m
   648	[33m[39;49;00m
   649	[33mIf AFTER is t or omitted, the new binding goes at the end of the keymap.[39;49;00m
   650	[33mAFTER should be a single event type--a symbol or a character, not a sequence.[39;49;00m
   651	[33m[39;49;00m
   652	[33mBindings are always added before any inherited map.[39;49;00m
   653	[33m[39;49;00m
   654	[33mThe order of bindings in a keymap only matters when it is used as[39;49;00m
   655	[33ma menu, so this function is not useful for non-menu keymaps.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   656	[37m  [39;49;00m([36munless[39;49;00m[37m [39;49;00m[31mafter[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mafter[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m
   657	[37m  [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mkeymapp[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m)[37m[39;49;00m
   658	[37m      [39;49;00m([32msignal[39;49;00m[37m [39;49;00m[33m'wrong-type-argument[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'keymapp[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m)))[37m[39;49;00m
   659	[37m  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m[39;49;00m
   660	[37m	[39;49;00m([34mif[39;49;00m[37m [39;49;00m([32m<=[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31mkey[39;49;00m)[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m([32maref[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m
   661	[37m	  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m[37m [39;49;00m([32mlookup-key[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m[37m[39;49;00m
   662	[37m				   [39;49;00m([32mapply[39;49;00m[37m [39;49;00m[33m'vector[39;49;00m[37m[39;49;00m
   663	[37m					  [39;49;00m([31mbutlast[39;49;00m[37m [39;49;00m([32mmapcar[39;49;00m[37m [39;49;00m[33m'identity[39;49;00m[37m [39;49;00m[31mkey[39;49;00m)))))[37m[39;49;00m
   664	[37m	  [39;49;00m([32maref[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m([32m1-[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31mkey[39;49;00m)))))[37m[39;49;00m
   665	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtail[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m)[37m [39;49;00m[31mdone[39;49;00m[37m [39;49;00m[31minserted[39;49;00m)[37m[39;49;00m
   666	[37m    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m[31mdone[39;49;00m)[37m [39;49;00m[31mtail[39;49;00m)[37m[39;49;00m
   667	[37m      [39;49;00m[37m;; Delete any earlier bindings for the same key.[39;49;00m[37m[39;49;00m
   668	[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mcar-safe[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)))[37m [39;49;00m[31mkey[39;49;00m)[37m[39;49;00m
   669	[37m	  [39;49;00m([32msetcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))))[37m[39;49;00m
   670	[37m      [39;49;00m[37m;; If we hit an included map, go down that one.[39;49;00m[37m[39;49;00m
   671	[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mkeymapp[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)))[37m[39;49;00m
   672	[37m      [39;49;00m[37m;; When we reach AFTER's binding, insert the new binding after.[39;49;00m[37m[39;49;00m
   673	[37m      [39;49;00m[37m;; If we reach an inherited keymap, insert just before that.[39;49;00m[37m[39;49;00m
   674	[37m      [39;49;00m[37m;; If we reach the end of this keymap, insert at the end.[39;49;00m[37m[39;49;00m
   675	[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mcar-safe[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))[37m [39;49;00m[31mafter[39;49;00m)[37m[39;49;00m
   676	[37m		   [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mafter[39;49;00m[37m [39;49;00m[31mt[39;49;00m)))[37m[39;49;00m
   677	[37m	      [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))[37m [39;49;00m[33m'keymap[39;49;00m)[37m[39;49;00m
   678	[37m	      [39;49;00m([32mnull[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)))[37m[39;49;00m
   679	[37m	  [39;49;00m([34mprogn[39;49;00m[37m[39;49;00m
   680	[37m	    [39;49;00m[37m;; Stop the scan only if we find a parent keymap.[39;49;00m[37m[39;49;00m
   681	[37m	    [39;49;00m[37m;; Keep going past the inserted element[39;49;00m[37m[39;49;00m
   682	[37m	    [39;49;00m[37m;; so we can delete any duplications that come later.[39;49;00m[37m[39;49;00m
   683	[37m	    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))[37m [39;49;00m[33m'keymap[39;49;00m)[37m[39;49;00m
   684	[37m		[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mdone[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m
   685	[37m	    [39;49;00m[37m;; Don't insert more than once.[39;49;00m[37m[39;49;00m
   686	[37m	    [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31minserted[39;49;00m[37m[39;49;00m
   687	[37m		[39;49;00m([32msetcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m[31mdefinition[39;49;00m)[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))))[37m[39;49;00m
   688	[37m	    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31minserted[39;49;00m[37m [39;49;00m[31mt[39;49;00m)))[37m[39;49;00m
   689	[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)))))[37m[39;49;00m
   690	[37m[39;49;00m
   691	([36mdefun[39;49;00m[37m [39;49;00m[31mmap-keymap-sorted[39;49;00m[37m [39;49;00m([34mfunction[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m)[37m[39;49;00m
   692	[37m  [39;49;00m[33m"[39;49;00m[33mImplement [39;49;00m[33m`map-keymap'[39;49;00m[33m with sorting.[39;49;00m
   693	[33mDon't call this function; it is for internal use only.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   694	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m([32mlist[39;49;00m)[37m[39;49;00m
   695	[37m    [39;49;00m([32mmap-keymap[39;49;00m[37m [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31ma[39;49;00m[37m [39;49;00m[31mb[39;49;00m)[37m [39;49;00m([36mpush[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31ma[39;49;00m[37m [39;49;00m[31mb[39;49;00m)[37m [39;49;00m[32mlist[39;49;00m))[37m[39;49;00m
   696	[37m                [39;49;00m[31mkeymap[39;49;00m)[37m[39;49;00m
   697	[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[32mlist[39;49;00m[37m [39;49;00m([32msort[39;49;00m[37m [39;49;00m[32mlist[39;49;00m[37m[39;49;00m
   698	[37m                     [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31ma[39;49;00m[37m [39;49;00m[31mb[39;49;00m)[37m[39;49;00m
   699	[37m                       [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31ma[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31ma[39;49;00m)[37m [39;49;00m[31mb[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mb[39;49;00m))[37m[39;49;00m
   700	[37m                       [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mintegerp[39;49;00m[37m [39;49;00m[31ma[39;49;00m)[37m[39;49;00m
   701	[37m                           [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mintegerp[39;49;00m[37m [39;49;00m[31mb[39;49;00m)[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m[31ma[39;49;00m[37m [39;49;00m[31mb[39;49;00m)[37m[39;49;00m
   702	[37m                             [39;49;00m[31mt[39;49;00m)[37m[39;49;00m
   703	[37m                         [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mintegerp[39;49;00m[37m [39;49;00m[31mb[39;49;00m)[37m [39;49;00m[31mt[39;49;00m[37m[39;49;00m
   704	[37m                           [39;49;00m[37m;; string< also accepts symbols.[39;49;00m[37m[39;49;00m
   705	[37m                           [39;49;00m([32mstring<[39;49;00m[37m [39;49;00m[31ma[39;49;00m[37m [39;49;00m[31mb[39;49;00m))))))[37m[39;49;00m
   706	[37m    [39;49;00m([36mdolist[39;49;00m[37m [39;49;00m([31mp[39;49;00m[37m [39;49;00m[32mlist[39;49;00m)[37m[39;49;00m
   707	[37m      [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[34mfunction[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mp[39;49;00m)[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mp[39;49;00m)))))[37m[39;49;00m
   708	[37m[39;49;00m
   709	([36mdefun[39;49;00m[37m [39;49;00m[31mkeymap--menu-item-binding[39;49;00m[37m [39;49;00m([31mval[39;49;00m)[37m[39;49;00m
   710	[37m  [39;49;00m[33m"[39;49;00m[33mReturn the binding part of a menu-item.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   711	[37m  [39;49;00m([34mcond[39;49;00m[37m[39;49;00m
   712	[37m   [39;49;00m(([31mnot[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mval[39;49;00m))[37m [39;49;00m[31mval[39;49;00m)[37m              [39;49;00m[37m;Not a menu-item.[39;49;00m[37m[39;49;00m
   713	[37m   [39;49;00m(([32meq[39;49;00m[37m [39;49;00m[33m'menu-item[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mval[39;49;00m))[37m[39;49;00m
   714	[37m    [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mbinding[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m[31mval[39;49;00m))[37m[39;49;00m
   715	[37m           [39;49;00m([31mplist[39;49;00m[37m [39;49;00m([32mnthcdr[39;49;00m[37m [39;49;00m[34m3[39;49;00m[37m [39;49;00m[31mval[39;49;00m))[37m[39;49;00m
   716	[37m           [39;49;00m([31mfilter[39;49;00m[37m [39;49;00m([32mplist-get[39;49;00m[37m [39;49;00m[31mplist[39;49;00m[37m [39;49;00m[36m:filter[39;49;00m)))[37m[39;49;00m
   717	[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mfilter[39;49;00m[37m [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mfilter[39;49;00m[37m [39;49;00m[31mbinding[39;49;00m)[37m[39;49;00m
   718	[37m        [39;49;00m[31mbinding[39;49;00m)))[37m[39;49;00m
   719	[37m   [39;49;00m(([34mand[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mval[39;49;00m))[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m([31mcadr[39;49;00m[37m [39;49;00m[31mval[39;49;00m)))[37m[39;49;00m
   720	[37m    [39;49;00m([31mcddr[39;49;00m[37m [39;49;00m[31mval[39;49;00m))[37m[39;49;00m
   721	[37m   [39;49;00m(([32mstringp[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mval[39;49;00m))[37m[39;49;00m
   722	[37m    [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mval[39;49;00m))[37m[39;49;00m
   723	[37m   [39;49;00m([31mt[39;49;00m[37m [39;49;00m[31mval[39;49;00m)))[37m                            [39;49;00m[37m;Not a menu-item either.[39;49;00m[37m[39;49;00m
   724	[37m[39;49;00m
   725	([36mdefun[39;49;00m[37m [39;49;00m[31mkeymap--menu-item-with-binding[39;49;00m[37m [39;49;00m([31mitem[39;49;00m[37m [39;49;00m[31mbinding[39;49;00m)[37m[39;49;00m
   726	[37m  [39;49;00m[33m"[39;49;00m[33mBuild a menu-item like ITEM but with its binding changed to BINDING.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   727	[37m  [39;49;00m([34mcond[39;49;00m[37m[39;49;00m
   728	[37m   [39;49;00m(([31mnot[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mitem[39;49;00m))[37m [39;49;00m[31mbinding[39;49;00m)[37m		[39;49;00m[37m;Not a menu-item.[39;49;00m[37m[39;49;00m
   729	[37m   [39;49;00m(([32meq[39;49;00m[37m [39;49;00m[33m'menu-item[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mitem[39;49;00m))[37m[39;49;00m
   730	[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mitem[39;49;00m[37m [39;49;00m([32mcopy-sequence[39;49;00m[37m [39;49;00m[31mitem[39;49;00m))[37m[39;49;00m
   731	[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtail[39;49;00m[37m [39;49;00m([32mnthcdr[39;49;00m[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m[31mitem[39;49;00m)))[37m[39;49;00m
   732	[37m      [39;49;00m([32msetcar[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m[31mbinding[39;49;00m)[37m[39;49;00m
   733	[37m      [39;49;00m[37m;; Remove any potential filter.[39;49;00m[37m[39;49;00m
   734	[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mplist-get[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)[37m [39;49;00m[36m:filter[39;49;00m)[37m[39;49;00m
   735	[37m          [39;49;00m([32msetcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([32mplist-put[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)[37m [39;49;00m[36m:filter[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))))[37m[39;49;00m
   736	[37m    [39;49;00m[31mitem[39;49;00m)[37m[39;49;00m
   737	[37m   [39;49;00m(([34mand[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mitem[39;49;00m))[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m([31mcadr[39;49;00m[37m [39;49;00m[31mitem[39;49;00m)))[37m[39;49;00m
   738	[37m    [39;49;00m([32mcons[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mitem[39;49;00m)[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m([31mcadr[39;49;00m[37m [39;49;00m[31mitem[39;49;00m)[37m [39;49;00m[31mbinding[39;49;00m)))[37m[39;49;00m
   739	[37m   [39;49;00m([31mt[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mitem[39;49;00m)[37m [39;49;00m[31mbinding[39;49;00m))))[37m[39;49;00m
   740	[37m[39;49;00m
   741	([36mdefun[39;49;00m[37m [39;49;00m[31mkeymap--merge-bindings[39;49;00m[37m [39;49;00m([31mval1[39;49;00m[37m [39;49;00m[31mval2[39;49;00m)[37m[39;49;00m
   742	[37m  [39;49;00m[33m"[39;49;00m[33mMerge bindings VAL1 and VAL2.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   743	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mmap1[39;49;00m[37m [39;49;00m([31mkeymap--menu-item-binding[39;49;00m[37m [39;49;00m[31mval1[39;49;00m))[37m[39;49;00m
   744	[37m        [39;49;00m([31mmap2[39;49;00m[37m [39;49;00m([31mkeymap--menu-item-binding[39;49;00m[37m [39;49;00m[31mval2[39;49;00m)))[37m[39;49;00m
   745	[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mkeymapp[39;49;00m[37m [39;49;00m[31mmap1[39;49;00m)[37m [39;49;00m([32mkeymapp[39;49;00m[37m [39;49;00m[31mmap2[39;49;00m)))[37m[39;49;00m
   746	[37m        [39;49;00m[37m;; There's nothing to merge: val1 takes precedence.[39;49;00m[37m[39;49;00m
   747	[37m        [39;49;00m[31mval1[39;49;00m[37m[39;49;00m
   748	[37m      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mmap[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'keymap[39;49;00m[37m [39;49;00m[31mmap1[39;49;00m[37m [39;49;00m[31mmap2[39;49;00m))[37m[39;49;00m
   749	[37m            [39;49;00m([31mitem[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mkeymapp[39;49;00m[37m [39;49;00m[31mval1[39;49;00m)[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mkeymapp[39;49;00m[37m [39;49;00m[31mval2[39;49;00m)[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mval2[39;49;00m)[37m [39;49;00m[31mval1[39;49;00m)))[37m[39;49;00m
   750	[37m        [39;49;00m([31mkeymap--menu-item-with-binding[39;49;00m[37m [39;49;00m[31mitem[39;49;00m[37m [39;49;00m[31mmap[39;49;00m)))))[37m[39;49;00m
   751	[37m[39;49;00m
   752	([36mdefun[39;49;00m[37m [39;49;00m[31mkeymap-canonicalize[39;49;00m[37m [39;49;00m([31mmap[39;49;00m)[37m[39;49;00m
   753	[37m  [39;49;00m[33m"[39;49;00m[33mReturn a simpler equivalent keymap.[39;49;00m
   754	[33mThis resolves inheritance and redefinitions.  The returned keymap[39;49;00m
   755	[33mshould behave identically to a copy of KEYMAP w.r.t [39;49;00m[33m`lookup-key'[39;49;00m[33m[39;49;00m
   756	[33mand use in active keymaps and menus.[39;49;00m
   757	[33mSubkeymaps may be modified but are not canonicalized.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   758	[37m  [39;49;00m[37m;; FIXME: Problem with the difference between a nil binding[39;49;00m[37m[39;49;00m
   759	[37m  [39;49;00m[37m;; that hides a binding in an inherited map and a nil binding that's ignored[39;49;00m[37m[39;49;00m
   760	[37m  [39;49;00m[37m;; to let some further binding visible.  Currently a nil binding hides all.[39;49;00m[37m[39;49;00m
   761	[37m  [39;49;00m[37m;; FIXME: we may want to carefully (re)order elements in case they're[39;49;00m[37m[39;49;00m
   762	[37m  [39;49;00m[37m;; menu-entries.[39;49;00m[37m[39;49;00m
   763	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mbindings[39;49;00m[37m [39;49;00m())[37m[39;49;00m
   764	[37m        [39;49;00m([31mranges[39;49;00m[37m [39;49;00m())[37m[39;49;00m
   765	[37m	[39;49;00m([31mprompt[39;49;00m[37m [39;49;00m([32mkeymap-prompt[39;49;00m[37m [39;49;00m[31mmap[39;49;00m)))[37m[39;49;00m
   766	[37m    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32mkeymapp[39;49;00m[37m [39;49;00m[31mmap[39;49;00m)[37m[39;49;00m
   767	[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m([32mmap-keymap[39;49;00m[37m [39;49;00m[37m;; -internal[39;49;00m[37m[39;49;00m
   768	[37m                 [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31mkey[39;49;00m[37m [39;49;00m[31mitem[39;49;00m)[37m[39;49;00m
   769	[37m                   [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mkey[39;49;00m)[37m[39;49;00m
   770	[37m                       [39;49;00m[37m;; Treat char-ranges specially.[39;49;00m[37m[39;49;00m
   771	[37m                       [39;49;00m([36mpush[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m[31mitem[39;49;00m)[37m [39;49;00m[31mranges[39;49;00m)[37m[39;49;00m
   772	[37m                     [39;49;00m([36mpush[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m[31mitem[39;49;00m)[37m [39;49;00m[31mbindings[39;49;00m)))[37m[39;49;00m
   773	[37m                 [39;49;00m[31mmap[39;49;00m)))[37m[39;49;00m
   774	[37m    [39;49;00m[37m;; Create the new map.[39;49;00m[37m[39;49;00m
   775	[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mranges[39;49;00m[37m [39;49;00m[33m'make-keymap[39;49;00m[37m [39;49;00m[33m'make-sparse-keymap[39;49;00m)[37m [39;49;00m[31mprompt[39;49;00m))[37m[39;49;00m
   776	[37m    [39;49;00m([36mdolist[39;49;00m[37m [39;49;00m([31mbinding[39;49;00m[37m [39;49;00m[31mranges[39;49;00m)[37m[39;49;00m
   777	[37m      [39;49;00m[37m;; Treat char-ranges specially.  FIXME: need to merge as well.[39;49;00m[37m[39;49;00m
   778	[37m      [39;49;00m([32mdefine-key[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m([32mvector[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mbinding[39;49;00m))[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mbinding[39;49;00m)))[37m[39;49;00m
   779	[37m    [39;49;00m[37m;; Process the bindings starting from the end.[39;49;00m[37m[39;49;00m
   780	[37m    [39;49;00m([36mdolist[39;49;00m[37m [39;49;00m([31mbinding[39;49;00m[37m [39;49;00m([34mprog1[39;49;00m[37m [39;49;00m[31mbindings[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbindings[39;49;00m[37m [39;49;00m())))[37m[39;49;00m
   781	[37m      [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mkey[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mbinding[39;49;00m))[37m[39;49;00m
   782	[37m             [39;49;00m([31moldbind[39;49;00m[37m [39;49;00m([32massq[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m[31mbindings[39;49;00m)))[37m[39;49;00m
   783	[37m        [39;49;00m([36mpush[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m[31moldbind[39;49;00m)[37m[39;49;00m
   784	[37m                  [39;49;00m[37m;; The normal case: no duplicate bindings.[39;49;00m[37m[39;49;00m
   785	[37m                  [39;49;00m[31mbinding[39;49;00m[37m[39;49;00m
   786	[37m                [39;49;00m[37m;; This is the second binding for this key.[39;49;00m[37m[39;49;00m
   787	[37m                [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbindings[39;49;00m[37m [39;49;00m([32mdelq[39;49;00m[37m [39;49;00m[31moldbind[39;49;00m[37m [39;49;00m[31mbindings[39;49;00m))[37m[39;49;00m
   788	[37m                [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m([31mkeymap--merge-bindings[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mbinding[39;49;00m)[37m[39;49;00m
   789	[37m                                                  [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31moldbind[39;49;00m))))[37m[39;49;00m
   790	[37m              [39;49;00m[31mbindings[39;49;00m)))[37m[39;49;00m
   791	[37m    [39;49;00m([32mnconc[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m[31mbindings[39;49;00m)))[37m[39;49;00m
   792	[37m[39;49;00m
   793	([32mput[39;49;00m[37m [39;49;00m[33m'keyboard-translate-table[39;49;00m[37m [39;49;00m[33m'char-table-extra-slots[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m
   794	[37m[39;49;00m
   795	([36mdefun[39;49;00m[37m [39;49;00m[31mkeyboard-translate[39;49;00m[37m [39;49;00m([31mfrom[39;49;00m[37m [39;49;00m[31mto[39;49;00m)[37m[39;49;00m
   796	[37m  [39;49;00m[33m"[39;49;00m[33mTranslate character FROM to TO on the current terminal.[39;49;00m
   797	[33mThis function creates a [39;49;00m[33m`keyboard-translate-table'[39;49;00m[33m if necessary[39;49;00m
   798	[33mand then modifies one entry in it.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   799	[37m  [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mchar-table-p[39;49;00m[37m [39;49;00m[31mkeyboard-translate-table[39;49;00m)[37m[39;49;00m
   800	[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mkeyboard-translate-table[39;49;00m[37m[39;49;00m
   801	[37m	    [39;49;00m([32mmake-char-table[39;49;00m[37m [39;49;00m[33m'keyboard-translate-table[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)))[37m[39;49;00m
   802	[37m  [39;49;00m([32maset[39;49;00m[37m [39;49;00m[31mkeyboard-translate-table[39;49;00m[37m [39;49;00m[31mfrom[39;49;00m[37m [39;49;00m[31mto[39;49;00m))[37m[39;49;00m
   803	[37m[39;49;00m[37m[39;49;00m
   804	[37m;;;; Key binding commands.[39;49;00m[37m[39;49;00m
   805	[37m[39;49;00m
   806	([36mdefun[39;49;00m[37m [39;49;00m[31mglobal-set-key[39;49;00m[37m [39;49;00m([31mkey[39;49;00m[37m [39;49;00m[31mcommand[39;49;00m)[37m[39;49;00m
   807	[37m  [39;49;00m[33m"[39;49;00m[33mGive KEY a global binding as COMMAND.[39;49;00m
   808	[33mCOMMAND is the command definition to use; usually it is[39;49;00m
   809	[33ma symbol naming an interactively-callable function.[39;49;00m
   810	[33mKEY is a key sequence; noninteractively, it is a string or vector[39;49;00m
   811	[33mof characters or event types, and non-ASCII characters with codes[39;49;00m
   812	[33mabove 127 (such as ISO Latin-1) can be included if you use a vector.[39;49;00m
   813	[33m[39;49;00m
   814	[33mNote that if KEY has a local binding in the current buffer,[39;49;00m
   815	[33mthat local binding will continue to shadow any global binding[39;49;00m
   816	[33mthat you make with this function.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   817	[37m  [39;49;00m([34minteractive[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mKSet key globally: [39;49;00m[33m\n[39;49;00m[33mCSet key %s to command: [39;49;00m[33m"[39;49;00m)[37m[39;49;00m
   818	[37m  [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mvectorp[39;49;00m[37m [39;49;00m[31mkey[39;49;00m)[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m[31mkey[39;49;00m)[37m[39;49;00m
   819	[37m      [39;49;00m([32msignal[39;49;00m[37m [39;49;00m[33m'wrong-type-argument[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'arrayp[39;49;00m[37m [39;49;00m[31mkey[39;49;00m)))[37m[39;49;00m
   820	[37m  [39;49;00m([32mdefine-key[39;49;00m[37m [39;49;00m([32mcurrent-global-map[39;49;00m)[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m[31mcommand[39;49;00m))[37m[39;49;00m
   821	[37m[39;49;00m
   822	([36mdefun[39;49;00m[37m [39;49;00m[31mlocal-set-key[39;49;00m[37m [39;49;00m([31mkey[39;49;00m[37m [39;49;00m[31mcommand[39;49;00m)[37m[39;49;00m
   823	[37m  [39;49;00m[33m"[39;49;00m[33mGive KEY a local binding as COMMAND.[39;49;00m
   824	[33mCOMMAND is the command definition to use; usually it is[39;49;00m
   825	[33ma symbol naming an interactively-callable function.[39;49;00m
   826	[33mKEY is a key sequence; noninteractively, it is a string or vector[39;49;00m
   827	[33mof characters or event types, and non-ASCII characters with codes[39;49;00m
   828	[33mabove 127 (such as ISO Latin-1) can be included if you use a vector.[39;49;00m
   829	[33m[39;49;00m
   830	[33mThe binding goes in the current buffer's local map, which in most[39;49;00m
   831	[33mcases is shared with all other buffers in the same major mode.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   832	[37m  [39;49;00m([34minteractive[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mKSet key locally: [39;49;00m[33m\n[39;49;00m[33mCSet key %s locally to command: [39;49;00m[33m"[39;49;00m)[37m[39;49;00m
   833	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mmap[39;49;00m[37m [39;49;00m([32mcurrent-local-map[39;49;00m)))[37m[39;49;00m
   834	[37m    [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m[39;49;00m
   835	[37m	[39;49;00m([32muse-local-map[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m([32mmake-sparse-keymap[39;49;00m))))[37m[39;49;00m
   836	[37m    [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mvectorp[39;49;00m[37m [39;49;00m[31mkey[39;49;00m)[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m[31mkey[39;49;00m)[37m[39;49;00m
   837	[37m	[39;49;00m([32msignal[39;49;00m[37m [39;49;00m[33m'wrong-type-argument[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'arrayp[39;49;00m[37m [39;49;00m[31mkey[39;49;00m)))[37m[39;49;00m
   838	[37m    [39;49;00m([32mdefine-key[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m[31mcommand[39;49;00m)))[37m[39;49;00m
   839	[37m[39;49;00m
   840	([36mdefun[39;49;00m[37m [39;49;00m[31mglobal-unset-key[39;49;00m[37m [39;49;00m([31mkey[39;49;00m)[37m[39;49;00m
   841	[37m  [39;49;00m[33m"[39;49;00m[33mRemove global binding of KEY.[39;49;00m
   842	[33mKEY is a string or vector representing a sequence of keystrokes.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   843	[37m  [39;49;00m([34minteractive[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mkUnset key globally: [39;49;00m[33m"[39;49;00m)[37m[39;49;00m
   844	[37m  [39;49;00m([31mglobal-set-key[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m
   845	[37m[39;49;00m
   846	([36mdefun[39;49;00m[37m [39;49;00m[31mlocal-unset-key[39;49;00m[37m [39;49;00m([31mkey[39;49;00m)[37m[39;49;00m
   847	[37m  [39;49;00m[33m"[39;49;00m[33mRemove local binding of KEY.[39;49;00m
   848	[33mKEY is a string or vector representing a sequence of keystrokes.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   849	[37m  [39;49;00m([34minteractive[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mkUnset key locally: [39;49;00m[33m"[39;49;00m)[37m[39;49;00m
   850	[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mcurrent-local-map[39;49;00m)[37m[39;49;00m
   851	[37m      [39;49;00m([31mlocal-set-key[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m
   852	[37m  [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m
   853	[37m[39;49;00m[37m[39;49;00m
   854	[37m;;;; substitute-key-definition and its subroutines.[39;49;00m[37m[39;49;00m
   855	[37m[39;49;00m
   856	([34mdefvar[39;49;00m[37m [39;49;00m[31mkey-substitution-in-progress[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m
   857	[37m  [39;49;00m[33m"[39;49;00m[33mUsed internally by [39;49;00m[33m`substitute-key-definition'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
   858	[37m[39;49;00m
   859	([36mdefun[39;49;00m[37m [39;49;00m[31msubstitute-key-definition[39;49;00m[37m [39;49;00m([31molddef[39;49;00m[37m [39;49;00m[31mnewdef[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31moldmap[39;49;00m[37m [39;49;00m[31mprefix[39;49;00m)[37m[39;49;00m
   860	[37m  [39;49;00m[33m"[39;49;00m[33mReplace OLDDEF with NEWDEF for any keys in KEYMAP now defined as OLDDEF.[39;49;00m
   861	[33mIn other words, OLDDEF is replaced with NEWDEF where ever it appears.[39;49;00m
   862	[33mAlternatively, if optional fourth argument OLDMAP is specified, we redefine[39;49;00m
   863	[33min KEYMAP as NEWDEF those keys which are defined as OLDDEF in OLDMAP.[39;49;00m
   864	[33m[39;49;00m
   865	[33mIf you don't specify OLDMAP, you can usually get the same results[39;49;00m
   866	[33min a cleaner way with command remapping, like this:[39;49;00m
   867	[33m  (define-key KEYMAP [remap OLDDEF] NEWDEF)[39;49;00m
   868	[33m\n[39;49;00m[33m(fn OLDDEF NEWDEF KEYMAP &optional OLDMAP)[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   869	[37m  [39;49;00m[37m;; Don't document PREFIX in the doc string because we don't want to[39;49;00m[37m[39;49;00m
   870	[37m  [39;49;00m[37m;; advertise it.  It's meant for recursive calls only.  Here's its[39;49;00m[37m[39;49;00m
   871	[37m  [39;49;00m[37m;; meaning[39;49;00m[37m[39;49;00m
   872	[37m[39;49;00m
   873	[37m  [39;49;00m[37m;; If optional argument PREFIX is specified, it should be a key[39;49;00m[37m[39;49;00m
   874	[37m  [39;49;00m[37m;; prefix, a string.  Redefined bindings will then be bound to the[39;49;00m[37m[39;49;00m
   875	[37m  [39;49;00m[37m;; original key, with PREFIX added at the front.[39;49;00m[37m[39;49;00m
   876	[37m  [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mprefix[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mprefix[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m"[39;49;00m))[37m[39;49;00m
   877	[37m  [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mscan[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31moldmap[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m))[37m[39;49;00m
   878	[37m	 [39;49;00m([31mprefix1[39;49;00m[37m [39;49;00m([32mvconcat[39;49;00m[37m [39;49;00m[31mprefix[39;49;00m[37m [39;49;00m[[31mnil[39;49;00m]))[37m[39;49;00m
   879	[37m	 [39;49;00m([31mkey-substitution-in-progress[39;49;00m[37m[39;49;00m
   880	[37m	  [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mscan[39;49;00m[37m [39;49;00m[31mkey-substitution-in-progress[39;49;00m)))[37m[39;49;00m
   881	[37m    [39;49;00m[37m;; Scan OLDMAP, finding each char or event-symbol that[39;49;00m[37m[39;49;00m
   882	[37m    [39;49;00m[37m;; has any definition, and act on it with hack-key.[39;49;00m[37m[39;49;00m
   883	[37m    [39;49;00m([32mmap-keymap[39;49;00m[37m[39;49;00m
   884	[37m     [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31mchar[39;49;00m[37m [39;49;00m[31mdefn[39;49;00m)[37m[39;49;00m
   885	[37m       [39;49;00m([32maset[39;49;00m[37m [39;49;00m[31mprefix1[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31mprefix[39;49;00m)[37m [39;49;00m[31mchar[39;49;00m)[37m[39;49;00m
   886	[37m       [39;49;00m([31msubstitute-key-definition-key[39;49;00m[37m [39;49;00m[31mdefn[39;49;00m[37m [39;49;00m[31molddef[39;49;00m[37m [39;49;00m[31mnewdef[39;49;00m[37m [39;49;00m[31mprefix1[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m))[37m[39;49;00m
   887	[37m     [39;49;00m[31mscan[39;49;00m)))[37m[39;49;00m
   888	[37m[39;49;00m
   889	([36mdefun[39;49;00m[37m [39;49;00m[31msubstitute-key-definition-key[39;49;00m[37m [39;49;00m([31mdefn[39;49;00m[37m [39;49;00m[31molddef[39;49;00m[37m [39;49;00m[31mnewdef[39;49;00m[37m [39;49;00m[31mprefix[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m)[37m[39;49;00m
   890	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m([31minner-def[39;49;00m[37m [39;49;00m[31mskipped[39;49;00m[37m [39;49;00m[31mmenu-item[39;49;00m)[37m[39;49;00m
   891	[37m    [39;49;00m[37m;; Find the actual command name within the binding.[39;49;00m[37m[39;49;00m
   892	[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mcar-safe[39;49;00m[37m [39;49;00m[31mdefn[39;49;00m)[37m [39;49;00m[33m'menu-item[39;49;00m)[37m[39;49;00m
   893	[37m	[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mmenu-item[39;49;00m[37m [39;49;00m[31mdefn[39;49;00m[37m [39;49;00m[31mdefn[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m[31mdefn[39;49;00m))[37m[39;49;00m
   894	[37m      [39;49;00m[37m;; Skip past menu-prompt.[39;49;00m[37m[39;49;00m
   895	[37m      [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m([32mcar-safe[39;49;00m[37m [39;49;00m[31mdefn[39;49;00m))[37m[39;49;00m
   896	[37m	[39;49;00m([36mpush[39;49;00m[37m [39;49;00m([36mpop[39;49;00m[37m [39;49;00m[31mdefn[39;49;00m)[37m [39;49;00m[31mskipped[39;49;00m))[37m[39;49;00m
   897	[37m      [39;49;00m[37m;; Skip past cached key-equivalence data for menu items.[39;49;00m[37m[39;49;00m
   898	[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m([32mcar-safe[39;49;00m[37m [39;49;00m[31mdefn[39;49;00m))[37m[39;49;00m
   899	[37m	  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mdefn[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mdefn[39;49;00m))))[37m[39;49;00m
   900	[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mdefn[39;49;00m[37m [39;49;00m[31molddef[39;49;00m)[37m[39;49;00m
   901	[37m	    [39;49;00m[37m;; Compare with equal if definition is a key sequence.[39;49;00m[37m[39;49;00m
   902	[37m	    [39;49;00m[37m;; That is useful for operating on function-key-map.[39;49;00m[37m[39;49;00m
   903	[37m	    [39;49;00m([34mand[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m[31mdefn[39;49;00m)[37m [39;49;00m([32mvectorp[39;49;00m[37m [39;49;00m[31mdefn[39;49;00m))[37m[39;49;00m
   904	[37m		 [39;49;00m([32mequal[39;49;00m[37m [39;49;00m[31mdefn[39;49;00m[37m [39;49;00m[31molddef[39;49;00m)))[37m[39;49;00m
   905	[37m	[39;49;00m([32mdefine-key[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m[37m [39;49;00m[31mprefix[39;49;00m[37m[39;49;00m
   906	[37m	  [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mmenu-item[39;49;00m[37m[39;49;00m
   907	[37m	      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mcopy[39;49;00m[37m [39;49;00m([32mcopy-sequence[39;49;00m[37m [39;49;00m[31mmenu-item[39;49;00m)))[37m[39;49;00m
   908	[37m		[39;49;00m([32msetcar[39;49;00m[37m [39;49;00m([32mnthcdr[39;49;00m[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m[31mcopy[39;49;00m)[37m [39;49;00m[31mnewdef[39;49;00m)[37m[39;49;00m
   909	[37m		[39;49;00m[31mcopy[39;49;00m)[37m[39;49;00m
   910	[37m	    [39;49;00m([32mnconc[39;49;00m[37m [39;49;00m([32mnreverse[39;49;00m[37m [39;49;00m[31mskipped[39;49;00m)[37m [39;49;00m[31mnewdef[39;49;00m)))[37m[39;49;00m
   911	[37m      [39;49;00m[37m;; Look past a symbol that names a keymap.[39;49;00m[37m[39;49;00m
   912	[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31minner-def[39;49;00m[37m[39;49;00m
   913	[37m	    [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mindirect-function[39;49;00m[37m [39;49;00m[31mdefn[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m [39;49;00m[31mdefn[39;49;00m))[37m[39;49;00m
   914	[37m      [39;49;00m[37m;; For nested keymaps, we use `inner-def' rather than `defn' so as to[39;49;00m[37m[39;49;00m
   915	[37m      [39;49;00m[37m;; avoid autoloading a keymap.  This is mostly done to preserve the[39;49;00m[37m[39;49;00m
   916	[37m      [39;49;00m[37m;; original non-autoloading behavior of pre-map-keymap times.[39;49;00m[37m[39;49;00m
   917	[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mkeymapp[39;49;00m[37m [39;49;00m[31minner-def[39;49;00m)[37m[39;49;00m
   918	[37m	       [39;49;00m[37m;; Avoid recursively scanning[39;49;00m[37m[39;49;00m
   919	[37m	       [39;49;00m[37m;; where KEYMAP does not have a submap.[39;49;00m[37m[39;49;00m
   920	[37m	       [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([32melt[39;49;00m[37m [39;49;00m([32mlookup-key[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m[37m [39;49;00m[31mprefix[39;49;00m)))[37m[39;49;00m
   921	[37m		 [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[32melt[39;49;00m)[37m [39;49;00m([32mnatnump[39;49;00m[37m [39;49;00m[32melt[39;49;00m)[37m [39;49;00m([32mkeymapp[39;49;00m[37m [39;49;00m[32melt[39;49;00m)))[37m[39;49;00m
   922	[37m	       [39;49;00m[37m;; Avoid recursively rescanning keymap being scanned.[39;49;00m[37m[39;49;00m
   923	[37m	       [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[31minner-def[39;49;00m[37m [39;49;00m[31mkey-substitution-in-progress[39;49;00m)))[37m[39;49;00m
   924	[37m	  [39;49;00m[37m;; If this one isn't being scanned already, scan it now.[39;49;00m[37m[39;49;00m
   925	[37m	  [39;49;00m([31msubstitute-key-definition[39;49;00m[37m [39;49;00m[31molddef[39;49;00m[37m [39;49;00m[31mnewdef[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m[37m [39;49;00m[31minner-def[39;49;00m[37m [39;49;00m[31mprefix[39;49;00m)))))[37m[39;49;00m
   926	[37m[39;49;00m
   927	[37m[39;49;00m[37m[39;49;00m
   928	[37m;;;; The global keymap tree.[39;49;00m[37m[39;49;00m
   929	[37m[39;49;00m
   930	[37m;; global-map, esc-map, and ctl-x-map have their values set up in[39;49;00m[37m[39;49;00m
   931	[37m;; keymap.c; we just give them docstrings here.[39;49;00m[37m[39;49;00m
   932	[37m[39;49;00m
   933	([34mdefvar[39;49;00m[37m [39;49;00m[31mglobal-map[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m
   934	[37m  [39;49;00m[33m"[39;49;00m[33mDefault global keymap mapping Emacs keyboard input into commands.[39;49;00m
   935	[33mThe value is a keymap which is usually (but not necessarily) Emacs's[39;49;00m
   936	[33mglobal map.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
   937	[37m[39;49;00m
   938	([34mdefvar[39;49;00m[37m [39;49;00m[31mesc-map[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m
   939	[37m  [39;49;00m[33m"[39;49;00m[33mDefault keymap for ESC (meta) commands.[39;49;00m
   940	[33mThe normal global definition of the character ESC indirects to this keymap.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
   941	[37m[39;49;00m
   942	([34mdefvar[39;49;00m[37m [39;49;00m[31mctl-x-map[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m
   943	[37m  [39;49;00m[33m"[39;49;00m[33mDefault keymap for C-x commands.[39;49;00m
   944	[33mThe normal global definition of the character C-x indirects to this keymap.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
   945	[37m[39;49;00m
   946	([34mdefvar[39;49;00m[37m [39;49;00m[31mctl-x-4-map[39;49;00m[37m [39;49;00m([32mmake-sparse-keymap[39;49;00m)[37m[39;49;00m
   947	[37m  [39;49;00m[33m"[39;49;00m[33mKeymap for subcommands of C-x 4.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
   948	([36mdefalias[39;49;00m[37m [39;49;00m[33m'ctl-x-4-prefix[39;49;00m[37m [39;49;00m[31mctl-x-4-map[39;49;00m)[37m[39;49;00m
   949	([32mdefine-key[39;49;00m[37m [39;49;00m[31mctl-x-map[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m4[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m'ctl-x-4-prefix[39;49;00m)[37m[39;49;00m
   950	[37m[39;49;00m
   951	([34mdefvar[39;49;00m[37m [39;49;00m[31mctl-x-5-map[39;49;00m[37m [39;49;00m([32mmake-sparse-keymap[39;49;00m)[37m[39;49;00m
   952	[37m  [39;49;00m[33m"[39;49;00m[33mKeymap for frame commands.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
   953	([36mdefalias[39;49;00m[37m [39;49;00m[33m'ctl-x-5-prefix[39;49;00m[37m [39;49;00m[31mctl-x-5-map[39;49;00m)[37m[39;49;00m
   954	([32mdefine-key[39;49;00m[37m [39;49;00m[31mctl-x-map[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m5[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m'ctl-x-5-prefix[39;49;00m)[37m[39;49;00m
   955	[37m[39;49;00m
   956	[37m[39;49;00m[37m[39;49;00m
   957	[37m;;;; Event manipulation functions.[39;49;00m[37m[39;49;00m
   958	[37m[39;49;00m
   959	([34mdefconst[39;49;00m[37m [39;49;00m[31mlistify-key-sequence-1[39;49;00m[37m [39;49;00m([32mlogior[39;49;00m[37m [39;49;00m[34m128[39;49;00m[37m [39;49;00m[33m?\M[39;49;00m[31m-\C-@[39;49;00m))[37m[39;49;00m
   960	[37m[39;49;00m
   961	([36mdefun[39;49;00m[37m [39;49;00m[31mlistify-key-sequence[39;49;00m[37m [39;49;00m([31mkey[39;49;00m)[37m[39;49;00m
   962	[37m  [39;49;00m[33m"[39;49;00m[33mConvert a key sequence to a list of events.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   963	[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mvectorp[39;49;00m[37m [39;49;00m[31mkey[39;49;00m)[37m[39;49;00m
   964	[37m      [39;49;00m([32mappend[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m
   965	[37m    [39;49;00m([32mmapcar[39;49;00m[37m [39;49;00m([34mfunction[39;49;00m[37m [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31mc[39;49;00m)[37m[39;49;00m
   966	[37m			[39;49;00m([34mif[39;49;00m[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m[31mc[39;49;00m[37m [39;49;00m[34m127[39;49;00m)[37m[39;49;00m
   967	[37m			    [39;49;00m([32mlogxor[39;49;00m[37m [39;49;00m[31mc[39;49;00m[37m [39;49;00m[31mlistify-key-sequence-1[39;49;00m)[37m[39;49;00m
   968	[37m			  [39;49;00m[31mc[39;49;00m)))[37m[39;49;00m
   969	[37m	    [39;49;00m[31mkey[39;49;00m)))[37m[39;49;00m
   970	[37m[39;49;00m
   971	([36mdefun[39;49;00m[37m [39;49;00m[31meventp[39;49;00m[37m [39;49;00m([31mobj[39;49;00m)[37m[39;49;00m
   972	[37m  [39;49;00m[33m"[39;49;00m[33mTrue if the argument is an event object.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   973	[37m  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31mobj[39;49;00m[37m[39;49;00m
   974	[37m    [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mintegerp[39;49;00m[37m [39;49;00m[31mobj[39;49;00m)[37m[39;49;00m
   975	[37m        [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32msymbolp[39;49;00m[37m [39;49;00m[31mobj[39;49;00m)[37m [39;49;00m[31mobj[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mkeywordp[39;49;00m[37m [39;49;00m[31mobj[39;49;00m)))[37m[39;49;00m
   976	[37m        [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mobj[39;49;00m)[37m [39;49;00m([32msymbolp[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mobj[39;49;00m))))))[37m[39;49;00m
   977	[37m[39;49;00m
   978	([36mdefun[39;49;00m[37m [39;49;00m[31mevent-modifiers[39;49;00m[37m [39;49;00m([31mevent[39;49;00m)[37m[39;49;00m
   979	[37m  [39;49;00m[33m"[39;49;00m[33mReturn a list of symbols representing the modifier keys in event EVENT.[39;49;00m
   980	[33mThe elements of the list may include [39;49;00m[33m`meta'[39;49;00m[33m, [39;49;00m[33m`control'[39;49;00m[33m,[39;49;00m
   981	[33m`shift'[39;49;00m[33m, [39;49;00m[33m`hyper'[39;49;00m[33m, [39;49;00m[33m`super'[39;49;00m[33m, [39;49;00m[33m`alt'[39;49;00m[33m, [39;49;00m[33m`click'[39;49;00m[33m, [39;49;00m[33m`double'[39;49;00m[33m, [39;49;00m[33m`triple'[39;49;00m[33m, [39;49;00m[33m`drag'[39;49;00m[33m,[39;49;00m
   982	[33mand [39;49;00m[33m`down'[39;49;00m[33m.[39;49;00m
   983	[33mEVENT may be an event or an event type.  If EVENT is a symbol[39;49;00m
   984	[33mthat has never been used in an event that has been read as input[39;49;00m
   985	[33min the current Emacs session, then this function may fail to include[39;49;00m
   986	[33mthe [39;49;00m[33m`click'[39;49;00m[33m modifier.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   987	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtype[39;49;00m[37m [39;49;00m[31mevent[39;49;00m))[37m[39;49;00m
   988	[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mlistp[39;49;00m[37m [39;49;00m[31mtype[39;49;00m)[37m[39;49;00m
   989	[37m	[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mtype[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mtype[39;49;00m)))[37m[39;49;00m
   990	[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32msymbolp[39;49;00m[37m [39;49;00m[31mtype[39;49;00m)[37m[39;49;00m
   991	[37m        [39;49;00m[37m;; Don't read event-symbol-elements directly since we're not[39;49;00m[37m[39;49;00m
   992	[37m        [39;49;00m[37m;; sure the symbol has already been parsed.[39;49;00m[37m[39;49;00m
   993	[37m	[39;49;00m([32mcdr[39;49;00m[37m [39;49;00m([32minternal-event-symbol-parse-modifiers[39;49;00m[37m [39;49;00m[31mtype[39;49;00m))[37m[39;49;00m
   994	[37m      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([32mlist[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m
   995	[37m	    [39;49;00m([31mchar[39;49;00m[37m [39;49;00m([32mlogand[39;49;00m[37m [39;49;00m[31mtype[39;49;00m[37m [39;49;00m([32mlognot[39;49;00m[37m [39;49;00m([32mlogior[39;49;00m[37m [39;49;00m[33m?\M[39;49;00m[31m-\^@[39;49;00m[37m [39;49;00m[33m?\C[39;49;00m[31m-\^@[39;49;00m[37m [39;49;00m[33m?\S[39;49;00m[31m-\^@[39;49;00m[37m[39;49;00m
   996	[37m					       [39;49;00m[33m?\H[39;49;00m[31m-\^@[39;49;00m[37m [39;49;00m[33m?\s[39;49;00m[31m-\^@[39;49;00m[37m [39;49;00m[33m?\A[39;49;00m[31m-\^@[39;49;00m)))))[37m[39;49;00m
   997	[37m	[39;49;00m([34mif[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([31mzerop[39;49;00m[37m [39;49;00m([32mlogand[39;49;00m[37m [39;49;00m[31mtype[39;49;00m[37m [39;49;00m[33m?\M[39;49;00m[31m-\^@[39;49;00m)))[37m[39;49;00m
   998	[37m	    [39;49;00m([36mpush[39;49;00m[37m [39;49;00m[33m'meta[39;49;00m[37m [39;49;00m[32mlist[39;49;00m))[37m[39;49;00m
   999	[37m	[39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([31mzerop[39;49;00m[37m [39;49;00m([32mlogand[39;49;00m[37m [39;49;00m[31mtype[39;49;00m[37m [39;49;00m[33m?\C[39;49;00m[31m-\^@[39;49;00m)))[37m[39;49;00m
  1000	[37m		[39;49;00m([32m<[39;49;00m[37m [39;49;00m[31mchar[39;49;00m[37m [39;49;00m[34m32[39;49;00m))[37m[39;49;00m
  1001	[37m	    [39;49;00m([36mpush[39;49;00m[37m [39;49;00m[33m'control[39;49;00m[37m [39;49;00m[32mlist[39;49;00m))[37m[39;49;00m
  1002	[37m	[39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([31mzerop[39;49;00m[37m [39;49;00m([32mlogand[39;49;00m[37m [39;49;00m[31mtype[39;49;00m[37m [39;49;00m[33m?\S[39;49;00m[31m-\^@[39;49;00m)))[37m[39;49;00m
  1003	[37m		[39;49;00m([32m/=[39;49;00m[37m [39;49;00m[31mchar[39;49;00m[37m [39;49;00m([32mdowncase[39;49;00m[37m [39;49;00m[31mchar[39;49;00m)))[37m[39;49;00m
  1004	[37m	    [39;49;00m([36mpush[39;49;00m[37m [39;49;00m[33m'shift[39;49;00m[37m [39;49;00m[32mlist[39;49;00m))[37m[39;49;00m
  1005	[37m	[39;49;00m([34mor[39;49;00m[37m [39;49;00m([31mzerop[39;49;00m[37m [39;49;00m([32mlogand[39;49;00m[37m [39;49;00m[31mtype[39;49;00m[37m [39;49;00m[33m?\H[39;49;00m[31m-\^@[39;49;00m))[37m[39;49;00m
  1006	[37m	    [39;49;00m([36mpush[39;49;00m[37m [39;49;00m[33m'hyper[39;49;00m[37m [39;49;00m[32mlist[39;49;00m))[37m[39;49;00m
  1007	[37m	[39;49;00m([34mor[39;49;00m[37m [39;49;00m([31mzerop[39;49;00m[37m [39;49;00m([32mlogand[39;49;00m[37m [39;49;00m[31mtype[39;49;00m[37m [39;49;00m[33m?\s[39;49;00m[31m-\^@[39;49;00m))[37m[39;49;00m
  1008	[37m	    [39;49;00m([36mpush[39;49;00m[37m [39;49;00m[33m'super[39;49;00m[37m [39;49;00m[32mlist[39;49;00m))[37m[39;49;00m
  1009	[37m	[39;49;00m([34mor[39;49;00m[37m [39;49;00m([31mzerop[39;49;00m[37m [39;49;00m([32mlogand[39;49;00m[37m [39;49;00m[31mtype[39;49;00m[37m [39;49;00m[33m?\A[39;49;00m[31m-\^@[39;49;00m))[37m[39;49;00m
  1010	[37m	    [39;49;00m([36mpush[39;49;00m[37m [39;49;00m[33m'alt[39;49;00m[37m [39;49;00m[32mlist[39;49;00m))[37m[39;49;00m
  1011	[37m	[39;49;00m[32mlist[39;49;00m))))[37m[39;49;00m
  1012	[37m[39;49;00m
  1013	([36mdefun[39;49;00m[37m [39;49;00m[31mevent-basic-type[39;49;00m[37m [39;49;00m([31mevent[39;49;00m)[37m[39;49;00m
  1014	[37m  [39;49;00m[33m"[39;49;00m[33mReturn the basic type of the given event (all modifiers removed).[39;49;00m
  1015	[33mThe value is a printing character (not upper case) or a symbol.[39;49;00m
  1016	[33mEVENT may be an event or an event type.  If EVENT is a symbol[39;49;00m
  1017	[33mthat has never been used in an event that has been read as input[39;49;00m
  1018	[33min the current Emacs session, then this function may return nil.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  1019	[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mevent[39;49;00m)[37m[39;49;00m
  1020	[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mevent[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mevent[39;49;00m)))[37m[39;49;00m
  1021	[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32msymbolp[39;49;00m[37m [39;49;00m[31mevent[39;49;00m)[37m[39;49;00m
  1022	[37m      [39;49;00m([32mcar[39;49;00m[37m [39;49;00m([32mget[39;49;00m[37m [39;49;00m[31mevent[39;49;00m[37m [39;49;00m[33m'event-symbol-elements[39;49;00m))[37m[39;49;00m
  1023	[37m    [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mbase[39;49;00m[37m [39;49;00m([32mlogand[39;49;00m[37m [39;49;00m[31mevent[39;49;00m[37m [39;49;00m([32m1-[39;49;00m[37m [39;49;00m[33m?\A[39;49;00m[31m-\^@[39;49;00m)))[37m[39;49;00m
  1024	[37m	   [39;49;00m([31muncontrolled[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m[31mbase[39;49;00m[37m [39;49;00m[34m32[39;49;00m)[37m [39;49;00m([32mlogior[39;49;00m[37m [39;49;00m[31mbase[39;49;00m[37m [39;49;00m[34m64[39;49;00m)[37m [39;49;00m[31mbase[39;49;00m)))[37m[39;49;00m
  1025	[37m      [39;49;00m[37m;; There are some numbers that are invalid characters and[39;49;00m[37m[39;49;00m
  1026	[37m      [39;49;00m[37m;; cause `downcase' to get an error.[39;49;00m[37m[39;49;00m
  1027	[37m      [39;49;00m([34mcondition-case[39;49;00m[37m [39;49;00m()[37m[39;49;00m
  1028	[37m	  [39;49;00m([32mdowncase[39;49;00m[37m [39;49;00m[31muncontrolled[39;49;00m)[37m[39;49;00m
  1029	[37m	[39;49;00m([36merror[39;49;00m[37m [39;49;00m[31muncontrolled[39;49;00m)))))[37m[39;49;00m
  1030	[37m[39;49;00m
  1031	([36mdefsubst[39;49;00m[37m [39;49;00m[31mmouse-movement-p[39;49;00m[37m [39;49;00m([31mobject[39;49;00m)[37m[39;49;00m
  1032	[37m  [39;49;00m[33m"[39;49;00m[33mReturn non-nil if OBJECT is a mouse movement event.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  1033	[37m  [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mcar-safe[39;49;00m[37m [39;49;00m[31mobject[39;49;00m)[37m [39;49;00m[33m'mouse-movement[39;49;00m))[37m[39;49;00m
  1034	[37m[39;49;00m
  1035	([36mdefun[39;49;00m[37m [39;49;00m[31mmouse-event-p[39;49;00m[37m [39;49;00m([31mobject[39;49;00m)[37m[39;49;00m
  1036	[37m  [39;49;00m[33m"[39;49;00m[33mReturn non-nil if OBJECT is a mouse click event.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  1037	[37m  [39;49;00m[37m;; is this really correct? maybe remove mouse-movement?[39;49;00m[37m[39;49;00m
  1038	[37m  [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m([31mevent-basic-type[39;49;00m[37m [39;49;00m[31mobject[39;49;00m)[37m [39;49;00m'([31mmouse-1[39;49;00m[37m [39;49;00m[31mmouse-2[39;49;00m[37m [39;49;00m[31mmouse-3[39;49;00m[37m [39;49;00m[31mmouse-movement[39;49;00m)))[37m[39;49;00m
  1039	[37m[39;49;00m
  1040	([36mdefun[39;49;00m[37m [39;49;00m[31mevent-start[39;49;00m[37m [39;49;00m([31mevent[39;49;00m)[37m[39;49;00m
  1041	[37m  [39;49;00m[33m"[39;49;00m[33mReturn the starting position of EVENT.[39;49;00m
  1042	[33mEVENT should be a mouse click, drag, or key press event.  If[39;49;00m
  1043	[33mEVENT is nil, the value of [39;49;00m[33m`posn-at-point'[39;49;00m[33m is used instead.[39;49;00m
  1044	[33m[39;49;00m
  1045	[33mThe following accessor functions are used to access the elements[39;49;00m
  1046	[33mof the position:[39;49;00m
  1047	[33m[39;49;00m
  1048	[33m`posn-window'[39;49;00m[33m: The window the event is in.[39;49;00m
  1049	[33m`posn-area'[39;49;00m[33m: A symbol identifying the area the event occurred in,[39;49;00m
  1050	[33mor nil if the event occurred in the text area.[39;49;00m
  1051	[33m`posn-point'[39;49;00m[33m: The buffer position of the event.[39;49;00m
  1052	[33m`posn-x-y'[39;49;00m[33m: The pixel-based coordinates of the event.[39;49;00m
  1053	[33m`posn-col-row'[39;49;00m[33m: The estimated column and row corresponding to the[39;49;00m
  1054	[33mposition of the event.[39;49;00m
  1055	[33m`posn-actual-col-row'[39;49;00m[33m: The actual column and row corresponding to the[39;49;00m
  1056	[33mposition of the event.[39;49;00m
  1057	[33m`posn-string'[39;49;00m[33m: The string object of the event, which is either[39;49;00m
  1058	[33mnil or (STRING . POSITION)'.[39;49;00m
  1059	[33m`posn-image'[39;49;00m[33m: The image object of the event, if any.[39;49;00m
  1060	[33m`posn-object'[39;49;00m[33m: The image or string object of the event, if any.[39;49;00m
  1061	[33m`posn-timestamp'[39;49;00m[33m: The time the event occurred, in milliseconds.[39;49;00m
  1062	[33m[39;49;00m
  1063	[33mFor more information, see Info node [39;49;00m[33m`[39;49;00m[33m(elisp)Click Events'.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  1064	[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mevent[39;49;00m)[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mevent[39;49;00m)[37m[39;49;00m
  1065	[37m    [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mposn-at-point[39;49;00m)[37m[39;49;00m
  1066	[37m        [39;49;00m([32mlist[39;49;00m[37m [39;49;00m([32mselected-window[39;49;00m)[37m [39;49;00m([32mpoint[39;49;00m)[37m [39;49;00m'([34m0[39;49;00m[37m [39;49;00m.[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34m0[39;49;00m))))[37m[39;49;00m
  1067	[37m[39;49;00m
  1068	([36mdefun[39;49;00m[37m [39;49;00m[31mevent-end[39;49;00m[37m [39;49;00m([31mevent[39;49;00m)[37m[39;49;00m
  1069	[37m  [39;49;00m[33m"[39;49;00m[33mReturn the ending position of EVENT.[39;49;00m
  1070	[33mEVENT should be a click, drag, or key press event.[39;49;00m
  1071	[33m[39;49;00m
  1072	[33mSee [39;49;00m[33m`event-start'[39;49;00m[33m for a description of the value returned.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  1073	[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mevent[39;49;00m)[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m[31mevent[39;49;00m))[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m[31mevent[39;49;00m)[37m[39;49;00m
  1074	[37m    [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mposn-at-point[39;49;00m)[37m[39;49;00m
  1075	[37m        [39;49;00m([32mlist[39;49;00m[37m [39;49;00m([32mselected-window[39;49;00m)[37m [39;49;00m([32mpoint[39;49;00m)[37m [39;49;00m'([34m0[39;49;00m[37m [39;49;00m.[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34m0[39;49;00m))))[37m[39;49;00m
  1076	[37m[39;49;00m
  1077	([36mdefsubst[39;49;00m[37m [39;49;00m[31mevent-click-count[39;49;00m[37m [39;49;00m([31mevent[39;49;00m)[37m[39;49;00m
  1078	[37m  [39;49;00m[33m"[39;49;00m[33mReturn the multi-click count of EVENT, a click or drag event.[39;49;00m
  1079	[33mThe return value is a positive integer.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  1080	[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mevent[39;49;00m)[37m [39;49;00m([32mintegerp[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m[31mevent[39;49;00m)))[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m[31mevent[39;49;00m)[37m [39;49;00m[34m1[39;49;00m))[37m[39;49;00m
  1081	[37m[39;49;00m[37m[39;49;00m
  1082	[37m;;;; Extracting fields of the positions in an event.[39;49;00m[37m[39;49;00m
  1083	[37m[39;49;00m
  1084	([36mdefun[39;49;00m[37m [39;49;00m[31mposnp[39;49;00m[37m [39;49;00m([31mobj[39;49;00m)[37m[39;49;00m
  1085	[37m  [39;49;00m[33m"[39;49;00m[33mReturn non-nil if OBJ appears to be a valid [39;49;00m[33m`posn'[39;49;00m[33m object specifying a window.[39;49;00m
  1086	[33mIf OBJ is a valid [39;49;00m[33m`posn'[39;49;00m[33m object, but specifies a frame rather[39;49;00m
  1087	[33mthan a window, return nil.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  1088	[37m  [39;49;00m[37m;; FIXME: Correct the behavior of this function so that all valid[39;49;00m[37m[39;49;00m
  1089	[37m  [39;49;00m[37m;; `posn' objects are recognized, after updating other code that[39;49;00m[37m[39;49;00m
  1090	[37m  [39;49;00m[37m;; depends on its present behavior.[39;49;00m[37m[39;49;00m
  1091	[37m  [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mwindowp[39;49;00m[37m [39;49;00m([32mcar-safe[39;49;00m[37m [39;49;00m[31mobj[39;49;00m))[37m[39;49;00m
  1092	[37m       [39;49;00m([32matom[39;49;00m[37m [39;49;00m([32mcar-safe[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mobj[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mobj[39;49;00m))))[37m                [39;49;00m[37m;AREA-OR-POS.[39;49;00m[37m[39;49;00m
  1093	[37m       [39;49;00m([32mintegerp[39;49;00m[37m [39;49;00m([32mcar-safe[39;49;00m[37m [39;49;00m([32mcar-safe[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mobj[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mobj[39;49;00m)))))[37m [39;49;00m[37m;XOFFSET.[39;49;00m[37m[39;49;00m
  1094	[37m       [39;49;00m([32mintegerp[39;49;00m[37m [39;49;00m([32mcar-safe[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mobj[39;49;00m)))))[37m                     [39;49;00m[37m;TIMESTAMP.[39;49;00m[37m[39;49;00m
  1095	[37m[39;49;00m
  1096	([36mdefsubst[39;49;00m[37m [39;49;00m[31mposn-window[39;49;00m[37m [39;49;00m([31mposition[39;49;00m)[37m[39;49;00m
  1097	[37m  [39;49;00m[33m"[39;49;00m[33mReturn the window in POSITION.[39;49;00m
  1098	[33mPOSITION should be a list of the form returned by the [39;49;00m[33m`event-start'[39;49;00m[33m[39;49;00m
  1099	[33mand [39;49;00m[33m`event-end'[39;49;00m[33m functions.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  1100	[37m  [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[31mposition[39;49;00m))[37m[39;49;00m
  1101	[37m[39;49;00m
  1102	([36mdefsubst[39;49;00m[37m [39;49;00m[31mposn-area[39;49;00m[37m [39;49;00m([31mposition[39;49;00m)[37m[39;49;00m
  1103	[37m  [39;49;00m[33m"[39;49;00m[33mReturn the window area recorded in POSITION, or nil for the text area.[39;49;00m
  1104	[33mPOSITION should be a list of the form returned by the [39;49;00m[33m`event-start'[39;49;00m[33m[39;49;00m
  1105	[33mand [39;49;00m[33m`event-end'[39;49;00m[33m functions.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  1106	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31marea[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mposition[39;49;00m))[37m[39;49;00m
  1107	[37m		  [39;49;00m([32mcar[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mposition[39;49;00m))[37m[39;49;00m
  1108	[37m		[39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mposition[39;49;00m))))[37m[39;49;00m
  1109	[37m    [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32msymbolp[39;49;00m[37m [39;49;00m[31marea[39;49;00m)[37m [39;49;00m[31marea[39;49;00m)))[37m[39;49;00m
  1110	[37m[39;49;00m
  1111	([36mdefun[39;49;00m[37m [39;49;00m[31mposn-point[39;49;00m[37m [39;49;00m([31mposition[39;49;00m)[37m[39;49;00m
  1112	[37m  [39;49;00m[33m"[39;49;00m[33mReturn the buffer location in POSITION.[39;49;00m
  1113	[33mPOSITION should be a list of the form returned by the [39;49;00m[33m`event-start'[39;49;00m[33m[39;49;00m
  1114	[33mand [39;49;00m[33m`event-end'[39;49;00m[33m functions.[39;49;00m
  1115	[33mReturns nil if POSITION does not correspond to any buffer location (e.g.[39;49;00m
  1116	[33ma click on a scroll bar).[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  1117	[37m  [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m5[39;49;00m[37m [39;49;00m[31mposition[39;49;00m)[37m[39;49;00m
  1118	[37m      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mpt[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mposition[39;49;00m)))[37m[39;49;00m
  1119	[37m        [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mcar-safe[39;49;00m[37m [39;49;00m[31mpt[39;49;00m)[37m[39;49;00m
  1120	[37m            [39;49;00m[37m;; Apparently this can also be `vertical-scroll-bar' (bug#13979).[39;49;00m[37m[39;49;00m
  1121	[37m            [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mintegerp[39;49;00m[37m [39;49;00m[31mpt[39;49;00m)[37m [39;49;00m[31mpt[39;49;00m)))))[37m[39;49;00m
  1122	[37m[39;49;00m
  1123	([36mdefun[39;49;00m[37m [39;49;00m[31mposn-set-point[39;49;00m[37m [39;49;00m([31mposition[39;49;00m)[37m[39;49;00m
  1124	[37m  [39;49;00m[33m"[39;49;00m[33mMove point to POSITION.[39;49;00m
  1125	[33mSelect the corresponding window as well.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  1126	[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mwindowp[39;49;00m[37m [39;49;00m([31mposn-window[39;49;00m[37m [39;49;00m[31mposition[39;49;00m)))[37m[39;49;00m
  1127	[37m      [39;49;00m([36merror[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mPosition not in text area of window[39;49;00m[33m"[39;49;00m))[37m[39;49;00m
  1128	[37m  [39;49;00m([32mselect-window[39;49;00m[37m [39;49;00m([31mposn-window[39;49;00m[37m [39;49;00m[31mposition[39;49;00m))[37m[39;49;00m
  1129	[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mnumberp[39;49;00m[37m [39;49;00m([31mposn-point[39;49;00m[37m [39;49;00m[31mposition[39;49;00m))[37m[39;49;00m
  1130	[37m      [39;49;00m([32mgoto-char[39;49;00m[37m [39;49;00m([31mposn-point[39;49;00m[37m [39;49;00m[31mposition[39;49;00m))))[37m[39;49;00m
  1131	[37m[39;49;00m
  1132	([36mdefsubst[39;49;00m[37m [39;49;00m[31mposn-x-y[39;49;00m[37m [39;49;00m([31mposition[39;49;00m)[37m[39;49;00m
  1133	[37m  [39;49;00m[33m"[39;49;00m[33mReturn the x and y coordinates in POSITION.[39;49;00m
  1134	[33mThe return value has the form (X . Y), where X and Y are given in[39;49;00m
  1135	[33mpixels.  POSITION should be a list of the form returned by[39;49;00m
  1136	[33m`event-start'[39;49;00m[33m and [39;49;00m[33m`event-end'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  1137	[37m  [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m[31mposition[39;49;00m))[37m[39;49;00m
  1138	[37m[39;49;00m
  1139	([36mdeclare-function[39;49;00m[37m [39;49;00m[31mscroll-bar-scale[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mscroll-bar[39;49;00m[33m"[39;49;00m[37m [39;49;00m([31mnum-denom[39;49;00m[37m [39;49;00m[31mwhole[39;49;00m))[37m[39;49;00m
  1140	[37m[39;49;00m
  1141	([36mdefun[39;49;00m[37m [39;49;00m[31mposn-col-row[39;49;00m[37m [39;49;00m([31mposition[39;49;00m)[37m[39;49;00m
  1142	[37m  [39;49;00m[33m"[39;49;00m[33mReturn the nominal column and row in POSITION, measured in characters.[39;49;00m
  1143	[33mThe column and row values are approximations calculated from the x[39;49;00m
  1144	[33mand y coordinates in POSITION and the frame's default character width[39;49;00m
  1145	[33mand default line height, including spacing.[39;49;00m
  1146	[33mFor a scroll-bar event, the result column is 0, and the row[39;49;00m
  1147	[33mcorresponds to the vertical position of the click in the scroll bar.[39;49;00m
  1148	[33mPOSITION should be a list of the form returned by the [39;49;00m[33m`event-start'[39;49;00m[33m[39;49;00m
  1149	[33mand [39;49;00m[33m`event-end'[39;49;00m[33m functions.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  1150	[37m  [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mpair[39;49;00m[37m            [39;49;00m([31mposn-x-y[39;49;00m[37m [39;49;00m[31mposition[39;49;00m))[37m[39;49;00m
  1151	[37m         [39;49;00m([31mframe-or-window[39;49;00m[37m [39;49;00m([31mposn-window[39;49;00m[37m [39;49;00m[31mposition[39;49;00m))[37m[39;49;00m
  1152	[37m         [39;49;00m([31mframe[39;49;00m[37m           [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mframep[39;49;00m[37m [39;49;00m[31mframe-or-window[39;49;00m)[37m[39;49;00m
  1153	[37m                              [39;49;00m[31mframe-or-window[39;49;00m[37m[39;49;00m
  1154	[37m                            [39;49;00m([32mwindow-frame[39;49;00m[37m [39;49;00m[31mframe-or-window[39;49;00m)))[37m[39;49;00m
  1155	[37m         [39;49;00m([31mwindow[39;49;00m[37m          [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mwindowp[39;49;00m[37m [39;49;00m[31mframe-or-window[39;49;00m)[37m [39;49;00m[31mframe-or-window[39;49;00m))[37m[39;49;00m
  1156	[37m         [39;49;00m([31marea[39;49;00m[37m            [39;49;00m([31mposn-area[39;49;00m[37m [39;49;00m[31mposition[39;49;00m)))[37m[39;49;00m
  1157	[37m    [39;49;00m([34mcond[39;49;00m[37m[39;49;00m
  1158	[37m     [39;49;00m(([32mnull[39;49;00m[37m [39;49;00m[31mframe-or-window[39;49;00m)[37m[39;49;00m
  1159	[37m      [39;49;00m'([34m0[39;49;00m[37m [39;49;00m.[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m
  1160	[37m     [39;49;00m(([32meq[39;49;00m[37m [39;49;00m[31marea[39;49;00m[37m [39;49;00m[33m'vertical-scroll-bar[39;49;00m)[37m[39;49;00m
  1161	[37m      [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m([31mscroll-bar-scale[39;49;00m[37m [39;49;00m[31mpair[39;49;00m[37m [39;49;00m([32m1-[39;49;00m[37m [39;49;00m([31mwindow-height[39;49;00m[37m [39;49;00m[31mwindow[39;49;00m)))))[37m[39;49;00m
  1162	[37m     [39;49;00m(([32meq[39;49;00m[37m [39;49;00m[31marea[39;49;00m[37m [39;49;00m[33m'horizontal-scroll-bar[39;49;00m)[37m[39;49;00m
  1163	[37m      [39;49;00m([32mcons[39;49;00m[37m [39;49;00m([31mscroll-bar-scale[39;49;00m[37m [39;49;00m[31mpair[39;49;00m[37m [39;49;00m([31mwindow-width[39;49;00m[37m [39;49;00m[31mwindow[39;49;00m))[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m
  1164	[37m     [39;49;00m([31mt[39;49;00m[37m[39;49;00m
  1165	[37m      [39;49;00m[37m;; FIXME: This should take line-spacing properties on[39;49;00m[37m[39;49;00m
  1166	[37m      [39;49;00m[37m;; newlines into account.[39;49;00m[37m[39;49;00m
  1167	[37m      [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mspacing[39;49;00m[37m [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([31mdisplay-graphic-p[39;49;00m[37m [39;49;00m[31mframe[39;49;00m)[37m[39;49;00m
  1168	[37m                        [39;49;00m([34mor[39;49;00m[37m [39;49;00m([36mwith-current-buffer[39;49;00m[37m[39;49;00m
  1169	[37m                                [39;49;00m([32mwindow-buffer[39;49;00m[37m [39;49;00m([32mframe-selected-window[39;49;00m[37m [39;49;00m[31mframe[39;49;00m))[37m[39;49;00m
  1170	[37m                              [39;49;00m[31mline-spacing[39;49;00m)[37m[39;49;00m
  1171	[37m                            [39;49;00m([32mframe-parameter[39;49;00m[37m [39;49;00m[31mframe[39;49;00m[37m [39;49;00m[33m'line-spacing[39;49;00m)))))[37m[39;49;00m
  1172	[37m	[39;49;00m([34mcond[39;49;00m[37m [39;49;00m(([32mfloatp[39;49;00m[37m [39;49;00m[31mspacing[39;49;00m)[37m[39;49;00m
  1173	[37m	       [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mspacing[39;49;00m[37m [39;49;00m([32mtruncate[39;49;00m[37m [39;49;00m([32m*[39;49;00m[37m [39;49;00m[31mspacing[39;49;00m[37m[39;49;00m
  1174	[37m					  [39;49;00m([32mframe-char-height[39;49;00m[37m [39;49;00m[31mframe[39;49;00m)))))[37m[39;49;00m
  1175	[37m	      [39;49;00m(([32mnull[39;49;00m[37m [39;49;00m[31mspacing[39;49;00m)[37m[39;49;00m
  1176	[37m	       [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mspacing[39;49;00m[37m [39;49;00m[34m0[39;49;00m)))[37m[39;49;00m
  1177	[37m	[39;49;00m([32mcons[39;49;00m[37m [39;49;00m([32m/[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mpair[39;49;00m)[37m [39;49;00m([32mframe-char-width[39;49;00m[37m [39;49;00m[31mframe[39;49;00m))[37m[39;49;00m
  1178	[37m	      [39;49;00m([32m/[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mpair[39;49;00m)[37m [39;49;00m([32m+[39;49;00m[37m [39;49;00m([32mframe-char-height[39;49;00m[37m [39;49;00m[31mframe[39;49;00m)[37m [39;49;00m[31mspacing[39;49;00m))))))))[37m[39;49;00m
  1179	[37m[39;49;00m
  1180	([36mdefun[39;49;00m[37m [39;49;00m[31mposn-actual-col-row[39;49;00m[37m [39;49;00m([31mposition[39;49;00m)[37m[39;49;00m
  1181	[37m  [39;49;00m[33m"[39;49;00m[33mReturn the window row number in POSITION and character number in that row.[39;49;00m
  1182	[33m[39;49;00m
  1183	[33mReturn nil if POSITION does not contain the actual position; in that case[39;49;00m
  1184	[33m\`[39;49;00m[33mposn-col-row' can be used to get approximate values.[39;49;00m
  1185	[33mPOSITION should be a list of the form returned by the [39;49;00m[33m`event-start'[39;49;00m[33m[39;49;00m
  1186	[33mand [39;49;00m[33m`event-end'[39;49;00m[33m functions.[39;49;00m
  1187	[33m[39;49;00m
  1188	[33mThis function does not account for the width on display, like the[39;49;00m
  1189	[33mnumber of visual columns taken by a TAB or image.  If you need[39;49;00m
  1190	[33mthe coordinates of POSITION in character units, you should use[39;49;00m
  1191	[33m\`[39;49;00m[33mposn-col-row', not this function.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  1192	[37m  [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m6[39;49;00m[37m [39;49;00m[31mposition[39;49;00m))[37m[39;49;00m
  1193	[37m[39;49;00m
  1194	([36mdefsubst[39;49;00m[37m [39;49;00m[31mposn-timestamp[39;49;00m[37m [39;49;00m([31mposition[39;49;00m)[37m[39;49;00m
  1195	[37m  [39;49;00m[33m"[39;49;00m[33mReturn the timestamp of POSITION.[39;49;00m
  1196	[33mPOSITION should be a list of the form returned by the [39;49;00m[33m`event-start'[39;49;00m[33m[39;49;00m
  1197	[33mand [39;49;00m[33m`event-end'[39;49;00m[33m functions.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  1198	[37m  [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m3[39;49;00m[37m [39;49;00m[31mposition[39;49;00m))[37m[39;49;00m
  1199	[37m[39;49;00m
  1200	([36mdefun[39;49;00m[37m [39;49;00m[31mposn-string[39;49;00m[37m [39;49;00m([31mposition[39;49;00m)[37m[39;49;00m
  1201	[37m  [39;49;00m[33m"[39;49;00m[33mReturn the string object of POSITION.[39;49;00m
  1202	[33mValue is a cons (STRING . STRING-POS), or nil if not a string.[39;49;00m
  1203	[33mPOSITION should be a list of the form returned by the [39;49;00m[33m`event-start'[39;49;00m[33m[39;49;00m
  1204	[33mand [39;49;00m[33m`event-end'[39;49;00m[33m functions.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  1205	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mx[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m4[39;49;00m[37m [39;49;00m[31mposition[39;49;00m)))[37m[39;49;00m
  1206	[37m    [39;49;00m[37m;; Apparently this can also be `handle' or `below-handle' (bug#13979).[39;49;00m[37m[39;49;00m
  1207	[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mx[39;49;00m)[37m [39;49;00m[31mx[39;49;00m)))[37m[39;49;00m
  1208	[37m[39;49;00m
  1209	([36mdefsubst[39;49;00m[37m [39;49;00m[31mposn-image[39;49;00m[37m [39;49;00m([31mposition[39;49;00m)[37m[39;49;00m
  1210	[37m  [39;49;00m[33m"[39;49;00m[33mReturn the image object of POSITION.[39;49;00m
  1211	[33mValue is a list (image ...), or nil if not an image.[39;49;00m
  1212	[33mPOSITION should be a list of the form returned by the [39;49;00m[33m`event-start'[39;49;00m[33m[39;49;00m
  1213	[33mand [39;49;00m[33m`event-end'[39;49;00m[33m functions.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  1214	[37m  [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m7[39;49;00m[37m [39;49;00m[31mposition[39;49;00m))[37m[39;49;00m
  1215	[37m[39;49;00m
  1216	([36mdefsubst[39;49;00m[37m [39;49;00m[31mposn-object[39;49;00m[37m [39;49;00m([31mposition[39;49;00m)[37m[39;49;00m
  1217	[37m  [39;49;00m[33m"[39;49;00m[33mReturn the object (image or string) of POSITION.[39;49;00m
  1218	[33mValue is a list (image ...) for an image object, a cons cell[39;49;00m
  1219	[33m\([39;49;00m[33mSTRING . STRING-POS) for a string object, and nil for a buffer position.[39;49;00m
  1220	[33mPOSITION should be a list of the form returned by the [39;49;00m[33m`event-start'[39;49;00m[33m[39;49;00m
  1221	[33mand [39;49;00m[33m`event-end'[39;49;00m[33m functions.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  1222	[37m  [39;49;00m([34mor[39;49;00m[37m [39;49;00m([31mposn-image[39;49;00m[37m [39;49;00m[31mposition[39;49;00m)[37m [39;49;00m([31mposn-string[39;49;00m[37m [39;49;00m[31mposition[39;49;00m)))[37m[39;49;00m
  1223	[37m[39;49;00m
  1224	([36mdefsubst[39;49;00m[37m [39;49;00m[31mposn-object-x-y[39;49;00m[37m [39;49;00m([31mposition[39;49;00m)[37m[39;49;00m
  1225	[37m  [39;49;00m[33m"[39;49;00m[33mReturn the x and y coordinates relative to the object of POSITION.[39;49;00m
  1226	[33mThe return value has the form (DX . DY), where DX and DY are[39;49;00m
  1227	[33mgiven in pixels.  POSITION should be a list of the form returned[39;49;00m
  1228	[33mby [39;49;00m[33m`event-start'[39;49;00m[33m and [39;49;00m[33m`event-end'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  1229	[37m  [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m8[39;49;00m[37m [39;49;00m[31mposition[39;49;00m))[37m[39;49;00m
  1230	[37m[39;49;00m
  1231	([36mdefsubst[39;49;00m[37m [39;49;00m[31mposn-object-width-height[39;49;00m[37m [39;49;00m([31mposition[39;49;00m)[37m[39;49;00m
  1232	[37m  [39;49;00m[33m"[39;49;00m[33mReturn the pixel width and height of the object of POSITION.[39;49;00m
  1233	[33mThe return value has the form (WIDTH . HEIGHT).  POSITION should[39;49;00m
  1234	[33mbe a list of the form returned by [39;49;00m[33m`event-start'[39;49;00m[33m and [39;49;00m[33m`event-end'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  1235	[37m  [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m9[39;49;00m[37m [39;49;00m[31mposition[39;49;00m))[37m[39;49;00m
  1236	[37m[39;49;00m
  1237	[37m[39;49;00m[37m[39;49;00m
  1238	[37m;;;; Obsolescent names for functions.[39;49;00m[37m[39;49;00m
  1239	[37m[39;49;00m
  1240	([36mdefine-obsolete-function-alias[39;49;00m[37m [39;49;00m[33m'window-dot[39;49;00m[37m [39;49;00m[33m'window-point[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m22.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1241	([36mdefine-obsolete-function-alias[39;49;00m[37m [39;49;00m[33m'set-window-dot[39;49;00m[37m [39;49;00m[33m'set-window-point[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m22.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1242	([36mdefine-obsolete-function-alias[39;49;00m[37m [39;49;00m[33m'read-input[39;49;00m[37m [39;49;00m[33m'read-string[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m22.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1243	([36mdefine-obsolete-function-alias[39;49;00m[37m [39;49;00m[33m'show-buffer[39;49;00m[37m [39;49;00m[33m'set-window-buffer[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m22.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1244	([36mdefine-obsolete-function-alias[39;49;00m[37m [39;49;00m[33m'eval-current-buffer[39;49;00m[37m [39;49;00m[33m'eval-buffer[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m22.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1245	([36mdefine-obsolete-function-alias[39;49;00m[37m [39;49;00m[33m'string-to-int[39;49;00m[37m [39;49;00m[33m'string-to-number[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m22.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1246	[37m[39;49;00m
  1247	([31mmake-obsolete[39;49;00m[37m [39;49;00m[33m'forward-point[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33muse (+ (point) N) instead.[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1248	([31mmake-obsolete[39;49;00m[37m [39;49;00m[33m'buffer-has-markers-at[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m24.3[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1249	[37m[39;49;00m
  1250	([36mdefun[39;49;00m[37m [39;49;00m[31minsert-string[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31margs[39;49;00m)[37m[39;49;00m
  1251	[37m  [39;49;00m[33m"[39;49;00m[33mMocklisp-compatibility insert function.[39;49;00m
  1252	[33mLike the function [39;49;00m[33m`insert'[39;49;00m[33m except that any argument that is a number[39;49;00m
  1253	[33mis converted into a string by expressing it in decimal.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  1254	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mobsolete[39;49;00m[37m [39;49;00m[32minsert[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m22.1[39;49;00m[33m"[39;49;00m))[37m[39;49;00m
  1255	[37m  [39;49;00m([36mdolist[39;49;00m[37m [39;49;00m([31mel[39;49;00m[37m [39;49;00m[31margs[39;49;00m)[37m[39;49;00m
  1256	[37m    [39;49;00m([32minsert[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mintegerp[39;49;00m[37m [39;49;00m[31mel[39;49;00m)[37m [39;49;00m([32mnumber-to-string[39;49;00m[37m [39;49;00m[31mel[39;49;00m)[37m [39;49;00m[31mel[39;49;00m))))[37m[39;49;00m
  1257	[37m[39;49;00m
  1258	([36mdefun[39;49;00m[37m [39;49;00m[31mmakehash[39;49;00m[37m [39;49;00m([34m&optional[39;49;00m[37m [39;49;00m[31mtest[39;49;00m)[37m[39;49;00m
  1259	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mobsolete[39;49;00m[37m [39;49;00m[32mmake-hash-table[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m22.1[39;49;00m[33m"[39;49;00m))[37m[39;49;00m
  1260	[37m  [39;49;00m([32mmake-hash-table[39;49;00m[37m [39;49;00m[36m:test[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mtest[39;49;00m[37m [39;49;00m[33m'eql[39;49;00m)))[37m[39;49;00m
  1261	[37m[39;49;00m
  1262	([36mdefun[39;49;00m[37m [39;49;00m[31mlog10[39;49;00m[37m [39;49;00m([31mx[39;49;00m)[37m[39;49;00m
  1263	[37m  [39;49;00m[33m"[39;49;00m[33mReturn (log X 10), the log base 10 of X.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  1264	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mobsolete[39;49;00m[37m [39;49;00m[32mlog[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m24.4[39;49;00m[33m"[39;49;00m))[37m[39;49;00m
  1265	[37m  [39;49;00m([32mlog[39;49;00m[37m [39;49;00m[31mx[39;49;00m[37m [39;49;00m[34m10[39;49;00m))[37m[39;49;00m
  1266	[37m[39;49;00m
  1267	[37m;; These are used by VM and some old programs[39;49;00m[37m[39;49;00m
  1268	([36mdefalias[39;49;00m[37m [39;49;00m[33m'focus-frame[39;49;00m[37m [39;49;00m[33m'ignore[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1269	([31mmake-obsolete[39;49;00m[37m [39;49;00m[33m'focus-frame[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mit does nothing.[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m22.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1270	([36mdefalias[39;49;00m[37m [39;49;00m[33m'unfocus-frame[39;49;00m[37m [39;49;00m[33m'ignore[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1271	([31mmake-obsolete[39;49;00m[37m [39;49;00m[33m'unfocus-frame[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mit does nothing.[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m22.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1272	([31mmake-obsolete[39;49;00m[37m [39;49;00m[33m'make-variable-frame-local[39;49;00m[37m[39;49;00m
  1273	[37m	       [39;49;00m[33m"[39;49;00m[33mexplicitly check for a frame-parameter instead.[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m22.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1274	([31mset-advertised-calling-convention[39;49;00m[37m[39;49;00m
  1275	[37m [39;49;00m[33m'all-completions[39;49;00m[37m [39;49;00m'([32mstring[39;49;00m[37m [39;49;00m[31mcollection[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mpredicate[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m23.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1276	([31mset-advertised-calling-convention[39;49;00m[37m [39;49;00m[33m'unintern[39;49;00m[37m [39;49;00m'([31mname[39;49;00m[37m [39;49;00m[31mobarray[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m23.3[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1277	([31mset-advertised-calling-convention[39;49;00m[37m [39;49;00m[33m'indirect-function[39;49;00m[37m [39;49;00m'([31mobject[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m25.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1278	([31mset-advertised-calling-convention[39;49;00m[37m [39;49;00m[33m'redirect-frame-focus[39;49;00m[37m [39;49;00m'([31mframe[39;49;00m[37m [39;49;00m[31mfocus-frame[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m24.3[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1279	([31mset-advertised-calling-convention[39;49;00m[37m [39;49;00m[33m'decode-char[39;49;00m[37m [39;49;00m'([31mch[39;49;00m[37m [39;49;00m[31mcharset[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m21.4[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1280	([31mset-advertised-calling-convention[39;49;00m[37m [39;49;00m[33m'encode-char[39;49;00m[37m [39;49;00m'([31mch[39;49;00m[37m [39;49;00m[31mcharset[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m21.4[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1281	[37m[39;49;00m[37m[39;49;00m
  1282	[37m;;;; Obsolescence declarations for variables, and aliases.[39;49;00m[37m[39;49;00m
  1283	[37m[39;49;00m
  1284	[37m;; Special "default-FOO" variables which contain the default value of[39;49;00m[37m[39;49;00m
  1285	[37m;; the "FOO" variable are nasty.  Their implementation is brittle, and[39;49;00m[37m[39;49;00m
  1286	[37m;; slows down several unrelated variable operations; furthermore, they[39;49;00m[37m[39;49;00m
  1287	[37m;; can lead to really odd behavior if you decide to make them[39;49;00m[37m[39;49;00m
  1288	[37m;; buffer-local.[39;49;00m[37m[39;49;00m
  1289	[37m[39;49;00m
  1290	[37m;; Not used at all in Emacs, last time I checked:[39;49;00m[37m[39;49;00m
  1291	([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-mode-line-format[39;49;00m[37m [39;49;00m[33m'mode-line-format[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1292	([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-header-line-format[39;49;00m[37m [39;49;00m[33m'header-line-format[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1293	([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-line-spacing[39;49;00m[37m [39;49;00m[33m'line-spacing[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1294	([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-abbrev-mode[39;49;00m[37m [39;49;00m[33m'abbrev-mode[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1295	([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-ctl-arrow[39;49;00m[37m [39;49;00m[33m'ctl-arrow[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1296	([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-truncate-lines[39;49;00m[37m [39;49;00m[33m'truncate-lines[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1297	([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-left-margin[39;49;00m[37m [39;49;00m[33m'left-margin[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1298	([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-tab-width[39;49;00m[37m [39;49;00m[33m'tab-width[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1299	([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-case-fold-search[39;49;00m[37m [39;49;00m[33m'case-fold-search[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1300	([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-left-margin-width[39;49;00m[37m [39;49;00m[33m'left-margin-width[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1301	([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-right-margin-width[39;49;00m[37m [39;49;00m[33m'right-margin-width[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1302	([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-left-fringe-width[39;49;00m[37m [39;49;00m[33m'left-fringe-width[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1303	([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-right-fringe-width[39;49;00m[37m [39;49;00m[33m'right-fringe-width[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1304	([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-fringes-outside-margins[39;49;00m[37m [39;49;00m[33m'fringes-outside-margins[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1305	([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-scroll-bar-width[39;49;00m[37m [39;49;00m[33m'scroll-bar-width[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1306	([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-vertical-scroll-bar[39;49;00m[37m [39;49;00m[33m'vertical-scroll-bar[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1307	([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-indicate-empty-lines[39;49;00m[37m [39;49;00m[33m'indicate-empty-lines[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1308	([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-indicate-buffer-boundaries[39;49;00m[37m [39;49;00m[33m'indicate-buffer-boundaries[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1309	([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-fringe-indicator-alist[39;49;00m[37m [39;49;00m[33m'fringe-indicator-alist[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1310	([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-fringe-cursor-alist[39;49;00m[37m [39;49;00m[33m'fringe-cursor-alist[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1311	([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-scroll-up-aggressively[39;49;00m[37m [39;49;00m[33m'scroll-up-aggressively[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1312	([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-scroll-down-aggressively[39;49;00m[37m [39;49;00m[33m'scroll-down-aggressively[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1313	([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-fill-column[39;49;00m[37m [39;49;00m[33m'fill-column[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1314	([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-cursor-type[39;49;00m[37m [39;49;00m[33m'cursor-type[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1315	([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-cursor-in-non-selected-windows[39;49;00m[37m [39;49;00m[33m'cursor-in-non-selected-windows[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1316	([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-buffer-file-coding-system[39;49;00m[37m [39;49;00m[33m'buffer-file-coding-system[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1317	([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-major-mode[39;49;00m[37m [39;49;00m[33m'major-mode[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1318	([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-enable-multibyte-characters[39;49;00m[37m[39;49;00m
  1319	[37m      [39;49;00m[33m"[39;49;00m[33muse enable-multibyte-characters or set-buffer-multibyte instead[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1320	[37m[39;49;00m
  1321	([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'define-key-rebound-commands[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1322	([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'redisplay-end-trigger-functions[39;49;00m[37m [39;49;00m[33m'jit-lock-register[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1323	([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'deferred-action-list[39;49;00m[37m [39;49;00m[33m'post-command-hook[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m24.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1324	([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'deferred-action-function[39;49;00m[37m [39;49;00m[33m'post-command-hook[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m24.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1325	([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'redisplay-dont-pause[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m24.5[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1326	([31mmake-obsolete[39;49;00m[37m [39;49;00m[33m'window-redisplay-end-trigger[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1327	([31mmake-obsolete[39;49;00m[37m [39;49;00m[33m'set-window-redisplay-end-trigger[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1328	[37m[39;49;00m
  1329	([31mmake-obsolete[39;49;00m[37m [39;49;00m[33m'process-filter-multibyte-p[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1330	([31mmake-obsolete[39;49;00m[37m [39;49;00m[33m'set-process-filter-multibyte[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1331	[37m[39;49;00m
  1332	[37m;; Lisp manual only updated in 22.1.[39;49;00m[37m[39;49;00m
  1333	([36mdefine-obsolete-variable-alias[39;49;00m[37m [39;49;00m[33m'executing-macro[39;49;00m[37m [39;49;00m[33m'executing-kbd-macro[39;49;00m[37m[39;49;00m
  1334	[37m  [39;49;00m[33m"[39;49;00m[33mbefore 19.34[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1335	[37m[39;49;00m
  1336	([36mdefine-obsolete-variable-alias[39;49;00m[37m [39;49;00m[33m'x-lost-selection-hooks[39;49;00m[37m[39;49;00m
  1337	[37m  [39;49;00m[33m'x-lost-selection-functions[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m22.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1338	([36mdefine-obsolete-variable-alias[39;49;00m[37m [39;49;00m[33m'x-sent-selection-hooks[39;49;00m[37m[39;49;00m
  1339	[37m  [39;49;00m[33m'x-sent-selection-functions[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m22.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1340	[37m[39;49;00m
  1341	[37m;; This was introduced in 21.4 for pre-unicode unification.  That[39;49;00m[37m[39;49;00m
  1342	[37m;; usage was rendered obsolete in 23.1 which uses Unicode internally.[39;49;00m[37m[39;49;00m
  1343	[37m;; Other uses are possible, so this variable is not _really_ obsolete,[39;49;00m[37m[39;49;00m
  1344	[37m;; but Stefan insists to mark it so.[39;49;00m[37m[39;49;00m
  1345	([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'translation-table-for-input[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1346	[37m[39;49;00m
  1347	([36mdefvaralias[39;49;00m[37m [39;49;00m[33m'messages-buffer-max-lines[39;49;00m[37m [39;49;00m[33m'message-log-max[39;49;00m)[37m[39;49;00m
  1348	[37m[39;49;00m[37m[39;49;00m
  1349	[37m;;;; Alternate names for functions - these are not being phased out.[39;49;00m[37m[39;49;00m
  1350	[37m[39;49;00m
  1351	([36mdefalias[39;49;00m[37m [39;49;00m[33m'send-string[39;49;00m[37m [39;49;00m[33m'process-send-string[39;49;00m)[37m[39;49;00m
  1352	([36mdefalias[39;49;00m[37m [39;49;00m[33m'send-region[39;49;00m[37m [39;49;00m[33m'process-send-region[39;49;00m)[37m[39;49;00m
  1353	([36mdefalias[39;49;00m[37m [39;49;00m[33m'string=[39;49;00m[37m [39;49;00m[33m'string-equal[39;49;00m)[37m[39;49;00m
  1354	([36mdefalias[39;49;00m[37m [39;49;00m[33m'string<[39;49;00m[37m [39;49;00m[33m'string-lessp[39;49;00m)[37m[39;49;00m
  1355	([36mdefalias[39;49;00m[37m [39;49;00m[33m'move-marker[39;49;00m[37m [39;49;00m[33m'set-marker[39;49;00m)[37m[39;49;00m
  1356	([36mdefalias[39;49;00m[37m [39;49;00m[33m'rplaca[39;49;00m[37m [39;49;00m[33m'setcar[39;49;00m)[37m[39;49;00m
  1357	([36mdefalias[39;49;00m[37m [39;49;00m[33m'rplacd[39;49;00m[37m [39;49;00m[33m'setcdr[39;49;00m)[37m[39;49;00m
  1358	([36mdefalias[39;49;00m[37m [39;49;00m[33m'beep[39;49;00m[37m [39;49;00m[33m'ding[39;49;00m)[37m [39;49;00m[37m;preserve lingual purity[39;49;00m[37m[39;49;00m
  1359	([36mdefalias[39;49;00m[37m [39;49;00m[33m'indent-to-column[39;49;00m[37m [39;49;00m[33m'indent-to[39;49;00m)[37m[39;49;00m
  1360	([36mdefalias[39;49;00m[37m [39;49;00m[33m'backward-delete-char[39;49;00m[37m [39;49;00m[33m'delete-backward-char[39;49;00m)[37m[39;49;00m
  1361	([36mdefalias[39;49;00m[37m [39;49;00m[33m'search-forward-regexp[39;49;00m[37m [39;49;00m([32msymbol-function[39;49;00m[37m [39;49;00m[33m're-search-forward[39;49;00m))[37m[39;49;00m
  1362	([36mdefalias[39;49;00m[37m [39;49;00m[33m'search-backward-regexp[39;49;00m[37m [39;49;00m([32msymbol-function[39;49;00m[37m [39;49;00m[33m're-search-backward[39;49;00m))[37m[39;49;00m
  1363	([36mdefalias[39;49;00m[37m [39;49;00m[33m'int-to-string[39;49;00m[37m [39;49;00m[33m'number-to-string[39;49;00m)[37m[39;49;00m
  1364	([36mdefalias[39;49;00m[37m [39;49;00m[33m'store-match-data[39;49;00m[37m [39;49;00m[33m'set-match-data[39;49;00m)[37m[39;49;00m
  1365	([36mdefalias[39;49;00m[37m [39;49;00m[33m'chmod[39;49;00m[37m [39;49;00m[33m'set-file-modes[39;49;00m)[37m[39;49;00m
  1366	([36mdefalias[39;49;00m[37m [39;49;00m[33m'mkdir[39;49;00m[37m [39;49;00m[33m'make-directory[39;49;00m)[37m[39;49;00m
  1367	[37m;; These are the XEmacs names:[39;49;00m[37m[39;49;00m
  1368	([36mdefalias[39;49;00m[37m [39;49;00m[33m'point-at-eol[39;49;00m[37m [39;49;00m[33m'line-end-position[39;49;00m)[37m[39;49;00m
  1369	([36mdefalias[39;49;00m[37m [39;49;00m[33m'point-at-bol[39;49;00m[37m [39;49;00m[33m'line-beginning-position[39;49;00m)[37m[39;49;00m
  1370	[37m[39;49;00m
  1371	([36mdefalias[39;49;00m[37m [39;49;00m[33m'user-original-login-name[39;49;00m[37m [39;49;00m[33m'user-login-name[39;49;00m)[37m[39;49;00m
  1372	[37m[39;49;00m
  1373	[37m[39;49;00m[37m[39;49;00m
  1374	[37m;;;; Hook manipulation functions.[39;49;00m[37m[39;49;00m
  1375	[37m[39;49;00m
  1376	([36mdefun[39;49;00m[37m [39;49;00m[31madd-hook[39;49;00m[37m [39;49;00m([31mhook[39;49;00m[37m [39;49;00m[34mfunction[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[32mappend[39;49;00m[37m [39;49;00m[31mlocal[39;49;00m)[37m[39;49;00m
  1377	[37m  [39;49;00m[33m"[39;49;00m[33mAdd to the value of HOOK the function FUNCTION.[39;49;00m
  1378	[33mFUNCTION is not added if already present.[39;49;00m
  1379	[33mFUNCTION is added (if necessary) at the beginning of the hook list[39;49;00m
  1380	[33munless the optional argument APPEND is non-nil, in which case[39;49;00m
  1381	[33mFUNCTION is added at the end.[39;49;00m
  1382	[33m[39;49;00m
  1383	[33mThe optional fourth argument, LOCAL, if non-nil, says to modify[39;49;00m
  1384	[33mthe hook's buffer-local value rather than its global value.[39;49;00m
  1385	[33mThis makes the hook buffer-local, and it makes t a member of the[39;49;00m
  1386	[33mbuffer-local value.  That acts as a flag to run the hook[39;49;00m
  1387	[33mfunctions of the global value as well as in the local value.[39;49;00m
  1388	[33m[39;49;00m
  1389	[33mHOOK should be a symbol, and FUNCTION may be any valid function.  If[39;49;00m
  1390	[33mHOOK is void, it is first set to nil.  If HOOK's value is a single[39;49;00m
  1391	[33mfunction, it is changed to a list of functions.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  1392	[37m  [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mboundp[39;49;00m[37m [39;49;00m[31mhook[39;49;00m)[37m [39;49;00m([32mset[39;49;00m[37m [39;49;00m[31mhook[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m
  1393	[37m  [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mdefault-boundp[39;49;00m[37m [39;49;00m[31mhook[39;49;00m)[37m [39;49;00m([32mset-default[39;49;00m[37m [39;49;00m[31mhook[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m
  1394	[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mlocal[39;49;00m[37m [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32mlocal-variable-if-set-p[39;49;00m[37m [39;49;00m[31mhook[39;49;00m)[37m[39;49;00m
  1395	[37m	      [39;49;00m([32mset[39;49;00m[37m [39;49;00m([32mmake-local-variable[39;49;00m[37m [39;49;00m[31mhook[39;49;00m)[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[31mt[39;49;00m)))[37m[39;49;00m
  1396	[37m    [39;49;00m[37m;; Detect the case where make-local-variable was used on a hook[39;49;00m[37m[39;49;00m
  1397	[37m    [39;49;00m[37m;; and do what we used to do.[39;49;00m[37m[39;49;00m
  1398	[37m    [39;49;00m([36munless[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mhook[39;49;00m))[37m [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mhook[39;49;00m)))[37m[39;49;00m
  1399	[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mlocal[39;49;00m[37m [39;49;00m[31mt[39;49;00m)))[37m[39;49;00m
  1400	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mhook-value[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mlocal[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mhook[39;49;00m)[37m [39;49;00m([32mdefault-value[39;49;00m[37m [39;49;00m[31mhook[39;49;00m))))[37m[39;49;00m
  1401	[37m    [39;49;00m[37m;; If the hook value is a single function, turn it into a list.[39;49;00m[37m[39;49;00m
  1402	[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mlistp[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m))[37m [39;49;00m([32mfunctionp[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m))[37m[39;49;00m
  1403	[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m)))[37m[39;49;00m
  1404	[37m    [39;49;00m[37m;; Do the actual addition if necessary[39;49;00m[37m[39;49;00m
  1405	[37m    [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32mmember[39;49;00m[37m [39;49;00m[34mfunction[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m)[37m[39;49;00m
  1406	[37m      [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m[34mfunction[39;49;00m)[37m[39;49;00m
  1407	[37m	[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[34mfunction[39;49;00m[37m [39;49;00m([32mpurecopy[39;49;00m[37m [39;49;00m[34mfunction[39;49;00m)))[37m[39;49;00m
  1408	[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m[37m[39;49;00m
  1409	[37m	    [39;49;00m([34mif[39;49;00m[37m [39;49;00m[32mappend[39;49;00m[37m[39;49;00m
  1410	[37m		[39;49;00m([32mappend[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[34mfunction[39;49;00m))[37m[39;49;00m
  1411	[37m	      [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[34mfunction[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m))))[37m[39;49;00m
  1412	[37m    [39;49;00m[37m;; Set the actual variable[39;49;00m[37m[39;49;00m
  1413	[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mlocal[39;49;00m[37m[39;49;00m
  1414	[37m	[39;49;00m([34mprogn[39;49;00m[37m[39;49;00m
  1415	[37m	  [39;49;00m[37m;; If HOOK isn't a permanent local,[39;49;00m[37m[39;49;00m
  1416	[37m	  [39;49;00m[37m;; but FUNCTION wants to survive a change of modes,[39;49;00m[37m[39;49;00m
  1417	[37m	  [39;49;00m[37m;; mark HOOK as partially permanent.[39;49;00m[37m[39;49;00m
  1418	[37m	  [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32msymbolp[39;49;00m[37m [39;49;00m[34mfunction[39;49;00m)[37m[39;49;00m
  1419	[37m	       [39;49;00m([32mget[39;49;00m[37m [39;49;00m[34mfunction[39;49;00m[37m [39;49;00m[33m'permanent-local-hook[39;49;00m)[37m[39;49;00m
  1420	[37m	       [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mget[39;49;00m[37m [39;49;00m[31mhook[39;49;00m[37m [39;49;00m[33m'permanent-local[39;49;00m))[37m[39;49;00m
  1421	[37m	       [39;49;00m([32mput[39;49;00m[37m [39;49;00m[31mhook[39;49;00m[37m [39;49;00m[33m'permanent-local[39;49;00m[37m [39;49;00m[33m'permanent-local-hook[39;49;00m))[37m[39;49;00m
  1422	[37m	  [39;49;00m([32mset[39;49;00m[37m [39;49;00m[31mhook[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m))[37m[39;49;00m
  1423	[37m      [39;49;00m([32mset-default[39;49;00m[37m [39;49;00m[31mhook[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m))))[37m[39;49;00m
  1424	[37m[39;49;00m
  1425	([36mdefun[39;49;00m[37m [39;49;00m[31mremove-hook[39;49;00m[37m [39;49;00m([31mhook[39;49;00m[37m [39;49;00m[34mfunction[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mlocal[39;49;00m)[37m[39;49;00m
  1426	[37m  [39;49;00m[33m"[39;49;00m[33mRemove from the value of HOOK the function FUNCTION.[39;49;00m
  1427	[33mHOOK should be a symbol, and FUNCTION may be any valid function.  If[39;49;00m
  1428	[33mFUNCTION isn't the value of HOOK, or, if FUNCTION doesn't appear in the[39;49;00m
  1429	[33mlist of hooks to run in HOOK, then nothing is done.  See [39;49;00m[33m`add-hook'[39;49;00m[33m.[39;49;00m
  1430	[33m[39;49;00m
  1431	[33mThe optional third argument, LOCAL, if non-nil, says to modify[39;49;00m
  1432	[33mthe hook's buffer-local value rather than its default value.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  1433	[37m  [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mboundp[39;49;00m[37m [39;49;00m[31mhook[39;49;00m)[37m [39;49;00m([32mset[39;49;00m[37m [39;49;00m[31mhook[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m
  1434	[37m  [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mdefault-boundp[39;49;00m[37m [39;49;00m[31mhook[39;49;00m)[37m [39;49;00m([32mset-default[39;49;00m[37m [39;49;00m[31mhook[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m
  1435	[37m  [39;49;00m[37m;; Do nothing if LOCAL is t but this hook has no local binding.[39;49;00m[37m[39;49;00m
  1436	[37m  [39;49;00m([36munless[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mlocal[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mlocal-variable-p[39;49;00m[37m [39;49;00m[31mhook[39;49;00m)))[37m[39;49;00m
  1437	[37m    [39;49;00m[37m;; Detect the case where make-local-variable was used on a hook[39;49;00m[37m[39;49;00m
  1438	[37m    [39;49;00m[37m;; and do what we used to do.[39;49;00m[37m[39;49;00m
  1439	[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mlocal-variable-p[39;49;00m[37m [39;49;00m[31mhook[39;49;00m)[37m[39;49;00m
  1440	[37m	       [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mhook[39;49;00m))[37m[39;49;00m
  1441	[37m			 [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mhook[39;49;00m)))))[37m[39;49;00m
  1442	[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mlocal[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m
  1443	[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mhook-value[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mlocal[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mhook[39;49;00m)[37m [39;49;00m([32mdefault-value[39;49;00m[37m [39;49;00m[31mhook[39;49;00m))))[37m[39;49;00m
  1444	[37m      [39;49;00m[37m;; Remove the function, for both the list and the non-list cases.[39;49;00m[37m[39;49;00m
  1445	[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mlistp[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m))[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m)[37m [39;49;00m[33m'lambda[39;49;00m))[37m[39;49;00m
  1446	[37m	  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mequal[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m[37m [39;49;00m[34mfunction[39;49;00m)[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m
  1447	[37m	[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m[37m [39;49;00m([32mdelete[39;49;00m[37m [39;49;00m[34mfunction[39;49;00m[37m [39;49;00m([32mcopy-sequence[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m))))[37m[39;49;00m
  1448	[37m      [39;49;00m[37m;; If the function is on the global hook, we need to shadow it locally[39;49;00m[37m[39;49;00m
  1449	[37m      [39;49;00m[37m;;(when (and local (member function (default-value hook))[39;49;00m[37m[39;49;00m
  1450	[37m      [39;49;00m[37m;;	       (not (member (cons 'not function) hook-value)))[39;49;00m[37m[39;49;00m
  1451	[37m      [39;49;00m[37m;;  (push (cons 'not function) hook-value))[39;49;00m[37m[39;49;00m
  1452	[37m      [39;49;00m[37m;; Set the actual variable[39;49;00m[37m[39;49;00m
  1453	[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m[31mlocal[39;49;00m)[37m[39;49;00m
  1454	[37m	  [39;49;00m([32mset-default[39;49;00m[37m [39;49;00m[31mhook[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m)[37m[39;49;00m
  1455	[37m	[39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mequal[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m[37m [39;49;00m'([31mt[39;49;00m))[37m[39;49;00m
  1456	[37m	    [39;49;00m([32mkill-local-variable[39;49;00m[37m [39;49;00m[31mhook[39;49;00m)[37m[39;49;00m
  1457	[37m	  [39;49;00m([32mset[39;49;00m[37m [39;49;00m[31mhook[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m))))))[37m[39;49;00m
  1458	[37m[39;49;00m
  1459	([36mdefmacro[39;49;00m[37m [39;49;00m[36mletrec[39;49;00m[37m [39;49;00m([31mbinders[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m
  1460	[37m  [39;49;00m[33m"[39;49;00m[33mBind variables according to BINDERS then eval BODY.[39;49;00m
  1461	[33mThe value of the last form in BODY is returned.[39;49;00m
  1462	[33mEach element of BINDERS is a list (SYMBOL VALUEFORM) which binds[39;49;00m
  1463	[33mSYMBOL to the value of VALUEFORM.[39;49;00m
  1464	[33mAll symbols are bound before the VALUEFORMs are evalled.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  1465	[37m  [39;49;00m[37m;; Only useful in lexical-binding mode.[39;49;00m[37m[39;49;00m
  1466	[37m  [39;49;00m[37m;; As a special-form, we could implement it more efficiently (and cleanly,[39;49;00m[37m[39;49;00m
  1467	[37m  [39;49;00m[37m;; making the vars actually unbound during evaluation of the binders).[39;49;00m[37m[39;49;00m
  1468	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[34mlet[39;49;00m)[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m1[39;49;00m))[37m[39;49;00m
  1469	[37m  [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m,([32mmapcar[39;49;00m[37m [39;49;00m[32m#'[39;49;00m[32mcar[39;49;00m[37m [39;49;00m[31mbinders[39;49;00m)[37m[39;49;00m
  1470	[37m     [39;49;00m,@([32mmapcar[39;49;00m[37m [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31mbinder[39;49;00m)[37m [39;49;00m`([34msetq[39;49;00m[37m [39;49;00m,@[31mbinder[39;49;00m))[37m [39;49;00m[31mbinders[39;49;00m)[37m[39;49;00m
  1471	[37m     [39;49;00m,@[31mbody[39;49;00m))[37m[39;49;00m
  1472	[37m[39;49;00m
  1473	([36mdefmacro[39;49;00m[37m [39;49;00m[36mwith-wrapper-hook[39;49;00m[37m [39;49;00m([31mhook[39;49;00m[37m [39;49;00m[31margs[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m
  1474	[37m  [39;49;00m[33m"[39;49;00m[33mRun BODY, using wrapper functions from HOOK with additional ARGS.[39;49;00m
  1475	[33mHOOK is an abnormal hook.  Each hook function in HOOK [39;49;00m[33m\"[39;49;00m[33mwraps[39;49;00m[33m\"[39;49;00m[33m[39;49;00m
  1476	[33maround the preceding ones, like a set of nested [39;49;00m[33m`around'[39;49;00m[33m advices.[39;49;00m
  1477	[33m[39;49;00m
  1478	[33mEach hook function should accept an argument list consisting of a[39;49;00m
  1479	[33mfunction FUN, followed by the additional arguments in ARGS.[39;49;00m
  1480	[33m[39;49;00m
  1481	[33mThe first hook function in HOOK is passed a FUN that, if it is called[39;49;00m
  1482	[33mwith arguments ARGS, performs BODY (i.e., the default operation).[39;49;00m
  1483	[33mThe FUN passed to each successive hook function is defined based[39;49;00m
  1484	[33mon the preceding hook functions; if called with arguments ARGS,[39;49;00m
  1485	[33mit does what the [39;49;00m[33m`with-wrapper-hook'[39;49;00m[33m call would do if the[39;49;00m
  1486	[33mpreceding hook functions were the only ones present in HOOK.[39;49;00m
  1487	[33m[39;49;00m
  1488	[33mEach hook function may call its FUN argument as many times as it wishes,[39;49;00m
  1489	[33mincluding never.  In that case, such a hook function acts to replace[39;49;00m
  1490	[33mthe default definition altogether, and any preceding hook functions.[39;49;00m
  1491	[33mOf course, a subsequent hook function may do the same thing.[39;49;00m
  1492	[33m[39;49;00m
  1493	[33mEach hook function definition is used to construct the FUN passed[39;49;00m
  1494	[33mto the next hook function, if any.  The last (or [39;49;00m[33m\"[39;49;00m[33moutermost[39;49;00m[33m\"[39;49;00m[33m)[39;49;00m
  1495	[33mFUN is then called once.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  1496	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m2[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m([31mform[39;49;00m[37m [39;49;00m[31msexp[39;49;00m[37m [39;49;00m[31mbody[39;49;00m))[37m[39;49;00m
  1497	[37m           [39;49;00m([31mobsolete[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33muse a <foo>-function variable modified by [39;49;00m[33m`add-function'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  1498	[37m                     [39;49;00m[33m"[39;49;00m[33m24.4[39;49;00m[33m"[39;49;00m))[37m[39;49;00m
  1499	[37m  [39;49;00m[37m;; We need those two gensyms because CL's lexical scoping is not available[39;49;00m[37m[39;49;00m
  1500	[37m  [39;49;00m[37m;; for function arguments :-([39;49;00m[37m[39;49;00m
  1501	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mfuns[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mfuns[39;49;00m[33m"[39;49;00m))[37m[39;49;00m
  1502	[37m        [39;49;00m([31mglobal[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mglobal[39;49;00m[33m"[39;49;00m))[37m[39;49;00m
  1503	[37m        [39;49;00m([31margssym[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33margs[39;49;00m[33m"[39;49;00m))[37m[39;49;00m
  1504	[37m        [39;49;00m([31mrunrestofhook[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mrunrestofhook[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m
  1505	[37m    [39;49;00m[37m;; Since the hook is a wrapper, the loop has to be done via[39;49;00m[37m[39;49;00m
  1506	[37m    [39;49;00m[37m;; recursion: a given hook function will call its parameter in order to[39;49;00m[37m[39;49;00m
  1507	[37m    [39;49;00m[37m;; continue looping.[39;49;00m[37m[39;49;00m
  1508	[37m    [39;49;00m`([36mletrec[39;49;00m[37m [39;49;00m((,[31mrunrestofhook[39;49;00m[37m[39;49;00m
  1509	[37m               [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m(,[31mfuns[39;49;00m[37m [39;49;00m,[31mglobal[39;49;00m[37m [39;49;00m,[31margssym[39;49;00m)[37m[39;49;00m
  1510	[37m                 [39;49;00m[37m;; `funs' holds the functions left on the hook and `global'[39;49;00m[37m[39;49;00m
  1511	[37m                 [39;49;00m[37m;; holds the functions left on the global part of the hook[39;49;00m[37m[39;49;00m
  1512	[37m                 [39;49;00m[37m;; (in case the hook is local).[39;49;00m[37m[39;49;00m
  1513	[37m                 [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m,[31mfuns[39;49;00m)[37m[39;49;00m
  1514	[37m                     [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m,[31mfuns[39;49;00m))[37m[39;49;00m
  1515	[37m                         [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m,[31mrunrestofhook[39;49;00m[37m[39;49;00m
  1516	[37m                                  [39;49;00m([32mappend[39;49;00m[37m [39;49;00m,[31mglobal[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m,[31mfuns[39;49;00m))[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m,[31margssym[39;49;00m)[37m[39;49;00m
  1517	[37m                       [39;49;00m([32mapply[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m,[31mfuns[39;49;00m)[37m[39;49;00m
  1518	[37m                              [39;49;00m([31mapply-partially[39;49;00m[37m[39;49;00m
  1519	[37m                               [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m(,[31mfuns[39;49;00m[37m [39;49;00m,[31mglobal[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m,[31margssym[39;49;00m)[37m[39;49;00m
  1520	[37m                                 [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m,[31mrunrestofhook[39;49;00m[37m [39;49;00m,[31mfuns[39;49;00m[37m [39;49;00m,[31mglobal[39;49;00m[37m [39;49;00m,[31margssym[39;49;00m))[37m[39;49;00m
  1521	[37m                               [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m,[31mfuns[39;49;00m)[37m [39;49;00m,[31mglobal[39;49;00m)[37m[39;49;00m
  1522	[37m                              [39;49;00m,[31margssym[39;49;00m))[37m[39;49;00m
  1523	[37m                   [39;49;00m[37m;; Once there are no more functions on the hook, run[39;49;00m[37m[39;49;00m
  1524	[37m                   [39;49;00m[37m;; the original body.[39;49;00m[37m[39;49;00m
  1525	[37m                   [39;49;00m([32mapply[39;49;00m[37m [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m,[31margs[39;49;00m[37m [39;49;00m,@[31mbody[39;49;00m)[37m [39;49;00m,[31margssym[39;49;00m)))))[37m[39;49;00m
  1526	[37m       [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m,[31mrunrestofhook[39;49;00m[37m [39;49;00m,[31mhook[39;49;00m[37m[39;49;00m
  1527	[37m                [39;49;00m[37m;; The global part of the hook, if any.[39;49;00m[37m[39;49;00m
  1528	[37m                [39;49;00m,([34mif[39;49;00m[37m [39;49;00m([32msymbolp[39;49;00m[37m [39;49;00m[31mhook[39;49;00m)[37m[39;49;00m
  1529	[37m                     [39;49;00m`([34mif[39;49;00m[37m [39;49;00m([32mlocal-variable-p[39;49;00m[37m [39;49;00m[33m',hook[39;49;00m)[37m[39;49;00m
  1530	[37m                          [39;49;00m([32mdefault-value[39;49;00m[37m [39;49;00m[33m',hook[39;49;00m)))[37m[39;49;00m
  1531	[37m                [39;49;00m([32mlist[39;49;00m[37m [39;49;00m,@[31margs[39;49;00m)))))[37m[39;49;00m
  1532	[37m[39;49;00m
  1533	([36mdefun[39;49;00m[37m [39;49;00m[31madd-to-list[39;49;00m[37m [39;49;00m([31mlist-var[39;49;00m[37m [39;49;00m[31melement[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[32mappend[39;49;00m[37m [39;49;00m[31mcompare-fn[39;49;00m)[37m[39;49;00m
  1534	[37m  [39;49;00m[33m"[39;49;00m[33mAdd ELEMENT to the value of LIST-VAR if it isn't there yet.[39;49;00m
  1535	[33mThe test for presence of ELEMENT is done with [39;49;00m[33m`equal'[39;49;00m[33m, or with[39;49;00m
  1536	[33mCOMPARE-FN if that's non-nil.[39;49;00m
  1537	[33mIf ELEMENT is added, it is added at the beginning of the list,[39;49;00m
  1538	[33munless the optional argument APPEND is non-nil, in which case[39;49;00m
  1539	[33mELEMENT is added at the end.[39;49;00m
  1540	[33m[39;49;00m
  1541	[33mThe return value is the new value of LIST-VAR.[39;49;00m
  1542	[33m[39;49;00m
  1543	[33mThis is handy to add some elements to configuration variables,[39;49;00m
  1544	[33mbut please do not abuse it in Elisp code, where you are usually[39;49;00m
  1545	[33mbetter off using [39;49;00m[33m`push'[39;49;00m[33m or [39;49;00m[33m`cl-pushnew'[39;49;00m[33m.[39;49;00m
  1546	[33m[39;49;00m
  1547	[33mIf you want to use [39;49;00m[33m`add-to-list'[39;49;00m[33m on a variable that is not[39;49;00m
  1548	[33mdefined until a certain package is loaded, you should put the[39;49;00m
  1549	[33mcall to [39;49;00m[33m`add-to-list'[39;49;00m[33m into a hook function that will be run only[39;49;00m
  1550	[33mafter loading the package.  [39;49;00m[33m`eval-after-load'[39;49;00m[33m provides one way to[39;49;00m
  1551	[33mdo this.  In some cases other hooks, such as major mode hooks,[39;49;00m
  1552	[33mcan do the job.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  1553	[37m  [39;49;00m([36mdeclare[39;49;00m[37m[39;49;00m
  1554	[37m   [39;49;00m([31mcompiler-macro[39;49;00m[37m[39;49;00m
  1555	[37m    [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([32mexp[39;49;00m)[37m[39;49;00m
  1556	[37m      [39;49;00m[37m;; FIXME: Something like this could be used for `set' as well.[39;49;00m[37m[39;49;00m
  1557	[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[33m'quote[39;49;00m[37m [39;49;00m([32mcar-safe[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m)))[37m[39;49;00m
  1558	[37m              [39;49;00m([32mspecial-variable-p[39;49;00m[37m [39;49;00m([31mcadr[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m))[37m[39;49;00m
  1559	[37m              [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([31mmacroexp-const-p[39;49;00m[37m [39;49;00m[32mappend[39;49;00m)))[37m[39;49;00m
  1560	[37m          [39;49;00m[32mexp[39;49;00m[37m[39;49;00m
  1561	[37m        [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31msym[39;49;00m[37m [39;49;00m([31mcadr[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m))[37m[39;49;00m
  1562	[37m               [39;49;00m([32mappend[39;49;00m[37m [39;49;00m([32meval[39;49;00m[37m [39;49;00m[32mappend[39;49;00m))[37m[39;49;00m
  1563	[37m               [39;49;00m([31mmsg[39;49;00m[37m [39;49;00m([32mformat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m`add-to-list'[39;49;00m[33m can't use lexical var [39;49;00m[33m`%s'[39;49;00m[33m; use [39;49;00m[33m`push'[39;49;00m[33m or [39;49;00m[33m`cl-pushnew'[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  1564	[37m                            [39;49;00m[31msym[39;49;00m))[37m[39;49;00m
  1565	[37m               [39;49;00m[37m;; Big ugly hack so we only output a warning during[39;49;00m[37m[39;49;00m
  1566	[37m               [39;49;00m[37m;; byte-compilation, and so we can use[39;49;00m[37m[39;49;00m
  1567	[37m               [39;49;00m[37m;; byte-compile-not-lexical-var-p to silence the warning[39;49;00m[37m[39;49;00m
  1568	[37m               [39;49;00m[37m;; when a defvar has been seen but not yet executed.[39;49;00m[37m[39;49;00m
  1569	[37m               [39;49;00m([31mwarnfun[39;49;00m[37m [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m()[37m[39;49;00m
  1570	[37m                          [39;49;00m[37m;; FIXME: We should also emit a warning for let-bound[39;49;00m[37m[39;49;00m
  1571	[37m                          [39;49;00m[37m;; variables with dynamic binding.[39;49;00m[37m[39;49;00m
  1572	[37m                          [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32massq[39;49;00m[37m [39;49;00m[31msym[39;49;00m[37m [39;49;00m[31mbyte-compile--lexical-environment[39;49;00m)[37m[39;49;00m
  1573	[37m                            [39;49;00m([31mbyte-compile-log-warning[39;49;00m[37m [39;49;00m[31mmsg[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m[36m:error[39;49;00m))))[37m[39;49;00m
  1574	[37m               [39;49;00m([31mcode[39;49;00m[37m[39;49;00m
  1575	[37m                [39;49;00m([31mmacroexp-let2[39;49;00m[37m [39;49;00m[31mmacroexp-copyable-p[39;49;00m[37m [39;49;00m[31mx[39;49;00m[37m [39;49;00m[31melement[39;49;00m[37m[39;49;00m
  1576	[37m                  [39;49;00m`([34mif[39;49;00m[37m [39;49;00m,([34mif[39;49;00m[37m [39;49;00m[31mcompare-fn[39;49;00m[37m[39;49;00m
  1577	[37m                            [39;49;00m([34mprogn[39;49;00m[37m[39;49;00m
  1578	[37m                              [39;49;00m([36mrequire[39;49;00m[37m [39;49;00m[33m'cl-lib[39;49;00m)[37m[39;49;00m
  1579	[37m                              [39;49;00m`([31mcl-member[39;49;00m[37m [39;49;00m,[31mx[39;49;00m[37m [39;49;00m,[31msym[39;49;00m[37m [39;49;00m[36m:test[39;49;00m[37m [39;49;00m,[31mcompare-fn[39;49;00m))[37m[39;49;00m
  1580	[37m                          [39;49;00m[37m;; For bootstrapping reasons, don't rely on[39;49;00m[37m[39;49;00m
  1581	[37m                          [39;49;00m[37m;; cl--compiler-macro-member for the base case.[39;49;00m[37m[39;49;00m
  1582	[37m                          [39;49;00m`([32mmember[39;49;00m[37m [39;49;00m,[31mx[39;49;00m[37m [39;49;00m,[31msym[39;49;00m))[37m[39;49;00m
  1583	[37m                       [39;49;00m,[31msym[39;49;00m[37m[39;49;00m
  1584	[37m                     [39;49;00m,([34mif[39;49;00m[37m [39;49;00m[32mappend[39;49;00m[37m[39;49;00m
  1585	[37m                          [39;49;00m`([34msetq[39;49;00m[37m [39;49;00m,[31msym[39;49;00m[37m [39;49;00m([32mappend[39;49;00m[37m [39;49;00m,[31msym[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m,[31mx[39;49;00m)))[37m[39;49;00m
  1586	[37m                        [39;49;00m`([36mpush[39;49;00m[37m [39;49;00m,[31mx[39;49;00m[37m [39;49;00m,[31msym[39;49;00m))))))[37m[39;49;00m
  1587	[37m          [39;49;00m([34mif[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([31mmacroexp--compiling-p[39;49;00m))[37m[39;49;00m
  1588	[37m              [39;49;00m[31mcode[39;49;00m[37m[39;49;00m
  1589	[37m            [39;49;00m`([34mprogn[39;49;00m[37m[39;49;00m
  1590	[37m               [39;49;00m([31mmacroexp--funcall-if-compiled[39;49;00m[37m [39;49;00m[33m',warnfun[39;49;00m)[37m[39;49;00m
  1591	[37m               [39;49;00m,[31mcode[39;49;00m)))))))[37m[39;49;00m
  1592	[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mcond[39;49;00m[37m[39;49;00m
  1593	[37m       [39;49;00m(([32mnull[39;49;00m[37m [39;49;00m[31mcompare-fn[39;49;00m)[37m[39;49;00m
  1594	[37m	[39;49;00m([32mmember[39;49;00m[37m [39;49;00m[31melement[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m)))[37m[39;49;00m
  1595	[37m       [39;49;00m(([32meq[39;49;00m[37m [39;49;00m[31mcompare-fn[39;49;00m[37m [39;49;00m[33m'eq[39;49;00m)[37m[39;49;00m
  1596	[37m	[39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[31melement[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m)))[37m[39;49;00m
  1597	[37m       [39;49;00m(([32meq[39;49;00m[37m [39;49;00m[31mcompare-fn[39;49;00m[37m [39;49;00m[33m'eql[39;49;00m)[37m[39;49;00m
  1598	[37m	[39;49;00m([32mmemql[39;49;00m[37m [39;49;00m[31melement[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m)))[37m[39;49;00m
  1599	[37m       [39;49;00m([31mt[39;49;00m[37m[39;49;00m
  1600	[37m	[39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mlst[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m)))[37m[39;49;00m
  1601	[37m	  [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mlst[39;49;00m[37m[39;49;00m
  1602	[37m		      [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mcompare-fn[39;49;00m[37m [39;49;00m[31melement[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mlst[39;49;00m))))[37m[39;49;00m
  1603	[37m	    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mlst[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mlst[39;49;00m)))[37m[39;49;00m
  1604	[37m          [39;49;00m[31mlst[39;49;00m)))[37m[39;49;00m
  1605	[37m      [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m)[37m[39;49;00m
  1606	[37m    [39;49;00m([32mset[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m[37m[39;49;00m
  1607	[37m	 [39;49;00m([34mif[39;49;00m[37m [39;49;00m[32mappend[39;49;00m[37m[39;49;00m
  1608	[37m	     [39;49;00m([32mappend[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m)[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[31melement[39;49;00m))[37m[39;49;00m
  1609	[37m	   [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31melement[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m))))))[37m[39;49;00m
  1610	[37m[39;49;00m
  1611	[37m[39;49;00m
  1612	([36mdefun[39;49;00m[37m [39;49;00m[31madd-to-ordered-list[39;49;00m[37m [39;49;00m([31mlist-var[39;49;00m[37m [39;49;00m[31melement[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31morder[39;49;00m)[37m[39;49;00m
  1613	[37m  [39;49;00m[33m"[39;49;00m[33mAdd ELEMENT to the value of LIST-VAR if it isn't there yet.[39;49;00m
  1614	[33mThe test for presence of ELEMENT is done with [39;49;00m[33m`eq'[39;49;00m[33m.[39;49;00m
  1615	[33m[39;49;00m
  1616	[33mThe resulting list is reordered so that the elements are in the[39;49;00m
  1617	[33morder given by each element's numeric list order.  Elements[39;49;00m
  1618	[33mwithout a numeric list order are placed at the end of the list.[39;49;00m
  1619	[33m[39;49;00m
  1620	[33mIf the third optional argument ORDER is a number (integer or[39;49;00m
  1621	[33mfloat), set the element's list order to the given value.  If[39;49;00m
  1622	[33mORDER is nil or omitted, do not change the numeric order of[39;49;00m
  1623	[33mELEMENT.  If ORDER has any other value, remove the numeric order[39;49;00m
  1624	[33mof ELEMENT if it has one.[39;49;00m
  1625	[33m[39;49;00m
  1626	[33mThe list order for each element is stored in LIST-VAR's[39;49;00m
  1627	[33m`list-order'[39;49;00m[33m property.[39;49;00m
  1628	[33m[39;49;00m
  1629	[33mThe return value is the new value of LIST-VAR.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  1630	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mordering[39;49;00m[37m [39;49;00m([32mget[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m[37m [39;49;00m[33m'list-order[39;49;00m)))[37m[39;49;00m
  1631	[37m    [39;49;00m([36munless[39;49;00m[37m [39;49;00m[31mordering[39;49;00m[37m[39;49;00m
  1632	[37m      [39;49;00m([32mput[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m[37m [39;49;00m[33m'list-order[39;49;00m[37m[39;49;00m
  1633	[37m           [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mordering[39;49;00m[37m [39;49;00m([32mmake-hash-table[39;49;00m[37m [39;49;00m[36m:weakness[39;49;00m[37m [39;49;00m[33m'key[39;49;00m[37m [39;49;00m[36m:test[39;49;00m[37m [39;49;00m[33m'eq[39;49;00m))))[37m[39;49;00m
  1634	[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31morder[39;49;00m[37m[39;49;00m
  1635	[37m      [39;49;00m([32mputhash[39;49;00m[37m [39;49;00m[31melement[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mnumberp[39;49;00m[37m [39;49;00m[31morder[39;49;00m)[37m [39;49;00m[31morder[39;49;00m)[37m [39;49;00m[31mordering[39;49;00m))[37m[39;49;00m
  1636	[37m    [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[31melement[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m))[37m[39;49;00m
  1637	[37m      [39;49;00m([32mset[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31melement[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m))))[37m[39;49;00m
  1638	[37m    [39;49;00m([32mset[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m[37m [39;49;00m([32msort[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m)[37m[39;49;00m
  1639	[37m			[39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31ma[39;49;00m[37m [39;49;00m[31mb[39;49;00m)[37m[39;49;00m
  1640	[37m			  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31moa[39;49;00m[37m [39;49;00m([32mgethash[39;49;00m[37m [39;49;00m[31ma[39;49;00m[37m [39;49;00m[31mordering[39;49;00m))[37m[39;49;00m
  1641	[37m				[39;49;00m([31mob[39;49;00m[37m [39;49;00m([32mgethash[39;49;00m[37m [39;49;00m[31mb[39;49;00m[37m [39;49;00m[31mordering[39;49;00m)))[37m[39;49;00m
  1642	[37m			    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31moa[39;49;00m[37m [39;49;00m[31mob[39;49;00m)[37m[39;49;00m
  1643	[37m				[39;49;00m([32m<[39;49;00m[37m [39;49;00m[31moa[39;49;00m[37m [39;49;00m[31mob[39;49;00m)[37m[39;49;00m
  1644	[37m			      [39;49;00m[31moa[39;49;00m)))))))[37m[39;49;00m
  1645	[37m[39;49;00m
  1646	([36mdefun[39;49;00m[37m [39;49;00m[31madd-to-history[39;49;00m[37m [39;49;00m([31mhistory-var[39;49;00m[37m [39;49;00m[31mnewelt[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mmaxelt[39;49;00m[37m [39;49;00m[31mkeep-all[39;49;00m)[37m[39;49;00m
  1647	[37m  [39;49;00m[33m"[39;49;00m[33mAdd NEWELT to the history list stored in the variable HISTORY-VAR.[39;49;00m
  1648	[33mReturn the new history list.[39;49;00m
  1649	[33mIf MAXELT is non-nil, it specifies the maximum length of the history.[39;49;00m
  1650	[33mOtherwise, the maximum history length is the value of the [39;49;00m[33m`history-length'[39;49;00m[33m[39;49;00m
  1651	[33mproperty on symbol HISTORY-VAR, if set, or the value of the [39;49;00m[33m`history-length'[39;49;00m[33m[39;49;00m
  1652	[33mvariable.[39;49;00m
  1653	[33mRemove duplicates of NEWELT if [39;49;00m[33m`history-delete-duplicates'[39;49;00m[33m is non-nil.[39;49;00m
  1654	[33mIf optional fourth arg KEEP-ALL is non-nil, add NEWELT to history even[39;49;00m
  1655	[33mif it is empty or a duplicate.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  1656	[37m  [39;49;00m([36munless[39;49;00m[37m [39;49;00m[31mmaxelt[39;49;00m[37m[39;49;00m
  1657	[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mmaxelt[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mget[39;49;00m[37m [39;49;00m[31mhistory-var[39;49;00m[37m [39;49;00m[33m'history-length[39;49;00m)[37m[39;49;00m
  1658	[37m		     [39;49;00m[31mhistory-length[39;49;00m)))[37m[39;49;00m
  1659	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mhistory[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mhistory-var[39;49;00m))[37m[39;49;00m
  1660	[37m	[39;49;00m[31mtail[39;49;00m)[37m[39;49;00m
  1661	[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mlistp[39;49;00m[37m [39;49;00m[31mhistory[39;49;00m)[37m[39;49;00m
  1662	[37m	       [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mkeep-all[39;49;00m[37m[39;49;00m
  1663	[37m		   [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m[31mnewelt[39;49;00m))[37m[39;49;00m
  1664	[37m		   [39;49;00m([32m>[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31mnewelt[39;49;00m)[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m
  1665	[37m	       [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mkeep-all[39;49;00m[37m[39;49;00m
  1666	[37m		   [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mequal[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mhistory[39;49;00m)[37m [39;49;00m[31mnewelt[39;49;00m))))[37m[39;49;00m
  1667	[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mhistory-delete-duplicates[39;49;00m[37m[39;49;00m
  1668	[37m	  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mhistory[39;49;00m[37m [39;49;00m([32mdelete[39;49;00m[37m [39;49;00m[31mnewelt[39;49;00m[37m [39;49;00m[31mhistory[39;49;00m)))[37m[39;49;00m
  1669	[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mhistory[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mnewelt[39;49;00m[37m [39;49;00m[31mhistory[39;49;00m))[37m[39;49;00m
  1670	[37m      [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mintegerp[39;49;00m[37m [39;49;00m[31mmaxelt[39;49;00m)[37m[39;49;00m
  1671	[37m	[39;49;00m([34mif[39;49;00m[37m [39;49;00m([32m=[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[31mmaxelt[39;49;00m)[37m[39;49;00m
  1672	[37m	    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mhistory[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m
  1673	[37m	  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([32mnthcdr[39;49;00m[37m [39;49;00m([32m1-[39;49;00m[37m [39;49;00m[31mmaxelt[39;49;00m)[37m [39;49;00m[31mhistory[39;49;00m))[37m[39;49;00m
  1674	[37m	  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)[37m[39;49;00m
  1675	[37m	    [39;49;00m([32msetcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)))))[37m[39;49;00m
  1676	[37m    [39;49;00m([32mset[39;49;00m[37m [39;49;00m[31mhistory-var[39;49;00m[37m [39;49;00m[31mhistory[39;49;00m)))[37m[39;49;00m
  1677	[37m[39;49;00m
  1678	[37m[39;49;00m[37m[39;49;00m
  1679	[37m;;;; Mode hooks.[39;49;00m[37m[39;49;00m
  1680	[37m[39;49;00m
  1681	([34mdefvar[39;49;00m[37m [39;49;00m[36mdelay-mode-hooks[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m
  1682	[37m  [39;49;00m[33m"[39;49;00m[33mIf non-nil, [39;49;00m[33m`run-mode-hooks'[39;49;00m[33m should delay running the hooks.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1683	([34mdefvar[39;49;00m[37m [39;49;00m[31mdelayed-mode-hooks[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m
  1684	[37m  [39;49;00m[33m"[39;49;00m[33mList of delayed mode hooks waiting to be run.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1685	([32mmake-variable-buffer-local[39;49;00m[37m [39;49;00m[33m'delayed-mode-hooks[39;49;00m)[37m[39;49;00m
  1686	([32mput[39;49;00m[37m [39;49;00m[33m'delay-mode-hooks[39;49;00m[37m [39;49;00m[33m'permanent-local[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m
  1687	[37m[39;49;00m
  1688	([34mdefvar[39;49;00m[37m [39;49;00m[31mchange-major-mode-after-body-hook[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m
  1689	[37m  [39;49;00m[33m"[39;49;00m[33mNormal hook run in major mode functions, before the mode hooks.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1690	[37m[39;49;00m
  1691	([34mdefvar[39;49;00m[37m [39;49;00m[31mafter-change-major-mode-hook[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m
  1692	[37m  [39;49;00m[33m"[39;49;00m[33mNormal hook run at the very end of major mode functions.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1693	[37m[39;49;00m
  1694	([36mdefun[39;49;00m[37m [39;49;00m[31mrun-mode-hooks[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31mhooks[39;49;00m)[37m[39;49;00m
  1695	[37m  [39;49;00m[33m"[39;49;00m[33mRun mode hooks [39;49;00m[33m`delayed-mode-hooks'[39;49;00m[33m and HOOKS, or delay HOOKS.[39;49;00m
  1696	[33mIf the variable [39;49;00m[33m`delay-mode-hooks'[39;49;00m[33m is non-nil, does not run any hooks,[39;49;00m
  1697	[33mjust adds the HOOKS to the list [39;49;00m[33m`delayed-mode-hooks'[39;49;00m[33m.[39;49;00m
  1698	[33mOtherwise, runs hooks in the sequence: [39;49;00m[33m`change-major-mode-after-body-hook'[39;49;00m[33m,[39;49;00m
  1699	[33m`delayed-mode-hooks'[39;49;00m[33m (in reverse order), HOOKS, and finally[39;49;00m
  1700	[33m`after-change-major-mode-hook'[39;49;00m[33m.  Major mode functions should use[39;49;00m
  1701	[33mthis instead of [39;49;00m[33m`run-hooks'[39;49;00m[33m when running their FOO-mode-hook.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  1702	[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m[36mdelay-mode-hooks[39;49;00m[37m[39;49;00m
  1703	[37m      [39;49;00m[37m;; Delaying case.[39;49;00m[37m[39;49;00m
  1704	[37m      [39;49;00m([36mdolist[39;49;00m[37m [39;49;00m([31mhook[39;49;00m[37m [39;49;00m[31mhooks[39;49;00m)[37m[39;49;00m
  1705	[37m	[39;49;00m([36mpush[39;49;00m[37m [39;49;00m[31mhook[39;49;00m[37m [39;49;00m[31mdelayed-mode-hooks[39;49;00m))[37m[39;49;00m
  1706	[37m    [39;49;00m[37m;; Normal case, just run the hook as before plus any delayed hooks.[39;49;00m[37m[39;49;00m
  1707	[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mhooks[39;49;00m[37m [39;49;00m([32mnconc[39;49;00m[37m [39;49;00m([32mnreverse[39;49;00m[37m [39;49;00m[31mdelayed-mode-hooks[39;49;00m)[37m [39;49;00m[31mhooks[39;49;00m))[37m[39;49;00m
  1708	[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mdelayed-mode-hooks[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m
  1709	[37m    [39;49;00m([32mapply[39;49;00m[37m [39;49;00m[33m'run-hooks[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[33m'change-major-mode-after-body-hook[39;49;00m[37m [39;49;00m[31mhooks[39;49;00m))[37m[39;49;00m
  1710	[37m    [39;49;00m([32mrun-hooks[39;49;00m[37m [39;49;00m[33m'after-change-major-mode-hook[39;49;00m)))[37m[39;49;00m
  1711	[37m[39;49;00m
  1712	([36mdefmacro[39;49;00m[37m [39;49;00m[36mdelay-mode-hooks[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m
  1713	[37m  [39;49;00m[33m"[39;49;00m[33mExecute BODY, but delay any [39;49;00m[33m`run-mode-hooks'[39;49;00m[33m.[39;49;00m
  1714	[33mThese hooks will be executed by the first following call to[39;49;00m
  1715	[33m`run-mode-hooks'[39;49;00m[33m that occurs outside any [39;49;00m[33m`delayed-mode-hooks'[39;49;00m[33m form.[39;49;00m
  1716	[33mOnly affects hooks run in the current buffer.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  1717	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m
  1718	[37m  [39;49;00m`([34mprogn[39;49;00m[37m[39;49;00m
  1719	[37m     [39;49;00m([32mmake-local-variable[39;49;00m[37m [39;49;00m[33m'delay-mode-hooks[39;49;00m)[37m[39;49;00m
  1720	[37m     [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([36mdelay-mode-hooks[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m
  1721	[37m       [39;49;00m,@[31mbody[39;49;00m)))[37m[39;49;00m
  1722	[37m[39;49;00m
  1723	[37m;; PUBLIC: find if the current mode derives from another.[39;49;00m[37m[39;49;00m
  1724	[37m[39;49;00m
  1725	([36mdefun[39;49;00m[37m [39;49;00m[31mderived-mode-p[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31mmodes[39;49;00m)[37m[39;49;00m
  1726	[37m  [39;49;00m[33m"[39;49;00m[33mNon-nil if the current major mode is derived from one of MODES.[39;49;00m
  1727	[33mUses the [39;49;00m[33m`derived-mode-parent'[39;49;00m[33m property of the symbol to trace backwards.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  1728	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mparent[39;49;00m[37m [39;49;00m[31mmajor-mode[39;49;00m))[37m[39;49;00m
  1729	[37m    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[31mparent[39;49;00m[37m [39;49;00m[31mmodes[39;49;00m))[37m[39;49;00m
  1730	[37m		[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mparent[39;49;00m[37m [39;49;00m([32mget[39;49;00m[37m [39;49;00m[31mparent[39;49;00m[37m [39;49;00m[33m'derived-mode-parent[39;49;00m))))[37m[39;49;00m
  1731	[37m    [39;49;00m[31mparent[39;49;00m))[37m[39;49;00m
  1732	[37m[39;49;00m[37m[39;49;00m
  1733	[37m;;;; Minor modes.[39;49;00m[37m[39;49;00m
  1734	[37m[39;49;00m
  1735	[37m;; If a minor mode is not defined with define-minor-mode,[39;49;00m[37m[39;49;00m
  1736	[37m;; add it here explicitly.[39;49;00m[37m[39;49;00m
  1737	[37m;; isearch-mode is deliberately excluded, since you should[39;49;00m[37m[39;49;00m
  1738	[37m;; not call it yourself.[39;49;00m[37m[39;49;00m
  1739	([34mdefvar[39;49;00m[37m [39;49;00m[31mminor-mode-list[39;49;00m[37m [39;49;00m'([31mauto-save-mode[39;49;00m[37m [39;49;00m[31mauto-fill-mode[39;49;00m[37m [39;49;00m[31mabbrev-mode[39;49;00m[37m[39;49;00m
  1740	[37m					 [39;49;00m[31moverwrite-mode[39;49;00m[37m [39;49;00m[31mview-mode[39;49;00m[37m[39;49;00m
  1741	[37m                                         [39;49;00m[31mhs-minor-mode[39;49;00m)[37m[39;49;00m
  1742	[37m  [39;49;00m[33m"[39;49;00m[33mList of all minor mode functions.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1743	[37m[39;49;00m
  1744	([36mdefun[39;49;00m[37m [39;49;00m[31madd-minor-mode[39;49;00m[37m [39;49;00m([31mtoggle[39;49;00m[37m [39;49;00m[31mname[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m[37m [39;49;00m[31mafter[39;49;00m[37m [39;49;00m[31mtoggle-fun[39;49;00m)[37m[39;49;00m
  1745	[37m  [39;49;00m[33m"[39;49;00m[33mRegister a new minor mode.[39;49;00m
  1746	[33m[39;49;00m
  1747	[33mThis is an XEmacs-compatibility function.  Use [39;49;00m[33m`define-minor-mode'[39;49;00m[33m instead.[39;49;00m
  1748	[33m[39;49;00m
  1749	[33mTOGGLE is a symbol which is the name of a buffer-local variable that[39;49;00m
  1750	[33mis toggled on or off to say whether the minor mode is active or not.[39;49;00m
  1751	[33m[39;49;00m
  1752	[33mNAME specifies what will appear in the mode line when the minor mode[39;49;00m
  1753	[33mis active.  NAME should be either a string starting with a space, or a[39;49;00m
  1754	[33msymbol whose value is such a string.[39;49;00m
  1755	[33m[39;49;00m
  1756	[33mOptional KEYMAP is the keymap for the minor mode that will be added[39;49;00m
  1757	[33mto [39;49;00m[33m`minor-mode-map-alist'[39;49;00m[33m.[39;49;00m
  1758	[33m[39;49;00m
  1759	[33mOptional AFTER specifies that TOGGLE should be added after AFTER[39;49;00m
  1760	[33min [39;49;00m[33m`minor-mode-alist'[39;49;00m[33m.[39;49;00m
  1761	[33m[39;49;00m
  1762	[33mOptional TOGGLE-FUN is an interactive function to toggle the mode.[39;49;00m
  1763	[33mIt defaults to (and should by convention be) TOGGLE.[39;49;00m
  1764	[33m[39;49;00m
  1765	[33mIf TOGGLE has a non-nil [39;49;00m[33m`[39;49;00m[33m:included' property, an entry for the mode is[39;49;00m
  1766	[33mincluded in the mode-line minor mode menu.[39;49;00m
  1767	[33mIf TOGGLE has a [39;49;00m[33m`[39;49;00m[33m:menu-tag', that is used for the menu item's label.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  1768	[37m  [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[31mtoggle[39;49;00m[37m [39;49;00m[31mminor-mode-list[39;49;00m)[37m[39;49;00m
  1769	[37m    [39;49;00m([36mpush[39;49;00m[37m [39;49;00m[31mtoggle[39;49;00m[37m [39;49;00m[31mminor-mode-list[39;49;00m))[37m[39;49;00m
  1770	[37m[39;49;00m
  1771	[37m  [39;49;00m([36munless[39;49;00m[37m [39;49;00m[31mtoggle-fun[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mtoggle-fun[39;49;00m[37m [39;49;00m[31mtoggle[39;49;00m))[37m[39;49;00m
  1772	[37m  [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mtoggle-fun[39;49;00m[37m [39;49;00m[31mtoggle[39;49;00m)[37m[39;49;00m
  1773	[37m    [39;49;00m([32mput[39;49;00m[37m [39;49;00m[31mtoggle[39;49;00m[37m [39;49;00m[36m:minor-mode-function[39;49;00m[37m [39;49;00m[31mtoggle-fun[39;49;00m))[37m[39;49;00m
  1774	[37m  [39;49;00m[37m;; Add the name to the minor-mode-alist.[39;49;00m[37m[39;49;00m
  1775	[37m  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31mname[39;49;00m[37m[39;49;00m
  1776	[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mexisting[39;49;00m[37m [39;49;00m([32massq[39;49;00m[37m [39;49;00m[31mtoggle[39;49;00m[37m [39;49;00m[31mminor-mode-alist[39;49;00m)))[37m[39;49;00m
  1777	[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mexisting[39;49;00m[37m[39;49;00m
  1778	[37m	  [39;49;00m([32msetcdr[39;49;00m[37m [39;49;00m[31mexisting[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[31mname[39;49;00m))[37m[39;49;00m
  1779	[37m	[39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtail[39;49;00m[37m [39;49;00m[31mminor-mode-alist[39;49;00m)[37m [39;49;00m[31mfound[39;49;00m)[37m[39;49;00m
  1780	[37m	  [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m[31mfound[39;49;00m))[37m[39;49;00m
  1781	[37m	    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mafter[39;49;00m[37m [39;49;00m([31mcaar[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))[37m[39;49;00m
  1782	[37m		[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mfound[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)[37m[39;49;00m
  1783	[37m	      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))))[37m[39;49;00m
  1784	[37m	  [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mfound[39;49;00m[37m[39;49;00m
  1785	[37m	      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mrest[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mfound[39;49;00m)))[37m[39;49;00m
  1786	[37m		[39;49;00m([32msetcdr[39;49;00m[37m [39;49;00m[31mfound[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m
  1787	[37m		[39;49;00m([32mnconc[39;49;00m[37m [39;49;00m[31mfound[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[31mtoggle[39;49;00m[37m [39;49;00m[31mname[39;49;00m))[37m [39;49;00m[31mrest[39;49;00m))[37m[39;49;00m
  1788	[37m	    [39;49;00m([36mpush[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[31mtoggle[39;49;00m[37m [39;49;00m[31mname[39;49;00m)[37m [39;49;00m[31mminor-mode-alist[39;49;00m))))))[37m[39;49;00m
  1789	[37m  [39;49;00m[37m;; Add the toggle to the minor-modes menu if requested.[39;49;00m[37m[39;49;00m
  1790	[37m  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mget[39;49;00m[37m [39;49;00m[31mtoggle[39;49;00m[37m [39;49;00m[36m:included[39;49;00m)[37m[39;49;00m
  1791	[37m    [39;49;00m([32mdefine-key[39;49;00m[37m [39;49;00m[31mmode-line-mode-menu[39;49;00m[37m[39;49;00m
  1792	[37m      [39;49;00m([32mvector[39;49;00m[37m [39;49;00m[31mtoggle[39;49;00m)[37m[39;49;00m
  1793	[37m      [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'menu-item[39;49;00m[37m[39;49;00m
  1794	[37m	    [39;49;00m([32mconcat[39;49;00m[37m[39;49;00m
  1795	[37m	     [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mget[39;49;00m[37m [39;49;00m[31mtoggle[39;49;00m[37m [39;49;00m[36m:menu-tag[39;49;00m)[37m[39;49;00m
  1796	[37m		 [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m[31mname[39;49;00m)[37m [39;49;00m[31mname[39;49;00m[37m [39;49;00m([32msymbol-name[39;49;00m[37m [39;49;00m[31mtoggle[39;49;00m)))[37m[39;49;00m
  1797	[37m	     [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mmode-name[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32msymbolp[39;49;00m[37m [39;49;00m[31mname[39;49;00m)[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mname[39;49;00m))))[37m[39;49;00m
  1798	[37m	       [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m[31mmode-name[39;49;00m)[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m[^ ]+[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mmode-name[39;49;00m))[37m[39;49;00m
  1799	[37m		   [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m ([39;49;00m[33m"[39;49;00m[37m [39;49;00m([31mmatch-string[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[31mmode-name[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m)[39;49;00m[33m"[39;49;00m))))[37m[39;49;00m
  1800	[37m	    [39;49;00m[31mtoggle-fun[39;49;00m[37m[39;49;00m
  1801	[37m	    [39;49;00m[36m:button[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[36m:toggle[39;49;00m[37m [39;49;00m[31mtoggle[39;49;00m))))[37m[39;49;00m
  1802	[37m[39;49;00m
  1803	[37m  [39;49;00m[37m;; Add the map to the minor-mode-map-alist.[39;49;00m[37m[39;49;00m
  1804	[37m  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m[37m[39;49;00m
  1805	[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mexisting[39;49;00m[37m [39;49;00m([32massq[39;49;00m[37m [39;49;00m[31mtoggle[39;49;00m[37m [39;49;00m[31mminor-mode-map-alist[39;49;00m)))[37m[39;49;00m
  1806	[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mexisting[39;49;00m[37m[39;49;00m
  1807	[37m	  [39;49;00m([32msetcdr[39;49;00m[37m [39;49;00m[31mexisting[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m)[37m[39;49;00m
  1808	[37m	[39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtail[39;49;00m[37m [39;49;00m[31mminor-mode-map-alist[39;49;00m)[37m [39;49;00m[31mfound[39;49;00m)[37m[39;49;00m
  1809	[37m	  [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m[31mfound[39;49;00m))[37m[39;49;00m
  1810	[37m	    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mafter[39;49;00m[37m [39;49;00m([31mcaar[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))[37m[39;49;00m
  1811	[37m		[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mfound[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)[37m[39;49;00m
  1812	[37m	      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))))[37m[39;49;00m
  1813	[37m	  [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mfound[39;49;00m[37m[39;49;00m
  1814	[37m	      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mrest[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mfound[39;49;00m)))[37m[39;49;00m
  1815	[37m		[39;49;00m([32msetcdr[39;49;00m[37m [39;49;00m[31mfound[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m
  1816	[37m		[39;49;00m([32mnconc[39;49;00m[37m [39;49;00m[31mfound[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mtoggle[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m))[37m [39;49;00m[31mrest[39;49;00m))[37m[39;49;00m
  1817	[37m	    [39;49;00m([36mpush[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mtoggle[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m)[37m [39;49;00m[31mminor-mode-map-alist[39;49;00m)))))))[37m[39;49;00m
  1818	[37m[39;49;00m[37m[39;49;00m
  1819	[37m;;;; Load history[39;49;00m[37m[39;49;00m
  1820	[37m[39;49;00m
  1821	([36mdefsubst[39;49;00m[37m [39;49;00m[31mautoloadp[39;49;00m[37m [39;49;00m([31mobject[39;49;00m)[37m[39;49;00m
  1822	[37m  [39;49;00m[33m"[39;49;00m[33mNon-nil if OBJECT is an autoload.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  1823	[37m  [39;49;00m([32meq[39;49;00m[37m [39;49;00m[33m'autoload[39;49;00m[37m [39;49;00m([32mcar-safe[39;49;00m[37m [39;49;00m[31mobject[39;49;00m)))[37m[39;49;00m
  1824	[37m[39;49;00m
  1825	[37m;; (defun autoload-type (object)[39;49;00m[37m[39;49;00m
  1826	[37m;;   "Returns the type of OBJECT or `function' or `command' if the type is nil.[39;49;00m[37m[39;49;00m
  1827	[37m;; OBJECT should be an autoload object."[39;49;00m[37m[39;49;00m
  1828	[37m;;   (when (autoloadp object)[39;49;00m[37m[39;49;00m
  1829	[37m;;     (let ((type (nth 3 object)))[39;49;00m[37m[39;49;00m
  1830	[37m;;       (cond ((null type) (if (nth 2 object) 'command 'function))[39;49;00m[37m[39;49;00m
  1831	[37m;;             ((eq 'keymap t) 'macro)[39;49;00m[37m[39;49;00m
  1832	[37m;;             (type)))))[39;49;00m[37m[39;49;00m
  1833	[37m[39;49;00m
  1834	[37m;; (defalias 'autoload-file #'cadr[39;49;00m[37m[39;49;00m
  1835	[37m;;   "Return the name of the file from which AUTOLOAD will be loaded.[39;49;00m[37m[39;49;00m
  1836	[37m;; \n\(fn AUTOLOAD)")[39;49;00m[37m[39;49;00m
  1837	[37m[39;49;00m
  1838	([36mdefun[39;49;00m[37m [39;49;00m[31msymbol-file[39;49;00m[37m [39;49;00m([31msymbol[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mtype[39;49;00m)[37m[39;49;00m
  1839	[37m  [39;49;00m[33m"[39;49;00m[33mReturn the name of the file that defined SYMBOL.[39;49;00m
  1840	[33mThe value is normally an absolute file name.  It can also be nil,[39;49;00m
  1841	[33mif the definition is not associated with any file.  If SYMBOL[39;49;00m
  1842	[33mspecifies an autoloaded function, the value can be a relative[39;49;00m
  1843	[33mfile name without extension.[39;49;00m
  1844	[33m[39;49;00m
  1845	[33mIf TYPE is nil, then any kind of definition is acceptable.  If[39;49;00m
  1846	[33mTYPE is [39;49;00m[33m`defun'[39;49;00m[33m, [39;49;00m[33m`defvar'[39;49;00m[33m, or [39;49;00m[33m`defface'[39;49;00m[33m, that specifies function[39;49;00m
  1847	[33mdefinition, variable definition, or face definition only.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  1848	[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[31mtype[39;49;00m)[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mtype[39;49;00m[37m [39;49;00m[33m'defun[39;49;00m))[37m[39;49;00m
  1849	[37m	   [39;49;00m([32msymbolp[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m)[37m[39;49;00m
  1850	[37m	   [39;49;00m([31mautoloadp[39;49;00m[37m [39;49;00m([32msymbol-function[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m)))[37m[39;49;00m
  1851	[37m      [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m([32msymbol-function[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m))[37m[39;49;00m
  1852	[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mfiles[39;49;00m[37m [39;49;00m[31mload-history[39;49;00m)[37m[39;49;00m
  1853	[37m	  [39;49;00m[31mfile[39;49;00m)[37m[39;49;00m
  1854	[37m      [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m[31mfiles[39;49;00m[37m[39;49;00m
  1855	[37m	[39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mtype[39;49;00m[37m[39;49;00m
  1856	[37m		[39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mtype[39;49;00m[37m [39;49;00m[33m'defvar[39;49;00m)[37m[39;49;00m
  1857	[37m		    [39;49;00m[37m;; Variables are present just as their names.[39;49;00m[37m[39;49;00m
  1858	[37m		    [39;49;00m([32mmember[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mfiles[39;49;00m)))[37m[39;49;00m
  1859	[37m		  [39;49;00m[37m;; Other types are represented as (TYPE . NAME).[39;49;00m[37m[39;49;00m
  1860	[37m		  [39;49;00m([32mmember[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mtype[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m)[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mfiles[39;49;00m))))[37m[39;49;00m
  1861	[37m	      [39;49;00m[37m;; We accept all types, so look for variable def[39;49;00m[37m[39;49;00m
  1862	[37m	      [39;49;00m[37m;; and then for any other kind.[39;49;00m[37m[39;49;00m
  1863	[37m	      [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mmember[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mfiles[39;49;00m)))[37m[39;49;00m
  1864	[37m		  [39;49;00m([32mrassq[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mfiles[39;49;00m)))))[37m[39;49;00m
  1865	[37m	    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mfile[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mfiles[39;49;00m))[37m [39;49;00m[31mfiles[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m
  1866	[37m	[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mfiles[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mfiles[39;49;00m)))[37m[39;49;00m
  1867	[37m      [39;49;00m[31mfile[39;49;00m)))[37m[39;49;00m
  1868	[37m[39;49;00m
  1869	([36mdefun[39;49;00m[37m [39;49;00m[31mlocate-library[39;49;00m[37m [39;49;00m([31mlibrary[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mnosuffix[39;49;00m[37m [39;49;00m[31mpath[39;49;00m[37m [39;49;00m[31minteractive-call[39;49;00m)[37m[39;49;00m
  1870	[37m  [39;49;00m[33m"[39;49;00m[33mShow the precise file name of Emacs library LIBRARY.[39;49;00m
  1871	[33mLIBRARY should be a relative file name of the library, a string.[39;49;00m
  1872	[33mIt can omit the suffix (a.k.a. file-name extension) if NOSUFFIX is[39;49;00m
  1873	[33mnil (which is the default, see below).[39;49;00m
  1874	[33mThis command searches the directories in [39;49;00m[33m`load-path'[39;49;00m[33m like [39;49;00m[33m`[39;49;00m[33m\\[39;49;00m[33m[load-library]'[39;49;00m
  1875	[33mto find the file that [39;49;00m[33m`[39;49;00m[33m\\[39;49;00m[33m[load-library] RET LIBRARY RET' would load.[39;49;00m
  1876	[33mOptional second arg NOSUFFIX non-nil means don't add suffixes [39;49;00m[33m`load-suffixes'[39;49;00m[33m[39;49;00m
  1877	[33mto the specified name LIBRARY.[39;49;00m
  1878	[33m[39;49;00m
  1879	[33mIf the optional third arg PATH is specified, that list of directories[39;49;00m
  1880	[33mis used instead of [39;49;00m[33m`load-path'[39;49;00m[33m.[39;49;00m
  1881	[33m[39;49;00m
  1882	[33mWhen called from a program, the file name is normally returned as a[39;49;00m
  1883	[33mstring.  When run interactively, the argument INTERACTIVE-CALL is t,[39;49;00m
  1884	[33mand the file name is displayed in the echo area.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  1885	[37m  [39;49;00m([34minteractive[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m([32mcompleting-read[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mLocate library: [39;49;00m[33m"[39;49;00m[37m[39;49;00m
  1886	[37m				      [39;49;00m([31mapply-partially[39;49;00m[37m[39;49;00m
  1887	[37m                                       [39;49;00m[33m'locate-file-completion-table[39;49;00m[37m[39;49;00m
  1888	[37m                                       [39;49;00m[31mload-path[39;49;00m[37m [39;49;00m([32mget-load-suffixes[39;49;00m)))[37m[39;49;00m
  1889	[37m		     [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m
  1890	[37m		     [39;49;00m[31mt[39;49;00m))[37m[39;49;00m
  1891	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mfile[39;49;00m[37m [39;49;00m([31mlocate-file[39;49;00m[37m [39;49;00m[31mlibrary[39;49;00m[37m[39;49;00m
  1892	[37m			   [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mpath[39;49;00m[37m [39;49;00m[31mload-path[39;49;00m)[37m[39;49;00m
  1893	[37m			   [39;49;00m([32mappend[39;49;00m[37m [39;49;00m([36munless[39;49;00m[37m [39;49;00m[31mnosuffix[39;49;00m[37m [39;49;00m([32mget-load-suffixes[39;49;00m))[37m[39;49;00m
  1894	[37m				   [39;49;00m[31mload-file-rep-suffixes[39;49;00m))))[37m[39;49;00m
  1895	[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31minteractive-call[39;49;00m[37m[39;49;00m
  1896	[37m	[39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mfile[39;49;00m[37m[39;49;00m
  1897	[37m	    [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mLibrary is file %s[39;49;00m[33m"[39;49;00m[37m [39;49;00m([31mabbreviate-file-name[39;49;00m[37m [39;49;00m[31mfile[39;49;00m))[37m[39;49;00m
  1898	[37m	  [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mNo library %s in search path[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mlibrary[39;49;00m)))[37m[39;49;00m
  1899	[37m    [39;49;00m[31mfile[39;49;00m))[37m[39;49;00m
  1900	[37m[39;49;00m
  1901	[37m[39;49;00m[37m[39;49;00m
  1902	[37m;;;; Process stuff.[39;49;00m[37m[39;49;00m
  1903	[37m[39;49;00m
  1904	([36mdefun[39;49;00m[37m [39;49;00m[31mprocess-lines[39;49;00m[37m [39;49;00m([31mprogram[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31margs[39;49;00m)[37m[39;49;00m
  1905	[37m  [39;49;00m[33m"[39;49;00m[33mExecute PROGRAM with ARGS, returning its output as a list of lines.[39;49;00m
  1906	[33mSignal an error if the program returns with a non-zero exit status.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  1907	[37m  [39;49;00m([36mwith-temp-buffer[39;49;00m[37m[39;49;00m
  1908	[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mstatus[39;49;00m[37m [39;49;00m([32mapply[39;49;00m[37m [39;49;00m[33m'call-process[39;49;00m[37m [39;49;00m[31mprogram[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m([32mcurrent-buffer[39;49;00m)[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31margs[39;49;00m)))[37m[39;49;00m
  1909	[37m      [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mstatus[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m
  1910	[37m	[39;49;00m([36merror[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m%s exited with status %s[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mprogram[39;49;00m[37m [39;49;00m[31mstatus[39;49;00m))[37m[39;49;00m
  1911	[37m      [39;49;00m([32mgoto-char[39;49;00m[37m [39;49;00m([32mpoint-min[39;49;00m))[37m[39;49;00m
  1912	[37m      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m([31mlines[39;49;00m)[37m[39;49;00m
  1913	[37m	[39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32meobp[39;49;00m))[37m[39;49;00m
  1914	[37m	  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mlines[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m([32mbuffer-substring-no-properties[39;49;00m[37m[39;49;00m
  1915	[37m			     [39;49;00m([32mline-beginning-position[39;49;00m)[37m[39;49;00m
  1916	[37m			     [39;49;00m([32mline-end-position[39;49;00m))[37m[39;49;00m
  1917	[37m			    [39;49;00m[31mlines[39;49;00m))[37m[39;49;00m
  1918	[37m	  [39;49;00m([32mforward-line[39;49;00m[37m [39;49;00m[34m1[39;49;00m))[37m[39;49;00m
  1919	[37m	[39;49;00m([32mnreverse[39;49;00m[37m [39;49;00m[31mlines[39;49;00m)))))[37m[39;49;00m
  1920	[37m[39;49;00m
  1921	([36mdefun[39;49;00m[37m [39;49;00m[31mprocess-live-p[39;49;00m[37m [39;49;00m([31mprocess[39;49;00m)[37m[39;49;00m
  1922	[37m  [39;49;00m[33m"[39;49;00m[33mReturns non-nil if PROCESS is alive.[39;49;00m
  1923	[33mA process is considered alive if its status is [39;49;00m[33m`run'[39;49;00m[33m, [39;49;00m[33m`open'[39;49;00m[33m,[39;49;00m
  1924	[33m`listen'[39;49;00m[33m, [39;49;00m[33m`connect'[39;49;00m[33m or [39;49;00m[33m`stop'[39;49;00m[33m.  Value is nil if PROCESS is not a[39;49;00m
  1925	[33mprocess.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  1926	[37m  [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mprocessp[39;49;00m[37m [39;49;00m[31mprocess[39;49;00m)[37m[39;49;00m
  1927	[37m       [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m([32mprocess-status[39;49;00m[37m [39;49;00m[31mprocess[39;49;00m)[37m[39;49;00m
  1928	[37m	     [39;49;00m'([31mrun[39;49;00m[37m [39;49;00m[31mopen[39;49;00m[37m [39;49;00m[31mlisten[39;49;00m[37m [39;49;00m[31mconnect[39;49;00m[37m [39;49;00m[31mstop[39;49;00m))))[37m[39;49;00m
  1929	[37m[39;49;00m
  1930	[37m;; compatibility[39;49;00m[37m[39;49;00m
  1931	[37m[39;49;00m
  1932	([31mmake-obsolete[39;49;00m[37m[39;49;00m
  1933	[37m [39;49;00m[33m'process-kill-without-query[39;49;00m[37m[39;49;00m
  1934	[37m [39;49;00m[33m"[39;49;00m[33muse [39;49;00m[33m`process-query-on-exit-flag'[39;49;00m[33m or [39;49;00m[33m`set-process-query-on-exit-flag'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  1935	[37m [39;49;00m[33m"[39;49;00m[33m22.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  1936	([36mdefun[39;49;00m[37m [39;49;00m[31mprocess-kill-without-query[39;49;00m[37m [39;49;00m([31mprocess[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31m_flag[39;49;00m)[37m[39;49;00m
  1937	[37m  [39;49;00m[33m"[39;49;00m[33mSay no query needed if PROCESS is running when Emacs is exited.[39;49;00m
  1938	[33mOptional second argument if non-nil says to require a query.[39;49;00m
  1939	[33mValue is t if a query was formerly required.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  1940	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mold[39;49;00m[37m [39;49;00m([32mprocess-query-on-exit-flag[39;49;00m[37m [39;49;00m[31mprocess[39;49;00m)))[37m[39;49;00m
  1941	[37m    [39;49;00m([32mset-process-query-on-exit-flag[39;49;00m[37m [39;49;00m[31mprocess[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m
  1942	[37m    [39;49;00m[31mold[39;49;00m))[37m[39;49;00m
  1943	[37m[39;49;00m
  1944	([36mdefun[39;49;00m[37m [39;49;00m[31mprocess-kill-buffer-query-function[39;49;00m[37m [39;49;00m()[37m[39;49;00m
  1945	[37m  [39;49;00m[33m"[39;49;00m[33mAsk before killing a buffer that has a running process.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  1946	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mprocess[39;49;00m[37m [39;49;00m([32mget-buffer-process[39;49;00m[37m [39;49;00m([32mcurrent-buffer[39;49;00m))))[37m[39;49;00m
  1947	[37m    [39;49;00m([34mor[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m[31mprocess[39;49;00m)[37m[39;49;00m
  1948	[37m        [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m([32mprocess-status[39;49;00m[37m [39;49;00m[31mprocess[39;49;00m)[37m [39;49;00m'([31mrun[39;49;00m[37m [39;49;00m[31mstop[39;49;00m[37m [39;49;00m[31mopen[39;49;00m[37m [39;49;00m[31mlisten[39;49;00m)))[37m[39;49;00m
  1949	[37m        [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mprocess-query-on-exit-flag[39;49;00m[37m [39;49;00m[31mprocess[39;49;00m))[37m[39;49;00m
  1950	[37m        [39;49;00m([32myes-or-no-p[39;49;00m[37m[39;49;00m
  1951	[37m	 [39;49;00m([32mformat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mBuffer %S has a running process; kill it? [39;49;00m[33m"[39;49;00m[37m[39;49;00m
  1952	[37m		 [39;49;00m([32mbuffer-name[39;49;00m[37m [39;49;00m([32mcurrent-buffer[39;49;00m)))))))[37m[39;49;00m
  1953	[37m[39;49;00m
  1954	([31madd-hook[39;49;00m[37m [39;49;00m[33m'kill-buffer-query-functions[39;49;00m[37m [39;49;00m[33m'process-kill-buffer-query-function[39;49;00m)[37m[39;49;00m
  1955	[37m[39;49;00m
  1956	[37m;; process plist management[39;49;00m[37m[39;49;00m
  1957	[37m[39;49;00m
  1958	([36mdefun[39;49;00m[37m [39;49;00m[31mprocess-get[39;49;00m[37m [39;49;00m([31mprocess[39;49;00m[37m [39;49;00m[31mpropname[39;49;00m)[37m[39;49;00m
  1959	[37m  [39;49;00m[33m"[39;49;00m[33mReturn the value of PROCESS' PROPNAME property.[39;49;00m
  1960	[33mThis is the last value stored with [39;49;00m[33m`[39;49;00m[33m(process-put PROCESS PROPNAME VALUE)'.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  1961	[37m  [39;49;00m([32mplist-get[39;49;00m[37m [39;49;00m([32mprocess-plist[39;49;00m[37m [39;49;00m[31mprocess[39;49;00m)[37m [39;49;00m[31mpropname[39;49;00m))[37m[39;49;00m
  1962	[37m[39;49;00m
  1963	([36mdefun[39;49;00m[37m [39;49;00m[31mprocess-put[39;49;00m[37m [39;49;00m([31mprocess[39;49;00m[37m [39;49;00m[31mpropname[39;49;00m[37m [39;49;00m[31mvalue[39;49;00m)[37m[39;49;00m
  1964	[37m  [39;49;00m[33m"[39;49;00m[33mChange PROCESS' PROPNAME property to VALUE.[39;49;00m
  1965	[33mIt can be retrieved with [39;49;00m[33m`[39;49;00m[33m(process-get PROCESS PROPNAME)'.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  1966	[37m  [39;49;00m([32mset-process-plist[39;49;00m[37m [39;49;00m[31mprocess[39;49;00m[37m[39;49;00m
  1967	[37m		     [39;49;00m([32mplist-put[39;49;00m[37m [39;49;00m([32mprocess-plist[39;49;00m[37m [39;49;00m[31mprocess[39;49;00m)[37m [39;49;00m[31mpropname[39;49;00m[37m [39;49;00m[31mvalue[39;49;00m)))[37m[39;49;00m
  1968	[37m[39;49;00m
  1969	[37m[39;49;00m[37m[39;49;00m
  1970	[37m;;;; Input and display facilities.[39;49;00m[37m[39;49;00m
  1971	[37m[39;49;00m
  1972	([34mdefconst[39;49;00m[37m [39;49;00m[31mread-key-empty-map[39;49;00m[37m [39;49;00m([32mmake-sparse-keymap[39;49;00m))[37m[39;49;00m
  1973	[37m[39;49;00m
  1974	([34mdefvar[39;49;00m[37m [39;49;00m[31mread-key-delay[39;49;00m[37m [39;49;00m[34m0.01[39;49;00m)[37m [39;49;00m[37m;Fast enough for 100Hz repeat rate, hopefully.[39;49;00m[37m[39;49;00m
  1975	[37m[39;49;00m
  1976	([36mdefun[39;49;00m[37m [39;49;00m[31mread-key[39;49;00m[37m [39;49;00m([34m&optional[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m)[37m[39;49;00m
  1977	[37m  [39;49;00m[33m"[39;49;00m[33mRead a key from the keyboard.[39;49;00m
  1978	[33mContrary to [39;49;00m[33m`read-event'[39;49;00m[33m this will not return a raw event but instead will[39;49;00m
  1979	[33mobey the input decoding and translations usually done by [39;49;00m[33m`read-key-sequence'[39;49;00m[33m.[39;49;00m
  1980	[33mSo escape sequences and keyboard encoding are taken into account.[39;49;00m
  1981	[33mWhen there's an ambiguity because the key looks like the prefix of[39;49;00m
  1982	[33msome sort of escape sequence, the ambiguity is resolved via [39;49;00m[33m`read-key-delay'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  1983	[37m  [39;49;00m[37m;; This overriding-terminal-local-map binding also happens to[39;49;00m[37m[39;49;00m
  1984	[37m  [39;49;00m[37m;; disable quail's input methods, so although read-key-sequence[39;49;00m[37m[39;49;00m
  1985	[37m  [39;49;00m[37m;; always inherits the input method, in practice read-key does not[39;49;00m[37m[39;49;00m
  1986	[37m  [39;49;00m[37m;; inherit the input method (at least not if it's based on quail).[39;49;00m[37m[39;49;00m
  1987	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31moverriding-terminal-local-map[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m
  1988	[37m	[39;49;00m([31moverriding-local-map[39;49;00m[37m [39;49;00m[31mread-key-empty-map[39;49;00m)[37m[39;49;00m
  1989	[37m        [39;49;00m([31mecho-keystrokes[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m
  1990	[37m	[39;49;00m([31mold-global-map[39;49;00m[37m [39;49;00m([32mcurrent-global-map[39;49;00m))[37m[39;49;00m
  1991	[37m        [39;49;00m([31mtimer[39;49;00m[37m [39;49;00m([31mrun-with-idle-timer[39;49;00m[37m[39;49;00m
  1992	[37m                [39;49;00m[37m;; Wait long enough that Emacs has the time to receive and[39;49;00m[37m[39;49;00m
  1993	[37m                [39;49;00m[37m;; process all the raw events associated with the single-key.[39;49;00m[37m[39;49;00m
  1994	[37m                [39;49;00m[37m;; But don't wait too long, or the user may find the delay[39;49;00m[37m[39;49;00m
  1995	[37m                [39;49;00m[37m;; annoying (or keep hitting more keys which may then get[39;49;00m[37m[39;49;00m
  1996	[37m                [39;49;00m[37m;; lost or misinterpreted).[39;49;00m[37m[39;49;00m
  1997	[37m                [39;49;00m[37m;; This is only relevant for keys which Emacs perceives as[39;49;00m[37m[39;49;00m
  1998	[37m                [39;49;00m[37m;; "prefixes", such as C-x (because of the C-x 8 map in[39;49;00m[37m[39;49;00m
  1999	[37m                [39;49;00m[37m;; key-translate-table and the C-x @ map in function-key-map)[39;49;00m[37m[39;49;00m
  2000	[37m                [39;49;00m[37m;; or ESC (because of terminal escape sequences in[39;49;00m[37m[39;49;00m
  2001	[37m                [39;49;00m[37m;; input-decode-map).[39;49;00m[37m[39;49;00m
  2002	[37m                [39;49;00m[31mread-key-delay[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m[39;49;00m
  2003	[37m                [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m()[37m[39;49;00m
  2004	[37m                  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mkeys[39;49;00m[37m [39;49;00m([32mthis-command-keys-vector[39;49;00m)))[37m[39;49;00m
  2005	[37m                    [39;49;00m([36munless[39;49;00m[37m [39;49;00m([31mzerop[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31mkeys[39;49;00m))[37m[39;49;00m
  2006	[37m                      [39;49;00m[37m;; `keys' is non-empty, so the user has hit at least[39;49;00m[37m[39;49;00m
  2007	[37m                      [39;49;00m[37m;; one key; there's no point waiting any longer, even[39;49;00m[37m[39;49;00m
  2008	[37m                      [39;49;00m[37m;; though read-key-sequence thinks we should wait[39;49;00m[37m[39;49;00m
  2009	[37m                      [39;49;00m[37m;; for more input to decide how to interpret the[39;49;00m[37m[39;49;00m
  2010	[37m                      [39;49;00m[37m;; current input.[39;49;00m[37m[39;49;00m
  2011	[37m                      [39;49;00m([36mthrow[39;49;00m[37m [39;49;00m[33m'read-key[39;49;00m[37m [39;49;00m[31mkeys[39;49;00m)))))))[37m[39;49;00m
  2012	[37m    [39;49;00m([34munwind-protect[39;49;00m[37m[39;49;00m
  2013	[37m        [39;49;00m([34mprogn[39;49;00m[37m[39;49;00m
  2014	[37m	  [39;49;00m([32muse-global-map[39;49;00m[37m[39;49;00m
  2015	[37m           [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mmap[39;49;00m[37m [39;49;00m([32mmake-sparse-keymap[39;49;00m)))[37m[39;49;00m
  2016	[37m             [39;49;00m[37m;; Don't hide the menu-bar and tool-bar entries.[39;49;00m[37m[39;49;00m
  2017	[37m             [39;49;00m([32mdefine-key[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m[[31mmenu-bar[39;49;00m][37m [39;49;00m([32mlookup-key[39;49;00m[37m [39;49;00m[31mglobal-map[39;49;00m[37m [39;49;00m[[31mmenu-bar[39;49;00m]))[37m[39;49;00m
  2018	[37m             [39;49;00m([32mdefine-key[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m[[31mtool-bar[39;49;00m][37m[39;49;00m
  2019	[37m	       [39;49;00m[37m;; This hack avoids evaluating the :filter (Bug#9922).[39;49;00m[37m[39;49;00m
  2020	[37m	       [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m([32massq[39;49;00m[37m [39;49;00m[33m'tool-bar[39;49;00m[37m [39;49;00m[31mglobal-map[39;49;00m))[37m[39;49;00m
  2021	[37m		   [39;49;00m([32mlookup-key[39;49;00m[37m [39;49;00m[31mglobal-map[39;49;00m[37m [39;49;00m[[31mtool-bar[39;49;00m])))[37m[39;49;00m
  2022	[37m             [39;49;00m[31mmap[39;49;00m))[37m[39;49;00m
  2023	[37m          [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mkeys[39;49;00m[37m[39;49;00m
  2024	[37m                  [39;49;00m([34mcatch[39;49;00m[37m [39;49;00m[33m'read-key[39;49;00m[37m [39;49;00m([32mread-key-sequence-vector[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mt[39;49;00m)))[37m[39;49;00m
  2025	[37m                 [39;49;00m([31mkey[39;49;00m[37m [39;49;00m([32maref[39;49;00m[37m [39;49;00m[31mkeys[39;49;00m[37m [39;49;00m[34m0[39;49;00m)))[37m[39;49;00m
  2026	[37m            [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31mkeys[39;49;00m)[37m [39;49;00m[34m1[39;49;00m)[37m[39;49;00m
  2027	[37m                     [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m'([31mmode-line[39;49;00m[37m [39;49;00m[31mheader-line[39;49;00m[37m[39;49;00m
  2028	[37m                                 [39;49;00m[31mleft-fringe[39;49;00m[37m [39;49;00m[31mright-fringe[39;49;00m)))[37m[39;49;00m
  2029	[37m                [39;49;00m([32maref[39;49;00m[37m [39;49;00m[31mkeys[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m[39;49;00m
  2030	[37m              [39;49;00m[31mkey[39;49;00m)))[37m[39;49;00m
  2031	[37m      [39;49;00m([31mcancel-timer[39;49;00m[37m [39;49;00m[31mtimer[39;49;00m)[37m[39;49;00m
  2032	[37m      [39;49;00m([32muse-global-map[39;49;00m[37m [39;49;00m[31mold-global-map[39;49;00m))))[37m[39;49;00m
  2033	[37m[39;49;00m
  2034	([34mdefvar[39;49;00m[37m [39;49;00m[31mread-passwd-map[39;49;00m[37m[39;49;00m
  2035	[37m  [39;49;00m[37m;; BEWARE: `defconst' would purecopy it, breaking the sharing with[39;49;00m[37m[39;49;00m
  2036	[37m  [39;49;00m[37m;; minibuffer-local-map along the way![39;49;00m[37m[39;49;00m
  2037	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mmap[39;49;00m[37m [39;49;00m([32mmake-sparse-keymap[39;49;00m)))[37m[39;49;00m
  2038	[37m    [39;49;00m([32mset-keymap-parent[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m[31mminibuffer-local-map[39;49;00m)[37m[39;49;00m
  2039	[37m    [39;49;00m([32mdefine-key[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\C[39;49;00m[33m-u[39;49;00m[33m"[39;49;00m[37m [39;49;00m[32m#'[39;49;00m[31mdelete-minibuffer-contents[39;49;00m)[37m [39;49;00m[37m;bug#12570[39;49;00m[37m[39;49;00m
  2040	[37m    [39;49;00m[31mmap[39;49;00m)[37m[39;49;00m
  2041	[37m  [39;49;00m[33m"[39;49;00m[33mKeymap used while reading passwords.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  2042	[37m[39;49;00m
  2043	([36mdefun[39;49;00m[37m [39;49;00m[31mread-passwd[39;49;00m[37m [39;49;00m([31mprompt[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mconfirm[39;49;00m[37m [39;49;00m[31mdefault[39;49;00m)[37m[39;49;00m
  2044	[37m  [39;49;00m[33m"[39;49;00m[33mRead a password, prompting with PROMPT, and return it.[39;49;00m
  2045	[33mIf optional CONFIRM is non-nil, read the password twice to make sure.[39;49;00m
  2046	[33mOptional DEFAULT is a default password to use instead of empty input.[39;49;00m
  2047	[33m[39;49;00m
  2048	[33mThis function echoes [39;49;00m[33m`.'[39;49;00m[33m for each character that the user types.[39;49;00m
  2049	[33mYou could let-bind [39;49;00m[33m`read-hide-char'[39;49;00m[33m to another hiding character, though.[39;49;00m
  2050	[33m[39;49;00m
  2051	[33mOnce the caller uses the password, it can erase the password[39;49;00m
  2052	[33mby doing (clear-string STRING).[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2053	[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mconfirm[39;49;00m[37m[39;49;00m
  2054	[37m      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m([31msuccess[39;49;00m)[37m[39;49;00m
  2055	[37m        [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m[31msuccess[39;49;00m)[37m[39;49;00m
  2056	[37m          [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mfirst[39;49;00m[37m [39;49;00m([31mread-passwd[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mdefault[39;49;00m))[37m[39;49;00m
  2057	[37m                [39;49;00m([31msecond[39;49;00m[37m [39;49;00m([31mread-passwd[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mConfirm password: [39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mdefault[39;49;00m)))[37m[39;49;00m
  2058	[37m            [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mequal[39;49;00m[37m [39;49;00m[31mfirst[39;49;00m[37m [39;49;00m[31msecond[39;49;00m)[37m[39;49;00m
  2059	[37m                [39;49;00m([34mprogn[39;49;00m[37m[39;49;00m
  2060	[37m                  [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32marrayp[39;49;00m[37m [39;49;00m[31msecond[39;49;00m)[37m [39;49;00m([32mclear-string[39;49;00m[37m [39;49;00m[31msecond[39;49;00m))[37m[39;49;00m
  2061	[37m                  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31msuccess[39;49;00m[37m [39;49;00m[31mfirst[39;49;00m))[37m[39;49;00m
  2062	[37m              [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32marrayp[39;49;00m[37m [39;49;00m[31mfirst[39;49;00m)[37m [39;49;00m([32mclear-string[39;49;00m[37m [39;49;00m[31mfirst[39;49;00m))[37m[39;49;00m
  2063	[37m              [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32marrayp[39;49;00m[37m [39;49;00m[31msecond[39;49;00m)[37m [39;49;00m([32mclear-string[39;49;00m[37m [39;49;00m[31msecond[39;49;00m))[37m[39;49;00m
  2064	[37m              [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mPassword not repeated accurately; please start over[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  2065	[37m              [39;49;00m([31msit-for[39;49;00m[37m [39;49;00m[34m1[39;49;00m))))[37m[39;49;00m
  2066	[37m        [39;49;00m[31msuccess[39;49;00m)[37m[39;49;00m
  2067	[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mhide-chars-fun[39;49;00m[37m[39;49;00m
  2068	[37m           [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31mbeg[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[31m_len[39;49;00m)[37m[39;49;00m
  2069	[37m             [39;49;00m([32mclear-this-command-keys[39;49;00m)[37m[39;49;00m
  2070	[37m             [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m[37m [39;49;00m([32mmin[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m([32mmax[39;49;00m[37m [39;49;00m([32mminibuffer-prompt-end[39;49;00m)[37m[39;49;00m
  2071	[37m                                     [39;49;00m[31mbeg[39;49;00m)))[37m[39;49;00m
  2072	[37m             [39;49;00m([36mdotimes[39;49;00m[37m [39;49;00m([31mi[39;49;00m[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m))[37m[39;49;00m
  2073	[37m               [39;49;00m([32mput-text-property[39;49;00m[37m [39;49;00m([32m+[39;49;00m[37m [39;49;00m[31mi[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m)[37m [39;49;00m([32m+[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mi[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m)[37m[39;49;00m
  2074	[37m                                  [39;49;00m[33m'display[39;49;00m[37m [39;49;00m([32mstring[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mread-hide-char[39;49;00m[37m [39;49;00m[33m?.[39;49;00m))))))[37m[39;49;00m
  2075	[37m          [39;49;00m[31mminibuf[39;49;00m)[37m[39;49;00m
  2076	[37m      [39;49;00m([31mminibuffer-with-setup-hook[39;49;00m[37m[39;49;00m
  2077	[37m          [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m()[37m[39;49;00m
  2078	[37m            [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mminibuf[39;49;00m[37m [39;49;00m([32mcurrent-buffer[39;49;00m))[37m[39;49;00m
  2079	[37m            [39;49;00m[37m;; Turn off electricity.[39;49;00m[37m[39;49;00m
  2080	[37m            [39;49;00m([36msetq-local[39;49;00m[37m [39;49;00m[31mpost-self-insert-hook[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m
  2081	[37m            [39;49;00m([36msetq-local[39;49;00m[37m [39;49;00m[31mbuffer-undo-list[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m
  2082	[37m            [39;49;00m([36msetq-local[39;49;00m[37m [39;49;00m[31mselect-active-regions[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m
  2083	[37m            [39;49;00m([32muse-local-map[39;49;00m[37m [39;49;00m[31mread-passwd-map[39;49;00m)[37m[39;49;00m
  2084	[37m            [39;49;00m([36msetq-local[39;49;00m[37m [39;49;00m[31minhibit-modification-hooks[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m [39;49;00m[37m;bug#15501.[39;49;00m[37m[39;49;00m
  2085	[37m	    [39;49;00m([36msetq-local[39;49;00m[37m [39;49;00m[31mshow-paren-mode[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m		[39;49;00m[37m;bug#16091.[39;49;00m[37m[39;49;00m
  2086	[37m            [39;49;00m([31madd-hook[39;49;00m[37m [39;49;00m[33m'after-change-functions[39;49;00m[37m [39;49;00m[31mhide-chars-fun[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[33m'local[39;49;00m))[37m[39;49;00m
  2087	[37m        [39;49;00m([34munwind-protect[39;49;00m[37m[39;49;00m
  2088	[37m            [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31menable-recursive-minibuffers[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m
  2089	[37m		  [39;49;00m([31mread-hide-char[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mread-hide-char[39;49;00m[37m [39;49;00m[33m?.[39;49;00m)))[37m[39;49;00m
  2090	[37m              [39;49;00m([32mread-string[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m[31mdefault[39;49;00m))[37m [39;49;00m[37m; t = "no history"[39;49;00m[37m[39;49;00m
  2091	[37m          [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mbuffer-live-p[39;49;00m[37m [39;49;00m[31mminibuf[39;49;00m)[37m[39;49;00m
  2092	[37m            [39;49;00m([36mwith-current-buffer[39;49;00m[37m [39;49;00m[31mminibuf[39;49;00m[37m[39;49;00m
  2093	[37m              [39;49;00m[37m;; Not sure why but it seems that there might be cases where the[39;49;00m[37m[39;49;00m
  2094	[37m              [39;49;00m[37m;; minibuffer is not always properly reset later on, so undo[39;49;00m[37m[39;49;00m
  2095	[37m              [39;49;00m[37m;; whatever we've done here (bug#11392).[39;49;00m[37m[39;49;00m
  2096	[37m              [39;49;00m([31mremove-hook[39;49;00m[37m [39;49;00m[33m'after-change-functions[39;49;00m[37m [39;49;00m[31mhide-chars-fun[39;49;00m[37m [39;49;00m[33m'local[39;49;00m)[37m[39;49;00m
  2097	[37m              [39;49;00m([32mkill-local-variable[39;49;00m[37m [39;49;00m[33m'post-self-insert-hook[39;49;00m)[37m[39;49;00m
  2098	[37m              [39;49;00m[37m;; And of course, don't keep the sensitive data around.[39;49;00m[37m[39;49;00m
  2099	[37m              [39;49;00m([32merase-buffer[39;49;00m))))))))[37m[39;49;00m
  2100	[37m[39;49;00m
  2101	([36mdefun[39;49;00m[37m [39;49;00m[31mread-number[39;49;00m[37m [39;49;00m([31mprompt[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mdefault[39;49;00m)[37m[39;49;00m
  2102	[37m  [39;49;00m[33m"[39;49;00m[33mRead a numeric value in the minibuffer, prompting with PROMPT.[39;49;00m
  2103	[33mDEFAULT specifies a default value to return if the user just types RET.[39;49;00m
  2104	[33mThe value of DEFAULT is inserted into PROMPT.[39;49;00m
  2105	[33mThis function is used by the [39;49;00m[33m`interactive'[39;49;00m[33m code letter [39;49;00m[33m`n'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2106	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mn[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m
  2107	[37m	[39;49;00m([31mdefault1[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mdefault[39;49;00m)[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mdefault[39;49;00m)[37m [39;49;00m[31mdefault[39;49;00m)))[37m[39;49;00m
  2108	[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31mdefault1[39;49;00m[37m[39;49;00m
  2109	[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m[37m[39;49;00m
  2110	[37m	    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m([39;49;00m[33m\\[39;49;00m[33m):[ [39;49;00m[33m\t[39;49;00m[33m]*[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m)[37m[39;49;00m
  2111	[37m		[39;49;00m([32mreplace-match[39;49;00m[37m [39;49;00m([32mformat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m (default %s)[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mdefault1[39;49;00m)[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m[39;49;00m
  2112	[37m	      [39;49;00m([31mreplace-regexp-in-string[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m[ [39;49;00m[33m\t[39;49;00m[33m]*[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2113	[37m					[39;49;00m([32mformat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m (default %s) [39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mdefault1[39;49;00m)[37m[39;49;00m
  2114	[37m					[39;49;00m[31mprompt[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m[31mt[39;49;00m))))[37m[39;49;00m
  2115	[37m    [39;49;00m([34mwhile[39;49;00m[37m[39;49;00m
  2116	[37m	[39;49;00m([34mprogn[39;49;00m[37m[39;49;00m
  2117	[37m	  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mstr[39;49;00m[37m [39;49;00m([32mread-from-minibuffer[39;49;00m[37m[39;49;00m
  2118	[37m		      [39;49;00m[31mprompt[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m
  2119	[37m		      [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31mdefault[39;49;00m[37m[39;49;00m
  2120	[37m			[39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mdefault[39;49;00m)[37m[39;49;00m
  2121	[37m			    [39;49;00m([32mmapcar[39;49;00m[37m [39;49;00m[33m'number-to-string[39;49;00m[37m [39;49;00m([32mdelq[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mdefault[39;49;00m))[37m[39;49;00m
  2122	[37m			  [39;49;00m([32mnumber-to-string[39;49;00m[37m [39;49;00m[31mdefault[39;49;00m))))))[37m[39;49;00m
  2123	[37m	    [39;49;00m([34mcondition-case[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m
  2124	[37m		[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mn[39;49;00m[37m [39;49;00m([34mcond[39;49;00m[37m[39;49;00m
  2125	[37m			 [39;49;00m(([31mzerop[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31mstr[39;49;00m))[37m [39;49;00m[31mdefault1[39;49;00m)[37m[39;49;00m
  2126	[37m			 [39;49;00m(([32mstringp[39;49;00m[37m [39;49;00m[31mstr[39;49;00m)[37m [39;49;00m([32mread[39;49;00m[37m [39;49;00m[31mstr[39;49;00m))))[37m[39;49;00m
  2127	[37m	      [39;49;00m([36merror[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)))[37m[39;49;00m
  2128	[37m	  [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32mnumberp[39;49;00m[37m [39;49;00m[31mn[39;49;00m)[37m[39;49;00m
  2129	[37m	    [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mPlease enter a number.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  2130	[37m	    [39;49;00m([31msit-for[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m[39;49;00m
  2131	[37m	    [39;49;00m[31mt[39;49;00m)))[37m[39;49;00m
  2132	[37m    [39;49;00m[31mn[39;49;00m))[37m[39;49;00m
  2133	[37m[39;49;00m
  2134	([36mdefun[39;49;00m[37m [39;49;00m[31mread-char-choice[39;49;00m[37m [39;49;00m([31mprompt[39;49;00m[37m [39;49;00m[31mchars[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31minhibit-keyboard-quit[39;49;00m)[37m[39;49;00m
  2135	[37m  [39;49;00m[33m"[39;49;00m[33mRead and return one of CHARS, prompting for PROMPT.[39;49;00m
  2136	[33mAny input that is not one of CHARS is ignored.[39;49;00m
  2137	[33m[39;49;00m
  2138	[33mIf optional argument INHIBIT-KEYBOARD-QUIT is non-nil, ignore[39;49;00m
  2139	[33mkeyboard-quit events while waiting for a valid input.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2140	[37m  [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mchars[39;49;00m)[37m[39;49;00m
  2141	[37m    [39;49;00m([36merror[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mCalled [39;49;00m[33m`read-char-choice'[39;49;00m[33m without valid char choices[39;49;00m[33m"[39;49;00m))[37m[39;49;00m
  2142	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m([31mchar[39;49;00m[37m [39;49;00m[31mdone[39;49;00m[37m [39;49;00m[31mshow-help[39;49;00m[37m [39;49;00m([31mhelpbuf[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m *Char Help*[39;49;00m[33m"[39;49;00m))[37m[39;49;00m
  2143	[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mcursor-in-echo-area[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m
  2144	[37m          [39;49;00m([31mexecuting-kbd-macro[39;49;00m[37m [39;49;00m[31mexecuting-kbd-macro[39;49;00m)[37m[39;49;00m
  2145	[37m	  [39;49;00m([31mesc-flag[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m
  2146	[37m      [39;49;00m([36msave-window-excursion[39;49;00m[37m	      [39;49;00m[37m; in case we call help-form-show[39;49;00m[37m[39;49;00m
  2147	[37m	[39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m[31mdone[39;49;00m)[37m[39;49;00m
  2148	[37m	  [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32mget-text-property[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[33m'face[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m)[37m[39;49;00m
  2149	[37m	    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m[37m [39;49;00m([32mpropertize[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m[37m [39;49;00m[33m'face[39;49;00m[37m [39;49;00m[33m'minibuffer-prompt[39;49;00m)))[37m[39;49;00m
  2150	[37m	  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mchar[39;49;00m[37m [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31minhibit-quit[39;49;00m[37m [39;49;00m[31minhibit-keyboard-quit[39;49;00m))[37m[39;49;00m
  2151	[37m		       [39;49;00m([31mread-key[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m)))[37m[39;49;00m
  2152	[37m	  [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mshow-help[39;49;00m[37m [39;49;00m([32mbuffer-live-p[39;49;00m[37m [39;49;00m([32mget-buffer[39;49;00m[37m [39;49;00m[31mhelpbuf[39;49;00m))[37m[39;49;00m
  2153	[37m	       [39;49;00m([32mkill-buffer[39;49;00m[37m [39;49;00m[31mhelpbuf[39;49;00m))[37m[39;49;00m
  2154	[37m	  [39;49;00m([34mcond[39;49;00m[37m[39;49;00m
  2155	[37m	   [39;49;00m(([31mnot[39;49;00m[37m [39;49;00m([32mnumberp[39;49;00m[37m [39;49;00m[31mchar[39;49;00m)))[37m[39;49;00m
  2156	[37m	   [39;49;00m[37m;; If caller has set help-form, that's enough.[39;49;00m[37m[39;49;00m
  2157	[37m	   [39;49;00m[37m;; They don't explicitly have to add help-char to chars.[39;49;00m[37m[39;49;00m
  2158	[37m	   [39;49;00m(([34mand[39;49;00m[37m [39;49;00m[31mhelp-form[39;49;00m[37m[39;49;00m
  2159	[37m		 [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mchar[39;49;00m[37m [39;49;00m[31mhelp-char[39;49;00m)[37m[39;49;00m
  2160	[37m		 [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mshow-help[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m
  2161	[37m		 [39;49;00m([31mhelp-form-show[39;49;00m)))[37m[39;49;00m
  2162	[37m	   [39;49;00m(([32mmemq[39;49;00m[37m [39;49;00m[31mchar[39;49;00m[37m [39;49;00m[31mchars[39;49;00m)[37m[39;49;00m
  2163	[37m	    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mdone[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m
  2164	[37m	   [39;49;00m(([34mand[39;49;00m[37m [39;49;00m[31mexecuting-kbd-macro[39;49;00m[37m [39;49;00m([32m=[39;49;00m[37m [39;49;00m[31mchar[39;49;00m[37m [39;49;00m[34m-1[39;49;00m))[37m[39;49;00m
  2165	[37m	    [39;49;00m[37m;; read-event returns -1 if we are in a kbd macro and[39;49;00m[37m[39;49;00m
  2166	[37m	    [39;49;00m[37m;; there are no more events in the macro.  Attempt to[39;49;00m[37m[39;49;00m
  2167	[37m	    [39;49;00m[37m;; get an event interactively.[39;49;00m[37m[39;49;00m
  2168	[37m	    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mexecuting-kbd-macro[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m
  2169	[37m	   [39;49;00m(([31mnot[39;49;00m[37m [39;49;00m[31minhibit-keyboard-quit[39;49;00m)[37m[39;49;00m
  2170	[37m	    [39;49;00m([34mcond[39;49;00m[37m[39;49;00m
  2171	[37m	     [39;49;00m(([34mand[39;49;00m[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[31mesc-flag[39;49;00m)[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mchar[39;49;00m[37m [39;49;00m[33m?\e[39;49;00m))[37m[39;49;00m
  2172	[37m	      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mesc-flag[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m
  2173	[37m	     [39;49;00m(([32mmemq[39;49;00m[37m [39;49;00m[31mchar[39;49;00m[37m [39;49;00m'([33m?\C[39;49;00m[31m-g[39;49;00m[37m [39;49;00m[33m?\e[39;49;00m))[37m[39;49;00m
  2174	[37m	      [39;49;00m([31mkeyboard-quit[39;49;00m))))))))[37m[39;49;00m
  2175	[37m    [39;49;00m[37m;; Display the question with the answer.  But without cursor-in-echo-area.[39;49;00m[37m[39;49;00m
  2176	[37m    [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m%s%s[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m[37m [39;49;00m([32mchar-to-string[39;49;00m[37m [39;49;00m[31mchar[39;49;00m))[37m[39;49;00m
  2177	[37m    [39;49;00m[31mchar[39;49;00m))[37m[39;49;00m
  2178	[37m[39;49;00m
  2179	([36mdefun[39;49;00m[37m [39;49;00m[31msit-for[39;49;00m[37m [39;49;00m([31mseconds[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mnodisp[39;49;00m[37m [39;49;00m[31mobsolete[39;49;00m)[37m[39;49;00m
  2180	[37m  [39;49;00m[33m"[39;49;00m[33mRedisplay, then wait for SECONDS seconds.  Stop when input is available.[39;49;00m
  2181	[33mSECONDS may be a floating-point value.[39;49;00m
  2182	[33m\([39;49;00m[33mOn operating systems that do not support waiting for fractions of a[39;49;00m
  2183	[33msecond, floating-point values are rounded down to the nearest integer.)[39;49;00m
  2184	[33m[39;49;00m
  2185	[33mIf optional arg NODISP is t, don't redisplay, just wait for input.[39;49;00m
  2186	[33mRedisplay does not happen if input is available before it starts.[39;49;00m
  2187	[33m[39;49;00m
  2188	[33mValue is t if waited the full time with no input arriving, and nil otherwise.[39;49;00m
  2189	[33m[39;49;00m
  2190	[33mAn obsolete, but still supported form is[39;49;00m
  2191	[33m\([39;49;00m[33msit-for SECONDS &optional MILLISECONDS NODISP)[39;49;00m
  2192	[33mwhere the optional arg MILLISECONDS specifies an additional wait period,[39;49;00m
  2193	[33min milliseconds; this was useful when Emacs was built without[39;49;00m
  2194	[33mfloating point support.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2195	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31madvertised-calling-convention[39;49;00m[37m [39;49;00m([31mseconds[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mnodisp[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m22.1[39;49;00m[33m"[39;49;00m))[37m[39;49;00m
  2196	[37m  [39;49;00m[37m;; This used to be implemented in C until the following discussion:[39;49;00m[37m[39;49;00m
  2197	[37m  [39;49;00m[37m;; http://lists.gnu.org/archive/html/emacs-devel/2006-07/msg00401.html[39;49;00m[37m[39;49;00m
  2198	[37m  [39;49;00m[37m;; Then it was moved here using an implementation based on an idle timer,[39;49;00m[37m[39;49;00m
  2199	[37m  [39;49;00m[37m;; which was then replaced by the use of read-event.[39;49;00m[37m[39;49;00m
  2200	[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mnumberp[39;49;00m[37m [39;49;00m[31mnodisp[39;49;00m)[37m[39;49;00m
  2201	[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mseconds[39;49;00m[37m [39;49;00m([32m+[39;49;00m[37m [39;49;00m[31mseconds[39;49;00m[37m [39;49;00m([32m*[39;49;00m[37m [39;49;00m[34m1e-3[39;49;00m[37m [39;49;00m[31mnodisp[39;49;00m))[37m[39;49;00m
  2202	[37m            [39;49;00m[31mnodisp[39;49;00m[37m [39;49;00m[31mobsolete[39;49;00m)[37m[39;49;00m
  2203	[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mobsolete[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mnodisp[39;49;00m[37m [39;49;00m[31mobsolete[39;49;00m)))[37m[39;49;00m
  2204	[37m  [39;49;00m([34mcond[39;49;00m[37m[39;49;00m
  2205	[37m   [39;49;00m([31mnoninteractive[39;49;00m[37m[39;49;00m
  2206	[37m    [39;49;00m([32msleep-for[39;49;00m[37m [39;49;00m[31mseconds[39;49;00m)[37m[39;49;00m
  2207	[37m    [39;49;00m[31mt[39;49;00m)[37m[39;49;00m
  2208	[37m   [39;49;00m(([32minput-pending-p[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m
  2209	[37m    [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m
  2210	[37m   [39;49;00m(([32m<=[39;49;00m[37m [39;49;00m[31mseconds[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m
  2211	[37m    [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mnodisp[39;49;00m[37m [39;49;00m([32mredisplay[39;49;00m)))[37m[39;49;00m
  2212	[37m   [39;49;00m([31mt[39;49;00m[37m[39;49;00m
  2213	[37m    [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mnodisp[39;49;00m[37m [39;49;00m([32mredisplay[39;49;00m))[37m[39;49;00m
  2214	[37m    [39;49;00m[37m;; FIXME: we should not read-event here at all, because it's much too[39;49;00m[37m[39;49;00m
  2215	[37m    [39;49;00m[37m;; difficult to reliably "undo" a read-event by pushing it onto[39;49;00m[37m[39;49;00m
  2216	[37m    [39;49;00m[37m;; unread-command-events.[39;49;00m[37m[39;49;00m
  2217	[37m    [39;49;00m[37m;; For bug#14782, we need read-event to do the keyboard-coding-system[39;49;00m[37m[39;49;00m
  2218	[37m    [39;49;00m[37m;; decoding (hence non-nil as second arg under POSIX ttys).[39;49;00m[37m[39;49;00m
  2219	[37m    [39;49;00m[37m;; For bug#15614, we need read-event not to inherit-input-method.[39;49;00m[37m[39;49;00m
  2220	[37m    [39;49;00m[37m;; So we temporarily suspend input-method-function.[39;49;00m[37m[39;49;00m
  2221	[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([32mread[39;49;00m[37m [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31minput-method-function[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m
  2222	[37m                  [39;49;00m([32mread-event[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m[31mseconds[39;49;00m))))[37m[39;49;00m
  2223	[37m      [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[32mread[39;49;00m)[37m[39;49;00m
  2224	[37m	  [39;49;00m([34mprogn[39;49;00m[37m[39;49;00m
  2225	[37m            [39;49;00m[37m;; https://lists.gnu.org/archive/html/emacs-devel/2006-10/msg00394.html[39;49;00m[37m[39;49;00m
  2226	[37m            [39;49;00m[37m;; We want `read' appear in the next command's this-command-event[39;49;00m[37m[39;49;00m
  2227	[37m            [39;49;00m[37m;; but not in the current one.[39;49;00m[37m[39;49;00m
  2228	[37m            [39;49;00m[37m;; By pushing (cons t read), we indicate that `read' has not[39;49;00m[37m[39;49;00m
  2229	[37m            [39;49;00m[37m;; yet been recorded in this-command-keys, so it will be recorded[39;49;00m[37m[39;49;00m
  2230	[37m            [39;49;00m[37m;; next time it's read.[39;49;00m[37m[39;49;00m
  2231	[37m            [39;49;00m[37m;; And indeed the `seconds' argument to read-event correctly[39;49;00m[37m[39;49;00m
  2232	[37m            [39;49;00m[37m;; prevented recording this event in the current command's[39;49;00m[37m[39;49;00m
  2233	[37m            [39;49;00m[37m;; this-command-keys.[39;49;00m[37m[39;49;00m
  2234	[37m	    [39;49;00m([36mpush[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m[32mread[39;49;00m)[37m [39;49;00m[31munread-command-events[39;49;00m)[37m[39;49;00m
  2235	[37m	    [39;49;00m[31mnil[39;49;00m))))))[37m[39;49;00m
  2236	[37m[39;49;00m
  2237	[37m;; Behind display-popup-menus-p test.[39;49;00m[37m[39;49;00m
  2238	([36mdeclare-function[39;49;00m[37m [39;49;00m[32mx-popup-dialog[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mmenu.c[39;49;00m[33m"[39;49;00m[37m [39;49;00m([31mposition[39;49;00m[37m [39;49;00m[31mcontents[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mheader[39;49;00m))[37m[39;49;00m
  2239	[37m[39;49;00m
  2240	([36mdefun[39;49;00m[37m [39;49;00m[31my-or-n-p[39;49;00m[37m [39;49;00m([31mprompt[39;49;00m)[37m[39;49;00m
  2241	[37m  [39;49;00m[33m"[39;49;00m[33mAsk user a [39;49;00m[33m\"[39;49;00m[33my or n[39;49;00m[33m\"[39;49;00m[33m question.  Return t if answer is [39;49;00m[33m\"[39;49;00m[33my[39;49;00m[33m\"[39;49;00m[33m.[39;49;00m
  2242	[33mPROMPT is the string to display to ask the question.  It should[39;49;00m
  2243	[33mend in a space; [39;49;00m[33m`y-or-n-p'[39;49;00m[33m adds [39;49;00m[33m\"[39;49;00m[33m(y or n) [39;49;00m[33m\"[39;49;00m[33m to it.[39;49;00m
  2244	[33m[39;49;00m
  2245	[33mNo confirmation of the answer is requested; a single character is[39;49;00m
  2246	[33menough.  SPC also means yes, and DEL means no.[39;49;00m
  2247	[33m[39;49;00m
  2248	[33mTo be precise, this function translates user input into responses[39;49;00m
  2249	[33mby consulting the bindings in [39;49;00m[33m`query-replace-map'[39;49;00m[33m; see the[39;49;00m
  2250	[33mdocumentation of that variable for more information.  In this[39;49;00m
  2251	[33mcase, the useful bindings are [39;49;00m[33m`act'[39;49;00m[33m, [39;49;00m[33m`skip'[39;49;00m[33m, [39;49;00m[33m`recenter'[39;49;00m[33m,[39;49;00m
  2252	[33m`scroll-up'[39;49;00m[33m, [39;49;00m[33m`scroll-down'[39;49;00m[33m, and [39;49;00m[33m`quit'[39;49;00m[33m.[39;49;00m
  2253	[33mAn [39;49;00m[33m`act'[39;49;00m[33m response means yes, and a [39;49;00m[33m`skip'[39;49;00m[33m response means no.[39;49;00m
  2254	[33mA [39;49;00m[33m`quit'[39;49;00m[33m response means to invoke [39;49;00m[33m`keyboard-quit'[39;49;00m[33m.[39;49;00m
  2255	[33mIf the user enters [39;49;00m[33m`recenter'[39;49;00m[33m, [39;49;00m[33m`scroll-up'[39;49;00m[33m, or [39;49;00m[33m`scroll-down'[39;49;00m[33m[39;49;00m
  2256	[33mresponses, perform the requested window recentering or scrolling[39;49;00m
  2257	[33mand ask again.[39;49;00m
  2258	[33m[39;49;00m
  2259	[33mUnder a windowing system a dialog box will be used if [39;49;00m[33m`last-nonmenu-event'[39;49;00m[33m[39;49;00m
  2260	[33mis nil and [39;49;00m[33m`use-dialog-box'[39;49;00m[33m is non-nil.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2261	[37m  [39;49;00m[37m;; ¡Beware! when I tried to edebug this code, Emacs got into a weird state[39;49;00m[37m[39;49;00m
  2262	[37m  [39;49;00m[37m;; where all the keys were unbound (i.e. it somehow got triggered[39;49;00m[37m[39;49;00m
  2263	[37m  [39;49;00m[37m;; within read-key, apparently).  I had to kill it.[39;49;00m[37m[39;49;00m
  2264	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31manswer[39;49;00m[37m [39;49;00m[33m'recenter[39;49;00m)[37m[39;49;00m
  2265	[37m	[39;49;00m([31mpadded[39;49;00m[37m [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31mprompt[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mdialog[39;49;00m)[37m[39;49;00m
  2266	[37m		  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31ml[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m)))[37m[39;49;00m
  2267	[37m		    [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m[37m[39;49;00m
  2268	[37m			    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([31mzerop[39;49;00m[37m [39;49;00m[31ml[39;49;00m)[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[33m?\s[39;49;00m[37m [39;49;00m([32maref[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m[37m [39;49;00m([32m1-[39;49;00m[37m [39;49;00m[31ml[39;49;00m))))[37m[39;49;00m
  2269	[37m				[39;49;00m[33m"[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  2270	[37m			    [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mdialog[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m(y or n) [39;49;00m[33m"[39;49;00m))))))[37m[39;49;00m
  2271	[37m    [39;49;00m([34mcond[39;49;00m[37m[39;49;00m
  2272	[37m     [39;49;00m([31mnoninteractive[39;49;00m[37m[39;49;00m
  2273	[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m[37m [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mpadded[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m))[37m[39;49;00m
  2274	[37m      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtemp-prompt[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m))[37m[39;49;00m
  2275	[37m	[39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[31manswer[39;49;00m[37m [39;49;00m'([31mact[39;49;00m[37m [39;49;00m[31mskip[39;49;00m)))[37m[39;49;00m
  2276	[37m	  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mstr[39;49;00m[37m [39;49;00m([32mread-string[39;49;00m[37m [39;49;00m[31mtemp-prompt[39;49;00m)))[37m[39;49;00m
  2277	[37m	    [39;49;00m([34mcond[39;49;00m[37m [39;49;00m(([32mmember[39;49;00m[37m [39;49;00m[31mstr[39;49;00m[37m [39;49;00m'([33m"[39;49;00m[33my[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mY[39;49;00m[33m"[39;49;00m))[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31manswer[39;49;00m[37m [39;49;00m[33m'act[39;49;00m))[37m[39;49;00m
  2278	[37m		  [39;49;00m(([32mmember[39;49;00m[37m [39;49;00m[31mstr[39;49;00m[37m [39;49;00m'([33m"[39;49;00m[33mn[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mN[39;49;00m[33m"[39;49;00m))[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31manswer[39;49;00m[37m [39;49;00m[33m'skip[39;49;00m))[37m[39;49;00m
  2279	[37m		  [39;49;00m([31mt[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mtemp-prompt[39;49;00m[37m [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mPlease answer y or n.  [39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2280	[37m					       [39;49;00m[31mprompt[39;49;00m))))))))[37m[39;49;00m
  2281	[37m     [39;49;00m(([34mand[39;49;00m[37m [39;49;00m([31mdisplay-popup-menus-p[39;49;00m)[37m[39;49;00m
  2282	[37m	   [39;49;00m([32mlistp[39;49;00m[37m [39;49;00m[31mlast-nonmenu-event[39;49;00m)[37m[39;49;00m
  2283	[37m	   [39;49;00m[31muse-dialog-box[39;49;00m)[37m[39;49;00m
  2284	[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m[37m [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mpadded[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m
  2285	[37m	    [39;49;00m[31manswer[39;49;00m[37m [39;49;00m([32mx-popup-dialog[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m`(,[31mprompt[39;49;00m[37m [39;49;00m([33m"[39;49;00m[33mYes[39;49;00m[33m"[39;49;00m[37m [39;49;00m.[37m [39;49;00m[31mact[39;49;00m)[37m [39;49;00m([33m"[39;49;00m[33mNo[39;49;00m[33m"[39;49;00m[37m [39;49;00m.[37m [39;49;00m[31mskip[39;49;00m)))))[37m[39;49;00m
  2286	[37m     [39;49;00m([31mt[39;49;00m[37m[39;49;00m
  2287	[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m[37m [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mpadded[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m))[37m[39;49;00m
  2288	[37m      [39;49;00m([34mwhile[39;49;00m[37m[39;49;00m
  2289	[37m          [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mscroll-actions[39;49;00m[37m [39;49;00m'([32mrecenter[39;49;00m[37m [39;49;00m[32mscroll-up[39;49;00m[37m [39;49;00m[32mscroll-down[39;49;00m[37m[39;49;00m
  2290	[37m				   [39;49;00m[32mscroll-other-window[39;49;00m[37m [39;49;00m[31mscroll-other-window-down[39;49;00m))[37m[39;49;00m
  2291	[37m		 [39;49;00m([31mkey[39;49;00m[37m[39;49;00m
  2292	[37m                  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mcursor-in-echo-area[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m
  2293	[37m                    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31mminibuffer-auto-raise[39;49;00m[37m[39;49;00m
  2294	[37m                      [39;49;00m([32mraise-frame[39;49;00m[37m [39;49;00m([32mwindow-frame[39;49;00m[37m [39;49;00m([32mminibuffer-window[39;49;00m))))[37m[39;49;00m
  2295	[37m                    [39;49;00m([31mread-key[39;49;00m[37m [39;49;00m([32mpropertize[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[31manswer[39;49;00m[37m [39;49;00m[31mscroll-actions[39;49;00m)[37m[39;49;00m
  2296	[37m                                              [39;49;00m[31mprompt[39;49;00m[37m[39;49;00m
  2297	[37m                                            [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mPlease answer y or n.  [39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2298	[37m                                                    [39;49;00m[31mprompt[39;49;00m))[37m[39;49;00m
  2299	[37m                                          [39;49;00m[33m'face[39;49;00m[37m [39;49;00m[33m'minibuffer-prompt[39;49;00m)))))[37m[39;49;00m
  2300	[37m            [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31manswer[39;49;00m[37m [39;49;00m([32mlookup-key[39;49;00m[37m [39;49;00m[31mquery-replace-map[39;49;00m[37m [39;49;00m([32mvector[39;49;00m[37m [39;49;00m[31mkey[39;49;00m)[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m
  2301	[37m            [39;49;00m([34mcond[39;49;00m[37m[39;49;00m
  2302	[37m	     [39;49;00m(([32mmemq[39;49;00m[37m [39;49;00m[31manswer[39;49;00m[37m [39;49;00m'([31mskip[39;49;00m[37m [39;49;00m[31mact[39;49;00m))[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m
  2303	[37m	     [39;49;00m(([32meq[39;49;00m[37m [39;49;00m[31manswer[39;49;00m[37m [39;49;00m[33m'recenter[39;49;00m)[37m[39;49;00m
  2304	[37m	      [39;49;00m([32mrecenter[39;49;00m)[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m
  2305	[37m	     [39;49;00m(([32meq[39;49;00m[37m [39;49;00m[31manswer[39;49;00m[37m [39;49;00m[33m'scroll-up[39;49;00m)[37m[39;49;00m
  2306	[37m	      [39;49;00m([36mignore-errors[39;49;00m[37m [39;49;00m([31mscroll-up-command[39;49;00m))[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m
  2307	[37m	     [39;49;00m(([32meq[39;49;00m[37m [39;49;00m[31manswer[39;49;00m[37m [39;49;00m[33m'scroll-down[39;49;00m)[37m[39;49;00m
  2308	[37m	      [39;49;00m([36mignore-errors[39;49;00m[37m [39;49;00m([31mscroll-down-command[39;49;00m))[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m
  2309	[37m	     [39;49;00m(([32meq[39;49;00m[37m [39;49;00m[31manswer[39;49;00m[37m [39;49;00m[33m'scroll-other-window[39;49;00m)[37m[39;49;00m
  2310	[37m	      [39;49;00m([36mignore-errors[39;49;00m[37m [39;49;00m([32mscroll-other-window[39;49;00m))[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m
  2311	[37m	     [39;49;00m(([32meq[39;49;00m[37m [39;49;00m[31manswer[39;49;00m[37m [39;49;00m[33m'scroll-other-window-down[39;49;00m)[37m[39;49;00m
  2312	[37m	      [39;49;00m([36mignore-errors[39;49;00m[37m [39;49;00m([31mscroll-other-window-down[39;49;00m))[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m
  2313	[37m	     [39;49;00m(([34mor[39;49;00m[37m [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[31manswer[39;49;00m[37m [39;49;00m'([31mexit-prefix[39;49;00m[37m [39;49;00m[31mquit[39;49;00m))[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m[33m?\e[39;49;00m))[37m[39;49;00m
  2314	[37m	      [39;49;00m([32msignal[39;49;00m[37m [39;49;00m[33m'quit[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m
  2315	[37m	     [39;49;00m([31mt[39;49;00m[37m [39;49;00m[31mt[39;49;00m)))[37m[39;49;00m
  2316	[37m        [39;49;00m([32mding[39;49;00m)[37m[39;49;00m
  2317	[37m        [39;49;00m([32mdiscard-input[39;49;00m))))[37m[39;49;00m
  2318	[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mret[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31manswer[39;49;00m[37m [39;49;00m[33m'act[39;49;00m)))[37m[39;49;00m
  2319	[37m      [39;49;00m([36munless[39;49;00m[37m [39;49;00m[31mnoninteractive[39;49;00m[37m[39;49;00m
  2320	[37m        [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m%s%c[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mret[39;49;00m[37m [39;49;00m[33m?y[39;49;00m[37m [39;49;00m[33m?n[39;49;00m)))[37m[39;49;00m
  2321	[37m      [39;49;00m[31mret[39;49;00m)))[37m[39;49;00m
  2322	[37m[39;49;00m
  2323	[37m[39;49;00m[37m[39;49;00m
  2324	[37m;;; Atomic change groups.[39;49;00m[37m[39;49;00m
  2325	[37m[39;49;00m
  2326	([36mdefmacro[39;49;00m[37m [39;49;00m[36matomic-change-group[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m
  2327	[37m  [39;49;00m[33m"[39;49;00m[33mPerform BODY as an atomic change group.[39;49;00m
  2328	[33mThis means that if BODY exits abnormally,[39;49;00m
  2329	[33mall of its changes to the current buffer are undone.[39;49;00m
  2330	[33mThis works regardless of whether undo is enabled in the buffer.[39;49;00m
  2331	[33m[39;49;00m
  2332	[33mThis mechanism is transparent to ordinary use of undo;[39;49;00m
  2333	[33mif undo is enabled in the buffer and BODY succeeds, the[39;49;00m
  2334	[33muser can undo the change normally.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2335	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m
  2336	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mhandle[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m--change-group-handle--[39;49;00m[33m"[39;49;00m))[37m[39;49;00m
  2337	[37m	[39;49;00m([31msuccess[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m--change-group-success--[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m
  2338	[37m    [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m((,[31mhandle[39;49;00m[37m [39;49;00m([31mprepare-change-group[39;49;00m))[37m[39;49;00m
  2339	[37m	   [39;49;00m[37m;; Don't truncate any undo data in the middle of this.[39;49;00m[37m[39;49;00m
  2340	[37m	   [39;49;00m([31mundo-outer-limit[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m
  2341	[37m	   [39;49;00m([31mundo-limit[39;49;00m[37m [39;49;00m[31mmost-positive-fixnum[39;49;00m)[37m[39;49;00m
  2342	[37m	   [39;49;00m([31mundo-strong-limit[39;49;00m[37m [39;49;00m[31mmost-positive-fixnum[39;49;00m)[37m[39;49;00m
  2343	[37m	   [39;49;00m(,[31msuccess[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m
  2344	[37m       [39;49;00m([34munwind-protect[39;49;00m[37m[39;49;00m
  2345	[37m	   [39;49;00m([34mprogn[39;49;00m[37m[39;49;00m
  2346	[37m	     [39;49;00m[37m;; This is inside the unwind-protect because[39;49;00m[37m[39;49;00m
  2347	[37m	     [39;49;00m[37m;; it enables undo if that was disabled; we need[39;49;00m[37m[39;49;00m
  2348	[37m	     [39;49;00m[37m;; to make sure that it gets disabled again.[39;49;00m[37m[39;49;00m
  2349	[37m	     [39;49;00m([31mactivate-change-group[39;49;00m[37m [39;49;00m,[31mhandle[39;49;00m)[37m[39;49;00m
  2350	[37m	     [39;49;00m,@[31mbody[39;49;00m[37m[39;49;00m
  2351	[37m	     [39;49;00m([34msetq[39;49;00m[37m [39;49;00m,[31msuccess[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m
  2352	[37m	 [39;49;00m[37m;; Either of these functions will disable undo[39;49;00m[37m[39;49;00m
  2353	[37m	 [39;49;00m[37m;; if it was disabled before.[39;49;00m[37m[39;49;00m
  2354	[37m	 [39;49;00m([34mif[39;49;00m[37m [39;49;00m,[31msuccess[39;49;00m[37m[39;49;00m
  2355	[37m	     [39;49;00m([31maccept-change-group[39;49;00m[37m [39;49;00m,[31mhandle[39;49;00m)[37m[39;49;00m
  2356	[37m	   [39;49;00m([31mcancel-change-group[39;49;00m[37m [39;49;00m,[31mhandle[39;49;00m))))))[37m[39;49;00m
  2357	[37m[39;49;00m
  2358	([36mdefun[39;49;00m[37m [39;49;00m[31mprepare-change-group[39;49;00m[37m [39;49;00m([34m&optional[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m)[37m[39;49;00m
  2359	[37m  [39;49;00m[33m"[39;49;00m[33mReturn a handle for the current buffer's state, for a change group.[39;49;00m
  2360	[33mIf you specify BUFFER, make a handle for BUFFER's state instead.[39;49;00m
  2361	[33m[39;49;00m
  2362	[33mPass the handle to [39;49;00m[33m`activate-change-group'[39;49;00m[33m afterward to initiate[39;49;00m
  2363	[33mthe actual changes of the change group.[39;49;00m
  2364	[33m[39;49;00m
  2365	[33mTo finish the change group, call either [39;49;00m[33m`accept-change-group'[39;49;00m[33m or[39;49;00m
  2366	[33m`cancel-change-group'[39;49;00m[33m passing the same handle as argument.  Call[39;49;00m
  2367	[33m`accept-change-group'[39;49;00m[33m to accept the changes in the group as final;[39;49;00m
  2368	[33mcall [39;49;00m[33m`cancel-change-group'[39;49;00m[33m to undo them all.  You should use[39;49;00m
  2369	[33m`unwind-protect'[39;49;00m[33m to make sure the group is always finished.  The call[39;49;00m
  2370	[33mto [39;49;00m[33m`activate-change-group'[39;49;00m[33m should be inside the [39;49;00m[33m`unwind-protect'[39;49;00m[33m.[39;49;00m
  2371	[33mOnce you finish the group, don't use the handle again--don't try to[39;49;00m
  2372	[33mfinish the same group twice.  For a simple example of correct use, see[39;49;00m
  2373	[33mthe source code of [39;49;00m[33m`atomic-change-group'[39;49;00m[33m.[39;49;00m
  2374	[33m[39;49;00m
  2375	[33mThe handle records only the specified buffer.  To make a multibuffer[39;49;00m
  2376	[33mchange group, call this function once for each buffer you want to[39;49;00m
  2377	[33mcover, then use [39;49;00m[33m`nconc'[39;49;00m[33m to combine the returned values, like this:[39;49;00m
  2378	[33m[39;49;00m
  2379	[33m  (nconc (prepare-change-group buffer-1)[39;49;00m
  2380	[33m         (prepare-change-group buffer-2))[39;49;00m
  2381	[33m[39;49;00m
  2382	[33mYou can then activate that multibuffer change group with a single[39;49;00m
  2383	[33mcall to [39;49;00m[33m`activate-change-group'[39;49;00m[33m and finish it with a single call[39;49;00m
  2384	[33mto [39;49;00m[33m`accept-change-group'[39;49;00m[33m or [39;49;00m[33m`cancel-change-group'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2385	[37m[39;49;00m
  2386	[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m[39;49;00m
  2387	[37m      [39;49;00m([32mlist[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m [39;49;00m([36mwith-current-buffer[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m [39;49;00m[31mbuffer-undo-list[39;49;00m)))[37m[39;49;00m
  2388	[37m    [39;49;00m([32mlist[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m([32mcurrent-buffer[39;49;00m)[37m [39;49;00m[31mbuffer-undo-list[39;49;00m))))[37m[39;49;00m
  2389	[37m[39;49;00m
  2390	([36mdefun[39;49;00m[37m [39;49;00m[31mactivate-change-group[39;49;00m[37m [39;49;00m([31mhandle[39;49;00m)[37m[39;49;00m
  2391	[37m  [39;49;00m[33m"[39;49;00m[33mActivate a change group made with [39;49;00m[33m`prepare-change-group'[39;49;00m[33m (which see).[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2392	[37m  [39;49;00m([36mdolist[39;49;00m[37m [39;49;00m([32melt[39;49;00m[37m [39;49;00m[31mhandle[39;49;00m)[37m[39;49;00m
  2393	[37m    [39;49;00m([36mwith-current-buffer[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[32melt[39;49;00m)[37m[39;49;00m
  2394	[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mbuffer-undo-list[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m
  2395	[37m	  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbuffer-undo-list[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)))))[37m[39;49;00m
  2396	[37m[39;49;00m
  2397	([36mdefun[39;49;00m[37m [39;49;00m[31maccept-change-group[39;49;00m[37m [39;49;00m([31mhandle[39;49;00m)[37m[39;49;00m
  2398	[37m  [39;49;00m[33m"[39;49;00m[33mFinish a change group made with [39;49;00m[33m`prepare-change-group'[39;49;00m[33m (which see).[39;49;00m
  2399	[33mThis finishes the change group by accepting its changes as final.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2400	[37m  [39;49;00m([36mdolist[39;49;00m[37m [39;49;00m([32melt[39;49;00m[37m [39;49;00m[31mhandle[39;49;00m)[37m[39;49;00m
  2401	[37m    [39;49;00m([36mwith-current-buffer[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[32melt[39;49;00m)[37m[39;49;00m
  2402	[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[32melt[39;49;00m)[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m
  2403	[37m	  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbuffer-undo-list[39;49;00m[37m [39;49;00m[31mt[39;49;00m)))))[37m[39;49;00m
  2404	[37m[39;49;00m
  2405	([36mdefun[39;49;00m[37m [39;49;00m[31mcancel-change-group[39;49;00m[37m [39;49;00m([31mhandle[39;49;00m)[37m[39;49;00m
  2406	[37m  [39;49;00m[33m"[39;49;00m[33mFinish a change group made with [39;49;00m[33m`prepare-change-group'[39;49;00m[33m (which see).[39;49;00m
  2407	[33mThis finishes the change group by reverting all of its changes.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2408	[37m  [39;49;00m([36mdolist[39;49;00m[37m [39;49;00m([32melt[39;49;00m[37m [39;49;00m[31mhandle[39;49;00m)[37m[39;49;00m
  2409	[37m    [39;49;00m([36mwith-current-buffer[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[32melt[39;49;00m)[37m[39;49;00m
  2410	[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[32melt[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[32melt[39;49;00m))[37m[39;49;00m
  2411	[37m      [39;49;00m([34msave-restriction[39;49;00m[37m[39;49;00m
  2412	[37m	[39;49;00m[37m;; Widen buffer temporarily so if the buffer was narrowed within[39;49;00m[37m[39;49;00m
  2413	[37m	[39;49;00m[37m;; the body of `atomic-change-group' all changes can be undone.[39;49;00m[37m[39;49;00m
  2414	[37m	[39;49;00m([32mwiden[39;49;00m)[37m[39;49;00m
  2415	[37m	[39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mold-car[39;49;00m[37m[39;49;00m
  2416	[37m	       [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[32melt[39;49;00m)[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[32melt[39;49;00m)))[37m[39;49;00m
  2417	[37m	      [39;49;00m([31mold-cdr[39;49;00m[37m[39;49;00m
  2418	[37m	       [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[32melt[39;49;00m)[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[32melt[39;49;00m))))[37m[39;49;00m
  2419	[37m	  [39;49;00m[37m;; Temporarily truncate the undo log at ELT.[39;49;00m[37m[39;49;00m
  2420	[37m	  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[32melt[39;49;00m)[37m[39;49;00m
  2421	[37m	    [39;49;00m([32msetcar[39;49;00m[37m [39;49;00m[32melt[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m [39;49;00m([32msetcdr[39;49;00m[37m [39;49;00m[32melt[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m
  2422	[37m	  [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mlast-command[39;49;00m[37m [39;49;00m[33m'undo[39;49;00m)[37m [39;49;00m([31mundo-start[39;49;00m))[37m[39;49;00m
  2423	[37m	  [39;49;00m[37m;; Make sure there's no confusion.[39;49;00m[37m[39;49;00m
  2424	[37m	  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[32melt[39;49;00m)[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[32melt[39;49;00m[37m [39;49;00m([31mlast[39;49;00m[37m [39;49;00m[31mpending-undo-list[39;49;00m))))[37m[39;49;00m
  2425	[37m	    [39;49;00m([36merror[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mUndoing to some unrelated state[39;49;00m[33m"[39;49;00m))[37m[39;49;00m
  2426	[37m	  [39;49;00m[37m;; Undo it all.[39;49;00m[37m[39;49;00m
  2427	[37m	  [39;49;00m([34msave-excursion[39;49;00m[37m[39;49;00m
  2428	[37m	    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32mlistp[39;49;00m[37m [39;49;00m[31mpending-undo-list[39;49;00m)[37m [39;49;00m([31mundo-more[39;49;00m[37m [39;49;00m[34m1[39;49;00m)))[37m[39;49;00m
  2429	[37m	  [39;49;00m[37m;; Reset the modified cons cell ELT to its original content.[39;49;00m[37m[39;49;00m
  2430	[37m	  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[32melt[39;49;00m)[37m[39;49;00m
  2431	[37m	    [39;49;00m([32msetcar[39;49;00m[37m [39;49;00m[32melt[39;49;00m[37m [39;49;00m[31mold-car[39;49;00m)[37m[39;49;00m
  2432	[37m	    [39;49;00m([32msetcdr[39;49;00m[37m [39;49;00m[32melt[39;49;00m[37m [39;49;00m[31mold-cdr[39;49;00m))[37m[39;49;00m
  2433	[37m	  [39;49;00m[37m;; Revert the undo info to what it was when we grabbed the state.[39;49;00m[37m[39;49;00m
  2434	[37m	  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbuffer-undo-list[39;49;00m[37m [39;49;00m[32melt[39;49;00m))))))[37m[39;49;00m
  2435	[37m[39;49;00m[37m[39;49;00m
  2436	[37m;;;; Display-related functions.[39;49;00m[37m[39;49;00m
  2437	[37m[39;49;00m
  2438	[37m;; For compatibility.[39;49;00m[37m[39;49;00m
  2439	([36mdefine-obsolete-function-alias[39;49;00m[37m [39;49;00m[33m'redraw-modeline[39;49;00m[37m[39;49;00m
  2440	[37m  [39;49;00m[33m'force-mode-line-update[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m24.3[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  2441	[37m[39;49;00m
  2442	([36mdefun[39;49;00m[37m [39;49;00m[31mmomentary-string-display[39;49;00m[37m [39;49;00m([32mstring[39;49;00m[37m [39;49;00m[31mpos[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mexit-char[39;49;00m[37m [39;49;00m[32mmessage[39;49;00m)[37m[39;49;00m
  2443	[37m  [39;49;00m[33m"[39;49;00m[33mMomentarily display STRING in the buffer at POS.[39;49;00m
  2444	[33mDisplay remains until next event is input.[39;49;00m
  2445	[33mIf POS is a marker, only its position is used; its buffer is ignored.[39;49;00m
  2446	[33mOptional third arg EXIT-CHAR can be a character, event or event[39;49;00m
  2447	[33mdescription list.  EXIT-CHAR defaults to SPC.  If the input is[39;49;00m
  2448	[33mEXIT-CHAR it is swallowed; otherwise it is then available as[39;49;00m
  2449	[33minput (as a command if nothing else).[39;49;00m
  2450	[33mDisplay MESSAGE (optional fourth arg) in the echo area.[39;49;00m
  2451	[33mIf MESSAGE is nil, instructions to type EXIT-CHAR are displayed there.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2452	[37m  [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mexit-char[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mexit-char[39;49;00m[37m [39;49;00m[33m?\s[39;49;00m))[37m[39;49;00m
  2453	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mol[39;49;00m[37m [39;49;00m([32mmake-overlay[39;49;00m[37m [39;49;00m[31mpos[39;49;00m[37m [39;49;00m[31mpos[39;49;00m))[37m[39;49;00m
  2454	[37m        [39;49;00m([31mstr[39;49;00m[37m [39;49;00m([32mcopy-sequence[39;49;00m[37m [39;49;00m[32mstring[39;49;00m)))[37m[39;49;00m
  2455	[37m    [39;49;00m([34munwind-protect[39;49;00m[37m[39;49;00m
  2456	[37m        [39;49;00m([34mprogn[39;49;00m[37m[39;49;00m
  2457	[37m          [39;49;00m([34msave-excursion[39;49;00m[37m[39;49;00m
  2458	[37m            [39;49;00m([32moverlay-put[39;49;00m[37m [39;49;00m[31mol[39;49;00m[37m [39;49;00m[33m'after-string[39;49;00m[37m [39;49;00m[31mstr[39;49;00m)[37m[39;49;00m
  2459	[37m            [39;49;00m([32mgoto-char[39;49;00m[37m [39;49;00m[31mpos[39;49;00m)[37m[39;49;00m
  2460	[37m            [39;49;00m[37m;; To avoid trouble with out-of-bounds position[39;49;00m[37m[39;49;00m
  2461	[37m            [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mpos[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m))[37m[39;49;00m
  2462	[37m            [39;49;00m[37m;; If the string end is off screen, recenter now.[39;49;00m[37m[39;49;00m
  2463	[37m            [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32m<=[39;49;00m[37m [39;49;00m([32mwindow-end[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m [39;49;00m[31mpos[39;49;00m)[37m[39;49;00m
  2464	[37m                [39;49;00m([32mrecenter[39;49;00m[37m [39;49;00m([32m/[39;49;00m[37m [39;49;00m([31mwindow-height[39;49;00m)[37m [39;49;00m[34m2[39;49;00m))))[37m[39;49;00m
  2465	[37m          [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[32mmessage[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mType %s to continue editing.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  2466	[37m                   [39;49;00m([32msingle-key-description[39;49;00m[37m [39;49;00m[31mexit-char[39;49;00m))[37m[39;49;00m
  2467	[37m	  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mevent[39;49;00m[37m [39;49;00m([31mread-key[39;49;00m)))[37m[39;49;00m
  2468	[37m	    [39;49;00m[37m;; `exit-char' can be an event, or an event description list.[39;49;00m[37m[39;49;00m
  2469	[37m	    [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mevent[39;49;00m[37m [39;49;00m[31mexit-char[39;49;00m)[37m[39;49;00m
  2470	[37m		[39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mevent[39;49;00m[37m [39;49;00m([32mevent-convert-list[39;49;00m[37m [39;49;00m[31mexit-char[39;49;00m))[37m[39;49;00m
  2471	[37m		[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31munread-command-events[39;49;00m[37m[39;49;00m
  2472	[37m                      [39;49;00m([32mappend[39;49;00m[37m [39;49;00m([32mthis-single-command-raw-keys[39;49;00m))))))[37m[39;49;00m
  2473	[37m      [39;49;00m([32mdelete-overlay[39;49;00m[37m [39;49;00m[31mol[39;49;00m))))[37m[39;49;00m
  2474	[37m[39;49;00m
  2475	[37m[39;49;00m[37m[39;49;00m
  2476	[37m;;;; Overlay operations[39;49;00m[37m[39;49;00m
  2477	[37m[39;49;00m
  2478	([36mdefun[39;49;00m[37m [39;49;00m[31mcopy-overlay[39;49;00m[37m [39;49;00m([31mo[39;49;00m)[37m[39;49;00m
  2479	[37m  [39;49;00m[33m"[39;49;00m[33mReturn a copy of overlay O.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2480	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mo1[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32moverlay-buffer[39;49;00m[37m [39;49;00m[31mo[39;49;00m)[37m[39;49;00m
  2481	[37m                [39;49;00m([32mmake-overlay[39;49;00m[37m [39;49;00m([32moverlay-start[39;49;00m[37m [39;49;00m[31mo[39;49;00m)[37m [39;49;00m([32moverlay-end[39;49;00m[37m [39;49;00m[31mo[39;49;00m)[37m[39;49;00m
  2482	[37m                              [39;49;00m[37m;; FIXME: there's no easy way to find the[39;49;00m[37m[39;49;00m
  2483	[37m                              [39;49;00m[37m;; insertion-type of the two markers.[39;49;00m[37m[39;49;00m
  2484	[37m                              [39;49;00m([32moverlay-buffer[39;49;00m[37m [39;49;00m[31mo[39;49;00m))[37m[39;49;00m
  2485	[37m              [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mo1[39;49;00m[37m [39;49;00m([32mmake-overlay[39;49;00m[37m [39;49;00m([32mpoint-min[39;49;00m)[37m [39;49;00m([32mpoint-min[39;49;00m))))[37m[39;49;00m
  2486	[37m                [39;49;00m([32mdelete-overlay[39;49;00m[37m [39;49;00m[31mo1[39;49;00m)[37m[39;49;00m
  2487	[37m                [39;49;00m[31mo1[39;49;00m)))[37m[39;49;00m
  2488	[37m	[39;49;00m([31mprops[39;49;00m[37m [39;49;00m([32moverlay-properties[39;49;00m[37m [39;49;00m[31mo[39;49;00m)))[37m[39;49;00m
  2489	[37m    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m[31mprops[39;49;00m[37m[39;49;00m
  2490	[37m      [39;49;00m([32moverlay-put[39;49;00m[37m [39;49;00m[31mo1[39;49;00m[37m [39;49;00m([36mpop[39;49;00m[37m [39;49;00m[31mprops[39;49;00m)[37m [39;49;00m([36mpop[39;49;00m[37m [39;49;00m[31mprops[39;49;00m)))[37m[39;49;00m
  2491	[37m    [39;49;00m[31mo1[39;49;00m))[37m[39;49;00m
  2492	[37m[39;49;00m
  2493	([36mdefun[39;49;00m[37m [39;49;00m[31mremove-overlays[39;49;00m[37m [39;49;00m([34m&optional[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[31mname[39;49;00m[37m [39;49;00m[31mval[39;49;00m)[37m[39;49;00m
  2494	[37m  [39;49;00m[33m"[39;49;00m[33mClear BEG and END of overlays whose property NAME has value VAL.[39;49;00m
  2495	[33mOverlays might be moved and/or split.[39;49;00m
  2496	[33mBEG and END default respectively to the beginning and end of buffer.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2497	[37m  [39;49;00m[37m;; This speeds up the loops over overlays.[39;49;00m[37m[39;49;00m
  2498	[37m  [39;49;00m([36munless[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m[37m [39;49;00m([32mpoint-min[39;49;00m)))[37m[39;49;00m
  2499	[37m  [39;49;00m([36munless[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m([32mpoint-max[39;49;00m)))[37m[39;49;00m
  2500	[37m  [39;49;00m([32moverlay-recenter[39;49;00m[37m [39;49;00m[31mend[39;49;00m)[37m[39;49;00m
  2501	[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m)[37m[39;49;00m
  2502	[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m[37m [39;49;00m([34mprog1[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m))))[37m[39;49;00m
  2503	[37m  [39;49;00m([34msave-excursion[39;49;00m[37m[39;49;00m
  2504	[37m    [39;49;00m([36mdolist[39;49;00m[37m [39;49;00m([31mo[39;49;00m[37m [39;49;00m([32moverlays-in[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m[37m [39;49;00m[31mend[39;49;00m))[37m[39;49;00m
  2505	[37m      [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32moverlay-get[39;49;00m[37m [39;49;00m[31mo[39;49;00m[37m [39;49;00m[31mname[39;49;00m)[37m [39;49;00m[31mval[39;49;00m)[37m[39;49;00m
  2506	[37m	[39;49;00m[37m;; Either push this overlay outside beg...end[39;49;00m[37m[39;49;00m
  2507	[37m	[39;49;00m[37m;; or split it to exclude beg...end[39;49;00m[37m[39;49;00m
  2508	[37m	[39;49;00m[37m;; or delete it entirely (if it is contained in beg...end).[39;49;00m[37m[39;49;00m
  2509	[37m	[39;49;00m([34mif[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m([32moverlay-start[39;49;00m[37m [39;49;00m[31mo[39;49;00m)[37m [39;49;00m[31mbeg[39;49;00m)[37m[39;49;00m
  2510	[37m	    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m([32moverlay-end[39;49;00m[37m [39;49;00m[31mo[39;49;00m)[37m [39;49;00m[31mend[39;49;00m)[37m[39;49;00m
  2511	[37m		[39;49;00m([34mprogn[39;49;00m[37m[39;49;00m
  2512	[37m		  [39;49;00m([32mmove-overlay[39;49;00m[37m [39;49;00m([31mcopy-overlay[39;49;00m[37m [39;49;00m[31mo[39;49;00m)[37m[39;49;00m
  2513	[37m				[39;49;00m([32moverlay-start[39;49;00m[37m [39;49;00m[31mo[39;49;00m)[37m [39;49;00m[31mbeg[39;49;00m)[37m[39;49;00m
  2514	[37m		  [39;49;00m([32mmove-overlay[39;49;00m[37m [39;49;00m[31mo[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m([32moverlay-end[39;49;00m[37m [39;49;00m[31mo[39;49;00m)))[37m[39;49;00m
  2515	[37m	      [39;49;00m([32mmove-overlay[39;49;00m[37m [39;49;00m[31mo[39;49;00m[37m [39;49;00m([32moverlay-start[39;49;00m[37m [39;49;00m[31mo[39;49;00m)[37m [39;49;00m[31mbeg[39;49;00m))[37m[39;49;00m
  2516	[37m	  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m([32moverlay-end[39;49;00m[37m [39;49;00m[31mo[39;49;00m)[37m [39;49;00m[31mend[39;49;00m)[37m[39;49;00m
  2517	[37m	      [39;49;00m([32mmove-overlay[39;49;00m[37m [39;49;00m[31mo[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m([32moverlay-end[39;49;00m[37m [39;49;00m[31mo[39;49;00m))[37m[39;49;00m
  2518	[37m	    [39;49;00m([32mdelete-overlay[39;49;00m[37m [39;49;00m[31mo[39;49;00m)))))))[37m[39;49;00m
  2519	[37m[39;49;00m[37m[39;49;00m
  2520	[37m;;;; Miscellanea.[39;49;00m[37m[39;49;00m
  2521	[37m[39;49;00m
  2522	([34mdefvar[39;49;00m[37m [39;49;00m[31msuspend-hook[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m
  2523	[37m  [39;49;00m[33m"[39;49;00m[33mNormal hook run by [39;49;00m[33m`suspend-emacs'[39;49;00m[33m, before suspending.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  2524	[37m[39;49;00m
  2525	([34mdefvar[39;49;00m[37m [39;49;00m[31msuspend-resume-hook[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m
  2526	[37m  [39;49;00m[33m"[39;49;00m[33mNormal hook run by [39;49;00m[33m`suspend-emacs'[39;49;00m[33m, after Emacs is continued.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  2527	[37m[39;49;00m
  2528	([34mdefvar[39;49;00m[37m [39;49;00m[31mtemp-buffer-show-hook[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m
  2529	[37m  [39;49;00m[33m"[39;49;00m[33mNormal hook run by [39;49;00m[33m`with-output-to-temp-buffer'[39;49;00m[33m after displaying the buffer.[39;49;00m
  2530	[33mWhen the hook runs, the temporary buffer is current, and the window it[39;49;00m
  2531	[33mwas displayed in is selected.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  2532	[37m[39;49;00m
  2533	([34mdefvar[39;49;00m[37m [39;49;00m[31mtemp-buffer-setup-hook[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m
  2534	[37m  [39;49;00m[33m"[39;49;00m[33mNormal hook run by [39;49;00m[33m`with-output-to-temp-buffer'[39;49;00m[33m at the start.[39;49;00m
  2535	[33mWhen the hook runs, the temporary buffer is current.[39;49;00m
  2536	[33mThis hook is normally set up with a function to put the buffer in Help[39;49;00m
  2537	[33mmode.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  2538	[37m[39;49;00m
  2539	([34mdefconst[39;49;00m[37m [39;49;00m[31muser-emacs-directory[39;49;00m[37m[39;49;00m
  2540	[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31msystem-type[39;49;00m[37m [39;49;00m[33m'ms-dos[39;49;00m)[37m[39;49;00m
  2541	[37m      [39;49;00m[37m;; MS-DOS cannot have initial dot.[39;49;00m[37m[39;49;00m
  2542	[37m      [39;49;00m[33m"[39;49;00m[33m~/_emacs.d/[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2543	[37m    [39;49;00m[33m"[39;49;00m[33m~/.emacs.d/[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  2544	[37m  [39;49;00m[33m"[39;49;00m[33mDirectory beneath which additional per-user Emacs-specific files are placed.[39;49;00m
  2545	[33mVarious programs in Emacs store information in this directory.[39;49;00m
  2546	[33mNote that this should end with a directory separator.[39;49;00m
  2547	[33mSee also [39;49;00m[33m`locate-user-emacs-file'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  2548	[37m[39;49;00m[37m[39;49;00m
  2549	[37m;;;; Misc. useful functions.[39;49;00m[37m[39;49;00m
  2550	[37m[39;49;00m
  2551	([36mdefsubst[39;49;00m[37m [39;49;00m[31mbuffer-narrowed-p[39;49;00m[37m [39;49;00m()[37m[39;49;00m
  2552	[37m  [39;49;00m[33m"[39;49;00m[33mReturn non-nil if the current buffer is narrowed.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2553	[37m  [39;49;00m([32m/=[39;49;00m[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m([32mpoint-max[39;49;00m)[37m [39;49;00m([32mpoint-min[39;49;00m))[37m [39;49;00m([32mbuffer-size[39;49;00m)))[37m[39;49;00m
  2554	[37m[39;49;00m
  2555	([36mdefun[39;49;00m[37m [39;49;00m[31mfind-tag-default-bounds[39;49;00m[37m [39;49;00m()[37m[39;49;00m
  2556	[37m  [39;49;00m[33m"[39;49;00m[33mDetermine the boundaries of the default tag, based on text at point.[39;49;00m
  2557	[33mReturn a cons cell with the beginning and end of the found tag.[39;49;00m
  2558	[33mIf there is no plausible default, return nil.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2559	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m([31mfrom[39;49;00m[37m [39;49;00m[31mto[39;49;00m[37m [39;49;00m[31mbound[39;49;00m)[37m[39;49;00m
  2560	[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([34mprogn[39;49;00m[37m[39;49;00m
  2561	[37m		[39;49;00m[37m;; Look at text around `point'.[39;49;00m[37m[39;49;00m
  2562	[37m		[39;49;00m([34msave-excursion[39;49;00m[37m[39;49;00m
  2563	[37m		  [39;49;00m([32mskip-syntax-backward[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mw_[39;49;00m[33m"[39;49;00m)[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mfrom[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m)))[37m[39;49;00m
  2564	[37m		[39;49;00m([34msave-excursion[39;49;00m[37m[39;49;00m
  2565	[37m		  [39;49;00m([32mskip-syntax-forward[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mw_[39;49;00m[33m"[39;49;00m)[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mto[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m)))[37m[39;49;00m
  2566	[37m		[39;49;00m([32m>[39;49;00m[37m [39;49;00m[31mto[39;49;00m[37m [39;49;00m[31mfrom[39;49;00m))[37m[39;49;00m
  2567	[37m	      [39;49;00m[37m;; Look between `line-beginning-position' and `point'.[39;49;00m[37m[39;49;00m
  2568	[37m	      [39;49;00m([34msave-excursion[39;49;00m[37m[39;49;00m
  2569	[37m		[39;49;00m([34mand[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbound[39;49;00m[37m [39;49;00m([32mline-beginning-position[39;49;00m))[37m[39;49;00m
  2570	[37m		     [39;49;00m([32mskip-syntax-backward[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m^w_[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mbound[39;49;00m)[37m[39;49;00m
  2571	[37m		     [39;49;00m([32m>[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mto[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m))[37m [39;49;00m[31mbound[39;49;00m)[37m[39;49;00m
  2572	[37m		     [39;49;00m([32mskip-syntax-backward[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mw_[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  2573	[37m		     [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mfrom[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m))))[37m[39;49;00m
  2574	[37m	      [39;49;00m[37m;; Look between `point' and `line-end-position'.[39;49;00m[37m[39;49;00m
  2575	[37m	      [39;49;00m([34msave-excursion[39;49;00m[37m[39;49;00m
  2576	[37m		[39;49;00m([34mand[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbound[39;49;00m[37m [39;49;00m([32mline-end-position[39;49;00m))[37m[39;49;00m
  2577	[37m		     [39;49;00m([32mskip-syntax-forward[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m^w_[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mbound[39;49;00m)[37m[39;49;00m
  2578	[37m		     [39;49;00m([32m<[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mfrom[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m))[37m [39;49;00m[31mbound[39;49;00m)[37m[39;49;00m
  2579	[37m		     [39;49;00m([32mskip-syntax-forward[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mw_[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  2580	[37m		     [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mto[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m)))))[37m[39;49;00m
  2581	[37m      [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mfrom[39;49;00m[37m [39;49;00m[31mto[39;49;00m))))[37m[39;49;00m
  2582	[37m[39;49;00m
  2583	([36mdefun[39;49;00m[37m [39;49;00m[31mfind-tag-default[39;49;00m[37m [39;49;00m()[37m[39;49;00m
  2584	[37m  [39;49;00m[33m"[39;49;00m[33mDetermine default tag to search for, based on text at point.[39;49;00m
  2585	[33mIf there is no plausible default, return nil.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2586	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mbounds[39;49;00m[37m [39;49;00m([31mfind-tag-default-bounds[39;49;00m)))[37m[39;49;00m
  2587	[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31mbounds[39;49;00m[37m[39;49;00m
  2588	[37m      [39;49;00m([32mbuffer-substring-no-properties[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mbounds[39;49;00m)[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mbounds[39;49;00m)))))[37m[39;49;00m
  2589	[37m[39;49;00m
  2590	([36mdefun[39;49;00m[37m [39;49;00m[31mfind-tag-default-as-regexp[39;49;00m[37m [39;49;00m()[37m[39;49;00m
  2591	[37m  [39;49;00m[33m"[39;49;00m[33mReturn regexp that matches the default tag at point.[39;49;00m
  2592	[33mIf there is no tag at point, return nil.[39;49;00m
  2593	[33m[39;49;00m
  2594	[33mWhen in a major mode that does not provide its own[39;49;00m
  2595	[33m`find-tag-default-function'[39;49;00m[33m, return a regexp that matches the[39;49;00m
  2596	[33msymbol at point exactly.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2597	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtag[39;49;00m[37m [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mfind-tag-default-function[39;49;00m[37m[39;49;00m
  2598	[37m			  [39;49;00m([32mget[39;49;00m[37m [39;49;00m[31mmajor-mode[39;49;00m[37m [39;49;00m[33m'find-tag-default-function[39;49;00m)[37m[39;49;00m
  2599	[37m			  [39;49;00m[33m'find-tag-default[39;49;00m))))[37m[39;49;00m
  2600	[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mtag[39;49;00m[37m [39;49;00m([32mregexp-quote[39;49;00m[37m [39;49;00m[31mtag[39;49;00m))))[37m[39;49;00m
  2601	[37m[39;49;00m
  2602	([36mdefun[39;49;00m[37m [39;49;00m[31mfind-tag-default-as-symbol-regexp[39;49;00m[37m [39;49;00m()[37m[39;49;00m
  2603	[37m  [39;49;00m[33m"[39;49;00m[33mReturn regexp that matches the default tag at point as symbol.[39;49;00m
  2604	[33mIf there is no tag at point, return nil.[39;49;00m
  2605	[33m[39;49;00m
  2606	[33mWhen in a major mode that does not provide its own[39;49;00m
  2607	[33m`find-tag-default-function'[39;49;00m[33m, return a regexp that matches the[39;49;00m
  2608	[33msymbol at point exactly.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2609	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtag-regexp[39;49;00m[37m [39;49;00m([31mfind-tag-default-as-regexp[39;49;00m)))[37m[39;49;00m
  2610	[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mtag-regexp[39;49;00m[37m[39;49;00m
  2611	[37m	     [39;49;00m([32meq[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mfind-tag-default-function[39;49;00m[37m[39;49;00m
  2612	[37m		     [39;49;00m([32mget[39;49;00m[37m [39;49;00m[31mmajor-mode[39;49;00m[37m [39;49;00m[33m'find-tag-default-function[39;49;00m)[37m[39;49;00m
  2613	[37m		     [39;49;00m[33m'find-tag-default[39;49;00m)[37m[39;49;00m
  2614	[37m		 [39;49;00m[33m'find-tag-default[39;49;00m))[37m[39;49;00m
  2615	[37m	[39;49;00m([32mformat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m_<%s[39;49;00m[33m\\[39;49;00m[33m_>[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mtag-regexp[39;49;00m)[37m[39;49;00m
  2616	[37m      [39;49;00m[31mtag-regexp[39;49;00m)))[37m[39;49;00m
  2617	[37m[39;49;00m
  2618	([36mdefun[39;49;00m[37m [39;49;00m[31mplay-sound[39;49;00m[37m [39;49;00m([31msound[39;49;00m)[37m[39;49;00m
  2619	[37m  [39;49;00m[33m"[39;49;00m[33mSOUND is a list of the form [39;49;00m[33m`[39;49;00m[33m(sound KEYWORD VALUE...)'.[39;49;00m
  2620	[33mThe following keywords are recognized:[39;49;00m
  2621	[33m[39;49;00m
  2622	[33m  :file FILE - read sound data from FILE.  If FILE isn't an[39;49;00m
  2623	[33mabsolute file name, it is searched in [39;49;00m[33m`data-directory'[39;49;00m[33m.[39;49;00m
  2624	[33m[39;49;00m
  2625	[33m  :data DATA - read sound data from string DATA.[39;49;00m
  2626	[33m[39;49;00m
  2627	[33mExactly one of :file or :data must be present.[39;49;00m
  2628	[33m[39;49;00m
  2629	[33m  :volume VOL - set volume to VOL.  VOL must an integer in the[39;49;00m
  2630	[33mrange 0..100 or a float in the range 0..1.0.  If not specified,[39;49;00m
  2631	[33mdon't change the volume setting of the sound device.[39;49;00m
  2632	[33m[39;49;00m
  2633	[33m  :device DEVICE - play sound on DEVICE.  If not specified,[39;49;00m
  2634	[33ma system-dependent default device name is used.[39;49;00m
  2635	[33m[39;49;00m
  2636	[33mNote: :data and :device are currently not supported on Windows.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2637	[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mfboundp[39;49;00m[37m [39;49;00m[33m'play-sound-internal[39;49;00m)[37m[39;49;00m
  2638	[37m      [39;49;00m([32mplay-sound-internal[39;49;00m[37m [39;49;00m[31msound[39;49;00m)[37m[39;49;00m
  2639	[37m    [39;49;00m([36merror[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mThis Emacs binary lacks sound support[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m
  2640	[37m[39;49;00m
  2641	([36mdeclare-function[39;49;00m[37m [39;49;00m[31mw32-shell-dos-semantics[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mw32-fns[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m
  2642	[37m[39;49;00m
  2643	([36mdefun[39;49;00m[37m [39;49;00m[31mshell-quote-argument[39;49;00m[37m [39;49;00m([31margument[39;49;00m)[37m[39;49;00m
  2644	[37m  [39;49;00m[33m"[39;49;00m[33mQuote ARGUMENT for passing as argument to an inferior shell.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2645	[37m  [39;49;00m([34mcond[39;49;00m[37m[39;49;00m
  2646	[37m   [39;49;00m(([32meq[39;49;00m[37m [39;49;00m[31msystem-type[39;49;00m[37m [39;49;00m[33m'ms-dos[39;49;00m)[37m[39;49;00m
  2647	[37m    [39;49;00m[37m;; Quote using double quotes, but escape any existing quotes in[39;49;00m[37m[39;49;00m
  2648	[37m    [39;49;00m[37m;; the argument with backslashes.[39;49;00m[37m[39;49;00m
  2649	[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mresult[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  2650	[37m          [39;49;00m([31mstart[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m
  2651	[37m          [39;49;00m[31mend[39;49;00m)[37m[39;49;00m
  2652	[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m[^[39;49;00m[33m\"[39;49;00m[33m][39;49;00m[33m"[39;49;00m[37m [39;49;00m[31margument[39;49;00m))[37m[39;49;00m
  2653	[37m              [39;49;00m([32m<[39;49;00m[37m [39;49;00m([32mmatch-end[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31margument[39;49;00m)))[37m[39;49;00m
  2654	[37m          [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m[[39;49;00m[33m\"[39;49;00m[33m][39;49;00m[33m"[39;49;00m[37m [39;49;00m[31margument[39;49;00m[37m [39;49;00m[31mstart[39;49;00m)[37m[39;49;00m
  2655	[37m            [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m([32mmatch-beginning[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m
  2656	[37m                  [39;49;00m[31mresult[39;49;00m[37m [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[31mresult[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[31margument[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mend[39;49;00m)[37m[39;49;00m
  2657	[37m                                 [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m"[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[31margument[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m([32m1+[39;49;00m[37m [39;49;00m[31mend[39;49;00m)))[37m[39;49;00m
  2658	[37m                  [39;49;00m[31mstart[39;49;00m[37m [39;49;00m([32m1+[39;49;00m[37m [39;49;00m[31mend[39;49;00m))))[37m[39;49;00m
  2659	[37m      [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mresult[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[31margument[39;49;00m[37m [39;49;00m[31mstart[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m
  2660	[37m[39;49;00m
  2661	[37m   [39;49;00m(([34mand[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31msystem-type[39;49;00m[37m [39;49;00m[33m'windows-nt[39;49;00m)[37m [39;49;00m([31mw32-shell-dos-semantics[39;49;00m))[37m[39;49;00m
  2662	[37m[39;49;00m
  2663	[37m    [39;49;00m[37m;; First, quote argument so that CommandLineToArgvW will[39;49;00m[37m[39;49;00m
  2664	[37m    [39;49;00m[37m;; understand it.  See[39;49;00m[37m[39;49;00m
  2665	[37m    [39;49;00m[37m;; http://msdn.microsoft.com/en-us/library/17w5ykft%28v=vs.85%29.aspx[39;49;00m[37m[39;49;00m
  2666	[37m    [39;49;00m[37m;; After we perform that level of quoting, escape shell[39;49;00m[37m[39;49;00m
  2667	[37m    [39;49;00m[37m;; metacharacters so that cmd won't mangle our argument.  If the[39;49;00m[37m[39;49;00m
  2668	[37m    [39;49;00m[37m;; argument contains no double quote characters, we can just[39;49;00m[37m[39;49;00m
  2669	[37m    [39;49;00m[37m;; surround it with double quotes.  Otherwise, we need to prefix[39;49;00m[37m[39;49;00m
  2670	[37m    [39;49;00m[37m;; each shell metacharacter with a caret.[39;49;00m[37m[39;49;00m
  2671	[37m[39;49;00m
  2672	[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31margument[39;49;00m[37m[39;49;00m
  2673	[37m          [39;49;00m[37m;; escape backslashes at end of string[39;49;00m[37m[39;49;00m
  2674	[37m          [39;49;00m([31mreplace-regexp-in-string[39;49;00m[37m[39;49;00m
  2675	[37m           [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m([39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m*[39;49;00m[33m\\[39;49;00m[33m)$[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2676	[37m           [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m1[39;49;00m[33m\\[39;49;00m[33m1[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2677	[37m           [39;49;00m[37m;; escape backslashes and quotes in string body[39;49;00m[37m[39;49;00m
  2678	[37m           [39;49;00m([31mreplace-regexp-in-string[39;49;00m[37m[39;49;00m
  2679	[37m            [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m([39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m*[39;49;00m[33m\\[39;49;00m[33m)[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2680	[37m            [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m1[39;49;00m[33m\\[39;49;00m[33m1[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2681	[37m            [39;49;00m[31margument[39;49;00m)))[37m[39;49;00m
  2682	[37m[39;49;00m
  2683	[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m[%![39;49;00m[33m\"[39;49;00m[33m][39;49;00m[33m"[39;49;00m[37m [39;49;00m[31margument[39;49;00m)[37m[39;49;00m
  2684	[37m        [39;49;00m([32mconcat[39;49;00m[37m[39;49;00m
  2685	[37m         [39;49;00m[33m"[39;49;00m[33m^[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2686	[37m         [39;49;00m([31mreplace-regexp-in-string[39;49;00m[37m[39;49;00m
  2687	[37m          [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m([%!()[39;49;00m[33m\"[39;49;00m[33m<>&|^][39;49;00m[33m\\[39;49;00m[33m)[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2688	[37m          [39;49;00m[33m"[39;49;00m[33m^[39;49;00m[33m\\[39;49;00m[33m1[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2689	[37m          [39;49;00m[31margument[39;49;00m)[37m[39;49;00m
  2690	[37m         [39;49;00m[33m"[39;49;00m[33m^[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  2691	[37m      [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31margument[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m
  2692	[37m[39;49;00m
  2693	[37m   [39;49;00m([31mt[39;49;00m[37m[39;49;00m
  2694	[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mequal[39;49;00m[37m [39;49;00m[31margument[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  2695	[37m        [39;49;00m[33m"[39;49;00m[33m''[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2696	[37m      [39;49;00m[37m;; Quote everything except POSIX filename characters.[39;49;00m[37m[39;49;00m
  2697	[37m      [39;49;00m[37m;; This should be safe enough even for really weird shells.[39;49;00m[37m[39;49;00m
  2698	[37m      [39;49;00m([31mreplace-regexp-in-string[39;49;00m[37m[39;49;00m
  2699	[37m       [39;49;00m[33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m'[39;49;00m[33m\n[39;49;00m[33m'[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2700	[37m       [39;49;00m([31mreplace-regexp-in-string[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m[^-0-9a-zA-Z_./[39;49;00m[33m\n[39;49;00m[33m][39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m&[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31margument[39;49;00m))))[37m[39;49;00m
  2701	[37m   [39;49;00m))[37m[39;49;00m
  2702	[37m[39;49;00m
  2703	([36mdefun[39;49;00m[37m [39;49;00m[31mstring-or-null-p[39;49;00m[37m [39;49;00m([31mobject[39;49;00m)[37m[39;49;00m
  2704	[37m  [39;49;00m[33m"[39;49;00m[33mReturn t if OBJECT is a string or nil.[39;49;00m
  2705	[33mOtherwise, return nil.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2706	[37m  [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m[31mobject[39;49;00m)[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[31mobject[39;49;00m)))[37m[39;49;00m
  2707	[37m[39;49;00m
  2708	([36mdefun[39;49;00m[37m [39;49;00m[31mbooleanp[39;49;00m[37m [39;49;00m([31mobject[39;49;00m)[37m[39;49;00m
  2709	[37m  [39;49;00m[33m"[39;49;00m[33mReturn t if OBJECT is one of the two canonical boolean values: t or nil.[39;49;00m
  2710	[33mOtherwise, return nil.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2711	[37m  [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[31mobject[39;49;00m[37m [39;49;00m'([31mnil[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m
  2712	[37m[39;49;00m
  2713	([36mdefun[39;49;00m[37m [39;49;00m[31mspecial-form-p[39;49;00m[37m [39;49;00m([31mobject[39;49;00m)[37m[39;49;00m
  2714	[37m  [39;49;00m[33m"[39;49;00m[33mNon-nil if and only if OBJECT is a special form.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2715	[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32msymbolp[39;49;00m[37m [39;49;00m[31mobject[39;49;00m)[37m [39;49;00m([32mfboundp[39;49;00m[37m [39;49;00m[31mobject[39;49;00m))[37m[39;49;00m
  2716	[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mobject[39;49;00m[37m [39;49;00m([32mindirect-function[39;49;00m[37m [39;49;00m[31mobject[39;49;00m[37m [39;49;00m[31mt[39;49;00m)))[37m[39;49;00m
  2717	[37m  [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32msubrp[39;49;00m[37m [39;49;00m[31mobject[39;49;00m)[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m([34msubr-arity[39;49;00m[37m [39;49;00m[31mobject[39;49;00m))[37m [39;49;00m[33m'unevalled[39;49;00m)))[37m[39;49;00m
  2718	[37m[39;49;00m
  2719	([36mdefun[39;49;00m[37m [39;49;00m[31mmacrop[39;49;00m[37m [39;49;00m([31mobject[39;49;00m)[37m[39;49;00m
  2720	[37m  [39;49;00m[33m"[39;49;00m[33mNon-nil if and only if OBJECT is a macro.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2721	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mdef[39;49;00m[37m [39;49;00m([32mindirect-function[39;49;00m[37m [39;49;00m[31mobject[39;49;00m[37m [39;49;00m[31mt[39;49;00m)))[37m[39;49;00m
  2722	[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mdef[39;49;00m)[37m[39;49;00m
  2723	[37m      [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[33m'macro[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mdef[39;49;00m))[37m[39;49;00m
  2724	[37m          [39;49;00m([34mand[39;49;00m[37m [39;49;00m([31mautoloadp[39;49;00m[37m [39;49;00m[31mdef[39;49;00m)[37m [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m4[39;49;00m[37m [39;49;00m[31mdef[39;49;00m)[37m [39;49;00m'([31mmacro[39;49;00m[37m [39;49;00m[31mt[39;49;00m)))))))[37m[39;49;00m
  2725	[37m[39;49;00m
  2726	([36mdefun[39;49;00m[37m [39;49;00m[31mfield-at-pos[39;49;00m[37m [39;49;00m([31mpos[39;49;00m)[37m[39;49;00m
  2727	[37m  [39;49;00m[33m"[39;49;00m[33mReturn the field at position POS, taking stickiness etc into account.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2728	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mraw-field[39;49;00m[37m [39;49;00m([32mget-char-property[39;49;00m[37m [39;49;00m([32mfield-beginning[39;49;00m[37m [39;49;00m[31mpos[39;49;00m)[37m [39;49;00m[33m'field[39;49;00m)))[37m[39;49;00m
  2729	[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mraw-field[39;49;00m[37m [39;49;00m[33m'boundary[39;49;00m)[37m[39;49;00m
  2730	[37m	[39;49;00m([32mget-char-property[39;49;00m[37m [39;49;00m([32m1-[39;49;00m[37m [39;49;00m([32mfield-end[39;49;00m[37m [39;49;00m[31mpos[39;49;00m))[37m [39;49;00m[33m'field[39;49;00m)[37m[39;49;00m
  2731	[37m      [39;49;00m[31mraw-field[39;49;00m)))[37m[39;49;00m
  2732	[37m[39;49;00m
  2733	([36mdefun[39;49;00m[37m [39;49;00m[31msha1[39;49;00m[37m [39;49;00m([31mobject[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[31mbinary[39;49;00m)[37m[39;49;00m
  2734	[37m  [39;49;00m[33m"[39;49;00m[33mReturn the SHA1 (Secure Hash Algorithm) of an OBJECT.[39;49;00m
  2735	[33mOBJECT is either a string or a buffer.  Optional arguments START and[39;49;00m
  2736	[33mEND are character positions specifying which portion of OBJECT for[39;49;00m
  2737	[33mcomputing the hash.  If BINARY is non-nil, return a string in binary[39;49;00m
  2738	[33mform.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2739	[37m  [39;49;00m([32msecure-hash[39;49;00m[37m [39;49;00m[33m'sha1[39;49;00m[37m [39;49;00m[31mobject[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[31mbinary[39;49;00m))[37m[39;49;00m
  2740	[37m[39;49;00m
  2741	([36mdefun[39;49;00m[37m [39;49;00m[31mfunction-get[39;49;00m[37m [39;49;00m([31mf[39;49;00m[37m [39;49;00m[31mprop[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[32mautoload[39;49;00m)[37m[39;49;00m
  2742	[37m  [39;49;00m[33m"[39;49;00m[33mReturn the value of property PROP of function F.[39;49;00m
  2743	[33mIf AUTOLOAD is non-nil and F is autoloaded, try to autoload it[39;49;00m
  2744	[33min the hope that it will set PROP.  If AUTOLOAD is [39;49;00m[33m`macro'[39;49;00m[33m, only do it[39;49;00m
  2745	[33mif it's an autoloaded macro.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2746	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mval[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m
  2747	[37m    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32msymbolp[39;49;00m[37m [39;49;00m[31mf[39;49;00m)[37m[39;49;00m
  2748	[37m                [39;49;00m([32mnull[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mval[39;49;00m[37m [39;49;00m([32mget[39;49;00m[37m [39;49;00m[31mf[39;49;00m[37m [39;49;00m[31mprop[39;49;00m)))[37m[39;49;00m
  2749	[37m                [39;49;00m([32mfboundp[39;49;00m[37m [39;49;00m[31mf[39;49;00m))[37m[39;49;00m
  2750	[37m      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mfundef[39;49;00m[37m [39;49;00m([32msymbol-function[39;49;00m[37m [39;49;00m[31mf[39;49;00m)))[37m[39;49;00m
  2751	[37m        [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[32mautoload[39;49;00m[37m [39;49;00m([31mautoloadp[39;49;00m[37m [39;49;00m[31mfundef[39;49;00m)[37m[39;49;00m
  2752	[37m                 [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mequal[39;49;00m[37m [39;49;00m[31mfundef[39;49;00m[37m[39;49;00m
  2753	[37m                             [39;49;00m([32mautoload-do-load[39;49;00m[37m [39;49;00m[31mfundef[39;49;00m[37m [39;49;00m[31mf[39;49;00m[37m[39;49;00m
  2754	[37m                                               [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[32mautoload[39;49;00m[37m [39;49;00m[33m'macro[39;49;00m)[37m[39;49;00m
  2755	[37m                                                   [39;49;00m[33m'macro[39;49;00m)))))[37m[39;49;00m
  2756	[37m            [39;49;00m[31mnil[39;49;00m[37m                         [39;49;00m[37m;Re-try `get' on the same `f'.[39;49;00m[37m[39;49;00m
  2757	[37m          [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mf[39;49;00m[37m [39;49;00m[31mfundef[39;49;00m))))[37m[39;49;00m
  2758	[37m    [39;49;00m[31mval[39;49;00m))[37m[39;49;00m
  2759	[37m[39;49;00m[37m[39;49;00m
  2760	[37m;;;; Support for yanking and text properties.[39;49;00m[37m[39;49;00m
  2761	[37m;; Why here in subr.el rather than in simple.el?  --Stef[39;49;00m[37m[39;49;00m
  2762	[37m[39;49;00m
  2763	([34mdefvar[39;49;00m[37m [39;49;00m[31myank-handled-properties[39;49;00m)[37m[39;49;00m
  2764	([34mdefvar[39;49;00m[37m [39;49;00m[31myank-excluded-properties[39;49;00m)[37m[39;49;00m
  2765	[37m[39;49;00m
  2766	([36mdefun[39;49;00m[37m [39;49;00m[31mremove-yank-excluded-properties[39;49;00m[37m [39;49;00m([31mstart[39;49;00m[37m [39;49;00m[31mend[39;49;00m)[37m[39;49;00m
  2767	[37m  [39;49;00m[33m"[39;49;00m[33mProcess text properties between START and END, inserted for a [39;49;00m[33m`yank'[39;49;00m[33m.[39;49;00m
  2768	[33mPerform the handling specified by [39;49;00m[33m`yank-handled-properties'[39;49;00m[33m, then[39;49;00m
  2769	[33mremove properties specified by [39;49;00m[33m`yank-excluded-properties'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2770	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31minhibit-read-only[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m
  2771	[37m    [39;49;00m([36mdolist[39;49;00m[37m [39;49;00m([31mhandler[39;49;00m[37m [39;49;00m[31myank-handled-properties[39;49;00m)[37m[39;49;00m
  2772	[37m      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mprop[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mhandler[39;49;00m))[37m[39;49;00m
  2773	[37m	    [39;49;00m([31mfun[39;49;00m[37m  [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mhandler[39;49;00m))[37m[39;49;00m
  2774	[37m	    [39;49;00m([31mrun-start[39;49;00m[37m [39;49;00m[31mstart[39;49;00m))[37m[39;49;00m
  2775	[37m	[39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m[31mrun-start[39;49;00m[37m [39;49;00m[31mend[39;49;00m)[37m[39;49;00m
  2776	[37m	  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mvalue[39;49;00m[37m [39;49;00m([32mget-text-property[39;49;00m[37m [39;49;00m[31mrun-start[39;49;00m[37m [39;49;00m[31mprop[39;49;00m))[37m[39;49;00m
  2777	[37m		[39;49;00m([31mrun-end[39;49;00m[37m [39;49;00m([32mnext-single-property-change[39;49;00m[37m[39;49;00m
  2778	[37m			  [39;49;00m[31mrun-start[39;49;00m[37m [39;49;00m[31mprop[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mend[39;49;00m)))[37m[39;49;00m
  2779	[37m	    [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mfun[39;49;00m[37m [39;49;00m[31mvalue[39;49;00m[37m [39;49;00m[31mrun-start[39;49;00m[37m [39;49;00m[31mrun-end[39;49;00m)[37m[39;49;00m
  2780	[37m	    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mrun-start[39;49;00m[37m [39;49;00m[31mrun-end[39;49;00m)))))[37m[39;49;00m
  2781	[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31myank-excluded-properties[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m
  2782	[37m	[39;49;00m([32mset-text-properties[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m
  2783	[37m      [39;49;00m([32mremove-list-of-text-properties[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[31myank-excluded-properties[39;49;00m))))[37m[39;49;00m
  2784	[37m[39;49;00m
  2785	([34mdefvar[39;49;00m[37m [39;49;00m[31myank-undo-function[39;49;00m)[37m[39;49;00m
  2786	[37m[39;49;00m
  2787	([36mdefun[39;49;00m[37m [39;49;00m[31minsert-for-yank[39;49;00m[37m [39;49;00m([32mstring[39;49;00m)[37m[39;49;00m
  2788	[37m  [39;49;00m[33m"[39;49;00m[33mCall [39;49;00m[33m`insert-for-yank-1'[39;49;00m[33m repetitively for each [39;49;00m[33m`yank-handler'[39;49;00m[33m segment.[39;49;00m
  2789	[33m[39;49;00m
  2790	[33mSee [39;49;00m[33m`insert-for-yank-1'[39;49;00m[33m for more details.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2791	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m([31mto[39;49;00m)[37m[39;49;00m
  2792	[37m    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mto[39;49;00m[37m [39;49;00m([32mnext-single-property-change[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[33m'yank-handler[39;49;00m[37m [39;49;00m[32mstring[39;49;00m))[37m[39;49;00m
  2793	[37m      [39;49;00m([31minsert-for-yank-1[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[31mto[39;49;00m))[37m[39;49;00m
  2794	[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[31mto[39;49;00m))))[37m[39;49;00m
  2795	[37m  [39;49;00m([31minsert-for-yank-1[39;49;00m[37m [39;49;00m[32mstring[39;49;00m))[37m[39;49;00m
  2796	[37m[39;49;00m
  2797	([36mdefun[39;49;00m[37m [39;49;00m[31minsert-for-yank-1[39;49;00m[37m [39;49;00m([32mstring[39;49;00m)[37m[39;49;00m
  2798	[37m  [39;49;00m[33m"[39;49;00m[33mInsert STRING at point for the [39;49;00m[33m`yank'[39;49;00m[33m command.[39;49;00m
  2799	[33mThis function is like [39;49;00m[33m`insert'[39;49;00m[33m, except it honors the variables[39;49;00m
  2800	[33m`yank-handled-properties'[39;49;00m[33m and [39;49;00m[33m`yank-excluded-properties'[39;49;00m[33m, and the[39;49;00m
  2801	[33m`yank-handler'[39;49;00m[33m text property.[39;49;00m
  2802	[33m[39;49;00m
  2803	[33mProperties listed in [39;49;00m[33m`yank-handled-properties'[39;49;00m[33m are processed,[39;49;00m
  2804	[33mthen those listed in [39;49;00m[33m`yank-excluded-properties'[39;49;00m[33m are discarded.[39;49;00m
  2805	[33m[39;49;00m
  2806	[33mIf STRING has a non-nil [39;49;00m[33m`yank-handler'[39;49;00m[33m property on its first[39;49;00m
  2807	[33mcharacter, the normal insert behavior is altered.  The value of[39;49;00m
  2808	[33mthe [39;49;00m[33m`yank-handler'[39;49;00m[33m property must be a list of one to four[39;49;00m
  2809	[33melements, of the form (FUNCTION PARAM NOEXCLUDE UNDO).[39;49;00m
  2810	[33mFUNCTION, if non-nil, should be a function of one argument, an[39;49;00m
  2811	[33m object to insert; it is called instead of [39;49;00m[33m`insert'[39;49;00m[33m.[39;49;00m
  2812	[33mPARAM, if present and non-nil, replaces STRING as the argument to[39;49;00m
  2813	[33m FUNCTION or [39;49;00m[33m`insert'[39;49;00m[33m; e.g. if FUNCTION is [39;49;00m[33m`yank-rectangle'[39;49;00m[33m, PARAM[39;49;00m
  2814	[33m may be a list of strings to insert as a rectangle.[39;49;00m
  2815	[33mIf NOEXCLUDE is present and non-nil, the normal removal of[39;49;00m
  2816	[33m [39;49;00m[33m`yank-excluded-properties'[39;49;00m[33m is not performed; instead FUNCTION is[39;49;00m
  2817	[33m responsible for the removal.  This may be necessary if FUNCTION[39;49;00m
  2818	[33m adjusts point before or after inserting the object.[39;49;00m
  2819	[33mUNDO, if present and non-nil, should be a function to be called[39;49;00m
  2820	[33m by [39;49;00m[33m`yank-pop'[39;49;00m[33m to undo the insertion of the current object.  It is[39;49;00m
  2821	[33m given two arguments, the start and end of the region.  FUNCTION[39;49;00m
  2822	[33m may set [39;49;00m[33m`yank-undo-function'[39;49;00m[33m to override UNDO.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2823	[37m  [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mhandler[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m[32mstring[39;49;00m)[37m[39;49;00m
  2824	[37m		       [39;49;00m([32mget-text-property[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[33m'yank-handler[39;49;00m[37m [39;49;00m[32mstring[39;49;00m)))[37m[39;49;00m
  2825	[37m	 [39;49;00m([31mparam[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mhandler[39;49;00m)[37m [39;49;00m[32mstring[39;49;00m))[37m[39;49;00m
  2826	[37m	 [39;49;00m([31mopoint[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m))[37m[39;49;00m
  2827	[37m	 [39;49;00m([31minhibit-read-only[39;49;00m[37m [39;49;00m[31minhibit-read-only[39;49;00m)[37m[39;49;00m
  2828	[37m	 [39;49;00m[31mend[39;49;00m)[37m[39;49;00m
  2829	[37m[39;49;00m
  2830	[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31myank-undo-function[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m
  2831	[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[31mhandler[39;49;00m)[37m [39;49;00m[37m; FUNCTION[39;49;00m[37m[39;49;00m
  2832	[37m	[39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mhandler[39;49;00m)[37m [39;49;00m[31mparam[39;49;00m)[37m[39;49;00m
  2833	[37m      [39;49;00m([32minsert[39;49;00m[37m [39;49;00m[31mparam[39;49;00m))[37m[39;49;00m
  2834	[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m))[37m[39;49;00m
  2835	[37m[39;49;00m
  2836	[37m    [39;49;00m[37m;; Prevent read-only properties from interfering with the[39;49;00m[37m[39;49;00m
  2837	[37m    [39;49;00m[37m;; following text property changes.[39;49;00m[37m[39;49;00m
  2838	[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31minhibit-read-only[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m
  2839	[37m[39;49;00m
  2840	[37m    [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m[31mhandler[39;49;00m)[37m [39;49;00m[37m; NOEXCLUDE[39;49;00m[37m[39;49;00m
  2841	[37m      [39;49;00m([31mremove-yank-excluded-properties[39;49;00m[37m [39;49;00m[31mopoint[39;49;00m[37m [39;49;00m[31mend[39;49;00m))[37m[39;49;00m
  2842	[37m[39;49;00m
  2843	[37m    [39;49;00m[37m;; If last inserted char has properties, mark them as rear-nonsticky.[39;49;00m[37m[39;49;00m
  2844	[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[31mopoint[39;49;00m)[37m[39;49;00m
  2845	[37m	     [39;49;00m([32mtext-properties-at[39;49;00m[37m [39;49;00m([32m1-[39;49;00m[37m [39;49;00m[31mend[39;49;00m)))[37m[39;49;00m
  2846	[37m	[39;49;00m([32mput-text-property[39;49;00m[37m [39;49;00m([32m1-[39;49;00m[37m [39;49;00m[31mend[39;49;00m)[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[33m'rear-nonsticky[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m
  2847	[37m[39;49;00m
  2848	[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31myank-undo-function[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m		   [39;49;00m[37m; not set by FUNCTION[39;49;00m[37m[39;49;00m
  2849	[37m	[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31myank-undo-function[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m3[39;49;00m[37m [39;49;00m[31mhandler[39;49;00m)))[37m [39;49;00m[37m; UNDO[39;49;00m[37m[39;49;00m
  2850	[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m4[39;49;00m[37m [39;49;00m[31mhandler[39;49;00m)[37m				   [39;49;00m[37m; COMMAND[39;49;00m[37m[39;49;00m
  2851	[37m	[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mthis-command[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m4[39;49;00m[37m [39;49;00m[31mhandler[39;49;00m)))))[37m[39;49;00m
  2852	[37m[39;49;00m
  2853	([36mdefun[39;49;00m[37m [39;49;00m[31minsert-buffer-substring-no-properties[39;49;00m[37m [39;49;00m([31mbuffer[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mend[39;49;00m)[37m[39;49;00m
  2854	[37m  [39;49;00m[33m"[39;49;00m[33mInsert before point a substring of BUFFER, without text properties.[39;49;00m
  2855	[33mBUFFER may be a buffer or a buffer name.[39;49;00m
  2856	[33mArguments START and END are character positions specifying the substring.[39;49;00m
  2857	[33mThey default to the values of (point-min) and (point-max) in BUFFER.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2858	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mopoint[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m)))[37m[39;49;00m
  2859	[37m    [39;49;00m([32minsert-buffer-substring[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mend[39;49;00m)[37m[39;49;00m
  2860	[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31minhibit-read-only[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m
  2861	[37m      [39;49;00m([32mset-text-properties[39;49;00m[37m [39;49;00m[31mopoint[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m)[37m [39;49;00m[31mnil[39;49;00m))))[37m[39;49;00m
  2862	[37m[39;49;00m
  2863	([36mdefun[39;49;00m[37m [39;49;00m[31minsert-buffer-substring-as-yank[39;49;00m[37m [39;49;00m([31mbuffer[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mend[39;49;00m)[37m[39;49;00m
  2864	[37m  [39;49;00m[33m"[39;49;00m[33mInsert before point a part of BUFFER, stripping some text properties.[39;49;00m
  2865	[33mBUFFER may be a buffer or a buffer name.[39;49;00m
  2866	[33mArguments START and END are character positions specifying the substring.[39;49;00m
  2867	[33mThey default to the values of (point-min) and (point-max) in BUFFER.[39;49;00m
  2868	[33mBefore insertion, process text properties according to[39;49;00m
  2869	[33m`yank-handled-properties'[39;49;00m[33m and [39;49;00m[33m`yank-excluded-properties'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2870	[37m  [39;49;00m[37m;; Since the buffer text should not normally have yank-handler properties,[39;49;00m[37m[39;49;00m
  2871	[37m  [39;49;00m[37m;; there is no need to handle them here.[39;49;00m[37m[39;49;00m
  2872	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mopoint[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m)))[37m[39;49;00m
  2873	[37m    [39;49;00m([32minsert-buffer-substring[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mend[39;49;00m)[37m[39;49;00m
  2874	[37m    [39;49;00m([31mremove-yank-excluded-properties[39;49;00m[37m [39;49;00m[31mopoint[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m))))[37m[39;49;00m
  2875	[37m[39;49;00m
  2876	([36mdefun[39;49;00m[37m [39;49;00m[31myank-handle-font-lock-face-property[39;49;00m[37m [39;49;00m([31mface[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mend[39;49;00m)[37m[39;49;00m
  2877	[37m  [39;49;00m[33m"[39;49;00m[33mIf [39;49;00m[33m`font-lock-defaults'[39;49;00m[33m is nil, apply FACE as a [39;49;00m[33m`face'[39;49;00m[33m property.[39;49;00m
  2878	[33mSTART and END denote the start and end of the text to act on.[39;49;00m
  2879	[33mDo nothing if FACE is nil.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2880	[37m  [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mface[39;49;00m[37m[39;49;00m
  2881	[37m       [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[31mfont-lock-defaults[39;49;00m)[37m[39;49;00m
  2882	[37m       [39;49;00m([32mput-text-property[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[33m'face[39;49;00m[37m [39;49;00m[31mface[39;49;00m)))[37m[39;49;00m
  2883	[37m[39;49;00m
  2884	[37m;; This removes `mouse-face' properties in *Help* buffer buttons:[39;49;00m[37m[39;49;00m
  2885	[37m;; http://lists.gnu.org/archive/html/emacs-devel/2002-04/msg00648.html[39;49;00m[37m[39;49;00m
  2886	([36mdefun[39;49;00m[37m [39;49;00m[31myank-handle-category-property[39;49;00m[37m [39;49;00m([31mcategory[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mend[39;49;00m)[37m[39;49;00m
  2887	[37m  [39;49;00m[33m"[39;49;00m[33mApply property category CATEGORY's properties between START and END.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2888	[37m  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31mcategory[39;49;00m[37m[39;49;00m
  2889	[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mstart2[39;49;00m[37m [39;49;00m[31mstart[39;49;00m))[37m[39;49;00m
  2890	[37m      [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m[31mstart2[39;49;00m[37m [39;49;00m[31mend[39;49;00m)[37m[39;49;00m
  2891	[37m	[39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mend2[39;49;00m[37m     [39;49;00m([32mnext-property-change[39;49;00m[37m [39;49;00m[31mstart2[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mend[39;49;00m))[37m[39;49;00m
  2892	[37m	      [39;49;00m([31moriginal[39;49;00m[37m [39;49;00m([32mtext-properties-at[39;49;00m[37m [39;49;00m[31mstart2[39;49;00m)))[37m[39;49;00m
  2893	[37m	  [39;49;00m([32mset-text-properties[39;49;00m[37m [39;49;00m[31mstart2[39;49;00m[37m [39;49;00m[31mend2[39;49;00m[37m [39;49;00m([32msymbol-plist[39;49;00m[37m [39;49;00m[31mcategory[39;49;00m))[37m[39;49;00m
  2894	[37m	  [39;49;00m([32madd-text-properties[39;49;00m[37m [39;49;00m[31mstart2[39;49;00m[37m [39;49;00m[31mend2[39;49;00m[37m [39;49;00m[31moriginal[39;49;00m)[37m[39;49;00m
  2895	[37m	  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mstart2[39;49;00m[37m [39;49;00m[31mend2[39;49;00m))))))[37m[39;49;00m
  2896	[37m[39;49;00m
  2897	[37m[39;49;00m[37m[39;49;00m
  2898	[37m;;;; Synchronous shell commands.[39;49;00m[37m[39;49;00m
  2899	[37m[39;49;00m
  2900	([36mdefun[39;49;00m[37m [39;49;00m[31mstart-process-shell-command[39;49;00m[37m [39;49;00m([31mname[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31margs[39;49;00m)[37m[39;49;00m
  2901	[37m  [39;49;00m[33m"[39;49;00m[33mStart a program in a subprocess.  Return the process object for it.[39;49;00m
  2902	[33mNAME is name for process.  It is modified if necessary to make it unique.[39;49;00m
  2903	[33mBUFFER is the buffer (or buffer name) to associate with the process.[39;49;00m
  2904	[33m Process output goes at end of that buffer, unless you specify[39;49;00m
  2905	[33m an output stream or filter function to handle the output.[39;49;00m
  2906	[33m BUFFER may be also nil, meaning that this process is not associated[39;49;00m
  2907	[33m with any buffer[39;49;00m
  2908	[33mCOMMAND is the shell command to run.[39;49;00m
  2909	[33m[39;49;00m
  2910	[33mAn old calling convention accepted any number of arguments after COMMAND,[39;49;00m
  2911	[33mwhich were just concatenated to COMMAND.  This is still supported but strongly[39;49;00m
  2912	[33mdiscouraged.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2913	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31madvertised-calling-convention[39;49;00m[37m [39;49;00m([31mname[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m [39;49;00m[31mcommand[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m23.1[39;49;00m[33m"[39;49;00m))[37m[39;49;00m
  2914	[37m  [39;49;00m[37m;; We used to use `exec' to replace the shell with the command,[39;49;00m[37m[39;49;00m
  2915	[37m  [39;49;00m[37m;; but that failed to handle (...) and semicolon, etc.[39;49;00m[37m[39;49;00m
  2916	[37m  [39;49;00m([32mstart-process[39;49;00m[37m [39;49;00m[31mname[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m [39;49;00m[31mshell-file-name[39;49;00m[37m [39;49;00m[31mshell-command-switch[39;49;00m[37m[39;49;00m
  2917	[37m		 [39;49;00m([32mmapconcat[39;49;00m[37m [39;49;00m[33m'identity[39;49;00m[37m [39;49;00m[31margs[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m)))[37m[39;49;00m
  2918	[37m[39;49;00m
  2919	([36mdefun[39;49;00m[37m [39;49;00m[31mstart-file-process-shell-command[39;49;00m[37m [39;49;00m([31mname[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31margs[39;49;00m)[37m[39;49;00m
  2920	[37m  [39;49;00m[33m"[39;49;00m[33mStart a program in a subprocess.  Return the process object for it.[39;49;00m
  2921	[33mSimilar to [39;49;00m[33m`start-process-shell-command'[39;49;00m[33m, but calls [39;49;00m[33m`start-file-process'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2922	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31madvertised-calling-convention[39;49;00m[37m [39;49;00m([31mname[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m [39;49;00m[31mcommand[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m23.1[39;49;00m[33m"[39;49;00m))[37m[39;49;00m
  2923	[37m  [39;49;00m([31mstart-file-process[39;49;00m[37m[39;49;00m
  2924	[37m   [39;49;00m[31mname[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m[39;49;00m
  2925	[37m   [39;49;00m([34mif[39;49;00m[37m [39;49;00m([31mfile-remote-p[39;49;00m[37m [39;49;00m[31mdefault-directory[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m/bin/sh[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mshell-file-name[39;49;00m)[37m[39;49;00m
  2926	[37m   [39;49;00m([34mif[39;49;00m[37m [39;49;00m([31mfile-remote-p[39;49;00m[37m [39;49;00m[31mdefault-directory[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m-c[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mshell-command-switch[39;49;00m)[37m[39;49;00m
  2927	[37m   [39;49;00m([32mmapconcat[39;49;00m[37m [39;49;00m[33m'identity[39;49;00m[37m [39;49;00m[31margs[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m)))[37m[39;49;00m
  2928	[37m[39;49;00m
  2929	([36mdefun[39;49;00m[37m [39;49;00m[31mcall-process-shell-command[39;49;00m[37m [39;49;00m([31mcommand[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31minfile[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m [39;49;00m[31mdisplay[39;49;00m[37m[39;49;00m
  2930	[37m					   [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31margs[39;49;00m)[37m[39;49;00m
  2931	[37m  [39;49;00m[33m"[39;49;00m[33mExecute the shell command COMMAND synchronously in separate process.[39;49;00m
  2932	[33mThe remaining arguments are optional.[39;49;00m
  2933	[33mThe program's input comes from file INFILE (nil means [39;49;00m[33m`/dev/null'[39;49;00m[33m).[39;49;00m
  2934	[33mInsert output in BUFFER before point; t means current buffer;[39;49;00m
  2935	[33m nil for BUFFER means discard it; 0 means discard and don't wait.[39;49;00m
  2936	[33mBUFFER can also have the form (REAL-BUFFER STDERR-FILE); in that case,[39;49;00m
  2937	[33mREAL-BUFFER says what to do with standard output, as above,[39;49;00m
  2938	[33mwhile STDERR-FILE says what to do with standard error in the child.[39;49;00m
  2939	[33mSTDERR-FILE may be nil (discard standard error output),[39;49;00m
  2940	[33mt (mix it with ordinary output), or a file name string.[39;49;00m
  2941	[33m[39;49;00m
  2942	[33mFourth arg DISPLAY non-nil means redisplay buffer as output is inserted.[39;49;00m
  2943	[33mWildcards and redirection are handled as usual in the shell.[39;49;00m
  2944	[33m[39;49;00m
  2945	[33mIf BUFFER is 0, [39;49;00m[33m`call-process-shell-command'[39;49;00m[33m returns immediately with value nil.[39;49;00m
  2946	[33mOtherwise it waits for COMMAND to terminate and returns a numeric exit[39;49;00m
  2947	[33mstatus or a signal description string.[39;49;00m
  2948	[33mIf you quit, the process is killed with SIGINT, or SIGKILL if you quit again.[39;49;00m
  2949	[33m[39;49;00m
  2950	[33mAn old calling convention accepted any number of arguments after DISPLAY,[39;49;00m
  2951	[33mwhich were just concatenated to COMMAND.  This is still supported but strongly[39;49;00m
  2952	[33mdiscouraged.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2953	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31madvertised-calling-convention[39;49;00m[37m[39;49;00m
  2954	[37m            [39;49;00m([31mcommand[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31minfile[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m [39;49;00m[31mdisplay[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m24.5[39;49;00m[33m"[39;49;00m))[37m[39;49;00m
  2955	[37m  [39;49;00m[37m;; We used to use `exec' to replace the shell with the command,[39;49;00m[37m[39;49;00m
  2956	[37m  [39;49;00m[37m;; but that failed to handle (...) and semicolon, etc.[39;49;00m[37m[39;49;00m
  2957	[37m  [39;49;00m([32mcall-process[39;49;00m[37m [39;49;00m[31mshell-file-name[39;49;00m[37m[39;49;00m
  2958	[37m		[39;49;00m[31minfile[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m [39;49;00m[31mdisplay[39;49;00m[37m[39;49;00m
  2959	[37m		[39;49;00m[31mshell-command-switch[39;49;00m[37m[39;49;00m
  2960	[37m		[39;49;00m([32mmapconcat[39;49;00m[37m [39;49;00m[33m'identity[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mcommand[39;49;00m[37m [39;49;00m[31margs[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m)))[37m[39;49;00m
  2961	[37m[39;49;00m
  2962	([36mdefun[39;49;00m[37m [39;49;00m[31mprocess-file-shell-command[39;49;00m[37m [39;49;00m([31mcommand[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31minfile[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m [39;49;00m[31mdisplay[39;49;00m[37m[39;49;00m
  2963	[37m					   [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31margs[39;49;00m)[37m[39;49;00m
  2964	[37m  [39;49;00m[33m"[39;49;00m[33mProcess files synchronously in a separate process.[39;49;00m
  2965	[33mSimilar to [39;49;00m[33m`call-process-shell-command'[39;49;00m[33m, but calls [39;49;00m[33m`process-file'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2966	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31madvertised-calling-convention[39;49;00m[37m[39;49;00m
  2967	[37m            [39;49;00m([31mcommand[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31minfile[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m [39;49;00m[31mdisplay[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m24.5[39;49;00m[33m"[39;49;00m))[37m[39;49;00m
  2968	[37m  [39;49;00m([31mprocess-file[39;49;00m[37m[39;49;00m
  2969	[37m   [39;49;00m([34mif[39;49;00m[37m [39;49;00m([31mfile-remote-p[39;49;00m[37m [39;49;00m[31mdefault-directory[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m/bin/sh[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mshell-file-name[39;49;00m)[37m[39;49;00m
  2970	[37m   [39;49;00m[31minfile[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m [39;49;00m[31mdisplay[39;49;00m[37m[39;49;00m
  2971	[37m   [39;49;00m([34mif[39;49;00m[37m [39;49;00m([31mfile-remote-p[39;49;00m[37m [39;49;00m[31mdefault-directory[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m-c[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mshell-command-switch[39;49;00m)[37m[39;49;00m
  2972	[37m   [39;49;00m([32mmapconcat[39;49;00m[37m [39;49;00m[33m'identity[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mcommand[39;49;00m[37m [39;49;00m[31margs[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m)))[37m[39;49;00m
  2973	[37m[39;49;00m[37m[39;49;00m
  2974	[37m;;;; Lisp macros to do various things temporarily.[39;49;00m[37m[39;49;00m
  2975	[37m[39;49;00m
  2976	([36mdefmacro[39;49;00m[37m [39;49;00m[36mtrack-mouse[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m
  2977	[37m  [39;49;00m[33m"[39;49;00m[33mEvaluate BODY with mouse movement events enabled.[39;49;00m
  2978	[33mWithin a [39;49;00m[33m`track-mouse'[39;49;00m[33m form, mouse motion generates input events that[39;49;00m
  2979	[33m you can read with [39;49;00m[33m`read-event'[39;49;00m[33m.[39;49;00m
  2980	[33mNormally, mouse motion is ignored.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2981	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m
  2982	[37m  [39;49;00m`([32minternal--track-mouse[39;49;00m[37m [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m()[37m [39;49;00m,@[31mbody[39;49;00m)))[37m[39;49;00m
  2983	[37m[39;49;00m
  2984	([36mdefmacro[39;49;00m[37m [39;49;00m[36mwith-current-buffer[39;49;00m[37m [39;49;00m([31mbuffer-or-name[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m
  2985	[37m  [39;49;00m[33m"[39;49;00m[33mExecute the forms in BODY with BUFFER-OR-NAME temporarily current.[39;49;00m
  2986	[33mBUFFER-OR-NAME must be a buffer or the name of an existing buffer.[39;49;00m
  2987	[33mThe value returned is the value of the last form in BODY.  See[39;49;00m
  2988	[33malso [39;49;00m[33m`with-temp-buffer'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  2989	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m
  2990	[37m  [39;49;00m`([34msave-current-buffer[39;49;00m[37m[39;49;00m
  2991	[37m     [39;49;00m([32mset-buffer[39;49;00m[37m [39;49;00m,[31mbuffer-or-name[39;49;00m)[37m[39;49;00m
  2992	[37m     [39;49;00m,@[31mbody[39;49;00m))[37m[39;49;00m
  2993	[37m[39;49;00m
  2994	([36mdefun[39;49;00m[37m [39;49;00m[31minternal--before-with-selected-window[39;49;00m[37m [39;49;00m([31mwindow[39;49;00m)[37m[39;49;00m
  2995	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mother-frame[39;49;00m[37m [39;49;00m([32mwindow-frame[39;49;00m[37m [39;49;00m[31mwindow[39;49;00m)))[37m[39;49;00m
  2996	[37m    [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[31mwindow[39;49;00m[37m [39;49;00m([32mselected-window[39;49;00m)[37m[39;49;00m
  2997	[37m          [39;49;00m[37m;; Selecting a window on another frame also changes that[39;49;00m[37m[39;49;00m
  2998	[37m          [39;49;00m[37m;; frame's frame-selected-window.  We must save&restore it.[39;49;00m[37m[39;49;00m
  2999	[37m          [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mselected-frame[39;49;00m)[37m [39;49;00m[31mother-frame[39;49;00m)[37m[39;49;00m
  3000	[37m            [39;49;00m([32mframe-selected-window[39;49;00m[37m [39;49;00m[31mother-frame[39;49;00m))[37m[39;49;00m
  3001	[37m          [39;49;00m[37m;; Also remember the top-frame if on ttys.[39;49;00m[37m[39;49;00m
  3002	[37m          [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mselected-frame[39;49;00m)[37m [39;49;00m[31mother-frame[39;49;00m)[37m[39;49;00m
  3003	[37m            [39;49;00m([32mtty-top-frame[39;49;00m[37m [39;49;00m[31mother-frame[39;49;00m)))))[37m[39;49;00m
  3004	[37m[39;49;00m
  3005	([36mdefun[39;49;00m[37m [39;49;00m[31minternal--after-with-selected-window[39;49;00m[37m [39;49;00m([31mstate[39;49;00m)[37m[39;49;00m
  3006	[37m  [39;49;00m[37m;; First reset frame-selected-window.[39;49;00m[37m[39;49;00m
  3007	[37m  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mwindow-live-p[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m[31mstate[39;49;00m))[37m[39;49;00m
  3008	[37m    [39;49;00m[37m;; We don't use set-frame-selected-window because it does not[39;49;00m[37m[39;49;00m
  3009	[37m    [39;49;00m[37m;; pass the `norecord' argument to Fselect_window.[39;49;00m[37m[39;49;00m
  3010	[37m    [39;49;00m([32mselect-window[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m[31mstate[39;49;00m)[37m [39;49;00m[33m'norecord[39;49;00m)[37m[39;49;00m
  3011	[37m    [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mframe-live-p[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m3[39;49;00m[37m [39;49;00m[31mstate[39;49;00m))[37m[39;49;00m
  3012	[37m         [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mtty-top-frame[39;49;00m)[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m3[39;49;00m[37m [39;49;00m[31mstate[39;49;00m)))[37m[39;49;00m
  3013	[37m         [39;49;00m([32mselect-frame[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m3[39;49;00m[37m [39;49;00m[31mstate[39;49;00m)[37m [39;49;00m[33m'norecord[39;49;00m)))[37m[39;49;00m
  3014	[37m  [39;49;00m[37m;; Then reset the actual selected-window.[39;49;00m[37m[39;49;00m
  3015	[37m  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mwindow-live-p[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mstate[39;49;00m))[37m[39;49;00m
  3016	[37m    [39;49;00m([32mselect-window[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mstate[39;49;00m)[37m [39;49;00m[33m'norecord[39;49;00m)))[37m[39;49;00m
  3017	[37m[39;49;00m
  3018	([36mdefmacro[39;49;00m[37m [39;49;00m[36mwith-selected-window[39;49;00m[37m [39;49;00m([31mwindow[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m
  3019	[37m  [39;49;00m[33m"[39;49;00m[33mExecute the forms in BODY with WINDOW as the selected window.[39;49;00m
  3020	[33mThe value returned is the value of the last form in BODY.[39;49;00m
  3021	[33m[39;49;00m
  3022	[33mThis macro saves and restores the selected window, as well as the[39;49;00m
  3023	[33mselected window of each frame.  It does not change the order of[39;49;00m
  3024	[33mrecently selected windows.  If the previously selected window of[39;49;00m
  3025	[33msome frame is no longer live at the end of BODY, that frame's[39;49;00m
  3026	[33mselected window is left alone.  If the selected window is no[39;49;00m
  3027	[33mlonger live, then whatever window is selected at the end of BODY[39;49;00m
  3028	[33mremains selected.[39;49;00m
  3029	[33m[39;49;00m
  3030	[33mThis macro uses [39;49;00m[33m`save-current-buffer'[39;49;00m[33m to save and restore the[39;49;00m
  3031	[33mcurrent buffer, since otherwise its normal operation could[39;49;00m
  3032	[33mpotentially make a different buffer current.  It does not alter[39;49;00m
  3033	[33mthe buffer list ordering.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3034	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m
  3035	[37m  [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m(([31msave-selected-window--state[39;49;00m[37m[39;49;00m
  3036	[37m          [39;49;00m([31minternal--before-with-selected-window[39;49;00m[37m [39;49;00m,[31mwindow[39;49;00m)))[37m[39;49;00m
  3037	[37m     [39;49;00m([34msave-current-buffer[39;49;00m[37m[39;49;00m
  3038	[37m       [39;49;00m([34munwind-protect[39;49;00m[37m[39;49;00m
  3039	[37m           [39;49;00m([34mprogn[39;49;00m[37m [39;49;00m([32mselect-window[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31msave-selected-window--state[39;49;00m)[37m [39;49;00m[33m'norecord[39;49;00m)[37m[39;49;00m
  3040	[37m		  [39;49;00m,@[31mbody[39;49;00m)[37m[39;49;00m
  3041	[37m         [39;49;00m([31minternal--after-with-selected-window[39;49;00m[37m [39;49;00m[31msave-selected-window--state[39;49;00m)))))[37m[39;49;00m
  3042	[37m[39;49;00m
  3043	([36mdefmacro[39;49;00m[37m [39;49;00m[36mwith-selected-frame[39;49;00m[37m [39;49;00m([31mframe[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m
  3044	[37m  [39;49;00m[33m"[39;49;00m[33mExecute the forms in BODY with FRAME as the selected frame.[39;49;00m
  3045	[33mThe value returned is the value of the last form in BODY.[39;49;00m
  3046	[33m[39;49;00m
  3047	[33mThis macro saves and restores the selected frame, and changes the[39;49;00m
  3048	[33morder of neither the recently selected windows nor the buffers in[39;49;00m
  3049	[33mthe buffer list.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3050	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m
  3051	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mold-frame[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mold-frame[39;49;00m[33m"[39;49;00m))[37m[39;49;00m
  3052	[37m	[39;49;00m([31mold-buffer[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mold-buffer[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m
  3053	[37m    [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m((,[31mold-frame[39;49;00m[37m [39;49;00m([32mselected-frame[39;49;00m))[37m[39;49;00m
  3054	[37m	   [39;49;00m(,[31mold-buffer[39;49;00m[37m [39;49;00m([32mcurrent-buffer[39;49;00m)))[37m[39;49;00m
  3055	[37m       [39;49;00m([34munwind-protect[39;49;00m[37m[39;49;00m
  3056	[37m	   [39;49;00m([34mprogn[39;49;00m[37m [39;49;00m([32mselect-frame[39;49;00m[37m [39;49;00m,[31mframe[39;49;00m[37m [39;49;00m[33m'norecord[39;49;00m)[37m[39;49;00m
  3057	[37m		  [39;49;00m,@[31mbody[39;49;00m)[37m[39;49;00m
  3058	[37m	 [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mframe-live-p[39;49;00m[37m [39;49;00m,[31mold-frame[39;49;00m)[37m[39;49;00m
  3059	[37m	   [39;49;00m([32mselect-frame[39;49;00m[37m [39;49;00m,[31mold-frame[39;49;00m[37m [39;49;00m[33m'norecord[39;49;00m))[37m[39;49;00m
  3060	[37m	 [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mbuffer-live-p[39;49;00m[37m [39;49;00m,[31mold-buffer[39;49;00m)[37m[39;49;00m
  3061	[37m	   [39;49;00m([32mset-buffer[39;49;00m[37m [39;49;00m,[31mold-buffer[39;49;00m))))))[37m[39;49;00m
  3062	[37m[39;49;00m
  3063	([36mdefmacro[39;49;00m[37m [39;49;00m[36msave-window-excursion[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m
  3064	[37m  [39;49;00m[33m"[39;49;00m[33mExecute BODY, then restore previous window configuration.[39;49;00m
  3065	[33mThis macro saves the window configuration on the selected frame,[39;49;00m
  3066	[33mexecutes BODY, then calls [39;49;00m[33m`set-window-configuration'[39;49;00m[33m to restore[39;49;00m
  3067	[33mthe saved window configuration.  The return value is the last[39;49;00m
  3068	[33mform in BODY.  The window configuration is also restored if BODY[39;49;00m
  3069	[33mexits nonlocally.[39;49;00m
  3070	[33m[39;49;00m
  3071	[33mBEWARE: Most uses of this macro introduce bugs.[39;49;00m
  3072	[33mE.g. it should not be used to try and prevent some code from opening[39;49;00m
  3073	[33ma new window, since that window may sometimes appear in another frame,[39;49;00m
  3074	[33min which case [39;49;00m[33m`save-window-excursion'[39;49;00m[33m cannot help.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3075	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m
  3076	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mc[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mwconfig[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m
  3077	[37m    [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m((,[31mc[39;49;00m[37m [39;49;00m([32mcurrent-window-configuration[39;49;00m)))[37m[39;49;00m
  3078	[37m       [39;49;00m([34munwind-protect[39;49;00m[37m [39;49;00m([34mprogn[39;49;00m[37m [39;49;00m,@[31mbody[39;49;00m)[37m[39;49;00m
  3079	[37m         [39;49;00m([32mset-window-configuration[39;49;00m[37m [39;49;00m,[31mc[39;49;00m)))))[37m[39;49;00m
  3080	[37m[39;49;00m
  3081	([36mdefun[39;49;00m[37m [39;49;00m[31minternal-temp-output-buffer-show[39;49;00m[37m [39;49;00m([31mbuffer[39;49;00m)[37m[39;49;00m
  3082	[37m  [39;49;00m[33m"[39;49;00m[33mInternal function for [39;49;00m[33m`with-output-to-temp-buffer'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3083	[37m  [39;49;00m([36mwith-current-buffer[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m[39;49;00m
  3084	[37m    [39;49;00m([32mset-buffer-modified-p[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m
  3085	[37m    [39;49;00m([32mgoto-char[39;49;00m[37m [39;49;00m([32mpoint-min[39;49;00m)))[37m[39;49;00m
  3086	[37m[39;49;00m
  3087	[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mtemp-buffer-show-function[39;49;00m[37m[39;49;00m
  3088	[37m      [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mtemp-buffer-show-function[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m)[37m[39;49;00m
  3089	[37m    [39;49;00m([36mwith-current-buffer[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m[39;49;00m
  3090	[37m      [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mwindow[39;49;00m[37m[39;49;00m
  3091	[37m	      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([32mwindow-combination-limit[39;49;00m[37m[39;49;00m
  3092	[37m		   [39;49;00m[37m;; When `window-combination-limit' equals[39;49;00m[37m[39;49;00m
  3093	[37m		   [39;49;00m[37m;; `temp-buffer' or `temp-buffer-resize' and[39;49;00m[37m[39;49;00m
  3094	[37m		   [39;49;00m[37m;; `temp-buffer-resize-mode' is enabled in this[39;49;00m[37m[39;49;00m
  3095	[37m		   [39;49;00m[37m;; buffer bind it to t so resizing steals space[39;49;00m[37m[39;49;00m
  3096	[37m		   [39;49;00m[37m;; preferably from the window that was split.[39;49;00m[37m[39;49;00m
  3097	[37m		   [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[32mwindow-combination-limit[39;49;00m[37m [39;49;00m[33m'temp-buffer[39;49;00m)[37m[39;49;00m
  3098	[37m			   [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[32mwindow-combination-limit[39;49;00m[37m[39;49;00m
  3099	[37m				    [39;49;00m[33m'temp-buffer-resize[39;49;00m)[37m[39;49;00m
  3100	[37m				[39;49;00m[31mtemp-buffer-resize-mode[39;49;00m))[37m[39;49;00m
  3101	[37m		       [39;49;00m[31mt[39;49;00m[37m[39;49;00m
  3102	[37m		     [39;49;00m[32mwindow-combination-limit[39;49;00m)))[37m[39;49;00m
  3103	[37m		[39;49;00m([31mdisplay-buffer[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m)))[37m[39;49;00m
  3104	[37m	     [39;49;00m([31mframe[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mwindow[39;49;00m[37m [39;49;00m([32mwindow-frame[39;49;00m[37m [39;49;00m[31mwindow[39;49;00m))))[37m[39;49;00m
  3105	[37m	[39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31mwindow[39;49;00m[37m[39;49;00m
  3106	[37m	  [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mframe[39;49;00m[37m [39;49;00m([32mselected-frame[39;49;00m))[37m[39;49;00m
  3107	[37m	    [39;49;00m([32mmake-frame-visible[39;49;00m[37m [39;49;00m[31mframe[39;49;00m))[37m[39;49;00m
  3108	[37m	  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mminibuffer-scroll-window[39;49;00m[37m [39;49;00m[31mwindow[39;49;00m)[37m[39;49;00m
  3109	[37m	  [39;49;00m([32mset-window-hscroll[39;49;00m[37m [39;49;00m[31mwindow[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m
  3110	[37m	  [39;49;00m[37m;; Don't try this with NOFORCE non-nil![39;49;00m[37m[39;49;00m
  3111	[37m	  [39;49;00m([32mset-window-start[39;49;00m[37m [39;49;00m[31mwindow[39;49;00m[37m [39;49;00m([32mpoint-min[39;49;00m)[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m
  3112	[37m	  [39;49;00m[37m;; This should not be necessary.[39;49;00m[37m[39;49;00m
  3113	[37m	  [39;49;00m([32mset-window-point[39;49;00m[37m [39;49;00m[31mwindow[39;49;00m[37m [39;49;00m([32mpoint-min[39;49;00m))[37m[39;49;00m
  3114	[37m	  [39;49;00m[37m;; Run `temp-buffer-show-hook', with the chosen window selected.[39;49;00m[37m[39;49;00m
  3115	[37m	  [39;49;00m([36mwith-selected-window[39;49;00m[37m [39;49;00m[31mwindow[39;49;00m[37m[39;49;00m
  3116	[37m	    [39;49;00m([32mrun-hooks[39;49;00m[37m [39;49;00m[33m'temp-buffer-show-hook[39;49;00m))))))[37m[39;49;00m
  3117	[37m  [39;49;00m[37m;; Return nil.[39;49;00m[37m[39;49;00m
  3118	[37m  [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m
  3119	[37m[39;49;00m
  3120	[37m;; Doc is very similar to with-temp-buffer-window.[39;49;00m[37m[39;49;00m
  3121	([36mdefmacro[39;49;00m[37m [39;49;00m[36mwith-output-to-temp-buffer[39;49;00m[37m [39;49;00m([31mbufname[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m
  3122	[37m  [39;49;00m[33m"[39;49;00m[33mBind [39;49;00m[33m`standard-output'[39;49;00m[33m to buffer BUFNAME, eval BODY, then show that buffer.[39;49;00m
  3123	[33m[39;49;00m
  3124	[33mThis construct makes buffer BUFNAME empty before running BODY.[39;49;00m
  3125	[33mIt does not make the buffer current for BODY.[39;49;00m
  3126	[33mInstead it binds [39;49;00m[33m`standard-output'[39;49;00m[33m to that buffer, so that output[39;49;00m
  3127	[33mgenerated with [39;49;00m[33m`prin1'[39;49;00m[33m and similar functions in BODY goes into[39;49;00m
  3128	[33mthe buffer.[39;49;00m
  3129	[33m[39;49;00m
  3130	[33mAt the end of BODY, this marks buffer BUFNAME unmodified and displays[39;49;00m
  3131	[33mit in a window, but does not select it.  The normal way to do this is[39;49;00m
  3132	[33mby calling [39;49;00m[33m`display-buffer'[39;49;00m[33m, then running [39;49;00m[33m`temp-buffer-show-hook'[39;49;00m[33m.[39;49;00m
  3133	[33mHowever, if [39;49;00m[33m`temp-buffer-show-function'[39;49;00m[33m is non-nil, it calls that[39;49;00m
  3134	[33mfunction instead (and does not run [39;49;00m[33m`temp-buffer-show-hook'[39;49;00m[33m).  The[39;49;00m
  3135	[33mfunction gets one argument, the buffer to display.[39;49;00m
  3136	[33m[39;49;00m
  3137	[33mThe return value of [39;49;00m[33m`with-output-to-temp-buffer'[39;49;00m[33m is the value of the[39;49;00m
  3138	[33mlast form in BODY.  If BODY does not finish normally, the buffer[39;49;00m
  3139	[33mBUFNAME is not displayed.[39;49;00m
  3140	[33m[39;49;00m
  3141	[33mThis runs the hook [39;49;00m[33m`temp-buffer-setup-hook'[39;49;00m[33m before BODY,[39;49;00m
  3142	[33mwith the buffer BUFNAME temporarily current.  It runs the hook[39;49;00m
  3143	[33m`temp-buffer-show-hook'[39;49;00m[33m after displaying buffer BUFNAME, with that[39;49;00m
  3144	[33mbuffer temporarily current, and the window that was used to display it[39;49;00m
  3145	[33mtemporarily selected.  But it doesn't run [39;49;00m[33m`temp-buffer-show-hook'[39;49;00m[33m[39;49;00m
  3146	[33mif it uses [39;49;00m[33m`temp-buffer-show-function'[39;49;00m[33m.[39;49;00m
  3147	[33m[39;49;00m
  3148	[33mBy default, the setup hook puts the buffer into Help mode before running BODY.[39;49;00m
  3149	[33mIf BODY does not change the major mode, the show hook makes the buffer[39;49;00m
  3150	[33mread-only, and scans it for function and variable names to make them into[39;49;00m
  3151	[33mclickable cross-references.[39;49;00m
  3152	[33m[39;49;00m
  3153	[33mSee the related form [39;49;00m[33m`with-temp-buffer-window'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3154	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m
  3155	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mold-dir[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mold-dir[39;49;00m[33m"[39;49;00m))[37m[39;49;00m
  3156	[37m        [39;49;00m([31mbuf[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mbuf[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m
  3157	[37m    [39;49;00m`([34mlet*[39;49;00m[37m [39;49;00m((,[31mold-dir[39;49;00m[37m [39;49;00m[31mdefault-directory[39;49;00m)[37m[39;49;00m
  3158	[37m            [39;49;00m(,[31mbuf[39;49;00m[37m[39;49;00m
  3159	[37m             [39;49;00m([36mwith-current-buffer[39;49;00m[37m [39;49;00m([32mget-buffer-create[39;49;00m[37m [39;49;00m,[31mbufname[39;49;00m)[37m[39;49;00m
  3160	[37m               [39;49;00m([34mprog1[39;49;00m[37m [39;49;00m([32mcurrent-buffer[39;49;00m)[37m[39;49;00m
  3161	[37m                 [39;49;00m([32mkill-all-local-variables[39;49;00m)[37m[39;49;00m
  3162	[37m                 [39;49;00m[37m;; FIXME: delete_all_overlays[39;49;00m[37m[39;49;00m
  3163	[37m                 [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mdefault-directory[39;49;00m[37m [39;49;00m,[31mold-dir[39;49;00m)[37m[39;49;00m
  3164	[37m                 [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbuffer-read-only[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m
  3165	[37m                 [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[32mbuffer-file-name[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m
  3166	[37m                 [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbuffer-undo-list[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m
  3167	[37m                 [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31minhibit-read-only[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m
  3168	[37m                       [39;49;00m([31minhibit-modification-hooks[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m
  3169	[37m                   [39;49;00m([32merase-buffer[39;49;00m)[37m[39;49;00m
  3170	[37m                   [39;49;00m([32mrun-hooks[39;49;00m[37m [39;49;00m[33m'temp-buffer-setup-hook[39;49;00m)))))[37m[39;49;00m
  3171	[37m            [39;49;00m([31mstandard-output[39;49;00m[37m [39;49;00m,[31mbuf[39;49;00m))[37m[39;49;00m
  3172	[37m       [39;49;00m([34mprog1[39;49;00m[37m [39;49;00m([34mprogn[39;49;00m[37m [39;49;00m,@[31mbody[39;49;00m)[37m[39;49;00m
  3173	[37m         [39;49;00m([31minternal-temp-output-buffer-show[39;49;00m[37m [39;49;00m,[31mbuf[39;49;00m)))))[37m[39;49;00m
  3174	[37m[39;49;00m
  3175	([36mdefmacro[39;49;00m[37m [39;49;00m[36mwith-temp-file[39;49;00m[37m [39;49;00m([31mfile[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m
  3176	[37m  [39;49;00m[33m"[39;49;00m[33mCreate a new buffer, evaluate BODY there, and write the buffer to FILE.[39;49;00m
  3177	[33mThe value returned is the value of the last form in BODY.[39;49;00m
  3178	[33mSee also [39;49;00m[33m`with-temp-buffer'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3179	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m
  3180	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtemp-file[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mtemp-file[39;49;00m[33m"[39;49;00m))[37m[39;49;00m
  3181	[37m	[39;49;00m([31mtemp-buffer[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mtemp-buffer[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m
  3182	[37m    [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m((,[31mtemp-file[39;49;00m[37m [39;49;00m,[31mfile[39;49;00m)[37m[39;49;00m
  3183	[37m	   [39;49;00m(,[31mtemp-buffer[39;49;00m[37m[39;49;00m
  3184	[37m	    [39;49;00m([32mget-buffer-create[39;49;00m[37m [39;49;00m([32mgenerate-new-buffer-name[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m *temp file*[39;49;00m[33m"[39;49;00m))))[37m[39;49;00m
  3185	[37m       [39;49;00m([34munwind-protect[39;49;00m[37m[39;49;00m
  3186	[37m	   [39;49;00m([34mprog1[39;49;00m[37m[39;49;00m
  3187	[37m	       [39;49;00m([36mwith-current-buffer[39;49;00m[37m [39;49;00m,[31mtemp-buffer[39;49;00m[37m[39;49;00m
  3188	[37m		 [39;49;00m,@[31mbody[39;49;00m)[37m[39;49;00m
  3189	[37m	     [39;49;00m([36mwith-current-buffer[39;49;00m[37m [39;49;00m,[31mtemp-buffer[39;49;00m[37m[39;49;00m
  3190	[37m	       [39;49;00m([32mwrite-region[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m,[31mtemp-file[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[34m0[39;49;00m)))[37m[39;49;00m
  3191	[37m	 [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mbuffer-name[39;49;00m[37m [39;49;00m,[31mtemp-buffer[39;49;00m)[37m[39;49;00m
  3192	[37m	      [39;49;00m([32mkill-buffer[39;49;00m[37m [39;49;00m,[31mtemp-buffer[39;49;00m))))))[37m[39;49;00m
  3193	[37m[39;49;00m
  3194	([36mdefmacro[39;49;00m[37m [39;49;00m[36mwith-temp-message[39;49;00m[37m [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m
  3195	[37m  [39;49;00m[33m"[39;49;00m[33mDisplay MESSAGE temporarily if non-nil while BODY is evaluated.[39;49;00m
  3196	[33mThe original message is restored to the echo area after BODY has finished.[39;49;00m
  3197	[33mThe value returned is the value of the last form in BODY.[39;49;00m
  3198	[33mMESSAGE is written to the message log buffer if [39;49;00m[33m`message-log-max'[39;49;00m[33m is non-nil.[39;49;00m
  3199	[33mIf MESSAGE is nil, the echo area and message log buffer are unchanged.[39;49;00m
  3200	[33mUse a MESSAGE of [39;49;00m[33m\"[39;49;00m[33m\"[39;49;00m[33m to temporarily clear the echo area.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3201	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m1[39;49;00m))[37m[39;49;00m
  3202	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([32mcurrent-message[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mcurrent-message[39;49;00m[33m"[39;49;00m))[37m[39;49;00m
  3203	[37m	[39;49;00m([31mtemp-message[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mwith-temp-message[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m
  3204	[37m    [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m((,[31mtemp-message[39;49;00m[37m [39;49;00m,[32mmessage[39;49;00m)[37m[39;49;00m
  3205	[37m	   [39;49;00m(,[32mcurrent-message[39;49;00m))[37m[39;49;00m
  3206	[37m       [39;49;00m([34munwind-protect[39;49;00m[37m[39;49;00m
  3207	[37m	   [39;49;00m([34mprogn[39;49;00m[37m[39;49;00m
  3208	[37m	     [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m,[31mtemp-message[39;49;00m[37m[39;49;00m
  3209	[37m	       [39;49;00m([34msetq[39;49;00m[37m [39;49;00m,[32mcurrent-message[39;49;00m[37m [39;49;00m([32mcurrent-message[39;49;00m))[37m[39;49;00m
  3210	[37m	       [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m%s[39;49;00m[33m"[39;49;00m[37m [39;49;00m,[31mtemp-message[39;49;00m))[37m[39;49;00m
  3211	[37m	     [39;49;00m,@[31mbody[39;49;00m)[37m[39;49;00m
  3212	[37m	 [39;49;00m([34mand[39;49;00m[37m [39;49;00m,[31mtemp-message[39;49;00m[37m[39;49;00m
  3213	[37m	      [39;49;00m([34mif[39;49;00m[37m [39;49;00m,[32mcurrent-message[39;49;00m[37m[39;49;00m
  3214	[37m		  [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m%s[39;49;00m[33m"[39;49;00m[37m [39;49;00m,[32mcurrent-message[39;49;00m)[37m[39;49;00m
  3215	[37m		[39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)))))))[37m[39;49;00m
  3216	[37m[39;49;00m
  3217	([36mdefmacro[39;49;00m[37m [39;49;00m[36mwith-temp-buffer[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m
  3218	[37m  [39;49;00m[33m"[39;49;00m[33mCreate a temporary buffer, and evaluate BODY there like [39;49;00m[33m`progn'[39;49;00m[33m.[39;49;00m
  3219	[33mSee also [39;49;00m[33m`with-temp-file'[39;49;00m[33m and [39;49;00m[33m`with-output-to-string'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3220	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m
  3221	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtemp-buffer[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mtemp-buffer[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m
  3222	[37m    [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m((,[31mtemp-buffer[39;49;00m[37m [39;49;00m([31mgenerate-new-buffer[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m *temp*[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m
  3223	[37m       [39;49;00m[37m;; FIXME: kill-buffer can change current-buffer in some odd cases.[39;49;00m[37m[39;49;00m
  3224	[37m       [39;49;00m([36mwith-current-buffer[39;49;00m[37m [39;49;00m,[31mtemp-buffer[39;49;00m[37m[39;49;00m
  3225	[37m         [39;49;00m([34munwind-protect[39;49;00m[37m[39;49;00m
  3226	[37m	     [39;49;00m([34mprogn[39;49;00m[37m [39;49;00m,@[31mbody[39;49;00m)[37m[39;49;00m
  3227	[37m           [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mbuffer-name[39;49;00m[37m [39;49;00m,[31mtemp-buffer[39;49;00m)[37m[39;49;00m
  3228	[37m                [39;49;00m([32mkill-buffer[39;49;00m[37m [39;49;00m,[31mtemp-buffer[39;49;00m)))))))[37m[39;49;00m
  3229	[37m[39;49;00m
  3230	([36mdefmacro[39;49;00m[37m [39;49;00m[36mwith-silent-modifications[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m
  3231	[37m  [39;49;00m[33m"[39;49;00m[33mExecute BODY, pretending it does not modify the buffer.[39;49;00m
  3232	[33mIf BODY performs real modifications to the buffer's text, other[39;49;00m
  3233	[33mthan cosmetic ones, undo data may become corrupted.[39;49;00m
  3234	[33m[39;49;00m
  3235	[33mThis macro will run BODY normally, but doesn't count its buffer[39;49;00m
  3236	[33mmodifications as being buffer modifications.  This affects things[39;49;00m
  3237	[33mlike [39;49;00m[33m`buffer-modified-p'[39;49;00m[33m, checking whether the file is locked by[39;49;00m
  3238	[33msomeone else, running buffer modification hooks, and other things[39;49;00m
  3239	[33mof that nature.[39;49;00m
  3240	[33m[39;49;00m
  3241	[33mTypically used around modifications of text-properties which do[39;49;00m
  3242	[33mnot really affect the buffer's content.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3243	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m
  3244	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mmodified[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mmodified[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m
  3245	[37m    [39;49;00m`([34mlet*[39;49;00m[37m [39;49;00m((,[31mmodified[39;49;00m[37m [39;49;00m([32mbuffer-modified-p[39;49;00m))[37m[39;49;00m
  3246	[37m            [39;49;00m([31mbuffer-undo-list[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m
  3247	[37m            [39;49;00m([31minhibit-read-only[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m
  3248	[37m            [39;49;00m([31minhibit-modification-hooks[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m
  3249	[37m       [39;49;00m([34munwind-protect[39;49;00m[37m[39;49;00m
  3250	[37m           [39;49;00m([34mprogn[39;49;00m[37m[39;49;00m
  3251	[37m             [39;49;00m,@[31mbody[39;49;00m)[37m[39;49;00m
  3252	[37m         [39;49;00m([36munless[39;49;00m[37m [39;49;00m,[31mmodified[39;49;00m[37m[39;49;00m
  3253	[37m           [39;49;00m([32mrestore-buffer-modified-p[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))))))[37m[39;49;00m
  3254	[37m[39;49;00m
  3255	([36mdefmacro[39;49;00m[37m [39;49;00m[36mwith-output-to-string[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m
  3256	[37m  [39;49;00m[33m"[39;49;00m[33mExecute BODY, return the text it sent to [39;49;00m[33m`standard-output'[39;49;00m[33m, as a string.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3257	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m
  3258	[37m  [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m(([31mstandard-output[39;49;00m[37m[39;49;00m
  3259	[37m	  [39;49;00m([32mget-buffer-create[39;49;00m[37m [39;49;00m([32mgenerate-new-buffer-name[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m *string-output*[39;49;00m[33m"[39;49;00m))))[37m[39;49;00m
  3260	[37m     [39;49;00m([34munwind-protect[39;49;00m[37m[39;49;00m
  3261	[37m	 [39;49;00m([34mprogn[39;49;00m[37m[39;49;00m
  3262	[37m	   [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mstandard-output[39;49;00m[37m [39;49;00m[31mstandard-output[39;49;00m))[37m[39;49;00m
  3263	[37m	     [39;49;00m,@[31mbody[39;49;00m)[37m[39;49;00m
  3264	[37m	   [39;49;00m([36mwith-current-buffer[39;49;00m[37m [39;49;00m[31mstandard-output[39;49;00m[37m[39;49;00m
  3265	[37m	     [39;49;00m([32mbuffer-string[39;49;00m)))[37m[39;49;00m
  3266	[37m       [39;49;00m([32mkill-buffer[39;49;00m[37m [39;49;00m[31mstandard-output[39;49;00m))))[37m[39;49;00m
  3267	[37m[39;49;00m
  3268	([36mdefmacro[39;49;00m[37m [39;49;00m[36mwith-local-quit[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m
  3269	[37m  [39;49;00m[33m"[39;49;00m[33mExecute BODY, allowing quits to terminate BODY but not escape further.[39;49;00m
  3270	[33mWhen a quit terminates BODY, [39;49;00m[33m`with-local-quit'[39;49;00m[33m returns nil but[39;49;00m
  3271	[33mrequests another quit.  That quit will be processed as soon as quitting[39;49;00m
  3272	[33mis allowed once again.  (Immediately, if [39;49;00m[33m`inhibit-quit'[39;49;00m[33m is nil.)[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3273	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m
  3274	[37m  [39;49;00m`([34mcondition-case[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m
  3275	[37m       [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31minhibit-quit[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m
  3276	[37m	 [39;49;00m,@[31mbody[39;49;00m)[37m[39;49;00m
  3277	[37m     [39;49;00m([31mquit[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mquit-flag[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m
  3278	[37m	   [39;49;00m[37m;; This call is to give a chance to handle quit-flag[39;49;00m[37m[39;49;00m
  3279	[37m	   [39;49;00m[37m;; in case inhibit-quit is nil.[39;49;00m[37m[39;49;00m
  3280	[37m	   [39;49;00m[37m;; Without this, it will not be handled until the next function[39;49;00m[37m[39;49;00m
  3281	[37m	   [39;49;00m[37m;; call, and that might allow it to exit thru a condition-case[39;49;00m[37m[39;49;00m
  3282	[37m	   [39;49;00m[37m;; that intends to handle the quit signal next time.[39;49;00m[37m[39;49;00m
  3283	[37m	   [39;49;00m([32meval[39;49;00m[37m [39;49;00m'([31mignore[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)))))[37m[39;49;00m
  3284	[37m[39;49;00m
  3285	([36mdefmacro[39;49;00m[37m [39;49;00m[36mwhile-no-input[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m
  3286	[37m  [39;49;00m[33m"[39;49;00m[33mExecute BODY only as long as there's no pending input.[39;49;00m
  3287	[33mIf input arrives, that ends the execution of BODY,[39;49;00m
  3288	[33mand [39;49;00m[33m`while-no-input'[39;49;00m[33m returns t.  Quitting makes it return nil.[39;49;00m
  3289	[33mIf BODY finishes, [39;49;00m[33m`while-no-input'[39;49;00m[33m returns whatever value BODY produced.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3290	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m
  3291	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mcatch-sym[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33minput[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m
  3292	[37m    [39;49;00m`([36mwith-local-quit[39;49;00m[37m[39;49;00m
  3293	[37m       [39;49;00m([34mcatch[39;49;00m[37m [39;49;00m[33m',catch-sym[39;49;00m[37m[39;49;00m
  3294	[37m	 [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mthrow-on-input[39;49;00m[37m [39;49;00m[33m',catch-sym[39;49;00m))[37m[39;49;00m
  3295	[37m	   [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32minput-pending-p[39;49;00m)[37m[39;49;00m
  3296	[37m	       [39;49;00m([34mprogn[39;49;00m[37m [39;49;00m,@[31mbody[39;49;00m)))))))[37m[39;49;00m
  3297	[37m[39;49;00m
  3298	([36mdefmacro[39;49;00m[37m [39;49;00m[36mcondition-case-unless-debug[39;49;00m[37m [39;49;00m([31mvar[39;49;00m[37m [39;49;00m[31mbodyform[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mhandlers[39;49;00m)[37m[39;49;00m
  3299	[37m  [39;49;00m[33m"[39;49;00m[33mLike [39;49;00m[33m`condition-case'[39;49;00m[33m except that it does not prevent debugging.[39;49;00m
  3300	[33mMore specifically if [39;49;00m[33m`debug-on-error'[39;49;00m[33m is set then the debugger will be invoked[39;49;00m
  3301	[33meven if this catches the signal.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3302	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[34mcondition-case[39;49;00m)[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m2[39;49;00m))[37m[39;49;00m
  3303	[37m  [39;49;00m`([34mcondition-case[39;49;00m[37m [39;49;00m,[31mvar[39;49;00m[37m[39;49;00m
  3304	[37m       [39;49;00m,[31mbodyform[39;49;00m[37m[39;49;00m
  3305	[37m     [39;49;00m,@([32mmapcar[39;49;00m[37m [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31mhandler[39;49;00m)[37m[39;49;00m
  3306	[37m                 [39;49;00m`(([31mdebug[39;49;00m[37m [39;49;00m,@([34mif[39;49;00m[37m [39;49;00m([32mlistp[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mhandler[39;49;00m))[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mhandler[39;49;00m)[37m[39;49;00m
  3307	[37m                              [39;49;00m([32mlist[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mhandler[39;49;00m))))[37m[39;49;00m
  3308	[37m                   [39;49;00m,@([32mcdr[39;49;00m[37m [39;49;00m[31mhandler[39;49;00m)))[37m[39;49;00m
  3309	[37m               [39;49;00m[31mhandlers[39;49;00m)))[37m[39;49;00m
  3310	[37m[39;49;00m
  3311	([36mdefine-obsolete-function-alias[39;49;00m[37m [39;49;00m[33m'condition-case-no-debug[39;49;00m[37m[39;49;00m
  3312	[37m  [39;49;00m[33m'condition-case-unless-debug[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m24.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  3313	[37m[39;49;00m
  3314	([36mdefmacro[39;49;00m[37m [39;49;00m[36mwith-demoted-errors[39;49;00m[37m [39;49;00m([32mformat[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m
  3315	[37m  [39;49;00m[33m"[39;49;00m[33mRun BODY and demote any errors to simple messages.[39;49;00m
  3316	[33mFORMAT is a string passed to [39;49;00m[33m`message'[39;49;00m[33m to format any error message.[39;49;00m
  3317	[33mIt should contain a single %-sequence; e.g., [39;49;00m[33m\"[39;49;00m[33mError: %S[39;49;00m[33m\"[39;49;00m[33m.[39;49;00m
  3318	[33m[39;49;00m
  3319	[33mIf [39;49;00m[33m`debug-on-error'[39;49;00m[33m is non-nil, run BODY without catching its errors.[39;49;00m
  3320	[33mThis is to be used around code which is not expected to signal an error[39;49;00m
  3321	[33mbut which should be robust in the unexpected case that an error is signaled.[39;49;00m
  3322	[33m[39;49;00m
  3323	[33mFor backward compatibility, if FORMAT is not a constant string, it[39;49;00m
  3324	[33mis assumed to be part of BODY, in which case the message format[39;49;00m
  3325	[33mused is [39;49;00m[33m\"[39;49;00m[33mError: %S[39;49;00m[33m\"[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3326	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m1[39;49;00m))[37m[39;49;00m
  3327	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31merr[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33merr[39;49;00m[33m"[39;49;00m))[37m[39;49;00m
  3328	[37m        [39;49;00m([32mformat[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m[32mformat[39;49;00m)[37m [39;49;00m[31mbody[39;49;00m)[37m [39;49;00m[32mformat[39;49;00m[37m[39;49;00m
  3329	[37m                  [39;49;00m([34mprog1[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mError: %S[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3330	[37m                    [39;49;00m([34mif[39;49;00m[37m [39;49;00m[32mformat[39;49;00m[37m [39;49;00m([36mpush[39;49;00m[37m [39;49;00m[32mformat[39;49;00m[37m [39;49;00m[31mbody[39;49;00m))))))[37m[39;49;00m
  3331	[37m    [39;49;00m`([36mcondition-case-unless-debug[39;49;00m[37m [39;49;00m,[31merr[39;49;00m[37m[39;49;00m
  3332	[37m         [39;49;00m,([31mmacroexp-progn[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m
  3333	[37m       [39;49;00m([36merror[39;49;00m[37m [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m,[32mformat[39;49;00m[37m [39;49;00m,[31merr[39;49;00m)[37m [39;49;00m[31mnil[39;49;00m))))[37m[39;49;00m
  3334	[37m[39;49;00m
  3335	([36mdefmacro[39;49;00m[37m [39;49;00m[36mcombine-after-change-calls[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m
  3336	[37m  [39;49;00m[33m"[39;49;00m[33mExecute BODY, but don't call the after-change functions till the end.[39;49;00m
  3337	[33mIf BODY makes changes in the buffer, they are recorded[39;49;00m
  3338	[33mand the functions on [39;49;00m[33m`after-change-functions'[39;49;00m[33m are called several times[39;49;00m
  3339	[33mwhen BODY is finished.[39;49;00m
  3340	[33mThe return value is the value of the last form in BODY.[39;49;00m
  3341	[33m[39;49;00m
  3342	[33mIf [39;49;00m[33m`before-change-functions'[39;49;00m[33m is non-nil, then calls to the after-change[39;49;00m
  3343	[33mfunctions can't be deferred, so in that case this macro has no effect.[39;49;00m
  3344	[33m[39;49;00m
  3345	[33mDo not alter [39;49;00m[33m`after-change-functions'[39;49;00m[33m or [39;49;00m[33m`before-change-functions'[39;49;00m[33m[39;49;00m
  3346	[33min BODY.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3347	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m
  3348	[37m  [39;49;00m`([34munwind-protect[39;49;00m[37m[39;49;00m
  3349	[37m       [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([36mcombine-after-change-calls[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m
  3350	[37m	 [39;49;00m.[37m [39;49;00m,[31mbody[39;49;00m)[37m[39;49;00m
  3351	[37m     [39;49;00m([32mcombine-after-change-execute[39;49;00m)))[37m[39;49;00m
  3352	[37m[39;49;00m
  3353	([36mdefmacro[39;49;00m[37m [39;49;00m[36mwith-case-table[39;49;00m[37m [39;49;00m([31mtable[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m
  3354	[37m  [39;49;00m[33m"[39;49;00m[33mExecute the forms in BODY with TABLE as the current case table.[39;49;00m
  3355	[33mThe value returned is the value of the last form in BODY.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3356	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m
  3357	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mold-case-table[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mtable[39;49;00m[33m"[39;49;00m))[37m[39;49;00m
  3358	[37m	[39;49;00m([31mold-buffer[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mbuffer[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m
  3359	[37m    [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m((,[31mold-case-table[39;49;00m[37m [39;49;00m([32mcurrent-case-table[39;49;00m))[37m[39;49;00m
  3360	[37m	   [39;49;00m(,[31mold-buffer[39;49;00m[37m [39;49;00m([32mcurrent-buffer[39;49;00m)))[37m[39;49;00m
  3361	[37m       [39;49;00m([34munwind-protect[39;49;00m[37m[39;49;00m
  3362	[37m	   [39;49;00m([34mprogn[39;49;00m[37m [39;49;00m([32mset-case-table[39;49;00m[37m [39;49;00m,[31mtable[39;49;00m)[37m[39;49;00m
  3363	[37m		  [39;49;00m,@[31mbody[39;49;00m)[37m[39;49;00m
  3364	[37m	 [39;49;00m([36mwith-current-buffer[39;49;00m[37m [39;49;00m,[31mold-buffer[39;49;00m[37m[39;49;00m
  3365	[37m	   [39;49;00m([32mset-case-table[39;49;00m[37m [39;49;00m,[31mold-case-table[39;49;00m))))))[37m[39;49;00m
  3366	[37m[39;49;00m
  3367	([36mdefmacro[39;49;00m[37m [39;49;00m[36mwith-file-modes[39;49;00m[37m [39;49;00m([31mmodes[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m
  3368	[37m  [39;49;00m[33m"[39;49;00m[33mExecute BODY with default file permissions temporarily set to MODES.[39;49;00m
  3369	[33mMODES is as for [39;49;00m[33m`set-default-file-modes'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3370	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m
  3371	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mumask[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mumask[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m
  3372	[37m    [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m((,[31mumask[39;49;00m[37m [39;49;00m([32mdefault-file-modes[39;49;00m)))[37m[39;49;00m
  3373	[37m       [39;49;00m([34munwind-protect[39;49;00m[37m[39;49;00m
  3374	[37m           [39;49;00m([34mprogn[39;49;00m[37m[39;49;00m
  3375	[37m             [39;49;00m([32mset-default-file-modes[39;49;00m[37m [39;49;00m,[31mmodes[39;49;00m)[37m[39;49;00m
  3376	[37m             [39;49;00m,@[31mbody[39;49;00m)[37m[39;49;00m
  3377	[37m         [39;49;00m([32mset-default-file-modes[39;49;00m[37m [39;49;00m,[31mumask[39;49;00m)))))[37m[39;49;00m
  3378	[37m[39;49;00m
  3379	[37m[39;49;00m[37m[39;49;00m
  3380	[37m;;; Matching and match data.[39;49;00m[37m[39;49;00m
  3381	[37m[39;49;00m
  3382	([34mdefvar[39;49;00m[37m [39;49;00m[31msave-match-data-internal[39;49;00m)[37m[39;49;00m
  3383	[37m[39;49;00m
  3384	[37m;; We use save-match-data-internal as the local variable because[39;49;00m[37m[39;49;00m
  3385	[37m;; that works ok in practice (people should not use that variable elsewhere).[39;49;00m[37m[39;49;00m
  3386	[37m;; We used to use an uninterned symbol; the compiler handles that properly[39;49;00m[37m[39;49;00m
  3387	[37m;; now, but it generates slower code.[39;49;00m[37m[39;49;00m
  3388	([36mdefmacro[39;49;00m[37m [39;49;00m[36msave-match-data[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m
  3389	[37m  [39;49;00m[33m"[39;49;00m[33mExecute the BODY forms, restoring the global value of the match data.[39;49;00m
  3390	[33mThe value returned is the value of the last form in BODY.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3391	[37m  [39;49;00m[37m;; It is better not to use backquote here,[39;49;00m[37m[39;49;00m
  3392	[37m  [39;49;00m[37m;; because that makes a bootstrapping problem[39;49;00m[37m[39;49;00m
  3393	[37m  [39;49;00m[37m;; if you need to recompile all the Lisp files using interpreted code.[39;49;00m[37m[39;49;00m
  3394	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m
  3395	[37m  [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'let[39;49;00m[37m[39;49;00m
  3396	[37m	[39;49;00m'(([31msave-match-data-internal[39;49;00m[37m [39;49;00m([32mmatch-data[39;49;00m)))[37m[39;49;00m
  3397	[37m	[39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'unwind-protect[39;49;00m[37m[39;49;00m
  3398	[37m	      [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[33m'progn[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m
  3399	[37m	      [39;49;00m[37m;; It is safe to free (evaporate) markers immediately here,[39;49;00m[37m[39;49;00m
  3400	[37m	      [39;49;00m[37m;; as Lisp programs should not copy from save-match-data-internal.[39;49;00m[37m[39;49;00m
  3401	[37m	      [39;49;00m'([32mset-match-data[39;49;00m[37m [39;49;00m[31msave-match-data-internal[39;49;00m[37m [39;49;00m[33m'evaporate[39;49;00m))))[37m[39;49;00m
  3402	[37m[39;49;00m
  3403	([36mdefun[39;49;00m[37m [39;49;00m[31mmatch-string[39;49;00m[37m [39;49;00m([31mnum[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[32mstring[39;49;00m)[37m[39;49;00m
  3404	[37m  [39;49;00m[33m"[39;49;00m[33mReturn string of text matched by last search.[39;49;00m
  3405	[33mNUM specifies which parenthesized expression in the last regexp.[39;49;00m
  3406	[33m Value is nil if NUMth pair didn't match, or there were less than NUM pairs.[39;49;00m
  3407	[33mZero means the entire text matched by the whole regexp or whole string.[39;49;00m
  3408	[33mSTRING should be given if the last search was by [39;49;00m[33m`string-match'[39;49;00m[33m on STRING.[39;49;00m
  3409	[33mIf STRING is nil, the current buffer should be the same buffer[39;49;00m
  3410	[33mthe search/match was performed in.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3411	[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mmatch-beginning[39;49;00m[37m [39;49;00m[31mnum[39;49;00m)[37m[39;49;00m
  3412	[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m[39;49;00m
  3413	[37m	  [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m([32mmatch-beginning[39;49;00m[37m [39;49;00m[31mnum[39;49;00m)[37m [39;49;00m([32mmatch-end[39;49;00m[37m [39;49;00m[31mnum[39;49;00m))[37m[39;49;00m
  3414	[37m	[39;49;00m([32mbuffer-substring[39;49;00m[37m [39;49;00m([32mmatch-beginning[39;49;00m[37m [39;49;00m[31mnum[39;49;00m)[37m [39;49;00m([32mmatch-end[39;49;00m[37m [39;49;00m[31mnum[39;49;00m)))))[37m[39;49;00m
  3415	[37m[39;49;00m
  3416	([36mdefun[39;49;00m[37m [39;49;00m[31mmatch-string-no-properties[39;49;00m[37m [39;49;00m([31mnum[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[32mstring[39;49;00m)[37m[39;49;00m
  3417	[37m  [39;49;00m[33m"[39;49;00m[33mReturn string of text matched by last search, without text properties.[39;49;00m
  3418	[33mNUM specifies which parenthesized expression in the last regexp.[39;49;00m
  3419	[33m Value is nil if NUMth pair didn't match, or there were less than NUM pairs.[39;49;00m
  3420	[33mZero means the entire text matched by the whole regexp or whole string.[39;49;00m
  3421	[33mSTRING should be given if the last search was by [39;49;00m[33m`string-match'[39;49;00m[33m on STRING.[39;49;00m
  3422	[33mIf STRING is nil, the current buffer should be the same buffer[39;49;00m
  3423	[33mthe search/match was performed in.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3424	[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mmatch-beginning[39;49;00m[37m [39;49;00m[31mnum[39;49;00m)[37m[39;49;00m
  3425	[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m[39;49;00m
  3426	[37m	  [39;49;00m([32msubstring-no-properties[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m([32mmatch-beginning[39;49;00m[37m [39;49;00m[31mnum[39;49;00m)[37m[39;49;00m
  3427	[37m				   [39;49;00m([32mmatch-end[39;49;00m[37m [39;49;00m[31mnum[39;49;00m))[37m[39;49;00m
  3428	[37m	[39;49;00m([32mbuffer-substring-no-properties[39;49;00m[37m [39;49;00m([32mmatch-beginning[39;49;00m[37m [39;49;00m[31mnum[39;49;00m)[37m[39;49;00m
  3429	[37m					[39;49;00m([32mmatch-end[39;49;00m[37m [39;49;00m[31mnum[39;49;00m)))))[37m[39;49;00m
  3430	[37m[39;49;00m
  3431	[37m[39;49;00m
  3432	([36mdefun[39;49;00m[37m [39;49;00m[31mmatch-substitute-replacement[39;49;00m[37m [39;49;00m([31mreplacement[39;49;00m[37m[39;49;00m
  3433	[37m				     [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mfixedcase[39;49;00m[37m [39;49;00m[31mliteral[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[31msubexp[39;49;00m)[37m[39;49;00m
  3434	[37m  [39;49;00m[33m"[39;49;00m[33mReturn REPLACEMENT as it will be inserted by [39;49;00m[33m`replace-match'[39;49;00m[33m.[39;49;00m
  3435	[33mIn other words, all back-references in the form [39;49;00m[33m`\\&'[39;49;00m[33m and [39;49;00m[33m`\\N'[39;49;00m[33m[39;49;00m
  3436	[33mare substituted with actual strings matched by the last search.[39;49;00m
  3437	[33mOptional FIXEDCASE, LITERAL, STRING and SUBEXP have the same[39;49;00m
  3438	[33mmeaning as for [39;49;00m[33m`replace-match'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3439	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mmatch[39;49;00m[37m [39;49;00m([31mmatch-string[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[32mstring[39;49;00m)))[37m[39;49;00m
  3440	[37m    [39;49;00m([36msave-match-data[39;49;00m[37m[39;49;00m
  3441	[37m      [39;49;00m([32mset-match-data[39;49;00m[37m [39;49;00m([32mmapcar[39;49;00m[37m [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31mx[39;49;00m)[37m[39;49;00m
  3442	[37m				[39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mnumberp[39;49;00m[37m [39;49;00m[31mx[39;49;00m)[37m[39;49;00m
  3443	[37m				    [39;49;00m([32m-[39;49;00m[37m [39;49;00m[31mx[39;49;00m[37m [39;49;00m([32mmatch-beginning[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m
  3444	[37m				  [39;49;00m[31mx[39;49;00m))[37m[39;49;00m
  3445	[37m			      [39;49;00m([32mmatch-data[39;49;00m[37m [39;49;00m[31mt[39;49;00m)))[37m[39;49;00m
  3446	[37m      [39;49;00m([32mreplace-match[39;49;00m[37m [39;49;00m[31mreplacement[39;49;00m[37m [39;49;00m[31mfixedcase[39;49;00m[37m [39;49;00m[31mliteral[39;49;00m[37m [39;49;00m[31mmatch[39;49;00m[37m [39;49;00m[31msubexp[39;49;00m))))[37m[39;49;00m
  3447	[37m[39;49;00m
  3448	[37m[39;49;00m
  3449	([36mdefun[39;49;00m[37m [39;49;00m[31mlooking-back[39;49;00m[37m [39;49;00m([31mregexp[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mlimit[39;49;00m[37m [39;49;00m[31mgreedy[39;49;00m)[37m[39;49;00m
  3450	[37m  [39;49;00m[33m"[39;49;00m[33mReturn non-nil if text before point matches regular expression REGEXP.[39;49;00m
  3451	[33mLike [39;49;00m[33m`looking-at'[39;49;00m[33m except matches before point, and is slower.[39;49;00m
  3452	[33mLIMIT if non-nil speeds up the search by specifying a minimum[39;49;00m
  3453	[33mstarting position, to avoid checking matches that would start[39;49;00m
  3454	[33mbefore LIMIT.[39;49;00m
  3455	[33m[39;49;00m
  3456	[33mIf GREEDY is non-nil, extend the match backwards as far as[39;49;00m
  3457	[33mpossible, stopping when a single additional previous character[39;49;00m
  3458	[33mcannot be part of a match for REGEXP.  When the match is[39;49;00m
  3459	[33mextended, its starting position is allowed to occur before[39;49;00m
  3460	[33mLIMIT.[39;49;00m
  3461	[33m[39;49;00m
  3462	[33mAs a general recommendation, try to avoid using [39;49;00m[33m`looking-back'[39;49;00m[33m[39;49;00m
  3463	[33mwherever possible, since it is slow.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3464	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mstart[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m))[37m[39;49;00m
  3465	[37m	[39;49;00m([31mpos[39;49;00m[37m[39;49;00m
  3466	[37m	 [39;49;00m([34msave-excursion[39;49;00m[37m[39;49;00m
  3467	[37m	   [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mre-search-backward[39;49;00m[37m [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m(?:[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mregexp[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m)[39;49;00m[33m\\[39;49;00m[33m=[39;49;00m[33m"[39;49;00m)[37m [39;49;00m[31mlimit[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m
  3468	[37m		[39;49;00m([32mpoint[39;49;00m)))))[37m[39;49;00m
  3469	[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mgreedy[39;49;00m[37m [39;49;00m[31mpos[39;49;00m)[37m[39;49;00m
  3470	[37m	[39;49;00m([34msave-restriction[39;49;00m[37m[39;49;00m
  3471	[37m	  [39;49;00m([32mnarrow-to-region[39;49;00m[37m [39;49;00m([32mpoint-min[39;49;00m)[37m [39;49;00m[31mstart[39;49;00m)[37m[39;49;00m
  3472	[37m	  [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m[31mpos[39;49;00m[37m [39;49;00m([32mpoint-min[39;49;00m))[37m[39;49;00m
  3473	[37m		      [39;49;00m([34msave-excursion[39;49;00m[37m[39;49;00m
  3474	[37m			[39;49;00m([32mgoto-char[39;49;00m[37m [39;49;00m[31mpos[39;49;00m)[37m[39;49;00m
  3475	[37m			[39;49;00m([32mbackward-char[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m[39;49;00m
  3476	[37m			[39;49;00m([32mlooking-at[39;49;00m[37m [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m(?:[39;49;00m[33m"[39;49;00m[37m  [39;49;00m[31mregexp[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m)[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m[33m"[39;49;00m))))[37m[39;49;00m
  3477	[37m	    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mpos[39;49;00m[37m [39;49;00m([32m1-[39;49;00m[37m [39;49;00m[31mpos[39;49;00m)))[37m[39;49;00m
  3478	[37m	  [39;49;00m([34msave-excursion[39;49;00m[37m[39;49;00m
  3479	[37m	    [39;49;00m([32mgoto-char[39;49;00m[37m [39;49;00m[31mpos[39;49;00m)[37m[39;49;00m
  3480	[37m	    [39;49;00m([32mlooking-at[39;49;00m[37m [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m(?:[39;49;00m[33m"[39;49;00m[37m  [39;49;00m[31mregexp[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m)[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m[33m"[39;49;00m)))))[37m[39;49;00m
  3481	[37m    [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[31mpos[39;49;00m))))[37m[39;49;00m
  3482	[37m[39;49;00m
  3483	([36mdefsubst[39;49;00m[37m [39;49;00m[31mlooking-at-p[39;49;00m[37m [39;49;00m([31mregexp[39;49;00m)[37m[39;49;00m
  3484	[37m  [39;49;00m[33m"[39;49;00m[33m\[39;49;00m
  3485	[33mSame as [39;49;00m[33m`looking-at'[39;49;00m[33m except this function does not change the match data.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3486	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31minhibit-changing-match-data[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m
  3487	[37m    [39;49;00m([32mlooking-at[39;49;00m[37m [39;49;00m[31mregexp[39;49;00m)))[37m[39;49;00m
  3488	[37m[39;49;00m
  3489	([36mdefsubst[39;49;00m[37m [39;49;00m[31mstring-match-p[39;49;00m[37m [39;49;00m([31mregexp[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mstart[39;49;00m)[37m[39;49;00m
  3490	[37m  [39;49;00m[33m"[39;49;00m[33m\[39;49;00m
  3491	[33mSame as [39;49;00m[33m`string-match'[39;49;00m[33m except this function does not change the match data.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3492	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31minhibit-changing-match-data[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m
  3493	[37m    [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[31mregexp[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[31mstart[39;49;00m)))[37m[39;49;00m
  3494	[37m[39;49;00m
  3495	([36mdefun[39;49;00m[37m [39;49;00m[31msubregexp-context-p[39;49;00m[37m [39;49;00m([31mregexp[39;49;00m[37m [39;49;00m[31mpos[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mstart[39;49;00m)[37m[39;49;00m
  3496	[37m  [39;49;00m[33m"[39;49;00m[33mReturn non-nil if POS is in a normal subregexp context in REGEXP.[39;49;00m
  3497	[33mA subregexp context is one where a sub-regexp can appear.[39;49;00m
  3498	[33mA non-subregexp context is for example within brackets, or within a[39;49;00m
  3499	[33mrepetition bounds operator [39;49;00m[33m`\\=\\{...\\}'[39;49;00m[33m, or right after a [39;49;00m[33m`\\'[39;49;00m[33m.[39;49;00m
  3500	[33mIf START is non-nil, it should be a position in REGEXP, smaller[39;49;00m
  3501	[33mthan POS, and known to be in a subregexp context.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3502	[37m  [39;49;00m[37m;; Here's one possible implementation, with the great benefit that it[39;49;00m[37m[39;49;00m
  3503	[37m  [39;49;00m[37m;; reuses the regexp-matcher's own parser, so it understands all the[39;49;00m[37m[39;49;00m
  3504	[37m  [39;49;00m[37m;; details of the syntax.  A disadvantage is that it needs to match the[39;49;00m[37m[39;49;00m
  3505	[37m  [39;49;00m[37m;; error string.[39;49;00m[37m[39;49;00m
  3506	[37m  [39;49;00m([34mcondition-case[39;49;00m[37m [39;49;00m[31merr[39;49;00m[37m[39;49;00m
  3507	[37m      [39;49;00m([34mprogn[39;49;00m[37m[39;49;00m
  3508	[37m        [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[31mregexp[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[31mpos[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  3509	[37m        [39;49;00m[31mt[39;49;00m)[37m[39;49;00m
  3510	[37m    [39;49;00m([31minvalid-regexp[39;49;00m[37m[39;49;00m
  3511	[37m     [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mmember[39;49;00m[37m [39;49;00m([31mcadr[39;49;00m[37m [39;49;00m[31merr[39;49;00m)[37m [39;49;00m'([33m"[39;49;00m[33mUnmatched [ or [^[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3512	[37m                               [39;49;00m[33m"[39;49;00m[33mUnmatched [39;49;00m[33m\\[39;49;00m[33m{[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3513	[37m                               [39;49;00m[33m"[39;49;00m[33mTrailing backslash[39;49;00m[33m"[39;49;00m)))))[37m[39;49;00m
  3514	[37m  [39;49;00m[37m;; An alternative implementation:[39;49;00m[37m[39;49;00m
  3515	[37m  [39;49;00m[37m;; (defconst re-context-re[39;49;00m[37m[39;49;00m
  3516	[37m  [39;49;00m[37m;;   (let* ((harmless-ch "[^\\[]")[39;49;00m[37m[39;49;00m
  3517	[37m  [39;49;00m[37m;;          (harmless-esc "\\\\[^{]")[39;49;00m[37m[39;49;00m
  3518	[37m  [39;49;00m[37m;;          (class-harmless-ch "[^][]")[39;49;00m[37m[39;49;00m
  3519	[37m  [39;49;00m[37m;;          (class-lb-harmless "[^]:]")[39;49;00m[37m[39;49;00m
  3520	[37m  [39;49;00m[37m;;          (class-lb-colon-maybe-charclass ":\\([a-z]+:]\\)?")[39;49;00m[37m[39;49;00m
  3521	[37m  [39;49;00m[37m;;          (class-lb (concat "\\[\\(" class-lb-harmless[39;49;00m[37m[39;49;00m
  3522	[37m  [39;49;00m[37m;;                            "\\|" class-lb-colon-maybe-charclass "\\)"))[39;49;00m[37m[39;49;00m
  3523	[37m  [39;49;00m[37m;;          (class[39;49;00m[37m[39;49;00m
  3524	[37m  [39;49;00m[37m;;           (concat "\\[^?]?"[39;49;00m[37m[39;49;00m
  3525	[37m  [39;49;00m[37m;;                   "\\(" class-harmless-ch[39;49;00m[37m[39;49;00m
  3526	[37m  [39;49;00m[37m;;                   "\\|" class-lb "\\)*"[39;49;00m[37m[39;49;00m
  3527	[37m  [39;49;00m[37m;;                   "\\[?]"))     ; special handling for bare [ at end of re[39;49;00m[37m[39;49;00m
  3528	[37m  [39;49;00m[37m;;          (braces "\\\\{[0-9,]+\\\\}"))[39;49;00m[37m[39;49;00m
  3529	[37m  [39;49;00m[37m;;     (concat "\\`\\(" harmless-ch "\\|" harmless-esc[39;49;00m[37m[39;49;00m
  3530	[37m  [39;49;00m[37m;;             "\\|" class "\\|" braces "\\)*\\'"))[39;49;00m[37m[39;49;00m
  3531	[37m  [39;49;00m[37m;;   "Matches any prefix that corresponds to a normal subregexp context.")[39;49;00m[37m[39;49;00m
  3532	[37m  [39;49;00m[37m;; (string-match re-context-re (substring regexp (or start 0) pos))[39;49;00m[37m[39;49;00m
  3533	[37m  [39;49;00m)[37m[39;49;00m
  3534	[37m[39;49;00m[37m[39;49;00m
  3535	[37m;;;; split-string[39;49;00m[37m[39;49;00m
  3536	[37m[39;49;00m
  3537	([34mdefconst[39;49;00m[37m [39;49;00m[31msplit-string-default-separators[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m[ [39;49;00m[33m\f[39;49;00m[33m\t[39;49;00m[33m\n[39;49;00m[33m\r[39;49;00m[33m\v[39;49;00m[33m]+[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3538	[37m  [39;49;00m[33m"[39;49;00m[33mThe default value of separators for [39;49;00m[33m`split-string'[39;49;00m[33m.[39;49;00m
  3539	[33m[39;49;00m
  3540	[33mA regexp matching strings of whitespace.  May be locale-dependent[39;49;00m
  3541	[33m\([39;49;00m[33mas yet unimplemented).  Should not match non-breaking spaces.[39;49;00m
  3542	[33m[39;49;00m
  3543	[33mWarning: binding this to a different value and using it as default is[39;49;00m
  3544	[33mlikely to have undesired semantics.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  3545	[37m[39;49;00m
  3546	[37m;; The specification says that if both SEPARATORS and OMIT-NULLS are[39;49;00m[37m[39;49;00m
  3547	[37m;; defaulted, OMIT-NULLS should be treated as t.  Simplifying the logical[39;49;00m[37m[39;49;00m
  3548	[37m;; expression leads to the equivalent implementation that if SEPARATORS[39;49;00m[37m[39;49;00m
  3549	[37m;; is defaulted, OMIT-NULLS is treated as t.[39;49;00m[37m[39;49;00m
  3550	([36mdefun[39;49;00m[37m [39;49;00m[31msplit-string[39;49;00m[37m [39;49;00m([32mstring[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mseparators[39;49;00m[37m [39;49;00m[31momit-nulls[39;49;00m[37m [39;49;00m[31mtrim[39;49;00m)[37m[39;49;00m
  3551	[37m  [39;49;00m[33m"[39;49;00m[33mSplit STRING into substrings bounded by matches for SEPARATORS.[39;49;00m
  3552	[33m[39;49;00m
  3553	[33mThe beginning and end of STRING, and each match for SEPARATORS, are[39;49;00m
  3554	[33msplitting points.  The substrings matching SEPARATORS are removed, and[39;49;00m
  3555	[33mthe substrings between the splitting points are collected as a list,[39;49;00m
  3556	[33mwhich is returned.[39;49;00m
  3557	[33m[39;49;00m
  3558	[33mIf SEPARATORS is non-nil, it should be a regular expression matching text[39;49;00m
  3559	[33mwhich separates, but is not part of, the substrings.  If nil it defaults to[39;49;00m
  3560	[33m`split-string-default-separators'[39;49;00m[33m, normally [39;49;00m[33m\"[39;49;00m[33m[ [39;49;00m[33m\\[39;49;00m[33mf[39;49;00m[33m\\[39;49;00m[33mt[39;49;00m[33m\\[39;49;00m[33mn[39;49;00m[33m\\[39;49;00m[33mr[39;49;00m[33m\\[39;49;00m[33mv]+[39;49;00m[33m\"[39;49;00m[33m, and[39;49;00m
  3561	[33mOMIT-NULLS is forced to t.[39;49;00m
  3562	[33m[39;49;00m
  3563	[33mIf OMIT-NULLS is t, zero-length substrings are omitted from the list (so[39;49;00m
  3564	[33mthat for the default value of SEPARATORS leading and trailing whitespace[39;49;00m
  3565	[33mare effectively trimmed).  If nil, all zero-length substrings are retained,[39;49;00m
  3566	[33mwhich correctly parses CSV format, for example.[39;49;00m
  3567	[33m[39;49;00m
  3568	[33mIf TRIM is non-nil, it should be a regular expression to match[39;49;00m
  3569	[33mtext to trim from the beginning and end of each substring.  If trimming[39;49;00m
  3570	[33mmakes the substring empty, it is treated as null.[39;49;00m
  3571	[33m[39;49;00m
  3572	[33mIf you want to trim whitespace from the substrings, the reliably correct[39;49;00m
  3573	[33mway is using TRIM.  Making SEPARATORS match that whitespace gives incorrect[39;49;00m
  3574	[33mresults when there is whitespace at the start or end of STRING.  If you[39;49;00m
  3575	[33msee such calls to [39;49;00m[33m`split-string'[39;49;00m[33m, please fix them.[39;49;00m
  3576	[33m[39;49;00m
  3577	[33mNote that the effect of [39;49;00m[33m`[39;49;00m[33m(split-string STRING)' is the same as[39;49;00m
  3578	[33m`[39;49;00m[33m(split-string STRING split-string-default-separators t)'.  In the rare[39;49;00m
  3579	[33mcase that you wish to retain zero-length substrings when splitting on[39;49;00m
  3580	[33mwhitespace, use [39;49;00m[33m`[39;49;00m[33m(split-string STRING split-string-default-separators)'.[39;49;00m
  3581	[33m[39;49;00m
  3582	[33mModifies the match data; use [39;49;00m[33m`save-match-data'[39;49;00m[33m if necessary.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3583	[37m  [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mkeep-nulls[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mseparators[39;49;00m[37m [39;49;00m[31momit-nulls[39;49;00m[37m [39;49;00m[31mt[39;49;00m)))[37m[39;49;00m
  3584	[37m	 [39;49;00m([31mrexp[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mseparators[39;49;00m[37m [39;49;00m[31msplit-string-default-separators[39;49;00m))[37m[39;49;00m
  3585	[37m	 [39;49;00m([31mstart[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m
  3586	[37m	 [39;49;00m[31mthis-start[39;49;00m[37m [39;49;00m[31mthis-end[39;49;00m[37m[39;49;00m
  3587	[37m	 [39;49;00m[31mnotfirst[39;49;00m[37m[39;49;00m
  3588	[37m	 [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m
  3589	[37m	 [39;49;00m([31mpush-one[39;49;00m[37m[39;49;00m
  3590	[37m	  [39;49;00m[37m;; Push the substring in range THIS-START to THIS-END[39;49;00m[37m[39;49;00m
  3591	[37m	  [39;49;00m[37m;; onto LIST, trimming it and perhaps discarding it.[39;49;00m[37m[39;49;00m
  3592	[37m	  [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m()[37m[39;49;00m
  3593	[37m	    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31mtrim[39;49;00m[37m[39;49;00m
  3594	[37m	      [39;49;00m[37m;; Discard the trim from start of this substring.[39;49;00m[37m[39;49;00m
  3595	[37m	      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtem[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[31mtrim[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[31mthis-start[39;49;00m)))[37m[39;49;00m
  3596	[37m		[39;49;00m([34mand[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mtem[39;49;00m[37m [39;49;00m[31mthis-start[39;49;00m)[37m[39;49;00m
  3597	[37m		     [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mthis-start[39;49;00m[37m [39;49;00m([32mmatch-end[39;49;00m[37m [39;49;00m[34m0[39;49;00m)))))[37m[39;49;00m
  3598	[37m[39;49;00m
  3599	[37m	    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mkeep-nulls[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m[31mthis-start[39;49;00m[37m [39;49;00m[31mthis-end[39;49;00m))[37m[39;49;00m
  3600	[37m	      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mthis[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[31mthis-start[39;49;00m[37m [39;49;00m[31mthis-end[39;49;00m)))[37m[39;49;00m
  3601	[37m[39;49;00m
  3602	[37m		[39;49;00m[37m;; Discard the trim from end of this substring.[39;49;00m[37m[39;49;00m
  3603	[37m		[39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31mtrim[39;49;00m[37m[39;49;00m
  3604	[37m		  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtem[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[31mtrim[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m[33m"[39;49;00m)[37m [39;49;00m[31mthis[39;49;00m[37m [39;49;00m[34m0[39;49;00m)))[37m[39;49;00m
  3605	[37m		    [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mtem[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m[31mtem[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31mthis[39;49;00m))[37m[39;49;00m
  3606	[37m			 [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mthis[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[31mthis[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[31mtem[39;49;00m)))))[37m[39;49;00m
  3607	[37m[39;49;00m
  3608	[37m		[39;49;00m[37m;; Trimming could make it empty; check again.[39;49;00m[37m[39;49;00m
  3609	[37m		[39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mkeep-nulls[39;49;00m[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31mthis[39;49;00m)[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m
  3610	[37m		  [39;49;00m([36mpush[39;49;00m[37m [39;49;00m[31mthis[39;49;00m[37m [39;49;00m[32mlist[39;49;00m)))))))[37m[39;49;00m
  3611	[37m[39;49;00m
  3612	[37m    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[31mrexp[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m[39;49;00m
  3613	[37m			      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mnotfirst[39;49;00m[37m[39;49;00m
  3614	[37m				       [39;49;00m([32m=[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m([32mmatch-beginning[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m
  3615	[37m				       [39;49;00m([32m<[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[32mstring[39;49;00m)))[37m[39;49;00m
  3616	[37m				  [39;49;00m([32m1+[39;49;00m[37m [39;49;00m[31mstart[39;49;00m)[37m [39;49;00m[31mstart[39;49;00m))[37m[39;49;00m
  3617	[37m		[39;49;00m([32m<[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[32mstring[39;49;00m)))[37m[39;49;00m
  3618	[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mnotfirst[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m
  3619	[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mthis-start[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mthis-end[39;49;00m[37m [39;49;00m([32mmatch-beginning[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m
  3620	[37m	    [39;49;00m[31mstart[39;49;00m[37m [39;49;00m([32mmatch-end[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m
  3621	[37m[39;49;00m
  3622	[37m      [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mpush-one[39;49;00m))[37m[39;49;00m
  3623	[37m[39;49;00m
  3624	[37m    [39;49;00m[37m;; Handle the substring at the end of STRING.[39;49;00m[37m[39;49;00m
  3625	[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mthis-start[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mthis-end[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[32mstring[39;49;00m))[37m[39;49;00m
  3626	[37m    [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mpush-one[39;49;00m)[37m[39;49;00m
  3627	[37m[39;49;00m
  3628	[37m    [39;49;00m([32mnreverse[39;49;00m[37m [39;49;00m[32mlist[39;49;00m)))[37m[39;49;00m
  3629	[37m[39;49;00m
  3630	([36mdefun[39;49;00m[37m [39;49;00m[31mcombine-and-quote-strings[39;49;00m[37m [39;49;00m([31mstrings[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mseparator[39;49;00m)[37m[39;49;00m
  3631	[37m  [39;49;00m[33m"[39;49;00m[33mConcatenate the STRINGS, adding the SEPARATOR (default [39;49;00m[33m\"[39;49;00m[33m [39;49;00m[33m\"[39;49;00m[33m).[39;49;00m
  3632	[33mThis tries to quote the strings to avoid ambiguity such that[39;49;00m
  3633	[33m  (split-string-and-unquote (combine-and-quote-strings strs)) == strs[39;49;00m
  3634	[33mOnly some SEPARATORs will work properly.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3635	[37m  [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31msep[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mseparator[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m))[37m[39;49;00m
  3636	[37m         [39;49;00m([31mre[39;49;00m[37m [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m[[39;49;00m[33m\\[39;49;00m[33m\"[39;49;00m[33m][39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m|[39;49;00m[33m"[39;49;00m[37m [39;49;00m([32mregexp-quote[39;49;00m[37m [39;49;00m[31msep[39;49;00m))))[37m[39;49;00m
  3637	[37m    [39;49;00m([32mmapconcat[39;49;00m[37m[39;49;00m
  3638	[37m     [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31mstr[39;49;00m)[37m[39;49;00m
  3639	[37m       [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[31mre[39;49;00m[37m [39;49;00m[31mstr[39;49;00m)[37m[39;49;00m
  3640	[37m	   [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m[37m [39;49;00m([31mreplace-regexp-in-string[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m[[39;49;00m[33m\\[39;49;00m[33m\"[39;49;00m[33m][39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m&[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mstr[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  3641	[37m	 [39;49;00m[31mstr[39;49;00m))[37m[39;49;00m
  3642	[37m     [39;49;00m[31mstrings[39;49;00m[37m [39;49;00m[31msep[39;49;00m)))[37m[39;49;00m
  3643	[37m[39;49;00m
  3644	([36mdefun[39;49;00m[37m [39;49;00m[31msplit-string-and-unquote[39;49;00m[37m [39;49;00m([32mstring[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mseparator[39;49;00m)[37m[39;49;00m
  3645	[37m  [39;49;00m[33m"[39;49;00m[33mSplit the STRING into a list of strings.[39;49;00m
  3646	[33mIt understands Emacs Lisp quoting within STRING, such that[39;49;00m
  3647	[33m  (split-string-and-unquote (combine-and-quote-strings strs)) == strs[39;49;00m
  3648	[33mThe SEPARATOR regexp defaults to [39;49;00m[33m\"[39;49;00m[33m\\[39;49;00m[33ms-+[39;49;00m[33m\"[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3649	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31msep[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mseparator[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33ms-+[39;49;00m[33m"[39;49;00m))[37m[39;49;00m
  3650	[37m	[39;49;00m([31mi[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m[37m [39;49;00m[32mstring[39;49;00m)))[37m[39;49;00m
  3651	[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[31mi[39;49;00m)[37m[39;49;00m
  3652	[37m	[39;49;00m([31msplit-string[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[31msep[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m	[39;49;00m[37m; no quoting:  easy[39;49;00m[37m[39;49;00m
  3653	[37m      [39;49;00m([32mappend[39;49;00m[37m [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mi[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m([31msplit-string[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[31mi[39;49;00m)[37m [39;49;00m[31msep[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m
  3654	[37m	      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mrfs[39;49;00m[37m [39;49;00m([32mread-from-string[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[31mi[39;49;00m)))[37m[39;49;00m
  3655	[37m		[39;49;00m([32mcons[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mrfs[39;49;00m)[37m[39;49;00m
  3656	[37m		      [39;49;00m([31msplit-string-and-unquote[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mrfs[39;49;00m))[37m[39;49;00m
  3657	[37m						[39;49;00m[31msep[39;49;00m)))))))[37m[39;49;00m
  3658	[37m[39;49;00m
  3659	[37m[39;49;00m[37m[39;49;00m
  3660	[37m;;;; Replacement in strings.[39;49;00m[37m[39;49;00m
  3661	[37m[39;49;00m
  3662	([36mdefun[39;49;00m[37m [39;49;00m[31msubst-char-in-string[39;49;00m[37m [39;49;00m([31mfromchar[39;49;00m[37m [39;49;00m[31mtochar[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31minplace[39;49;00m)[37m[39;49;00m
  3663	[37m  [39;49;00m[33m"[39;49;00m[33mReplace FROMCHAR with TOCHAR in STRING each time it occurs.[39;49;00m
  3664	[33mUnless optional argument INPLACE is non-nil, return a new string.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3665	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mi[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[32mstring[39;49;00m))[37m[39;49;00m
  3666	[37m	[39;49;00m([31mnewstr[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31minplace[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m([32mcopy-sequence[39;49;00m[37m [39;49;00m[32mstring[39;49;00m))))[37m[39;49;00m
  3667	[37m    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m[31mi[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m
  3668	[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mi[39;49;00m[37m [39;49;00m([32m1-[39;49;00m[37m [39;49;00m[31mi[39;49;00m))[37m[39;49;00m
  3669	[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32maref[39;49;00m[37m [39;49;00m[31mnewstr[39;49;00m[37m [39;49;00m[31mi[39;49;00m)[37m [39;49;00m[31mfromchar[39;49;00m)[37m[39;49;00m
  3670	[37m	  [39;49;00m([32maset[39;49;00m[37m [39;49;00m[31mnewstr[39;49;00m[37m [39;49;00m[31mi[39;49;00m[37m [39;49;00m[31mtochar[39;49;00m)))[37m[39;49;00m
  3671	[37m    [39;49;00m[31mnewstr[39;49;00m))[37m[39;49;00m
  3672	[37m[39;49;00m
  3673	([36mdefun[39;49;00m[37m [39;49;00m[31mreplace-regexp-in-string[39;49;00m[37m [39;49;00m([31mregexp[39;49;00m[37m [39;49;00m[31mrep[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m[39;49;00m
  3674	[37m					[39;49;00m[31mfixedcase[39;49;00m[37m [39;49;00m[31mliteral[39;49;00m[37m [39;49;00m[31msubexp[39;49;00m[37m [39;49;00m[31mstart[39;49;00m)[37m[39;49;00m
  3675	[37m  [39;49;00m[33m"[39;49;00m[33mReplace all matches for REGEXP with REP in STRING.[39;49;00m
  3676	[33m[39;49;00m
  3677	[33mReturn a new string containing the replacements.[39;49;00m
  3678	[33m[39;49;00m
  3679	[33mOptional arguments FIXEDCASE, LITERAL and SUBEXP are like the[39;49;00m
  3680	[33marguments with the same names of function [39;49;00m[33m`replace-match'[39;49;00m[33m.  If START[39;49;00m
  3681	[33mis non-nil, start replacements at that index in STRING.[39;49;00m
  3682	[33m[39;49;00m
  3683	[33mREP is either a string used as the NEWTEXT arg of [39;49;00m[33m`replace-match'[39;49;00m[33m or a[39;49;00m
  3684	[33mfunction.  If it is a function, it is called with the actual text of each[39;49;00m
  3685	[33mmatch, and its value is used as the replacement text.  When REP is called,[39;49;00m
  3686	[33mthe match data are the result of matching REGEXP against a substring[39;49;00m
  3687	[33mof STRING.[39;49;00m
  3688	[33m[39;49;00m
  3689	[33mTo replace only the first match (if any), make REGEXP match up to [39;49;00m[33m\\[39;49;00m[33m'[39;49;00m
  3690	[33mand replace a sub-expression, e.g.[39;49;00m
  3691	[33m  (replace-regexp-in-string [39;49;00m[33m\"[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m(foo[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m).*[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m[33m\"[39;49;00m[33m [39;49;00m[33m\"[39;49;00m[33mbar[39;49;00m[33m\"[39;49;00m[33m [39;49;00m[33m\"[39;49;00m[33m foo foo[39;49;00m[33m\"[39;49;00m[33m nil nil 1)[39;49;00m
  3692	[33m    => [39;49;00m[33m\"[39;49;00m[33m bar foo[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3693	[37m[39;49;00m
  3694	[37m  [39;49;00m[37m;; To avoid excessive consing from multiple matches in long strings,[39;49;00m[37m[39;49;00m
  3695	[37m  [39;49;00m[37m;; don't just call `replace-match' continually.  Walk down the[39;49;00m[37m[39;49;00m
  3696	[37m  [39;49;00m[37m;; string looking for matches of REGEXP and building up a (reversed)[39;49;00m[37m[39;49;00m
  3697	[37m  [39;49;00m[37m;; list MATCHES.  This comprises segments of STRING which weren't[39;49;00m[37m[39;49;00m
  3698	[37m  [39;49;00m[37m;; matched interspersed with replacements for segments that were.[39;49;00m[37m[39;49;00m
  3699	[37m  [39;49;00m[37m;; [For a `large' number of replacements it's more efficient to[39;49;00m[37m[39;49;00m
  3700	[37m  [39;49;00m[37m;; operate in a temporary buffer; we can't tell from the function's[39;49;00m[37m[39;49;00m
  3701	[37m  [39;49;00m[37m;; args whether to choose the buffer-based implementation, though it[39;49;00m[37m[39;49;00m
  3702	[37m  [39;49;00m[37m;; might be reasonable to do so for long enough STRING.][39;49;00m[37m[39;49;00m
  3703	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31ml[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[32mstring[39;49;00m))[37m[39;49;00m
  3704	[37m	[39;49;00m([31mstart[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m
  3705	[37m	[39;49;00m[31mmatches[39;49;00m[37m [39;49;00m[31mstr[39;49;00m[37m [39;49;00m[31mmb[39;49;00m[37m [39;49;00m[31mme[39;49;00m)[37m[39;49;00m
  3706	[37m    [39;49;00m([36msave-match-data[39;49;00m[37m[39;49;00m
  3707	[37m      [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31ml[39;49;00m)[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[31mregexp[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[31mstart[39;49;00m))[37m[39;49;00m
  3708	[37m	[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mmb[39;49;00m[37m [39;49;00m([32mmatch-beginning[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m
  3709	[37m	      [39;49;00m[31mme[39;49;00m[37m [39;49;00m([32mmatch-end[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m
  3710	[37m	[39;49;00m[37m;; If we matched the empty string, make sure we advance by one char[39;49;00m[37m[39;49;00m
  3711	[37m	[39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32m=[39;49;00m[37m [39;49;00m[31mme[39;49;00m[37m [39;49;00m[31mmb[39;49;00m)[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mme[39;49;00m[37m [39;49;00m([32mmin[39;49;00m[37m [39;49;00m[31ml[39;49;00m[37m [39;49;00m([32m1+[39;49;00m[37m [39;49;00m[31mmb[39;49;00m))))[37m[39;49;00m
  3712	[37m	[39;49;00m[37m;; Generate a replacement for the matched substring.[39;49;00m[37m[39;49;00m
  3713	[37m	[39;49;00m[37m;; Operate only on the substring to minimize string consing.[39;49;00m[37m[39;49;00m
  3714	[37m	[39;49;00m[37m;; Set up match data for the substring for replacement;[39;49;00m[37m[39;49;00m
  3715	[37m	[39;49;00m[37m;; presumably this is likely to be faster than munging the[39;49;00m[37m[39;49;00m
  3716	[37m	[39;49;00m[37m;; match data directly in Lisp.[39;49;00m[37m[39;49;00m
  3717	[37m	[39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[31mregexp[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mstr[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[31mmb[39;49;00m[37m [39;49;00m[31mme[39;49;00m)))[37m[39;49;00m
  3718	[37m	[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mmatches[39;49;00m[37m[39;49;00m
  3719	[37m	      [39;49;00m([32mcons[39;49;00m[37m [39;49;00m([32mreplace-match[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m[31mrep[39;49;00m)[37m[39;49;00m
  3720	[37m				       [39;49;00m[31mrep[39;49;00m[37m[39;49;00m
  3721	[37m				     [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mrep[39;49;00m[37m [39;49;00m([31mmatch-string[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[31mstr[39;49;00m)))[37m[39;49;00m
  3722	[37m				   [39;49;00m[31mfixedcase[39;49;00m[37m [39;49;00m[31mliteral[39;49;00m[37m [39;49;00m[31mstr[39;49;00m[37m [39;49;00m[31msubexp[39;49;00m)[37m[39;49;00m
  3723	[37m		    [39;49;00m([32mcons[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mmb[39;49;00m)[37m [39;49;00m[37m; unmatched prefix[39;49;00m[37m[39;49;00m
  3724	[37m			  [39;49;00m[31mmatches[39;49;00m)))[37m[39;49;00m
  3725	[37m	[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mme[39;49;00m))[37m[39;49;00m
  3726	[37m      [39;49;00m[37m;; Reconstruct a string from the pieces.[39;49;00m[37m[39;49;00m
  3727	[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mmatches[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31ml[39;49;00m)[37m [39;49;00m[31mmatches[39;49;00m))[37m [39;49;00m[37m; leftover[39;49;00m[37m[39;49;00m
  3728	[37m      [39;49;00m([32mapply[39;49;00m[37m [39;49;00m[32m#'[39;49;00m[32mconcat[39;49;00m[37m [39;49;00m([32mnreverse[39;49;00m[37m [39;49;00m[31mmatches[39;49;00m)))))[37m[39;49;00m
  3729	[37m[39;49;00m[37m[39;49;00m
  3730	([36mdefun[39;49;00m[37m [39;49;00m[31mstring-prefix-p[39;49;00m[37m [39;49;00m([31mprefix[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mignore-case[39;49;00m)[37m[39;49;00m
  3731	[37m  [39;49;00m[33m"[39;49;00m[33mReturn non-nil if PREFIX is a prefix of STRING.[39;49;00m
  3732	[33mIf IGNORE-CASE is non-nil, the comparison is done without paying attention[39;49;00m
  3733	[33mto case differences.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3734	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mprefix-length[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31mprefix[39;49;00m)))[37m[39;49;00m
  3735	[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m[31mprefix-length[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[32mstring[39;49;00m))[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m
  3736	[37m      [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m([32mcompare-strings[39;49;00m[37m [39;49;00m[31mprefix[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[31mprefix-length[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m[39;49;00m
  3737	[37m			     [39;49;00m[34m0[39;49;00m[37m [39;49;00m[31mprefix-length[39;49;00m[37m [39;49;00m[31mignore-case[39;49;00m)))))[37m[39;49;00m
  3738	[37m[39;49;00m
  3739	([36mdefun[39;49;00m[37m [39;49;00m[31mstring-suffix-p[39;49;00m[37m [39;49;00m([31msuffix[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m  [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mignore-case[39;49;00m)[37m[39;49;00m
  3740	[37m  [39;49;00m[33m"[39;49;00m[33mReturn non-nil if SUFFIX is a suffix of STRING.[39;49;00m
  3741	[33mIf IGNORE-CASE is non-nil, the comparison is done without paying[39;49;00m
  3742	[33mattention to case differences.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3743	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mstart-pos[39;49;00m[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[32mstring[39;49;00m)[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31msuffix[39;49;00m))))[37m[39;49;00m
  3744	[37m    [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32m>=[39;49;00m[37m [39;49;00m[31mstart-pos[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m
  3745	[37m         [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m([32mcompare-strings[39;49;00m[37m [39;49;00m[31msuffix[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m
  3746	[37m                                [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[31mstart-pos[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mignore-case[39;49;00m)))))[37m[39;49;00m
  3747	[37m[39;49;00m
  3748	([36mdefun[39;49;00m[37m [39;49;00m[31mbidi-string-mark-left-to-right[39;49;00m[37m [39;49;00m([31mstr[39;49;00m)[37m[39;49;00m
  3749	[37m  [39;49;00m[33m"[39;49;00m[33mReturn a string that can be safely inserted in left-to-right text.[39;49;00m
  3750	[33m[39;49;00m
  3751	[33mNormally, inserting a string with right-to-left (RTL) script into[39;49;00m
  3752	[33ma buffer may cause some subsequent text to be displayed as part[39;49;00m
  3753	[33mof the RTL segment (usually this affects punctuation characters).[39;49;00m
  3754	[33mThis function returns a string which displays as STR but forces[39;49;00m
  3755	[33msubsequent text to be displayed as left-to-right.[39;49;00m
  3756	[33m[39;49;00m
  3757	[33mIf STR contains any RTL character, this function returns a string[39;49;00m
  3758	[33mconsisting of STR followed by an invisible left-to-right mark[39;49;00m
  3759	[33m\([39;49;00m[33mLRM) character.  Otherwise, it returns STR.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3760	[37m  [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m[31mstr[39;49;00m)[37m[39;49;00m
  3761	[37m    [39;49;00m([32msignal[39;49;00m[37m [39;49;00m[33m'wrong-type-argument[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'stringp[39;49;00m[37m [39;49;00m[31mstr[39;49;00m)))[37m[39;49;00m
  3762	[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33mcR[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mstr[39;49;00m)[37m[39;49;00m
  3763	[37m      [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[31mstr[39;49;00m[37m [39;49;00m([32mpropertize[39;49;00m[37m [39;49;00m([32mstring[39;49;00m[37m [39;49;00m[33m?\x[39;49;00m[31m200e[39;49;00m)[37m [39;49;00m[33m'invisible[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m
  3764	[37m    [39;49;00m[31mstr[39;49;00m))[37m[39;49;00m
  3765	[37m[39;49;00m[37m[39;49;00m
  3766	[37m;;;; Specifying things to do later.[39;49;00m[37m[39;49;00m
  3767	[37m[39;49;00m
  3768	([36mdefun[39;49;00m[37m [39;49;00m[31mload-history-regexp[39;49;00m[37m [39;49;00m([31mfile[39;49;00m)[37m[39;49;00m
  3769	[37m  [39;49;00m[33m"[39;49;00m[33mForm a regexp to find FILE in [39;49;00m[33m`load-history'[39;49;00m[33m.[39;49;00m
  3770	[33mFILE, a string, is described in the function [39;49;00m[33m`eval-after-load'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3771	[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mfile-name-absolute-p[39;49;00m[37m [39;49;00m[31mfile[39;49;00m)[37m[39;49;00m
  3772	[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mfile[39;49;00m[37m [39;49;00m([31mfile-truename[39;49;00m[37m [39;49;00m[31mfile[39;49;00m)))[37m[39;49;00m
  3773	[37m  [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mfile-name-absolute-p[39;49;00m[37m [39;49;00m[31mfile[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m`[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m([39;49;00m[33m\\[39;49;00m[33m`[39;49;00m[33m\\[39;49;00m[33m|/[39;49;00m[33m\\[39;49;00m[33m)[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  3774	[37m	  [39;49;00m([32mregexp-quote[39;49;00m[37m [39;49;00m[31mfile[39;49;00m)[37m[39;49;00m
  3775	[37m	  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([31mfile-name-extension[39;49;00m[37m [39;49;00m[31mfile[39;49;00m)[37m[39;49;00m
  3776	[37m	      [39;49;00m[33m"[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3777	[37m	    [39;49;00m[37m;; Note: regexp-opt can't be used here, since we need to call[39;49;00m[37m[39;49;00m
  3778	[37m	    [39;49;00m[37m;; this before Emacs has been fully started.  2006-05-21[39;49;00m[37m[39;49;00m
  3779	[37m	    [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m([39;49;00m[33m"[39;49;00m[37m [39;49;00m([32mmapconcat[39;49;00m[37m [39;49;00m[33m'regexp-quote[39;49;00m[37m [39;49;00m[31mload-suffixes[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m|[39;49;00m[33m"[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m)?[39;49;00m[33m"[39;49;00m))[37m[39;49;00m
  3780	[37m	  [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m([39;49;00m[33m"[39;49;00m[37m [39;49;00m([32mmapconcat[39;49;00m[37m [39;49;00m[33m'regexp-quote[39;49;00m[37m [39;49;00m[31mjka-compr-load-suffixes[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m|[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  3781	[37m	  [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m)?[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m[33m"[39;49;00m))[37m[39;49;00m
  3782	[37m[39;49;00m
  3783	([36mdefun[39;49;00m[37m [39;49;00m[31mload-history-filename-element[39;49;00m[37m [39;49;00m([31mfile-regexp[39;49;00m)[37m[39;49;00m
  3784	[37m  [39;49;00m[33m"[39;49;00m[33mGet the first elt of [39;49;00m[33m`load-history'[39;49;00m[33m whose car matches FILE-REGEXP.[39;49;00m
  3785	[33mReturn nil if there isn't one.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3786	[37m  [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mloads[39;49;00m[37m [39;49;00m[31mload-history[39;49;00m)[37m[39;49;00m
  3787	[37m	 [39;49;00m([31mload-elt[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mloads[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mloads[39;49;00m))))[37m[39;49;00m
  3788	[37m    [39;49;00m([36msave-match-data[39;49;00m[37m[39;49;00m
  3789	[37m      [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mloads[39;49;00m[37m[39;49;00m
  3790	[37m		  [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mload-elt[39;49;00m))[37m[39;49;00m
  3791	[37m		      [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[31mfile-regexp[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mload-elt[39;49;00m)))))[37m[39;49;00m
  3792	[37m	[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mloads[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mloads[39;49;00m)[37m[39;49;00m
  3793	[37m	      [39;49;00m[31mload-elt[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mloads[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mloads[39;49;00m)))))[37m[39;49;00m
  3794	[37m    [39;49;00m[31mload-elt[39;49;00m))[37m[39;49;00m
  3795	[37m[39;49;00m
  3796	([32mput[39;49;00m[37m [39;49;00m[33m'eval-after-load[39;49;00m[37m [39;49;00m[33m'lisp-indent-function[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m[39;49;00m
  3797	([36mdefun[39;49;00m[37m [39;49;00m[31meval-after-load[39;49;00m[37m [39;49;00m([31mfile[39;49;00m[37m [39;49;00m[31mform[39;49;00m)[37m[39;49;00m
  3798	[37m  [39;49;00m[33m"[39;49;00m[33mArrange that if FILE is loaded, FORM will be run immediately afterwards.[39;49;00m
  3799	[33mIf FILE is already loaded, evaluate FORM right now.[39;49;00m
  3800	[33mFORM can be an Elisp expression (in which case it's passed to [39;49;00m[33m`eval'[39;49;00m[33m),[39;49;00m
  3801	[33mor a function (in which case it's passed to [39;49;00m[33m`funcall'[39;49;00m[33m with no argument).[39;49;00m
  3802	[33m[39;49;00m
  3803	[33mIf a matching file is loaded again, FORM will be evaluated again.[39;49;00m
  3804	[33m[39;49;00m
  3805	[33mIf FILE is a string, it may be either an absolute or a relative file[39;49;00m
  3806	[33mname, and may have an extension (e.g. [39;49;00m[33m\"[39;49;00m[33m.el[39;49;00m[33m\"[39;49;00m[33m) or may lack one, and[39;49;00m
  3807	[33madditionally may or may not have an extension denoting a compressed[39;49;00m
  3808	[33mformat (e.g. [39;49;00m[33m\"[39;49;00m[33m.gz[39;49;00m[33m\"[39;49;00m[33m).[39;49;00m
  3809	[33m[39;49;00m
  3810	[33mWhen FILE is absolute, this first converts it to a true name by chasing[39;49;00m
  3811	[33msymbolic links.  Only a file of this name (see next paragraph regarding[39;49;00m
  3812	[33mextensions) will trigger the evaluation of FORM.  When FILE is relative,[39;49;00m
  3813	[33ma file whose absolute true name ends in FILE will trigger evaluation.[39;49;00m
  3814	[33m[39;49;00m
  3815	[33mWhen FILE lacks an extension, a file name with any extension will trigger[39;49;00m
  3816	[33mevaluation.  Otherwise, its extension must match FILE's.  A further[39;49;00m
  3817	[33mextension for a compressed format (e.g. [39;49;00m[33m\"[39;49;00m[33m.gz[39;49;00m[33m\"[39;49;00m[33m) on FILE will not affect[39;49;00m
  3818	[33mthis name matching.[39;49;00m
  3819	[33m[39;49;00m
  3820	[33mAlternatively, FILE can be a feature (i.e. a symbol), in which case FORM[39;49;00m
  3821	[33mis evaluated at the end of any file that [39;49;00m[33m`provide'[39;49;00m[33ms this feature.[39;49;00m
  3822	[33mIf the feature is provided when evaluating code not associated with a[39;49;00m
  3823	[33mfile, FORM is evaluated immediately after the provide statement.[39;49;00m
  3824	[33m[39;49;00m
  3825	[33mUsually FILE is just a library name like [39;49;00m[33m\"[39;49;00m[33mfont-lock[39;49;00m[33m\"[39;49;00m[33m or a feature name[39;49;00m
  3826	[33mlike 'font-lock.[39;49;00m
  3827	[33m[39;49;00m
  3828	[33mThis function makes or adds to an entry on [39;49;00m[33m`after-load-alist'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3829	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mcompiler-macro[39;49;00m[37m[39;49;00m
  3830	[37m            [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31mwhole[39;49;00m)[37m[39;49;00m
  3831	[37m              [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[33m'quote[39;49;00m[37m [39;49;00m([32mcar-safe[39;49;00m[37m [39;49;00m[31mform[39;49;00m))[37m[39;49;00m
  3832	[37m                  [39;49;00m[37m;; Quote with lambda so the compiler can look inside.[39;49;00m[37m[39;49;00m
  3833	[37m                  [39;49;00m`([31meval-after-load[39;49;00m[37m [39;49;00m,[31mfile[39;49;00m[37m [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m()[37m [39;49;00m,([32mnth[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mform[39;49;00m)))[37m[39;49;00m
  3834	[37m                [39;49;00m[31mwhole[39;49;00m))))[37m[39;49;00m
  3835	[37m  [39;49;00m[37m;; Add this FORM into after-load-alist (regardless of whether we'll be[39;49;00m[37m[39;49;00m
  3836	[37m  [39;49;00m[37m;; evaluating it now).[39;49;00m[37m[39;49;00m
  3837	[37m  [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mregexp-or-feature[39;49;00m[37m[39;49;00m
  3838	[37m	  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m[31mfile[39;49;00m)[37m[39;49;00m
  3839	[37m              [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mfile[39;49;00m[37m [39;49;00m([32mpurecopy[39;49;00m[37m [39;49;00m([31mload-history-regexp[39;49;00m[37m [39;49;00m[31mfile[39;49;00m)))[37m[39;49;00m
  3840	[37m            [39;49;00m[31mfile[39;49;00m))[37m[39;49;00m
  3841	[37m	 [39;49;00m([32melt[39;49;00m[37m [39;49;00m([32massoc[39;49;00m[37m [39;49;00m[31mregexp-or-feature[39;49;00m[37m [39;49;00m[31mafter-load-alist[39;49;00m))[37m[39;49;00m
  3842	[37m         [39;49;00m([31mfunc[39;49;00m[37m[39;49;00m
  3843	[37m          [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mfunctionp[39;49;00m[37m [39;49;00m[31mform[39;49;00m)[37m [39;49;00m[31mform[39;49;00m[37m[39;49;00m
  3844	[37m            [39;49;00m[37m;; Try to use the "current" lexical/dynamic mode for `form'.[39;49;00m[37m[39;49;00m
  3845	[37m            [39;49;00m([32meval[39;49;00m[37m [39;49;00m`([36mlambda[39;49;00m[37m [39;49;00m()[37m [39;49;00m,[31mform[39;49;00m)[37m [39;49;00m[31mlexical-binding[39;49;00m))))[37m[39;49;00m
  3846	[37m    [39;49;00m([36munless[39;49;00m[37m [39;49;00m[32melt[39;49;00m[37m[39;49;00m
  3847	[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[32melt[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[31mregexp-or-feature[39;49;00m))[37m[39;49;00m
  3848	[37m      [39;49;00m([36mpush[39;49;00m[37m [39;49;00m[32melt[39;49;00m[37m [39;49;00m[31mafter-load-alist[39;49;00m))[37m[39;49;00m
  3849	[37m    [39;49;00m[37m;; Is there an already loaded file whose name (or `provide' name)[39;49;00m[37m[39;49;00m
  3850	[37m    [39;49;00m[37m;; matches FILE?[39;49;00m[37m[39;49;00m
  3851	[37m    [39;49;00m([34mprog1[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m[31mfile[39;49;00m)[37m[39;49;00m
  3852	[37m		   [39;49;00m([31mload-history-filename-element[39;49;00m[37m [39;49;00m[31mregexp-or-feature[39;49;00m)[37m[39;49;00m
  3853	[37m		 [39;49;00m([36mfeaturep[39;49;00m[37m [39;49;00m[31mfile[39;49;00m))[37m[39;49;00m
  3854	[37m	       [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mfunc[39;49;00m))[37m[39;49;00m
  3855	[37m      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mdelayed-func[39;49;00m[37m[39;49;00m
  3856	[37m             [39;49;00m([34mif[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32msymbolp[39;49;00m[37m [39;49;00m[31mregexp-or-feature[39;49;00m))[37m [39;49;00m[31mfunc[39;49;00m[37m[39;49;00m
  3857	[37m               [39;49;00m[37m;; For features, the after-load-alist elements get run when[39;49;00m[37m[39;49;00m
  3858	[37m               [39;49;00m[37m;; `provide' is called rather than at the end of the file.[39;49;00m[37m[39;49;00m
  3859	[37m               [39;49;00m[37m;; So add an indirection to make sure that `func' is really run[39;49;00m[37m[39;49;00m
  3860	[37m               [39;49;00m[37m;; "after-load" in case the provide call happens early.[39;49;00m[37m[39;49;00m
  3861	[37m               [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m()[37m[39;49;00m
  3862	[37m                 [39;49;00m([34mif[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m[31mload-file-name[39;49;00m)[37m[39;49;00m
  3863	[37m                     [39;49;00m[37m;; Not being provided from a file, run func right now.[39;49;00m[37m[39;49;00m
  3864	[37m                     [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mfunc[39;49;00m)[37m[39;49;00m
  3865	[37m                   [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mlfn[39;49;00m[37m [39;49;00m[31mload-file-name[39;49;00m)[37m[39;49;00m
  3866	[37m                         [39;49;00m[37m;; Don't use letrec, because equal (in[39;49;00m[37m[39;49;00m
  3867	[37m                         [39;49;00m[37m;; add/remove-hook) would get trapped in a cycle.[39;49;00m[37m[39;49;00m
  3868	[37m                         [39;49;00m([31mfun[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33meval-after-load-helper[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m
  3869	[37m                     [39;49;00m([32mfset[39;49;00m[37m [39;49;00m[31mfun[39;49;00m[37m [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31mfile[39;49;00m)[37m[39;49;00m
  3870	[37m                                 [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mequal[39;49;00m[37m [39;49;00m[31mfile[39;49;00m[37m [39;49;00m[31mlfn[39;49;00m)[37m[39;49;00m
  3871	[37m                                   [39;49;00m([31mremove-hook[39;49;00m[37m [39;49;00m[33m'after-load-functions[39;49;00m[37m [39;49;00m[31mfun[39;49;00m)[37m[39;49;00m
  3872	[37m                                   [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mfunc[39;49;00m))))[37m[39;49;00m
  3873	[37m                     [39;49;00m([31madd-hook[39;49;00m[37m [39;49;00m[33m'after-load-functions[39;49;00m[37m [39;49;00m[31mfun[39;49;00m[37m [39;49;00m[33m'append[39;49;00m)))))))[37m[39;49;00m
  3874	[37m        [39;49;00m[37m;; Add FORM to the element unless it's already there.[39;49;00m[37m[39;49;00m
  3875	[37m        [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32mmember[39;49;00m[37m [39;49;00m[31mdelayed-func[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[32melt[39;49;00m))[37m[39;49;00m
  3876	[37m          [39;49;00m([32mnconc[39;49;00m[37m [39;49;00m[32melt[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[31mdelayed-func[39;49;00m)))))))[37m[39;49;00m
  3877	[37m[39;49;00m
  3878	([36mdefmacro[39;49;00m[37m [39;49;00m[36mwith-eval-after-load[39;49;00m[37m [39;49;00m([31mfile[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m
  3879	[37m  [39;49;00m[33m"[39;49;00m[33mExecute BODY after FILE is loaded.[39;49;00m
  3880	[33mFILE is normally a feature name, but it can also be a file name,[39;49;00m
  3881	[33min case that file does not provide any feature.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3882	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m
  3883	[37m  [39;49;00m`([31meval-after-load[39;49;00m[37m [39;49;00m,[31mfile[39;49;00m[37m [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m()[37m [39;49;00m,@[31mbody[39;49;00m)))[37m[39;49;00m
  3884	[37m[39;49;00m
  3885	([34mdefvar[39;49;00m[37m [39;49;00m[31mafter-load-functions[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m
  3886	[37m  [39;49;00m[33m"[39;49;00m[33mSpecial hook run after loading a file.[39;49;00m
  3887	[33mEach function there is called with a single argument, the absolute[39;49;00m
  3888	[33mname of the file just loaded.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  3889	[37m[39;49;00m
  3890	([36mdefun[39;49;00m[37m [39;49;00m[31mdo-after-load-evaluation[39;49;00m[37m [39;49;00m([31mabs-file[39;49;00m)[37m[39;49;00m
  3891	[37m  [39;49;00m[33m"[39;49;00m[33mEvaluate all [39;49;00m[33m`eval-after-load'[39;49;00m[33m forms, if any, for ABS-FILE.[39;49;00m
  3892	[33mABS-FILE, a string, should be the absolute true name of a file just loaded.[39;49;00m
  3893	[33mThis function is called directly from the C code.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3894	[37m  [39;49;00m[37m;; Run the relevant eval-after-load forms.[39;49;00m[37m[39;49;00m
  3895	[37m  [39;49;00m([36mdolist[39;49;00m[37m [39;49;00m([31ma-l-element[39;49;00m[37m [39;49;00m[31mafter-load-alist[39;49;00m)[37m[39;49;00m
  3896	[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31ma-l-element[39;49;00m))[37m[39;49;00m
  3897	[37m               [39;49;00m([31mstring-match-p[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31ma-l-element[39;49;00m)[37m [39;49;00m[31mabs-file[39;49;00m))[37m[39;49;00m
  3898	[37m      [39;49;00m[37m;; discard the file name regexp[39;49;00m[37m[39;49;00m
  3899	[37m      [39;49;00m([32mmapc[39;49;00m[37m [39;49;00m[32m#'[39;49;00m[32mfuncall[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31ma-l-element[39;49;00m))))[37m[39;49;00m
  3900	[37m  [39;49;00m[37m;; Complain when the user uses obsolete files.[39;49;00m[37m[39;49;00m
  3901	[37m  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([36msave-match-data[39;49;00m[37m[39;49;00m
  3902	[37m          [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m/obsolete/[39;49;00m[33m\\[39;49;00m[33m([^/]*[39;49;00m[33m\\[39;49;00m[33m)[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mabs-file[39;49;00m)[37m[39;49;00m
  3903	[37m               [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mequal[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mloaddefs.el[39;49;00m[33m"[39;49;00m[37m [39;49;00m([31mmatch-string[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mabs-file[39;49;00m)))))[37m[39;49;00m
  3904	[37m    [39;49;00m[37m;; Maybe we should just use display-warning?  This seems yucky...[39;49;00m[37m[39;49;00m
  3905	[37m    [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mfile[39;49;00m[37m [39;49;00m([32mfile-name-nondirectory[39;49;00m[37m [39;49;00m[31mabs-file[39;49;00m))[37m[39;49;00m
  3906	[37m	   [39;49;00m([31mmsg[39;49;00m[37m [39;49;00m([32mformat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mPackage %s is obsolete![39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3907	[37m			[39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[31mfile[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m[39;49;00m
  3908	[37m				   [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m.elc?[39;49;00m[33m\\[39;49;00m[33m>[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mfile[39;49;00m)))))[37m[39;49;00m
  3909	[37m      [39;49;00m[37m;; Cribbed from cl--compiling-file.[39;49;00m[37m[39;49;00m
  3910	[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mboundp[39;49;00m[37m [39;49;00m[33m'byte-compile--outbuffer[39;49;00m)[37m[39;49;00m
  3911	[37m	       [39;49;00m([32mbufferp[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[33m'byte-compile--outbuffer[39;49;00m))[37m[39;49;00m
  3912	[37m	       [39;49;00m([32mequal[39;49;00m[37m [39;49;00m([32mbuffer-name[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[33m'byte-compile--outbuffer[39;49;00m))[37m[39;49;00m
  3913	[37m		      [39;49;00m[33m"[39;49;00m[33m *Compiler Output*[39;49;00m[33m"[39;49;00m))[37m[39;49;00m
  3914	[37m	  [39;49;00m[37m;; Don't warn about obsolete files using other obsolete files.[39;49;00m[37m[39;49;00m
  3915	[37m	  [39;49;00m([36munless[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m[31mbyte-compile-current-file[39;49;00m)[37m[39;49;00m
  3916	[37m		       [39;49;00m([31mstring-match-p[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m/obsolete/[^/]*[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3917	[37m				       [39;49;00m([32mexpand-file-name[39;49;00m[37m[39;49;00m
  3918	[37m					[39;49;00m[31mbyte-compile-current-file[39;49;00m[37m[39;49;00m
  3919	[37m					[39;49;00m[31mbyte-compile-root-dir[39;49;00m)))[37m[39;49;00m
  3920	[37m	    [39;49;00m([31mbyte-compile-log-warning[39;49;00m[37m [39;49;00m[31mmsg[39;49;00m))[37m[39;49;00m
  3921	[37m	[39;49;00m([31mrun-with-timer[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m
  3922	[37m			[39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31mmsg[39;49;00m)[37m[39;49;00m
  3923	[37m			  [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m%s[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mmsg[39;49;00m))[37m[39;49;00m
  3924	[37m                        [39;49;00m[31mmsg[39;49;00m))))[37m[39;49;00m
  3925	[37m[39;49;00m
  3926	[37m  [39;49;00m[37m;; Finally, run any other hook.[39;49;00m[37m[39;49;00m
  3927	[37m  [39;49;00m([32mrun-hook-with-args[39;49;00m[37m [39;49;00m[33m'after-load-functions[39;49;00m[37m [39;49;00m[31mabs-file[39;49;00m))[37m[39;49;00m
  3928	[37m[39;49;00m
  3929	([36mdefun[39;49;00m[37m [39;49;00m[31meval-next-after-load[39;49;00m[37m [39;49;00m([31mfile[39;49;00m)[37m[39;49;00m
  3930	[37m  [39;49;00m[33m"[39;49;00m[33mRead the following input sexp, and run it whenever FILE is loaded.[39;49;00m
  3931	[33mThis makes or adds to an entry on [39;49;00m[33m`after-load-alist'[39;49;00m[33m.[39;49;00m
  3932	[33mFILE should be the name of a library, with no directory name.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3933	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mobsolete[39;49;00m[37m [39;49;00m[31meval-after-load[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m))[37m[39;49;00m
  3934	[37m  [39;49;00m([31meval-after-load[39;49;00m[37m [39;49;00m[31mfile[39;49;00m[37m [39;49;00m([32mread[39;49;00m)))[37m[39;49;00m
  3935	[37m[39;49;00m
  3936	[37m[39;49;00m[37m[39;49;00m
  3937	([36mdefun[39;49;00m[37m [39;49;00m[31mdisplay-delayed-warnings[39;49;00m[37m [39;49;00m()[37m[39;49;00m
  3938	[37m  [39;49;00m[33m"[39;49;00m[33mDisplay delayed warnings from [39;49;00m[33m`delayed-warnings-list'[39;49;00m[33m.[39;49;00m
  3939	[33mUsed from [39;49;00m[33m`delayed-warnings-hook'[39;49;00m[33m (which see).[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3940	[37m  [39;49;00m([36mdolist[39;49;00m[37m [39;49;00m([31mwarning[39;49;00m[37m [39;49;00m([32mnreverse[39;49;00m[37m [39;49;00m[31mdelayed-warnings-list[39;49;00m))[37m[39;49;00m
  3941	[37m    [39;49;00m([32mapply[39;49;00m[37m [39;49;00m[33m'display-warning[39;49;00m[37m [39;49;00m[31mwarning[39;49;00m))[37m[39;49;00m
  3942	[37m  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mdelayed-warnings-list[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m
  3943	[37m[39;49;00m
  3944	([36mdefun[39;49;00m[37m [39;49;00m[31mcollapse-delayed-warnings[39;49;00m[37m [39;49;00m()[37m[39;49;00m
  3945	[37m  [39;49;00m[33m"[39;49;00m[33mRemove duplicates from [39;49;00m[33m`delayed-warnings-list'[39;49;00m[33m.[39;49;00m
  3946	[33mCollapse identical adjacent warnings into one (plus count).[39;49;00m
  3947	[33mUsed from [39;49;00m[33m`delayed-warnings-hook'[39;49;00m[33m (which see).[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3948	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mcount[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m[39;49;00m
  3949	[37m        [39;49;00m[31mcollapsed[39;49;00m[37m [39;49;00m[31mwarning[39;49;00m)[37m[39;49;00m
  3950	[37m    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m[31mdelayed-warnings-list[39;49;00m[37m[39;49;00m
  3951	[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mwarning[39;49;00m[37m [39;49;00m([36mpop[39;49;00m[37m [39;49;00m[31mdelayed-warnings-list[39;49;00m))[37m[39;49;00m
  3952	[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mequal[39;49;00m[37m [39;49;00m[31mwarning[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mdelayed-warnings-list[39;49;00m))[37m[39;49;00m
  3953	[37m          [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mcount[39;49;00m[37m [39;49;00m([32m1+[39;49;00m[37m [39;49;00m[31mcount[39;49;00m))[37m[39;49;00m
  3954	[37m        [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m[31mcount[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m[39;49;00m
  3955	[37m          [39;49;00m([32msetcdr[39;49;00m[37m [39;49;00m[31mwarning[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m([32mformat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m%s [%d times][39;49;00m[33m"[39;49;00m[37m [39;49;00m([31mcadr[39;49;00m[37m [39;49;00m[31mwarning[39;49;00m)[37m [39;49;00m[31mcount[39;49;00m)[37m[39;49;00m
  3956	[37m                                [39;49;00m([31mcddr[39;49;00m[37m [39;49;00m[31mwarning[39;49;00m)))[37m[39;49;00m
  3957	[37m          [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mcount[39;49;00m[37m [39;49;00m[34m1[39;49;00m))[37m[39;49;00m
  3958	[37m        [39;49;00m([36mpush[39;49;00m[37m [39;49;00m[31mwarning[39;49;00m[37m [39;49;00m[31mcollapsed[39;49;00m)))[37m[39;49;00m
  3959	[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mdelayed-warnings-list[39;49;00m[37m [39;49;00m([32mnreverse[39;49;00m[37m [39;49;00m[31mcollapsed[39;49;00m))))[37m[39;49;00m
  3960	[37m[39;49;00m
  3961	[37m;; At present this is only used for Emacs internals.[39;49;00m[37m[39;49;00m
  3962	[37m;; Ref http://lists.gnu.org/archive/html/emacs-devel/2012-02/msg00085.html[39;49;00m[37m[39;49;00m
  3963	([34mdefvar[39;49;00m[37m [39;49;00m[31mdelayed-warnings-hook[39;49;00m[37m [39;49;00m'([31mcollapse-delayed-warnings[39;49;00m[37m[39;49;00m
  3964	[37m                                [39;49;00m[31mdisplay-delayed-warnings[39;49;00m)[37m[39;49;00m
  3965	[37m  [39;49;00m[33m"[39;49;00m[33mNormal hook run to process and display delayed warnings.[39;49;00m
  3966	[33mBy default, this hook contains functions to consolidate the[39;49;00m
  3967	[33mwarnings listed in [39;49;00m[33m`delayed-warnings-list'[39;49;00m[33m, display them, and set[39;49;00m
  3968	[33m`delayed-warnings-list'[39;49;00m[33m back to nil.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  3969	[37m[39;49;00m
  3970	([36mdefun[39;49;00m[37m [39;49;00m[31mdelay-warning[39;49;00m[37m [39;49;00m([31mtype[39;49;00m[37m [39;49;00m[32mmessage[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mlevel[39;49;00m[37m [39;49;00m[32mbuffer-name[39;49;00m)[37m[39;49;00m
  3971	[37m  [39;49;00m[33m"[39;49;00m[33mDisplay a delayed warning.[39;49;00m
  3972	[33mAside from going through [39;49;00m[33m`delayed-warnings-list'[39;49;00m[33m, this is equivalent[39;49;00m
  3973	[33mto [39;49;00m[33m`display-warning'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3974	[37m  [39;49;00m([36mpush[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[31mtype[39;49;00m[37m [39;49;00m[32mmessage[39;49;00m[37m [39;49;00m[31mlevel[39;49;00m[37m [39;49;00m[32mbuffer-name[39;49;00m)[37m [39;49;00m[31mdelayed-warnings-list[39;49;00m))[37m[39;49;00m
  3975	[37m[39;49;00m
  3976	[37m[39;49;00m[37m[39;49;00m
  3977	[37m;;;; invisibility specs[39;49;00m[37m[39;49;00m
  3978	[37m[39;49;00m
  3979	([36mdefun[39;49;00m[37m [39;49;00m[31madd-to-invisibility-spec[39;49;00m[37m [39;49;00m([31melement[39;49;00m)[37m[39;49;00m
  3980	[37m  [39;49;00m[33m"[39;49;00m[33mAdd ELEMENT to [39;49;00m[33m`buffer-invisibility-spec'[39;49;00m[33m.[39;49;00m
  3981	[33mSee documentation for [39;49;00m[33m`buffer-invisibility-spec'[39;49;00m[33m for the kind of elements[39;49;00m
  3982	[33mthat can be added.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3983	[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mbuffer-invisibility-spec[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m
  3984	[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbuffer-invisibility-spec[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[31mt[39;49;00m)))[37m[39;49;00m
  3985	[37m  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbuffer-invisibility-spec[39;49;00m[37m[39;49;00m
  3986	[37m	[39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31melement[39;49;00m[37m [39;49;00m[31mbuffer-invisibility-spec[39;49;00m)))[37m[39;49;00m
  3987	[37m[39;49;00m
  3988	([36mdefun[39;49;00m[37m [39;49;00m[31mremove-from-invisibility-spec[39;49;00m[37m [39;49;00m([31melement[39;49;00m)[37m[39;49;00m
  3989	[37m  [39;49;00m[33m"[39;49;00m[33mRemove ELEMENT from [39;49;00m[33m`buffer-invisibility-spec'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  3990	[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mbuffer-invisibility-spec[39;49;00m)[37m[39;49;00m
  3991	[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbuffer-invisibility-spec[39;49;00m[37m[39;49;00m
  3992	[37m	    [39;49;00m([32mdelete[39;49;00m[37m [39;49;00m[31melement[39;49;00m[37m [39;49;00m[31mbuffer-invisibility-spec[39;49;00m))))[37m[39;49;00m
  3993	[37m[39;49;00m[37m[39;49;00m
  3994	[37m;;;; Syntax tables.[39;49;00m[37m[39;49;00m
  3995	[37m[39;49;00m
  3996	([36mdefmacro[39;49;00m[37m [39;49;00m[36mwith-syntax-table[39;49;00m[37m [39;49;00m([31mtable[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m
  3997	[37m  [39;49;00m[33m"[39;49;00m[33mEvaluate BODY with syntax table of current buffer set to TABLE.[39;49;00m
  3998	[33mThe syntax table of the current buffer is saved, BODY is evaluated, and the[39;49;00m
  3999	[33msaved table is restored, even in case of an abnormal exit.[39;49;00m
  4000	[33mValue is what BODY returns.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  4001	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m1[39;49;00m))[37m[39;49;00m
  4002	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mold-table[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mtable[39;49;00m[33m"[39;49;00m))[37m[39;49;00m
  4003	[37m	[39;49;00m([31mold-buffer[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mbuffer[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m
  4004	[37m    [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m((,[31mold-table[39;49;00m[37m [39;49;00m([32msyntax-table[39;49;00m))[37m[39;49;00m
  4005	[37m	   [39;49;00m(,[31mold-buffer[39;49;00m[37m [39;49;00m([32mcurrent-buffer[39;49;00m)))[37m[39;49;00m
  4006	[37m       [39;49;00m([34munwind-protect[39;49;00m[37m[39;49;00m
  4007	[37m	   [39;49;00m([34mprogn[39;49;00m[37m[39;49;00m
  4008	[37m	     [39;49;00m([32mset-syntax-table[39;49;00m[37m [39;49;00m,[31mtable[39;49;00m)[37m[39;49;00m
  4009	[37m	     [39;49;00m,@[31mbody[39;49;00m)[37m[39;49;00m
  4010	[37m	 [39;49;00m([34msave-current-buffer[39;49;00m[37m[39;49;00m
  4011	[37m	   [39;49;00m([32mset-buffer[39;49;00m[37m [39;49;00m,[31mold-buffer[39;49;00m)[37m[39;49;00m
  4012	[37m	   [39;49;00m([32mset-syntax-table[39;49;00m[37m [39;49;00m,[31mold-table[39;49;00m))))))[37m[39;49;00m
  4013	[37m[39;49;00m
  4014	([36mdefun[39;49;00m[37m [39;49;00m[31mmake-syntax-table[39;49;00m[37m [39;49;00m([34m&optional[39;49;00m[37m [39;49;00m[31moldtable[39;49;00m)[37m[39;49;00m
  4015	[37m  [39;49;00m[33m"[39;49;00m[33mReturn a new syntax table.[39;49;00m
  4016	[33mCreate a syntax table which inherits from OLDTABLE (if non-nil) or[39;49;00m
  4017	[33mfrom [39;49;00m[33m`standard-syntax-table'[39;49;00m[33m otherwise.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  4018	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtable[39;49;00m[37m [39;49;00m([32mmake-char-table[39;49;00m[37m [39;49;00m[33m'syntax-table[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)))[37m[39;49;00m
  4019	[37m    [39;49;00m([32mset-char-table-parent[39;49;00m[37m [39;49;00m[31mtable[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31moldtable[39;49;00m[37m [39;49;00m([32mstandard-syntax-table[39;49;00m)))[37m[39;49;00m
  4020	[37m    [39;49;00m[31mtable[39;49;00m))[37m[39;49;00m
  4021	[37m[39;49;00m
  4022	([36mdefun[39;49;00m[37m [39;49;00m[31msyntax-after[39;49;00m[37m [39;49;00m([31mpos[39;49;00m)[37m[39;49;00m
  4023	[37m  [39;49;00m[33m"[39;49;00m[33mReturn the raw syntax descriptor for the char after POS.[39;49;00m
  4024	[33mIf POS is outside the buffer's accessible portion, return nil.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  4025	[37m  [39;49;00m([36munless[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m[31mpos[39;49;00m[37m [39;49;00m([32mpoint-min[39;49;00m))[37m [39;49;00m([32m>=[39;49;00m[37m [39;49;00m[31mpos[39;49;00m[37m [39;49;00m([32mpoint-max[39;49;00m)))[37m[39;49;00m
  4026	[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mst[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mparse-sexp-lookup-properties[39;49;00m[37m[39;49;00m
  4027	[37m		  [39;49;00m([32mget-char-property[39;49;00m[37m [39;49;00m[31mpos[39;49;00m[37m [39;49;00m[33m'syntax-table[39;49;00m))))[37m[39;49;00m
  4028	[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mst[39;49;00m)[37m [39;49;00m[31mst[39;49;00m[37m[39;49;00m
  4029	[37m	[39;49;00m([32maref[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mst[39;49;00m[37m [39;49;00m([32msyntax-table[39;49;00m))[37m [39;49;00m([32mchar-after[39;49;00m[37m [39;49;00m[31mpos[39;49;00m))))))[37m[39;49;00m
  4030	[37m[39;49;00m
  4031	([36mdefun[39;49;00m[37m [39;49;00m[31msyntax-class[39;49;00m[37m [39;49;00m([31msyntax[39;49;00m)[37m[39;49;00m
  4032	[37m  [39;49;00m[33m"[39;49;00m[33mReturn the code for the syntax class described by SYNTAX.[39;49;00m
  4033	[33m[39;49;00m
  4034	[33mSYNTAX should be a raw syntax descriptor; the return value is a[39;49;00m
  4035	[33minteger which encodes the corresponding syntax class.  See Info[39;49;00m
  4036	[33mnode [39;49;00m[33m`[39;49;00m[33m(elisp)Syntax Table Internals' for a list of codes.[39;49;00m
  4037	[33m[39;49;00m
  4038	[33mIf SYNTAX is nil, return nil.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  4039	[37m  [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31msyntax[39;49;00m[37m [39;49;00m([32mlogand[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31msyntax[39;49;00m)[37m [39;49;00m[34m65535[39;49;00m)))[37m[39;49;00m
  4040	[37m[39;49;00m[37m[39;49;00m
  4041	[37m;; Utility motion commands[39;49;00m[37m[39;49;00m
  4042	[37m[39;49;00m
  4043	[37m;;  Whitespace[39;49;00m[37m[39;49;00m
  4044	[37m[39;49;00m
  4045	([36mdefun[39;49;00m[37m [39;49;00m[31mforward-whitespace[39;49;00m[37m [39;49;00m([31marg[39;49;00m)[37m[39;49;00m
  4046	[37m  [39;49;00m[33m"[39;49;00m[33mMove point to the end of the next sequence of whitespace chars.[39;49;00m
  4047	[33mEach such sequence may be a single newline, or a sequence of[39;49;00m
  4048	[33mconsecutive space and/or tab characters.[39;49;00m
  4049	[33mWith prefix argument ARG, do it ARG times if positive, or move[39;49;00m
  4050	[33mbackwards ARG times if negative.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  4051	[37m  [39;49;00m([34minteractive[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m^p[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  4052	[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mnatnump[39;49;00m[37m [39;49;00m[31marg[39;49;00m)[37m[39;49;00m
  4053	[37m      [39;49;00m([32mre-search-forward[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m[ [39;49;00m[33m\t[39;49;00m[33m]+[39;49;00m[33m\\[39;49;00m[33m|[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[33m'move[39;49;00m[37m [39;49;00m[31marg[39;49;00m)[37m[39;49;00m
  4054	[37m    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m[31marg[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m
  4055	[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mre-search-backward[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m[ [39;49;00m[33m\t[39;49;00m[33m]+[39;49;00m[33m\\[39;49;00m[33m|[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[33m'move[39;49;00m)[37m[39;49;00m
  4056	[37m	  [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mchar-after[39;49;00m[37m [39;49;00m([32mmatch-beginning[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m [39;49;00m[33m?\n[39;49;00m)[37m[39;49;00m
  4057	[37m	      [39;49;00m([32mskip-chars-backward[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m [39;49;00m[33m\t[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m
  4058	[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31marg[39;49;00m[37m [39;49;00m([32m1+[39;49;00m[37m [39;49;00m[31marg[39;49;00m)))))[37m[39;49;00m
  4059	[37m[39;49;00m
  4060	[37m;;  Symbols[39;49;00m[37m[39;49;00m
  4061	[37m[39;49;00m
  4062	([36mdefun[39;49;00m[37m [39;49;00m[31mforward-symbol[39;49;00m[37m [39;49;00m([31marg[39;49;00m)[37m[39;49;00m
  4063	[37m  [39;49;00m[33m"[39;49;00m[33mMove point to the next position that is the end of a symbol.[39;49;00m
  4064	[33mA symbol is any sequence of characters that are in either the[39;49;00m
  4065	[33mword constituent or symbol constituent syntax class.[39;49;00m
  4066	[33mWith prefix argument ARG, do it ARG times if positive, or move[39;49;00m
  4067	[33mbackwards ARG times if negative.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  4068	[37m  [39;49;00m([34minteractive[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m^p[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  4069	[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mnatnump[39;49;00m[37m [39;49;00m[31marg[39;49;00m)[37m[39;49;00m
  4070	[37m      [39;49;00m([32mre-search-forward[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m([39;49;00m[33m\\[39;49;00m[33msw[39;49;00m[33m\\[39;49;00m[33m|[39;49;00m[33m\\[39;49;00m[33ms_[39;49;00m[33m\\[39;49;00m[33m)+[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[33m'move[39;49;00m[37m [39;49;00m[31marg[39;49;00m)[37m[39;49;00m
  4071	[37m    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m[31marg[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m
  4072	[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mre-search-backward[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m([39;49;00m[33m\\[39;49;00m[33msw[39;49;00m[33m\\[39;49;00m[33m|[39;49;00m[33m\\[39;49;00m[33ms_[39;49;00m[33m\\[39;49;00m[33m)+[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[33m'move[39;49;00m)[37m[39;49;00m
  4073	[37m	  [39;49;00m([32mskip-syntax-backward[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mw_[39;49;00m[33m"[39;49;00m))[37m[39;49;00m
  4074	[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31marg[39;49;00m[37m [39;49;00m([32m1+[39;49;00m[37m [39;49;00m[31marg[39;49;00m)))))[37m[39;49;00m
  4075	[37m[39;49;00m
  4076	[37m;;  Syntax blocks[39;49;00m[37m[39;49;00m
  4077	[37m[39;49;00m
  4078	([36mdefun[39;49;00m[37m [39;49;00m[31mforward-same-syntax[39;49;00m[37m [39;49;00m([34m&optional[39;49;00m[37m [39;49;00m[31marg[39;49;00m)[37m[39;49;00m
  4079	[37m  [39;49;00m[33m"[39;49;00m[33mMove point past all characters with the same syntax class.[39;49;00m
  4080	[33mWith prefix argument ARG, do it ARG times if positive, or move[39;49;00m
  4081	[33mbackwards ARG times if negative.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  4082	[37m  [39;49;00m([34minteractive[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m^p[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  4083	[37m  [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31marg[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31marg[39;49;00m[37m [39;49;00m[34m1[39;49;00m))[37m[39;49;00m
  4084	[37m  [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m[31marg[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m
  4085	[37m    [39;49;00m([32mskip-syntax-backward[39;49;00m[37m[39;49;00m
  4086	[37m     [39;49;00m([32mchar-to-string[39;49;00m[37m [39;49;00m([32mchar-syntax[39;49;00m[37m [39;49;00m([32mchar-before[39;49;00m))))[37m[39;49;00m
  4087	[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31marg[39;49;00m[37m [39;49;00m([32m1+[39;49;00m[37m [39;49;00m[31marg[39;49;00m)))[37m[39;49;00m
  4088	[37m  [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m[31marg[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m
  4089	[37m    [39;49;00m([32mskip-syntax-forward[39;49;00m[37m [39;49;00m([32mchar-to-string[39;49;00m[37m [39;49;00m([32mchar-syntax[39;49;00m[37m [39;49;00m([32mchar-after[39;49;00m))))[37m[39;49;00m
  4090	[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31marg[39;49;00m[37m [39;49;00m([32m1-[39;49;00m[37m [39;49;00m[31marg[39;49;00m))))[37m[39;49;00m
  4091	[37m[39;49;00m
  4092	[37m[39;49;00m[37m[39;49;00m
  4093	[37m;;;; Text clones[39;49;00m[37m[39;49;00m
  4094	[37m[39;49;00m
  4095	([34mdefvar[39;49;00m[37m [39;49;00m[31mtext-clone--maintaining[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m
  4096	[37m[39;49;00m
  4097	([36mdefun[39;49;00m[37m [39;49;00m[31mtext-clone--maintain[39;49;00m[37m [39;49;00m([31mol1[39;49;00m[37m [39;49;00m[31mafter[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31m_len[39;49;00m)[37m[39;49;00m
  4098	[37m  [39;49;00m[33m"[39;49;00m[33mPropagate the changes made under the overlay OL1 to the other clones.[39;49;00m
  4099	[33mThis is used on the [39;49;00m[33m`modification-hooks'[39;49;00m[33m property of text clones.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  4100	[37m  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mafter[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m[31mundo-in-progress[39;49;00m)[37m[39;49;00m
  4101	[37m             [39;49;00m([31mnot[39;49;00m[37m [39;49;00m[31mtext-clone--maintaining[39;49;00m)[37m[39;49;00m
  4102	[37m             [39;49;00m([32moverlay-start[39;49;00m[37m [39;49;00m[31mol1[39;49;00m))[37m[39;49;00m
  4103	[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mmargin[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32moverlay-get[39;49;00m[37m [39;49;00m[31mol1[39;49;00m[37m [39;49;00m[33m'text-clone-spreadp[39;49;00m)[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[34m0[39;49;00m)))[37m[39;49;00m
  4104	[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m[37m [39;49;00m([32mmax[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m[37m [39;49;00m([32m+[39;49;00m[37m [39;49;00m([32moverlay-start[39;49;00m[37m [39;49;00m[31mol1[39;49;00m)[37m [39;49;00m[31mmargin[39;49;00m)))[37m[39;49;00m
  4105	[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m([32mmin[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m([32moverlay-end[39;49;00m[37m [39;49;00m[31mol1[39;49;00m)[37m [39;49;00m[31mmargin[39;49;00m)))[37m[39;49;00m
  4106	[37m      [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32m<=[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m[37m [39;49;00m[31mend[39;49;00m)[37m[39;49;00m
  4107	[37m	[39;49;00m([34msave-excursion[39;49;00m[37m[39;49;00m
  4108	[37m	  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32moverlay-get[39;49;00m[37m [39;49;00m[31mol1[39;49;00m[37m [39;49;00m[33m'text-clone-syntax[39;49;00m)[37m[39;49;00m
  4109	[37m	    [39;49;00m[37m;; Check content of the clone's text.[39;49;00m[37m[39;49;00m
  4110	[37m	    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mcbeg[39;49;00m[37m [39;49;00m([32m+[39;49;00m[37m [39;49;00m([32moverlay-start[39;49;00m[37m [39;49;00m[31mol1[39;49;00m)[37m [39;49;00m[31mmargin[39;49;00m))[37m[39;49;00m
  4111	[37m		  [39;49;00m([31mcend[39;49;00m[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m([32moverlay-end[39;49;00m[37m [39;49;00m[31mol1[39;49;00m)[37m [39;49;00m[31mmargin[39;49;00m)))[37m[39;49;00m
  4112	[37m	      [39;49;00m([32mgoto-char[39;49;00m[37m [39;49;00m[31mcbeg[39;49;00m)[37m[39;49;00m
  4113	[37m	      [39;49;00m([36msave-match-data[39;49;00m[37m[39;49;00m
  4114	[37m		[39;49;00m([34mif[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mre-search-forward[39;49;00m[37m[39;49;00m
  4115	[37m			  [39;49;00m([32moverlay-get[39;49;00m[37m [39;49;00m[31mol1[39;49;00m[37m [39;49;00m[33m'text-clone-syntax[39;49;00m)[37m [39;49;00m[31mcend[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m
  4116	[37m		    [39;49;00m[37m;; Mark the overlay for deletion.[39;49;00m[37m[39;49;00m
  4117	[37m		    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[31mcbeg[39;49;00m)[37m[39;49;00m
  4118	[37m		  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m([32mmatch-end[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[31mcend[39;49;00m)[37m[39;49;00m
  4119	[37m		    [39;49;00m[37m;; Shrink the clone at its end.[39;49;00m[37m[39;49;00m
  4120	[37m		    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m([32mmin[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m([32mmatch-end[39;49;00m[37m [39;49;00m[34m0[39;49;00m)))[37m[39;49;00m
  4121	[37m		    [39;49;00m([32mmove-overlay[39;49;00m[37m [39;49;00m[31mol1[39;49;00m[37m [39;49;00m([32moverlay-start[39;49;00m[37m [39;49;00m[31mol1[39;49;00m)[37m[39;49;00m
  4122	[37m				  [39;49;00m([32m+[39;49;00m[37m [39;49;00m([32mmatch-end[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[31mmargin[39;49;00m)))[37m[39;49;00m
  4123	[37m		  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m([32mmatch-beginning[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[31mcbeg[39;49;00m)[37m[39;49;00m
  4124	[37m		    [39;49;00m[37m;; Shrink the clone at its beginning.[39;49;00m[37m[39;49;00m
  4125	[37m		    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m[37m [39;49;00m([32mmax[39;49;00m[37m [39;49;00m([32mmatch-beginning[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[31mbeg[39;49;00m))[37m[39;49;00m
  4126	[37m		    [39;49;00m([32mmove-overlay[39;49;00m[37m [39;49;00m[31mol1[39;49;00m[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m([32mmatch-beginning[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[31mmargin[39;49;00m)[37m[39;49;00m
  4127	[37m				  [39;49;00m([32moverlay-end[39;49;00m[37m [39;49;00m[31mol1[39;49;00m)))))))[37m[39;49;00m
  4128	[37m	  [39;49;00m[37m;; Now go ahead and update the clones.[39;49;00m[37m[39;49;00m
  4129	[37m	  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mhead[39;49;00m[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m[37m [39;49;00m([32moverlay-start[39;49;00m[37m [39;49;00m[31mol1[39;49;00m)))[37m[39;49;00m
  4130	[37m		[39;49;00m([31mtail[39;49;00m[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m([32moverlay-end[39;49;00m[37m [39;49;00m[31mol1[39;49;00m)[37m [39;49;00m[31mend[39;49;00m))[37m[39;49;00m
  4131	[37m		[39;49;00m([31mstr[39;49;00m[37m [39;49;00m([32mbuffer-substring[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m[37m [39;49;00m[31mend[39;49;00m))[37m[39;49;00m
  4132	[37m		[39;49;00m([31mnothing-left[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m
  4133	[37m		[39;49;00m([31mtext-clone--maintaining[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m
  4134	[37m	    [39;49;00m([36mdolist[39;49;00m[37m [39;49;00m([31mol2[39;49;00m[37m [39;49;00m([32moverlay-get[39;49;00m[37m [39;49;00m[31mol1[39;49;00m[37m [39;49;00m[33m'text-clones[39;49;00m))[37m[39;49;00m
  4135	[37m	      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31moe[39;49;00m[37m [39;49;00m([32moverlay-end[39;49;00m[37m [39;49;00m[31mol2[39;49;00m)))[37m[39;49;00m
  4136	[37m		[39;49;00m([36munless[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mol1[39;49;00m[37m [39;49;00m[31mol2[39;49;00m)[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[31moe[39;49;00m))[37m[39;49;00m
  4137	[37m		  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mnothing-left[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m
  4138	[37m		  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mmod-beg[39;49;00m[37m [39;49;00m([32m+[39;49;00m[37m [39;49;00m([32moverlay-start[39;49;00m[37m [39;49;00m[31mol2[39;49;00m)[37m [39;49;00m[31mhead[39;49;00m)))[37m[39;49;00m
  4139	[37m		    [39;49;00m[37m;;(overlay-put ol2 'modification-hooks nil)[39;49;00m[37m[39;49;00m
  4140	[37m		    [39;49;00m([32mgoto-char[39;49;00m[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m([32moverlay-end[39;49;00m[37m [39;49;00m[31mol2[39;49;00m)[37m [39;49;00m[31mtail[39;49;00m))[37m[39;49;00m
  4141	[37m		    [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m[31mmod-beg[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m))[37m[39;49;00m
  4142	[37m		      [39;49;00m([34msave-excursion[39;49;00m[37m [39;49;00m([32minsert[39;49;00m[37m [39;49;00m[31mstr[39;49;00m))[37m[39;49;00m
  4143	[37m		      [39;49;00m([32mdelete-region[39;49;00m[37m [39;49;00m[31mmod-beg[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m)))[37m[39;49;00m
  4144	[37m		    [39;49;00m[37m;;(overlay-put ol2 'modification-hooks '(text-clone--maintain))[39;49;00m[37m[39;49;00m
  4145	[37m		    [39;49;00m))))[37m[39;49;00m
  4146	[37m	    [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mnothing-left[39;49;00m[37m [39;49;00m([32mdelete-overlay[39;49;00m[37m [39;49;00m[31mol1[39;49;00m))))))))[37m[39;49;00m
  4147	[37m[39;49;00m
  4148	([36mdefun[39;49;00m[37m [39;49;00m[31mtext-clone-create[39;49;00m[37m [39;49;00m([31mstart[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mspreadp[39;49;00m[37m [39;49;00m[31msyntax[39;49;00m)[37m[39;49;00m
  4149	[37m  [39;49;00m[33m"[39;49;00m[33mCreate a text clone of START...END at point.[39;49;00m
  4150	[33mText clones are chunks of text that are automatically kept identical:[39;49;00m
  4151	[33mchanges done to one of the clones will be immediately propagated to the other.[39;49;00m
  4152	[33m[39;49;00m
  4153	[33mThe buffer's content at point is assumed to be already identical to[39;49;00m
  4154	[33mthe one between START and END.[39;49;00m
  4155	[33mIf SYNTAX is provided it's a regexp that describes the possible text of[39;49;00m
  4156	[33mthe clones; the clone will be shrunk or killed if necessary to ensure that[39;49;00m
  4157	[33mits text matches the regexp.[39;49;00m
  4158	[33mIf SPREADP is non-nil it indicates that text inserted before/after the[39;49;00m
  4159	[33mclone should be incorporated in the clone.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  4160	[37m  [39;49;00m[37m;; To deal with SPREADP we can either use an overlay with `nil t' along[39;49;00m[37m[39;49;00m
  4161	[37m  [39;49;00m[37m;; with insert-(behind|in-front-of)-hooks or use a slightly larger overlay[39;49;00m[37m[39;49;00m
  4162	[37m  [39;49;00m[37m;; (with a one-char margin at each end) with `t nil'.[39;49;00m[37m[39;49;00m
  4163	[37m  [39;49;00m[37m;; We opted for a larger overlay because it behaves better in the case[39;49;00m[37m[39;49;00m
  4164	[37m  [39;49;00m[37m;; where the clone is reduced to the empty string (we want the overlay to[39;49;00m[37m[39;49;00m
  4165	[37m  [39;49;00m[37m;; stay when the clone's content is the empty string and we want to use[39;49;00m[37m[39;49;00m
  4166	[37m  [39;49;00m[37m;; `evaporate' to make sure those overlays get deleted when needed).[39;49;00m[37m[39;49;00m
  4167	[37m  [39;49;00m[37m;;[39;49;00m[37m[39;49;00m
  4168	[37m  [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mpt-end[39;49;00m[37m [39;49;00m([32m+[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m)[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[31mstart[39;49;00m)))[37m[39;49;00m
  4169	[37m  	 [39;49;00m([31mstart-margin[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m[31mspreadp[39;49;00m)[37m [39;49;00m([32mbobp[39;49;00m)[37m [39;49;00m([32m<=[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m([32mpoint-min[39;49;00m)))[37m[39;49;00m
  4170	[37m			   [39;49;00m[34m0[39;49;00m[37m [39;49;00m[34m1[39;49;00m))[37m[39;49;00m
  4171	[37m  	 [39;49;00m([31mend-margin[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m[31mspreadp[39;49;00m)[37m[39;49;00m
  4172	[37m			     [39;49;00m([32m>=[39;49;00m[37m [39;49;00m[31mpt-end[39;49;00m[37m [39;49;00m([32mpoint-max[39;49;00m))[37m[39;49;00m
  4173	[37m  			     [39;49;00m([32m>=[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m([32mpoint-max[39;49;00m)))[37m[39;49;00m
  4174	[37m  			 [39;49;00m[34m0[39;49;00m[37m [39;49;00m[34m1[39;49;00m))[37m[39;49;00m
  4175	[37m         [39;49;00m[37m;; FIXME: Reuse overlays at point to extend dups![39;49;00m[37m[39;49;00m
  4176	[37m  	 [39;49;00m([31mol1[39;49;00m[37m [39;49;00m([32mmake-overlay[39;49;00m[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mstart-margin[39;49;00m)[37m [39;49;00m([32m+[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[31mend-margin[39;49;00m)[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m
  4177	[37m  	 [39;49;00m([31mol2[39;49;00m[37m [39;49;00m([32mmake-overlay[39;49;00m[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m)[37m [39;49;00m[31mstart-margin[39;49;00m)[37m [39;49;00m([32m+[39;49;00m[37m [39;49;00m[31mpt-end[39;49;00m[37m [39;49;00m[31mend-margin[39;49;00m)[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m
  4178	[37m	 [39;49;00m([31mdups[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[31mol1[39;49;00m[37m [39;49;00m[31mol2[39;49;00m)))[37m[39;49;00m
  4179	[37m    [39;49;00m([32moverlay-put[39;49;00m[37m [39;49;00m[31mol1[39;49;00m[37m [39;49;00m[33m'modification-hooks[39;49;00m[37m [39;49;00m'([31mtext-clone--maintain[39;49;00m))[37m[39;49;00m
  4180	[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31mspreadp[39;49;00m[37m [39;49;00m([32moverlay-put[39;49;00m[37m [39;49;00m[31mol1[39;49;00m[37m [39;49;00m[33m'text-clone-spreadp[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m
  4181	[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31msyntax[39;49;00m[37m [39;49;00m([32moverlay-put[39;49;00m[37m [39;49;00m[31mol1[39;49;00m[37m [39;49;00m[33m'text-clone-syntax[39;49;00m[37m [39;49;00m[31msyntax[39;49;00m))[37m[39;49;00m
  4182	[37m    [39;49;00m[37m;;(overlay-put ol1 'face 'underline)[39;49;00m[37m[39;49;00m
  4183	[37m    [39;49;00m([32moverlay-put[39;49;00m[37m [39;49;00m[31mol1[39;49;00m[37m [39;49;00m[33m'evaporate[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m
  4184	[37m    [39;49;00m([32moverlay-put[39;49;00m[37m [39;49;00m[31mol1[39;49;00m[37m [39;49;00m[33m'text-clones[39;49;00m[37m [39;49;00m[31mdups[39;49;00m)[37m[39;49;00m
  4185	[37m    [39;49;00m[37m;;[39;49;00m[37m[39;49;00m
  4186	[37m    [39;49;00m([32moverlay-put[39;49;00m[37m [39;49;00m[31mol2[39;49;00m[37m [39;49;00m[33m'modification-hooks[39;49;00m[37m [39;49;00m'([31mtext-clone--maintain[39;49;00m))[37m[39;49;00m
  4187	[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31mspreadp[39;49;00m[37m [39;49;00m([32moverlay-put[39;49;00m[37m [39;49;00m[31mol2[39;49;00m[37m [39;49;00m[33m'text-clone-spreadp[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m
  4188	[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31msyntax[39;49;00m[37m [39;49;00m([32moverlay-put[39;49;00m[37m [39;49;00m[31mol2[39;49;00m[37m [39;49;00m[33m'text-clone-syntax[39;49;00m[37m [39;49;00m[31msyntax[39;49;00m))[37m[39;49;00m
  4189	[37m    [39;49;00m[37m;;(overlay-put ol2 'face 'underline)[39;49;00m[37m[39;49;00m
  4190	[37m    [39;49;00m([32moverlay-put[39;49;00m[37m [39;49;00m[31mol2[39;49;00m[37m [39;49;00m[33m'evaporate[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m
  4191	[37m    [39;49;00m([32moverlay-put[39;49;00m[37m [39;49;00m[31mol2[39;49;00m[37m [39;49;00m[33m'text-clones[39;49;00m[37m [39;49;00m[31mdups[39;49;00m)))[37m[39;49;00m
  4192	[37m[39;49;00m[37m[39;49;00m
  4193	[37m;;;; Mail user agents.[39;49;00m[37m[39;49;00m
  4194	[37m[39;49;00m
  4195	[37m;; Here we include just enough for other packages to be able[39;49;00m[37m[39;49;00m
  4196	[37m;; to define them.[39;49;00m[37m[39;49;00m
  4197	[37m[39;49;00m
  4198	([36mdefun[39;49;00m[37m [39;49;00m[31mdefine-mail-user-agent[39;49;00m[37m [39;49;00m([31msymbol[39;49;00m[37m [39;49;00m[31mcomposefunc[39;49;00m[37m [39;49;00m[31msendfunc[39;49;00m[37m[39;49;00m
  4199	[37m				      [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mabortfunc[39;49;00m[37m [39;49;00m[31mhookvar[39;49;00m)[37m[39;49;00m
  4200	[37m  [39;49;00m[33m"[39;49;00m[33mDefine a symbol to identify a mail-sending package for [39;49;00m[33m`mail-user-agent'[39;49;00m[33m.[39;49;00m
  4201	[33m[39;49;00m
  4202	[33mSYMBOL can be any Lisp symbol.  Its function definition and/or[39;49;00m
  4203	[33mvalue as a variable do not matter for this usage; we use only certain[39;49;00m
  4204	[33mproperties on its property list, to encode the rest of the arguments.[39;49;00m
  4205	[33m[39;49;00m
  4206	[33mCOMPOSEFUNC is program callable function that composes an outgoing[39;49;00m
  4207	[33mmail message buffer.  This function should set up the basics of the[39;49;00m
  4208	[33mbuffer without requiring user interaction.  It should populate the[39;49;00m
  4209	[33mstandard mail headers, leaving the [39;49;00m[33m`to:'[39;49;00m[33m and [39;49;00m[33m`subject:'[39;49;00m[33m headers blank[39;49;00m
  4210	[33mby default.[39;49;00m
  4211	[33m[39;49;00m
  4212	[33mCOMPOSEFUNC should accept several optional arguments--the same[39;49;00m
  4213	[33marguments that [39;49;00m[33m`compose-mail'[39;49;00m[33m takes.  See that function's documentation.[39;49;00m
  4214	[33m[39;49;00m
  4215	[33mSENDFUNC is the command a user would run to send the message.[39;49;00m
  4216	[33m[39;49;00m
  4217	[33mOptional ABORTFUNC is the command a user would run to abort the[39;49;00m
  4218	[33mmessage.  For mail packages that don't have a separate abort function,[39;49;00m
  4219	[33mthis can be [39;49;00m[33m`kill-buffer'[39;49;00m[33m (the equivalent of omitting this argument).[39;49;00m
  4220	[33m[39;49;00m
  4221	[33mOptional HOOKVAR is a hook variable that gets run before the message[39;49;00m
  4222	[33mis actually sent.  Callers that use the [39;49;00m[33m`mail-user-agent'[39;49;00m[33m may[39;49;00m
  4223	[33minstall a hook function temporarily on this hook variable.[39;49;00m
  4224	[33mIf HOOKVAR is nil, [39;49;00m[33m`mail-send-hook'[39;49;00m[33m is used.[39;49;00m
  4225	[33m[39;49;00m
  4226	[33mThe properties used on SYMBOL are [39;49;00m[33m`composefunc'[39;49;00m[33m, [39;49;00m[33m`sendfunc'[39;49;00m[33m,[39;49;00m
  4227	[33m`abortfunc'[39;49;00m[33m, and [39;49;00m[33m`hookvar'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  4228	[37m  [39;49;00m([32mput[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m[37m [39;49;00m[33m'composefunc[39;49;00m[37m [39;49;00m[31mcomposefunc[39;49;00m)[37m[39;49;00m
  4229	[37m  [39;49;00m([32mput[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m[37m [39;49;00m[33m'sendfunc[39;49;00m[37m [39;49;00m[31msendfunc[39;49;00m)[37m[39;49;00m
  4230	[37m  [39;49;00m([32mput[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m[37m [39;49;00m[33m'abortfunc[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mabortfunc[39;49;00m[37m [39;49;00m[33m'kill-buffer[39;49;00m))[37m[39;49;00m
  4231	[37m  [39;49;00m([32mput[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m[37m [39;49;00m[33m'hookvar[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mhookvar[39;49;00m[37m [39;49;00m[33m'mail-send-hook[39;49;00m)))[37m[39;49;00m
  4232	[37m[39;49;00m[37m[39;49;00m
  4233	([34mdefvar[39;49;00m[37m [39;49;00m[31mcalled-interactively-p-functions[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m
  4234	[37m  [39;49;00m[33m"[39;49;00m[33mSpecial hook called to skip special frames in [39;49;00m[33m`called-interactively-p'[39;49;00m[33m.[39;49;00m
  4235	[33mThe functions are called with 3 arguments: (I FRAME1 FRAME2),[39;49;00m
  4236	[33mwhere FRAME1 is a [39;49;00m[33m\"[39;49;00m[33mcurrent frame[39;49;00m[33m\"[39;49;00m[33m, FRAME2 is the next frame,[39;49;00m
  4237	[33mI is the index of the frame after FRAME2.  It should return nil[39;49;00m
  4238	[33mif those frames don't seem special and otherwise, it should return[39;49;00m
  4239	[33mthe number of frames to skip (minus 1).[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  4240	[37m[39;49;00m
  4241	([34mdefconst[39;49;00m[37m [39;49;00m[31minternal--funcall-interactively[39;49;00m[37m[39;49;00m
  4242	[37m  [39;49;00m([32msymbol-function[39;49;00m[37m [39;49;00m[33m'funcall-interactively[39;49;00m))[37m[39;49;00m
  4243	[37m[39;49;00m
  4244	([36mdefun[39;49;00m[37m [39;49;00m[31mcalled-interactively-p[39;49;00m[37m [39;49;00m([34m&optional[39;49;00m[37m [39;49;00m[31mkind[39;49;00m)[37m[39;49;00m
  4245	[37m  [39;49;00m[33m"[39;49;00m[33mReturn t if the containing function was called by [39;49;00m[33m`call-interactively'[39;49;00m[33m.[39;49;00m
  4246	[33mIf KIND is [39;49;00m[33m`interactive'[39;49;00m[33m, then only return t if the call was made[39;49;00m
  4247	[33minteractively by the user, i.e. not in [39;49;00m[33m`noninteractive'[39;49;00m[33m mode nor[39;49;00m
  4248	[33mwhen [39;49;00m[33m`executing-kbd-macro'[39;49;00m[33m.[39;49;00m
  4249	[33mIf KIND is [39;49;00m[33m`any'[39;49;00m[33m, on the other hand, it will return t for any kind of[39;49;00m
  4250	[33minteractive call, including being called as the binding of a key or[39;49;00m
  4251	[33mfrom a keyboard macro, even in [39;49;00m[33m`noninteractive'[39;49;00m[33m mode.[39;49;00m
  4252	[33m[39;49;00m
  4253	[33mThis function is very brittle, it may fail to return the intended result when[39;49;00m
  4254	[33mthe code is debugged, advised, or instrumented in some form.  Some macros and[39;49;00m
  4255	[33mspecial forms (such as [39;49;00m[33m`condition-case'[39;49;00m[33m) may also sometimes wrap their bodies[39;49;00m
  4256	[33min a [39;49;00m[33m`lambda'[39;49;00m[33m, so any call to [39;49;00m[33m`called-interactively-p'[39;49;00m[33m from those bodies will[39;49;00m
  4257	[33mindicate whether that lambda (rather than the surrounding function) was called[39;49;00m
  4258	[33minteractively.[39;49;00m
  4259	[33m[39;49;00m
  4260	[33mInstead of using this function, it is cleaner and more reliable to give your[39;49;00m
  4261	[33mfunction an extra optional argument whose [39;49;00m[33m`interactive'[39;49;00m[33m spec specifies[39;49;00m
  4262	[33mnon-nil unconditionally ([39;49;00m[33m\"[39;49;00m[33mp[39;49;00m[33m\"[39;49;00m[33m is a good way to do this), or via[39;49;00m
  4263	[33m\([39;49;00m[33mnot (or executing-kbd-macro noninteractive)).[39;49;00m
  4264	[33m[39;49;00m
  4265	[33mThe only known proper use of [39;49;00m[33m`interactive'[39;49;00m[33m for KIND is in deciding[39;49;00m
  4266	[33mwhether to display a helpful message, or how to display it.  If you're[39;49;00m
  4267	[33mthinking of using it for any other purpose, it is quite likely that[39;49;00m
  4268	[33myou're making a mistake.  Think: what do you want to do when the[39;49;00m
  4269	[33mcommand is called from a keyboard macro?[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  4270	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31madvertised-calling-convention[39;49;00m[37m [39;49;00m([31mkind[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m23.1[39;49;00m[33m"[39;49;00m))[37m[39;49;00m
  4271	[37m  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mkind[39;49;00m[37m [39;49;00m[33m'interactive[39;49;00m)[37m[39;49;00m
  4272	[37m                  [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mexecuting-kbd-macro[39;49;00m[37m [39;49;00m[31mnoninteractive[39;49;00m)))[37m[39;49;00m
  4273	[37m    [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mi[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m[37m;; 0 is the called-interactively-p frame.[39;49;00m[37m[39;49;00m
  4274	[37m           [39;49;00m[31mframe[39;49;00m[37m [39;49;00m[31mnextframe[39;49;00m[37m[39;49;00m
  4275	[37m           [39;49;00m([31mget-next-frame[39;49;00m[37m[39;49;00m
  4276	[37m            [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m()[37m[39;49;00m
  4277	[37m              [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mframe[39;49;00m[37m [39;49;00m[31mnextframe[39;49;00m)[37m[39;49;00m
  4278	[37m              [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mnextframe[39;49;00m[37m [39;49;00m([32mbacktrace-frame[39;49;00m[37m [39;49;00m[31mi[39;49;00m[37m [39;49;00m[33m'called-interactively-p[39;49;00m))[37m[39;49;00m
  4279	[37m              [39;49;00m[37m;; (message "Frame %d = %S" i nextframe)[39;49;00m[37m[39;49;00m
  4280	[37m              [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mi[39;49;00m[37m [39;49;00m([32m1+[39;49;00m[37m [39;49;00m[31mi[39;49;00m)))))[37m[39;49;00m
  4281	[37m      [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mget-next-frame[39;49;00m)[37m [39;49;00m[37m;; Get the first frame.[39;49;00m[37m[39;49;00m
  4282	[37m      [39;49;00m([34mwhile[39;49;00m[37m[39;49;00m
  4283	[37m          [39;49;00m[37m;; FIXME: The edebug and advice handling should be made modular and[39;49;00m[37m[39;49;00m
  4284	[37m          [39;49;00m[37m;; provided directly by edebug.el and nadvice.el.[39;49;00m[37m[39;49;00m
  4285	[37m          [39;49;00m([34mprogn[39;49;00m[37m[39;49;00m
  4286	[37m            [39;49;00m[37m;; frame    =(backtrace-frame i-2)[39;49;00m[37m[39;49;00m
  4287	[37m            [39;49;00m[37m;; nextframe=(backtrace-frame i-1)[39;49;00m[37m[39;49;00m
  4288	[37m            [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mget-next-frame[39;49;00m)[37m[39;49;00m
  4289	[37m            [39;49;00m[37m;; `pcase' would be a fairly good fit here, but it sometimes moves[39;49;00m[37m[39;49;00m
  4290	[37m            [39;49;00m[37m;; branches within local functions, which then messes up the[39;49;00m[37m[39;49;00m
  4291	[37m            [39;49;00m[37m;; `backtrace-frame' data we get,[39;49;00m[37m[39;49;00m
  4292	[37m            [39;49;00m([34mor[39;49;00m[37m[39;49;00m
  4293	[37m             [39;49;00m[37m;; Skip special forms (from non-compiled code).[39;49;00m[37m[39;49;00m
  4294	[37m             [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mframe[39;49;00m[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mframe[39;49;00m)))[37m[39;49;00m
  4295	[37m             [39;49;00m[37m;; Skip also `interactive-p' (because we don't want to know if[39;49;00m[37m[39;49;00m
  4296	[37m             [39;49;00m[37m;; interactive-p was called interactively but if it's caller was)[39;49;00m[37m[39;49;00m
  4297	[37m             [39;49;00m[37m;; and `byte-code' (idem; this appears in subexpressions of things[39;49;00m[37m[39;49;00m
  4298	[37m             [39;49;00m[37m;; like condition-case, which are wrapped in a separate bytecode[39;49;00m[37m[39;49;00m
  4299	[37m             [39;49;00m[37m;; chunk).[39;49;00m[37m[39;49;00m
  4300	[37m             [39;49;00m[37m;; FIXME: For lexical-binding code, this is much worse,[39;49;00m[37m[39;49;00m
  4301	[37m             [39;49;00m[37m;; because the frames look like "byte-code -> funcall -> #[...]",[39;49;00m[37m[39;49;00m
  4302	[37m             [39;49;00m[37m;; which is not a reliable signature.[39;49;00m[37m[39;49;00m
  4303	[37m             [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mframe[39;49;00m)[37m [39;49;00m'([31minteractive-p[39;49;00m[37m [39;49;00m[33m'byte-code[39;49;00m))[37m[39;49;00m
  4304	[37m             [39;49;00m[37m;; Skip package-specific stack-frames.[39;49;00m[37m[39;49;00m
  4305	[37m             [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mskip[39;49;00m[37m [39;49;00m([32mrun-hook-with-args-until-success[39;49;00m[37m[39;49;00m
  4306	[37m                          [39;49;00m[33m'called-interactively-p-functions[39;49;00m[37m[39;49;00m
  4307	[37m                          [39;49;00m[31mi[39;49;00m[37m [39;49;00m[31mframe[39;49;00m[37m [39;49;00m[31mnextframe[39;49;00m)))[37m[39;49;00m
  4308	[37m               [39;49;00m([36mpcase[39;49;00m[37m [39;49;00m[31mskip[39;49;00m[37m[39;49;00m
  4309	[37m                 [39;49;00m(`[31mnil[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m
  4310	[37m                 [39;49;00m(`[34m0[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m
  4311	[37m                 [39;49;00m([31m_[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mi[39;49;00m[37m [39;49;00m([32m+[39;49;00m[37m [39;49;00m[31mi[39;49;00m[37m [39;49;00m[31mskip[39;49;00m[37m [39;49;00m[34m-1[39;49;00m))[37m [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mget-next-frame[39;49;00m)))))))[37m[39;49;00m
  4312	[37m      [39;49;00m[37m;; Now `frame' should be "the function from which we were called".[39;49;00m[37m[39;49;00m
  4313	[37m      [39;49;00m([36mpcase[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mframe[39;49;00m[37m [39;49;00m[31mnextframe[39;49;00m)[37m[39;49;00m
  4314	[37m        [39;49;00m[37m;; No subr calls `interactive-p', so we can rule that out.[39;49;00m[37m[39;49;00m
  4315	[37m        [39;49;00m(`((,[31m_[39;49;00m[37m [39;49;00m,([31mpred[39;49;00m[37m [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31mf[39;49;00m)[37m [39;49;00m([32msubrp[39;49;00m[37m [39;49;00m([32mindirect-function[39;49;00m[37m [39;49;00m[31mf[39;49;00m))))[37m [39;49;00m.[37m [39;49;00m,[31m_[39;49;00m)[37m [39;49;00m.[37m [39;49;00m,[31m_[39;49;00m)[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m
  4316	[37m        [39;49;00m[37m;; In case #<subr funcall-interactively> without going through the[39;49;00m[37m[39;49;00m
  4317	[37m        [39;49;00m[37m;; `funcall-interactively' symbol (bug#3984).[39;49;00m[37m[39;49;00m
  4318	[37m        [39;49;00m(`(,[31m_[39;49;00m[37m [39;49;00m.[37m [39;49;00m([31mt[39;49;00m[37m [39;49;00m,([31mpred[39;49;00m[37m [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31mf[39;49;00m)[37m[39;49;00m
  4319	[37m                            [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31minternal--funcall-interactively[39;49;00m[37m[39;49;00m
  4320	[37m                                [39;49;00m([32mindirect-function[39;49;00m[37m [39;49;00m[31mf[39;49;00m))))[37m[39;49;00m
  4321	[37m                   [39;49;00m.[37m [39;49;00m,[31m_[39;49;00m))[37m[39;49;00m
  4322	[37m         [39;49;00m[31mt[39;49;00m)))))[37m[39;49;00m
  4323	[37m[39;49;00m
  4324	([36mdefun[39;49;00m[37m [39;49;00m[31minteractive-p[39;49;00m[37m [39;49;00m()[37m[39;49;00m
  4325	[37m  [39;49;00m[33m"[39;49;00m[33mReturn t if the containing function was run directly by user input.[39;49;00m
  4326	[33mThis means that the function was called with [39;49;00m[33m`call-interactively'[39;49;00m[33m[39;49;00m
  4327	[33m\([39;49;00m[33mwhich includes being called as the binding of a key)[39;49;00m
  4328	[33mand input is currently coming from the keyboard (not a keyboard macro),[39;49;00m
  4329	[33mand Emacs is not running in batch mode ([39;49;00m[33m`noninteractive'[39;49;00m[33m is nil).[39;49;00m
  4330	[33m[39;49;00m
  4331	[33mThe only known proper use of [39;49;00m[33m`interactive-p'[39;49;00m[33m is in deciding whether to[39;49;00m
  4332	[33mdisplay a helpful message, or how to display it.  If you're thinking[39;49;00m
  4333	[33mof using it for any other purpose, it is quite likely that you're[39;49;00m
  4334	[33mmaking a mistake.  Think: what do you want to do when the command is[39;49;00m
  4335	[33mcalled from a keyboard macro or in batch mode?[39;49;00m
  4336	[33m[39;49;00m
  4337	[33mTo test whether your function was called with [39;49;00m[33m`call-interactively'[39;49;00m[33m,[39;49;00m
  4338	[33meither (i) add an extra optional argument and give it an [39;49;00m[33m`interactive'[39;49;00m[33m[39;49;00m
  4339	[33mspec that specifies non-nil unconditionally (such as [39;49;00m[33m\"[39;49;00m[33mp[39;49;00m[33m\"[39;49;00m[33m); or (ii)[39;49;00m
  4340	[33muse [39;49;00m[33m`called-interactively-p'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  4341	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mobsolete[39;49;00m[37m [39;49;00m[31mcalled-interactively-p[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m))[37m[39;49;00m
  4342	[37m  [39;49;00m([31mcalled-interactively-p[39;49;00m[37m [39;49;00m[33m'interactive[39;49;00m))[37m[39;49;00m
  4343	[37m[39;49;00m
  4344	([36mdefun[39;49;00m[37m [39;49;00m[31minternal-push-keymap[39;49;00m[37m [39;49;00m([31mkeymap[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m)[37m[39;49;00m
  4345	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mmap[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m)))[37m[39;49;00m
  4346	[37m    [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m[37m [39;49;00m[31mmap[39;49;00m)[37m[39;49;00m
  4347	[37m      [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[33m'add-keymap-witness[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m))[37m[39;49;00m
  4348	[37m        [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m([31mmake-composed-keymap[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m)))[37m[39;49;00m
  4349	[37m        [39;49;00m([36mpush[39;49;00m[37m [39;49;00m[33m'add-keymap-witness[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mmap[39;49;00m))[37m[39;49;00m
  4350	[37m        [39;49;00m([32mset[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m[37m [39;49;00m[31mmap[39;49;00m))[37m[39;49;00m
  4351	[37m      [39;49;00m([36mpush[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mmap[39;49;00m)))))[37m[39;49;00m
  4352	[37m[39;49;00m
  4353	([36mdefun[39;49;00m[37m [39;49;00m[31minternal-pop-keymap[39;49;00m[37m [39;49;00m([31mkeymap[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m)[37m[39;49;00m
  4354	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mmap[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m)))[37m[39;49;00m
  4355	[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m[37m [39;49;00m[31mmap[39;49;00m)[37m[39;49;00m
  4356	[37m      [39;49;00m([36msetf[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mmap[39;49;00m)[37m [39;49;00m([32mdelq[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mmap[39;49;00m))))[37m[39;49;00m
  4357	[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtail[39;49;00m[37m [39;49;00m([31mcddr[39;49;00m[37m [39;49;00m[31mmap[39;49;00m)))[37m[39;49;00m
  4358	[37m      [39;49;00m([34mand[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)[37m [39;49;00m([32mkeymapp[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))[37m[39;49;00m
  4359	[37m           [39;49;00m([32meq[39;49;00m[37m [39;49;00m[33m'add-keymap-witness[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mmap[39;49;00m))[37m[39;49;00m
  4360	[37m           [39;49;00m([32mset[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)))))[37m[39;49;00m
  4361	[37m[39;49;00m
  4362	([36mdefine-obsolete-function-alias[39;49;00m[37m[39;49;00m
  4363	[37m  [39;49;00m[33m'set-temporary-overlay-map[39;49;00m[37m [39;49;00m[33m'set-transient-map[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m24.4[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  4364	[37m[39;49;00m
  4365	([36mdefun[39;49;00m[37m [39;49;00m[31mset-transient-map[39;49;00m[37m [39;49;00m([31mmap[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mkeep-pred[39;49;00m[37m [39;49;00m[31mon-exit[39;49;00m)[37m[39;49;00m
  4366	[37m  [39;49;00m[33m"[39;49;00m[33mSet MAP as a temporary keymap taking precedence over other keymaps.[39;49;00m
  4367	[33mNormally, MAP is used only once, to look up the very next key.[39;49;00m
  4368	[33mHowever, if the optional argument KEEP-PRED is t, MAP stays[39;49;00m
  4369	[33mactive if a key from MAP is used.  KEEP-PRED can also be a[39;49;00m
  4370	[33mfunction of no arguments: it is called from [39;49;00m[33m`pre-command-hook'[39;49;00m[33m and[39;49;00m
  4371	[33mif it returns non-nil, then MAP stays active.[39;49;00m
  4372	[33m[39;49;00m
  4373	[33mOptional arg ON-EXIT, if non-nil, specifies a function that is[39;49;00m
  4374	[33mcalled, with no arguments, after MAP is deactivated.[39;49;00m
  4375	[33m[39;49;00m
  4376	[33mThis uses [39;49;00m[33m`overriding-terminal-local-map'[39;49;00m[33m which takes precedence over all other[39;49;00m
  4377	[33mkeymaps.  As usual, if no match for a key is found in MAP, the normal key[39;49;00m
  4378	[33mlookup sequence then continues.[39;49;00m
  4379	[33m[39;49;00m
  4380	[33mThis returns an [39;49;00m[33m\"[39;49;00m[33mexit function[39;49;00m[33m\"[39;49;00m[33m, which can be called with no argument[39;49;00m
  4381	[33mto deactivate this transient map, regardless of KEEP-PRED.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  4382	[37m  [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mclearfun[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mclear-transient-map[39;49;00m[33m"[39;49;00m))[37m[39;49;00m
  4383	[37m         [39;49;00m([31mexitfun[39;49;00m[37m[39;49;00m
  4384	[37m          [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m()[37m[39;49;00m
  4385	[37m            [39;49;00m([31minternal-pop-keymap[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m[33m'overriding-terminal-local-map[39;49;00m)[37m[39;49;00m
  4386	[37m            [39;49;00m([31mremove-hook[39;49;00m[37m [39;49;00m[33m'pre-command-hook[39;49;00m[37m [39;49;00m[31mclearfun[39;49;00m)[37m[39;49;00m
  4387	[37m            [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31mon-exit[39;49;00m[37m [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mon-exit[39;49;00m)))))[37m[39;49;00m
  4388	[37m    [39;49;00m[37m;; Don't use letrec, because equal (in add/remove-hook) would get trapped[39;49;00m[37m[39;49;00m
  4389	[37m    [39;49;00m[37m;; in a cycle.[39;49;00m[37m[39;49;00m
  4390	[37m    [39;49;00m([32mfset[39;49;00m[37m [39;49;00m[31mclearfun[39;49;00m[37m[39;49;00m
  4391	[37m          [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m()[37m[39;49;00m
  4392	[37m            [39;49;00m([36mwith-demoted-errors[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mset-transient-map PCH: %S[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  4393	[37m              [39;49;00m([36munless[39;49;00m[37m [39;49;00m([34mcond[39;49;00m[37m[39;49;00m
  4394	[37m                       [39;49;00m(([32mnull[39;49;00m[37m [39;49;00m[31mkeep-pred[39;49;00m)[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m
  4395	[37m                       [39;49;00m(([31mnot[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m([31mcadr[39;49;00m[37m [39;49;00m[31moverriding-terminal-local-map[39;49;00m)))[37m[39;49;00m
  4396	[37m                        [39;49;00m[37m;; There's presumably some other transient-map in[39;49;00m[37m[39;49;00m
  4397	[37m                        [39;49;00m[37m;; effect.  Wait for that one to terminate before we[39;49;00m[37m[39;49;00m
  4398	[37m                        [39;49;00m[37m;; remove ourselves.[39;49;00m[37m[39;49;00m
  4399	[37m                        [39;49;00m[37m;; For example, if isearch and C-u both use transient[39;49;00m[37m[39;49;00m
  4400	[37m                        [39;49;00m[37m;; maps, then the lifetime of the C-u should be nested[39;49;00m[37m[39;49;00m
  4401	[37m                        [39;49;00m[37m;; within isearch's, so the pre-command-hook of[39;49;00m[37m[39;49;00m
  4402	[37m                        [39;49;00m[37m;; isearch should be suspended during the C-u one so[39;49;00m[37m[39;49;00m
  4403	[37m                        [39;49;00m[37m;; we don't exit isearch just because we hit 1 after[39;49;00m[37m[39;49;00m
  4404	[37m                        [39;49;00m[37m;; C-u and that 1 exits isearch whereas it doesn't[39;49;00m[37m[39;49;00m
  4405	[37m                        [39;49;00m[37m;; exit C-u.[39;49;00m[37m[39;49;00m
  4406	[37m                        [39;49;00m[31mt[39;49;00m)[37m[39;49;00m
  4407	[37m                       [39;49;00m(([32meq[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m[31mkeep-pred[39;49;00m)[37m[39;49;00m
  4408	[37m                        [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mthis-command[39;49;00m[37m[39;49;00m
  4409	[37m                            [39;49;00m([32mlookup-key[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m([32mthis-command-keys-vector[39;49;00m))))[37m[39;49;00m
  4410	[37m                       [39;49;00m([31mt[39;49;00m[37m [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mkeep-pred[39;49;00m)))[37m[39;49;00m
  4411	[37m                [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mexitfun[39;49;00m)))))[37m[39;49;00m
  4412	[37m    [39;49;00m([31madd-hook[39;49;00m[37m [39;49;00m[33m'pre-command-hook[39;49;00m[37m [39;49;00m[31mclearfun[39;49;00m)[37m[39;49;00m
  4413	[37m    [39;49;00m([31minternal-push-keymap[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m[33m'overriding-terminal-local-map[39;49;00m)[37m[39;49;00m
  4414	[37m    [39;49;00m[31mexitfun[39;49;00m))[37m[39;49;00m
  4415	[37m[39;49;00m
  4416	[37m;;;; Progress reporters.[39;49;00m[37m[39;49;00m
  4417	[37m[39;49;00m
  4418	[37m;; Progress reporter has the following structure:[39;49;00m[37m[39;49;00m
  4419	[37m;;[39;49;00m[37m[39;49;00m
  4420	[37m;;	(NEXT-UPDATE-VALUE . [NEXT-UPDATE-TIME[39;49;00m[37m[39;49;00m
  4421	[37m;;			      MIN-VALUE[39;49;00m[37m[39;49;00m
  4422	[37m;;			      MAX-VALUE[39;49;00m[37m[39;49;00m
  4423	[37m;;			      MESSAGE[39;49;00m[37m[39;49;00m
  4424	[37m;;			      MIN-CHANGE[39;49;00m[37m[39;49;00m
  4425	[37m;;			      MIN-TIME])[39;49;00m[37m[39;49;00m
  4426	[37m;;[39;49;00m[37m[39;49;00m
  4427	[37m;; This weirdness is for optimization reasons: we want[39;49;00m[37m[39;49;00m
  4428	[37m;; `progress-reporter-update' to be as fast as possible, so[39;49;00m[37m[39;49;00m
  4429	[37m;; `(car reporter)' is better than `(aref reporter 0)'.[39;49;00m[37m[39;49;00m
  4430	[37m;;[39;49;00m[37m[39;49;00m
  4431	[37m;; NEXT-UPDATE-TIME is a float.  While `float-time' loses a couple[39;49;00m[37m[39;49;00m
  4432	[37m;; digits of precision, it doesn't really matter here.  On the other[39;49;00m[37m[39;49;00m
  4433	[37m;; hand, it greatly simplifies the code.[39;49;00m[37m[39;49;00m
  4434	[37m[39;49;00m
  4435	([36mdefsubst[39;49;00m[37m [39;49;00m[31mprogress-reporter-update[39;49;00m[37m [39;49;00m([31mreporter[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mvalue[39;49;00m)[37m[39;49;00m
  4436	[37m  [39;49;00m[33m"[39;49;00m[33mReport progress of an operation in the echo area.[39;49;00m
  4437	[33mREPORTER should be the result of a call to [39;49;00m[33m`make-progress-reporter'[39;49;00m[33m.[39;49;00m
  4438	[33m[39;49;00m
  4439	[33mIf REPORTER is a numerical progress reporter---i.e. if it was[39;49;00m
  4440	[33m made using non-nil MIN-VALUE and MAX-VALUE arguments to[39;49;00m
  4441	[33m [39;49;00m[33m`make-progress-reporter'[39;49;00m[33m---then VALUE should be a number between[39;49;00m
  4442	[33m MIN-VALUE and MAX-VALUE.[39;49;00m
  4443	[33m[39;49;00m
  4444	[33mIf REPORTER is a non-numerical reporter, VALUE should be nil.[39;49;00m
  4445	[33m[39;49;00m
  4446	[33mThis function is relatively inexpensive.  If the change since[39;49;00m
  4447	[33mlast update is too small or insufficient time has passed, it does[39;49;00m
  4448	[33mnothing.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  4449	[37m  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mnumberp[39;49;00m[37m [39;49;00m[31mvalue[39;49;00m))[37m      [39;49;00m[37m; For pulsing reporter[39;49;00m[37m[39;49;00m
  4450	[37m	    [39;49;00m([32m>=[39;49;00m[37m [39;49;00m[31mvalue[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mreporter[39;49;00m)))[37m [39;49;00m[37m; For numerical reporter[39;49;00m[37m[39;49;00m
  4451	[37m    [39;49;00m([31mprogress-reporter-do-update[39;49;00m[37m [39;49;00m[31mreporter[39;49;00m[37m [39;49;00m[31mvalue[39;49;00m)))[37m[39;49;00m
  4452	[37m[39;49;00m
  4453	([36mdefun[39;49;00m[37m [39;49;00m[31mmake-progress-reporter[39;49;00m[37m [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mmin-value[39;49;00m[37m [39;49;00m[31mmax-value[39;49;00m[37m[39;49;00m
  4454	[37m				       [39;49;00m[31mcurrent-value[39;49;00m[37m [39;49;00m[31mmin-change[39;49;00m[37m [39;49;00m[31mmin-time[39;49;00m)[37m[39;49;00m
  4455	[37m  [39;49;00m[33m"[39;49;00m[33mReturn progress reporter object for use with [39;49;00m[33m`progress-reporter-update'[39;49;00m[33m.[39;49;00m
  4456	[33m[39;49;00m
  4457	[33mMESSAGE is shown in the echo area, with a status indicator[39;49;00m
  4458	[33mappended to the end.  When you call [39;49;00m[33m`progress-reporter-done'[39;49;00m[33m, the[39;49;00m
  4459	[33mword [39;49;00m[33m\"[39;49;00m[33mdone[39;49;00m[33m\"[39;49;00m[33m is printed after the MESSAGE.  You can change the[39;49;00m
  4460	[33mMESSAGE of an existing progress reporter by calling[39;49;00m
  4461	[33m`progress-reporter-force-update'[39;49;00m[33m.[39;49;00m
  4462	[33m[39;49;00m
  4463	[33mMIN-VALUE and MAX-VALUE, if non-nil, are starting (0% complete)[39;49;00m
  4464	[33mand final (100% complete) states of operation; the latter should[39;49;00m
  4465	[33mbe larger.  In this case, the status message shows the percentage[39;49;00m
  4466	[33mprogress.[39;49;00m
  4467	[33m[39;49;00m
  4468	[33mIf MIN-VALUE and/or MAX-VALUE is omitted or nil, the status[39;49;00m
  4469	[33mmessage shows a [39;49;00m[33m\"[39;49;00m[33mspinning[39;49;00m[33m\"[39;49;00m[33m, non-numeric indicator.[39;49;00m
  4470	[33m[39;49;00m
  4471	[33mOptional CURRENT-VALUE is the initial progress; the default is[39;49;00m
  4472	[33mMIN-VALUE.[39;49;00m
  4473	[33mOptional MIN-CHANGE is the minimal change in percents to report;[39;49;00m
  4474	[33mthe default is 1%.[39;49;00m
  4475	[33mCURRENT-VALUE and MIN-CHANGE do not have any effect if MIN-VALUE[39;49;00m
  4476	[33mand/or MAX-VALUE are nil.[39;49;00m
  4477	[33m[39;49;00m
  4478	[33mOptional MIN-TIME specifies the minimum interval time between[39;49;00m
  4479	[33mecho area updates (default is 0.2 seconds.)  If the function[39;49;00m
  4480	[33m`float-time'[39;49;00m[33m is not present, time is not tracked at all.  If the[39;49;00m
  4481	[33mOS is not capable of measuring fractions of seconds, this[39;49;00m
  4482	[33mparameter is effectively rounded up.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  4483	[37m  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m[[:alnum:]][39;49;00m[33m\\[39;49;00m[33m'[39;49;00m[33m"[39;49;00m[37m [39;49;00m[32mmessage[39;49;00m)[37m[39;49;00m
  4484	[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[32mmessage[39;49;00m[37m [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[32mmessage[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m...[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m
  4485	[37m  [39;49;00m([36munless[39;49;00m[37m [39;49;00m[31mmin-time[39;49;00m[37m[39;49;00m
  4486	[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mmin-time[39;49;00m[37m [39;49;00m[34m0.2[39;49;00m))[37m[39;49;00m
  4487	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mreporter[39;49;00m[37m[39;49;00m
  4488	[37m	 [39;49;00m[37m;; Force a call to `message' now[39;49;00m[37m[39;49;00m
  4489	[37m	 [39;49;00m([32mcons[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mmin-value[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m
  4490	[37m	       [39;49;00m([32mvector[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mfboundp[39;49;00m[37m [39;49;00m[33m'float-time[39;49;00m)[37m[39;49;00m
  4491	[37m				[39;49;00m([32m>=[39;49;00m[37m [39;49;00m[31mmin-time[39;49;00m[37m [39;49;00m[34m0.02[39;49;00m))[37m[39;49;00m
  4492	[37m			   [39;49;00m([32mfloat-time[39;49;00m)[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m
  4493	[37m		       [39;49;00m[31mmin-value[39;49;00m[37m[39;49;00m
  4494	[37m		       [39;49;00m[31mmax-value[39;49;00m[37m[39;49;00m
  4495	[37m		       [39;49;00m[32mmessage[39;49;00m[37m[39;49;00m
  4496	[37m		       [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mmin-change[39;49;00m[37m [39;49;00m([32mmax[39;49;00m[37m [39;49;00m([32mmin[39;49;00m[37m [39;49;00m[31mmin-change[39;49;00m[37m [39;49;00m[34m50[39;49;00m)[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m[34m1[39;49;00m)[37m[39;49;00m
  4497	[37m		       [39;49;00m[31mmin-time[39;49;00m))))[37m[39;49;00m
  4498	[37m    [39;49;00m([31mprogress-reporter-update[39;49;00m[37m [39;49;00m[31mreporter[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mcurrent-value[39;49;00m[37m [39;49;00m[31mmin-value[39;49;00m))[37m[39;49;00m
  4499	[37m    [39;49;00m[31mreporter[39;49;00m))[37m[39;49;00m
  4500	[37m[39;49;00m
  4501	([36mdefun[39;49;00m[37m [39;49;00m[31mprogress-reporter-force-update[39;49;00m[37m [39;49;00m([31mreporter[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mvalue[39;49;00m[37m [39;49;00m[31mnew-message[39;49;00m)[37m[39;49;00m
  4502	[37m  [39;49;00m[33m"[39;49;00m[33mReport progress of an operation in the echo area unconditionally.[39;49;00m
  4503	[33m[39;49;00m
  4504	[33mThe first two arguments are the same as in [39;49;00m[33m`progress-reporter-update'[39;49;00m[33m.[39;49;00m
  4505	[33mNEW-MESSAGE, if non-nil, sets a new message for the reporter.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  4506	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mparameters[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mreporter[39;49;00m)))[37m[39;49;00m
  4507	[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31mnew-message[39;49;00m[37m[39;49;00m
  4508	[37m      [39;49;00m([32maset[39;49;00m[37m [39;49;00m[31mparameters[39;49;00m[37m [39;49;00m[34m3[39;49;00m[37m [39;49;00m[31mnew-message[39;49;00m))[37m[39;49;00m
  4509	[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32maref[39;49;00m[37m [39;49;00m[31mparameters[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m
  4510	[37m      [39;49;00m([32maset[39;49;00m[37m [39;49;00m[31mparameters[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m([32mfloat-time[39;49;00m)))[37m[39;49;00m
  4511	[37m    [39;49;00m([31mprogress-reporter-do-update[39;49;00m[37m [39;49;00m[31mreporter[39;49;00m[37m [39;49;00m[31mvalue[39;49;00m)))[37m[39;49;00m
  4512	[37m[39;49;00m
  4513	([34mdefvar[39;49;00m[37m [39;49;00m[31mprogress-reporter--pulse-characters[39;49;00m[37m [39;49;00m[[33m"[39;49;00m[33m-[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m|[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m/[39;49;00m[33m"[39;49;00m][37m[39;49;00m
  4514	[37m  [39;49;00m[33m"[39;49;00m[33mCharacters to use for pulsing progress reporters.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  4515	[37m[39;49;00m
  4516	([36mdefun[39;49;00m[37m [39;49;00m[31mprogress-reporter-do-update[39;49;00m[37m [39;49;00m([31mreporter[39;49;00m[37m [39;49;00m[31mvalue[39;49;00m)[37m[39;49;00m
  4517	[37m  [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mparameters[39;49;00m[37m   [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mreporter[39;49;00m))[37m[39;49;00m
  4518	[37m	 [39;49;00m([31mupdate-time[39;49;00m[37m  [39;49;00m([32maref[39;49;00m[37m [39;49;00m[31mparameters[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m
  4519	[37m	 [39;49;00m([31mmin-value[39;49;00m[37m    [39;49;00m([32maref[39;49;00m[37m [39;49;00m[31mparameters[39;49;00m[37m [39;49;00m[34m1[39;49;00m))[37m[39;49;00m
  4520	[37m	 [39;49;00m([31mmax-value[39;49;00m[37m    [39;49;00m([32maref[39;49;00m[37m [39;49;00m[31mparameters[39;49;00m[37m [39;49;00m[34m2[39;49;00m))[37m[39;49;00m
  4521	[37m	 [39;49;00m([31mtext[39;49;00m[37m         [39;49;00m([32maref[39;49;00m[37m [39;49;00m[31mparameters[39;49;00m[37m [39;49;00m[34m3[39;49;00m))[37m[39;49;00m
  4522	[37m	 [39;49;00m([31menough-time-passed[39;49;00m[37m[39;49;00m
  4523	[37m	  [39;49;00m[37m;; See if enough time has passed since the last update.[39;49;00m[37m[39;49;00m
  4524	[37m	  [39;49;00m([34mor[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m[31mupdate-time[39;49;00m)[37m[39;49;00m
  4525	[37m	      [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32m>=[39;49;00m[37m [39;49;00m([32mfloat-time[39;49;00m)[37m [39;49;00m[31mupdate-time[39;49;00m)[37m[39;49;00m
  4526	[37m		[39;49;00m[37m;; Calculate time for the next update[39;49;00m[37m[39;49;00m
  4527	[37m		[39;49;00m([32maset[39;49;00m[37m [39;49;00m[31mparameters[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m([32m+[39;49;00m[37m [39;49;00m[31mupdate-time[39;49;00m[37m [39;49;00m([32maref[39;49;00m[37m [39;49;00m[31mparameters[39;49;00m[37m [39;49;00m[34m5[39;49;00m)))))))[37m[39;49;00m
  4528	[37m    [39;49;00m([34mcond[39;49;00m[37m [39;49;00m(([34mand[39;49;00m[37m [39;49;00m[31mmin-value[39;49;00m[37m [39;49;00m[31mmax-value[39;49;00m)[37m[39;49;00m
  4529	[37m	   [39;49;00m[37m;; Numerical indicator[39;49;00m[37m[39;49;00m
  4530	[37m	   [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mone-percent[39;49;00m[37m [39;49;00m([32m/[39;49;00m[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m[31mmax-value[39;49;00m[37m [39;49;00m[31mmin-value[39;49;00m)[37m [39;49;00m[34m100.0[39;49;00m))[37m[39;49;00m
  4531	[37m		  [39;49;00m([31mpercentage[39;49;00m[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32m=[39;49;00m[37m [39;49;00m[31mmax-value[39;49;00m[37m [39;49;00m[31mmin-value[39;49;00m)[37m[39;49;00m
  4532	[37m				   [39;49;00m[34m0[39;49;00m[37m[39;49;00m
  4533	[37m				 [39;49;00m([32mtruncate[39;49;00m[37m [39;49;00m([32m/[39;49;00m[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m[31mvalue[39;49;00m[37m [39;49;00m[31mmin-value[39;49;00m)[37m[39;49;00m
  4534	[37m					      [39;49;00m[31mone-percent[39;49;00m)))))[37m[39;49;00m
  4535	[37m	     [39;49;00m[37m;; Calculate NEXT-UPDATE-VALUE.  If we are not printing[39;49;00m[37m[39;49;00m
  4536	[37m	     [39;49;00m[37m;; message because not enough time has passed, use 1[39;49;00m[37m[39;49;00m
  4537	[37m	     [39;49;00m[37m;; instead of MIN-CHANGE.  This makes delays between echo[39;49;00m[37m[39;49;00m
  4538	[37m	     [39;49;00m[37m;; area updates closer to MIN-TIME.[39;49;00m[37m[39;49;00m
  4539	[37m	     [39;49;00m([32msetcar[39;49;00m[37m [39;49;00m[31mreporter[39;49;00m[37m[39;49;00m
  4540	[37m		     [39;49;00m([32mmin[39;49;00m[37m [39;49;00m([32m+[39;49;00m[37m [39;49;00m[31mmin-value[39;49;00m[37m [39;49;00m([32m*[39;49;00m[37m [39;49;00m([32m+[39;49;00m[37m [39;49;00m[31mpercentage[39;49;00m[37m[39;49;00m
  4541	[37m					     [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31menough-time-passed[39;49;00m[37m[39;49;00m
  4542	[37m						 [39;49;00m[37m;; MIN-CHANGE[39;49;00m[37m[39;49;00m
  4543	[37m						 [39;49;00m([32maref[39;49;00m[37m [39;49;00m[31mparameters[39;49;00m[37m [39;49;00m[34m4[39;49;00m)[37m[39;49;00m
  4544	[37m					       [39;49;00m[34m1[39;49;00m))[37m[39;49;00m
  4545	[37m					  [39;49;00m[31mone-percent[39;49;00m))[37m[39;49;00m
  4546	[37m			  [39;49;00m[31mmax-value[39;49;00m))[37m[39;49;00m
  4547	[37m	     [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mintegerp[39;49;00m[37m [39;49;00m[31mvalue[39;49;00m)[37m[39;49;00m
  4548	[37m	       [39;49;00m([32msetcar[39;49;00m[37m [39;49;00m[31mreporter[39;49;00m[37m [39;49;00m([32mceiling[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mreporter[39;49;00m))))[37m[39;49;00m
  4549	[37m	     [39;49;00m[37m;; Only print message if enough time has passed[39;49;00m[37m[39;49;00m
  4550	[37m	     [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31menough-time-passed[39;49;00m[37m[39;49;00m
  4551	[37m	       [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m[31mpercentage[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m
  4552	[37m		   [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m%s%d%%[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mtext[39;49;00m[37m [39;49;00m[31mpercentage[39;49;00m)[37m[39;49;00m
  4553	[37m		 [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m%s[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mtext[39;49;00m)))))[37m[39;49;00m
  4554	[37m	  [39;49;00m[37m;; Pulsing indicator[39;49;00m[37m[39;49;00m
  4555	[37m	  [39;49;00m([31menough-time-passed[39;49;00m[37m[39;49;00m
  4556	[37m	   [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mindex[39;49;00m[37m [39;49;00m([32mmod[39;49;00m[37m [39;49;00m([32m1+[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mreporter[39;49;00m))[37m [39;49;00m[34m4[39;49;00m))[37m[39;49;00m
  4557	[37m		 [39;49;00m([31mmessage-log-max[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m
  4558	[37m	     [39;49;00m([32msetcar[39;49;00m[37m [39;49;00m[31mreporter[39;49;00m[37m [39;49;00m[31mindex[39;49;00m)[37m[39;49;00m
  4559	[37m	     [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m%s %s[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  4560	[37m		      [39;49;00m[31mtext[39;49;00m[37m[39;49;00m
  4561	[37m		      [39;49;00m([32maref[39;49;00m[37m [39;49;00m[31mprogress-reporter--pulse-characters[39;49;00m[37m[39;49;00m
  4562	[37m			    [39;49;00m[31mindex[39;49;00m)))))))[37m[39;49;00m
  4563	[37m[39;49;00m
  4564	([36mdefun[39;49;00m[37m [39;49;00m[31mprogress-reporter-done[39;49;00m[37m [39;49;00m([31mreporter[39;49;00m)[37m[39;49;00m
  4565	[37m  [39;49;00m[33m"[39;49;00m[33mPrint reporter's message followed by word [39;49;00m[33m\"[39;49;00m[33mdone[39;49;00m[33m\"[39;49;00m[33m in echo area.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  4566	[37m  [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m%sdone[39;49;00m[33m"[39;49;00m[37m [39;49;00m([32maref[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mreporter[39;49;00m)[37m [39;49;00m[34m3[39;49;00m)))[37m[39;49;00m
  4567	[37m[39;49;00m
  4568	([36mdefmacro[39;49;00m[37m [39;49;00m[36mdotimes-with-progress-reporter[39;49;00m[37m [39;49;00m([31mspec[39;49;00m[37m [39;49;00m[32mmessage[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m
  4569	[37m  [39;49;00m[33m"[39;49;00m[33mLoop a certain number of times and report progress in the echo area.[39;49;00m
  4570	[33mEvaluate BODY with VAR bound to successive integers running from[39;49;00m
  4571	[33m0, inclusive, to COUNT, exclusive.  Then evaluate RESULT to get[39;49;00m
  4572	[33mthe return value (nil if RESULT is omitted).[39;49;00m
  4573	[33m[39;49;00m
  4574	[33mAt each iteration MESSAGE followed by progress percentage is[39;49;00m
  4575	[33mprinted in the echo area.  After the loop is finished, MESSAGE[39;49;00m
  4576	[33mfollowed by word [39;49;00m[33m\"[39;49;00m[33mdone[39;49;00m[33m\"[39;49;00m[33m is printed.  This macro is a[39;49;00m
  4577	[33mconvenience wrapper around [39;49;00m[33m`make-progress-reporter'[39;49;00m[33m and friends.[39;49;00m
  4578	[33m[39;49;00m
  4579	[33m\([39;49;00m[33mfn (VAR COUNT [RESULT]) MESSAGE BODY...)[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  4580	[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m2[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m(([32msymbolp[39;49;00m[37m [39;49;00m[31mform[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mform[39;49;00m)[37m [39;49;00m[31mform[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)))[37m[39;49;00m
  4581	[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtemp[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m--dotimes-temp--[39;49;00m[33m"[39;49;00m))[37m[39;49;00m
  4582	[37m	[39;49;00m([31mtemp2[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m--dotimes-temp2--[39;49;00m[33m"[39;49;00m))[37m[39;49;00m
  4583	[37m	[39;49;00m([31mstart[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m
  4584	[37m	[39;49;00m([31mend[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)))[37m[39;49;00m
  4585	[37m    [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m((,[31mtemp[39;49;00m[37m [39;49;00m,[31mend[39;49;00m)[37m[39;49;00m
  4586	[37m	   [39;49;00m(,([32mcar[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)[37m [39;49;00m,[31mstart[39;49;00m)[37m[39;49;00m
  4587	[37m	   [39;49;00m(,[31mtemp2[39;49;00m[37m [39;49;00m([31mmake-progress-reporter[39;49;00m[37m [39;49;00m,[32mmessage[39;49;00m[37m [39;49;00m,[31mstart[39;49;00m[37m [39;49;00m,[31mend[39;49;00m)))[37m[39;49;00m
  4588	[37m       [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m,([32mcar[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)[37m [39;49;00m,[31mtemp[39;49;00m)[37m[39;49;00m
  4589	[37m	 [39;49;00m,@[31mbody[39;49;00m[37m[39;49;00m
  4590	[37m	 [39;49;00m([31mprogress-reporter-update[39;49;00m[37m [39;49;00m,[31mtemp2[39;49;00m[37m[39;49;00m
  4591	[37m				   [39;49;00m([34msetq[39;49;00m[37m [39;49;00m,([32mcar[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)[37m [39;49;00m([32m1+[39;49;00m[37m [39;49;00m,([32mcar[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)))))[37m[39;49;00m
  4592	[37m       [39;49;00m([31mprogress-reporter-done[39;49;00m[37m [39;49;00m,[31mtemp2[39;49;00m)[37m[39;49;00m
  4593	[37m       [39;49;00m[31mnil[39;49;00m[37m [39;49;00m,@([32mcdr[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)))))[37m[39;49;00m
  4594	[37m[39;49;00m
  4595	[37m[39;49;00m[37m[39;49;00m
  4596	[37m;;;; Comparing version strings.[39;49;00m[37m[39;49;00m
  4597	[37m[39;49;00m
  4598	([34mdefconst[39;49;00m[37m [39;49;00m[31mversion-separator[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  4599	[37m  [39;49;00m[33m"[39;49;00m[33mSpecify the string used to separate the version elements.[39;49;00m
  4600	[33m[39;49;00m
  4601	[33mUsually the separator is [39;49;00m[33m\"[39;49;00m[33m.[39;49;00m[33m\"[39;49;00m[33m, but it can be any other string.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  4602	[37m[39;49;00m
  4603	[37m[39;49;00m
  4604	([34mdefconst[39;49;00m[37m [39;49;00m[31mversion-regexp-alist[39;49;00m[37m[39;49;00m
  4605	[37m  [39;49;00m'(([33m"[39;49;00m[33m^[-_+ ]?snapshot$[39;49;00m[33m"[39;49;00m[37m                                 [39;49;00m.[37m [39;49;00m[34m-4[39;49;00m)[37m[39;49;00m
  4606	[37m    [39;49;00m[37m;; treat "1.2.3-20050920" and "1.2-3" as snapshot releases[39;49;00m[37m[39;49;00m
  4607	[37m    [39;49;00m([33m"[39;49;00m[33m^[-_+]$[39;49;00m[33m"[39;49;00m[37m                                           [39;49;00m.[37m [39;49;00m[34m-4[39;49;00m)[37m[39;49;00m
  4608	[37m    [39;49;00m[37m;; treat "1.2.3-CVS" as snapshot release[39;49;00m[37m[39;49;00m
  4609	[37m    [39;49;00m([33m"[39;49;00m[33m^[-_+ ]?[39;49;00m[33m\\[39;49;00m[33m(cvs[39;49;00m[33m\\[39;49;00m[33m|git[39;49;00m[33m\\[39;49;00m[33m|bzr[39;49;00m[33m\\[39;49;00m[33m|svn[39;49;00m[33m\\[39;49;00m[33m|hg[39;49;00m[33m\\[39;49;00m[33m|darcs[39;49;00m[33m\\[39;49;00m[33m)$[39;49;00m[33m"[39;49;00m[37m [39;49;00m.[37m [39;49;00m[34m-4[39;49;00m)[37m[39;49;00m
  4610	[37m    [39;49;00m([33m"[39;49;00m[33m^[-_+ ]?alpha$[39;49;00m[33m"[39;49;00m[37m                                    [39;49;00m.[37m [39;49;00m[34m-3[39;49;00m)[37m[39;49;00m
  4611	[37m    [39;49;00m([33m"[39;49;00m[33m^[-_+ ]?beta$[39;49;00m[33m"[39;49;00m[37m                                     [39;49;00m.[37m [39;49;00m[34m-2[39;49;00m)[37m[39;49;00m
  4612	[37m    [39;49;00m([33m"[39;49;00m[33m^[-_+ ]?[39;49;00m[33m\\[39;49;00m[33m(pre[39;49;00m[33m\\[39;49;00m[33m|rc[39;49;00m[33m\\[39;49;00m[33m)$[39;49;00m[33m"[39;49;00m[37m                           [39;49;00m.[37m [39;49;00m[34m-1[39;49;00m))[37m[39;49;00m
  4613	[37m  [39;49;00m[33m"[39;49;00m[33mSpecify association between non-numeric version and its priority.[39;49;00m
  4614	[33m[39;49;00m
  4615	[33mThis association is used to handle version string like [39;49;00m[33m\"[39;49;00m[33m1.0pre2[39;49;00m[33m\"[39;49;00m[33m,[39;49;00m
  4616	[33m\"[39;49;00m[33m0.9alpha1[39;49;00m[33m\"[39;49;00m[33m, etc.  It's used by [39;49;00m[33m`version-to-list'[39;49;00m[33m (which see) to convert the[39;49;00m
  4617	[33mnon-numeric part of a version string to an integer.  For example:[39;49;00m
  4618	[33m[39;49;00m
  4619	[33m   String Version    Integer List Version[39;49;00m
  4620	[33m   [39;49;00m[33m\"[39;49;00m[33m0.9snapshot[39;49;00m[33m\"[39;49;00m[33m     (0  9 -4)[39;49;00m
  4621	[33m   [39;49;00m[33m\"[39;49;00m[33m1.0-git[39;49;00m[33m\"[39;49;00m[33m         (1  0 -4)[39;49;00m
  4622	[33m   [39;49;00m[33m\"[39;49;00m[33m1.0pre2[39;49;00m[33m\"[39;49;00m[33m         (1  0 -1 2)[39;49;00m
  4623	[33m   [39;49;00m[33m\"[39;49;00m[33m1.0PRE2[39;49;00m[33m\"[39;49;00m[33m         (1  0 -1 2)[39;49;00m
  4624	[33m   [39;49;00m[33m\"[39;49;00m[33m22.8beta3[39;49;00m[33m\"[39;49;00m[33m       (22 8 -2 3)[39;49;00m
  4625	[33m   [39;49;00m[33m\"[39;49;00m[33m22.8 Beta3[39;49;00m[33m\"[39;49;00m[33m      (22 8 -2 3)[39;49;00m
  4626	[33m   [39;49;00m[33m\"[39;49;00m[33m0.9alpha1[39;49;00m[33m\"[39;49;00m[33m       (0  9 -3 1)[39;49;00m
  4627	[33m   [39;49;00m[33m\"[39;49;00m[33m0.9AlphA1[39;49;00m[33m\"[39;49;00m[33m       (0  9 -3 1)[39;49;00m
  4628	[33m   [39;49;00m[33m\"[39;49;00m[33m0.9 alpha[39;49;00m[33m\"[39;49;00m[33m       (0  9 -3)[39;49;00m
  4629	[33m[39;49;00m
  4630	[33mEach element has the following form:[39;49;00m
  4631	[33m[39;49;00m
  4632	[33m   (REGEXP . PRIORITY)[39;49;00m
  4633	[33m[39;49;00m
  4634	[33mWhere:[39;49;00m
  4635	[33m[39;49;00m
  4636	[33mREGEXP		regexp used to match non-numeric part of a version string.[39;49;00m
  4637	[33m		It should begin with the [39;49;00m[33m`^'[39;49;00m[33m anchor and end with a [39;49;00m[33m`$'[39;49;00m[33m to[39;49;00m
  4638	[33m		prevent false hits.  Letter-case is ignored while matching[39;49;00m
  4639	[33m		REGEXP.[39;49;00m
  4640	[33m[39;49;00m
  4641	[33mPRIORITY	a negative integer specifying non-numeric priority of REGEXP.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  4642	[37m[39;49;00m
  4643	[37m[39;49;00m
  4644	([36mdefun[39;49;00m[37m [39;49;00m[31mversion-to-list[39;49;00m[37m [39;49;00m([31mver[39;49;00m)[37m[39;49;00m
  4645	[37m  [39;49;00m[33m"[39;49;00m[33mConvert version string VER into a list of integers.[39;49;00m
  4646	[33m[39;49;00m
  4647	[33mThe version syntax is given by the following EBNF:[39;49;00m
  4648	[33m[39;49;00m
  4649	[33m   VERSION ::= NUMBER ( SEPARATOR NUMBER )*.[39;49;00m
  4650	[33m[39;49;00m
  4651	[33m   NUMBER ::= (0|1|2|3|4|5|6|7|8|9)+.[39;49;00m
  4652	[33m[39;49;00m
  4653	[33m   SEPARATOR ::= [39;49;00m[33m`version-separator'[39;49;00m[33m (which see)[39;49;00m
  4654	[33m	       | [39;49;00m[33m`version-regexp-alist'[39;49;00m[33m (which see).[39;49;00m
  4655	[33m[39;49;00m
  4656	[33mThe NUMBER part is optional if SEPARATOR is a match for an element[39;49;00m
  4657	[33min [39;49;00m[33m`version-regexp-alist'[39;49;00m[33m.[39;49;00m
  4658	[33m[39;49;00m
  4659	[33mExamples of valid version syntax:[39;49;00m
  4660	[33m[39;49;00m
  4661	[33m   1.0pre2   1.0.7.5   22.8beta3   0.9alpha1   6.9.30Beta[39;49;00m
  4662	[33m[39;49;00m
  4663	[33mExamples of invalid version syntax:[39;49;00m
  4664	[33m[39;49;00m
  4665	[33m   1.0prepre2   1.0..7.5   22.8X3   alpha3.2   .5[39;49;00m
  4666	[33m[39;49;00m
  4667	[33mExamples of version conversion:[39;49;00m
  4668	[33m[39;49;00m
  4669	[33m   Version String    Version as a List of Integers[39;49;00m
  4670	[33m   [39;49;00m[33m\"[39;49;00m[33m1.0.7.5[39;49;00m[33m\"[39;49;00m[33m         (1  0  7 5)[39;49;00m
  4671	[33m   [39;49;00m[33m\"[39;49;00m[33m1.0pre2[39;49;00m[33m\"[39;49;00m[33m         (1  0 -1 2)[39;49;00m
  4672	[33m   [39;49;00m[33m\"[39;49;00m[33m1.0PRE2[39;49;00m[33m\"[39;49;00m[33m         (1  0 -1 2)[39;49;00m
  4673	[33m   [39;49;00m[33m\"[39;49;00m[33m22.8beta3[39;49;00m[33m\"[39;49;00m[33m       (22 8 -2 3)[39;49;00m
  4674	[33m   [39;49;00m[33m\"[39;49;00m[33m22.8Beta3[39;49;00m[33m\"[39;49;00m[33m       (22 8 -2 3)[39;49;00m
  4675	[33m   [39;49;00m[33m\"[39;49;00m[33m0.9alpha1[39;49;00m[33m\"[39;49;00m[33m       (0  9 -3 1)[39;49;00m
  4676	[33m   [39;49;00m[33m\"[39;49;00m[33m0.9AlphA1[39;49;00m[33m\"[39;49;00m[33m       (0  9 -3 1)[39;49;00m
  4677	[33m   [39;49;00m[33m\"[39;49;00m[33m0.9alpha[39;49;00m[33m\"[39;49;00m[33m        (0  9 -3)[39;49;00m
  4678	[33m   [39;49;00m[33m\"[39;49;00m[33m0.9snapshot[39;49;00m[33m\"[39;49;00m[33m     (0  9 -4)[39;49;00m
  4679	[33m   [39;49;00m[33m\"[39;49;00m[33m1.0-git[39;49;00m[33m\"[39;49;00m[33m         (1  0 -4)[39;49;00m
  4680	[33m[39;49;00m
  4681	[33mSee documentation for [39;49;00m[33m`version-separator'[39;49;00m[33m and [39;49;00m[33m`version-regexp-alist'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  4682	[37m  [39;49;00m([34mor[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m[31mver[39;49;00m)[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31mver[39;49;00m)[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m
  4683	[37m      [39;49;00m([36merror[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mInvalid version string: '%s'[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mver[39;49;00m))[37m[39;49;00m
  4684	[37m  [39;49;00m[37m;; Change .x.y to 0.x.y[39;49;00m[37m[39;49;00m
  4685	[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32m>=[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31mver[39;49;00m)[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31mversion-separator[39;49;00m))[37m[39;49;00m
  4686	[37m	   [39;49;00m([32mstring-equal[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[31mver[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31mversion-separator[39;49;00m))[37m[39;49;00m
  4687	[37m			 [39;49;00m[31mversion-separator[39;49;00m))[37m[39;49;00m
  4688	[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mver[39;49;00m[37m [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m0[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mver[39;49;00m)))[37m[39;49;00m
  4689	[37m  [39;49;00m([36msave-match-data[39;49;00m[37m[39;49;00m
  4690	[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mi[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m
  4691	[37m	  [39;49;00m([31mcase-fold-search[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m		[39;49;00m[37m; ignore case in matching[39;49;00m[37m[39;49;00m
  4692	[37m	  [39;49;00m[31mlst[39;49;00m[37m [39;49;00m[31ms[39;49;00m[37m [39;49;00m[31mal[39;49;00m)[37m[39;49;00m
  4693	[37m      [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31ms[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m[0-9]+[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mver[39;49;00m[37m [39;49;00m[31mi[39;49;00m))[37m[39;49;00m
  4694	[37m		  [39;49;00m([32m=[39;49;00m[37m [39;49;00m[31ms[39;49;00m[37m [39;49;00m[31mi[39;49;00m))[37m[39;49;00m
  4695	[37m	[39;49;00m[37m;; handle numeric part[39;49;00m[37m[39;49;00m
  4696	[37m	[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mlst[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m([32mstring-to-number[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[31mver[39;49;00m[37m [39;49;00m[31mi[39;49;00m[37m [39;49;00m([32mmatch-end[39;49;00m[37m [39;49;00m[34m0[39;49;00m)))[37m[39;49;00m
  4697	[37m			[39;49;00m[31mlst[39;49;00m)[37m[39;49;00m
  4698	[37m	      [39;49;00m[31mi[39;49;00m[37m   [39;49;00m([32mmatch-end[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m
  4699	[37m	[39;49;00m[37m;; handle non-numeric part[39;49;00m[37m[39;49;00m
  4700	[37m	[39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31ms[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m[^0-9]+[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mver[39;49;00m[37m [39;49;00m[31mi[39;49;00m))[37m[39;49;00m
  4701	[37m		   [39;49;00m([32m=[39;49;00m[37m [39;49;00m[31ms[39;49;00m[37m [39;49;00m[31mi[39;49;00m))[37m[39;49;00m
  4702	[37m	  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31ms[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[31mver[39;49;00m[37m [39;49;00m[31mi[39;49;00m[37m [39;49;00m([32mmatch-end[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m
  4703	[37m		[39;49;00m[31mi[39;49;00m[37m [39;49;00m([32mmatch-end[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m
  4704	[37m	  [39;49;00m[37m;; handle alpha, beta, pre, etc. separator[39;49;00m[37m[39;49;00m
  4705	[37m	  [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32mstring=[39;49;00m[37m [39;49;00m[31ms[39;49;00m[37m [39;49;00m[31mversion-separator[39;49;00m)[37m[39;49;00m
  4706	[37m	    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mal[39;49;00m[37m [39;49;00m[31mversion-regexp-alist[39;49;00m)[37m[39;49;00m
  4707	[37m	    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mal[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m([31mcaar[39;49;00m[37m [39;49;00m[31mal[39;49;00m)[37m [39;49;00m[31ms[39;49;00m)))[37m[39;49;00m
  4708	[37m	      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mal[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mal[39;49;00m)))[37m[39;49;00m
  4709	[37m	    [39;49;00m([34mcond[39;49;00m[37m [39;49;00m([31mal[39;49;00m[37m[39;49;00m
  4710	[37m		   [39;49;00m([36mpush[39;49;00m[37m [39;49;00m([31mcdar[39;49;00m[37m [39;49;00m[31mal[39;49;00m)[37m [39;49;00m[31mlst[39;49;00m))[37m[39;49;00m
  4711	[37m		  [39;49;00m[37m;; Convert 22.3a to 22.3.1, 22.3b to 22.3.2, etc.[39;49;00m[37m[39;49;00m
  4712	[37m		  [39;49;00m(([32mstring-match[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m^[-_+ ]?[39;49;00m[33m\\[39;49;00m[33m([a-zA-Z][39;49;00m[33m\\[39;49;00m[33m)$[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31ms[39;49;00m)[37m[39;49;00m
  4713	[37m		   [39;49;00m([36mpush[39;49;00m[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m([32maref[39;49;00m[37m [39;49;00m([32mdowncase[39;49;00m[37m [39;49;00m([31mmatch-string[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31ms[39;49;00m))[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[33m?a[39;49;00m[37m [39;49;00m[34m-1[39;49;00m)[37m[39;49;00m
  4714	[37m			 [39;49;00m[31mlst[39;49;00m))[37m[39;49;00m
  4715	[37m		  [39;49;00m([31mt[39;49;00m[37m [39;49;00m([36merror[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mInvalid version syntax: '%s'[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mver[39;49;00m))))))[37m[39;49;00m
  4716	[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[31mlst[39;49;00m)[37m[39;49;00m
  4717	[37m	  [39;49;00m([36merror[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mInvalid version syntax: '%s'[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mver[39;49;00m)[37m[39;49;00m
  4718	[37m	[39;49;00m([32mnreverse[39;49;00m[37m [39;49;00m[31mlst[39;49;00m)))))[37m[39;49;00m
  4719	[37m[39;49;00m
  4720	[37m[39;49;00m
  4721	([36mdefun[39;49;00m[37m [39;49;00m[31mversion-list-<[39;49;00m[37m [39;49;00m([31ml1[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)[37m[39;49;00m
  4722	[37m  [39;49;00m[33m"[39;49;00m[33mReturn t if L1, a list specification of a version, is lower than L2.[39;49;00m
  4723	[33m[39;49;00m
  4724	[33mNote that a version specified by the list (1) is equal to (1 0),[39;49;00m
  4725	[33m\([39;49;00m[33m1 0 0), (1 0 0 0), etc.  That is, the trailing zeros are insignificant.[39;49;00m
  4726	[33mAlso, a version given by the list (1) is higher than (1 -1), which in[39;49;00m
  4727	[33mturn is higher than (1 -2), which is higher than (1 -3).[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  4728	[37m  [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31ml1[39;49;00m[37m [39;49;00m[31ml2[39;49;00m[37m [39;49;00m([32m=[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31ml1[39;49;00m)[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)))[37m[39;49;00m
  4729	[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31ml1[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31ml1[39;49;00m)[37m[39;49;00m
  4730	[37m	  [39;49;00m[31ml2[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)))[37m[39;49;00m
  4731	[37m  [39;49;00m([34mcond[39;49;00m[37m[39;49;00m
  4732	[37m   [39;49;00m[37m;; l1 not null and l2 not null[39;49;00m[37m[39;49;00m
  4733	[37m   [39;49;00m(([34mand[39;49;00m[37m [39;49;00m[31ml1[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31ml1[39;49;00m)[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)))[37m[39;49;00m
  4734	[37m   [39;49;00m[37m;; l1 null and l2 null         ==> l1 length = l2 length[39;49;00m[37m[39;49;00m
  4735	[37m   [39;49;00m(([34mand[39;49;00m[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[31ml1[39;49;00m)[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[31ml2[39;49;00m))[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m
  4736	[37m   [39;49;00m[37m;; l1 not null and l2 null     ==> l1 length > l2 length[39;49;00m[37m[39;49;00m
  4737	[37m   [39;49;00m([31ml1[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m([31mversion-list-not-zero[39;49;00m[37m [39;49;00m[31ml1[39;49;00m)[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m
  4738	[37m   [39;49;00m[37m;; l1 null and l2 not null     ==> l2 length > l1 length[39;49;00m[37m[39;49;00m
  4739	[37m   [39;49;00m([31mt[39;49;00m[37m  [39;49;00m([32m<[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m([31mversion-list-not-zero[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)))))[37m[39;49;00m
  4740	[37m[39;49;00m
  4741	[37m[39;49;00m
  4742	([36mdefun[39;49;00m[37m [39;49;00m[31mversion-list-=[39;49;00m[37m [39;49;00m([31ml1[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)[37m[39;49;00m
  4743	[37m  [39;49;00m[33m"[39;49;00m[33mReturn t if L1, a list specification of a version, is equal to L2.[39;49;00m
  4744	[33m[39;49;00m
  4745	[33mNote that a version specified by the list (1) is equal to (1 0),[39;49;00m
  4746	[33m\([39;49;00m[33m1 0 0), (1 0 0 0), etc.  That is, the trailing zeros are insignificant.[39;49;00m
  4747	[33mAlso, a version given by the list (1) is higher than (1 -1), which in[39;49;00m
  4748	[33mturn is higher than (1 -2), which is higher than (1 -3).[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  4749	[37m  [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31ml1[39;49;00m[37m [39;49;00m[31ml2[39;49;00m[37m [39;49;00m([32m=[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31ml1[39;49;00m)[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)))[37m[39;49;00m
  4750	[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31ml1[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31ml1[39;49;00m)[37m[39;49;00m
  4751	[37m	  [39;49;00m[31ml2[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)))[37m[39;49;00m
  4752	[37m  [39;49;00m([34mcond[39;49;00m[37m[39;49;00m
  4753	[37m   [39;49;00m[37m;; l1 not null and l2 not null[39;49;00m[37m[39;49;00m
  4754	[37m   [39;49;00m(([34mand[39;49;00m[37m [39;49;00m[31ml1[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m
  4755	[37m   [39;49;00m[37m;; l1 null and l2 null     ==> l1 length = l2 length[39;49;00m[37m[39;49;00m
  4756	[37m   [39;49;00m(([34mand[39;49;00m[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[31ml1[39;49;00m)[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)))[37m[39;49;00m
  4757	[37m   [39;49;00m[37m;; l1 not null and l2 null ==> l1 length > l2 length[39;49;00m[37m[39;49;00m
  4758	[37m   [39;49;00m([31ml1[39;49;00m[37m [39;49;00m([31mzerop[39;49;00m[37m [39;49;00m([31mversion-list-not-zero[39;49;00m[37m [39;49;00m[31ml1[39;49;00m)))[37m[39;49;00m
  4759	[37m   [39;49;00m[37m;; l1 null and l2 not null ==> l2 length > l1 length[39;49;00m[37m[39;49;00m
  4760	[37m   [39;49;00m([31mt[39;49;00m[37m  [39;49;00m([31mzerop[39;49;00m[37m [39;49;00m([31mversion-list-not-zero[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)))))[37m[39;49;00m
  4761	[37m[39;49;00m
  4762	[37m[39;49;00m
  4763	([36mdefun[39;49;00m[37m [39;49;00m[31mversion-list-<=[39;49;00m[37m [39;49;00m([31ml1[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)[37m[39;49;00m
  4764	[37m  [39;49;00m[33m"[39;49;00m[33mReturn t if L1, a list specification of a version, is lower or equal to L2.[39;49;00m
  4765	[33m[39;49;00m
  4766	[33mNote that integer list (1) is equal to (1 0), (1 0 0), (1 0 0 0),[39;49;00m
  4767	[33metc.  That is, the trailing zeroes are insignificant.  Also, integer[39;49;00m
  4768	[33mlist (1) is greater than (1 -1) which is greater than (1 -2)[39;49;00m
  4769	[33mwhich is greater than (1 -3).[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  4770	[37m  [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31ml1[39;49;00m[37m [39;49;00m[31ml2[39;49;00m[37m [39;49;00m([32m=[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31ml1[39;49;00m)[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)))[37m[39;49;00m
  4771	[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31ml1[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31ml1[39;49;00m)[37m[39;49;00m
  4772	[37m	  [39;49;00m[31ml2[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)))[37m[39;49;00m
  4773	[37m  [39;49;00m([34mcond[39;49;00m[37m[39;49;00m
  4774	[37m   [39;49;00m[37m;; l1 not null and l2 not null[39;49;00m[37m[39;49;00m
  4775	[37m   [39;49;00m(([34mand[39;49;00m[37m [39;49;00m[31ml1[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31ml1[39;49;00m)[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)))[37m[39;49;00m
  4776	[37m   [39;49;00m[37m;; l1 null and l2 null     ==> l1 length = l2 length[39;49;00m[37m[39;49;00m
  4777	[37m   [39;49;00m(([34mand[39;49;00m[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[31ml1[39;49;00m)[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)))[37m[39;49;00m
  4778	[37m   [39;49;00m[37m;; l1 not null and l2 null ==> l1 length > l2 length[39;49;00m[37m[39;49;00m
  4779	[37m   [39;49;00m([31ml1[39;49;00m[37m [39;49;00m([32m<=[39;49;00m[37m [39;49;00m([31mversion-list-not-zero[39;49;00m[37m [39;49;00m[31ml1[39;49;00m)[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m
  4780	[37m   [39;49;00m[37m;; l1 null and l2 not null ==> l2 length > l1 length[39;49;00m[37m[39;49;00m
  4781	[37m   [39;49;00m([31mt[39;49;00m[37m  [39;49;00m([32m<=[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m([31mversion-list-not-zero[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)))))[37m[39;49;00m
  4782	[37m[39;49;00m
  4783	([36mdefun[39;49;00m[37m [39;49;00m[31mversion-list-not-zero[39;49;00m[37m [39;49;00m([31mlst[39;49;00m)[37m[39;49;00m
  4784	[37m  [39;49;00m[33m"[39;49;00m[33mReturn the first non-zero element of LST, which is a list of integers.[39;49;00m
  4785	[33m[39;49;00m
  4786	[33mIf all LST elements are zeros or LST is nil, return zero.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  4787	[37m  [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mlst[39;49;00m[37m [39;49;00m([31mzerop[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mlst[39;49;00m)))[37m[39;49;00m
  4788	[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mlst[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mlst[39;49;00m)))[37m[39;49;00m
  4789	[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mlst[39;49;00m[37m[39;49;00m
  4790	[37m      [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mlst[39;49;00m)[37m[39;49;00m
  4791	[37m    [39;49;00m[37m;; there is no element different of zero[39;49;00m[37m[39;49;00m
  4792	[37m    [39;49;00m[34m0[39;49;00m))[37m[39;49;00m
  4793	[37m[39;49;00m
  4794	[37m[39;49;00m
  4795	([36mdefun[39;49;00m[37m [39;49;00m[31mversion<[39;49;00m[37m [39;49;00m([31mv1[39;49;00m[37m [39;49;00m[31mv2[39;49;00m)[37m[39;49;00m
  4796	[37m  [39;49;00m[33m"[39;49;00m[33mReturn t if version V1 is lower (older) than V2.[39;49;00m
  4797	[33m[39;49;00m
  4798	[33mNote that version string [39;49;00m[33m\"[39;49;00m[33m1[39;49;00m[33m\"[39;49;00m[33m is equal to [39;49;00m[33m\"[39;49;00m[33m1.0[39;49;00m[33m\"[39;49;00m[33m, [39;49;00m[33m\"[39;49;00m[33m1.0.0[39;49;00m[33m\"[39;49;00m[33m, [39;49;00m[33m\"[39;49;00m[33m1.0.0.0[39;49;00m[33m\"[39;49;00m[33m,[39;49;00m
  4799	[33metc.  That is, the trailing [39;49;00m[33m\"[39;49;00m[33m.0[39;49;00m[33m\"[39;49;00m[33ms are insignificant.  Also, version[39;49;00m
  4800	[33mstring [39;49;00m[33m\"[39;49;00m[33m1[39;49;00m[33m\"[39;49;00m[33m is higher (newer) than [39;49;00m[33m\"[39;49;00m[33m1pre[39;49;00m[33m\"[39;49;00m[33m, which is higher than [39;49;00m[33m\"[39;49;00m[33m1beta[39;49;00m[33m\"[39;49;00m[33m,[39;49;00m
  4801	[33mwhich is higher than [39;49;00m[33m\"[39;49;00m[33m1alpha[39;49;00m[33m\"[39;49;00m[33m, which is higher than [39;49;00m[33m\"[39;49;00m[33m1snapshot[39;49;00m[33m\"[39;49;00m[33m.[39;49;00m
  4802	[33mAlso, [39;49;00m[33m\"[39;49;00m[33m-GIT[39;49;00m[33m\"[39;49;00m[33m, [39;49;00m[33m\"[39;49;00m[33m-CVS[39;49;00m[33m\"[39;49;00m[33m and [39;49;00m[33m\"[39;49;00m[33m-NNN[39;49;00m[33m\"[39;49;00m[33m are treated as snapshot versions.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  4803	[37m  [39;49;00m([31mversion-list-<[39;49;00m[37m [39;49;00m([31mversion-to-list[39;49;00m[37m [39;49;00m[31mv1[39;49;00m)[37m [39;49;00m([31mversion-to-list[39;49;00m[37m [39;49;00m[31mv2[39;49;00m)))[37m[39;49;00m
  4804	[37m[39;49;00m
  4805	([36mdefun[39;49;00m[37m [39;49;00m[31mversion<=[39;49;00m[37m [39;49;00m([31mv1[39;49;00m[37m [39;49;00m[31mv2[39;49;00m)[37m[39;49;00m
  4806	[37m  [39;49;00m[33m"[39;49;00m[33mReturn t if version V1 is lower (older) than or equal to V2.[39;49;00m
  4807	[33m[39;49;00m
  4808	[33mNote that version string [39;49;00m[33m\"[39;49;00m[33m1[39;49;00m[33m\"[39;49;00m[33m is equal to [39;49;00m[33m\"[39;49;00m[33m1.0[39;49;00m[33m\"[39;49;00m[33m, [39;49;00m[33m\"[39;49;00m[33m1.0.0[39;49;00m[33m\"[39;49;00m[33m, [39;49;00m[33m\"[39;49;00m[33m1.0.0.0[39;49;00m[33m\"[39;49;00m[33m,[39;49;00m
  4809	[33metc.  That is, the trailing [39;49;00m[33m\"[39;49;00m[33m.0[39;49;00m[33m\"[39;49;00m[33ms are insignificant.  Also, version[39;49;00m
  4810	[33mstring [39;49;00m[33m\"[39;49;00m[33m1[39;49;00m[33m\"[39;49;00m[33m is higher (newer) than [39;49;00m[33m\"[39;49;00m[33m1pre[39;49;00m[33m\"[39;49;00m[33m, which is higher than [39;49;00m[33m\"[39;49;00m[33m1beta[39;49;00m[33m\"[39;49;00m[33m,[39;49;00m
  4811	[33mwhich is higher than [39;49;00m[33m\"[39;49;00m[33m1alpha[39;49;00m[33m\"[39;49;00m[33m, which is higher than [39;49;00m[33m\"[39;49;00m[33m1snapshot[39;49;00m[33m\"[39;49;00m[33m.[39;49;00m
  4812	[33mAlso, [39;49;00m[33m\"[39;49;00m[33m-GIT[39;49;00m[33m\"[39;49;00m[33m, [39;49;00m[33m\"[39;49;00m[33m-CVS[39;49;00m[33m\"[39;49;00m[33m and [39;49;00m[33m\"[39;49;00m[33m-NNN[39;49;00m[33m\"[39;49;00m[33m are treated as snapshot versions.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  4813	[37m  [39;49;00m([31mversion-list-<=[39;49;00m[37m [39;49;00m([31mversion-to-list[39;49;00m[37m [39;49;00m[31mv1[39;49;00m)[37m [39;49;00m([31mversion-to-list[39;49;00m[37m [39;49;00m[31mv2[39;49;00m)))[37m[39;49;00m
  4814	[37m[39;49;00m
  4815	([36mdefun[39;49;00m[37m [39;49;00m[31mversion=[39;49;00m[37m [39;49;00m([31mv1[39;49;00m[37m [39;49;00m[31mv2[39;49;00m)[37m[39;49;00m
  4816	[37m  [39;49;00m[33m"[39;49;00m[33mReturn t if version V1 is equal to V2.[39;49;00m
  4817	[33m[39;49;00m
  4818	[33mNote that version string [39;49;00m[33m\"[39;49;00m[33m1[39;49;00m[33m\"[39;49;00m[33m is equal to [39;49;00m[33m\"[39;49;00m[33m1.0[39;49;00m[33m\"[39;49;00m[33m, [39;49;00m[33m\"[39;49;00m[33m1.0.0[39;49;00m[33m\"[39;49;00m[33m, [39;49;00m[33m\"[39;49;00m[33m1.0.0.0[39;49;00m[33m\"[39;49;00m[33m,[39;49;00m
  4819	[33metc.  That is, the trailing [39;49;00m[33m\"[39;49;00m[33m.0[39;49;00m[33m\"[39;49;00m[33ms are insignificant.  Also, version[39;49;00m
  4820	[33mstring [39;49;00m[33m\"[39;49;00m[33m1[39;49;00m[33m\"[39;49;00m[33m is higher (newer) than [39;49;00m[33m\"[39;49;00m[33m1pre[39;49;00m[33m\"[39;49;00m[33m, which is higher than [39;49;00m[33m\"[39;49;00m[33m1beta[39;49;00m[33m\"[39;49;00m[33m,[39;49;00m
  4821	[33mwhich is higher than [39;49;00m[33m\"[39;49;00m[33m1alpha[39;49;00m[33m\"[39;49;00m[33m, which is higher than [39;49;00m[33m\"[39;49;00m[33m1snapshot[39;49;00m[33m\"[39;49;00m[33m.[39;49;00m
  4822	[33mAlso, [39;49;00m[33m\"[39;49;00m[33m-GIT[39;49;00m[33m\"[39;49;00m[33m, [39;49;00m[33m\"[39;49;00m[33m-CVS[39;49;00m[33m\"[39;49;00m[33m and [39;49;00m[33m\"[39;49;00m[33m-NNN[39;49;00m[33m\"[39;49;00m[33m are treated as snapshot versions.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  4823	[37m  [39;49;00m([31mversion-list-=[39;49;00m[37m [39;49;00m([31mversion-to-list[39;49;00m[37m [39;49;00m[31mv1[39;49;00m)[37m [39;49;00m([31mversion-to-list[39;49;00m[37m [39;49;00m[31mv2[39;49;00m)))[37m[39;49;00m
  4824	[37m[39;49;00m
  4825	([34mdefvar[39;49;00m[37m [39;49;00m[31mpackage--builtin-versions[39;49;00m[37m[39;49;00m
  4826	[37m  [39;49;00m[37m;; Mostly populated by loaddefs.el via autoload-builtin-package-versions.[39;49;00m[37m[39;49;00m
  4827	[37m  [39;49;00m([32mpurecopy[39;49;00m[37m [39;49;00m`(([31memacs[39;49;00m[37m [39;49;00m.[37m [39;49;00m,([31mversion-to-list[39;49;00m[37m [39;49;00m[31memacs-version[39;49;00m))))[37m[39;49;00m
  4828	[37m  [39;49;00m[33m"[39;49;00m[33mAlist giving the version of each versioned builtin package.[39;49;00m
  4829	[33mI.e. each element of the list is of the form (NAME . VERSION) where[39;49;00m
  4830	[33mNAME is the package name as a symbol, and VERSION is its version[39;49;00m
  4831	[33mas a list.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  4832	[37m[39;49;00m
  4833	([36mdefun[39;49;00m[37m [39;49;00m[31mpackage--description-file[39;49;00m[37m [39;49;00m([31mdir[39;49;00m)[37m[39;49;00m
  4834	[37m  [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31msubdir[39;49;00m[37m [39;49;00m([32mfile-name-nondirectory[39;49;00m[37m[39;49;00m
  4835	[37m                         [39;49;00m([32mdirectory-file-name[39;49;00m[37m [39;49;00m[31mdir[39;49;00m))))[37m[39;49;00m
  4836	[37m            [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m([^.].*?[39;49;00m[33m\\[39;49;00m[33m)-[39;49;00m[33m\\[39;49;00m[33m([0-9]+[39;49;00m[33m\\[39;49;00m[33m(?:[.][0-9]+[39;49;00m[33m\\[39;49;00m[33m|[39;49;00m[33m\\[39;49;00m[33m(?:pre[39;49;00m[33m\\[39;49;00m[33m|beta[39;49;00m[33m\\[39;49;00m[33m|alpha[39;49;00m[33m\\[39;49;00m[33m)[0-9]+[39;49;00m[33m\\[39;49;00m[33m)*[39;49;00m[33m\\[39;49;00m[33m)[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31msubdir[39;49;00m)[37m[39;49;00m
  4837	[37m                [39;49;00m([31mmatch-string[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31msubdir[39;49;00m)[37m [39;49;00m[31msubdir[39;49;00m))[37m[39;49;00m
  4838	[37m          [39;49;00m[33m"[39;49;00m[33m-pkg.el[39;49;00m[33m"[39;49;00m))[37m[39;49;00m
  4839	[37m[39;49;00m
  4840	[37m[39;49;00m[37m[39;49;00m
  4841	[37m;;; Misc.[39;49;00m[37m[39;49;00m
  4842	([34mdefconst[39;49;00m[37m [39;49;00m[31mmenu-bar-separator[39;49;00m[37m [39;49;00m'([33m"[39;49;00m[33m--[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  4843	[37m  [39;49;00m[33m"[39;49;00m[33mSeparator for menus.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
  4844	[37m[39;49;00m
  4845	[37m;; The following statement ought to be in print.c, but `provide' can't[39;49;00m[37m[39;49;00m
  4846	[37m;; be used there.[39;49;00m[37m[39;49;00m
  4847	[37m;; http://lists.gnu.org/archive/html/emacs-devel/2009-08/msg00236.html[39;49;00m[37m[39;49;00m
  4848	([36mwhen[39;49;00m[37m [39;49;00m([32mhash-table-p[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m([32mread-from-string[39;49;00m[37m[39;49;00m
  4849	[37m			  [39;49;00m([32mprin1-to-string[39;49;00m[37m [39;49;00m([32mmake-hash-table[39;49;00m)))))[37m[39;49;00m
  4850	[37m  [39;49;00m([36mprovide[39;49;00m[37m [39;49;00m[33m'hashtable-print-readable[39;49;00m))[37m[39;49;00m
  4851	[37m[39;49;00m
  4852	[37m;; This is used in lisp/Makefile.in and in leim/Makefile.in to[39;49;00m[37m[39;49;00m
  4853	[37m;; generate file names for autoloads, custom-deps, and finder-data.[39;49;00m[37m[39;49;00m
  4854	([36mdefun[39;49;00m[37m [39;49;00m[31munmsys--file-name[39;49;00m[37m [39;49;00m([31mfile[39;49;00m)[37m[39;49;00m
  4855	[37m  [39;49;00m[33m"[39;49;00m[33mProduce the canonical file name for FILE from its MSYS form.[39;49;00m
  4856	[33m[39;49;00m
  4857	[33mOn systems other than MS-Windows, just returns FILE.[39;49;00m
  4858	[33mOn MS-Windows, converts /d/foo/bar form of file names[39;49;00m
  4859	[33mpassed by MSYS Make into d:/foo/bar that Emacs can grok.[39;49;00m
  4860	[33m[39;49;00m
  4861	[33mThis function is called from lisp/Makefile and leim/Makefile.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
  4862	[37m  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31msystem-type[39;49;00m[37m [39;49;00m[33m'windows-nt[39;49;00m)[37m[39;49;00m
  4863	[37m	     [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m`[39;49;00m[33m/[a-zA-Z]/[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mfile[39;49;00m))[37m[39;49;00m
  4864	[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mfile[39;49;00m[37m [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[31mfile[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[34m2[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m:[39;49;00m[33m"[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[31mfile[39;49;00m[37m [39;49;00m[34m2[39;49;00m))))[37m[39;49;00m
  4865	[37m  [39;49;00m[31mfile[39;49;00m)[37m[39;49;00m
  4866	[37m[39;49;00m
  4867	[37m[39;49;00m
  4868	[37m;;; subr.el ends here[39;49;00m

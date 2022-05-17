     1^I[37m;;; subr.el --- basic lisp subroutines for Emacs  -*- coding: utf-8; lexical-binding:t -*-[39;49;00m[37m[39;49;00m$
     2^I[37m[39;49;00m$
     3^I[37m;; Copyright (C) 1985-1986, 1992, 1994-1995, 1999-2015 Free Software[39;49;00m[37m[39;49;00m$
     4^I[37m;; Foundation, Inc.[39;49;00m[37m[39;49;00m$
     5^I[37m[39;49;00m$
     6^I[37m;; Maintainer: emacs-devel@gnu.org[39;49;00m[37m[39;49;00m$
     7^I[37m;; Keywords: internal[39;49;00m[37m[39;49;00m$
     8^I[37m;; Package: emacs[39;49;00m[37m[39;49;00m$
     9^I[37m[39;49;00m$
    10^I[37m;; This file is part of GNU Emacs.[39;49;00m[37m[39;49;00m$
    11^I[37m[39;49;00m$
    12^I[37m;; GNU Emacs is free software: you can redistribute it and/or modify[39;49;00m[37m[39;49;00m$
    13^I[37m;; it under the terms of the GNU General Public License as published by[39;49;00m[37m[39;49;00m$
    14^I[37m;; the Free Software Foundation, either version 3 of the License, or[39;49;00m[37m[39;49;00m$
    15^I[37m;; (at your option) any later version.[39;49;00m[37m[39;49;00m$
    16^I[37m[39;49;00m$
    17^I[37m;; GNU Emacs is distributed in the hope that it will be useful,[39;49;00m[37m[39;49;00m$
    18^I[37m;; but WITHOUT ANY WARRANTY; without even the implied warranty of[39;49;00m[37m[39;49;00m$
    19^I[37m;; MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the[39;49;00m[37m[39;49;00m$
    20^I[37m;; GNU General Public License for more details.[39;49;00m[37m[39;49;00m$
    21^I[37m[39;49;00m$
    22^I[37m;; You should have received a copy of the GNU General Public License[39;49;00m[37m[39;49;00m$
    23^I[37m;; along with GNU Emacs.  If not, see <http://www.gnu.org/licenses/>.[39;49;00m[37m[39;49;00m$
    24^I[37m[39;49;00m$
    25^I[37m;;; Commentary:[39;49;00m[37m[39;49;00m$
    26^I[37m[39;49;00m$
    27^I[37m;;; Code:[39;49;00m[37m[39;49;00m$
    28^I[37m[39;49;00m$
    29^I[37m;; Beware: while this file has tag `utf-8', before it's compiled, it gets[39;49;00m[37m[39;49;00m$
    30^I[37m;; loaded as "raw-text", so non-ASCII chars won't work right during bootstrap.[39;49;00m[37m[39;49;00m$
    31^I[37m[39;49;00m$
    32^I([36mdefmacro[39;49;00m[37m [39;49;00m[36mdeclare-function[39;49;00m[37m [39;49;00m([31m_fn[39;49;00m[37m [39;49;00m[31m_file[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31m_arglist[39;49;00m[37m [39;49;00m[31m_fileonly[39;49;00m)[37m[39;49;00m$
    33^I[37m  [39;49;00m[33m"[39;49;00m[33mTell the byte-compiler that function FN is defined, in FILE.[39;49;00m$
    34^I[33mOptional ARGLIST is the argument list used by the function.[39;49;00m$
    35^I[33mThe FILE argument is not used by the byte-compiler, but by the[39;49;00m$
    36^I[33m`check-declare'[39;49;00m[33m package, which checks that FILE contains a[39;49;00m$
    37^I[33mdefinition for FN.  ARGLIST is used by both the byte-compiler[39;49;00m$
    38^I[33mand [39;49;00m[33m`check-declare'[39;49;00m[33m to check for consistency.[39;49;00m$
    39^I[33m[39;49;00m$
    40^I[33mFILE can be either a Lisp file (in which case the [39;49;00m[33m\"[39;49;00m[33m.el[39;49;00m[33m\"[39;49;00m[33m[39;49;00m$
    41^I[33mextension is optional), or a C file.  C files are expanded[39;49;00m$
    42^I[33mrelative to the Emacs [39;49;00m[33m\"[39;49;00m[33msrc/[39;49;00m[33m\"[39;49;00m[33m directory.  Lisp files are[39;49;00m$
    43^I[33msearched for using [39;49;00m[33m`locate-library'[39;49;00m[33m, and if that fails they are[39;49;00m$
    44^I[33mexpanded relative to the location of the file containing the[39;49;00m$
    45^I[33mdeclaration.  A FILE with an [39;49;00m[33m\"[39;49;00m[33mext:[39;49;00m[33m\"[39;49;00m[33m prefix is an external file.[39;49;00m$
    46^I[33m`check-declare'[39;49;00m[33m will check such files if they are found, and skip[39;49;00m$
    47^I[33mthem without error if they are not.[39;49;00m$
    48^I[33m[39;49;00m$
    49^I[33mFILEONLY non-nil means that [39;49;00m[33m`check-declare'[39;49;00m[33m will only check that[39;49;00m$
    50^I[33mFILE exists, not that it defines FN.  This is intended for[39;49;00m$
    51^I[33mfunction-definitions that [39;49;00m[33m`check-declare'[39;49;00m[33m does not recognize, e.g.[39;49;00m$
    52^I[33m`defstruct'[39;49;00m[33m.[39;49;00m$
    53^I[33m[39;49;00m$
    54^I[33mTo specify a value for FILEONLY without passing an argument list,[39;49;00m$
    55^I[33mset ARGLIST to t.  This is necessary because nil means an[39;49;00m$
    56^I[33mempty argument list, rather than an unspecified one.[39;49;00m$
    57^I[33m[39;49;00m$
    58^I[33mNote that for the purposes of [39;49;00m[33m`check-declare'[39;49;00m[33m, this statement[39;49;00m$
    59^I[33mmust be the first non-whitespace on a line.[39;49;00m$
    60^I[33m[39;49;00m$
    61^I[33mFor more information, see Info node [39;49;00m[33m`[39;49;00m[33m(elisp)Declaring Functions'.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
    62^I[37m  [39;49;00m[37m;; Does nothing - byte-compile-declare-function does the work.[39;49;00m[37m[39;49;00m$
    63^I[37m  [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
    64^I[37m[39;49;00m$
    65^I[37m[39;49;00m[37m[39;49;00m$
    66^I[37m;;;; Basic Lisp macros.[39;49;00m[37m[39;49;00m$
    67^I[37m[39;49;00m$
    68^I([36mdefalias[39;49;00m[37m [39;49;00m[33m'not[39;49;00m[37m [39;49;00m[33m'null[39;49;00m)[37m[39;49;00m$
    69^I[37m[39;49;00m$
    70^I([36mdefmacro[39;49;00m[37m [39;49;00m[36mnoreturn[39;49;00m[37m [39;49;00m([31mform[39;49;00m)[37m[39;49;00m$
    71^I[37m  [39;49;00m[33m"[39;49;00m[33mEvaluate FORM, expecting it not to return.[39;49;00m$
    72^I[33mIf FORM does return, signal an error.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
    73^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
    74^I[37m  [39;49;00m`([34mprog1[39;49;00m[37m [39;49;00m,[31mform[39;49;00m[37m[39;49;00m$
    75^I[37m     [39;49;00m([36merror[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mForm marked with [39;49;00m[33m`noreturn'[39;49;00m[33m did return[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
    76^I[37m[39;49;00m$
    77^I([36mdefmacro[39;49;00m[37m [39;49;00m[31m1value[39;49;00m[37m [39;49;00m([31mform[39;49;00m)[37m[39;49;00m$
    78^I[37m  [39;49;00m[33m"[39;49;00m[33mEvaluate FORM, expecting a constant return value.[39;49;00m$
    79^I[33mThis is the global do-nothing version.  There is also [39;49;00m[33m`testcover-1value'[39;49;00m[33m[39;49;00m$
    80^I[33mthat complains if FORM ever does return differing values.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
    81^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
    82^I[37m  [39;49;00m[31mform[39;49;00m)[37m[39;49;00m$
    83^I[37m[39;49;00m$
    84^I([36mdefmacro[39;49;00m[37m [39;49;00m[36mdef-edebug-spec[39;49;00m[37m [39;49;00m([31msymbol[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)[37m[39;49;00m$
    85^I[37m  [39;49;00m[33m"[39;49;00m[33mSet the [39;49;00m[33m`edebug-form-spec'[39;49;00m[33m property of SYMBOL according to SPEC.[39;49;00m$
    86^I[33mBoth SYMBOL and SPEC are unevaluated.  The SPEC can be:[39;49;00m$
    87^I[33m0 (instrument no arguments); t (instrument all arguments);[39;49;00m$
    88^I[33ma symbol (naming a function with an Edebug specification); or a list.[39;49;00m$
    89^I[33mThe elements of the list describe the argument types; see[39;49;00m$
    90^I[33mInfo node [39;49;00m[33m`[39;49;00m[33m(elisp)Specification List' for details.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
    91^I[37m  [39;49;00m`([32mput[39;49;00m[37m [39;49;00m([34mquote[39;49;00m[37m [39;49;00m,[31msymbol[39;49;00m)[37m [39;49;00m[33m'edebug-form-spec[39;49;00m[37m [39;49;00m([34mquote[39;49;00m[37m [39;49;00m,[31mspec[39;49;00m)))[37m[39;49;00m$
    92^I[37m[39;49;00m$
    93^I([36mdefmacro[39;49;00m[37m [39;49;00m[36mlambda[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[32mcdr[39;49;00m)[37m[39;49;00m$
    94^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn a lambda expression.[39;49;00m$
    95^I[33mA call of the form (lambda ARGS DOCSTRING INTERACTIVE BODY) is[39;49;00m$
    96^I[33mself-quoting; the result of evaluating the lambda expression is the[39;49;00m$
    97^I[33mexpression itself.  The lambda expression may then be treated as a[39;49;00m$
    98^I[33mfunction, i.e., stored as the function value of a symbol, passed to[39;49;00m$
    99^I[33m`funcall'[39;49;00m[33m or [39;49;00m[33m`mapcar'[39;49;00m[33m, etc.[39;49;00m$
   100^I[33m[39;49;00m$
   101^I[33mARGS should take the same form as an argument list for a [39;49;00m[33m`defun'[39;49;00m[33m.[39;49;00m$
   102^I[33mDOCSTRING is an optional documentation string.[39;49;00m$
   103^I[33m If present, it should describe how to call the function.[39;49;00m$
   104^I[33m But documentation strings are usually not useful in nameless functions.[39;49;00m$
   105^I[33mINTERACTIVE should be a call to the function [39;49;00m[33m`interactive'[39;49;00m[33m, which see.[39;49;00m$
   106^I[33mIt may also be omitted.[39;49;00m$
   107^I[33mBODY should be a list of Lisp expressions.[39;49;00m$
   108^I[33m[39;49;00m$
   109^I[33m\([39;49;00m[33mfn ARGS [DOCSTRING] [INTERACTIVE] BODY)[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   110^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdoc-string[39;49;00m[37m [39;49;00m[34m2[39;49;00m)[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[36mdefun[39;49;00m)[37m[39;49;00m$
   111^I[37m           [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m([31m&define[39;49;00m[37m [39;49;00m[31mlambda-list[39;49;00m[37m[39;49;00m$
   112^I[37m                           [39;49;00m[[34m&optional[39;49;00m[37m [39;49;00m[32mstringp[39;49;00m][37m[39;49;00m$
   113^I[37m                           [39;49;00m[[34m&optional[39;49;00m[37m [39;49;00m([33m"[39;49;00m[33minteractive[39;49;00m[33m"[39;49;00m[37m [39;49;00m[34minteractive[39;49;00m)][37m[39;49;00m$
   114^I[37m                           [39;49;00m[31mdef-body[39;49;00m)))[37m[39;49;00m$
   115^I[37m  [39;49;00m[37m;; Note that this definition should not use backquotes; subr.el should not[39;49;00m[37m[39;49;00m$
   116^I[37m  [39;49;00m[37m;; depend on backquote.el.[39;49;00m[37m[39;49;00m$
   117^I[37m  [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'function[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[33m'lambda[39;49;00m[37m [39;49;00m[32mcdr[39;49;00m)))[37m[39;49;00m$
   118^I[37m[39;49;00m$
   119^I([36mdefmacro[39;49;00m[37m [39;49;00m[36msetq-local[39;49;00m[37m [39;49;00m([31mvar[39;49;00m[37m [39;49;00m[31mval[39;49;00m)[37m[39;49;00m$
   120^I[37m  [39;49;00m[33m"[39;49;00m[33mSet variable VAR to value VAL in current buffer.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   121^I[37m  [39;49;00m[37m;; Can't use backquote here, it's too early in the bootstrap.[39;49;00m[37m[39;49;00m$
   122^I[37m  [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'set[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'make-local-variable[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'quote[39;49;00m[37m [39;49;00m[31mvar[39;49;00m))[37m [39;49;00m[31mval[39;49;00m))[37m[39;49;00m$
   123^I[37m[39;49;00m$
   124^I([36mdefmacro[39;49;00m[37m [39;49;00m[36mdefvar-local[39;49;00m[37m [39;49;00m([31mvar[39;49;00m[37m [39;49;00m[31mval[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mdocstring[39;49;00m)[37m[39;49;00m$
   125^I[37m  [39;49;00m[33m"[39;49;00m[33mDefine VAR as a buffer-local variable with default value VAL.[39;49;00m$
   126^I[33mLike [39;49;00m[33m`defvar'[39;49;00m[33m but additionally marks the variable as being automatically[39;49;00m$
   127^I[33mbuffer-local wherever it is set.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   128^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[34mdefvar[39;49;00m)[37m [39;49;00m([31mdoc-string[39;49;00m[37m [39;49;00m[34m3[39;49;00m))[37m[39;49;00m$
   129^I[37m  [39;49;00m[37m;; Can't use backquote here, it's too early in the bootstrap.[39;49;00m[37m[39;49;00m$
   130^I[37m  [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'progn[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'defvar[39;49;00m[37m [39;49;00m[31mvar[39;49;00m[37m [39;49;00m[31mval[39;49;00m[37m [39;49;00m[31mdocstring[39;49;00m)[37m[39;49;00m$
   131^I[37m        [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'make-variable-buffer-local[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'quote[39;49;00m[37m [39;49;00m[31mvar[39;49;00m))))[37m[39;49;00m$
   132^I[37m[39;49;00m$
   133^I([36mdefun[39;49;00m[37m [39;49;00m[31mapply-partially[39;49;00m[37m [39;49;00m([31mfun[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31margs[39;49;00m)[37m[39;49;00m$
   134^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn a function that is a partial application of FUN to ARGS.[39;49;00m$
   135^I[33mARGS is a list of the first N arguments to pass to FUN.[39;49;00m$
   136^I[33mThe result is a new function which does the same as FUN, except that[39;49;00m$
   137^I[33mthe first N arguments are fixed at the values with which this function[39;49;00m$
   138^I[33mwas called.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   139^I[37m  [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31margs2[39;49;00m)[37m[39;49;00m$
   140^I[37m    [39;49;00m([32mapply[39;49;00m[37m [39;49;00m[31mfun[39;49;00m[37m [39;49;00m([32mappend[39;49;00m[37m [39;49;00m[31margs[39;49;00m[37m [39;49;00m[31margs2[39;49;00m))))[37m[39;49;00m$
   141^I[37m[39;49;00m$
   142^I([36mdefmacro[39;49;00m[37m [39;49;00m[36mpush[39;49;00m[37m [39;49;00m([31mnewelt[39;49;00m[37m [39;49;00m[31mplace[39;49;00m)[37m[39;49;00m$
   143^I[37m  [39;49;00m[33m"[39;49;00m[33mAdd NEWELT to the list stored in the generalized variable PLACE.[39;49;00m$
   144^I[33mThis is morally equivalent to (setf PLACE (cons NEWELT PLACE)),[39;49;00m$
   145^I[33mexcept that PLACE is only evaluated once (after NEWELT).[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   146^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m([31mform[39;49;00m[37m [39;49;00m[31mgv-place[39;49;00m)))[37m[39;49;00m$
   147^I[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32msymbolp[39;49;00m[37m [39;49;00m[31mplace[39;49;00m)[37m[39;49;00m$
   148^I[37m      [39;49;00m[37m;; Important special case, to avoid triggering GV too early in[39;49;00m[37m[39;49;00m$
   149^I[37m      [39;49;00m[37m;; the bootstrap.[39;49;00m[37m[39;49;00m$
   150^I[37m      [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'setq[39;49;00m[37m [39;49;00m[31mplace[39;49;00m[37m[39;49;00m$
   151^I[37m            [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'cons[39;49;00m[37m [39;49;00m[31mnewelt[39;49;00m[37m [39;49;00m[31mplace[39;49;00m))[37m[39;49;00m$
   152^I[37m    [39;49;00m([36mrequire[39;49;00m[37m [39;49;00m[33m'macroexp[39;49;00m)[37m[39;49;00m$
   153^I[37m    [39;49;00m([31mmacroexp-let2[39;49;00m[37m [39;49;00m[31mmacroexp-copyable-p[39;49;00m[37m [39;49;00m[31mv[39;49;00m[37m [39;49;00m[31mnewelt[39;49;00m[37m[39;49;00m$
   154^I[37m      [39;49;00m([31mgv-letplace[39;49;00m[37m [39;49;00m([31mgetter[39;49;00m[37m [39;49;00m[31msetter[39;49;00m)[37m [39;49;00m[31mplace[39;49;00m[37m[39;49;00m$
   155^I[37m        [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31msetter[39;49;00m[37m [39;49;00m`([32mcons[39;49;00m[37m [39;49;00m,[31mv[39;49;00m[37m [39;49;00m,[31mgetter[39;49;00m))))))[37m[39;49;00m$
   156^I[37m[39;49;00m$
   157^I([36mdefmacro[39;49;00m[37m [39;49;00m[36mpop[39;49;00m[37m [39;49;00m([31mplace[39;49;00m)[37m[39;49;00m$
   158^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn the first element of PLACE's value, and remove it from the list.[39;49;00m$
   159^I[33mPLACE must be a generalized variable whose value is a list.[39;49;00m$
   160^I[33mIf the value is nil, [39;49;00m[33m`pop'[39;49;00m[33m returns nil but does not actually[39;49;00m$
   161^I[33mchange the list.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   162^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m([31mgv-place[39;49;00m)))[37m[39;49;00m$
   163^I[37m  [39;49;00m[37m;; We use `car-safe' here instead of `car' because the behavior is the same[39;49;00m[37m[39;49;00m$
   164^I[37m  [39;49;00m[37m;; (if it's not a cons cell, the `cdr' would have signaled an error already),[39;49;00m[37m[39;49;00m$
   165^I[37m  [39;49;00m[37m;; but `car-safe' is total, so the byte-compiler can safely remove it if the[39;49;00m[37m[39;49;00m$
   166^I[37m  [39;49;00m[37m;; result is not used.[39;49;00m[37m[39;49;00m$
   167^I[37m  [39;49;00m`([32mcar-safe[39;49;00m[37m[39;49;00m$
   168^I[37m    [39;49;00m,([34mif[39;49;00m[37m [39;49;00m([32msymbolp[39;49;00m[37m [39;49;00m[31mplace[39;49;00m)[37m[39;49;00m$
   169^I[37m         [39;49;00m[37m;; So we can use `pop' in the bootstrap before `gv' can be used.[39;49;00m[37m[39;49;00m$
   170^I[37m         [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'prog1[39;49;00m[37m [39;49;00m[31mplace[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'setq[39;49;00m[37m [39;49;00m[31mplace[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'cdr[39;49;00m[37m [39;49;00m[31mplace[39;49;00m)))[37m[39;49;00m$
   171^I[37m       [39;49;00m([31mgv-letplace[39;49;00m[37m [39;49;00m([31mgetter[39;49;00m[37m [39;49;00m[31msetter[39;49;00m)[37m [39;49;00m[31mplace[39;49;00m[37m[39;49;00m$
   172^I[37m         [39;49;00m([31mmacroexp-let2[39;49;00m[37m [39;49;00m[31mmacroexp-copyable-p[39;49;00m[37m [39;49;00m[31mx[39;49;00m[37m [39;49;00m[31mgetter[39;49;00m[37m[39;49;00m$
   173^I[37m           [39;49;00m`([34mprog1[39;49;00m[37m [39;49;00m,[31mx[39;49;00m[37m [39;49;00m,([32mfuncall[39;49;00m[37m [39;49;00m[31msetter[39;49;00m[37m [39;49;00m`([32mcdr[39;49;00m[37m [39;49;00m,[31mx[39;49;00m))))))))[37m[39;49;00m$
   174^I[37m[39;49;00m$
   175^I([36mdefmacro[39;49;00m[37m [39;49;00m[36mwhen[39;49;00m[37m [39;49;00m([34mcond[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
   176^I[37m  [39;49;00m[33m"[39;49;00m[33mIf COND yields non-nil, do BODY, else return nil.[39;49;00m$
   177^I[33mWhen COND yields non-nil, eval BODY forms sequentially and return[39;49;00m$
   178^I[33mvalue of last one, or nil if there are none.[39;49;00m$
   179^I[33m[39;49;00m$
   180^I[33m\([39;49;00m[33mfn COND BODY...)[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   181^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
   182^I[37m  [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'if[39;49;00m[37m [39;49;00m[34mcond[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[33m'progn[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)))[37m[39;49;00m$
   183^I[37m[39;49;00m$
   184^I([36mdefmacro[39;49;00m[37m [39;49;00m[36munless[39;49;00m[37m [39;49;00m([34mcond[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
   185^I[37m  [39;49;00m[33m"[39;49;00m[33mIf COND yields nil, do BODY, else return nil.[39;49;00m$
   186^I[33mWhen COND yields nil, eval BODY forms sequentially and return[39;49;00m$
   187^I[33mvalue of last one, or nil if there are none.[39;49;00m$
   188^I[33m[39;49;00m$
   189^I[33m\([39;49;00m[33mfn COND BODY...)[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   190^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
   191^I[37m  [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[33m'if[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[34mcond[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mbody[39;49;00m))))[37m[39;49;00m$
   192^I[37m[39;49;00m$
   193^I([36mdefmacro[39;49;00m[37m [39;49;00m[36mdolist[39;49;00m[37m [39;49;00m([31mspec[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
   194^I[37m  [39;49;00m[33m"[39;49;00m[33mLoop over a list.[39;49;00m$
   195^I[33mEvaluate BODY with VAR bound to each car from LIST, in turn.[39;49;00m$
   196^I[33mThen evaluate RESULT to get return value, default nil.[39;49;00m$
   197^I[33m[39;49;00m$
   198^I[33m\([39;49;00m[33mfn (VAR LIST [RESULT]) BODY...)[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   199^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m(([32msymbolp[39;49;00m[37m [39;49;00m[31mform[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mform[39;49;00m)[37m [39;49;00m[31mbody[39;49;00m)))[37m[39;49;00m$
   200^I[37m  [39;49;00m[37m;; It would be cleaner to create an uninterned symbol,[39;49;00m[37m[39;49;00m$
   201^I[37m  [39;49;00m[37m;; but that uses a lot more space when many functions in many files[39;49;00m[37m[39;49;00m$
   202^I[37m  [39;49;00m[37m;; use dolist.[39;49;00m[37m[39;49;00m$
   203^I[37m  [39;49;00m[37m;; FIXME: This cost disappears in byte-compiled lexical-binding files.[39;49;00m[37m[39;49;00m$
   204^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtemp[39;49;00m[37m [39;49;00m[33m'--dolist-tail--[39;49;00m))[37m[39;49;00m$
   205^I[37m    [39;49;00m[37m;; This is not a reliable test, but it does not matter because both[39;49;00m[37m[39;49;00m$
   206^I[37m    [39;49;00m[37m;; semantics are acceptable, tho one is slightly faster with dynamic[39;49;00m[37m[39;49;00m$
   207^I[37m    [39;49;00m[37m;; scoping and the other is slightly faster (and has cleaner semantics)[39;49;00m[37m[39;49;00m$
   208^I[37m    [39;49;00m[37m;; with lexical scoping.[39;49;00m[37m[39;49;00m$
   209^I[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mlexical-binding[39;49;00m[37m[39;49;00m$
   210^I[37m        [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m((,[31mtemp[39;49;00m[37m [39;49;00m,([32mnth[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)))[37m[39;49;00m$
   211^I[37m           [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m,[31mtemp[39;49;00m[37m[39;49;00m$
   212^I[37m             [39;49;00m([34mlet[39;49;00m[37m [39;49;00m((,([32mcar[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m,[31mtemp[39;49;00m)))[37m[39;49;00m$
   213^I[37m               [39;49;00m,@[31mbody[39;49;00m[37m[39;49;00m$
   214^I[37m               [39;49;00m([34msetq[39;49;00m[37m [39;49;00m,[31mtemp[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m,[31mtemp[39;49;00m))))[37m[39;49;00m$
   215^I[37m           [39;49;00m,@([32mcdr[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)))[37m[39;49;00m$
   216^I[37m      [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m((,[31mtemp[39;49;00m[37m [39;49;00m,([32mnth[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mspec[39;49;00m))[37m[39;49;00m$
   217^I[37m             [39;49;00m,([32mcar[39;49;00m[37m [39;49;00m[31mspec[39;49;00m))[37m[39;49;00m$
   218^I[37m         [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m,[31mtemp[39;49;00m[37m[39;49;00m$
   219^I[37m           [39;49;00m([34msetq[39;49;00m[37m [39;49;00m,([32mcar[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m,[31mtemp[39;49;00m))[37m[39;49;00m$
   220^I[37m           [39;49;00m,@[31mbody[39;49;00m[37m[39;49;00m$
   221^I[37m           [39;49;00m([34msetq[39;49;00m[37m [39;49;00m,[31mtemp[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m,[31mtemp[39;49;00m)))[37m[39;49;00m$
   222^I[37m         [39;49;00m,@([34mif[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mspec[39;49;00m))[37m[39;49;00m$
   223^I[37m               [39;49;00m`(([34msetq[39;49;00m[37m [39;49;00m,([32mcar[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)[37m [39;49;00m[31mnil[39;49;00m)[37m [39;49;00m,@([32mcdr[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mspec[39;49;00m))))))))[37m[39;49;00m$
   224^I[37m[39;49;00m$
   225^I([36mdefmacro[39;49;00m[37m [39;49;00m[36mdotimes[39;49;00m[37m [39;49;00m([31mspec[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
   226^I[37m  [39;49;00m[33m"[39;49;00m[33mLoop a certain number of times.[39;49;00m$
   227^I[33mEvaluate BODY with VAR bound to successive integers running from 0,[39;49;00m$
   228^I[33minclusive, to COUNT, exclusive.  Then evaluate RESULT to get[39;49;00m$
   229^I[33mthe return value (nil if RESULT is omitted).[39;49;00m$
   230^I[33m[39;49;00m$
   231^I[33m\([39;49;00m[33mfn (VAR COUNT [RESULT]) BODY...)[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   232^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[36mdolist[39;49;00m))[37m[39;49;00m$
   233^I[37m  [39;49;00m[37m;; It would be cleaner to create an uninterned symbol,[39;49;00m[37m[39;49;00m$
   234^I[37m  [39;49;00m[37m;; but that uses a lot more space when many functions in many files[39;49;00m[37m[39;49;00m$
   235^I[37m  [39;49;00m[37m;; use dotimes.[39;49;00m[37m[39;49;00m$
   236^I[37m  [39;49;00m[37m;; FIXME: This cost disappears in byte-compiled lexical-binding files.[39;49;00m[37m[39;49;00m$
   237^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtemp[39;49;00m[37m [39;49;00m[33m'--dotimes-limit--[39;49;00m)[37m[39;49;00m$
   238^I[37m^I[39;49;00m([31mstart[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
   239^I[37m^I[39;49;00m([31mend[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)))[37m[39;49;00m$
   240^I[37m    [39;49;00m[37m;; This is not a reliable test, but it does not matter because both[39;49;00m[37m[39;49;00m$
   241^I[37m    [39;49;00m[37m;; semantics are acceptable, tho one is slightly faster with dynamic[39;49;00m[37m[39;49;00m$
   242^I[37m    [39;49;00m[37m;; scoping and the other has cleaner semantics.[39;49;00m[37m[39;49;00m$
   243^I[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mlexical-binding[39;49;00m[37m[39;49;00m$
   244^I[37m        [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mcounter[39;49;00m[37m [39;49;00m[33m'--dotimes-counter--[39;49;00m))[37m[39;49;00m$
   245^I[37m          [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m((,[31mtemp[39;49;00m[37m [39;49;00m,[31mend[39;49;00m)[37m[39;49;00m$
   246^I[37m                 [39;49;00m(,[31mcounter[39;49;00m[37m [39;49;00m,[31mstart[39;49;00m))[37m[39;49;00m$
   247^I[37m             [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m,[31mcounter[39;49;00m[37m [39;49;00m,[31mtemp[39;49;00m)[37m[39;49;00m$
   248^I[37m               [39;49;00m([34mlet[39;49;00m[37m [39;49;00m((,([32mcar[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)[37m [39;49;00m,[31mcounter[39;49;00m))[37m[39;49;00m$
   249^I[37m                 [39;49;00m,@[31mbody[39;49;00m)[37m[39;49;00m$
   250^I[37m               [39;49;00m([34msetq[39;49;00m[37m [39;49;00m,[31mcounter[39;49;00m[37m [39;49;00m([32m1+[39;49;00m[37m [39;49;00m,[31mcounter[39;49;00m)))[37m[39;49;00m$
   251^I[37m             [39;49;00m,@([34mif[39;49;00m[37m [39;49;00m([31mcddr[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)[37m[39;49;00m$
   252^I[37m                   [39;49;00m[37m;; FIXME: This let often leads to "unused var" warnings.[39;49;00m[37m[39;49;00m$
   253^I[37m                   [39;49;00m`(([34mlet[39;49;00m[37m [39;49;00m((,([32mcar[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)[37m [39;49;00m,[31mcounter[39;49;00m))[37m [39;49;00m,@([31mcddr[39;49;00m[37m [39;49;00m[31mspec[39;49;00m))))))[37m[39;49;00m$
   254^I[37m      [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m((,[31mtemp[39;49;00m[37m [39;49;00m,[31mend[39;49;00m)[37m[39;49;00m$
   255^I[37m             [39;49;00m(,([32mcar[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)[37m [39;49;00m,[31mstart[39;49;00m))[37m[39;49;00m$
   256^I[37m         [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m,([32mcar[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)[37m [39;49;00m,[31mtemp[39;49;00m)[37m[39;49;00m$
   257^I[37m           [39;49;00m,@[31mbody[39;49;00m[37m[39;49;00m$
   258^I[37m           [39;49;00m([34msetq[39;49;00m[37m [39;49;00m,([32mcar[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)[37m [39;49;00m([32m1+[39;49;00m[37m [39;49;00m,([32mcar[39;49;00m[37m [39;49;00m[31mspec[39;49;00m))))[37m[39;49;00m$
   259^I[37m         [39;49;00m,@([32mcdr[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mspec[39;49;00m))))))[37m[39;49;00m$
   260^I[37m[39;49;00m$
   261^I([36mdefmacro[39;49;00m[37m [39;49;00m[36mdeclare[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31m_specs[39;49;00m)[37m[39;49;00m$
   262^I[37m  [39;49;00m[33m"[39;49;00m[33mDo not evaluate any arguments, and return nil.[39;49;00m$
   263^I[33mIf a [39;49;00m[33m`declare'[39;49;00m[33m form appears as the first form in the body of a[39;49;00m$
   264^I[33m`defun'[39;49;00m[33m or [39;49;00m[33m`defmacro'[39;49;00m[33m form, SPECS specifies various additional[39;49;00m$
   265^I[33minformation about the function or macro; these go into effect[39;49;00m$
   266^I[33mduring the evaluation of the [39;49;00m[33m`defun'[39;49;00m[33m or [39;49;00m[33m`defmacro'[39;49;00m[33m form.[39;49;00m$
   267^I[33m[39;49;00m$
   268^I[33mThe possible values of SPECS are specified by[39;49;00m$
   269^I[33m`defun-declarations-alist'[39;49;00m[33m and [39;49;00m[33m`macro-declarations-alist'[39;49;00m[33m.[39;49;00m$
   270^I[33m[39;49;00m$
   271^I[33mFor more information, see info node [39;49;00m[33m`[39;49;00m[33m(elisp)Declare Form'.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   272^I[37m  [39;49;00m[37m;; FIXME: edebug spec should pay attention to defun-declarations-alist.[39;49;00m[37m[39;49;00m$
   273^I[37m  [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
   274^I[37m[39;49;00m$
   275^I([36mdefmacro[39;49;00m[37m [39;49;00m[36mignore-errors[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
   276^I[37m  [39;49;00m[33m"[39;49;00m[33mExecute BODY; if an error occurs, return nil.[39;49;00m$
   277^I[33mOtherwise, return result of last form in BODY.[39;49;00m$
   278^I[33mSee also [39;49;00m[33m`with-demoted-errors'[39;49;00m[33m that does something similar[39;49;00m$
   279^I[33mwithout silencing all errors.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   280^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m$
   281^I[37m  [39;49;00m`([34mcondition-case[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m([34mprogn[39;49;00m[37m [39;49;00m,@[31mbody[39;49;00m)[37m [39;49;00m([36merror[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)))[37m[39;49;00m$
   282^I[37m[39;49;00m[37m[39;49;00m$
   283^I[37m;;;; Basic Lisp functions.[39;49;00m[37m[39;49;00m$
   284^I[37m[39;49;00m$
   285^I([36mdefun[39;49;00m[37m [39;49;00m[31mignore[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31m_ignore[39;49;00m)[37m[39;49;00m$
   286^I[37m  [39;49;00m[33m"[39;49;00m[33mDo nothing and return nil.[39;49;00m$
   287^I[33mThis function accepts any number of arguments, but ignores them.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   288^I[37m  [39;49;00m([34minteractive[39;49;00m)[37m[39;49;00m$
   289^I[37m  [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
   290^I[37m[39;49;00m$
   291^I[37m;; Signal a compile-error if the first arg is missing.[39;49;00m[37m[39;49;00m$
   292^I([36mdefun[39;49;00m[37m [39;49;00m[36merror[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31margs[39;49;00m)[37m[39;49;00m$
   293^I[37m  [39;49;00m[33m"[39;49;00m[33mSignal an error, making error message by passing all args to [39;49;00m[33m`format'[39;49;00m[33m.[39;49;00m$
   294^I[33mIn Emacs, the convention is that error messages start with a capital[39;49;00m$
   295^I[33mletter but *do not* end with a period.  Please follow this convention[39;49;00m$
   296^I[33mfor the sake of consistency.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   297^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31madvertised-calling-convention[39;49;00m[37m [39;49;00m([32mstring[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31margs[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m23.1[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
   298^I[37m  [39;49;00m([32msignal[39;49;00m[37m [39;49;00m[33m'error[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m([32mapply[39;49;00m[37m [39;49;00m[33m'format[39;49;00m[37m [39;49;00m[31margs[39;49;00m))))[37m[39;49;00m$
   299^I[37m[39;49;00m$
   300^I([36mdefun[39;49;00m[37m [39;49;00m[36muser-error[39;49;00m[37m [39;49;00m([32mformat[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31margs[39;49;00m)[37m[39;49;00m$
   301^I[37m  [39;49;00m[33m"[39;49;00m[33mSignal a pilot error, making error message by passing all args to [39;49;00m[33m`format'[39;49;00m[33m.[39;49;00m$
   302^I[33mIn Emacs, the convention is that error messages start with a capital[39;49;00m$
   303^I[33mletter but *do not* end with a period.  Please follow this convention[39;49;00m$
   304^I[33mfor the sake of consistency.[39;49;00m$
   305^I[33mThis is just like [39;49;00m[33m`error'[39;49;00m[33m except that [39;49;00m[33m`user-error'[39;49;00m[33ms are expected to be the[39;49;00m$
   306^I[33mresult of an incorrect manipulation on the part of the user, rather than the[39;49;00m$
   307^I[33mresult of an actual problem.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   308^I[37m  [39;49;00m([32msignal[39;49;00m[37m [39;49;00m[33m'user-error[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m([32mapply[39;49;00m[37m [39;49;00m[32m#'[39;49;00m[32mformat[39;49;00m[37m [39;49;00m[32mformat[39;49;00m[37m [39;49;00m[31margs[39;49;00m))))[37m[39;49;00m$
   309^I[37m[39;49;00m$
   310^I([36mdefun[39;49;00m[37m [39;49;00m[31mdefine-error[39;49;00m[37m [39;49;00m([31mname[39;49;00m[37m [39;49;00m[32mmessage[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mparent[39;49;00m)[37m[39;49;00m$
   311^I[37m  [39;49;00m[33m"[39;49;00m[33mDefine NAME as a new error signal.[39;49;00m$
   312^I[33mMESSAGE is a string that will be output to the echo area if such an error[39;49;00m$
   313^I[33mis signaled without being caught by a [39;49;00m[33m`condition-case'[39;49;00m[33m.[39;49;00m$
   314^I[33mPARENT is either a signal or a list of signals from which it inherits.[39;49;00m$
   315^I[33mDefaults to [39;49;00m[33m`error'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   316^I[37m  [39;49;00m([36munless[39;49;00m[37m [39;49;00m[31mparent[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mparent[39;49;00m[37m [39;49;00m[33m'error[39;49;00m))[37m[39;49;00m$
   317^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mconditions[39;49;00m[37m[39;49;00m$
   318^I[37m         [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mparent[39;49;00m)[37m[39;49;00m$
   319^I[37m             [39;49;00m([32mapply[39;49;00m[37m [39;49;00m[32m#'[39;49;00m[32mappend[39;49;00m[37m[39;49;00m$
   320^I[37m                    [39;49;00m([32mmapcar[39;49;00m[37m [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31mparent[39;49;00m)[37m[39;49;00m$
   321^I[37m                              [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mparent[39;49;00m[37m[39;49;00m$
   322^I[37m                                    [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mget[39;49;00m[37m [39;49;00m[31mparent[39;49;00m[37m [39;49;00m[33m'error-conditions[39;49;00m)[37m[39;49;00m$
   323^I[37m                                        [39;49;00m([36merror[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mUnknown signal [39;49;00m[33m`%s'[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mparent[39;49;00m))))[37m[39;49;00m$
   324^I[37m                            [39;49;00m[31mparent[39;49;00m))[37m[39;49;00m$
   325^I[37m           [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mparent[39;49;00m[37m [39;49;00m([32mget[39;49;00m[37m [39;49;00m[31mparent[39;49;00m[37m [39;49;00m[33m'error-conditions[39;49;00m)))))[37m[39;49;00m$
   326^I[37m    [39;49;00m([32mput[39;49;00m[37m [39;49;00m[31mname[39;49;00m[37m [39;49;00m[33m'error-conditions[39;49;00m[37m[39;49;00m$
   327^I[37m         [39;49;00m([31mdelete-dups[39;49;00m[37m [39;49;00m([32mcopy-sequence[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mname[39;49;00m[37m [39;49;00m[31mconditions[39;49;00m))))[37m[39;49;00m$
   328^I[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[32mmessage[39;49;00m[37m [39;49;00m([32mput[39;49;00m[37m [39;49;00m[31mname[39;49;00m[37m [39;49;00m[33m'error-message[39;49;00m[37m [39;49;00m[32mmessage[39;49;00m))))[37m[39;49;00m$
   329^I[37m[39;49;00m$
   330^I[37m;; We put this here instead of in frame.el so that it's defined even on[39;49;00m[37m[39;49;00m$
   331^I[37m;; systems where frame.el isn't loaded.[39;49;00m[37m[39;49;00m$
   332^I([36mdefun[39;49;00m[37m [39;49;00m[31mframe-configuration-p[39;49;00m[37m [39;49;00m([31mobject[39;49;00m)[37m[39;49;00m$
   333^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn non-nil if OBJECT seems to be a frame configuration.[39;49;00m$
   334^I[33mAny list whose car is [39;49;00m[33m`frame-configuration'[39;49;00m[33m is assumed to be a frame[39;49;00m$
   335^I[33mconfiguration.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   336^I[37m  [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mobject[39;49;00m)[37m[39;49;00m$
   337^I[37m       [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mobject[39;49;00m)[37m [39;49;00m[33m'frame-configuration[39;49;00m)))[37m[39;49;00m$
   338^I[37m[39;49;00m$
   339^I[37m[39;49;00m[37m[39;49;00m$
   340^I[37m;;;; List functions.[39;49;00m[37m[39;49;00m$
   341^I[37m[39;49;00m$
   342^I([36mdefsubst[39;49;00m[37m [39;49;00m[31mcaar[39;49;00m[37m [39;49;00m([31mx[39;49;00m)[37m[39;49;00m$
   343^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn the car of the car of X.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   344^I[37m  [39;49;00m([32mcar[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mx[39;49;00m)))[37m[39;49;00m$
   345^I[37m[39;49;00m$
   346^I([36mdefsubst[39;49;00m[37m [39;49;00m[31mcadr[39;49;00m[37m [39;49;00m([31mx[39;49;00m)[37m[39;49;00m$
   347^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn the car of the cdr of X.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   348^I[37m  [39;49;00m([32mcar[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mx[39;49;00m)))[37m[39;49;00m$
   349^I[37m[39;49;00m$
   350^I([36mdefsubst[39;49;00m[37m [39;49;00m[31mcdar[39;49;00m[37m [39;49;00m([31mx[39;49;00m)[37m[39;49;00m$
   351^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn the cdr of the car of X.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   352^I[37m  [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mx[39;49;00m)))[37m[39;49;00m$
   353^I[37m[39;49;00m$
   354^I([36mdefsubst[39;49;00m[37m [39;49;00m[31mcddr[39;49;00m[37m [39;49;00m([31mx[39;49;00m)[37m[39;49;00m$
   355^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn the cdr of the cdr of X.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   356^I[37m  [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mx[39;49;00m)))[37m[39;49;00m$
   357^I[37m[39;49;00m$
   358^I([36mdefun[39;49;00m[37m [39;49;00m[31mlast[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mn[39;49;00m)[37m[39;49;00m$
   359^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn the last link of LIST.  Its car is the last element.[39;49;00m$
   360^I[33mIf LIST is nil, return nil.[39;49;00m$
   361^I[33mIf N is non-nil, return the Nth-to-last link of LIST.[39;49;00m$
   362^I[33mIf N is bigger than the length of LIST, return LIST.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   363^I[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mn[39;49;00m[37m[39;49;00m$
   364^I[37m      [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32m>=[39;49;00m[37m [39;49;00m[31mn[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
   365^I[37m           [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mm[39;49;00m[37m [39;49;00m([32msafe-length[39;49;00m[37m [39;49;00m[32mlist[39;49;00m)))[37m[39;49;00m$
   366^I[37m             [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m[31mn[39;49;00m[37m [39;49;00m[31mm[39;49;00m)[37m [39;49;00m([32mnthcdr[39;49;00m[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m[31mm[39;49;00m[37m [39;49;00m[31mn[39;49;00m)[37m [39;49;00m[32mlist[39;49;00m)[37m [39;49;00m[32mlist[39;49;00m)))[37m[39;49;00m$
   367^I[37m    [39;49;00m([34mand[39;49;00m[37m [39;49;00m[32mlist[39;49;00m[37m[39;49;00m$
   368^I[37m         [39;49;00m([32mnthcdr[39;49;00m[37m [39;49;00m([32m1-[39;49;00m[37m [39;49;00m([32msafe-length[39;49;00m[37m [39;49;00m[32mlist[39;49;00m))[37m [39;49;00m[32mlist[39;49;00m))))[37m[39;49;00m$
   369^I[37m[39;49;00m$
   370^I([36mdefun[39;49;00m[37m [39;49;00m[31mbutlast[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mn[39;49;00m)[37m[39;49;00m$
   371^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn a copy of LIST with the last N elements removed.[39;49;00m$
   372^I[33mIf N is omitted or nil, the last element is removed from the[39;49;00m$
   373^I[33mcopy.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   374^I[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mn[39;49;00m[37m [39;49;00m([32m<=[39;49;00m[37m [39;49;00m[31mn[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m [39;49;00m[32mlist[39;49;00m[37m[39;49;00m$
   375^I[37m    [39;49;00m([31mnbutlast[39;49;00m[37m [39;49;00m([32mcopy-sequence[39;49;00m[37m [39;49;00m[32mlist[39;49;00m)[37m [39;49;00m[31mn[39;49;00m)))[37m[39;49;00m$
   376^I[37m[39;49;00m$
   377^I([36mdefun[39;49;00m[37m [39;49;00m[31mnbutlast[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mn[39;49;00m)[37m[39;49;00m$
   378^I[37m  [39;49;00m[33m"[39;49;00m[33mModifies LIST to remove the last N elements.[39;49;00m$
   379^I[33mIf N is omitted or nil, remove the last element.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   380^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mm[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[32mlist[39;49;00m)))[37m[39;49;00m$
   381^I[37m    [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mn[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mn[39;49;00m[37m [39;49;00m[34m1[39;49;00m))[37m[39;49;00m$
   382^I[37m    [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m[31mn[39;49;00m[37m [39;49;00m[31mm[39;49;00m)[37m[39;49;00m$
   383^I[37m^I [39;49;00m([34mprogn[39;49;00m[37m[39;49;00m$
   384^I[37m^I   [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m[31mn[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m([32msetcdr[39;49;00m[37m [39;49;00m([32mnthcdr[39;49;00m[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m([32m1-[39;49;00m[37m [39;49;00m[31mm[39;49;00m)[37m [39;49;00m[31mn[39;49;00m)[37m [39;49;00m[32mlist[39;49;00m)[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m$
   385^I[37m^I   [39;49;00m[32mlist[39;49;00m))))[37m[39;49;00m$
   386^I[37m[39;49;00m$
   387^I([36mdefun[39;49;00m[37m [39;49;00m[31mzerop[39;49;00m[37m [39;49;00m([31mnumber[39;49;00m)[37m[39;49;00m$
   388^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn t if NUMBER is zero.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   389^I[37m  [39;49;00m[37m;; Used to be in C, but it's pointless since (= 0 n) is faster anyway because[39;49;00m[37m[39;49;00m$
   390^I[37m  [39;49;00m[37m;; = has a byte-code.[39;49;00m[37m[39;49;00m$
   391^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mcompiler-macro[39;49;00m[37m [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31m_[39;49;00m)[37m [39;49;00m`([32m=[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m,[31mnumber[39;49;00m))))[37m[39;49;00m$
   392^I[37m  [39;49;00m([32m=[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[31mnumber[39;49;00m))[37m[39;49;00m$
   393^I[37m[39;49;00m$
   394^I([36mdefun[39;49;00m[37m [39;49;00m[31mdelete-dups[39;49;00m[37m [39;49;00m([32mlist[39;49;00m)[37m[39;49;00m$
   395^I[37m  [39;49;00m[33m"[39;49;00m[33mDestructively remove [39;49;00m[33m`equal'[39;49;00m[33m duplicates from LIST.[39;49;00m$
   396^I[33mStore the result in LIST and return it.  LIST must be a proper list.[39;49;00m$
   397^I[33mOf several [39;49;00m[33m`equal'[39;49;00m[33m occurrences of an element in LIST, the first[39;49;00m$
   398^I[33mone is kept.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   399^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtail[39;49;00m[37m [39;49;00m[32mlist[39;49;00m))[37m[39;49;00m$
   400^I[37m    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m[39;49;00m$
   401^I[37m      [39;49;00m([32msetcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([32mdelete[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)))[37m[39;49;00m$
   402^I[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))))[37m[39;49;00m$
   403^I[37m  [39;49;00m[32mlist[39;49;00m)[37m[39;49;00m$
   404^I[37m[39;49;00m$
   405^I[37m;; See http://lists.gnu.org/archive/html/emacs-devel/2013-05/msg00204.html[39;49;00m[37m[39;49;00m$
   406^I([36mdefun[39;49;00m[37m [39;49;00m[31mdelete-consecutive-dups[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mcircular[39;49;00m)[37m[39;49;00m$
   407^I[37m  [39;49;00m[33m"[39;49;00m[33mDestructively remove [39;49;00m[33m`equal'[39;49;00m[33m consecutive duplicates from LIST.[39;49;00m$
   408^I[33mFirst and last elements are considered consecutive if CIRCULAR is[39;49;00m$
   409^I[33mnon-nil.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   410^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtail[39;49;00m[37m [39;49;00m[32mlist[39;49;00m)[37m [39;49;00m[31mlast[39;49;00m)[37m[39;49;00m$
   411^I[37m    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)[37m[39;49;00m$
   412^I[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mequal[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)[37m [39;49;00m([31mcadr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))[37m[39;49;00m$
   413^I[37m^I  [39;49;00m([32msetcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([31mcddr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))[37m[39;49;00m$
   414^I[37m^I[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mlast[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)[37m[39;49;00m$
   415^I[37m^I      [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))))[37m[39;49;00m$
   416^I[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mcircular[39;49;00m[37m[39;49;00m$
   417^I[37m^I     [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[32mlist[39;49;00m)[37m[39;49;00m$
   418^I[37m^I     [39;49;00m([32mequal[39;49;00m[37m [39;49;00m[31mlast[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[32mlist[39;49;00m)))[37m[39;49;00m$
   419^I[37m^I[39;49;00m([31mnbutlast[39;49;00m[37m [39;49;00m[32mlist[39;49;00m)[37m[39;49;00m$
   420^I[37m      [39;49;00m[32mlist[39;49;00m)))[37m[39;49;00m$
   421^I[37m[39;49;00m$
   422^I([36mdefun[39;49;00m[37m [39;49;00m[31mnumber-sequence[39;49;00m[37m [39;49;00m([31mfrom[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mto[39;49;00m[37m [39;49;00m[31minc[39;49;00m)[37m[39;49;00m$
   423^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn a sequence of numbers from FROM to TO (both inclusive) as a list.[39;49;00m$
   424^I[33mINC is the increment used between numbers in the sequence and defaults to 1.[39;49;00m$
   425^I[33mSo, the Nth element of the list is (+ FROM (* N INC)) where N counts from[39;49;00m$
   426^I[33mzero.  TO is only included if there is an N for which TO = FROM + N * INC.[39;49;00m$
   427^I[33mIf TO is nil or numerically equal to FROM, return (FROM).[39;49;00m$
   428^I[33mIf INC is positive and TO is less than FROM, or INC is negative[39;49;00m$
   429^I[33mand TO is larger than FROM, return nil.[39;49;00m$
   430^I[33mIf INC is zero and TO is neither nil nor numerically equal to[39;49;00m$
   431^I[33mFROM, signal an error.[39;49;00m$
   432^I[33m[39;49;00m$
   433^I[33mThis function is primarily designed for integer arguments.[39;49;00m$
   434^I[33mNevertheless, FROM, TO and INC can be integer or float.  However,[39;49;00m$
   435^I[33mfloating point arithmetic is inexact.  For instance, depending on[39;49;00m$
   436^I[33mthe machine, it may quite well happen that[39;49;00m$
   437^I[33m\([39;49;00m[33mnumber-sequence 0.4 0.6 0.2) returns the one element list (0.4),[39;49;00m$
   438^I[33mwhereas (number-sequence 0.4 0.8 0.2) returns a list with three[39;49;00m$
   439^I[33melements.  Thus, if some of the arguments are floats and one wants[39;49;00m$
   440^I[33mto make sure that TO is included, one may have to explicitly write[39;49;00m$
   441^I[33mTO as (+ FROM (* N INC)) or use a variable whose value was[39;49;00m$
   442^I[33mcomputed with this exact expression.  Alternatively, you can,[39;49;00m$
   443^I[33mof course, also replace TO with a slightly larger value[39;49;00m$
   444^I[33m\([39;49;00m[33mor a slightly more negative value if INC is negative).[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   445^I[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m[31mto[39;49;00m)[37m [39;49;00m([32m=[39;49;00m[37m [39;49;00m[31mfrom[39;49;00m[37m [39;49;00m[31mto[39;49;00m))[37m[39;49;00m$
   446^I[37m      [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[31mfrom[39;49;00m)[37m[39;49;00m$
   447^I[37m    [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31minc[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31minc[39;49;00m[37m [39;49;00m[34m1[39;49;00m))[37m[39;49;00m$
   448^I[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([31mzerop[39;49;00m[37m [39;49;00m[31minc[39;49;00m)[37m [39;49;00m([36merror[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mThe increment can not be zero[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
   449^I[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m([31mseq[39;49;00m[37m [39;49;00m([31mn[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m([31mnext[39;49;00m[37m [39;49;00m[31mfrom[39;49;00m))[37m[39;49;00m$
   450^I[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m[31minc[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
   451^I[37m          [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32m<=[39;49;00m[37m [39;49;00m[31mnext[39;49;00m[37m [39;49;00m[31mto[39;49;00m)[37m[39;49;00m$
   452^I[37m            [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mseq[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mnext[39;49;00m[37m [39;49;00m[31mseq[39;49;00m)[37m[39;49;00m$
   453^I[37m                  [39;49;00m[31mn[39;49;00m[37m [39;49;00m([32m1+[39;49;00m[37m [39;49;00m[31mn[39;49;00m)[37m[39;49;00m$
   454^I[37m                  [39;49;00m[31mnext[39;49;00m[37m [39;49;00m([32m+[39;49;00m[37m [39;49;00m[31mfrom[39;49;00m[37m [39;49;00m([32m*[39;49;00m[37m [39;49;00m[31mn[39;49;00m[37m [39;49;00m[31minc[39;49;00m))))[37m[39;49;00m$
   455^I[37m        [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32m>=[39;49;00m[37m [39;49;00m[31mnext[39;49;00m[37m [39;49;00m[31mto[39;49;00m)[37m[39;49;00m$
   456^I[37m          [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mseq[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mnext[39;49;00m[37m [39;49;00m[31mseq[39;49;00m)[37m[39;49;00m$
   457^I[37m                [39;49;00m[31mn[39;49;00m[37m [39;49;00m([32m1+[39;49;00m[37m [39;49;00m[31mn[39;49;00m)[37m[39;49;00m$
   458^I[37m                [39;49;00m[31mnext[39;49;00m[37m [39;49;00m([32m+[39;49;00m[37m [39;49;00m[31mfrom[39;49;00m[37m [39;49;00m([32m*[39;49;00m[37m [39;49;00m[31mn[39;49;00m[37m [39;49;00m[31minc[39;49;00m)))))[37m[39;49;00m$
   459^I[37m      [39;49;00m([32mnreverse[39;49;00m[37m [39;49;00m[31mseq[39;49;00m))))[37m[39;49;00m$
   460^I[37m[39;49;00m$
   461^I([36mdefun[39;49;00m[37m [39;49;00m[31mcopy-tree[39;49;00m[37m [39;49;00m([31mtree[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mvecp[39;49;00m)[37m[39;49;00m$
   462^I[37m  [39;49;00m[33m"[39;49;00m[33mMake a copy of TREE.[39;49;00m$
   463^I[33mIf TREE is a cons cell, this recursively copies both its car and its cdr.[39;49;00m$
   464^I[33mContrast to [39;49;00m[33m`copy-sequence'[39;49;00m[33m, which copies only along the cdrs.  With second[39;49;00m$
   465^I[33margument VECP, this copies vectors as well as conses.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   466^I[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mtree[39;49;00m)[37m[39;49;00m$
   467^I[37m      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m([31mresult[39;49;00m)[37m[39;49;00m$
   468^I[37m^I[39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mtree[39;49;00m)[37m[39;49;00m$
   469^I[37m^I  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mnewcar[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mtree[39;49;00m)))[37m[39;49;00m$
   470^I[37m^I    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mtree[39;49;00m))[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mvecp[39;49;00m[37m [39;49;00m([32mvectorp[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mtree[39;49;00m))))[37m[39;49;00m$
   471^I[37m^I^I[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mnewcar[39;49;00m[37m [39;49;00m([31mcopy-tree[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mtree[39;49;00m)[37m [39;49;00m[31mvecp[39;49;00m)))[37m[39;49;00m$
   472^I[37m^I    [39;49;00m([36mpush[39;49;00m[37m [39;49;00m[31mnewcar[39;49;00m[37m [39;49;00m[31mresult[39;49;00m))[37m[39;49;00m$
   473^I[37m^I  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mtree[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtree[39;49;00m)))[37m[39;49;00m$
   474^I[37m^I[39;49;00m([32mnconc[39;49;00m[37m [39;49;00m([32mnreverse[39;49;00m[37m [39;49;00m[31mresult[39;49;00m)[37m [39;49;00m[31mtree[39;49;00m))[37m[39;49;00m$
   475^I[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mvecp[39;49;00m[37m [39;49;00m([32mvectorp[39;49;00m[37m [39;49;00m[31mtree[39;49;00m))[37m[39;49;00m$
   476^I[37m^I[39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mi[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mtree[39;49;00m[37m [39;49;00m([32mcopy-sequence[39;49;00m[37m [39;49;00m[31mtree[39;49;00m)))))[37m[39;49;00m$
   477^I[37m^I  [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32m>=[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mi[39;49;00m[37m [39;49;00m([32m1-[39;49;00m[37m [39;49;00m[31mi[39;49;00m))[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
   478^I[37m^I    [39;49;00m([32maset[39;49;00m[37m [39;49;00m[31mtree[39;49;00m[37m [39;49;00m[31mi[39;49;00m[37m [39;49;00m([31mcopy-tree[39;49;00m[37m [39;49;00m([32maref[39;49;00m[37m [39;49;00m[31mtree[39;49;00m[37m [39;49;00m[31mi[39;49;00m)[37m [39;49;00m[31mvecp[39;49;00m)))[37m[39;49;00m$
   479^I[37m^I  [39;49;00m[31mtree[39;49;00m)[37m[39;49;00m$
   480^I[37m      [39;49;00m[31mtree[39;49;00m)))[37m[39;49;00m$
   481^I[37m[39;49;00m[37m[39;49;00m$
   482^I[37m;;;; Various list-search functions.[39;49;00m[37m[39;49;00m$
   483^I[37m[39;49;00m$
   484^I([36mdefun[39;49;00m[37m [39;49;00m[31massoc-default[39;49;00m[37m [39;49;00m([31mkey[39;49;00m[37m [39;49;00m[31malist[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mtest[39;49;00m[37m [39;49;00m[31mdefault[39;49;00m)[37m[39;49;00m$
   485^I[37m  [39;49;00m[33m"[39;49;00m[33mFind object KEY in a pseudo-alist ALIST.[39;49;00m$
   486^I[33mALIST is a list of conses or objects.  Each element[39;49;00m$
   487^I[33m (or the element's car, if it is a cons) is compared with KEY by[39;49;00m$
   488^I[33m calling TEST, with two arguments: (i) the element or its car,[39;49;00m$
   489^I[33m and (ii) KEY.[39;49;00m$
   490^I[33mIf that is non-nil, the element matches; then [39;49;00m[33m`assoc-default'[39;49;00m[33m[39;49;00m$
   491^I[33m returns the element's cdr, if it is a cons, or DEFAULT if the[39;49;00m$
   492^I[33m element is not a cons.[39;49;00m$
   493^I[33m[39;49;00m$
   494^I[33mIf no element matches, the value is nil.[39;49;00m$
   495^I[33mIf TEST is omitted or nil, [39;49;00m[33m`equal'[39;49;00m[33m is used.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   496^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m([31mfound[39;49;00m[37m [39;49;00m([31mtail[39;49;00m[37m [39;49;00m[31malist[39;49;00m)[37m [39;49;00m[31mvalue[39;49;00m)[37m[39;49;00m$
   497^I[37m    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m[31mfound[39;49;00m))[37m[39;49;00m$
   498^I[37m      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([32melt[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)))[37m[39;49;00m$
   499^I[37m^I[39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mtest[39;49;00m[37m [39;49;00m[33m'equal[39;49;00m)[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[32melt[39;49;00m)[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[32melt[39;49;00m)[37m [39;49;00m[32melt[39;49;00m)[37m [39;49;00m[31mkey[39;49;00m)[37m[39;49;00m$
   500^I[37m^I  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mfound[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m[31mvalue[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[32melt[39;49;00m)[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[32melt[39;49;00m)[37m [39;49;00m[31mdefault[39;49;00m))))[37m[39;49;00m$
   501^I[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)))[37m[39;49;00m$
   502^I[37m    [39;49;00m[31mvalue[39;49;00m))[37m[39;49;00m$
   503^I[37m[39;49;00m$
   504^I([36mdefun[39;49;00m[37m [39;49;00m[31massoc-ignore-case[39;49;00m[37m [39;49;00m([31mkey[39;49;00m[37m [39;49;00m[31malist[39;49;00m)[37m[39;49;00m$
   505^I[37m  [39;49;00m[33m"[39;49;00m[33mLike [39;49;00m[33m`assoc'[39;49;00m[33m, but ignores differences in case and text representation.[39;49;00m$
   506^I[33mKEY must be a string.  Upper-case and lower-case letters are treated as equal.[39;49;00m$
   507^I[33mUnibyte strings are converted to multibyte for comparison.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   508^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mobsolete[39;49;00m[37m [39;49;00m[32massoc-string[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m22.1[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
   509^I[37m  [39;49;00m([32massoc-string[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m[31malist[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
   510^I[37m[39;49;00m$
   511^I([36mdefun[39;49;00m[37m [39;49;00m[31massoc-ignore-representation[39;49;00m[37m [39;49;00m([31mkey[39;49;00m[37m [39;49;00m[31malist[39;49;00m)[37m[39;49;00m$
   512^I[37m  [39;49;00m[33m"[39;49;00m[33mLike [39;49;00m[33m`assoc'[39;49;00m[33m, but ignores differences in text representation.[39;49;00m$
   513^I[33mKEY must be a string.[39;49;00m$
   514^I[33mUnibyte strings are converted to multibyte for comparison.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   515^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mobsolete[39;49;00m[37m [39;49;00m[32massoc-string[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m22.1[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
   516^I[37m  [39;49;00m([32massoc-string[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m[31malist[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m$
   517^I[37m[39;49;00m$
   518^I([36mdefun[39;49;00m[37m [39;49;00m[31mmember-ignore-case[39;49;00m[37m [39;49;00m([32melt[39;49;00m[37m [39;49;00m[32mlist[39;49;00m)[37m[39;49;00m$
   519^I[37m  [39;49;00m[33m"[39;49;00m[33mLike [39;49;00m[33m`member'[39;49;00m[33m, but ignore differences in case and text representation.[39;49;00m$
   520^I[33mELT must be a string.  Upper-case and lower-case letters are treated as equal.[39;49;00m$
   521^I[33mUnibyte strings are converted to multibyte for comparison.[39;49;00m$
   522^I[33mNon-strings in LIST are ignored.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   523^I[37m  [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[32mlist[39;49;00m[37m[39;49;00m$
   524^I[37m^I      [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[32mlist[39;49;00m))[37m[39;49;00m$
   525^I[37m^I^I^I[39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m([32mcompare-strings[39;49;00m[37m [39;49;00m[32melt[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[32mlist[39;49;00m)[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mt[39;49;00m)))))[37m[39;49;00m$
   526^I[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[32mlist[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[32mlist[39;49;00m)))[37m[39;49;00m$
   527^I[37m  [39;49;00m[32mlist[39;49;00m)[37m[39;49;00m$
   528^I[37m[39;49;00m$
   529^I([36mdefun[39;49;00m[37m [39;49;00m[31massq-delete-all[39;49;00m[37m [39;49;00m([31mkey[39;49;00m[37m [39;49;00m[31malist[39;49;00m)[37m[39;49;00m$
   530^I[37m  [39;49;00m[33m"[39;49;00m[33mDelete from ALIST all elements whose car is [39;49;00m[33m`eq'[39;49;00m[33m to KEY.[39;49;00m$
   531^I[33mReturn the modified alist.[39;49;00m$
   532^I[33mElements of ALIST that are not conses are ignored.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   533^I[37m  [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31malist[39;49;00m))[37m[39;49;00m$
   534^I[37m^I      [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31malist[39;49;00m))[37m [39;49;00m[31mkey[39;49;00m))[37m[39;49;00m$
   535^I[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31malist[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31malist[39;49;00m)))[37m[39;49;00m$
   536^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtail[39;49;00m[37m [39;49;00m[31malist[39;49;00m)[37m [39;49;00m[31mtail-cdr[39;49;00m)[37m[39;49;00m$
   537^I[37m    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mtail-cdr[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))[37m[39;49;00m$
   538^I[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mtail-cdr[39;49;00m))[37m[39;49;00m$
   539^I[37m^I       [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mtail-cdr[39;49;00m))[37m [39;49;00m[31mkey[39;49;00m))[37m[39;49;00m$
   540^I[37m^I  [39;49;00m([32msetcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail-cdr[39;49;00m))[37m[39;49;00m$
   541^I[37m^I[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m[31mtail-cdr[39;49;00m))))[37m[39;49;00m$
   542^I[37m  [39;49;00m[31malist[39;49;00m)[37m[39;49;00m$
   543^I[37m[39;49;00m$
   544^I([36mdefun[39;49;00m[37m [39;49;00m[31mrassq-delete-all[39;49;00m[37m [39;49;00m([31mvalue[39;49;00m[37m [39;49;00m[31malist[39;49;00m)[37m[39;49;00m$
   545^I[37m  [39;49;00m[33m"[39;49;00m[33mDelete from ALIST all elements whose cdr is [39;49;00m[33m`eq'[39;49;00m[33m to VALUE.[39;49;00m$
   546^I[33mReturn the modified alist.[39;49;00m$
   547^I[33mElements of ALIST that are not conses are ignored.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   548^I[37m  [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31malist[39;49;00m))[37m[39;49;00m$
   549^I[37m^I      [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31malist[39;49;00m))[37m [39;49;00m[31mvalue[39;49;00m))[37m[39;49;00m$
   550^I[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31malist[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31malist[39;49;00m)))[37m[39;49;00m$
   551^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtail[39;49;00m[37m [39;49;00m[31malist[39;49;00m)[37m [39;49;00m[31mtail-cdr[39;49;00m)[37m[39;49;00m$
   552^I[37m    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mtail-cdr[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))[37m[39;49;00m$
   553^I[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mtail-cdr[39;49;00m))[37m[39;49;00m$
   554^I[37m^I       [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mtail-cdr[39;49;00m))[37m [39;49;00m[31mvalue[39;49;00m))[37m[39;49;00m$
   555^I[37m^I  [39;49;00m([32msetcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail-cdr[39;49;00m))[37m[39;49;00m$
   556^I[37m^I[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m[31mtail-cdr[39;49;00m))))[37m[39;49;00m$
   557^I[37m  [39;49;00m[31malist[39;49;00m)[37m[39;49;00m$
   558^I[37m[39;49;00m$
   559^I([36mdefun[39;49;00m[37m [39;49;00m[31malist-get[39;49;00m[37m [39;49;00m([31mkey[39;49;00m[37m [39;49;00m[31malist[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mdefault[39;49;00m[37m [39;49;00m[31mremove[39;49;00m)[37m[39;49;00m$
   560^I[37m  [39;49;00m[33m"[39;49;00m[33mGet the value associated to KEY in ALIST.[39;49;00m$
   561^I[33mDEFAULT is the value to return if KEY is not found in ALIST.[39;49;00m$
   562^I[33mREMOVE, if non-nil, means that when setting this element, we should[39;49;00m$
   563^I[33mremove the entry if the new value is [39;49;00m[33m`eql'[39;49;00m[33m to DEFAULT.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   564^I[37m  [39;49;00m([31mignore[39;49;00m[37m [39;49;00m[31mremove[39;49;00m)[37m [39;49;00m[37m;;Silence byte-compiler.[39;49;00m[37m[39;49;00m$
   565^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mx[39;49;00m[37m [39;49;00m([32massq[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m[31malist[39;49;00m)))[37m[39;49;00m$
   566^I[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mx[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mx[39;49;00m)[37m [39;49;00m[31mdefault[39;49;00m)))[37m[39;49;00m$
   567^I[37m[39;49;00m$
   568^I([36mdefun[39;49;00m[37m [39;49;00m[31mremove[39;49;00m[37m [39;49;00m([32melt[39;49;00m[37m [39;49;00m[31mseq[39;49;00m)[37m[39;49;00m$
   569^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn a copy of SEQ with all occurrences of ELT removed.[39;49;00m$
   570^I[33mSEQ must be a list, vector, or string.  The comparison is done with [39;49;00m[33m`equal'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   571^I[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mnlistp[39;49;00m[37m [39;49;00m[31mseq[39;49;00m)[37m[39;49;00m$
   572^I[37m      [39;49;00m[37m;; If SEQ isn't a list, there's no need to copy SEQ because[39;49;00m[37m[39;49;00m$
   573^I[37m      [39;49;00m[37m;; `delete' will return a new object.[39;49;00m[37m[39;49;00m$
   574^I[37m      [39;49;00m([32mdelete[39;49;00m[37m [39;49;00m[32melt[39;49;00m[37m [39;49;00m[31mseq[39;49;00m)[37m[39;49;00m$
   575^I[37m    [39;49;00m([32mdelete[39;49;00m[37m [39;49;00m[32melt[39;49;00m[37m [39;49;00m([32mcopy-sequence[39;49;00m[37m [39;49;00m[31mseq[39;49;00m))))[37m[39;49;00m$
   576^I[37m[39;49;00m$
   577^I([36mdefun[39;49;00m[37m [39;49;00m[31mremq[39;49;00m[37m [39;49;00m([32melt[39;49;00m[37m [39;49;00m[32mlist[39;49;00m)[37m[39;49;00m$
   578^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn LIST with all occurrences of ELT removed.[39;49;00m$
   579^I[33mThe comparison is done with [39;49;00m[33m`eq'[39;49;00m[33m.  Contrary to [39;49;00m[33m`delq'[39;49;00m[33m, this does not use[39;49;00m$
   580^I[33mside-effects, and the argument LIST is not modified.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   581^I[37m  [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[32melt[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[32mlist[39;49;00m))[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[32mlist[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[32mlist[39;49;00m))))[37m[39;49;00m$
   582^I[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[32melt[39;49;00m[37m [39;49;00m[32mlist[39;49;00m)[37m[39;49;00m$
   583^I[37m      [39;49;00m([32mdelq[39;49;00m[37m [39;49;00m[32melt[39;49;00m[37m [39;49;00m([32mcopy-sequence[39;49;00m[37m [39;49;00m[32mlist[39;49;00m))[37m[39;49;00m$
   584^I[37m    [39;49;00m[32mlist[39;49;00m))[37m[39;49;00m$
   585^I[37m[39;49;00m[37m[39;49;00m$
   586^I[37m;;;; Keymap support.[39;49;00m[37m[39;49;00m$
   587^I[37m[39;49;00m$
   588^I([36mdefun[39;49;00m[37m [39;49;00m[31mkbd[39;49;00m[37m [39;49;00m([31mkeys[39;49;00m)[37m[39;49;00m$
   589^I[37m  [39;49;00m[33m"[39;49;00m[33mConvert KEYS to the internal Emacs key representation.[39;49;00m$
   590^I[33mKEYS should be a string constant in the format used for[39;49;00m$
   591^I[33msaving keyboard macros (see [39;49;00m[33m`edmacro-mode'[39;49;00m[33m).[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   592^I[37m  [39;49;00m[37m;; Don't use a defalias, since the `pure' property is only true for[39;49;00m[37m[39;49;00m$
   593^I[37m  [39;49;00m[37m;; the calling convention of `kbd'.[39;49;00m[37m[39;49;00m$
   594^I[37m  [39;49;00m([31mread-kbd-macro[39;49;00m[37m [39;49;00m[31mkeys[39;49;00m))[37m[39;49;00m$
   595^I([32mput[39;49;00m[37m [39;49;00m[33m'kbd[39;49;00m[37m [39;49;00m[33m'pure[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
   596^I[37m[39;49;00m$
   597^I([36mdefun[39;49;00m[37m [39;49;00m[31mundefined[39;49;00m[37m [39;49;00m()[37m[39;49;00m$
   598^I[37m  [39;49;00m[33m"[39;49;00m[33mBeep to tell the user this binding is undefined.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   599^I[37m  [39;49;00m([34minteractive[39;49;00m)[37m[39;49;00m$
   600^I[37m  [39;49;00m([32mding[39;49;00m)[37m[39;49;00m$
   601^I[37m  [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m%s is undefined[39;49;00m[33m"[39;49;00m[37m [39;49;00m([32mkey-description[39;49;00m[37m [39;49;00m([32mthis-single-command-keys[39;49;00m)))[37m[39;49;00m$
   602^I[37m  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mdefining-kbd-macro[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
   603^I[37m  [39;49;00m([32mforce-mode-line-update[39;49;00m)[37m[39;49;00m$
   604^I[37m  [39;49;00m[37m;; If this is a down-mouse event, don't reset prefix-arg;[39;49;00m[37m[39;49;00m$
   605^I[37m  [39;49;00m[37m;; pass it to the command run by the up event.[39;49;00m[37m[39;49;00m$
   606^I[37m  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mprefix-arg[39;49;00m[37m[39;49;00m$
   607^I[37m        [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[33m'down[39;49;00m[37m [39;49;00m([31mevent-modifiers[39;49;00m[37m [39;49;00m[31mlast-command-event[39;49;00m))[37m[39;49;00m$
   608^I[37m          [39;49;00m[31mcurrent-prefix-arg[39;49;00m)))[37m[39;49;00m$
   609^I[37m[39;49;00m$
   610^I[37m;; Prevent the \{...} documentation construct[39;49;00m[37m[39;49;00m$
   611^I[37m;; from mentioning keys that run this command.[39;49;00m[37m[39;49;00m$
   612^I([32mput[39;49;00m[37m [39;49;00m[33m'undefined[39;49;00m[37m [39;49;00m[33m'suppress-keymap[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
   613^I[37m[39;49;00m$
   614^I([36mdefun[39;49;00m[37m [39;49;00m[31msuppress-keymap[39;49;00m[37m [39;49;00m([31mmap[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mnodigits[39;49;00m)[37m[39;49;00m$
   615^I[37m  [39;49;00m[33m"[39;49;00m[33mMake MAP override all normally self-inserting keys to be undefined.[39;49;00m$
   616^I[33mNormally, as an exception, digits and minus-sign are set to make prefix args,[39;49;00m$
   617^I[33mbut optional second arg NODIGITS non-nil treats them like other chars.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   618^I[37m  [39;49;00m([32mdefine-key[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m[[31mremap[39;49;00m[37m [39;49;00m[32mself-insert-command[39;49;00m][37m [39;49;00m[33m'undefined[39;49;00m)[37m[39;49;00m$
   619^I[37m  [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mnodigits[39;49;00m[37m[39;49;00m$
   620^I[37m      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m([36mloop[39;49;00m)[37m[39;49;00m$
   621^I[37m^I[39;49;00m([32mdefine-key[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m-[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m'negative-argument[39;49;00m)[37m[39;49;00m$
   622^I[37m^I[39;49;00m[37m;; Make plain numbers do numeric args.[39;49;00m[37m[39;49;00m$
   623^I[37m^I[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[36mloop[39;49;00m[37m [39;49;00m[33m?0[39;49;00m)[37m[39;49;00m$
   624^I[37m^I[39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32m<=[39;49;00m[37m [39;49;00m[36mloop[39;49;00m[37m [39;49;00m[33m?9[39;49;00m)[37m[39;49;00m$
   625^I[37m^I  [39;49;00m([32mdefine-key[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m([32mchar-to-string[39;49;00m[37m [39;49;00m[36mloop[39;49;00m)[37m [39;49;00m[33m'digit-argument[39;49;00m)[37m[39;49;00m$
   626^I[37m^I  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[36mloop[39;49;00m[37m [39;49;00m([32m1+[39;49;00m[37m [39;49;00m[36mloop[39;49;00m))))))[37m[39;49;00m$
   627^I[37m[39;49;00m$
   628^I([36mdefun[39;49;00m[37m [39;49;00m[31mmake-composed-keymap[39;49;00m[37m [39;49;00m([31mmaps[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mparent[39;49;00m)[37m[39;49;00m$
   629^I[37m  [39;49;00m[33m"[39;49;00m[33mConstruct a new keymap composed of MAPS and inheriting from PARENT.[39;49;00m$
   630^I[33mWhen looking up a key in the returned map, the key is looked in each[39;49;00m$
   631^I[33mkeymap of MAPS in turn until a binding is found.[39;49;00m$
   632^I[33mIf no binding is found in MAPS, the lookup continues in PARENT, if non-nil.[39;49;00m$
   633^I[33mAs always with keymap inheritance, a nil binding in MAPS overrides[39;49;00m$
   634^I[33many corresponding binding in PARENT, but it does not override corresponding[39;49;00m$
   635^I[33mbindings in other keymaps of MAPS.[39;49;00m$
   636^I[33mMAPS can be a list of keymaps or a single keymap.[39;49;00m$
   637^I[33mPARENT if non-nil should be a keymap.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   638^I[37m  [39;49;00m`([31mkeymap[39;49;00m[37m[39;49;00m$
   639^I[37m    [39;49;00m,@([34mif[39;49;00m[37m [39;49;00m([32mkeymapp[39;49;00m[37m [39;49;00m[31mmaps[39;49;00m)[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[31mmaps[39;49;00m)[37m [39;49;00m[31mmaps[39;49;00m)[37m[39;49;00m$
   640^I[37m    [39;49;00m,@[31mparent[39;49;00m))[37m[39;49;00m$
   641^I[37m[39;49;00m$
   642^I([36mdefun[39;49;00m[37m [39;49;00m[31mdefine-key-after[39;49;00m[37m [39;49;00m([31mkeymap[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m[31mdefinition[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mafter[39;49;00m)[37m[39;49;00m$
   643^I[37m  [39;49;00m[33m"[39;49;00m[33mAdd binding in KEYMAP for KEY => DEFINITION, right after AFTER's binding.[39;49;00m$
   644^I[33mThis is like [39;49;00m[33m`define-key'[39;49;00m[33m except that the binding for KEY is placed[39;49;00m$
   645^I[33mjust after the binding for the event AFTER, instead of at the beginning[39;49;00m$
   646^I[33mof the map.  Note that AFTER must be an event type (like KEY), NOT a command[39;49;00m$
   647^I[33m\([39;49;00m[33mlike DEFINITION).[39;49;00m$
   648^I[33m[39;49;00m$
   649^I[33mIf AFTER is t or omitted, the new binding goes at the end of the keymap.[39;49;00m$
   650^I[33mAFTER should be a single event type--a symbol or a character, not a sequence.[39;49;00m$
   651^I[33m[39;49;00m$
   652^I[33mBindings are always added before any inherited map.[39;49;00m$
   653^I[33m[39;49;00m$
   654^I[33mThe order of bindings in a keymap only matters when it is used as[39;49;00m$
   655^I[33ma menu, so this function is not useful for non-menu keymaps.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   656^I[37m  [39;49;00m([36munless[39;49;00m[37m [39;49;00m[31mafter[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mafter[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
   657^I[37m  [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mkeymapp[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m)[37m[39;49;00m$
   658^I[37m      [39;49;00m([32msignal[39;49;00m[37m [39;49;00m[33m'wrong-type-argument[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'keymapp[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m)))[37m[39;49;00m$
   659^I[37m  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m[39;49;00m$
   660^I[37m^I[39;49;00m([34mif[39;49;00m[37m [39;49;00m([32m<=[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31mkey[39;49;00m)[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m([32maref[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
   661^I[37m^I  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m[37m [39;49;00m([32mlookup-key[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m[37m[39;49;00m$
   662^I[37m^I^I^I^I   [39;49;00m([32mapply[39;49;00m[37m [39;49;00m[33m'vector[39;49;00m[37m[39;49;00m$
   663^I[37m^I^I^I^I^I  [39;49;00m([31mbutlast[39;49;00m[37m [39;49;00m([32mmapcar[39;49;00m[37m [39;49;00m[33m'identity[39;49;00m[37m [39;49;00m[31mkey[39;49;00m)))))[37m[39;49;00m$
   664^I[37m^I  [39;49;00m([32maref[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m([32m1-[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31mkey[39;49;00m)))))[37m[39;49;00m$
   665^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtail[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m)[37m [39;49;00m[31mdone[39;49;00m[37m [39;49;00m[31minserted[39;49;00m)[37m[39;49;00m$
   666^I[37m    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m[31mdone[39;49;00m)[37m [39;49;00m[31mtail[39;49;00m)[37m[39;49;00m$
   667^I[37m      [39;49;00m[37m;; Delete any earlier bindings for the same key.[39;49;00m[37m[39;49;00m$
   668^I[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mcar-safe[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)))[37m [39;49;00m[31mkey[39;49;00m)[37m[39;49;00m$
   669^I[37m^I  [39;49;00m([32msetcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))))[37m[39;49;00m$
   670^I[37m      [39;49;00m[37m;; If we hit an included map, go down that one.[39;49;00m[37m[39;49;00m$
   671^I[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mkeymapp[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)))[37m[39;49;00m$
   672^I[37m      [39;49;00m[37m;; When we reach AFTER's binding, insert the new binding after.[39;49;00m[37m[39;49;00m$
   673^I[37m      [39;49;00m[37m;; If we reach an inherited keymap, insert just before that.[39;49;00m[37m[39;49;00m$
   674^I[37m      [39;49;00m[37m;; If we reach the end of this keymap, insert at the end.[39;49;00m[37m[39;49;00m$
   675^I[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mcar-safe[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))[37m [39;49;00m[31mafter[39;49;00m)[37m[39;49;00m$
   676^I[37m^I^I   [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mafter[39;49;00m[37m [39;49;00m[31mt[39;49;00m)))[37m[39;49;00m$
   677^I[37m^I      [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))[37m [39;49;00m[33m'keymap[39;49;00m)[37m[39;49;00m$
   678^I[37m^I      [39;49;00m([32mnull[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)))[37m[39;49;00m$
   679^I[37m^I  [39;49;00m([34mprogn[39;49;00m[37m[39;49;00m$
   680^I[37m^I    [39;49;00m[37m;; Stop the scan only if we find a parent keymap.[39;49;00m[37m[39;49;00m$
   681^I[37m^I    [39;49;00m[37m;; Keep going past the inserted element[39;49;00m[37m[39;49;00m$
   682^I[37m^I    [39;49;00m[37m;; so we can delete any duplications that come later.[39;49;00m[37m[39;49;00m$
   683^I[37m^I    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))[37m [39;49;00m[33m'keymap[39;49;00m)[37m[39;49;00m$
   684^I[37m^I^I[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mdone[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
   685^I[37m^I    [39;49;00m[37m;; Don't insert more than once.[39;49;00m[37m[39;49;00m$
   686^I[37m^I    [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31minserted[39;49;00m[37m[39;49;00m$
   687^I[37m^I^I[39;49;00m([32msetcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m[31mdefinition[39;49;00m)[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))))[37m[39;49;00m$
   688^I[37m^I    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31minserted[39;49;00m[37m [39;49;00m[31mt[39;49;00m)))[37m[39;49;00m$
   689^I[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)))))[37m[39;49;00m$
   690^I[37m[39;49;00m$
   691^I([36mdefun[39;49;00m[37m [39;49;00m[31mmap-keymap-sorted[39;49;00m[37m [39;49;00m([34mfunction[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m)[37m[39;49;00m$
   692^I[37m  [39;49;00m[33m"[39;49;00m[33mImplement [39;49;00m[33m`map-keymap'[39;49;00m[33m with sorting.[39;49;00m$
   693^I[33mDon't call this function; it is for internal use only.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   694^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m([32mlist[39;49;00m)[37m[39;49;00m$
   695^I[37m    [39;49;00m([32mmap-keymap[39;49;00m[37m [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31ma[39;49;00m[37m [39;49;00m[31mb[39;49;00m)[37m [39;49;00m([36mpush[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31ma[39;49;00m[37m [39;49;00m[31mb[39;49;00m)[37m [39;49;00m[32mlist[39;49;00m))[37m[39;49;00m$
   696^I[37m                [39;49;00m[31mkeymap[39;49;00m)[37m[39;49;00m$
   697^I[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[32mlist[39;49;00m[37m [39;49;00m([32msort[39;49;00m[37m [39;49;00m[32mlist[39;49;00m[37m[39;49;00m$
   698^I[37m                     [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31ma[39;49;00m[37m [39;49;00m[31mb[39;49;00m)[37m[39;49;00m$
   699^I[37m                       [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31ma[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31ma[39;49;00m)[37m [39;49;00m[31mb[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mb[39;49;00m))[37m[39;49;00m$
   700^I[37m                       [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mintegerp[39;49;00m[37m [39;49;00m[31ma[39;49;00m)[37m[39;49;00m$
   701^I[37m                           [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mintegerp[39;49;00m[37m [39;49;00m[31mb[39;49;00m)[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m[31ma[39;49;00m[37m [39;49;00m[31mb[39;49;00m)[37m[39;49;00m$
   702^I[37m                             [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
   703^I[37m                         [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mintegerp[39;49;00m[37m [39;49;00m[31mb[39;49;00m)[37m [39;49;00m[31mt[39;49;00m[37m[39;49;00m$
   704^I[37m                           [39;49;00m[37m;; string< also accepts symbols.[39;49;00m[37m[39;49;00m$
   705^I[37m                           [39;49;00m([32mstring<[39;49;00m[37m [39;49;00m[31ma[39;49;00m[37m [39;49;00m[31mb[39;49;00m))))))[37m[39;49;00m$
   706^I[37m    [39;49;00m([36mdolist[39;49;00m[37m [39;49;00m([31mp[39;49;00m[37m [39;49;00m[32mlist[39;49;00m)[37m[39;49;00m$
   707^I[37m      [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[34mfunction[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mp[39;49;00m)[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mp[39;49;00m)))))[37m[39;49;00m$
   708^I[37m[39;49;00m$
   709^I([36mdefun[39;49;00m[37m [39;49;00m[31mkeymap--menu-item-binding[39;49;00m[37m [39;49;00m([31mval[39;49;00m)[37m[39;49;00m$
   710^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn the binding part of a menu-item.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   711^I[37m  [39;49;00m([34mcond[39;49;00m[37m[39;49;00m$
   712^I[37m   [39;49;00m(([31mnot[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mval[39;49;00m))[37m [39;49;00m[31mval[39;49;00m)[37m              [39;49;00m[37m;Not a menu-item.[39;49;00m[37m[39;49;00m$
   713^I[37m   [39;49;00m(([32meq[39;49;00m[37m [39;49;00m[33m'menu-item[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mval[39;49;00m))[37m[39;49;00m$
   714^I[37m    [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mbinding[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m[31mval[39;49;00m))[37m[39;49;00m$
   715^I[37m           [39;49;00m([31mplist[39;49;00m[37m [39;49;00m([32mnthcdr[39;49;00m[37m [39;49;00m[34m3[39;49;00m[37m [39;49;00m[31mval[39;49;00m))[37m[39;49;00m$
   716^I[37m           [39;49;00m([31mfilter[39;49;00m[37m [39;49;00m([32mplist-get[39;49;00m[37m [39;49;00m[31mplist[39;49;00m[37m [39;49;00m[36m:filter[39;49;00m)))[37m[39;49;00m$
   717^I[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mfilter[39;49;00m[37m [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mfilter[39;49;00m[37m [39;49;00m[31mbinding[39;49;00m)[37m[39;49;00m$
   718^I[37m        [39;49;00m[31mbinding[39;49;00m)))[37m[39;49;00m$
   719^I[37m   [39;49;00m(([34mand[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mval[39;49;00m))[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m([31mcadr[39;49;00m[37m [39;49;00m[31mval[39;49;00m)))[37m[39;49;00m$
   720^I[37m    [39;49;00m([31mcddr[39;49;00m[37m [39;49;00m[31mval[39;49;00m))[37m[39;49;00m$
   721^I[37m   [39;49;00m(([32mstringp[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mval[39;49;00m))[37m[39;49;00m$
   722^I[37m    [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mval[39;49;00m))[37m[39;49;00m$
   723^I[37m   [39;49;00m([31mt[39;49;00m[37m [39;49;00m[31mval[39;49;00m)))[37m                            [39;49;00m[37m;Not a menu-item either.[39;49;00m[37m[39;49;00m$
   724^I[37m[39;49;00m$
   725^I([36mdefun[39;49;00m[37m [39;49;00m[31mkeymap--menu-item-with-binding[39;49;00m[37m [39;49;00m([31mitem[39;49;00m[37m [39;49;00m[31mbinding[39;49;00m)[37m[39;49;00m$
   726^I[37m  [39;49;00m[33m"[39;49;00m[33mBuild a menu-item like ITEM but with its binding changed to BINDING.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   727^I[37m  [39;49;00m([34mcond[39;49;00m[37m[39;49;00m$
   728^I[37m   [39;49;00m(([31mnot[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mitem[39;49;00m))[37m [39;49;00m[31mbinding[39;49;00m)[37m^I^I[39;49;00m[37m;Not a menu-item.[39;49;00m[37m[39;49;00m$
   729^I[37m   [39;49;00m(([32meq[39;49;00m[37m [39;49;00m[33m'menu-item[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mitem[39;49;00m))[37m[39;49;00m$
   730^I[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mitem[39;49;00m[37m [39;49;00m([32mcopy-sequence[39;49;00m[37m [39;49;00m[31mitem[39;49;00m))[37m[39;49;00m$
   731^I[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtail[39;49;00m[37m [39;49;00m([32mnthcdr[39;49;00m[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m[31mitem[39;49;00m)))[37m[39;49;00m$
   732^I[37m      [39;49;00m([32msetcar[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m[31mbinding[39;49;00m)[37m[39;49;00m$
   733^I[37m      [39;49;00m[37m;; Remove any potential filter.[39;49;00m[37m[39;49;00m$
   734^I[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mplist-get[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)[37m [39;49;00m[36m:filter[39;49;00m)[37m[39;49;00m$
   735^I[37m          [39;49;00m([32msetcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([32mplist-put[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)[37m [39;49;00m[36m:filter[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))))[37m[39;49;00m$
   736^I[37m    [39;49;00m[31mitem[39;49;00m)[37m[39;49;00m$
   737^I[37m   [39;49;00m(([34mand[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mitem[39;49;00m))[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m([31mcadr[39;49;00m[37m [39;49;00m[31mitem[39;49;00m)))[37m[39;49;00m$
   738^I[37m    [39;49;00m([32mcons[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mitem[39;49;00m)[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m([31mcadr[39;49;00m[37m [39;49;00m[31mitem[39;49;00m)[37m [39;49;00m[31mbinding[39;49;00m)))[37m[39;49;00m$
   739^I[37m   [39;49;00m([31mt[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mitem[39;49;00m)[37m [39;49;00m[31mbinding[39;49;00m))))[37m[39;49;00m$
   740^I[37m[39;49;00m$
   741^I([36mdefun[39;49;00m[37m [39;49;00m[31mkeymap--merge-bindings[39;49;00m[37m [39;49;00m([31mval1[39;49;00m[37m [39;49;00m[31mval2[39;49;00m)[37m[39;49;00m$
   742^I[37m  [39;49;00m[33m"[39;49;00m[33mMerge bindings VAL1 and VAL2.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   743^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mmap1[39;49;00m[37m [39;49;00m([31mkeymap--menu-item-binding[39;49;00m[37m [39;49;00m[31mval1[39;49;00m))[37m[39;49;00m$
   744^I[37m        [39;49;00m([31mmap2[39;49;00m[37m [39;49;00m([31mkeymap--menu-item-binding[39;49;00m[37m [39;49;00m[31mval2[39;49;00m)))[37m[39;49;00m$
   745^I[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mkeymapp[39;49;00m[37m [39;49;00m[31mmap1[39;49;00m)[37m [39;49;00m([32mkeymapp[39;49;00m[37m [39;49;00m[31mmap2[39;49;00m)))[37m[39;49;00m$
   746^I[37m        [39;49;00m[37m;; There's nothing to merge: val1 takes precedence.[39;49;00m[37m[39;49;00m$
   747^I[37m        [39;49;00m[31mval1[39;49;00m[37m[39;49;00m$
   748^I[37m      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mmap[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'keymap[39;49;00m[37m [39;49;00m[31mmap1[39;49;00m[37m [39;49;00m[31mmap2[39;49;00m))[37m[39;49;00m$
   749^I[37m            [39;49;00m([31mitem[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mkeymapp[39;49;00m[37m [39;49;00m[31mval1[39;49;00m)[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mkeymapp[39;49;00m[37m [39;49;00m[31mval2[39;49;00m)[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mval2[39;49;00m)[37m [39;49;00m[31mval1[39;49;00m)))[37m[39;49;00m$
   750^I[37m        [39;49;00m([31mkeymap--menu-item-with-binding[39;49;00m[37m [39;49;00m[31mitem[39;49;00m[37m [39;49;00m[31mmap[39;49;00m)))))[37m[39;49;00m$
   751^I[37m[39;49;00m$
   752^I([36mdefun[39;49;00m[37m [39;49;00m[31mkeymap-canonicalize[39;49;00m[37m [39;49;00m([31mmap[39;49;00m)[37m[39;49;00m$
   753^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn a simpler equivalent keymap.[39;49;00m$
   754^I[33mThis resolves inheritance and redefinitions.  The returned keymap[39;49;00m$
   755^I[33mshould behave identically to a copy of KEYMAP w.r.t [39;49;00m[33m`lookup-key'[39;49;00m[33m[39;49;00m$
   756^I[33mand use in active keymaps and menus.[39;49;00m$
   757^I[33mSubkeymaps may be modified but are not canonicalized.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   758^I[37m  [39;49;00m[37m;; FIXME: Problem with the difference between a nil binding[39;49;00m[37m[39;49;00m$
   759^I[37m  [39;49;00m[37m;; that hides a binding in an inherited map and a nil binding that's ignored[39;49;00m[37m[39;49;00m$
   760^I[37m  [39;49;00m[37m;; to let some further binding visible.  Currently a nil binding hides all.[39;49;00m[37m[39;49;00m$
   761^I[37m  [39;49;00m[37m;; FIXME: we may want to carefully (re)order elements in case they're[39;49;00m[37m[39;49;00m$
   762^I[37m  [39;49;00m[37m;; menu-entries.[39;49;00m[37m[39;49;00m$
   763^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mbindings[39;49;00m[37m [39;49;00m())[37m[39;49;00m$
   764^I[37m        [39;49;00m([31mranges[39;49;00m[37m [39;49;00m())[37m[39;49;00m$
   765^I[37m^I[39;49;00m([31mprompt[39;49;00m[37m [39;49;00m([32mkeymap-prompt[39;49;00m[37m [39;49;00m[31mmap[39;49;00m)))[37m[39;49;00m$
   766^I[37m    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32mkeymapp[39;49;00m[37m [39;49;00m[31mmap[39;49;00m)[37m[39;49;00m$
   767^I[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m([32mmap-keymap[39;49;00m[37m [39;49;00m[37m;; -internal[39;49;00m[37m[39;49;00m$
   768^I[37m                 [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31mkey[39;49;00m[37m [39;49;00m[31mitem[39;49;00m)[37m[39;49;00m$
   769^I[37m                   [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mkey[39;49;00m)[37m[39;49;00m$
   770^I[37m                       [39;49;00m[37m;; Treat char-ranges specially.[39;49;00m[37m[39;49;00m$
   771^I[37m                       [39;49;00m([36mpush[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m[31mitem[39;49;00m)[37m [39;49;00m[31mranges[39;49;00m)[37m[39;49;00m$
   772^I[37m                     [39;49;00m([36mpush[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m[31mitem[39;49;00m)[37m [39;49;00m[31mbindings[39;49;00m)))[37m[39;49;00m$
   773^I[37m                 [39;49;00m[31mmap[39;49;00m)))[37m[39;49;00m$
   774^I[37m    [39;49;00m[37m;; Create the new map.[39;49;00m[37m[39;49;00m$
   775^I[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mranges[39;49;00m[37m [39;49;00m[33m'make-keymap[39;49;00m[37m [39;49;00m[33m'make-sparse-keymap[39;49;00m)[37m [39;49;00m[31mprompt[39;49;00m))[37m[39;49;00m$
   776^I[37m    [39;49;00m([36mdolist[39;49;00m[37m [39;49;00m([31mbinding[39;49;00m[37m [39;49;00m[31mranges[39;49;00m)[37m[39;49;00m$
   777^I[37m      [39;49;00m[37m;; Treat char-ranges specially.  FIXME: need to merge as well.[39;49;00m[37m[39;49;00m$
   778^I[37m      [39;49;00m([32mdefine-key[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m([32mvector[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mbinding[39;49;00m))[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mbinding[39;49;00m)))[37m[39;49;00m$
   779^I[37m    [39;49;00m[37m;; Process the bindings starting from the end.[39;49;00m[37m[39;49;00m$
   780^I[37m    [39;49;00m([36mdolist[39;49;00m[37m [39;49;00m([31mbinding[39;49;00m[37m [39;49;00m([34mprog1[39;49;00m[37m [39;49;00m[31mbindings[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbindings[39;49;00m[37m [39;49;00m())))[37m[39;49;00m$
   781^I[37m      [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mkey[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mbinding[39;49;00m))[37m[39;49;00m$
   782^I[37m             [39;49;00m([31moldbind[39;49;00m[37m [39;49;00m([32massq[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m[31mbindings[39;49;00m)))[37m[39;49;00m$
   783^I[37m        [39;49;00m([36mpush[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m[31moldbind[39;49;00m)[37m[39;49;00m$
   784^I[37m                  [39;49;00m[37m;; The normal case: no duplicate bindings.[39;49;00m[37m[39;49;00m$
   785^I[37m                  [39;49;00m[31mbinding[39;49;00m[37m[39;49;00m$
   786^I[37m                [39;49;00m[37m;; This is the second binding for this key.[39;49;00m[37m[39;49;00m$
   787^I[37m                [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbindings[39;49;00m[37m [39;49;00m([32mdelq[39;49;00m[37m [39;49;00m[31moldbind[39;49;00m[37m [39;49;00m[31mbindings[39;49;00m))[37m[39;49;00m$
   788^I[37m                [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m([31mkeymap--merge-bindings[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mbinding[39;49;00m)[37m[39;49;00m$
   789^I[37m                                                  [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31moldbind[39;49;00m))))[37m[39;49;00m$
   790^I[37m              [39;49;00m[31mbindings[39;49;00m)))[37m[39;49;00m$
   791^I[37m    [39;49;00m([32mnconc[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m[31mbindings[39;49;00m)))[37m[39;49;00m$
   792^I[37m[39;49;00m$
   793^I([32mput[39;49;00m[37m [39;49;00m[33m'keyboard-translate-table[39;49;00m[37m [39;49;00m[33m'char-table-extra-slots[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
   794^I[37m[39;49;00m$
   795^I([36mdefun[39;49;00m[37m [39;49;00m[31mkeyboard-translate[39;49;00m[37m [39;49;00m([31mfrom[39;49;00m[37m [39;49;00m[31mto[39;49;00m)[37m[39;49;00m$
   796^I[37m  [39;49;00m[33m"[39;49;00m[33mTranslate character FROM to TO on the current terminal.[39;49;00m$
   797^I[33mThis function creates a [39;49;00m[33m`keyboard-translate-table'[39;49;00m[33m if necessary[39;49;00m$
   798^I[33mand then modifies one entry in it.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   799^I[37m  [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mchar-table-p[39;49;00m[37m [39;49;00m[31mkeyboard-translate-table[39;49;00m)[37m[39;49;00m$
   800^I[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mkeyboard-translate-table[39;49;00m[37m[39;49;00m$
   801^I[37m^I    [39;49;00m([32mmake-char-table[39;49;00m[37m [39;49;00m[33m'keyboard-translate-table[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)))[37m[39;49;00m$
   802^I[37m  [39;49;00m([32maset[39;49;00m[37m [39;49;00m[31mkeyboard-translate-table[39;49;00m[37m [39;49;00m[31mfrom[39;49;00m[37m [39;49;00m[31mto[39;49;00m))[37m[39;49;00m$
   803^I[37m[39;49;00m[37m[39;49;00m$
   804^I[37m;;;; Key binding commands.[39;49;00m[37m[39;49;00m$
   805^I[37m[39;49;00m$
   806^I([36mdefun[39;49;00m[37m [39;49;00m[31mglobal-set-key[39;49;00m[37m [39;49;00m([31mkey[39;49;00m[37m [39;49;00m[31mcommand[39;49;00m)[37m[39;49;00m$
   807^I[37m  [39;49;00m[33m"[39;49;00m[33mGive KEY a global binding as COMMAND.[39;49;00m$
   808^I[33mCOMMAND is the command definition to use; usually it is[39;49;00m$
   809^I[33ma symbol naming an interactively-callable function.[39;49;00m$
   810^I[33mKEY is a key sequence; noninteractively, it is a string or vector[39;49;00m$
   811^I[33mof characters or event types, and non-ASCII characters with codes[39;49;00m$
   812^I[33mabove 127 (such as ISO Latin-1) can be included if you use a vector.[39;49;00m$
   813^I[33m[39;49;00m$
   814^I[33mNote that if KEY has a local binding in the current buffer,[39;49;00m$
   815^I[33mthat local binding will continue to shadow any global binding[39;49;00m$
   816^I[33mthat you make with this function.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   817^I[37m  [39;49;00m([34minteractive[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mKSet key globally: [39;49;00m[33m\n[39;49;00m[33mCSet key %s to command: [39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
   818^I[37m  [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mvectorp[39;49;00m[37m [39;49;00m[31mkey[39;49;00m)[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m[31mkey[39;49;00m)[37m[39;49;00m$
   819^I[37m      [39;49;00m([32msignal[39;49;00m[37m [39;49;00m[33m'wrong-type-argument[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'arrayp[39;49;00m[37m [39;49;00m[31mkey[39;49;00m)))[37m[39;49;00m$
   820^I[37m  [39;49;00m([32mdefine-key[39;49;00m[37m [39;49;00m([32mcurrent-global-map[39;49;00m)[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m[31mcommand[39;49;00m))[37m[39;49;00m$
   821^I[37m[39;49;00m$
   822^I([36mdefun[39;49;00m[37m [39;49;00m[31mlocal-set-key[39;49;00m[37m [39;49;00m([31mkey[39;49;00m[37m [39;49;00m[31mcommand[39;49;00m)[37m[39;49;00m$
   823^I[37m  [39;49;00m[33m"[39;49;00m[33mGive KEY a local binding as COMMAND.[39;49;00m$
   824^I[33mCOMMAND is the command definition to use; usually it is[39;49;00m$
   825^I[33ma symbol naming an interactively-callable function.[39;49;00m$
   826^I[33mKEY is a key sequence; noninteractively, it is a string or vector[39;49;00m$
   827^I[33mof characters or event types, and non-ASCII characters with codes[39;49;00m$
   828^I[33mabove 127 (such as ISO Latin-1) can be included if you use a vector.[39;49;00m$
   829^I[33m[39;49;00m$
   830^I[33mThe binding goes in the current buffer's local map, which in most[39;49;00m$
   831^I[33mcases is shared with all other buffers in the same major mode.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   832^I[37m  [39;49;00m([34minteractive[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mKSet key locally: [39;49;00m[33m\n[39;49;00m[33mCSet key %s locally to command: [39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
   833^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mmap[39;49;00m[37m [39;49;00m([32mcurrent-local-map[39;49;00m)))[37m[39;49;00m$
   834^I[37m    [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m[39;49;00m$
   835^I[37m^I[39;49;00m([32muse-local-map[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m([32mmake-sparse-keymap[39;49;00m))))[37m[39;49;00m$
   836^I[37m    [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mvectorp[39;49;00m[37m [39;49;00m[31mkey[39;49;00m)[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m[31mkey[39;49;00m)[37m[39;49;00m$
   837^I[37m^I[39;49;00m([32msignal[39;49;00m[37m [39;49;00m[33m'wrong-type-argument[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'arrayp[39;49;00m[37m [39;49;00m[31mkey[39;49;00m)))[37m[39;49;00m$
   838^I[37m    [39;49;00m([32mdefine-key[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m[31mcommand[39;49;00m)))[37m[39;49;00m$
   839^I[37m[39;49;00m$
   840^I([36mdefun[39;49;00m[37m [39;49;00m[31mglobal-unset-key[39;49;00m[37m [39;49;00m([31mkey[39;49;00m)[37m[39;49;00m$
   841^I[37m  [39;49;00m[33m"[39;49;00m[33mRemove global binding of KEY.[39;49;00m$
   842^I[33mKEY is a string or vector representing a sequence of keystrokes.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   843^I[37m  [39;49;00m([34minteractive[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mkUnset key globally: [39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
   844^I[37m  [39;49;00m([31mglobal-set-key[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m$
   845^I[37m[39;49;00m$
   846^I([36mdefun[39;49;00m[37m [39;49;00m[31mlocal-unset-key[39;49;00m[37m [39;49;00m([31mkey[39;49;00m)[37m[39;49;00m$
   847^I[37m  [39;49;00m[33m"[39;49;00m[33mRemove local binding of KEY.[39;49;00m$
   848^I[33mKEY is a string or vector representing a sequence of keystrokes.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   849^I[37m  [39;49;00m([34minteractive[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mkUnset key locally: [39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
   850^I[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mcurrent-local-map[39;49;00m)[37m[39;49;00m$
   851^I[37m      [39;49;00m([31mlocal-set-key[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m$
   852^I[37m  [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
   853^I[37m[39;49;00m[37m[39;49;00m$
   854^I[37m;;;; substitute-key-definition and its subroutines.[39;49;00m[37m[39;49;00m$
   855^I[37m[39;49;00m$
   856^I([34mdefvar[39;49;00m[37m [39;49;00m[31mkey-substitution-in-progress[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m$
   857^I[37m  [39;49;00m[33m"[39;49;00m[33mUsed internally by [39;49;00m[33m`substitute-key-definition'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
   858^I[37m[39;49;00m$
   859^I([36mdefun[39;49;00m[37m [39;49;00m[31msubstitute-key-definition[39;49;00m[37m [39;49;00m([31molddef[39;49;00m[37m [39;49;00m[31mnewdef[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31moldmap[39;49;00m[37m [39;49;00m[31mprefix[39;49;00m)[37m[39;49;00m$
   860^I[37m  [39;49;00m[33m"[39;49;00m[33mReplace OLDDEF with NEWDEF for any keys in KEYMAP now defined as OLDDEF.[39;49;00m$
   861^I[33mIn other words, OLDDEF is replaced with NEWDEF where ever it appears.[39;49;00m$
   862^I[33mAlternatively, if optional fourth argument OLDMAP is specified, we redefine[39;49;00m$
   863^I[33min KEYMAP as NEWDEF those keys which are defined as OLDDEF in OLDMAP.[39;49;00m$
   864^I[33m[39;49;00m$
   865^I[33mIf you don't specify OLDMAP, you can usually get the same results[39;49;00m$
   866^I[33min a cleaner way with command remapping, like this:[39;49;00m$
   867^I[33m  (define-key KEYMAP [remap OLDDEF] NEWDEF)[39;49;00m$
   868^I[33m\n[39;49;00m[33m(fn OLDDEF NEWDEF KEYMAP &optional OLDMAP)[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   869^I[37m  [39;49;00m[37m;; Don't document PREFIX in the doc string because we don't want to[39;49;00m[37m[39;49;00m$
   870^I[37m  [39;49;00m[37m;; advertise it.  It's meant for recursive calls only.  Here's its[39;49;00m[37m[39;49;00m$
   871^I[37m  [39;49;00m[37m;; meaning[39;49;00m[37m[39;49;00m$
   872^I[37m[39;49;00m$
   873^I[37m  [39;49;00m[37m;; If optional argument PREFIX is specified, it should be a key[39;49;00m[37m[39;49;00m$
   874^I[37m  [39;49;00m[37m;; prefix, a string.  Redefined bindings will then be bound to the[39;49;00m[37m[39;49;00m$
   875^I[37m  [39;49;00m[37m;; original key, with PREFIX added at the front.[39;49;00m[37m[39;49;00m$
   876^I[37m  [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mprefix[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mprefix[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
   877^I[37m  [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mscan[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31moldmap[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m))[37m[39;49;00m$
   878^I[37m^I [39;49;00m([31mprefix1[39;49;00m[37m [39;49;00m([32mvconcat[39;49;00m[37m [39;49;00m[31mprefix[39;49;00m[37m [39;49;00m[[31mnil[39;49;00m]))[37m[39;49;00m$
   879^I[37m^I [39;49;00m([31mkey-substitution-in-progress[39;49;00m[37m[39;49;00m$
   880^I[37m^I  [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mscan[39;49;00m[37m [39;49;00m[31mkey-substitution-in-progress[39;49;00m)))[37m[39;49;00m$
   881^I[37m    [39;49;00m[37m;; Scan OLDMAP, finding each char or event-symbol that[39;49;00m[37m[39;49;00m$
   882^I[37m    [39;49;00m[37m;; has any definition, and act on it with hack-key.[39;49;00m[37m[39;49;00m$
   883^I[37m    [39;49;00m([32mmap-keymap[39;49;00m[37m[39;49;00m$
   884^I[37m     [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31mchar[39;49;00m[37m [39;49;00m[31mdefn[39;49;00m)[37m[39;49;00m$
   885^I[37m       [39;49;00m([32maset[39;49;00m[37m [39;49;00m[31mprefix1[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31mprefix[39;49;00m)[37m [39;49;00m[31mchar[39;49;00m)[37m[39;49;00m$
   886^I[37m       [39;49;00m([31msubstitute-key-definition-key[39;49;00m[37m [39;49;00m[31mdefn[39;49;00m[37m [39;49;00m[31molddef[39;49;00m[37m [39;49;00m[31mnewdef[39;49;00m[37m [39;49;00m[31mprefix1[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m))[37m[39;49;00m$
   887^I[37m     [39;49;00m[31mscan[39;49;00m)))[37m[39;49;00m$
   888^I[37m[39;49;00m$
   889^I([36mdefun[39;49;00m[37m [39;49;00m[31msubstitute-key-definition-key[39;49;00m[37m [39;49;00m([31mdefn[39;49;00m[37m [39;49;00m[31molddef[39;49;00m[37m [39;49;00m[31mnewdef[39;49;00m[37m [39;49;00m[31mprefix[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m)[37m[39;49;00m$
   890^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m([31minner-def[39;49;00m[37m [39;49;00m[31mskipped[39;49;00m[37m [39;49;00m[31mmenu-item[39;49;00m)[37m[39;49;00m$
   891^I[37m    [39;49;00m[37m;; Find the actual command name within the binding.[39;49;00m[37m[39;49;00m$
   892^I[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mcar-safe[39;49;00m[37m [39;49;00m[31mdefn[39;49;00m)[37m [39;49;00m[33m'menu-item[39;49;00m)[37m[39;49;00m$
   893^I[37m^I[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mmenu-item[39;49;00m[37m [39;49;00m[31mdefn[39;49;00m[37m [39;49;00m[31mdefn[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m[31mdefn[39;49;00m))[37m[39;49;00m$
   894^I[37m      [39;49;00m[37m;; Skip past menu-prompt.[39;49;00m[37m[39;49;00m$
   895^I[37m      [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m([32mcar-safe[39;49;00m[37m [39;49;00m[31mdefn[39;49;00m))[37m[39;49;00m$
   896^I[37m^I[39;49;00m([36mpush[39;49;00m[37m [39;49;00m([36mpop[39;49;00m[37m [39;49;00m[31mdefn[39;49;00m)[37m [39;49;00m[31mskipped[39;49;00m))[37m[39;49;00m$
   897^I[37m      [39;49;00m[37m;; Skip past cached key-equivalence data for menu items.[39;49;00m[37m[39;49;00m$
   898^I[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m([32mcar-safe[39;49;00m[37m [39;49;00m[31mdefn[39;49;00m))[37m[39;49;00m$
   899^I[37m^I  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mdefn[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mdefn[39;49;00m))))[37m[39;49;00m$
   900^I[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mdefn[39;49;00m[37m [39;49;00m[31molddef[39;49;00m)[37m[39;49;00m$
   901^I[37m^I    [39;49;00m[37m;; Compare with equal if definition is a key sequence.[39;49;00m[37m[39;49;00m$
   902^I[37m^I    [39;49;00m[37m;; That is useful for operating on function-key-map.[39;49;00m[37m[39;49;00m$
   903^I[37m^I    [39;49;00m([34mand[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m[31mdefn[39;49;00m)[37m [39;49;00m([32mvectorp[39;49;00m[37m [39;49;00m[31mdefn[39;49;00m))[37m[39;49;00m$
   904^I[37m^I^I [39;49;00m([32mequal[39;49;00m[37m [39;49;00m[31mdefn[39;49;00m[37m [39;49;00m[31molddef[39;49;00m)))[37m[39;49;00m$
   905^I[37m^I[39;49;00m([32mdefine-key[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m[37m [39;49;00m[31mprefix[39;49;00m[37m[39;49;00m$
   906^I[37m^I  [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mmenu-item[39;49;00m[37m[39;49;00m$
   907^I[37m^I      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mcopy[39;49;00m[37m [39;49;00m([32mcopy-sequence[39;49;00m[37m [39;49;00m[31mmenu-item[39;49;00m)))[37m[39;49;00m$
   908^I[37m^I^I[39;49;00m([32msetcar[39;49;00m[37m [39;49;00m([32mnthcdr[39;49;00m[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m[31mcopy[39;49;00m)[37m [39;49;00m[31mnewdef[39;49;00m)[37m[39;49;00m$
   909^I[37m^I^I[39;49;00m[31mcopy[39;49;00m)[37m[39;49;00m$
   910^I[37m^I    [39;49;00m([32mnconc[39;49;00m[37m [39;49;00m([32mnreverse[39;49;00m[37m [39;49;00m[31mskipped[39;49;00m)[37m [39;49;00m[31mnewdef[39;49;00m)))[37m[39;49;00m$
   911^I[37m      [39;49;00m[37m;; Look past a symbol that names a keymap.[39;49;00m[37m[39;49;00m$
   912^I[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31minner-def[39;49;00m[37m[39;49;00m$
   913^I[37m^I    [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mindirect-function[39;49;00m[37m [39;49;00m[31mdefn[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m [39;49;00m[31mdefn[39;49;00m))[37m[39;49;00m$
   914^I[37m      [39;49;00m[37m;; For nested keymaps, we use `inner-def' rather than `defn' so as to[39;49;00m[37m[39;49;00m$
   915^I[37m      [39;49;00m[37m;; avoid autoloading a keymap.  This is mostly done to preserve the[39;49;00m[37m[39;49;00m$
   916^I[37m      [39;49;00m[37m;; original non-autoloading behavior of pre-map-keymap times.[39;49;00m[37m[39;49;00m$
   917^I[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mkeymapp[39;49;00m[37m [39;49;00m[31minner-def[39;49;00m)[37m[39;49;00m$
   918^I[37m^I       [39;49;00m[37m;; Avoid recursively scanning[39;49;00m[37m[39;49;00m$
   919^I[37m^I       [39;49;00m[37m;; where KEYMAP does not have a submap.[39;49;00m[37m[39;49;00m$
   920^I[37m^I       [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([32melt[39;49;00m[37m [39;49;00m([32mlookup-key[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m[37m [39;49;00m[31mprefix[39;49;00m)))[37m[39;49;00m$
   921^I[37m^I^I [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[32melt[39;49;00m)[37m [39;49;00m([32mnatnump[39;49;00m[37m [39;49;00m[32melt[39;49;00m)[37m [39;49;00m([32mkeymapp[39;49;00m[37m [39;49;00m[32melt[39;49;00m)))[37m[39;49;00m$
   922^I[37m^I       [39;49;00m[37m;; Avoid recursively rescanning keymap being scanned.[39;49;00m[37m[39;49;00m$
   923^I[37m^I       [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[31minner-def[39;49;00m[37m [39;49;00m[31mkey-substitution-in-progress[39;49;00m)))[37m[39;49;00m$
   924^I[37m^I  [39;49;00m[37m;; If this one isn't being scanned already, scan it now.[39;49;00m[37m[39;49;00m$
   925^I[37m^I  [39;49;00m([31msubstitute-key-definition[39;49;00m[37m [39;49;00m[31molddef[39;49;00m[37m [39;49;00m[31mnewdef[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m[37m [39;49;00m[31minner-def[39;49;00m[37m [39;49;00m[31mprefix[39;49;00m)))))[37m[39;49;00m$
   926^I[37m[39;49;00m$
   927^I[37m[39;49;00m[37m[39;49;00m$
   928^I[37m;;;; The global keymap tree.[39;49;00m[37m[39;49;00m$
   929^I[37m[39;49;00m$
   930^I[37m;; global-map, esc-map, and ctl-x-map have their values set up in[39;49;00m[37m[39;49;00m$
   931^I[37m;; keymap.c; we just give them docstrings here.[39;49;00m[37m[39;49;00m$
   932^I[37m[39;49;00m$
   933^I([34mdefvar[39;49;00m[37m [39;49;00m[31mglobal-map[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m$
   934^I[37m  [39;49;00m[33m"[39;49;00m[33mDefault global keymap mapping Emacs keyboard input into commands.[39;49;00m$
   935^I[33mThe value is a keymap which is usually (but not necessarily) Emacs's[39;49;00m$
   936^I[33mglobal map.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
   937^I[37m[39;49;00m$
   938^I([34mdefvar[39;49;00m[37m [39;49;00m[31mesc-map[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m$
   939^I[37m  [39;49;00m[33m"[39;49;00m[33mDefault keymap for ESC (meta) commands.[39;49;00m$
   940^I[33mThe normal global definition of the character ESC indirects to this keymap.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
   941^I[37m[39;49;00m$
   942^I([34mdefvar[39;49;00m[37m [39;49;00m[31mctl-x-map[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m$
   943^I[37m  [39;49;00m[33m"[39;49;00m[33mDefault keymap for C-x commands.[39;49;00m$
   944^I[33mThe normal global definition of the character C-x indirects to this keymap.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
   945^I[37m[39;49;00m$
   946^I([34mdefvar[39;49;00m[37m [39;49;00m[31mctl-x-4-map[39;49;00m[37m [39;49;00m([32mmake-sparse-keymap[39;49;00m)[37m[39;49;00m$
   947^I[37m  [39;49;00m[33m"[39;49;00m[33mKeymap for subcommands of C-x 4.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
   948^I([36mdefalias[39;49;00m[37m [39;49;00m[33m'ctl-x-4-prefix[39;49;00m[37m [39;49;00m[31mctl-x-4-map[39;49;00m)[37m[39;49;00m$
   949^I([32mdefine-key[39;49;00m[37m [39;49;00m[31mctl-x-map[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m4[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m'ctl-x-4-prefix[39;49;00m)[37m[39;49;00m$
   950^I[37m[39;49;00m$
   951^I([34mdefvar[39;49;00m[37m [39;49;00m[31mctl-x-5-map[39;49;00m[37m [39;49;00m([32mmake-sparse-keymap[39;49;00m)[37m[39;49;00m$
   952^I[37m  [39;49;00m[33m"[39;49;00m[33mKeymap for frame commands.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
   953^I([36mdefalias[39;49;00m[37m [39;49;00m[33m'ctl-x-5-prefix[39;49;00m[37m [39;49;00m[31mctl-x-5-map[39;49;00m)[37m[39;49;00m$
   954^I([32mdefine-key[39;49;00m[37m [39;49;00m[31mctl-x-map[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m5[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m'ctl-x-5-prefix[39;49;00m)[37m[39;49;00m$
   955^I[37m[39;49;00m$
   956^I[37m[39;49;00m[37m[39;49;00m$
   957^I[37m;;;; Event manipulation functions.[39;49;00m[37m[39;49;00m$
   958^I[37m[39;49;00m$
   959^I([34mdefconst[39;49;00m[37m [39;49;00m[31mlistify-key-sequence-1[39;49;00m[37m [39;49;00m([32mlogior[39;49;00m[37m [39;49;00m[34m128[39;49;00m[37m [39;49;00m[33m?\M[39;49;00m[31m-\C-@[39;49;00m))[37m[39;49;00m$
   960^I[37m[39;49;00m$
   961^I([36mdefun[39;49;00m[37m [39;49;00m[31mlistify-key-sequence[39;49;00m[37m [39;49;00m([31mkey[39;49;00m)[37m[39;49;00m$
   962^I[37m  [39;49;00m[33m"[39;49;00m[33mConvert a key sequence to a list of events.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   963^I[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mvectorp[39;49;00m[37m [39;49;00m[31mkey[39;49;00m)[37m[39;49;00m$
   964^I[37m      [39;49;00m([32mappend[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
   965^I[37m    [39;49;00m([32mmapcar[39;49;00m[37m [39;49;00m([34mfunction[39;49;00m[37m [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31mc[39;49;00m)[37m[39;49;00m$
   966^I[37m^I^I^I[39;49;00m([34mif[39;49;00m[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m[31mc[39;49;00m[37m [39;49;00m[34m127[39;49;00m)[37m[39;49;00m$
   967^I[37m^I^I^I    [39;49;00m([32mlogxor[39;49;00m[37m [39;49;00m[31mc[39;49;00m[37m [39;49;00m[31mlistify-key-sequence-1[39;49;00m)[37m[39;49;00m$
   968^I[37m^I^I^I  [39;49;00m[31mc[39;49;00m)))[37m[39;49;00m$
   969^I[37m^I    [39;49;00m[31mkey[39;49;00m)))[37m[39;49;00m$
   970^I[37m[39;49;00m$
   971^I([36mdefun[39;49;00m[37m [39;49;00m[31meventp[39;49;00m[37m [39;49;00m([31mobj[39;49;00m)[37m[39;49;00m$
   972^I[37m  [39;49;00m[33m"[39;49;00m[33mTrue if the argument is an event object.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   973^I[37m  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31mobj[39;49;00m[37m[39;49;00m$
   974^I[37m    [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mintegerp[39;49;00m[37m [39;49;00m[31mobj[39;49;00m)[37m[39;49;00m$
   975^I[37m        [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32msymbolp[39;49;00m[37m [39;49;00m[31mobj[39;49;00m)[37m [39;49;00m[31mobj[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mkeywordp[39;49;00m[37m [39;49;00m[31mobj[39;49;00m)))[37m[39;49;00m$
   976^I[37m        [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mobj[39;49;00m)[37m [39;49;00m([32msymbolp[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mobj[39;49;00m))))))[37m[39;49;00m$
   977^I[37m[39;49;00m$
   978^I([36mdefun[39;49;00m[37m [39;49;00m[31mevent-modifiers[39;49;00m[37m [39;49;00m([31mevent[39;49;00m)[37m[39;49;00m$
   979^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn a list of symbols representing the modifier keys in event EVENT.[39;49;00m$
   980^I[33mThe elements of the list may include [39;49;00m[33m`meta'[39;49;00m[33m, [39;49;00m[33m`control'[39;49;00m[33m,[39;49;00m$
   981^I[33m`shift'[39;49;00m[33m, [39;49;00m[33m`hyper'[39;49;00m[33m, [39;49;00m[33m`super'[39;49;00m[33m, [39;49;00m[33m`alt'[39;49;00m[33m, [39;49;00m[33m`click'[39;49;00m[33m, [39;49;00m[33m`double'[39;49;00m[33m, [39;49;00m[33m`triple'[39;49;00m[33m, [39;49;00m[33m`drag'[39;49;00m[33m,[39;49;00m$
   982^I[33mand [39;49;00m[33m`down'[39;49;00m[33m.[39;49;00m$
   983^I[33mEVENT may be an event or an event type.  If EVENT is a symbol[39;49;00m$
   984^I[33mthat has never been used in an event that has been read as input[39;49;00m$
   985^I[33min the current Emacs session, then this function may fail to include[39;49;00m$
   986^I[33mthe [39;49;00m[33m`click'[39;49;00m[33m modifier.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   987^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtype[39;49;00m[37m [39;49;00m[31mevent[39;49;00m))[37m[39;49;00m$
   988^I[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mlistp[39;49;00m[37m [39;49;00m[31mtype[39;49;00m)[37m[39;49;00m$
   989^I[37m^I[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mtype[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mtype[39;49;00m)))[37m[39;49;00m$
   990^I[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32msymbolp[39;49;00m[37m [39;49;00m[31mtype[39;49;00m)[37m[39;49;00m$
   991^I[37m        [39;49;00m[37m;; Don't read event-symbol-elements directly since we're not[39;49;00m[37m[39;49;00m$
   992^I[37m        [39;49;00m[37m;; sure the symbol has already been parsed.[39;49;00m[37m[39;49;00m$
   993^I[37m^I[39;49;00m([32mcdr[39;49;00m[37m [39;49;00m([32minternal-event-symbol-parse-modifiers[39;49;00m[37m [39;49;00m[31mtype[39;49;00m))[37m[39;49;00m$
   994^I[37m      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([32mlist[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
   995^I[37m^I    [39;49;00m([31mchar[39;49;00m[37m [39;49;00m([32mlogand[39;49;00m[37m [39;49;00m[31mtype[39;49;00m[37m [39;49;00m([32mlognot[39;49;00m[37m [39;49;00m([32mlogior[39;49;00m[37m [39;49;00m[33m?\M[39;49;00m[31m-\^@[39;49;00m[37m [39;49;00m[33m?\C[39;49;00m[31m-\^@[39;49;00m[37m [39;49;00m[33m?\S[39;49;00m[31m-\^@[39;49;00m[37m[39;49;00m$
   996^I[37m^I^I^I^I^I       [39;49;00m[33m?\H[39;49;00m[31m-\^@[39;49;00m[37m [39;49;00m[33m?\s[39;49;00m[31m-\^@[39;49;00m[37m [39;49;00m[33m?\A[39;49;00m[31m-\^@[39;49;00m)))))[37m[39;49;00m$
   997^I[37m^I[39;49;00m([34mif[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([31mzerop[39;49;00m[37m [39;49;00m([32mlogand[39;49;00m[37m [39;49;00m[31mtype[39;49;00m[37m [39;49;00m[33m?\M[39;49;00m[31m-\^@[39;49;00m)))[37m[39;49;00m$
   998^I[37m^I    [39;49;00m([36mpush[39;49;00m[37m [39;49;00m[33m'meta[39;49;00m[37m [39;49;00m[32mlist[39;49;00m))[37m[39;49;00m$
   999^I[37m^I[39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([31mzerop[39;49;00m[37m [39;49;00m([32mlogand[39;49;00m[37m [39;49;00m[31mtype[39;49;00m[37m [39;49;00m[33m?\C[39;49;00m[31m-\^@[39;49;00m)))[37m[39;49;00m$
  1000^I[37m^I^I[39;49;00m([32m<[39;49;00m[37m [39;49;00m[31mchar[39;49;00m[37m [39;49;00m[34m32[39;49;00m))[37m[39;49;00m$
  1001^I[37m^I    [39;49;00m([36mpush[39;49;00m[37m [39;49;00m[33m'control[39;49;00m[37m [39;49;00m[32mlist[39;49;00m))[37m[39;49;00m$
  1002^I[37m^I[39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([31mzerop[39;49;00m[37m [39;49;00m([32mlogand[39;49;00m[37m [39;49;00m[31mtype[39;49;00m[37m [39;49;00m[33m?\S[39;49;00m[31m-\^@[39;49;00m)))[37m[39;49;00m$
  1003^I[37m^I^I[39;49;00m([32m/=[39;49;00m[37m [39;49;00m[31mchar[39;49;00m[37m [39;49;00m([32mdowncase[39;49;00m[37m [39;49;00m[31mchar[39;49;00m)))[37m[39;49;00m$
  1004^I[37m^I    [39;49;00m([36mpush[39;49;00m[37m [39;49;00m[33m'shift[39;49;00m[37m [39;49;00m[32mlist[39;49;00m))[37m[39;49;00m$
  1005^I[37m^I[39;49;00m([34mor[39;49;00m[37m [39;49;00m([31mzerop[39;49;00m[37m [39;49;00m([32mlogand[39;49;00m[37m [39;49;00m[31mtype[39;49;00m[37m [39;49;00m[33m?\H[39;49;00m[31m-\^@[39;49;00m))[37m[39;49;00m$
  1006^I[37m^I    [39;49;00m([36mpush[39;49;00m[37m [39;49;00m[33m'hyper[39;49;00m[37m [39;49;00m[32mlist[39;49;00m))[37m[39;49;00m$
  1007^I[37m^I[39;49;00m([34mor[39;49;00m[37m [39;49;00m([31mzerop[39;49;00m[37m [39;49;00m([32mlogand[39;49;00m[37m [39;49;00m[31mtype[39;49;00m[37m [39;49;00m[33m?\s[39;49;00m[31m-\^@[39;49;00m))[37m[39;49;00m$
  1008^I[37m^I    [39;49;00m([36mpush[39;49;00m[37m [39;49;00m[33m'super[39;49;00m[37m [39;49;00m[32mlist[39;49;00m))[37m[39;49;00m$
  1009^I[37m^I[39;49;00m([34mor[39;49;00m[37m [39;49;00m([31mzerop[39;49;00m[37m [39;49;00m([32mlogand[39;49;00m[37m [39;49;00m[31mtype[39;49;00m[37m [39;49;00m[33m?\A[39;49;00m[31m-\^@[39;49;00m))[37m[39;49;00m$
  1010^I[37m^I    [39;49;00m([36mpush[39;49;00m[37m [39;49;00m[33m'alt[39;49;00m[37m [39;49;00m[32mlist[39;49;00m))[37m[39;49;00m$
  1011^I[37m^I[39;49;00m[32mlist[39;49;00m))))[37m[39;49;00m$
  1012^I[37m[39;49;00m$
  1013^I([36mdefun[39;49;00m[37m [39;49;00m[31mevent-basic-type[39;49;00m[37m [39;49;00m([31mevent[39;49;00m)[37m[39;49;00m$
  1014^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn the basic type of the given event (all modifiers removed).[39;49;00m$
  1015^I[33mThe value is a printing character (not upper case) or a symbol.[39;49;00m$
  1016^I[33mEVENT may be an event or an event type.  If EVENT is a symbol[39;49;00m$
  1017^I[33mthat has never been used in an event that has been read as input[39;49;00m$
  1018^I[33min the current Emacs session, then this function may return nil.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1019^I[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mevent[39;49;00m)[37m[39;49;00m$
  1020^I[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mevent[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mevent[39;49;00m)))[37m[39;49;00m$
  1021^I[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32msymbolp[39;49;00m[37m [39;49;00m[31mevent[39;49;00m)[37m[39;49;00m$
  1022^I[37m      [39;49;00m([32mcar[39;49;00m[37m [39;49;00m([32mget[39;49;00m[37m [39;49;00m[31mevent[39;49;00m[37m [39;49;00m[33m'event-symbol-elements[39;49;00m))[37m[39;49;00m$
  1023^I[37m    [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mbase[39;49;00m[37m [39;49;00m([32mlogand[39;49;00m[37m [39;49;00m[31mevent[39;49;00m[37m [39;49;00m([32m1-[39;49;00m[37m [39;49;00m[33m?\A[39;49;00m[31m-\^@[39;49;00m)))[37m[39;49;00m$
  1024^I[37m^I   [39;49;00m([31muncontrolled[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m[31mbase[39;49;00m[37m [39;49;00m[34m32[39;49;00m)[37m [39;49;00m([32mlogior[39;49;00m[37m [39;49;00m[31mbase[39;49;00m[37m [39;49;00m[34m64[39;49;00m)[37m [39;49;00m[31mbase[39;49;00m)))[37m[39;49;00m$
  1025^I[37m      [39;49;00m[37m;; There are some numbers that are invalid characters and[39;49;00m[37m[39;49;00m$
  1026^I[37m      [39;49;00m[37m;; cause `downcase' to get an error.[39;49;00m[37m[39;49;00m$
  1027^I[37m      [39;49;00m([34mcondition-case[39;49;00m[37m [39;49;00m()[37m[39;49;00m$
  1028^I[37m^I  [39;49;00m([32mdowncase[39;49;00m[37m [39;49;00m[31muncontrolled[39;49;00m)[37m[39;49;00m$
  1029^I[37m^I[39;49;00m([36merror[39;49;00m[37m [39;49;00m[31muncontrolled[39;49;00m)))))[37m[39;49;00m$
  1030^I[37m[39;49;00m$
  1031^I([36mdefsubst[39;49;00m[37m [39;49;00m[31mmouse-movement-p[39;49;00m[37m [39;49;00m([31mobject[39;49;00m)[37m[39;49;00m$
  1032^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn non-nil if OBJECT is a mouse movement event.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1033^I[37m  [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mcar-safe[39;49;00m[37m [39;49;00m[31mobject[39;49;00m)[37m [39;49;00m[33m'mouse-movement[39;49;00m))[37m[39;49;00m$
  1034^I[37m[39;49;00m$
  1035^I([36mdefun[39;49;00m[37m [39;49;00m[31mmouse-event-p[39;49;00m[37m [39;49;00m([31mobject[39;49;00m)[37m[39;49;00m$
  1036^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn non-nil if OBJECT is a mouse click event.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1037^I[37m  [39;49;00m[37m;; is this really correct? maybe remove mouse-movement?[39;49;00m[37m[39;49;00m$
  1038^I[37m  [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m([31mevent-basic-type[39;49;00m[37m [39;49;00m[31mobject[39;49;00m)[37m [39;49;00m'([31mmouse-1[39;49;00m[37m [39;49;00m[31mmouse-2[39;49;00m[37m [39;49;00m[31mmouse-3[39;49;00m[37m [39;49;00m[31mmouse-movement[39;49;00m)))[37m[39;49;00m$
  1039^I[37m[39;49;00m$
  1040^I([36mdefun[39;49;00m[37m [39;49;00m[31mevent-start[39;49;00m[37m [39;49;00m([31mevent[39;49;00m)[37m[39;49;00m$
  1041^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn the starting position of EVENT.[39;49;00m$
  1042^I[33mEVENT should be a mouse click, drag, or key press event.  If[39;49;00m$
  1043^I[33mEVENT is nil, the value of [39;49;00m[33m`posn-at-point'[39;49;00m[33m is used instead.[39;49;00m$
  1044^I[33m[39;49;00m$
  1045^I[33mThe following accessor functions are used to access the elements[39;49;00m$
  1046^I[33mof the position:[39;49;00m$
  1047^I[33m[39;49;00m$
  1048^I[33m`posn-window'[39;49;00m[33m: The window the event is in.[39;49;00m$
  1049^I[33m`posn-area'[39;49;00m[33m: A symbol identifying the area the event occurred in,[39;49;00m$
  1050^I[33mor nil if the event occurred in the text area.[39;49;00m$
  1051^I[33m`posn-point'[39;49;00m[33m: The buffer position of the event.[39;49;00m$
  1052^I[33m`posn-x-y'[39;49;00m[33m: The pixel-based coordinates of the event.[39;49;00m$
  1053^I[33m`posn-col-row'[39;49;00m[33m: The estimated column and row corresponding to the[39;49;00m$
  1054^I[33mposition of the event.[39;49;00m$
  1055^I[33m`posn-actual-col-row'[39;49;00m[33m: The actual column and row corresponding to the[39;49;00m$
  1056^I[33mposition of the event.[39;49;00m$
  1057^I[33m`posn-string'[39;49;00m[33m: The string object of the event, which is either[39;49;00m$
  1058^I[33mnil or (STRING . POSITION)'.[39;49;00m$
  1059^I[33m`posn-image'[39;49;00m[33m: The image object of the event, if any.[39;49;00m$
  1060^I[33m`posn-object'[39;49;00m[33m: The image or string object of the event, if any.[39;49;00m$
  1061^I[33m`posn-timestamp'[39;49;00m[33m: The time the event occurred, in milliseconds.[39;49;00m$
  1062^I[33m[39;49;00m$
  1063^I[33mFor more information, see Info node [39;49;00m[33m`[39;49;00m[33m(elisp)Click Events'.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1064^I[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mevent[39;49;00m)[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mevent[39;49;00m)[37m[39;49;00m$
  1065^I[37m    [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mposn-at-point[39;49;00m)[37m[39;49;00m$
  1066^I[37m        [39;49;00m([32mlist[39;49;00m[37m [39;49;00m([32mselected-window[39;49;00m)[37m [39;49;00m([32mpoint[39;49;00m)[37m [39;49;00m'([34m0[39;49;00m[37m [39;49;00m.[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34m0[39;49;00m))))[37m[39;49;00m$
  1067^I[37m[39;49;00m$
  1068^I([36mdefun[39;49;00m[37m [39;49;00m[31mevent-end[39;49;00m[37m [39;49;00m([31mevent[39;49;00m)[37m[39;49;00m$
  1069^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn the ending position of EVENT.[39;49;00m$
  1070^I[33mEVENT should be a click, drag, or key press event.[39;49;00m$
  1071^I[33m[39;49;00m$
  1072^I[33mSee [39;49;00m[33m`event-start'[39;49;00m[33m for a description of the value returned.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1073^I[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mevent[39;49;00m)[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m[31mevent[39;49;00m))[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m[31mevent[39;49;00m)[37m[39;49;00m$
  1074^I[37m    [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mposn-at-point[39;49;00m)[37m[39;49;00m$
  1075^I[37m        [39;49;00m([32mlist[39;49;00m[37m [39;49;00m([32mselected-window[39;49;00m)[37m [39;49;00m([32mpoint[39;49;00m)[37m [39;49;00m'([34m0[39;49;00m[37m [39;49;00m.[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34m0[39;49;00m))))[37m[39;49;00m$
  1076^I[37m[39;49;00m$
  1077^I([36mdefsubst[39;49;00m[37m [39;49;00m[31mevent-click-count[39;49;00m[37m [39;49;00m([31mevent[39;49;00m)[37m[39;49;00m$
  1078^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn the multi-click count of EVENT, a click or drag event.[39;49;00m$
  1079^I[33mThe return value is a positive integer.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1080^I[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mevent[39;49;00m)[37m [39;49;00m([32mintegerp[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m[31mevent[39;49;00m)))[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m[31mevent[39;49;00m)[37m [39;49;00m[34m1[39;49;00m))[37m[39;49;00m$
  1081^I[37m[39;49;00m[37m[39;49;00m$
  1082^I[37m;;;; Extracting fields of the positions in an event.[39;49;00m[37m[39;49;00m$
  1083^I[37m[39;49;00m$
  1084^I([36mdefun[39;49;00m[37m [39;49;00m[31mposnp[39;49;00m[37m [39;49;00m([31mobj[39;49;00m)[37m[39;49;00m$
  1085^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn non-nil if OBJ appears to be a valid [39;49;00m[33m`posn'[39;49;00m[33m object specifying a window.[39;49;00m$
  1086^I[33mIf OBJ is a valid [39;49;00m[33m`posn'[39;49;00m[33m object, but specifies a frame rather[39;49;00m$
  1087^I[33mthan a window, return nil.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1088^I[37m  [39;49;00m[37m;; FIXME: Correct the behavior of this function so that all valid[39;49;00m[37m[39;49;00m$
  1089^I[37m  [39;49;00m[37m;; `posn' objects are recognized, after updating other code that[39;49;00m[37m[39;49;00m$
  1090^I[37m  [39;49;00m[37m;; depends on its present behavior.[39;49;00m[37m[39;49;00m$
  1091^I[37m  [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mwindowp[39;49;00m[37m [39;49;00m([32mcar-safe[39;49;00m[37m [39;49;00m[31mobj[39;49;00m))[37m[39;49;00m$
  1092^I[37m       [39;49;00m([32matom[39;49;00m[37m [39;49;00m([32mcar-safe[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mobj[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mobj[39;49;00m))))[37m                [39;49;00m[37m;AREA-OR-POS.[39;49;00m[37m[39;49;00m$
  1093^I[37m       [39;49;00m([32mintegerp[39;49;00m[37m [39;49;00m([32mcar-safe[39;49;00m[37m [39;49;00m([32mcar-safe[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mobj[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mobj[39;49;00m)))))[37m [39;49;00m[37m;XOFFSET.[39;49;00m[37m[39;49;00m$
  1094^I[37m       [39;49;00m([32mintegerp[39;49;00m[37m [39;49;00m([32mcar-safe[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mobj[39;49;00m)))))[37m                     [39;49;00m[37m;TIMESTAMP.[39;49;00m[37m[39;49;00m$
  1095^I[37m[39;49;00m$
  1096^I([36mdefsubst[39;49;00m[37m [39;49;00m[31mposn-window[39;49;00m[37m [39;49;00m([31mposition[39;49;00m)[37m[39;49;00m$
  1097^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn the window in POSITION.[39;49;00m$
  1098^I[33mPOSITION should be a list of the form returned by the [39;49;00m[33m`event-start'[39;49;00m[33m[39;49;00m$
  1099^I[33mand [39;49;00m[33m`event-end'[39;49;00m[33m functions.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1100^I[37m  [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[31mposition[39;49;00m))[37m[39;49;00m$
  1101^I[37m[39;49;00m$
  1102^I([36mdefsubst[39;49;00m[37m [39;49;00m[31mposn-area[39;49;00m[37m [39;49;00m([31mposition[39;49;00m)[37m[39;49;00m$
  1103^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn the window area recorded in POSITION, or nil for the text area.[39;49;00m$
  1104^I[33mPOSITION should be a list of the form returned by the [39;49;00m[33m`event-start'[39;49;00m[33m[39;49;00m$
  1105^I[33mand [39;49;00m[33m`event-end'[39;49;00m[33m functions.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1106^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31marea[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mposition[39;49;00m))[37m[39;49;00m$
  1107^I[37m^I^I  [39;49;00m([32mcar[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mposition[39;49;00m))[37m[39;49;00m$
  1108^I[37m^I^I[39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mposition[39;49;00m))))[37m[39;49;00m$
  1109^I[37m    [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32msymbolp[39;49;00m[37m [39;49;00m[31marea[39;49;00m)[37m [39;49;00m[31marea[39;49;00m)))[37m[39;49;00m$
  1110^I[37m[39;49;00m$
  1111^I([36mdefun[39;49;00m[37m [39;49;00m[31mposn-point[39;49;00m[37m [39;49;00m([31mposition[39;49;00m)[37m[39;49;00m$
  1112^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn the buffer location in POSITION.[39;49;00m$
  1113^I[33mPOSITION should be a list of the form returned by the [39;49;00m[33m`event-start'[39;49;00m[33m[39;49;00m$
  1114^I[33mand [39;49;00m[33m`event-end'[39;49;00m[33m functions.[39;49;00m$
  1115^I[33mReturns nil if POSITION does not correspond to any buffer location (e.g.[39;49;00m$
  1116^I[33ma click on a scroll bar).[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1117^I[37m  [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m5[39;49;00m[37m [39;49;00m[31mposition[39;49;00m)[37m[39;49;00m$
  1118^I[37m      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mpt[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mposition[39;49;00m)))[37m[39;49;00m$
  1119^I[37m        [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mcar-safe[39;49;00m[37m [39;49;00m[31mpt[39;49;00m)[37m[39;49;00m$
  1120^I[37m            [39;49;00m[37m;; Apparently this can also be `vertical-scroll-bar' (bug#13979).[39;49;00m[37m[39;49;00m$
  1121^I[37m            [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mintegerp[39;49;00m[37m [39;49;00m[31mpt[39;49;00m)[37m [39;49;00m[31mpt[39;49;00m)))))[37m[39;49;00m$
  1122^I[37m[39;49;00m$
  1123^I([36mdefun[39;49;00m[37m [39;49;00m[31mposn-set-point[39;49;00m[37m [39;49;00m([31mposition[39;49;00m)[37m[39;49;00m$
  1124^I[37m  [39;49;00m[33m"[39;49;00m[33mMove point to POSITION.[39;49;00m$
  1125^I[33mSelect the corresponding window as well.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1126^I[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mwindowp[39;49;00m[37m [39;49;00m([31mposn-window[39;49;00m[37m [39;49;00m[31mposition[39;49;00m)))[37m[39;49;00m$
  1127^I[37m      [39;49;00m([36merror[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mPosition not in text area of window[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
  1128^I[37m  [39;49;00m([32mselect-window[39;49;00m[37m [39;49;00m([31mposn-window[39;49;00m[37m [39;49;00m[31mposition[39;49;00m))[37m[39;49;00m$
  1129^I[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mnumberp[39;49;00m[37m [39;49;00m([31mposn-point[39;49;00m[37m [39;49;00m[31mposition[39;49;00m))[37m[39;49;00m$
  1130^I[37m      [39;49;00m([32mgoto-char[39;49;00m[37m [39;49;00m([31mposn-point[39;49;00m[37m [39;49;00m[31mposition[39;49;00m))))[37m[39;49;00m$
  1131^I[37m[39;49;00m$
  1132^I([36mdefsubst[39;49;00m[37m [39;49;00m[31mposn-x-y[39;49;00m[37m [39;49;00m([31mposition[39;49;00m)[37m[39;49;00m$
  1133^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn the x and y coordinates in POSITION.[39;49;00m$
  1134^I[33mThe return value has the form (X . Y), where X and Y are given in[39;49;00m$
  1135^I[33mpixels.  POSITION should be a list of the form returned by[39;49;00m$
  1136^I[33m`event-start'[39;49;00m[33m and [39;49;00m[33m`event-end'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1137^I[37m  [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m[31mposition[39;49;00m))[37m[39;49;00m$
  1138^I[37m[39;49;00m$
  1139^I([36mdeclare-function[39;49;00m[37m [39;49;00m[31mscroll-bar-scale[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mscroll-bar[39;49;00m[33m"[39;49;00m[37m [39;49;00m([31mnum-denom[39;49;00m[37m [39;49;00m[31mwhole[39;49;00m))[37m[39;49;00m$
  1140^I[37m[39;49;00m$
  1141^I([36mdefun[39;49;00m[37m [39;49;00m[31mposn-col-row[39;49;00m[37m [39;49;00m([31mposition[39;49;00m)[37m[39;49;00m$
  1142^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn the nominal column and row in POSITION, measured in characters.[39;49;00m$
  1143^I[33mThe column and row values are approximations calculated from the x[39;49;00m$
  1144^I[33mand y coordinates in POSITION and the frame's default character width[39;49;00m$
  1145^I[33mand default line height, including spacing.[39;49;00m$
  1146^I[33mFor a scroll-bar event, the result column is 0, and the row[39;49;00m$
  1147^I[33mcorresponds to the vertical position of the click in the scroll bar.[39;49;00m$
  1148^I[33mPOSITION should be a list of the form returned by the [39;49;00m[33m`event-start'[39;49;00m[33m[39;49;00m$
  1149^I[33mand [39;49;00m[33m`event-end'[39;49;00m[33m functions.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1150^I[37m  [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mpair[39;49;00m[37m            [39;49;00m([31mposn-x-y[39;49;00m[37m [39;49;00m[31mposition[39;49;00m))[37m[39;49;00m$
  1151^I[37m         [39;49;00m([31mframe-or-window[39;49;00m[37m [39;49;00m([31mposn-window[39;49;00m[37m [39;49;00m[31mposition[39;49;00m))[37m[39;49;00m$
  1152^I[37m         [39;49;00m([31mframe[39;49;00m[37m           [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mframep[39;49;00m[37m [39;49;00m[31mframe-or-window[39;49;00m)[37m[39;49;00m$
  1153^I[37m                              [39;49;00m[31mframe-or-window[39;49;00m[37m[39;49;00m$
  1154^I[37m                            [39;49;00m([32mwindow-frame[39;49;00m[37m [39;49;00m[31mframe-or-window[39;49;00m)))[37m[39;49;00m$
  1155^I[37m         [39;49;00m([31mwindow[39;49;00m[37m          [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mwindowp[39;49;00m[37m [39;49;00m[31mframe-or-window[39;49;00m)[37m [39;49;00m[31mframe-or-window[39;49;00m))[37m[39;49;00m$
  1156^I[37m         [39;49;00m([31marea[39;49;00m[37m            [39;49;00m([31mposn-area[39;49;00m[37m [39;49;00m[31mposition[39;49;00m)))[37m[39;49;00m$
  1157^I[37m    [39;49;00m([34mcond[39;49;00m[37m[39;49;00m$
  1158^I[37m     [39;49;00m(([32mnull[39;49;00m[37m [39;49;00m[31mframe-or-window[39;49;00m)[37m[39;49;00m$
  1159^I[37m      [39;49;00m'([34m0[39;49;00m[37m [39;49;00m.[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m$
  1160^I[37m     [39;49;00m(([32meq[39;49;00m[37m [39;49;00m[31marea[39;49;00m[37m [39;49;00m[33m'vertical-scroll-bar[39;49;00m)[37m[39;49;00m$
  1161^I[37m      [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m([31mscroll-bar-scale[39;49;00m[37m [39;49;00m[31mpair[39;49;00m[37m [39;49;00m([32m1-[39;49;00m[37m [39;49;00m([31mwindow-height[39;49;00m[37m [39;49;00m[31mwindow[39;49;00m)))))[37m[39;49;00m$
  1162^I[37m     [39;49;00m(([32meq[39;49;00m[37m [39;49;00m[31marea[39;49;00m[37m [39;49;00m[33m'horizontal-scroll-bar[39;49;00m)[37m[39;49;00m$
  1163^I[37m      [39;49;00m([32mcons[39;49;00m[37m [39;49;00m([31mscroll-bar-scale[39;49;00m[37m [39;49;00m[31mpair[39;49;00m[37m [39;49;00m([31mwindow-width[39;49;00m[37m [39;49;00m[31mwindow[39;49;00m))[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m$
  1164^I[37m     [39;49;00m([31mt[39;49;00m[37m[39;49;00m$
  1165^I[37m      [39;49;00m[37m;; FIXME: This should take line-spacing properties on[39;49;00m[37m[39;49;00m$
  1166^I[37m      [39;49;00m[37m;; newlines into account.[39;49;00m[37m[39;49;00m$
  1167^I[37m      [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mspacing[39;49;00m[37m [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([31mdisplay-graphic-p[39;49;00m[37m [39;49;00m[31mframe[39;49;00m)[37m[39;49;00m$
  1168^I[37m                        [39;49;00m([34mor[39;49;00m[37m [39;49;00m([36mwith-current-buffer[39;49;00m[37m[39;49;00m$
  1169^I[37m                                [39;49;00m([32mwindow-buffer[39;49;00m[37m [39;49;00m([32mframe-selected-window[39;49;00m[37m [39;49;00m[31mframe[39;49;00m))[37m[39;49;00m$
  1170^I[37m                              [39;49;00m[31mline-spacing[39;49;00m)[37m[39;49;00m$
  1171^I[37m                            [39;49;00m([32mframe-parameter[39;49;00m[37m [39;49;00m[31mframe[39;49;00m[37m [39;49;00m[33m'line-spacing[39;49;00m)))))[37m[39;49;00m$
  1172^I[37m^I[39;49;00m([34mcond[39;49;00m[37m [39;49;00m(([32mfloatp[39;49;00m[37m [39;49;00m[31mspacing[39;49;00m)[37m[39;49;00m$
  1173^I[37m^I       [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mspacing[39;49;00m[37m [39;49;00m([32mtruncate[39;49;00m[37m [39;49;00m([32m*[39;49;00m[37m [39;49;00m[31mspacing[39;49;00m[37m[39;49;00m$
  1174^I[37m^I^I^I^I^I  [39;49;00m([32mframe-char-height[39;49;00m[37m [39;49;00m[31mframe[39;49;00m)))))[37m[39;49;00m$
  1175^I[37m^I      [39;49;00m(([32mnull[39;49;00m[37m [39;49;00m[31mspacing[39;49;00m)[37m[39;49;00m$
  1176^I[37m^I       [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mspacing[39;49;00m[37m [39;49;00m[34m0[39;49;00m)))[37m[39;49;00m$
  1177^I[37m^I[39;49;00m([32mcons[39;49;00m[37m [39;49;00m([32m/[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mpair[39;49;00m)[37m [39;49;00m([32mframe-char-width[39;49;00m[37m [39;49;00m[31mframe[39;49;00m))[37m[39;49;00m$
  1178^I[37m^I      [39;49;00m([32m/[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mpair[39;49;00m)[37m [39;49;00m([32m+[39;49;00m[37m [39;49;00m([32mframe-char-height[39;49;00m[37m [39;49;00m[31mframe[39;49;00m)[37m [39;49;00m[31mspacing[39;49;00m))))))))[37m[39;49;00m$
  1179^I[37m[39;49;00m$
  1180^I([36mdefun[39;49;00m[37m [39;49;00m[31mposn-actual-col-row[39;49;00m[37m [39;49;00m([31mposition[39;49;00m)[37m[39;49;00m$
  1181^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn the window row number in POSITION and character number in that row.[39;49;00m$
  1182^I[33m[39;49;00m$
  1183^I[33mReturn nil if POSITION does not contain the actual position; in that case[39;49;00m$
  1184^I[33m\`[39;49;00m[33mposn-col-row' can be used to get approximate values.[39;49;00m$
  1185^I[33mPOSITION should be a list of the form returned by the [39;49;00m[33m`event-start'[39;49;00m[33m[39;49;00m$
  1186^I[33mand [39;49;00m[33m`event-end'[39;49;00m[33m functions.[39;49;00m$
  1187^I[33m[39;49;00m$
  1188^I[33mThis function does not account for the width on display, like the[39;49;00m$
  1189^I[33mnumber of visual columns taken by a TAB or image.  If you need[39;49;00m$
  1190^I[33mthe coordinates of POSITION in character units, you should use[39;49;00m$
  1191^I[33m\`[39;49;00m[33mposn-col-row', not this function.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1192^I[37m  [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m6[39;49;00m[37m [39;49;00m[31mposition[39;49;00m))[37m[39;49;00m$
  1193^I[37m[39;49;00m$
  1194^I([36mdefsubst[39;49;00m[37m [39;49;00m[31mposn-timestamp[39;49;00m[37m [39;49;00m([31mposition[39;49;00m)[37m[39;49;00m$
  1195^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn the timestamp of POSITION.[39;49;00m$
  1196^I[33mPOSITION should be a list of the form returned by the [39;49;00m[33m`event-start'[39;49;00m[33m[39;49;00m$
  1197^I[33mand [39;49;00m[33m`event-end'[39;49;00m[33m functions.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1198^I[37m  [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m3[39;49;00m[37m [39;49;00m[31mposition[39;49;00m))[37m[39;49;00m$
  1199^I[37m[39;49;00m$
  1200^I([36mdefun[39;49;00m[37m [39;49;00m[31mposn-string[39;49;00m[37m [39;49;00m([31mposition[39;49;00m)[37m[39;49;00m$
  1201^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn the string object of POSITION.[39;49;00m$
  1202^I[33mValue is a cons (STRING . STRING-POS), or nil if not a string.[39;49;00m$
  1203^I[33mPOSITION should be a list of the form returned by the [39;49;00m[33m`event-start'[39;49;00m[33m[39;49;00m$
  1204^I[33mand [39;49;00m[33m`event-end'[39;49;00m[33m functions.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1205^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mx[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m4[39;49;00m[37m [39;49;00m[31mposition[39;49;00m)))[37m[39;49;00m$
  1206^I[37m    [39;49;00m[37m;; Apparently this can also be `handle' or `below-handle' (bug#13979).[39;49;00m[37m[39;49;00m$
  1207^I[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mx[39;49;00m)[37m [39;49;00m[31mx[39;49;00m)))[37m[39;49;00m$
  1208^I[37m[39;49;00m$
  1209^I([36mdefsubst[39;49;00m[37m [39;49;00m[31mposn-image[39;49;00m[37m [39;49;00m([31mposition[39;49;00m)[37m[39;49;00m$
  1210^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn the image object of POSITION.[39;49;00m$
  1211^I[33mValue is a list (image ...), or nil if not an image.[39;49;00m$
  1212^I[33mPOSITION should be a list of the form returned by the [39;49;00m[33m`event-start'[39;49;00m[33m[39;49;00m$
  1213^I[33mand [39;49;00m[33m`event-end'[39;49;00m[33m functions.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1214^I[37m  [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m7[39;49;00m[37m [39;49;00m[31mposition[39;49;00m))[37m[39;49;00m$
  1215^I[37m[39;49;00m$
  1216^I([36mdefsubst[39;49;00m[37m [39;49;00m[31mposn-object[39;49;00m[37m [39;49;00m([31mposition[39;49;00m)[37m[39;49;00m$
  1217^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn the object (image or string) of POSITION.[39;49;00m$
  1218^I[33mValue is a list (image ...) for an image object, a cons cell[39;49;00m$
  1219^I[33m\([39;49;00m[33mSTRING . STRING-POS) for a string object, and nil for a buffer position.[39;49;00m$
  1220^I[33mPOSITION should be a list of the form returned by the [39;49;00m[33m`event-start'[39;49;00m[33m[39;49;00m$
  1221^I[33mand [39;49;00m[33m`event-end'[39;49;00m[33m functions.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1222^I[37m  [39;49;00m([34mor[39;49;00m[37m [39;49;00m([31mposn-image[39;49;00m[37m [39;49;00m[31mposition[39;49;00m)[37m [39;49;00m([31mposn-string[39;49;00m[37m [39;49;00m[31mposition[39;49;00m)))[37m[39;49;00m$
  1223^I[37m[39;49;00m$
  1224^I([36mdefsubst[39;49;00m[37m [39;49;00m[31mposn-object-x-y[39;49;00m[37m [39;49;00m([31mposition[39;49;00m)[37m[39;49;00m$
  1225^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn the x and y coordinates relative to the object of POSITION.[39;49;00m$
  1226^I[33mThe return value has the form (DX . DY), where DX and DY are[39;49;00m$
  1227^I[33mgiven in pixels.  POSITION should be a list of the form returned[39;49;00m$
  1228^I[33mby [39;49;00m[33m`event-start'[39;49;00m[33m and [39;49;00m[33m`event-end'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1229^I[37m  [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m8[39;49;00m[37m [39;49;00m[31mposition[39;49;00m))[37m[39;49;00m$
  1230^I[37m[39;49;00m$
  1231^I([36mdefsubst[39;49;00m[37m [39;49;00m[31mposn-object-width-height[39;49;00m[37m [39;49;00m([31mposition[39;49;00m)[37m[39;49;00m$
  1232^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn the pixel width and height of the object of POSITION.[39;49;00m$
  1233^I[33mThe return value has the form (WIDTH . HEIGHT).  POSITION should[39;49;00m$
  1234^I[33mbe a list of the form returned by [39;49;00m[33m`event-start'[39;49;00m[33m and [39;49;00m[33m`event-end'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1235^I[37m  [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m9[39;49;00m[37m [39;49;00m[31mposition[39;49;00m))[37m[39;49;00m$
  1236^I[37m[39;49;00m$
  1237^I[37m[39;49;00m[37m[39;49;00m$
  1238^I[37m;;;; Obsolescent names for functions.[39;49;00m[37m[39;49;00m$
  1239^I[37m[39;49;00m$
  1240^I([36mdefine-obsolete-function-alias[39;49;00m[37m [39;49;00m[33m'window-dot[39;49;00m[37m [39;49;00m[33m'window-point[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m22.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1241^I([36mdefine-obsolete-function-alias[39;49;00m[37m [39;49;00m[33m'set-window-dot[39;49;00m[37m [39;49;00m[33m'set-window-point[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m22.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1242^I([36mdefine-obsolete-function-alias[39;49;00m[37m [39;49;00m[33m'read-input[39;49;00m[37m [39;49;00m[33m'read-string[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m22.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1243^I([36mdefine-obsolete-function-alias[39;49;00m[37m [39;49;00m[33m'show-buffer[39;49;00m[37m [39;49;00m[33m'set-window-buffer[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m22.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1244^I([36mdefine-obsolete-function-alias[39;49;00m[37m [39;49;00m[33m'eval-current-buffer[39;49;00m[37m [39;49;00m[33m'eval-buffer[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m22.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1245^I([36mdefine-obsolete-function-alias[39;49;00m[37m [39;49;00m[33m'string-to-int[39;49;00m[37m [39;49;00m[33m'string-to-number[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m22.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1246^I[37m[39;49;00m$
  1247^I([31mmake-obsolete[39;49;00m[37m [39;49;00m[33m'forward-point[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33muse (+ (point) N) instead.[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1248^I([31mmake-obsolete[39;49;00m[37m [39;49;00m[33m'buffer-has-markers-at[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m24.3[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1249^I[37m[39;49;00m$
  1250^I([36mdefun[39;49;00m[37m [39;49;00m[31minsert-string[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31margs[39;49;00m)[37m[39;49;00m$
  1251^I[37m  [39;49;00m[33m"[39;49;00m[33mMocklisp-compatibility insert function.[39;49;00m$
  1252^I[33mLike the function [39;49;00m[33m`insert'[39;49;00m[33m except that any argument that is a number[39;49;00m$
  1253^I[33mis converted into a string by expressing it in decimal.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1254^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mobsolete[39;49;00m[37m [39;49;00m[32minsert[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m22.1[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
  1255^I[37m  [39;49;00m([36mdolist[39;49;00m[37m [39;49;00m([31mel[39;49;00m[37m [39;49;00m[31margs[39;49;00m)[37m[39;49;00m$
  1256^I[37m    [39;49;00m([32minsert[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mintegerp[39;49;00m[37m [39;49;00m[31mel[39;49;00m)[37m [39;49;00m([32mnumber-to-string[39;49;00m[37m [39;49;00m[31mel[39;49;00m)[37m [39;49;00m[31mel[39;49;00m))))[37m[39;49;00m$
  1257^I[37m[39;49;00m$
  1258^I([36mdefun[39;49;00m[37m [39;49;00m[31mmakehash[39;49;00m[37m [39;49;00m([34m&optional[39;49;00m[37m [39;49;00m[31mtest[39;49;00m)[37m[39;49;00m$
  1259^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mobsolete[39;49;00m[37m [39;49;00m[32mmake-hash-table[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m22.1[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
  1260^I[37m  [39;49;00m([32mmake-hash-table[39;49;00m[37m [39;49;00m[36m:test[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mtest[39;49;00m[37m [39;49;00m[33m'eql[39;49;00m)))[37m[39;49;00m$
  1261^I[37m[39;49;00m$
  1262^I([36mdefun[39;49;00m[37m [39;49;00m[31mlog10[39;49;00m[37m [39;49;00m([31mx[39;49;00m)[37m[39;49;00m$
  1263^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn (log X 10), the log base 10 of X.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1264^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mobsolete[39;49;00m[37m [39;49;00m[32mlog[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m24.4[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
  1265^I[37m  [39;49;00m([32mlog[39;49;00m[37m [39;49;00m[31mx[39;49;00m[37m [39;49;00m[34m10[39;49;00m))[37m[39;49;00m$
  1266^I[37m[39;49;00m$
  1267^I[37m;; These are used by VM and some old programs[39;49;00m[37m[39;49;00m$
  1268^I([36mdefalias[39;49;00m[37m [39;49;00m[33m'focus-frame[39;49;00m[37m [39;49;00m[33m'ignore[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1269^I([31mmake-obsolete[39;49;00m[37m [39;49;00m[33m'focus-frame[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mit does nothing.[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m22.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1270^I([36mdefalias[39;49;00m[37m [39;49;00m[33m'unfocus-frame[39;49;00m[37m [39;49;00m[33m'ignore[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1271^I([31mmake-obsolete[39;49;00m[37m [39;49;00m[33m'unfocus-frame[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mit does nothing.[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m22.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1272^I([31mmake-obsolete[39;49;00m[37m [39;49;00m[33m'make-variable-frame-local[39;49;00m[37m[39;49;00m$
  1273^I[37m^I       [39;49;00m[33m"[39;49;00m[33mexplicitly check for a frame-parameter instead.[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m22.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1274^I([31mset-advertised-calling-convention[39;49;00m[37m[39;49;00m$
  1275^I[37m [39;49;00m[33m'all-completions[39;49;00m[37m [39;49;00m'([32mstring[39;49;00m[37m [39;49;00m[31mcollection[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mpredicate[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m23.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1276^I([31mset-advertised-calling-convention[39;49;00m[37m [39;49;00m[33m'unintern[39;49;00m[37m [39;49;00m'([31mname[39;49;00m[37m [39;49;00m[31mobarray[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m23.3[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1277^I([31mset-advertised-calling-convention[39;49;00m[37m [39;49;00m[33m'indirect-function[39;49;00m[37m [39;49;00m'([31mobject[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m25.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1278^I([31mset-advertised-calling-convention[39;49;00m[37m [39;49;00m[33m'redirect-frame-focus[39;49;00m[37m [39;49;00m'([31mframe[39;49;00m[37m [39;49;00m[31mfocus-frame[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m24.3[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1279^I([31mset-advertised-calling-convention[39;49;00m[37m [39;49;00m[33m'decode-char[39;49;00m[37m [39;49;00m'([31mch[39;49;00m[37m [39;49;00m[31mcharset[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m21.4[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1280^I([31mset-advertised-calling-convention[39;49;00m[37m [39;49;00m[33m'encode-char[39;49;00m[37m [39;49;00m'([31mch[39;49;00m[37m [39;49;00m[31mcharset[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m21.4[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1281^I[37m[39;49;00m[37m[39;49;00m$
  1282^I[37m;;;; Obsolescence declarations for variables, and aliases.[39;49;00m[37m[39;49;00m$
  1283^I[37m[39;49;00m$
  1284^I[37m;; Special "default-FOO" variables which contain the default value of[39;49;00m[37m[39;49;00m$
  1285^I[37m;; the "FOO" variable are nasty.  Their implementation is brittle, and[39;49;00m[37m[39;49;00m$
  1286^I[37m;; slows down several unrelated variable operations; furthermore, they[39;49;00m[37m[39;49;00m$
  1287^I[37m;; can lead to really odd behavior if you decide to make them[39;49;00m[37m[39;49;00m$
  1288^I[37m;; buffer-local.[39;49;00m[37m[39;49;00m$
  1289^I[37m[39;49;00m$
  1290^I[37m;; Not used at all in Emacs, last time I checked:[39;49;00m[37m[39;49;00m$
  1291^I([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-mode-line-format[39;49;00m[37m [39;49;00m[33m'mode-line-format[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1292^I([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-header-line-format[39;49;00m[37m [39;49;00m[33m'header-line-format[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1293^I([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-line-spacing[39;49;00m[37m [39;49;00m[33m'line-spacing[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1294^I([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-abbrev-mode[39;49;00m[37m [39;49;00m[33m'abbrev-mode[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1295^I([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-ctl-arrow[39;49;00m[37m [39;49;00m[33m'ctl-arrow[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1296^I([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-truncate-lines[39;49;00m[37m [39;49;00m[33m'truncate-lines[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1297^I([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-left-margin[39;49;00m[37m [39;49;00m[33m'left-margin[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1298^I([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-tab-width[39;49;00m[37m [39;49;00m[33m'tab-width[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1299^I([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-case-fold-search[39;49;00m[37m [39;49;00m[33m'case-fold-search[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1300^I([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-left-margin-width[39;49;00m[37m [39;49;00m[33m'left-margin-width[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1301^I([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-right-margin-width[39;49;00m[37m [39;49;00m[33m'right-margin-width[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1302^I([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-left-fringe-width[39;49;00m[37m [39;49;00m[33m'left-fringe-width[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1303^I([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-right-fringe-width[39;49;00m[37m [39;49;00m[33m'right-fringe-width[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1304^I([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-fringes-outside-margins[39;49;00m[37m [39;49;00m[33m'fringes-outside-margins[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1305^I([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-scroll-bar-width[39;49;00m[37m [39;49;00m[33m'scroll-bar-width[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1306^I([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-vertical-scroll-bar[39;49;00m[37m [39;49;00m[33m'vertical-scroll-bar[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1307^I([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-indicate-empty-lines[39;49;00m[37m [39;49;00m[33m'indicate-empty-lines[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1308^I([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-indicate-buffer-boundaries[39;49;00m[37m [39;49;00m[33m'indicate-buffer-boundaries[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1309^I([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-fringe-indicator-alist[39;49;00m[37m [39;49;00m[33m'fringe-indicator-alist[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1310^I([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-fringe-cursor-alist[39;49;00m[37m [39;49;00m[33m'fringe-cursor-alist[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1311^I([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-scroll-up-aggressively[39;49;00m[37m [39;49;00m[33m'scroll-up-aggressively[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1312^I([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-scroll-down-aggressively[39;49;00m[37m [39;49;00m[33m'scroll-down-aggressively[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1313^I([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-fill-column[39;49;00m[37m [39;49;00m[33m'fill-column[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1314^I([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-cursor-type[39;49;00m[37m [39;49;00m[33m'cursor-type[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1315^I([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-cursor-in-non-selected-windows[39;49;00m[37m [39;49;00m[33m'cursor-in-non-selected-windows[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1316^I([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-buffer-file-coding-system[39;49;00m[37m [39;49;00m[33m'buffer-file-coding-system[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1317^I([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-major-mode[39;49;00m[37m [39;49;00m[33m'major-mode[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1318^I([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-enable-multibyte-characters[39;49;00m[37m[39;49;00m$
  1319^I[37m      [39;49;00m[33m"[39;49;00m[33muse enable-multibyte-characters or set-buffer-multibyte instead[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1320^I[37m[39;49;00m$
  1321^I([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'define-key-rebound-commands[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1322^I([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'redisplay-end-trigger-functions[39;49;00m[37m [39;49;00m[33m'jit-lock-register[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1323^I([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'deferred-action-list[39;49;00m[37m [39;49;00m[33m'post-command-hook[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m24.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1324^I([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'deferred-action-function[39;49;00m[37m [39;49;00m[33m'post-command-hook[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m24.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1325^I([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'redisplay-dont-pause[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m24.5[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1326^I([31mmake-obsolete[39;49;00m[37m [39;49;00m[33m'window-redisplay-end-trigger[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1327^I([31mmake-obsolete[39;49;00m[37m [39;49;00m[33m'set-window-redisplay-end-trigger[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1328^I[37m[39;49;00m$
  1329^I([31mmake-obsolete[39;49;00m[37m [39;49;00m[33m'process-filter-multibyte-p[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1330^I([31mmake-obsolete[39;49;00m[37m [39;49;00m[33m'set-process-filter-multibyte[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1331^I[37m[39;49;00m$
  1332^I[37m;; Lisp manual only updated in 22.1.[39;49;00m[37m[39;49;00m$
  1333^I([36mdefine-obsolete-variable-alias[39;49;00m[37m [39;49;00m[33m'executing-macro[39;49;00m[37m [39;49;00m[33m'executing-kbd-macro[39;49;00m[37m[39;49;00m$
  1334^I[37m  [39;49;00m[33m"[39;49;00m[33mbefore 19.34[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1335^I[37m[39;49;00m$
  1336^I([36mdefine-obsolete-variable-alias[39;49;00m[37m [39;49;00m[33m'x-lost-selection-hooks[39;49;00m[37m[39;49;00m$
  1337^I[37m  [39;49;00m[33m'x-lost-selection-functions[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m22.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1338^I([36mdefine-obsolete-variable-alias[39;49;00m[37m [39;49;00m[33m'x-sent-selection-hooks[39;49;00m[37m[39;49;00m$
  1339^I[37m  [39;49;00m[33m'x-sent-selection-functions[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m22.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1340^I[37m[39;49;00m$
  1341^I[37m;; This was introduced in 21.4 for pre-unicode unification.  That[39;49;00m[37m[39;49;00m$
  1342^I[37m;; usage was rendered obsolete in 23.1 which uses Unicode internally.[39;49;00m[37m[39;49;00m$
  1343^I[37m;; Other uses are possible, so this variable is not _really_ obsolete,[39;49;00m[37m[39;49;00m$
  1344^I[37m;; but Stefan insists to mark it so.[39;49;00m[37m[39;49;00m$
  1345^I([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'translation-table-for-input[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1346^I[37m[39;49;00m$
  1347^I([36mdefvaralias[39;49;00m[37m [39;49;00m[33m'messages-buffer-max-lines[39;49;00m[37m [39;49;00m[33m'message-log-max[39;49;00m)[37m[39;49;00m$
  1348^I[37m[39;49;00m[37m[39;49;00m$
  1349^I[37m;;;; Alternate names for functions - these are not being phased out.[39;49;00m[37m[39;49;00m$
  1350^I[37m[39;49;00m$
  1351^I([36mdefalias[39;49;00m[37m [39;49;00m[33m'send-string[39;49;00m[37m [39;49;00m[33m'process-send-string[39;49;00m)[37m[39;49;00m$
  1352^I([36mdefalias[39;49;00m[37m [39;49;00m[33m'send-region[39;49;00m[37m [39;49;00m[33m'process-send-region[39;49;00m)[37m[39;49;00m$
  1353^I([36mdefalias[39;49;00m[37m [39;49;00m[33m'string=[39;49;00m[37m [39;49;00m[33m'string-equal[39;49;00m)[37m[39;49;00m$
  1354^I([36mdefalias[39;49;00m[37m [39;49;00m[33m'string<[39;49;00m[37m [39;49;00m[33m'string-lessp[39;49;00m)[37m[39;49;00m$
  1355^I([36mdefalias[39;49;00m[37m [39;49;00m[33m'move-marker[39;49;00m[37m [39;49;00m[33m'set-marker[39;49;00m)[37m[39;49;00m$
  1356^I([36mdefalias[39;49;00m[37m [39;49;00m[33m'rplaca[39;49;00m[37m [39;49;00m[33m'setcar[39;49;00m)[37m[39;49;00m$
  1357^I([36mdefalias[39;49;00m[37m [39;49;00m[33m'rplacd[39;49;00m[37m [39;49;00m[33m'setcdr[39;49;00m)[37m[39;49;00m$
  1358^I([36mdefalias[39;49;00m[37m [39;49;00m[33m'beep[39;49;00m[37m [39;49;00m[33m'ding[39;49;00m)[37m [39;49;00m[37m;preserve lingual purity[39;49;00m[37m[39;49;00m$
  1359^I([36mdefalias[39;49;00m[37m [39;49;00m[33m'indent-to-column[39;49;00m[37m [39;49;00m[33m'indent-to[39;49;00m)[37m[39;49;00m$
  1360^I([36mdefalias[39;49;00m[37m [39;49;00m[33m'backward-delete-char[39;49;00m[37m [39;49;00m[33m'delete-backward-char[39;49;00m)[37m[39;49;00m$
  1361^I([36mdefalias[39;49;00m[37m [39;49;00m[33m'search-forward-regexp[39;49;00m[37m [39;49;00m([32msymbol-function[39;49;00m[37m [39;49;00m[33m're-search-forward[39;49;00m))[37m[39;49;00m$
  1362^I([36mdefalias[39;49;00m[37m [39;49;00m[33m'search-backward-regexp[39;49;00m[37m [39;49;00m([32msymbol-function[39;49;00m[37m [39;49;00m[33m're-search-backward[39;49;00m))[37m[39;49;00m$
  1363^I([36mdefalias[39;49;00m[37m [39;49;00m[33m'int-to-string[39;49;00m[37m [39;49;00m[33m'number-to-string[39;49;00m)[37m[39;49;00m$
  1364^I([36mdefalias[39;49;00m[37m [39;49;00m[33m'store-match-data[39;49;00m[37m [39;49;00m[33m'set-match-data[39;49;00m)[37m[39;49;00m$
  1365^I([36mdefalias[39;49;00m[37m [39;49;00m[33m'chmod[39;49;00m[37m [39;49;00m[33m'set-file-modes[39;49;00m)[37m[39;49;00m$
  1366^I([36mdefalias[39;49;00m[37m [39;49;00m[33m'mkdir[39;49;00m[37m [39;49;00m[33m'make-directory[39;49;00m)[37m[39;49;00m$
  1367^I[37m;; These are the XEmacs names:[39;49;00m[37m[39;49;00m$
  1368^I([36mdefalias[39;49;00m[37m [39;49;00m[33m'point-at-eol[39;49;00m[37m [39;49;00m[33m'line-end-position[39;49;00m)[37m[39;49;00m$
  1369^I([36mdefalias[39;49;00m[37m [39;49;00m[33m'point-at-bol[39;49;00m[37m [39;49;00m[33m'line-beginning-position[39;49;00m)[37m[39;49;00m$
  1370^I[37m[39;49;00m$
  1371^I([36mdefalias[39;49;00m[37m [39;49;00m[33m'user-original-login-name[39;49;00m[37m [39;49;00m[33m'user-login-name[39;49;00m)[37m[39;49;00m$
  1372^I[37m[39;49;00m$
  1373^I[37m[39;49;00m[37m[39;49;00m$
  1374^I[37m;;;; Hook manipulation functions.[39;49;00m[37m[39;49;00m$
  1375^I[37m[39;49;00m$
  1376^I([36mdefun[39;49;00m[37m [39;49;00m[31madd-hook[39;49;00m[37m [39;49;00m([31mhook[39;49;00m[37m [39;49;00m[34mfunction[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[32mappend[39;49;00m[37m [39;49;00m[31mlocal[39;49;00m)[37m[39;49;00m$
  1377^I[37m  [39;49;00m[33m"[39;49;00m[33mAdd to the value of HOOK the function FUNCTION.[39;49;00m$
  1378^I[33mFUNCTION is not added if already present.[39;49;00m$
  1379^I[33mFUNCTION is added (if necessary) at the beginning of the hook list[39;49;00m$
  1380^I[33munless the optional argument APPEND is non-nil, in which case[39;49;00m$
  1381^I[33mFUNCTION is added at the end.[39;49;00m$
  1382^I[33m[39;49;00m$
  1383^I[33mThe optional fourth argument, LOCAL, if non-nil, says to modify[39;49;00m$
  1384^I[33mthe hook's buffer-local value rather than its global value.[39;49;00m$
  1385^I[33mThis makes the hook buffer-local, and it makes t a member of the[39;49;00m$
  1386^I[33mbuffer-local value.  That acts as a flag to run the hook[39;49;00m$
  1387^I[33mfunctions of the global value as well as in the local value.[39;49;00m$
  1388^I[33m[39;49;00m$
  1389^I[33mHOOK should be a symbol, and FUNCTION may be any valid function.  If[39;49;00m$
  1390^I[33mHOOK is void, it is first set to nil.  If HOOK's value is a single[39;49;00m$
  1391^I[33mfunction, it is changed to a list of functions.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1392^I[37m  [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mboundp[39;49;00m[37m [39;49;00m[31mhook[39;49;00m)[37m [39;49;00m([32mset[39;49;00m[37m [39;49;00m[31mhook[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m$
  1393^I[37m  [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mdefault-boundp[39;49;00m[37m [39;49;00m[31mhook[39;49;00m)[37m [39;49;00m([32mset-default[39;49;00m[37m [39;49;00m[31mhook[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m$
  1394^I[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mlocal[39;49;00m[37m [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32mlocal-variable-if-set-p[39;49;00m[37m [39;49;00m[31mhook[39;49;00m)[37m[39;49;00m$
  1395^I[37m^I      [39;49;00m([32mset[39;49;00m[37m [39;49;00m([32mmake-local-variable[39;49;00m[37m [39;49;00m[31mhook[39;49;00m)[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[31mt[39;49;00m)))[37m[39;49;00m$
  1396^I[37m    [39;49;00m[37m;; Detect the case where make-local-variable was used on a hook[39;49;00m[37m[39;49;00m$
  1397^I[37m    [39;49;00m[37m;; and do what we used to do.[39;49;00m[37m[39;49;00m$
  1398^I[37m    [39;49;00m([36munless[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mhook[39;49;00m))[37m [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mhook[39;49;00m)))[37m[39;49;00m$
  1399^I[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mlocal[39;49;00m[37m [39;49;00m[31mt[39;49;00m)))[37m[39;49;00m$
  1400^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mhook-value[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mlocal[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mhook[39;49;00m)[37m [39;49;00m([32mdefault-value[39;49;00m[37m [39;49;00m[31mhook[39;49;00m))))[37m[39;49;00m$
  1401^I[37m    [39;49;00m[37m;; If the hook value is a single function, turn it into a list.[39;49;00m[37m[39;49;00m$
  1402^I[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mlistp[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m))[37m [39;49;00m([32mfunctionp[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m))[37m[39;49;00m$
  1403^I[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m)))[37m[39;49;00m$
  1404^I[37m    [39;49;00m[37m;; Do the actual addition if necessary[39;49;00m[37m[39;49;00m$
  1405^I[37m    [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32mmember[39;49;00m[37m [39;49;00m[34mfunction[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m)[37m[39;49;00m$
  1406^I[37m      [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m[34mfunction[39;49;00m)[37m[39;49;00m$
  1407^I[37m^I[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[34mfunction[39;49;00m[37m [39;49;00m([32mpurecopy[39;49;00m[37m [39;49;00m[34mfunction[39;49;00m)))[37m[39;49;00m$
  1408^I[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m[37m[39;49;00m$
  1409^I[37m^I    [39;49;00m([34mif[39;49;00m[37m [39;49;00m[32mappend[39;49;00m[37m[39;49;00m$
  1410^I[37m^I^I[39;49;00m([32mappend[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[34mfunction[39;49;00m))[37m[39;49;00m$
  1411^I[37m^I      [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[34mfunction[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m))))[37m[39;49;00m$
  1412^I[37m    [39;49;00m[37m;; Set the actual variable[39;49;00m[37m[39;49;00m$
  1413^I[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mlocal[39;49;00m[37m[39;49;00m$
  1414^I[37m^I[39;49;00m([34mprogn[39;49;00m[37m[39;49;00m$
  1415^I[37m^I  [39;49;00m[37m;; If HOOK isn't a permanent local,[39;49;00m[37m[39;49;00m$
  1416^I[37m^I  [39;49;00m[37m;; but FUNCTION wants to survive a change of modes,[39;49;00m[37m[39;49;00m$
  1417^I[37m^I  [39;49;00m[37m;; mark HOOK as partially permanent.[39;49;00m[37m[39;49;00m$
  1418^I[37m^I  [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32msymbolp[39;49;00m[37m [39;49;00m[34mfunction[39;49;00m)[37m[39;49;00m$
  1419^I[37m^I       [39;49;00m([32mget[39;49;00m[37m [39;49;00m[34mfunction[39;49;00m[37m [39;49;00m[33m'permanent-local-hook[39;49;00m)[37m[39;49;00m$
  1420^I[37m^I       [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mget[39;49;00m[37m [39;49;00m[31mhook[39;49;00m[37m [39;49;00m[33m'permanent-local[39;49;00m))[37m[39;49;00m$
  1421^I[37m^I       [39;49;00m([32mput[39;49;00m[37m [39;49;00m[31mhook[39;49;00m[37m [39;49;00m[33m'permanent-local[39;49;00m[37m [39;49;00m[33m'permanent-local-hook[39;49;00m))[37m[39;49;00m$
  1422^I[37m^I  [39;49;00m([32mset[39;49;00m[37m [39;49;00m[31mhook[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m))[37m[39;49;00m$
  1423^I[37m      [39;49;00m([32mset-default[39;49;00m[37m [39;49;00m[31mhook[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m))))[37m[39;49;00m$
  1424^I[37m[39;49;00m$
  1425^I([36mdefun[39;49;00m[37m [39;49;00m[31mremove-hook[39;49;00m[37m [39;49;00m([31mhook[39;49;00m[37m [39;49;00m[34mfunction[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mlocal[39;49;00m)[37m[39;49;00m$
  1426^I[37m  [39;49;00m[33m"[39;49;00m[33mRemove from the value of HOOK the function FUNCTION.[39;49;00m$
  1427^I[33mHOOK should be a symbol, and FUNCTION may be any valid function.  If[39;49;00m$
  1428^I[33mFUNCTION isn't the value of HOOK, or, if FUNCTION doesn't appear in the[39;49;00m$
  1429^I[33mlist of hooks to run in HOOK, then nothing is done.  See [39;49;00m[33m`add-hook'[39;49;00m[33m.[39;49;00m$
  1430^I[33m[39;49;00m$
  1431^I[33mThe optional third argument, LOCAL, if non-nil, says to modify[39;49;00m$
  1432^I[33mthe hook's buffer-local value rather than its default value.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1433^I[37m  [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mboundp[39;49;00m[37m [39;49;00m[31mhook[39;49;00m)[37m [39;49;00m([32mset[39;49;00m[37m [39;49;00m[31mhook[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m$
  1434^I[37m  [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mdefault-boundp[39;49;00m[37m [39;49;00m[31mhook[39;49;00m)[37m [39;49;00m([32mset-default[39;49;00m[37m [39;49;00m[31mhook[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m$
  1435^I[37m  [39;49;00m[37m;; Do nothing if LOCAL is t but this hook has no local binding.[39;49;00m[37m[39;49;00m$
  1436^I[37m  [39;49;00m([36munless[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mlocal[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mlocal-variable-p[39;49;00m[37m [39;49;00m[31mhook[39;49;00m)))[37m[39;49;00m$
  1437^I[37m    [39;49;00m[37m;; Detect the case where make-local-variable was used on a hook[39;49;00m[37m[39;49;00m$
  1438^I[37m    [39;49;00m[37m;; and do what we used to do.[39;49;00m[37m[39;49;00m$
  1439^I[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mlocal-variable-p[39;49;00m[37m [39;49;00m[31mhook[39;49;00m)[37m[39;49;00m$
  1440^I[37m^I       [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mhook[39;49;00m))[37m[39;49;00m$
  1441^I[37m^I^I^I [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mhook[39;49;00m)))))[37m[39;49;00m$
  1442^I[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mlocal[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
  1443^I[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mhook-value[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mlocal[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mhook[39;49;00m)[37m [39;49;00m([32mdefault-value[39;49;00m[37m [39;49;00m[31mhook[39;49;00m))))[37m[39;49;00m$
  1444^I[37m      [39;49;00m[37m;; Remove the function, for both the list and the non-list cases.[39;49;00m[37m[39;49;00m$
  1445^I[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mlistp[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m))[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m)[37m [39;49;00m[33m'lambda[39;49;00m))[37m[39;49;00m$
  1446^I[37m^I  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mequal[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m[37m [39;49;00m[34mfunction[39;49;00m)[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m$
  1447^I[37m^I[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m[37m [39;49;00m([32mdelete[39;49;00m[37m [39;49;00m[34mfunction[39;49;00m[37m [39;49;00m([32mcopy-sequence[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m))))[37m[39;49;00m$
  1448^I[37m      [39;49;00m[37m;; If the function is on the global hook, we need to shadow it locally[39;49;00m[37m[39;49;00m$
  1449^I[37m      [39;49;00m[37m;;(when (and local (member function (default-value hook))[39;49;00m[37m[39;49;00m$
  1450^I[37m      [39;49;00m[37m;;^I       (not (member (cons 'not function) hook-value)))[39;49;00m[37m[39;49;00m$
  1451^I[37m      [39;49;00m[37m;;  (push (cons 'not function) hook-value))[39;49;00m[37m[39;49;00m$
  1452^I[37m      [39;49;00m[37m;; Set the actual variable[39;49;00m[37m[39;49;00m$
  1453^I[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m[31mlocal[39;49;00m)[37m[39;49;00m$
  1454^I[37m^I  [39;49;00m([32mset-default[39;49;00m[37m [39;49;00m[31mhook[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m)[37m[39;49;00m$
  1455^I[37m^I[39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mequal[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m[37m [39;49;00m'([31mt[39;49;00m))[37m[39;49;00m$
  1456^I[37m^I    [39;49;00m([32mkill-local-variable[39;49;00m[37m [39;49;00m[31mhook[39;49;00m)[37m[39;49;00m$
  1457^I[37m^I  [39;49;00m([32mset[39;49;00m[37m [39;49;00m[31mhook[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m))))))[37m[39;49;00m$
  1458^I[37m[39;49;00m$
  1459^I([36mdefmacro[39;49;00m[37m [39;49;00m[36mletrec[39;49;00m[37m [39;49;00m([31mbinders[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
  1460^I[37m  [39;49;00m[33m"[39;49;00m[33mBind variables according to BINDERS then eval BODY.[39;49;00m$
  1461^I[33mThe value of the last form in BODY is returned.[39;49;00m$
  1462^I[33mEach element of BINDERS is a list (SYMBOL VALUEFORM) which binds[39;49;00m$
  1463^I[33mSYMBOL to the value of VALUEFORM.[39;49;00m$
  1464^I[33mAll symbols are bound before the VALUEFORMs are evalled.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1465^I[37m  [39;49;00m[37m;; Only useful in lexical-binding mode.[39;49;00m[37m[39;49;00m$
  1466^I[37m  [39;49;00m[37m;; As a special-form, we could implement it more efficiently (and cleanly,[39;49;00m[37m[39;49;00m$
  1467^I[37m  [39;49;00m[37m;; making the vars actually unbound during evaluation of the binders).[39;49;00m[37m[39;49;00m$
  1468^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[34mlet[39;49;00m)[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m1[39;49;00m))[37m[39;49;00m$
  1469^I[37m  [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m,([32mmapcar[39;49;00m[37m [39;49;00m[32m#'[39;49;00m[32mcar[39;49;00m[37m [39;49;00m[31mbinders[39;49;00m)[37m[39;49;00m$
  1470^I[37m     [39;49;00m,@([32mmapcar[39;49;00m[37m [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31mbinder[39;49;00m)[37m [39;49;00m`([34msetq[39;49;00m[37m [39;49;00m,@[31mbinder[39;49;00m))[37m [39;49;00m[31mbinders[39;49;00m)[37m[39;49;00m$
  1471^I[37m     [39;49;00m,@[31mbody[39;49;00m))[37m[39;49;00m$
  1472^I[37m[39;49;00m$
  1473^I([36mdefmacro[39;49;00m[37m [39;49;00m[36mwith-wrapper-hook[39;49;00m[37m [39;49;00m([31mhook[39;49;00m[37m [39;49;00m[31margs[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
  1474^I[37m  [39;49;00m[33m"[39;49;00m[33mRun BODY, using wrapper functions from HOOK with additional ARGS.[39;49;00m$
  1475^I[33mHOOK is an abnormal hook.  Each hook function in HOOK [39;49;00m[33m\"[39;49;00m[33mwraps[39;49;00m[33m\"[39;49;00m[33m[39;49;00m$
  1476^I[33maround the preceding ones, like a set of nested [39;49;00m[33m`around'[39;49;00m[33m advices.[39;49;00m$
  1477^I[33m[39;49;00m$
  1478^I[33mEach hook function should accept an argument list consisting of a[39;49;00m$
  1479^I[33mfunction FUN, followed by the additional arguments in ARGS.[39;49;00m$
  1480^I[33m[39;49;00m$
  1481^I[33mThe first hook function in HOOK is passed a FUN that, if it is called[39;49;00m$
  1482^I[33mwith arguments ARGS, performs BODY (i.e., the default operation).[39;49;00m$
  1483^I[33mThe FUN passed to each successive hook function is defined based[39;49;00m$
  1484^I[33mon the preceding hook functions; if called with arguments ARGS,[39;49;00m$
  1485^I[33mit does what the [39;49;00m[33m`with-wrapper-hook'[39;49;00m[33m call would do if the[39;49;00m$
  1486^I[33mpreceding hook functions were the only ones present in HOOK.[39;49;00m$
  1487^I[33m[39;49;00m$
  1488^I[33mEach hook function may call its FUN argument as many times as it wishes,[39;49;00m$
  1489^I[33mincluding never.  In that case, such a hook function acts to replace[39;49;00m$
  1490^I[33mthe default definition altogether, and any preceding hook functions.[39;49;00m$
  1491^I[33mOf course, a subsequent hook function may do the same thing.[39;49;00m$
  1492^I[33m[39;49;00m$
  1493^I[33mEach hook function definition is used to construct the FUN passed[39;49;00m$
  1494^I[33mto the next hook function, if any.  The last (or [39;49;00m[33m\"[39;49;00m[33moutermost[39;49;00m[33m\"[39;49;00m[33m)[39;49;00m$
  1495^I[33mFUN is then called once.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1496^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m2[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m([31mform[39;49;00m[37m [39;49;00m[31msexp[39;49;00m[37m [39;49;00m[31mbody[39;49;00m))[37m[39;49;00m$
  1497^I[37m           [39;49;00m([31mobsolete[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33muse a <foo>-function variable modified by [39;49;00m[33m`add-function'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1498^I[37m                     [39;49;00m[33m"[39;49;00m[33m24.4[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
  1499^I[37m  [39;49;00m[37m;; We need those two gensyms because CL's lexical scoping is not available[39;49;00m[37m[39;49;00m$
  1500^I[37m  [39;49;00m[37m;; for function arguments :-([39;49;00m[37m[39;49;00m$
  1501^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mfuns[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mfuns[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
  1502^I[37m        [39;49;00m([31mglobal[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mglobal[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
  1503^I[37m        [39;49;00m([31margssym[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33margs[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
  1504^I[37m        [39;49;00m([31mrunrestofhook[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mrunrestofhook[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
  1505^I[37m    [39;49;00m[37m;; Since the hook is a wrapper, the loop has to be done via[39;49;00m[37m[39;49;00m$
  1506^I[37m    [39;49;00m[37m;; recursion: a given hook function will call its parameter in order to[39;49;00m[37m[39;49;00m$
  1507^I[37m    [39;49;00m[37m;; continue looping.[39;49;00m[37m[39;49;00m$
  1508^I[37m    [39;49;00m`([36mletrec[39;49;00m[37m [39;49;00m((,[31mrunrestofhook[39;49;00m[37m[39;49;00m$
  1509^I[37m               [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m(,[31mfuns[39;49;00m[37m [39;49;00m,[31mglobal[39;49;00m[37m [39;49;00m,[31margssym[39;49;00m)[37m[39;49;00m$
  1510^I[37m                 [39;49;00m[37m;; `funs' holds the functions left on the hook and `global'[39;49;00m[37m[39;49;00m$
  1511^I[37m                 [39;49;00m[37m;; holds the functions left on the global part of the hook[39;49;00m[37m[39;49;00m$
  1512^I[37m                 [39;49;00m[37m;; (in case the hook is local).[39;49;00m[37m[39;49;00m$
  1513^I[37m                 [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m,[31mfuns[39;49;00m)[37m[39;49;00m$
  1514^I[37m                     [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m,[31mfuns[39;49;00m))[37m[39;49;00m$
  1515^I[37m                         [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m,[31mrunrestofhook[39;49;00m[37m[39;49;00m$
  1516^I[37m                                  [39;49;00m([32mappend[39;49;00m[37m [39;49;00m,[31mglobal[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m,[31mfuns[39;49;00m))[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m,[31margssym[39;49;00m)[37m[39;49;00m$
  1517^I[37m                       [39;49;00m([32mapply[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m,[31mfuns[39;49;00m)[37m[39;49;00m$
  1518^I[37m                              [39;49;00m([31mapply-partially[39;49;00m[37m[39;49;00m$
  1519^I[37m                               [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m(,[31mfuns[39;49;00m[37m [39;49;00m,[31mglobal[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m,[31margssym[39;49;00m)[37m[39;49;00m$
  1520^I[37m                                 [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m,[31mrunrestofhook[39;49;00m[37m [39;49;00m,[31mfuns[39;49;00m[37m [39;49;00m,[31mglobal[39;49;00m[37m [39;49;00m,[31margssym[39;49;00m))[37m[39;49;00m$
  1521^I[37m                               [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m,[31mfuns[39;49;00m)[37m [39;49;00m,[31mglobal[39;49;00m)[37m[39;49;00m$
  1522^I[37m                              [39;49;00m,[31margssym[39;49;00m))[37m[39;49;00m$
  1523^I[37m                   [39;49;00m[37m;; Once there are no more functions on the hook, run[39;49;00m[37m[39;49;00m$
  1524^I[37m                   [39;49;00m[37m;; the original body.[39;49;00m[37m[39;49;00m$
  1525^I[37m                   [39;49;00m([32mapply[39;49;00m[37m [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m,[31margs[39;49;00m[37m [39;49;00m,@[31mbody[39;49;00m)[37m [39;49;00m,[31margssym[39;49;00m)))))[37m[39;49;00m$
  1526^I[37m       [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m,[31mrunrestofhook[39;49;00m[37m [39;49;00m,[31mhook[39;49;00m[37m[39;49;00m$
  1527^I[37m                [39;49;00m[37m;; The global part of the hook, if any.[39;49;00m[37m[39;49;00m$
  1528^I[37m                [39;49;00m,([34mif[39;49;00m[37m [39;49;00m([32msymbolp[39;49;00m[37m [39;49;00m[31mhook[39;49;00m)[37m[39;49;00m$
  1529^I[37m                     [39;49;00m`([34mif[39;49;00m[37m [39;49;00m([32mlocal-variable-p[39;49;00m[37m [39;49;00m[33m',hook[39;49;00m)[37m[39;49;00m$
  1530^I[37m                          [39;49;00m([32mdefault-value[39;49;00m[37m [39;49;00m[33m',hook[39;49;00m)))[37m[39;49;00m$
  1531^I[37m                [39;49;00m([32mlist[39;49;00m[37m [39;49;00m,@[31margs[39;49;00m)))))[37m[39;49;00m$
  1532^I[37m[39;49;00m$
  1533^I([36mdefun[39;49;00m[37m [39;49;00m[31madd-to-list[39;49;00m[37m [39;49;00m([31mlist-var[39;49;00m[37m [39;49;00m[31melement[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[32mappend[39;49;00m[37m [39;49;00m[31mcompare-fn[39;49;00m)[37m[39;49;00m$
  1534^I[37m  [39;49;00m[33m"[39;49;00m[33mAdd ELEMENT to the value of LIST-VAR if it isn't there yet.[39;49;00m$
  1535^I[33mThe test for presence of ELEMENT is done with [39;49;00m[33m`equal'[39;49;00m[33m, or with[39;49;00m$
  1536^I[33mCOMPARE-FN if that's non-nil.[39;49;00m$
  1537^I[33mIf ELEMENT is added, it is added at the beginning of the list,[39;49;00m$
  1538^I[33munless the optional argument APPEND is non-nil, in which case[39;49;00m$
  1539^I[33mELEMENT is added at the end.[39;49;00m$
  1540^I[33m[39;49;00m$
  1541^I[33mThe return value is the new value of LIST-VAR.[39;49;00m$
  1542^I[33m[39;49;00m$
  1543^I[33mThis is handy to add some elements to configuration variables,[39;49;00m$
  1544^I[33mbut please do not abuse it in Elisp code, where you are usually[39;49;00m$
  1545^I[33mbetter off using [39;49;00m[33m`push'[39;49;00m[33m or [39;49;00m[33m`cl-pushnew'[39;49;00m[33m.[39;49;00m$
  1546^I[33m[39;49;00m$
  1547^I[33mIf you want to use [39;49;00m[33m`add-to-list'[39;49;00m[33m on a variable that is not[39;49;00m$
  1548^I[33mdefined until a certain package is loaded, you should put the[39;49;00m$
  1549^I[33mcall to [39;49;00m[33m`add-to-list'[39;49;00m[33m into a hook function that will be run only[39;49;00m$
  1550^I[33mafter loading the package.  [39;49;00m[33m`eval-after-load'[39;49;00m[33m provides one way to[39;49;00m$
  1551^I[33mdo this.  In some cases other hooks, such as major mode hooks,[39;49;00m$
  1552^I[33mcan do the job.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1553^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m[39;49;00m$
  1554^I[37m   [39;49;00m([31mcompiler-macro[39;49;00m[37m[39;49;00m$
  1555^I[37m    [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([32mexp[39;49;00m)[37m[39;49;00m$
  1556^I[37m      [39;49;00m[37m;; FIXME: Something like this could be used for `set' as well.[39;49;00m[37m[39;49;00m$
  1557^I[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[33m'quote[39;49;00m[37m [39;49;00m([32mcar-safe[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m)))[37m[39;49;00m$
  1558^I[37m              [39;49;00m([32mspecial-variable-p[39;49;00m[37m [39;49;00m([31mcadr[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m))[37m[39;49;00m$
  1559^I[37m              [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([31mmacroexp-const-p[39;49;00m[37m [39;49;00m[32mappend[39;49;00m)))[37m[39;49;00m$
  1560^I[37m          [39;49;00m[32mexp[39;49;00m[37m[39;49;00m$
  1561^I[37m        [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31msym[39;49;00m[37m [39;49;00m([31mcadr[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m))[37m[39;49;00m$
  1562^I[37m               [39;49;00m([32mappend[39;49;00m[37m [39;49;00m([32meval[39;49;00m[37m [39;49;00m[32mappend[39;49;00m))[37m[39;49;00m$
  1563^I[37m               [39;49;00m([31mmsg[39;49;00m[37m [39;49;00m([32mformat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m`add-to-list'[39;49;00m[33m can't use lexical var [39;49;00m[33m`%s'[39;49;00m[33m; use [39;49;00m[33m`push'[39;49;00m[33m or [39;49;00m[33m`cl-pushnew'[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1564^I[37m                            [39;49;00m[31msym[39;49;00m))[37m[39;49;00m$
  1565^I[37m               [39;49;00m[37m;; Big ugly hack so we only output a warning during[39;49;00m[37m[39;49;00m$
  1566^I[37m               [39;49;00m[37m;; byte-compilation, and so we can use[39;49;00m[37m[39;49;00m$
  1567^I[37m               [39;49;00m[37m;; byte-compile-not-lexical-var-p to silence the warning[39;49;00m[37m[39;49;00m$
  1568^I[37m               [39;49;00m[37m;; when a defvar has been seen but not yet executed.[39;49;00m[37m[39;49;00m$
  1569^I[37m               [39;49;00m([31mwarnfun[39;49;00m[37m [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m()[37m[39;49;00m$
  1570^I[37m                          [39;49;00m[37m;; FIXME: We should also emit a warning for let-bound[39;49;00m[37m[39;49;00m$
  1571^I[37m                          [39;49;00m[37m;; variables with dynamic binding.[39;49;00m[37m[39;49;00m$
  1572^I[37m                          [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32massq[39;49;00m[37m [39;49;00m[31msym[39;49;00m[37m [39;49;00m[31mbyte-compile--lexical-environment[39;49;00m)[37m[39;49;00m$
  1573^I[37m                            [39;49;00m([31mbyte-compile-log-warning[39;49;00m[37m [39;49;00m[31mmsg[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m[36m:error[39;49;00m))))[37m[39;49;00m$
  1574^I[37m               [39;49;00m([31mcode[39;49;00m[37m[39;49;00m$
  1575^I[37m                [39;49;00m([31mmacroexp-let2[39;49;00m[37m [39;49;00m[31mmacroexp-copyable-p[39;49;00m[37m [39;49;00m[31mx[39;49;00m[37m [39;49;00m[31melement[39;49;00m[37m[39;49;00m$
  1576^I[37m                  [39;49;00m`([34mif[39;49;00m[37m [39;49;00m,([34mif[39;49;00m[37m [39;49;00m[31mcompare-fn[39;49;00m[37m[39;49;00m$
  1577^I[37m                            [39;49;00m([34mprogn[39;49;00m[37m[39;49;00m$
  1578^I[37m                              [39;49;00m([36mrequire[39;49;00m[37m [39;49;00m[33m'cl-lib[39;49;00m)[37m[39;49;00m$
  1579^I[37m                              [39;49;00m`([31mcl-member[39;49;00m[37m [39;49;00m,[31mx[39;49;00m[37m [39;49;00m,[31msym[39;49;00m[37m [39;49;00m[36m:test[39;49;00m[37m [39;49;00m,[31mcompare-fn[39;49;00m))[37m[39;49;00m$
  1580^I[37m                          [39;49;00m[37m;; For bootstrapping reasons, don't rely on[39;49;00m[37m[39;49;00m$
  1581^I[37m                          [39;49;00m[37m;; cl--compiler-macro-member for the base case.[39;49;00m[37m[39;49;00m$
  1582^I[37m                          [39;49;00m`([32mmember[39;49;00m[37m [39;49;00m,[31mx[39;49;00m[37m [39;49;00m,[31msym[39;49;00m))[37m[39;49;00m$
  1583^I[37m                       [39;49;00m,[31msym[39;49;00m[37m[39;49;00m$
  1584^I[37m                     [39;49;00m,([34mif[39;49;00m[37m [39;49;00m[32mappend[39;49;00m[37m[39;49;00m$
  1585^I[37m                          [39;49;00m`([34msetq[39;49;00m[37m [39;49;00m,[31msym[39;49;00m[37m [39;49;00m([32mappend[39;49;00m[37m [39;49;00m,[31msym[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m,[31mx[39;49;00m)))[37m[39;49;00m$
  1586^I[37m                        [39;49;00m`([36mpush[39;49;00m[37m [39;49;00m,[31mx[39;49;00m[37m [39;49;00m,[31msym[39;49;00m))))))[37m[39;49;00m$
  1587^I[37m          [39;49;00m([34mif[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([31mmacroexp--compiling-p[39;49;00m))[37m[39;49;00m$
  1588^I[37m              [39;49;00m[31mcode[39;49;00m[37m[39;49;00m$
  1589^I[37m            [39;49;00m`([34mprogn[39;49;00m[37m[39;49;00m$
  1590^I[37m               [39;49;00m([31mmacroexp--funcall-if-compiled[39;49;00m[37m [39;49;00m[33m',warnfun[39;49;00m)[37m[39;49;00m$
  1591^I[37m               [39;49;00m,[31mcode[39;49;00m)))))))[37m[39;49;00m$
  1592^I[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mcond[39;49;00m[37m[39;49;00m$
  1593^I[37m       [39;49;00m(([32mnull[39;49;00m[37m [39;49;00m[31mcompare-fn[39;49;00m)[37m[39;49;00m$
  1594^I[37m^I[39;49;00m([32mmember[39;49;00m[37m [39;49;00m[31melement[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m)))[37m[39;49;00m$
  1595^I[37m       [39;49;00m(([32meq[39;49;00m[37m [39;49;00m[31mcompare-fn[39;49;00m[37m [39;49;00m[33m'eq[39;49;00m)[37m[39;49;00m$
  1596^I[37m^I[39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[31melement[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m)))[37m[39;49;00m$
  1597^I[37m       [39;49;00m(([32meq[39;49;00m[37m [39;49;00m[31mcompare-fn[39;49;00m[37m [39;49;00m[33m'eql[39;49;00m)[37m[39;49;00m$
  1598^I[37m^I[39;49;00m([32mmemql[39;49;00m[37m [39;49;00m[31melement[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m)))[37m[39;49;00m$
  1599^I[37m       [39;49;00m([31mt[39;49;00m[37m[39;49;00m$
  1600^I[37m^I[39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mlst[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m)))[37m[39;49;00m$
  1601^I[37m^I  [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mlst[39;49;00m[37m[39;49;00m$
  1602^I[37m^I^I      [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mcompare-fn[39;49;00m[37m [39;49;00m[31melement[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mlst[39;49;00m))))[37m[39;49;00m$
  1603^I[37m^I    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mlst[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mlst[39;49;00m)))[37m[39;49;00m$
  1604^I[37m          [39;49;00m[31mlst[39;49;00m)))[37m[39;49;00m$
  1605^I[37m      [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m)[37m[39;49;00m$
  1606^I[37m    [39;49;00m([32mset[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m[37m[39;49;00m$
  1607^I[37m^I [39;49;00m([34mif[39;49;00m[37m [39;49;00m[32mappend[39;49;00m[37m[39;49;00m$
  1608^I[37m^I     [39;49;00m([32mappend[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m)[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[31melement[39;49;00m))[37m[39;49;00m$
  1609^I[37m^I   [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31melement[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m))))))[37m[39;49;00m$
  1610^I[37m[39;49;00m$
  1611^I[37m[39;49;00m$
  1612^I([36mdefun[39;49;00m[37m [39;49;00m[31madd-to-ordered-list[39;49;00m[37m [39;49;00m([31mlist-var[39;49;00m[37m [39;49;00m[31melement[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31morder[39;49;00m)[37m[39;49;00m$
  1613^I[37m  [39;49;00m[33m"[39;49;00m[33mAdd ELEMENT to the value of LIST-VAR if it isn't there yet.[39;49;00m$
  1614^I[33mThe test for presence of ELEMENT is done with [39;49;00m[33m`eq'[39;49;00m[33m.[39;49;00m$
  1615^I[33m[39;49;00m$
  1616^I[33mThe resulting list is reordered so that the elements are in the[39;49;00m$
  1617^I[33morder given by each element's numeric list order.  Elements[39;49;00m$
  1618^I[33mwithout a numeric list order are placed at the end of the list.[39;49;00m$
  1619^I[33m[39;49;00m$
  1620^I[33mIf the third optional argument ORDER is a number (integer or[39;49;00m$
  1621^I[33mfloat), set the element's list order to the given value.  If[39;49;00m$
  1622^I[33mORDER is nil or omitted, do not change the numeric order of[39;49;00m$
  1623^I[33mELEMENT.  If ORDER has any other value, remove the numeric order[39;49;00m$
  1624^I[33mof ELEMENT if it has one.[39;49;00m$
  1625^I[33m[39;49;00m$
  1626^I[33mThe list order for each element is stored in LIST-VAR's[39;49;00m$
  1627^I[33m`list-order'[39;49;00m[33m property.[39;49;00m$
  1628^I[33m[39;49;00m$
  1629^I[33mThe return value is the new value of LIST-VAR.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1630^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mordering[39;49;00m[37m [39;49;00m([32mget[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m[37m [39;49;00m[33m'list-order[39;49;00m)))[37m[39;49;00m$
  1631^I[37m    [39;49;00m([36munless[39;49;00m[37m [39;49;00m[31mordering[39;49;00m[37m[39;49;00m$
  1632^I[37m      [39;49;00m([32mput[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m[37m [39;49;00m[33m'list-order[39;49;00m[37m[39;49;00m$
  1633^I[37m           [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mordering[39;49;00m[37m [39;49;00m([32mmake-hash-table[39;49;00m[37m [39;49;00m[36m:weakness[39;49;00m[37m [39;49;00m[33m'key[39;49;00m[37m [39;49;00m[36m:test[39;49;00m[37m [39;49;00m[33m'eq[39;49;00m))))[37m[39;49;00m$
  1634^I[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31morder[39;49;00m[37m[39;49;00m$
  1635^I[37m      [39;49;00m([32mputhash[39;49;00m[37m [39;49;00m[31melement[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mnumberp[39;49;00m[37m [39;49;00m[31morder[39;49;00m)[37m [39;49;00m[31morder[39;49;00m)[37m [39;49;00m[31mordering[39;49;00m))[37m[39;49;00m$
  1636^I[37m    [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[31melement[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m))[37m[39;49;00m$
  1637^I[37m      [39;49;00m([32mset[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31melement[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m))))[37m[39;49;00m$
  1638^I[37m    [39;49;00m([32mset[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m[37m [39;49;00m([32msort[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m)[37m[39;49;00m$
  1639^I[37m^I^I^I[39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31ma[39;49;00m[37m [39;49;00m[31mb[39;49;00m)[37m[39;49;00m$
  1640^I[37m^I^I^I  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31moa[39;49;00m[37m [39;49;00m([32mgethash[39;49;00m[37m [39;49;00m[31ma[39;49;00m[37m [39;49;00m[31mordering[39;49;00m))[37m[39;49;00m$
  1641^I[37m^I^I^I^I[39;49;00m([31mob[39;49;00m[37m [39;49;00m([32mgethash[39;49;00m[37m [39;49;00m[31mb[39;49;00m[37m [39;49;00m[31mordering[39;49;00m)))[37m[39;49;00m$
  1642^I[37m^I^I^I    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31moa[39;49;00m[37m [39;49;00m[31mob[39;49;00m)[37m[39;49;00m$
  1643^I[37m^I^I^I^I[39;49;00m([32m<[39;49;00m[37m [39;49;00m[31moa[39;49;00m[37m [39;49;00m[31mob[39;49;00m)[37m[39;49;00m$
  1644^I[37m^I^I^I      [39;49;00m[31moa[39;49;00m)))))))[37m[39;49;00m$
  1645^I[37m[39;49;00m$
  1646^I([36mdefun[39;49;00m[37m [39;49;00m[31madd-to-history[39;49;00m[37m [39;49;00m([31mhistory-var[39;49;00m[37m [39;49;00m[31mnewelt[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mmaxelt[39;49;00m[37m [39;49;00m[31mkeep-all[39;49;00m)[37m[39;49;00m$
  1647^I[37m  [39;49;00m[33m"[39;49;00m[33mAdd NEWELT to the history list stored in the variable HISTORY-VAR.[39;49;00m$
  1648^I[33mReturn the new history list.[39;49;00m$
  1649^I[33mIf MAXELT is non-nil, it specifies the maximum length of the history.[39;49;00m$
  1650^I[33mOtherwise, the maximum history length is the value of the [39;49;00m[33m`history-length'[39;49;00m[33m[39;49;00m$
  1651^I[33mproperty on symbol HISTORY-VAR, if set, or the value of the [39;49;00m[33m`history-length'[39;49;00m[33m[39;49;00m$
  1652^I[33mvariable.[39;49;00m$
  1653^I[33mRemove duplicates of NEWELT if [39;49;00m[33m`history-delete-duplicates'[39;49;00m[33m is non-nil.[39;49;00m$
  1654^I[33mIf optional fourth arg KEEP-ALL is non-nil, add NEWELT to history even[39;49;00m$
  1655^I[33mif it is empty or a duplicate.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1656^I[37m  [39;49;00m([36munless[39;49;00m[37m [39;49;00m[31mmaxelt[39;49;00m[37m[39;49;00m$
  1657^I[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mmaxelt[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mget[39;49;00m[37m [39;49;00m[31mhistory-var[39;49;00m[37m [39;49;00m[33m'history-length[39;49;00m)[37m[39;49;00m$
  1658^I[37m^I^I     [39;49;00m[31mhistory-length[39;49;00m)))[37m[39;49;00m$
  1659^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mhistory[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mhistory-var[39;49;00m))[37m[39;49;00m$
  1660^I[37m^I[39;49;00m[31mtail[39;49;00m)[37m[39;49;00m$
  1661^I[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mlistp[39;49;00m[37m [39;49;00m[31mhistory[39;49;00m)[37m[39;49;00m$
  1662^I[37m^I       [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mkeep-all[39;49;00m[37m[39;49;00m$
  1663^I[37m^I^I   [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m[31mnewelt[39;49;00m))[37m[39;49;00m$
  1664^I[37m^I^I   [39;49;00m([32m>[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31mnewelt[39;49;00m)[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m$
  1665^I[37m^I       [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mkeep-all[39;49;00m[37m[39;49;00m$
  1666^I[37m^I^I   [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mequal[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mhistory[39;49;00m)[37m [39;49;00m[31mnewelt[39;49;00m))))[37m[39;49;00m$
  1667^I[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mhistory-delete-duplicates[39;49;00m[37m[39;49;00m$
  1668^I[37m^I  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mhistory[39;49;00m[37m [39;49;00m([32mdelete[39;49;00m[37m [39;49;00m[31mnewelt[39;49;00m[37m [39;49;00m[31mhistory[39;49;00m)))[37m[39;49;00m$
  1669^I[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mhistory[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mnewelt[39;49;00m[37m [39;49;00m[31mhistory[39;49;00m))[37m[39;49;00m$
  1670^I[37m      [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mintegerp[39;49;00m[37m [39;49;00m[31mmaxelt[39;49;00m)[37m[39;49;00m$
  1671^I[37m^I[39;49;00m([34mif[39;49;00m[37m [39;49;00m([32m=[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[31mmaxelt[39;49;00m)[37m[39;49;00m$
  1672^I[37m^I    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mhistory[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
  1673^I[37m^I  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([32mnthcdr[39;49;00m[37m [39;49;00m([32m1-[39;49;00m[37m [39;49;00m[31mmaxelt[39;49;00m)[37m [39;49;00m[31mhistory[39;49;00m))[37m[39;49;00m$
  1674^I[37m^I  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)[37m[39;49;00m$
  1675^I[37m^I    [39;49;00m([32msetcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)))))[37m[39;49;00m$
  1676^I[37m    [39;49;00m([32mset[39;49;00m[37m [39;49;00m[31mhistory-var[39;49;00m[37m [39;49;00m[31mhistory[39;49;00m)))[37m[39;49;00m$
  1677^I[37m[39;49;00m$
  1678^I[37m[39;49;00m[37m[39;49;00m$
  1679^I[37m;;;; Mode hooks.[39;49;00m[37m[39;49;00m$
  1680^I[37m[39;49;00m$
  1681^I([34mdefvar[39;49;00m[37m [39;49;00m[36mdelay-mode-hooks[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m$
  1682^I[37m  [39;49;00m[33m"[39;49;00m[33mIf non-nil, [39;49;00m[33m`run-mode-hooks'[39;49;00m[33m should delay running the hooks.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1683^I([34mdefvar[39;49;00m[37m [39;49;00m[31mdelayed-mode-hooks[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m$
  1684^I[37m  [39;49;00m[33m"[39;49;00m[33mList of delayed mode hooks waiting to be run.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1685^I([32mmake-variable-buffer-local[39;49;00m[37m [39;49;00m[33m'delayed-mode-hooks[39;49;00m)[37m[39;49;00m$
  1686^I([32mput[39;49;00m[37m [39;49;00m[33m'delay-mode-hooks[39;49;00m[37m [39;49;00m[33m'permanent-local[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
  1687^I[37m[39;49;00m$
  1688^I([34mdefvar[39;49;00m[37m [39;49;00m[31mchange-major-mode-after-body-hook[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m$
  1689^I[37m  [39;49;00m[33m"[39;49;00m[33mNormal hook run in major mode functions, before the mode hooks.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1690^I[37m[39;49;00m$
  1691^I([34mdefvar[39;49;00m[37m [39;49;00m[31mafter-change-major-mode-hook[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m$
  1692^I[37m  [39;49;00m[33m"[39;49;00m[33mNormal hook run at the very end of major mode functions.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1693^I[37m[39;49;00m$
  1694^I([36mdefun[39;49;00m[37m [39;49;00m[31mrun-mode-hooks[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31mhooks[39;49;00m)[37m[39;49;00m$
  1695^I[37m  [39;49;00m[33m"[39;49;00m[33mRun mode hooks [39;49;00m[33m`delayed-mode-hooks'[39;49;00m[33m and HOOKS, or delay HOOKS.[39;49;00m$
  1696^I[33mIf the variable [39;49;00m[33m`delay-mode-hooks'[39;49;00m[33m is non-nil, does not run any hooks,[39;49;00m$
  1697^I[33mjust adds the HOOKS to the list [39;49;00m[33m`delayed-mode-hooks'[39;49;00m[33m.[39;49;00m$
  1698^I[33mOtherwise, runs hooks in the sequence: [39;49;00m[33m`change-major-mode-after-body-hook'[39;49;00m[33m,[39;49;00m$
  1699^I[33m`delayed-mode-hooks'[39;49;00m[33m (in reverse order), HOOKS, and finally[39;49;00m$
  1700^I[33m`after-change-major-mode-hook'[39;49;00m[33m.  Major mode functions should use[39;49;00m$
  1701^I[33mthis instead of [39;49;00m[33m`run-hooks'[39;49;00m[33m when running their FOO-mode-hook.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1702^I[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m[36mdelay-mode-hooks[39;49;00m[37m[39;49;00m$
  1703^I[37m      [39;49;00m[37m;; Delaying case.[39;49;00m[37m[39;49;00m$
  1704^I[37m      [39;49;00m([36mdolist[39;49;00m[37m [39;49;00m([31mhook[39;49;00m[37m [39;49;00m[31mhooks[39;49;00m)[37m[39;49;00m$
  1705^I[37m^I[39;49;00m([36mpush[39;49;00m[37m [39;49;00m[31mhook[39;49;00m[37m [39;49;00m[31mdelayed-mode-hooks[39;49;00m))[37m[39;49;00m$
  1706^I[37m    [39;49;00m[37m;; Normal case, just run the hook as before plus any delayed hooks.[39;49;00m[37m[39;49;00m$
  1707^I[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mhooks[39;49;00m[37m [39;49;00m([32mnconc[39;49;00m[37m [39;49;00m([32mnreverse[39;49;00m[37m [39;49;00m[31mdelayed-mode-hooks[39;49;00m)[37m [39;49;00m[31mhooks[39;49;00m))[37m[39;49;00m$
  1708^I[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mdelayed-mode-hooks[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
  1709^I[37m    [39;49;00m([32mapply[39;49;00m[37m [39;49;00m[33m'run-hooks[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[33m'change-major-mode-after-body-hook[39;49;00m[37m [39;49;00m[31mhooks[39;49;00m))[37m[39;49;00m$
  1710^I[37m    [39;49;00m([32mrun-hooks[39;49;00m[37m [39;49;00m[33m'after-change-major-mode-hook[39;49;00m)))[37m[39;49;00m$
  1711^I[37m[39;49;00m$
  1712^I([36mdefmacro[39;49;00m[37m [39;49;00m[36mdelay-mode-hooks[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
  1713^I[37m  [39;49;00m[33m"[39;49;00m[33mExecute BODY, but delay any [39;49;00m[33m`run-mode-hooks'[39;49;00m[33m.[39;49;00m$
  1714^I[33mThese hooks will be executed by the first following call to[39;49;00m$
  1715^I[33m`run-mode-hooks'[39;49;00m[33m that occurs outside any [39;49;00m[33m`delayed-mode-hooks'[39;49;00m[33m form.[39;49;00m$
  1716^I[33mOnly affects hooks run in the current buffer.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1717^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m$
  1718^I[37m  [39;49;00m`([34mprogn[39;49;00m[37m[39;49;00m$
  1719^I[37m     [39;49;00m([32mmake-local-variable[39;49;00m[37m [39;49;00m[33m'delay-mode-hooks[39;49;00m)[37m[39;49;00m$
  1720^I[37m     [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([36mdelay-mode-hooks[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
  1721^I[37m       [39;49;00m,@[31mbody[39;49;00m)))[37m[39;49;00m$
  1722^I[37m[39;49;00m$
  1723^I[37m;; PUBLIC: find if the current mode derives from another.[39;49;00m[37m[39;49;00m$
  1724^I[37m[39;49;00m$
  1725^I([36mdefun[39;49;00m[37m [39;49;00m[31mderived-mode-p[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31mmodes[39;49;00m)[37m[39;49;00m$
  1726^I[37m  [39;49;00m[33m"[39;49;00m[33mNon-nil if the current major mode is derived from one of MODES.[39;49;00m$
  1727^I[33mUses the [39;49;00m[33m`derived-mode-parent'[39;49;00m[33m property of the symbol to trace backwards.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1728^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mparent[39;49;00m[37m [39;49;00m[31mmajor-mode[39;49;00m))[37m[39;49;00m$
  1729^I[37m    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[31mparent[39;49;00m[37m [39;49;00m[31mmodes[39;49;00m))[37m[39;49;00m$
  1730^I[37m^I^I[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mparent[39;49;00m[37m [39;49;00m([32mget[39;49;00m[37m [39;49;00m[31mparent[39;49;00m[37m [39;49;00m[33m'derived-mode-parent[39;49;00m))))[37m[39;49;00m$
  1731^I[37m    [39;49;00m[31mparent[39;49;00m))[37m[39;49;00m$
  1732^I[37m[39;49;00m[37m[39;49;00m$
  1733^I[37m;;;; Minor modes.[39;49;00m[37m[39;49;00m$
  1734^I[37m[39;49;00m$
  1735^I[37m;; If a minor mode is not defined with define-minor-mode,[39;49;00m[37m[39;49;00m$
  1736^I[37m;; add it here explicitly.[39;49;00m[37m[39;49;00m$
  1737^I[37m;; isearch-mode is deliberately excluded, since you should[39;49;00m[37m[39;49;00m$
  1738^I[37m;; not call it yourself.[39;49;00m[37m[39;49;00m$
  1739^I([34mdefvar[39;49;00m[37m [39;49;00m[31mminor-mode-list[39;49;00m[37m [39;49;00m'([31mauto-save-mode[39;49;00m[37m [39;49;00m[31mauto-fill-mode[39;49;00m[37m [39;49;00m[31mabbrev-mode[39;49;00m[37m[39;49;00m$
  1740^I[37m^I^I^I^I^I [39;49;00m[31moverwrite-mode[39;49;00m[37m [39;49;00m[31mview-mode[39;49;00m[37m[39;49;00m$
  1741^I[37m                                         [39;49;00m[31mhs-minor-mode[39;49;00m)[37m[39;49;00m$
  1742^I[37m  [39;49;00m[33m"[39;49;00m[33mList of all minor mode functions.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1743^I[37m[39;49;00m$
  1744^I([36mdefun[39;49;00m[37m [39;49;00m[31madd-minor-mode[39;49;00m[37m [39;49;00m([31mtoggle[39;49;00m[37m [39;49;00m[31mname[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m[37m [39;49;00m[31mafter[39;49;00m[37m [39;49;00m[31mtoggle-fun[39;49;00m)[37m[39;49;00m$
  1745^I[37m  [39;49;00m[33m"[39;49;00m[33mRegister a new minor mode.[39;49;00m$
  1746^I[33m[39;49;00m$
  1747^I[33mThis is an XEmacs-compatibility function.  Use [39;49;00m[33m`define-minor-mode'[39;49;00m[33m instead.[39;49;00m$
  1748^I[33m[39;49;00m$
  1749^I[33mTOGGLE is a symbol which is the name of a buffer-local variable that[39;49;00m$
  1750^I[33mis toggled on or off to say whether the minor mode is active or not.[39;49;00m$
  1751^I[33m[39;49;00m$
  1752^I[33mNAME specifies what will appear in the mode line when the minor mode[39;49;00m$
  1753^I[33mis active.  NAME should be either a string starting with a space, or a[39;49;00m$
  1754^I[33msymbol whose value is such a string.[39;49;00m$
  1755^I[33m[39;49;00m$
  1756^I[33mOptional KEYMAP is the keymap for the minor mode that will be added[39;49;00m$
  1757^I[33mto [39;49;00m[33m`minor-mode-map-alist'[39;49;00m[33m.[39;49;00m$
  1758^I[33m[39;49;00m$
  1759^I[33mOptional AFTER specifies that TOGGLE should be added after AFTER[39;49;00m$
  1760^I[33min [39;49;00m[33m`minor-mode-alist'[39;49;00m[33m.[39;49;00m$
  1761^I[33m[39;49;00m$
  1762^I[33mOptional TOGGLE-FUN is an interactive function to toggle the mode.[39;49;00m$
  1763^I[33mIt defaults to (and should by convention be) TOGGLE.[39;49;00m$
  1764^I[33m[39;49;00m$
  1765^I[33mIf TOGGLE has a non-nil [39;49;00m[33m`[39;49;00m[33m:included' property, an entry for the mode is[39;49;00m$
  1766^I[33mincluded in the mode-line minor mode menu.[39;49;00m$
  1767^I[33mIf TOGGLE has a [39;49;00m[33m`[39;49;00m[33m:menu-tag', that is used for the menu item's label.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1768^I[37m  [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[31mtoggle[39;49;00m[37m [39;49;00m[31mminor-mode-list[39;49;00m)[37m[39;49;00m$
  1769^I[37m    [39;49;00m([36mpush[39;49;00m[37m [39;49;00m[31mtoggle[39;49;00m[37m [39;49;00m[31mminor-mode-list[39;49;00m))[37m[39;49;00m$
  1770^I[37m[39;49;00m$
  1771^I[37m  [39;49;00m([36munless[39;49;00m[37m [39;49;00m[31mtoggle-fun[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mtoggle-fun[39;49;00m[37m [39;49;00m[31mtoggle[39;49;00m))[37m[39;49;00m$
  1772^I[37m  [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mtoggle-fun[39;49;00m[37m [39;49;00m[31mtoggle[39;49;00m)[37m[39;49;00m$
  1773^I[37m    [39;49;00m([32mput[39;49;00m[37m [39;49;00m[31mtoggle[39;49;00m[37m [39;49;00m[36m:minor-mode-function[39;49;00m[37m [39;49;00m[31mtoggle-fun[39;49;00m))[37m[39;49;00m$
  1774^I[37m  [39;49;00m[37m;; Add the name to the minor-mode-alist.[39;49;00m[37m[39;49;00m$
  1775^I[37m  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31mname[39;49;00m[37m[39;49;00m$
  1776^I[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mexisting[39;49;00m[37m [39;49;00m([32massq[39;49;00m[37m [39;49;00m[31mtoggle[39;49;00m[37m [39;49;00m[31mminor-mode-alist[39;49;00m)))[37m[39;49;00m$
  1777^I[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mexisting[39;49;00m[37m[39;49;00m$
  1778^I[37m^I  [39;49;00m([32msetcdr[39;49;00m[37m [39;49;00m[31mexisting[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[31mname[39;49;00m))[37m[39;49;00m$
  1779^I[37m^I[39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtail[39;49;00m[37m [39;49;00m[31mminor-mode-alist[39;49;00m)[37m [39;49;00m[31mfound[39;49;00m)[37m[39;49;00m$
  1780^I[37m^I  [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m[31mfound[39;49;00m))[37m[39;49;00m$
  1781^I[37m^I    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mafter[39;49;00m[37m [39;49;00m([31mcaar[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))[37m[39;49;00m$
  1782^I[37m^I^I[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mfound[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)[37m[39;49;00m$
  1783^I[37m^I      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))))[37m[39;49;00m$
  1784^I[37m^I  [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mfound[39;49;00m[37m[39;49;00m$
  1785^I[37m^I      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mrest[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mfound[39;49;00m)))[37m[39;49;00m$
  1786^I[37m^I^I[39;49;00m([32msetcdr[39;49;00m[37m [39;49;00m[31mfound[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
  1787^I[37m^I^I[39;49;00m([32mnconc[39;49;00m[37m [39;49;00m[31mfound[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[31mtoggle[39;49;00m[37m [39;49;00m[31mname[39;49;00m))[37m [39;49;00m[31mrest[39;49;00m))[37m[39;49;00m$
  1788^I[37m^I    [39;49;00m([36mpush[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[31mtoggle[39;49;00m[37m [39;49;00m[31mname[39;49;00m)[37m [39;49;00m[31mminor-mode-alist[39;49;00m))))))[37m[39;49;00m$
  1789^I[37m  [39;49;00m[37m;; Add the toggle to the minor-modes menu if requested.[39;49;00m[37m[39;49;00m$
  1790^I[37m  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mget[39;49;00m[37m [39;49;00m[31mtoggle[39;49;00m[37m [39;49;00m[36m:included[39;49;00m)[37m[39;49;00m$
  1791^I[37m    [39;49;00m([32mdefine-key[39;49;00m[37m [39;49;00m[31mmode-line-mode-menu[39;49;00m[37m[39;49;00m$
  1792^I[37m      [39;49;00m([32mvector[39;49;00m[37m [39;49;00m[31mtoggle[39;49;00m)[37m[39;49;00m$
  1793^I[37m      [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'menu-item[39;49;00m[37m[39;49;00m$
  1794^I[37m^I    [39;49;00m([32mconcat[39;49;00m[37m[39;49;00m$
  1795^I[37m^I     [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mget[39;49;00m[37m [39;49;00m[31mtoggle[39;49;00m[37m [39;49;00m[36m:menu-tag[39;49;00m)[37m[39;49;00m$
  1796^I[37m^I^I [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m[31mname[39;49;00m)[37m [39;49;00m[31mname[39;49;00m[37m [39;49;00m([32msymbol-name[39;49;00m[37m [39;49;00m[31mtoggle[39;49;00m)))[37m[39;49;00m$
  1797^I[37m^I     [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mmode-name[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32msymbolp[39;49;00m[37m [39;49;00m[31mname[39;49;00m)[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mname[39;49;00m))))[37m[39;49;00m$
  1798^I[37m^I       [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m[31mmode-name[39;49;00m)[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m[^ ]+[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mmode-name[39;49;00m))[37m[39;49;00m$
  1799^I[37m^I^I   [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m ([39;49;00m[33m"[39;49;00m[37m [39;49;00m([31mmatch-string[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[31mmode-name[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m)[39;49;00m[33m"[39;49;00m))))[37m[39;49;00m$
  1800^I[37m^I    [39;49;00m[31mtoggle-fun[39;49;00m[37m[39;49;00m$
  1801^I[37m^I    [39;49;00m[36m:button[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[36m:toggle[39;49;00m[37m [39;49;00m[31mtoggle[39;49;00m))))[37m[39;49;00m$
  1802^I[37m[39;49;00m$
  1803^I[37m  [39;49;00m[37m;; Add the map to the minor-mode-map-alist.[39;49;00m[37m[39;49;00m$
  1804^I[37m  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m[37m[39;49;00m$
  1805^I[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mexisting[39;49;00m[37m [39;49;00m([32massq[39;49;00m[37m [39;49;00m[31mtoggle[39;49;00m[37m [39;49;00m[31mminor-mode-map-alist[39;49;00m)))[37m[39;49;00m$
  1806^I[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mexisting[39;49;00m[37m[39;49;00m$
  1807^I[37m^I  [39;49;00m([32msetcdr[39;49;00m[37m [39;49;00m[31mexisting[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m)[37m[39;49;00m$
  1808^I[37m^I[39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtail[39;49;00m[37m [39;49;00m[31mminor-mode-map-alist[39;49;00m)[37m [39;49;00m[31mfound[39;49;00m)[37m[39;49;00m$
  1809^I[37m^I  [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m[31mfound[39;49;00m))[37m[39;49;00m$
  1810^I[37m^I    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mafter[39;49;00m[37m [39;49;00m([31mcaar[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))[37m[39;49;00m$
  1811^I[37m^I^I[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mfound[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)[37m[39;49;00m$
  1812^I[37m^I      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))))[37m[39;49;00m$
  1813^I[37m^I  [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mfound[39;49;00m[37m[39;49;00m$
  1814^I[37m^I      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mrest[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mfound[39;49;00m)))[37m[39;49;00m$
  1815^I[37m^I^I[39;49;00m([32msetcdr[39;49;00m[37m [39;49;00m[31mfound[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
  1816^I[37m^I^I[39;49;00m([32mnconc[39;49;00m[37m [39;49;00m[31mfound[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mtoggle[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m))[37m [39;49;00m[31mrest[39;49;00m))[37m[39;49;00m$
  1817^I[37m^I    [39;49;00m([36mpush[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mtoggle[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m)[37m [39;49;00m[31mminor-mode-map-alist[39;49;00m)))))))[37m[39;49;00m$
  1818^I[37m[39;49;00m[37m[39;49;00m$
  1819^I[37m;;;; Load history[39;49;00m[37m[39;49;00m$
  1820^I[37m[39;49;00m$
  1821^I([36mdefsubst[39;49;00m[37m [39;49;00m[31mautoloadp[39;49;00m[37m [39;49;00m([31mobject[39;49;00m)[37m[39;49;00m$
  1822^I[37m  [39;49;00m[33m"[39;49;00m[33mNon-nil if OBJECT is an autoload.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1823^I[37m  [39;49;00m([32meq[39;49;00m[37m [39;49;00m[33m'autoload[39;49;00m[37m [39;49;00m([32mcar-safe[39;49;00m[37m [39;49;00m[31mobject[39;49;00m)))[37m[39;49;00m$
  1824^I[37m[39;49;00m$
  1825^I[37m;; (defun autoload-type (object)[39;49;00m[37m[39;49;00m$
  1826^I[37m;;   "Returns the type of OBJECT or `function' or `command' if the type is nil.[39;49;00m[37m[39;49;00m$
  1827^I[37m;; OBJECT should be an autoload object."[39;49;00m[37m[39;49;00m$
  1828^I[37m;;   (when (autoloadp object)[39;49;00m[37m[39;49;00m$
  1829^I[37m;;     (let ((type (nth 3 object)))[39;49;00m[37m[39;49;00m$
  1830^I[37m;;       (cond ((null type) (if (nth 2 object) 'command 'function))[39;49;00m[37m[39;49;00m$
  1831^I[37m;;             ((eq 'keymap t) 'macro)[39;49;00m[37m[39;49;00m$
  1832^I[37m;;             (type)))))[39;49;00m[37m[39;49;00m$
  1833^I[37m[39;49;00m$
  1834^I[37m;; (defalias 'autoload-file #'cadr[39;49;00m[37m[39;49;00m$
  1835^I[37m;;   "Return the name of the file from which AUTOLOAD will be loaded.[39;49;00m[37m[39;49;00m$
  1836^I[37m;; \n\(fn AUTOLOAD)")[39;49;00m[37m[39;49;00m$
  1837^I[37m[39;49;00m$
  1838^I([36mdefun[39;49;00m[37m [39;49;00m[31msymbol-file[39;49;00m[37m [39;49;00m([31msymbol[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mtype[39;49;00m)[37m[39;49;00m$
  1839^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn the name of the file that defined SYMBOL.[39;49;00m$
  1840^I[33mThe value is normally an absolute file name.  It can also be nil,[39;49;00m$
  1841^I[33mif the definition is not associated with any file.  If SYMBOL[39;49;00m$
  1842^I[33mspecifies an autoloaded function, the value can be a relative[39;49;00m$
  1843^I[33mfile name without extension.[39;49;00m$
  1844^I[33m[39;49;00m$
  1845^I[33mIf TYPE is nil, then any kind of definition is acceptable.  If[39;49;00m$
  1846^I[33mTYPE is [39;49;00m[33m`defun'[39;49;00m[33m, [39;49;00m[33m`defvar'[39;49;00m[33m, or [39;49;00m[33m`defface'[39;49;00m[33m, that specifies function[39;49;00m$
  1847^I[33mdefinition, variable definition, or face definition only.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1848^I[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[31mtype[39;49;00m)[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mtype[39;49;00m[37m [39;49;00m[33m'defun[39;49;00m))[37m[39;49;00m$
  1849^I[37m^I   [39;49;00m([32msymbolp[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m)[37m[39;49;00m$
  1850^I[37m^I   [39;49;00m([31mautoloadp[39;49;00m[37m [39;49;00m([32msymbol-function[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m)))[37m[39;49;00m$
  1851^I[37m      [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m([32msymbol-function[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m))[37m[39;49;00m$
  1852^I[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mfiles[39;49;00m[37m [39;49;00m[31mload-history[39;49;00m)[37m[39;49;00m$
  1853^I[37m^I  [39;49;00m[31mfile[39;49;00m)[37m[39;49;00m$
  1854^I[37m      [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m[31mfiles[39;49;00m[37m[39;49;00m$
  1855^I[37m^I[39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mtype[39;49;00m[37m[39;49;00m$
  1856^I[37m^I^I[39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mtype[39;49;00m[37m [39;49;00m[33m'defvar[39;49;00m)[37m[39;49;00m$
  1857^I[37m^I^I    [39;49;00m[37m;; Variables are present just as their names.[39;49;00m[37m[39;49;00m$
  1858^I[37m^I^I    [39;49;00m([32mmember[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mfiles[39;49;00m)))[37m[39;49;00m$
  1859^I[37m^I^I  [39;49;00m[37m;; Other types are represented as (TYPE . NAME).[39;49;00m[37m[39;49;00m$
  1860^I[37m^I^I  [39;49;00m([32mmember[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mtype[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m)[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mfiles[39;49;00m))))[37m[39;49;00m$
  1861^I[37m^I      [39;49;00m[37m;; We accept all types, so look for variable def[39;49;00m[37m[39;49;00m$
  1862^I[37m^I      [39;49;00m[37m;; and then for any other kind.[39;49;00m[37m[39;49;00m$
  1863^I[37m^I      [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mmember[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mfiles[39;49;00m)))[37m[39;49;00m$
  1864^I[37m^I^I  [39;49;00m([32mrassq[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mfiles[39;49;00m)))))[37m[39;49;00m$
  1865^I[37m^I    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mfile[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mfiles[39;49;00m))[37m [39;49;00m[31mfiles[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m$
  1866^I[37m^I[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mfiles[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mfiles[39;49;00m)))[37m[39;49;00m$
  1867^I[37m      [39;49;00m[31mfile[39;49;00m)))[37m[39;49;00m$
  1868^I[37m[39;49;00m$
  1869^I([36mdefun[39;49;00m[37m [39;49;00m[31mlocate-library[39;49;00m[37m [39;49;00m([31mlibrary[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mnosuffix[39;49;00m[37m [39;49;00m[31mpath[39;49;00m[37m [39;49;00m[31minteractive-call[39;49;00m)[37m[39;49;00m$
  1870^I[37m  [39;49;00m[33m"[39;49;00m[33mShow the precise file name of Emacs library LIBRARY.[39;49;00m$
  1871^I[33mLIBRARY should be a relative file name of the library, a string.[39;49;00m$
  1872^I[33mIt can omit the suffix (a.k.a. file-name extension) if NOSUFFIX is[39;49;00m$
  1873^I[33mnil (which is the default, see below).[39;49;00m$
  1874^I[33mThis command searches the directories in [39;49;00m[33m`load-path'[39;49;00m[33m like [39;49;00m[33m`[39;49;00m[33m\\[39;49;00m[33m[load-library]'[39;49;00m$
  1875^I[33mto find the file that [39;49;00m[33m`[39;49;00m[33m\\[39;49;00m[33m[load-library] RET LIBRARY RET' would load.[39;49;00m$
  1876^I[33mOptional second arg NOSUFFIX non-nil means don't add suffixes [39;49;00m[33m`load-suffixes'[39;49;00m[33m[39;49;00m$
  1877^I[33mto the specified name LIBRARY.[39;49;00m$
  1878^I[33m[39;49;00m$
  1879^I[33mIf the optional third arg PATH is specified, that list of directories[39;49;00m$
  1880^I[33mis used instead of [39;49;00m[33m`load-path'[39;49;00m[33m.[39;49;00m$
  1881^I[33m[39;49;00m$
  1882^I[33mWhen called from a program, the file name is normally returned as a[39;49;00m$
  1883^I[33mstring.  When run interactively, the argument INTERACTIVE-CALL is t,[39;49;00m$
  1884^I[33mand the file name is displayed in the echo area.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1885^I[37m  [39;49;00m([34minteractive[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m([32mcompleting-read[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mLocate library: [39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1886^I[37m^I^I^I^I      [39;49;00m([31mapply-partially[39;49;00m[37m[39;49;00m$
  1887^I[37m                                       [39;49;00m[33m'locate-file-completion-table[39;49;00m[37m[39;49;00m$
  1888^I[37m                                       [39;49;00m[31mload-path[39;49;00m[37m [39;49;00m([32mget-load-suffixes[39;49;00m)))[37m[39;49;00m$
  1889^I[37m^I^I     [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m$
  1890^I[37m^I^I     [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
  1891^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mfile[39;49;00m[37m [39;49;00m([31mlocate-file[39;49;00m[37m [39;49;00m[31mlibrary[39;49;00m[37m[39;49;00m$
  1892^I[37m^I^I^I   [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mpath[39;49;00m[37m [39;49;00m[31mload-path[39;49;00m)[37m[39;49;00m$
  1893^I[37m^I^I^I   [39;49;00m([32mappend[39;49;00m[37m [39;49;00m([36munless[39;49;00m[37m [39;49;00m[31mnosuffix[39;49;00m[37m [39;49;00m([32mget-load-suffixes[39;49;00m))[37m[39;49;00m$
  1894^I[37m^I^I^I^I   [39;49;00m[31mload-file-rep-suffixes[39;49;00m))))[37m[39;49;00m$
  1895^I[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31minteractive-call[39;49;00m[37m[39;49;00m$
  1896^I[37m^I[39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mfile[39;49;00m[37m[39;49;00m$
  1897^I[37m^I    [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mLibrary is file %s[39;49;00m[33m"[39;49;00m[37m [39;49;00m([31mabbreviate-file-name[39;49;00m[37m [39;49;00m[31mfile[39;49;00m))[37m[39;49;00m$
  1898^I[37m^I  [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mNo library %s in search path[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mlibrary[39;49;00m)))[37m[39;49;00m$
  1899^I[37m    [39;49;00m[31mfile[39;49;00m))[37m[39;49;00m$
  1900^I[37m[39;49;00m$
  1901^I[37m[39;49;00m[37m[39;49;00m$
  1902^I[37m;;;; Process stuff.[39;49;00m[37m[39;49;00m$
  1903^I[37m[39;49;00m$
  1904^I([36mdefun[39;49;00m[37m [39;49;00m[31mprocess-lines[39;49;00m[37m [39;49;00m([31mprogram[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31margs[39;49;00m)[37m[39;49;00m$
  1905^I[37m  [39;49;00m[33m"[39;49;00m[33mExecute PROGRAM with ARGS, returning its output as a list of lines.[39;49;00m$
  1906^I[33mSignal an error if the program returns with a non-zero exit status.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1907^I[37m  [39;49;00m([36mwith-temp-buffer[39;49;00m[37m[39;49;00m$
  1908^I[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mstatus[39;49;00m[37m [39;49;00m([32mapply[39;49;00m[37m [39;49;00m[33m'call-process[39;49;00m[37m [39;49;00m[31mprogram[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m([32mcurrent-buffer[39;49;00m)[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31margs[39;49;00m)))[37m[39;49;00m$
  1909^I[37m      [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mstatus[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1910^I[37m^I[39;49;00m([36merror[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m%s exited with status %s[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mprogram[39;49;00m[37m [39;49;00m[31mstatus[39;49;00m))[37m[39;49;00m$
  1911^I[37m      [39;49;00m([32mgoto-char[39;49;00m[37m [39;49;00m([32mpoint-min[39;49;00m))[37m[39;49;00m$
  1912^I[37m      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m([31mlines[39;49;00m)[37m[39;49;00m$
  1913^I[37m^I[39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32meobp[39;49;00m))[37m[39;49;00m$
  1914^I[37m^I  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mlines[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m([32mbuffer-substring-no-properties[39;49;00m[37m[39;49;00m$
  1915^I[37m^I^I^I     [39;49;00m([32mline-beginning-position[39;49;00m)[37m[39;49;00m$
  1916^I[37m^I^I^I     [39;49;00m([32mline-end-position[39;49;00m))[37m[39;49;00m$
  1917^I[37m^I^I^I    [39;49;00m[31mlines[39;49;00m))[37m[39;49;00m$
  1918^I[37m^I  [39;49;00m([32mforward-line[39;49;00m[37m [39;49;00m[34m1[39;49;00m))[37m[39;49;00m$
  1919^I[37m^I[39;49;00m([32mnreverse[39;49;00m[37m [39;49;00m[31mlines[39;49;00m)))))[37m[39;49;00m$
  1920^I[37m[39;49;00m$
  1921^I([36mdefun[39;49;00m[37m [39;49;00m[31mprocess-live-p[39;49;00m[37m [39;49;00m([31mprocess[39;49;00m)[37m[39;49;00m$
  1922^I[37m  [39;49;00m[33m"[39;49;00m[33mReturns non-nil if PROCESS is alive.[39;49;00m$
  1923^I[33mA process is considered alive if its status is [39;49;00m[33m`run'[39;49;00m[33m, [39;49;00m[33m`open'[39;49;00m[33m,[39;49;00m$
  1924^I[33m`listen'[39;49;00m[33m, [39;49;00m[33m`connect'[39;49;00m[33m or [39;49;00m[33m`stop'[39;49;00m[33m.  Value is nil if PROCESS is not a[39;49;00m$
  1925^I[33mprocess.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1926^I[37m  [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mprocessp[39;49;00m[37m [39;49;00m[31mprocess[39;49;00m)[37m[39;49;00m$
  1927^I[37m       [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m([32mprocess-status[39;49;00m[37m [39;49;00m[31mprocess[39;49;00m)[37m[39;49;00m$
  1928^I[37m^I     [39;49;00m'([31mrun[39;49;00m[37m [39;49;00m[31mopen[39;49;00m[37m [39;49;00m[31mlisten[39;49;00m[37m [39;49;00m[31mconnect[39;49;00m[37m [39;49;00m[31mstop[39;49;00m))))[37m[39;49;00m$
  1929^I[37m[39;49;00m$
  1930^I[37m;; compatibility[39;49;00m[37m[39;49;00m$
  1931^I[37m[39;49;00m$
  1932^I([31mmake-obsolete[39;49;00m[37m[39;49;00m$
  1933^I[37m [39;49;00m[33m'process-kill-without-query[39;49;00m[37m[39;49;00m$
  1934^I[37m [39;49;00m[33m"[39;49;00m[33muse [39;49;00m[33m`process-query-on-exit-flag'[39;49;00m[33m or [39;49;00m[33m`set-process-query-on-exit-flag'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1935^I[37m [39;49;00m[33m"[39;49;00m[33m22.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  1936^I([36mdefun[39;49;00m[37m [39;49;00m[31mprocess-kill-without-query[39;49;00m[37m [39;49;00m([31mprocess[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31m_flag[39;49;00m)[37m[39;49;00m$
  1937^I[37m  [39;49;00m[33m"[39;49;00m[33mSay no query needed if PROCESS is running when Emacs is exited.[39;49;00m$
  1938^I[33mOptional second argument if non-nil says to require a query.[39;49;00m$
  1939^I[33mValue is t if a query was formerly required.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1940^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mold[39;49;00m[37m [39;49;00m([32mprocess-query-on-exit-flag[39;49;00m[37m [39;49;00m[31mprocess[39;49;00m)))[37m[39;49;00m$
  1941^I[37m    [39;49;00m([32mset-process-query-on-exit-flag[39;49;00m[37m [39;49;00m[31mprocess[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
  1942^I[37m    [39;49;00m[31mold[39;49;00m))[37m[39;49;00m$
  1943^I[37m[39;49;00m$
  1944^I([36mdefun[39;49;00m[37m [39;49;00m[31mprocess-kill-buffer-query-function[39;49;00m[37m [39;49;00m()[37m[39;49;00m$
  1945^I[37m  [39;49;00m[33m"[39;49;00m[33mAsk before killing a buffer that has a running process.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1946^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mprocess[39;49;00m[37m [39;49;00m([32mget-buffer-process[39;49;00m[37m [39;49;00m([32mcurrent-buffer[39;49;00m))))[37m[39;49;00m$
  1947^I[37m    [39;49;00m([34mor[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m[31mprocess[39;49;00m)[37m[39;49;00m$
  1948^I[37m        [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m([32mprocess-status[39;49;00m[37m [39;49;00m[31mprocess[39;49;00m)[37m [39;49;00m'([31mrun[39;49;00m[37m [39;49;00m[31mstop[39;49;00m[37m [39;49;00m[31mopen[39;49;00m[37m [39;49;00m[31mlisten[39;49;00m)))[37m[39;49;00m$
  1949^I[37m        [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mprocess-query-on-exit-flag[39;49;00m[37m [39;49;00m[31mprocess[39;49;00m))[37m[39;49;00m$
  1950^I[37m        [39;49;00m([32myes-or-no-p[39;49;00m[37m[39;49;00m$
  1951^I[37m^I [39;49;00m([32mformat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mBuffer %S has a running process; kill it? [39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1952^I[37m^I^I [39;49;00m([32mbuffer-name[39;49;00m[37m [39;49;00m([32mcurrent-buffer[39;49;00m)))))))[37m[39;49;00m$
  1953^I[37m[39;49;00m$
  1954^I([31madd-hook[39;49;00m[37m [39;49;00m[33m'kill-buffer-query-functions[39;49;00m[37m [39;49;00m[33m'process-kill-buffer-query-function[39;49;00m)[37m[39;49;00m$
  1955^I[37m[39;49;00m$
  1956^I[37m;; process plist management[39;49;00m[37m[39;49;00m$
  1957^I[37m[39;49;00m$
  1958^I([36mdefun[39;49;00m[37m [39;49;00m[31mprocess-get[39;49;00m[37m [39;49;00m([31mprocess[39;49;00m[37m [39;49;00m[31mpropname[39;49;00m)[37m[39;49;00m$
  1959^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn the value of PROCESS' PROPNAME property.[39;49;00m$
  1960^I[33mThis is the last value stored with [39;49;00m[33m`[39;49;00m[33m(process-put PROCESS PROPNAME VALUE)'.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1961^I[37m  [39;49;00m([32mplist-get[39;49;00m[37m [39;49;00m([32mprocess-plist[39;49;00m[37m [39;49;00m[31mprocess[39;49;00m)[37m [39;49;00m[31mpropname[39;49;00m))[37m[39;49;00m$
  1962^I[37m[39;49;00m$
  1963^I([36mdefun[39;49;00m[37m [39;49;00m[31mprocess-put[39;49;00m[37m [39;49;00m([31mprocess[39;49;00m[37m [39;49;00m[31mpropname[39;49;00m[37m [39;49;00m[31mvalue[39;49;00m)[37m[39;49;00m$
  1964^I[37m  [39;49;00m[33m"[39;49;00m[33mChange PROCESS' PROPNAME property to VALUE.[39;49;00m$
  1965^I[33mIt can be retrieved with [39;49;00m[33m`[39;49;00m[33m(process-get PROCESS PROPNAME)'.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1966^I[37m  [39;49;00m([32mset-process-plist[39;49;00m[37m [39;49;00m[31mprocess[39;49;00m[37m[39;49;00m$
  1967^I[37m^I^I     [39;49;00m([32mplist-put[39;49;00m[37m [39;49;00m([32mprocess-plist[39;49;00m[37m [39;49;00m[31mprocess[39;49;00m)[37m [39;49;00m[31mpropname[39;49;00m[37m [39;49;00m[31mvalue[39;49;00m)))[37m[39;49;00m$
  1968^I[37m[39;49;00m$
  1969^I[37m[39;49;00m[37m[39;49;00m$
  1970^I[37m;;;; Input and display facilities.[39;49;00m[37m[39;49;00m$
  1971^I[37m[39;49;00m$
  1972^I([34mdefconst[39;49;00m[37m [39;49;00m[31mread-key-empty-map[39;49;00m[37m [39;49;00m([32mmake-sparse-keymap[39;49;00m))[37m[39;49;00m$
  1973^I[37m[39;49;00m$
  1974^I([34mdefvar[39;49;00m[37m [39;49;00m[31mread-key-delay[39;49;00m[37m [39;49;00m[34m0.01[39;49;00m)[37m [39;49;00m[37m;Fast enough for 100Hz repeat rate, hopefully.[39;49;00m[37m[39;49;00m$
  1975^I[37m[39;49;00m$
  1976^I([36mdefun[39;49;00m[37m [39;49;00m[31mread-key[39;49;00m[37m [39;49;00m([34m&optional[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m)[37m[39;49;00m$
  1977^I[37m  [39;49;00m[33m"[39;49;00m[33mRead a key from the keyboard.[39;49;00m$
  1978^I[33mContrary to [39;49;00m[33m`read-event'[39;49;00m[33m this will not return a raw event but instead will[39;49;00m$
  1979^I[33mobey the input decoding and translations usually done by [39;49;00m[33m`read-key-sequence'[39;49;00m[33m.[39;49;00m$
  1980^I[33mSo escape sequences and keyboard encoding are taken into account.[39;49;00m$
  1981^I[33mWhen there's an ambiguity because the key looks like the prefix of[39;49;00m$
  1982^I[33msome sort of escape sequence, the ambiguity is resolved via [39;49;00m[33m`read-key-delay'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1983^I[37m  [39;49;00m[37m;; This overriding-terminal-local-map binding also happens to[39;49;00m[37m[39;49;00m$
  1984^I[37m  [39;49;00m[37m;; disable quail's input methods, so although read-key-sequence[39;49;00m[37m[39;49;00m$
  1985^I[37m  [39;49;00m[37m;; always inherits the input method, in practice read-key does not[39;49;00m[37m[39;49;00m$
  1986^I[37m  [39;49;00m[37m;; inherit the input method (at least not if it's based on quail).[39;49;00m[37m[39;49;00m$
  1987^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31moverriding-terminal-local-map[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
  1988^I[37m^I[39;49;00m([31moverriding-local-map[39;49;00m[37m [39;49;00m[31mread-key-empty-map[39;49;00m)[37m[39;49;00m$
  1989^I[37m        [39;49;00m([31mecho-keystrokes[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1990^I[37m^I[39;49;00m([31mold-global-map[39;49;00m[37m [39;49;00m([32mcurrent-global-map[39;49;00m))[37m[39;49;00m$
  1991^I[37m        [39;49;00m([31mtimer[39;49;00m[37m [39;49;00m([31mrun-with-idle-timer[39;49;00m[37m[39;49;00m$
  1992^I[37m                [39;49;00m[37m;; Wait long enough that Emacs has the time to receive and[39;49;00m[37m[39;49;00m$
  1993^I[37m                [39;49;00m[37m;; process all the raw events associated with the single-key.[39;49;00m[37m[39;49;00m$
  1994^I[37m                [39;49;00m[37m;; But don't wait too long, or the user may find the delay[39;49;00m[37m[39;49;00m$
  1995^I[37m                [39;49;00m[37m;; annoying (or keep hitting more keys which may then get[39;49;00m[37m[39;49;00m$
  1996^I[37m                [39;49;00m[37m;; lost or misinterpreted).[39;49;00m[37m[39;49;00m$
  1997^I[37m                [39;49;00m[37m;; This is only relevant for keys which Emacs perceives as[39;49;00m[37m[39;49;00m$
  1998^I[37m                [39;49;00m[37m;; "prefixes", such as C-x (because of the C-x 8 map in[39;49;00m[37m[39;49;00m$
  1999^I[37m                [39;49;00m[37m;; key-translate-table and the C-x @ map in function-key-map)[39;49;00m[37m[39;49;00m$
  2000^I[37m                [39;49;00m[37m;; or ESC (because of terminal escape sequences in[39;49;00m[37m[39;49;00m$
  2001^I[37m                [39;49;00m[37m;; input-decode-map).[39;49;00m[37m[39;49;00m$
  2002^I[37m                [39;49;00m[31mread-key-delay[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m[39;49;00m$
  2003^I[37m                [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m()[37m[39;49;00m$
  2004^I[37m                  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mkeys[39;49;00m[37m [39;49;00m([32mthis-command-keys-vector[39;49;00m)))[37m[39;49;00m$
  2005^I[37m                    [39;49;00m([36munless[39;49;00m[37m [39;49;00m([31mzerop[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31mkeys[39;49;00m))[37m[39;49;00m$
  2006^I[37m                      [39;49;00m[37m;; `keys' is non-empty, so the user has hit at least[39;49;00m[37m[39;49;00m$
  2007^I[37m                      [39;49;00m[37m;; one key; there's no point waiting any longer, even[39;49;00m[37m[39;49;00m$
  2008^I[37m                      [39;49;00m[37m;; though read-key-sequence thinks we should wait[39;49;00m[37m[39;49;00m$
  2009^I[37m                      [39;49;00m[37m;; for more input to decide how to interpret the[39;49;00m[37m[39;49;00m$
  2010^I[37m                      [39;49;00m[37m;; current input.[39;49;00m[37m[39;49;00m$
  2011^I[37m                      [39;49;00m([36mthrow[39;49;00m[37m [39;49;00m[33m'read-key[39;49;00m[37m [39;49;00m[31mkeys[39;49;00m)))))))[37m[39;49;00m$
  2012^I[37m    [39;49;00m([34munwind-protect[39;49;00m[37m[39;49;00m$
  2013^I[37m        [39;49;00m([34mprogn[39;49;00m[37m[39;49;00m$
  2014^I[37m^I  [39;49;00m([32muse-global-map[39;49;00m[37m[39;49;00m$
  2015^I[37m           [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mmap[39;49;00m[37m [39;49;00m([32mmake-sparse-keymap[39;49;00m)))[37m[39;49;00m$
  2016^I[37m             [39;49;00m[37m;; Don't hide the menu-bar and tool-bar entries.[39;49;00m[37m[39;49;00m$
  2017^I[37m             [39;49;00m([32mdefine-key[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m[[31mmenu-bar[39;49;00m][37m [39;49;00m([32mlookup-key[39;49;00m[37m [39;49;00m[31mglobal-map[39;49;00m[37m [39;49;00m[[31mmenu-bar[39;49;00m]))[37m[39;49;00m$
  2018^I[37m             [39;49;00m([32mdefine-key[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m[[31mtool-bar[39;49;00m][37m[39;49;00m$
  2019^I[37m^I       [39;49;00m[37m;; This hack avoids evaluating the :filter (Bug#9922).[39;49;00m[37m[39;49;00m$
  2020^I[37m^I       [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m([32massq[39;49;00m[37m [39;49;00m[33m'tool-bar[39;49;00m[37m [39;49;00m[31mglobal-map[39;49;00m))[37m[39;49;00m$
  2021^I[37m^I^I   [39;49;00m([32mlookup-key[39;49;00m[37m [39;49;00m[31mglobal-map[39;49;00m[37m [39;49;00m[[31mtool-bar[39;49;00m])))[37m[39;49;00m$
  2022^I[37m             [39;49;00m[31mmap[39;49;00m))[37m[39;49;00m$
  2023^I[37m          [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mkeys[39;49;00m[37m[39;49;00m$
  2024^I[37m                  [39;49;00m([34mcatch[39;49;00m[37m [39;49;00m[33m'read-key[39;49;00m[37m [39;49;00m([32mread-key-sequence-vector[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mt[39;49;00m)))[37m[39;49;00m$
  2025^I[37m                 [39;49;00m([31mkey[39;49;00m[37m [39;49;00m([32maref[39;49;00m[37m [39;49;00m[31mkeys[39;49;00m[37m [39;49;00m[34m0[39;49;00m)))[37m[39;49;00m$
  2026^I[37m            [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31mkeys[39;49;00m)[37m [39;49;00m[34m1[39;49;00m)[37m[39;49;00m$
  2027^I[37m                     [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m'([31mmode-line[39;49;00m[37m [39;49;00m[31mheader-line[39;49;00m[37m[39;49;00m$
  2028^I[37m                                 [39;49;00m[31mleft-fringe[39;49;00m[37m [39;49;00m[31mright-fringe[39;49;00m)))[37m[39;49;00m$
  2029^I[37m                [39;49;00m([32maref[39;49;00m[37m [39;49;00m[31mkeys[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m[39;49;00m$
  2030^I[37m              [39;49;00m[31mkey[39;49;00m)))[37m[39;49;00m$
  2031^I[37m      [39;49;00m([31mcancel-timer[39;49;00m[37m [39;49;00m[31mtimer[39;49;00m)[37m[39;49;00m$
  2032^I[37m      [39;49;00m([32muse-global-map[39;49;00m[37m [39;49;00m[31mold-global-map[39;49;00m))))[37m[39;49;00m$
  2033^I[37m[39;49;00m$
  2034^I([34mdefvar[39;49;00m[37m [39;49;00m[31mread-passwd-map[39;49;00m[37m[39;49;00m$
  2035^I[37m  [39;49;00m[37m;; BEWARE: `defconst' would purecopy it, breaking the sharing with[39;49;00m[37m[39;49;00m$
  2036^I[37m  [39;49;00m[37m;; minibuffer-local-map along the way![39;49;00m[37m[39;49;00m$
  2037^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mmap[39;49;00m[37m [39;49;00m([32mmake-sparse-keymap[39;49;00m)))[37m[39;49;00m$
  2038^I[37m    [39;49;00m([32mset-keymap-parent[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m[31mminibuffer-local-map[39;49;00m)[37m[39;49;00m$
  2039^I[37m    [39;49;00m([32mdefine-key[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\C[39;49;00m[33m-u[39;49;00m[33m"[39;49;00m[37m [39;49;00m[32m#'[39;49;00m[31mdelete-minibuffer-contents[39;49;00m)[37m [39;49;00m[37m;bug#12570[39;49;00m[37m[39;49;00m$
  2040^I[37m    [39;49;00m[31mmap[39;49;00m)[37m[39;49;00m$
  2041^I[37m  [39;49;00m[33m"[39;49;00m[33mKeymap used while reading passwords.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  2042^I[37m[39;49;00m$
  2043^I([36mdefun[39;49;00m[37m [39;49;00m[31mread-passwd[39;49;00m[37m [39;49;00m([31mprompt[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mconfirm[39;49;00m[37m [39;49;00m[31mdefault[39;49;00m)[37m[39;49;00m$
  2044^I[37m  [39;49;00m[33m"[39;49;00m[33mRead a password, prompting with PROMPT, and return it.[39;49;00m$
  2045^I[33mIf optional CONFIRM is non-nil, read the password twice to make sure.[39;49;00m$
  2046^I[33mOptional DEFAULT is a default password to use instead of empty input.[39;49;00m$
  2047^I[33m[39;49;00m$
  2048^I[33mThis function echoes [39;49;00m[33m`.'[39;49;00m[33m for each character that the user types.[39;49;00m$
  2049^I[33mYou could let-bind [39;49;00m[33m`read-hide-char'[39;49;00m[33m to another hiding character, though.[39;49;00m$
  2050^I[33m[39;49;00m$
  2051^I[33mOnce the caller uses the password, it can erase the password[39;49;00m$
  2052^I[33mby doing (clear-string STRING).[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2053^I[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mconfirm[39;49;00m[37m[39;49;00m$
  2054^I[37m      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m([31msuccess[39;49;00m)[37m[39;49;00m$
  2055^I[37m        [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m[31msuccess[39;49;00m)[37m[39;49;00m$
  2056^I[37m          [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mfirst[39;49;00m[37m [39;49;00m([31mread-passwd[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mdefault[39;49;00m))[37m[39;49;00m$
  2057^I[37m                [39;49;00m([31msecond[39;49;00m[37m [39;49;00m([31mread-passwd[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mConfirm password: [39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mdefault[39;49;00m)))[37m[39;49;00m$
  2058^I[37m            [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mequal[39;49;00m[37m [39;49;00m[31mfirst[39;49;00m[37m [39;49;00m[31msecond[39;49;00m)[37m[39;49;00m$
  2059^I[37m                [39;49;00m([34mprogn[39;49;00m[37m[39;49;00m$
  2060^I[37m                  [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32marrayp[39;49;00m[37m [39;49;00m[31msecond[39;49;00m)[37m [39;49;00m([32mclear-string[39;49;00m[37m [39;49;00m[31msecond[39;49;00m))[37m[39;49;00m$
  2061^I[37m                  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31msuccess[39;49;00m[37m [39;49;00m[31mfirst[39;49;00m))[37m[39;49;00m$
  2062^I[37m              [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32marrayp[39;49;00m[37m [39;49;00m[31mfirst[39;49;00m)[37m [39;49;00m([32mclear-string[39;49;00m[37m [39;49;00m[31mfirst[39;49;00m))[37m[39;49;00m$
  2063^I[37m              [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32marrayp[39;49;00m[37m [39;49;00m[31msecond[39;49;00m)[37m [39;49;00m([32mclear-string[39;49;00m[37m [39;49;00m[31msecond[39;49;00m))[37m[39;49;00m$
  2064^I[37m              [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mPassword not repeated accurately; please start over[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  2065^I[37m              [39;49;00m([31msit-for[39;49;00m[37m [39;49;00m[34m1[39;49;00m))))[37m[39;49;00m$
  2066^I[37m        [39;49;00m[31msuccess[39;49;00m)[37m[39;49;00m$
  2067^I[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mhide-chars-fun[39;49;00m[37m[39;49;00m$
  2068^I[37m           [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31mbeg[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[31m_len[39;49;00m)[37m[39;49;00m$
  2069^I[37m             [39;49;00m([32mclear-this-command-keys[39;49;00m)[37m[39;49;00m$
  2070^I[37m             [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m[37m [39;49;00m([32mmin[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m([32mmax[39;49;00m[37m [39;49;00m([32mminibuffer-prompt-end[39;49;00m)[37m[39;49;00m$
  2071^I[37m                                     [39;49;00m[31mbeg[39;49;00m)))[37m[39;49;00m$
  2072^I[37m             [39;49;00m([36mdotimes[39;49;00m[37m [39;49;00m([31mi[39;49;00m[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m))[37m[39;49;00m$
  2073^I[37m               [39;49;00m([32mput-text-property[39;49;00m[37m [39;49;00m([32m+[39;49;00m[37m [39;49;00m[31mi[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m)[37m [39;49;00m([32m+[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mi[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m)[37m[39;49;00m$
  2074^I[37m                                  [39;49;00m[33m'display[39;49;00m[37m [39;49;00m([32mstring[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mread-hide-char[39;49;00m[37m [39;49;00m[33m?.[39;49;00m))))))[37m[39;49;00m$
  2075^I[37m          [39;49;00m[31mminibuf[39;49;00m)[37m[39;49;00m$
  2076^I[37m      [39;49;00m([31mminibuffer-with-setup-hook[39;49;00m[37m[39;49;00m$
  2077^I[37m          [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m()[37m[39;49;00m$
  2078^I[37m            [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mminibuf[39;49;00m[37m [39;49;00m([32mcurrent-buffer[39;49;00m))[37m[39;49;00m$
  2079^I[37m            [39;49;00m[37m;; Turn off electricity.[39;49;00m[37m[39;49;00m$
  2080^I[37m            [39;49;00m([36msetq-local[39;49;00m[37m [39;49;00m[31mpost-self-insert-hook[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
  2081^I[37m            [39;49;00m([36msetq-local[39;49;00m[37m [39;49;00m[31mbuffer-undo-list[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
  2082^I[37m            [39;49;00m([36msetq-local[39;49;00m[37m [39;49;00m[31mselect-active-regions[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
  2083^I[37m            [39;49;00m([32muse-local-map[39;49;00m[37m [39;49;00m[31mread-passwd-map[39;49;00m)[37m[39;49;00m$
  2084^I[37m            [39;49;00m([36msetq-local[39;49;00m[37m [39;49;00m[31minhibit-modification-hooks[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m [39;49;00m[37m;bug#15501.[39;49;00m[37m[39;49;00m$
  2085^I[37m^I    [39;49;00m([36msetq-local[39;49;00m[37m [39;49;00m[31mshow-paren-mode[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m^I^I[39;49;00m[37m;bug#16091.[39;49;00m[37m[39;49;00m$
  2086^I[37m            [39;49;00m([31madd-hook[39;49;00m[37m [39;49;00m[33m'after-change-functions[39;49;00m[37m [39;49;00m[31mhide-chars-fun[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[33m'local[39;49;00m))[37m[39;49;00m$
  2087^I[37m        [39;49;00m([34munwind-protect[39;49;00m[37m[39;49;00m$
  2088^I[37m            [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31menable-recursive-minibuffers[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
  2089^I[37m^I^I  [39;49;00m([31mread-hide-char[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mread-hide-char[39;49;00m[37m [39;49;00m[33m?.[39;49;00m)))[37m[39;49;00m$
  2090^I[37m              [39;49;00m([32mread-string[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m[31mdefault[39;49;00m))[37m [39;49;00m[37m; t = "no history"[39;49;00m[37m[39;49;00m$
  2091^I[37m          [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mbuffer-live-p[39;49;00m[37m [39;49;00m[31mminibuf[39;49;00m)[37m[39;49;00m$
  2092^I[37m            [39;49;00m([36mwith-current-buffer[39;49;00m[37m [39;49;00m[31mminibuf[39;49;00m[37m[39;49;00m$
  2093^I[37m              [39;49;00m[37m;; Not sure why but it seems that there might be cases where the[39;49;00m[37m[39;49;00m$
  2094^I[37m              [39;49;00m[37m;; minibuffer is not always properly reset later on, so undo[39;49;00m[37m[39;49;00m$
  2095^I[37m              [39;49;00m[37m;; whatever we've done here (bug#11392).[39;49;00m[37m[39;49;00m$
  2096^I[37m              [39;49;00m([31mremove-hook[39;49;00m[37m [39;49;00m[33m'after-change-functions[39;49;00m[37m [39;49;00m[31mhide-chars-fun[39;49;00m[37m [39;49;00m[33m'local[39;49;00m)[37m[39;49;00m$
  2097^I[37m              [39;49;00m([32mkill-local-variable[39;49;00m[37m [39;49;00m[33m'post-self-insert-hook[39;49;00m)[37m[39;49;00m$
  2098^I[37m              [39;49;00m[37m;; And of course, don't keep the sensitive data around.[39;49;00m[37m[39;49;00m$
  2099^I[37m              [39;49;00m([32merase-buffer[39;49;00m))))))))[37m[39;49;00m$
  2100^I[37m[39;49;00m$
  2101^I([36mdefun[39;49;00m[37m [39;49;00m[31mread-number[39;49;00m[37m [39;49;00m([31mprompt[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mdefault[39;49;00m)[37m[39;49;00m$
  2102^I[37m  [39;49;00m[33m"[39;49;00m[33mRead a numeric value in the minibuffer, prompting with PROMPT.[39;49;00m$
  2103^I[33mDEFAULT specifies a default value to return if the user just types RET.[39;49;00m$
  2104^I[33mThe value of DEFAULT is inserted into PROMPT.[39;49;00m$
  2105^I[33mThis function is used by the [39;49;00m[33m`interactive'[39;49;00m[33m code letter [39;49;00m[33m`n'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2106^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mn[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
  2107^I[37m^I[39;49;00m([31mdefault1[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mdefault[39;49;00m)[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mdefault[39;49;00m)[37m [39;49;00m[31mdefault[39;49;00m)))[37m[39;49;00m$
  2108^I[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31mdefault1[39;49;00m[37m[39;49;00m$
  2109^I[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m[37m[39;49;00m$
  2110^I[37m^I    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m([39;49;00m[33m\\[39;49;00m[33m):[ [39;49;00m[33m\t[39;49;00m[33m]*[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m)[37m[39;49;00m$
  2111^I[37m^I^I[39;49;00m([32mreplace-match[39;49;00m[37m [39;49;00m([32mformat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m (default %s)[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mdefault1[39;49;00m)[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m[39;49;00m$
  2112^I[37m^I      [39;49;00m([31mreplace-regexp-in-string[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m[ [39;49;00m[33m\t[39;49;00m[33m]*[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2113^I[37m^I^I^I^I^I[39;49;00m([32mformat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m (default %s) [39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mdefault1[39;49;00m)[37m[39;49;00m$
  2114^I[37m^I^I^I^I^I[39;49;00m[31mprompt[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m[31mt[39;49;00m))))[37m[39;49;00m$
  2115^I[37m    [39;49;00m([34mwhile[39;49;00m[37m[39;49;00m$
  2116^I[37m^I[39;49;00m([34mprogn[39;49;00m[37m[39;49;00m$
  2117^I[37m^I  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mstr[39;49;00m[37m [39;49;00m([32mread-from-minibuffer[39;49;00m[37m[39;49;00m$
  2118^I[37m^I^I      [39;49;00m[31mprompt[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m$
  2119^I[37m^I^I      [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31mdefault[39;49;00m[37m[39;49;00m$
  2120^I[37m^I^I^I[39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mdefault[39;49;00m)[37m[39;49;00m$
  2121^I[37m^I^I^I    [39;49;00m([32mmapcar[39;49;00m[37m [39;49;00m[33m'number-to-string[39;49;00m[37m [39;49;00m([32mdelq[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mdefault[39;49;00m))[37m[39;49;00m$
  2122^I[37m^I^I^I  [39;49;00m([32mnumber-to-string[39;49;00m[37m [39;49;00m[31mdefault[39;49;00m))))))[37m[39;49;00m$
  2123^I[37m^I    [39;49;00m([34mcondition-case[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m$
  2124^I[37m^I^I[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mn[39;49;00m[37m [39;49;00m([34mcond[39;49;00m[37m[39;49;00m$
  2125^I[37m^I^I^I [39;49;00m(([31mzerop[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31mstr[39;49;00m))[37m [39;49;00m[31mdefault1[39;49;00m)[37m[39;49;00m$
  2126^I[37m^I^I^I [39;49;00m(([32mstringp[39;49;00m[37m [39;49;00m[31mstr[39;49;00m)[37m [39;49;00m([32mread[39;49;00m[37m [39;49;00m[31mstr[39;49;00m))))[37m[39;49;00m$
  2127^I[37m^I      [39;49;00m([36merror[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)))[37m[39;49;00m$
  2128^I[37m^I  [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32mnumberp[39;49;00m[37m [39;49;00m[31mn[39;49;00m)[37m[39;49;00m$
  2129^I[37m^I    [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mPlease enter a number.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  2130^I[37m^I    [39;49;00m([31msit-for[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m[39;49;00m$
  2131^I[37m^I    [39;49;00m[31mt[39;49;00m)))[37m[39;49;00m$
  2132^I[37m    [39;49;00m[31mn[39;49;00m))[37m[39;49;00m$
  2133^I[37m[39;49;00m$
  2134^I([36mdefun[39;49;00m[37m [39;49;00m[31mread-char-choice[39;49;00m[37m [39;49;00m([31mprompt[39;49;00m[37m [39;49;00m[31mchars[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31minhibit-keyboard-quit[39;49;00m)[37m[39;49;00m$
  2135^I[37m  [39;49;00m[33m"[39;49;00m[33mRead and return one of CHARS, prompting for PROMPT.[39;49;00m$
  2136^I[33mAny input that is not one of CHARS is ignored.[39;49;00m$
  2137^I[33m[39;49;00m$
  2138^I[33mIf optional argument INHIBIT-KEYBOARD-QUIT is non-nil, ignore[39;49;00m$
  2139^I[33mkeyboard-quit events while waiting for a valid input.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2140^I[37m  [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mchars[39;49;00m)[37m[39;49;00m$
  2141^I[37m    [39;49;00m([36merror[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mCalled [39;49;00m[33m`read-char-choice'[39;49;00m[33m without valid char choices[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
  2142^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m([31mchar[39;49;00m[37m [39;49;00m[31mdone[39;49;00m[37m [39;49;00m[31mshow-help[39;49;00m[37m [39;49;00m([31mhelpbuf[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m *Char Help*[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
  2143^I[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mcursor-in-echo-area[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
  2144^I[37m          [39;49;00m([31mexecuting-kbd-macro[39;49;00m[37m [39;49;00m[31mexecuting-kbd-macro[39;49;00m)[37m[39;49;00m$
  2145^I[37m^I  [39;49;00m([31mesc-flag[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m$
  2146^I[37m      [39;49;00m([36msave-window-excursion[39;49;00m[37m^I      [39;49;00m[37m; in case we call help-form-show[39;49;00m[37m[39;49;00m$
  2147^I[37m^I[39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m[31mdone[39;49;00m)[37m[39;49;00m$
  2148^I[37m^I  [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32mget-text-property[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[33m'face[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m)[37m[39;49;00m$
  2149^I[37m^I    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m[37m [39;49;00m([32mpropertize[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m[37m [39;49;00m[33m'face[39;49;00m[37m [39;49;00m[33m'minibuffer-prompt[39;49;00m)))[37m[39;49;00m$
  2150^I[37m^I  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mchar[39;49;00m[37m [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31minhibit-quit[39;49;00m[37m [39;49;00m[31minhibit-keyboard-quit[39;49;00m))[37m[39;49;00m$
  2151^I[37m^I^I       [39;49;00m([31mread-key[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m)))[37m[39;49;00m$
  2152^I[37m^I  [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mshow-help[39;49;00m[37m [39;49;00m([32mbuffer-live-p[39;49;00m[37m [39;49;00m([32mget-buffer[39;49;00m[37m [39;49;00m[31mhelpbuf[39;49;00m))[37m[39;49;00m$
  2153^I[37m^I       [39;49;00m([32mkill-buffer[39;49;00m[37m [39;49;00m[31mhelpbuf[39;49;00m))[37m[39;49;00m$
  2154^I[37m^I  [39;49;00m([34mcond[39;49;00m[37m[39;49;00m$
  2155^I[37m^I   [39;49;00m(([31mnot[39;49;00m[37m [39;49;00m([32mnumberp[39;49;00m[37m [39;49;00m[31mchar[39;49;00m)))[37m[39;49;00m$
  2156^I[37m^I   [39;49;00m[37m;; If caller has set help-form, that's enough.[39;49;00m[37m[39;49;00m$
  2157^I[37m^I   [39;49;00m[37m;; They don't explicitly have to add help-char to chars.[39;49;00m[37m[39;49;00m$
  2158^I[37m^I   [39;49;00m(([34mand[39;49;00m[37m [39;49;00m[31mhelp-form[39;49;00m[37m[39;49;00m$
  2159^I[37m^I^I [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mchar[39;49;00m[37m [39;49;00m[31mhelp-char[39;49;00m)[37m[39;49;00m$
  2160^I[37m^I^I [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mshow-help[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
  2161^I[37m^I^I [39;49;00m([31mhelp-form-show[39;49;00m)))[37m[39;49;00m$
  2162^I[37m^I   [39;49;00m(([32mmemq[39;49;00m[37m [39;49;00m[31mchar[39;49;00m[37m [39;49;00m[31mchars[39;49;00m)[37m[39;49;00m$
  2163^I[37m^I    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mdone[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
  2164^I[37m^I   [39;49;00m(([34mand[39;49;00m[37m [39;49;00m[31mexecuting-kbd-macro[39;49;00m[37m [39;49;00m([32m=[39;49;00m[37m [39;49;00m[31mchar[39;49;00m[37m [39;49;00m[34m-1[39;49;00m))[37m[39;49;00m$
  2165^I[37m^I    [39;49;00m[37m;; read-event returns -1 if we are in a kbd macro and[39;49;00m[37m[39;49;00m$
  2166^I[37m^I    [39;49;00m[37m;; there are no more events in the macro.  Attempt to[39;49;00m[37m[39;49;00m$
  2167^I[37m^I    [39;49;00m[37m;; get an event interactively.[39;49;00m[37m[39;49;00m$
  2168^I[37m^I    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mexecuting-kbd-macro[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m$
  2169^I[37m^I   [39;49;00m(([31mnot[39;49;00m[37m [39;49;00m[31minhibit-keyboard-quit[39;49;00m)[37m[39;49;00m$
  2170^I[37m^I    [39;49;00m([34mcond[39;49;00m[37m[39;49;00m$
  2171^I[37m^I     [39;49;00m(([34mand[39;49;00m[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[31mesc-flag[39;49;00m)[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mchar[39;49;00m[37m [39;49;00m[33m?\e[39;49;00m))[37m[39;49;00m$
  2172^I[37m^I      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mesc-flag[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
  2173^I[37m^I     [39;49;00m(([32mmemq[39;49;00m[37m [39;49;00m[31mchar[39;49;00m[37m [39;49;00m'([33m?\C[39;49;00m[31m-g[39;49;00m[37m [39;49;00m[33m?\e[39;49;00m))[37m[39;49;00m$
  2174^I[37m^I      [39;49;00m([31mkeyboard-quit[39;49;00m))))))))[37m[39;49;00m$
  2175^I[37m    [39;49;00m[37m;; Display the question with the answer.  But without cursor-in-echo-area.[39;49;00m[37m[39;49;00m$
  2176^I[37m    [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m%s%s[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m[37m [39;49;00m([32mchar-to-string[39;49;00m[37m [39;49;00m[31mchar[39;49;00m))[37m[39;49;00m$
  2177^I[37m    [39;49;00m[31mchar[39;49;00m))[37m[39;49;00m$
  2178^I[37m[39;49;00m$
  2179^I([36mdefun[39;49;00m[37m [39;49;00m[31msit-for[39;49;00m[37m [39;49;00m([31mseconds[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mnodisp[39;49;00m[37m [39;49;00m[31mobsolete[39;49;00m)[37m[39;49;00m$
  2180^I[37m  [39;49;00m[33m"[39;49;00m[33mRedisplay, then wait for SECONDS seconds.  Stop when input is available.[39;49;00m$
  2181^I[33mSECONDS may be a floating-point value.[39;49;00m$
  2182^I[33m\([39;49;00m[33mOn operating systems that do not support waiting for fractions of a[39;49;00m$
  2183^I[33msecond, floating-point values are rounded down to the nearest integer.)[39;49;00m$
  2184^I[33m[39;49;00m$
  2185^I[33mIf optional arg NODISP is t, don't redisplay, just wait for input.[39;49;00m$
  2186^I[33mRedisplay does not happen if input is available before it starts.[39;49;00m$
  2187^I[33m[39;49;00m$
  2188^I[33mValue is t if waited the full time with no input arriving, and nil otherwise.[39;49;00m$
  2189^I[33m[39;49;00m$
  2190^I[33mAn obsolete, but still supported form is[39;49;00m$
  2191^I[33m\([39;49;00m[33msit-for SECONDS &optional MILLISECONDS NODISP)[39;49;00m$
  2192^I[33mwhere the optional arg MILLISECONDS specifies an additional wait period,[39;49;00m$
  2193^I[33min milliseconds; this was useful when Emacs was built without[39;49;00m$
  2194^I[33mfloating point support.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2195^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31madvertised-calling-convention[39;49;00m[37m [39;49;00m([31mseconds[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mnodisp[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m22.1[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
  2196^I[37m  [39;49;00m[37m;; This used to be implemented in C until the following discussion:[39;49;00m[37m[39;49;00m$
  2197^I[37m  [39;49;00m[37m;; http://lists.gnu.org/archive/html/emacs-devel/2006-07/msg00401.html[39;49;00m[37m[39;49;00m$
  2198^I[37m  [39;49;00m[37m;; Then it was moved here using an implementation based on an idle timer,[39;49;00m[37m[39;49;00m$
  2199^I[37m  [39;49;00m[37m;; which was then replaced by the use of read-event.[39;49;00m[37m[39;49;00m$
  2200^I[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mnumberp[39;49;00m[37m [39;49;00m[31mnodisp[39;49;00m)[37m[39;49;00m$
  2201^I[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mseconds[39;49;00m[37m [39;49;00m([32m+[39;49;00m[37m [39;49;00m[31mseconds[39;49;00m[37m [39;49;00m([32m*[39;49;00m[37m [39;49;00m[34m1e-3[39;49;00m[37m [39;49;00m[31mnodisp[39;49;00m))[37m[39;49;00m$
  2202^I[37m            [39;49;00m[31mnodisp[39;49;00m[37m [39;49;00m[31mobsolete[39;49;00m)[37m[39;49;00m$
  2203^I[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mobsolete[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mnodisp[39;49;00m[37m [39;49;00m[31mobsolete[39;49;00m)))[37m[39;49;00m$
  2204^I[37m  [39;49;00m([34mcond[39;49;00m[37m[39;49;00m$
  2205^I[37m   [39;49;00m([31mnoninteractive[39;49;00m[37m[39;49;00m$
  2206^I[37m    [39;49;00m([32msleep-for[39;49;00m[37m [39;49;00m[31mseconds[39;49;00m)[37m[39;49;00m$
  2207^I[37m    [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
  2208^I[37m   [39;49;00m(([32minput-pending-p[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
  2209^I[37m    [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
  2210^I[37m   [39;49;00m(([32m<=[39;49;00m[37m [39;49;00m[31mseconds[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  2211^I[37m    [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mnodisp[39;49;00m[37m [39;49;00m([32mredisplay[39;49;00m)))[37m[39;49;00m$
  2212^I[37m   [39;49;00m([31mt[39;49;00m[37m[39;49;00m$
  2213^I[37m    [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mnodisp[39;49;00m[37m [39;49;00m([32mredisplay[39;49;00m))[37m[39;49;00m$
  2214^I[37m    [39;49;00m[37m;; FIXME: we should not read-event here at all, because it's much too[39;49;00m[37m[39;49;00m$
  2215^I[37m    [39;49;00m[37m;; difficult to reliably "undo" a read-event by pushing it onto[39;49;00m[37m[39;49;00m$
  2216^I[37m    [39;49;00m[37m;; unread-command-events.[39;49;00m[37m[39;49;00m$
  2217^I[37m    [39;49;00m[37m;; For bug#14782, we need read-event to do the keyboard-coding-system[39;49;00m[37m[39;49;00m$
  2218^I[37m    [39;49;00m[37m;; decoding (hence non-nil as second arg under POSIX ttys).[39;49;00m[37m[39;49;00m$
  2219^I[37m    [39;49;00m[37m;; For bug#15614, we need read-event not to inherit-input-method.[39;49;00m[37m[39;49;00m$
  2220^I[37m    [39;49;00m[37m;; So we temporarily suspend input-method-function.[39;49;00m[37m[39;49;00m$
  2221^I[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([32mread[39;49;00m[37m [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31minput-method-function[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m$
  2222^I[37m                  [39;49;00m([32mread-event[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m[31mseconds[39;49;00m))))[37m[39;49;00m$
  2223^I[37m      [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[32mread[39;49;00m)[37m[39;49;00m$
  2224^I[37m^I  [39;49;00m([34mprogn[39;49;00m[37m[39;49;00m$
  2225^I[37m            [39;49;00m[37m;; https://lists.gnu.org/archive/html/emacs-devel/2006-10/msg00394.html[39;49;00m[37m[39;49;00m$
  2226^I[37m            [39;49;00m[37m;; We want `read' appear in the next command's this-command-event[39;49;00m[37m[39;49;00m$
  2227^I[37m            [39;49;00m[37m;; but not in the current one.[39;49;00m[37m[39;49;00m$
  2228^I[37m            [39;49;00m[37m;; By pushing (cons t read), we indicate that `read' has not[39;49;00m[37m[39;49;00m$
  2229^I[37m            [39;49;00m[37m;; yet been recorded in this-command-keys, so it will be recorded[39;49;00m[37m[39;49;00m$
  2230^I[37m            [39;49;00m[37m;; next time it's read.[39;49;00m[37m[39;49;00m$
  2231^I[37m            [39;49;00m[37m;; And indeed the `seconds' argument to read-event correctly[39;49;00m[37m[39;49;00m$
  2232^I[37m            [39;49;00m[37m;; prevented recording this event in the current command's[39;49;00m[37m[39;49;00m$
  2233^I[37m            [39;49;00m[37m;; this-command-keys.[39;49;00m[37m[39;49;00m$
  2234^I[37m^I    [39;49;00m([36mpush[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m[32mread[39;49;00m)[37m [39;49;00m[31munread-command-events[39;49;00m)[37m[39;49;00m$
  2235^I[37m^I    [39;49;00m[31mnil[39;49;00m))))))[37m[39;49;00m$
  2236^I[37m[39;49;00m$
  2237^I[37m;; Behind display-popup-menus-p test.[39;49;00m[37m[39;49;00m$
  2238^I([36mdeclare-function[39;49;00m[37m [39;49;00m[32mx-popup-dialog[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mmenu.c[39;49;00m[33m"[39;49;00m[37m [39;49;00m([31mposition[39;49;00m[37m [39;49;00m[31mcontents[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mheader[39;49;00m))[37m[39;49;00m$
  2239^I[37m[39;49;00m$
  2240^I([36mdefun[39;49;00m[37m [39;49;00m[31my-or-n-p[39;49;00m[37m [39;49;00m([31mprompt[39;49;00m)[37m[39;49;00m$
  2241^I[37m  [39;49;00m[33m"[39;49;00m[33mAsk user a [39;49;00m[33m\"[39;49;00m[33my or n[39;49;00m[33m\"[39;49;00m[33m question.  Return t if answer is [39;49;00m[33m\"[39;49;00m[33my[39;49;00m[33m\"[39;49;00m[33m.[39;49;00m$
  2242^I[33mPROMPT is the string to display to ask the question.  It should[39;49;00m$
  2243^I[33mend in a space; [39;49;00m[33m`y-or-n-p'[39;49;00m[33m adds [39;49;00m[33m\"[39;49;00m[33m(y or n) [39;49;00m[33m\"[39;49;00m[33m to it.[39;49;00m$
  2244^I[33m[39;49;00m$
  2245^I[33mNo confirmation of the answer is requested; a single character is[39;49;00m$
  2246^I[33menough.  SPC also means yes, and DEL means no.[39;49;00m$
  2247^I[33m[39;49;00m$
  2248^I[33mTo be precise, this function translates user input into responses[39;49;00m$
  2249^I[33mby consulting the bindings in [39;49;00m[33m`query-replace-map'[39;49;00m[33m; see the[39;49;00m$
  2250^I[33mdocumentation of that variable for more information.  In this[39;49;00m$
  2251^I[33mcase, the useful bindings are [39;49;00m[33m`act'[39;49;00m[33m, [39;49;00m[33m`skip'[39;49;00m[33m, [39;49;00m[33m`recenter'[39;49;00m[33m,[39;49;00m$
  2252^I[33m`scroll-up'[39;49;00m[33m, [39;49;00m[33m`scroll-down'[39;49;00m[33m, and [39;49;00m[33m`quit'[39;49;00m[33m.[39;49;00m$
  2253^I[33mAn [39;49;00m[33m`act'[39;49;00m[33m response means yes, and a [39;49;00m[33m`skip'[39;49;00m[33m response means no.[39;49;00m$
  2254^I[33mA [39;49;00m[33m`quit'[39;49;00m[33m response means to invoke [39;49;00m[33m`keyboard-quit'[39;49;00m[33m.[39;49;00m$
  2255^I[33mIf the user enters [39;49;00m[33m`recenter'[39;49;00m[33m, [39;49;00m[33m`scroll-up'[39;49;00m[33m, or [39;49;00m[33m`scroll-down'[39;49;00m[33m[39;49;00m$
  2256^I[33mresponses, perform the requested window recentering or scrolling[39;49;00m$
  2257^I[33mand ask again.[39;49;00m$
  2258^I[33m[39;49;00m$
  2259^I[33mUnder a windowing system a dialog box will be used if [39;49;00m[33m`last-nonmenu-event'[39;49;00m[33m[39;49;00m$
  2260^I[33mis nil and [39;49;00m[33m`use-dialog-box'[39;49;00m[33m is non-nil.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2261^I[37m  [39;49;00m[37m;; ¡Beware! when I tried to edebug this code, Emacs got into a weird state[39;49;00m[37m[39;49;00m$
  2262^I[37m  [39;49;00m[37m;; where all the keys were unbound (i.e. it somehow got triggered[39;49;00m[37m[39;49;00m$
  2263^I[37m  [39;49;00m[37m;; within read-key, apparently).  I had to kill it.[39;49;00m[37m[39;49;00m$
  2264^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31manswer[39;49;00m[37m [39;49;00m[33m'recenter[39;49;00m)[37m[39;49;00m$
  2265^I[37m^I[39;49;00m([31mpadded[39;49;00m[37m [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31mprompt[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mdialog[39;49;00m)[37m[39;49;00m$
  2266^I[37m^I^I  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31ml[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m)))[37m[39;49;00m$
  2267^I[37m^I^I    [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m[37m[39;49;00m$
  2268^I[37m^I^I^I    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([31mzerop[39;49;00m[37m [39;49;00m[31ml[39;49;00m)[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[33m?\s[39;49;00m[37m [39;49;00m([32maref[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m[37m [39;49;00m([32m1-[39;49;00m[37m [39;49;00m[31ml[39;49;00m))))[37m[39;49;00m$
  2269^I[37m^I^I^I^I[39;49;00m[33m"[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  2270^I[37m^I^I^I    [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mdialog[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m(y or n) [39;49;00m[33m"[39;49;00m))))))[37m[39;49;00m$
  2271^I[37m    [39;49;00m([34mcond[39;49;00m[37m[39;49;00m$
  2272^I[37m     [39;49;00m([31mnoninteractive[39;49;00m[37m[39;49;00m$
  2273^I[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m[37m [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mpadded[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m))[37m[39;49;00m$
  2274^I[37m      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtemp-prompt[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m))[37m[39;49;00m$
  2275^I[37m^I[39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[31manswer[39;49;00m[37m [39;49;00m'([31mact[39;49;00m[37m [39;49;00m[31mskip[39;49;00m)))[37m[39;49;00m$
  2276^I[37m^I  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mstr[39;49;00m[37m [39;49;00m([32mread-string[39;49;00m[37m [39;49;00m[31mtemp-prompt[39;49;00m)))[37m[39;49;00m$
  2277^I[37m^I    [39;49;00m([34mcond[39;49;00m[37m [39;49;00m(([32mmember[39;49;00m[37m [39;49;00m[31mstr[39;49;00m[37m [39;49;00m'([33m"[39;49;00m[33my[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mY[39;49;00m[33m"[39;49;00m))[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31manswer[39;49;00m[37m [39;49;00m[33m'act[39;49;00m))[37m[39;49;00m$
  2278^I[37m^I^I  [39;49;00m(([32mmember[39;49;00m[37m [39;49;00m[31mstr[39;49;00m[37m [39;49;00m'([33m"[39;49;00m[33mn[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mN[39;49;00m[33m"[39;49;00m))[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31manswer[39;49;00m[37m [39;49;00m[33m'skip[39;49;00m))[37m[39;49;00m$
  2279^I[37m^I^I  [39;49;00m([31mt[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mtemp-prompt[39;49;00m[37m [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mPlease answer y or n.  [39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2280^I[37m^I^I^I^I^I       [39;49;00m[31mprompt[39;49;00m))))))))[37m[39;49;00m$
  2281^I[37m     [39;49;00m(([34mand[39;49;00m[37m [39;49;00m([31mdisplay-popup-menus-p[39;49;00m)[37m[39;49;00m$
  2282^I[37m^I   [39;49;00m([32mlistp[39;49;00m[37m [39;49;00m[31mlast-nonmenu-event[39;49;00m)[37m[39;49;00m$
  2283^I[37m^I   [39;49;00m[31muse-dialog-box[39;49;00m)[37m[39;49;00m$
  2284^I[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m[37m [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mpadded[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
  2285^I[37m^I    [39;49;00m[31manswer[39;49;00m[37m [39;49;00m([32mx-popup-dialog[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m`(,[31mprompt[39;49;00m[37m [39;49;00m([33m"[39;49;00m[33mYes[39;49;00m[33m"[39;49;00m[37m [39;49;00m.[37m [39;49;00m[31mact[39;49;00m)[37m [39;49;00m([33m"[39;49;00m[33mNo[39;49;00m[33m"[39;49;00m[37m [39;49;00m.[37m [39;49;00m[31mskip[39;49;00m)))))[37m[39;49;00m$
  2286^I[37m     [39;49;00m([31mt[39;49;00m[37m[39;49;00m$
  2287^I[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m[37m [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mpadded[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m))[37m[39;49;00m$
  2288^I[37m      [39;49;00m([34mwhile[39;49;00m[37m[39;49;00m$
  2289^I[37m          [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mscroll-actions[39;49;00m[37m [39;49;00m'([32mrecenter[39;49;00m[37m [39;49;00m[32mscroll-up[39;49;00m[37m [39;49;00m[32mscroll-down[39;49;00m[37m[39;49;00m$
  2290^I[37m^I^I^I^I   [39;49;00m[32mscroll-other-window[39;49;00m[37m [39;49;00m[31mscroll-other-window-down[39;49;00m))[37m[39;49;00m$
  2291^I[37m^I^I [39;49;00m([31mkey[39;49;00m[37m[39;49;00m$
  2292^I[37m                  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mcursor-in-echo-area[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
  2293^I[37m                    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31mminibuffer-auto-raise[39;49;00m[37m[39;49;00m$
  2294^I[37m                      [39;49;00m([32mraise-frame[39;49;00m[37m [39;49;00m([32mwindow-frame[39;49;00m[37m [39;49;00m([32mminibuffer-window[39;49;00m))))[37m[39;49;00m$
  2295^I[37m                    [39;49;00m([31mread-key[39;49;00m[37m [39;49;00m([32mpropertize[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[31manswer[39;49;00m[37m [39;49;00m[31mscroll-actions[39;49;00m)[37m[39;49;00m$
  2296^I[37m                                              [39;49;00m[31mprompt[39;49;00m[37m[39;49;00m$
  2297^I[37m                                            [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mPlease answer y or n.  [39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2298^I[37m                                                    [39;49;00m[31mprompt[39;49;00m))[37m[39;49;00m$
  2299^I[37m                                          [39;49;00m[33m'face[39;49;00m[37m [39;49;00m[33m'minibuffer-prompt[39;49;00m)))))[37m[39;49;00m$
  2300^I[37m            [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31manswer[39;49;00m[37m [39;49;00m([32mlookup-key[39;49;00m[37m [39;49;00m[31mquery-replace-map[39;49;00m[37m [39;49;00m([32mvector[39;49;00m[37m [39;49;00m[31mkey[39;49;00m)[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
  2301^I[37m            [39;49;00m([34mcond[39;49;00m[37m[39;49;00m$
  2302^I[37m^I     [39;49;00m(([32mmemq[39;49;00m[37m [39;49;00m[31manswer[39;49;00m[37m [39;49;00m'([31mskip[39;49;00m[37m [39;49;00m[31mact[39;49;00m))[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
  2303^I[37m^I     [39;49;00m(([32meq[39;49;00m[37m [39;49;00m[31manswer[39;49;00m[37m [39;49;00m[33m'recenter[39;49;00m)[37m[39;49;00m$
  2304^I[37m^I      [39;49;00m([32mrecenter[39;49;00m)[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
  2305^I[37m^I     [39;49;00m(([32meq[39;49;00m[37m [39;49;00m[31manswer[39;49;00m[37m [39;49;00m[33m'scroll-up[39;49;00m)[37m[39;49;00m$
  2306^I[37m^I      [39;49;00m([36mignore-errors[39;49;00m[37m [39;49;00m([31mscroll-up-command[39;49;00m))[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
  2307^I[37m^I     [39;49;00m(([32meq[39;49;00m[37m [39;49;00m[31manswer[39;49;00m[37m [39;49;00m[33m'scroll-down[39;49;00m)[37m[39;49;00m$
  2308^I[37m^I      [39;49;00m([36mignore-errors[39;49;00m[37m [39;49;00m([31mscroll-down-command[39;49;00m))[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
  2309^I[37m^I     [39;49;00m(([32meq[39;49;00m[37m [39;49;00m[31manswer[39;49;00m[37m [39;49;00m[33m'scroll-other-window[39;49;00m)[37m[39;49;00m$
  2310^I[37m^I      [39;49;00m([36mignore-errors[39;49;00m[37m [39;49;00m([32mscroll-other-window[39;49;00m))[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
  2311^I[37m^I     [39;49;00m(([32meq[39;49;00m[37m [39;49;00m[31manswer[39;49;00m[37m [39;49;00m[33m'scroll-other-window-down[39;49;00m)[37m[39;49;00m$
  2312^I[37m^I      [39;49;00m([36mignore-errors[39;49;00m[37m [39;49;00m([31mscroll-other-window-down[39;49;00m))[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
  2313^I[37m^I     [39;49;00m(([34mor[39;49;00m[37m [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[31manswer[39;49;00m[37m [39;49;00m'([31mexit-prefix[39;49;00m[37m [39;49;00m[31mquit[39;49;00m))[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m[33m?\e[39;49;00m))[37m[39;49;00m$
  2314^I[37m^I      [39;49;00m([32msignal[39;49;00m[37m [39;49;00m[33m'quit[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
  2315^I[37m^I     [39;49;00m([31mt[39;49;00m[37m [39;49;00m[31mt[39;49;00m)))[37m[39;49;00m$
  2316^I[37m        [39;49;00m([32mding[39;49;00m)[37m[39;49;00m$
  2317^I[37m        [39;49;00m([32mdiscard-input[39;49;00m))))[37m[39;49;00m$
  2318^I[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mret[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31manswer[39;49;00m[37m [39;49;00m[33m'act[39;49;00m)))[37m[39;49;00m$
  2319^I[37m      [39;49;00m([36munless[39;49;00m[37m [39;49;00m[31mnoninteractive[39;49;00m[37m[39;49;00m$
  2320^I[37m        [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m%s%c[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mret[39;49;00m[37m [39;49;00m[33m?y[39;49;00m[37m [39;49;00m[33m?n[39;49;00m)))[37m[39;49;00m$
  2321^I[37m      [39;49;00m[31mret[39;49;00m)))[37m[39;49;00m$
  2322^I[37m[39;49;00m$
  2323^I[37m[39;49;00m[37m[39;49;00m$
  2324^I[37m;;; Atomic change groups.[39;49;00m[37m[39;49;00m$
  2325^I[37m[39;49;00m$
  2326^I([36mdefmacro[39;49;00m[37m [39;49;00m[36matomic-change-group[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
  2327^I[37m  [39;49;00m[33m"[39;49;00m[33mPerform BODY as an atomic change group.[39;49;00m$
  2328^I[33mThis means that if BODY exits abnormally,[39;49;00m$
  2329^I[33mall of its changes to the current buffer are undone.[39;49;00m$
  2330^I[33mThis works regardless of whether undo is enabled in the buffer.[39;49;00m$
  2331^I[33m[39;49;00m$
  2332^I[33mThis mechanism is transparent to ordinary use of undo;[39;49;00m$
  2333^I[33mif undo is enabled in the buffer and BODY succeeds, the[39;49;00m$
  2334^I[33muser can undo the change normally.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2335^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
  2336^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mhandle[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m--change-group-handle--[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
  2337^I[37m^I[39;49;00m([31msuccess[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m--change-group-success--[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
  2338^I[37m    [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m((,[31mhandle[39;49;00m[37m [39;49;00m([31mprepare-change-group[39;49;00m))[37m[39;49;00m$
  2339^I[37m^I   [39;49;00m[37m;; Don't truncate any undo data in the middle of this.[39;49;00m[37m[39;49;00m$
  2340^I[37m^I   [39;49;00m([31mundo-outer-limit[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
  2341^I[37m^I   [39;49;00m([31mundo-limit[39;49;00m[37m [39;49;00m[31mmost-positive-fixnum[39;49;00m)[37m[39;49;00m$
  2342^I[37m^I   [39;49;00m([31mundo-strong-limit[39;49;00m[37m [39;49;00m[31mmost-positive-fixnum[39;49;00m)[37m[39;49;00m$
  2343^I[37m^I   [39;49;00m(,[31msuccess[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m$
  2344^I[37m       [39;49;00m([34munwind-protect[39;49;00m[37m[39;49;00m$
  2345^I[37m^I   [39;49;00m([34mprogn[39;49;00m[37m[39;49;00m$
  2346^I[37m^I     [39;49;00m[37m;; This is inside the unwind-protect because[39;49;00m[37m[39;49;00m$
  2347^I[37m^I     [39;49;00m[37m;; it enables undo if that was disabled; we need[39;49;00m[37m[39;49;00m$
  2348^I[37m^I     [39;49;00m[37m;; to make sure that it gets disabled again.[39;49;00m[37m[39;49;00m$
  2349^I[37m^I     [39;49;00m([31mactivate-change-group[39;49;00m[37m [39;49;00m,[31mhandle[39;49;00m)[37m[39;49;00m$
  2350^I[37m^I     [39;49;00m,@[31mbody[39;49;00m[37m[39;49;00m$
  2351^I[37m^I     [39;49;00m([34msetq[39;49;00m[37m [39;49;00m,[31msuccess[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
  2352^I[37m^I [39;49;00m[37m;; Either of these functions will disable undo[39;49;00m[37m[39;49;00m$
  2353^I[37m^I [39;49;00m[37m;; if it was disabled before.[39;49;00m[37m[39;49;00m$
  2354^I[37m^I [39;49;00m([34mif[39;49;00m[37m [39;49;00m,[31msuccess[39;49;00m[37m[39;49;00m$
  2355^I[37m^I     [39;49;00m([31maccept-change-group[39;49;00m[37m [39;49;00m,[31mhandle[39;49;00m)[37m[39;49;00m$
  2356^I[37m^I   [39;49;00m([31mcancel-change-group[39;49;00m[37m [39;49;00m,[31mhandle[39;49;00m))))))[37m[39;49;00m$
  2357^I[37m[39;49;00m$
  2358^I([36mdefun[39;49;00m[37m [39;49;00m[31mprepare-change-group[39;49;00m[37m [39;49;00m([34m&optional[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m)[37m[39;49;00m$
  2359^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn a handle for the current buffer's state, for a change group.[39;49;00m$
  2360^I[33mIf you specify BUFFER, make a handle for BUFFER's state instead.[39;49;00m$
  2361^I[33m[39;49;00m$
  2362^I[33mPass the handle to [39;49;00m[33m`activate-change-group'[39;49;00m[33m afterward to initiate[39;49;00m$
  2363^I[33mthe actual changes of the change group.[39;49;00m$
  2364^I[33m[39;49;00m$
  2365^I[33mTo finish the change group, call either [39;49;00m[33m`accept-change-group'[39;49;00m[33m or[39;49;00m$
  2366^I[33m`cancel-change-group'[39;49;00m[33m passing the same handle as argument.  Call[39;49;00m$
  2367^I[33m`accept-change-group'[39;49;00m[33m to accept the changes in the group as final;[39;49;00m$
  2368^I[33mcall [39;49;00m[33m`cancel-change-group'[39;49;00m[33m to undo them all.  You should use[39;49;00m$
  2369^I[33m`unwind-protect'[39;49;00m[33m to make sure the group is always finished.  The call[39;49;00m$
  2370^I[33mto [39;49;00m[33m`activate-change-group'[39;49;00m[33m should be inside the [39;49;00m[33m`unwind-protect'[39;49;00m[33m.[39;49;00m$
  2371^I[33mOnce you finish the group, don't use the handle again--don't try to[39;49;00m$
  2372^I[33mfinish the same group twice.  For a simple example of correct use, see[39;49;00m$
  2373^I[33mthe source code of [39;49;00m[33m`atomic-change-group'[39;49;00m[33m.[39;49;00m$
  2374^I[33m[39;49;00m$
  2375^I[33mThe handle records only the specified buffer.  To make a multibuffer[39;49;00m$
  2376^I[33mchange group, call this function once for each buffer you want to[39;49;00m$
  2377^I[33mcover, then use [39;49;00m[33m`nconc'[39;49;00m[33m to combine the returned values, like this:[39;49;00m$
  2378^I[33m[39;49;00m$
  2379^I[33m  (nconc (prepare-change-group buffer-1)[39;49;00m$
  2380^I[33m         (prepare-change-group buffer-2))[39;49;00m$
  2381^I[33m[39;49;00m$
  2382^I[33mYou can then activate that multibuffer change group with a single[39;49;00m$
  2383^I[33mcall to [39;49;00m[33m`activate-change-group'[39;49;00m[33m and finish it with a single call[39;49;00m$
  2384^I[33mto [39;49;00m[33m`accept-change-group'[39;49;00m[33m or [39;49;00m[33m`cancel-change-group'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2385^I[37m[39;49;00m$
  2386^I[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m[39;49;00m$
  2387^I[37m      [39;49;00m([32mlist[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m [39;49;00m([36mwith-current-buffer[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m [39;49;00m[31mbuffer-undo-list[39;49;00m)))[37m[39;49;00m$
  2388^I[37m    [39;49;00m([32mlist[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m([32mcurrent-buffer[39;49;00m)[37m [39;49;00m[31mbuffer-undo-list[39;49;00m))))[37m[39;49;00m$
  2389^I[37m[39;49;00m$
  2390^I([36mdefun[39;49;00m[37m [39;49;00m[31mactivate-change-group[39;49;00m[37m [39;49;00m([31mhandle[39;49;00m)[37m[39;49;00m$
  2391^I[37m  [39;49;00m[33m"[39;49;00m[33mActivate a change group made with [39;49;00m[33m`prepare-change-group'[39;49;00m[33m (which see).[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2392^I[37m  [39;49;00m([36mdolist[39;49;00m[37m [39;49;00m([32melt[39;49;00m[37m [39;49;00m[31mhandle[39;49;00m)[37m[39;49;00m$
  2393^I[37m    [39;49;00m([36mwith-current-buffer[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[32melt[39;49;00m)[37m[39;49;00m$
  2394^I[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mbuffer-undo-list[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
  2395^I[37m^I  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbuffer-undo-list[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)))))[37m[39;49;00m$
  2396^I[37m[39;49;00m$
  2397^I([36mdefun[39;49;00m[37m [39;49;00m[31maccept-change-group[39;49;00m[37m [39;49;00m([31mhandle[39;49;00m)[37m[39;49;00m$
  2398^I[37m  [39;49;00m[33m"[39;49;00m[33mFinish a change group made with [39;49;00m[33m`prepare-change-group'[39;49;00m[33m (which see).[39;49;00m$
  2399^I[33mThis finishes the change group by accepting its changes as final.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2400^I[37m  [39;49;00m([36mdolist[39;49;00m[37m [39;49;00m([32melt[39;49;00m[37m [39;49;00m[31mhandle[39;49;00m)[37m[39;49;00m$
  2401^I[37m    [39;49;00m([36mwith-current-buffer[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[32melt[39;49;00m)[37m[39;49;00m$
  2402^I[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[32melt[39;49;00m)[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
  2403^I[37m^I  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbuffer-undo-list[39;49;00m[37m [39;49;00m[31mt[39;49;00m)))))[37m[39;49;00m$
  2404^I[37m[39;49;00m$
  2405^I([36mdefun[39;49;00m[37m [39;49;00m[31mcancel-change-group[39;49;00m[37m [39;49;00m([31mhandle[39;49;00m)[37m[39;49;00m$
  2406^I[37m  [39;49;00m[33m"[39;49;00m[33mFinish a change group made with [39;49;00m[33m`prepare-change-group'[39;49;00m[33m (which see).[39;49;00m$
  2407^I[33mThis finishes the change group by reverting all of its changes.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2408^I[37m  [39;49;00m([36mdolist[39;49;00m[37m [39;49;00m([32melt[39;49;00m[37m [39;49;00m[31mhandle[39;49;00m)[37m[39;49;00m$
  2409^I[37m    [39;49;00m([36mwith-current-buffer[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[32melt[39;49;00m)[37m[39;49;00m$
  2410^I[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[32melt[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[32melt[39;49;00m))[37m[39;49;00m$
  2411^I[37m      [39;49;00m([34msave-restriction[39;49;00m[37m[39;49;00m$
  2412^I[37m^I[39;49;00m[37m;; Widen buffer temporarily so if the buffer was narrowed within[39;49;00m[37m[39;49;00m$
  2413^I[37m^I[39;49;00m[37m;; the body of `atomic-change-group' all changes can be undone.[39;49;00m[37m[39;49;00m$
  2414^I[37m^I[39;49;00m([32mwiden[39;49;00m)[37m[39;49;00m$
  2415^I[37m^I[39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mold-car[39;49;00m[37m[39;49;00m$
  2416^I[37m^I       [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[32melt[39;49;00m)[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[32melt[39;49;00m)))[37m[39;49;00m$
  2417^I[37m^I      [39;49;00m([31mold-cdr[39;49;00m[37m[39;49;00m$
  2418^I[37m^I       [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[32melt[39;49;00m)[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[32melt[39;49;00m))))[37m[39;49;00m$
  2419^I[37m^I  [39;49;00m[37m;; Temporarily truncate the undo log at ELT.[39;49;00m[37m[39;49;00m$
  2420^I[37m^I  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[32melt[39;49;00m)[37m[39;49;00m$
  2421^I[37m^I    [39;49;00m([32msetcar[39;49;00m[37m [39;49;00m[32melt[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m [39;49;00m([32msetcdr[39;49;00m[37m [39;49;00m[32melt[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m$
  2422^I[37m^I  [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mlast-command[39;49;00m[37m [39;49;00m[33m'undo[39;49;00m)[37m [39;49;00m([31mundo-start[39;49;00m))[37m[39;49;00m$
  2423^I[37m^I  [39;49;00m[37m;; Make sure there's no confusion.[39;49;00m[37m[39;49;00m$
  2424^I[37m^I  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[32melt[39;49;00m)[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[32melt[39;49;00m[37m [39;49;00m([31mlast[39;49;00m[37m [39;49;00m[31mpending-undo-list[39;49;00m))))[37m[39;49;00m$
  2425^I[37m^I    [39;49;00m([36merror[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mUndoing to some unrelated state[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
  2426^I[37m^I  [39;49;00m[37m;; Undo it all.[39;49;00m[37m[39;49;00m$
  2427^I[37m^I  [39;49;00m([34msave-excursion[39;49;00m[37m[39;49;00m$
  2428^I[37m^I    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32mlistp[39;49;00m[37m [39;49;00m[31mpending-undo-list[39;49;00m)[37m [39;49;00m([31mundo-more[39;49;00m[37m [39;49;00m[34m1[39;49;00m)))[37m[39;49;00m$
  2429^I[37m^I  [39;49;00m[37m;; Reset the modified cons cell ELT to its original content.[39;49;00m[37m[39;49;00m$
  2430^I[37m^I  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[32melt[39;49;00m)[37m[39;49;00m$
  2431^I[37m^I    [39;49;00m([32msetcar[39;49;00m[37m [39;49;00m[32melt[39;49;00m[37m [39;49;00m[31mold-car[39;49;00m)[37m[39;49;00m$
  2432^I[37m^I    [39;49;00m([32msetcdr[39;49;00m[37m [39;49;00m[32melt[39;49;00m[37m [39;49;00m[31mold-cdr[39;49;00m))[37m[39;49;00m$
  2433^I[37m^I  [39;49;00m[37m;; Revert the undo info to what it was when we grabbed the state.[39;49;00m[37m[39;49;00m$
  2434^I[37m^I  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbuffer-undo-list[39;49;00m[37m [39;49;00m[32melt[39;49;00m))))))[37m[39;49;00m$
  2435^I[37m[39;49;00m[37m[39;49;00m$
  2436^I[37m;;;; Display-related functions.[39;49;00m[37m[39;49;00m$
  2437^I[37m[39;49;00m$
  2438^I[37m;; For compatibility.[39;49;00m[37m[39;49;00m$
  2439^I([36mdefine-obsolete-function-alias[39;49;00m[37m [39;49;00m[33m'redraw-modeline[39;49;00m[37m[39;49;00m$
  2440^I[37m  [39;49;00m[33m'force-mode-line-update[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m24.3[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  2441^I[37m[39;49;00m$
  2442^I([36mdefun[39;49;00m[37m [39;49;00m[31mmomentary-string-display[39;49;00m[37m [39;49;00m([32mstring[39;49;00m[37m [39;49;00m[31mpos[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mexit-char[39;49;00m[37m [39;49;00m[32mmessage[39;49;00m)[37m[39;49;00m$
  2443^I[37m  [39;49;00m[33m"[39;49;00m[33mMomentarily display STRING in the buffer at POS.[39;49;00m$
  2444^I[33mDisplay remains until next event is input.[39;49;00m$
  2445^I[33mIf POS is a marker, only its position is used; its buffer is ignored.[39;49;00m$
  2446^I[33mOptional third arg EXIT-CHAR can be a character, event or event[39;49;00m$
  2447^I[33mdescription list.  EXIT-CHAR defaults to SPC.  If the input is[39;49;00m$
  2448^I[33mEXIT-CHAR it is swallowed; otherwise it is then available as[39;49;00m$
  2449^I[33minput (as a command if nothing else).[39;49;00m$
  2450^I[33mDisplay MESSAGE (optional fourth arg) in the echo area.[39;49;00m$
  2451^I[33mIf MESSAGE is nil, instructions to type EXIT-CHAR are displayed there.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2452^I[37m  [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mexit-char[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mexit-char[39;49;00m[37m [39;49;00m[33m?\s[39;49;00m))[37m[39;49;00m$
  2453^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mol[39;49;00m[37m [39;49;00m([32mmake-overlay[39;49;00m[37m [39;49;00m[31mpos[39;49;00m[37m [39;49;00m[31mpos[39;49;00m))[37m[39;49;00m$
  2454^I[37m        [39;49;00m([31mstr[39;49;00m[37m [39;49;00m([32mcopy-sequence[39;49;00m[37m [39;49;00m[32mstring[39;49;00m)))[37m[39;49;00m$
  2455^I[37m    [39;49;00m([34munwind-protect[39;49;00m[37m[39;49;00m$
  2456^I[37m        [39;49;00m([34mprogn[39;49;00m[37m[39;49;00m$
  2457^I[37m          [39;49;00m([34msave-excursion[39;49;00m[37m[39;49;00m$
  2458^I[37m            [39;49;00m([32moverlay-put[39;49;00m[37m [39;49;00m[31mol[39;49;00m[37m [39;49;00m[33m'after-string[39;49;00m[37m [39;49;00m[31mstr[39;49;00m)[37m[39;49;00m$
  2459^I[37m            [39;49;00m([32mgoto-char[39;49;00m[37m [39;49;00m[31mpos[39;49;00m)[37m[39;49;00m$
  2460^I[37m            [39;49;00m[37m;; To avoid trouble with out-of-bounds position[39;49;00m[37m[39;49;00m$
  2461^I[37m            [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mpos[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m))[37m[39;49;00m$
  2462^I[37m            [39;49;00m[37m;; If the string end is off screen, recenter now.[39;49;00m[37m[39;49;00m$
  2463^I[37m            [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32m<=[39;49;00m[37m [39;49;00m([32mwindow-end[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m [39;49;00m[31mpos[39;49;00m)[37m[39;49;00m$
  2464^I[37m                [39;49;00m([32mrecenter[39;49;00m[37m [39;49;00m([32m/[39;49;00m[37m [39;49;00m([31mwindow-height[39;49;00m)[37m [39;49;00m[34m2[39;49;00m))))[37m[39;49;00m$
  2465^I[37m          [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[32mmessage[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mType %s to continue editing.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  2466^I[37m                   [39;49;00m([32msingle-key-description[39;49;00m[37m [39;49;00m[31mexit-char[39;49;00m))[37m[39;49;00m$
  2467^I[37m^I  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mevent[39;49;00m[37m [39;49;00m([31mread-key[39;49;00m)))[37m[39;49;00m$
  2468^I[37m^I    [39;49;00m[37m;; `exit-char' can be an event, or an event description list.[39;49;00m[37m[39;49;00m$
  2469^I[37m^I    [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mevent[39;49;00m[37m [39;49;00m[31mexit-char[39;49;00m)[37m[39;49;00m$
  2470^I[37m^I^I[39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mevent[39;49;00m[37m [39;49;00m([32mevent-convert-list[39;49;00m[37m [39;49;00m[31mexit-char[39;49;00m))[37m[39;49;00m$
  2471^I[37m^I^I[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31munread-command-events[39;49;00m[37m[39;49;00m$
  2472^I[37m                      [39;49;00m([32mappend[39;49;00m[37m [39;49;00m([32mthis-single-command-raw-keys[39;49;00m))))))[37m[39;49;00m$
  2473^I[37m      [39;49;00m([32mdelete-overlay[39;49;00m[37m [39;49;00m[31mol[39;49;00m))))[37m[39;49;00m$
  2474^I[37m[39;49;00m$
  2475^I[37m[39;49;00m[37m[39;49;00m$
  2476^I[37m;;;; Overlay operations[39;49;00m[37m[39;49;00m$
  2477^I[37m[39;49;00m$
  2478^I([36mdefun[39;49;00m[37m [39;49;00m[31mcopy-overlay[39;49;00m[37m [39;49;00m([31mo[39;49;00m)[37m[39;49;00m$
  2479^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn a copy of overlay O.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2480^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mo1[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32moverlay-buffer[39;49;00m[37m [39;49;00m[31mo[39;49;00m)[37m[39;49;00m$
  2481^I[37m                [39;49;00m([32mmake-overlay[39;49;00m[37m [39;49;00m([32moverlay-start[39;49;00m[37m [39;49;00m[31mo[39;49;00m)[37m [39;49;00m([32moverlay-end[39;49;00m[37m [39;49;00m[31mo[39;49;00m)[37m[39;49;00m$
  2482^I[37m                              [39;49;00m[37m;; FIXME: there's no easy way to find the[39;49;00m[37m[39;49;00m$
  2483^I[37m                              [39;49;00m[37m;; insertion-type of the two markers.[39;49;00m[37m[39;49;00m$
  2484^I[37m                              [39;49;00m([32moverlay-buffer[39;49;00m[37m [39;49;00m[31mo[39;49;00m))[37m[39;49;00m$
  2485^I[37m              [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mo1[39;49;00m[37m [39;49;00m([32mmake-overlay[39;49;00m[37m [39;49;00m([32mpoint-min[39;49;00m)[37m [39;49;00m([32mpoint-min[39;49;00m))))[37m[39;49;00m$
  2486^I[37m                [39;49;00m([32mdelete-overlay[39;49;00m[37m [39;49;00m[31mo1[39;49;00m)[37m[39;49;00m$
  2487^I[37m                [39;49;00m[31mo1[39;49;00m)))[37m[39;49;00m$
  2488^I[37m^I[39;49;00m([31mprops[39;49;00m[37m [39;49;00m([32moverlay-properties[39;49;00m[37m [39;49;00m[31mo[39;49;00m)))[37m[39;49;00m$
  2489^I[37m    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m[31mprops[39;49;00m[37m[39;49;00m$
  2490^I[37m      [39;49;00m([32moverlay-put[39;49;00m[37m [39;49;00m[31mo1[39;49;00m[37m [39;49;00m([36mpop[39;49;00m[37m [39;49;00m[31mprops[39;49;00m)[37m [39;49;00m([36mpop[39;49;00m[37m [39;49;00m[31mprops[39;49;00m)))[37m[39;49;00m$
  2491^I[37m    [39;49;00m[31mo1[39;49;00m))[37m[39;49;00m$
  2492^I[37m[39;49;00m$
  2493^I([36mdefun[39;49;00m[37m [39;49;00m[31mremove-overlays[39;49;00m[37m [39;49;00m([34m&optional[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[31mname[39;49;00m[37m [39;49;00m[31mval[39;49;00m)[37m[39;49;00m$
  2494^I[37m  [39;49;00m[33m"[39;49;00m[33mClear BEG and END of overlays whose property NAME has value VAL.[39;49;00m$
  2495^I[33mOverlays might be moved and/or split.[39;49;00m$
  2496^I[33mBEG and END default respectively to the beginning and end of buffer.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2497^I[37m  [39;49;00m[37m;; This speeds up the loops over overlays.[39;49;00m[37m[39;49;00m$
  2498^I[37m  [39;49;00m([36munless[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m[37m [39;49;00m([32mpoint-min[39;49;00m)))[37m[39;49;00m$
  2499^I[37m  [39;49;00m([36munless[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m([32mpoint-max[39;49;00m)))[37m[39;49;00m$
  2500^I[37m  [39;49;00m([32moverlay-recenter[39;49;00m[37m [39;49;00m[31mend[39;49;00m)[37m[39;49;00m$
  2501^I[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m)[37m[39;49;00m$
  2502^I[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m[37m [39;49;00m([34mprog1[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m))))[37m[39;49;00m$
  2503^I[37m  [39;49;00m([34msave-excursion[39;49;00m[37m[39;49;00m$
  2504^I[37m    [39;49;00m([36mdolist[39;49;00m[37m [39;49;00m([31mo[39;49;00m[37m [39;49;00m([32moverlays-in[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m[37m [39;49;00m[31mend[39;49;00m))[37m[39;49;00m$
  2505^I[37m      [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32moverlay-get[39;49;00m[37m [39;49;00m[31mo[39;49;00m[37m [39;49;00m[31mname[39;49;00m)[37m [39;49;00m[31mval[39;49;00m)[37m[39;49;00m$
  2506^I[37m^I[39;49;00m[37m;; Either push this overlay outside beg...end[39;49;00m[37m[39;49;00m$
  2507^I[37m^I[39;49;00m[37m;; or split it to exclude beg...end[39;49;00m[37m[39;49;00m$
  2508^I[37m^I[39;49;00m[37m;; or delete it entirely (if it is contained in beg...end).[39;49;00m[37m[39;49;00m$
  2509^I[37m^I[39;49;00m([34mif[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m([32moverlay-start[39;49;00m[37m [39;49;00m[31mo[39;49;00m)[37m [39;49;00m[31mbeg[39;49;00m)[37m[39;49;00m$
  2510^I[37m^I    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m([32moverlay-end[39;49;00m[37m [39;49;00m[31mo[39;49;00m)[37m [39;49;00m[31mend[39;49;00m)[37m[39;49;00m$
  2511^I[37m^I^I[39;49;00m([34mprogn[39;49;00m[37m[39;49;00m$
  2512^I[37m^I^I  [39;49;00m([32mmove-overlay[39;49;00m[37m [39;49;00m([31mcopy-overlay[39;49;00m[37m [39;49;00m[31mo[39;49;00m)[37m[39;49;00m$
  2513^I[37m^I^I^I^I[39;49;00m([32moverlay-start[39;49;00m[37m [39;49;00m[31mo[39;49;00m)[37m [39;49;00m[31mbeg[39;49;00m)[37m[39;49;00m$
  2514^I[37m^I^I  [39;49;00m([32mmove-overlay[39;49;00m[37m [39;49;00m[31mo[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m([32moverlay-end[39;49;00m[37m [39;49;00m[31mo[39;49;00m)))[37m[39;49;00m$
  2515^I[37m^I      [39;49;00m([32mmove-overlay[39;49;00m[37m [39;49;00m[31mo[39;49;00m[37m [39;49;00m([32moverlay-start[39;49;00m[37m [39;49;00m[31mo[39;49;00m)[37m [39;49;00m[31mbeg[39;49;00m))[37m[39;49;00m$
  2516^I[37m^I  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m([32moverlay-end[39;49;00m[37m [39;49;00m[31mo[39;49;00m)[37m [39;49;00m[31mend[39;49;00m)[37m[39;49;00m$
  2517^I[37m^I      [39;49;00m([32mmove-overlay[39;49;00m[37m [39;49;00m[31mo[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m([32moverlay-end[39;49;00m[37m [39;49;00m[31mo[39;49;00m))[37m[39;49;00m$
  2518^I[37m^I    [39;49;00m([32mdelete-overlay[39;49;00m[37m [39;49;00m[31mo[39;49;00m)))))))[37m[39;49;00m$
  2519^I[37m[39;49;00m[37m[39;49;00m$
  2520^I[37m;;;; Miscellanea.[39;49;00m[37m[39;49;00m$
  2521^I[37m[39;49;00m$
  2522^I([34mdefvar[39;49;00m[37m [39;49;00m[31msuspend-hook[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m$
  2523^I[37m  [39;49;00m[33m"[39;49;00m[33mNormal hook run by [39;49;00m[33m`suspend-emacs'[39;49;00m[33m, before suspending.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  2524^I[37m[39;49;00m$
  2525^I([34mdefvar[39;49;00m[37m [39;49;00m[31msuspend-resume-hook[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m$
  2526^I[37m  [39;49;00m[33m"[39;49;00m[33mNormal hook run by [39;49;00m[33m`suspend-emacs'[39;49;00m[33m, after Emacs is continued.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  2527^I[37m[39;49;00m$
  2528^I([34mdefvar[39;49;00m[37m [39;49;00m[31mtemp-buffer-show-hook[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m$
  2529^I[37m  [39;49;00m[33m"[39;49;00m[33mNormal hook run by [39;49;00m[33m`with-output-to-temp-buffer'[39;49;00m[33m after displaying the buffer.[39;49;00m$
  2530^I[33mWhen the hook runs, the temporary buffer is current, and the window it[39;49;00m$
  2531^I[33mwas displayed in is selected.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  2532^I[37m[39;49;00m$
  2533^I([34mdefvar[39;49;00m[37m [39;49;00m[31mtemp-buffer-setup-hook[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m$
  2534^I[37m  [39;49;00m[33m"[39;49;00m[33mNormal hook run by [39;49;00m[33m`with-output-to-temp-buffer'[39;49;00m[33m at the start.[39;49;00m$
  2535^I[33mWhen the hook runs, the temporary buffer is current.[39;49;00m$
  2536^I[33mThis hook is normally set up with a function to put the buffer in Help[39;49;00m$
  2537^I[33mmode.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  2538^I[37m[39;49;00m$
  2539^I([34mdefconst[39;49;00m[37m [39;49;00m[31muser-emacs-directory[39;49;00m[37m[39;49;00m$
  2540^I[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31msystem-type[39;49;00m[37m [39;49;00m[33m'ms-dos[39;49;00m)[37m[39;49;00m$
  2541^I[37m      [39;49;00m[37m;; MS-DOS cannot have initial dot.[39;49;00m[37m[39;49;00m$
  2542^I[37m      [39;49;00m[33m"[39;49;00m[33m~/_emacs.d/[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2543^I[37m    [39;49;00m[33m"[39;49;00m[33m~/.emacs.d/[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  2544^I[37m  [39;49;00m[33m"[39;49;00m[33mDirectory beneath which additional per-user Emacs-specific files are placed.[39;49;00m$
  2545^I[33mVarious programs in Emacs store information in this directory.[39;49;00m$
  2546^I[33mNote that this should end with a directory separator.[39;49;00m$
  2547^I[33mSee also [39;49;00m[33m`locate-user-emacs-file'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  2548^I[37m[39;49;00m[37m[39;49;00m$
  2549^I[37m;;;; Misc. useful functions.[39;49;00m[37m[39;49;00m$
  2550^I[37m[39;49;00m$
  2551^I([36mdefsubst[39;49;00m[37m [39;49;00m[31mbuffer-narrowed-p[39;49;00m[37m [39;49;00m()[37m[39;49;00m$
  2552^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn non-nil if the current buffer is narrowed.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2553^I[37m  [39;49;00m([32m/=[39;49;00m[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m([32mpoint-max[39;49;00m)[37m [39;49;00m([32mpoint-min[39;49;00m))[37m [39;49;00m([32mbuffer-size[39;49;00m)))[37m[39;49;00m$
  2554^I[37m[39;49;00m$
  2555^I([36mdefun[39;49;00m[37m [39;49;00m[31mfind-tag-default-bounds[39;49;00m[37m [39;49;00m()[37m[39;49;00m$
  2556^I[37m  [39;49;00m[33m"[39;49;00m[33mDetermine the boundaries of the default tag, based on text at point.[39;49;00m$
  2557^I[33mReturn a cons cell with the beginning and end of the found tag.[39;49;00m$
  2558^I[33mIf there is no plausible default, return nil.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2559^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m([31mfrom[39;49;00m[37m [39;49;00m[31mto[39;49;00m[37m [39;49;00m[31mbound[39;49;00m)[37m[39;49;00m$
  2560^I[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([34mprogn[39;49;00m[37m[39;49;00m$
  2561^I[37m^I^I[39;49;00m[37m;; Look at text around `point'.[39;49;00m[37m[39;49;00m$
  2562^I[37m^I^I[39;49;00m([34msave-excursion[39;49;00m[37m[39;49;00m$
  2563^I[37m^I^I  [39;49;00m([32mskip-syntax-backward[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mw_[39;49;00m[33m"[39;49;00m)[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mfrom[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m)))[37m[39;49;00m$
  2564^I[37m^I^I[39;49;00m([34msave-excursion[39;49;00m[37m[39;49;00m$
  2565^I[37m^I^I  [39;49;00m([32mskip-syntax-forward[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mw_[39;49;00m[33m"[39;49;00m)[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mto[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m)))[37m[39;49;00m$
  2566^I[37m^I^I[39;49;00m([32m>[39;49;00m[37m [39;49;00m[31mto[39;49;00m[37m [39;49;00m[31mfrom[39;49;00m))[37m[39;49;00m$
  2567^I[37m^I      [39;49;00m[37m;; Look between `line-beginning-position' and `point'.[39;49;00m[37m[39;49;00m$
  2568^I[37m^I      [39;49;00m([34msave-excursion[39;49;00m[37m[39;49;00m$
  2569^I[37m^I^I[39;49;00m([34mand[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbound[39;49;00m[37m [39;49;00m([32mline-beginning-position[39;49;00m))[37m[39;49;00m$
  2570^I[37m^I^I     [39;49;00m([32mskip-syntax-backward[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m^w_[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mbound[39;49;00m)[37m[39;49;00m$
  2571^I[37m^I^I     [39;49;00m([32m>[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mto[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m))[37m [39;49;00m[31mbound[39;49;00m)[37m[39;49;00m$
  2572^I[37m^I^I     [39;49;00m([32mskip-syntax-backward[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mw_[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  2573^I[37m^I^I     [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mfrom[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m))))[37m[39;49;00m$
  2574^I[37m^I      [39;49;00m[37m;; Look between `point' and `line-end-position'.[39;49;00m[37m[39;49;00m$
  2575^I[37m^I      [39;49;00m([34msave-excursion[39;49;00m[37m[39;49;00m$
  2576^I[37m^I^I[39;49;00m([34mand[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbound[39;49;00m[37m [39;49;00m([32mline-end-position[39;49;00m))[37m[39;49;00m$
  2577^I[37m^I^I     [39;49;00m([32mskip-syntax-forward[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m^w_[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mbound[39;49;00m)[37m[39;49;00m$
  2578^I[37m^I^I     [39;49;00m([32m<[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mfrom[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m))[37m [39;49;00m[31mbound[39;49;00m)[37m[39;49;00m$
  2579^I[37m^I^I     [39;49;00m([32mskip-syntax-forward[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mw_[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  2580^I[37m^I^I     [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mto[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m)))))[37m[39;49;00m$
  2581^I[37m      [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mfrom[39;49;00m[37m [39;49;00m[31mto[39;49;00m))))[37m[39;49;00m$
  2582^I[37m[39;49;00m$
  2583^I([36mdefun[39;49;00m[37m [39;49;00m[31mfind-tag-default[39;49;00m[37m [39;49;00m()[37m[39;49;00m$
  2584^I[37m  [39;49;00m[33m"[39;49;00m[33mDetermine default tag to search for, based on text at point.[39;49;00m$
  2585^I[33mIf there is no plausible default, return nil.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2586^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mbounds[39;49;00m[37m [39;49;00m([31mfind-tag-default-bounds[39;49;00m)))[37m[39;49;00m$
  2587^I[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31mbounds[39;49;00m[37m[39;49;00m$
  2588^I[37m      [39;49;00m([32mbuffer-substring-no-properties[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mbounds[39;49;00m)[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mbounds[39;49;00m)))))[37m[39;49;00m$
  2589^I[37m[39;49;00m$
  2590^I([36mdefun[39;49;00m[37m [39;49;00m[31mfind-tag-default-as-regexp[39;49;00m[37m [39;49;00m()[37m[39;49;00m$
  2591^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn regexp that matches the default tag at point.[39;49;00m$
  2592^I[33mIf there is no tag at point, return nil.[39;49;00m$
  2593^I[33m[39;49;00m$
  2594^I[33mWhen in a major mode that does not provide its own[39;49;00m$
  2595^I[33m`find-tag-default-function'[39;49;00m[33m, return a regexp that matches the[39;49;00m$
  2596^I[33msymbol at point exactly.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2597^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtag[39;49;00m[37m [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mfind-tag-default-function[39;49;00m[37m[39;49;00m$
  2598^I[37m^I^I^I  [39;49;00m([32mget[39;49;00m[37m [39;49;00m[31mmajor-mode[39;49;00m[37m [39;49;00m[33m'find-tag-default-function[39;49;00m)[37m[39;49;00m$
  2599^I[37m^I^I^I  [39;49;00m[33m'find-tag-default[39;49;00m))))[37m[39;49;00m$
  2600^I[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mtag[39;49;00m[37m [39;49;00m([32mregexp-quote[39;49;00m[37m [39;49;00m[31mtag[39;49;00m))))[37m[39;49;00m$
  2601^I[37m[39;49;00m$
  2602^I([36mdefun[39;49;00m[37m [39;49;00m[31mfind-tag-default-as-symbol-regexp[39;49;00m[37m [39;49;00m()[37m[39;49;00m$
  2603^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn regexp that matches the default tag at point as symbol.[39;49;00m$
  2604^I[33mIf there is no tag at point, return nil.[39;49;00m$
  2605^I[33m[39;49;00m$
  2606^I[33mWhen in a major mode that does not provide its own[39;49;00m$
  2607^I[33m`find-tag-default-function'[39;49;00m[33m, return a regexp that matches the[39;49;00m$
  2608^I[33msymbol at point exactly.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2609^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtag-regexp[39;49;00m[37m [39;49;00m([31mfind-tag-default-as-regexp[39;49;00m)))[37m[39;49;00m$
  2610^I[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mtag-regexp[39;49;00m[37m[39;49;00m$
  2611^I[37m^I     [39;49;00m([32meq[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mfind-tag-default-function[39;49;00m[37m[39;49;00m$
  2612^I[37m^I^I     [39;49;00m([32mget[39;49;00m[37m [39;49;00m[31mmajor-mode[39;49;00m[37m [39;49;00m[33m'find-tag-default-function[39;49;00m)[37m[39;49;00m$
  2613^I[37m^I^I     [39;49;00m[33m'find-tag-default[39;49;00m)[37m[39;49;00m$
  2614^I[37m^I^I [39;49;00m[33m'find-tag-default[39;49;00m))[37m[39;49;00m$
  2615^I[37m^I[39;49;00m([32mformat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m_<%s[39;49;00m[33m\\[39;49;00m[33m_>[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mtag-regexp[39;49;00m)[37m[39;49;00m$
  2616^I[37m      [39;49;00m[31mtag-regexp[39;49;00m)))[37m[39;49;00m$
  2617^I[37m[39;49;00m$
  2618^I([36mdefun[39;49;00m[37m [39;49;00m[31mplay-sound[39;49;00m[37m [39;49;00m([31msound[39;49;00m)[37m[39;49;00m$
  2619^I[37m  [39;49;00m[33m"[39;49;00m[33mSOUND is a list of the form [39;49;00m[33m`[39;49;00m[33m(sound KEYWORD VALUE...)'.[39;49;00m$
  2620^I[33mThe following keywords are recognized:[39;49;00m$
  2621^I[33m[39;49;00m$
  2622^I[33m  :file FILE - read sound data from FILE.  If FILE isn't an[39;49;00m$
  2623^I[33mabsolute file name, it is searched in [39;49;00m[33m`data-directory'[39;49;00m[33m.[39;49;00m$
  2624^I[33m[39;49;00m$
  2625^I[33m  :data DATA - read sound data from string DATA.[39;49;00m$
  2626^I[33m[39;49;00m$
  2627^I[33mExactly one of :file or :data must be present.[39;49;00m$
  2628^I[33m[39;49;00m$
  2629^I[33m  :volume VOL - set volume to VOL.  VOL must an integer in the[39;49;00m$
  2630^I[33mrange 0..100 or a float in the range 0..1.0.  If not specified,[39;49;00m$
  2631^I[33mdon't change the volume setting of the sound device.[39;49;00m$
  2632^I[33m[39;49;00m$
  2633^I[33m  :device DEVICE - play sound on DEVICE.  If not specified,[39;49;00m$
  2634^I[33ma system-dependent default device name is used.[39;49;00m$
  2635^I[33m[39;49;00m$
  2636^I[33mNote: :data and :device are currently not supported on Windows.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2637^I[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mfboundp[39;49;00m[37m [39;49;00m[33m'play-sound-internal[39;49;00m)[37m[39;49;00m$
  2638^I[37m      [39;49;00m([32mplay-sound-internal[39;49;00m[37m [39;49;00m[31msound[39;49;00m)[37m[39;49;00m$
  2639^I[37m    [39;49;00m([36merror[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mThis Emacs binary lacks sound support[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
  2640^I[37m[39;49;00m$
  2641^I([36mdeclare-function[39;49;00m[37m [39;49;00m[31mw32-shell-dos-semantics[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mw32-fns[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
  2642^I[37m[39;49;00m$
  2643^I([36mdefun[39;49;00m[37m [39;49;00m[31mshell-quote-argument[39;49;00m[37m [39;49;00m([31margument[39;49;00m)[37m[39;49;00m$
  2644^I[37m  [39;49;00m[33m"[39;49;00m[33mQuote ARGUMENT for passing as argument to an inferior shell.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2645^I[37m  [39;49;00m([34mcond[39;49;00m[37m[39;49;00m$
  2646^I[37m   [39;49;00m(([32meq[39;49;00m[37m [39;49;00m[31msystem-type[39;49;00m[37m [39;49;00m[33m'ms-dos[39;49;00m)[37m[39;49;00m$
  2647^I[37m    [39;49;00m[37m;; Quote using double quotes, but escape any existing quotes in[39;49;00m[37m[39;49;00m$
  2648^I[37m    [39;49;00m[37m;; the argument with backslashes.[39;49;00m[37m[39;49;00m$
  2649^I[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mresult[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  2650^I[37m          [39;49;00m([31mstart[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  2651^I[37m          [39;49;00m[31mend[39;49;00m)[37m[39;49;00m$
  2652^I[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m[^[39;49;00m[33m\"[39;49;00m[33m][39;49;00m[33m"[39;49;00m[37m [39;49;00m[31margument[39;49;00m))[37m[39;49;00m$
  2653^I[37m              [39;49;00m([32m<[39;49;00m[37m [39;49;00m([32mmatch-end[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31margument[39;49;00m)))[37m[39;49;00m$
  2654^I[37m          [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m[[39;49;00m[33m\"[39;49;00m[33m][39;49;00m[33m"[39;49;00m[37m [39;49;00m[31margument[39;49;00m[37m [39;49;00m[31mstart[39;49;00m)[37m[39;49;00m$
  2655^I[37m            [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m([32mmatch-beginning[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  2656^I[37m                  [39;49;00m[31mresult[39;49;00m[37m [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[31mresult[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[31margument[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mend[39;49;00m)[37m[39;49;00m$
  2657^I[37m                                 [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m"[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[31margument[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m([32m1+[39;49;00m[37m [39;49;00m[31mend[39;49;00m)))[37m[39;49;00m$
  2658^I[37m                  [39;49;00m[31mstart[39;49;00m[37m [39;49;00m([32m1+[39;49;00m[37m [39;49;00m[31mend[39;49;00m))))[37m[39;49;00m$
  2659^I[37m      [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mresult[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[31margument[39;49;00m[37m [39;49;00m[31mstart[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
  2660^I[37m[39;49;00m$
  2661^I[37m   [39;49;00m(([34mand[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31msystem-type[39;49;00m[37m [39;49;00m[33m'windows-nt[39;49;00m)[37m [39;49;00m([31mw32-shell-dos-semantics[39;49;00m))[37m[39;49;00m$
  2662^I[37m[39;49;00m$
  2663^I[37m    [39;49;00m[37m;; First, quote argument so that CommandLineToArgvW will[39;49;00m[37m[39;49;00m$
  2664^I[37m    [39;49;00m[37m;; understand it.  See[39;49;00m[37m[39;49;00m$
  2665^I[37m    [39;49;00m[37m;; http://msdn.microsoft.com/en-us/library/17w5ykft%28v=vs.85%29.aspx[39;49;00m[37m[39;49;00m$
  2666^I[37m    [39;49;00m[37m;; After we perform that level of quoting, escape shell[39;49;00m[37m[39;49;00m$
  2667^I[37m    [39;49;00m[37m;; metacharacters so that cmd won't mangle our argument.  If the[39;49;00m[37m[39;49;00m$
  2668^I[37m    [39;49;00m[37m;; argument contains no double quote characters, we can just[39;49;00m[37m[39;49;00m$
  2669^I[37m    [39;49;00m[37m;; surround it with double quotes.  Otherwise, we need to prefix[39;49;00m[37m[39;49;00m$
  2670^I[37m    [39;49;00m[37m;; each shell metacharacter with a caret.[39;49;00m[37m[39;49;00m$
  2671^I[37m[39;49;00m$
  2672^I[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31margument[39;49;00m[37m[39;49;00m$
  2673^I[37m          [39;49;00m[37m;; escape backslashes at end of string[39;49;00m[37m[39;49;00m$
  2674^I[37m          [39;49;00m([31mreplace-regexp-in-string[39;49;00m[37m[39;49;00m$
  2675^I[37m           [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m([39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m*[39;49;00m[33m\\[39;49;00m[33m)$[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2676^I[37m           [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m1[39;49;00m[33m\\[39;49;00m[33m1[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2677^I[37m           [39;49;00m[37m;; escape backslashes and quotes in string body[39;49;00m[37m[39;49;00m$
  2678^I[37m           [39;49;00m([31mreplace-regexp-in-string[39;49;00m[37m[39;49;00m$
  2679^I[37m            [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m([39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m*[39;49;00m[33m\\[39;49;00m[33m)[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2680^I[37m            [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m1[39;49;00m[33m\\[39;49;00m[33m1[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2681^I[37m            [39;49;00m[31margument[39;49;00m)))[37m[39;49;00m$
  2682^I[37m[39;49;00m$
  2683^I[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m[%![39;49;00m[33m\"[39;49;00m[33m][39;49;00m[33m"[39;49;00m[37m [39;49;00m[31margument[39;49;00m)[37m[39;49;00m$
  2684^I[37m        [39;49;00m([32mconcat[39;49;00m[37m[39;49;00m$
  2685^I[37m         [39;49;00m[33m"[39;49;00m[33m^[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2686^I[37m         [39;49;00m([31mreplace-regexp-in-string[39;49;00m[37m[39;49;00m$
  2687^I[37m          [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m([%!()[39;49;00m[33m\"[39;49;00m[33m<>&|^][39;49;00m[33m\\[39;49;00m[33m)[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2688^I[37m          [39;49;00m[33m"[39;49;00m[33m^[39;49;00m[33m\\[39;49;00m[33m1[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2689^I[37m          [39;49;00m[31margument[39;49;00m)[37m[39;49;00m$
  2690^I[37m         [39;49;00m[33m"[39;49;00m[33m^[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  2691^I[37m      [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31margument[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
  2692^I[37m[39;49;00m$
  2693^I[37m   [39;49;00m([31mt[39;49;00m[37m[39;49;00m$
  2694^I[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mequal[39;49;00m[37m [39;49;00m[31margument[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  2695^I[37m        [39;49;00m[33m"[39;49;00m[33m''[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2696^I[37m      [39;49;00m[37m;; Quote everything except POSIX filename characters.[39;49;00m[37m[39;49;00m$
  2697^I[37m      [39;49;00m[37m;; This should be safe enough even for really weird shells.[39;49;00m[37m[39;49;00m$
  2698^I[37m      [39;49;00m([31mreplace-regexp-in-string[39;49;00m[37m[39;49;00m$
  2699^I[37m       [39;49;00m[33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m'[39;49;00m[33m\n[39;49;00m[33m'[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2700^I[37m       [39;49;00m([31mreplace-regexp-in-string[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m[^-0-9a-zA-Z_./[39;49;00m[33m\n[39;49;00m[33m][39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m&[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31margument[39;49;00m))))[37m[39;49;00m$
  2701^I[37m   [39;49;00m))[37m[39;49;00m$
  2702^I[37m[39;49;00m$
  2703^I([36mdefun[39;49;00m[37m [39;49;00m[31mstring-or-null-p[39;49;00m[37m [39;49;00m([31mobject[39;49;00m)[37m[39;49;00m$
  2704^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn t if OBJECT is a string or nil.[39;49;00m$
  2705^I[33mOtherwise, return nil.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2706^I[37m  [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m[31mobject[39;49;00m)[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[31mobject[39;49;00m)))[37m[39;49;00m$
  2707^I[37m[39;49;00m$
  2708^I([36mdefun[39;49;00m[37m [39;49;00m[31mbooleanp[39;49;00m[37m [39;49;00m([31mobject[39;49;00m)[37m[39;49;00m$
  2709^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn t if OBJECT is one of the two canonical boolean values: t or nil.[39;49;00m$
  2710^I[33mOtherwise, return nil.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2711^I[37m  [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[31mobject[39;49;00m[37m [39;49;00m'([31mnil[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
  2712^I[37m[39;49;00m$
  2713^I([36mdefun[39;49;00m[37m [39;49;00m[31mspecial-form-p[39;49;00m[37m [39;49;00m([31mobject[39;49;00m)[37m[39;49;00m$
  2714^I[37m  [39;49;00m[33m"[39;49;00m[33mNon-nil if and only if OBJECT is a special form.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2715^I[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32msymbolp[39;49;00m[37m [39;49;00m[31mobject[39;49;00m)[37m [39;49;00m([32mfboundp[39;49;00m[37m [39;49;00m[31mobject[39;49;00m))[37m[39;49;00m$
  2716^I[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mobject[39;49;00m[37m [39;49;00m([32mindirect-function[39;49;00m[37m [39;49;00m[31mobject[39;49;00m[37m [39;49;00m[31mt[39;49;00m)))[37m[39;49;00m$
  2717^I[37m  [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32msubrp[39;49;00m[37m [39;49;00m[31mobject[39;49;00m)[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m([34msubr-arity[39;49;00m[37m [39;49;00m[31mobject[39;49;00m))[37m [39;49;00m[33m'unevalled[39;49;00m)))[37m[39;49;00m$
  2718^I[37m[39;49;00m$
  2719^I([36mdefun[39;49;00m[37m [39;49;00m[31mmacrop[39;49;00m[37m [39;49;00m([31mobject[39;49;00m)[37m[39;49;00m$
  2720^I[37m  [39;49;00m[33m"[39;49;00m[33mNon-nil if and only if OBJECT is a macro.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2721^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mdef[39;49;00m[37m [39;49;00m([32mindirect-function[39;49;00m[37m [39;49;00m[31mobject[39;49;00m[37m [39;49;00m[31mt[39;49;00m)))[37m[39;49;00m$
  2722^I[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mdef[39;49;00m)[37m[39;49;00m$
  2723^I[37m      [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[33m'macro[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mdef[39;49;00m))[37m[39;49;00m$
  2724^I[37m          [39;49;00m([34mand[39;49;00m[37m [39;49;00m([31mautoloadp[39;49;00m[37m [39;49;00m[31mdef[39;49;00m)[37m [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m4[39;49;00m[37m [39;49;00m[31mdef[39;49;00m)[37m [39;49;00m'([31mmacro[39;49;00m[37m [39;49;00m[31mt[39;49;00m)))))))[37m[39;49;00m$
  2725^I[37m[39;49;00m$
  2726^I([36mdefun[39;49;00m[37m [39;49;00m[31mfield-at-pos[39;49;00m[37m [39;49;00m([31mpos[39;49;00m)[37m[39;49;00m$
  2727^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn the field at position POS, taking stickiness etc into account.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2728^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mraw-field[39;49;00m[37m [39;49;00m([32mget-char-property[39;49;00m[37m [39;49;00m([32mfield-beginning[39;49;00m[37m [39;49;00m[31mpos[39;49;00m)[37m [39;49;00m[33m'field[39;49;00m)))[37m[39;49;00m$
  2729^I[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mraw-field[39;49;00m[37m [39;49;00m[33m'boundary[39;49;00m)[37m[39;49;00m$
  2730^I[37m^I[39;49;00m([32mget-char-property[39;49;00m[37m [39;49;00m([32m1-[39;49;00m[37m [39;49;00m([32mfield-end[39;49;00m[37m [39;49;00m[31mpos[39;49;00m))[37m [39;49;00m[33m'field[39;49;00m)[37m[39;49;00m$
  2731^I[37m      [39;49;00m[31mraw-field[39;49;00m)))[37m[39;49;00m$
  2732^I[37m[39;49;00m$
  2733^I([36mdefun[39;49;00m[37m [39;49;00m[31msha1[39;49;00m[37m [39;49;00m([31mobject[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[31mbinary[39;49;00m)[37m[39;49;00m$
  2734^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn the SHA1 (Secure Hash Algorithm) of an OBJECT.[39;49;00m$
  2735^I[33mOBJECT is either a string or a buffer.  Optional arguments START and[39;49;00m$
  2736^I[33mEND are character positions specifying which portion of OBJECT for[39;49;00m$
  2737^I[33mcomputing the hash.  If BINARY is non-nil, return a string in binary[39;49;00m$
  2738^I[33mform.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2739^I[37m  [39;49;00m([32msecure-hash[39;49;00m[37m [39;49;00m[33m'sha1[39;49;00m[37m [39;49;00m[31mobject[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[31mbinary[39;49;00m))[37m[39;49;00m$
  2740^I[37m[39;49;00m$
  2741^I([36mdefun[39;49;00m[37m [39;49;00m[31mfunction-get[39;49;00m[37m [39;49;00m([31mf[39;49;00m[37m [39;49;00m[31mprop[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[32mautoload[39;49;00m)[37m[39;49;00m$
  2742^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn the value of property PROP of function F.[39;49;00m$
  2743^I[33mIf AUTOLOAD is non-nil and F is autoloaded, try to autoload it[39;49;00m$
  2744^I[33min the hope that it will set PROP.  If AUTOLOAD is [39;49;00m[33m`macro'[39;49;00m[33m, only do it[39;49;00m$
  2745^I[33mif it's an autoloaded macro.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2746^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mval[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m$
  2747^I[37m    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32msymbolp[39;49;00m[37m [39;49;00m[31mf[39;49;00m)[37m[39;49;00m$
  2748^I[37m                [39;49;00m([32mnull[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mval[39;49;00m[37m [39;49;00m([32mget[39;49;00m[37m [39;49;00m[31mf[39;49;00m[37m [39;49;00m[31mprop[39;49;00m)))[37m[39;49;00m$
  2749^I[37m                [39;49;00m([32mfboundp[39;49;00m[37m [39;49;00m[31mf[39;49;00m))[37m[39;49;00m$
  2750^I[37m      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mfundef[39;49;00m[37m [39;49;00m([32msymbol-function[39;49;00m[37m [39;49;00m[31mf[39;49;00m)))[37m[39;49;00m$
  2751^I[37m        [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[32mautoload[39;49;00m[37m [39;49;00m([31mautoloadp[39;49;00m[37m [39;49;00m[31mfundef[39;49;00m)[37m[39;49;00m$
  2752^I[37m                 [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mequal[39;49;00m[37m [39;49;00m[31mfundef[39;49;00m[37m[39;49;00m$
  2753^I[37m                             [39;49;00m([32mautoload-do-load[39;49;00m[37m [39;49;00m[31mfundef[39;49;00m[37m [39;49;00m[31mf[39;49;00m[37m[39;49;00m$
  2754^I[37m                                               [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[32mautoload[39;49;00m[37m [39;49;00m[33m'macro[39;49;00m)[37m[39;49;00m$
  2755^I[37m                                                   [39;49;00m[33m'macro[39;49;00m)))))[37m[39;49;00m$
  2756^I[37m            [39;49;00m[31mnil[39;49;00m[37m                         [39;49;00m[37m;Re-try `get' on the same `f'.[39;49;00m[37m[39;49;00m$
  2757^I[37m          [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mf[39;49;00m[37m [39;49;00m[31mfundef[39;49;00m))))[37m[39;49;00m$
  2758^I[37m    [39;49;00m[31mval[39;49;00m))[37m[39;49;00m$
  2759^I[37m[39;49;00m[37m[39;49;00m$
  2760^I[37m;;;; Support for yanking and text properties.[39;49;00m[37m[39;49;00m$
  2761^I[37m;; Why here in subr.el rather than in simple.el?  --Stef[39;49;00m[37m[39;49;00m$
  2762^I[37m[39;49;00m$
  2763^I([34mdefvar[39;49;00m[37m [39;49;00m[31myank-handled-properties[39;49;00m)[37m[39;49;00m$
  2764^I([34mdefvar[39;49;00m[37m [39;49;00m[31myank-excluded-properties[39;49;00m)[37m[39;49;00m$
  2765^I[37m[39;49;00m$
  2766^I([36mdefun[39;49;00m[37m [39;49;00m[31mremove-yank-excluded-properties[39;49;00m[37m [39;49;00m([31mstart[39;49;00m[37m [39;49;00m[31mend[39;49;00m)[37m[39;49;00m$
  2767^I[37m  [39;49;00m[33m"[39;49;00m[33mProcess text properties between START and END, inserted for a [39;49;00m[33m`yank'[39;49;00m[33m.[39;49;00m$
  2768^I[33mPerform the handling specified by [39;49;00m[33m`yank-handled-properties'[39;49;00m[33m, then[39;49;00m$
  2769^I[33mremove properties specified by [39;49;00m[33m`yank-excluded-properties'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2770^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31minhibit-read-only[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
  2771^I[37m    [39;49;00m([36mdolist[39;49;00m[37m [39;49;00m([31mhandler[39;49;00m[37m [39;49;00m[31myank-handled-properties[39;49;00m)[37m[39;49;00m$
  2772^I[37m      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mprop[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mhandler[39;49;00m))[37m[39;49;00m$
  2773^I[37m^I    [39;49;00m([31mfun[39;49;00m[37m  [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mhandler[39;49;00m))[37m[39;49;00m$
  2774^I[37m^I    [39;49;00m([31mrun-start[39;49;00m[37m [39;49;00m[31mstart[39;49;00m))[37m[39;49;00m$
  2775^I[37m^I[39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m[31mrun-start[39;49;00m[37m [39;49;00m[31mend[39;49;00m)[37m[39;49;00m$
  2776^I[37m^I  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mvalue[39;49;00m[37m [39;49;00m([32mget-text-property[39;49;00m[37m [39;49;00m[31mrun-start[39;49;00m[37m [39;49;00m[31mprop[39;49;00m))[37m[39;49;00m$
  2777^I[37m^I^I[39;49;00m([31mrun-end[39;49;00m[37m [39;49;00m([32mnext-single-property-change[39;49;00m[37m[39;49;00m$
  2778^I[37m^I^I^I  [39;49;00m[31mrun-start[39;49;00m[37m [39;49;00m[31mprop[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mend[39;49;00m)))[37m[39;49;00m$
  2779^I[37m^I    [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mfun[39;49;00m[37m [39;49;00m[31mvalue[39;49;00m[37m [39;49;00m[31mrun-start[39;49;00m[37m [39;49;00m[31mrun-end[39;49;00m)[37m[39;49;00m$
  2780^I[37m^I    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mrun-start[39;49;00m[37m [39;49;00m[31mrun-end[39;49;00m)))))[37m[39;49;00m$
  2781^I[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31myank-excluded-properties[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
  2782^I[37m^I[39;49;00m([32mset-text-properties[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
  2783^I[37m      [39;49;00m([32mremove-list-of-text-properties[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[31myank-excluded-properties[39;49;00m))))[37m[39;49;00m$
  2784^I[37m[39;49;00m$
  2785^I([34mdefvar[39;49;00m[37m [39;49;00m[31myank-undo-function[39;49;00m)[37m[39;49;00m$
  2786^I[37m[39;49;00m$
  2787^I([36mdefun[39;49;00m[37m [39;49;00m[31minsert-for-yank[39;49;00m[37m [39;49;00m([32mstring[39;49;00m)[37m[39;49;00m$
  2788^I[37m  [39;49;00m[33m"[39;49;00m[33mCall [39;49;00m[33m`insert-for-yank-1'[39;49;00m[33m repetitively for each [39;49;00m[33m`yank-handler'[39;49;00m[33m segment.[39;49;00m$
  2789^I[33m[39;49;00m$
  2790^I[33mSee [39;49;00m[33m`insert-for-yank-1'[39;49;00m[33m for more details.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2791^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m([31mto[39;49;00m)[37m[39;49;00m$
  2792^I[37m    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mto[39;49;00m[37m [39;49;00m([32mnext-single-property-change[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[33m'yank-handler[39;49;00m[37m [39;49;00m[32mstring[39;49;00m))[37m[39;49;00m$
  2793^I[37m      [39;49;00m([31minsert-for-yank-1[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[31mto[39;49;00m))[37m[39;49;00m$
  2794^I[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[31mto[39;49;00m))))[37m[39;49;00m$
  2795^I[37m  [39;49;00m([31minsert-for-yank-1[39;49;00m[37m [39;49;00m[32mstring[39;49;00m))[37m[39;49;00m$
  2796^I[37m[39;49;00m$
  2797^I([36mdefun[39;49;00m[37m [39;49;00m[31minsert-for-yank-1[39;49;00m[37m [39;49;00m([32mstring[39;49;00m)[37m[39;49;00m$
  2798^I[37m  [39;49;00m[33m"[39;49;00m[33mInsert STRING at point for the [39;49;00m[33m`yank'[39;49;00m[33m command.[39;49;00m$
  2799^I[33mThis function is like [39;49;00m[33m`insert'[39;49;00m[33m, except it honors the variables[39;49;00m$
  2800^I[33m`yank-handled-properties'[39;49;00m[33m and [39;49;00m[33m`yank-excluded-properties'[39;49;00m[33m, and the[39;49;00m$
  2801^I[33m`yank-handler'[39;49;00m[33m text property.[39;49;00m$
  2802^I[33m[39;49;00m$
  2803^I[33mProperties listed in [39;49;00m[33m`yank-handled-properties'[39;49;00m[33m are processed,[39;49;00m$
  2804^I[33mthen those listed in [39;49;00m[33m`yank-excluded-properties'[39;49;00m[33m are discarded.[39;49;00m$
  2805^I[33m[39;49;00m$
  2806^I[33mIf STRING has a non-nil [39;49;00m[33m`yank-handler'[39;49;00m[33m property on its first[39;49;00m$
  2807^I[33mcharacter, the normal insert behavior is altered.  The value of[39;49;00m$
  2808^I[33mthe [39;49;00m[33m`yank-handler'[39;49;00m[33m property must be a list of one to four[39;49;00m$
  2809^I[33melements, of the form (FUNCTION PARAM NOEXCLUDE UNDO).[39;49;00m$
  2810^I[33mFUNCTION, if non-nil, should be a function of one argument, an[39;49;00m$
  2811^I[33m object to insert; it is called instead of [39;49;00m[33m`insert'[39;49;00m[33m.[39;49;00m$
  2812^I[33mPARAM, if present and non-nil, replaces STRING as the argument to[39;49;00m$
  2813^I[33m FUNCTION or [39;49;00m[33m`insert'[39;49;00m[33m; e.g. if FUNCTION is [39;49;00m[33m`yank-rectangle'[39;49;00m[33m, PARAM[39;49;00m$
  2814^I[33m may be a list of strings to insert as a rectangle.[39;49;00m$
  2815^I[33mIf NOEXCLUDE is present and non-nil, the normal removal of[39;49;00m$
  2816^I[33m [39;49;00m[33m`yank-excluded-properties'[39;49;00m[33m is not performed; instead FUNCTION is[39;49;00m$
  2817^I[33m responsible for the removal.  This may be necessary if FUNCTION[39;49;00m$
  2818^I[33m adjusts point before or after inserting the object.[39;49;00m$
  2819^I[33mUNDO, if present and non-nil, should be a function to be called[39;49;00m$
  2820^I[33m by [39;49;00m[33m`yank-pop'[39;49;00m[33m to undo the insertion of the current object.  It is[39;49;00m$
  2821^I[33m given two arguments, the start and end of the region.  FUNCTION[39;49;00m$
  2822^I[33m may set [39;49;00m[33m`yank-undo-function'[39;49;00m[33m to override UNDO.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2823^I[37m  [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mhandler[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m[32mstring[39;49;00m)[37m[39;49;00m$
  2824^I[37m^I^I       [39;49;00m([32mget-text-property[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[33m'yank-handler[39;49;00m[37m [39;49;00m[32mstring[39;49;00m)))[37m[39;49;00m$
  2825^I[37m^I [39;49;00m([31mparam[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mhandler[39;49;00m)[37m [39;49;00m[32mstring[39;49;00m))[37m[39;49;00m$
  2826^I[37m^I [39;49;00m([31mopoint[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m))[37m[39;49;00m$
  2827^I[37m^I [39;49;00m([31minhibit-read-only[39;49;00m[37m [39;49;00m[31minhibit-read-only[39;49;00m)[37m[39;49;00m$
  2828^I[37m^I [39;49;00m[31mend[39;49;00m)[37m[39;49;00m$
  2829^I[37m[39;49;00m$
  2830^I[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31myank-undo-function[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
  2831^I[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[31mhandler[39;49;00m)[37m [39;49;00m[37m; FUNCTION[39;49;00m[37m[39;49;00m$
  2832^I[37m^I[39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mhandler[39;49;00m)[37m [39;49;00m[31mparam[39;49;00m)[37m[39;49;00m$
  2833^I[37m      [39;49;00m([32minsert[39;49;00m[37m [39;49;00m[31mparam[39;49;00m))[37m[39;49;00m$
  2834^I[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m))[37m[39;49;00m$
  2835^I[37m[39;49;00m$
  2836^I[37m    [39;49;00m[37m;; Prevent read-only properties from interfering with the[39;49;00m[37m[39;49;00m$
  2837^I[37m    [39;49;00m[37m;; following text property changes.[39;49;00m[37m[39;49;00m$
  2838^I[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31minhibit-read-only[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
  2839^I[37m[39;49;00m$
  2840^I[37m    [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m[31mhandler[39;49;00m)[37m [39;49;00m[37m; NOEXCLUDE[39;49;00m[37m[39;49;00m$
  2841^I[37m      [39;49;00m([31mremove-yank-excluded-properties[39;49;00m[37m [39;49;00m[31mopoint[39;49;00m[37m [39;49;00m[31mend[39;49;00m))[37m[39;49;00m$
  2842^I[37m[39;49;00m$
  2843^I[37m    [39;49;00m[37m;; If last inserted char has properties, mark them as rear-nonsticky.[39;49;00m[37m[39;49;00m$
  2844^I[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[31mopoint[39;49;00m)[37m[39;49;00m$
  2845^I[37m^I     [39;49;00m([32mtext-properties-at[39;49;00m[37m [39;49;00m([32m1-[39;49;00m[37m [39;49;00m[31mend[39;49;00m)))[37m[39;49;00m$
  2846^I[37m^I[39;49;00m([32mput-text-property[39;49;00m[37m [39;49;00m([32m1-[39;49;00m[37m [39;49;00m[31mend[39;49;00m)[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[33m'rear-nonsticky[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
  2847^I[37m[39;49;00m$
  2848^I[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31myank-undo-function[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m^I^I   [39;49;00m[37m; not set by FUNCTION[39;49;00m[37m[39;49;00m$
  2849^I[37m^I[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31myank-undo-function[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m3[39;49;00m[37m [39;49;00m[31mhandler[39;49;00m)))[37m [39;49;00m[37m; UNDO[39;49;00m[37m[39;49;00m$
  2850^I[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m4[39;49;00m[37m [39;49;00m[31mhandler[39;49;00m)[37m^I^I^I^I   [39;49;00m[37m; COMMAND[39;49;00m[37m[39;49;00m$
  2851^I[37m^I[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mthis-command[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m4[39;49;00m[37m [39;49;00m[31mhandler[39;49;00m)))))[37m[39;49;00m$
  2852^I[37m[39;49;00m$
  2853^I([36mdefun[39;49;00m[37m [39;49;00m[31minsert-buffer-substring-no-properties[39;49;00m[37m [39;49;00m([31mbuffer[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mend[39;49;00m)[37m[39;49;00m$
  2854^I[37m  [39;49;00m[33m"[39;49;00m[33mInsert before point a substring of BUFFER, without text properties.[39;49;00m$
  2855^I[33mBUFFER may be a buffer or a buffer name.[39;49;00m$
  2856^I[33mArguments START and END are character positions specifying the substring.[39;49;00m$
  2857^I[33mThey default to the values of (point-min) and (point-max) in BUFFER.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2858^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mopoint[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m)))[37m[39;49;00m$
  2859^I[37m    [39;49;00m([32minsert-buffer-substring[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mend[39;49;00m)[37m[39;49;00m$
  2860^I[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31minhibit-read-only[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
  2861^I[37m      [39;49;00m([32mset-text-properties[39;49;00m[37m [39;49;00m[31mopoint[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m)[37m [39;49;00m[31mnil[39;49;00m))))[37m[39;49;00m$
  2862^I[37m[39;49;00m$
  2863^I([36mdefun[39;49;00m[37m [39;49;00m[31minsert-buffer-substring-as-yank[39;49;00m[37m [39;49;00m([31mbuffer[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mend[39;49;00m)[37m[39;49;00m$
  2864^I[37m  [39;49;00m[33m"[39;49;00m[33mInsert before point a part of BUFFER, stripping some text properties.[39;49;00m$
  2865^I[33mBUFFER may be a buffer or a buffer name.[39;49;00m$
  2866^I[33mArguments START and END are character positions specifying the substring.[39;49;00m$
  2867^I[33mThey default to the values of (point-min) and (point-max) in BUFFER.[39;49;00m$
  2868^I[33mBefore insertion, process text properties according to[39;49;00m$
  2869^I[33m`yank-handled-properties'[39;49;00m[33m and [39;49;00m[33m`yank-excluded-properties'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2870^I[37m  [39;49;00m[37m;; Since the buffer text should not normally have yank-handler properties,[39;49;00m[37m[39;49;00m$
  2871^I[37m  [39;49;00m[37m;; there is no need to handle them here.[39;49;00m[37m[39;49;00m$
  2872^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mopoint[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m)))[37m[39;49;00m$
  2873^I[37m    [39;49;00m([32minsert-buffer-substring[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mend[39;49;00m)[37m[39;49;00m$
  2874^I[37m    [39;49;00m([31mremove-yank-excluded-properties[39;49;00m[37m [39;49;00m[31mopoint[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m))))[37m[39;49;00m$
  2875^I[37m[39;49;00m$
  2876^I([36mdefun[39;49;00m[37m [39;49;00m[31myank-handle-font-lock-face-property[39;49;00m[37m [39;49;00m([31mface[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mend[39;49;00m)[37m[39;49;00m$
  2877^I[37m  [39;49;00m[33m"[39;49;00m[33mIf [39;49;00m[33m`font-lock-defaults'[39;49;00m[33m is nil, apply FACE as a [39;49;00m[33m`face'[39;49;00m[33m property.[39;49;00m$
  2878^I[33mSTART and END denote the start and end of the text to act on.[39;49;00m$
  2879^I[33mDo nothing if FACE is nil.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2880^I[37m  [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mface[39;49;00m[37m[39;49;00m$
  2881^I[37m       [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[31mfont-lock-defaults[39;49;00m)[37m[39;49;00m$
  2882^I[37m       [39;49;00m([32mput-text-property[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[33m'face[39;49;00m[37m [39;49;00m[31mface[39;49;00m)))[37m[39;49;00m$
  2883^I[37m[39;49;00m$
  2884^I[37m;; This removes `mouse-face' properties in *Help* buffer buttons:[39;49;00m[37m[39;49;00m$
  2885^I[37m;; http://lists.gnu.org/archive/html/emacs-devel/2002-04/msg00648.html[39;49;00m[37m[39;49;00m$
  2886^I([36mdefun[39;49;00m[37m [39;49;00m[31myank-handle-category-property[39;49;00m[37m [39;49;00m([31mcategory[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mend[39;49;00m)[37m[39;49;00m$
  2887^I[37m  [39;49;00m[33m"[39;49;00m[33mApply property category CATEGORY's properties between START and END.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2888^I[37m  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31mcategory[39;49;00m[37m[39;49;00m$
  2889^I[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mstart2[39;49;00m[37m [39;49;00m[31mstart[39;49;00m))[37m[39;49;00m$
  2890^I[37m      [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m[31mstart2[39;49;00m[37m [39;49;00m[31mend[39;49;00m)[37m[39;49;00m$
  2891^I[37m^I[39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mend2[39;49;00m[37m     [39;49;00m([32mnext-property-change[39;49;00m[37m [39;49;00m[31mstart2[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mend[39;49;00m))[37m[39;49;00m$
  2892^I[37m^I      [39;49;00m([31moriginal[39;49;00m[37m [39;49;00m([32mtext-properties-at[39;49;00m[37m [39;49;00m[31mstart2[39;49;00m)))[37m[39;49;00m$
  2893^I[37m^I  [39;49;00m([32mset-text-properties[39;49;00m[37m [39;49;00m[31mstart2[39;49;00m[37m [39;49;00m[31mend2[39;49;00m[37m [39;49;00m([32msymbol-plist[39;49;00m[37m [39;49;00m[31mcategory[39;49;00m))[37m[39;49;00m$
  2894^I[37m^I  [39;49;00m([32madd-text-properties[39;49;00m[37m [39;49;00m[31mstart2[39;49;00m[37m [39;49;00m[31mend2[39;49;00m[37m [39;49;00m[31moriginal[39;49;00m)[37m[39;49;00m$
  2895^I[37m^I  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mstart2[39;49;00m[37m [39;49;00m[31mend2[39;49;00m))))))[37m[39;49;00m$
  2896^I[37m[39;49;00m$
  2897^I[37m[39;49;00m[37m[39;49;00m$
  2898^I[37m;;;; Synchronous shell commands.[39;49;00m[37m[39;49;00m$
  2899^I[37m[39;49;00m$
  2900^I([36mdefun[39;49;00m[37m [39;49;00m[31mstart-process-shell-command[39;49;00m[37m [39;49;00m([31mname[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31margs[39;49;00m)[37m[39;49;00m$
  2901^I[37m  [39;49;00m[33m"[39;49;00m[33mStart a program in a subprocess.  Return the process object for it.[39;49;00m$
  2902^I[33mNAME is name for process.  It is modified if necessary to make it unique.[39;49;00m$
  2903^I[33mBUFFER is the buffer (or buffer name) to associate with the process.[39;49;00m$
  2904^I[33m Process output goes at end of that buffer, unless you specify[39;49;00m$
  2905^I[33m an output stream or filter function to handle the output.[39;49;00m$
  2906^I[33m BUFFER may be also nil, meaning that this process is not associated[39;49;00m$
  2907^I[33m with any buffer[39;49;00m$
  2908^I[33mCOMMAND is the shell command to run.[39;49;00m$
  2909^I[33m[39;49;00m$
  2910^I[33mAn old calling convention accepted any number of arguments after COMMAND,[39;49;00m$
  2911^I[33mwhich were just concatenated to COMMAND.  This is still supported but strongly[39;49;00m$
  2912^I[33mdiscouraged.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2913^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31madvertised-calling-convention[39;49;00m[37m [39;49;00m([31mname[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m [39;49;00m[31mcommand[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m23.1[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
  2914^I[37m  [39;49;00m[37m;; We used to use `exec' to replace the shell with the command,[39;49;00m[37m[39;49;00m$
  2915^I[37m  [39;49;00m[37m;; but that failed to handle (...) and semicolon, etc.[39;49;00m[37m[39;49;00m$
  2916^I[37m  [39;49;00m([32mstart-process[39;49;00m[37m [39;49;00m[31mname[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m [39;49;00m[31mshell-file-name[39;49;00m[37m [39;49;00m[31mshell-command-switch[39;49;00m[37m[39;49;00m$
  2917^I[37m^I^I [39;49;00m([32mmapconcat[39;49;00m[37m [39;49;00m[33m'identity[39;49;00m[37m [39;49;00m[31margs[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
  2918^I[37m[39;49;00m$
  2919^I([36mdefun[39;49;00m[37m [39;49;00m[31mstart-file-process-shell-command[39;49;00m[37m [39;49;00m([31mname[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31margs[39;49;00m)[37m[39;49;00m$
  2920^I[37m  [39;49;00m[33m"[39;49;00m[33mStart a program in a subprocess.  Return the process object for it.[39;49;00m$
  2921^I[33mSimilar to [39;49;00m[33m`start-process-shell-command'[39;49;00m[33m, but calls [39;49;00m[33m`start-file-process'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2922^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31madvertised-calling-convention[39;49;00m[37m [39;49;00m([31mname[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m [39;49;00m[31mcommand[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m23.1[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
  2923^I[37m  [39;49;00m([31mstart-file-process[39;49;00m[37m[39;49;00m$
  2924^I[37m   [39;49;00m[31mname[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m[39;49;00m$
  2925^I[37m   [39;49;00m([34mif[39;49;00m[37m [39;49;00m([31mfile-remote-p[39;49;00m[37m [39;49;00m[31mdefault-directory[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m/bin/sh[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mshell-file-name[39;49;00m)[37m[39;49;00m$
  2926^I[37m   [39;49;00m([34mif[39;49;00m[37m [39;49;00m([31mfile-remote-p[39;49;00m[37m [39;49;00m[31mdefault-directory[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m-c[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mshell-command-switch[39;49;00m)[37m[39;49;00m$
  2927^I[37m   [39;49;00m([32mmapconcat[39;49;00m[37m [39;49;00m[33m'identity[39;49;00m[37m [39;49;00m[31margs[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
  2928^I[37m[39;49;00m$
  2929^I([36mdefun[39;49;00m[37m [39;49;00m[31mcall-process-shell-command[39;49;00m[37m [39;49;00m([31mcommand[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31minfile[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m [39;49;00m[31mdisplay[39;49;00m[37m[39;49;00m$
  2930^I[37m^I^I^I^I^I   [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31margs[39;49;00m)[37m[39;49;00m$
  2931^I[37m  [39;49;00m[33m"[39;49;00m[33mExecute the shell command COMMAND synchronously in separate process.[39;49;00m$
  2932^I[33mThe remaining arguments are optional.[39;49;00m$
  2933^I[33mThe program's input comes from file INFILE (nil means [39;49;00m[33m`/dev/null'[39;49;00m[33m).[39;49;00m$
  2934^I[33mInsert output in BUFFER before point; t means current buffer;[39;49;00m$
  2935^I[33m nil for BUFFER means discard it; 0 means discard and don't wait.[39;49;00m$
  2936^I[33mBUFFER can also have the form (REAL-BUFFER STDERR-FILE); in that case,[39;49;00m$
  2937^I[33mREAL-BUFFER says what to do with standard output, as above,[39;49;00m$
  2938^I[33mwhile STDERR-FILE says what to do with standard error in the child.[39;49;00m$
  2939^I[33mSTDERR-FILE may be nil (discard standard error output),[39;49;00m$
  2940^I[33mt (mix it with ordinary output), or a file name string.[39;49;00m$
  2941^I[33m[39;49;00m$
  2942^I[33mFourth arg DISPLAY non-nil means redisplay buffer as output is inserted.[39;49;00m$
  2943^I[33mWildcards and redirection are handled as usual in the shell.[39;49;00m$
  2944^I[33m[39;49;00m$
  2945^I[33mIf BUFFER is 0, [39;49;00m[33m`call-process-shell-command'[39;49;00m[33m returns immediately with value nil.[39;49;00m$
  2946^I[33mOtherwise it waits for COMMAND to terminate and returns a numeric exit[39;49;00m$
  2947^I[33mstatus or a signal description string.[39;49;00m$
  2948^I[33mIf you quit, the process is killed with SIGINT, or SIGKILL if you quit again.[39;49;00m$
  2949^I[33m[39;49;00m$
  2950^I[33mAn old calling convention accepted any number of arguments after DISPLAY,[39;49;00m$
  2951^I[33mwhich were just concatenated to COMMAND.  This is still supported but strongly[39;49;00m$
  2952^I[33mdiscouraged.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2953^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31madvertised-calling-convention[39;49;00m[37m[39;49;00m$
  2954^I[37m            [39;49;00m([31mcommand[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31minfile[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m [39;49;00m[31mdisplay[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m24.5[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
  2955^I[37m  [39;49;00m[37m;; We used to use `exec' to replace the shell with the command,[39;49;00m[37m[39;49;00m$
  2956^I[37m  [39;49;00m[37m;; but that failed to handle (...) and semicolon, etc.[39;49;00m[37m[39;49;00m$
  2957^I[37m  [39;49;00m([32mcall-process[39;49;00m[37m [39;49;00m[31mshell-file-name[39;49;00m[37m[39;49;00m$
  2958^I[37m^I^I[39;49;00m[31minfile[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m [39;49;00m[31mdisplay[39;49;00m[37m[39;49;00m$
  2959^I[37m^I^I[39;49;00m[31mshell-command-switch[39;49;00m[37m[39;49;00m$
  2960^I[37m^I^I[39;49;00m([32mmapconcat[39;49;00m[37m [39;49;00m[33m'identity[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mcommand[39;49;00m[37m [39;49;00m[31margs[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
  2961^I[37m[39;49;00m$
  2962^I([36mdefun[39;49;00m[37m [39;49;00m[31mprocess-file-shell-command[39;49;00m[37m [39;49;00m([31mcommand[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31minfile[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m [39;49;00m[31mdisplay[39;49;00m[37m[39;49;00m$
  2963^I[37m^I^I^I^I^I   [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31margs[39;49;00m)[37m[39;49;00m$
  2964^I[37m  [39;49;00m[33m"[39;49;00m[33mProcess files synchronously in a separate process.[39;49;00m$
  2965^I[33mSimilar to [39;49;00m[33m`call-process-shell-command'[39;49;00m[33m, but calls [39;49;00m[33m`process-file'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2966^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31madvertised-calling-convention[39;49;00m[37m[39;49;00m$
  2967^I[37m            [39;49;00m([31mcommand[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31minfile[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m [39;49;00m[31mdisplay[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m24.5[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
  2968^I[37m  [39;49;00m([31mprocess-file[39;49;00m[37m[39;49;00m$
  2969^I[37m   [39;49;00m([34mif[39;49;00m[37m [39;49;00m([31mfile-remote-p[39;49;00m[37m [39;49;00m[31mdefault-directory[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m/bin/sh[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mshell-file-name[39;49;00m)[37m[39;49;00m$
  2970^I[37m   [39;49;00m[31minfile[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m [39;49;00m[31mdisplay[39;49;00m[37m[39;49;00m$
  2971^I[37m   [39;49;00m([34mif[39;49;00m[37m [39;49;00m([31mfile-remote-p[39;49;00m[37m [39;49;00m[31mdefault-directory[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m-c[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mshell-command-switch[39;49;00m)[37m[39;49;00m$
  2972^I[37m   [39;49;00m([32mmapconcat[39;49;00m[37m [39;49;00m[33m'identity[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mcommand[39;49;00m[37m [39;49;00m[31margs[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
  2973^I[37m[39;49;00m[37m[39;49;00m$
  2974^I[37m;;;; Lisp macros to do various things temporarily.[39;49;00m[37m[39;49;00m$
  2975^I[37m[39;49;00m$
  2976^I([36mdefmacro[39;49;00m[37m [39;49;00m[36mtrack-mouse[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
  2977^I[37m  [39;49;00m[33m"[39;49;00m[33mEvaluate BODY with mouse movement events enabled.[39;49;00m$
  2978^I[33mWithin a [39;49;00m[33m`track-mouse'[39;49;00m[33m form, mouse motion generates input events that[39;49;00m$
  2979^I[33m you can read with [39;49;00m[33m`read-event'[39;49;00m[33m.[39;49;00m$
  2980^I[33mNormally, mouse motion is ignored.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2981^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m$
  2982^I[37m  [39;49;00m`([32minternal--track-mouse[39;49;00m[37m [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m()[37m [39;49;00m,@[31mbody[39;49;00m)))[37m[39;49;00m$
  2983^I[37m[39;49;00m$
  2984^I([36mdefmacro[39;49;00m[37m [39;49;00m[36mwith-current-buffer[39;49;00m[37m [39;49;00m([31mbuffer-or-name[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
  2985^I[37m  [39;49;00m[33m"[39;49;00m[33mExecute the forms in BODY with BUFFER-OR-NAME temporarily current.[39;49;00m$
  2986^I[33mBUFFER-OR-NAME must be a buffer or the name of an existing buffer.[39;49;00m$
  2987^I[33mThe value returned is the value of the last form in BODY.  See[39;49;00m$
  2988^I[33malso [39;49;00m[33m`with-temp-buffer'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2989^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
  2990^I[37m  [39;49;00m`([34msave-current-buffer[39;49;00m[37m[39;49;00m$
  2991^I[37m     [39;49;00m([32mset-buffer[39;49;00m[37m [39;49;00m,[31mbuffer-or-name[39;49;00m)[37m[39;49;00m$
  2992^I[37m     [39;49;00m,@[31mbody[39;49;00m))[37m[39;49;00m$
  2993^I[37m[39;49;00m$
  2994^I([36mdefun[39;49;00m[37m [39;49;00m[31minternal--before-with-selected-window[39;49;00m[37m [39;49;00m([31mwindow[39;49;00m)[37m[39;49;00m$
  2995^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mother-frame[39;49;00m[37m [39;49;00m([32mwindow-frame[39;49;00m[37m [39;49;00m[31mwindow[39;49;00m)))[37m[39;49;00m$
  2996^I[37m    [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[31mwindow[39;49;00m[37m [39;49;00m([32mselected-window[39;49;00m)[37m[39;49;00m$
  2997^I[37m          [39;49;00m[37m;; Selecting a window on another frame also changes that[39;49;00m[37m[39;49;00m$
  2998^I[37m          [39;49;00m[37m;; frame's frame-selected-window.  We must save&restore it.[39;49;00m[37m[39;49;00m$
  2999^I[37m          [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mselected-frame[39;49;00m)[37m [39;49;00m[31mother-frame[39;49;00m)[37m[39;49;00m$
  3000^I[37m            [39;49;00m([32mframe-selected-window[39;49;00m[37m [39;49;00m[31mother-frame[39;49;00m))[37m[39;49;00m$
  3001^I[37m          [39;49;00m[37m;; Also remember the top-frame if on ttys.[39;49;00m[37m[39;49;00m$
  3002^I[37m          [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mselected-frame[39;49;00m)[37m [39;49;00m[31mother-frame[39;49;00m)[37m[39;49;00m$
  3003^I[37m            [39;49;00m([32mtty-top-frame[39;49;00m[37m [39;49;00m[31mother-frame[39;49;00m)))))[37m[39;49;00m$
  3004^I[37m[39;49;00m$
  3005^I([36mdefun[39;49;00m[37m [39;49;00m[31minternal--after-with-selected-window[39;49;00m[37m [39;49;00m([31mstate[39;49;00m)[37m[39;49;00m$
  3006^I[37m  [39;49;00m[37m;; First reset frame-selected-window.[39;49;00m[37m[39;49;00m$
  3007^I[37m  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mwindow-live-p[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m[31mstate[39;49;00m))[37m[39;49;00m$
  3008^I[37m    [39;49;00m[37m;; We don't use set-frame-selected-window because it does not[39;49;00m[37m[39;49;00m$
  3009^I[37m    [39;49;00m[37m;; pass the `norecord' argument to Fselect_window.[39;49;00m[37m[39;49;00m$
  3010^I[37m    [39;49;00m([32mselect-window[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m[31mstate[39;49;00m)[37m [39;49;00m[33m'norecord[39;49;00m)[37m[39;49;00m$
  3011^I[37m    [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mframe-live-p[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m3[39;49;00m[37m [39;49;00m[31mstate[39;49;00m))[37m[39;49;00m$
  3012^I[37m         [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mtty-top-frame[39;49;00m)[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m3[39;49;00m[37m [39;49;00m[31mstate[39;49;00m)))[37m[39;49;00m$
  3013^I[37m         [39;49;00m([32mselect-frame[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m3[39;49;00m[37m [39;49;00m[31mstate[39;49;00m)[37m [39;49;00m[33m'norecord[39;49;00m)))[37m[39;49;00m$
  3014^I[37m  [39;49;00m[37m;; Then reset the actual selected-window.[39;49;00m[37m[39;49;00m$
  3015^I[37m  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mwindow-live-p[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mstate[39;49;00m))[37m[39;49;00m$
  3016^I[37m    [39;49;00m([32mselect-window[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mstate[39;49;00m)[37m [39;49;00m[33m'norecord[39;49;00m)))[37m[39;49;00m$
  3017^I[37m[39;49;00m$
  3018^I([36mdefmacro[39;49;00m[37m [39;49;00m[36mwith-selected-window[39;49;00m[37m [39;49;00m([31mwindow[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
  3019^I[37m  [39;49;00m[33m"[39;49;00m[33mExecute the forms in BODY with WINDOW as the selected window.[39;49;00m$
  3020^I[33mThe value returned is the value of the last form in BODY.[39;49;00m$
  3021^I[33m[39;49;00m$
  3022^I[33mThis macro saves and restores the selected window, as well as the[39;49;00m$
  3023^I[33mselected window of each frame.  It does not change the order of[39;49;00m$
  3024^I[33mrecently selected windows.  If the previously selected window of[39;49;00m$
  3025^I[33msome frame is no longer live at the end of BODY, that frame's[39;49;00m$
  3026^I[33mselected window is left alone.  If the selected window is no[39;49;00m$
  3027^I[33mlonger live, then whatever window is selected at the end of BODY[39;49;00m$
  3028^I[33mremains selected.[39;49;00m$
  3029^I[33m[39;49;00m$
  3030^I[33mThis macro uses [39;49;00m[33m`save-current-buffer'[39;49;00m[33m to save and restore the[39;49;00m$
  3031^I[33mcurrent buffer, since otherwise its normal operation could[39;49;00m$
  3032^I[33mpotentially make a different buffer current.  It does not alter[39;49;00m$
  3033^I[33mthe buffer list ordering.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3034^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
  3035^I[37m  [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m(([31msave-selected-window--state[39;49;00m[37m[39;49;00m$
  3036^I[37m          [39;49;00m([31minternal--before-with-selected-window[39;49;00m[37m [39;49;00m,[31mwindow[39;49;00m)))[37m[39;49;00m$
  3037^I[37m     [39;49;00m([34msave-current-buffer[39;49;00m[37m[39;49;00m$
  3038^I[37m       [39;49;00m([34munwind-protect[39;49;00m[37m[39;49;00m$
  3039^I[37m           [39;49;00m([34mprogn[39;49;00m[37m [39;49;00m([32mselect-window[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31msave-selected-window--state[39;49;00m)[37m [39;49;00m[33m'norecord[39;49;00m)[37m[39;49;00m$
  3040^I[37m^I^I  [39;49;00m,@[31mbody[39;49;00m)[37m[39;49;00m$
  3041^I[37m         [39;49;00m([31minternal--after-with-selected-window[39;49;00m[37m [39;49;00m[31msave-selected-window--state[39;49;00m)))))[37m[39;49;00m$
  3042^I[37m[39;49;00m$
  3043^I([36mdefmacro[39;49;00m[37m [39;49;00m[36mwith-selected-frame[39;49;00m[37m [39;49;00m([31mframe[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
  3044^I[37m  [39;49;00m[33m"[39;49;00m[33mExecute the forms in BODY with FRAME as the selected frame.[39;49;00m$
  3045^I[33mThe value returned is the value of the last form in BODY.[39;49;00m$
  3046^I[33m[39;49;00m$
  3047^I[33mThis macro saves and restores the selected frame, and changes the[39;49;00m$
  3048^I[33morder of neither the recently selected windows nor the buffers in[39;49;00m$
  3049^I[33mthe buffer list.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3050^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
  3051^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mold-frame[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mold-frame[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
  3052^I[37m^I[39;49;00m([31mold-buffer[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mold-buffer[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
  3053^I[37m    [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m((,[31mold-frame[39;49;00m[37m [39;49;00m([32mselected-frame[39;49;00m))[37m[39;49;00m$
  3054^I[37m^I   [39;49;00m(,[31mold-buffer[39;49;00m[37m [39;49;00m([32mcurrent-buffer[39;49;00m)))[37m[39;49;00m$
  3055^I[37m       [39;49;00m([34munwind-protect[39;49;00m[37m[39;49;00m$
  3056^I[37m^I   [39;49;00m([34mprogn[39;49;00m[37m [39;49;00m([32mselect-frame[39;49;00m[37m [39;49;00m,[31mframe[39;49;00m[37m [39;49;00m[33m'norecord[39;49;00m)[37m[39;49;00m$
  3057^I[37m^I^I  [39;49;00m,@[31mbody[39;49;00m)[37m[39;49;00m$
  3058^I[37m^I [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mframe-live-p[39;49;00m[37m [39;49;00m,[31mold-frame[39;49;00m)[37m[39;49;00m$
  3059^I[37m^I   [39;49;00m([32mselect-frame[39;49;00m[37m [39;49;00m,[31mold-frame[39;49;00m[37m [39;49;00m[33m'norecord[39;49;00m))[37m[39;49;00m$
  3060^I[37m^I [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mbuffer-live-p[39;49;00m[37m [39;49;00m,[31mold-buffer[39;49;00m)[37m[39;49;00m$
  3061^I[37m^I   [39;49;00m([32mset-buffer[39;49;00m[37m [39;49;00m,[31mold-buffer[39;49;00m))))))[37m[39;49;00m$
  3062^I[37m[39;49;00m$
  3063^I([36mdefmacro[39;49;00m[37m [39;49;00m[36msave-window-excursion[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
  3064^I[37m  [39;49;00m[33m"[39;49;00m[33mExecute BODY, then restore previous window configuration.[39;49;00m$
  3065^I[33mThis macro saves the window configuration on the selected frame,[39;49;00m$
  3066^I[33mexecutes BODY, then calls [39;49;00m[33m`set-window-configuration'[39;49;00m[33m to restore[39;49;00m$
  3067^I[33mthe saved window configuration.  The return value is the last[39;49;00m$
  3068^I[33mform in BODY.  The window configuration is also restored if BODY[39;49;00m$
  3069^I[33mexits nonlocally.[39;49;00m$
  3070^I[33m[39;49;00m$
  3071^I[33mBEWARE: Most uses of this macro introduce bugs.[39;49;00m$
  3072^I[33mE.g. it should not be used to try and prevent some code from opening[39;49;00m$
  3073^I[33ma new window, since that window may sometimes appear in another frame,[39;49;00m$
  3074^I[33min which case [39;49;00m[33m`save-window-excursion'[39;49;00m[33m cannot help.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3075^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
  3076^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mc[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mwconfig[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
  3077^I[37m    [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m((,[31mc[39;49;00m[37m [39;49;00m([32mcurrent-window-configuration[39;49;00m)))[37m[39;49;00m$
  3078^I[37m       [39;49;00m([34munwind-protect[39;49;00m[37m [39;49;00m([34mprogn[39;49;00m[37m [39;49;00m,@[31mbody[39;49;00m)[37m[39;49;00m$
  3079^I[37m         [39;49;00m([32mset-window-configuration[39;49;00m[37m [39;49;00m,[31mc[39;49;00m)))))[37m[39;49;00m$
  3080^I[37m[39;49;00m$
  3081^I([36mdefun[39;49;00m[37m [39;49;00m[31minternal-temp-output-buffer-show[39;49;00m[37m [39;49;00m([31mbuffer[39;49;00m)[37m[39;49;00m$
  3082^I[37m  [39;49;00m[33m"[39;49;00m[33mInternal function for [39;49;00m[33m`with-output-to-temp-buffer'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3083^I[37m  [39;49;00m([36mwith-current-buffer[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m[39;49;00m$
  3084^I[37m    [39;49;00m([32mset-buffer-modified-p[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
  3085^I[37m    [39;49;00m([32mgoto-char[39;49;00m[37m [39;49;00m([32mpoint-min[39;49;00m)))[37m[39;49;00m$
  3086^I[37m[39;49;00m$
  3087^I[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mtemp-buffer-show-function[39;49;00m[37m[39;49;00m$
  3088^I[37m      [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mtemp-buffer-show-function[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m)[37m[39;49;00m$
  3089^I[37m    [39;49;00m([36mwith-current-buffer[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m[39;49;00m$
  3090^I[37m      [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mwindow[39;49;00m[37m[39;49;00m$
  3091^I[37m^I      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([32mwindow-combination-limit[39;49;00m[37m[39;49;00m$
  3092^I[37m^I^I   [39;49;00m[37m;; When `window-combination-limit' equals[39;49;00m[37m[39;49;00m$
  3093^I[37m^I^I   [39;49;00m[37m;; `temp-buffer' or `temp-buffer-resize' and[39;49;00m[37m[39;49;00m$
  3094^I[37m^I^I   [39;49;00m[37m;; `temp-buffer-resize-mode' is enabled in this[39;49;00m[37m[39;49;00m$
  3095^I[37m^I^I   [39;49;00m[37m;; buffer bind it to t so resizing steals space[39;49;00m[37m[39;49;00m$
  3096^I[37m^I^I   [39;49;00m[37m;; preferably from the window that was split.[39;49;00m[37m[39;49;00m$
  3097^I[37m^I^I   [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[32mwindow-combination-limit[39;49;00m[37m [39;49;00m[33m'temp-buffer[39;49;00m)[37m[39;49;00m$
  3098^I[37m^I^I^I   [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[32mwindow-combination-limit[39;49;00m[37m[39;49;00m$
  3099^I[37m^I^I^I^I    [39;49;00m[33m'temp-buffer-resize[39;49;00m)[37m[39;49;00m$
  3100^I[37m^I^I^I^I[39;49;00m[31mtemp-buffer-resize-mode[39;49;00m))[37m[39;49;00m$
  3101^I[37m^I^I       [39;49;00m[31mt[39;49;00m[37m[39;49;00m$
  3102^I[37m^I^I     [39;49;00m[32mwindow-combination-limit[39;49;00m)))[37m[39;49;00m$
  3103^I[37m^I^I[39;49;00m([31mdisplay-buffer[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m)))[37m[39;49;00m$
  3104^I[37m^I     [39;49;00m([31mframe[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mwindow[39;49;00m[37m [39;49;00m([32mwindow-frame[39;49;00m[37m [39;49;00m[31mwindow[39;49;00m))))[37m[39;49;00m$
  3105^I[37m^I[39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31mwindow[39;49;00m[37m[39;49;00m$
  3106^I[37m^I  [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mframe[39;49;00m[37m [39;49;00m([32mselected-frame[39;49;00m))[37m[39;49;00m$
  3107^I[37m^I    [39;49;00m([32mmake-frame-visible[39;49;00m[37m [39;49;00m[31mframe[39;49;00m))[37m[39;49;00m$
  3108^I[37m^I  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mminibuffer-scroll-window[39;49;00m[37m [39;49;00m[31mwindow[39;49;00m)[37m[39;49;00m$
  3109^I[37m^I  [39;49;00m([32mset-window-hscroll[39;49;00m[37m [39;49;00m[31mwindow[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  3110^I[37m^I  [39;49;00m[37m;; Don't try this with NOFORCE non-nil![39;49;00m[37m[39;49;00m$
  3111^I[37m^I  [39;49;00m([32mset-window-start[39;49;00m[37m [39;49;00m[31mwindow[39;49;00m[37m [39;49;00m([32mpoint-min[39;49;00m)[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
  3112^I[37m^I  [39;49;00m[37m;; This should not be necessary.[39;49;00m[37m[39;49;00m$
  3113^I[37m^I  [39;49;00m([32mset-window-point[39;49;00m[37m [39;49;00m[31mwindow[39;49;00m[37m [39;49;00m([32mpoint-min[39;49;00m))[37m[39;49;00m$
  3114^I[37m^I  [39;49;00m[37m;; Run `temp-buffer-show-hook', with the chosen window selected.[39;49;00m[37m[39;49;00m$
  3115^I[37m^I  [39;49;00m([36mwith-selected-window[39;49;00m[37m [39;49;00m[31mwindow[39;49;00m[37m[39;49;00m$
  3116^I[37m^I    [39;49;00m([32mrun-hooks[39;49;00m[37m [39;49;00m[33m'temp-buffer-show-hook[39;49;00m))))))[37m[39;49;00m$
  3117^I[37m  [39;49;00m[37m;; Return nil.[39;49;00m[37m[39;49;00m$
  3118^I[37m  [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
  3119^I[37m[39;49;00m$
  3120^I[37m;; Doc is very similar to with-temp-buffer-window.[39;49;00m[37m[39;49;00m$
  3121^I([36mdefmacro[39;49;00m[37m [39;49;00m[36mwith-output-to-temp-buffer[39;49;00m[37m [39;49;00m([31mbufname[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
  3122^I[37m  [39;49;00m[33m"[39;49;00m[33mBind [39;49;00m[33m`standard-output'[39;49;00m[33m to buffer BUFNAME, eval BODY, then show that buffer.[39;49;00m$
  3123^I[33m[39;49;00m$
  3124^I[33mThis construct makes buffer BUFNAME empty before running BODY.[39;49;00m$
  3125^I[33mIt does not make the buffer current for BODY.[39;49;00m$
  3126^I[33mInstead it binds [39;49;00m[33m`standard-output'[39;49;00m[33m to that buffer, so that output[39;49;00m$
  3127^I[33mgenerated with [39;49;00m[33m`prin1'[39;49;00m[33m and similar functions in BODY goes into[39;49;00m$
  3128^I[33mthe buffer.[39;49;00m$
  3129^I[33m[39;49;00m$
  3130^I[33mAt the end of BODY, this marks buffer BUFNAME unmodified and displays[39;49;00m$
  3131^I[33mit in a window, but does not select it.  The normal way to do this is[39;49;00m$
  3132^I[33mby calling [39;49;00m[33m`display-buffer'[39;49;00m[33m, then running [39;49;00m[33m`temp-buffer-show-hook'[39;49;00m[33m.[39;49;00m$
  3133^I[33mHowever, if [39;49;00m[33m`temp-buffer-show-function'[39;49;00m[33m is non-nil, it calls that[39;49;00m$
  3134^I[33mfunction instead (and does not run [39;49;00m[33m`temp-buffer-show-hook'[39;49;00m[33m).  The[39;49;00m$
  3135^I[33mfunction gets one argument, the buffer to display.[39;49;00m$
  3136^I[33m[39;49;00m$
  3137^I[33mThe return value of [39;49;00m[33m`with-output-to-temp-buffer'[39;49;00m[33m is the value of the[39;49;00m$
  3138^I[33mlast form in BODY.  If BODY does not finish normally, the buffer[39;49;00m$
  3139^I[33mBUFNAME is not displayed.[39;49;00m$
  3140^I[33m[39;49;00m$
  3141^I[33mThis runs the hook [39;49;00m[33m`temp-buffer-setup-hook'[39;49;00m[33m before BODY,[39;49;00m$
  3142^I[33mwith the buffer BUFNAME temporarily current.  It runs the hook[39;49;00m$
  3143^I[33m`temp-buffer-show-hook'[39;49;00m[33m after displaying buffer BUFNAME, with that[39;49;00m$
  3144^I[33mbuffer temporarily current, and the window that was used to display it[39;49;00m$
  3145^I[33mtemporarily selected.  But it doesn't run [39;49;00m[33m`temp-buffer-show-hook'[39;49;00m[33m[39;49;00m$
  3146^I[33mif it uses [39;49;00m[33m`temp-buffer-show-function'[39;49;00m[33m.[39;49;00m$
  3147^I[33m[39;49;00m$
  3148^I[33mBy default, the setup hook puts the buffer into Help mode before running BODY.[39;49;00m$
  3149^I[33mIf BODY does not change the major mode, the show hook makes the buffer[39;49;00m$
  3150^I[33mread-only, and scans it for function and variable names to make them into[39;49;00m$
  3151^I[33mclickable cross-references.[39;49;00m$
  3152^I[33m[39;49;00m$
  3153^I[33mSee the related form [39;49;00m[33m`with-temp-buffer-window'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3154^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
  3155^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mold-dir[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mold-dir[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
  3156^I[37m        [39;49;00m([31mbuf[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mbuf[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
  3157^I[37m    [39;49;00m`([34mlet*[39;49;00m[37m [39;49;00m((,[31mold-dir[39;49;00m[37m [39;49;00m[31mdefault-directory[39;49;00m)[37m[39;49;00m$
  3158^I[37m            [39;49;00m(,[31mbuf[39;49;00m[37m[39;49;00m$
  3159^I[37m             [39;49;00m([36mwith-current-buffer[39;49;00m[37m [39;49;00m([32mget-buffer-create[39;49;00m[37m [39;49;00m,[31mbufname[39;49;00m)[37m[39;49;00m$
  3160^I[37m               [39;49;00m([34mprog1[39;49;00m[37m [39;49;00m([32mcurrent-buffer[39;49;00m)[37m[39;49;00m$
  3161^I[37m                 [39;49;00m([32mkill-all-local-variables[39;49;00m)[37m[39;49;00m$
  3162^I[37m                 [39;49;00m[37m;; FIXME: delete_all_overlays[39;49;00m[37m[39;49;00m$
  3163^I[37m                 [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mdefault-directory[39;49;00m[37m [39;49;00m,[31mold-dir[39;49;00m)[37m[39;49;00m$
  3164^I[37m                 [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbuffer-read-only[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
  3165^I[37m                 [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[32mbuffer-file-name[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
  3166^I[37m                 [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbuffer-undo-list[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
  3167^I[37m                 [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31minhibit-read-only[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
  3168^I[37m                       [39;49;00m([31minhibit-modification-hooks[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
  3169^I[37m                   [39;49;00m([32merase-buffer[39;49;00m)[37m[39;49;00m$
  3170^I[37m                   [39;49;00m([32mrun-hooks[39;49;00m[37m [39;49;00m[33m'temp-buffer-setup-hook[39;49;00m)))))[37m[39;49;00m$
  3171^I[37m            [39;49;00m([31mstandard-output[39;49;00m[37m [39;49;00m,[31mbuf[39;49;00m))[37m[39;49;00m$
  3172^I[37m       [39;49;00m([34mprog1[39;49;00m[37m [39;49;00m([34mprogn[39;49;00m[37m [39;49;00m,@[31mbody[39;49;00m)[37m[39;49;00m$
  3173^I[37m         [39;49;00m([31minternal-temp-output-buffer-show[39;49;00m[37m [39;49;00m,[31mbuf[39;49;00m)))))[37m[39;49;00m$
  3174^I[37m[39;49;00m$
  3175^I([36mdefmacro[39;49;00m[37m [39;49;00m[36mwith-temp-file[39;49;00m[37m [39;49;00m([31mfile[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
  3176^I[37m  [39;49;00m[33m"[39;49;00m[33mCreate a new buffer, evaluate BODY there, and write the buffer to FILE.[39;49;00m$
  3177^I[33mThe value returned is the value of the last form in BODY.[39;49;00m$
  3178^I[33mSee also [39;49;00m[33m`with-temp-buffer'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3179^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
  3180^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtemp-file[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mtemp-file[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
  3181^I[37m^I[39;49;00m([31mtemp-buffer[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mtemp-buffer[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
  3182^I[37m    [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m((,[31mtemp-file[39;49;00m[37m [39;49;00m,[31mfile[39;49;00m)[37m[39;49;00m$
  3183^I[37m^I   [39;49;00m(,[31mtemp-buffer[39;49;00m[37m[39;49;00m$
  3184^I[37m^I    [39;49;00m([32mget-buffer-create[39;49;00m[37m [39;49;00m([32mgenerate-new-buffer-name[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m *temp file*[39;49;00m[33m"[39;49;00m))))[37m[39;49;00m$
  3185^I[37m       [39;49;00m([34munwind-protect[39;49;00m[37m[39;49;00m$
  3186^I[37m^I   [39;49;00m([34mprog1[39;49;00m[37m[39;49;00m$
  3187^I[37m^I       [39;49;00m([36mwith-current-buffer[39;49;00m[37m [39;49;00m,[31mtemp-buffer[39;49;00m[37m[39;49;00m$
  3188^I[37m^I^I [39;49;00m,@[31mbody[39;49;00m)[37m[39;49;00m$
  3189^I[37m^I     [39;49;00m([36mwith-current-buffer[39;49;00m[37m [39;49;00m,[31mtemp-buffer[39;49;00m[37m[39;49;00m$
  3190^I[37m^I       [39;49;00m([32mwrite-region[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m,[31mtemp-file[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[34m0[39;49;00m)))[37m[39;49;00m$
  3191^I[37m^I [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mbuffer-name[39;49;00m[37m [39;49;00m,[31mtemp-buffer[39;49;00m)[37m[39;49;00m$
  3192^I[37m^I      [39;49;00m([32mkill-buffer[39;49;00m[37m [39;49;00m,[31mtemp-buffer[39;49;00m))))))[37m[39;49;00m$
  3193^I[37m[39;49;00m$
  3194^I([36mdefmacro[39;49;00m[37m [39;49;00m[36mwith-temp-message[39;49;00m[37m [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
  3195^I[37m  [39;49;00m[33m"[39;49;00m[33mDisplay MESSAGE temporarily if non-nil while BODY is evaluated.[39;49;00m$
  3196^I[33mThe original message is restored to the echo area after BODY has finished.[39;49;00m$
  3197^I[33mThe value returned is the value of the last form in BODY.[39;49;00m$
  3198^I[33mMESSAGE is written to the message log buffer if [39;49;00m[33m`message-log-max'[39;49;00m[33m is non-nil.[39;49;00m$
  3199^I[33mIf MESSAGE is nil, the echo area and message log buffer are unchanged.[39;49;00m$
  3200^I[33mUse a MESSAGE of [39;49;00m[33m\"[39;49;00m[33m\"[39;49;00m[33m to temporarily clear the echo area.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3201^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m1[39;49;00m))[37m[39;49;00m$
  3202^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([32mcurrent-message[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mcurrent-message[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
  3203^I[37m^I[39;49;00m([31mtemp-message[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mwith-temp-message[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
  3204^I[37m    [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m((,[31mtemp-message[39;49;00m[37m [39;49;00m,[32mmessage[39;49;00m)[37m[39;49;00m$
  3205^I[37m^I   [39;49;00m(,[32mcurrent-message[39;49;00m))[37m[39;49;00m$
  3206^I[37m       [39;49;00m([34munwind-protect[39;49;00m[37m[39;49;00m$
  3207^I[37m^I   [39;49;00m([34mprogn[39;49;00m[37m[39;49;00m$
  3208^I[37m^I     [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m,[31mtemp-message[39;49;00m[37m[39;49;00m$
  3209^I[37m^I       [39;49;00m([34msetq[39;49;00m[37m [39;49;00m,[32mcurrent-message[39;49;00m[37m [39;49;00m([32mcurrent-message[39;49;00m))[37m[39;49;00m$
  3210^I[37m^I       [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m%s[39;49;00m[33m"[39;49;00m[37m [39;49;00m,[31mtemp-message[39;49;00m))[37m[39;49;00m$
  3211^I[37m^I     [39;49;00m,@[31mbody[39;49;00m)[37m[39;49;00m$
  3212^I[37m^I [39;49;00m([34mand[39;49;00m[37m [39;49;00m,[31mtemp-message[39;49;00m[37m[39;49;00m$
  3213^I[37m^I      [39;49;00m([34mif[39;49;00m[37m [39;49;00m,[32mcurrent-message[39;49;00m[37m[39;49;00m$
  3214^I[37m^I^I  [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m%s[39;49;00m[33m"[39;49;00m[37m [39;49;00m,[32mcurrent-message[39;49;00m)[37m[39;49;00m$
  3215^I[37m^I^I[39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)))))))[37m[39;49;00m$
  3216^I[37m[39;49;00m$
  3217^I([36mdefmacro[39;49;00m[37m [39;49;00m[36mwith-temp-buffer[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
  3218^I[37m  [39;49;00m[33m"[39;49;00m[33mCreate a temporary buffer, and evaluate BODY there like [39;49;00m[33m`progn'[39;49;00m[33m.[39;49;00m$
  3219^I[33mSee also [39;49;00m[33m`with-temp-file'[39;49;00m[33m and [39;49;00m[33m`with-output-to-string'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3220^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
  3221^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtemp-buffer[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mtemp-buffer[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
  3222^I[37m    [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m((,[31mtemp-buffer[39;49;00m[37m [39;49;00m([31mgenerate-new-buffer[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m *temp*[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
  3223^I[37m       [39;49;00m[37m;; FIXME: kill-buffer can change current-buffer in some odd cases.[39;49;00m[37m[39;49;00m$
  3224^I[37m       [39;49;00m([36mwith-current-buffer[39;49;00m[37m [39;49;00m,[31mtemp-buffer[39;49;00m[37m[39;49;00m$
  3225^I[37m         [39;49;00m([34munwind-protect[39;49;00m[37m[39;49;00m$
  3226^I[37m^I     [39;49;00m([34mprogn[39;49;00m[37m [39;49;00m,@[31mbody[39;49;00m)[37m[39;49;00m$
  3227^I[37m           [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mbuffer-name[39;49;00m[37m [39;49;00m,[31mtemp-buffer[39;49;00m)[37m[39;49;00m$
  3228^I[37m                [39;49;00m([32mkill-buffer[39;49;00m[37m [39;49;00m,[31mtemp-buffer[39;49;00m)))))))[37m[39;49;00m$
  3229^I[37m[39;49;00m$
  3230^I([36mdefmacro[39;49;00m[37m [39;49;00m[36mwith-silent-modifications[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
  3231^I[37m  [39;49;00m[33m"[39;49;00m[33mExecute BODY, pretending it does not modify the buffer.[39;49;00m$
  3232^I[33mIf BODY performs real modifications to the buffer's text, other[39;49;00m$
  3233^I[33mthan cosmetic ones, undo data may become corrupted.[39;49;00m$
  3234^I[33m[39;49;00m$
  3235^I[33mThis macro will run BODY normally, but doesn't count its buffer[39;49;00m$
  3236^I[33mmodifications as being buffer modifications.  This affects things[39;49;00m$
  3237^I[33mlike [39;49;00m[33m`buffer-modified-p'[39;49;00m[33m, checking whether the file is locked by[39;49;00m$
  3238^I[33msomeone else, running buffer modification hooks, and other things[39;49;00m$
  3239^I[33mof that nature.[39;49;00m$
  3240^I[33m[39;49;00m$
  3241^I[33mTypically used around modifications of text-properties which do[39;49;00m$
  3242^I[33mnot really affect the buffer's content.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3243^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m$
  3244^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mmodified[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mmodified[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
  3245^I[37m    [39;49;00m`([34mlet*[39;49;00m[37m [39;49;00m((,[31mmodified[39;49;00m[37m [39;49;00m([32mbuffer-modified-p[39;49;00m))[37m[39;49;00m$
  3246^I[37m            [39;49;00m([31mbuffer-undo-list[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
  3247^I[37m            [39;49;00m([31minhibit-read-only[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
  3248^I[37m            [39;49;00m([31minhibit-modification-hooks[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
  3249^I[37m       [39;49;00m([34munwind-protect[39;49;00m[37m[39;49;00m$
  3250^I[37m           [39;49;00m([34mprogn[39;49;00m[37m[39;49;00m$
  3251^I[37m             [39;49;00m,@[31mbody[39;49;00m)[37m[39;49;00m$
  3252^I[37m         [39;49;00m([36munless[39;49;00m[37m [39;49;00m,[31mmodified[39;49;00m[37m[39;49;00m$
  3253^I[37m           [39;49;00m([32mrestore-buffer-modified-p[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))))))[37m[39;49;00m$
  3254^I[37m[39;49;00m$
  3255^I([36mdefmacro[39;49;00m[37m [39;49;00m[36mwith-output-to-string[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
  3256^I[37m  [39;49;00m[33m"[39;49;00m[33mExecute BODY, return the text it sent to [39;49;00m[33m`standard-output'[39;49;00m[33m, as a string.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3257^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
  3258^I[37m  [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m(([31mstandard-output[39;49;00m[37m[39;49;00m$
  3259^I[37m^I  [39;49;00m([32mget-buffer-create[39;49;00m[37m [39;49;00m([32mgenerate-new-buffer-name[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m *string-output*[39;49;00m[33m"[39;49;00m))))[37m[39;49;00m$
  3260^I[37m     [39;49;00m([34munwind-protect[39;49;00m[37m[39;49;00m$
  3261^I[37m^I [39;49;00m([34mprogn[39;49;00m[37m[39;49;00m$
  3262^I[37m^I   [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mstandard-output[39;49;00m[37m [39;49;00m[31mstandard-output[39;49;00m))[37m[39;49;00m$
  3263^I[37m^I     [39;49;00m,@[31mbody[39;49;00m)[37m[39;49;00m$
  3264^I[37m^I   [39;49;00m([36mwith-current-buffer[39;49;00m[37m [39;49;00m[31mstandard-output[39;49;00m[37m[39;49;00m$
  3265^I[37m^I     [39;49;00m([32mbuffer-string[39;49;00m)))[37m[39;49;00m$
  3266^I[37m       [39;49;00m([32mkill-buffer[39;49;00m[37m [39;49;00m[31mstandard-output[39;49;00m))))[37m[39;49;00m$
  3267^I[37m[39;49;00m$
  3268^I([36mdefmacro[39;49;00m[37m [39;49;00m[36mwith-local-quit[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
  3269^I[37m  [39;49;00m[33m"[39;49;00m[33mExecute BODY, allowing quits to terminate BODY but not escape further.[39;49;00m$
  3270^I[33mWhen a quit terminates BODY, [39;49;00m[33m`with-local-quit'[39;49;00m[33m returns nil but[39;49;00m$
  3271^I[33mrequests another quit.  That quit will be processed as soon as quitting[39;49;00m$
  3272^I[33mis allowed once again.  (Immediately, if [39;49;00m[33m`inhibit-quit'[39;49;00m[33m is nil.)[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3273^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m$
  3274^I[37m  [39;49;00m`([34mcondition-case[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m$
  3275^I[37m       [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31minhibit-quit[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m$
  3276^I[37m^I [39;49;00m,@[31mbody[39;49;00m)[37m[39;49;00m$
  3277^I[37m     [39;49;00m([31mquit[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mquit-flag[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
  3278^I[37m^I   [39;49;00m[37m;; This call is to give a chance to handle quit-flag[39;49;00m[37m[39;49;00m$
  3279^I[37m^I   [39;49;00m[37m;; in case inhibit-quit is nil.[39;49;00m[37m[39;49;00m$
  3280^I[37m^I   [39;49;00m[37m;; Without this, it will not be handled until the next function[39;49;00m[37m[39;49;00m$
  3281^I[37m^I   [39;49;00m[37m;; call, and that might allow it to exit thru a condition-case[39;49;00m[37m[39;49;00m$
  3282^I[37m^I   [39;49;00m[37m;; that intends to handle the quit signal next time.[39;49;00m[37m[39;49;00m$
  3283^I[37m^I   [39;49;00m([32meval[39;49;00m[37m [39;49;00m'([31mignore[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)))))[37m[39;49;00m$
  3284^I[37m[39;49;00m$
  3285^I([36mdefmacro[39;49;00m[37m [39;49;00m[36mwhile-no-input[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
  3286^I[37m  [39;49;00m[33m"[39;49;00m[33mExecute BODY only as long as there's no pending input.[39;49;00m$
  3287^I[33mIf input arrives, that ends the execution of BODY,[39;49;00m$
  3288^I[33mand [39;49;00m[33m`while-no-input'[39;49;00m[33m returns t.  Quitting makes it return nil.[39;49;00m$
  3289^I[33mIf BODY finishes, [39;49;00m[33m`while-no-input'[39;49;00m[33m returns whatever value BODY produced.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3290^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m$
  3291^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mcatch-sym[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33minput[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
  3292^I[37m    [39;49;00m`([36mwith-local-quit[39;49;00m[37m[39;49;00m$
  3293^I[37m       [39;49;00m([34mcatch[39;49;00m[37m [39;49;00m[33m',catch-sym[39;49;00m[37m[39;49;00m$
  3294^I[37m^I [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mthrow-on-input[39;49;00m[37m [39;49;00m[33m',catch-sym[39;49;00m))[37m[39;49;00m$
  3295^I[37m^I   [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32minput-pending-p[39;49;00m)[37m[39;49;00m$
  3296^I[37m^I       [39;49;00m([34mprogn[39;49;00m[37m [39;49;00m,@[31mbody[39;49;00m)))))))[37m[39;49;00m$
  3297^I[37m[39;49;00m$
  3298^I([36mdefmacro[39;49;00m[37m [39;49;00m[36mcondition-case-unless-debug[39;49;00m[37m [39;49;00m([31mvar[39;49;00m[37m [39;49;00m[31mbodyform[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mhandlers[39;49;00m)[37m[39;49;00m$
  3299^I[37m  [39;49;00m[33m"[39;49;00m[33mLike [39;49;00m[33m`condition-case'[39;49;00m[33m except that it does not prevent debugging.[39;49;00m$
  3300^I[33mMore specifically if [39;49;00m[33m`debug-on-error'[39;49;00m[33m is set then the debugger will be invoked[39;49;00m$
  3301^I[33meven if this catches the signal.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3302^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[34mcondition-case[39;49;00m)[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m2[39;49;00m))[37m[39;49;00m$
  3303^I[37m  [39;49;00m`([34mcondition-case[39;49;00m[37m [39;49;00m,[31mvar[39;49;00m[37m[39;49;00m$
  3304^I[37m       [39;49;00m,[31mbodyform[39;49;00m[37m[39;49;00m$
  3305^I[37m     [39;49;00m,@([32mmapcar[39;49;00m[37m [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31mhandler[39;49;00m)[37m[39;49;00m$
  3306^I[37m                 [39;49;00m`(([31mdebug[39;49;00m[37m [39;49;00m,@([34mif[39;49;00m[37m [39;49;00m([32mlistp[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mhandler[39;49;00m))[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mhandler[39;49;00m)[37m[39;49;00m$
  3307^I[37m                              [39;49;00m([32mlist[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mhandler[39;49;00m))))[37m[39;49;00m$
  3308^I[37m                   [39;49;00m,@([32mcdr[39;49;00m[37m [39;49;00m[31mhandler[39;49;00m)))[37m[39;49;00m$
  3309^I[37m               [39;49;00m[31mhandlers[39;49;00m)))[37m[39;49;00m$
  3310^I[37m[39;49;00m$
  3311^I([36mdefine-obsolete-function-alias[39;49;00m[37m [39;49;00m[33m'condition-case-no-debug[39;49;00m[37m[39;49;00m$
  3312^I[37m  [39;49;00m[33m'condition-case-unless-debug[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m24.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  3313^I[37m[39;49;00m$
  3314^I([36mdefmacro[39;49;00m[37m [39;49;00m[36mwith-demoted-errors[39;49;00m[37m [39;49;00m([32mformat[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
  3315^I[37m  [39;49;00m[33m"[39;49;00m[33mRun BODY and demote any errors to simple messages.[39;49;00m$
  3316^I[33mFORMAT is a string passed to [39;49;00m[33m`message'[39;49;00m[33m to format any error message.[39;49;00m$
  3317^I[33mIt should contain a single %-sequence; e.g., [39;49;00m[33m\"[39;49;00m[33mError: %S[39;49;00m[33m\"[39;49;00m[33m.[39;49;00m$
  3318^I[33m[39;49;00m$
  3319^I[33mIf [39;49;00m[33m`debug-on-error'[39;49;00m[33m is non-nil, run BODY without catching its errors.[39;49;00m$
  3320^I[33mThis is to be used around code which is not expected to signal an error[39;49;00m$
  3321^I[33mbut which should be robust in the unexpected case that an error is signaled.[39;49;00m$
  3322^I[33m[39;49;00m$
  3323^I[33mFor backward compatibility, if FORMAT is not a constant string, it[39;49;00m$
  3324^I[33mis assumed to be part of BODY, in which case the message format[39;49;00m$
  3325^I[33mused is [39;49;00m[33m\"[39;49;00m[33mError: %S[39;49;00m[33m\"[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3326^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m1[39;49;00m))[37m[39;49;00m$
  3327^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31merr[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33merr[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
  3328^I[37m        [39;49;00m([32mformat[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m[32mformat[39;49;00m)[37m [39;49;00m[31mbody[39;49;00m)[37m [39;49;00m[32mformat[39;49;00m[37m[39;49;00m$
  3329^I[37m                  [39;49;00m([34mprog1[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mError: %S[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3330^I[37m                    [39;49;00m([34mif[39;49;00m[37m [39;49;00m[32mformat[39;49;00m[37m [39;49;00m([36mpush[39;49;00m[37m [39;49;00m[32mformat[39;49;00m[37m [39;49;00m[31mbody[39;49;00m))))))[37m[39;49;00m$
  3331^I[37m    [39;49;00m`([36mcondition-case-unless-debug[39;49;00m[37m [39;49;00m,[31merr[39;49;00m[37m[39;49;00m$
  3332^I[37m         [39;49;00m,([31mmacroexp-progn[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
  3333^I[37m       [39;49;00m([36merror[39;49;00m[37m [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m,[32mformat[39;49;00m[37m [39;49;00m,[31merr[39;49;00m)[37m [39;49;00m[31mnil[39;49;00m))))[37m[39;49;00m$
  3334^I[37m[39;49;00m$
  3335^I([36mdefmacro[39;49;00m[37m [39;49;00m[36mcombine-after-change-calls[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
  3336^I[37m  [39;49;00m[33m"[39;49;00m[33mExecute BODY, but don't call the after-change functions till the end.[39;49;00m$
  3337^I[33mIf BODY makes changes in the buffer, they are recorded[39;49;00m$
  3338^I[33mand the functions on [39;49;00m[33m`after-change-functions'[39;49;00m[33m are called several times[39;49;00m$
  3339^I[33mwhen BODY is finished.[39;49;00m$
  3340^I[33mThe return value is the value of the last form in BODY.[39;49;00m$
  3341^I[33m[39;49;00m$
  3342^I[33mIf [39;49;00m[33m`before-change-functions'[39;49;00m[33m is non-nil, then calls to the after-change[39;49;00m$
  3343^I[33mfunctions can't be deferred, so in that case this macro has no effect.[39;49;00m$
  3344^I[33m[39;49;00m$
  3345^I[33mDo not alter [39;49;00m[33m`after-change-functions'[39;49;00m[33m or [39;49;00m[33m`before-change-functions'[39;49;00m[33m[39;49;00m$
  3346^I[33min BODY.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3347^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
  3348^I[37m  [39;49;00m`([34munwind-protect[39;49;00m[37m[39;49;00m$
  3349^I[37m       [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([36mcombine-after-change-calls[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
  3350^I[37m^I [39;49;00m.[37m [39;49;00m,[31mbody[39;49;00m)[37m[39;49;00m$
  3351^I[37m     [39;49;00m([32mcombine-after-change-execute[39;49;00m)))[37m[39;49;00m$
  3352^I[37m[39;49;00m$
  3353^I([36mdefmacro[39;49;00m[37m [39;49;00m[36mwith-case-table[39;49;00m[37m [39;49;00m([31mtable[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
  3354^I[37m  [39;49;00m[33m"[39;49;00m[33mExecute the forms in BODY with TABLE as the current case table.[39;49;00m$
  3355^I[33mThe value returned is the value of the last form in BODY.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3356^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
  3357^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mold-case-table[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mtable[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
  3358^I[37m^I[39;49;00m([31mold-buffer[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mbuffer[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
  3359^I[37m    [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m((,[31mold-case-table[39;49;00m[37m [39;49;00m([32mcurrent-case-table[39;49;00m))[37m[39;49;00m$
  3360^I[37m^I   [39;49;00m(,[31mold-buffer[39;49;00m[37m [39;49;00m([32mcurrent-buffer[39;49;00m)))[37m[39;49;00m$
  3361^I[37m       [39;49;00m([34munwind-protect[39;49;00m[37m[39;49;00m$
  3362^I[37m^I   [39;49;00m([34mprogn[39;49;00m[37m [39;49;00m([32mset-case-table[39;49;00m[37m [39;49;00m,[31mtable[39;49;00m)[37m[39;49;00m$
  3363^I[37m^I^I  [39;49;00m,@[31mbody[39;49;00m)[37m[39;49;00m$
  3364^I[37m^I [39;49;00m([36mwith-current-buffer[39;49;00m[37m [39;49;00m,[31mold-buffer[39;49;00m[37m[39;49;00m$
  3365^I[37m^I   [39;49;00m([32mset-case-table[39;49;00m[37m [39;49;00m,[31mold-case-table[39;49;00m))))))[37m[39;49;00m$
  3366^I[37m[39;49;00m$
  3367^I([36mdefmacro[39;49;00m[37m [39;49;00m[36mwith-file-modes[39;49;00m[37m [39;49;00m([31mmodes[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
  3368^I[37m  [39;49;00m[33m"[39;49;00m[33mExecute BODY with default file permissions temporarily set to MODES.[39;49;00m$
  3369^I[33mMODES is as for [39;49;00m[33m`set-default-file-modes'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3370^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
  3371^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mumask[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mumask[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
  3372^I[37m    [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m((,[31mumask[39;49;00m[37m [39;49;00m([32mdefault-file-modes[39;49;00m)))[37m[39;49;00m$
  3373^I[37m       [39;49;00m([34munwind-protect[39;49;00m[37m[39;49;00m$
  3374^I[37m           [39;49;00m([34mprogn[39;49;00m[37m[39;49;00m$
  3375^I[37m             [39;49;00m([32mset-default-file-modes[39;49;00m[37m [39;49;00m,[31mmodes[39;49;00m)[37m[39;49;00m$
  3376^I[37m             [39;49;00m,@[31mbody[39;49;00m)[37m[39;49;00m$
  3377^I[37m         [39;49;00m([32mset-default-file-modes[39;49;00m[37m [39;49;00m,[31mumask[39;49;00m)))))[37m[39;49;00m$
  3378^I[37m[39;49;00m$
  3379^I[37m[39;49;00m[37m[39;49;00m$
  3380^I[37m;;; Matching and match data.[39;49;00m[37m[39;49;00m$
  3381^I[37m[39;49;00m$
  3382^I([34mdefvar[39;49;00m[37m [39;49;00m[31msave-match-data-internal[39;49;00m)[37m[39;49;00m$
  3383^I[37m[39;49;00m$
  3384^I[37m;; We use save-match-data-internal as the local variable because[39;49;00m[37m[39;49;00m$
  3385^I[37m;; that works ok in practice (people should not use that variable elsewhere).[39;49;00m[37m[39;49;00m$
  3386^I[37m;; We used to use an uninterned symbol; the compiler handles that properly[39;49;00m[37m[39;49;00m$
  3387^I[37m;; now, but it generates slower code.[39;49;00m[37m[39;49;00m$
  3388^I([36mdefmacro[39;49;00m[37m [39;49;00m[36msave-match-data[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
  3389^I[37m  [39;49;00m[33m"[39;49;00m[33mExecute the BODY forms, restoring the global value of the match data.[39;49;00m$
  3390^I[33mThe value returned is the value of the last form in BODY.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3391^I[37m  [39;49;00m[37m;; It is better not to use backquote here,[39;49;00m[37m[39;49;00m$
  3392^I[37m  [39;49;00m[37m;; because that makes a bootstrapping problem[39;49;00m[37m[39;49;00m$
  3393^I[37m  [39;49;00m[37m;; if you need to recompile all the Lisp files using interpreted code.[39;49;00m[37m[39;49;00m$
  3394^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
  3395^I[37m  [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'let[39;49;00m[37m[39;49;00m$
  3396^I[37m^I[39;49;00m'(([31msave-match-data-internal[39;49;00m[37m [39;49;00m([32mmatch-data[39;49;00m)))[37m[39;49;00m$
  3397^I[37m^I[39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'unwind-protect[39;49;00m[37m[39;49;00m$
  3398^I[37m^I      [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[33m'progn[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
  3399^I[37m^I      [39;49;00m[37m;; It is safe to free (evaporate) markers immediately here,[39;49;00m[37m[39;49;00m$
  3400^I[37m^I      [39;49;00m[37m;; as Lisp programs should not copy from save-match-data-internal.[39;49;00m[37m[39;49;00m$
  3401^I[37m^I      [39;49;00m'([32mset-match-data[39;49;00m[37m [39;49;00m[31msave-match-data-internal[39;49;00m[37m [39;49;00m[33m'evaporate[39;49;00m))))[37m[39;49;00m$
  3402^I[37m[39;49;00m$
  3403^I([36mdefun[39;49;00m[37m [39;49;00m[31mmatch-string[39;49;00m[37m [39;49;00m([31mnum[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[32mstring[39;49;00m)[37m[39;49;00m$
  3404^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn string of text matched by last search.[39;49;00m$
  3405^I[33mNUM specifies which parenthesized expression in the last regexp.[39;49;00m$
  3406^I[33m Value is nil if NUMth pair didn't match, or there were less than NUM pairs.[39;49;00m$
  3407^I[33mZero means the entire text matched by the whole regexp or whole string.[39;49;00m$
  3408^I[33mSTRING should be given if the last search was by [39;49;00m[33m`string-match'[39;49;00m[33m on STRING.[39;49;00m$
  3409^I[33mIf STRING is nil, the current buffer should be the same buffer[39;49;00m$
  3410^I[33mthe search/match was performed in.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3411^I[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mmatch-beginning[39;49;00m[37m [39;49;00m[31mnum[39;49;00m)[37m[39;49;00m$
  3412^I[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m[39;49;00m$
  3413^I[37m^I  [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m([32mmatch-beginning[39;49;00m[37m [39;49;00m[31mnum[39;49;00m)[37m [39;49;00m([32mmatch-end[39;49;00m[37m [39;49;00m[31mnum[39;49;00m))[37m[39;49;00m$
  3414^I[37m^I[39;49;00m([32mbuffer-substring[39;49;00m[37m [39;49;00m([32mmatch-beginning[39;49;00m[37m [39;49;00m[31mnum[39;49;00m)[37m [39;49;00m([32mmatch-end[39;49;00m[37m [39;49;00m[31mnum[39;49;00m)))))[37m[39;49;00m$
  3415^I[37m[39;49;00m$
  3416^I([36mdefun[39;49;00m[37m [39;49;00m[31mmatch-string-no-properties[39;49;00m[37m [39;49;00m([31mnum[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[32mstring[39;49;00m)[37m[39;49;00m$
  3417^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn string of text matched by last search, without text properties.[39;49;00m$
  3418^I[33mNUM specifies which parenthesized expression in the last regexp.[39;49;00m$
  3419^I[33m Value is nil if NUMth pair didn't match, or there were less than NUM pairs.[39;49;00m$
  3420^I[33mZero means the entire text matched by the whole regexp or whole string.[39;49;00m$
  3421^I[33mSTRING should be given if the last search was by [39;49;00m[33m`string-match'[39;49;00m[33m on STRING.[39;49;00m$
  3422^I[33mIf STRING is nil, the current buffer should be the same buffer[39;49;00m$
  3423^I[33mthe search/match was performed in.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3424^I[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mmatch-beginning[39;49;00m[37m [39;49;00m[31mnum[39;49;00m)[37m[39;49;00m$
  3425^I[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m[39;49;00m$
  3426^I[37m^I  [39;49;00m([32msubstring-no-properties[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m([32mmatch-beginning[39;49;00m[37m [39;49;00m[31mnum[39;49;00m)[37m[39;49;00m$
  3427^I[37m^I^I^I^I   [39;49;00m([32mmatch-end[39;49;00m[37m [39;49;00m[31mnum[39;49;00m))[37m[39;49;00m$
  3428^I[37m^I[39;49;00m([32mbuffer-substring-no-properties[39;49;00m[37m [39;49;00m([32mmatch-beginning[39;49;00m[37m [39;49;00m[31mnum[39;49;00m)[37m[39;49;00m$
  3429^I[37m^I^I^I^I^I[39;49;00m([32mmatch-end[39;49;00m[37m [39;49;00m[31mnum[39;49;00m)))))[37m[39;49;00m$
  3430^I[37m[39;49;00m$
  3431^I[37m[39;49;00m$
  3432^I([36mdefun[39;49;00m[37m [39;49;00m[31mmatch-substitute-replacement[39;49;00m[37m [39;49;00m([31mreplacement[39;49;00m[37m[39;49;00m$
  3433^I[37m^I^I^I^I     [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mfixedcase[39;49;00m[37m [39;49;00m[31mliteral[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[31msubexp[39;49;00m)[37m[39;49;00m$
  3434^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn REPLACEMENT as it will be inserted by [39;49;00m[33m`replace-match'[39;49;00m[33m.[39;49;00m$
  3435^I[33mIn other words, all back-references in the form [39;49;00m[33m`\\&'[39;49;00m[33m and [39;49;00m[33m`\\N'[39;49;00m[33m[39;49;00m$
  3436^I[33mare substituted with actual strings matched by the last search.[39;49;00m$
  3437^I[33mOptional FIXEDCASE, LITERAL, STRING and SUBEXP have the same[39;49;00m$
  3438^I[33mmeaning as for [39;49;00m[33m`replace-match'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3439^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mmatch[39;49;00m[37m [39;49;00m([31mmatch-string[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[32mstring[39;49;00m)))[37m[39;49;00m$
  3440^I[37m    [39;49;00m([36msave-match-data[39;49;00m[37m[39;49;00m$
  3441^I[37m      [39;49;00m([32mset-match-data[39;49;00m[37m [39;49;00m([32mmapcar[39;49;00m[37m [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31mx[39;49;00m)[37m[39;49;00m$
  3442^I[37m^I^I^I^I[39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mnumberp[39;49;00m[37m [39;49;00m[31mx[39;49;00m)[37m[39;49;00m$
  3443^I[37m^I^I^I^I    [39;49;00m([32m-[39;49;00m[37m [39;49;00m[31mx[39;49;00m[37m [39;49;00m([32mmatch-beginning[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m$
  3444^I[37m^I^I^I^I  [39;49;00m[31mx[39;49;00m))[37m[39;49;00m$
  3445^I[37m^I^I^I      [39;49;00m([32mmatch-data[39;49;00m[37m [39;49;00m[31mt[39;49;00m)))[37m[39;49;00m$
  3446^I[37m      [39;49;00m([32mreplace-match[39;49;00m[37m [39;49;00m[31mreplacement[39;49;00m[37m [39;49;00m[31mfixedcase[39;49;00m[37m [39;49;00m[31mliteral[39;49;00m[37m [39;49;00m[31mmatch[39;49;00m[37m [39;49;00m[31msubexp[39;49;00m))))[37m[39;49;00m$
  3447^I[37m[39;49;00m$
  3448^I[37m[39;49;00m$
  3449^I([36mdefun[39;49;00m[37m [39;49;00m[31mlooking-back[39;49;00m[37m [39;49;00m([31mregexp[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mlimit[39;49;00m[37m [39;49;00m[31mgreedy[39;49;00m)[37m[39;49;00m$
  3450^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn non-nil if text before point matches regular expression REGEXP.[39;49;00m$
  3451^I[33mLike [39;49;00m[33m`looking-at'[39;49;00m[33m except matches before point, and is slower.[39;49;00m$
  3452^I[33mLIMIT if non-nil speeds up the search by specifying a minimum[39;49;00m$
  3453^I[33mstarting position, to avoid checking matches that would start[39;49;00m$
  3454^I[33mbefore LIMIT.[39;49;00m$
  3455^I[33m[39;49;00m$
  3456^I[33mIf GREEDY is non-nil, extend the match backwards as far as[39;49;00m$
  3457^I[33mpossible, stopping when a single additional previous character[39;49;00m$
  3458^I[33mcannot be part of a match for REGEXP.  When the match is[39;49;00m$
  3459^I[33mextended, its starting position is allowed to occur before[39;49;00m$
  3460^I[33mLIMIT.[39;49;00m$
  3461^I[33m[39;49;00m$
  3462^I[33mAs a general recommendation, try to avoid using [39;49;00m[33m`looking-back'[39;49;00m[33m[39;49;00m$
  3463^I[33mwherever possible, since it is slow.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3464^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mstart[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m))[37m[39;49;00m$
  3465^I[37m^I[39;49;00m([31mpos[39;49;00m[37m[39;49;00m$
  3466^I[37m^I [39;49;00m([34msave-excursion[39;49;00m[37m[39;49;00m$
  3467^I[37m^I   [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mre-search-backward[39;49;00m[37m [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m(?:[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mregexp[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m)[39;49;00m[33m\\[39;49;00m[33m=[39;49;00m[33m"[39;49;00m)[37m [39;49;00m[31mlimit[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
  3468^I[37m^I^I[39;49;00m([32mpoint[39;49;00m)))))[37m[39;49;00m$
  3469^I[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mgreedy[39;49;00m[37m [39;49;00m[31mpos[39;49;00m)[37m[39;49;00m$
  3470^I[37m^I[39;49;00m([34msave-restriction[39;49;00m[37m[39;49;00m$
  3471^I[37m^I  [39;49;00m([32mnarrow-to-region[39;49;00m[37m [39;49;00m([32mpoint-min[39;49;00m)[37m [39;49;00m[31mstart[39;49;00m)[37m[39;49;00m$
  3472^I[37m^I  [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m[31mpos[39;49;00m[37m [39;49;00m([32mpoint-min[39;49;00m))[37m[39;49;00m$
  3473^I[37m^I^I      [39;49;00m([34msave-excursion[39;49;00m[37m[39;49;00m$
  3474^I[37m^I^I^I[39;49;00m([32mgoto-char[39;49;00m[37m [39;49;00m[31mpos[39;49;00m)[37m[39;49;00m$
  3475^I[37m^I^I^I[39;49;00m([32mbackward-char[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m[39;49;00m$
  3476^I[37m^I^I^I[39;49;00m([32mlooking-at[39;49;00m[37m [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m(?:[39;49;00m[33m"[39;49;00m[37m  [39;49;00m[31mregexp[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m)[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m[33m"[39;49;00m))))[37m[39;49;00m$
  3477^I[37m^I    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mpos[39;49;00m[37m [39;49;00m([32m1-[39;49;00m[37m [39;49;00m[31mpos[39;49;00m)))[37m[39;49;00m$
  3478^I[37m^I  [39;49;00m([34msave-excursion[39;49;00m[37m[39;49;00m$
  3479^I[37m^I    [39;49;00m([32mgoto-char[39;49;00m[37m [39;49;00m[31mpos[39;49;00m)[37m[39;49;00m$
  3480^I[37m^I    [39;49;00m([32mlooking-at[39;49;00m[37m [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m(?:[39;49;00m[33m"[39;49;00m[37m  [39;49;00m[31mregexp[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m)[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m[33m"[39;49;00m)))))[37m[39;49;00m$
  3481^I[37m    [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[31mpos[39;49;00m))))[37m[39;49;00m$
  3482^I[37m[39;49;00m$
  3483^I([36mdefsubst[39;49;00m[37m [39;49;00m[31mlooking-at-p[39;49;00m[37m [39;49;00m([31mregexp[39;49;00m)[37m[39;49;00m$
  3484^I[37m  [39;49;00m[33m"[39;49;00m[33m\[39;49;00m$
  3485^I[33mSame as [39;49;00m[33m`looking-at'[39;49;00m[33m except this function does not change the match data.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3486^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31minhibit-changing-match-data[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
  3487^I[37m    [39;49;00m([32mlooking-at[39;49;00m[37m [39;49;00m[31mregexp[39;49;00m)))[37m[39;49;00m$
  3488^I[37m[39;49;00m$
  3489^I([36mdefsubst[39;49;00m[37m [39;49;00m[31mstring-match-p[39;49;00m[37m [39;49;00m([31mregexp[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mstart[39;49;00m)[37m[39;49;00m$
  3490^I[37m  [39;49;00m[33m"[39;49;00m[33m\[39;49;00m$
  3491^I[33mSame as [39;49;00m[33m`string-match'[39;49;00m[33m except this function does not change the match data.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3492^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31minhibit-changing-match-data[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
  3493^I[37m    [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[31mregexp[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[31mstart[39;49;00m)))[37m[39;49;00m$
  3494^I[37m[39;49;00m$
  3495^I([36mdefun[39;49;00m[37m [39;49;00m[31msubregexp-context-p[39;49;00m[37m [39;49;00m([31mregexp[39;49;00m[37m [39;49;00m[31mpos[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mstart[39;49;00m)[37m[39;49;00m$
  3496^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn non-nil if POS is in a normal subregexp context in REGEXP.[39;49;00m$
  3497^I[33mA subregexp context is one where a sub-regexp can appear.[39;49;00m$
  3498^I[33mA non-subregexp context is for example within brackets, or within a[39;49;00m$
  3499^I[33mrepetition bounds operator [39;49;00m[33m`\\=\\{...\\}'[39;49;00m[33m, or right after a [39;49;00m[33m`\\'[39;49;00m[33m.[39;49;00m$
  3500^I[33mIf START is non-nil, it should be a position in REGEXP, smaller[39;49;00m$
  3501^I[33mthan POS, and known to be in a subregexp context.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3502^I[37m  [39;49;00m[37m;; Here's one possible implementation, with the great benefit that it[39;49;00m[37m[39;49;00m$
  3503^I[37m  [39;49;00m[37m;; reuses the regexp-matcher's own parser, so it understands all the[39;49;00m[37m[39;49;00m$
  3504^I[37m  [39;49;00m[37m;; details of the syntax.  A disadvantage is that it needs to match the[39;49;00m[37m[39;49;00m$
  3505^I[37m  [39;49;00m[37m;; error string.[39;49;00m[37m[39;49;00m$
  3506^I[37m  [39;49;00m([34mcondition-case[39;49;00m[37m [39;49;00m[31merr[39;49;00m[37m[39;49;00m$
  3507^I[37m      [39;49;00m([34mprogn[39;49;00m[37m[39;49;00m$
  3508^I[37m        [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[31mregexp[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[31mpos[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  3509^I[37m        [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
  3510^I[37m    [39;49;00m([31minvalid-regexp[39;49;00m[37m[39;49;00m$
  3511^I[37m     [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mmember[39;49;00m[37m [39;49;00m([31mcadr[39;49;00m[37m [39;49;00m[31merr[39;49;00m)[37m [39;49;00m'([33m"[39;49;00m[33mUnmatched [ or [^[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3512^I[37m                               [39;49;00m[33m"[39;49;00m[33mUnmatched [39;49;00m[33m\\[39;49;00m[33m{[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3513^I[37m                               [39;49;00m[33m"[39;49;00m[33mTrailing backslash[39;49;00m[33m"[39;49;00m)))))[37m[39;49;00m$
  3514^I[37m  [39;49;00m[37m;; An alternative implementation:[39;49;00m[37m[39;49;00m$
  3515^I[37m  [39;49;00m[37m;; (defconst re-context-re[39;49;00m[37m[39;49;00m$
  3516^I[37m  [39;49;00m[37m;;   (let* ((harmless-ch "[^\\[]")[39;49;00m[37m[39;49;00m$
  3517^I[37m  [39;49;00m[37m;;          (harmless-esc "\\\\[^{]")[39;49;00m[37m[39;49;00m$
  3518^I[37m  [39;49;00m[37m;;          (class-harmless-ch "[^][]")[39;49;00m[37m[39;49;00m$
  3519^I[37m  [39;49;00m[37m;;          (class-lb-harmless "[^]:]")[39;49;00m[37m[39;49;00m$
  3520^I[37m  [39;49;00m[37m;;          (class-lb-colon-maybe-charclass ":\\([a-z]+:]\\)?")[39;49;00m[37m[39;49;00m$
  3521^I[37m  [39;49;00m[37m;;          (class-lb (concat "\\[\\(" class-lb-harmless[39;49;00m[37m[39;49;00m$
  3522^I[37m  [39;49;00m[37m;;                            "\\|" class-lb-colon-maybe-charclass "\\)"))[39;49;00m[37m[39;49;00m$
  3523^I[37m  [39;49;00m[37m;;          (class[39;49;00m[37m[39;49;00m$
  3524^I[37m  [39;49;00m[37m;;           (concat "\\[^?]?"[39;49;00m[37m[39;49;00m$
  3525^I[37m  [39;49;00m[37m;;                   "\\(" class-harmless-ch[39;49;00m[37m[39;49;00m$
  3526^I[37m  [39;49;00m[37m;;                   "\\|" class-lb "\\)*"[39;49;00m[37m[39;49;00m$
  3527^I[37m  [39;49;00m[37m;;                   "\\[?]"))     ; special handling for bare [ at end of re[39;49;00m[37m[39;49;00m$
  3528^I[37m  [39;49;00m[37m;;          (braces "\\\\{[0-9,]+\\\\}"))[39;49;00m[37m[39;49;00m$
  3529^I[37m  [39;49;00m[37m;;     (concat "\\`\\(" harmless-ch "\\|" harmless-esc[39;49;00m[37m[39;49;00m$
  3530^I[37m  [39;49;00m[37m;;             "\\|" class "\\|" braces "\\)*\\'"))[39;49;00m[37m[39;49;00m$
  3531^I[37m  [39;49;00m[37m;;   "Matches any prefix that corresponds to a normal subregexp context.")[39;49;00m[37m[39;49;00m$
  3532^I[37m  [39;49;00m[37m;; (string-match re-context-re (substring regexp (or start 0) pos))[39;49;00m[37m[39;49;00m$
  3533^I[37m  [39;49;00m)[37m[39;49;00m$
  3534^I[37m[39;49;00m[37m[39;49;00m$
  3535^I[37m;;;; split-string[39;49;00m[37m[39;49;00m$
  3536^I[37m[39;49;00m$
  3537^I([34mdefconst[39;49;00m[37m [39;49;00m[31msplit-string-default-separators[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m[ [39;49;00m[33m\f[39;49;00m[33m\t[39;49;00m[33m\n[39;49;00m[33m\r[39;49;00m[33m\v[39;49;00m[33m]+[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3538^I[37m  [39;49;00m[33m"[39;49;00m[33mThe default value of separators for [39;49;00m[33m`split-string'[39;49;00m[33m.[39;49;00m$
  3539^I[33m[39;49;00m$
  3540^I[33mA regexp matching strings of whitespace.  May be locale-dependent[39;49;00m$
  3541^I[33m\([39;49;00m[33mas yet unimplemented).  Should not match non-breaking spaces.[39;49;00m$
  3542^I[33m[39;49;00m$
  3543^I[33mWarning: binding this to a different value and using it as default is[39;49;00m$
  3544^I[33mlikely to have undesired semantics.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  3545^I[37m[39;49;00m$
  3546^I[37m;; The specification says that if both SEPARATORS and OMIT-NULLS are[39;49;00m[37m[39;49;00m$
  3547^I[37m;; defaulted, OMIT-NULLS should be treated as t.  Simplifying the logical[39;49;00m[37m[39;49;00m$
  3548^I[37m;; expression leads to the equivalent implementation that if SEPARATORS[39;49;00m[37m[39;49;00m$
  3549^I[37m;; is defaulted, OMIT-NULLS is treated as t.[39;49;00m[37m[39;49;00m$
  3550^I([36mdefun[39;49;00m[37m [39;49;00m[31msplit-string[39;49;00m[37m [39;49;00m([32mstring[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mseparators[39;49;00m[37m [39;49;00m[31momit-nulls[39;49;00m[37m [39;49;00m[31mtrim[39;49;00m)[37m[39;49;00m$
  3551^I[37m  [39;49;00m[33m"[39;49;00m[33mSplit STRING into substrings bounded by matches for SEPARATORS.[39;49;00m$
  3552^I[33m[39;49;00m$
  3553^I[33mThe beginning and end of STRING, and each match for SEPARATORS, are[39;49;00m$
  3554^I[33msplitting points.  The substrings matching SEPARATORS are removed, and[39;49;00m$
  3555^I[33mthe substrings between the splitting points are collected as a list,[39;49;00m$
  3556^I[33mwhich is returned.[39;49;00m$
  3557^I[33m[39;49;00m$
  3558^I[33mIf SEPARATORS is non-nil, it should be a regular expression matching text[39;49;00m$
  3559^I[33mwhich separates, but is not part of, the substrings.  If nil it defaults to[39;49;00m$
  3560^I[33m`split-string-default-separators'[39;49;00m[33m, normally [39;49;00m[33m\"[39;49;00m[33m[ [39;49;00m[33m\\[39;49;00m[33mf[39;49;00m[33m\\[39;49;00m[33mt[39;49;00m[33m\\[39;49;00m[33mn[39;49;00m[33m\\[39;49;00m[33mr[39;49;00m[33m\\[39;49;00m[33mv]+[39;49;00m[33m\"[39;49;00m[33m, and[39;49;00m$
  3561^I[33mOMIT-NULLS is forced to t.[39;49;00m$
  3562^I[33m[39;49;00m$
  3563^I[33mIf OMIT-NULLS is t, zero-length substrings are omitted from the list (so[39;49;00m$
  3564^I[33mthat for the default value of SEPARATORS leading and trailing whitespace[39;49;00m$
  3565^I[33mare effectively trimmed).  If nil, all zero-length substrings are retained,[39;49;00m$
  3566^I[33mwhich correctly parses CSV format, for example.[39;49;00m$
  3567^I[33m[39;49;00m$
  3568^I[33mIf TRIM is non-nil, it should be a regular expression to match[39;49;00m$
  3569^I[33mtext to trim from the beginning and end of each substring.  If trimming[39;49;00m$
  3570^I[33mmakes the substring empty, it is treated as null.[39;49;00m$
  3571^I[33m[39;49;00m$
  3572^I[33mIf you want to trim whitespace from the substrings, the reliably correct[39;49;00m$
  3573^I[33mway is using TRIM.  Making SEPARATORS match that whitespace gives incorrect[39;49;00m$
  3574^I[33mresults when there is whitespace at the start or end of STRING.  If you[39;49;00m$
  3575^I[33msee such calls to [39;49;00m[33m`split-string'[39;49;00m[33m, please fix them.[39;49;00m$
  3576^I[33m[39;49;00m$
  3577^I[33mNote that the effect of [39;49;00m[33m`[39;49;00m[33m(split-string STRING)' is the same as[39;49;00m$
  3578^I[33m`[39;49;00m[33m(split-string STRING split-string-default-separators t)'.  In the rare[39;49;00m$
  3579^I[33mcase that you wish to retain zero-length substrings when splitting on[39;49;00m$
  3580^I[33mwhitespace, use [39;49;00m[33m`[39;49;00m[33m(split-string STRING split-string-default-separators)'.[39;49;00m$
  3581^I[33m[39;49;00m$
  3582^I[33mModifies the match data; use [39;49;00m[33m`save-match-data'[39;49;00m[33m if necessary.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3583^I[37m  [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mkeep-nulls[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mseparators[39;49;00m[37m [39;49;00m[31momit-nulls[39;49;00m[37m [39;49;00m[31mt[39;49;00m)))[37m[39;49;00m$
  3584^I[37m^I [39;49;00m([31mrexp[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mseparators[39;49;00m[37m [39;49;00m[31msplit-string-default-separators[39;49;00m))[37m[39;49;00m$
  3585^I[37m^I [39;49;00m([31mstart[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  3586^I[37m^I [39;49;00m[31mthis-start[39;49;00m[37m [39;49;00m[31mthis-end[39;49;00m[37m[39;49;00m$
  3587^I[37m^I [39;49;00m[31mnotfirst[39;49;00m[37m[39;49;00m$
  3588^I[37m^I [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
  3589^I[37m^I [39;49;00m([31mpush-one[39;49;00m[37m[39;49;00m$
  3590^I[37m^I  [39;49;00m[37m;; Push the substring in range THIS-START to THIS-END[39;49;00m[37m[39;49;00m$
  3591^I[37m^I  [39;49;00m[37m;; onto LIST, trimming it and perhaps discarding it.[39;49;00m[37m[39;49;00m$
  3592^I[37m^I  [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m()[37m[39;49;00m$
  3593^I[37m^I    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31mtrim[39;49;00m[37m[39;49;00m$
  3594^I[37m^I      [39;49;00m[37m;; Discard the trim from start of this substring.[39;49;00m[37m[39;49;00m$
  3595^I[37m^I      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtem[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[31mtrim[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[31mthis-start[39;49;00m)))[37m[39;49;00m$
  3596^I[37m^I^I[39;49;00m([34mand[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mtem[39;49;00m[37m [39;49;00m[31mthis-start[39;49;00m)[37m[39;49;00m$
  3597^I[37m^I^I     [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mthis-start[39;49;00m[37m [39;49;00m([32mmatch-end[39;49;00m[37m [39;49;00m[34m0[39;49;00m)))))[37m[39;49;00m$
  3598^I[37m[39;49;00m$
  3599^I[37m^I    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mkeep-nulls[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m[31mthis-start[39;49;00m[37m [39;49;00m[31mthis-end[39;49;00m))[37m[39;49;00m$
  3600^I[37m^I      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mthis[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[31mthis-start[39;49;00m[37m [39;49;00m[31mthis-end[39;49;00m)))[37m[39;49;00m$
  3601^I[37m[39;49;00m$
  3602^I[37m^I^I[39;49;00m[37m;; Discard the trim from end of this substring.[39;49;00m[37m[39;49;00m$
  3603^I[37m^I^I[39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31mtrim[39;49;00m[37m[39;49;00m$
  3604^I[37m^I^I  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtem[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[31mtrim[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m[33m"[39;49;00m)[37m [39;49;00m[31mthis[39;49;00m[37m [39;49;00m[34m0[39;49;00m)))[37m[39;49;00m$
  3605^I[37m^I^I    [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mtem[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m[31mtem[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31mthis[39;49;00m))[37m[39;49;00m$
  3606^I[37m^I^I^I [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mthis[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[31mthis[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[31mtem[39;49;00m)))))[37m[39;49;00m$
  3607^I[37m[39;49;00m$
  3608^I[37m^I^I[39;49;00m[37m;; Trimming could make it empty; check again.[39;49;00m[37m[39;49;00m$
  3609^I[37m^I^I[39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mkeep-nulls[39;49;00m[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31mthis[39;49;00m)[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m$
  3610^I[37m^I^I  [39;49;00m([36mpush[39;49;00m[37m [39;49;00m[31mthis[39;49;00m[37m [39;49;00m[32mlist[39;49;00m)))))))[37m[39;49;00m$
  3611^I[37m[39;49;00m$
  3612^I[37m    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[31mrexp[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m[39;49;00m$
  3613^I[37m^I^I^I      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mnotfirst[39;49;00m[37m[39;49;00m$
  3614^I[37m^I^I^I^I       [39;49;00m([32m=[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m([32mmatch-beginning[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m$
  3615^I[37m^I^I^I^I       [39;49;00m([32m<[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[32mstring[39;49;00m)))[37m[39;49;00m$
  3616^I[37m^I^I^I^I  [39;49;00m([32m1+[39;49;00m[37m [39;49;00m[31mstart[39;49;00m)[37m [39;49;00m[31mstart[39;49;00m))[37m[39;49;00m$
  3617^I[37m^I^I[39;49;00m([32m<[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[32mstring[39;49;00m)))[37m[39;49;00m$
  3618^I[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mnotfirst[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
  3619^I[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mthis-start[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mthis-end[39;49;00m[37m [39;49;00m([32mmatch-beginning[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  3620^I[37m^I    [39;49;00m[31mstart[39;49;00m[37m [39;49;00m([32mmatch-end[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m$
  3621^I[37m[39;49;00m$
  3622^I[37m      [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mpush-one[39;49;00m))[37m[39;49;00m$
  3623^I[37m[39;49;00m$
  3624^I[37m    [39;49;00m[37m;; Handle the substring at the end of STRING.[39;49;00m[37m[39;49;00m$
  3625^I[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mthis-start[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mthis-end[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[32mstring[39;49;00m))[37m[39;49;00m$
  3626^I[37m    [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mpush-one[39;49;00m)[37m[39;49;00m$
  3627^I[37m[39;49;00m$
  3628^I[37m    [39;49;00m([32mnreverse[39;49;00m[37m [39;49;00m[32mlist[39;49;00m)))[37m[39;49;00m$
  3629^I[37m[39;49;00m$
  3630^I([36mdefun[39;49;00m[37m [39;49;00m[31mcombine-and-quote-strings[39;49;00m[37m [39;49;00m([31mstrings[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mseparator[39;49;00m)[37m[39;49;00m$
  3631^I[37m  [39;49;00m[33m"[39;49;00m[33mConcatenate the STRINGS, adding the SEPARATOR (default [39;49;00m[33m\"[39;49;00m[33m [39;49;00m[33m\"[39;49;00m[33m).[39;49;00m$
  3632^I[33mThis tries to quote the strings to avoid ambiguity such that[39;49;00m$
  3633^I[33m  (split-string-and-unquote (combine-and-quote-strings strs)) == strs[39;49;00m$
  3634^I[33mOnly some SEPARATORs will work properly.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3635^I[37m  [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31msep[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mseparator[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
  3636^I[37m         [39;49;00m([31mre[39;49;00m[37m [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m[[39;49;00m[33m\\[39;49;00m[33m\"[39;49;00m[33m][39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m|[39;49;00m[33m"[39;49;00m[37m [39;49;00m([32mregexp-quote[39;49;00m[37m [39;49;00m[31msep[39;49;00m))))[37m[39;49;00m$
  3637^I[37m    [39;49;00m([32mmapconcat[39;49;00m[37m[39;49;00m$
  3638^I[37m     [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31mstr[39;49;00m)[37m[39;49;00m$
  3639^I[37m       [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[31mre[39;49;00m[37m [39;49;00m[31mstr[39;49;00m)[37m[39;49;00m$
  3640^I[37m^I   [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m[37m [39;49;00m([31mreplace-regexp-in-string[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m[[39;49;00m[33m\\[39;49;00m[33m\"[39;49;00m[33m][39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m&[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mstr[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  3641^I[37m^I [39;49;00m[31mstr[39;49;00m))[37m[39;49;00m$
  3642^I[37m     [39;49;00m[31mstrings[39;49;00m[37m [39;49;00m[31msep[39;49;00m)))[37m[39;49;00m$
  3643^I[37m[39;49;00m$
  3644^I([36mdefun[39;49;00m[37m [39;49;00m[31msplit-string-and-unquote[39;49;00m[37m [39;49;00m([32mstring[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mseparator[39;49;00m)[37m[39;49;00m$
  3645^I[37m  [39;49;00m[33m"[39;49;00m[33mSplit the STRING into a list of strings.[39;49;00m$
  3646^I[33mIt understands Emacs Lisp quoting within STRING, such that[39;49;00m$
  3647^I[33m  (split-string-and-unquote (combine-and-quote-strings strs)) == strs[39;49;00m$
  3648^I[33mThe SEPARATOR regexp defaults to [39;49;00m[33m\"[39;49;00m[33m\\[39;49;00m[33ms-+[39;49;00m[33m\"[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3649^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31msep[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mseparator[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33ms-+[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
  3650^I[37m^I[39;49;00m([31mi[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m[37m [39;49;00m[32mstring[39;49;00m)))[37m[39;49;00m$
  3651^I[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[31mi[39;49;00m)[37m[39;49;00m$
  3652^I[37m^I[39;49;00m([31msplit-string[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[31msep[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m^I[39;49;00m[37m; no quoting:  easy[39;49;00m[37m[39;49;00m$
  3653^I[37m      [39;49;00m([32mappend[39;49;00m[37m [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mi[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m([31msplit-string[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[31mi[39;49;00m)[37m [39;49;00m[31msep[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
  3654^I[37m^I      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mrfs[39;49;00m[37m [39;49;00m([32mread-from-string[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[31mi[39;49;00m)))[37m[39;49;00m$
  3655^I[37m^I^I[39;49;00m([32mcons[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mrfs[39;49;00m)[37m[39;49;00m$
  3656^I[37m^I^I      [39;49;00m([31msplit-string-and-unquote[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mrfs[39;49;00m))[37m[39;49;00m$
  3657^I[37m^I^I^I^I^I^I[39;49;00m[31msep[39;49;00m)))))))[37m[39;49;00m$
  3658^I[37m[39;49;00m$
  3659^I[37m[39;49;00m[37m[39;49;00m$
  3660^I[37m;;;; Replacement in strings.[39;49;00m[37m[39;49;00m$
  3661^I[37m[39;49;00m$
  3662^I([36mdefun[39;49;00m[37m [39;49;00m[31msubst-char-in-string[39;49;00m[37m [39;49;00m([31mfromchar[39;49;00m[37m [39;49;00m[31mtochar[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31minplace[39;49;00m)[37m[39;49;00m$
  3663^I[37m  [39;49;00m[33m"[39;49;00m[33mReplace FROMCHAR with TOCHAR in STRING each time it occurs.[39;49;00m$
  3664^I[33mUnless optional argument INPLACE is non-nil, return a new string.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3665^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mi[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[32mstring[39;49;00m))[37m[39;49;00m$
  3666^I[37m^I[39;49;00m([31mnewstr[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31minplace[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m([32mcopy-sequence[39;49;00m[37m [39;49;00m[32mstring[39;49;00m))))[37m[39;49;00m$
  3667^I[37m    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m[31mi[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  3668^I[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mi[39;49;00m[37m [39;49;00m([32m1-[39;49;00m[37m [39;49;00m[31mi[39;49;00m))[37m[39;49;00m$
  3669^I[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32maref[39;49;00m[37m [39;49;00m[31mnewstr[39;49;00m[37m [39;49;00m[31mi[39;49;00m)[37m [39;49;00m[31mfromchar[39;49;00m)[37m[39;49;00m$
  3670^I[37m^I  [39;49;00m([32maset[39;49;00m[37m [39;49;00m[31mnewstr[39;49;00m[37m [39;49;00m[31mi[39;49;00m[37m [39;49;00m[31mtochar[39;49;00m)))[37m[39;49;00m$
  3671^I[37m    [39;49;00m[31mnewstr[39;49;00m))[37m[39;49;00m$
  3672^I[37m[39;49;00m$
  3673^I([36mdefun[39;49;00m[37m [39;49;00m[31mreplace-regexp-in-string[39;49;00m[37m [39;49;00m([31mregexp[39;49;00m[37m [39;49;00m[31mrep[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m[39;49;00m$
  3674^I[37m^I^I^I^I^I[39;49;00m[31mfixedcase[39;49;00m[37m [39;49;00m[31mliteral[39;49;00m[37m [39;49;00m[31msubexp[39;49;00m[37m [39;49;00m[31mstart[39;49;00m)[37m[39;49;00m$
  3675^I[37m  [39;49;00m[33m"[39;49;00m[33mReplace all matches for REGEXP with REP in STRING.[39;49;00m$
  3676^I[33m[39;49;00m$
  3677^I[33mReturn a new string containing the replacements.[39;49;00m$
  3678^I[33m[39;49;00m$
  3679^I[33mOptional arguments FIXEDCASE, LITERAL and SUBEXP are like the[39;49;00m$
  3680^I[33marguments with the same names of function [39;49;00m[33m`replace-match'[39;49;00m[33m.  If START[39;49;00m$
  3681^I[33mis non-nil, start replacements at that index in STRING.[39;49;00m$
  3682^I[33m[39;49;00m$
  3683^I[33mREP is either a string used as the NEWTEXT arg of [39;49;00m[33m`replace-match'[39;49;00m[33m or a[39;49;00m$
  3684^I[33mfunction.  If it is a function, it is called with the actual text of each[39;49;00m$
  3685^I[33mmatch, and its value is used as the replacement text.  When REP is called,[39;49;00m$
  3686^I[33mthe match data are the result of matching REGEXP against a substring[39;49;00m$
  3687^I[33mof STRING.[39;49;00m$
  3688^I[33m[39;49;00m$
  3689^I[33mTo replace only the first match (if any), make REGEXP match up to [39;49;00m[33m\\[39;49;00m[33m'[39;49;00m$
  3690^I[33mand replace a sub-expression, e.g.[39;49;00m$
  3691^I[33m  (replace-regexp-in-string [39;49;00m[33m\"[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m(foo[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m).*[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m[33m\"[39;49;00m[33m [39;49;00m[33m\"[39;49;00m[33mbar[39;49;00m[33m\"[39;49;00m[33m [39;49;00m[33m\"[39;49;00m[33m foo foo[39;49;00m[33m\"[39;49;00m[33m nil nil 1)[39;49;00m$
  3692^I[33m    => [39;49;00m[33m\"[39;49;00m[33m bar foo[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3693^I[37m[39;49;00m$
  3694^I[37m  [39;49;00m[37m;; To avoid excessive consing from multiple matches in long strings,[39;49;00m[37m[39;49;00m$
  3695^I[37m  [39;49;00m[37m;; don't just call `replace-match' continually.  Walk down the[39;49;00m[37m[39;49;00m$
  3696^I[37m  [39;49;00m[37m;; string looking for matches of REGEXP and building up a (reversed)[39;49;00m[37m[39;49;00m$
  3697^I[37m  [39;49;00m[37m;; list MATCHES.  This comprises segments of STRING which weren't[39;49;00m[37m[39;49;00m$
  3698^I[37m  [39;49;00m[37m;; matched interspersed with replacements for segments that were.[39;49;00m[37m[39;49;00m$
  3699^I[37m  [39;49;00m[37m;; [For a `large' number of replacements it's more efficient to[39;49;00m[37m[39;49;00m$
  3700^I[37m  [39;49;00m[37m;; operate in a temporary buffer; we can't tell from the function's[39;49;00m[37m[39;49;00m$
  3701^I[37m  [39;49;00m[37m;; args whether to choose the buffer-based implementation, though it[39;49;00m[37m[39;49;00m$
  3702^I[37m  [39;49;00m[37m;; might be reasonable to do so for long enough STRING.][39;49;00m[37m[39;49;00m$
  3703^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31ml[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[32mstring[39;49;00m))[37m[39;49;00m$
  3704^I[37m^I[39;49;00m([31mstart[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m$
  3705^I[37m^I[39;49;00m[31mmatches[39;49;00m[37m [39;49;00m[31mstr[39;49;00m[37m [39;49;00m[31mmb[39;49;00m[37m [39;49;00m[31mme[39;49;00m)[37m[39;49;00m$
  3706^I[37m    [39;49;00m([36msave-match-data[39;49;00m[37m[39;49;00m$
  3707^I[37m      [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31ml[39;49;00m)[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[31mregexp[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[31mstart[39;49;00m))[37m[39;49;00m$
  3708^I[37m^I[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mmb[39;49;00m[37m [39;49;00m([32mmatch-beginning[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  3709^I[37m^I      [39;49;00m[31mme[39;49;00m[37m [39;49;00m([32mmatch-end[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m$
  3710^I[37m^I[39;49;00m[37m;; If we matched the empty string, make sure we advance by one char[39;49;00m[37m[39;49;00m$
  3711^I[37m^I[39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32m=[39;49;00m[37m [39;49;00m[31mme[39;49;00m[37m [39;49;00m[31mmb[39;49;00m)[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mme[39;49;00m[37m [39;49;00m([32mmin[39;49;00m[37m [39;49;00m[31ml[39;49;00m[37m [39;49;00m([32m1+[39;49;00m[37m [39;49;00m[31mmb[39;49;00m))))[37m[39;49;00m$
  3712^I[37m^I[39;49;00m[37m;; Generate a replacement for the matched substring.[39;49;00m[37m[39;49;00m$
  3713^I[37m^I[39;49;00m[37m;; Operate only on the substring to minimize string consing.[39;49;00m[37m[39;49;00m$
  3714^I[37m^I[39;49;00m[37m;; Set up match data for the substring for replacement;[39;49;00m[37m[39;49;00m$
  3715^I[37m^I[39;49;00m[37m;; presumably this is likely to be faster than munging the[39;49;00m[37m[39;49;00m$
  3716^I[37m^I[39;49;00m[37m;; match data directly in Lisp.[39;49;00m[37m[39;49;00m$
  3717^I[37m^I[39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[31mregexp[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mstr[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[31mmb[39;49;00m[37m [39;49;00m[31mme[39;49;00m)))[37m[39;49;00m$
  3718^I[37m^I[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mmatches[39;49;00m[37m[39;49;00m$
  3719^I[37m^I      [39;49;00m([32mcons[39;49;00m[37m [39;49;00m([32mreplace-match[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m[31mrep[39;49;00m)[37m[39;49;00m$
  3720^I[37m^I^I^I^I       [39;49;00m[31mrep[39;49;00m[37m[39;49;00m$
  3721^I[37m^I^I^I^I     [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mrep[39;49;00m[37m [39;49;00m([31mmatch-string[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[31mstr[39;49;00m)))[37m[39;49;00m$
  3722^I[37m^I^I^I^I   [39;49;00m[31mfixedcase[39;49;00m[37m [39;49;00m[31mliteral[39;49;00m[37m [39;49;00m[31mstr[39;49;00m[37m [39;49;00m[31msubexp[39;49;00m)[37m[39;49;00m$
  3723^I[37m^I^I    [39;49;00m([32mcons[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mmb[39;49;00m)[37m [39;49;00m[37m; unmatched prefix[39;49;00m[37m[39;49;00m$
  3724^I[37m^I^I^I  [39;49;00m[31mmatches[39;49;00m)))[37m[39;49;00m$
  3725^I[37m^I[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mme[39;49;00m))[37m[39;49;00m$
  3726^I[37m      [39;49;00m[37m;; Reconstruct a string from the pieces.[39;49;00m[37m[39;49;00m$
  3727^I[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mmatches[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31ml[39;49;00m)[37m [39;49;00m[31mmatches[39;49;00m))[37m [39;49;00m[37m; leftover[39;49;00m[37m[39;49;00m$
  3728^I[37m      [39;49;00m([32mapply[39;49;00m[37m [39;49;00m[32m#'[39;49;00m[32mconcat[39;49;00m[37m [39;49;00m([32mnreverse[39;49;00m[37m [39;49;00m[31mmatches[39;49;00m)))))[37m[39;49;00m$
  3729^I[37m[39;49;00m[37m[39;49;00m$
  3730^I([36mdefun[39;49;00m[37m [39;49;00m[31mstring-prefix-p[39;49;00m[37m [39;49;00m([31mprefix[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mignore-case[39;49;00m)[37m[39;49;00m$
  3731^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn non-nil if PREFIX is a prefix of STRING.[39;49;00m$
  3732^I[33mIf IGNORE-CASE is non-nil, the comparison is done without paying attention[39;49;00m$
  3733^I[33mto case differences.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3734^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mprefix-length[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31mprefix[39;49;00m)))[37m[39;49;00m$
  3735^I[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m[31mprefix-length[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[32mstring[39;49;00m))[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m$
  3736^I[37m      [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m([32mcompare-strings[39;49;00m[37m [39;49;00m[31mprefix[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[31mprefix-length[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m[39;49;00m$
  3737^I[37m^I^I^I     [39;49;00m[34m0[39;49;00m[37m [39;49;00m[31mprefix-length[39;49;00m[37m [39;49;00m[31mignore-case[39;49;00m)))))[37m[39;49;00m$
  3738^I[37m[39;49;00m$
  3739^I([36mdefun[39;49;00m[37m [39;49;00m[31mstring-suffix-p[39;49;00m[37m [39;49;00m([31msuffix[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m  [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mignore-case[39;49;00m)[37m[39;49;00m$
  3740^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn non-nil if SUFFIX is a suffix of STRING.[39;49;00m$
  3741^I[33mIf IGNORE-CASE is non-nil, the comparison is done without paying[39;49;00m$
  3742^I[33mattention to case differences.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3743^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mstart-pos[39;49;00m[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[32mstring[39;49;00m)[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31msuffix[39;49;00m))))[37m[39;49;00m$
  3744^I[37m    [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32m>=[39;49;00m[37m [39;49;00m[31mstart-pos[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  3745^I[37m         [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m([32mcompare-strings[39;49;00m[37m [39;49;00m[31msuffix[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m$
  3746^I[37m                                [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[31mstart-pos[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mignore-case[39;49;00m)))))[37m[39;49;00m$
  3747^I[37m[39;49;00m$
  3748^I([36mdefun[39;49;00m[37m [39;49;00m[31mbidi-string-mark-left-to-right[39;49;00m[37m [39;49;00m([31mstr[39;49;00m)[37m[39;49;00m$
  3749^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn a string that can be safely inserted in left-to-right text.[39;49;00m$
  3750^I[33m[39;49;00m$
  3751^I[33mNormally, inserting a string with right-to-left (RTL) script into[39;49;00m$
  3752^I[33ma buffer may cause some subsequent text to be displayed as part[39;49;00m$
  3753^I[33mof the RTL segment (usually this affects punctuation characters).[39;49;00m$
  3754^I[33mThis function returns a string which displays as STR but forces[39;49;00m$
  3755^I[33msubsequent text to be displayed as left-to-right.[39;49;00m$
  3756^I[33m[39;49;00m$
  3757^I[33mIf STR contains any RTL character, this function returns a string[39;49;00m$
  3758^I[33mconsisting of STR followed by an invisible left-to-right mark[39;49;00m$
  3759^I[33m\([39;49;00m[33mLRM) character.  Otherwise, it returns STR.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3760^I[37m  [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m[31mstr[39;49;00m)[37m[39;49;00m$
  3761^I[37m    [39;49;00m([32msignal[39;49;00m[37m [39;49;00m[33m'wrong-type-argument[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'stringp[39;49;00m[37m [39;49;00m[31mstr[39;49;00m)))[37m[39;49;00m$
  3762^I[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33mcR[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mstr[39;49;00m)[37m[39;49;00m$
  3763^I[37m      [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[31mstr[39;49;00m[37m [39;49;00m([32mpropertize[39;49;00m[37m [39;49;00m([32mstring[39;49;00m[37m [39;49;00m[33m?\x[39;49;00m[31m200e[39;49;00m)[37m [39;49;00m[33m'invisible[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
  3764^I[37m    [39;49;00m[31mstr[39;49;00m))[37m[39;49;00m$
  3765^I[37m[39;49;00m[37m[39;49;00m$
  3766^I[37m;;;; Specifying things to do later.[39;49;00m[37m[39;49;00m$
  3767^I[37m[39;49;00m$
  3768^I([36mdefun[39;49;00m[37m [39;49;00m[31mload-history-regexp[39;49;00m[37m [39;49;00m([31mfile[39;49;00m)[37m[39;49;00m$
  3769^I[37m  [39;49;00m[33m"[39;49;00m[33mForm a regexp to find FILE in [39;49;00m[33m`load-history'[39;49;00m[33m.[39;49;00m$
  3770^I[33mFILE, a string, is described in the function [39;49;00m[33m`eval-after-load'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3771^I[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mfile-name-absolute-p[39;49;00m[37m [39;49;00m[31mfile[39;49;00m)[37m[39;49;00m$
  3772^I[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mfile[39;49;00m[37m [39;49;00m([31mfile-truename[39;49;00m[37m [39;49;00m[31mfile[39;49;00m)))[37m[39;49;00m$
  3773^I[37m  [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mfile-name-absolute-p[39;49;00m[37m [39;49;00m[31mfile[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m`[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m([39;49;00m[33m\\[39;49;00m[33m`[39;49;00m[33m\\[39;49;00m[33m|/[39;49;00m[33m\\[39;49;00m[33m)[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  3774^I[37m^I  [39;49;00m([32mregexp-quote[39;49;00m[37m [39;49;00m[31mfile[39;49;00m)[37m[39;49;00m$
  3775^I[37m^I  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([31mfile-name-extension[39;49;00m[37m [39;49;00m[31mfile[39;49;00m)[37m[39;49;00m$
  3776^I[37m^I      [39;49;00m[33m"[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3777^I[37m^I    [39;49;00m[37m;; Note: regexp-opt can't be used here, since we need to call[39;49;00m[37m[39;49;00m$
  3778^I[37m^I    [39;49;00m[37m;; this before Emacs has been fully started.  2006-05-21[39;49;00m[37m[39;49;00m$
  3779^I[37m^I    [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m([39;49;00m[33m"[39;49;00m[37m [39;49;00m([32mmapconcat[39;49;00m[37m [39;49;00m[33m'regexp-quote[39;49;00m[37m [39;49;00m[31mload-suffixes[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m|[39;49;00m[33m"[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m)?[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
  3780^I[37m^I  [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m([39;49;00m[33m"[39;49;00m[37m [39;49;00m([32mmapconcat[39;49;00m[37m [39;49;00m[33m'regexp-quote[39;49;00m[37m [39;49;00m[31mjka-compr-load-suffixes[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m|[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  3781^I[37m^I  [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m)?[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
  3782^I[37m[39;49;00m$
  3783^I([36mdefun[39;49;00m[37m [39;49;00m[31mload-history-filename-element[39;49;00m[37m [39;49;00m([31mfile-regexp[39;49;00m)[37m[39;49;00m$
  3784^I[37m  [39;49;00m[33m"[39;49;00m[33mGet the first elt of [39;49;00m[33m`load-history'[39;49;00m[33m whose car matches FILE-REGEXP.[39;49;00m$
  3785^I[33mReturn nil if there isn't one.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3786^I[37m  [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mloads[39;49;00m[37m [39;49;00m[31mload-history[39;49;00m)[37m[39;49;00m$
  3787^I[37m^I [39;49;00m([31mload-elt[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mloads[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mloads[39;49;00m))))[37m[39;49;00m$
  3788^I[37m    [39;49;00m([36msave-match-data[39;49;00m[37m[39;49;00m$
  3789^I[37m      [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mloads[39;49;00m[37m[39;49;00m$
  3790^I[37m^I^I  [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mload-elt[39;49;00m))[37m[39;49;00m$
  3791^I[37m^I^I      [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[31mfile-regexp[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mload-elt[39;49;00m)))))[37m[39;49;00m$
  3792^I[37m^I[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mloads[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mloads[39;49;00m)[37m[39;49;00m$
  3793^I[37m^I      [39;49;00m[31mload-elt[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mloads[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mloads[39;49;00m)))))[37m[39;49;00m$
  3794^I[37m    [39;49;00m[31mload-elt[39;49;00m))[37m[39;49;00m$
  3795^I[37m[39;49;00m$
  3796^I([32mput[39;49;00m[37m [39;49;00m[33m'eval-after-load[39;49;00m[37m [39;49;00m[33m'lisp-indent-function[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m[39;49;00m$
  3797^I([36mdefun[39;49;00m[37m [39;49;00m[31meval-after-load[39;49;00m[37m [39;49;00m([31mfile[39;49;00m[37m [39;49;00m[31mform[39;49;00m)[37m[39;49;00m$
  3798^I[37m  [39;49;00m[33m"[39;49;00m[33mArrange that if FILE is loaded, FORM will be run immediately afterwards.[39;49;00m$
  3799^I[33mIf FILE is already loaded, evaluate FORM right now.[39;49;00m$
  3800^I[33mFORM can be an Elisp expression (in which case it's passed to [39;49;00m[33m`eval'[39;49;00m[33m),[39;49;00m$
  3801^I[33mor a function (in which case it's passed to [39;49;00m[33m`funcall'[39;49;00m[33m with no argument).[39;49;00m$
  3802^I[33m[39;49;00m$
  3803^I[33mIf a matching file is loaded again, FORM will be evaluated again.[39;49;00m$
  3804^I[33m[39;49;00m$
  3805^I[33mIf FILE is a string, it may be either an absolute or a relative file[39;49;00m$
  3806^I[33mname, and may have an extension (e.g. [39;49;00m[33m\"[39;49;00m[33m.el[39;49;00m[33m\"[39;49;00m[33m) or may lack one, and[39;49;00m$
  3807^I[33madditionally may or may not have an extension denoting a compressed[39;49;00m$
  3808^I[33mformat (e.g. [39;49;00m[33m\"[39;49;00m[33m.gz[39;49;00m[33m\"[39;49;00m[33m).[39;49;00m$
  3809^I[33m[39;49;00m$
  3810^I[33mWhen FILE is absolute, this first converts it to a true name by chasing[39;49;00m$
  3811^I[33msymbolic links.  Only a file of this name (see next paragraph regarding[39;49;00m$
  3812^I[33mextensions) will trigger the evaluation of FORM.  When FILE is relative,[39;49;00m$
  3813^I[33ma file whose absolute true name ends in FILE will trigger evaluation.[39;49;00m$
  3814^I[33m[39;49;00m$
  3815^I[33mWhen FILE lacks an extension, a file name with any extension will trigger[39;49;00m$
  3816^I[33mevaluation.  Otherwise, its extension must match FILE's.  A further[39;49;00m$
  3817^I[33mextension for a compressed format (e.g. [39;49;00m[33m\"[39;49;00m[33m.gz[39;49;00m[33m\"[39;49;00m[33m) on FILE will not affect[39;49;00m$
  3818^I[33mthis name matching.[39;49;00m$
  3819^I[33m[39;49;00m$
  3820^I[33mAlternatively, FILE can be a feature (i.e. a symbol), in which case FORM[39;49;00m$
  3821^I[33mis evaluated at the end of any file that [39;49;00m[33m`provide'[39;49;00m[33ms this feature.[39;49;00m$
  3822^I[33mIf the feature is provided when evaluating code not associated with a[39;49;00m$
  3823^I[33mfile, FORM is evaluated immediately after the provide statement.[39;49;00m$
  3824^I[33m[39;49;00m$
  3825^I[33mUsually FILE is just a library name like [39;49;00m[33m\"[39;49;00m[33mfont-lock[39;49;00m[33m\"[39;49;00m[33m or a feature name[39;49;00m$
  3826^I[33mlike 'font-lock.[39;49;00m$
  3827^I[33m[39;49;00m$
  3828^I[33mThis function makes or adds to an entry on [39;49;00m[33m`after-load-alist'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3829^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mcompiler-macro[39;49;00m[37m[39;49;00m$
  3830^I[37m            [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31mwhole[39;49;00m)[37m[39;49;00m$
  3831^I[37m              [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[33m'quote[39;49;00m[37m [39;49;00m([32mcar-safe[39;49;00m[37m [39;49;00m[31mform[39;49;00m))[37m[39;49;00m$
  3832^I[37m                  [39;49;00m[37m;; Quote with lambda so the compiler can look inside.[39;49;00m[37m[39;49;00m$
  3833^I[37m                  [39;49;00m`([31meval-after-load[39;49;00m[37m [39;49;00m,[31mfile[39;49;00m[37m [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m()[37m [39;49;00m,([32mnth[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mform[39;49;00m)))[37m[39;49;00m$
  3834^I[37m                [39;49;00m[31mwhole[39;49;00m))))[37m[39;49;00m$
  3835^I[37m  [39;49;00m[37m;; Add this FORM into after-load-alist (regardless of whether we'll be[39;49;00m[37m[39;49;00m$
  3836^I[37m  [39;49;00m[37m;; evaluating it now).[39;49;00m[37m[39;49;00m$
  3837^I[37m  [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mregexp-or-feature[39;49;00m[37m[39;49;00m$
  3838^I[37m^I  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m[31mfile[39;49;00m)[37m[39;49;00m$
  3839^I[37m              [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mfile[39;49;00m[37m [39;49;00m([32mpurecopy[39;49;00m[37m [39;49;00m([31mload-history-regexp[39;49;00m[37m [39;49;00m[31mfile[39;49;00m)))[37m[39;49;00m$
  3840^I[37m            [39;49;00m[31mfile[39;49;00m))[37m[39;49;00m$
  3841^I[37m^I [39;49;00m([32melt[39;49;00m[37m [39;49;00m([32massoc[39;49;00m[37m [39;49;00m[31mregexp-or-feature[39;49;00m[37m [39;49;00m[31mafter-load-alist[39;49;00m))[37m[39;49;00m$
  3842^I[37m         [39;49;00m([31mfunc[39;49;00m[37m[39;49;00m$
  3843^I[37m          [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mfunctionp[39;49;00m[37m [39;49;00m[31mform[39;49;00m)[37m [39;49;00m[31mform[39;49;00m[37m[39;49;00m$
  3844^I[37m            [39;49;00m[37m;; Try to use the "current" lexical/dynamic mode for `form'.[39;49;00m[37m[39;49;00m$
  3845^I[37m            [39;49;00m([32meval[39;49;00m[37m [39;49;00m`([36mlambda[39;49;00m[37m [39;49;00m()[37m [39;49;00m,[31mform[39;49;00m)[37m [39;49;00m[31mlexical-binding[39;49;00m))))[37m[39;49;00m$
  3846^I[37m    [39;49;00m([36munless[39;49;00m[37m [39;49;00m[32melt[39;49;00m[37m[39;49;00m$
  3847^I[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[32melt[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[31mregexp-or-feature[39;49;00m))[37m[39;49;00m$
  3848^I[37m      [39;49;00m([36mpush[39;49;00m[37m [39;49;00m[32melt[39;49;00m[37m [39;49;00m[31mafter-load-alist[39;49;00m))[37m[39;49;00m$
  3849^I[37m    [39;49;00m[37m;; Is there an already loaded file whose name (or `provide' name)[39;49;00m[37m[39;49;00m$
  3850^I[37m    [39;49;00m[37m;; matches FILE?[39;49;00m[37m[39;49;00m$
  3851^I[37m    [39;49;00m([34mprog1[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m[31mfile[39;49;00m)[37m[39;49;00m$
  3852^I[37m^I^I   [39;49;00m([31mload-history-filename-element[39;49;00m[37m [39;49;00m[31mregexp-or-feature[39;49;00m)[37m[39;49;00m$
  3853^I[37m^I^I [39;49;00m([36mfeaturep[39;49;00m[37m [39;49;00m[31mfile[39;49;00m))[37m[39;49;00m$
  3854^I[37m^I       [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mfunc[39;49;00m))[37m[39;49;00m$
  3855^I[37m      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mdelayed-func[39;49;00m[37m[39;49;00m$
  3856^I[37m             [39;49;00m([34mif[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32msymbolp[39;49;00m[37m [39;49;00m[31mregexp-or-feature[39;49;00m))[37m [39;49;00m[31mfunc[39;49;00m[37m[39;49;00m$
  3857^I[37m               [39;49;00m[37m;; For features, the after-load-alist elements get run when[39;49;00m[37m[39;49;00m$
  3858^I[37m               [39;49;00m[37m;; `provide' is called rather than at the end of the file.[39;49;00m[37m[39;49;00m$
  3859^I[37m               [39;49;00m[37m;; So add an indirection to make sure that `func' is really run[39;49;00m[37m[39;49;00m$
  3860^I[37m               [39;49;00m[37m;; "after-load" in case the provide call happens early.[39;49;00m[37m[39;49;00m$
  3861^I[37m               [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m()[37m[39;49;00m$
  3862^I[37m                 [39;49;00m([34mif[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m[31mload-file-name[39;49;00m)[37m[39;49;00m$
  3863^I[37m                     [39;49;00m[37m;; Not being provided from a file, run func right now.[39;49;00m[37m[39;49;00m$
  3864^I[37m                     [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mfunc[39;49;00m)[37m[39;49;00m$
  3865^I[37m                   [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mlfn[39;49;00m[37m [39;49;00m[31mload-file-name[39;49;00m)[37m[39;49;00m$
  3866^I[37m                         [39;49;00m[37m;; Don't use letrec, because equal (in[39;49;00m[37m[39;49;00m$
  3867^I[37m                         [39;49;00m[37m;; add/remove-hook) would get trapped in a cycle.[39;49;00m[37m[39;49;00m$
  3868^I[37m                         [39;49;00m([31mfun[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33meval-after-load-helper[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
  3869^I[37m                     [39;49;00m([32mfset[39;49;00m[37m [39;49;00m[31mfun[39;49;00m[37m [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31mfile[39;49;00m)[37m[39;49;00m$
  3870^I[37m                                 [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mequal[39;49;00m[37m [39;49;00m[31mfile[39;49;00m[37m [39;49;00m[31mlfn[39;49;00m)[37m[39;49;00m$
  3871^I[37m                                   [39;49;00m([31mremove-hook[39;49;00m[37m [39;49;00m[33m'after-load-functions[39;49;00m[37m [39;49;00m[31mfun[39;49;00m)[37m[39;49;00m$
  3872^I[37m                                   [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mfunc[39;49;00m))))[37m[39;49;00m$
  3873^I[37m                     [39;49;00m([31madd-hook[39;49;00m[37m [39;49;00m[33m'after-load-functions[39;49;00m[37m [39;49;00m[31mfun[39;49;00m[37m [39;49;00m[33m'append[39;49;00m)))))))[37m[39;49;00m$
  3874^I[37m        [39;49;00m[37m;; Add FORM to the element unless it's already there.[39;49;00m[37m[39;49;00m$
  3875^I[37m        [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32mmember[39;49;00m[37m [39;49;00m[31mdelayed-func[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[32melt[39;49;00m))[37m[39;49;00m$
  3876^I[37m          [39;49;00m([32mnconc[39;49;00m[37m [39;49;00m[32melt[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[31mdelayed-func[39;49;00m)))))))[37m[39;49;00m$
  3877^I[37m[39;49;00m$
  3878^I([36mdefmacro[39;49;00m[37m [39;49;00m[36mwith-eval-after-load[39;49;00m[37m [39;49;00m([31mfile[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
  3879^I[37m  [39;49;00m[33m"[39;49;00m[33mExecute BODY after FILE is loaded.[39;49;00m$
  3880^I[33mFILE is normally a feature name, but it can also be a file name,[39;49;00m$
  3881^I[33min case that file does not provide any feature.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3882^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
  3883^I[37m  [39;49;00m`([31meval-after-load[39;49;00m[37m [39;49;00m,[31mfile[39;49;00m[37m [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m()[37m [39;49;00m,@[31mbody[39;49;00m)))[37m[39;49;00m$
  3884^I[37m[39;49;00m$
  3885^I([34mdefvar[39;49;00m[37m [39;49;00m[31mafter-load-functions[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m$
  3886^I[37m  [39;49;00m[33m"[39;49;00m[33mSpecial hook run after loading a file.[39;49;00m$
  3887^I[33mEach function there is called with a single argument, the absolute[39;49;00m$
  3888^I[33mname of the file just loaded.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  3889^I[37m[39;49;00m$
  3890^I([36mdefun[39;49;00m[37m [39;49;00m[31mdo-after-load-evaluation[39;49;00m[37m [39;49;00m([31mabs-file[39;49;00m)[37m[39;49;00m$
  3891^I[37m  [39;49;00m[33m"[39;49;00m[33mEvaluate all [39;49;00m[33m`eval-after-load'[39;49;00m[33m forms, if any, for ABS-FILE.[39;49;00m$
  3892^I[33mABS-FILE, a string, should be the absolute true name of a file just loaded.[39;49;00m$
  3893^I[33mThis function is called directly from the C code.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3894^I[37m  [39;49;00m[37m;; Run the relevant eval-after-load forms.[39;49;00m[37m[39;49;00m$
  3895^I[37m  [39;49;00m([36mdolist[39;49;00m[37m [39;49;00m([31ma-l-element[39;49;00m[37m [39;49;00m[31mafter-load-alist[39;49;00m)[37m[39;49;00m$
  3896^I[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31ma-l-element[39;49;00m))[37m[39;49;00m$
  3897^I[37m               [39;49;00m([31mstring-match-p[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31ma-l-element[39;49;00m)[37m [39;49;00m[31mabs-file[39;49;00m))[37m[39;49;00m$
  3898^I[37m      [39;49;00m[37m;; discard the file name regexp[39;49;00m[37m[39;49;00m$
  3899^I[37m      [39;49;00m([32mmapc[39;49;00m[37m [39;49;00m[32m#'[39;49;00m[32mfuncall[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31ma-l-element[39;49;00m))))[37m[39;49;00m$
  3900^I[37m  [39;49;00m[37m;; Complain when the user uses obsolete files.[39;49;00m[37m[39;49;00m$
  3901^I[37m  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([36msave-match-data[39;49;00m[37m[39;49;00m$
  3902^I[37m          [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m/obsolete/[39;49;00m[33m\\[39;49;00m[33m([^/]*[39;49;00m[33m\\[39;49;00m[33m)[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mabs-file[39;49;00m)[37m[39;49;00m$
  3903^I[37m               [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mequal[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mloaddefs.el[39;49;00m[33m"[39;49;00m[37m [39;49;00m([31mmatch-string[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mabs-file[39;49;00m)))))[37m[39;49;00m$
  3904^I[37m    [39;49;00m[37m;; Maybe we should just use display-warning?  This seems yucky...[39;49;00m[37m[39;49;00m$
  3905^I[37m    [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mfile[39;49;00m[37m [39;49;00m([32mfile-name-nondirectory[39;49;00m[37m [39;49;00m[31mabs-file[39;49;00m))[37m[39;49;00m$
  3906^I[37m^I   [39;49;00m([31mmsg[39;49;00m[37m [39;49;00m([32mformat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mPackage %s is obsolete![39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3907^I[37m^I^I^I[39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[31mfile[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m[39;49;00m$
  3908^I[37m^I^I^I^I   [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m.elc?[39;49;00m[33m\\[39;49;00m[33m>[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mfile[39;49;00m)))))[37m[39;49;00m$
  3909^I[37m      [39;49;00m[37m;; Cribbed from cl--compiling-file.[39;49;00m[37m[39;49;00m$
  3910^I[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mboundp[39;49;00m[37m [39;49;00m[33m'byte-compile--outbuffer[39;49;00m)[37m[39;49;00m$
  3911^I[37m^I       [39;49;00m([32mbufferp[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[33m'byte-compile--outbuffer[39;49;00m))[37m[39;49;00m$
  3912^I[37m^I       [39;49;00m([32mequal[39;49;00m[37m [39;49;00m([32mbuffer-name[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[33m'byte-compile--outbuffer[39;49;00m))[37m[39;49;00m$
  3913^I[37m^I^I      [39;49;00m[33m"[39;49;00m[33m *Compiler Output*[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
  3914^I[37m^I  [39;49;00m[37m;; Don't warn about obsolete files using other obsolete files.[39;49;00m[37m[39;49;00m$
  3915^I[37m^I  [39;49;00m([36munless[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m[31mbyte-compile-current-file[39;49;00m)[37m[39;49;00m$
  3916^I[37m^I^I       [39;49;00m([31mstring-match-p[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m/obsolete/[^/]*[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3917^I[37m^I^I^I^I       [39;49;00m([32mexpand-file-name[39;49;00m[37m[39;49;00m$
  3918^I[37m^I^I^I^I^I[39;49;00m[31mbyte-compile-current-file[39;49;00m[37m[39;49;00m$
  3919^I[37m^I^I^I^I^I[39;49;00m[31mbyte-compile-root-dir[39;49;00m)))[37m[39;49;00m$
  3920^I[37m^I    [39;49;00m([31mbyte-compile-log-warning[39;49;00m[37m [39;49;00m[31mmsg[39;49;00m))[37m[39;49;00m$
  3921^I[37m^I[39;49;00m([31mrun-with-timer[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m$
  3922^I[37m^I^I^I[39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31mmsg[39;49;00m)[37m[39;49;00m$
  3923^I[37m^I^I^I  [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m%s[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mmsg[39;49;00m))[37m[39;49;00m$
  3924^I[37m                        [39;49;00m[31mmsg[39;49;00m))))[37m[39;49;00m$
  3925^I[37m[39;49;00m$
  3926^I[37m  [39;49;00m[37m;; Finally, run any other hook.[39;49;00m[37m[39;49;00m$
  3927^I[37m  [39;49;00m([32mrun-hook-with-args[39;49;00m[37m [39;49;00m[33m'after-load-functions[39;49;00m[37m [39;49;00m[31mabs-file[39;49;00m))[37m[39;49;00m$
  3928^I[37m[39;49;00m$
  3929^I([36mdefun[39;49;00m[37m [39;49;00m[31meval-next-after-load[39;49;00m[37m [39;49;00m([31mfile[39;49;00m)[37m[39;49;00m$
  3930^I[37m  [39;49;00m[33m"[39;49;00m[33mRead the following input sexp, and run it whenever FILE is loaded.[39;49;00m$
  3931^I[33mThis makes or adds to an entry on [39;49;00m[33m`after-load-alist'[39;49;00m[33m.[39;49;00m$
  3932^I[33mFILE should be the name of a library, with no directory name.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3933^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mobsolete[39;49;00m[37m [39;49;00m[31meval-after-load[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
  3934^I[37m  [39;49;00m([31meval-after-load[39;49;00m[37m [39;49;00m[31mfile[39;49;00m[37m [39;49;00m([32mread[39;49;00m)))[37m[39;49;00m$
  3935^I[37m[39;49;00m$
  3936^I[37m[39;49;00m[37m[39;49;00m$
  3937^I([36mdefun[39;49;00m[37m [39;49;00m[31mdisplay-delayed-warnings[39;49;00m[37m [39;49;00m()[37m[39;49;00m$
  3938^I[37m  [39;49;00m[33m"[39;49;00m[33mDisplay delayed warnings from [39;49;00m[33m`delayed-warnings-list'[39;49;00m[33m.[39;49;00m$
  3939^I[33mUsed from [39;49;00m[33m`delayed-warnings-hook'[39;49;00m[33m (which see).[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3940^I[37m  [39;49;00m([36mdolist[39;49;00m[37m [39;49;00m([31mwarning[39;49;00m[37m [39;49;00m([32mnreverse[39;49;00m[37m [39;49;00m[31mdelayed-warnings-list[39;49;00m))[37m[39;49;00m$
  3941^I[37m    [39;49;00m([32mapply[39;49;00m[37m [39;49;00m[33m'display-warning[39;49;00m[37m [39;49;00m[31mwarning[39;49;00m))[37m[39;49;00m$
  3942^I[37m  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mdelayed-warnings-list[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m$
  3943^I[37m[39;49;00m$
  3944^I([36mdefun[39;49;00m[37m [39;49;00m[31mcollapse-delayed-warnings[39;49;00m[37m [39;49;00m()[37m[39;49;00m$
  3945^I[37m  [39;49;00m[33m"[39;49;00m[33mRemove duplicates from [39;49;00m[33m`delayed-warnings-list'[39;49;00m[33m.[39;49;00m$
  3946^I[33mCollapse identical adjacent warnings into one (plus count).[39;49;00m$
  3947^I[33mUsed from [39;49;00m[33m`delayed-warnings-hook'[39;49;00m[33m (which see).[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3948^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mcount[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m[39;49;00m$
  3949^I[37m        [39;49;00m[31mcollapsed[39;49;00m[37m [39;49;00m[31mwarning[39;49;00m)[37m[39;49;00m$
  3950^I[37m    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m[31mdelayed-warnings-list[39;49;00m[37m[39;49;00m$
  3951^I[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mwarning[39;49;00m[37m [39;49;00m([36mpop[39;49;00m[37m [39;49;00m[31mdelayed-warnings-list[39;49;00m))[37m[39;49;00m$
  3952^I[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mequal[39;49;00m[37m [39;49;00m[31mwarning[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mdelayed-warnings-list[39;49;00m))[37m[39;49;00m$
  3953^I[37m          [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mcount[39;49;00m[37m [39;49;00m([32m1+[39;49;00m[37m [39;49;00m[31mcount[39;49;00m))[37m[39;49;00m$
  3954^I[37m        [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m[31mcount[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m[39;49;00m$
  3955^I[37m          [39;49;00m([32msetcdr[39;49;00m[37m [39;49;00m[31mwarning[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m([32mformat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m%s [%d times][39;49;00m[33m"[39;49;00m[37m [39;49;00m([31mcadr[39;49;00m[37m [39;49;00m[31mwarning[39;49;00m)[37m [39;49;00m[31mcount[39;49;00m)[37m[39;49;00m$
  3956^I[37m                                [39;49;00m([31mcddr[39;49;00m[37m [39;49;00m[31mwarning[39;49;00m)))[37m[39;49;00m$
  3957^I[37m          [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mcount[39;49;00m[37m [39;49;00m[34m1[39;49;00m))[37m[39;49;00m$
  3958^I[37m        [39;49;00m([36mpush[39;49;00m[37m [39;49;00m[31mwarning[39;49;00m[37m [39;49;00m[31mcollapsed[39;49;00m)))[37m[39;49;00m$
  3959^I[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mdelayed-warnings-list[39;49;00m[37m [39;49;00m([32mnreverse[39;49;00m[37m [39;49;00m[31mcollapsed[39;49;00m))))[37m[39;49;00m$
  3960^I[37m[39;49;00m$
  3961^I[37m;; At present this is only used for Emacs internals.[39;49;00m[37m[39;49;00m$
  3962^I[37m;; Ref http://lists.gnu.org/archive/html/emacs-devel/2012-02/msg00085.html[39;49;00m[37m[39;49;00m$
  3963^I([34mdefvar[39;49;00m[37m [39;49;00m[31mdelayed-warnings-hook[39;49;00m[37m [39;49;00m'([31mcollapse-delayed-warnings[39;49;00m[37m[39;49;00m$
  3964^I[37m                                [39;49;00m[31mdisplay-delayed-warnings[39;49;00m)[37m[39;49;00m$
  3965^I[37m  [39;49;00m[33m"[39;49;00m[33mNormal hook run to process and display delayed warnings.[39;49;00m$
  3966^I[33mBy default, this hook contains functions to consolidate the[39;49;00m$
  3967^I[33mwarnings listed in [39;49;00m[33m`delayed-warnings-list'[39;49;00m[33m, display them, and set[39;49;00m$
  3968^I[33m`delayed-warnings-list'[39;49;00m[33m back to nil.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  3969^I[37m[39;49;00m$
  3970^I([36mdefun[39;49;00m[37m [39;49;00m[31mdelay-warning[39;49;00m[37m [39;49;00m([31mtype[39;49;00m[37m [39;49;00m[32mmessage[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mlevel[39;49;00m[37m [39;49;00m[32mbuffer-name[39;49;00m)[37m[39;49;00m$
  3971^I[37m  [39;49;00m[33m"[39;49;00m[33mDisplay a delayed warning.[39;49;00m$
  3972^I[33mAside from going through [39;49;00m[33m`delayed-warnings-list'[39;49;00m[33m, this is equivalent[39;49;00m$
  3973^I[33mto [39;49;00m[33m`display-warning'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3974^I[37m  [39;49;00m([36mpush[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[31mtype[39;49;00m[37m [39;49;00m[32mmessage[39;49;00m[37m [39;49;00m[31mlevel[39;49;00m[37m [39;49;00m[32mbuffer-name[39;49;00m)[37m [39;49;00m[31mdelayed-warnings-list[39;49;00m))[37m[39;49;00m$
  3975^I[37m[39;49;00m$
  3976^I[37m[39;49;00m[37m[39;49;00m$
  3977^I[37m;;;; invisibility specs[39;49;00m[37m[39;49;00m$
  3978^I[37m[39;49;00m$
  3979^I([36mdefun[39;49;00m[37m [39;49;00m[31madd-to-invisibility-spec[39;49;00m[37m [39;49;00m([31melement[39;49;00m)[37m[39;49;00m$
  3980^I[37m  [39;49;00m[33m"[39;49;00m[33mAdd ELEMENT to [39;49;00m[33m`buffer-invisibility-spec'[39;49;00m[33m.[39;49;00m$
  3981^I[33mSee documentation for [39;49;00m[33m`buffer-invisibility-spec'[39;49;00m[33m for the kind of elements[39;49;00m$
  3982^I[33mthat can be added.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3983^I[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mbuffer-invisibility-spec[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
  3984^I[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbuffer-invisibility-spec[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[31mt[39;49;00m)))[37m[39;49;00m$
  3985^I[37m  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbuffer-invisibility-spec[39;49;00m[37m[39;49;00m$
  3986^I[37m^I[39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31melement[39;49;00m[37m [39;49;00m[31mbuffer-invisibility-spec[39;49;00m)))[37m[39;49;00m$
  3987^I[37m[39;49;00m$
  3988^I([36mdefun[39;49;00m[37m [39;49;00m[31mremove-from-invisibility-spec[39;49;00m[37m [39;49;00m([31melement[39;49;00m)[37m[39;49;00m$
  3989^I[37m  [39;49;00m[33m"[39;49;00m[33mRemove ELEMENT from [39;49;00m[33m`buffer-invisibility-spec'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  3990^I[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mbuffer-invisibility-spec[39;49;00m)[37m[39;49;00m$
  3991^I[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbuffer-invisibility-spec[39;49;00m[37m[39;49;00m$
  3992^I[37m^I    [39;49;00m([32mdelete[39;49;00m[37m [39;49;00m[31melement[39;49;00m[37m [39;49;00m[31mbuffer-invisibility-spec[39;49;00m))))[37m[39;49;00m$
  3993^I[37m[39;49;00m[37m[39;49;00m$
  3994^I[37m;;;; Syntax tables.[39;49;00m[37m[39;49;00m$
  3995^I[37m[39;49;00m$
  3996^I([36mdefmacro[39;49;00m[37m [39;49;00m[36mwith-syntax-table[39;49;00m[37m [39;49;00m([31mtable[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
  3997^I[37m  [39;49;00m[33m"[39;49;00m[33mEvaluate BODY with syntax table of current buffer set to TABLE.[39;49;00m$
  3998^I[33mThe syntax table of the current buffer is saved, BODY is evaluated, and the[39;49;00m$
  3999^I[33msaved table is restored, even in case of an abnormal exit.[39;49;00m$
  4000^I[33mValue is what BODY returns.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  4001^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m1[39;49;00m))[37m[39;49;00m$
  4002^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mold-table[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mtable[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
  4003^I[37m^I[39;49;00m([31mold-buffer[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mbuffer[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
  4004^I[37m    [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m((,[31mold-table[39;49;00m[37m [39;49;00m([32msyntax-table[39;49;00m))[37m[39;49;00m$
  4005^I[37m^I   [39;49;00m(,[31mold-buffer[39;49;00m[37m [39;49;00m([32mcurrent-buffer[39;49;00m)))[37m[39;49;00m$
  4006^I[37m       [39;49;00m([34munwind-protect[39;49;00m[37m[39;49;00m$
  4007^I[37m^I   [39;49;00m([34mprogn[39;49;00m[37m[39;49;00m$
  4008^I[37m^I     [39;49;00m([32mset-syntax-table[39;49;00m[37m [39;49;00m,[31mtable[39;49;00m)[37m[39;49;00m$
  4009^I[37m^I     [39;49;00m,@[31mbody[39;49;00m)[37m[39;49;00m$
  4010^I[37m^I [39;49;00m([34msave-current-buffer[39;49;00m[37m[39;49;00m$
  4011^I[37m^I   [39;49;00m([32mset-buffer[39;49;00m[37m [39;49;00m,[31mold-buffer[39;49;00m)[37m[39;49;00m$
  4012^I[37m^I   [39;49;00m([32mset-syntax-table[39;49;00m[37m [39;49;00m,[31mold-table[39;49;00m))))))[37m[39;49;00m$
  4013^I[37m[39;49;00m$
  4014^I([36mdefun[39;49;00m[37m [39;49;00m[31mmake-syntax-table[39;49;00m[37m [39;49;00m([34m&optional[39;49;00m[37m [39;49;00m[31moldtable[39;49;00m)[37m[39;49;00m$
  4015^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn a new syntax table.[39;49;00m$
  4016^I[33mCreate a syntax table which inherits from OLDTABLE (if non-nil) or[39;49;00m$
  4017^I[33mfrom [39;49;00m[33m`standard-syntax-table'[39;49;00m[33m otherwise.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  4018^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtable[39;49;00m[37m [39;49;00m([32mmake-char-table[39;49;00m[37m [39;49;00m[33m'syntax-table[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)))[37m[39;49;00m$
  4019^I[37m    [39;49;00m([32mset-char-table-parent[39;49;00m[37m [39;49;00m[31mtable[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31moldtable[39;49;00m[37m [39;49;00m([32mstandard-syntax-table[39;49;00m)))[37m[39;49;00m$
  4020^I[37m    [39;49;00m[31mtable[39;49;00m))[37m[39;49;00m$
  4021^I[37m[39;49;00m$
  4022^I([36mdefun[39;49;00m[37m [39;49;00m[31msyntax-after[39;49;00m[37m [39;49;00m([31mpos[39;49;00m)[37m[39;49;00m$
  4023^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn the raw syntax descriptor for the char after POS.[39;49;00m$
  4024^I[33mIf POS is outside the buffer's accessible portion, return nil.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  4025^I[37m  [39;49;00m([36munless[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m[31mpos[39;49;00m[37m [39;49;00m([32mpoint-min[39;49;00m))[37m [39;49;00m([32m>=[39;49;00m[37m [39;49;00m[31mpos[39;49;00m[37m [39;49;00m([32mpoint-max[39;49;00m)))[37m[39;49;00m$
  4026^I[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mst[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mparse-sexp-lookup-properties[39;49;00m[37m[39;49;00m$
  4027^I[37m^I^I  [39;49;00m([32mget-char-property[39;49;00m[37m [39;49;00m[31mpos[39;49;00m[37m [39;49;00m[33m'syntax-table[39;49;00m))))[37m[39;49;00m$
  4028^I[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mst[39;49;00m)[37m [39;49;00m[31mst[39;49;00m[37m[39;49;00m$
  4029^I[37m^I[39;49;00m([32maref[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mst[39;49;00m[37m [39;49;00m([32msyntax-table[39;49;00m))[37m [39;49;00m([32mchar-after[39;49;00m[37m [39;49;00m[31mpos[39;49;00m))))))[37m[39;49;00m$
  4030^I[37m[39;49;00m$
  4031^I([36mdefun[39;49;00m[37m [39;49;00m[31msyntax-class[39;49;00m[37m [39;49;00m([31msyntax[39;49;00m)[37m[39;49;00m$
  4032^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn the code for the syntax class described by SYNTAX.[39;49;00m$
  4033^I[33m[39;49;00m$
  4034^I[33mSYNTAX should be a raw syntax descriptor; the return value is a[39;49;00m$
  4035^I[33minteger which encodes the corresponding syntax class.  See Info[39;49;00m$
  4036^I[33mnode [39;49;00m[33m`[39;49;00m[33m(elisp)Syntax Table Internals' for a list of codes.[39;49;00m$
  4037^I[33m[39;49;00m$
  4038^I[33mIf SYNTAX is nil, return nil.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  4039^I[37m  [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31msyntax[39;49;00m[37m [39;49;00m([32mlogand[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31msyntax[39;49;00m)[37m [39;49;00m[34m65535[39;49;00m)))[37m[39;49;00m$
  4040^I[37m[39;49;00m[37m[39;49;00m$
  4041^I[37m;; Utility motion commands[39;49;00m[37m[39;49;00m$
  4042^I[37m[39;49;00m$
  4043^I[37m;;  Whitespace[39;49;00m[37m[39;49;00m$
  4044^I[37m[39;49;00m$
  4045^I([36mdefun[39;49;00m[37m [39;49;00m[31mforward-whitespace[39;49;00m[37m [39;49;00m([31marg[39;49;00m)[37m[39;49;00m$
  4046^I[37m  [39;49;00m[33m"[39;49;00m[33mMove point to the end of the next sequence of whitespace chars.[39;49;00m$
  4047^I[33mEach such sequence may be a single newline, or a sequence of[39;49;00m$
  4048^I[33mconsecutive space and/or tab characters.[39;49;00m$
  4049^I[33mWith prefix argument ARG, do it ARG times if positive, or move[39;49;00m$
  4050^I[33mbackwards ARG times if negative.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  4051^I[37m  [39;49;00m([34minteractive[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m^p[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  4052^I[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mnatnump[39;49;00m[37m [39;49;00m[31marg[39;49;00m)[37m[39;49;00m$
  4053^I[37m      [39;49;00m([32mre-search-forward[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m[ [39;49;00m[33m\t[39;49;00m[33m]+[39;49;00m[33m\\[39;49;00m[33m|[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[33m'move[39;49;00m[37m [39;49;00m[31marg[39;49;00m)[37m[39;49;00m$
  4054^I[37m    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m[31marg[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  4055^I[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mre-search-backward[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m[ [39;49;00m[33m\t[39;49;00m[33m]+[39;49;00m[33m\\[39;49;00m[33m|[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[33m'move[39;49;00m)[37m[39;49;00m$
  4056^I[37m^I  [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mchar-after[39;49;00m[37m [39;49;00m([32mmatch-beginning[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m [39;49;00m[33m?\n[39;49;00m)[37m[39;49;00m$
  4057^I[37m^I      [39;49;00m([32mskip-chars-backward[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m [39;49;00m[33m\t[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
  4058^I[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31marg[39;49;00m[37m [39;49;00m([32m1+[39;49;00m[37m [39;49;00m[31marg[39;49;00m)))))[37m[39;49;00m$
  4059^I[37m[39;49;00m$
  4060^I[37m;;  Symbols[39;49;00m[37m[39;49;00m$
  4061^I[37m[39;49;00m$
  4062^I([36mdefun[39;49;00m[37m [39;49;00m[31mforward-symbol[39;49;00m[37m [39;49;00m([31marg[39;49;00m)[37m[39;49;00m$
  4063^I[37m  [39;49;00m[33m"[39;49;00m[33mMove point to the next position that is the end of a symbol.[39;49;00m$
  4064^I[33mA symbol is any sequence of characters that are in either the[39;49;00m$
  4065^I[33mword constituent or symbol constituent syntax class.[39;49;00m$
  4066^I[33mWith prefix argument ARG, do it ARG times if positive, or move[39;49;00m$
  4067^I[33mbackwards ARG times if negative.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  4068^I[37m  [39;49;00m([34minteractive[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m^p[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  4069^I[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mnatnump[39;49;00m[37m [39;49;00m[31marg[39;49;00m)[37m[39;49;00m$
  4070^I[37m      [39;49;00m([32mre-search-forward[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m([39;49;00m[33m\\[39;49;00m[33msw[39;49;00m[33m\\[39;49;00m[33m|[39;49;00m[33m\\[39;49;00m[33ms_[39;49;00m[33m\\[39;49;00m[33m)+[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[33m'move[39;49;00m[37m [39;49;00m[31marg[39;49;00m)[37m[39;49;00m$
  4071^I[37m    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m[31marg[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  4072^I[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mre-search-backward[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m([39;49;00m[33m\\[39;49;00m[33msw[39;49;00m[33m\\[39;49;00m[33m|[39;49;00m[33m\\[39;49;00m[33ms_[39;49;00m[33m\\[39;49;00m[33m)+[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[33m'move[39;49;00m)[37m[39;49;00m$
  4073^I[37m^I  [39;49;00m([32mskip-syntax-backward[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mw_[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
  4074^I[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31marg[39;49;00m[37m [39;49;00m([32m1+[39;49;00m[37m [39;49;00m[31marg[39;49;00m)))))[37m[39;49;00m$
  4075^I[37m[39;49;00m$
  4076^I[37m;;  Syntax blocks[39;49;00m[37m[39;49;00m$
  4077^I[37m[39;49;00m$
  4078^I([36mdefun[39;49;00m[37m [39;49;00m[31mforward-same-syntax[39;49;00m[37m [39;49;00m([34m&optional[39;49;00m[37m [39;49;00m[31marg[39;49;00m)[37m[39;49;00m$
  4079^I[37m  [39;49;00m[33m"[39;49;00m[33mMove point past all characters with the same syntax class.[39;49;00m$
  4080^I[33mWith prefix argument ARG, do it ARG times if positive, or move[39;49;00m$
  4081^I[33mbackwards ARG times if negative.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  4082^I[37m  [39;49;00m([34minteractive[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m^p[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  4083^I[37m  [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31marg[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31marg[39;49;00m[37m [39;49;00m[34m1[39;49;00m))[37m[39;49;00m$
  4084^I[37m  [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m[31marg[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  4085^I[37m    [39;49;00m([32mskip-syntax-backward[39;49;00m[37m[39;49;00m$
  4086^I[37m     [39;49;00m([32mchar-to-string[39;49;00m[37m [39;49;00m([32mchar-syntax[39;49;00m[37m [39;49;00m([32mchar-before[39;49;00m))))[37m[39;49;00m$
  4087^I[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31marg[39;49;00m[37m [39;49;00m([32m1+[39;49;00m[37m [39;49;00m[31marg[39;49;00m)))[37m[39;49;00m$
  4088^I[37m  [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m[31marg[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  4089^I[37m    [39;49;00m([32mskip-syntax-forward[39;49;00m[37m [39;49;00m([32mchar-to-string[39;49;00m[37m [39;49;00m([32mchar-syntax[39;49;00m[37m [39;49;00m([32mchar-after[39;49;00m))))[37m[39;49;00m$
  4090^I[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31marg[39;49;00m[37m [39;49;00m([32m1-[39;49;00m[37m [39;49;00m[31marg[39;49;00m))))[37m[39;49;00m$
  4091^I[37m[39;49;00m$
  4092^I[37m[39;49;00m[37m[39;49;00m$
  4093^I[37m;;;; Text clones[39;49;00m[37m[39;49;00m$
  4094^I[37m[39;49;00m$
  4095^I([34mdefvar[39;49;00m[37m [39;49;00m[31mtext-clone--maintaining[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
  4096^I[37m[39;49;00m$
  4097^I([36mdefun[39;49;00m[37m [39;49;00m[31mtext-clone--maintain[39;49;00m[37m [39;49;00m([31mol1[39;49;00m[37m [39;49;00m[31mafter[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31m_len[39;49;00m)[37m[39;49;00m$
  4098^I[37m  [39;49;00m[33m"[39;49;00m[33mPropagate the changes made under the overlay OL1 to the other clones.[39;49;00m$
  4099^I[33mThis is used on the [39;49;00m[33m`modification-hooks'[39;49;00m[33m property of text clones.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  4100^I[37m  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mafter[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m[31mundo-in-progress[39;49;00m)[37m[39;49;00m$
  4101^I[37m             [39;49;00m([31mnot[39;49;00m[37m [39;49;00m[31mtext-clone--maintaining[39;49;00m)[37m[39;49;00m$
  4102^I[37m             [39;49;00m([32moverlay-start[39;49;00m[37m [39;49;00m[31mol1[39;49;00m))[37m[39;49;00m$
  4103^I[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mmargin[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32moverlay-get[39;49;00m[37m [39;49;00m[31mol1[39;49;00m[37m [39;49;00m[33m'text-clone-spreadp[39;49;00m)[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[34m0[39;49;00m)))[37m[39;49;00m$
  4104^I[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m[37m [39;49;00m([32mmax[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m[37m [39;49;00m([32m+[39;49;00m[37m [39;49;00m([32moverlay-start[39;49;00m[37m [39;49;00m[31mol1[39;49;00m)[37m [39;49;00m[31mmargin[39;49;00m)))[37m[39;49;00m$
  4105^I[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m([32mmin[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m([32moverlay-end[39;49;00m[37m [39;49;00m[31mol1[39;49;00m)[37m [39;49;00m[31mmargin[39;49;00m)))[37m[39;49;00m$
  4106^I[37m      [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32m<=[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m[37m [39;49;00m[31mend[39;49;00m)[37m[39;49;00m$
  4107^I[37m^I[39;49;00m([34msave-excursion[39;49;00m[37m[39;49;00m$
  4108^I[37m^I  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32moverlay-get[39;49;00m[37m [39;49;00m[31mol1[39;49;00m[37m [39;49;00m[33m'text-clone-syntax[39;49;00m)[37m[39;49;00m$
  4109^I[37m^I    [39;49;00m[37m;; Check content of the clone's text.[39;49;00m[37m[39;49;00m$
  4110^I[37m^I    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mcbeg[39;49;00m[37m [39;49;00m([32m+[39;49;00m[37m [39;49;00m([32moverlay-start[39;49;00m[37m [39;49;00m[31mol1[39;49;00m)[37m [39;49;00m[31mmargin[39;49;00m))[37m[39;49;00m$
  4111^I[37m^I^I  [39;49;00m([31mcend[39;49;00m[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m([32moverlay-end[39;49;00m[37m [39;49;00m[31mol1[39;49;00m)[37m [39;49;00m[31mmargin[39;49;00m)))[37m[39;49;00m$
  4112^I[37m^I      [39;49;00m([32mgoto-char[39;49;00m[37m [39;49;00m[31mcbeg[39;49;00m)[37m[39;49;00m$
  4113^I[37m^I      [39;49;00m([36msave-match-data[39;49;00m[37m[39;49;00m$
  4114^I[37m^I^I[39;49;00m([34mif[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mre-search-forward[39;49;00m[37m[39;49;00m$
  4115^I[37m^I^I^I  [39;49;00m([32moverlay-get[39;49;00m[37m [39;49;00m[31mol1[39;49;00m[37m [39;49;00m[33m'text-clone-syntax[39;49;00m)[37m [39;49;00m[31mcend[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
  4116^I[37m^I^I    [39;49;00m[37m;; Mark the overlay for deletion.[39;49;00m[37m[39;49;00m$
  4117^I[37m^I^I    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[31mcbeg[39;49;00m)[37m[39;49;00m$
  4118^I[37m^I^I  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m([32mmatch-end[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[31mcend[39;49;00m)[37m[39;49;00m$
  4119^I[37m^I^I    [39;49;00m[37m;; Shrink the clone at its end.[39;49;00m[37m[39;49;00m$
  4120^I[37m^I^I    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m([32mmin[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m([32mmatch-end[39;49;00m[37m [39;49;00m[34m0[39;49;00m)))[37m[39;49;00m$
  4121^I[37m^I^I    [39;49;00m([32mmove-overlay[39;49;00m[37m [39;49;00m[31mol1[39;49;00m[37m [39;49;00m([32moverlay-start[39;49;00m[37m [39;49;00m[31mol1[39;49;00m)[37m[39;49;00m$
  4122^I[37m^I^I^I^I  [39;49;00m([32m+[39;49;00m[37m [39;49;00m([32mmatch-end[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[31mmargin[39;49;00m)))[37m[39;49;00m$
  4123^I[37m^I^I  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m([32mmatch-beginning[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[31mcbeg[39;49;00m)[37m[39;49;00m$
  4124^I[37m^I^I    [39;49;00m[37m;; Shrink the clone at its beginning.[39;49;00m[37m[39;49;00m$
  4125^I[37m^I^I    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m[37m [39;49;00m([32mmax[39;49;00m[37m [39;49;00m([32mmatch-beginning[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[31mbeg[39;49;00m))[37m[39;49;00m$
  4126^I[37m^I^I    [39;49;00m([32mmove-overlay[39;49;00m[37m [39;49;00m[31mol1[39;49;00m[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m([32mmatch-beginning[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[31mmargin[39;49;00m)[37m[39;49;00m$
  4127^I[37m^I^I^I^I  [39;49;00m([32moverlay-end[39;49;00m[37m [39;49;00m[31mol1[39;49;00m)))))))[37m[39;49;00m$
  4128^I[37m^I  [39;49;00m[37m;; Now go ahead and update the clones.[39;49;00m[37m[39;49;00m$
  4129^I[37m^I  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mhead[39;49;00m[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m[37m [39;49;00m([32moverlay-start[39;49;00m[37m [39;49;00m[31mol1[39;49;00m)))[37m[39;49;00m$
  4130^I[37m^I^I[39;49;00m([31mtail[39;49;00m[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m([32moverlay-end[39;49;00m[37m [39;49;00m[31mol1[39;49;00m)[37m [39;49;00m[31mend[39;49;00m))[37m[39;49;00m$
  4131^I[37m^I^I[39;49;00m([31mstr[39;49;00m[37m [39;49;00m([32mbuffer-substring[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m[37m [39;49;00m[31mend[39;49;00m))[37m[39;49;00m$
  4132^I[37m^I^I[39;49;00m([31mnothing-left[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
  4133^I[37m^I^I[39;49;00m([31mtext-clone--maintaining[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
  4134^I[37m^I    [39;49;00m([36mdolist[39;49;00m[37m [39;49;00m([31mol2[39;49;00m[37m [39;49;00m([32moverlay-get[39;49;00m[37m [39;49;00m[31mol1[39;49;00m[37m [39;49;00m[33m'text-clones[39;49;00m))[37m[39;49;00m$
  4135^I[37m^I      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31moe[39;49;00m[37m [39;49;00m([32moverlay-end[39;49;00m[37m [39;49;00m[31mol2[39;49;00m)))[37m[39;49;00m$
  4136^I[37m^I^I[39;49;00m([36munless[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mol1[39;49;00m[37m [39;49;00m[31mol2[39;49;00m)[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[31moe[39;49;00m))[37m[39;49;00m$
  4137^I[37m^I^I  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mnothing-left[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
  4138^I[37m^I^I  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mmod-beg[39;49;00m[37m [39;49;00m([32m+[39;49;00m[37m [39;49;00m([32moverlay-start[39;49;00m[37m [39;49;00m[31mol2[39;49;00m)[37m [39;49;00m[31mhead[39;49;00m)))[37m[39;49;00m$
  4139^I[37m^I^I    [39;49;00m[37m;;(overlay-put ol2 'modification-hooks nil)[39;49;00m[37m[39;49;00m$
  4140^I[37m^I^I    [39;49;00m([32mgoto-char[39;49;00m[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m([32moverlay-end[39;49;00m[37m [39;49;00m[31mol2[39;49;00m)[37m [39;49;00m[31mtail[39;49;00m))[37m[39;49;00m$
  4141^I[37m^I^I    [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m[31mmod-beg[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m))[37m[39;49;00m$
  4142^I[37m^I^I      [39;49;00m([34msave-excursion[39;49;00m[37m [39;49;00m([32minsert[39;49;00m[37m [39;49;00m[31mstr[39;49;00m))[37m[39;49;00m$
  4143^I[37m^I^I      [39;49;00m([32mdelete-region[39;49;00m[37m [39;49;00m[31mmod-beg[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m)))[37m[39;49;00m$
  4144^I[37m^I^I    [39;49;00m[37m;;(overlay-put ol2 'modification-hooks '(text-clone--maintain))[39;49;00m[37m[39;49;00m$
  4145^I[37m^I^I    [39;49;00m))))[37m[39;49;00m$
  4146^I[37m^I    [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mnothing-left[39;49;00m[37m [39;49;00m([32mdelete-overlay[39;49;00m[37m [39;49;00m[31mol1[39;49;00m))))))))[37m[39;49;00m$
  4147^I[37m[39;49;00m$
  4148^I([36mdefun[39;49;00m[37m [39;49;00m[31mtext-clone-create[39;49;00m[37m [39;49;00m([31mstart[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mspreadp[39;49;00m[37m [39;49;00m[31msyntax[39;49;00m)[37m[39;49;00m$
  4149^I[37m  [39;49;00m[33m"[39;49;00m[33mCreate a text clone of START...END at point.[39;49;00m$
  4150^I[33mText clones are chunks of text that are automatically kept identical:[39;49;00m$
  4151^I[33mchanges done to one of the clones will be immediately propagated to the other.[39;49;00m$
  4152^I[33m[39;49;00m$
  4153^I[33mThe buffer's content at point is assumed to be already identical to[39;49;00m$
  4154^I[33mthe one between START and END.[39;49;00m$
  4155^I[33mIf SYNTAX is provided it's a regexp that describes the possible text of[39;49;00m$
  4156^I[33mthe clones; the clone will be shrunk or killed if necessary to ensure that[39;49;00m$
  4157^I[33mits text matches the regexp.[39;49;00m$
  4158^I[33mIf SPREADP is non-nil it indicates that text inserted before/after the[39;49;00m$
  4159^I[33mclone should be incorporated in the clone.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  4160^I[37m  [39;49;00m[37m;; To deal with SPREADP we can either use an overlay with `nil t' along[39;49;00m[37m[39;49;00m$
  4161^I[37m  [39;49;00m[37m;; with insert-(behind|in-front-of)-hooks or use a slightly larger overlay[39;49;00m[37m[39;49;00m$
  4162^I[37m  [39;49;00m[37m;; (with a one-char margin at each end) with `t nil'.[39;49;00m[37m[39;49;00m$
  4163^I[37m  [39;49;00m[37m;; We opted for a larger overlay because it behaves better in the case[39;49;00m[37m[39;49;00m$
  4164^I[37m  [39;49;00m[37m;; where the clone is reduced to the empty string (we want the overlay to[39;49;00m[37m[39;49;00m$
  4165^I[37m  [39;49;00m[37m;; stay when the clone's content is the empty string and we want to use[39;49;00m[37m[39;49;00m$
  4166^I[37m  [39;49;00m[37m;; `evaporate' to make sure those overlays get deleted when needed).[39;49;00m[37m[39;49;00m$
  4167^I[37m  [39;49;00m[37m;;[39;49;00m[37m[39;49;00m$
  4168^I[37m  [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mpt-end[39;49;00m[37m [39;49;00m([32m+[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m)[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[31mstart[39;49;00m)))[37m[39;49;00m$
  4169^I[37m  ^I [39;49;00m([31mstart-margin[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m[31mspreadp[39;49;00m)[37m [39;49;00m([32mbobp[39;49;00m)[37m [39;49;00m([32m<=[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m([32mpoint-min[39;49;00m)))[37m[39;49;00m$
  4170^I[37m^I^I^I   [39;49;00m[34m0[39;49;00m[37m [39;49;00m[34m1[39;49;00m))[37m[39;49;00m$
  4171^I[37m  ^I [39;49;00m([31mend-margin[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m[31mspreadp[39;49;00m)[37m[39;49;00m$
  4172^I[37m^I^I^I     [39;49;00m([32m>=[39;49;00m[37m [39;49;00m[31mpt-end[39;49;00m[37m [39;49;00m([32mpoint-max[39;49;00m))[37m[39;49;00m$
  4173^I[37m  ^I^I^I     [39;49;00m([32m>=[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m([32mpoint-max[39;49;00m)))[37m[39;49;00m$
  4174^I[37m  ^I^I^I [39;49;00m[34m0[39;49;00m[37m [39;49;00m[34m1[39;49;00m))[37m[39;49;00m$
  4175^I[37m         [39;49;00m[37m;; FIXME: Reuse overlays at point to extend dups![39;49;00m[37m[39;49;00m$
  4176^I[37m  ^I [39;49;00m([31mol1[39;49;00m[37m [39;49;00m([32mmake-overlay[39;49;00m[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mstart-margin[39;49;00m)[37m [39;49;00m([32m+[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[31mend-margin[39;49;00m)[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
  4177^I[37m  ^I [39;49;00m([31mol2[39;49;00m[37m [39;49;00m([32mmake-overlay[39;49;00m[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m)[37m [39;49;00m[31mstart-margin[39;49;00m)[37m [39;49;00m([32m+[39;49;00m[37m [39;49;00m[31mpt-end[39;49;00m[37m [39;49;00m[31mend-margin[39;49;00m)[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
  4178^I[37m^I [39;49;00m([31mdups[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[31mol1[39;49;00m[37m [39;49;00m[31mol2[39;49;00m)))[37m[39;49;00m$
  4179^I[37m    [39;49;00m([32moverlay-put[39;49;00m[37m [39;49;00m[31mol1[39;49;00m[37m [39;49;00m[33m'modification-hooks[39;49;00m[37m [39;49;00m'([31mtext-clone--maintain[39;49;00m))[37m[39;49;00m$
  4180^I[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31mspreadp[39;49;00m[37m [39;49;00m([32moverlay-put[39;49;00m[37m [39;49;00m[31mol1[39;49;00m[37m [39;49;00m[33m'text-clone-spreadp[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
  4181^I[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31msyntax[39;49;00m[37m [39;49;00m([32moverlay-put[39;49;00m[37m [39;49;00m[31mol1[39;49;00m[37m [39;49;00m[33m'text-clone-syntax[39;49;00m[37m [39;49;00m[31msyntax[39;49;00m))[37m[39;49;00m$
  4182^I[37m    [39;49;00m[37m;;(overlay-put ol1 'face 'underline)[39;49;00m[37m[39;49;00m$
  4183^I[37m    [39;49;00m([32moverlay-put[39;49;00m[37m [39;49;00m[31mol1[39;49;00m[37m [39;49;00m[33m'evaporate[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
  4184^I[37m    [39;49;00m([32moverlay-put[39;49;00m[37m [39;49;00m[31mol1[39;49;00m[37m [39;49;00m[33m'text-clones[39;49;00m[37m [39;49;00m[31mdups[39;49;00m)[37m[39;49;00m$
  4185^I[37m    [39;49;00m[37m;;[39;49;00m[37m[39;49;00m$
  4186^I[37m    [39;49;00m([32moverlay-put[39;49;00m[37m [39;49;00m[31mol2[39;49;00m[37m [39;49;00m[33m'modification-hooks[39;49;00m[37m [39;49;00m'([31mtext-clone--maintain[39;49;00m))[37m[39;49;00m$
  4187^I[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31mspreadp[39;49;00m[37m [39;49;00m([32moverlay-put[39;49;00m[37m [39;49;00m[31mol2[39;49;00m[37m [39;49;00m[33m'text-clone-spreadp[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
  4188^I[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31msyntax[39;49;00m[37m [39;49;00m([32moverlay-put[39;49;00m[37m [39;49;00m[31mol2[39;49;00m[37m [39;49;00m[33m'text-clone-syntax[39;49;00m[37m [39;49;00m[31msyntax[39;49;00m))[37m[39;49;00m$
  4189^I[37m    [39;49;00m[37m;;(overlay-put ol2 'face 'underline)[39;49;00m[37m[39;49;00m$
  4190^I[37m    [39;49;00m([32moverlay-put[39;49;00m[37m [39;49;00m[31mol2[39;49;00m[37m [39;49;00m[33m'evaporate[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
  4191^I[37m    [39;49;00m([32moverlay-put[39;49;00m[37m [39;49;00m[31mol2[39;49;00m[37m [39;49;00m[33m'text-clones[39;49;00m[37m [39;49;00m[31mdups[39;49;00m)))[37m[39;49;00m$
  4192^I[37m[39;49;00m[37m[39;49;00m$
  4193^I[37m;;;; Mail user agents.[39;49;00m[37m[39;49;00m$
  4194^I[37m[39;49;00m$
  4195^I[37m;; Here we include just enough for other packages to be able[39;49;00m[37m[39;49;00m$
  4196^I[37m;; to define them.[39;49;00m[37m[39;49;00m$
  4197^I[37m[39;49;00m$
  4198^I([36mdefun[39;49;00m[37m [39;49;00m[31mdefine-mail-user-agent[39;49;00m[37m [39;49;00m([31msymbol[39;49;00m[37m [39;49;00m[31mcomposefunc[39;49;00m[37m [39;49;00m[31msendfunc[39;49;00m[37m[39;49;00m$
  4199^I[37m^I^I^I^I      [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mabortfunc[39;49;00m[37m [39;49;00m[31mhookvar[39;49;00m)[37m[39;49;00m$
  4200^I[37m  [39;49;00m[33m"[39;49;00m[33mDefine a symbol to identify a mail-sending package for [39;49;00m[33m`mail-user-agent'[39;49;00m[33m.[39;49;00m$
  4201^I[33m[39;49;00m$
  4202^I[33mSYMBOL can be any Lisp symbol.  Its function definition and/or[39;49;00m$
  4203^I[33mvalue as a variable do not matter for this usage; we use only certain[39;49;00m$
  4204^I[33mproperties on its property list, to encode the rest of the arguments.[39;49;00m$
  4205^I[33m[39;49;00m$
  4206^I[33mCOMPOSEFUNC is program callable function that composes an outgoing[39;49;00m$
  4207^I[33mmail message buffer.  This function should set up the basics of the[39;49;00m$
  4208^I[33mbuffer without requiring user interaction.  It should populate the[39;49;00m$
  4209^I[33mstandard mail headers, leaving the [39;49;00m[33m`to:'[39;49;00m[33m and [39;49;00m[33m`subject:'[39;49;00m[33m headers blank[39;49;00m$
  4210^I[33mby default.[39;49;00m$
  4211^I[33m[39;49;00m$
  4212^I[33mCOMPOSEFUNC should accept several optional arguments--the same[39;49;00m$
  4213^I[33marguments that [39;49;00m[33m`compose-mail'[39;49;00m[33m takes.  See that function's documentation.[39;49;00m$
  4214^I[33m[39;49;00m$
  4215^I[33mSENDFUNC is the command a user would run to send the message.[39;49;00m$
  4216^I[33m[39;49;00m$
  4217^I[33mOptional ABORTFUNC is the command a user would run to abort the[39;49;00m$
  4218^I[33mmessage.  For mail packages that don't have a separate abort function,[39;49;00m$
  4219^I[33mthis can be [39;49;00m[33m`kill-buffer'[39;49;00m[33m (the equivalent of omitting this argument).[39;49;00m$
  4220^I[33m[39;49;00m$
  4221^I[33mOptional HOOKVAR is a hook variable that gets run before the message[39;49;00m$
  4222^I[33mis actually sent.  Callers that use the [39;49;00m[33m`mail-user-agent'[39;49;00m[33m may[39;49;00m$
  4223^I[33minstall a hook function temporarily on this hook variable.[39;49;00m$
  4224^I[33mIf HOOKVAR is nil, [39;49;00m[33m`mail-send-hook'[39;49;00m[33m is used.[39;49;00m$
  4225^I[33m[39;49;00m$
  4226^I[33mThe properties used on SYMBOL are [39;49;00m[33m`composefunc'[39;49;00m[33m, [39;49;00m[33m`sendfunc'[39;49;00m[33m,[39;49;00m$
  4227^I[33m`abortfunc'[39;49;00m[33m, and [39;49;00m[33m`hookvar'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  4228^I[37m  [39;49;00m([32mput[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m[37m [39;49;00m[33m'composefunc[39;49;00m[37m [39;49;00m[31mcomposefunc[39;49;00m)[37m[39;49;00m$
  4229^I[37m  [39;49;00m([32mput[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m[37m [39;49;00m[33m'sendfunc[39;49;00m[37m [39;49;00m[31msendfunc[39;49;00m)[37m[39;49;00m$
  4230^I[37m  [39;49;00m([32mput[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m[37m [39;49;00m[33m'abortfunc[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mabortfunc[39;49;00m[37m [39;49;00m[33m'kill-buffer[39;49;00m))[37m[39;49;00m$
  4231^I[37m  [39;49;00m([32mput[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m[37m [39;49;00m[33m'hookvar[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mhookvar[39;49;00m[37m [39;49;00m[33m'mail-send-hook[39;49;00m)))[37m[39;49;00m$
  4232^I[37m[39;49;00m[37m[39;49;00m$
  4233^I([34mdefvar[39;49;00m[37m [39;49;00m[31mcalled-interactively-p-functions[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m$
  4234^I[37m  [39;49;00m[33m"[39;49;00m[33mSpecial hook called to skip special frames in [39;49;00m[33m`called-interactively-p'[39;49;00m[33m.[39;49;00m$
  4235^I[33mThe functions are called with 3 arguments: (I FRAME1 FRAME2),[39;49;00m$
  4236^I[33mwhere FRAME1 is a [39;49;00m[33m\"[39;49;00m[33mcurrent frame[39;49;00m[33m\"[39;49;00m[33m, FRAME2 is the next frame,[39;49;00m$
  4237^I[33mI is the index of the frame after FRAME2.  It should return nil[39;49;00m$
  4238^I[33mif those frames don't seem special and otherwise, it should return[39;49;00m$
  4239^I[33mthe number of frames to skip (minus 1).[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  4240^I[37m[39;49;00m$
  4241^I([34mdefconst[39;49;00m[37m [39;49;00m[31minternal--funcall-interactively[39;49;00m[37m[39;49;00m$
  4242^I[37m  [39;49;00m([32msymbol-function[39;49;00m[37m [39;49;00m[33m'funcall-interactively[39;49;00m))[37m[39;49;00m$
  4243^I[37m[39;49;00m$
  4244^I([36mdefun[39;49;00m[37m [39;49;00m[31mcalled-interactively-p[39;49;00m[37m [39;49;00m([34m&optional[39;49;00m[37m [39;49;00m[31mkind[39;49;00m)[37m[39;49;00m$
  4245^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn t if the containing function was called by [39;49;00m[33m`call-interactively'[39;49;00m[33m.[39;49;00m$
  4246^I[33mIf KIND is [39;49;00m[33m`interactive'[39;49;00m[33m, then only return t if the call was made[39;49;00m$
  4247^I[33minteractively by the user, i.e. not in [39;49;00m[33m`noninteractive'[39;49;00m[33m mode nor[39;49;00m$
  4248^I[33mwhen [39;49;00m[33m`executing-kbd-macro'[39;49;00m[33m.[39;49;00m$
  4249^I[33mIf KIND is [39;49;00m[33m`any'[39;49;00m[33m, on the other hand, it will return t for any kind of[39;49;00m$
  4250^I[33minteractive call, including being called as the binding of a key or[39;49;00m$
  4251^I[33mfrom a keyboard macro, even in [39;49;00m[33m`noninteractive'[39;49;00m[33m mode.[39;49;00m$
  4252^I[33m[39;49;00m$
  4253^I[33mThis function is very brittle, it may fail to return the intended result when[39;49;00m$
  4254^I[33mthe code is debugged, advised, or instrumented in some form.  Some macros and[39;49;00m$
  4255^I[33mspecial forms (such as [39;49;00m[33m`condition-case'[39;49;00m[33m) may also sometimes wrap their bodies[39;49;00m$
  4256^I[33min a [39;49;00m[33m`lambda'[39;49;00m[33m, so any call to [39;49;00m[33m`called-interactively-p'[39;49;00m[33m from those bodies will[39;49;00m$
  4257^I[33mindicate whether that lambda (rather than the surrounding function) was called[39;49;00m$
  4258^I[33minteractively.[39;49;00m$
  4259^I[33m[39;49;00m$
  4260^I[33mInstead of using this function, it is cleaner and more reliable to give your[39;49;00m$
  4261^I[33mfunction an extra optional argument whose [39;49;00m[33m`interactive'[39;49;00m[33m spec specifies[39;49;00m$
  4262^I[33mnon-nil unconditionally ([39;49;00m[33m\"[39;49;00m[33mp[39;49;00m[33m\"[39;49;00m[33m is a good way to do this), or via[39;49;00m$
  4263^I[33m\([39;49;00m[33mnot (or executing-kbd-macro noninteractive)).[39;49;00m$
  4264^I[33m[39;49;00m$
  4265^I[33mThe only known proper use of [39;49;00m[33m`interactive'[39;49;00m[33m for KIND is in deciding[39;49;00m$
  4266^I[33mwhether to display a helpful message, or how to display it.  If you're[39;49;00m$
  4267^I[33mthinking of using it for any other purpose, it is quite likely that[39;49;00m$
  4268^I[33myou're making a mistake.  Think: what do you want to do when the[39;49;00m$
  4269^I[33mcommand is called from a keyboard macro?[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  4270^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31madvertised-calling-convention[39;49;00m[37m [39;49;00m([31mkind[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m23.1[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
  4271^I[37m  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mkind[39;49;00m[37m [39;49;00m[33m'interactive[39;49;00m)[37m[39;49;00m$
  4272^I[37m                  [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mexecuting-kbd-macro[39;49;00m[37m [39;49;00m[31mnoninteractive[39;49;00m)))[37m[39;49;00m$
  4273^I[37m    [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mi[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m[37m;; 0 is the called-interactively-p frame.[39;49;00m[37m[39;49;00m$
  4274^I[37m           [39;49;00m[31mframe[39;49;00m[37m [39;49;00m[31mnextframe[39;49;00m[37m[39;49;00m$
  4275^I[37m           [39;49;00m([31mget-next-frame[39;49;00m[37m[39;49;00m$
  4276^I[37m            [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m()[37m[39;49;00m$
  4277^I[37m              [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mframe[39;49;00m[37m [39;49;00m[31mnextframe[39;49;00m)[37m[39;49;00m$
  4278^I[37m              [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mnextframe[39;49;00m[37m [39;49;00m([32mbacktrace-frame[39;49;00m[37m [39;49;00m[31mi[39;49;00m[37m [39;49;00m[33m'called-interactively-p[39;49;00m))[37m[39;49;00m$
  4279^I[37m              [39;49;00m[37m;; (message "Frame %d = %S" i nextframe)[39;49;00m[37m[39;49;00m$
  4280^I[37m              [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mi[39;49;00m[37m [39;49;00m([32m1+[39;49;00m[37m [39;49;00m[31mi[39;49;00m)))))[37m[39;49;00m$
  4281^I[37m      [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mget-next-frame[39;49;00m)[37m [39;49;00m[37m;; Get the first frame.[39;49;00m[37m[39;49;00m$
  4282^I[37m      [39;49;00m([34mwhile[39;49;00m[37m[39;49;00m$
  4283^I[37m          [39;49;00m[37m;; FIXME: The edebug and advice handling should be made modular and[39;49;00m[37m[39;49;00m$
  4284^I[37m          [39;49;00m[37m;; provided directly by edebug.el and nadvice.el.[39;49;00m[37m[39;49;00m$
  4285^I[37m          [39;49;00m([34mprogn[39;49;00m[37m[39;49;00m$
  4286^I[37m            [39;49;00m[37m;; frame    =(backtrace-frame i-2)[39;49;00m[37m[39;49;00m$
  4287^I[37m            [39;49;00m[37m;; nextframe=(backtrace-frame i-1)[39;49;00m[37m[39;49;00m$
  4288^I[37m            [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mget-next-frame[39;49;00m)[37m[39;49;00m$
  4289^I[37m            [39;49;00m[37m;; `pcase' would be a fairly good fit here, but it sometimes moves[39;49;00m[37m[39;49;00m$
  4290^I[37m            [39;49;00m[37m;; branches within local functions, which then messes up the[39;49;00m[37m[39;49;00m$
  4291^I[37m            [39;49;00m[37m;; `backtrace-frame' data we get,[39;49;00m[37m[39;49;00m$
  4292^I[37m            [39;49;00m([34mor[39;49;00m[37m[39;49;00m$
  4293^I[37m             [39;49;00m[37m;; Skip special forms (from non-compiled code).[39;49;00m[37m[39;49;00m$
  4294^I[37m             [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mframe[39;49;00m[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mframe[39;49;00m)))[37m[39;49;00m$
  4295^I[37m             [39;49;00m[37m;; Skip also `interactive-p' (because we don't want to know if[39;49;00m[37m[39;49;00m$
  4296^I[37m             [39;49;00m[37m;; interactive-p was called interactively but if it's caller was)[39;49;00m[37m[39;49;00m$
  4297^I[37m             [39;49;00m[37m;; and `byte-code' (idem; this appears in subexpressions of things[39;49;00m[37m[39;49;00m$
  4298^I[37m             [39;49;00m[37m;; like condition-case, which are wrapped in a separate bytecode[39;49;00m[37m[39;49;00m$
  4299^I[37m             [39;49;00m[37m;; chunk).[39;49;00m[37m[39;49;00m$
  4300^I[37m             [39;49;00m[37m;; FIXME: For lexical-binding code, this is much worse,[39;49;00m[37m[39;49;00m$
  4301^I[37m             [39;49;00m[37m;; because the frames look like "byte-code -> funcall -> #[...]",[39;49;00m[37m[39;49;00m$
  4302^I[37m             [39;49;00m[37m;; which is not a reliable signature.[39;49;00m[37m[39;49;00m$
  4303^I[37m             [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mframe[39;49;00m)[37m [39;49;00m'([31minteractive-p[39;49;00m[37m [39;49;00m[33m'byte-code[39;49;00m))[37m[39;49;00m$
  4304^I[37m             [39;49;00m[37m;; Skip package-specific stack-frames.[39;49;00m[37m[39;49;00m$
  4305^I[37m             [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mskip[39;49;00m[37m [39;49;00m([32mrun-hook-with-args-until-success[39;49;00m[37m[39;49;00m$
  4306^I[37m                          [39;49;00m[33m'called-interactively-p-functions[39;49;00m[37m[39;49;00m$
  4307^I[37m                          [39;49;00m[31mi[39;49;00m[37m [39;49;00m[31mframe[39;49;00m[37m [39;49;00m[31mnextframe[39;49;00m)))[37m[39;49;00m$
  4308^I[37m               [39;49;00m([36mpcase[39;49;00m[37m [39;49;00m[31mskip[39;49;00m[37m[39;49;00m$
  4309^I[37m                 [39;49;00m(`[31mnil[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
  4310^I[37m                 [39;49;00m(`[34m0[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
  4311^I[37m                 [39;49;00m([31m_[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mi[39;49;00m[37m [39;49;00m([32m+[39;49;00m[37m [39;49;00m[31mi[39;49;00m[37m [39;49;00m[31mskip[39;49;00m[37m [39;49;00m[34m-1[39;49;00m))[37m [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mget-next-frame[39;49;00m)))))))[37m[39;49;00m$
  4312^I[37m      [39;49;00m[37m;; Now `frame' should be "the function from which we were called".[39;49;00m[37m[39;49;00m$
  4313^I[37m      [39;49;00m([36mpcase[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mframe[39;49;00m[37m [39;49;00m[31mnextframe[39;49;00m)[37m[39;49;00m$
  4314^I[37m        [39;49;00m[37m;; No subr calls `interactive-p', so we can rule that out.[39;49;00m[37m[39;49;00m$
  4315^I[37m        [39;49;00m(`((,[31m_[39;49;00m[37m [39;49;00m,([31mpred[39;49;00m[37m [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31mf[39;49;00m)[37m [39;49;00m([32msubrp[39;49;00m[37m [39;49;00m([32mindirect-function[39;49;00m[37m [39;49;00m[31mf[39;49;00m))))[37m [39;49;00m.[37m [39;49;00m,[31m_[39;49;00m)[37m [39;49;00m.[37m [39;49;00m,[31m_[39;49;00m)[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
  4316^I[37m        [39;49;00m[37m;; In case #<subr funcall-interactively> without going through the[39;49;00m[37m[39;49;00m$
  4317^I[37m        [39;49;00m[37m;; `funcall-interactively' symbol (bug#3984).[39;49;00m[37m[39;49;00m$
  4318^I[37m        [39;49;00m(`(,[31m_[39;49;00m[37m [39;49;00m.[37m [39;49;00m([31mt[39;49;00m[37m [39;49;00m,([31mpred[39;49;00m[37m [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31mf[39;49;00m)[37m[39;49;00m$
  4319^I[37m                            [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31minternal--funcall-interactively[39;49;00m[37m[39;49;00m$
  4320^I[37m                                [39;49;00m([32mindirect-function[39;49;00m[37m [39;49;00m[31mf[39;49;00m))))[37m[39;49;00m$
  4321^I[37m                   [39;49;00m.[37m [39;49;00m,[31m_[39;49;00m))[37m[39;49;00m$
  4322^I[37m         [39;49;00m[31mt[39;49;00m)))))[37m[39;49;00m$
  4323^I[37m[39;49;00m$
  4324^I([36mdefun[39;49;00m[37m [39;49;00m[31minteractive-p[39;49;00m[37m [39;49;00m()[37m[39;49;00m$
  4325^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn t if the containing function was run directly by user input.[39;49;00m$
  4326^I[33mThis means that the function was called with [39;49;00m[33m`call-interactively'[39;49;00m[33m[39;49;00m$
  4327^I[33m\([39;49;00m[33mwhich includes being called as the binding of a key)[39;49;00m$
  4328^I[33mand input is currently coming from the keyboard (not a keyboard macro),[39;49;00m$
  4329^I[33mand Emacs is not running in batch mode ([39;49;00m[33m`noninteractive'[39;49;00m[33m is nil).[39;49;00m$
  4330^I[33m[39;49;00m$
  4331^I[33mThe only known proper use of [39;49;00m[33m`interactive-p'[39;49;00m[33m is in deciding whether to[39;49;00m$
  4332^I[33mdisplay a helpful message, or how to display it.  If you're thinking[39;49;00m$
  4333^I[33mof using it for any other purpose, it is quite likely that you're[39;49;00m$
  4334^I[33mmaking a mistake.  Think: what do you want to do when the command is[39;49;00m$
  4335^I[33mcalled from a keyboard macro or in batch mode?[39;49;00m$
  4336^I[33m[39;49;00m$
  4337^I[33mTo test whether your function was called with [39;49;00m[33m`call-interactively'[39;49;00m[33m,[39;49;00m$
  4338^I[33meither (i) add an extra optional argument and give it an [39;49;00m[33m`interactive'[39;49;00m[33m[39;49;00m$
  4339^I[33mspec that specifies non-nil unconditionally (such as [39;49;00m[33m\"[39;49;00m[33mp[39;49;00m[33m\"[39;49;00m[33m); or (ii)[39;49;00m$
  4340^I[33muse [39;49;00m[33m`called-interactively-p'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  4341^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mobsolete[39;49;00m[37m [39;49;00m[31mcalled-interactively-p[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
  4342^I[37m  [39;49;00m([31mcalled-interactively-p[39;49;00m[37m [39;49;00m[33m'interactive[39;49;00m))[37m[39;49;00m$
  4343^I[37m[39;49;00m$
  4344^I([36mdefun[39;49;00m[37m [39;49;00m[31minternal-push-keymap[39;49;00m[37m [39;49;00m([31mkeymap[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m)[37m[39;49;00m$
  4345^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mmap[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m)))[37m[39;49;00m$
  4346^I[37m    [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m[37m [39;49;00m[31mmap[39;49;00m)[37m[39;49;00m$
  4347^I[37m      [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[33m'add-keymap-witness[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m))[37m[39;49;00m$
  4348^I[37m        [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m([31mmake-composed-keymap[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m)))[37m[39;49;00m$
  4349^I[37m        [39;49;00m([36mpush[39;49;00m[37m [39;49;00m[33m'add-keymap-witness[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mmap[39;49;00m))[37m[39;49;00m$
  4350^I[37m        [39;49;00m([32mset[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m[37m [39;49;00m[31mmap[39;49;00m))[37m[39;49;00m$
  4351^I[37m      [39;49;00m([36mpush[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mmap[39;49;00m)))))[37m[39;49;00m$
  4352^I[37m[39;49;00m$
  4353^I([36mdefun[39;49;00m[37m [39;49;00m[31minternal-pop-keymap[39;49;00m[37m [39;49;00m([31mkeymap[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m)[37m[39;49;00m$
  4354^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mmap[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m)))[37m[39;49;00m$
  4355^I[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m[37m [39;49;00m[31mmap[39;49;00m)[37m[39;49;00m$
  4356^I[37m      [39;49;00m([36msetf[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mmap[39;49;00m)[37m [39;49;00m([32mdelq[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mmap[39;49;00m))))[37m[39;49;00m$
  4357^I[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtail[39;49;00m[37m [39;49;00m([31mcddr[39;49;00m[37m [39;49;00m[31mmap[39;49;00m)))[37m[39;49;00m$
  4358^I[37m      [39;49;00m([34mand[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)[37m [39;49;00m([32mkeymapp[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))[37m[39;49;00m$
  4359^I[37m           [39;49;00m([32meq[39;49;00m[37m [39;49;00m[33m'add-keymap-witness[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mmap[39;49;00m))[37m[39;49;00m$
  4360^I[37m           [39;49;00m([32mset[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)))))[37m[39;49;00m$
  4361^I[37m[39;49;00m$
  4362^I([36mdefine-obsolete-function-alias[39;49;00m[37m[39;49;00m$
  4363^I[37m  [39;49;00m[33m'set-temporary-overlay-map[39;49;00m[37m [39;49;00m[33m'set-transient-map[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m24.4[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  4364^I[37m[39;49;00m$
  4365^I([36mdefun[39;49;00m[37m [39;49;00m[31mset-transient-map[39;49;00m[37m [39;49;00m([31mmap[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mkeep-pred[39;49;00m[37m [39;49;00m[31mon-exit[39;49;00m)[37m[39;49;00m$
  4366^I[37m  [39;49;00m[33m"[39;49;00m[33mSet MAP as a temporary keymap taking precedence over other keymaps.[39;49;00m$
  4367^I[33mNormally, MAP is used only once, to look up the very next key.[39;49;00m$
  4368^I[33mHowever, if the optional argument KEEP-PRED is t, MAP stays[39;49;00m$
  4369^I[33mactive if a key from MAP is used.  KEEP-PRED can also be a[39;49;00m$
  4370^I[33mfunction of no arguments: it is called from [39;49;00m[33m`pre-command-hook'[39;49;00m[33m and[39;49;00m$
  4371^I[33mif it returns non-nil, then MAP stays active.[39;49;00m$
  4372^I[33m[39;49;00m$
  4373^I[33mOptional arg ON-EXIT, if non-nil, specifies a function that is[39;49;00m$
  4374^I[33mcalled, with no arguments, after MAP is deactivated.[39;49;00m$
  4375^I[33m[39;49;00m$
  4376^I[33mThis uses [39;49;00m[33m`overriding-terminal-local-map'[39;49;00m[33m which takes precedence over all other[39;49;00m$
  4377^I[33mkeymaps.  As usual, if no match for a key is found in MAP, the normal key[39;49;00m$
  4378^I[33mlookup sequence then continues.[39;49;00m$
  4379^I[33m[39;49;00m$
  4380^I[33mThis returns an [39;49;00m[33m\"[39;49;00m[33mexit function[39;49;00m[33m\"[39;49;00m[33m, which can be called with no argument[39;49;00m$
  4381^I[33mto deactivate this transient map, regardless of KEEP-PRED.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  4382^I[37m  [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mclearfun[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mclear-transient-map[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
  4383^I[37m         [39;49;00m([31mexitfun[39;49;00m[37m[39;49;00m$
  4384^I[37m          [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m()[37m[39;49;00m$
  4385^I[37m            [39;49;00m([31minternal-pop-keymap[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m[33m'overriding-terminal-local-map[39;49;00m)[37m[39;49;00m$
  4386^I[37m            [39;49;00m([31mremove-hook[39;49;00m[37m [39;49;00m[33m'pre-command-hook[39;49;00m[37m [39;49;00m[31mclearfun[39;49;00m)[37m[39;49;00m$
  4387^I[37m            [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31mon-exit[39;49;00m[37m [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mon-exit[39;49;00m)))))[37m[39;49;00m$
  4388^I[37m    [39;49;00m[37m;; Don't use letrec, because equal (in add/remove-hook) would get trapped[39;49;00m[37m[39;49;00m$
  4389^I[37m    [39;49;00m[37m;; in a cycle.[39;49;00m[37m[39;49;00m$
  4390^I[37m    [39;49;00m([32mfset[39;49;00m[37m [39;49;00m[31mclearfun[39;49;00m[37m[39;49;00m$
  4391^I[37m          [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m()[37m[39;49;00m$
  4392^I[37m            [39;49;00m([36mwith-demoted-errors[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mset-transient-map PCH: %S[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  4393^I[37m              [39;49;00m([36munless[39;49;00m[37m [39;49;00m([34mcond[39;49;00m[37m[39;49;00m$
  4394^I[37m                       [39;49;00m(([32mnull[39;49;00m[37m [39;49;00m[31mkeep-pred[39;49;00m)[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
  4395^I[37m                       [39;49;00m(([31mnot[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m([31mcadr[39;49;00m[37m [39;49;00m[31moverriding-terminal-local-map[39;49;00m)))[37m[39;49;00m$
  4396^I[37m                        [39;49;00m[37m;; There's presumably some other transient-map in[39;49;00m[37m[39;49;00m$
  4397^I[37m                        [39;49;00m[37m;; effect.  Wait for that one to terminate before we[39;49;00m[37m[39;49;00m$
  4398^I[37m                        [39;49;00m[37m;; remove ourselves.[39;49;00m[37m[39;49;00m$
  4399^I[37m                        [39;49;00m[37m;; For example, if isearch and C-u both use transient[39;49;00m[37m[39;49;00m$
  4400^I[37m                        [39;49;00m[37m;; maps, then the lifetime of the C-u should be nested[39;49;00m[37m[39;49;00m$
  4401^I[37m                        [39;49;00m[37m;; within isearch's, so the pre-command-hook of[39;49;00m[37m[39;49;00m$
  4402^I[37m                        [39;49;00m[37m;; isearch should be suspended during the C-u one so[39;49;00m[37m[39;49;00m$
  4403^I[37m                        [39;49;00m[37m;; we don't exit isearch just because we hit 1 after[39;49;00m[37m[39;49;00m$
  4404^I[37m                        [39;49;00m[37m;; C-u and that 1 exits isearch whereas it doesn't[39;49;00m[37m[39;49;00m$
  4405^I[37m                        [39;49;00m[37m;; exit C-u.[39;49;00m[37m[39;49;00m$
  4406^I[37m                        [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
  4407^I[37m                       [39;49;00m(([32meq[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m[31mkeep-pred[39;49;00m)[37m[39;49;00m$
  4408^I[37m                        [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mthis-command[39;49;00m[37m[39;49;00m$
  4409^I[37m                            [39;49;00m([32mlookup-key[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m([32mthis-command-keys-vector[39;49;00m))))[37m[39;49;00m$
  4410^I[37m                       [39;49;00m([31mt[39;49;00m[37m [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mkeep-pred[39;49;00m)))[37m[39;49;00m$
  4411^I[37m                [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mexitfun[39;49;00m)))))[37m[39;49;00m$
  4412^I[37m    [39;49;00m([31madd-hook[39;49;00m[37m [39;49;00m[33m'pre-command-hook[39;49;00m[37m [39;49;00m[31mclearfun[39;49;00m)[37m[39;49;00m$
  4413^I[37m    [39;49;00m([31minternal-push-keymap[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m[33m'overriding-terminal-local-map[39;49;00m)[37m[39;49;00m$
  4414^I[37m    [39;49;00m[31mexitfun[39;49;00m))[37m[39;49;00m$
  4415^I[37m[39;49;00m$
  4416^I[37m;;;; Progress reporters.[39;49;00m[37m[39;49;00m$
  4417^I[37m[39;49;00m$
  4418^I[37m;; Progress reporter has the following structure:[39;49;00m[37m[39;49;00m$
  4419^I[37m;;[39;49;00m[37m[39;49;00m$
  4420^I[37m;;^I(NEXT-UPDATE-VALUE . [NEXT-UPDATE-TIME[39;49;00m[37m[39;49;00m$
  4421^I[37m;;^I^I^I      MIN-VALUE[39;49;00m[37m[39;49;00m$
  4422^I[37m;;^I^I^I      MAX-VALUE[39;49;00m[37m[39;49;00m$
  4423^I[37m;;^I^I^I      MESSAGE[39;49;00m[37m[39;49;00m$
  4424^I[37m;;^I^I^I      MIN-CHANGE[39;49;00m[37m[39;49;00m$
  4425^I[37m;;^I^I^I      MIN-TIME])[39;49;00m[37m[39;49;00m$
  4426^I[37m;;[39;49;00m[37m[39;49;00m$
  4427^I[37m;; This weirdness is for optimization reasons: we want[39;49;00m[37m[39;49;00m$
  4428^I[37m;; `progress-reporter-update' to be as fast as possible, so[39;49;00m[37m[39;49;00m$
  4429^I[37m;; `(car reporter)' is better than `(aref reporter 0)'.[39;49;00m[37m[39;49;00m$
  4430^I[37m;;[39;49;00m[37m[39;49;00m$
  4431^I[37m;; NEXT-UPDATE-TIME is a float.  While `float-time' loses a couple[39;49;00m[37m[39;49;00m$
  4432^I[37m;; digits of precision, it doesn't really matter here.  On the other[39;49;00m[37m[39;49;00m$
  4433^I[37m;; hand, it greatly simplifies the code.[39;49;00m[37m[39;49;00m$
  4434^I[37m[39;49;00m$
  4435^I([36mdefsubst[39;49;00m[37m [39;49;00m[31mprogress-reporter-update[39;49;00m[37m [39;49;00m([31mreporter[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mvalue[39;49;00m)[37m[39;49;00m$
  4436^I[37m  [39;49;00m[33m"[39;49;00m[33mReport progress of an operation in the echo area.[39;49;00m$
  4437^I[33mREPORTER should be the result of a call to [39;49;00m[33m`make-progress-reporter'[39;49;00m[33m.[39;49;00m$
  4438^I[33m[39;49;00m$
  4439^I[33mIf REPORTER is a numerical progress reporter---i.e. if it was[39;49;00m$
  4440^I[33m made using non-nil MIN-VALUE and MAX-VALUE arguments to[39;49;00m$
  4441^I[33m [39;49;00m[33m`make-progress-reporter'[39;49;00m[33m---then VALUE should be a number between[39;49;00m$
  4442^I[33m MIN-VALUE and MAX-VALUE.[39;49;00m$
  4443^I[33m[39;49;00m$
  4444^I[33mIf REPORTER is a non-numerical reporter, VALUE should be nil.[39;49;00m$
  4445^I[33m[39;49;00m$
  4446^I[33mThis function is relatively inexpensive.  If the change since[39;49;00m$
  4447^I[33mlast update is too small or insufficient time has passed, it does[39;49;00m$
  4448^I[33mnothing.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  4449^I[37m  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mnumberp[39;49;00m[37m [39;49;00m[31mvalue[39;49;00m))[37m      [39;49;00m[37m; For pulsing reporter[39;49;00m[37m[39;49;00m$
  4450^I[37m^I    [39;49;00m([32m>=[39;49;00m[37m [39;49;00m[31mvalue[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mreporter[39;49;00m)))[37m [39;49;00m[37m; For numerical reporter[39;49;00m[37m[39;49;00m$
  4451^I[37m    [39;49;00m([31mprogress-reporter-do-update[39;49;00m[37m [39;49;00m[31mreporter[39;49;00m[37m [39;49;00m[31mvalue[39;49;00m)))[37m[39;49;00m$
  4452^I[37m[39;49;00m$
  4453^I([36mdefun[39;49;00m[37m [39;49;00m[31mmake-progress-reporter[39;49;00m[37m [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mmin-value[39;49;00m[37m [39;49;00m[31mmax-value[39;49;00m[37m[39;49;00m$
  4454^I[37m^I^I^I^I       [39;49;00m[31mcurrent-value[39;49;00m[37m [39;49;00m[31mmin-change[39;49;00m[37m [39;49;00m[31mmin-time[39;49;00m)[37m[39;49;00m$
  4455^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn progress reporter object for use with [39;49;00m[33m`progress-reporter-update'[39;49;00m[33m.[39;49;00m$
  4456^I[33m[39;49;00m$
  4457^I[33mMESSAGE is shown in the echo area, with a status indicator[39;49;00m$
  4458^I[33mappended to the end.  When you call [39;49;00m[33m`progress-reporter-done'[39;49;00m[33m, the[39;49;00m$
  4459^I[33mword [39;49;00m[33m\"[39;49;00m[33mdone[39;49;00m[33m\"[39;49;00m[33m is printed after the MESSAGE.  You can change the[39;49;00m$
  4460^I[33mMESSAGE of an existing progress reporter by calling[39;49;00m$
  4461^I[33m`progress-reporter-force-update'[39;49;00m[33m.[39;49;00m$
  4462^I[33m[39;49;00m$
  4463^I[33mMIN-VALUE and MAX-VALUE, if non-nil, are starting (0% complete)[39;49;00m$
  4464^I[33mand final (100% complete) states of operation; the latter should[39;49;00m$
  4465^I[33mbe larger.  In this case, the status message shows the percentage[39;49;00m$
  4466^I[33mprogress.[39;49;00m$
  4467^I[33m[39;49;00m$
  4468^I[33mIf MIN-VALUE and/or MAX-VALUE is omitted or nil, the status[39;49;00m$
  4469^I[33mmessage shows a [39;49;00m[33m\"[39;49;00m[33mspinning[39;49;00m[33m\"[39;49;00m[33m, non-numeric indicator.[39;49;00m$
  4470^I[33m[39;49;00m$
  4471^I[33mOptional CURRENT-VALUE is the initial progress; the default is[39;49;00m$
  4472^I[33mMIN-VALUE.[39;49;00m$
  4473^I[33mOptional MIN-CHANGE is the minimal change in percents to report;[39;49;00m$
  4474^I[33mthe default is 1%.[39;49;00m$
  4475^I[33mCURRENT-VALUE and MIN-CHANGE do not have any effect if MIN-VALUE[39;49;00m$
  4476^I[33mand/or MAX-VALUE are nil.[39;49;00m$
  4477^I[33m[39;49;00m$
  4478^I[33mOptional MIN-TIME specifies the minimum interval time between[39;49;00m$
  4479^I[33mecho area updates (default is 0.2 seconds.)  If the function[39;49;00m$
  4480^I[33m`float-time'[39;49;00m[33m is not present, time is not tracked at all.  If the[39;49;00m$
  4481^I[33mOS is not capable of measuring fractions of seconds, this[39;49;00m$
  4482^I[33mparameter is effectively rounded up.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  4483^I[37m  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m[[:alnum:]][39;49;00m[33m\\[39;49;00m[33m'[39;49;00m[33m"[39;49;00m[37m [39;49;00m[32mmessage[39;49;00m)[37m[39;49;00m$
  4484^I[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[32mmessage[39;49;00m[37m [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[32mmessage[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m...[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
  4485^I[37m  [39;49;00m([36munless[39;49;00m[37m [39;49;00m[31mmin-time[39;49;00m[37m[39;49;00m$
  4486^I[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mmin-time[39;49;00m[37m [39;49;00m[34m0.2[39;49;00m))[37m[39;49;00m$
  4487^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mreporter[39;49;00m[37m[39;49;00m$
  4488^I[37m^I [39;49;00m[37m;; Force a call to `message' now[39;49;00m[37m[39;49;00m$
  4489^I[37m^I [39;49;00m([32mcons[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mmin-value[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  4490^I[37m^I       [39;49;00m([32mvector[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mfboundp[39;49;00m[37m [39;49;00m[33m'float-time[39;49;00m)[37m[39;49;00m$
  4491^I[37m^I^I^I^I[39;49;00m([32m>=[39;49;00m[37m [39;49;00m[31mmin-time[39;49;00m[37m [39;49;00m[34m0.02[39;49;00m))[37m[39;49;00m$
  4492^I[37m^I^I^I   [39;49;00m([32mfloat-time[39;49;00m)[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
  4493^I[37m^I^I       [39;49;00m[31mmin-value[39;49;00m[37m[39;49;00m$
  4494^I[37m^I^I       [39;49;00m[31mmax-value[39;49;00m[37m[39;49;00m$
  4495^I[37m^I^I       [39;49;00m[32mmessage[39;49;00m[37m[39;49;00m$
  4496^I[37m^I^I       [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mmin-change[39;49;00m[37m [39;49;00m([32mmax[39;49;00m[37m [39;49;00m([32mmin[39;49;00m[37m [39;49;00m[31mmin-change[39;49;00m[37m [39;49;00m[34m50[39;49;00m)[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m[34m1[39;49;00m)[37m[39;49;00m$
  4497^I[37m^I^I       [39;49;00m[31mmin-time[39;49;00m))))[37m[39;49;00m$
  4498^I[37m    [39;49;00m([31mprogress-reporter-update[39;49;00m[37m [39;49;00m[31mreporter[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mcurrent-value[39;49;00m[37m [39;49;00m[31mmin-value[39;49;00m))[37m[39;49;00m$
  4499^I[37m    [39;49;00m[31mreporter[39;49;00m))[37m[39;49;00m$
  4500^I[37m[39;49;00m$
  4501^I([36mdefun[39;49;00m[37m [39;49;00m[31mprogress-reporter-force-update[39;49;00m[37m [39;49;00m([31mreporter[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mvalue[39;49;00m[37m [39;49;00m[31mnew-message[39;49;00m)[37m[39;49;00m$
  4502^I[37m  [39;49;00m[33m"[39;49;00m[33mReport progress of an operation in the echo area unconditionally.[39;49;00m$
  4503^I[33m[39;49;00m$
  4504^I[33mThe first two arguments are the same as in [39;49;00m[33m`progress-reporter-update'[39;49;00m[33m.[39;49;00m$
  4505^I[33mNEW-MESSAGE, if non-nil, sets a new message for the reporter.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  4506^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mparameters[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mreporter[39;49;00m)))[37m[39;49;00m$
  4507^I[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31mnew-message[39;49;00m[37m[39;49;00m$
  4508^I[37m      [39;49;00m([32maset[39;49;00m[37m [39;49;00m[31mparameters[39;49;00m[37m [39;49;00m[34m3[39;49;00m[37m [39;49;00m[31mnew-message[39;49;00m))[37m[39;49;00m$
  4509^I[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32maref[39;49;00m[37m [39;49;00m[31mparameters[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  4510^I[37m      [39;49;00m([32maset[39;49;00m[37m [39;49;00m[31mparameters[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m([32mfloat-time[39;49;00m)))[37m[39;49;00m$
  4511^I[37m    [39;49;00m([31mprogress-reporter-do-update[39;49;00m[37m [39;49;00m[31mreporter[39;49;00m[37m [39;49;00m[31mvalue[39;49;00m)))[37m[39;49;00m$
  4512^I[37m[39;49;00m$
  4513^I([34mdefvar[39;49;00m[37m [39;49;00m[31mprogress-reporter--pulse-characters[39;49;00m[37m [39;49;00m[[33m"[39;49;00m[33m-[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m|[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m/[39;49;00m[33m"[39;49;00m][37m[39;49;00m$
  4514^I[37m  [39;49;00m[33m"[39;49;00m[33mCharacters to use for pulsing progress reporters.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  4515^I[37m[39;49;00m$
  4516^I([36mdefun[39;49;00m[37m [39;49;00m[31mprogress-reporter-do-update[39;49;00m[37m [39;49;00m([31mreporter[39;49;00m[37m [39;49;00m[31mvalue[39;49;00m)[37m[39;49;00m$
  4517^I[37m  [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mparameters[39;49;00m[37m   [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mreporter[39;49;00m))[37m[39;49;00m$
  4518^I[37m^I [39;49;00m([31mupdate-time[39;49;00m[37m  [39;49;00m([32maref[39;49;00m[37m [39;49;00m[31mparameters[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m$
  4519^I[37m^I [39;49;00m([31mmin-value[39;49;00m[37m    [39;49;00m([32maref[39;49;00m[37m [39;49;00m[31mparameters[39;49;00m[37m [39;49;00m[34m1[39;49;00m))[37m[39;49;00m$
  4520^I[37m^I [39;49;00m([31mmax-value[39;49;00m[37m    [39;49;00m([32maref[39;49;00m[37m [39;49;00m[31mparameters[39;49;00m[37m [39;49;00m[34m2[39;49;00m))[37m[39;49;00m$
  4521^I[37m^I [39;49;00m([31mtext[39;49;00m[37m         [39;49;00m([32maref[39;49;00m[37m [39;49;00m[31mparameters[39;49;00m[37m [39;49;00m[34m3[39;49;00m))[37m[39;49;00m$
  4522^I[37m^I [39;49;00m([31menough-time-passed[39;49;00m[37m[39;49;00m$
  4523^I[37m^I  [39;49;00m[37m;; See if enough time has passed since the last update.[39;49;00m[37m[39;49;00m$
  4524^I[37m^I  [39;49;00m([34mor[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m[31mupdate-time[39;49;00m)[37m[39;49;00m$
  4525^I[37m^I      [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32m>=[39;49;00m[37m [39;49;00m([32mfloat-time[39;49;00m)[37m [39;49;00m[31mupdate-time[39;49;00m)[37m[39;49;00m$
  4526^I[37m^I^I[39;49;00m[37m;; Calculate time for the next update[39;49;00m[37m[39;49;00m$
  4527^I[37m^I^I[39;49;00m([32maset[39;49;00m[37m [39;49;00m[31mparameters[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m([32m+[39;49;00m[37m [39;49;00m[31mupdate-time[39;49;00m[37m [39;49;00m([32maref[39;49;00m[37m [39;49;00m[31mparameters[39;49;00m[37m [39;49;00m[34m5[39;49;00m)))))))[37m[39;49;00m$
  4528^I[37m    [39;49;00m([34mcond[39;49;00m[37m [39;49;00m(([34mand[39;49;00m[37m [39;49;00m[31mmin-value[39;49;00m[37m [39;49;00m[31mmax-value[39;49;00m)[37m[39;49;00m$
  4529^I[37m^I   [39;49;00m[37m;; Numerical indicator[39;49;00m[37m[39;49;00m$
  4530^I[37m^I   [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mone-percent[39;49;00m[37m [39;49;00m([32m/[39;49;00m[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m[31mmax-value[39;49;00m[37m [39;49;00m[31mmin-value[39;49;00m)[37m [39;49;00m[34m100.0[39;49;00m))[37m[39;49;00m$
  4531^I[37m^I^I  [39;49;00m([31mpercentage[39;49;00m[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32m=[39;49;00m[37m [39;49;00m[31mmax-value[39;49;00m[37m [39;49;00m[31mmin-value[39;49;00m)[37m[39;49;00m$
  4532^I[37m^I^I^I^I   [39;49;00m[34m0[39;49;00m[37m[39;49;00m$
  4533^I[37m^I^I^I^I [39;49;00m([32mtruncate[39;49;00m[37m [39;49;00m([32m/[39;49;00m[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m[31mvalue[39;49;00m[37m [39;49;00m[31mmin-value[39;49;00m)[37m[39;49;00m$
  4534^I[37m^I^I^I^I^I      [39;49;00m[31mone-percent[39;49;00m)))))[37m[39;49;00m$
  4535^I[37m^I     [39;49;00m[37m;; Calculate NEXT-UPDATE-VALUE.  If we are not printing[39;49;00m[37m[39;49;00m$
  4536^I[37m^I     [39;49;00m[37m;; message because not enough time has passed, use 1[39;49;00m[37m[39;49;00m$
  4537^I[37m^I     [39;49;00m[37m;; instead of MIN-CHANGE.  This makes delays between echo[39;49;00m[37m[39;49;00m$
  4538^I[37m^I     [39;49;00m[37m;; area updates closer to MIN-TIME.[39;49;00m[37m[39;49;00m$
  4539^I[37m^I     [39;49;00m([32msetcar[39;49;00m[37m [39;49;00m[31mreporter[39;49;00m[37m[39;49;00m$
  4540^I[37m^I^I     [39;49;00m([32mmin[39;49;00m[37m [39;49;00m([32m+[39;49;00m[37m [39;49;00m[31mmin-value[39;49;00m[37m [39;49;00m([32m*[39;49;00m[37m [39;49;00m([32m+[39;49;00m[37m [39;49;00m[31mpercentage[39;49;00m[37m[39;49;00m$
  4541^I[37m^I^I^I^I^I     [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31menough-time-passed[39;49;00m[37m[39;49;00m$
  4542^I[37m^I^I^I^I^I^I [39;49;00m[37m;; MIN-CHANGE[39;49;00m[37m[39;49;00m$
  4543^I[37m^I^I^I^I^I^I [39;49;00m([32maref[39;49;00m[37m [39;49;00m[31mparameters[39;49;00m[37m [39;49;00m[34m4[39;49;00m)[37m[39;49;00m$
  4544^I[37m^I^I^I^I^I       [39;49;00m[34m1[39;49;00m))[37m[39;49;00m$
  4545^I[37m^I^I^I^I^I  [39;49;00m[31mone-percent[39;49;00m))[37m[39;49;00m$
  4546^I[37m^I^I^I  [39;49;00m[31mmax-value[39;49;00m))[37m[39;49;00m$
  4547^I[37m^I     [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mintegerp[39;49;00m[37m [39;49;00m[31mvalue[39;49;00m)[37m[39;49;00m$
  4548^I[37m^I       [39;49;00m([32msetcar[39;49;00m[37m [39;49;00m[31mreporter[39;49;00m[37m [39;49;00m([32mceiling[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mreporter[39;49;00m))))[37m[39;49;00m$
  4549^I[37m^I     [39;49;00m[37m;; Only print message if enough time has passed[39;49;00m[37m[39;49;00m$
  4550^I[37m^I     [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31menough-time-passed[39;49;00m[37m[39;49;00m$
  4551^I[37m^I       [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m[31mpercentage[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  4552^I[37m^I^I   [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m%s%d%%[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mtext[39;49;00m[37m [39;49;00m[31mpercentage[39;49;00m)[37m[39;49;00m$
  4553^I[37m^I^I [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m%s[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mtext[39;49;00m)))))[37m[39;49;00m$
  4554^I[37m^I  [39;49;00m[37m;; Pulsing indicator[39;49;00m[37m[39;49;00m$
  4555^I[37m^I  [39;49;00m([31menough-time-passed[39;49;00m[37m[39;49;00m$
  4556^I[37m^I   [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mindex[39;49;00m[37m [39;49;00m([32mmod[39;49;00m[37m [39;49;00m([32m1+[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mreporter[39;49;00m))[37m [39;49;00m[34m4[39;49;00m))[37m[39;49;00m$
  4557^I[37m^I^I [39;49;00m([31mmessage-log-max[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m$
  4558^I[37m^I     [39;49;00m([32msetcar[39;49;00m[37m [39;49;00m[31mreporter[39;49;00m[37m [39;49;00m[31mindex[39;49;00m)[37m[39;49;00m$
  4559^I[37m^I     [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m%s %s[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  4560^I[37m^I^I      [39;49;00m[31mtext[39;49;00m[37m[39;49;00m$
  4561^I[37m^I^I      [39;49;00m([32maref[39;49;00m[37m [39;49;00m[31mprogress-reporter--pulse-characters[39;49;00m[37m[39;49;00m$
  4562^I[37m^I^I^I    [39;49;00m[31mindex[39;49;00m)))))))[37m[39;49;00m$
  4563^I[37m[39;49;00m$
  4564^I([36mdefun[39;49;00m[37m [39;49;00m[31mprogress-reporter-done[39;49;00m[37m [39;49;00m([31mreporter[39;49;00m)[37m[39;49;00m$
  4565^I[37m  [39;49;00m[33m"[39;49;00m[33mPrint reporter's message followed by word [39;49;00m[33m\"[39;49;00m[33mdone[39;49;00m[33m\"[39;49;00m[33m in echo area.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  4566^I[37m  [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m%sdone[39;49;00m[33m"[39;49;00m[37m [39;49;00m([32maref[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mreporter[39;49;00m)[37m [39;49;00m[34m3[39;49;00m)))[37m[39;49;00m$
  4567^I[37m[39;49;00m$
  4568^I([36mdefmacro[39;49;00m[37m [39;49;00m[36mdotimes-with-progress-reporter[39;49;00m[37m [39;49;00m([31mspec[39;49;00m[37m [39;49;00m[32mmessage[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
  4569^I[37m  [39;49;00m[33m"[39;49;00m[33mLoop a certain number of times and report progress in the echo area.[39;49;00m$
  4570^I[33mEvaluate BODY with VAR bound to successive integers running from[39;49;00m$
  4571^I[33m0, inclusive, to COUNT, exclusive.  Then evaluate RESULT to get[39;49;00m$
  4572^I[33mthe return value (nil if RESULT is omitted).[39;49;00m$
  4573^I[33m[39;49;00m$
  4574^I[33mAt each iteration MESSAGE followed by progress percentage is[39;49;00m$
  4575^I[33mprinted in the echo area.  After the loop is finished, MESSAGE[39;49;00m$
  4576^I[33mfollowed by word [39;49;00m[33m\"[39;49;00m[33mdone[39;49;00m[33m\"[39;49;00m[33m is printed.  This macro is a[39;49;00m$
  4577^I[33mconvenience wrapper around [39;49;00m[33m`make-progress-reporter'[39;49;00m[33m and friends.[39;49;00m$
  4578^I[33m[39;49;00m$
  4579^I[33m\([39;49;00m[33mfn (VAR COUNT [RESULT]) MESSAGE BODY...)[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  4580^I[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m2[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m(([32msymbolp[39;49;00m[37m [39;49;00m[31mform[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mform[39;49;00m)[37m [39;49;00m[31mform[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)))[37m[39;49;00m$
  4581^I[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtemp[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m--dotimes-temp--[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
  4582^I[37m^I[39;49;00m([31mtemp2[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m--dotimes-temp2--[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
  4583^I[37m^I[39;49;00m([31mstart[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  4584^I[37m^I[39;49;00m([31mend[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)))[37m[39;49;00m$
  4585^I[37m    [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m((,[31mtemp[39;49;00m[37m [39;49;00m,[31mend[39;49;00m)[37m[39;49;00m$
  4586^I[37m^I   [39;49;00m(,([32mcar[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)[37m [39;49;00m,[31mstart[39;49;00m)[37m[39;49;00m$
  4587^I[37m^I   [39;49;00m(,[31mtemp2[39;49;00m[37m [39;49;00m([31mmake-progress-reporter[39;49;00m[37m [39;49;00m,[32mmessage[39;49;00m[37m [39;49;00m,[31mstart[39;49;00m[37m [39;49;00m,[31mend[39;49;00m)))[37m[39;49;00m$
  4588^I[37m       [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m,([32mcar[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)[37m [39;49;00m,[31mtemp[39;49;00m)[37m[39;49;00m$
  4589^I[37m^I [39;49;00m,@[31mbody[39;49;00m[37m[39;49;00m$
  4590^I[37m^I [39;49;00m([31mprogress-reporter-update[39;49;00m[37m [39;49;00m,[31mtemp2[39;49;00m[37m[39;49;00m$
  4591^I[37m^I^I^I^I   [39;49;00m([34msetq[39;49;00m[37m [39;49;00m,([32mcar[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)[37m [39;49;00m([32m1+[39;49;00m[37m [39;49;00m,([32mcar[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)))))[37m[39;49;00m$
  4592^I[37m       [39;49;00m([31mprogress-reporter-done[39;49;00m[37m [39;49;00m,[31mtemp2[39;49;00m)[37m[39;49;00m$
  4593^I[37m       [39;49;00m[31mnil[39;49;00m[37m [39;49;00m,@([32mcdr[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)))))[37m[39;49;00m$
  4594^I[37m[39;49;00m$
  4595^I[37m[39;49;00m[37m[39;49;00m$
  4596^I[37m;;;; Comparing version strings.[39;49;00m[37m[39;49;00m$
  4597^I[37m[39;49;00m$
  4598^I([34mdefconst[39;49;00m[37m [39;49;00m[31mversion-separator[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  4599^I[37m  [39;49;00m[33m"[39;49;00m[33mSpecify the string used to separate the version elements.[39;49;00m$
  4600^I[33m[39;49;00m$
  4601^I[33mUsually the separator is [39;49;00m[33m\"[39;49;00m[33m.[39;49;00m[33m\"[39;49;00m[33m, but it can be any other string.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  4602^I[37m[39;49;00m$
  4603^I[37m[39;49;00m$
  4604^I([34mdefconst[39;49;00m[37m [39;49;00m[31mversion-regexp-alist[39;49;00m[37m[39;49;00m$
  4605^I[37m  [39;49;00m'(([33m"[39;49;00m[33m^[-_+ ]?snapshot$[39;49;00m[33m"[39;49;00m[37m                                 [39;49;00m.[37m [39;49;00m[34m-4[39;49;00m)[37m[39;49;00m$
  4606^I[37m    [39;49;00m[37m;; treat "1.2.3-20050920" and "1.2-3" as snapshot releases[39;49;00m[37m[39;49;00m$
  4607^I[37m    [39;49;00m([33m"[39;49;00m[33m^[-_+]$[39;49;00m[33m"[39;49;00m[37m                                           [39;49;00m.[37m [39;49;00m[34m-4[39;49;00m)[37m[39;49;00m$
  4608^I[37m    [39;49;00m[37m;; treat "1.2.3-CVS" as snapshot release[39;49;00m[37m[39;49;00m$
  4609^I[37m    [39;49;00m([33m"[39;49;00m[33m^[-_+ ]?[39;49;00m[33m\\[39;49;00m[33m(cvs[39;49;00m[33m\\[39;49;00m[33m|git[39;49;00m[33m\\[39;49;00m[33m|bzr[39;49;00m[33m\\[39;49;00m[33m|svn[39;49;00m[33m\\[39;49;00m[33m|hg[39;49;00m[33m\\[39;49;00m[33m|darcs[39;49;00m[33m\\[39;49;00m[33m)$[39;49;00m[33m"[39;49;00m[37m [39;49;00m.[37m [39;49;00m[34m-4[39;49;00m)[37m[39;49;00m$
  4610^I[37m    [39;49;00m([33m"[39;49;00m[33m^[-_+ ]?alpha$[39;49;00m[33m"[39;49;00m[37m                                    [39;49;00m.[37m [39;49;00m[34m-3[39;49;00m)[37m[39;49;00m$
  4611^I[37m    [39;49;00m([33m"[39;49;00m[33m^[-_+ ]?beta$[39;49;00m[33m"[39;49;00m[37m                                     [39;49;00m.[37m [39;49;00m[34m-2[39;49;00m)[37m[39;49;00m$
  4612^I[37m    [39;49;00m([33m"[39;49;00m[33m^[-_+ ]?[39;49;00m[33m\\[39;49;00m[33m(pre[39;49;00m[33m\\[39;49;00m[33m|rc[39;49;00m[33m\\[39;49;00m[33m)$[39;49;00m[33m"[39;49;00m[37m                           [39;49;00m.[37m [39;49;00m[34m-1[39;49;00m))[37m[39;49;00m$
  4613^I[37m  [39;49;00m[33m"[39;49;00m[33mSpecify association between non-numeric version and its priority.[39;49;00m$
  4614^I[33m[39;49;00m$
  4615^I[33mThis association is used to handle version string like [39;49;00m[33m\"[39;49;00m[33m1.0pre2[39;49;00m[33m\"[39;49;00m[33m,[39;49;00m$
  4616^I[33m\"[39;49;00m[33m0.9alpha1[39;49;00m[33m\"[39;49;00m[33m, etc.  It's used by [39;49;00m[33m`version-to-list'[39;49;00m[33m (which see) to convert the[39;49;00m$
  4617^I[33mnon-numeric part of a version string to an integer.  For example:[39;49;00m$
  4618^I[33m[39;49;00m$
  4619^I[33m   String Version    Integer List Version[39;49;00m$
  4620^I[33m   [39;49;00m[33m\"[39;49;00m[33m0.9snapshot[39;49;00m[33m\"[39;49;00m[33m     (0  9 -4)[39;49;00m$
  4621^I[33m   [39;49;00m[33m\"[39;49;00m[33m1.0-git[39;49;00m[33m\"[39;49;00m[33m         (1  0 -4)[39;49;00m$
  4622^I[33m   [39;49;00m[33m\"[39;49;00m[33m1.0pre2[39;49;00m[33m\"[39;49;00m[33m         (1  0 -1 2)[39;49;00m$
  4623^I[33m   [39;49;00m[33m\"[39;49;00m[33m1.0PRE2[39;49;00m[33m\"[39;49;00m[33m         (1  0 -1 2)[39;49;00m$
  4624^I[33m   [39;49;00m[33m\"[39;49;00m[33m22.8beta3[39;49;00m[33m\"[39;49;00m[33m       (22 8 -2 3)[39;49;00m$
  4625^I[33m   [39;49;00m[33m\"[39;49;00m[33m22.8 Beta3[39;49;00m[33m\"[39;49;00m[33m      (22 8 -2 3)[39;49;00m$
  4626^I[33m   [39;49;00m[33m\"[39;49;00m[33m0.9alpha1[39;49;00m[33m\"[39;49;00m[33m       (0  9 -3 1)[39;49;00m$
  4627^I[33m   [39;49;00m[33m\"[39;49;00m[33m0.9AlphA1[39;49;00m[33m\"[39;49;00m[33m       (0  9 -3 1)[39;49;00m$
  4628^I[33m   [39;49;00m[33m\"[39;49;00m[33m0.9 alpha[39;49;00m[33m\"[39;49;00m[33m       (0  9 -3)[39;49;00m$
  4629^I[33m[39;49;00m$
  4630^I[33mEach element has the following form:[39;49;00m$
  4631^I[33m[39;49;00m$
  4632^I[33m   (REGEXP . PRIORITY)[39;49;00m$
  4633^I[33m[39;49;00m$
  4634^I[33mWhere:[39;49;00m$
  4635^I[33m[39;49;00m$
  4636^I[33mREGEXP^I^Iregexp used to match non-numeric part of a version string.[39;49;00m$
  4637^I[33m^I^IIt should begin with the [39;49;00m[33m`^'[39;49;00m[33m anchor and end with a [39;49;00m[33m`$'[39;49;00m[33m to[39;49;00m$
  4638^I[33m^I^Iprevent false hits.  Letter-case is ignored while matching[39;49;00m$
  4639^I[33m^I^IREGEXP.[39;49;00m$
  4640^I[33m[39;49;00m$
  4641^I[33mPRIORITY^Ia negative integer specifying non-numeric priority of REGEXP.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  4642^I[37m[39;49;00m$
  4643^I[37m[39;49;00m$
  4644^I([36mdefun[39;49;00m[37m [39;49;00m[31mversion-to-list[39;49;00m[37m [39;49;00m([31mver[39;49;00m)[37m[39;49;00m$
  4645^I[37m  [39;49;00m[33m"[39;49;00m[33mConvert version string VER into a list of integers.[39;49;00m$
  4646^I[33m[39;49;00m$
  4647^I[33mThe version syntax is given by the following EBNF:[39;49;00m$
  4648^I[33m[39;49;00m$
  4649^I[33m   VERSION ::= NUMBER ( SEPARATOR NUMBER )*.[39;49;00m$
  4650^I[33m[39;49;00m$
  4651^I[33m   NUMBER ::= (0|1|2|3|4|5|6|7|8|9)+.[39;49;00m$
  4652^I[33m[39;49;00m$
  4653^I[33m   SEPARATOR ::= [39;49;00m[33m`version-separator'[39;49;00m[33m (which see)[39;49;00m$
  4654^I[33m^I       | [39;49;00m[33m`version-regexp-alist'[39;49;00m[33m (which see).[39;49;00m$
  4655^I[33m[39;49;00m$
  4656^I[33mThe NUMBER part is optional if SEPARATOR is a match for an element[39;49;00m$
  4657^I[33min [39;49;00m[33m`version-regexp-alist'[39;49;00m[33m.[39;49;00m$
  4658^I[33m[39;49;00m$
  4659^I[33mExamples of valid version syntax:[39;49;00m$
  4660^I[33m[39;49;00m$
  4661^I[33m   1.0pre2   1.0.7.5   22.8beta3   0.9alpha1   6.9.30Beta[39;49;00m$
  4662^I[33m[39;49;00m$
  4663^I[33mExamples of invalid version syntax:[39;49;00m$
  4664^I[33m[39;49;00m$
  4665^I[33m   1.0prepre2   1.0..7.5   22.8X3   alpha3.2   .5[39;49;00m$
  4666^I[33m[39;49;00m$
  4667^I[33mExamples of version conversion:[39;49;00m$
  4668^I[33m[39;49;00m$
  4669^I[33m   Version String    Version as a List of Integers[39;49;00m$
  4670^I[33m   [39;49;00m[33m\"[39;49;00m[33m1.0.7.5[39;49;00m[33m\"[39;49;00m[33m         (1  0  7 5)[39;49;00m$
  4671^I[33m   [39;49;00m[33m\"[39;49;00m[33m1.0pre2[39;49;00m[33m\"[39;49;00m[33m         (1  0 -1 2)[39;49;00m$
  4672^I[33m   [39;49;00m[33m\"[39;49;00m[33m1.0PRE2[39;49;00m[33m\"[39;49;00m[33m         (1  0 -1 2)[39;49;00m$
  4673^I[33m   [39;49;00m[33m\"[39;49;00m[33m22.8beta3[39;49;00m[33m\"[39;49;00m[33m       (22 8 -2 3)[39;49;00m$
  4674^I[33m   [39;49;00m[33m\"[39;49;00m[33m22.8Beta3[39;49;00m[33m\"[39;49;00m[33m       (22 8 -2 3)[39;49;00m$
  4675^I[33m   [39;49;00m[33m\"[39;49;00m[33m0.9alpha1[39;49;00m[33m\"[39;49;00m[33m       (0  9 -3 1)[39;49;00m$
  4676^I[33m   [39;49;00m[33m\"[39;49;00m[33m0.9AlphA1[39;49;00m[33m\"[39;49;00m[33m       (0  9 -3 1)[39;49;00m$
  4677^I[33m   [39;49;00m[33m\"[39;49;00m[33m0.9alpha[39;49;00m[33m\"[39;49;00m[33m        (0  9 -3)[39;49;00m$
  4678^I[33m   [39;49;00m[33m\"[39;49;00m[33m0.9snapshot[39;49;00m[33m\"[39;49;00m[33m     (0  9 -4)[39;49;00m$
  4679^I[33m   [39;49;00m[33m\"[39;49;00m[33m1.0-git[39;49;00m[33m\"[39;49;00m[33m         (1  0 -4)[39;49;00m$
  4680^I[33m[39;49;00m$
  4681^I[33mSee documentation for [39;49;00m[33m`version-separator'[39;49;00m[33m and [39;49;00m[33m`version-regexp-alist'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  4682^I[37m  [39;49;00m([34mor[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m[31mver[39;49;00m)[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31mver[39;49;00m)[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m$
  4683^I[37m      [39;49;00m([36merror[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mInvalid version string: '%s'[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mver[39;49;00m))[37m[39;49;00m$
  4684^I[37m  [39;49;00m[37m;; Change .x.y to 0.x.y[39;49;00m[37m[39;49;00m$
  4685^I[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32m>=[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31mver[39;49;00m)[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31mversion-separator[39;49;00m))[37m[39;49;00m$
  4686^I[37m^I   [39;49;00m([32mstring-equal[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[31mver[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31mversion-separator[39;49;00m))[37m[39;49;00m$
  4687^I[37m^I^I^I [39;49;00m[31mversion-separator[39;49;00m))[37m[39;49;00m$
  4688^I[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mver[39;49;00m[37m [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m0[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mver[39;49;00m)))[37m[39;49;00m$
  4689^I[37m  [39;49;00m([36msave-match-data[39;49;00m[37m[39;49;00m$
  4690^I[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mi[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  4691^I[37m^I  [39;49;00m([31mcase-fold-search[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m^I^I[39;49;00m[37m; ignore case in matching[39;49;00m[37m[39;49;00m$
  4692^I[37m^I  [39;49;00m[31mlst[39;49;00m[37m [39;49;00m[31ms[39;49;00m[37m [39;49;00m[31mal[39;49;00m)[37m[39;49;00m$
  4693^I[37m      [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31ms[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m[0-9]+[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mver[39;49;00m[37m [39;49;00m[31mi[39;49;00m))[37m[39;49;00m$
  4694^I[37m^I^I  [39;49;00m([32m=[39;49;00m[37m [39;49;00m[31ms[39;49;00m[37m [39;49;00m[31mi[39;49;00m))[37m[39;49;00m$
  4695^I[37m^I[39;49;00m[37m;; handle numeric part[39;49;00m[37m[39;49;00m$
  4696^I[37m^I[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mlst[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m([32mstring-to-number[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[31mver[39;49;00m[37m [39;49;00m[31mi[39;49;00m[37m [39;49;00m([32mmatch-end[39;49;00m[37m [39;49;00m[34m0[39;49;00m)))[37m[39;49;00m$
  4697^I[37m^I^I^I[39;49;00m[31mlst[39;49;00m)[37m[39;49;00m$
  4698^I[37m^I      [39;49;00m[31mi[39;49;00m[37m   [39;49;00m([32mmatch-end[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m$
  4699^I[37m^I[39;49;00m[37m;; handle non-numeric part[39;49;00m[37m[39;49;00m$
  4700^I[37m^I[39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31ms[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m[^0-9]+[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mver[39;49;00m[37m [39;49;00m[31mi[39;49;00m))[37m[39;49;00m$
  4701^I[37m^I^I   [39;49;00m([32m=[39;49;00m[37m [39;49;00m[31ms[39;49;00m[37m [39;49;00m[31mi[39;49;00m))[37m[39;49;00m$
  4702^I[37m^I  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31ms[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[31mver[39;49;00m[37m [39;49;00m[31mi[39;49;00m[37m [39;49;00m([32mmatch-end[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m$
  4703^I[37m^I^I[39;49;00m[31mi[39;49;00m[37m [39;49;00m([32mmatch-end[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m$
  4704^I[37m^I  [39;49;00m[37m;; handle alpha, beta, pre, etc. separator[39;49;00m[37m[39;49;00m$
  4705^I[37m^I  [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32mstring=[39;49;00m[37m [39;49;00m[31ms[39;49;00m[37m [39;49;00m[31mversion-separator[39;49;00m)[37m[39;49;00m$
  4706^I[37m^I    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mal[39;49;00m[37m [39;49;00m[31mversion-regexp-alist[39;49;00m)[37m[39;49;00m$
  4707^I[37m^I    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mal[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m([31mcaar[39;49;00m[37m [39;49;00m[31mal[39;49;00m)[37m [39;49;00m[31ms[39;49;00m)))[37m[39;49;00m$
  4708^I[37m^I      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mal[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mal[39;49;00m)))[37m[39;49;00m$
  4709^I[37m^I    [39;49;00m([34mcond[39;49;00m[37m [39;49;00m([31mal[39;49;00m[37m[39;49;00m$
  4710^I[37m^I^I   [39;49;00m([36mpush[39;49;00m[37m [39;49;00m([31mcdar[39;49;00m[37m [39;49;00m[31mal[39;49;00m)[37m [39;49;00m[31mlst[39;49;00m))[37m[39;49;00m$
  4711^I[37m^I^I  [39;49;00m[37m;; Convert 22.3a to 22.3.1, 22.3b to 22.3.2, etc.[39;49;00m[37m[39;49;00m$
  4712^I[37m^I^I  [39;49;00m(([32mstring-match[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m^[-_+ ]?[39;49;00m[33m\\[39;49;00m[33m([a-zA-Z][39;49;00m[33m\\[39;49;00m[33m)$[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31ms[39;49;00m)[37m[39;49;00m$
  4713^I[37m^I^I   [39;49;00m([36mpush[39;49;00m[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m([32maref[39;49;00m[37m [39;49;00m([32mdowncase[39;49;00m[37m [39;49;00m([31mmatch-string[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31ms[39;49;00m))[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[33m?a[39;49;00m[37m [39;49;00m[34m-1[39;49;00m)[37m[39;49;00m$
  4714^I[37m^I^I^I [39;49;00m[31mlst[39;49;00m))[37m[39;49;00m$
  4715^I[37m^I^I  [39;49;00m([31mt[39;49;00m[37m [39;49;00m([36merror[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mInvalid version syntax: '%s'[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mver[39;49;00m))))))[37m[39;49;00m$
  4716^I[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[31mlst[39;49;00m)[37m[39;49;00m$
  4717^I[37m^I  [39;49;00m([36merror[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mInvalid version syntax: '%s'[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mver[39;49;00m)[37m[39;49;00m$
  4718^I[37m^I[39;49;00m([32mnreverse[39;49;00m[37m [39;49;00m[31mlst[39;49;00m)))))[37m[39;49;00m$
  4719^I[37m[39;49;00m$
  4720^I[37m[39;49;00m$
  4721^I([36mdefun[39;49;00m[37m [39;49;00m[31mversion-list-<[39;49;00m[37m [39;49;00m([31ml1[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)[37m[39;49;00m$
  4722^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn t if L1, a list specification of a version, is lower than L2.[39;49;00m$
  4723^I[33m[39;49;00m$
  4724^I[33mNote that a version specified by the list (1) is equal to (1 0),[39;49;00m$
  4725^I[33m\([39;49;00m[33m1 0 0), (1 0 0 0), etc.  That is, the trailing zeros are insignificant.[39;49;00m$
  4726^I[33mAlso, a version given by the list (1) is higher than (1 -1), which in[39;49;00m$
  4727^I[33mturn is higher than (1 -2), which is higher than (1 -3).[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  4728^I[37m  [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31ml1[39;49;00m[37m [39;49;00m[31ml2[39;49;00m[37m [39;49;00m([32m=[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31ml1[39;49;00m)[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)))[37m[39;49;00m$
  4729^I[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31ml1[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31ml1[39;49;00m)[37m[39;49;00m$
  4730^I[37m^I  [39;49;00m[31ml2[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)))[37m[39;49;00m$
  4731^I[37m  [39;49;00m([34mcond[39;49;00m[37m[39;49;00m$
  4732^I[37m   [39;49;00m[37m;; l1 not null and l2 not null[39;49;00m[37m[39;49;00m$
  4733^I[37m   [39;49;00m(([34mand[39;49;00m[37m [39;49;00m[31ml1[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31ml1[39;49;00m)[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)))[37m[39;49;00m$
  4734^I[37m   [39;49;00m[37m;; l1 null and l2 null         ==> l1 length = l2 length[39;49;00m[37m[39;49;00m$
  4735^I[37m   [39;49;00m(([34mand[39;49;00m[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[31ml1[39;49;00m)[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[31ml2[39;49;00m))[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
  4736^I[37m   [39;49;00m[37m;; l1 not null and l2 null     ==> l1 length > l2 length[39;49;00m[37m[39;49;00m$
  4737^I[37m   [39;49;00m([31ml1[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m([31mversion-list-not-zero[39;49;00m[37m [39;49;00m[31ml1[39;49;00m)[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m$
  4738^I[37m   [39;49;00m[37m;; l1 null and l2 not null     ==> l2 length > l1 length[39;49;00m[37m[39;49;00m$
  4739^I[37m   [39;49;00m([31mt[39;49;00m[37m  [39;49;00m([32m<[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m([31mversion-list-not-zero[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)))))[37m[39;49;00m$
  4740^I[37m[39;49;00m$
  4741^I[37m[39;49;00m$
  4742^I([36mdefun[39;49;00m[37m [39;49;00m[31mversion-list-=[39;49;00m[37m [39;49;00m([31ml1[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)[37m[39;49;00m$
  4743^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn t if L1, a list specification of a version, is equal to L2.[39;49;00m$
  4744^I[33m[39;49;00m$
  4745^I[33mNote that a version specified by the list (1) is equal to (1 0),[39;49;00m$
  4746^I[33m\([39;49;00m[33m1 0 0), (1 0 0 0), etc.  That is, the trailing zeros are insignificant.[39;49;00m$
  4747^I[33mAlso, a version given by the list (1) is higher than (1 -1), which in[39;49;00m$
  4748^I[33mturn is higher than (1 -2), which is higher than (1 -3).[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  4749^I[37m  [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31ml1[39;49;00m[37m [39;49;00m[31ml2[39;49;00m[37m [39;49;00m([32m=[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31ml1[39;49;00m)[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)))[37m[39;49;00m$
  4750^I[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31ml1[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31ml1[39;49;00m)[37m[39;49;00m$
  4751^I[37m^I  [39;49;00m[31ml2[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)))[37m[39;49;00m$
  4752^I[37m  [39;49;00m([34mcond[39;49;00m[37m[39;49;00m$
  4753^I[37m   [39;49;00m[37m;; l1 not null and l2 not null[39;49;00m[37m[39;49;00m$
  4754^I[37m   [39;49;00m(([34mand[39;49;00m[37m [39;49;00m[31ml1[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
  4755^I[37m   [39;49;00m[37m;; l1 null and l2 null     ==> l1 length = l2 length[39;49;00m[37m[39;49;00m$
  4756^I[37m   [39;49;00m(([34mand[39;49;00m[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[31ml1[39;49;00m)[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)))[37m[39;49;00m$
  4757^I[37m   [39;49;00m[37m;; l1 not null and l2 null ==> l1 length > l2 length[39;49;00m[37m[39;49;00m$
  4758^I[37m   [39;49;00m([31ml1[39;49;00m[37m [39;49;00m([31mzerop[39;49;00m[37m [39;49;00m([31mversion-list-not-zero[39;49;00m[37m [39;49;00m[31ml1[39;49;00m)))[37m[39;49;00m$
  4759^I[37m   [39;49;00m[37m;; l1 null and l2 not null ==> l2 length > l1 length[39;49;00m[37m[39;49;00m$
  4760^I[37m   [39;49;00m([31mt[39;49;00m[37m  [39;49;00m([31mzerop[39;49;00m[37m [39;49;00m([31mversion-list-not-zero[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)))))[37m[39;49;00m$
  4761^I[37m[39;49;00m$
  4762^I[37m[39;49;00m$
  4763^I([36mdefun[39;49;00m[37m [39;49;00m[31mversion-list-<=[39;49;00m[37m [39;49;00m([31ml1[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)[37m[39;49;00m$
  4764^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn t if L1, a list specification of a version, is lower or equal to L2.[39;49;00m$
  4765^I[33m[39;49;00m$
  4766^I[33mNote that integer list (1) is equal to (1 0), (1 0 0), (1 0 0 0),[39;49;00m$
  4767^I[33metc.  That is, the trailing zeroes are insignificant.  Also, integer[39;49;00m$
  4768^I[33mlist (1) is greater than (1 -1) which is greater than (1 -2)[39;49;00m$
  4769^I[33mwhich is greater than (1 -3).[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  4770^I[37m  [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31ml1[39;49;00m[37m [39;49;00m[31ml2[39;49;00m[37m [39;49;00m([32m=[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31ml1[39;49;00m)[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)))[37m[39;49;00m$
  4771^I[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31ml1[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31ml1[39;49;00m)[37m[39;49;00m$
  4772^I[37m^I  [39;49;00m[31ml2[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)))[37m[39;49;00m$
  4773^I[37m  [39;49;00m([34mcond[39;49;00m[37m[39;49;00m$
  4774^I[37m   [39;49;00m[37m;; l1 not null and l2 not null[39;49;00m[37m[39;49;00m$
  4775^I[37m   [39;49;00m(([34mand[39;49;00m[37m [39;49;00m[31ml1[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31ml1[39;49;00m)[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)))[37m[39;49;00m$
  4776^I[37m   [39;49;00m[37m;; l1 null and l2 null     ==> l1 length = l2 length[39;49;00m[37m[39;49;00m$
  4777^I[37m   [39;49;00m(([34mand[39;49;00m[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[31ml1[39;49;00m)[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)))[37m[39;49;00m$
  4778^I[37m   [39;49;00m[37m;; l1 not null and l2 null ==> l1 length > l2 length[39;49;00m[37m[39;49;00m$
  4779^I[37m   [39;49;00m([31ml1[39;49;00m[37m [39;49;00m([32m<=[39;49;00m[37m [39;49;00m([31mversion-list-not-zero[39;49;00m[37m [39;49;00m[31ml1[39;49;00m)[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m$
  4780^I[37m   [39;49;00m[37m;; l1 null and l2 not null ==> l2 length > l1 length[39;49;00m[37m[39;49;00m$
  4781^I[37m   [39;49;00m([31mt[39;49;00m[37m  [39;49;00m([32m<=[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m([31mversion-list-not-zero[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)))))[37m[39;49;00m$
  4782^I[37m[39;49;00m$
  4783^I([36mdefun[39;49;00m[37m [39;49;00m[31mversion-list-not-zero[39;49;00m[37m [39;49;00m([31mlst[39;49;00m)[37m[39;49;00m$
  4784^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn the first non-zero element of LST, which is a list of integers.[39;49;00m$
  4785^I[33m[39;49;00m$
  4786^I[33mIf all LST elements are zeros or LST is nil, return zero.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  4787^I[37m  [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mlst[39;49;00m[37m [39;49;00m([31mzerop[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mlst[39;49;00m)))[37m[39;49;00m$
  4788^I[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mlst[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mlst[39;49;00m)))[37m[39;49;00m$
  4789^I[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mlst[39;49;00m[37m[39;49;00m$
  4790^I[37m      [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mlst[39;49;00m)[37m[39;49;00m$
  4791^I[37m    [39;49;00m[37m;; there is no element different of zero[39;49;00m[37m[39;49;00m$
  4792^I[37m    [39;49;00m[34m0[39;49;00m))[37m[39;49;00m$
  4793^I[37m[39;49;00m$
  4794^I[37m[39;49;00m$
  4795^I([36mdefun[39;49;00m[37m [39;49;00m[31mversion<[39;49;00m[37m [39;49;00m([31mv1[39;49;00m[37m [39;49;00m[31mv2[39;49;00m)[37m[39;49;00m$
  4796^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn t if version V1 is lower (older) than V2.[39;49;00m$
  4797^I[33m[39;49;00m$
  4798^I[33mNote that version string [39;49;00m[33m\"[39;49;00m[33m1[39;49;00m[33m\"[39;49;00m[33m is equal to [39;49;00m[33m\"[39;49;00m[33m1.0[39;49;00m[33m\"[39;49;00m[33m, [39;49;00m[33m\"[39;49;00m[33m1.0.0[39;49;00m[33m\"[39;49;00m[33m, [39;49;00m[33m\"[39;49;00m[33m1.0.0.0[39;49;00m[33m\"[39;49;00m[33m,[39;49;00m$
  4799^I[33metc.  That is, the trailing [39;49;00m[33m\"[39;49;00m[33m.0[39;49;00m[33m\"[39;49;00m[33ms are insignificant.  Also, version[39;49;00m$
  4800^I[33mstring [39;49;00m[33m\"[39;49;00m[33m1[39;49;00m[33m\"[39;49;00m[33m is higher (newer) than [39;49;00m[33m\"[39;49;00m[33m1pre[39;49;00m[33m\"[39;49;00m[33m, which is higher than [39;49;00m[33m\"[39;49;00m[33m1beta[39;49;00m[33m\"[39;49;00m[33m,[39;49;00m$
  4801^I[33mwhich is higher than [39;49;00m[33m\"[39;49;00m[33m1alpha[39;49;00m[33m\"[39;49;00m[33m, which is higher than [39;49;00m[33m\"[39;49;00m[33m1snapshot[39;49;00m[33m\"[39;49;00m[33m.[39;49;00m$
  4802^I[33mAlso, [39;49;00m[33m\"[39;49;00m[33m-GIT[39;49;00m[33m\"[39;49;00m[33m, [39;49;00m[33m\"[39;49;00m[33m-CVS[39;49;00m[33m\"[39;49;00m[33m and [39;49;00m[33m\"[39;49;00m[33m-NNN[39;49;00m[33m\"[39;49;00m[33m are treated as snapshot versions.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  4803^I[37m  [39;49;00m([31mversion-list-<[39;49;00m[37m [39;49;00m([31mversion-to-list[39;49;00m[37m [39;49;00m[31mv1[39;49;00m)[37m [39;49;00m([31mversion-to-list[39;49;00m[37m [39;49;00m[31mv2[39;49;00m)))[37m[39;49;00m$
  4804^I[37m[39;49;00m$
  4805^I([36mdefun[39;49;00m[37m [39;49;00m[31mversion<=[39;49;00m[37m [39;49;00m([31mv1[39;49;00m[37m [39;49;00m[31mv2[39;49;00m)[37m[39;49;00m$
  4806^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn t if version V1 is lower (older) than or equal to V2.[39;49;00m$
  4807^I[33m[39;49;00m$
  4808^I[33mNote that version string [39;49;00m[33m\"[39;49;00m[33m1[39;49;00m[33m\"[39;49;00m[33m is equal to [39;49;00m[33m\"[39;49;00m[33m1.0[39;49;00m[33m\"[39;49;00m[33m, [39;49;00m[33m\"[39;49;00m[33m1.0.0[39;49;00m[33m\"[39;49;00m[33m, [39;49;00m[33m\"[39;49;00m[33m1.0.0.0[39;49;00m[33m\"[39;49;00m[33m,[39;49;00m$
  4809^I[33metc.  That is, the trailing [39;49;00m[33m\"[39;49;00m[33m.0[39;49;00m[33m\"[39;49;00m[33ms are insignificant.  Also, version[39;49;00m$
  4810^I[33mstring [39;49;00m[33m\"[39;49;00m[33m1[39;49;00m[33m\"[39;49;00m[33m is higher (newer) than [39;49;00m[33m\"[39;49;00m[33m1pre[39;49;00m[33m\"[39;49;00m[33m, which is higher than [39;49;00m[33m\"[39;49;00m[33m1beta[39;49;00m[33m\"[39;49;00m[33m,[39;49;00m$
  4811^I[33mwhich is higher than [39;49;00m[33m\"[39;49;00m[33m1alpha[39;49;00m[33m\"[39;49;00m[33m, which is higher than [39;49;00m[33m\"[39;49;00m[33m1snapshot[39;49;00m[33m\"[39;49;00m[33m.[39;49;00m$
  4812^I[33mAlso, [39;49;00m[33m\"[39;49;00m[33m-GIT[39;49;00m[33m\"[39;49;00m[33m, [39;49;00m[33m\"[39;49;00m[33m-CVS[39;49;00m[33m\"[39;49;00m[33m and [39;49;00m[33m\"[39;49;00m[33m-NNN[39;49;00m[33m\"[39;49;00m[33m are treated as snapshot versions.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  4813^I[37m  [39;49;00m([31mversion-list-<=[39;49;00m[37m [39;49;00m([31mversion-to-list[39;49;00m[37m [39;49;00m[31mv1[39;49;00m)[37m [39;49;00m([31mversion-to-list[39;49;00m[37m [39;49;00m[31mv2[39;49;00m)))[37m[39;49;00m$
  4814^I[37m[39;49;00m$
  4815^I([36mdefun[39;49;00m[37m [39;49;00m[31mversion=[39;49;00m[37m [39;49;00m([31mv1[39;49;00m[37m [39;49;00m[31mv2[39;49;00m)[37m[39;49;00m$
  4816^I[37m  [39;49;00m[33m"[39;49;00m[33mReturn t if version V1 is equal to V2.[39;49;00m$
  4817^I[33m[39;49;00m$
  4818^I[33mNote that version string [39;49;00m[33m\"[39;49;00m[33m1[39;49;00m[33m\"[39;49;00m[33m is equal to [39;49;00m[33m\"[39;49;00m[33m1.0[39;49;00m[33m\"[39;49;00m[33m, [39;49;00m[33m\"[39;49;00m[33m1.0.0[39;49;00m[33m\"[39;49;00m[33m, [39;49;00m[33m\"[39;49;00m[33m1.0.0.0[39;49;00m[33m\"[39;49;00m[33m,[39;49;00m$
  4819^I[33metc.  That is, the trailing [39;49;00m[33m\"[39;49;00m[33m.0[39;49;00m[33m\"[39;49;00m[33ms are insignificant.  Also, version[39;49;00m$
  4820^I[33mstring [39;49;00m[33m\"[39;49;00m[33m1[39;49;00m[33m\"[39;49;00m[33m is higher (newer) than [39;49;00m[33m\"[39;49;00m[33m1pre[39;49;00m[33m\"[39;49;00m[33m, which is higher than [39;49;00m[33m\"[39;49;00m[33m1beta[39;49;00m[33m\"[39;49;00m[33m,[39;49;00m$
  4821^I[33mwhich is higher than [39;49;00m[33m\"[39;49;00m[33m1alpha[39;49;00m[33m\"[39;49;00m[33m, which is higher than [39;49;00m[33m\"[39;49;00m[33m1snapshot[39;49;00m[33m\"[39;49;00m[33m.[39;49;00m$
  4822^I[33mAlso, [39;49;00m[33m\"[39;49;00m[33m-GIT[39;49;00m[33m\"[39;49;00m[33m, [39;49;00m[33m\"[39;49;00m[33m-CVS[39;49;00m[33m\"[39;49;00m[33m and [39;49;00m[33m\"[39;49;00m[33m-NNN[39;49;00m[33m\"[39;49;00m[33m are treated as snapshot versions.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  4823^I[37m  [39;49;00m([31mversion-list-=[39;49;00m[37m [39;49;00m([31mversion-to-list[39;49;00m[37m [39;49;00m[31mv1[39;49;00m)[37m [39;49;00m([31mversion-to-list[39;49;00m[37m [39;49;00m[31mv2[39;49;00m)))[37m[39;49;00m$
  4824^I[37m[39;49;00m$
  4825^I([34mdefvar[39;49;00m[37m [39;49;00m[31mpackage--builtin-versions[39;49;00m[37m[39;49;00m$
  4826^I[37m  [39;49;00m[37m;; Mostly populated by loaddefs.el via autoload-builtin-package-versions.[39;49;00m[37m[39;49;00m$
  4827^I[37m  [39;49;00m([32mpurecopy[39;49;00m[37m [39;49;00m`(([31memacs[39;49;00m[37m [39;49;00m.[37m [39;49;00m,([31mversion-to-list[39;49;00m[37m [39;49;00m[31memacs-version[39;49;00m))))[37m[39;49;00m$
  4828^I[37m  [39;49;00m[33m"[39;49;00m[33mAlist giving the version of each versioned builtin package.[39;49;00m$
  4829^I[33mI.e. each element of the list is of the form (NAME . VERSION) where[39;49;00m$
  4830^I[33mNAME is the package name as a symbol, and VERSION is its version[39;49;00m$
  4831^I[33mas a list.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  4832^I[37m[39;49;00m$
  4833^I([36mdefun[39;49;00m[37m [39;49;00m[31mpackage--description-file[39;49;00m[37m [39;49;00m([31mdir[39;49;00m)[37m[39;49;00m$
  4834^I[37m  [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31msubdir[39;49;00m[37m [39;49;00m([32mfile-name-nondirectory[39;49;00m[37m[39;49;00m$
  4835^I[37m                         [39;49;00m([32mdirectory-file-name[39;49;00m[37m [39;49;00m[31mdir[39;49;00m))))[37m[39;49;00m$
  4836^I[37m            [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m([^.].*?[39;49;00m[33m\\[39;49;00m[33m)-[39;49;00m[33m\\[39;49;00m[33m([0-9]+[39;49;00m[33m\\[39;49;00m[33m(?:[.][0-9]+[39;49;00m[33m\\[39;49;00m[33m|[39;49;00m[33m\\[39;49;00m[33m(?:pre[39;49;00m[33m\\[39;49;00m[33m|beta[39;49;00m[33m\\[39;49;00m[33m|alpha[39;49;00m[33m\\[39;49;00m[33m)[0-9]+[39;49;00m[33m\\[39;49;00m[33m)*[39;49;00m[33m\\[39;49;00m[33m)[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31msubdir[39;49;00m)[37m[39;49;00m$
  4837^I[37m                [39;49;00m([31mmatch-string[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31msubdir[39;49;00m)[37m [39;49;00m[31msubdir[39;49;00m))[37m[39;49;00m$
  4838^I[37m          [39;49;00m[33m"[39;49;00m[33m-pkg.el[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
  4839^I[37m[39;49;00m$
  4840^I[37m[39;49;00m[37m[39;49;00m$
  4841^I[37m;;; Misc.[39;49;00m[37m[39;49;00m$
  4842^I([34mdefconst[39;49;00m[37m [39;49;00m[31mmenu-bar-separator[39;49;00m[37m [39;49;00m'([33m"[39;49;00m[33m--[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  4843^I[37m  [39;49;00m[33m"[39;49;00m[33mSeparator for menus.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
  4844^I[37m[39;49;00m$
  4845^I[37m;; The following statement ought to be in print.c, but `provide' can't[39;49;00m[37m[39;49;00m$
  4846^I[37m;; be used there.[39;49;00m[37m[39;49;00m$
  4847^I[37m;; http://lists.gnu.org/archive/html/emacs-devel/2009-08/msg00236.html[39;49;00m[37m[39;49;00m$
  4848^I([36mwhen[39;49;00m[37m [39;49;00m([32mhash-table-p[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m([32mread-from-string[39;49;00m[37m[39;49;00m$
  4849^I[37m^I^I^I  [39;49;00m([32mprin1-to-string[39;49;00m[37m [39;49;00m([32mmake-hash-table[39;49;00m)))))[37m[39;49;00m$
  4850^I[37m  [39;49;00m([36mprovide[39;49;00m[37m [39;49;00m[33m'hashtable-print-readable[39;49;00m))[37m[39;49;00m$
  4851^I[37m[39;49;00m$
  4852^I[37m;; This is used in lisp/Makefile.in and in leim/Makefile.in to[39;49;00m[37m[39;49;00m$
  4853^I[37m;; generate file names for autoloads, custom-deps, and finder-data.[39;49;00m[37m[39;49;00m$
  4854^I([36mdefun[39;49;00m[37m [39;49;00m[31munmsys--file-name[39;49;00m[37m [39;49;00m([31mfile[39;49;00m)[37m[39;49;00m$
  4855^I[37m  [39;49;00m[33m"[39;49;00m[33mProduce the canonical file name for FILE from its MSYS form.[39;49;00m$
  4856^I[33m[39;49;00m$
  4857^I[33mOn systems other than MS-Windows, just returns FILE.[39;49;00m$
  4858^I[33mOn MS-Windows, converts /d/foo/bar form of file names[39;49;00m$
  4859^I[33mpassed by MSYS Make into d:/foo/bar that Emacs can grok.[39;49;00m$
  4860^I[33m[39;49;00m$
  4861^I[33mThis function is called from lisp/Makefile and leim/Makefile.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  4862^I[37m  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31msystem-type[39;49;00m[37m [39;49;00m[33m'windows-nt[39;49;00m)[37m[39;49;00m$
  4863^I[37m^I     [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m`[39;49;00m[33m/[a-zA-Z]/[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mfile[39;49;00m))[37m[39;49;00m$
  4864^I[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mfile[39;49;00m[37m [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[31mfile[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[34m2[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m:[39;49;00m[33m"[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[31mfile[39;49;00m[37m [39;49;00m[34m2[39;49;00m))))[37m[39;49;00m$
  4865^I[37m  [39;49;00m[31mfile[39;49;00m)[37m[39;49;00m$
  4866^I[37m[39;49;00m$
  4867^I[37m[39;49;00m$
  4868^I[37m;;; subr.el ends here[39;49;00m$

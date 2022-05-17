[37m;;; subr.el --- basic lisp subroutines for Emacs  -*- coding: utf-8; lexical-binding:t -*-[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m;; Copyright (C) 1985-1986, 1992, 1994-1995, 1999-2015 Free Software[39;49;00m[37m[39;49;00m$
[37m;; Foundation, Inc.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m;; Maintainer: emacs-devel@gnu.org[39;49;00m[37m[39;49;00m$
[37m;; Keywords: internal[39;49;00m[37m[39;49;00m$
[37m;; Package: emacs[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m;; This file is part of GNU Emacs.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m;; GNU Emacs is free software: you can redistribute it and/or modify[39;49;00m[37m[39;49;00m$
[37m;; it under the terms of the GNU General Public License as published by[39;49;00m[37m[39;49;00m$
[37m;; the Free Software Foundation, either version 3 of the License, or[39;49;00m[37m[39;49;00m$
[37m;; (at your option) any later version.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m;; GNU Emacs is distributed in the hope that it will be useful,[39;49;00m[37m[39;49;00m$
[37m;; but WITHOUT ANY WARRANTY; without even the implied warranty of[39;49;00m[37m[39;49;00m$
[37m;; MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the[39;49;00m[37m[39;49;00m$
[37m;; GNU General Public License for more details.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m;; You should have received a copy of the GNU General Public License[39;49;00m[37m[39;49;00m$
[37m;; along with GNU Emacs.  If not, see <http://www.gnu.org/licenses/>.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m;;; Commentary:[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m;;; Code:[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m;; Beware: while this file has tag `utf-8', before it's compiled, it gets[39;49;00m[37m[39;49;00m$
[37m;; loaded as "raw-text", so non-ASCII chars won't work right during bootstrap.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
([36mdefmacro[39;49;00m[37m [39;49;00m[36mdeclare-function[39;49;00m[37m [39;49;00m([31m_fn[39;49;00m[37m [39;49;00m[31m_file[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31m_arglist[39;49;00m[37m [39;49;00m[31m_fileonly[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mTell the byte-compiler that function FN is defined, in FILE.[39;49;00m$
[33mOptional ARGLIST is the argument list used by the function.[39;49;00m$
[33mThe FILE argument is not used by the byte-compiler, but by the[39;49;00m$
[33m`check-declare'[39;49;00m[33m package, which checks that FILE contains a[39;49;00m$
[33mdefinition for FN.  ARGLIST is used by both the byte-compiler[39;49;00m$
[33mand [39;49;00m[33m`check-declare'[39;49;00m[33m to check for consistency.[39;49;00m$
[33m[39;49;00m$
[33mFILE can be either a Lisp file (in which case the [39;49;00m[33m\"[39;49;00m[33m.el[39;49;00m[33m\"[39;49;00m[33m[39;49;00m$
[33mextension is optional), or a C file.  C files are expanded[39;49;00m$
[33mrelative to the Emacs [39;49;00m[33m\"[39;49;00m[33msrc/[39;49;00m[33m\"[39;49;00m[33m directory.  Lisp files are[39;49;00m$
[33msearched for using [39;49;00m[33m`locate-library'[39;49;00m[33m, and if that fails they are[39;49;00m$
[33mexpanded relative to the location of the file containing the[39;49;00m$
[33mdeclaration.  A FILE with an [39;49;00m[33m\"[39;49;00m[33mext:[39;49;00m[33m\"[39;49;00m[33m prefix is an external file.[39;49;00m$
[33m`check-declare'[39;49;00m[33m will check such files if they are found, and skip[39;49;00m$
[33mthem without error if they are not.[39;49;00m$
[33m[39;49;00m$
[33mFILEONLY non-nil means that [39;49;00m[33m`check-declare'[39;49;00m[33m will only check that[39;49;00m$
[33mFILE exists, not that it defines FN.  This is intended for[39;49;00m$
[33mfunction-definitions that [39;49;00m[33m`check-declare'[39;49;00m[33m does not recognize, e.g.[39;49;00m$
[33m`defstruct'[39;49;00m[33m.[39;49;00m$
[33m[39;49;00m$
[33mTo specify a value for FILEONLY without passing an argument list,[39;49;00m$
[33mset ARGLIST to t.  This is necessary because nil means an[39;49;00m$
[33mempty argument list, rather than an unspecified one.[39;49;00m$
[33m[39;49;00m$
[33mNote that for the purposes of [39;49;00m[33m`check-declare'[39;49;00m[33m, this statement[39;49;00m$
[33mmust be the first non-whitespace on a line.[39;49;00m$
[33m[39;49;00m$
[33mFor more information, see Info node [39;49;00m[33m`[39;49;00m[33m(elisp)Declaring Functions'.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; Does nothing - byte-compile-declare-function does the work.[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m[37m[39;49;00m$
[37m;;;; Basic Lisp macros.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
([36mdefalias[39;49;00m[37m [39;49;00m[33m'not[39;49;00m[37m [39;49;00m[33m'null[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
([36mdefmacro[39;49;00m[37m [39;49;00m[36mnoreturn[39;49;00m[37m [39;49;00m([31mform[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mEvaluate FORM, expecting it not to return.[39;49;00m$
[33mIf FORM does return, signal an error.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m`([34mprog1[39;49;00m[37m [39;49;00m,[31mform[39;49;00m[37m[39;49;00m$
[37m     [39;49;00m([36merror[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mForm marked with [39;49;00m[33m`noreturn'[39;49;00m[33m did return[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefmacro[39;49;00m[37m [39;49;00m[31m1value[39;49;00m[37m [39;49;00m([31mform[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mEvaluate FORM, expecting a constant return value.[39;49;00m$
[33mThis is the global do-nothing version.  There is also [39;49;00m[33m`testcover-1value'[39;49;00m[33m[39;49;00m$
[33mthat complains if FORM ever does return differing values.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m[31mform[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
([36mdefmacro[39;49;00m[37m [39;49;00m[36mdef-edebug-spec[39;49;00m[37m [39;49;00m([31msymbol[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mSet the [39;49;00m[33m`edebug-form-spec'[39;49;00m[33m property of SYMBOL according to SPEC.[39;49;00m$
[33mBoth SYMBOL and SPEC are unevaluated.  The SPEC can be:[39;49;00m$
[33m0 (instrument no arguments); t (instrument all arguments);[39;49;00m$
[33ma symbol (naming a function with an Edebug specification); or a list.[39;49;00m$
[33mThe elements of the list describe the argument types; see[39;49;00m$
[33mInfo node [39;49;00m[33m`[39;49;00m[33m(elisp)Specification List' for details.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m`([32mput[39;49;00m[37m [39;49;00m([34mquote[39;49;00m[37m [39;49;00m,[31msymbol[39;49;00m)[37m [39;49;00m[33m'edebug-form-spec[39;49;00m[37m [39;49;00m([34mquote[39;49;00m[37m [39;49;00m,[31mspec[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefmacro[39;49;00m[37m [39;49;00m[36mlambda[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[32mcdr[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn a lambda expression.[39;49;00m$
[33mA call of the form (lambda ARGS DOCSTRING INTERACTIVE BODY) is[39;49;00m$
[33mself-quoting; the result of evaluating the lambda expression is the[39;49;00m$
[33mexpression itself.  The lambda expression may then be treated as a[39;49;00m$
[33mfunction, i.e., stored as the function value of a symbol, passed to[39;49;00m$
[33m`funcall'[39;49;00m[33m or [39;49;00m[33m`mapcar'[39;49;00m[33m, etc.[39;49;00m$
[33m[39;49;00m$
[33mARGS should take the same form as an argument list for a [39;49;00m[33m`defun'[39;49;00m[33m.[39;49;00m$
[33mDOCSTRING is an optional documentation string.[39;49;00m$
[33m If present, it should describe how to call the function.[39;49;00m$
[33m But documentation strings are usually not useful in nameless functions.[39;49;00m$
[33mINTERACTIVE should be a call to the function [39;49;00m[33m`interactive'[39;49;00m[33m, which see.[39;49;00m$
[33mIt may also be omitted.[39;49;00m$
[33mBODY should be a list of Lisp expressions.[39;49;00m$
[33m[39;49;00m$
[33m\([39;49;00m[33mfn ARGS [DOCSTRING] [INTERACTIVE] BODY)[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdoc-string[39;49;00m[37m [39;49;00m[34m2[39;49;00m)[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[36mdefun[39;49;00m)[37m[39;49;00m$
[37m           [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m([31m&define[39;49;00m[37m [39;49;00m[31mlambda-list[39;49;00m[37m[39;49;00m$
[37m                           [39;49;00m[[34m&optional[39;49;00m[37m [39;49;00m[32mstringp[39;49;00m][37m[39;49;00m$
[37m                           [39;49;00m[[34m&optional[39;49;00m[37m [39;49;00m([33m"[39;49;00m[33minteractive[39;49;00m[33m"[39;49;00m[37m [39;49;00m[34minteractive[39;49;00m)][37m[39;49;00m$
[37m                           [39;49;00m[31mdef-body[39;49;00m)))[37m[39;49;00m$
[37m  [39;49;00m[37m;; Note that this definition should not use backquotes; subr.el should not[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; depend on backquote.el.[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'function[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[33m'lambda[39;49;00m[37m [39;49;00m[32mcdr[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefmacro[39;49;00m[37m [39;49;00m[36msetq-local[39;49;00m[37m [39;49;00m([31mvar[39;49;00m[37m [39;49;00m[31mval[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mSet variable VAR to value VAL in current buffer.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; Can't use backquote here, it's too early in the bootstrap.[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'set[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'make-local-variable[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'quote[39;49;00m[37m [39;49;00m[31mvar[39;49;00m))[37m [39;49;00m[31mval[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefmacro[39;49;00m[37m [39;49;00m[36mdefvar-local[39;49;00m[37m [39;49;00m([31mvar[39;49;00m[37m [39;49;00m[31mval[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mdocstring[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mDefine VAR as a buffer-local variable with default value VAL.[39;49;00m$
[33mLike [39;49;00m[33m`defvar'[39;49;00m[33m but additionally marks the variable as being automatically[39;49;00m$
[33mbuffer-local wherever it is set.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[34mdefvar[39;49;00m)[37m [39;49;00m([31mdoc-string[39;49;00m[37m [39;49;00m[34m3[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m[37m;; Can't use backquote here, it's too early in the bootstrap.[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'progn[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'defvar[39;49;00m[37m [39;49;00m[31mvar[39;49;00m[37m [39;49;00m[31mval[39;49;00m[37m [39;49;00m[31mdocstring[39;49;00m)[37m[39;49;00m$
[37m        [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'make-variable-buffer-local[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'quote[39;49;00m[37m [39;49;00m[31mvar[39;49;00m))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mapply-partially[39;49;00m[37m [39;49;00m([31mfun[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31margs[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn a function that is a partial application of FUN to ARGS.[39;49;00m$
[33mARGS is a list of the first N arguments to pass to FUN.[39;49;00m$
[33mThe result is a new function which does the same as FUN, except that[39;49;00m$
[33mthe first N arguments are fixed at the values with which this function[39;49;00m$
[33mwas called.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31margs2[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([32mapply[39;49;00m[37m [39;49;00m[31mfun[39;49;00m[37m [39;49;00m([32mappend[39;49;00m[37m [39;49;00m[31margs[39;49;00m[37m [39;49;00m[31margs2[39;49;00m))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefmacro[39;49;00m[37m [39;49;00m[36mpush[39;49;00m[37m [39;49;00m([31mnewelt[39;49;00m[37m [39;49;00m[31mplace[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mAdd NEWELT to the list stored in the generalized variable PLACE.[39;49;00m$
[33mThis is morally equivalent to (setf PLACE (cons NEWELT PLACE)),[39;49;00m$
[33mexcept that PLACE is only evaluated once (after NEWELT).[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m([31mform[39;49;00m[37m [39;49;00m[31mgv-place[39;49;00m)))[37m[39;49;00m$
[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32msymbolp[39;49;00m[37m [39;49;00m[31mplace[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m[37m;; Important special case, to avoid triggering GV too early in[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m[37m;; the bootstrap.[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'setq[39;49;00m[37m [39;49;00m[31mplace[39;49;00m[37m[39;49;00m$
[37m            [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'cons[39;49;00m[37m [39;49;00m[31mnewelt[39;49;00m[37m [39;49;00m[31mplace[39;49;00m))[37m[39;49;00m$
[37m    [39;49;00m([36mrequire[39;49;00m[37m [39;49;00m[33m'macroexp[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([31mmacroexp-let2[39;49;00m[37m [39;49;00m[31mmacroexp-copyable-p[39;49;00m[37m [39;49;00m[31mv[39;49;00m[37m [39;49;00m[31mnewelt[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([31mgv-letplace[39;49;00m[37m [39;49;00m([31mgetter[39;49;00m[37m [39;49;00m[31msetter[39;49;00m)[37m [39;49;00m[31mplace[39;49;00m[37m[39;49;00m$
[37m        [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31msetter[39;49;00m[37m [39;49;00m`([32mcons[39;49;00m[37m [39;49;00m,[31mv[39;49;00m[37m [39;49;00m,[31mgetter[39;49;00m))))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefmacro[39;49;00m[37m [39;49;00m[36mpop[39;49;00m[37m [39;49;00m([31mplace[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn the first element of PLACE's value, and remove it from the list.[39;49;00m$
[33mPLACE must be a generalized variable whose value is a list.[39;49;00m$
[33mIf the value is nil, [39;49;00m[33m`pop'[39;49;00m[33m returns nil but does not actually[39;49;00m$
[33mchange the list.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m([31mgv-place[39;49;00m)))[37m[39;49;00m$
[37m  [39;49;00m[37m;; We use `car-safe' here instead of `car' because the behavior is the same[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; (if it's not a cons cell, the `cdr' would have signaled an error already),[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; but `car-safe' is total, so the byte-compiler can safely remove it if the[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; result is not used.[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m`([32mcar-safe[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m,([34mif[39;49;00m[37m [39;49;00m([32msymbolp[39;49;00m[37m [39;49;00m[31mplace[39;49;00m)[37m[39;49;00m$
[37m         [39;49;00m[37m;; So we can use `pop' in the bootstrap before `gv' can be used.[39;49;00m[37m[39;49;00m$
[37m         [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'prog1[39;49;00m[37m [39;49;00m[31mplace[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'setq[39;49;00m[37m [39;49;00m[31mplace[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'cdr[39;49;00m[37m [39;49;00m[31mplace[39;49;00m)))[37m[39;49;00m$
[37m       [39;49;00m([31mgv-letplace[39;49;00m[37m [39;49;00m([31mgetter[39;49;00m[37m [39;49;00m[31msetter[39;49;00m)[37m [39;49;00m[31mplace[39;49;00m[37m[39;49;00m$
[37m         [39;49;00m([31mmacroexp-let2[39;49;00m[37m [39;49;00m[31mmacroexp-copyable-p[39;49;00m[37m [39;49;00m[31mx[39;49;00m[37m [39;49;00m[31mgetter[39;49;00m[37m[39;49;00m$
[37m           [39;49;00m`([34mprog1[39;49;00m[37m [39;49;00m,[31mx[39;49;00m[37m [39;49;00m,([32mfuncall[39;49;00m[37m [39;49;00m[31msetter[39;49;00m[37m [39;49;00m`([32mcdr[39;49;00m[37m [39;49;00m,[31mx[39;49;00m))))))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefmacro[39;49;00m[37m [39;49;00m[36mwhen[39;49;00m[37m [39;49;00m([34mcond[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mIf COND yields non-nil, do BODY, else return nil.[39;49;00m$
[33mWhen COND yields non-nil, eval BODY forms sequentially and return[39;49;00m$
[33mvalue of last one, or nil if there are none.[39;49;00m$
[33m[39;49;00m$
[33m\([39;49;00m[33mfn COND BODY...)[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'if[39;49;00m[37m [39;49;00m[34mcond[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[33m'progn[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefmacro[39;49;00m[37m [39;49;00m[36munless[39;49;00m[37m [39;49;00m([34mcond[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mIf COND yields nil, do BODY, else return nil.[39;49;00m$
[33mWhen COND yields nil, eval BODY forms sequentially and return[39;49;00m$
[33mvalue of last one, or nil if there are none.[39;49;00m$
[33m[39;49;00m$
[33m\([39;49;00m[33mfn COND BODY...)[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[33m'if[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[34mcond[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mbody[39;49;00m))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefmacro[39;49;00m[37m [39;49;00m[36mdolist[39;49;00m[37m [39;49;00m([31mspec[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mLoop over a list.[39;49;00m$
[33mEvaluate BODY with VAR bound to each car from LIST, in turn.[39;49;00m$
[33mThen evaluate RESULT to get return value, default nil.[39;49;00m$
[33m[39;49;00m$
[33m\([39;49;00m[33mfn (VAR LIST [RESULT]) BODY...)[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m(([32msymbolp[39;49;00m[37m [39;49;00m[31mform[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mform[39;49;00m)[37m [39;49;00m[31mbody[39;49;00m)))[37m[39;49;00m$
[37m  [39;49;00m[37m;; It would be cleaner to create an uninterned symbol,[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; but that uses a lot more space when many functions in many files[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; use dolist.[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; FIXME: This cost disappears in byte-compiled lexical-binding files.[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtemp[39;49;00m[37m [39;49;00m[33m'--dolist-tail--[39;49;00m))[37m[39;49;00m$
[37m    [39;49;00m[37m;; This is not a reliable test, but it does not matter because both[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[37m;; semantics are acceptable, tho one is slightly faster with dynamic[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[37m;; scoping and the other is slightly faster (and has cleaner semantics)[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[37m;; with lexical scoping.[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mlexical-binding[39;49;00m[37m[39;49;00m$
[37m        [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m((,[31mtemp[39;49;00m[37m [39;49;00m,([32mnth[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)))[37m[39;49;00m$
[37m           [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m,[31mtemp[39;49;00m[37m[39;49;00m$
[37m             [39;49;00m([34mlet[39;49;00m[37m [39;49;00m((,([32mcar[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m,[31mtemp[39;49;00m)))[37m[39;49;00m$
[37m               [39;49;00m,@[31mbody[39;49;00m[37m[39;49;00m$
[37m               [39;49;00m([34msetq[39;49;00m[37m [39;49;00m,[31mtemp[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m,[31mtemp[39;49;00m))))[37m[39;49;00m$
[37m           [39;49;00m,@([32mcdr[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)))[37m[39;49;00m$
[37m      [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m((,[31mtemp[39;49;00m[37m [39;49;00m,([32mnth[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mspec[39;49;00m))[37m[39;49;00m$
[37m             [39;49;00m,([32mcar[39;49;00m[37m [39;49;00m[31mspec[39;49;00m))[37m[39;49;00m$
[37m         [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m,[31mtemp[39;49;00m[37m[39;49;00m$
[37m           [39;49;00m([34msetq[39;49;00m[37m [39;49;00m,([32mcar[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m,[31mtemp[39;49;00m))[37m[39;49;00m$
[37m           [39;49;00m,@[31mbody[39;49;00m[37m[39;49;00m$
[37m           [39;49;00m([34msetq[39;49;00m[37m [39;49;00m,[31mtemp[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m,[31mtemp[39;49;00m)))[37m[39;49;00m$
[37m         [39;49;00m,@([34mif[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mspec[39;49;00m))[37m[39;49;00m$
[37m               [39;49;00m`(([34msetq[39;49;00m[37m [39;49;00m,([32mcar[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)[37m [39;49;00m[31mnil[39;49;00m)[37m [39;49;00m,@([32mcdr[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mspec[39;49;00m))))))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefmacro[39;49;00m[37m [39;49;00m[36mdotimes[39;49;00m[37m [39;49;00m([31mspec[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mLoop a certain number of times.[39;49;00m$
[33mEvaluate BODY with VAR bound to successive integers running from 0,[39;49;00m$
[33minclusive, to COUNT, exclusive.  Then evaluate RESULT to get[39;49;00m$
[33mthe return value (nil if RESULT is omitted).[39;49;00m$
[33m[39;49;00m$
[33m\([39;49;00m[33mfn (VAR COUNT [RESULT]) BODY...)[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[36mdolist[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m[37m;; It would be cleaner to create an uninterned symbol,[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; but that uses a lot more space when many functions in many files[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; use dotimes.[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; FIXME: This cost disappears in byte-compiled lexical-binding files.[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtemp[39;49;00m[37m [39;49;00m[33m'--dotimes-limit--[39;49;00m)[37m[39;49;00m$
[37m^I[39;49;00m([31mstart[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m^I[39;49;00m([31mend[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m[37m;; This is not a reliable test, but it does not matter because both[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[37m;; semantics are acceptable, tho one is slightly faster with dynamic[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[37m;; scoping and the other has cleaner semantics.[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mlexical-binding[39;49;00m[37m[39;49;00m$
[37m        [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mcounter[39;49;00m[37m [39;49;00m[33m'--dotimes-counter--[39;49;00m))[37m[39;49;00m$
[37m          [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m((,[31mtemp[39;49;00m[37m [39;49;00m,[31mend[39;49;00m)[37m[39;49;00m$
[37m                 [39;49;00m(,[31mcounter[39;49;00m[37m [39;49;00m,[31mstart[39;49;00m))[37m[39;49;00m$
[37m             [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m,[31mcounter[39;49;00m[37m [39;49;00m,[31mtemp[39;49;00m)[37m[39;49;00m$
[37m               [39;49;00m([34mlet[39;49;00m[37m [39;49;00m((,([32mcar[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)[37m [39;49;00m,[31mcounter[39;49;00m))[37m[39;49;00m$
[37m                 [39;49;00m,@[31mbody[39;49;00m)[37m[39;49;00m$
[37m               [39;49;00m([34msetq[39;49;00m[37m [39;49;00m,[31mcounter[39;49;00m[37m [39;49;00m([32m1+[39;49;00m[37m [39;49;00m,[31mcounter[39;49;00m)))[37m[39;49;00m$
[37m             [39;49;00m,@([34mif[39;49;00m[37m [39;49;00m([31mcddr[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)[37m[39;49;00m$
[37m                   [39;49;00m[37m;; FIXME: This let often leads to "unused var" warnings.[39;49;00m[37m[39;49;00m$
[37m                   [39;49;00m`(([34mlet[39;49;00m[37m [39;49;00m((,([32mcar[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)[37m [39;49;00m,[31mcounter[39;49;00m))[37m [39;49;00m,@([31mcddr[39;49;00m[37m [39;49;00m[31mspec[39;49;00m))))))[37m[39;49;00m$
[37m      [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m((,[31mtemp[39;49;00m[37m [39;49;00m,[31mend[39;49;00m)[37m[39;49;00m$
[37m             [39;49;00m(,([32mcar[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)[37m [39;49;00m,[31mstart[39;49;00m))[37m[39;49;00m$
[37m         [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m,([32mcar[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)[37m [39;49;00m,[31mtemp[39;49;00m)[37m[39;49;00m$
[37m           [39;49;00m,@[31mbody[39;49;00m[37m[39;49;00m$
[37m           [39;49;00m([34msetq[39;49;00m[37m [39;49;00m,([32mcar[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)[37m [39;49;00m([32m1+[39;49;00m[37m [39;49;00m,([32mcar[39;49;00m[37m [39;49;00m[31mspec[39;49;00m))))[37m[39;49;00m$
[37m         [39;49;00m,@([32mcdr[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mspec[39;49;00m))))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefmacro[39;49;00m[37m [39;49;00m[36mdeclare[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31m_specs[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mDo not evaluate any arguments, and return nil.[39;49;00m$
[33mIf a [39;49;00m[33m`declare'[39;49;00m[33m form appears as the first form in the body of a[39;49;00m$
[33m`defun'[39;49;00m[33m or [39;49;00m[33m`defmacro'[39;49;00m[33m form, SPECS specifies various additional[39;49;00m$
[33minformation about the function or macro; these go into effect[39;49;00m$
[33mduring the evaluation of the [39;49;00m[33m`defun'[39;49;00m[33m or [39;49;00m[33m`defmacro'[39;49;00m[33m form.[39;49;00m$
[33m[39;49;00m$
[33mThe possible values of SPECS are specified by[39;49;00m$
[33m`defun-declarations-alist'[39;49;00m[33m and [39;49;00m[33m`macro-declarations-alist'[39;49;00m[33m.[39;49;00m$
[33m[39;49;00m$
[33mFor more information, see info node [39;49;00m[33m`[39;49;00m[33m(elisp)Declare Form'.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; FIXME: edebug spec should pay attention to defun-declarations-alist.[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
([36mdefmacro[39;49;00m[37m [39;49;00m[36mignore-errors[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mExecute BODY; if an error occurs, return nil.[39;49;00m$
[33mOtherwise, return result of last form in BODY.[39;49;00m$
[33mSee also [39;49;00m[33m`with-demoted-errors'[39;49;00m[33m that does something similar[39;49;00m$
[33mwithout silencing all errors.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m`([34mcondition-case[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m([34mprogn[39;49;00m[37m [39;49;00m,@[31mbody[39;49;00m)[37m [39;49;00m([36merror[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m[37m[39;49;00m$
[37m;;;; Basic Lisp functions.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mignore[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31m_ignore[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mDo nothing and return nil.[39;49;00m$
[33mThis function accepts any number of arguments, but ignores them.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34minteractive[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
[37m;; Signal a compile-error if the first arg is missing.[39;49;00m[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[36merror[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31margs[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mSignal an error, making error message by passing all args to [39;49;00m[33m`format'[39;49;00m[33m.[39;49;00m$
[33mIn Emacs, the convention is that error messages start with a capital[39;49;00m$
[33mletter but *do not* end with a period.  Please follow this convention[39;49;00m$
[33mfor the sake of consistency.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31madvertised-calling-convention[39;49;00m[37m [39;49;00m([32mstring[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31margs[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m23.1[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m([32msignal[39;49;00m[37m [39;49;00m[33m'error[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m([32mapply[39;49;00m[37m [39;49;00m[33m'format[39;49;00m[37m [39;49;00m[31margs[39;49;00m))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[36muser-error[39;49;00m[37m [39;49;00m([32mformat[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31margs[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mSignal a pilot error, making error message by passing all args to [39;49;00m[33m`format'[39;49;00m[33m.[39;49;00m$
[33mIn Emacs, the convention is that error messages start with a capital[39;49;00m$
[33mletter but *do not* end with a period.  Please follow this convention[39;49;00m$
[33mfor the sake of consistency.[39;49;00m$
[33mThis is just like [39;49;00m[33m`error'[39;49;00m[33m except that [39;49;00m[33m`user-error'[39;49;00m[33ms are expected to be the[39;49;00m$
[33mresult of an incorrect manipulation on the part of the user, rather than the[39;49;00m$
[33mresult of an actual problem.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([32msignal[39;49;00m[37m [39;49;00m[33m'user-error[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m([32mapply[39;49;00m[37m [39;49;00m[32m#'[39;49;00m[32mformat[39;49;00m[37m [39;49;00m[32mformat[39;49;00m[37m [39;49;00m[31margs[39;49;00m))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mdefine-error[39;49;00m[37m [39;49;00m([31mname[39;49;00m[37m [39;49;00m[32mmessage[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mparent[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mDefine NAME as a new error signal.[39;49;00m$
[33mMESSAGE is a string that will be output to the echo area if such an error[39;49;00m$
[33mis signaled without being caught by a [39;49;00m[33m`condition-case'[39;49;00m[33m.[39;49;00m$
[33mPARENT is either a signal or a list of signals from which it inherits.[39;49;00m$
[33mDefaults to [39;49;00m[33m`error'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36munless[39;49;00m[37m [39;49;00m[31mparent[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mparent[39;49;00m[37m [39;49;00m[33m'error[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mconditions[39;49;00m[37m[39;49;00m$
[37m         [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mparent[39;49;00m)[37m[39;49;00m$
[37m             [39;49;00m([32mapply[39;49;00m[37m [39;49;00m[32m#'[39;49;00m[32mappend[39;49;00m[37m[39;49;00m$
[37m                    [39;49;00m([32mmapcar[39;49;00m[37m [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31mparent[39;49;00m)[37m[39;49;00m$
[37m                              [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mparent[39;49;00m[37m[39;49;00m$
[37m                                    [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mget[39;49;00m[37m [39;49;00m[31mparent[39;49;00m[37m [39;49;00m[33m'error-conditions[39;49;00m)[37m[39;49;00m$
[37m                                        [39;49;00m([36merror[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mUnknown signal [39;49;00m[33m`%s'[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mparent[39;49;00m))))[37m[39;49;00m$
[37m                            [39;49;00m[31mparent[39;49;00m))[37m[39;49;00m$
[37m           [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mparent[39;49;00m[37m [39;49;00m([32mget[39;49;00m[37m [39;49;00m[31mparent[39;49;00m[37m [39;49;00m[33m'error-conditions[39;49;00m)))))[37m[39;49;00m$
[37m    [39;49;00m([32mput[39;49;00m[37m [39;49;00m[31mname[39;49;00m[37m [39;49;00m[33m'error-conditions[39;49;00m[37m[39;49;00m$
[37m         [39;49;00m([31mdelete-dups[39;49;00m[37m [39;49;00m([32mcopy-sequence[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mname[39;49;00m[37m [39;49;00m[31mconditions[39;49;00m))))[37m[39;49;00m$
[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[32mmessage[39;49;00m[37m [39;49;00m([32mput[39;49;00m[37m [39;49;00m[31mname[39;49;00m[37m [39;49;00m[33m'error-message[39;49;00m[37m [39;49;00m[32mmessage[39;49;00m))))[37m[39;49;00m$
[37m[39;49;00m$
[37m;; We put this here instead of in frame.el so that it's defined even on[39;49;00m[37m[39;49;00m$
[37m;; systems where frame.el isn't loaded.[39;49;00m[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mframe-configuration-p[39;49;00m[37m [39;49;00m([31mobject[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn non-nil if OBJECT seems to be a frame configuration.[39;49;00m$
[33mAny list whose car is [39;49;00m[33m`frame-configuration'[39;49;00m[33m is assumed to be a frame[39;49;00m$
[33mconfiguration.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mobject[39;49;00m)[37m[39;49;00m$
[37m       [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mobject[39;49;00m)[37m [39;49;00m[33m'frame-configuration[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m[37m[39;49;00m$
[37m;;;; List functions.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
([36mdefsubst[39;49;00m[37m [39;49;00m[31mcaar[39;49;00m[37m [39;49;00m([31mx[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn the car of the car of X.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([32mcar[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mx[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefsubst[39;49;00m[37m [39;49;00m[31mcadr[39;49;00m[37m [39;49;00m([31mx[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn the car of the cdr of X.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([32mcar[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mx[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefsubst[39;49;00m[37m [39;49;00m[31mcdar[39;49;00m[37m [39;49;00m([31mx[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn the cdr of the car of X.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mx[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefsubst[39;49;00m[37m [39;49;00m[31mcddr[39;49;00m[37m [39;49;00m([31mx[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn the cdr of the cdr of X.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mx[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mlast[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mn[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn the last link of LIST.  Its car is the last element.[39;49;00m$
[33mIf LIST is nil, return nil.[39;49;00m$
[33mIf N is non-nil, return the Nth-to-last link of LIST.[39;49;00m$
[33mIf N is bigger than the length of LIST, return LIST.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mn[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32m>=[39;49;00m[37m [39;49;00m[31mn[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m           [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mm[39;49;00m[37m [39;49;00m([32msafe-length[39;49;00m[37m [39;49;00m[32mlist[39;49;00m)))[37m[39;49;00m$
[37m             [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m[31mn[39;49;00m[37m [39;49;00m[31mm[39;49;00m)[37m [39;49;00m([32mnthcdr[39;49;00m[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m[31mm[39;49;00m[37m [39;49;00m[31mn[39;49;00m)[37m [39;49;00m[32mlist[39;49;00m)[37m [39;49;00m[32mlist[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m([34mand[39;49;00m[37m [39;49;00m[32mlist[39;49;00m[37m[39;49;00m$
[37m         [39;49;00m([32mnthcdr[39;49;00m[37m [39;49;00m([32m1-[39;49;00m[37m [39;49;00m([32msafe-length[39;49;00m[37m [39;49;00m[32mlist[39;49;00m))[37m [39;49;00m[32mlist[39;49;00m))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mbutlast[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mn[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn a copy of LIST with the last N elements removed.[39;49;00m$
[33mIf N is omitted or nil, the last element is removed from the[39;49;00m$
[33mcopy.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mn[39;49;00m[37m [39;49;00m([32m<=[39;49;00m[37m [39;49;00m[31mn[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m [39;49;00m[32mlist[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m([31mnbutlast[39;49;00m[37m [39;49;00m([32mcopy-sequence[39;49;00m[37m [39;49;00m[32mlist[39;49;00m)[37m [39;49;00m[31mn[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mnbutlast[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mn[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mModifies LIST to remove the last N elements.[39;49;00m$
[33mIf N is omitted or nil, remove the last element.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mm[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[32mlist[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mn[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mn[39;49;00m[37m [39;49;00m[34m1[39;49;00m))[37m[39;49;00m$
[37m    [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m[31mn[39;49;00m[37m [39;49;00m[31mm[39;49;00m)[37m[39;49;00m$
[37m^I [39;49;00m([34mprogn[39;49;00m[37m[39;49;00m$
[37m^I   [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m[31mn[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m([32msetcdr[39;49;00m[37m [39;49;00m([32mnthcdr[39;49;00m[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m([32m1-[39;49;00m[37m [39;49;00m[31mm[39;49;00m)[37m [39;49;00m[31mn[39;49;00m)[37m [39;49;00m[32mlist[39;49;00m)[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m$
[37m^I   [39;49;00m[32mlist[39;49;00m))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mzerop[39;49;00m[37m [39;49;00m([31mnumber[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn t if NUMBER is zero.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; Used to be in C, but it's pointless since (= 0 n) is faster anyway because[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; = has a byte-code.[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mcompiler-macro[39;49;00m[37m [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31m_[39;49;00m)[37m [39;49;00m`([32m=[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m,[31mnumber[39;49;00m))))[37m[39;49;00m$
[37m  [39;49;00m([32m=[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[31mnumber[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mdelete-dups[39;49;00m[37m [39;49;00m([32mlist[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mDestructively remove [39;49;00m[33m`equal'[39;49;00m[33m duplicates from LIST.[39;49;00m$
[33mStore the result in LIST and return it.  LIST must be a proper list.[39;49;00m$
[33mOf several [39;49;00m[33m`equal'[39;49;00m[33m occurrences of an element in LIST, the first[39;49;00m$
[33mone is kept.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtail[39;49;00m[37m [39;49;00m[32mlist[39;49;00m))[37m[39;49;00m$
[37m    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([32msetcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([32mdelete[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)))[37m[39;49;00m$
[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))))[37m[39;49;00m$
[37m  [39;49;00m[32mlist[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
[37m;; See http://lists.gnu.org/archive/html/emacs-devel/2013-05/msg00204.html[39;49;00m[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mdelete-consecutive-dups[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mcircular[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mDestructively remove [39;49;00m[33m`equal'[39;49;00m[33m consecutive duplicates from LIST.[39;49;00m$
[33mFirst and last elements are considered consecutive if CIRCULAR is[39;49;00m$
[33mnon-nil.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtail[39;49;00m[37m [39;49;00m[32mlist[39;49;00m)[37m [39;49;00m[31mlast[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mequal[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)[37m [39;49;00m([31mcadr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))[37m[39;49;00m$
[37m^I  [39;49;00m([32msetcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([31mcddr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))[37m[39;49;00m$
[37m^I[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mlast[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)[37m[39;49;00m$
[37m^I      [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))))[37m[39;49;00m$
[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mcircular[39;49;00m[37m[39;49;00m$
[37m^I     [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[32mlist[39;49;00m)[37m[39;49;00m$
[37m^I     [39;49;00m([32mequal[39;49;00m[37m [39;49;00m[31mlast[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[32mlist[39;49;00m)))[37m[39;49;00m$
[37m^I[39;49;00m([31mnbutlast[39;49;00m[37m [39;49;00m[32mlist[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m[32mlist[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mnumber-sequence[39;49;00m[37m [39;49;00m([31mfrom[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mto[39;49;00m[37m [39;49;00m[31minc[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn a sequence of numbers from FROM to TO (both inclusive) as a list.[39;49;00m$
[33mINC is the increment used between numbers in the sequence and defaults to 1.[39;49;00m$
[33mSo, the Nth element of the list is (+ FROM (* N INC)) where N counts from[39;49;00m$
[33mzero.  TO is only included if there is an N for which TO = FROM + N * INC.[39;49;00m$
[33mIf TO is nil or numerically equal to FROM, return (FROM).[39;49;00m$
[33mIf INC is positive and TO is less than FROM, or INC is negative[39;49;00m$
[33mand TO is larger than FROM, return nil.[39;49;00m$
[33mIf INC is zero and TO is neither nil nor numerically equal to[39;49;00m$
[33mFROM, signal an error.[39;49;00m$
[33m[39;49;00m$
[33mThis function is primarily designed for integer arguments.[39;49;00m$
[33mNevertheless, FROM, TO and INC can be integer or float.  However,[39;49;00m$
[33mfloating point arithmetic is inexact.  For instance, depending on[39;49;00m$
[33mthe machine, it may quite well happen that[39;49;00m$
[33m\([39;49;00m[33mnumber-sequence 0.4 0.6 0.2) returns the one element list (0.4),[39;49;00m$
[33mwhereas (number-sequence 0.4 0.8 0.2) returns a list with three[39;49;00m$
[33melements.  Thus, if some of the arguments are floats and one wants[39;49;00m$
[33mto make sure that TO is included, one may have to explicitly write[39;49;00m$
[33mTO as (+ FROM (* N INC)) or use a variable whose value was[39;49;00m$
[33mcomputed with this exact expression.  Alternatively, you can,[39;49;00m$
[33mof course, also replace TO with a slightly larger value[39;49;00m$
[33m\([39;49;00m[33mor a slightly more negative value if INC is negative).[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m[31mto[39;49;00m)[37m [39;49;00m([32m=[39;49;00m[37m [39;49;00m[31mfrom[39;49;00m[37m [39;49;00m[31mto[39;49;00m))[37m[39;49;00m$
[37m      [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[31mfrom[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31minc[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31minc[39;49;00m[37m [39;49;00m[34m1[39;49;00m))[37m[39;49;00m$
[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([31mzerop[39;49;00m[37m [39;49;00m[31minc[39;49;00m)[37m [39;49;00m([36merror[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mThe increment can not be zero[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m([31mseq[39;49;00m[37m [39;49;00m([31mn[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m([31mnext[39;49;00m[37m [39;49;00m[31mfrom[39;49;00m))[37m[39;49;00m$
[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m[31minc[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m          [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32m<=[39;49;00m[37m [39;49;00m[31mnext[39;49;00m[37m [39;49;00m[31mto[39;49;00m)[37m[39;49;00m$
[37m            [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mseq[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mnext[39;49;00m[37m [39;49;00m[31mseq[39;49;00m)[37m[39;49;00m$
[37m                  [39;49;00m[31mn[39;49;00m[37m [39;49;00m([32m1+[39;49;00m[37m [39;49;00m[31mn[39;49;00m)[37m[39;49;00m$
[37m                  [39;49;00m[31mnext[39;49;00m[37m [39;49;00m([32m+[39;49;00m[37m [39;49;00m[31mfrom[39;49;00m[37m [39;49;00m([32m*[39;49;00m[37m [39;49;00m[31mn[39;49;00m[37m [39;49;00m[31minc[39;49;00m))))[37m[39;49;00m$
[37m        [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32m>=[39;49;00m[37m [39;49;00m[31mnext[39;49;00m[37m [39;49;00m[31mto[39;49;00m)[37m[39;49;00m$
[37m          [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mseq[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mnext[39;49;00m[37m [39;49;00m[31mseq[39;49;00m)[37m[39;49;00m$
[37m                [39;49;00m[31mn[39;49;00m[37m [39;49;00m([32m1+[39;49;00m[37m [39;49;00m[31mn[39;49;00m)[37m[39;49;00m$
[37m                [39;49;00m[31mnext[39;49;00m[37m [39;49;00m([32m+[39;49;00m[37m [39;49;00m[31mfrom[39;49;00m[37m [39;49;00m([32m*[39;49;00m[37m [39;49;00m[31mn[39;49;00m[37m [39;49;00m[31minc[39;49;00m)))))[37m[39;49;00m$
[37m      [39;49;00m([32mnreverse[39;49;00m[37m [39;49;00m[31mseq[39;49;00m))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mcopy-tree[39;49;00m[37m [39;49;00m([31mtree[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mvecp[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mMake a copy of TREE.[39;49;00m$
[33mIf TREE is a cons cell, this recursively copies both its car and its cdr.[39;49;00m$
[33mContrast to [39;49;00m[33m`copy-sequence'[39;49;00m[33m, which copies only along the cdrs.  With second[39;49;00m$
[33margument VECP, this copies vectors as well as conses.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mtree[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m([31mresult[39;49;00m)[37m[39;49;00m$
[37m^I[39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mtree[39;49;00m)[37m[39;49;00m$
[37m^I  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mnewcar[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mtree[39;49;00m)))[37m[39;49;00m$
[37m^I    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mtree[39;49;00m))[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mvecp[39;49;00m[37m [39;49;00m([32mvectorp[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mtree[39;49;00m))))[37m[39;49;00m$
[37m^I^I[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mnewcar[39;49;00m[37m [39;49;00m([31mcopy-tree[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mtree[39;49;00m)[37m [39;49;00m[31mvecp[39;49;00m)))[37m[39;49;00m$
[37m^I    [39;49;00m([36mpush[39;49;00m[37m [39;49;00m[31mnewcar[39;49;00m[37m [39;49;00m[31mresult[39;49;00m))[37m[39;49;00m$
[37m^I  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mtree[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtree[39;49;00m)))[37m[39;49;00m$
[37m^I[39;49;00m([32mnconc[39;49;00m[37m [39;49;00m([32mnreverse[39;49;00m[37m [39;49;00m[31mresult[39;49;00m)[37m [39;49;00m[31mtree[39;49;00m))[37m[39;49;00m$
[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mvecp[39;49;00m[37m [39;49;00m([32mvectorp[39;49;00m[37m [39;49;00m[31mtree[39;49;00m))[37m[39;49;00m$
[37m^I[39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mi[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mtree[39;49;00m[37m [39;49;00m([32mcopy-sequence[39;49;00m[37m [39;49;00m[31mtree[39;49;00m)))))[37m[39;49;00m$
[37m^I  [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32m>=[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mi[39;49;00m[37m [39;49;00m([32m1-[39;49;00m[37m [39;49;00m[31mi[39;49;00m))[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m^I    [39;49;00m([32maset[39;49;00m[37m [39;49;00m[31mtree[39;49;00m[37m [39;49;00m[31mi[39;49;00m[37m [39;49;00m([31mcopy-tree[39;49;00m[37m [39;49;00m([32maref[39;49;00m[37m [39;49;00m[31mtree[39;49;00m[37m [39;49;00m[31mi[39;49;00m)[37m [39;49;00m[31mvecp[39;49;00m)))[37m[39;49;00m$
[37m^I  [39;49;00m[31mtree[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m[31mtree[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m[37m[39;49;00m$
[37m;;;; Various list-search functions.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31massoc-default[39;49;00m[37m [39;49;00m([31mkey[39;49;00m[37m [39;49;00m[31malist[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mtest[39;49;00m[37m [39;49;00m[31mdefault[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mFind object KEY in a pseudo-alist ALIST.[39;49;00m$
[33mALIST is a list of conses or objects.  Each element[39;49;00m$
[33m (or the element's car, if it is a cons) is compared with KEY by[39;49;00m$
[33m calling TEST, with two arguments: (i) the element or its car,[39;49;00m$
[33m and (ii) KEY.[39;49;00m$
[33mIf that is non-nil, the element matches; then [39;49;00m[33m`assoc-default'[39;49;00m[33m[39;49;00m$
[33m returns the element's cdr, if it is a cons, or DEFAULT if the[39;49;00m$
[33m element is not a cons.[39;49;00m$
[33m[39;49;00m$
[33mIf no element matches, the value is nil.[39;49;00m$
[33mIf TEST is omitted or nil, [39;49;00m[33m`equal'[39;49;00m[33m is used.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m([31mfound[39;49;00m[37m [39;49;00m([31mtail[39;49;00m[37m [39;49;00m[31malist[39;49;00m)[37m [39;49;00m[31mvalue[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m[31mfound[39;49;00m))[37m[39;49;00m$
[37m      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([32melt[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)))[37m[39;49;00m$
[37m^I[39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mtest[39;49;00m[37m [39;49;00m[33m'equal[39;49;00m)[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[32melt[39;49;00m)[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[32melt[39;49;00m)[37m [39;49;00m[32melt[39;49;00m)[37m [39;49;00m[31mkey[39;49;00m)[37m[39;49;00m$
[37m^I  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mfound[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m[31mvalue[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[32melt[39;49;00m)[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[32melt[39;49;00m)[37m [39;49;00m[31mdefault[39;49;00m))))[37m[39;49;00m$
[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m[31mvalue[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31massoc-ignore-case[39;49;00m[37m [39;49;00m([31mkey[39;49;00m[37m [39;49;00m[31malist[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mLike [39;49;00m[33m`assoc'[39;49;00m[33m, but ignores differences in case and text representation.[39;49;00m$
[33mKEY must be a string.  Upper-case and lower-case letters are treated as equal.[39;49;00m$
[33mUnibyte strings are converted to multibyte for comparison.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mobsolete[39;49;00m[37m [39;49;00m[32massoc-string[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m22.1[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m([32massoc-string[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m[31malist[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31massoc-ignore-representation[39;49;00m[37m [39;49;00m([31mkey[39;49;00m[37m [39;49;00m[31malist[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mLike [39;49;00m[33m`assoc'[39;49;00m[33m, but ignores differences in text representation.[39;49;00m$
[33mKEY must be a string.[39;49;00m$
[33mUnibyte strings are converted to multibyte for comparison.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mobsolete[39;49;00m[37m [39;49;00m[32massoc-string[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m22.1[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m([32massoc-string[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m[31malist[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mmember-ignore-case[39;49;00m[37m [39;49;00m([32melt[39;49;00m[37m [39;49;00m[32mlist[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mLike [39;49;00m[33m`member'[39;49;00m[33m, but ignore differences in case and text representation.[39;49;00m$
[33mELT must be a string.  Upper-case and lower-case letters are treated as equal.[39;49;00m$
[33mUnibyte strings are converted to multibyte for comparison.[39;49;00m$
[33mNon-strings in LIST are ignored.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[32mlist[39;49;00m[37m[39;49;00m$
[37m^I      [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[32mlist[39;49;00m))[37m[39;49;00m$
[37m^I^I^I[39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m([32mcompare-strings[39;49;00m[37m [39;49;00m[32melt[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[32mlist[39;49;00m)[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mt[39;49;00m)))))[37m[39;49;00m$
[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[32mlist[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[32mlist[39;49;00m)))[37m[39;49;00m$
[37m  [39;49;00m[32mlist[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31massq-delete-all[39;49;00m[37m [39;49;00m([31mkey[39;49;00m[37m [39;49;00m[31malist[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mDelete from ALIST all elements whose car is [39;49;00m[33m`eq'[39;49;00m[33m to KEY.[39;49;00m$
[33mReturn the modified alist.[39;49;00m$
[33mElements of ALIST that are not conses are ignored.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31malist[39;49;00m))[37m[39;49;00m$
[37m^I      [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31malist[39;49;00m))[37m [39;49;00m[31mkey[39;49;00m))[37m[39;49;00m$
[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31malist[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31malist[39;49;00m)))[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtail[39;49;00m[37m [39;49;00m[31malist[39;49;00m)[37m [39;49;00m[31mtail-cdr[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mtail-cdr[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))[37m[39;49;00m$
[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mtail-cdr[39;49;00m))[37m[39;49;00m$
[37m^I       [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mtail-cdr[39;49;00m))[37m [39;49;00m[31mkey[39;49;00m))[37m[39;49;00m$
[37m^I  [39;49;00m([32msetcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail-cdr[39;49;00m))[37m[39;49;00m$
[37m^I[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m[31mtail-cdr[39;49;00m))))[37m[39;49;00m$
[37m  [39;49;00m[31malist[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mrassq-delete-all[39;49;00m[37m [39;49;00m([31mvalue[39;49;00m[37m [39;49;00m[31malist[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mDelete from ALIST all elements whose cdr is [39;49;00m[33m`eq'[39;49;00m[33m to VALUE.[39;49;00m$
[33mReturn the modified alist.[39;49;00m$
[33mElements of ALIST that are not conses are ignored.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31malist[39;49;00m))[37m[39;49;00m$
[37m^I      [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31malist[39;49;00m))[37m [39;49;00m[31mvalue[39;49;00m))[37m[39;49;00m$
[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31malist[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31malist[39;49;00m)))[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtail[39;49;00m[37m [39;49;00m[31malist[39;49;00m)[37m [39;49;00m[31mtail-cdr[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mtail-cdr[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))[37m[39;49;00m$
[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mtail-cdr[39;49;00m))[37m[39;49;00m$
[37m^I       [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mtail-cdr[39;49;00m))[37m [39;49;00m[31mvalue[39;49;00m))[37m[39;49;00m$
[37m^I  [39;49;00m([32msetcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail-cdr[39;49;00m))[37m[39;49;00m$
[37m^I[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m[31mtail-cdr[39;49;00m))))[37m[39;49;00m$
[37m  [39;49;00m[31malist[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31malist-get[39;49;00m[37m [39;49;00m([31mkey[39;49;00m[37m [39;49;00m[31malist[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mdefault[39;49;00m[37m [39;49;00m[31mremove[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mGet the value associated to KEY in ALIST.[39;49;00m$
[33mDEFAULT is the value to return if KEY is not found in ALIST.[39;49;00m$
[33mREMOVE, if non-nil, means that when setting this element, we should[39;49;00m$
[33mremove the entry if the new value is [39;49;00m[33m`eql'[39;49;00m[33m to DEFAULT.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([31mignore[39;49;00m[37m [39;49;00m[31mremove[39;49;00m)[37m [39;49;00m[37m;;Silence byte-compiler.[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mx[39;49;00m[37m [39;49;00m([32massq[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m[31malist[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mx[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mx[39;49;00m)[37m [39;49;00m[31mdefault[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mremove[39;49;00m[37m [39;49;00m([32melt[39;49;00m[37m [39;49;00m[31mseq[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn a copy of SEQ with all occurrences of ELT removed.[39;49;00m$
[33mSEQ must be a list, vector, or string.  The comparison is done with [39;49;00m[33m`equal'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mnlistp[39;49;00m[37m [39;49;00m[31mseq[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m[37m;; If SEQ isn't a list, there's no need to copy SEQ because[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m[37m;; `delete' will return a new object.[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([32mdelete[39;49;00m[37m [39;49;00m[32melt[39;49;00m[37m [39;49;00m[31mseq[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([32mdelete[39;49;00m[37m [39;49;00m[32melt[39;49;00m[37m [39;49;00m([32mcopy-sequence[39;49;00m[37m [39;49;00m[31mseq[39;49;00m))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mremq[39;49;00m[37m [39;49;00m([32melt[39;49;00m[37m [39;49;00m[32mlist[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn LIST with all occurrences of ELT removed.[39;49;00m$
[33mThe comparison is done with [39;49;00m[33m`eq'[39;49;00m[33m.  Contrary to [39;49;00m[33m`delq'[39;49;00m[33m, this does not use[39;49;00m$
[33mside-effects, and the argument LIST is not modified.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[32melt[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[32mlist[39;49;00m))[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[32mlist[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[32mlist[39;49;00m))))[37m[39;49;00m$
[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[32melt[39;49;00m[37m [39;49;00m[32mlist[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m([32mdelq[39;49;00m[37m [39;49;00m[32melt[39;49;00m[37m [39;49;00m([32mcopy-sequence[39;49;00m[37m [39;49;00m[32mlist[39;49;00m))[37m[39;49;00m$
[37m    [39;49;00m[32mlist[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m[37m[39;49;00m$
[37m;;;; Keymap support.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mkbd[39;49;00m[37m [39;49;00m([31mkeys[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mConvert KEYS to the internal Emacs key representation.[39;49;00m$
[33mKEYS should be a string constant in the format used for[39;49;00m$
[33msaving keyboard macros (see [39;49;00m[33m`edmacro-mode'[39;49;00m[33m).[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; Don't use a defalias, since the `pure' property is only true for[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; the calling convention of `kbd'.[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([31mread-kbd-macro[39;49;00m[37m [39;49;00m[31mkeys[39;49;00m))[37m[39;49;00m$
([32mput[39;49;00m[37m [39;49;00m[33m'kbd[39;49;00m[37m [39;49;00m[33m'pure[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mundefined[39;49;00m[37m [39;49;00m()[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mBeep to tell the user this binding is undefined.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34minteractive[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m([32mding[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m%s is undefined[39;49;00m[33m"[39;49;00m[37m [39;49;00m([32mkey-description[39;49;00m[37m [39;49;00m([32mthis-single-command-keys[39;49;00m)))[37m[39;49;00m$
[37m  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mdefining-kbd-macro[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m([32mforce-mode-line-update[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[37m;; If this is a down-mouse event, don't reset prefix-arg;[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; pass it to the command run by the up event.[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mprefix-arg[39;49;00m[37m[39;49;00m$
[37m        [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[33m'down[39;49;00m[37m [39;49;00m([31mevent-modifiers[39;49;00m[37m [39;49;00m[31mlast-command-event[39;49;00m))[37m[39;49;00m$
[37m          [39;49;00m[31mcurrent-prefix-arg[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
[37m;; Prevent the \{...} documentation construct[39;49;00m[37m[39;49;00m$
[37m;; from mentioning keys that run this command.[39;49;00m[37m[39;49;00m$
([32mput[39;49;00m[37m [39;49;00m[33m'undefined[39;49;00m[37m [39;49;00m[33m'suppress-keymap[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31msuppress-keymap[39;49;00m[37m [39;49;00m([31mmap[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mnodigits[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mMake MAP override all normally self-inserting keys to be undefined.[39;49;00m$
[33mNormally, as an exception, digits and minus-sign are set to make prefix args,[39;49;00m$
[33mbut optional second arg NODIGITS non-nil treats them like other chars.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([32mdefine-key[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m[[31mremap[39;49;00m[37m [39;49;00m[32mself-insert-command[39;49;00m][37m [39;49;00m[33m'undefined[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mnodigits[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m([36mloop[39;49;00m)[37m[39;49;00m$
[37m^I[39;49;00m([32mdefine-key[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m-[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m'negative-argument[39;49;00m)[37m[39;49;00m$
[37m^I[39;49;00m[37m;; Make plain numbers do numeric args.[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[36mloop[39;49;00m[37m [39;49;00m[33m?0[39;49;00m)[37m[39;49;00m$
[37m^I[39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32m<=[39;49;00m[37m [39;49;00m[36mloop[39;49;00m[37m [39;49;00m[33m?9[39;49;00m)[37m[39;49;00m$
[37m^I  [39;49;00m([32mdefine-key[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m([32mchar-to-string[39;49;00m[37m [39;49;00m[36mloop[39;49;00m)[37m [39;49;00m[33m'digit-argument[39;49;00m)[37m[39;49;00m$
[37m^I  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[36mloop[39;49;00m[37m [39;49;00m([32m1+[39;49;00m[37m [39;49;00m[36mloop[39;49;00m))))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mmake-composed-keymap[39;49;00m[37m [39;49;00m([31mmaps[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mparent[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mConstruct a new keymap composed of MAPS and inheriting from PARENT.[39;49;00m$
[33mWhen looking up a key in the returned map, the key is looked in each[39;49;00m$
[33mkeymap of MAPS in turn until a binding is found.[39;49;00m$
[33mIf no binding is found in MAPS, the lookup continues in PARENT, if non-nil.[39;49;00m$
[33mAs always with keymap inheritance, a nil binding in MAPS overrides[39;49;00m$
[33many corresponding binding in PARENT, but it does not override corresponding[39;49;00m$
[33mbindings in other keymaps of MAPS.[39;49;00m$
[33mMAPS can be a list of keymaps or a single keymap.[39;49;00m$
[33mPARENT if non-nil should be a keymap.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m`([31mkeymap[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m,@([34mif[39;49;00m[37m [39;49;00m([32mkeymapp[39;49;00m[37m [39;49;00m[31mmaps[39;49;00m)[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[31mmaps[39;49;00m)[37m [39;49;00m[31mmaps[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m,@[31mparent[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mdefine-key-after[39;49;00m[37m [39;49;00m([31mkeymap[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m[31mdefinition[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mafter[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mAdd binding in KEYMAP for KEY => DEFINITION, right after AFTER's binding.[39;49;00m$
[33mThis is like [39;49;00m[33m`define-key'[39;49;00m[33m except that the binding for KEY is placed[39;49;00m$
[33mjust after the binding for the event AFTER, instead of at the beginning[39;49;00m$
[33mof the map.  Note that AFTER must be an event type (like KEY), NOT a command[39;49;00m$
[33m\([39;49;00m[33mlike DEFINITION).[39;49;00m$
[33m[39;49;00m$
[33mIf AFTER is t or omitted, the new binding goes at the end of the keymap.[39;49;00m$
[33mAFTER should be a single event type--a symbol or a character, not a sequence.[39;49;00m$
[33m[39;49;00m$
[33mBindings are always added before any inherited map.[39;49;00m$
[33m[39;49;00m$
[33mThe order of bindings in a keymap only matters when it is used as[39;49;00m$
[33ma menu, so this function is not useful for non-menu keymaps.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36munless[39;49;00m[37m [39;49;00m[31mafter[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mafter[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mkeymapp[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m([32msignal[39;49;00m[37m [39;49;00m[33m'wrong-type-argument[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'keymapp[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m)))[37m[39;49;00m$
[37m  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00m([34mif[39;49;00m[37m [39;49;00m([32m<=[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31mkey[39;49;00m)[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m([32maref[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m^I  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m[37m [39;49;00m([32mlookup-key[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I   [39;49;00m([32mapply[39;49;00m[37m [39;49;00m[33m'vector[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I^I  [39;49;00m([31mbutlast[39;49;00m[37m [39;49;00m([32mmapcar[39;49;00m[37m [39;49;00m[33m'identity[39;49;00m[37m [39;49;00m[31mkey[39;49;00m)))))[37m[39;49;00m$
[37m^I  [39;49;00m([32maref[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m([32m1-[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31mkey[39;49;00m)))))[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtail[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m)[37m [39;49;00m[31mdone[39;49;00m[37m [39;49;00m[31minserted[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m[31mdone[39;49;00m)[37m [39;49;00m[31mtail[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m[37m;; Delete any earlier bindings for the same key.[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mcar-safe[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)))[37m [39;49;00m[31mkey[39;49;00m)[37m[39;49;00m$
[37m^I  [39;49;00m([32msetcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))))[37m[39;49;00m$
[37m      [39;49;00m[37m;; If we hit an included map, go down that one.[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mkeymapp[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)))[37m[39;49;00m$
[37m      [39;49;00m[37m;; When we reach AFTER's binding, insert the new binding after.[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m[37m;; If we reach an inherited keymap, insert just before that.[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m[37m;; If we reach the end of this keymap, insert at the end.[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mcar-safe[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))[37m [39;49;00m[31mafter[39;49;00m)[37m[39;49;00m$
[37m^I^I   [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mafter[39;49;00m[37m [39;49;00m[31mt[39;49;00m)))[37m[39;49;00m$
[37m^I      [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))[37m [39;49;00m[33m'keymap[39;49;00m)[37m[39;49;00m$
[37m^I      [39;49;00m([32mnull[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)))[37m[39;49;00m$
[37m^I  [39;49;00m([34mprogn[39;49;00m[37m[39;49;00m$
[37m^I    [39;49;00m[37m;; Stop the scan only if we find a parent keymap.[39;49;00m[37m[39;49;00m$
[37m^I    [39;49;00m[37m;; Keep going past the inserted element[39;49;00m[37m[39;49;00m$
[37m^I    [39;49;00m[37m;; so we can delete any duplications that come later.[39;49;00m[37m[39;49;00m$
[37m^I    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))[37m [39;49;00m[33m'keymap[39;49;00m)[37m[39;49;00m$
[37m^I^I[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mdone[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
[37m^I    [39;49;00m[37m;; Don't insert more than once.[39;49;00m[37m[39;49;00m$
[37m^I    [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31minserted[39;49;00m[37m[39;49;00m$
[37m^I^I[39;49;00m([32msetcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m[31mdefinition[39;49;00m)[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))))[37m[39;49;00m$
[37m^I    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31minserted[39;49;00m[37m [39;49;00m[31mt[39;49;00m)))[37m[39;49;00m$
[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mmap-keymap-sorted[39;49;00m[37m [39;49;00m([34mfunction[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mImplement [39;49;00m[33m`map-keymap'[39;49;00m[33m with sorting.[39;49;00m$
[33mDon't call this function; it is for internal use only.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m([32mlist[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([32mmap-keymap[39;49;00m[37m [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31ma[39;49;00m[37m [39;49;00m[31mb[39;49;00m)[37m [39;49;00m([36mpush[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31ma[39;49;00m[37m [39;49;00m[31mb[39;49;00m)[37m [39;49;00m[32mlist[39;49;00m))[37m[39;49;00m$
[37m                [39;49;00m[31mkeymap[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[32mlist[39;49;00m[37m [39;49;00m([32msort[39;49;00m[37m [39;49;00m[32mlist[39;49;00m[37m[39;49;00m$
[37m                     [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31ma[39;49;00m[37m [39;49;00m[31mb[39;49;00m)[37m[39;49;00m$
[37m                       [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31ma[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31ma[39;49;00m)[37m [39;49;00m[31mb[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mb[39;49;00m))[37m[39;49;00m$
[37m                       [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mintegerp[39;49;00m[37m [39;49;00m[31ma[39;49;00m)[37m[39;49;00m$
[37m                           [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mintegerp[39;49;00m[37m [39;49;00m[31mb[39;49;00m)[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m[31ma[39;49;00m[37m [39;49;00m[31mb[39;49;00m)[37m[39;49;00m$
[37m                             [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
[37m                         [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mintegerp[39;49;00m[37m [39;49;00m[31mb[39;49;00m)[37m [39;49;00m[31mt[39;49;00m[37m[39;49;00m$
[37m                           [39;49;00m[37m;; string< also accepts symbols.[39;49;00m[37m[39;49;00m$
[37m                           [39;49;00m([32mstring<[39;49;00m[37m [39;49;00m[31ma[39;49;00m[37m [39;49;00m[31mb[39;49;00m))))))[37m[39;49;00m$
[37m    [39;49;00m([36mdolist[39;49;00m[37m [39;49;00m([31mp[39;49;00m[37m [39;49;00m[32mlist[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[34mfunction[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mp[39;49;00m)[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mp[39;49;00m)))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mkeymap--menu-item-binding[39;49;00m[37m [39;49;00m([31mval[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn the binding part of a menu-item.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mcond[39;49;00m[37m[39;49;00m$
[37m   [39;49;00m(([31mnot[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mval[39;49;00m))[37m [39;49;00m[31mval[39;49;00m)[37m              [39;49;00m[37m;Not a menu-item.[39;49;00m[37m[39;49;00m$
[37m   [39;49;00m(([32meq[39;49;00m[37m [39;49;00m[33m'menu-item[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mval[39;49;00m))[37m[39;49;00m$
[37m    [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mbinding[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m[31mval[39;49;00m))[37m[39;49;00m$
[37m           [39;49;00m([31mplist[39;49;00m[37m [39;49;00m([32mnthcdr[39;49;00m[37m [39;49;00m[34m3[39;49;00m[37m [39;49;00m[31mval[39;49;00m))[37m[39;49;00m$
[37m           [39;49;00m([31mfilter[39;49;00m[37m [39;49;00m([32mplist-get[39;49;00m[37m [39;49;00m[31mplist[39;49;00m[37m [39;49;00m[36m:filter[39;49;00m)))[37m[39;49;00m$
[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mfilter[39;49;00m[37m [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mfilter[39;49;00m[37m [39;49;00m[31mbinding[39;49;00m)[37m[39;49;00m$
[37m        [39;49;00m[31mbinding[39;49;00m)))[37m[39;49;00m$
[37m   [39;49;00m(([34mand[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mval[39;49;00m))[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m([31mcadr[39;49;00m[37m [39;49;00m[31mval[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m([31mcddr[39;49;00m[37m [39;49;00m[31mval[39;49;00m))[37m[39;49;00m$
[37m   [39;49;00m(([32mstringp[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mval[39;49;00m))[37m[39;49;00m$
[37m    [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mval[39;49;00m))[37m[39;49;00m$
[37m   [39;49;00m([31mt[39;49;00m[37m [39;49;00m[31mval[39;49;00m)))[37m                            [39;49;00m[37m;Not a menu-item either.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mkeymap--menu-item-with-binding[39;49;00m[37m [39;49;00m([31mitem[39;49;00m[37m [39;49;00m[31mbinding[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mBuild a menu-item like ITEM but with its binding changed to BINDING.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mcond[39;49;00m[37m[39;49;00m$
[37m   [39;49;00m(([31mnot[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mitem[39;49;00m))[37m [39;49;00m[31mbinding[39;49;00m)[37m^I^I[39;49;00m[37m;Not a menu-item.[39;49;00m[37m[39;49;00m$
[37m   [39;49;00m(([32meq[39;49;00m[37m [39;49;00m[33m'menu-item[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mitem[39;49;00m))[37m[39;49;00m$
[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mitem[39;49;00m[37m [39;49;00m([32mcopy-sequence[39;49;00m[37m [39;49;00m[31mitem[39;49;00m))[37m[39;49;00m$
[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtail[39;49;00m[37m [39;49;00m([32mnthcdr[39;49;00m[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m[31mitem[39;49;00m)))[37m[39;49;00m$
[37m      [39;49;00m([32msetcar[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m[31mbinding[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m[37m;; Remove any potential filter.[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mplist-get[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)[37m [39;49;00m[36m:filter[39;49;00m)[37m[39;49;00m$
[37m          [39;49;00m([32msetcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([32mplist-put[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)[37m [39;49;00m[36m:filter[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))))[37m[39;49;00m$
[37m    [39;49;00m[31mitem[39;49;00m)[37m[39;49;00m$
[37m   [39;49;00m(([34mand[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mitem[39;49;00m))[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m([31mcadr[39;49;00m[37m [39;49;00m[31mitem[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m([32mcons[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mitem[39;49;00m)[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m([31mcadr[39;49;00m[37m [39;49;00m[31mitem[39;49;00m)[37m [39;49;00m[31mbinding[39;49;00m)))[37m[39;49;00m$
[37m   [39;49;00m([31mt[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mitem[39;49;00m)[37m [39;49;00m[31mbinding[39;49;00m))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mkeymap--merge-bindings[39;49;00m[37m [39;49;00m([31mval1[39;49;00m[37m [39;49;00m[31mval2[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mMerge bindings VAL1 and VAL2.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mmap1[39;49;00m[37m [39;49;00m([31mkeymap--menu-item-binding[39;49;00m[37m [39;49;00m[31mval1[39;49;00m))[37m[39;49;00m$
[37m        [39;49;00m([31mmap2[39;49;00m[37m [39;49;00m([31mkeymap--menu-item-binding[39;49;00m[37m [39;49;00m[31mval2[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mkeymapp[39;49;00m[37m [39;49;00m[31mmap1[39;49;00m)[37m [39;49;00m([32mkeymapp[39;49;00m[37m [39;49;00m[31mmap2[39;49;00m)))[37m[39;49;00m$
[37m        [39;49;00m[37m;; There's nothing to merge: val1 takes precedence.[39;49;00m[37m[39;49;00m$
[37m        [39;49;00m[31mval1[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mmap[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'keymap[39;49;00m[37m [39;49;00m[31mmap1[39;49;00m[37m [39;49;00m[31mmap2[39;49;00m))[37m[39;49;00m$
[37m            [39;49;00m([31mitem[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mkeymapp[39;49;00m[37m [39;49;00m[31mval1[39;49;00m)[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mkeymapp[39;49;00m[37m [39;49;00m[31mval2[39;49;00m)[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mval2[39;49;00m)[37m [39;49;00m[31mval1[39;49;00m)))[37m[39;49;00m$
[37m        [39;49;00m([31mkeymap--menu-item-with-binding[39;49;00m[37m [39;49;00m[31mitem[39;49;00m[37m [39;49;00m[31mmap[39;49;00m)))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mkeymap-canonicalize[39;49;00m[37m [39;49;00m([31mmap[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn a simpler equivalent keymap.[39;49;00m$
[33mThis resolves inheritance and redefinitions.  The returned keymap[39;49;00m$
[33mshould behave identically to a copy of KEYMAP w.r.t [39;49;00m[33m`lookup-key'[39;49;00m[33m[39;49;00m$
[33mand use in active keymaps and menus.[39;49;00m$
[33mSubkeymaps may be modified but are not canonicalized.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; FIXME: Problem with the difference between a nil binding[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; that hides a binding in an inherited map and a nil binding that's ignored[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; to let some further binding visible.  Currently a nil binding hides all.[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; FIXME: we may want to carefully (re)order elements in case they're[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; menu-entries.[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mbindings[39;49;00m[37m [39;49;00m())[37m[39;49;00m$
[37m        [39;49;00m([31mranges[39;49;00m[37m [39;49;00m())[37m[39;49;00m$
[37m^I[39;49;00m([31mprompt[39;49;00m[37m [39;49;00m([32mkeymap-prompt[39;49;00m[37m [39;49;00m[31mmap[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32mkeymapp[39;49;00m[37m [39;49;00m[31mmap[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m([32mmap-keymap[39;49;00m[37m [39;49;00m[37m;; -internal[39;49;00m[37m[39;49;00m$
[37m                 [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31mkey[39;49;00m[37m [39;49;00m[31mitem[39;49;00m)[37m[39;49;00m$
[37m                   [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mkey[39;49;00m)[37m[39;49;00m$
[37m                       [39;49;00m[37m;; Treat char-ranges specially.[39;49;00m[37m[39;49;00m$
[37m                       [39;49;00m([36mpush[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m[31mitem[39;49;00m)[37m [39;49;00m[31mranges[39;49;00m)[37m[39;49;00m$
[37m                     [39;49;00m([36mpush[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m[31mitem[39;49;00m)[37m [39;49;00m[31mbindings[39;49;00m)))[37m[39;49;00m$
[37m                 [39;49;00m[31mmap[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m[37m;; Create the new map.[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mranges[39;49;00m[37m [39;49;00m[33m'make-keymap[39;49;00m[37m [39;49;00m[33m'make-sparse-keymap[39;49;00m)[37m [39;49;00m[31mprompt[39;49;00m))[37m[39;49;00m$
[37m    [39;49;00m([36mdolist[39;49;00m[37m [39;49;00m([31mbinding[39;49;00m[37m [39;49;00m[31mranges[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m[37m;; Treat char-ranges specially.  FIXME: need to merge as well.[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([32mdefine-key[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m([32mvector[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mbinding[39;49;00m))[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mbinding[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m[37m;; Process the bindings starting from the end.[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m([36mdolist[39;49;00m[37m [39;49;00m([31mbinding[39;49;00m[37m [39;49;00m([34mprog1[39;49;00m[37m [39;49;00m[31mbindings[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbindings[39;49;00m[37m [39;49;00m())))[37m[39;49;00m$
[37m      [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mkey[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mbinding[39;49;00m))[37m[39;49;00m$
[37m             [39;49;00m([31moldbind[39;49;00m[37m [39;49;00m([32massq[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m[31mbindings[39;49;00m)))[37m[39;49;00m$
[37m        [39;49;00m([36mpush[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m[31moldbind[39;49;00m)[37m[39;49;00m$
[37m                  [39;49;00m[37m;; The normal case: no duplicate bindings.[39;49;00m[37m[39;49;00m$
[37m                  [39;49;00m[31mbinding[39;49;00m[37m[39;49;00m$
[37m                [39;49;00m[37m;; This is the second binding for this key.[39;49;00m[37m[39;49;00m$
[37m                [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbindings[39;49;00m[37m [39;49;00m([32mdelq[39;49;00m[37m [39;49;00m[31moldbind[39;49;00m[37m [39;49;00m[31mbindings[39;49;00m))[37m[39;49;00m$
[37m                [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m([31mkeymap--merge-bindings[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mbinding[39;49;00m)[37m[39;49;00m$
[37m                                                  [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31moldbind[39;49;00m))))[37m[39;49;00m$
[37m              [39;49;00m[31mbindings[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m([32mnconc[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m[31mbindings[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
([32mput[39;49;00m[37m [39;49;00m[33m'keyboard-translate-table[39;49;00m[37m [39;49;00m[33m'char-table-extra-slots[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mkeyboard-translate[39;49;00m[37m [39;49;00m([31mfrom[39;49;00m[37m [39;49;00m[31mto[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mTranslate character FROM to TO on the current terminal.[39;49;00m$
[33mThis function creates a [39;49;00m[33m`keyboard-translate-table'[39;49;00m[33m if necessary[39;49;00m$
[33mand then modifies one entry in it.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mchar-table-p[39;49;00m[37m [39;49;00m[31mkeyboard-translate-table[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mkeyboard-translate-table[39;49;00m[37m[39;49;00m$
[37m^I    [39;49;00m([32mmake-char-table[39;49;00m[37m [39;49;00m[33m'keyboard-translate-table[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)))[37m[39;49;00m$
[37m  [39;49;00m([32maset[39;49;00m[37m [39;49;00m[31mkeyboard-translate-table[39;49;00m[37m [39;49;00m[31mfrom[39;49;00m[37m [39;49;00m[31mto[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m[37m[39;49;00m$
[37m;;;; Key binding commands.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mglobal-set-key[39;49;00m[37m [39;49;00m([31mkey[39;49;00m[37m [39;49;00m[31mcommand[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mGive KEY a global binding as COMMAND.[39;49;00m$
[33mCOMMAND is the command definition to use; usually it is[39;49;00m$
[33ma symbol naming an interactively-callable function.[39;49;00m$
[33mKEY is a key sequence; noninteractively, it is a string or vector[39;49;00m$
[33mof characters or event types, and non-ASCII characters with codes[39;49;00m$
[33mabove 127 (such as ISO Latin-1) can be included if you use a vector.[39;49;00m$
[33m[39;49;00m$
[33mNote that if KEY has a local binding in the current buffer,[39;49;00m$
[33mthat local binding will continue to shadow any global binding[39;49;00m$
[33mthat you make with this function.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34minteractive[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mKSet key globally: [39;49;00m[33m\n[39;49;00m[33mCSet key %s to command: [39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mvectorp[39;49;00m[37m [39;49;00m[31mkey[39;49;00m)[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m[31mkey[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m([32msignal[39;49;00m[37m [39;49;00m[33m'wrong-type-argument[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'arrayp[39;49;00m[37m [39;49;00m[31mkey[39;49;00m)))[37m[39;49;00m$
[37m  [39;49;00m([32mdefine-key[39;49;00m[37m [39;49;00m([32mcurrent-global-map[39;49;00m)[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m[31mcommand[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mlocal-set-key[39;49;00m[37m [39;49;00m([31mkey[39;49;00m[37m [39;49;00m[31mcommand[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mGive KEY a local binding as COMMAND.[39;49;00m$
[33mCOMMAND is the command definition to use; usually it is[39;49;00m$
[33ma symbol naming an interactively-callable function.[39;49;00m$
[33mKEY is a key sequence; noninteractively, it is a string or vector[39;49;00m$
[33mof characters or event types, and non-ASCII characters with codes[39;49;00m$
[33mabove 127 (such as ISO Latin-1) can be included if you use a vector.[39;49;00m$
[33m[39;49;00m$
[33mThe binding goes in the current buffer's local map, which in most[39;49;00m$
[33mcases is shared with all other buffers in the same major mode.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34minteractive[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mKSet key locally: [39;49;00m[33m\n[39;49;00m[33mCSet key %s locally to command: [39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mmap[39;49;00m[37m [39;49;00m([32mcurrent-local-map[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00m([32muse-local-map[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m([32mmake-sparse-keymap[39;49;00m))))[37m[39;49;00m$
[37m    [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mvectorp[39;49;00m[37m [39;49;00m[31mkey[39;49;00m)[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m[31mkey[39;49;00m)[37m[39;49;00m$
[37m^I[39;49;00m([32msignal[39;49;00m[37m [39;49;00m[33m'wrong-type-argument[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'arrayp[39;49;00m[37m [39;49;00m[31mkey[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m([32mdefine-key[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m[31mcommand[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mglobal-unset-key[39;49;00m[37m [39;49;00m([31mkey[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mRemove global binding of KEY.[39;49;00m$
[33mKEY is a string or vector representing a sequence of keystrokes.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34minteractive[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mkUnset key globally: [39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m([31mglobal-set-key[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mlocal-unset-key[39;49;00m[37m [39;49;00m([31mkey[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mRemove local binding of KEY.[39;49;00m$
[33mKEY is a string or vector representing a sequence of keystrokes.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34minteractive[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mkUnset key locally: [39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mcurrent-local-map[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m([31mlocal-set-key[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m[37m[39;49;00m$
[37m;;;; substitute-key-definition and its subroutines.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
([34mdefvar[39;49;00m[37m [39;49;00m[31mkey-substitution-in-progress[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mUsed internally by [39;49;00m[33m`substitute-key-definition'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31msubstitute-key-definition[39;49;00m[37m [39;49;00m([31molddef[39;49;00m[37m [39;49;00m[31mnewdef[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31moldmap[39;49;00m[37m [39;49;00m[31mprefix[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReplace OLDDEF with NEWDEF for any keys in KEYMAP now defined as OLDDEF.[39;49;00m$
[33mIn other words, OLDDEF is replaced with NEWDEF where ever it appears.[39;49;00m$
[33mAlternatively, if optional fourth argument OLDMAP is specified, we redefine[39;49;00m$
[33min KEYMAP as NEWDEF those keys which are defined as OLDDEF in OLDMAP.[39;49;00m$
[33m[39;49;00m$
[33mIf you don't specify OLDMAP, you can usually get the same results[39;49;00m$
[33min a cleaner way with command remapping, like this:[39;49;00m$
[33m  (define-key KEYMAP [remap OLDDEF] NEWDEF)[39;49;00m$
[33m\n[39;49;00m[33m(fn OLDDEF NEWDEF KEYMAP &optional OLDMAP)[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; Don't document PREFIX in the doc string because we don't want to[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; advertise it.  It's meant for recursive calls only.  Here's its[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; meaning[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m  [39;49;00m[37m;; If optional argument PREFIX is specified, it should be a key[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; prefix, a string.  Redefined bindings will then be bound to the[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; original key, with PREFIX added at the front.[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mprefix[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mprefix[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mscan[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31moldmap[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m))[37m[39;49;00m$
[37m^I [39;49;00m([31mprefix1[39;49;00m[37m [39;49;00m([32mvconcat[39;49;00m[37m [39;49;00m[31mprefix[39;49;00m[37m [39;49;00m[[31mnil[39;49;00m]))[37m[39;49;00m$
[37m^I [39;49;00m([31mkey-substitution-in-progress[39;49;00m[37m[39;49;00m$
[37m^I  [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mscan[39;49;00m[37m [39;49;00m[31mkey-substitution-in-progress[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m[37m;; Scan OLDMAP, finding each char or event-symbol that[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[37m;; has any definition, and act on it with hack-key.[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m([32mmap-keymap[39;49;00m[37m[39;49;00m$
[37m     [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31mchar[39;49;00m[37m [39;49;00m[31mdefn[39;49;00m)[37m[39;49;00m$
[37m       [39;49;00m([32maset[39;49;00m[37m [39;49;00m[31mprefix1[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31mprefix[39;49;00m)[37m [39;49;00m[31mchar[39;49;00m)[37m[39;49;00m$
[37m       [39;49;00m([31msubstitute-key-definition-key[39;49;00m[37m [39;49;00m[31mdefn[39;49;00m[37m [39;49;00m[31molddef[39;49;00m[37m [39;49;00m[31mnewdef[39;49;00m[37m [39;49;00m[31mprefix1[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m))[37m[39;49;00m$
[37m     [39;49;00m[31mscan[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31msubstitute-key-definition-key[39;49;00m[37m [39;49;00m([31mdefn[39;49;00m[37m [39;49;00m[31molddef[39;49;00m[37m [39;49;00m[31mnewdef[39;49;00m[37m [39;49;00m[31mprefix[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m([31minner-def[39;49;00m[37m [39;49;00m[31mskipped[39;49;00m[37m [39;49;00m[31mmenu-item[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m[37m;; Find the actual command name within the binding.[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mcar-safe[39;49;00m[37m [39;49;00m[31mdefn[39;49;00m)[37m [39;49;00m[33m'menu-item[39;49;00m)[37m[39;49;00m$
[37m^I[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mmenu-item[39;49;00m[37m [39;49;00m[31mdefn[39;49;00m[37m [39;49;00m[31mdefn[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m[31mdefn[39;49;00m))[37m[39;49;00m$
[37m      [39;49;00m[37m;; Skip past menu-prompt.[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m([32mcar-safe[39;49;00m[37m [39;49;00m[31mdefn[39;49;00m))[37m[39;49;00m$
[37m^I[39;49;00m([36mpush[39;49;00m[37m [39;49;00m([36mpop[39;49;00m[37m [39;49;00m[31mdefn[39;49;00m)[37m [39;49;00m[31mskipped[39;49;00m))[37m[39;49;00m$
[37m      [39;49;00m[37m;; Skip past cached key-equivalence data for menu items.[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m([32mcar-safe[39;49;00m[37m [39;49;00m[31mdefn[39;49;00m))[37m[39;49;00m$
[37m^I  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mdefn[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mdefn[39;49;00m))))[37m[39;49;00m$
[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mdefn[39;49;00m[37m [39;49;00m[31molddef[39;49;00m)[37m[39;49;00m$
[37m^I    [39;49;00m[37m;; Compare with equal if definition is a key sequence.[39;49;00m[37m[39;49;00m$
[37m^I    [39;49;00m[37m;; That is useful for operating on function-key-map.[39;49;00m[37m[39;49;00m$
[37m^I    [39;49;00m([34mand[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m[31mdefn[39;49;00m)[37m [39;49;00m([32mvectorp[39;49;00m[37m [39;49;00m[31mdefn[39;49;00m))[37m[39;49;00m$
[37m^I^I [39;49;00m([32mequal[39;49;00m[37m [39;49;00m[31mdefn[39;49;00m[37m [39;49;00m[31molddef[39;49;00m)))[37m[39;49;00m$
[37m^I[39;49;00m([32mdefine-key[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m[37m [39;49;00m[31mprefix[39;49;00m[37m[39;49;00m$
[37m^I  [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mmenu-item[39;49;00m[37m[39;49;00m$
[37m^I      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mcopy[39;49;00m[37m [39;49;00m([32mcopy-sequence[39;49;00m[37m [39;49;00m[31mmenu-item[39;49;00m)))[37m[39;49;00m$
[37m^I^I[39;49;00m([32msetcar[39;49;00m[37m [39;49;00m([32mnthcdr[39;49;00m[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m[31mcopy[39;49;00m)[37m [39;49;00m[31mnewdef[39;49;00m)[37m[39;49;00m$
[37m^I^I[39;49;00m[31mcopy[39;49;00m)[37m[39;49;00m$
[37m^I    [39;49;00m([32mnconc[39;49;00m[37m [39;49;00m([32mnreverse[39;49;00m[37m [39;49;00m[31mskipped[39;49;00m)[37m [39;49;00m[31mnewdef[39;49;00m)))[37m[39;49;00m$
[37m      [39;49;00m[37m;; Look past a symbol that names a keymap.[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31minner-def[39;49;00m[37m[39;49;00m$
[37m^I    [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mindirect-function[39;49;00m[37m [39;49;00m[31mdefn[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m [39;49;00m[31mdefn[39;49;00m))[37m[39;49;00m$
[37m      [39;49;00m[37m;; For nested keymaps, we use `inner-def' rather than `defn' so as to[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m[37m;; avoid autoloading a keymap.  This is mostly done to preserve the[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m[37m;; original non-autoloading behavior of pre-map-keymap times.[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mkeymapp[39;49;00m[37m [39;49;00m[31minner-def[39;49;00m)[37m[39;49;00m$
[37m^I       [39;49;00m[37m;; Avoid recursively scanning[39;49;00m[37m[39;49;00m$
[37m^I       [39;49;00m[37m;; where KEYMAP does not have a submap.[39;49;00m[37m[39;49;00m$
[37m^I       [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([32melt[39;49;00m[37m [39;49;00m([32mlookup-key[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m[37m [39;49;00m[31mprefix[39;49;00m)))[37m[39;49;00m$
[37m^I^I [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[32melt[39;49;00m)[37m [39;49;00m([32mnatnump[39;49;00m[37m [39;49;00m[32melt[39;49;00m)[37m [39;49;00m([32mkeymapp[39;49;00m[37m [39;49;00m[32melt[39;49;00m)))[37m[39;49;00m$
[37m^I       [39;49;00m[37m;; Avoid recursively rescanning keymap being scanned.[39;49;00m[37m[39;49;00m$
[37m^I       [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[31minner-def[39;49;00m[37m [39;49;00m[31mkey-substitution-in-progress[39;49;00m)))[37m[39;49;00m$
[37m^I  [39;49;00m[37m;; If this one isn't being scanned already, scan it now.[39;49;00m[37m[39;49;00m$
[37m^I  [39;49;00m([31msubstitute-key-definition[39;49;00m[37m [39;49;00m[31molddef[39;49;00m[37m [39;49;00m[31mnewdef[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m[37m [39;49;00m[31minner-def[39;49;00m[37m [39;49;00m[31mprefix[39;49;00m)))))[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m[37m[39;49;00m$
[37m;;;; The global keymap tree.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m;; global-map, esc-map, and ctl-x-map have their values set up in[39;49;00m[37m[39;49;00m$
[37m;; keymap.c; we just give them docstrings here.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
([34mdefvar[39;49;00m[37m [39;49;00m[31mglobal-map[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mDefault global keymap mapping Emacs keyboard input into commands.[39;49;00m$
[33mThe value is a keymap which is usually (but not necessarily) Emacs's[39;49;00m$
[33mglobal map.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
([34mdefvar[39;49;00m[37m [39;49;00m[31mesc-map[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mDefault keymap for ESC (meta) commands.[39;49;00m$
[33mThe normal global definition of the character ESC indirects to this keymap.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
([34mdefvar[39;49;00m[37m [39;49;00m[31mctl-x-map[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mDefault keymap for C-x commands.[39;49;00m$
[33mThe normal global definition of the character C-x indirects to this keymap.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
([34mdefvar[39;49;00m[37m [39;49;00m[31mctl-x-4-map[39;49;00m[37m [39;49;00m([32mmake-sparse-keymap[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mKeymap for subcommands of C-x 4.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([36mdefalias[39;49;00m[37m [39;49;00m[33m'ctl-x-4-prefix[39;49;00m[37m [39;49;00m[31mctl-x-4-map[39;49;00m)[37m[39;49;00m$
([32mdefine-key[39;49;00m[37m [39;49;00m[31mctl-x-map[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m4[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m'ctl-x-4-prefix[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
([34mdefvar[39;49;00m[37m [39;49;00m[31mctl-x-5-map[39;49;00m[37m [39;49;00m([32mmake-sparse-keymap[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mKeymap for frame commands.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([36mdefalias[39;49;00m[37m [39;49;00m[33m'ctl-x-5-prefix[39;49;00m[37m [39;49;00m[31mctl-x-5-map[39;49;00m)[37m[39;49;00m$
([32mdefine-key[39;49;00m[37m [39;49;00m[31mctl-x-map[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m5[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m'ctl-x-5-prefix[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m[37m[39;49;00m$
[37m;;;; Event manipulation functions.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
([34mdefconst[39;49;00m[37m [39;49;00m[31mlistify-key-sequence-1[39;49;00m[37m [39;49;00m([32mlogior[39;49;00m[37m [39;49;00m[34m128[39;49;00m[37m [39;49;00m[33m?\M[39;49;00m[31m-\C-@[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mlistify-key-sequence[39;49;00m[37m [39;49;00m([31mkey[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mConvert a key sequence to a list of events.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mvectorp[39;49;00m[37m [39;49;00m[31mkey[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m([32mappend[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([32mmapcar[39;49;00m[37m [39;49;00m([34mfunction[39;49;00m[37m [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31mc[39;49;00m)[37m[39;49;00m$
[37m^I^I^I[39;49;00m([34mif[39;49;00m[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m[31mc[39;49;00m[37m [39;49;00m[34m127[39;49;00m)[37m[39;49;00m$
[37m^I^I^I    [39;49;00m([32mlogxor[39;49;00m[37m [39;49;00m[31mc[39;49;00m[37m [39;49;00m[31mlistify-key-sequence-1[39;49;00m)[37m[39;49;00m$
[37m^I^I^I  [39;49;00m[31mc[39;49;00m)))[37m[39;49;00m$
[37m^I    [39;49;00m[31mkey[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31meventp[39;49;00m[37m [39;49;00m([31mobj[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mTrue if the argument is an event object.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31mobj[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mintegerp[39;49;00m[37m [39;49;00m[31mobj[39;49;00m)[37m[39;49;00m$
[37m        [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32msymbolp[39;49;00m[37m [39;49;00m[31mobj[39;49;00m)[37m [39;49;00m[31mobj[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mkeywordp[39;49;00m[37m [39;49;00m[31mobj[39;49;00m)))[37m[39;49;00m$
[37m        [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mobj[39;49;00m)[37m [39;49;00m([32msymbolp[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mobj[39;49;00m))))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mevent-modifiers[39;49;00m[37m [39;49;00m([31mevent[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn a list of symbols representing the modifier keys in event EVENT.[39;49;00m$
[33mThe elements of the list may include [39;49;00m[33m`meta'[39;49;00m[33m, [39;49;00m[33m`control'[39;49;00m[33m,[39;49;00m$
[33m`shift'[39;49;00m[33m, [39;49;00m[33m`hyper'[39;49;00m[33m, [39;49;00m[33m`super'[39;49;00m[33m, [39;49;00m[33m`alt'[39;49;00m[33m, [39;49;00m[33m`click'[39;49;00m[33m, [39;49;00m[33m`double'[39;49;00m[33m, [39;49;00m[33m`triple'[39;49;00m[33m, [39;49;00m[33m`drag'[39;49;00m[33m,[39;49;00m$
[33mand [39;49;00m[33m`down'[39;49;00m[33m.[39;49;00m$
[33mEVENT may be an event or an event type.  If EVENT is a symbol[39;49;00m$
[33mthat has never been used in an event that has been read as input[39;49;00m$
[33min the current Emacs session, then this function may fail to include[39;49;00m$
[33mthe [39;49;00m[33m`click'[39;49;00m[33m modifier.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtype[39;49;00m[37m [39;49;00m[31mevent[39;49;00m))[37m[39;49;00m$
[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mlistp[39;49;00m[37m [39;49;00m[31mtype[39;49;00m)[37m[39;49;00m$
[37m^I[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mtype[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mtype[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32msymbolp[39;49;00m[37m [39;49;00m[31mtype[39;49;00m)[37m[39;49;00m$
[37m        [39;49;00m[37m;; Don't read event-symbol-elements directly since we're not[39;49;00m[37m[39;49;00m$
[37m        [39;49;00m[37m;; sure the symbol has already been parsed.[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00m([32mcdr[39;49;00m[37m [39;49;00m([32minternal-event-symbol-parse-modifiers[39;49;00m[37m [39;49;00m[31mtype[39;49;00m))[37m[39;49;00m$
[37m      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([32mlist[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
[37m^I    [39;49;00m([31mchar[39;49;00m[37m [39;49;00m([32mlogand[39;49;00m[37m [39;49;00m[31mtype[39;49;00m[37m [39;49;00m([32mlognot[39;49;00m[37m [39;49;00m([32mlogior[39;49;00m[37m [39;49;00m[33m?\M[39;49;00m[31m-\^@[39;49;00m[37m [39;49;00m[33m?\C[39;49;00m[31m-\^@[39;49;00m[37m [39;49;00m[33m?\S[39;49;00m[31m-\^@[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I^I       [39;49;00m[33m?\H[39;49;00m[31m-\^@[39;49;00m[37m [39;49;00m[33m?\s[39;49;00m[31m-\^@[39;49;00m[37m [39;49;00m[33m?\A[39;49;00m[31m-\^@[39;49;00m)))))[37m[39;49;00m$
[37m^I[39;49;00m([34mif[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([31mzerop[39;49;00m[37m [39;49;00m([32mlogand[39;49;00m[37m [39;49;00m[31mtype[39;49;00m[37m [39;49;00m[33m?\M[39;49;00m[31m-\^@[39;49;00m)))[37m[39;49;00m$
[37m^I    [39;49;00m([36mpush[39;49;00m[37m [39;49;00m[33m'meta[39;49;00m[37m [39;49;00m[32mlist[39;49;00m))[37m[39;49;00m$
[37m^I[39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([31mzerop[39;49;00m[37m [39;49;00m([32mlogand[39;49;00m[37m [39;49;00m[31mtype[39;49;00m[37m [39;49;00m[33m?\C[39;49;00m[31m-\^@[39;49;00m)))[37m[39;49;00m$
[37m^I^I[39;49;00m([32m<[39;49;00m[37m [39;49;00m[31mchar[39;49;00m[37m [39;49;00m[34m32[39;49;00m))[37m[39;49;00m$
[37m^I    [39;49;00m([36mpush[39;49;00m[37m [39;49;00m[33m'control[39;49;00m[37m [39;49;00m[32mlist[39;49;00m))[37m[39;49;00m$
[37m^I[39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([31mzerop[39;49;00m[37m [39;49;00m([32mlogand[39;49;00m[37m [39;49;00m[31mtype[39;49;00m[37m [39;49;00m[33m?\S[39;49;00m[31m-\^@[39;49;00m)))[37m[39;49;00m$
[37m^I^I[39;49;00m([32m/=[39;49;00m[37m [39;49;00m[31mchar[39;49;00m[37m [39;49;00m([32mdowncase[39;49;00m[37m [39;49;00m[31mchar[39;49;00m)))[37m[39;49;00m$
[37m^I    [39;49;00m([36mpush[39;49;00m[37m [39;49;00m[33m'shift[39;49;00m[37m [39;49;00m[32mlist[39;49;00m))[37m[39;49;00m$
[37m^I[39;49;00m([34mor[39;49;00m[37m [39;49;00m([31mzerop[39;49;00m[37m [39;49;00m([32mlogand[39;49;00m[37m [39;49;00m[31mtype[39;49;00m[37m [39;49;00m[33m?\H[39;49;00m[31m-\^@[39;49;00m))[37m[39;49;00m$
[37m^I    [39;49;00m([36mpush[39;49;00m[37m [39;49;00m[33m'hyper[39;49;00m[37m [39;49;00m[32mlist[39;49;00m))[37m[39;49;00m$
[37m^I[39;49;00m([34mor[39;49;00m[37m [39;49;00m([31mzerop[39;49;00m[37m [39;49;00m([32mlogand[39;49;00m[37m [39;49;00m[31mtype[39;49;00m[37m [39;49;00m[33m?\s[39;49;00m[31m-\^@[39;49;00m))[37m[39;49;00m$
[37m^I    [39;49;00m([36mpush[39;49;00m[37m [39;49;00m[33m'super[39;49;00m[37m [39;49;00m[32mlist[39;49;00m))[37m[39;49;00m$
[37m^I[39;49;00m([34mor[39;49;00m[37m [39;49;00m([31mzerop[39;49;00m[37m [39;49;00m([32mlogand[39;49;00m[37m [39;49;00m[31mtype[39;49;00m[37m [39;49;00m[33m?\A[39;49;00m[31m-\^@[39;49;00m))[37m[39;49;00m$
[37m^I    [39;49;00m([36mpush[39;49;00m[37m [39;49;00m[33m'alt[39;49;00m[37m [39;49;00m[32mlist[39;49;00m))[37m[39;49;00m$
[37m^I[39;49;00m[32mlist[39;49;00m))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mevent-basic-type[39;49;00m[37m [39;49;00m([31mevent[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn the basic type of the given event (all modifiers removed).[39;49;00m$
[33mThe value is a printing character (not upper case) or a symbol.[39;49;00m$
[33mEVENT may be an event or an event type.  If EVENT is a symbol[39;49;00m$
[33mthat has never been used in an event that has been read as input[39;49;00m$
[33min the current Emacs session, then this function may return nil.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mevent[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mevent[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mevent[39;49;00m)))[37m[39;49;00m$
[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32msymbolp[39;49;00m[37m [39;49;00m[31mevent[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m([32mcar[39;49;00m[37m [39;49;00m([32mget[39;49;00m[37m [39;49;00m[31mevent[39;49;00m[37m [39;49;00m[33m'event-symbol-elements[39;49;00m))[37m[39;49;00m$
[37m    [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mbase[39;49;00m[37m [39;49;00m([32mlogand[39;49;00m[37m [39;49;00m[31mevent[39;49;00m[37m [39;49;00m([32m1-[39;49;00m[37m [39;49;00m[33m?\A[39;49;00m[31m-\^@[39;49;00m)))[37m[39;49;00m$
[37m^I   [39;49;00m([31muncontrolled[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m[31mbase[39;49;00m[37m [39;49;00m[34m32[39;49;00m)[37m [39;49;00m([32mlogior[39;49;00m[37m [39;49;00m[31mbase[39;49;00m[37m [39;49;00m[34m64[39;49;00m)[37m [39;49;00m[31mbase[39;49;00m)))[37m[39;49;00m$
[37m      [39;49;00m[37m;; There are some numbers that are invalid characters and[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m[37m;; cause `downcase' to get an error.[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([34mcondition-case[39;49;00m[37m [39;49;00m()[37m[39;49;00m$
[37m^I  [39;49;00m([32mdowncase[39;49;00m[37m [39;49;00m[31muncontrolled[39;49;00m)[37m[39;49;00m$
[37m^I[39;49;00m([36merror[39;49;00m[37m [39;49;00m[31muncontrolled[39;49;00m)))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefsubst[39;49;00m[37m [39;49;00m[31mmouse-movement-p[39;49;00m[37m [39;49;00m([31mobject[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn non-nil if OBJECT is a mouse movement event.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mcar-safe[39;49;00m[37m [39;49;00m[31mobject[39;49;00m)[37m [39;49;00m[33m'mouse-movement[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mmouse-event-p[39;49;00m[37m [39;49;00m([31mobject[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn non-nil if OBJECT is a mouse click event.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; is this really correct? maybe remove mouse-movement?[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m([31mevent-basic-type[39;49;00m[37m [39;49;00m[31mobject[39;49;00m)[37m [39;49;00m'([31mmouse-1[39;49;00m[37m [39;49;00m[31mmouse-2[39;49;00m[37m [39;49;00m[31mmouse-3[39;49;00m[37m [39;49;00m[31mmouse-movement[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mevent-start[39;49;00m[37m [39;49;00m([31mevent[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn the starting position of EVENT.[39;49;00m$
[33mEVENT should be a mouse click, drag, or key press event.  If[39;49;00m$
[33mEVENT is nil, the value of [39;49;00m[33m`posn-at-point'[39;49;00m[33m is used instead.[39;49;00m$
[33m[39;49;00m$
[33mThe following accessor functions are used to access the elements[39;49;00m$
[33mof the position:[39;49;00m$
[33m[39;49;00m$
[33m`posn-window'[39;49;00m[33m: The window the event is in.[39;49;00m$
[33m`posn-area'[39;49;00m[33m: A symbol identifying the area the event occurred in,[39;49;00m$
[33mor nil if the event occurred in the text area.[39;49;00m$
[33m`posn-point'[39;49;00m[33m: The buffer position of the event.[39;49;00m$
[33m`posn-x-y'[39;49;00m[33m: The pixel-based coordinates of the event.[39;49;00m$
[33m`posn-col-row'[39;49;00m[33m: The estimated column and row corresponding to the[39;49;00m$
[33mposition of the event.[39;49;00m$
[33m`posn-actual-col-row'[39;49;00m[33m: The actual column and row corresponding to the[39;49;00m$
[33mposition of the event.[39;49;00m$
[33m`posn-string'[39;49;00m[33m: The string object of the event, which is either[39;49;00m$
[33mnil or (STRING . POSITION)'.[39;49;00m$
[33m`posn-image'[39;49;00m[33m: The image object of the event, if any.[39;49;00m$
[33m`posn-object'[39;49;00m[33m: The image or string object of the event, if any.[39;49;00m$
[33m`posn-timestamp'[39;49;00m[33m: The time the event occurred, in milliseconds.[39;49;00m$
[33m[39;49;00m$
[33mFor more information, see Info node [39;49;00m[33m`[39;49;00m[33m(elisp)Click Events'.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mevent[39;49;00m)[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mevent[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mposn-at-point[39;49;00m)[37m[39;49;00m$
[37m        [39;49;00m([32mlist[39;49;00m[37m [39;49;00m([32mselected-window[39;49;00m)[37m [39;49;00m([32mpoint[39;49;00m)[37m [39;49;00m'([34m0[39;49;00m[37m [39;49;00m.[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34m0[39;49;00m))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mevent-end[39;49;00m[37m [39;49;00m([31mevent[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn the ending position of EVENT.[39;49;00m$
[33mEVENT should be a click, drag, or key press event.[39;49;00m$
[33m[39;49;00m$
[33mSee [39;49;00m[33m`event-start'[39;49;00m[33m for a description of the value returned.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mevent[39;49;00m)[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m[31mevent[39;49;00m))[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m[31mevent[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mposn-at-point[39;49;00m)[37m[39;49;00m$
[37m        [39;49;00m([32mlist[39;49;00m[37m [39;49;00m([32mselected-window[39;49;00m)[37m [39;49;00m([32mpoint[39;49;00m)[37m [39;49;00m'([34m0[39;49;00m[37m [39;49;00m.[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34m0[39;49;00m))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefsubst[39;49;00m[37m [39;49;00m[31mevent-click-count[39;49;00m[37m [39;49;00m([31mevent[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn the multi-click count of EVENT, a click or drag event.[39;49;00m$
[33mThe return value is a positive integer.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mevent[39;49;00m)[37m [39;49;00m([32mintegerp[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m[31mevent[39;49;00m)))[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m[31mevent[39;49;00m)[37m [39;49;00m[34m1[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m[37m[39;49;00m$
[37m;;;; Extracting fields of the positions in an event.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mposnp[39;49;00m[37m [39;49;00m([31mobj[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn non-nil if OBJ appears to be a valid [39;49;00m[33m`posn'[39;49;00m[33m object specifying a window.[39;49;00m$
[33mIf OBJ is a valid [39;49;00m[33m`posn'[39;49;00m[33m object, but specifies a frame rather[39;49;00m$
[33mthan a window, return nil.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; FIXME: Correct the behavior of this function so that all valid[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; `posn' objects are recognized, after updating other code that[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; depends on its present behavior.[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mwindowp[39;49;00m[37m [39;49;00m([32mcar-safe[39;49;00m[37m [39;49;00m[31mobj[39;49;00m))[37m[39;49;00m$
[37m       [39;49;00m([32matom[39;49;00m[37m [39;49;00m([32mcar-safe[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mobj[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mobj[39;49;00m))))[37m                [39;49;00m[37m;AREA-OR-POS.[39;49;00m[37m[39;49;00m$
[37m       [39;49;00m([32mintegerp[39;49;00m[37m [39;49;00m([32mcar-safe[39;49;00m[37m [39;49;00m([32mcar-safe[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mobj[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mobj[39;49;00m)))))[37m [39;49;00m[37m;XOFFSET.[39;49;00m[37m[39;49;00m$
[37m       [39;49;00m([32mintegerp[39;49;00m[37m [39;49;00m([32mcar-safe[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mobj[39;49;00m)))))[37m                     [39;49;00m[37m;TIMESTAMP.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
([36mdefsubst[39;49;00m[37m [39;49;00m[31mposn-window[39;49;00m[37m [39;49;00m([31mposition[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn the window in POSITION.[39;49;00m$
[33mPOSITION should be a list of the form returned by the [39;49;00m[33m`event-start'[39;49;00m[33m[39;49;00m$
[33mand [39;49;00m[33m`event-end'[39;49;00m[33m functions.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[31mposition[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefsubst[39;49;00m[37m [39;49;00m[31mposn-area[39;49;00m[37m [39;49;00m([31mposition[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn the window area recorded in POSITION, or nil for the text area.[39;49;00m$
[33mPOSITION should be a list of the form returned by the [39;49;00m[33m`event-start'[39;49;00m[33m[39;49;00m$
[33mand [39;49;00m[33m`event-end'[39;49;00m[33m functions.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31marea[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mposition[39;49;00m))[37m[39;49;00m$
[37m^I^I  [39;49;00m([32mcar[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mposition[39;49;00m))[37m[39;49;00m$
[37m^I^I[39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mposition[39;49;00m))))[37m[39;49;00m$
[37m    [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32msymbolp[39;49;00m[37m [39;49;00m[31marea[39;49;00m)[37m [39;49;00m[31marea[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mposn-point[39;49;00m[37m [39;49;00m([31mposition[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn the buffer location in POSITION.[39;49;00m$
[33mPOSITION should be a list of the form returned by the [39;49;00m[33m`event-start'[39;49;00m[33m[39;49;00m$
[33mand [39;49;00m[33m`event-end'[39;49;00m[33m functions.[39;49;00m$
[33mReturns nil if POSITION does not correspond to any buffer location (e.g.[39;49;00m$
[33ma click on a scroll bar).[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m5[39;49;00m[37m [39;49;00m[31mposition[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mpt[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mposition[39;49;00m)))[37m[39;49;00m$
[37m        [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mcar-safe[39;49;00m[37m [39;49;00m[31mpt[39;49;00m)[37m[39;49;00m$
[37m            [39;49;00m[37m;; Apparently this can also be `vertical-scroll-bar' (bug#13979).[39;49;00m[37m[39;49;00m$
[37m            [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mintegerp[39;49;00m[37m [39;49;00m[31mpt[39;49;00m)[37m [39;49;00m[31mpt[39;49;00m)))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mposn-set-point[39;49;00m[37m [39;49;00m([31mposition[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mMove point to POSITION.[39;49;00m$
[33mSelect the corresponding window as well.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mwindowp[39;49;00m[37m [39;49;00m([31mposn-window[39;49;00m[37m [39;49;00m[31mposition[39;49;00m)))[37m[39;49;00m$
[37m      [39;49;00m([36merror[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mPosition not in text area of window[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m([32mselect-window[39;49;00m[37m [39;49;00m([31mposn-window[39;49;00m[37m [39;49;00m[31mposition[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mnumberp[39;49;00m[37m [39;49;00m([31mposn-point[39;49;00m[37m [39;49;00m[31mposition[39;49;00m))[37m[39;49;00m$
[37m      [39;49;00m([32mgoto-char[39;49;00m[37m [39;49;00m([31mposn-point[39;49;00m[37m [39;49;00m[31mposition[39;49;00m))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefsubst[39;49;00m[37m [39;49;00m[31mposn-x-y[39;49;00m[37m [39;49;00m([31mposition[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn the x and y coordinates in POSITION.[39;49;00m$
[33mThe return value has the form (X . Y), where X and Y are given in[39;49;00m$
[33mpixels.  POSITION should be a list of the form returned by[39;49;00m$
[33m`event-start'[39;49;00m[33m and [39;49;00m[33m`event-end'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m[31mposition[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
([36mdeclare-function[39;49;00m[37m [39;49;00m[31mscroll-bar-scale[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mscroll-bar[39;49;00m[33m"[39;49;00m[37m [39;49;00m([31mnum-denom[39;49;00m[37m [39;49;00m[31mwhole[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mposn-col-row[39;49;00m[37m [39;49;00m([31mposition[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn the nominal column and row in POSITION, measured in characters.[39;49;00m$
[33mThe column and row values are approximations calculated from the x[39;49;00m$
[33mand y coordinates in POSITION and the frame's default character width[39;49;00m$
[33mand default line height, including spacing.[39;49;00m$
[33mFor a scroll-bar event, the result column is 0, and the row[39;49;00m$
[33mcorresponds to the vertical position of the click in the scroll bar.[39;49;00m$
[33mPOSITION should be a list of the form returned by the [39;49;00m[33m`event-start'[39;49;00m[33m[39;49;00m$
[33mand [39;49;00m[33m`event-end'[39;49;00m[33m functions.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mpair[39;49;00m[37m            [39;49;00m([31mposn-x-y[39;49;00m[37m [39;49;00m[31mposition[39;49;00m))[37m[39;49;00m$
[37m         [39;49;00m([31mframe-or-window[39;49;00m[37m [39;49;00m([31mposn-window[39;49;00m[37m [39;49;00m[31mposition[39;49;00m))[37m[39;49;00m$
[37m         [39;49;00m([31mframe[39;49;00m[37m           [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mframep[39;49;00m[37m [39;49;00m[31mframe-or-window[39;49;00m)[37m[39;49;00m$
[37m                              [39;49;00m[31mframe-or-window[39;49;00m[37m[39;49;00m$
[37m                            [39;49;00m([32mwindow-frame[39;49;00m[37m [39;49;00m[31mframe-or-window[39;49;00m)))[37m[39;49;00m$
[37m         [39;49;00m([31mwindow[39;49;00m[37m          [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mwindowp[39;49;00m[37m [39;49;00m[31mframe-or-window[39;49;00m)[37m [39;49;00m[31mframe-or-window[39;49;00m))[37m[39;49;00m$
[37m         [39;49;00m([31marea[39;49;00m[37m            [39;49;00m([31mposn-area[39;49;00m[37m [39;49;00m[31mposition[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m([34mcond[39;49;00m[37m[39;49;00m$
[37m     [39;49;00m(([32mnull[39;49;00m[37m [39;49;00m[31mframe-or-window[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m'([34m0[39;49;00m[37m [39;49;00m.[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m$
[37m     [39;49;00m(([32meq[39;49;00m[37m [39;49;00m[31marea[39;49;00m[37m [39;49;00m[33m'vertical-scroll-bar[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m([31mscroll-bar-scale[39;49;00m[37m [39;49;00m[31mpair[39;49;00m[37m [39;49;00m([32m1-[39;49;00m[37m [39;49;00m([31mwindow-height[39;49;00m[37m [39;49;00m[31mwindow[39;49;00m)))))[37m[39;49;00m$
[37m     [39;49;00m(([32meq[39;49;00m[37m [39;49;00m[31marea[39;49;00m[37m [39;49;00m[33m'horizontal-scroll-bar[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m([32mcons[39;49;00m[37m [39;49;00m([31mscroll-bar-scale[39;49;00m[37m [39;49;00m[31mpair[39;49;00m[37m [39;49;00m([31mwindow-width[39;49;00m[37m [39;49;00m[31mwindow[39;49;00m))[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m$
[37m     [39;49;00m([31mt[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m[37m;; FIXME: This should take line-spacing properties on[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m[37m;; newlines into account.[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mspacing[39;49;00m[37m [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([31mdisplay-graphic-p[39;49;00m[37m [39;49;00m[31mframe[39;49;00m)[37m[39;49;00m$
[37m                        [39;49;00m([34mor[39;49;00m[37m [39;49;00m([36mwith-current-buffer[39;49;00m[37m[39;49;00m$
[37m                                [39;49;00m([32mwindow-buffer[39;49;00m[37m [39;49;00m([32mframe-selected-window[39;49;00m[37m [39;49;00m[31mframe[39;49;00m))[37m[39;49;00m$
[37m                              [39;49;00m[31mline-spacing[39;49;00m)[37m[39;49;00m$
[37m                            [39;49;00m([32mframe-parameter[39;49;00m[37m [39;49;00m[31mframe[39;49;00m[37m [39;49;00m[33m'line-spacing[39;49;00m)))))[37m[39;49;00m$
[37m^I[39;49;00m([34mcond[39;49;00m[37m [39;49;00m(([32mfloatp[39;49;00m[37m [39;49;00m[31mspacing[39;49;00m)[37m[39;49;00m$
[37m^I       [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mspacing[39;49;00m[37m [39;49;00m([32mtruncate[39;49;00m[37m [39;49;00m([32m*[39;49;00m[37m [39;49;00m[31mspacing[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I^I  [39;49;00m([32mframe-char-height[39;49;00m[37m [39;49;00m[31mframe[39;49;00m)))))[37m[39;49;00m$
[37m^I      [39;49;00m(([32mnull[39;49;00m[37m [39;49;00m[31mspacing[39;49;00m)[37m[39;49;00m$
[37m^I       [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mspacing[39;49;00m[37m [39;49;00m[34m0[39;49;00m)))[37m[39;49;00m$
[37m^I[39;49;00m([32mcons[39;49;00m[37m [39;49;00m([32m/[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mpair[39;49;00m)[37m [39;49;00m([32mframe-char-width[39;49;00m[37m [39;49;00m[31mframe[39;49;00m))[37m[39;49;00m$
[37m^I      [39;49;00m([32m/[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mpair[39;49;00m)[37m [39;49;00m([32m+[39;49;00m[37m [39;49;00m([32mframe-char-height[39;49;00m[37m [39;49;00m[31mframe[39;49;00m)[37m [39;49;00m[31mspacing[39;49;00m))))))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mposn-actual-col-row[39;49;00m[37m [39;49;00m([31mposition[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn the window row number in POSITION and character number in that row.[39;49;00m$
[33m[39;49;00m$
[33mReturn nil if POSITION does not contain the actual position; in that case[39;49;00m$
[33m\`[39;49;00m[33mposn-col-row' can be used to get approximate values.[39;49;00m$
[33mPOSITION should be a list of the form returned by the [39;49;00m[33m`event-start'[39;49;00m[33m[39;49;00m$
[33mand [39;49;00m[33m`event-end'[39;49;00m[33m functions.[39;49;00m$
[33m[39;49;00m$
[33mThis function does not account for the width on display, like the[39;49;00m$
[33mnumber of visual columns taken by a TAB or image.  If you need[39;49;00m$
[33mthe coordinates of POSITION in character units, you should use[39;49;00m$
[33m\`[39;49;00m[33mposn-col-row', not this function.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m6[39;49;00m[37m [39;49;00m[31mposition[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefsubst[39;49;00m[37m [39;49;00m[31mposn-timestamp[39;49;00m[37m [39;49;00m([31mposition[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn the timestamp of POSITION.[39;49;00m$
[33mPOSITION should be a list of the form returned by the [39;49;00m[33m`event-start'[39;49;00m[33m[39;49;00m$
[33mand [39;49;00m[33m`event-end'[39;49;00m[33m functions.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m3[39;49;00m[37m [39;49;00m[31mposition[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mposn-string[39;49;00m[37m [39;49;00m([31mposition[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn the string object of POSITION.[39;49;00m$
[33mValue is a cons (STRING . STRING-POS), or nil if not a string.[39;49;00m$
[33mPOSITION should be a list of the form returned by the [39;49;00m[33m`event-start'[39;49;00m[33m[39;49;00m$
[33mand [39;49;00m[33m`event-end'[39;49;00m[33m functions.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mx[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m4[39;49;00m[37m [39;49;00m[31mposition[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m[37m;; Apparently this can also be `handle' or `below-handle' (bug#13979).[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mx[39;49;00m)[37m [39;49;00m[31mx[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefsubst[39;49;00m[37m [39;49;00m[31mposn-image[39;49;00m[37m [39;49;00m([31mposition[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn the image object of POSITION.[39;49;00m$
[33mValue is a list (image ...), or nil if not an image.[39;49;00m$
[33mPOSITION should be a list of the form returned by the [39;49;00m[33m`event-start'[39;49;00m[33m[39;49;00m$
[33mand [39;49;00m[33m`event-end'[39;49;00m[33m functions.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m7[39;49;00m[37m [39;49;00m[31mposition[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefsubst[39;49;00m[37m [39;49;00m[31mposn-object[39;49;00m[37m [39;49;00m([31mposition[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn the object (image or string) of POSITION.[39;49;00m$
[33mValue is a list (image ...) for an image object, a cons cell[39;49;00m$
[33m\([39;49;00m[33mSTRING . STRING-POS) for a string object, and nil for a buffer position.[39;49;00m$
[33mPOSITION should be a list of the form returned by the [39;49;00m[33m`event-start'[39;49;00m[33m[39;49;00m$
[33mand [39;49;00m[33m`event-end'[39;49;00m[33m functions.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mor[39;49;00m[37m [39;49;00m([31mposn-image[39;49;00m[37m [39;49;00m[31mposition[39;49;00m)[37m [39;49;00m([31mposn-string[39;49;00m[37m [39;49;00m[31mposition[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefsubst[39;49;00m[37m [39;49;00m[31mposn-object-x-y[39;49;00m[37m [39;49;00m([31mposition[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn the x and y coordinates relative to the object of POSITION.[39;49;00m$
[33mThe return value has the form (DX . DY), where DX and DY are[39;49;00m$
[33mgiven in pixels.  POSITION should be a list of the form returned[39;49;00m$
[33mby [39;49;00m[33m`event-start'[39;49;00m[33m and [39;49;00m[33m`event-end'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m8[39;49;00m[37m [39;49;00m[31mposition[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefsubst[39;49;00m[37m [39;49;00m[31mposn-object-width-height[39;49;00m[37m [39;49;00m([31mposition[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn the pixel width and height of the object of POSITION.[39;49;00m$
[33mThe return value has the form (WIDTH . HEIGHT).  POSITION should[39;49;00m$
[33mbe a list of the form returned by [39;49;00m[33m`event-start'[39;49;00m[33m and [39;49;00m[33m`event-end'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m9[39;49;00m[37m [39;49;00m[31mposition[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m[37m[39;49;00m$
[37m;;;; Obsolescent names for functions.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
([36mdefine-obsolete-function-alias[39;49;00m[37m [39;49;00m[33m'window-dot[39;49;00m[37m [39;49;00m[33m'window-point[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m22.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([36mdefine-obsolete-function-alias[39;49;00m[37m [39;49;00m[33m'set-window-dot[39;49;00m[37m [39;49;00m[33m'set-window-point[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m22.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([36mdefine-obsolete-function-alias[39;49;00m[37m [39;49;00m[33m'read-input[39;49;00m[37m [39;49;00m[33m'read-string[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m22.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([36mdefine-obsolete-function-alias[39;49;00m[37m [39;49;00m[33m'show-buffer[39;49;00m[37m [39;49;00m[33m'set-window-buffer[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m22.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([36mdefine-obsolete-function-alias[39;49;00m[37m [39;49;00m[33m'eval-current-buffer[39;49;00m[37m [39;49;00m[33m'eval-buffer[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m22.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([36mdefine-obsolete-function-alias[39;49;00m[37m [39;49;00m[33m'string-to-int[39;49;00m[37m [39;49;00m[33m'string-to-number[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m22.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
([31mmake-obsolete[39;49;00m[37m [39;49;00m[33m'forward-point[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33muse (+ (point) N) instead.[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([31mmake-obsolete[39;49;00m[37m [39;49;00m[33m'buffer-has-markers-at[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m24.3[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31minsert-string[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31margs[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mMocklisp-compatibility insert function.[39;49;00m$
[33mLike the function [39;49;00m[33m`insert'[39;49;00m[33m except that any argument that is a number[39;49;00m$
[33mis converted into a string by expressing it in decimal.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mobsolete[39;49;00m[37m [39;49;00m[32minsert[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m22.1[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m([36mdolist[39;49;00m[37m [39;49;00m([31mel[39;49;00m[37m [39;49;00m[31margs[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([32minsert[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mintegerp[39;49;00m[37m [39;49;00m[31mel[39;49;00m)[37m [39;49;00m([32mnumber-to-string[39;49;00m[37m [39;49;00m[31mel[39;49;00m)[37m [39;49;00m[31mel[39;49;00m))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mmakehash[39;49;00m[37m [39;49;00m([34m&optional[39;49;00m[37m [39;49;00m[31mtest[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mobsolete[39;49;00m[37m [39;49;00m[32mmake-hash-table[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m22.1[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m([32mmake-hash-table[39;49;00m[37m [39;49;00m[36m:test[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mtest[39;49;00m[37m [39;49;00m[33m'eql[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mlog10[39;49;00m[37m [39;49;00m([31mx[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn (log X 10), the log base 10 of X.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mobsolete[39;49;00m[37m [39;49;00m[32mlog[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m24.4[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m([32mlog[39;49;00m[37m [39;49;00m[31mx[39;49;00m[37m [39;49;00m[34m10[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
[37m;; These are used by VM and some old programs[39;49;00m[37m[39;49;00m$
([36mdefalias[39;49;00m[37m [39;49;00m[33m'focus-frame[39;49;00m[37m [39;49;00m[33m'ignore[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([31mmake-obsolete[39;49;00m[37m [39;49;00m[33m'focus-frame[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mit does nothing.[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m22.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([36mdefalias[39;49;00m[37m [39;49;00m[33m'unfocus-frame[39;49;00m[37m [39;49;00m[33m'ignore[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([31mmake-obsolete[39;49;00m[37m [39;49;00m[33m'unfocus-frame[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mit does nothing.[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m22.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([31mmake-obsolete[39;49;00m[37m [39;49;00m[33m'make-variable-frame-local[39;49;00m[37m[39;49;00m$
[37m^I       [39;49;00m[33m"[39;49;00m[33mexplicitly check for a frame-parameter instead.[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m22.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([31mset-advertised-calling-convention[39;49;00m[37m[39;49;00m$
[37m [39;49;00m[33m'all-completions[39;49;00m[37m [39;49;00m'([32mstring[39;49;00m[37m [39;49;00m[31mcollection[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mpredicate[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m23.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([31mset-advertised-calling-convention[39;49;00m[37m [39;49;00m[33m'unintern[39;49;00m[37m [39;49;00m'([31mname[39;49;00m[37m [39;49;00m[31mobarray[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m23.3[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([31mset-advertised-calling-convention[39;49;00m[37m [39;49;00m[33m'indirect-function[39;49;00m[37m [39;49;00m'([31mobject[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m25.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([31mset-advertised-calling-convention[39;49;00m[37m [39;49;00m[33m'redirect-frame-focus[39;49;00m[37m [39;49;00m'([31mframe[39;49;00m[37m [39;49;00m[31mfocus-frame[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m24.3[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([31mset-advertised-calling-convention[39;49;00m[37m [39;49;00m[33m'decode-char[39;49;00m[37m [39;49;00m'([31mch[39;49;00m[37m [39;49;00m[31mcharset[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m21.4[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([31mset-advertised-calling-convention[39;49;00m[37m [39;49;00m[33m'encode-char[39;49;00m[37m [39;49;00m'([31mch[39;49;00m[37m [39;49;00m[31mcharset[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m21.4[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m[37m[39;49;00m$
[37m;;;; Obsolescence declarations for variables, and aliases.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m;; Special "default-FOO" variables which contain the default value of[39;49;00m[37m[39;49;00m$
[37m;; the "FOO" variable are nasty.  Their implementation is brittle, and[39;49;00m[37m[39;49;00m$
[37m;; slows down several unrelated variable operations; furthermore, they[39;49;00m[37m[39;49;00m$
[37m;; can lead to really odd behavior if you decide to make them[39;49;00m[37m[39;49;00m$
[37m;; buffer-local.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m;; Not used at all in Emacs, last time I checked:[39;49;00m[37m[39;49;00m$
([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-mode-line-format[39;49;00m[37m [39;49;00m[33m'mode-line-format[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-header-line-format[39;49;00m[37m [39;49;00m[33m'header-line-format[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-line-spacing[39;49;00m[37m [39;49;00m[33m'line-spacing[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-abbrev-mode[39;49;00m[37m [39;49;00m[33m'abbrev-mode[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-ctl-arrow[39;49;00m[37m [39;49;00m[33m'ctl-arrow[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-truncate-lines[39;49;00m[37m [39;49;00m[33m'truncate-lines[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-left-margin[39;49;00m[37m [39;49;00m[33m'left-margin[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-tab-width[39;49;00m[37m [39;49;00m[33m'tab-width[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-case-fold-search[39;49;00m[37m [39;49;00m[33m'case-fold-search[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-left-margin-width[39;49;00m[37m [39;49;00m[33m'left-margin-width[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-right-margin-width[39;49;00m[37m [39;49;00m[33m'right-margin-width[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-left-fringe-width[39;49;00m[37m [39;49;00m[33m'left-fringe-width[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-right-fringe-width[39;49;00m[37m [39;49;00m[33m'right-fringe-width[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-fringes-outside-margins[39;49;00m[37m [39;49;00m[33m'fringes-outside-margins[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-scroll-bar-width[39;49;00m[37m [39;49;00m[33m'scroll-bar-width[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-vertical-scroll-bar[39;49;00m[37m [39;49;00m[33m'vertical-scroll-bar[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-indicate-empty-lines[39;49;00m[37m [39;49;00m[33m'indicate-empty-lines[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-indicate-buffer-boundaries[39;49;00m[37m [39;49;00m[33m'indicate-buffer-boundaries[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-fringe-indicator-alist[39;49;00m[37m [39;49;00m[33m'fringe-indicator-alist[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-fringe-cursor-alist[39;49;00m[37m [39;49;00m[33m'fringe-cursor-alist[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-scroll-up-aggressively[39;49;00m[37m [39;49;00m[33m'scroll-up-aggressively[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-scroll-down-aggressively[39;49;00m[37m [39;49;00m[33m'scroll-down-aggressively[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-fill-column[39;49;00m[37m [39;49;00m[33m'fill-column[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-cursor-type[39;49;00m[37m [39;49;00m[33m'cursor-type[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-cursor-in-non-selected-windows[39;49;00m[37m [39;49;00m[33m'cursor-in-non-selected-windows[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-buffer-file-coding-system[39;49;00m[37m [39;49;00m[33m'buffer-file-coding-system[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-major-mode[39;49;00m[37m [39;49;00m[33m'major-mode[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'default-enable-multibyte-characters[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m[33m"[39;49;00m[33muse enable-multibyte-characters or set-buffer-multibyte instead[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'define-key-rebound-commands[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'redisplay-end-trigger-functions[39;49;00m[37m [39;49;00m[33m'jit-lock-register[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'deferred-action-list[39;49;00m[37m [39;49;00m[33m'post-command-hook[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m24.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'deferred-action-function[39;49;00m[37m [39;49;00m[33m'post-command-hook[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m24.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'redisplay-dont-pause[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m24.5[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([31mmake-obsolete[39;49;00m[37m [39;49;00m[33m'window-redisplay-end-trigger[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([31mmake-obsolete[39;49;00m[37m [39;49;00m[33m'set-window-redisplay-end-trigger[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
([31mmake-obsolete[39;49;00m[37m [39;49;00m[33m'process-filter-multibyte-p[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([31mmake-obsolete[39;49;00m[37m [39;49;00m[33m'set-process-filter-multibyte[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
[37m;; Lisp manual only updated in 22.1.[39;49;00m[37m[39;49;00m$
([36mdefine-obsolete-variable-alias[39;49;00m[37m [39;49;00m[33m'executing-macro[39;49;00m[37m [39;49;00m[33m'executing-kbd-macro[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mbefore 19.34[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
([36mdefine-obsolete-variable-alias[39;49;00m[37m [39;49;00m[33m'x-lost-selection-hooks[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[33m'x-lost-selection-functions[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m22.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([36mdefine-obsolete-variable-alias[39;49;00m[37m [39;49;00m[33m'x-sent-selection-hooks[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[33m'x-sent-selection-functions[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m22.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
[37m;; This was introduced in 21.4 for pre-unicode unification.  That[39;49;00m[37m[39;49;00m$
[37m;; usage was rendered obsolete in 23.1 which uses Unicode internally.[39;49;00m[37m[39;49;00m$
[37m;; Other uses are possible, so this variable is not _really_ obsolete,[39;49;00m[37m[39;49;00m$
[37m;; but Stefan insists to mark it so.[39;49;00m[37m[39;49;00m$
([31mmake-obsolete-variable[39;49;00m[37m [39;49;00m[33m'translation-table-for-input[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
([36mdefvaralias[39;49;00m[37m [39;49;00m[33m'messages-buffer-max-lines[39;49;00m[37m [39;49;00m[33m'message-log-max[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m[37m[39;49;00m$
[37m;;;; Alternate names for functions - these are not being phased out.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
([36mdefalias[39;49;00m[37m [39;49;00m[33m'send-string[39;49;00m[37m [39;49;00m[33m'process-send-string[39;49;00m)[37m[39;49;00m$
([36mdefalias[39;49;00m[37m [39;49;00m[33m'send-region[39;49;00m[37m [39;49;00m[33m'process-send-region[39;49;00m)[37m[39;49;00m$
([36mdefalias[39;49;00m[37m [39;49;00m[33m'string=[39;49;00m[37m [39;49;00m[33m'string-equal[39;49;00m)[37m[39;49;00m$
([36mdefalias[39;49;00m[37m [39;49;00m[33m'string<[39;49;00m[37m [39;49;00m[33m'string-lessp[39;49;00m)[37m[39;49;00m$
([36mdefalias[39;49;00m[37m [39;49;00m[33m'move-marker[39;49;00m[37m [39;49;00m[33m'set-marker[39;49;00m)[37m[39;49;00m$
([36mdefalias[39;49;00m[37m [39;49;00m[33m'rplaca[39;49;00m[37m [39;49;00m[33m'setcar[39;49;00m)[37m[39;49;00m$
([36mdefalias[39;49;00m[37m [39;49;00m[33m'rplacd[39;49;00m[37m [39;49;00m[33m'setcdr[39;49;00m)[37m[39;49;00m$
([36mdefalias[39;49;00m[37m [39;49;00m[33m'beep[39;49;00m[37m [39;49;00m[33m'ding[39;49;00m)[37m [39;49;00m[37m;preserve lingual purity[39;49;00m[37m[39;49;00m$
([36mdefalias[39;49;00m[37m [39;49;00m[33m'indent-to-column[39;49;00m[37m [39;49;00m[33m'indent-to[39;49;00m)[37m[39;49;00m$
([36mdefalias[39;49;00m[37m [39;49;00m[33m'backward-delete-char[39;49;00m[37m [39;49;00m[33m'delete-backward-char[39;49;00m)[37m[39;49;00m$
([36mdefalias[39;49;00m[37m [39;49;00m[33m'search-forward-regexp[39;49;00m[37m [39;49;00m([32msymbol-function[39;49;00m[37m [39;49;00m[33m're-search-forward[39;49;00m))[37m[39;49;00m$
([36mdefalias[39;49;00m[37m [39;49;00m[33m'search-backward-regexp[39;49;00m[37m [39;49;00m([32msymbol-function[39;49;00m[37m [39;49;00m[33m're-search-backward[39;49;00m))[37m[39;49;00m$
([36mdefalias[39;49;00m[37m [39;49;00m[33m'int-to-string[39;49;00m[37m [39;49;00m[33m'number-to-string[39;49;00m)[37m[39;49;00m$
([36mdefalias[39;49;00m[37m [39;49;00m[33m'store-match-data[39;49;00m[37m [39;49;00m[33m'set-match-data[39;49;00m)[37m[39;49;00m$
([36mdefalias[39;49;00m[37m [39;49;00m[33m'chmod[39;49;00m[37m [39;49;00m[33m'set-file-modes[39;49;00m)[37m[39;49;00m$
([36mdefalias[39;49;00m[37m [39;49;00m[33m'mkdir[39;49;00m[37m [39;49;00m[33m'make-directory[39;49;00m)[37m[39;49;00m$
[37m;; These are the XEmacs names:[39;49;00m[37m[39;49;00m$
([36mdefalias[39;49;00m[37m [39;49;00m[33m'point-at-eol[39;49;00m[37m [39;49;00m[33m'line-end-position[39;49;00m)[37m[39;49;00m$
([36mdefalias[39;49;00m[37m [39;49;00m[33m'point-at-bol[39;49;00m[37m [39;49;00m[33m'line-beginning-position[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
([36mdefalias[39;49;00m[37m [39;49;00m[33m'user-original-login-name[39;49;00m[37m [39;49;00m[33m'user-login-name[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m[37m[39;49;00m$
[37m;;;; Hook manipulation functions.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31madd-hook[39;49;00m[37m [39;49;00m([31mhook[39;49;00m[37m [39;49;00m[34mfunction[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[32mappend[39;49;00m[37m [39;49;00m[31mlocal[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mAdd to the value of HOOK the function FUNCTION.[39;49;00m$
[33mFUNCTION is not added if already present.[39;49;00m$
[33mFUNCTION is added (if necessary) at the beginning of the hook list[39;49;00m$
[33munless the optional argument APPEND is non-nil, in which case[39;49;00m$
[33mFUNCTION is added at the end.[39;49;00m$
[33m[39;49;00m$
[33mThe optional fourth argument, LOCAL, if non-nil, says to modify[39;49;00m$
[33mthe hook's buffer-local value rather than its global value.[39;49;00m$
[33mThis makes the hook buffer-local, and it makes t a member of the[39;49;00m$
[33mbuffer-local value.  That acts as a flag to run the hook[39;49;00m$
[33mfunctions of the global value as well as in the local value.[39;49;00m$
[33m[39;49;00m$
[33mHOOK should be a symbol, and FUNCTION may be any valid function.  If[39;49;00m$
[33mHOOK is void, it is first set to nil.  If HOOK's value is a single[39;49;00m$
[33mfunction, it is changed to a list of functions.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mboundp[39;49;00m[37m [39;49;00m[31mhook[39;49;00m)[37m [39;49;00m([32mset[39;49;00m[37m [39;49;00m[31mhook[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mdefault-boundp[39;49;00m[37m [39;49;00m[31mhook[39;49;00m)[37m [39;49;00m([32mset-default[39;49;00m[37m [39;49;00m[31mhook[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mlocal[39;49;00m[37m [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32mlocal-variable-if-set-p[39;49;00m[37m [39;49;00m[31mhook[39;49;00m)[37m[39;49;00m$
[37m^I      [39;49;00m([32mset[39;49;00m[37m [39;49;00m([32mmake-local-variable[39;49;00m[37m [39;49;00m[31mhook[39;49;00m)[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[31mt[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m[37m;; Detect the case where make-local-variable was used on a hook[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[37m;; and do what we used to do.[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m([36munless[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mhook[39;49;00m))[37m [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mhook[39;49;00m)))[37m[39;49;00m$
[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mlocal[39;49;00m[37m [39;49;00m[31mt[39;49;00m)))[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mhook-value[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mlocal[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mhook[39;49;00m)[37m [39;49;00m([32mdefault-value[39;49;00m[37m [39;49;00m[31mhook[39;49;00m))))[37m[39;49;00m$
[37m    [39;49;00m[37m;; If the hook value is a single function, turn it into a list.[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mlistp[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m))[37m [39;49;00m([32mfunctionp[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m))[37m[39;49;00m$
[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m[37m;; Do the actual addition if necessary[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32mmember[39;49;00m[37m [39;49;00m[34mfunction[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m[34mfunction[39;49;00m)[37m[39;49;00m$
[37m^I[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[34mfunction[39;49;00m[37m [39;49;00m([32mpurecopy[39;49;00m[37m [39;49;00m[34mfunction[39;49;00m)))[37m[39;49;00m$
[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m[37m[39;49;00m$
[37m^I    [39;49;00m([34mif[39;49;00m[37m [39;49;00m[32mappend[39;49;00m[37m[39;49;00m$
[37m^I^I[39;49;00m([32mappend[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[34mfunction[39;49;00m))[37m[39;49;00m$
[37m^I      [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[34mfunction[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m))))[37m[39;49;00m$
[37m    [39;49;00m[37m;; Set the actual variable[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mlocal[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00m([34mprogn[39;49;00m[37m[39;49;00m$
[37m^I  [39;49;00m[37m;; If HOOK isn't a permanent local,[39;49;00m[37m[39;49;00m$
[37m^I  [39;49;00m[37m;; but FUNCTION wants to survive a change of modes,[39;49;00m[37m[39;49;00m$
[37m^I  [39;49;00m[37m;; mark HOOK as partially permanent.[39;49;00m[37m[39;49;00m$
[37m^I  [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32msymbolp[39;49;00m[37m [39;49;00m[34mfunction[39;49;00m)[37m[39;49;00m$
[37m^I       [39;49;00m([32mget[39;49;00m[37m [39;49;00m[34mfunction[39;49;00m[37m [39;49;00m[33m'permanent-local-hook[39;49;00m)[37m[39;49;00m$
[37m^I       [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mget[39;49;00m[37m [39;49;00m[31mhook[39;49;00m[37m [39;49;00m[33m'permanent-local[39;49;00m))[37m[39;49;00m$
[37m^I       [39;49;00m([32mput[39;49;00m[37m [39;49;00m[31mhook[39;49;00m[37m [39;49;00m[33m'permanent-local[39;49;00m[37m [39;49;00m[33m'permanent-local-hook[39;49;00m))[37m[39;49;00m$
[37m^I  [39;49;00m([32mset[39;49;00m[37m [39;49;00m[31mhook[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m))[37m[39;49;00m$
[37m      [39;49;00m([32mset-default[39;49;00m[37m [39;49;00m[31mhook[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mremove-hook[39;49;00m[37m [39;49;00m([31mhook[39;49;00m[37m [39;49;00m[34mfunction[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mlocal[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mRemove from the value of HOOK the function FUNCTION.[39;49;00m$
[33mHOOK should be a symbol, and FUNCTION may be any valid function.  If[39;49;00m$
[33mFUNCTION isn't the value of HOOK, or, if FUNCTION doesn't appear in the[39;49;00m$
[33mlist of hooks to run in HOOK, then nothing is done.  See [39;49;00m[33m`add-hook'[39;49;00m[33m.[39;49;00m$
[33m[39;49;00m$
[33mThe optional third argument, LOCAL, if non-nil, says to modify[39;49;00m$
[33mthe hook's buffer-local value rather than its default value.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mboundp[39;49;00m[37m [39;49;00m[31mhook[39;49;00m)[37m [39;49;00m([32mset[39;49;00m[37m [39;49;00m[31mhook[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mdefault-boundp[39;49;00m[37m [39;49;00m[31mhook[39;49;00m)[37m [39;49;00m([32mset-default[39;49;00m[37m [39;49;00m[31mhook[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m[37m;; Do nothing if LOCAL is t but this hook has no local binding.[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36munless[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mlocal[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mlocal-variable-p[39;49;00m[37m [39;49;00m[31mhook[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m[37m;; Detect the case where make-local-variable was used on a hook[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[37m;; and do what we used to do.[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mlocal-variable-p[39;49;00m[37m [39;49;00m[31mhook[39;49;00m)[37m[39;49;00m$
[37m^I       [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mhook[39;49;00m))[37m[39;49;00m$
[37m^I^I^I [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mhook[39;49;00m)))))[37m[39;49;00m$
[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mlocal[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mhook-value[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mlocal[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mhook[39;49;00m)[37m [39;49;00m([32mdefault-value[39;49;00m[37m [39;49;00m[31mhook[39;49;00m))))[37m[39;49;00m$
[37m      [39;49;00m[37m;; Remove the function, for both the list and the non-list cases.[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mlistp[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m))[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m)[37m [39;49;00m[33m'lambda[39;49;00m))[37m[39;49;00m$
[37m^I  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mequal[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m[37m [39;49;00m[34mfunction[39;49;00m)[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m$
[37m^I[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m[37m [39;49;00m([32mdelete[39;49;00m[37m [39;49;00m[34mfunction[39;49;00m[37m [39;49;00m([32mcopy-sequence[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m))))[37m[39;49;00m$
[37m      [39;49;00m[37m;; If the function is on the global hook, we need to shadow it locally[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m[37m;;(when (and local (member function (default-value hook))[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m[37m;;^I       (not (member (cons 'not function) hook-value)))[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m[37m;;  (push (cons 'not function) hook-value))[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m[37m;; Set the actual variable[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m[31mlocal[39;49;00m)[37m[39;49;00m$
[37m^I  [39;49;00m([32mset-default[39;49;00m[37m [39;49;00m[31mhook[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m)[37m[39;49;00m$
[37m^I[39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mequal[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m[37m [39;49;00m'([31mt[39;49;00m))[37m[39;49;00m$
[37m^I    [39;49;00m([32mkill-local-variable[39;49;00m[37m [39;49;00m[31mhook[39;49;00m)[37m[39;49;00m$
[37m^I  [39;49;00m([32mset[39;49;00m[37m [39;49;00m[31mhook[39;49;00m[37m [39;49;00m[31mhook-value[39;49;00m))))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefmacro[39;49;00m[37m [39;49;00m[36mletrec[39;49;00m[37m [39;49;00m([31mbinders[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mBind variables according to BINDERS then eval BODY.[39;49;00m$
[33mThe value of the last form in BODY is returned.[39;49;00m$
[33mEach element of BINDERS is a list (SYMBOL VALUEFORM) which binds[39;49;00m$
[33mSYMBOL to the value of VALUEFORM.[39;49;00m$
[33mAll symbols are bound before the VALUEFORMs are evalled.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; Only useful in lexical-binding mode.[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; As a special-form, we could implement it more efficiently (and cleanly,[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; making the vars actually unbound during evaluation of the binders).[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[34mlet[39;49;00m)[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m1[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m,([32mmapcar[39;49;00m[37m [39;49;00m[32m#'[39;49;00m[32mcar[39;49;00m[37m [39;49;00m[31mbinders[39;49;00m)[37m[39;49;00m$
[37m     [39;49;00m,@([32mmapcar[39;49;00m[37m [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31mbinder[39;49;00m)[37m [39;49;00m`([34msetq[39;49;00m[37m [39;49;00m,@[31mbinder[39;49;00m))[37m [39;49;00m[31mbinders[39;49;00m)[37m[39;49;00m$
[37m     [39;49;00m,@[31mbody[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefmacro[39;49;00m[37m [39;49;00m[36mwith-wrapper-hook[39;49;00m[37m [39;49;00m([31mhook[39;49;00m[37m [39;49;00m[31margs[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mRun BODY, using wrapper functions from HOOK with additional ARGS.[39;49;00m$
[33mHOOK is an abnormal hook.  Each hook function in HOOK [39;49;00m[33m\"[39;49;00m[33mwraps[39;49;00m[33m\"[39;49;00m[33m[39;49;00m$
[33maround the preceding ones, like a set of nested [39;49;00m[33m`around'[39;49;00m[33m advices.[39;49;00m$
[33m[39;49;00m$
[33mEach hook function should accept an argument list consisting of a[39;49;00m$
[33mfunction FUN, followed by the additional arguments in ARGS.[39;49;00m$
[33m[39;49;00m$
[33mThe first hook function in HOOK is passed a FUN that, if it is called[39;49;00m$
[33mwith arguments ARGS, performs BODY (i.e., the default operation).[39;49;00m$
[33mThe FUN passed to each successive hook function is defined based[39;49;00m$
[33mon the preceding hook functions; if called with arguments ARGS,[39;49;00m$
[33mit does what the [39;49;00m[33m`with-wrapper-hook'[39;49;00m[33m call would do if the[39;49;00m$
[33mpreceding hook functions were the only ones present in HOOK.[39;49;00m$
[33m[39;49;00m$
[33mEach hook function may call its FUN argument as many times as it wishes,[39;49;00m$
[33mincluding never.  In that case, such a hook function acts to replace[39;49;00m$
[33mthe default definition altogether, and any preceding hook functions.[39;49;00m$
[33mOf course, a subsequent hook function may do the same thing.[39;49;00m$
[33m[39;49;00m$
[33mEach hook function definition is used to construct the FUN passed[39;49;00m$
[33mto the next hook function, if any.  The last (or [39;49;00m[33m\"[39;49;00m[33moutermost[39;49;00m[33m\"[39;49;00m[33m)[39;49;00m$
[33mFUN is then called once.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m2[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m([31mform[39;49;00m[37m [39;49;00m[31msexp[39;49;00m[37m [39;49;00m[31mbody[39;49;00m))[37m[39;49;00m$
[37m           [39;49;00m([31mobsolete[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33muse a <foo>-function variable modified by [39;49;00m[33m`add-function'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m                     [39;49;00m[33m"[39;49;00m[33m24.4[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m[37m;; We need those two gensyms because CL's lexical scoping is not available[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; for function arguments :-([39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mfuns[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mfuns[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
[37m        [39;49;00m([31mglobal[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mglobal[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
[37m        [39;49;00m([31margssym[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33margs[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
[37m        [39;49;00m([31mrunrestofhook[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mrunrestofhook[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m[37m;; Since the hook is a wrapper, the loop has to be done via[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[37m;; recursion: a given hook function will call its parameter in order to[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[37m;; continue looping.[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m`([36mletrec[39;49;00m[37m [39;49;00m((,[31mrunrestofhook[39;49;00m[37m[39;49;00m$
[37m               [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m(,[31mfuns[39;49;00m[37m [39;49;00m,[31mglobal[39;49;00m[37m [39;49;00m,[31margssym[39;49;00m)[37m[39;49;00m$
[37m                 [39;49;00m[37m;; `funs' holds the functions left on the hook and `global'[39;49;00m[37m[39;49;00m$
[37m                 [39;49;00m[37m;; holds the functions left on the global part of the hook[39;49;00m[37m[39;49;00m$
[37m                 [39;49;00m[37m;; (in case the hook is local).[39;49;00m[37m[39;49;00m$
[37m                 [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m,[31mfuns[39;49;00m)[37m[39;49;00m$
[37m                     [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m,[31mfuns[39;49;00m))[37m[39;49;00m$
[37m                         [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m,[31mrunrestofhook[39;49;00m[37m[39;49;00m$
[37m                                  [39;49;00m([32mappend[39;49;00m[37m [39;49;00m,[31mglobal[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m,[31mfuns[39;49;00m))[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m,[31margssym[39;49;00m)[37m[39;49;00m$
[37m                       [39;49;00m([32mapply[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m,[31mfuns[39;49;00m)[37m[39;49;00m$
[37m                              [39;49;00m([31mapply-partially[39;49;00m[37m[39;49;00m$
[37m                               [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m(,[31mfuns[39;49;00m[37m [39;49;00m,[31mglobal[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m,[31margssym[39;49;00m)[37m[39;49;00m$
[37m                                 [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m,[31mrunrestofhook[39;49;00m[37m [39;49;00m,[31mfuns[39;49;00m[37m [39;49;00m,[31mglobal[39;49;00m[37m [39;49;00m,[31margssym[39;49;00m))[37m[39;49;00m$
[37m                               [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m,[31mfuns[39;49;00m)[37m [39;49;00m,[31mglobal[39;49;00m)[37m[39;49;00m$
[37m                              [39;49;00m,[31margssym[39;49;00m))[37m[39;49;00m$
[37m                   [39;49;00m[37m;; Once there are no more functions on the hook, run[39;49;00m[37m[39;49;00m$
[37m                   [39;49;00m[37m;; the original body.[39;49;00m[37m[39;49;00m$
[37m                   [39;49;00m([32mapply[39;49;00m[37m [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m,[31margs[39;49;00m[37m [39;49;00m,@[31mbody[39;49;00m)[37m [39;49;00m,[31margssym[39;49;00m)))))[37m[39;49;00m$
[37m       [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m,[31mrunrestofhook[39;49;00m[37m [39;49;00m,[31mhook[39;49;00m[37m[39;49;00m$
[37m                [39;49;00m[37m;; The global part of the hook, if any.[39;49;00m[37m[39;49;00m$
[37m                [39;49;00m,([34mif[39;49;00m[37m [39;49;00m([32msymbolp[39;49;00m[37m [39;49;00m[31mhook[39;49;00m)[37m[39;49;00m$
[37m                     [39;49;00m`([34mif[39;49;00m[37m [39;49;00m([32mlocal-variable-p[39;49;00m[37m [39;49;00m[33m',hook[39;49;00m)[37m[39;49;00m$
[37m                          [39;49;00m([32mdefault-value[39;49;00m[37m [39;49;00m[33m',hook[39;49;00m)))[37m[39;49;00m$
[37m                [39;49;00m([32mlist[39;49;00m[37m [39;49;00m,@[31margs[39;49;00m)))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31madd-to-list[39;49;00m[37m [39;49;00m([31mlist-var[39;49;00m[37m [39;49;00m[31melement[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[32mappend[39;49;00m[37m [39;49;00m[31mcompare-fn[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mAdd ELEMENT to the value of LIST-VAR if it isn't there yet.[39;49;00m$
[33mThe test for presence of ELEMENT is done with [39;49;00m[33m`equal'[39;49;00m[33m, or with[39;49;00m$
[33mCOMPARE-FN if that's non-nil.[39;49;00m$
[33mIf ELEMENT is added, it is added at the beginning of the list,[39;49;00m$
[33munless the optional argument APPEND is non-nil, in which case[39;49;00m$
[33mELEMENT is added at the end.[39;49;00m$
[33m[39;49;00m$
[33mThe return value is the new value of LIST-VAR.[39;49;00m$
[33m[39;49;00m$
[33mThis is handy to add some elements to configuration variables,[39;49;00m$
[33mbut please do not abuse it in Elisp code, where you are usually[39;49;00m$
[33mbetter off using [39;49;00m[33m`push'[39;49;00m[33m or [39;49;00m[33m`cl-pushnew'[39;49;00m[33m.[39;49;00m$
[33m[39;49;00m$
[33mIf you want to use [39;49;00m[33m`add-to-list'[39;49;00m[33m on a variable that is not[39;49;00m$
[33mdefined until a certain package is loaded, you should put the[39;49;00m$
[33mcall to [39;49;00m[33m`add-to-list'[39;49;00m[33m into a hook function that will be run only[39;49;00m$
[33mafter loading the package.  [39;49;00m[33m`eval-after-load'[39;49;00m[33m provides one way to[39;49;00m$
[33mdo this.  In some cases other hooks, such as major mode hooks,[39;49;00m$
[33mcan do the job.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m[39;49;00m$
[37m   [39;49;00m([31mcompiler-macro[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([32mexp[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m[37m;; FIXME: Something like this could be used for `set' as well.[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[33m'quote[39;49;00m[37m [39;49;00m([32mcar-safe[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m)))[37m[39;49;00m$
[37m              [39;49;00m([32mspecial-variable-p[39;49;00m[37m [39;49;00m([31mcadr[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m))[37m[39;49;00m$
[37m              [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([31mmacroexp-const-p[39;49;00m[37m [39;49;00m[32mappend[39;49;00m)))[37m[39;49;00m$
[37m          [39;49;00m[32mexp[39;49;00m[37m[39;49;00m$
[37m        [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31msym[39;49;00m[37m [39;49;00m([31mcadr[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m))[37m[39;49;00m$
[37m               [39;49;00m([32mappend[39;49;00m[37m [39;49;00m([32meval[39;49;00m[37m [39;49;00m[32mappend[39;49;00m))[37m[39;49;00m$
[37m               [39;49;00m([31mmsg[39;49;00m[37m [39;49;00m([32mformat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m`add-to-list'[39;49;00m[33m can't use lexical var [39;49;00m[33m`%s'[39;49;00m[33m; use [39;49;00m[33m`push'[39;49;00m[33m or [39;49;00m[33m`cl-pushnew'[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m                            [39;49;00m[31msym[39;49;00m))[37m[39;49;00m$
[37m               [39;49;00m[37m;; Big ugly hack so we only output a warning during[39;49;00m[37m[39;49;00m$
[37m               [39;49;00m[37m;; byte-compilation, and so we can use[39;49;00m[37m[39;49;00m$
[37m               [39;49;00m[37m;; byte-compile-not-lexical-var-p to silence the warning[39;49;00m[37m[39;49;00m$
[37m               [39;49;00m[37m;; when a defvar has been seen but not yet executed.[39;49;00m[37m[39;49;00m$
[37m               [39;49;00m([31mwarnfun[39;49;00m[37m [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m()[37m[39;49;00m$
[37m                          [39;49;00m[37m;; FIXME: We should also emit a warning for let-bound[39;49;00m[37m[39;49;00m$
[37m                          [39;49;00m[37m;; variables with dynamic binding.[39;49;00m[37m[39;49;00m$
[37m                          [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32massq[39;49;00m[37m [39;49;00m[31msym[39;49;00m[37m [39;49;00m[31mbyte-compile--lexical-environment[39;49;00m)[37m[39;49;00m$
[37m                            [39;49;00m([31mbyte-compile-log-warning[39;49;00m[37m [39;49;00m[31mmsg[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m[36m:error[39;49;00m))))[37m[39;49;00m$
[37m               [39;49;00m([31mcode[39;49;00m[37m[39;49;00m$
[37m                [39;49;00m([31mmacroexp-let2[39;49;00m[37m [39;49;00m[31mmacroexp-copyable-p[39;49;00m[37m [39;49;00m[31mx[39;49;00m[37m [39;49;00m[31melement[39;49;00m[37m[39;49;00m$
[37m                  [39;49;00m`([34mif[39;49;00m[37m [39;49;00m,([34mif[39;49;00m[37m [39;49;00m[31mcompare-fn[39;49;00m[37m[39;49;00m$
[37m                            [39;49;00m([34mprogn[39;49;00m[37m[39;49;00m$
[37m                              [39;49;00m([36mrequire[39;49;00m[37m [39;49;00m[33m'cl-lib[39;49;00m)[37m[39;49;00m$
[37m                              [39;49;00m`([31mcl-member[39;49;00m[37m [39;49;00m,[31mx[39;49;00m[37m [39;49;00m,[31msym[39;49;00m[37m [39;49;00m[36m:test[39;49;00m[37m [39;49;00m,[31mcompare-fn[39;49;00m))[37m[39;49;00m$
[37m                          [39;49;00m[37m;; For bootstrapping reasons, don't rely on[39;49;00m[37m[39;49;00m$
[37m                          [39;49;00m[37m;; cl--compiler-macro-member for the base case.[39;49;00m[37m[39;49;00m$
[37m                          [39;49;00m`([32mmember[39;49;00m[37m [39;49;00m,[31mx[39;49;00m[37m [39;49;00m,[31msym[39;49;00m))[37m[39;49;00m$
[37m                       [39;49;00m,[31msym[39;49;00m[37m[39;49;00m$
[37m                     [39;49;00m,([34mif[39;49;00m[37m [39;49;00m[32mappend[39;49;00m[37m[39;49;00m$
[37m                          [39;49;00m`([34msetq[39;49;00m[37m [39;49;00m,[31msym[39;49;00m[37m [39;49;00m([32mappend[39;49;00m[37m [39;49;00m,[31msym[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m,[31mx[39;49;00m)))[37m[39;49;00m$
[37m                        [39;49;00m`([36mpush[39;49;00m[37m [39;49;00m,[31mx[39;49;00m[37m [39;49;00m,[31msym[39;49;00m))))))[37m[39;49;00m$
[37m          [39;49;00m([34mif[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([31mmacroexp--compiling-p[39;49;00m))[37m[39;49;00m$
[37m              [39;49;00m[31mcode[39;49;00m[37m[39;49;00m$
[37m            [39;49;00m`([34mprogn[39;49;00m[37m[39;49;00m$
[37m               [39;49;00m([31mmacroexp--funcall-if-compiled[39;49;00m[37m [39;49;00m[33m',warnfun[39;49;00m)[37m[39;49;00m$
[37m               [39;49;00m,[31mcode[39;49;00m)))))))[37m[39;49;00m$
[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mcond[39;49;00m[37m[39;49;00m$
[37m       [39;49;00m(([32mnull[39;49;00m[37m [39;49;00m[31mcompare-fn[39;49;00m)[37m[39;49;00m$
[37m^I[39;49;00m([32mmember[39;49;00m[37m [39;49;00m[31melement[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m)))[37m[39;49;00m$
[37m       [39;49;00m(([32meq[39;49;00m[37m [39;49;00m[31mcompare-fn[39;49;00m[37m [39;49;00m[33m'eq[39;49;00m)[37m[39;49;00m$
[37m^I[39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[31melement[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m)))[37m[39;49;00m$
[37m       [39;49;00m(([32meq[39;49;00m[37m [39;49;00m[31mcompare-fn[39;49;00m[37m [39;49;00m[33m'eql[39;49;00m)[37m[39;49;00m$
[37m^I[39;49;00m([32mmemql[39;49;00m[37m [39;49;00m[31melement[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m)))[37m[39;49;00m$
[37m       [39;49;00m([31mt[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mlst[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m)))[37m[39;49;00m$
[37m^I  [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mlst[39;49;00m[37m[39;49;00m$
[37m^I^I      [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mcompare-fn[39;49;00m[37m [39;49;00m[31melement[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mlst[39;49;00m))))[37m[39;49;00m$
[37m^I    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mlst[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mlst[39;49;00m)))[37m[39;49;00m$
[37m          [39;49;00m[31mlst[39;49;00m)))[37m[39;49;00m$
[37m      [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([32mset[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m[37m[39;49;00m$
[37m^I [39;49;00m([34mif[39;49;00m[37m [39;49;00m[32mappend[39;49;00m[37m[39;49;00m$
[37m^I     [39;49;00m([32mappend[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m)[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[31melement[39;49;00m))[37m[39;49;00m$
[37m^I   [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31melement[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m))))))[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31madd-to-ordered-list[39;49;00m[37m [39;49;00m([31mlist-var[39;49;00m[37m [39;49;00m[31melement[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31morder[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mAdd ELEMENT to the value of LIST-VAR if it isn't there yet.[39;49;00m$
[33mThe test for presence of ELEMENT is done with [39;49;00m[33m`eq'[39;49;00m[33m.[39;49;00m$
[33m[39;49;00m$
[33mThe resulting list is reordered so that the elements are in the[39;49;00m$
[33morder given by each element's numeric list order.  Elements[39;49;00m$
[33mwithout a numeric list order are placed at the end of the list.[39;49;00m$
[33m[39;49;00m$
[33mIf the third optional argument ORDER is a number (integer or[39;49;00m$
[33mfloat), set the element's list order to the given value.  If[39;49;00m$
[33mORDER is nil or omitted, do not change the numeric order of[39;49;00m$
[33mELEMENT.  If ORDER has any other value, remove the numeric order[39;49;00m$
[33mof ELEMENT if it has one.[39;49;00m$
[33m[39;49;00m$
[33mThe list order for each element is stored in LIST-VAR's[39;49;00m$
[33m`list-order'[39;49;00m[33m property.[39;49;00m$
[33m[39;49;00m$
[33mThe return value is the new value of LIST-VAR.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mordering[39;49;00m[37m [39;49;00m([32mget[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m[37m [39;49;00m[33m'list-order[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m([36munless[39;49;00m[37m [39;49;00m[31mordering[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([32mput[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m[37m [39;49;00m[33m'list-order[39;49;00m[37m[39;49;00m$
[37m           [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mordering[39;49;00m[37m [39;49;00m([32mmake-hash-table[39;49;00m[37m [39;49;00m[36m:weakness[39;49;00m[37m [39;49;00m[33m'key[39;49;00m[37m [39;49;00m[36m:test[39;49;00m[37m [39;49;00m[33m'eq[39;49;00m))))[37m[39;49;00m$
[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31morder[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([32mputhash[39;49;00m[37m [39;49;00m[31melement[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mnumberp[39;49;00m[37m [39;49;00m[31morder[39;49;00m)[37m [39;49;00m[31morder[39;49;00m)[37m [39;49;00m[31mordering[39;49;00m))[37m[39;49;00m$
[37m    [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[31melement[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m))[37m[39;49;00m$
[37m      [39;49;00m([32mset[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31melement[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m))))[37m[39;49;00m$
[37m    [39;49;00m([32mset[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m[37m [39;49;00m([32msort[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mlist-var[39;49;00m)[37m[39;49;00m$
[37m^I^I^I[39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31ma[39;49;00m[37m [39;49;00m[31mb[39;49;00m)[37m[39;49;00m$
[37m^I^I^I  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31moa[39;49;00m[37m [39;49;00m([32mgethash[39;49;00m[37m [39;49;00m[31ma[39;49;00m[37m [39;49;00m[31mordering[39;49;00m))[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m([31mob[39;49;00m[37m [39;49;00m([32mgethash[39;49;00m[37m [39;49;00m[31mb[39;49;00m[37m [39;49;00m[31mordering[39;49;00m)))[37m[39;49;00m$
[37m^I^I^I    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31moa[39;49;00m[37m [39;49;00m[31mob[39;49;00m)[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m([32m<[39;49;00m[37m [39;49;00m[31moa[39;49;00m[37m [39;49;00m[31mob[39;49;00m)[37m[39;49;00m$
[37m^I^I^I      [39;49;00m[31moa[39;49;00m)))))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31madd-to-history[39;49;00m[37m [39;49;00m([31mhistory-var[39;49;00m[37m [39;49;00m[31mnewelt[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mmaxelt[39;49;00m[37m [39;49;00m[31mkeep-all[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mAdd NEWELT to the history list stored in the variable HISTORY-VAR.[39;49;00m$
[33mReturn the new history list.[39;49;00m$
[33mIf MAXELT is non-nil, it specifies the maximum length of the history.[39;49;00m$
[33mOtherwise, the maximum history length is the value of the [39;49;00m[33m`history-length'[39;49;00m[33m[39;49;00m$
[33mproperty on symbol HISTORY-VAR, if set, or the value of the [39;49;00m[33m`history-length'[39;49;00m[33m[39;49;00m$
[33mvariable.[39;49;00m$
[33mRemove duplicates of NEWELT if [39;49;00m[33m`history-delete-duplicates'[39;49;00m[33m is non-nil.[39;49;00m$
[33mIf optional fourth arg KEEP-ALL is non-nil, add NEWELT to history even[39;49;00m$
[33mif it is empty or a duplicate.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36munless[39;49;00m[37m [39;49;00m[31mmaxelt[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mmaxelt[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mget[39;49;00m[37m [39;49;00m[31mhistory-var[39;49;00m[37m [39;49;00m[33m'history-length[39;49;00m)[37m[39;49;00m$
[37m^I^I     [39;49;00m[31mhistory-length[39;49;00m)))[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mhistory[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mhistory-var[39;49;00m))[37m[39;49;00m$
[37m^I[39;49;00m[31mtail[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mlistp[39;49;00m[37m [39;49;00m[31mhistory[39;49;00m)[37m[39;49;00m$
[37m^I       [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mkeep-all[39;49;00m[37m[39;49;00m$
[37m^I^I   [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m[31mnewelt[39;49;00m))[37m[39;49;00m$
[37m^I^I   [39;49;00m([32m>[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31mnewelt[39;49;00m)[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m$
[37m^I       [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mkeep-all[39;49;00m[37m[39;49;00m$
[37m^I^I   [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mequal[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mhistory[39;49;00m)[37m [39;49;00m[31mnewelt[39;49;00m))))[37m[39;49;00m$
[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mhistory-delete-duplicates[39;49;00m[37m[39;49;00m$
[37m^I  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mhistory[39;49;00m[37m [39;49;00m([32mdelete[39;49;00m[37m [39;49;00m[31mnewelt[39;49;00m[37m [39;49;00m[31mhistory[39;49;00m)))[37m[39;49;00m$
[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mhistory[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mnewelt[39;49;00m[37m [39;49;00m[31mhistory[39;49;00m))[37m[39;49;00m$
[37m      [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mintegerp[39;49;00m[37m [39;49;00m[31mmaxelt[39;49;00m)[37m[39;49;00m$
[37m^I[39;49;00m([34mif[39;49;00m[37m [39;49;00m([32m=[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[31mmaxelt[39;49;00m)[37m[39;49;00m$
[37m^I    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mhistory[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
[37m^I  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([32mnthcdr[39;49;00m[37m [39;49;00m([32m1-[39;49;00m[37m [39;49;00m[31mmaxelt[39;49;00m)[37m [39;49;00m[31mhistory[39;49;00m))[37m[39;49;00m$
[37m^I  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)[37m[39;49;00m$
[37m^I    [39;49;00m([32msetcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)))))[37m[39;49;00m$
[37m    [39;49;00m([32mset[39;49;00m[37m [39;49;00m[31mhistory-var[39;49;00m[37m [39;49;00m[31mhistory[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m[37m[39;49;00m$
[37m;;;; Mode hooks.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
([34mdefvar[39;49;00m[37m [39;49;00m[36mdelay-mode-hooks[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mIf non-nil, [39;49;00m[33m`run-mode-hooks'[39;49;00m[33m should delay running the hooks.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([34mdefvar[39;49;00m[37m [39;49;00m[31mdelayed-mode-hooks[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mList of delayed mode hooks waiting to be run.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([32mmake-variable-buffer-local[39;49;00m[37m [39;49;00m[33m'delayed-mode-hooks[39;49;00m)[37m[39;49;00m$
([32mput[39;49;00m[37m [39;49;00m[33m'delay-mode-hooks[39;49;00m[37m [39;49;00m[33m'permanent-local[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
([34mdefvar[39;49;00m[37m [39;49;00m[31mchange-major-mode-after-body-hook[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mNormal hook run in major mode functions, before the mode hooks.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
([34mdefvar[39;49;00m[37m [39;49;00m[31mafter-change-major-mode-hook[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mNormal hook run at the very end of major mode functions.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mrun-mode-hooks[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31mhooks[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mRun mode hooks [39;49;00m[33m`delayed-mode-hooks'[39;49;00m[33m and HOOKS, or delay HOOKS.[39;49;00m$
[33mIf the variable [39;49;00m[33m`delay-mode-hooks'[39;49;00m[33m is non-nil, does not run any hooks,[39;49;00m$
[33mjust adds the HOOKS to the list [39;49;00m[33m`delayed-mode-hooks'[39;49;00m[33m.[39;49;00m$
[33mOtherwise, runs hooks in the sequence: [39;49;00m[33m`change-major-mode-after-body-hook'[39;49;00m[33m,[39;49;00m$
[33m`delayed-mode-hooks'[39;49;00m[33m (in reverse order), HOOKS, and finally[39;49;00m$
[33m`after-change-major-mode-hook'[39;49;00m[33m.  Major mode functions should use[39;49;00m$
[33mthis instead of [39;49;00m[33m`run-hooks'[39;49;00m[33m when running their FOO-mode-hook.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m[36mdelay-mode-hooks[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m[37m;; Delaying case.[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([36mdolist[39;49;00m[37m [39;49;00m([31mhook[39;49;00m[37m [39;49;00m[31mhooks[39;49;00m)[37m[39;49;00m$
[37m^I[39;49;00m([36mpush[39;49;00m[37m [39;49;00m[31mhook[39;49;00m[37m [39;49;00m[31mdelayed-mode-hooks[39;49;00m))[37m[39;49;00m$
[37m    [39;49;00m[37m;; Normal case, just run the hook as before plus any delayed hooks.[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mhooks[39;49;00m[37m [39;49;00m([32mnconc[39;49;00m[37m [39;49;00m([32mnreverse[39;49;00m[37m [39;49;00m[31mdelayed-mode-hooks[39;49;00m)[37m [39;49;00m[31mhooks[39;49;00m))[37m[39;49;00m$
[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mdelayed-mode-hooks[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([32mapply[39;49;00m[37m [39;49;00m[33m'run-hooks[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[33m'change-major-mode-after-body-hook[39;49;00m[37m [39;49;00m[31mhooks[39;49;00m))[37m[39;49;00m$
[37m    [39;49;00m([32mrun-hooks[39;49;00m[37m [39;49;00m[33m'after-change-major-mode-hook[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefmacro[39;49;00m[37m [39;49;00m[36mdelay-mode-hooks[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mExecute BODY, but delay any [39;49;00m[33m`run-mode-hooks'[39;49;00m[33m.[39;49;00m$
[33mThese hooks will be executed by the first following call to[39;49;00m$
[33m`run-mode-hooks'[39;49;00m[33m that occurs outside any [39;49;00m[33m`delayed-mode-hooks'[39;49;00m[33m form.[39;49;00m$
[33mOnly affects hooks run in the current buffer.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m`([34mprogn[39;49;00m[37m[39;49;00m$
[37m     [39;49;00m([32mmake-local-variable[39;49;00m[37m [39;49;00m[33m'delay-mode-hooks[39;49;00m)[37m[39;49;00m$
[37m     [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([36mdelay-mode-hooks[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
[37m       [39;49;00m,@[31mbody[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
[37m;; PUBLIC: find if the current mode derives from another.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mderived-mode-p[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31mmodes[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mNon-nil if the current major mode is derived from one of MODES.[39;49;00m$
[33mUses the [39;49;00m[33m`derived-mode-parent'[39;49;00m[33m property of the symbol to trace backwards.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mparent[39;49;00m[37m [39;49;00m[31mmajor-mode[39;49;00m))[37m[39;49;00m$
[37m    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[31mparent[39;49;00m[37m [39;49;00m[31mmodes[39;49;00m))[37m[39;49;00m$
[37m^I^I[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mparent[39;49;00m[37m [39;49;00m([32mget[39;49;00m[37m [39;49;00m[31mparent[39;49;00m[37m [39;49;00m[33m'derived-mode-parent[39;49;00m))))[37m[39;49;00m$
[37m    [39;49;00m[31mparent[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m[37m[39;49;00m$
[37m;;;; Minor modes.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m;; If a minor mode is not defined with define-minor-mode,[39;49;00m[37m[39;49;00m$
[37m;; add it here explicitly.[39;49;00m[37m[39;49;00m$
[37m;; isearch-mode is deliberately excluded, since you should[39;49;00m[37m[39;49;00m$
[37m;; not call it yourself.[39;49;00m[37m[39;49;00m$
([34mdefvar[39;49;00m[37m [39;49;00m[31mminor-mode-list[39;49;00m[37m [39;49;00m'([31mauto-save-mode[39;49;00m[37m [39;49;00m[31mauto-fill-mode[39;49;00m[37m [39;49;00m[31mabbrev-mode[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I^I [39;49;00m[31moverwrite-mode[39;49;00m[37m [39;49;00m[31mview-mode[39;49;00m[37m[39;49;00m$
[37m                                         [39;49;00m[31mhs-minor-mode[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mList of all minor mode functions.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31madd-minor-mode[39;49;00m[37m [39;49;00m([31mtoggle[39;49;00m[37m [39;49;00m[31mname[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m[37m [39;49;00m[31mafter[39;49;00m[37m [39;49;00m[31mtoggle-fun[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mRegister a new minor mode.[39;49;00m$
[33m[39;49;00m$
[33mThis is an XEmacs-compatibility function.  Use [39;49;00m[33m`define-minor-mode'[39;49;00m[33m instead.[39;49;00m$
[33m[39;49;00m$
[33mTOGGLE is a symbol which is the name of a buffer-local variable that[39;49;00m$
[33mis toggled on or off to say whether the minor mode is active or not.[39;49;00m$
[33m[39;49;00m$
[33mNAME specifies what will appear in the mode line when the minor mode[39;49;00m$
[33mis active.  NAME should be either a string starting with a space, or a[39;49;00m$
[33msymbol whose value is such a string.[39;49;00m$
[33m[39;49;00m$
[33mOptional KEYMAP is the keymap for the minor mode that will be added[39;49;00m$
[33mto [39;49;00m[33m`minor-mode-map-alist'[39;49;00m[33m.[39;49;00m$
[33m[39;49;00m$
[33mOptional AFTER specifies that TOGGLE should be added after AFTER[39;49;00m$
[33min [39;49;00m[33m`minor-mode-alist'[39;49;00m[33m.[39;49;00m$
[33m[39;49;00m$
[33mOptional TOGGLE-FUN is an interactive function to toggle the mode.[39;49;00m$
[33mIt defaults to (and should by convention be) TOGGLE.[39;49;00m$
[33m[39;49;00m$
[33mIf TOGGLE has a non-nil [39;49;00m[33m`[39;49;00m[33m:included' property, an entry for the mode is[39;49;00m$
[33mincluded in the mode-line minor mode menu.[39;49;00m$
[33mIf TOGGLE has a [39;49;00m[33m`[39;49;00m[33m:menu-tag', that is used for the menu item's label.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[31mtoggle[39;49;00m[37m [39;49;00m[31mminor-mode-list[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([36mpush[39;49;00m[37m [39;49;00m[31mtoggle[39;49;00m[37m [39;49;00m[31mminor-mode-list[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
[37m  [39;49;00m([36munless[39;49;00m[37m [39;49;00m[31mtoggle-fun[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mtoggle-fun[39;49;00m[37m [39;49;00m[31mtoggle[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mtoggle-fun[39;49;00m[37m [39;49;00m[31mtoggle[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([32mput[39;49;00m[37m [39;49;00m[31mtoggle[39;49;00m[37m [39;49;00m[36m:minor-mode-function[39;49;00m[37m [39;49;00m[31mtoggle-fun[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m[37m;; Add the name to the minor-mode-alist.[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31mname[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mexisting[39;49;00m[37m [39;49;00m([32massq[39;49;00m[37m [39;49;00m[31mtoggle[39;49;00m[37m [39;49;00m[31mminor-mode-alist[39;49;00m)))[37m[39;49;00m$
[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mexisting[39;49;00m[37m[39;49;00m$
[37m^I  [39;49;00m([32msetcdr[39;49;00m[37m [39;49;00m[31mexisting[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[31mname[39;49;00m))[37m[39;49;00m$
[37m^I[39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtail[39;49;00m[37m [39;49;00m[31mminor-mode-alist[39;49;00m)[37m [39;49;00m[31mfound[39;49;00m)[37m[39;49;00m$
[37m^I  [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m[31mfound[39;49;00m))[37m[39;49;00m$
[37m^I    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mafter[39;49;00m[37m [39;49;00m([31mcaar[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))[37m[39;49;00m$
[37m^I^I[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mfound[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)[37m[39;49;00m$
[37m^I      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))))[37m[39;49;00m$
[37m^I  [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mfound[39;49;00m[37m[39;49;00m$
[37m^I      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mrest[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mfound[39;49;00m)))[37m[39;49;00m$
[37m^I^I[39;49;00m([32msetcdr[39;49;00m[37m [39;49;00m[31mfound[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
[37m^I^I[39;49;00m([32mnconc[39;49;00m[37m [39;49;00m[31mfound[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[31mtoggle[39;49;00m[37m [39;49;00m[31mname[39;49;00m))[37m [39;49;00m[31mrest[39;49;00m))[37m[39;49;00m$
[37m^I    [39;49;00m([36mpush[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[31mtoggle[39;49;00m[37m [39;49;00m[31mname[39;49;00m)[37m [39;49;00m[31mminor-mode-alist[39;49;00m))))))[37m[39;49;00m$
[37m  [39;49;00m[37m;; Add the toggle to the minor-modes menu if requested.[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mget[39;49;00m[37m [39;49;00m[31mtoggle[39;49;00m[37m [39;49;00m[36m:included[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([32mdefine-key[39;49;00m[37m [39;49;00m[31mmode-line-mode-menu[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([32mvector[39;49;00m[37m [39;49;00m[31mtoggle[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'menu-item[39;49;00m[37m[39;49;00m$
[37m^I    [39;49;00m([32mconcat[39;49;00m[37m[39;49;00m$
[37m^I     [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mget[39;49;00m[37m [39;49;00m[31mtoggle[39;49;00m[37m [39;49;00m[36m:menu-tag[39;49;00m)[37m[39;49;00m$
[37m^I^I [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m[31mname[39;49;00m)[37m [39;49;00m[31mname[39;49;00m[37m [39;49;00m([32msymbol-name[39;49;00m[37m [39;49;00m[31mtoggle[39;49;00m)))[37m[39;49;00m$
[37m^I     [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mmode-name[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32msymbolp[39;49;00m[37m [39;49;00m[31mname[39;49;00m)[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31mname[39;49;00m))))[37m[39;49;00m$
[37m^I       [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m[31mmode-name[39;49;00m)[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m[^ ]+[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mmode-name[39;49;00m))[37m[39;49;00m$
[37m^I^I   [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m ([39;49;00m[33m"[39;49;00m[37m [39;49;00m([31mmatch-string[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[31mmode-name[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m)[39;49;00m[33m"[39;49;00m))))[37m[39;49;00m$
[37m^I    [39;49;00m[31mtoggle-fun[39;49;00m[37m[39;49;00m$
[37m^I    [39;49;00m[36m:button[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[36m:toggle[39;49;00m[37m [39;49;00m[31mtoggle[39;49;00m))))[37m[39;49;00m$
[37m[39;49;00m$
[37m  [39;49;00m[37m;; Add the map to the minor-mode-map-alist.[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mexisting[39;49;00m[37m [39;49;00m([32massq[39;49;00m[37m [39;49;00m[31mtoggle[39;49;00m[37m [39;49;00m[31mminor-mode-map-alist[39;49;00m)))[37m[39;49;00m$
[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mexisting[39;49;00m[37m[39;49;00m$
[37m^I  [39;49;00m([32msetcdr[39;49;00m[37m [39;49;00m[31mexisting[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m)[37m[39;49;00m$
[37m^I[39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtail[39;49;00m[37m [39;49;00m[31mminor-mode-map-alist[39;49;00m)[37m [39;49;00m[31mfound[39;49;00m)[37m[39;49;00m$
[37m^I  [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m[31mfound[39;49;00m))[37m[39;49;00m$
[37m^I    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mafter[39;49;00m[37m [39;49;00m([31mcaar[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))[37m[39;49;00m$
[37m^I^I[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mfound[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)[37m[39;49;00m$
[37m^I      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mtail[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))))[37m[39;49;00m$
[37m^I  [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mfound[39;49;00m[37m[39;49;00m$
[37m^I      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mrest[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mfound[39;49;00m)))[37m[39;49;00m$
[37m^I^I[39;49;00m([32msetcdr[39;49;00m[37m [39;49;00m[31mfound[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
[37m^I^I[39;49;00m([32mnconc[39;49;00m[37m [39;49;00m[31mfound[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mtoggle[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m))[37m [39;49;00m[31mrest[39;49;00m))[37m[39;49;00m$
[37m^I    [39;49;00m([36mpush[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mtoggle[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m)[37m [39;49;00m[31mminor-mode-map-alist[39;49;00m)))))))[37m[39;49;00m$
[37m[39;49;00m[37m[39;49;00m$
[37m;;;; Load history[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
([36mdefsubst[39;49;00m[37m [39;49;00m[31mautoloadp[39;49;00m[37m [39;49;00m([31mobject[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mNon-nil if OBJECT is an autoload.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([32meq[39;49;00m[37m [39;49;00m[33m'autoload[39;49;00m[37m [39;49;00m([32mcar-safe[39;49;00m[37m [39;49;00m[31mobject[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
[37m;; (defun autoload-type (object)[39;49;00m[37m[39;49;00m$
[37m;;   "Returns the type of OBJECT or `function' or `command' if the type is nil.[39;49;00m[37m[39;49;00m$
[37m;; OBJECT should be an autoload object."[39;49;00m[37m[39;49;00m$
[37m;;   (when (autoloadp object)[39;49;00m[37m[39;49;00m$
[37m;;     (let ((type (nth 3 object)))[39;49;00m[37m[39;49;00m$
[37m;;       (cond ((null type) (if (nth 2 object) 'command 'function))[39;49;00m[37m[39;49;00m$
[37m;;             ((eq 'keymap t) 'macro)[39;49;00m[37m[39;49;00m$
[37m;;             (type)))))[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m;; (defalias 'autoload-file #'cadr[39;49;00m[37m[39;49;00m$
[37m;;   "Return the name of the file from which AUTOLOAD will be loaded.[39;49;00m[37m[39;49;00m$
[37m;; \n\(fn AUTOLOAD)")[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31msymbol-file[39;49;00m[37m [39;49;00m([31msymbol[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mtype[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn the name of the file that defined SYMBOL.[39;49;00m$
[33mThe value is normally an absolute file name.  It can also be nil,[39;49;00m$
[33mif the definition is not associated with any file.  If SYMBOL[39;49;00m$
[33mspecifies an autoloaded function, the value can be a relative[39;49;00m$
[33mfile name without extension.[39;49;00m$
[33m[39;49;00m$
[33mIf TYPE is nil, then any kind of definition is acceptable.  If[39;49;00m$
[33mTYPE is [39;49;00m[33m`defun'[39;49;00m[33m, [39;49;00m[33m`defvar'[39;49;00m[33m, or [39;49;00m[33m`defface'[39;49;00m[33m, that specifies function[39;49;00m$
[33mdefinition, variable definition, or face definition only.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[31mtype[39;49;00m)[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mtype[39;49;00m[37m [39;49;00m[33m'defun[39;49;00m))[37m[39;49;00m$
[37m^I   [39;49;00m([32msymbolp[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m)[37m[39;49;00m$
[37m^I   [39;49;00m([31mautoloadp[39;49;00m[37m [39;49;00m([32msymbol-function[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m)))[37m[39;49;00m$
[37m      [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m([32msymbol-function[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m))[37m[39;49;00m$
[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mfiles[39;49;00m[37m [39;49;00m[31mload-history[39;49;00m)[37m[39;49;00m$
[37m^I  [39;49;00m[31mfile[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m[31mfiles[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mtype[39;49;00m[37m[39;49;00m$
[37m^I^I[39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mtype[39;49;00m[37m [39;49;00m[33m'defvar[39;49;00m)[37m[39;49;00m$
[37m^I^I    [39;49;00m[37m;; Variables are present just as their names.[39;49;00m[37m[39;49;00m$
[37m^I^I    [39;49;00m([32mmember[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mfiles[39;49;00m)))[37m[39;49;00m$
[37m^I^I  [39;49;00m[37m;; Other types are represented as (TYPE . NAME).[39;49;00m[37m[39;49;00m$
[37m^I^I  [39;49;00m([32mmember[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mtype[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m)[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mfiles[39;49;00m))))[37m[39;49;00m$
[37m^I      [39;49;00m[37m;; We accept all types, so look for variable def[39;49;00m[37m[39;49;00m$
[37m^I      [39;49;00m[37m;; and then for any other kind.[39;49;00m[37m[39;49;00m$
[37m^I      [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mmember[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mfiles[39;49;00m)))[37m[39;49;00m$
[37m^I^I  [39;49;00m([32mrassq[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mfiles[39;49;00m)))))[37m[39;49;00m$
[37m^I    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mfile[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mfiles[39;49;00m))[37m [39;49;00m[31mfiles[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m$
[37m^I[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mfiles[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mfiles[39;49;00m)))[37m[39;49;00m$
[37m      [39;49;00m[31mfile[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mlocate-library[39;49;00m[37m [39;49;00m([31mlibrary[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mnosuffix[39;49;00m[37m [39;49;00m[31mpath[39;49;00m[37m [39;49;00m[31minteractive-call[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mShow the precise file name of Emacs library LIBRARY.[39;49;00m$
[33mLIBRARY should be a relative file name of the library, a string.[39;49;00m$
[33mIt can omit the suffix (a.k.a. file-name extension) if NOSUFFIX is[39;49;00m$
[33mnil (which is the default, see below).[39;49;00m$
[33mThis command searches the directories in [39;49;00m[33m`load-path'[39;49;00m[33m like [39;49;00m[33m`[39;49;00m[33m\\[39;49;00m[33m[load-library]'[39;49;00m$
[33mto find the file that [39;49;00m[33m`[39;49;00m[33m\\[39;49;00m[33m[load-library] RET LIBRARY RET' would load.[39;49;00m$
[33mOptional second arg NOSUFFIX non-nil means don't add suffixes [39;49;00m[33m`load-suffixes'[39;49;00m[33m[39;49;00m$
[33mto the specified name LIBRARY.[39;49;00m$
[33m[39;49;00m$
[33mIf the optional third arg PATH is specified, that list of directories[39;49;00m$
[33mis used instead of [39;49;00m[33m`load-path'[39;49;00m[33m.[39;49;00m$
[33m[39;49;00m$
[33mWhen called from a program, the file name is normally returned as a[39;49;00m$
[33mstring.  When run interactively, the argument INTERACTIVE-CALL is t,[39;49;00m$
[33mand the file name is displayed in the echo area.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34minteractive[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m([32mcompleting-read[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mLocate library: [39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I      [39;49;00m([31mapply-partially[39;49;00m[37m[39;49;00m$
[37m                                       [39;49;00m[33m'locate-file-completion-table[39;49;00m[37m[39;49;00m$
[37m                                       [39;49;00m[31mload-path[39;49;00m[37m [39;49;00m([32mget-load-suffixes[39;49;00m)))[37m[39;49;00m$
[37m^I^I     [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m$
[37m^I^I     [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mfile[39;49;00m[37m [39;49;00m([31mlocate-file[39;49;00m[37m [39;49;00m[31mlibrary[39;49;00m[37m[39;49;00m$
[37m^I^I^I   [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mpath[39;49;00m[37m [39;49;00m[31mload-path[39;49;00m)[37m[39;49;00m$
[37m^I^I^I   [39;49;00m([32mappend[39;49;00m[37m [39;49;00m([36munless[39;49;00m[37m [39;49;00m[31mnosuffix[39;49;00m[37m [39;49;00m([32mget-load-suffixes[39;49;00m))[37m[39;49;00m$
[37m^I^I^I^I   [39;49;00m[31mload-file-rep-suffixes[39;49;00m))))[37m[39;49;00m$
[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31minteractive-call[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mfile[39;49;00m[37m[39;49;00m$
[37m^I    [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mLibrary is file %s[39;49;00m[33m"[39;49;00m[37m [39;49;00m([31mabbreviate-file-name[39;49;00m[37m [39;49;00m[31mfile[39;49;00m))[37m[39;49;00m$
[37m^I  [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mNo library %s in search path[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mlibrary[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m[31mfile[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m[37m[39;49;00m$
[37m;;;; Process stuff.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mprocess-lines[39;49;00m[37m [39;49;00m([31mprogram[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31margs[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mExecute PROGRAM with ARGS, returning its output as a list of lines.[39;49;00m$
[33mSignal an error if the program returns with a non-zero exit status.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mwith-temp-buffer[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mstatus[39;49;00m[37m [39;49;00m([32mapply[39;49;00m[37m [39;49;00m[33m'call-process[39;49;00m[37m [39;49;00m[31mprogram[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m([32mcurrent-buffer[39;49;00m)[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31margs[39;49;00m)))[37m[39;49;00m$
[37m      [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mstatus[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m^I[39;49;00m([36merror[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m%s exited with status %s[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mprogram[39;49;00m[37m [39;49;00m[31mstatus[39;49;00m))[37m[39;49;00m$
[37m      [39;49;00m([32mgoto-char[39;49;00m[37m [39;49;00m([32mpoint-min[39;49;00m))[37m[39;49;00m$
[37m      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m([31mlines[39;49;00m)[37m[39;49;00m$
[37m^I[39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32meobp[39;49;00m))[37m[39;49;00m$
[37m^I  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mlines[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m([32mbuffer-substring-no-properties[39;49;00m[37m[39;49;00m$
[37m^I^I^I     [39;49;00m([32mline-beginning-position[39;49;00m)[37m[39;49;00m$
[37m^I^I^I     [39;49;00m([32mline-end-position[39;49;00m))[37m[39;49;00m$
[37m^I^I^I    [39;49;00m[31mlines[39;49;00m))[37m[39;49;00m$
[37m^I  [39;49;00m([32mforward-line[39;49;00m[37m [39;49;00m[34m1[39;49;00m))[37m[39;49;00m$
[37m^I[39;49;00m([32mnreverse[39;49;00m[37m [39;49;00m[31mlines[39;49;00m)))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mprocess-live-p[39;49;00m[37m [39;49;00m([31mprocess[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturns non-nil if PROCESS is alive.[39;49;00m$
[33mA process is considered alive if its status is [39;49;00m[33m`run'[39;49;00m[33m, [39;49;00m[33m`open'[39;49;00m[33m,[39;49;00m$
[33m`listen'[39;49;00m[33m, [39;49;00m[33m`connect'[39;49;00m[33m or [39;49;00m[33m`stop'[39;49;00m[33m.  Value is nil if PROCESS is not a[39;49;00m$
[33mprocess.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mprocessp[39;49;00m[37m [39;49;00m[31mprocess[39;49;00m)[37m[39;49;00m$
[37m       [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m([32mprocess-status[39;49;00m[37m [39;49;00m[31mprocess[39;49;00m)[37m[39;49;00m$
[37m^I     [39;49;00m'([31mrun[39;49;00m[37m [39;49;00m[31mopen[39;49;00m[37m [39;49;00m[31mlisten[39;49;00m[37m [39;49;00m[31mconnect[39;49;00m[37m [39;49;00m[31mstop[39;49;00m))))[37m[39;49;00m$
[37m[39;49;00m$
[37m;; compatibility[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
([31mmake-obsolete[39;49;00m[37m[39;49;00m$
[37m [39;49;00m[33m'process-kill-without-query[39;49;00m[37m[39;49;00m$
[37m [39;49;00m[33m"[39;49;00m[33muse [39;49;00m[33m`process-query-on-exit-flag'[39;49;00m[33m or [39;49;00m[33m`set-process-query-on-exit-flag'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m [39;49;00m[33m"[39;49;00m[33m22.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mprocess-kill-without-query[39;49;00m[37m [39;49;00m([31mprocess[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31m_flag[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mSay no query needed if PROCESS is running when Emacs is exited.[39;49;00m$
[33mOptional second argument if non-nil says to require a query.[39;49;00m$
[33mValue is t if a query was formerly required.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mold[39;49;00m[37m [39;49;00m([32mprocess-query-on-exit-flag[39;49;00m[37m [39;49;00m[31mprocess[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m([32mset-process-query-on-exit-flag[39;49;00m[37m [39;49;00m[31mprocess[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m[31mold[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mprocess-kill-buffer-query-function[39;49;00m[37m [39;49;00m()[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mAsk before killing a buffer that has a running process.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mprocess[39;49;00m[37m [39;49;00m([32mget-buffer-process[39;49;00m[37m [39;49;00m([32mcurrent-buffer[39;49;00m))))[37m[39;49;00m$
[37m    [39;49;00m([34mor[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m[31mprocess[39;49;00m)[37m[39;49;00m$
[37m        [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m([32mprocess-status[39;49;00m[37m [39;49;00m[31mprocess[39;49;00m)[37m [39;49;00m'([31mrun[39;49;00m[37m [39;49;00m[31mstop[39;49;00m[37m [39;49;00m[31mopen[39;49;00m[37m [39;49;00m[31mlisten[39;49;00m)))[37m[39;49;00m$
[37m        [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mprocess-query-on-exit-flag[39;49;00m[37m [39;49;00m[31mprocess[39;49;00m))[37m[39;49;00m$
[37m        [39;49;00m([32myes-or-no-p[39;49;00m[37m[39;49;00m$
[37m^I [39;49;00m([32mformat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mBuffer %S has a running process; kill it? [39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m^I^I [39;49;00m([32mbuffer-name[39;49;00m[37m [39;49;00m([32mcurrent-buffer[39;49;00m)))))))[37m[39;49;00m$
[37m[39;49;00m$
([31madd-hook[39;49;00m[37m [39;49;00m[33m'kill-buffer-query-functions[39;49;00m[37m [39;49;00m[33m'process-kill-buffer-query-function[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
[37m;; process plist management[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mprocess-get[39;49;00m[37m [39;49;00m([31mprocess[39;49;00m[37m [39;49;00m[31mpropname[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn the value of PROCESS' PROPNAME property.[39;49;00m$
[33mThis is the last value stored with [39;49;00m[33m`[39;49;00m[33m(process-put PROCESS PROPNAME VALUE)'.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([32mplist-get[39;49;00m[37m [39;49;00m([32mprocess-plist[39;49;00m[37m [39;49;00m[31mprocess[39;49;00m)[37m [39;49;00m[31mpropname[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mprocess-put[39;49;00m[37m [39;49;00m([31mprocess[39;49;00m[37m [39;49;00m[31mpropname[39;49;00m[37m [39;49;00m[31mvalue[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mChange PROCESS' PROPNAME property to VALUE.[39;49;00m$
[33mIt can be retrieved with [39;49;00m[33m`[39;49;00m[33m(process-get PROCESS PROPNAME)'.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([32mset-process-plist[39;49;00m[37m [39;49;00m[31mprocess[39;49;00m[37m[39;49;00m$
[37m^I^I     [39;49;00m([32mplist-put[39;49;00m[37m [39;49;00m([32mprocess-plist[39;49;00m[37m [39;49;00m[31mprocess[39;49;00m)[37m [39;49;00m[31mpropname[39;49;00m[37m [39;49;00m[31mvalue[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m[37m[39;49;00m$
[37m;;;; Input and display facilities.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
([34mdefconst[39;49;00m[37m [39;49;00m[31mread-key-empty-map[39;49;00m[37m [39;49;00m([32mmake-sparse-keymap[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
([34mdefvar[39;49;00m[37m [39;49;00m[31mread-key-delay[39;49;00m[37m [39;49;00m[34m0.01[39;49;00m)[37m [39;49;00m[37m;Fast enough for 100Hz repeat rate, hopefully.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mread-key[39;49;00m[37m [39;49;00m([34m&optional[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mRead a key from the keyboard.[39;49;00m$
[33mContrary to [39;49;00m[33m`read-event'[39;49;00m[33m this will not return a raw event but instead will[39;49;00m$
[33mobey the input decoding and translations usually done by [39;49;00m[33m`read-key-sequence'[39;49;00m[33m.[39;49;00m$
[33mSo escape sequences and keyboard encoding are taken into account.[39;49;00m$
[33mWhen there's an ambiguity because the key looks like the prefix of[39;49;00m$
[33msome sort of escape sequence, the ambiguity is resolved via [39;49;00m[33m`read-key-delay'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; This overriding-terminal-local-map binding also happens to[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; disable quail's input methods, so although read-key-sequence[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; always inherits the input method, in practice read-key does not[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; inherit the input method (at least not if it's based on quail).[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31moverriding-terminal-local-map[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
[37m^I[39;49;00m([31moverriding-local-map[39;49;00m[37m [39;49;00m[31mread-key-empty-map[39;49;00m)[37m[39;49;00m$
[37m        [39;49;00m([31mecho-keystrokes[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m^I[39;49;00m([31mold-global-map[39;49;00m[37m [39;49;00m([32mcurrent-global-map[39;49;00m))[37m[39;49;00m$
[37m        [39;49;00m([31mtimer[39;49;00m[37m [39;49;00m([31mrun-with-idle-timer[39;49;00m[37m[39;49;00m$
[37m                [39;49;00m[37m;; Wait long enough that Emacs has the time to receive and[39;49;00m[37m[39;49;00m$
[37m                [39;49;00m[37m;; process all the raw events associated with the single-key.[39;49;00m[37m[39;49;00m$
[37m                [39;49;00m[37m;; But don't wait too long, or the user may find the delay[39;49;00m[37m[39;49;00m$
[37m                [39;49;00m[37m;; annoying (or keep hitting more keys which may then get[39;49;00m[37m[39;49;00m$
[37m                [39;49;00m[37m;; lost or misinterpreted).[39;49;00m[37m[39;49;00m$
[37m                [39;49;00m[37m;; This is only relevant for keys which Emacs perceives as[39;49;00m[37m[39;49;00m$
[37m                [39;49;00m[37m;; "prefixes", such as C-x (because of the C-x 8 map in[39;49;00m[37m[39;49;00m$
[37m                [39;49;00m[37m;; key-translate-table and the C-x @ map in function-key-map)[39;49;00m[37m[39;49;00m$
[37m                [39;49;00m[37m;; or ESC (because of terminal escape sequences in[39;49;00m[37m[39;49;00m$
[37m                [39;49;00m[37m;; input-decode-map).[39;49;00m[37m[39;49;00m$
[37m                [39;49;00m[31mread-key-delay[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m[39;49;00m$
[37m                [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m()[37m[39;49;00m$
[37m                  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mkeys[39;49;00m[37m [39;49;00m([32mthis-command-keys-vector[39;49;00m)))[37m[39;49;00m$
[37m                    [39;49;00m([36munless[39;49;00m[37m [39;49;00m([31mzerop[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31mkeys[39;49;00m))[37m[39;49;00m$
[37m                      [39;49;00m[37m;; `keys' is non-empty, so the user has hit at least[39;49;00m[37m[39;49;00m$
[37m                      [39;49;00m[37m;; one key; there's no point waiting any longer, even[39;49;00m[37m[39;49;00m$
[37m                      [39;49;00m[37m;; though read-key-sequence thinks we should wait[39;49;00m[37m[39;49;00m$
[37m                      [39;49;00m[37m;; for more input to decide how to interpret the[39;49;00m[37m[39;49;00m$
[37m                      [39;49;00m[37m;; current input.[39;49;00m[37m[39;49;00m$
[37m                      [39;49;00m([36mthrow[39;49;00m[37m [39;49;00m[33m'read-key[39;49;00m[37m [39;49;00m[31mkeys[39;49;00m)))))))[37m[39;49;00m$
[37m    [39;49;00m([34munwind-protect[39;49;00m[37m[39;49;00m$
[37m        [39;49;00m([34mprogn[39;49;00m[37m[39;49;00m$
[37m^I  [39;49;00m([32muse-global-map[39;49;00m[37m[39;49;00m$
[37m           [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mmap[39;49;00m[37m [39;49;00m([32mmake-sparse-keymap[39;49;00m)))[37m[39;49;00m$
[37m             [39;49;00m[37m;; Don't hide the menu-bar and tool-bar entries.[39;49;00m[37m[39;49;00m$
[37m             [39;49;00m([32mdefine-key[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m[[31mmenu-bar[39;49;00m][37m [39;49;00m([32mlookup-key[39;49;00m[37m [39;49;00m[31mglobal-map[39;49;00m[37m [39;49;00m[[31mmenu-bar[39;49;00m]))[37m[39;49;00m$
[37m             [39;49;00m([32mdefine-key[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m[[31mtool-bar[39;49;00m][37m[39;49;00m$
[37m^I       [39;49;00m[37m;; This hack avoids evaluating the :filter (Bug#9922).[39;49;00m[37m[39;49;00m$
[37m^I       [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m([32massq[39;49;00m[37m [39;49;00m[33m'tool-bar[39;49;00m[37m [39;49;00m[31mglobal-map[39;49;00m))[37m[39;49;00m$
[37m^I^I   [39;49;00m([32mlookup-key[39;49;00m[37m [39;49;00m[31mglobal-map[39;49;00m[37m [39;49;00m[[31mtool-bar[39;49;00m])))[37m[39;49;00m$
[37m             [39;49;00m[31mmap[39;49;00m))[37m[39;49;00m$
[37m          [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mkeys[39;49;00m[37m[39;49;00m$
[37m                  [39;49;00m([34mcatch[39;49;00m[37m [39;49;00m[33m'read-key[39;49;00m[37m [39;49;00m([32mread-key-sequence-vector[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mt[39;49;00m)))[37m[39;49;00m$
[37m                 [39;49;00m([31mkey[39;49;00m[37m [39;49;00m([32maref[39;49;00m[37m [39;49;00m[31mkeys[39;49;00m[37m [39;49;00m[34m0[39;49;00m)))[37m[39;49;00m$
[37m            [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31mkeys[39;49;00m)[37m [39;49;00m[34m1[39;49;00m)[37m[39;49;00m$
[37m                     [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m'([31mmode-line[39;49;00m[37m [39;49;00m[31mheader-line[39;49;00m[37m[39;49;00m$
[37m                                 [39;49;00m[31mleft-fringe[39;49;00m[37m [39;49;00m[31mright-fringe[39;49;00m)))[37m[39;49;00m$
[37m                [39;49;00m([32maref[39;49;00m[37m [39;49;00m[31mkeys[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m[39;49;00m$
[37m              [39;49;00m[31mkey[39;49;00m)))[37m[39;49;00m$
[37m      [39;49;00m([31mcancel-timer[39;49;00m[37m [39;49;00m[31mtimer[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m([32muse-global-map[39;49;00m[37m [39;49;00m[31mold-global-map[39;49;00m))))[37m[39;49;00m$
[37m[39;49;00m$
([34mdefvar[39;49;00m[37m [39;49;00m[31mread-passwd-map[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; BEWARE: `defconst' would purecopy it, breaking the sharing with[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; minibuffer-local-map along the way![39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mmap[39;49;00m[37m [39;49;00m([32mmake-sparse-keymap[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m([32mset-keymap-parent[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m[31mminibuffer-local-map[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([32mdefine-key[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\C[39;49;00m[33m-u[39;49;00m[33m"[39;49;00m[37m [39;49;00m[32m#'[39;49;00m[31mdelete-minibuffer-contents[39;49;00m)[37m [39;49;00m[37m;bug#12570[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[31mmap[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mKeymap used while reading passwords.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mread-passwd[39;49;00m[37m [39;49;00m([31mprompt[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mconfirm[39;49;00m[37m [39;49;00m[31mdefault[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mRead a password, prompting with PROMPT, and return it.[39;49;00m$
[33mIf optional CONFIRM is non-nil, read the password twice to make sure.[39;49;00m$
[33mOptional DEFAULT is a default password to use instead of empty input.[39;49;00m$
[33m[39;49;00m$
[33mThis function echoes [39;49;00m[33m`.'[39;49;00m[33m for each character that the user types.[39;49;00m$
[33mYou could let-bind [39;49;00m[33m`read-hide-char'[39;49;00m[33m to another hiding character, though.[39;49;00m$
[33m[39;49;00m$
[33mOnce the caller uses the password, it can erase the password[39;49;00m$
[33mby doing (clear-string STRING).[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mconfirm[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m([31msuccess[39;49;00m)[37m[39;49;00m$
[37m        [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m[31msuccess[39;49;00m)[37m[39;49;00m$
[37m          [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mfirst[39;49;00m[37m [39;49;00m([31mread-passwd[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mdefault[39;49;00m))[37m[39;49;00m$
[37m                [39;49;00m([31msecond[39;49;00m[37m [39;49;00m([31mread-passwd[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mConfirm password: [39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mdefault[39;49;00m)))[37m[39;49;00m$
[37m            [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mequal[39;49;00m[37m [39;49;00m[31mfirst[39;49;00m[37m [39;49;00m[31msecond[39;49;00m)[37m[39;49;00m$
[37m                [39;49;00m([34mprogn[39;49;00m[37m[39;49;00m$
[37m                  [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32marrayp[39;49;00m[37m [39;49;00m[31msecond[39;49;00m)[37m [39;49;00m([32mclear-string[39;49;00m[37m [39;49;00m[31msecond[39;49;00m))[37m[39;49;00m$
[37m                  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31msuccess[39;49;00m[37m [39;49;00m[31mfirst[39;49;00m))[37m[39;49;00m$
[37m              [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32marrayp[39;49;00m[37m [39;49;00m[31mfirst[39;49;00m)[37m [39;49;00m([32mclear-string[39;49;00m[37m [39;49;00m[31mfirst[39;49;00m))[37m[39;49;00m$
[37m              [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32marrayp[39;49;00m[37m [39;49;00m[31msecond[39;49;00m)[37m [39;49;00m([32mclear-string[39;49;00m[37m [39;49;00m[31msecond[39;49;00m))[37m[39;49;00m$
[37m              [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mPassword not repeated accurately; please start over[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m              [39;49;00m([31msit-for[39;49;00m[37m [39;49;00m[34m1[39;49;00m))))[37m[39;49;00m$
[37m        [39;49;00m[31msuccess[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mhide-chars-fun[39;49;00m[37m[39;49;00m$
[37m           [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31mbeg[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[31m_len[39;49;00m)[37m[39;49;00m$
[37m             [39;49;00m([32mclear-this-command-keys[39;49;00m)[37m[39;49;00m$
[37m             [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m[37m [39;49;00m([32mmin[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m([32mmax[39;49;00m[37m [39;49;00m([32mminibuffer-prompt-end[39;49;00m)[37m[39;49;00m$
[37m                                     [39;49;00m[31mbeg[39;49;00m)))[37m[39;49;00m$
[37m             [39;49;00m([36mdotimes[39;49;00m[37m [39;49;00m([31mi[39;49;00m[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m))[37m[39;49;00m$
[37m               [39;49;00m([32mput-text-property[39;49;00m[37m [39;49;00m([32m+[39;49;00m[37m [39;49;00m[31mi[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m)[37m [39;49;00m([32m+[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mi[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m)[37m[39;49;00m$
[37m                                  [39;49;00m[33m'display[39;49;00m[37m [39;49;00m([32mstring[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mread-hide-char[39;49;00m[37m [39;49;00m[33m?.[39;49;00m))))))[37m[39;49;00m$
[37m          [39;49;00m[31mminibuf[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m([31mminibuffer-with-setup-hook[39;49;00m[37m[39;49;00m$
[37m          [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m()[37m[39;49;00m$
[37m            [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mminibuf[39;49;00m[37m [39;49;00m([32mcurrent-buffer[39;49;00m))[37m[39;49;00m$
[37m            [39;49;00m[37m;; Turn off electricity.[39;49;00m[37m[39;49;00m$
[37m            [39;49;00m([36msetq-local[39;49;00m[37m [39;49;00m[31mpost-self-insert-hook[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
[37m            [39;49;00m([36msetq-local[39;49;00m[37m [39;49;00m[31mbuffer-undo-list[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
[37m            [39;49;00m([36msetq-local[39;49;00m[37m [39;49;00m[31mselect-active-regions[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
[37m            [39;49;00m([32muse-local-map[39;49;00m[37m [39;49;00m[31mread-passwd-map[39;49;00m)[37m[39;49;00m$
[37m            [39;49;00m([36msetq-local[39;49;00m[37m [39;49;00m[31minhibit-modification-hooks[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m [39;49;00m[37m;bug#15501.[39;49;00m[37m[39;49;00m$
[37m^I    [39;49;00m([36msetq-local[39;49;00m[37m [39;49;00m[31mshow-paren-mode[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m^I^I[39;49;00m[37m;bug#16091.[39;49;00m[37m[39;49;00m$
[37m            [39;49;00m([31madd-hook[39;49;00m[37m [39;49;00m[33m'after-change-functions[39;49;00m[37m [39;49;00m[31mhide-chars-fun[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[33m'local[39;49;00m))[37m[39;49;00m$
[37m        [39;49;00m([34munwind-protect[39;49;00m[37m[39;49;00m$
[37m            [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31menable-recursive-minibuffers[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
[37m^I^I  [39;49;00m([31mread-hide-char[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mread-hide-char[39;49;00m[37m [39;49;00m[33m?.[39;49;00m)))[37m[39;49;00m$
[37m              [39;49;00m([32mread-string[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m[31mdefault[39;49;00m))[37m [39;49;00m[37m; t = "no history"[39;49;00m[37m[39;49;00m$
[37m          [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mbuffer-live-p[39;49;00m[37m [39;49;00m[31mminibuf[39;49;00m)[37m[39;49;00m$
[37m            [39;49;00m([36mwith-current-buffer[39;49;00m[37m [39;49;00m[31mminibuf[39;49;00m[37m[39;49;00m$
[37m              [39;49;00m[37m;; Not sure why but it seems that there might be cases where the[39;49;00m[37m[39;49;00m$
[37m              [39;49;00m[37m;; minibuffer is not always properly reset later on, so undo[39;49;00m[37m[39;49;00m$
[37m              [39;49;00m[37m;; whatever we've done here (bug#11392).[39;49;00m[37m[39;49;00m$
[37m              [39;49;00m([31mremove-hook[39;49;00m[37m [39;49;00m[33m'after-change-functions[39;49;00m[37m [39;49;00m[31mhide-chars-fun[39;49;00m[37m [39;49;00m[33m'local[39;49;00m)[37m[39;49;00m$
[37m              [39;49;00m([32mkill-local-variable[39;49;00m[37m [39;49;00m[33m'post-self-insert-hook[39;49;00m)[37m[39;49;00m$
[37m              [39;49;00m[37m;; And of course, don't keep the sensitive data around.[39;49;00m[37m[39;49;00m$
[37m              [39;49;00m([32merase-buffer[39;49;00m))))))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mread-number[39;49;00m[37m [39;49;00m([31mprompt[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mdefault[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mRead a numeric value in the minibuffer, prompting with PROMPT.[39;49;00m$
[33mDEFAULT specifies a default value to return if the user just types RET.[39;49;00m$
[33mThe value of DEFAULT is inserted into PROMPT.[39;49;00m$
[33mThis function is used by the [39;49;00m[33m`interactive'[39;49;00m[33m code letter [39;49;00m[33m`n'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mn[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
[37m^I[39;49;00m([31mdefault1[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mdefault[39;49;00m)[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mdefault[39;49;00m)[37m [39;49;00m[31mdefault[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31mdefault1[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m[37m[39;49;00m$
[37m^I    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m([39;49;00m[33m\\[39;49;00m[33m):[ [39;49;00m[33m\t[39;49;00m[33m]*[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m)[37m[39;49;00m$
[37m^I^I[39;49;00m([32mreplace-match[39;49;00m[37m [39;49;00m([32mformat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m (default %s)[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mdefault1[39;49;00m)[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m[39;49;00m$
[37m^I      [39;49;00m([31mreplace-regexp-in-string[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m[ [39;49;00m[33m\t[39;49;00m[33m]*[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m([32mformat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m (default %s) [39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mdefault1[39;49;00m)[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m[31mprompt[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m[31mt[39;49;00m))))[37m[39;49;00m$
[37m    [39;49;00m([34mwhile[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00m([34mprogn[39;49;00m[37m[39;49;00m$
[37m^I  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mstr[39;49;00m[37m [39;49;00m([32mread-from-minibuffer[39;49;00m[37m[39;49;00m$
[37m^I^I      [39;49;00m[31mprompt[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m$
[37m^I^I      [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31mdefault[39;49;00m[37m[39;49;00m$
[37m^I^I^I[39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mdefault[39;49;00m)[37m[39;49;00m$
[37m^I^I^I    [39;49;00m([32mmapcar[39;49;00m[37m [39;49;00m[33m'number-to-string[39;49;00m[37m [39;49;00m([32mdelq[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mdefault[39;49;00m))[37m[39;49;00m$
[37m^I^I^I  [39;49;00m([32mnumber-to-string[39;49;00m[37m [39;49;00m[31mdefault[39;49;00m))))))[37m[39;49;00m$
[37m^I    [39;49;00m([34mcondition-case[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m$
[37m^I^I[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mn[39;49;00m[37m [39;49;00m([34mcond[39;49;00m[37m[39;49;00m$
[37m^I^I^I [39;49;00m(([31mzerop[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31mstr[39;49;00m))[37m [39;49;00m[31mdefault1[39;49;00m)[37m[39;49;00m$
[37m^I^I^I [39;49;00m(([32mstringp[39;49;00m[37m [39;49;00m[31mstr[39;49;00m)[37m [39;49;00m([32mread[39;49;00m[37m [39;49;00m[31mstr[39;49;00m))))[37m[39;49;00m$
[37m^I      [39;49;00m([36merror[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)))[37m[39;49;00m$
[37m^I  [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32mnumberp[39;49;00m[37m [39;49;00m[31mn[39;49;00m)[37m[39;49;00m$
[37m^I    [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mPlease enter a number.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m^I    [39;49;00m([31msit-for[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m[39;49;00m$
[37m^I    [39;49;00m[31mt[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m[31mn[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mread-char-choice[39;49;00m[37m [39;49;00m([31mprompt[39;49;00m[37m [39;49;00m[31mchars[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31minhibit-keyboard-quit[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mRead and return one of CHARS, prompting for PROMPT.[39;49;00m$
[33mAny input that is not one of CHARS is ignored.[39;49;00m$
[33m[39;49;00m$
[33mIf optional argument INHIBIT-KEYBOARD-QUIT is non-nil, ignore[39;49;00m$
[33mkeyboard-quit events while waiting for a valid input.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mchars[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([36merror[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mCalled [39;49;00m[33m`read-char-choice'[39;49;00m[33m without valid char choices[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m([31mchar[39;49;00m[37m [39;49;00m[31mdone[39;49;00m[37m [39;49;00m[31mshow-help[39;49;00m[37m [39;49;00m([31mhelpbuf[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m *Char Help*[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mcursor-in-echo-area[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
[37m          [39;49;00m([31mexecuting-kbd-macro[39;49;00m[37m [39;49;00m[31mexecuting-kbd-macro[39;49;00m)[37m[39;49;00m$
[37m^I  [39;49;00m([31mesc-flag[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m$
[37m      [39;49;00m([36msave-window-excursion[39;49;00m[37m^I      [39;49;00m[37m; in case we call help-form-show[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m[31mdone[39;49;00m)[37m[39;49;00m$
[37m^I  [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32mget-text-property[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[33m'face[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m)[37m[39;49;00m$
[37m^I    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m[37m [39;49;00m([32mpropertize[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m[37m [39;49;00m[33m'face[39;49;00m[37m [39;49;00m[33m'minibuffer-prompt[39;49;00m)))[37m[39;49;00m$
[37m^I  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mchar[39;49;00m[37m [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31minhibit-quit[39;49;00m[37m [39;49;00m[31minhibit-keyboard-quit[39;49;00m))[37m[39;49;00m$
[37m^I^I       [39;49;00m([31mread-key[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m)))[37m[39;49;00m$
[37m^I  [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mshow-help[39;49;00m[37m [39;49;00m([32mbuffer-live-p[39;49;00m[37m [39;49;00m([32mget-buffer[39;49;00m[37m [39;49;00m[31mhelpbuf[39;49;00m))[37m[39;49;00m$
[37m^I       [39;49;00m([32mkill-buffer[39;49;00m[37m [39;49;00m[31mhelpbuf[39;49;00m))[37m[39;49;00m$
[37m^I  [39;49;00m([34mcond[39;49;00m[37m[39;49;00m$
[37m^I   [39;49;00m(([31mnot[39;49;00m[37m [39;49;00m([32mnumberp[39;49;00m[37m [39;49;00m[31mchar[39;49;00m)))[37m[39;49;00m$
[37m^I   [39;49;00m[37m;; If caller has set help-form, that's enough.[39;49;00m[37m[39;49;00m$
[37m^I   [39;49;00m[37m;; They don't explicitly have to add help-char to chars.[39;49;00m[37m[39;49;00m$
[37m^I   [39;49;00m(([34mand[39;49;00m[37m [39;49;00m[31mhelp-form[39;49;00m[37m[39;49;00m$
[37m^I^I [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mchar[39;49;00m[37m [39;49;00m[31mhelp-char[39;49;00m)[37m[39;49;00m$
[37m^I^I [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mshow-help[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
[37m^I^I [39;49;00m([31mhelp-form-show[39;49;00m)))[37m[39;49;00m$
[37m^I   [39;49;00m(([32mmemq[39;49;00m[37m [39;49;00m[31mchar[39;49;00m[37m [39;49;00m[31mchars[39;49;00m)[37m[39;49;00m$
[37m^I    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mdone[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
[37m^I   [39;49;00m(([34mand[39;49;00m[37m [39;49;00m[31mexecuting-kbd-macro[39;49;00m[37m [39;49;00m([32m=[39;49;00m[37m [39;49;00m[31mchar[39;49;00m[37m [39;49;00m[34m-1[39;49;00m))[37m[39;49;00m$
[37m^I    [39;49;00m[37m;; read-event returns -1 if we are in a kbd macro and[39;49;00m[37m[39;49;00m$
[37m^I    [39;49;00m[37m;; there are no more events in the macro.  Attempt to[39;49;00m[37m[39;49;00m$
[37m^I    [39;49;00m[37m;; get an event interactively.[39;49;00m[37m[39;49;00m$
[37m^I    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mexecuting-kbd-macro[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m$
[37m^I   [39;49;00m(([31mnot[39;49;00m[37m [39;49;00m[31minhibit-keyboard-quit[39;49;00m)[37m[39;49;00m$
[37m^I    [39;49;00m([34mcond[39;49;00m[37m[39;49;00m$
[37m^I     [39;49;00m(([34mand[39;49;00m[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[31mesc-flag[39;49;00m)[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mchar[39;49;00m[37m [39;49;00m[33m?\e[39;49;00m))[37m[39;49;00m$
[37m^I      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mesc-flag[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
[37m^I     [39;49;00m(([32mmemq[39;49;00m[37m [39;49;00m[31mchar[39;49;00m[37m [39;49;00m'([33m?\C[39;49;00m[31m-g[39;49;00m[37m [39;49;00m[33m?\e[39;49;00m))[37m[39;49;00m$
[37m^I      [39;49;00m([31mkeyboard-quit[39;49;00m))))))))[37m[39;49;00m$
[37m    [39;49;00m[37m;; Display the question with the answer.  But without cursor-in-echo-area.[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m%s%s[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m[37m [39;49;00m([32mchar-to-string[39;49;00m[37m [39;49;00m[31mchar[39;49;00m))[37m[39;49;00m$
[37m    [39;49;00m[31mchar[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31msit-for[39;49;00m[37m [39;49;00m([31mseconds[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mnodisp[39;49;00m[37m [39;49;00m[31mobsolete[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mRedisplay, then wait for SECONDS seconds.  Stop when input is available.[39;49;00m$
[33mSECONDS may be a floating-point value.[39;49;00m$
[33m\([39;49;00m[33mOn operating systems that do not support waiting for fractions of a[39;49;00m$
[33msecond, floating-point values are rounded down to the nearest integer.)[39;49;00m$
[33m[39;49;00m$
[33mIf optional arg NODISP is t, don't redisplay, just wait for input.[39;49;00m$
[33mRedisplay does not happen if input is available before it starts.[39;49;00m$
[33m[39;49;00m$
[33mValue is t if waited the full time with no input arriving, and nil otherwise.[39;49;00m$
[33m[39;49;00m$
[33mAn obsolete, but still supported form is[39;49;00m$
[33m\([39;49;00m[33msit-for SECONDS &optional MILLISECONDS NODISP)[39;49;00m$
[33mwhere the optional arg MILLISECONDS specifies an additional wait period,[39;49;00m$
[33min milliseconds; this was useful when Emacs was built without[39;49;00m$
[33mfloating point support.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31madvertised-calling-convention[39;49;00m[37m [39;49;00m([31mseconds[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mnodisp[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m22.1[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m[37m;; This used to be implemented in C until the following discussion:[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; http://lists.gnu.org/archive/html/emacs-devel/2006-07/msg00401.html[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; Then it was moved here using an implementation based on an idle timer,[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; which was then replaced by the use of read-event.[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mnumberp[39;49;00m[37m [39;49;00m[31mnodisp[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mseconds[39;49;00m[37m [39;49;00m([32m+[39;49;00m[37m [39;49;00m[31mseconds[39;49;00m[37m [39;49;00m([32m*[39;49;00m[37m [39;49;00m[34m1e-3[39;49;00m[37m [39;49;00m[31mnodisp[39;49;00m))[37m[39;49;00m$
[37m            [39;49;00m[31mnodisp[39;49;00m[37m [39;49;00m[31mobsolete[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mobsolete[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mnodisp[39;49;00m[37m [39;49;00m[31mobsolete[39;49;00m)))[37m[39;49;00m$
[37m  [39;49;00m([34mcond[39;49;00m[37m[39;49;00m$
[37m   [39;49;00m([31mnoninteractive[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m([32msleep-for[39;49;00m[37m [39;49;00m[31mseconds[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
[37m   [39;49;00m(([32minput-pending-p[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
[37m   [39;49;00m(([32m<=[39;49;00m[37m [39;49;00m[31mseconds[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mnodisp[39;49;00m[37m [39;49;00m([32mredisplay[39;49;00m)))[37m[39;49;00m$
[37m   [39;49;00m([31mt[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mnodisp[39;49;00m[37m [39;49;00m([32mredisplay[39;49;00m))[37m[39;49;00m$
[37m    [39;49;00m[37m;; FIXME: we should not read-event here at all, because it's much too[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[37m;; difficult to reliably "undo" a read-event by pushing it onto[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[37m;; unread-command-events.[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[37m;; For bug#14782, we need read-event to do the keyboard-coding-system[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[37m;; decoding (hence non-nil as second arg under POSIX ttys).[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[37m;; For bug#15614, we need read-event not to inherit-input-method.[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[37m;; So we temporarily suspend input-method-function.[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([32mread[39;49;00m[37m [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31minput-method-function[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m$
[37m                  [39;49;00m([32mread-event[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m[31mseconds[39;49;00m))))[37m[39;49;00m$
[37m      [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[32mread[39;49;00m)[37m[39;49;00m$
[37m^I  [39;49;00m([34mprogn[39;49;00m[37m[39;49;00m$
[37m            [39;49;00m[37m;; https://lists.gnu.org/archive/html/emacs-devel/2006-10/msg00394.html[39;49;00m[37m[39;49;00m$
[37m            [39;49;00m[37m;; We want `read' appear in the next command's this-command-event[39;49;00m[37m[39;49;00m$
[37m            [39;49;00m[37m;; but not in the current one.[39;49;00m[37m[39;49;00m$
[37m            [39;49;00m[37m;; By pushing (cons t read), we indicate that `read' has not[39;49;00m[37m[39;49;00m$
[37m            [39;49;00m[37m;; yet been recorded in this-command-keys, so it will be recorded[39;49;00m[37m[39;49;00m$
[37m            [39;49;00m[37m;; next time it's read.[39;49;00m[37m[39;49;00m$
[37m            [39;49;00m[37m;; And indeed the `seconds' argument to read-event correctly[39;49;00m[37m[39;49;00m$
[37m            [39;49;00m[37m;; prevented recording this event in the current command's[39;49;00m[37m[39;49;00m$
[37m            [39;49;00m[37m;; this-command-keys.[39;49;00m[37m[39;49;00m$
[37m^I    [39;49;00m([36mpush[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m[32mread[39;49;00m)[37m [39;49;00m[31munread-command-events[39;49;00m)[37m[39;49;00m$
[37m^I    [39;49;00m[31mnil[39;49;00m))))))[37m[39;49;00m$
[37m[39;49;00m$
[37m;; Behind display-popup-menus-p test.[39;49;00m[37m[39;49;00m$
([36mdeclare-function[39;49;00m[37m [39;49;00m[32mx-popup-dialog[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mmenu.c[39;49;00m[33m"[39;49;00m[37m [39;49;00m([31mposition[39;49;00m[37m [39;49;00m[31mcontents[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mheader[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31my-or-n-p[39;49;00m[37m [39;49;00m([31mprompt[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mAsk user a [39;49;00m[33m\"[39;49;00m[33my or n[39;49;00m[33m\"[39;49;00m[33m question.  Return t if answer is [39;49;00m[33m\"[39;49;00m[33my[39;49;00m[33m\"[39;49;00m[33m.[39;49;00m$
[33mPROMPT is the string to display to ask the question.  It should[39;49;00m$
[33mend in a space; [39;49;00m[33m`y-or-n-p'[39;49;00m[33m adds [39;49;00m[33m\"[39;49;00m[33m(y or n) [39;49;00m[33m\"[39;49;00m[33m to it.[39;49;00m$
[33m[39;49;00m$
[33mNo confirmation of the answer is requested; a single character is[39;49;00m$
[33menough.  SPC also means yes, and DEL means no.[39;49;00m$
[33m[39;49;00m$
[33mTo be precise, this function translates user input into responses[39;49;00m$
[33mby consulting the bindings in [39;49;00m[33m`query-replace-map'[39;49;00m[33m; see the[39;49;00m$
[33mdocumentation of that variable for more information.  In this[39;49;00m$
[33mcase, the useful bindings are [39;49;00m[33m`act'[39;49;00m[33m, [39;49;00m[33m`skip'[39;49;00m[33m, [39;49;00m[33m`recenter'[39;49;00m[33m,[39;49;00m$
[33m`scroll-up'[39;49;00m[33m, [39;49;00m[33m`scroll-down'[39;49;00m[33m, and [39;49;00m[33m`quit'[39;49;00m[33m.[39;49;00m$
[33mAn [39;49;00m[33m`act'[39;49;00m[33m response means yes, and a [39;49;00m[33m`skip'[39;49;00m[33m response means no.[39;49;00m$
[33mA [39;49;00m[33m`quit'[39;49;00m[33m response means to invoke [39;49;00m[33m`keyboard-quit'[39;49;00m[33m.[39;49;00m$
[33mIf the user enters [39;49;00m[33m`recenter'[39;49;00m[33m, [39;49;00m[33m`scroll-up'[39;49;00m[33m, or [39;49;00m[33m`scroll-down'[39;49;00m[33m[39;49;00m$
[33mresponses, perform the requested window recentering or scrolling[39;49;00m$
[33mand ask again.[39;49;00m$
[33m[39;49;00m$
[33mUnder a windowing system a dialog box will be used if [39;49;00m[33m`last-nonmenu-event'[39;49;00m[33m[39;49;00m$
[33mis nil and [39;49;00m[33m`use-dialog-box'[39;49;00m[33m is non-nil.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; ¡Beware! when I tried to edebug this code, Emacs got into a weird state[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; where all the keys were unbound (i.e. it somehow got triggered[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; within read-key, apparently).  I had to kill it.[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31manswer[39;49;00m[37m [39;49;00m[33m'recenter[39;49;00m)[37m[39;49;00m$
[37m^I[39;49;00m([31mpadded[39;49;00m[37m [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31mprompt[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mdialog[39;49;00m)[37m[39;49;00m$
[37m^I^I  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31ml[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m)))[37m[39;49;00m$
[37m^I^I    [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m[37m[39;49;00m$
[37m^I^I^I    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([31mzerop[39;49;00m[37m [39;49;00m[31ml[39;49;00m)[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[33m?\s[39;49;00m[37m [39;49;00m([32maref[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m[37m [39;49;00m([32m1-[39;49;00m[37m [39;49;00m[31ml[39;49;00m))))[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[33m"[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m^I^I^I    [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mdialog[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m(y or n) [39;49;00m[33m"[39;49;00m))))))[37m[39;49;00m$
[37m    [39;49;00m([34mcond[39;49;00m[37m[39;49;00m$
[37m     [39;49;00m([31mnoninteractive[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m[37m [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mpadded[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m))[37m[39;49;00m$
[37m      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtemp-prompt[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m))[37m[39;49;00m$
[37m^I[39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[31manswer[39;49;00m[37m [39;49;00m'([31mact[39;49;00m[37m [39;49;00m[31mskip[39;49;00m)))[37m[39;49;00m$
[37m^I  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mstr[39;49;00m[37m [39;49;00m([32mread-string[39;49;00m[37m [39;49;00m[31mtemp-prompt[39;49;00m)))[37m[39;49;00m$
[37m^I    [39;49;00m([34mcond[39;49;00m[37m [39;49;00m(([32mmember[39;49;00m[37m [39;49;00m[31mstr[39;49;00m[37m [39;49;00m'([33m"[39;49;00m[33my[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mY[39;49;00m[33m"[39;49;00m))[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31manswer[39;49;00m[37m [39;49;00m[33m'act[39;49;00m))[37m[39;49;00m$
[37m^I^I  [39;49;00m(([32mmember[39;49;00m[37m [39;49;00m[31mstr[39;49;00m[37m [39;49;00m'([33m"[39;49;00m[33mn[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mN[39;49;00m[33m"[39;49;00m))[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31manswer[39;49;00m[37m [39;49;00m[33m'skip[39;49;00m))[37m[39;49;00m$
[37m^I^I  [39;49;00m([31mt[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mtemp-prompt[39;49;00m[37m [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mPlease answer y or n.  [39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I^I       [39;49;00m[31mprompt[39;49;00m))))))))[37m[39;49;00m$
[37m     [39;49;00m(([34mand[39;49;00m[37m [39;49;00m([31mdisplay-popup-menus-p[39;49;00m)[37m[39;49;00m$
[37m^I   [39;49;00m([32mlistp[39;49;00m[37m [39;49;00m[31mlast-nonmenu-event[39;49;00m)[37m[39;49;00m$
[37m^I   [39;49;00m[31muse-dialog-box[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m[37m [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mpadded[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
[37m^I    [39;49;00m[31manswer[39;49;00m[37m [39;49;00m([32mx-popup-dialog[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m`(,[31mprompt[39;49;00m[37m [39;49;00m([33m"[39;49;00m[33mYes[39;49;00m[33m"[39;49;00m[37m [39;49;00m.[37m [39;49;00m[31mact[39;49;00m)[37m [39;49;00m([33m"[39;49;00m[33mNo[39;49;00m[33m"[39;49;00m[37m [39;49;00m.[37m [39;49;00m[31mskip[39;49;00m)))))[37m[39;49;00m$
[37m     [39;49;00m([31mt[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m[37m [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mpadded[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m))[37m[39;49;00m$
[37m      [39;49;00m([34mwhile[39;49;00m[37m[39;49;00m$
[37m          [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mscroll-actions[39;49;00m[37m [39;49;00m'([32mrecenter[39;49;00m[37m [39;49;00m[32mscroll-up[39;49;00m[37m [39;49;00m[32mscroll-down[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I   [39;49;00m[32mscroll-other-window[39;49;00m[37m [39;49;00m[31mscroll-other-window-down[39;49;00m))[37m[39;49;00m$
[37m^I^I [39;49;00m([31mkey[39;49;00m[37m[39;49;00m$
[37m                  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mcursor-in-echo-area[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
[37m                    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31mminibuffer-auto-raise[39;49;00m[37m[39;49;00m$
[37m                      [39;49;00m([32mraise-frame[39;49;00m[37m [39;49;00m([32mwindow-frame[39;49;00m[37m [39;49;00m([32mminibuffer-window[39;49;00m))))[37m[39;49;00m$
[37m                    [39;49;00m([31mread-key[39;49;00m[37m [39;49;00m([32mpropertize[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[31manswer[39;49;00m[37m [39;49;00m[31mscroll-actions[39;49;00m)[37m[39;49;00m$
[37m                                              [39;49;00m[31mprompt[39;49;00m[37m[39;49;00m$
[37m                                            [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mPlease answer y or n.  [39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m                                                    [39;49;00m[31mprompt[39;49;00m))[37m[39;49;00m$
[37m                                          [39;49;00m[33m'face[39;49;00m[37m [39;49;00m[33m'minibuffer-prompt[39;49;00m)))))[37m[39;49;00m$
[37m            [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31manswer[39;49;00m[37m [39;49;00m([32mlookup-key[39;49;00m[37m [39;49;00m[31mquery-replace-map[39;49;00m[37m [39;49;00m([32mvector[39;49;00m[37m [39;49;00m[31mkey[39;49;00m)[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
[37m            [39;49;00m([34mcond[39;49;00m[37m[39;49;00m$
[37m^I     [39;49;00m(([32mmemq[39;49;00m[37m [39;49;00m[31manswer[39;49;00m[37m [39;49;00m'([31mskip[39;49;00m[37m [39;49;00m[31mact[39;49;00m))[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
[37m^I     [39;49;00m(([32meq[39;49;00m[37m [39;49;00m[31manswer[39;49;00m[37m [39;49;00m[33m'recenter[39;49;00m)[37m[39;49;00m$
[37m^I      [39;49;00m([32mrecenter[39;49;00m)[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
[37m^I     [39;49;00m(([32meq[39;49;00m[37m [39;49;00m[31manswer[39;49;00m[37m [39;49;00m[33m'scroll-up[39;49;00m)[37m[39;49;00m$
[37m^I      [39;49;00m([36mignore-errors[39;49;00m[37m [39;49;00m([31mscroll-up-command[39;49;00m))[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
[37m^I     [39;49;00m(([32meq[39;49;00m[37m [39;49;00m[31manswer[39;49;00m[37m [39;49;00m[33m'scroll-down[39;49;00m)[37m[39;49;00m$
[37m^I      [39;49;00m([36mignore-errors[39;49;00m[37m [39;49;00m([31mscroll-down-command[39;49;00m))[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
[37m^I     [39;49;00m(([32meq[39;49;00m[37m [39;49;00m[31manswer[39;49;00m[37m [39;49;00m[33m'scroll-other-window[39;49;00m)[37m[39;49;00m$
[37m^I      [39;49;00m([36mignore-errors[39;49;00m[37m [39;49;00m([32mscroll-other-window[39;49;00m))[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
[37m^I     [39;49;00m(([32meq[39;49;00m[37m [39;49;00m[31manswer[39;49;00m[37m [39;49;00m[33m'scroll-other-window-down[39;49;00m)[37m[39;49;00m$
[37m^I      [39;49;00m([36mignore-errors[39;49;00m[37m [39;49;00m([31mscroll-other-window-down[39;49;00m))[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
[37m^I     [39;49;00m(([34mor[39;49;00m[37m [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[31manswer[39;49;00m[37m [39;49;00m'([31mexit-prefix[39;49;00m[37m [39;49;00m[31mquit[39;49;00m))[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mkey[39;49;00m[37m [39;49;00m[33m?\e[39;49;00m))[37m[39;49;00m$
[37m^I      [39;49;00m([32msignal[39;49;00m[37m [39;49;00m[33m'quit[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
[37m^I     [39;49;00m([31mt[39;49;00m[37m [39;49;00m[31mt[39;49;00m)))[37m[39;49;00m$
[37m        [39;49;00m([32mding[39;49;00m)[37m[39;49;00m$
[37m        [39;49;00m([32mdiscard-input[39;49;00m))))[37m[39;49;00m$
[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mret[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31manswer[39;49;00m[37m [39;49;00m[33m'act[39;49;00m)))[37m[39;49;00m$
[37m      [39;49;00m([36munless[39;49;00m[37m [39;49;00m[31mnoninteractive[39;49;00m[37m[39;49;00m$
[37m        [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m%s%c[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mprompt[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mret[39;49;00m[37m [39;49;00m[33m?y[39;49;00m[37m [39;49;00m[33m?n[39;49;00m)))[37m[39;49;00m$
[37m      [39;49;00m[31mret[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m[37m[39;49;00m$
[37m;;; Atomic change groups.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
([36mdefmacro[39;49;00m[37m [39;49;00m[36matomic-change-group[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mPerform BODY as an atomic change group.[39;49;00m$
[33mThis means that if BODY exits abnormally,[39;49;00m$
[33mall of its changes to the current buffer are undone.[39;49;00m$
[33mThis works regardless of whether undo is enabled in the buffer.[39;49;00m$
[33m[39;49;00m$
[33mThis mechanism is transparent to ordinary use of undo;[39;49;00m$
[33mif undo is enabled in the buffer and BODY succeeds, the[39;49;00m$
[33muser can undo the change normally.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mhandle[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m--change-group-handle--[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
[37m^I[39;49;00m([31msuccess[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m--change-group-success--[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m((,[31mhandle[39;49;00m[37m [39;49;00m([31mprepare-change-group[39;49;00m))[37m[39;49;00m$
[37m^I   [39;49;00m[37m;; Don't truncate any undo data in the middle of this.[39;49;00m[37m[39;49;00m$
[37m^I   [39;49;00m([31mundo-outer-limit[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
[37m^I   [39;49;00m([31mundo-limit[39;49;00m[37m [39;49;00m[31mmost-positive-fixnum[39;49;00m)[37m[39;49;00m$
[37m^I   [39;49;00m([31mundo-strong-limit[39;49;00m[37m [39;49;00m[31mmost-positive-fixnum[39;49;00m)[37m[39;49;00m$
[37m^I   [39;49;00m(,[31msuccess[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m$
[37m       [39;49;00m([34munwind-protect[39;49;00m[37m[39;49;00m$
[37m^I   [39;49;00m([34mprogn[39;49;00m[37m[39;49;00m$
[37m^I     [39;49;00m[37m;; This is inside the unwind-protect because[39;49;00m[37m[39;49;00m$
[37m^I     [39;49;00m[37m;; it enables undo if that was disabled; we need[39;49;00m[37m[39;49;00m$
[37m^I     [39;49;00m[37m;; to make sure that it gets disabled again.[39;49;00m[37m[39;49;00m$
[37m^I     [39;49;00m([31mactivate-change-group[39;49;00m[37m [39;49;00m,[31mhandle[39;49;00m)[37m[39;49;00m$
[37m^I     [39;49;00m,@[31mbody[39;49;00m[37m[39;49;00m$
[37m^I     [39;49;00m([34msetq[39;49;00m[37m [39;49;00m,[31msuccess[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
[37m^I [39;49;00m[37m;; Either of these functions will disable undo[39;49;00m[37m[39;49;00m$
[37m^I [39;49;00m[37m;; if it was disabled before.[39;49;00m[37m[39;49;00m$
[37m^I [39;49;00m([34mif[39;49;00m[37m [39;49;00m,[31msuccess[39;49;00m[37m[39;49;00m$
[37m^I     [39;49;00m([31maccept-change-group[39;49;00m[37m [39;49;00m,[31mhandle[39;49;00m)[37m[39;49;00m$
[37m^I   [39;49;00m([31mcancel-change-group[39;49;00m[37m [39;49;00m,[31mhandle[39;49;00m))))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mprepare-change-group[39;49;00m[37m [39;49;00m([34m&optional[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn a handle for the current buffer's state, for a change group.[39;49;00m$
[33mIf you specify BUFFER, make a handle for BUFFER's state instead.[39;49;00m$
[33m[39;49;00m$
[33mPass the handle to [39;49;00m[33m`activate-change-group'[39;49;00m[33m afterward to initiate[39;49;00m$
[33mthe actual changes of the change group.[39;49;00m$
[33m[39;49;00m$
[33mTo finish the change group, call either [39;49;00m[33m`accept-change-group'[39;49;00m[33m or[39;49;00m$
[33m`cancel-change-group'[39;49;00m[33m passing the same handle as argument.  Call[39;49;00m$
[33m`accept-change-group'[39;49;00m[33m to accept the changes in the group as final;[39;49;00m$
[33mcall [39;49;00m[33m`cancel-change-group'[39;49;00m[33m to undo them all.  You should use[39;49;00m$
[33m`unwind-protect'[39;49;00m[33m to make sure the group is always finished.  The call[39;49;00m$
[33mto [39;49;00m[33m`activate-change-group'[39;49;00m[33m should be inside the [39;49;00m[33m`unwind-protect'[39;49;00m[33m.[39;49;00m$
[33mOnce you finish the group, don't use the handle again--don't try to[39;49;00m$
[33mfinish the same group twice.  For a simple example of correct use, see[39;49;00m$
[33mthe source code of [39;49;00m[33m`atomic-change-group'[39;49;00m[33m.[39;49;00m$
[33m[39;49;00m$
[33mThe handle records only the specified buffer.  To make a multibuffer[39;49;00m$
[33mchange group, call this function once for each buffer you want to[39;49;00m$
[33mcover, then use [39;49;00m[33m`nconc'[39;49;00m[33m to combine the returned values, like this:[39;49;00m$
[33m[39;49;00m$
[33m  (nconc (prepare-change-group buffer-1)[39;49;00m$
[33m         (prepare-change-group buffer-2))[39;49;00m$
[33m[39;49;00m$
[33mYou can then activate that multibuffer change group with a single[39;49;00m$
[33mcall to [39;49;00m[33m`activate-change-group'[39;49;00m[33m and finish it with a single call[39;49;00m$
[33mto [39;49;00m[33m`accept-change-group'[39;49;00m[33m or [39;49;00m[33m`cancel-change-group'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([32mlist[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m [39;49;00m([36mwith-current-buffer[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m [39;49;00m[31mbuffer-undo-list[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m([32mlist[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m([32mcurrent-buffer[39;49;00m)[37m [39;49;00m[31mbuffer-undo-list[39;49;00m))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mactivate-change-group[39;49;00m[37m [39;49;00m([31mhandle[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mActivate a change group made with [39;49;00m[33m`prepare-change-group'[39;49;00m[33m (which see).[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdolist[39;49;00m[37m [39;49;00m([32melt[39;49;00m[37m [39;49;00m[31mhandle[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([36mwith-current-buffer[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[32melt[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mbuffer-undo-list[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
[37m^I  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbuffer-undo-list[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31maccept-change-group[39;49;00m[37m [39;49;00m([31mhandle[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mFinish a change group made with [39;49;00m[33m`prepare-change-group'[39;49;00m[33m (which see).[39;49;00m$
[33mThis finishes the change group by accepting its changes as final.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdolist[39;49;00m[37m [39;49;00m([32melt[39;49;00m[37m [39;49;00m[31mhandle[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([36mwith-current-buffer[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[32melt[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[32melt[39;49;00m)[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
[37m^I  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbuffer-undo-list[39;49;00m[37m [39;49;00m[31mt[39;49;00m)))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mcancel-change-group[39;49;00m[37m [39;49;00m([31mhandle[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mFinish a change group made with [39;49;00m[33m`prepare-change-group'[39;49;00m[33m (which see).[39;49;00m$
[33mThis finishes the change group by reverting all of its changes.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdolist[39;49;00m[37m [39;49;00m([32melt[39;49;00m[37m [39;49;00m[31mhandle[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([36mwith-current-buffer[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[32melt[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[32melt[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[32melt[39;49;00m))[37m[39;49;00m$
[37m      [39;49;00m([34msave-restriction[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00m[37m;; Widen buffer temporarily so if the buffer was narrowed within[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00m[37m;; the body of `atomic-change-group' all changes can be undone.[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00m([32mwiden[39;49;00m)[37m[39;49;00m$
[37m^I[39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mold-car[39;49;00m[37m[39;49;00m$
[37m^I       [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[32melt[39;49;00m)[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[32melt[39;49;00m)))[37m[39;49;00m$
[37m^I      [39;49;00m([31mold-cdr[39;49;00m[37m[39;49;00m$
[37m^I       [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[32melt[39;49;00m)[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[32melt[39;49;00m))))[37m[39;49;00m$
[37m^I  [39;49;00m[37m;; Temporarily truncate the undo log at ELT.[39;49;00m[37m[39;49;00m$
[37m^I  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[32melt[39;49;00m)[37m[39;49;00m$
[37m^I    [39;49;00m([32msetcar[39;49;00m[37m [39;49;00m[32melt[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m [39;49;00m([32msetcdr[39;49;00m[37m [39;49;00m[32melt[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m$
[37m^I  [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mlast-command[39;49;00m[37m [39;49;00m[33m'undo[39;49;00m)[37m [39;49;00m([31mundo-start[39;49;00m))[37m[39;49;00m$
[37m^I  [39;49;00m[37m;; Make sure there's no confusion.[39;49;00m[37m[39;49;00m$
[37m^I  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[32melt[39;49;00m)[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[32melt[39;49;00m[37m [39;49;00m([31mlast[39;49;00m[37m [39;49;00m[31mpending-undo-list[39;49;00m))))[37m[39;49;00m$
[37m^I    [39;49;00m([36merror[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mUndoing to some unrelated state[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
[37m^I  [39;49;00m[37m;; Undo it all.[39;49;00m[37m[39;49;00m$
[37m^I  [39;49;00m([34msave-excursion[39;49;00m[37m[39;49;00m$
[37m^I    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32mlistp[39;49;00m[37m [39;49;00m[31mpending-undo-list[39;49;00m)[37m [39;49;00m([31mundo-more[39;49;00m[37m [39;49;00m[34m1[39;49;00m)))[37m[39;49;00m$
[37m^I  [39;49;00m[37m;; Reset the modified cons cell ELT to its original content.[39;49;00m[37m[39;49;00m$
[37m^I  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[32melt[39;49;00m)[37m[39;49;00m$
[37m^I    [39;49;00m([32msetcar[39;49;00m[37m [39;49;00m[32melt[39;49;00m[37m [39;49;00m[31mold-car[39;49;00m)[37m[39;49;00m$
[37m^I    [39;49;00m([32msetcdr[39;49;00m[37m [39;49;00m[32melt[39;49;00m[37m [39;49;00m[31mold-cdr[39;49;00m))[37m[39;49;00m$
[37m^I  [39;49;00m[37m;; Revert the undo info to what it was when we grabbed the state.[39;49;00m[37m[39;49;00m$
[37m^I  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbuffer-undo-list[39;49;00m[37m [39;49;00m[32melt[39;49;00m))))))[37m[39;49;00m$
[37m[39;49;00m[37m[39;49;00m$
[37m;;;; Display-related functions.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m;; For compatibility.[39;49;00m[37m[39;49;00m$
([36mdefine-obsolete-function-alias[39;49;00m[37m [39;49;00m[33m'redraw-modeline[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[33m'force-mode-line-update[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m24.3[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mmomentary-string-display[39;49;00m[37m [39;49;00m([32mstring[39;49;00m[37m [39;49;00m[31mpos[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mexit-char[39;49;00m[37m [39;49;00m[32mmessage[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mMomentarily display STRING in the buffer at POS.[39;49;00m$
[33mDisplay remains until next event is input.[39;49;00m$
[33mIf POS is a marker, only its position is used; its buffer is ignored.[39;49;00m$
[33mOptional third arg EXIT-CHAR can be a character, event or event[39;49;00m$
[33mdescription list.  EXIT-CHAR defaults to SPC.  If the input is[39;49;00m$
[33mEXIT-CHAR it is swallowed; otherwise it is then available as[39;49;00m$
[33minput (as a command if nothing else).[39;49;00m$
[33mDisplay MESSAGE (optional fourth arg) in the echo area.[39;49;00m$
[33mIf MESSAGE is nil, instructions to type EXIT-CHAR are displayed there.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mexit-char[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mexit-char[39;49;00m[37m [39;49;00m[33m?\s[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mol[39;49;00m[37m [39;49;00m([32mmake-overlay[39;49;00m[37m [39;49;00m[31mpos[39;49;00m[37m [39;49;00m[31mpos[39;49;00m))[37m[39;49;00m$
[37m        [39;49;00m([31mstr[39;49;00m[37m [39;49;00m([32mcopy-sequence[39;49;00m[37m [39;49;00m[32mstring[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m([34munwind-protect[39;49;00m[37m[39;49;00m$
[37m        [39;49;00m([34mprogn[39;49;00m[37m[39;49;00m$
[37m          [39;49;00m([34msave-excursion[39;49;00m[37m[39;49;00m$
[37m            [39;49;00m([32moverlay-put[39;49;00m[37m [39;49;00m[31mol[39;49;00m[37m [39;49;00m[33m'after-string[39;49;00m[37m [39;49;00m[31mstr[39;49;00m)[37m[39;49;00m$
[37m            [39;49;00m([32mgoto-char[39;49;00m[37m [39;49;00m[31mpos[39;49;00m)[37m[39;49;00m$
[37m            [39;49;00m[37m;; To avoid trouble with out-of-bounds position[39;49;00m[37m[39;49;00m$
[37m            [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mpos[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m))[37m[39;49;00m$
[37m            [39;49;00m[37m;; If the string end is off screen, recenter now.[39;49;00m[37m[39;49;00m$
[37m            [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32m<=[39;49;00m[37m [39;49;00m([32mwindow-end[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m [39;49;00m[31mpos[39;49;00m)[37m[39;49;00m$
[37m                [39;49;00m([32mrecenter[39;49;00m[37m [39;49;00m([32m/[39;49;00m[37m [39;49;00m([31mwindow-height[39;49;00m)[37m [39;49;00m[34m2[39;49;00m))))[37m[39;49;00m$
[37m          [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[32mmessage[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mType %s to continue editing.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m                   [39;49;00m([32msingle-key-description[39;49;00m[37m [39;49;00m[31mexit-char[39;49;00m))[37m[39;49;00m$
[37m^I  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mevent[39;49;00m[37m [39;49;00m([31mread-key[39;49;00m)))[37m[39;49;00m$
[37m^I    [39;49;00m[37m;; `exit-char' can be an event, or an event description list.[39;49;00m[37m[39;49;00m$
[37m^I    [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mevent[39;49;00m[37m [39;49;00m[31mexit-char[39;49;00m)[37m[39;49;00m$
[37m^I^I[39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mevent[39;49;00m[37m [39;49;00m([32mevent-convert-list[39;49;00m[37m [39;49;00m[31mexit-char[39;49;00m))[37m[39;49;00m$
[37m^I^I[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31munread-command-events[39;49;00m[37m[39;49;00m$
[37m                      [39;49;00m([32mappend[39;49;00m[37m [39;49;00m([32mthis-single-command-raw-keys[39;49;00m))))))[37m[39;49;00m$
[37m      [39;49;00m([32mdelete-overlay[39;49;00m[37m [39;49;00m[31mol[39;49;00m))))[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m[37m[39;49;00m$
[37m;;;; Overlay operations[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mcopy-overlay[39;49;00m[37m [39;49;00m([31mo[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn a copy of overlay O.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mo1[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32moverlay-buffer[39;49;00m[37m [39;49;00m[31mo[39;49;00m)[37m[39;49;00m$
[37m                [39;49;00m([32mmake-overlay[39;49;00m[37m [39;49;00m([32moverlay-start[39;49;00m[37m [39;49;00m[31mo[39;49;00m)[37m [39;49;00m([32moverlay-end[39;49;00m[37m [39;49;00m[31mo[39;49;00m)[37m[39;49;00m$
[37m                              [39;49;00m[37m;; FIXME: there's no easy way to find the[39;49;00m[37m[39;49;00m$
[37m                              [39;49;00m[37m;; insertion-type of the two markers.[39;49;00m[37m[39;49;00m$
[37m                              [39;49;00m([32moverlay-buffer[39;49;00m[37m [39;49;00m[31mo[39;49;00m))[37m[39;49;00m$
[37m              [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mo1[39;49;00m[37m [39;49;00m([32mmake-overlay[39;49;00m[37m [39;49;00m([32mpoint-min[39;49;00m)[37m [39;49;00m([32mpoint-min[39;49;00m))))[37m[39;49;00m$
[37m                [39;49;00m([32mdelete-overlay[39;49;00m[37m [39;49;00m[31mo1[39;49;00m)[37m[39;49;00m$
[37m                [39;49;00m[31mo1[39;49;00m)))[37m[39;49;00m$
[37m^I[39;49;00m([31mprops[39;49;00m[37m [39;49;00m([32moverlay-properties[39;49;00m[37m [39;49;00m[31mo[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m[31mprops[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([32moverlay-put[39;49;00m[37m [39;49;00m[31mo1[39;49;00m[37m [39;49;00m([36mpop[39;49;00m[37m [39;49;00m[31mprops[39;49;00m)[37m [39;49;00m([36mpop[39;49;00m[37m [39;49;00m[31mprops[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m[31mo1[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mremove-overlays[39;49;00m[37m [39;49;00m([34m&optional[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[31mname[39;49;00m[37m [39;49;00m[31mval[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mClear BEG and END of overlays whose property NAME has value VAL.[39;49;00m$
[33mOverlays might be moved and/or split.[39;49;00m$
[33mBEG and END default respectively to the beginning and end of buffer.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; This speeds up the loops over overlays.[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36munless[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m[37m [39;49;00m([32mpoint-min[39;49;00m)))[37m[39;49;00m$
[37m  [39;49;00m([36munless[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m([32mpoint-max[39;49;00m)))[37m[39;49;00m$
[37m  [39;49;00m([32moverlay-recenter[39;49;00m[37m [39;49;00m[31mend[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m[37m [39;49;00m([34mprog1[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m))))[37m[39;49;00m$
[37m  [39;49;00m([34msave-excursion[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m([36mdolist[39;49;00m[37m [39;49;00m([31mo[39;49;00m[37m [39;49;00m([32moverlays-in[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m[37m [39;49;00m[31mend[39;49;00m))[37m[39;49;00m$
[37m      [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32moverlay-get[39;49;00m[37m [39;49;00m[31mo[39;49;00m[37m [39;49;00m[31mname[39;49;00m)[37m [39;49;00m[31mval[39;49;00m)[37m[39;49;00m$
[37m^I[39;49;00m[37m;; Either push this overlay outside beg...end[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00m[37m;; or split it to exclude beg...end[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00m[37m;; or delete it entirely (if it is contained in beg...end).[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00m([34mif[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m([32moverlay-start[39;49;00m[37m [39;49;00m[31mo[39;49;00m)[37m [39;49;00m[31mbeg[39;49;00m)[37m[39;49;00m$
[37m^I    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m([32moverlay-end[39;49;00m[37m [39;49;00m[31mo[39;49;00m)[37m [39;49;00m[31mend[39;49;00m)[37m[39;49;00m$
[37m^I^I[39;49;00m([34mprogn[39;49;00m[37m[39;49;00m$
[37m^I^I  [39;49;00m([32mmove-overlay[39;49;00m[37m [39;49;00m([31mcopy-overlay[39;49;00m[37m [39;49;00m[31mo[39;49;00m)[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m([32moverlay-start[39;49;00m[37m [39;49;00m[31mo[39;49;00m)[37m [39;49;00m[31mbeg[39;49;00m)[37m[39;49;00m$
[37m^I^I  [39;49;00m([32mmove-overlay[39;49;00m[37m [39;49;00m[31mo[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m([32moverlay-end[39;49;00m[37m [39;49;00m[31mo[39;49;00m)))[37m[39;49;00m$
[37m^I      [39;49;00m([32mmove-overlay[39;49;00m[37m [39;49;00m[31mo[39;49;00m[37m [39;49;00m([32moverlay-start[39;49;00m[37m [39;49;00m[31mo[39;49;00m)[37m [39;49;00m[31mbeg[39;49;00m))[37m[39;49;00m$
[37m^I  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m([32moverlay-end[39;49;00m[37m [39;49;00m[31mo[39;49;00m)[37m [39;49;00m[31mend[39;49;00m)[37m[39;49;00m$
[37m^I      [39;49;00m([32mmove-overlay[39;49;00m[37m [39;49;00m[31mo[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m([32moverlay-end[39;49;00m[37m [39;49;00m[31mo[39;49;00m))[37m[39;49;00m$
[37m^I    [39;49;00m([32mdelete-overlay[39;49;00m[37m [39;49;00m[31mo[39;49;00m)))))))[37m[39;49;00m$
[37m[39;49;00m[37m[39;49;00m$
[37m;;;; Miscellanea.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
([34mdefvar[39;49;00m[37m [39;49;00m[31msuspend-hook[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mNormal hook run by [39;49;00m[33m`suspend-emacs'[39;49;00m[33m, before suspending.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
([34mdefvar[39;49;00m[37m [39;49;00m[31msuspend-resume-hook[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mNormal hook run by [39;49;00m[33m`suspend-emacs'[39;49;00m[33m, after Emacs is continued.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
([34mdefvar[39;49;00m[37m [39;49;00m[31mtemp-buffer-show-hook[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mNormal hook run by [39;49;00m[33m`with-output-to-temp-buffer'[39;49;00m[33m after displaying the buffer.[39;49;00m$
[33mWhen the hook runs, the temporary buffer is current, and the window it[39;49;00m$
[33mwas displayed in is selected.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
([34mdefvar[39;49;00m[37m [39;49;00m[31mtemp-buffer-setup-hook[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mNormal hook run by [39;49;00m[33m`with-output-to-temp-buffer'[39;49;00m[33m at the start.[39;49;00m$
[33mWhen the hook runs, the temporary buffer is current.[39;49;00m$
[33mThis hook is normally set up with a function to put the buffer in Help[39;49;00m$
[33mmode.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
([34mdefconst[39;49;00m[37m [39;49;00m[31muser-emacs-directory[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31msystem-type[39;49;00m[37m [39;49;00m[33m'ms-dos[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m[37m;; MS-DOS cannot have initial dot.[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m[33m"[39;49;00m[33m~/_emacs.d/[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[33m"[39;49;00m[33m~/.emacs.d/[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mDirectory beneath which additional per-user Emacs-specific files are placed.[39;49;00m$
[33mVarious programs in Emacs store information in this directory.[39;49;00m$
[33mNote that this should end with a directory separator.[39;49;00m$
[33mSee also [39;49;00m[33m`locate-user-emacs-file'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m[37m[39;49;00m$
[37m;;;; Misc. useful functions.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
([36mdefsubst[39;49;00m[37m [39;49;00m[31mbuffer-narrowed-p[39;49;00m[37m [39;49;00m()[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn non-nil if the current buffer is narrowed.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([32m/=[39;49;00m[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m([32mpoint-max[39;49;00m)[37m [39;49;00m([32mpoint-min[39;49;00m))[37m [39;49;00m([32mbuffer-size[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mfind-tag-default-bounds[39;49;00m[37m [39;49;00m()[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mDetermine the boundaries of the default tag, based on text at point.[39;49;00m$
[33mReturn a cons cell with the beginning and end of the found tag.[39;49;00m$
[33mIf there is no plausible default, return nil.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m([31mfrom[39;49;00m[37m [39;49;00m[31mto[39;49;00m[37m [39;49;00m[31mbound[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([34mprogn[39;49;00m[37m[39;49;00m$
[37m^I^I[39;49;00m[37m;; Look at text around `point'.[39;49;00m[37m[39;49;00m$
[37m^I^I[39;49;00m([34msave-excursion[39;49;00m[37m[39;49;00m$
[37m^I^I  [39;49;00m([32mskip-syntax-backward[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mw_[39;49;00m[33m"[39;49;00m)[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mfrom[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m)))[37m[39;49;00m$
[37m^I^I[39;49;00m([34msave-excursion[39;49;00m[37m[39;49;00m$
[37m^I^I  [39;49;00m([32mskip-syntax-forward[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mw_[39;49;00m[33m"[39;49;00m)[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mto[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m)))[37m[39;49;00m$
[37m^I^I[39;49;00m([32m>[39;49;00m[37m [39;49;00m[31mto[39;49;00m[37m [39;49;00m[31mfrom[39;49;00m))[37m[39;49;00m$
[37m^I      [39;49;00m[37m;; Look between `line-beginning-position' and `point'.[39;49;00m[37m[39;49;00m$
[37m^I      [39;49;00m([34msave-excursion[39;49;00m[37m[39;49;00m$
[37m^I^I[39;49;00m([34mand[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbound[39;49;00m[37m [39;49;00m([32mline-beginning-position[39;49;00m))[37m[39;49;00m$
[37m^I^I     [39;49;00m([32mskip-syntax-backward[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m^w_[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mbound[39;49;00m)[37m[39;49;00m$
[37m^I^I     [39;49;00m([32m>[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mto[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m))[37m [39;49;00m[31mbound[39;49;00m)[37m[39;49;00m$
[37m^I^I     [39;49;00m([32mskip-syntax-backward[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mw_[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m^I^I     [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mfrom[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m))))[37m[39;49;00m$
[37m^I      [39;49;00m[37m;; Look between `point' and `line-end-position'.[39;49;00m[37m[39;49;00m$
[37m^I      [39;49;00m([34msave-excursion[39;49;00m[37m[39;49;00m$
[37m^I^I[39;49;00m([34mand[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbound[39;49;00m[37m [39;49;00m([32mline-end-position[39;49;00m))[37m[39;49;00m$
[37m^I^I     [39;49;00m([32mskip-syntax-forward[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m^w_[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mbound[39;49;00m)[37m[39;49;00m$
[37m^I^I     [39;49;00m([32m<[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mfrom[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m))[37m [39;49;00m[31mbound[39;49;00m)[37m[39;49;00m$
[37m^I^I     [39;49;00m([32mskip-syntax-forward[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mw_[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m^I^I     [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mto[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m)))))[37m[39;49;00m$
[37m      [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mfrom[39;49;00m[37m [39;49;00m[31mto[39;49;00m))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mfind-tag-default[39;49;00m[37m [39;49;00m()[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mDetermine default tag to search for, based on text at point.[39;49;00m$
[33mIf there is no plausible default, return nil.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mbounds[39;49;00m[37m [39;49;00m([31mfind-tag-default-bounds[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31mbounds[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([32mbuffer-substring-no-properties[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mbounds[39;49;00m)[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mbounds[39;49;00m)))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mfind-tag-default-as-regexp[39;49;00m[37m [39;49;00m()[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn regexp that matches the default tag at point.[39;49;00m$
[33mIf there is no tag at point, return nil.[39;49;00m$
[33m[39;49;00m$
[33mWhen in a major mode that does not provide its own[39;49;00m$
[33m`find-tag-default-function'[39;49;00m[33m, return a regexp that matches the[39;49;00m$
[33msymbol at point exactly.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtag[39;49;00m[37m [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mfind-tag-default-function[39;49;00m[37m[39;49;00m$
[37m^I^I^I  [39;49;00m([32mget[39;49;00m[37m [39;49;00m[31mmajor-mode[39;49;00m[37m [39;49;00m[33m'find-tag-default-function[39;49;00m)[37m[39;49;00m$
[37m^I^I^I  [39;49;00m[33m'find-tag-default[39;49;00m))))[37m[39;49;00m$
[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mtag[39;49;00m[37m [39;49;00m([32mregexp-quote[39;49;00m[37m [39;49;00m[31mtag[39;49;00m))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mfind-tag-default-as-symbol-regexp[39;49;00m[37m [39;49;00m()[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn regexp that matches the default tag at point as symbol.[39;49;00m$
[33mIf there is no tag at point, return nil.[39;49;00m$
[33m[39;49;00m$
[33mWhen in a major mode that does not provide its own[39;49;00m$
[33m`find-tag-default-function'[39;49;00m[33m, return a regexp that matches the[39;49;00m$
[33msymbol at point exactly.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtag-regexp[39;49;00m[37m [39;49;00m([31mfind-tag-default-as-regexp[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mtag-regexp[39;49;00m[37m[39;49;00m$
[37m^I     [39;49;00m([32meq[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mfind-tag-default-function[39;49;00m[37m[39;49;00m$
[37m^I^I     [39;49;00m([32mget[39;49;00m[37m [39;49;00m[31mmajor-mode[39;49;00m[37m [39;49;00m[33m'find-tag-default-function[39;49;00m)[37m[39;49;00m$
[37m^I^I     [39;49;00m[33m'find-tag-default[39;49;00m)[37m[39;49;00m$
[37m^I^I [39;49;00m[33m'find-tag-default[39;49;00m))[37m[39;49;00m$
[37m^I[39;49;00m([32mformat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m_<%s[39;49;00m[33m\\[39;49;00m[33m_>[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mtag-regexp[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m[31mtag-regexp[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mplay-sound[39;49;00m[37m [39;49;00m([31msound[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mSOUND is a list of the form [39;49;00m[33m`[39;49;00m[33m(sound KEYWORD VALUE...)'.[39;49;00m$
[33mThe following keywords are recognized:[39;49;00m$
[33m[39;49;00m$
[33m  :file FILE - read sound data from FILE.  If FILE isn't an[39;49;00m$
[33mabsolute file name, it is searched in [39;49;00m[33m`data-directory'[39;49;00m[33m.[39;49;00m$
[33m[39;49;00m$
[33m  :data DATA - read sound data from string DATA.[39;49;00m$
[33m[39;49;00m$
[33mExactly one of :file or :data must be present.[39;49;00m$
[33m[39;49;00m$
[33m  :volume VOL - set volume to VOL.  VOL must an integer in the[39;49;00m$
[33mrange 0..100 or a float in the range 0..1.0.  If not specified,[39;49;00m$
[33mdon't change the volume setting of the sound device.[39;49;00m$
[33m[39;49;00m$
[33m  :device DEVICE - play sound on DEVICE.  If not specified,[39;49;00m$
[33ma system-dependent default device name is used.[39;49;00m$
[33m[39;49;00m$
[33mNote: :data and :device are currently not supported on Windows.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mfboundp[39;49;00m[37m [39;49;00m[33m'play-sound-internal[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m([32mplay-sound-internal[39;49;00m[37m [39;49;00m[31msound[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([36merror[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mThis Emacs binary lacks sound support[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
([36mdeclare-function[39;49;00m[37m [39;49;00m[31mw32-shell-dos-semantics[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mw32-fns[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mshell-quote-argument[39;49;00m[37m [39;49;00m([31margument[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mQuote ARGUMENT for passing as argument to an inferior shell.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mcond[39;49;00m[37m[39;49;00m$
[37m   [39;49;00m(([32meq[39;49;00m[37m [39;49;00m[31msystem-type[39;49;00m[37m [39;49;00m[33m'ms-dos[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m[37m;; Quote using double quotes, but escape any existing quotes in[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[37m;; the argument with backslashes.[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mresult[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m          [39;49;00m([31mstart[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m          [39;49;00m[31mend[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m[^[39;49;00m[33m\"[39;49;00m[33m][39;49;00m[33m"[39;49;00m[37m [39;49;00m[31margument[39;49;00m))[37m[39;49;00m$
[37m              [39;49;00m([32m<[39;49;00m[37m [39;49;00m([32mmatch-end[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31margument[39;49;00m)))[37m[39;49;00m$
[37m          [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m[[39;49;00m[33m\"[39;49;00m[33m][39;49;00m[33m"[39;49;00m[37m [39;49;00m[31margument[39;49;00m[37m [39;49;00m[31mstart[39;49;00m)[37m[39;49;00m$
[37m            [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m([32mmatch-beginning[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m                  [39;49;00m[31mresult[39;49;00m[37m [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[31mresult[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[31margument[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mend[39;49;00m)[37m[39;49;00m$
[37m                                 [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m"[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[31margument[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m([32m1+[39;49;00m[37m [39;49;00m[31mend[39;49;00m)))[37m[39;49;00m$
[37m                  [39;49;00m[31mstart[39;49;00m[37m [39;49;00m([32m1+[39;49;00m[37m [39;49;00m[31mend[39;49;00m))))[37m[39;49;00m$
[37m      [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mresult[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[31margument[39;49;00m[37m [39;49;00m[31mstart[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
[37m   [39;49;00m(([34mand[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31msystem-type[39;49;00m[37m [39;49;00m[33m'windows-nt[39;49;00m)[37m [39;49;00m([31mw32-shell-dos-semantics[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[37m;; First, quote argument so that CommandLineToArgvW will[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[37m;; understand it.  See[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[37m;; http://msdn.microsoft.com/en-us/library/17w5ykft%28v=vs.85%29.aspx[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[37m;; After we perform that level of quoting, escape shell[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[37m;; metacharacters so that cmd won't mangle our argument.  If the[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[37m;; argument contains no double quote characters, we can just[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[37m;; surround it with double quotes.  Otherwise, we need to prefix[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[37m;; each shell metacharacter with a caret.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31margument[39;49;00m[37m[39;49;00m$
[37m          [39;49;00m[37m;; escape backslashes at end of string[39;49;00m[37m[39;49;00m$
[37m          [39;49;00m([31mreplace-regexp-in-string[39;49;00m[37m[39;49;00m$
[37m           [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m([39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m*[39;49;00m[33m\\[39;49;00m[33m)$[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m           [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m1[39;49;00m[33m\\[39;49;00m[33m1[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m           [39;49;00m[37m;; escape backslashes and quotes in string body[39;49;00m[37m[39;49;00m$
[37m           [39;49;00m([31mreplace-regexp-in-string[39;49;00m[37m[39;49;00m$
[37m            [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m([39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m*[39;49;00m[33m\\[39;49;00m[33m)[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m            [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m1[39;49;00m[33m\\[39;49;00m[33m1[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m            [39;49;00m[31margument[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m[%![39;49;00m[33m\"[39;49;00m[33m][39;49;00m[33m"[39;49;00m[37m [39;49;00m[31margument[39;49;00m)[37m[39;49;00m$
[37m        [39;49;00m([32mconcat[39;49;00m[37m[39;49;00m$
[37m         [39;49;00m[33m"[39;49;00m[33m^[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m         [39;49;00m([31mreplace-regexp-in-string[39;49;00m[37m[39;49;00m$
[37m          [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m([%!()[39;49;00m[33m\"[39;49;00m[33m<>&|^][39;49;00m[33m\\[39;49;00m[33m)[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m          [39;49;00m[33m"[39;49;00m[33m^[39;49;00m[33m\\[39;49;00m[33m1[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m          [39;49;00m[31margument[39;49;00m)[37m[39;49;00m$
[37m         [39;49;00m[33m"[39;49;00m[33m^[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31margument[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
[37m   [39;49;00m([31mt[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mequal[39;49;00m[37m [39;49;00m[31margument[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m        [39;49;00m[33m"[39;49;00m[33m''[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m[37m;; Quote everything except POSIX filename characters.[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m[37m;; This should be safe enough even for really weird shells.[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([31mreplace-regexp-in-string[39;49;00m[37m[39;49;00m$
[37m       [39;49;00m[33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m'[39;49;00m[33m\n[39;49;00m[33m'[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m       [39;49;00m([31mreplace-regexp-in-string[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m[^-0-9a-zA-Z_./[39;49;00m[33m\n[39;49;00m[33m][39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m&[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31margument[39;49;00m))))[37m[39;49;00m$
[37m   [39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mstring-or-null-p[39;49;00m[37m [39;49;00m([31mobject[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn t if OBJECT is a string or nil.[39;49;00m$
[33mOtherwise, return nil.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m[31mobject[39;49;00m)[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[31mobject[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mbooleanp[39;49;00m[37m [39;49;00m([31mobject[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn t if OBJECT is one of the two canonical boolean values: t or nil.[39;49;00m$
[33mOtherwise, return nil.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[31mobject[39;49;00m[37m [39;49;00m'([31mnil[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mspecial-form-p[39;49;00m[37m [39;49;00m([31mobject[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mNon-nil if and only if OBJECT is a special form.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32msymbolp[39;49;00m[37m [39;49;00m[31mobject[39;49;00m)[37m [39;49;00m([32mfboundp[39;49;00m[37m [39;49;00m[31mobject[39;49;00m))[37m[39;49;00m$
[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mobject[39;49;00m[37m [39;49;00m([32mindirect-function[39;49;00m[37m [39;49;00m[31mobject[39;49;00m[37m [39;49;00m[31mt[39;49;00m)))[37m[39;49;00m$
[37m  [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32msubrp[39;49;00m[37m [39;49;00m[31mobject[39;49;00m)[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m([34msubr-arity[39;49;00m[37m [39;49;00m[31mobject[39;49;00m))[37m [39;49;00m[33m'unevalled[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mmacrop[39;49;00m[37m [39;49;00m([31mobject[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mNon-nil if and only if OBJECT is a macro.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mdef[39;49;00m[37m [39;49;00m([32mindirect-function[39;49;00m[37m [39;49;00m[31mobject[39;49;00m[37m [39;49;00m[31mt[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mdef[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[33m'macro[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mdef[39;49;00m))[37m[39;49;00m$
[37m          [39;49;00m([34mand[39;49;00m[37m [39;49;00m([31mautoloadp[39;49;00m[37m [39;49;00m[31mdef[39;49;00m)[37m [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m4[39;49;00m[37m [39;49;00m[31mdef[39;49;00m)[37m [39;49;00m'([31mmacro[39;49;00m[37m [39;49;00m[31mt[39;49;00m)))))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mfield-at-pos[39;49;00m[37m [39;49;00m([31mpos[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn the field at position POS, taking stickiness etc into account.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mraw-field[39;49;00m[37m [39;49;00m([32mget-char-property[39;49;00m[37m [39;49;00m([32mfield-beginning[39;49;00m[37m [39;49;00m[31mpos[39;49;00m)[37m [39;49;00m[33m'field[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mraw-field[39;49;00m[37m [39;49;00m[33m'boundary[39;49;00m)[37m[39;49;00m$
[37m^I[39;49;00m([32mget-char-property[39;49;00m[37m [39;49;00m([32m1-[39;49;00m[37m [39;49;00m([32mfield-end[39;49;00m[37m [39;49;00m[31mpos[39;49;00m))[37m [39;49;00m[33m'field[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m[31mraw-field[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31msha1[39;49;00m[37m [39;49;00m([31mobject[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[31mbinary[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn the SHA1 (Secure Hash Algorithm) of an OBJECT.[39;49;00m$
[33mOBJECT is either a string or a buffer.  Optional arguments START and[39;49;00m$
[33mEND are character positions specifying which portion of OBJECT for[39;49;00m$
[33mcomputing the hash.  If BINARY is non-nil, return a string in binary[39;49;00m$
[33mform.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([32msecure-hash[39;49;00m[37m [39;49;00m[33m'sha1[39;49;00m[37m [39;49;00m[31mobject[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[31mbinary[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mfunction-get[39;49;00m[37m [39;49;00m([31mf[39;49;00m[37m [39;49;00m[31mprop[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[32mautoload[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn the value of property PROP of function F.[39;49;00m$
[33mIf AUTOLOAD is non-nil and F is autoloaded, try to autoload it[39;49;00m$
[33min the hope that it will set PROP.  If AUTOLOAD is [39;49;00m[33m`macro'[39;49;00m[33m, only do it[39;49;00m$
[33mif it's an autoloaded macro.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mval[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m$
[37m    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32msymbolp[39;49;00m[37m [39;49;00m[31mf[39;49;00m)[37m[39;49;00m$
[37m                [39;49;00m([32mnull[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mval[39;49;00m[37m [39;49;00m([32mget[39;49;00m[37m [39;49;00m[31mf[39;49;00m[37m [39;49;00m[31mprop[39;49;00m)))[37m[39;49;00m$
[37m                [39;49;00m([32mfboundp[39;49;00m[37m [39;49;00m[31mf[39;49;00m))[37m[39;49;00m$
[37m      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mfundef[39;49;00m[37m [39;49;00m([32msymbol-function[39;49;00m[37m [39;49;00m[31mf[39;49;00m)))[37m[39;49;00m$
[37m        [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[32mautoload[39;49;00m[37m [39;49;00m([31mautoloadp[39;49;00m[37m [39;49;00m[31mfundef[39;49;00m)[37m[39;49;00m$
[37m                 [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mequal[39;49;00m[37m [39;49;00m[31mfundef[39;49;00m[37m[39;49;00m$
[37m                             [39;49;00m([32mautoload-do-load[39;49;00m[37m [39;49;00m[31mfundef[39;49;00m[37m [39;49;00m[31mf[39;49;00m[37m[39;49;00m$
[37m                                               [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[32mautoload[39;49;00m[37m [39;49;00m[33m'macro[39;49;00m)[37m[39;49;00m$
[37m                                                   [39;49;00m[33m'macro[39;49;00m)))))[37m[39;49;00m$
[37m            [39;49;00m[31mnil[39;49;00m[37m                         [39;49;00m[37m;Re-try `get' on the same `f'.[39;49;00m[37m[39;49;00m$
[37m          [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mf[39;49;00m[37m [39;49;00m[31mfundef[39;49;00m))))[37m[39;49;00m$
[37m    [39;49;00m[31mval[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m[37m[39;49;00m$
[37m;;;; Support for yanking and text properties.[39;49;00m[37m[39;49;00m$
[37m;; Why here in subr.el rather than in simple.el?  --Stef[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
([34mdefvar[39;49;00m[37m [39;49;00m[31myank-handled-properties[39;49;00m)[37m[39;49;00m$
([34mdefvar[39;49;00m[37m [39;49;00m[31myank-excluded-properties[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mremove-yank-excluded-properties[39;49;00m[37m [39;49;00m([31mstart[39;49;00m[37m [39;49;00m[31mend[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mProcess text properties between START and END, inserted for a [39;49;00m[33m`yank'[39;49;00m[33m.[39;49;00m$
[33mPerform the handling specified by [39;49;00m[33m`yank-handled-properties'[39;49;00m[33m, then[39;49;00m$
[33mremove properties specified by [39;49;00m[33m`yank-excluded-properties'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31minhibit-read-only[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
[37m    [39;49;00m([36mdolist[39;49;00m[37m [39;49;00m([31mhandler[39;49;00m[37m [39;49;00m[31myank-handled-properties[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mprop[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mhandler[39;49;00m))[37m[39;49;00m$
[37m^I    [39;49;00m([31mfun[39;49;00m[37m  [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mhandler[39;49;00m))[37m[39;49;00m$
[37m^I    [39;49;00m([31mrun-start[39;49;00m[37m [39;49;00m[31mstart[39;49;00m))[37m[39;49;00m$
[37m^I[39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m[31mrun-start[39;49;00m[37m [39;49;00m[31mend[39;49;00m)[37m[39;49;00m$
[37m^I  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mvalue[39;49;00m[37m [39;49;00m([32mget-text-property[39;49;00m[37m [39;49;00m[31mrun-start[39;49;00m[37m [39;49;00m[31mprop[39;49;00m))[37m[39;49;00m$
[37m^I^I[39;49;00m([31mrun-end[39;49;00m[37m [39;49;00m([32mnext-single-property-change[39;49;00m[37m[39;49;00m$
[37m^I^I^I  [39;49;00m[31mrun-start[39;49;00m[37m [39;49;00m[31mprop[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mend[39;49;00m)))[37m[39;49;00m$
[37m^I    [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mfun[39;49;00m[37m [39;49;00m[31mvalue[39;49;00m[37m [39;49;00m[31mrun-start[39;49;00m[37m [39;49;00m[31mrun-end[39;49;00m)[37m[39;49;00m$
[37m^I    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mrun-start[39;49;00m[37m [39;49;00m[31mrun-end[39;49;00m)))))[37m[39;49;00m$
[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31myank-excluded-properties[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
[37m^I[39;49;00m([32mset-text-properties[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m([32mremove-list-of-text-properties[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[31myank-excluded-properties[39;49;00m))))[37m[39;49;00m$
[37m[39;49;00m$
([34mdefvar[39;49;00m[37m [39;49;00m[31myank-undo-function[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31minsert-for-yank[39;49;00m[37m [39;49;00m([32mstring[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mCall [39;49;00m[33m`insert-for-yank-1'[39;49;00m[33m repetitively for each [39;49;00m[33m`yank-handler'[39;49;00m[33m segment.[39;49;00m$
[33m[39;49;00m$
[33mSee [39;49;00m[33m`insert-for-yank-1'[39;49;00m[33m for more details.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m([31mto[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mto[39;49;00m[37m [39;49;00m([32mnext-single-property-change[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[33m'yank-handler[39;49;00m[37m [39;49;00m[32mstring[39;49;00m))[37m[39;49;00m$
[37m      [39;49;00m([31minsert-for-yank-1[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[31mto[39;49;00m))[37m[39;49;00m$
[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[31mto[39;49;00m))))[37m[39;49;00m$
[37m  [39;49;00m([31minsert-for-yank-1[39;49;00m[37m [39;49;00m[32mstring[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31minsert-for-yank-1[39;49;00m[37m [39;49;00m([32mstring[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mInsert STRING at point for the [39;49;00m[33m`yank'[39;49;00m[33m command.[39;49;00m$
[33mThis function is like [39;49;00m[33m`insert'[39;49;00m[33m, except it honors the variables[39;49;00m$
[33m`yank-handled-properties'[39;49;00m[33m and [39;49;00m[33m`yank-excluded-properties'[39;49;00m[33m, and the[39;49;00m$
[33m`yank-handler'[39;49;00m[33m text property.[39;49;00m$
[33m[39;49;00m$
[33mProperties listed in [39;49;00m[33m`yank-handled-properties'[39;49;00m[33m are processed,[39;49;00m$
[33mthen those listed in [39;49;00m[33m`yank-excluded-properties'[39;49;00m[33m are discarded.[39;49;00m$
[33m[39;49;00m$
[33mIf STRING has a non-nil [39;49;00m[33m`yank-handler'[39;49;00m[33m property on its first[39;49;00m$
[33mcharacter, the normal insert behavior is altered.  The value of[39;49;00m$
[33mthe [39;49;00m[33m`yank-handler'[39;49;00m[33m property must be a list of one to four[39;49;00m$
[33melements, of the form (FUNCTION PARAM NOEXCLUDE UNDO).[39;49;00m$
[33mFUNCTION, if non-nil, should be a function of one argument, an[39;49;00m$
[33m object to insert; it is called instead of [39;49;00m[33m`insert'[39;49;00m[33m.[39;49;00m$
[33mPARAM, if present and non-nil, replaces STRING as the argument to[39;49;00m$
[33m FUNCTION or [39;49;00m[33m`insert'[39;49;00m[33m; e.g. if FUNCTION is [39;49;00m[33m`yank-rectangle'[39;49;00m[33m, PARAM[39;49;00m$
[33m may be a list of strings to insert as a rectangle.[39;49;00m$
[33mIf NOEXCLUDE is present and non-nil, the normal removal of[39;49;00m$
[33m [39;49;00m[33m`yank-excluded-properties'[39;49;00m[33m is not performed; instead FUNCTION is[39;49;00m$
[33m responsible for the removal.  This may be necessary if FUNCTION[39;49;00m$
[33m adjusts point before or after inserting the object.[39;49;00m$
[33mUNDO, if present and non-nil, should be a function to be called[39;49;00m$
[33m by [39;49;00m[33m`yank-pop'[39;49;00m[33m to undo the insertion of the current object.  It is[39;49;00m$
[33m given two arguments, the start and end of the region.  FUNCTION[39;49;00m$
[33m may set [39;49;00m[33m`yank-undo-function'[39;49;00m[33m to override UNDO.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mhandler[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m[32mstring[39;49;00m)[37m[39;49;00m$
[37m^I^I       [39;49;00m([32mget-text-property[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[33m'yank-handler[39;49;00m[37m [39;49;00m[32mstring[39;49;00m)))[37m[39;49;00m$
[37m^I [39;49;00m([31mparam[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mhandler[39;49;00m)[37m [39;49;00m[32mstring[39;49;00m))[37m[39;49;00m$
[37m^I [39;49;00m([31mopoint[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m))[37m[39;49;00m$
[37m^I [39;49;00m([31minhibit-read-only[39;49;00m[37m [39;49;00m[31minhibit-read-only[39;49;00m)[37m[39;49;00m$
[37m^I [39;49;00m[31mend[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31myank-undo-function[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[31mhandler[39;49;00m)[37m [39;49;00m[37m; FUNCTION[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mhandler[39;49;00m)[37m [39;49;00m[31mparam[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m([32minsert[39;49;00m[37m [39;49;00m[31mparam[39;49;00m))[37m[39;49;00m$
[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[37m;; Prevent read-only properties from interfering with the[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[37m;; following text property changes.[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31minhibit-read-only[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m[31mhandler[39;49;00m)[37m [39;49;00m[37m; NOEXCLUDE[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([31mremove-yank-excluded-properties[39;49;00m[37m [39;49;00m[31mopoint[39;49;00m[37m [39;49;00m[31mend[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[37m;; If last inserted char has properties, mark them as rear-nonsticky.[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[31mopoint[39;49;00m)[37m[39;49;00m$
[37m^I     [39;49;00m([32mtext-properties-at[39;49;00m[37m [39;49;00m([32m1-[39;49;00m[37m [39;49;00m[31mend[39;49;00m)))[37m[39;49;00m$
[37m^I[39;49;00m([32mput-text-property[39;49;00m[37m [39;49;00m([32m1-[39;49;00m[37m [39;49;00m[31mend[39;49;00m)[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[33m'rear-nonsticky[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31myank-undo-function[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m^I^I   [39;49;00m[37m; not set by FUNCTION[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31myank-undo-function[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m3[39;49;00m[37m [39;49;00m[31mhandler[39;49;00m)))[37m [39;49;00m[37m; UNDO[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m4[39;49;00m[37m [39;49;00m[31mhandler[39;49;00m)[37m^I^I^I^I   [39;49;00m[37m; COMMAND[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mthis-command[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m4[39;49;00m[37m [39;49;00m[31mhandler[39;49;00m)))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31minsert-buffer-substring-no-properties[39;49;00m[37m [39;49;00m([31mbuffer[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mend[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mInsert before point a substring of BUFFER, without text properties.[39;49;00m$
[33mBUFFER may be a buffer or a buffer name.[39;49;00m$
[33mArguments START and END are character positions specifying the substring.[39;49;00m$
[33mThey default to the values of (point-min) and (point-max) in BUFFER.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mopoint[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m([32minsert-buffer-substring[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mend[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31minhibit-read-only[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
[37m      [39;49;00m([32mset-text-properties[39;49;00m[37m [39;49;00m[31mopoint[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m)[37m [39;49;00m[31mnil[39;49;00m))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31minsert-buffer-substring-as-yank[39;49;00m[37m [39;49;00m([31mbuffer[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mend[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mInsert before point a part of BUFFER, stripping some text properties.[39;49;00m$
[33mBUFFER may be a buffer or a buffer name.[39;49;00m$
[33mArguments START and END are character positions specifying the substring.[39;49;00m$
[33mThey default to the values of (point-min) and (point-max) in BUFFER.[39;49;00m$
[33mBefore insertion, process text properties according to[39;49;00m$
[33m`yank-handled-properties'[39;49;00m[33m and [39;49;00m[33m`yank-excluded-properties'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; Since the buffer text should not normally have yank-handler properties,[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; there is no need to handle them here.[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mopoint[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m([32minsert-buffer-substring[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mend[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([31mremove-yank-excluded-properties[39;49;00m[37m [39;49;00m[31mopoint[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31myank-handle-font-lock-face-property[39;49;00m[37m [39;49;00m([31mface[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mend[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mIf [39;49;00m[33m`font-lock-defaults'[39;49;00m[33m is nil, apply FACE as a [39;49;00m[33m`face'[39;49;00m[33m property.[39;49;00m$
[33mSTART and END denote the start and end of the text to act on.[39;49;00m$
[33mDo nothing if FACE is nil.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mface[39;49;00m[37m[39;49;00m$
[37m       [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[31mfont-lock-defaults[39;49;00m)[37m[39;49;00m$
[37m       [39;49;00m([32mput-text-property[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[33m'face[39;49;00m[37m [39;49;00m[31mface[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
[37m;; This removes `mouse-face' properties in *Help* buffer buttons:[39;49;00m[37m[39;49;00m$
[37m;; http://lists.gnu.org/archive/html/emacs-devel/2002-04/msg00648.html[39;49;00m[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31myank-handle-category-property[39;49;00m[37m [39;49;00m([31mcategory[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mend[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mApply property category CATEGORY's properties between START and END.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31mcategory[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mstart2[39;49;00m[37m [39;49;00m[31mstart[39;49;00m))[37m[39;49;00m$
[37m      [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m[31mstart2[39;49;00m[37m [39;49;00m[31mend[39;49;00m)[37m[39;49;00m$
[37m^I[39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mend2[39;49;00m[37m     [39;49;00m([32mnext-property-change[39;49;00m[37m [39;49;00m[31mstart2[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mend[39;49;00m))[37m[39;49;00m$
[37m^I      [39;49;00m([31moriginal[39;49;00m[37m [39;49;00m([32mtext-properties-at[39;49;00m[37m [39;49;00m[31mstart2[39;49;00m)))[37m[39;49;00m$
[37m^I  [39;49;00m([32mset-text-properties[39;49;00m[37m [39;49;00m[31mstart2[39;49;00m[37m [39;49;00m[31mend2[39;49;00m[37m [39;49;00m([32msymbol-plist[39;49;00m[37m [39;49;00m[31mcategory[39;49;00m))[37m[39;49;00m$
[37m^I  [39;49;00m([32madd-text-properties[39;49;00m[37m [39;49;00m[31mstart2[39;49;00m[37m [39;49;00m[31mend2[39;49;00m[37m [39;49;00m[31moriginal[39;49;00m)[37m[39;49;00m$
[37m^I  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mstart2[39;49;00m[37m [39;49;00m[31mend2[39;49;00m))))))[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m[37m[39;49;00m$
[37m;;;; Synchronous shell commands.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mstart-process-shell-command[39;49;00m[37m [39;49;00m([31mname[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31margs[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mStart a program in a subprocess.  Return the process object for it.[39;49;00m$
[33mNAME is name for process.  It is modified if necessary to make it unique.[39;49;00m$
[33mBUFFER is the buffer (or buffer name) to associate with the process.[39;49;00m$
[33m Process output goes at end of that buffer, unless you specify[39;49;00m$
[33m an output stream or filter function to handle the output.[39;49;00m$
[33m BUFFER may be also nil, meaning that this process is not associated[39;49;00m$
[33m with any buffer[39;49;00m$
[33mCOMMAND is the shell command to run.[39;49;00m$
[33m[39;49;00m$
[33mAn old calling convention accepted any number of arguments after COMMAND,[39;49;00m$
[33mwhich were just concatenated to COMMAND.  This is still supported but strongly[39;49;00m$
[33mdiscouraged.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31madvertised-calling-convention[39;49;00m[37m [39;49;00m([31mname[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m [39;49;00m[31mcommand[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m23.1[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m[37m;; We used to use `exec' to replace the shell with the command,[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; but that failed to handle (...) and semicolon, etc.[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([32mstart-process[39;49;00m[37m [39;49;00m[31mname[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m [39;49;00m[31mshell-file-name[39;49;00m[37m [39;49;00m[31mshell-command-switch[39;49;00m[37m[39;49;00m$
[37m^I^I [39;49;00m([32mmapconcat[39;49;00m[37m [39;49;00m[33m'identity[39;49;00m[37m [39;49;00m[31margs[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mstart-file-process-shell-command[39;49;00m[37m [39;49;00m([31mname[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31margs[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mStart a program in a subprocess.  Return the process object for it.[39;49;00m$
[33mSimilar to [39;49;00m[33m`start-process-shell-command'[39;49;00m[33m, but calls [39;49;00m[33m`start-file-process'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31madvertised-calling-convention[39;49;00m[37m [39;49;00m([31mname[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m [39;49;00m[31mcommand[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m23.1[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m([31mstart-file-process[39;49;00m[37m[39;49;00m$
[37m   [39;49;00m[31mname[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m[39;49;00m$
[37m   [39;49;00m([34mif[39;49;00m[37m [39;49;00m([31mfile-remote-p[39;49;00m[37m [39;49;00m[31mdefault-directory[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m/bin/sh[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mshell-file-name[39;49;00m)[37m[39;49;00m$
[37m   [39;49;00m([34mif[39;49;00m[37m [39;49;00m([31mfile-remote-p[39;49;00m[37m [39;49;00m[31mdefault-directory[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m-c[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mshell-command-switch[39;49;00m)[37m[39;49;00m$
[37m   [39;49;00m([32mmapconcat[39;49;00m[37m [39;49;00m[33m'identity[39;49;00m[37m [39;49;00m[31margs[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mcall-process-shell-command[39;49;00m[37m [39;49;00m([31mcommand[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31minfile[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m [39;49;00m[31mdisplay[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I^I   [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31margs[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mExecute the shell command COMMAND synchronously in separate process.[39;49;00m$
[33mThe remaining arguments are optional.[39;49;00m$
[33mThe program's input comes from file INFILE (nil means [39;49;00m[33m`/dev/null'[39;49;00m[33m).[39;49;00m$
[33mInsert output in BUFFER before point; t means current buffer;[39;49;00m$
[33m nil for BUFFER means discard it; 0 means discard and don't wait.[39;49;00m$
[33mBUFFER can also have the form (REAL-BUFFER STDERR-FILE); in that case,[39;49;00m$
[33mREAL-BUFFER says what to do with standard output, as above,[39;49;00m$
[33mwhile STDERR-FILE says what to do with standard error in the child.[39;49;00m$
[33mSTDERR-FILE may be nil (discard standard error output),[39;49;00m$
[33mt (mix it with ordinary output), or a file name string.[39;49;00m$
[33m[39;49;00m$
[33mFourth arg DISPLAY non-nil means redisplay buffer as output is inserted.[39;49;00m$
[33mWildcards and redirection are handled as usual in the shell.[39;49;00m$
[33m[39;49;00m$
[33mIf BUFFER is 0, [39;49;00m[33m`call-process-shell-command'[39;49;00m[33m returns immediately with value nil.[39;49;00m$
[33mOtherwise it waits for COMMAND to terminate and returns a numeric exit[39;49;00m$
[33mstatus or a signal description string.[39;49;00m$
[33mIf you quit, the process is killed with SIGINT, or SIGKILL if you quit again.[39;49;00m$
[33m[39;49;00m$
[33mAn old calling convention accepted any number of arguments after DISPLAY,[39;49;00m$
[33mwhich were just concatenated to COMMAND.  This is still supported but strongly[39;49;00m$
[33mdiscouraged.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31madvertised-calling-convention[39;49;00m[37m[39;49;00m$
[37m            [39;49;00m([31mcommand[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31minfile[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m [39;49;00m[31mdisplay[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m24.5[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m[37m;; We used to use `exec' to replace the shell with the command,[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; but that failed to handle (...) and semicolon, etc.[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([32mcall-process[39;49;00m[37m [39;49;00m[31mshell-file-name[39;49;00m[37m[39;49;00m$
[37m^I^I[39;49;00m[31minfile[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m [39;49;00m[31mdisplay[39;49;00m[37m[39;49;00m$
[37m^I^I[39;49;00m[31mshell-command-switch[39;49;00m[37m[39;49;00m$
[37m^I^I[39;49;00m([32mmapconcat[39;49;00m[37m [39;49;00m[33m'identity[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mcommand[39;49;00m[37m [39;49;00m[31margs[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mprocess-file-shell-command[39;49;00m[37m [39;49;00m([31mcommand[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31minfile[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m [39;49;00m[31mdisplay[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I^I   [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31margs[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mProcess files synchronously in a separate process.[39;49;00m$
[33mSimilar to [39;49;00m[33m`call-process-shell-command'[39;49;00m[33m, but calls [39;49;00m[33m`process-file'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31madvertised-calling-convention[39;49;00m[37m[39;49;00m$
[37m            [39;49;00m([31mcommand[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31minfile[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m [39;49;00m[31mdisplay[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m24.5[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m([31mprocess-file[39;49;00m[37m[39;49;00m$
[37m   [39;49;00m([34mif[39;49;00m[37m [39;49;00m([31mfile-remote-p[39;49;00m[37m [39;49;00m[31mdefault-directory[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m/bin/sh[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mshell-file-name[39;49;00m)[37m[39;49;00m$
[37m   [39;49;00m[31minfile[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m [39;49;00m[31mdisplay[39;49;00m[37m[39;49;00m$
[37m   [39;49;00m([34mif[39;49;00m[37m [39;49;00m([31mfile-remote-p[39;49;00m[37m [39;49;00m[31mdefault-directory[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m-c[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mshell-command-switch[39;49;00m)[37m[39;49;00m$
[37m   [39;49;00m([32mmapconcat[39;49;00m[37m [39;49;00m[33m'identity[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mcommand[39;49;00m[37m [39;49;00m[31margs[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m[37m[39;49;00m$
[37m;;;; Lisp macros to do various things temporarily.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
([36mdefmacro[39;49;00m[37m [39;49;00m[36mtrack-mouse[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mEvaluate BODY with mouse movement events enabled.[39;49;00m$
[33mWithin a [39;49;00m[33m`track-mouse'[39;49;00m[33m form, mouse motion generates input events that[39;49;00m$
[33m you can read with [39;49;00m[33m`read-event'[39;49;00m[33m.[39;49;00m$
[33mNormally, mouse motion is ignored.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m`([32minternal--track-mouse[39;49;00m[37m [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m()[37m [39;49;00m,@[31mbody[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefmacro[39;49;00m[37m [39;49;00m[36mwith-current-buffer[39;49;00m[37m [39;49;00m([31mbuffer-or-name[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mExecute the forms in BODY with BUFFER-OR-NAME temporarily current.[39;49;00m$
[33mBUFFER-OR-NAME must be a buffer or the name of an existing buffer.[39;49;00m$
[33mThe value returned is the value of the last form in BODY.  See[39;49;00m$
[33malso [39;49;00m[33m`with-temp-buffer'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m`([34msave-current-buffer[39;49;00m[37m[39;49;00m$
[37m     [39;49;00m([32mset-buffer[39;49;00m[37m [39;49;00m,[31mbuffer-or-name[39;49;00m)[37m[39;49;00m$
[37m     [39;49;00m,@[31mbody[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31minternal--before-with-selected-window[39;49;00m[37m [39;49;00m([31mwindow[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mother-frame[39;49;00m[37m [39;49;00m([32mwindow-frame[39;49;00m[37m [39;49;00m[31mwindow[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[31mwindow[39;49;00m[37m [39;49;00m([32mselected-window[39;49;00m)[37m[39;49;00m$
[37m          [39;49;00m[37m;; Selecting a window on another frame also changes that[39;49;00m[37m[39;49;00m$
[37m          [39;49;00m[37m;; frame's frame-selected-window.  We must save&restore it.[39;49;00m[37m[39;49;00m$
[37m          [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mselected-frame[39;49;00m)[37m [39;49;00m[31mother-frame[39;49;00m)[37m[39;49;00m$
[37m            [39;49;00m([32mframe-selected-window[39;49;00m[37m [39;49;00m[31mother-frame[39;49;00m))[37m[39;49;00m$
[37m          [39;49;00m[37m;; Also remember the top-frame if on ttys.[39;49;00m[37m[39;49;00m$
[37m          [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mselected-frame[39;49;00m)[37m [39;49;00m[31mother-frame[39;49;00m)[37m[39;49;00m$
[37m            [39;49;00m([32mtty-top-frame[39;49;00m[37m [39;49;00m[31mother-frame[39;49;00m)))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31minternal--after-with-selected-window[39;49;00m[37m [39;49;00m([31mstate[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[37m;; First reset frame-selected-window.[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mwindow-live-p[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m[31mstate[39;49;00m))[37m[39;49;00m$
[37m    [39;49;00m[37m;; We don't use set-frame-selected-window because it does not[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[37m;; pass the `norecord' argument to Fselect_window.[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m([32mselect-window[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m[31mstate[39;49;00m)[37m [39;49;00m[33m'norecord[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mframe-live-p[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m3[39;49;00m[37m [39;49;00m[31mstate[39;49;00m))[37m[39;49;00m$
[37m         [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mtty-top-frame[39;49;00m)[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m3[39;49;00m[37m [39;49;00m[31mstate[39;49;00m)))[37m[39;49;00m$
[37m         [39;49;00m([32mselect-frame[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m3[39;49;00m[37m [39;49;00m[31mstate[39;49;00m)[37m [39;49;00m[33m'norecord[39;49;00m)))[37m[39;49;00m$
[37m  [39;49;00m[37m;; Then reset the actual selected-window.[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mwindow-live-p[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mstate[39;49;00m))[37m[39;49;00m$
[37m    [39;49;00m([32mselect-window[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mstate[39;49;00m)[37m [39;49;00m[33m'norecord[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefmacro[39;49;00m[37m [39;49;00m[36mwith-selected-window[39;49;00m[37m [39;49;00m([31mwindow[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mExecute the forms in BODY with WINDOW as the selected window.[39;49;00m$
[33mThe value returned is the value of the last form in BODY.[39;49;00m$
[33m[39;49;00m$
[33mThis macro saves and restores the selected window, as well as the[39;49;00m$
[33mselected window of each frame.  It does not change the order of[39;49;00m$
[33mrecently selected windows.  If the previously selected window of[39;49;00m$
[33msome frame is no longer live at the end of BODY, that frame's[39;49;00m$
[33mselected window is left alone.  If the selected window is no[39;49;00m$
[33mlonger live, then whatever window is selected at the end of BODY[39;49;00m$
[33mremains selected.[39;49;00m$
[33m[39;49;00m$
[33mThis macro uses [39;49;00m[33m`save-current-buffer'[39;49;00m[33m to save and restore the[39;49;00m$
[33mcurrent buffer, since otherwise its normal operation could[39;49;00m$
[33mpotentially make a different buffer current.  It does not alter[39;49;00m$
[33mthe buffer list ordering.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m(([31msave-selected-window--state[39;49;00m[37m[39;49;00m$
[37m          [39;49;00m([31minternal--before-with-selected-window[39;49;00m[37m [39;49;00m,[31mwindow[39;49;00m)))[37m[39;49;00m$
[37m     [39;49;00m([34msave-current-buffer[39;49;00m[37m[39;49;00m$
[37m       [39;49;00m([34munwind-protect[39;49;00m[37m[39;49;00m$
[37m           [39;49;00m([34mprogn[39;49;00m[37m [39;49;00m([32mselect-window[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31msave-selected-window--state[39;49;00m)[37m [39;49;00m[33m'norecord[39;49;00m)[37m[39;49;00m$
[37m^I^I  [39;49;00m,@[31mbody[39;49;00m)[37m[39;49;00m$
[37m         [39;49;00m([31minternal--after-with-selected-window[39;49;00m[37m [39;49;00m[31msave-selected-window--state[39;49;00m)))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefmacro[39;49;00m[37m [39;49;00m[36mwith-selected-frame[39;49;00m[37m [39;49;00m([31mframe[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mExecute the forms in BODY with FRAME as the selected frame.[39;49;00m$
[33mThe value returned is the value of the last form in BODY.[39;49;00m$
[33m[39;49;00m$
[33mThis macro saves and restores the selected frame, and changes the[39;49;00m$
[33morder of neither the recently selected windows nor the buffers in[39;49;00m$
[33mthe buffer list.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mold-frame[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mold-frame[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
[37m^I[39;49;00m([31mold-buffer[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mold-buffer[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m((,[31mold-frame[39;49;00m[37m [39;49;00m([32mselected-frame[39;49;00m))[37m[39;49;00m$
[37m^I   [39;49;00m(,[31mold-buffer[39;49;00m[37m [39;49;00m([32mcurrent-buffer[39;49;00m)))[37m[39;49;00m$
[37m       [39;49;00m([34munwind-protect[39;49;00m[37m[39;49;00m$
[37m^I   [39;49;00m([34mprogn[39;49;00m[37m [39;49;00m([32mselect-frame[39;49;00m[37m [39;49;00m,[31mframe[39;49;00m[37m [39;49;00m[33m'norecord[39;49;00m)[37m[39;49;00m$
[37m^I^I  [39;49;00m,@[31mbody[39;49;00m)[37m[39;49;00m$
[37m^I [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mframe-live-p[39;49;00m[37m [39;49;00m,[31mold-frame[39;49;00m)[37m[39;49;00m$
[37m^I   [39;49;00m([32mselect-frame[39;49;00m[37m [39;49;00m,[31mold-frame[39;49;00m[37m [39;49;00m[33m'norecord[39;49;00m))[37m[39;49;00m$
[37m^I [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mbuffer-live-p[39;49;00m[37m [39;49;00m,[31mold-buffer[39;49;00m)[37m[39;49;00m$
[37m^I   [39;49;00m([32mset-buffer[39;49;00m[37m [39;49;00m,[31mold-buffer[39;49;00m))))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefmacro[39;49;00m[37m [39;49;00m[36msave-window-excursion[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mExecute BODY, then restore previous window configuration.[39;49;00m$
[33mThis macro saves the window configuration on the selected frame,[39;49;00m$
[33mexecutes BODY, then calls [39;49;00m[33m`set-window-configuration'[39;49;00m[33m to restore[39;49;00m$
[33mthe saved window configuration.  The return value is the last[39;49;00m$
[33mform in BODY.  The window configuration is also restored if BODY[39;49;00m$
[33mexits nonlocally.[39;49;00m$
[33m[39;49;00m$
[33mBEWARE: Most uses of this macro introduce bugs.[39;49;00m$
[33mE.g. it should not be used to try and prevent some code from opening[39;49;00m$
[33ma new window, since that window may sometimes appear in another frame,[39;49;00m$
[33min which case [39;49;00m[33m`save-window-excursion'[39;49;00m[33m cannot help.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mc[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mwconfig[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m((,[31mc[39;49;00m[37m [39;49;00m([32mcurrent-window-configuration[39;49;00m)))[37m[39;49;00m$
[37m       [39;49;00m([34munwind-protect[39;49;00m[37m [39;49;00m([34mprogn[39;49;00m[37m [39;49;00m,@[31mbody[39;49;00m)[37m[39;49;00m$
[37m         [39;49;00m([32mset-window-configuration[39;49;00m[37m [39;49;00m,[31mc[39;49;00m)))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31minternal-temp-output-buffer-show[39;49;00m[37m [39;49;00m([31mbuffer[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mInternal function for [39;49;00m[33m`with-output-to-temp-buffer'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mwith-current-buffer[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m([32mset-buffer-modified-p[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([32mgoto-char[39;49;00m[37m [39;49;00m([32mpoint-min[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mtemp-buffer-show-function[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mtemp-buffer-show-function[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([36mwith-current-buffer[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mwindow[39;49;00m[37m[39;49;00m$
[37m^I      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([32mwindow-combination-limit[39;49;00m[37m[39;49;00m$
[37m^I^I   [39;49;00m[37m;; When `window-combination-limit' equals[39;49;00m[37m[39;49;00m$
[37m^I^I   [39;49;00m[37m;; `temp-buffer' or `temp-buffer-resize' and[39;49;00m[37m[39;49;00m$
[37m^I^I   [39;49;00m[37m;; `temp-buffer-resize-mode' is enabled in this[39;49;00m[37m[39;49;00m$
[37m^I^I   [39;49;00m[37m;; buffer bind it to t so resizing steals space[39;49;00m[37m[39;49;00m$
[37m^I^I   [39;49;00m[37m;; preferably from the window that was split.[39;49;00m[37m[39;49;00m$
[37m^I^I   [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[32mwindow-combination-limit[39;49;00m[37m [39;49;00m[33m'temp-buffer[39;49;00m)[37m[39;49;00m$
[37m^I^I^I   [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[32mwindow-combination-limit[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I    [39;49;00m[33m'temp-buffer-resize[39;49;00m)[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[31mtemp-buffer-resize-mode[39;49;00m))[37m[39;49;00m$
[37m^I^I       [39;49;00m[31mt[39;49;00m[37m[39;49;00m$
[37m^I^I     [39;49;00m[32mwindow-combination-limit[39;49;00m)))[37m[39;49;00m$
[37m^I^I[39;49;00m([31mdisplay-buffer[39;49;00m[37m [39;49;00m[31mbuffer[39;49;00m)))[37m[39;49;00m$
[37m^I     [39;49;00m([31mframe[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mwindow[39;49;00m[37m [39;49;00m([32mwindow-frame[39;49;00m[37m [39;49;00m[31mwindow[39;49;00m))))[37m[39;49;00m$
[37m^I[39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31mwindow[39;49;00m[37m[39;49;00m$
[37m^I  [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mframe[39;49;00m[37m [39;49;00m([32mselected-frame[39;49;00m))[37m[39;49;00m$
[37m^I    [39;49;00m([32mmake-frame-visible[39;49;00m[37m [39;49;00m[31mframe[39;49;00m))[37m[39;49;00m$
[37m^I  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mminibuffer-scroll-window[39;49;00m[37m [39;49;00m[31mwindow[39;49;00m)[37m[39;49;00m$
[37m^I  [39;49;00m([32mset-window-hscroll[39;49;00m[37m [39;49;00m[31mwindow[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m^I  [39;49;00m[37m;; Don't try this with NOFORCE non-nil![39;49;00m[37m[39;49;00m$
[37m^I  [39;49;00m([32mset-window-start[39;49;00m[37m [39;49;00m[31mwindow[39;49;00m[37m [39;49;00m([32mpoint-min[39;49;00m)[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
[37m^I  [39;49;00m[37m;; This should not be necessary.[39;49;00m[37m[39;49;00m$
[37m^I  [39;49;00m([32mset-window-point[39;49;00m[37m [39;49;00m[31mwindow[39;49;00m[37m [39;49;00m([32mpoint-min[39;49;00m))[37m[39;49;00m$
[37m^I  [39;49;00m[37m;; Run `temp-buffer-show-hook', with the chosen window selected.[39;49;00m[37m[39;49;00m$
[37m^I  [39;49;00m([36mwith-selected-window[39;49;00m[37m [39;49;00m[31mwindow[39;49;00m[37m[39;49;00m$
[37m^I    [39;49;00m([32mrun-hooks[39;49;00m[37m [39;49;00m[33m'temp-buffer-show-hook[39;49;00m))))))[37m[39;49;00m$
[37m  [39;49;00m[37m;; Return nil.[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
[37m;; Doc is very similar to with-temp-buffer-window.[39;49;00m[37m[39;49;00m$
([36mdefmacro[39;49;00m[37m [39;49;00m[36mwith-output-to-temp-buffer[39;49;00m[37m [39;49;00m([31mbufname[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mBind [39;49;00m[33m`standard-output'[39;49;00m[33m to buffer BUFNAME, eval BODY, then show that buffer.[39;49;00m$
[33m[39;49;00m$
[33mThis construct makes buffer BUFNAME empty before running BODY.[39;49;00m$
[33mIt does not make the buffer current for BODY.[39;49;00m$
[33mInstead it binds [39;49;00m[33m`standard-output'[39;49;00m[33m to that buffer, so that output[39;49;00m$
[33mgenerated with [39;49;00m[33m`prin1'[39;49;00m[33m and similar functions in BODY goes into[39;49;00m$
[33mthe buffer.[39;49;00m$
[33m[39;49;00m$
[33mAt the end of BODY, this marks buffer BUFNAME unmodified and displays[39;49;00m$
[33mit in a window, but does not select it.  The normal way to do this is[39;49;00m$
[33mby calling [39;49;00m[33m`display-buffer'[39;49;00m[33m, then running [39;49;00m[33m`temp-buffer-show-hook'[39;49;00m[33m.[39;49;00m$
[33mHowever, if [39;49;00m[33m`temp-buffer-show-function'[39;49;00m[33m is non-nil, it calls that[39;49;00m$
[33mfunction instead (and does not run [39;49;00m[33m`temp-buffer-show-hook'[39;49;00m[33m).  The[39;49;00m$
[33mfunction gets one argument, the buffer to display.[39;49;00m$
[33m[39;49;00m$
[33mThe return value of [39;49;00m[33m`with-output-to-temp-buffer'[39;49;00m[33m is the value of the[39;49;00m$
[33mlast form in BODY.  If BODY does not finish normally, the buffer[39;49;00m$
[33mBUFNAME is not displayed.[39;49;00m$
[33m[39;49;00m$
[33mThis runs the hook [39;49;00m[33m`temp-buffer-setup-hook'[39;49;00m[33m before BODY,[39;49;00m$
[33mwith the buffer BUFNAME temporarily current.  It runs the hook[39;49;00m$
[33m`temp-buffer-show-hook'[39;49;00m[33m after displaying buffer BUFNAME, with that[39;49;00m$
[33mbuffer temporarily current, and the window that was used to display it[39;49;00m$
[33mtemporarily selected.  But it doesn't run [39;49;00m[33m`temp-buffer-show-hook'[39;49;00m[33m[39;49;00m$
[33mif it uses [39;49;00m[33m`temp-buffer-show-function'[39;49;00m[33m.[39;49;00m$
[33m[39;49;00m$
[33mBy default, the setup hook puts the buffer into Help mode before running BODY.[39;49;00m$
[33mIf BODY does not change the major mode, the show hook makes the buffer[39;49;00m$
[33mread-only, and scans it for function and variable names to make them into[39;49;00m$
[33mclickable cross-references.[39;49;00m$
[33m[39;49;00m$
[33mSee the related form [39;49;00m[33m`with-temp-buffer-window'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mold-dir[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mold-dir[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
[37m        [39;49;00m([31mbuf[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mbuf[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m`([34mlet*[39;49;00m[37m [39;49;00m((,[31mold-dir[39;49;00m[37m [39;49;00m[31mdefault-directory[39;49;00m)[37m[39;49;00m$
[37m            [39;49;00m(,[31mbuf[39;49;00m[37m[39;49;00m$
[37m             [39;49;00m([36mwith-current-buffer[39;49;00m[37m [39;49;00m([32mget-buffer-create[39;49;00m[37m [39;49;00m,[31mbufname[39;49;00m)[37m[39;49;00m$
[37m               [39;49;00m([34mprog1[39;49;00m[37m [39;49;00m([32mcurrent-buffer[39;49;00m)[37m[39;49;00m$
[37m                 [39;49;00m([32mkill-all-local-variables[39;49;00m)[37m[39;49;00m$
[37m                 [39;49;00m[37m;; FIXME: delete_all_overlays[39;49;00m[37m[39;49;00m$
[37m                 [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mdefault-directory[39;49;00m[37m [39;49;00m,[31mold-dir[39;49;00m)[37m[39;49;00m$
[37m                 [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbuffer-read-only[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
[37m                 [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[32mbuffer-file-name[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
[37m                 [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbuffer-undo-list[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
[37m                 [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31minhibit-read-only[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
[37m                       [39;49;00m([31minhibit-modification-hooks[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
[37m                   [39;49;00m([32merase-buffer[39;49;00m)[37m[39;49;00m$
[37m                   [39;49;00m([32mrun-hooks[39;49;00m[37m [39;49;00m[33m'temp-buffer-setup-hook[39;49;00m)))))[37m[39;49;00m$
[37m            [39;49;00m([31mstandard-output[39;49;00m[37m [39;49;00m,[31mbuf[39;49;00m))[37m[39;49;00m$
[37m       [39;49;00m([34mprog1[39;49;00m[37m [39;49;00m([34mprogn[39;49;00m[37m [39;49;00m,@[31mbody[39;49;00m)[37m[39;49;00m$
[37m         [39;49;00m([31minternal-temp-output-buffer-show[39;49;00m[37m [39;49;00m,[31mbuf[39;49;00m)))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefmacro[39;49;00m[37m [39;49;00m[36mwith-temp-file[39;49;00m[37m [39;49;00m([31mfile[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mCreate a new buffer, evaluate BODY there, and write the buffer to FILE.[39;49;00m$
[33mThe value returned is the value of the last form in BODY.[39;49;00m$
[33mSee also [39;49;00m[33m`with-temp-buffer'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtemp-file[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mtemp-file[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
[37m^I[39;49;00m([31mtemp-buffer[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mtemp-buffer[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m((,[31mtemp-file[39;49;00m[37m [39;49;00m,[31mfile[39;49;00m)[37m[39;49;00m$
[37m^I   [39;49;00m(,[31mtemp-buffer[39;49;00m[37m[39;49;00m$
[37m^I    [39;49;00m([32mget-buffer-create[39;49;00m[37m [39;49;00m([32mgenerate-new-buffer-name[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m *temp file*[39;49;00m[33m"[39;49;00m))))[37m[39;49;00m$
[37m       [39;49;00m([34munwind-protect[39;49;00m[37m[39;49;00m$
[37m^I   [39;49;00m([34mprog1[39;49;00m[37m[39;49;00m$
[37m^I       [39;49;00m([36mwith-current-buffer[39;49;00m[37m [39;49;00m,[31mtemp-buffer[39;49;00m[37m[39;49;00m$
[37m^I^I [39;49;00m,@[31mbody[39;49;00m)[37m[39;49;00m$
[37m^I     [39;49;00m([36mwith-current-buffer[39;49;00m[37m [39;49;00m,[31mtemp-buffer[39;49;00m[37m[39;49;00m$
[37m^I       [39;49;00m([32mwrite-region[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m,[31mtemp-file[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[34m0[39;49;00m)))[37m[39;49;00m$
[37m^I [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mbuffer-name[39;49;00m[37m [39;49;00m,[31mtemp-buffer[39;49;00m)[37m[39;49;00m$
[37m^I      [39;49;00m([32mkill-buffer[39;49;00m[37m [39;49;00m,[31mtemp-buffer[39;49;00m))))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefmacro[39;49;00m[37m [39;49;00m[36mwith-temp-message[39;49;00m[37m [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mDisplay MESSAGE temporarily if non-nil while BODY is evaluated.[39;49;00m$
[33mThe original message is restored to the echo area after BODY has finished.[39;49;00m$
[33mThe value returned is the value of the last form in BODY.[39;49;00m$
[33mMESSAGE is written to the message log buffer if [39;49;00m[33m`message-log-max'[39;49;00m[33m is non-nil.[39;49;00m$
[33mIf MESSAGE is nil, the echo area and message log buffer are unchanged.[39;49;00m$
[33mUse a MESSAGE of [39;49;00m[33m\"[39;49;00m[33m\"[39;49;00m[33m to temporarily clear the echo area.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m1[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([32mcurrent-message[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mcurrent-message[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
[37m^I[39;49;00m([31mtemp-message[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mwith-temp-message[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m((,[31mtemp-message[39;49;00m[37m [39;49;00m,[32mmessage[39;49;00m)[37m[39;49;00m$
[37m^I   [39;49;00m(,[32mcurrent-message[39;49;00m))[37m[39;49;00m$
[37m       [39;49;00m([34munwind-protect[39;49;00m[37m[39;49;00m$
[37m^I   [39;49;00m([34mprogn[39;49;00m[37m[39;49;00m$
[37m^I     [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m,[31mtemp-message[39;49;00m[37m[39;49;00m$
[37m^I       [39;49;00m([34msetq[39;49;00m[37m [39;49;00m,[32mcurrent-message[39;49;00m[37m [39;49;00m([32mcurrent-message[39;49;00m))[37m[39;49;00m$
[37m^I       [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m%s[39;49;00m[33m"[39;49;00m[37m [39;49;00m,[31mtemp-message[39;49;00m))[37m[39;49;00m$
[37m^I     [39;49;00m,@[31mbody[39;49;00m)[37m[39;49;00m$
[37m^I [39;49;00m([34mand[39;49;00m[37m [39;49;00m,[31mtemp-message[39;49;00m[37m[39;49;00m$
[37m^I      [39;49;00m([34mif[39;49;00m[37m [39;49;00m,[32mcurrent-message[39;49;00m[37m[39;49;00m$
[37m^I^I  [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m%s[39;49;00m[33m"[39;49;00m[37m [39;49;00m,[32mcurrent-message[39;49;00m)[37m[39;49;00m$
[37m^I^I[39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)))))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefmacro[39;49;00m[37m [39;49;00m[36mwith-temp-buffer[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mCreate a temporary buffer, and evaluate BODY there like [39;49;00m[33m`progn'[39;49;00m[33m.[39;49;00m$
[33mSee also [39;49;00m[33m`with-temp-file'[39;49;00m[33m and [39;49;00m[33m`with-output-to-string'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtemp-buffer[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mtemp-buffer[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m((,[31mtemp-buffer[39;49;00m[37m [39;49;00m([31mgenerate-new-buffer[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m *temp*[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
[37m       [39;49;00m[37m;; FIXME: kill-buffer can change current-buffer in some odd cases.[39;49;00m[37m[39;49;00m$
[37m       [39;49;00m([36mwith-current-buffer[39;49;00m[37m [39;49;00m,[31mtemp-buffer[39;49;00m[37m[39;49;00m$
[37m         [39;49;00m([34munwind-protect[39;49;00m[37m[39;49;00m$
[37m^I     [39;49;00m([34mprogn[39;49;00m[37m [39;49;00m,@[31mbody[39;49;00m)[37m[39;49;00m$
[37m           [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mbuffer-name[39;49;00m[37m [39;49;00m,[31mtemp-buffer[39;49;00m)[37m[39;49;00m$
[37m                [39;49;00m([32mkill-buffer[39;49;00m[37m [39;49;00m,[31mtemp-buffer[39;49;00m)))))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefmacro[39;49;00m[37m [39;49;00m[36mwith-silent-modifications[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mExecute BODY, pretending it does not modify the buffer.[39;49;00m$
[33mIf BODY performs real modifications to the buffer's text, other[39;49;00m$
[33mthan cosmetic ones, undo data may become corrupted.[39;49;00m$
[33m[39;49;00m$
[33mThis macro will run BODY normally, but doesn't count its buffer[39;49;00m$
[33mmodifications as being buffer modifications.  This affects things[39;49;00m$
[33mlike [39;49;00m[33m`buffer-modified-p'[39;49;00m[33m, checking whether the file is locked by[39;49;00m$
[33msomeone else, running buffer modification hooks, and other things[39;49;00m$
[33mof that nature.[39;49;00m$
[33m[39;49;00m$
[33mTypically used around modifications of text-properties which do[39;49;00m$
[33mnot really affect the buffer's content.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mmodified[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mmodified[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m`([34mlet*[39;49;00m[37m [39;49;00m((,[31mmodified[39;49;00m[37m [39;49;00m([32mbuffer-modified-p[39;49;00m))[37m[39;49;00m$
[37m            [39;49;00m([31mbuffer-undo-list[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
[37m            [39;49;00m([31minhibit-read-only[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
[37m            [39;49;00m([31minhibit-modification-hooks[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
[37m       [39;49;00m([34munwind-protect[39;49;00m[37m[39;49;00m$
[37m           [39;49;00m([34mprogn[39;49;00m[37m[39;49;00m$
[37m             [39;49;00m,@[31mbody[39;49;00m)[37m[39;49;00m$
[37m         [39;49;00m([36munless[39;49;00m[37m [39;49;00m,[31mmodified[39;49;00m[37m[39;49;00m$
[37m           [39;49;00m([32mrestore-buffer-modified-p[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefmacro[39;49;00m[37m [39;49;00m[36mwith-output-to-string[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mExecute BODY, return the text it sent to [39;49;00m[33m`standard-output'[39;49;00m[33m, as a string.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m(([31mstandard-output[39;49;00m[37m[39;49;00m$
[37m^I  [39;49;00m([32mget-buffer-create[39;49;00m[37m [39;49;00m([32mgenerate-new-buffer-name[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m *string-output*[39;49;00m[33m"[39;49;00m))))[37m[39;49;00m$
[37m     [39;49;00m([34munwind-protect[39;49;00m[37m[39;49;00m$
[37m^I [39;49;00m([34mprogn[39;49;00m[37m[39;49;00m$
[37m^I   [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mstandard-output[39;49;00m[37m [39;49;00m[31mstandard-output[39;49;00m))[37m[39;49;00m$
[37m^I     [39;49;00m,@[31mbody[39;49;00m)[37m[39;49;00m$
[37m^I   [39;49;00m([36mwith-current-buffer[39;49;00m[37m [39;49;00m[31mstandard-output[39;49;00m[37m[39;49;00m$
[37m^I     [39;49;00m([32mbuffer-string[39;49;00m)))[37m[39;49;00m$
[37m       [39;49;00m([32mkill-buffer[39;49;00m[37m [39;49;00m[31mstandard-output[39;49;00m))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefmacro[39;49;00m[37m [39;49;00m[36mwith-local-quit[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mExecute BODY, allowing quits to terminate BODY but not escape further.[39;49;00m$
[33mWhen a quit terminates BODY, [39;49;00m[33m`with-local-quit'[39;49;00m[33m returns nil but[39;49;00m$
[33mrequests another quit.  That quit will be processed as soon as quitting[39;49;00m$
[33mis allowed once again.  (Immediately, if [39;49;00m[33m`inhibit-quit'[39;49;00m[33m is nil.)[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m`([34mcondition-case[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m$
[37m       [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31minhibit-quit[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m$
[37m^I [39;49;00m,@[31mbody[39;49;00m)[37m[39;49;00m$
[37m     [39;49;00m([31mquit[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mquit-flag[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
[37m^I   [39;49;00m[37m;; This call is to give a chance to handle quit-flag[39;49;00m[37m[39;49;00m$
[37m^I   [39;49;00m[37m;; in case inhibit-quit is nil.[39;49;00m[37m[39;49;00m$
[37m^I   [39;49;00m[37m;; Without this, it will not be handled until the next function[39;49;00m[37m[39;49;00m$
[37m^I   [39;49;00m[37m;; call, and that might allow it to exit thru a condition-case[39;49;00m[37m[39;49;00m$
[37m^I   [39;49;00m[37m;; that intends to handle the quit signal next time.[39;49;00m[37m[39;49;00m$
[37m^I   [39;49;00m([32meval[39;49;00m[37m [39;49;00m'([31mignore[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefmacro[39;49;00m[37m [39;49;00m[36mwhile-no-input[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mExecute BODY only as long as there's no pending input.[39;49;00m$
[33mIf input arrives, that ends the execution of BODY,[39;49;00m$
[33mand [39;49;00m[33m`while-no-input'[39;49;00m[33m returns t.  Quitting makes it return nil.[39;49;00m$
[33mIf BODY finishes, [39;49;00m[33m`while-no-input'[39;49;00m[33m returns whatever value BODY produced.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mcatch-sym[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33minput[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m`([36mwith-local-quit[39;49;00m[37m[39;49;00m$
[37m       [39;49;00m([34mcatch[39;49;00m[37m [39;49;00m[33m',catch-sym[39;49;00m[37m[39;49;00m$
[37m^I [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mthrow-on-input[39;49;00m[37m [39;49;00m[33m',catch-sym[39;49;00m))[37m[39;49;00m$
[37m^I   [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32minput-pending-p[39;49;00m)[37m[39;49;00m$
[37m^I       [39;49;00m([34mprogn[39;49;00m[37m [39;49;00m,@[31mbody[39;49;00m)))))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefmacro[39;49;00m[37m [39;49;00m[36mcondition-case-unless-debug[39;49;00m[37m [39;49;00m([31mvar[39;49;00m[37m [39;49;00m[31mbodyform[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mhandlers[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mLike [39;49;00m[33m`condition-case'[39;49;00m[33m except that it does not prevent debugging.[39;49;00m$
[33mMore specifically if [39;49;00m[33m`debug-on-error'[39;49;00m[33m is set then the debugger will be invoked[39;49;00m$
[33meven if this catches the signal.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[34mcondition-case[39;49;00m)[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m2[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m`([34mcondition-case[39;49;00m[37m [39;49;00m,[31mvar[39;49;00m[37m[39;49;00m$
[37m       [39;49;00m,[31mbodyform[39;49;00m[37m[39;49;00m$
[37m     [39;49;00m,@([32mmapcar[39;49;00m[37m [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31mhandler[39;49;00m)[37m[39;49;00m$
[37m                 [39;49;00m`(([31mdebug[39;49;00m[37m [39;49;00m,@([34mif[39;49;00m[37m [39;49;00m([32mlistp[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mhandler[39;49;00m))[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mhandler[39;49;00m)[37m[39;49;00m$
[37m                              [39;49;00m([32mlist[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mhandler[39;49;00m))))[37m[39;49;00m$
[37m                   [39;49;00m,@([32mcdr[39;49;00m[37m [39;49;00m[31mhandler[39;49;00m)))[37m[39;49;00m$
[37m               [39;49;00m[31mhandlers[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefine-obsolete-function-alias[39;49;00m[37m [39;49;00m[33m'condition-case-no-debug[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[33m'condition-case-unless-debug[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m24.1[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
([36mdefmacro[39;49;00m[37m [39;49;00m[36mwith-demoted-errors[39;49;00m[37m [39;49;00m([32mformat[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mRun BODY and demote any errors to simple messages.[39;49;00m$
[33mFORMAT is a string passed to [39;49;00m[33m`message'[39;49;00m[33m to format any error message.[39;49;00m$
[33mIt should contain a single %-sequence; e.g., [39;49;00m[33m\"[39;49;00m[33mError: %S[39;49;00m[33m\"[39;49;00m[33m.[39;49;00m$
[33m[39;49;00m$
[33mIf [39;49;00m[33m`debug-on-error'[39;49;00m[33m is non-nil, run BODY without catching its errors.[39;49;00m$
[33mThis is to be used around code which is not expected to signal an error[39;49;00m$
[33mbut which should be robust in the unexpected case that an error is signaled.[39;49;00m$
[33m[39;49;00m$
[33mFor backward compatibility, if FORMAT is not a constant string, it[39;49;00m$
[33mis assumed to be part of BODY, in which case the message format[39;49;00m$
[33mused is [39;49;00m[33m\"[39;49;00m[33mError: %S[39;49;00m[33m\"[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m1[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31merr[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33merr[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
[37m        [39;49;00m([32mformat[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m[32mformat[39;49;00m)[37m [39;49;00m[31mbody[39;49;00m)[37m [39;49;00m[32mformat[39;49;00m[37m[39;49;00m$
[37m                  [39;49;00m([34mprog1[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mError: %S[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m                    [39;49;00m([34mif[39;49;00m[37m [39;49;00m[32mformat[39;49;00m[37m [39;49;00m([36mpush[39;49;00m[37m [39;49;00m[32mformat[39;49;00m[37m [39;49;00m[31mbody[39;49;00m))))))[37m[39;49;00m$
[37m    [39;49;00m`([36mcondition-case-unless-debug[39;49;00m[37m [39;49;00m,[31merr[39;49;00m[37m[39;49;00m$
[37m         [39;49;00m,([31mmacroexp-progn[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
[37m       [39;49;00m([36merror[39;49;00m[37m [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m,[32mformat[39;49;00m[37m [39;49;00m,[31merr[39;49;00m)[37m [39;49;00m[31mnil[39;49;00m))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefmacro[39;49;00m[37m [39;49;00m[36mcombine-after-change-calls[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mExecute BODY, but don't call the after-change functions till the end.[39;49;00m$
[33mIf BODY makes changes in the buffer, they are recorded[39;49;00m$
[33mand the functions on [39;49;00m[33m`after-change-functions'[39;49;00m[33m are called several times[39;49;00m$
[33mwhen BODY is finished.[39;49;00m$
[33mThe return value is the value of the last form in BODY.[39;49;00m$
[33m[39;49;00m$
[33mIf [39;49;00m[33m`before-change-functions'[39;49;00m[33m is non-nil, then calls to the after-change[39;49;00m$
[33mfunctions can't be deferred, so in that case this macro has no effect.[39;49;00m$
[33m[39;49;00m$
[33mDo not alter [39;49;00m[33m`after-change-functions'[39;49;00m[33m or [39;49;00m[33m`before-change-functions'[39;49;00m[33m[39;49;00m$
[33min BODY.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m`([34munwind-protect[39;49;00m[37m[39;49;00m$
[37m       [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([36mcombine-after-change-calls[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
[37m^I [39;49;00m.[37m [39;49;00m,[31mbody[39;49;00m)[37m[39;49;00m$
[37m     [39;49;00m([32mcombine-after-change-execute[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefmacro[39;49;00m[37m [39;49;00m[36mwith-case-table[39;49;00m[37m [39;49;00m([31mtable[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mExecute the forms in BODY with TABLE as the current case table.[39;49;00m$
[33mThe value returned is the value of the last form in BODY.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mold-case-table[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mtable[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
[37m^I[39;49;00m([31mold-buffer[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mbuffer[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m((,[31mold-case-table[39;49;00m[37m [39;49;00m([32mcurrent-case-table[39;49;00m))[37m[39;49;00m$
[37m^I   [39;49;00m(,[31mold-buffer[39;49;00m[37m [39;49;00m([32mcurrent-buffer[39;49;00m)))[37m[39;49;00m$
[37m       [39;49;00m([34munwind-protect[39;49;00m[37m[39;49;00m$
[37m^I   [39;49;00m([34mprogn[39;49;00m[37m [39;49;00m([32mset-case-table[39;49;00m[37m [39;49;00m,[31mtable[39;49;00m)[37m[39;49;00m$
[37m^I^I  [39;49;00m,@[31mbody[39;49;00m)[37m[39;49;00m$
[37m^I [39;49;00m([36mwith-current-buffer[39;49;00m[37m [39;49;00m,[31mold-buffer[39;49;00m[37m[39;49;00m$
[37m^I   [39;49;00m([32mset-case-table[39;49;00m[37m [39;49;00m,[31mold-case-table[39;49;00m))))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefmacro[39;49;00m[37m [39;49;00m[36mwith-file-modes[39;49;00m[37m [39;49;00m([31mmodes[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mExecute BODY with default file permissions temporarily set to MODES.[39;49;00m$
[33mMODES is as for [39;49;00m[33m`set-default-file-modes'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mumask[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mumask[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m((,[31mumask[39;49;00m[37m [39;49;00m([32mdefault-file-modes[39;49;00m)))[37m[39;49;00m$
[37m       [39;49;00m([34munwind-protect[39;49;00m[37m[39;49;00m$
[37m           [39;49;00m([34mprogn[39;49;00m[37m[39;49;00m$
[37m             [39;49;00m([32mset-default-file-modes[39;49;00m[37m [39;49;00m,[31mmodes[39;49;00m)[37m[39;49;00m$
[37m             [39;49;00m,@[31mbody[39;49;00m)[37m[39;49;00m$
[37m         [39;49;00m([32mset-default-file-modes[39;49;00m[37m [39;49;00m,[31mumask[39;49;00m)))))[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m[37m[39;49;00m$
[37m;;; Matching and match data.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
([34mdefvar[39;49;00m[37m [39;49;00m[31msave-match-data-internal[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
[37m;; We use save-match-data-internal as the local variable because[39;49;00m[37m[39;49;00m$
[37m;; that works ok in practice (people should not use that variable elsewhere).[39;49;00m[37m[39;49;00m$
[37m;; We used to use an uninterned symbol; the compiler handles that properly[39;49;00m[37m[39;49;00m$
[37m;; now, but it generates slower code.[39;49;00m[37m[39;49;00m$
([36mdefmacro[39;49;00m[37m [39;49;00m[36msave-match-data[39;49;00m[37m [39;49;00m([34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mExecute the BODY forms, restoring the global value of the match data.[39;49;00m$
[33mThe value returned is the value of the last form in BODY.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; It is better not to use backquote here,[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; because that makes a bootstrapping problem[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; if you need to recompile all the Lisp files using interpreted code.[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'let[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00m'(([31msave-match-data-internal[39;49;00m[37m [39;49;00m([32mmatch-data[39;49;00m)))[37m[39;49;00m$
[37m^I[39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'unwind-protect[39;49;00m[37m[39;49;00m$
[37m^I      [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[33m'progn[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
[37m^I      [39;49;00m[37m;; It is safe to free (evaporate) markers immediately here,[39;49;00m[37m[39;49;00m$
[37m^I      [39;49;00m[37m;; as Lisp programs should not copy from save-match-data-internal.[39;49;00m[37m[39;49;00m$
[37m^I      [39;49;00m'([32mset-match-data[39;49;00m[37m [39;49;00m[31msave-match-data-internal[39;49;00m[37m [39;49;00m[33m'evaporate[39;49;00m))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mmatch-string[39;49;00m[37m [39;49;00m([31mnum[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[32mstring[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn string of text matched by last search.[39;49;00m$
[33mNUM specifies which parenthesized expression in the last regexp.[39;49;00m$
[33m Value is nil if NUMth pair didn't match, or there were less than NUM pairs.[39;49;00m$
[33mZero means the entire text matched by the whole regexp or whole string.[39;49;00m$
[33mSTRING should be given if the last search was by [39;49;00m[33m`string-match'[39;49;00m[33m on STRING.[39;49;00m$
[33mIf STRING is nil, the current buffer should be the same buffer[39;49;00m$
[33mthe search/match was performed in.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mmatch-beginning[39;49;00m[37m [39;49;00m[31mnum[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m[39;49;00m$
[37m^I  [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m([32mmatch-beginning[39;49;00m[37m [39;49;00m[31mnum[39;49;00m)[37m [39;49;00m([32mmatch-end[39;49;00m[37m [39;49;00m[31mnum[39;49;00m))[37m[39;49;00m$
[37m^I[39;49;00m([32mbuffer-substring[39;49;00m[37m [39;49;00m([32mmatch-beginning[39;49;00m[37m [39;49;00m[31mnum[39;49;00m)[37m [39;49;00m([32mmatch-end[39;49;00m[37m [39;49;00m[31mnum[39;49;00m)))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mmatch-string-no-properties[39;49;00m[37m [39;49;00m([31mnum[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[32mstring[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn string of text matched by last search, without text properties.[39;49;00m$
[33mNUM specifies which parenthesized expression in the last regexp.[39;49;00m$
[33m Value is nil if NUMth pair didn't match, or there were less than NUM pairs.[39;49;00m$
[33mZero means the entire text matched by the whole regexp or whole string.[39;49;00m$
[33mSTRING should be given if the last search was by [39;49;00m[33m`string-match'[39;49;00m[33m on STRING.[39;49;00m$
[33mIf STRING is nil, the current buffer should be the same buffer[39;49;00m$
[33mthe search/match was performed in.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mmatch-beginning[39;49;00m[37m [39;49;00m[31mnum[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m[39;49;00m$
[37m^I  [39;49;00m([32msubstring-no-properties[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m([32mmatch-beginning[39;49;00m[37m [39;49;00m[31mnum[39;49;00m)[37m[39;49;00m$
[37m^I^I^I^I   [39;49;00m([32mmatch-end[39;49;00m[37m [39;49;00m[31mnum[39;49;00m))[37m[39;49;00m$
[37m^I[39;49;00m([32mbuffer-substring-no-properties[39;49;00m[37m [39;49;00m([32mmatch-beginning[39;49;00m[37m [39;49;00m[31mnum[39;49;00m)[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m([32mmatch-end[39;49;00m[37m [39;49;00m[31mnum[39;49;00m)))))[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mmatch-substitute-replacement[39;49;00m[37m [39;49;00m([31mreplacement[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I     [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mfixedcase[39;49;00m[37m [39;49;00m[31mliteral[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[31msubexp[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn REPLACEMENT as it will be inserted by [39;49;00m[33m`replace-match'[39;49;00m[33m.[39;49;00m$
[33mIn other words, all back-references in the form [39;49;00m[33m`\\&'[39;49;00m[33m and [39;49;00m[33m`\\N'[39;49;00m[33m[39;49;00m$
[33mare substituted with actual strings matched by the last search.[39;49;00m$
[33mOptional FIXEDCASE, LITERAL, STRING and SUBEXP have the same[39;49;00m$
[33mmeaning as for [39;49;00m[33m`replace-match'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mmatch[39;49;00m[37m [39;49;00m([31mmatch-string[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[32mstring[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m([36msave-match-data[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([32mset-match-data[39;49;00m[37m [39;49;00m([32mmapcar[39;49;00m[37m [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31mx[39;49;00m)[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mnumberp[39;49;00m[37m [39;49;00m[31mx[39;49;00m)[37m[39;49;00m$
[37m^I^I^I^I    [39;49;00m([32m-[39;49;00m[37m [39;49;00m[31mx[39;49;00m[37m [39;49;00m([32mmatch-beginning[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m$
[37m^I^I^I^I  [39;49;00m[31mx[39;49;00m))[37m[39;49;00m$
[37m^I^I^I      [39;49;00m([32mmatch-data[39;49;00m[37m [39;49;00m[31mt[39;49;00m)))[37m[39;49;00m$
[37m      [39;49;00m([32mreplace-match[39;49;00m[37m [39;49;00m[31mreplacement[39;49;00m[37m [39;49;00m[31mfixedcase[39;49;00m[37m [39;49;00m[31mliteral[39;49;00m[37m [39;49;00m[31mmatch[39;49;00m[37m [39;49;00m[31msubexp[39;49;00m))))[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mlooking-back[39;49;00m[37m [39;49;00m([31mregexp[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mlimit[39;49;00m[37m [39;49;00m[31mgreedy[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn non-nil if text before point matches regular expression REGEXP.[39;49;00m$
[33mLike [39;49;00m[33m`looking-at'[39;49;00m[33m except matches before point, and is slower.[39;49;00m$
[33mLIMIT if non-nil speeds up the search by specifying a minimum[39;49;00m$
[33mstarting position, to avoid checking matches that would start[39;49;00m$
[33mbefore LIMIT.[39;49;00m$
[33m[39;49;00m$
[33mIf GREEDY is non-nil, extend the match backwards as far as[39;49;00m$
[33mpossible, stopping when a single additional previous character[39;49;00m$
[33mcannot be part of a match for REGEXP.  When the match is[39;49;00m$
[33mextended, its starting position is allowed to occur before[39;49;00m$
[33mLIMIT.[39;49;00m$
[33m[39;49;00m$
[33mAs a general recommendation, try to avoid using [39;49;00m[33m`looking-back'[39;49;00m[33m[39;49;00m$
[33mwherever possible, since it is slow.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mstart[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m))[37m[39;49;00m$
[37m^I[39;49;00m([31mpos[39;49;00m[37m[39;49;00m$
[37m^I [39;49;00m([34msave-excursion[39;49;00m[37m[39;49;00m$
[37m^I   [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mre-search-backward[39;49;00m[37m [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m(?:[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mregexp[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m)[39;49;00m[33m\\[39;49;00m[33m=[39;49;00m[33m"[39;49;00m)[37m [39;49;00m[31mlimit[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
[37m^I^I[39;49;00m([32mpoint[39;49;00m)))))[37m[39;49;00m$
[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mgreedy[39;49;00m[37m [39;49;00m[31mpos[39;49;00m)[37m[39;49;00m$
[37m^I[39;49;00m([34msave-restriction[39;49;00m[37m[39;49;00m$
[37m^I  [39;49;00m([32mnarrow-to-region[39;49;00m[37m [39;49;00m([32mpoint-min[39;49;00m)[37m [39;49;00m[31mstart[39;49;00m)[37m[39;49;00m$
[37m^I  [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m[31mpos[39;49;00m[37m [39;49;00m([32mpoint-min[39;49;00m))[37m[39;49;00m$
[37m^I^I      [39;49;00m([34msave-excursion[39;49;00m[37m[39;49;00m$
[37m^I^I^I[39;49;00m([32mgoto-char[39;49;00m[37m [39;49;00m[31mpos[39;49;00m)[37m[39;49;00m$
[37m^I^I^I[39;49;00m([32mbackward-char[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m[39;49;00m$
[37m^I^I^I[39;49;00m([32mlooking-at[39;49;00m[37m [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m(?:[39;49;00m[33m"[39;49;00m[37m  [39;49;00m[31mregexp[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m)[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m[33m"[39;49;00m))))[37m[39;49;00m$
[37m^I    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mpos[39;49;00m[37m [39;49;00m([32m1-[39;49;00m[37m [39;49;00m[31mpos[39;49;00m)))[37m[39;49;00m$
[37m^I  [39;49;00m([34msave-excursion[39;49;00m[37m[39;49;00m$
[37m^I    [39;49;00m([32mgoto-char[39;49;00m[37m [39;49;00m[31mpos[39;49;00m)[37m[39;49;00m$
[37m^I    [39;49;00m([32mlooking-at[39;49;00m[37m [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m(?:[39;49;00m[33m"[39;49;00m[37m  [39;49;00m[31mregexp[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m)[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m[33m"[39;49;00m)))))[37m[39;49;00m$
[37m    [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[31mpos[39;49;00m))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefsubst[39;49;00m[37m [39;49;00m[31mlooking-at-p[39;49;00m[37m [39;49;00m([31mregexp[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33m\[39;49;00m$
[33mSame as [39;49;00m[33m`looking-at'[39;49;00m[33m except this function does not change the match data.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31minhibit-changing-match-data[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
[37m    [39;49;00m([32mlooking-at[39;49;00m[37m [39;49;00m[31mregexp[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefsubst[39;49;00m[37m [39;49;00m[31mstring-match-p[39;49;00m[37m [39;49;00m([31mregexp[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mstart[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33m\[39;49;00m$
[33mSame as [39;49;00m[33m`string-match'[39;49;00m[33m except this function does not change the match data.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31minhibit-changing-match-data[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
[37m    [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[31mregexp[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[31mstart[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31msubregexp-context-p[39;49;00m[37m [39;49;00m([31mregexp[39;49;00m[37m [39;49;00m[31mpos[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mstart[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn non-nil if POS is in a normal subregexp context in REGEXP.[39;49;00m$
[33mA subregexp context is one where a sub-regexp can appear.[39;49;00m$
[33mA non-subregexp context is for example within brackets, or within a[39;49;00m$
[33mrepetition bounds operator [39;49;00m[33m`\\=\\{...\\}'[39;49;00m[33m, or right after a [39;49;00m[33m`\\'[39;49;00m[33m.[39;49;00m$
[33mIf START is non-nil, it should be a position in REGEXP, smaller[39;49;00m$
[33mthan POS, and known to be in a subregexp context.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; Here's one possible implementation, with the great benefit that it[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; reuses the regexp-matcher's own parser, so it understands all the[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; details of the syntax.  A disadvantage is that it needs to match the[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; error string.[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mcondition-case[39;49;00m[37m [39;49;00m[31merr[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([34mprogn[39;49;00m[37m[39;49;00m$
[37m        [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[31mregexp[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[31mpos[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m        [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([31minvalid-regexp[39;49;00m[37m[39;49;00m$
[37m     [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mmember[39;49;00m[37m [39;49;00m([31mcadr[39;49;00m[37m [39;49;00m[31merr[39;49;00m)[37m [39;49;00m'([33m"[39;49;00m[33mUnmatched [ or [^[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m                               [39;49;00m[33m"[39;49;00m[33mUnmatched [39;49;00m[33m\\[39;49;00m[33m{[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m                               [39;49;00m[33m"[39;49;00m[33mTrailing backslash[39;49;00m[33m"[39;49;00m)))))[37m[39;49;00m$
[37m  [39;49;00m[37m;; An alternative implementation:[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; (defconst re-context-re[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;;   (let* ((harmless-ch "[^\\[]")[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;;          (harmless-esc "\\\\[^{]")[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;;          (class-harmless-ch "[^][]")[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;;          (class-lb-harmless "[^]:]")[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;;          (class-lb-colon-maybe-charclass ":\\([a-z]+:]\\)?")[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;;          (class-lb (concat "\\[\\(" class-lb-harmless[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;;                            "\\|" class-lb-colon-maybe-charclass "\\)"))[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;;          (class[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;;           (concat "\\[^?]?"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;;                   "\\(" class-harmless-ch[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;;                   "\\|" class-lb "\\)*"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;;                   "\\[?]"))     ; special handling for bare [ at end of re[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;;          (braces "\\\\{[0-9,]+\\\\}"))[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;;     (concat "\\`\\(" harmless-ch "\\|" harmless-esc[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;;             "\\|" class "\\|" braces "\\)*\\'"))[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;;   "Matches any prefix that corresponds to a normal subregexp context.")[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; (string-match re-context-re (substring regexp (or start 0) pos))[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m)[37m[39;49;00m$
[37m[39;49;00m[37m[39;49;00m$
[37m;;;; split-string[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
([34mdefconst[39;49;00m[37m [39;49;00m[31msplit-string-default-separators[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m[ [39;49;00m[33m\f[39;49;00m[33m\t[39;49;00m[33m\n[39;49;00m[33m\r[39;49;00m[33m\v[39;49;00m[33m]+[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mThe default value of separators for [39;49;00m[33m`split-string'[39;49;00m[33m.[39;49;00m$
[33m[39;49;00m$
[33mA regexp matching strings of whitespace.  May be locale-dependent[39;49;00m$
[33m\([39;49;00m[33mas yet unimplemented).  Should not match non-breaking spaces.[39;49;00m$
[33m[39;49;00m$
[33mWarning: binding this to a different value and using it as default is[39;49;00m$
[33mlikely to have undesired semantics.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
[37m;; The specification says that if both SEPARATORS and OMIT-NULLS are[39;49;00m[37m[39;49;00m$
[37m;; defaulted, OMIT-NULLS should be treated as t.  Simplifying the logical[39;49;00m[37m[39;49;00m$
[37m;; expression leads to the equivalent implementation that if SEPARATORS[39;49;00m[37m[39;49;00m$
[37m;; is defaulted, OMIT-NULLS is treated as t.[39;49;00m[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31msplit-string[39;49;00m[37m [39;49;00m([32mstring[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mseparators[39;49;00m[37m [39;49;00m[31momit-nulls[39;49;00m[37m [39;49;00m[31mtrim[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mSplit STRING into substrings bounded by matches for SEPARATORS.[39;49;00m$
[33m[39;49;00m$
[33mThe beginning and end of STRING, and each match for SEPARATORS, are[39;49;00m$
[33msplitting points.  The substrings matching SEPARATORS are removed, and[39;49;00m$
[33mthe substrings between the splitting points are collected as a list,[39;49;00m$
[33mwhich is returned.[39;49;00m$
[33m[39;49;00m$
[33mIf SEPARATORS is non-nil, it should be a regular expression matching text[39;49;00m$
[33mwhich separates, but is not part of, the substrings.  If nil it defaults to[39;49;00m$
[33m`split-string-default-separators'[39;49;00m[33m, normally [39;49;00m[33m\"[39;49;00m[33m[ [39;49;00m[33m\\[39;49;00m[33mf[39;49;00m[33m\\[39;49;00m[33mt[39;49;00m[33m\\[39;49;00m[33mn[39;49;00m[33m\\[39;49;00m[33mr[39;49;00m[33m\\[39;49;00m[33mv]+[39;49;00m[33m\"[39;49;00m[33m, and[39;49;00m$
[33mOMIT-NULLS is forced to t.[39;49;00m$
[33m[39;49;00m$
[33mIf OMIT-NULLS is t, zero-length substrings are omitted from the list (so[39;49;00m$
[33mthat for the default value of SEPARATORS leading and trailing whitespace[39;49;00m$
[33mare effectively trimmed).  If nil, all zero-length substrings are retained,[39;49;00m$
[33mwhich correctly parses CSV format, for example.[39;49;00m$
[33m[39;49;00m$
[33mIf TRIM is non-nil, it should be a regular expression to match[39;49;00m$
[33mtext to trim from the beginning and end of each substring.  If trimming[39;49;00m$
[33mmakes the substring empty, it is treated as null.[39;49;00m$
[33m[39;49;00m$
[33mIf you want to trim whitespace from the substrings, the reliably correct[39;49;00m$
[33mway is using TRIM.  Making SEPARATORS match that whitespace gives incorrect[39;49;00m$
[33mresults when there is whitespace at the start or end of STRING.  If you[39;49;00m$
[33msee such calls to [39;49;00m[33m`split-string'[39;49;00m[33m, please fix them.[39;49;00m$
[33m[39;49;00m$
[33mNote that the effect of [39;49;00m[33m`[39;49;00m[33m(split-string STRING)' is the same as[39;49;00m$
[33m`[39;49;00m[33m(split-string STRING split-string-default-separators t)'.  In the rare[39;49;00m$
[33mcase that you wish to retain zero-length substrings when splitting on[39;49;00m$
[33mwhitespace, use [39;49;00m[33m`[39;49;00m[33m(split-string STRING split-string-default-separators)'.[39;49;00m$
[33m[39;49;00m$
[33mModifies the match data; use [39;49;00m[33m`save-match-data'[39;49;00m[33m if necessary.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mkeep-nulls[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mseparators[39;49;00m[37m [39;49;00m[31momit-nulls[39;49;00m[37m [39;49;00m[31mt[39;49;00m)))[37m[39;49;00m$
[37m^I [39;49;00m([31mrexp[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mseparators[39;49;00m[37m [39;49;00m[31msplit-string-default-separators[39;49;00m))[37m[39;49;00m$
[37m^I [39;49;00m([31mstart[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m^I [39;49;00m[31mthis-start[39;49;00m[37m [39;49;00m[31mthis-end[39;49;00m[37m[39;49;00m$
[37m^I [39;49;00m[31mnotfirst[39;49;00m[37m[39;49;00m$
[37m^I [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
[37m^I [39;49;00m([31mpush-one[39;49;00m[37m[39;49;00m$
[37m^I  [39;49;00m[37m;; Push the substring in range THIS-START to THIS-END[39;49;00m[37m[39;49;00m$
[37m^I  [39;49;00m[37m;; onto LIST, trimming it and perhaps discarding it.[39;49;00m[37m[39;49;00m$
[37m^I  [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m()[37m[39;49;00m$
[37m^I    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31mtrim[39;49;00m[37m[39;49;00m$
[37m^I      [39;49;00m[37m;; Discard the trim from start of this substring.[39;49;00m[37m[39;49;00m$
[37m^I      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtem[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[31mtrim[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[31mthis-start[39;49;00m)))[37m[39;49;00m$
[37m^I^I[39;49;00m([34mand[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mtem[39;49;00m[37m [39;49;00m[31mthis-start[39;49;00m)[37m[39;49;00m$
[37m^I^I     [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mthis-start[39;49;00m[37m [39;49;00m([32mmatch-end[39;49;00m[37m [39;49;00m[34m0[39;49;00m)))))[37m[39;49;00m$
[37m[39;49;00m$
[37m^I    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mkeep-nulls[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m[31mthis-start[39;49;00m[37m [39;49;00m[31mthis-end[39;49;00m))[37m[39;49;00m$
[37m^I      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mthis[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[31mthis-start[39;49;00m[37m [39;49;00m[31mthis-end[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[37m;; Discard the trim from end of this substring.[39;49;00m[37m[39;49;00m$
[37m^I^I[39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31mtrim[39;49;00m[37m[39;49;00m$
[37m^I^I  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtem[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[31mtrim[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m[33m"[39;49;00m)[37m [39;49;00m[31mthis[39;49;00m[37m [39;49;00m[34m0[39;49;00m)))[37m[39;49;00m$
[37m^I^I    [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mtem[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m[31mtem[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31mthis[39;49;00m))[37m[39;49;00m$
[37m^I^I^I [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mthis[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[31mthis[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[31mtem[39;49;00m)))))[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[37m;; Trimming could make it empty; check again.[39;49;00m[37m[39;49;00m$
[37m^I^I[39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mkeep-nulls[39;49;00m[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31mthis[39;49;00m)[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m$
[37m^I^I  [39;49;00m([36mpush[39;49;00m[37m [39;49;00m[31mthis[39;49;00m[37m [39;49;00m[32mlist[39;49;00m)))))))[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[31mrexp[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m[39;49;00m$
[37m^I^I^I      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mnotfirst[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I       [39;49;00m([32m=[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m([32mmatch-beginning[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m$
[37m^I^I^I^I       [39;49;00m([32m<[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[32mstring[39;49;00m)))[37m[39;49;00m$
[37m^I^I^I^I  [39;49;00m([32m1+[39;49;00m[37m [39;49;00m[31mstart[39;49;00m)[37m [39;49;00m[31mstart[39;49;00m))[37m[39;49;00m$
[37m^I^I[39;49;00m([32m<[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[32mstring[39;49;00m)))[37m[39;49;00m$
[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mnotfirst[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mthis-start[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mthis-end[39;49;00m[37m [39;49;00m([32mmatch-beginning[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m^I    [39;49;00m[31mstart[39;49;00m[37m [39;49;00m([32mmatch-end[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
[37m      [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mpush-one[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[37m;; Handle the substring at the end of STRING.[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mthis-start[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mthis-end[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[32mstring[39;49;00m))[37m[39;49;00m$
[37m    [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mpush-one[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m([32mnreverse[39;49;00m[37m [39;49;00m[32mlist[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mcombine-and-quote-strings[39;49;00m[37m [39;49;00m([31mstrings[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mseparator[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mConcatenate the STRINGS, adding the SEPARATOR (default [39;49;00m[33m\"[39;49;00m[33m [39;49;00m[33m\"[39;49;00m[33m).[39;49;00m$
[33mThis tries to quote the strings to avoid ambiguity such that[39;49;00m$
[33m  (split-string-and-unquote (combine-and-quote-strings strs)) == strs[39;49;00m$
[33mOnly some SEPARATORs will work properly.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31msep[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mseparator[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
[37m         [39;49;00m([31mre[39;49;00m[37m [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m[[39;49;00m[33m\\[39;49;00m[33m\"[39;49;00m[33m][39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m|[39;49;00m[33m"[39;49;00m[37m [39;49;00m([32mregexp-quote[39;49;00m[37m [39;49;00m[31msep[39;49;00m))))[37m[39;49;00m$
[37m    [39;49;00m([32mmapconcat[39;49;00m[37m[39;49;00m$
[37m     [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31mstr[39;49;00m)[37m[39;49;00m$
[37m       [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[31mre[39;49;00m[37m [39;49;00m[31mstr[39;49;00m)[37m[39;49;00m$
[37m^I   [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m[37m [39;49;00m([31mreplace-regexp-in-string[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m[[39;49;00m[33m\\[39;49;00m[33m\"[39;49;00m[33m][39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m&[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mstr[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m^I [39;49;00m[31mstr[39;49;00m))[37m[39;49;00m$
[37m     [39;49;00m[31mstrings[39;49;00m[37m [39;49;00m[31msep[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31msplit-string-and-unquote[39;49;00m[37m [39;49;00m([32mstring[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mseparator[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mSplit the STRING into a list of strings.[39;49;00m$
[33mIt understands Emacs Lisp quoting within STRING, such that[39;49;00m$
[33m  (split-string-and-unquote (combine-and-quote-strings strs)) == strs[39;49;00m$
[33mThe SEPARATOR regexp defaults to [39;49;00m[33m\"[39;49;00m[33m\\[39;49;00m[33ms-+[39;49;00m[33m\"[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31msep[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mseparator[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33ms-+[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
[37m^I[39;49;00m([31mi[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m[37m [39;49;00m[32mstring[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[31mi[39;49;00m)[37m[39;49;00m$
[37m^I[39;49;00m([31msplit-string[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[31msep[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m^I[39;49;00m[37m; no quoting:  easy[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([32mappend[39;49;00m[37m [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mi[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m([31msplit-string[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[31mi[39;49;00m)[37m [39;49;00m[31msep[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
[37m^I      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mrfs[39;49;00m[37m [39;49;00m([32mread-from-string[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[31mi[39;49;00m)))[37m[39;49;00m$
[37m^I^I[39;49;00m([32mcons[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mrfs[39;49;00m)[37m[39;49;00m$
[37m^I^I      [39;49;00m([31msplit-string-and-unquote[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mrfs[39;49;00m))[37m[39;49;00m$
[37m^I^I^I^I^I^I[39;49;00m[31msep[39;49;00m)))))))[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m[37m[39;49;00m$
[37m;;;; Replacement in strings.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31msubst-char-in-string[39;49;00m[37m [39;49;00m([31mfromchar[39;49;00m[37m [39;49;00m[31mtochar[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31minplace[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReplace FROMCHAR with TOCHAR in STRING each time it occurs.[39;49;00m$
[33mUnless optional argument INPLACE is non-nil, return a new string.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mi[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[32mstring[39;49;00m))[37m[39;49;00m$
[37m^I[39;49;00m([31mnewstr[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31minplace[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m([32mcopy-sequence[39;49;00m[37m [39;49;00m[32mstring[39;49;00m))))[37m[39;49;00m$
[37m    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m[31mi[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mi[39;49;00m[37m [39;49;00m([32m1-[39;49;00m[37m [39;49;00m[31mi[39;49;00m))[37m[39;49;00m$
[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32maref[39;49;00m[37m [39;49;00m[31mnewstr[39;49;00m[37m [39;49;00m[31mi[39;49;00m)[37m [39;49;00m[31mfromchar[39;49;00m)[37m[39;49;00m$
[37m^I  [39;49;00m([32maset[39;49;00m[37m [39;49;00m[31mnewstr[39;49;00m[37m [39;49;00m[31mi[39;49;00m[37m [39;49;00m[31mtochar[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m[31mnewstr[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mreplace-regexp-in-string[39;49;00m[37m [39;49;00m([31mregexp[39;49;00m[37m [39;49;00m[31mrep[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m[31mfixedcase[39;49;00m[37m [39;49;00m[31mliteral[39;49;00m[37m [39;49;00m[31msubexp[39;49;00m[37m [39;49;00m[31mstart[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReplace all matches for REGEXP with REP in STRING.[39;49;00m$
[33m[39;49;00m$
[33mReturn a new string containing the replacements.[39;49;00m$
[33m[39;49;00m$
[33mOptional arguments FIXEDCASE, LITERAL and SUBEXP are like the[39;49;00m$
[33marguments with the same names of function [39;49;00m[33m`replace-match'[39;49;00m[33m.  If START[39;49;00m$
[33mis non-nil, start replacements at that index in STRING.[39;49;00m$
[33m[39;49;00m$
[33mREP is either a string used as the NEWTEXT arg of [39;49;00m[33m`replace-match'[39;49;00m[33m or a[39;49;00m$
[33mfunction.  If it is a function, it is called with the actual text of each[39;49;00m$
[33mmatch, and its value is used as the replacement text.  When REP is called,[39;49;00m$
[33mthe match data are the result of matching REGEXP against a substring[39;49;00m$
[33mof STRING.[39;49;00m$
[33m[39;49;00m$
[33mTo replace only the first match (if any), make REGEXP match up to [39;49;00m[33m\\[39;49;00m[33m'[39;49;00m$
[33mand replace a sub-expression, e.g.[39;49;00m$
[33m  (replace-regexp-in-string [39;49;00m[33m\"[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m(foo[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m).*[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m[33m\"[39;49;00m[33m [39;49;00m[33m\"[39;49;00m[33mbar[39;49;00m[33m\"[39;49;00m[33m [39;49;00m[33m\"[39;49;00m[33m foo foo[39;49;00m[33m\"[39;49;00m[33m nil nil 1)[39;49;00m$
[33m    => [39;49;00m[33m\"[39;49;00m[33m bar foo[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m  [39;49;00m[37m;; To avoid excessive consing from multiple matches in long strings,[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; don't just call `replace-match' continually.  Walk down the[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; string looking for matches of REGEXP and building up a (reversed)[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; list MATCHES.  This comprises segments of STRING which weren't[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; matched interspersed with replacements for segments that were.[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; [For a `large' number of replacements it's more efficient to[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; operate in a temporary buffer; we can't tell from the function's[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; args whether to choose the buffer-based implementation, though it[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; might be reasonable to do so for long enough STRING.][39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31ml[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[32mstring[39;49;00m))[37m[39;49;00m$
[37m^I[39;49;00m([31mstart[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m$
[37m^I[39;49;00m[31mmatches[39;49;00m[37m [39;49;00m[31mstr[39;49;00m[37m [39;49;00m[31mmb[39;49;00m[37m [39;49;00m[31mme[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([36msave-match-data[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31ml[39;49;00m)[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[31mregexp[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[31mstart[39;49;00m))[37m[39;49;00m$
[37m^I[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mmb[39;49;00m[37m [39;49;00m([32mmatch-beginning[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m^I      [39;49;00m[31mme[39;49;00m[37m [39;49;00m([32mmatch-end[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m$
[37m^I[39;49;00m[37m;; If we matched the empty string, make sure we advance by one char[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32m=[39;49;00m[37m [39;49;00m[31mme[39;49;00m[37m [39;49;00m[31mmb[39;49;00m)[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mme[39;49;00m[37m [39;49;00m([32mmin[39;49;00m[37m [39;49;00m[31ml[39;49;00m[37m [39;49;00m([32m1+[39;49;00m[37m [39;49;00m[31mmb[39;49;00m))))[37m[39;49;00m$
[37m^I[39;49;00m[37m;; Generate a replacement for the matched substring.[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00m[37m;; Operate only on the substring to minimize string consing.[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00m[37m;; Set up match data for the substring for replacement;[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00m[37m;; presumably this is likely to be faster than munging the[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00m[37m;; match data directly in Lisp.[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[31mregexp[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mstr[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[31mmb[39;49;00m[37m [39;49;00m[31mme[39;49;00m)))[37m[39;49;00m$
[37m^I[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mmatches[39;49;00m[37m[39;49;00m$
[37m^I      [39;49;00m([32mcons[39;49;00m[37m [39;49;00m([32mreplace-match[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m[31mrep[39;49;00m)[37m[39;49;00m$
[37m^I^I^I^I       [39;49;00m[31mrep[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I     [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mrep[39;49;00m[37m [39;49;00m([31mmatch-string[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[31mstr[39;49;00m)))[37m[39;49;00m$
[37m^I^I^I^I   [39;49;00m[31mfixedcase[39;49;00m[37m [39;49;00m[31mliteral[39;49;00m[37m [39;49;00m[31mstr[39;49;00m[37m [39;49;00m[31msubexp[39;49;00m)[37m[39;49;00m$
[37m^I^I    [39;49;00m([32mcons[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mmb[39;49;00m)[37m [39;49;00m[37m; unmatched prefix[39;49;00m[37m[39;49;00m$
[37m^I^I^I  [39;49;00m[31mmatches[39;49;00m)))[37m[39;49;00m$
[37m^I[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mme[39;49;00m))[37m[39;49;00m$
[37m      [39;49;00m[37m;; Reconstruct a string from the pieces.[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mmatches[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31ml[39;49;00m)[37m [39;49;00m[31mmatches[39;49;00m))[37m [39;49;00m[37m; leftover[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([32mapply[39;49;00m[37m [39;49;00m[32m#'[39;49;00m[32mconcat[39;49;00m[37m [39;49;00m([32mnreverse[39;49;00m[37m [39;49;00m[31mmatches[39;49;00m)))))[37m[39;49;00m$
[37m[39;49;00m[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mstring-prefix-p[39;49;00m[37m [39;49;00m([31mprefix[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mignore-case[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn non-nil if PREFIX is a prefix of STRING.[39;49;00m$
[33mIf IGNORE-CASE is non-nil, the comparison is done without paying attention[39;49;00m$
[33mto case differences.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mprefix-length[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31mprefix[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m[31mprefix-length[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[32mstring[39;49;00m))[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m([32mcompare-strings[39;49;00m[37m [39;49;00m[31mprefix[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[31mprefix-length[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m[39;49;00m$
[37m^I^I^I     [39;49;00m[34m0[39;49;00m[37m [39;49;00m[31mprefix-length[39;49;00m[37m [39;49;00m[31mignore-case[39;49;00m)))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mstring-suffix-p[39;49;00m[37m [39;49;00m([31msuffix[39;49;00m[37m [39;49;00m[32mstring[39;49;00m[37m  [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mignore-case[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn non-nil if SUFFIX is a suffix of STRING.[39;49;00m$
[33mIf IGNORE-CASE is non-nil, the comparison is done without paying[39;49;00m$
[33mattention to case differences.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mstart-pos[39;49;00m[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[32mstring[39;49;00m)[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31msuffix[39;49;00m))))[37m[39;49;00m$
[37m    [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32m>=[39;49;00m[37m [39;49;00m[31mstart-pos[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m         [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m([32mcompare-strings[39;49;00m[37m [39;49;00m[31msuffix[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m$
[37m                                [39;49;00m[32mstring[39;49;00m[37m [39;49;00m[31mstart-pos[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mignore-case[39;49;00m)))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mbidi-string-mark-left-to-right[39;49;00m[37m [39;49;00m([31mstr[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn a string that can be safely inserted in left-to-right text.[39;49;00m$
[33m[39;49;00m$
[33mNormally, inserting a string with right-to-left (RTL) script into[39;49;00m$
[33ma buffer may cause some subsequent text to be displayed as part[39;49;00m$
[33mof the RTL segment (usually this affects punctuation characters).[39;49;00m$
[33mThis function returns a string which displays as STR but forces[39;49;00m$
[33msubsequent text to be displayed as left-to-right.[39;49;00m$
[33m[39;49;00m$
[33mIf STR contains any RTL character, this function returns a string[39;49;00m$
[33mconsisting of STR followed by an invisible left-to-right mark[39;49;00m$
[33m\([39;49;00m[33mLRM) character.  Otherwise, it returns STR.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m[31mstr[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([32msignal[39;49;00m[37m [39;49;00m[33m'wrong-type-argument[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[33m'stringp[39;49;00m[37m [39;49;00m[31mstr[39;49;00m)))[37m[39;49;00m$
[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33mcR[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mstr[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[31mstr[39;49;00m[37m [39;49;00m([32mpropertize[39;49;00m[37m [39;49;00m([32mstring[39;49;00m[37m [39;49;00m[33m?\x[39;49;00m[31m200e[39;49;00m)[37m [39;49;00m[33m'invisible[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
[37m    [39;49;00m[31mstr[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m[37m[39;49;00m$
[37m;;;; Specifying things to do later.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mload-history-regexp[39;49;00m[37m [39;49;00m([31mfile[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mForm a regexp to find FILE in [39;49;00m[33m`load-history'[39;49;00m[33m.[39;49;00m$
[33mFILE, a string, is described in the function [39;49;00m[33m`eval-after-load'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mfile-name-absolute-p[39;49;00m[37m [39;49;00m[31mfile[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mfile[39;49;00m[37m [39;49;00m([31mfile-truename[39;49;00m[37m [39;49;00m[31mfile[39;49;00m)))[37m[39;49;00m$
[37m  [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mfile-name-absolute-p[39;49;00m[37m [39;49;00m[31mfile[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m`[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m([39;49;00m[33m\\[39;49;00m[33m`[39;49;00m[33m\\[39;49;00m[33m|/[39;49;00m[33m\\[39;49;00m[33m)[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m^I  [39;49;00m([32mregexp-quote[39;49;00m[37m [39;49;00m[31mfile[39;49;00m)[37m[39;49;00m$
[37m^I  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([31mfile-name-extension[39;49;00m[37m [39;49;00m[31mfile[39;49;00m)[37m[39;49;00m$
[37m^I      [39;49;00m[33m"[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m^I    [39;49;00m[37m;; Note: regexp-opt can't be used here, since we need to call[39;49;00m[37m[39;49;00m$
[37m^I    [39;49;00m[37m;; this before Emacs has been fully started.  2006-05-21[39;49;00m[37m[39;49;00m$
[37m^I    [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m([39;49;00m[33m"[39;49;00m[37m [39;49;00m([32mmapconcat[39;49;00m[37m [39;49;00m[33m'regexp-quote[39;49;00m[37m [39;49;00m[31mload-suffixes[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m|[39;49;00m[33m"[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m)?[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
[37m^I  [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m([39;49;00m[33m"[39;49;00m[37m [39;49;00m([32mmapconcat[39;49;00m[37m [39;49;00m[33m'regexp-quote[39;49;00m[37m [39;49;00m[31mjka-compr-load-suffixes[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m|[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m^I  [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m)?[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mload-history-filename-element[39;49;00m[37m [39;49;00m([31mfile-regexp[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mGet the first elt of [39;49;00m[33m`load-history'[39;49;00m[33m whose car matches FILE-REGEXP.[39;49;00m$
[33mReturn nil if there isn't one.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mloads[39;49;00m[37m [39;49;00m[31mload-history[39;49;00m)[37m[39;49;00m$
[37m^I [39;49;00m([31mload-elt[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mloads[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mloads[39;49;00m))))[37m[39;49;00m$
[37m    [39;49;00m([36msave-match-data[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mloads[39;49;00m[37m[39;49;00m$
[37m^I^I  [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mload-elt[39;49;00m))[37m[39;49;00m$
[37m^I^I      [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[31mfile-regexp[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mload-elt[39;49;00m)))))[37m[39;49;00m$
[37m^I[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mloads[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mloads[39;49;00m)[37m[39;49;00m$
[37m^I      [39;49;00m[31mload-elt[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mloads[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mloads[39;49;00m)))))[37m[39;49;00m$
[37m    [39;49;00m[31mload-elt[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
([32mput[39;49;00m[37m [39;49;00m[33m'eval-after-load[39;49;00m[37m [39;49;00m[33m'lisp-indent-function[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31meval-after-load[39;49;00m[37m [39;49;00m([31mfile[39;49;00m[37m [39;49;00m[31mform[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mArrange that if FILE is loaded, FORM will be run immediately afterwards.[39;49;00m$
[33mIf FILE is already loaded, evaluate FORM right now.[39;49;00m$
[33mFORM can be an Elisp expression (in which case it's passed to [39;49;00m[33m`eval'[39;49;00m[33m),[39;49;00m$
[33mor a function (in which case it's passed to [39;49;00m[33m`funcall'[39;49;00m[33m with no argument).[39;49;00m$
[33m[39;49;00m$
[33mIf a matching file is loaded again, FORM will be evaluated again.[39;49;00m$
[33m[39;49;00m$
[33mIf FILE is a string, it may be either an absolute or a relative file[39;49;00m$
[33mname, and may have an extension (e.g. [39;49;00m[33m\"[39;49;00m[33m.el[39;49;00m[33m\"[39;49;00m[33m) or may lack one, and[39;49;00m$
[33madditionally may or may not have an extension denoting a compressed[39;49;00m$
[33mformat (e.g. [39;49;00m[33m\"[39;49;00m[33m.gz[39;49;00m[33m\"[39;49;00m[33m).[39;49;00m$
[33m[39;49;00m$
[33mWhen FILE is absolute, this first converts it to a true name by chasing[39;49;00m$
[33msymbolic links.  Only a file of this name (see next paragraph regarding[39;49;00m$
[33mextensions) will trigger the evaluation of FORM.  When FILE is relative,[39;49;00m$
[33ma file whose absolute true name ends in FILE will trigger evaluation.[39;49;00m$
[33m[39;49;00m$
[33mWhen FILE lacks an extension, a file name with any extension will trigger[39;49;00m$
[33mevaluation.  Otherwise, its extension must match FILE's.  A further[39;49;00m$
[33mextension for a compressed format (e.g. [39;49;00m[33m\"[39;49;00m[33m.gz[39;49;00m[33m\"[39;49;00m[33m) on FILE will not affect[39;49;00m$
[33mthis name matching.[39;49;00m$
[33m[39;49;00m$
[33mAlternatively, FILE can be a feature (i.e. a symbol), in which case FORM[39;49;00m$
[33mis evaluated at the end of any file that [39;49;00m[33m`provide'[39;49;00m[33ms this feature.[39;49;00m$
[33mIf the feature is provided when evaluating code not associated with a[39;49;00m$
[33mfile, FORM is evaluated immediately after the provide statement.[39;49;00m$
[33m[39;49;00m$
[33mUsually FILE is just a library name like [39;49;00m[33m\"[39;49;00m[33mfont-lock[39;49;00m[33m\"[39;49;00m[33m or a feature name[39;49;00m$
[33mlike 'font-lock.[39;49;00m$
[33m[39;49;00m$
[33mThis function makes or adds to an entry on [39;49;00m[33m`after-load-alist'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mcompiler-macro[39;49;00m[37m[39;49;00m$
[37m            [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31mwhole[39;49;00m)[37m[39;49;00m$
[37m              [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[33m'quote[39;49;00m[37m [39;49;00m([32mcar-safe[39;49;00m[37m [39;49;00m[31mform[39;49;00m))[37m[39;49;00m$
[37m                  [39;49;00m[37m;; Quote with lambda so the compiler can look inside.[39;49;00m[37m[39;49;00m$
[37m                  [39;49;00m`([31meval-after-load[39;49;00m[37m [39;49;00m,[31mfile[39;49;00m[37m [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m()[37m [39;49;00m,([32mnth[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mform[39;49;00m)))[37m[39;49;00m$
[37m                [39;49;00m[31mwhole[39;49;00m))))[37m[39;49;00m$
[37m  [39;49;00m[37m;; Add this FORM into after-load-alist (regardless of whether we'll be[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; evaluating it now).[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mregexp-or-feature[39;49;00m[37m[39;49;00m$
[37m^I  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m[31mfile[39;49;00m)[37m[39;49;00m$
[37m              [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mfile[39;49;00m[37m [39;49;00m([32mpurecopy[39;49;00m[37m [39;49;00m([31mload-history-regexp[39;49;00m[37m [39;49;00m[31mfile[39;49;00m)))[37m[39;49;00m$
[37m            [39;49;00m[31mfile[39;49;00m))[37m[39;49;00m$
[37m^I [39;49;00m([32melt[39;49;00m[37m [39;49;00m([32massoc[39;49;00m[37m [39;49;00m[31mregexp-or-feature[39;49;00m[37m [39;49;00m[31mafter-load-alist[39;49;00m))[37m[39;49;00m$
[37m         [39;49;00m([31mfunc[39;49;00m[37m[39;49;00m$
[37m          [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mfunctionp[39;49;00m[37m [39;49;00m[31mform[39;49;00m)[37m [39;49;00m[31mform[39;49;00m[37m[39;49;00m$
[37m            [39;49;00m[37m;; Try to use the "current" lexical/dynamic mode for `form'.[39;49;00m[37m[39;49;00m$
[37m            [39;49;00m([32meval[39;49;00m[37m [39;49;00m`([36mlambda[39;49;00m[37m [39;49;00m()[37m [39;49;00m,[31mform[39;49;00m)[37m [39;49;00m[31mlexical-binding[39;49;00m))))[37m[39;49;00m$
[37m    [39;49;00m([36munless[39;49;00m[37m [39;49;00m[32melt[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[32melt[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[31mregexp-or-feature[39;49;00m))[37m[39;49;00m$
[37m      [39;49;00m([36mpush[39;49;00m[37m [39;49;00m[32melt[39;49;00m[37m [39;49;00m[31mafter-load-alist[39;49;00m))[37m[39;49;00m$
[37m    [39;49;00m[37m;; Is there an already loaded file whose name (or `provide' name)[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[37m;; matches FILE?[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m([34mprog1[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m[31mfile[39;49;00m)[37m[39;49;00m$
[37m^I^I   [39;49;00m([31mload-history-filename-element[39;49;00m[37m [39;49;00m[31mregexp-or-feature[39;49;00m)[37m[39;49;00m$
[37m^I^I [39;49;00m([36mfeaturep[39;49;00m[37m [39;49;00m[31mfile[39;49;00m))[37m[39;49;00m$
[37m^I       [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mfunc[39;49;00m))[37m[39;49;00m$
[37m      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mdelayed-func[39;49;00m[37m[39;49;00m$
[37m             [39;49;00m([34mif[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32msymbolp[39;49;00m[37m [39;49;00m[31mregexp-or-feature[39;49;00m))[37m [39;49;00m[31mfunc[39;49;00m[37m[39;49;00m$
[37m               [39;49;00m[37m;; For features, the after-load-alist elements get run when[39;49;00m[37m[39;49;00m$
[37m               [39;49;00m[37m;; `provide' is called rather than at the end of the file.[39;49;00m[37m[39;49;00m$
[37m               [39;49;00m[37m;; So add an indirection to make sure that `func' is really run[39;49;00m[37m[39;49;00m$
[37m               [39;49;00m[37m;; "after-load" in case the provide call happens early.[39;49;00m[37m[39;49;00m$
[37m               [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m()[37m[39;49;00m$
[37m                 [39;49;00m([34mif[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m[31mload-file-name[39;49;00m)[37m[39;49;00m$
[37m                     [39;49;00m[37m;; Not being provided from a file, run func right now.[39;49;00m[37m[39;49;00m$
[37m                     [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mfunc[39;49;00m)[37m[39;49;00m$
[37m                   [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mlfn[39;49;00m[37m [39;49;00m[31mload-file-name[39;49;00m)[37m[39;49;00m$
[37m                         [39;49;00m[37m;; Don't use letrec, because equal (in[39;49;00m[37m[39;49;00m$
[37m                         [39;49;00m[37m;; add/remove-hook) would get trapped in a cycle.[39;49;00m[37m[39;49;00m$
[37m                         [39;49;00m([31mfun[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33meval-after-load-helper[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
[37m                     [39;49;00m([32mfset[39;49;00m[37m [39;49;00m[31mfun[39;49;00m[37m [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31mfile[39;49;00m)[37m[39;49;00m$
[37m                                 [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mequal[39;49;00m[37m [39;49;00m[31mfile[39;49;00m[37m [39;49;00m[31mlfn[39;49;00m)[37m[39;49;00m$
[37m                                   [39;49;00m([31mremove-hook[39;49;00m[37m [39;49;00m[33m'after-load-functions[39;49;00m[37m [39;49;00m[31mfun[39;49;00m)[37m[39;49;00m$
[37m                                   [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mfunc[39;49;00m))))[37m[39;49;00m$
[37m                     [39;49;00m([31madd-hook[39;49;00m[37m [39;49;00m[33m'after-load-functions[39;49;00m[37m [39;49;00m[31mfun[39;49;00m[37m [39;49;00m[33m'append[39;49;00m)))))))[37m[39;49;00m$
[37m        [39;49;00m[37m;; Add FORM to the element unless it's already there.[39;49;00m[37m[39;49;00m$
[37m        [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32mmember[39;49;00m[37m [39;49;00m[31mdelayed-func[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[32melt[39;49;00m))[37m[39;49;00m$
[37m          [39;49;00m([32mnconc[39;49;00m[37m [39;49;00m[32melt[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[31mdelayed-func[39;49;00m)))))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefmacro[39;49;00m[37m [39;49;00m[36mwith-eval-after-load[39;49;00m[37m [39;49;00m([31mfile[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mExecute BODY after FILE is loaded.[39;49;00m$
[33mFILE is normally a feature name, but it can also be a file name,[39;49;00m$
[33min case that file does not provide any feature.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m`([31meval-after-load[39;49;00m[37m [39;49;00m,[31mfile[39;49;00m[37m [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m()[37m [39;49;00m,@[31mbody[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
([34mdefvar[39;49;00m[37m [39;49;00m[31mafter-load-functions[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mSpecial hook run after loading a file.[39;49;00m$
[33mEach function there is called with a single argument, the absolute[39;49;00m$
[33mname of the file just loaded.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mdo-after-load-evaluation[39;49;00m[37m [39;49;00m([31mabs-file[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mEvaluate all [39;49;00m[33m`eval-after-load'[39;49;00m[33m forms, if any, for ABS-FILE.[39;49;00m$
[33mABS-FILE, a string, should be the absolute true name of a file just loaded.[39;49;00m$
[33mThis function is called directly from the C code.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; Run the relevant eval-after-load forms.[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdolist[39;49;00m[37m [39;49;00m([31ma-l-element[39;49;00m[37m [39;49;00m[31mafter-load-alist[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31ma-l-element[39;49;00m))[37m[39;49;00m$
[37m               [39;49;00m([31mstring-match-p[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31ma-l-element[39;49;00m)[37m [39;49;00m[31mabs-file[39;49;00m))[37m[39;49;00m$
[37m      [39;49;00m[37m;; discard the file name regexp[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([32mmapc[39;49;00m[37m [39;49;00m[32m#'[39;49;00m[32mfuncall[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31ma-l-element[39;49;00m))))[37m[39;49;00m$
[37m  [39;49;00m[37m;; Complain when the user uses obsolete files.[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([36msave-match-data[39;49;00m[37m[39;49;00m$
[37m          [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m/obsolete/[39;49;00m[33m\\[39;49;00m[33m([^/]*[39;49;00m[33m\\[39;49;00m[33m)[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mabs-file[39;49;00m)[37m[39;49;00m$
[37m               [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mequal[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mloaddefs.el[39;49;00m[33m"[39;49;00m[37m [39;49;00m([31mmatch-string[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mabs-file[39;49;00m)))))[37m[39;49;00m$
[37m    [39;49;00m[37m;; Maybe we should just use display-warning?  This seems yucky...[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mfile[39;49;00m[37m [39;49;00m([32mfile-name-nondirectory[39;49;00m[37m [39;49;00m[31mabs-file[39;49;00m))[37m[39;49;00m$
[37m^I   [39;49;00m([31mmsg[39;49;00m[37m [39;49;00m([32mformat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mPackage %s is obsolete![39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m^I^I^I[39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[31mfile[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I   [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m.elc?[39;49;00m[33m\\[39;49;00m[33m>[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mfile[39;49;00m)))))[37m[39;49;00m$
[37m      [39;49;00m[37m;; Cribbed from cl--compiling-file.[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mboundp[39;49;00m[37m [39;49;00m[33m'byte-compile--outbuffer[39;49;00m)[37m[39;49;00m$
[37m^I       [39;49;00m([32mbufferp[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[33m'byte-compile--outbuffer[39;49;00m))[37m[39;49;00m$
[37m^I       [39;49;00m([32mequal[39;49;00m[37m [39;49;00m([32mbuffer-name[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[33m'byte-compile--outbuffer[39;49;00m))[37m[39;49;00m$
[37m^I^I      [39;49;00m[33m"[39;49;00m[33m *Compiler Output*[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
[37m^I  [39;49;00m[37m;; Don't warn about obsolete files using other obsolete files.[39;49;00m[37m[39;49;00m$
[37m^I  [39;49;00m([36munless[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m[31mbyte-compile-current-file[39;49;00m)[37m[39;49;00m$
[37m^I^I       [39;49;00m([31mstring-match-p[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m/obsolete/[^/]*[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I       [39;49;00m([32mexpand-file-name[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m[31mbyte-compile-current-file[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m[31mbyte-compile-root-dir[39;49;00m)))[37m[39;49;00m$
[37m^I    [39;49;00m([31mbyte-compile-log-warning[39;49;00m[37m [39;49;00m[31mmsg[39;49;00m))[37m[39;49;00m$
[37m^I[39;49;00m([31mrun-with-timer[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m$
[37m^I^I^I[39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31mmsg[39;49;00m)[37m[39;49;00m$
[37m^I^I^I  [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m%s[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mmsg[39;49;00m))[37m[39;49;00m$
[37m                        [39;49;00m[31mmsg[39;49;00m))))[37m[39;49;00m$
[37m[39;49;00m$
[37m  [39;49;00m[37m;; Finally, run any other hook.[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([32mrun-hook-with-args[39;49;00m[37m [39;49;00m[33m'after-load-functions[39;49;00m[37m [39;49;00m[31mabs-file[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31meval-next-after-load[39;49;00m[37m [39;49;00m([31mfile[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mRead the following input sexp, and run it whenever FILE is loaded.[39;49;00m$
[33mThis makes or adds to an entry on [39;49;00m[33m`after-load-alist'[39;49;00m[33m.[39;49;00m$
[33mFILE should be the name of a library, with no directory name.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mobsolete[39;49;00m[37m [39;49;00m[31meval-after-load[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m([31meval-after-load[39;49;00m[37m [39;49;00m[31mfile[39;49;00m[37m [39;49;00m([32mread[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mdisplay-delayed-warnings[39;49;00m[37m [39;49;00m()[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mDisplay delayed warnings from [39;49;00m[33m`delayed-warnings-list'[39;49;00m[33m.[39;49;00m$
[33mUsed from [39;49;00m[33m`delayed-warnings-hook'[39;49;00m[33m (which see).[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdolist[39;49;00m[37m [39;49;00m([31mwarning[39;49;00m[37m [39;49;00m([32mnreverse[39;49;00m[37m [39;49;00m[31mdelayed-warnings-list[39;49;00m))[37m[39;49;00m$
[37m    [39;49;00m([32mapply[39;49;00m[37m [39;49;00m[33m'display-warning[39;49;00m[37m [39;49;00m[31mwarning[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mdelayed-warnings-list[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mcollapse-delayed-warnings[39;49;00m[37m [39;49;00m()[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mRemove duplicates from [39;49;00m[33m`delayed-warnings-list'[39;49;00m[33m.[39;49;00m$
[33mCollapse identical adjacent warnings into one (plus count).[39;49;00m$
[33mUsed from [39;49;00m[33m`delayed-warnings-hook'[39;49;00m[33m (which see).[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mcount[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m[39;49;00m$
[37m        [39;49;00m[31mcollapsed[39;49;00m[37m [39;49;00m[31mwarning[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m[31mdelayed-warnings-list[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mwarning[39;49;00m[37m [39;49;00m([36mpop[39;49;00m[37m [39;49;00m[31mdelayed-warnings-list[39;49;00m))[37m[39;49;00m$
[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mequal[39;49;00m[37m [39;49;00m[31mwarning[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mdelayed-warnings-list[39;49;00m))[37m[39;49;00m$
[37m          [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mcount[39;49;00m[37m [39;49;00m([32m1+[39;49;00m[37m [39;49;00m[31mcount[39;49;00m))[37m[39;49;00m$
[37m        [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m[31mcount[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m[39;49;00m$
[37m          [39;49;00m([32msetcdr[39;49;00m[37m [39;49;00m[31mwarning[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m([32mformat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m%s [%d times][39;49;00m[33m"[39;49;00m[37m [39;49;00m([31mcadr[39;49;00m[37m [39;49;00m[31mwarning[39;49;00m)[37m [39;49;00m[31mcount[39;49;00m)[37m[39;49;00m$
[37m                                [39;49;00m([31mcddr[39;49;00m[37m [39;49;00m[31mwarning[39;49;00m)))[37m[39;49;00m$
[37m          [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mcount[39;49;00m[37m [39;49;00m[34m1[39;49;00m))[37m[39;49;00m$
[37m        [39;49;00m([36mpush[39;49;00m[37m [39;49;00m[31mwarning[39;49;00m[37m [39;49;00m[31mcollapsed[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mdelayed-warnings-list[39;49;00m[37m [39;49;00m([32mnreverse[39;49;00m[37m [39;49;00m[31mcollapsed[39;49;00m))))[37m[39;49;00m$
[37m[39;49;00m$
[37m;; At present this is only used for Emacs internals.[39;49;00m[37m[39;49;00m$
[37m;; Ref http://lists.gnu.org/archive/html/emacs-devel/2012-02/msg00085.html[39;49;00m[37m[39;49;00m$
([34mdefvar[39;49;00m[37m [39;49;00m[31mdelayed-warnings-hook[39;49;00m[37m [39;49;00m'([31mcollapse-delayed-warnings[39;49;00m[37m[39;49;00m$
[37m                                [39;49;00m[31mdisplay-delayed-warnings[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mNormal hook run to process and display delayed warnings.[39;49;00m$
[33mBy default, this hook contains functions to consolidate the[39;49;00m$
[33mwarnings listed in [39;49;00m[33m`delayed-warnings-list'[39;49;00m[33m, display them, and set[39;49;00m$
[33m`delayed-warnings-list'[39;49;00m[33m back to nil.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mdelay-warning[39;49;00m[37m [39;49;00m([31mtype[39;49;00m[37m [39;49;00m[32mmessage[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mlevel[39;49;00m[37m [39;49;00m[32mbuffer-name[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mDisplay a delayed warning.[39;49;00m$
[33mAside from going through [39;49;00m[33m`delayed-warnings-list'[39;49;00m[33m, this is equivalent[39;49;00m$
[33mto [39;49;00m[33m`display-warning'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mpush[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[31mtype[39;49;00m[37m [39;49;00m[32mmessage[39;49;00m[37m [39;49;00m[31mlevel[39;49;00m[37m [39;49;00m[32mbuffer-name[39;49;00m)[37m [39;49;00m[31mdelayed-warnings-list[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m[37m[39;49;00m$
[37m;;;; invisibility specs[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31madd-to-invisibility-spec[39;49;00m[37m [39;49;00m([31melement[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mAdd ELEMENT to [39;49;00m[33m`buffer-invisibility-spec'[39;49;00m[33m.[39;49;00m$
[33mSee documentation for [39;49;00m[33m`buffer-invisibility-spec'[39;49;00m[33m for the kind of elements[39;49;00m$
[33mthat can be added.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mbuffer-invisibility-spec[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbuffer-invisibility-spec[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[31mt[39;49;00m)))[37m[39;49;00m$
[37m  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbuffer-invisibility-spec[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31melement[39;49;00m[37m [39;49;00m[31mbuffer-invisibility-spec[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mremove-from-invisibility-spec[39;49;00m[37m [39;49;00m([31melement[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mRemove ELEMENT from [39;49;00m[33m`buffer-invisibility-spec'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mbuffer-invisibility-spec[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbuffer-invisibility-spec[39;49;00m[37m[39;49;00m$
[37m^I    [39;49;00m([32mdelete[39;49;00m[37m [39;49;00m[31melement[39;49;00m[37m [39;49;00m[31mbuffer-invisibility-spec[39;49;00m))))[37m[39;49;00m$
[37m[39;49;00m[37m[39;49;00m$
[37m;;;; Syntax tables.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
([36mdefmacro[39;49;00m[37m [39;49;00m[36mwith-syntax-table[39;49;00m[37m [39;49;00m([31mtable[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mEvaluate BODY with syntax table of current buffer set to TABLE.[39;49;00m$
[33mThe syntax table of the current buffer is saved, BODY is evaluated, and the[39;49;00m$
[33msaved table is restored, even in case of an abnormal exit.[39;49;00m$
[33mValue is what BODY returns.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m1[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mold-table[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mtable[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
[37m^I[39;49;00m([31mold-buffer[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mbuffer[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m((,[31mold-table[39;49;00m[37m [39;49;00m([32msyntax-table[39;49;00m))[37m[39;49;00m$
[37m^I   [39;49;00m(,[31mold-buffer[39;49;00m[37m [39;49;00m([32mcurrent-buffer[39;49;00m)))[37m[39;49;00m$
[37m       [39;49;00m([34munwind-protect[39;49;00m[37m[39;49;00m$
[37m^I   [39;49;00m([34mprogn[39;49;00m[37m[39;49;00m$
[37m^I     [39;49;00m([32mset-syntax-table[39;49;00m[37m [39;49;00m,[31mtable[39;49;00m)[37m[39;49;00m$
[37m^I     [39;49;00m,@[31mbody[39;49;00m)[37m[39;49;00m$
[37m^I [39;49;00m([34msave-current-buffer[39;49;00m[37m[39;49;00m$
[37m^I   [39;49;00m([32mset-buffer[39;49;00m[37m [39;49;00m,[31mold-buffer[39;49;00m)[37m[39;49;00m$
[37m^I   [39;49;00m([32mset-syntax-table[39;49;00m[37m [39;49;00m,[31mold-table[39;49;00m))))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mmake-syntax-table[39;49;00m[37m [39;49;00m([34m&optional[39;49;00m[37m [39;49;00m[31moldtable[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn a new syntax table.[39;49;00m$
[33mCreate a syntax table which inherits from OLDTABLE (if non-nil) or[39;49;00m$
[33mfrom [39;49;00m[33m`standard-syntax-table'[39;49;00m[33m otherwise.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtable[39;49;00m[37m [39;49;00m([32mmake-char-table[39;49;00m[37m [39;49;00m[33m'syntax-table[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m([32mset-char-table-parent[39;49;00m[37m [39;49;00m[31mtable[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31moldtable[39;49;00m[37m [39;49;00m([32mstandard-syntax-table[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m[31mtable[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31msyntax-after[39;49;00m[37m [39;49;00m([31mpos[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn the raw syntax descriptor for the char after POS.[39;49;00m$
[33mIf POS is outside the buffer's accessible portion, return nil.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36munless[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m[31mpos[39;49;00m[37m [39;49;00m([32mpoint-min[39;49;00m))[37m [39;49;00m([32m>=[39;49;00m[37m [39;49;00m[31mpos[39;49;00m[37m [39;49;00m([32mpoint-max[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mst[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mparse-sexp-lookup-properties[39;49;00m[37m[39;49;00m$
[37m^I^I  [39;49;00m([32mget-char-property[39;49;00m[37m [39;49;00m[31mpos[39;49;00m[37m [39;49;00m[33m'syntax-table[39;49;00m))))[37m[39;49;00m$
[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mconsp[39;49;00m[37m [39;49;00m[31mst[39;49;00m)[37m [39;49;00m[31mst[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00m([32maref[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mst[39;49;00m[37m [39;49;00m([32msyntax-table[39;49;00m))[37m [39;49;00m([32mchar-after[39;49;00m[37m [39;49;00m[31mpos[39;49;00m))))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31msyntax-class[39;49;00m[37m [39;49;00m([31msyntax[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn the code for the syntax class described by SYNTAX.[39;49;00m$
[33m[39;49;00m$
[33mSYNTAX should be a raw syntax descriptor; the return value is a[39;49;00m$
[33minteger which encodes the corresponding syntax class.  See Info[39;49;00m$
[33mnode [39;49;00m[33m`[39;49;00m[33m(elisp)Syntax Table Internals' for a list of codes.[39;49;00m$
[33m[39;49;00m$
[33mIf SYNTAX is nil, return nil.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31msyntax[39;49;00m[37m [39;49;00m([32mlogand[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31msyntax[39;49;00m)[37m [39;49;00m[34m65535[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m[37m[39;49;00m$
[37m;; Utility motion commands[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m;;  Whitespace[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mforward-whitespace[39;49;00m[37m [39;49;00m([31marg[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mMove point to the end of the next sequence of whitespace chars.[39;49;00m$
[33mEach such sequence may be a single newline, or a sequence of[39;49;00m$
[33mconsecutive space and/or tab characters.[39;49;00m$
[33mWith prefix argument ARG, do it ARG times if positive, or move[39;49;00m$
[33mbackwards ARG times if negative.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34minteractive[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m^p[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mnatnump[39;49;00m[37m [39;49;00m[31marg[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m([32mre-search-forward[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m[ [39;49;00m[33m\t[39;49;00m[33m]+[39;49;00m[33m\\[39;49;00m[33m|[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[33m'move[39;49;00m[37m [39;49;00m[31marg[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m[31marg[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mre-search-backward[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m[ [39;49;00m[33m\t[39;49;00m[33m]+[39;49;00m[33m\\[39;49;00m[33m|[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[33m'move[39;49;00m)[37m[39;49;00m$
[37m^I  [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m([32mchar-after[39;49;00m[37m [39;49;00m([32mmatch-beginning[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m [39;49;00m[33m?\n[39;49;00m)[37m[39;49;00m$
[37m^I      [39;49;00m([32mskip-chars-backward[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m [39;49;00m[33m\t[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31marg[39;49;00m[37m [39;49;00m([32m1+[39;49;00m[37m [39;49;00m[31marg[39;49;00m)))))[37m[39;49;00m$
[37m[39;49;00m$
[37m;;  Symbols[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mforward-symbol[39;49;00m[37m [39;49;00m([31marg[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mMove point to the next position that is the end of a symbol.[39;49;00m$
[33mA symbol is any sequence of characters that are in either the[39;49;00m$
[33mword constituent or symbol constituent syntax class.[39;49;00m$
[33mWith prefix argument ARG, do it ARG times if positive, or move[39;49;00m$
[33mbackwards ARG times if negative.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34minteractive[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m^p[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mnatnump[39;49;00m[37m [39;49;00m[31marg[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m([32mre-search-forward[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m([39;49;00m[33m\\[39;49;00m[33msw[39;49;00m[33m\\[39;49;00m[33m|[39;49;00m[33m\\[39;49;00m[33ms_[39;49;00m[33m\\[39;49;00m[33m)+[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[33m'move[39;49;00m[37m [39;49;00m[31marg[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m[31marg[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mre-search-backward[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m([39;49;00m[33m\\[39;49;00m[33msw[39;49;00m[33m\\[39;49;00m[33m|[39;49;00m[33m\\[39;49;00m[33ms_[39;49;00m[33m\\[39;49;00m[33m)+[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[33m'move[39;49;00m)[37m[39;49;00m$
[37m^I  [39;49;00m([32mskip-syntax-backward[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mw_[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31marg[39;49;00m[37m [39;49;00m([32m1+[39;49;00m[37m [39;49;00m[31marg[39;49;00m)))))[37m[39;49;00m$
[37m[39;49;00m$
[37m;;  Syntax blocks[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mforward-same-syntax[39;49;00m[37m [39;49;00m([34m&optional[39;49;00m[37m [39;49;00m[31marg[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mMove point past all characters with the same syntax class.[39;49;00m$
[33mWith prefix argument ARG, do it ARG times if positive, or move[39;49;00m$
[33mbackwards ARG times if negative.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34minteractive[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m^p[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31marg[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31marg[39;49;00m[37m [39;49;00m[34m1[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m[31marg[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([32mskip-syntax-backward[39;49;00m[37m[39;49;00m$
[37m     [39;49;00m([32mchar-to-string[39;49;00m[37m [39;49;00m([32mchar-syntax[39;49;00m[37m [39;49;00m([32mchar-before[39;49;00m))))[37m[39;49;00m$
[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31marg[39;49;00m[37m [39;49;00m([32m1+[39;49;00m[37m [39;49;00m[31marg[39;49;00m)))[37m[39;49;00m$
[37m  [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m[31marg[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([32mskip-syntax-forward[39;49;00m[37m [39;49;00m([32mchar-to-string[39;49;00m[37m [39;49;00m([32mchar-syntax[39;49;00m[37m [39;49;00m([32mchar-after[39;49;00m))))[37m[39;49;00m$
[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31marg[39;49;00m[37m [39;49;00m([32m1-[39;49;00m[37m [39;49;00m[31marg[39;49;00m))))[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m[37m[39;49;00m$
[37m;;;; Text clones[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
([34mdefvar[39;49;00m[37m [39;49;00m[31mtext-clone--maintaining[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mtext-clone--maintain[39;49;00m[37m [39;49;00m([31mol1[39;49;00m[37m [39;49;00m[31mafter[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31m_len[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mPropagate the changes made under the overlay OL1 to the other clones.[39;49;00m$
[33mThis is used on the [39;49;00m[33m`modification-hooks'[39;49;00m[33m property of text clones.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mafter[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m[31mundo-in-progress[39;49;00m)[37m[39;49;00m$
[37m             [39;49;00m([31mnot[39;49;00m[37m [39;49;00m[31mtext-clone--maintaining[39;49;00m)[37m[39;49;00m$
[37m             [39;49;00m([32moverlay-start[39;49;00m[37m [39;49;00m[31mol1[39;49;00m))[37m[39;49;00m$
[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mmargin[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32moverlay-get[39;49;00m[37m [39;49;00m[31mol1[39;49;00m[37m [39;49;00m[33m'text-clone-spreadp[39;49;00m)[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[34m0[39;49;00m)))[37m[39;49;00m$
[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m[37m [39;49;00m([32mmax[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m[37m [39;49;00m([32m+[39;49;00m[37m [39;49;00m([32moverlay-start[39;49;00m[37m [39;49;00m[31mol1[39;49;00m)[37m [39;49;00m[31mmargin[39;49;00m)))[37m[39;49;00m$
[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m([32mmin[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m([32moverlay-end[39;49;00m[37m [39;49;00m[31mol1[39;49;00m)[37m [39;49;00m[31mmargin[39;49;00m)))[37m[39;49;00m$
[37m      [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32m<=[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m[37m [39;49;00m[31mend[39;49;00m)[37m[39;49;00m$
[37m^I[39;49;00m([34msave-excursion[39;49;00m[37m[39;49;00m$
[37m^I  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32moverlay-get[39;49;00m[37m [39;49;00m[31mol1[39;49;00m[37m [39;49;00m[33m'text-clone-syntax[39;49;00m)[37m[39;49;00m$
[37m^I    [39;49;00m[37m;; Check content of the clone's text.[39;49;00m[37m[39;49;00m$
[37m^I    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mcbeg[39;49;00m[37m [39;49;00m([32m+[39;49;00m[37m [39;49;00m([32moverlay-start[39;49;00m[37m [39;49;00m[31mol1[39;49;00m)[37m [39;49;00m[31mmargin[39;49;00m))[37m[39;49;00m$
[37m^I^I  [39;49;00m([31mcend[39;49;00m[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m([32moverlay-end[39;49;00m[37m [39;49;00m[31mol1[39;49;00m)[37m [39;49;00m[31mmargin[39;49;00m)))[37m[39;49;00m$
[37m^I      [39;49;00m([32mgoto-char[39;49;00m[37m [39;49;00m[31mcbeg[39;49;00m)[37m[39;49;00m$
[37m^I      [39;49;00m([36msave-match-data[39;49;00m[37m[39;49;00m$
[37m^I^I[39;49;00m([34mif[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mre-search-forward[39;49;00m[37m[39;49;00m$
[37m^I^I^I  [39;49;00m([32moverlay-get[39;49;00m[37m [39;49;00m[31mol1[39;49;00m[37m [39;49;00m[33m'text-clone-syntax[39;49;00m)[37m [39;49;00m[31mcend[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
[37m^I^I    [39;49;00m[37m;; Mark the overlay for deletion.[39;49;00m[37m[39;49;00m$
[37m^I^I    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[31mcbeg[39;49;00m)[37m[39;49;00m$
[37m^I^I  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m([32mmatch-end[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[31mcend[39;49;00m)[37m[39;49;00m$
[37m^I^I    [39;49;00m[37m;; Shrink the clone at its end.[39;49;00m[37m[39;49;00m$
[37m^I^I    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m([32mmin[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m([32mmatch-end[39;49;00m[37m [39;49;00m[34m0[39;49;00m)))[37m[39;49;00m$
[37m^I^I    [39;49;00m([32mmove-overlay[39;49;00m[37m [39;49;00m[31mol1[39;49;00m[37m [39;49;00m([32moverlay-start[39;49;00m[37m [39;49;00m[31mol1[39;49;00m)[37m[39;49;00m$
[37m^I^I^I^I  [39;49;00m([32m+[39;49;00m[37m [39;49;00m([32mmatch-end[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[31mmargin[39;49;00m)))[37m[39;49;00m$
[37m^I^I  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m([32mmatch-beginning[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[31mcbeg[39;49;00m)[37m[39;49;00m$
[37m^I^I    [39;49;00m[37m;; Shrink the clone at its beginning.[39;49;00m[37m[39;49;00m$
[37m^I^I    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m[37m [39;49;00m([32mmax[39;49;00m[37m [39;49;00m([32mmatch-beginning[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[31mbeg[39;49;00m))[37m[39;49;00m$
[37m^I^I    [39;49;00m([32mmove-overlay[39;49;00m[37m [39;49;00m[31mol1[39;49;00m[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m([32mmatch-beginning[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[31mmargin[39;49;00m)[37m[39;49;00m$
[37m^I^I^I^I  [39;49;00m([32moverlay-end[39;49;00m[37m [39;49;00m[31mol1[39;49;00m)))))))[37m[39;49;00m$
[37m^I  [39;49;00m[37m;; Now go ahead and update the clones.[39;49;00m[37m[39;49;00m$
[37m^I  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mhead[39;49;00m[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m[37m [39;49;00m([32moverlay-start[39;49;00m[37m [39;49;00m[31mol1[39;49;00m)))[37m[39;49;00m$
[37m^I^I[39;49;00m([31mtail[39;49;00m[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m([32moverlay-end[39;49;00m[37m [39;49;00m[31mol1[39;49;00m)[37m [39;49;00m[31mend[39;49;00m))[37m[39;49;00m$
[37m^I^I[39;49;00m([31mstr[39;49;00m[37m [39;49;00m([32mbuffer-substring[39;49;00m[37m [39;49;00m[31mbeg[39;49;00m[37m [39;49;00m[31mend[39;49;00m))[37m[39;49;00m$
[37m^I^I[39;49;00m([31mnothing-left[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
[37m^I^I[39;49;00m([31mtext-clone--maintaining[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
[37m^I    [39;49;00m([36mdolist[39;49;00m[37m [39;49;00m([31mol2[39;49;00m[37m [39;49;00m([32moverlay-get[39;49;00m[37m [39;49;00m[31mol1[39;49;00m[37m [39;49;00m[33m'text-clones[39;49;00m))[37m[39;49;00m$
[37m^I      [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31moe[39;49;00m[37m [39;49;00m([32moverlay-end[39;49;00m[37m [39;49;00m[31mol2[39;49;00m)))[37m[39;49;00m$
[37m^I^I[39;49;00m([36munless[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mol1[39;49;00m[37m [39;49;00m[31mol2[39;49;00m)[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[31moe[39;49;00m))[37m[39;49;00m$
[37m^I^I  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mnothing-left[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
[37m^I^I  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mmod-beg[39;49;00m[37m [39;49;00m([32m+[39;49;00m[37m [39;49;00m([32moverlay-start[39;49;00m[37m [39;49;00m[31mol2[39;49;00m)[37m [39;49;00m[31mhead[39;49;00m)))[37m[39;49;00m$
[37m^I^I    [39;49;00m[37m;;(overlay-put ol2 'modification-hooks nil)[39;49;00m[37m[39;49;00m$
[37m^I^I    [39;49;00m([32mgoto-char[39;49;00m[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m([32moverlay-end[39;49;00m[37m [39;49;00m[31mol2[39;49;00m)[37m [39;49;00m[31mtail[39;49;00m))[37m[39;49;00m$
[37m^I^I    [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m[31mmod-beg[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m))[37m[39;49;00m$
[37m^I^I      [39;49;00m([34msave-excursion[39;49;00m[37m [39;49;00m([32minsert[39;49;00m[37m [39;49;00m[31mstr[39;49;00m))[37m[39;49;00m$
[37m^I^I      [39;49;00m([32mdelete-region[39;49;00m[37m [39;49;00m[31mmod-beg[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m)))[37m[39;49;00m$
[37m^I^I    [39;49;00m[37m;;(overlay-put ol2 'modification-hooks '(text-clone--maintain))[39;49;00m[37m[39;49;00m$
[37m^I^I    [39;49;00m))))[37m[39;49;00m$
[37m^I    [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mnothing-left[39;49;00m[37m [39;49;00m([32mdelete-overlay[39;49;00m[37m [39;49;00m[31mol1[39;49;00m))))))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mtext-clone-create[39;49;00m[37m [39;49;00m([31mstart[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mspreadp[39;49;00m[37m [39;49;00m[31msyntax[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mCreate a text clone of START...END at point.[39;49;00m$
[33mText clones are chunks of text that are automatically kept identical:[39;49;00m$
[33mchanges done to one of the clones will be immediately propagated to the other.[39;49;00m$
[33m[39;49;00m$
[33mThe buffer's content at point is assumed to be already identical to[39;49;00m$
[33mthe one between START and END.[39;49;00m$
[33mIf SYNTAX is provided it's a regexp that describes the possible text of[39;49;00m$
[33mthe clones; the clone will be shrunk or killed if necessary to ensure that[39;49;00m$
[33mits text matches the regexp.[39;49;00m$
[33mIf SPREADP is non-nil it indicates that text inserted before/after the[39;49;00m$
[33mclone should be incorporated in the clone.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; To deal with SPREADP we can either use an overlay with `nil t' along[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; with insert-(behind|in-front-of)-hooks or use a slightly larger overlay[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; (with a one-char margin at each end) with `t nil'.[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; We opted for a larger overlay because it behaves better in the case[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; where the clone is reduced to the empty string (we want the overlay to[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; stay when the clone's content is the empty string and we want to use[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; `evaporate' to make sure those overlays get deleted when needed).[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;;[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mpt-end[39;49;00m[37m [39;49;00m([32m+[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m)[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[31mstart[39;49;00m)))[37m[39;49;00m$
[37m  ^I [39;49;00m([31mstart-margin[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m[31mspreadp[39;49;00m)[37m [39;49;00m([32mbobp[39;49;00m)[37m [39;49;00m([32m<=[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m([32mpoint-min[39;49;00m)))[37m[39;49;00m$
[37m^I^I^I   [39;49;00m[34m0[39;49;00m[37m [39;49;00m[34m1[39;49;00m))[37m[39;49;00m$
[37m  ^I [39;49;00m([31mend-margin[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m[31mspreadp[39;49;00m)[37m[39;49;00m$
[37m^I^I^I     [39;49;00m([32m>=[39;49;00m[37m [39;49;00m[31mpt-end[39;49;00m[37m [39;49;00m([32mpoint-max[39;49;00m))[37m[39;49;00m$
[37m  ^I^I^I     [39;49;00m([32m>=[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m([32mpoint-max[39;49;00m)))[37m[39;49;00m$
[37m  ^I^I^I [39;49;00m[34m0[39;49;00m[37m [39;49;00m[34m1[39;49;00m))[37m[39;49;00m$
[37m         [39;49;00m[37m;; FIXME: Reuse overlays at point to extend dups![39;49;00m[37m[39;49;00m$
[37m  ^I [39;49;00m([31mol1[39;49;00m[37m [39;49;00m([32mmake-overlay[39;49;00m[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m[31mstart[39;49;00m[37m [39;49;00m[31mstart-margin[39;49;00m)[37m [39;49;00m([32m+[39;49;00m[37m [39;49;00m[31mend[39;49;00m[37m [39;49;00m[31mend-margin[39;49;00m)[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
[37m  ^I [39;49;00m([31mol2[39;49;00m[37m [39;49;00m([32mmake-overlay[39;49;00m[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m([32mpoint[39;49;00m)[37m [39;49;00m[31mstart-margin[39;49;00m)[37m [39;49;00m([32m+[39;49;00m[37m [39;49;00m[31mpt-end[39;49;00m[37m [39;49;00m[31mend-margin[39;49;00m)[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
[37m^I [39;49;00m([31mdups[39;49;00m[37m [39;49;00m([32mlist[39;49;00m[37m [39;49;00m[31mol1[39;49;00m[37m [39;49;00m[31mol2[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m([32moverlay-put[39;49;00m[37m [39;49;00m[31mol1[39;49;00m[37m [39;49;00m[33m'modification-hooks[39;49;00m[37m [39;49;00m'([31mtext-clone--maintain[39;49;00m))[37m[39;49;00m$
[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31mspreadp[39;49;00m[37m [39;49;00m([32moverlay-put[39;49;00m[37m [39;49;00m[31mol1[39;49;00m[37m [39;49;00m[33m'text-clone-spreadp[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31msyntax[39;49;00m[37m [39;49;00m([32moverlay-put[39;49;00m[37m [39;49;00m[31mol1[39;49;00m[37m [39;49;00m[33m'text-clone-syntax[39;49;00m[37m [39;49;00m[31msyntax[39;49;00m))[37m[39;49;00m$
[37m    [39;49;00m[37m;;(overlay-put ol1 'face 'underline)[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m([32moverlay-put[39;49;00m[37m [39;49;00m[31mol1[39;49;00m[37m [39;49;00m[33m'evaporate[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([32moverlay-put[39;49;00m[37m [39;49;00m[31mol1[39;49;00m[37m [39;49;00m[33m'text-clones[39;49;00m[37m [39;49;00m[31mdups[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m[37m;;[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m([32moverlay-put[39;49;00m[37m [39;49;00m[31mol2[39;49;00m[37m [39;49;00m[33m'modification-hooks[39;49;00m[37m [39;49;00m'([31mtext-clone--maintain[39;49;00m))[37m[39;49;00m$
[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31mspreadp[39;49;00m[37m [39;49;00m([32moverlay-put[39;49;00m[37m [39;49;00m[31mol2[39;49;00m[37m [39;49;00m[33m'text-clone-spreadp[39;49;00m[37m [39;49;00m[31mt[39;49;00m))[37m[39;49;00m$
[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31msyntax[39;49;00m[37m [39;49;00m([32moverlay-put[39;49;00m[37m [39;49;00m[31mol2[39;49;00m[37m [39;49;00m[33m'text-clone-syntax[39;49;00m[37m [39;49;00m[31msyntax[39;49;00m))[37m[39;49;00m$
[37m    [39;49;00m[37m;;(overlay-put ol2 'face 'underline)[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m([32moverlay-put[39;49;00m[37m [39;49;00m[31mol2[39;49;00m[37m [39;49;00m[33m'evaporate[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([32moverlay-put[39;49;00m[37m [39;49;00m[31mol2[39;49;00m[37m [39;49;00m[33m'text-clones[39;49;00m[37m [39;49;00m[31mdups[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m[37m[39;49;00m$
[37m;;;; Mail user agents.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m;; Here we include just enough for other packages to be able[39;49;00m[37m[39;49;00m$
[37m;; to define them.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mdefine-mail-user-agent[39;49;00m[37m [39;49;00m([31msymbol[39;49;00m[37m [39;49;00m[31mcomposefunc[39;49;00m[37m [39;49;00m[31msendfunc[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I      [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mabortfunc[39;49;00m[37m [39;49;00m[31mhookvar[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mDefine a symbol to identify a mail-sending package for [39;49;00m[33m`mail-user-agent'[39;49;00m[33m.[39;49;00m$
[33m[39;49;00m$
[33mSYMBOL can be any Lisp symbol.  Its function definition and/or[39;49;00m$
[33mvalue as a variable do not matter for this usage; we use only certain[39;49;00m$
[33mproperties on its property list, to encode the rest of the arguments.[39;49;00m$
[33m[39;49;00m$
[33mCOMPOSEFUNC is program callable function that composes an outgoing[39;49;00m$
[33mmail message buffer.  This function should set up the basics of the[39;49;00m$
[33mbuffer without requiring user interaction.  It should populate the[39;49;00m$
[33mstandard mail headers, leaving the [39;49;00m[33m`to:'[39;49;00m[33m and [39;49;00m[33m`subject:'[39;49;00m[33m headers blank[39;49;00m$
[33mby default.[39;49;00m$
[33m[39;49;00m$
[33mCOMPOSEFUNC should accept several optional arguments--the same[39;49;00m$
[33marguments that [39;49;00m[33m`compose-mail'[39;49;00m[33m takes.  See that function's documentation.[39;49;00m$
[33m[39;49;00m$
[33mSENDFUNC is the command a user would run to send the message.[39;49;00m$
[33m[39;49;00m$
[33mOptional ABORTFUNC is the command a user would run to abort the[39;49;00m$
[33mmessage.  For mail packages that don't have a separate abort function,[39;49;00m$
[33mthis can be [39;49;00m[33m`kill-buffer'[39;49;00m[33m (the equivalent of omitting this argument).[39;49;00m$
[33m[39;49;00m$
[33mOptional HOOKVAR is a hook variable that gets run before the message[39;49;00m$
[33mis actually sent.  Callers that use the [39;49;00m[33m`mail-user-agent'[39;49;00m[33m may[39;49;00m$
[33minstall a hook function temporarily on this hook variable.[39;49;00m$
[33mIf HOOKVAR is nil, [39;49;00m[33m`mail-send-hook'[39;49;00m[33m is used.[39;49;00m$
[33m[39;49;00m$
[33mThe properties used on SYMBOL are [39;49;00m[33m`composefunc'[39;49;00m[33m, [39;49;00m[33m`sendfunc'[39;49;00m[33m,[39;49;00m$
[33m`abortfunc'[39;49;00m[33m, and [39;49;00m[33m`hookvar'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([32mput[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m[37m [39;49;00m[33m'composefunc[39;49;00m[37m [39;49;00m[31mcomposefunc[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m([32mput[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m[37m [39;49;00m[33m'sendfunc[39;49;00m[37m [39;49;00m[31msendfunc[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m([32mput[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m[37m [39;49;00m[33m'abortfunc[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mabortfunc[39;49;00m[37m [39;49;00m[33m'kill-buffer[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m([32mput[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m[37m [39;49;00m[33m'hookvar[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mhookvar[39;49;00m[37m [39;49;00m[33m'mail-send-hook[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m[37m[39;49;00m$
([34mdefvar[39;49;00m[37m [39;49;00m[31mcalled-interactively-p-functions[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mSpecial hook called to skip special frames in [39;49;00m[33m`called-interactively-p'[39;49;00m[33m.[39;49;00m$
[33mThe functions are called with 3 arguments: (I FRAME1 FRAME2),[39;49;00m$
[33mwhere FRAME1 is a [39;49;00m[33m\"[39;49;00m[33mcurrent frame[39;49;00m[33m\"[39;49;00m[33m, FRAME2 is the next frame,[39;49;00m$
[33mI is the index of the frame after FRAME2.  It should return nil[39;49;00m$
[33mif those frames don't seem special and otherwise, it should return[39;49;00m$
[33mthe number of frames to skip (minus 1).[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
([34mdefconst[39;49;00m[37m [39;49;00m[31minternal--funcall-interactively[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([32msymbol-function[39;49;00m[37m [39;49;00m[33m'funcall-interactively[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mcalled-interactively-p[39;49;00m[37m [39;49;00m([34m&optional[39;49;00m[37m [39;49;00m[31mkind[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn t if the containing function was called by [39;49;00m[33m`call-interactively'[39;49;00m[33m.[39;49;00m$
[33mIf KIND is [39;49;00m[33m`interactive'[39;49;00m[33m, then only return t if the call was made[39;49;00m$
[33minteractively by the user, i.e. not in [39;49;00m[33m`noninteractive'[39;49;00m[33m mode nor[39;49;00m$
[33mwhen [39;49;00m[33m`executing-kbd-macro'[39;49;00m[33m.[39;49;00m$
[33mIf KIND is [39;49;00m[33m`any'[39;49;00m[33m, on the other hand, it will return t for any kind of[39;49;00m$
[33minteractive call, including being called as the binding of a key or[39;49;00m$
[33mfrom a keyboard macro, even in [39;49;00m[33m`noninteractive'[39;49;00m[33m mode.[39;49;00m$
[33m[39;49;00m$
[33mThis function is very brittle, it may fail to return the intended result when[39;49;00m$
[33mthe code is debugged, advised, or instrumented in some form.  Some macros and[39;49;00m$
[33mspecial forms (such as [39;49;00m[33m`condition-case'[39;49;00m[33m) may also sometimes wrap their bodies[39;49;00m$
[33min a [39;49;00m[33m`lambda'[39;49;00m[33m, so any call to [39;49;00m[33m`called-interactively-p'[39;49;00m[33m from those bodies will[39;49;00m$
[33mindicate whether that lambda (rather than the surrounding function) was called[39;49;00m$
[33minteractively.[39;49;00m$
[33m[39;49;00m$
[33mInstead of using this function, it is cleaner and more reliable to give your[39;49;00m$
[33mfunction an extra optional argument whose [39;49;00m[33m`interactive'[39;49;00m[33m spec specifies[39;49;00m$
[33mnon-nil unconditionally ([39;49;00m[33m\"[39;49;00m[33mp[39;49;00m[33m\"[39;49;00m[33m is a good way to do this), or via[39;49;00m$
[33m\([39;49;00m[33mnot (or executing-kbd-macro noninteractive)).[39;49;00m$
[33m[39;49;00m$
[33mThe only known proper use of [39;49;00m[33m`interactive'[39;49;00m[33m for KIND is in deciding[39;49;00m$
[33mwhether to display a helpful message, or how to display it.  If you're[39;49;00m$
[33mthinking of using it for any other purpose, it is quite likely that[39;49;00m$
[33myou're making a mistake.  Think: what do you want to do when the[39;49;00m$
[33mcommand is called from a keyboard macro?[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31madvertised-calling-convention[39;49;00m[37m [39;49;00m([31mkind[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m23.1[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mkind[39;49;00m[37m [39;49;00m[33m'interactive[39;49;00m)[37m[39;49;00m$
[37m                  [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mexecuting-kbd-macro[39;49;00m[37m [39;49;00m[31mnoninteractive[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mi[39;49;00m[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m[37m;; 0 is the called-interactively-p frame.[39;49;00m[37m[39;49;00m$
[37m           [39;49;00m[31mframe[39;49;00m[37m [39;49;00m[31mnextframe[39;49;00m[37m[39;49;00m$
[37m           [39;49;00m([31mget-next-frame[39;49;00m[37m[39;49;00m$
[37m            [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m()[37m[39;49;00m$
[37m              [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mframe[39;49;00m[37m [39;49;00m[31mnextframe[39;49;00m)[37m[39;49;00m$
[37m              [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mnextframe[39;49;00m[37m [39;49;00m([32mbacktrace-frame[39;49;00m[37m [39;49;00m[31mi[39;49;00m[37m [39;49;00m[33m'called-interactively-p[39;49;00m))[37m[39;49;00m$
[37m              [39;49;00m[37m;; (message "Frame %d = %S" i nextframe)[39;49;00m[37m[39;49;00m$
[37m              [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mi[39;49;00m[37m [39;49;00m([32m1+[39;49;00m[37m [39;49;00m[31mi[39;49;00m)))))[37m[39;49;00m$
[37m      [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mget-next-frame[39;49;00m)[37m [39;49;00m[37m;; Get the first frame.[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([34mwhile[39;49;00m[37m[39;49;00m$
[37m          [39;49;00m[37m;; FIXME: The edebug and advice handling should be made modular and[39;49;00m[37m[39;49;00m$
[37m          [39;49;00m[37m;; provided directly by edebug.el and nadvice.el.[39;49;00m[37m[39;49;00m$
[37m          [39;49;00m([34mprogn[39;49;00m[37m[39;49;00m$
[37m            [39;49;00m[37m;; frame    =(backtrace-frame i-2)[39;49;00m[37m[39;49;00m$
[37m            [39;49;00m[37m;; nextframe=(backtrace-frame i-1)[39;49;00m[37m[39;49;00m$
[37m            [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mget-next-frame[39;49;00m)[37m[39;49;00m$
[37m            [39;49;00m[37m;; `pcase' would be a fairly good fit here, but it sometimes moves[39;49;00m[37m[39;49;00m$
[37m            [39;49;00m[37m;; branches within local functions, which then messes up the[39;49;00m[37m[39;49;00m$
[37m            [39;49;00m[37m;; `backtrace-frame' data we get,[39;49;00m[37m[39;49;00m$
[37m            [39;49;00m([34mor[39;49;00m[37m[39;49;00m$
[37m             [39;49;00m[37m;; Skip special forms (from non-compiled code).[39;49;00m[37m[39;49;00m$
[37m             [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mframe[39;49;00m[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mframe[39;49;00m)))[37m[39;49;00m$
[37m             [39;49;00m[37m;; Skip also `interactive-p' (because we don't want to know if[39;49;00m[37m[39;49;00m$
[37m             [39;49;00m[37m;; interactive-p was called interactively but if it's caller was)[39;49;00m[37m[39;49;00m$
[37m             [39;49;00m[37m;; and `byte-code' (idem; this appears in subexpressions of things[39;49;00m[37m[39;49;00m$
[37m             [39;49;00m[37m;; like condition-case, which are wrapped in a separate bytecode[39;49;00m[37m[39;49;00m$
[37m             [39;49;00m[37m;; chunk).[39;49;00m[37m[39;49;00m$
[37m             [39;49;00m[37m;; FIXME: For lexical-binding code, this is much worse,[39;49;00m[37m[39;49;00m$
[37m             [39;49;00m[37m;; because the frames look like "byte-code -> funcall -> #[...]",[39;49;00m[37m[39;49;00m$
[37m             [39;49;00m[37m;; which is not a reliable signature.[39;49;00m[37m[39;49;00m$
[37m             [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mframe[39;49;00m)[37m [39;49;00m'([31minteractive-p[39;49;00m[37m [39;49;00m[33m'byte-code[39;49;00m))[37m[39;49;00m$
[37m             [39;49;00m[37m;; Skip package-specific stack-frames.[39;49;00m[37m[39;49;00m$
[37m             [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mskip[39;49;00m[37m [39;49;00m([32mrun-hook-with-args-until-success[39;49;00m[37m[39;49;00m$
[37m                          [39;49;00m[33m'called-interactively-p-functions[39;49;00m[37m[39;49;00m$
[37m                          [39;49;00m[31mi[39;49;00m[37m [39;49;00m[31mframe[39;49;00m[37m [39;49;00m[31mnextframe[39;49;00m)))[37m[39;49;00m$
[37m               [39;49;00m([36mpcase[39;49;00m[37m [39;49;00m[31mskip[39;49;00m[37m[39;49;00m$
[37m                 [39;49;00m(`[31mnil[39;49;00m[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
[37m                 [39;49;00m(`[34m0[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
[37m                 [39;49;00m([31m_[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mi[39;49;00m[37m [39;49;00m([32m+[39;49;00m[37m [39;49;00m[31mi[39;49;00m[37m [39;49;00m[31mskip[39;49;00m[37m [39;49;00m[34m-1[39;49;00m))[37m [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mget-next-frame[39;49;00m)))))))[37m[39;49;00m$
[37m      [39;49;00m[37m;; Now `frame' should be "the function from which we were called".[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([36mpcase[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m[31mframe[39;49;00m[37m [39;49;00m[31mnextframe[39;49;00m)[37m[39;49;00m$
[37m        [39;49;00m[37m;; No subr calls `interactive-p', so we can rule that out.[39;49;00m[37m[39;49;00m$
[37m        [39;49;00m(`((,[31m_[39;49;00m[37m [39;49;00m,([31mpred[39;49;00m[37m [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31mf[39;49;00m)[37m [39;49;00m([32msubrp[39;49;00m[37m [39;49;00m([32mindirect-function[39;49;00m[37m [39;49;00m[31mf[39;49;00m))))[37m [39;49;00m.[37m [39;49;00m,[31m_[39;49;00m)[37m [39;49;00m.[37m [39;49;00m,[31m_[39;49;00m)[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
[37m        [39;49;00m[37m;; In case #<subr funcall-interactively> without going through the[39;49;00m[37m[39;49;00m$
[37m        [39;49;00m[37m;; `funcall-interactively' symbol (bug#3984).[39;49;00m[37m[39;49;00m$
[37m        [39;49;00m(`(,[31m_[39;49;00m[37m [39;49;00m.[37m [39;49;00m([31mt[39;49;00m[37m [39;49;00m,([31mpred[39;49;00m[37m [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m([31mf[39;49;00m)[37m[39;49;00m$
[37m                            [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31minternal--funcall-interactively[39;49;00m[37m[39;49;00m$
[37m                                [39;49;00m([32mindirect-function[39;49;00m[37m [39;49;00m[31mf[39;49;00m))))[37m[39;49;00m$
[37m                   [39;49;00m.[37m [39;49;00m,[31m_[39;49;00m))[37m[39;49;00m$
[37m         [39;49;00m[31mt[39;49;00m)))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31minteractive-p[39;49;00m[37m [39;49;00m()[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn t if the containing function was run directly by user input.[39;49;00m$
[33mThis means that the function was called with [39;49;00m[33m`call-interactively'[39;49;00m[33m[39;49;00m$
[33m\([39;49;00m[33mwhich includes being called as the binding of a key)[39;49;00m$
[33mand input is currently coming from the keyboard (not a keyboard macro),[39;49;00m$
[33mand Emacs is not running in batch mode ([39;49;00m[33m`noninteractive'[39;49;00m[33m is nil).[39;49;00m$
[33m[39;49;00m$
[33mThe only known proper use of [39;49;00m[33m`interactive-p'[39;49;00m[33m is in deciding whether to[39;49;00m$
[33mdisplay a helpful message, or how to display it.  If you're thinking[39;49;00m$
[33mof using it for any other purpose, it is quite likely that you're[39;49;00m$
[33mmaking a mistake.  Think: what do you want to do when the command is[39;49;00m$
[33mcalled from a keyboard macro or in batch mode?[39;49;00m$
[33m[39;49;00m$
[33mTo test whether your function was called with [39;49;00m[33m`call-interactively'[39;49;00m[33m,[39;49;00m$
[33meither (i) add an extra optional argument and give it an [39;49;00m[33m`interactive'[39;49;00m[33m[39;49;00m$
[33mspec that specifies non-nil unconditionally (such as [39;49;00m[33m\"[39;49;00m[33mp[39;49;00m[33m\"[39;49;00m[33m); or (ii)[39;49;00m$
[33muse [39;49;00m[33m`called-interactively-p'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mobsolete[39;49;00m[37m [39;49;00m[31mcalled-interactively-p[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m23.2[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m([31mcalled-interactively-p[39;49;00m[37m [39;49;00m[33m'interactive[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31minternal-push-keymap[39;49;00m[37m [39;49;00m([31mkeymap[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mmap[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m[37m [39;49;00m[31mmap[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[33m'add-keymap-witness[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m))[37m[39;49;00m$
[37m        [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m([31mmake-composed-keymap[39;49;00m[37m [39;49;00m[31mnil[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m)))[37m[39;49;00m$
[37m        [39;49;00m([36mpush[39;49;00m[37m [39;49;00m[33m'add-keymap-witness[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mmap[39;49;00m))[37m[39;49;00m$
[37m        [39;49;00m([32mset[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m[37m [39;49;00m[31mmap[39;49;00m))[37m[39;49;00m$
[37m      [39;49;00m([36mpush[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mmap[39;49;00m)))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31minternal-pop-keymap[39;49;00m[37m [39;49;00m([31mkeymap[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mmap[39;49;00m[37m [39;49;00m([32msymbol-value[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mmemq[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m[37m [39;49;00m[31mmap[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m([36msetf[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mmap[39;49;00m)[37m [39;49;00m([32mdelq[39;49;00m[37m [39;49;00m[31mkeymap[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mmap[39;49;00m))))[37m[39;49;00m$
[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtail[39;49;00m[37m [39;49;00m([31mcddr[39;49;00m[37m [39;49;00m[31mmap[39;49;00m)))[37m[39;49;00m$
[37m      [39;49;00m([34mand[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)[37m [39;49;00m([32mkeymapp[39;49;00m[37m [39;49;00m[31mtail[39;49;00m))[37m[39;49;00m$
[37m           [39;49;00m([32meq[39;49;00m[37m [39;49;00m[33m'add-keymap-witness[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mmap[39;49;00m))[37m[39;49;00m$
[37m           [39;49;00m([32mset[39;49;00m[37m [39;49;00m[31msymbol[39;49;00m[37m [39;49;00m[31mtail[39;49;00m)))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefine-obsolete-function-alias[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[33m'set-temporary-overlay-map[39;49;00m[37m [39;49;00m[33m'set-transient-map[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m24.4[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mset-transient-map[39;49;00m[37m [39;49;00m([31mmap[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mkeep-pred[39;49;00m[37m [39;49;00m[31mon-exit[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mSet MAP as a temporary keymap taking precedence over other keymaps.[39;49;00m$
[33mNormally, MAP is used only once, to look up the very next key.[39;49;00m$
[33mHowever, if the optional argument KEEP-PRED is t, MAP stays[39;49;00m$
[33mactive if a key from MAP is used.  KEEP-PRED can also be a[39;49;00m$
[33mfunction of no arguments: it is called from [39;49;00m[33m`pre-command-hook'[39;49;00m[33m and[39;49;00m$
[33mif it returns non-nil, then MAP stays active.[39;49;00m$
[33m[39;49;00m$
[33mOptional arg ON-EXIT, if non-nil, specifies a function that is[39;49;00m$
[33mcalled, with no arguments, after MAP is deactivated.[39;49;00m$
[33m[39;49;00m$
[33mThis uses [39;49;00m[33m`overriding-terminal-local-map'[39;49;00m[33m which takes precedence over all other[39;49;00m$
[33mkeymaps.  As usual, if no match for a key is found in MAP, the normal key[39;49;00m$
[33mlookup sequence then continues.[39;49;00m$
[33m[39;49;00m$
[33mThis returns an [39;49;00m[33m\"[39;49;00m[33mexit function[39;49;00m[33m\"[39;49;00m[33m, which can be called with no argument[39;49;00m$
[33mto deactivate this transient map, regardless of KEEP-PRED.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mclearfun[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mclear-transient-map[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
[37m         [39;49;00m([31mexitfun[39;49;00m[37m[39;49;00m$
[37m          [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m()[37m[39;49;00m$
[37m            [39;49;00m([31minternal-pop-keymap[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m[33m'overriding-terminal-local-map[39;49;00m)[37m[39;49;00m$
[37m            [39;49;00m([31mremove-hook[39;49;00m[37m [39;49;00m[33m'pre-command-hook[39;49;00m[37m [39;49;00m[31mclearfun[39;49;00m)[37m[39;49;00m$
[37m            [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31mon-exit[39;49;00m[37m [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mon-exit[39;49;00m)))))[37m[39;49;00m$
[37m    [39;49;00m[37m;; Don't use letrec, because equal (in add/remove-hook) would get trapped[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[37m;; in a cycle.[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m([32mfset[39;49;00m[37m [39;49;00m[31mclearfun[39;49;00m[37m[39;49;00m$
[37m          [39;49;00m([36mlambda[39;49;00m[37m [39;49;00m()[37m[39;49;00m$
[37m            [39;49;00m([36mwith-demoted-errors[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mset-transient-map PCH: %S[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m              [39;49;00m([36munless[39;49;00m[37m [39;49;00m([34mcond[39;49;00m[37m[39;49;00m$
[37m                       [39;49;00m(([32mnull[39;49;00m[37m [39;49;00m[31mkeep-pred[39;49;00m)[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
[37m                       [39;49;00m(([31mnot[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m([31mcadr[39;49;00m[37m [39;49;00m[31moverriding-terminal-local-map[39;49;00m)))[37m[39;49;00m$
[37m                        [39;49;00m[37m;; There's presumably some other transient-map in[39;49;00m[37m[39;49;00m$
[37m                        [39;49;00m[37m;; effect.  Wait for that one to terminate before we[39;49;00m[37m[39;49;00m$
[37m                        [39;49;00m[37m;; remove ourselves.[39;49;00m[37m[39;49;00m$
[37m                        [39;49;00m[37m;; For example, if isearch and C-u both use transient[39;49;00m[37m[39;49;00m$
[37m                        [39;49;00m[37m;; maps, then the lifetime of the C-u should be nested[39;49;00m[37m[39;49;00m$
[37m                        [39;49;00m[37m;; within isearch's, so the pre-command-hook of[39;49;00m[37m[39;49;00m$
[37m                        [39;49;00m[37m;; isearch should be suspended during the C-u one so[39;49;00m[37m[39;49;00m$
[37m                        [39;49;00m[37m;; we don't exit isearch just because we hit 1 after[39;49;00m[37m[39;49;00m$
[37m                        [39;49;00m[37m;; C-u and that 1 exits isearch whereas it doesn't[39;49;00m[37m[39;49;00m$
[37m                        [39;49;00m[37m;; exit C-u.[39;49;00m[37m[39;49;00m$
[37m                        [39;49;00m[31mt[39;49;00m)[37m[39;49;00m$
[37m                       [39;49;00m(([32meq[39;49;00m[37m [39;49;00m[31mt[39;49;00m[37m [39;49;00m[31mkeep-pred[39;49;00m)[37m[39;49;00m$
[37m                        [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31mthis-command[39;49;00m[37m[39;49;00m$
[37m                            [39;49;00m([32mlookup-key[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m([32mthis-command-keys-vector[39;49;00m))))[37m[39;49;00m$
[37m                       [39;49;00m([31mt[39;49;00m[37m [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mkeep-pred[39;49;00m)))[37m[39;49;00m$
[37m                [39;49;00m([32mfuncall[39;49;00m[37m [39;49;00m[31mexitfun[39;49;00m)))))[37m[39;49;00m$
[37m    [39;49;00m([31madd-hook[39;49;00m[37m [39;49;00m[33m'pre-command-hook[39;49;00m[37m [39;49;00m[31mclearfun[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([31minternal-push-keymap[39;49;00m[37m [39;49;00m[31mmap[39;49;00m[37m [39;49;00m[33m'overriding-terminal-local-map[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m[31mexitfun[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
[37m;;;; Progress reporters.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m;; Progress reporter has the following structure:[39;49;00m[37m[39;49;00m$
[37m;;[39;49;00m[37m[39;49;00m$
[37m;;^I(NEXT-UPDATE-VALUE . [NEXT-UPDATE-TIME[39;49;00m[37m[39;49;00m$
[37m;;^I^I^I      MIN-VALUE[39;49;00m[37m[39;49;00m$
[37m;;^I^I^I      MAX-VALUE[39;49;00m[37m[39;49;00m$
[37m;;^I^I^I      MESSAGE[39;49;00m[37m[39;49;00m$
[37m;;^I^I^I      MIN-CHANGE[39;49;00m[37m[39;49;00m$
[37m;;^I^I^I      MIN-TIME])[39;49;00m[37m[39;49;00m$
[37m;;[39;49;00m[37m[39;49;00m$
[37m;; This weirdness is for optimization reasons: we want[39;49;00m[37m[39;49;00m$
[37m;; `progress-reporter-update' to be as fast as possible, so[39;49;00m[37m[39;49;00m$
[37m;; `(car reporter)' is better than `(aref reporter 0)'.[39;49;00m[37m[39;49;00m$
[37m;;[39;49;00m[37m[39;49;00m$
[37m;; NEXT-UPDATE-TIME is a float.  While `float-time' loses a couple[39;49;00m[37m[39;49;00m$
[37m;; digits of precision, it doesn't really matter here.  On the other[39;49;00m[37m[39;49;00m$
[37m;; hand, it greatly simplifies the code.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
([36mdefsubst[39;49;00m[37m [39;49;00m[31mprogress-reporter-update[39;49;00m[37m [39;49;00m([31mreporter[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mvalue[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReport progress of an operation in the echo area.[39;49;00m$
[33mREPORTER should be the result of a call to [39;49;00m[33m`make-progress-reporter'[39;49;00m[33m.[39;49;00m$
[33m[39;49;00m$
[33mIf REPORTER is a numerical progress reporter---i.e. if it was[39;49;00m$
[33m made using non-nil MIN-VALUE and MAX-VALUE arguments to[39;49;00m$
[33m [39;49;00m[33m`make-progress-reporter'[39;49;00m[33m---then VALUE should be a number between[39;49;00m$
[33m MIN-VALUE and MAX-VALUE.[39;49;00m$
[33m[39;49;00m$
[33mIf REPORTER is a non-numerical reporter, VALUE should be nil.[39;49;00m$
[33m[39;49;00m$
[33mThis function is relatively inexpensive.  If the change since[39;49;00m$
[33mlast update is too small or insufficient time has passed, it does[39;49;00m$
[33mnothing.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mnumberp[39;49;00m[37m [39;49;00m[31mvalue[39;49;00m))[37m      [39;49;00m[37m; For pulsing reporter[39;49;00m[37m[39;49;00m$
[37m^I    [39;49;00m([32m>=[39;49;00m[37m [39;49;00m[31mvalue[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mreporter[39;49;00m)))[37m [39;49;00m[37m; For numerical reporter[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m([31mprogress-reporter-do-update[39;49;00m[37m [39;49;00m[31mreporter[39;49;00m[37m [39;49;00m[31mvalue[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mmake-progress-reporter[39;49;00m[37m [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mmin-value[39;49;00m[37m [39;49;00m[31mmax-value[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I       [39;49;00m[31mcurrent-value[39;49;00m[37m [39;49;00m[31mmin-change[39;49;00m[37m [39;49;00m[31mmin-time[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn progress reporter object for use with [39;49;00m[33m`progress-reporter-update'[39;49;00m[33m.[39;49;00m$
[33m[39;49;00m$
[33mMESSAGE is shown in the echo area, with a status indicator[39;49;00m$
[33mappended to the end.  When you call [39;49;00m[33m`progress-reporter-done'[39;49;00m[33m, the[39;49;00m$
[33mword [39;49;00m[33m\"[39;49;00m[33mdone[39;49;00m[33m\"[39;49;00m[33m is printed after the MESSAGE.  You can change the[39;49;00m$
[33mMESSAGE of an existing progress reporter by calling[39;49;00m$
[33m`progress-reporter-force-update'[39;49;00m[33m.[39;49;00m$
[33m[39;49;00m$
[33mMIN-VALUE and MAX-VALUE, if non-nil, are starting (0% complete)[39;49;00m$
[33mand final (100% complete) states of operation; the latter should[39;49;00m$
[33mbe larger.  In this case, the status message shows the percentage[39;49;00m$
[33mprogress.[39;49;00m$
[33m[39;49;00m$
[33mIf MIN-VALUE and/or MAX-VALUE is omitted or nil, the status[39;49;00m$
[33mmessage shows a [39;49;00m[33m\"[39;49;00m[33mspinning[39;49;00m[33m\"[39;49;00m[33m, non-numeric indicator.[39;49;00m$
[33m[39;49;00m$
[33mOptional CURRENT-VALUE is the initial progress; the default is[39;49;00m$
[33mMIN-VALUE.[39;49;00m$
[33mOptional MIN-CHANGE is the minimal change in percents to report;[39;49;00m$
[33mthe default is 1%.[39;49;00m$
[33mCURRENT-VALUE and MIN-CHANGE do not have any effect if MIN-VALUE[39;49;00m$
[33mand/or MAX-VALUE are nil.[39;49;00m$
[33m[39;49;00m$
[33mOptional MIN-TIME specifies the minimum interval time between[39;49;00m$
[33mecho area updates (default is 0.2 seconds.)  If the function[39;49;00m$
[33m`float-time'[39;49;00m[33m is not present, time is not tracked at all.  If the[39;49;00m$
[33mOS is not capable of measuring fractions of seconds, this[39;49;00m$
[33mparameter is effectively rounded up.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m[[:alnum:]][39;49;00m[33m\\[39;49;00m[33m'[39;49;00m[33m"[39;49;00m[37m [39;49;00m[32mmessage[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[32mmessage[39;49;00m[37m [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[32mmessage[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m...[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
[37m  [39;49;00m([36munless[39;49;00m[37m [39;49;00m[31mmin-time[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mmin-time[39;49;00m[37m [39;49;00m[34m0.2[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mreporter[39;49;00m[37m[39;49;00m$
[37m^I [39;49;00m[37m;; Force a call to `message' now[39;49;00m[37m[39;49;00m$
[37m^I [39;49;00m([32mcons[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mmin-value[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m^I       [39;49;00m([32mvector[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mfboundp[39;49;00m[37m [39;49;00m[33m'float-time[39;49;00m)[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m([32m>=[39;49;00m[37m [39;49;00m[31mmin-time[39;49;00m[37m [39;49;00m[34m0.02[39;49;00m))[37m[39;49;00m$
[37m^I^I^I   [39;49;00m([32mfloat-time[39;49;00m)[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
[37m^I^I       [39;49;00m[31mmin-value[39;49;00m[37m[39;49;00m$
[37m^I^I       [39;49;00m[31mmax-value[39;49;00m[37m[39;49;00m$
[37m^I^I       [39;49;00m[32mmessage[39;49;00m[37m[39;49;00m$
[37m^I^I       [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mmin-change[39;49;00m[37m [39;49;00m([32mmax[39;49;00m[37m [39;49;00m([32mmin[39;49;00m[37m [39;49;00m[31mmin-change[39;49;00m[37m [39;49;00m[34m50[39;49;00m)[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m[34m1[39;49;00m)[37m[39;49;00m$
[37m^I^I       [39;49;00m[31mmin-time[39;49;00m))))[37m[39;49;00m$
[37m    [39;49;00m([31mprogress-reporter-update[39;49;00m[37m [39;49;00m[31mreporter[39;49;00m[37m [39;49;00m([34mor[39;49;00m[37m [39;49;00m[31mcurrent-value[39;49;00m[37m [39;49;00m[31mmin-value[39;49;00m))[37m[39;49;00m$
[37m    [39;49;00m[31mreporter[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mprogress-reporter-force-update[39;49;00m[37m [39;49;00m([31mreporter[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mvalue[39;49;00m[37m [39;49;00m[31mnew-message[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReport progress of an operation in the echo area unconditionally.[39;49;00m$
[33m[39;49;00m$
[33mThe first two arguments are the same as in [39;49;00m[33m`progress-reporter-update'[39;49;00m[33m.[39;49;00m$
[33mNEW-MESSAGE, if non-nil, sets a new message for the reporter.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mparameters[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mreporter[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31mnew-message[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([32maset[39;49;00m[37m [39;49;00m[31mparameters[39;49;00m[37m [39;49;00m[34m3[39;49;00m[37m [39;49;00m[31mnew-message[39;49;00m))[37m[39;49;00m$
[37m    [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32maref[39;49;00m[37m [39;49;00m[31mparameters[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m([32maset[39;49;00m[37m [39;49;00m[31mparameters[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m([32mfloat-time[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m([31mprogress-reporter-do-update[39;49;00m[37m [39;49;00m[31mreporter[39;49;00m[37m [39;49;00m[31mvalue[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
([34mdefvar[39;49;00m[37m [39;49;00m[31mprogress-reporter--pulse-characters[39;49;00m[37m [39;49;00m[[33m"[39;49;00m[33m-[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m|[39;49;00m[33m"[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m/[39;49;00m[33m"[39;49;00m][37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mCharacters to use for pulsing progress reporters.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mprogress-reporter-do-update[39;49;00m[37m [39;49;00m([31mreporter[39;49;00m[37m [39;49;00m[31mvalue[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mparameters[39;49;00m[37m   [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mreporter[39;49;00m))[37m[39;49;00m$
[37m^I [39;49;00m([31mupdate-time[39;49;00m[37m  [39;49;00m([32maref[39;49;00m[37m [39;49;00m[31mparameters[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m$
[37m^I [39;49;00m([31mmin-value[39;49;00m[37m    [39;49;00m([32maref[39;49;00m[37m [39;49;00m[31mparameters[39;49;00m[37m [39;49;00m[34m1[39;49;00m))[37m[39;49;00m$
[37m^I [39;49;00m([31mmax-value[39;49;00m[37m    [39;49;00m([32maref[39;49;00m[37m [39;49;00m[31mparameters[39;49;00m[37m [39;49;00m[34m2[39;49;00m))[37m[39;49;00m$
[37m^I [39;49;00m([31mtext[39;49;00m[37m         [39;49;00m([32maref[39;49;00m[37m [39;49;00m[31mparameters[39;49;00m[37m [39;49;00m[34m3[39;49;00m))[37m[39;49;00m$
[37m^I [39;49;00m([31menough-time-passed[39;49;00m[37m[39;49;00m$
[37m^I  [39;49;00m[37m;; See if enough time has passed since the last update.[39;49;00m[37m[39;49;00m$
[37m^I  [39;49;00m([34mor[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m[31mupdate-time[39;49;00m)[37m[39;49;00m$
[37m^I      [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32m>=[39;49;00m[37m [39;49;00m([32mfloat-time[39;49;00m)[37m [39;49;00m[31mupdate-time[39;49;00m)[37m[39;49;00m$
[37m^I^I[39;49;00m[37m;; Calculate time for the next update[39;49;00m[37m[39;49;00m$
[37m^I^I[39;49;00m([32maset[39;49;00m[37m [39;49;00m[31mparameters[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m([32m+[39;49;00m[37m [39;49;00m[31mupdate-time[39;49;00m[37m [39;49;00m([32maref[39;49;00m[37m [39;49;00m[31mparameters[39;49;00m[37m [39;49;00m[34m5[39;49;00m)))))))[37m[39;49;00m$
[37m    [39;49;00m([34mcond[39;49;00m[37m [39;49;00m(([34mand[39;49;00m[37m [39;49;00m[31mmin-value[39;49;00m[37m [39;49;00m[31mmax-value[39;49;00m)[37m[39;49;00m$
[37m^I   [39;49;00m[37m;; Numerical indicator[39;49;00m[37m[39;49;00m$
[37m^I   [39;49;00m([34mlet*[39;49;00m[37m [39;49;00m(([31mone-percent[39;49;00m[37m [39;49;00m([32m/[39;49;00m[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m[31mmax-value[39;49;00m[37m [39;49;00m[31mmin-value[39;49;00m)[37m [39;49;00m[34m100.0[39;49;00m))[37m[39;49;00m$
[37m^I^I  [39;49;00m([31mpercentage[39;49;00m[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32m=[39;49;00m[37m [39;49;00m[31mmax-value[39;49;00m[37m [39;49;00m[31mmin-value[39;49;00m)[37m[39;49;00m$
[37m^I^I^I^I   [39;49;00m[34m0[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I [39;49;00m([32mtruncate[39;49;00m[37m [39;49;00m([32m/[39;49;00m[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m[31mvalue[39;49;00m[37m [39;49;00m[31mmin-value[39;49;00m)[37m[39;49;00m$
[37m^I^I^I^I^I      [39;49;00m[31mone-percent[39;49;00m)))))[37m[39;49;00m$
[37m^I     [39;49;00m[37m;; Calculate NEXT-UPDATE-VALUE.  If we are not printing[39;49;00m[37m[39;49;00m$
[37m^I     [39;49;00m[37m;; message because not enough time has passed, use 1[39;49;00m[37m[39;49;00m$
[37m^I     [39;49;00m[37m;; instead of MIN-CHANGE.  This makes delays between echo[39;49;00m[37m[39;49;00m$
[37m^I     [39;49;00m[37m;; area updates closer to MIN-TIME.[39;49;00m[37m[39;49;00m$
[37m^I     [39;49;00m([32msetcar[39;49;00m[37m [39;49;00m[31mreporter[39;49;00m[37m[39;49;00m$
[37m^I^I     [39;49;00m([32mmin[39;49;00m[37m [39;49;00m([32m+[39;49;00m[37m [39;49;00m[31mmin-value[39;49;00m[37m [39;49;00m([32m*[39;49;00m[37m [39;49;00m([32m+[39;49;00m[37m [39;49;00m[31mpercentage[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I^I     [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31menough-time-passed[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I^I^I [39;49;00m[37m;; MIN-CHANGE[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I^I^I [39;49;00m([32maref[39;49;00m[37m [39;49;00m[31mparameters[39;49;00m[37m [39;49;00m[34m4[39;49;00m)[37m[39;49;00m$
[37m^I^I^I^I^I       [39;49;00m[34m1[39;49;00m))[37m[39;49;00m$
[37m^I^I^I^I^I  [39;49;00m[31mone-percent[39;49;00m))[37m[39;49;00m$
[37m^I^I^I  [39;49;00m[31mmax-value[39;49;00m))[37m[39;49;00m$
[37m^I     [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([32mintegerp[39;49;00m[37m [39;49;00m[31mvalue[39;49;00m)[37m[39;49;00m$
[37m^I       [39;49;00m([32msetcar[39;49;00m[37m [39;49;00m[31mreporter[39;49;00m[37m [39;49;00m([32mceiling[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mreporter[39;49;00m))))[37m[39;49;00m$
[37m^I     [39;49;00m[37m;; Only print message if enough time has passed[39;49;00m[37m[39;49;00m$
[37m^I     [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m[31menough-time-passed[39;49;00m[37m[39;49;00m$
[37m^I       [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m[31mpercentage[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m^I^I   [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m%s%d%%[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mtext[39;49;00m[37m [39;49;00m[31mpercentage[39;49;00m)[37m[39;49;00m$
[37m^I^I [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m%s[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mtext[39;49;00m)))))[37m[39;49;00m$
[37m^I  [39;49;00m[37m;; Pulsing indicator[39;49;00m[37m[39;49;00m$
[37m^I  [39;49;00m([31menough-time-passed[39;49;00m[37m[39;49;00m$
[37m^I   [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mindex[39;49;00m[37m [39;49;00m([32mmod[39;49;00m[37m [39;49;00m([32m1+[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mreporter[39;49;00m))[37m [39;49;00m[34m4[39;49;00m))[37m[39;49;00m$
[37m^I^I [39;49;00m([31mmessage-log-max[39;49;00m[37m [39;49;00m[31mnil[39;49;00m))[37m[39;49;00m$
[37m^I     [39;49;00m([32msetcar[39;49;00m[37m [39;49;00m[31mreporter[39;49;00m[37m [39;49;00m[31mindex[39;49;00m)[37m[39;49;00m$
[37m^I     [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m%s %s[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m^I^I      [39;49;00m[31mtext[39;49;00m[37m[39;49;00m$
[37m^I^I      [39;49;00m([32maref[39;49;00m[37m [39;49;00m[31mprogress-reporter--pulse-characters[39;49;00m[37m[39;49;00m$
[37m^I^I^I    [39;49;00m[31mindex[39;49;00m)))))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mprogress-reporter-done[39;49;00m[37m [39;49;00m([31mreporter[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mPrint reporter's message followed by word [39;49;00m[33m\"[39;49;00m[33mdone[39;49;00m[33m\"[39;49;00m[33m in echo area.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([32mmessage[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m%sdone[39;49;00m[33m"[39;49;00m[37m [39;49;00m([32maref[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mreporter[39;49;00m)[37m [39;49;00m[34m3[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefmacro[39;49;00m[37m [39;49;00m[36mdotimes-with-progress-reporter[39;49;00m[37m [39;49;00m([31mspec[39;49;00m[37m [39;49;00m[32mmessage[39;49;00m[37m [39;49;00m[34m&rest[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mLoop a certain number of times and report progress in the echo area.[39;49;00m$
[33mEvaluate BODY with VAR bound to successive integers running from[39;49;00m$
[33m0, inclusive, to COUNT, exclusive.  Then evaluate RESULT to get[39;49;00m$
[33mthe return value (nil if RESULT is omitted).[39;49;00m$
[33m[39;49;00m$
[33mAt each iteration MESSAGE followed by progress percentage is[39;49;00m$
[33mprinted in the echo area.  After the loop is finished, MESSAGE[39;49;00m$
[33mfollowed by word [39;49;00m[33m\"[39;49;00m[33mdone[39;49;00m[33m\"[39;49;00m[33m is printed.  This macro is a[39;49;00m$
[33mconvenience wrapper around [39;49;00m[33m`make-progress-reporter'[39;49;00m[33m and friends.[39;49;00m$
[33m[39;49;00m$
[33m\([39;49;00m[33mfn (VAR COUNT [RESULT]) MESSAGE BODY...)[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mdeclare[39;49;00m[37m [39;49;00m([31mindent[39;49;00m[37m [39;49;00m[34m2[39;49;00m)[37m [39;49;00m([31mdebug[39;49;00m[37m [39;49;00m(([32msymbolp[39;49;00m[37m [39;49;00m[31mform[39;49;00m[37m [39;49;00m[34m&optional[39;49;00m[37m [39;49;00m[31mform[39;49;00m)[37m [39;49;00m[31mform[39;49;00m[37m [39;49;00m[31mbody[39;49;00m)))[37m[39;49;00m$
[37m  [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mtemp[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m--dotimes-temp--[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
[37m^I[39;49;00m([31mtemp2[39;49;00m[37m [39;49;00m([32mmake-symbol[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m--dotimes-temp2--[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
[37m^I[39;49;00m([31mstart[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m^I[39;49;00m([31mend[39;49;00m[37m [39;49;00m([32mnth[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m`([34mlet[39;49;00m[37m [39;49;00m((,[31mtemp[39;49;00m[37m [39;49;00m,[31mend[39;49;00m)[37m[39;49;00m$
[37m^I   [39;49;00m(,([32mcar[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)[37m [39;49;00m,[31mstart[39;49;00m)[37m[39;49;00m$
[37m^I   [39;49;00m(,[31mtemp2[39;49;00m[37m [39;49;00m([31mmake-progress-reporter[39;49;00m[37m [39;49;00m,[32mmessage[39;49;00m[37m [39;49;00m,[31mstart[39;49;00m[37m [39;49;00m,[31mend[39;49;00m)))[37m[39;49;00m$
[37m       [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m,([32mcar[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)[37m [39;49;00m,[31mtemp[39;49;00m)[37m[39;49;00m$
[37m^I [39;49;00m,@[31mbody[39;49;00m[37m[39;49;00m$
[37m^I [39;49;00m([31mprogress-reporter-update[39;49;00m[37m [39;49;00m,[31mtemp2[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I   [39;49;00m([34msetq[39;49;00m[37m [39;49;00m,([32mcar[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)[37m [39;49;00m([32m1+[39;49;00m[37m [39;49;00m,([32mcar[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)))))[37m[39;49;00m$
[37m       [39;49;00m([31mprogress-reporter-done[39;49;00m[37m [39;49;00m,[31mtemp2[39;49;00m)[37m[39;49;00m$
[37m       [39;49;00m[31mnil[39;49;00m[37m [39;49;00m,@([32mcdr[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mspec[39;49;00m)))))[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m[37m[39;49;00m$
[37m;;;; Comparing version strings.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
([34mdefconst[39;49;00m[37m [39;49;00m[31mversion-separator[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mSpecify the string used to separate the version elements.[39;49;00m$
[33m[39;49;00m$
[33mUsually the separator is [39;49;00m[33m\"[39;49;00m[33m.[39;49;00m[33m\"[39;49;00m[33m, but it can be any other string.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
([34mdefconst[39;49;00m[37m [39;49;00m[31mversion-regexp-alist[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m'(([33m"[39;49;00m[33m^[-_+ ]?snapshot$[39;49;00m[33m"[39;49;00m[37m                                 [39;49;00m.[37m [39;49;00m[34m-4[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m[37m;; treat "1.2.3-20050920" and "1.2-3" as snapshot releases[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m([33m"[39;49;00m[33m^[-_+]$[39;49;00m[33m"[39;49;00m[37m                                           [39;49;00m.[37m [39;49;00m[34m-4[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m[37m;; treat "1.2.3-CVS" as snapshot release[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m([33m"[39;49;00m[33m^[-_+ ]?[39;49;00m[33m\\[39;49;00m[33m(cvs[39;49;00m[33m\\[39;49;00m[33m|git[39;49;00m[33m\\[39;49;00m[33m|bzr[39;49;00m[33m\\[39;49;00m[33m|svn[39;49;00m[33m\\[39;49;00m[33m|hg[39;49;00m[33m\\[39;49;00m[33m|darcs[39;49;00m[33m\\[39;49;00m[33m)$[39;49;00m[33m"[39;49;00m[37m [39;49;00m.[37m [39;49;00m[34m-4[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([33m"[39;49;00m[33m^[-_+ ]?alpha$[39;49;00m[33m"[39;49;00m[37m                                    [39;49;00m.[37m [39;49;00m[34m-3[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([33m"[39;49;00m[33m^[-_+ ]?beta$[39;49;00m[33m"[39;49;00m[37m                                     [39;49;00m.[37m [39;49;00m[34m-2[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m([33m"[39;49;00m[33m^[-_+ ]?[39;49;00m[33m\\[39;49;00m[33m(pre[39;49;00m[33m\\[39;49;00m[33m|rc[39;49;00m[33m\\[39;49;00m[33m)$[39;49;00m[33m"[39;49;00m[37m                           [39;49;00m.[37m [39;49;00m[34m-1[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mSpecify association between non-numeric version and its priority.[39;49;00m$
[33m[39;49;00m$
[33mThis association is used to handle version string like [39;49;00m[33m\"[39;49;00m[33m1.0pre2[39;49;00m[33m\"[39;49;00m[33m,[39;49;00m$
[33m\"[39;49;00m[33m0.9alpha1[39;49;00m[33m\"[39;49;00m[33m, etc.  It's used by [39;49;00m[33m`version-to-list'[39;49;00m[33m (which see) to convert the[39;49;00m$
[33mnon-numeric part of a version string to an integer.  For example:[39;49;00m$
[33m[39;49;00m$
[33m   String Version    Integer List Version[39;49;00m$
[33m   [39;49;00m[33m\"[39;49;00m[33m0.9snapshot[39;49;00m[33m\"[39;49;00m[33m     (0  9 -4)[39;49;00m$
[33m   [39;49;00m[33m\"[39;49;00m[33m1.0-git[39;49;00m[33m\"[39;49;00m[33m         (1  0 -4)[39;49;00m$
[33m   [39;49;00m[33m\"[39;49;00m[33m1.0pre2[39;49;00m[33m\"[39;49;00m[33m         (1  0 -1 2)[39;49;00m$
[33m   [39;49;00m[33m\"[39;49;00m[33m1.0PRE2[39;49;00m[33m\"[39;49;00m[33m         (1  0 -1 2)[39;49;00m$
[33m   [39;49;00m[33m\"[39;49;00m[33m22.8beta3[39;49;00m[33m\"[39;49;00m[33m       (22 8 -2 3)[39;49;00m$
[33m   [39;49;00m[33m\"[39;49;00m[33m22.8 Beta3[39;49;00m[33m\"[39;49;00m[33m      (22 8 -2 3)[39;49;00m$
[33m   [39;49;00m[33m\"[39;49;00m[33m0.9alpha1[39;49;00m[33m\"[39;49;00m[33m       (0  9 -3 1)[39;49;00m$
[33m   [39;49;00m[33m\"[39;49;00m[33m0.9AlphA1[39;49;00m[33m\"[39;49;00m[33m       (0  9 -3 1)[39;49;00m$
[33m   [39;49;00m[33m\"[39;49;00m[33m0.9 alpha[39;49;00m[33m\"[39;49;00m[33m       (0  9 -3)[39;49;00m$
[33m[39;49;00m$
[33mEach element has the following form:[39;49;00m$
[33m[39;49;00m$
[33m   (REGEXP . PRIORITY)[39;49;00m$
[33m[39;49;00m$
[33mWhere:[39;49;00m$
[33m[39;49;00m$
[33mREGEXP^I^Iregexp used to match non-numeric part of a version string.[39;49;00m$
[33m^I^IIt should begin with the [39;49;00m[33m`^'[39;49;00m[33m anchor and end with a [39;49;00m[33m`$'[39;49;00m[33m to[39;49;00m$
[33m^I^Iprevent false hits.  Letter-case is ignored while matching[39;49;00m$
[33m^I^IREGEXP.[39;49;00m$
[33m[39;49;00m$
[33mPRIORITY^Ia negative integer specifying non-numeric priority of REGEXP.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mversion-to-list[39;49;00m[37m [39;49;00m([31mver[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mConvert version string VER into a list of integers.[39;49;00m$
[33m[39;49;00m$
[33mThe version syntax is given by the following EBNF:[39;49;00m$
[33m[39;49;00m$
[33m   VERSION ::= NUMBER ( SEPARATOR NUMBER )*.[39;49;00m$
[33m[39;49;00m$
[33m   NUMBER ::= (0|1|2|3|4|5|6|7|8|9)+.[39;49;00m$
[33m[39;49;00m$
[33m   SEPARATOR ::= [39;49;00m[33m`version-separator'[39;49;00m[33m (which see)[39;49;00m$
[33m^I       | [39;49;00m[33m`version-regexp-alist'[39;49;00m[33m (which see).[39;49;00m$
[33m[39;49;00m$
[33mThe NUMBER part is optional if SEPARATOR is a match for an element[39;49;00m$
[33min [39;49;00m[33m`version-regexp-alist'[39;49;00m[33m.[39;49;00m$
[33m[39;49;00m$
[33mExamples of valid version syntax:[39;49;00m$
[33m[39;49;00m$
[33m   1.0pre2   1.0.7.5   22.8beta3   0.9alpha1   6.9.30Beta[39;49;00m$
[33m[39;49;00m$
[33mExamples of invalid version syntax:[39;49;00m$
[33m[39;49;00m$
[33m   1.0prepre2   1.0..7.5   22.8X3   alpha3.2   .5[39;49;00m$
[33m[39;49;00m$
[33mExamples of version conversion:[39;49;00m$
[33m[39;49;00m$
[33m   Version String    Version as a List of Integers[39;49;00m$
[33m   [39;49;00m[33m\"[39;49;00m[33m1.0.7.5[39;49;00m[33m\"[39;49;00m[33m         (1  0  7 5)[39;49;00m$
[33m   [39;49;00m[33m\"[39;49;00m[33m1.0pre2[39;49;00m[33m\"[39;49;00m[33m         (1  0 -1 2)[39;49;00m$
[33m   [39;49;00m[33m\"[39;49;00m[33m1.0PRE2[39;49;00m[33m\"[39;49;00m[33m         (1  0 -1 2)[39;49;00m$
[33m   [39;49;00m[33m\"[39;49;00m[33m22.8beta3[39;49;00m[33m\"[39;49;00m[33m       (22 8 -2 3)[39;49;00m$
[33m   [39;49;00m[33m\"[39;49;00m[33m22.8Beta3[39;49;00m[33m\"[39;49;00m[33m       (22 8 -2 3)[39;49;00m$
[33m   [39;49;00m[33m\"[39;49;00m[33m0.9alpha1[39;49;00m[33m\"[39;49;00m[33m       (0  9 -3 1)[39;49;00m$
[33m   [39;49;00m[33m\"[39;49;00m[33m0.9AlphA1[39;49;00m[33m\"[39;49;00m[33m       (0  9 -3 1)[39;49;00m$
[33m   [39;49;00m[33m\"[39;49;00m[33m0.9alpha[39;49;00m[33m\"[39;49;00m[33m        (0  9 -3)[39;49;00m$
[33m   [39;49;00m[33m\"[39;49;00m[33m0.9snapshot[39;49;00m[33m\"[39;49;00m[33m     (0  9 -4)[39;49;00m$
[33m   [39;49;00m[33m\"[39;49;00m[33m1.0-git[39;49;00m[33m\"[39;49;00m[33m         (1  0 -4)[39;49;00m$
[33m[39;49;00m$
[33mSee documentation for [39;49;00m[33m`version-separator'[39;49;00m[33m and [39;49;00m[33m`version-regexp-alist'[39;49;00m[33m.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mor[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32mstringp[39;49;00m[37m [39;49;00m[31mver[39;49;00m)[37m [39;49;00m([32m>[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31mver[39;49;00m)[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m$
[37m      [39;49;00m([36merror[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mInvalid version string: '%s'[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mver[39;49;00m))[37m[39;49;00m$
[37m  [39;49;00m[37m;; Change .x.y to 0.x.y[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32m>=[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31mver[39;49;00m)[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31mversion-separator[39;49;00m))[37m[39;49;00m$
[37m^I   [39;49;00m([32mstring-equal[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[31mver[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m([32mlength[39;49;00m[37m [39;49;00m[31mversion-separator[39;49;00m))[37m[39;49;00m$
[37m^I^I^I [39;49;00m[31mversion-separator[39;49;00m))[37m[39;49;00m$
[37m      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mver[39;49;00m[37m [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m0[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mver[39;49;00m)))[37m[39;49;00m$
[37m  [39;49;00m([36msave-match-data[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31mi[39;49;00m[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m^I  [39;49;00m([31mcase-fold-search[39;49;00m[37m [39;49;00m[31mt[39;49;00m)[37m^I^I[39;49;00m[37m; ignore case in matching[39;49;00m[37m[39;49;00m$
[37m^I  [39;49;00m[31mlst[39;49;00m[37m [39;49;00m[31ms[39;49;00m[37m [39;49;00m[31mal[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31ms[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m[0-9]+[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mver[39;49;00m[37m [39;49;00m[31mi[39;49;00m))[37m[39;49;00m$
[37m^I^I  [39;49;00m([32m=[39;49;00m[37m [39;49;00m[31ms[39;49;00m[37m [39;49;00m[31mi[39;49;00m))[37m[39;49;00m$
[37m^I[39;49;00m[37m;; handle numeric part[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mlst[39;49;00m[37m [39;49;00m([32mcons[39;49;00m[37m [39;49;00m([32mstring-to-number[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[31mver[39;49;00m[37m [39;49;00m[31mi[39;49;00m[37m [39;49;00m([32mmatch-end[39;49;00m[37m [39;49;00m[34m0[39;49;00m)))[37m[39;49;00m$
[37m^I^I^I[39;49;00m[31mlst[39;49;00m)[37m[39;49;00m$
[37m^I      [39;49;00m[31mi[39;49;00m[37m   [39;49;00m([32mmatch-end[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m$
[37m^I[39;49;00m[37m;; handle non-numeric part[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31ms[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m[^0-9]+[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mver[39;49;00m[37m [39;49;00m[31mi[39;49;00m))[37m[39;49;00m$
[37m^I^I   [39;49;00m([32m=[39;49;00m[37m [39;49;00m[31ms[39;49;00m[37m [39;49;00m[31mi[39;49;00m))[37m[39;49;00m$
[37m^I  [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31ms[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[31mver[39;49;00m[37m [39;49;00m[31mi[39;49;00m[37m [39;49;00m([32mmatch-end[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m$
[37m^I^I[39;49;00m[31mi[39;49;00m[37m [39;49;00m([32mmatch-end[39;49;00m[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m$
[37m^I  [39;49;00m[37m;; handle alpha, beta, pre, etc. separator[39;49;00m[37m[39;49;00m$
[37m^I  [39;49;00m([36munless[39;49;00m[37m [39;49;00m([32mstring=[39;49;00m[37m [39;49;00m[31ms[39;49;00m[37m [39;49;00m[31mversion-separator[39;49;00m)[37m[39;49;00m$
[37m^I    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mal[39;49;00m[37m [39;49;00m[31mversion-regexp-alist[39;49;00m)[37m[39;49;00m$
[37m^I    [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mal[39;49;00m[37m [39;49;00m([31mnot[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m([31mcaar[39;49;00m[37m [39;49;00m[31mal[39;49;00m)[37m [39;49;00m[31ms[39;49;00m)))[37m[39;49;00m$
[37m^I      [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mal[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mal[39;49;00m)))[37m[39;49;00m$
[37m^I    [39;49;00m([34mcond[39;49;00m[37m [39;49;00m([31mal[39;49;00m[37m[39;49;00m$
[37m^I^I   [39;49;00m([36mpush[39;49;00m[37m [39;49;00m([31mcdar[39;49;00m[37m [39;49;00m[31mal[39;49;00m)[37m [39;49;00m[31mlst[39;49;00m))[37m[39;49;00m$
[37m^I^I  [39;49;00m[37m;; Convert 22.3a to 22.3.1, 22.3b to 22.3.2, etc.[39;49;00m[37m[39;49;00m$
[37m^I^I  [39;49;00m(([32mstring-match[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m^[-_+ ]?[39;49;00m[33m\\[39;49;00m[33m([a-zA-Z][39;49;00m[33m\\[39;49;00m[33m)$[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31ms[39;49;00m)[37m[39;49;00m$
[37m^I^I   [39;49;00m([36mpush[39;49;00m[37m [39;49;00m([32m-[39;49;00m[37m [39;49;00m([32maref[39;49;00m[37m [39;49;00m([32mdowncase[39;49;00m[37m [39;49;00m([31mmatch-string[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31ms[39;49;00m))[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[33m?a[39;49;00m[37m [39;49;00m[34m-1[39;49;00m)[37m[39;49;00m$
[37m^I^I^I [39;49;00m[31mlst[39;49;00m))[37m[39;49;00m$
[37m^I^I  [39;49;00m([31mt[39;49;00m[37m [39;49;00m([36merror[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mInvalid version syntax: '%s'[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mver[39;49;00m))))))[37m[39;49;00m$
[37m      [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[31mlst[39;49;00m)[37m[39;49;00m$
[37m^I  [39;49;00m([36merror[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mInvalid version syntax: '%s'[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mver[39;49;00m)[37m[39;49;00m$
[37m^I[39;49;00m([32mnreverse[39;49;00m[37m [39;49;00m[31mlst[39;49;00m)))))[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mversion-list-<[39;49;00m[37m [39;49;00m([31ml1[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn t if L1, a list specification of a version, is lower than L2.[39;49;00m$
[33m[39;49;00m$
[33mNote that a version specified by the list (1) is equal to (1 0),[39;49;00m$
[33m\([39;49;00m[33m1 0 0), (1 0 0 0), etc.  That is, the trailing zeros are insignificant.[39;49;00m$
[33mAlso, a version given by the list (1) is higher than (1 -1), which in[39;49;00m$
[33mturn is higher than (1 -2), which is higher than (1 -3).[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31ml1[39;49;00m[37m [39;49;00m[31ml2[39;49;00m[37m [39;49;00m([32m=[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31ml1[39;49;00m)[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31ml1[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31ml1[39;49;00m)[37m[39;49;00m$
[37m^I  [39;49;00m[31ml2[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)))[37m[39;49;00m$
[37m  [39;49;00m([34mcond[39;49;00m[37m[39;49;00m$
[37m   [39;49;00m[37m;; l1 not null and l2 not null[39;49;00m[37m[39;49;00m$
[37m   [39;49;00m(([34mand[39;49;00m[37m [39;49;00m[31ml1[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31ml1[39;49;00m)[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)))[37m[39;49;00m$
[37m   [39;49;00m[37m;; l1 null and l2 null         ==> l1 length = l2 length[39;49;00m[37m[39;49;00m$
[37m   [39;49;00m(([34mand[39;49;00m[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[31ml1[39;49;00m)[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[31ml2[39;49;00m))[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
[37m   [39;49;00m[37m;; l1 not null and l2 null     ==> l1 length > l2 length[39;49;00m[37m[39;49;00m$
[37m   [39;49;00m([31ml1[39;49;00m[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m([31mversion-list-not-zero[39;49;00m[37m [39;49;00m[31ml1[39;49;00m)[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m$
[37m   [39;49;00m[37m;; l1 null and l2 not null     ==> l2 length > l1 length[39;49;00m[37m[39;49;00m$
[37m   [39;49;00m([31mt[39;49;00m[37m  [39;49;00m([32m<[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m([31mversion-list-not-zero[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)))))[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mversion-list-=[39;49;00m[37m [39;49;00m([31ml1[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn t if L1, a list specification of a version, is equal to L2.[39;49;00m$
[33m[39;49;00m$
[33mNote that a version specified by the list (1) is equal to (1 0),[39;49;00m$
[33m\([39;49;00m[33m1 0 0), (1 0 0 0), etc.  That is, the trailing zeros are insignificant.[39;49;00m$
[33mAlso, a version given by the list (1) is higher than (1 -1), which in[39;49;00m$
[33mturn is higher than (1 -2), which is higher than (1 -3).[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31ml1[39;49;00m[37m [39;49;00m[31ml2[39;49;00m[37m [39;49;00m([32m=[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31ml1[39;49;00m)[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31ml1[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31ml1[39;49;00m)[37m[39;49;00m$
[37m^I  [39;49;00m[31ml2[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)))[37m[39;49;00m$
[37m  [39;49;00m([34mcond[39;49;00m[37m[39;49;00m$
[37m   [39;49;00m[37m;; l1 not null and l2 not null[39;49;00m[37m[39;49;00m$
[37m   [39;49;00m(([34mand[39;49;00m[37m [39;49;00m[31ml1[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)[37m [39;49;00m[31mnil[39;49;00m)[37m[39;49;00m$
[37m   [39;49;00m[37m;; l1 null and l2 null     ==> l1 length = l2 length[39;49;00m[37m[39;49;00m$
[37m   [39;49;00m(([34mand[39;49;00m[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[31ml1[39;49;00m)[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)))[37m[39;49;00m$
[37m   [39;49;00m[37m;; l1 not null and l2 null ==> l1 length > l2 length[39;49;00m[37m[39;49;00m$
[37m   [39;49;00m([31ml1[39;49;00m[37m [39;49;00m([31mzerop[39;49;00m[37m [39;49;00m([31mversion-list-not-zero[39;49;00m[37m [39;49;00m[31ml1[39;49;00m)))[37m[39;49;00m$
[37m   [39;49;00m[37m;; l1 null and l2 not null ==> l2 length > l1 length[39;49;00m[37m[39;49;00m$
[37m   [39;49;00m([31mt[39;49;00m[37m  [39;49;00m([31mzerop[39;49;00m[37m [39;49;00m([31mversion-list-not-zero[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)))))[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mversion-list-<=[39;49;00m[37m [39;49;00m([31ml1[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn t if L1, a list specification of a version, is lower or equal to L2.[39;49;00m$
[33m[39;49;00m$
[33mNote that integer list (1) is equal to (1 0), (1 0 0), (1 0 0 0),[39;49;00m$
[33metc.  That is, the trailing zeroes are insignificant.  Also, integer[39;49;00m$
[33mlist (1) is greater than (1 -1) which is greater than (1 -2)[39;49;00m$
[33mwhich is greater than (1 -3).[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31ml1[39;49;00m[37m [39;49;00m[31ml2[39;49;00m[37m [39;49;00m([32m=[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31ml1[39;49;00m)[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31ml1[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31ml1[39;49;00m)[37m[39;49;00m$
[37m^I  [39;49;00m[31ml2[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)))[37m[39;49;00m$
[37m  [39;49;00m([34mcond[39;49;00m[37m[39;49;00m$
[37m   [39;49;00m[37m;; l1 not null and l2 not null[39;49;00m[37m[39;49;00m$
[37m   [39;49;00m(([34mand[39;49;00m[37m [39;49;00m[31ml1[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)[37m [39;49;00m([32m<[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31ml1[39;49;00m)[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)))[37m[39;49;00m$
[37m   [39;49;00m[37m;; l1 null and l2 null     ==> l1 length = l2 length[39;49;00m[37m[39;49;00m$
[37m   [39;49;00m(([34mand[39;49;00m[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[31ml1[39;49;00m)[37m [39;49;00m([32mnull[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)))[37m[39;49;00m$
[37m   [39;49;00m[37m;; l1 not null and l2 null ==> l1 length > l2 length[39;49;00m[37m[39;49;00m$
[37m   [39;49;00m([31ml1[39;49;00m[37m [39;49;00m([32m<=[39;49;00m[37m [39;49;00m([31mversion-list-not-zero[39;49;00m[37m [39;49;00m[31ml1[39;49;00m)[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m$
[37m   [39;49;00m[37m;; l1 null and l2 not null ==> l2 length > l1 length[39;49;00m[37m[39;49;00m$
[37m   [39;49;00m([31mt[39;49;00m[37m  [39;49;00m([32m<=[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m([31mversion-list-not-zero[39;49;00m[37m [39;49;00m[31ml2[39;49;00m)))))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mversion-list-not-zero[39;49;00m[37m [39;49;00m([31mlst[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn the first non-zero element of LST, which is a list of integers.[39;49;00m$
[33m[39;49;00m$
[33mIf all LST elements are zeros or LST is nil, return zero.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([34mwhile[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m[31mlst[39;49;00m[37m [39;49;00m([31mzerop[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mlst[39;49;00m)))[37m[39;49;00m$
[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mlst[39;49;00m[37m [39;49;00m([32mcdr[39;49;00m[37m [39;49;00m[31mlst[39;49;00m)))[37m[39;49;00m$
[37m  [39;49;00m([34mif[39;49;00m[37m [39;49;00m[31mlst[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m([32mcar[39;49;00m[37m [39;49;00m[31mlst[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m[37m;; there is no element different of zero[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[34m0[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mversion<[39;49;00m[37m [39;49;00m([31mv1[39;49;00m[37m [39;49;00m[31mv2[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn t if version V1 is lower (older) than V2.[39;49;00m$
[33m[39;49;00m$
[33mNote that version string [39;49;00m[33m\"[39;49;00m[33m1[39;49;00m[33m\"[39;49;00m[33m is equal to [39;49;00m[33m\"[39;49;00m[33m1.0[39;49;00m[33m\"[39;49;00m[33m, [39;49;00m[33m\"[39;49;00m[33m1.0.0[39;49;00m[33m\"[39;49;00m[33m, [39;49;00m[33m\"[39;49;00m[33m1.0.0.0[39;49;00m[33m\"[39;49;00m[33m,[39;49;00m$
[33metc.  That is, the trailing [39;49;00m[33m\"[39;49;00m[33m.0[39;49;00m[33m\"[39;49;00m[33ms are insignificant.  Also, version[39;49;00m$
[33mstring [39;49;00m[33m\"[39;49;00m[33m1[39;49;00m[33m\"[39;49;00m[33m is higher (newer) than [39;49;00m[33m\"[39;49;00m[33m1pre[39;49;00m[33m\"[39;49;00m[33m, which is higher than [39;49;00m[33m\"[39;49;00m[33m1beta[39;49;00m[33m\"[39;49;00m[33m,[39;49;00m$
[33mwhich is higher than [39;49;00m[33m\"[39;49;00m[33m1alpha[39;49;00m[33m\"[39;49;00m[33m, which is higher than [39;49;00m[33m\"[39;49;00m[33m1snapshot[39;49;00m[33m\"[39;49;00m[33m.[39;49;00m$
[33mAlso, [39;49;00m[33m\"[39;49;00m[33m-GIT[39;49;00m[33m\"[39;49;00m[33m, [39;49;00m[33m\"[39;49;00m[33m-CVS[39;49;00m[33m\"[39;49;00m[33m and [39;49;00m[33m\"[39;49;00m[33m-NNN[39;49;00m[33m\"[39;49;00m[33m are treated as snapshot versions.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([31mversion-list-<[39;49;00m[37m [39;49;00m([31mversion-to-list[39;49;00m[37m [39;49;00m[31mv1[39;49;00m)[37m [39;49;00m([31mversion-to-list[39;49;00m[37m [39;49;00m[31mv2[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mversion<=[39;49;00m[37m [39;49;00m([31mv1[39;49;00m[37m [39;49;00m[31mv2[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn t if version V1 is lower (older) than or equal to V2.[39;49;00m$
[33m[39;49;00m$
[33mNote that version string [39;49;00m[33m\"[39;49;00m[33m1[39;49;00m[33m\"[39;49;00m[33m is equal to [39;49;00m[33m\"[39;49;00m[33m1.0[39;49;00m[33m\"[39;49;00m[33m, [39;49;00m[33m\"[39;49;00m[33m1.0.0[39;49;00m[33m\"[39;49;00m[33m, [39;49;00m[33m\"[39;49;00m[33m1.0.0.0[39;49;00m[33m\"[39;49;00m[33m,[39;49;00m$
[33metc.  That is, the trailing [39;49;00m[33m\"[39;49;00m[33m.0[39;49;00m[33m\"[39;49;00m[33ms are insignificant.  Also, version[39;49;00m$
[33mstring [39;49;00m[33m\"[39;49;00m[33m1[39;49;00m[33m\"[39;49;00m[33m is higher (newer) than [39;49;00m[33m\"[39;49;00m[33m1pre[39;49;00m[33m\"[39;49;00m[33m, which is higher than [39;49;00m[33m\"[39;49;00m[33m1beta[39;49;00m[33m\"[39;49;00m[33m,[39;49;00m$
[33mwhich is higher than [39;49;00m[33m\"[39;49;00m[33m1alpha[39;49;00m[33m\"[39;49;00m[33m, which is higher than [39;49;00m[33m\"[39;49;00m[33m1snapshot[39;49;00m[33m\"[39;49;00m[33m.[39;49;00m$
[33mAlso, [39;49;00m[33m\"[39;49;00m[33m-GIT[39;49;00m[33m\"[39;49;00m[33m, [39;49;00m[33m\"[39;49;00m[33m-CVS[39;49;00m[33m\"[39;49;00m[33m and [39;49;00m[33m\"[39;49;00m[33m-NNN[39;49;00m[33m\"[39;49;00m[33m are treated as snapshot versions.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([31mversion-list-<=[39;49;00m[37m [39;49;00m([31mversion-to-list[39;49;00m[37m [39;49;00m[31mv1[39;49;00m)[37m [39;49;00m([31mversion-to-list[39;49;00m[37m [39;49;00m[31mv2[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mversion=[39;49;00m[37m [39;49;00m([31mv1[39;49;00m[37m [39;49;00m[31mv2[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mReturn t if version V1 is equal to V2.[39;49;00m$
[33m[39;49;00m$
[33mNote that version string [39;49;00m[33m\"[39;49;00m[33m1[39;49;00m[33m\"[39;49;00m[33m is equal to [39;49;00m[33m\"[39;49;00m[33m1.0[39;49;00m[33m\"[39;49;00m[33m, [39;49;00m[33m\"[39;49;00m[33m1.0.0[39;49;00m[33m\"[39;49;00m[33m, [39;49;00m[33m\"[39;49;00m[33m1.0.0.0[39;49;00m[33m\"[39;49;00m[33m,[39;49;00m$
[33metc.  That is, the trailing [39;49;00m[33m\"[39;49;00m[33m.0[39;49;00m[33m\"[39;49;00m[33ms are insignificant.  Also, version[39;49;00m$
[33mstring [39;49;00m[33m\"[39;49;00m[33m1[39;49;00m[33m\"[39;49;00m[33m is higher (newer) than [39;49;00m[33m\"[39;49;00m[33m1pre[39;49;00m[33m\"[39;49;00m[33m, which is higher than [39;49;00m[33m\"[39;49;00m[33m1beta[39;49;00m[33m\"[39;49;00m[33m,[39;49;00m$
[33mwhich is higher than [39;49;00m[33m\"[39;49;00m[33m1alpha[39;49;00m[33m\"[39;49;00m[33m, which is higher than [39;49;00m[33m\"[39;49;00m[33m1snapshot[39;49;00m[33m\"[39;49;00m[33m.[39;49;00m$
[33mAlso, [39;49;00m[33m\"[39;49;00m[33m-GIT[39;49;00m[33m\"[39;49;00m[33m, [39;49;00m[33m\"[39;49;00m[33m-CVS[39;49;00m[33m\"[39;49;00m[33m and [39;49;00m[33m\"[39;49;00m[33m-NNN[39;49;00m[33m\"[39;49;00m[33m are treated as snapshot versions.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([31mversion-list-=[39;49;00m[37m [39;49;00m([31mversion-to-list[39;49;00m[37m [39;49;00m[31mv1[39;49;00m)[37m [39;49;00m([31mversion-to-list[39;49;00m[37m [39;49;00m[31mv2[39;49;00m)))[37m[39;49;00m$
[37m[39;49;00m$
([34mdefvar[39;49;00m[37m [39;49;00m[31mpackage--builtin-versions[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[37m;; Mostly populated by loaddefs.el via autoload-builtin-package-versions.[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([32mpurecopy[39;49;00m[37m [39;49;00m`(([31memacs[39;49;00m[37m [39;49;00m.[37m [39;49;00m,([31mversion-to-list[39;49;00m[37m [39;49;00m[31memacs-version[39;49;00m))))[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mAlist giving the version of each versioned builtin package.[39;49;00m$
[33mI.e. each element of the list is of the form (NAME . VERSION) where[39;49;00m$
[33mNAME is the package name as a symbol, and VERSION is its version[39;49;00m$
[33mas a list.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31mpackage--description-file[39;49;00m[37m [39;49;00m([31mdir[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m([34mlet[39;49;00m[37m [39;49;00m(([31msubdir[39;49;00m[37m [39;49;00m([32mfile-name-nondirectory[39;49;00m[37m[39;49;00m$
[37m                         [39;49;00m([32mdirectory-file-name[39;49;00m[37m [39;49;00m[31mdir[39;49;00m))))[37m[39;49;00m$
[37m            [39;49;00m([34mif[39;49;00m[37m [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m([^.].*?[39;49;00m[33m\\[39;49;00m[33m)-[39;49;00m[33m\\[39;49;00m[33m([0-9]+[39;49;00m[33m\\[39;49;00m[33m(?:[.][0-9]+[39;49;00m[33m\\[39;49;00m[33m|[39;49;00m[33m\\[39;49;00m[33m(?:pre[39;49;00m[33m\\[39;49;00m[33m|beta[39;49;00m[33m\\[39;49;00m[33m|alpha[39;49;00m[33m\\[39;49;00m[33m)[0-9]+[39;49;00m[33m\\[39;49;00m[33m)*[39;49;00m[33m\\[39;49;00m[33m)[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31msubdir[39;49;00m)[37m[39;49;00m$
[37m                [39;49;00m([31mmatch-string[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[31msubdir[39;49;00m)[37m [39;49;00m[31msubdir[39;49;00m))[37m[39;49;00m$
[37m          [39;49;00m[33m"[39;49;00m[33m-pkg.el[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m[37m[39;49;00m$
[37m;;; Misc.[39;49;00m[37m[39;49;00m$
([34mdefconst[39;49;00m[37m [39;49;00m[31mmenu-bar-separator[39;49;00m[37m [39;49;00m'([33m"[39;49;00m[33m--[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mSeparator for menus.[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
[37m;; The following statement ought to be in print.c, but `provide' can't[39;49;00m[37m[39;49;00m$
[37m;; be used there.[39;49;00m[37m[39;49;00m$
[37m;; http://lists.gnu.org/archive/html/emacs-devel/2009-08/msg00236.html[39;49;00m[37m[39;49;00m$
([36mwhen[39;49;00m[37m [39;49;00m([32mhash-table-p[39;49;00m[37m [39;49;00m([32mcar[39;49;00m[37m [39;49;00m([32mread-from-string[39;49;00m[37m[39;49;00m$
[37m^I^I^I  [39;49;00m([32mprin1-to-string[39;49;00m[37m [39;49;00m([32mmake-hash-table[39;49;00m)))))[37m[39;49;00m$
[37m  [39;49;00m([36mprovide[39;49;00m[37m [39;49;00m[33m'hashtable-print-readable[39;49;00m))[37m[39;49;00m$
[37m[39;49;00m$
[37m;; This is used in lisp/Makefile.in and in leim/Makefile.in to[39;49;00m[37m[39;49;00m$
[37m;; generate file names for autoloads, custom-deps, and finder-data.[39;49;00m[37m[39;49;00m$
([36mdefun[39;49;00m[37m [39;49;00m[31munmsys--file-name[39;49;00m[37m [39;49;00m([31mfile[39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[33m"[39;49;00m[33mProduce the canonical file name for FILE from its MSYS form.[39;49;00m$
[33m[39;49;00m$
[33mOn systems other than MS-Windows, just returns FILE.[39;49;00m$
[33mOn MS-Windows, converts /d/foo/bar form of file names[39;49;00m$
[33mpassed by MSYS Make into d:/foo/bar that Emacs can grok.[39;49;00m$
[33m[39;49;00m$
[33mThis function is called from lisp/Makefile and leim/Makefile.[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m([36mwhen[39;49;00m[37m [39;49;00m([34mand[39;49;00m[37m [39;49;00m([32meq[39;49;00m[37m [39;49;00m[31msystem-type[39;49;00m[37m [39;49;00m[33m'windows-nt[39;49;00m)[37m[39;49;00m$
[37m^I     [39;49;00m([32mstring-match[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m`[39;49;00m[33m/[a-zA-Z]/[39;49;00m[33m"[39;49;00m[37m [39;49;00m[31mfile[39;49;00m))[37m[39;49;00m$
[37m    [39;49;00m([34msetq[39;49;00m[37m [39;49;00m[31mfile[39;49;00m[37m [39;49;00m([32mconcat[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[31mfile[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[34m2[39;49;00m)[37m [39;49;00m[33m"[39;49;00m[33m:[39;49;00m[33m"[39;49;00m[37m [39;49;00m([32msubstring[39;49;00m[37m [39;49;00m[31mfile[39;49;00m[37m [39;49;00m[34m2[39;49;00m))))[37m[39;49;00m$
[37m  [39;49;00m[31mfile[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
[37m;;; subr.el ends here[39;49;00m$

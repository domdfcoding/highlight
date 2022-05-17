[37m/* Execute compiled code */[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m/* XXX TO DO:[39;49;00m$
[37m   XXX speed up searching for keywords by using a dictionary[39;49;00m$
[37m   XXX document it![39;49;00m$
[37m   */[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m/* enable more aggressive intra-module optimizations, where available */[39;49;00m[37m[39;49;00m$
[36m#[39;49;00m[36mdefine PY_LOCAL_AGGRESSIVE[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"Python.h"[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"code.h"[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"frameobject.h"[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"eval.h"[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"opcode.h"[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"structmember.h"[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<ctype.h>[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36mifndef WITH_TSC[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36mdefine READ_TIMESTAMP(var)[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36melse[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[34mtypedef[39;49;00m[37m [39;49;00m[36munsigned[39;49;00m[37m [39;49;00m[36mlong[39;49;00m[37m [39;49;00m[36mlong[39;49;00m[37m [39;49;00muint64;[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36mif defined(__ppc__) [39;49;00m[37m/* <- Don't know if this is the correct symbol; this[39;49;00m$
[37m^I^I^I   section should work for GCC on any PowerPC platform,[39;49;00m$
[37m^I^I^I   irrespective of OS.  POWER?  Who knows :-) */[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36mdefine READ_TIMESTAMP(var) ppc_getcounter(&var)[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[34mstatic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m[39;49;00m$
[32mppc_getcounter[39;49;00m(uint64[37m [39;49;00m*v)[37m[39;49;00m$
{[37m[39;49;00m$
[37m^I[39;49;00m[34mregister[39;49;00m[37m [39;49;00m[36munsigned[39;49;00m[37m [39;49;00m[36mlong[39;49;00m[37m [39;49;00mtbu,[37m [39;49;00mtb,[37m [39;49;00mtbu2;[37m[39;49;00m$
[37m[39;49;00m$
[37m  [39;49;00mloop:[37m[39;49;00m$
[37m^I[39;49;00m[34masm[39;49;00m[37m [39;49;00m[34mvolatile[39;49;00m[37m [39;49;00m([33m"[39;49;00m[33mmftbu %0[39;49;00m[33m"[39;49;00m[37m [39;49;00m:[37m [39;49;00m[33m"[39;49;00m[33m=r[39;49;00m[33m"[39;49;00m[37m [39;49;00m(tbu)[37m [39;49;00m);[37m[39;49;00m$
[37m^I[39;49;00m[34masm[39;49;00m[37m [39;49;00m[34mvolatile[39;49;00m[37m [39;49;00m([33m"[39;49;00m[33mmftb  %0[39;49;00m[33m"[39;49;00m[37m [39;49;00m:[37m [39;49;00m[33m"[39;49;00m[33m=r[39;49;00m[33m"[39;49;00m[37m [39;49;00m(tb)[37m  [39;49;00m);[37m[39;49;00m$
[37m^I[39;49;00m[34masm[39;49;00m[37m [39;49;00m[34mvolatile[39;49;00m[37m [39;49;00m([33m"[39;49;00m[33mmftbu %0[39;49;00m[33m"[39;49;00m[37m [39;49;00m:[37m [39;49;00m[33m"[39;49;00m[33m=r[39;49;00m[33m"[39;49;00m[37m [39;49;00m(tbu2));[37m[39;49;00m$
[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(__builtin_expect(tbu[37m [39;49;00m!=[37m [39;49;00mtbu2,[37m [39;49;00m[34m0[39;49;00m))[37m [39;49;00m[34mgoto[39;49;00m[37m [39;49;00mloop;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I[39;49;00m[37m/* The slightly peculiar way of writing the next lines is[39;49;00m$
[37m^I   compiled better by GCC than any other way I tried. */[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00m(([36mlong[39;49;00m*)(v))[[34m0[39;49;00m][37m [39;49;00m=[37m [39;49;00mtbu;[37m[39;49;00m$
[37m^I[39;49;00m(([36mlong[39;49;00m*)(v))[[34m1[39;49;00m][37m [39;49;00m=[37m [39;49;00mtb;[37m[39;49;00m$
}[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36melse [39;49;00m[37m/* this is for linux/x86 (and probably any other GCC/x86 combo) */[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36mdefine READ_TIMESTAMP(val) \[39;49;00m[36m[39;49;00m$
[36m     __asm__ __volatile__("rdtsc" : "=A" (val))[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[36mvoid[39;49;00m[37m [39;49;00m[32mdump_tsc[39;49;00m([36mint[39;49;00m[37m [39;49;00mopcode,[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mticked,[37m [39;49;00muint64[37m [39;49;00minst0,[37m [39;49;00muint64[37m [39;49;00minst1,[37m[39;49;00m$
[37m^I      [39;49;00muint64[37m [39;49;00mloop0,[37m [39;49;00muint64[37m [39;49;00mloop1,[37m [39;49;00muint64[37m [39;49;00mintr0,[37m [39;49;00muint64[37m [39;49;00mintr1)[37m[39;49;00m$
{[37m[39;49;00m$
[37m^I[39;49;00muint64[37m [39;49;00mintr,[37m [39;49;00minst,[37m [39;49;00mloop;[37m[39;49;00m$
[37m^I[39;49;00mPyThreadState[37m [39;49;00m*tstate[37m [39;49;00m=[37m [39;49;00mPyThreadState_Get();[37m[39;49;00m$
[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(!tstate->interp->tscdump)[37m[39;49;00m$
[37m^I^I[39;49;00m[34mreturn[39;49;00m;[37m[39;49;00m$
[37m^I[39;49;00mintr[37m [39;49;00m=[37m [39;49;00mintr1[37m [39;49;00m-[37m [39;49;00mintr0;[37m[39;49;00m$
[37m^I[39;49;00minst[37m [39;49;00m=[37m [39;49;00minst1[37m [39;49;00m-[37m [39;49;00minst0[37m [39;49;00m-[37m [39;49;00mintr;[37m[39;49;00m$
[37m^I[39;49;00mloop[37m [39;49;00m=[37m [39;49;00mloop1[37m [39;49;00m-[37m [39;49;00mloop0[37m [39;49;00m-[37m [39;49;00mintr;[37m[39;49;00m$
[37m^I[39;49;00mfprintf(stderr,[37m [39;49;00m[33m"[39;49;00m[33mopcode=%03d t=%d inst=%06lld loop=%06lld[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m,[37m[39;49;00m$
[37m^I^I[39;49;00mopcode,[37m [39;49;00mticked,[37m [39;49;00minst,[37m [39;49;00mloop);[37m[39;49;00m$
}[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[37m/* Turn this on if your compiler chokes on the big switch: */[39;49;00m[37m[39;49;00m$
[37m/* #define CASE_TOO_BIG 1 */[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36mifdef Py_DEBUG[39;49;00m[36m[39;49;00m$
[37m/* For debugging the interpreter: */[39;49;00m[37m[39;49;00m$
[36m#[39;49;00m[36mdefine LLTRACE  1^I[39;49;00m[37m/* Low-level trace feature */[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine CHECKEXC 1^I[39;49;00m[37m/* Double-check exception checking */[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[34mtypedef[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*(*callproc)(PyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*);[37m[39;49;00m$
[37m[39;49;00m$
[37m/* Forward declarations */[39;49;00m[37m[39;49;00m$
[36m#[39;49;00m[36mifdef WITH_TSC[39;49;00m[36m[39;49;00m$
[34mstatic[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*[37m [39;49;00m[32mcall_function[39;49;00m(PyObject[37m [39;49;00m***,[37m [39;49;00m[36mint[39;49;00m,[37m [39;49;00muint64*,[37m [39;49;00muint64*);[37m[39;49;00m$
[36m#[39;49;00m[36melse[39;49;00m[36m[39;49;00m$
[34mstatic[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*[37m [39;49;00m[32mcall_function[39;49;00m(PyObject[37m [39;49;00m***,[37m [39;49;00m[36mint[39;49;00m);[37m[39;49;00m$
[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
[34mstatic[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*[37m [39;49;00m[32mfast_function[39;49;00m(PyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m***,[37m [39;49;00m[36mint[39;49;00m,[37m [39;49;00m[36mint[39;49;00m,[37m [39;49;00m[36mint[39;49;00m);[37m[39;49;00m$
[34mstatic[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*[37m [39;49;00m[32mdo_call[39;49;00m(PyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m***,[37m [39;49;00m[36mint[39;49;00m,[37m [39;49;00m[36mint[39;49;00m);[37m[39;49;00m$
[34mstatic[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*[37m [39;49;00m[32mext_do_call[39;49;00m(PyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m***,[37m [39;49;00m[36mint[39;49;00m,[37m [39;49;00m[36mint[39;49;00m,[37m [39;49;00m[36mint[39;49;00m);[37m[39;49;00m$
[34mstatic[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*[37m [39;49;00m[32mupdate_keyword_args[39;49;00m(PyObject[37m [39;49;00m*,[37m [39;49;00m[36mint[39;49;00m,[37m [39;49;00mPyObject[37m [39;49;00m***,PyObject[37m [39;49;00m*);[37m[39;49;00m$
[34mstatic[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*[37m [39;49;00m[32mupdate_star_args[39;49;00m([36mint[39;49;00m,[37m [39;49;00m[36mint[39;49;00m,[37m [39;49;00mPyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m***);[37m[39;49;00m$
[34mstatic[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*[37m [39;49;00m[32mload_args[39;49;00m(PyObject[37m [39;49;00m***,[37m [39;49;00m[36mint[39;49;00m);[37m[39;49;00m$
[36m#[39;49;00m[36mdefine CALL_FLAG_VAR 1[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine CALL_FLAG_KW 2[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36mifdef LLTRACE[39;49;00m[36m[39;49;00m$
[34mstatic[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mlltrace;[37m[39;49;00m$
[34mstatic[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00m[32mprtrace[39;49;00m(PyObject[37m [39;49;00m*,[37m [39;49;00m[36mchar[39;49;00m[37m [39;49;00m*);[37m[39;49;00m$
[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
[34mstatic[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00m[32mcall_trace[39;49;00m(Py_tracefunc,[37m [39;49;00mPyObject[37m [39;49;00m*,[37m [39;49;00mPyFrameObject[37m [39;49;00m*,[37m[39;49;00m$
[37m^I^I      [39;49;00m[36mint[39;49;00m,[37m [39;49;00mPyObject[37m [39;49;00m*);[37m[39;49;00m$
[34mstatic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mcall_trace_protected[39;49;00m(Py_tracefunc,[37m [39;49;00mPyObject[37m [39;49;00m*,[37m[39;49;00m$
[37m^I^I^I^I [39;49;00mPyFrameObject[37m [39;49;00m*,[37m [39;49;00m[36mint[39;49;00m,[37m [39;49;00mPyObject[37m [39;49;00m*);[37m[39;49;00m$
[34mstatic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mcall_exc_trace[39;49;00m(Py_tracefunc,[37m [39;49;00mPyObject[37m [39;49;00m*,[37m [39;49;00mPyFrameObject[37m [39;49;00m*);[37m[39;49;00m$
[34mstatic[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00m[32mmaybe_call_line_trace[39;49;00m(Py_tracefunc,[37m [39;49;00mPyObject[37m [39;49;00m*,[37m[39;49;00m$
[37m^I^I^I^I  [39;49;00mPyFrameObject[37m [39;49;00m*,[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00m*,[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00m*,[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00m*);[37m[39;49;00m$
[37m[39;49;00m$
[34mstatic[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*[37m [39;49;00m[32mapply_slice[39;49;00m(PyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*);[37m[39;49;00m$
[34mstatic[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00m[32massign_slice[39;49;00m(PyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*,[37m[39;49;00m$
[37m^I^I^I[39;49;00mPyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*);[37m[39;49;00m$
[34mstatic[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*[37m [39;49;00m[32mcmp_outcome[39;49;00m([36mint[39;49;00m,[37m [39;49;00mPyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*);[37m[39;49;00m$
[34mstatic[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*[37m [39;49;00m[32mimport_from[39;49;00m(PyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*);[37m[39;49;00m$
[34mstatic[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00m[32mimport_all_from[39;49;00m(PyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*);[37m[39;49;00m$
[34mstatic[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*[37m [39;49;00m[32mbuild_class[39;49;00m(PyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*);[37m[39;49;00m$
[34mstatic[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00m[32mexec_statement[39;49;00m(PyFrameObject[37m [39;49;00m*,[37m[39;49;00m$
[37m^I^I^I  [39;49;00mPyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*);[37m[39;49;00m$
[34mstatic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mset_exc_info[39;49;00m(PyThreadState[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*);[37m[39;49;00m$
[34mstatic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mreset_exc_info[39;49;00m(PyThreadState[37m [39;49;00m*);[37m[39;49;00m$
[34mstatic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mformat_exc_check_arg[39;49;00m(PyObject[37m [39;49;00m*,[37m [39;49;00m[36mchar[39;49;00m[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*);[37m[39;49;00m$
[34mstatic[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*[37m [39;49;00m[32mstring_concatenate[39;49;00m(PyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*,[37m[39;49;00m$
[37m^I^I^I^I    [39;49;00mPyFrameObject[37m [39;49;00m*,[37m [39;49;00m[36munsigned[39;49;00m[37m [39;49;00m[36mchar[39;49;00m[37m [39;49;00m*);[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36mdefine NAME_ERROR_MSG \[39;49;00m[36m[39;49;00m$
[36m^I"name '%.200s' is not defined"[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine GLOBAL_NAME_ERROR_MSG \[39;49;00m[36m[39;49;00m$
[36m^I"global name '%.200s' is not defined"[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine UNBOUNDLOCAL_ERROR_MSG \[39;49;00m[36m[39;49;00m$
[36m^I"local variable '%.200s' referenced before assignment"[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine UNBOUNDFREE_ERROR_MSG \[39;49;00m[36m[39;49;00m$
[36m^I"free variable '%.200s' referenced before assignment" \[39;49;00m[36m[39;49;00m$
[36m        " in enclosing scope"[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[37m/* Dynamic execution profile */[39;49;00m[37m[39;49;00m$
[36m#[39;49;00m[36mifdef DYNAMIC_EXECUTION_PROFILE[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mifdef DXPAIRS[39;49;00m[36m[39;49;00m$
[34mstatic[39;49;00m[37m [39;49;00m[36mlong[39;49;00m[37m [39;49;00mdxpairs[[34m257[39;49;00m][[34m256[39;49;00m];[37m[39;49;00m$
[36m#[39;49;00m[36mdefine dxp dxpairs[256][39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36melse[39;49;00m[36m[39;49;00m$
[34mstatic[39;49;00m[37m [39;49;00m[36mlong[39;49;00m[37m [39;49;00mdxp[[34m256[39;49;00m];[37m[39;49;00m$
[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[37m/* Function call profile */[39;49;00m[37m[39;49;00m$
[36m#[39;49;00m[36mifdef CALL_PROFILE[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine PCALL_NUM 11[39;49;00m[36m[39;49;00m$
[34mstatic[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mpcall[PCALL_NUM];[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36mdefine PCALL_ALL 0[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine PCALL_FUNCTION 1[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine PCALL_FAST_FUNCTION 2[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine PCALL_FASTER_FUNCTION 3[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine PCALL_METHOD 4[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine PCALL_BOUND_METHOD 5[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine PCALL_CFUNCTION 6[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine PCALL_TYPE 7[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine PCALL_GENERATOR 8[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine PCALL_OTHER 9[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine PCALL_POP 10[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[37m/* Notes about the statistics[39;49;00m$
[37m[39;49;00m$
[37m   PCALL_FAST stats[39;49;00m$
[37m[39;49;00m$
[37m   FAST_FUNCTION means no argument tuple needs to be created.[39;49;00m$
[37m   FASTER_FUNCTION means that the fast-path frame setup code is used.[39;49;00m$
[37m[39;49;00m$
[37m   If there is a method call where the call can be optimized by changing[39;49;00m$
[37m   the argument tuple and calling the function directly, it gets recorded[39;49;00m$
[37m   twice.[39;49;00m$
[37m[39;49;00m$
[37m   As a result, the relationship among the statistics appears to be[39;49;00m$
[37m   PCALL_ALL == PCALL_FUNCTION + PCALL_METHOD - PCALL_BOUND_METHOD +[39;49;00m$
[37m                PCALL_CFUNCTION + PCALL_TYPE + PCALL_GENERATOR + PCALL_OTHER[39;49;00m$
[37m   PCALL_FUNCTION > PCALL_FAST_FUNCTION > PCALL_FASTER_FUNCTION[39;49;00m$
[37m   PCALL_METHOD > PCALL_BOUND_METHOD[39;49;00m$
[37m*/[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36mdefine PCALL(POS) pcall[POS]++[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
PyObject[37m [39;49;00m*[37m[39;49;00m$
[32mPyEval_GetCallStats[39;49;00m(PyObject[37m [39;49;00m*self)[37m[39;49;00m$
{[37m[39;49;00m$
[37m^I[39;49;00m[34mreturn[39;49;00m[37m [39;49;00mPy_BuildValue([33m"[39;49;00m[33miiiiiiiiii[39;49;00m[33m"[39;49;00m,[37m[39;49;00m$
[37m^I^I^I     [39;49;00mpcall[[34m0[39;49;00m],[37m [39;49;00mpcall[[34m1[39;49;00m],[37m [39;49;00mpcall[[34m2[39;49;00m],[37m [39;49;00mpcall[[34m3[39;49;00m],[37m[39;49;00m$
[37m^I^I^I     [39;49;00mpcall[[34m4[39;49;00m],[37m [39;49;00mpcall[[34m5[39;49;00m],[37m [39;49;00mpcall[[34m6[39;49;00m],[37m [39;49;00mpcall[[34m7[39;49;00m],[37m[39;49;00m$
[37m^I^I^I     [39;49;00mpcall[[34m8[39;49;00m],[37m [39;49;00mpcall[[34m9[39;49;00m]);[37m[39;49;00m$
}[37m[39;49;00m$
[36m#[39;49;00m[36melse[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine PCALL(O)[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
PyObject[37m [39;49;00m*[37m[39;49;00m$
[32mPyEval_GetCallStats[39;49;00m(PyObject[37m [39;49;00m*self)[37m[39;49;00m$
{[37m[39;49;00m$
[37m^I[39;49;00mPy_INCREF(Py_None);[37m[39;49;00m$
[37m^I[39;49;00m[34mreturn[39;49;00m[37m [39;49;00mPy_None;[37m[39;49;00m$
}[37m[39;49;00m$
[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36mifdef WITH_THREAD[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36mifdef HAVE_ERRNO_H[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<errno.h>[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"pythread.h"[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[34mstatic[39;49;00m[37m [39;49;00mPyThread_type_lock[37m [39;49;00minterpreter_lock[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m [39;49;00m[37m/* This is the GIL */[39;49;00m[37m[39;49;00m$
[34mstatic[39;49;00m[37m [39;49;00m[36mlong[39;49;00m[37m [39;49;00mmain_thread[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[36mint[39;49;00m[37m[39;49;00m$
[32mPyEval_ThreadsInitialized[39;49;00m([36mvoid[39;49;00m)[37m[39;49;00m$
{[37m[39;49;00m$
[37m^I[39;49;00m[34mreturn[39;49;00m[37m [39;49;00minterpreter_lock[37m [39;49;00m!=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
}[37m[39;49;00m$
[37m[39;49;00m$
[36mvoid[39;49;00m[37m[39;49;00m$
[32mPyEval_InitThreads[39;49;00m([36mvoid[39;49;00m)[37m[39;49;00m$
{[37m[39;49;00m$
[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(interpreter_lock)[37m[39;49;00m$
[37m^I^I[39;49;00m[34mreturn[39;49;00m;[37m[39;49;00m$
[37m^I[39;49;00minterpreter_lock[37m [39;49;00m=[37m [39;49;00mPyThread_allocate_lock();[37m[39;49;00m$
[37m^I[39;49;00mPyThread_acquire_lock(interpreter_lock,[37m [39;49;00m[34m1[39;49;00m);[37m[39;49;00m$
[37m^I[39;49;00mmain_thread[37m [39;49;00m=[37m [39;49;00mPyThread_get_thread_ident();[37m[39;49;00m$
}[37m[39;49;00m$
[37m[39;49;00m$
[36mvoid[39;49;00m[37m[39;49;00m$
[32mPyEval_AcquireLock[39;49;00m([36mvoid[39;49;00m)[37m[39;49;00m$
{[37m[39;49;00m$
[37m^I[39;49;00mPyThread_acquire_lock(interpreter_lock,[37m [39;49;00m[34m1[39;49;00m);[37m[39;49;00m$
}[37m[39;49;00m$
[37m[39;49;00m$
[36mvoid[39;49;00m[37m[39;49;00m$
[32mPyEval_ReleaseLock[39;49;00m([36mvoid[39;49;00m)[37m[39;49;00m$
{[37m[39;49;00m$
[37m^I[39;49;00mPyThread_release_lock(interpreter_lock);[37m[39;49;00m$
}[37m[39;49;00m$
[37m[39;49;00m$
[36mvoid[39;49;00m[37m[39;49;00m$
[32mPyEval_AcquireThread[39;49;00m(PyThreadState[37m [39;49;00m*tstate)[37m[39;49;00m$
{[37m[39;49;00m$
[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(tstate[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
[37m^I^I[39;49;00mPy_FatalError([33m"[39;49;00m[33mPyEval_AcquireThread: NULL new thread state[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
[37m^I[39;49;00m[37m/* Check someone has called PyEval_InitThreads() to create the lock */[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00massert(interpreter_lock);[37m[39;49;00m$
[37m^I[39;49;00mPyThread_acquire_lock(interpreter_lock,[37m [39;49;00m[34m1[39;49;00m);[37m[39;49;00m$
[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyThreadState_Swap(tstate)[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
[37m^I^I[39;49;00mPy_FatalError([37m[39;49;00m$
[37m^I^I^I[39;49;00m[33m"[39;49;00m[33mPyEval_AcquireThread: non-NULL old thread state[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
}[37m[39;49;00m$
[37m[39;49;00m$
[36mvoid[39;49;00m[37m[39;49;00m$
[32mPyEval_ReleaseThread[39;49;00m(PyThreadState[37m [39;49;00m*tstate)[37m[39;49;00m$
{[37m[39;49;00m$
[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(tstate[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
[37m^I^I[39;49;00mPy_FatalError([33m"[39;49;00m[33mPyEval_ReleaseThread: NULL thread state[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyThreadState_Swap([36mNULL[39;49;00m)[37m [39;49;00m!=[37m [39;49;00mtstate)[37m[39;49;00m$
[37m^I^I[39;49;00mPy_FatalError([33m"[39;49;00m[33mPyEval_ReleaseThread: wrong thread state[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
[37m^I[39;49;00mPyThread_release_lock(interpreter_lock);[37m[39;49;00m$
}[37m[39;49;00m$
[37m[39;49;00m$
[37m/* This function is called from PyOS_AfterFork to ensure that newly[39;49;00m$
[37m   created child processes don't hold locks referring to threads which[39;49;00m$
[37m   are not running in the child process.  (This could also be done using[39;49;00m$
[37m   pthread_atfork mechanism, at least for the pthreads implementation.) */[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[36mvoid[39;49;00m[37m[39;49;00m$
[32mPyEval_ReInitThreads[39;49;00m([36mvoid[39;49;00m)[37m[39;49;00m$
{[37m[39;49;00m$
[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(!interpreter_lock)[37m[39;49;00m$
[37m^I^I[39;49;00m[34mreturn[39;49;00m;[37m[39;49;00m$
[37m^I[39;49;00m[37m/*XXX Can't use PyThread_free_lock here because it does too[39;49;00m$
[37m^I  much error-checking.  Doing this cleanly would require[39;49;00m$
[37m^I  adding a new function to each thread_*.h.  Instead, just[39;49;00m$
[37m^I  create a new lock and waste a little bit of memory */[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00minterpreter_lock[37m [39;49;00m=[37m [39;49;00mPyThread_allocate_lock();[37m[39;49;00m$
[37m^I[39;49;00mPyThread_acquire_lock(interpreter_lock,[37m [39;49;00m[34m1[39;49;00m);[37m[39;49;00m$
[37m^I[39;49;00mmain_thread[37m [39;49;00m=[37m [39;49;00mPyThread_get_thread_ident();[37m[39;49;00m$
}[37m[39;49;00m$
[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[37m/* Functions save_thread and restore_thread are always defined so[39;49;00m$
[37m   dynamically loaded modules needn't be compiled separately for use[39;49;00m$
[37m   with and without threads: */[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
PyThreadState[37m [39;49;00m*[37m[39;49;00m$
[32mPyEval_SaveThread[39;49;00m([36mvoid[39;49;00m)[37m[39;49;00m$
{[37m[39;49;00m$
[37m^I[39;49;00mPyThreadState[37m [39;49;00m*tstate[37m [39;49;00m=[37m [39;49;00mPyThreadState_Swap([36mNULL[39;49;00m);[37m[39;49;00m$
[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(tstate[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
[37m^I^I[39;49;00mPy_FatalError([33m"[39;49;00m[33mPyEval_SaveThread: NULL tstate[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
[36m#[39;49;00m[36mifdef WITH_THREAD[39;49;00m[36m[39;49;00m$
[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(interpreter_lock)[37m[39;49;00m$
[37m^I^I[39;49;00mPyThread_release_lock(interpreter_lock);[37m[39;49;00m$
[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
[37m^I[39;49;00m[34mreturn[39;49;00m[37m [39;49;00mtstate;[37m[39;49;00m$
}[37m[39;49;00m$
[37m[39;49;00m$
[36mvoid[39;49;00m[37m[39;49;00m$
[32mPyEval_RestoreThread[39;49;00m(PyThreadState[37m [39;49;00m*tstate)[37m[39;49;00m$
{[37m[39;49;00m$
[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(tstate[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
[37m^I^I[39;49;00mPy_FatalError([33m"[39;49;00m[33mPyEval_RestoreThread: NULL tstate[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
[36m#[39;49;00m[36mifdef WITH_THREAD[39;49;00m[36m[39;49;00m$
[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(interpreter_lock)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I[39;49;00m[36mint[39;49;00m[37m [39;49;00merr[37m [39;49;00m=[37m [39;49;00merrno;[37m[39;49;00m$
[37m^I^I[39;49;00mPyThread_acquire_lock(interpreter_lock,[37m [39;49;00m[34m1[39;49;00m);[37m[39;49;00m$
[37m^I^I[39;49;00merrno[37m [39;49;00m=[37m [39;49;00merr;[37m[39;49;00m$
[37m^I[39;49;00m}[37m[39;49;00m$
[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
[37m^I[39;49;00mPyThreadState_Swap(tstate);[37m[39;49;00m$
}[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
[37m/* Mechanism whereby asynchronously executing callbacks (e.g. UNIX[39;49;00m$
[37m   signal handlers or Mac I/O completion routines) can schedule calls[39;49;00m$
[37m   to a function to be called synchronously.[39;49;00m$
[37m   The synchronous function is called with one void* argument.[39;49;00m$
[37m   It should return 0 for success or -1 for failure -- failure should[39;49;00m$
[37m   be accompanied by an exception.[39;49;00m$
[37m[39;49;00m$
[37m   If registry succeeds, the registry function returns 0; if it fails[39;49;00m$
[37m   (e.g. due to too many pending calls) it returns -1 (without setting[39;49;00m$
[37m   an exception condition).[39;49;00m$
[37m[39;49;00m$
[37m   Note that because registry may occur from within signal handlers,[39;49;00m$
[37m   or other asynchronous events, calling malloc() is unsafe![39;49;00m$
[37m[39;49;00m$
[37m#ifdef WITH_THREAD[39;49;00m$
[37m   Any thread can schedule pending calls, but only the main thread[39;49;00m$
[37m   will execute them.[39;49;00m$
[37m#endif[39;49;00m$
[37m[39;49;00m$
[37m   XXX WARNING!  ASYNCHRONOUSLY EXECUTING CODE![39;49;00m$
[37m   There are two possible race conditions:[39;49;00m$
[37m   (1) nested asynchronous registry calls;[39;49;00m$
[37m   (2) registry calls made while pending calls are being processed.[39;49;00m$
[37m   While (1) is very unlikely, (2) is a real possibility.[39;49;00m$
[37m   The current code is safe against (2), but not against (1).[39;49;00m$
[37m   The safety against (2) is derived from the fact that only one[39;49;00m$
[37m   thread (the main thread) ever takes things out of the queue.[39;49;00m$
[37m[39;49;00m$
[37m   XXX Darn!  With the advent of thread state, we should have an array[39;49;00m$
[37m   of pending calls per thread in the thread state!  Later...[39;49;00m$
[37m*/[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36mdefine NPENDINGCALLS 32[39;49;00m[36m[39;49;00m$
[34mstatic[39;49;00m[37m [39;49;00m[34mstruct[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
[37m^I[39;49;00m[36mint[39;49;00m[37m [39;49;00m(*func)([36mvoid[39;49;00m[37m [39;49;00m*);[37m[39;49;00m$
[37m^I[39;49;00m[36mvoid[39;49;00m[37m [39;49;00m*arg;[37m[39;49;00m$
}[37m [39;49;00mpendingcalls[NPENDINGCALLS];[37m[39;49;00m$
[34mstatic[39;49;00m[37m [39;49;00m[34mvolatile[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mpendingfirst[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
[34mstatic[39;49;00m[37m [39;49;00m[34mvolatile[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mpendinglast[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
[34mstatic[39;49;00m[37m [39;49;00m[34mvolatile[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mthings_to_do[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[36mint[39;49;00m[37m[39;49;00m$
[32mPy_AddPendingCall[39;49;00m([36mint[39;49;00m[37m [39;49;00m(*func)([36mvoid[39;49;00m[37m [39;49;00m*),[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m*arg)[37m[39;49;00m$
{[37m[39;49;00m$
[37m^I[39;49;00m[34mstatic[39;49;00m[37m [39;49;00m[34mvolatile[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mbusy[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
[37m^I[39;49;00m[36mint[39;49;00m[37m [39;49;00mi,[37m [39;49;00mj;[37m[39;49;00m$
[37m^I[39;49;00m[37m/* XXX Begin critical section */[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00m[37m/* XXX If you want this to be safe against nested[39;49;00m$
[37m^I   XXX asynchronous calls, you'll have to work harder! */[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(busy)[37m[39;49;00m$
[37m^I^I[39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34m-1[39;49;00m;[37m[39;49;00m$
[37m^I[39;49;00mbusy[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
[37m^I[39;49;00mi[37m [39;49;00m=[37m [39;49;00mpendinglast;[37m[39;49;00m$
[37m^I[39;49;00mj[37m [39;49;00m=[37m [39;49;00m(i[37m [39;49;00m+[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m%[37m [39;49;00mNPENDINGCALLS;[37m[39;49;00m$
[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(j[37m [39;49;00m==[37m [39;49;00mpendingfirst)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I[39;49;00mbusy[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
[37m^I^I[39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34m-1[39;49;00m;[37m [39;49;00m[37m/* Queue full */[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00m}[37m[39;49;00m$
[37m^I[39;49;00mpendingcalls[i].func[37m [39;49;00m=[37m [39;49;00mfunc;[37m[39;49;00m$
[37m^I[39;49;00mpendingcalls[i].arg[37m [39;49;00m=[37m [39;49;00marg;[37m[39;49;00m$
[37m^I[39;49;00mpendinglast[37m [39;49;00m=[37m [39;49;00mj;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I[39;49;00m_Py_Ticker[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
[37m^I[39;49;00mthings_to_do[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m;[37m [39;49;00m[37m/* Signal main loop */[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00mbusy[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
[37m^I[39;49;00m[37m/* XXX End critical section */[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
}[37m[39;49;00m$
[37m[39;49;00m$
[36mint[39;49;00m[37m[39;49;00m$
[32mPy_MakePendingCalls[39;49;00m([36mvoid[39;49;00m)[37m[39;49;00m$
{[37m[39;49;00m$
[37m^I[39;49;00m[34mstatic[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mbusy[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
[36m#[39;49;00m[36mifdef WITH_THREAD[39;49;00m[36m[39;49;00m$
[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(main_thread[37m [39;49;00m&&[37m [39;49;00mPyThread_get_thread_ident()[37m [39;49;00m!=[37m [39;49;00mmain_thread)[37m[39;49;00m$
[37m^I^I[39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(busy)[37m[39;49;00m$
[37m^I^I[39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
[37m^I[39;49;00mbusy[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
[37m^I[39;49;00mthings_to_do[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
[37m^I[39;49;00m[34mfor[39;49;00m[37m [39;49;00m(;;)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I[39;49;00m[36mint[39;49;00m[37m [39;49;00mi;[37m[39;49;00m$
[37m^I^I[39;49;00m[36mint[39;49;00m[37m [39;49;00m(*func)([36mvoid[39;49;00m[37m [39;49;00m*);[37m[39;49;00m$
[37m^I^I[39;49;00m[36mvoid[39;49;00m[37m [39;49;00m*arg;[37m[39;49;00m$
[37m^I^I[39;49;00mi[37m [39;49;00m=[37m [39;49;00mpendingfirst;[37m[39;49;00m$
[37m^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(i[37m [39;49;00m==[37m [39;49;00mpendinglast)[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m [39;49;00m[37m/* Queue empty */[39;49;00m[37m[39;49;00m$
[37m^I^I[39;49;00mfunc[37m [39;49;00m=[37m [39;49;00mpendingcalls[i].func;[37m[39;49;00m$
[37m^I^I[39;49;00marg[37m [39;49;00m=[37m [39;49;00mpendingcalls[i].arg;[37m[39;49;00m$
[37m^I^I[39;49;00mpendingfirst[37m [39;49;00m=[37m [39;49;00m(i[37m [39;49;00m+[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m%[37m [39;49;00mNPENDINGCALLS;[37m[39;49;00m$
[37m^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(func(arg)[37m [39;49;00m<[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I[39;49;00mbusy[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00mthings_to_do[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m;[37m [39;49;00m[37m/* We're not done yet */[39;49;00m[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34m-1[39;49;00m;[37m[39;49;00m$
[37m^I^I[39;49;00m}[37m[39;49;00m$
[37m^I[39;49;00m}[37m[39;49;00m$
[37m^I[39;49;00mbusy[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
[37m^I[39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
}[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
[37m/* The interpreter's recursion limit */[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36mifndef Py_DEFAULT_RECURSION_LIMIT[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine Py_DEFAULT_RECURSION_LIMIT 1000[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
[34mstatic[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mrecursion_limit[37m [39;49;00m=[37m [39;49;00mPy_DEFAULT_RECURSION_LIMIT;[37m[39;49;00m$
[36mint[39;49;00m[37m [39;49;00m_Py_CheckRecursionLimit[37m [39;49;00m=[37m [39;49;00mPy_DEFAULT_RECURSION_LIMIT;[37m[39;49;00m$
[37m[39;49;00m$
[36mint[39;49;00m[37m[39;49;00m$
[32mPy_GetRecursionLimit[39;49;00m([36mvoid[39;49;00m)[37m[39;49;00m$
{[37m[39;49;00m$
[37m^I[39;49;00m[34mreturn[39;49;00m[37m [39;49;00mrecursion_limit;[37m[39;49;00m$
}[37m[39;49;00m$
[37m[39;49;00m$
[36mvoid[39;49;00m[37m[39;49;00m$
[32mPy_SetRecursionLimit[39;49;00m([36mint[39;49;00m[37m [39;49;00mnew_limit)[37m[39;49;00m$
{[37m[39;49;00m$
[37m^I[39;49;00mrecursion_limit[37m [39;49;00m=[37m [39;49;00mnew_limit;[37m[39;49;00m$
[37m        [39;49;00m_Py_CheckRecursionLimit[37m [39;49;00m=[37m [39;49;00mrecursion_limit;[37m[39;49;00m$
}[37m[39;49;00m$
[37m[39;49;00m$
[37m/* the macro Py_EnterRecursiveCall() only calls _Py_CheckRecursiveCall()[39;49;00m$
[37m   if the recursion_depth reaches _Py_CheckRecursionLimit.[39;49;00m$
[37m   If USE_STACKCHECK, the macro decrements _Py_CheckRecursionLimit[39;49;00m$
[37m   to guarantee that _Py_CheckRecursiveCall() is regularly called.[39;49;00m$
[37m   Without USE_STACKCHECK, there is no need for this. */[39;49;00m[37m[39;49;00m$
[36mint[39;49;00m[37m[39;49;00m$
[32m_Py_CheckRecursiveCall[39;49;00m([36mchar[39;49;00m[37m [39;49;00m*where)[37m[39;49;00m$
{[37m[39;49;00m$
[37m^I[39;49;00mPyThreadState[37m [39;49;00m*tstate[37m [39;49;00m=[37m [39;49;00mPyThreadState_GET();[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36mifdef USE_STACKCHECK[39;49;00m[36m[39;49;00m$
[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyOS_CheckStack())[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I[39;49;00m--tstate->recursion_depth;[37m[39;49;00m$
[37m^I^I[39;49;00mPyErr_SetString(PyExc_MemoryError,[37m [39;49;00m[33m"[39;49;00m[33mStack overflow[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
[37m^I^I[39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34m-1[39;49;00m;[37m[39;49;00m$
[37m^I[39;49;00m}[37m[39;49;00m$
[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(tstate->recursion_depth[37m [39;49;00m>[37m [39;49;00mrecursion_limit)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I[39;49;00m--tstate->recursion_depth;[37m[39;49;00m$
[37m^I^I[39;49;00mPyErr_Format(PyExc_RuntimeError,[37m[39;49;00m$
[37m^I^I^I     [39;49;00m[33m"[39;49;00m[33mmaximum recursion depth exceeded%s[39;49;00m[33m"[39;49;00m,[37m[39;49;00m$
[37m^I^I^I     [39;49;00mwhere);[37m[39;49;00m$
[37m^I^I[39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34m-1[39;49;00m;[37m[39;49;00m$
[37m^I[39;49;00m}[37m[39;49;00m$
[37m        [39;49;00m_Py_CheckRecursionLimit[37m [39;49;00m=[37m [39;49;00mrecursion_limit;[37m[39;49;00m$
[37m^I[39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
}[37m[39;49;00m$
[37m[39;49;00m$
[37m/* Status code for main loop (reason for stack unwind) */[39;49;00m[37m[39;49;00m$
[34menum[39;49;00m[37m [39;49;00mwhy_code[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I[39;49;00mWHY_NOT[37m [39;49;00m=[37m^I[39;49;00m[34m0x0001[39;49;00m,[37m^I[39;49;00m[37m/* No error */[39;49;00m[37m[39;49;00m$
[37m^I^I[39;49;00mWHY_EXCEPTION[37m [39;49;00m=[37m [39;49;00m[34m0x0002[39;49;00m,[37m^I[39;49;00m[37m/* Exception occurred */[39;49;00m[37m[39;49;00m$
[37m^I^I[39;49;00mWHY_RERAISE[37m [39;49;00m=[37m^I[39;49;00m[34m0x0004[39;49;00m,[37m^I[39;49;00m[37m/* Exception re-raised by 'finally' */[39;49;00m[37m[39;49;00m$
[37m^I^I[39;49;00mWHY_RETURN[37m [39;49;00m=[37m^I[39;49;00m[34m0x0008[39;49;00m,[37m^I[39;49;00m[37m/* 'return' statement */[39;49;00m[37m[39;49;00m$
[37m^I^I[39;49;00mWHY_BREAK[37m [39;49;00m=[37m^I[39;49;00m[34m0x0010[39;49;00m,[37m^I[39;49;00m[37m/* 'break' statement */[39;49;00m[37m[39;49;00m$
[37m^I^I[39;49;00mWHY_CONTINUE[37m [39;49;00m=[37m^I[39;49;00m[34m0x0020[39;49;00m,[37m^I[39;49;00m[37m/* 'continue' statement */[39;49;00m[37m[39;49;00m$
[37m^I^I[39;49;00mWHY_YIELD[37m [39;49;00m=[37m^I[39;49;00m[34m0x0040[39;49;00m[37m^I[39;49;00m[37m/* 'yield' operator */[39;49;00m[37m[39;49;00m$
};[37m[39;49;00m$
[37m[39;49;00m$
[34mstatic[39;49;00m[37m [39;49;00m[34menum[39;49;00m[37m [39;49;00mwhy_code[37m [39;49;00m[32mdo_raise[39;49;00m(PyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*);[37m[39;49;00m$
[34mstatic[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00m[32munpack_iterable[39;49;00m(PyObject[37m [39;49;00m*,[37m [39;49;00m[36mint[39;49;00m,[37m [39;49;00mPyObject[37m [39;49;00m**);[37m[39;49;00m$
[37m[39;49;00m$
[37m/* for manipulating the thread switch and periodic "stuff" - used to be[39;49;00m$
[37m   per thread, now just a pair o' globals */[39;49;00m[37m[39;49;00m$
[36mint[39;49;00m[37m [39;49;00m_Py_CheckInterval[37m [39;49;00m=[37m [39;49;00m[34m100[39;49;00m;[37m[39;49;00m$
[34mvolatile[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00m_Py_Ticker[37m [39;49;00m=[37m [39;49;00m[34m100[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
PyObject[37m [39;49;00m*[37m[39;49;00m$
[32mPyEval_EvalCode[39;49;00m(PyCodeObject[37m [39;49;00m*co,[37m [39;49;00mPyObject[37m [39;49;00m*globals,[37m [39;49;00mPyObject[37m [39;49;00m*locals)[37m[39;49;00m$
{[37m[39;49;00m$
[37m^I[39;49;00m[37m/* XXX raise SystemError if globals is NULL */[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00m[34mreturn[39;49;00m[37m [39;49;00mPyEval_EvalCodeEx(co,[37m[39;49;00m$
[37m^I^I^I  [39;49;00mglobals,[37m [39;49;00mlocals,[37m[39;49;00m$
[37m^I^I^I  [39;49;00m(PyObject[37m [39;49;00m**)[36mNULL[39;49;00m,[37m [39;49;00m[34m0[39;49;00m,[37m[39;49;00m$
[37m^I^I^I  [39;49;00m(PyObject[37m [39;49;00m**)[36mNULL[39;49;00m,[37m [39;49;00m[34m0[39;49;00m,[37m[39;49;00m$
[37m^I^I^I  [39;49;00m(PyObject[37m [39;49;00m**)[36mNULL[39;49;00m,[37m [39;49;00m[34m0[39;49;00m,[37m[39;49;00m$
[37m^I^I^I  [39;49;00m[36mNULL[39;49;00m);[37m[39;49;00m$
}[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
[37m/* Interpreter main loop */[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
PyObject[37m [39;49;00m*[37m[39;49;00m$
[32mPyEval_EvalFrame[39;49;00m(PyFrameObject[37m [39;49;00m*f)[37m [39;49;00m{[37m[39;49;00m$
[37m^I[39;49;00m[37m/* This is for backward compatibility with extension modules that[39;49;00m$
[37m           used this API; core interpreter code should call PyEval_EvalFrameEx() */[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00m[34mreturn[39;49;00m[37m [39;49;00mPyEval_EvalFrameEx(f,[37m [39;49;00m[34m0[39;49;00m);[37m[39;49;00m$
}[37m[39;49;00m$
[37m[39;49;00m$
PyObject[37m [39;49;00m*[37m[39;49;00m$
[32mPyEval_EvalFrameEx[39;49;00m(PyFrameObject[37m [39;49;00m*f,[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mthrowflag)[37m[39;49;00m$
{[37m[39;49;00m$
[36m#[39;49;00m[36mifdef DXPAIRS[39;49;00m[36m[39;49;00m$
[37m^I[39;49;00m[36mint[39;49;00m[37m [39;49;00mlastopcode[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
[37m^I[39;49;00m[34mregister[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m**stack_pointer;[37m   [39;49;00m[37m/* Next free slot in value stack */[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00m[34mregister[39;49;00m[37m [39;49;00m[36munsigned[39;49;00m[37m [39;49;00m[36mchar[39;49;00m[37m [39;49;00m*next_instr;[37m[39;49;00m$
[37m^I[39;49;00m[34mregister[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mopcode;[37m^I[39;49;00m[37m/* Current opcode */[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00m[34mregister[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00moparg;[37m^I[39;49;00m[37m/* Current opcode argument, if any */[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00m[34mregister[39;49;00m[37m [39;49;00m[34menum[39;49;00m[37m [39;49;00mwhy_code[37m [39;49;00mwhy;[37m [39;49;00m[37m/* Reason for block stack unwind */[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00m[34mregister[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00merr;[37m^I[39;49;00m[37m/* Error status -- nonzero if error */[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00m[34mregister[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*x;[37m^I[39;49;00m[37m/* Result object -- NULL if error */[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00m[34mregister[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*v;[37m^I[39;49;00m[37m/* Temporary objects popped off stack */[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00m[34mregister[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*w;[37m[39;49;00m$
[37m^I[39;49;00m[34mregister[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*u;[37m[39;49;00m$
[37m^I[39;49;00m[34mregister[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*t;[37m[39;49;00m$
[37m^I[39;49;00m[34mregister[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*stream[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m    [39;49;00m[37m/* for PRINT opcodes */[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00m[34mregister[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m**fastlocals,[37m [39;49;00m**freevars;[37m[39;49;00m$
[37m^I[39;49;00mPyObject[37m [39;49;00m*retval[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m^I[39;49;00m[37m/* Return value */[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00mPyThreadState[37m [39;49;00m*tstate[37m [39;49;00m=[37m [39;49;00mPyThreadState_GET();[37m[39;49;00m$
[37m^I[39;49;00mPyCodeObject[37m [39;49;00m*co;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I[39;49;00m[37m/* when tracing we set things up so that[39;49;00m$
[37m[39;49;00m$
[37m               not (instr_lb <= current_bytecode_offset < instr_ub)[39;49;00m$
[37m[39;49;00m$
[37m^I   is true when the line being executed has changed.  The[39;49;00m$
[37m           initial values are such as to make this false the first[39;49;00m$
[37m           time it is tested. */[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00m[36mint[39;49;00m[37m [39;49;00minstr_ub[37m [39;49;00m=[37m [39;49;00m[34m-1[39;49;00m,[37m [39;49;00minstr_lb[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m,[37m [39;49;00minstr_prev[37m [39;49;00m=[37m [39;49;00m[34m-1[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I[39;49;00m[36munsigned[39;49;00m[37m [39;49;00m[36mchar[39;49;00m[37m [39;49;00m*first_instr;[37m[39;49;00m$
[37m^I[39;49;00mPyObject[37m [39;49;00m*names;[37m[39;49;00m$
[37m^I[39;49;00mPyObject[37m [39;49;00m*consts;[37m[39;49;00m$
[36m#[39;49;00m[36mif defined(Py_DEBUG) || defined(LLTRACE)[39;49;00m[36m[39;49;00m$
[37m^I[39;49;00m[37m/* Make it easier to find out where we are with a debugger */[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00m[36mchar[39;49;00m[37m [39;49;00m*filename;[37m[39;49;00m$
[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[37m/* Tuple access macros */[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36mifndef Py_DEBUG[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine GETITEM(v, i) PyTuple_GET_ITEM((PyTupleObject *)(v), (i))[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36melse[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine GETITEM(v, i) PyTuple_GetItem((v), (i))[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36mifdef WITH_TSC[39;49;00m[36m[39;49;00m$
[37m/* Use Pentium timestamp counter to mark certain events:[39;49;00m$
[37m   inst0 -- beginning of switch statement for opcode dispatch[39;49;00m$
[37m   inst1 -- end of switch statement (may be skipped)[39;49;00m$
[37m   loop0 -- the top of the mainloop[39;49;00m$
[37m   loop1 -- place where control returns again to top of mainloop[39;49;00m$
[37m            (may be skipped)[39;49;00m$
[37m   intr1 -- beginning of long interruption[39;49;00m$
[37m   intr2 -- end of long interruption[39;49;00m$
[37m[39;49;00m$
[37m   Many opcodes call out to helper C functions.  In some cases, the[39;49;00m$
[37m   time in those functions should be counted towards the time for the[39;49;00m$
[37m   opcode, but not in all cases.  For example, a CALL_FUNCTION opcode[39;49;00m$
[37m   calls another Python function; there's no point in charge all the[39;49;00m$
[37m   bytecode executed by the called function to the caller.[39;49;00m$
[37m[39;49;00m$
[37m   It's hard to make a useful judgement statically.  In the presence[39;49;00m$
[37m   of operator overloading, it's impossible to tell if a call will[39;49;00m$
[37m   execute new Python code or not.[39;49;00m$
[37m[39;49;00m$
[37m   It's a case-by-case judgement.  I'll use intr1 for the following[39;49;00m$
[37m   cases:[39;49;00m$
[37m[39;49;00m$
[37m   EXEC_STMT[39;49;00m$
[37m   IMPORT_STAR[39;49;00m$
[37m   IMPORT_FROM[39;49;00m$
[37m   CALL_FUNCTION (and friends)[39;49;00m$
[37m[39;49;00m$
[37m */[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00muint64[37m [39;49;00minst0,[37m [39;49;00minst1,[37m [39;49;00mloop0,[37m [39;49;00mloop1,[37m [39;49;00mintr0[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m,[37m [39;49;00mintr1[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
[37m^I[39;49;00m[36mint[39;49;00m[37m [39;49;00mticked[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I[39;49;00mREAD_TIMESTAMP(inst0);[37m[39;49;00m$
[37m^I[39;49;00mREAD_TIMESTAMP(inst1);[37m[39;49;00m$
[37m^I[39;49;00mREAD_TIMESTAMP(loop0);[37m[39;49;00m$
[37m^I[39;49;00mREAD_TIMESTAMP(loop1);[37m[39;49;00m$
[37m[39;49;00m$
[37m^I[39;49;00m[37m/* shut up the compiler */[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00mopcode[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[37m/* Code access macros */[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36mdefine INSTR_OFFSET()^I((int)(next_instr - first_instr))[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine NEXTOP()^I(*next_instr++)[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine NEXTARG()^I(next_instr += 2, (next_instr[-1]<<8) + next_instr[-2])[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine PEEKARG()^I((next_instr[2]<<8) + next_instr[1])[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine JUMPTO(x)^I(next_instr = first_instr + (x))[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine JUMPBY(x)^I(next_instr += (x))[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[37m/* OpCode prediction macros[39;49;00m$
[37m^ISome opcodes tend to come in pairs thus making it possible to predict[39;49;00m$
[37m^Ithe second code when the first is run.  For example, COMPARE_OP is often[39;49;00m$
[37m^Ifollowed by JUMP_IF_FALSE or JUMP_IF_TRUE.  And, those opcodes are often[39;49;00m$
[37m^Ifollowed by a POP_TOP.[39;49;00m$
[37m[39;49;00m$
[37m^IVerifying the prediction costs a single high-speed test of register[39;49;00m$
[37m^Ivariable against a constant.  If the pairing was good, then the[39;49;00m$
[37m^Iprocessor has a high likelihood of making its own successful branch[39;49;00m$
[37m^Iprediction which results in a nearly zero overhead transition to the[39;49;00m$
[37m^Inext opcode.[39;49;00m$
[37m[39;49;00m$
[37m^IA successful prediction saves a trip through the eval-loop including[39;49;00m$
[37m^Iits two unpredictable branches, the HASARG test and the switch-case.[39;49;00m$
[37m[39;49;00m$
[37m        If collecting opcode statistics, turn off prediction so that[39;49;00m$
[37m^Istatistics are accurately maintained (the predictions bypass[39;49;00m$
[37m^Ithe opcode frequency counter updates).[39;49;00m$
[37m*/[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36mifdef DYNAMIC_EXECUTION_PROFILE[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine PREDICT(op)^I^Iif (0) goto PRED_##op[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36melse[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine PREDICT(op)^I^Iif (*next_instr == op) goto PRED_##op[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36mdefine PREDICTED(op)^I^IPRED_##op: next_instr++[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine PREDICTED_WITH_ARG(op)^IPRED_##op: oparg = PEEKARG(); next_instr += 3[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[37m/* Stack manipulation macros */[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m/* The stack can grow at most MAXINT deep, as co_nlocals and[39;49;00m$
[37m   co_stacksize are ints. */[39;49;00m[37m[39;49;00m$
[36m#[39;49;00m[36mdefine STACK_LEVEL()^I((int)(stack_pointer - f->f_valuestack))[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine EMPTY()^I^I(STACK_LEVEL() == 0)[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine TOP()^I^I(stack_pointer[-1])[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine SECOND()^I(stack_pointer[-2])[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine THIRD() ^I(stack_pointer[-3])[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine FOURTH()^I(stack_pointer[-4])[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine SET_TOP(v)^I(stack_pointer[-1] = (v))[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine SET_SECOND(v)^I(stack_pointer[-2] = (v))[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine SET_THIRD(v)^I(stack_pointer[-3] = (v))[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine SET_FOURTH(v)^I(stack_pointer[-4] = (v))[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine BASIC_STACKADJ(n)^I(stack_pointer += n)[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine BASIC_PUSH(v)^I(*stack_pointer++ = (v))[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine BASIC_POP()^I(*--stack_pointer)[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36mifdef LLTRACE[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine PUSH(v)^I^I{ (void)(BASIC_PUSH(v), \[39;49;00m[36m[39;49;00m$
[36m                               lltrace && prtrace(TOP(), "push")); \[39;49;00m[36m[39;49;00m$
[36m                               assert(STACK_LEVEL() <= co->co_stacksize); }[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine POP()^I^I((void)(lltrace && prtrace(TOP(), "pop")), BASIC_POP())[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine STACKADJ(n)^I{ (void)(BASIC_STACKADJ(n), \[39;49;00m[36m[39;49;00m$
[36m                               lltrace && prtrace(TOP(), "stackadj")); \[39;49;00m[36m[39;49;00m$
[36m                               assert(STACK_LEVEL() <= co->co_stacksize); }[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine EXT_POP(STACK_POINTER) (lltrace && prtrace(*(STACK_POINTER), "ext_pop"), *--(STACK_POINTER))[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36melse[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine PUSH(v)^I^IBASIC_PUSH(v)[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine POP()^I^IBASIC_POP()[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine STACKADJ(n)^IBASIC_STACKADJ(n)[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine EXT_POP(STACK_POINTER) (*--(STACK_POINTER))[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[37m/* Local variable macros */[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36mdefine GETLOCAL(i)^I(fastlocals[i])[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[37m/* The SETLOCAL() macro must not DECREF the local variable in-place and[39;49;00m$
[37m   then store the new value; it must copy the old value to a temporary[39;49;00m$
[37m   value, then store the new value, and then DECREF the temporary value.[39;49;00m$
[37m   This is because it is possible that during the DECREF the frame is[39;49;00m$
[37m   accessed by other code (e.g. a __del__ method or gc.collect()) and the[39;49;00m$
[37m   variable would be pointing to already-freed memory. */[39;49;00m[37m[39;49;00m$
[36m#[39;49;00m[36mdefine SETLOCAL(i, value)^Ido { PyObject *tmp = GETLOCAL(i); \[39;49;00m[36m[39;49;00m$
[36m^I^I^I^I     GETLOCAL(i) = value; \[39;49;00m[36m[39;49;00m$
[36m                                     Py_XDECREF(tmp); } while (0)[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[37m/* Start of code */[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(f[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
[37m^I^I[39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I[39;49;00m[37m/* push frame */[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(Py_EnterRecursiveCall([33m"[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
[37m^I^I[39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I[39;49;00mtstate->frame[37m [39;49;00m=[37m [39;49;00mf;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(tstate->use_tracing)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(tstate->c_tracefunc[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I[39;49;00m[37m/* tstate->c_tracefunc, if defined, is a[39;49;00m$
[37m^I^I^I   function that will be called on *every* entry[39;49;00m$
[37m^I^I^I   to a code block.  Its return value, if not[39;49;00m$
[37m^I^I^I   None, is a function that will be called at[39;49;00m$
[37m^I^I^I   the start of each executed line of code.[39;49;00m$
[37m^I^I^I   (Actually, the function must return itself[39;49;00m$
[37m^I^I^I   in order to continue tracing.)  The trace[39;49;00m$
[37m^I^I^I   functions are called with three arguments:[39;49;00m$
[37m^I^I^I   a pointer to the current frame, a string[39;49;00m$
[37m^I^I^I   indicating why the function is called, and[39;49;00m$
[37m^I^I^I   an argument which depends on the situation.[39;49;00m$
[37m^I^I^I   The global trace function is also called[39;49;00m$
[37m^I^I^I   whenever an exception is detected. */[39;49;00m[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(call_trace(tstate->c_tracefunc,[37m [39;49;00mtstate->c_traceobj,[37m[39;49;00m$
[37m^I^I^I^I       [39;49;00mf,[37m [39;49;00mPyTrace_CALL,[37m [39;49;00mPy_None))[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[37m/* Trace function raised an error */[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mexit_eval_frame;[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(tstate->c_profilefunc[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I[39;49;00m[37m/* Similar for c_profilefunc, except it needn't[39;49;00m$
[37m^I^I^I   return itself and isn't called for "line" events */[39;49;00m[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(call_trace(tstate->c_profilefunc,[37m[39;49;00m$
[37m^I^I^I^I       [39;49;00mtstate->c_profileobj,[37m[39;49;00m$
[37m^I^I^I^I       [39;49;00mf,[37m [39;49;00mPyTrace_CALL,[37m [39;49;00mPy_None))[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[37m/* Profile function raised an error */[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mexit_eval_frame;[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I[39;49;00m}[37m[39;49;00m$
[37m^I[39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m^I[39;49;00mco[37m [39;49;00m=[37m [39;49;00mf->f_code;[37m[39;49;00m$
[37m^I[39;49;00mnames[37m [39;49;00m=[37m [39;49;00mco->co_names;[37m[39;49;00m$
[37m^I[39;49;00mconsts[37m [39;49;00m=[37m [39;49;00mco->co_consts;[37m[39;49;00m$
[37m^I[39;49;00mfastlocals[37m [39;49;00m=[37m [39;49;00mf->f_localsplus;[37m[39;49;00m$
[37m^I[39;49;00mfreevars[37m [39;49;00m=[37m [39;49;00mf->f_localsplus[37m [39;49;00m+[37m [39;49;00mco->co_nlocals;[37m[39;49;00m$
[37m^I[39;49;00mfirst_instr[37m [39;49;00m=[37m [39;49;00m([36munsigned[39;49;00m[37m [39;49;00m[36mchar[39;49;00m*)[37m [39;49;00mPyString_AS_STRING(co->co_code);[37m[39;49;00m$
[37m^I[39;49;00m[37m/* An explanation is in order for the next line.[39;49;00m$
[37m[39;49;00m$
[37m^I   f->f_lasti now refers to the index of the last instruction[39;49;00m$
[37m^I   executed.  You might think this was obvious from the name, but[39;49;00m$
[37m^I   this wasn't always true before 2.3!  PyFrame_New now sets[39;49;00m$
[37m^I   f->f_lasti to -1 (i.e. the index *before* the first instruction)[39;49;00m$
[37m^I   and YIELD_VALUE doesn't fiddle with f_lasti any more.  So this[39;49;00m$
[37m^I   does work.  Promise. */[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00mnext_instr[37m [39;49;00m=[37m [39;49;00mfirst_instr[37m [39;49;00m+[37m [39;49;00mf->f_lasti[37m [39;49;00m+[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
[37m^I[39;49;00mstack_pointer[37m [39;49;00m=[37m [39;49;00mf->f_stacktop;[37m[39;49;00m$
[37m^I[39;49;00massert(stack_pointer[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m);[37m[39;49;00m$
[37m^I[39;49;00mf->f_stacktop[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m^I[39;49;00m[37m/* remains NULL unless yield suspends frame */[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36mifdef LLTRACE[39;49;00m[36m[39;49;00m$
[37m^I[39;49;00mlltrace[37m [39;49;00m=[37m [39;49;00mPyDict_GetItemString(f->f_globals,[37m [39;49;00m[33m"[39;49;00m[33m__lltrace__[39;49;00m[33m"[39;49;00m)[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mif defined(Py_DEBUG) || defined(LLTRACE)[39;49;00m[36m[39;49;00m$
[37m^I[39;49;00mfilename[37m [39;49;00m=[37m [39;49;00mPyString_AsString(co->co_filename);[37m[39;49;00m$
[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[37m^I[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_NOT;[37m[39;49;00m$
[37m^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
[37m^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPy_None;[37m^I[39;49;00m[37m/* Not a reference, just anything non-NULL */[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(throwflag)[37m [39;49;00m{[37m [39;49;00m[37m/* support for generator.throw() */[39;49;00m[37m[39;49;00m$
[37m^I^I[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_EXCEPTION;[37m[39;49;00m$
[37m^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mon_error;[37m[39;49;00m$
[37m^I[39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m^I[39;49;00m[34mfor[39;49;00m[37m [39;49;00m(;;)[37m [39;49;00m{[37m[39;49;00m$
[36m#[39;49;00m[36mifdef WITH_TSC[39;49;00m[36m[39;49;00m$
[37m^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(inst1[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I[39;49;00m[37m/* Almost surely, the opcode executed a break[39;49;00m$
[37m^I^I^I   or a continue, preventing inst1 from being set[39;49;00m$
[37m^I^I^I   on the way out of the loop.[39;49;00m$
[37m^I^I^I*/[39;49;00m[37m[39;49;00m$
[37m^I^I^I[39;49;00mREAD_TIMESTAMP(inst1);[37m[39;49;00m$
[37m^I^I^I[39;49;00mloop1[37m [39;49;00m=[37m [39;49;00minst1;[37m[39;49;00m$
[37m^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I[39;49;00mdump_tsc(opcode,[37m [39;49;00mticked,[37m [39;49;00minst0,[37m [39;49;00minst1,[37m [39;49;00mloop0,[37m [39;49;00mloop1,[37m[39;49;00m$
[37m^I^I^I [39;49;00mintr0,[37m [39;49;00mintr1);[37m[39;49;00m$
[37m^I^I[39;49;00mticked[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
[37m^I^I[39;49;00minst1[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
[37m^I^I[39;49;00mintr0[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
[37m^I^I[39;49;00mintr1[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
[37m^I^I[39;49;00mREAD_TIMESTAMP(loop0);[37m[39;49;00m$
[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
[37m^I^I[39;49;00massert(stack_pointer[37m [39;49;00m>=[37m [39;49;00mf->f_valuestack);[37m [39;49;00m[37m/* else underflow */[39;49;00m[37m[39;49;00m$
[37m^I^I[39;49;00massert(STACK_LEVEL()[37m [39;49;00m<=[37m [39;49;00mco->co_stacksize);[37m  [39;49;00m[37m/* else overflow */[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[37m/* Do periodic things.  Doing this every time through[39;49;00m$
[37m^I^I   the loop would add too much overhead, so we do it[39;49;00m$
[37m^I^I   only every Nth instruction.  We also do it if[39;49;00m$
[37m^I^I   ``things_to_do'' is set, i.e. when an asynchronous[39;49;00m$
[37m^I^I   event needs attention (e.g. a signal handler or[39;49;00m$
[37m^I^I   async I/O handler); see Py_AddPendingCall() and[39;49;00m$
[37m^I^I   Py_MakePendingCalls() above. */[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(--_Py_Ticker[37m [39;49;00m<[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m                        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(*next_instr[37m [39;49;00m==[37m [39;49;00mSETUP_FINALLY)[37m [39;49;00m{[37m[39;49;00m$
[37m                                [39;49;00m[37m/* Make the last opcode before[39;49;00m$
[37m                                   a try: finally: block uninterruptable. */[39;49;00m[37m[39;49;00m$
[37m                                [39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
[37m                        [39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m_Py_Ticker[37m [39;49;00m=[37m [39;49;00m_Py_CheckInterval;[37m[39;49;00m$
[37m^I^I^I[39;49;00mtstate->tick_counter++;[37m[39;49;00m$
[36m#[39;49;00m[36mifdef WITH_TSC[39;49;00m[36m[39;49;00m$
[37m^I^I^I[39;49;00mticked[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(things_to_do)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(Py_MakePendingCalls()[37m [39;49;00m<[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_EXCEPTION;[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mon_error;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(things_to_do)[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m[37m/* MakePendingCalls() didn't succeed.[39;49;00m$
[37m^I^I^I^I^I   Force early re-execution of this[39;49;00m$
[37m^I^I^I^I^I   "periodic" code, possibly after[39;49;00m$
[37m^I^I^I^I^I   a thread switch */[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m_Py_Ticker[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[36m#[39;49;00m[36mifdef WITH_THREAD[39;49;00m[36m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(interpreter_lock)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[37m/* Give another thread a chance */[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyThreadState_Swap([36mNULL[39;49;00m)[37m [39;49;00m!=[37m [39;49;00mtstate)[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mPy_FatalError([33m"[39;49;00m[33mceval: tstate mix-up[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPyThread_release_lock(interpreter_lock);[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[37m/* Other threads may run now */[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPyThread_acquire_lock(interpreter_lock,[37m [39;49;00m[34m1[39;49;00m);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyThreadState_Swap(tstate)[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mPy_FatalError([33m"[39;49;00m[33mceval: orphan tstate[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[37m/* Check for thread interrupts */[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(tstate->async_exc[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mtstate->async_exc;[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mtstate->async_exc[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mPyErr_SetNone(x);[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mPy_DECREF(x);[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_EXCEPTION;[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mon_error;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
[37m^I^I[39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m^I[39;49;00mfast_next_opcode:[37m[39;49;00m$
[37m^I^I[39;49;00mf->f_lasti[37m [39;49;00m=[37m [39;49;00mINSTR_OFFSET();[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[37m/* line-by-line tracing support */[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(tstate->c_tracefunc[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m[37m [39;49;00m&&[37m [39;49;00m!tstate->tracing)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I[39;49;00m[37m/* see maybe_call_line_trace[39;49;00m$
[37m^I^I^I   for expository comments */[39;49;00m[37m[39;49;00m$
[37m^I^I^I[39;49;00mf->f_stacktop[37m [39;49;00m=[37m [39;49;00mstack_pointer;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00mmaybe_call_line_trace(tstate->c_tracefunc,[37m[39;49;00m$
[37m^I^I^I^I^I^I    [39;49;00mtstate->c_traceobj,[37m[39;49;00m$
[37m^I^I^I^I^I^I    [39;49;00mf,[37m [39;49;00m&instr_lb,[37m [39;49;00m&instr_ub,[37m[39;49;00m$
[37m^I^I^I^I^I^I    [39;49;00m&instr_prev);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[37m/* Reload possibly changed frame fields */[39;49;00m[37m[39;49;00m$
[37m^I^I^I[39;49;00mJUMPTO(f->f_lasti);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(f->f_stacktop[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mstack_pointer[37m [39;49;00m=[37m [39;49;00mf->f_stacktop;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mf->f_stacktop[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[37m/* trace function raised an exception */[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mon_error;[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I[39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[37m/* Extract opcode and argument */[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00mopcode[37m [39;49;00m=[37m [39;49;00mNEXTOP();[37m[39;49;00m$
[37m^I^I[39;49;00moparg[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m   [39;49;00m[37m/* allows oparg to be stored in a register because[39;49;00m$
[37m^I^I^Iit doesn't have to be remembered across a full loop */[39;49;00m[37m[39;49;00m$
[37m^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(HAS_ARG(opcode))[37m[39;49;00m$
[37m^I^I^I[39;49;00moparg[37m [39;49;00m=[37m [39;49;00mNEXTARG();[37m[39;49;00m$
[37m^I  [39;49;00mdispatch_opcode:[37m[39;49;00m$
[36m#[39;49;00m[36mifdef DYNAMIC_EXECUTION_PROFILE[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mifdef DXPAIRS[39;49;00m[36m[39;49;00m$
[37m^I^I[39;49;00mdxpairs[lastopcode][opcode]++;[37m[39;49;00m$
[37m^I^I[39;49;00mlastopcode[37m [39;49;00m=[37m [39;49;00mopcode;[37m[39;49;00m$
[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
[37m^I^I[39;49;00mdxp[opcode]++;[37m[39;49;00m$
[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36mifdef LLTRACE[39;49;00m[36m[39;49;00m$
[37m^I^I[39;49;00m[37m/* Instruction tracing */[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(lltrace)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(HAS_ARG(opcode))[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mprintf([33m"[39;49;00m[33m%d: %d, %d[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m,[37m[39;49;00m$
[37m^I^I^I^I       [39;49;00mf->f_lasti,[37m [39;49;00mopcode,[37m [39;49;00moparg);[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mprintf([33m"[39;49;00m[33m%d: %d[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m,[37m[39;49;00m$
[37m^I^I^I^I       [39;49;00mf->f_lasti,[37m [39;49;00mopcode);[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I[39;49;00m}[37m[39;49;00m$
[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[37m/* Main switch on opcode */[39;49;00m[37m[39;49;00m$
[37m^I^I[39;49;00mREAD_TIMESTAMP(inst0);[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mswitch[39;49;00m[37m [39;49;00m(opcode)[37m [39;49;00m{[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[37m/* BEWARE![39;49;00m$
[37m^I^I   It is essential that any operation that fails sets either[39;49;00m$
[37m^I^I   x to NULL, err to nonzero, or why to anything but WHY_NOT,[39;49;00m$
[37m^I^I   and that no operation that succeeds does this! */[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[37m/* case STOP_CODE: this is an error! */[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mNOP[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mLOAD_FAST[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mGETLOCAL(oparg);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPy_INCREF(x);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPUSH(x);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00mformat_exc_check_arg(PyExc_UnboundLocalError,[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mUNBOUNDLOCAL_ERROR_MSG,[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPyTuple_GetItem(co->co_varnames,[37m [39;49;00moparg));[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mLOAD_CONST[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mGETITEM(consts,[37m [39;49;00moparg);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_INCREF(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPUSH(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00mPREDICTED_WITH_ARG(STORE_FAST);[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSTORE_FAST[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mSETLOCAL(oparg,[37m [39;49;00mv);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00mPREDICTED(POP_TOP);[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mPOP_TOP[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mROT_TWO[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mSECOND();[37m[39;49;00m$
[37m^I^I^I[39;49;00mSET_TOP(w);[37m[39;49;00m$
[37m^I^I^I[39;49;00mSET_SECOND(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mROT_THREE[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mSECOND();[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mTHIRD();[37m[39;49;00m$
[37m^I^I^I[39;49;00mSET_TOP(w);[37m[39;49;00m$
[37m^I^I^I[39;49;00mSET_SECOND(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00mSET_THIRD(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mROT_FOUR[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mu[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mSECOND();[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mTHIRD();[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mFOURTH();[37m[39;49;00m$
[37m^I^I^I[39;49;00mSET_TOP(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mSET_SECOND(w);[37m[39;49;00m$
[37m^I^I^I[39;49;00mSET_THIRD(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00mSET_FOURTH(u);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mDUP_TOP[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_INCREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPUSH(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mDUP_TOPX[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(oparg[37m [39;49;00m==[37m [39;49;00m[34m2[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPy_INCREF(x);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mSECOND();[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPy_INCREF(w);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mSTACKADJ([34m2[39;49;00m);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mSET_SECOND(w);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(oparg[37m [39;49;00m==[37m [39;49;00m[34m3[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPy_INCREF(x);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mSECOND();[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPy_INCREF(w);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTHIRD();[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPy_INCREF(v);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mSTACKADJ([34m3[39;49;00m);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mSET_SECOND(w);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mSET_THIRD(v);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_FatalError([33m"[39;49;00m[33minvalid argument to DUP_TOPX[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I      [39;49;00m[33m"[39;49;00m[33m (bytecode corruption?)[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mUNARY_POSITIVE[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_Positive(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mUNARY_NEGATIVE[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_Negative(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mUNARY_NOT[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyObject_IsTrue(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPy_INCREF(Py_True);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mSET_TOP(Py_True);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m>[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPy_INCREF(Py_False);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mSET_TOP(Py_False);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00mSTACKADJ([34m-1[39;49;00m);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mUNARY_CONVERT[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyObject_Repr(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mUNARY_INVERT[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_Invert(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBINARY_POWER[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_Power(v,[37m [39;49;00mw,[37m [39;49;00mPy_None);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBINARY_MULTIPLY[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_Multiply(v,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBINARY_DIVIDE[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(!_Py_QnewFlag)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_Divide(v,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m[37m/* -Qnew is in effect:^Ifall through to[39;49;00m$
[37m^I^I^I   BINARY_TRUE_DIVIDE */[39;49;00m[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBINARY_TRUE_DIVIDE[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_TrueDivide(v,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBINARY_FLOOR_DIVIDE[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_FloorDivide(v,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBINARY_MODULO[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_Remainder(v,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBINARY_ADD[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyInt_CheckExact(v)[37m [39;49;00m&&[37m [39;49;00mPyInt_CheckExact(w))[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[37m/* INLINE: int + int */[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mregister[39;49;00m[37m [39;49;00m[36mlong[39;49;00m[37m [39;49;00ma,[37m [39;49;00mb,[37m [39;49;00mi;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00ma[37m [39;49;00m=[37m [39;49;00mPyInt_AS_LONG(v);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mb[37m [39;49;00m=[37m [39;49;00mPyInt_AS_LONG(w);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mi[37m [39;49;00m=[37m [39;49;00ma[37m [39;49;00m+[37m [39;49;00mb;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m((i^a)[37m [39;49;00m<[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m&&[37m [39;49;00m(i^b)[37m [39;49;00m<[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mslow_add;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyInt_FromLong(i);[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyString_CheckExact(v)[37m [39;49;00m&&[37m[39;49;00m$
[37m^I^I^I^I [39;49;00mPyString_CheckExact(w))[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mstring_concatenate(v,[37m [39;49;00mw,[37m [39;49;00mf,[37m [39;49;00mnext_instr);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[37m/* string_concatenate consumed the ref to v */[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mskip_decref_vx;[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I  [39;49;00mslow_add:[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_Add(v,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I  [39;49;00mskip_decref_vx:[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBINARY_SUBTRACT[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyInt_CheckExact(v)[37m [39;49;00m&&[37m [39;49;00mPyInt_CheckExact(w))[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[37m/* INLINE: int - int */[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mregister[39;49;00m[37m [39;49;00m[36mlong[39;49;00m[37m [39;49;00ma,[37m [39;49;00mb,[37m [39;49;00mi;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00ma[37m [39;49;00m=[37m [39;49;00mPyInt_AS_LONG(v);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mb[37m [39;49;00m=[37m [39;49;00mPyInt_AS_LONG(w);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mi[37m [39;49;00m=[37m [39;49;00ma[37m [39;49;00m-[37m [39;49;00mb;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m((i^a)[37m [39;49;00m<[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m&&[37m [39;49;00m(i^~b)[37m [39;49;00m<[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mslow_sub;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyInt_FromLong(i);[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I  [39;49;00mslow_sub:[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_Subtract(v,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBINARY_SUBSCR[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyList_CheckExact(v)[37m [39;49;00m&&[37m [39;49;00mPyInt_CheckExact(w))[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[37m/* INLINE: list[int] */[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPy_ssize_t[37m [39;49;00mi[37m [39;49;00m=[37m [39;49;00mPyInt_AsSsize_t(w);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(i[37m [39;49;00m<[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mi[37m [39;49;00m+=[37m [39;49;00mPyList_GET_SIZE(v);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(i[37m [39;49;00m>=[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m&&[37m [39;49;00mi[37m [39;49;00m<[37m [39;49;00mPyList_GET_SIZE(v))[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyList_GET_ITEM(v,[37m [39;49;00mi);[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mPy_INCREF(x);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34melse[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mslow_get;[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m[39;49;00m$
[37m^I^I^I  [39;49;00mslow_get:[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyObject_GetItem(v,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBINARY_LSHIFT[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_Lshift(v,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBINARY_RSHIFT[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_Rshift(v,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBINARY_AND[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_And(v,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBINARY_XOR[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_Xor(v,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBINARY_OR[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_Or(v,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mLIST_APPEND[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyList_Append(v,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPREDICT(JUMP_ABSOLUTE);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mINPLACE_POWER[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_InPlacePower(v,[37m [39;49;00mw,[37m [39;49;00mPy_None);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mINPLACE_MULTIPLY[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_InPlaceMultiply(v,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mINPLACE_DIVIDE[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(!_Py_QnewFlag)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_InPlaceDivide(v,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m[37m/* -Qnew is in effect:^Ifall through to[39;49;00m$
[37m^I^I^I   INPLACE_TRUE_DIVIDE */[39;49;00m[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mINPLACE_TRUE_DIVIDE[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_InPlaceTrueDivide(v,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mINPLACE_FLOOR_DIVIDE[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_InPlaceFloorDivide(v,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mINPLACE_MODULO[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_InPlaceRemainder(v,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mINPLACE_ADD[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyInt_CheckExact(v)[37m [39;49;00m&&[37m [39;49;00mPyInt_CheckExact(w))[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[37m/* INLINE: int + int */[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mregister[39;49;00m[37m [39;49;00m[36mlong[39;49;00m[37m [39;49;00ma,[37m [39;49;00mb,[37m [39;49;00mi;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00ma[37m [39;49;00m=[37m [39;49;00mPyInt_AS_LONG(v);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mb[37m [39;49;00m=[37m [39;49;00mPyInt_AS_LONG(w);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mi[37m [39;49;00m=[37m [39;49;00ma[37m [39;49;00m+[37m [39;49;00mb;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m((i^a)[37m [39;49;00m<[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m&&[37m [39;49;00m(i^b)[37m [39;49;00m<[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mslow_iadd;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyInt_FromLong(i);[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyString_CheckExact(v)[37m [39;49;00m&&[37m[39;49;00m$
[37m^I^I^I^I [39;49;00mPyString_CheckExact(w))[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mstring_concatenate(v,[37m [39;49;00mw,[37m [39;49;00mf,[37m [39;49;00mnext_instr);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[37m/* string_concatenate consumed the ref to v */[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mskip_decref_v;[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I  [39;49;00mslow_iadd:[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_InPlaceAdd(v,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I  [39;49;00mskip_decref_v:[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mINPLACE_SUBTRACT[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyInt_CheckExact(v)[37m [39;49;00m&&[37m [39;49;00mPyInt_CheckExact(w))[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[37m/* INLINE: int - int */[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mregister[39;49;00m[37m [39;49;00m[36mlong[39;49;00m[37m [39;49;00ma,[37m [39;49;00mb,[37m [39;49;00mi;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00ma[37m [39;49;00m=[37m [39;49;00mPyInt_AS_LONG(v);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mb[37m [39;49;00m=[37m [39;49;00mPyInt_AS_LONG(w);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mi[37m [39;49;00m=[37m [39;49;00ma[37m [39;49;00m-[37m [39;49;00mb;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m((i^a)[37m [39;49;00m<[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m&&[37m [39;49;00m(i^~b)[37m [39;49;00m<[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mslow_isub;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyInt_FromLong(i);[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I  [39;49;00mslow_isub:[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_InPlaceSubtract(v,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mINPLACE_LSHIFT[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_InPlaceLshift(v,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mINPLACE_RSHIFT[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_InPlaceRshift(v,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mINPLACE_AND[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_InPlaceAnd(v,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mINPLACE_XOR[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_InPlaceXor(v,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mINPLACE_OR[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_InPlaceOr(v,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSLICE[39;49;00m+[34m0[39;49;00m:[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSLICE[39;49;00m+[34m1[39;49;00m:[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSLICE[39;49;00m+[34m2[39;49;00m:[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSLICE[39;49;00m+[34m3[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m((opcode-SLICE)[37m [39;49;00m&[37m [39;49;00m[34m2[39;49;00m)[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m((opcode-SLICE)[37m [39;49;00m&[37m [39;49;00m[34m1[39;49;00m)[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00mu[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mapply_slice(u,[37m [39;49;00mv,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(u);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_XDECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_XDECREF(w);[37m[39;49;00m$
[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSTORE_SLICE[39;49;00m+[34m0[39;49;00m:[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSTORE_SLICE[39;49;00m+[34m1[39;49;00m:[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSTORE_SLICE[39;49;00m+[34m2[39;49;00m:[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSTORE_SLICE[39;49;00m+[34m3[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m((opcode-STORE_SLICE)[37m [39;49;00m&[37m [39;49;00m[34m2[39;49;00m)[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m((opcode-STORE_SLICE)[37m [39;49;00m&[37m [39;49;00m[34m1[39;49;00m)[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00mu[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mt[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00massign_slice(u,[37m [39;49;00mv,[37m [39;49;00mw,[37m [39;49;00mt);[37m [39;49;00m[37m/* u[v:w] = t */[39;49;00m[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(t);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(u);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_XDECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_XDECREF(w);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mDELETE_SLICE[39;49;00m+[34m0[39;49;00m:[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mDELETE_SLICE[39;49;00m+[34m1[39;49;00m:[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mDELETE_SLICE[39;49;00m+[34m2[39;49;00m:[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mDELETE_SLICE[39;49;00m+[34m3[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m((opcode-DELETE_SLICE)[37m [39;49;00m&[37m [39;49;00m[34m2[39;49;00m)[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m((opcode-DELETE_SLICE)[37m [39;49;00m&[37m [39;49;00m[34m1[39;49;00m)[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00mu[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00massign_slice(u,[37m [39;49;00mv,[37m [39;49;00mw,[37m [39;49;00m(PyObject[37m [39;49;00m*)[36mNULL[39;49;00m);[37m[39;49;00m$
[37m^I^I^I^I^I^I^I[39;49;00m[37m/* del u[v:w] */[39;49;00m[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(u);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_XDECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_XDECREF(w);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSTORE_SUBSCR[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mSECOND();[37m[39;49;00m$
[37m^I^I^I[39;49;00mu[37m [39;49;00m=[37m [39;49;00mTHIRD();[37m[39;49;00m$
[37m^I^I^I[39;49;00mSTACKADJ([34m-3[39;49;00m);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[37m/* v[w] = u */[39;49;00m[37m[39;49;00m$
[37m^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyObject_SetItem(v,[37m [39;49;00mw,[37m [39;49;00mu);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(u);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mDELETE_SUBSCR[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mSECOND();[37m[39;49;00m$
[37m^I^I^I[39;49;00mSTACKADJ([34m-2[39;49;00m);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[37m/* del v[w] */[39;49;00m[37m[39;49;00m$
[37m^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyObject_DelItem(v,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mPRINT_EXPR[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPySys_GetObject([33m"[39;49;00m[33mdisplayhook[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(w[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPyErr_SetString(PyExc_RuntimeError,[37m[39;49;00m$
[37m^I^I^I^I^I^I[39;49;00m[33m"[39;49;00m[33mlost sys.displayhook[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00m[34m-1[39;49;00m;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyTuple_Pack([34m1[39;49;00m,[37m [39;49;00mv);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00m[34m-1[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPyEval_CallObject(w,[37m [39;49;00mx);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPy_XDECREF(w);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(w[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00m[34m-1[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_XDECREF(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mPRINT_ITEM_TO[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mstream[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00m[37m/* fall through to PRINT_ITEM */[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mPRINT_ITEM[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(stream[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m[37m [39;49;00m||[37m [39;49;00mstream[37m [39;49;00m==[37m [39;49;00mPy_None)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPySys_GetObject([33m"[39;49;00m[33mstdout[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(w[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mPyErr_SetString(PyExc_RuntimeError,[37m[39;49;00m$
[37m^I^I^I^I^I^I^I[39;49;00m[33m"[39;49;00m[33mlost sys.stdout[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00m[34m-1[39;49;00m;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m[37m/* PyFile_SoftSpace() can exececute arbitrary code[39;49;00m$
[37m^I^I^I   if sys.stdout is an instance with a __getattr__.[39;49;00m$
[37m^I^I^I   If __getattr__ raises an exception, w will[39;49;00m$
[37m^I^I^I   be freed, so we need to prevent that temporarily. */[39;49;00m[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_XINCREF(w);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(w[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m[37m [39;49;00m&&[37m [39;49;00mPyFile_SoftSpace(w,[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m$
[37m^I^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyFile_WriteString([33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m^I^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyFile_WriteObject(v,[37m [39;49;00mw,[37m [39;49;00mPy_PRINT_RAW);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I    [39;49;00m[37m/* XXX move into writeobject() ? */[39;49;00m[37m[39;49;00m$
[37m^I^I^I    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyString_Check(v))[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[36mchar[39;49;00m[37m [39;49;00m*s[37m [39;49;00m=[37m [39;49;00mPyString_AS_STRING(v);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPy_ssize_t[37m [39;49;00mlen[37m [39;49;00m=[37m [39;49;00mPyString_GET_SIZE(v);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(len[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m||[37m[39;49;00m$
[37m^I^I^I^I    [39;49;00m!isspace(Py_CHARMASK(s[len[34m-1[39;49;00m]))[37m [39;49;00m||[37m[39;49;00m$
[37m^I^I^I^I    [39;49;00ms[len[34m-1[39;49;00m][37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mPyFile_SoftSpace(w,[37m [39;49;00m[34m1[39;49;00m);[37m[39;49;00m$
[37m^I^I^I    [39;49;00m}[37m[39;49;00m$
[36m#[39;49;00m[36mifdef Py_USING_UNICODE[39;49;00m[36m[39;49;00m$
[37m^I^I^I    [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyUnicode_Check(v))[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPy_UNICODE[37m [39;49;00m*s[37m [39;49;00m=[37m [39;49;00mPyUnicode_AS_UNICODE(v);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPy_ssize_t[37m [39;49;00mlen[37m [39;49;00m=[37m [39;49;00mPyUnicode_GET_SIZE(v);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(len[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m||[37m[39;49;00m$
[37m^I^I^I^I    [39;49;00m!Py_UNICODE_ISSPACE(s[len[34m-1[39;49;00m])[37m [39;49;00m||[37m[39;49;00m$
[37m^I^I^I^I    [39;49;00ms[len[34m-1[39;49;00m][37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
[37m^I^I^I^I    [39;49;00mPyFile_SoftSpace(w,[37m [39;49;00m[34m1[39;49;00m);[37m[39;49;00m$
[37m^I^I^I    [39;49;00m}[37m[39;49;00m$
[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
[37m^I^I^I    [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
[37m^I^I^I    ^I[39;49;00mPyFile_SoftSpace(w,[37m [39;49;00m[34m1[39;49;00m);[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_XDECREF(w);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_XDECREF(stream);[37m[39;49;00m$
[37m^I^I^I[39;49;00mstream[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mPRINT_NEWLINE_TO[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mstream[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00m[37m/* fall through to PRINT_NEWLINE */[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mPRINT_NEWLINE[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(stream[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m[37m [39;49;00m||[37m [39;49;00mstream[37m [39;49;00m==[37m [39;49;00mPy_None)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPySys_GetObject([33m"[39;49;00m[33mstdout[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(w[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mPyErr_SetString(PyExc_RuntimeError,[37m[39;49;00m$
[37m^I^I^I^I^I^I^I[39;49;00m[33m"[39;49;00m[33mlost sys.stdout[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(w[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyFile_WriteString([33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mPyFile_SoftSpace(w,[37m [39;49;00m[34m0[39;49;00m);[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_XDECREF(stream);[37m[39;49;00m$
[37m^I^I^I[39;49;00mstream[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36mifdef CASE_TOO_BIG[39;49;00m[36m[39;49;00m$
[37m^I^I[39;49;00m[34mdefault[39;49;00m:[37m [39;49;00m[34mswitch[39;49;00m[37m [39;49;00m(opcode)[37m [39;49;00m{[37m[39;49;00m$
[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mRAISE_VARARGS[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mu[37m [39;49;00m=[37m [39;49;00mv[37m [39;49;00m=[37m [39;49;00mw[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mswitch[39;49;00m[37m [39;49;00m(oparg)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[34m3[39;49;00m:[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mu[37m [39;49;00m=[37m [39;49;00mPOP();[37m [39;49;00m[37m/* traceback */[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[37m/* Fallthrough */[39;49;00m[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[34m2[39;49;00m:[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m [39;49;00m[37m/* value */[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[37m/* Fallthrough */[39;49;00m[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[34m1[39;49;00m:[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m [39;49;00m[37m/* exc */[39;49;00m[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[34m0[39;49;00m:[37m [39;49;00m[37m/* Fallthrough */[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mdo_raise(w,[37m [39;49;00mv,[37m [39;49;00mu);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mdefault[39;49;00m:[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPyErr_SetString(PyExc_SystemError,[37m[39;49;00m$
[37m^I^I^I^I^I   [39;49;00m[33m"[39;49;00m[33mbad RAISE_VARARGS oparg[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_EXCEPTION;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mLOAD_LOCALS[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m((x[37m [39;49;00m=[37m [39;49;00mf->f_locals)[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPy_INCREF(x);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPUSH(x);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00mPyErr_SetString(PyExc_SystemError,[37m [39;49;00m[33m"[39;49;00m[33mno locals[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mRETURN_VALUE[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mretval[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_RETURN;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_block_end;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mYIELD_VALUE[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mretval[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mf->f_stacktop[37m [39;49;00m=[37m [39;49;00mstack_pointer;[37m[39;49;00m$
[37m^I^I^I[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_YIELD;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_yield;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mEXEC_STMT[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mSECOND();[37m[39;49;00m$
[37m^I^I^I[39;49;00mu[37m [39;49;00m=[37m [39;49;00mTHIRD();[37m[39;49;00m$
[37m^I^I^I[39;49;00mSTACKADJ([34m-3[39;49;00m);[37m[39;49;00m$
[37m^I^I^I[39;49;00mREAD_TIMESTAMP(intr0);[37m[39;49;00m$
[37m^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00mexec_statement(f,[37m [39;49;00mu,[37m [39;49;00mv,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I[39;49;00mREAD_TIMESTAMP(intr1);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(u);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mPOP_BLOCK[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPyTryBlock[37m [39;49;00m*b[37m [39;49;00m=[37m [39;49;00mPyFrame_BlockPop(f);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(STACK_LEVEL()[37m [39;49;00m>[37m [39;49;00mb->b_level)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mEND_FINALLY[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyInt_Check(v))[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00m([34menum[39;49;00m[37m [39;49;00mwhy_code)[37m [39;49;00mPyInt_AS_LONG(v);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00massert(why[37m [39;49;00m!=[37m [39;49;00mWHY_YIELD);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(why[37m [39;49;00m==[37m [39;49;00mWHY_RETURN[37m [39;49;00m||[37m[39;49;00m$
[37m^I^I^I^I    [39;49;00mwhy[37m [39;49;00m==[37m [39;49;00mWHY_CONTINUE)[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mretval[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyExceptionClass_Check(v)[37m [39;49;00m||[37m [39;49;00mPyString_Check(v))[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mu[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPyErr_Restore(v,[37m [39;49;00mw,[37m [39;49;00mu);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_RERAISE;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(v[37m [39;49;00m!=[37m [39;49;00mPy_None)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPyErr_SetString(PyExc_SystemError,[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m[33m"[39;49;00m[33m'finally' pops bad exception[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_EXCEPTION;[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBUILD_CLASS[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mu[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mSECOND();[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mTHIRD();[37m[39;49;00m$
[37m^I^I^I[39;49;00mSTACKADJ([34m-2[39;49;00m);[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mbuild_class(u,[37m [39;49;00mv,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(u);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSTORE_NAME[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mGETITEM(names,[37m [39;49;00moparg);[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m((x[37m [39;49;00m=[37m [39;49;00mf->f_locals)[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyDict_CheckExact(x))[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyDict_SetItem(x,[37m [39;49;00mw,[37m [39;49;00mv);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34melse[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyObject_SetItem(x,[37m [39;49;00mw,[37m [39;49;00mv);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00mPyErr_Format(PyExc_SystemError,[37m[39;49;00m$
[37m^I^I^I^I     [39;49;00m[33m"[39;49;00m[33mno locals found when storing %s[39;49;00m[33m"[39;49;00m,[37m[39;49;00m$
[37m^I^I^I^I     [39;49;00mPyObject_REPR(w));[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mDELETE_NAME[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mGETITEM(names,[37m [39;49;00moparg);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m((x[37m [39;49;00m=[37m [39;49;00mf->f_locals)[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m((err[37m [39;49;00m=[37m [39;49;00mPyObject_DelItem(x,[37m [39;49;00mw))[37m [39;49;00m!=[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mformat_exc_check_arg(PyExc_NameError,[37m[39;49;00m$
[37m^I^I^I^I^I^I^I^I[39;49;00mNAME_ERROR_MSG[37m [39;49;00m,w);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00mPyErr_Format(PyExc_SystemError,[37m[39;49;00m$
[37m^I^I^I^I     [39;49;00m[33m"[39;49;00m[33mno locals when deleting %s[39;49;00m[33m"[39;49;00m,[37m[39;49;00m$
[37m^I^I^I^I     [39;49;00mPyObject_REPR(w));[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00mPREDICTED_WITH_ARG(UNPACK_SEQUENCE);[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mUNPACK_SEQUENCE[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyTuple_CheckExact(v)[37m [39;49;00m&&[37m [39;49;00mPyTuple_GET_SIZE(v)[37m [39;49;00m==[37m [39;49;00moparg)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPyObject[37m [39;49;00m**items[37m [39;49;00m=[37m [39;49;00m((PyTupleObject[37m [39;49;00m*)v)->ob_item;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(oparg--)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mitems[oparg];[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mPy_INCREF(w);[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mPUSH(w);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyList_CheckExact(v)[37m [39;49;00m&&[37m [39;49;00mPyList_GET_SIZE(v)[37m [39;49;00m==[37m [39;49;00moparg)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPyObject[37m [39;49;00m**items[37m [39;49;00m=[37m [39;49;00m((PyListObject[37m [39;49;00m*)v)->ob_item;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(oparg--)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mitems[oparg];[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mPy_INCREF(w);[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mPUSH(w);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(unpack_iterable(v,[37m [39;49;00moparg,[37m[39;49;00m$
[37m^I^I^I^I^I^I [39;49;00mstack_pointer[37m [39;49;00m+[37m [39;49;00moparg))[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mstack_pointer[37m [39;49;00m+=[37m [39;49;00moparg;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyErr_ExceptionMatches(PyExc_TypeError))[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mPyErr_SetString(PyExc_TypeError,[37m[39;49;00m$
[37m^I^I^I^I^I^I[39;49;00m[33m"[39;49;00m[33munpack non-sequence[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_EXCEPTION;[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSTORE_ATTR[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mGETITEM(names,[37m [39;49;00moparg);[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mu[37m [39;49;00m=[37m [39;49;00mSECOND();[37m[39;49;00m$
[37m^I^I^I[39;49;00mSTACKADJ([34m-2[39;49;00m);[37m[39;49;00m$
[37m^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyObject_SetAttr(v,[37m [39;49;00mw,[37m [39;49;00mu);[37m [39;49;00m[37m/* v.w = u */[39;49;00m[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(u);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mDELETE_ATTR[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mGETITEM(names,[37m [39;49;00moparg);[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyObject_SetAttr(v,[37m [39;49;00mw,[37m [39;49;00m(PyObject[37m [39;49;00m*)[36mNULL[39;49;00m);[37m[39;49;00m$
[37m^I^I^I^I^I^I^I[39;49;00m[37m/* del v.w */[39;49;00m[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSTORE_GLOBAL[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mGETITEM(names,[37m [39;49;00moparg);[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyDict_SetItem(f->f_globals,[37m [39;49;00mw,[37m [39;49;00mv);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mDELETE_GLOBAL[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mGETITEM(names,[37m [39;49;00moparg);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m((err[37m [39;49;00m=[37m [39;49;00mPyDict_DelItem(f->f_globals,[37m [39;49;00mw))[37m [39;49;00m!=[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mformat_exc_check_arg([37m[39;49;00m$
[37m^I^I^I^I    [39;49;00mPyExc_NameError,[37m [39;49;00mGLOBAL_NAME_ERROR_MSG,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mLOAD_NAME[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mGETITEM(names,[37m [39;49;00moparg);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m((v[37m [39;49;00m=[37m [39;49;00mf->f_locals)[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPyErr_Format(PyExc_SystemError,[37m[39;49;00m$
[37m^I^I^I^I^I     [39;49;00m[33m"[39;49;00m[33mno locals when loading %s[39;49;00m[33m"[39;49;00m,[37m[39;49;00m$
[37m^I^I^I^I^I     [39;49;00mPyObject_REPR(w));[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyDict_CheckExact(v))[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyDict_GetItem(v,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPy_XINCREF(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyObject_GetItem(v,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m[37m [39;49;00m&&[37m [39;49;00mPyErr_Occurred())[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(!PyErr_ExceptionMatches(PyExc_KeyError))[37m[39;49;00m$
[37m^I^I^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mPyErr_Clear();[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyDict_GetItem(f->f_globals,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyDict_GetItem(f->f_builtins,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I^I^I[39;49;00mformat_exc_check_arg([37m[39;49;00m$
[37m^I^I^I^I^I^I^I    [39;49;00mPyExc_NameError,[37m[39;49;00m$
[37m^I^I^I^I^I^I^I    [39;49;00mNAME_ERROR_MSG[37m [39;49;00m,w);[37m[39;49;00m$
[37m^I^I^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPy_INCREF(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00mPUSH(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mLOAD_GLOBAL[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mGETITEM(names,[37m [39;49;00moparg);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyString_CheckExact(w))[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[37m/* Inline the PyDict_GetItem() calls.[39;49;00m$
[37m^I^I^I^I   WARNING: this is an extreme speed hack.[39;49;00m$
[37m^I^I^I^I   Do not try this at home. */[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[36mlong[39;49;00m[37m [39;49;00mhash[37m [39;49;00m=[37m [39;49;00m((PyStringObject[37m [39;49;00m*)w)->ob_shash;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(hash[37m [39;49;00m!=[37m [39;49;00m[34m-1[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mPyDictObject[37m [39;49;00m*d;[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mPyDictEntry[37m [39;49;00m*e;[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00md[37m [39;49;00m=[37m [39;49;00m(PyDictObject[37m [39;49;00m*)(f->f_globals);[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00me[37m [39;49;00m=[37m [39;49;00md->ma_lookup(d,[37m [39;49;00mw,[37m [39;49;00mhash);[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(e[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m^I^I^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00me->me_value;[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I^I^I[39;49;00mPy_INCREF(x);[37m[39;49;00m$
[37m^I^I^I^I^I^I[39;49;00mPUSH(x);[37m[39;49;00m$
[37m^I^I^I^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00md[37m [39;49;00m=[37m [39;49;00m(PyDictObject[37m [39;49;00m*)(f->f_builtins);[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00me[37m [39;49;00m=[37m [39;49;00md->ma_lookup(d,[37m [39;49;00mw,[37m [39;49;00mhash);[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(e[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m^I^I^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00me->me_value;[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I^I^I[39;49;00mPy_INCREF(x);[37m[39;49;00m$
[37m^I^I^I^I^I^I[39;49;00mPUSH(x);[37m[39;49;00m$
[37m^I^I^I^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mload_global_error;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m[37m/* This is the un-inlined version of the code above */[39;49;00m[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyDict_GetItem(f->f_globals,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyDict_GetItem(f->f_builtins,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I  [39;49;00mload_global_error:[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mformat_exc_check_arg([37m[39;49;00m$
[37m^I^I^I^I^I^I    [39;49;00mPyExc_NameError,[37m[39;49;00m$
[37m^I^I^I^I^I^I    [39;49;00mGLOBAL_NAME_ERROR_MSG,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_INCREF(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPUSH(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mDELETE_FAST[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mGETLOCAL(oparg);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mSETLOCAL(oparg,[37m [39;49;00m[36mNULL[39;49;00m);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00mformat_exc_check_arg([37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPyExc_UnboundLocalError,[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mUNBOUNDLOCAL_ERROR_MSG,[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPyTuple_GetItem(co->co_varnames,[37m [39;49;00moparg)[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mLOAD_CLOSURE[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mfreevars[oparg];[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_INCREF(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPUSH(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mLOAD_DEREF[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mfreevars[oparg];[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPyCell_Get(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(w[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPUSH(w);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00m[34m-1[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[37m/* Don't stomp existing exception */[39;49;00m[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyErr_Occurred())[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(oparg[37m [39;49;00m<[37m [39;49;00mPyTuple_GET_SIZE(co->co_cellvars))[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPyTuple_GET_ITEM(co->co_cellvars,[37m[39;49;00m$
[37m^I^I^I^I^I^I       [39;49;00moparg);[37m[39;49;00m$
[37m^I^I^I       [39;49;00mformat_exc_check_arg([37m[39;49;00m$
[37m^I^I^I^I       [39;49;00mPyExc_UnboundLocalError,[37m[39;49;00m$
[37m^I^I^I^I       [39;49;00mUNBOUNDLOCAL_ERROR_MSG,[37m[39;49;00m$
[37m^I^I^I^I       [39;49;00mv);[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I       [39;49;00mv[37m [39;49;00m=[37m [39;49;00mPyTuple_GET_ITEM([37m[39;49;00m$
[37m^I^I^I^I^I      [39;49;00mco->co_freevars,[37m[39;49;00m$
[37m^I^I^I^I^I      [39;49;00moparg[37m [39;49;00m-[37m [39;49;00mPyTuple_GET_SIZE(co->co_cellvars));[37m[39;49;00m$
[37m^I^I^I       [39;49;00mformat_exc_check_arg([37m[39;49;00m$
[37m^I^I^I^I       [39;49;00mPyExc_NameError,[37m[39;49;00m$
[37m^I^I^I^I       [39;49;00mUNBOUNDFREE_ERROR_MSG,[37m[39;49;00m$
[37m^I^I^I^I       [39;49;00mv);[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSTORE_DEREF[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mfreevars[oparg];[37m[39;49;00m$
[37m^I^I^I[39;49;00mPyCell_Set(x,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBUILD_TUPLE[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyTuple_New(oparg);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mfor[39;49;00m[37m [39;49;00m(;[37m [39;49;00m--oparg[37m [39;49;00m>=[37m [39;49;00m[34m0[39;49;00m;)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mPyTuple_SET_ITEM(x,[37m [39;49;00moparg,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPUSH(x);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBUILD_LIST[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m  [39;49;00mPyList_New(oparg);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mfor[39;49;00m[37m [39;49;00m(;[37m [39;49;00m--oparg[37m [39;49;00m>=[37m [39;49;00m[34m0[39;49;00m;)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mPyList_SET_ITEM(x,[37m [39;49;00moparg,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPUSH(x);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBUILD_MAP[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyDict_New();[37m[39;49;00m$
[37m^I^I^I[39;49;00mPUSH(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mLOAD_ATTR[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mGETITEM(names,[37m [39;49;00moparg);[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyObject_GetAttr(v,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mCOMPARE_OP[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyInt_CheckExact(w)[37m [39;49;00m&&[37m [39;49;00mPyInt_CheckExact(v))[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[37m/* INLINE: cmp(int, int) */[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mregister[39;49;00m[37m [39;49;00m[36mlong[39;49;00m[37m [39;49;00ma,[37m [39;49;00mb;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mregister[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mres;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00ma[37m [39;49;00m=[37m [39;49;00mPyInt_AS_LONG(v);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mb[37m [39;49;00m=[37m [39;49;00mPyInt_AS_LONG(w);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mswitch[39;49;00m[37m [39;49;00m(oparg)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mPyCmp_LT[39;49;00m:[37m [39;49;00mres[37m [39;49;00m=[37m [39;49;00ma[37m [39;49;00m<[37m  [39;49;00mb;[37m [39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mPyCmp_LE[39;49;00m:[37m [39;49;00mres[37m [39;49;00m=[37m [39;49;00ma[37m [39;49;00m<=[37m [39;49;00mb;[37m [39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mPyCmp_EQ[39;49;00m:[37m [39;49;00mres[37m [39;49;00m=[37m [39;49;00ma[37m [39;49;00m==[37m [39;49;00mb;[37m [39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mPyCmp_NE[39;49;00m:[37m [39;49;00mres[37m [39;49;00m=[37m [39;49;00ma[37m [39;49;00m!=[37m [39;49;00mb;[37m [39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mPyCmp_GT[39;49;00m:[37m [39;49;00mres[37m [39;49;00m=[37m [39;49;00ma[37m [39;49;00m>[37m  [39;49;00mb;[37m [39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mPyCmp_GE[39;49;00m:[37m [39;49;00mres[37m [39;49;00m=[37m [39;49;00ma[37m [39;49;00m>=[37m [39;49;00mb;[37m [39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mPyCmp_IS[39;49;00m:[37m [39;49;00mres[37m [39;49;00m=[37m [39;49;00mv[37m [39;49;00m==[37m [39;49;00mw;[37m [39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mPyCmp_IS_NOT[39;49;00m:[37m [39;49;00mres[37m [39;49;00m=[37m [39;49;00mv[37m [39;49;00m!=[37m [39;49;00mw;[37m [39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mdefault[39;49;00m:[37m [39;49;00m[34mgoto[39;49;00m[37m [39;49;00mslow_compare;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mres[37m [39;49;00m?[37m [39;49;00mPy_True[37m [39;49;00m:[37m [39;49;00mPy_False;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPy_INCREF(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I  [39;49;00mslow_compare:[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mcmp_outcome(oparg,[37m [39;49;00mv,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00mPREDICT(JUMP_IF_FALSE);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPREDICT(JUMP_IF_TRUE);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mIMPORT_NAME[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mGETITEM(names,[37m [39;49;00moparg);[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyDict_GetItemString(f->f_builtins,[37m [39;49;00m[33m"[39;49;00m[33m__import__[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPyErr_SetString(PyExc_ImportError,[37m[39;49;00m$
[37m^I^I^I^I^I^I[39;49;00m[33m"[39;49;00m[33m__import__ not found[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mu[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyInt_AsLong(u)[37m [39;49;00m!=[37m [39;49;00m[34m-1[39;49;00m[37m [39;49;00m||[37m [39;49;00mPyErr_Occurred())[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPyTuple_Pack([34m5[39;49;00m,[37m[39;49;00m$
[37m^I^I^I^I^I    [39;49;00mw,[37m[39;49;00m$
[37m^I^I^I^I^I    [39;49;00mf->f_globals,[37m[39;49;00m$
[37m^I^I^I^I^I    [39;49;00mf->f_locals[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m[37m [39;49;00m?[37m[39;49;00m$
[37m^I^I^I^I^I^I  [39;49;00mPy_None[37m [39;49;00m:[37m [39;49;00mf->f_locals,[37m[39;49;00m$
[37m^I^I^I^I^I    [39;49;00mv,[37m[39;49;00m$
[37m^I^I^I^I^I    [39;49;00mu);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPyTuple_Pack([34m4[39;49;00m,[37m[39;49;00m$
[37m^I^I^I^I^I    [39;49;00mw,[37m[39;49;00m$
[37m^I^I^I^I^I    [39;49;00mf->f_globals,[37m[39;49;00m$
[37m^I^I^I^I^I    [39;49;00mf->f_locals[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m[37m [39;49;00m?[37m[39;49;00m$
[37m^I^I^I^I^I^I  [39;49;00mPy_None[37m [39;49;00m:[37m [39;49;00mf->f_locals,[37m[39;49;00m$
[37m^I^I^I^I^I    [39;49;00mv);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(u);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(w[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mu[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00mREAD_TIMESTAMP(intr0);[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyEval_CallObject(x,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I[39;49;00mREAD_TIMESTAMP(intr1);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mIMPORT_STAR[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mPyFrame_FastToLocals(f);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m((x[37m [39;49;00m=[37m [39;49;00mf->f_locals)[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPyErr_SetString(PyExc_SystemError,[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m[33m"[39;49;00m[33mno locals found during 'import *'[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00mREAD_TIMESTAMP(intr0);[37m[39;49;00m$
[37m^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00mimport_all_from(x,[37m [39;49;00mv);[37m[39;49;00m$
[37m^I^I^I[39;49;00mREAD_TIMESTAMP(intr1);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPyFrame_LocalsToFast(f,[37m [39;49;00m[34m0[39;49;00m);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mIMPORT_FROM[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mGETITEM(names,[37m [39;49;00moparg);[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mREAD_TIMESTAMP(intr0);[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mimport_from(v,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I[39;49;00mREAD_TIMESTAMP(intr1);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPUSH(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mJUMP_FORWARD[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mJUMPBY(oparg);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00mPREDICTED_WITH_ARG(JUMP_IF_FALSE);[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mJUMP_IF_FALSE[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(w[37m [39;49;00m==[37m [39;49;00mPy_True)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPREDICT(POP_TOP);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(w[37m [39;49;00m==[37m [39;49;00mPy_False)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mJUMPBY(oparg);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyObject_IsTrue(w);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m>[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m^I^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mJUMPBY(oparg);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00mPREDICTED_WITH_ARG(JUMP_IF_TRUE);[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mJUMP_IF_TRUE[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(w[37m [39;49;00m==[37m [39;49;00mPy_False)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPREDICT(POP_TOP);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(w[37m [39;49;00m==[37m [39;49;00mPy_True)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mJUMPBY(oparg);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyObject_IsTrue(w);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m>[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mJUMPBY(oparg);[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00mPREDICTED_WITH_ARG(JUMP_ABSOLUTE);[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mJUMP_ABSOLUTE[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mJUMPTO(oparg);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mGET_ITER[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00m[37m/* before: [obj]; after [getiter(obj)] */[39;49;00m[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyObject_GetIter(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPREDICT(FOR_ITER);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00mSTACKADJ([34m-1[39;49;00m);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00mPREDICTED_WITH_ARG(FOR_ITER);[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mFOR_ITER[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00m[37m/* before: [iter]; after: [iter, iter()] *or* [] */[39;49;00m[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00m(*v->ob_type->tp_iternext)(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPUSH(x);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPREDICT(STORE_FAST);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPREDICT(UNPACK_SEQUENCE);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyErr_Occurred())[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(!PyErr_ExceptionMatches(PyExc_StopIteration))[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPyErr_Clear();[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m[37m/* iterator ended normally */[39;49;00m[37m[39;49;00m$
[37m ^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mJUMPBY(oparg);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBREAK_LOOP[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_BREAK;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_block_end;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mCONTINUE_LOOP[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mretval[37m [39;49;00m=[37m [39;49;00mPyInt_FromLong(oparg);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(!retval)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_CONTINUE;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_block_end;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSETUP_LOOP[39;49;00m:[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSETUP_EXCEPT[39;49;00m:[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSETUP_FINALLY[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00m[37m/* NOTE: If you add any new block-setup opcodes that are not try/except/finally[39;49;00m$
[37m^I^I^I   handlers, you may need to update the PyGen_NeedsFinalizing() function. */[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I^I[39;49;00mPyFrame_BlockSetup(f,[37m [39;49;00mopcode,[37m [39;49;00mINSTR_OFFSET()[37m [39;49;00m+[37m [39;49;00moparg,[37m[39;49;00m$
[37m^I^I^I^I^I   [39;49;00mSTACK_LEVEL());[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mWITH_CLEANUP[39;49;00m:[37m[39;49;00m$
[37m^I^I[39;49;00m{[37m[39;49;00m$
[37m^I^I^I[39;49;00m[37m/* TOP is the context.__exit__ bound method.[39;49;00m$
[37m^I^I^I   Below that are 1-3 values indicating how/why[39;49;00m$
[37m^I^I^I   we entered the finally clause:[39;49;00m$
[37m^I^I^I   - SECOND = None[39;49;00m$
[37m^I^I^I   - (SECOND, THIRD) = (WHY_{RETURN,CONTINUE}), retval[39;49;00m$
[37m^I^I^I   - SECOND = WHY_*; no retval below it[39;49;00m$
[37m^I^I^I   - (SECOND, THIRD, FOURTH) = exc_info()[39;49;00m$
[37m^I^I^I   In the last case, we must call[39;49;00m$
[37m^I^I^I     TOP(SECOND, THIRD, FOURTH)[39;49;00m$
[37m^I^I^I   otherwise we must call[39;49;00m$
[37m^I^I^I     TOP(None, None, None)[39;49;00m$
[37m[39;49;00m$
[37m^I^I^I   In addition, if the stack represents an exception,[39;49;00m$
[37m^I^I^I   *and* the function call returns a 'true' value, we[39;49;00m$
[37m^I^I^I   "zap" this information, to prevent END_FINALLY from[39;49;00m$
[37m^I^I^I   re-raising the exception.  (But non-local gotos[39;49;00m$
[37m^I^I^I   should still be resumed.)[39;49;00m$
[37m^I^I^I*/[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mu[37m [39;49;00m=[37m [39;49;00mSECOND();[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyInt_Check(u)[37m [39;49;00m||[37m [39;49;00mu[37m [39;49;00m==[37m [39;49;00mPy_None)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mu[37m [39;49;00m=[37m [39;49;00mv[37m [39;49;00m=[37m [39;49;00mw[37m [39;49;00m=[37m [39;49;00mPy_None;[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTHIRD();[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mFOURTH();[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m[37m/* XXX Not the fastest way to call it... */[39;49;00m[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyObject_CallFunctionObjArgs(x,[37m [39;49;00mu,[37m [39;49;00mv,[37m [39;49;00mw,[37m [39;49;00m[36mNULL[39;49;00m);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m [39;49;00m[37m/* Go to error exit */[39;49;00m[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(u[37m [39;49;00m!=[37m [39;49;00mPy_None[37m [39;49;00m&&[37m [39;49;00mPyObject_IsTrue(x))[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[37m/* There was an exception and a true return */[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPy_DECREF(x);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mTOP();[37m [39;49;00m[37m/* Again */[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mSTACKADJ([34m-3[39;49;00m);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPy_INCREF(Py_None);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mSET_TOP(Py_None);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPy_DECREF(x);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPy_DECREF(u);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[37m/* Let END_FINALLY do its thing */[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPy_DECREF(x);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPy_DECREF(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m^I^I[39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mCALL_FUNCTION[39;49;00m:[37m[39;49;00m$
[37m^I^I[39;49;00m{[37m[39;49;00m$
[37m^I^I^I[39;49;00mPyObject[37m [39;49;00m**sp;[37m[39;49;00m$
[37m^I^I^I[39;49;00mPCALL(PCALL_ALL);[37m[39;49;00m$
[37m^I^I^I[39;49;00msp[37m [39;49;00m=[37m [39;49;00mstack_pointer;[37m[39;49;00m$
[36m#[39;49;00m[36mifdef WITH_TSC[39;49;00m[36m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mcall_function(&sp,[37m [39;49;00moparg,[37m [39;49;00m&intr0,[37m [39;49;00m&intr1);[37m[39;49;00m$
[36m#[39;49;00m[36melse[39;49;00m[36m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mcall_function(&sp,[37m [39;49;00moparg);[37m[39;49;00m$
[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
[37m^I^I^I[39;49;00mstack_pointer[37m [39;49;00m=[37m [39;49;00msp;[37m[39;49;00m$
[37m^I^I^I[39;49;00mPUSH(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m^I^I[39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mCALL_FUNCTION_VAR[39;49;00m:[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mCALL_FUNCTION_KW[39;49;00m:[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mCALL_FUNCTION_VAR_KW[39;49;00m:[37m[39;49;00m$
[37m^I^I[39;49;00m{[37m[39;49;00m$
[37m^I^I    [39;49;00m[36mint[39;49;00m[37m [39;49;00mna[37m [39;49;00m=[37m [39;49;00moparg[37m [39;49;00m&[37m [39;49;00m[34m0xff[39;49;00m;[37m[39;49;00m$
[37m^I^I    [39;49;00m[36mint[39;49;00m[37m [39;49;00mnk[37m [39;49;00m=[37m [39;49;00m(oparg>>[34m8[39;49;00m)[37m [39;49;00m&[37m [39;49;00m[34m0xff[39;49;00m;[37m[39;49;00m$
[37m^I^I    [39;49;00m[36mint[39;49;00m[37m [39;49;00mflags[37m [39;49;00m=[37m [39;49;00m(opcode[37m [39;49;00m-[37m [39;49;00mCALL_FUNCTION)[37m [39;49;00m&[37m [39;49;00m[34m3[39;49;00m;[37m[39;49;00m$
[37m^I^I    [39;49;00m[36mint[39;49;00m[37m [39;49;00mn[37m [39;49;00m=[37m [39;49;00mna[37m [39;49;00m+[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m*[37m [39;49;00mnk;[37m[39;49;00m$
[37m^I^I    [39;49;00mPyObject[37m [39;49;00m**pfunc,[37m [39;49;00m*func,[37m [39;49;00m**sp;[37m[39;49;00m$
[37m^I^I    [39;49;00mPCALL(PCALL_ALL);[37m[39;49;00m$
[37m^I^I    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(flags[37m [39;49;00m&[37m [39;49;00mCALL_FLAG_VAR)[37m[39;49;00m$
[37m^I^I^I    [39;49;00mn++;[37m[39;49;00m$
[37m^I^I    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(flags[37m [39;49;00m&[37m [39;49;00mCALL_FLAG_KW)[37m[39;49;00m$
[37m^I^I^I    [39;49;00mn++;[37m[39;49;00m$
[37m^I^I    [39;49;00mpfunc[37m [39;49;00m=[37m [39;49;00mstack_pointer[37m [39;49;00m-[37m [39;49;00mn[37m [39;49;00m-[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
[37m^I^I    [39;49;00mfunc[37m [39;49;00m=[37m [39;49;00m*pfunc;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyMethod_Check(func)[37m[39;49;00m$
[37m^I^I^I[39;49;00m&&[37m [39;49;00mPyMethod_GET_SELF(func)[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I    [39;49;00mPyObject[37m [39;49;00m*self[37m [39;49;00m=[37m [39;49;00mPyMethod_GET_SELF(func);[37m[39;49;00m$
[37m^I^I^I    [39;49;00mPy_INCREF(self);[37m[39;49;00m$
[37m^I^I^I    [39;49;00mfunc[37m [39;49;00m=[37m [39;49;00mPyMethod_GET_FUNCTION(func);[37m[39;49;00m$
[37m^I^I^I    [39;49;00mPy_INCREF(func);[37m[39;49;00m$
[37m^I^I^I    [39;49;00mPy_DECREF(*pfunc);[37m[39;49;00m$
[37m^I^I^I    [39;49;00m*pfunc[37m [39;49;00m=[37m [39;49;00mself;[37m[39;49;00m$
[37m^I^I^I    [39;49;00mna++;[37m[39;49;00m$
[37m^I^I^I    [39;49;00mn++;[37m[39;49;00m$
[37m^I^I    [39;49;00m}[37m [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
[37m^I^I^I    [39;49;00mPy_INCREF(func);[37m[39;49;00m$
[37m^I^I    [39;49;00msp[37m [39;49;00m=[37m [39;49;00mstack_pointer;[37m[39;49;00m$
[37m^I^I    [39;49;00mREAD_TIMESTAMP(intr0);[37m[39;49;00m$
[37m^I^I    [39;49;00mx[37m [39;49;00m=[37m [39;49;00mext_do_call(func,[37m [39;49;00m&sp,[37m [39;49;00mflags,[37m [39;49;00mna,[37m [39;49;00mnk);[37m[39;49;00m$
[37m^I^I    [39;49;00mREAD_TIMESTAMP(intr1);[37m[39;49;00m$
[37m^I^I    [39;49;00mstack_pointer[37m [39;49;00m=[37m [39;49;00msp;[37m[39;49;00m$
[37m^I^I    [39;49;00mPy_DECREF(func);[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I    [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(stack_pointer[37m [39;49;00m>[37m [39;49;00mpfunc)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I    [39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I    [39;49;00mPy_DECREF(w);[37m[39;49;00m$
[37m^I^I    [39;49;00m}[37m[39;49;00m$
[37m^I^I    [39;49;00mPUSH(x);[37m[39;49;00m$
[37m^I^I    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
[37m^I^I^I    [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I    [39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m^I^I[39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mMAKE_FUNCTION[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m [39;49;00m[37m/* code object */[39;49;00m[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyFunction_New(v,[37m [39;49;00mf->f_globals);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[37m/* XXX Maybe this should be a separate opcode? */[39;49;00m[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m[37m [39;49;00m&&[37m [39;49;00moparg[37m [39;49;00m>[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPyTuple_New(oparg);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(v[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mPy_DECREF(x);[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(--oparg[37m [39;49;00m>=[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mPyTuple_SET_ITEM(v,[37m [39;49;00moparg,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyFunction_SetDefaults(x,[37m [39;49;00mv);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00mPUSH(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mMAKE_CLOSURE[39;49;00m:[37m[39;49;00m$
[37m^I^I[39;49;00m{[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m [39;49;00m[37m/* code object */[39;49;00m[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyFunction_New(v,[37m [39;49;00mf->f_globals);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyFunction_SetClosure(x,[37m [39;49;00mv);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m[37m [39;49;00m&&[37m [39;49;00moparg[37m [39;49;00m>[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPyTuple_New(oparg);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(v[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mPy_DECREF(x);[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(--oparg[37m [39;49;00m>=[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mPyTuple_SET_ITEM(v,[37m [39;49;00moparg,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyFunction_SetDefaults(x,[37m [39;49;00mv);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00mPUSH(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m^I^I[39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBUILD_SLICE[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(oparg[37m [39;49;00m==[37m [39;49;00m[34m3[39;49;00m)[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mu[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPySlice_New(u,[37m [39;49;00mv,[37m [39;49;00mw);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(u);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPy_XDECREF(w);[37m[39;49;00m$
[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mEXTENDED_ARG[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mopcode[37m [39;49;00m=[37m [39;49;00mNEXTOP();[37m[39;49;00m$
[37m^I^I^I[39;49;00moparg[37m [39;49;00m=[37m [39;49;00moparg<<[34m16[39;49;00m[37m [39;49;00m|[37m [39;49;00mNEXTARG();[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mdispatch_opcode;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mdefault[39;49;00m:[37m[39;49;00m$
[37m^I^I^I[39;49;00mfprintf(stderr,[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[33m"[39;49;00m[33mXXX lineno: %d, opcode: %d[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m,[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPyCode_Addr2Line(f->f_code,[37m [39;49;00mf->f_lasti),[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mopcode);[37m[39;49;00m$
[37m^I^I^I[39;49;00mPyErr_SetString(PyExc_SystemError,[37m [39;49;00m[33m"[39;49;00m[33munknown opcode[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
[37m^I^I^I[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_EXCEPTION;[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36mifdef CASE_TOO_BIG[39;49;00m[36m[39;49;00m$
[37m^I^I[39;49;00m}[37m[39;49;00m$
[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m}[37m [39;49;00m[37m/* switch */[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m^I    [39;49;00mon_error:[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00mREAD_TIMESTAMP(inst1);[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[37m/* Quickly continue if no error occurred */[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(why[37m [39;49;00m==[37m [39;49;00mWHY_NOT)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m&&[37m [39;49;00mx[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[36m#[39;49;00m[36mifdef CHECKEXC[39;49;00m[36m[39;49;00m$
[37m^I^I^I^I[39;49;00m[37m/* This check is expensive! */[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyErr_Occurred())[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mfprintf(stderr,[37m[39;49;00m$
[37m^I^I^I^I^I^I[39;49;00m[33m"[39;49;00m[33mXXX undetected error[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mREAD_TIMESTAMP(loop1);[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m [39;49;00m[37m/* Normal, fast path */[39;49;00m[37m[39;49;00m$
[36m#[39;49;00m[36mifdef CHECKEXC[39;49;00m[36m[39;49;00m$
[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_EXCEPTION;[37m[39;49;00m$
[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPy_None;[37m[39;49;00m$
[37m^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
[37m^I^I[39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[37m/* Double-check exception status */[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(why[37m [39;49;00m==[37m [39;49;00mWHY_EXCEPTION[37m [39;49;00m||[37m [39;49;00mwhy[37m [39;49;00m==[37m [39;49;00mWHY_RERAISE)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(!PyErr_Occurred())[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPyErr_SetString(PyExc_SystemError,[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m[33m"[39;49;00m[33merror return without exception set[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_EXCEPTION;[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I[39;49;00m}[37m[39;49;00m$
[36m#[39;49;00m[36mifdef CHECKEXC[39;49;00m[36m[39;49;00m$
[37m^I^I[39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I[39;49;00m[37m/* This check is expensive! */[39;49;00m[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyErr_Occurred())[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[36mchar[39;49;00m[37m [39;49;00mbuf[[34m1024[39;49;00m];[37m[39;49;00m$
[37m^I^I^I^I[39;49;00msprintf(buf,[37m [39;49;00m[33m"[39;49;00m[33mStack unwind with exception [39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m[33m"[39;49;00m[33mset and why=%d[39;49;00m[33m"[39;49;00m,[37m [39;49;00mwhy);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPy_FatalError(buf);[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I[39;49;00m}[37m[39;49;00m$
[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[37m/* Log traceback info if this is a real exception */[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(why[37m [39;49;00m==[37m [39;49;00mWHY_EXCEPTION)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I[39;49;00mPyTraceBack_Here(f);[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(tstate->c_tracefunc[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mcall_exc_trace(tstate->c_tracefunc,[37m[39;49;00m$
[37m^I^I^I^I^I       [39;49;00mtstate->c_traceobj,[37m [39;49;00mf);[37m[39;49;00m$
[37m^I^I[39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[37m/* For the rest, treat WHY_RERAISE as WHY_EXCEPTION */[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(why[37m [39;49;00m==[37m [39;49;00mWHY_RERAISE)[37m[39;49;00m$
[37m^I^I^I[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_EXCEPTION;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[37m/* Unwind stacks if a (pseudo) exception occurred */[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
fast_block_end:[37m[39;49;00m$
[37m^I^I[39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(why[37m [39;49;00m!=[37m [39;49;00mWHY_NOT[37m [39;49;00m&&[37m [39;49;00mf->f_iblock[37m [39;49;00m>[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I[39;49;00mPyTryBlock[37m [39;49;00m*b[37m [39;49;00m=[37m [39;49;00mPyFrame_BlockPop(f);[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I^I[39;49;00massert(why[37m [39;49;00m!=[37m [39;49;00mWHY_YIELD);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(b->b_type[37m [39;49;00m==[37m [39;49;00mSETUP_LOOP[37m [39;49;00m&&[37m [39;49;00mwhy[37m [39;49;00m==[37m [39;49;00mWHY_CONTINUE)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[37m/* For a continue inside a try block,[39;49;00m$
[37m^I^I^I^I   don't pop the block for the loop. */[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPyFrame_BlockSetup(f,[37m [39;49;00mb->b_type,[37m [39;49;00mb->b_handler,[37m[39;49;00m$
[37m^I^I^I^I^I^I   [39;49;00mb->b_level);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_NOT;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mJUMPTO(PyInt_AS_LONG(retval));[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPy_DECREF(retval);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(STACK_LEVEL()[37m [39;49;00m>[37m [39;49;00mb->b_level)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPy_XDECREF(v);[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(b->b_type[37m [39;49;00m==[37m [39;49;00mSETUP_LOOP[37m [39;49;00m&&[37m [39;49;00mwhy[37m [39;49;00m==[37m [39;49;00mWHY_BREAK)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_NOT;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mJUMPTO(b->b_handler);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(b->b_type[37m [39;49;00m==[37m [39;49;00mSETUP_FINALLY[37m [39;49;00m||[37m[39;49;00m$
[37m^I^I^I    [39;49;00m(b->b_type[37m [39;49;00m==[37m [39;49;00mSETUP_EXCEPT[37m [39;49;00m&&[37m[39;49;00m$
[37m^I^I^I     [39;49;00mwhy[37m [39;49;00m==[37m [39;49;00mWHY_EXCEPTION))[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(why[37m [39;49;00m==[37m [39;49;00mWHY_EXCEPTION)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mPyObject[37m [39;49;00m*exc,[37m [39;49;00m*val,[37m [39;49;00m*tb;[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mPyErr_Fetch(&exc,[37m [39;49;00m&val,[37m [39;49;00m&tb);[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(val[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I^I^I[39;49;00mval[37m [39;49;00m=[37m [39;49;00mPy_None;[37m[39;49;00m$
[37m^I^I^I^I^I^I[39;49;00mPy_INCREF(val);[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m[37m/* Make the raw exception data[39;49;00m$
[37m^I^I^I^I^I   available to the handler,[39;49;00m$
[37m^I^I^I^I^I   so a program can emulate the[39;49;00m$
[37m^I^I^I^I^I   Python main loop.  Don't do[39;49;00m$
[37m^I^I^I^I^I   this for 'finally'. */[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(b->b_type[37m [39;49;00m==[37m [39;49;00mSETUP_EXCEPT)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I^I^I[39;49;00mPyErr_NormalizeException([37m[39;49;00m$
[37m^I^I^I^I^I^I^I[39;49;00m&exc,[37m [39;49;00m&val,[37m [39;49;00m&tb);[37m[39;49;00m$
[37m^I^I^I^I^I^I[39;49;00mset_exc_info(tstate,[37m[39;49;00m$
[37m^I^I^I^I^I^I^I     [39;49;00mexc,[37m [39;49;00mval,[37m [39;49;00mtb);[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(tb[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I^I^I[39;49;00mPy_INCREF(Py_None);[37m[39;49;00m$
[37m^I^I^I^I^I^I[39;49;00mPUSH(Py_None);[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m}[37m [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I^I^I[39;49;00mPUSH(tb);[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mPUSH(val);[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mPUSH(exc);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(why[37m [39;49;00m&[37m [39;49;00m(WHY_RETURN[37m [39;49;00m|[37m [39;49;00mWHY_CONTINUE))[37m[39;49;00m$
[37m^I^I^I^I^I^I[39;49;00mPUSH(retval);[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPyInt_FromLong(([36mlong[39;49;00m)why);[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mPUSH(v);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_NOT;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mJUMPTO(b->b_handler);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I[39;49;00m}[37m [39;49;00m[37m/* unwind stack */[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[37m/* End the loop if we still have an error (or return) */[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(why[37m [39;49;00m!=[37m [39;49;00mWHY_NOT)[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m^I^I[39;49;00mREAD_TIMESTAMP(loop1);[37m[39;49;00m$
[37m[39;49;00m$
[37m^I[39;49;00m}[37m [39;49;00m[37m/* main loop */[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m^I[39;49;00massert(why[37m [39;49;00m!=[37m [39;49;00mWHY_YIELD);[37m[39;49;00m$
[37m^I[39;49;00m[37m/* Pop remaining stack entries. */[39;49;00m[37m[39;49;00m$
[37m^I[39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(!EMPTY())[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
[37m^I^I[39;49;00mPy_XDECREF(v);[37m[39;49;00m$
[37m^I[39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(why[37m [39;49;00m!=[37m [39;49;00mWHY_RETURN)[37m[39;49;00m$
[37m^I^I[39;49;00mretval[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
fast_yield:[37m[39;49;00m$
[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(tstate->use_tracing)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(tstate->c_tracefunc)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(why[37m [39;49;00m==[37m [39;49;00mWHY_RETURN[37m [39;49;00m||[37m [39;49;00mwhy[37m [39;49;00m==[37m [39;49;00mWHY_YIELD)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(call_trace(tstate->c_tracefunc,[37m[39;49;00m$
[37m^I^I^I^I^I       [39;49;00mtstate->c_traceobj,[37m [39;49;00mf,[37m[39;49;00m$
[37m^I^I^I^I^I       [39;49;00mPyTrace_RETURN,[37m [39;49;00mretval))[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mPy_XDECREF(retval);[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mretval[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_EXCEPTION;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(why[37m [39;49;00m==[37m [39;49;00mWHY_EXCEPTION)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mcall_trace_protected(tstate->c_tracefunc,[37m[39;49;00m$
[37m^I^I^I^I^I^I     [39;49;00mtstate->c_traceobj,[37m [39;49;00mf,[37m[39;49;00m$
[37m^I^I^I^I^I^I     [39;49;00mPyTrace_RETURN,[37m [39;49;00m[36mNULL[39;49;00m);[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(tstate->c_profilefunc)[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(why[37m [39;49;00m==[37m [39;49;00mWHY_EXCEPTION)[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mcall_trace_protected(tstate->c_profilefunc,[37m[39;49;00m$
[37m^I^I^I^I^I^I     [39;49;00mtstate->c_profileobj,[37m [39;49;00mf,[37m[39;49;00m$
[37m^I^I^I^I^I^I     [39;49;00mPyTrace_RETURN,[37m [39;49;00m[36mNULL[39;49;00m);[37m[39;49;00m$
[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(call_trace(tstate->c_profilefunc,[37m[39;49;00m$
[37m^I^I^I^I^I    [39;49;00mtstate->c_profileobj,[37m [39;49;00mf,[37m[39;49;00m$
[37m^I^I^I^I^I    [39;49;00mPyTrace_RETURN,[37m [39;49;00mretval))[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mPy_XDECREF(retval);[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mretval[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_EXCEPTION;[37m[39;49;00m$
[37m^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I[39;49;00m}[37m[39;49;00m$
[37m^I[39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(tstate->frame->f_exc_type[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
[37m^I^I[39;49;00mreset_exc_info(tstate);[37m[39;49;00m$
[37m^I[39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
[37m^I^I[39;49;00massert(tstate->frame->f_exc_value[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m);[37m[39;49;00m$
[37m^I^I[39;49;00massert(tstate->frame->f_exc_traceback[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m);[37m[39;49;00m$
[37m^I[39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m^I[39;49;00m[37m/* pop frame */[39;49;00m[37m[39;49;00m$
[37m    [39;49;00mexit_eval_frame:[37m[39;49;00m$
[37m^I[39;49;00mPy_LeaveRecursiveCall();[37m[39;49;00m$
[37m^I[39;49;00mtstate->frame[37m [39;49;00m=[37m [39;49;00mf->f_back;[37m[39;49;00m$
[37m[39;49;00m$
[37m^I[39;49;00m[34mreturn[39;49;00m[37m [39;49;00mretval;[37m[39;49;00m$
}$

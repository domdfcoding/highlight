     1^I[37m/* Execute compiled code */[39;49;00m[37m[39;49;00m$
     2^I[37m[39;49;00m$
     3^I[37m/* XXX TO DO:[39;49;00m$
     4^I[37m   XXX speed up searching for keywords by using a dictionary[39;49;00m$
     5^I[37m   XXX document it![39;49;00m$
     6^I[37m   */[39;49;00m[37m[39;49;00m$
     7^I[37m[39;49;00m$
     8^I[37m/* enable more aggressive intra-module optimizations, where available */[39;49;00m[37m[39;49;00m$
     9^I[36m#[39;49;00m[36mdefine PY_LOCAL_AGGRESSIVE[39;49;00m[36m[39;49;00m$
    10^I[37m[39;49;00m$
    11^I[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"Python.h"[39;49;00m[36m[39;49;00m$
    12^I[37m[39;49;00m$
    13^I[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"code.h"[39;49;00m[36m[39;49;00m$
    14^I[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"frameobject.h"[39;49;00m[36m[39;49;00m$
    15^I[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"eval.h"[39;49;00m[36m[39;49;00m$
    16^I[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"opcode.h"[39;49;00m[36m[39;49;00m$
    17^I[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"structmember.h"[39;49;00m[36m[39;49;00m$
    18^I[37m[39;49;00m$
    19^I[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<ctype.h>[39;49;00m[36m[39;49;00m$
    20^I[37m[39;49;00m$
    21^I[36m#[39;49;00m[36mifndef WITH_TSC[39;49;00m[36m[39;49;00m$
    22^I[37m[39;49;00m$
    23^I[36m#[39;49;00m[36mdefine READ_TIMESTAMP(var)[39;49;00m[36m[39;49;00m$
    24^I[37m[39;49;00m$
    25^I[36m#[39;49;00m[36melse[39;49;00m[36m[39;49;00m$
    26^I[37m[39;49;00m$
    27^I[34mtypedef[39;49;00m[37m [39;49;00m[36munsigned[39;49;00m[37m [39;49;00m[36mlong[39;49;00m[37m [39;49;00m[36mlong[39;49;00m[37m [39;49;00muint64;[37m[39;49;00m$
    28^I[37m[39;49;00m$
    29^I[36m#[39;49;00m[36mif defined(__ppc__) [39;49;00m[37m/* <- Don't know if this is the correct symbol; this[39;49;00m$
    30^I[37m^I^I^I   section should work for GCC on any PowerPC platform,[39;49;00m$
    31^I[37m^I^I^I   irrespective of OS.  POWER?  Who knows :-) */[39;49;00m[36m[39;49;00m$
    32^I[37m[39;49;00m$
    33^I[36m#[39;49;00m[36mdefine READ_TIMESTAMP(var) ppc_getcounter(&var)[39;49;00m[36m[39;49;00m$
    34^I[37m[39;49;00m$
    35^I[34mstatic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m[39;49;00m$
    36^I[32mppc_getcounter[39;49;00m(uint64[37m [39;49;00m*v)[37m[39;49;00m$
    37^I{[37m[39;49;00m$
    38^I[37m^I[39;49;00m[34mregister[39;49;00m[37m [39;49;00m[36munsigned[39;49;00m[37m [39;49;00m[36mlong[39;49;00m[37m [39;49;00mtbu,[37m [39;49;00mtb,[37m [39;49;00mtbu2;[37m[39;49;00m$
    39^I[37m[39;49;00m$
    40^I[37m  [39;49;00mloop:[37m[39;49;00m$
    41^I[37m^I[39;49;00m[34masm[39;49;00m[37m [39;49;00m[34mvolatile[39;49;00m[37m [39;49;00m([33m"[39;49;00m[33mmftbu %0[39;49;00m[33m"[39;49;00m[37m [39;49;00m:[37m [39;49;00m[33m"[39;49;00m[33m=r[39;49;00m[33m"[39;49;00m[37m [39;49;00m(tbu)[37m [39;49;00m);[37m[39;49;00m$
    42^I[37m^I[39;49;00m[34masm[39;49;00m[37m [39;49;00m[34mvolatile[39;49;00m[37m [39;49;00m([33m"[39;49;00m[33mmftb  %0[39;49;00m[33m"[39;49;00m[37m [39;49;00m:[37m [39;49;00m[33m"[39;49;00m[33m=r[39;49;00m[33m"[39;49;00m[37m [39;49;00m(tb)[37m  [39;49;00m);[37m[39;49;00m$
    43^I[37m^I[39;49;00m[34masm[39;49;00m[37m [39;49;00m[34mvolatile[39;49;00m[37m [39;49;00m([33m"[39;49;00m[33mmftbu %0[39;49;00m[33m"[39;49;00m[37m [39;49;00m:[37m [39;49;00m[33m"[39;49;00m[33m=r[39;49;00m[33m"[39;49;00m[37m [39;49;00m(tbu2));[37m[39;49;00m$
    44^I[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(__builtin_expect(tbu[37m [39;49;00m!=[37m [39;49;00mtbu2,[37m [39;49;00m[34m0[39;49;00m))[37m [39;49;00m[34mgoto[39;49;00m[37m [39;49;00mloop;[37m[39;49;00m$
    45^I[37m[39;49;00m$
    46^I[37m^I[39;49;00m[37m/* The slightly peculiar way of writing the next lines is[39;49;00m$
    47^I[37m^I   compiled better by GCC than any other way I tried. */[39;49;00m[37m[39;49;00m$
    48^I[37m^I[39;49;00m(([36mlong[39;49;00m*)(v))[[34m0[39;49;00m][37m [39;49;00m=[37m [39;49;00mtbu;[37m[39;49;00m$
    49^I[37m^I[39;49;00m(([36mlong[39;49;00m*)(v))[[34m1[39;49;00m][37m [39;49;00m=[37m [39;49;00mtb;[37m[39;49;00m$
    50^I}[37m[39;49;00m$
    51^I[37m[39;49;00m$
    52^I[36m#[39;49;00m[36melse [39;49;00m[37m/* this is for linux/x86 (and probably any other GCC/x86 combo) */[39;49;00m[36m[39;49;00m$
    53^I[37m[39;49;00m$
    54^I[36m#[39;49;00m[36mdefine READ_TIMESTAMP(val) \[39;49;00m[36m[39;49;00m$
    55^I[36m     __asm__ __volatile__("rdtsc" : "=A" (val))[39;49;00m[36m[39;49;00m$
    56^I[37m[39;49;00m$
    57^I[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
    58^I[37m[39;49;00m$
    59^I[36mvoid[39;49;00m[37m [39;49;00m[32mdump_tsc[39;49;00m([36mint[39;49;00m[37m [39;49;00mopcode,[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mticked,[37m [39;49;00muint64[37m [39;49;00minst0,[37m [39;49;00muint64[37m [39;49;00minst1,[37m[39;49;00m$
    60^I[37m^I      [39;49;00muint64[37m [39;49;00mloop0,[37m [39;49;00muint64[37m [39;49;00mloop1,[37m [39;49;00muint64[37m [39;49;00mintr0,[37m [39;49;00muint64[37m [39;49;00mintr1)[37m[39;49;00m$
    61^I{[37m[39;49;00m$
    62^I[37m^I[39;49;00muint64[37m [39;49;00mintr,[37m [39;49;00minst,[37m [39;49;00mloop;[37m[39;49;00m$
    63^I[37m^I[39;49;00mPyThreadState[37m [39;49;00m*tstate[37m [39;49;00m=[37m [39;49;00mPyThreadState_Get();[37m[39;49;00m$
    64^I[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(!tstate->interp->tscdump)[37m[39;49;00m$
    65^I[37m^I^I[39;49;00m[34mreturn[39;49;00m;[37m[39;49;00m$
    66^I[37m^I[39;49;00mintr[37m [39;49;00m=[37m [39;49;00mintr1[37m [39;49;00m-[37m [39;49;00mintr0;[37m[39;49;00m$
    67^I[37m^I[39;49;00minst[37m [39;49;00m=[37m [39;49;00minst1[37m [39;49;00m-[37m [39;49;00minst0[37m [39;49;00m-[37m [39;49;00mintr;[37m[39;49;00m$
    68^I[37m^I[39;49;00mloop[37m [39;49;00m=[37m [39;49;00mloop1[37m [39;49;00m-[37m [39;49;00mloop0[37m [39;49;00m-[37m [39;49;00mintr;[37m[39;49;00m$
    69^I[37m^I[39;49;00mfprintf(stderr,[37m [39;49;00m[33m"[39;49;00m[33mopcode=%03d t=%d inst=%06lld loop=%06lld[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m,[37m[39;49;00m$
    70^I[37m^I^I[39;49;00mopcode,[37m [39;49;00mticked,[37m [39;49;00minst,[37m [39;49;00mloop);[37m[39;49;00m$
    71^I}[37m[39;49;00m$
    72^I[37m[39;49;00m$
    73^I[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
    74^I[37m[39;49;00m$
    75^I[37m/* Turn this on if your compiler chokes on the big switch: */[39;49;00m[37m[39;49;00m$
    76^I[37m/* #define CASE_TOO_BIG 1 */[39;49;00m[37m[39;49;00m$
    77^I[37m[39;49;00m$
    78^I[36m#[39;49;00m[36mifdef Py_DEBUG[39;49;00m[36m[39;49;00m$
    79^I[37m/* For debugging the interpreter: */[39;49;00m[37m[39;49;00m$
    80^I[36m#[39;49;00m[36mdefine LLTRACE  1^I[39;49;00m[37m/* Low-level trace feature */[39;49;00m[36m[39;49;00m$
    81^I[36m#[39;49;00m[36mdefine CHECKEXC 1^I[39;49;00m[37m/* Double-check exception checking */[39;49;00m[36m[39;49;00m$
    82^I[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
    83^I[37m[39;49;00m$
    84^I[34mtypedef[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*(*callproc)(PyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*);[37m[39;49;00m$
    85^I[37m[39;49;00m$
    86^I[37m/* Forward declarations */[39;49;00m[37m[39;49;00m$
    87^I[36m#[39;49;00m[36mifdef WITH_TSC[39;49;00m[36m[39;49;00m$
    88^I[34mstatic[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*[37m [39;49;00m[32mcall_function[39;49;00m(PyObject[37m [39;49;00m***,[37m [39;49;00m[36mint[39;49;00m,[37m [39;49;00muint64*,[37m [39;49;00muint64*);[37m[39;49;00m$
    89^I[36m#[39;49;00m[36melse[39;49;00m[36m[39;49;00m$
    90^I[34mstatic[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*[37m [39;49;00m[32mcall_function[39;49;00m(PyObject[37m [39;49;00m***,[37m [39;49;00m[36mint[39;49;00m);[37m[39;49;00m$
    91^I[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
    92^I[34mstatic[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*[37m [39;49;00m[32mfast_function[39;49;00m(PyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m***,[37m [39;49;00m[36mint[39;49;00m,[37m [39;49;00m[36mint[39;49;00m,[37m [39;49;00m[36mint[39;49;00m);[37m[39;49;00m$
    93^I[34mstatic[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*[37m [39;49;00m[32mdo_call[39;49;00m(PyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m***,[37m [39;49;00m[36mint[39;49;00m,[37m [39;49;00m[36mint[39;49;00m);[37m[39;49;00m$
    94^I[34mstatic[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*[37m [39;49;00m[32mext_do_call[39;49;00m(PyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m***,[37m [39;49;00m[36mint[39;49;00m,[37m [39;49;00m[36mint[39;49;00m,[37m [39;49;00m[36mint[39;49;00m);[37m[39;49;00m$
    95^I[34mstatic[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*[37m [39;49;00m[32mupdate_keyword_args[39;49;00m(PyObject[37m [39;49;00m*,[37m [39;49;00m[36mint[39;49;00m,[37m [39;49;00mPyObject[37m [39;49;00m***,PyObject[37m [39;49;00m*);[37m[39;49;00m$
    96^I[34mstatic[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*[37m [39;49;00m[32mupdate_star_args[39;49;00m([36mint[39;49;00m,[37m [39;49;00m[36mint[39;49;00m,[37m [39;49;00mPyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m***);[37m[39;49;00m$
    97^I[34mstatic[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*[37m [39;49;00m[32mload_args[39;49;00m(PyObject[37m [39;49;00m***,[37m [39;49;00m[36mint[39;49;00m);[37m[39;49;00m$
    98^I[36m#[39;49;00m[36mdefine CALL_FLAG_VAR 1[39;49;00m[36m[39;49;00m$
    99^I[36m#[39;49;00m[36mdefine CALL_FLAG_KW 2[39;49;00m[36m[39;49;00m$
   100^I[37m[39;49;00m$
   101^I[36m#[39;49;00m[36mifdef LLTRACE[39;49;00m[36m[39;49;00m$
   102^I[34mstatic[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mlltrace;[37m[39;49;00m$
   103^I[34mstatic[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00m[32mprtrace[39;49;00m(PyObject[37m [39;49;00m*,[37m [39;49;00m[36mchar[39;49;00m[37m [39;49;00m*);[37m[39;49;00m$
   104^I[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   105^I[34mstatic[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00m[32mcall_trace[39;49;00m(Py_tracefunc,[37m [39;49;00mPyObject[37m [39;49;00m*,[37m [39;49;00mPyFrameObject[37m [39;49;00m*,[37m[39;49;00m$
   106^I[37m^I^I      [39;49;00m[36mint[39;49;00m,[37m [39;49;00mPyObject[37m [39;49;00m*);[37m[39;49;00m$
   107^I[34mstatic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mcall_trace_protected[39;49;00m(Py_tracefunc,[37m [39;49;00mPyObject[37m [39;49;00m*,[37m[39;49;00m$
   108^I[37m^I^I^I^I [39;49;00mPyFrameObject[37m [39;49;00m*,[37m [39;49;00m[36mint[39;49;00m,[37m [39;49;00mPyObject[37m [39;49;00m*);[37m[39;49;00m$
   109^I[34mstatic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mcall_exc_trace[39;49;00m(Py_tracefunc,[37m [39;49;00mPyObject[37m [39;49;00m*,[37m [39;49;00mPyFrameObject[37m [39;49;00m*);[37m[39;49;00m$
   110^I[34mstatic[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00m[32mmaybe_call_line_trace[39;49;00m(Py_tracefunc,[37m [39;49;00mPyObject[37m [39;49;00m*,[37m[39;49;00m$
   111^I[37m^I^I^I^I  [39;49;00mPyFrameObject[37m [39;49;00m*,[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00m*,[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00m*,[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00m*);[37m[39;49;00m$
   112^I[37m[39;49;00m$
   113^I[34mstatic[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*[37m [39;49;00m[32mapply_slice[39;49;00m(PyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*);[37m[39;49;00m$
   114^I[34mstatic[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00m[32massign_slice[39;49;00m(PyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*,[37m[39;49;00m$
   115^I[37m^I^I^I[39;49;00mPyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*);[37m[39;49;00m$
   116^I[34mstatic[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*[37m [39;49;00m[32mcmp_outcome[39;49;00m([36mint[39;49;00m,[37m [39;49;00mPyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*);[37m[39;49;00m$
   117^I[34mstatic[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*[37m [39;49;00m[32mimport_from[39;49;00m(PyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*);[37m[39;49;00m$
   118^I[34mstatic[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00m[32mimport_all_from[39;49;00m(PyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*);[37m[39;49;00m$
   119^I[34mstatic[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*[37m [39;49;00m[32mbuild_class[39;49;00m(PyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*);[37m[39;49;00m$
   120^I[34mstatic[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00m[32mexec_statement[39;49;00m(PyFrameObject[37m [39;49;00m*,[37m[39;49;00m$
   121^I[37m^I^I^I  [39;49;00mPyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*);[37m[39;49;00m$
   122^I[34mstatic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mset_exc_info[39;49;00m(PyThreadState[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*);[37m[39;49;00m$
   123^I[34mstatic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mreset_exc_info[39;49;00m(PyThreadState[37m [39;49;00m*);[37m[39;49;00m$
   124^I[34mstatic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mformat_exc_check_arg[39;49;00m(PyObject[37m [39;49;00m*,[37m [39;49;00m[36mchar[39;49;00m[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*);[37m[39;49;00m$
   125^I[34mstatic[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*[37m [39;49;00m[32mstring_concatenate[39;49;00m(PyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*,[37m[39;49;00m$
   126^I[37m^I^I^I^I    [39;49;00mPyFrameObject[37m [39;49;00m*,[37m [39;49;00m[36munsigned[39;49;00m[37m [39;49;00m[36mchar[39;49;00m[37m [39;49;00m*);[37m[39;49;00m$
   127^I[37m[39;49;00m$
   128^I[36m#[39;49;00m[36mdefine NAME_ERROR_MSG \[39;49;00m[36m[39;49;00m$
   129^I[36m^I"name '%.200s' is not defined"[39;49;00m[36m[39;49;00m$
   130^I[36m#[39;49;00m[36mdefine GLOBAL_NAME_ERROR_MSG \[39;49;00m[36m[39;49;00m$
   131^I[36m^I"global name '%.200s' is not defined"[39;49;00m[36m[39;49;00m$
   132^I[36m#[39;49;00m[36mdefine UNBOUNDLOCAL_ERROR_MSG \[39;49;00m[36m[39;49;00m$
   133^I[36m^I"local variable '%.200s' referenced before assignment"[39;49;00m[36m[39;49;00m$
   134^I[36m#[39;49;00m[36mdefine UNBOUNDFREE_ERROR_MSG \[39;49;00m[36m[39;49;00m$
   135^I[36m^I"free variable '%.200s' referenced before assignment" \[39;49;00m[36m[39;49;00m$
   136^I[36m        " in enclosing scope"[39;49;00m[36m[39;49;00m$
   137^I[37m[39;49;00m$
   138^I[37m/* Dynamic execution profile */[39;49;00m[37m[39;49;00m$
   139^I[36m#[39;49;00m[36mifdef DYNAMIC_EXECUTION_PROFILE[39;49;00m[36m[39;49;00m$
   140^I[36m#[39;49;00m[36mifdef DXPAIRS[39;49;00m[36m[39;49;00m$
   141^I[34mstatic[39;49;00m[37m [39;49;00m[36mlong[39;49;00m[37m [39;49;00mdxpairs[[34m257[39;49;00m][[34m256[39;49;00m];[37m[39;49;00m$
   142^I[36m#[39;49;00m[36mdefine dxp dxpairs[256][39;49;00m[36m[39;49;00m$
   143^I[36m#[39;49;00m[36melse[39;49;00m[36m[39;49;00m$
   144^I[34mstatic[39;49;00m[37m [39;49;00m[36mlong[39;49;00m[37m [39;49;00mdxp[[34m256[39;49;00m];[37m[39;49;00m$
   145^I[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   146^I[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   147^I[37m[39;49;00m$
   148^I[37m/* Function call profile */[39;49;00m[37m[39;49;00m$
   149^I[36m#[39;49;00m[36mifdef CALL_PROFILE[39;49;00m[36m[39;49;00m$
   150^I[36m#[39;49;00m[36mdefine PCALL_NUM 11[39;49;00m[36m[39;49;00m$
   151^I[34mstatic[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mpcall[PCALL_NUM];[37m[39;49;00m$
   152^I[37m[39;49;00m$
   153^I[36m#[39;49;00m[36mdefine PCALL_ALL 0[39;49;00m[36m[39;49;00m$
   154^I[36m#[39;49;00m[36mdefine PCALL_FUNCTION 1[39;49;00m[36m[39;49;00m$
   155^I[36m#[39;49;00m[36mdefine PCALL_FAST_FUNCTION 2[39;49;00m[36m[39;49;00m$
   156^I[36m#[39;49;00m[36mdefine PCALL_FASTER_FUNCTION 3[39;49;00m[36m[39;49;00m$
   157^I[36m#[39;49;00m[36mdefine PCALL_METHOD 4[39;49;00m[36m[39;49;00m$
   158^I[36m#[39;49;00m[36mdefine PCALL_BOUND_METHOD 5[39;49;00m[36m[39;49;00m$
   159^I[36m#[39;49;00m[36mdefine PCALL_CFUNCTION 6[39;49;00m[36m[39;49;00m$
   160^I[36m#[39;49;00m[36mdefine PCALL_TYPE 7[39;49;00m[36m[39;49;00m$
   161^I[36m#[39;49;00m[36mdefine PCALL_GENERATOR 8[39;49;00m[36m[39;49;00m$
   162^I[36m#[39;49;00m[36mdefine PCALL_OTHER 9[39;49;00m[36m[39;49;00m$
   163^I[36m#[39;49;00m[36mdefine PCALL_POP 10[39;49;00m[36m[39;49;00m$
   164^I[37m[39;49;00m$
   165^I[37m/* Notes about the statistics[39;49;00m$
   166^I[37m[39;49;00m$
   167^I[37m   PCALL_FAST stats[39;49;00m$
   168^I[37m[39;49;00m$
   169^I[37m   FAST_FUNCTION means no argument tuple needs to be created.[39;49;00m$
   170^I[37m   FASTER_FUNCTION means that the fast-path frame setup code is used.[39;49;00m$
   171^I[37m[39;49;00m$
   172^I[37m   If there is a method call where the call can be optimized by changing[39;49;00m$
   173^I[37m   the argument tuple and calling the function directly, it gets recorded[39;49;00m$
   174^I[37m   twice.[39;49;00m$
   175^I[37m[39;49;00m$
   176^I[37m   As a result, the relationship among the statistics appears to be[39;49;00m$
   177^I[37m   PCALL_ALL == PCALL_FUNCTION + PCALL_METHOD - PCALL_BOUND_METHOD +[39;49;00m$
   178^I[37m                PCALL_CFUNCTION + PCALL_TYPE + PCALL_GENERATOR + PCALL_OTHER[39;49;00m$
   179^I[37m   PCALL_FUNCTION > PCALL_FAST_FUNCTION > PCALL_FASTER_FUNCTION[39;49;00m$
   180^I[37m   PCALL_METHOD > PCALL_BOUND_METHOD[39;49;00m$
   181^I[37m*/[39;49;00m[37m[39;49;00m$
   182^I[37m[39;49;00m$
   183^I[36m#[39;49;00m[36mdefine PCALL(POS) pcall[POS]++[39;49;00m[36m[39;49;00m$
   184^I[37m[39;49;00m$
   185^IPyObject[37m [39;49;00m*[37m[39;49;00m$
   186^I[32mPyEval_GetCallStats[39;49;00m(PyObject[37m [39;49;00m*self)[37m[39;49;00m$
   187^I{[37m[39;49;00m$
   188^I[37m^I[39;49;00m[34mreturn[39;49;00m[37m [39;49;00mPy_BuildValue([33m"[39;49;00m[33miiiiiiiiii[39;49;00m[33m"[39;49;00m,[37m[39;49;00m$
   189^I[37m^I^I^I     [39;49;00mpcall[[34m0[39;49;00m],[37m [39;49;00mpcall[[34m1[39;49;00m],[37m [39;49;00mpcall[[34m2[39;49;00m],[37m [39;49;00mpcall[[34m3[39;49;00m],[37m[39;49;00m$
   190^I[37m^I^I^I     [39;49;00mpcall[[34m4[39;49;00m],[37m [39;49;00mpcall[[34m5[39;49;00m],[37m [39;49;00mpcall[[34m6[39;49;00m],[37m [39;49;00mpcall[[34m7[39;49;00m],[37m[39;49;00m$
   191^I[37m^I^I^I     [39;49;00mpcall[[34m8[39;49;00m],[37m [39;49;00mpcall[[34m9[39;49;00m]);[37m[39;49;00m$
   192^I}[37m[39;49;00m$
   193^I[36m#[39;49;00m[36melse[39;49;00m[36m[39;49;00m$
   194^I[36m#[39;49;00m[36mdefine PCALL(O)[39;49;00m[36m[39;49;00m$
   195^I[37m[39;49;00m$
   196^IPyObject[37m [39;49;00m*[37m[39;49;00m$
   197^I[32mPyEval_GetCallStats[39;49;00m(PyObject[37m [39;49;00m*self)[37m[39;49;00m$
   198^I{[37m[39;49;00m$
   199^I[37m^I[39;49;00mPy_INCREF(Py_None);[37m[39;49;00m$
   200^I[37m^I[39;49;00m[34mreturn[39;49;00m[37m [39;49;00mPy_None;[37m[39;49;00m$
   201^I}[37m[39;49;00m$
   202^I[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   203^I[37m[39;49;00m$
   204^I[37m[39;49;00m$
   205^I[36m#[39;49;00m[36mifdef WITH_THREAD[39;49;00m[36m[39;49;00m$
   206^I[37m[39;49;00m$
   207^I[36m#[39;49;00m[36mifdef HAVE_ERRNO_H[39;49;00m[36m[39;49;00m$
   208^I[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<errno.h>[39;49;00m[36m[39;49;00m$
   209^I[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   210^I[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"pythread.h"[39;49;00m[36m[39;49;00m$
   211^I[37m[39;49;00m$
   212^I[34mstatic[39;49;00m[37m [39;49;00mPyThread_type_lock[37m [39;49;00minterpreter_lock[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m [39;49;00m[37m/* This is the GIL */[39;49;00m[37m[39;49;00m$
   213^I[34mstatic[39;49;00m[37m [39;49;00m[36mlong[39;49;00m[37m [39;49;00mmain_thread[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   214^I[37m[39;49;00m$
   215^I[36mint[39;49;00m[37m[39;49;00m$
   216^I[32mPyEval_ThreadsInitialized[39;49;00m([36mvoid[39;49;00m)[37m[39;49;00m$
   217^I{[37m[39;49;00m$
   218^I[37m^I[39;49;00m[34mreturn[39;49;00m[37m [39;49;00minterpreter_lock[37m [39;49;00m!=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   219^I}[37m[39;49;00m$
   220^I[37m[39;49;00m$
   221^I[36mvoid[39;49;00m[37m[39;49;00m$
   222^I[32mPyEval_InitThreads[39;49;00m([36mvoid[39;49;00m)[37m[39;49;00m$
   223^I{[37m[39;49;00m$
   224^I[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(interpreter_lock)[37m[39;49;00m$
   225^I[37m^I^I[39;49;00m[34mreturn[39;49;00m;[37m[39;49;00m$
   226^I[37m^I[39;49;00minterpreter_lock[37m [39;49;00m=[37m [39;49;00mPyThread_allocate_lock();[37m[39;49;00m$
   227^I[37m^I[39;49;00mPyThread_acquire_lock(interpreter_lock,[37m [39;49;00m[34m1[39;49;00m);[37m[39;49;00m$
   228^I[37m^I[39;49;00mmain_thread[37m [39;49;00m=[37m [39;49;00mPyThread_get_thread_ident();[37m[39;49;00m$
   229^I}[37m[39;49;00m$
   230^I[37m[39;49;00m$
   231^I[36mvoid[39;49;00m[37m[39;49;00m$
   232^I[32mPyEval_AcquireLock[39;49;00m([36mvoid[39;49;00m)[37m[39;49;00m$
   233^I{[37m[39;49;00m$
   234^I[37m^I[39;49;00mPyThread_acquire_lock(interpreter_lock,[37m [39;49;00m[34m1[39;49;00m);[37m[39;49;00m$
   235^I}[37m[39;49;00m$
   236^I[37m[39;49;00m$
   237^I[36mvoid[39;49;00m[37m[39;49;00m$
   238^I[32mPyEval_ReleaseLock[39;49;00m([36mvoid[39;49;00m)[37m[39;49;00m$
   239^I{[37m[39;49;00m$
   240^I[37m^I[39;49;00mPyThread_release_lock(interpreter_lock);[37m[39;49;00m$
   241^I}[37m[39;49;00m$
   242^I[37m[39;49;00m$
   243^I[36mvoid[39;49;00m[37m[39;49;00m$
   244^I[32mPyEval_AcquireThread[39;49;00m(PyThreadState[37m [39;49;00m*tstate)[37m[39;49;00m$
   245^I{[37m[39;49;00m$
   246^I[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(tstate[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
   247^I[37m^I^I[39;49;00mPy_FatalError([33m"[39;49;00m[33mPyEval_AcquireThread: NULL new thread state[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
   248^I[37m^I[39;49;00m[37m/* Check someone has called PyEval_InitThreads() to create the lock */[39;49;00m[37m[39;49;00m$
   249^I[37m^I[39;49;00massert(interpreter_lock);[37m[39;49;00m$
   250^I[37m^I[39;49;00mPyThread_acquire_lock(interpreter_lock,[37m [39;49;00m[34m1[39;49;00m);[37m[39;49;00m$
   251^I[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyThreadState_Swap(tstate)[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
   252^I[37m^I^I[39;49;00mPy_FatalError([37m[39;49;00m$
   253^I[37m^I^I^I[39;49;00m[33m"[39;49;00m[33mPyEval_AcquireThread: non-NULL old thread state[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
   254^I}[37m[39;49;00m$
   255^I[37m[39;49;00m$
   256^I[36mvoid[39;49;00m[37m[39;49;00m$
   257^I[32mPyEval_ReleaseThread[39;49;00m(PyThreadState[37m [39;49;00m*tstate)[37m[39;49;00m$
   258^I{[37m[39;49;00m$
   259^I[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(tstate[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
   260^I[37m^I^I[39;49;00mPy_FatalError([33m"[39;49;00m[33mPyEval_ReleaseThread: NULL thread state[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
   261^I[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyThreadState_Swap([36mNULL[39;49;00m)[37m [39;49;00m!=[37m [39;49;00mtstate)[37m[39;49;00m$
   262^I[37m^I^I[39;49;00mPy_FatalError([33m"[39;49;00m[33mPyEval_ReleaseThread: wrong thread state[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
   263^I[37m^I[39;49;00mPyThread_release_lock(interpreter_lock);[37m[39;49;00m$
   264^I}[37m[39;49;00m$
   265^I[37m[39;49;00m$
   266^I[37m/* This function is called from PyOS_AfterFork to ensure that newly[39;49;00m$
   267^I[37m   created child processes don't hold locks referring to threads which[39;49;00m$
   268^I[37m   are not running in the child process.  (This could also be done using[39;49;00m$
   269^I[37m   pthread_atfork mechanism, at least for the pthreads implementation.) */[39;49;00m[37m[39;49;00m$
   270^I[37m[39;49;00m$
   271^I[36mvoid[39;49;00m[37m[39;49;00m$
   272^I[32mPyEval_ReInitThreads[39;49;00m([36mvoid[39;49;00m)[37m[39;49;00m$
   273^I{[37m[39;49;00m$
   274^I[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(!interpreter_lock)[37m[39;49;00m$
   275^I[37m^I^I[39;49;00m[34mreturn[39;49;00m;[37m[39;49;00m$
   276^I[37m^I[39;49;00m[37m/*XXX Can't use PyThread_free_lock here because it does too[39;49;00m$
   277^I[37m^I  much error-checking.  Doing this cleanly would require[39;49;00m$
   278^I[37m^I  adding a new function to each thread_*.h.  Instead, just[39;49;00m$
   279^I[37m^I  create a new lock and waste a little bit of memory */[39;49;00m[37m[39;49;00m$
   280^I[37m^I[39;49;00minterpreter_lock[37m [39;49;00m=[37m [39;49;00mPyThread_allocate_lock();[37m[39;49;00m$
   281^I[37m^I[39;49;00mPyThread_acquire_lock(interpreter_lock,[37m [39;49;00m[34m1[39;49;00m);[37m[39;49;00m$
   282^I[37m^I[39;49;00mmain_thread[37m [39;49;00m=[37m [39;49;00mPyThread_get_thread_ident();[37m[39;49;00m$
   283^I}[37m[39;49;00m$
   284^I[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   285^I[37m[39;49;00m$
   286^I[37m/* Functions save_thread and restore_thread are always defined so[39;49;00m$
   287^I[37m   dynamically loaded modules needn't be compiled separately for use[39;49;00m$
   288^I[37m   with and without threads: */[39;49;00m[37m[39;49;00m$
   289^I[37m[39;49;00m$
   290^IPyThreadState[37m [39;49;00m*[37m[39;49;00m$
   291^I[32mPyEval_SaveThread[39;49;00m([36mvoid[39;49;00m)[37m[39;49;00m$
   292^I{[37m[39;49;00m$
   293^I[37m^I[39;49;00mPyThreadState[37m [39;49;00m*tstate[37m [39;49;00m=[37m [39;49;00mPyThreadState_Swap([36mNULL[39;49;00m);[37m[39;49;00m$
   294^I[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(tstate[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
   295^I[37m^I^I[39;49;00mPy_FatalError([33m"[39;49;00m[33mPyEval_SaveThread: NULL tstate[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
   296^I[36m#[39;49;00m[36mifdef WITH_THREAD[39;49;00m[36m[39;49;00m$
   297^I[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(interpreter_lock)[37m[39;49;00m$
   298^I[37m^I^I[39;49;00mPyThread_release_lock(interpreter_lock);[37m[39;49;00m$
   299^I[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   300^I[37m^I[39;49;00m[34mreturn[39;49;00m[37m [39;49;00mtstate;[37m[39;49;00m$
   301^I}[37m[39;49;00m$
   302^I[37m[39;49;00m$
   303^I[36mvoid[39;49;00m[37m[39;49;00m$
   304^I[32mPyEval_RestoreThread[39;49;00m(PyThreadState[37m [39;49;00m*tstate)[37m[39;49;00m$
   305^I{[37m[39;49;00m$
   306^I[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(tstate[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
   307^I[37m^I^I[39;49;00mPy_FatalError([33m"[39;49;00m[33mPyEval_RestoreThread: NULL tstate[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
   308^I[36m#[39;49;00m[36mifdef WITH_THREAD[39;49;00m[36m[39;49;00m$
   309^I[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(interpreter_lock)[37m [39;49;00m{[37m[39;49;00m$
   310^I[37m^I^I[39;49;00m[36mint[39;49;00m[37m [39;49;00merr[37m [39;49;00m=[37m [39;49;00merrno;[37m[39;49;00m$
   311^I[37m^I^I[39;49;00mPyThread_acquire_lock(interpreter_lock,[37m [39;49;00m[34m1[39;49;00m);[37m[39;49;00m$
   312^I[37m^I^I[39;49;00merrno[37m [39;49;00m=[37m [39;49;00merr;[37m[39;49;00m$
   313^I[37m^I[39;49;00m}[37m[39;49;00m$
   314^I[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   315^I[37m^I[39;49;00mPyThreadState_Swap(tstate);[37m[39;49;00m$
   316^I}[37m[39;49;00m$
   317^I[37m[39;49;00m$
   318^I[37m[39;49;00m$
   319^I[37m/* Mechanism whereby asynchronously executing callbacks (e.g. UNIX[39;49;00m$
   320^I[37m   signal handlers or Mac I/O completion routines) can schedule calls[39;49;00m$
   321^I[37m   to a function to be called synchronously.[39;49;00m$
   322^I[37m   The synchronous function is called with one void* argument.[39;49;00m$
   323^I[37m   It should return 0 for success or -1 for failure -- failure should[39;49;00m$
   324^I[37m   be accompanied by an exception.[39;49;00m$
   325^I[37m[39;49;00m$
   326^I[37m   If registry succeeds, the registry function returns 0; if it fails[39;49;00m$
   327^I[37m   (e.g. due to too many pending calls) it returns -1 (without setting[39;49;00m$
   328^I[37m   an exception condition).[39;49;00m$
   329^I[37m[39;49;00m$
   330^I[37m   Note that because registry may occur from within signal handlers,[39;49;00m$
   331^I[37m   or other asynchronous events, calling malloc() is unsafe![39;49;00m$
   332^I[37m[39;49;00m$
   333^I[37m#ifdef WITH_THREAD[39;49;00m$
   334^I[37m   Any thread can schedule pending calls, but only the main thread[39;49;00m$
   335^I[37m   will execute them.[39;49;00m$
   336^I[37m#endif[39;49;00m$
   337^I[37m[39;49;00m$
   338^I[37m   XXX WARNING!  ASYNCHRONOUSLY EXECUTING CODE![39;49;00m$
   339^I[37m   There are two possible race conditions:[39;49;00m$
   340^I[37m   (1) nested asynchronous registry calls;[39;49;00m$
   341^I[37m   (2) registry calls made while pending calls are being processed.[39;49;00m$
   342^I[37m   While (1) is very unlikely, (2) is a real possibility.[39;49;00m$
   343^I[37m   The current code is safe against (2), but not against (1).[39;49;00m$
   344^I[37m   The safety against (2) is derived from the fact that only one[39;49;00m$
   345^I[37m   thread (the main thread) ever takes things out of the queue.[39;49;00m$
   346^I[37m[39;49;00m$
   347^I[37m   XXX Darn!  With the advent of thread state, we should have an array[39;49;00m$
   348^I[37m   of pending calls per thread in the thread state!  Later...[39;49;00m$
   349^I[37m*/[39;49;00m[37m[39;49;00m$
   350^I[37m[39;49;00m$
   351^I[36m#[39;49;00m[36mdefine NPENDINGCALLS 32[39;49;00m[36m[39;49;00m$
   352^I[34mstatic[39;49;00m[37m [39;49;00m[34mstruct[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
   353^I[37m^I[39;49;00m[36mint[39;49;00m[37m [39;49;00m(*func)([36mvoid[39;49;00m[37m [39;49;00m*);[37m[39;49;00m$
   354^I[37m^I[39;49;00m[36mvoid[39;49;00m[37m [39;49;00m*arg;[37m[39;49;00m$
   355^I}[37m [39;49;00mpendingcalls[NPENDINGCALLS];[37m[39;49;00m$
   356^I[34mstatic[39;49;00m[37m [39;49;00m[34mvolatile[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mpendingfirst[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   357^I[34mstatic[39;49;00m[37m [39;49;00m[34mvolatile[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mpendinglast[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   358^I[34mstatic[39;49;00m[37m [39;49;00m[34mvolatile[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mthings_to_do[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   359^I[37m[39;49;00m$
   360^I[36mint[39;49;00m[37m[39;49;00m$
   361^I[32mPy_AddPendingCall[39;49;00m([36mint[39;49;00m[37m [39;49;00m(*func)([36mvoid[39;49;00m[37m [39;49;00m*),[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m*arg)[37m[39;49;00m$
   362^I{[37m[39;49;00m$
   363^I[37m^I[39;49;00m[34mstatic[39;49;00m[37m [39;49;00m[34mvolatile[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mbusy[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   364^I[37m^I[39;49;00m[36mint[39;49;00m[37m [39;49;00mi,[37m [39;49;00mj;[37m[39;49;00m$
   365^I[37m^I[39;49;00m[37m/* XXX Begin critical section */[39;49;00m[37m[39;49;00m$
   366^I[37m^I[39;49;00m[37m/* XXX If you want this to be safe against nested[39;49;00m$
   367^I[37m^I   XXX asynchronous calls, you'll have to work harder! */[39;49;00m[37m[39;49;00m$
   368^I[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(busy)[37m[39;49;00m$
   369^I[37m^I^I[39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34m-1[39;49;00m;[37m[39;49;00m$
   370^I[37m^I[39;49;00mbusy[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
   371^I[37m^I[39;49;00mi[37m [39;49;00m=[37m [39;49;00mpendinglast;[37m[39;49;00m$
   372^I[37m^I[39;49;00mj[37m [39;49;00m=[37m [39;49;00m(i[37m [39;49;00m+[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m%[37m [39;49;00mNPENDINGCALLS;[37m[39;49;00m$
   373^I[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(j[37m [39;49;00m==[37m [39;49;00mpendingfirst)[37m [39;49;00m{[37m[39;49;00m$
   374^I[37m^I^I[39;49;00mbusy[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   375^I[37m^I^I[39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34m-1[39;49;00m;[37m [39;49;00m[37m/* Queue full */[39;49;00m[37m[39;49;00m$
   376^I[37m^I[39;49;00m}[37m[39;49;00m$
   377^I[37m^I[39;49;00mpendingcalls[i].func[37m [39;49;00m=[37m [39;49;00mfunc;[37m[39;49;00m$
   378^I[37m^I[39;49;00mpendingcalls[i].arg[37m [39;49;00m=[37m [39;49;00marg;[37m[39;49;00m$
   379^I[37m^I[39;49;00mpendinglast[37m [39;49;00m=[37m [39;49;00mj;[37m[39;49;00m$
   380^I[37m[39;49;00m$
   381^I[37m^I[39;49;00m_Py_Ticker[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   382^I[37m^I[39;49;00mthings_to_do[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m;[37m [39;49;00m[37m/* Signal main loop */[39;49;00m[37m[39;49;00m$
   383^I[37m^I[39;49;00mbusy[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   384^I[37m^I[39;49;00m[37m/* XXX End critical section */[39;49;00m[37m[39;49;00m$
   385^I[37m^I[39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   386^I}[37m[39;49;00m$
   387^I[37m[39;49;00m$
   388^I[36mint[39;49;00m[37m[39;49;00m$
   389^I[32mPy_MakePendingCalls[39;49;00m([36mvoid[39;49;00m)[37m[39;49;00m$
   390^I{[37m[39;49;00m$
   391^I[37m^I[39;49;00m[34mstatic[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mbusy[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   392^I[36m#[39;49;00m[36mifdef WITH_THREAD[39;49;00m[36m[39;49;00m$
   393^I[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(main_thread[37m [39;49;00m&&[37m [39;49;00mPyThread_get_thread_ident()[37m [39;49;00m!=[37m [39;49;00mmain_thread)[37m[39;49;00m$
   394^I[37m^I^I[39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   395^I[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   396^I[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(busy)[37m[39;49;00m$
   397^I[37m^I^I[39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   398^I[37m^I[39;49;00mbusy[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
   399^I[37m^I[39;49;00mthings_to_do[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   400^I[37m^I[39;49;00m[34mfor[39;49;00m[37m [39;49;00m(;;)[37m [39;49;00m{[37m[39;49;00m$
   401^I[37m^I^I[39;49;00m[36mint[39;49;00m[37m [39;49;00mi;[37m[39;49;00m$
   402^I[37m^I^I[39;49;00m[36mint[39;49;00m[37m [39;49;00m(*func)([36mvoid[39;49;00m[37m [39;49;00m*);[37m[39;49;00m$
   403^I[37m^I^I[39;49;00m[36mvoid[39;49;00m[37m [39;49;00m*arg;[37m[39;49;00m$
   404^I[37m^I^I[39;49;00mi[37m [39;49;00m=[37m [39;49;00mpendingfirst;[37m[39;49;00m$
   405^I[37m^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(i[37m [39;49;00m==[37m [39;49;00mpendinglast)[37m[39;49;00m$
   406^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m [39;49;00m[37m/* Queue empty */[39;49;00m[37m[39;49;00m$
   407^I[37m^I^I[39;49;00mfunc[37m [39;49;00m=[37m [39;49;00mpendingcalls[i].func;[37m[39;49;00m$
   408^I[37m^I^I[39;49;00marg[37m [39;49;00m=[37m [39;49;00mpendingcalls[i].arg;[37m[39;49;00m$
   409^I[37m^I^I[39;49;00mpendingfirst[37m [39;49;00m=[37m [39;49;00m(i[37m [39;49;00m+[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m%[37m [39;49;00mNPENDINGCALLS;[37m[39;49;00m$
   410^I[37m^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(func(arg)[37m [39;49;00m<[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
   411^I[37m^I^I^I[39;49;00mbusy[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   412^I[37m^I^I^I[39;49;00mthings_to_do[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m;[37m [39;49;00m[37m/* We're not done yet */[39;49;00m[37m[39;49;00m$
   413^I[37m^I^I^I[39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34m-1[39;49;00m;[37m[39;49;00m$
   414^I[37m^I^I[39;49;00m}[37m[39;49;00m$
   415^I[37m^I[39;49;00m}[37m[39;49;00m$
   416^I[37m^I[39;49;00mbusy[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   417^I[37m^I[39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   418^I}[37m[39;49;00m$
   419^I[37m[39;49;00m$
   420^I[37m[39;49;00m$
   421^I[37m/* The interpreter's recursion limit */[39;49;00m[37m[39;49;00m$
   422^I[37m[39;49;00m$
   423^I[36m#[39;49;00m[36mifndef Py_DEFAULT_RECURSION_LIMIT[39;49;00m[36m[39;49;00m$
   424^I[36m#[39;49;00m[36mdefine Py_DEFAULT_RECURSION_LIMIT 1000[39;49;00m[36m[39;49;00m$
   425^I[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   426^I[34mstatic[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mrecursion_limit[37m [39;49;00m=[37m [39;49;00mPy_DEFAULT_RECURSION_LIMIT;[37m[39;49;00m$
   427^I[36mint[39;49;00m[37m [39;49;00m_Py_CheckRecursionLimit[37m [39;49;00m=[37m [39;49;00mPy_DEFAULT_RECURSION_LIMIT;[37m[39;49;00m$
   428^I[37m[39;49;00m$
   429^I[36mint[39;49;00m[37m[39;49;00m$
   430^I[32mPy_GetRecursionLimit[39;49;00m([36mvoid[39;49;00m)[37m[39;49;00m$
   431^I{[37m[39;49;00m$
   432^I[37m^I[39;49;00m[34mreturn[39;49;00m[37m [39;49;00mrecursion_limit;[37m[39;49;00m$
   433^I}[37m[39;49;00m$
   434^I[37m[39;49;00m$
   435^I[36mvoid[39;49;00m[37m[39;49;00m$
   436^I[32mPy_SetRecursionLimit[39;49;00m([36mint[39;49;00m[37m [39;49;00mnew_limit)[37m[39;49;00m$
   437^I{[37m[39;49;00m$
   438^I[37m^I[39;49;00mrecursion_limit[37m [39;49;00m=[37m [39;49;00mnew_limit;[37m[39;49;00m$
   439^I[37m        [39;49;00m_Py_CheckRecursionLimit[37m [39;49;00m=[37m [39;49;00mrecursion_limit;[37m[39;49;00m$
   440^I}[37m[39;49;00m$
   441^I[37m[39;49;00m$
   442^I[37m/* the macro Py_EnterRecursiveCall() only calls _Py_CheckRecursiveCall()[39;49;00m$
   443^I[37m   if the recursion_depth reaches _Py_CheckRecursionLimit.[39;49;00m$
   444^I[37m   If USE_STACKCHECK, the macro decrements _Py_CheckRecursionLimit[39;49;00m$
   445^I[37m   to guarantee that _Py_CheckRecursiveCall() is regularly called.[39;49;00m$
   446^I[37m   Without USE_STACKCHECK, there is no need for this. */[39;49;00m[37m[39;49;00m$
   447^I[36mint[39;49;00m[37m[39;49;00m$
   448^I[32m_Py_CheckRecursiveCall[39;49;00m([36mchar[39;49;00m[37m [39;49;00m*where)[37m[39;49;00m$
   449^I{[37m[39;49;00m$
   450^I[37m^I[39;49;00mPyThreadState[37m [39;49;00m*tstate[37m [39;49;00m=[37m [39;49;00mPyThreadState_GET();[37m[39;49;00m$
   451^I[37m[39;49;00m$
   452^I[36m#[39;49;00m[36mifdef USE_STACKCHECK[39;49;00m[36m[39;49;00m$
   453^I[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyOS_CheckStack())[37m [39;49;00m{[37m[39;49;00m$
   454^I[37m^I^I[39;49;00m--tstate->recursion_depth;[37m[39;49;00m$
   455^I[37m^I^I[39;49;00mPyErr_SetString(PyExc_MemoryError,[37m [39;49;00m[33m"[39;49;00m[33mStack overflow[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
   456^I[37m^I^I[39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34m-1[39;49;00m;[37m[39;49;00m$
   457^I[37m^I[39;49;00m}[37m[39;49;00m$
   458^I[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   459^I[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(tstate->recursion_depth[37m [39;49;00m>[37m [39;49;00mrecursion_limit)[37m [39;49;00m{[37m[39;49;00m$
   460^I[37m^I^I[39;49;00m--tstate->recursion_depth;[37m[39;49;00m$
   461^I[37m^I^I[39;49;00mPyErr_Format(PyExc_RuntimeError,[37m[39;49;00m$
   462^I[37m^I^I^I     [39;49;00m[33m"[39;49;00m[33mmaximum recursion depth exceeded%s[39;49;00m[33m"[39;49;00m,[37m[39;49;00m$
   463^I[37m^I^I^I     [39;49;00mwhere);[37m[39;49;00m$
   464^I[37m^I^I[39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34m-1[39;49;00m;[37m[39;49;00m$
   465^I[37m^I[39;49;00m}[37m[39;49;00m$
   466^I[37m        [39;49;00m_Py_CheckRecursionLimit[37m [39;49;00m=[37m [39;49;00mrecursion_limit;[37m[39;49;00m$
   467^I[37m^I[39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   468^I}[37m[39;49;00m$
   469^I[37m[39;49;00m$
   470^I[37m/* Status code for main loop (reason for stack unwind) */[39;49;00m[37m[39;49;00m$
   471^I[34menum[39;49;00m[37m [39;49;00mwhy_code[37m [39;49;00m{[37m[39;49;00m$
   472^I[37m^I^I[39;49;00mWHY_NOT[37m [39;49;00m=[37m^I[39;49;00m[34m0x0001[39;49;00m,[37m^I[39;49;00m[37m/* No error */[39;49;00m[37m[39;49;00m$
   473^I[37m^I^I[39;49;00mWHY_EXCEPTION[37m [39;49;00m=[37m [39;49;00m[34m0x0002[39;49;00m,[37m^I[39;49;00m[37m/* Exception occurred */[39;49;00m[37m[39;49;00m$
   474^I[37m^I^I[39;49;00mWHY_RERAISE[37m [39;49;00m=[37m^I[39;49;00m[34m0x0004[39;49;00m,[37m^I[39;49;00m[37m/* Exception re-raised by 'finally' */[39;49;00m[37m[39;49;00m$
   475^I[37m^I^I[39;49;00mWHY_RETURN[37m [39;49;00m=[37m^I[39;49;00m[34m0x0008[39;49;00m,[37m^I[39;49;00m[37m/* 'return' statement */[39;49;00m[37m[39;49;00m$
   476^I[37m^I^I[39;49;00mWHY_BREAK[37m [39;49;00m=[37m^I[39;49;00m[34m0x0010[39;49;00m,[37m^I[39;49;00m[37m/* 'break' statement */[39;49;00m[37m[39;49;00m$
   477^I[37m^I^I[39;49;00mWHY_CONTINUE[37m [39;49;00m=[37m^I[39;49;00m[34m0x0020[39;49;00m,[37m^I[39;49;00m[37m/* 'continue' statement */[39;49;00m[37m[39;49;00m$
   478^I[37m^I^I[39;49;00mWHY_YIELD[37m [39;49;00m=[37m^I[39;49;00m[34m0x0040[39;49;00m[37m^I[39;49;00m[37m/* 'yield' operator */[39;49;00m[37m[39;49;00m$
   479^I};[37m[39;49;00m$
   480^I[37m[39;49;00m$
   481^I[34mstatic[39;49;00m[37m [39;49;00m[34menum[39;49;00m[37m [39;49;00mwhy_code[37m [39;49;00m[32mdo_raise[39;49;00m(PyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*);[37m[39;49;00m$
   482^I[34mstatic[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00m[32munpack_iterable[39;49;00m(PyObject[37m [39;49;00m*,[37m [39;49;00m[36mint[39;49;00m,[37m [39;49;00mPyObject[37m [39;49;00m**);[37m[39;49;00m$
   483^I[37m[39;49;00m$
   484^I[37m/* for manipulating the thread switch and periodic "stuff" - used to be[39;49;00m$
   485^I[37m   per thread, now just a pair o' globals */[39;49;00m[37m[39;49;00m$
   486^I[36mint[39;49;00m[37m [39;49;00m_Py_CheckInterval[37m [39;49;00m=[37m [39;49;00m[34m100[39;49;00m;[37m[39;49;00m$
   487^I[34mvolatile[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00m_Py_Ticker[37m [39;49;00m=[37m [39;49;00m[34m100[39;49;00m;[37m[39;49;00m$
   488^I[37m[39;49;00m$
   489^IPyObject[37m [39;49;00m*[37m[39;49;00m$
   490^I[32mPyEval_EvalCode[39;49;00m(PyCodeObject[37m [39;49;00m*co,[37m [39;49;00mPyObject[37m [39;49;00m*globals,[37m [39;49;00mPyObject[37m [39;49;00m*locals)[37m[39;49;00m$
   491^I{[37m[39;49;00m$
   492^I[37m^I[39;49;00m[37m/* XXX raise SystemError if globals is NULL */[39;49;00m[37m[39;49;00m$
   493^I[37m^I[39;49;00m[34mreturn[39;49;00m[37m [39;49;00mPyEval_EvalCodeEx(co,[37m[39;49;00m$
   494^I[37m^I^I^I  [39;49;00mglobals,[37m [39;49;00mlocals,[37m[39;49;00m$
   495^I[37m^I^I^I  [39;49;00m(PyObject[37m [39;49;00m**)[36mNULL[39;49;00m,[37m [39;49;00m[34m0[39;49;00m,[37m[39;49;00m$
   496^I[37m^I^I^I  [39;49;00m(PyObject[37m [39;49;00m**)[36mNULL[39;49;00m,[37m [39;49;00m[34m0[39;49;00m,[37m[39;49;00m$
   497^I[37m^I^I^I  [39;49;00m(PyObject[37m [39;49;00m**)[36mNULL[39;49;00m,[37m [39;49;00m[34m0[39;49;00m,[37m[39;49;00m$
   498^I[37m^I^I^I  [39;49;00m[36mNULL[39;49;00m);[37m[39;49;00m$
   499^I}[37m[39;49;00m$
   500^I[37m[39;49;00m$
   501^I[37m[39;49;00m$
   502^I[37m/* Interpreter main loop */[39;49;00m[37m[39;49;00m$
   503^I[37m[39;49;00m$
   504^IPyObject[37m [39;49;00m*[37m[39;49;00m$
   505^I[32mPyEval_EvalFrame[39;49;00m(PyFrameObject[37m [39;49;00m*f)[37m [39;49;00m{[37m[39;49;00m$
   506^I[37m^I[39;49;00m[37m/* This is for backward compatibility with extension modules that[39;49;00m$
   507^I[37m           used this API; core interpreter code should call PyEval_EvalFrameEx() */[39;49;00m[37m[39;49;00m$
   508^I[37m^I[39;49;00m[34mreturn[39;49;00m[37m [39;49;00mPyEval_EvalFrameEx(f,[37m [39;49;00m[34m0[39;49;00m);[37m[39;49;00m$
   509^I}[37m[39;49;00m$
   510^I[37m[39;49;00m$
   511^IPyObject[37m [39;49;00m*[37m[39;49;00m$
   512^I[32mPyEval_EvalFrameEx[39;49;00m(PyFrameObject[37m [39;49;00m*f,[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mthrowflag)[37m[39;49;00m$
   513^I{[37m[39;49;00m$
   514^I[36m#[39;49;00m[36mifdef DXPAIRS[39;49;00m[36m[39;49;00m$
   515^I[37m^I[39;49;00m[36mint[39;49;00m[37m [39;49;00mlastopcode[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   516^I[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   517^I[37m^I[39;49;00m[34mregister[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m**stack_pointer;[37m   [39;49;00m[37m/* Next free slot in value stack */[39;49;00m[37m[39;49;00m$
   518^I[37m^I[39;49;00m[34mregister[39;49;00m[37m [39;49;00m[36munsigned[39;49;00m[37m [39;49;00m[36mchar[39;49;00m[37m [39;49;00m*next_instr;[37m[39;49;00m$
   519^I[37m^I[39;49;00m[34mregister[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mopcode;[37m^I[39;49;00m[37m/* Current opcode */[39;49;00m[37m[39;49;00m$
   520^I[37m^I[39;49;00m[34mregister[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00moparg;[37m^I[39;49;00m[37m/* Current opcode argument, if any */[39;49;00m[37m[39;49;00m$
   521^I[37m^I[39;49;00m[34mregister[39;49;00m[37m [39;49;00m[34menum[39;49;00m[37m [39;49;00mwhy_code[37m [39;49;00mwhy;[37m [39;49;00m[37m/* Reason for block stack unwind */[39;49;00m[37m[39;49;00m$
   522^I[37m^I[39;49;00m[34mregister[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00merr;[37m^I[39;49;00m[37m/* Error status -- nonzero if error */[39;49;00m[37m[39;49;00m$
   523^I[37m^I[39;49;00m[34mregister[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*x;[37m^I[39;49;00m[37m/* Result object -- NULL if error */[39;49;00m[37m[39;49;00m$
   524^I[37m^I[39;49;00m[34mregister[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*v;[37m^I[39;49;00m[37m/* Temporary objects popped off stack */[39;49;00m[37m[39;49;00m$
   525^I[37m^I[39;49;00m[34mregister[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*w;[37m[39;49;00m$
   526^I[37m^I[39;49;00m[34mregister[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*u;[37m[39;49;00m$
   527^I[37m^I[39;49;00m[34mregister[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*t;[37m[39;49;00m$
   528^I[37m^I[39;49;00m[34mregister[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*stream[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m    [39;49;00m[37m/* for PRINT opcodes */[39;49;00m[37m[39;49;00m$
   529^I[37m^I[39;49;00m[34mregister[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m**fastlocals,[37m [39;49;00m**freevars;[37m[39;49;00m$
   530^I[37m^I[39;49;00mPyObject[37m [39;49;00m*retval[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m^I[39;49;00m[37m/* Return value */[39;49;00m[37m[39;49;00m$
   531^I[37m^I[39;49;00mPyThreadState[37m [39;49;00m*tstate[37m [39;49;00m=[37m [39;49;00mPyThreadState_GET();[37m[39;49;00m$
   532^I[37m^I[39;49;00mPyCodeObject[37m [39;49;00m*co;[37m[39;49;00m$
   533^I[37m[39;49;00m$
   534^I[37m^I[39;49;00m[37m/* when tracing we set things up so that[39;49;00m$
   535^I[37m[39;49;00m$
   536^I[37m               not (instr_lb <= current_bytecode_offset < instr_ub)[39;49;00m$
   537^I[37m[39;49;00m$
   538^I[37m^I   is true when the line being executed has changed.  The[39;49;00m$
   539^I[37m           initial values are such as to make this false the first[39;49;00m$
   540^I[37m           time it is tested. */[39;49;00m[37m[39;49;00m$
   541^I[37m^I[39;49;00m[36mint[39;49;00m[37m [39;49;00minstr_ub[37m [39;49;00m=[37m [39;49;00m[34m-1[39;49;00m,[37m [39;49;00minstr_lb[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m,[37m [39;49;00minstr_prev[37m [39;49;00m=[37m [39;49;00m[34m-1[39;49;00m;[37m[39;49;00m$
   542^I[37m[39;49;00m$
   543^I[37m^I[39;49;00m[36munsigned[39;49;00m[37m [39;49;00m[36mchar[39;49;00m[37m [39;49;00m*first_instr;[37m[39;49;00m$
   544^I[37m^I[39;49;00mPyObject[37m [39;49;00m*names;[37m[39;49;00m$
   545^I[37m^I[39;49;00mPyObject[37m [39;49;00m*consts;[37m[39;49;00m$
   546^I[36m#[39;49;00m[36mif defined(Py_DEBUG) || defined(LLTRACE)[39;49;00m[36m[39;49;00m$
   547^I[37m^I[39;49;00m[37m/* Make it easier to find out where we are with a debugger */[39;49;00m[37m[39;49;00m$
   548^I[37m^I[39;49;00m[36mchar[39;49;00m[37m [39;49;00m*filename;[37m[39;49;00m$
   549^I[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   550^I[37m[39;49;00m$
   551^I[37m/* Tuple access macros */[39;49;00m[37m[39;49;00m$
   552^I[37m[39;49;00m$
   553^I[36m#[39;49;00m[36mifndef Py_DEBUG[39;49;00m[36m[39;49;00m$
   554^I[36m#[39;49;00m[36mdefine GETITEM(v, i) PyTuple_GET_ITEM((PyTupleObject *)(v), (i))[39;49;00m[36m[39;49;00m$
   555^I[36m#[39;49;00m[36melse[39;49;00m[36m[39;49;00m$
   556^I[36m#[39;49;00m[36mdefine GETITEM(v, i) PyTuple_GetItem((v), (i))[39;49;00m[36m[39;49;00m$
   557^I[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   558^I[37m[39;49;00m$
   559^I[36m#[39;49;00m[36mifdef WITH_TSC[39;49;00m[36m[39;49;00m$
   560^I[37m/* Use Pentium timestamp counter to mark certain events:[39;49;00m$
   561^I[37m   inst0 -- beginning of switch statement for opcode dispatch[39;49;00m$
   562^I[37m   inst1 -- end of switch statement (may be skipped)[39;49;00m$
   563^I[37m   loop0 -- the top of the mainloop[39;49;00m$
   564^I[37m   loop1 -- place where control returns again to top of mainloop[39;49;00m$
   565^I[37m            (may be skipped)[39;49;00m$
   566^I[37m   intr1 -- beginning of long interruption[39;49;00m$
   567^I[37m   intr2 -- end of long interruption[39;49;00m$
   568^I[37m[39;49;00m$
   569^I[37m   Many opcodes call out to helper C functions.  In some cases, the[39;49;00m$
   570^I[37m   time in those functions should be counted towards the time for the[39;49;00m$
   571^I[37m   opcode, but not in all cases.  For example, a CALL_FUNCTION opcode[39;49;00m$
   572^I[37m   calls another Python function; there's no point in charge all the[39;49;00m$
   573^I[37m   bytecode executed by the called function to the caller.[39;49;00m$
   574^I[37m[39;49;00m$
   575^I[37m   It's hard to make a useful judgement statically.  In the presence[39;49;00m$
   576^I[37m   of operator overloading, it's impossible to tell if a call will[39;49;00m$
   577^I[37m   execute new Python code or not.[39;49;00m$
   578^I[37m[39;49;00m$
   579^I[37m   It's a case-by-case judgement.  I'll use intr1 for the following[39;49;00m$
   580^I[37m   cases:[39;49;00m$
   581^I[37m[39;49;00m$
   582^I[37m   EXEC_STMT[39;49;00m$
   583^I[37m   IMPORT_STAR[39;49;00m$
   584^I[37m   IMPORT_FROM[39;49;00m$
   585^I[37m   CALL_FUNCTION (and friends)[39;49;00m$
   586^I[37m[39;49;00m$
   587^I[37m */[39;49;00m[37m[39;49;00m$
   588^I[37m^I[39;49;00muint64[37m [39;49;00minst0,[37m [39;49;00minst1,[37m [39;49;00mloop0,[37m [39;49;00mloop1,[37m [39;49;00mintr0[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m,[37m [39;49;00mintr1[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   589^I[37m^I[39;49;00m[36mint[39;49;00m[37m [39;49;00mticked[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   590^I[37m[39;49;00m$
   591^I[37m^I[39;49;00mREAD_TIMESTAMP(inst0);[37m[39;49;00m$
   592^I[37m^I[39;49;00mREAD_TIMESTAMP(inst1);[37m[39;49;00m$
   593^I[37m^I[39;49;00mREAD_TIMESTAMP(loop0);[37m[39;49;00m$
   594^I[37m^I[39;49;00mREAD_TIMESTAMP(loop1);[37m[39;49;00m$
   595^I[37m[39;49;00m$
   596^I[37m^I[39;49;00m[37m/* shut up the compiler */[39;49;00m[37m[39;49;00m$
   597^I[37m^I[39;49;00mopcode[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   598^I[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   599^I[37m[39;49;00m$
   600^I[37m/* Code access macros */[39;49;00m[37m[39;49;00m$
   601^I[37m[39;49;00m$
   602^I[36m#[39;49;00m[36mdefine INSTR_OFFSET()^I((int)(next_instr - first_instr))[39;49;00m[36m[39;49;00m$
   603^I[36m#[39;49;00m[36mdefine NEXTOP()^I(*next_instr++)[39;49;00m[36m[39;49;00m$
   604^I[36m#[39;49;00m[36mdefine NEXTARG()^I(next_instr += 2, (next_instr[-1]<<8) + next_instr[-2])[39;49;00m[36m[39;49;00m$
   605^I[36m#[39;49;00m[36mdefine PEEKARG()^I((next_instr[2]<<8) + next_instr[1])[39;49;00m[36m[39;49;00m$
   606^I[36m#[39;49;00m[36mdefine JUMPTO(x)^I(next_instr = first_instr + (x))[39;49;00m[36m[39;49;00m$
   607^I[36m#[39;49;00m[36mdefine JUMPBY(x)^I(next_instr += (x))[39;49;00m[36m[39;49;00m$
   608^I[37m[39;49;00m$
   609^I[37m/* OpCode prediction macros[39;49;00m$
   610^I[37m^ISome opcodes tend to come in pairs thus making it possible to predict[39;49;00m$
   611^I[37m^Ithe second code when the first is run.  For example, COMPARE_OP is often[39;49;00m$
   612^I[37m^Ifollowed by JUMP_IF_FALSE or JUMP_IF_TRUE.  And, those opcodes are often[39;49;00m$
   613^I[37m^Ifollowed by a POP_TOP.[39;49;00m$
   614^I[37m[39;49;00m$
   615^I[37m^IVerifying the prediction costs a single high-speed test of register[39;49;00m$
   616^I[37m^Ivariable against a constant.  If the pairing was good, then the[39;49;00m$
   617^I[37m^Iprocessor has a high likelihood of making its own successful branch[39;49;00m$
   618^I[37m^Iprediction which results in a nearly zero overhead transition to the[39;49;00m$
   619^I[37m^Inext opcode.[39;49;00m$
   620^I[37m[39;49;00m$
   621^I[37m^IA successful prediction saves a trip through the eval-loop including[39;49;00m$
   622^I[37m^Iits two unpredictable branches, the HASARG test and the switch-case.[39;49;00m$
   623^I[37m[39;49;00m$
   624^I[37m        If collecting opcode statistics, turn off prediction so that[39;49;00m$
   625^I[37m^Istatistics are accurately maintained (the predictions bypass[39;49;00m$
   626^I[37m^Ithe opcode frequency counter updates).[39;49;00m$
   627^I[37m*/[39;49;00m[37m[39;49;00m$
   628^I[37m[39;49;00m$
   629^I[36m#[39;49;00m[36mifdef DYNAMIC_EXECUTION_PROFILE[39;49;00m[36m[39;49;00m$
   630^I[36m#[39;49;00m[36mdefine PREDICT(op)^I^Iif (0) goto PRED_##op[39;49;00m[36m[39;49;00m$
   631^I[36m#[39;49;00m[36melse[39;49;00m[36m[39;49;00m$
   632^I[36m#[39;49;00m[36mdefine PREDICT(op)^I^Iif (*next_instr == op) goto PRED_##op[39;49;00m[36m[39;49;00m$
   633^I[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   634^I[37m[39;49;00m$
   635^I[36m#[39;49;00m[36mdefine PREDICTED(op)^I^IPRED_##op: next_instr++[39;49;00m[36m[39;49;00m$
   636^I[36m#[39;49;00m[36mdefine PREDICTED_WITH_ARG(op)^IPRED_##op: oparg = PEEKARG(); next_instr += 3[39;49;00m[36m[39;49;00m$
   637^I[37m[39;49;00m$
   638^I[37m/* Stack manipulation macros */[39;49;00m[37m[39;49;00m$
   639^I[37m[39;49;00m$
   640^I[37m/* The stack can grow at most MAXINT deep, as co_nlocals and[39;49;00m$
   641^I[37m   co_stacksize are ints. */[39;49;00m[37m[39;49;00m$
   642^I[36m#[39;49;00m[36mdefine STACK_LEVEL()^I((int)(stack_pointer - f->f_valuestack))[39;49;00m[36m[39;49;00m$
   643^I[36m#[39;49;00m[36mdefine EMPTY()^I^I(STACK_LEVEL() == 0)[39;49;00m[36m[39;49;00m$
   644^I[36m#[39;49;00m[36mdefine TOP()^I^I(stack_pointer[-1])[39;49;00m[36m[39;49;00m$
   645^I[36m#[39;49;00m[36mdefine SECOND()^I(stack_pointer[-2])[39;49;00m[36m[39;49;00m$
   646^I[36m#[39;49;00m[36mdefine THIRD() ^I(stack_pointer[-3])[39;49;00m[36m[39;49;00m$
   647^I[36m#[39;49;00m[36mdefine FOURTH()^I(stack_pointer[-4])[39;49;00m[36m[39;49;00m$
   648^I[36m#[39;49;00m[36mdefine SET_TOP(v)^I(stack_pointer[-1] = (v))[39;49;00m[36m[39;49;00m$
   649^I[36m#[39;49;00m[36mdefine SET_SECOND(v)^I(stack_pointer[-2] = (v))[39;49;00m[36m[39;49;00m$
   650^I[36m#[39;49;00m[36mdefine SET_THIRD(v)^I(stack_pointer[-3] = (v))[39;49;00m[36m[39;49;00m$
   651^I[36m#[39;49;00m[36mdefine SET_FOURTH(v)^I(stack_pointer[-4] = (v))[39;49;00m[36m[39;49;00m$
   652^I[36m#[39;49;00m[36mdefine BASIC_STACKADJ(n)^I(stack_pointer += n)[39;49;00m[36m[39;49;00m$
   653^I[36m#[39;49;00m[36mdefine BASIC_PUSH(v)^I(*stack_pointer++ = (v))[39;49;00m[36m[39;49;00m$
   654^I[36m#[39;49;00m[36mdefine BASIC_POP()^I(*--stack_pointer)[39;49;00m[36m[39;49;00m$
   655^I[37m[39;49;00m$
   656^I[36m#[39;49;00m[36mifdef LLTRACE[39;49;00m[36m[39;49;00m$
   657^I[36m#[39;49;00m[36mdefine PUSH(v)^I^I{ (void)(BASIC_PUSH(v), \[39;49;00m[36m[39;49;00m$
   658^I[36m                               lltrace && prtrace(TOP(), "push")); \[39;49;00m[36m[39;49;00m$
   659^I[36m                               assert(STACK_LEVEL() <= co->co_stacksize); }[39;49;00m[36m[39;49;00m$
   660^I[36m#[39;49;00m[36mdefine POP()^I^I((void)(lltrace && prtrace(TOP(), "pop")), BASIC_POP())[39;49;00m[36m[39;49;00m$
   661^I[36m#[39;49;00m[36mdefine STACKADJ(n)^I{ (void)(BASIC_STACKADJ(n), \[39;49;00m[36m[39;49;00m$
   662^I[36m                               lltrace && prtrace(TOP(), "stackadj")); \[39;49;00m[36m[39;49;00m$
   663^I[36m                               assert(STACK_LEVEL() <= co->co_stacksize); }[39;49;00m[36m[39;49;00m$
   664^I[36m#[39;49;00m[36mdefine EXT_POP(STACK_POINTER) (lltrace && prtrace(*(STACK_POINTER), "ext_pop"), *--(STACK_POINTER))[39;49;00m[36m[39;49;00m$
   665^I[36m#[39;49;00m[36melse[39;49;00m[36m[39;49;00m$
   666^I[36m#[39;49;00m[36mdefine PUSH(v)^I^IBASIC_PUSH(v)[39;49;00m[36m[39;49;00m$
   667^I[36m#[39;49;00m[36mdefine POP()^I^IBASIC_POP()[39;49;00m[36m[39;49;00m$
   668^I[36m#[39;49;00m[36mdefine STACKADJ(n)^IBASIC_STACKADJ(n)[39;49;00m[36m[39;49;00m$
   669^I[36m#[39;49;00m[36mdefine EXT_POP(STACK_POINTER) (*--(STACK_POINTER))[39;49;00m[36m[39;49;00m$
   670^I[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   671^I[37m[39;49;00m$
   672^I[37m/* Local variable macros */[39;49;00m[37m[39;49;00m$
   673^I[37m[39;49;00m$
   674^I[36m#[39;49;00m[36mdefine GETLOCAL(i)^I(fastlocals[i])[39;49;00m[36m[39;49;00m$
   675^I[37m[39;49;00m$
   676^I[37m/* The SETLOCAL() macro must not DECREF the local variable in-place and[39;49;00m$
   677^I[37m   then store the new value; it must copy the old value to a temporary[39;49;00m$
   678^I[37m   value, then store the new value, and then DECREF the temporary value.[39;49;00m$
   679^I[37m   This is because it is possible that during the DECREF the frame is[39;49;00m$
   680^I[37m   accessed by other code (e.g. a __del__ method or gc.collect()) and the[39;49;00m$
   681^I[37m   variable would be pointing to already-freed memory. */[39;49;00m[37m[39;49;00m$
   682^I[36m#[39;49;00m[36mdefine SETLOCAL(i, value)^Ido { PyObject *tmp = GETLOCAL(i); \[39;49;00m[36m[39;49;00m$
   683^I[36m^I^I^I^I     GETLOCAL(i) = value; \[39;49;00m[36m[39;49;00m$
   684^I[36m                                     Py_XDECREF(tmp); } while (0)[39;49;00m[36m[39;49;00m$
   685^I[37m[39;49;00m$
   686^I[37m/* Start of code */[39;49;00m[37m[39;49;00m$
   687^I[37m[39;49;00m$
   688^I[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(f[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
   689^I[37m^I^I[39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   690^I[37m[39;49;00m$
   691^I[37m^I[39;49;00m[37m/* push frame */[39;49;00m[37m[39;49;00m$
   692^I[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(Py_EnterRecursiveCall([33m"[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
   693^I[37m^I^I[39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   694^I[37m[39;49;00m$
   695^I[37m^I[39;49;00mtstate->frame[37m [39;49;00m=[37m [39;49;00mf;[37m[39;49;00m$
   696^I[37m[39;49;00m$
   697^I[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(tstate->use_tracing)[37m [39;49;00m{[37m[39;49;00m$
   698^I[37m^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(tstate->c_tracefunc[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
   699^I[37m^I^I^I[39;49;00m[37m/* tstate->c_tracefunc, if defined, is a[39;49;00m$
   700^I[37m^I^I^I   function that will be called on *every* entry[39;49;00m$
   701^I[37m^I^I^I   to a code block.  Its return value, if not[39;49;00m$
   702^I[37m^I^I^I   None, is a function that will be called at[39;49;00m$
   703^I[37m^I^I^I   the start of each executed line of code.[39;49;00m$
   704^I[37m^I^I^I   (Actually, the function must return itself[39;49;00m$
   705^I[37m^I^I^I   in order to continue tracing.)  The trace[39;49;00m$
   706^I[37m^I^I^I   functions are called with three arguments:[39;49;00m$
   707^I[37m^I^I^I   a pointer to the current frame, a string[39;49;00m$
   708^I[37m^I^I^I   indicating why the function is called, and[39;49;00m$
   709^I[37m^I^I^I   an argument which depends on the situation.[39;49;00m$
   710^I[37m^I^I^I   The global trace function is also called[39;49;00m$
   711^I[37m^I^I^I   whenever an exception is detected. */[39;49;00m[37m[39;49;00m$
   712^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(call_trace(tstate->c_tracefunc,[37m [39;49;00mtstate->c_traceobj,[37m[39;49;00m$
   713^I[37m^I^I^I^I       [39;49;00mf,[37m [39;49;00mPyTrace_CALL,[37m [39;49;00mPy_None))[37m [39;49;00m{[37m[39;49;00m$
   714^I[37m^I^I^I^I[39;49;00m[37m/* Trace function raised an error */[39;49;00m[37m[39;49;00m$
   715^I[37m^I^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mexit_eval_frame;[37m[39;49;00m$
   716^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
   717^I[37m^I^I[39;49;00m}[37m[39;49;00m$
   718^I[37m^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(tstate->c_profilefunc[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
   719^I[37m^I^I^I[39;49;00m[37m/* Similar for c_profilefunc, except it needn't[39;49;00m$
   720^I[37m^I^I^I   return itself and isn't called for "line" events */[39;49;00m[37m[39;49;00m$
   721^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(call_trace(tstate->c_profilefunc,[37m[39;49;00m$
   722^I[37m^I^I^I^I       [39;49;00mtstate->c_profileobj,[37m[39;49;00m$
   723^I[37m^I^I^I^I       [39;49;00mf,[37m [39;49;00mPyTrace_CALL,[37m [39;49;00mPy_None))[37m [39;49;00m{[37m[39;49;00m$
   724^I[37m^I^I^I^I[39;49;00m[37m/* Profile function raised an error */[39;49;00m[37m[39;49;00m$
   725^I[37m^I^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mexit_eval_frame;[37m[39;49;00m$
   726^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
   727^I[37m^I^I[39;49;00m}[37m[39;49;00m$
   728^I[37m^I[39;49;00m}[37m[39;49;00m$
   729^I[37m[39;49;00m$
   730^I[37m^I[39;49;00mco[37m [39;49;00m=[37m [39;49;00mf->f_code;[37m[39;49;00m$
   731^I[37m^I[39;49;00mnames[37m [39;49;00m=[37m [39;49;00mco->co_names;[37m[39;49;00m$
   732^I[37m^I[39;49;00mconsts[37m [39;49;00m=[37m [39;49;00mco->co_consts;[37m[39;49;00m$
   733^I[37m^I[39;49;00mfastlocals[37m [39;49;00m=[37m [39;49;00mf->f_localsplus;[37m[39;49;00m$
   734^I[37m^I[39;49;00mfreevars[37m [39;49;00m=[37m [39;49;00mf->f_localsplus[37m [39;49;00m+[37m [39;49;00mco->co_nlocals;[37m[39;49;00m$
   735^I[37m^I[39;49;00mfirst_instr[37m [39;49;00m=[37m [39;49;00m([36munsigned[39;49;00m[37m [39;49;00m[36mchar[39;49;00m*)[37m [39;49;00mPyString_AS_STRING(co->co_code);[37m[39;49;00m$
   736^I[37m^I[39;49;00m[37m/* An explanation is in order for the next line.[39;49;00m$
   737^I[37m[39;49;00m$
   738^I[37m^I   f->f_lasti now refers to the index of the last instruction[39;49;00m$
   739^I[37m^I   executed.  You might think this was obvious from the name, but[39;49;00m$
   740^I[37m^I   this wasn't always true before 2.3!  PyFrame_New now sets[39;49;00m$
   741^I[37m^I   f->f_lasti to -1 (i.e. the index *before* the first instruction)[39;49;00m$
   742^I[37m^I   and YIELD_VALUE doesn't fiddle with f_lasti any more.  So this[39;49;00m$
   743^I[37m^I   does work.  Promise. */[39;49;00m[37m[39;49;00m$
   744^I[37m^I[39;49;00mnext_instr[37m [39;49;00m=[37m [39;49;00mfirst_instr[37m [39;49;00m+[37m [39;49;00mf->f_lasti[37m [39;49;00m+[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
   745^I[37m^I[39;49;00mstack_pointer[37m [39;49;00m=[37m [39;49;00mf->f_stacktop;[37m[39;49;00m$
   746^I[37m^I[39;49;00massert(stack_pointer[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m);[37m[39;49;00m$
   747^I[37m^I[39;49;00mf->f_stacktop[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m^I[39;49;00m[37m/* remains NULL unless yield suspends frame */[39;49;00m[37m[39;49;00m$
   748^I[37m[39;49;00m$
   749^I[36m#[39;49;00m[36mifdef LLTRACE[39;49;00m[36m[39;49;00m$
   750^I[37m^I[39;49;00mlltrace[37m [39;49;00m=[37m [39;49;00mPyDict_GetItemString(f->f_globals,[37m [39;49;00m[33m"[39;49;00m[33m__lltrace__[39;49;00m[33m"[39;49;00m)[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   751^I[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   752^I[36m#[39;49;00m[36mif defined(Py_DEBUG) || defined(LLTRACE)[39;49;00m[36m[39;49;00m$
   753^I[37m^I[39;49;00mfilename[37m [39;49;00m=[37m [39;49;00mPyString_AsString(co->co_filename);[37m[39;49;00m$
   754^I[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   755^I[37m[39;49;00m$
   756^I[37m^I[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_NOT;[37m[39;49;00m$
   757^I[37m^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   758^I[37m^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPy_None;[37m^I[39;49;00m[37m/* Not a reference, just anything non-NULL */[39;49;00m[37m[39;49;00m$
   759^I[37m^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   760^I[37m[39;49;00m$
   761^I[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(throwflag)[37m [39;49;00m{[37m [39;49;00m[37m/* support for generator.throw() */[39;49;00m[37m[39;49;00m$
   762^I[37m^I^I[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_EXCEPTION;[37m[39;49;00m$
   763^I[37m^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mon_error;[37m[39;49;00m$
   764^I[37m^I[39;49;00m}[37m[39;49;00m$
   765^I[37m[39;49;00m$
   766^I[37m^I[39;49;00m[34mfor[39;49;00m[37m [39;49;00m(;;)[37m [39;49;00m{[37m[39;49;00m$
   767^I[36m#[39;49;00m[36mifdef WITH_TSC[39;49;00m[36m[39;49;00m$
   768^I[37m^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(inst1[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
   769^I[37m^I^I^I[39;49;00m[37m/* Almost surely, the opcode executed a break[39;49;00m$
   770^I[37m^I^I^I   or a continue, preventing inst1 from being set[39;49;00m$
   771^I[37m^I^I^I   on the way out of the loop.[39;49;00m$
   772^I[37m^I^I^I*/[39;49;00m[37m[39;49;00m$
   773^I[37m^I^I^I[39;49;00mREAD_TIMESTAMP(inst1);[37m[39;49;00m$
   774^I[37m^I^I^I[39;49;00mloop1[37m [39;49;00m=[37m [39;49;00minst1;[37m[39;49;00m$
   775^I[37m^I^I[39;49;00m}[37m[39;49;00m$
   776^I[37m^I^I[39;49;00mdump_tsc(opcode,[37m [39;49;00mticked,[37m [39;49;00minst0,[37m [39;49;00minst1,[37m [39;49;00mloop0,[37m [39;49;00mloop1,[37m[39;49;00m$
   777^I[37m^I^I^I [39;49;00mintr0,[37m [39;49;00mintr1);[37m[39;49;00m$
   778^I[37m^I^I[39;49;00mticked[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   779^I[37m^I^I[39;49;00minst1[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   780^I[37m^I^I[39;49;00mintr0[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   781^I[37m^I^I[39;49;00mintr1[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   782^I[37m^I^I[39;49;00mREAD_TIMESTAMP(loop0);[37m[39;49;00m$
   783^I[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   784^I[37m^I^I[39;49;00massert(stack_pointer[37m [39;49;00m>=[37m [39;49;00mf->f_valuestack);[37m [39;49;00m[37m/* else underflow */[39;49;00m[37m[39;49;00m$
   785^I[37m^I^I[39;49;00massert(STACK_LEVEL()[37m [39;49;00m<=[37m [39;49;00mco->co_stacksize);[37m  [39;49;00m[37m/* else overflow */[39;49;00m[37m[39;49;00m$
   786^I[37m[39;49;00m$
   787^I[37m^I^I[39;49;00m[37m/* Do periodic things.  Doing this every time through[39;49;00m$
   788^I[37m^I^I   the loop would add too much overhead, so we do it[39;49;00m$
   789^I[37m^I^I   only every Nth instruction.  We also do it if[39;49;00m$
   790^I[37m^I^I   ``things_to_do'' is set, i.e. when an asynchronous[39;49;00m$
   791^I[37m^I^I   event needs attention (e.g. a signal handler or[39;49;00m$
   792^I[37m^I^I   async I/O handler); see Py_AddPendingCall() and[39;49;00m$
   793^I[37m^I^I   Py_MakePendingCalls() above. */[39;49;00m[37m[39;49;00m$
   794^I[37m[39;49;00m$
   795^I[37m^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(--_Py_Ticker[37m [39;49;00m<[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
   796^I[37m                        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(*next_instr[37m [39;49;00m==[37m [39;49;00mSETUP_FINALLY)[37m [39;49;00m{[37m[39;49;00m$
   797^I[37m                                [39;49;00m[37m/* Make the last opcode before[39;49;00m$
   798^I[37m                                   a try: finally: block uninterruptable. */[39;49;00m[37m[39;49;00m$
   799^I[37m                                [39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
   800^I[37m                        [39;49;00m}[37m[39;49;00m$
   801^I[37m^I^I^I[39;49;00m_Py_Ticker[37m [39;49;00m=[37m [39;49;00m_Py_CheckInterval;[37m[39;49;00m$
   802^I[37m^I^I^I[39;49;00mtstate->tick_counter++;[37m[39;49;00m$
   803^I[36m#[39;49;00m[36mifdef WITH_TSC[39;49;00m[36m[39;49;00m$
   804^I[37m^I^I^I[39;49;00mticked[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
   805^I[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   806^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(things_to_do)[37m [39;49;00m{[37m[39;49;00m$
   807^I[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(Py_MakePendingCalls()[37m [39;49;00m<[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
   808^I[37m^I^I^I^I^I[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_EXCEPTION;[37m[39;49;00m$
   809^I[37m^I^I^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mon_error;[37m[39;49;00m$
   810^I[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
   811^I[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(things_to_do)[37m[39;49;00m$
   812^I[37m^I^I^I^I^I[39;49;00m[37m/* MakePendingCalls() didn't succeed.[39;49;00m$
   813^I[37m^I^I^I^I^I   Force early re-execution of this[39;49;00m$
   814^I[37m^I^I^I^I^I   "periodic" code, possibly after[39;49;00m$
   815^I[37m^I^I^I^I^I   a thread switch */[39;49;00m[37m[39;49;00m$
   816^I[37m^I^I^I^I^I[39;49;00m_Py_Ticker[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   817^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
   818^I[36m#[39;49;00m[36mifdef WITH_THREAD[39;49;00m[36m[39;49;00m$
   819^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(interpreter_lock)[37m [39;49;00m{[37m[39;49;00m$
   820^I[37m^I^I^I^I[39;49;00m[37m/* Give another thread a chance */[39;49;00m[37m[39;49;00m$
   821^I[37m[39;49;00m$
   822^I[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyThreadState_Swap([36mNULL[39;49;00m)[37m [39;49;00m!=[37m [39;49;00mtstate)[37m[39;49;00m$
   823^I[37m^I^I^I^I^I[39;49;00mPy_FatalError([33m"[39;49;00m[33mceval: tstate mix-up[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
   824^I[37m^I^I^I^I[39;49;00mPyThread_release_lock(interpreter_lock);[37m[39;49;00m$
   825^I[37m[39;49;00m$
   826^I[37m^I^I^I^I[39;49;00m[37m/* Other threads may run now */[39;49;00m[37m[39;49;00m$
   827^I[37m[39;49;00m$
   828^I[37m^I^I^I^I[39;49;00mPyThread_acquire_lock(interpreter_lock,[37m [39;49;00m[34m1[39;49;00m);[37m[39;49;00m$
   829^I[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyThreadState_Swap(tstate)[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
   830^I[37m^I^I^I^I^I[39;49;00mPy_FatalError([33m"[39;49;00m[33mceval: orphan tstate[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
   831^I[37m[39;49;00m$
   832^I[37m^I^I^I^I[39;49;00m[37m/* Check for thread interrupts */[39;49;00m[37m[39;49;00m$
   833^I[37m[39;49;00m$
   834^I[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(tstate->async_exc[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
   835^I[37m^I^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mtstate->async_exc;[37m[39;49;00m$
   836^I[37m^I^I^I^I^I[39;49;00mtstate->async_exc[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   837^I[37m^I^I^I^I^I[39;49;00mPyErr_SetNone(x);[37m[39;49;00m$
   838^I[37m^I^I^I^I^I[39;49;00mPy_DECREF(x);[37m[39;49;00m$
   839^I[37m^I^I^I^I^I[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_EXCEPTION;[37m[39;49;00m$
   840^I[37m^I^I^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mon_error;[37m[39;49;00m$
   841^I[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
   842^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
   843^I[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   844^I[37m^I^I[39;49;00m}[37m[39;49;00m$
   845^I[37m[39;49;00m$
   846^I[37m^I[39;49;00mfast_next_opcode:[37m[39;49;00m$
   847^I[37m^I^I[39;49;00mf->f_lasti[37m [39;49;00m=[37m [39;49;00mINSTR_OFFSET();[37m[39;49;00m$
   848^I[37m[39;49;00m$
   849^I[37m^I^I[39;49;00m[37m/* line-by-line tracing support */[39;49;00m[37m[39;49;00m$
   850^I[37m[39;49;00m$
   851^I[37m^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(tstate->c_tracefunc[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m[37m [39;49;00m&&[37m [39;49;00m!tstate->tracing)[37m [39;49;00m{[37m[39;49;00m$
   852^I[37m^I^I^I[39;49;00m[37m/* see maybe_call_line_trace[39;49;00m$
   853^I[37m^I^I^I   for expository comments */[39;49;00m[37m[39;49;00m$
   854^I[37m^I^I^I[39;49;00mf->f_stacktop[37m [39;49;00m=[37m [39;49;00mstack_pointer;[37m[39;49;00m$
   855^I[37m[39;49;00m$
   856^I[37m^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00mmaybe_call_line_trace(tstate->c_tracefunc,[37m[39;49;00m$
   857^I[37m^I^I^I^I^I^I    [39;49;00mtstate->c_traceobj,[37m[39;49;00m$
   858^I[37m^I^I^I^I^I^I    [39;49;00mf,[37m [39;49;00m&instr_lb,[37m [39;49;00m&instr_ub,[37m[39;49;00m$
   859^I[37m^I^I^I^I^I^I    [39;49;00m&instr_prev);[37m[39;49;00m$
   860^I[37m^I^I^I[39;49;00m[37m/* Reload possibly changed frame fields */[39;49;00m[37m[39;49;00m$
   861^I[37m^I^I^I[39;49;00mJUMPTO(f->f_lasti);[37m[39;49;00m$
   862^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(f->f_stacktop[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
   863^I[37m^I^I^I^I[39;49;00mstack_pointer[37m [39;49;00m=[37m [39;49;00mf->f_stacktop;[37m[39;49;00m$
   864^I[37m^I^I^I^I[39;49;00mf->f_stacktop[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   865^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
   866^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err)[37m [39;49;00m{[37m[39;49;00m$
   867^I[37m^I^I^I^I[39;49;00m[37m/* trace function raised an exception */[39;49;00m[37m[39;49;00m$
   868^I[37m^I^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mon_error;[37m[39;49;00m$
   869^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
   870^I[37m^I^I[39;49;00m}[37m[39;49;00m$
   871^I[37m[39;49;00m$
   872^I[37m^I^I[39;49;00m[37m/* Extract opcode and argument */[39;49;00m[37m[39;49;00m$
   873^I[37m[39;49;00m$
   874^I[37m^I^I[39;49;00mopcode[37m [39;49;00m=[37m [39;49;00mNEXTOP();[37m[39;49;00m$
   875^I[37m^I^I[39;49;00moparg[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m   [39;49;00m[37m/* allows oparg to be stored in a register because[39;49;00m$
   876^I[37m^I^I^Iit doesn't have to be remembered across a full loop */[39;49;00m[37m[39;49;00m$
   877^I[37m^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(HAS_ARG(opcode))[37m[39;49;00m$
   878^I[37m^I^I^I[39;49;00moparg[37m [39;49;00m=[37m [39;49;00mNEXTARG();[37m[39;49;00m$
   879^I[37m^I  [39;49;00mdispatch_opcode:[37m[39;49;00m$
   880^I[36m#[39;49;00m[36mifdef DYNAMIC_EXECUTION_PROFILE[39;49;00m[36m[39;49;00m$
   881^I[36m#[39;49;00m[36mifdef DXPAIRS[39;49;00m[36m[39;49;00m$
   882^I[37m^I^I[39;49;00mdxpairs[lastopcode][opcode]++;[37m[39;49;00m$
   883^I[37m^I^I[39;49;00mlastopcode[37m [39;49;00m=[37m [39;49;00mopcode;[37m[39;49;00m$
   884^I[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   885^I[37m^I^I[39;49;00mdxp[opcode]++;[37m[39;49;00m$
   886^I[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   887^I[37m[39;49;00m$
   888^I[36m#[39;49;00m[36mifdef LLTRACE[39;49;00m[36m[39;49;00m$
   889^I[37m^I^I[39;49;00m[37m/* Instruction tracing */[39;49;00m[37m[39;49;00m$
   890^I[37m[39;49;00m$
   891^I[37m^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(lltrace)[37m [39;49;00m{[37m[39;49;00m$
   892^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(HAS_ARG(opcode))[37m [39;49;00m{[37m[39;49;00m$
   893^I[37m^I^I^I^I[39;49;00mprintf([33m"[39;49;00m[33m%d: %d, %d[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m,[37m[39;49;00m$
   894^I[37m^I^I^I^I       [39;49;00mf->f_lasti,[37m [39;49;00mopcode,[37m [39;49;00moparg);[37m[39;49;00m$
   895^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
   896^I[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
   897^I[37m^I^I^I^I[39;49;00mprintf([33m"[39;49;00m[33m%d: %d[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m,[37m[39;49;00m$
   898^I[37m^I^I^I^I       [39;49;00mf->f_lasti,[37m [39;49;00mopcode);[37m[39;49;00m$
   899^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
   900^I[37m^I^I[39;49;00m}[37m[39;49;00m$
   901^I[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   902^I[37m[39;49;00m$
   903^I[37m^I^I[39;49;00m[37m/* Main switch on opcode */[39;49;00m[37m[39;49;00m$
   904^I[37m^I^I[39;49;00mREAD_TIMESTAMP(inst0);[37m[39;49;00m$
   905^I[37m[39;49;00m$
   906^I[37m^I^I[39;49;00m[34mswitch[39;49;00m[37m [39;49;00m(opcode)[37m [39;49;00m{[37m[39;49;00m$
   907^I[37m[39;49;00m$
   908^I[37m^I^I[39;49;00m[37m/* BEWARE![39;49;00m$
   909^I[37m^I^I   It is essential that any operation that fails sets either[39;49;00m$
   910^I[37m^I^I   x to NULL, err to nonzero, or why to anything but WHY_NOT,[39;49;00m$
   911^I[37m^I^I   and that no operation that succeeds does this! */[39;49;00m[37m[39;49;00m$
   912^I[37m[39;49;00m$
   913^I[37m^I^I[39;49;00m[37m/* case STOP_CODE: this is an error! */[39;49;00m[37m[39;49;00m$
   914^I[37m[39;49;00m$
   915^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mNOP[39;49;00m:[37m[39;49;00m$
   916^I[37m^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
   917^I[37m[39;49;00m$
   918^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mLOAD_FAST[39;49;00m:[37m[39;49;00m$
   919^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mGETLOCAL(oparg);[37m[39;49;00m$
   920^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
   921^I[37m^I^I^I^I[39;49;00mPy_INCREF(x);[37m[39;49;00m$
   922^I[37m^I^I^I^I[39;49;00mPUSH(x);[37m[39;49;00m$
   923^I[37m^I^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
   924^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
   925^I[37m^I^I^I[39;49;00mformat_exc_check_arg(PyExc_UnboundLocalError,[37m[39;49;00m$
   926^I[37m^I^I^I^I[39;49;00mUNBOUNDLOCAL_ERROR_MSG,[37m[39;49;00m$
   927^I[37m^I^I^I^I[39;49;00mPyTuple_GetItem(co->co_varnames,[37m [39;49;00moparg));[37m[39;49;00m$
   928^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
   929^I[37m[39;49;00m$
   930^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mLOAD_CONST[39;49;00m:[37m[39;49;00m$
   931^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mGETITEM(consts,[37m [39;49;00moparg);[37m[39;49;00m$
   932^I[37m^I^I^I[39;49;00mPy_INCREF(x);[37m[39;49;00m$
   933^I[37m^I^I^I[39;49;00mPUSH(x);[37m[39;49;00m$
   934^I[37m^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
   935^I[37m[39;49;00m$
   936^I[37m^I^I[39;49;00mPREDICTED_WITH_ARG(STORE_FAST);[37m[39;49;00m$
   937^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSTORE_FAST[39;49;00m:[37m[39;49;00m$
   938^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
   939^I[37m^I^I^I[39;49;00mSETLOCAL(oparg,[37m [39;49;00mv);[37m[39;49;00m$
   940^I[37m^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
   941^I[37m[39;49;00m$
   942^I[37m^I^I[39;49;00mPREDICTED(POP_TOP);[37m[39;49;00m$
   943^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mPOP_TOP[39;49;00m:[37m[39;49;00m$
   944^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
   945^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
   946^I[37m^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
   947^I[37m[39;49;00m$
   948^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mROT_TWO[39;49;00m:[37m[39;49;00m$
   949^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
   950^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mSECOND();[37m[39;49;00m$
   951^I[37m^I^I^I[39;49;00mSET_TOP(w);[37m[39;49;00m$
   952^I[37m^I^I^I[39;49;00mSET_SECOND(v);[37m[39;49;00m$
   953^I[37m^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
   954^I[37m[39;49;00m$
   955^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mROT_THREE[39;49;00m:[37m[39;49;00m$
   956^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
   957^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mSECOND();[37m[39;49;00m$
   958^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mTHIRD();[37m[39;49;00m$
   959^I[37m^I^I^I[39;49;00mSET_TOP(w);[37m[39;49;00m$
   960^I[37m^I^I^I[39;49;00mSET_SECOND(x);[37m[39;49;00m$
   961^I[37m^I^I^I[39;49;00mSET_THIRD(v);[37m[39;49;00m$
   962^I[37m^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
   963^I[37m[39;49;00m$
   964^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mROT_FOUR[39;49;00m:[37m[39;49;00m$
   965^I[37m^I^I^I[39;49;00mu[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
   966^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mSECOND();[37m[39;49;00m$
   967^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mTHIRD();[37m[39;49;00m$
   968^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mFOURTH();[37m[39;49;00m$
   969^I[37m^I^I^I[39;49;00mSET_TOP(v);[37m[39;49;00m$
   970^I[37m^I^I^I[39;49;00mSET_SECOND(w);[37m[39;49;00m$
   971^I[37m^I^I^I[39;49;00mSET_THIRD(x);[37m[39;49;00m$
   972^I[37m^I^I^I[39;49;00mSET_FOURTH(u);[37m[39;49;00m$
   973^I[37m^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
   974^I[37m[39;49;00m$
   975^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mDUP_TOP[39;49;00m:[37m[39;49;00m$
   976^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
   977^I[37m^I^I^I[39;49;00mPy_INCREF(v);[37m[39;49;00m$
   978^I[37m^I^I^I[39;49;00mPUSH(v);[37m[39;49;00m$
   979^I[37m^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
   980^I[37m[39;49;00m$
   981^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mDUP_TOPX[39;49;00m:[37m[39;49;00m$
   982^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(oparg[37m [39;49;00m==[37m [39;49;00m[34m2[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
   983^I[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
   984^I[37m^I^I^I^I[39;49;00mPy_INCREF(x);[37m[39;49;00m$
   985^I[37m^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mSECOND();[37m[39;49;00m$
   986^I[37m^I^I^I^I[39;49;00mPy_INCREF(w);[37m[39;49;00m$
   987^I[37m^I^I^I^I[39;49;00mSTACKADJ([34m2[39;49;00m);[37m[39;49;00m$
   988^I[37m^I^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
   989^I[37m^I^I^I^I[39;49;00mSET_SECOND(w);[37m[39;49;00m$
   990^I[37m^I^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
   991^I[37m^I^I^I[39;49;00m}[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(oparg[37m [39;49;00m==[37m [39;49;00m[34m3[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
   992^I[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
   993^I[37m^I^I^I^I[39;49;00mPy_INCREF(x);[37m[39;49;00m$
   994^I[37m^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mSECOND();[37m[39;49;00m$
   995^I[37m^I^I^I^I[39;49;00mPy_INCREF(w);[37m[39;49;00m$
   996^I[37m^I^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTHIRD();[37m[39;49;00m$
   997^I[37m^I^I^I^I[39;49;00mPy_INCREF(v);[37m[39;49;00m$
   998^I[37m^I^I^I^I[39;49;00mSTACKADJ([34m3[39;49;00m);[37m[39;49;00m$
   999^I[37m^I^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1000^I[37m^I^I^I^I[39;49;00mSET_SECOND(w);[37m[39;49;00m$
  1001^I[37m^I^I^I^I[39;49;00mSET_THIRD(v);[37m[39;49;00m$
  1002^I[37m^I^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
  1003^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  1004^I[37m^I^I^I[39;49;00mPy_FatalError([33m"[39;49;00m[33minvalid argument to DUP_TOPX[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1005^I[37m^I^I^I^I      [39;49;00m[33m"[39;49;00m[33m (bytecode corruption?)[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
  1006^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1007^I[37m[39;49;00m$
  1008^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mUNARY_POSITIVE[39;49;00m:[37m[39;49;00m$
  1009^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1010^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_Positive(v);[37m[39;49;00m$
  1011^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1012^I[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1013^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1014^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1015^I[37m[39;49;00m$
  1016^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mUNARY_NEGATIVE[39;49;00m:[37m[39;49;00m$
  1017^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1018^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_Negative(v);[37m[39;49;00m$
  1019^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1020^I[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1021^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1022^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1023^I[37m[39;49;00m$
  1024^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mUNARY_NOT[39;49;00m:[37m[39;49;00m$
  1025^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1026^I[37m^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyObject_IsTrue(v);[37m[39;49;00m$
  1027^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1028^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1029^I[37m^I^I^I^I[39;49;00mPy_INCREF(Py_True);[37m[39;49;00m$
  1030^I[37m^I^I^I^I[39;49;00mSET_TOP(Py_True);[37m[39;49;00m$
  1031^I[37m^I^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1032^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  1033^I[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m>[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1034^I[37m^I^I^I^I[39;49;00mPy_INCREF(Py_False);[37m[39;49;00m$
  1035^I[37m^I^I^I^I[39;49;00mSET_TOP(Py_False);[37m[39;49;00m$
  1036^I[37m^I^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
  1037^I[37m^I^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1038^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  1039^I[37m^I^I^I[39;49;00mSTACKADJ([34m-1[39;49;00m);[37m[39;49;00m$
  1040^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1041^I[37m[39;49;00m$
  1042^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mUNARY_CONVERT[39;49;00m:[37m[39;49;00m$
  1043^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1044^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyObject_Repr(v);[37m[39;49;00m$
  1045^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1046^I[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1047^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1048^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1049^I[37m[39;49;00m$
  1050^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mUNARY_INVERT[39;49;00m:[37m[39;49;00m$
  1051^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1052^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_Invert(v);[37m[39;49;00m$
  1053^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1054^I[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1055^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1056^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1057^I[37m[39;49;00m$
  1058^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBINARY_POWER[39;49;00m:[37m[39;49;00m$
  1059^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1060^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1061^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_Power(v,[37m [39;49;00mw,[37m [39;49;00mPy_None);[37m[39;49;00m$
  1062^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1063^I[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1064^I[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1065^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1066^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1067^I[37m[39;49;00m$
  1068^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBINARY_MULTIPLY[39;49;00m:[37m[39;49;00m$
  1069^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1070^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1071^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_Multiply(v,[37m [39;49;00mw);[37m[39;49;00m$
  1072^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1073^I[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1074^I[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1075^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1076^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1077^I[37m[39;49;00m$
  1078^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBINARY_DIVIDE[39;49;00m:[37m[39;49;00m$
  1079^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(!_Py_QnewFlag)[37m [39;49;00m{[37m[39;49;00m$
  1080^I[37m^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1081^I[37m^I^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1082^I[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_Divide(v,[37m [39;49;00mw);[37m[39;49;00m$
  1083^I[37m^I^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1084^I[37m^I^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1085^I[37m^I^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1086^I[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1087^I[37m^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1088^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  1089^I[37m^I^I^I[39;49;00m[37m/* -Qnew is in effect:^Ifall through to[39;49;00m$
  1090^I[37m^I^I^I   BINARY_TRUE_DIVIDE */[39;49;00m[37m[39;49;00m$
  1091^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBINARY_TRUE_DIVIDE[39;49;00m:[37m[39;49;00m$
  1092^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1093^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1094^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_TrueDivide(v,[37m [39;49;00mw);[37m[39;49;00m$
  1095^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1096^I[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1097^I[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1098^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1099^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1100^I[37m[39;49;00m$
  1101^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBINARY_FLOOR_DIVIDE[39;49;00m:[37m[39;49;00m$
  1102^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1103^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1104^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_FloorDivide(v,[37m [39;49;00mw);[37m[39;49;00m$
  1105^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1106^I[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1107^I[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1108^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1109^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1110^I[37m[39;49;00m$
  1111^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBINARY_MODULO[39;49;00m:[37m[39;49;00m$
  1112^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1113^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1114^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_Remainder(v,[37m [39;49;00mw);[37m[39;49;00m$
  1115^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1116^I[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1117^I[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1118^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1119^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1120^I[37m[39;49;00m$
  1121^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBINARY_ADD[39;49;00m:[37m[39;49;00m$
  1122^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1123^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1124^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyInt_CheckExact(v)[37m [39;49;00m&&[37m [39;49;00mPyInt_CheckExact(w))[37m [39;49;00m{[37m[39;49;00m$
  1125^I[37m^I^I^I^I[39;49;00m[37m/* INLINE: int + int */[39;49;00m[37m[39;49;00m$
  1126^I[37m^I^I^I^I[39;49;00m[34mregister[39;49;00m[37m [39;49;00m[36mlong[39;49;00m[37m [39;49;00ma,[37m [39;49;00mb,[37m [39;49;00mi;[37m[39;49;00m$
  1127^I[37m^I^I^I^I[39;49;00ma[37m [39;49;00m=[37m [39;49;00mPyInt_AS_LONG(v);[37m[39;49;00m$
  1128^I[37m^I^I^I^I[39;49;00mb[37m [39;49;00m=[37m [39;49;00mPyInt_AS_LONG(w);[37m[39;49;00m$
  1129^I[37m^I^I^I^I[39;49;00mi[37m [39;49;00m=[37m [39;49;00ma[37m [39;49;00m+[37m [39;49;00mb;[37m[39;49;00m$
  1130^I[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m((i^a)[37m [39;49;00m<[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m&&[37m [39;49;00m(i^b)[37m [39;49;00m<[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1131^I[37m^I^I^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mslow_add;[37m[39;49;00m$
  1132^I[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyInt_FromLong(i);[37m[39;49;00m$
  1133^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  1134^I[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyString_CheckExact(v)[37m [39;49;00m&&[37m[39;49;00m$
  1135^I[37m^I^I^I^I [39;49;00mPyString_CheckExact(w))[37m [39;49;00m{[37m[39;49;00m$
  1136^I[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mstring_concatenate(v,[37m [39;49;00mw,[37m [39;49;00mf,[37m [39;49;00mnext_instr);[37m[39;49;00m$
  1137^I[37m^I^I^I^I[39;49;00m[37m/* string_concatenate consumed the ref to v */[39;49;00m[37m[39;49;00m$
  1138^I[37m^I^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mskip_decref_vx;[37m[39;49;00m$
  1139^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  1140^I[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
  1141^I[37m^I^I^I  [39;49;00mslow_add:[37m[39;49;00m$
  1142^I[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_Add(v,[37m [39;49;00mw);[37m[39;49;00m$
  1143^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  1144^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1145^I[37m^I^I  [39;49;00mskip_decref_vx:[37m[39;49;00m$
  1146^I[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1147^I[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1148^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1149^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1150^I[37m[39;49;00m$
  1151^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBINARY_SUBTRACT[39;49;00m:[37m[39;49;00m$
  1152^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1153^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1154^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyInt_CheckExact(v)[37m [39;49;00m&&[37m [39;49;00mPyInt_CheckExact(w))[37m [39;49;00m{[37m[39;49;00m$
  1155^I[37m^I^I^I^I[39;49;00m[37m/* INLINE: int - int */[39;49;00m[37m[39;49;00m$
  1156^I[37m^I^I^I^I[39;49;00m[34mregister[39;49;00m[37m [39;49;00m[36mlong[39;49;00m[37m [39;49;00ma,[37m [39;49;00mb,[37m [39;49;00mi;[37m[39;49;00m$
  1157^I[37m^I^I^I^I[39;49;00ma[37m [39;49;00m=[37m [39;49;00mPyInt_AS_LONG(v);[37m[39;49;00m$
  1158^I[37m^I^I^I^I[39;49;00mb[37m [39;49;00m=[37m [39;49;00mPyInt_AS_LONG(w);[37m[39;49;00m$
  1159^I[37m^I^I^I^I[39;49;00mi[37m [39;49;00m=[37m [39;49;00ma[37m [39;49;00m-[37m [39;49;00mb;[37m[39;49;00m$
  1160^I[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m((i^a)[37m [39;49;00m<[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m&&[37m [39;49;00m(i^~b)[37m [39;49;00m<[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1161^I[37m^I^I^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mslow_sub;[37m[39;49;00m$
  1162^I[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyInt_FromLong(i);[37m[39;49;00m$
  1163^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  1164^I[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
  1165^I[37m^I^I^I  [39;49;00mslow_sub:[37m[39;49;00m$
  1166^I[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_Subtract(v,[37m [39;49;00mw);[37m[39;49;00m$
  1167^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  1168^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1169^I[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1170^I[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1171^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1172^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1173^I[37m[39;49;00m$
  1174^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBINARY_SUBSCR[39;49;00m:[37m[39;49;00m$
  1175^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1176^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1177^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyList_CheckExact(v)[37m [39;49;00m&&[37m [39;49;00mPyInt_CheckExact(w))[37m [39;49;00m{[37m[39;49;00m$
  1178^I[37m^I^I^I^I[39;49;00m[37m/* INLINE: list[int] */[39;49;00m[37m[39;49;00m$
  1179^I[37m^I^I^I^I[39;49;00mPy_ssize_t[37m [39;49;00mi[37m [39;49;00m=[37m [39;49;00mPyInt_AsSsize_t(w);[37m[39;49;00m$
  1180^I[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(i[37m [39;49;00m<[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1181^I[37m^I^I^I^I^I[39;49;00mi[37m [39;49;00m+=[37m [39;49;00mPyList_GET_SIZE(v);[37m[39;49;00m$
  1182^I[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(i[37m [39;49;00m>=[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m&&[37m [39;49;00mi[37m [39;49;00m<[37m [39;49;00mPyList_GET_SIZE(v))[37m [39;49;00m{[37m[39;49;00m$
  1183^I[37m^I^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyList_GET_ITEM(v,[37m [39;49;00mi);[37m[39;49;00m$
  1184^I[37m^I^I^I^I^I[39;49;00mPy_INCREF(x);[37m[39;49;00m$
  1185^I[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
  1186^I[37m^I^I^I^I[39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  1187^I[37m^I^I^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mslow_get;[37m[39;49;00m$
  1188^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  1189^I[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  1190^I[37m^I^I^I  [39;49;00mslow_get:[37m[39;49;00m$
  1191^I[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyObject_GetItem(v,[37m [39;49;00mw);[37m[39;49;00m$
  1192^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1193^I[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1194^I[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1195^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1196^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1197^I[37m[39;49;00m$
  1198^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBINARY_LSHIFT[39;49;00m:[37m[39;49;00m$
  1199^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1200^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1201^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_Lshift(v,[37m [39;49;00mw);[37m[39;49;00m$
  1202^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1203^I[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1204^I[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1205^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1206^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1207^I[37m[39;49;00m$
  1208^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBINARY_RSHIFT[39;49;00m:[37m[39;49;00m$
  1209^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1210^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1211^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_Rshift(v,[37m [39;49;00mw);[37m[39;49;00m$
  1212^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1213^I[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1214^I[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1215^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1216^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1217^I[37m[39;49;00m$
  1218^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBINARY_AND[39;49;00m:[37m[39;49;00m$
  1219^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1220^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1221^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_And(v,[37m [39;49;00mw);[37m[39;49;00m$
  1222^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1223^I[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1224^I[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1225^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1226^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1227^I[37m[39;49;00m$
  1228^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBINARY_XOR[39;49;00m:[37m[39;49;00m$
  1229^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1230^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1231^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_Xor(v,[37m [39;49;00mw);[37m[39;49;00m$
  1232^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1233^I[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1234^I[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1235^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1236^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1237^I[37m[39;49;00m$
  1238^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBINARY_OR[39;49;00m:[37m[39;49;00m$
  1239^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1240^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1241^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_Or(v,[37m [39;49;00mw);[37m[39;49;00m$
  1242^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1243^I[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1244^I[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1245^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1246^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1247^I[37m[39;49;00m$
  1248^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mLIST_APPEND[39;49;00m:[37m[39;49;00m$
  1249^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1250^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1251^I[37m^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyList_Append(v,[37m [39;49;00mw);[37m[39;49;00m$
  1252^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1253^I[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1254^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1255^I[37m^I^I^I^I[39;49;00mPREDICT(JUMP_ABSOLUTE);[37m[39;49;00m$
  1256^I[37m^I^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1257^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  1258^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1259^I[37m[39;49;00m$
  1260^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mINPLACE_POWER[39;49;00m:[37m[39;49;00m$
  1261^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1262^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1263^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_InPlacePower(v,[37m [39;49;00mw,[37m [39;49;00mPy_None);[37m[39;49;00m$
  1264^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1265^I[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1266^I[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1267^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1268^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1269^I[37m[39;49;00m$
  1270^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mINPLACE_MULTIPLY[39;49;00m:[37m[39;49;00m$
  1271^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1272^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1273^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_InPlaceMultiply(v,[37m [39;49;00mw);[37m[39;49;00m$
  1274^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1275^I[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1276^I[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1277^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1278^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1279^I[37m[39;49;00m$
  1280^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mINPLACE_DIVIDE[39;49;00m:[37m[39;49;00m$
  1281^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(!_Py_QnewFlag)[37m [39;49;00m{[37m[39;49;00m$
  1282^I[37m^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1283^I[37m^I^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1284^I[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_InPlaceDivide(v,[37m [39;49;00mw);[37m[39;49;00m$
  1285^I[37m^I^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1286^I[37m^I^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1287^I[37m^I^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1288^I[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1289^I[37m^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1290^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  1291^I[37m^I^I^I[39;49;00m[37m/* -Qnew is in effect:^Ifall through to[39;49;00m$
  1292^I[37m^I^I^I   INPLACE_TRUE_DIVIDE */[39;49;00m[37m[39;49;00m$
  1293^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mINPLACE_TRUE_DIVIDE[39;49;00m:[37m[39;49;00m$
  1294^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1295^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1296^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_InPlaceTrueDivide(v,[37m [39;49;00mw);[37m[39;49;00m$
  1297^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1298^I[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1299^I[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1300^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1301^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1302^I[37m[39;49;00m$
  1303^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mINPLACE_FLOOR_DIVIDE[39;49;00m:[37m[39;49;00m$
  1304^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1305^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1306^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_InPlaceFloorDivide(v,[37m [39;49;00mw);[37m[39;49;00m$
  1307^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1308^I[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1309^I[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1310^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1311^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1312^I[37m[39;49;00m$
  1313^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mINPLACE_MODULO[39;49;00m:[37m[39;49;00m$
  1314^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1315^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1316^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_InPlaceRemainder(v,[37m [39;49;00mw);[37m[39;49;00m$
  1317^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1318^I[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1319^I[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1320^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1321^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1322^I[37m[39;49;00m$
  1323^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mINPLACE_ADD[39;49;00m:[37m[39;49;00m$
  1324^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1325^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1326^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyInt_CheckExact(v)[37m [39;49;00m&&[37m [39;49;00mPyInt_CheckExact(w))[37m [39;49;00m{[37m[39;49;00m$
  1327^I[37m^I^I^I^I[39;49;00m[37m/* INLINE: int + int */[39;49;00m[37m[39;49;00m$
  1328^I[37m^I^I^I^I[39;49;00m[34mregister[39;49;00m[37m [39;49;00m[36mlong[39;49;00m[37m [39;49;00ma,[37m [39;49;00mb,[37m [39;49;00mi;[37m[39;49;00m$
  1329^I[37m^I^I^I^I[39;49;00ma[37m [39;49;00m=[37m [39;49;00mPyInt_AS_LONG(v);[37m[39;49;00m$
  1330^I[37m^I^I^I^I[39;49;00mb[37m [39;49;00m=[37m [39;49;00mPyInt_AS_LONG(w);[37m[39;49;00m$
  1331^I[37m^I^I^I^I[39;49;00mi[37m [39;49;00m=[37m [39;49;00ma[37m [39;49;00m+[37m [39;49;00mb;[37m[39;49;00m$
  1332^I[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m((i^a)[37m [39;49;00m<[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m&&[37m [39;49;00m(i^b)[37m [39;49;00m<[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1333^I[37m^I^I^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mslow_iadd;[37m[39;49;00m$
  1334^I[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyInt_FromLong(i);[37m[39;49;00m$
  1335^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  1336^I[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyString_CheckExact(v)[37m [39;49;00m&&[37m[39;49;00m$
  1337^I[37m^I^I^I^I [39;49;00mPyString_CheckExact(w))[37m [39;49;00m{[37m[39;49;00m$
  1338^I[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mstring_concatenate(v,[37m [39;49;00mw,[37m [39;49;00mf,[37m [39;49;00mnext_instr);[37m[39;49;00m$
  1339^I[37m^I^I^I^I[39;49;00m[37m/* string_concatenate consumed the ref to v */[39;49;00m[37m[39;49;00m$
  1340^I[37m^I^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mskip_decref_v;[37m[39;49;00m$
  1341^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  1342^I[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
  1343^I[37m^I^I^I  [39;49;00mslow_iadd:[37m[39;49;00m$
  1344^I[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_InPlaceAdd(v,[37m [39;49;00mw);[37m[39;49;00m$
  1345^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  1346^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1347^I[37m^I^I  [39;49;00mskip_decref_v:[37m[39;49;00m$
  1348^I[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1349^I[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1350^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1351^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1352^I[37m[39;49;00m$
  1353^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mINPLACE_SUBTRACT[39;49;00m:[37m[39;49;00m$
  1354^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1355^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1356^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyInt_CheckExact(v)[37m [39;49;00m&&[37m [39;49;00mPyInt_CheckExact(w))[37m [39;49;00m{[37m[39;49;00m$
  1357^I[37m^I^I^I^I[39;49;00m[37m/* INLINE: int - int */[39;49;00m[37m[39;49;00m$
  1358^I[37m^I^I^I^I[39;49;00m[34mregister[39;49;00m[37m [39;49;00m[36mlong[39;49;00m[37m [39;49;00ma,[37m [39;49;00mb,[37m [39;49;00mi;[37m[39;49;00m$
  1359^I[37m^I^I^I^I[39;49;00ma[37m [39;49;00m=[37m [39;49;00mPyInt_AS_LONG(v);[37m[39;49;00m$
  1360^I[37m^I^I^I^I[39;49;00mb[37m [39;49;00m=[37m [39;49;00mPyInt_AS_LONG(w);[37m[39;49;00m$
  1361^I[37m^I^I^I^I[39;49;00mi[37m [39;49;00m=[37m [39;49;00ma[37m [39;49;00m-[37m [39;49;00mb;[37m[39;49;00m$
  1362^I[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m((i^a)[37m [39;49;00m<[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m&&[37m [39;49;00m(i^~b)[37m [39;49;00m<[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1363^I[37m^I^I^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mslow_isub;[37m[39;49;00m$
  1364^I[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyInt_FromLong(i);[37m[39;49;00m$
  1365^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  1366^I[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
  1367^I[37m^I^I^I  [39;49;00mslow_isub:[37m[39;49;00m$
  1368^I[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_InPlaceSubtract(v,[37m [39;49;00mw);[37m[39;49;00m$
  1369^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  1370^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1371^I[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1372^I[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1373^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1374^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1375^I[37m[39;49;00m$
  1376^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mINPLACE_LSHIFT[39;49;00m:[37m[39;49;00m$
  1377^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1378^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1379^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_InPlaceLshift(v,[37m [39;49;00mw);[37m[39;49;00m$
  1380^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1381^I[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1382^I[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1383^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1384^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1385^I[37m[39;49;00m$
  1386^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mINPLACE_RSHIFT[39;49;00m:[37m[39;49;00m$
  1387^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1388^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1389^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_InPlaceRshift(v,[37m [39;49;00mw);[37m[39;49;00m$
  1390^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1391^I[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1392^I[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1393^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1394^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1395^I[37m[39;49;00m$
  1396^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mINPLACE_AND[39;49;00m:[37m[39;49;00m$
  1397^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1398^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1399^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_InPlaceAnd(v,[37m [39;49;00mw);[37m[39;49;00m$
  1400^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1401^I[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1402^I[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1403^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1404^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1405^I[37m[39;49;00m$
  1406^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mINPLACE_XOR[39;49;00m:[37m[39;49;00m$
  1407^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1408^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1409^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_InPlaceXor(v,[37m [39;49;00mw);[37m[39;49;00m$
  1410^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1411^I[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1412^I[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1413^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1414^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1415^I[37m[39;49;00m$
  1416^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mINPLACE_OR[39;49;00m:[37m[39;49;00m$
  1417^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1418^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1419^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_InPlaceOr(v,[37m [39;49;00mw);[37m[39;49;00m$
  1420^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1421^I[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1422^I[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1423^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1424^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1425^I[37m[39;49;00m$
  1426^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSLICE[39;49;00m+[34m0[39;49;00m:[37m[39;49;00m$
  1427^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSLICE[39;49;00m+[34m1[39;49;00m:[37m[39;49;00m$
  1428^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSLICE[39;49;00m+[34m2[39;49;00m:[37m[39;49;00m$
  1429^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSLICE[39;49;00m+[34m3[39;49;00m:[37m[39;49;00m$
  1430^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m((opcode-SLICE)[37m [39;49;00m&[37m [39;49;00m[34m2[39;49;00m)[37m[39;49;00m$
  1431^I[37m^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1432^I[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  1433^I[37m^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  1434^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m((opcode-SLICE)[37m [39;49;00m&[37m [39;49;00m[34m1[39;49;00m)[37m[39;49;00m$
  1435^I[37m^I^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1436^I[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  1437^I[37m^I^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  1438^I[37m^I^I^I[39;49;00mu[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1439^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mapply_slice(u,[37m [39;49;00mv,[37m [39;49;00mw);[37m[39;49;00m$
  1440^I[37m^I^I^I[39;49;00mPy_DECREF(u);[37m[39;49;00m$
  1441^I[37m^I^I^I[39;49;00mPy_XDECREF(v);[37m[39;49;00m$
  1442^I[37m^I^I^I[39;49;00mPy_XDECREF(w);[37m[39;49;00m$
  1443^I[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1444^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1445^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1446^I[37m[39;49;00m$
  1447^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSTORE_SLICE[39;49;00m+[34m0[39;49;00m:[37m[39;49;00m$
  1448^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSTORE_SLICE[39;49;00m+[34m1[39;49;00m:[37m[39;49;00m$
  1449^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSTORE_SLICE[39;49;00m+[34m2[39;49;00m:[37m[39;49;00m$
  1450^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSTORE_SLICE[39;49;00m+[34m3[39;49;00m:[37m[39;49;00m$
  1451^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m((opcode-STORE_SLICE)[37m [39;49;00m&[37m [39;49;00m[34m2[39;49;00m)[37m[39;49;00m$
  1452^I[37m^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1453^I[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  1454^I[37m^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  1455^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m((opcode-STORE_SLICE)[37m [39;49;00m&[37m [39;49;00m[34m1[39;49;00m)[37m[39;49;00m$
  1456^I[37m^I^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1457^I[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  1458^I[37m^I^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  1459^I[37m^I^I^I[39;49;00mu[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1460^I[37m^I^I^I[39;49;00mt[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1461^I[37m^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00massign_slice(u,[37m [39;49;00mv,[37m [39;49;00mw,[37m [39;49;00mt);[37m [39;49;00m[37m/* u[v:w] = t */[39;49;00m[37m[39;49;00m$
  1462^I[37m^I^I^I[39;49;00mPy_DECREF(t);[37m[39;49;00m$
  1463^I[37m^I^I^I[39;49;00mPy_DECREF(u);[37m[39;49;00m$
  1464^I[37m^I^I^I[39;49;00mPy_XDECREF(v);[37m[39;49;00m$
  1465^I[37m^I^I^I[39;49;00mPy_XDECREF(w);[37m[39;49;00m$
  1466^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1467^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1468^I[37m[39;49;00m$
  1469^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mDELETE_SLICE[39;49;00m+[34m0[39;49;00m:[37m[39;49;00m$
  1470^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mDELETE_SLICE[39;49;00m+[34m1[39;49;00m:[37m[39;49;00m$
  1471^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mDELETE_SLICE[39;49;00m+[34m2[39;49;00m:[37m[39;49;00m$
  1472^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mDELETE_SLICE[39;49;00m+[34m3[39;49;00m:[37m[39;49;00m$
  1473^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m((opcode-DELETE_SLICE)[37m [39;49;00m&[37m [39;49;00m[34m2[39;49;00m)[37m[39;49;00m$
  1474^I[37m^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1475^I[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  1476^I[37m^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  1477^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m((opcode-DELETE_SLICE)[37m [39;49;00m&[37m [39;49;00m[34m1[39;49;00m)[37m[39;49;00m$
  1478^I[37m^I^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1479^I[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  1480^I[37m^I^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  1481^I[37m^I^I^I[39;49;00mu[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1482^I[37m^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00massign_slice(u,[37m [39;49;00mv,[37m [39;49;00mw,[37m [39;49;00m(PyObject[37m [39;49;00m*)[36mNULL[39;49;00m);[37m[39;49;00m$
  1483^I[37m^I^I^I^I^I^I^I[39;49;00m[37m/* del u[v:w] */[39;49;00m[37m[39;49;00m$
  1484^I[37m^I^I^I[39;49;00mPy_DECREF(u);[37m[39;49;00m$
  1485^I[37m^I^I^I[39;49;00mPy_XDECREF(v);[37m[39;49;00m$
  1486^I[37m^I^I^I[39;49;00mPy_XDECREF(w);[37m[39;49;00m$
  1487^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1488^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1489^I[37m[39;49;00m$
  1490^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSTORE_SUBSCR[39;49;00m:[37m[39;49;00m$
  1491^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1492^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mSECOND();[37m[39;49;00m$
  1493^I[37m^I^I^I[39;49;00mu[37m [39;49;00m=[37m [39;49;00mTHIRD();[37m[39;49;00m$
  1494^I[37m^I^I^I[39;49;00mSTACKADJ([34m-3[39;49;00m);[37m[39;49;00m$
  1495^I[37m^I^I^I[39;49;00m[37m/* v[w] = u */[39;49;00m[37m[39;49;00m$
  1496^I[37m^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyObject_SetItem(v,[37m [39;49;00mw,[37m [39;49;00mu);[37m[39;49;00m$
  1497^I[37m^I^I^I[39;49;00mPy_DECREF(u);[37m[39;49;00m$
  1498^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1499^I[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1500^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1501^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1502^I[37m[39;49;00m$
  1503^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mDELETE_SUBSCR[39;49;00m:[37m[39;49;00m$
  1504^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1505^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mSECOND();[37m[39;49;00m$
  1506^I[37m^I^I^I[39;49;00mSTACKADJ([34m-2[39;49;00m);[37m[39;49;00m$
  1507^I[37m^I^I^I[39;49;00m[37m/* del v[w] */[39;49;00m[37m[39;49;00m$
  1508^I[37m^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyObject_DelItem(v,[37m [39;49;00mw);[37m[39;49;00m$
  1509^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1510^I[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1511^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1512^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1513^I[37m[39;49;00m$
  1514^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mPRINT_EXPR[39;49;00m:[37m[39;49;00m$
  1515^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1516^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPySys_GetObject([33m"[39;49;00m[33mdisplayhook[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
  1517^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(w[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1518^I[37m^I^I^I^I[39;49;00mPyErr_SetString(PyExc_RuntimeError,[37m[39;49;00m$
  1519^I[37m^I^I^I^I^I^I[39;49;00m[33m"[39;49;00m[33mlost sys.displayhook[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
  1520^I[37m^I^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00m[34m-1[39;49;00m;[37m[39;49;00m$
  1521^I[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  1522^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  1523^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1524^I[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyTuple_Pack([34m1[39;49;00m,[37m [39;49;00mv);[37m[39;49;00m$
  1525^I[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
  1526^I[37m^I^I^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00m[34m-1[39;49;00m;[37m[39;49;00m$
  1527^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  1528^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1529^I[37m^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPyEval_CallObject(w,[37m [39;49;00mx);[37m[39;49;00m$
  1530^I[37m^I^I^I^I[39;49;00mPy_XDECREF(w);[37m[39;49;00m$
  1531^I[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(w[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
  1532^I[37m^I^I^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00m[34m-1[39;49;00m;[37m[39;49;00m$
  1533^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  1534^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1535^I[37m^I^I^I[39;49;00mPy_XDECREF(x);[37m[39;49;00m$
  1536^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1537^I[37m[39;49;00m$
  1538^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mPRINT_ITEM_TO[39;49;00m:[37m[39;49;00m$
  1539^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mstream[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1540^I[37m^I^I^I[39;49;00m[37m/* fall through to PRINT_ITEM */[39;49;00m[37m[39;49;00m$
  1541^I[37m[39;49;00m$
  1542^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mPRINT_ITEM[39;49;00m:[37m[39;49;00m$
  1543^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1544^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(stream[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m[37m [39;49;00m||[37m [39;49;00mstream[37m [39;49;00m==[37m [39;49;00mPy_None)[37m [39;49;00m{[37m[39;49;00m$
  1545^I[37m^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPySys_GetObject([33m"[39;49;00m[33mstdout[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
  1546^I[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(w[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1547^I[37m^I^I^I^I^I[39;49;00mPyErr_SetString(PyExc_RuntimeError,[37m[39;49;00m$
  1548^I[37m^I^I^I^I^I^I^I[39;49;00m[33m"[39;49;00m[33mlost sys.stdout[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
  1549^I[37m^I^I^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00m[34m-1[39;49;00m;[37m[39;49;00m$
  1550^I[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
  1551^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  1552^I[37m^I^I^I[39;49;00m[37m/* PyFile_SoftSpace() can exececute arbitrary code[39;49;00m$
  1553^I[37m^I^I^I   if sys.stdout is an instance with a __getattr__.[39;49;00m$
  1554^I[37m^I^I^I   If __getattr__ raises an exception, w will[39;49;00m$
  1555^I[37m^I^I^I   be freed, so we need to prevent that temporarily. */[39;49;00m[37m[39;49;00m$
  1556^I[37m^I^I^I[39;49;00mPy_XINCREF(w);[37m[39;49;00m$
  1557^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(w[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m[37m [39;49;00m&&[37m [39;49;00mPyFile_SoftSpace(w,[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m$
  1558^I[37m^I^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyFile_WriteString([33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m,[37m [39;49;00mw);[37m[39;49;00m$
  1559^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1560^I[37m^I^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyFile_WriteObject(v,[37m [39;49;00mw,[37m [39;49;00mPy_PRINT_RAW);[37m[39;49;00m$
  1561^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1562^I[37m^I^I^I    [39;49;00m[37m/* XXX move into writeobject() ? */[39;49;00m[37m[39;49;00m$
  1563^I[37m^I^I^I    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyString_Check(v))[37m [39;49;00m{[37m[39;49;00m$
  1564^I[37m^I^I^I^I[39;49;00m[36mchar[39;49;00m[37m [39;49;00m*s[37m [39;49;00m=[37m [39;49;00mPyString_AS_STRING(v);[37m[39;49;00m$
  1565^I[37m^I^I^I^I[39;49;00mPy_ssize_t[37m [39;49;00mlen[37m [39;49;00m=[37m [39;49;00mPyString_GET_SIZE(v);[37m[39;49;00m$
  1566^I[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(len[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m||[37m[39;49;00m$
  1567^I[37m^I^I^I^I    [39;49;00m!isspace(Py_CHARMASK(s[len[34m-1[39;49;00m]))[37m [39;49;00m||[37m[39;49;00m$
  1568^I[37m^I^I^I^I    [39;49;00ms[len[34m-1[39;49;00m][37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
  1569^I[37m^I^I^I^I^I[39;49;00mPyFile_SoftSpace(w,[37m [39;49;00m[34m1[39;49;00m);[37m[39;49;00m$
  1570^I[37m^I^I^I    [39;49;00m}[37m[39;49;00m$
  1571^I[36m#[39;49;00m[36mifdef Py_USING_UNICODE[39;49;00m[36m[39;49;00m$
  1572^I[37m^I^I^I    [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyUnicode_Check(v))[37m [39;49;00m{[37m[39;49;00m$
  1573^I[37m^I^I^I^I[39;49;00mPy_UNICODE[37m [39;49;00m*s[37m [39;49;00m=[37m [39;49;00mPyUnicode_AS_UNICODE(v);[37m[39;49;00m$
  1574^I[37m^I^I^I^I[39;49;00mPy_ssize_t[37m [39;49;00mlen[37m [39;49;00m=[37m [39;49;00mPyUnicode_GET_SIZE(v);[37m[39;49;00m$
  1575^I[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(len[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m||[37m[39;49;00m$
  1576^I[37m^I^I^I^I    [39;49;00m!Py_UNICODE_ISSPACE(s[len[34m-1[39;49;00m])[37m [39;49;00m||[37m[39;49;00m$
  1577^I[37m^I^I^I^I    [39;49;00ms[len[34m-1[39;49;00m][37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
  1578^I[37m^I^I^I^I    [39;49;00mPyFile_SoftSpace(w,[37m [39;49;00m[34m1[39;49;00m);[37m[39;49;00m$
  1579^I[37m^I^I^I    [39;49;00m}[37m[39;49;00m$
  1580^I[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
  1581^I[37m^I^I^I    [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  1582^I[37m^I^I^I    ^I[39;49;00mPyFile_SoftSpace(w,[37m [39;49;00m[34m1[39;49;00m);[37m[39;49;00m$
  1583^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  1584^I[37m^I^I^I[39;49;00mPy_XDECREF(w);[37m[39;49;00m$
  1585^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1586^I[37m^I^I^I[39;49;00mPy_XDECREF(stream);[37m[39;49;00m$
  1587^I[37m^I^I^I[39;49;00mstream[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  1588^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1589^I[37m^I^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1590^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1591^I[37m[39;49;00m$
  1592^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mPRINT_NEWLINE_TO[39;49;00m:[37m[39;49;00m$
  1593^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mstream[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1594^I[37m^I^I^I[39;49;00m[37m/* fall through to PRINT_NEWLINE */[39;49;00m[37m[39;49;00m$
  1595^I[37m[39;49;00m$
  1596^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mPRINT_NEWLINE[39;49;00m:[37m[39;49;00m$
  1597^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(stream[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m[37m [39;49;00m||[37m [39;49;00mstream[37m [39;49;00m==[37m [39;49;00mPy_None)[37m [39;49;00m{[37m[39;49;00m$
  1598^I[37m^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPySys_GetObject([33m"[39;49;00m[33mstdout[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
  1599^I[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(w[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
  1600^I[37m^I^I^I^I^I[39;49;00mPyErr_SetString(PyExc_RuntimeError,[37m[39;49;00m$
  1601^I[37m^I^I^I^I^I^I^I[39;49;00m[33m"[39;49;00m[33mlost sys.stdout[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
  1602^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  1603^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(w[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1604^I[37m^I^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyFile_WriteString([33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m,[37m [39;49;00mw);[37m[39;49;00m$
  1605^I[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1606^I[37m^I^I^I^I^I[39;49;00mPyFile_SoftSpace(w,[37m [39;49;00m[34m0[39;49;00m);[37m[39;49;00m$
  1607^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  1608^I[37m^I^I^I[39;49;00mPy_XDECREF(stream);[37m[39;49;00m$
  1609^I[37m^I^I^I[39;49;00mstream[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  1610^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1611^I[37m[39;49;00m$
  1612^I[37m[39;49;00m$
  1613^I[36m#[39;49;00m[36mifdef CASE_TOO_BIG[39;49;00m[36m[39;49;00m$
  1614^I[37m^I^I[39;49;00m[34mdefault[39;49;00m:[37m [39;49;00m[34mswitch[39;49;00m[37m [39;49;00m(opcode)[37m [39;49;00m{[37m[39;49;00m$
  1615^I[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
  1616^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mRAISE_VARARGS[39;49;00m:[37m[39;49;00m$
  1617^I[37m^I^I^I[39;49;00mu[37m [39;49;00m=[37m [39;49;00mv[37m [39;49;00m=[37m [39;49;00mw[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  1618^I[37m^I^I^I[39;49;00m[34mswitch[39;49;00m[37m [39;49;00m(oparg)[37m [39;49;00m{[37m[39;49;00m$
  1619^I[37m^I^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[34m3[39;49;00m:[37m[39;49;00m$
  1620^I[37m^I^I^I^I[39;49;00mu[37m [39;49;00m=[37m [39;49;00mPOP();[37m [39;49;00m[37m/* traceback */[39;49;00m[37m[39;49;00m$
  1621^I[37m^I^I^I^I[39;49;00m[37m/* Fallthrough */[39;49;00m[37m[39;49;00m$
  1622^I[37m^I^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[34m2[39;49;00m:[37m[39;49;00m$
  1623^I[37m^I^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m [39;49;00m[37m/* value */[39;49;00m[37m[39;49;00m$
  1624^I[37m^I^I^I^I[39;49;00m[37m/* Fallthrough */[39;49;00m[37m[39;49;00m$
  1625^I[37m^I^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[34m1[39;49;00m:[37m[39;49;00m$
  1626^I[37m^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m [39;49;00m[37m/* exc */[39;49;00m[37m[39;49;00m$
  1627^I[37m^I^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[34m0[39;49;00m:[37m [39;49;00m[37m/* Fallthrough */[39;49;00m[37m[39;49;00m$
  1628^I[37m^I^I^I^I[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mdo_raise(w,[37m [39;49;00mv,[37m [39;49;00mu);[37m[39;49;00m$
  1629^I[37m^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1630^I[37m^I^I^I[39;49;00m[34mdefault[39;49;00m:[37m[39;49;00m$
  1631^I[37m^I^I^I^I[39;49;00mPyErr_SetString(PyExc_SystemError,[37m[39;49;00m$
  1632^I[37m^I^I^I^I^I   [39;49;00m[33m"[39;49;00m[33mbad RAISE_VARARGS oparg[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
  1633^I[37m^I^I^I^I[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_EXCEPTION;[37m[39;49;00m$
  1634^I[37m^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1635^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  1636^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1637^I[37m[39;49;00m$
  1638^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mLOAD_LOCALS[39;49;00m:[37m[39;49;00m$
  1639^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m((x[37m [39;49;00m=[37m [39;49;00mf->f_locals)[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1640^I[37m^I^I^I^I[39;49;00mPy_INCREF(x);[37m[39;49;00m$
  1641^I[37m^I^I^I^I[39;49;00mPUSH(x);[37m[39;49;00m$
  1642^I[37m^I^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1643^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  1644^I[37m^I^I^I[39;49;00mPyErr_SetString(PyExc_SystemError,[37m [39;49;00m[33m"[39;49;00m[33mno locals[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
  1645^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1646^I[37m[39;49;00m$
  1647^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mRETURN_VALUE[39;49;00m:[37m[39;49;00m$
  1648^I[37m^I^I^I[39;49;00mretval[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1649^I[37m^I^I^I[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_RETURN;[37m[39;49;00m$
  1650^I[37m^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_block_end;[37m[39;49;00m$
  1651^I[37m[39;49;00m$
  1652^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mYIELD_VALUE[39;49;00m:[37m[39;49;00m$
  1653^I[37m^I^I^I[39;49;00mretval[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1654^I[37m^I^I^I[39;49;00mf->f_stacktop[37m [39;49;00m=[37m [39;49;00mstack_pointer;[37m[39;49;00m$
  1655^I[37m^I^I^I[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_YIELD;[37m[39;49;00m$
  1656^I[37m^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_yield;[37m[39;49;00m$
  1657^I[37m[39;49;00m$
  1658^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mEXEC_STMT[39;49;00m:[37m[39;49;00m$
  1659^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1660^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mSECOND();[37m[39;49;00m$
  1661^I[37m^I^I^I[39;49;00mu[37m [39;49;00m=[37m [39;49;00mTHIRD();[37m[39;49;00m$
  1662^I[37m^I^I^I[39;49;00mSTACKADJ([34m-3[39;49;00m);[37m[39;49;00m$
  1663^I[37m^I^I^I[39;49;00mREAD_TIMESTAMP(intr0);[37m[39;49;00m$
  1664^I[37m^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00mexec_statement(f,[37m [39;49;00mu,[37m [39;49;00mv,[37m [39;49;00mw);[37m[39;49;00m$
  1665^I[37m^I^I^I[39;49;00mREAD_TIMESTAMP(intr1);[37m[39;49;00m$
  1666^I[37m^I^I^I[39;49;00mPy_DECREF(u);[37m[39;49;00m$
  1667^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1668^I[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1669^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1670^I[37m[39;49;00m$
  1671^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mPOP_BLOCK[39;49;00m:[37m[39;49;00m$
  1672^I[37m^I^I^I[39;49;00m{[37m[39;49;00m$
  1673^I[37m^I^I^I^I[39;49;00mPyTryBlock[37m [39;49;00m*b[37m [39;49;00m=[37m [39;49;00mPyFrame_BlockPop(f);[37m[39;49;00m$
  1674^I[37m^I^I^I^I[39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(STACK_LEVEL()[37m [39;49;00m>[37m [39;49;00mb->b_level)[37m [39;49;00m{[37m[39;49;00m$
  1675^I[37m^I^I^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1676^I[37m^I^I^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1677^I[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
  1678^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  1679^I[37m^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1680^I[37m[39;49;00m$
  1681^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mEND_FINALLY[39;49;00m:[37m[39;49;00m$
  1682^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1683^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyInt_Check(v))[37m [39;49;00m{[37m[39;49;00m$
  1684^I[37m^I^I^I^I[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00m([34menum[39;49;00m[37m [39;49;00mwhy_code)[37m [39;49;00mPyInt_AS_LONG(v);[37m[39;49;00m$
  1685^I[37m^I^I^I^I[39;49;00massert(why[37m [39;49;00m!=[37m [39;49;00mWHY_YIELD);[37m[39;49;00m$
  1686^I[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(why[37m [39;49;00m==[37m [39;49;00mWHY_RETURN[37m [39;49;00m||[37m[39;49;00m$
  1687^I[37m^I^I^I^I    [39;49;00mwhy[37m [39;49;00m==[37m [39;49;00mWHY_CONTINUE)[37m[39;49;00m$
  1688^I[37m^I^I^I^I^I[39;49;00mretval[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1689^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  1690^I[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyExceptionClass_Check(v)[37m [39;49;00m||[37m [39;49;00mPyString_Check(v))[37m [39;49;00m{[37m[39;49;00m$
  1691^I[37m^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1692^I[37m^I^I^I^I[39;49;00mu[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1693^I[37m^I^I^I^I[39;49;00mPyErr_Restore(v,[37m [39;49;00mw,[37m [39;49;00mu);[37m[39;49;00m$
  1694^I[37m^I^I^I^I[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_RERAISE;[37m[39;49;00m$
  1695^I[37m^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1696^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  1697^I[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(v[37m [39;49;00m!=[37m [39;49;00mPy_None)[37m [39;49;00m{[37m[39;49;00m$
  1698^I[37m^I^I^I^I[39;49;00mPyErr_SetString(PyExc_SystemError,[37m[39;49;00m$
  1699^I[37m^I^I^I^I^I[39;49;00m[33m"[39;49;00m[33m'finally' pops bad exception[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
  1700^I[37m^I^I^I^I[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_EXCEPTION;[37m[39;49;00m$
  1701^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  1702^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1703^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1704^I[37m[39;49;00m$
  1705^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBUILD_CLASS[39;49;00m:[37m[39;49;00m$
  1706^I[37m^I^I^I[39;49;00mu[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1707^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mSECOND();[37m[39;49;00m$
  1708^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mTHIRD();[37m[39;49;00m$
  1709^I[37m^I^I^I[39;49;00mSTACKADJ([34m-2[39;49;00m);[37m[39;49;00m$
  1710^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mbuild_class(u,[37m [39;49;00mv,[37m [39;49;00mw);[37m[39;49;00m$
  1711^I[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1712^I[37m^I^I^I[39;49;00mPy_DECREF(u);[37m[39;49;00m$
  1713^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1714^I[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1715^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1716^I[37m[39;49;00m$
  1717^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSTORE_NAME[39;49;00m:[37m[39;49;00m$
  1718^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mGETITEM(names,[37m [39;49;00moparg);[37m[39;49;00m$
  1719^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1720^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m((x[37m [39;49;00m=[37m [39;49;00mf->f_locals)[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1721^I[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyDict_CheckExact(x))[37m[39;49;00m$
  1722^I[37m^I^I^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyDict_SetItem(x,[37m [39;49;00mw,[37m [39;49;00mv);[37m[39;49;00m$
  1723^I[37m^I^I^I^I[39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  1724^I[37m^I^I^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyObject_SetItem(x,[37m [39;49;00mw,[37m [39;49;00mv);[37m[39;49;00m$
  1725^I[37m^I^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1726^I[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1727^I[37m^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1728^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  1729^I[37m^I^I^I[39;49;00mPyErr_Format(PyExc_SystemError,[37m[39;49;00m$
  1730^I[37m^I^I^I^I     [39;49;00m[33m"[39;49;00m[33mno locals found when storing %s[39;49;00m[33m"[39;49;00m,[37m[39;49;00m$
  1731^I[37m^I^I^I^I     [39;49;00mPyObject_REPR(w));[37m[39;49;00m$
  1732^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1733^I[37m[39;49;00m$
  1734^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mDELETE_NAME[39;49;00m:[37m[39;49;00m$
  1735^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mGETITEM(names,[37m [39;49;00moparg);[37m[39;49;00m$
  1736^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m((x[37m [39;49;00m=[37m [39;49;00mf->f_locals)[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1737^I[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m((err[37m [39;49;00m=[37m [39;49;00mPyObject_DelItem(x,[37m [39;49;00mw))[37m [39;49;00m!=[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1738^I[37m^I^I^I^I^I[39;49;00mformat_exc_check_arg(PyExc_NameError,[37m[39;49;00m$
  1739^I[37m^I^I^I^I^I^I^I^I[39;49;00mNAME_ERROR_MSG[37m [39;49;00m,w);[37m[39;49;00m$
  1740^I[37m^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1741^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  1742^I[37m^I^I^I[39;49;00mPyErr_Format(PyExc_SystemError,[37m[39;49;00m$
  1743^I[37m^I^I^I^I     [39;49;00m[33m"[39;49;00m[33mno locals when deleting %s[39;49;00m[33m"[39;49;00m,[37m[39;49;00m$
  1744^I[37m^I^I^I^I     [39;49;00mPyObject_REPR(w));[37m[39;49;00m$
  1745^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1746^I[37m[39;49;00m$
  1747^I[37m^I^I[39;49;00mPREDICTED_WITH_ARG(UNPACK_SEQUENCE);[37m[39;49;00m$
  1748^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mUNPACK_SEQUENCE[39;49;00m:[37m[39;49;00m$
  1749^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1750^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyTuple_CheckExact(v)[37m [39;49;00m&&[37m [39;49;00mPyTuple_GET_SIZE(v)[37m [39;49;00m==[37m [39;49;00moparg)[37m [39;49;00m{[37m[39;49;00m$
  1751^I[37m^I^I^I^I[39;49;00mPyObject[37m [39;49;00m**items[37m [39;49;00m=[37m [39;49;00m((PyTupleObject[37m [39;49;00m*)v)->ob_item;[37m[39;49;00m$
  1752^I[37m^I^I^I^I[39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(oparg--)[37m [39;49;00m{[37m[39;49;00m$
  1753^I[37m^I^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mitems[oparg];[37m[39;49;00m$
  1754^I[37m^I^I^I^I^I[39;49;00mPy_INCREF(w);[37m[39;49;00m$
  1755^I[37m^I^I^I^I^I[39;49;00mPUSH(w);[37m[39;49;00m$
  1756^I[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
  1757^I[37m^I^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1758^I[37m^I^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1759^I[37m^I^I^I[39;49;00m}[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyList_CheckExact(v)[37m [39;49;00m&&[37m [39;49;00mPyList_GET_SIZE(v)[37m [39;49;00m==[37m [39;49;00moparg)[37m [39;49;00m{[37m[39;49;00m$
  1760^I[37m^I^I^I^I[39;49;00mPyObject[37m [39;49;00m**items[37m [39;49;00m=[37m [39;49;00m((PyListObject[37m [39;49;00m*)v)->ob_item;[37m[39;49;00m$
  1761^I[37m^I^I^I^I[39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(oparg--)[37m [39;49;00m{[37m[39;49;00m$
  1762^I[37m^I^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mitems[oparg];[37m[39;49;00m$
  1763^I[37m^I^I^I^I^I[39;49;00mPy_INCREF(w);[37m[39;49;00m$
  1764^I[37m^I^I^I^I^I[39;49;00mPUSH(w);[37m[39;49;00m$
  1765^I[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
  1766^I[37m^I^I^I[39;49;00m}[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(unpack_iterable(v,[37m [39;49;00moparg,[37m[39;49;00m$
  1767^I[37m^I^I^I^I^I^I [39;49;00mstack_pointer[37m [39;49;00m+[37m [39;49;00moparg))[37m[39;49;00m$
  1768^I[37m^I^I^I^I[39;49;00mstack_pointer[37m [39;49;00m+=[37m [39;49;00moparg;[37m[39;49;00m$
  1769^I[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
  1770^I[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyErr_ExceptionMatches(PyExc_TypeError))[37m[39;49;00m$
  1771^I[37m^I^I^I^I^I[39;49;00mPyErr_SetString(PyExc_TypeError,[37m[39;49;00m$
  1772^I[37m^I^I^I^I^I^I[39;49;00m[33m"[39;49;00m[33munpack non-sequence[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
  1773^I[37m^I^I^I^I[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_EXCEPTION;[37m[39;49;00m$
  1774^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  1775^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1776^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1777^I[37m[39;49;00m$
  1778^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSTORE_ATTR[39;49;00m:[37m[39;49;00m$
  1779^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mGETITEM(names,[37m [39;49;00moparg);[37m[39;49;00m$
  1780^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1781^I[37m^I^I^I[39;49;00mu[37m [39;49;00m=[37m [39;49;00mSECOND();[37m[39;49;00m$
  1782^I[37m^I^I^I[39;49;00mSTACKADJ([34m-2[39;49;00m);[37m[39;49;00m$
  1783^I[37m^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyObject_SetAttr(v,[37m [39;49;00mw,[37m [39;49;00mu);[37m [39;49;00m[37m/* v.w = u */[39;49;00m[37m[39;49;00m$
  1784^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1785^I[37m^I^I^I[39;49;00mPy_DECREF(u);[37m[39;49;00m$
  1786^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1787^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1788^I[37m[39;49;00m$
  1789^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mDELETE_ATTR[39;49;00m:[37m[39;49;00m$
  1790^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mGETITEM(names,[37m [39;49;00moparg);[37m[39;49;00m$
  1791^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1792^I[37m^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyObject_SetAttr(v,[37m [39;49;00mw,[37m [39;49;00m(PyObject[37m [39;49;00m*)[36mNULL[39;49;00m);[37m[39;49;00m$
  1793^I[37m^I^I^I^I^I^I^I[39;49;00m[37m/* del v.w */[39;49;00m[37m[39;49;00m$
  1794^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1795^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1796^I[37m[39;49;00m$
  1797^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSTORE_GLOBAL[39;49;00m:[37m[39;49;00m$
  1798^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mGETITEM(names,[37m [39;49;00moparg);[37m[39;49;00m$
  1799^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1800^I[37m^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyDict_SetItem(f->f_globals,[37m [39;49;00mw,[37m [39;49;00mv);[37m[39;49;00m$
  1801^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1802^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1803^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1804^I[37m[39;49;00m$
  1805^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mDELETE_GLOBAL[39;49;00m:[37m[39;49;00m$
  1806^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mGETITEM(names,[37m [39;49;00moparg);[37m[39;49;00m$
  1807^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m((err[37m [39;49;00m=[37m [39;49;00mPyDict_DelItem(f->f_globals,[37m [39;49;00mw))[37m [39;49;00m!=[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1808^I[37m^I^I^I^I[39;49;00mformat_exc_check_arg([37m[39;49;00m$
  1809^I[37m^I^I^I^I    [39;49;00mPyExc_NameError,[37m [39;49;00mGLOBAL_NAME_ERROR_MSG,[37m [39;49;00mw);[37m[39;49;00m$
  1810^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1811^I[37m[39;49;00m$
  1812^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mLOAD_NAME[39;49;00m:[37m[39;49;00m$
  1813^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mGETITEM(names,[37m [39;49;00moparg);[37m[39;49;00m$
  1814^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m((v[37m [39;49;00m=[37m [39;49;00mf->f_locals)[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1815^I[37m^I^I^I^I[39;49;00mPyErr_Format(PyExc_SystemError,[37m[39;49;00m$
  1816^I[37m^I^I^I^I^I     [39;49;00m[33m"[39;49;00m[33mno locals when loading %s[39;49;00m[33m"[39;49;00m,[37m[39;49;00m$
  1817^I[37m^I^I^I^I^I     [39;49;00mPyObject_REPR(w));[37m[39;49;00m$
  1818^I[37m^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1819^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  1820^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyDict_CheckExact(v))[37m [39;49;00m{[37m[39;49;00m$
  1821^I[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyDict_GetItem(v,[37m [39;49;00mw);[37m[39;49;00m$
  1822^I[37m^I^I^I^I[39;49;00mPy_XINCREF(x);[37m[39;49;00m$
  1823^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  1824^I[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
  1825^I[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyObject_GetItem(v,[37m [39;49;00mw);[37m[39;49;00m$
  1826^I[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m[37m [39;49;00m&&[37m [39;49;00mPyErr_Occurred())[37m [39;49;00m{[37m[39;49;00m$
  1827^I[37m^I^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(!PyErr_ExceptionMatches(PyExc_KeyError))[37m[39;49;00m$
  1828^I[37m^I^I^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1829^I[37m^I^I^I^I^I[39;49;00mPyErr_Clear();[37m[39;49;00m$
  1830^I[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
  1831^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  1832^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1833^I[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyDict_GetItem(f->f_globals,[37m [39;49;00mw);[37m[39;49;00m$
  1834^I[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1835^I[37m^I^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyDict_GetItem(f->f_builtins,[37m [39;49;00mw);[37m[39;49;00m$
  1836^I[37m^I^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1837^I[37m^I^I^I^I^I^I[39;49;00mformat_exc_check_arg([37m[39;49;00m$
  1838^I[37m^I^I^I^I^I^I^I    [39;49;00mPyExc_NameError,[37m[39;49;00m$
  1839^I[37m^I^I^I^I^I^I^I    [39;49;00mNAME_ERROR_MSG[37m [39;49;00m,w);[37m[39;49;00m$
  1840^I[37m^I^I^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1841^I[37m^I^I^I^I^I[39;49;00m}[37m[39;49;00m$
  1842^I[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
  1843^I[37m^I^I^I^I[39;49;00mPy_INCREF(x);[37m[39;49;00m$
  1844^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  1845^I[37m^I^I^I[39;49;00mPUSH(x);[37m[39;49;00m$
  1846^I[37m^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1847^I[37m[39;49;00m$
  1848^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mLOAD_GLOBAL[39;49;00m:[37m[39;49;00m$
  1849^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mGETITEM(names,[37m [39;49;00moparg);[37m[39;49;00m$
  1850^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyString_CheckExact(w))[37m [39;49;00m{[37m[39;49;00m$
  1851^I[37m^I^I^I^I[39;49;00m[37m/* Inline the PyDict_GetItem() calls.[39;49;00m$
  1852^I[37m^I^I^I^I   WARNING: this is an extreme speed hack.[39;49;00m$
  1853^I[37m^I^I^I^I   Do not try this at home. */[39;49;00m[37m[39;49;00m$
  1854^I[37m^I^I^I^I[39;49;00m[36mlong[39;49;00m[37m [39;49;00mhash[37m [39;49;00m=[37m [39;49;00m((PyStringObject[37m [39;49;00m*)w)->ob_shash;[37m[39;49;00m$
  1855^I[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(hash[37m [39;49;00m!=[37m [39;49;00m[34m-1[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1856^I[37m^I^I^I^I^I[39;49;00mPyDictObject[37m [39;49;00m*d;[37m[39;49;00m$
  1857^I[37m^I^I^I^I^I[39;49;00mPyDictEntry[37m [39;49;00m*e;[37m[39;49;00m$
  1858^I[37m^I^I^I^I^I[39;49;00md[37m [39;49;00m=[37m [39;49;00m(PyDictObject[37m [39;49;00m*)(f->f_globals);[37m[39;49;00m$
  1859^I[37m^I^I^I^I^I[39;49;00me[37m [39;49;00m=[37m [39;49;00md->ma_lookup(d,[37m [39;49;00mw,[37m [39;49;00mhash);[37m[39;49;00m$
  1860^I[37m^I^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(e[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1861^I[37m^I^I^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  1862^I[37m^I^I^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1863^I[37m^I^I^I^I^I[39;49;00m}[37m[39;49;00m$
  1864^I[37m^I^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00me->me_value;[37m[39;49;00m$
  1865^I[37m^I^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1866^I[37m^I^I^I^I^I^I[39;49;00mPy_INCREF(x);[37m[39;49;00m$
  1867^I[37m^I^I^I^I^I^I[39;49;00mPUSH(x);[37m[39;49;00m$
  1868^I[37m^I^I^I^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1869^I[37m^I^I^I^I^I[39;49;00m}[37m[39;49;00m$
  1870^I[37m^I^I^I^I^I[39;49;00md[37m [39;49;00m=[37m [39;49;00m(PyDictObject[37m [39;49;00m*)(f->f_builtins);[37m[39;49;00m$
  1871^I[37m^I^I^I^I^I[39;49;00me[37m [39;49;00m=[37m [39;49;00md->ma_lookup(d,[37m [39;49;00mw,[37m [39;49;00mhash);[37m[39;49;00m$
  1872^I[37m^I^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(e[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1873^I[37m^I^I^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  1874^I[37m^I^I^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1875^I[37m^I^I^I^I^I[39;49;00m}[37m[39;49;00m$
  1876^I[37m^I^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00me->me_value;[37m[39;49;00m$
  1877^I[37m^I^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1878^I[37m^I^I^I^I^I^I[39;49;00mPy_INCREF(x);[37m[39;49;00m$
  1879^I[37m^I^I^I^I^I^I[39;49;00mPUSH(x);[37m[39;49;00m$
  1880^I[37m^I^I^I^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1881^I[37m^I^I^I^I^I[39;49;00m}[37m[39;49;00m$
  1882^I[37m^I^I^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mload_global_error;[37m[39;49;00m$
  1883^I[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
  1884^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  1885^I[37m^I^I^I[39;49;00m[37m/* This is the un-inlined version of the code above */[39;49;00m[37m[39;49;00m$
  1886^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyDict_GetItem(f->f_globals,[37m [39;49;00mw);[37m[39;49;00m$
  1887^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1888^I[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyDict_GetItem(f->f_builtins,[37m [39;49;00mw);[37m[39;49;00m$
  1889^I[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1890^I[37m^I^I^I^I  [39;49;00mload_global_error:[37m[39;49;00m$
  1891^I[37m^I^I^I^I^I[39;49;00mformat_exc_check_arg([37m[39;49;00m$
  1892^I[37m^I^I^I^I^I^I    [39;49;00mPyExc_NameError,[37m[39;49;00m$
  1893^I[37m^I^I^I^I^I^I    [39;49;00mGLOBAL_NAME_ERROR_MSG,[37m [39;49;00mw);[37m[39;49;00m$
  1894^I[37m^I^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1895^I[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
  1896^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  1897^I[37m^I^I^I[39;49;00mPy_INCREF(x);[37m[39;49;00m$
  1898^I[37m^I^I^I[39;49;00mPUSH(x);[37m[39;49;00m$
  1899^I[37m^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1900^I[37m[39;49;00m$
  1901^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mDELETE_FAST[39;49;00m:[37m[39;49;00m$
  1902^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mGETLOCAL(oparg);[37m[39;49;00m$
  1903^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1904^I[37m^I^I^I^I[39;49;00mSETLOCAL(oparg,[37m [39;49;00m[36mNULL[39;49;00m);[37m[39;49;00m$
  1905^I[37m^I^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1906^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  1907^I[37m^I^I^I[39;49;00mformat_exc_check_arg([37m[39;49;00m$
  1908^I[37m^I^I^I^I[39;49;00mPyExc_UnboundLocalError,[37m[39;49;00m$
  1909^I[37m^I^I^I^I[39;49;00mUNBOUNDLOCAL_ERROR_MSG,[37m[39;49;00m$
  1910^I[37m^I^I^I^I[39;49;00mPyTuple_GetItem(co->co_varnames,[37m [39;49;00moparg)[37m[39;49;00m$
  1911^I[37m^I^I^I^I[39;49;00m);[37m[39;49;00m$
  1912^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1913^I[37m[39;49;00m$
  1914^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mLOAD_CLOSURE[39;49;00m:[37m[39;49;00m$
  1915^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mfreevars[oparg];[37m[39;49;00m$
  1916^I[37m^I^I^I[39;49;00mPy_INCREF(x);[37m[39;49;00m$
  1917^I[37m^I^I^I[39;49;00mPUSH(x);[37m[39;49;00m$
  1918^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1919^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1920^I[37m[39;49;00m$
  1921^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mLOAD_DEREF[39;49;00m:[37m[39;49;00m$
  1922^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mfreevars[oparg];[37m[39;49;00m$
  1923^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPyCell_Get(x);[37m[39;49;00m$
  1924^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(w[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1925^I[37m^I^I^I^I[39;49;00mPUSH(w);[37m[39;49;00m$
  1926^I[37m^I^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1927^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  1928^I[37m^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00m[34m-1[39;49;00m;[37m[39;49;00m$
  1929^I[37m^I^I^I[39;49;00m[37m/* Don't stomp existing exception */[39;49;00m[37m[39;49;00m$
  1930^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyErr_Occurred())[37m[39;49;00m$
  1931^I[37m^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1932^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(oparg[37m [39;49;00m<[37m [39;49;00mPyTuple_GET_SIZE(co->co_cellvars))[37m [39;49;00m{[37m[39;49;00m$
  1933^I[37m^I^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPyTuple_GET_ITEM(co->co_cellvars,[37m[39;49;00m$
  1934^I[37m^I^I^I^I^I^I       [39;49;00moparg);[37m[39;49;00m$
  1935^I[37m^I^I^I       [39;49;00mformat_exc_check_arg([37m[39;49;00m$
  1936^I[37m^I^I^I^I       [39;49;00mPyExc_UnboundLocalError,[37m[39;49;00m$
  1937^I[37m^I^I^I^I       [39;49;00mUNBOUNDLOCAL_ERROR_MSG,[37m[39;49;00m$
  1938^I[37m^I^I^I^I       [39;49;00mv);[37m[39;49;00m$
  1939^I[37m^I^I^I[39;49;00m}[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
  1940^I[37m^I^I^I       [39;49;00mv[37m [39;49;00m=[37m [39;49;00mPyTuple_GET_ITEM([37m[39;49;00m$
  1941^I[37m^I^I^I^I^I      [39;49;00mco->co_freevars,[37m[39;49;00m$
  1942^I[37m^I^I^I^I^I      [39;49;00moparg[37m [39;49;00m-[37m [39;49;00mPyTuple_GET_SIZE(co->co_cellvars));[37m[39;49;00m$
  1943^I[37m^I^I^I       [39;49;00mformat_exc_check_arg([37m[39;49;00m$
  1944^I[37m^I^I^I^I       [39;49;00mPyExc_NameError,[37m[39;49;00m$
  1945^I[37m^I^I^I^I       [39;49;00mUNBOUNDFREE_ERROR_MSG,[37m[39;49;00m$
  1946^I[37m^I^I^I^I       [39;49;00mv);[37m[39;49;00m$
  1947^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  1948^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1949^I[37m[39;49;00m$
  1950^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSTORE_DEREF[39;49;00m:[37m[39;49;00m$
  1951^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1952^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mfreevars[oparg];[37m[39;49;00m$
  1953^I[37m^I^I^I[39;49;00mPyCell_Set(x,[37m [39;49;00mw);[37m[39;49;00m$
  1954^I[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1955^I[37m^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1956^I[37m[39;49;00m$
  1957^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBUILD_TUPLE[39;49;00m:[37m[39;49;00m$
  1958^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyTuple_New(oparg);[37m[39;49;00m$
  1959^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1960^I[37m^I^I^I^I[39;49;00m[34mfor[39;49;00m[37m [39;49;00m(;[37m [39;49;00m--oparg[37m [39;49;00m>=[37m [39;49;00m[34m0[39;49;00m;)[37m [39;49;00m{[37m[39;49;00m$
  1961^I[37m^I^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1962^I[37m^I^I^I^I^I[39;49;00mPyTuple_SET_ITEM(x,[37m [39;49;00moparg,[37m [39;49;00mw);[37m[39;49;00m$
  1963^I[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
  1964^I[37m^I^I^I^I[39;49;00mPUSH(x);[37m[39;49;00m$
  1965^I[37m^I^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1966^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  1967^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1968^I[37m[39;49;00m$
  1969^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBUILD_LIST[39;49;00m:[37m[39;49;00m$
  1970^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m  [39;49;00mPyList_New(oparg);[37m[39;49;00m$
  1971^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1972^I[37m^I^I^I^I[39;49;00m[34mfor[39;49;00m[37m [39;49;00m(;[37m [39;49;00m--oparg[37m [39;49;00m>=[37m [39;49;00m[34m0[39;49;00m;)[37m [39;49;00m{[37m[39;49;00m$
  1973^I[37m^I^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1974^I[37m^I^I^I^I^I[39;49;00mPyList_SET_ITEM(x,[37m [39;49;00moparg,[37m [39;49;00mw);[37m[39;49;00m$
  1975^I[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
  1976^I[37m^I^I^I^I[39;49;00mPUSH(x);[37m[39;49;00m$
  1977^I[37m^I^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1978^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  1979^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1980^I[37m[39;49;00m$
  1981^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBUILD_MAP[39;49;00m:[37m[39;49;00m$
  1982^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyDict_New();[37m[39;49;00m$
  1983^I[37m^I^I^I[39;49;00mPUSH(x);[37m[39;49;00m$
  1984^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1985^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1986^I[37m[39;49;00m$
  1987^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mLOAD_ATTR[39;49;00m:[37m[39;49;00m$
  1988^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mGETITEM(names,[37m [39;49;00moparg);[37m[39;49;00m$
  1989^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1990^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyObject_GetAttr(v,[37m [39;49;00mw);[37m[39;49;00m$
  1991^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1992^I[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1993^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1994^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1995^I[37m[39;49;00m$
  1996^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mCOMPARE_OP[39;49;00m:[37m[39;49;00m$
  1997^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1998^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1999^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyInt_CheckExact(w)[37m [39;49;00m&&[37m [39;49;00mPyInt_CheckExact(v))[37m [39;49;00m{[37m[39;49;00m$
  2000^I[37m^I^I^I^I[39;49;00m[37m/* INLINE: cmp(int, int) */[39;49;00m[37m[39;49;00m$
  2001^I[37m^I^I^I^I[39;49;00m[34mregister[39;49;00m[37m [39;49;00m[36mlong[39;49;00m[37m [39;49;00ma,[37m [39;49;00mb;[37m[39;49;00m$
  2002^I[37m^I^I^I^I[39;49;00m[34mregister[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mres;[37m[39;49;00m$
  2003^I[37m^I^I^I^I[39;49;00ma[37m [39;49;00m=[37m [39;49;00mPyInt_AS_LONG(v);[37m[39;49;00m$
  2004^I[37m^I^I^I^I[39;49;00mb[37m [39;49;00m=[37m [39;49;00mPyInt_AS_LONG(w);[37m[39;49;00m$
  2005^I[37m^I^I^I^I[39;49;00m[34mswitch[39;49;00m[37m [39;49;00m(oparg)[37m [39;49;00m{[37m[39;49;00m$
  2006^I[37m^I^I^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mPyCmp_LT[39;49;00m:[37m [39;49;00mres[37m [39;49;00m=[37m [39;49;00ma[37m [39;49;00m<[37m  [39;49;00mb;[37m [39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2007^I[37m^I^I^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mPyCmp_LE[39;49;00m:[37m [39;49;00mres[37m [39;49;00m=[37m [39;49;00ma[37m [39;49;00m<=[37m [39;49;00mb;[37m [39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2008^I[37m^I^I^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mPyCmp_EQ[39;49;00m:[37m [39;49;00mres[37m [39;49;00m=[37m [39;49;00ma[37m [39;49;00m==[37m [39;49;00mb;[37m [39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2009^I[37m^I^I^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mPyCmp_NE[39;49;00m:[37m [39;49;00mres[37m [39;49;00m=[37m [39;49;00ma[37m [39;49;00m!=[37m [39;49;00mb;[37m [39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2010^I[37m^I^I^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mPyCmp_GT[39;49;00m:[37m [39;49;00mres[37m [39;49;00m=[37m [39;49;00ma[37m [39;49;00m>[37m  [39;49;00mb;[37m [39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2011^I[37m^I^I^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mPyCmp_GE[39;49;00m:[37m [39;49;00mres[37m [39;49;00m=[37m [39;49;00ma[37m [39;49;00m>=[37m [39;49;00mb;[37m [39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2012^I[37m^I^I^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mPyCmp_IS[39;49;00m:[37m [39;49;00mres[37m [39;49;00m=[37m [39;49;00mv[37m [39;49;00m==[37m [39;49;00mw;[37m [39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2013^I[37m^I^I^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mPyCmp_IS_NOT[39;49;00m:[37m [39;49;00mres[37m [39;49;00m=[37m [39;49;00mv[37m [39;49;00m!=[37m [39;49;00mw;[37m [39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2014^I[37m^I^I^I^I[39;49;00m[34mdefault[39;49;00m:[37m [39;49;00m[34mgoto[39;49;00m[37m [39;49;00mslow_compare;[37m[39;49;00m$
  2015^I[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
  2016^I[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mres[37m [39;49;00m?[37m [39;49;00mPy_True[37m [39;49;00m:[37m [39;49;00mPy_False;[37m[39;49;00m$
  2017^I[37m^I^I^I^I[39;49;00mPy_INCREF(x);[37m[39;49;00m$
  2018^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  2019^I[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
  2020^I[37m^I^I^I  [39;49;00mslow_compare:[37m[39;49;00m$
  2021^I[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mcmp_outcome(oparg,[37m [39;49;00mv,[37m [39;49;00mw);[37m[39;49;00m$
  2022^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  2023^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  2024^I[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  2025^I[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
  2026^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2027^I[37m^I^I^I[39;49;00mPREDICT(JUMP_IF_FALSE);[37m[39;49;00m$
  2028^I[37m^I^I^I[39;49;00mPREDICT(JUMP_IF_TRUE);[37m[39;49;00m$
  2029^I[37m^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  2030^I[37m[39;49;00m$
  2031^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mIMPORT_NAME[39;49;00m:[37m[39;49;00m$
  2032^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mGETITEM(names,[37m [39;49;00moparg);[37m[39;49;00m$
  2033^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyDict_GetItemString(f->f_builtins,[37m [39;49;00m[33m"[39;49;00m[33m__import__[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
  2034^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  2035^I[37m^I^I^I^I[39;49;00mPyErr_SetString(PyExc_ImportError,[37m[39;49;00m$
  2036^I[37m^I^I^I^I^I^I[39;49;00m[33m"[39;49;00m[33m__import__ not found[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
  2037^I[37m^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2038^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  2039^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  2040^I[37m^I^I^I[39;49;00mu[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  2041^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyInt_AsLong(u)[37m [39;49;00m!=[37m [39;49;00m[34m-1[39;49;00m[37m [39;49;00m||[37m [39;49;00mPyErr_Occurred())[37m[39;49;00m$
  2042^I[37m^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPyTuple_Pack([34m5[39;49;00m,[37m[39;49;00m$
  2043^I[37m^I^I^I^I^I    [39;49;00mw,[37m[39;49;00m$
  2044^I[37m^I^I^I^I^I    [39;49;00mf->f_globals,[37m[39;49;00m$
  2045^I[37m^I^I^I^I^I    [39;49;00mf->f_locals[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m[37m [39;49;00m?[37m[39;49;00m$
  2046^I[37m^I^I^I^I^I^I  [39;49;00mPy_None[37m [39;49;00m:[37m [39;49;00mf->f_locals,[37m[39;49;00m$
  2047^I[37m^I^I^I^I^I    [39;49;00mv,[37m[39;49;00m$
  2048^I[37m^I^I^I^I^I    [39;49;00mu);[37m[39;49;00m$
  2049^I[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  2050^I[37m^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPyTuple_Pack([34m4[39;49;00m,[37m[39;49;00m$
  2051^I[37m^I^I^I^I^I    [39;49;00mw,[37m[39;49;00m$
  2052^I[37m^I^I^I^I^I    [39;49;00mf->f_globals,[37m[39;49;00m$
  2053^I[37m^I^I^I^I^I    [39;49;00mf->f_locals[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m[37m [39;49;00m?[37m[39;49;00m$
  2054^I[37m^I^I^I^I^I^I  [39;49;00mPy_None[37m [39;49;00m:[37m [39;49;00mf->f_locals,[37m[39;49;00m$
  2055^I[37m^I^I^I^I^I    [39;49;00mv);[37m[39;49;00m$
  2056^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  2057^I[37m^I^I^I[39;49;00mPy_DECREF(u);[37m[39;49;00m$
  2058^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(w[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  2059^I[37m^I^I^I^I[39;49;00mu[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  2060^I[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  2061^I[37m^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2062^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  2063^I[37m^I^I^I[39;49;00mREAD_TIMESTAMP(intr0);[37m[39;49;00m$
  2064^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyEval_CallObject(x,[37m [39;49;00mw);[37m[39;49;00m$
  2065^I[37m^I^I^I[39;49;00mREAD_TIMESTAMP(intr1);[37m[39;49;00m$
  2066^I[37m^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  2067^I[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
  2068^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  2069^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2070^I[37m[39;49;00m$
  2071^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mIMPORT_STAR[39;49;00m:[37m[39;49;00m$
  2072^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  2073^I[37m^I^I^I[39;49;00mPyFrame_FastToLocals(f);[37m[39;49;00m$
  2074^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m((x[37m [39;49;00m=[37m [39;49;00mf->f_locals)[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  2075^I[37m^I^I^I^I[39;49;00mPyErr_SetString(PyExc_SystemError,[37m[39;49;00m$
  2076^I[37m^I^I^I^I^I[39;49;00m[33m"[39;49;00m[33mno locals found during 'import *'[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
  2077^I[37m^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2078^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  2079^I[37m^I^I^I[39;49;00mREAD_TIMESTAMP(intr0);[37m[39;49;00m$
  2080^I[37m^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00mimport_all_from(x,[37m [39;49;00mv);[37m[39;49;00m$
  2081^I[37m^I^I^I[39;49;00mREAD_TIMESTAMP(intr1);[37m[39;49;00m$
  2082^I[37m^I^I^I[39;49;00mPyFrame_LocalsToFast(f,[37m [39;49;00m[34m0[39;49;00m);[37m[39;49;00m$
  2083^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  2084^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  2085^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2086^I[37m[39;49;00m$
  2087^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mIMPORT_FROM[39;49;00m:[37m[39;49;00m$
  2088^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mGETITEM(names,[37m [39;49;00moparg);[37m[39;49;00m$
  2089^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  2090^I[37m^I^I^I[39;49;00mREAD_TIMESTAMP(intr0);[37m[39;49;00m$
  2091^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mimport_from(v,[37m [39;49;00mw);[37m[39;49;00m$
  2092^I[37m^I^I^I[39;49;00mREAD_TIMESTAMP(intr1);[37m[39;49;00m$
  2093^I[37m^I^I^I[39;49;00mPUSH(x);[37m[39;49;00m$
  2094^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  2095^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2096^I[37m[39;49;00m$
  2097^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mJUMP_FORWARD[39;49;00m:[37m[39;49;00m$
  2098^I[37m^I^I^I[39;49;00mJUMPBY(oparg);[37m[39;49;00m$
  2099^I[37m^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
  2100^I[37m[39;49;00m$
  2101^I[37m^I^I[39;49;00mPREDICTED_WITH_ARG(JUMP_IF_FALSE);[37m[39;49;00m$
  2102^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mJUMP_IF_FALSE[39;49;00m:[37m[39;49;00m$
  2103^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  2104^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(w[37m [39;49;00m==[37m [39;49;00mPy_True)[37m [39;49;00m{[37m[39;49;00m$
  2105^I[37m^I^I^I^I[39;49;00mPREDICT(POP_TOP);[37m[39;49;00m$
  2106^I[37m^I^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
  2107^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  2108^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(w[37m [39;49;00m==[37m [39;49;00mPy_False)[37m [39;49;00m{[37m[39;49;00m$
  2109^I[37m^I^I^I^I[39;49;00mJUMPBY(oparg);[37m[39;49;00m$
  2110^I[37m^I^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
  2111^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  2112^I[37m^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyObject_IsTrue(w);[37m[39;49;00m$
  2113^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m>[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  2114^I[37m^I^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
  2115^I[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  2116^I[37m^I^I^I^I[39;49;00mJUMPBY(oparg);[37m[39;49;00m$
  2117^I[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  2118^I[37m^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2119^I[37m^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  2120^I[37m[39;49;00m$
  2121^I[37m^I^I[39;49;00mPREDICTED_WITH_ARG(JUMP_IF_TRUE);[37m[39;49;00m$
  2122^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mJUMP_IF_TRUE[39;49;00m:[37m[39;49;00m$
  2123^I[37m^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  2124^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(w[37m [39;49;00m==[37m [39;49;00mPy_False)[37m [39;49;00m{[37m[39;49;00m$
  2125^I[37m^I^I^I^I[39;49;00mPREDICT(POP_TOP);[37m[39;49;00m$
  2126^I[37m^I^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
  2127^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  2128^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(w[37m [39;49;00m==[37m [39;49;00mPy_True)[37m [39;49;00m{[37m[39;49;00m$
  2129^I[37m^I^I^I^I[39;49;00mJUMPBY(oparg);[37m[39;49;00m$
  2130^I[37m^I^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
  2131^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  2132^I[37m^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyObject_IsTrue(w);[37m[39;49;00m$
  2133^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m>[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  2134^I[37m^I^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
  2135^I[37m^I^I^I^I[39;49;00mJUMPBY(oparg);[37m[39;49;00m$
  2136^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  2137^I[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  2138^I[37m^I^I^I^I[39;49;00m;[37m[39;49;00m$
  2139^I[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  2140^I[37m^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2141^I[37m^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  2142^I[37m[39;49;00m$
  2143^I[37m^I^I[39;49;00mPREDICTED_WITH_ARG(JUMP_ABSOLUTE);[37m[39;49;00m$
  2144^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mJUMP_ABSOLUTE[39;49;00m:[37m[39;49;00m$
  2145^I[37m^I^I^I[39;49;00mJUMPTO(oparg);[37m[39;49;00m$
  2146^I[37m^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  2147^I[37m[39;49;00m$
  2148^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mGET_ITER[39;49;00m:[37m[39;49;00m$
  2149^I[37m^I^I^I[39;49;00m[37m/* before: [obj]; after [getiter(obj)] */[39;49;00m[37m[39;49;00m$
  2150^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  2151^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyObject_GetIter(v);[37m[39;49;00m$
  2152^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  2153^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  2154^I[37m^I^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
  2155^I[37m^I^I^I^I[39;49;00mPREDICT(FOR_ITER);[37m[39;49;00m$
  2156^I[37m^I^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  2157^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  2158^I[37m^I^I^I[39;49;00mSTACKADJ([34m-1[39;49;00m);[37m[39;49;00m$
  2159^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2160^I[37m[39;49;00m$
  2161^I[37m^I^I[39;49;00mPREDICTED_WITH_ARG(FOR_ITER);[37m[39;49;00m$
  2162^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mFOR_ITER[39;49;00m:[37m[39;49;00m$
  2163^I[37m^I^I^I[39;49;00m[37m/* before: [iter]; after: [iter, iter()] *or* [] */[39;49;00m[37m[39;49;00m$
  2164^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  2165^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00m(*v->ob_type->tp_iternext)(v);[37m[39;49;00m$
  2166^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  2167^I[37m^I^I^I^I[39;49;00mPUSH(x);[37m[39;49;00m$
  2168^I[37m^I^I^I^I[39;49;00mPREDICT(STORE_FAST);[37m[39;49;00m$
  2169^I[37m^I^I^I^I[39;49;00mPREDICT(UNPACK_SEQUENCE);[37m[39;49;00m$
  2170^I[37m^I^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  2171^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  2172^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyErr_Occurred())[37m [39;49;00m{[37m[39;49;00m$
  2173^I[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(!PyErr_ExceptionMatches(PyExc_StopIteration))[37m[39;49;00m$
  2174^I[37m^I^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2175^I[37m^I^I^I^I[39;49;00mPyErr_Clear();[37m[39;49;00m$
  2176^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  2177^I[37m^I^I^I[39;49;00m[37m/* iterator ended normally */[39;49;00m[37m[39;49;00m$
  2178^I[37m ^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  2179^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  2180^I[37m^I^I^I[39;49;00mJUMPBY(oparg);[37m[39;49;00m$
  2181^I[37m^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  2182^I[37m[39;49;00m$
  2183^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBREAK_LOOP[39;49;00m:[37m[39;49;00m$
  2184^I[37m^I^I^I[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_BREAK;[37m[39;49;00m$
  2185^I[37m^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_block_end;[37m[39;49;00m$
  2186^I[37m[39;49;00m$
  2187^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mCONTINUE_LOOP[39;49;00m:[37m[39;49;00m$
  2188^I[37m^I^I^I[39;49;00mretval[37m [39;49;00m=[37m [39;49;00mPyInt_FromLong(oparg);[37m[39;49;00m$
  2189^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(!retval)[37m [39;49;00m{[37m[39;49;00m$
  2190^I[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  2191^I[37m^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2192^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  2193^I[37m^I^I^I[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_CONTINUE;[37m[39;49;00m$
  2194^I[37m^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_block_end;[37m[39;49;00m$
  2195^I[37m[39;49;00m$
  2196^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSETUP_LOOP[39;49;00m:[37m[39;49;00m$
  2197^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSETUP_EXCEPT[39;49;00m:[37m[39;49;00m$
  2198^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSETUP_FINALLY[39;49;00m:[37m[39;49;00m$
  2199^I[37m^I^I^I[39;49;00m[37m/* NOTE: If you add any new block-setup opcodes that are not try/except/finally[39;49;00m$
  2200^I[37m^I^I^I   handlers, you may need to update the PyGen_NeedsFinalizing() function. */[39;49;00m[37m[39;49;00m$
  2201^I[37m[39;49;00m$
  2202^I[37m^I^I^I[39;49;00mPyFrame_BlockSetup(f,[37m [39;49;00mopcode,[37m [39;49;00mINSTR_OFFSET()[37m [39;49;00m+[37m [39;49;00moparg,[37m[39;49;00m$
  2203^I[37m^I^I^I^I^I   [39;49;00mSTACK_LEVEL());[37m[39;49;00m$
  2204^I[37m^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  2205^I[37m[39;49;00m$
  2206^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mWITH_CLEANUP[39;49;00m:[37m[39;49;00m$
  2207^I[37m^I^I[39;49;00m{[37m[39;49;00m$
  2208^I[37m^I^I^I[39;49;00m[37m/* TOP is the context.__exit__ bound method.[39;49;00m$
  2209^I[37m^I^I^I   Below that are 1-3 values indicating how/why[39;49;00m$
  2210^I[37m^I^I^I   we entered the finally clause:[39;49;00m$
  2211^I[37m^I^I^I   - SECOND = None[39;49;00m$
  2212^I[37m^I^I^I   - (SECOND, THIRD) = (WHY_{RETURN,CONTINUE}), retval[39;49;00m$
  2213^I[37m^I^I^I   - SECOND = WHY_*; no retval below it[39;49;00m$
  2214^I[37m^I^I^I   - (SECOND, THIRD, FOURTH) = exc_info()[39;49;00m$
  2215^I[37m^I^I^I   In the last case, we must call[39;49;00m$
  2216^I[37m^I^I^I     TOP(SECOND, THIRD, FOURTH)[39;49;00m$
  2217^I[37m^I^I^I   otherwise we must call[39;49;00m$
  2218^I[37m^I^I^I     TOP(None, None, None)[39;49;00m$
  2219^I[37m[39;49;00m$
  2220^I[37m^I^I^I   In addition, if the stack represents an exception,[39;49;00m$
  2221^I[37m^I^I^I   *and* the function call returns a 'true' value, we[39;49;00m$
  2222^I[37m^I^I^I   "zap" this information, to prevent END_FINALLY from[39;49;00m$
  2223^I[37m^I^I^I   re-raising the exception.  (But non-local gotos[39;49;00m$
  2224^I[37m^I^I^I   should still be resumed.)[39;49;00m$
  2225^I[37m^I^I^I*/[39;49;00m[37m[39;49;00m$
  2226^I[37m[39;49;00m$
  2227^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  2228^I[37m^I^I^I[39;49;00mu[37m [39;49;00m=[37m [39;49;00mSECOND();[37m[39;49;00m$
  2229^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyInt_Check(u)[37m [39;49;00m||[37m [39;49;00mu[37m [39;49;00m==[37m [39;49;00mPy_None)[37m [39;49;00m{[37m[39;49;00m$
  2230^I[37m^I^I^I^I[39;49;00mu[37m [39;49;00m=[37m [39;49;00mv[37m [39;49;00m=[37m [39;49;00mw[37m [39;49;00m=[37m [39;49;00mPy_None;[37m[39;49;00m$
  2231^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  2232^I[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
  2233^I[37m^I^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTHIRD();[37m[39;49;00m$
  2234^I[37m^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mFOURTH();[37m[39;49;00m$
  2235^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  2236^I[37m^I^I^I[39;49;00m[37m/* XXX Not the fastest way to call it... */[39;49;00m[37m[39;49;00m$
  2237^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyObject_CallFunctionObjArgs(x,[37m [39;49;00mu,[37m [39;49;00mv,[37m [39;49;00mw,[37m [39;49;00m[36mNULL[39;49;00m);[37m[39;49;00m$
  2238^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
  2239^I[37m^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m [39;49;00m[37m/* Go to error exit */[39;49;00m[37m[39;49;00m$
  2240^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(u[37m [39;49;00m!=[37m [39;49;00mPy_None[37m [39;49;00m&&[37m [39;49;00mPyObject_IsTrue(x))[37m [39;49;00m{[37m[39;49;00m$
  2241^I[37m^I^I^I^I[39;49;00m[37m/* There was an exception and a true return */[39;49;00m[37m[39;49;00m$
  2242^I[37m^I^I^I^I[39;49;00mPy_DECREF(x);[37m[39;49;00m$
  2243^I[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mTOP();[37m [39;49;00m[37m/* Again */[39;49;00m[37m[39;49;00m$
  2244^I[37m^I^I^I^I[39;49;00mSTACKADJ([34m-3[39;49;00m);[37m[39;49;00m$
  2245^I[37m^I^I^I^I[39;49;00mPy_INCREF(Py_None);[37m[39;49;00m$
  2246^I[37m^I^I^I^I[39;49;00mSET_TOP(Py_None);[37m[39;49;00m$
  2247^I[37m^I^I^I^I[39;49;00mPy_DECREF(x);[37m[39;49;00m$
  2248^I[37m^I^I^I^I[39;49;00mPy_DECREF(u);[37m[39;49;00m$
  2249^I[37m^I^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  2250^I[37m^I^I^I^I[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  2251^I[37m^I^I^I[39;49;00m}[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
  2252^I[37m^I^I^I^I[39;49;00m[37m/* Let END_FINALLY do its thing */[39;49;00m[37m[39;49;00m$
  2253^I[37m^I^I^I^I[39;49;00mPy_DECREF(x);[37m[39;49;00m$
  2254^I[37m^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  2255^I[37m^I^I^I^I[39;49;00mPy_DECREF(x);[37m[39;49;00m$
  2256^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  2257^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2258^I[37m^I^I[39;49;00m}[37m[39;49;00m$
  2259^I[37m[39;49;00m$
  2260^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mCALL_FUNCTION[39;49;00m:[37m[39;49;00m$
  2261^I[37m^I^I[39;49;00m{[37m[39;49;00m$
  2262^I[37m^I^I^I[39;49;00mPyObject[37m [39;49;00m**sp;[37m[39;49;00m$
  2263^I[37m^I^I^I[39;49;00mPCALL(PCALL_ALL);[37m[39;49;00m$
  2264^I[37m^I^I^I[39;49;00msp[37m [39;49;00m=[37m [39;49;00mstack_pointer;[37m[39;49;00m$
  2265^I[36m#[39;49;00m[36mifdef WITH_TSC[39;49;00m[36m[39;49;00m$
  2266^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mcall_function(&sp,[37m [39;49;00moparg,[37m [39;49;00m&intr0,[37m [39;49;00m&intr1);[37m[39;49;00m$
  2267^I[36m#[39;49;00m[36melse[39;49;00m[36m[39;49;00m$
  2268^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mcall_function(&sp,[37m [39;49;00moparg);[37m[39;49;00m$
  2269^I[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
  2270^I[37m^I^I^I[39;49;00mstack_pointer[37m [39;49;00m=[37m [39;49;00msp;[37m[39;49;00m$
  2271^I[37m^I^I^I[39;49;00mPUSH(x);[37m[39;49;00m$
  2272^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
  2273^I[37m^I^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  2274^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2275^I[37m^I^I[39;49;00m}[37m[39;49;00m$
  2276^I[37m[39;49;00m$
  2277^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mCALL_FUNCTION_VAR[39;49;00m:[37m[39;49;00m$
  2278^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mCALL_FUNCTION_KW[39;49;00m:[37m[39;49;00m$
  2279^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mCALL_FUNCTION_VAR_KW[39;49;00m:[37m[39;49;00m$
  2280^I[37m^I^I[39;49;00m{[37m[39;49;00m$
  2281^I[37m^I^I    [39;49;00m[36mint[39;49;00m[37m [39;49;00mna[37m [39;49;00m=[37m [39;49;00moparg[37m [39;49;00m&[37m [39;49;00m[34m0xff[39;49;00m;[37m[39;49;00m$
  2282^I[37m^I^I    [39;49;00m[36mint[39;49;00m[37m [39;49;00mnk[37m [39;49;00m=[37m [39;49;00m(oparg>>[34m8[39;49;00m)[37m [39;49;00m&[37m [39;49;00m[34m0xff[39;49;00m;[37m[39;49;00m$
  2283^I[37m^I^I    [39;49;00m[36mint[39;49;00m[37m [39;49;00mflags[37m [39;49;00m=[37m [39;49;00m(opcode[37m [39;49;00m-[37m [39;49;00mCALL_FUNCTION)[37m [39;49;00m&[37m [39;49;00m[34m3[39;49;00m;[37m[39;49;00m$
  2284^I[37m^I^I    [39;49;00m[36mint[39;49;00m[37m [39;49;00mn[37m [39;49;00m=[37m [39;49;00mna[37m [39;49;00m+[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m*[37m [39;49;00mnk;[37m[39;49;00m$
  2285^I[37m^I^I    [39;49;00mPyObject[37m [39;49;00m**pfunc,[37m [39;49;00m*func,[37m [39;49;00m**sp;[37m[39;49;00m$
  2286^I[37m^I^I    [39;49;00mPCALL(PCALL_ALL);[37m[39;49;00m$
  2287^I[37m^I^I    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(flags[37m [39;49;00m&[37m [39;49;00mCALL_FLAG_VAR)[37m[39;49;00m$
  2288^I[37m^I^I^I    [39;49;00mn++;[37m[39;49;00m$
  2289^I[37m^I^I    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(flags[37m [39;49;00m&[37m [39;49;00mCALL_FLAG_KW)[37m[39;49;00m$
  2290^I[37m^I^I^I    [39;49;00mn++;[37m[39;49;00m$
  2291^I[37m^I^I    [39;49;00mpfunc[37m [39;49;00m=[37m [39;49;00mstack_pointer[37m [39;49;00m-[37m [39;49;00mn[37m [39;49;00m-[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
  2292^I[37m^I^I    [39;49;00mfunc[37m [39;49;00m=[37m [39;49;00m*pfunc;[37m[39;49;00m$
  2293^I[37m[39;49;00m$
  2294^I[37m^I^I    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyMethod_Check(func)[37m[39;49;00m$
  2295^I[37m^I^I^I[39;49;00m&&[37m [39;49;00mPyMethod_GET_SELF(func)[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  2296^I[37m^I^I^I    [39;49;00mPyObject[37m [39;49;00m*self[37m [39;49;00m=[37m [39;49;00mPyMethod_GET_SELF(func);[37m[39;49;00m$
  2297^I[37m^I^I^I    [39;49;00mPy_INCREF(self);[37m[39;49;00m$
  2298^I[37m^I^I^I    [39;49;00mfunc[37m [39;49;00m=[37m [39;49;00mPyMethod_GET_FUNCTION(func);[37m[39;49;00m$
  2299^I[37m^I^I^I    [39;49;00mPy_INCREF(func);[37m[39;49;00m$
  2300^I[37m^I^I^I    [39;49;00mPy_DECREF(*pfunc);[37m[39;49;00m$
  2301^I[37m^I^I^I    [39;49;00m*pfunc[37m [39;49;00m=[37m [39;49;00mself;[37m[39;49;00m$
  2302^I[37m^I^I^I    [39;49;00mna++;[37m[39;49;00m$
  2303^I[37m^I^I^I    [39;49;00mn++;[37m[39;49;00m$
  2304^I[37m^I^I    [39;49;00m}[37m [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  2305^I[37m^I^I^I    [39;49;00mPy_INCREF(func);[37m[39;49;00m$
  2306^I[37m^I^I    [39;49;00msp[37m [39;49;00m=[37m [39;49;00mstack_pointer;[37m[39;49;00m$
  2307^I[37m^I^I    [39;49;00mREAD_TIMESTAMP(intr0);[37m[39;49;00m$
  2308^I[37m^I^I    [39;49;00mx[37m [39;49;00m=[37m [39;49;00mext_do_call(func,[37m [39;49;00m&sp,[37m [39;49;00mflags,[37m [39;49;00mna,[37m [39;49;00mnk);[37m[39;49;00m$
  2309^I[37m^I^I    [39;49;00mREAD_TIMESTAMP(intr1);[37m[39;49;00m$
  2310^I[37m^I^I    [39;49;00mstack_pointer[37m [39;49;00m=[37m [39;49;00msp;[37m[39;49;00m$
  2311^I[37m^I^I    [39;49;00mPy_DECREF(func);[37m[39;49;00m$
  2312^I[37m[39;49;00m$
  2313^I[37m^I^I    [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(stack_pointer[37m [39;49;00m>[37m [39;49;00mpfunc)[37m [39;49;00m{[37m[39;49;00m$
  2314^I[37m^I^I^I    [39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  2315^I[37m^I^I^I    [39;49;00mPy_DECREF(w);[37m[39;49;00m$
  2316^I[37m^I^I    [39;49;00m}[37m[39;49;00m$
  2317^I[37m^I^I    [39;49;00mPUSH(x);[37m[39;49;00m$
  2318^I[37m^I^I    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
  2319^I[37m^I^I^I    [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  2320^I[37m^I^I    [39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2321^I[37m^I^I[39;49;00m}[37m[39;49;00m$
  2322^I[37m[39;49;00m$
  2323^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mMAKE_FUNCTION[39;49;00m:[37m[39;49;00m$
  2324^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m [39;49;00m[37m/* code object */[39;49;00m[37m[39;49;00m$
  2325^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyFunction_New(v,[37m [39;49;00mf->f_globals);[37m[39;49;00m$
  2326^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  2327^I[37m^I^I^I[39;49;00m[37m/* XXX Maybe this should be a separate opcode? */[39;49;00m[37m[39;49;00m$
  2328^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m[37m [39;49;00m&&[37m [39;49;00moparg[37m [39;49;00m>[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  2329^I[37m^I^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPyTuple_New(oparg);[37m[39;49;00m$
  2330^I[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(v[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  2331^I[37m^I^I^I^I^I[39;49;00mPy_DECREF(x);[37m[39;49;00m$
  2332^I[37m^I^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  2333^I[37m^I^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2334^I[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
  2335^I[37m^I^I^I^I[39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(--oparg[37m [39;49;00m>=[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  2336^I[37m^I^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  2337^I[37m^I^I^I^I^I[39;49;00mPyTuple_SET_ITEM(v,[37m [39;49;00moparg,[37m [39;49;00mw);[37m[39;49;00m$
  2338^I[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
  2339^I[37m^I^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyFunction_SetDefaults(x,[37m [39;49;00mv);[37m[39;49;00m$
  2340^I[37m^I^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  2341^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  2342^I[37m^I^I^I[39;49;00mPUSH(x);[37m[39;49;00m$
  2343^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2344^I[37m[39;49;00m$
  2345^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mMAKE_CLOSURE[39;49;00m:[37m[39;49;00m$
  2346^I[37m^I^I[39;49;00m{[37m[39;49;00m$
  2347^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m [39;49;00m[37m/* code object */[39;49;00m[37m[39;49;00m$
  2348^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyFunction_New(v,[37m [39;49;00mf->f_globals);[37m[39;49;00m$
  2349^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  2350^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  2351^I[37m^I^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  2352^I[37m^I^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyFunction_SetClosure(x,[37m [39;49;00mv);[37m[39;49;00m$
  2353^I[37m^I^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  2354^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  2355^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m[37m [39;49;00m&&[37m [39;49;00moparg[37m [39;49;00m>[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  2356^I[37m^I^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPyTuple_New(oparg);[37m[39;49;00m$
  2357^I[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(v[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  2358^I[37m^I^I^I^I^I[39;49;00mPy_DECREF(x);[37m[39;49;00m$
  2359^I[37m^I^I^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  2360^I[37m^I^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2361^I[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
  2362^I[37m^I^I^I^I[39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(--oparg[37m [39;49;00m>=[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  2363^I[37m^I^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  2364^I[37m^I^I^I^I^I[39;49;00mPyTuple_SET_ITEM(v,[37m [39;49;00moparg,[37m [39;49;00mw);[37m[39;49;00m$
  2365^I[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
  2366^I[37m^I^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyFunction_SetDefaults(x,[37m [39;49;00mv);[37m[39;49;00m$
  2367^I[37m^I^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  2368^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  2369^I[37m^I^I^I[39;49;00mPUSH(x);[37m[39;49;00m$
  2370^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2371^I[37m^I^I[39;49;00m}[37m[39;49;00m$
  2372^I[37m[39;49;00m$
  2373^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBUILD_SLICE[39;49;00m:[37m[39;49;00m$
  2374^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(oparg[37m [39;49;00m==[37m [39;49;00m[34m3[39;49;00m)[37m[39;49;00m$
  2375^I[37m^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  2376^I[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  2377^I[37m^I^I^I^I[39;49;00mw[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  2378^I[37m^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  2379^I[37m^I^I^I[39;49;00mu[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  2380^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPySlice_New(u,[37m [39;49;00mv,[37m [39;49;00mw);[37m[39;49;00m$
  2381^I[37m^I^I^I[39;49;00mPy_DECREF(u);[37m[39;49;00m$
  2382^I[37m^I^I^I[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  2383^I[37m^I^I^I[39;49;00mPy_XDECREF(w);[37m[39;49;00m$
  2384^I[37m^I^I^I[39;49;00mSET_TOP(x);[37m[39;49;00m$
  2385^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  2386^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2387^I[37m[39;49;00m$
  2388^I[37m^I^I[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mEXTENDED_ARG[39;49;00m:[37m[39;49;00m$
  2389^I[37m^I^I^I[39;49;00mopcode[37m [39;49;00m=[37m [39;49;00mNEXTOP();[37m[39;49;00m$
  2390^I[37m^I^I^I[39;49;00moparg[37m [39;49;00m=[37m [39;49;00moparg<<[34m16[39;49;00m[37m [39;49;00m|[37m [39;49;00mNEXTARG();[37m[39;49;00m$
  2391^I[37m^I^I^I[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mdispatch_opcode;[37m[39;49;00m$
  2392^I[37m[39;49;00m$
  2393^I[37m^I^I[39;49;00m[34mdefault[39;49;00m:[37m[39;49;00m$
  2394^I[37m^I^I^I[39;49;00mfprintf(stderr,[37m[39;49;00m$
  2395^I[37m^I^I^I^I[39;49;00m[33m"[39;49;00m[33mXXX lineno: %d, opcode: %d[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m,[37m[39;49;00m$
  2396^I[37m^I^I^I^I[39;49;00mPyCode_Addr2Line(f->f_code,[37m [39;49;00mf->f_lasti),[37m[39;49;00m$
  2397^I[37m^I^I^I^I[39;49;00mopcode);[37m[39;49;00m$
  2398^I[37m^I^I^I[39;49;00mPyErr_SetString(PyExc_SystemError,[37m [39;49;00m[33m"[39;49;00m[33munknown opcode[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
  2399^I[37m^I^I^I[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_EXCEPTION;[37m[39;49;00m$
  2400^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2401^I[37m[39;49;00m$
  2402^I[36m#[39;49;00m[36mifdef CASE_TOO_BIG[39;49;00m[36m[39;49;00m$
  2403^I[37m^I^I[39;49;00m}[37m[39;49;00m$
  2404^I[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
  2405^I[37m[39;49;00m$
  2406^I[37m^I^I[39;49;00m}[37m [39;49;00m[37m/* switch */[39;49;00m[37m[39;49;00m$
  2407^I[37m[39;49;00m$
  2408^I[37m^I    [39;49;00mon_error:[37m[39;49;00m$
  2409^I[37m[39;49;00m$
  2410^I[37m^I^I[39;49;00mREAD_TIMESTAMP(inst1);[37m[39;49;00m$
  2411^I[37m[39;49;00m$
  2412^I[37m^I^I[39;49;00m[37m/* Quickly continue if no error occurred */[39;49;00m[37m[39;49;00m$
  2413^I[37m[39;49;00m$
  2414^I[37m^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(why[37m [39;49;00m==[37m [39;49;00mWHY_NOT)[37m [39;49;00m{[37m[39;49;00m$
  2415^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m&&[37m [39;49;00mx[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  2416^I[36m#[39;49;00m[36mifdef CHECKEXC[39;49;00m[36m[39;49;00m$
  2417^I[37m^I^I^I^I[39;49;00m[37m/* This check is expensive! */[39;49;00m[37m[39;49;00m$
  2418^I[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyErr_Occurred())[37m[39;49;00m$
  2419^I[37m^I^I^I^I^I[39;49;00mfprintf(stderr,[37m[39;49;00m$
  2420^I[37m^I^I^I^I^I^I[39;49;00m[33m"[39;49;00m[33mXXX undetected error[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
  2421^I[37m^I^I^I^I[39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
  2422^I[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
  2423^I[37m^I^I^I^I^I[39;49;00mREAD_TIMESTAMP(loop1);[37m[39;49;00m$
  2424^I[37m^I^I^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m [39;49;00m[37m/* Normal, fast path */[39;49;00m[37m[39;49;00m$
  2425^I[36m#[39;49;00m[36mifdef CHECKEXC[39;49;00m[36m[39;49;00m$
  2426^I[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
  2427^I[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
  2428^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  2429^I[37m^I^I^I[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_EXCEPTION;[37m[39;49;00m$
  2430^I[37m^I^I^I[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPy_None;[37m[39;49;00m$
  2431^I[37m^I^I^I[39;49;00merr[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
  2432^I[37m^I^I[39;49;00m}[37m[39;49;00m$
  2433^I[37m[39;49;00m$
  2434^I[37m^I^I[39;49;00m[37m/* Double-check exception status */[39;49;00m[37m[39;49;00m$
  2435^I[37m[39;49;00m$
  2436^I[37m^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(why[37m [39;49;00m==[37m [39;49;00mWHY_EXCEPTION[37m [39;49;00m||[37m [39;49;00mwhy[37m [39;49;00m==[37m [39;49;00mWHY_RERAISE)[37m [39;49;00m{[37m[39;49;00m$
  2437^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(!PyErr_Occurred())[37m [39;49;00m{[37m[39;49;00m$
  2438^I[37m^I^I^I^I[39;49;00mPyErr_SetString(PyExc_SystemError,[37m[39;49;00m$
  2439^I[37m^I^I^I^I^I[39;49;00m[33m"[39;49;00m[33merror return without exception set[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
  2440^I[37m^I^I^I^I[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_EXCEPTION;[37m[39;49;00m$
  2441^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  2442^I[37m^I^I[39;49;00m}[37m[39;49;00m$
  2443^I[36m#[39;49;00m[36mifdef CHECKEXC[39;49;00m[36m[39;49;00m$
  2444^I[37m^I^I[39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
  2445^I[37m^I^I^I[39;49;00m[37m/* This check is expensive! */[39;49;00m[37m[39;49;00m$
  2446^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyErr_Occurred())[37m [39;49;00m{[37m[39;49;00m$
  2447^I[37m^I^I^I^I[39;49;00m[36mchar[39;49;00m[37m [39;49;00mbuf[[34m1024[39;49;00m];[37m[39;49;00m$
  2448^I[37m^I^I^I^I[39;49;00msprintf(buf,[37m [39;49;00m[33m"[39;49;00m[33mStack unwind with exception [39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2449^I[37m^I^I^I^I^I[39;49;00m[33m"[39;49;00m[33mset and why=%d[39;49;00m[33m"[39;49;00m,[37m [39;49;00mwhy);[37m[39;49;00m$
  2450^I[37m^I^I^I^I[39;49;00mPy_FatalError(buf);[37m[39;49;00m$
  2451^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  2452^I[37m^I^I[39;49;00m}[37m[39;49;00m$
  2453^I[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
  2454^I[37m[39;49;00m$
  2455^I[37m^I^I[39;49;00m[37m/* Log traceback info if this is a real exception */[39;49;00m[37m[39;49;00m$
  2456^I[37m[39;49;00m$
  2457^I[37m^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(why[37m [39;49;00m==[37m [39;49;00mWHY_EXCEPTION)[37m [39;49;00m{[37m[39;49;00m$
  2458^I[37m^I^I^I[39;49;00mPyTraceBack_Here(f);[37m[39;49;00m$
  2459^I[37m[39;49;00m$
  2460^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(tstate->c_tracefunc[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
  2461^I[37m^I^I^I^I[39;49;00mcall_exc_trace(tstate->c_tracefunc,[37m[39;49;00m$
  2462^I[37m^I^I^I^I^I       [39;49;00mtstate->c_traceobj,[37m [39;49;00mf);[37m[39;49;00m$
  2463^I[37m^I^I[39;49;00m}[37m[39;49;00m$
  2464^I[37m[39;49;00m$
  2465^I[37m^I^I[39;49;00m[37m/* For the rest, treat WHY_RERAISE as WHY_EXCEPTION */[39;49;00m[37m[39;49;00m$
  2466^I[37m[39;49;00m$
  2467^I[37m^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(why[37m [39;49;00m==[37m [39;49;00mWHY_RERAISE)[37m[39;49;00m$
  2468^I[37m^I^I^I[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_EXCEPTION;[37m[39;49;00m$
  2469^I[37m[39;49;00m$
  2470^I[37m^I^I[39;49;00m[37m/* Unwind stacks if a (pseudo) exception occurred */[39;49;00m[37m[39;49;00m$
  2471^I[37m[39;49;00m$
  2472^Ifast_block_end:[37m[39;49;00m$
  2473^I[37m^I^I[39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(why[37m [39;49;00m!=[37m [39;49;00mWHY_NOT[37m [39;49;00m&&[37m [39;49;00mf->f_iblock[37m [39;49;00m>[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  2474^I[37m^I^I^I[39;49;00mPyTryBlock[37m [39;49;00m*b[37m [39;49;00m=[37m [39;49;00mPyFrame_BlockPop(f);[37m[39;49;00m$
  2475^I[37m[39;49;00m$
  2476^I[37m^I^I^I[39;49;00massert(why[37m [39;49;00m!=[37m [39;49;00mWHY_YIELD);[37m[39;49;00m$
  2477^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(b->b_type[37m [39;49;00m==[37m [39;49;00mSETUP_LOOP[37m [39;49;00m&&[37m [39;49;00mwhy[37m [39;49;00m==[37m [39;49;00mWHY_CONTINUE)[37m [39;49;00m{[37m[39;49;00m$
  2478^I[37m^I^I^I^I[39;49;00m[37m/* For a continue inside a try block,[39;49;00m$
  2479^I[37m^I^I^I^I   don't pop the block for the loop. */[39;49;00m[37m[39;49;00m$
  2480^I[37m^I^I^I^I[39;49;00mPyFrame_BlockSetup(f,[37m [39;49;00mb->b_type,[37m [39;49;00mb->b_handler,[37m[39;49;00m$
  2481^I[37m^I^I^I^I^I^I   [39;49;00mb->b_level);[37m[39;49;00m$
  2482^I[37m^I^I^I^I[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_NOT;[37m[39;49;00m$
  2483^I[37m^I^I^I^I[39;49;00mJUMPTO(PyInt_AS_LONG(retval));[37m[39;49;00m$
  2484^I[37m^I^I^I^I[39;49;00mPy_DECREF(retval);[37m[39;49;00m$
  2485^I[37m^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2486^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  2487^I[37m[39;49;00m$
  2488^I[37m^I^I^I[39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(STACK_LEVEL()[37m [39;49;00m>[37m [39;49;00mb->b_level)[37m [39;49;00m{[37m[39;49;00m$
  2489^I[37m^I^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  2490^I[37m^I^I^I^I[39;49;00mPy_XDECREF(v);[37m[39;49;00m$
  2491^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  2492^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(b->b_type[37m [39;49;00m==[37m [39;49;00mSETUP_LOOP[37m [39;49;00m&&[37m [39;49;00mwhy[37m [39;49;00m==[37m [39;49;00mWHY_BREAK)[37m [39;49;00m{[37m[39;49;00m$
  2493^I[37m^I^I^I^I[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_NOT;[37m[39;49;00m$
  2494^I[37m^I^I^I^I[39;49;00mJUMPTO(b->b_handler);[37m[39;49;00m$
  2495^I[37m^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2496^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  2497^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(b->b_type[37m [39;49;00m==[37m [39;49;00mSETUP_FINALLY[37m [39;49;00m||[37m[39;49;00m$
  2498^I[37m^I^I^I    [39;49;00m(b->b_type[37m [39;49;00m==[37m [39;49;00mSETUP_EXCEPT[37m [39;49;00m&&[37m[39;49;00m$
  2499^I[37m^I^I^I     [39;49;00mwhy[37m [39;49;00m==[37m [39;49;00mWHY_EXCEPTION))[37m [39;49;00m{[37m[39;49;00m$
  2500^I[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(why[37m [39;49;00m==[37m [39;49;00mWHY_EXCEPTION)[37m [39;49;00m{[37m[39;49;00m$
  2501^I[37m^I^I^I^I^I[39;49;00mPyObject[37m [39;49;00m*exc,[37m [39;49;00m*val,[37m [39;49;00m*tb;[37m[39;49;00m$
  2502^I[37m^I^I^I^I^I[39;49;00mPyErr_Fetch(&exc,[37m [39;49;00m&val,[37m [39;49;00m&tb);[37m[39;49;00m$
  2503^I[37m^I^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(val[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  2504^I[37m^I^I^I^I^I^I[39;49;00mval[37m [39;49;00m=[37m [39;49;00mPy_None;[37m[39;49;00m$
  2505^I[37m^I^I^I^I^I^I[39;49;00mPy_INCREF(val);[37m[39;49;00m$
  2506^I[37m^I^I^I^I^I[39;49;00m}[37m[39;49;00m$
  2507^I[37m^I^I^I^I^I[39;49;00m[37m/* Make the raw exception data[39;49;00m$
  2508^I[37m^I^I^I^I^I   available to the handler,[39;49;00m$
  2509^I[37m^I^I^I^I^I   so a program can emulate the[39;49;00m$
  2510^I[37m^I^I^I^I^I   Python main loop.  Don't do[39;49;00m$
  2511^I[37m^I^I^I^I^I   this for 'finally'. */[39;49;00m[37m[39;49;00m$
  2512^I[37m^I^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(b->b_type[37m [39;49;00m==[37m [39;49;00mSETUP_EXCEPT)[37m [39;49;00m{[37m[39;49;00m$
  2513^I[37m^I^I^I^I^I^I[39;49;00mPyErr_NormalizeException([37m[39;49;00m$
  2514^I[37m^I^I^I^I^I^I^I[39;49;00m&exc,[37m [39;49;00m&val,[37m [39;49;00m&tb);[37m[39;49;00m$
  2515^I[37m^I^I^I^I^I^I[39;49;00mset_exc_info(tstate,[37m[39;49;00m$
  2516^I[37m^I^I^I^I^I^I^I     [39;49;00mexc,[37m [39;49;00mval,[37m [39;49;00mtb);[37m[39;49;00m$
  2517^I[37m^I^I^I^I^I[39;49;00m}[37m[39;49;00m$
  2518^I[37m^I^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(tb[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  2519^I[37m^I^I^I^I^I^I[39;49;00mPy_INCREF(Py_None);[37m[39;49;00m$
  2520^I[37m^I^I^I^I^I^I[39;49;00mPUSH(Py_None);[37m[39;49;00m$
  2521^I[37m^I^I^I^I^I[39;49;00m}[37m [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  2522^I[37m^I^I^I^I^I^I[39;49;00mPUSH(tb);[37m[39;49;00m$
  2523^I[37m^I^I^I^I^I[39;49;00mPUSH(val);[37m[39;49;00m$
  2524^I[37m^I^I^I^I^I[39;49;00mPUSH(exc);[37m[39;49;00m$
  2525^I[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
  2526^I[37m^I^I^I^I[39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
  2527^I[37m^I^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(why[37m [39;49;00m&[37m [39;49;00m(WHY_RETURN[37m [39;49;00m|[37m [39;49;00mWHY_CONTINUE))[37m[39;49;00m$
  2528^I[37m^I^I^I^I^I^I[39;49;00mPUSH(retval);[37m[39;49;00m$
  2529^I[37m^I^I^I^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPyInt_FromLong(([36mlong[39;49;00m)why);[37m[39;49;00m$
  2530^I[37m^I^I^I^I^I[39;49;00mPUSH(v);[37m[39;49;00m$
  2531^I[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
  2532^I[37m^I^I^I^I[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_NOT;[37m[39;49;00m$
  2533^I[37m^I^I^I^I[39;49;00mJUMPTO(b->b_handler);[37m[39;49;00m$
  2534^I[37m^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2535^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  2536^I[37m^I^I[39;49;00m}[37m [39;49;00m[37m/* unwind stack */[39;49;00m[37m[39;49;00m$
  2537^I[37m[39;49;00m$
  2538^I[37m^I^I[39;49;00m[37m/* End the loop if we still have an error (or return) */[39;49;00m[37m[39;49;00m$
  2539^I[37m[39;49;00m$
  2540^I[37m^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(why[37m [39;49;00m!=[37m [39;49;00mWHY_NOT)[37m[39;49;00m$
  2541^I[37m^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2542^I[37m^I^I[39;49;00mREAD_TIMESTAMP(loop1);[37m[39;49;00m$
  2543^I[37m[39;49;00m$
  2544^I[37m^I[39;49;00m}[37m [39;49;00m[37m/* main loop */[39;49;00m[37m[39;49;00m$
  2545^I[37m[39;49;00m$
  2546^I[37m^I[39;49;00massert(why[37m [39;49;00m!=[37m [39;49;00mWHY_YIELD);[37m[39;49;00m$
  2547^I[37m^I[39;49;00m[37m/* Pop remaining stack entries. */[39;49;00m[37m[39;49;00m$
  2548^I[37m^I[39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(!EMPTY())[37m [39;49;00m{[37m[39;49;00m$
  2549^I[37m^I^I[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  2550^I[37m^I^I[39;49;00mPy_XDECREF(v);[37m[39;49;00m$
  2551^I[37m^I[39;49;00m}[37m[39;49;00m$
  2552^I[37m[39;49;00m$
  2553^I[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(why[37m [39;49;00m!=[37m [39;49;00mWHY_RETURN)[37m[39;49;00m$
  2554^I[37m^I^I[39;49;00mretval[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  2555^I[37m[39;49;00m$
  2556^Ifast_yield:[37m[39;49;00m$
  2557^I[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(tstate->use_tracing)[37m [39;49;00m{[37m[39;49;00m$
  2558^I[37m^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(tstate->c_tracefunc)[37m [39;49;00m{[37m[39;49;00m$
  2559^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(why[37m [39;49;00m==[37m [39;49;00mWHY_RETURN[37m [39;49;00m||[37m [39;49;00mwhy[37m [39;49;00m==[37m [39;49;00mWHY_YIELD)[37m [39;49;00m{[37m[39;49;00m$
  2560^I[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(call_trace(tstate->c_tracefunc,[37m[39;49;00m$
  2561^I[37m^I^I^I^I^I       [39;49;00mtstate->c_traceobj,[37m [39;49;00mf,[37m[39;49;00m$
  2562^I[37m^I^I^I^I^I       [39;49;00mPyTrace_RETURN,[37m [39;49;00mretval))[37m [39;49;00m{[37m[39;49;00m$
  2563^I[37m^I^I^I^I^I[39;49;00mPy_XDECREF(retval);[37m[39;49;00m$
  2564^I[37m^I^I^I^I^I[39;49;00mretval[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  2565^I[37m^I^I^I^I^I[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_EXCEPTION;[37m[39;49;00m$
  2566^I[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
  2567^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  2568^I[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(why[37m [39;49;00m==[37m [39;49;00mWHY_EXCEPTION)[37m [39;49;00m{[37m[39;49;00m$
  2569^I[37m^I^I^I^I[39;49;00mcall_trace_protected(tstate->c_tracefunc,[37m[39;49;00m$
  2570^I[37m^I^I^I^I^I^I     [39;49;00mtstate->c_traceobj,[37m [39;49;00mf,[37m[39;49;00m$
  2571^I[37m^I^I^I^I^I^I     [39;49;00mPyTrace_RETURN,[37m [39;49;00m[36mNULL[39;49;00m);[37m[39;49;00m$
  2572^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  2573^I[37m^I^I[39;49;00m}[37m[39;49;00m$
  2574^I[37m^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(tstate->c_profilefunc)[37m [39;49;00m{[37m[39;49;00m$
  2575^I[37m^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(why[37m [39;49;00m==[37m [39;49;00mWHY_EXCEPTION)[37m[39;49;00m$
  2576^I[37m^I^I^I^I[39;49;00mcall_trace_protected(tstate->c_profilefunc,[37m[39;49;00m$
  2577^I[37m^I^I^I^I^I^I     [39;49;00mtstate->c_profileobj,[37m [39;49;00mf,[37m[39;49;00m$
  2578^I[37m^I^I^I^I^I^I     [39;49;00mPyTrace_RETURN,[37m [39;49;00m[36mNULL[39;49;00m);[37m[39;49;00m$
  2579^I[37m^I^I^I[39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(call_trace(tstate->c_profilefunc,[37m[39;49;00m$
  2580^I[37m^I^I^I^I^I    [39;49;00mtstate->c_profileobj,[37m [39;49;00mf,[37m[39;49;00m$
  2581^I[37m^I^I^I^I^I    [39;49;00mPyTrace_RETURN,[37m [39;49;00mretval))[37m [39;49;00m{[37m[39;49;00m$
  2582^I[37m^I^I^I^I[39;49;00mPy_XDECREF(retval);[37m[39;49;00m$
  2583^I[37m^I^I^I^I[39;49;00mretval[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  2584^I[37m^I^I^I^I[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_EXCEPTION;[37m[39;49;00m$
  2585^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
  2586^I[37m^I^I[39;49;00m}[37m[39;49;00m$
  2587^I[37m^I[39;49;00m}[37m[39;49;00m$
  2588^I[37m[39;49;00m$
  2589^I[37m^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(tstate->frame->f_exc_type[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
  2590^I[37m^I^I[39;49;00mreset_exc_info(tstate);[37m[39;49;00m$
  2591^I[37m^I[39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
  2592^I[37m^I^I[39;49;00massert(tstate->frame->f_exc_value[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m);[37m[39;49;00m$
  2593^I[37m^I^I[39;49;00massert(tstate->frame->f_exc_traceback[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m);[37m[39;49;00m$
  2594^I[37m^I[39;49;00m}[37m[39;49;00m$
  2595^I[37m[39;49;00m$
  2596^I[37m^I[39;49;00m[37m/* pop frame */[39;49;00m[37m[39;49;00m$
  2597^I[37m    [39;49;00mexit_eval_frame:[37m[39;49;00m$
  2598^I[37m^I[39;49;00mPy_LeaveRecursiveCall();[37m[39;49;00m$
  2599^I[37m^I[39;49;00mtstate->frame[37m [39;49;00m=[37m [39;49;00mf->f_back;[37m[39;49;00m$
  2600^I[37m[39;49;00m$
  2601^I[37m^I[39;49;00m[34mreturn[39;49;00m[37m [39;49;00mretval;[37m[39;49;00m$
  2602^I}$

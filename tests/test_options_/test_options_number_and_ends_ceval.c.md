     1	[37m/* Execute compiled code */[39;49;00m[37m[39;49;00m$
     2	[37m[39;49;00m$
     3	[37m/* XXX TO DO:[39;49;00m$
     4	[37m   XXX speed up searching for keywords by using a dictionary[39;49;00m$
     5	[37m   XXX document it![39;49;00m$
     6	[37m   */[39;49;00m[37m[39;49;00m$
     7	[37m[39;49;00m$
     8	[37m/* enable more aggressive intra-module optimizations, where available */[39;49;00m[37m[39;49;00m$
     9	[36m#[39;49;00m[36mdefine PY_LOCAL_AGGRESSIVE[39;49;00m[36m[39;49;00m$
    10	[37m[39;49;00m$
    11	[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"Python.h"[39;49;00m[36m[39;49;00m$
    12	[37m[39;49;00m$
    13	[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"code.h"[39;49;00m[36m[39;49;00m$
    14	[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"frameobject.h"[39;49;00m[36m[39;49;00m$
    15	[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"eval.h"[39;49;00m[36m[39;49;00m$
    16	[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"opcode.h"[39;49;00m[36m[39;49;00m$
    17	[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"structmember.h"[39;49;00m[36m[39;49;00m$
    18	[37m[39;49;00m$
    19	[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<ctype.h>[39;49;00m[36m[39;49;00m$
    20	[37m[39;49;00m$
    21	[36m#[39;49;00m[36mifndef WITH_TSC[39;49;00m[36m[39;49;00m$
    22	[37m[39;49;00m$
    23	[36m#[39;49;00m[36mdefine READ_TIMESTAMP(var)[39;49;00m[36m[39;49;00m$
    24	[37m[39;49;00m$
    25	[36m#[39;49;00m[36melse[39;49;00m[36m[39;49;00m$
    26	[37m[39;49;00m$
    27	[34mtypedef[39;49;00m[37m [39;49;00m[36munsigned[39;49;00m[37m [39;49;00m[36mlong[39;49;00m[37m [39;49;00m[36mlong[39;49;00m[37m [39;49;00muint64;[37m[39;49;00m$
    28	[37m[39;49;00m$
    29	[36m#[39;49;00m[36mif defined(__ppc__) [39;49;00m[37m/* <- Don't know if this is the correct symbol; this[39;49;00m$
    30	[37m			   section should work for GCC on any PowerPC platform,[39;49;00m$
    31	[37m			   irrespective of OS.  POWER?  Who knows :-) */[39;49;00m[36m[39;49;00m$
    32	[37m[39;49;00m$
    33	[36m#[39;49;00m[36mdefine READ_TIMESTAMP(var) ppc_getcounter(&var)[39;49;00m[36m[39;49;00m$
    34	[37m[39;49;00m$
    35	[34mstatic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m[39;49;00m$
    36	[32mppc_getcounter[39;49;00m(uint64[37m [39;49;00m*v)[37m[39;49;00m$
    37	{[37m[39;49;00m$
    38	[37m	[39;49;00m[34mregister[39;49;00m[37m [39;49;00m[36munsigned[39;49;00m[37m [39;49;00m[36mlong[39;49;00m[37m [39;49;00mtbu,[37m [39;49;00mtb,[37m [39;49;00mtbu2;[37m[39;49;00m$
    39	[37m[39;49;00m$
    40	[37m  [39;49;00mloop:[37m[39;49;00m$
    41	[37m	[39;49;00m[34masm[39;49;00m[37m [39;49;00m[34mvolatile[39;49;00m[37m [39;49;00m([33m"[39;49;00m[33mmftbu %0[39;49;00m[33m"[39;49;00m[37m [39;49;00m:[37m [39;49;00m[33m"[39;49;00m[33m=r[39;49;00m[33m"[39;49;00m[37m [39;49;00m(tbu)[37m [39;49;00m);[37m[39;49;00m$
    42	[37m	[39;49;00m[34masm[39;49;00m[37m [39;49;00m[34mvolatile[39;49;00m[37m [39;49;00m([33m"[39;49;00m[33mmftb  %0[39;49;00m[33m"[39;49;00m[37m [39;49;00m:[37m [39;49;00m[33m"[39;49;00m[33m=r[39;49;00m[33m"[39;49;00m[37m [39;49;00m(tb)[37m  [39;49;00m);[37m[39;49;00m$
    43	[37m	[39;49;00m[34masm[39;49;00m[37m [39;49;00m[34mvolatile[39;49;00m[37m [39;49;00m([33m"[39;49;00m[33mmftbu %0[39;49;00m[33m"[39;49;00m[37m [39;49;00m:[37m [39;49;00m[33m"[39;49;00m[33m=r[39;49;00m[33m"[39;49;00m[37m [39;49;00m(tbu2));[37m[39;49;00m$
    44	[37m	[39;49;00m[34mif[39;49;00m[37m [39;49;00m(__builtin_expect(tbu[37m [39;49;00m!=[37m [39;49;00mtbu2,[37m [39;49;00m[34m0[39;49;00m))[37m [39;49;00m[34mgoto[39;49;00m[37m [39;49;00mloop;[37m[39;49;00m$
    45	[37m[39;49;00m$
    46	[37m	[39;49;00m[37m/* The slightly peculiar way of writing the next lines is[39;49;00m$
    47	[37m	   compiled better by GCC than any other way I tried. */[39;49;00m[37m[39;49;00m$
    48	[37m	[39;49;00m(([36mlong[39;49;00m*)(v))[[34m0[39;49;00m][37m [39;49;00m=[37m [39;49;00mtbu;[37m[39;49;00m$
    49	[37m	[39;49;00m(([36mlong[39;49;00m*)(v))[[34m1[39;49;00m][37m [39;49;00m=[37m [39;49;00mtb;[37m[39;49;00m$
    50	}[37m[39;49;00m$
    51	[37m[39;49;00m$
    52	[36m#[39;49;00m[36melse [39;49;00m[37m/* this is for linux/x86 (and probably any other GCC/x86 combo) */[39;49;00m[36m[39;49;00m$
    53	[37m[39;49;00m$
    54	[36m#[39;49;00m[36mdefine READ_TIMESTAMP(val) \[39;49;00m[36m[39;49;00m$
    55	[36m     __asm__ __volatile__("rdtsc" : "=A" (val))[39;49;00m[36m[39;49;00m$
    56	[37m[39;49;00m$
    57	[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
    58	[37m[39;49;00m$
    59	[36mvoid[39;49;00m[37m [39;49;00m[32mdump_tsc[39;49;00m([36mint[39;49;00m[37m [39;49;00mopcode,[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mticked,[37m [39;49;00muint64[37m [39;49;00minst0,[37m [39;49;00muint64[37m [39;49;00minst1,[37m[39;49;00m$
    60	[37m	      [39;49;00muint64[37m [39;49;00mloop0,[37m [39;49;00muint64[37m [39;49;00mloop1,[37m [39;49;00muint64[37m [39;49;00mintr0,[37m [39;49;00muint64[37m [39;49;00mintr1)[37m[39;49;00m$
    61	{[37m[39;49;00m$
    62	[37m	[39;49;00muint64[37m [39;49;00mintr,[37m [39;49;00minst,[37m [39;49;00mloop;[37m[39;49;00m$
    63	[37m	[39;49;00mPyThreadState[37m [39;49;00m*tstate[37m [39;49;00m=[37m [39;49;00mPyThreadState_Get();[37m[39;49;00m$
    64	[37m	[39;49;00m[34mif[39;49;00m[37m [39;49;00m(!tstate->interp->tscdump)[37m[39;49;00m$
    65	[37m		[39;49;00m[34mreturn[39;49;00m;[37m[39;49;00m$
    66	[37m	[39;49;00mintr[37m [39;49;00m=[37m [39;49;00mintr1[37m [39;49;00m-[37m [39;49;00mintr0;[37m[39;49;00m$
    67	[37m	[39;49;00minst[37m [39;49;00m=[37m [39;49;00minst1[37m [39;49;00m-[37m [39;49;00minst0[37m [39;49;00m-[37m [39;49;00mintr;[37m[39;49;00m$
    68	[37m	[39;49;00mloop[37m [39;49;00m=[37m [39;49;00mloop1[37m [39;49;00m-[37m [39;49;00mloop0[37m [39;49;00m-[37m [39;49;00mintr;[37m[39;49;00m$
    69	[37m	[39;49;00mfprintf(stderr,[37m [39;49;00m[33m"[39;49;00m[33mopcode=%03d t=%d inst=%06lld loop=%06lld[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m,[37m[39;49;00m$
    70	[37m		[39;49;00mopcode,[37m [39;49;00mticked,[37m [39;49;00minst,[37m [39;49;00mloop);[37m[39;49;00m$
    71	}[37m[39;49;00m$
    72	[37m[39;49;00m$
    73	[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
    74	[37m[39;49;00m$
    75	[37m/* Turn this on if your compiler chokes on the big switch: */[39;49;00m[37m[39;49;00m$
    76	[37m/* #define CASE_TOO_BIG 1 */[39;49;00m[37m[39;49;00m$
    77	[37m[39;49;00m$
    78	[36m#[39;49;00m[36mifdef Py_DEBUG[39;49;00m[36m[39;49;00m$
    79	[37m/* For debugging the interpreter: */[39;49;00m[37m[39;49;00m$
    80	[36m#[39;49;00m[36mdefine LLTRACE  1	[39;49;00m[37m/* Low-level trace feature */[39;49;00m[36m[39;49;00m$
    81	[36m#[39;49;00m[36mdefine CHECKEXC 1	[39;49;00m[37m/* Double-check exception checking */[39;49;00m[36m[39;49;00m$
    82	[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
    83	[37m[39;49;00m$
    84	[34mtypedef[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*(*callproc)(PyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*);[37m[39;49;00m$
    85	[37m[39;49;00m$
    86	[37m/* Forward declarations */[39;49;00m[37m[39;49;00m$
    87	[36m#[39;49;00m[36mifdef WITH_TSC[39;49;00m[36m[39;49;00m$
    88	[34mstatic[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*[37m [39;49;00m[32mcall_function[39;49;00m(PyObject[37m [39;49;00m***,[37m [39;49;00m[36mint[39;49;00m,[37m [39;49;00muint64*,[37m [39;49;00muint64*);[37m[39;49;00m$
    89	[36m#[39;49;00m[36melse[39;49;00m[36m[39;49;00m$
    90	[34mstatic[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*[37m [39;49;00m[32mcall_function[39;49;00m(PyObject[37m [39;49;00m***,[37m [39;49;00m[36mint[39;49;00m);[37m[39;49;00m$
    91	[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
    92	[34mstatic[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*[37m [39;49;00m[32mfast_function[39;49;00m(PyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m***,[37m [39;49;00m[36mint[39;49;00m,[37m [39;49;00m[36mint[39;49;00m,[37m [39;49;00m[36mint[39;49;00m);[37m[39;49;00m$
    93	[34mstatic[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*[37m [39;49;00m[32mdo_call[39;49;00m(PyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m***,[37m [39;49;00m[36mint[39;49;00m,[37m [39;49;00m[36mint[39;49;00m);[37m[39;49;00m$
    94	[34mstatic[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*[37m [39;49;00m[32mext_do_call[39;49;00m(PyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m***,[37m [39;49;00m[36mint[39;49;00m,[37m [39;49;00m[36mint[39;49;00m,[37m [39;49;00m[36mint[39;49;00m);[37m[39;49;00m$
    95	[34mstatic[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*[37m [39;49;00m[32mupdate_keyword_args[39;49;00m(PyObject[37m [39;49;00m*,[37m [39;49;00m[36mint[39;49;00m,[37m [39;49;00mPyObject[37m [39;49;00m***,PyObject[37m [39;49;00m*);[37m[39;49;00m$
    96	[34mstatic[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*[37m [39;49;00m[32mupdate_star_args[39;49;00m([36mint[39;49;00m,[37m [39;49;00m[36mint[39;49;00m,[37m [39;49;00mPyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m***);[37m[39;49;00m$
    97	[34mstatic[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*[37m [39;49;00m[32mload_args[39;49;00m(PyObject[37m [39;49;00m***,[37m [39;49;00m[36mint[39;49;00m);[37m[39;49;00m$
    98	[36m#[39;49;00m[36mdefine CALL_FLAG_VAR 1[39;49;00m[36m[39;49;00m$
    99	[36m#[39;49;00m[36mdefine CALL_FLAG_KW 2[39;49;00m[36m[39;49;00m$
   100	[37m[39;49;00m$
   101	[36m#[39;49;00m[36mifdef LLTRACE[39;49;00m[36m[39;49;00m$
   102	[34mstatic[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mlltrace;[37m[39;49;00m$
   103	[34mstatic[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00m[32mprtrace[39;49;00m(PyObject[37m [39;49;00m*,[37m [39;49;00m[36mchar[39;49;00m[37m [39;49;00m*);[37m[39;49;00m$
   104	[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   105	[34mstatic[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00m[32mcall_trace[39;49;00m(Py_tracefunc,[37m [39;49;00mPyObject[37m [39;49;00m*,[37m [39;49;00mPyFrameObject[37m [39;49;00m*,[37m[39;49;00m$
   106	[37m		      [39;49;00m[36mint[39;49;00m,[37m [39;49;00mPyObject[37m [39;49;00m*);[37m[39;49;00m$
   107	[34mstatic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mcall_trace_protected[39;49;00m(Py_tracefunc,[37m [39;49;00mPyObject[37m [39;49;00m*,[37m[39;49;00m$
   108	[37m				 [39;49;00mPyFrameObject[37m [39;49;00m*,[37m [39;49;00m[36mint[39;49;00m,[37m [39;49;00mPyObject[37m [39;49;00m*);[37m[39;49;00m$
   109	[34mstatic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mcall_exc_trace[39;49;00m(Py_tracefunc,[37m [39;49;00mPyObject[37m [39;49;00m*,[37m [39;49;00mPyFrameObject[37m [39;49;00m*);[37m[39;49;00m$
   110	[34mstatic[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00m[32mmaybe_call_line_trace[39;49;00m(Py_tracefunc,[37m [39;49;00mPyObject[37m [39;49;00m*,[37m[39;49;00m$
   111	[37m				  [39;49;00mPyFrameObject[37m [39;49;00m*,[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00m*,[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00m*,[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00m*);[37m[39;49;00m$
   112	[37m[39;49;00m$
   113	[34mstatic[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*[37m [39;49;00m[32mapply_slice[39;49;00m(PyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*);[37m[39;49;00m$
   114	[34mstatic[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00m[32massign_slice[39;49;00m(PyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*,[37m[39;49;00m$
   115	[37m			[39;49;00mPyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*);[37m[39;49;00m$
   116	[34mstatic[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*[37m [39;49;00m[32mcmp_outcome[39;49;00m([36mint[39;49;00m,[37m [39;49;00mPyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*);[37m[39;49;00m$
   117	[34mstatic[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*[37m [39;49;00m[32mimport_from[39;49;00m(PyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*);[37m[39;49;00m$
   118	[34mstatic[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00m[32mimport_all_from[39;49;00m(PyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*);[37m[39;49;00m$
   119	[34mstatic[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*[37m [39;49;00m[32mbuild_class[39;49;00m(PyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*);[37m[39;49;00m$
   120	[34mstatic[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00m[32mexec_statement[39;49;00m(PyFrameObject[37m [39;49;00m*,[37m[39;49;00m$
   121	[37m			  [39;49;00mPyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*);[37m[39;49;00m$
   122	[34mstatic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mset_exc_info[39;49;00m(PyThreadState[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*);[37m[39;49;00m$
   123	[34mstatic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mreset_exc_info[39;49;00m(PyThreadState[37m [39;49;00m*);[37m[39;49;00m$
   124	[34mstatic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mformat_exc_check_arg[39;49;00m(PyObject[37m [39;49;00m*,[37m [39;49;00m[36mchar[39;49;00m[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*);[37m[39;49;00m$
   125	[34mstatic[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*[37m [39;49;00m[32mstring_concatenate[39;49;00m(PyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*,[37m[39;49;00m$
   126	[37m				    [39;49;00mPyFrameObject[37m [39;49;00m*,[37m [39;49;00m[36munsigned[39;49;00m[37m [39;49;00m[36mchar[39;49;00m[37m [39;49;00m*);[37m[39;49;00m$
   127	[37m[39;49;00m$
   128	[36m#[39;49;00m[36mdefine NAME_ERROR_MSG \[39;49;00m[36m[39;49;00m$
   129	[36m	"name '%.200s' is not defined"[39;49;00m[36m[39;49;00m$
   130	[36m#[39;49;00m[36mdefine GLOBAL_NAME_ERROR_MSG \[39;49;00m[36m[39;49;00m$
   131	[36m	"global name '%.200s' is not defined"[39;49;00m[36m[39;49;00m$
   132	[36m#[39;49;00m[36mdefine UNBOUNDLOCAL_ERROR_MSG \[39;49;00m[36m[39;49;00m$
   133	[36m	"local variable '%.200s' referenced before assignment"[39;49;00m[36m[39;49;00m$
   134	[36m#[39;49;00m[36mdefine UNBOUNDFREE_ERROR_MSG \[39;49;00m[36m[39;49;00m$
   135	[36m	"free variable '%.200s' referenced before assignment" \[39;49;00m[36m[39;49;00m$
   136	[36m        " in enclosing scope"[39;49;00m[36m[39;49;00m$
   137	[37m[39;49;00m$
   138	[37m/* Dynamic execution profile */[39;49;00m[37m[39;49;00m$
   139	[36m#[39;49;00m[36mifdef DYNAMIC_EXECUTION_PROFILE[39;49;00m[36m[39;49;00m$
   140	[36m#[39;49;00m[36mifdef DXPAIRS[39;49;00m[36m[39;49;00m$
   141	[34mstatic[39;49;00m[37m [39;49;00m[36mlong[39;49;00m[37m [39;49;00mdxpairs[[34m257[39;49;00m][[34m256[39;49;00m];[37m[39;49;00m$
   142	[36m#[39;49;00m[36mdefine dxp dxpairs[256][39;49;00m[36m[39;49;00m$
   143	[36m#[39;49;00m[36melse[39;49;00m[36m[39;49;00m$
   144	[34mstatic[39;49;00m[37m [39;49;00m[36mlong[39;49;00m[37m [39;49;00mdxp[[34m256[39;49;00m];[37m[39;49;00m$
   145	[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   146	[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   147	[37m[39;49;00m$
   148	[37m/* Function call profile */[39;49;00m[37m[39;49;00m$
   149	[36m#[39;49;00m[36mifdef CALL_PROFILE[39;49;00m[36m[39;49;00m$
   150	[36m#[39;49;00m[36mdefine PCALL_NUM 11[39;49;00m[36m[39;49;00m$
   151	[34mstatic[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mpcall[PCALL_NUM];[37m[39;49;00m$
   152	[37m[39;49;00m$
   153	[36m#[39;49;00m[36mdefine PCALL_ALL 0[39;49;00m[36m[39;49;00m$
   154	[36m#[39;49;00m[36mdefine PCALL_FUNCTION 1[39;49;00m[36m[39;49;00m$
   155	[36m#[39;49;00m[36mdefine PCALL_FAST_FUNCTION 2[39;49;00m[36m[39;49;00m$
   156	[36m#[39;49;00m[36mdefine PCALL_FASTER_FUNCTION 3[39;49;00m[36m[39;49;00m$
   157	[36m#[39;49;00m[36mdefine PCALL_METHOD 4[39;49;00m[36m[39;49;00m$
   158	[36m#[39;49;00m[36mdefine PCALL_BOUND_METHOD 5[39;49;00m[36m[39;49;00m$
   159	[36m#[39;49;00m[36mdefine PCALL_CFUNCTION 6[39;49;00m[36m[39;49;00m$
   160	[36m#[39;49;00m[36mdefine PCALL_TYPE 7[39;49;00m[36m[39;49;00m$
   161	[36m#[39;49;00m[36mdefine PCALL_GENERATOR 8[39;49;00m[36m[39;49;00m$
   162	[36m#[39;49;00m[36mdefine PCALL_OTHER 9[39;49;00m[36m[39;49;00m$
   163	[36m#[39;49;00m[36mdefine PCALL_POP 10[39;49;00m[36m[39;49;00m$
   164	[37m[39;49;00m$
   165	[37m/* Notes about the statistics[39;49;00m$
   166	[37m[39;49;00m$
   167	[37m   PCALL_FAST stats[39;49;00m$
   168	[37m[39;49;00m$
   169	[37m   FAST_FUNCTION means no argument tuple needs to be created.[39;49;00m$
   170	[37m   FASTER_FUNCTION means that the fast-path frame setup code is used.[39;49;00m$
   171	[37m[39;49;00m$
   172	[37m   If there is a method call where the call can be optimized by changing[39;49;00m$
   173	[37m   the argument tuple and calling the function directly, it gets recorded[39;49;00m$
   174	[37m   twice.[39;49;00m$
   175	[37m[39;49;00m$
   176	[37m   As a result, the relationship among the statistics appears to be[39;49;00m$
   177	[37m   PCALL_ALL == PCALL_FUNCTION + PCALL_METHOD - PCALL_BOUND_METHOD +[39;49;00m$
   178	[37m                PCALL_CFUNCTION + PCALL_TYPE + PCALL_GENERATOR + PCALL_OTHER[39;49;00m$
   179	[37m   PCALL_FUNCTION > PCALL_FAST_FUNCTION > PCALL_FASTER_FUNCTION[39;49;00m$
   180	[37m   PCALL_METHOD > PCALL_BOUND_METHOD[39;49;00m$
   181	[37m*/[39;49;00m[37m[39;49;00m$
   182	[37m[39;49;00m$
   183	[36m#[39;49;00m[36mdefine PCALL(POS) pcall[POS]++[39;49;00m[36m[39;49;00m$
   184	[37m[39;49;00m$
   185	PyObject[37m [39;49;00m*[37m[39;49;00m$
   186	[32mPyEval_GetCallStats[39;49;00m(PyObject[37m [39;49;00m*self)[37m[39;49;00m$
   187	{[37m[39;49;00m$
   188	[37m	[39;49;00m[34mreturn[39;49;00m[37m [39;49;00mPy_BuildValue([33m"[39;49;00m[33miiiiiiiiii[39;49;00m[33m"[39;49;00m,[37m[39;49;00m$
   189	[37m			     [39;49;00mpcall[[34m0[39;49;00m],[37m [39;49;00mpcall[[34m1[39;49;00m],[37m [39;49;00mpcall[[34m2[39;49;00m],[37m [39;49;00mpcall[[34m3[39;49;00m],[37m[39;49;00m$
   190	[37m			     [39;49;00mpcall[[34m4[39;49;00m],[37m [39;49;00mpcall[[34m5[39;49;00m],[37m [39;49;00mpcall[[34m6[39;49;00m],[37m [39;49;00mpcall[[34m7[39;49;00m],[37m[39;49;00m$
   191	[37m			     [39;49;00mpcall[[34m8[39;49;00m],[37m [39;49;00mpcall[[34m9[39;49;00m]);[37m[39;49;00m$
   192	}[37m[39;49;00m$
   193	[36m#[39;49;00m[36melse[39;49;00m[36m[39;49;00m$
   194	[36m#[39;49;00m[36mdefine PCALL(O)[39;49;00m[36m[39;49;00m$
   195	[37m[39;49;00m$
   196	PyObject[37m [39;49;00m*[37m[39;49;00m$
   197	[32mPyEval_GetCallStats[39;49;00m(PyObject[37m [39;49;00m*self)[37m[39;49;00m$
   198	{[37m[39;49;00m$
   199	[37m	[39;49;00mPy_INCREF(Py_None);[37m[39;49;00m$
   200	[37m	[39;49;00m[34mreturn[39;49;00m[37m [39;49;00mPy_None;[37m[39;49;00m$
   201	}[37m[39;49;00m$
   202	[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   203	[37m[39;49;00m$
   204	[37m[39;49;00m$
   205	[36m#[39;49;00m[36mifdef WITH_THREAD[39;49;00m[36m[39;49;00m$
   206	[37m[39;49;00m$
   207	[36m#[39;49;00m[36mifdef HAVE_ERRNO_H[39;49;00m[36m[39;49;00m$
   208	[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<errno.h>[39;49;00m[36m[39;49;00m$
   209	[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   210	[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"pythread.h"[39;49;00m[36m[39;49;00m$
   211	[37m[39;49;00m$
   212	[34mstatic[39;49;00m[37m [39;49;00mPyThread_type_lock[37m [39;49;00minterpreter_lock[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m [39;49;00m[37m/* This is the GIL */[39;49;00m[37m[39;49;00m$
   213	[34mstatic[39;49;00m[37m [39;49;00m[36mlong[39;49;00m[37m [39;49;00mmain_thread[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   214	[37m[39;49;00m$
   215	[36mint[39;49;00m[37m[39;49;00m$
   216	[32mPyEval_ThreadsInitialized[39;49;00m([36mvoid[39;49;00m)[37m[39;49;00m$
   217	{[37m[39;49;00m$
   218	[37m	[39;49;00m[34mreturn[39;49;00m[37m [39;49;00minterpreter_lock[37m [39;49;00m!=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   219	}[37m[39;49;00m$
   220	[37m[39;49;00m$
   221	[36mvoid[39;49;00m[37m[39;49;00m$
   222	[32mPyEval_InitThreads[39;49;00m([36mvoid[39;49;00m)[37m[39;49;00m$
   223	{[37m[39;49;00m$
   224	[37m	[39;49;00m[34mif[39;49;00m[37m [39;49;00m(interpreter_lock)[37m[39;49;00m$
   225	[37m		[39;49;00m[34mreturn[39;49;00m;[37m[39;49;00m$
   226	[37m	[39;49;00minterpreter_lock[37m [39;49;00m=[37m [39;49;00mPyThread_allocate_lock();[37m[39;49;00m$
   227	[37m	[39;49;00mPyThread_acquire_lock(interpreter_lock,[37m [39;49;00m[34m1[39;49;00m);[37m[39;49;00m$
   228	[37m	[39;49;00mmain_thread[37m [39;49;00m=[37m [39;49;00mPyThread_get_thread_ident();[37m[39;49;00m$
   229	}[37m[39;49;00m$
   230	[37m[39;49;00m$
   231	[36mvoid[39;49;00m[37m[39;49;00m$
   232	[32mPyEval_AcquireLock[39;49;00m([36mvoid[39;49;00m)[37m[39;49;00m$
   233	{[37m[39;49;00m$
   234	[37m	[39;49;00mPyThread_acquire_lock(interpreter_lock,[37m [39;49;00m[34m1[39;49;00m);[37m[39;49;00m$
   235	}[37m[39;49;00m$
   236	[37m[39;49;00m$
   237	[36mvoid[39;49;00m[37m[39;49;00m$
   238	[32mPyEval_ReleaseLock[39;49;00m([36mvoid[39;49;00m)[37m[39;49;00m$
   239	{[37m[39;49;00m$
   240	[37m	[39;49;00mPyThread_release_lock(interpreter_lock);[37m[39;49;00m$
   241	}[37m[39;49;00m$
   242	[37m[39;49;00m$
   243	[36mvoid[39;49;00m[37m[39;49;00m$
   244	[32mPyEval_AcquireThread[39;49;00m(PyThreadState[37m [39;49;00m*tstate)[37m[39;49;00m$
   245	{[37m[39;49;00m$
   246	[37m	[39;49;00m[34mif[39;49;00m[37m [39;49;00m(tstate[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
   247	[37m		[39;49;00mPy_FatalError([33m"[39;49;00m[33mPyEval_AcquireThread: NULL new thread state[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
   248	[37m	[39;49;00m[37m/* Check someone has called PyEval_InitThreads() to create the lock */[39;49;00m[37m[39;49;00m$
   249	[37m	[39;49;00massert(interpreter_lock);[37m[39;49;00m$
   250	[37m	[39;49;00mPyThread_acquire_lock(interpreter_lock,[37m [39;49;00m[34m1[39;49;00m);[37m[39;49;00m$
   251	[37m	[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyThreadState_Swap(tstate)[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
   252	[37m		[39;49;00mPy_FatalError([37m[39;49;00m$
   253	[37m			[39;49;00m[33m"[39;49;00m[33mPyEval_AcquireThread: non-NULL old thread state[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
   254	}[37m[39;49;00m$
   255	[37m[39;49;00m$
   256	[36mvoid[39;49;00m[37m[39;49;00m$
   257	[32mPyEval_ReleaseThread[39;49;00m(PyThreadState[37m [39;49;00m*tstate)[37m[39;49;00m$
   258	{[37m[39;49;00m$
   259	[37m	[39;49;00m[34mif[39;49;00m[37m [39;49;00m(tstate[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
   260	[37m		[39;49;00mPy_FatalError([33m"[39;49;00m[33mPyEval_ReleaseThread: NULL thread state[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
   261	[37m	[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyThreadState_Swap([36mNULL[39;49;00m)[37m [39;49;00m!=[37m [39;49;00mtstate)[37m[39;49;00m$
   262	[37m		[39;49;00mPy_FatalError([33m"[39;49;00m[33mPyEval_ReleaseThread: wrong thread state[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
   263	[37m	[39;49;00mPyThread_release_lock(interpreter_lock);[37m[39;49;00m$
   264	}[37m[39;49;00m$
   265	[37m[39;49;00m$
   266	[37m/* This function is called from PyOS_AfterFork to ensure that newly[39;49;00m$
   267	[37m   created child processes don't hold locks referring to threads which[39;49;00m$
   268	[37m   are not running in the child process.  (This could also be done using[39;49;00m$
   269	[37m   pthread_atfork mechanism, at least for the pthreads implementation.) */[39;49;00m[37m[39;49;00m$
   270	[37m[39;49;00m$
   271	[36mvoid[39;49;00m[37m[39;49;00m$
   272	[32mPyEval_ReInitThreads[39;49;00m([36mvoid[39;49;00m)[37m[39;49;00m$
   273	{[37m[39;49;00m$
   274	[37m	[39;49;00m[34mif[39;49;00m[37m [39;49;00m(!interpreter_lock)[37m[39;49;00m$
   275	[37m		[39;49;00m[34mreturn[39;49;00m;[37m[39;49;00m$
   276	[37m	[39;49;00m[37m/*XXX Can't use PyThread_free_lock here because it does too[39;49;00m$
   277	[37m	  much error-checking.  Doing this cleanly would require[39;49;00m$
   278	[37m	  adding a new function to each thread_*.h.  Instead, just[39;49;00m$
   279	[37m	  create a new lock and waste a little bit of memory */[39;49;00m[37m[39;49;00m$
   280	[37m	[39;49;00minterpreter_lock[37m [39;49;00m=[37m [39;49;00mPyThread_allocate_lock();[37m[39;49;00m$
   281	[37m	[39;49;00mPyThread_acquire_lock(interpreter_lock,[37m [39;49;00m[34m1[39;49;00m);[37m[39;49;00m$
   282	[37m	[39;49;00mmain_thread[37m [39;49;00m=[37m [39;49;00mPyThread_get_thread_ident();[37m[39;49;00m$
   283	}[37m[39;49;00m$
   284	[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   285	[37m[39;49;00m$
   286	[37m/* Functions save_thread and restore_thread are always defined so[39;49;00m$
   287	[37m   dynamically loaded modules needn't be compiled separately for use[39;49;00m$
   288	[37m   with and without threads: */[39;49;00m[37m[39;49;00m$
   289	[37m[39;49;00m$
   290	PyThreadState[37m [39;49;00m*[37m[39;49;00m$
   291	[32mPyEval_SaveThread[39;49;00m([36mvoid[39;49;00m)[37m[39;49;00m$
   292	{[37m[39;49;00m$
   293	[37m	[39;49;00mPyThreadState[37m [39;49;00m*tstate[37m [39;49;00m=[37m [39;49;00mPyThreadState_Swap([36mNULL[39;49;00m);[37m[39;49;00m$
   294	[37m	[39;49;00m[34mif[39;49;00m[37m [39;49;00m(tstate[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
   295	[37m		[39;49;00mPy_FatalError([33m"[39;49;00m[33mPyEval_SaveThread: NULL tstate[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
   296	[36m#[39;49;00m[36mifdef WITH_THREAD[39;49;00m[36m[39;49;00m$
   297	[37m	[39;49;00m[34mif[39;49;00m[37m [39;49;00m(interpreter_lock)[37m[39;49;00m$
   298	[37m		[39;49;00mPyThread_release_lock(interpreter_lock);[37m[39;49;00m$
   299	[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   300	[37m	[39;49;00m[34mreturn[39;49;00m[37m [39;49;00mtstate;[37m[39;49;00m$
   301	}[37m[39;49;00m$
   302	[37m[39;49;00m$
   303	[36mvoid[39;49;00m[37m[39;49;00m$
   304	[32mPyEval_RestoreThread[39;49;00m(PyThreadState[37m [39;49;00m*tstate)[37m[39;49;00m$
   305	{[37m[39;49;00m$
   306	[37m	[39;49;00m[34mif[39;49;00m[37m [39;49;00m(tstate[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
   307	[37m		[39;49;00mPy_FatalError([33m"[39;49;00m[33mPyEval_RestoreThread: NULL tstate[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
   308	[36m#[39;49;00m[36mifdef WITH_THREAD[39;49;00m[36m[39;49;00m$
   309	[37m	[39;49;00m[34mif[39;49;00m[37m [39;49;00m(interpreter_lock)[37m [39;49;00m{[37m[39;49;00m$
   310	[37m		[39;49;00m[36mint[39;49;00m[37m [39;49;00merr[37m [39;49;00m=[37m [39;49;00merrno;[37m[39;49;00m$
   311	[37m		[39;49;00mPyThread_acquire_lock(interpreter_lock,[37m [39;49;00m[34m1[39;49;00m);[37m[39;49;00m$
   312	[37m		[39;49;00merrno[37m [39;49;00m=[37m [39;49;00merr;[37m[39;49;00m$
   313	[37m	[39;49;00m}[37m[39;49;00m$
   314	[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   315	[37m	[39;49;00mPyThreadState_Swap(tstate);[37m[39;49;00m$
   316	}[37m[39;49;00m$
   317	[37m[39;49;00m$
   318	[37m[39;49;00m$
   319	[37m/* Mechanism whereby asynchronously executing callbacks (e.g. UNIX[39;49;00m$
   320	[37m   signal handlers or Mac I/O completion routines) can schedule calls[39;49;00m$
   321	[37m   to a function to be called synchronously.[39;49;00m$
   322	[37m   The synchronous function is called with one void* argument.[39;49;00m$
   323	[37m   It should return 0 for success or -1 for failure -- failure should[39;49;00m$
   324	[37m   be accompanied by an exception.[39;49;00m$
   325	[37m[39;49;00m$
   326	[37m   If registry succeeds, the registry function returns 0; if it fails[39;49;00m$
   327	[37m   (e.g. due to too many pending calls) it returns -1 (without setting[39;49;00m$
   328	[37m   an exception condition).[39;49;00m$
   329	[37m[39;49;00m$
   330	[37m   Note that because registry may occur from within signal handlers,[39;49;00m$
   331	[37m   or other asynchronous events, calling malloc() is unsafe![39;49;00m$
   332	[37m[39;49;00m$
   333	[37m#ifdef WITH_THREAD[39;49;00m$
   334	[37m   Any thread can schedule pending calls, but only the main thread[39;49;00m$
   335	[37m   will execute them.[39;49;00m$
   336	[37m#endif[39;49;00m$
   337	[37m[39;49;00m$
   338	[37m   XXX WARNING!  ASYNCHRONOUSLY EXECUTING CODE![39;49;00m$
   339	[37m   There are two possible race conditions:[39;49;00m$
   340	[37m   (1) nested asynchronous registry calls;[39;49;00m$
   341	[37m   (2) registry calls made while pending calls are being processed.[39;49;00m$
   342	[37m   While (1) is very unlikely, (2) is a real possibility.[39;49;00m$
   343	[37m   The current code is safe against (2), but not against (1).[39;49;00m$
   344	[37m   The safety against (2) is derived from the fact that only one[39;49;00m$
   345	[37m   thread (the main thread) ever takes things out of the queue.[39;49;00m$
   346	[37m[39;49;00m$
   347	[37m   XXX Darn!  With the advent of thread state, we should have an array[39;49;00m$
   348	[37m   of pending calls per thread in the thread state!  Later...[39;49;00m$
   349	[37m*/[39;49;00m[37m[39;49;00m$
   350	[37m[39;49;00m$
   351	[36m#[39;49;00m[36mdefine NPENDINGCALLS 32[39;49;00m[36m[39;49;00m$
   352	[34mstatic[39;49;00m[37m [39;49;00m[34mstruct[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
   353	[37m	[39;49;00m[36mint[39;49;00m[37m [39;49;00m(*func)([36mvoid[39;49;00m[37m [39;49;00m*);[37m[39;49;00m$
   354	[37m	[39;49;00m[36mvoid[39;49;00m[37m [39;49;00m*arg;[37m[39;49;00m$
   355	}[37m [39;49;00mpendingcalls[NPENDINGCALLS];[37m[39;49;00m$
   356	[34mstatic[39;49;00m[37m [39;49;00m[34mvolatile[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mpendingfirst[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   357	[34mstatic[39;49;00m[37m [39;49;00m[34mvolatile[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mpendinglast[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   358	[34mstatic[39;49;00m[37m [39;49;00m[34mvolatile[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mthings_to_do[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   359	[37m[39;49;00m$
   360	[36mint[39;49;00m[37m[39;49;00m$
   361	[32mPy_AddPendingCall[39;49;00m([36mint[39;49;00m[37m [39;49;00m(*func)([36mvoid[39;49;00m[37m [39;49;00m*),[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m*arg)[37m[39;49;00m$
   362	{[37m[39;49;00m$
   363	[37m	[39;49;00m[34mstatic[39;49;00m[37m [39;49;00m[34mvolatile[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mbusy[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   364	[37m	[39;49;00m[36mint[39;49;00m[37m [39;49;00mi,[37m [39;49;00mj;[37m[39;49;00m$
   365	[37m	[39;49;00m[37m/* XXX Begin critical section */[39;49;00m[37m[39;49;00m$
   366	[37m	[39;49;00m[37m/* XXX If you want this to be safe against nested[39;49;00m$
   367	[37m	   XXX asynchronous calls, you'll have to work harder! */[39;49;00m[37m[39;49;00m$
   368	[37m	[39;49;00m[34mif[39;49;00m[37m [39;49;00m(busy)[37m[39;49;00m$
   369	[37m		[39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34m-1[39;49;00m;[37m[39;49;00m$
   370	[37m	[39;49;00mbusy[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
   371	[37m	[39;49;00mi[37m [39;49;00m=[37m [39;49;00mpendinglast;[37m[39;49;00m$
   372	[37m	[39;49;00mj[37m [39;49;00m=[37m [39;49;00m(i[37m [39;49;00m+[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m%[37m [39;49;00mNPENDINGCALLS;[37m[39;49;00m$
   373	[37m	[39;49;00m[34mif[39;49;00m[37m [39;49;00m(j[37m [39;49;00m==[37m [39;49;00mpendingfirst)[37m [39;49;00m{[37m[39;49;00m$
   374	[37m		[39;49;00mbusy[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   375	[37m		[39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34m-1[39;49;00m;[37m [39;49;00m[37m/* Queue full */[39;49;00m[37m[39;49;00m$
   376	[37m	[39;49;00m}[37m[39;49;00m$
   377	[37m	[39;49;00mpendingcalls[i].func[37m [39;49;00m=[37m [39;49;00mfunc;[37m[39;49;00m$
   378	[37m	[39;49;00mpendingcalls[i].arg[37m [39;49;00m=[37m [39;49;00marg;[37m[39;49;00m$
   379	[37m	[39;49;00mpendinglast[37m [39;49;00m=[37m [39;49;00mj;[37m[39;49;00m$
   380	[37m[39;49;00m$
   381	[37m	[39;49;00m_Py_Ticker[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   382	[37m	[39;49;00mthings_to_do[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m;[37m [39;49;00m[37m/* Signal main loop */[39;49;00m[37m[39;49;00m$
   383	[37m	[39;49;00mbusy[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   384	[37m	[39;49;00m[37m/* XXX End critical section */[39;49;00m[37m[39;49;00m$
   385	[37m	[39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   386	}[37m[39;49;00m$
   387	[37m[39;49;00m$
   388	[36mint[39;49;00m[37m[39;49;00m$
   389	[32mPy_MakePendingCalls[39;49;00m([36mvoid[39;49;00m)[37m[39;49;00m$
   390	{[37m[39;49;00m$
   391	[37m	[39;49;00m[34mstatic[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mbusy[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   392	[36m#[39;49;00m[36mifdef WITH_THREAD[39;49;00m[36m[39;49;00m$
   393	[37m	[39;49;00m[34mif[39;49;00m[37m [39;49;00m(main_thread[37m [39;49;00m&&[37m [39;49;00mPyThread_get_thread_ident()[37m [39;49;00m!=[37m [39;49;00mmain_thread)[37m[39;49;00m$
   394	[37m		[39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   395	[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   396	[37m	[39;49;00m[34mif[39;49;00m[37m [39;49;00m(busy)[37m[39;49;00m$
   397	[37m		[39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   398	[37m	[39;49;00mbusy[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
   399	[37m	[39;49;00mthings_to_do[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   400	[37m	[39;49;00m[34mfor[39;49;00m[37m [39;49;00m(;;)[37m [39;49;00m{[37m[39;49;00m$
   401	[37m		[39;49;00m[36mint[39;49;00m[37m [39;49;00mi;[37m[39;49;00m$
   402	[37m		[39;49;00m[36mint[39;49;00m[37m [39;49;00m(*func)([36mvoid[39;49;00m[37m [39;49;00m*);[37m[39;49;00m$
   403	[37m		[39;49;00m[36mvoid[39;49;00m[37m [39;49;00m*arg;[37m[39;49;00m$
   404	[37m		[39;49;00mi[37m [39;49;00m=[37m [39;49;00mpendingfirst;[37m[39;49;00m$
   405	[37m		[39;49;00m[34mif[39;49;00m[37m [39;49;00m(i[37m [39;49;00m==[37m [39;49;00mpendinglast)[37m[39;49;00m$
   406	[37m			[39;49;00m[34mbreak[39;49;00m;[37m [39;49;00m[37m/* Queue empty */[39;49;00m[37m[39;49;00m$
   407	[37m		[39;49;00mfunc[37m [39;49;00m=[37m [39;49;00mpendingcalls[i].func;[37m[39;49;00m$
   408	[37m		[39;49;00marg[37m [39;49;00m=[37m [39;49;00mpendingcalls[i].arg;[37m[39;49;00m$
   409	[37m		[39;49;00mpendingfirst[37m [39;49;00m=[37m [39;49;00m(i[37m [39;49;00m+[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m%[37m [39;49;00mNPENDINGCALLS;[37m[39;49;00m$
   410	[37m		[39;49;00m[34mif[39;49;00m[37m [39;49;00m(func(arg)[37m [39;49;00m<[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
   411	[37m			[39;49;00mbusy[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   412	[37m			[39;49;00mthings_to_do[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m;[37m [39;49;00m[37m/* We're not done yet */[39;49;00m[37m[39;49;00m$
   413	[37m			[39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34m-1[39;49;00m;[37m[39;49;00m$
   414	[37m		[39;49;00m}[37m[39;49;00m$
   415	[37m	[39;49;00m}[37m[39;49;00m$
   416	[37m	[39;49;00mbusy[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   417	[37m	[39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   418	}[37m[39;49;00m$
   419	[37m[39;49;00m$
   420	[37m[39;49;00m$
   421	[37m/* The interpreter's recursion limit */[39;49;00m[37m[39;49;00m$
   422	[37m[39;49;00m$
   423	[36m#[39;49;00m[36mifndef Py_DEFAULT_RECURSION_LIMIT[39;49;00m[36m[39;49;00m$
   424	[36m#[39;49;00m[36mdefine Py_DEFAULT_RECURSION_LIMIT 1000[39;49;00m[36m[39;49;00m$
   425	[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   426	[34mstatic[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mrecursion_limit[37m [39;49;00m=[37m [39;49;00mPy_DEFAULT_RECURSION_LIMIT;[37m[39;49;00m$
   427	[36mint[39;49;00m[37m [39;49;00m_Py_CheckRecursionLimit[37m [39;49;00m=[37m [39;49;00mPy_DEFAULT_RECURSION_LIMIT;[37m[39;49;00m$
   428	[37m[39;49;00m$
   429	[36mint[39;49;00m[37m[39;49;00m$
   430	[32mPy_GetRecursionLimit[39;49;00m([36mvoid[39;49;00m)[37m[39;49;00m$
   431	{[37m[39;49;00m$
   432	[37m	[39;49;00m[34mreturn[39;49;00m[37m [39;49;00mrecursion_limit;[37m[39;49;00m$
   433	}[37m[39;49;00m$
   434	[37m[39;49;00m$
   435	[36mvoid[39;49;00m[37m[39;49;00m$
   436	[32mPy_SetRecursionLimit[39;49;00m([36mint[39;49;00m[37m [39;49;00mnew_limit)[37m[39;49;00m$
   437	{[37m[39;49;00m$
   438	[37m	[39;49;00mrecursion_limit[37m [39;49;00m=[37m [39;49;00mnew_limit;[37m[39;49;00m$
   439	[37m        [39;49;00m_Py_CheckRecursionLimit[37m [39;49;00m=[37m [39;49;00mrecursion_limit;[37m[39;49;00m$
   440	}[37m[39;49;00m$
   441	[37m[39;49;00m$
   442	[37m/* the macro Py_EnterRecursiveCall() only calls _Py_CheckRecursiveCall()[39;49;00m$
   443	[37m   if the recursion_depth reaches _Py_CheckRecursionLimit.[39;49;00m$
   444	[37m   If USE_STACKCHECK, the macro decrements _Py_CheckRecursionLimit[39;49;00m$
   445	[37m   to guarantee that _Py_CheckRecursiveCall() is regularly called.[39;49;00m$
   446	[37m   Without USE_STACKCHECK, there is no need for this. */[39;49;00m[37m[39;49;00m$
   447	[36mint[39;49;00m[37m[39;49;00m$
   448	[32m_Py_CheckRecursiveCall[39;49;00m([36mchar[39;49;00m[37m [39;49;00m*where)[37m[39;49;00m$
   449	{[37m[39;49;00m$
   450	[37m	[39;49;00mPyThreadState[37m [39;49;00m*tstate[37m [39;49;00m=[37m [39;49;00mPyThreadState_GET();[37m[39;49;00m$
   451	[37m[39;49;00m$
   452	[36m#[39;49;00m[36mifdef USE_STACKCHECK[39;49;00m[36m[39;49;00m$
   453	[37m	[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyOS_CheckStack())[37m [39;49;00m{[37m[39;49;00m$
   454	[37m		[39;49;00m--tstate->recursion_depth;[37m[39;49;00m$
   455	[37m		[39;49;00mPyErr_SetString(PyExc_MemoryError,[37m [39;49;00m[33m"[39;49;00m[33mStack overflow[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
   456	[37m		[39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34m-1[39;49;00m;[37m[39;49;00m$
   457	[37m	[39;49;00m}[37m[39;49;00m$
   458	[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   459	[37m	[39;49;00m[34mif[39;49;00m[37m [39;49;00m(tstate->recursion_depth[37m [39;49;00m>[37m [39;49;00mrecursion_limit)[37m [39;49;00m{[37m[39;49;00m$
   460	[37m		[39;49;00m--tstate->recursion_depth;[37m[39;49;00m$
   461	[37m		[39;49;00mPyErr_Format(PyExc_RuntimeError,[37m[39;49;00m$
   462	[37m			     [39;49;00m[33m"[39;49;00m[33mmaximum recursion depth exceeded%s[39;49;00m[33m"[39;49;00m,[37m[39;49;00m$
   463	[37m			     [39;49;00mwhere);[37m[39;49;00m$
   464	[37m		[39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34m-1[39;49;00m;[37m[39;49;00m$
   465	[37m	[39;49;00m}[37m[39;49;00m$
   466	[37m        [39;49;00m_Py_CheckRecursionLimit[37m [39;49;00m=[37m [39;49;00mrecursion_limit;[37m[39;49;00m$
   467	[37m	[39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   468	}[37m[39;49;00m$
   469	[37m[39;49;00m$
   470	[37m/* Status code for main loop (reason for stack unwind) */[39;49;00m[37m[39;49;00m$
   471	[34menum[39;49;00m[37m [39;49;00mwhy_code[37m [39;49;00m{[37m[39;49;00m$
   472	[37m		[39;49;00mWHY_NOT[37m [39;49;00m=[37m	[39;49;00m[34m0x0001[39;49;00m,[37m	[39;49;00m[37m/* No error */[39;49;00m[37m[39;49;00m$
   473	[37m		[39;49;00mWHY_EXCEPTION[37m [39;49;00m=[37m [39;49;00m[34m0x0002[39;49;00m,[37m	[39;49;00m[37m/* Exception occurred */[39;49;00m[37m[39;49;00m$
   474	[37m		[39;49;00mWHY_RERAISE[37m [39;49;00m=[37m	[39;49;00m[34m0x0004[39;49;00m,[37m	[39;49;00m[37m/* Exception re-raised by 'finally' */[39;49;00m[37m[39;49;00m$
   475	[37m		[39;49;00mWHY_RETURN[37m [39;49;00m=[37m	[39;49;00m[34m0x0008[39;49;00m,[37m	[39;49;00m[37m/* 'return' statement */[39;49;00m[37m[39;49;00m$
   476	[37m		[39;49;00mWHY_BREAK[37m [39;49;00m=[37m	[39;49;00m[34m0x0010[39;49;00m,[37m	[39;49;00m[37m/* 'break' statement */[39;49;00m[37m[39;49;00m$
   477	[37m		[39;49;00mWHY_CONTINUE[37m [39;49;00m=[37m	[39;49;00m[34m0x0020[39;49;00m,[37m	[39;49;00m[37m/* 'continue' statement */[39;49;00m[37m[39;49;00m$
   478	[37m		[39;49;00mWHY_YIELD[37m [39;49;00m=[37m	[39;49;00m[34m0x0040[39;49;00m[37m	[39;49;00m[37m/* 'yield' operator */[39;49;00m[37m[39;49;00m$
   479	};[37m[39;49;00m$
   480	[37m[39;49;00m$
   481	[34mstatic[39;49;00m[37m [39;49;00m[34menum[39;49;00m[37m [39;49;00mwhy_code[37m [39;49;00m[32mdo_raise[39;49;00m(PyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*,[37m [39;49;00mPyObject[37m [39;49;00m*);[37m[39;49;00m$
   482	[34mstatic[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00m[32munpack_iterable[39;49;00m(PyObject[37m [39;49;00m*,[37m [39;49;00m[36mint[39;49;00m,[37m [39;49;00mPyObject[37m [39;49;00m**);[37m[39;49;00m$
   483	[37m[39;49;00m$
   484	[37m/* for manipulating the thread switch and periodic "stuff" - used to be[39;49;00m$
   485	[37m   per thread, now just a pair o' globals */[39;49;00m[37m[39;49;00m$
   486	[36mint[39;49;00m[37m [39;49;00m_Py_CheckInterval[37m [39;49;00m=[37m [39;49;00m[34m100[39;49;00m;[37m[39;49;00m$
   487	[34mvolatile[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00m_Py_Ticker[37m [39;49;00m=[37m [39;49;00m[34m100[39;49;00m;[37m[39;49;00m$
   488	[37m[39;49;00m$
   489	PyObject[37m [39;49;00m*[37m[39;49;00m$
   490	[32mPyEval_EvalCode[39;49;00m(PyCodeObject[37m [39;49;00m*co,[37m [39;49;00mPyObject[37m [39;49;00m*globals,[37m [39;49;00mPyObject[37m [39;49;00m*locals)[37m[39;49;00m$
   491	{[37m[39;49;00m$
   492	[37m	[39;49;00m[37m/* XXX raise SystemError if globals is NULL */[39;49;00m[37m[39;49;00m$
   493	[37m	[39;49;00m[34mreturn[39;49;00m[37m [39;49;00mPyEval_EvalCodeEx(co,[37m[39;49;00m$
   494	[37m			  [39;49;00mglobals,[37m [39;49;00mlocals,[37m[39;49;00m$
   495	[37m			  [39;49;00m(PyObject[37m [39;49;00m**)[36mNULL[39;49;00m,[37m [39;49;00m[34m0[39;49;00m,[37m[39;49;00m$
   496	[37m			  [39;49;00m(PyObject[37m [39;49;00m**)[36mNULL[39;49;00m,[37m [39;49;00m[34m0[39;49;00m,[37m[39;49;00m$
   497	[37m			  [39;49;00m(PyObject[37m [39;49;00m**)[36mNULL[39;49;00m,[37m [39;49;00m[34m0[39;49;00m,[37m[39;49;00m$
   498	[37m			  [39;49;00m[36mNULL[39;49;00m);[37m[39;49;00m$
   499	}[37m[39;49;00m$
   500	[37m[39;49;00m$
   501	[37m[39;49;00m$
   502	[37m/* Interpreter main loop */[39;49;00m[37m[39;49;00m$
   503	[37m[39;49;00m$
   504	PyObject[37m [39;49;00m*[37m[39;49;00m$
   505	[32mPyEval_EvalFrame[39;49;00m(PyFrameObject[37m [39;49;00m*f)[37m [39;49;00m{[37m[39;49;00m$
   506	[37m	[39;49;00m[37m/* This is for backward compatibility with extension modules that[39;49;00m$
   507	[37m           used this API; core interpreter code should call PyEval_EvalFrameEx() */[39;49;00m[37m[39;49;00m$
   508	[37m	[39;49;00m[34mreturn[39;49;00m[37m [39;49;00mPyEval_EvalFrameEx(f,[37m [39;49;00m[34m0[39;49;00m);[37m[39;49;00m$
   509	}[37m[39;49;00m$
   510	[37m[39;49;00m$
   511	PyObject[37m [39;49;00m*[37m[39;49;00m$
   512	[32mPyEval_EvalFrameEx[39;49;00m(PyFrameObject[37m [39;49;00m*f,[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mthrowflag)[37m[39;49;00m$
   513	{[37m[39;49;00m$
   514	[36m#[39;49;00m[36mifdef DXPAIRS[39;49;00m[36m[39;49;00m$
   515	[37m	[39;49;00m[36mint[39;49;00m[37m [39;49;00mlastopcode[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   516	[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   517	[37m	[39;49;00m[34mregister[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m**stack_pointer;[37m   [39;49;00m[37m/* Next free slot in value stack */[39;49;00m[37m[39;49;00m$
   518	[37m	[39;49;00m[34mregister[39;49;00m[37m [39;49;00m[36munsigned[39;49;00m[37m [39;49;00m[36mchar[39;49;00m[37m [39;49;00m*next_instr;[37m[39;49;00m$
   519	[37m	[39;49;00m[34mregister[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mopcode;[37m	[39;49;00m[37m/* Current opcode */[39;49;00m[37m[39;49;00m$
   520	[37m	[39;49;00m[34mregister[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00moparg;[37m	[39;49;00m[37m/* Current opcode argument, if any */[39;49;00m[37m[39;49;00m$
   521	[37m	[39;49;00m[34mregister[39;49;00m[37m [39;49;00m[34menum[39;49;00m[37m [39;49;00mwhy_code[37m [39;49;00mwhy;[37m [39;49;00m[37m/* Reason for block stack unwind */[39;49;00m[37m[39;49;00m$
   522	[37m	[39;49;00m[34mregister[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00merr;[37m	[39;49;00m[37m/* Error status -- nonzero if error */[39;49;00m[37m[39;49;00m$
   523	[37m	[39;49;00m[34mregister[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*x;[37m	[39;49;00m[37m/* Result object -- NULL if error */[39;49;00m[37m[39;49;00m$
   524	[37m	[39;49;00m[34mregister[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*v;[37m	[39;49;00m[37m/* Temporary objects popped off stack */[39;49;00m[37m[39;49;00m$
   525	[37m	[39;49;00m[34mregister[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*w;[37m[39;49;00m$
   526	[37m	[39;49;00m[34mregister[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*u;[37m[39;49;00m$
   527	[37m	[39;49;00m[34mregister[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*t;[37m[39;49;00m$
   528	[37m	[39;49;00m[34mregister[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m*stream[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m    [39;49;00m[37m/* for PRINT opcodes */[39;49;00m[37m[39;49;00m$
   529	[37m	[39;49;00m[34mregister[39;49;00m[37m [39;49;00mPyObject[37m [39;49;00m**fastlocals,[37m [39;49;00m**freevars;[37m[39;49;00m$
   530	[37m	[39;49;00mPyObject[37m [39;49;00m*retval[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m	[39;49;00m[37m/* Return value */[39;49;00m[37m[39;49;00m$
   531	[37m	[39;49;00mPyThreadState[37m [39;49;00m*tstate[37m [39;49;00m=[37m [39;49;00mPyThreadState_GET();[37m[39;49;00m$
   532	[37m	[39;49;00mPyCodeObject[37m [39;49;00m*co;[37m[39;49;00m$
   533	[37m[39;49;00m$
   534	[37m	[39;49;00m[37m/* when tracing we set things up so that[39;49;00m$
   535	[37m[39;49;00m$
   536	[37m               not (instr_lb <= current_bytecode_offset < instr_ub)[39;49;00m$
   537	[37m[39;49;00m$
   538	[37m	   is true when the line being executed has changed.  The[39;49;00m$
   539	[37m           initial values are such as to make this false the first[39;49;00m$
   540	[37m           time it is tested. */[39;49;00m[37m[39;49;00m$
   541	[37m	[39;49;00m[36mint[39;49;00m[37m [39;49;00minstr_ub[37m [39;49;00m=[37m [39;49;00m[34m-1[39;49;00m,[37m [39;49;00minstr_lb[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m,[37m [39;49;00minstr_prev[37m [39;49;00m=[37m [39;49;00m[34m-1[39;49;00m;[37m[39;49;00m$
   542	[37m[39;49;00m$
   543	[37m	[39;49;00m[36munsigned[39;49;00m[37m [39;49;00m[36mchar[39;49;00m[37m [39;49;00m*first_instr;[37m[39;49;00m$
   544	[37m	[39;49;00mPyObject[37m [39;49;00m*names;[37m[39;49;00m$
   545	[37m	[39;49;00mPyObject[37m [39;49;00m*consts;[37m[39;49;00m$
   546	[36m#[39;49;00m[36mif defined(Py_DEBUG) || defined(LLTRACE)[39;49;00m[36m[39;49;00m$
   547	[37m	[39;49;00m[37m/* Make it easier to find out where we are with a debugger */[39;49;00m[37m[39;49;00m$
   548	[37m	[39;49;00m[36mchar[39;49;00m[37m [39;49;00m*filename;[37m[39;49;00m$
   549	[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   550	[37m[39;49;00m$
   551	[37m/* Tuple access macros */[39;49;00m[37m[39;49;00m$
   552	[37m[39;49;00m$
   553	[36m#[39;49;00m[36mifndef Py_DEBUG[39;49;00m[36m[39;49;00m$
   554	[36m#[39;49;00m[36mdefine GETITEM(v, i) PyTuple_GET_ITEM((PyTupleObject *)(v), (i))[39;49;00m[36m[39;49;00m$
   555	[36m#[39;49;00m[36melse[39;49;00m[36m[39;49;00m$
   556	[36m#[39;49;00m[36mdefine GETITEM(v, i) PyTuple_GetItem((v), (i))[39;49;00m[36m[39;49;00m$
   557	[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   558	[37m[39;49;00m$
   559	[36m#[39;49;00m[36mifdef WITH_TSC[39;49;00m[36m[39;49;00m$
   560	[37m/* Use Pentium timestamp counter to mark certain events:[39;49;00m$
   561	[37m   inst0 -- beginning of switch statement for opcode dispatch[39;49;00m$
   562	[37m   inst1 -- end of switch statement (may be skipped)[39;49;00m$
   563	[37m   loop0 -- the top of the mainloop[39;49;00m$
   564	[37m   loop1 -- place where control returns again to top of mainloop[39;49;00m$
   565	[37m            (may be skipped)[39;49;00m$
   566	[37m   intr1 -- beginning of long interruption[39;49;00m$
   567	[37m   intr2 -- end of long interruption[39;49;00m$
   568	[37m[39;49;00m$
   569	[37m   Many opcodes call out to helper C functions.  In some cases, the[39;49;00m$
   570	[37m   time in those functions should be counted towards the time for the[39;49;00m$
   571	[37m   opcode, but not in all cases.  For example, a CALL_FUNCTION opcode[39;49;00m$
   572	[37m   calls another Python function; there's no point in charge all the[39;49;00m$
   573	[37m   bytecode executed by the called function to the caller.[39;49;00m$
   574	[37m[39;49;00m$
   575	[37m   It's hard to make a useful judgement statically.  In the presence[39;49;00m$
   576	[37m   of operator overloading, it's impossible to tell if a call will[39;49;00m$
   577	[37m   execute new Python code or not.[39;49;00m$
   578	[37m[39;49;00m$
   579	[37m   It's a case-by-case judgement.  I'll use intr1 for the following[39;49;00m$
   580	[37m   cases:[39;49;00m$
   581	[37m[39;49;00m$
   582	[37m   EXEC_STMT[39;49;00m$
   583	[37m   IMPORT_STAR[39;49;00m$
   584	[37m   IMPORT_FROM[39;49;00m$
   585	[37m   CALL_FUNCTION (and friends)[39;49;00m$
   586	[37m[39;49;00m$
   587	[37m */[39;49;00m[37m[39;49;00m$
   588	[37m	[39;49;00muint64[37m [39;49;00minst0,[37m [39;49;00minst1,[37m [39;49;00mloop0,[37m [39;49;00mloop1,[37m [39;49;00mintr0[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m,[37m [39;49;00mintr1[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   589	[37m	[39;49;00m[36mint[39;49;00m[37m [39;49;00mticked[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   590	[37m[39;49;00m$
   591	[37m	[39;49;00mREAD_TIMESTAMP(inst0);[37m[39;49;00m$
   592	[37m	[39;49;00mREAD_TIMESTAMP(inst1);[37m[39;49;00m$
   593	[37m	[39;49;00mREAD_TIMESTAMP(loop0);[37m[39;49;00m$
   594	[37m	[39;49;00mREAD_TIMESTAMP(loop1);[37m[39;49;00m$
   595	[37m[39;49;00m$
   596	[37m	[39;49;00m[37m/* shut up the compiler */[39;49;00m[37m[39;49;00m$
   597	[37m	[39;49;00mopcode[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   598	[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   599	[37m[39;49;00m$
   600	[37m/* Code access macros */[39;49;00m[37m[39;49;00m$
   601	[37m[39;49;00m$
   602	[36m#[39;49;00m[36mdefine INSTR_OFFSET()	((int)(next_instr - first_instr))[39;49;00m[36m[39;49;00m$
   603	[36m#[39;49;00m[36mdefine NEXTOP()	(*next_instr++)[39;49;00m[36m[39;49;00m$
   604	[36m#[39;49;00m[36mdefine NEXTARG()	(next_instr += 2, (next_instr[-1]<<8) + next_instr[-2])[39;49;00m[36m[39;49;00m$
   605	[36m#[39;49;00m[36mdefine PEEKARG()	((next_instr[2]<<8) + next_instr[1])[39;49;00m[36m[39;49;00m$
   606	[36m#[39;49;00m[36mdefine JUMPTO(x)	(next_instr = first_instr + (x))[39;49;00m[36m[39;49;00m$
   607	[36m#[39;49;00m[36mdefine JUMPBY(x)	(next_instr += (x))[39;49;00m[36m[39;49;00m$
   608	[37m[39;49;00m$
   609	[37m/* OpCode prediction macros[39;49;00m$
   610	[37m	Some opcodes tend to come in pairs thus making it possible to predict[39;49;00m$
   611	[37m	the second code when the first is run.  For example, COMPARE_OP is often[39;49;00m$
   612	[37m	followed by JUMP_IF_FALSE or JUMP_IF_TRUE.  And, those opcodes are often[39;49;00m$
   613	[37m	followed by a POP_TOP.[39;49;00m$
   614	[37m[39;49;00m$
   615	[37m	Verifying the prediction costs a single high-speed test of register[39;49;00m$
   616	[37m	variable against a constant.  If the pairing was good, then the[39;49;00m$
   617	[37m	processor has a high likelihood of making its own successful branch[39;49;00m$
   618	[37m	prediction which results in a nearly zero overhead transition to the[39;49;00m$
   619	[37m	next opcode.[39;49;00m$
   620	[37m[39;49;00m$
   621	[37m	A successful prediction saves a trip through the eval-loop including[39;49;00m$
   622	[37m	its two unpredictable branches, the HASARG test and the switch-case.[39;49;00m$
   623	[37m[39;49;00m$
   624	[37m        If collecting opcode statistics, turn off prediction so that[39;49;00m$
   625	[37m	statistics are accurately maintained (the predictions bypass[39;49;00m$
   626	[37m	the opcode frequency counter updates).[39;49;00m$
   627	[37m*/[39;49;00m[37m[39;49;00m$
   628	[37m[39;49;00m$
   629	[36m#[39;49;00m[36mifdef DYNAMIC_EXECUTION_PROFILE[39;49;00m[36m[39;49;00m$
   630	[36m#[39;49;00m[36mdefine PREDICT(op)		if (0) goto PRED_##op[39;49;00m[36m[39;49;00m$
   631	[36m#[39;49;00m[36melse[39;49;00m[36m[39;49;00m$
   632	[36m#[39;49;00m[36mdefine PREDICT(op)		if (*next_instr == op) goto PRED_##op[39;49;00m[36m[39;49;00m$
   633	[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   634	[37m[39;49;00m$
   635	[36m#[39;49;00m[36mdefine PREDICTED(op)		PRED_##op: next_instr++[39;49;00m[36m[39;49;00m$
   636	[36m#[39;49;00m[36mdefine PREDICTED_WITH_ARG(op)	PRED_##op: oparg = PEEKARG(); next_instr += 3[39;49;00m[36m[39;49;00m$
   637	[37m[39;49;00m$
   638	[37m/* Stack manipulation macros */[39;49;00m[37m[39;49;00m$
   639	[37m[39;49;00m$
   640	[37m/* The stack can grow at most MAXINT deep, as co_nlocals and[39;49;00m$
   641	[37m   co_stacksize are ints. */[39;49;00m[37m[39;49;00m$
   642	[36m#[39;49;00m[36mdefine STACK_LEVEL()	((int)(stack_pointer - f->f_valuestack))[39;49;00m[36m[39;49;00m$
   643	[36m#[39;49;00m[36mdefine EMPTY()		(STACK_LEVEL() == 0)[39;49;00m[36m[39;49;00m$
   644	[36m#[39;49;00m[36mdefine TOP()		(stack_pointer[-1])[39;49;00m[36m[39;49;00m$
   645	[36m#[39;49;00m[36mdefine SECOND()	(stack_pointer[-2])[39;49;00m[36m[39;49;00m$
   646	[36m#[39;49;00m[36mdefine THIRD() 	(stack_pointer[-3])[39;49;00m[36m[39;49;00m$
   647	[36m#[39;49;00m[36mdefine FOURTH()	(stack_pointer[-4])[39;49;00m[36m[39;49;00m$
   648	[36m#[39;49;00m[36mdefine SET_TOP(v)	(stack_pointer[-1] = (v))[39;49;00m[36m[39;49;00m$
   649	[36m#[39;49;00m[36mdefine SET_SECOND(v)	(stack_pointer[-2] = (v))[39;49;00m[36m[39;49;00m$
   650	[36m#[39;49;00m[36mdefine SET_THIRD(v)	(stack_pointer[-3] = (v))[39;49;00m[36m[39;49;00m$
   651	[36m#[39;49;00m[36mdefine SET_FOURTH(v)	(stack_pointer[-4] = (v))[39;49;00m[36m[39;49;00m$
   652	[36m#[39;49;00m[36mdefine BASIC_STACKADJ(n)	(stack_pointer += n)[39;49;00m[36m[39;49;00m$
   653	[36m#[39;49;00m[36mdefine BASIC_PUSH(v)	(*stack_pointer++ = (v))[39;49;00m[36m[39;49;00m$
   654	[36m#[39;49;00m[36mdefine BASIC_POP()	(*--stack_pointer)[39;49;00m[36m[39;49;00m$
   655	[37m[39;49;00m$
   656	[36m#[39;49;00m[36mifdef LLTRACE[39;49;00m[36m[39;49;00m$
   657	[36m#[39;49;00m[36mdefine PUSH(v)		{ (void)(BASIC_PUSH(v), \[39;49;00m[36m[39;49;00m$
   658	[36m                               lltrace && prtrace(TOP(), "push")); \[39;49;00m[36m[39;49;00m$
   659	[36m                               assert(STACK_LEVEL() <= co->co_stacksize); }[39;49;00m[36m[39;49;00m$
   660	[36m#[39;49;00m[36mdefine POP()		((void)(lltrace && prtrace(TOP(), "pop")), BASIC_POP())[39;49;00m[36m[39;49;00m$
   661	[36m#[39;49;00m[36mdefine STACKADJ(n)	{ (void)(BASIC_STACKADJ(n), \[39;49;00m[36m[39;49;00m$
   662	[36m                               lltrace && prtrace(TOP(), "stackadj")); \[39;49;00m[36m[39;49;00m$
   663	[36m                               assert(STACK_LEVEL() <= co->co_stacksize); }[39;49;00m[36m[39;49;00m$
   664	[36m#[39;49;00m[36mdefine EXT_POP(STACK_POINTER) (lltrace && prtrace(*(STACK_POINTER), "ext_pop"), *--(STACK_POINTER))[39;49;00m[36m[39;49;00m$
   665	[36m#[39;49;00m[36melse[39;49;00m[36m[39;49;00m$
   666	[36m#[39;49;00m[36mdefine PUSH(v)		BASIC_PUSH(v)[39;49;00m[36m[39;49;00m$
   667	[36m#[39;49;00m[36mdefine POP()		BASIC_POP()[39;49;00m[36m[39;49;00m$
   668	[36m#[39;49;00m[36mdefine STACKADJ(n)	BASIC_STACKADJ(n)[39;49;00m[36m[39;49;00m$
   669	[36m#[39;49;00m[36mdefine EXT_POP(STACK_POINTER) (*--(STACK_POINTER))[39;49;00m[36m[39;49;00m$
   670	[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   671	[37m[39;49;00m$
   672	[37m/* Local variable macros */[39;49;00m[37m[39;49;00m$
   673	[37m[39;49;00m$
   674	[36m#[39;49;00m[36mdefine GETLOCAL(i)	(fastlocals[i])[39;49;00m[36m[39;49;00m$
   675	[37m[39;49;00m$
   676	[37m/* The SETLOCAL() macro must not DECREF the local variable in-place and[39;49;00m$
   677	[37m   then store the new value; it must copy the old value to a temporary[39;49;00m$
   678	[37m   value, then store the new value, and then DECREF the temporary value.[39;49;00m$
   679	[37m   This is because it is possible that during the DECREF the frame is[39;49;00m$
   680	[37m   accessed by other code (e.g. a __del__ method or gc.collect()) and the[39;49;00m$
   681	[37m   variable would be pointing to already-freed memory. */[39;49;00m[37m[39;49;00m$
   682	[36m#[39;49;00m[36mdefine SETLOCAL(i, value)	do { PyObject *tmp = GETLOCAL(i); \[39;49;00m[36m[39;49;00m$
   683	[36m				     GETLOCAL(i) = value; \[39;49;00m[36m[39;49;00m$
   684	[36m                                     Py_XDECREF(tmp); } while (0)[39;49;00m[36m[39;49;00m$
   685	[37m[39;49;00m$
   686	[37m/* Start of code */[39;49;00m[37m[39;49;00m$
   687	[37m[39;49;00m$
   688	[37m	[39;49;00m[34mif[39;49;00m[37m [39;49;00m(f[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
   689	[37m		[39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   690	[37m[39;49;00m$
   691	[37m	[39;49;00m[37m/* push frame */[39;49;00m[37m[39;49;00m$
   692	[37m	[39;49;00m[34mif[39;49;00m[37m [39;49;00m(Py_EnterRecursiveCall([33m"[39;49;00m[33m"[39;49;00m))[37m[39;49;00m$
   693	[37m		[39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   694	[37m[39;49;00m$
   695	[37m	[39;49;00mtstate->frame[37m [39;49;00m=[37m [39;49;00mf;[37m[39;49;00m$
   696	[37m[39;49;00m$
   697	[37m	[39;49;00m[34mif[39;49;00m[37m [39;49;00m(tstate->use_tracing)[37m [39;49;00m{[37m[39;49;00m$
   698	[37m		[39;49;00m[34mif[39;49;00m[37m [39;49;00m(tstate->c_tracefunc[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
   699	[37m			[39;49;00m[37m/* tstate->c_tracefunc, if defined, is a[39;49;00m$
   700	[37m			   function that will be called on *every* entry[39;49;00m$
   701	[37m			   to a code block.  Its return value, if not[39;49;00m$
   702	[37m			   None, is a function that will be called at[39;49;00m$
   703	[37m			   the start of each executed line of code.[39;49;00m$
   704	[37m			   (Actually, the function must return itself[39;49;00m$
   705	[37m			   in order to continue tracing.)  The trace[39;49;00m$
   706	[37m			   functions are called with three arguments:[39;49;00m$
   707	[37m			   a pointer to the current frame, a string[39;49;00m$
   708	[37m			   indicating why the function is called, and[39;49;00m$
   709	[37m			   an argument which depends on the situation.[39;49;00m$
   710	[37m			   The global trace function is also called[39;49;00m$
   711	[37m			   whenever an exception is detected. */[39;49;00m[37m[39;49;00m$
   712	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(call_trace(tstate->c_tracefunc,[37m [39;49;00mtstate->c_traceobj,[37m[39;49;00m$
   713	[37m				       [39;49;00mf,[37m [39;49;00mPyTrace_CALL,[37m [39;49;00mPy_None))[37m [39;49;00m{[37m[39;49;00m$
   714	[37m				[39;49;00m[37m/* Trace function raised an error */[39;49;00m[37m[39;49;00m$
   715	[37m				[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mexit_eval_frame;[37m[39;49;00m$
   716	[37m			[39;49;00m}[37m[39;49;00m$
   717	[37m		[39;49;00m}[37m[39;49;00m$
   718	[37m		[39;49;00m[34mif[39;49;00m[37m [39;49;00m(tstate->c_profilefunc[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
   719	[37m			[39;49;00m[37m/* Similar for c_profilefunc, except it needn't[39;49;00m$
   720	[37m			   return itself and isn't called for "line" events */[39;49;00m[37m[39;49;00m$
   721	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(call_trace(tstate->c_profilefunc,[37m[39;49;00m$
   722	[37m				       [39;49;00mtstate->c_profileobj,[37m[39;49;00m$
   723	[37m				       [39;49;00mf,[37m [39;49;00mPyTrace_CALL,[37m [39;49;00mPy_None))[37m [39;49;00m{[37m[39;49;00m$
   724	[37m				[39;49;00m[37m/* Profile function raised an error */[39;49;00m[37m[39;49;00m$
   725	[37m				[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mexit_eval_frame;[37m[39;49;00m$
   726	[37m			[39;49;00m}[37m[39;49;00m$
   727	[37m		[39;49;00m}[37m[39;49;00m$
   728	[37m	[39;49;00m}[37m[39;49;00m$
   729	[37m[39;49;00m$
   730	[37m	[39;49;00mco[37m [39;49;00m=[37m [39;49;00mf->f_code;[37m[39;49;00m$
   731	[37m	[39;49;00mnames[37m [39;49;00m=[37m [39;49;00mco->co_names;[37m[39;49;00m$
   732	[37m	[39;49;00mconsts[37m [39;49;00m=[37m [39;49;00mco->co_consts;[37m[39;49;00m$
   733	[37m	[39;49;00mfastlocals[37m [39;49;00m=[37m [39;49;00mf->f_localsplus;[37m[39;49;00m$
   734	[37m	[39;49;00mfreevars[37m [39;49;00m=[37m [39;49;00mf->f_localsplus[37m [39;49;00m+[37m [39;49;00mco->co_nlocals;[37m[39;49;00m$
   735	[37m	[39;49;00mfirst_instr[37m [39;49;00m=[37m [39;49;00m([36munsigned[39;49;00m[37m [39;49;00m[36mchar[39;49;00m*)[37m [39;49;00mPyString_AS_STRING(co->co_code);[37m[39;49;00m$
   736	[37m	[39;49;00m[37m/* An explanation is in order for the next line.[39;49;00m$
   737	[37m[39;49;00m$
   738	[37m	   f->f_lasti now refers to the index of the last instruction[39;49;00m$
   739	[37m	   executed.  You might think this was obvious from the name, but[39;49;00m$
   740	[37m	   this wasn't always true before 2.3!  PyFrame_New now sets[39;49;00m$
   741	[37m	   f->f_lasti to -1 (i.e. the index *before* the first instruction)[39;49;00m$
   742	[37m	   and YIELD_VALUE doesn't fiddle with f_lasti any more.  So this[39;49;00m$
   743	[37m	   does work.  Promise. */[39;49;00m[37m[39;49;00m$
   744	[37m	[39;49;00mnext_instr[37m [39;49;00m=[37m [39;49;00mfirst_instr[37m [39;49;00m+[37m [39;49;00mf->f_lasti[37m [39;49;00m+[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
   745	[37m	[39;49;00mstack_pointer[37m [39;49;00m=[37m [39;49;00mf->f_stacktop;[37m[39;49;00m$
   746	[37m	[39;49;00massert(stack_pointer[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m);[37m[39;49;00m$
   747	[37m	[39;49;00mf->f_stacktop[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m	[39;49;00m[37m/* remains NULL unless yield suspends frame */[39;49;00m[37m[39;49;00m$
   748	[37m[39;49;00m$
   749	[36m#[39;49;00m[36mifdef LLTRACE[39;49;00m[36m[39;49;00m$
   750	[37m	[39;49;00mlltrace[37m [39;49;00m=[37m [39;49;00mPyDict_GetItemString(f->f_globals,[37m [39;49;00m[33m"[39;49;00m[33m__lltrace__[39;49;00m[33m"[39;49;00m)[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   751	[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   752	[36m#[39;49;00m[36mif defined(Py_DEBUG) || defined(LLTRACE)[39;49;00m[36m[39;49;00m$
   753	[37m	[39;49;00mfilename[37m [39;49;00m=[37m [39;49;00mPyString_AsString(co->co_filename);[37m[39;49;00m$
   754	[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   755	[37m[39;49;00m$
   756	[37m	[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_NOT;[37m[39;49;00m$
   757	[37m	[39;49;00merr[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   758	[37m	[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPy_None;[37m	[39;49;00m[37m/* Not a reference, just anything non-NULL */[39;49;00m[37m[39;49;00m$
   759	[37m	[39;49;00mw[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   760	[37m[39;49;00m$
   761	[37m	[39;49;00m[34mif[39;49;00m[37m [39;49;00m(throwflag)[37m [39;49;00m{[37m [39;49;00m[37m/* support for generator.throw() */[39;49;00m[37m[39;49;00m$
   762	[37m		[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_EXCEPTION;[37m[39;49;00m$
   763	[37m		[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mon_error;[37m[39;49;00m$
   764	[37m	[39;49;00m}[37m[39;49;00m$
   765	[37m[39;49;00m$
   766	[37m	[39;49;00m[34mfor[39;49;00m[37m [39;49;00m(;;)[37m [39;49;00m{[37m[39;49;00m$
   767	[36m#[39;49;00m[36mifdef WITH_TSC[39;49;00m[36m[39;49;00m$
   768	[37m		[39;49;00m[34mif[39;49;00m[37m [39;49;00m(inst1[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
   769	[37m			[39;49;00m[37m/* Almost surely, the opcode executed a break[39;49;00m$
   770	[37m			   or a continue, preventing inst1 from being set[39;49;00m$
   771	[37m			   on the way out of the loop.[39;49;00m$
   772	[37m			*/[39;49;00m[37m[39;49;00m$
   773	[37m			[39;49;00mREAD_TIMESTAMP(inst1);[37m[39;49;00m$
   774	[37m			[39;49;00mloop1[37m [39;49;00m=[37m [39;49;00minst1;[37m[39;49;00m$
   775	[37m		[39;49;00m}[37m[39;49;00m$
   776	[37m		[39;49;00mdump_tsc(opcode,[37m [39;49;00mticked,[37m [39;49;00minst0,[37m [39;49;00minst1,[37m [39;49;00mloop0,[37m [39;49;00mloop1,[37m[39;49;00m$
   777	[37m			 [39;49;00mintr0,[37m [39;49;00mintr1);[37m[39;49;00m$
   778	[37m		[39;49;00mticked[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   779	[37m		[39;49;00minst1[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   780	[37m		[39;49;00mintr0[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   781	[37m		[39;49;00mintr1[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   782	[37m		[39;49;00mREAD_TIMESTAMP(loop0);[37m[39;49;00m$
   783	[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   784	[37m		[39;49;00massert(stack_pointer[37m [39;49;00m>=[37m [39;49;00mf->f_valuestack);[37m [39;49;00m[37m/* else underflow */[39;49;00m[37m[39;49;00m$
   785	[37m		[39;49;00massert(STACK_LEVEL()[37m [39;49;00m<=[37m [39;49;00mco->co_stacksize);[37m  [39;49;00m[37m/* else overflow */[39;49;00m[37m[39;49;00m$
   786	[37m[39;49;00m$
   787	[37m		[39;49;00m[37m/* Do periodic things.  Doing this every time through[39;49;00m$
   788	[37m		   the loop would add too much overhead, so we do it[39;49;00m$
   789	[37m		   only every Nth instruction.  We also do it if[39;49;00m$
   790	[37m		   ``things_to_do'' is set, i.e. when an asynchronous[39;49;00m$
   791	[37m		   event needs attention (e.g. a signal handler or[39;49;00m$
   792	[37m		   async I/O handler); see Py_AddPendingCall() and[39;49;00m$
   793	[37m		   Py_MakePendingCalls() above. */[39;49;00m[37m[39;49;00m$
   794	[37m[39;49;00m$
   795	[37m		[39;49;00m[34mif[39;49;00m[37m [39;49;00m(--_Py_Ticker[37m [39;49;00m<[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
   796	[37m                        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(*next_instr[37m [39;49;00m==[37m [39;49;00mSETUP_FINALLY)[37m [39;49;00m{[37m[39;49;00m$
   797	[37m                                [39;49;00m[37m/* Make the last opcode before[39;49;00m$
   798	[37m                                   a try: finally: block uninterruptable. */[39;49;00m[37m[39;49;00m$
   799	[37m                                [39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
   800	[37m                        [39;49;00m}[37m[39;49;00m$
   801	[37m			[39;49;00m_Py_Ticker[37m [39;49;00m=[37m [39;49;00m_Py_CheckInterval;[37m[39;49;00m$
   802	[37m			[39;49;00mtstate->tick_counter++;[37m[39;49;00m$
   803	[36m#[39;49;00m[36mifdef WITH_TSC[39;49;00m[36m[39;49;00m$
   804	[37m			[39;49;00mticked[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
   805	[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   806	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(things_to_do)[37m [39;49;00m{[37m[39;49;00m$
   807	[37m				[39;49;00m[34mif[39;49;00m[37m [39;49;00m(Py_MakePendingCalls()[37m [39;49;00m<[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
   808	[37m					[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_EXCEPTION;[37m[39;49;00m$
   809	[37m					[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mon_error;[37m[39;49;00m$
   810	[37m				[39;49;00m}[37m[39;49;00m$
   811	[37m				[39;49;00m[34mif[39;49;00m[37m [39;49;00m(things_to_do)[37m[39;49;00m$
   812	[37m					[39;49;00m[37m/* MakePendingCalls() didn't succeed.[39;49;00m$
   813	[37m					   Force early re-execution of this[39;49;00m$
   814	[37m					   "periodic" code, possibly after[39;49;00m$
   815	[37m					   a thread switch */[39;49;00m[37m[39;49;00m$
   816	[37m					[39;49;00m_Py_Ticker[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   817	[37m			[39;49;00m}[37m[39;49;00m$
   818	[36m#[39;49;00m[36mifdef WITH_THREAD[39;49;00m[36m[39;49;00m$
   819	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(interpreter_lock)[37m [39;49;00m{[37m[39;49;00m$
   820	[37m				[39;49;00m[37m/* Give another thread a chance */[39;49;00m[37m[39;49;00m$
   821	[37m[39;49;00m$
   822	[37m				[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyThreadState_Swap([36mNULL[39;49;00m)[37m [39;49;00m!=[37m [39;49;00mtstate)[37m[39;49;00m$
   823	[37m					[39;49;00mPy_FatalError([33m"[39;49;00m[33mceval: tstate mix-up[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
   824	[37m				[39;49;00mPyThread_release_lock(interpreter_lock);[37m[39;49;00m$
   825	[37m[39;49;00m$
   826	[37m				[39;49;00m[37m/* Other threads may run now */[39;49;00m[37m[39;49;00m$
   827	[37m[39;49;00m$
   828	[37m				[39;49;00mPyThread_acquire_lock(interpreter_lock,[37m [39;49;00m[34m1[39;49;00m);[37m[39;49;00m$
   829	[37m				[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyThreadState_Swap(tstate)[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
   830	[37m					[39;49;00mPy_FatalError([33m"[39;49;00m[33mceval: orphan tstate[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
   831	[37m[39;49;00m$
   832	[37m				[39;49;00m[37m/* Check for thread interrupts */[39;49;00m[37m[39;49;00m$
   833	[37m[39;49;00m$
   834	[37m				[39;49;00m[34mif[39;49;00m[37m [39;49;00m(tstate->async_exc[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
   835	[37m					[39;49;00mx[37m [39;49;00m=[37m [39;49;00mtstate->async_exc;[37m[39;49;00m$
   836	[37m					[39;49;00mtstate->async_exc[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   837	[37m					[39;49;00mPyErr_SetNone(x);[37m[39;49;00m$
   838	[37m					[39;49;00mPy_DECREF(x);[37m[39;49;00m$
   839	[37m					[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_EXCEPTION;[37m[39;49;00m$
   840	[37m					[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mon_error;[37m[39;49;00m$
   841	[37m				[39;49;00m}[37m[39;49;00m$
   842	[37m			[39;49;00m}[37m[39;49;00m$
   843	[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   844	[37m		[39;49;00m}[37m[39;49;00m$
   845	[37m[39;49;00m$
   846	[37m	[39;49;00mfast_next_opcode:[37m[39;49;00m$
   847	[37m		[39;49;00mf->f_lasti[37m [39;49;00m=[37m [39;49;00mINSTR_OFFSET();[37m[39;49;00m$
   848	[37m[39;49;00m$
   849	[37m		[39;49;00m[37m/* line-by-line tracing support */[39;49;00m[37m[39;49;00m$
   850	[37m[39;49;00m$
   851	[37m		[39;49;00m[34mif[39;49;00m[37m [39;49;00m(tstate->c_tracefunc[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m[37m [39;49;00m&&[37m [39;49;00m!tstate->tracing)[37m [39;49;00m{[37m[39;49;00m$
   852	[37m			[39;49;00m[37m/* see maybe_call_line_trace[39;49;00m$
   853	[37m			   for expository comments */[39;49;00m[37m[39;49;00m$
   854	[37m			[39;49;00mf->f_stacktop[37m [39;49;00m=[37m [39;49;00mstack_pointer;[37m[39;49;00m$
   855	[37m[39;49;00m$
   856	[37m			[39;49;00merr[37m [39;49;00m=[37m [39;49;00mmaybe_call_line_trace(tstate->c_tracefunc,[37m[39;49;00m$
   857	[37m						    [39;49;00mtstate->c_traceobj,[37m[39;49;00m$
   858	[37m						    [39;49;00mf,[37m [39;49;00m&instr_lb,[37m [39;49;00m&instr_ub,[37m[39;49;00m$
   859	[37m						    [39;49;00m&instr_prev);[37m[39;49;00m$
   860	[37m			[39;49;00m[37m/* Reload possibly changed frame fields */[39;49;00m[37m[39;49;00m$
   861	[37m			[39;49;00mJUMPTO(f->f_lasti);[37m[39;49;00m$
   862	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(f->f_stacktop[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
   863	[37m				[39;49;00mstack_pointer[37m [39;49;00m=[37m [39;49;00mf->f_stacktop;[37m[39;49;00m$
   864	[37m				[39;49;00mf->f_stacktop[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   865	[37m			[39;49;00m}[37m[39;49;00m$
   866	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err)[37m [39;49;00m{[37m[39;49;00m$
   867	[37m				[39;49;00m[37m/* trace function raised an exception */[39;49;00m[37m[39;49;00m$
   868	[37m				[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mon_error;[37m[39;49;00m$
   869	[37m			[39;49;00m}[37m[39;49;00m$
   870	[37m		[39;49;00m}[37m[39;49;00m$
   871	[37m[39;49;00m$
   872	[37m		[39;49;00m[37m/* Extract opcode and argument */[39;49;00m[37m[39;49;00m$
   873	[37m[39;49;00m$
   874	[37m		[39;49;00mopcode[37m [39;49;00m=[37m [39;49;00mNEXTOP();[37m[39;49;00m$
   875	[37m		[39;49;00moparg[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m   [39;49;00m[37m/* allows oparg to be stored in a register because[39;49;00m$
   876	[37m			it doesn't have to be remembered across a full loop */[39;49;00m[37m[39;49;00m$
   877	[37m		[39;49;00m[34mif[39;49;00m[37m [39;49;00m(HAS_ARG(opcode))[37m[39;49;00m$
   878	[37m			[39;49;00moparg[37m [39;49;00m=[37m [39;49;00mNEXTARG();[37m[39;49;00m$
   879	[37m	  [39;49;00mdispatch_opcode:[37m[39;49;00m$
   880	[36m#[39;49;00m[36mifdef DYNAMIC_EXECUTION_PROFILE[39;49;00m[36m[39;49;00m$
   881	[36m#[39;49;00m[36mifdef DXPAIRS[39;49;00m[36m[39;49;00m$
   882	[37m		[39;49;00mdxpairs[lastopcode][opcode]++;[37m[39;49;00m$
   883	[37m		[39;49;00mlastopcode[37m [39;49;00m=[37m [39;49;00mopcode;[37m[39;49;00m$
   884	[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   885	[37m		[39;49;00mdxp[opcode]++;[37m[39;49;00m$
   886	[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   887	[37m[39;49;00m$
   888	[36m#[39;49;00m[36mifdef LLTRACE[39;49;00m[36m[39;49;00m$
   889	[37m		[39;49;00m[37m/* Instruction tracing */[39;49;00m[37m[39;49;00m$
   890	[37m[39;49;00m$
   891	[37m		[39;49;00m[34mif[39;49;00m[37m [39;49;00m(lltrace)[37m [39;49;00m{[37m[39;49;00m$
   892	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(HAS_ARG(opcode))[37m [39;49;00m{[37m[39;49;00m$
   893	[37m				[39;49;00mprintf([33m"[39;49;00m[33m%d: %d, %d[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m,[37m[39;49;00m$
   894	[37m				       [39;49;00mf->f_lasti,[37m [39;49;00mopcode,[37m [39;49;00moparg);[37m[39;49;00m$
   895	[37m			[39;49;00m}[37m[39;49;00m$
   896	[37m			[39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
   897	[37m				[39;49;00mprintf([33m"[39;49;00m[33m%d: %d[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m,[37m[39;49;00m$
   898	[37m				       [39;49;00mf->f_lasti,[37m [39;49;00mopcode);[37m[39;49;00m$
   899	[37m			[39;49;00m}[37m[39;49;00m$
   900	[37m		[39;49;00m}[37m[39;49;00m$
   901	[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   902	[37m[39;49;00m$
   903	[37m		[39;49;00m[37m/* Main switch on opcode */[39;49;00m[37m[39;49;00m$
   904	[37m		[39;49;00mREAD_TIMESTAMP(inst0);[37m[39;49;00m$
   905	[37m[39;49;00m$
   906	[37m		[39;49;00m[34mswitch[39;49;00m[37m [39;49;00m(opcode)[37m [39;49;00m{[37m[39;49;00m$
   907	[37m[39;49;00m$
   908	[37m		[39;49;00m[37m/* BEWARE![39;49;00m$
   909	[37m		   It is essential that any operation that fails sets either[39;49;00m$
   910	[37m		   x to NULL, err to nonzero, or why to anything but WHY_NOT,[39;49;00m$
   911	[37m		   and that no operation that succeeds does this! */[39;49;00m[37m[39;49;00m$
   912	[37m[39;49;00m$
   913	[37m		[39;49;00m[37m/* case STOP_CODE: this is an error! */[39;49;00m[37m[39;49;00m$
   914	[37m[39;49;00m$
   915	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mNOP[39;49;00m:[37m[39;49;00m$
   916	[37m			[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
   917	[37m[39;49;00m$
   918	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mLOAD_FAST[39;49;00m:[37m[39;49;00m$
   919	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mGETLOCAL(oparg);[37m[39;49;00m$
   920	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
   921	[37m				[39;49;00mPy_INCREF(x);[37m[39;49;00m$
   922	[37m				[39;49;00mPUSH(x);[37m[39;49;00m$
   923	[37m				[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
   924	[37m			[39;49;00m}[37m[39;49;00m$
   925	[37m			[39;49;00mformat_exc_check_arg(PyExc_UnboundLocalError,[37m[39;49;00m$
   926	[37m				[39;49;00mUNBOUNDLOCAL_ERROR_MSG,[37m[39;49;00m$
   927	[37m				[39;49;00mPyTuple_GetItem(co->co_varnames,[37m [39;49;00moparg));[37m[39;49;00m$
   928	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
   929	[37m[39;49;00m$
   930	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mLOAD_CONST[39;49;00m:[37m[39;49;00m$
   931	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mGETITEM(consts,[37m [39;49;00moparg);[37m[39;49;00m$
   932	[37m			[39;49;00mPy_INCREF(x);[37m[39;49;00m$
   933	[37m			[39;49;00mPUSH(x);[37m[39;49;00m$
   934	[37m			[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
   935	[37m[39;49;00m$
   936	[37m		[39;49;00mPREDICTED_WITH_ARG(STORE_FAST);[37m[39;49;00m$
   937	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSTORE_FAST[39;49;00m:[37m[39;49;00m$
   938	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
   939	[37m			[39;49;00mSETLOCAL(oparg,[37m [39;49;00mv);[37m[39;49;00m$
   940	[37m			[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
   941	[37m[39;49;00m$
   942	[37m		[39;49;00mPREDICTED(POP_TOP);[37m[39;49;00m$
   943	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mPOP_TOP[39;49;00m:[37m[39;49;00m$
   944	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
   945	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
   946	[37m			[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
   947	[37m[39;49;00m$
   948	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mROT_TWO[39;49;00m:[37m[39;49;00m$
   949	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
   950	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mSECOND();[37m[39;49;00m$
   951	[37m			[39;49;00mSET_TOP(w);[37m[39;49;00m$
   952	[37m			[39;49;00mSET_SECOND(v);[37m[39;49;00m$
   953	[37m			[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
   954	[37m[39;49;00m$
   955	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mROT_THREE[39;49;00m:[37m[39;49;00m$
   956	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
   957	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mSECOND();[37m[39;49;00m$
   958	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mTHIRD();[37m[39;49;00m$
   959	[37m			[39;49;00mSET_TOP(w);[37m[39;49;00m$
   960	[37m			[39;49;00mSET_SECOND(x);[37m[39;49;00m$
   961	[37m			[39;49;00mSET_THIRD(v);[37m[39;49;00m$
   962	[37m			[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
   963	[37m[39;49;00m$
   964	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mROT_FOUR[39;49;00m:[37m[39;49;00m$
   965	[37m			[39;49;00mu[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
   966	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mSECOND();[37m[39;49;00m$
   967	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mTHIRD();[37m[39;49;00m$
   968	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mFOURTH();[37m[39;49;00m$
   969	[37m			[39;49;00mSET_TOP(v);[37m[39;49;00m$
   970	[37m			[39;49;00mSET_SECOND(w);[37m[39;49;00m$
   971	[37m			[39;49;00mSET_THIRD(x);[37m[39;49;00m$
   972	[37m			[39;49;00mSET_FOURTH(u);[37m[39;49;00m$
   973	[37m			[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
   974	[37m[39;49;00m$
   975	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mDUP_TOP[39;49;00m:[37m[39;49;00m$
   976	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
   977	[37m			[39;49;00mPy_INCREF(v);[37m[39;49;00m$
   978	[37m			[39;49;00mPUSH(v);[37m[39;49;00m$
   979	[37m			[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
   980	[37m[39;49;00m$
   981	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mDUP_TOPX[39;49;00m:[37m[39;49;00m$
   982	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(oparg[37m [39;49;00m==[37m [39;49;00m[34m2[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
   983	[37m				[39;49;00mx[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
   984	[37m				[39;49;00mPy_INCREF(x);[37m[39;49;00m$
   985	[37m				[39;49;00mw[37m [39;49;00m=[37m [39;49;00mSECOND();[37m[39;49;00m$
   986	[37m				[39;49;00mPy_INCREF(w);[37m[39;49;00m$
   987	[37m				[39;49;00mSTACKADJ([34m2[39;49;00m);[37m[39;49;00m$
   988	[37m				[39;49;00mSET_TOP(x);[37m[39;49;00m$
   989	[37m				[39;49;00mSET_SECOND(w);[37m[39;49;00m$
   990	[37m				[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
   991	[37m			[39;49;00m}[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(oparg[37m [39;49;00m==[37m [39;49;00m[34m3[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
   992	[37m				[39;49;00mx[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
   993	[37m				[39;49;00mPy_INCREF(x);[37m[39;49;00m$
   994	[37m				[39;49;00mw[37m [39;49;00m=[37m [39;49;00mSECOND();[37m[39;49;00m$
   995	[37m				[39;49;00mPy_INCREF(w);[37m[39;49;00m$
   996	[37m				[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTHIRD();[37m[39;49;00m$
   997	[37m				[39;49;00mPy_INCREF(v);[37m[39;49;00m$
   998	[37m				[39;49;00mSTACKADJ([34m3[39;49;00m);[37m[39;49;00m$
   999	[37m				[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1000	[37m				[39;49;00mSET_SECOND(w);[37m[39;49;00m$
  1001	[37m				[39;49;00mSET_THIRD(v);[37m[39;49;00m$
  1002	[37m				[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
  1003	[37m			[39;49;00m}[37m[39;49;00m$
  1004	[37m			[39;49;00mPy_FatalError([33m"[39;49;00m[33minvalid argument to DUP_TOPX[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  1005	[37m				      [39;49;00m[33m"[39;49;00m[33m (bytecode corruption?)[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
  1006	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1007	[37m[39;49;00m$
  1008	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mUNARY_POSITIVE[39;49;00m:[37m[39;49;00m$
  1009	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1010	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_Positive(v);[37m[39;49;00m$
  1011	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1012	[37m			[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1013	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1014	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1015	[37m[39;49;00m$
  1016	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mUNARY_NEGATIVE[39;49;00m:[37m[39;49;00m$
  1017	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1018	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_Negative(v);[37m[39;49;00m$
  1019	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1020	[37m			[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1021	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1022	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1023	[37m[39;49;00m$
  1024	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mUNARY_NOT[39;49;00m:[37m[39;49;00m$
  1025	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1026	[37m			[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyObject_IsTrue(v);[37m[39;49;00m$
  1027	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1028	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1029	[37m				[39;49;00mPy_INCREF(Py_True);[37m[39;49;00m$
  1030	[37m				[39;49;00mSET_TOP(Py_True);[37m[39;49;00m$
  1031	[37m				[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1032	[37m			[39;49;00m}[37m[39;49;00m$
  1033	[37m			[39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m>[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1034	[37m				[39;49;00mPy_INCREF(Py_False);[37m[39;49;00m$
  1035	[37m				[39;49;00mSET_TOP(Py_False);[37m[39;49;00m$
  1036	[37m				[39;49;00merr[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
  1037	[37m				[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1038	[37m			[39;49;00m}[37m[39;49;00m$
  1039	[37m			[39;49;00mSTACKADJ([34m-1[39;49;00m);[37m[39;49;00m$
  1040	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1041	[37m[39;49;00m$
  1042	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mUNARY_CONVERT[39;49;00m:[37m[39;49;00m$
  1043	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1044	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyObject_Repr(v);[37m[39;49;00m$
  1045	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1046	[37m			[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1047	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1048	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1049	[37m[39;49;00m$
  1050	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mUNARY_INVERT[39;49;00m:[37m[39;49;00m$
  1051	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1052	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_Invert(v);[37m[39;49;00m$
  1053	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1054	[37m			[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1055	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1056	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1057	[37m[39;49;00m$
  1058	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBINARY_POWER[39;49;00m:[37m[39;49;00m$
  1059	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1060	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1061	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_Power(v,[37m [39;49;00mw,[37m [39;49;00mPy_None);[37m[39;49;00m$
  1062	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1063	[37m			[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1064	[37m			[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1065	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1066	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1067	[37m[39;49;00m$
  1068	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBINARY_MULTIPLY[39;49;00m:[37m[39;49;00m$
  1069	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1070	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1071	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_Multiply(v,[37m [39;49;00mw);[37m[39;49;00m$
  1072	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1073	[37m			[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1074	[37m			[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1075	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1076	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1077	[37m[39;49;00m$
  1078	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBINARY_DIVIDE[39;49;00m:[37m[39;49;00m$
  1079	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(!_Py_QnewFlag)[37m [39;49;00m{[37m[39;49;00m$
  1080	[37m				[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1081	[37m				[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1082	[37m				[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_Divide(v,[37m [39;49;00mw);[37m[39;49;00m$
  1083	[37m				[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1084	[37m				[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1085	[37m				[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1086	[37m				[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1087	[37m				[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1088	[37m			[39;49;00m}[37m[39;49;00m$
  1089	[37m			[39;49;00m[37m/* -Qnew is in effect:	fall through to[39;49;00m$
  1090	[37m			   BINARY_TRUE_DIVIDE */[39;49;00m[37m[39;49;00m$
  1091	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBINARY_TRUE_DIVIDE[39;49;00m:[37m[39;49;00m$
  1092	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1093	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1094	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_TrueDivide(v,[37m [39;49;00mw);[37m[39;49;00m$
  1095	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1096	[37m			[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1097	[37m			[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1098	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1099	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1100	[37m[39;49;00m$
  1101	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBINARY_FLOOR_DIVIDE[39;49;00m:[37m[39;49;00m$
  1102	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1103	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1104	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_FloorDivide(v,[37m [39;49;00mw);[37m[39;49;00m$
  1105	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1106	[37m			[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1107	[37m			[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1108	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1109	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1110	[37m[39;49;00m$
  1111	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBINARY_MODULO[39;49;00m:[37m[39;49;00m$
  1112	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1113	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1114	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_Remainder(v,[37m [39;49;00mw);[37m[39;49;00m$
  1115	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1116	[37m			[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1117	[37m			[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1118	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1119	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1120	[37m[39;49;00m$
  1121	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBINARY_ADD[39;49;00m:[37m[39;49;00m$
  1122	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1123	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1124	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyInt_CheckExact(v)[37m [39;49;00m&&[37m [39;49;00mPyInt_CheckExact(w))[37m [39;49;00m{[37m[39;49;00m$
  1125	[37m				[39;49;00m[37m/* INLINE: int + int */[39;49;00m[37m[39;49;00m$
  1126	[37m				[39;49;00m[34mregister[39;49;00m[37m [39;49;00m[36mlong[39;49;00m[37m [39;49;00ma,[37m [39;49;00mb,[37m [39;49;00mi;[37m[39;49;00m$
  1127	[37m				[39;49;00ma[37m [39;49;00m=[37m [39;49;00mPyInt_AS_LONG(v);[37m[39;49;00m$
  1128	[37m				[39;49;00mb[37m [39;49;00m=[37m [39;49;00mPyInt_AS_LONG(w);[37m[39;49;00m$
  1129	[37m				[39;49;00mi[37m [39;49;00m=[37m [39;49;00ma[37m [39;49;00m+[37m [39;49;00mb;[37m[39;49;00m$
  1130	[37m				[39;49;00m[34mif[39;49;00m[37m [39;49;00m((i^a)[37m [39;49;00m<[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m&&[37m [39;49;00m(i^b)[37m [39;49;00m<[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1131	[37m					[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mslow_add;[37m[39;49;00m$
  1132	[37m				[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyInt_FromLong(i);[37m[39;49;00m$
  1133	[37m			[39;49;00m}[37m[39;49;00m$
  1134	[37m			[39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyString_CheckExact(v)[37m [39;49;00m&&[37m[39;49;00m$
  1135	[37m				 [39;49;00mPyString_CheckExact(w))[37m [39;49;00m{[37m[39;49;00m$
  1136	[37m				[39;49;00mx[37m [39;49;00m=[37m [39;49;00mstring_concatenate(v,[37m [39;49;00mw,[37m [39;49;00mf,[37m [39;49;00mnext_instr);[37m[39;49;00m$
  1137	[37m				[39;49;00m[37m/* string_concatenate consumed the ref to v */[39;49;00m[37m[39;49;00m$
  1138	[37m				[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mskip_decref_vx;[37m[39;49;00m$
  1139	[37m			[39;49;00m}[37m[39;49;00m$
  1140	[37m			[39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
  1141	[37m			  [39;49;00mslow_add:[37m[39;49;00m$
  1142	[37m				[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_Add(v,[37m [39;49;00mw);[37m[39;49;00m$
  1143	[37m			[39;49;00m}[37m[39;49;00m$
  1144	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1145	[37m		  [39;49;00mskip_decref_vx:[37m[39;49;00m$
  1146	[37m			[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1147	[37m			[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1148	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1149	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1150	[37m[39;49;00m$
  1151	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBINARY_SUBTRACT[39;49;00m:[37m[39;49;00m$
  1152	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1153	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1154	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyInt_CheckExact(v)[37m [39;49;00m&&[37m [39;49;00mPyInt_CheckExact(w))[37m [39;49;00m{[37m[39;49;00m$
  1155	[37m				[39;49;00m[37m/* INLINE: int - int */[39;49;00m[37m[39;49;00m$
  1156	[37m				[39;49;00m[34mregister[39;49;00m[37m [39;49;00m[36mlong[39;49;00m[37m [39;49;00ma,[37m [39;49;00mb,[37m [39;49;00mi;[37m[39;49;00m$
  1157	[37m				[39;49;00ma[37m [39;49;00m=[37m [39;49;00mPyInt_AS_LONG(v);[37m[39;49;00m$
  1158	[37m				[39;49;00mb[37m [39;49;00m=[37m [39;49;00mPyInt_AS_LONG(w);[37m[39;49;00m$
  1159	[37m				[39;49;00mi[37m [39;49;00m=[37m [39;49;00ma[37m [39;49;00m-[37m [39;49;00mb;[37m[39;49;00m$
  1160	[37m				[39;49;00m[34mif[39;49;00m[37m [39;49;00m((i^a)[37m [39;49;00m<[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m&&[37m [39;49;00m(i^~b)[37m [39;49;00m<[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1161	[37m					[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mslow_sub;[37m[39;49;00m$
  1162	[37m				[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyInt_FromLong(i);[37m[39;49;00m$
  1163	[37m			[39;49;00m}[37m[39;49;00m$
  1164	[37m			[39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
  1165	[37m			  [39;49;00mslow_sub:[37m[39;49;00m$
  1166	[37m				[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_Subtract(v,[37m [39;49;00mw);[37m[39;49;00m$
  1167	[37m			[39;49;00m}[37m[39;49;00m$
  1168	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1169	[37m			[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1170	[37m			[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1171	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1172	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1173	[37m[39;49;00m$
  1174	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBINARY_SUBSCR[39;49;00m:[37m[39;49;00m$
  1175	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1176	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1177	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyList_CheckExact(v)[37m [39;49;00m&&[37m [39;49;00mPyInt_CheckExact(w))[37m [39;49;00m{[37m[39;49;00m$
  1178	[37m				[39;49;00m[37m/* INLINE: list[int] */[39;49;00m[37m[39;49;00m$
  1179	[37m				[39;49;00mPy_ssize_t[37m [39;49;00mi[37m [39;49;00m=[37m [39;49;00mPyInt_AsSsize_t(w);[37m[39;49;00m$
  1180	[37m				[39;49;00m[34mif[39;49;00m[37m [39;49;00m(i[37m [39;49;00m<[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1181	[37m					[39;49;00mi[37m [39;49;00m+=[37m [39;49;00mPyList_GET_SIZE(v);[37m[39;49;00m$
  1182	[37m				[39;49;00m[34mif[39;49;00m[37m [39;49;00m(i[37m [39;49;00m>=[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m&&[37m [39;49;00mi[37m [39;49;00m<[37m [39;49;00mPyList_GET_SIZE(v))[37m [39;49;00m{[37m[39;49;00m$
  1183	[37m					[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyList_GET_ITEM(v,[37m [39;49;00mi);[37m[39;49;00m$
  1184	[37m					[39;49;00mPy_INCREF(x);[37m[39;49;00m$
  1185	[37m				[39;49;00m}[37m[39;49;00m$
  1186	[37m				[39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  1187	[37m					[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mslow_get;[37m[39;49;00m$
  1188	[37m			[39;49;00m}[37m[39;49;00m$
  1189	[37m			[39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  1190	[37m			  [39;49;00mslow_get:[37m[39;49;00m$
  1191	[37m				[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyObject_GetItem(v,[37m [39;49;00mw);[37m[39;49;00m$
  1192	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1193	[37m			[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1194	[37m			[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1195	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1196	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1197	[37m[39;49;00m$
  1198	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBINARY_LSHIFT[39;49;00m:[37m[39;49;00m$
  1199	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1200	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1201	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_Lshift(v,[37m [39;49;00mw);[37m[39;49;00m$
  1202	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1203	[37m			[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1204	[37m			[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1205	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1206	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1207	[37m[39;49;00m$
  1208	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBINARY_RSHIFT[39;49;00m:[37m[39;49;00m$
  1209	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1210	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1211	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_Rshift(v,[37m [39;49;00mw);[37m[39;49;00m$
  1212	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1213	[37m			[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1214	[37m			[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1215	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1216	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1217	[37m[39;49;00m$
  1218	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBINARY_AND[39;49;00m:[37m[39;49;00m$
  1219	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1220	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1221	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_And(v,[37m [39;49;00mw);[37m[39;49;00m$
  1222	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1223	[37m			[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1224	[37m			[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1225	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1226	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1227	[37m[39;49;00m$
  1228	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBINARY_XOR[39;49;00m:[37m[39;49;00m$
  1229	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1230	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1231	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_Xor(v,[37m [39;49;00mw);[37m[39;49;00m$
  1232	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1233	[37m			[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1234	[37m			[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1235	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1236	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1237	[37m[39;49;00m$
  1238	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBINARY_OR[39;49;00m:[37m[39;49;00m$
  1239	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1240	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1241	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_Or(v,[37m [39;49;00mw);[37m[39;49;00m$
  1242	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1243	[37m			[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1244	[37m			[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1245	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1246	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1247	[37m[39;49;00m$
  1248	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mLIST_APPEND[39;49;00m:[37m[39;49;00m$
  1249	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1250	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1251	[37m			[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyList_Append(v,[37m [39;49;00mw);[37m[39;49;00m$
  1252	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1253	[37m			[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1254	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1255	[37m				[39;49;00mPREDICT(JUMP_ABSOLUTE);[37m[39;49;00m$
  1256	[37m				[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1257	[37m			[39;49;00m}[37m[39;49;00m$
  1258	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1259	[37m[39;49;00m$
  1260	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mINPLACE_POWER[39;49;00m:[37m[39;49;00m$
  1261	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1262	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1263	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_InPlacePower(v,[37m [39;49;00mw,[37m [39;49;00mPy_None);[37m[39;49;00m$
  1264	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1265	[37m			[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1266	[37m			[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1267	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1268	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1269	[37m[39;49;00m$
  1270	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mINPLACE_MULTIPLY[39;49;00m:[37m[39;49;00m$
  1271	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1272	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1273	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_InPlaceMultiply(v,[37m [39;49;00mw);[37m[39;49;00m$
  1274	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1275	[37m			[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1276	[37m			[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1277	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1278	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1279	[37m[39;49;00m$
  1280	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mINPLACE_DIVIDE[39;49;00m:[37m[39;49;00m$
  1281	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(!_Py_QnewFlag)[37m [39;49;00m{[37m[39;49;00m$
  1282	[37m				[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1283	[37m				[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1284	[37m				[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_InPlaceDivide(v,[37m [39;49;00mw);[37m[39;49;00m$
  1285	[37m				[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1286	[37m				[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1287	[37m				[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1288	[37m				[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1289	[37m				[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1290	[37m			[39;49;00m}[37m[39;49;00m$
  1291	[37m			[39;49;00m[37m/* -Qnew is in effect:	fall through to[39;49;00m$
  1292	[37m			   INPLACE_TRUE_DIVIDE */[39;49;00m[37m[39;49;00m$
  1293	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mINPLACE_TRUE_DIVIDE[39;49;00m:[37m[39;49;00m$
  1294	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1295	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1296	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_InPlaceTrueDivide(v,[37m [39;49;00mw);[37m[39;49;00m$
  1297	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1298	[37m			[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1299	[37m			[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1300	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1301	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1302	[37m[39;49;00m$
  1303	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mINPLACE_FLOOR_DIVIDE[39;49;00m:[37m[39;49;00m$
  1304	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1305	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1306	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_InPlaceFloorDivide(v,[37m [39;49;00mw);[37m[39;49;00m$
  1307	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1308	[37m			[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1309	[37m			[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1310	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1311	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1312	[37m[39;49;00m$
  1313	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mINPLACE_MODULO[39;49;00m:[37m[39;49;00m$
  1314	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1315	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1316	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_InPlaceRemainder(v,[37m [39;49;00mw);[37m[39;49;00m$
  1317	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1318	[37m			[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1319	[37m			[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1320	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1321	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1322	[37m[39;49;00m$
  1323	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mINPLACE_ADD[39;49;00m:[37m[39;49;00m$
  1324	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1325	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1326	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyInt_CheckExact(v)[37m [39;49;00m&&[37m [39;49;00mPyInt_CheckExact(w))[37m [39;49;00m{[37m[39;49;00m$
  1327	[37m				[39;49;00m[37m/* INLINE: int + int */[39;49;00m[37m[39;49;00m$
  1328	[37m				[39;49;00m[34mregister[39;49;00m[37m [39;49;00m[36mlong[39;49;00m[37m [39;49;00ma,[37m [39;49;00mb,[37m [39;49;00mi;[37m[39;49;00m$
  1329	[37m				[39;49;00ma[37m [39;49;00m=[37m [39;49;00mPyInt_AS_LONG(v);[37m[39;49;00m$
  1330	[37m				[39;49;00mb[37m [39;49;00m=[37m [39;49;00mPyInt_AS_LONG(w);[37m[39;49;00m$
  1331	[37m				[39;49;00mi[37m [39;49;00m=[37m [39;49;00ma[37m [39;49;00m+[37m [39;49;00mb;[37m[39;49;00m$
  1332	[37m				[39;49;00m[34mif[39;49;00m[37m [39;49;00m((i^a)[37m [39;49;00m<[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m&&[37m [39;49;00m(i^b)[37m [39;49;00m<[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1333	[37m					[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mslow_iadd;[37m[39;49;00m$
  1334	[37m				[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyInt_FromLong(i);[37m[39;49;00m$
  1335	[37m			[39;49;00m}[37m[39;49;00m$
  1336	[37m			[39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyString_CheckExact(v)[37m [39;49;00m&&[37m[39;49;00m$
  1337	[37m				 [39;49;00mPyString_CheckExact(w))[37m [39;49;00m{[37m[39;49;00m$
  1338	[37m				[39;49;00mx[37m [39;49;00m=[37m [39;49;00mstring_concatenate(v,[37m [39;49;00mw,[37m [39;49;00mf,[37m [39;49;00mnext_instr);[37m[39;49;00m$
  1339	[37m				[39;49;00m[37m/* string_concatenate consumed the ref to v */[39;49;00m[37m[39;49;00m$
  1340	[37m				[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mskip_decref_v;[37m[39;49;00m$
  1341	[37m			[39;49;00m}[37m[39;49;00m$
  1342	[37m			[39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
  1343	[37m			  [39;49;00mslow_iadd:[37m[39;49;00m$
  1344	[37m				[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_InPlaceAdd(v,[37m [39;49;00mw);[37m[39;49;00m$
  1345	[37m			[39;49;00m}[37m[39;49;00m$
  1346	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1347	[37m		  [39;49;00mskip_decref_v:[37m[39;49;00m$
  1348	[37m			[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1349	[37m			[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1350	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1351	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1352	[37m[39;49;00m$
  1353	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mINPLACE_SUBTRACT[39;49;00m:[37m[39;49;00m$
  1354	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1355	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1356	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyInt_CheckExact(v)[37m [39;49;00m&&[37m [39;49;00mPyInt_CheckExact(w))[37m [39;49;00m{[37m[39;49;00m$
  1357	[37m				[39;49;00m[37m/* INLINE: int - int */[39;49;00m[37m[39;49;00m$
  1358	[37m				[39;49;00m[34mregister[39;49;00m[37m [39;49;00m[36mlong[39;49;00m[37m [39;49;00ma,[37m [39;49;00mb,[37m [39;49;00mi;[37m[39;49;00m$
  1359	[37m				[39;49;00ma[37m [39;49;00m=[37m [39;49;00mPyInt_AS_LONG(v);[37m[39;49;00m$
  1360	[37m				[39;49;00mb[37m [39;49;00m=[37m [39;49;00mPyInt_AS_LONG(w);[37m[39;49;00m$
  1361	[37m				[39;49;00mi[37m [39;49;00m=[37m [39;49;00ma[37m [39;49;00m-[37m [39;49;00mb;[37m[39;49;00m$
  1362	[37m				[39;49;00m[34mif[39;49;00m[37m [39;49;00m((i^a)[37m [39;49;00m<[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m&&[37m [39;49;00m(i^~b)[37m [39;49;00m<[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1363	[37m					[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mslow_isub;[37m[39;49;00m$
  1364	[37m				[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyInt_FromLong(i);[37m[39;49;00m$
  1365	[37m			[39;49;00m}[37m[39;49;00m$
  1366	[37m			[39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
  1367	[37m			  [39;49;00mslow_isub:[37m[39;49;00m$
  1368	[37m				[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_InPlaceSubtract(v,[37m [39;49;00mw);[37m[39;49;00m$
  1369	[37m			[39;49;00m}[37m[39;49;00m$
  1370	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1371	[37m			[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1372	[37m			[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1373	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1374	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1375	[37m[39;49;00m$
  1376	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mINPLACE_LSHIFT[39;49;00m:[37m[39;49;00m$
  1377	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1378	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1379	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_InPlaceLshift(v,[37m [39;49;00mw);[37m[39;49;00m$
  1380	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1381	[37m			[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1382	[37m			[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1383	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1384	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1385	[37m[39;49;00m$
  1386	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mINPLACE_RSHIFT[39;49;00m:[37m[39;49;00m$
  1387	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1388	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1389	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_InPlaceRshift(v,[37m [39;49;00mw);[37m[39;49;00m$
  1390	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1391	[37m			[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1392	[37m			[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1393	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1394	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1395	[37m[39;49;00m$
  1396	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mINPLACE_AND[39;49;00m:[37m[39;49;00m$
  1397	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1398	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1399	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_InPlaceAnd(v,[37m [39;49;00mw);[37m[39;49;00m$
  1400	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1401	[37m			[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1402	[37m			[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1403	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1404	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1405	[37m[39;49;00m$
  1406	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mINPLACE_XOR[39;49;00m:[37m[39;49;00m$
  1407	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1408	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1409	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_InPlaceXor(v,[37m [39;49;00mw);[37m[39;49;00m$
  1410	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1411	[37m			[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1412	[37m			[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1413	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1414	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1415	[37m[39;49;00m$
  1416	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mINPLACE_OR[39;49;00m:[37m[39;49;00m$
  1417	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1418	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1419	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyNumber_InPlaceOr(v,[37m [39;49;00mw);[37m[39;49;00m$
  1420	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1421	[37m			[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1422	[37m			[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1423	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1424	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1425	[37m[39;49;00m$
  1426	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSLICE[39;49;00m+[34m0[39;49;00m:[37m[39;49;00m$
  1427	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSLICE[39;49;00m+[34m1[39;49;00m:[37m[39;49;00m$
  1428	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSLICE[39;49;00m+[34m2[39;49;00m:[37m[39;49;00m$
  1429	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSLICE[39;49;00m+[34m3[39;49;00m:[37m[39;49;00m$
  1430	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m((opcode-SLICE)[37m [39;49;00m&[37m [39;49;00m[34m2[39;49;00m)[37m[39;49;00m$
  1431	[37m				[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1432	[37m			[39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  1433	[37m				[39;49;00mw[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  1434	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m((opcode-SLICE)[37m [39;49;00m&[37m [39;49;00m[34m1[39;49;00m)[37m[39;49;00m$
  1435	[37m				[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1436	[37m			[39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  1437	[37m				[39;49;00mv[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  1438	[37m			[39;49;00mu[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1439	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mapply_slice(u,[37m [39;49;00mv,[37m [39;49;00mw);[37m[39;49;00m$
  1440	[37m			[39;49;00mPy_DECREF(u);[37m[39;49;00m$
  1441	[37m			[39;49;00mPy_XDECREF(v);[37m[39;49;00m$
  1442	[37m			[39;49;00mPy_XDECREF(w);[37m[39;49;00m$
  1443	[37m			[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1444	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1445	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1446	[37m[39;49;00m$
  1447	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSTORE_SLICE[39;49;00m+[34m0[39;49;00m:[37m[39;49;00m$
  1448	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSTORE_SLICE[39;49;00m+[34m1[39;49;00m:[37m[39;49;00m$
  1449	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSTORE_SLICE[39;49;00m+[34m2[39;49;00m:[37m[39;49;00m$
  1450	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSTORE_SLICE[39;49;00m+[34m3[39;49;00m:[37m[39;49;00m$
  1451	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m((opcode-STORE_SLICE)[37m [39;49;00m&[37m [39;49;00m[34m2[39;49;00m)[37m[39;49;00m$
  1452	[37m				[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1453	[37m			[39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  1454	[37m				[39;49;00mw[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  1455	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m((opcode-STORE_SLICE)[37m [39;49;00m&[37m [39;49;00m[34m1[39;49;00m)[37m[39;49;00m$
  1456	[37m				[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1457	[37m			[39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  1458	[37m				[39;49;00mv[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  1459	[37m			[39;49;00mu[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1460	[37m			[39;49;00mt[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1461	[37m			[39;49;00merr[37m [39;49;00m=[37m [39;49;00massign_slice(u,[37m [39;49;00mv,[37m [39;49;00mw,[37m [39;49;00mt);[37m [39;49;00m[37m/* u[v:w] = t */[39;49;00m[37m[39;49;00m$
  1462	[37m			[39;49;00mPy_DECREF(t);[37m[39;49;00m$
  1463	[37m			[39;49;00mPy_DECREF(u);[37m[39;49;00m$
  1464	[37m			[39;49;00mPy_XDECREF(v);[37m[39;49;00m$
  1465	[37m			[39;49;00mPy_XDECREF(w);[37m[39;49;00m$
  1466	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1467	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1468	[37m[39;49;00m$
  1469	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mDELETE_SLICE[39;49;00m+[34m0[39;49;00m:[37m[39;49;00m$
  1470	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mDELETE_SLICE[39;49;00m+[34m1[39;49;00m:[37m[39;49;00m$
  1471	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mDELETE_SLICE[39;49;00m+[34m2[39;49;00m:[37m[39;49;00m$
  1472	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mDELETE_SLICE[39;49;00m+[34m3[39;49;00m:[37m[39;49;00m$
  1473	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m((opcode-DELETE_SLICE)[37m [39;49;00m&[37m [39;49;00m[34m2[39;49;00m)[37m[39;49;00m$
  1474	[37m				[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1475	[37m			[39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  1476	[37m				[39;49;00mw[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  1477	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m((opcode-DELETE_SLICE)[37m [39;49;00m&[37m [39;49;00m[34m1[39;49;00m)[37m[39;49;00m$
  1478	[37m				[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1479	[37m			[39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  1480	[37m				[39;49;00mv[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  1481	[37m			[39;49;00mu[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1482	[37m			[39;49;00merr[37m [39;49;00m=[37m [39;49;00massign_slice(u,[37m [39;49;00mv,[37m [39;49;00mw,[37m [39;49;00m(PyObject[37m [39;49;00m*)[36mNULL[39;49;00m);[37m[39;49;00m$
  1483	[37m							[39;49;00m[37m/* del u[v:w] */[39;49;00m[37m[39;49;00m$
  1484	[37m			[39;49;00mPy_DECREF(u);[37m[39;49;00m$
  1485	[37m			[39;49;00mPy_XDECREF(v);[37m[39;49;00m$
  1486	[37m			[39;49;00mPy_XDECREF(w);[37m[39;49;00m$
  1487	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1488	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1489	[37m[39;49;00m$
  1490	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSTORE_SUBSCR[39;49;00m:[37m[39;49;00m$
  1491	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1492	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mSECOND();[37m[39;49;00m$
  1493	[37m			[39;49;00mu[37m [39;49;00m=[37m [39;49;00mTHIRD();[37m[39;49;00m$
  1494	[37m			[39;49;00mSTACKADJ([34m-3[39;49;00m);[37m[39;49;00m$
  1495	[37m			[39;49;00m[37m/* v[w] = u */[39;49;00m[37m[39;49;00m$
  1496	[37m			[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyObject_SetItem(v,[37m [39;49;00mw,[37m [39;49;00mu);[37m[39;49;00m$
  1497	[37m			[39;49;00mPy_DECREF(u);[37m[39;49;00m$
  1498	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1499	[37m			[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1500	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1501	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1502	[37m[39;49;00m$
  1503	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mDELETE_SUBSCR[39;49;00m:[37m[39;49;00m$
  1504	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1505	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mSECOND();[37m[39;49;00m$
  1506	[37m			[39;49;00mSTACKADJ([34m-2[39;49;00m);[37m[39;49;00m$
  1507	[37m			[39;49;00m[37m/* del v[w] */[39;49;00m[37m[39;49;00m$
  1508	[37m			[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyObject_DelItem(v,[37m [39;49;00mw);[37m[39;49;00m$
  1509	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1510	[37m			[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1511	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1512	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1513	[37m[39;49;00m$
  1514	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mPRINT_EXPR[39;49;00m:[37m[39;49;00m$
  1515	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1516	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPySys_GetObject([33m"[39;49;00m[33mdisplayhook[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
  1517	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(w[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1518	[37m				[39;49;00mPyErr_SetString(PyExc_RuntimeError,[37m[39;49;00m$
  1519	[37m						[39;49;00m[33m"[39;49;00m[33mlost sys.displayhook[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
  1520	[37m				[39;49;00merr[37m [39;49;00m=[37m [39;49;00m[34m-1[39;49;00m;[37m[39;49;00m$
  1521	[37m				[39;49;00mx[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  1522	[37m			[39;49;00m}[37m[39;49;00m$
  1523	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1524	[37m				[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyTuple_Pack([34m1[39;49;00m,[37m [39;49;00mv);[37m[39;49;00m$
  1525	[37m				[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
  1526	[37m					[39;49;00merr[37m [39;49;00m=[37m [39;49;00m[34m-1[39;49;00m;[37m[39;49;00m$
  1527	[37m			[39;49;00m}[37m[39;49;00m$
  1528	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1529	[37m				[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPyEval_CallObject(w,[37m [39;49;00mx);[37m[39;49;00m$
  1530	[37m				[39;49;00mPy_XDECREF(w);[37m[39;49;00m$
  1531	[37m				[39;49;00m[34mif[39;49;00m[37m [39;49;00m(w[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
  1532	[37m					[39;49;00merr[37m [39;49;00m=[37m [39;49;00m[34m-1[39;49;00m;[37m[39;49;00m$
  1533	[37m			[39;49;00m}[37m[39;49;00m$
  1534	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1535	[37m			[39;49;00mPy_XDECREF(x);[37m[39;49;00m$
  1536	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1537	[37m[39;49;00m$
  1538	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mPRINT_ITEM_TO[39;49;00m:[37m[39;49;00m$
  1539	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mstream[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1540	[37m			[39;49;00m[37m/* fall through to PRINT_ITEM */[39;49;00m[37m[39;49;00m$
  1541	[37m[39;49;00m$
  1542	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mPRINT_ITEM[39;49;00m:[37m[39;49;00m$
  1543	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1544	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(stream[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m[37m [39;49;00m||[37m [39;49;00mstream[37m [39;49;00m==[37m [39;49;00mPy_None)[37m [39;49;00m{[37m[39;49;00m$
  1545	[37m				[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPySys_GetObject([33m"[39;49;00m[33mstdout[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
  1546	[37m				[39;49;00m[34mif[39;49;00m[37m [39;49;00m(w[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1547	[37m					[39;49;00mPyErr_SetString(PyExc_RuntimeError,[37m[39;49;00m$
  1548	[37m							[39;49;00m[33m"[39;49;00m[33mlost sys.stdout[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
  1549	[37m					[39;49;00merr[37m [39;49;00m=[37m [39;49;00m[34m-1[39;49;00m;[37m[39;49;00m$
  1550	[37m				[39;49;00m}[37m[39;49;00m$
  1551	[37m			[39;49;00m}[37m[39;49;00m$
  1552	[37m			[39;49;00m[37m/* PyFile_SoftSpace() can exececute arbitrary code[39;49;00m$
  1553	[37m			   if sys.stdout is an instance with a __getattr__.[39;49;00m$
  1554	[37m			   If __getattr__ raises an exception, w will[39;49;00m$
  1555	[37m			   be freed, so we need to prevent that temporarily. */[39;49;00m[37m[39;49;00m$
  1556	[37m			[39;49;00mPy_XINCREF(w);[37m[39;49;00m$
  1557	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(w[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m[37m [39;49;00m&&[37m [39;49;00mPyFile_SoftSpace(w,[37m [39;49;00m[34m0[39;49;00m))[37m[39;49;00m$
  1558	[37m				[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyFile_WriteString([33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m,[37m [39;49;00mw);[37m[39;49;00m$
  1559	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1560	[37m				[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyFile_WriteObject(v,[37m [39;49;00mw,[37m [39;49;00mPy_PRINT_RAW);[37m[39;49;00m$
  1561	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1562	[37m			    [39;49;00m[37m/* XXX move into writeobject() ? */[39;49;00m[37m[39;49;00m$
  1563	[37m			    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyString_Check(v))[37m [39;49;00m{[37m[39;49;00m$
  1564	[37m				[39;49;00m[36mchar[39;49;00m[37m [39;49;00m*s[37m [39;49;00m=[37m [39;49;00mPyString_AS_STRING(v);[37m[39;49;00m$
  1565	[37m				[39;49;00mPy_ssize_t[37m [39;49;00mlen[37m [39;49;00m=[37m [39;49;00mPyString_GET_SIZE(v);[37m[39;49;00m$
  1566	[37m				[39;49;00m[34mif[39;49;00m[37m [39;49;00m(len[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m||[37m[39;49;00m$
  1567	[37m				    [39;49;00m!isspace(Py_CHARMASK(s[len[34m-1[39;49;00m]))[37m [39;49;00m||[37m[39;49;00m$
  1568	[37m				    [39;49;00ms[len[34m-1[39;49;00m][37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
  1569	[37m					[39;49;00mPyFile_SoftSpace(w,[37m [39;49;00m[34m1[39;49;00m);[37m[39;49;00m$
  1570	[37m			    [39;49;00m}[37m[39;49;00m$
  1571	[36m#[39;49;00m[36mifdef Py_USING_UNICODE[39;49;00m[36m[39;49;00m$
  1572	[37m			    [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyUnicode_Check(v))[37m [39;49;00m{[37m[39;49;00m$
  1573	[37m				[39;49;00mPy_UNICODE[37m [39;49;00m*s[37m [39;49;00m=[37m [39;49;00mPyUnicode_AS_UNICODE(v);[37m[39;49;00m$
  1574	[37m				[39;49;00mPy_ssize_t[37m [39;49;00mlen[37m [39;49;00m=[37m [39;49;00mPyUnicode_GET_SIZE(v);[37m[39;49;00m$
  1575	[37m				[39;49;00m[34mif[39;49;00m[37m [39;49;00m(len[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m||[37m[39;49;00m$
  1576	[37m				    [39;49;00m!Py_UNICODE_ISSPACE(s[len[34m-1[39;49;00m])[37m [39;49;00m||[37m[39;49;00m$
  1577	[37m				    [39;49;00ms[len[34m-1[39;49;00m][37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
  1578	[37m				    [39;49;00mPyFile_SoftSpace(w,[37m [39;49;00m[34m1[39;49;00m);[37m[39;49;00m$
  1579	[37m			    [39;49;00m}[37m[39;49;00m$
  1580	[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
  1581	[37m			    [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  1582	[37m			    	[39;49;00mPyFile_SoftSpace(w,[37m [39;49;00m[34m1[39;49;00m);[37m[39;49;00m$
  1583	[37m			[39;49;00m}[37m[39;49;00m$
  1584	[37m			[39;49;00mPy_XDECREF(w);[37m[39;49;00m$
  1585	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1586	[37m			[39;49;00mPy_XDECREF(stream);[37m[39;49;00m$
  1587	[37m			[39;49;00mstream[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  1588	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1589	[37m				[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1590	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1591	[37m[39;49;00m$
  1592	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mPRINT_NEWLINE_TO[39;49;00m:[37m[39;49;00m$
  1593	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mstream[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1594	[37m			[39;49;00m[37m/* fall through to PRINT_NEWLINE */[39;49;00m[37m[39;49;00m$
  1595	[37m[39;49;00m$
  1596	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mPRINT_NEWLINE[39;49;00m:[37m[39;49;00m$
  1597	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(stream[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m[37m [39;49;00m||[37m [39;49;00mstream[37m [39;49;00m==[37m [39;49;00mPy_None)[37m [39;49;00m{[37m[39;49;00m$
  1598	[37m				[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPySys_GetObject([33m"[39;49;00m[33mstdout[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
  1599	[37m				[39;49;00m[34mif[39;49;00m[37m [39;49;00m(w[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
  1600	[37m					[39;49;00mPyErr_SetString(PyExc_RuntimeError,[37m[39;49;00m$
  1601	[37m							[39;49;00m[33m"[39;49;00m[33mlost sys.stdout[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
  1602	[37m			[39;49;00m}[37m[39;49;00m$
  1603	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(w[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1604	[37m				[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyFile_WriteString([33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m,[37m [39;49;00mw);[37m[39;49;00m$
  1605	[37m				[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1606	[37m					[39;49;00mPyFile_SoftSpace(w,[37m [39;49;00m[34m0[39;49;00m);[37m[39;49;00m$
  1607	[37m			[39;49;00m}[37m[39;49;00m$
  1608	[37m			[39;49;00mPy_XDECREF(stream);[37m[39;49;00m$
  1609	[37m			[39;49;00mstream[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  1610	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1611	[37m[39;49;00m$
  1612	[37m[39;49;00m$
  1613	[36m#[39;49;00m[36mifdef CASE_TOO_BIG[39;49;00m[36m[39;49;00m$
  1614	[37m		[39;49;00m[34mdefault[39;49;00m:[37m [39;49;00m[34mswitch[39;49;00m[37m [39;49;00m(opcode)[37m [39;49;00m{[37m[39;49;00m$
  1615	[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
  1616	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mRAISE_VARARGS[39;49;00m:[37m[39;49;00m$
  1617	[37m			[39;49;00mu[37m [39;49;00m=[37m [39;49;00mv[37m [39;49;00m=[37m [39;49;00mw[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  1618	[37m			[39;49;00m[34mswitch[39;49;00m[37m [39;49;00m(oparg)[37m [39;49;00m{[37m[39;49;00m$
  1619	[37m			[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[34m3[39;49;00m:[37m[39;49;00m$
  1620	[37m				[39;49;00mu[37m [39;49;00m=[37m [39;49;00mPOP();[37m [39;49;00m[37m/* traceback */[39;49;00m[37m[39;49;00m$
  1621	[37m				[39;49;00m[37m/* Fallthrough */[39;49;00m[37m[39;49;00m$
  1622	[37m			[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[34m2[39;49;00m:[37m[39;49;00m$
  1623	[37m				[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m [39;49;00m[37m/* value */[39;49;00m[37m[39;49;00m$
  1624	[37m				[39;49;00m[37m/* Fallthrough */[39;49;00m[37m[39;49;00m$
  1625	[37m			[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[34m1[39;49;00m:[37m[39;49;00m$
  1626	[37m				[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m [39;49;00m[37m/* exc */[39;49;00m[37m[39;49;00m$
  1627	[37m			[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[34m0[39;49;00m:[37m [39;49;00m[37m/* Fallthrough */[39;49;00m[37m[39;49;00m$
  1628	[37m				[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mdo_raise(w,[37m [39;49;00mv,[37m [39;49;00mu);[37m[39;49;00m$
  1629	[37m				[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1630	[37m			[39;49;00m[34mdefault[39;49;00m:[37m[39;49;00m$
  1631	[37m				[39;49;00mPyErr_SetString(PyExc_SystemError,[37m[39;49;00m$
  1632	[37m					   [39;49;00m[33m"[39;49;00m[33mbad RAISE_VARARGS oparg[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
  1633	[37m				[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_EXCEPTION;[37m[39;49;00m$
  1634	[37m				[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1635	[37m			[39;49;00m}[37m[39;49;00m$
  1636	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1637	[37m[39;49;00m$
  1638	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mLOAD_LOCALS[39;49;00m:[37m[39;49;00m$
  1639	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m((x[37m [39;49;00m=[37m [39;49;00mf->f_locals)[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1640	[37m				[39;49;00mPy_INCREF(x);[37m[39;49;00m$
  1641	[37m				[39;49;00mPUSH(x);[37m[39;49;00m$
  1642	[37m				[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1643	[37m			[39;49;00m}[37m[39;49;00m$
  1644	[37m			[39;49;00mPyErr_SetString(PyExc_SystemError,[37m [39;49;00m[33m"[39;49;00m[33mno locals[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
  1645	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1646	[37m[39;49;00m$
  1647	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mRETURN_VALUE[39;49;00m:[37m[39;49;00m$
  1648	[37m			[39;49;00mretval[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1649	[37m			[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_RETURN;[37m[39;49;00m$
  1650	[37m			[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_block_end;[37m[39;49;00m$
  1651	[37m[39;49;00m$
  1652	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mYIELD_VALUE[39;49;00m:[37m[39;49;00m$
  1653	[37m			[39;49;00mretval[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1654	[37m			[39;49;00mf->f_stacktop[37m [39;49;00m=[37m [39;49;00mstack_pointer;[37m[39;49;00m$
  1655	[37m			[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_YIELD;[37m[39;49;00m$
  1656	[37m			[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_yield;[37m[39;49;00m$
  1657	[37m[39;49;00m$
  1658	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mEXEC_STMT[39;49;00m:[37m[39;49;00m$
  1659	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1660	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mSECOND();[37m[39;49;00m$
  1661	[37m			[39;49;00mu[37m [39;49;00m=[37m [39;49;00mTHIRD();[37m[39;49;00m$
  1662	[37m			[39;49;00mSTACKADJ([34m-3[39;49;00m);[37m[39;49;00m$
  1663	[37m			[39;49;00mREAD_TIMESTAMP(intr0);[37m[39;49;00m$
  1664	[37m			[39;49;00merr[37m [39;49;00m=[37m [39;49;00mexec_statement(f,[37m [39;49;00mu,[37m [39;49;00mv,[37m [39;49;00mw);[37m[39;49;00m$
  1665	[37m			[39;49;00mREAD_TIMESTAMP(intr1);[37m[39;49;00m$
  1666	[37m			[39;49;00mPy_DECREF(u);[37m[39;49;00m$
  1667	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1668	[37m			[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1669	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1670	[37m[39;49;00m$
  1671	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mPOP_BLOCK[39;49;00m:[37m[39;49;00m$
  1672	[37m			[39;49;00m{[37m[39;49;00m$
  1673	[37m				[39;49;00mPyTryBlock[37m [39;49;00m*b[37m [39;49;00m=[37m [39;49;00mPyFrame_BlockPop(f);[37m[39;49;00m$
  1674	[37m				[39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(STACK_LEVEL()[37m [39;49;00m>[37m [39;49;00mb->b_level)[37m [39;49;00m{[37m[39;49;00m$
  1675	[37m					[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1676	[37m					[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1677	[37m				[39;49;00m}[37m[39;49;00m$
  1678	[37m			[39;49;00m}[37m[39;49;00m$
  1679	[37m			[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1680	[37m[39;49;00m$
  1681	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mEND_FINALLY[39;49;00m:[37m[39;49;00m$
  1682	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1683	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyInt_Check(v))[37m [39;49;00m{[37m[39;49;00m$
  1684	[37m				[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00m([34menum[39;49;00m[37m [39;49;00mwhy_code)[37m [39;49;00mPyInt_AS_LONG(v);[37m[39;49;00m$
  1685	[37m				[39;49;00massert(why[37m [39;49;00m!=[37m [39;49;00mWHY_YIELD);[37m[39;49;00m$
  1686	[37m				[39;49;00m[34mif[39;49;00m[37m [39;49;00m(why[37m [39;49;00m==[37m [39;49;00mWHY_RETURN[37m [39;49;00m||[37m[39;49;00m$
  1687	[37m				    [39;49;00mwhy[37m [39;49;00m==[37m [39;49;00mWHY_CONTINUE)[37m[39;49;00m$
  1688	[37m					[39;49;00mretval[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1689	[37m			[39;49;00m}[37m[39;49;00m$
  1690	[37m			[39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyExceptionClass_Check(v)[37m [39;49;00m||[37m [39;49;00mPyString_Check(v))[37m [39;49;00m{[37m[39;49;00m$
  1691	[37m				[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1692	[37m				[39;49;00mu[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1693	[37m				[39;49;00mPyErr_Restore(v,[37m [39;49;00mw,[37m [39;49;00mu);[37m[39;49;00m$
  1694	[37m				[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_RERAISE;[37m[39;49;00m$
  1695	[37m				[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1696	[37m			[39;49;00m}[37m[39;49;00m$
  1697	[37m			[39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(v[37m [39;49;00m!=[37m [39;49;00mPy_None)[37m [39;49;00m{[37m[39;49;00m$
  1698	[37m				[39;49;00mPyErr_SetString(PyExc_SystemError,[37m[39;49;00m$
  1699	[37m					[39;49;00m[33m"[39;49;00m[33m'finally' pops bad exception[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
  1700	[37m				[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_EXCEPTION;[37m[39;49;00m$
  1701	[37m			[39;49;00m}[37m[39;49;00m$
  1702	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1703	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1704	[37m[39;49;00m$
  1705	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBUILD_CLASS[39;49;00m:[37m[39;49;00m$
  1706	[37m			[39;49;00mu[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1707	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mSECOND();[37m[39;49;00m$
  1708	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mTHIRD();[37m[39;49;00m$
  1709	[37m			[39;49;00mSTACKADJ([34m-2[39;49;00m);[37m[39;49;00m$
  1710	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mbuild_class(u,[37m [39;49;00mv,[37m [39;49;00mw);[37m[39;49;00m$
  1711	[37m			[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1712	[37m			[39;49;00mPy_DECREF(u);[37m[39;49;00m$
  1713	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1714	[37m			[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1715	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1716	[37m[39;49;00m$
  1717	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSTORE_NAME[39;49;00m:[37m[39;49;00m$
  1718	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mGETITEM(names,[37m [39;49;00moparg);[37m[39;49;00m$
  1719	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1720	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m((x[37m [39;49;00m=[37m [39;49;00mf->f_locals)[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1721	[37m				[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyDict_CheckExact(x))[37m[39;49;00m$
  1722	[37m					[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyDict_SetItem(x,[37m [39;49;00mw,[37m [39;49;00mv);[37m[39;49;00m$
  1723	[37m				[39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  1724	[37m					[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyObject_SetItem(x,[37m [39;49;00mw,[37m [39;49;00mv);[37m[39;49;00m$
  1725	[37m				[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1726	[37m				[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1727	[37m				[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1728	[37m			[39;49;00m}[37m[39;49;00m$
  1729	[37m			[39;49;00mPyErr_Format(PyExc_SystemError,[37m[39;49;00m$
  1730	[37m				     [39;49;00m[33m"[39;49;00m[33mno locals found when storing %s[39;49;00m[33m"[39;49;00m,[37m[39;49;00m$
  1731	[37m				     [39;49;00mPyObject_REPR(w));[37m[39;49;00m$
  1732	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1733	[37m[39;49;00m$
  1734	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mDELETE_NAME[39;49;00m:[37m[39;49;00m$
  1735	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mGETITEM(names,[37m [39;49;00moparg);[37m[39;49;00m$
  1736	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m((x[37m [39;49;00m=[37m [39;49;00mf->f_locals)[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1737	[37m				[39;49;00m[34mif[39;49;00m[37m [39;49;00m((err[37m [39;49;00m=[37m [39;49;00mPyObject_DelItem(x,[37m [39;49;00mw))[37m [39;49;00m!=[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1738	[37m					[39;49;00mformat_exc_check_arg(PyExc_NameError,[37m[39;49;00m$
  1739	[37m								[39;49;00mNAME_ERROR_MSG[37m [39;49;00m,w);[37m[39;49;00m$
  1740	[37m				[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1741	[37m			[39;49;00m}[37m[39;49;00m$
  1742	[37m			[39;49;00mPyErr_Format(PyExc_SystemError,[37m[39;49;00m$
  1743	[37m				     [39;49;00m[33m"[39;49;00m[33mno locals when deleting %s[39;49;00m[33m"[39;49;00m,[37m[39;49;00m$
  1744	[37m				     [39;49;00mPyObject_REPR(w));[37m[39;49;00m$
  1745	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1746	[37m[39;49;00m$
  1747	[37m		[39;49;00mPREDICTED_WITH_ARG(UNPACK_SEQUENCE);[37m[39;49;00m$
  1748	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mUNPACK_SEQUENCE[39;49;00m:[37m[39;49;00m$
  1749	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1750	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyTuple_CheckExact(v)[37m [39;49;00m&&[37m [39;49;00mPyTuple_GET_SIZE(v)[37m [39;49;00m==[37m [39;49;00moparg)[37m [39;49;00m{[37m[39;49;00m$
  1751	[37m				[39;49;00mPyObject[37m [39;49;00m**items[37m [39;49;00m=[37m [39;49;00m((PyTupleObject[37m [39;49;00m*)v)->ob_item;[37m[39;49;00m$
  1752	[37m				[39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(oparg--)[37m [39;49;00m{[37m[39;49;00m$
  1753	[37m					[39;49;00mw[37m [39;49;00m=[37m [39;49;00mitems[oparg];[37m[39;49;00m$
  1754	[37m					[39;49;00mPy_INCREF(w);[37m[39;49;00m$
  1755	[37m					[39;49;00mPUSH(w);[37m[39;49;00m$
  1756	[37m				[39;49;00m}[37m[39;49;00m$
  1757	[37m				[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1758	[37m				[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1759	[37m			[39;49;00m}[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyList_CheckExact(v)[37m [39;49;00m&&[37m [39;49;00mPyList_GET_SIZE(v)[37m [39;49;00m==[37m [39;49;00moparg)[37m [39;49;00m{[37m[39;49;00m$
  1760	[37m				[39;49;00mPyObject[37m [39;49;00m**items[37m [39;49;00m=[37m [39;49;00m((PyListObject[37m [39;49;00m*)v)->ob_item;[37m[39;49;00m$
  1761	[37m				[39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(oparg--)[37m [39;49;00m{[37m[39;49;00m$
  1762	[37m					[39;49;00mw[37m [39;49;00m=[37m [39;49;00mitems[oparg];[37m[39;49;00m$
  1763	[37m					[39;49;00mPy_INCREF(w);[37m[39;49;00m$
  1764	[37m					[39;49;00mPUSH(w);[37m[39;49;00m$
  1765	[37m				[39;49;00m}[37m[39;49;00m$
  1766	[37m			[39;49;00m}[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(unpack_iterable(v,[37m [39;49;00moparg,[37m[39;49;00m$
  1767	[37m						 [39;49;00mstack_pointer[37m [39;49;00m+[37m [39;49;00moparg))[37m[39;49;00m$
  1768	[37m				[39;49;00mstack_pointer[37m [39;49;00m+=[37m [39;49;00moparg;[37m[39;49;00m$
  1769	[37m			[39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
  1770	[37m				[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyErr_ExceptionMatches(PyExc_TypeError))[37m[39;49;00m$
  1771	[37m					[39;49;00mPyErr_SetString(PyExc_TypeError,[37m[39;49;00m$
  1772	[37m						[39;49;00m[33m"[39;49;00m[33munpack non-sequence[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
  1773	[37m				[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_EXCEPTION;[37m[39;49;00m$
  1774	[37m			[39;49;00m}[37m[39;49;00m$
  1775	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1776	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1777	[37m[39;49;00m$
  1778	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSTORE_ATTR[39;49;00m:[37m[39;49;00m$
  1779	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mGETITEM(names,[37m [39;49;00moparg);[37m[39;49;00m$
  1780	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1781	[37m			[39;49;00mu[37m [39;49;00m=[37m [39;49;00mSECOND();[37m[39;49;00m$
  1782	[37m			[39;49;00mSTACKADJ([34m-2[39;49;00m);[37m[39;49;00m$
  1783	[37m			[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyObject_SetAttr(v,[37m [39;49;00mw,[37m [39;49;00mu);[37m [39;49;00m[37m/* v.w = u */[39;49;00m[37m[39;49;00m$
  1784	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1785	[37m			[39;49;00mPy_DECREF(u);[37m[39;49;00m$
  1786	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1787	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1788	[37m[39;49;00m$
  1789	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mDELETE_ATTR[39;49;00m:[37m[39;49;00m$
  1790	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mGETITEM(names,[37m [39;49;00moparg);[37m[39;49;00m$
  1791	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1792	[37m			[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyObject_SetAttr(v,[37m [39;49;00mw,[37m [39;49;00m(PyObject[37m [39;49;00m*)[36mNULL[39;49;00m);[37m[39;49;00m$
  1793	[37m							[39;49;00m[37m/* del v.w */[39;49;00m[37m[39;49;00m$
  1794	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1795	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1796	[37m[39;49;00m$
  1797	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSTORE_GLOBAL[39;49;00m:[37m[39;49;00m$
  1798	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mGETITEM(names,[37m [39;49;00moparg);[37m[39;49;00m$
  1799	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1800	[37m			[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyDict_SetItem(f->f_globals,[37m [39;49;00mw,[37m [39;49;00mv);[37m[39;49;00m$
  1801	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1802	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1803	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1804	[37m[39;49;00m$
  1805	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mDELETE_GLOBAL[39;49;00m:[37m[39;49;00m$
  1806	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mGETITEM(names,[37m [39;49;00moparg);[37m[39;49;00m$
  1807	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m((err[37m [39;49;00m=[37m [39;49;00mPyDict_DelItem(f->f_globals,[37m [39;49;00mw))[37m [39;49;00m!=[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1808	[37m				[39;49;00mformat_exc_check_arg([37m[39;49;00m$
  1809	[37m				    [39;49;00mPyExc_NameError,[37m [39;49;00mGLOBAL_NAME_ERROR_MSG,[37m [39;49;00mw);[37m[39;49;00m$
  1810	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1811	[37m[39;49;00m$
  1812	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mLOAD_NAME[39;49;00m:[37m[39;49;00m$
  1813	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mGETITEM(names,[37m [39;49;00moparg);[37m[39;49;00m$
  1814	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m((v[37m [39;49;00m=[37m [39;49;00mf->f_locals)[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1815	[37m				[39;49;00mPyErr_Format(PyExc_SystemError,[37m[39;49;00m$
  1816	[37m					     [39;49;00m[33m"[39;49;00m[33mno locals when loading %s[39;49;00m[33m"[39;49;00m,[37m[39;49;00m$
  1817	[37m					     [39;49;00mPyObject_REPR(w));[37m[39;49;00m$
  1818	[37m				[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1819	[37m			[39;49;00m}[37m[39;49;00m$
  1820	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyDict_CheckExact(v))[37m [39;49;00m{[37m[39;49;00m$
  1821	[37m				[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyDict_GetItem(v,[37m [39;49;00mw);[37m[39;49;00m$
  1822	[37m				[39;49;00mPy_XINCREF(x);[37m[39;49;00m$
  1823	[37m			[39;49;00m}[37m[39;49;00m$
  1824	[37m			[39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
  1825	[37m				[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyObject_GetItem(v,[37m [39;49;00mw);[37m[39;49;00m$
  1826	[37m				[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m[37m [39;49;00m&&[37m [39;49;00mPyErr_Occurred())[37m [39;49;00m{[37m[39;49;00m$
  1827	[37m					[39;49;00m[34mif[39;49;00m[37m [39;49;00m(!PyErr_ExceptionMatches(PyExc_KeyError))[37m[39;49;00m$
  1828	[37m						[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1829	[37m					[39;49;00mPyErr_Clear();[37m[39;49;00m$
  1830	[37m				[39;49;00m}[37m[39;49;00m$
  1831	[37m			[39;49;00m}[37m[39;49;00m$
  1832	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1833	[37m				[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyDict_GetItem(f->f_globals,[37m [39;49;00mw);[37m[39;49;00m$
  1834	[37m				[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1835	[37m					[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyDict_GetItem(f->f_builtins,[37m [39;49;00mw);[37m[39;49;00m$
  1836	[37m					[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1837	[37m						[39;49;00mformat_exc_check_arg([37m[39;49;00m$
  1838	[37m							    [39;49;00mPyExc_NameError,[37m[39;49;00m$
  1839	[37m							    [39;49;00mNAME_ERROR_MSG[37m [39;49;00m,w);[37m[39;49;00m$
  1840	[37m						[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1841	[37m					[39;49;00m}[37m[39;49;00m$
  1842	[37m				[39;49;00m}[37m[39;49;00m$
  1843	[37m				[39;49;00mPy_INCREF(x);[37m[39;49;00m$
  1844	[37m			[39;49;00m}[37m[39;49;00m$
  1845	[37m			[39;49;00mPUSH(x);[37m[39;49;00m$
  1846	[37m			[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1847	[37m[39;49;00m$
  1848	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mLOAD_GLOBAL[39;49;00m:[37m[39;49;00m$
  1849	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mGETITEM(names,[37m [39;49;00moparg);[37m[39;49;00m$
  1850	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyString_CheckExact(w))[37m [39;49;00m{[37m[39;49;00m$
  1851	[37m				[39;49;00m[37m/* Inline the PyDict_GetItem() calls.[39;49;00m$
  1852	[37m				   WARNING: this is an extreme speed hack.[39;49;00m$
  1853	[37m				   Do not try this at home. */[39;49;00m[37m[39;49;00m$
  1854	[37m				[39;49;00m[36mlong[39;49;00m[37m [39;49;00mhash[37m [39;49;00m=[37m [39;49;00m((PyStringObject[37m [39;49;00m*)w)->ob_shash;[37m[39;49;00m$
  1855	[37m				[39;49;00m[34mif[39;49;00m[37m [39;49;00m(hash[37m [39;49;00m!=[37m [39;49;00m[34m-1[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1856	[37m					[39;49;00mPyDictObject[37m [39;49;00m*d;[37m[39;49;00m$
  1857	[37m					[39;49;00mPyDictEntry[37m [39;49;00m*e;[37m[39;49;00m$
  1858	[37m					[39;49;00md[37m [39;49;00m=[37m [39;49;00m(PyDictObject[37m [39;49;00m*)(f->f_globals);[37m[39;49;00m$
  1859	[37m					[39;49;00me[37m [39;49;00m=[37m [39;49;00md->ma_lookup(d,[37m [39;49;00mw,[37m [39;49;00mhash);[37m[39;49;00m$
  1860	[37m					[39;49;00m[34mif[39;49;00m[37m [39;49;00m(e[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1861	[37m						[39;49;00mx[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  1862	[37m						[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1863	[37m					[39;49;00m}[37m[39;49;00m$
  1864	[37m					[39;49;00mx[37m [39;49;00m=[37m [39;49;00me->me_value;[37m[39;49;00m$
  1865	[37m					[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1866	[37m						[39;49;00mPy_INCREF(x);[37m[39;49;00m$
  1867	[37m						[39;49;00mPUSH(x);[37m[39;49;00m$
  1868	[37m						[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1869	[37m					[39;49;00m}[37m[39;49;00m$
  1870	[37m					[39;49;00md[37m [39;49;00m=[37m [39;49;00m(PyDictObject[37m [39;49;00m*)(f->f_builtins);[37m[39;49;00m$
  1871	[37m					[39;49;00me[37m [39;49;00m=[37m [39;49;00md->ma_lookup(d,[37m [39;49;00mw,[37m [39;49;00mhash);[37m[39;49;00m$
  1872	[37m					[39;49;00m[34mif[39;49;00m[37m [39;49;00m(e[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1873	[37m						[39;49;00mx[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  1874	[37m						[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1875	[37m					[39;49;00m}[37m[39;49;00m$
  1876	[37m					[39;49;00mx[37m [39;49;00m=[37m [39;49;00me->me_value;[37m[39;49;00m$
  1877	[37m					[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1878	[37m						[39;49;00mPy_INCREF(x);[37m[39;49;00m$
  1879	[37m						[39;49;00mPUSH(x);[37m[39;49;00m$
  1880	[37m						[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1881	[37m					[39;49;00m}[37m[39;49;00m$
  1882	[37m					[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mload_global_error;[37m[39;49;00m$
  1883	[37m				[39;49;00m}[37m[39;49;00m$
  1884	[37m			[39;49;00m}[37m[39;49;00m$
  1885	[37m			[39;49;00m[37m/* This is the un-inlined version of the code above */[39;49;00m[37m[39;49;00m$
  1886	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyDict_GetItem(f->f_globals,[37m [39;49;00mw);[37m[39;49;00m$
  1887	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1888	[37m				[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyDict_GetItem(f->f_builtins,[37m [39;49;00mw);[37m[39;49;00m$
  1889	[37m				[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1890	[37m				  [39;49;00mload_global_error:[37m[39;49;00m$
  1891	[37m					[39;49;00mformat_exc_check_arg([37m[39;49;00m$
  1892	[37m						    [39;49;00mPyExc_NameError,[37m[39;49;00m$
  1893	[37m						    [39;49;00mGLOBAL_NAME_ERROR_MSG,[37m [39;49;00mw);[37m[39;49;00m$
  1894	[37m					[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1895	[37m				[39;49;00m}[37m[39;49;00m$
  1896	[37m			[39;49;00m}[37m[39;49;00m$
  1897	[37m			[39;49;00mPy_INCREF(x);[37m[39;49;00m$
  1898	[37m			[39;49;00mPUSH(x);[37m[39;49;00m$
  1899	[37m			[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1900	[37m[39;49;00m$
  1901	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mDELETE_FAST[39;49;00m:[37m[39;49;00m$
  1902	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mGETLOCAL(oparg);[37m[39;49;00m$
  1903	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1904	[37m				[39;49;00mSETLOCAL(oparg,[37m [39;49;00m[36mNULL[39;49;00m);[37m[39;49;00m$
  1905	[37m				[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1906	[37m			[39;49;00m}[37m[39;49;00m$
  1907	[37m			[39;49;00mformat_exc_check_arg([37m[39;49;00m$
  1908	[37m				[39;49;00mPyExc_UnboundLocalError,[37m[39;49;00m$
  1909	[37m				[39;49;00mUNBOUNDLOCAL_ERROR_MSG,[37m[39;49;00m$
  1910	[37m				[39;49;00mPyTuple_GetItem(co->co_varnames,[37m [39;49;00moparg)[37m[39;49;00m$
  1911	[37m				[39;49;00m);[37m[39;49;00m$
  1912	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1913	[37m[39;49;00m$
  1914	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mLOAD_CLOSURE[39;49;00m:[37m[39;49;00m$
  1915	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mfreevars[oparg];[37m[39;49;00m$
  1916	[37m			[39;49;00mPy_INCREF(x);[37m[39;49;00m$
  1917	[37m			[39;49;00mPUSH(x);[37m[39;49;00m$
  1918	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1919	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1920	[37m[39;49;00m$
  1921	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mLOAD_DEREF[39;49;00m:[37m[39;49;00m$
  1922	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mfreevars[oparg];[37m[39;49;00m$
  1923	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPyCell_Get(x);[37m[39;49;00m$
  1924	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(w[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1925	[37m				[39;49;00mPUSH(w);[37m[39;49;00m$
  1926	[37m				[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1927	[37m			[39;49;00m}[37m[39;49;00m$
  1928	[37m			[39;49;00merr[37m [39;49;00m=[37m [39;49;00m[34m-1[39;49;00m;[37m[39;49;00m$
  1929	[37m			[39;49;00m[37m/* Don't stomp existing exception */[39;49;00m[37m[39;49;00m$
  1930	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyErr_Occurred())[37m[39;49;00m$
  1931	[37m				[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1932	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(oparg[37m [39;49;00m<[37m [39;49;00mPyTuple_GET_SIZE(co->co_cellvars))[37m [39;49;00m{[37m[39;49;00m$
  1933	[37m				[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPyTuple_GET_ITEM(co->co_cellvars,[37m[39;49;00m$
  1934	[37m						       [39;49;00moparg);[37m[39;49;00m$
  1935	[37m			       [39;49;00mformat_exc_check_arg([37m[39;49;00m$
  1936	[37m				       [39;49;00mPyExc_UnboundLocalError,[37m[39;49;00m$
  1937	[37m				       [39;49;00mUNBOUNDLOCAL_ERROR_MSG,[37m[39;49;00m$
  1938	[37m				       [39;49;00mv);[37m[39;49;00m$
  1939	[37m			[39;49;00m}[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
  1940	[37m			       [39;49;00mv[37m [39;49;00m=[37m [39;49;00mPyTuple_GET_ITEM([37m[39;49;00m$
  1941	[37m					      [39;49;00mco->co_freevars,[37m[39;49;00m$
  1942	[37m					      [39;49;00moparg[37m [39;49;00m-[37m [39;49;00mPyTuple_GET_SIZE(co->co_cellvars));[37m[39;49;00m$
  1943	[37m			       [39;49;00mformat_exc_check_arg([37m[39;49;00m$
  1944	[37m				       [39;49;00mPyExc_NameError,[37m[39;49;00m$
  1945	[37m				       [39;49;00mUNBOUNDFREE_ERROR_MSG,[37m[39;49;00m$
  1946	[37m				       [39;49;00mv);[37m[39;49;00m$
  1947	[37m			[39;49;00m}[37m[39;49;00m$
  1948	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1949	[37m[39;49;00m$
  1950	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSTORE_DEREF[39;49;00m:[37m[39;49;00m$
  1951	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1952	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mfreevars[oparg];[37m[39;49;00m$
  1953	[37m			[39;49;00mPyCell_Set(x,[37m [39;49;00mw);[37m[39;49;00m$
  1954	[37m			[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  1955	[37m			[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1956	[37m[39;49;00m$
  1957	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBUILD_TUPLE[39;49;00m:[37m[39;49;00m$
  1958	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyTuple_New(oparg);[37m[39;49;00m$
  1959	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1960	[37m				[39;49;00m[34mfor[39;49;00m[37m [39;49;00m(;[37m [39;49;00m--oparg[37m [39;49;00m>=[37m [39;49;00m[34m0[39;49;00m;)[37m [39;49;00m{[37m[39;49;00m$
  1961	[37m					[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1962	[37m					[39;49;00mPyTuple_SET_ITEM(x,[37m [39;49;00moparg,[37m [39;49;00mw);[37m[39;49;00m$
  1963	[37m				[39;49;00m}[37m[39;49;00m$
  1964	[37m				[39;49;00mPUSH(x);[37m[39;49;00m$
  1965	[37m				[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1966	[37m			[39;49;00m}[37m[39;49;00m$
  1967	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1968	[37m[39;49;00m$
  1969	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBUILD_LIST[39;49;00m:[37m[39;49;00m$
  1970	[37m			[39;49;00mx[37m [39;49;00m=[37m  [39;49;00mPyList_New(oparg);[37m[39;49;00m$
  1971	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  1972	[37m				[39;49;00m[34mfor[39;49;00m[37m [39;49;00m(;[37m [39;49;00m--oparg[37m [39;49;00m>=[37m [39;49;00m[34m0[39;49;00m;)[37m [39;49;00m{[37m[39;49;00m$
  1973	[37m					[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1974	[37m					[39;49;00mPyList_SET_ITEM(x,[37m [39;49;00moparg,[37m [39;49;00mw);[37m[39;49;00m$
  1975	[37m				[39;49;00m}[37m[39;49;00m$
  1976	[37m				[39;49;00mPUSH(x);[37m[39;49;00m$
  1977	[37m				[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1978	[37m			[39;49;00m}[37m[39;49;00m$
  1979	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1980	[37m[39;49;00m$
  1981	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBUILD_MAP[39;49;00m:[37m[39;49;00m$
  1982	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyDict_New();[37m[39;49;00m$
  1983	[37m			[39;49;00mPUSH(x);[37m[39;49;00m$
  1984	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1985	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1986	[37m[39;49;00m$
  1987	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mLOAD_ATTR[39;49;00m:[37m[39;49;00m$
  1988	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mGETITEM(names,[37m [39;49;00moparg);[37m[39;49;00m$
  1989	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1990	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyObject_GetAttr(v,[37m [39;49;00mw);[37m[39;49;00m$
  1991	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  1992	[37m			[39;49;00mSET_TOP(x);[37m[39;49;00m$
  1993	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1994	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1995	[37m[39;49;00m$
  1996	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mCOMPARE_OP[39;49;00m:[37m[39;49;00m$
  1997	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  1998	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  1999	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyInt_CheckExact(w)[37m [39;49;00m&&[37m [39;49;00mPyInt_CheckExact(v))[37m [39;49;00m{[37m[39;49;00m$
  2000	[37m				[39;49;00m[37m/* INLINE: cmp(int, int) */[39;49;00m[37m[39;49;00m$
  2001	[37m				[39;49;00m[34mregister[39;49;00m[37m [39;49;00m[36mlong[39;49;00m[37m [39;49;00ma,[37m [39;49;00mb;[37m[39;49;00m$
  2002	[37m				[39;49;00m[34mregister[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mres;[37m[39;49;00m$
  2003	[37m				[39;49;00ma[37m [39;49;00m=[37m [39;49;00mPyInt_AS_LONG(v);[37m[39;49;00m$
  2004	[37m				[39;49;00mb[37m [39;49;00m=[37m [39;49;00mPyInt_AS_LONG(w);[37m[39;49;00m$
  2005	[37m				[39;49;00m[34mswitch[39;49;00m[37m [39;49;00m(oparg)[37m [39;49;00m{[37m[39;49;00m$
  2006	[37m				[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mPyCmp_LT[39;49;00m:[37m [39;49;00mres[37m [39;49;00m=[37m [39;49;00ma[37m [39;49;00m<[37m  [39;49;00mb;[37m [39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2007	[37m				[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mPyCmp_LE[39;49;00m:[37m [39;49;00mres[37m [39;49;00m=[37m [39;49;00ma[37m [39;49;00m<=[37m [39;49;00mb;[37m [39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2008	[37m				[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mPyCmp_EQ[39;49;00m:[37m [39;49;00mres[37m [39;49;00m=[37m [39;49;00ma[37m [39;49;00m==[37m [39;49;00mb;[37m [39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2009	[37m				[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mPyCmp_NE[39;49;00m:[37m [39;49;00mres[37m [39;49;00m=[37m [39;49;00ma[37m [39;49;00m!=[37m [39;49;00mb;[37m [39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2010	[37m				[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mPyCmp_GT[39;49;00m:[37m [39;49;00mres[37m [39;49;00m=[37m [39;49;00ma[37m [39;49;00m>[37m  [39;49;00mb;[37m [39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2011	[37m				[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mPyCmp_GE[39;49;00m:[37m [39;49;00mres[37m [39;49;00m=[37m [39;49;00ma[37m [39;49;00m>=[37m [39;49;00mb;[37m [39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2012	[37m				[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mPyCmp_IS[39;49;00m:[37m [39;49;00mres[37m [39;49;00m=[37m [39;49;00mv[37m [39;49;00m==[37m [39;49;00mw;[37m [39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2013	[37m				[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mPyCmp_IS_NOT[39;49;00m:[37m [39;49;00mres[37m [39;49;00m=[37m [39;49;00mv[37m [39;49;00m!=[37m [39;49;00mw;[37m [39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2014	[37m				[39;49;00m[34mdefault[39;49;00m:[37m [39;49;00m[34mgoto[39;49;00m[37m [39;49;00mslow_compare;[37m[39;49;00m$
  2015	[37m				[39;49;00m}[37m[39;49;00m$
  2016	[37m				[39;49;00mx[37m [39;49;00m=[37m [39;49;00mres[37m [39;49;00m?[37m [39;49;00mPy_True[37m [39;49;00m:[37m [39;49;00mPy_False;[37m[39;49;00m$
  2017	[37m				[39;49;00mPy_INCREF(x);[37m[39;49;00m$
  2018	[37m			[39;49;00m}[37m[39;49;00m$
  2019	[37m			[39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
  2020	[37m			  [39;49;00mslow_compare:[37m[39;49;00m$
  2021	[37m				[39;49;00mx[37m [39;49;00m=[37m [39;49;00mcmp_outcome(oparg,[37m [39;49;00mv,[37m [39;49;00mw);[37m[39;49;00m$
  2022	[37m			[39;49;00m}[37m[39;49;00m$
  2023	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  2024	[37m			[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  2025	[37m			[39;49;00mSET_TOP(x);[37m[39;49;00m$
  2026	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2027	[37m			[39;49;00mPREDICT(JUMP_IF_FALSE);[37m[39;49;00m$
  2028	[37m			[39;49;00mPREDICT(JUMP_IF_TRUE);[37m[39;49;00m$
  2029	[37m			[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  2030	[37m[39;49;00m$
  2031	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mIMPORT_NAME[39;49;00m:[37m[39;49;00m$
  2032	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mGETITEM(names,[37m [39;49;00moparg);[37m[39;49;00m$
  2033	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyDict_GetItemString(f->f_builtins,[37m [39;49;00m[33m"[39;49;00m[33m__import__[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
  2034	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  2035	[37m				[39;49;00mPyErr_SetString(PyExc_ImportError,[37m[39;49;00m$
  2036	[37m						[39;49;00m[33m"[39;49;00m[33m__import__ not found[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
  2037	[37m				[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2038	[37m			[39;49;00m}[37m[39;49;00m$
  2039	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  2040	[37m			[39;49;00mu[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  2041	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyInt_AsLong(u)[37m [39;49;00m!=[37m [39;49;00m[34m-1[39;49;00m[37m [39;49;00m||[37m [39;49;00mPyErr_Occurred())[37m[39;49;00m$
  2042	[37m				[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPyTuple_Pack([34m5[39;49;00m,[37m[39;49;00m$
  2043	[37m					    [39;49;00mw,[37m[39;49;00m$
  2044	[37m					    [39;49;00mf->f_globals,[37m[39;49;00m$
  2045	[37m					    [39;49;00mf->f_locals[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m[37m [39;49;00m?[37m[39;49;00m$
  2046	[37m						  [39;49;00mPy_None[37m [39;49;00m:[37m [39;49;00mf->f_locals,[37m[39;49;00m$
  2047	[37m					    [39;49;00mv,[37m[39;49;00m$
  2048	[37m					    [39;49;00mu);[37m[39;49;00m$
  2049	[37m			[39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  2050	[37m				[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPyTuple_Pack([34m4[39;49;00m,[37m[39;49;00m$
  2051	[37m					    [39;49;00mw,[37m[39;49;00m$
  2052	[37m					    [39;49;00mf->f_globals,[37m[39;49;00m$
  2053	[37m					    [39;49;00mf->f_locals[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m[37m [39;49;00m?[37m[39;49;00m$
  2054	[37m						  [39;49;00mPy_None[37m [39;49;00m:[37m [39;49;00mf->f_locals,[37m[39;49;00m$
  2055	[37m					    [39;49;00mv);[37m[39;49;00m$
  2056	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  2057	[37m			[39;49;00mPy_DECREF(u);[37m[39;49;00m$
  2058	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(w[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  2059	[37m				[39;49;00mu[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  2060	[37m				[39;49;00mx[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  2061	[37m				[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2062	[37m			[39;49;00m}[37m[39;49;00m$
  2063	[37m			[39;49;00mREAD_TIMESTAMP(intr0);[37m[39;49;00m$
  2064	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyEval_CallObject(x,[37m [39;49;00mw);[37m[39;49;00m$
  2065	[37m			[39;49;00mREAD_TIMESTAMP(intr1);[37m[39;49;00m$
  2066	[37m			[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  2067	[37m			[39;49;00mSET_TOP(x);[37m[39;49;00m$
  2068	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  2069	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2070	[37m[39;49;00m$
  2071	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mIMPORT_STAR[39;49;00m:[37m[39;49;00m$
  2072	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  2073	[37m			[39;49;00mPyFrame_FastToLocals(f);[37m[39;49;00m$
  2074	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m((x[37m [39;49;00m=[37m [39;49;00mf->f_locals)[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  2075	[37m				[39;49;00mPyErr_SetString(PyExc_SystemError,[37m[39;49;00m$
  2076	[37m					[39;49;00m[33m"[39;49;00m[33mno locals found during 'import *'[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
  2077	[37m				[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2078	[37m			[39;49;00m}[37m[39;49;00m$
  2079	[37m			[39;49;00mREAD_TIMESTAMP(intr0);[37m[39;49;00m$
  2080	[37m			[39;49;00merr[37m [39;49;00m=[37m [39;49;00mimport_all_from(x,[37m [39;49;00mv);[37m[39;49;00m$
  2081	[37m			[39;49;00mREAD_TIMESTAMP(intr1);[37m[39;49;00m$
  2082	[37m			[39;49;00mPyFrame_LocalsToFast(f,[37m [39;49;00m[34m0[39;49;00m);[37m[39;49;00m$
  2083	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  2084	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  2085	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2086	[37m[39;49;00m$
  2087	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mIMPORT_FROM[39;49;00m:[37m[39;49;00m$
  2088	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mGETITEM(names,[37m [39;49;00moparg);[37m[39;49;00m$
  2089	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  2090	[37m			[39;49;00mREAD_TIMESTAMP(intr0);[37m[39;49;00m$
  2091	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mimport_from(v,[37m [39;49;00mw);[37m[39;49;00m$
  2092	[37m			[39;49;00mREAD_TIMESTAMP(intr1);[37m[39;49;00m$
  2093	[37m			[39;49;00mPUSH(x);[37m[39;49;00m$
  2094	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  2095	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2096	[37m[39;49;00m$
  2097	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mJUMP_FORWARD[39;49;00m:[37m[39;49;00m$
  2098	[37m			[39;49;00mJUMPBY(oparg);[37m[39;49;00m$
  2099	[37m			[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
  2100	[37m[39;49;00m$
  2101	[37m		[39;49;00mPREDICTED_WITH_ARG(JUMP_IF_FALSE);[37m[39;49;00m$
  2102	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mJUMP_IF_FALSE[39;49;00m:[37m[39;49;00m$
  2103	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  2104	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(w[37m [39;49;00m==[37m [39;49;00mPy_True)[37m [39;49;00m{[37m[39;49;00m$
  2105	[37m				[39;49;00mPREDICT(POP_TOP);[37m[39;49;00m$
  2106	[37m				[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
  2107	[37m			[39;49;00m}[37m[39;49;00m$
  2108	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(w[37m [39;49;00m==[37m [39;49;00mPy_False)[37m [39;49;00m{[37m[39;49;00m$
  2109	[37m				[39;49;00mJUMPBY(oparg);[37m[39;49;00m$
  2110	[37m				[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
  2111	[37m			[39;49;00m}[37m[39;49;00m$
  2112	[37m			[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyObject_IsTrue(w);[37m[39;49;00m$
  2113	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m>[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  2114	[37m				[39;49;00merr[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
  2115	[37m			[39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  2116	[37m				[39;49;00mJUMPBY(oparg);[37m[39;49;00m$
  2117	[37m			[39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  2118	[37m				[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2119	[37m			[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  2120	[37m[39;49;00m$
  2121	[37m		[39;49;00mPREDICTED_WITH_ARG(JUMP_IF_TRUE);[37m[39;49;00m$
  2122	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mJUMP_IF_TRUE[39;49;00m:[37m[39;49;00m$
  2123	[37m			[39;49;00mw[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  2124	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(w[37m [39;49;00m==[37m [39;49;00mPy_False)[37m [39;49;00m{[37m[39;49;00m$
  2125	[37m				[39;49;00mPREDICT(POP_TOP);[37m[39;49;00m$
  2126	[37m				[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
  2127	[37m			[39;49;00m}[37m[39;49;00m$
  2128	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(w[37m [39;49;00m==[37m [39;49;00mPy_True)[37m [39;49;00m{[37m[39;49;00m$
  2129	[37m				[39;49;00mJUMPBY(oparg);[37m[39;49;00m$
  2130	[37m				[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_next_opcode;[37m[39;49;00m$
  2131	[37m			[39;49;00m}[37m[39;49;00m$
  2132	[37m			[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyObject_IsTrue(w);[37m[39;49;00m$
  2133	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m>[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  2134	[37m				[39;49;00merr[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
  2135	[37m				[39;49;00mJUMPBY(oparg);[37m[39;49;00m$
  2136	[37m			[39;49;00m}[37m[39;49;00m$
  2137	[37m			[39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  2138	[37m				[39;49;00m;[37m[39;49;00m$
  2139	[37m			[39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  2140	[37m				[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2141	[37m			[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  2142	[37m[39;49;00m$
  2143	[37m		[39;49;00mPREDICTED_WITH_ARG(JUMP_ABSOLUTE);[37m[39;49;00m$
  2144	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mJUMP_ABSOLUTE[39;49;00m:[37m[39;49;00m$
  2145	[37m			[39;49;00mJUMPTO(oparg);[37m[39;49;00m$
  2146	[37m			[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  2147	[37m[39;49;00m$
  2148	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mGET_ITER[39;49;00m:[37m[39;49;00m$
  2149	[37m			[39;49;00m[37m/* before: [obj]; after [getiter(obj)] */[39;49;00m[37m[39;49;00m$
  2150	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  2151	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyObject_GetIter(v);[37m[39;49;00m$
  2152	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  2153	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  2154	[37m				[39;49;00mSET_TOP(x);[37m[39;49;00m$
  2155	[37m				[39;49;00mPREDICT(FOR_ITER);[37m[39;49;00m$
  2156	[37m				[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  2157	[37m			[39;49;00m}[37m[39;49;00m$
  2158	[37m			[39;49;00mSTACKADJ([34m-1[39;49;00m);[37m[39;49;00m$
  2159	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2160	[37m[39;49;00m$
  2161	[37m		[39;49;00mPREDICTED_WITH_ARG(FOR_ITER);[37m[39;49;00m$
  2162	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mFOR_ITER[39;49;00m:[37m[39;49;00m$
  2163	[37m			[39;49;00m[37m/* before: [iter]; after: [iter, iter()] *or* [] */[39;49;00m[37m[39;49;00m$
  2164	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  2165	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00m(*v->ob_type->tp_iternext)(v);[37m[39;49;00m$
  2166	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  2167	[37m				[39;49;00mPUSH(x);[37m[39;49;00m$
  2168	[37m				[39;49;00mPREDICT(STORE_FAST);[37m[39;49;00m$
  2169	[37m				[39;49;00mPREDICT(UNPACK_SEQUENCE);[37m[39;49;00m$
  2170	[37m				[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  2171	[37m			[39;49;00m}[37m[39;49;00m$
  2172	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyErr_Occurred())[37m [39;49;00m{[37m[39;49;00m$
  2173	[37m				[39;49;00m[34mif[39;49;00m[37m [39;49;00m(!PyErr_ExceptionMatches(PyExc_StopIteration))[37m[39;49;00m$
  2174	[37m					[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2175	[37m				[39;49;00mPyErr_Clear();[37m[39;49;00m$
  2176	[37m			[39;49;00m}[37m[39;49;00m$
  2177	[37m			[39;49;00m[37m/* iterator ended normally */[39;49;00m[37m[39;49;00m$
  2178	[37m 			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  2179	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  2180	[37m			[39;49;00mJUMPBY(oparg);[37m[39;49;00m$
  2181	[37m			[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  2182	[37m[39;49;00m$
  2183	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBREAK_LOOP[39;49;00m:[37m[39;49;00m$
  2184	[37m			[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_BREAK;[37m[39;49;00m$
  2185	[37m			[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_block_end;[37m[39;49;00m$
  2186	[37m[39;49;00m$
  2187	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mCONTINUE_LOOP[39;49;00m:[37m[39;49;00m$
  2188	[37m			[39;49;00mretval[37m [39;49;00m=[37m [39;49;00mPyInt_FromLong(oparg);[37m[39;49;00m$
  2189	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(!retval)[37m [39;49;00m{[37m[39;49;00m$
  2190	[37m				[39;49;00mx[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  2191	[37m				[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2192	[37m			[39;49;00m}[37m[39;49;00m$
  2193	[37m			[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_CONTINUE;[37m[39;49;00m$
  2194	[37m			[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mfast_block_end;[37m[39;49;00m$
  2195	[37m[39;49;00m$
  2196	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSETUP_LOOP[39;49;00m:[37m[39;49;00m$
  2197	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSETUP_EXCEPT[39;49;00m:[37m[39;49;00m$
  2198	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mSETUP_FINALLY[39;49;00m:[37m[39;49;00m$
  2199	[37m			[39;49;00m[37m/* NOTE: If you add any new block-setup opcodes that are not try/except/finally[39;49;00m$
  2200	[37m			   handlers, you may need to update the PyGen_NeedsFinalizing() function. */[39;49;00m[37m[39;49;00m$
  2201	[37m[39;49;00m$
  2202	[37m			[39;49;00mPyFrame_BlockSetup(f,[37m [39;49;00mopcode,[37m [39;49;00mINSTR_OFFSET()[37m [39;49;00m+[37m [39;49;00moparg,[37m[39;49;00m$
  2203	[37m					   [39;49;00mSTACK_LEVEL());[37m[39;49;00m$
  2204	[37m			[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  2205	[37m[39;49;00m$
  2206	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mWITH_CLEANUP[39;49;00m:[37m[39;49;00m$
  2207	[37m		[39;49;00m{[37m[39;49;00m$
  2208	[37m			[39;49;00m[37m/* TOP is the context.__exit__ bound method.[39;49;00m$
  2209	[37m			   Below that are 1-3 values indicating how/why[39;49;00m$
  2210	[37m			   we entered the finally clause:[39;49;00m$
  2211	[37m			   - SECOND = None[39;49;00m$
  2212	[37m			   - (SECOND, THIRD) = (WHY_{RETURN,CONTINUE}), retval[39;49;00m$
  2213	[37m			   - SECOND = WHY_*; no retval below it[39;49;00m$
  2214	[37m			   - (SECOND, THIRD, FOURTH) = exc_info()[39;49;00m$
  2215	[37m			   In the last case, we must call[39;49;00m$
  2216	[37m			     TOP(SECOND, THIRD, FOURTH)[39;49;00m$
  2217	[37m			   otherwise we must call[39;49;00m$
  2218	[37m			     TOP(None, None, None)[39;49;00m$
  2219	[37m[39;49;00m$
  2220	[37m			   In addition, if the stack represents an exception,[39;49;00m$
  2221	[37m			   *and* the function call returns a 'true' value, we[39;49;00m$
  2222	[37m			   "zap" this information, to prevent END_FINALLY from[39;49;00m$
  2223	[37m			   re-raising the exception.  (But non-local gotos[39;49;00m$
  2224	[37m			   should still be resumed.)[39;49;00m$
  2225	[37m			*/[39;49;00m[37m[39;49;00m$
  2226	[37m[39;49;00m$
  2227	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  2228	[37m			[39;49;00mu[37m [39;49;00m=[37m [39;49;00mSECOND();[37m[39;49;00m$
  2229	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyInt_Check(u)[37m [39;49;00m||[37m [39;49;00mu[37m [39;49;00m==[37m [39;49;00mPy_None)[37m [39;49;00m{[37m[39;49;00m$
  2230	[37m				[39;49;00mu[37m [39;49;00m=[37m [39;49;00mv[37m [39;49;00m=[37m [39;49;00mw[37m [39;49;00m=[37m [39;49;00mPy_None;[37m[39;49;00m$
  2231	[37m			[39;49;00m}[37m[39;49;00m$
  2232	[37m			[39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
  2233	[37m				[39;49;00mv[37m [39;49;00m=[37m [39;49;00mTHIRD();[37m[39;49;00m$
  2234	[37m				[39;49;00mw[37m [39;49;00m=[37m [39;49;00mFOURTH();[37m[39;49;00m$
  2235	[37m			[39;49;00m}[37m[39;49;00m$
  2236	[37m			[39;49;00m[37m/* XXX Not the fastest way to call it... */[39;49;00m[37m[39;49;00m$
  2237	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyObject_CallFunctionObjArgs(x,[37m [39;49;00mu,[37m [39;49;00mv,[37m [39;49;00mw,[37m [39;49;00m[36mNULL[39;49;00m);[37m[39;49;00m$
  2238	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
  2239	[37m				[39;49;00m[34mbreak[39;49;00m;[37m [39;49;00m[37m/* Go to error exit */[39;49;00m[37m[39;49;00m$
  2240	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(u[37m [39;49;00m!=[37m [39;49;00mPy_None[37m [39;49;00m&&[37m [39;49;00mPyObject_IsTrue(x))[37m [39;49;00m{[37m[39;49;00m$
  2241	[37m				[39;49;00m[37m/* There was an exception and a true return */[39;49;00m[37m[39;49;00m$
  2242	[37m				[39;49;00mPy_DECREF(x);[37m[39;49;00m$
  2243	[37m				[39;49;00mx[37m [39;49;00m=[37m [39;49;00mTOP();[37m [39;49;00m[37m/* Again */[39;49;00m[37m[39;49;00m$
  2244	[37m				[39;49;00mSTACKADJ([34m-3[39;49;00m);[37m[39;49;00m$
  2245	[37m				[39;49;00mPy_INCREF(Py_None);[37m[39;49;00m$
  2246	[37m				[39;49;00mSET_TOP(Py_None);[37m[39;49;00m$
  2247	[37m				[39;49;00mPy_DECREF(x);[37m[39;49;00m$
  2248	[37m				[39;49;00mPy_DECREF(u);[37m[39;49;00m$
  2249	[37m				[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  2250	[37m				[39;49;00mPy_DECREF(w);[37m[39;49;00m$
  2251	[37m			[39;49;00m}[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
  2252	[37m				[39;49;00m[37m/* Let END_FINALLY do its thing */[39;49;00m[37m[39;49;00m$
  2253	[37m				[39;49;00mPy_DECREF(x);[37m[39;49;00m$
  2254	[37m				[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  2255	[37m				[39;49;00mPy_DECREF(x);[37m[39;49;00m$
  2256	[37m			[39;49;00m}[37m[39;49;00m$
  2257	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2258	[37m		[39;49;00m}[37m[39;49;00m$
  2259	[37m[39;49;00m$
  2260	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mCALL_FUNCTION[39;49;00m:[37m[39;49;00m$
  2261	[37m		[39;49;00m{[37m[39;49;00m$
  2262	[37m			[39;49;00mPyObject[37m [39;49;00m**sp;[37m[39;49;00m$
  2263	[37m			[39;49;00mPCALL(PCALL_ALL);[37m[39;49;00m$
  2264	[37m			[39;49;00msp[37m [39;49;00m=[37m [39;49;00mstack_pointer;[37m[39;49;00m$
  2265	[36m#[39;49;00m[36mifdef WITH_TSC[39;49;00m[36m[39;49;00m$
  2266	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mcall_function(&sp,[37m [39;49;00moparg,[37m [39;49;00m&intr0,[37m [39;49;00m&intr1);[37m[39;49;00m$
  2267	[36m#[39;49;00m[36melse[39;49;00m[36m[39;49;00m$
  2268	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mcall_function(&sp,[37m [39;49;00moparg);[37m[39;49;00m$
  2269	[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
  2270	[37m			[39;49;00mstack_pointer[37m [39;49;00m=[37m [39;49;00msp;[37m[39;49;00m$
  2271	[37m			[39;49;00mPUSH(x);[37m[39;49;00m$
  2272	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
  2273	[37m				[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  2274	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2275	[37m		[39;49;00m}[37m[39;49;00m$
  2276	[37m[39;49;00m$
  2277	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mCALL_FUNCTION_VAR[39;49;00m:[37m[39;49;00m$
  2278	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mCALL_FUNCTION_KW[39;49;00m:[37m[39;49;00m$
  2279	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mCALL_FUNCTION_VAR_KW[39;49;00m:[37m[39;49;00m$
  2280	[37m		[39;49;00m{[37m[39;49;00m$
  2281	[37m		    [39;49;00m[36mint[39;49;00m[37m [39;49;00mna[37m [39;49;00m=[37m [39;49;00moparg[37m [39;49;00m&[37m [39;49;00m[34m0xff[39;49;00m;[37m[39;49;00m$
  2282	[37m		    [39;49;00m[36mint[39;49;00m[37m [39;49;00mnk[37m [39;49;00m=[37m [39;49;00m(oparg>>[34m8[39;49;00m)[37m [39;49;00m&[37m [39;49;00m[34m0xff[39;49;00m;[37m[39;49;00m$
  2283	[37m		    [39;49;00m[36mint[39;49;00m[37m [39;49;00mflags[37m [39;49;00m=[37m [39;49;00m(opcode[37m [39;49;00m-[37m [39;49;00mCALL_FUNCTION)[37m [39;49;00m&[37m [39;49;00m[34m3[39;49;00m;[37m[39;49;00m$
  2284	[37m		    [39;49;00m[36mint[39;49;00m[37m [39;49;00mn[37m [39;49;00m=[37m [39;49;00mna[37m [39;49;00m+[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m*[37m [39;49;00mnk;[37m[39;49;00m$
  2285	[37m		    [39;49;00mPyObject[37m [39;49;00m**pfunc,[37m [39;49;00m*func,[37m [39;49;00m**sp;[37m[39;49;00m$
  2286	[37m		    [39;49;00mPCALL(PCALL_ALL);[37m[39;49;00m$
  2287	[37m		    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(flags[37m [39;49;00m&[37m [39;49;00mCALL_FLAG_VAR)[37m[39;49;00m$
  2288	[37m			    [39;49;00mn++;[37m[39;49;00m$
  2289	[37m		    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(flags[37m [39;49;00m&[37m [39;49;00mCALL_FLAG_KW)[37m[39;49;00m$
  2290	[37m			    [39;49;00mn++;[37m[39;49;00m$
  2291	[37m		    [39;49;00mpfunc[37m [39;49;00m=[37m [39;49;00mstack_pointer[37m [39;49;00m-[37m [39;49;00mn[37m [39;49;00m-[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
  2292	[37m		    [39;49;00mfunc[37m [39;49;00m=[37m [39;49;00m*pfunc;[37m[39;49;00m$
  2293	[37m[39;49;00m$
  2294	[37m		    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyMethod_Check(func)[37m[39;49;00m$
  2295	[37m			[39;49;00m&&[37m [39;49;00mPyMethod_GET_SELF(func)[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  2296	[37m			    [39;49;00mPyObject[37m [39;49;00m*self[37m [39;49;00m=[37m [39;49;00mPyMethod_GET_SELF(func);[37m[39;49;00m$
  2297	[37m			    [39;49;00mPy_INCREF(self);[37m[39;49;00m$
  2298	[37m			    [39;49;00mfunc[37m [39;49;00m=[37m [39;49;00mPyMethod_GET_FUNCTION(func);[37m[39;49;00m$
  2299	[37m			    [39;49;00mPy_INCREF(func);[37m[39;49;00m$
  2300	[37m			    [39;49;00mPy_DECREF(*pfunc);[37m[39;49;00m$
  2301	[37m			    [39;49;00m*pfunc[37m [39;49;00m=[37m [39;49;00mself;[37m[39;49;00m$
  2302	[37m			    [39;49;00mna++;[37m[39;49;00m$
  2303	[37m			    [39;49;00mn++;[37m[39;49;00m$
  2304	[37m		    [39;49;00m}[37m [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  2305	[37m			    [39;49;00mPy_INCREF(func);[37m[39;49;00m$
  2306	[37m		    [39;49;00msp[37m [39;49;00m=[37m [39;49;00mstack_pointer;[37m[39;49;00m$
  2307	[37m		    [39;49;00mREAD_TIMESTAMP(intr0);[37m[39;49;00m$
  2308	[37m		    [39;49;00mx[37m [39;49;00m=[37m [39;49;00mext_do_call(func,[37m [39;49;00m&sp,[37m [39;49;00mflags,[37m [39;49;00mna,[37m [39;49;00mnk);[37m[39;49;00m$
  2309	[37m		    [39;49;00mREAD_TIMESTAMP(intr1);[37m[39;49;00m$
  2310	[37m		    [39;49;00mstack_pointer[37m [39;49;00m=[37m [39;49;00msp;[37m[39;49;00m$
  2311	[37m		    [39;49;00mPy_DECREF(func);[37m[39;49;00m$
  2312	[37m[39;49;00m$
  2313	[37m		    [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(stack_pointer[37m [39;49;00m>[37m [39;49;00mpfunc)[37m [39;49;00m{[37m[39;49;00m$
  2314	[37m			    [39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  2315	[37m			    [39;49;00mPy_DECREF(w);[37m[39;49;00m$
  2316	[37m		    [39;49;00m}[37m[39;49;00m$
  2317	[37m		    [39;49;00mPUSH(x);[37m[39;49;00m$
  2318	[37m		    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
  2319	[37m			    [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  2320	[37m		    [39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2321	[37m		[39;49;00m}[37m[39;49;00m$
  2322	[37m[39;49;00m$
  2323	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mMAKE_FUNCTION[39;49;00m:[37m[39;49;00m$
  2324	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m [39;49;00m[37m/* code object */[39;49;00m[37m[39;49;00m$
  2325	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyFunction_New(v,[37m [39;49;00mf->f_globals);[37m[39;49;00m$
  2326	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  2327	[37m			[39;49;00m[37m/* XXX Maybe this should be a separate opcode? */[39;49;00m[37m[39;49;00m$
  2328	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m[37m [39;49;00m&&[37m [39;49;00moparg[37m [39;49;00m>[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  2329	[37m				[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPyTuple_New(oparg);[37m[39;49;00m$
  2330	[37m				[39;49;00m[34mif[39;49;00m[37m [39;49;00m(v[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  2331	[37m					[39;49;00mPy_DECREF(x);[37m[39;49;00m$
  2332	[37m					[39;49;00mx[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  2333	[37m					[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2334	[37m				[39;49;00m}[37m[39;49;00m$
  2335	[37m				[39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(--oparg[37m [39;49;00m>=[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  2336	[37m					[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  2337	[37m					[39;49;00mPyTuple_SET_ITEM(v,[37m [39;49;00moparg,[37m [39;49;00mw);[37m[39;49;00m$
  2338	[37m				[39;49;00m}[37m[39;49;00m$
  2339	[37m				[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyFunction_SetDefaults(x,[37m [39;49;00mv);[37m[39;49;00m$
  2340	[37m				[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  2341	[37m			[39;49;00m}[37m[39;49;00m$
  2342	[37m			[39;49;00mPUSH(x);[37m[39;49;00m$
  2343	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2344	[37m[39;49;00m$
  2345	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mMAKE_CLOSURE[39;49;00m:[37m[39;49;00m$
  2346	[37m		[39;49;00m{[37m[39;49;00m$
  2347	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m [39;49;00m[37m/* code object */[39;49;00m[37m[39;49;00m$
  2348	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPyFunction_New(v,[37m [39;49;00mf->f_globals);[37m[39;49;00m$
  2349	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  2350	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  2351	[37m				[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  2352	[37m				[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyFunction_SetClosure(x,[37m [39;49;00mv);[37m[39;49;00m$
  2353	[37m				[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  2354	[37m			[39;49;00m}[37m[39;49;00m$
  2355	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m[37m [39;49;00m&&[37m [39;49;00moparg[37m [39;49;00m>[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  2356	[37m				[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPyTuple_New(oparg);[37m[39;49;00m$
  2357	[37m				[39;49;00m[34mif[39;49;00m[37m [39;49;00m(v[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  2358	[37m					[39;49;00mPy_DECREF(x);[37m[39;49;00m$
  2359	[37m					[39;49;00mx[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  2360	[37m					[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2361	[37m				[39;49;00m}[37m[39;49;00m$
  2362	[37m				[39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(--oparg[37m [39;49;00m>=[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  2363	[37m					[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  2364	[37m					[39;49;00mPyTuple_SET_ITEM(v,[37m [39;49;00moparg,[37m [39;49;00mw);[37m[39;49;00m$
  2365	[37m				[39;49;00m}[37m[39;49;00m$
  2366	[37m				[39;49;00merr[37m [39;49;00m=[37m [39;49;00mPyFunction_SetDefaults(x,[37m [39;49;00mv);[37m[39;49;00m$
  2367	[37m				[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  2368	[37m			[39;49;00m}[37m[39;49;00m$
  2369	[37m			[39;49;00mPUSH(x);[37m[39;49;00m$
  2370	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2371	[37m		[39;49;00m}[37m[39;49;00m$
  2372	[37m[39;49;00m$
  2373	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mBUILD_SLICE[39;49;00m:[37m[39;49;00m$
  2374	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(oparg[37m [39;49;00m==[37m [39;49;00m[34m3[39;49;00m)[37m[39;49;00m$
  2375	[37m				[39;49;00mw[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  2376	[37m			[39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  2377	[37m				[39;49;00mw[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  2378	[37m			[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  2379	[37m			[39;49;00mu[37m [39;49;00m=[37m [39;49;00mTOP();[37m[39;49;00m$
  2380	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPySlice_New(u,[37m [39;49;00mv,[37m [39;49;00mw);[37m[39;49;00m$
  2381	[37m			[39;49;00mPy_DECREF(u);[37m[39;49;00m$
  2382	[37m			[39;49;00mPy_DECREF(v);[37m[39;49;00m$
  2383	[37m			[39;49;00mPy_XDECREF(w);[37m[39;49;00m$
  2384	[37m			[39;49;00mSET_TOP(x);[37m[39;49;00m$
  2385	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(x[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  2386	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2387	[37m[39;49;00m$
  2388	[37m		[39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31mEXTENDED_ARG[39;49;00m:[37m[39;49;00m$
  2389	[37m			[39;49;00mopcode[37m [39;49;00m=[37m [39;49;00mNEXTOP();[37m[39;49;00m$
  2390	[37m			[39;49;00moparg[37m [39;49;00m=[37m [39;49;00moparg<<[34m16[39;49;00m[37m [39;49;00m|[37m [39;49;00mNEXTARG();[37m[39;49;00m$
  2391	[37m			[39;49;00m[34mgoto[39;49;00m[37m [39;49;00mdispatch_opcode;[37m[39;49;00m$
  2392	[37m[39;49;00m$
  2393	[37m		[39;49;00m[34mdefault[39;49;00m:[37m[39;49;00m$
  2394	[37m			[39;49;00mfprintf(stderr,[37m[39;49;00m$
  2395	[37m				[39;49;00m[33m"[39;49;00m[33mXXX lineno: %d, opcode: %d[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m,[37m[39;49;00m$
  2396	[37m				[39;49;00mPyCode_Addr2Line(f->f_code,[37m [39;49;00mf->f_lasti),[37m[39;49;00m$
  2397	[37m				[39;49;00mopcode);[37m[39;49;00m$
  2398	[37m			[39;49;00mPyErr_SetString(PyExc_SystemError,[37m [39;49;00m[33m"[39;49;00m[33munknown opcode[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
  2399	[37m			[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_EXCEPTION;[37m[39;49;00m$
  2400	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2401	[37m[39;49;00m$
  2402	[36m#[39;49;00m[36mifdef CASE_TOO_BIG[39;49;00m[36m[39;49;00m$
  2403	[37m		[39;49;00m}[37m[39;49;00m$
  2404	[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
  2405	[37m[39;49;00m$
  2406	[37m		[39;49;00m}[37m [39;49;00m[37m/* switch */[39;49;00m[37m[39;49;00m$
  2407	[37m[39;49;00m$
  2408	[37m	    [39;49;00mon_error:[37m[39;49;00m$
  2409	[37m[39;49;00m$
  2410	[37m		[39;49;00mREAD_TIMESTAMP(inst1);[37m[39;49;00m$
  2411	[37m[39;49;00m$
  2412	[37m		[39;49;00m[37m/* Quickly continue if no error occurred */[39;49;00m[37m[39;49;00m$
  2413	[37m[39;49;00m$
  2414	[37m		[39;49;00m[34mif[39;49;00m[37m [39;49;00m(why[37m [39;49;00m==[37m [39;49;00mWHY_NOT)[37m [39;49;00m{[37m[39;49;00m$
  2415	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(err[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m&&[37m [39;49;00mx[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  2416	[36m#[39;49;00m[36mifdef CHECKEXC[39;49;00m[36m[39;49;00m$
  2417	[37m				[39;49;00m[37m/* This check is expensive! */[39;49;00m[37m[39;49;00m$
  2418	[37m				[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyErr_Occurred())[37m[39;49;00m$
  2419	[37m					[39;49;00mfprintf(stderr,[37m[39;49;00m$
  2420	[37m						[39;49;00m[33m"[39;49;00m[33mXXX undetected error[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
  2421	[37m				[39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
  2422	[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
  2423	[37m					[39;49;00mREAD_TIMESTAMP(loop1);[37m[39;49;00m$
  2424	[37m					[39;49;00m[34mcontinue[39;49;00m;[37m [39;49;00m[37m/* Normal, fast path */[39;49;00m[37m[39;49;00m$
  2425	[36m#[39;49;00m[36mifdef CHECKEXC[39;49;00m[36m[39;49;00m$
  2426	[37m				[39;49;00m}[37m[39;49;00m$
  2427	[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
  2428	[37m			[39;49;00m}[37m[39;49;00m$
  2429	[37m			[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_EXCEPTION;[37m[39;49;00m$
  2430	[37m			[39;49;00mx[37m [39;49;00m=[37m [39;49;00mPy_None;[37m[39;49;00m$
  2431	[37m			[39;49;00merr[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
  2432	[37m		[39;49;00m}[37m[39;49;00m$
  2433	[37m[39;49;00m$
  2434	[37m		[39;49;00m[37m/* Double-check exception status */[39;49;00m[37m[39;49;00m$
  2435	[37m[39;49;00m$
  2436	[37m		[39;49;00m[34mif[39;49;00m[37m [39;49;00m(why[37m [39;49;00m==[37m [39;49;00mWHY_EXCEPTION[37m [39;49;00m||[37m [39;49;00mwhy[37m [39;49;00m==[37m [39;49;00mWHY_RERAISE)[37m [39;49;00m{[37m[39;49;00m$
  2437	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(!PyErr_Occurred())[37m [39;49;00m{[37m[39;49;00m$
  2438	[37m				[39;49;00mPyErr_SetString(PyExc_SystemError,[37m[39;49;00m$
  2439	[37m					[39;49;00m[33m"[39;49;00m[33merror return without exception set[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
  2440	[37m				[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_EXCEPTION;[37m[39;49;00m$
  2441	[37m			[39;49;00m}[37m[39;49;00m$
  2442	[37m		[39;49;00m}[37m[39;49;00m$
  2443	[36m#[39;49;00m[36mifdef CHECKEXC[39;49;00m[36m[39;49;00m$
  2444	[37m		[39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
  2445	[37m			[39;49;00m[37m/* This check is expensive! */[39;49;00m[37m[39;49;00m$
  2446	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(PyErr_Occurred())[37m [39;49;00m{[37m[39;49;00m$
  2447	[37m				[39;49;00m[36mchar[39;49;00m[37m [39;49;00mbuf[[34m1024[39;49;00m];[37m[39;49;00m$
  2448	[37m				[39;49;00msprintf(buf,[37m [39;49;00m[33m"[39;49;00m[33mStack unwind with exception [39;49;00m[33m"[39;49;00m[37m[39;49;00m$
  2449	[37m					[39;49;00m[33m"[39;49;00m[33mset and why=%d[39;49;00m[33m"[39;49;00m,[37m [39;49;00mwhy);[37m[39;49;00m$
  2450	[37m				[39;49;00mPy_FatalError(buf);[37m[39;49;00m$
  2451	[37m			[39;49;00m}[37m[39;49;00m$
  2452	[37m		[39;49;00m}[37m[39;49;00m$
  2453	[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
  2454	[37m[39;49;00m$
  2455	[37m		[39;49;00m[37m/* Log traceback info if this is a real exception */[39;49;00m[37m[39;49;00m$
  2456	[37m[39;49;00m$
  2457	[37m		[39;49;00m[34mif[39;49;00m[37m [39;49;00m(why[37m [39;49;00m==[37m [39;49;00mWHY_EXCEPTION)[37m [39;49;00m{[37m[39;49;00m$
  2458	[37m			[39;49;00mPyTraceBack_Here(f);[37m[39;49;00m$
  2459	[37m[39;49;00m$
  2460	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(tstate->c_tracefunc[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
  2461	[37m				[39;49;00mcall_exc_trace(tstate->c_tracefunc,[37m[39;49;00m$
  2462	[37m					       [39;49;00mtstate->c_traceobj,[37m [39;49;00mf);[37m[39;49;00m$
  2463	[37m		[39;49;00m}[37m[39;49;00m$
  2464	[37m[39;49;00m$
  2465	[37m		[39;49;00m[37m/* For the rest, treat WHY_RERAISE as WHY_EXCEPTION */[39;49;00m[37m[39;49;00m$
  2466	[37m[39;49;00m$
  2467	[37m		[39;49;00m[34mif[39;49;00m[37m [39;49;00m(why[37m [39;49;00m==[37m [39;49;00mWHY_RERAISE)[37m[39;49;00m$
  2468	[37m			[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_EXCEPTION;[37m[39;49;00m$
  2469	[37m[39;49;00m$
  2470	[37m		[39;49;00m[37m/* Unwind stacks if a (pseudo) exception occurred */[39;49;00m[37m[39;49;00m$
  2471	[37m[39;49;00m$
  2472	fast_block_end:[37m[39;49;00m$
  2473	[37m		[39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(why[37m [39;49;00m!=[37m [39;49;00mWHY_NOT[37m [39;49;00m&&[37m [39;49;00mf->f_iblock[37m [39;49;00m>[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  2474	[37m			[39;49;00mPyTryBlock[37m [39;49;00m*b[37m [39;49;00m=[37m [39;49;00mPyFrame_BlockPop(f);[37m[39;49;00m$
  2475	[37m[39;49;00m$
  2476	[37m			[39;49;00massert(why[37m [39;49;00m!=[37m [39;49;00mWHY_YIELD);[37m[39;49;00m$
  2477	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(b->b_type[37m [39;49;00m==[37m [39;49;00mSETUP_LOOP[37m [39;49;00m&&[37m [39;49;00mwhy[37m [39;49;00m==[37m [39;49;00mWHY_CONTINUE)[37m [39;49;00m{[37m[39;49;00m$
  2478	[37m				[39;49;00m[37m/* For a continue inside a try block,[39;49;00m$
  2479	[37m				   don't pop the block for the loop. */[39;49;00m[37m[39;49;00m$
  2480	[37m				[39;49;00mPyFrame_BlockSetup(f,[37m [39;49;00mb->b_type,[37m [39;49;00mb->b_handler,[37m[39;49;00m$
  2481	[37m						   [39;49;00mb->b_level);[37m[39;49;00m$
  2482	[37m				[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_NOT;[37m[39;49;00m$
  2483	[37m				[39;49;00mJUMPTO(PyInt_AS_LONG(retval));[37m[39;49;00m$
  2484	[37m				[39;49;00mPy_DECREF(retval);[37m[39;49;00m$
  2485	[37m				[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2486	[37m			[39;49;00m}[37m[39;49;00m$
  2487	[37m[39;49;00m$
  2488	[37m			[39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(STACK_LEVEL()[37m [39;49;00m>[37m [39;49;00mb->b_level)[37m [39;49;00m{[37m[39;49;00m$
  2489	[37m				[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  2490	[37m				[39;49;00mPy_XDECREF(v);[37m[39;49;00m$
  2491	[37m			[39;49;00m}[37m[39;49;00m$
  2492	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(b->b_type[37m [39;49;00m==[37m [39;49;00mSETUP_LOOP[37m [39;49;00m&&[37m [39;49;00mwhy[37m [39;49;00m==[37m [39;49;00mWHY_BREAK)[37m [39;49;00m{[37m[39;49;00m$
  2493	[37m				[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_NOT;[37m[39;49;00m$
  2494	[37m				[39;49;00mJUMPTO(b->b_handler);[37m[39;49;00m$
  2495	[37m				[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2496	[37m			[39;49;00m}[37m[39;49;00m$
  2497	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(b->b_type[37m [39;49;00m==[37m [39;49;00mSETUP_FINALLY[37m [39;49;00m||[37m[39;49;00m$
  2498	[37m			    [39;49;00m(b->b_type[37m [39;49;00m==[37m [39;49;00mSETUP_EXCEPT[37m [39;49;00m&&[37m[39;49;00m$
  2499	[37m			     [39;49;00mwhy[37m [39;49;00m==[37m [39;49;00mWHY_EXCEPTION))[37m [39;49;00m{[37m[39;49;00m$
  2500	[37m				[39;49;00m[34mif[39;49;00m[37m [39;49;00m(why[37m [39;49;00m==[37m [39;49;00mWHY_EXCEPTION)[37m [39;49;00m{[37m[39;49;00m$
  2501	[37m					[39;49;00mPyObject[37m [39;49;00m*exc,[37m [39;49;00m*val,[37m [39;49;00m*tb;[37m[39;49;00m$
  2502	[37m					[39;49;00mPyErr_Fetch(&exc,[37m [39;49;00m&val,[37m [39;49;00m&tb);[37m[39;49;00m$
  2503	[37m					[39;49;00m[34mif[39;49;00m[37m [39;49;00m(val[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  2504	[37m						[39;49;00mval[37m [39;49;00m=[37m [39;49;00mPy_None;[37m[39;49;00m$
  2505	[37m						[39;49;00mPy_INCREF(val);[37m[39;49;00m$
  2506	[37m					[39;49;00m}[37m[39;49;00m$
  2507	[37m					[39;49;00m[37m/* Make the raw exception data[39;49;00m$
  2508	[37m					   available to the handler,[39;49;00m$
  2509	[37m					   so a program can emulate the[39;49;00m$
  2510	[37m					   Python main loop.  Don't do[39;49;00m$
  2511	[37m					   this for 'finally'. */[39;49;00m[37m[39;49;00m$
  2512	[37m					[39;49;00m[34mif[39;49;00m[37m [39;49;00m(b->b_type[37m [39;49;00m==[37m [39;49;00mSETUP_EXCEPT)[37m [39;49;00m{[37m[39;49;00m$
  2513	[37m						[39;49;00mPyErr_NormalizeException([37m[39;49;00m$
  2514	[37m							[39;49;00m&exc,[37m [39;49;00m&val,[37m [39;49;00m&tb);[37m[39;49;00m$
  2515	[37m						[39;49;00mset_exc_info(tstate,[37m[39;49;00m$
  2516	[37m							     [39;49;00mexc,[37m [39;49;00mval,[37m [39;49;00mtb);[37m[39;49;00m$
  2517	[37m					[39;49;00m}[37m[39;49;00m$
  2518	[37m					[39;49;00m[34mif[39;49;00m[37m [39;49;00m(tb[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
  2519	[37m						[39;49;00mPy_INCREF(Py_None);[37m[39;49;00m$
  2520	[37m						[39;49;00mPUSH(Py_None);[37m[39;49;00m$
  2521	[37m					[39;49;00m}[37m [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  2522	[37m						[39;49;00mPUSH(tb);[37m[39;49;00m$
  2523	[37m					[39;49;00mPUSH(val);[37m[39;49;00m$
  2524	[37m					[39;49;00mPUSH(exc);[37m[39;49;00m$
  2525	[37m				[39;49;00m}[37m[39;49;00m$
  2526	[37m				[39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
  2527	[37m					[39;49;00m[34mif[39;49;00m[37m [39;49;00m(why[37m [39;49;00m&[37m [39;49;00m(WHY_RETURN[37m [39;49;00m|[37m [39;49;00mWHY_CONTINUE))[37m[39;49;00m$
  2528	[37m						[39;49;00mPUSH(retval);[37m[39;49;00m$
  2529	[37m					[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPyInt_FromLong(([36mlong[39;49;00m)why);[37m[39;49;00m$
  2530	[37m					[39;49;00mPUSH(v);[37m[39;49;00m$
  2531	[37m				[39;49;00m}[37m[39;49;00m$
  2532	[37m				[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_NOT;[37m[39;49;00m$
  2533	[37m				[39;49;00mJUMPTO(b->b_handler);[37m[39;49;00m$
  2534	[37m				[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2535	[37m			[39;49;00m}[37m[39;49;00m$
  2536	[37m		[39;49;00m}[37m [39;49;00m[37m/* unwind stack */[39;49;00m[37m[39;49;00m$
  2537	[37m[39;49;00m$
  2538	[37m		[39;49;00m[37m/* End the loop if we still have an error (or return) */[39;49;00m[37m[39;49;00m$
  2539	[37m[39;49;00m$
  2540	[37m		[39;49;00m[34mif[39;49;00m[37m [39;49;00m(why[37m [39;49;00m!=[37m [39;49;00mWHY_NOT)[37m[39;49;00m$
  2541	[37m			[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  2542	[37m		[39;49;00mREAD_TIMESTAMP(loop1);[37m[39;49;00m$
  2543	[37m[39;49;00m$
  2544	[37m	[39;49;00m}[37m [39;49;00m[37m/* main loop */[39;49;00m[37m[39;49;00m$
  2545	[37m[39;49;00m$
  2546	[37m	[39;49;00massert(why[37m [39;49;00m!=[37m [39;49;00mWHY_YIELD);[37m[39;49;00m$
  2547	[37m	[39;49;00m[37m/* Pop remaining stack entries. */[39;49;00m[37m[39;49;00m$
  2548	[37m	[39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(!EMPTY())[37m [39;49;00m{[37m[39;49;00m$
  2549	[37m		[39;49;00mv[37m [39;49;00m=[37m [39;49;00mPOP();[37m[39;49;00m$
  2550	[37m		[39;49;00mPy_XDECREF(v);[37m[39;49;00m$
  2551	[37m	[39;49;00m}[37m[39;49;00m$
  2552	[37m[39;49;00m$
  2553	[37m	[39;49;00m[34mif[39;49;00m[37m [39;49;00m(why[37m [39;49;00m!=[37m [39;49;00mWHY_RETURN)[37m[39;49;00m$
  2554	[37m		[39;49;00mretval[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  2555	[37m[39;49;00m$
  2556	fast_yield:[37m[39;49;00m$
  2557	[37m	[39;49;00m[34mif[39;49;00m[37m [39;49;00m(tstate->use_tracing)[37m [39;49;00m{[37m[39;49;00m$
  2558	[37m		[39;49;00m[34mif[39;49;00m[37m [39;49;00m(tstate->c_tracefunc)[37m [39;49;00m{[37m[39;49;00m$
  2559	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(why[37m [39;49;00m==[37m [39;49;00mWHY_RETURN[37m [39;49;00m||[37m [39;49;00mwhy[37m [39;49;00m==[37m [39;49;00mWHY_YIELD)[37m [39;49;00m{[37m[39;49;00m$
  2560	[37m				[39;49;00m[34mif[39;49;00m[37m [39;49;00m(call_trace(tstate->c_tracefunc,[37m[39;49;00m$
  2561	[37m					       [39;49;00mtstate->c_traceobj,[37m [39;49;00mf,[37m[39;49;00m$
  2562	[37m					       [39;49;00mPyTrace_RETURN,[37m [39;49;00mretval))[37m [39;49;00m{[37m[39;49;00m$
  2563	[37m					[39;49;00mPy_XDECREF(retval);[37m[39;49;00m$
  2564	[37m					[39;49;00mretval[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  2565	[37m					[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_EXCEPTION;[37m[39;49;00m$
  2566	[37m				[39;49;00m}[37m[39;49;00m$
  2567	[37m			[39;49;00m}[37m[39;49;00m$
  2568	[37m			[39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(why[37m [39;49;00m==[37m [39;49;00mWHY_EXCEPTION)[37m [39;49;00m{[37m[39;49;00m$
  2569	[37m				[39;49;00mcall_trace_protected(tstate->c_tracefunc,[37m[39;49;00m$
  2570	[37m						     [39;49;00mtstate->c_traceobj,[37m [39;49;00mf,[37m[39;49;00m$
  2571	[37m						     [39;49;00mPyTrace_RETURN,[37m [39;49;00m[36mNULL[39;49;00m);[37m[39;49;00m$
  2572	[37m			[39;49;00m}[37m[39;49;00m$
  2573	[37m		[39;49;00m}[37m[39;49;00m$
  2574	[37m		[39;49;00m[34mif[39;49;00m[37m [39;49;00m(tstate->c_profilefunc)[37m [39;49;00m{[37m[39;49;00m$
  2575	[37m			[39;49;00m[34mif[39;49;00m[37m [39;49;00m(why[37m [39;49;00m==[37m [39;49;00mWHY_EXCEPTION)[37m[39;49;00m$
  2576	[37m				[39;49;00mcall_trace_protected(tstate->c_profilefunc,[37m[39;49;00m$
  2577	[37m						     [39;49;00mtstate->c_profileobj,[37m [39;49;00mf,[37m[39;49;00m$
  2578	[37m						     [39;49;00mPyTrace_RETURN,[37m [39;49;00m[36mNULL[39;49;00m);[37m[39;49;00m$
  2579	[37m			[39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(call_trace(tstate->c_profilefunc,[37m[39;49;00m$
  2580	[37m					    [39;49;00mtstate->c_profileobj,[37m [39;49;00mf,[37m[39;49;00m$
  2581	[37m					    [39;49;00mPyTrace_RETURN,[37m [39;49;00mretval))[37m [39;49;00m{[37m[39;49;00m$
  2582	[37m				[39;49;00mPy_XDECREF(retval);[37m[39;49;00m$
  2583	[37m				[39;49;00mretval[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  2584	[37m				[39;49;00mwhy[37m [39;49;00m=[37m [39;49;00mWHY_EXCEPTION;[37m[39;49;00m$
  2585	[37m			[39;49;00m}[37m[39;49;00m$
  2586	[37m		[39;49;00m}[37m[39;49;00m$
  2587	[37m	[39;49;00m}[37m[39;49;00m$
  2588	[37m[39;49;00m$
  2589	[37m	[39;49;00m[34mif[39;49;00m[37m [39;49;00m(tstate->frame->f_exc_type[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
  2590	[37m		[39;49;00mreset_exc_info(tstate);[37m[39;49;00m$
  2591	[37m	[39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
  2592	[37m		[39;49;00massert(tstate->frame->f_exc_value[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m);[37m[39;49;00m$
  2593	[37m		[39;49;00massert(tstate->frame->f_exc_traceback[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m);[37m[39;49;00m$
  2594	[37m	[39;49;00m}[37m[39;49;00m$
  2595	[37m[39;49;00m$
  2596	[37m	[39;49;00m[37m/* pop frame */[39;49;00m[37m[39;49;00m$
  2597	[37m    [39;49;00mexit_eval_frame:[37m[39;49;00m$
  2598	[37m	[39;49;00mPy_LeaveRecursiveCall();[37m[39;49;00m$
  2599	[37m	[39;49;00mtstate->frame[37m [39;49;00m=[37m [39;49;00mf->f_back;[37m[39;49;00m$
  2600	[37m[39;49;00m$
  2601	[37m	[39;49;00m[34mreturn[39;49;00m[37m [39;49;00mretval;[37m[39;49;00m$
  2602	}$

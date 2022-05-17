     1	[37m# Generated automatically from Makefile.pre by makesetup.[39;49;00m$
     2	[37m# Top-level Makefile for Python[39;49;00m$
     3	[37m#[39;49;00m$
     4	[37m# As distributed, this file is called Makefile.pre.in; it is processed[39;49;00m$
     5	[37m# into the real Makefile by running the script ./configure, which[39;49;00m$
     6	[37m# replaces things like @spam@ with values appropriate for your system.[39;49;00m$
     7	[37m# This means that if you edit Makefile, your changes get lost the next[39;49;00m$
     8	[37m# time you run the configure script.  Ideally, you can do:[39;49;00m$
     9	[37m#[39;49;00m$
    10	[37m#	./configure[39;49;00m$
    11	[37m#	make[39;49;00m$
    12	[37m#	make test[39;49;00m$
    13	[37m#	make install[39;49;00m$
    14	[37m#[39;49;00m$
    15	[37m# If you have a previous version of Python installed that you don't[39;49;00m$
    16	[37m# want to overwrite, you can use "make altinstall" instead of "make[39;49;00m$
    17	[37m# install".  Refer to the "Installing" section in the README file for[39;49;00m$
    18	[37m# additional details.[39;49;00m$
    19	[37m#[39;49;00m$
    20	[37m# See also the section "Build instructions" in the README file.[39;49;00m$
    21	$
    22	[37m# === Variables set by makesetup ===[39;49;00m$
    23	$
    24	[31mMODOBJS[39;49;00m=          Modules/threadmodule.o  Modules/signalmodule.o  Modules/posixmodule.o  Modules/errnomodule.o  Modules/pwdmodule.o  Modules/_sre.o  Modules/_codecsmodule.o  Modules/zipimport.o  Modules/symtablemodule.o  Modules/xxsubtype.o$
    25	[31mMODLIBS[39;49;00m=        [34m$([39;49;00mLOCALMODLIBS[34m)[39;49;00m [34m$([39;49;00mBASEMODLIBS[34m)[39;49;00m$
    26	$
    27	[37m# === Variables set by configure[39;49;00m$
    28	[31mVERSION[39;49;00m=	[34m2[39;49;00m.6$
    29	[31msrcdir[39;49;00m=		.$
    30	$
    31	$
    32	[31mCC[39;49;00m=		gcc -pthread$
    33	[31mCXX[39;49;00m=		g++ -pthread$
    34	[31mMAINCC[39;49;00m=		[34m$([39;49;00mCC[34m)[39;49;00m$
    35	[31mLINKCC[39;49;00m=		[34m$([39;49;00mPURIFY[34m)[39;49;00m [34m$([39;49;00mMAINCC[34m)[39;49;00m$
    36	[31mAR[39;49;00m=		ar$
    37	[31mRANLIB[39;49;00m=		ranlib$
    38	[31mSVNVERSION[39;49;00m=	svnversion [34m$([39;49;00msrcdir[34m)[39;49;00m$
    39	$
    40	[37m# Shell used by make (some versions default to the login shell, which is bad)[39;49;00m$
    41	[31mSHELL[39;49;00m=		/bin/sh$
    42	$
    43	[37m# Use this to make a link between python$(VERSION) and python in $(BINDIR)[39;49;00m$
    44	[31mLN[39;49;00m=		ln$
    45	$
    46	[37m# Portable install script (configure doesn't always guess right)[39;49;00m$
    47	[31mINSTALL[39;49;00m=	/usr/bin/install -c$
    48	[31mINSTALL_PROGRAM[39;49;00m=[33m${[39;49;00m[31mINSTALL[39;49;00m[33m}[39;49;00m$
    49	[31mINSTALL_SCRIPT[39;49;00m= [33m${[39;49;00m[31mINSTALL[39;49;00m[33m}[39;49;00m$
    50	[31mINSTALL_DATA[39;49;00m=	[33m${[39;49;00m[31mINSTALL[39;49;00m[33m}[39;49;00m -m [34m644[39;49;00m$
    51	[37m# Shared libraries must be installed with executable mode on some systems;[39;49;00m$
    52	[37m# rather than figuring out exactly which, we always give them executable mode.[39;49;00m$
    53	[37m# Also, making them read-only seems to be a good idea...[39;49;00m$
    54	[31mINSTALL_SHARED[39;49;00m= [33m${[39;49;00m[31mINSTALL[39;49;00m[33m}[39;49;00m -m [34m555[39;49;00m$
    55	$
    56	[31mMAKESETUP[39;49;00m=      [34m$([39;49;00msrcdir[34m)[39;49;00m/Modules/makesetup$
    57	$
    58	[37m# Compiler options[39;49;00m$
    59	[31mOPT[39;49;00m=		-g -Wall -Wstrict-prototypes$
    60	[31mBASECFLAGS[39;49;00m=	 -fno-strict-aliasing$
    61	[31mCFLAGS[39;49;00m=		[34m$([39;49;00mBASECFLAGS[34m)[39;49;00m [34m$([39;49;00mOPT[34m)[39;49;00m [34m$([39;49;00mEXTRA_CFLAGS[34m)[39;49;00m$
    62	[37m# Both CPPFLAGS and LDFLAGS need to contain the shell's value for setup.py to[39;49;00m$
    63	[37m# be able to build extension modules using the directories specified in the[39;49;00m$
    64	[37m# environment variables[39;49;00m$
    65	[31mCPPFLAGS[39;49;00m=	-I. -I[34m$([39;49;00msrcdir[34m)[39;49;00m/Include $
    66	[31mLDFLAGS[39;49;00m=	$
    67	[31mLDLAST[39;49;00m=		$
    68	[31mSGI_ABI[39;49;00m=	$
    69	[31mCCSHARED[39;49;00m=	-fPIC$
    70	[31mLINKFORSHARED[39;49;00m=	-Xlinker -export-dynamic$
    71	[37m# Extra C flags added for building the interpreter object files.[39;49;00m$
    72	[31mCFLAGSFORSHARED[39;49;00m=$
    73	[37m# C flags used for building the interpreter object files[39;49;00m$
    74	[31mPY_CFLAGS[39;49;00m=	[34m$([39;49;00mCFLAGS[34m)[39;49;00m [34m$([39;49;00mCPPFLAGS[34m)[39;49;00m [34m$([39;49;00mCFLAGSFORSHARED[34m)[39;49;00m -DPy_BUILD_CORE$
    75	$
    76	$
    77	[37m# Machine-dependent subdirectories[39;49;00m$
    78	[31mMACHDEP[39;49;00m=	linux2$
    79	$
    80	[37m# Install prefix for architecture-independent files[39;49;00m$
    81	[31mprefix[39;49;00m=		/usr/local$
    82	$
    83	[37m# Install prefix for architecture-dependent files[39;49;00m$
    84	[31mexec_prefix[39;49;00m=	[33m${[39;49;00m[31mprefix[39;49;00m[33m}[39;49;00m$
    85	$
    86	[37m# Expanded directories[39;49;00m$
    87	[31mBINDIR[39;49;00m=		[34m$([39;49;00mexec_prefix[34m)[39;49;00m/bin$
    88	[31mLIBDIR[39;49;00m=		[34m$([39;49;00mexec_prefix[34m)[39;49;00m/lib$
    89	[31mMANDIR[39;49;00m=		[33m${[39;49;00m[31mprefix[39;49;00m[33m}[39;49;00m/man$
    90	[31mINCLUDEDIR[39;49;00m=	[33m${[39;49;00m[31mprefix[39;49;00m[33m}[39;49;00m/include$
    91	[31mCONFINCLUDEDIR[39;49;00m=	[34m$([39;49;00mexec_prefix[34m)[39;49;00m/include$
    92	[31mSCRIPTDIR[39;49;00m=	[34m$([39;49;00mprefix[34m)[39;49;00m/lib$
    93	$
    94	[37m# Detailed destination directories[39;49;00m$
    95	[31mBINLIBDEST[39;49;00m=	[34m$([39;49;00mLIBDIR[34m)[39;49;00m/python[34m$([39;49;00mVERSION[34m)[39;49;00m$
    96	[31mLIBDEST[39;49;00m=	[34m$([39;49;00mSCRIPTDIR[34m)[39;49;00m/python[34m$([39;49;00mVERSION[34m)[39;49;00m$
    97	[31mINCLUDEPY[39;49;00m=	[34m$([39;49;00mINCLUDEDIR[34m)[39;49;00m/python[34m$([39;49;00mVERSION[34m)[39;49;00m$
    98	[31mCONFINCLUDEPY[39;49;00m=	[34m$([39;49;00mCONFINCLUDEDIR[34m)[39;49;00m/python[34m$([39;49;00mVERSION[34m)[39;49;00m$
    99	[31mLIBP[39;49;00m=		[34m$([39;49;00mLIBDIR[34m)[39;49;00m/python[34m$([39;49;00mVERSION[34m)[39;49;00m$
   100	$
   101	[37m# Symbols used for using shared libraries[39;49;00m$
   102	[31mSO[39;49;00m=		.so$
   103	[31mLDSHARED[39;49;00m=	[34m$([39;49;00mCC[34m)[39;49;00m -shared$
   104	[31mBLDSHARED[39;49;00m=	[34m$([39;49;00mCC[34m)[39;49;00m -shared$
   105	[31mDESTSHARED[39;49;00m=	[34m$([39;49;00mBINLIBDEST[34m)[39;49;00m/lib-dynload$
   106	$
   107	[37m# Executable suffix (.exe on Windows and Mac OS X)[39;49;00m$
   108	[31mEXE[39;49;00m=		$
   109	[31mBUILDEXE[39;49;00m=	$
   110	$
   111	[37m# Short name and location for Mac OS X Python framework[39;49;00m$
   112	[31mUNIVERSALSDK[39;49;00m=$
   113	[31mPYTHONFRAMEWORK[39;49;00m=	$
   114	[31mPYTHONFRAMEWORKDIR[39;49;00m=	no-framework$
   115	[31mPYTHONFRAMEWORKPREFIX[39;49;00m=	$
   116	[31mPYTHONFRAMEWORKINSTALLDIR[39;49;00m= $
   117	[37m# Deployment target selected during configure, to be checked[39;49;00m$
   118	[37m# by distutils. The export statement is needed to ensure that the[39;49;00m$
   119	[37m# deployment target is active during build.[39;49;00m$
   120	[31mMACOSX_DEPLOYMENT_TARGET[39;49;00m=$
   121	[37m#export MACOSX_DEPLOYMENT_TARGET[39;49;00m$
   122	$
   123	[37m# Options to enable prebinding (for fast startup prior to Mac OS X 10.3)[39;49;00m$
   124	[31mOTHER_LIBTOOL_OPT[39;49;00m=$
   125	$
   126	[37m# Environment to run shared python without installed libraries[39;49;00m$
   127	[31mRUNSHARED[39;49;00m=       $
   128	$
   129	[37m# Modes for directories, executables and data files created by the[39;49;00m$
   130	[37m# install process.  Default to user-only-writable for all file types.[39;49;00m$
   131	[31mDIRMODE[39;49;00m=	[34m755[39;49;00m$
   132	[31mEXEMODE[39;49;00m=	[34m755[39;49;00m$
   133	[31mFILEMODE[39;49;00m=	[34m644[39;49;00m$
   134	$
   135	[37m# configure script arguments[39;49;00m$
   136	[31mCONFIG_ARGS[39;49;00m=	[33m'--with-pydebug'[39;49;00m$
   137	$
   138	$
   139	[37m# Subdirectories with code[39;49;00m$
   140	[31mSRCDIRS[39;49;00m= 	Parser Grammar Objects Python Modules Mac$
   141	$
   142	[37m# Other subdirectories[39;49;00m$
   143	[31mSUBDIRSTOO[39;49;00m=	Include Lib Misc Demo$
   144	$
   145	[37m# Files and directories to be distributed[39;49;00m$
   146	[31mCONFIGFILES[39;49;00m=	configure configure.in acconfig.h pyconfig.h.in Makefile.pre.in$
   147	[31mDISTFILES[39;49;00m=	README ChangeLog [34m$([39;49;00mCONFIGFILES[34m)[39;49;00m$
   148	[31mDISTDIRS[39;49;00m=	[34m$([39;49;00mSUBDIRS[34m)[39;49;00m [34m$([39;49;00mSUBDIRSTOO[34m)[39;49;00m Ext-dummy$
   149	[31mDIST[39;49;00m=		[34m$([39;49;00mDISTFILES[34m)[39;49;00m [34m$([39;49;00mDISTDIRS[34m)[39;49;00m$
   150	$
   151	$
   152	[31mLIBRARY[39;49;00m=	libpython[34m$([39;49;00mVERSION[34m)[39;49;00m.a$
   153	[31mLDLIBRARY[39;49;00m=      libpython[34m$([39;49;00mVERSION[34m)[39;49;00m.a$
   154	[31mBLDLIBRARY[39;49;00m=     [34m$([39;49;00mLDLIBRARY[34m)[39;49;00m$
   155	[31mDLLLIBRARY[39;49;00m=	$
   156	[31mLDLIBRARYDIR[39;49;00m=   $
   157	[31mINSTSONAME[39;49;00m=	[34m$([39;49;00mLDLIBRARY[34m)[39;49;00m$
   158	$
   159	$
   160	[31mLIBS[39;49;00m=		-lpthread -ldl  -lutil$
   161	[31mLIBM[39;49;00m=		-lm$
   162	[31mLIBC[39;49;00m=		$
   163	[31mSYSLIBS[39;49;00m=	[34m$([39;49;00mLIBM[34m)[39;49;00m [34m$([39;49;00mLIBC[34m)[39;49;00m$
   164	[31mSHLIBS[39;49;00m=		[34m$([39;49;00mLIBS[34m)[39;49;00m$
   165	$
   166	[31mTHREADOBJ[39;49;00m=	Python/thread.o$
   167	[31mDLINCLDIR[39;49;00m=	.$
   168	[31mDYNLOADFILE[39;49;00m=	dynload_shlib.o$
   169	[31mMACHDEP_OBJS[39;49;00m=	$
   170	[31mUNICODE_OBJS[39;49;00m=   Objects/unicodeobject.o Objects/unicodectype.o$
   171	$
   172	[31mPYTHON[39;49;00m=		python[34m$([39;49;00mEXE[34m)[39;49;00m$
   173	[31mBUILDPYTHON[39;49;00m=	python[34m$([39;49;00mBUILDEXE[34m)[39;49;00m$
   174	$
   175	[37m# === Definitions added by makesetup ===[39;49;00m$
   176	$
   177	[31mLOCALMODLIBS[39;49;00m=          $
   178	[31mBASEMODLIBS[39;49;00m=$
   179	[31mGLHACK[39;49;00m=-Dclear=__GLclear$
   180	[31mPYTHONPATH[39;49;00m=[34m$([39;49;00mCOREPYTHONPATH[34m)[39;49;00m$
   181	[31mCOREPYTHONPATH[39;49;00m=[34m$([39;49;00mDESTPATH[34m)[39;49;00m[34m$([39;49;00mSITEPATH[34m)[39;49;00m[34m$([39;49;00mTESTPATH[34m)[39;49;00m[34m$([39;49;00mMACHDEPPATH[34m)[39;49;00m[34m$([39;49;00mEXTRAMACHDEPPATH[34m)[39;49;00m[34m$([39;49;00mTKPATH[34m)[39;49;00m$
   182	[31mTKPATH[39;49;00m=:lib-tk$
   183	[31mEXTRAMACHDEPPATH[39;49;00m=$
   184	[31mMACHDEPPATH[39;49;00m=:plat-[34m$([39;49;00mMACHDEP[34m)[39;49;00m$
   185	[31mTESTPATH[39;49;00m=$
   186	[31mSITEPATH[39;49;00m=$
   187	[31mDESTPATH[39;49;00m=$
   188	[31mMACHDESTLIB[39;49;00m=[34m$([39;49;00mBINLIBDEST[34m)[39;49;00m$
   189	[31mDESTLIB[39;49;00m=[34m$([39;49;00mLIBDEST[34m)[39;49;00m$
   190	$
   191	$
   192	$
   193	[37m##########################################################################[39;49;00m$
   194	[37m# Modules[39;49;00m$
   195	[31mMODULE_OBJS[39;49;00m=	[33m\[39;49;00m$
   196			Modules/config.o [33m\[39;49;00m$
   197			Modules/getpath.o [33m\[39;49;00m$
   198			Modules/main.o [33m\[39;49;00m$
   199			Modules/gcmodule.o$
   200	$
   201	[37m# Used of signalmodule.o is not available[39;49;00m$
   202	[31mSIGNAL_OBJS[39;49;00m=	$
   203	$
   204	$
   205	[37m##########################################################################[39;49;00m$
   206	[37m# Grammar[39;49;00m$
   207	[31mGRAMMAR_H[39;49;00m=	[34m$([39;49;00msrcdir[34m)[39;49;00m/Include/graminit.h$
   208	[31mGRAMMAR_C[39;49;00m=	[34m$([39;49;00msrcdir[34m)[39;49;00m/Python/graminit.c$
   209	[31mGRAMMAR_INPUT[39;49;00m=	[34m$([39;49;00msrcdir[34m)[39;49;00m/Grammar/Grammar$
   210	$
   211	$
   212	[37m##########################################################################[39;49;00m$
   213	[37m# Parser[39;49;00m$
   214	[31mPGEN[39;49;00m=		Parser/pgen[34m$([39;49;00mEXE[34m)[39;49;00m$
   215	$
   216	[31mPOBJS[39;49;00m=		[33m\[39;49;00m$
   217			Parser/acceler.o [33m\[39;49;00m$
   218			Parser/grammar1.o [33m\[39;49;00m$
   219			Parser/listnode.o [33m\[39;49;00m$
   220			Parser/node.o [33m\[39;49;00m$
   221			Parser/parser.o [33m\[39;49;00m$
   222			Parser/parsetok.o [33m\[39;49;00m$
   223			Parser/bitset.o [33m\[39;49;00m$
   224			Parser/metagrammar.o [33m\[39;49;00m$
   225			Parser/firstsets.o [33m\[39;49;00m$
   226			Parser/grammar.o [33m\[39;49;00m$
   227			Parser/pgen.o$
   228	$
   229	[31mPARSER_OBJS[39;49;00m=	[34m$([39;49;00mPOBJS[34m)[39;49;00m Parser/myreadline.o Parser/tokenizer.o$
   230	$
   231	[31mPGOBJS[39;49;00m=		[33m\[39;49;00m$
   232			Objects/obmalloc.o [33m\[39;49;00m$
   233			Python/mysnprintf.o [33m\[39;49;00m$
   234			Parser/tokenizer_pgen.o [33m\[39;49;00m$
   235			Parser/printgrammar.o [33m\[39;49;00m$
   236			Parser/pgenmain.o$
   237	$
   238	[31mPGENOBJS[39;49;00m=	[34m$([39;49;00mPGENMAIN[34m)[39;49;00m [34m$([39;49;00mPOBJS[34m)[39;49;00m [34m$([39;49;00mPGOBJS[34m)[39;49;00m$
   239	$
   240	[37m##########################################################################[39;49;00m$
   241	[37m# AST[39;49;00m$
   242	[31mAST_H_DIR[39;49;00m=	[34m$([39;49;00msrcdir[34m)[39;49;00m/Include$
   243	[31mAST_H[39;49;00m=		[34m$([39;49;00mAST_H_DIR[34m)[39;49;00m/Python-ast.h$
   244	[31mAST_C_DIR[39;49;00m=	[34m$([39;49;00msrcdir[34m)[39;49;00m/Python$
   245	[31mAST_C[39;49;00m=		[34m$([39;49;00mAST_C_DIR[34m)[39;49;00m/Python-ast.c$
   246	[31mAST_ASDL[39;49;00m=	[34m$([39;49;00msrcdir[34m)[39;49;00m/Parser/Python.asdl$
   247	$
   248	[31mASDLGEN_FILES[39;49;00m=	[34m$([39;49;00msrcdir[34m)[39;49;00m/Parser/asdl.py [34m$([39;49;00msrcdir[34m)[39;49;00m/Parser/asdl_c.py$
   249	[37m# XXX Note that a build now requires Python exist before the build starts[39;49;00m$
   250	[31mASDLGEN[39;49;00m=	[34m$([39;49;00msrcdir[34m)[39;49;00m/Parser/asdl_c.py$
   251	$
   252	[37m##########################################################################[39;49;00m$
   253	[37m# Python[39;49;00m$
   254	[31mPYTHON_OBJS[39;49;00m=	[33m\[39;49;00m$
   255			Python/Python-ast.o [33m\[39;49;00m$
   256			Python/asdl.o [33m\[39;49;00m$
   257			Python/ast.o [33m\[39;49;00m$
   258			Python/bltinmodule.o [33m\[39;49;00m$
   259			Python/ceval.o [33m\[39;49;00m$
   260			Python/compile.o [33m\[39;49;00m$
   261			Python/codecs.o [33m\[39;49;00m$
   262			Python/errors.o [33m\[39;49;00m$
   263			Python/frozen.o [33m\[39;49;00m$
   264			Python/frozenmain.o [33m\[39;49;00m$
   265			Python/future.o [33m\[39;49;00m$
   266			Python/getargs.o [33m\[39;49;00m$
   267			Python/getcompiler.o [33m\[39;49;00m$
   268			Python/getcopyright.o [33m\[39;49;00m$
   269			Python/getmtime.o [33m\[39;49;00m$
   270			Python/getplatform.o [33m\[39;49;00m$
   271			Python/getversion.o [33m\[39;49;00m$
   272			Python/graminit.o [33m\[39;49;00m$
   273			Python/import.o [33m\[39;49;00m$
   274			Python/importdl.o [33m\[39;49;00m$
   275			Python/marshal.o [33m\[39;49;00m$
   276			Python/modsupport.o [33m\[39;49;00m$
   277			Python/mystrtoul.o [33m\[39;49;00m$
   278			Python/mysnprintf.o [33m\[39;49;00m$
   279			Python/peephole.o [33m\[39;49;00m$
   280			Python/pyarena.o [33m\[39;49;00m$
   281			Python/pyfpe.o [33m\[39;49;00m$
   282			Python/pystate.o [33m\[39;49;00m$
   283			Python/pythonrun.o [33m\[39;49;00m$
   284			Python/structmember.o [33m\[39;49;00m$
   285			Python/symtable.o [33m\[39;49;00m$
   286			Python/sysmodule.o [33m\[39;49;00m$
   287			Python/traceback.o [33m\[39;49;00m$
   288			Python/getopt.o [33m\[39;49;00m$
   289			Python/pystrtod.o [33m\[39;49;00m$
   290			Python/[34m$([39;49;00mDYNLOADFILE[34m)[39;49;00m [33m\[39;49;00m$
   291			[34m$([39;49;00mMACHDEP_OBJS[34m)[39;49;00m [33m\[39;49;00m$
   292			[34m$([39;49;00mTHREADOBJ[34m)[39;49;00m$
   293	$
   294	$
   295	[37m##########################################################################[39;49;00m$
   296	[37m# Objects[39;49;00m$
   297	[31mOBJECT_OBJS[39;49;00m=	[33m\[39;49;00m$
   298			Objects/abstract.o [33m\[39;49;00m$
   299			Objects/boolobject.o [33m\[39;49;00m$
   300			Objects/bufferobject.o [33m\[39;49;00m$
   301			Objects/cellobject.o [33m\[39;49;00m$
   302			Objects/classobject.o [33m\[39;49;00m$
   303			Objects/cobject.o [33m\[39;49;00m$
   304			Objects/codeobject.o [33m\[39;49;00m$
   305			Objects/complexobject.o [33m\[39;49;00m$
   306			Objects/descrobject.o [33m\[39;49;00m$
   307			Objects/enumobject.o [33m\[39;49;00m$
   308			Objects/exceptions.o [33m\[39;49;00m$
   309			Objects/genobject.o [33m\[39;49;00m$
   310			Objects/fileobject.o [33m\[39;49;00m$
   311			Objects/floatobject.o [33m\[39;49;00m$
   312			Objects/frameobject.o [33m\[39;49;00m$
   313			Objects/funcobject.o [33m\[39;49;00m$
   314			Objects/intobject.o [33m\[39;49;00m$
   315			Objects/iterobject.o [33m\[39;49;00m$
   316			Objects/listobject.o [33m\[39;49;00m$
   317			Objects/longobject.o [33m\[39;49;00m$
   318			Objects/dictobject.o [33m\[39;49;00m$
   319			Objects/methodobject.o [33m\[39;49;00m$
   320			Objects/moduleobject.o [33m\[39;49;00m$
   321			Objects/object.o [33m\[39;49;00m$
   322			Objects/obmalloc.o [33m\[39;49;00m$
   323			Objects/rangeobject.o [33m\[39;49;00m$
   324	                Objects/setobject.o [33m\[39;49;00m$
   325			Objects/sliceobject.o [33m\[39;49;00m$
   326			Objects/stringobject.o [33m\[39;49;00m$
   327			Objects/structseq.o [33m\[39;49;00m$
   328			Objects/tupleobject.o [33m\[39;49;00m$
   329			Objects/typeobject.o [33m\[39;49;00m$
   330			Objects/weakrefobject.o [33m\[39;49;00m$
   331			[34m$([39;49;00mUNICODE_OBJS[34m)[39;49;00m$
   332	$
   333	$
   334	[37m##########################################################################[39;49;00m$
   335	[37m# objects that get linked into the Python library[39;49;00m$
   336	[31mLIBRARY_OBJS[39;49;00m=	[33m\[39;49;00m$
   337			Modules/_typesmodule.o [33m\[39;49;00m$
   338			Modules/getbuildinfo.o [33m\[39;49;00m$
   339			[34m$([39;49;00mPARSER_OBJS[34m)[39;49;00m [33m\[39;49;00m$
   340			[34m$([39;49;00mOBJECT_OBJS[34m)[39;49;00m [33m\[39;49;00m$
   341			[34m$([39;49;00mPYTHON_OBJS[34m)[39;49;00m [33m\[39;49;00m$
   342			[34m$([39;49;00mMODULE_OBJS[34m)[39;49;00m [33m\[39;49;00m$
   343			[34m$([39;49;00mSIGNAL_OBJS[34m)[39;49;00m [33m\[39;49;00m$
   344			[34m$([39;49;00mMODOBJS[34m)[39;49;00m$
   345	$
   346	[37m#########################################################################[39;49;00m$
   347	[37m# Rules[39;49;00m$
   348	$
   349	[37m# Default target[39;49;00m$
   350	[32mall[39;49;00m:		[34m$([39;49;00m[31mBUILDPYTHON[39;49;00m[34m)[39;49;00m oldsharedmods sharedmods$
   351	$
   352	[37m# Build the interpreter[39;49;00m$
   353	[32m$(BUILDPYTHON)[39;49;00m:	Modules/python.o [34m$([39;49;00m[31mLIBRARY[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31mLDLIBRARY[39;49;00m[34m)[39;49;00m$
   354			[34m$([39;49;00mLINKCC[34m)[39;49;00m [34m$([39;49;00mLDFLAGS[34m)[39;49;00m [34m$([39;49;00mLINKFORSHARED[34m)[39;49;00m -o [31m$@[39;49;00m [33m\[39;49;00m$
   355				Modules/python.o [33m\[39;49;00m$
   356				[34m$([39;49;00mBLDLIBRARY[34m)[39;49;00m [34m$([39;49;00mLIBS[34m)[39;49;00m [34m$([39;49;00mMODLIBS[34m)[39;49;00m [34m$([39;49;00mSYSLIBS[34m)[39;49;00m [34m$([39;49;00mLDLAST[34m)[39;49;00m$
   357	$
   358	[32mplatform[39;49;00m: [34m$([39;49;00m[31mBUILDPYTHON[39;49;00m[34m)[39;49;00m$
   359		[34m$([39;49;00mRUNSHARED[34m)[39;49;00m ./[34m$([39;49;00mBUILDPYTHON[34m)[39;49;00m -E -c [33m'import sys ; from distutils.util import get_platform ; print get_platform()+"-"+sys.version[0:3]'[39;49;00m >platform$
   360	$
   361	$
   362	[37m# Build the shared modules[39;49;00m$
   363	[32msharedmods[39;49;00m: [34m$([39;49;00m[31mBUILDPYTHON[39;49;00m[34m)[39;49;00m$
   364		@case [31m$$[39;49;00mMAKEFLAGS [34min[39;49;00m [33m\[39;49;00m$
   365		*-s*) [34m$([39;49;00mRUNSHARED[34m)[39;49;00m [31mCC[39;49;00m=[33m'$(CC)'[39;49;00m [31mLDSHARED[39;49;00m=[33m'$(BLDSHARED)'[39;49;00m [31mOPT[39;49;00m=[33m'$(OPT)'[39;49;00m ./[34m$([39;49;00mBUILDPYTHON[34m)[39;49;00m -E [34m$([39;49;00msrcdir[34m)[39;49;00m/setup.py -q build;; [33m\[39;49;00m$
   366		*) [34m$([39;49;00mRUNSHARED[34m)[39;49;00m [31mCC[39;49;00m=[33m'$(CC)'[39;49;00m [31mLDSHARED[39;49;00m=[33m'$(BLDSHARED)'[39;49;00m [31mOPT[39;49;00m=[33m'$(OPT)'[39;49;00m ./[34m$([39;49;00mBUILDPYTHON[34m)[39;49;00m -E [34m$([39;49;00msrcdir[34m)[39;49;00m/setup.py build;; [33m\[39;49;00m$
   367		[34mesac[39;49;00m$
   368	$
   369	[37m# Build static library[39;49;00m$
   370	[37m# avoid long command lines, same as LIBRARY_OBJS[39;49;00m$
   371	[32m$(LIBRARY)[39;49;00m: [34m$([39;49;00m[31mLIBRARY_OBJS[39;49;00m[34m)[39;49;00m$
   372		-rm -f [31m$@[39;49;00m$
   373		[34m$([39;49;00mAR[34m)[39;49;00m cr [31m$@[39;49;00m Modules/getbuildinfo.o$
   374		[34m$([39;49;00mAR[34m)[39;49;00m cr [31m$@[39;49;00m Modules/_typesmodule.o$
   375		[34m$([39;49;00mAR[34m)[39;49;00m cr [31m$@[39;49;00m [34m$([39;49;00mPARSER_OBJS[34m)[39;49;00m$
   376		[34m$([39;49;00mAR[34m)[39;49;00m cr [31m$@[39;49;00m [34m$([39;49;00mOBJECT_OBJS[34m)[39;49;00m$
   377		[34m$([39;49;00mAR[34m)[39;49;00m cr [31m$@[39;49;00m [34m$([39;49;00mPYTHON_OBJS[34m)[39;49;00m$
   378		[34m$([39;49;00mAR[34m)[39;49;00m cr [31m$@[39;49;00m [34m$([39;49;00mMODULE_OBJS[34m)[39;49;00m [34m$([39;49;00mSIGNAL_OBJS[34m)[39;49;00m$
   379		[34m$([39;49;00mAR[34m)[39;49;00m cr [31m$@[39;49;00m [34m$([39;49;00mMODOBJS[34m)[39;49;00m$
   380		[34m$([39;49;00mRANLIB[34m)[39;49;00m [31m$@[39;49;00m$
   381	$
   382	[32mlibpython$(VERSION).so[39;49;00m: [34m$([39;49;00m[31mLIBRARY_OBJS[39;49;00m[34m)[39;49;00m$
   383	[36m	if test $(INSTSONAME) != $(LDLIBRARY); then \[39;49;00m$
   384	[36m		$(LDSHARED) -Wl,-h$(INSTSONAME) -o $(INSTSONAME) $(LIBRARY_OBJS) $(SHLIBS) $(LIBC) $(LIBM); \[39;49;00m$
   385	[36m		$(LN) -f $(INSTSONAME) $@; \[39;49;00m$
   386	[36m	else\[39;49;00m$
   387	[36m		$(LDSHARED) -o $@ $(LIBRARY_OBJS) $(SHLIBS) $(LIBC) $(LIBM); \[39;49;00m$
   388	[36m	fi[39;49;00m$
   389	$
   390	[32mlibpython$(VERSION).sl[39;49;00m: [34m$([39;49;00m[31mLIBRARY_OBJS[39;49;00m[34m)[39;49;00m$
   391		[34m$([39;49;00mLDSHARED[34m)[39;49;00m -o [31m$@[39;49;00m [34m$([39;49;00mLIBRARY_OBJS[34m)[39;49;00m [34m$([39;49;00mSHLIBS[34m)[39;49;00m [34m$([39;49;00mLIBC[34m)[39;49;00m [34m$([39;49;00mLIBM[34m)[39;49;00m$
   392	$
   393	[37m# This rule is here for OPENSTEP/Rhapsody/MacOSX. It builds a temporary[39;49;00m$
   394	[37m# minimal framework (not including the Lib directory and such) in the current[39;49;00m$
   395	[37m# directory.[39;49;00m$
   396	[31mRESSRCDIR[39;49;00m=[34m$([39;49;00msrcdir[34m)[39;49;00m/Mac/Resources/framework$
   397	[32m$(PYTHONFRAMEWORKDIR)/Versions/$(VERSION)/$(PYTHONFRAMEWORK)[39;49;00m: \$
   398			[34m$([39;49;00m[31mLIBRARY[39;49;00m[34m)[39;49;00m \$
   399			[34m$([39;49;00m[31mRESSRCDIR[39;49;00m[34m)[39;49;00m/Info.plist \$
   400	                [34m$([39;49;00m[31mRESSRCDIR[39;49;00m[34m)[39;49;00m/version.plist \$
   401	                [34m$([39;49;00m[31mRESSRCDIR[39;49;00m[34m)[39;49;00m/English.lproj/InfoPlist.strings$
   402		[34m$([39;49;00mINSTALL[34m)[39;49;00m -d -m [34m$([39;49;00mDIRMODE[34m)[39;49;00m [34m$([39;49;00mPYTHONFRAMEWORKDIR[34m)[39;49;00m/Versions/[34m$([39;49;00mVERSION[34m)[39;49;00m$
   403	[36m	if test "${UNIVERSALSDK}"; then \[39;49;00m$
   404	[36m		$(CC) -o $(LDLIBRARY) -arch i386 -arch ppc -dynamiclib \[39;49;00m$
   405	[36m			-isysroot "${UNIVERSALSDK}" \[39;49;00m$
   406	[36m			-all_load $(LIBRARY) -Wl,-single_module \[39;49;00m$
   407	[36m			-install_name $(DESTDIR)$(PYTHONFRAMEWORKINSTALLDIR)/Versions/$(VERSION)/Python \[39;49;00m$
   408	[36m			-compatibility_version $(VERSION) \[39;49;00m$
   409	[36m			-current_version $(VERSION); \[39;49;00m$
   410	[36m        else \[39;49;00m$
   411	[36m		libtool -o $(LDLIBRARY) -dynamic $(OTHER_LIBTOOL_OPT) $(LIBRARY) \[39;49;00m$
   412	[36m			 ;\[39;49;00m$
   413	[36m	fi[39;49;00m$
   414		[34m$([39;49;00mINSTALL[34m)[39;49;00m -d -m [34m$([39;49;00mDIRMODE[34m)[39;49;00m  [33m\[39;49;00m$
   415			[34m$([39;49;00mPYTHONFRAMEWORKDIR[34m)[39;49;00m/Versions/[34m$([39;49;00mVERSION[34m)[39;49;00m/Resources/English.lproj$
   416		[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m [34m$([39;49;00mRESSRCDIR[34m)[39;49;00m/Info.plist [33m\[39;49;00m$
   417			[34m$([39;49;00mPYTHONFRAMEWORKDIR[34m)[39;49;00m/Versions/[34m$([39;49;00mVERSION[34m)[39;49;00m/Resources/Info.plist$
   418		[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m [34m$([39;49;00mRESSRCDIR[34m)[39;49;00m/version.plist [33m\[39;49;00m$
   419			[34m$([39;49;00mPYTHONFRAMEWORKDIR[34m)[39;49;00m/Versions/[34m$([39;49;00mVERSION[34m)[39;49;00m/Resources/version.plist$
   420		[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m [34m$([39;49;00mRESSRCDIR[34m)[39;49;00m/English.lproj/InfoPlist.strings [33m\[39;49;00m$
   421			[34m$([39;49;00mPYTHONFRAMEWORKDIR[34m)[39;49;00m/Versions/[34m$([39;49;00mVERSION[34m)[39;49;00m/Resources/English.lproj/InfoPlist.strings$
   422		[34m$([39;49;00mLN[34m)[39;49;00m -fsn [34m$([39;49;00mVERSION[34m)[39;49;00m [34m$([39;49;00mPYTHONFRAMEWORKDIR[34m)[39;49;00m/Versions/Current$
   423		[34m$([39;49;00mLN[34m)[39;49;00m -fsn Versions/Current/[34m$([39;49;00mPYTHONFRAMEWORK[34m)[39;49;00m [34m$([39;49;00mPYTHONFRAMEWORKDIR[34m)[39;49;00m/[34m$([39;49;00mPYTHONFRAMEWORK[34m)[39;49;00m$
   424		[34m$([39;49;00mLN[34m)[39;49;00m -fsn Versions/Current/Headers [34m$([39;49;00mPYTHONFRAMEWORKDIR[34m)[39;49;00m/Headers$
   425		[34m$([39;49;00mLN[34m)[39;49;00m -fsn Versions/Current/Resources [34m$([39;49;00mPYTHONFRAMEWORKDIR[34m)[39;49;00m/Resources$
   426	$
   427	[37m# This rule builds the Cygwin Python DLL and import library if configured[39;49;00m$
   428	[37m# for a shared core library; otherwise, this rule is a noop.[39;49;00m$
   429	[32m$(DLLLIBRARY) libpython$(VERSION).dll.a[39;49;00m: [34m$([39;49;00m[31mLIBRARY_OBJS[39;49;00m[34m)[39;49;00m$
   430	[36m	if test -n "$(DLLLIBRARY)"; then \[39;49;00m$
   431	[36m		$(LDSHARED) -Wl,--out-implib=$@ -o $(DLLLIBRARY) $^ \[39;49;00m$
   432	[36m			$(LIBS) $(MODLIBS) $(SYSLIBS); \[39;49;00m$
   433	[36m	else true; \[39;49;00m$
   434	[36m	fi[39;49;00m$
   435	$
   436	$
   437	[32moldsharedmods[39;49;00m: [34m$([39;49;00m[31mSHAREDMODS[39;49;00m[34m)[39;49;00m$
   438	$
   439	$
   440	[32mMakefile Modules/config.c[39;49;00m: Makefile.pre \$
   441					[34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/config.c.in \$
   442					[34m$([39;49;00m[31mMAKESETUP[39;49;00m[34m)[39;49;00m \$
   443					Modules/Setup.config \$
   444					Modules/Setup \$
   445					Modules/Setup.local$
   446		[34m$([39;49;00mSHELL[34m)[39;49;00m [34m$([39;49;00mMAKESETUP[34m)[39;49;00m -c [34m$([39;49;00msrcdir[34m)[39;49;00m/Modules/config.c.in [33m\[39;49;00m$
   447					-s Modules [33m\[39;49;00m$
   448					Modules/Setup.config [33m\[39;49;00m$
   449					Modules/Setup.local [33m\[39;49;00m$
   450					Modules/Setup$
   451		@mv config.c Modules$
   452		@echo [33m"The Makefile was updated, you may need to re-run make."[39;49;00m$
   453	$
   454	$
   455	[32mModules/Setup[39;49;00m: [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/Setup.dist$
   456		@if [36mtest[39;49;00m -f Modules/Setup; [34mthen[39;49;00m [33m\[39;49;00m$
   457			[36mecho[39;49;00m [33m"-----------------------------------------------"[39;49;00m; [33m\[39;49;00m$
   458			[36mecho[39;49;00m [33m"Modules/Setup.dist is newer than Modules/Setup;"[39;49;00m; [33m\[39;49;00m$
   459			[36mecho[39;49;00m [33m"check to make sure you have all the updates you"[39;49;00m; [33m\[39;49;00m$
   460			[36mecho[39;49;00m [33m"need in your Modules/Setup file."[39;49;00m; [33m\[39;49;00m$
   461			[36mecho[39;49;00m [33m"Usually, copying Setup.dist to Setup will work."[39;49;00m; [33m\[39;49;00m$
   462			[36mecho[39;49;00m [33m"-----------------------------------------------"[39;49;00m; [33m\[39;49;00m$
   463		[34mfi[39;49;00m$
   464	$
   465	[37m############################################################################[39;49;00m$
   466	[37m# Special rules for object files[39;49;00m$
   467	$
   468	[32mModules/getbuildinfo.o[39;49;00m: [34m$([39;49;00m[31mPARSER_OBJS[39;49;00m[34m)[39;49;00m \$
   469			[34m$([39;49;00m[31mOBJECT_OBJS[39;49;00m[34m)[39;49;00m \$
   470			[34m$([39;49;00m[31mPYTHON_OBJS[39;49;00m[34m)[39;49;00m \$
   471			[34m$([39;49;00m[31mMODULE_OBJS[39;49;00m[34m)[39;49;00m \$
   472			[34m$([39;49;00m[31mSIGNAL_OBJS[39;49;00m[34m)[39;49;00m \$
   473			[34m$([39;49;00m[31mMODOBJS[39;49;00m[34m)[39;49;00m \$
   474			[34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/getbuildinfo.c$
   475		[34m$([39;49;00mCC[34m)[39;49;00m -c [34m$([39;49;00mPY_CFLAGS[34m)[39;49;00m -DSVNVERSION=[33m\"[39;49;00m[33m`[39;49;00m[31mLC_ALL[39;49;00m=C [34m$([39;49;00mSVNVERSION[34m)[39;49;00m[33m`[39;49;00m[33m\"[39;49;00m -o [31m$@[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/Modules/getbuildinfo.c$
   476	$
   477	[32mModules/getpath.o[39;49;00m: [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/getpath.c Makefile$
   478		[34m$([39;49;00mCC[34m)[39;49;00m -c [34m$([39;49;00mPY_CFLAGS[34m)[39;49;00m -DPYTHONPATH=[33m'"$(PYTHONPATH)"'[39;49;00m [33m\[39;49;00m$
   479			-DPREFIX=[33m'"$(prefix)"'[39;49;00m [33m\[39;49;00m$
   480			-DEXEC_PREFIX=[33m'"$(exec_prefix)"'[39;49;00m [33m\[39;49;00m$
   481			-DVERSION=[33m'"$(VERSION)"'[39;49;00m [33m\[39;49;00m$
   482			-DVPATH=[33m'"$(VPATH)"'[39;49;00m [33m\[39;49;00m$
   483			-o [31m$@[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/Modules/getpath.c$
   484	$
   485	[32mModules/python.o[39;49;00m: [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/python.c$
   486		[34m$([39;49;00mMAINCC[34m)[39;49;00m -c [34m$([39;49;00mPY_CFLAGS[34m)[39;49;00m -o [31m$@[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/Modules/python.c$
   487	$
   488	$
   489	[32m$(GRAMMAR_H) $(GRAMMAR_C)[39;49;00m: [34m$([39;49;00m[31mPGEN[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31mGRAMMAR_INPUT[39;49;00m[34m)[39;49;00m$
   490			-[34m$([39;49;00mPGEN[34m)[39;49;00m [34m$([39;49;00mGRAMMAR_INPUT[34m)[39;49;00m [34m$([39;49;00mGRAMMAR_H[34m)[39;49;00m [34m$([39;49;00mGRAMMAR_C[34m)[39;49;00m$
   491	$
   492	[32m$(PGEN)[39;49;00m:	[34m$([39;49;00m[31mPGENOBJS[39;49;00m[34m)[39;49;00m$
   493			[34m$([39;49;00mCC[34m)[39;49;00m [34m$([39;49;00mOPT[34m)[39;49;00m [34m$([39;49;00mLDFLAGS[34m)[39;49;00m [34m$([39;49;00mPGENOBJS[34m)[39;49;00m [34m$([39;49;00mLIBS[34m)[39;49;00m -o [34m$([39;49;00mPGEN[34m)[39;49;00m$
   494	$
   495	[32mParser/grammar.o[39;49;00m:	[34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Parser/grammar.c \$
   496					[34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Include/token.h \$
   497					[34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Include/grammar.h$
   498	[32mParser/metagrammar.o[39;49;00m:	[34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Parser/metagrammar.c$
   499	$
   500	[32mParser/tokenizer_pgen.o[39;49;00m:	[34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Parser/tokenizer.c$
   501	$
   502	[32mParser/pgenmain.o[39;49;00m:	[34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Include/parsetok.h$
   503	$
   504	[32m$(AST_H)[39;49;00m: [34m$([39;49;00m[31mAST_ASDL[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31mASDLGEN_FILES[39;49;00m[34m)[39;49;00m$
   505		[34m$([39;49;00mASDLGEN[34m)[39;49;00m -h [34m$([39;49;00mAST_H_DIR[34m)[39;49;00m [34m$([39;49;00mAST_ASDL[34m)[39;49;00m$
   506	$
   507	[32m$(AST_C)[39;49;00m: [34m$([39;49;00m[31mAST_ASDL[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31mASDLGEN_FILES[39;49;00m[34m)[39;49;00m$
   508		[34m$([39;49;00mASDLGEN[34m)[39;49;00m -c [34m$([39;49;00mAST_C_DIR[34m)[39;49;00m [34m$([39;49;00mAST_ASDL[34m)[39;49;00m$
   509	$
   510	[32mPython/compile.o Python/symtable.o[39;49;00m: [34m$([39;49;00m[31mGRAMMAR_H[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31mAST_H[39;49;00m[34m)[39;49;00m$
   511	$
   512	[32mPython/getplatform.o[39;49;00m: [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Python/getplatform.c$
   513			[34m$([39;49;00mCC[34m)[39;49;00m -c [34m$([39;49;00mPY_CFLAGS[34m)[39;49;00m -DPLATFORM=[33m'"$(MACHDEP)"'[39;49;00m -o [31m$@[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/Python/getplatform.c$
   514	$
   515	[32mPython/importdl.o[39;49;00m: [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Python/importdl.c$
   516			[34m$([39;49;00mCC[34m)[39;49;00m -c [34m$([39;49;00mPY_CFLAGS[34m)[39;49;00m -I[34m$([39;49;00mDLINCLDIR[34m)[39;49;00m -o [31m$@[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/Python/importdl.c$
   517	$
   518	[32mObjects/unicodectype.o[39;49;00m:	[34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Objects/unicodectype.c \$
   519					[34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Objects/unicodetype_db.h$
   520	$
   521	[37m############################################################################[39;49;00m$
   522	[37m# Header files[39;49;00m$
   523	$
   524	[31mPYTHON_HEADERS[39;49;00m= [33m\[39;49;00m$
   525			Include/Python.h [33m\[39;49;00m$
   526			Include/Python-ast.h [33m\[39;49;00m$
   527			Include/asdl.h [33m\[39;49;00m$
   528			Include/abstract.h [33m\[39;49;00m$
   529			Include/boolobject.h [33m\[39;49;00m$
   530			Include/bufferobject.h [33m\[39;49;00m$
   531			Include/ceval.h [33m\[39;49;00m$
   532			Include/classobject.h [33m\[39;49;00m$
   533			Include/cobject.h [33m\[39;49;00m$
   534			Include/code.h [33m\[39;49;00m$
   535			Include/codecs.h [33m\[39;49;00m$
   536			Include/compile.h [33m\[39;49;00m$
   537			Include/complexobject.h [33m\[39;49;00m$
   538			Include/descrobject.h [33m\[39;49;00m$
   539			Include/dictobject.h [33m\[39;49;00m$
   540			Include/enumobject.h [33m\[39;49;00m$
   541			Include/genobject.h [33m\[39;49;00m$
   542			Include/fileobject.h [33m\[39;49;00m$
   543			Include/floatobject.h [33m\[39;49;00m$
   544			Include/funcobject.h [33m\[39;49;00m$
   545			Include/import.h [33m\[39;49;00m$
   546			Include/intobject.h [33m\[39;49;00m$
   547			Include/intrcheck.h [33m\[39;49;00m$
   548			Include/iterobject.h [33m\[39;49;00m$
   549			Include/listobject.h [33m\[39;49;00m$
   550			Include/longobject.h [33m\[39;49;00m$
   551			Include/methodobject.h [33m\[39;49;00m$
   552			Include/modsupport.h [33m\[39;49;00m$
   553			Include/moduleobject.h [33m\[39;49;00m$
   554			Include/object.h [33m\[39;49;00m$
   555			Include/objimpl.h [33m\[39;49;00m$
   556			Include/parsetok.h [33m\[39;49;00m$
   557			Include/patchlevel.h [33m\[39;49;00m$
   558			Include/pyarena.h [33m\[39;49;00m$
   559			Include/pydebug.h [33m\[39;49;00m$
   560			Include/pyerrors.h [33m\[39;49;00m$
   561			Include/pyfpe.h [33m\[39;49;00m$
   562			Include/pymem.h [33m\[39;49;00m$
   563			Include/pyport.h [33m\[39;49;00m$
   564			Include/pystate.h [33m\[39;49;00m$
   565			Include/pythonrun.h [33m\[39;49;00m$
   566			Include/rangeobject.h [33m\[39;49;00m$
   567	                Include/setobject.h [33m\[39;49;00m$
   568			Include/sliceobject.h [33m\[39;49;00m$
   569			Include/stringobject.h [33m\[39;49;00m$
   570			Include/structseq.h [33m\[39;49;00m$
   571			Include/structmember.h [33m\[39;49;00m$
   572			Include/symtable.h [33m\[39;49;00m$
   573			Include/sysmodule.h [33m\[39;49;00m$
   574			Include/traceback.h [33m\[39;49;00m$
   575			Include/tupleobject.h [33m\[39;49;00m$
   576			Include/unicodeobject.h [33m\[39;49;00m$
   577			Include/weakrefobject.h [33m\[39;49;00m$
   578			pyconfig.h$
   579	$
   580	[32m$(LIBRARY_OBJS) $(MODOBJS) Modules/python.o[39;49;00m: [34m$([39;49;00m[31mPYTHON_HEADERS[39;49;00m[34m)[39;49;00m$
   581	$
   582	$
   583	[37m######################################################################[39;49;00m$
   584	$
   585	[37m# Test the interpreter (twice, once without .pyc files, once with)[39;49;00m$
   586	[37m# In the past, we've had problems where bugs in the marshalling or[39;49;00m$
   587	[37m# elsewhere caused bytecode read from .pyc files to behave differently[39;49;00m$
   588	[37m# than bytecode generated directly from a .py source file.  Sometimes[39;49;00m$
   589	[37m# the bytecode read from a .pyc file had the bug, somtimes the directly[39;49;00m$
   590	[37m# generated bytecode.  This is sometimes a very shy bug needing a lot of[39;49;00m$
   591	[37m# sample data.[39;49;00m$
   592	$
   593	[31mTESTOPTS[39;49;00m=	-l [34m$([39;49;00mEXTRATESTOPTS[34m)[39;49;00m$
   594	[31mTESTPROG[39;49;00m=	[34m$([39;49;00msrcdir[34m)[39;49;00m/Lib/test/regrtest.py$
   595	[31mTESTPYTHON[39;49;00m=	[34m$([39;49;00mRUNSHARED[34m)[39;49;00m ./[34m$([39;49;00mBUILDPYTHON[34m)[39;49;00m -E -tt$
   596	[32mtest[39;49;00m:		all platform$
   597			-find [34m$([39;49;00msrcdir[34m)[39;49;00m/Lib -name [33m'*.py[co]'[39;49;00m -print | xargs rm -f$
   598			-[34m$([39;49;00mTESTPYTHON[34m)[39;49;00m [34m$([39;49;00mTESTPROG[34m)[39;49;00m [34m$([39;49;00mTESTOPTS[34m)[39;49;00m$
   599			[34m$([39;49;00mTESTPYTHON[34m)[39;49;00m [34m$([39;49;00mTESTPROG[34m)[39;49;00m [34m$([39;49;00mTESTOPTS[34m)[39;49;00m$
   600	$
   601	[32mtestall[39;49;00m:	all platform$
   602			-find [34m$([39;49;00msrcdir[34m)[39;49;00m/Lib -name [33m'*.py[co]'[39;49;00m -print | xargs rm -f$
   603			-[34m$([39;49;00mTESTPYTHON[34m)[39;49;00m [34m$([39;49;00mTESTPROG[34m)[39;49;00m [34m$([39;49;00mTESTOPTS[34m)[39;49;00m -uall$
   604			[34m$([39;49;00mTESTPYTHON[34m)[39;49;00m [34m$([39;49;00mTESTPROG[34m)[39;49;00m [34m$([39;49;00mTESTOPTS[34m)[39;49;00m -uall$
   605	$
   606	[37m#  Run the unitests for both architectures in a Universal build on OSX[39;49;00m$
   607	[37m#  Must be run on an Intel box.[39;49;00m$
   608	[32mtestuniversal[39;49;00m:	all platform$
   609	[36m		if [ `arch` != 'i386' ];then \[39;49;00m$
   610	[36m			echo "This can only be used on OSX/i386" ;\[39;49;00m$
   611	[36m			exit 1 ;\[39;49;00m$
   612	[36m		fi[39;49;00m$
   613			-find [34m$([39;49;00msrcdir[34m)[39;49;00m/Lib -name [33m'*.py[co]'[39;49;00m -print | xargs rm -f$
   614			-[34m$([39;49;00mTESTPYTHON[34m)[39;49;00m [34m$([39;49;00mTESTPROG[34m)[39;49;00m [34m$([39;49;00mTESTOPTS[34m)[39;49;00m -uall$
   615			[34m$([39;49;00mTESTPYTHON[34m)[39;49;00m [34m$([39;49;00mTESTPROG[34m)[39;49;00m [34m$([39;49;00mTESTOPTS[34m)[39;49;00m -uall$
   616			[34m$([39;49;00mRUNSHARED[34m)[39;49;00m /usr/libexec/oah/translate ./[34m$([39;49;00mBUILDPYTHON[34m)[39;49;00m -E -tt [34m$([39;49;00mTESTPROG[34m)[39;49;00m [34m$([39;49;00mTESTOPTS[34m)[39;49;00m -uall$
   617	$
   618	$
   619	[37m# Like testall, but with a single pass only[39;49;00m$
   620	[32mbuildbottest[39;49;00m:	all platform$
   621			[34m$([39;49;00mTESTPYTHON[34m)[39;49;00m [34m$([39;49;00mTESTPROG[34m)[39;49;00m [34m$([39;49;00mTESTOPTS[34m)[39;49;00m -uall -rw$
   622	$
   623	[31mQUICKTESTOPTS[39;49;00m=	[34m$([39;49;00mTESTOPTS[34m)[39;49;00m -x test_thread test_signal test_strftime [33m\[39;49;00m$
   624			test_unicodedata test_re test_sre test_select test_poll [33m\[39;49;00m$
   625			test_linuxaudiodev test_struct test_sunaudiodev test_zlib$
   626	[32mquicktest[39;49;00m:	all platform$
   627			-find [34m$([39;49;00msrcdir[34m)[39;49;00m/Lib -name [33m'*.py[co]'[39;49;00m -print | xargs rm -f$
   628			-[34m$([39;49;00mTESTPYTHON[34m)[39;49;00m [34m$([39;49;00mTESTPROG[34m)[39;49;00m [34m$([39;49;00mQUICKTESTOPTS[34m)[39;49;00m$
   629			[34m$([39;49;00mTESTPYTHON[34m)[39;49;00m [34m$([39;49;00mTESTPROG[34m)[39;49;00m [34m$([39;49;00mQUICKTESTOPTS[34m)[39;49;00m$
   630	$
   631	[31mMEMTESTOPTS[39;49;00m=    [34m$([39;49;00mQUICKTESTOPTS[34m)[39;49;00m -x test_dl test___all__ test_fork1 [33m\[39;49;00m$
   632			test_longexp$
   633	[32mmemtest[39;49;00m:	all platform$
   634			-rm -f [34m$([39;49;00msrcdir[34m)[39;49;00m/Lib/test/*.py[co]$
   635			-[34m$([39;49;00mTESTPYTHON[34m)[39;49;00m [34m$([39;49;00mTESTPROG[34m)[39;49;00m [34m$([39;49;00mMEMTESTOPTS[34m)[39;49;00m$
   636			[34m$([39;49;00mTESTPYTHON[34m)[39;49;00m [34m$([39;49;00mTESTPROG[34m)[39;49;00m [34m$([39;49;00mMEMTESTOPTS[34m)[39;49;00m$
   637	$
   638	[37m# Install everything[39;49;00m$
   639	[32minstall[39;49;00m:	 altinstall bininstall maninstall $
   640	$
   641	[37m# Install almost everything without disturbing previous versions[39;49;00m$
   642	[32maltinstall[39;49;00m:	 altbininstall libinstall inclinstall libainstall \$
   643	                sharedinstall oldsharedinstall $
   644	$
   645	[37m# Install shared libraries enabled by Setup[39;49;00m$
   646	[31mDESTDIRS[39;49;00m=	[34m$([39;49;00mexec_prefix[34m)[39;49;00m [34m$([39;49;00mLIBDIR[34m)[39;49;00m [34m$([39;49;00mBINLIBDEST[34m)[39;49;00m [34m$([39;49;00mDESTSHARED[34m)[39;49;00m$
   647	$
   648	[32moldsharedinstall[39;49;00m: [34m$([39;49;00m[31mDESTSHARED[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31mSHAREDMODS[39;49;00m[34m)[39;49;00m$
   649			@for i [34min[39;49;00m X [34m$([39;49;00mSHAREDMODS[34m)[39;49;00m; [34mdo[39;49;00m [33m\[39;49;00m$
   650	[36m		  if test $$i != X; then \[39;49;00m$
   651	[36m		    echo $(INSTALL_SHARED) $$i $(DESTSHARED)/`basename $$i`; \[39;49;00m$
   652	[36m		    $(INSTALL_SHARED) $$i $(DESTDIR)$(DESTSHARED)/`basename $$i`; \[39;49;00m$
   653	[36m		  fi; \[39;49;00m$
   654	[36m		done[39;49;00m$
   655	$
   656	[32m$(DESTSHARED)[39;49;00m:$
   657			@for i [34min[39;49;00m [34m$([39;49;00mDESTDIRS[34m)[39;49;00m; [33m\[39;49;00m$
   658			[34mdo[39;49;00m [33m\[39;49;00m$
   659	[36m			if test ! -d $(DESTDIR)$$i; then \[39;49;00m$
   660	[36m				echo "Creating directory $$i"; \[39;49;00m$
   661	[36m				$(INSTALL) -d -m $(DIRMODE) $(DESTDIR)$$i; \[39;49;00m$
   662	[36m			else    true; \[39;49;00m$
   663	[36m			fi; \[39;49;00m$
   664	[36m		done[39;49;00m$
   665	$
   666	$
   667	[37m# Install the interpreter (by creating a hard link to python$(VERSION))[39;49;00m$
   668	[32mbininstall[39;49;00m:	altbininstall$
   669		-if [36mtest[39;49;00m -f [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mBINDIR[34m)[39;49;00m/[34m$([39;49;00mPYTHON[34m)[39;49;00m -o -h [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mBINDIR[34m)[39;49;00m/[34m$([39;49;00mPYTHON[34m)[39;49;00m; [33m\[39;49;00m$
   670		[34mthen[39;49;00m rm -f [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mBINDIR[34m)[39;49;00m/[34m$([39;49;00mPYTHON[34m)[39;49;00m; [33m\[39;49;00m$
   671	[36m	else true; \[39;49;00m$
   672	[36m	fi[39;49;00m$
   673		([36mcd[39;49;00m [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mBINDIR[34m)[39;49;00m; [34m$([39;49;00mLN[34m)[39;49;00m python[34m$([39;49;00mVERSION[34m)[39;49;00m[34m$([39;49;00mEXE[34m)[39;49;00m [34m$([39;49;00mPYTHON[34m)[39;49;00m)$
   674		([36mcd[39;49;00m [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mBINDIR[34m)[39;49;00m; [34m$([39;49;00mLN[34m)[39;49;00m -sf python[34m$([39;49;00mVERSION[34m)[39;49;00m-config python-config)$
   675	$
   676	[37m# Install the interpreter with $(VERSION) affixed[39;49;00m$
   677	[37m# This goes into $(exec_prefix)[39;49;00m$
   678	[32maltbininstall[39;49;00m:	[34m$([39;49;00m[31mBUILDPYTHON[39;49;00m[34m)[39;49;00m$
   679		@for i [34min[39;49;00m [34m$([39;49;00mBINDIR[34m)[39;49;00m [34m$([39;49;00mLIBDIR[34m)[39;49;00m; [33m\[39;49;00m$
   680		[34mdo[39;49;00m [33m\[39;49;00m$
   681	[36m		if test ! -d $(DESTDIR)$$i; then \[39;49;00m$
   682	[36m			echo "Creating directory $$i"; \[39;49;00m$
   683	[36m			$(INSTALL) -d -m $(DIRMODE) $(DESTDIR)$$i; \[39;49;00m$
   684	[36m		else	true; \[39;49;00m$
   685	[36m		fi; \[39;49;00m$
   686	[36m	done[39;49;00m$
   687		[34m$([39;49;00mINSTALL_PROGRAM[34m)[39;49;00m [34m$([39;49;00mBUILDPYTHON[34m)[39;49;00m [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mBINDIR[34m)[39;49;00m/python[34m$([39;49;00mVERSION[34m)[39;49;00m[34m$([39;49;00mEXE[34m)[39;49;00m$
   688	[36m	if test -f libpython$(VERSION)$(SO); then \[39;49;00m$
   689	[36m		if test "$(SO)" = .dll; then \[39;49;00m$
   690	[36m			$(INSTALL_SHARED) libpython$(VERSION)$(SO) $(DESTDIR)$(BINDIR); \[39;49;00m$
   691	[36m		else \[39;49;00m$
   692	[36m			$(INSTALL_SHARED) libpython$(VERSION)$(SO) $(DESTDIR)$(LIBDIR)/$(INSTSONAME); \[39;49;00m$
   693	[36m			if test libpython$(VERSION)$(SO) != $(INSTSONAME); then \[39;49;00m$
   694	[36m				(cd $(DESTDIR)$(LIBDIR); $(LN) -sf $(INSTSONAME) libpython$(VERSION)$(SO)); \[39;49;00m$
   695	[36m			fi \[39;49;00m$
   696	[36m		fi; \[39;49;00m$
   697	[36m	else	true; \[39;49;00m$
   698	[36m	fi[39;49;00m$
   699	$
   700	[37m# Install the manual page[39;49;00m$
   701	[32mmaninstall[39;49;00m:$
   702		@for i [34min[39;49;00m [34m$([39;49;00mMANDIR[34m)[39;49;00m [34m$([39;49;00mMANDIR[34m)[39;49;00m/man1; [33m\[39;49;00m$
   703		[34mdo[39;49;00m [33m\[39;49;00m$
   704	[36m		if test ! -d $(DESTDIR)$$i; then \[39;49;00m$
   705	[36m			echo "Creating directory $$i"; \[39;49;00m$
   706	[36m			$(INSTALL) -d -m $(DIRMODE) $(DESTDIR)$$i; \[39;49;00m$
   707	[36m		else	true; \[39;49;00m$
   708	[36m		fi; \[39;49;00m$
   709	[36m	done[39;49;00m$
   710		[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/Misc/python.man [33m\[39;49;00m$
   711			[34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mMANDIR[34m)[39;49;00m/man1/python.1$
   712	$
   713	[37m# Install the library[39;49;00m$
   714	[31mPLATDIR[39;49;00m=	plat-[34m$([39;49;00mMACHDEP[34m)[39;49;00m$
   715	[31mEXTRAPLATDIR[39;49;00m= $
   716	[31mEXTRAMACHDEPPATH[39;49;00m=$
   717	[31mMACHDEPS[39;49;00m=	[34m$([39;49;00mPLATDIR[34m)[39;49;00m [34m$([39;49;00mEXTRAPLATDIR[34m)[39;49;00m$
   718	[31mXMLLIBSUBDIRS[39;49;00m=  xml xml/dom xml/etree xml/parsers xml/sax$
   719	[31mPLATMACDIRS[39;49;00m= plat-mac plat-mac/Carbon plat-mac/lib-scriptpackages [33m\[39;49;00m$
   720		plat-mac/lib-scriptpackages/_builtinSuites [33m\[39;49;00m$
   721		plat-mac/lib-scriptpackages/CodeWarrior [33m\[39;49;00m$
   722		plat-mac/lib-scriptpackages/Explorer [33m\[39;49;00m$
   723		plat-mac/lib-scriptpackages/Finder [33m\[39;49;00m$
   724		plat-mac/lib-scriptpackages/Netscape [33m\[39;49;00m$
   725		plat-mac/lib-scriptpackages/StdSuites [33m\[39;49;00m$
   726		plat-mac/lib-scriptpackages/SystemEvents [33m\[39;49;00m$
   727		plat-mac/lib-scriptpackages/Terminal $
   728	[31mPLATMACPATH[39;49;00m=:plat-mac:plat-mac/lib-scriptpackages$
   729	[31mLIBSUBDIRS[39;49;00m=	lib-tk site-packages [36mtest[39;49;00m test/output test/data [33m\[39;49;00m$
   730			test/decimaltestdata [33m\[39;49;00m$
   731			encodings compiler hotshot [33m\[39;49;00m$
   732			email email/mime email/test email/test/data [33m\[39;49;00m$
   733			sqlite3 sqlite3/test [33m\[39;49;00m$
   734			logging bsddb bsddb/test csv wsgiref [33m\[39;49;00m$
   735			ctypes ctypes/test ctypes/macholib idlelib idlelib/Icons [33m\[39;49;00m$
   736			distutils distutils/command distutils/tests [34m$([39;49;00mXMLLIBSUBDIRS[34m)[39;49;00m [33m\[39;49;00m$
   737			setuptools setuptools/command setuptools/tests setuptools.egg-info [33m\[39;49;00m$
   738			curses [34m$([39;49;00mMACHDEPS[34m)[39;49;00m$
   739	[32mlibinstall[39;49;00m:	[34m$([39;49;00m[31mBUILDPYTHON[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Lib/[34m$([39;49;00m[31mPLATDIR[39;49;00m[34m)[39;49;00m$
   740		@for i [34min[39;49;00m [34m$([39;49;00mSCRIPTDIR[34m)[39;49;00m [34m$([39;49;00mLIBDEST[34m)[39;49;00m; [33m\[39;49;00m$
   741		[34mdo[39;49;00m [33m\[39;49;00m$
   742	[36m		if test ! -d $(DESTDIR)$$i; then \[39;49;00m$
   743	[36m			echo "Creating directory $$i"; \[39;49;00m$
   744	[36m			$(INSTALL) -d -m $(DIRMODE) $(DESTDIR)$$i; \[39;49;00m$
   745	[36m		else	true; \[39;49;00m$
   746	[36m		fi; \[39;49;00m$
   747	[36m	done[39;49;00m$
   748		@for d [34min[39;49;00m [34m$([39;49;00mLIBSUBDIRS[34m)[39;49;00m; [33m\[39;49;00m$
   749		[34mdo[39;49;00m [33m\[39;49;00m$
   750			[31ma[39;49;00m=[34m$([39;49;00msrcdir[34m)[39;49;00m/Lib/[31m$$[39;49;00md; [33m\[39;49;00m$
   751	[36m		if test ! -d $$a; then continue; else true; fi; \[39;49;00m$
   752	[36m		b=$(LIBDEST)/$$d; \[39;49;00m$
   753	[36m		if test ! -d $(DESTDIR)$$b; then \[39;49;00m$
   754	[36m			echo "Creating directory $$b"; \[39;49;00m$
   755	[36m			$(INSTALL) -d -m $(DIRMODE) $(DESTDIR)$$b; \[39;49;00m$
   756	[36m		else	true; \[39;49;00m$
   757	[36m		fi; \[39;49;00m$
   758	[36m	done[39;49;00m$
   759		@for i [34min[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/Lib/*.py [34m$([39;49;00msrcdir[34m)[39;49;00m/Lib/*.doc [34m$([39;49;00msrcdir[34m)[39;49;00m/Lib/*.egg-info ; [33m\[39;49;00m$
   760		[34mdo[39;49;00m [33m\[39;49;00m$
   761	[36m		if test -x $$i; then \[39;49;00m$
   762	[36m			$(INSTALL_SCRIPT) $$i $(DESTDIR)$(LIBDEST); \[39;49;00m$
   763	[36m			echo $(INSTALL_SCRIPT) $$i $(LIBDEST); \[39;49;00m$
   764	[36m		else \[39;49;00m$
   765	[36m			$(INSTALL_DATA) $$i $(DESTDIR)$(LIBDEST); \[39;49;00m$
   766	[36m			echo $(INSTALL_DATA) $$i $(LIBDEST); \[39;49;00m$
   767	[36m		fi; \[39;49;00m$
   768	[36m	done[39;49;00m$
   769		@for d [34min[39;49;00m [34m$([39;49;00mLIBSUBDIRS[34m)[39;49;00m; [33m\[39;49;00m$
   770		[34mdo[39;49;00m [33m\[39;49;00m$
   771			[31ma[39;49;00m=[34m$([39;49;00msrcdir[34m)[39;49;00m/Lib/[31m$$[39;49;00md; [33m\[39;49;00m$
   772	[36m		if test ! -d $$a; then continue; else true; fi; \[39;49;00m$
   773	[36m		if test `ls $$a | wc -l` -lt 1; then continue; fi; \[39;49;00m$
   774	[36m		b=$(LIBDEST)/$$d; \[39;49;00m$
   775	[36m		for i in $$a/*; \[39;49;00m$
   776	[36m		do \[39;49;00m$
   777	[36m			case $$i in \[39;49;00m$
   778	[36m			*CVS) ;; \[39;49;00m$
   779	[36m			*.py[co]) ;; \[39;49;00m$
   780	[36m			*.orig) ;; \[39;49;00m$
   781	[36m			*~) ;; \[39;49;00m$
   782	[36m			*) \[39;49;00m$
   783	[36m				if test -d $$i; then continue; fi; \[39;49;00m$
   784	[36m				if test -x $$i; then \[39;49;00m$
   785	[36m				    echo $(INSTALL_SCRIPT) $$i $$b; \[39;49;00m$
   786	[36m				    $(INSTALL_SCRIPT) $$i $(DESTDIR)$$b; \[39;49;00m$
   787	[36m				else \[39;49;00m$
   788	[36m				    echo $(INSTALL_DATA) $$i $$b; \[39;49;00m$
   789	[36m				    $(INSTALL_DATA) $$i $(DESTDIR)$$b; \[39;49;00m$
   790	[36m				fi;; \[39;49;00m$
   791	[36m			esac; \[39;49;00m$
   792	[36m		done; \[39;49;00m$
   793	[36m	done[39;49;00m$
   794		[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/LICENSE [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBDEST[34m)[39;49;00m/LICENSE.txt$
   795		[31mPYTHONPATH[39;49;00m=[34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBDEST[34m)[39;49;00m  [34m$([39;49;00mRUNSHARED[34m)[39;49;00m [33m\[39;49;00m$
   796			./[34m$([39;49;00mBUILDPYTHON[34m)[39;49;00m -Wi -tt [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBDEST[34m)[39;49;00m/compileall.py [33m\[39;49;00m$
   797			-d [34m$([39;49;00mLIBDEST[34m)[39;49;00m -f [33m\[39;49;00m$
   798			-x [33m'bad_coding|badsyntax|site-packages'[39;49;00m [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBDEST[34m)[39;49;00m$
   799		[31mPYTHONPATH[39;49;00m=[34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBDEST[34m)[39;49;00m [34m$([39;49;00mRUNSHARED[34m)[39;49;00m [33m\[39;49;00m$
   800			./[34m$([39;49;00mBUILDPYTHON[34m)[39;49;00m -Wi -tt -O [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBDEST[34m)[39;49;00m/compileall.py [33m\[39;49;00m$
   801			-d [34m$([39;49;00mLIBDEST[34m)[39;49;00m -f [33m\[39;49;00m$
   802			-x [33m'bad_coding|badsyntax|site-packages'[39;49;00m [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBDEST[34m)[39;49;00m$
   803		-PYTHONPATH=[34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBDEST[34m)[39;49;00m  [34m$([39;49;00mRUNSHARED[34m)[39;49;00m [33m\[39;49;00m$
   804			./[34m$([39;49;00mBUILDPYTHON[34m)[39;49;00m -Wi -t [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBDEST[34m)[39;49;00m/compileall.py [33m\[39;49;00m$
   805			-d [34m$([39;49;00mLIBDEST[34m)[39;49;00m/site-packages -f [33m\[39;49;00m$
   806			-x badsyntax [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBDEST[34m)[39;49;00m/site-packages$
   807		-PYTHONPATH=[34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBDEST[34m)[39;49;00m [34m$([39;49;00mRUNSHARED[34m)[39;49;00m [33m\[39;49;00m$
   808			./[34m$([39;49;00mBUILDPYTHON[34m)[39;49;00m -Wi -t -O [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBDEST[34m)[39;49;00m/compileall.py [33m\[39;49;00m$
   809			-d [34m$([39;49;00mLIBDEST[34m)[39;49;00m/site-packages -f [33m\[39;49;00m$
   810			-x badsyntax [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBDEST[34m)[39;49;00m/site-packages$
   811	$
   812	[37m# Create the PLATDIR source directory, if one wasn't distributed..[39;49;00m$
   813	[32m$(srcdir)/Lib/$(PLATDIR)[39;49;00m:$
   814		mkdir [34m$([39;49;00msrcdir[34m)[39;49;00m/Lib/[34m$([39;49;00mPLATDIR[34m)[39;49;00m$
   815		cp [34m$([39;49;00msrcdir[34m)[39;49;00m/Lib/plat-generic/regen [34m$([39;49;00msrcdir[34m)[39;49;00m/Lib/[34m$([39;49;00mPLATDIR[34m)[39;49;00m/regen$
   816		[36mexport[39;49;00m PATH; [31mPATH[39;49;00m=[33m"[39;49;00m[33m`pwd`:[39;49;00m[31m$$[39;49;00m[33mPATH[39;49;00m[33m"[39;49;00m; [33m\[39;49;00m$
   817		[36mexport[39;49;00m PYTHONPATH; [31mPYTHONPATH[39;49;00m=[33m"`pwd`/Lib"[39;49;00m; [33m\[39;49;00m$
   818		[36mexport[39;49;00m DYLD_FRAMEWORK_PATH; [31mDYLD_FRAMEWORK_PATH[39;49;00m=[33m"`pwd`"[39;49;00m; [33m\[39;49;00m$
   819		[36mexport[39;49;00m EXE; [31mEXE[39;49;00m=[33m"[39;49;00m[34m$([39;49;00mBUILDEXE[34m)[39;49;00m[33m"[39;49;00m; [33m\[39;49;00m$
   820		[36mcd[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/Lib/[34m$([39;49;00mPLATDIR[34m)[39;49;00m; ./regen$
   821	$
   822	[37m# Install the include files[39;49;00m$
   823	[31mINCLDIRSTOMAKE[39;49;00m=[34m$([39;49;00mINCLUDEDIR[34m)[39;49;00m [34m$([39;49;00mCONFINCLUDEDIR[34m)[39;49;00m [34m$([39;49;00mINCLUDEPY[34m)[39;49;00m [34m$([39;49;00mCONFINCLUDEPY[34m)[39;49;00m$
   824	[32minclinstall[39;49;00m:$
   825		@for i [34min[39;49;00m [34m$([39;49;00mINCLDIRSTOMAKE[34m)[39;49;00m; [33m\[39;49;00m$
   826		[34mdo[39;49;00m [33m\[39;49;00m$
   827	[36m		if test ! -d $(DESTDIR)$$i; then \[39;49;00m$
   828	[36m			echo "Creating directory $$i"; \[39;49;00m$
   829	[36m			$(INSTALL) -d -m $(DIRMODE) $(DESTDIR)$$i; \[39;49;00m$
   830	[36m		else	true; \[39;49;00m$
   831	[36m		fi; \[39;49;00m$
   832	[36m	done[39;49;00m$
   833		@for i [34min[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/Include/*.h; [33m\[39;49;00m$
   834		[34mdo[39;49;00m [33m\[39;49;00m$
   835			[36mecho[39;49;00m [34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m [31m$$[39;49;00mi [34m$([39;49;00mINCLUDEPY[34m)[39;49;00m; [33m\[39;49;00m$
   836			[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m [31m$$[39;49;00mi [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mINCLUDEPY[34m)[39;49;00m; [33m\[39;49;00m$
   837		[34mdone[39;49;00m$
   838		[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m pyconfig.h [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mCONFINCLUDEPY[34m)[39;49;00m/pyconfig.h$
   839	$
   840	[37m# Install the library and miscellaneous stuff needed for extending/embedding[39;49;00m$
   841	[37m# This goes into $(exec_prefix)[39;49;00m$
   842	[31mLIBPL[39;49;00m=		[34m$([39;49;00mLIBP[34m)[39;49;00m/config$
   843	[32mlibainstall[39;49;00m:	all$
   844		@for i [34min[39;49;00m [34m$([39;49;00mLIBDIR[34m)[39;49;00m [34m$([39;49;00mLIBP[34m)[39;49;00m [34m$([39;49;00mLIBPL[34m)[39;49;00m; [33m\[39;49;00m$
   845		[34mdo[39;49;00m [33m\[39;49;00m$
   846	[36m		if test ! -d $(DESTDIR)$$i; then \[39;49;00m$
   847	[36m			echo "Creating directory $$i"; \[39;49;00m$
   848	[36m			$(INSTALL) -d -m $(DIRMODE) $(DESTDIR)$$i; \[39;49;00m$
   849	[36m		else	true; \[39;49;00m$
   850	[36m		fi; \[39;49;00m$
   851	[36m	done[39;49;00m$
   852		@if [36mtest[39;49;00m -d [34m$([39;49;00mLIBRARY[34m)[39;49;00m; [34mthen[39;49;00m :; [34melse[39;49;00m [33m\[39;49;00m$
   853	[36m		if test "$(PYTHONFRAMEWORKDIR)" = no-framework; then \[39;49;00m$
   854	[36m			if test "$(SO)" = .dll; then \[39;49;00m$
   855	[36m				$(INSTALL_DATA) $(LDLIBRARY) $(DESTDIR)$(LIBPL) ; \[39;49;00m$
   856	[36m			else \[39;49;00m$
   857	[36m				$(INSTALL_DATA) $(LIBRARY) $(DESTDIR)$(LIBPL)/$(LIBRARY) ; \[39;49;00m$
   858	[36m				$(RANLIB) $(DESTDIR)$(LIBPL)/$(LIBRARY) ; \[39;49;00m$
   859	[36m			fi; \[39;49;00m$
   860	[36m		else \[39;49;00m$
   861	[36m			echo Skip install of $(LIBRARY) - use make frameworkinstall; \[39;49;00m$
   862	[36m		fi; \[39;49;00m$
   863	[36m	fi[39;49;00m$
   864		[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m Modules/config.c [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m/config.c$
   865		[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m Modules/python.o [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m/python.o$
   866		[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/Modules/config.c.in [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m/config.c.in$
   867		[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m Makefile [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m/Makefile$
   868		[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m Modules/Setup [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m/Setup$
   869		[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m Modules/Setup.local [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m/Setup.local$
   870		[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m Modules/Setup.config [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m/Setup.config$
   871		[34m$([39;49;00mINSTALL_SCRIPT[34m)[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/Modules/makesetup [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m/makesetup$
   872		[34m$([39;49;00mINSTALL_SCRIPT[34m)[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/install-sh [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m/install-sh$
   873	[37m	# Substitution happens here, as the completely-expanded BINDIR[39;49;00m$
   874	[37m	# is not available in configure[39;49;00m$
   875		sed -e [33m"[39;49;00m[33ms,@EXENAME@,[39;49;00m[34m$([39;49;00mBINDIR[34m)[39;49;00m[33m/python[39;49;00m[34m$([39;49;00mVERSION[34m)[39;49;00m[34m$([39;49;00mEXE[34m)[39;49;00m[33m,[39;49;00m[33m"[39;49;00m < [34m$([39;49;00msrcdir[34m)[39;49;00m/Misc/python-config.in >python-config$
   876		[34m$([39;49;00mINSTALL_SCRIPT[34m)[39;49;00m python-config [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mBINDIR[34m)[39;49;00m/python[34m$([39;49;00mVERSION[34m)[39;49;00m-config$
   877		rm python-config$
   878		@if [ -s Modules/python.exp -a [33m\[39;49;00m$
   879			[33m"[39;49;00m[33m`echo [39;49;00m[34m$([39;49;00mMACHDEP[34m)[39;49;00m[33m | sed 's/^\(...\).*/\1/'`[39;49;00m[33m"[39;49;00m = [33m"aix"[39;49;00m ]; [34mthen[39;49;00m [33m\[39;49;00m$
   880			echo; [36mecho[39;49;00m [33m"Installing support files for building shared extension modules on AIX:"[39;49;00m; [33m\[39;49;00m$
   881			[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m Modules/python.exp		[33m\[39;49;00m$
   882					[34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m/python.exp;		[33m\[39;49;00m$
   883			echo; [36mecho[39;49;00m [33m"[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m[33m/python.exp[39;49;00m[33m"[39;49;00m;		[33m\[39;49;00m$
   884			[34m$([39;49;00mINSTALL_SCRIPT[34m)[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/Modules/makexp_aix	[33m\[39;49;00m$
   885					[34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m/makexp_aix;		[33m\[39;49;00m$
   886			[36mecho[39;49;00m [33m"[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m[33m/makexp_aix[39;49;00m[33m"[39;49;00m;			[33m\[39;49;00m$
   887			[34m$([39;49;00mINSTALL_SCRIPT[34m)[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/Modules/ld_so_aix	[33m\[39;49;00m$
   888					[34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m/ld_so_aix;		[33m\[39;49;00m$
   889			[36mecho[39;49;00m [33m"[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m[33m/ld_so_aix[39;49;00m[33m"[39;49;00m;			[33m\[39;49;00m$
   890			echo; [36mecho[39;49;00m [33m"See Misc/AIX-NOTES for details."[39;49;00m;	[33m\[39;49;00m$
   891	[36m	else true; \[39;49;00m$
   892	[36m	fi[39;49;00m$
   893		@case [33m"[39;49;00m[34m$([39;49;00mMACHDEP[34m)[39;49;00m[33m"[39;49;00m [34min[39;49;00m beos*) [33m\[39;49;00m$
   894			echo; [36mecho[39;49;00m [33m"Installing support files for building shared extension modules on BeOS:"[39;49;00m; [33m\[39;49;00m$
   895			[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m Misc/BeOS-NOTES [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m/README;	[33m\[39;49;00m$
   896			echo; [36mecho[39;49;00m [33m"[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m[33m/README[39;49;00m[33m"[39;49;00m;			[33m\[39;49;00m$
   897			[34m$([39;49;00mINSTALL_SCRIPT[34m)[39;49;00m Modules/ar_beos [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m/ar_beos; [33m\[39;49;00m$
   898			[36mecho[39;49;00m [33m"[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m[33m/ar_beos[39;49;00m[33m"[39;49;00m;			[33m\[39;49;00m$
   899			[34m$([39;49;00mINSTALL_SCRIPT[34m)[39;49;00m Modules/ld_so_beos [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m/ld_so_beos; [33m\[39;49;00m$
   900			[36mecho[39;49;00m [33m"[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m[33m/ld_so_beos[39;49;00m[33m"[39;49;00m;			[33m\[39;49;00m$
   901			echo; [36mecho[39;49;00m [33m"See Misc/BeOS-NOTES for details."[39;49;00m;	[33m\[39;49;00m$
   902			;; [33m\[39;49;00m$
   903		[34mesac[39;49;00m$
   904	$
   905	[37m# Install the dynamically loadable modules[39;49;00m$
   906	[37m# This goes into $(exec_prefix)[39;49;00m$
   907	[32msharedinstall[39;49;00m:$
   908		[34m$([39;49;00mRUNSHARED[34m)[39;49;00m ./[34m$([39;49;00mBUILDPYTHON[34m)[39;49;00m -E [34m$([39;49;00msrcdir[34m)[39;49;00m/setup.py install [33m\[39;49;00m$
   909		   	--prefix=[34m$([39;49;00mprefix[34m)[39;49;00m [33m\[39;49;00m$
   910			--install-scripts=[34m$([39;49;00mBINDIR[34m)[39;49;00m [33m\[39;49;00m$
   911			--install-platlib=[34m$([39;49;00mDESTSHARED[34m)[39;49;00m [33m\[39;49;00m$
   912			--root=/[34m$([39;49;00mDESTDIR[34m)[39;49;00m$
   913	$
   914	[37m# Here are a couple of targets for MacOSX again, to install a full[39;49;00m$
   915	[37m# framework-based Python. frameworkinstall installs everything, the[39;49;00m$
   916	[37m# subtargets install specific parts. Much of the actual work is offloaded to[39;49;00m$
   917	[37m# the Makefile in Mac[39;49;00m$
   918	[37m#[39;49;00m$
   919	[37m#[39;49;00m$
   920	[37m# This target is here for backward compatiblity, previous versions of Python[39;49;00m$
   921	[37m# hadn't integrated framework installation in the normal install process.[39;49;00m$
   922	[32mframeworkinstall[39;49;00m: install$
   923	$
   924	[37m# On install, we re-make the framework[39;49;00m$
   925	[37m# structure in the install location, /Library/Frameworks/ or the argument to[39;49;00m$
   926	[37m# --enable-framework. If --enable-framework has been specified then we have[39;49;00m$
   927	[37m# automatically set prefix to the location deep down in the framework, so we[39;49;00m$
   928	[37m# only have to cater for the structural bits of the framework.[39;49;00m$
   929	$
   930	[32mframeworkinstallframework[39;49;00m: frameworkinstallstructure install frameworkinstallmaclib$
   931	$
   932	[32mframeworkinstallstructure[39;49;00m:	[34m$([39;49;00m[31mLDLIBRARY[39;49;00m[34m)[39;49;00m$
   933		@if [36mtest[39;49;00m [33m"[39;49;00m[34m$([39;49;00mPYTHONFRAMEWORKDIR[34m)[39;49;00m[33m"[39;49;00m = no-framework; [34mthen[39;49;00m [33m\[39;49;00m$
   934			[36mecho[39;49;00m Not configured with --enable-framework; [33m\[39;49;00m$
   935			[36mexit[39;49;00m [34m1[39;49;00m; [33m\[39;49;00m$
   936	[36m	else true; \[39;49;00m$
   937	[36m	fi[39;49;00m$
   938		@for i [34min[39;49;00m [34m$([39;49;00mprefix[34m)[39;49;00m/Resources/English.lproj [34m$([39;49;00mprefix[34m)[39;49;00m/lib; [34mdo[39;49;00m[33m\[39;49;00m$
   939	[36m		if test ! -d $(DESTDIR)$$i; then \[39;49;00m$
   940	[36m			echo "Creating directory $(DESTDIR)$$i"; \[39;49;00m$
   941	[36m			$(INSTALL) -d -m $(DIRMODE) $(DESTDIR)$$i; \[39;49;00m$
   942	[36m		else	true; \[39;49;00m$
   943	[36m		fi; \[39;49;00m$
   944	[36m	done[39;49;00m$
   945		[34m$([39;49;00mLN[34m)[39;49;00m -fsn include/python[34m$([39;49;00mVERSION[34m)[39;49;00m [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mprefix[34m)[39;49;00m/Headers$
   946		[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m [34m$([39;49;00mRESSRCDIR[34m)[39;49;00m/Info.plist [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mprefix[34m)[39;49;00m/Resources/Info.plist$
   947		[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m [34m$([39;49;00mRESSRCDIR[34m)[39;49;00m/version.plist [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mprefix[34m)[39;49;00m/Resources/version.plist$
   948		[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m [34m$([39;49;00mRESSRCDIR[34m)[39;49;00m/English.lproj/InfoPlist.strings [33m\[39;49;00m$
   949			[34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mprefix[34m)[39;49;00m/Resources/English.lproj/InfoPlist.strings$
   950		[34m$([39;49;00mLN[34m)[39;49;00m -fsn [34m$([39;49;00mVERSION[34m)[39;49;00m [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mPYTHONFRAMEWORKINSTALLDIR[34m)[39;49;00m/Versions/Current$
   951		[34m$([39;49;00mLN[34m)[39;49;00m -fsn Versions/Current/Python [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mPYTHONFRAMEWORKINSTALLDIR[34m)[39;49;00m/Python$
   952		[34m$([39;49;00mLN[34m)[39;49;00m -fsn Versions/Current/Headers [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mPYTHONFRAMEWORKINSTALLDIR[34m)[39;49;00m/Headers$
   953		[34m$([39;49;00mLN[34m)[39;49;00m -fsn Versions/Current/Resources [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mPYTHONFRAMEWORKINSTALLDIR[34m)[39;49;00m/Resources$
   954		[34m$([39;49;00mINSTALL_SHARED[34m)[39;49;00m [34m$([39;49;00mLDLIBRARY[34m)[39;49;00m [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mPYTHONFRAMEWORKPREFIX[34m)[39;49;00m/[34m$([39;49;00mLDLIBRARY[34m)[39;49;00m$
   955	$
   956	[37m# This installs Mac/Lib into the framework[39;49;00m$
   957	[37m# Install a number of symlinks to keep software that expects a normal unix[39;49;00m$
   958	[37m# install (which includes python-config) happy.[39;49;00m$
   959	[32mframeworkinstallmaclib[39;49;00m:$
   960		ln -fs [33m"../../../Python"[39;49;00m [33m"[39;49;00m[34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mprefix[34m)[39;49;00m[33m/lib/python[39;49;00m[34m$([39;49;00mVERSION[34m)[39;49;00m[33m/config/libpython[39;49;00m[34m$([39;49;00mVERSION[34m)[39;49;00m[33m.a[39;49;00m[33m"[39;49;00m$
   961		[36mcd[39;49;00m Mac && [34m$([39;49;00mMAKE[34m)[39;49;00m installmacsubtree [31mDESTDIR[39;49;00m=[33m"[39;49;00m[34m$([39;49;00mDESTDIR[34m)[39;49;00m[33m"[39;49;00m$
   962	$
   963	[37m# This installs the IDE, the Launcher and other apps into /Applications[39;49;00m$
   964	[32mframeworkinstallapps[39;49;00m:$
   965		[36mcd[39;49;00m Mac && [34m$([39;49;00mMAKE[34m)[39;49;00m installapps [31mDESTDIR[39;49;00m=[33m"[39;49;00m[34m$([39;49;00mDESTDIR[34m)[39;49;00m[33m"[39;49;00m$
   966	$
   967	[37m# This install the unix python and pythonw tools in /usr/local/bin[39;49;00m$
   968	[32mframeworkinstallunixtools[39;49;00m:$
   969		[36mcd[39;49;00m Mac && [34m$([39;49;00mMAKE[34m)[39;49;00m installunixtools [31mDESTDIR[39;49;00m=[33m"[39;49;00m[34m$([39;49;00mDESTDIR[34m)[39;49;00m[33m"[39;49;00m$
   970	$
   971	[32mframeworkaltinstallunixtools[39;49;00m:$
   972		[36mcd[39;49;00m Mac && [34m$([39;49;00mMAKE[34m)[39;49;00m altinstallunixtools [31mDESTDIR[39;49;00m=[33m"[39;49;00m[34m$([39;49;00mDESTDIR[34m)[39;49;00m[33m"[39;49;00m$
   973	$
   974	[37m# This installs the Demos and Tools into the applications directory.[39;49;00m$
   975	[37m# It is not part of a normal frameworkinstall[39;49;00m$
   976	[32mframeworkinstallextras[39;49;00m:$
   977		[36mcd[39;49;00m Mac && Make installextras [31mDESTDIR[39;49;00m=[33m"[39;49;00m[34m$([39;49;00mDESTDIR[34m)[39;49;00m[33m"[39;49;00m$
   978	$
   979	[37m# This installs a few of the useful scripts in Tools/scripts[39;49;00m$
   980	[32mscriptsinstall[39;49;00m:$
   981		[31mSRCDIR[39;49;00m=[34m$([39;49;00msrcdir[34m)[39;49;00m [34m$([39;49;00mRUNSHARED[34m)[39;49;00m [33m\[39;49;00m$
   982		./[34m$([39;49;00mBUILDPYTHON[34m)[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/Tools/scripts/setup.py install [33m\[39;49;00m$
   983		--prefix=[34m$([39;49;00mprefix[34m)[39;49;00m [33m\[39;49;00m$
   984		--install-scripts=[34m$([39;49;00mBINDIR[34m)[39;49;00m [33m\[39;49;00m$
   985		--root=/[34m$([39;49;00mDESTDIR[34m)[39;49;00m$
   986	$
   987	[37m# Build the toplevel Makefile[39;49;00m$
   988	[32mMakefile.pre[39;49;00m: Makefile.pre.in config.status$
   989		[31mCONFIG_FILES[39;49;00m=Makefile.pre [31mCONFIG_HEADERS[39;49;00m= [34m$([39;49;00mSHELL[34m)[39;49;00m config.status$
   990		[34m$([39;49;00mMAKE[34m)[39;49;00m -f Makefile.pre Makefile$
   991	$
   992	[37m# Run the configure script.[39;49;00m$
   993	[32mconfig.status[39;49;00m:	[34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/configure$
   994		[34m$([39;49;00mSHELL[34m)[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/configure [34m$([39;49;00mCONFIG_ARGS[34m)[39;49;00m$
   995	$
   996	[32m.PRECIOUS[39;49;00m: config.status [34m$([39;49;00m[31mBUILDPYTHON[39;49;00m[34m)[39;49;00m Makefile Makefile.pre$
   997	$
   998	[37m# Some make's put the object file in the current directory[39;49;00m$
   999	[32m.c.o[39;49;00m:$
  1000		[34m$([39;49;00mCC[34m)[39;49;00m -c [34m$([39;49;00mPY_CFLAGS[34m)[39;49;00m -o [31m$@[39;49;00m $<$
  1001	$
  1002	[37m# Run reindent on the library[39;49;00m$
  1003	[32mreindent[39;49;00m:$
  1004		./python[34m$([39;49;00mEXEEXT[34m)[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/Tools/scripts/reindent.py -r [34m$([39;49;00msrcdir[34m)[39;49;00m/Lib$
  1005	$
  1006	[37m# Rerun configure with the same options as it was run last time,[39;49;00m$
  1007	[37m# provided the config.status script exists[39;49;00m$
  1008	[32mrecheck[39;49;00m:$
  1009		[34m$([39;49;00mSHELL[34m)[39;49;00m config.status --recheck$
  1010		[34m$([39;49;00mSHELL[34m)[39;49;00m config.status$
  1011	$
  1012	[37m# Rebuild the configure script from configure.in; also rebuild pyconfig.h.in[39;49;00m$
  1013	[32mautoconf[39;49;00m:$
  1014		([36mcd[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m; autoconf)$
  1015		([36mcd[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m; autoheader)$
  1016	$
  1017	[37m# Create a tags file for vi[39;49;00m$
  1018	[32mtags[39;49;00m::$
  1019		[36mcd[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m; [33m\[39;49;00m$
  1020		ctags -w -t Include/*.h; [33m\[39;49;00m$
  1021		[34mfor[39;49;00m i [34min[39;49;00m [34m$([39;49;00mSRCDIRS[34m)[39;49;00m; [34mdo[39;49;00m ctags -w -t -a [31m$$[39;49;00mi/*.[ch]; [33m\[39;49;00m$
  1022		[34mdone[39;49;00m; [33m\[39;49;00m$
  1023		sort -o tags tags$
  1024	$
  1025	[37m# Create a tags file for GNU Emacs[39;49;00m$
  1026	[32mTAGS[39;49;00m::$
  1027		[36mcd[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m; [33m\[39;49;00m$
  1028		etags Include/*.h; [33m\[39;49;00m$
  1029		[34mfor[39;49;00m i [34min[39;49;00m [34m$([39;49;00mSRCDIRS[34m)[39;49;00m; [34mdo[39;49;00m etags -a [31m$$[39;49;00mi/*.[ch]; [34mdone[39;49;00m$
  1030	$
  1031	[37m# Sanitation targets -- clean leaves libraries, executables and tags[39;49;00m$
  1032	[37m# files, which clobber removes those as well[39;49;00m$
  1033	[32mpycremoval[39;49;00m:$
  1034		find [34m$([39;49;00msrcdir[34m)[39;49;00m -name [33m'*.py[co]'[39;49;00m -exec rm -f {} [33m';'[39;49;00m$
  1035	$
  1036	[32mclean[39;49;00m: pycremoval$
  1037		find . -name [33m'*.o'[39;49;00m -exec rm -f {} [33m';'[39;49;00m$
  1038		find . -name [33m'*.s[ol]'[39;49;00m -exec rm -f {} [33m';'[39;49;00m$
  1039		find [34m$([39;49;00msrcdir[34m)[39;49;00m/build -name [33m'fficonfig.h'[39;49;00m -exec rm -f {} [33m';'[39;49;00m || [36mtrue[39;49;00m$
  1040		find [34m$([39;49;00msrcdir[34m)[39;49;00m/build -name [33m'fficonfig.py'[39;49;00m -exec rm -f {} [33m';'[39;49;00m || [36mtrue[39;49;00m$
  1041	$
  1042	[32mclobber[39;49;00m: clean$
  1043		-rm -f [34m$([39;49;00mBUILDPYTHON[34m)[39;49;00m [34m$([39;49;00mPGEN[34m)[39;49;00m [34m$([39;49;00mLIBRARY[34m)[39;49;00m [34m$([39;49;00mLDLIBRARY[34m)[39;49;00m [34m$([39;49;00mDLLLIBRARY[34m)[39;49;00m [33m\[39;49;00m$
  1044			tags TAGS [33m\[39;49;00m$
  1045			config.cache config.log pyconfig.h Modules/config.c$
  1046		-rm -rf build platform$
  1047		-rm -rf [34m$([39;49;00mPYTHONFRAMEWORKDIR[34m)[39;49;00m$
  1048	$
  1049	[37m# Make things extra clean, before making a distribution:[39;49;00m$
  1050	[37m# remove all generated files, even Makefile[.pre][39;49;00m$
  1051	[37m# Keep configure and Python-ast.[ch], it's possible they can't be generated[39;49;00m$
  1052	[32mdistclean[39;49;00m: clobber$
  1053		-rm -f core Makefile Makefile.pre config.status [33m\[39;49;00m$
  1054			Modules/Setup Modules/Setup.local Modules/Setup.config$
  1055		find [34m$([39;49;00msrcdir[34m)[39;49;00m [33m'('[39;49;00m -name [33m'*.fdc'[39;49;00m -o -name [33m'*~'[39;49;00m [33m\[39;49;00m$
  1056				   -o -name [33m'[@,#]*'[39;49;00m -o -name [33m'*.old'[39;49;00m [33m\[39;49;00m$
  1057				   -o -name [33m'*.orig'[39;49;00m -o -name [33m'*.rej'[39;49;00m [33m\[39;49;00m$
  1058				   -o -name [33m'*.bak'[39;49;00m [33m')'[39;49;00m [33m\[39;49;00m$
  1059				   -exec rm -f {} [33m';'[39;49;00m$
  1060	$
  1061	[37m# Check for smelly exported symbols (not starting with Py/_Py)[39;49;00m$
  1062	[32msmelly[39;49;00m: all$
  1063		nm -p [34m$([39;49;00mLIBRARY[34m)[39;49;00m | [33m\[39;49;00m$
  1064			sed -n [33m"/ [TDB] /s/.* //p"[39;49;00m | grep -v [33m"^_*Py"[39;49;00m | sort -u; [33m\[39;49;00m$
  1065	$
  1066	[37m# Find files with funny names[39;49;00m$
  1067	[32mfunny[39;49;00m:$
  1068		find [34m$([39;49;00mDISTDIRS[34m)[39;49;00m -type d [33m\[39;49;00m$
  1069			-o -name [33m'*.[chs]'[39;49;00m [33m\[39;49;00m$
  1070			-o -name [33m'*.py'[39;49;00m [33m\[39;49;00m$
  1071			-o -name [33m'*.doc'[39;49;00m [33m\[39;49;00m$
  1072			-o -name [33m'*.sty'[39;49;00m [33m\[39;49;00m$
  1073			-o -name [33m'*.bib'[39;49;00m [33m\[39;49;00m$
  1074			-o -name [33m'*.dat'[39;49;00m [33m\[39;49;00m$
  1075			-o -name [33m'*.el'[39;49;00m [33m\[39;49;00m$
  1076			-o -name [33m'*.fd'[39;49;00m [33m\[39;49;00m$
  1077			-o -name [33m'*.in'[39;49;00m [33m\[39;49;00m$
  1078			-o -name [33m'*.tex'[39;49;00m [33m\[39;49;00m$
  1079			-o -name [33m'*,[vpt]'[39;49;00m [33m\[39;49;00m$
  1080			-o -name [33m'Setup'[39;49;00m [33m\[39;49;00m$
  1081			-o -name [33m'Setup.*'[39;49;00m [33m\[39;49;00m$
  1082			-o -name README [33m\[39;49;00m$
  1083			-o -name Makefile [33m\[39;49;00m$
  1084			-o -name ChangeLog [33m\[39;49;00m$
  1085			-o -name Repository [33m\[39;49;00m$
  1086			-o -name Root [33m\[39;49;00m$
  1087			-o -name Entries [33m\[39;49;00m$
  1088			-o -name Tag [33m\[39;49;00m$
  1089			-o -name tags [33m\[39;49;00m$
  1090			-o -name TAGS [33m\[39;49;00m$
  1091			-o -name .cvsignore [33m\[39;49;00m$
  1092			-o -name MANIFEST [33m\[39;49;00m$
  1093			-o -print$
  1094	$
  1095	[37m# Dependencies[39;49;00m$
  1096	$
  1097	[32mPython/thread.o[39;49;00m:  [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Python/thread_atheos.h [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Python/thread_beos.h [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Python/thread_cthread.h [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Python/thread_foobar.h [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Python/thread_lwp.h [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Python/thread_nt.h [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Python/thread_os2.h [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Python/thread_pth.h [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Python/thread_pthread.h [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Python/thread_sgi.h [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Python/thread_solaris.h [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Python/thread_wince.h$
  1098	$
  1099	[37m# Declare targets that aren't real files[39;49;00m$
  1100	[32m.PHONY[39;49;00m: all sharedmods oldsharedmods test quicktest memtest$
  1101	[32m.PHONY[39;49;00m: install altinstall oldsharedinstall bininstall altbininstall$
  1102	[32m.PHONY[39;49;00m: maninstall libinstall inclinstall libainstall sharedinstall$
  1103	[32m.PHONY[39;49;00m: frameworkinstall frameworkinstallframework frameworkinstallstructure$
  1104	[32m.PHONY[39;49;00m: frameworkinstallmaclib frameworkinstallapps frameworkinstallunixtools$
  1105	[32m.PHONY[39;49;00m: frameworkaltinstallunixtools recheck autoconf clean clobber distclean $
  1106	[32m.PHONY[39;49;00m: smelly funny$
  1107	$
  1108	[37m# IF YOU PUT ANYTHING HERE IT WILL GO AWAY[39;49;00m$
  1109	$
  1110	[37m# Rules appended by makedepend[39;49;00m$
  1111	$
  1112	[32mModules/threadmodule.o[39;49;00m: [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/threadmodule.c; [34m$([39;49;00m[31mCC[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31mPY_CFLAGS[39;49;00m[34m)[39;49;00m  -c [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/threadmodule.c -o Modules/threadmodule.o$
  1113	[32mModules/threadmodule$(SO)[39;49;00m:  Modules/threadmodule.o; [34m$([39;49;00m[31mLDSHARED[39;49;00m[34m)[39;49;00m  Modules/threadmodule.o   -o Modules/threadmodule[34m$([39;49;00m[31mSO[39;49;00m[34m)[39;49;00m$
  1114	[32mModules/signalmodule.o[39;49;00m: [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/signalmodule.c; [34m$([39;49;00m[31mCC[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31mPY_CFLAGS[39;49;00m[34m)[39;49;00m  -c [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/signalmodule.c -o Modules/signalmodule.o$
  1115	[32mModules/signalmodule$(SO)[39;49;00m:  Modules/signalmodule.o; [34m$([39;49;00m[31mLDSHARED[39;49;00m[34m)[39;49;00m  Modules/signalmodule.o   -o Modules/signalmodule[34m$([39;49;00m[31mSO[39;49;00m[34m)[39;49;00m$
  1116	[32mModules/posixmodule.o[39;49;00m: [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/posixmodule.c; [34m$([39;49;00m[31mCC[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31mPY_CFLAGS[39;49;00m[34m)[39;49;00m  -c [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/posixmodule.c -o Modules/posixmodule.o$
  1117	[32mModules/posixmodule$(SO)[39;49;00m:  Modules/posixmodule.o; [34m$([39;49;00m[31mLDSHARED[39;49;00m[34m)[39;49;00m  Modules/posixmodule.o   -o Modules/posixmodule[34m$([39;49;00m[31mSO[39;49;00m[34m)[39;49;00m$
  1118	[32mModules/errnomodule.o[39;49;00m: [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/errnomodule.c; [34m$([39;49;00m[31mCC[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31mPY_CFLAGS[39;49;00m[34m)[39;49;00m  -c [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/errnomodule.c -o Modules/errnomodule.o$
  1119	[32mModules/errnomodule$(SO)[39;49;00m:  Modules/errnomodule.o; [34m$([39;49;00m[31mLDSHARED[39;49;00m[34m)[39;49;00m  Modules/errnomodule.o   -o Modules/errnomodule[34m$([39;49;00m[31mSO[39;49;00m[34m)[39;49;00m$
  1120	[32mModules/pwdmodule.o[39;49;00m: [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/pwdmodule.c; [34m$([39;49;00m[31mCC[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31mPY_CFLAGS[39;49;00m[34m)[39;49;00m  -c [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/pwdmodule.c -o Modules/pwdmodule.o$
  1121	[32mModules/pwdmodule$(SO)[39;49;00m:  Modules/pwdmodule.o; [34m$([39;49;00m[31mLDSHARED[39;49;00m[34m)[39;49;00m  Modules/pwdmodule.o   -o Modules/pwdmodule[34m$([39;49;00m[31mSO[39;49;00m[34m)[39;49;00m$
  1122	[32mModules/_sre.o[39;49;00m: [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/_sre.c; [34m$([39;49;00m[31mCC[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31mPY_CFLAGS[39;49;00m[34m)[39;49;00m  -c [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/_sre.c -o Modules/_sre.o$
  1123	[32mModules/_sre$(SO)[39;49;00m:  Modules/_sre.o; [34m$([39;49;00m[31mLDSHARED[39;49;00m[34m)[39;49;00m  Modules/_sre.o   -o Modules/_sre[34m$([39;49;00m[31mSO[39;49;00m[34m)[39;49;00m$
  1124	[32mModules/_codecsmodule.o[39;49;00m: [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/_codecsmodule.c; [34m$([39;49;00m[31mCC[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31mPY_CFLAGS[39;49;00m[34m)[39;49;00m  -c [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/_codecsmodule.c -o Modules/_codecsmodule.o$
  1125	[32mModules/_codecsmodule$(SO)[39;49;00m:  Modules/_codecsmodule.o; [34m$([39;49;00m[31mLDSHARED[39;49;00m[34m)[39;49;00m  Modules/_codecsmodule.o   -o Modules/_codecsmodule[34m$([39;49;00m[31mSO[39;49;00m[34m)[39;49;00m$
  1126	[32mModules/zipimport.o[39;49;00m: [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/zipimport.c; [34m$([39;49;00m[31mCC[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31mPY_CFLAGS[39;49;00m[34m)[39;49;00m  -c [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/zipimport.c -o Modules/zipimport.o$
  1127	[32mModules/zipimport$(SO)[39;49;00m:  Modules/zipimport.o; [34m$([39;49;00m[31mLDSHARED[39;49;00m[34m)[39;49;00m  Modules/zipimport.o   -o Modules/zipimport[34m$([39;49;00m[31mSO[39;49;00m[34m)[39;49;00m$
  1128	[32mModules/symtablemodule.o[39;49;00m: [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/symtablemodule.c; [34m$([39;49;00m[31mCC[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31mPY_CFLAGS[39;49;00m[34m)[39;49;00m  -c [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/symtablemodule.c -o Modules/symtablemodule.o$
  1129	[32mModules/_symtablemodule$(SO)[39;49;00m:  Modules/symtablemodule.o; [34m$([39;49;00m[31mLDSHARED[39;49;00m[34m)[39;49;00m  Modules/symtablemodule.o   -o Modules/_symtablemodule[34m$([39;49;00m[31mSO[39;49;00m[34m)[39;49;00m$
  1130	[32mModules/xxsubtype.o[39;49;00m: [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/xxsubtype.c; [34m$([39;49;00m[31mCC[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31mPY_CFLAGS[39;49;00m[34m)[39;49;00m  -c [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/xxsubtype.c -o Modules/xxsubtype.o$
  1131	[32mModules/xxsubtype$(SO)[39;49;00m:  Modules/xxsubtype.o; [34m$([39;49;00m[31mLDSHARED[39;49;00m[34m)[39;49;00m  Modules/xxsubtype.o   -o Modules/xxsubtype[34m$([39;49;00m[31mSO[39;49;00m[34m)[39;49;00m$

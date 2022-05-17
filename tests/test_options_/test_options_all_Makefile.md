     1^I[37m# Generated automatically from Makefile.pre by makesetup.[39;49;00m$
     2^I[37m# Top-level Makefile for Python[39;49;00m$
     3^I[37m#[39;49;00m$
     4^I[37m# As distributed, this file is called Makefile.pre.in; it is processed[39;49;00m$
     5^I[37m# into the real Makefile by running the script ./configure, which[39;49;00m$
     6^I[37m# replaces things like @spam@ with values appropriate for your system.[39;49;00m$
     7^I[37m# This means that if you edit Makefile, your changes get lost the next[39;49;00m$
     8^I[37m# time you run the configure script.  Ideally, you can do:[39;49;00m$
     9^I[37m#[39;49;00m$
    10^I[37m#^I./configure[39;49;00m$
    11^I[37m#^Imake[39;49;00m$
    12^I[37m#^Imake test[39;49;00m$
    13^I[37m#^Imake install[39;49;00m$
    14^I[37m#[39;49;00m$
    15^I[37m# If you have a previous version of Python installed that you don't[39;49;00m$
    16^I[37m# want to overwrite, you can use "make altinstall" instead of "make[39;49;00m$
    17^I[37m# install".  Refer to the "Installing" section in the README file for[39;49;00m$
    18^I[37m# additional details.[39;49;00m$
    19^I[37m#[39;49;00m$
    20^I[37m# See also the section "Build instructions" in the README file.[39;49;00m$
    21^I$
    22^I[37m# === Variables set by makesetup ===[39;49;00m$
    23^I$
    24^I[31mMODOBJS[39;49;00m=          Modules/threadmodule.o  Modules/signalmodule.o  Modules/posixmodule.o  Modules/errnomodule.o  Modules/pwdmodule.o  Modules/_sre.o  Modules/_codecsmodule.o  Modules/zipimport.o  Modules/symtablemodule.o  Modules/xxsubtype.o$
    25^I[31mMODLIBS[39;49;00m=        [34m$([39;49;00mLOCALMODLIBS[34m)[39;49;00m [34m$([39;49;00mBASEMODLIBS[34m)[39;49;00m$
    26^I$
    27^I[37m# === Variables set by configure[39;49;00m$
    28^I[31mVERSION[39;49;00m=^I[34m2[39;49;00m.6$
    29^I[31msrcdir[39;49;00m=^I^I.$
    30^I$
    31^I$
    32^I[31mCC[39;49;00m=^I^Igcc -pthread$
    33^I[31mCXX[39;49;00m=^I^Ig++ -pthread$
    34^I[31mMAINCC[39;49;00m=^I^I[34m$([39;49;00mCC[34m)[39;49;00m$
    35^I[31mLINKCC[39;49;00m=^I^I[34m$([39;49;00mPURIFY[34m)[39;49;00m [34m$([39;49;00mMAINCC[34m)[39;49;00m$
    36^I[31mAR[39;49;00m=^I^Iar$
    37^I[31mRANLIB[39;49;00m=^I^Iranlib$
    38^I[31mSVNVERSION[39;49;00m=^Isvnversion [34m$([39;49;00msrcdir[34m)[39;49;00m$
    39^I$
    40^I[37m# Shell used by make (some versions default to the login shell, which is bad)[39;49;00m$
    41^I[31mSHELL[39;49;00m=^I^I/bin/sh$
    42^I$
    43^I[37m# Use this to make a link between python$(VERSION) and python in $(BINDIR)[39;49;00m$
    44^I[31mLN[39;49;00m=^I^Iln$
    45^I$
    46^I[37m# Portable install script (configure doesn't always guess right)[39;49;00m$
    47^I[31mINSTALL[39;49;00m=^I/usr/bin/install -c$
    48^I[31mINSTALL_PROGRAM[39;49;00m=[33m${[39;49;00m[31mINSTALL[39;49;00m[33m}[39;49;00m$
    49^I[31mINSTALL_SCRIPT[39;49;00m= [33m${[39;49;00m[31mINSTALL[39;49;00m[33m}[39;49;00m$
    50^I[31mINSTALL_DATA[39;49;00m=^I[33m${[39;49;00m[31mINSTALL[39;49;00m[33m}[39;49;00m -m [34m644[39;49;00m$
    51^I[37m# Shared libraries must be installed with executable mode on some systems;[39;49;00m$
    52^I[37m# rather than figuring out exactly which, we always give them executable mode.[39;49;00m$
    53^I[37m# Also, making them read-only seems to be a good idea...[39;49;00m$
    54^I[31mINSTALL_SHARED[39;49;00m= [33m${[39;49;00m[31mINSTALL[39;49;00m[33m}[39;49;00m -m [34m555[39;49;00m$
    55^I$
    56^I[31mMAKESETUP[39;49;00m=      [34m$([39;49;00msrcdir[34m)[39;49;00m/Modules/makesetup$
    57^I$
    58^I[37m# Compiler options[39;49;00m$
    59^I[31mOPT[39;49;00m=^I^I-g -Wall -Wstrict-prototypes$
    60^I[31mBASECFLAGS[39;49;00m=^I -fno-strict-aliasing$
    61^I[31mCFLAGS[39;49;00m=^I^I[34m$([39;49;00mBASECFLAGS[34m)[39;49;00m [34m$([39;49;00mOPT[34m)[39;49;00m [34m$([39;49;00mEXTRA_CFLAGS[34m)[39;49;00m$
    62^I[37m# Both CPPFLAGS and LDFLAGS need to contain the shell's value for setup.py to[39;49;00m$
    63^I[37m# be able to build extension modules using the directories specified in the[39;49;00m$
    64^I[37m# environment variables[39;49;00m$
    65^I[31mCPPFLAGS[39;49;00m=^I-I. -I[34m$([39;49;00msrcdir[34m)[39;49;00m/Include $
    66^I[31mLDFLAGS[39;49;00m=^I$
    67^I[31mLDLAST[39;49;00m=^I^I$
    68^I[31mSGI_ABI[39;49;00m=^I$
    69^I[31mCCSHARED[39;49;00m=^I-fPIC$
    70^I[31mLINKFORSHARED[39;49;00m=^I-Xlinker -export-dynamic$
    71^I[37m# Extra C flags added for building the interpreter object files.[39;49;00m$
    72^I[31mCFLAGSFORSHARED[39;49;00m=$
    73^I[37m# C flags used for building the interpreter object files[39;49;00m$
    74^I[31mPY_CFLAGS[39;49;00m=^I[34m$([39;49;00mCFLAGS[34m)[39;49;00m [34m$([39;49;00mCPPFLAGS[34m)[39;49;00m [34m$([39;49;00mCFLAGSFORSHARED[34m)[39;49;00m -DPy_BUILD_CORE$
    75^I$
    76^I$
    77^I[37m# Machine-dependent subdirectories[39;49;00m$
    78^I[31mMACHDEP[39;49;00m=^Ilinux2$
    79^I$
    80^I[37m# Install prefix for architecture-independent files[39;49;00m$
    81^I[31mprefix[39;49;00m=^I^I/usr/local$
    82^I$
    83^I[37m# Install prefix for architecture-dependent files[39;49;00m$
    84^I[31mexec_prefix[39;49;00m=^I[33m${[39;49;00m[31mprefix[39;49;00m[33m}[39;49;00m$
    85^I$
    86^I[37m# Expanded directories[39;49;00m$
    87^I[31mBINDIR[39;49;00m=^I^I[34m$([39;49;00mexec_prefix[34m)[39;49;00m/bin$
    88^I[31mLIBDIR[39;49;00m=^I^I[34m$([39;49;00mexec_prefix[34m)[39;49;00m/lib$
    89^I[31mMANDIR[39;49;00m=^I^I[33m${[39;49;00m[31mprefix[39;49;00m[33m}[39;49;00m/man$
    90^I[31mINCLUDEDIR[39;49;00m=^I[33m${[39;49;00m[31mprefix[39;49;00m[33m}[39;49;00m/include$
    91^I[31mCONFINCLUDEDIR[39;49;00m=^I[34m$([39;49;00mexec_prefix[34m)[39;49;00m/include$
    92^I[31mSCRIPTDIR[39;49;00m=^I[34m$([39;49;00mprefix[34m)[39;49;00m/lib$
    93^I$
    94^I[37m# Detailed destination directories[39;49;00m$
    95^I[31mBINLIBDEST[39;49;00m=^I[34m$([39;49;00mLIBDIR[34m)[39;49;00m/python[34m$([39;49;00mVERSION[34m)[39;49;00m$
    96^I[31mLIBDEST[39;49;00m=^I[34m$([39;49;00mSCRIPTDIR[34m)[39;49;00m/python[34m$([39;49;00mVERSION[34m)[39;49;00m$
    97^I[31mINCLUDEPY[39;49;00m=^I[34m$([39;49;00mINCLUDEDIR[34m)[39;49;00m/python[34m$([39;49;00mVERSION[34m)[39;49;00m$
    98^I[31mCONFINCLUDEPY[39;49;00m=^I[34m$([39;49;00mCONFINCLUDEDIR[34m)[39;49;00m/python[34m$([39;49;00mVERSION[34m)[39;49;00m$
    99^I[31mLIBP[39;49;00m=^I^I[34m$([39;49;00mLIBDIR[34m)[39;49;00m/python[34m$([39;49;00mVERSION[34m)[39;49;00m$
   100^I$
   101^I[37m# Symbols used for using shared libraries[39;49;00m$
   102^I[31mSO[39;49;00m=^I^I.so$
   103^I[31mLDSHARED[39;49;00m=^I[34m$([39;49;00mCC[34m)[39;49;00m -shared$
   104^I[31mBLDSHARED[39;49;00m=^I[34m$([39;49;00mCC[34m)[39;49;00m -shared$
   105^I[31mDESTSHARED[39;49;00m=^I[34m$([39;49;00mBINLIBDEST[34m)[39;49;00m/lib-dynload$
   106^I$
   107^I[37m# Executable suffix (.exe on Windows and Mac OS X)[39;49;00m$
   108^I[31mEXE[39;49;00m=^I^I$
   109^I[31mBUILDEXE[39;49;00m=^I$
   110^I$
   111^I[37m# Short name and location for Mac OS X Python framework[39;49;00m$
   112^I[31mUNIVERSALSDK[39;49;00m=$
   113^I[31mPYTHONFRAMEWORK[39;49;00m=^I$
   114^I[31mPYTHONFRAMEWORKDIR[39;49;00m=^Ino-framework$
   115^I[31mPYTHONFRAMEWORKPREFIX[39;49;00m=^I$
   116^I[31mPYTHONFRAMEWORKINSTALLDIR[39;49;00m= $
   117^I[37m# Deployment target selected during configure, to be checked[39;49;00m$
   118^I[37m# by distutils. The export statement is needed to ensure that the[39;49;00m$
   119^I[37m# deployment target is active during build.[39;49;00m$
   120^I[31mMACOSX_DEPLOYMENT_TARGET[39;49;00m=$
   121^I[37m#export MACOSX_DEPLOYMENT_TARGET[39;49;00m$
   122^I$
   123^I[37m# Options to enable prebinding (for fast startup prior to Mac OS X 10.3)[39;49;00m$
   124^I[31mOTHER_LIBTOOL_OPT[39;49;00m=$
   125^I$
   126^I[37m# Environment to run shared python without installed libraries[39;49;00m$
   127^I[31mRUNSHARED[39;49;00m=       $
   128^I$
   129^I[37m# Modes for directories, executables and data files created by the[39;49;00m$
   130^I[37m# install process.  Default to user-only-writable for all file types.[39;49;00m$
   131^I[31mDIRMODE[39;49;00m=^I[34m755[39;49;00m$
   132^I[31mEXEMODE[39;49;00m=^I[34m755[39;49;00m$
   133^I[31mFILEMODE[39;49;00m=^I[34m644[39;49;00m$
   134^I$
   135^I[37m# configure script arguments[39;49;00m$
   136^I[31mCONFIG_ARGS[39;49;00m=^I[33m'--with-pydebug'[39;49;00m$
   137^I$
   138^I$
   139^I[37m# Subdirectories with code[39;49;00m$
   140^I[31mSRCDIRS[39;49;00m= ^IParser Grammar Objects Python Modules Mac$
   141^I$
   142^I[37m# Other subdirectories[39;49;00m$
   143^I[31mSUBDIRSTOO[39;49;00m=^IInclude Lib Misc Demo$
   144^I$
   145^I[37m# Files and directories to be distributed[39;49;00m$
   146^I[31mCONFIGFILES[39;49;00m=^Iconfigure configure.in acconfig.h pyconfig.h.in Makefile.pre.in$
   147^I[31mDISTFILES[39;49;00m=^IREADME ChangeLog [34m$([39;49;00mCONFIGFILES[34m)[39;49;00m$
   148^I[31mDISTDIRS[39;49;00m=^I[34m$([39;49;00mSUBDIRS[34m)[39;49;00m [34m$([39;49;00mSUBDIRSTOO[34m)[39;49;00m Ext-dummy$
   149^I[31mDIST[39;49;00m=^I^I[34m$([39;49;00mDISTFILES[34m)[39;49;00m [34m$([39;49;00mDISTDIRS[34m)[39;49;00m$
   150^I$
   151^I$
   152^I[31mLIBRARY[39;49;00m=^Ilibpython[34m$([39;49;00mVERSION[34m)[39;49;00m.a$
   153^I[31mLDLIBRARY[39;49;00m=      libpython[34m$([39;49;00mVERSION[34m)[39;49;00m.a$
   154^I[31mBLDLIBRARY[39;49;00m=     [34m$([39;49;00mLDLIBRARY[34m)[39;49;00m$
   155^I[31mDLLLIBRARY[39;49;00m=^I$
   156^I[31mLDLIBRARYDIR[39;49;00m=   $
   157^I[31mINSTSONAME[39;49;00m=^I[34m$([39;49;00mLDLIBRARY[34m)[39;49;00m$
   158^I$
   159^I$
   160^I[31mLIBS[39;49;00m=^I^I-lpthread -ldl  -lutil$
   161^I[31mLIBM[39;49;00m=^I^I-lm$
   162^I[31mLIBC[39;49;00m=^I^I$
   163^I[31mSYSLIBS[39;49;00m=^I[34m$([39;49;00mLIBM[34m)[39;49;00m [34m$([39;49;00mLIBC[34m)[39;49;00m$
   164^I[31mSHLIBS[39;49;00m=^I^I[34m$([39;49;00mLIBS[34m)[39;49;00m$
   165^I$
   166^I[31mTHREADOBJ[39;49;00m=^IPython/thread.o$
   167^I[31mDLINCLDIR[39;49;00m=^I.$
   168^I[31mDYNLOADFILE[39;49;00m=^Idynload_shlib.o$
   169^I[31mMACHDEP_OBJS[39;49;00m=^I$
   170^I[31mUNICODE_OBJS[39;49;00m=   Objects/unicodeobject.o Objects/unicodectype.o$
   171^I$
   172^I[31mPYTHON[39;49;00m=^I^Ipython[34m$([39;49;00mEXE[34m)[39;49;00m$
   173^I[31mBUILDPYTHON[39;49;00m=^Ipython[34m$([39;49;00mBUILDEXE[34m)[39;49;00m$
   174^I$
   175^I[37m# === Definitions added by makesetup ===[39;49;00m$
   176^I$
   177^I[31mLOCALMODLIBS[39;49;00m=          $
   178^I[31mBASEMODLIBS[39;49;00m=$
   179^I[31mGLHACK[39;49;00m=-Dclear=__GLclear$
   180^I[31mPYTHONPATH[39;49;00m=[34m$([39;49;00mCOREPYTHONPATH[34m)[39;49;00m$
   181^I[31mCOREPYTHONPATH[39;49;00m=[34m$([39;49;00mDESTPATH[34m)[39;49;00m[34m$([39;49;00mSITEPATH[34m)[39;49;00m[34m$([39;49;00mTESTPATH[34m)[39;49;00m[34m$([39;49;00mMACHDEPPATH[34m)[39;49;00m[34m$([39;49;00mEXTRAMACHDEPPATH[34m)[39;49;00m[34m$([39;49;00mTKPATH[34m)[39;49;00m$
   182^I[31mTKPATH[39;49;00m=:lib-tk$
   183^I[31mEXTRAMACHDEPPATH[39;49;00m=$
   184^I[31mMACHDEPPATH[39;49;00m=:plat-[34m$([39;49;00mMACHDEP[34m)[39;49;00m$
   185^I[31mTESTPATH[39;49;00m=$
   186^I[31mSITEPATH[39;49;00m=$
   187^I[31mDESTPATH[39;49;00m=$
   188^I[31mMACHDESTLIB[39;49;00m=[34m$([39;49;00mBINLIBDEST[34m)[39;49;00m$
   189^I[31mDESTLIB[39;49;00m=[34m$([39;49;00mLIBDEST[34m)[39;49;00m$
   190^I$
   191^I$
   192^I$
   193^I[37m##########################################################################[39;49;00m$
   194^I[37m# Modules[39;49;00m$
   195^I[31mMODULE_OBJS[39;49;00m=^I[33m\[39;49;00m$
   196^I^I^IModules/config.o [33m\[39;49;00m$
   197^I^I^IModules/getpath.o [33m\[39;49;00m$
   198^I^I^IModules/main.o [33m\[39;49;00m$
   199^I^I^IModules/gcmodule.o$
   200^I$
   201^I[37m# Used of signalmodule.o is not available[39;49;00m$
   202^I[31mSIGNAL_OBJS[39;49;00m=^I$
   203^I$
   204^I$
   205^I[37m##########################################################################[39;49;00m$
   206^I[37m# Grammar[39;49;00m$
   207^I[31mGRAMMAR_H[39;49;00m=^I[34m$([39;49;00msrcdir[34m)[39;49;00m/Include/graminit.h$
   208^I[31mGRAMMAR_C[39;49;00m=^I[34m$([39;49;00msrcdir[34m)[39;49;00m/Python/graminit.c$
   209^I[31mGRAMMAR_INPUT[39;49;00m=^I[34m$([39;49;00msrcdir[34m)[39;49;00m/Grammar/Grammar$
   210^I$
   211^I$
   212^I[37m##########################################################################[39;49;00m$
   213^I[37m# Parser[39;49;00m$
   214^I[31mPGEN[39;49;00m=^I^IParser/pgen[34m$([39;49;00mEXE[34m)[39;49;00m$
   215^I$
   216^I[31mPOBJS[39;49;00m=^I^I[33m\[39;49;00m$
   217^I^I^IParser/acceler.o [33m\[39;49;00m$
   218^I^I^IParser/grammar1.o [33m\[39;49;00m$
   219^I^I^IParser/listnode.o [33m\[39;49;00m$
   220^I^I^IParser/node.o [33m\[39;49;00m$
   221^I^I^IParser/parser.o [33m\[39;49;00m$
   222^I^I^IParser/parsetok.o [33m\[39;49;00m$
   223^I^I^IParser/bitset.o [33m\[39;49;00m$
   224^I^I^IParser/metagrammar.o [33m\[39;49;00m$
   225^I^I^IParser/firstsets.o [33m\[39;49;00m$
   226^I^I^IParser/grammar.o [33m\[39;49;00m$
   227^I^I^IParser/pgen.o$
   228^I$
   229^I[31mPARSER_OBJS[39;49;00m=^I[34m$([39;49;00mPOBJS[34m)[39;49;00m Parser/myreadline.o Parser/tokenizer.o$
   230^I$
   231^I[31mPGOBJS[39;49;00m=^I^I[33m\[39;49;00m$
   232^I^I^IObjects/obmalloc.o [33m\[39;49;00m$
   233^I^I^IPython/mysnprintf.o [33m\[39;49;00m$
   234^I^I^IParser/tokenizer_pgen.o [33m\[39;49;00m$
   235^I^I^IParser/printgrammar.o [33m\[39;49;00m$
   236^I^I^IParser/pgenmain.o$
   237^I$
   238^I[31mPGENOBJS[39;49;00m=^I[34m$([39;49;00mPGENMAIN[34m)[39;49;00m [34m$([39;49;00mPOBJS[34m)[39;49;00m [34m$([39;49;00mPGOBJS[34m)[39;49;00m$
   239^I$
   240^I[37m##########################################################################[39;49;00m$
   241^I[37m# AST[39;49;00m$
   242^I[31mAST_H_DIR[39;49;00m=^I[34m$([39;49;00msrcdir[34m)[39;49;00m/Include$
   243^I[31mAST_H[39;49;00m=^I^I[34m$([39;49;00mAST_H_DIR[34m)[39;49;00m/Python-ast.h$
   244^I[31mAST_C_DIR[39;49;00m=^I[34m$([39;49;00msrcdir[34m)[39;49;00m/Python$
   245^I[31mAST_C[39;49;00m=^I^I[34m$([39;49;00mAST_C_DIR[34m)[39;49;00m/Python-ast.c$
   246^I[31mAST_ASDL[39;49;00m=^I[34m$([39;49;00msrcdir[34m)[39;49;00m/Parser/Python.asdl$
   247^I$
   248^I[31mASDLGEN_FILES[39;49;00m=^I[34m$([39;49;00msrcdir[34m)[39;49;00m/Parser/asdl.py [34m$([39;49;00msrcdir[34m)[39;49;00m/Parser/asdl_c.py$
   249^I[37m# XXX Note that a build now requires Python exist before the build starts[39;49;00m$
   250^I[31mASDLGEN[39;49;00m=^I[34m$([39;49;00msrcdir[34m)[39;49;00m/Parser/asdl_c.py$
   251^I$
   252^I[37m##########################################################################[39;49;00m$
   253^I[37m# Python[39;49;00m$
   254^I[31mPYTHON_OBJS[39;49;00m=^I[33m\[39;49;00m$
   255^I^I^IPython/Python-ast.o [33m\[39;49;00m$
   256^I^I^IPython/asdl.o [33m\[39;49;00m$
   257^I^I^IPython/ast.o [33m\[39;49;00m$
   258^I^I^IPython/bltinmodule.o [33m\[39;49;00m$
   259^I^I^IPython/ceval.o [33m\[39;49;00m$
   260^I^I^IPython/compile.o [33m\[39;49;00m$
   261^I^I^IPython/codecs.o [33m\[39;49;00m$
   262^I^I^IPython/errors.o [33m\[39;49;00m$
   263^I^I^IPython/frozen.o [33m\[39;49;00m$
   264^I^I^IPython/frozenmain.o [33m\[39;49;00m$
   265^I^I^IPython/future.o [33m\[39;49;00m$
   266^I^I^IPython/getargs.o [33m\[39;49;00m$
   267^I^I^IPython/getcompiler.o [33m\[39;49;00m$
   268^I^I^IPython/getcopyright.o [33m\[39;49;00m$
   269^I^I^IPython/getmtime.o [33m\[39;49;00m$
   270^I^I^IPython/getplatform.o [33m\[39;49;00m$
   271^I^I^IPython/getversion.o [33m\[39;49;00m$
   272^I^I^IPython/graminit.o [33m\[39;49;00m$
   273^I^I^IPython/import.o [33m\[39;49;00m$
   274^I^I^IPython/importdl.o [33m\[39;49;00m$
   275^I^I^IPython/marshal.o [33m\[39;49;00m$
   276^I^I^IPython/modsupport.o [33m\[39;49;00m$
   277^I^I^IPython/mystrtoul.o [33m\[39;49;00m$
   278^I^I^IPython/mysnprintf.o [33m\[39;49;00m$
   279^I^I^IPython/peephole.o [33m\[39;49;00m$
   280^I^I^IPython/pyarena.o [33m\[39;49;00m$
   281^I^I^IPython/pyfpe.o [33m\[39;49;00m$
   282^I^I^IPython/pystate.o [33m\[39;49;00m$
   283^I^I^IPython/pythonrun.o [33m\[39;49;00m$
   284^I^I^IPython/structmember.o [33m\[39;49;00m$
   285^I^I^IPython/symtable.o [33m\[39;49;00m$
   286^I^I^IPython/sysmodule.o [33m\[39;49;00m$
   287^I^I^IPython/traceback.o [33m\[39;49;00m$
   288^I^I^IPython/getopt.o [33m\[39;49;00m$
   289^I^I^IPython/pystrtod.o [33m\[39;49;00m$
   290^I^I^IPython/[34m$([39;49;00mDYNLOADFILE[34m)[39;49;00m [33m\[39;49;00m$
   291^I^I^I[34m$([39;49;00mMACHDEP_OBJS[34m)[39;49;00m [33m\[39;49;00m$
   292^I^I^I[34m$([39;49;00mTHREADOBJ[34m)[39;49;00m$
   293^I$
   294^I$
   295^I[37m##########################################################################[39;49;00m$
   296^I[37m# Objects[39;49;00m$
   297^I[31mOBJECT_OBJS[39;49;00m=^I[33m\[39;49;00m$
   298^I^I^IObjects/abstract.o [33m\[39;49;00m$
   299^I^I^IObjects/boolobject.o [33m\[39;49;00m$
   300^I^I^IObjects/bufferobject.o [33m\[39;49;00m$
   301^I^I^IObjects/cellobject.o [33m\[39;49;00m$
   302^I^I^IObjects/classobject.o [33m\[39;49;00m$
   303^I^I^IObjects/cobject.o [33m\[39;49;00m$
   304^I^I^IObjects/codeobject.o [33m\[39;49;00m$
   305^I^I^IObjects/complexobject.o [33m\[39;49;00m$
   306^I^I^IObjects/descrobject.o [33m\[39;49;00m$
   307^I^I^IObjects/enumobject.o [33m\[39;49;00m$
   308^I^I^IObjects/exceptions.o [33m\[39;49;00m$
   309^I^I^IObjects/genobject.o [33m\[39;49;00m$
   310^I^I^IObjects/fileobject.o [33m\[39;49;00m$
   311^I^I^IObjects/floatobject.o [33m\[39;49;00m$
   312^I^I^IObjects/frameobject.o [33m\[39;49;00m$
   313^I^I^IObjects/funcobject.o [33m\[39;49;00m$
   314^I^I^IObjects/intobject.o [33m\[39;49;00m$
   315^I^I^IObjects/iterobject.o [33m\[39;49;00m$
   316^I^I^IObjects/listobject.o [33m\[39;49;00m$
   317^I^I^IObjects/longobject.o [33m\[39;49;00m$
   318^I^I^IObjects/dictobject.o [33m\[39;49;00m$
   319^I^I^IObjects/methodobject.o [33m\[39;49;00m$
   320^I^I^IObjects/moduleobject.o [33m\[39;49;00m$
   321^I^I^IObjects/object.o [33m\[39;49;00m$
   322^I^I^IObjects/obmalloc.o [33m\[39;49;00m$
   323^I^I^IObjects/rangeobject.o [33m\[39;49;00m$
   324^I                Objects/setobject.o [33m\[39;49;00m$
   325^I^I^IObjects/sliceobject.o [33m\[39;49;00m$
   326^I^I^IObjects/stringobject.o [33m\[39;49;00m$
   327^I^I^IObjects/structseq.o [33m\[39;49;00m$
   328^I^I^IObjects/tupleobject.o [33m\[39;49;00m$
   329^I^I^IObjects/typeobject.o [33m\[39;49;00m$
   330^I^I^IObjects/weakrefobject.o [33m\[39;49;00m$
   331^I^I^I[34m$([39;49;00mUNICODE_OBJS[34m)[39;49;00m$
   332^I$
   333^I$
   334^I[37m##########################################################################[39;49;00m$
   335^I[37m# objects that get linked into the Python library[39;49;00m$
   336^I[31mLIBRARY_OBJS[39;49;00m=^I[33m\[39;49;00m$
   337^I^I^IModules/_typesmodule.o [33m\[39;49;00m$
   338^I^I^IModules/getbuildinfo.o [33m\[39;49;00m$
   339^I^I^I[34m$([39;49;00mPARSER_OBJS[34m)[39;49;00m [33m\[39;49;00m$
   340^I^I^I[34m$([39;49;00mOBJECT_OBJS[34m)[39;49;00m [33m\[39;49;00m$
   341^I^I^I[34m$([39;49;00mPYTHON_OBJS[34m)[39;49;00m [33m\[39;49;00m$
   342^I^I^I[34m$([39;49;00mMODULE_OBJS[34m)[39;49;00m [33m\[39;49;00m$
   343^I^I^I[34m$([39;49;00mSIGNAL_OBJS[34m)[39;49;00m [33m\[39;49;00m$
   344^I^I^I[34m$([39;49;00mMODOBJS[34m)[39;49;00m$
   345^I$
   346^I[37m#########################################################################[39;49;00m$
   347^I[37m# Rules[39;49;00m$
   348^I$
   349^I[37m# Default target[39;49;00m$
   350^I[32mall[39;49;00m:^I^I[34m$([39;49;00m[31mBUILDPYTHON[39;49;00m[34m)[39;49;00m oldsharedmods sharedmods$
   351^I$
   352^I[37m# Build the interpreter[39;49;00m$
   353^I[32m$(BUILDPYTHON)[39;49;00m:^IModules/python.o [34m$([39;49;00m[31mLIBRARY[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31mLDLIBRARY[39;49;00m[34m)[39;49;00m$
   354^I^I^I[34m$([39;49;00mLINKCC[34m)[39;49;00m [34m$([39;49;00mLDFLAGS[34m)[39;49;00m [34m$([39;49;00mLINKFORSHARED[34m)[39;49;00m -o [31m$@[39;49;00m [33m\[39;49;00m$
   355^I^I^I^IModules/python.o [33m\[39;49;00m$
   356^I^I^I^I[34m$([39;49;00mBLDLIBRARY[34m)[39;49;00m [34m$([39;49;00mLIBS[34m)[39;49;00m [34m$([39;49;00mMODLIBS[34m)[39;49;00m [34m$([39;49;00mSYSLIBS[34m)[39;49;00m [34m$([39;49;00mLDLAST[34m)[39;49;00m$
   357^I$
   358^I[32mplatform[39;49;00m: [34m$([39;49;00m[31mBUILDPYTHON[39;49;00m[34m)[39;49;00m$
   359^I^I[34m$([39;49;00mRUNSHARED[34m)[39;49;00m ./[34m$([39;49;00mBUILDPYTHON[34m)[39;49;00m -E -c [33m'import sys ; from distutils.util import get_platform ; print get_platform()+"-"+sys.version[0:3]'[39;49;00m >platform$
   360^I$
   361^I$
   362^I[37m# Build the shared modules[39;49;00m$
   363^I[32msharedmods[39;49;00m: [34m$([39;49;00m[31mBUILDPYTHON[39;49;00m[34m)[39;49;00m$
   364^I^I@case [31m$$[39;49;00mMAKEFLAGS [34min[39;49;00m [33m\[39;49;00m$
   365^I^I*-s*) [34m$([39;49;00mRUNSHARED[34m)[39;49;00m [31mCC[39;49;00m=[33m'$(CC)'[39;49;00m [31mLDSHARED[39;49;00m=[33m'$(BLDSHARED)'[39;49;00m [31mOPT[39;49;00m=[33m'$(OPT)'[39;49;00m ./[34m$([39;49;00mBUILDPYTHON[34m)[39;49;00m -E [34m$([39;49;00msrcdir[34m)[39;49;00m/setup.py -q build;; [33m\[39;49;00m$
   366^I^I*) [34m$([39;49;00mRUNSHARED[34m)[39;49;00m [31mCC[39;49;00m=[33m'$(CC)'[39;49;00m [31mLDSHARED[39;49;00m=[33m'$(BLDSHARED)'[39;49;00m [31mOPT[39;49;00m=[33m'$(OPT)'[39;49;00m ./[34m$([39;49;00mBUILDPYTHON[34m)[39;49;00m -E [34m$([39;49;00msrcdir[34m)[39;49;00m/setup.py build;; [33m\[39;49;00m$
   367^I^I[34mesac[39;49;00m$
   368^I$
   369^I[37m# Build static library[39;49;00m$
   370^I[37m# avoid long command lines, same as LIBRARY_OBJS[39;49;00m$
   371^I[32m$(LIBRARY)[39;49;00m: [34m$([39;49;00m[31mLIBRARY_OBJS[39;49;00m[34m)[39;49;00m$
   372^I^I-rm -f [31m$@[39;49;00m$
   373^I^I[34m$([39;49;00mAR[34m)[39;49;00m cr [31m$@[39;49;00m Modules/getbuildinfo.o$
   374^I^I[34m$([39;49;00mAR[34m)[39;49;00m cr [31m$@[39;49;00m Modules/_typesmodule.o$
   375^I^I[34m$([39;49;00mAR[34m)[39;49;00m cr [31m$@[39;49;00m [34m$([39;49;00mPARSER_OBJS[34m)[39;49;00m$
   376^I^I[34m$([39;49;00mAR[34m)[39;49;00m cr [31m$@[39;49;00m [34m$([39;49;00mOBJECT_OBJS[34m)[39;49;00m$
   377^I^I[34m$([39;49;00mAR[34m)[39;49;00m cr [31m$@[39;49;00m [34m$([39;49;00mPYTHON_OBJS[34m)[39;49;00m$
   378^I^I[34m$([39;49;00mAR[34m)[39;49;00m cr [31m$@[39;49;00m [34m$([39;49;00mMODULE_OBJS[34m)[39;49;00m [34m$([39;49;00mSIGNAL_OBJS[34m)[39;49;00m$
   379^I^I[34m$([39;49;00mAR[34m)[39;49;00m cr [31m$@[39;49;00m [34m$([39;49;00mMODOBJS[34m)[39;49;00m$
   380^I^I[34m$([39;49;00mRANLIB[34m)[39;49;00m [31m$@[39;49;00m$
   381^I$
   382^I[32mlibpython$(VERSION).so[39;49;00m: [34m$([39;49;00m[31mLIBRARY_OBJS[39;49;00m[34m)[39;49;00m$
   383^I[36m^Iif test $(INSTSONAME) != $(LDLIBRARY); then \[39;49;00m$
   384^I[36m^I^I$(LDSHARED) -Wl,-h$(INSTSONAME) -o $(INSTSONAME) $(LIBRARY_OBJS) $(SHLIBS) $(LIBC) $(LIBM); \[39;49;00m$
   385^I[36m^I^I$(LN) -f $(INSTSONAME) $@; \[39;49;00m$
   386^I[36m^Ielse\[39;49;00m$
   387^I[36m^I^I$(LDSHARED) -o $@ $(LIBRARY_OBJS) $(SHLIBS) $(LIBC) $(LIBM); \[39;49;00m$
   388^I[36m^Ifi[39;49;00m$
   389^I$
   390^I[32mlibpython$(VERSION).sl[39;49;00m: [34m$([39;49;00m[31mLIBRARY_OBJS[39;49;00m[34m)[39;49;00m$
   391^I^I[34m$([39;49;00mLDSHARED[34m)[39;49;00m -o [31m$@[39;49;00m [34m$([39;49;00mLIBRARY_OBJS[34m)[39;49;00m [34m$([39;49;00mSHLIBS[34m)[39;49;00m [34m$([39;49;00mLIBC[34m)[39;49;00m [34m$([39;49;00mLIBM[34m)[39;49;00m$
   392^I$
   393^I[37m# This rule is here for OPENSTEP/Rhapsody/MacOSX. It builds a temporary[39;49;00m$
   394^I[37m# minimal framework (not including the Lib directory and such) in the current[39;49;00m$
   395^I[37m# directory.[39;49;00m$
   396^I[31mRESSRCDIR[39;49;00m=[34m$([39;49;00msrcdir[34m)[39;49;00m/Mac/Resources/framework$
   397^I[32m$(PYTHONFRAMEWORKDIR)/Versions/$(VERSION)/$(PYTHONFRAMEWORK)[39;49;00m: \$
   398^I^I^I[34m$([39;49;00m[31mLIBRARY[39;49;00m[34m)[39;49;00m \$
   399^I^I^I[34m$([39;49;00m[31mRESSRCDIR[39;49;00m[34m)[39;49;00m/Info.plist \$
   400^I                [34m$([39;49;00m[31mRESSRCDIR[39;49;00m[34m)[39;49;00m/version.plist \$
   401^I                [34m$([39;49;00m[31mRESSRCDIR[39;49;00m[34m)[39;49;00m/English.lproj/InfoPlist.strings$
   402^I^I[34m$([39;49;00mINSTALL[34m)[39;49;00m -d -m [34m$([39;49;00mDIRMODE[34m)[39;49;00m [34m$([39;49;00mPYTHONFRAMEWORKDIR[34m)[39;49;00m/Versions/[34m$([39;49;00mVERSION[34m)[39;49;00m$
   403^I[36m^Iif test "${UNIVERSALSDK}"; then \[39;49;00m$
   404^I[36m^I^I$(CC) -o $(LDLIBRARY) -arch i386 -arch ppc -dynamiclib \[39;49;00m$
   405^I[36m^I^I^I-isysroot "${UNIVERSALSDK}" \[39;49;00m$
   406^I[36m^I^I^I-all_load $(LIBRARY) -Wl,-single_module \[39;49;00m$
   407^I[36m^I^I^I-install_name $(DESTDIR)$(PYTHONFRAMEWORKINSTALLDIR)/Versions/$(VERSION)/Python \[39;49;00m$
   408^I[36m^I^I^I-compatibility_version $(VERSION) \[39;49;00m$
   409^I[36m^I^I^I-current_version $(VERSION); \[39;49;00m$
   410^I[36m        else \[39;49;00m$
   411^I[36m^I^Ilibtool -o $(LDLIBRARY) -dynamic $(OTHER_LIBTOOL_OPT) $(LIBRARY) \[39;49;00m$
   412^I[36m^I^I^I ;\[39;49;00m$
   413^I[36m^Ifi[39;49;00m$
   414^I^I[34m$([39;49;00mINSTALL[34m)[39;49;00m -d -m [34m$([39;49;00mDIRMODE[34m)[39;49;00m  [33m\[39;49;00m$
   415^I^I^I[34m$([39;49;00mPYTHONFRAMEWORKDIR[34m)[39;49;00m/Versions/[34m$([39;49;00mVERSION[34m)[39;49;00m/Resources/English.lproj$
   416^I^I[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m [34m$([39;49;00mRESSRCDIR[34m)[39;49;00m/Info.plist [33m\[39;49;00m$
   417^I^I^I[34m$([39;49;00mPYTHONFRAMEWORKDIR[34m)[39;49;00m/Versions/[34m$([39;49;00mVERSION[34m)[39;49;00m/Resources/Info.plist$
   418^I^I[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m [34m$([39;49;00mRESSRCDIR[34m)[39;49;00m/version.plist [33m\[39;49;00m$
   419^I^I^I[34m$([39;49;00mPYTHONFRAMEWORKDIR[34m)[39;49;00m/Versions/[34m$([39;49;00mVERSION[34m)[39;49;00m/Resources/version.plist$
   420^I^I[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m [34m$([39;49;00mRESSRCDIR[34m)[39;49;00m/English.lproj/InfoPlist.strings [33m\[39;49;00m$
   421^I^I^I[34m$([39;49;00mPYTHONFRAMEWORKDIR[34m)[39;49;00m/Versions/[34m$([39;49;00mVERSION[34m)[39;49;00m/Resources/English.lproj/InfoPlist.strings$
   422^I^I[34m$([39;49;00mLN[34m)[39;49;00m -fsn [34m$([39;49;00mVERSION[34m)[39;49;00m [34m$([39;49;00mPYTHONFRAMEWORKDIR[34m)[39;49;00m/Versions/Current$
   423^I^I[34m$([39;49;00mLN[34m)[39;49;00m -fsn Versions/Current/[34m$([39;49;00mPYTHONFRAMEWORK[34m)[39;49;00m [34m$([39;49;00mPYTHONFRAMEWORKDIR[34m)[39;49;00m/[34m$([39;49;00mPYTHONFRAMEWORK[34m)[39;49;00m$
   424^I^I[34m$([39;49;00mLN[34m)[39;49;00m -fsn Versions/Current/Headers [34m$([39;49;00mPYTHONFRAMEWORKDIR[34m)[39;49;00m/Headers$
   425^I^I[34m$([39;49;00mLN[34m)[39;49;00m -fsn Versions/Current/Resources [34m$([39;49;00mPYTHONFRAMEWORKDIR[34m)[39;49;00m/Resources$
   426^I$
   427^I[37m# This rule builds the Cygwin Python DLL and import library if configured[39;49;00m$
   428^I[37m# for a shared core library; otherwise, this rule is a noop.[39;49;00m$
   429^I[32m$(DLLLIBRARY) libpython$(VERSION).dll.a[39;49;00m: [34m$([39;49;00m[31mLIBRARY_OBJS[39;49;00m[34m)[39;49;00m$
   430^I[36m^Iif test -n "$(DLLLIBRARY)"; then \[39;49;00m$
   431^I[36m^I^I$(LDSHARED) -Wl,--out-implib=$@ -o $(DLLLIBRARY) $^ \[39;49;00m$
   432^I[36m^I^I^I$(LIBS) $(MODLIBS) $(SYSLIBS); \[39;49;00m$
   433^I[36m^Ielse true; \[39;49;00m$
   434^I[36m^Ifi[39;49;00m$
   435^I$
   436^I$
   437^I[32moldsharedmods[39;49;00m: [34m$([39;49;00m[31mSHAREDMODS[39;49;00m[34m)[39;49;00m$
   438^I$
   439^I$
   440^I[32mMakefile Modules/config.c[39;49;00m: Makefile.pre \$
   441^I^I^I^I^I[34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/config.c.in \$
   442^I^I^I^I^I[34m$([39;49;00m[31mMAKESETUP[39;49;00m[34m)[39;49;00m \$
   443^I^I^I^I^IModules/Setup.config \$
   444^I^I^I^I^IModules/Setup \$
   445^I^I^I^I^IModules/Setup.local$
   446^I^I[34m$([39;49;00mSHELL[34m)[39;49;00m [34m$([39;49;00mMAKESETUP[34m)[39;49;00m -c [34m$([39;49;00msrcdir[34m)[39;49;00m/Modules/config.c.in [33m\[39;49;00m$
   447^I^I^I^I^I-s Modules [33m\[39;49;00m$
   448^I^I^I^I^IModules/Setup.config [33m\[39;49;00m$
   449^I^I^I^I^IModules/Setup.local [33m\[39;49;00m$
   450^I^I^I^I^IModules/Setup$
   451^I^I@mv config.c Modules$
   452^I^I@echo [33m"The Makefile was updated, you may need to re-run make."[39;49;00m$
   453^I$
   454^I$
   455^I[32mModules/Setup[39;49;00m: [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/Setup.dist$
   456^I^I@if [36mtest[39;49;00m -f Modules/Setup; [34mthen[39;49;00m [33m\[39;49;00m$
   457^I^I^I[36mecho[39;49;00m [33m"-----------------------------------------------"[39;49;00m; [33m\[39;49;00m$
   458^I^I^I[36mecho[39;49;00m [33m"Modules/Setup.dist is newer than Modules/Setup;"[39;49;00m; [33m\[39;49;00m$
   459^I^I^I[36mecho[39;49;00m [33m"check to make sure you have all the updates you"[39;49;00m; [33m\[39;49;00m$
   460^I^I^I[36mecho[39;49;00m [33m"need in your Modules/Setup file."[39;49;00m; [33m\[39;49;00m$
   461^I^I^I[36mecho[39;49;00m [33m"Usually, copying Setup.dist to Setup will work."[39;49;00m; [33m\[39;49;00m$
   462^I^I^I[36mecho[39;49;00m [33m"-----------------------------------------------"[39;49;00m; [33m\[39;49;00m$
   463^I^I[34mfi[39;49;00m$
   464^I$
   465^I[37m############################################################################[39;49;00m$
   466^I[37m# Special rules for object files[39;49;00m$
   467^I$
   468^I[32mModules/getbuildinfo.o[39;49;00m: [34m$([39;49;00m[31mPARSER_OBJS[39;49;00m[34m)[39;49;00m \$
   469^I^I^I[34m$([39;49;00m[31mOBJECT_OBJS[39;49;00m[34m)[39;49;00m \$
   470^I^I^I[34m$([39;49;00m[31mPYTHON_OBJS[39;49;00m[34m)[39;49;00m \$
   471^I^I^I[34m$([39;49;00m[31mMODULE_OBJS[39;49;00m[34m)[39;49;00m \$
   472^I^I^I[34m$([39;49;00m[31mSIGNAL_OBJS[39;49;00m[34m)[39;49;00m \$
   473^I^I^I[34m$([39;49;00m[31mMODOBJS[39;49;00m[34m)[39;49;00m \$
   474^I^I^I[34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/getbuildinfo.c$
   475^I^I[34m$([39;49;00mCC[34m)[39;49;00m -c [34m$([39;49;00mPY_CFLAGS[34m)[39;49;00m -DSVNVERSION=[33m\"[39;49;00m[33m`[39;49;00m[31mLC_ALL[39;49;00m=C [34m$([39;49;00mSVNVERSION[34m)[39;49;00m[33m`[39;49;00m[33m\"[39;49;00m -o [31m$@[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/Modules/getbuildinfo.c$
   476^I$
   477^I[32mModules/getpath.o[39;49;00m: [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/getpath.c Makefile$
   478^I^I[34m$([39;49;00mCC[34m)[39;49;00m -c [34m$([39;49;00mPY_CFLAGS[34m)[39;49;00m -DPYTHONPATH=[33m'"$(PYTHONPATH)"'[39;49;00m [33m\[39;49;00m$
   479^I^I^I-DPREFIX=[33m'"$(prefix)"'[39;49;00m [33m\[39;49;00m$
   480^I^I^I-DEXEC_PREFIX=[33m'"$(exec_prefix)"'[39;49;00m [33m\[39;49;00m$
   481^I^I^I-DVERSION=[33m'"$(VERSION)"'[39;49;00m [33m\[39;49;00m$
   482^I^I^I-DVPATH=[33m'"$(VPATH)"'[39;49;00m [33m\[39;49;00m$
   483^I^I^I-o [31m$@[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/Modules/getpath.c$
   484^I$
   485^I[32mModules/python.o[39;49;00m: [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/python.c$
   486^I^I[34m$([39;49;00mMAINCC[34m)[39;49;00m -c [34m$([39;49;00mPY_CFLAGS[34m)[39;49;00m -o [31m$@[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/Modules/python.c$
   487^I$
   488^I$
   489^I[32m$(GRAMMAR_H) $(GRAMMAR_C)[39;49;00m: [34m$([39;49;00m[31mPGEN[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31mGRAMMAR_INPUT[39;49;00m[34m)[39;49;00m$
   490^I^I^I-[34m$([39;49;00mPGEN[34m)[39;49;00m [34m$([39;49;00mGRAMMAR_INPUT[34m)[39;49;00m [34m$([39;49;00mGRAMMAR_H[34m)[39;49;00m [34m$([39;49;00mGRAMMAR_C[34m)[39;49;00m$
   491^I$
   492^I[32m$(PGEN)[39;49;00m:^I[34m$([39;49;00m[31mPGENOBJS[39;49;00m[34m)[39;49;00m$
   493^I^I^I[34m$([39;49;00mCC[34m)[39;49;00m [34m$([39;49;00mOPT[34m)[39;49;00m [34m$([39;49;00mLDFLAGS[34m)[39;49;00m [34m$([39;49;00mPGENOBJS[34m)[39;49;00m [34m$([39;49;00mLIBS[34m)[39;49;00m -o [34m$([39;49;00mPGEN[34m)[39;49;00m$
   494^I$
   495^I[32mParser/grammar.o[39;49;00m:^I[34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Parser/grammar.c \$
   496^I^I^I^I^I[34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Include/token.h \$
   497^I^I^I^I^I[34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Include/grammar.h$
   498^I[32mParser/metagrammar.o[39;49;00m:^I[34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Parser/metagrammar.c$
   499^I$
   500^I[32mParser/tokenizer_pgen.o[39;49;00m:^I[34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Parser/tokenizer.c$
   501^I$
   502^I[32mParser/pgenmain.o[39;49;00m:^I[34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Include/parsetok.h$
   503^I$
   504^I[32m$(AST_H)[39;49;00m: [34m$([39;49;00m[31mAST_ASDL[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31mASDLGEN_FILES[39;49;00m[34m)[39;49;00m$
   505^I^I[34m$([39;49;00mASDLGEN[34m)[39;49;00m -h [34m$([39;49;00mAST_H_DIR[34m)[39;49;00m [34m$([39;49;00mAST_ASDL[34m)[39;49;00m$
   506^I$
   507^I[32m$(AST_C)[39;49;00m: [34m$([39;49;00m[31mAST_ASDL[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31mASDLGEN_FILES[39;49;00m[34m)[39;49;00m$
   508^I^I[34m$([39;49;00mASDLGEN[34m)[39;49;00m -c [34m$([39;49;00mAST_C_DIR[34m)[39;49;00m [34m$([39;49;00mAST_ASDL[34m)[39;49;00m$
   509^I$
   510^I[32mPython/compile.o Python/symtable.o[39;49;00m: [34m$([39;49;00m[31mGRAMMAR_H[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31mAST_H[39;49;00m[34m)[39;49;00m$
   511^I$
   512^I[32mPython/getplatform.o[39;49;00m: [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Python/getplatform.c$
   513^I^I^I[34m$([39;49;00mCC[34m)[39;49;00m -c [34m$([39;49;00mPY_CFLAGS[34m)[39;49;00m -DPLATFORM=[33m'"$(MACHDEP)"'[39;49;00m -o [31m$@[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/Python/getplatform.c$
   514^I$
   515^I[32mPython/importdl.o[39;49;00m: [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Python/importdl.c$
   516^I^I^I[34m$([39;49;00mCC[34m)[39;49;00m -c [34m$([39;49;00mPY_CFLAGS[34m)[39;49;00m -I[34m$([39;49;00mDLINCLDIR[34m)[39;49;00m -o [31m$@[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/Python/importdl.c$
   517^I$
   518^I[32mObjects/unicodectype.o[39;49;00m:^I[34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Objects/unicodectype.c \$
   519^I^I^I^I^I[34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Objects/unicodetype_db.h$
   520^I$
   521^I[37m############################################################################[39;49;00m$
   522^I[37m# Header files[39;49;00m$
   523^I$
   524^I[31mPYTHON_HEADERS[39;49;00m= [33m\[39;49;00m$
   525^I^I^IInclude/Python.h [33m\[39;49;00m$
   526^I^I^IInclude/Python-ast.h [33m\[39;49;00m$
   527^I^I^IInclude/asdl.h [33m\[39;49;00m$
   528^I^I^IInclude/abstract.h [33m\[39;49;00m$
   529^I^I^IInclude/boolobject.h [33m\[39;49;00m$
   530^I^I^IInclude/bufferobject.h [33m\[39;49;00m$
   531^I^I^IInclude/ceval.h [33m\[39;49;00m$
   532^I^I^IInclude/classobject.h [33m\[39;49;00m$
   533^I^I^IInclude/cobject.h [33m\[39;49;00m$
   534^I^I^IInclude/code.h [33m\[39;49;00m$
   535^I^I^IInclude/codecs.h [33m\[39;49;00m$
   536^I^I^IInclude/compile.h [33m\[39;49;00m$
   537^I^I^IInclude/complexobject.h [33m\[39;49;00m$
   538^I^I^IInclude/descrobject.h [33m\[39;49;00m$
   539^I^I^IInclude/dictobject.h [33m\[39;49;00m$
   540^I^I^IInclude/enumobject.h [33m\[39;49;00m$
   541^I^I^IInclude/genobject.h [33m\[39;49;00m$
   542^I^I^IInclude/fileobject.h [33m\[39;49;00m$
   543^I^I^IInclude/floatobject.h [33m\[39;49;00m$
   544^I^I^IInclude/funcobject.h [33m\[39;49;00m$
   545^I^I^IInclude/import.h [33m\[39;49;00m$
   546^I^I^IInclude/intobject.h [33m\[39;49;00m$
   547^I^I^IInclude/intrcheck.h [33m\[39;49;00m$
   548^I^I^IInclude/iterobject.h [33m\[39;49;00m$
   549^I^I^IInclude/listobject.h [33m\[39;49;00m$
   550^I^I^IInclude/longobject.h [33m\[39;49;00m$
   551^I^I^IInclude/methodobject.h [33m\[39;49;00m$
   552^I^I^IInclude/modsupport.h [33m\[39;49;00m$
   553^I^I^IInclude/moduleobject.h [33m\[39;49;00m$
   554^I^I^IInclude/object.h [33m\[39;49;00m$
   555^I^I^IInclude/objimpl.h [33m\[39;49;00m$
   556^I^I^IInclude/parsetok.h [33m\[39;49;00m$
   557^I^I^IInclude/patchlevel.h [33m\[39;49;00m$
   558^I^I^IInclude/pyarena.h [33m\[39;49;00m$
   559^I^I^IInclude/pydebug.h [33m\[39;49;00m$
   560^I^I^IInclude/pyerrors.h [33m\[39;49;00m$
   561^I^I^IInclude/pyfpe.h [33m\[39;49;00m$
   562^I^I^IInclude/pymem.h [33m\[39;49;00m$
   563^I^I^IInclude/pyport.h [33m\[39;49;00m$
   564^I^I^IInclude/pystate.h [33m\[39;49;00m$
   565^I^I^IInclude/pythonrun.h [33m\[39;49;00m$
   566^I^I^IInclude/rangeobject.h [33m\[39;49;00m$
   567^I                Include/setobject.h [33m\[39;49;00m$
   568^I^I^IInclude/sliceobject.h [33m\[39;49;00m$
   569^I^I^IInclude/stringobject.h [33m\[39;49;00m$
   570^I^I^IInclude/structseq.h [33m\[39;49;00m$
   571^I^I^IInclude/structmember.h [33m\[39;49;00m$
   572^I^I^IInclude/symtable.h [33m\[39;49;00m$
   573^I^I^IInclude/sysmodule.h [33m\[39;49;00m$
   574^I^I^IInclude/traceback.h [33m\[39;49;00m$
   575^I^I^IInclude/tupleobject.h [33m\[39;49;00m$
   576^I^I^IInclude/unicodeobject.h [33m\[39;49;00m$
   577^I^I^IInclude/weakrefobject.h [33m\[39;49;00m$
   578^I^I^Ipyconfig.h$
   579^I$
   580^I[32m$(LIBRARY_OBJS) $(MODOBJS) Modules/python.o[39;49;00m: [34m$([39;49;00m[31mPYTHON_HEADERS[39;49;00m[34m)[39;49;00m$
   581^I$
   582^I$
   583^I[37m######################################################################[39;49;00m$
   584^I$
   585^I[37m# Test the interpreter (twice, once without .pyc files, once with)[39;49;00m$
   586^I[37m# In the past, we've had problems where bugs in the marshalling or[39;49;00m$
   587^I[37m# elsewhere caused bytecode read from .pyc files to behave differently[39;49;00m$
   588^I[37m# than bytecode generated directly from a .py source file.  Sometimes[39;49;00m$
   589^I[37m# the bytecode read from a .pyc file had the bug, somtimes the directly[39;49;00m$
   590^I[37m# generated bytecode.  This is sometimes a very shy bug needing a lot of[39;49;00m$
   591^I[37m# sample data.[39;49;00m$
   592^I$
   593^I[31mTESTOPTS[39;49;00m=^I-l [34m$([39;49;00mEXTRATESTOPTS[34m)[39;49;00m$
   594^I[31mTESTPROG[39;49;00m=^I[34m$([39;49;00msrcdir[34m)[39;49;00m/Lib/test/regrtest.py$
   595^I[31mTESTPYTHON[39;49;00m=^I[34m$([39;49;00mRUNSHARED[34m)[39;49;00m ./[34m$([39;49;00mBUILDPYTHON[34m)[39;49;00m -E -tt$
   596^I[32mtest[39;49;00m:^I^Iall platform$
   597^I^I^I-find [34m$([39;49;00msrcdir[34m)[39;49;00m/Lib -name [33m'*.py[co]'[39;49;00m -print | xargs rm -f$
   598^I^I^I-[34m$([39;49;00mTESTPYTHON[34m)[39;49;00m [34m$([39;49;00mTESTPROG[34m)[39;49;00m [34m$([39;49;00mTESTOPTS[34m)[39;49;00m$
   599^I^I^I[34m$([39;49;00mTESTPYTHON[34m)[39;49;00m [34m$([39;49;00mTESTPROG[34m)[39;49;00m [34m$([39;49;00mTESTOPTS[34m)[39;49;00m$
   600^I$
   601^I[32mtestall[39;49;00m:^Iall platform$
   602^I^I^I-find [34m$([39;49;00msrcdir[34m)[39;49;00m/Lib -name [33m'*.py[co]'[39;49;00m -print | xargs rm -f$
   603^I^I^I-[34m$([39;49;00mTESTPYTHON[34m)[39;49;00m [34m$([39;49;00mTESTPROG[34m)[39;49;00m [34m$([39;49;00mTESTOPTS[34m)[39;49;00m -uall$
   604^I^I^I[34m$([39;49;00mTESTPYTHON[34m)[39;49;00m [34m$([39;49;00mTESTPROG[34m)[39;49;00m [34m$([39;49;00mTESTOPTS[34m)[39;49;00m -uall$
   605^I$
   606^I[37m#  Run the unitests for both architectures in a Universal build on OSX[39;49;00m$
   607^I[37m#  Must be run on an Intel box.[39;49;00m$
   608^I[32mtestuniversal[39;49;00m:^Iall platform$
   609^I[36m^I^Iif [ `arch` != 'i386' ];then \[39;49;00m$
   610^I[36m^I^I^Iecho "This can only be used on OSX/i386" ;\[39;49;00m$
   611^I[36m^I^I^Iexit 1 ;\[39;49;00m$
   612^I[36m^I^Ifi[39;49;00m$
   613^I^I^I-find [34m$([39;49;00msrcdir[34m)[39;49;00m/Lib -name [33m'*.py[co]'[39;49;00m -print | xargs rm -f$
   614^I^I^I-[34m$([39;49;00mTESTPYTHON[34m)[39;49;00m [34m$([39;49;00mTESTPROG[34m)[39;49;00m [34m$([39;49;00mTESTOPTS[34m)[39;49;00m -uall$
   615^I^I^I[34m$([39;49;00mTESTPYTHON[34m)[39;49;00m [34m$([39;49;00mTESTPROG[34m)[39;49;00m [34m$([39;49;00mTESTOPTS[34m)[39;49;00m -uall$
   616^I^I^I[34m$([39;49;00mRUNSHARED[34m)[39;49;00m /usr/libexec/oah/translate ./[34m$([39;49;00mBUILDPYTHON[34m)[39;49;00m -E -tt [34m$([39;49;00mTESTPROG[34m)[39;49;00m [34m$([39;49;00mTESTOPTS[34m)[39;49;00m -uall$
   617^I$
   618^I$
   619^I[37m# Like testall, but with a single pass only[39;49;00m$
   620^I[32mbuildbottest[39;49;00m:^Iall platform$
   621^I^I^I[34m$([39;49;00mTESTPYTHON[34m)[39;49;00m [34m$([39;49;00mTESTPROG[34m)[39;49;00m [34m$([39;49;00mTESTOPTS[34m)[39;49;00m -uall -rw$
   622^I$
   623^I[31mQUICKTESTOPTS[39;49;00m=^I[34m$([39;49;00mTESTOPTS[34m)[39;49;00m -x test_thread test_signal test_strftime [33m\[39;49;00m$
   624^I^I^Itest_unicodedata test_re test_sre test_select test_poll [33m\[39;49;00m$
   625^I^I^Itest_linuxaudiodev test_struct test_sunaudiodev test_zlib$
   626^I[32mquicktest[39;49;00m:^Iall platform$
   627^I^I^I-find [34m$([39;49;00msrcdir[34m)[39;49;00m/Lib -name [33m'*.py[co]'[39;49;00m -print | xargs rm -f$
   628^I^I^I-[34m$([39;49;00mTESTPYTHON[34m)[39;49;00m [34m$([39;49;00mTESTPROG[34m)[39;49;00m [34m$([39;49;00mQUICKTESTOPTS[34m)[39;49;00m$
   629^I^I^I[34m$([39;49;00mTESTPYTHON[34m)[39;49;00m [34m$([39;49;00mTESTPROG[34m)[39;49;00m [34m$([39;49;00mQUICKTESTOPTS[34m)[39;49;00m$
   630^I$
   631^I[31mMEMTESTOPTS[39;49;00m=    [34m$([39;49;00mQUICKTESTOPTS[34m)[39;49;00m -x test_dl test___all__ test_fork1 [33m\[39;49;00m$
   632^I^I^Itest_longexp$
   633^I[32mmemtest[39;49;00m:^Iall platform$
   634^I^I^I-rm -f [34m$([39;49;00msrcdir[34m)[39;49;00m/Lib/test/*.py[co]$
   635^I^I^I-[34m$([39;49;00mTESTPYTHON[34m)[39;49;00m [34m$([39;49;00mTESTPROG[34m)[39;49;00m [34m$([39;49;00mMEMTESTOPTS[34m)[39;49;00m$
   636^I^I^I[34m$([39;49;00mTESTPYTHON[34m)[39;49;00m [34m$([39;49;00mTESTPROG[34m)[39;49;00m [34m$([39;49;00mMEMTESTOPTS[34m)[39;49;00m$
   637^I$
   638^I[37m# Install everything[39;49;00m$
   639^I[32minstall[39;49;00m:^I altinstall bininstall maninstall $
   640^I$
   641^I[37m# Install almost everything without disturbing previous versions[39;49;00m$
   642^I[32maltinstall[39;49;00m:^I altbininstall libinstall inclinstall libainstall \$
   643^I                sharedinstall oldsharedinstall $
   644^I$
   645^I[37m# Install shared libraries enabled by Setup[39;49;00m$
   646^I[31mDESTDIRS[39;49;00m=^I[34m$([39;49;00mexec_prefix[34m)[39;49;00m [34m$([39;49;00mLIBDIR[34m)[39;49;00m [34m$([39;49;00mBINLIBDEST[34m)[39;49;00m [34m$([39;49;00mDESTSHARED[34m)[39;49;00m$
   647^I$
   648^I[32moldsharedinstall[39;49;00m: [34m$([39;49;00m[31mDESTSHARED[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31mSHAREDMODS[39;49;00m[34m)[39;49;00m$
   649^I^I^I@for i [34min[39;49;00m X [34m$([39;49;00mSHAREDMODS[34m)[39;49;00m; [34mdo[39;49;00m [33m\[39;49;00m$
   650^I[36m^I^I  if test $$i != X; then \[39;49;00m$
   651^I[36m^I^I    echo $(INSTALL_SHARED) $$i $(DESTSHARED)/`basename $$i`; \[39;49;00m$
   652^I[36m^I^I    $(INSTALL_SHARED) $$i $(DESTDIR)$(DESTSHARED)/`basename $$i`; \[39;49;00m$
   653^I[36m^I^I  fi; \[39;49;00m$
   654^I[36m^I^Idone[39;49;00m$
   655^I$
   656^I[32m$(DESTSHARED)[39;49;00m:$
   657^I^I^I@for i [34min[39;49;00m [34m$([39;49;00mDESTDIRS[34m)[39;49;00m; [33m\[39;49;00m$
   658^I^I^I[34mdo[39;49;00m [33m\[39;49;00m$
   659^I[36m^I^I^Iif test ! -d $(DESTDIR)$$i; then \[39;49;00m$
   660^I[36m^I^I^I^Iecho "Creating directory $$i"; \[39;49;00m$
   661^I[36m^I^I^I^I$(INSTALL) -d -m $(DIRMODE) $(DESTDIR)$$i; \[39;49;00m$
   662^I[36m^I^I^Ielse    true; \[39;49;00m$
   663^I[36m^I^I^Ifi; \[39;49;00m$
   664^I[36m^I^Idone[39;49;00m$
   665^I$
   666^I$
   667^I[37m# Install the interpreter (by creating a hard link to python$(VERSION))[39;49;00m$
   668^I[32mbininstall[39;49;00m:^Ialtbininstall$
   669^I^I-if [36mtest[39;49;00m -f [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mBINDIR[34m)[39;49;00m/[34m$([39;49;00mPYTHON[34m)[39;49;00m -o -h [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mBINDIR[34m)[39;49;00m/[34m$([39;49;00mPYTHON[34m)[39;49;00m; [33m\[39;49;00m$
   670^I^I[34mthen[39;49;00m rm -f [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mBINDIR[34m)[39;49;00m/[34m$([39;49;00mPYTHON[34m)[39;49;00m; [33m\[39;49;00m$
   671^I[36m^Ielse true; \[39;49;00m$
   672^I[36m^Ifi[39;49;00m$
   673^I^I([36mcd[39;49;00m [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mBINDIR[34m)[39;49;00m; [34m$([39;49;00mLN[34m)[39;49;00m python[34m$([39;49;00mVERSION[34m)[39;49;00m[34m$([39;49;00mEXE[34m)[39;49;00m [34m$([39;49;00mPYTHON[34m)[39;49;00m)$
   674^I^I([36mcd[39;49;00m [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mBINDIR[34m)[39;49;00m; [34m$([39;49;00mLN[34m)[39;49;00m -sf python[34m$([39;49;00mVERSION[34m)[39;49;00m-config python-config)$
   675^I$
   676^I[37m# Install the interpreter with $(VERSION) affixed[39;49;00m$
   677^I[37m# This goes into $(exec_prefix)[39;49;00m$
   678^I[32maltbininstall[39;49;00m:^I[34m$([39;49;00m[31mBUILDPYTHON[39;49;00m[34m)[39;49;00m$
   679^I^I@for i [34min[39;49;00m [34m$([39;49;00mBINDIR[34m)[39;49;00m [34m$([39;49;00mLIBDIR[34m)[39;49;00m; [33m\[39;49;00m$
   680^I^I[34mdo[39;49;00m [33m\[39;49;00m$
   681^I[36m^I^Iif test ! -d $(DESTDIR)$$i; then \[39;49;00m$
   682^I[36m^I^I^Iecho "Creating directory $$i"; \[39;49;00m$
   683^I[36m^I^I^I$(INSTALL) -d -m $(DIRMODE) $(DESTDIR)$$i; \[39;49;00m$
   684^I[36m^I^Ielse^Itrue; \[39;49;00m$
   685^I[36m^I^Ifi; \[39;49;00m$
   686^I[36m^Idone[39;49;00m$
   687^I^I[34m$([39;49;00mINSTALL_PROGRAM[34m)[39;49;00m [34m$([39;49;00mBUILDPYTHON[34m)[39;49;00m [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mBINDIR[34m)[39;49;00m/python[34m$([39;49;00mVERSION[34m)[39;49;00m[34m$([39;49;00mEXE[34m)[39;49;00m$
   688^I[36m^Iif test -f libpython$(VERSION)$(SO); then \[39;49;00m$
   689^I[36m^I^Iif test "$(SO)" = .dll; then \[39;49;00m$
   690^I[36m^I^I^I$(INSTALL_SHARED) libpython$(VERSION)$(SO) $(DESTDIR)$(BINDIR); \[39;49;00m$
   691^I[36m^I^Ielse \[39;49;00m$
   692^I[36m^I^I^I$(INSTALL_SHARED) libpython$(VERSION)$(SO) $(DESTDIR)$(LIBDIR)/$(INSTSONAME); \[39;49;00m$
   693^I[36m^I^I^Iif test libpython$(VERSION)$(SO) != $(INSTSONAME); then \[39;49;00m$
   694^I[36m^I^I^I^I(cd $(DESTDIR)$(LIBDIR); $(LN) -sf $(INSTSONAME) libpython$(VERSION)$(SO)); \[39;49;00m$
   695^I[36m^I^I^Ifi \[39;49;00m$
   696^I[36m^I^Ifi; \[39;49;00m$
   697^I[36m^Ielse^Itrue; \[39;49;00m$
   698^I[36m^Ifi[39;49;00m$
   699^I$
   700^I[37m# Install the manual page[39;49;00m$
   701^I[32mmaninstall[39;49;00m:$
   702^I^I@for i [34min[39;49;00m [34m$([39;49;00mMANDIR[34m)[39;49;00m [34m$([39;49;00mMANDIR[34m)[39;49;00m/man1; [33m\[39;49;00m$
   703^I^I[34mdo[39;49;00m [33m\[39;49;00m$
   704^I[36m^I^Iif test ! -d $(DESTDIR)$$i; then \[39;49;00m$
   705^I[36m^I^I^Iecho "Creating directory $$i"; \[39;49;00m$
   706^I[36m^I^I^I$(INSTALL) -d -m $(DIRMODE) $(DESTDIR)$$i; \[39;49;00m$
   707^I[36m^I^Ielse^Itrue; \[39;49;00m$
   708^I[36m^I^Ifi; \[39;49;00m$
   709^I[36m^Idone[39;49;00m$
   710^I^I[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/Misc/python.man [33m\[39;49;00m$
   711^I^I^I[34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mMANDIR[34m)[39;49;00m/man1/python.1$
   712^I$
   713^I[37m# Install the library[39;49;00m$
   714^I[31mPLATDIR[39;49;00m=^Iplat-[34m$([39;49;00mMACHDEP[34m)[39;49;00m$
   715^I[31mEXTRAPLATDIR[39;49;00m= $
   716^I[31mEXTRAMACHDEPPATH[39;49;00m=$
   717^I[31mMACHDEPS[39;49;00m=^I[34m$([39;49;00mPLATDIR[34m)[39;49;00m [34m$([39;49;00mEXTRAPLATDIR[34m)[39;49;00m$
   718^I[31mXMLLIBSUBDIRS[39;49;00m=  xml xml/dom xml/etree xml/parsers xml/sax$
   719^I[31mPLATMACDIRS[39;49;00m= plat-mac plat-mac/Carbon plat-mac/lib-scriptpackages [33m\[39;49;00m$
   720^I^Iplat-mac/lib-scriptpackages/_builtinSuites [33m\[39;49;00m$
   721^I^Iplat-mac/lib-scriptpackages/CodeWarrior [33m\[39;49;00m$
   722^I^Iplat-mac/lib-scriptpackages/Explorer [33m\[39;49;00m$
   723^I^Iplat-mac/lib-scriptpackages/Finder [33m\[39;49;00m$
   724^I^Iplat-mac/lib-scriptpackages/Netscape [33m\[39;49;00m$
   725^I^Iplat-mac/lib-scriptpackages/StdSuites [33m\[39;49;00m$
   726^I^Iplat-mac/lib-scriptpackages/SystemEvents [33m\[39;49;00m$
   727^I^Iplat-mac/lib-scriptpackages/Terminal $
   728^I[31mPLATMACPATH[39;49;00m=:plat-mac:plat-mac/lib-scriptpackages$
   729^I[31mLIBSUBDIRS[39;49;00m=^Ilib-tk site-packages [36mtest[39;49;00m test/output test/data [33m\[39;49;00m$
   730^I^I^Itest/decimaltestdata [33m\[39;49;00m$
   731^I^I^Iencodings compiler hotshot [33m\[39;49;00m$
   732^I^I^Iemail email/mime email/test email/test/data [33m\[39;49;00m$
   733^I^I^Isqlite3 sqlite3/test [33m\[39;49;00m$
   734^I^I^Ilogging bsddb bsddb/test csv wsgiref [33m\[39;49;00m$
   735^I^I^Ictypes ctypes/test ctypes/macholib idlelib idlelib/Icons [33m\[39;49;00m$
   736^I^I^Idistutils distutils/command distutils/tests [34m$([39;49;00mXMLLIBSUBDIRS[34m)[39;49;00m [33m\[39;49;00m$
   737^I^I^Isetuptools setuptools/command setuptools/tests setuptools.egg-info [33m\[39;49;00m$
   738^I^I^Icurses [34m$([39;49;00mMACHDEPS[34m)[39;49;00m$
   739^I[32mlibinstall[39;49;00m:^I[34m$([39;49;00m[31mBUILDPYTHON[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Lib/[34m$([39;49;00m[31mPLATDIR[39;49;00m[34m)[39;49;00m$
   740^I^I@for i [34min[39;49;00m [34m$([39;49;00mSCRIPTDIR[34m)[39;49;00m [34m$([39;49;00mLIBDEST[34m)[39;49;00m; [33m\[39;49;00m$
   741^I^I[34mdo[39;49;00m [33m\[39;49;00m$
   742^I[36m^I^Iif test ! -d $(DESTDIR)$$i; then \[39;49;00m$
   743^I[36m^I^I^Iecho "Creating directory $$i"; \[39;49;00m$
   744^I[36m^I^I^I$(INSTALL) -d -m $(DIRMODE) $(DESTDIR)$$i; \[39;49;00m$
   745^I[36m^I^Ielse^Itrue; \[39;49;00m$
   746^I[36m^I^Ifi; \[39;49;00m$
   747^I[36m^Idone[39;49;00m$
   748^I^I@for d [34min[39;49;00m [34m$([39;49;00mLIBSUBDIRS[34m)[39;49;00m; [33m\[39;49;00m$
   749^I^I[34mdo[39;49;00m [33m\[39;49;00m$
   750^I^I^I[31ma[39;49;00m=[34m$([39;49;00msrcdir[34m)[39;49;00m/Lib/[31m$$[39;49;00md; [33m\[39;49;00m$
   751^I[36m^I^Iif test ! -d $$a; then continue; else true; fi; \[39;49;00m$
   752^I[36m^I^Ib=$(LIBDEST)/$$d; \[39;49;00m$
   753^I[36m^I^Iif test ! -d $(DESTDIR)$$b; then \[39;49;00m$
   754^I[36m^I^I^Iecho "Creating directory $$b"; \[39;49;00m$
   755^I[36m^I^I^I$(INSTALL) -d -m $(DIRMODE) $(DESTDIR)$$b; \[39;49;00m$
   756^I[36m^I^Ielse^Itrue; \[39;49;00m$
   757^I[36m^I^Ifi; \[39;49;00m$
   758^I[36m^Idone[39;49;00m$
   759^I^I@for i [34min[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/Lib/*.py [34m$([39;49;00msrcdir[34m)[39;49;00m/Lib/*.doc [34m$([39;49;00msrcdir[34m)[39;49;00m/Lib/*.egg-info ; [33m\[39;49;00m$
   760^I^I[34mdo[39;49;00m [33m\[39;49;00m$
   761^I[36m^I^Iif test -x $$i; then \[39;49;00m$
   762^I[36m^I^I^I$(INSTALL_SCRIPT) $$i $(DESTDIR)$(LIBDEST); \[39;49;00m$
   763^I[36m^I^I^Iecho $(INSTALL_SCRIPT) $$i $(LIBDEST); \[39;49;00m$
   764^I[36m^I^Ielse \[39;49;00m$
   765^I[36m^I^I^I$(INSTALL_DATA) $$i $(DESTDIR)$(LIBDEST); \[39;49;00m$
   766^I[36m^I^I^Iecho $(INSTALL_DATA) $$i $(LIBDEST); \[39;49;00m$
   767^I[36m^I^Ifi; \[39;49;00m$
   768^I[36m^Idone[39;49;00m$
   769^I^I@for d [34min[39;49;00m [34m$([39;49;00mLIBSUBDIRS[34m)[39;49;00m; [33m\[39;49;00m$
   770^I^I[34mdo[39;49;00m [33m\[39;49;00m$
   771^I^I^I[31ma[39;49;00m=[34m$([39;49;00msrcdir[34m)[39;49;00m/Lib/[31m$$[39;49;00md; [33m\[39;49;00m$
   772^I[36m^I^Iif test ! -d $$a; then continue; else true; fi; \[39;49;00m$
   773^I[36m^I^Iif test `ls $$a | wc -l` -lt 1; then continue; fi; \[39;49;00m$
   774^I[36m^I^Ib=$(LIBDEST)/$$d; \[39;49;00m$
   775^I[36m^I^Ifor i in $$a/*; \[39;49;00m$
   776^I[36m^I^Ido \[39;49;00m$
   777^I[36m^I^I^Icase $$i in \[39;49;00m$
   778^I[36m^I^I^I*CVS) ;; \[39;49;00m$
   779^I[36m^I^I^I*.py[co]) ;; \[39;49;00m$
   780^I[36m^I^I^I*.orig) ;; \[39;49;00m$
   781^I[36m^I^I^I*~) ;; \[39;49;00m$
   782^I[36m^I^I^I*) \[39;49;00m$
   783^I[36m^I^I^I^Iif test -d $$i; then continue; fi; \[39;49;00m$
   784^I[36m^I^I^I^Iif test -x $$i; then \[39;49;00m$
   785^I[36m^I^I^I^I    echo $(INSTALL_SCRIPT) $$i $$b; \[39;49;00m$
   786^I[36m^I^I^I^I    $(INSTALL_SCRIPT) $$i $(DESTDIR)$$b; \[39;49;00m$
   787^I[36m^I^I^I^Ielse \[39;49;00m$
   788^I[36m^I^I^I^I    echo $(INSTALL_DATA) $$i $$b; \[39;49;00m$
   789^I[36m^I^I^I^I    $(INSTALL_DATA) $$i $(DESTDIR)$$b; \[39;49;00m$
   790^I[36m^I^I^I^Ifi;; \[39;49;00m$
   791^I[36m^I^I^Iesac; \[39;49;00m$
   792^I[36m^I^Idone; \[39;49;00m$
   793^I[36m^Idone[39;49;00m$
   794^I^I[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/LICENSE [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBDEST[34m)[39;49;00m/LICENSE.txt$
   795^I^I[31mPYTHONPATH[39;49;00m=[34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBDEST[34m)[39;49;00m  [34m$([39;49;00mRUNSHARED[34m)[39;49;00m [33m\[39;49;00m$
   796^I^I^I./[34m$([39;49;00mBUILDPYTHON[34m)[39;49;00m -Wi -tt [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBDEST[34m)[39;49;00m/compileall.py [33m\[39;49;00m$
   797^I^I^I-d [34m$([39;49;00mLIBDEST[34m)[39;49;00m -f [33m\[39;49;00m$
   798^I^I^I-x [33m'bad_coding|badsyntax|site-packages'[39;49;00m [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBDEST[34m)[39;49;00m$
   799^I^I[31mPYTHONPATH[39;49;00m=[34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBDEST[34m)[39;49;00m [34m$([39;49;00mRUNSHARED[34m)[39;49;00m [33m\[39;49;00m$
   800^I^I^I./[34m$([39;49;00mBUILDPYTHON[34m)[39;49;00m -Wi -tt -O [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBDEST[34m)[39;49;00m/compileall.py [33m\[39;49;00m$
   801^I^I^I-d [34m$([39;49;00mLIBDEST[34m)[39;49;00m -f [33m\[39;49;00m$
   802^I^I^I-x [33m'bad_coding|badsyntax|site-packages'[39;49;00m [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBDEST[34m)[39;49;00m$
   803^I^I-PYTHONPATH=[34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBDEST[34m)[39;49;00m  [34m$([39;49;00mRUNSHARED[34m)[39;49;00m [33m\[39;49;00m$
   804^I^I^I./[34m$([39;49;00mBUILDPYTHON[34m)[39;49;00m -Wi -t [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBDEST[34m)[39;49;00m/compileall.py [33m\[39;49;00m$
   805^I^I^I-d [34m$([39;49;00mLIBDEST[34m)[39;49;00m/site-packages -f [33m\[39;49;00m$
   806^I^I^I-x badsyntax [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBDEST[34m)[39;49;00m/site-packages$
   807^I^I-PYTHONPATH=[34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBDEST[34m)[39;49;00m [34m$([39;49;00mRUNSHARED[34m)[39;49;00m [33m\[39;49;00m$
   808^I^I^I./[34m$([39;49;00mBUILDPYTHON[34m)[39;49;00m -Wi -t -O [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBDEST[34m)[39;49;00m/compileall.py [33m\[39;49;00m$
   809^I^I^I-d [34m$([39;49;00mLIBDEST[34m)[39;49;00m/site-packages -f [33m\[39;49;00m$
   810^I^I^I-x badsyntax [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBDEST[34m)[39;49;00m/site-packages$
   811^I$
   812^I[37m# Create the PLATDIR source directory, if one wasn't distributed..[39;49;00m$
   813^I[32m$(srcdir)/Lib/$(PLATDIR)[39;49;00m:$
   814^I^Imkdir [34m$([39;49;00msrcdir[34m)[39;49;00m/Lib/[34m$([39;49;00mPLATDIR[34m)[39;49;00m$
   815^I^Icp [34m$([39;49;00msrcdir[34m)[39;49;00m/Lib/plat-generic/regen [34m$([39;49;00msrcdir[34m)[39;49;00m/Lib/[34m$([39;49;00mPLATDIR[34m)[39;49;00m/regen$
   816^I^I[36mexport[39;49;00m PATH; [31mPATH[39;49;00m=[33m"[39;49;00m[33m`pwd`:[39;49;00m[31m$$[39;49;00m[33mPATH[39;49;00m[33m"[39;49;00m; [33m\[39;49;00m$
   817^I^I[36mexport[39;49;00m PYTHONPATH; [31mPYTHONPATH[39;49;00m=[33m"`pwd`/Lib"[39;49;00m; [33m\[39;49;00m$
   818^I^I[36mexport[39;49;00m DYLD_FRAMEWORK_PATH; [31mDYLD_FRAMEWORK_PATH[39;49;00m=[33m"`pwd`"[39;49;00m; [33m\[39;49;00m$
   819^I^I[36mexport[39;49;00m EXE; [31mEXE[39;49;00m=[33m"[39;49;00m[34m$([39;49;00mBUILDEXE[34m)[39;49;00m[33m"[39;49;00m; [33m\[39;49;00m$
   820^I^I[36mcd[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/Lib/[34m$([39;49;00mPLATDIR[34m)[39;49;00m; ./regen$
   821^I$
   822^I[37m# Install the include files[39;49;00m$
   823^I[31mINCLDIRSTOMAKE[39;49;00m=[34m$([39;49;00mINCLUDEDIR[34m)[39;49;00m [34m$([39;49;00mCONFINCLUDEDIR[34m)[39;49;00m [34m$([39;49;00mINCLUDEPY[34m)[39;49;00m [34m$([39;49;00mCONFINCLUDEPY[34m)[39;49;00m$
   824^I[32minclinstall[39;49;00m:$
   825^I^I@for i [34min[39;49;00m [34m$([39;49;00mINCLDIRSTOMAKE[34m)[39;49;00m; [33m\[39;49;00m$
   826^I^I[34mdo[39;49;00m [33m\[39;49;00m$
   827^I[36m^I^Iif test ! -d $(DESTDIR)$$i; then \[39;49;00m$
   828^I[36m^I^I^Iecho "Creating directory $$i"; \[39;49;00m$
   829^I[36m^I^I^I$(INSTALL) -d -m $(DIRMODE) $(DESTDIR)$$i; \[39;49;00m$
   830^I[36m^I^Ielse^Itrue; \[39;49;00m$
   831^I[36m^I^Ifi; \[39;49;00m$
   832^I[36m^Idone[39;49;00m$
   833^I^I@for i [34min[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/Include/*.h; [33m\[39;49;00m$
   834^I^I[34mdo[39;49;00m [33m\[39;49;00m$
   835^I^I^I[36mecho[39;49;00m [34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m [31m$$[39;49;00mi [34m$([39;49;00mINCLUDEPY[34m)[39;49;00m; [33m\[39;49;00m$
   836^I^I^I[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m [31m$$[39;49;00mi [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mINCLUDEPY[34m)[39;49;00m; [33m\[39;49;00m$
   837^I^I[34mdone[39;49;00m$
   838^I^I[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m pyconfig.h [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mCONFINCLUDEPY[34m)[39;49;00m/pyconfig.h$
   839^I$
   840^I[37m# Install the library and miscellaneous stuff needed for extending/embedding[39;49;00m$
   841^I[37m# This goes into $(exec_prefix)[39;49;00m$
   842^I[31mLIBPL[39;49;00m=^I^I[34m$([39;49;00mLIBP[34m)[39;49;00m/config$
   843^I[32mlibainstall[39;49;00m:^Iall$
   844^I^I@for i [34min[39;49;00m [34m$([39;49;00mLIBDIR[34m)[39;49;00m [34m$([39;49;00mLIBP[34m)[39;49;00m [34m$([39;49;00mLIBPL[34m)[39;49;00m; [33m\[39;49;00m$
   845^I^I[34mdo[39;49;00m [33m\[39;49;00m$
   846^I[36m^I^Iif test ! -d $(DESTDIR)$$i; then \[39;49;00m$
   847^I[36m^I^I^Iecho "Creating directory $$i"; \[39;49;00m$
   848^I[36m^I^I^I$(INSTALL) -d -m $(DIRMODE) $(DESTDIR)$$i; \[39;49;00m$
   849^I[36m^I^Ielse^Itrue; \[39;49;00m$
   850^I[36m^I^Ifi; \[39;49;00m$
   851^I[36m^Idone[39;49;00m$
   852^I^I@if [36mtest[39;49;00m -d [34m$([39;49;00mLIBRARY[34m)[39;49;00m; [34mthen[39;49;00m :; [34melse[39;49;00m [33m\[39;49;00m$
   853^I[36m^I^Iif test "$(PYTHONFRAMEWORKDIR)" = no-framework; then \[39;49;00m$
   854^I[36m^I^I^Iif test "$(SO)" = .dll; then \[39;49;00m$
   855^I[36m^I^I^I^I$(INSTALL_DATA) $(LDLIBRARY) $(DESTDIR)$(LIBPL) ; \[39;49;00m$
   856^I[36m^I^I^Ielse \[39;49;00m$
   857^I[36m^I^I^I^I$(INSTALL_DATA) $(LIBRARY) $(DESTDIR)$(LIBPL)/$(LIBRARY) ; \[39;49;00m$
   858^I[36m^I^I^I^I$(RANLIB) $(DESTDIR)$(LIBPL)/$(LIBRARY) ; \[39;49;00m$
   859^I[36m^I^I^Ifi; \[39;49;00m$
   860^I[36m^I^Ielse \[39;49;00m$
   861^I[36m^I^I^Iecho Skip install of $(LIBRARY) - use make frameworkinstall; \[39;49;00m$
   862^I[36m^I^Ifi; \[39;49;00m$
   863^I[36m^Ifi[39;49;00m$
   864^I^I[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m Modules/config.c [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m/config.c$
   865^I^I[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m Modules/python.o [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m/python.o$
   866^I^I[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/Modules/config.c.in [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m/config.c.in$
   867^I^I[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m Makefile [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m/Makefile$
   868^I^I[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m Modules/Setup [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m/Setup$
   869^I^I[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m Modules/Setup.local [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m/Setup.local$
   870^I^I[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m Modules/Setup.config [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m/Setup.config$
   871^I^I[34m$([39;49;00mINSTALL_SCRIPT[34m)[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/Modules/makesetup [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m/makesetup$
   872^I^I[34m$([39;49;00mINSTALL_SCRIPT[34m)[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/install-sh [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m/install-sh$
   873^I[37m^I# Substitution happens here, as the completely-expanded BINDIR[39;49;00m$
   874^I[37m^I# is not available in configure[39;49;00m$
   875^I^Ised -e [33m"[39;49;00m[33ms,@EXENAME@,[39;49;00m[34m$([39;49;00mBINDIR[34m)[39;49;00m[33m/python[39;49;00m[34m$([39;49;00mVERSION[34m)[39;49;00m[34m$([39;49;00mEXE[34m)[39;49;00m[33m,[39;49;00m[33m"[39;49;00m < [34m$([39;49;00msrcdir[34m)[39;49;00m/Misc/python-config.in >python-config$
   876^I^I[34m$([39;49;00mINSTALL_SCRIPT[34m)[39;49;00m python-config [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mBINDIR[34m)[39;49;00m/python[34m$([39;49;00mVERSION[34m)[39;49;00m-config$
   877^I^Irm python-config$
   878^I^I@if [ -s Modules/python.exp -a [33m\[39;49;00m$
   879^I^I^I[33m"[39;49;00m[33m`echo [39;49;00m[34m$([39;49;00mMACHDEP[34m)[39;49;00m[33m | sed 's/^\(...\).*/\1/'`[39;49;00m[33m"[39;49;00m = [33m"aix"[39;49;00m ]; [34mthen[39;49;00m [33m\[39;49;00m$
   880^I^I^Iecho; [36mecho[39;49;00m [33m"Installing support files for building shared extension modules on AIX:"[39;49;00m; [33m\[39;49;00m$
   881^I^I^I[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m Modules/python.exp^I^I[33m\[39;49;00m$
   882^I^I^I^I^I[34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m/python.exp;^I^I[33m\[39;49;00m$
   883^I^I^Iecho; [36mecho[39;49;00m [33m"[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m[33m/python.exp[39;49;00m[33m"[39;49;00m;^I^I[33m\[39;49;00m$
   884^I^I^I[34m$([39;49;00mINSTALL_SCRIPT[34m)[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/Modules/makexp_aix^I[33m\[39;49;00m$
   885^I^I^I^I^I[34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m/makexp_aix;^I^I[33m\[39;49;00m$
   886^I^I^I[36mecho[39;49;00m [33m"[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m[33m/makexp_aix[39;49;00m[33m"[39;49;00m;^I^I^I[33m\[39;49;00m$
   887^I^I^I[34m$([39;49;00mINSTALL_SCRIPT[34m)[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/Modules/ld_so_aix^I[33m\[39;49;00m$
   888^I^I^I^I^I[34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m/ld_so_aix;^I^I[33m\[39;49;00m$
   889^I^I^I[36mecho[39;49;00m [33m"[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m[33m/ld_so_aix[39;49;00m[33m"[39;49;00m;^I^I^I[33m\[39;49;00m$
   890^I^I^Iecho; [36mecho[39;49;00m [33m"See Misc/AIX-NOTES for details."[39;49;00m;^I[33m\[39;49;00m$
   891^I[36m^Ielse true; \[39;49;00m$
   892^I[36m^Ifi[39;49;00m$
   893^I^I@case [33m"[39;49;00m[34m$([39;49;00mMACHDEP[34m)[39;49;00m[33m"[39;49;00m [34min[39;49;00m beos*) [33m\[39;49;00m$
   894^I^I^Iecho; [36mecho[39;49;00m [33m"Installing support files for building shared extension modules on BeOS:"[39;49;00m; [33m\[39;49;00m$
   895^I^I^I[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m Misc/BeOS-NOTES [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m/README;^I[33m\[39;49;00m$
   896^I^I^Iecho; [36mecho[39;49;00m [33m"[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m[33m/README[39;49;00m[33m"[39;49;00m;^I^I^I[33m\[39;49;00m$
   897^I^I^I[34m$([39;49;00mINSTALL_SCRIPT[34m)[39;49;00m Modules/ar_beos [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m/ar_beos; [33m\[39;49;00m$
   898^I^I^I[36mecho[39;49;00m [33m"[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m[33m/ar_beos[39;49;00m[33m"[39;49;00m;^I^I^I[33m\[39;49;00m$
   899^I^I^I[34m$([39;49;00mINSTALL_SCRIPT[34m)[39;49;00m Modules/ld_so_beos [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m/ld_so_beos; [33m\[39;49;00m$
   900^I^I^I[36mecho[39;49;00m [33m"[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m[33m/ld_so_beos[39;49;00m[33m"[39;49;00m;^I^I^I[33m\[39;49;00m$
   901^I^I^Iecho; [36mecho[39;49;00m [33m"See Misc/BeOS-NOTES for details."[39;49;00m;^I[33m\[39;49;00m$
   902^I^I^I;; [33m\[39;49;00m$
   903^I^I[34mesac[39;49;00m$
   904^I$
   905^I[37m# Install the dynamically loadable modules[39;49;00m$
   906^I[37m# This goes into $(exec_prefix)[39;49;00m$
   907^I[32msharedinstall[39;49;00m:$
   908^I^I[34m$([39;49;00mRUNSHARED[34m)[39;49;00m ./[34m$([39;49;00mBUILDPYTHON[34m)[39;49;00m -E [34m$([39;49;00msrcdir[34m)[39;49;00m/setup.py install [33m\[39;49;00m$
   909^I^I   ^I--prefix=[34m$([39;49;00mprefix[34m)[39;49;00m [33m\[39;49;00m$
   910^I^I^I--install-scripts=[34m$([39;49;00mBINDIR[34m)[39;49;00m [33m\[39;49;00m$
   911^I^I^I--install-platlib=[34m$([39;49;00mDESTSHARED[34m)[39;49;00m [33m\[39;49;00m$
   912^I^I^I--root=/[34m$([39;49;00mDESTDIR[34m)[39;49;00m$
   913^I$
   914^I[37m# Here are a couple of targets for MacOSX again, to install a full[39;49;00m$
   915^I[37m# framework-based Python. frameworkinstall installs everything, the[39;49;00m$
   916^I[37m# subtargets install specific parts. Much of the actual work is offloaded to[39;49;00m$
   917^I[37m# the Makefile in Mac[39;49;00m$
   918^I[37m#[39;49;00m$
   919^I[37m#[39;49;00m$
   920^I[37m# This target is here for backward compatiblity, previous versions of Python[39;49;00m$
   921^I[37m# hadn't integrated framework installation in the normal install process.[39;49;00m$
   922^I[32mframeworkinstall[39;49;00m: install$
   923^I$
   924^I[37m# On install, we re-make the framework[39;49;00m$
   925^I[37m# structure in the install location, /Library/Frameworks/ or the argument to[39;49;00m$
   926^I[37m# --enable-framework. If --enable-framework has been specified then we have[39;49;00m$
   927^I[37m# automatically set prefix to the location deep down in the framework, so we[39;49;00m$
   928^I[37m# only have to cater for the structural bits of the framework.[39;49;00m$
   929^I$
   930^I[32mframeworkinstallframework[39;49;00m: frameworkinstallstructure install frameworkinstallmaclib$
   931^I$
   932^I[32mframeworkinstallstructure[39;49;00m:^I[34m$([39;49;00m[31mLDLIBRARY[39;49;00m[34m)[39;49;00m$
   933^I^I@if [36mtest[39;49;00m [33m"[39;49;00m[34m$([39;49;00mPYTHONFRAMEWORKDIR[34m)[39;49;00m[33m"[39;49;00m = no-framework; [34mthen[39;49;00m [33m\[39;49;00m$
   934^I^I^I[36mecho[39;49;00m Not configured with --enable-framework; [33m\[39;49;00m$
   935^I^I^I[36mexit[39;49;00m [34m1[39;49;00m; [33m\[39;49;00m$
   936^I[36m^Ielse true; \[39;49;00m$
   937^I[36m^Ifi[39;49;00m$
   938^I^I@for i [34min[39;49;00m [34m$([39;49;00mprefix[34m)[39;49;00m/Resources/English.lproj [34m$([39;49;00mprefix[34m)[39;49;00m/lib; [34mdo[39;49;00m[33m\[39;49;00m$
   939^I[36m^I^Iif test ! -d $(DESTDIR)$$i; then \[39;49;00m$
   940^I[36m^I^I^Iecho "Creating directory $(DESTDIR)$$i"; \[39;49;00m$
   941^I[36m^I^I^I$(INSTALL) -d -m $(DIRMODE) $(DESTDIR)$$i; \[39;49;00m$
   942^I[36m^I^Ielse^Itrue; \[39;49;00m$
   943^I[36m^I^Ifi; \[39;49;00m$
   944^I[36m^Idone[39;49;00m$
   945^I^I[34m$([39;49;00mLN[34m)[39;49;00m -fsn include/python[34m$([39;49;00mVERSION[34m)[39;49;00m [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mprefix[34m)[39;49;00m/Headers$
   946^I^I[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m [34m$([39;49;00mRESSRCDIR[34m)[39;49;00m/Info.plist [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mprefix[34m)[39;49;00m/Resources/Info.plist$
   947^I^I[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m [34m$([39;49;00mRESSRCDIR[34m)[39;49;00m/version.plist [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mprefix[34m)[39;49;00m/Resources/version.plist$
   948^I^I[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m [34m$([39;49;00mRESSRCDIR[34m)[39;49;00m/English.lproj/InfoPlist.strings [33m\[39;49;00m$
   949^I^I^I[34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mprefix[34m)[39;49;00m/Resources/English.lproj/InfoPlist.strings$
   950^I^I[34m$([39;49;00mLN[34m)[39;49;00m -fsn [34m$([39;49;00mVERSION[34m)[39;49;00m [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mPYTHONFRAMEWORKINSTALLDIR[34m)[39;49;00m/Versions/Current$
   951^I^I[34m$([39;49;00mLN[34m)[39;49;00m -fsn Versions/Current/Python [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mPYTHONFRAMEWORKINSTALLDIR[34m)[39;49;00m/Python$
   952^I^I[34m$([39;49;00mLN[34m)[39;49;00m -fsn Versions/Current/Headers [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mPYTHONFRAMEWORKINSTALLDIR[34m)[39;49;00m/Headers$
   953^I^I[34m$([39;49;00mLN[34m)[39;49;00m -fsn Versions/Current/Resources [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mPYTHONFRAMEWORKINSTALLDIR[34m)[39;49;00m/Resources$
   954^I^I[34m$([39;49;00mINSTALL_SHARED[34m)[39;49;00m [34m$([39;49;00mLDLIBRARY[34m)[39;49;00m [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mPYTHONFRAMEWORKPREFIX[34m)[39;49;00m/[34m$([39;49;00mLDLIBRARY[34m)[39;49;00m$
   955^I$
   956^I[37m# This installs Mac/Lib into the framework[39;49;00m$
   957^I[37m# Install a number of symlinks to keep software that expects a normal unix[39;49;00m$
   958^I[37m# install (which includes python-config) happy.[39;49;00m$
   959^I[32mframeworkinstallmaclib[39;49;00m:$
   960^I^Iln -fs [33m"../../../Python"[39;49;00m [33m"[39;49;00m[34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mprefix[34m)[39;49;00m[33m/lib/python[39;49;00m[34m$([39;49;00mVERSION[34m)[39;49;00m[33m/config/libpython[39;49;00m[34m$([39;49;00mVERSION[34m)[39;49;00m[33m.a[39;49;00m[33m"[39;49;00m$
   961^I^I[36mcd[39;49;00m Mac && [34m$([39;49;00mMAKE[34m)[39;49;00m installmacsubtree [31mDESTDIR[39;49;00m=[33m"[39;49;00m[34m$([39;49;00mDESTDIR[34m)[39;49;00m[33m"[39;49;00m$
   962^I$
   963^I[37m# This installs the IDE, the Launcher and other apps into /Applications[39;49;00m$
   964^I[32mframeworkinstallapps[39;49;00m:$
   965^I^I[36mcd[39;49;00m Mac && [34m$([39;49;00mMAKE[34m)[39;49;00m installapps [31mDESTDIR[39;49;00m=[33m"[39;49;00m[34m$([39;49;00mDESTDIR[34m)[39;49;00m[33m"[39;49;00m$
   966^I$
   967^I[37m# This install the unix python and pythonw tools in /usr/local/bin[39;49;00m$
   968^I[32mframeworkinstallunixtools[39;49;00m:$
   969^I^I[36mcd[39;49;00m Mac && [34m$([39;49;00mMAKE[34m)[39;49;00m installunixtools [31mDESTDIR[39;49;00m=[33m"[39;49;00m[34m$([39;49;00mDESTDIR[34m)[39;49;00m[33m"[39;49;00m$
   970^I$
   971^I[32mframeworkaltinstallunixtools[39;49;00m:$
   972^I^I[36mcd[39;49;00m Mac && [34m$([39;49;00mMAKE[34m)[39;49;00m altinstallunixtools [31mDESTDIR[39;49;00m=[33m"[39;49;00m[34m$([39;49;00mDESTDIR[34m)[39;49;00m[33m"[39;49;00m$
   973^I$
   974^I[37m# This installs the Demos and Tools into the applications directory.[39;49;00m$
   975^I[37m# It is not part of a normal frameworkinstall[39;49;00m$
   976^I[32mframeworkinstallextras[39;49;00m:$
   977^I^I[36mcd[39;49;00m Mac && Make installextras [31mDESTDIR[39;49;00m=[33m"[39;49;00m[34m$([39;49;00mDESTDIR[34m)[39;49;00m[33m"[39;49;00m$
   978^I$
   979^I[37m# This installs a few of the useful scripts in Tools/scripts[39;49;00m$
   980^I[32mscriptsinstall[39;49;00m:$
   981^I^I[31mSRCDIR[39;49;00m=[34m$([39;49;00msrcdir[34m)[39;49;00m [34m$([39;49;00mRUNSHARED[34m)[39;49;00m [33m\[39;49;00m$
   982^I^I./[34m$([39;49;00mBUILDPYTHON[34m)[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/Tools/scripts/setup.py install [33m\[39;49;00m$
   983^I^I--prefix=[34m$([39;49;00mprefix[34m)[39;49;00m [33m\[39;49;00m$
   984^I^I--install-scripts=[34m$([39;49;00mBINDIR[34m)[39;49;00m [33m\[39;49;00m$
   985^I^I--root=/[34m$([39;49;00mDESTDIR[34m)[39;49;00m$
   986^I$
   987^I[37m# Build the toplevel Makefile[39;49;00m$
   988^I[32mMakefile.pre[39;49;00m: Makefile.pre.in config.status$
   989^I^I[31mCONFIG_FILES[39;49;00m=Makefile.pre [31mCONFIG_HEADERS[39;49;00m= [34m$([39;49;00mSHELL[34m)[39;49;00m config.status$
   990^I^I[34m$([39;49;00mMAKE[34m)[39;49;00m -f Makefile.pre Makefile$
   991^I$
   992^I[37m# Run the configure script.[39;49;00m$
   993^I[32mconfig.status[39;49;00m:^I[34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/configure$
   994^I^I[34m$([39;49;00mSHELL[34m)[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/configure [34m$([39;49;00mCONFIG_ARGS[34m)[39;49;00m$
   995^I$
   996^I[32m.PRECIOUS[39;49;00m: config.status [34m$([39;49;00m[31mBUILDPYTHON[39;49;00m[34m)[39;49;00m Makefile Makefile.pre$
   997^I$
   998^I[37m# Some make's put the object file in the current directory[39;49;00m$
   999^I[32m.c.o[39;49;00m:$
  1000^I^I[34m$([39;49;00mCC[34m)[39;49;00m -c [34m$([39;49;00mPY_CFLAGS[34m)[39;49;00m -o [31m$@[39;49;00m $<$
  1001^I$
  1002^I[37m# Run reindent on the library[39;49;00m$
  1003^I[32mreindent[39;49;00m:$
  1004^I^I./python[34m$([39;49;00mEXEEXT[34m)[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/Tools/scripts/reindent.py -r [34m$([39;49;00msrcdir[34m)[39;49;00m/Lib$
  1005^I$
  1006^I[37m# Rerun configure with the same options as it was run last time,[39;49;00m$
  1007^I[37m# provided the config.status script exists[39;49;00m$
  1008^I[32mrecheck[39;49;00m:$
  1009^I^I[34m$([39;49;00mSHELL[34m)[39;49;00m config.status --recheck$
  1010^I^I[34m$([39;49;00mSHELL[34m)[39;49;00m config.status$
  1011^I$
  1012^I[37m# Rebuild the configure script from configure.in; also rebuild pyconfig.h.in[39;49;00m$
  1013^I[32mautoconf[39;49;00m:$
  1014^I^I([36mcd[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m; autoconf)$
  1015^I^I([36mcd[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m; autoheader)$
  1016^I$
  1017^I[37m# Create a tags file for vi[39;49;00m$
  1018^I[32mtags[39;49;00m::$
  1019^I^I[36mcd[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m; [33m\[39;49;00m$
  1020^I^Ictags -w -t Include/*.h; [33m\[39;49;00m$
  1021^I^I[34mfor[39;49;00m i [34min[39;49;00m [34m$([39;49;00mSRCDIRS[34m)[39;49;00m; [34mdo[39;49;00m ctags -w -t -a [31m$$[39;49;00mi/*.[ch]; [33m\[39;49;00m$
  1022^I^I[34mdone[39;49;00m; [33m\[39;49;00m$
  1023^I^Isort -o tags tags$
  1024^I$
  1025^I[37m# Create a tags file for GNU Emacs[39;49;00m$
  1026^I[32mTAGS[39;49;00m::$
  1027^I^I[36mcd[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m; [33m\[39;49;00m$
  1028^I^Ietags Include/*.h; [33m\[39;49;00m$
  1029^I^I[34mfor[39;49;00m i [34min[39;49;00m [34m$([39;49;00mSRCDIRS[34m)[39;49;00m; [34mdo[39;49;00m etags -a [31m$$[39;49;00mi/*.[ch]; [34mdone[39;49;00m$
  1030^I$
  1031^I[37m# Sanitation targets -- clean leaves libraries, executables and tags[39;49;00m$
  1032^I[37m# files, which clobber removes those as well[39;49;00m$
  1033^I[32mpycremoval[39;49;00m:$
  1034^I^Ifind [34m$([39;49;00msrcdir[34m)[39;49;00m -name [33m'*.py[co]'[39;49;00m -exec rm -f {} [33m';'[39;49;00m$
  1035^I$
  1036^I[32mclean[39;49;00m: pycremoval$
  1037^I^Ifind . -name [33m'*.o'[39;49;00m -exec rm -f {} [33m';'[39;49;00m$
  1038^I^Ifind . -name [33m'*.s[ol]'[39;49;00m -exec rm -f {} [33m';'[39;49;00m$
  1039^I^Ifind [34m$([39;49;00msrcdir[34m)[39;49;00m/build -name [33m'fficonfig.h'[39;49;00m -exec rm -f {} [33m';'[39;49;00m || [36mtrue[39;49;00m$
  1040^I^Ifind [34m$([39;49;00msrcdir[34m)[39;49;00m/build -name [33m'fficonfig.py'[39;49;00m -exec rm -f {} [33m';'[39;49;00m || [36mtrue[39;49;00m$
  1041^I$
  1042^I[32mclobber[39;49;00m: clean$
  1043^I^I-rm -f [34m$([39;49;00mBUILDPYTHON[34m)[39;49;00m [34m$([39;49;00mPGEN[34m)[39;49;00m [34m$([39;49;00mLIBRARY[34m)[39;49;00m [34m$([39;49;00mLDLIBRARY[34m)[39;49;00m [34m$([39;49;00mDLLLIBRARY[34m)[39;49;00m [33m\[39;49;00m$
  1044^I^I^Itags TAGS [33m\[39;49;00m$
  1045^I^I^Iconfig.cache config.log pyconfig.h Modules/config.c$
  1046^I^I-rm -rf build platform$
  1047^I^I-rm -rf [34m$([39;49;00mPYTHONFRAMEWORKDIR[34m)[39;49;00m$
  1048^I$
  1049^I[37m# Make things extra clean, before making a distribution:[39;49;00m$
  1050^I[37m# remove all generated files, even Makefile[.pre][39;49;00m$
  1051^I[37m# Keep configure and Python-ast.[ch], it's possible they can't be generated[39;49;00m$
  1052^I[32mdistclean[39;49;00m: clobber$
  1053^I^I-rm -f core Makefile Makefile.pre config.status [33m\[39;49;00m$
  1054^I^I^IModules/Setup Modules/Setup.local Modules/Setup.config$
  1055^I^Ifind [34m$([39;49;00msrcdir[34m)[39;49;00m [33m'('[39;49;00m -name [33m'*.fdc'[39;49;00m -o -name [33m'*~'[39;49;00m [33m\[39;49;00m$
  1056^I^I^I^I   -o -name [33m'[@,#]*'[39;49;00m -o -name [33m'*.old'[39;49;00m [33m\[39;49;00m$
  1057^I^I^I^I   -o -name [33m'*.orig'[39;49;00m -o -name [33m'*.rej'[39;49;00m [33m\[39;49;00m$
  1058^I^I^I^I   -o -name [33m'*.bak'[39;49;00m [33m')'[39;49;00m [33m\[39;49;00m$
  1059^I^I^I^I   -exec rm -f {} [33m';'[39;49;00m$
  1060^I$
  1061^I[37m# Check for smelly exported symbols (not starting with Py/_Py)[39;49;00m$
  1062^I[32msmelly[39;49;00m: all$
  1063^I^Inm -p [34m$([39;49;00mLIBRARY[34m)[39;49;00m | [33m\[39;49;00m$
  1064^I^I^Ised -n [33m"/ [TDB] /s/.* //p"[39;49;00m | grep -v [33m"^_*Py"[39;49;00m | sort -u; [33m\[39;49;00m$
  1065^I$
  1066^I[37m# Find files with funny names[39;49;00m$
  1067^I[32mfunny[39;49;00m:$
  1068^I^Ifind [34m$([39;49;00mDISTDIRS[34m)[39;49;00m -type d [33m\[39;49;00m$
  1069^I^I^I-o -name [33m'*.[chs]'[39;49;00m [33m\[39;49;00m$
  1070^I^I^I-o -name [33m'*.py'[39;49;00m [33m\[39;49;00m$
  1071^I^I^I-o -name [33m'*.doc'[39;49;00m [33m\[39;49;00m$
  1072^I^I^I-o -name [33m'*.sty'[39;49;00m [33m\[39;49;00m$
  1073^I^I^I-o -name [33m'*.bib'[39;49;00m [33m\[39;49;00m$
  1074^I^I^I-o -name [33m'*.dat'[39;49;00m [33m\[39;49;00m$
  1075^I^I^I-o -name [33m'*.el'[39;49;00m [33m\[39;49;00m$
  1076^I^I^I-o -name [33m'*.fd'[39;49;00m [33m\[39;49;00m$
  1077^I^I^I-o -name [33m'*.in'[39;49;00m [33m\[39;49;00m$
  1078^I^I^I-o -name [33m'*.tex'[39;49;00m [33m\[39;49;00m$
  1079^I^I^I-o -name [33m'*,[vpt]'[39;49;00m [33m\[39;49;00m$
  1080^I^I^I-o -name [33m'Setup'[39;49;00m [33m\[39;49;00m$
  1081^I^I^I-o -name [33m'Setup.*'[39;49;00m [33m\[39;49;00m$
  1082^I^I^I-o -name README [33m\[39;49;00m$
  1083^I^I^I-o -name Makefile [33m\[39;49;00m$
  1084^I^I^I-o -name ChangeLog [33m\[39;49;00m$
  1085^I^I^I-o -name Repository [33m\[39;49;00m$
  1086^I^I^I-o -name Root [33m\[39;49;00m$
  1087^I^I^I-o -name Entries [33m\[39;49;00m$
  1088^I^I^I-o -name Tag [33m\[39;49;00m$
  1089^I^I^I-o -name tags [33m\[39;49;00m$
  1090^I^I^I-o -name TAGS [33m\[39;49;00m$
  1091^I^I^I-o -name .cvsignore [33m\[39;49;00m$
  1092^I^I^I-o -name MANIFEST [33m\[39;49;00m$
  1093^I^I^I-o -print$
  1094^I$
  1095^I[37m# Dependencies[39;49;00m$
  1096^I$
  1097^I[32mPython/thread.o[39;49;00m:  [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Python/thread_atheos.h [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Python/thread_beos.h [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Python/thread_cthread.h [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Python/thread_foobar.h [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Python/thread_lwp.h [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Python/thread_nt.h [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Python/thread_os2.h [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Python/thread_pth.h [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Python/thread_pthread.h [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Python/thread_sgi.h [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Python/thread_solaris.h [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Python/thread_wince.h$
  1098^I$
  1099^I[37m# Declare targets that aren't real files[39;49;00m$
  1100^I[32m.PHONY[39;49;00m: all sharedmods oldsharedmods test quicktest memtest$
  1101^I[32m.PHONY[39;49;00m: install altinstall oldsharedinstall bininstall altbininstall$
  1102^I[32m.PHONY[39;49;00m: maninstall libinstall inclinstall libainstall sharedinstall$
  1103^I[32m.PHONY[39;49;00m: frameworkinstall frameworkinstallframework frameworkinstallstructure$
  1104^I[32m.PHONY[39;49;00m: frameworkinstallmaclib frameworkinstallapps frameworkinstallunixtools$
  1105^I[32m.PHONY[39;49;00m: frameworkaltinstallunixtools recheck autoconf clean clobber distclean $
  1106^I[32m.PHONY[39;49;00m: smelly funny$
  1107^I$
  1108^I[37m# IF YOU PUT ANYTHING HERE IT WILL GO AWAY[39;49;00m$
  1109^I$
  1110^I[37m# Rules appended by makedepend[39;49;00m$
  1111^I$
  1112^I[32mModules/threadmodule.o[39;49;00m: [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/threadmodule.c; [34m$([39;49;00m[31mCC[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31mPY_CFLAGS[39;49;00m[34m)[39;49;00m  -c [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/threadmodule.c -o Modules/threadmodule.o$
  1113^I[32mModules/threadmodule$(SO)[39;49;00m:  Modules/threadmodule.o; [34m$([39;49;00m[31mLDSHARED[39;49;00m[34m)[39;49;00m  Modules/threadmodule.o   -o Modules/threadmodule[34m$([39;49;00m[31mSO[39;49;00m[34m)[39;49;00m$
  1114^I[32mModules/signalmodule.o[39;49;00m: [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/signalmodule.c; [34m$([39;49;00m[31mCC[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31mPY_CFLAGS[39;49;00m[34m)[39;49;00m  -c [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/signalmodule.c -o Modules/signalmodule.o$
  1115^I[32mModules/signalmodule$(SO)[39;49;00m:  Modules/signalmodule.o; [34m$([39;49;00m[31mLDSHARED[39;49;00m[34m)[39;49;00m  Modules/signalmodule.o   -o Modules/signalmodule[34m$([39;49;00m[31mSO[39;49;00m[34m)[39;49;00m$
  1116^I[32mModules/posixmodule.o[39;49;00m: [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/posixmodule.c; [34m$([39;49;00m[31mCC[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31mPY_CFLAGS[39;49;00m[34m)[39;49;00m  -c [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/posixmodule.c -o Modules/posixmodule.o$
  1117^I[32mModules/posixmodule$(SO)[39;49;00m:  Modules/posixmodule.o; [34m$([39;49;00m[31mLDSHARED[39;49;00m[34m)[39;49;00m  Modules/posixmodule.o   -o Modules/posixmodule[34m$([39;49;00m[31mSO[39;49;00m[34m)[39;49;00m$
  1118^I[32mModules/errnomodule.o[39;49;00m: [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/errnomodule.c; [34m$([39;49;00m[31mCC[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31mPY_CFLAGS[39;49;00m[34m)[39;49;00m  -c [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/errnomodule.c -o Modules/errnomodule.o$
  1119^I[32mModules/errnomodule$(SO)[39;49;00m:  Modules/errnomodule.o; [34m$([39;49;00m[31mLDSHARED[39;49;00m[34m)[39;49;00m  Modules/errnomodule.o   -o Modules/errnomodule[34m$([39;49;00m[31mSO[39;49;00m[34m)[39;49;00m$
  1120^I[32mModules/pwdmodule.o[39;49;00m: [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/pwdmodule.c; [34m$([39;49;00m[31mCC[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31mPY_CFLAGS[39;49;00m[34m)[39;49;00m  -c [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/pwdmodule.c -o Modules/pwdmodule.o$
  1121^I[32mModules/pwdmodule$(SO)[39;49;00m:  Modules/pwdmodule.o; [34m$([39;49;00m[31mLDSHARED[39;49;00m[34m)[39;49;00m  Modules/pwdmodule.o   -o Modules/pwdmodule[34m$([39;49;00m[31mSO[39;49;00m[34m)[39;49;00m$
  1122^I[32mModules/_sre.o[39;49;00m: [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/_sre.c; [34m$([39;49;00m[31mCC[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31mPY_CFLAGS[39;49;00m[34m)[39;49;00m  -c [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/_sre.c -o Modules/_sre.o$
  1123^I[32mModules/_sre$(SO)[39;49;00m:  Modules/_sre.o; [34m$([39;49;00m[31mLDSHARED[39;49;00m[34m)[39;49;00m  Modules/_sre.o   -o Modules/_sre[34m$([39;49;00m[31mSO[39;49;00m[34m)[39;49;00m$
  1124^I[32mModules/_codecsmodule.o[39;49;00m: [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/_codecsmodule.c; [34m$([39;49;00m[31mCC[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31mPY_CFLAGS[39;49;00m[34m)[39;49;00m  -c [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/_codecsmodule.c -o Modules/_codecsmodule.o$
  1125^I[32mModules/_codecsmodule$(SO)[39;49;00m:  Modules/_codecsmodule.o; [34m$([39;49;00m[31mLDSHARED[39;49;00m[34m)[39;49;00m  Modules/_codecsmodule.o   -o Modules/_codecsmodule[34m$([39;49;00m[31mSO[39;49;00m[34m)[39;49;00m$
  1126^I[32mModules/zipimport.o[39;49;00m: [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/zipimport.c; [34m$([39;49;00m[31mCC[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31mPY_CFLAGS[39;49;00m[34m)[39;49;00m  -c [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/zipimport.c -o Modules/zipimport.o$
  1127^I[32mModules/zipimport$(SO)[39;49;00m:  Modules/zipimport.o; [34m$([39;49;00m[31mLDSHARED[39;49;00m[34m)[39;49;00m  Modules/zipimport.o   -o Modules/zipimport[34m$([39;49;00m[31mSO[39;49;00m[34m)[39;49;00m$
  1128^I[32mModules/symtablemodule.o[39;49;00m: [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/symtablemodule.c; [34m$([39;49;00m[31mCC[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31mPY_CFLAGS[39;49;00m[34m)[39;49;00m  -c [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/symtablemodule.c -o Modules/symtablemodule.o$
  1129^I[32mModules/_symtablemodule$(SO)[39;49;00m:  Modules/symtablemodule.o; [34m$([39;49;00m[31mLDSHARED[39;49;00m[34m)[39;49;00m  Modules/symtablemodule.o   -o Modules/_symtablemodule[34m$([39;49;00m[31mSO[39;49;00m[34m)[39;49;00m$
  1130^I[32mModules/xxsubtype.o[39;49;00m: [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/xxsubtype.c; [34m$([39;49;00m[31mCC[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31mPY_CFLAGS[39;49;00m[34m)[39;49;00m  -c [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/xxsubtype.c -o Modules/xxsubtype.o$
  1131^I[32mModules/xxsubtype$(SO)[39;49;00m:  Modules/xxsubtype.o; [34m$([39;49;00m[31mLDSHARED[39;49;00m[34m)[39;49;00m  Modules/xxsubtype.o   -o Modules/xxsubtype[34m$([39;49;00m[31mSO[39;49;00m[34m)[39;49;00m$

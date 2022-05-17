[37m# Generated automatically from Makefile.pre by makesetup.[39;49;00m$
[37m# Top-level Makefile for Python[39;49;00m$
[37m#[39;49;00m$
[37m# As distributed, this file is called Makefile.pre.in; it is processed[39;49;00m$
[37m# into the real Makefile by running the script ./configure, which[39;49;00m$
[37m# replaces things like @spam@ with values appropriate for your system.[39;49;00m$
[37m# This means that if you edit Makefile, your changes get lost the next[39;49;00m$
[37m# time you run the configure script.  Ideally, you can do:[39;49;00m$
[37m#[39;49;00m$
[37m#	./configure[39;49;00m$
[37m#	make[39;49;00m$
[37m#	make test[39;49;00m$
[37m#	make install[39;49;00m$
[37m#[39;49;00m$
[37m# If you have a previous version of Python installed that you don't[39;49;00m$
[37m# want to overwrite, you can use "make altinstall" instead of "make[39;49;00m$
[37m# install".  Refer to the "Installing" section in the README file for[39;49;00m$
[37m# additional details.[39;49;00m$
[37m#[39;49;00m$
[37m# See also the section "Build instructions" in the README file.[39;49;00m$
$
[37m# === Variables set by makesetup ===[39;49;00m$
$
[31mMODOBJS[39;49;00m=          Modules/threadmodule.o  Modules/signalmodule.o  Modules/posixmodule.o  Modules/errnomodule.o  Modules/pwdmodule.o  Modules/_sre.o  Modules/_codecsmodule.o  Modules/zipimport.o  Modules/symtablemodule.o  Modules/xxsubtype.o$
[31mMODLIBS[39;49;00m=        [34m$([39;49;00mLOCALMODLIBS[34m)[39;49;00m [34m$([39;49;00mBASEMODLIBS[34m)[39;49;00m$
$
[37m# === Variables set by configure[39;49;00m$
[31mVERSION[39;49;00m=	[34m2[39;49;00m.6$
[31msrcdir[39;49;00m=		.$
$
$
[31mCC[39;49;00m=		gcc -pthread$
[31mCXX[39;49;00m=		g++ -pthread$
[31mMAINCC[39;49;00m=		[34m$([39;49;00mCC[34m)[39;49;00m$
[31mLINKCC[39;49;00m=		[34m$([39;49;00mPURIFY[34m)[39;49;00m [34m$([39;49;00mMAINCC[34m)[39;49;00m$
[31mAR[39;49;00m=		ar$
[31mRANLIB[39;49;00m=		ranlib$
[31mSVNVERSION[39;49;00m=	svnversion [34m$([39;49;00msrcdir[34m)[39;49;00m$
$
[37m# Shell used by make (some versions default to the login shell, which is bad)[39;49;00m$
[31mSHELL[39;49;00m=		/bin/sh$
$
[37m# Use this to make a link between python$(VERSION) and python in $(BINDIR)[39;49;00m$
[31mLN[39;49;00m=		ln$
$
[37m# Portable install script (configure doesn't always guess right)[39;49;00m$
[31mINSTALL[39;49;00m=	/usr/bin/install -c$
[31mINSTALL_PROGRAM[39;49;00m=[33m${[39;49;00m[31mINSTALL[39;49;00m[33m}[39;49;00m$
[31mINSTALL_SCRIPT[39;49;00m= [33m${[39;49;00m[31mINSTALL[39;49;00m[33m}[39;49;00m$
[31mINSTALL_DATA[39;49;00m=	[33m${[39;49;00m[31mINSTALL[39;49;00m[33m}[39;49;00m -m [34m644[39;49;00m$
[37m# Shared libraries must be installed with executable mode on some systems;[39;49;00m$
[37m# rather than figuring out exactly which, we always give them executable mode.[39;49;00m$
[37m# Also, making them read-only seems to be a good idea...[39;49;00m$
[31mINSTALL_SHARED[39;49;00m= [33m${[39;49;00m[31mINSTALL[39;49;00m[33m}[39;49;00m -m [34m555[39;49;00m$
$
[31mMAKESETUP[39;49;00m=      [34m$([39;49;00msrcdir[34m)[39;49;00m/Modules/makesetup$
$
[37m# Compiler options[39;49;00m$
[31mOPT[39;49;00m=		-g -Wall -Wstrict-prototypes$
[31mBASECFLAGS[39;49;00m=	 -fno-strict-aliasing$
[31mCFLAGS[39;49;00m=		[34m$([39;49;00mBASECFLAGS[34m)[39;49;00m [34m$([39;49;00mOPT[34m)[39;49;00m [34m$([39;49;00mEXTRA_CFLAGS[34m)[39;49;00m$
[37m# Both CPPFLAGS and LDFLAGS need to contain the shell's value for setup.py to[39;49;00m$
[37m# be able to build extension modules using the directories specified in the[39;49;00m$
[37m# environment variables[39;49;00m$
[31mCPPFLAGS[39;49;00m=	-I. -I[34m$([39;49;00msrcdir[34m)[39;49;00m/Include $
[31mLDFLAGS[39;49;00m=	$
[31mLDLAST[39;49;00m=		$
[31mSGI_ABI[39;49;00m=	$
[31mCCSHARED[39;49;00m=	-fPIC$
[31mLINKFORSHARED[39;49;00m=	-Xlinker -export-dynamic$
[37m# Extra C flags added for building the interpreter object files.[39;49;00m$
[31mCFLAGSFORSHARED[39;49;00m=$
[37m# C flags used for building the interpreter object files[39;49;00m$
[31mPY_CFLAGS[39;49;00m=	[34m$([39;49;00mCFLAGS[34m)[39;49;00m [34m$([39;49;00mCPPFLAGS[34m)[39;49;00m [34m$([39;49;00mCFLAGSFORSHARED[34m)[39;49;00m -DPy_BUILD_CORE$
$
$
[37m# Machine-dependent subdirectories[39;49;00m$
[31mMACHDEP[39;49;00m=	linux2$
$
[37m# Install prefix for architecture-independent files[39;49;00m$
[31mprefix[39;49;00m=		/usr/local$
$
[37m# Install prefix for architecture-dependent files[39;49;00m$
[31mexec_prefix[39;49;00m=	[33m${[39;49;00m[31mprefix[39;49;00m[33m}[39;49;00m$
$
[37m# Expanded directories[39;49;00m$
[31mBINDIR[39;49;00m=		[34m$([39;49;00mexec_prefix[34m)[39;49;00m/bin$
[31mLIBDIR[39;49;00m=		[34m$([39;49;00mexec_prefix[34m)[39;49;00m/lib$
[31mMANDIR[39;49;00m=		[33m${[39;49;00m[31mprefix[39;49;00m[33m}[39;49;00m/man$
[31mINCLUDEDIR[39;49;00m=	[33m${[39;49;00m[31mprefix[39;49;00m[33m}[39;49;00m/include$
[31mCONFINCLUDEDIR[39;49;00m=	[34m$([39;49;00mexec_prefix[34m)[39;49;00m/include$
[31mSCRIPTDIR[39;49;00m=	[34m$([39;49;00mprefix[34m)[39;49;00m/lib$
$
[37m# Detailed destination directories[39;49;00m$
[31mBINLIBDEST[39;49;00m=	[34m$([39;49;00mLIBDIR[34m)[39;49;00m/python[34m$([39;49;00mVERSION[34m)[39;49;00m$
[31mLIBDEST[39;49;00m=	[34m$([39;49;00mSCRIPTDIR[34m)[39;49;00m/python[34m$([39;49;00mVERSION[34m)[39;49;00m$
[31mINCLUDEPY[39;49;00m=	[34m$([39;49;00mINCLUDEDIR[34m)[39;49;00m/python[34m$([39;49;00mVERSION[34m)[39;49;00m$
[31mCONFINCLUDEPY[39;49;00m=	[34m$([39;49;00mCONFINCLUDEDIR[34m)[39;49;00m/python[34m$([39;49;00mVERSION[34m)[39;49;00m$
[31mLIBP[39;49;00m=		[34m$([39;49;00mLIBDIR[34m)[39;49;00m/python[34m$([39;49;00mVERSION[34m)[39;49;00m$
$
[37m# Symbols used for using shared libraries[39;49;00m$
[31mSO[39;49;00m=		.so$
[31mLDSHARED[39;49;00m=	[34m$([39;49;00mCC[34m)[39;49;00m -shared$
[31mBLDSHARED[39;49;00m=	[34m$([39;49;00mCC[34m)[39;49;00m -shared$
[31mDESTSHARED[39;49;00m=	[34m$([39;49;00mBINLIBDEST[34m)[39;49;00m/lib-dynload$
$
[37m# Executable suffix (.exe on Windows and Mac OS X)[39;49;00m$
[31mEXE[39;49;00m=		$
[31mBUILDEXE[39;49;00m=	$
$
[37m# Short name and location for Mac OS X Python framework[39;49;00m$
[31mUNIVERSALSDK[39;49;00m=$
[31mPYTHONFRAMEWORK[39;49;00m=	$
[31mPYTHONFRAMEWORKDIR[39;49;00m=	no-framework$
[31mPYTHONFRAMEWORKPREFIX[39;49;00m=	$
[31mPYTHONFRAMEWORKINSTALLDIR[39;49;00m= $
[37m# Deployment target selected during configure, to be checked[39;49;00m$
[37m# by distutils. The export statement is needed to ensure that the[39;49;00m$
[37m# deployment target is active during build.[39;49;00m$
[31mMACOSX_DEPLOYMENT_TARGET[39;49;00m=$
[37m#export MACOSX_DEPLOYMENT_TARGET[39;49;00m$
$
[37m# Options to enable prebinding (for fast startup prior to Mac OS X 10.3)[39;49;00m$
[31mOTHER_LIBTOOL_OPT[39;49;00m=$
$
[37m# Environment to run shared python without installed libraries[39;49;00m$
[31mRUNSHARED[39;49;00m=       $
$
[37m# Modes for directories, executables and data files created by the[39;49;00m$
[37m# install process.  Default to user-only-writable for all file types.[39;49;00m$
[31mDIRMODE[39;49;00m=	[34m755[39;49;00m$
[31mEXEMODE[39;49;00m=	[34m755[39;49;00m$
[31mFILEMODE[39;49;00m=	[34m644[39;49;00m$
$
[37m# configure script arguments[39;49;00m$
[31mCONFIG_ARGS[39;49;00m=	[33m'--with-pydebug'[39;49;00m$
$
$
[37m# Subdirectories with code[39;49;00m$
[31mSRCDIRS[39;49;00m= 	Parser Grammar Objects Python Modules Mac$
$
[37m# Other subdirectories[39;49;00m$
[31mSUBDIRSTOO[39;49;00m=	Include Lib Misc Demo$
$
[37m# Files and directories to be distributed[39;49;00m$
[31mCONFIGFILES[39;49;00m=	configure configure.in acconfig.h pyconfig.h.in Makefile.pre.in$
[31mDISTFILES[39;49;00m=	README ChangeLog [34m$([39;49;00mCONFIGFILES[34m)[39;49;00m$
[31mDISTDIRS[39;49;00m=	[34m$([39;49;00mSUBDIRS[34m)[39;49;00m [34m$([39;49;00mSUBDIRSTOO[34m)[39;49;00m Ext-dummy$
[31mDIST[39;49;00m=		[34m$([39;49;00mDISTFILES[34m)[39;49;00m [34m$([39;49;00mDISTDIRS[34m)[39;49;00m$
$
$
[31mLIBRARY[39;49;00m=	libpython[34m$([39;49;00mVERSION[34m)[39;49;00m.a$
[31mLDLIBRARY[39;49;00m=      libpython[34m$([39;49;00mVERSION[34m)[39;49;00m.a$
[31mBLDLIBRARY[39;49;00m=     [34m$([39;49;00mLDLIBRARY[34m)[39;49;00m$
[31mDLLLIBRARY[39;49;00m=	$
[31mLDLIBRARYDIR[39;49;00m=   $
[31mINSTSONAME[39;49;00m=	[34m$([39;49;00mLDLIBRARY[34m)[39;49;00m$
$
$
[31mLIBS[39;49;00m=		-lpthread -ldl  -lutil$
[31mLIBM[39;49;00m=		-lm$
[31mLIBC[39;49;00m=		$
[31mSYSLIBS[39;49;00m=	[34m$([39;49;00mLIBM[34m)[39;49;00m [34m$([39;49;00mLIBC[34m)[39;49;00m$
[31mSHLIBS[39;49;00m=		[34m$([39;49;00mLIBS[34m)[39;49;00m$
$
[31mTHREADOBJ[39;49;00m=	Python/thread.o$
[31mDLINCLDIR[39;49;00m=	.$
[31mDYNLOADFILE[39;49;00m=	dynload_shlib.o$
[31mMACHDEP_OBJS[39;49;00m=	$
[31mUNICODE_OBJS[39;49;00m=   Objects/unicodeobject.o Objects/unicodectype.o$
$
[31mPYTHON[39;49;00m=		python[34m$([39;49;00mEXE[34m)[39;49;00m$
[31mBUILDPYTHON[39;49;00m=	python[34m$([39;49;00mBUILDEXE[34m)[39;49;00m$
$
[37m# === Definitions added by makesetup ===[39;49;00m$
$
[31mLOCALMODLIBS[39;49;00m=          $
[31mBASEMODLIBS[39;49;00m=$
[31mGLHACK[39;49;00m=-Dclear=__GLclear$
[31mPYTHONPATH[39;49;00m=[34m$([39;49;00mCOREPYTHONPATH[34m)[39;49;00m$
[31mCOREPYTHONPATH[39;49;00m=[34m$([39;49;00mDESTPATH[34m)[39;49;00m[34m$([39;49;00mSITEPATH[34m)[39;49;00m[34m$([39;49;00mTESTPATH[34m)[39;49;00m[34m$([39;49;00mMACHDEPPATH[34m)[39;49;00m[34m$([39;49;00mEXTRAMACHDEPPATH[34m)[39;49;00m[34m$([39;49;00mTKPATH[34m)[39;49;00m$
[31mTKPATH[39;49;00m=:lib-tk$
[31mEXTRAMACHDEPPATH[39;49;00m=$
[31mMACHDEPPATH[39;49;00m=:plat-[34m$([39;49;00mMACHDEP[34m)[39;49;00m$
[31mTESTPATH[39;49;00m=$
[31mSITEPATH[39;49;00m=$
[31mDESTPATH[39;49;00m=$
[31mMACHDESTLIB[39;49;00m=[34m$([39;49;00mBINLIBDEST[34m)[39;49;00m$
[31mDESTLIB[39;49;00m=[34m$([39;49;00mLIBDEST[34m)[39;49;00m$
$
$
$
[37m##########################################################################[39;49;00m$
[37m# Modules[39;49;00m$
[31mMODULE_OBJS[39;49;00m=	[33m\[39;49;00m$
		Modules/config.o [33m\[39;49;00m$
		Modules/getpath.o [33m\[39;49;00m$
		Modules/main.o [33m\[39;49;00m$
		Modules/gcmodule.o$
$
[37m# Used of signalmodule.o is not available[39;49;00m$
[31mSIGNAL_OBJS[39;49;00m=	$
$
$
[37m##########################################################################[39;49;00m$
[37m# Grammar[39;49;00m$
[31mGRAMMAR_H[39;49;00m=	[34m$([39;49;00msrcdir[34m)[39;49;00m/Include/graminit.h$
[31mGRAMMAR_C[39;49;00m=	[34m$([39;49;00msrcdir[34m)[39;49;00m/Python/graminit.c$
[31mGRAMMAR_INPUT[39;49;00m=	[34m$([39;49;00msrcdir[34m)[39;49;00m/Grammar/Grammar$
$
$
[37m##########################################################################[39;49;00m$
[37m# Parser[39;49;00m$
[31mPGEN[39;49;00m=		Parser/pgen[34m$([39;49;00mEXE[34m)[39;49;00m$
$
[31mPOBJS[39;49;00m=		[33m\[39;49;00m$
		Parser/acceler.o [33m\[39;49;00m$
		Parser/grammar1.o [33m\[39;49;00m$
		Parser/listnode.o [33m\[39;49;00m$
		Parser/node.o [33m\[39;49;00m$
		Parser/parser.o [33m\[39;49;00m$
		Parser/parsetok.o [33m\[39;49;00m$
		Parser/bitset.o [33m\[39;49;00m$
		Parser/metagrammar.o [33m\[39;49;00m$
		Parser/firstsets.o [33m\[39;49;00m$
		Parser/grammar.o [33m\[39;49;00m$
		Parser/pgen.o$
$
[31mPARSER_OBJS[39;49;00m=	[34m$([39;49;00mPOBJS[34m)[39;49;00m Parser/myreadline.o Parser/tokenizer.o$
$
[31mPGOBJS[39;49;00m=		[33m\[39;49;00m$
		Objects/obmalloc.o [33m\[39;49;00m$
		Python/mysnprintf.o [33m\[39;49;00m$
		Parser/tokenizer_pgen.o [33m\[39;49;00m$
		Parser/printgrammar.o [33m\[39;49;00m$
		Parser/pgenmain.o$
$
[31mPGENOBJS[39;49;00m=	[34m$([39;49;00mPGENMAIN[34m)[39;49;00m [34m$([39;49;00mPOBJS[34m)[39;49;00m [34m$([39;49;00mPGOBJS[34m)[39;49;00m$
$
[37m##########################################################################[39;49;00m$
[37m# AST[39;49;00m$
[31mAST_H_DIR[39;49;00m=	[34m$([39;49;00msrcdir[34m)[39;49;00m/Include$
[31mAST_H[39;49;00m=		[34m$([39;49;00mAST_H_DIR[34m)[39;49;00m/Python-ast.h$
[31mAST_C_DIR[39;49;00m=	[34m$([39;49;00msrcdir[34m)[39;49;00m/Python$
[31mAST_C[39;49;00m=		[34m$([39;49;00mAST_C_DIR[34m)[39;49;00m/Python-ast.c$
[31mAST_ASDL[39;49;00m=	[34m$([39;49;00msrcdir[34m)[39;49;00m/Parser/Python.asdl$
$
[31mASDLGEN_FILES[39;49;00m=	[34m$([39;49;00msrcdir[34m)[39;49;00m/Parser/asdl.py [34m$([39;49;00msrcdir[34m)[39;49;00m/Parser/asdl_c.py$
[37m# XXX Note that a build now requires Python exist before the build starts[39;49;00m$
[31mASDLGEN[39;49;00m=	[34m$([39;49;00msrcdir[34m)[39;49;00m/Parser/asdl_c.py$
$
[37m##########################################################################[39;49;00m$
[37m# Python[39;49;00m$
[31mPYTHON_OBJS[39;49;00m=	[33m\[39;49;00m$
		Python/Python-ast.o [33m\[39;49;00m$
		Python/asdl.o [33m\[39;49;00m$
		Python/ast.o [33m\[39;49;00m$
		Python/bltinmodule.o [33m\[39;49;00m$
		Python/ceval.o [33m\[39;49;00m$
		Python/compile.o [33m\[39;49;00m$
		Python/codecs.o [33m\[39;49;00m$
		Python/errors.o [33m\[39;49;00m$
		Python/frozen.o [33m\[39;49;00m$
		Python/frozenmain.o [33m\[39;49;00m$
		Python/future.o [33m\[39;49;00m$
		Python/getargs.o [33m\[39;49;00m$
		Python/getcompiler.o [33m\[39;49;00m$
		Python/getcopyright.o [33m\[39;49;00m$
		Python/getmtime.o [33m\[39;49;00m$
		Python/getplatform.o [33m\[39;49;00m$
		Python/getversion.o [33m\[39;49;00m$
		Python/graminit.o [33m\[39;49;00m$
		Python/import.o [33m\[39;49;00m$
		Python/importdl.o [33m\[39;49;00m$
		Python/marshal.o [33m\[39;49;00m$
		Python/modsupport.o [33m\[39;49;00m$
		Python/mystrtoul.o [33m\[39;49;00m$
		Python/mysnprintf.o [33m\[39;49;00m$
		Python/peephole.o [33m\[39;49;00m$
		Python/pyarena.o [33m\[39;49;00m$
		Python/pyfpe.o [33m\[39;49;00m$
		Python/pystate.o [33m\[39;49;00m$
		Python/pythonrun.o [33m\[39;49;00m$
		Python/structmember.o [33m\[39;49;00m$
		Python/symtable.o [33m\[39;49;00m$
		Python/sysmodule.o [33m\[39;49;00m$
		Python/traceback.o [33m\[39;49;00m$
		Python/getopt.o [33m\[39;49;00m$
		Python/pystrtod.o [33m\[39;49;00m$
		Python/[34m$([39;49;00mDYNLOADFILE[34m)[39;49;00m [33m\[39;49;00m$
		[34m$([39;49;00mMACHDEP_OBJS[34m)[39;49;00m [33m\[39;49;00m$
		[34m$([39;49;00mTHREADOBJ[34m)[39;49;00m$
$
$
[37m##########################################################################[39;49;00m$
[37m# Objects[39;49;00m$
[31mOBJECT_OBJS[39;49;00m=	[33m\[39;49;00m$
		Objects/abstract.o [33m\[39;49;00m$
		Objects/boolobject.o [33m\[39;49;00m$
		Objects/bufferobject.o [33m\[39;49;00m$
		Objects/cellobject.o [33m\[39;49;00m$
		Objects/classobject.o [33m\[39;49;00m$
		Objects/cobject.o [33m\[39;49;00m$
		Objects/codeobject.o [33m\[39;49;00m$
		Objects/complexobject.o [33m\[39;49;00m$
		Objects/descrobject.o [33m\[39;49;00m$
		Objects/enumobject.o [33m\[39;49;00m$
		Objects/exceptions.o [33m\[39;49;00m$
		Objects/genobject.o [33m\[39;49;00m$
		Objects/fileobject.o [33m\[39;49;00m$
		Objects/floatobject.o [33m\[39;49;00m$
		Objects/frameobject.o [33m\[39;49;00m$
		Objects/funcobject.o [33m\[39;49;00m$
		Objects/intobject.o [33m\[39;49;00m$
		Objects/iterobject.o [33m\[39;49;00m$
		Objects/listobject.o [33m\[39;49;00m$
		Objects/longobject.o [33m\[39;49;00m$
		Objects/dictobject.o [33m\[39;49;00m$
		Objects/methodobject.o [33m\[39;49;00m$
		Objects/moduleobject.o [33m\[39;49;00m$
		Objects/object.o [33m\[39;49;00m$
		Objects/obmalloc.o [33m\[39;49;00m$
		Objects/rangeobject.o [33m\[39;49;00m$
                Objects/setobject.o [33m\[39;49;00m$
		Objects/sliceobject.o [33m\[39;49;00m$
		Objects/stringobject.o [33m\[39;49;00m$
		Objects/structseq.o [33m\[39;49;00m$
		Objects/tupleobject.o [33m\[39;49;00m$
		Objects/typeobject.o [33m\[39;49;00m$
		Objects/weakrefobject.o [33m\[39;49;00m$
		[34m$([39;49;00mUNICODE_OBJS[34m)[39;49;00m$
$
$
[37m##########################################################################[39;49;00m$
[37m# objects that get linked into the Python library[39;49;00m$
[31mLIBRARY_OBJS[39;49;00m=	[33m\[39;49;00m$
		Modules/_typesmodule.o [33m\[39;49;00m$
		Modules/getbuildinfo.o [33m\[39;49;00m$
		[34m$([39;49;00mPARSER_OBJS[34m)[39;49;00m [33m\[39;49;00m$
		[34m$([39;49;00mOBJECT_OBJS[34m)[39;49;00m [33m\[39;49;00m$
		[34m$([39;49;00mPYTHON_OBJS[34m)[39;49;00m [33m\[39;49;00m$
		[34m$([39;49;00mMODULE_OBJS[34m)[39;49;00m [33m\[39;49;00m$
		[34m$([39;49;00mSIGNAL_OBJS[34m)[39;49;00m [33m\[39;49;00m$
		[34m$([39;49;00mMODOBJS[34m)[39;49;00m$
$
[37m#########################################################################[39;49;00m$
[37m# Rules[39;49;00m$
$
[37m# Default target[39;49;00m$
[32mall[39;49;00m:		[34m$([39;49;00m[31mBUILDPYTHON[39;49;00m[34m)[39;49;00m oldsharedmods sharedmods$
$
[37m# Build the interpreter[39;49;00m$
[32m$(BUILDPYTHON)[39;49;00m:	Modules/python.o [34m$([39;49;00m[31mLIBRARY[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31mLDLIBRARY[39;49;00m[34m)[39;49;00m$
		[34m$([39;49;00mLINKCC[34m)[39;49;00m [34m$([39;49;00mLDFLAGS[34m)[39;49;00m [34m$([39;49;00mLINKFORSHARED[34m)[39;49;00m -o [31m$@[39;49;00m [33m\[39;49;00m$
			Modules/python.o [33m\[39;49;00m$
			[34m$([39;49;00mBLDLIBRARY[34m)[39;49;00m [34m$([39;49;00mLIBS[34m)[39;49;00m [34m$([39;49;00mMODLIBS[34m)[39;49;00m [34m$([39;49;00mSYSLIBS[34m)[39;49;00m [34m$([39;49;00mLDLAST[34m)[39;49;00m$
$
[32mplatform[39;49;00m: [34m$([39;49;00m[31mBUILDPYTHON[39;49;00m[34m)[39;49;00m$
	[34m$([39;49;00mRUNSHARED[34m)[39;49;00m ./[34m$([39;49;00mBUILDPYTHON[34m)[39;49;00m -E -c [33m'import sys ; from distutils.util import get_platform ; print get_platform()+"-"+sys.version[0:3]'[39;49;00m >platform$
$
$
[37m# Build the shared modules[39;49;00m$
[32msharedmods[39;49;00m: [34m$([39;49;00m[31mBUILDPYTHON[39;49;00m[34m)[39;49;00m$
	@case [31m$$[39;49;00mMAKEFLAGS [34min[39;49;00m [33m\[39;49;00m$
	*-s*) [34m$([39;49;00mRUNSHARED[34m)[39;49;00m [31mCC[39;49;00m=[33m'$(CC)'[39;49;00m [31mLDSHARED[39;49;00m=[33m'$(BLDSHARED)'[39;49;00m [31mOPT[39;49;00m=[33m'$(OPT)'[39;49;00m ./[34m$([39;49;00mBUILDPYTHON[34m)[39;49;00m -E [34m$([39;49;00msrcdir[34m)[39;49;00m/setup.py -q build;; [33m\[39;49;00m$
	*) [34m$([39;49;00mRUNSHARED[34m)[39;49;00m [31mCC[39;49;00m=[33m'$(CC)'[39;49;00m [31mLDSHARED[39;49;00m=[33m'$(BLDSHARED)'[39;49;00m [31mOPT[39;49;00m=[33m'$(OPT)'[39;49;00m ./[34m$([39;49;00mBUILDPYTHON[34m)[39;49;00m -E [34m$([39;49;00msrcdir[34m)[39;49;00m/setup.py build;; [33m\[39;49;00m$
	[34mesac[39;49;00m$
$
[37m# Build static library[39;49;00m$
[37m# avoid long command lines, same as LIBRARY_OBJS[39;49;00m$
[32m$(LIBRARY)[39;49;00m: [34m$([39;49;00m[31mLIBRARY_OBJS[39;49;00m[34m)[39;49;00m$
	-rm -f [31m$@[39;49;00m$
	[34m$([39;49;00mAR[34m)[39;49;00m cr [31m$@[39;49;00m Modules/getbuildinfo.o$
	[34m$([39;49;00mAR[34m)[39;49;00m cr [31m$@[39;49;00m Modules/_typesmodule.o$
	[34m$([39;49;00mAR[34m)[39;49;00m cr [31m$@[39;49;00m [34m$([39;49;00mPARSER_OBJS[34m)[39;49;00m$
	[34m$([39;49;00mAR[34m)[39;49;00m cr [31m$@[39;49;00m [34m$([39;49;00mOBJECT_OBJS[34m)[39;49;00m$
	[34m$([39;49;00mAR[34m)[39;49;00m cr [31m$@[39;49;00m [34m$([39;49;00mPYTHON_OBJS[34m)[39;49;00m$
	[34m$([39;49;00mAR[34m)[39;49;00m cr [31m$@[39;49;00m [34m$([39;49;00mMODULE_OBJS[34m)[39;49;00m [34m$([39;49;00mSIGNAL_OBJS[34m)[39;49;00m$
	[34m$([39;49;00mAR[34m)[39;49;00m cr [31m$@[39;49;00m [34m$([39;49;00mMODOBJS[34m)[39;49;00m$
	[34m$([39;49;00mRANLIB[34m)[39;49;00m [31m$@[39;49;00m$
$
[32mlibpython$(VERSION).so[39;49;00m: [34m$([39;49;00m[31mLIBRARY_OBJS[39;49;00m[34m)[39;49;00m$
[36m	if test $(INSTSONAME) != $(LDLIBRARY); then \[39;49;00m$
[36m		$(LDSHARED) -Wl,-h$(INSTSONAME) -o $(INSTSONAME) $(LIBRARY_OBJS) $(SHLIBS) $(LIBC) $(LIBM); \[39;49;00m$
[36m		$(LN) -f $(INSTSONAME) $@; \[39;49;00m$
[36m	else\[39;49;00m$
[36m		$(LDSHARED) -o $@ $(LIBRARY_OBJS) $(SHLIBS) $(LIBC) $(LIBM); \[39;49;00m$
[36m	fi[39;49;00m$
$
[32mlibpython$(VERSION).sl[39;49;00m: [34m$([39;49;00m[31mLIBRARY_OBJS[39;49;00m[34m)[39;49;00m$
	[34m$([39;49;00mLDSHARED[34m)[39;49;00m -o [31m$@[39;49;00m [34m$([39;49;00mLIBRARY_OBJS[34m)[39;49;00m [34m$([39;49;00mSHLIBS[34m)[39;49;00m [34m$([39;49;00mLIBC[34m)[39;49;00m [34m$([39;49;00mLIBM[34m)[39;49;00m$
$
[37m# This rule is here for OPENSTEP/Rhapsody/MacOSX. It builds a temporary[39;49;00m$
[37m# minimal framework (not including the Lib directory and such) in the current[39;49;00m$
[37m# directory.[39;49;00m$
[31mRESSRCDIR[39;49;00m=[34m$([39;49;00msrcdir[34m)[39;49;00m/Mac/Resources/framework$
[32m$(PYTHONFRAMEWORKDIR)/Versions/$(VERSION)/$(PYTHONFRAMEWORK)[39;49;00m: \$
		[34m$([39;49;00m[31mLIBRARY[39;49;00m[34m)[39;49;00m \$
		[34m$([39;49;00m[31mRESSRCDIR[39;49;00m[34m)[39;49;00m/Info.plist \$
                [34m$([39;49;00m[31mRESSRCDIR[39;49;00m[34m)[39;49;00m/version.plist \$
                [34m$([39;49;00m[31mRESSRCDIR[39;49;00m[34m)[39;49;00m/English.lproj/InfoPlist.strings$
	[34m$([39;49;00mINSTALL[34m)[39;49;00m -d -m [34m$([39;49;00mDIRMODE[34m)[39;49;00m [34m$([39;49;00mPYTHONFRAMEWORKDIR[34m)[39;49;00m/Versions/[34m$([39;49;00mVERSION[34m)[39;49;00m$
[36m	if test "${UNIVERSALSDK}"; then \[39;49;00m$
[36m		$(CC) -o $(LDLIBRARY) -arch i386 -arch ppc -dynamiclib \[39;49;00m$
[36m			-isysroot "${UNIVERSALSDK}" \[39;49;00m$
[36m			-all_load $(LIBRARY) -Wl,-single_module \[39;49;00m$
[36m			-install_name $(DESTDIR)$(PYTHONFRAMEWORKINSTALLDIR)/Versions/$(VERSION)/Python \[39;49;00m$
[36m			-compatibility_version $(VERSION) \[39;49;00m$
[36m			-current_version $(VERSION); \[39;49;00m$
[36m        else \[39;49;00m$
[36m		libtool -o $(LDLIBRARY) -dynamic $(OTHER_LIBTOOL_OPT) $(LIBRARY) \[39;49;00m$
[36m			 ;\[39;49;00m$
[36m	fi[39;49;00m$
	[34m$([39;49;00mINSTALL[34m)[39;49;00m -d -m [34m$([39;49;00mDIRMODE[34m)[39;49;00m  [33m\[39;49;00m$
		[34m$([39;49;00mPYTHONFRAMEWORKDIR[34m)[39;49;00m/Versions/[34m$([39;49;00mVERSION[34m)[39;49;00m/Resources/English.lproj$
	[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m [34m$([39;49;00mRESSRCDIR[34m)[39;49;00m/Info.plist [33m\[39;49;00m$
		[34m$([39;49;00mPYTHONFRAMEWORKDIR[34m)[39;49;00m/Versions/[34m$([39;49;00mVERSION[34m)[39;49;00m/Resources/Info.plist$
	[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m [34m$([39;49;00mRESSRCDIR[34m)[39;49;00m/version.plist [33m\[39;49;00m$
		[34m$([39;49;00mPYTHONFRAMEWORKDIR[34m)[39;49;00m/Versions/[34m$([39;49;00mVERSION[34m)[39;49;00m/Resources/version.plist$
	[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m [34m$([39;49;00mRESSRCDIR[34m)[39;49;00m/English.lproj/InfoPlist.strings [33m\[39;49;00m$
		[34m$([39;49;00mPYTHONFRAMEWORKDIR[34m)[39;49;00m/Versions/[34m$([39;49;00mVERSION[34m)[39;49;00m/Resources/English.lproj/InfoPlist.strings$
	[34m$([39;49;00mLN[34m)[39;49;00m -fsn [34m$([39;49;00mVERSION[34m)[39;49;00m [34m$([39;49;00mPYTHONFRAMEWORKDIR[34m)[39;49;00m/Versions/Current$
	[34m$([39;49;00mLN[34m)[39;49;00m -fsn Versions/Current/[34m$([39;49;00mPYTHONFRAMEWORK[34m)[39;49;00m [34m$([39;49;00mPYTHONFRAMEWORKDIR[34m)[39;49;00m/[34m$([39;49;00mPYTHONFRAMEWORK[34m)[39;49;00m$
	[34m$([39;49;00mLN[34m)[39;49;00m -fsn Versions/Current/Headers [34m$([39;49;00mPYTHONFRAMEWORKDIR[34m)[39;49;00m/Headers$
	[34m$([39;49;00mLN[34m)[39;49;00m -fsn Versions/Current/Resources [34m$([39;49;00mPYTHONFRAMEWORKDIR[34m)[39;49;00m/Resources$
$
[37m# This rule builds the Cygwin Python DLL and import library if configured[39;49;00m$
[37m# for a shared core library; otherwise, this rule is a noop.[39;49;00m$
[32m$(DLLLIBRARY) libpython$(VERSION).dll.a[39;49;00m: [34m$([39;49;00m[31mLIBRARY_OBJS[39;49;00m[34m)[39;49;00m$
[36m	if test -n "$(DLLLIBRARY)"; then \[39;49;00m$
[36m		$(LDSHARED) -Wl,--out-implib=$@ -o $(DLLLIBRARY) $^ \[39;49;00m$
[36m			$(LIBS) $(MODLIBS) $(SYSLIBS); \[39;49;00m$
[36m	else true; \[39;49;00m$
[36m	fi[39;49;00m$
$
$
[32moldsharedmods[39;49;00m: [34m$([39;49;00m[31mSHAREDMODS[39;49;00m[34m)[39;49;00m$
$
$
[32mMakefile Modules/config.c[39;49;00m: Makefile.pre \$
				[34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/config.c.in \$
				[34m$([39;49;00m[31mMAKESETUP[39;49;00m[34m)[39;49;00m \$
				Modules/Setup.config \$
				Modules/Setup \$
				Modules/Setup.local$
	[34m$([39;49;00mSHELL[34m)[39;49;00m [34m$([39;49;00mMAKESETUP[34m)[39;49;00m -c [34m$([39;49;00msrcdir[34m)[39;49;00m/Modules/config.c.in [33m\[39;49;00m$
				-s Modules [33m\[39;49;00m$
				Modules/Setup.config [33m\[39;49;00m$
				Modules/Setup.local [33m\[39;49;00m$
				Modules/Setup$
	@mv config.c Modules$
	@echo [33m"The Makefile was updated, you may need to re-run make."[39;49;00m$
$
$
[32mModules/Setup[39;49;00m: [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/Setup.dist$
	@if [36mtest[39;49;00m -f Modules/Setup; [34mthen[39;49;00m [33m\[39;49;00m$
		[36mecho[39;49;00m [33m"-----------------------------------------------"[39;49;00m; [33m\[39;49;00m$
		[36mecho[39;49;00m [33m"Modules/Setup.dist is newer than Modules/Setup;"[39;49;00m; [33m\[39;49;00m$
		[36mecho[39;49;00m [33m"check to make sure you have all the updates you"[39;49;00m; [33m\[39;49;00m$
		[36mecho[39;49;00m [33m"need in your Modules/Setup file."[39;49;00m; [33m\[39;49;00m$
		[36mecho[39;49;00m [33m"Usually, copying Setup.dist to Setup will work."[39;49;00m; [33m\[39;49;00m$
		[36mecho[39;49;00m [33m"-----------------------------------------------"[39;49;00m; [33m\[39;49;00m$
	[34mfi[39;49;00m$
$
[37m############################################################################[39;49;00m$
[37m# Special rules for object files[39;49;00m$
$
[32mModules/getbuildinfo.o[39;49;00m: [34m$([39;49;00m[31mPARSER_OBJS[39;49;00m[34m)[39;49;00m \$
		[34m$([39;49;00m[31mOBJECT_OBJS[39;49;00m[34m)[39;49;00m \$
		[34m$([39;49;00m[31mPYTHON_OBJS[39;49;00m[34m)[39;49;00m \$
		[34m$([39;49;00m[31mMODULE_OBJS[39;49;00m[34m)[39;49;00m \$
		[34m$([39;49;00m[31mSIGNAL_OBJS[39;49;00m[34m)[39;49;00m \$
		[34m$([39;49;00m[31mMODOBJS[39;49;00m[34m)[39;49;00m \$
		[34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/getbuildinfo.c$
	[34m$([39;49;00mCC[34m)[39;49;00m -c [34m$([39;49;00mPY_CFLAGS[34m)[39;49;00m -DSVNVERSION=[33m\"[39;49;00m[33m`[39;49;00m[31mLC_ALL[39;49;00m=C [34m$([39;49;00mSVNVERSION[34m)[39;49;00m[33m`[39;49;00m[33m\"[39;49;00m -o [31m$@[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/Modules/getbuildinfo.c$
$
[32mModules/getpath.o[39;49;00m: [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/getpath.c Makefile$
	[34m$([39;49;00mCC[34m)[39;49;00m -c [34m$([39;49;00mPY_CFLAGS[34m)[39;49;00m -DPYTHONPATH=[33m'"$(PYTHONPATH)"'[39;49;00m [33m\[39;49;00m$
		-DPREFIX=[33m'"$(prefix)"'[39;49;00m [33m\[39;49;00m$
		-DEXEC_PREFIX=[33m'"$(exec_prefix)"'[39;49;00m [33m\[39;49;00m$
		-DVERSION=[33m'"$(VERSION)"'[39;49;00m [33m\[39;49;00m$
		-DVPATH=[33m'"$(VPATH)"'[39;49;00m [33m\[39;49;00m$
		-o [31m$@[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/Modules/getpath.c$
$
[32mModules/python.o[39;49;00m: [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/python.c$
	[34m$([39;49;00mMAINCC[34m)[39;49;00m -c [34m$([39;49;00mPY_CFLAGS[34m)[39;49;00m -o [31m$@[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/Modules/python.c$
$
$
[32m$(GRAMMAR_H) $(GRAMMAR_C)[39;49;00m: [34m$([39;49;00m[31mPGEN[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31mGRAMMAR_INPUT[39;49;00m[34m)[39;49;00m$
		-[34m$([39;49;00mPGEN[34m)[39;49;00m [34m$([39;49;00mGRAMMAR_INPUT[34m)[39;49;00m [34m$([39;49;00mGRAMMAR_H[34m)[39;49;00m [34m$([39;49;00mGRAMMAR_C[34m)[39;49;00m$
$
[32m$(PGEN)[39;49;00m:	[34m$([39;49;00m[31mPGENOBJS[39;49;00m[34m)[39;49;00m$
		[34m$([39;49;00mCC[34m)[39;49;00m [34m$([39;49;00mOPT[34m)[39;49;00m [34m$([39;49;00mLDFLAGS[34m)[39;49;00m [34m$([39;49;00mPGENOBJS[34m)[39;49;00m [34m$([39;49;00mLIBS[34m)[39;49;00m -o [34m$([39;49;00mPGEN[34m)[39;49;00m$
$
[32mParser/grammar.o[39;49;00m:	[34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Parser/grammar.c \$
				[34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Include/token.h \$
				[34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Include/grammar.h$
[32mParser/metagrammar.o[39;49;00m:	[34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Parser/metagrammar.c$
$
[32mParser/tokenizer_pgen.o[39;49;00m:	[34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Parser/tokenizer.c$
$
[32mParser/pgenmain.o[39;49;00m:	[34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Include/parsetok.h$
$
[32m$(AST_H)[39;49;00m: [34m$([39;49;00m[31mAST_ASDL[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31mASDLGEN_FILES[39;49;00m[34m)[39;49;00m$
	[34m$([39;49;00mASDLGEN[34m)[39;49;00m -h [34m$([39;49;00mAST_H_DIR[34m)[39;49;00m [34m$([39;49;00mAST_ASDL[34m)[39;49;00m$
$
[32m$(AST_C)[39;49;00m: [34m$([39;49;00m[31mAST_ASDL[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31mASDLGEN_FILES[39;49;00m[34m)[39;49;00m$
	[34m$([39;49;00mASDLGEN[34m)[39;49;00m -c [34m$([39;49;00mAST_C_DIR[34m)[39;49;00m [34m$([39;49;00mAST_ASDL[34m)[39;49;00m$
$
[32mPython/compile.o Python/symtable.o[39;49;00m: [34m$([39;49;00m[31mGRAMMAR_H[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31mAST_H[39;49;00m[34m)[39;49;00m$
$
[32mPython/getplatform.o[39;49;00m: [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Python/getplatform.c$
		[34m$([39;49;00mCC[34m)[39;49;00m -c [34m$([39;49;00mPY_CFLAGS[34m)[39;49;00m -DPLATFORM=[33m'"$(MACHDEP)"'[39;49;00m -o [31m$@[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/Python/getplatform.c$
$
[32mPython/importdl.o[39;49;00m: [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Python/importdl.c$
		[34m$([39;49;00mCC[34m)[39;49;00m -c [34m$([39;49;00mPY_CFLAGS[34m)[39;49;00m -I[34m$([39;49;00mDLINCLDIR[34m)[39;49;00m -o [31m$@[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/Python/importdl.c$
$
[32mObjects/unicodectype.o[39;49;00m:	[34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Objects/unicodectype.c \$
				[34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Objects/unicodetype_db.h$
$
[37m############################################################################[39;49;00m$
[37m# Header files[39;49;00m$
$
[31mPYTHON_HEADERS[39;49;00m= [33m\[39;49;00m$
		Include/Python.h [33m\[39;49;00m$
		Include/Python-ast.h [33m\[39;49;00m$
		Include/asdl.h [33m\[39;49;00m$
		Include/abstract.h [33m\[39;49;00m$
		Include/boolobject.h [33m\[39;49;00m$
		Include/bufferobject.h [33m\[39;49;00m$
		Include/ceval.h [33m\[39;49;00m$
		Include/classobject.h [33m\[39;49;00m$
		Include/cobject.h [33m\[39;49;00m$
		Include/code.h [33m\[39;49;00m$
		Include/codecs.h [33m\[39;49;00m$
		Include/compile.h [33m\[39;49;00m$
		Include/complexobject.h [33m\[39;49;00m$
		Include/descrobject.h [33m\[39;49;00m$
		Include/dictobject.h [33m\[39;49;00m$
		Include/enumobject.h [33m\[39;49;00m$
		Include/genobject.h [33m\[39;49;00m$
		Include/fileobject.h [33m\[39;49;00m$
		Include/floatobject.h [33m\[39;49;00m$
		Include/funcobject.h [33m\[39;49;00m$
		Include/import.h [33m\[39;49;00m$
		Include/intobject.h [33m\[39;49;00m$
		Include/intrcheck.h [33m\[39;49;00m$
		Include/iterobject.h [33m\[39;49;00m$
		Include/listobject.h [33m\[39;49;00m$
		Include/longobject.h [33m\[39;49;00m$
		Include/methodobject.h [33m\[39;49;00m$
		Include/modsupport.h [33m\[39;49;00m$
		Include/moduleobject.h [33m\[39;49;00m$
		Include/object.h [33m\[39;49;00m$
		Include/objimpl.h [33m\[39;49;00m$
		Include/parsetok.h [33m\[39;49;00m$
		Include/patchlevel.h [33m\[39;49;00m$
		Include/pyarena.h [33m\[39;49;00m$
		Include/pydebug.h [33m\[39;49;00m$
		Include/pyerrors.h [33m\[39;49;00m$
		Include/pyfpe.h [33m\[39;49;00m$
		Include/pymem.h [33m\[39;49;00m$
		Include/pyport.h [33m\[39;49;00m$
		Include/pystate.h [33m\[39;49;00m$
		Include/pythonrun.h [33m\[39;49;00m$
		Include/rangeobject.h [33m\[39;49;00m$
                Include/setobject.h [33m\[39;49;00m$
		Include/sliceobject.h [33m\[39;49;00m$
		Include/stringobject.h [33m\[39;49;00m$
		Include/structseq.h [33m\[39;49;00m$
		Include/structmember.h [33m\[39;49;00m$
		Include/symtable.h [33m\[39;49;00m$
		Include/sysmodule.h [33m\[39;49;00m$
		Include/traceback.h [33m\[39;49;00m$
		Include/tupleobject.h [33m\[39;49;00m$
		Include/unicodeobject.h [33m\[39;49;00m$
		Include/weakrefobject.h [33m\[39;49;00m$
		pyconfig.h$
$
[32m$(LIBRARY_OBJS) $(MODOBJS) Modules/python.o[39;49;00m: [34m$([39;49;00m[31mPYTHON_HEADERS[39;49;00m[34m)[39;49;00m$
$
$
[37m######################################################################[39;49;00m$
$
[37m# Test the interpreter (twice, once without .pyc files, once with)[39;49;00m$
[37m# In the past, we've had problems where bugs in the marshalling or[39;49;00m$
[37m# elsewhere caused bytecode read from .pyc files to behave differently[39;49;00m$
[37m# than bytecode generated directly from a .py source file.  Sometimes[39;49;00m$
[37m# the bytecode read from a .pyc file had the bug, somtimes the directly[39;49;00m$
[37m# generated bytecode.  This is sometimes a very shy bug needing a lot of[39;49;00m$
[37m# sample data.[39;49;00m$
$
[31mTESTOPTS[39;49;00m=	-l [34m$([39;49;00mEXTRATESTOPTS[34m)[39;49;00m$
[31mTESTPROG[39;49;00m=	[34m$([39;49;00msrcdir[34m)[39;49;00m/Lib/test/regrtest.py$
[31mTESTPYTHON[39;49;00m=	[34m$([39;49;00mRUNSHARED[34m)[39;49;00m ./[34m$([39;49;00mBUILDPYTHON[34m)[39;49;00m -E -tt$
[32mtest[39;49;00m:		all platform$
		-find [34m$([39;49;00msrcdir[34m)[39;49;00m/Lib -name [33m'*.py[co]'[39;49;00m -print | xargs rm -f$
		-[34m$([39;49;00mTESTPYTHON[34m)[39;49;00m [34m$([39;49;00mTESTPROG[34m)[39;49;00m [34m$([39;49;00mTESTOPTS[34m)[39;49;00m$
		[34m$([39;49;00mTESTPYTHON[34m)[39;49;00m [34m$([39;49;00mTESTPROG[34m)[39;49;00m [34m$([39;49;00mTESTOPTS[34m)[39;49;00m$
$
[32mtestall[39;49;00m:	all platform$
		-find [34m$([39;49;00msrcdir[34m)[39;49;00m/Lib -name [33m'*.py[co]'[39;49;00m -print | xargs rm -f$
		-[34m$([39;49;00mTESTPYTHON[34m)[39;49;00m [34m$([39;49;00mTESTPROG[34m)[39;49;00m [34m$([39;49;00mTESTOPTS[34m)[39;49;00m -uall$
		[34m$([39;49;00mTESTPYTHON[34m)[39;49;00m [34m$([39;49;00mTESTPROG[34m)[39;49;00m [34m$([39;49;00mTESTOPTS[34m)[39;49;00m -uall$
$
[37m#  Run the unitests for both architectures in a Universal build on OSX[39;49;00m$
[37m#  Must be run on an Intel box.[39;49;00m$
[32mtestuniversal[39;49;00m:	all platform$
[36m		if [ `arch` != 'i386' ];then \[39;49;00m$
[36m			echo "This can only be used on OSX/i386" ;\[39;49;00m$
[36m			exit 1 ;\[39;49;00m$
[36m		fi[39;49;00m$
		-find [34m$([39;49;00msrcdir[34m)[39;49;00m/Lib -name [33m'*.py[co]'[39;49;00m -print | xargs rm -f$
		-[34m$([39;49;00mTESTPYTHON[34m)[39;49;00m [34m$([39;49;00mTESTPROG[34m)[39;49;00m [34m$([39;49;00mTESTOPTS[34m)[39;49;00m -uall$
		[34m$([39;49;00mTESTPYTHON[34m)[39;49;00m [34m$([39;49;00mTESTPROG[34m)[39;49;00m [34m$([39;49;00mTESTOPTS[34m)[39;49;00m -uall$
		[34m$([39;49;00mRUNSHARED[34m)[39;49;00m /usr/libexec/oah/translate ./[34m$([39;49;00mBUILDPYTHON[34m)[39;49;00m -E -tt [34m$([39;49;00mTESTPROG[34m)[39;49;00m [34m$([39;49;00mTESTOPTS[34m)[39;49;00m -uall$
$
$
[37m# Like testall, but with a single pass only[39;49;00m$
[32mbuildbottest[39;49;00m:	all platform$
		[34m$([39;49;00mTESTPYTHON[34m)[39;49;00m [34m$([39;49;00mTESTPROG[34m)[39;49;00m [34m$([39;49;00mTESTOPTS[34m)[39;49;00m -uall -rw$
$
[31mQUICKTESTOPTS[39;49;00m=	[34m$([39;49;00mTESTOPTS[34m)[39;49;00m -x test_thread test_signal test_strftime [33m\[39;49;00m$
		test_unicodedata test_re test_sre test_select test_poll [33m\[39;49;00m$
		test_linuxaudiodev test_struct test_sunaudiodev test_zlib$
[32mquicktest[39;49;00m:	all platform$
		-find [34m$([39;49;00msrcdir[34m)[39;49;00m/Lib -name [33m'*.py[co]'[39;49;00m -print | xargs rm -f$
		-[34m$([39;49;00mTESTPYTHON[34m)[39;49;00m [34m$([39;49;00mTESTPROG[34m)[39;49;00m [34m$([39;49;00mQUICKTESTOPTS[34m)[39;49;00m$
		[34m$([39;49;00mTESTPYTHON[34m)[39;49;00m [34m$([39;49;00mTESTPROG[34m)[39;49;00m [34m$([39;49;00mQUICKTESTOPTS[34m)[39;49;00m$
$
[31mMEMTESTOPTS[39;49;00m=    [34m$([39;49;00mQUICKTESTOPTS[34m)[39;49;00m -x test_dl test___all__ test_fork1 [33m\[39;49;00m$
		test_longexp$
[32mmemtest[39;49;00m:	all platform$
		-rm -f [34m$([39;49;00msrcdir[34m)[39;49;00m/Lib/test/*.py[co]$
		-[34m$([39;49;00mTESTPYTHON[34m)[39;49;00m [34m$([39;49;00mTESTPROG[34m)[39;49;00m [34m$([39;49;00mMEMTESTOPTS[34m)[39;49;00m$
		[34m$([39;49;00mTESTPYTHON[34m)[39;49;00m [34m$([39;49;00mTESTPROG[34m)[39;49;00m [34m$([39;49;00mMEMTESTOPTS[34m)[39;49;00m$
$
[37m# Install everything[39;49;00m$
[32minstall[39;49;00m:	 altinstall bininstall maninstall $
$
[37m# Install almost everything without disturbing previous versions[39;49;00m$
[32maltinstall[39;49;00m:	 altbininstall libinstall inclinstall libainstall \$
                sharedinstall oldsharedinstall $
$
[37m# Install shared libraries enabled by Setup[39;49;00m$
[31mDESTDIRS[39;49;00m=	[34m$([39;49;00mexec_prefix[34m)[39;49;00m [34m$([39;49;00mLIBDIR[34m)[39;49;00m [34m$([39;49;00mBINLIBDEST[34m)[39;49;00m [34m$([39;49;00mDESTSHARED[34m)[39;49;00m$
$
[32moldsharedinstall[39;49;00m: [34m$([39;49;00m[31mDESTSHARED[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31mSHAREDMODS[39;49;00m[34m)[39;49;00m$
		@for i [34min[39;49;00m X [34m$([39;49;00mSHAREDMODS[34m)[39;49;00m; [34mdo[39;49;00m [33m\[39;49;00m$
[36m		  if test $$i != X; then \[39;49;00m$
[36m		    echo $(INSTALL_SHARED) $$i $(DESTSHARED)/`basename $$i`; \[39;49;00m$
[36m		    $(INSTALL_SHARED) $$i $(DESTDIR)$(DESTSHARED)/`basename $$i`; \[39;49;00m$
[36m		  fi; \[39;49;00m$
[36m		done[39;49;00m$
$
[32m$(DESTSHARED)[39;49;00m:$
		@for i [34min[39;49;00m [34m$([39;49;00mDESTDIRS[34m)[39;49;00m; [33m\[39;49;00m$
		[34mdo[39;49;00m [33m\[39;49;00m$
[36m			if test ! -d $(DESTDIR)$$i; then \[39;49;00m$
[36m				echo "Creating directory $$i"; \[39;49;00m$
[36m				$(INSTALL) -d -m $(DIRMODE) $(DESTDIR)$$i; \[39;49;00m$
[36m			else    true; \[39;49;00m$
[36m			fi; \[39;49;00m$
[36m		done[39;49;00m$
$
$
[37m# Install the interpreter (by creating a hard link to python$(VERSION))[39;49;00m$
[32mbininstall[39;49;00m:	altbininstall$
	-if [36mtest[39;49;00m -f [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mBINDIR[34m)[39;49;00m/[34m$([39;49;00mPYTHON[34m)[39;49;00m -o -h [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mBINDIR[34m)[39;49;00m/[34m$([39;49;00mPYTHON[34m)[39;49;00m; [33m\[39;49;00m$
	[34mthen[39;49;00m rm -f [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mBINDIR[34m)[39;49;00m/[34m$([39;49;00mPYTHON[34m)[39;49;00m; [33m\[39;49;00m$
[36m	else true; \[39;49;00m$
[36m	fi[39;49;00m$
	([36mcd[39;49;00m [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mBINDIR[34m)[39;49;00m; [34m$([39;49;00mLN[34m)[39;49;00m python[34m$([39;49;00mVERSION[34m)[39;49;00m[34m$([39;49;00mEXE[34m)[39;49;00m [34m$([39;49;00mPYTHON[34m)[39;49;00m)$
	([36mcd[39;49;00m [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mBINDIR[34m)[39;49;00m; [34m$([39;49;00mLN[34m)[39;49;00m -sf python[34m$([39;49;00mVERSION[34m)[39;49;00m-config python-config)$
$
[37m# Install the interpreter with $(VERSION) affixed[39;49;00m$
[37m# This goes into $(exec_prefix)[39;49;00m$
[32maltbininstall[39;49;00m:	[34m$([39;49;00m[31mBUILDPYTHON[39;49;00m[34m)[39;49;00m$
	@for i [34min[39;49;00m [34m$([39;49;00mBINDIR[34m)[39;49;00m [34m$([39;49;00mLIBDIR[34m)[39;49;00m; [33m\[39;49;00m$
	[34mdo[39;49;00m [33m\[39;49;00m$
[36m		if test ! -d $(DESTDIR)$$i; then \[39;49;00m$
[36m			echo "Creating directory $$i"; \[39;49;00m$
[36m			$(INSTALL) -d -m $(DIRMODE) $(DESTDIR)$$i; \[39;49;00m$
[36m		else	true; \[39;49;00m$
[36m		fi; \[39;49;00m$
[36m	done[39;49;00m$
	[34m$([39;49;00mINSTALL_PROGRAM[34m)[39;49;00m [34m$([39;49;00mBUILDPYTHON[34m)[39;49;00m [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mBINDIR[34m)[39;49;00m/python[34m$([39;49;00mVERSION[34m)[39;49;00m[34m$([39;49;00mEXE[34m)[39;49;00m$
[36m	if test -f libpython$(VERSION)$(SO); then \[39;49;00m$
[36m		if test "$(SO)" = .dll; then \[39;49;00m$
[36m			$(INSTALL_SHARED) libpython$(VERSION)$(SO) $(DESTDIR)$(BINDIR); \[39;49;00m$
[36m		else \[39;49;00m$
[36m			$(INSTALL_SHARED) libpython$(VERSION)$(SO) $(DESTDIR)$(LIBDIR)/$(INSTSONAME); \[39;49;00m$
[36m			if test libpython$(VERSION)$(SO) != $(INSTSONAME); then \[39;49;00m$
[36m				(cd $(DESTDIR)$(LIBDIR); $(LN) -sf $(INSTSONAME) libpython$(VERSION)$(SO)); \[39;49;00m$
[36m			fi \[39;49;00m$
[36m		fi; \[39;49;00m$
[36m	else	true; \[39;49;00m$
[36m	fi[39;49;00m$
$
[37m# Install the manual page[39;49;00m$
[32mmaninstall[39;49;00m:$
	@for i [34min[39;49;00m [34m$([39;49;00mMANDIR[34m)[39;49;00m [34m$([39;49;00mMANDIR[34m)[39;49;00m/man1; [33m\[39;49;00m$
	[34mdo[39;49;00m [33m\[39;49;00m$
[36m		if test ! -d $(DESTDIR)$$i; then \[39;49;00m$
[36m			echo "Creating directory $$i"; \[39;49;00m$
[36m			$(INSTALL) -d -m $(DIRMODE) $(DESTDIR)$$i; \[39;49;00m$
[36m		else	true; \[39;49;00m$
[36m		fi; \[39;49;00m$
[36m	done[39;49;00m$
	[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/Misc/python.man [33m\[39;49;00m$
		[34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mMANDIR[34m)[39;49;00m/man1/python.1$
$
[37m# Install the library[39;49;00m$
[31mPLATDIR[39;49;00m=	plat-[34m$([39;49;00mMACHDEP[34m)[39;49;00m$
[31mEXTRAPLATDIR[39;49;00m= $
[31mEXTRAMACHDEPPATH[39;49;00m=$
[31mMACHDEPS[39;49;00m=	[34m$([39;49;00mPLATDIR[34m)[39;49;00m [34m$([39;49;00mEXTRAPLATDIR[34m)[39;49;00m$
[31mXMLLIBSUBDIRS[39;49;00m=  xml xml/dom xml/etree xml/parsers xml/sax$
[31mPLATMACDIRS[39;49;00m= plat-mac plat-mac/Carbon plat-mac/lib-scriptpackages [33m\[39;49;00m$
	plat-mac/lib-scriptpackages/_builtinSuites [33m\[39;49;00m$
	plat-mac/lib-scriptpackages/CodeWarrior [33m\[39;49;00m$
	plat-mac/lib-scriptpackages/Explorer [33m\[39;49;00m$
	plat-mac/lib-scriptpackages/Finder [33m\[39;49;00m$
	plat-mac/lib-scriptpackages/Netscape [33m\[39;49;00m$
	plat-mac/lib-scriptpackages/StdSuites [33m\[39;49;00m$
	plat-mac/lib-scriptpackages/SystemEvents [33m\[39;49;00m$
	plat-mac/lib-scriptpackages/Terminal $
[31mPLATMACPATH[39;49;00m=:plat-mac:plat-mac/lib-scriptpackages$
[31mLIBSUBDIRS[39;49;00m=	lib-tk site-packages [36mtest[39;49;00m test/output test/data [33m\[39;49;00m$
		test/decimaltestdata [33m\[39;49;00m$
		encodings compiler hotshot [33m\[39;49;00m$
		email email/mime email/test email/test/data [33m\[39;49;00m$
		sqlite3 sqlite3/test [33m\[39;49;00m$
		logging bsddb bsddb/test csv wsgiref [33m\[39;49;00m$
		ctypes ctypes/test ctypes/macholib idlelib idlelib/Icons [33m\[39;49;00m$
		distutils distutils/command distutils/tests [34m$([39;49;00mXMLLIBSUBDIRS[34m)[39;49;00m [33m\[39;49;00m$
		setuptools setuptools/command setuptools/tests setuptools.egg-info [33m\[39;49;00m$
		curses [34m$([39;49;00mMACHDEPS[34m)[39;49;00m$
[32mlibinstall[39;49;00m:	[34m$([39;49;00m[31mBUILDPYTHON[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Lib/[34m$([39;49;00m[31mPLATDIR[39;49;00m[34m)[39;49;00m$
	@for i [34min[39;49;00m [34m$([39;49;00mSCRIPTDIR[34m)[39;49;00m [34m$([39;49;00mLIBDEST[34m)[39;49;00m; [33m\[39;49;00m$
	[34mdo[39;49;00m [33m\[39;49;00m$
[36m		if test ! -d $(DESTDIR)$$i; then \[39;49;00m$
[36m			echo "Creating directory $$i"; \[39;49;00m$
[36m			$(INSTALL) -d -m $(DIRMODE) $(DESTDIR)$$i; \[39;49;00m$
[36m		else	true; \[39;49;00m$
[36m		fi; \[39;49;00m$
[36m	done[39;49;00m$
	@for d [34min[39;49;00m [34m$([39;49;00mLIBSUBDIRS[34m)[39;49;00m; [33m\[39;49;00m$
	[34mdo[39;49;00m [33m\[39;49;00m$
		[31ma[39;49;00m=[34m$([39;49;00msrcdir[34m)[39;49;00m/Lib/[31m$$[39;49;00md; [33m\[39;49;00m$
[36m		if test ! -d $$a; then continue; else true; fi; \[39;49;00m$
[36m		b=$(LIBDEST)/$$d; \[39;49;00m$
[36m		if test ! -d $(DESTDIR)$$b; then \[39;49;00m$
[36m			echo "Creating directory $$b"; \[39;49;00m$
[36m			$(INSTALL) -d -m $(DIRMODE) $(DESTDIR)$$b; \[39;49;00m$
[36m		else	true; \[39;49;00m$
[36m		fi; \[39;49;00m$
[36m	done[39;49;00m$
	@for i [34min[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/Lib/*.py [34m$([39;49;00msrcdir[34m)[39;49;00m/Lib/*.doc [34m$([39;49;00msrcdir[34m)[39;49;00m/Lib/*.egg-info ; [33m\[39;49;00m$
	[34mdo[39;49;00m [33m\[39;49;00m$
[36m		if test -x $$i; then \[39;49;00m$
[36m			$(INSTALL_SCRIPT) $$i $(DESTDIR)$(LIBDEST); \[39;49;00m$
[36m			echo $(INSTALL_SCRIPT) $$i $(LIBDEST); \[39;49;00m$
[36m		else \[39;49;00m$
[36m			$(INSTALL_DATA) $$i $(DESTDIR)$(LIBDEST); \[39;49;00m$
[36m			echo $(INSTALL_DATA) $$i $(LIBDEST); \[39;49;00m$
[36m		fi; \[39;49;00m$
[36m	done[39;49;00m$
	@for d [34min[39;49;00m [34m$([39;49;00mLIBSUBDIRS[34m)[39;49;00m; [33m\[39;49;00m$
	[34mdo[39;49;00m [33m\[39;49;00m$
		[31ma[39;49;00m=[34m$([39;49;00msrcdir[34m)[39;49;00m/Lib/[31m$$[39;49;00md; [33m\[39;49;00m$
[36m		if test ! -d $$a; then continue; else true; fi; \[39;49;00m$
[36m		if test `ls $$a | wc -l` -lt 1; then continue; fi; \[39;49;00m$
[36m		b=$(LIBDEST)/$$d; \[39;49;00m$
[36m		for i in $$a/*; \[39;49;00m$
[36m		do \[39;49;00m$
[36m			case $$i in \[39;49;00m$
[36m			*CVS) ;; \[39;49;00m$
[36m			*.py[co]) ;; \[39;49;00m$
[36m			*.orig) ;; \[39;49;00m$
[36m			*~) ;; \[39;49;00m$
[36m			*) \[39;49;00m$
[36m				if test -d $$i; then continue; fi; \[39;49;00m$
[36m				if test -x $$i; then \[39;49;00m$
[36m				    echo $(INSTALL_SCRIPT) $$i $$b; \[39;49;00m$
[36m				    $(INSTALL_SCRIPT) $$i $(DESTDIR)$$b; \[39;49;00m$
[36m				else \[39;49;00m$
[36m				    echo $(INSTALL_DATA) $$i $$b; \[39;49;00m$
[36m				    $(INSTALL_DATA) $$i $(DESTDIR)$$b; \[39;49;00m$
[36m				fi;; \[39;49;00m$
[36m			esac; \[39;49;00m$
[36m		done; \[39;49;00m$
[36m	done[39;49;00m$
	[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/LICENSE [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBDEST[34m)[39;49;00m/LICENSE.txt$
	[31mPYTHONPATH[39;49;00m=[34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBDEST[34m)[39;49;00m  [34m$([39;49;00mRUNSHARED[34m)[39;49;00m [33m\[39;49;00m$
		./[34m$([39;49;00mBUILDPYTHON[34m)[39;49;00m -Wi -tt [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBDEST[34m)[39;49;00m/compileall.py [33m\[39;49;00m$
		-d [34m$([39;49;00mLIBDEST[34m)[39;49;00m -f [33m\[39;49;00m$
		-x [33m'bad_coding|badsyntax|site-packages'[39;49;00m [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBDEST[34m)[39;49;00m$
	[31mPYTHONPATH[39;49;00m=[34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBDEST[34m)[39;49;00m [34m$([39;49;00mRUNSHARED[34m)[39;49;00m [33m\[39;49;00m$
		./[34m$([39;49;00mBUILDPYTHON[34m)[39;49;00m -Wi -tt -O [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBDEST[34m)[39;49;00m/compileall.py [33m\[39;49;00m$
		-d [34m$([39;49;00mLIBDEST[34m)[39;49;00m -f [33m\[39;49;00m$
		-x [33m'bad_coding|badsyntax|site-packages'[39;49;00m [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBDEST[34m)[39;49;00m$
	-PYTHONPATH=[34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBDEST[34m)[39;49;00m  [34m$([39;49;00mRUNSHARED[34m)[39;49;00m [33m\[39;49;00m$
		./[34m$([39;49;00mBUILDPYTHON[34m)[39;49;00m -Wi -t [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBDEST[34m)[39;49;00m/compileall.py [33m\[39;49;00m$
		-d [34m$([39;49;00mLIBDEST[34m)[39;49;00m/site-packages -f [33m\[39;49;00m$
		-x badsyntax [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBDEST[34m)[39;49;00m/site-packages$
	-PYTHONPATH=[34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBDEST[34m)[39;49;00m [34m$([39;49;00mRUNSHARED[34m)[39;49;00m [33m\[39;49;00m$
		./[34m$([39;49;00mBUILDPYTHON[34m)[39;49;00m -Wi -t -O [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBDEST[34m)[39;49;00m/compileall.py [33m\[39;49;00m$
		-d [34m$([39;49;00mLIBDEST[34m)[39;49;00m/site-packages -f [33m\[39;49;00m$
		-x badsyntax [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBDEST[34m)[39;49;00m/site-packages$
$
[37m# Create the PLATDIR source directory, if one wasn't distributed..[39;49;00m$
[32m$(srcdir)/Lib/$(PLATDIR)[39;49;00m:$
	mkdir [34m$([39;49;00msrcdir[34m)[39;49;00m/Lib/[34m$([39;49;00mPLATDIR[34m)[39;49;00m$
	cp [34m$([39;49;00msrcdir[34m)[39;49;00m/Lib/plat-generic/regen [34m$([39;49;00msrcdir[34m)[39;49;00m/Lib/[34m$([39;49;00mPLATDIR[34m)[39;49;00m/regen$
	[36mexport[39;49;00m PATH; [31mPATH[39;49;00m=[33m"[39;49;00m[33m`pwd`:[39;49;00m[31m$$[39;49;00m[33mPATH[39;49;00m[33m"[39;49;00m; [33m\[39;49;00m$
	[36mexport[39;49;00m PYTHONPATH; [31mPYTHONPATH[39;49;00m=[33m"`pwd`/Lib"[39;49;00m; [33m\[39;49;00m$
	[36mexport[39;49;00m DYLD_FRAMEWORK_PATH; [31mDYLD_FRAMEWORK_PATH[39;49;00m=[33m"`pwd`"[39;49;00m; [33m\[39;49;00m$
	[36mexport[39;49;00m EXE; [31mEXE[39;49;00m=[33m"[39;49;00m[34m$([39;49;00mBUILDEXE[34m)[39;49;00m[33m"[39;49;00m; [33m\[39;49;00m$
	[36mcd[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/Lib/[34m$([39;49;00mPLATDIR[34m)[39;49;00m; ./regen$
$
[37m# Install the include files[39;49;00m$
[31mINCLDIRSTOMAKE[39;49;00m=[34m$([39;49;00mINCLUDEDIR[34m)[39;49;00m [34m$([39;49;00mCONFINCLUDEDIR[34m)[39;49;00m [34m$([39;49;00mINCLUDEPY[34m)[39;49;00m [34m$([39;49;00mCONFINCLUDEPY[34m)[39;49;00m$
[32minclinstall[39;49;00m:$
	@for i [34min[39;49;00m [34m$([39;49;00mINCLDIRSTOMAKE[34m)[39;49;00m; [33m\[39;49;00m$
	[34mdo[39;49;00m [33m\[39;49;00m$
[36m		if test ! -d $(DESTDIR)$$i; then \[39;49;00m$
[36m			echo "Creating directory $$i"; \[39;49;00m$
[36m			$(INSTALL) -d -m $(DIRMODE) $(DESTDIR)$$i; \[39;49;00m$
[36m		else	true; \[39;49;00m$
[36m		fi; \[39;49;00m$
[36m	done[39;49;00m$
	@for i [34min[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/Include/*.h; [33m\[39;49;00m$
	[34mdo[39;49;00m [33m\[39;49;00m$
		[36mecho[39;49;00m [34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m [31m$$[39;49;00mi [34m$([39;49;00mINCLUDEPY[34m)[39;49;00m; [33m\[39;49;00m$
		[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m [31m$$[39;49;00mi [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mINCLUDEPY[34m)[39;49;00m; [33m\[39;49;00m$
	[34mdone[39;49;00m$
	[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m pyconfig.h [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mCONFINCLUDEPY[34m)[39;49;00m/pyconfig.h$
$
[37m# Install the library and miscellaneous stuff needed for extending/embedding[39;49;00m$
[37m# This goes into $(exec_prefix)[39;49;00m$
[31mLIBPL[39;49;00m=		[34m$([39;49;00mLIBP[34m)[39;49;00m/config$
[32mlibainstall[39;49;00m:	all$
	@for i [34min[39;49;00m [34m$([39;49;00mLIBDIR[34m)[39;49;00m [34m$([39;49;00mLIBP[34m)[39;49;00m [34m$([39;49;00mLIBPL[34m)[39;49;00m; [33m\[39;49;00m$
	[34mdo[39;49;00m [33m\[39;49;00m$
[36m		if test ! -d $(DESTDIR)$$i; then \[39;49;00m$
[36m			echo "Creating directory $$i"; \[39;49;00m$
[36m			$(INSTALL) -d -m $(DIRMODE) $(DESTDIR)$$i; \[39;49;00m$
[36m		else	true; \[39;49;00m$
[36m		fi; \[39;49;00m$
[36m	done[39;49;00m$
	@if [36mtest[39;49;00m -d [34m$([39;49;00mLIBRARY[34m)[39;49;00m; [34mthen[39;49;00m :; [34melse[39;49;00m [33m\[39;49;00m$
[36m		if test "$(PYTHONFRAMEWORKDIR)" = no-framework; then \[39;49;00m$
[36m			if test "$(SO)" = .dll; then \[39;49;00m$
[36m				$(INSTALL_DATA) $(LDLIBRARY) $(DESTDIR)$(LIBPL) ; \[39;49;00m$
[36m			else \[39;49;00m$
[36m				$(INSTALL_DATA) $(LIBRARY) $(DESTDIR)$(LIBPL)/$(LIBRARY) ; \[39;49;00m$
[36m				$(RANLIB) $(DESTDIR)$(LIBPL)/$(LIBRARY) ; \[39;49;00m$
[36m			fi; \[39;49;00m$
[36m		else \[39;49;00m$
[36m			echo Skip install of $(LIBRARY) - use make frameworkinstall; \[39;49;00m$
[36m		fi; \[39;49;00m$
[36m	fi[39;49;00m$
	[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m Modules/config.c [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m/config.c$
	[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m Modules/python.o [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m/python.o$
	[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/Modules/config.c.in [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m/config.c.in$
	[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m Makefile [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m/Makefile$
	[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m Modules/Setup [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m/Setup$
	[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m Modules/Setup.local [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m/Setup.local$
	[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m Modules/Setup.config [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m/Setup.config$
	[34m$([39;49;00mINSTALL_SCRIPT[34m)[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/Modules/makesetup [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m/makesetup$
	[34m$([39;49;00mINSTALL_SCRIPT[34m)[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/install-sh [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m/install-sh$
[37m	# Substitution happens here, as the completely-expanded BINDIR[39;49;00m$
[37m	# is not available in configure[39;49;00m$
	sed -e [33m"[39;49;00m[33ms,@EXENAME@,[39;49;00m[34m$([39;49;00mBINDIR[34m)[39;49;00m[33m/python[39;49;00m[34m$([39;49;00mVERSION[34m)[39;49;00m[34m$([39;49;00mEXE[34m)[39;49;00m[33m,[39;49;00m[33m"[39;49;00m < [34m$([39;49;00msrcdir[34m)[39;49;00m/Misc/python-config.in >python-config$
	[34m$([39;49;00mINSTALL_SCRIPT[34m)[39;49;00m python-config [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mBINDIR[34m)[39;49;00m/python[34m$([39;49;00mVERSION[34m)[39;49;00m-config$
	rm python-config$
	@if [ -s Modules/python.exp -a [33m\[39;49;00m$
		[33m"[39;49;00m[33m`echo [39;49;00m[34m$([39;49;00mMACHDEP[34m)[39;49;00m[33m | sed 's/^\(...\).*/\1/'`[39;49;00m[33m"[39;49;00m = [33m"aix"[39;49;00m ]; [34mthen[39;49;00m [33m\[39;49;00m$
		echo; [36mecho[39;49;00m [33m"Installing support files for building shared extension modules on AIX:"[39;49;00m; [33m\[39;49;00m$
		[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m Modules/python.exp		[33m\[39;49;00m$
				[34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m/python.exp;		[33m\[39;49;00m$
		echo; [36mecho[39;49;00m [33m"[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m[33m/python.exp[39;49;00m[33m"[39;49;00m;		[33m\[39;49;00m$
		[34m$([39;49;00mINSTALL_SCRIPT[34m)[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/Modules/makexp_aix	[33m\[39;49;00m$
				[34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m/makexp_aix;		[33m\[39;49;00m$
		[36mecho[39;49;00m [33m"[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m[33m/makexp_aix[39;49;00m[33m"[39;49;00m;			[33m\[39;49;00m$
		[34m$([39;49;00mINSTALL_SCRIPT[34m)[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/Modules/ld_so_aix	[33m\[39;49;00m$
				[34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m/ld_so_aix;		[33m\[39;49;00m$
		[36mecho[39;49;00m [33m"[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m[33m/ld_so_aix[39;49;00m[33m"[39;49;00m;			[33m\[39;49;00m$
		echo; [36mecho[39;49;00m [33m"See Misc/AIX-NOTES for details."[39;49;00m;	[33m\[39;49;00m$
[36m	else true; \[39;49;00m$
[36m	fi[39;49;00m$
	@case [33m"[39;49;00m[34m$([39;49;00mMACHDEP[34m)[39;49;00m[33m"[39;49;00m [34min[39;49;00m beos*) [33m\[39;49;00m$
		echo; [36mecho[39;49;00m [33m"Installing support files for building shared extension modules on BeOS:"[39;49;00m; [33m\[39;49;00m$
		[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m Misc/BeOS-NOTES [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m/README;	[33m\[39;49;00m$
		echo; [36mecho[39;49;00m [33m"[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m[33m/README[39;49;00m[33m"[39;49;00m;			[33m\[39;49;00m$
		[34m$([39;49;00mINSTALL_SCRIPT[34m)[39;49;00m Modules/ar_beos [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m/ar_beos; [33m\[39;49;00m$
		[36mecho[39;49;00m [33m"[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m[33m/ar_beos[39;49;00m[33m"[39;49;00m;			[33m\[39;49;00m$
		[34m$([39;49;00mINSTALL_SCRIPT[34m)[39;49;00m Modules/ld_so_beos [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m/ld_so_beos; [33m\[39;49;00m$
		[36mecho[39;49;00m [33m"[39;49;00m[34m$([39;49;00mLIBPL[34m)[39;49;00m[33m/ld_so_beos[39;49;00m[33m"[39;49;00m;			[33m\[39;49;00m$
		echo; [36mecho[39;49;00m [33m"See Misc/BeOS-NOTES for details."[39;49;00m;	[33m\[39;49;00m$
		;; [33m\[39;49;00m$
	[34mesac[39;49;00m$
$
[37m# Install the dynamically loadable modules[39;49;00m$
[37m# This goes into $(exec_prefix)[39;49;00m$
[32msharedinstall[39;49;00m:$
	[34m$([39;49;00mRUNSHARED[34m)[39;49;00m ./[34m$([39;49;00mBUILDPYTHON[34m)[39;49;00m -E [34m$([39;49;00msrcdir[34m)[39;49;00m/setup.py install [33m\[39;49;00m$
	   	--prefix=[34m$([39;49;00mprefix[34m)[39;49;00m [33m\[39;49;00m$
		--install-scripts=[34m$([39;49;00mBINDIR[34m)[39;49;00m [33m\[39;49;00m$
		--install-platlib=[34m$([39;49;00mDESTSHARED[34m)[39;49;00m [33m\[39;49;00m$
		--root=/[34m$([39;49;00mDESTDIR[34m)[39;49;00m$
$
[37m# Here are a couple of targets for MacOSX again, to install a full[39;49;00m$
[37m# framework-based Python. frameworkinstall installs everything, the[39;49;00m$
[37m# subtargets install specific parts. Much of the actual work is offloaded to[39;49;00m$
[37m# the Makefile in Mac[39;49;00m$
[37m#[39;49;00m$
[37m#[39;49;00m$
[37m# This target is here for backward compatiblity, previous versions of Python[39;49;00m$
[37m# hadn't integrated framework installation in the normal install process.[39;49;00m$
[32mframeworkinstall[39;49;00m: install$
$
[37m# On install, we re-make the framework[39;49;00m$
[37m# structure in the install location, /Library/Frameworks/ or the argument to[39;49;00m$
[37m# --enable-framework. If --enable-framework has been specified then we have[39;49;00m$
[37m# automatically set prefix to the location deep down in the framework, so we[39;49;00m$
[37m# only have to cater for the structural bits of the framework.[39;49;00m$
$
[32mframeworkinstallframework[39;49;00m: frameworkinstallstructure install frameworkinstallmaclib$
$
[32mframeworkinstallstructure[39;49;00m:	[34m$([39;49;00m[31mLDLIBRARY[39;49;00m[34m)[39;49;00m$
	@if [36mtest[39;49;00m [33m"[39;49;00m[34m$([39;49;00mPYTHONFRAMEWORKDIR[34m)[39;49;00m[33m"[39;49;00m = no-framework; [34mthen[39;49;00m [33m\[39;49;00m$
		[36mecho[39;49;00m Not configured with --enable-framework; [33m\[39;49;00m$
		[36mexit[39;49;00m [34m1[39;49;00m; [33m\[39;49;00m$
[36m	else true; \[39;49;00m$
[36m	fi[39;49;00m$
	@for i [34min[39;49;00m [34m$([39;49;00mprefix[34m)[39;49;00m/Resources/English.lproj [34m$([39;49;00mprefix[34m)[39;49;00m/lib; [34mdo[39;49;00m[33m\[39;49;00m$
[36m		if test ! -d $(DESTDIR)$$i; then \[39;49;00m$
[36m			echo "Creating directory $(DESTDIR)$$i"; \[39;49;00m$
[36m			$(INSTALL) -d -m $(DIRMODE) $(DESTDIR)$$i; \[39;49;00m$
[36m		else	true; \[39;49;00m$
[36m		fi; \[39;49;00m$
[36m	done[39;49;00m$
	[34m$([39;49;00mLN[34m)[39;49;00m -fsn include/python[34m$([39;49;00mVERSION[34m)[39;49;00m [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mprefix[34m)[39;49;00m/Headers$
	[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m [34m$([39;49;00mRESSRCDIR[34m)[39;49;00m/Info.plist [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mprefix[34m)[39;49;00m/Resources/Info.plist$
	[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m [34m$([39;49;00mRESSRCDIR[34m)[39;49;00m/version.plist [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mprefix[34m)[39;49;00m/Resources/version.plist$
	[34m$([39;49;00mINSTALL_DATA[34m)[39;49;00m [34m$([39;49;00mRESSRCDIR[34m)[39;49;00m/English.lproj/InfoPlist.strings [33m\[39;49;00m$
		[34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mprefix[34m)[39;49;00m/Resources/English.lproj/InfoPlist.strings$
	[34m$([39;49;00mLN[34m)[39;49;00m -fsn [34m$([39;49;00mVERSION[34m)[39;49;00m [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mPYTHONFRAMEWORKINSTALLDIR[34m)[39;49;00m/Versions/Current$
	[34m$([39;49;00mLN[34m)[39;49;00m -fsn Versions/Current/Python [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mPYTHONFRAMEWORKINSTALLDIR[34m)[39;49;00m/Python$
	[34m$([39;49;00mLN[34m)[39;49;00m -fsn Versions/Current/Headers [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mPYTHONFRAMEWORKINSTALLDIR[34m)[39;49;00m/Headers$
	[34m$([39;49;00mLN[34m)[39;49;00m -fsn Versions/Current/Resources [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mPYTHONFRAMEWORKINSTALLDIR[34m)[39;49;00m/Resources$
	[34m$([39;49;00mINSTALL_SHARED[34m)[39;49;00m [34m$([39;49;00mLDLIBRARY[34m)[39;49;00m [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mPYTHONFRAMEWORKPREFIX[34m)[39;49;00m/[34m$([39;49;00mLDLIBRARY[34m)[39;49;00m$
$
[37m# This installs Mac/Lib into the framework[39;49;00m$
[37m# Install a number of symlinks to keep software that expects a normal unix[39;49;00m$
[37m# install (which includes python-config) happy.[39;49;00m$
[32mframeworkinstallmaclib[39;49;00m:$
	ln -fs [33m"../../../Python"[39;49;00m [33m"[39;49;00m[34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mprefix[34m)[39;49;00m[33m/lib/python[39;49;00m[34m$([39;49;00mVERSION[34m)[39;49;00m[33m/config/libpython[39;49;00m[34m$([39;49;00mVERSION[34m)[39;49;00m[33m.a[39;49;00m[33m"[39;49;00m$
	[36mcd[39;49;00m Mac && [34m$([39;49;00mMAKE[34m)[39;49;00m installmacsubtree [31mDESTDIR[39;49;00m=[33m"[39;49;00m[34m$([39;49;00mDESTDIR[34m)[39;49;00m[33m"[39;49;00m$
$
[37m# This installs the IDE, the Launcher and other apps into /Applications[39;49;00m$
[32mframeworkinstallapps[39;49;00m:$
	[36mcd[39;49;00m Mac && [34m$([39;49;00mMAKE[34m)[39;49;00m installapps [31mDESTDIR[39;49;00m=[33m"[39;49;00m[34m$([39;49;00mDESTDIR[34m)[39;49;00m[33m"[39;49;00m$
$
[37m# This install the unix python and pythonw tools in /usr/local/bin[39;49;00m$
[32mframeworkinstallunixtools[39;49;00m:$
	[36mcd[39;49;00m Mac && [34m$([39;49;00mMAKE[34m)[39;49;00m installunixtools [31mDESTDIR[39;49;00m=[33m"[39;49;00m[34m$([39;49;00mDESTDIR[34m)[39;49;00m[33m"[39;49;00m$
$
[32mframeworkaltinstallunixtools[39;49;00m:$
	[36mcd[39;49;00m Mac && [34m$([39;49;00mMAKE[34m)[39;49;00m altinstallunixtools [31mDESTDIR[39;49;00m=[33m"[39;49;00m[34m$([39;49;00mDESTDIR[34m)[39;49;00m[33m"[39;49;00m$
$
[37m# This installs the Demos and Tools into the applications directory.[39;49;00m$
[37m# It is not part of a normal frameworkinstall[39;49;00m$
[32mframeworkinstallextras[39;49;00m:$
	[36mcd[39;49;00m Mac && Make installextras [31mDESTDIR[39;49;00m=[33m"[39;49;00m[34m$([39;49;00mDESTDIR[34m)[39;49;00m[33m"[39;49;00m$
$
[37m# This installs a few of the useful scripts in Tools/scripts[39;49;00m$
[32mscriptsinstall[39;49;00m:$
	[31mSRCDIR[39;49;00m=[34m$([39;49;00msrcdir[34m)[39;49;00m [34m$([39;49;00mRUNSHARED[34m)[39;49;00m [33m\[39;49;00m$
	./[34m$([39;49;00mBUILDPYTHON[34m)[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/Tools/scripts/setup.py install [33m\[39;49;00m$
	--prefix=[34m$([39;49;00mprefix[34m)[39;49;00m [33m\[39;49;00m$
	--install-scripts=[34m$([39;49;00mBINDIR[34m)[39;49;00m [33m\[39;49;00m$
	--root=/[34m$([39;49;00mDESTDIR[34m)[39;49;00m$
$
[37m# Build the toplevel Makefile[39;49;00m$
[32mMakefile.pre[39;49;00m: Makefile.pre.in config.status$
	[31mCONFIG_FILES[39;49;00m=Makefile.pre [31mCONFIG_HEADERS[39;49;00m= [34m$([39;49;00mSHELL[34m)[39;49;00m config.status$
	[34m$([39;49;00mMAKE[34m)[39;49;00m -f Makefile.pre Makefile$
$
[37m# Run the configure script.[39;49;00m$
[32mconfig.status[39;49;00m:	[34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/configure$
	[34m$([39;49;00mSHELL[34m)[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/configure [34m$([39;49;00mCONFIG_ARGS[34m)[39;49;00m$
$
[32m.PRECIOUS[39;49;00m: config.status [34m$([39;49;00m[31mBUILDPYTHON[39;49;00m[34m)[39;49;00m Makefile Makefile.pre$
$
[37m# Some make's put the object file in the current directory[39;49;00m$
[32m.c.o[39;49;00m:$
	[34m$([39;49;00mCC[34m)[39;49;00m -c [34m$([39;49;00mPY_CFLAGS[34m)[39;49;00m -o [31m$@[39;49;00m $<$
$
[37m# Run reindent on the library[39;49;00m$
[32mreindent[39;49;00m:$
	./python[34m$([39;49;00mEXEEXT[34m)[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m/Tools/scripts/reindent.py -r [34m$([39;49;00msrcdir[34m)[39;49;00m/Lib$
$
[37m# Rerun configure with the same options as it was run last time,[39;49;00m$
[37m# provided the config.status script exists[39;49;00m$
[32mrecheck[39;49;00m:$
	[34m$([39;49;00mSHELL[34m)[39;49;00m config.status --recheck$
	[34m$([39;49;00mSHELL[34m)[39;49;00m config.status$
$
[37m# Rebuild the configure script from configure.in; also rebuild pyconfig.h.in[39;49;00m$
[32mautoconf[39;49;00m:$
	([36mcd[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m; autoconf)$
	([36mcd[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m; autoheader)$
$
[37m# Create a tags file for vi[39;49;00m$
[32mtags[39;49;00m::$
	[36mcd[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m; [33m\[39;49;00m$
	ctags -w -t Include/*.h; [33m\[39;49;00m$
	[34mfor[39;49;00m i [34min[39;49;00m [34m$([39;49;00mSRCDIRS[34m)[39;49;00m; [34mdo[39;49;00m ctags -w -t -a [31m$$[39;49;00mi/*.[ch]; [33m\[39;49;00m$
	[34mdone[39;49;00m; [33m\[39;49;00m$
	sort -o tags tags$
$
[37m# Create a tags file for GNU Emacs[39;49;00m$
[32mTAGS[39;49;00m::$
	[36mcd[39;49;00m [34m$([39;49;00msrcdir[34m)[39;49;00m; [33m\[39;49;00m$
	etags Include/*.h; [33m\[39;49;00m$
	[34mfor[39;49;00m i [34min[39;49;00m [34m$([39;49;00mSRCDIRS[34m)[39;49;00m; [34mdo[39;49;00m etags -a [31m$$[39;49;00mi/*.[ch]; [34mdone[39;49;00m$
$
[37m# Sanitation targets -- clean leaves libraries, executables and tags[39;49;00m$
[37m# files, which clobber removes those as well[39;49;00m$
[32mpycremoval[39;49;00m:$
	find [34m$([39;49;00msrcdir[34m)[39;49;00m -name [33m'*.py[co]'[39;49;00m -exec rm -f {} [33m';'[39;49;00m$
$
[32mclean[39;49;00m: pycremoval$
	find . -name [33m'*.o'[39;49;00m -exec rm -f {} [33m';'[39;49;00m$
	find . -name [33m'*.s[ol]'[39;49;00m -exec rm -f {} [33m';'[39;49;00m$
	find [34m$([39;49;00msrcdir[34m)[39;49;00m/build -name [33m'fficonfig.h'[39;49;00m -exec rm -f {} [33m';'[39;49;00m || [36mtrue[39;49;00m$
	find [34m$([39;49;00msrcdir[34m)[39;49;00m/build -name [33m'fficonfig.py'[39;49;00m -exec rm -f {} [33m';'[39;49;00m || [36mtrue[39;49;00m$
$
[32mclobber[39;49;00m: clean$
	-rm -f [34m$([39;49;00mBUILDPYTHON[34m)[39;49;00m [34m$([39;49;00mPGEN[34m)[39;49;00m [34m$([39;49;00mLIBRARY[34m)[39;49;00m [34m$([39;49;00mLDLIBRARY[34m)[39;49;00m [34m$([39;49;00mDLLLIBRARY[34m)[39;49;00m [33m\[39;49;00m$
		tags TAGS [33m\[39;49;00m$
		config.cache config.log pyconfig.h Modules/config.c$
	-rm -rf build platform$
	-rm -rf [34m$([39;49;00mPYTHONFRAMEWORKDIR[34m)[39;49;00m$
$
[37m# Make things extra clean, before making a distribution:[39;49;00m$
[37m# remove all generated files, even Makefile[.pre][39;49;00m$
[37m# Keep configure and Python-ast.[ch], it's possible they can't be generated[39;49;00m$
[32mdistclean[39;49;00m: clobber$
	-rm -f core Makefile Makefile.pre config.status [33m\[39;49;00m$
		Modules/Setup Modules/Setup.local Modules/Setup.config$
	find [34m$([39;49;00msrcdir[34m)[39;49;00m [33m'('[39;49;00m -name [33m'*.fdc'[39;49;00m -o -name [33m'*~'[39;49;00m [33m\[39;49;00m$
			   -o -name [33m'[@,#]*'[39;49;00m -o -name [33m'*.old'[39;49;00m [33m\[39;49;00m$
			   -o -name [33m'*.orig'[39;49;00m -o -name [33m'*.rej'[39;49;00m [33m\[39;49;00m$
			   -o -name [33m'*.bak'[39;49;00m [33m')'[39;49;00m [33m\[39;49;00m$
			   -exec rm -f {} [33m';'[39;49;00m$
$
[37m# Check for smelly exported symbols (not starting with Py/_Py)[39;49;00m$
[32msmelly[39;49;00m: all$
	nm -p [34m$([39;49;00mLIBRARY[34m)[39;49;00m | [33m\[39;49;00m$
		sed -n [33m"/ [TDB] /s/.* //p"[39;49;00m | grep -v [33m"^_*Py"[39;49;00m | sort -u; [33m\[39;49;00m$
$
[37m# Find files with funny names[39;49;00m$
[32mfunny[39;49;00m:$
	find [34m$([39;49;00mDISTDIRS[34m)[39;49;00m -type d [33m\[39;49;00m$
		-o -name [33m'*.[chs]'[39;49;00m [33m\[39;49;00m$
		-o -name [33m'*.py'[39;49;00m [33m\[39;49;00m$
		-o -name [33m'*.doc'[39;49;00m [33m\[39;49;00m$
		-o -name [33m'*.sty'[39;49;00m [33m\[39;49;00m$
		-o -name [33m'*.bib'[39;49;00m [33m\[39;49;00m$
		-o -name [33m'*.dat'[39;49;00m [33m\[39;49;00m$
		-o -name [33m'*.el'[39;49;00m [33m\[39;49;00m$
		-o -name [33m'*.fd'[39;49;00m [33m\[39;49;00m$
		-o -name [33m'*.in'[39;49;00m [33m\[39;49;00m$
		-o -name [33m'*.tex'[39;49;00m [33m\[39;49;00m$
		-o -name [33m'*,[vpt]'[39;49;00m [33m\[39;49;00m$
		-o -name [33m'Setup'[39;49;00m [33m\[39;49;00m$
		-o -name [33m'Setup.*'[39;49;00m [33m\[39;49;00m$
		-o -name README [33m\[39;49;00m$
		-o -name Makefile [33m\[39;49;00m$
		-o -name ChangeLog [33m\[39;49;00m$
		-o -name Repository [33m\[39;49;00m$
		-o -name Root [33m\[39;49;00m$
		-o -name Entries [33m\[39;49;00m$
		-o -name Tag [33m\[39;49;00m$
		-o -name tags [33m\[39;49;00m$
		-o -name TAGS [33m\[39;49;00m$
		-o -name .cvsignore [33m\[39;49;00m$
		-o -name MANIFEST [33m\[39;49;00m$
		-o -print$
$
[37m# Dependencies[39;49;00m$
$
[32mPython/thread.o[39;49;00m:  [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Python/thread_atheos.h [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Python/thread_beos.h [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Python/thread_cthread.h [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Python/thread_foobar.h [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Python/thread_lwp.h [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Python/thread_nt.h [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Python/thread_os2.h [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Python/thread_pth.h [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Python/thread_pthread.h [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Python/thread_sgi.h [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Python/thread_solaris.h [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Python/thread_wince.h$
$
[37m# Declare targets that aren't real files[39;49;00m$
[32m.PHONY[39;49;00m: all sharedmods oldsharedmods test quicktest memtest$
[32m.PHONY[39;49;00m: install altinstall oldsharedinstall bininstall altbininstall$
[32m.PHONY[39;49;00m: maninstall libinstall inclinstall libainstall sharedinstall$
[32m.PHONY[39;49;00m: frameworkinstall frameworkinstallframework frameworkinstallstructure$
[32m.PHONY[39;49;00m: frameworkinstallmaclib frameworkinstallapps frameworkinstallunixtools$
[32m.PHONY[39;49;00m: frameworkaltinstallunixtools recheck autoconf clean clobber distclean $
[32m.PHONY[39;49;00m: smelly funny$
$
[37m# IF YOU PUT ANYTHING HERE IT WILL GO AWAY[39;49;00m$
$
[37m# Rules appended by makedepend[39;49;00m$
$
[32mModules/threadmodule.o[39;49;00m: [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/threadmodule.c; [34m$([39;49;00m[31mCC[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31mPY_CFLAGS[39;49;00m[34m)[39;49;00m  -c [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/threadmodule.c -o Modules/threadmodule.o$
[32mModules/threadmodule$(SO)[39;49;00m:  Modules/threadmodule.o; [34m$([39;49;00m[31mLDSHARED[39;49;00m[34m)[39;49;00m  Modules/threadmodule.o   -o Modules/threadmodule[34m$([39;49;00m[31mSO[39;49;00m[34m)[39;49;00m$
[32mModules/signalmodule.o[39;49;00m: [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/signalmodule.c; [34m$([39;49;00m[31mCC[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31mPY_CFLAGS[39;49;00m[34m)[39;49;00m  -c [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/signalmodule.c -o Modules/signalmodule.o$
[32mModules/signalmodule$(SO)[39;49;00m:  Modules/signalmodule.o; [34m$([39;49;00m[31mLDSHARED[39;49;00m[34m)[39;49;00m  Modules/signalmodule.o   -o Modules/signalmodule[34m$([39;49;00m[31mSO[39;49;00m[34m)[39;49;00m$
[32mModules/posixmodule.o[39;49;00m: [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/posixmodule.c; [34m$([39;49;00m[31mCC[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31mPY_CFLAGS[39;49;00m[34m)[39;49;00m  -c [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/posixmodule.c -o Modules/posixmodule.o$
[32mModules/posixmodule$(SO)[39;49;00m:  Modules/posixmodule.o; [34m$([39;49;00m[31mLDSHARED[39;49;00m[34m)[39;49;00m  Modules/posixmodule.o   -o Modules/posixmodule[34m$([39;49;00m[31mSO[39;49;00m[34m)[39;49;00m$
[32mModules/errnomodule.o[39;49;00m: [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/errnomodule.c; [34m$([39;49;00m[31mCC[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31mPY_CFLAGS[39;49;00m[34m)[39;49;00m  -c [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/errnomodule.c -o Modules/errnomodule.o$
[32mModules/errnomodule$(SO)[39;49;00m:  Modules/errnomodule.o; [34m$([39;49;00m[31mLDSHARED[39;49;00m[34m)[39;49;00m  Modules/errnomodule.o   -o Modules/errnomodule[34m$([39;49;00m[31mSO[39;49;00m[34m)[39;49;00m$
[32mModules/pwdmodule.o[39;49;00m: [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/pwdmodule.c; [34m$([39;49;00m[31mCC[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31mPY_CFLAGS[39;49;00m[34m)[39;49;00m  -c [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/pwdmodule.c -o Modules/pwdmodule.o$
[32mModules/pwdmodule$(SO)[39;49;00m:  Modules/pwdmodule.o; [34m$([39;49;00m[31mLDSHARED[39;49;00m[34m)[39;49;00m  Modules/pwdmodule.o   -o Modules/pwdmodule[34m$([39;49;00m[31mSO[39;49;00m[34m)[39;49;00m$
[32mModules/_sre.o[39;49;00m: [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/_sre.c; [34m$([39;49;00m[31mCC[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31mPY_CFLAGS[39;49;00m[34m)[39;49;00m  -c [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/_sre.c -o Modules/_sre.o$
[32mModules/_sre$(SO)[39;49;00m:  Modules/_sre.o; [34m$([39;49;00m[31mLDSHARED[39;49;00m[34m)[39;49;00m  Modules/_sre.o   -o Modules/_sre[34m$([39;49;00m[31mSO[39;49;00m[34m)[39;49;00m$
[32mModules/_codecsmodule.o[39;49;00m: [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/_codecsmodule.c; [34m$([39;49;00m[31mCC[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31mPY_CFLAGS[39;49;00m[34m)[39;49;00m  -c [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/_codecsmodule.c -o Modules/_codecsmodule.o$
[32mModules/_codecsmodule$(SO)[39;49;00m:  Modules/_codecsmodule.o; [34m$([39;49;00m[31mLDSHARED[39;49;00m[34m)[39;49;00m  Modules/_codecsmodule.o   -o Modules/_codecsmodule[34m$([39;49;00m[31mSO[39;49;00m[34m)[39;49;00m$
[32mModules/zipimport.o[39;49;00m: [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/zipimport.c; [34m$([39;49;00m[31mCC[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31mPY_CFLAGS[39;49;00m[34m)[39;49;00m  -c [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/zipimport.c -o Modules/zipimport.o$
[32mModules/zipimport$(SO)[39;49;00m:  Modules/zipimport.o; [34m$([39;49;00m[31mLDSHARED[39;49;00m[34m)[39;49;00m  Modules/zipimport.o   -o Modules/zipimport[34m$([39;49;00m[31mSO[39;49;00m[34m)[39;49;00m$
[32mModules/symtablemodule.o[39;49;00m: [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/symtablemodule.c; [34m$([39;49;00m[31mCC[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31mPY_CFLAGS[39;49;00m[34m)[39;49;00m  -c [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/symtablemodule.c -o Modules/symtablemodule.o$
[32mModules/_symtablemodule$(SO)[39;49;00m:  Modules/symtablemodule.o; [34m$([39;49;00m[31mLDSHARED[39;49;00m[34m)[39;49;00m  Modules/symtablemodule.o   -o Modules/_symtablemodule[34m$([39;49;00m[31mSO[39;49;00m[34m)[39;49;00m$
[32mModules/xxsubtype.o[39;49;00m: [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/xxsubtype.c; [34m$([39;49;00m[31mCC[39;49;00m[34m)[39;49;00m [34m$([39;49;00m[31mPY_CFLAGS[39;49;00m[34m)[39;49;00m  -c [34m$([39;49;00m[31msrcdir[39;49;00m[34m)[39;49;00m/Modules/xxsubtype.c -o Modules/xxsubtype.o$
[32mModules/xxsubtype$(SO)[39;49;00m:  Modules/xxsubtype.o; [34m$([39;49;00m[31mLDSHARED[39;49;00m[34m)[39;49;00m  Modules/xxsubtype.o   -o Modules/xxsubtype[34m$([39;49;00m[31mSO[39;49;00m[34m)[39;49;00m$

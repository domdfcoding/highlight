[37m# New ports collection makefile for:    python25[39;49;00m
[37m# Date created:         3 July 2003[39;49;00m
[37m# Whom:                 Hye-Shik Chang <perky@FreeBSD.org>[39;49;00m
[37m#[39;49;00m
[37m# $FreeBSD: ports/lang/python25/Makefile,v 1.145 2007/10/03 23:22:04 edwin Exp $[39;49;00m

[31mPORTNAME[39;49;00m=^Ipython25
[31mPORTVERSION[39;49;00m=^I[34m2[39;49;00m.5.1
[31mCATEGORIES[39;49;00m=^Ilang python ipv6
[31mMASTER_SITES[39;49;00m=^I[33m${[39;49;00m[31mPYTHON_MASTER_SITES[39;49;00m[33m}[39;49;00m
[31mMASTER_SITE_SUBDIR[39;49;00m=^I[33m${[39;49;00m[31mPYTHON_MASTER_SITE_SUBDIR[39;49;00m[33m}[39;49;00m
[31mDISTFILES[39;49;00m=^I[33m${[39;49;00m[31mPYTHON_DISTFILE[39;49;00m[33m}[39;49;00m

[31mMAINTAINER[39;49;00m=^Ipython@FreeBSD.org
[31mCOMMENT[39;49;00m?=^IAn interpreted object-oriented programming language

[31mDIST_SUBDIR[39;49;00m=^Ipython
[31mWRKSRC[39;49;00m=^I^I[33m${[39;49;00m[31mPYTHON_WRKSRC[39;49;00m[33m}[39;49;00m/portbld.static
[31mPATCH_WRKSRC[39;49;00m=^I[33m${[39;49;00m[31mPYTHON_WRKSRC[39;49;00m[33m}[39;49;00m
[31mGNU_CONFIGURE[39;49;00m=^Iyes
[31mCONFIGURE_TARGET[39;49;00m=^I--build=[33m${[39;49;00m[31mMACHINE_ARCH[39;49;00m[33m}[39;49;00m-portbld-freebsd[33m${[39;49;00m[31mOSREL[39;49;00m[33m}[39;49;00m
[31mCONFIGURE_SCRIPT[39;49;00m=^I../configure [37m# must be relative[39;49;00m
[31mCONFIGURE_ENV[39;49;00m=^I[31mOPT[39;49;00m=[33m"[39;49;00m[33m${[39;49;00m[31mCFLAGS[39;49;00m[33m}[39;49;00m[33m"[39;49;00m [31mSVNVERSION[39;49;00m=[33m"echo freebsd"[39;49;00m
[31mMAKE_ENV[39;49;00m=^I[31mVPATH[39;49;00m=[33m"[39;49;00m[33m${[39;49;00m[31mPYTHON_WRKSRC[39;49;00m[33m}[39;49;00m[33m"[39;49;00m
[31mINSTALLS_SHLIB[39;49;00m=^Iyes
[31mINSTALL_TARGET[39;49;00m=^Ialtinstall
[31mMAN1[39;49;00m=^I^I[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m[33m}[39;49;00m.1

[31mUSE_PYTHON[39;49;00m=^Iyes
[31mPYTHON_VERSION[39;49;00m=^Ipython2.5
[31mPYTHON_NO_DEPENDS[39;49;00m=^Iyes

[31mSHARED_WRKSRC[39;49;00m=^I[33m${[39;49;00m[31mPYTHON_WRKSRC[39;49;00m[33m}[39;49;00m/portbld.shared
[31mPLIST[39;49;00m=^I^I[33m${[39;49;00m[31mWRKDIR[39;49;00m[33m}[39;49;00m/PLIST
[31mPLIST_TEMPLATE[39;49;00m?=[33m${[39;49;00m[31mPKGDIR[39;49;00m[33m}[39;49;00m/pkg-plist
[31mPLIST_SUB[39;49;00m=^I[31mPYVER[39;49;00m=[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m:[31mS[39;49;00m/python//[33m}[39;49;00m [33m\[39;49;00m
^I^I[31mPYVER_WITHPAT[39;49;00m=[33m${[39;49;00m[31mPORTVERSION[39;49;00m:[31mS[39;49;00m/.c/c/[33m}[39;49;00m
[31mDEMODIR[39;49;00m=^I[33m${[39;49;00m[31mPREFIX[39;49;00m[33m}[39;49;00m/share/examples/[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m[33m}[39;49;00m
[31mTOOLSDIR[39;49;00m=^I[33m${[39;49;00m[31mPREFIX[39;49;00m[33m}[39;49;00m/share/[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m[33m}[39;49;00m

[31mBIN_SCRIPTS[39;49;00m=^Iidle pydoc python python-shared smtpd.py python-config [33m\[39;49;00m
^I^Ipython-shared-config
[31mBINLINKS_SUB[39;49;00m=^I-e [33m's,smtpd,smtpd${PYTHON_VER},'[39;49;00m [33m\[39;49;00m
^I^I-e [33m's,(idle|pydoc|python-shared|python),\1${PYTHON_VER},'[39;49;00m

[31mOPTIONS[39;49;00m=^ITHREADS [33m"Enable thread support"[39;49;00m on [33m\[39;49;00m
^I^IHUGE_STACK_SIZE [33m"Use a larger thread stack"[39;49;00m off [33m\[39;49;00m
^I^IUCS4 [33m"Use UCS4 for unicode support"[39;49;00m on [33m\[39;49;00m
^I^IPYMALLOC [33m"Use python's internal malloc"[39;49;00m on [33m\[39;49;00m
^I^IIPV6 [33m"Enable IPv6 support"[39;49;00m on [33m\[39;49;00m
^I^IFPECTL [33m"Enable floating point exception handling"[39;49;00m off

[36m.include <bsd.port.pre.mk>[39;49;00m

[36m.if ${PYTHON_VERSION} == ${PYTHON_DEFAULT_VERSION}[39;49;00m
[31mMLINKS[39;49;00m=^I^I[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m[33m}[39;49;00m.1 python.1
[31mPLIST_SUB[39;49;00m+=^I[31mIF_DEFAULT[39;49;00m=[33m""[39;49;00m
[36m.else[39;49;00m
[31mPLIST_SUB[39;49;00m+=^I[31mIF_DEFAULT[39;49;00m=[33m"@comment "[39;49;00m
[36m.endif[39;49;00m

[37m# workaround for a bug in base curses.h.[39;49;00m
[31mCFLAGS[39;49;00m+=^I-D__wchar_t=wchar_t

[36m.if !defined(WITHOUT_THREADS)[39;49;00m
[31mCONFIGURE_ARGS[39;49;00m+=^I--with-threads
[31mCFLAGS[39;49;00m+=^I^I[33m${[39;49;00m[31mPTHREAD_CFLAGS[39;49;00m[33m}[39;49;00m
[36m.if defined(WITHOUT_HUGE_STACK_SIZE)[39;49;00m
[31mCFLAGS[39;49;00m+=^I^I-DTHREAD_STACK_SIZE=0x20000
[36m.else[39;49;00m
[31mCFLAGS[39;49;00m+=^I^I-DTHREAD_STACK_SIZE=0x100000
[36m.endif # defined(WITHOUT_HUGE_STACK_SIZE)[39;49;00m
[31mCONFIGURE_ENV[39;49;00m+=^I^I[31mLDFLAGS[39;49;00m=[33m"[39;49;00m[33m${[39;49;00m[31mPTHREAD_LIBS[39;49;00m[33m}[39;49;00m[33m [39;49;00m[33m${[39;49;00m[31mLDFLAGS[39;49;00m[33m}[39;49;00m[33m"[39;49;00m
[36m.else[39;49;00m
[31mCONFIGURE_ARGS[39;49;00m+=^I--without-threads
[36m.if defined(LDFLAGS)[39;49;00m
[31mCONFIGURE_ENV[39;49;00m+=^I^I[31mLDFLAGS[39;49;00m=[33m"[39;49;00m[33m${[39;49;00m[31mLDFLAGS[39;49;00m[33m}[39;49;00m[33m"[39;49;00m
[36m.endif # defined(LDFLAGS)[39;49;00m
[36m.endif # !defined(WITHOUT_THREADS)[39;49;00m

[36m.if !defined(WITHOUT_UCS4) && !defined(WITH_UCS2)[39;49;00m
[31mCONFIGURE_ARGS[39;49;00m+=^I--enable-unicode=ucs4
[36m.endif[39;49;00m

[36m.if defined(WITHOUT_PYMALLOC)[39;49;00m
[31mCONFIGURE_ARGS[39;49;00m+=        --without-pymalloc
[36m.endif[39;49;00m

[36m.if ${ARCH} == i386[39;49;00m
[31mPLIST_SUB[39;49;00m+=^I[31mX86_ONLY[39;49;00m=[33m""[39;49;00m
[36m.else[39;49;00m
[31mPLIST_SUB[39;49;00m+=^I[31mX86_ONLY[39;49;00m=[33m"@comment "[39;49;00m
[36m.endif[39;49;00m
[36m.if ${ARCH} == amd64 || ${ARCH} == ia64 || ${ARCH} == sparc64 || ${ARCH} == alpha[39;49;00m
[31mPLIST_SUB[39;49;00m+=     [31m32BIT_ONLY[39;49;00m=[33m"@comment "[39;49;00m
[36m.else[39;49;00m
[31mPLIST_SUB[39;49;00m+=     [31m32BIT_ONLY[39;49;00m=[33m""[39;49;00m
[36m.endif[39;49;00m
[36m.if ${ARCH} == sparc64[39;49;00m
[31mCFLAGS[39;49;00m+=        -DPYTHON_DEFAULT_RECURSION_LIMIT=[34m900[39;49;00m
[36m.endif[39;49;00m

[36m.if !exists(/usr/bin/ypcat) # the world with NO_NIS[39;49;00m
[31mPLIST_SUB[39;49;00m+=^I[31mNO_NIS[39;49;00m=[33m"@comment "[39;49;00m
[36m.else[39;49;00m
[31mPLIST_SUB[39;49;00m+=^I[31mNO_NIS[39;49;00m=[33m""[39;49;00m
[36m.endif[39;49;00m

[36m.if !defined(WITHOUT_IPV6)[39;49;00m
[31mCONFIGURE_ARGS[39;49;00m+= --enable-ipv6
[36m.else[39;49;00m
[31mCONFIGURE_ARGS[39;49;00m+= --disable-ipv6
[36m.endif[39;49;00m

[36m.if defined(WITH_FPECTL)[39;49;00m
[31mCONFIGURE_ARGS[39;49;00m+= --with-fpectl
[36m.endif[39;49;00m

[36m.if ${OSVERSION} >= 700000[39;49;00m
[31mPLATFORMS[39;49;00m=plat-freebsd4 plat-freebsd5 plat-freebsd6
[36m.elif ${OSVERSION} >= 600000[39;49;00m
[31mPLATFORMS[39;49;00m=plat-freebsd4 plat-freebsd5 plat-freebsd7
[36m.else[39;49;00m
[31mPLATFORMS[39;49;00m=plat-freebsd4 plat-freebsd6 plat-freebsd7
[36m.endif[39;49;00m

[32mpre-patch[39;49;00m:
^I[33m${[39;49;00m[31mMKDIR[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mWRKSRC[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mSHARED_WRKSRC[39;49;00m[33m}[39;49;00m/Modules
^I[33m${[39;49;00m[31mSED[39;49;00m[33m}[39;49;00m -e [33m'1s,^.*$$,#!${PREFIX}/bin/${PYTHON_VERSION},'[39;49;00m [33m\[39;49;00m
^I^I[33m${[39;49;00m[31mPATCH_WRKSRC[39;49;00m[33m}[39;49;00m/Tools/scripts/pydoc > [33m${[39;49;00m[31mWRKDIR[39;49;00m[33m}[39;49;00m/pydoc2.5
^I[33m${[39;49;00m[31mSED[39;49;00m[33m}[39;49;00m -e [33m'1s,^.*$$,#!${PREFIX}/bin/${PYTHON_VERSION},'[39;49;00m [33m\[39;49;00m
^I^I[33m${[39;49;00m[31mPATCH_WRKSRC[39;49;00m[33m}[39;49;00m/Tools/scripts/idle > [33m${[39;49;00m[31mWRKDIR[39;49;00m[33m}[39;49;00m/idle2.5
^I[33m${[39;49;00m[31mSED[39;49;00m[33m}[39;49;00m -e [33m'1s,^.*$$,#!${PREFIX}/bin/${PYTHON_VERSION},'[39;49;00m [33m\[39;49;00m
^I^I[33m${[39;49;00m[31mPATCH_WRKSRC[39;49;00m[33m}[39;49;00m/Lib/smtpd.py > [33m${[39;49;00m[31mWRKDIR[39;49;00m[33m}[39;49;00m/smtpd2.5.py
^I[33m${[39;49;00m[31mREINPLACE_CMD[39;49;00m[33m}[39;49;00m -e [33m\[39;49;00m
^I^I[33m's,/usr/doc/python-docs-,${PREFIX}/share/doc/python,g'[39;49;00m [33m\[39;49;00m
^I^I[33m${[39;49;00m[31mPATCH_WRKSRC[39;49;00m[33m}[39;49;00m/Lib/pydoc.py
^I[33m${[39;49;00m[31mREINPLACE_CMD[39;49;00m[33m}[39;49;00m -e [33m\[39;49;00m
^I^I[33m's|^\( *prefixes = .*\)\]$$|\1, "${X11BASE}"]|g'[39;49;00m [33m\[39;49;00m
^I^I[33m${[39;49;00m[31mPATCH_WRKSRC[39;49;00m[33m}[39;49;00m/Lib/site.py
^I[33m${[39;49;00m[31mREINPLACE_CMD[39;49;00m[33m}[39;49;00m -e [33m\[39;49;00m
^I^I[33m's|^^I\(..ASDLGEN.*\)$$|^I${TRUE}|g'[39;49;00m [33m\[39;49;00m
^I^I[33m${[39;49;00m[31mPATCH_WRKSRC[39;49;00m[33m}[39;49;00m/Makefile.pre.in

^I[33m${[39;49;00m[31mREINPLACE_CMD[39;49;00m[33m}[39;49;00m -e [33m\[39;49;00m
^I^I[33m's|*\(..INSTALL_SCRIPT.*\)python-config$$|#port \1|'[39;49;00m [33m\[39;49;00m
^I^I[33m${[39;49;00m[31mPATCH_WRKSRC[39;49;00m[33m}[39;49;00m/Makefile.pre.in

^I[33m${[39;49;00m[31mSED[39;49;00m[33m}[39;49;00m -e [33m's|^#!.*|#!${PREFIX}/bin/${PYTHON_VERSION}|'[39;49;00m [33m\[39;49;00m
^I^I[33m${[39;49;00m[31mPATCH_WRKSRC[39;49;00m[33m}[39;49;00m/Misc/python-config.in > [33m${[39;49;00m[31mWRKDIR[39;49;00m[33m}[39;49;00m/[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m[33m}[39;49;00m-config
^I[33m${[39;49;00m[31mSED[39;49;00m[33m}[39;49;00m -e [33m's|^#!.*|#!${PREFIX}/bin/${PYTHON_VERSION:S/thon/thon-shared/}|'[39;49;00m [33m\[39;49;00m
^I^I[33m${[39;49;00m[31mPATCH_WRKSRC[39;49;00m[33m}[39;49;00m/Misc/python-config.in > [33m${[39;49;00m[31mWRKDIR[39;49;00m[33m}[39;49;00m/[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m:[31mS[39;49;00m/thon/thon-shared/[33m}[39;49;00m-config

[36m.if defined(WITH_FPECTL) && ${ARCH} == i386[39;49;00m
^I[33m${[39;49;00m[31mMKDIR[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mWRKSRC[39;49;00m[33m}[39;49;00m/Modules
^I[33m${[39;49;00m[31mECHO[39;49;00m[33m}[39;49;00m [33m"fpectl fpectlmodule.c"[39;49;00m >> [33m${[39;49;00m[31mWRKSRC[39;49;00m[33m}[39;49;00m/Modules/Setup.dist
[36m.endif[39;49;00m

[32mpost-configure[39;49;00m:
^I[33m${[39;49;00m[31mTAR[39;49;00m[33m}[39;49;00m -C [33m${[39;49;00m[31mWRKSRC[39;49;00m[33m}[39;49;00m -cf - . | [33m${[39;49;00m[31mTAR[39;49;00m[33m}[39;49;00m -C [33m${[39;49;00m[31mSHARED_WRKSRC[39;49;00m[33m}[39;49;00m -xf -
^I[33m${[39;49;00m[31mLN[39;49;00m[33m}[39;49;00m -sf [33m${[39;49;00m[31mPYTHON_WRKSRC[39;49;00m[33m}[39;49;00m/Lib [33m${[39;49;00m[31mWRKSRC[39;49;00m[33m}[39;49;00m/Lib
^I[33m${[39;49;00m[31mSED[39;49;00m[33m}[39;49;00m -e [33m's,^\(LDLIBRARY=\).*$$,\1libpython$$(VERSION).so,'[39;49;00m [33m\[39;49;00m
^I^I-e [33m's,^\(BLDLIBRARY=\).*$$,\1-L. -lpython$$(VERSION),'[39;49;00m [33m\[39;49;00m
^I^I-e [33m's,^\(CFLAGSFORSHARED=\).*$$,\1$$(CCSHARED),'[39;49;00m [33m\[39;49;00m
^I^I-e [33m's,^\(Makefile Modules/config.c:.*\)Makefile.pre,\1,'[39;49;00m [33m\[39;49;00m
^I^I-e [33m's,^\(.(BUILDPYTHON)\: .*\).(LIBRARY),\1,'[39;49;00m [33m\[39;49;00m
^I^I-e [33m's,^\(.(BUILDPYTHON):.*\).(LIBRARY),\1,'[39;49;00m [33m\[39;49;00m
^I^I[33m${[39;49;00m[31mWRKSRC[39;49;00m[33m}[39;49;00m/Makefile > [33m${[39;49;00m[31mSHARED_WRKSRC[39;49;00m[33m}[39;49;00m/Makefile

[32mpre-build[39;49;00m:
^I[36mcd[39;49;00m [33m${[39;49;00m[31mSHARED_WRKSRC[39;49;00m[33m}[39;49;00m; [33m\[39;49;00m
^I[33m${[39;49;00m[31mSETENV[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mMAKE_ENV[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mMAKE[39;49;00m[33m}[39;49;00m lib[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m[33m}[39;49;00m.so python; [33m\[39;49;00m
^I[33m${[39;49;00m[31mLN[39;49;00m[33m}[39;49;00m -f lib[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m[33m}[39;49;00m.so lib[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m[33m}[39;49;00m.so.1; [33m\[39;49;00m
^I[33m${[39;49;00m[31mLN[39;49;00m[33m}[39;49;00m -f python [33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m:[31mS[39;49;00m/thon/thon-shared/[33m}[39;49;00m

[32mpre-su-install[39;49;00m:
[36m.for platform in ${PLATFORMS}[39;49;00m
^I[33m${[39;49;00m[31mMKDIR[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mPYTHONPREFIX_LIBDIR[39;49;00m[33m}[39;49;00m/[33m${[39;49;00m[31mplatform[39;49;00m[33m}[39;49;00m
[36m.for file in IN.py regen[39;49;00m
^I[33m${[39;49;00m[31mINSTALL_DATA[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mWRKSRC[39;49;00m[33m}[39;49;00m/Lib/[33m${[39;49;00m[31mplatform[39;49;00m[33m}[39;49;00m/[33m${[39;49;00m[31mfile[39;49;00m[33m}[39;49;00m [33m\[39;49;00m
^I^I[33m${[39;49;00m[31mPYTHONPREFIX_LIBDIR[39;49;00m[33m}[39;49;00m/[33m${[39;49;00m[31mplatform[39;49;00m[33m}[39;49;00m/
[36m.endfor[39;49;00m
[36m.endfor[39;49;00m

[32mpre-install[39;49;00m:
^I[33m${[39;49;00m[31mCAT[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mPLIST_TEMPLATE[39;49;00m[33m}[39;49;00m | [33m${[39;49;00m[31mAWK[39;49;00m[33m}[39;49;00m [33m'{ print $$0; } \[39;49;00m
[33m^I/LIBDIR.*\.py$$/ && !/\/bad/ { print $$0 "o"; print $$0 "c"; }'[39;49;00m^I> [33m${[39;49;00m[31mPLIST[39;49;00m[33m}[39;49;00m

[37m^I@# if openssl 0.9.8 is detected, _sha{256,512} module won't be installed[39;49;00m
^I([ -f [33m${[39;49;00m[31mWRKSRC[39;49;00m[33m}[39;49;00m/.without_own_sha ] && [33m\[39;49;00m
^I^I[33m${[39;49;00m[31mGREP[39;49;00m[33m}[39;49;00m -v [33m'lib-dynload/_sha'[39;49;00m [33m${[39;49;00m[31mPLIST[39;49;00m[33m}[39;49;00m > [33m${[39;49;00m[31mPLIST[39;49;00m[33m}[39;49;00m.tmp && [33m\[39;49;00m
^I^I[33m${[39;49;00m[31mCAT[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mPLIST[39;49;00m[33m}[39;49;00m.tmp > [33m${[39;49;00m[31mPLIST[39;49;00m[33m}[39;49;00m) || [33m${[39;49;00m[31mTRUE[39;49;00m[33m}[39;49;00m

[32mpost-install[39;49;00m:
[37m^I@# install config providers[39;49;00m
^I[33m${[39;49;00m[31mINSTALL_SCRIPT[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mWRKDIR[39;49;00m[33m}[39;49;00m/[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m[33m}[39;49;00m-config [33m${[39;49;00m[31mPREFIX[39;49;00m[33m}[39;49;00m/bin
^I[33m${[39;49;00m[31mINSTALL_SCRIPT[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mWRKDIR[39;49;00m[33m}[39;49;00m/[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m:[31mS[39;49;00m/thon/thon-shared/[33m}[39;49;00m-config [33m${[39;49;00m[31mPREFIX[39;49;00m[33m}[39;49;00m/bin

[37m^I@# shared version of executable and library[39;49;00m
^I[33m${[39;49;00m[31mINSTALL_PROGRAM[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mSHARED_WRKSRC[39;49;00m[33m}[39;49;00m/lib[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m[33m}[39;49;00m.so.1 [33m\[39;49;00m
^I^I[33m${[39;49;00m[31mPREFIX[39;49;00m[33m}[39;49;00m/lib
^I[36mcd[39;49;00m [33m${[39;49;00m[31mPREFIX[39;49;00m[33m}[39;49;00m/lib; [33m${[39;49;00m[31mLN[39;49;00m[33m}[39;49;00m -sf lib[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m[33m}[39;49;00m.so.1 [33m\[39;49;00m
^I^Ilib[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m[33m}[39;49;00m.so
^I[33m${[39;49;00m[31mLN[39;49;00m[33m}[39;49;00m -sf [33m${[39;49;00m[31mPREFIX[39;49;00m[33m}[39;49;00m/lib/lib[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m[33m}[39;49;00m.so [33m${[39;49;00m[31mPYTHONPREFIX_LIBDIR[39;49;00m[33m}[39;49;00m/config
^I[33m${[39;49;00m[31mINSTALL_PROGRAM[39;49;00m[33m}[39;49;00m [33m\[39;49;00m
^I^I[33m${[39;49;00m[31mSHARED_WRKSRC[39;49;00m[33m}[39;49;00m/[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m:[31mS[39;49;00m/thon/thon-shared/[33m}[39;49;00m [33m\[39;49;00m
^I^I[33m${[39;49;00m[31mPREFIX[39;49;00m[33m}[39;49;00m/bin

[37m^I@# additional files installing by ports[39;49;00m
^I[33m${[39;49;00m[31mINSTALL_SCRIPT[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mWRKDIR[39;49;00m[33m}[39;49;00m/pydoc2.5 [33m${[39;49;00m[31mWRKDIR[39;49;00m[33m}[39;49;00m/idle2.5 [33m\[39;49;00m
^I^I[33m${[39;49;00m[31mWRKDIR[39;49;00m[33m}[39;49;00m/smtpd2.5.py [33m${[39;49;00m[31mPREFIX[39;49;00m[33m}[39;49;00m/bin
^I@[33m${[39;49;00m[31mMKDIR[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mMANPREFIX[39;49;00m[33m}[39;49;00m/man/man1
^I[33m${[39;49;00m[31mINSTALL_MAN[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mPYTHON_WRKSRC[39;49;00m[33m}[39;49;00m/Misc/python.man [33m\[39;49;00m
^I^I[33m${[39;49;00m[31mMANPREFIX[39;49;00m[33m}[39;49;00m/man/man1/[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m[33m}[39;49;00m.1

[36m.if ${PYTHON_VERSION} == ${PYTHON_DEFAULT_VERSION}[39;49;00m
^I[34mfor[39;49;00m f [34min[39;49;00m [33m${[39;49;00m[31mBIN_SCRIPTS[39;49;00m[33m}[39;49;00m; [34mdo[39;49;00m [33m\[39;49;00m
^I^I[31mTARGET[39;49;00m=[33m`[39;49;00m[33m${[39;49;00m[31mECHO_CMD[39;49;00m[33m}[39;49;00m [31m$$[39;49;00mf | [33m${[39;49;00m[31mSED[39;49;00m[33m}[39;49;00m -E [33m${[39;49;00m[31mBINLINKS_SUB[39;49;00m[33m}[39;49;00m[33m`[39;49;00m; [33m\[39;49;00m
^I^I[36mcd[39;49;00m [33m${[39;49;00m[31mPREFIX[39;49;00m[33m}[39;49;00m/bin && [33m${[39;49;00m[31mLN[39;49;00m[33m}[39;49;00m -f [31m$$[39;49;00mTARGET [31m$$[39;49;00mf; [33m\[39;49;00m
^I[34mdone[39;49;00m
[36m.endif[39;49;00m

[36m.if !defined(NOPORTDOCS)[39;49;00m
^I@[33m${[39;49;00m[31mMKDIR[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mTOOLSDIR[39;49;00m[33m}[39;49;00m
^I@cd [33m${[39;49;00m[31mPYTHON_WRKSRC[39;49;00m[33m}[39;49;00m; [33m${[39;49;00m[31mTAR[39;49;00m[33m}[39;49;00m -cf - Tools | [33m\[39;49;00m
^I^I([36mcd[39;49;00m [33m${[39;49;00m[31mTOOLSDIR[39;49;00m[33m}[39;49;00m; [33m${[39;49;00m[31mTAR[39;49;00m[33m}[39;49;00m -xf -)
^I@[33m${[39;49;00m[31mMKDIR[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mDEMODIR[39;49;00m[33m}[39;49;00m
^I@cd [33m${[39;49;00m[31mPYTHON_WRKSRC[39;49;00m[33m}[39;49;00m/Demo; [33m${[39;49;00m[31mTAR[39;49;00m[33m}[39;49;00m -cf - * | [33m\[39;49;00m
^I^I([36mcd[39;49;00m [33m${[39;49;00m[31mDEMODIR[39;49;00m[33m}[39;49;00m; [33m${[39;49;00m[31mTAR[39;49;00m[33m}[39;49;00m -xf -)
[36m.endif[39;49;00m

^I@[33m${[39;49;00m[31mCAT[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mPKGMESSAGE[39;49;00m[33m}[39;49;00m

[36m.include <bsd.port.post.mk>[39;49;00m

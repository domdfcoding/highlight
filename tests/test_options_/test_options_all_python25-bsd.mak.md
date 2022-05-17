     1^I[37m# New ports collection makefile for:    python25[39;49;00m$
     2^I[37m# Date created:         3 July 2003[39;49;00m$
     3^I[37m# Whom:                 Hye-Shik Chang <perky@FreeBSD.org>[39;49;00m$
     4^I[37m#[39;49;00m$
     5^I[37m# $FreeBSD: ports/lang/python25/Makefile,v 1.145 2007/10/03 23:22:04 edwin Exp $[39;49;00m$
     6^I$
     7^I[31mPORTNAME[39;49;00m=^Ipython25$
     8^I[31mPORTVERSION[39;49;00m=^I[34m2[39;49;00m.5.1$
     9^I[31mCATEGORIES[39;49;00m=^Ilang python ipv6$
    10^I[31mMASTER_SITES[39;49;00m=^I[33m${[39;49;00m[31mPYTHON_MASTER_SITES[39;49;00m[33m}[39;49;00m$
    11^I[31mMASTER_SITE_SUBDIR[39;49;00m=^I[33m${[39;49;00m[31mPYTHON_MASTER_SITE_SUBDIR[39;49;00m[33m}[39;49;00m$
    12^I[31mDISTFILES[39;49;00m=^I[33m${[39;49;00m[31mPYTHON_DISTFILE[39;49;00m[33m}[39;49;00m$
    13^I$
    14^I[31mMAINTAINER[39;49;00m=^Ipython@FreeBSD.org$
    15^I[31mCOMMENT[39;49;00m?=^IAn interpreted object-oriented programming language$
    16^I$
    17^I[31mDIST_SUBDIR[39;49;00m=^Ipython$
    18^I[31mWRKSRC[39;49;00m=^I^I[33m${[39;49;00m[31mPYTHON_WRKSRC[39;49;00m[33m}[39;49;00m/portbld.static$
    19^I[31mPATCH_WRKSRC[39;49;00m=^I[33m${[39;49;00m[31mPYTHON_WRKSRC[39;49;00m[33m}[39;49;00m$
    20^I[31mGNU_CONFIGURE[39;49;00m=^Iyes$
    21^I[31mCONFIGURE_TARGET[39;49;00m=^I--build=[33m${[39;49;00m[31mMACHINE_ARCH[39;49;00m[33m}[39;49;00m-portbld-freebsd[33m${[39;49;00m[31mOSREL[39;49;00m[33m}[39;49;00m$
    22^I[31mCONFIGURE_SCRIPT[39;49;00m=^I../configure [37m# must be relative[39;49;00m$
    23^I[31mCONFIGURE_ENV[39;49;00m=^I[31mOPT[39;49;00m=[33m"[39;49;00m[33m${[39;49;00m[31mCFLAGS[39;49;00m[33m}[39;49;00m[33m"[39;49;00m [31mSVNVERSION[39;49;00m=[33m"echo freebsd"[39;49;00m$
    24^I[31mMAKE_ENV[39;49;00m=^I[31mVPATH[39;49;00m=[33m"[39;49;00m[33m${[39;49;00m[31mPYTHON_WRKSRC[39;49;00m[33m}[39;49;00m[33m"[39;49;00m$
    25^I[31mINSTALLS_SHLIB[39;49;00m=^Iyes$
    26^I[31mINSTALL_TARGET[39;49;00m=^Ialtinstall$
    27^I[31mMAN1[39;49;00m=^I^I[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m[33m}[39;49;00m.1$
    28^I$
    29^I[31mUSE_PYTHON[39;49;00m=^Iyes$
    30^I[31mPYTHON_VERSION[39;49;00m=^Ipython2.5$
    31^I[31mPYTHON_NO_DEPENDS[39;49;00m=^Iyes$
    32^I$
    33^I[31mSHARED_WRKSRC[39;49;00m=^I[33m${[39;49;00m[31mPYTHON_WRKSRC[39;49;00m[33m}[39;49;00m/portbld.shared$
    34^I[31mPLIST[39;49;00m=^I^I[33m${[39;49;00m[31mWRKDIR[39;49;00m[33m}[39;49;00m/PLIST$
    35^I[31mPLIST_TEMPLATE[39;49;00m?=[33m${[39;49;00m[31mPKGDIR[39;49;00m[33m}[39;49;00m/pkg-plist$
    36^I[31mPLIST_SUB[39;49;00m=^I[31mPYVER[39;49;00m=[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m:[31mS[39;49;00m/python//[33m}[39;49;00m [33m\[39;49;00m$
    37^I^I^I[31mPYVER_WITHPAT[39;49;00m=[33m${[39;49;00m[31mPORTVERSION[39;49;00m:[31mS[39;49;00m/.c/c/[33m}[39;49;00m$
    38^I[31mDEMODIR[39;49;00m=^I[33m${[39;49;00m[31mPREFIX[39;49;00m[33m}[39;49;00m/share/examples/[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m[33m}[39;49;00m$
    39^I[31mTOOLSDIR[39;49;00m=^I[33m${[39;49;00m[31mPREFIX[39;49;00m[33m}[39;49;00m/share/[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m[33m}[39;49;00m$
    40^I$
    41^I[31mBIN_SCRIPTS[39;49;00m=^Iidle pydoc python python-shared smtpd.py python-config [33m\[39;49;00m$
    42^I^I^Ipython-shared-config$
    43^I[31mBINLINKS_SUB[39;49;00m=^I-e [33m's,smtpd,smtpd${PYTHON_VER},'[39;49;00m [33m\[39;49;00m$
    44^I^I^I-e [33m's,(idle|pydoc|python-shared|python),\1${PYTHON_VER},'[39;49;00m$
    45^I$
    46^I[31mOPTIONS[39;49;00m=^ITHREADS [33m"Enable thread support"[39;49;00m on [33m\[39;49;00m$
    47^I^I^IHUGE_STACK_SIZE [33m"Use a larger thread stack"[39;49;00m off [33m\[39;49;00m$
    48^I^I^IUCS4 [33m"Use UCS4 for unicode support"[39;49;00m on [33m\[39;49;00m$
    49^I^I^IPYMALLOC [33m"Use python's internal malloc"[39;49;00m on [33m\[39;49;00m$
    50^I^I^IIPV6 [33m"Enable IPv6 support"[39;49;00m on [33m\[39;49;00m$
    51^I^I^IFPECTL [33m"Enable floating point exception handling"[39;49;00m off$
    52^I$
    53^I[36m.include <bsd.port.pre.mk>[39;49;00m$
    54^I$
    55^I[36m.if ${PYTHON_VERSION} == ${PYTHON_DEFAULT_VERSION}[39;49;00m$
    56^I[31mMLINKS[39;49;00m=^I^I[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m[33m}[39;49;00m.1 python.1$
    57^I[31mPLIST_SUB[39;49;00m+=^I[31mIF_DEFAULT[39;49;00m=[33m""[39;49;00m$
    58^I[36m.else[39;49;00m$
    59^I[31mPLIST_SUB[39;49;00m+=^I[31mIF_DEFAULT[39;49;00m=[33m"@comment "[39;49;00m$
    60^I[36m.endif[39;49;00m$
    61^I$
    62^I[37m# workaround for a bug in base curses.h.[39;49;00m$
    63^I[31mCFLAGS[39;49;00m+=^I-D__wchar_t=wchar_t$
    64^I$
    65^I[36m.if !defined(WITHOUT_THREADS)[39;49;00m$
    66^I[31mCONFIGURE_ARGS[39;49;00m+=^I--with-threads$
    67^I[31mCFLAGS[39;49;00m+=^I^I[33m${[39;49;00m[31mPTHREAD_CFLAGS[39;49;00m[33m}[39;49;00m$
    68^I[36m.if defined(WITHOUT_HUGE_STACK_SIZE)[39;49;00m$
    69^I[31mCFLAGS[39;49;00m+=^I^I-DTHREAD_STACK_SIZE=0x20000$
    70^I[36m.else[39;49;00m$
    71^I[31mCFLAGS[39;49;00m+=^I^I-DTHREAD_STACK_SIZE=0x100000$
    72^I[36m.endif # defined(WITHOUT_HUGE_STACK_SIZE)[39;49;00m$
    73^I[31mCONFIGURE_ENV[39;49;00m+=^I^I[31mLDFLAGS[39;49;00m=[33m"[39;49;00m[33m${[39;49;00m[31mPTHREAD_LIBS[39;49;00m[33m}[39;49;00m[33m [39;49;00m[33m${[39;49;00m[31mLDFLAGS[39;49;00m[33m}[39;49;00m[33m"[39;49;00m$
    74^I[36m.else[39;49;00m$
    75^I[31mCONFIGURE_ARGS[39;49;00m+=^I--without-threads$
    76^I[36m.if defined(LDFLAGS)[39;49;00m$
    77^I[31mCONFIGURE_ENV[39;49;00m+=^I^I[31mLDFLAGS[39;49;00m=[33m"[39;49;00m[33m${[39;49;00m[31mLDFLAGS[39;49;00m[33m}[39;49;00m[33m"[39;49;00m$
    78^I[36m.endif # defined(LDFLAGS)[39;49;00m$
    79^I[36m.endif # !defined(WITHOUT_THREADS)[39;49;00m$
    80^I$
    81^I[36m.if !defined(WITHOUT_UCS4) && !defined(WITH_UCS2)[39;49;00m$
    82^I[31mCONFIGURE_ARGS[39;49;00m+=^I--enable-unicode=ucs4$
    83^I[36m.endif[39;49;00m$
    84^I$
    85^I[36m.if defined(WITHOUT_PYMALLOC)[39;49;00m$
    86^I[31mCONFIGURE_ARGS[39;49;00m+=        --without-pymalloc$
    87^I[36m.endif[39;49;00m$
    88^I$
    89^I[36m.if ${ARCH} == i386[39;49;00m$
    90^I[31mPLIST_SUB[39;49;00m+=^I[31mX86_ONLY[39;49;00m=[33m""[39;49;00m$
    91^I[36m.else[39;49;00m$
    92^I[31mPLIST_SUB[39;49;00m+=^I[31mX86_ONLY[39;49;00m=[33m"@comment "[39;49;00m$
    93^I[36m.endif[39;49;00m$
    94^I[36m.if ${ARCH} == amd64 || ${ARCH} == ia64 || ${ARCH} == sparc64 || ${ARCH} == alpha[39;49;00m$
    95^I[31mPLIST_SUB[39;49;00m+=     [31m32BIT_ONLY[39;49;00m=[33m"@comment "[39;49;00m$
    96^I[36m.else[39;49;00m$
    97^I[31mPLIST_SUB[39;49;00m+=     [31m32BIT_ONLY[39;49;00m=[33m""[39;49;00m$
    98^I[36m.endif[39;49;00m$
    99^I[36m.if ${ARCH} == sparc64[39;49;00m$
   100^I[31mCFLAGS[39;49;00m+=        -DPYTHON_DEFAULT_RECURSION_LIMIT=[34m900[39;49;00m$
   101^I[36m.endif[39;49;00m$
   102^I$
   103^I[36m.if !exists(/usr/bin/ypcat) # the world with NO_NIS[39;49;00m$
   104^I[31mPLIST_SUB[39;49;00m+=^I[31mNO_NIS[39;49;00m=[33m"@comment "[39;49;00m$
   105^I[36m.else[39;49;00m$
   106^I[31mPLIST_SUB[39;49;00m+=^I[31mNO_NIS[39;49;00m=[33m""[39;49;00m$
   107^I[36m.endif[39;49;00m$
   108^I$
   109^I[36m.if !defined(WITHOUT_IPV6)[39;49;00m$
   110^I[31mCONFIGURE_ARGS[39;49;00m+= --enable-ipv6$
   111^I[36m.else[39;49;00m$
   112^I[31mCONFIGURE_ARGS[39;49;00m+= --disable-ipv6$
   113^I[36m.endif[39;49;00m$
   114^I$
   115^I[36m.if defined(WITH_FPECTL)[39;49;00m$
   116^I[31mCONFIGURE_ARGS[39;49;00m+= --with-fpectl$
   117^I[36m.endif[39;49;00m$
   118^I$
   119^I[36m.if ${OSVERSION} >= 700000[39;49;00m$
   120^I[31mPLATFORMS[39;49;00m=plat-freebsd4 plat-freebsd5 plat-freebsd6$
   121^I[36m.elif ${OSVERSION} >= 600000[39;49;00m$
   122^I[31mPLATFORMS[39;49;00m=plat-freebsd4 plat-freebsd5 plat-freebsd7$
   123^I[36m.else[39;49;00m$
   124^I[31mPLATFORMS[39;49;00m=plat-freebsd4 plat-freebsd6 plat-freebsd7$
   125^I[36m.endif[39;49;00m$
   126^I$
   127^I[32mpre-patch[39;49;00m:$
   128^I^I[33m${[39;49;00m[31mMKDIR[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mWRKSRC[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mSHARED_WRKSRC[39;49;00m[33m}[39;49;00m/Modules$
   129^I^I[33m${[39;49;00m[31mSED[39;49;00m[33m}[39;49;00m -e [33m'1s,^.*$$,#!${PREFIX}/bin/${PYTHON_VERSION},'[39;49;00m [33m\[39;49;00m$
   130^I^I^I[33m${[39;49;00m[31mPATCH_WRKSRC[39;49;00m[33m}[39;49;00m/Tools/scripts/pydoc > [33m${[39;49;00m[31mWRKDIR[39;49;00m[33m}[39;49;00m/pydoc2.5$
   131^I^I[33m${[39;49;00m[31mSED[39;49;00m[33m}[39;49;00m -e [33m'1s,^.*$$,#!${PREFIX}/bin/${PYTHON_VERSION},'[39;49;00m [33m\[39;49;00m$
   132^I^I^I[33m${[39;49;00m[31mPATCH_WRKSRC[39;49;00m[33m}[39;49;00m/Tools/scripts/idle > [33m${[39;49;00m[31mWRKDIR[39;49;00m[33m}[39;49;00m/idle2.5$
   133^I^I[33m${[39;49;00m[31mSED[39;49;00m[33m}[39;49;00m -e [33m'1s,^.*$$,#!${PREFIX}/bin/${PYTHON_VERSION},'[39;49;00m [33m\[39;49;00m$
   134^I^I^I[33m${[39;49;00m[31mPATCH_WRKSRC[39;49;00m[33m}[39;49;00m/Lib/smtpd.py > [33m${[39;49;00m[31mWRKDIR[39;49;00m[33m}[39;49;00m/smtpd2.5.py$
   135^I^I[33m${[39;49;00m[31mREINPLACE_CMD[39;49;00m[33m}[39;49;00m -e [33m\[39;49;00m$
   136^I^I^I[33m's,/usr/doc/python-docs-,${PREFIX}/share/doc/python,g'[39;49;00m [33m\[39;49;00m$
   137^I^I^I[33m${[39;49;00m[31mPATCH_WRKSRC[39;49;00m[33m}[39;49;00m/Lib/pydoc.py$
   138^I^I[33m${[39;49;00m[31mREINPLACE_CMD[39;49;00m[33m}[39;49;00m -e [33m\[39;49;00m$
   139^I^I^I[33m's|^\( *prefixes = .*\)\]$$|\1, "${X11BASE}"]|g'[39;49;00m [33m\[39;49;00m$
   140^I^I^I[33m${[39;49;00m[31mPATCH_WRKSRC[39;49;00m[33m}[39;49;00m/Lib/site.py$
   141^I^I[33m${[39;49;00m[31mREINPLACE_CMD[39;49;00m[33m}[39;49;00m -e [33m\[39;49;00m$
   142^I^I^I[33m's|^^I\(..ASDLGEN.*\)$$|^I${TRUE}|g'[39;49;00m [33m\[39;49;00m$
   143^I^I^I[33m${[39;49;00m[31mPATCH_WRKSRC[39;49;00m[33m}[39;49;00m/Makefile.pre.in$
   144^I$
   145^I^I[33m${[39;49;00m[31mREINPLACE_CMD[39;49;00m[33m}[39;49;00m -e [33m\[39;49;00m$
   146^I^I^I[33m's|*\(..INSTALL_SCRIPT.*\)python-config$$|#port \1|'[39;49;00m [33m\[39;49;00m$
   147^I^I^I[33m${[39;49;00m[31mPATCH_WRKSRC[39;49;00m[33m}[39;49;00m/Makefile.pre.in$
   148^I$
   149^I^I[33m${[39;49;00m[31mSED[39;49;00m[33m}[39;49;00m -e [33m's|^#!.*|#!${PREFIX}/bin/${PYTHON_VERSION}|'[39;49;00m [33m\[39;49;00m$
   150^I^I^I[33m${[39;49;00m[31mPATCH_WRKSRC[39;49;00m[33m}[39;49;00m/Misc/python-config.in > [33m${[39;49;00m[31mWRKDIR[39;49;00m[33m}[39;49;00m/[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m[33m}[39;49;00m-config$
   151^I^I[33m${[39;49;00m[31mSED[39;49;00m[33m}[39;49;00m -e [33m's|^#!.*|#!${PREFIX}/bin/${PYTHON_VERSION:S/thon/thon-shared/}|'[39;49;00m [33m\[39;49;00m$
   152^I^I^I[33m${[39;49;00m[31mPATCH_WRKSRC[39;49;00m[33m}[39;49;00m/Misc/python-config.in > [33m${[39;49;00m[31mWRKDIR[39;49;00m[33m}[39;49;00m/[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m:[31mS[39;49;00m/thon/thon-shared/[33m}[39;49;00m-config$
   153^I$
   154^I[36m.if defined(WITH_FPECTL) && ${ARCH} == i386[39;49;00m$
   155^I^I[33m${[39;49;00m[31mMKDIR[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mWRKSRC[39;49;00m[33m}[39;49;00m/Modules$
   156^I^I[33m${[39;49;00m[31mECHO[39;49;00m[33m}[39;49;00m [33m"fpectl fpectlmodule.c"[39;49;00m >> [33m${[39;49;00m[31mWRKSRC[39;49;00m[33m}[39;49;00m/Modules/Setup.dist$
   157^I[36m.endif[39;49;00m$
   158^I$
   159^I[32mpost-configure[39;49;00m:$
   160^I^I[33m${[39;49;00m[31mTAR[39;49;00m[33m}[39;49;00m -C [33m${[39;49;00m[31mWRKSRC[39;49;00m[33m}[39;49;00m -cf - . | [33m${[39;49;00m[31mTAR[39;49;00m[33m}[39;49;00m -C [33m${[39;49;00m[31mSHARED_WRKSRC[39;49;00m[33m}[39;49;00m -xf -$
   161^I^I[33m${[39;49;00m[31mLN[39;49;00m[33m}[39;49;00m -sf [33m${[39;49;00m[31mPYTHON_WRKSRC[39;49;00m[33m}[39;49;00m/Lib [33m${[39;49;00m[31mWRKSRC[39;49;00m[33m}[39;49;00m/Lib$
   162^I^I[33m${[39;49;00m[31mSED[39;49;00m[33m}[39;49;00m -e [33m's,^\(LDLIBRARY=\).*$$,\1libpython$$(VERSION).so,'[39;49;00m [33m\[39;49;00m$
   163^I^I^I-e [33m's,^\(BLDLIBRARY=\).*$$,\1-L. -lpython$$(VERSION),'[39;49;00m [33m\[39;49;00m$
   164^I^I^I-e [33m's,^\(CFLAGSFORSHARED=\).*$$,\1$$(CCSHARED),'[39;49;00m [33m\[39;49;00m$
   165^I^I^I-e [33m's,^\(Makefile Modules/config.c:.*\)Makefile.pre,\1,'[39;49;00m [33m\[39;49;00m$
   166^I^I^I-e [33m's,^\(.(BUILDPYTHON)\: .*\).(LIBRARY),\1,'[39;49;00m [33m\[39;49;00m$
   167^I^I^I-e [33m's,^\(.(BUILDPYTHON):.*\).(LIBRARY),\1,'[39;49;00m [33m\[39;49;00m$
   168^I^I^I[33m${[39;49;00m[31mWRKSRC[39;49;00m[33m}[39;49;00m/Makefile > [33m${[39;49;00m[31mSHARED_WRKSRC[39;49;00m[33m}[39;49;00m/Makefile$
   169^I$
   170^I[32mpre-build[39;49;00m:$
   171^I^I[36mcd[39;49;00m [33m${[39;49;00m[31mSHARED_WRKSRC[39;49;00m[33m}[39;49;00m; [33m\[39;49;00m$
   172^I^I[33m${[39;49;00m[31mSETENV[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mMAKE_ENV[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mMAKE[39;49;00m[33m}[39;49;00m lib[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m[33m}[39;49;00m.so python; [33m\[39;49;00m$
   173^I^I[33m${[39;49;00m[31mLN[39;49;00m[33m}[39;49;00m -f lib[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m[33m}[39;49;00m.so lib[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m[33m}[39;49;00m.so.1; [33m\[39;49;00m$
   174^I^I[33m${[39;49;00m[31mLN[39;49;00m[33m}[39;49;00m -f python [33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m:[31mS[39;49;00m/thon/thon-shared/[33m}[39;49;00m$
   175^I$
   176^I[32mpre-su-install[39;49;00m:$
   177^I[36m.for platform in ${PLATFORMS}[39;49;00m$
   178^I^I[33m${[39;49;00m[31mMKDIR[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mPYTHONPREFIX_LIBDIR[39;49;00m[33m}[39;49;00m/[33m${[39;49;00m[31mplatform[39;49;00m[33m}[39;49;00m$
   179^I[36m.for file in IN.py regen[39;49;00m$
   180^I^I[33m${[39;49;00m[31mINSTALL_DATA[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mWRKSRC[39;49;00m[33m}[39;49;00m/Lib/[33m${[39;49;00m[31mplatform[39;49;00m[33m}[39;49;00m/[33m${[39;49;00m[31mfile[39;49;00m[33m}[39;49;00m [33m\[39;49;00m$
   181^I^I^I[33m${[39;49;00m[31mPYTHONPREFIX_LIBDIR[39;49;00m[33m}[39;49;00m/[33m${[39;49;00m[31mplatform[39;49;00m[33m}[39;49;00m/$
   182^I[36m.endfor[39;49;00m$
   183^I[36m.endfor[39;49;00m$
   184^I$
   185^I[32mpre-install[39;49;00m:$
   186^I^I[33m${[39;49;00m[31mCAT[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mPLIST_TEMPLATE[39;49;00m[33m}[39;49;00m | [33m${[39;49;00m[31mAWK[39;49;00m[33m}[39;49;00m [33m'{ print $$0; } \[39;49;00m$
   187^I[33m^I/LIBDIR.*\.py$$/ && !/\/bad/ { print $$0 "o"; print $$0 "c"; }'[39;49;00m^I> [33m${[39;49;00m[31mPLIST[39;49;00m[33m}[39;49;00m$
   188^I$
   189^I[37m^I@# if openssl 0.9.8 is detected, _sha{256,512} module won't be installed[39;49;00m$
   190^I^I([ -f [33m${[39;49;00m[31mWRKSRC[39;49;00m[33m}[39;49;00m/.without_own_sha ] && [33m\[39;49;00m$
   191^I^I^I[33m${[39;49;00m[31mGREP[39;49;00m[33m}[39;49;00m -v [33m'lib-dynload/_sha'[39;49;00m [33m${[39;49;00m[31mPLIST[39;49;00m[33m}[39;49;00m > [33m${[39;49;00m[31mPLIST[39;49;00m[33m}[39;49;00m.tmp && [33m\[39;49;00m$
   192^I^I^I[33m${[39;49;00m[31mCAT[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mPLIST[39;49;00m[33m}[39;49;00m.tmp > [33m${[39;49;00m[31mPLIST[39;49;00m[33m}[39;49;00m) || [33m${[39;49;00m[31mTRUE[39;49;00m[33m}[39;49;00m$
   193^I$
   194^I[32mpost-install[39;49;00m:$
   195^I[37m^I@# install config providers[39;49;00m$
   196^I^I[33m${[39;49;00m[31mINSTALL_SCRIPT[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mWRKDIR[39;49;00m[33m}[39;49;00m/[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m[33m}[39;49;00m-config [33m${[39;49;00m[31mPREFIX[39;49;00m[33m}[39;49;00m/bin$
   197^I^I[33m${[39;49;00m[31mINSTALL_SCRIPT[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mWRKDIR[39;49;00m[33m}[39;49;00m/[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m:[31mS[39;49;00m/thon/thon-shared/[33m}[39;49;00m-config [33m${[39;49;00m[31mPREFIX[39;49;00m[33m}[39;49;00m/bin$
   198^I$
   199^I[37m^I@# shared version of executable and library[39;49;00m$
   200^I^I[33m${[39;49;00m[31mINSTALL_PROGRAM[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mSHARED_WRKSRC[39;49;00m[33m}[39;49;00m/lib[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m[33m}[39;49;00m.so.1 [33m\[39;49;00m$
   201^I^I^I[33m${[39;49;00m[31mPREFIX[39;49;00m[33m}[39;49;00m/lib$
   202^I^I[36mcd[39;49;00m [33m${[39;49;00m[31mPREFIX[39;49;00m[33m}[39;49;00m/lib; [33m${[39;49;00m[31mLN[39;49;00m[33m}[39;49;00m -sf lib[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m[33m}[39;49;00m.so.1 [33m\[39;49;00m$
   203^I^I^Ilib[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m[33m}[39;49;00m.so$
   204^I^I[33m${[39;49;00m[31mLN[39;49;00m[33m}[39;49;00m -sf [33m${[39;49;00m[31mPREFIX[39;49;00m[33m}[39;49;00m/lib/lib[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m[33m}[39;49;00m.so [33m${[39;49;00m[31mPYTHONPREFIX_LIBDIR[39;49;00m[33m}[39;49;00m/config$
   205^I^I[33m${[39;49;00m[31mINSTALL_PROGRAM[39;49;00m[33m}[39;49;00m [33m\[39;49;00m$
   206^I^I^I[33m${[39;49;00m[31mSHARED_WRKSRC[39;49;00m[33m}[39;49;00m/[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m:[31mS[39;49;00m/thon/thon-shared/[33m}[39;49;00m [33m\[39;49;00m$
   207^I^I^I[33m${[39;49;00m[31mPREFIX[39;49;00m[33m}[39;49;00m/bin$
   208^I$
   209^I[37m^I@# additional files installing by ports[39;49;00m$
   210^I^I[33m${[39;49;00m[31mINSTALL_SCRIPT[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mWRKDIR[39;49;00m[33m}[39;49;00m/pydoc2.5 [33m${[39;49;00m[31mWRKDIR[39;49;00m[33m}[39;49;00m/idle2.5 [33m\[39;49;00m$
   211^I^I^I[33m${[39;49;00m[31mWRKDIR[39;49;00m[33m}[39;49;00m/smtpd2.5.py [33m${[39;49;00m[31mPREFIX[39;49;00m[33m}[39;49;00m/bin$
   212^I^I@[33m${[39;49;00m[31mMKDIR[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mMANPREFIX[39;49;00m[33m}[39;49;00m/man/man1$
   213^I^I[33m${[39;49;00m[31mINSTALL_MAN[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mPYTHON_WRKSRC[39;49;00m[33m}[39;49;00m/Misc/python.man [33m\[39;49;00m$
   214^I^I^I[33m${[39;49;00m[31mMANPREFIX[39;49;00m[33m}[39;49;00m/man/man1/[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m[33m}[39;49;00m.1$
   215^I$
   216^I[36m.if ${PYTHON_VERSION} == ${PYTHON_DEFAULT_VERSION}[39;49;00m$
   217^I^I[34mfor[39;49;00m f [34min[39;49;00m [33m${[39;49;00m[31mBIN_SCRIPTS[39;49;00m[33m}[39;49;00m; [34mdo[39;49;00m [33m\[39;49;00m$
   218^I^I^I[31mTARGET[39;49;00m=[33m`[39;49;00m[33m${[39;49;00m[31mECHO_CMD[39;49;00m[33m}[39;49;00m [31m$$[39;49;00mf | [33m${[39;49;00m[31mSED[39;49;00m[33m}[39;49;00m -E [33m${[39;49;00m[31mBINLINKS_SUB[39;49;00m[33m}[39;49;00m[33m`[39;49;00m; [33m\[39;49;00m$
   219^I^I^I[36mcd[39;49;00m [33m${[39;49;00m[31mPREFIX[39;49;00m[33m}[39;49;00m/bin && [33m${[39;49;00m[31mLN[39;49;00m[33m}[39;49;00m -f [31m$$[39;49;00mTARGET [31m$$[39;49;00mf; [33m\[39;49;00m$
   220^I^I[34mdone[39;49;00m$
   221^I[36m.endif[39;49;00m$
   222^I$
   223^I[36m.if !defined(NOPORTDOCS)[39;49;00m$
   224^I^I@[33m${[39;49;00m[31mMKDIR[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mTOOLSDIR[39;49;00m[33m}[39;49;00m$
   225^I^I@cd [33m${[39;49;00m[31mPYTHON_WRKSRC[39;49;00m[33m}[39;49;00m; [33m${[39;49;00m[31mTAR[39;49;00m[33m}[39;49;00m -cf - Tools | [33m\[39;49;00m$
   226^I^I^I([36mcd[39;49;00m [33m${[39;49;00m[31mTOOLSDIR[39;49;00m[33m}[39;49;00m; [33m${[39;49;00m[31mTAR[39;49;00m[33m}[39;49;00m -xf -)$
   227^I^I@[33m${[39;49;00m[31mMKDIR[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mDEMODIR[39;49;00m[33m}[39;49;00m$
   228^I^I@cd [33m${[39;49;00m[31mPYTHON_WRKSRC[39;49;00m[33m}[39;49;00m/Demo; [33m${[39;49;00m[31mTAR[39;49;00m[33m}[39;49;00m -cf - * | [33m\[39;49;00m$
   229^I^I^I([36mcd[39;49;00m [33m${[39;49;00m[31mDEMODIR[39;49;00m[33m}[39;49;00m; [33m${[39;49;00m[31mTAR[39;49;00m[33m}[39;49;00m -xf -)$
   230^I[36m.endif[39;49;00m$
   231^I$
   232^I^I@[33m${[39;49;00m[31mCAT[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mPKGMESSAGE[39;49;00m[33m}[39;49;00m$
   233^I$
   234^I[36m.include <bsd.port.post.mk>[39;49;00m$

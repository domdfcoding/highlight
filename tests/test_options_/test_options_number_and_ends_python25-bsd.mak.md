     1	[37m# New ports collection makefile for:    python25[39;49;00m$
     2	[37m# Date created:         3 July 2003[39;49;00m$
     3	[37m# Whom:                 Hye-Shik Chang <perky@FreeBSD.org>[39;49;00m$
     4	[37m#[39;49;00m$
     5	[37m# $FreeBSD: ports/lang/python25/Makefile,v 1.145 2007/10/03 23:22:04 edwin Exp $[39;49;00m$
     6	$
     7	[31mPORTNAME[39;49;00m=	python25$
     8	[31mPORTVERSION[39;49;00m=	[34m2[39;49;00m.5.1$
     9	[31mCATEGORIES[39;49;00m=	lang python ipv6$
    10	[31mMASTER_SITES[39;49;00m=	[33m${[39;49;00m[31mPYTHON_MASTER_SITES[39;49;00m[33m}[39;49;00m$
    11	[31mMASTER_SITE_SUBDIR[39;49;00m=	[33m${[39;49;00m[31mPYTHON_MASTER_SITE_SUBDIR[39;49;00m[33m}[39;49;00m$
    12	[31mDISTFILES[39;49;00m=	[33m${[39;49;00m[31mPYTHON_DISTFILE[39;49;00m[33m}[39;49;00m$
    13	$
    14	[31mMAINTAINER[39;49;00m=	python@FreeBSD.org$
    15	[31mCOMMENT[39;49;00m?=	An interpreted object-oriented programming language$
    16	$
    17	[31mDIST_SUBDIR[39;49;00m=	python$
    18	[31mWRKSRC[39;49;00m=		[33m${[39;49;00m[31mPYTHON_WRKSRC[39;49;00m[33m}[39;49;00m/portbld.static$
    19	[31mPATCH_WRKSRC[39;49;00m=	[33m${[39;49;00m[31mPYTHON_WRKSRC[39;49;00m[33m}[39;49;00m$
    20	[31mGNU_CONFIGURE[39;49;00m=	yes$
    21	[31mCONFIGURE_TARGET[39;49;00m=	--build=[33m${[39;49;00m[31mMACHINE_ARCH[39;49;00m[33m}[39;49;00m-portbld-freebsd[33m${[39;49;00m[31mOSREL[39;49;00m[33m}[39;49;00m$
    22	[31mCONFIGURE_SCRIPT[39;49;00m=	../configure [37m# must be relative[39;49;00m$
    23	[31mCONFIGURE_ENV[39;49;00m=	[31mOPT[39;49;00m=[33m"[39;49;00m[33m${[39;49;00m[31mCFLAGS[39;49;00m[33m}[39;49;00m[33m"[39;49;00m [31mSVNVERSION[39;49;00m=[33m"echo freebsd"[39;49;00m$
    24	[31mMAKE_ENV[39;49;00m=	[31mVPATH[39;49;00m=[33m"[39;49;00m[33m${[39;49;00m[31mPYTHON_WRKSRC[39;49;00m[33m}[39;49;00m[33m"[39;49;00m$
    25	[31mINSTALLS_SHLIB[39;49;00m=	yes$
    26	[31mINSTALL_TARGET[39;49;00m=	altinstall$
    27	[31mMAN1[39;49;00m=		[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m[33m}[39;49;00m.1$
    28	$
    29	[31mUSE_PYTHON[39;49;00m=	yes$
    30	[31mPYTHON_VERSION[39;49;00m=	python2.5$
    31	[31mPYTHON_NO_DEPENDS[39;49;00m=	yes$
    32	$
    33	[31mSHARED_WRKSRC[39;49;00m=	[33m${[39;49;00m[31mPYTHON_WRKSRC[39;49;00m[33m}[39;49;00m/portbld.shared$
    34	[31mPLIST[39;49;00m=		[33m${[39;49;00m[31mWRKDIR[39;49;00m[33m}[39;49;00m/PLIST$
    35	[31mPLIST_TEMPLATE[39;49;00m?=[33m${[39;49;00m[31mPKGDIR[39;49;00m[33m}[39;49;00m/pkg-plist$
    36	[31mPLIST_SUB[39;49;00m=	[31mPYVER[39;49;00m=[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m:[31mS[39;49;00m/python//[33m}[39;49;00m [33m\[39;49;00m$
    37			[31mPYVER_WITHPAT[39;49;00m=[33m${[39;49;00m[31mPORTVERSION[39;49;00m:[31mS[39;49;00m/.c/c/[33m}[39;49;00m$
    38	[31mDEMODIR[39;49;00m=	[33m${[39;49;00m[31mPREFIX[39;49;00m[33m}[39;49;00m/share/examples/[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m[33m}[39;49;00m$
    39	[31mTOOLSDIR[39;49;00m=	[33m${[39;49;00m[31mPREFIX[39;49;00m[33m}[39;49;00m/share/[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m[33m}[39;49;00m$
    40	$
    41	[31mBIN_SCRIPTS[39;49;00m=	idle pydoc python python-shared smtpd.py python-config [33m\[39;49;00m$
    42			python-shared-config$
    43	[31mBINLINKS_SUB[39;49;00m=	-e [33m's,smtpd,smtpd${PYTHON_VER},'[39;49;00m [33m\[39;49;00m$
    44			-e [33m's,(idle|pydoc|python-shared|python),\1${PYTHON_VER},'[39;49;00m$
    45	$
    46	[31mOPTIONS[39;49;00m=	THREADS [33m"Enable thread support"[39;49;00m on [33m\[39;49;00m$
    47			HUGE_STACK_SIZE [33m"Use a larger thread stack"[39;49;00m off [33m\[39;49;00m$
    48			UCS4 [33m"Use UCS4 for unicode support"[39;49;00m on [33m\[39;49;00m$
    49			PYMALLOC [33m"Use python's internal malloc"[39;49;00m on [33m\[39;49;00m$
    50			IPV6 [33m"Enable IPv6 support"[39;49;00m on [33m\[39;49;00m$
    51			FPECTL [33m"Enable floating point exception handling"[39;49;00m off$
    52	$
    53	[36m.include <bsd.port.pre.mk>[39;49;00m$
    54	$
    55	[36m.if ${PYTHON_VERSION} == ${PYTHON_DEFAULT_VERSION}[39;49;00m$
    56	[31mMLINKS[39;49;00m=		[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m[33m}[39;49;00m.1 python.1$
    57	[31mPLIST_SUB[39;49;00m+=	[31mIF_DEFAULT[39;49;00m=[33m""[39;49;00m$
    58	[36m.else[39;49;00m$
    59	[31mPLIST_SUB[39;49;00m+=	[31mIF_DEFAULT[39;49;00m=[33m"@comment "[39;49;00m$
    60	[36m.endif[39;49;00m$
    61	$
    62	[37m# workaround for a bug in base curses.h.[39;49;00m$
    63	[31mCFLAGS[39;49;00m+=	-D__wchar_t=wchar_t$
    64	$
    65	[36m.if !defined(WITHOUT_THREADS)[39;49;00m$
    66	[31mCONFIGURE_ARGS[39;49;00m+=	--with-threads$
    67	[31mCFLAGS[39;49;00m+=		[33m${[39;49;00m[31mPTHREAD_CFLAGS[39;49;00m[33m}[39;49;00m$
    68	[36m.if defined(WITHOUT_HUGE_STACK_SIZE)[39;49;00m$
    69	[31mCFLAGS[39;49;00m+=		-DTHREAD_STACK_SIZE=0x20000$
    70	[36m.else[39;49;00m$
    71	[31mCFLAGS[39;49;00m+=		-DTHREAD_STACK_SIZE=0x100000$
    72	[36m.endif # defined(WITHOUT_HUGE_STACK_SIZE)[39;49;00m$
    73	[31mCONFIGURE_ENV[39;49;00m+=		[31mLDFLAGS[39;49;00m=[33m"[39;49;00m[33m${[39;49;00m[31mPTHREAD_LIBS[39;49;00m[33m}[39;49;00m[33m [39;49;00m[33m${[39;49;00m[31mLDFLAGS[39;49;00m[33m}[39;49;00m[33m"[39;49;00m$
    74	[36m.else[39;49;00m$
    75	[31mCONFIGURE_ARGS[39;49;00m+=	--without-threads$
    76	[36m.if defined(LDFLAGS)[39;49;00m$
    77	[31mCONFIGURE_ENV[39;49;00m+=		[31mLDFLAGS[39;49;00m=[33m"[39;49;00m[33m${[39;49;00m[31mLDFLAGS[39;49;00m[33m}[39;49;00m[33m"[39;49;00m$
    78	[36m.endif # defined(LDFLAGS)[39;49;00m$
    79	[36m.endif # !defined(WITHOUT_THREADS)[39;49;00m$
    80	$
    81	[36m.if !defined(WITHOUT_UCS4) && !defined(WITH_UCS2)[39;49;00m$
    82	[31mCONFIGURE_ARGS[39;49;00m+=	--enable-unicode=ucs4$
    83	[36m.endif[39;49;00m$
    84	$
    85	[36m.if defined(WITHOUT_PYMALLOC)[39;49;00m$
    86	[31mCONFIGURE_ARGS[39;49;00m+=        --without-pymalloc$
    87	[36m.endif[39;49;00m$
    88	$
    89	[36m.if ${ARCH} == i386[39;49;00m$
    90	[31mPLIST_SUB[39;49;00m+=	[31mX86_ONLY[39;49;00m=[33m""[39;49;00m$
    91	[36m.else[39;49;00m$
    92	[31mPLIST_SUB[39;49;00m+=	[31mX86_ONLY[39;49;00m=[33m"@comment "[39;49;00m$
    93	[36m.endif[39;49;00m$
    94	[36m.if ${ARCH} == amd64 || ${ARCH} == ia64 || ${ARCH} == sparc64 || ${ARCH} == alpha[39;49;00m$
    95	[31mPLIST_SUB[39;49;00m+=     [31m32BIT_ONLY[39;49;00m=[33m"@comment "[39;49;00m$
    96	[36m.else[39;49;00m$
    97	[31mPLIST_SUB[39;49;00m+=     [31m32BIT_ONLY[39;49;00m=[33m""[39;49;00m$
    98	[36m.endif[39;49;00m$
    99	[36m.if ${ARCH} == sparc64[39;49;00m$
   100	[31mCFLAGS[39;49;00m+=        -DPYTHON_DEFAULT_RECURSION_LIMIT=[34m900[39;49;00m$
   101	[36m.endif[39;49;00m$
   102	$
   103	[36m.if !exists(/usr/bin/ypcat) # the world with NO_NIS[39;49;00m$
   104	[31mPLIST_SUB[39;49;00m+=	[31mNO_NIS[39;49;00m=[33m"@comment "[39;49;00m$
   105	[36m.else[39;49;00m$
   106	[31mPLIST_SUB[39;49;00m+=	[31mNO_NIS[39;49;00m=[33m""[39;49;00m$
   107	[36m.endif[39;49;00m$
   108	$
   109	[36m.if !defined(WITHOUT_IPV6)[39;49;00m$
   110	[31mCONFIGURE_ARGS[39;49;00m+= --enable-ipv6$
   111	[36m.else[39;49;00m$
   112	[31mCONFIGURE_ARGS[39;49;00m+= --disable-ipv6$
   113	[36m.endif[39;49;00m$
   114	$
   115	[36m.if defined(WITH_FPECTL)[39;49;00m$
   116	[31mCONFIGURE_ARGS[39;49;00m+= --with-fpectl$
   117	[36m.endif[39;49;00m$
   118	$
   119	[36m.if ${OSVERSION} >= 700000[39;49;00m$
   120	[31mPLATFORMS[39;49;00m=plat-freebsd4 plat-freebsd5 plat-freebsd6$
   121	[36m.elif ${OSVERSION} >= 600000[39;49;00m$
   122	[31mPLATFORMS[39;49;00m=plat-freebsd4 plat-freebsd5 plat-freebsd7$
   123	[36m.else[39;49;00m$
   124	[31mPLATFORMS[39;49;00m=plat-freebsd4 plat-freebsd6 plat-freebsd7$
   125	[36m.endif[39;49;00m$
   126	$
   127	[32mpre-patch[39;49;00m:$
   128		[33m${[39;49;00m[31mMKDIR[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mWRKSRC[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mSHARED_WRKSRC[39;49;00m[33m}[39;49;00m/Modules$
   129		[33m${[39;49;00m[31mSED[39;49;00m[33m}[39;49;00m -e [33m'1s,^.*$$,#!${PREFIX}/bin/${PYTHON_VERSION},'[39;49;00m [33m\[39;49;00m$
   130			[33m${[39;49;00m[31mPATCH_WRKSRC[39;49;00m[33m}[39;49;00m/Tools/scripts/pydoc > [33m${[39;49;00m[31mWRKDIR[39;49;00m[33m}[39;49;00m/pydoc2.5$
   131		[33m${[39;49;00m[31mSED[39;49;00m[33m}[39;49;00m -e [33m'1s,^.*$$,#!${PREFIX}/bin/${PYTHON_VERSION},'[39;49;00m [33m\[39;49;00m$
   132			[33m${[39;49;00m[31mPATCH_WRKSRC[39;49;00m[33m}[39;49;00m/Tools/scripts/idle > [33m${[39;49;00m[31mWRKDIR[39;49;00m[33m}[39;49;00m/idle2.5$
   133		[33m${[39;49;00m[31mSED[39;49;00m[33m}[39;49;00m -e [33m'1s,^.*$$,#!${PREFIX}/bin/${PYTHON_VERSION},'[39;49;00m [33m\[39;49;00m$
   134			[33m${[39;49;00m[31mPATCH_WRKSRC[39;49;00m[33m}[39;49;00m/Lib/smtpd.py > [33m${[39;49;00m[31mWRKDIR[39;49;00m[33m}[39;49;00m/smtpd2.5.py$
   135		[33m${[39;49;00m[31mREINPLACE_CMD[39;49;00m[33m}[39;49;00m -e [33m\[39;49;00m$
   136			[33m's,/usr/doc/python-docs-,${PREFIX}/share/doc/python,g'[39;49;00m [33m\[39;49;00m$
   137			[33m${[39;49;00m[31mPATCH_WRKSRC[39;49;00m[33m}[39;49;00m/Lib/pydoc.py$
   138		[33m${[39;49;00m[31mREINPLACE_CMD[39;49;00m[33m}[39;49;00m -e [33m\[39;49;00m$
   139			[33m's|^\( *prefixes = .*\)\]$$|\1, "${X11BASE}"]|g'[39;49;00m [33m\[39;49;00m$
   140			[33m${[39;49;00m[31mPATCH_WRKSRC[39;49;00m[33m}[39;49;00m/Lib/site.py$
   141		[33m${[39;49;00m[31mREINPLACE_CMD[39;49;00m[33m}[39;49;00m -e [33m\[39;49;00m$
   142			[33m's|^	\(..ASDLGEN.*\)$$|	${TRUE}|g'[39;49;00m [33m\[39;49;00m$
   143			[33m${[39;49;00m[31mPATCH_WRKSRC[39;49;00m[33m}[39;49;00m/Makefile.pre.in$
   144	$
   145		[33m${[39;49;00m[31mREINPLACE_CMD[39;49;00m[33m}[39;49;00m -e [33m\[39;49;00m$
   146			[33m's|*\(..INSTALL_SCRIPT.*\)python-config$$|#port \1|'[39;49;00m [33m\[39;49;00m$
   147			[33m${[39;49;00m[31mPATCH_WRKSRC[39;49;00m[33m}[39;49;00m/Makefile.pre.in$
   148	$
   149		[33m${[39;49;00m[31mSED[39;49;00m[33m}[39;49;00m -e [33m's|^#!.*|#!${PREFIX}/bin/${PYTHON_VERSION}|'[39;49;00m [33m\[39;49;00m$
   150			[33m${[39;49;00m[31mPATCH_WRKSRC[39;49;00m[33m}[39;49;00m/Misc/python-config.in > [33m${[39;49;00m[31mWRKDIR[39;49;00m[33m}[39;49;00m/[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m[33m}[39;49;00m-config$
   151		[33m${[39;49;00m[31mSED[39;49;00m[33m}[39;49;00m -e [33m's|^#!.*|#!${PREFIX}/bin/${PYTHON_VERSION:S/thon/thon-shared/}|'[39;49;00m [33m\[39;49;00m$
   152			[33m${[39;49;00m[31mPATCH_WRKSRC[39;49;00m[33m}[39;49;00m/Misc/python-config.in > [33m${[39;49;00m[31mWRKDIR[39;49;00m[33m}[39;49;00m/[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m:[31mS[39;49;00m/thon/thon-shared/[33m}[39;49;00m-config$
   153	$
   154	[36m.if defined(WITH_FPECTL) && ${ARCH} == i386[39;49;00m$
   155		[33m${[39;49;00m[31mMKDIR[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mWRKSRC[39;49;00m[33m}[39;49;00m/Modules$
   156		[33m${[39;49;00m[31mECHO[39;49;00m[33m}[39;49;00m [33m"fpectl fpectlmodule.c"[39;49;00m >> [33m${[39;49;00m[31mWRKSRC[39;49;00m[33m}[39;49;00m/Modules/Setup.dist$
   157	[36m.endif[39;49;00m$
   158	$
   159	[32mpost-configure[39;49;00m:$
   160		[33m${[39;49;00m[31mTAR[39;49;00m[33m}[39;49;00m -C [33m${[39;49;00m[31mWRKSRC[39;49;00m[33m}[39;49;00m -cf - . | [33m${[39;49;00m[31mTAR[39;49;00m[33m}[39;49;00m -C [33m${[39;49;00m[31mSHARED_WRKSRC[39;49;00m[33m}[39;49;00m -xf -$
   161		[33m${[39;49;00m[31mLN[39;49;00m[33m}[39;49;00m -sf [33m${[39;49;00m[31mPYTHON_WRKSRC[39;49;00m[33m}[39;49;00m/Lib [33m${[39;49;00m[31mWRKSRC[39;49;00m[33m}[39;49;00m/Lib$
   162		[33m${[39;49;00m[31mSED[39;49;00m[33m}[39;49;00m -e [33m's,^\(LDLIBRARY=\).*$$,\1libpython$$(VERSION).so,'[39;49;00m [33m\[39;49;00m$
   163			-e [33m's,^\(BLDLIBRARY=\).*$$,\1-L. -lpython$$(VERSION),'[39;49;00m [33m\[39;49;00m$
   164			-e [33m's,^\(CFLAGSFORSHARED=\).*$$,\1$$(CCSHARED),'[39;49;00m [33m\[39;49;00m$
   165			-e [33m's,^\(Makefile Modules/config.c:.*\)Makefile.pre,\1,'[39;49;00m [33m\[39;49;00m$
   166			-e [33m's,^\(.(BUILDPYTHON)\: .*\).(LIBRARY),\1,'[39;49;00m [33m\[39;49;00m$
   167			-e [33m's,^\(.(BUILDPYTHON):.*\).(LIBRARY),\1,'[39;49;00m [33m\[39;49;00m$
   168			[33m${[39;49;00m[31mWRKSRC[39;49;00m[33m}[39;49;00m/Makefile > [33m${[39;49;00m[31mSHARED_WRKSRC[39;49;00m[33m}[39;49;00m/Makefile$
   169	$
   170	[32mpre-build[39;49;00m:$
   171		[36mcd[39;49;00m [33m${[39;49;00m[31mSHARED_WRKSRC[39;49;00m[33m}[39;49;00m; [33m\[39;49;00m$
   172		[33m${[39;49;00m[31mSETENV[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mMAKE_ENV[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mMAKE[39;49;00m[33m}[39;49;00m lib[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m[33m}[39;49;00m.so python; [33m\[39;49;00m$
   173		[33m${[39;49;00m[31mLN[39;49;00m[33m}[39;49;00m -f lib[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m[33m}[39;49;00m.so lib[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m[33m}[39;49;00m.so.1; [33m\[39;49;00m$
   174		[33m${[39;49;00m[31mLN[39;49;00m[33m}[39;49;00m -f python [33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m:[31mS[39;49;00m/thon/thon-shared/[33m}[39;49;00m$
   175	$
   176	[32mpre-su-install[39;49;00m:$
   177	[36m.for platform in ${PLATFORMS}[39;49;00m$
   178		[33m${[39;49;00m[31mMKDIR[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mPYTHONPREFIX_LIBDIR[39;49;00m[33m}[39;49;00m/[33m${[39;49;00m[31mplatform[39;49;00m[33m}[39;49;00m$
   179	[36m.for file in IN.py regen[39;49;00m$
   180		[33m${[39;49;00m[31mINSTALL_DATA[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mWRKSRC[39;49;00m[33m}[39;49;00m/Lib/[33m${[39;49;00m[31mplatform[39;49;00m[33m}[39;49;00m/[33m${[39;49;00m[31mfile[39;49;00m[33m}[39;49;00m [33m\[39;49;00m$
   181			[33m${[39;49;00m[31mPYTHONPREFIX_LIBDIR[39;49;00m[33m}[39;49;00m/[33m${[39;49;00m[31mplatform[39;49;00m[33m}[39;49;00m/$
   182	[36m.endfor[39;49;00m$
   183	[36m.endfor[39;49;00m$
   184	$
   185	[32mpre-install[39;49;00m:$
   186		[33m${[39;49;00m[31mCAT[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mPLIST_TEMPLATE[39;49;00m[33m}[39;49;00m | [33m${[39;49;00m[31mAWK[39;49;00m[33m}[39;49;00m [33m'{ print $$0; } \[39;49;00m$
   187	[33m	/LIBDIR.*\.py$$/ && !/\/bad/ { print $$0 "o"; print $$0 "c"; }'[39;49;00m	> [33m${[39;49;00m[31mPLIST[39;49;00m[33m}[39;49;00m$
   188	$
   189	[37m	@# if openssl 0.9.8 is detected, _sha{256,512} module won't be installed[39;49;00m$
   190		([ -f [33m${[39;49;00m[31mWRKSRC[39;49;00m[33m}[39;49;00m/.without_own_sha ] && [33m\[39;49;00m$
   191			[33m${[39;49;00m[31mGREP[39;49;00m[33m}[39;49;00m -v [33m'lib-dynload/_sha'[39;49;00m [33m${[39;49;00m[31mPLIST[39;49;00m[33m}[39;49;00m > [33m${[39;49;00m[31mPLIST[39;49;00m[33m}[39;49;00m.tmp && [33m\[39;49;00m$
   192			[33m${[39;49;00m[31mCAT[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mPLIST[39;49;00m[33m}[39;49;00m.tmp > [33m${[39;49;00m[31mPLIST[39;49;00m[33m}[39;49;00m) || [33m${[39;49;00m[31mTRUE[39;49;00m[33m}[39;49;00m$
   193	$
   194	[32mpost-install[39;49;00m:$
   195	[37m	@# install config providers[39;49;00m$
   196		[33m${[39;49;00m[31mINSTALL_SCRIPT[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mWRKDIR[39;49;00m[33m}[39;49;00m/[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m[33m}[39;49;00m-config [33m${[39;49;00m[31mPREFIX[39;49;00m[33m}[39;49;00m/bin$
   197		[33m${[39;49;00m[31mINSTALL_SCRIPT[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mWRKDIR[39;49;00m[33m}[39;49;00m/[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m:[31mS[39;49;00m/thon/thon-shared/[33m}[39;49;00m-config [33m${[39;49;00m[31mPREFIX[39;49;00m[33m}[39;49;00m/bin$
   198	$
   199	[37m	@# shared version of executable and library[39;49;00m$
   200		[33m${[39;49;00m[31mINSTALL_PROGRAM[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mSHARED_WRKSRC[39;49;00m[33m}[39;49;00m/lib[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m[33m}[39;49;00m.so.1 [33m\[39;49;00m$
   201			[33m${[39;49;00m[31mPREFIX[39;49;00m[33m}[39;49;00m/lib$
   202		[36mcd[39;49;00m [33m${[39;49;00m[31mPREFIX[39;49;00m[33m}[39;49;00m/lib; [33m${[39;49;00m[31mLN[39;49;00m[33m}[39;49;00m -sf lib[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m[33m}[39;49;00m.so.1 [33m\[39;49;00m$
   203			lib[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m[33m}[39;49;00m.so$
   204		[33m${[39;49;00m[31mLN[39;49;00m[33m}[39;49;00m -sf [33m${[39;49;00m[31mPREFIX[39;49;00m[33m}[39;49;00m/lib/lib[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m[33m}[39;49;00m.so [33m${[39;49;00m[31mPYTHONPREFIX_LIBDIR[39;49;00m[33m}[39;49;00m/config$
   205		[33m${[39;49;00m[31mINSTALL_PROGRAM[39;49;00m[33m}[39;49;00m [33m\[39;49;00m$
   206			[33m${[39;49;00m[31mSHARED_WRKSRC[39;49;00m[33m}[39;49;00m/[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m:[31mS[39;49;00m/thon/thon-shared/[33m}[39;49;00m [33m\[39;49;00m$
   207			[33m${[39;49;00m[31mPREFIX[39;49;00m[33m}[39;49;00m/bin$
   208	$
   209	[37m	@# additional files installing by ports[39;49;00m$
   210		[33m${[39;49;00m[31mINSTALL_SCRIPT[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mWRKDIR[39;49;00m[33m}[39;49;00m/pydoc2.5 [33m${[39;49;00m[31mWRKDIR[39;49;00m[33m}[39;49;00m/idle2.5 [33m\[39;49;00m$
   211			[33m${[39;49;00m[31mWRKDIR[39;49;00m[33m}[39;49;00m/smtpd2.5.py [33m${[39;49;00m[31mPREFIX[39;49;00m[33m}[39;49;00m/bin$
   212		@[33m${[39;49;00m[31mMKDIR[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mMANPREFIX[39;49;00m[33m}[39;49;00m/man/man1$
   213		[33m${[39;49;00m[31mINSTALL_MAN[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mPYTHON_WRKSRC[39;49;00m[33m}[39;49;00m/Misc/python.man [33m\[39;49;00m$
   214			[33m${[39;49;00m[31mMANPREFIX[39;49;00m[33m}[39;49;00m/man/man1/[33m${[39;49;00m[31mPYTHON_VERSION[39;49;00m[33m}[39;49;00m.1$
   215	$
   216	[36m.if ${PYTHON_VERSION} == ${PYTHON_DEFAULT_VERSION}[39;49;00m$
   217		[34mfor[39;49;00m f [34min[39;49;00m [33m${[39;49;00m[31mBIN_SCRIPTS[39;49;00m[33m}[39;49;00m; [34mdo[39;49;00m [33m\[39;49;00m$
   218			[31mTARGET[39;49;00m=[33m`[39;49;00m[33m${[39;49;00m[31mECHO_CMD[39;49;00m[33m}[39;49;00m [31m$$[39;49;00mf | [33m${[39;49;00m[31mSED[39;49;00m[33m}[39;49;00m -E [33m${[39;49;00m[31mBINLINKS_SUB[39;49;00m[33m}[39;49;00m[33m`[39;49;00m; [33m\[39;49;00m$
   219			[36mcd[39;49;00m [33m${[39;49;00m[31mPREFIX[39;49;00m[33m}[39;49;00m/bin && [33m${[39;49;00m[31mLN[39;49;00m[33m}[39;49;00m -f [31m$$[39;49;00mTARGET [31m$$[39;49;00mf; [33m\[39;49;00m$
   220		[34mdone[39;49;00m$
   221	[36m.endif[39;49;00m$
   222	$
   223	[36m.if !defined(NOPORTDOCS)[39;49;00m$
   224		@[33m${[39;49;00m[31mMKDIR[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mTOOLSDIR[39;49;00m[33m}[39;49;00m$
   225		@cd [33m${[39;49;00m[31mPYTHON_WRKSRC[39;49;00m[33m}[39;49;00m; [33m${[39;49;00m[31mTAR[39;49;00m[33m}[39;49;00m -cf - Tools | [33m\[39;49;00m$
   226			([36mcd[39;49;00m [33m${[39;49;00m[31mTOOLSDIR[39;49;00m[33m}[39;49;00m; [33m${[39;49;00m[31mTAR[39;49;00m[33m}[39;49;00m -xf -)$
   227		@[33m${[39;49;00m[31mMKDIR[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mDEMODIR[39;49;00m[33m}[39;49;00m$
   228		@cd [33m${[39;49;00m[31mPYTHON_WRKSRC[39;49;00m[33m}[39;49;00m/Demo; [33m${[39;49;00m[31mTAR[39;49;00m[33m}[39;49;00m -cf - * | [33m\[39;49;00m$
   229			([36mcd[39;49;00m [33m${[39;49;00m[31mDEMODIR[39;49;00m[33m}[39;49;00m; [33m${[39;49;00m[31mTAR[39;49;00m[33m}[39;49;00m -xf -)$
   230	[36m.endif[39;49;00m$
   231	$
   232		@[33m${[39;49;00m[31mCAT[39;49;00m[33m}[39;49;00m [33m${[39;49;00m[31mPKGMESSAGE[39;49;00m[33m}[39;49;00m$
   233	$
   234	[36m.include <bsd.port.post.mk>[39;49;00m$

     1	[37m// vim:ft=pascal[39;49;00m$
     2	$
     3	[34munit[39;49;00m YTools;$
     4	$
     5	[37m{===============================================================================[39;49;00m$
     6	[37m[39;49;00m$
     7	[37m   cYcnus.YTools 1.0.3 Beta for Delphi 4+[39;49;00m$
     8	[37m   by licenser and Murphy[39;49;00m$
     9	[37m[39;49;00m$
    10	[37m   ©2000-2003 by cYcnus[39;49;00m$
    11	[37m   visit www.cYcnus.de[39;49;00m$
    12	[37m[39;49;00m$
    13	[37m   licenser@cYcnus.de (Heinz N. Gies)[39;49;00m$
    14	[37m   murphy@cYcnus.de (Kornelius Kalnbach)[39;49;00m$
    15	[37m   [39;49;00m$
    16	[37m   this unit is published under the terms of the GPL[39;49;00m$
    17	[37m[39;49;00m$
    18	[37m===============================================================================}[39;49;00m$
    19	$
    20	[34minterface[39;49;00m$
    21	$
    22	[34muses[39;49;00m$
    23	  Windows, SysUtils, Classes, YTypes;$
    24	$
    25	[34mconst[39;49;00m$
    26	  BackSpace = [33m#8[39;49;00m;$
    27	  Tab = [33m#9[39;49;00m;$
    28	  LF = [33m#10[39;49;00m; [37m//Line Feed[39;49;00m$
    29	  CR = [33m#13[39;49;00m; [37m//Carriage Return[39;49;00m$
    30	  Space = [33m#32[39;49;00m;$
    31	  EOLChars = [CR, LF];$
    32	[37m{$IFNDEF VER140}[39;49;00m$
    33	  sLineBreak = [33m#13[39;49;00m[33m#10[39;49;00m;$
    34	  SwitchChars = [[33m'[39;49;00m[33m/[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33m-[39;49;00m[33m'[39;49;00m];$
    35	[37m{$ENDIF}[39;49;00m$
    36	  EOL = sLineBreak;$
    37	  MaxCard = [36mHigh[39;49;00m([36mCardinal[39;49;00m);$
    38	  AllChars = [[33m#0[39;49;00m..[33m#255[39;49;00m];$
    39	  Alphabetical = [[33m'[39;49;00m[33mA[39;49;00m[33m'[39;49;00m..[33m'[39;49;00m[33mZ[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33ma[39;49;00m[33m'[39;49;00m..[33m'[39;49;00m[33mz[39;49;00m[33m'[39;49;00m];$
    40	  DecimalChars = [[33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m..[33m'[39;49;00m[33m9[39;49;00m[33m'[39;49;00m];$
    41	  AlphaNumerical = Alphabetical + DecimalChars;$
    42	  StrangeChars = [[33m#0[39;49;00m..[33m#31[39;49;00m, [33m#127[39;49;00m, [33m#129[39;49;00m, [33m#141[39;49;00m..[33m#144[39;49;00m, [33m#157[39;49;00m, [33m#158[39;49;00m];$
    43	$
    44	  HexadecimalChars = DecimalChars + [[33m'[39;49;00m[33mA[39;49;00m[33m'[39;49;00m..[33m'[39;49;00m[33mF[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33ma[39;49;00m[33m'[39;49;00m..[33m'[39;49;00m[33mf[39;49;00m[33m'[39;49;00m];$
    45	  OctalChars = [[33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m..[33m'[39;49;00m[33m7[39;49;00m[33m'[39;49;00m];$
    46	  BinaryChars = [[33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33m1[39;49;00m[33m'[39;49;00m];$
    47	$
    48	  QuoteChars = [[33m'[39;49;00m[33m''[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33m"[39;49;00m[33m'[39;49;00m];$
    49	  WildCards = [[33m'[39;49;00m[33m*[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33m?[39;49;00m[33m'[39;49;00m];$
    50	  FileNameEnemies = WildCards + [[33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33m/[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33m:[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33m<[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33m>[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33m|[39;49;00m[33m'[39;49;00m];$
    51	$
    52	  HexChar: [34marray[39;49;00m[THex] [34mof[39;49;00m [36mChar[39;49;00m = ($
    53	    [33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m1[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m2[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m3[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m4[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m5[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m6[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m7[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m8[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m9[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mA[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mB[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mC[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mD[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mE[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mF[39;49;00m[33m'[39;49;00m);$
    54	  LowerHexChar: [34marray[39;49;00m[THex] [34mof[39;49;00m [36mChar[39;49;00m = ($
    55	    [33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m1[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m2[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m3[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m4[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m5[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m6[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m7[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m8[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m9[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33ma[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mb[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mc[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33md[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33me[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mf[39;49;00m[33m'[39;49;00m);$
    56	  BaseNChar: [34marray[39;49;00m[TBaseN] [34mof[39;49;00m [36mChar[39;49;00m = ($
    57	    [33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m1[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m2[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m3[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m4[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m5[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m6[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m7[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m8[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m9[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mA[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mB[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mC[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mD[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mE[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mF[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mG[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mH[39;49;00m[33m'[39;49;00m,$
    58	    [33m'[39;49;00m[33mI[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mJ[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mK[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mL[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mM[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mN[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mO[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mP[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mQ[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mR[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mS[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mT[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mU[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mV[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mW[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mX[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mY[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mZ[39;49;00m[33m'[39;49;00m);$
    59	$
    60	  cYcnusOverlayColor = [34m$050001[39;49;00m;$
    61	$
    62	  faFindEveryFile = faReadOnly + faHidden + faSysFile + faArchive;$
    63	$
    64	  platWin9x = [VER_PLATFORM_WIN32s, VER_PLATFORM_WIN32_WINDOWS];$
    65	$
    66	$
    67	[37m{ Debugging }[39;49;00m$
    68	[34mprocedure[39;49;00m [32mClearReport[39;49;00m([34mconst[39;49;00m ReportName: [34mstring[39;49;00m);$
    69	[34mprocedure[39;49;00m [32mReport[39;49;00m([34mconst[39;49;00m ReportName, Text: [34mstring[39;49;00m);$
    70	[34mprocedure[39;49;00m [32mReportFmt[39;49;00m([34mconst[39;49;00m ReportName, Fmt: [34mstring[39;49;00m; [34mconst[39;49;00m Args: [34marray[39;49;00m [34mof[39;49;00m [34mconst[39;49;00m);$
    71	$
    72	[37m{ Params }[39;49;00m$
    73	[34mprocedure[39;49;00m [32mGetParams[39;49;00m(Strings: TStrings); overload;$
    74	[34mfunction[39;49;00m [32mGetParams[39;49;00m([34mconst[39;49;00m Separator: [34mstring[39;49;00m = [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m; overload;$
    75	$
    76	[34mfunction[39;49;00m [32mParamNum[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [36mInteger[39;49;00m;$
    77	[34mfunction[39;49;00m [32mParamPrefixNum[39;49;00m([34mconst[39;49;00m Prefix: [34mstring[39;49;00m): [36mInteger[39;49;00m;$
    78	[34mfunction[39;49;00m [32mParam[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
    79	[34mfunction[39;49;00m [32mParamPrefix[39;49;00m([34mconst[39;49;00m Prefix: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
    80	$
    81	[34mfunction[39;49;00m [32mSwitch[39;49;00m([34mconst[39;49;00m Switch: [34mstring[39;49;00m; [34mconst[39;49;00m PrefixChars: TCharSet = SwitchChars;$
    82	  IgnoreCase: [36mBoolean[39;49;00m = [34mTrue[39;49;00m): [36mBoolean[39;49;00m;$
    83	[34mfunction[39;49;00m [32mGetParam[39;49;00m([34mconst[39;49;00m Prefix: [34mstring[39;49;00m = [33m'[39;49;00m[33m'[39;49;00m; [34mconst[39;49;00m [34mDefault[39;49;00m: [34mstring[39;49;00m = [33m'[39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;$
    84	$
    85	[37m{ Dirs & UserName}[39;49;00m$
    86	[34mfunction[39;49;00m [32mGetMyDir[39;49;00m(FullPath: [36mBoolean[39;49;00m = [34mFalse[39;49;00m): [34mstring[39;49;00m;$
    87	[34mfunction[39;49;00m [32mWinDir[39;49;00m: [34mstring[39;49;00m;$
    88	[34mfunction[39;49;00m [32mSysDir[39;49;00m: [34mstring[39;49;00m;$
    89	[34mfunction[39;49;00m [32mUserName[39;49;00m: [34mstring[39;49;00m;$
    90	$
    91	[37m{ Strings & Chars}[39;49;00m$
    92	[34mfunction[39;49;00m [32mFirstChar[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [36mChar[39;49;00m;$
    93	[34mfunction[39;49;00m [32mLastChar[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [36mChar[39;49;00m;$
    94	$
    95	[34mfunction[39;49;00m [32mCharPos[39;49;00m(C: [36mChar[39;49;00m; [34mconst[39;49;00m S: [34mstring[39;49;00m; Offset: [36mInteger[39;49;00m = [34m1[39;49;00m): [36mInteger[39;49;00m; overload;$
    96	[34mfunction[39;49;00m [32mCharPos[39;49;00m(C: TCharSet; [34mconst[39;49;00m S: [34mstring[39;49;00m; Offset: [36mInteger[39;49;00m = [34m1[39;49;00m): [36mInteger[39;49;00m; overload;$
    97	[34mfunction[39;49;00m [32mCharPosR[39;49;00m(C: [36mChar[39;49;00m; [34mconst[39;49;00m S: [34mstring[39;49;00m; Offset: [36mInteger[39;49;00m = -[34m1[39;49;00m): [36mInteger[39;49;00m;$
    98	[34mfunction[39;49;00m [32mPosEx[39;49;00m([34mconst[39;49;00m SubStr, S: [34mstring[39;49;00m; Offset: [36mInteger[39;49;00m = [34m1[39;49;00m): [36mInteger[39;49;00m;$
    99	[34mfunction[39;49;00m [32mPosExText[39;49;00m([34mconst[39;49;00m SubStr, S: [34mstring[39;49;00m; Offset: [36mInteger[39;49;00m = [34m1[39;49;00m): [36mInteger[39;49;00m;$
   100	[34mfunction[39;49;00m [32mPosExAnsiText[39;49;00m([34mconst[39;49;00m SubStr, S: [34mstring[39;49;00m; Offset: [36mInteger[39;49;00m = [34m1[39;49;00m): [36mInteger[39;49;00m;$
   101	$
   102	[34mfunction[39;49;00m [32mUntilChar[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Brake: [36mChar[39;49;00m): [34mstring[39;49;00m; overload;$
   103	[34mfunction[39;49;00m [32mUntilChar[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Brake: TCharSet): [34mstring[39;49;00m; overload;$
   104	[34mfunction[39;49;00m [32mUntilLastChar[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Brake: [36mChar[39;49;00m;$
   105	  IgnoreNoBrake: [36mBoolean[39;49;00m = [34mTrue[39;49;00m): [34mstring[39;49;00m;$
   106	$
   107	[34mfunction[39;49;00m [32mFromChar[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Brake: [36mChar[39;49;00m): [34mstring[39;49;00m; overload;$
   108	[34mfunction[39;49;00m [32mFromChar[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Brake: TCharSet): [34mstring[39;49;00m; overload;$
   109	[34mfunction[39;49;00m [32mFromLastChar[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Brake: [36mChar[39;49;00m;$
   110	  IgnoreNoBrake: [36mBoolean[39;49;00m = [34mFalse[39;49;00m): [34mstring[39;49;00m;$
   111	$
   112	[34mfunction[39;49;00m [32mBetweenChars[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Start, Finish: [36mChar[39;49;00m;$
   113	  Inclusive: [36mBoolean[39;49;00m = [34mFalse[39;49;00m): [34mstring[39;49;00m;$
   114	$
   115	[34mfunction[39;49;00m [32mUntilStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Brake: [34mstring[39;49;00m): [34mstring[39;49;00m;$
   116	[34mfunction[39;49;00m [32mFromStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Brake: [34mstring[39;49;00m): [34mstring[39;49;00m;$
   117	$
   118	[34mfunction[39;49;00m [32mStringWrap[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Width: [36mInteger[39;49;00m; [34mconst[39;49;00m LineEnd: [34mstring[39;49;00m = EOL): [34mstring[39;49;00m;$
   119	$
   120	[37m{ Splitting & Combining }[39;49;00m$
   121	[34mfunction[39;49;00m [32mSplit[39;49;00m([34mconst[39;49;00m S, Separator: [34mstring[39;49;00m; IgnoreMultiSep: [36mBoolean[39;49;00m = [34mTrue[39;49;00m;$
   122	  MinCount: [36mInteger[39;49;00m = [34m0[39;49;00m): TStrA; overload;$
   123	[34mprocedure[39;49;00m [32mSplit[39;49;00m([34mconst[39;49;00m S, Separator: [34mstring[39;49;00m; Strings: TStrings;$
   124	  IgnoreMultiSep: [36mBoolean[39;49;00m = [34mTrue[39;49;00m); overload;$
   125	[34mfunction[39;49;00m [32mSplit[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Separators: TCharSet;$
   126	  IgnoreMultiSep: [36mBoolean[39;49;00m = [34mTrue[39;49;00m; MinCount: [36mInteger[39;49;00m = [34m0[39;49;00m): TStrA; overload;$
   127	$
   128	[34mprocedure[39;49;00m [32mTileStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; BrakeStart: [36mInteger[39;49;00m; BrakeEnd: [36mInteger[39;49;00m;$
   129	  out Left, Right: [34mstring[39;49;00m);$
   130	$
   131	[34mfunction[39;49;00m [32mJoin[39;49;00m(Strings: TStrings; Separator: [34mstring[39;49;00m = [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m; overload;$
   132	[34mfunction[39;49;00m [32mJoin[39;49;00m(StrA: TStrA; Separator: [34mstring[39;49;00m = [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m; overload;$
   133	$
   134	[34mfunction[39;49;00m [32mMulStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Count: [36mInteger[39;49;00m): [34mstring[39;49;00m;$
   135	$
   136	[37m{ Strings ausrichten }[39;49;00m$
   137	[34mfunction[39;49;00m [32mAlignR[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Width: [36mInteger[39;49;00m; Filler: [36mChar[39;49;00m = [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;$
   138	[34mfunction[39;49;00m [32mMaxStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; MaxLen: [36mInteger[39;49;00m): [34mstring[39;49;00m;$
   139	$
   140	[37m{ Stringing }[39;49;00m$
   141	[34mfunction[39;49;00m [32mTrimAll[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [34mstring[39;49;00m;$
   142	$
   143	[34mfunction[39;49;00m [32mControlChar[39;49;00m(C: [36mChar[39;49;00m): [36mBoolean[39;49;00m;$
   144	[34mfunction[39;49;00m [32mFriendlyChar[39;49;00m(C: [36mChar[39;49;00m): [36mChar[39;49;00m;$
   145	$
   146	[34mfunction[39;49;00m [32mFriendlyStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [34mstring[39;49;00m; overload;$
   147	[34mfunction[39;49;00m [32mFriendlyStr[39;49;00m(a: TByteA): [34mstring[39;49;00m; overload;$
   148	$
   149	[34mfunction[39;49;00m [32mQuote[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Quoter: [36mChar[39;49;00m = [33m'[39;49;00m[33m"[39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;$
   150	[34mfunction[39;49;00m [32mUnQuote[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [34mstring[39;49;00m;$
   151	[34mfunction[39;49;00m [32mDeQuote[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [34mstring[39;49;00m;$
   152	$
   153	[34mfunction[39;49;00m [32mStrNumerus[39;49;00m([34mconst[39;49;00m Value: [36mInteger[39;49;00m; [34mconst[39;49;00m Singular, Plural: [34mstring[39;49;00m;$
   154	  [34mconst[39;49;00m Zero: [34mstring[39;49;00m = [33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;$
   155	$
   156	[34mfunction[39;49;00m [32mMakeStr[39;49;00m([34mconst[39;49;00m Items: [34marray[39;49;00m [34mof[39;49;00m [34mconst[39;49;00m; Separator: [34mstring[39;49;00m = [33m'[39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;$
   157	[34mprocedure[39;49;00m [32mShowText[39;49;00m([34mconst[39;49;00m Items: [34marray[39;49;00m [34mof[39;49;00m [34mconst[39;49;00m; Separator: [34mstring[39;49;00m = [33m'[39;49;00m[33m'[39;49;00m);$
   158	$
   159	[37m{ Delete }[39;49;00m$
   160	[34mfunction[39;49;00m [32mDeleteChars[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; C: [36mChar[39;49;00m): [34mstring[39;49;00m; overload;$
   161	[34mfunction[39;49;00m [32mDeleteChars[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; C: TCharSet): [34mstring[39;49;00m; overload;$
   162	[34mfunction[39;49;00m [32mExtractChars[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; C: TCharSet): [34mstring[39;49;00m;$
   163	$
   164	[37m{ Find }[39;49;00m$
   165	[34mfunction[39;49;00m [32mCharCount[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; C: [36mChar[39;49;00m): [36mInteger[39;49;00m;$
   166	$
   167	[34mfunction[39;49;00m [32mCharIn[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; C: [36mChar[39;49;00m): [36mBoolean[39;49;00m; overload;$
   168	[34mfunction[39;49;00m [32mCharIn[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; C: TCharSet): [36mBoolean[39;49;00m; overload;$
   169	$
   170	[34mfunction[39;49;00m [32mStrAtPos[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; [36mPos[39;49;00m: [36mInteger[39;49;00m; [34mconst[39;49;00m [36mStr[39;49;00m: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
   171	[34mfunction[39;49;00m [32mStrAtBegin[39;49;00m([34mconst[39;49;00m S, [36mStr[39;49;00m: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
   172	[34mfunction[39;49;00m [32mStrIn[39;49;00m([34mconst[39;49;00m S, SubStr: [34mstring[39;49;00m): [36mBoolean[39;49;00m; overload;$
   173	[34mfunction[39;49;00m [32mStrIn[39;49;00m(A: TStrA; [34mconst[39;49;00m S: [34mstring[39;49;00m): [36mBoolean[39;49;00m; overload;$
   174	[34mfunction[39;49;00m [32mStrIn[39;49;00m(SL: TStrings; [34mconst[39;49;00m S: [34mstring[39;49;00m): [36mBoolean[39;49;00m; overload;$
   175	[34mfunction[39;49;00m [32mStrIndex[39;49;00m(A: TStrA; [34mconst[39;49;00m S: [34mstring[39;49;00m): [36mInteger[39;49;00m; overload;$
   176	[34mfunction[39;49;00m [32mStrIndex[39;49;00m(SL: TStrings; [34mconst[39;49;00m S: [34mstring[39;49;00m): [36mInteger[39;49;00m; overload;$
   177	$
   178	[34mfunction[39;49;00m [32mTextAtPos[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; [36mPos[39;49;00m: [36mInteger[39;49;00m; [34mconst[39;49;00m Text: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
   179	[34mfunction[39;49;00m [32mTextAtBegin[39;49;00m([34mconst[39;49;00m S, Text: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
   180	[34mfunction[39;49;00m [32mTextIn[39;49;00m([34mconst[39;49;00m S, Text: [34mstring[39;49;00m): [36mBoolean[39;49;00m; overload;$
   181	[34mfunction[39;49;00m [32mTextIn[39;49;00m(A: TStrA; [34mconst[39;49;00m Text: [34mstring[39;49;00m): [36mBoolean[39;49;00m; overload;$
   182	[34mfunction[39;49;00m [32mTextIn[39;49;00m(SL: TStrings; [34mconst[39;49;00m Text: [34mstring[39;49;00m): [36mBoolean[39;49;00m; overload;$
   183	[34mfunction[39;49;00m [32mTextIndex[39;49;00m(A: TStrA; [34mconst[39;49;00m Text: [34mstring[39;49;00m): [36mInteger[39;49;00m; overload;$
   184	[34mfunction[39;49;00m [32mTextIndex[39;49;00m(SL: TStrings; [34mconst[39;49;00m Text: [34mstring[39;49;00m): [36mInteger[39;49;00m; overload;$
   185	$
   186	[37m{ Replace }[39;49;00m$
   187	[34mfunction[39;49;00m [32mReplaceChars[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Old, [34mNew[39;49;00m: [36mChar[39;49;00m): [34mstring[39;49;00m; overload;$
   188	[34mfunction[39;49;00m [32mReplaceChars[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Old: TCharSet; [34mNew[39;49;00m: [36mChar[39;49;00m): [34mstring[39;49;00m; overload;$
   189	$
   190	[34mfunction[39;49;00m [32mReplace[39;49;00m([34mconst[39;49;00m S, Old, [34mNew[39;49;00m: [34mstring[39;49;00m): [34mstring[39;49;00m;$
   191	$
   192	[37m{ TStrings }[39;49;00m$
   193	[34mfunction[39;49;00m [32mSLOfFile[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m): TStringList;$
   194	[34mfunction[39;49;00m [32mContainsEmptyLines[39;49;00m(SL: TStrings): [36mBoolean[39;49;00m;$
   195	[34mprocedure[39;49;00m [32mDeleteEmptyLines[39;49;00m(SL: TStrings);$
   196	[34mprocedure[39;49;00m [32mDeleteCommentLines[39;49;00m(SL: TStrings; [34mconst[39;49;00m CommentSign: [34mstring[39;49;00m = [33m'[39;49;00m[33m//[39;49;00m[33m'[39;49;00m);$
   197	[34mprocedure[39;49;00m [32mWriteSL[39;49;00m(Strings: TStrings; [34mconst[39;49;00m Prefix: [34mstring[39;49;00m = [33m'[39;49;00m[33m'[39;49;00m;$
   198	  [34mconst[39;49;00m Suffix: [34mstring[39;49;00m = [33m'[39;49;00m[33m'[39;49;00m);$
   199	$
   200	[34mfunction[39;49;00m [32mFindLine[39;49;00m(SL: TStrings; [34mconst[39;49;00m S: [34mstring[39;49;00m): [36mInteger[39;49;00m;$
   201	$
   202	[34mprocedure[39;49;00m [32mQuickSortSL[39;49;00m(SL: TStringList);$
   203	$
   204	[37m{ TStrA }[39;49;00m$
   205	[34mfunction[39;49;00m [32mIncStrA[39;49;00m(StrA: TStrA): [36mInteger[39;49;00m;$
   206	$
   207	[37m{ TByteA }[39;49;00m$
   208	[34mfunction[39;49;00m [32mStrOfByteA[39;49;00m(a: TByteA): [34mstring[39;49;00m;$
   209	[34mfunction[39;49;00m [32mByteAOfStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): TByteA;$
   210	[34mfunction[39;49;00m [32mByteAOfInt[39;49;00m(i: [36mInteger[39;49;00m): TByteA;$
   211	[34mfunction[39;49;00m [32mIntOfByteA[39;49;00m(A: TByteA): [36mInteger[39;49;00m;$
   212	[34mfunction[39;49;00m [32mByteAOfHex[39;49;00m([34mconst[39;49;00m Hex: [34mstring[39;49;00m): TByteA;$
   213	$
   214	[34mfunction[39;49;00m [32mSameByteA[39;49;00m([34mconst[39;49;00m A, B: TByteA): [36mBoolean[39;49;00m;$
   215	[34mfunction[39;49;00m [32mReverse[39;49;00m(a: TByteA): TByteA;$
   216	[34mfunction[39;49;00m [32mSaveByteA[39;49;00m(Data: TByteA; [34mconst[39;49;00m FileName: [34mstring[39;49;00m; Overwrite: [36mBoolean[39;49;00m = [34mTrue[39;49;00m): [36mBoolean[39;49;00m;$
   217	[34mfunction[39;49;00m [32mLoadByteA[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m): TByteA;$
   218	$
   219	[34mfunction[39;49;00m [32mEndian[39;49;00m(i: [36mInteger[39;49;00m): [36mInteger[39;49;00m;$
   220	$
   221	[37m{ Files }[39;49;00m$
   222	[34mfunction[39;49;00m [32mSizeOfFile[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m): [36mInteger[39;49;00m;$
   223	[34mfunction[39;49;00m [32mFileEx[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m; AllowFolders: [36mBoolean[39;49;00m = [34mFalse[39;49;00m): [36mBoolean[39;49;00m;$
   224	[34mfunction[39;49;00m [32mLWPSolve[39;49;00m([34mconst[39;49;00m Dir: [34mstring[39;49;00m): [34mstring[39;49;00m;$
   225	[34mfunction[39;49;00m [32mLWPSlash[39;49;00m([34mconst[39;49;00m Dir: [34mstring[39;49;00m): [34mstring[39;49;00m;$
   226	$
   227	[34mfunction[39;49;00m [32mExtractDrive[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m): [34mstring[39;49;00m;$
   228	[34mfunction[39;49;00m [32mExtractPath[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m): [34mstring[39;49;00m;$
   229	[34mfunction[39;49;00m [32mExtractPrefix[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m): [34mstring[39;49;00m;$
   230	[34mfunction[39;49;00m [32mExtractSuffix[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m): [34mstring[39;49;00m;$
   231	$
   232	[34mfunction[39;49;00m [32mIsValidFileName[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
   233	[34mfunction[39;49;00m [32mMakeValidFileName[39;49;00m(FileName: [34mstring[39;49;00m; [34mconst[39;49;00m [34mDefault[39;49;00m: [34mstring[39;49;00m = [33m'[39;49;00m[33mFile[39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;$
   234	$
   235	[37m{ Converting }[39;49;00m$
   236	[34mfunction[39;49;00m [32mIsValidInteger[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
   237	[34mfunction[39;49;00m [32mIsValidCardinal[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
   238	$
   239	[34mfunction[39;49;00m [32mStrOfBool[39;49;00m(flag: [36mBoolean[39;49;00m; [34mconst[39;49;00m TrueStr: [34mstring[39;49;00m = [33m'[39;49;00m[33mTrue[39;49;00m[33m'[39;49;00m;$
   240	  [34mconst[39;49;00m FalseStr: [34mstring[39;49;00m = [33m'[39;49;00m[33mFalse[39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;$
   241	[34mfunction[39;49;00m [32mStrOfInt[39;49;00m(i: [36mInteger[39;49;00m): [34mstring[39;49;00m;$
   242	[34mfunction[39;49;00m [32mCardOfStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [36mCardinal[39;49;00m;$
   243	$
   244	[34mfunction[39;49;00m [32mHexOrd[39;49;00m(Hex: [36mChar[39;49;00m): THex;$
   245	[34mfunction[39;49;00m [32mByteOfHex[39;49;00m(Hex: THexByteStr): [36mByte[39;49;00m;$
   246	$
   247	[34mfunction[39;49;00m [32mDecOfHex[39;49;00m([34mconst[39;49;00m Hex: [34mstring[39;49;00m): [34mstring[39;49;00m;$
   248	[34mfunction[39;49;00m [32mHexOfByte[39;49;00m(b: [36mByte[39;49;00m): THexByteStr;$
   249	[34mfunction[39;49;00m [32mHexOfCard[39;49;00m(i: [36mCardinal[39;49;00m): [34mstring[39;49;00m; overload;$
   250	[34mfunction[39;49;00m [32mHexOfCard[39;49;00m(i: [36mCardinal[39;49;00m; Digits: [36mInteger[39;49;00m): [34mstring[39;49;00m; overload;$
   251	$
   252	[34mfunction[39;49;00m [32mPascalHexArray[39;49;00m(a: TByteA; [34mName[39;49;00m: [34mstring[39;49;00m): [34mstring[39;49;00m;$
   253	$
   254	[34mfunction[39;49;00m [32mHexOfByteA[39;49;00m(a: TByteA; Blocks: [36mInteger[39;49;00m = [34m1[39;49;00m;$
   255	  [34mconst[39;49;00m Splitter: [34mstring[39;49;00m = [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;$
   256	[34mfunction[39;49;00m [32mBinOfByteA[39;49;00m(a: TByteA; Blocks: [36mInteger[39;49;00m = [34m4[39;49;00m;$
   257	  [34mconst[39;49;00m Splitter: [34mstring[39;49;00m = [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;$
   258	$
   259	[34mfunction[39;49;00m [32mCardOfHex[39;49;00m(Hex: [34mstring[39;49;00m): [36mCardinal[39;49;00m;$
   260	[34mfunction[39;49;00m [32mIntOfBin[39;49;00m(Bin: [34mstring[39;49;00m): [36mCardinal[39;49;00m;$
   261	$
   262	[34mfunction[39;49;00m [32mBinOfIntFill[39;49;00m(n: [36mcardinal[39;49;00m; MinCount: [36mInteger[39;49;00m = [34m8[39;49;00m): [34mstring[39;49;00m;$
   263	[34mfunction[39;49;00m [32mBinOfInt[39;49;00m(n: [36mcardinal[39;49;00m): [34mstring[39;49;00m;$
   264	$
   265	[34mfunction[39;49;00m [32mBaseNOfInt[39;49;00m(I: [36mCardinal[39;49;00m; B: TBaseN): [34mstring[39;49;00m;$
   266	[34mfunction[39;49;00m [32mIntOfBaseN[39;49;00m(V: [34mstring[39;49;00m; B: TBaseN): [36mCardinal[39;49;00m;$
   267	$
   268	[37m{ Ranges }[39;49;00m$
   269	[34mfunction[39;49;00m [32mKeepIn[39;49;00m(i, Bottom, Top: [36mVariant[39;49;00m): [36mVariant[39;49;00m;$
   270	[34mfunction[39;49;00m [32mInRange[39;49;00m(Value, Bottom, Top: [36mVariant[39;49;00m): [36mBoolean[39;49;00m;$
   271	[34mfunction[39;49;00m [32mInStrictRange[39;49;00m(Value, Bottom, Top: [36mVariant[39;49;00m): [36mBoolean[39;49;00m;$
   272	[34mfunction[39;49;00m [32mMin[39;49;00m([34mconst[39;49;00m A, B: [36mInteger[39;49;00m): [36mInteger[39;49;00m; overload;$
   273	[34mfunction[39;49;00m [32mMin[39;49;00m([34mconst[39;49;00m A: TIntA): [36mInteger[39;49;00m; overload;$
   274	[34mfunction[39;49;00m [32mMax[39;49;00m([34mconst[39;49;00m A, B: [36mInteger[39;49;00m): [36mInteger[39;49;00m; overload;$
   275	[34mfunction[39;49;00m [32mMax[39;49;00m([34mconst[39;49;00m A: TIntA): [36mInteger[39;49;00m; overload;$
   276	$
   277	[34mconst[39;49;00m$
   278	  RangesSeparator = [33m'[39;49;00m[33m,[39;49;00m[33m'[39;49;00m;$
   279	  RangeInnerSeparator = [33m'[39;49;00m[33m-[39;49;00m[33m'[39;49;00m;$
   280	  RangeInfinite = [33m'[39;49;00m[33m*[39;49;00m[33m'[39;49;00m;$
   281	  RangeSpecialChars = [RangesSeparator, RangeInnerSeparator, RangeInfinite];$
   282	$
   283	[34mfunction[39;49;00m [32mRangesOfStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): TRanges;$
   284	[34mfunction[39;49;00m [32mInRanges[39;49;00m(Ranges: TRanges; TestValue: [36mCardinal[39;49;00m): [36mBoolean[39;49;00m;$
   285	$
   286	[34mfunction[39;49;00m [32mSuccess[39;49;00m(Res: [36mInteger[39;49;00m; ResultOnSuccess: [36mInteger[39;49;00m = ERROR_SUCCESS): [36mBoolean[39;49;00m;$
   287	[34mfunction[39;49;00m [32mFailure[39;49;00m(Res: [36mInteger[39;49;00m; ResultOnSuccess: [36mInteger[39;49;00m = ERROR_SUCCESS): [36mBoolean[39;49;00m;$
   288	$
   289	[34mfunction[39;49;00m [32mExpandString[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [34mstring[39;49;00m;$
   290	$
   291	[37m{ Files }[39;49;00m$
   292	[34mprocedure[39;49;00m [32mDeleteFiles[39;49;00m([34mconst[39;49;00m Mask: [34mstring[39;49;00m; ScanSubDirs: [36mBoolean[39;49;00m = [34mTrue[39;49;00m;$
   293	  Attributes: [36mInteger[39;49;00m = faFindEveryFile);$
   294	[34mprocedure[39;49;00m [32mFileNew[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m);$
   295	[34mfunction[39;49;00m [32mDateTimeOfFileTime[39;49;00m([34mconst[39;49;00m FileTime: TFileTime): [36mTDateTime[39;49;00m;$
   296	$
   297	[37m{ FileNames }[39;49;00m$
   298	[34mfunction[39;49;00m [32mGetFileNew[39;49;00m(FileName: [34mstring[39;49;00m; NoFloppyDrives: [36mBoolean[39;49;00m = [34mTrue[39;49;00m): [34mstring[39;49;00m;$
   299	$
   300	[37m{ Finding Files }[39;49;00m$
   301	[34mfunction[39;49;00m [32mFindAll[39;49;00m(Strings: TStrings; [34mconst[39;49;00m Mask: [34mstring[39;49;00m;$
   302	  ScanSubDirs: [36mBoolean[39;49;00m = [34mTrue[39;49;00m; Attributes: [36mInteger[39;49;00m = faFindEveryFile;$
   303	  FileReturn: TFileNameFunc = [34mnil[39;49;00m): [36mBoolean[39;49;00m;$
   304	[34mfunction[39;49;00m [32mFindAllFirst[39;49;00m([34mconst[39;49;00m Mask: [34mstring[39;49;00m; ScanSubDirs: [36mBoolean[39;49;00m = [34mTrue[39;49;00m;$
   305	  Attributes: [36mInteger[39;49;00m = faFindEveryFile): [34mstring[39;49;00m;$
   306	$
   307	[34mfunction[39;49;00m [32mFullOSInfo[39;49;00m: [34mstring[39;49;00m;$
   308	[34mfunction[39;49;00m [32mWin32PlatformStr[39;49;00m: [34mstring[39;49;00m;$
   309	[34mfunction[39;49;00m [32mWin9x[39;49;00m: [36mBoolean[39;49;00m;$
   310	[34mfunction[39;49;00m [32mWinNT[39;49;00m: [36mBoolean[39;49;00m;$
   311	[34mfunction[39;49;00m [32mWin2000[39;49;00m: [36mBoolean[39;49;00m;$
   312	[34mfunction[39;49;00m [32mWinXP[39;49;00m: [36mBoolean[39;49;00m;$
   313	$
   314	[34mvar[39;49;00m$
   315	  MyDir: [34mstring[39;49;00m = [33m'[39;49;00m[33m'[39;49;00m;$
   316	  LastSuccessRes: [36mInteger[39;49;00m = [34m0[39;49;00m;$
   317	  $
   318	[37m{ Backward compatibility }[39;49;00m$
   319	[37m{$IFNDEF VER130}[39;49;00m$
   320	[34mfunction[39;49;00m [32mSameText[39;49;00m([34mconst[39;49;00m S1, S2: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
   321	[37m{$ENDIF}[39;49;00m$
   322	$
   323	[34mimplementation[39;49;00m$
   324	[37m{$IFNDEF VER140}[39;49;00m$
   325	[34muses[39;49;00m FileCtrl;$
   326	[37m{$ENDIF}[39;49;00m$
   327	$
   328	[37m{$IFNDEF VER130}[39;49;00m$
   329	[34mfunction[39;49;00m [32mSameText[39;49;00m([34mconst[39;49;00m S1, S2: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
   330	[34mbegin[39;49;00m$
   331	  [36mResult[39;49;00m := [36mCompareText[39;49;00m(S1, S2) = [34m0[39;49;00m;$
   332	[34mend[39;49;00m;$
   333	[37m{$ENDIF}[39;49;00m$
   334	$
   335	[34mprocedure[39;49;00m [32mReport[39;49;00m([34mconst[39;49;00m ReportName, Text: [34mstring[39;49;00m);$
   336	[34mvar[39;49;00m$
   337	  F: [36mTextFile[39;49;00m;$
   338	  FileName: [34mstring[39;49;00m;$
   339	[34mbegin[39;49;00m$
   340	  FileName := MyDir + ReportName + [33m'[39;49;00m[33m.rep[39;49;00m[33m'[39;49;00m;$
   341	  Assign(F, FileName);$
   342	  [34mtry[39;49;00m$
   343	    [34mif[39;49;00m [34mnot[39;49;00m [36mFileExists[39;49;00m(FileName) [34mthen[39;49;00m$
   344	      [36mRewrite[39;49;00m(F)$
   345	    [34melse[39;49;00m$
   346	      [36mAppend[39;49;00m(F);$
   347	    [36mWriteLn[39;49;00m(F, Text);$
   348	  [34mfinally[39;49;00m$
   349	    [36mClose[39;49;00m(F);$
   350	  [34mend[39;49;00m;$
   351	[34mend[39;49;00m;$
   352	$
   353	[34mprocedure[39;49;00m [32mClearReport[39;49;00m([34mconst[39;49;00m ReportName: [34mstring[39;49;00m);$
   354	[34mvar[39;49;00m$
   355	  FileName: [34mstring[39;49;00m;$
   356	[34mbegin[39;49;00m$
   357	  FileName := MyDir + ReportName + [33m'[39;49;00m[33m.rep[39;49;00m[33m'[39;49;00m;$
   358	  [36mDeleteFile[39;49;00m(FileName);$
   359	[34mend[39;49;00m;$
   360	$
   361	[34mprocedure[39;49;00m [32mReportFmt[39;49;00m([34mconst[39;49;00m ReportName, Fmt: [34mstring[39;49;00m; [34mconst[39;49;00m Args: [34marray[39;49;00m [34mof[39;49;00m [34mconst[39;49;00m);$
   362	[34mbegin[39;49;00m$
   363	  Report(ReportName, [36mFormat[39;49;00m(Fmt, Args));$
   364	[34mend[39;49;00m;$
   365	$
   366	[34mprocedure[39;49;00m [32mGetParams[39;49;00m(Strings: TStrings);$
   367	[34mvar[39;49;00m$
   368	  P: [36mPChar[39;49;00m;$
   369	  Param: [34mstring[39;49;00m;$
   370	$
   371	  [34mfunction[39;49;00m [32mGetParamStr[39;49;00m([34mvar[39;49;00m P: [36mPChar[39;49;00m; [34mvar[39;49;00m Param: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
   372	  [34mvar[39;49;00m$
   373	    Quoted: [36mBoolean[39;49;00m;$
   374	  [34mbegin[39;49;00m$
   375	    Param := [33m'[39;49;00m[33m'[39;49;00m;$
   376	$
   377	    [34mrepeat[39;49;00m$
   378	      [34mwhile[39;49;00m (P[[34m0[39;49;00m] <> [33m#0[39;49;00m) [34mand[39;49;00m (P[[34m0[39;49;00m] <= [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m) [34mdo[39;49;00m$
   379	        [36mInc[39;49;00m(P);$
   380	$
   381	      Quoted := [34mFalse[39;49;00m;$
   382	      [34mwhile[39;49;00m P[[34m0[39;49;00m] <> [33m#0[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m$
   383	        [34mif[39;49;00m P[[34m0[39;49;00m] = [33m'[39;49;00m[33m"[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m$
   384	          Quoted := [34mnot[39;49;00m Quoted;$
   385	          [36mInc[39;49;00m(P);$
   386	        [34mContinue[39;49;00m; [34mend[39;49;00m;$
   387	        [34mif[39;49;00m (P[[34m0[39;49;00m] <= [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m) [34mand[39;49;00m [34mnot[39;49;00m Quoted [34mthen[39;49;00m$
   388	          [34mBreak[39;49;00m;$
   389	        Param := Param + P[[34m0[39;49;00m];$
   390	        [36mInc[39;49;00m(P);$
   391	      [34mend[39;49;00m;$
   392	    [34muntil[39;49;00m (Param <> [33m'[39;49;00m[33m'[39;49;00m) [34mor[39;49;00m (P[[34m0[39;49;00m] = [33m#0[39;49;00m);$
   393	$
   394	    [36mResult[39;49;00m := Param <> [33m'[39;49;00m[33m'[39;49;00m;$
   395	  [34mend[39;49;00m;$
   396	$
   397	[34mbegin[39;49;00m$
   398	  Strings.Clear;$
   399	  P := GetCommandLine;$
   400	  GetParamStr(P, Param);$
   401	  [34mwhile[39;49;00m GetParamStr(P, Param) [34mdo[39;49;00m$
   402	    Strings.Add(Param);$
   403	[34mend[39;49;00m;$
   404	$
   405	[34mfunction[39;49;00m [32mGetParams[39;49;00m([34mconst[39;49;00m Separator: [34mstring[39;49;00m = [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;$
   406	[34mvar[39;49;00m$
   407	  SL: TStringList;$
   408	[34mbegin[39;49;00m$
   409	  SL := TStringList.Create;$
   410	  GetParams(SL);$
   411	  [36mResult[39;49;00m := Join(SL, Separator);$
   412	  SL.Free;$
   413	[34mend[39;49;00m;$
   414	$
   415	[34mfunction[39;49;00m [32mSwitch[39;49;00m([34mconst[39;49;00m Switch: [34mstring[39;49;00m; [34mconst[39;49;00m PrefixChars: TCharSet = SwitchChars;$
   416	  IgnoreCase: [36mBoolean[39;49;00m = [34mTrue[39;49;00m): [36mBoolean[39;49;00m;$
   417	[37m//= SysUtils.FindCmdLineSwitch[39;49;00m$
   418	[34mvar[39;49;00m$
   419	  i: [36mInteger[39;49;00m;$
   420	  s: [34mstring[39;49;00m;$
   421	[34mbegin[39;49;00m$
   422	  [36mResult[39;49;00m := [34mTrue[39;49;00m;$
   423	$
   424	  [34mfor[39;49;00m i := [34m1[39;49;00m [34mto[39;49;00m [36mParamCount[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m$
   425	    s := [36mParamStr[39;49;00m(i);$
   426	$
   427	    [34mif[39;49;00m (s <> [33m'[39;49;00m[33m'[39;49;00m) [34mand[39;49;00m (s[[34m1[39;49;00m] [34min[39;49;00m PrefixChars) [34mthen[39;49;00m [34mbegin[39;49;00m$
   428	    [37m//i know that always s <> '', but this is saver[39;49;00m$
   429	      s := [36mCopy[39;49;00m(s, [34m2[39;49;00m, MaxInt);$
   430	      [34mif[39;49;00m (s = Switch) [34mor[39;49;00m (IgnoreCase [34mand[39;49;00m ([34m0[39;49;00m=[36mAnsiCompareText[39;49;00m(s, Switch))) [34mthen[39;49;00m$
   431	        [34mExit[39;49;00m;$
   432	    [34mend[39;49;00m;$
   433	  [34mend[39;49;00m;$
   434	$
   435	  [36mResult[39;49;00m := [34mFalse[39;49;00m;$
   436	[34mend[39;49;00m;$
   437	$
   438	[34mfunction[39;49;00m [32mParamNum[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [36mInteger[39;49;00m;$
   439	[34mbegin[39;49;00m$
   440	  [34mfor[39;49;00m [36mResult[39;49;00m := [34m1[39;49;00m [34mto[39;49;00m [36mParamCount[39;49;00m [34mdo[39;49;00m$
   441	    [34mif[39;49;00m [34m0[39;49;00m=[36mAnsiCompareText[39;49;00m([36mParamStr[39;49;00m([36mResult[39;49;00m), S) [34mthen[39;49;00m$
   442	      [34mExit[39;49;00m;$
   443	$
   444	  [36mResult[39;49;00m := [34m0[39;49;00m;$
   445	[34mend[39;49;00m;$
   446	$
   447	[34mfunction[39;49;00m [32mParamPrefixNum[39;49;00m([34mconst[39;49;00m Prefix: [34mstring[39;49;00m): [36mInteger[39;49;00m;$
   448	[34mvar[39;49;00m$
   449	  Len: [36mInteger[39;49;00m;$
   450	[34mbegin[39;49;00m$
   451	  Len := [36mLength[39;49;00m(Prefix);$
   452	  [34mfor[39;49;00m [36mResult[39;49;00m := [34m1[39;49;00m [34mto[39;49;00m [36mParamCount[39;49;00m [34mdo[39;49;00m$
   453	    [34mif[39;49;00m [34m0[39;49;00m=[36mAnsiCompareText[39;49;00m([36mCopy[39;49;00m([36mParamStr[39;49;00m([36mResult[39;49;00m), [34m1[39;49;00m, Len), Prefix) [34mthen[39;49;00m$
   454	      [34mExit[39;49;00m;$
   455	$
   456	  [36mResult[39;49;00m := [34m0[39;49;00m;$
   457	[34mend[39;49;00m;$
   458	$
   459	[34mfunction[39;49;00m [32mParam[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
   460	[34mbegin[39;49;00m$
   461	  [36mResult[39;49;00m := ParamNum(S) > [34m0[39;49;00m;$
   462	[34mend[39;49;00m;$
   463	$
   464	[34mfunction[39;49;00m [32mParamPrefix[39;49;00m([34mconst[39;49;00m Prefix: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
   465	[34mbegin[39;49;00m$
   466	  [36mResult[39;49;00m := ParamPrefixNum(Prefix) > [34m0[39;49;00m;$
   467	[34mend[39;49;00m;$
   468	$
   469	[34mfunction[39;49;00m [32mGetParam[39;49;00m([34mconst[39;49;00m Prefix: [34mstring[39;49;00m = [33m'[39;49;00m[33m'[39;49;00m; [34mconst[39;49;00m [34mDefault[39;49;00m: [34mstring[39;49;00m = [33m'[39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;$
   470	[34mvar[39;49;00m$
   471	  i: [36mInteger[39;49;00m;$
   472	[34mbegin[39;49;00m$
   473	  [36mResult[39;49;00m := [34mDefault[39;49;00m;$
   474	$
   475	  [34mif[39;49;00m Prefix = [33m'[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m$
   476	    [36mResult[39;49;00m := [36mParamStr[39;49;00m([34m1[39;49;00m);$
   477	  [34mExit[39;49;00m; [34mend[39;49;00m;$
   478	$
   479	  i := ParamPrefixNum(Prefix);$
   480	  [34mif[39;49;00m i > [34m0[39;49;00m [34mthen[39;49;00m$
   481	    [36mResult[39;49;00m := [36mCopy[39;49;00m([36mParamStr[39;49;00m(i), [36mLength[39;49;00m(Prefix) + [34m1[39;49;00m, MaxInt);$
   482	[34mend[39;49;00m;$
   483	$
   484	[34mfunction[39;49;00m [32mGetMyDir[39;49;00m(FullPath: [36mBoolean[39;49;00m = [34mFalse[39;49;00m): [34mstring[39;49;00m;$
   485	[34mvar[39;49;00m$
   486	  Buffer: [34marray[39;49;00m[[34m0[39;49;00m..[34m260[39;49;00m] [34mof[39;49;00m [36mChar[39;49;00m;$
   487	[34mbegin[39;49;00m$
   488	  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
   489	  [36mSetString[39;49;00m([36mResult[39;49;00m, Buffer, [36mGetModuleFileName[39;49;00m([34m0[39;49;00m, Buffer, [36mSizeOf[39;49;00m(Buffer)));$
   490	  [34mif[39;49;00m FullPath [34mthen[39;49;00m$
   491	    [36mResult[39;49;00m := GetFileNew([36mResult[39;49;00m);$
   492	  [36mResult[39;49;00m := ExtractPath([36mResult[39;49;00m);$
   493	[34mend[39;49;00m;$
   494	$
   495	[34mfunction[39;49;00m [32mWinDir[39;49;00m: [34mstring[39;49;00m;$
   496	[34mvar[39;49;00m$
   497	  Res: [36mPChar[39;49;00m;$
   498	[34mbegin[39;49;00m$
   499	  [36mResult[39;49;00m := [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m;$
   500	  [36mGetMem[39;49;00m(Res, MAX_PATH);$
   501	  GetWindowsDirectory(Res, MAX_PATH);$
   502	  [36mResult[39;49;00m := Res + [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m;$
   503	  [36mFreeMem[39;49;00m(Res, MAX_PATH);$
   504	[34mend[39;49;00m;$
   505	$
   506	[34mfunction[39;49;00m [32mSysDir[39;49;00m: [34mstring[39;49;00m;$
   507	[34mvar[39;49;00m$
   508	  Res: [36mPChar[39;49;00m;$
   509	[34mbegin[39;49;00m$
   510	  [36mResult[39;49;00m := [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m;$
   511	  [36mGetMem[39;49;00m(Res, MAX_PATH);$
   512	  GetSystemDirectory(Res, MAX_PATH);$
   513	  [36mResult[39;49;00m := Res + [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m;$
   514	  [36mFreeMem[39;49;00m(Res, MAX_PATH);$
   515	[34mend[39;49;00m;$
   516	$
   517	[34mfunction[39;49;00m [32mUserName[39;49;00m: [34mstring[39;49;00m;$
   518	[34mvar[39;49;00m$
   519	  Len: [36mCardinal[39;49;00m;$
   520	  Res: [36mPChar[39;49;00m;$
   521	[34mbegin[39;49;00m$
   522	  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
   523	  [36mGetMem[39;49;00m(Res, MAX_PATH);$
   524	  Len := MAX_PATH;$
   525	  GetUserName(Res, Len);$
   526	  [36mResult[39;49;00m := Res;$
   527	  [36mFreeMem[39;49;00m(Res, MAX_PATH);$
   528	[34mend[39;49;00m;$
   529	$
   530	[34mfunction[39;49;00m [32mFirstChar[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [36mChar[39;49;00m;$
   531	[34mbegin[39;49;00m$
   532	  [34mif[39;49;00m s = [33m'[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m$
   533	    [36mResult[39;49;00m := [33m#0[39;49;00m$
   534	  [34melse[39;49;00m$
   535	    [36mResult[39;49;00m := s[[34m1[39;49;00m];$
   536	[34mend[39;49;00m;$
   537	$
   538	[34mfunction[39;49;00m [32mLastChar[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [36mChar[39;49;00m;$
   539	[34mbegin[39;49;00m$
   540	  [34mif[39;49;00m s = [33m'[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m$
   541	    [36mResult[39;49;00m := [33m#0[39;49;00m$
   542	  [34melse[39;49;00m$
   543	    [36mResult[39;49;00m := s[[36mLength[39;49;00m(s)];$
   544	[34mend[39;49;00m;$
   545	$
   546	[34mfunction[39;49;00m [32mCharPos[39;49;00m(C: [36mChar[39;49;00m; [34mconst[39;49;00m S: [34mstring[39;49;00m; Offset: [36mInteger[39;49;00m = [34m1[39;49;00m): [36mInteger[39;49;00m;$
   547	[34mvar[39;49;00m$
   548	  MaxPosToSearch: [36mInteger[39;49;00m;$
   549	[34mbegin[39;49;00m$
   550	  [36mResult[39;49;00m := Offset;$
   551	  MaxPosToSearch := [36mLength[39;49;00m(S);$
   552	$
   553	  [34mwhile[39;49;00m [36mResult[39;49;00m <= MaxPosToSearch [34mdo[39;49;00m [34mbegin[39;49;00m$
   554	    [34mif[39;49;00m S[[36mResult[39;49;00m] = C [34mthen[39;49;00m$
   555	      [34mExit[39;49;00m;$
   556	    [36mInc[39;49;00m([36mResult[39;49;00m);$
   557	  [34mend[39;49;00m;$
   558	$
   559	  [36mResult[39;49;00m := [34m0[39;49;00m;$
   560	[34mend[39;49;00m;$
   561	$
   562	[34mfunction[39;49;00m [32mCharPos[39;49;00m(C: TCharSet; [34mconst[39;49;00m S: [34mstring[39;49;00m; Offset: [36mInteger[39;49;00m = [34m1[39;49;00m): [36mInteger[39;49;00m;$
   563	[34mvar[39;49;00m$
   564	  MaxPosToSearch: [36mInteger[39;49;00m;$
   565	[34mbegin[39;49;00m$
   566	  [36mResult[39;49;00m := Offset;$
   567	  MaxPosToSearch := [36mLength[39;49;00m(S);$
   568	$
   569	  [34mwhile[39;49;00m [36mResult[39;49;00m <= MaxPosToSearch [34mdo[39;49;00m [34mbegin[39;49;00m$
   570	    [34mif[39;49;00m S[[36mResult[39;49;00m] [34min[39;49;00m C [34mthen[39;49;00m$
   571	      [34mExit[39;49;00m;$
   572	    [36mInc[39;49;00m([36mResult[39;49;00m);$
   573	  [34mend[39;49;00m;$
   574	$
   575	  [36mResult[39;49;00m := [34m0[39;49;00m;$
   576	[34mend[39;49;00m;$
   577	$
   578	[34mfunction[39;49;00m [32mCharPosR[39;49;00m(C: [36mChar[39;49;00m; [34mconst[39;49;00m S: [34mstring[39;49;00m; Offset: [36mInteger[39;49;00m = -[34m1[39;49;00m): [36mInteger[39;49;00m;$
   579	[34mbegin[39;49;00m$
   580	  [34mif[39;49;00m Offset < [34m0[39;49;00m [34mthen[39;49;00m$
   581	    [36mResult[39;49;00m := [36mLength[39;49;00m(S) + [34m1[39;49;00m - Offset$
   582	  [34melse[39;49;00m$
   583	    [36mResult[39;49;00m := Offset;$
   584	  [34mif[39;49;00m [36mResult[39;49;00m > [36mLength[39;49;00m(S) [34mthen[39;49;00m$
   585	    [36mResult[39;49;00m := [36mLength[39;49;00m(S);$
   586	$
   587	  [34mwhile[39;49;00m [36mResult[39;49;00m > [34m0[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m$
   588	    [34mif[39;49;00m S[[36mResult[39;49;00m] = C [34mthen[39;49;00m$
   589	      [34mExit[39;49;00m;$
   590	    [36mDec[39;49;00m([36mResult[39;49;00m);$
   591	  [34mend[39;49;00m;$
   592	[34mend[39;49;00m;$
   593	$
   594	[34mfunction[39;49;00m [32mPosEx[39;49;00m([34mconst[39;49;00m SubStr, S: [34mstring[39;49;00m; Offset: [36mInteger[39;49;00m = [34m1[39;49;00m): [36mInteger[39;49;00m;$
   595	[34mvar[39;49;00m$
   596	  MaxPosToSearch, LenSubStr, i: [36mInteger[39;49;00m;$
   597	[34mbegin[39;49;00m$
   598	  [34mif[39;49;00m SubStr = [33m'[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m$
   599	    [36mResult[39;49;00m := [34m0[39;49;00m;$
   600	  [34mExit[39;49;00m; [34mend[39;49;00m;$
   601	$
   602	  [34mif[39;49;00m Offset < [34m1[39;49;00m [34mthen[39;49;00m$
   603	    [36mResult[39;49;00m := [34m1[39;49;00m$
   604	  [34melse[39;49;00m$
   605	    [36mResult[39;49;00m := Offset;$
   606	$
   607	  LenSubStr := [36mLength[39;49;00m(SubStr);$
   608	  MaxPosToSearch := [36mLength[39;49;00m(S) - LenSubStr + [34m1[39;49;00m;$
   609	$
   610	  [34mwhile[39;49;00m [36mResult[39;49;00m <= MaxPosToSearch [34mdo[39;49;00m [34mbegin[39;49;00m$
   611	    [34mif[39;49;00m S[[36mResult[39;49;00m] = SubStr[[34m1[39;49;00m] [34mthen[39;49;00m [34mbegin[39;49;00m$
   612	      i := [34m1[39;49;00m;$
   613	$
   614	      [34mwhile[39;49;00m (i < LenSubStr)$
   615	       [34mand[39;49;00m (S[[36mResult[39;49;00m + i] = SubStr[i + [34m1[39;49;00m]) [34mdo[39;49;00m$
   616	        [36mInc[39;49;00m(i);$
   617	$
   618	      [34mif[39;49;00m i = LenSubStr [34mthen[39;49;00m$
   619	        [34mExit[39;49;00m;$
   620	    [34mend[39;49;00m;$
   621	    [36mInc[39;49;00m([36mResult[39;49;00m);$
   622	  [34mend[39;49;00m;$
   623	$
   624	  [36mResult[39;49;00m := [34m0[39;49;00m;$
   625	[34mend[39;49;00m;$
   626	$
   627	[34mfunction[39;49;00m [32mPosExText[39;49;00m([34mconst[39;49;00m SubStr, S: [34mstring[39;49;00m; Offset: [36mInteger[39;49;00m = [34m1[39;49;00m): [36mInteger[39;49;00m;$
   628	[34mvar[39;49;00m$
   629	  MaxPosToSearch, LenSubStr, i: [36mInteger[39;49;00m;$
   630	$
   631	  [34mfunction[39;49;00m [32mSameChar[39;49;00m(a, b: [36mChar[39;49;00m): [36mBoolean[39;49;00m;$
   632	  [34mbegin[39;49;00m$
   633	    [36mResult[39;49;00m := [36mUpCase[39;49;00m(a) = [36mUpCase[39;49;00m(b)$
   634	  [34mend[39;49;00m;$
   635	$
   636	[34mbegin[39;49;00m$
   637	  [34mif[39;49;00m SubStr = [33m'[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m$
   638	    [36mResult[39;49;00m := [34m0[39;49;00m;$
   639	  [34mExit[39;49;00m; [34mend[39;49;00m;$
   640	$
   641	  [34mif[39;49;00m Offset < [34m1[39;49;00m [34mthen[39;49;00m$
   642	    [36mResult[39;49;00m := [34m1[39;49;00m$
   643	  [34melse[39;49;00m$
   644	    [36mResult[39;49;00m := Offset;$
   645	$
   646	  LenSubStr := [36mLength[39;49;00m(SubStr);$
   647	  MaxPosToSearch := [36mLength[39;49;00m(S) - LenSubStr + [34m1[39;49;00m;$
   648	$
   649	  [34mwhile[39;49;00m [36mResult[39;49;00m <= MaxPosToSearch [34mdo[39;49;00m [34mbegin[39;49;00m$
   650	    [34mif[39;49;00m SameChar(S[[36mResult[39;49;00m], SubStr[[34m1[39;49;00m]) [34mthen[39;49;00m [34mbegin[39;49;00m$
   651	      i := [34m1[39;49;00m;$
   652	$
   653	      [34mwhile[39;49;00m (i < LenSubStr)$
   654	       [34mand[39;49;00m (SameChar(S[[36mResult[39;49;00m + i], SubStr[i + [34m1[39;49;00m])) [34mdo[39;49;00m$
   655	        [36mInc[39;49;00m(i);$
   656	$
   657	      [34mif[39;49;00m i = LenSubStr [34mthen[39;49;00m$
   658	        [34mExit[39;49;00m;$
   659	    [34mend[39;49;00m;$
   660	    [36mInc[39;49;00m([36mResult[39;49;00m);$
   661	  [34mend[39;49;00m;$
   662	$
   663	  [36mResult[39;49;00m := [34m0[39;49;00m;$
   664	[34mend[39;49;00m;$
   665	$
   666	[34mfunction[39;49;00m [32mPosExAnsiText[39;49;00m([34mconst[39;49;00m SubStr, S: [34mstring[39;49;00m; Offset: [36mInteger[39;49;00m = [34m1[39;49;00m): [36mInteger[39;49;00m;$
   667	[34mvar[39;49;00m$
   668	  MaxPosToSearch, LenSubStr, i: [36mInteger[39;49;00m;$
   669	$
   670	  [34mfunction[39;49;00m [32mSameChar[39;49;00m(a, b: [36mChar[39;49;00m): [36mBoolean[39;49;00m;$
   671	  [34mbegin[39;49;00m$
   672	    [36mResult[39;49;00m := CharLower([36mPChar[39;49;00m(a)) = CharLower([36mPChar[39;49;00m(b));$
   673	  [34mend[39;49;00m;$
   674	$
   675	[34mbegin[39;49;00m$
   676	  [34mif[39;49;00m SubStr = [33m'[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m$
   677	    [36mResult[39;49;00m := [34m0[39;49;00m;$
   678	  [34mExit[39;49;00m; [34mend[39;49;00m;$
   679	$
   680	  [34mif[39;49;00m Offset < [34m1[39;49;00m [34mthen[39;49;00m$
   681	    [36mResult[39;49;00m := [34m1[39;49;00m$
   682	  [34melse[39;49;00m$
   683	    [36mResult[39;49;00m := Offset;$
   684	$
   685	  LenSubStr := [36mLength[39;49;00m(SubStr);$
   686	  MaxPosToSearch := [36mLength[39;49;00m(S) - LenSubStr + [34m1[39;49;00m;$
   687	$
   688	  [34mwhile[39;49;00m [36mResult[39;49;00m <= MaxPosToSearch [34mdo[39;49;00m [34mbegin[39;49;00m$
   689	    [34mif[39;49;00m SameChar(S[[36mResult[39;49;00m], SubStr[[34m1[39;49;00m]) [34mthen[39;49;00m [34mbegin[39;49;00m$
   690	      i := [34m1[39;49;00m;$
   691	$
   692	      [34mwhile[39;49;00m (i < LenSubStr)$
   693	       [34mand[39;49;00m (SameChar(S[[36mResult[39;49;00m + i], SubStr[i + [34m1[39;49;00m])) [34mdo[39;49;00m$
   694	        [36mInc[39;49;00m(i);$
   695	$
   696	      [34mif[39;49;00m i = LenSubStr [34mthen[39;49;00m$
   697	        [34mExit[39;49;00m;$
   698	    [34mend[39;49;00m;$
   699	    [36mInc[39;49;00m([36mResult[39;49;00m);$
   700	  [34mend[39;49;00m;$
   701	$
   702	  [36mResult[39;49;00m := [34m0[39;49;00m;$
   703	[34mend[39;49;00m;$
   704	$
   705	[34mfunction[39;49;00m [32mUntilChar[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Brake: [36mChar[39;49;00m): [34mstring[39;49;00m;$
   706	[34mvar[39;49;00m$
   707	  p: [36mInteger[39;49;00m;$
   708	[34mbegin[39;49;00m$
   709	  p := CharPos(Brake, S);$
   710	$
   711	  [34mif[39;49;00m p > [34m0[39;49;00m [34mthen[39;49;00m$
   712	    [36mResult[39;49;00m := [36mCopy[39;49;00m(S, [34m1[39;49;00m, p - [34m1[39;49;00m)$
   713	  [34melse[39;49;00m$
   714	    [36mResult[39;49;00m := S;$
   715	[34mend[39;49;00m;$
   716	$
   717	[34mfunction[39;49;00m [32mUntilChar[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Brake: TCharSet): [34mstring[39;49;00m;$
   718	[34mvar[39;49;00m$
   719	  p: [36mInteger[39;49;00m;$
   720	[34mbegin[39;49;00m$
   721	  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
   722	  p := CharPos(Brake, S);$
   723	$
   724	  [34mif[39;49;00m p > [34m0[39;49;00m [34mthen[39;49;00m$
   725	    [36mResult[39;49;00m := [36mCopy[39;49;00m(S, [34m1[39;49;00m, p - [34m1[39;49;00m)$
   726	  [34melse[39;49;00m$
   727	    [36mResult[39;49;00m := S;$
   728	[34mend[39;49;00m;$
   729	$
   730	[34mfunction[39;49;00m [32mUntilLastChar[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Brake: [36mChar[39;49;00m;$
   731	  IgnoreNoBrake: [36mBoolean[39;49;00m = [34mTrue[39;49;00m): [34mstring[39;49;00m;$
   732	[34mvar[39;49;00m$
   733	  p: [36mInteger[39;49;00m;$
   734	[34mbegin[39;49;00m$
   735	  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
   736	  p := CharPosR(Brake, S);$
   737	$
   738	  [34mif[39;49;00m p > [34m0[39;49;00m [34mthen[39;49;00m$
   739	    [36mResult[39;49;00m := [36mCopy[39;49;00m(S, [34m1[39;49;00m, p - [34m1[39;49;00m)$
   740	  [34melse[39;49;00m [34mif[39;49;00m IgnoreNoBrake [34mthen[39;49;00m$
   741	    [36mResult[39;49;00m := S;$
   742	[34mend[39;49;00m;$
   743	$
   744	[34mfunction[39;49;00m [32mFromChar[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Brake: [36mChar[39;49;00m): [34mstring[39;49;00m;$
   745	[34mvar[39;49;00m$
   746	  p: [36mInteger[39;49;00m;$
   747	[34mbegin[39;49;00m$
   748	  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
   749	  p := CharPos(Brake, S);$
   750	$
   751	  [34mif[39;49;00m p > [34m0[39;49;00m [34mthen[39;49;00m$
   752	    [36mResult[39;49;00m := [36mCopy[39;49;00m(S, p + [34m1[39;49;00m, [36mLength[39;49;00m(S) - p);$
   753	[34mend[39;49;00m;$
   754	$
   755	[34mfunction[39;49;00m [32mFromChar[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Brake: TCharSet): [34mstring[39;49;00m;$
   756	[34mvar[39;49;00m$
   757	  p: [36mInteger[39;49;00m;$
   758	[34mbegin[39;49;00m$
   759	  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
   760	  p := CharPos(Brake, S);$
   761	$
   762	  [34mif[39;49;00m p > [34m0[39;49;00m [34mthen[39;49;00m$
   763	    [36mResult[39;49;00m := [36mCopy[39;49;00m(S, p + [34m1[39;49;00m, [36mLength[39;49;00m(S) - p);$
   764	[34mend[39;49;00m;$
   765	$
   766	[34mfunction[39;49;00m [32mFromLastChar[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Brake: [36mChar[39;49;00m;$
   767	  IgnoreNoBrake: [36mBoolean[39;49;00m = [34mFalse[39;49;00m): [34mstring[39;49;00m;$
   768	[34mvar[39;49;00m$
   769	  p: [36mInteger[39;49;00m;$
   770	[34mbegin[39;49;00m$
   771	  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
   772	  p := CharPosR(Brake, S);$
   773	$
   774	  [34mif[39;49;00m p > [34m0[39;49;00m [34mthen[39;49;00m$
   775	    [36mResult[39;49;00m := [36mCopy[39;49;00m(S, p + [34m1[39;49;00m, [36mLength[39;49;00m(S) - p)$
   776	  [34melse[39;49;00m [34mif[39;49;00m IgnoreNoBrake [34mthen[39;49;00m$
   777	    [36mResult[39;49;00m := S;$
   778	[34mend[39;49;00m;$
   779	$
   780	[34mfunction[39;49;00m [32mBetweenChars[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Start, Finish: [36mChar[39;49;00m;$
   781	  Inclusive: [36mBoolean[39;49;00m = [34mFalse[39;49;00m): [34mstring[39;49;00m;$
   782	[34mvar[39;49;00m$
   783	  p, fin: [36mInteger[39;49;00m;$
   784	[34mbegin[39;49;00m$
   785	  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
   786	$
   787	  p := CharPos(Start, S);$
   788	  [34mif[39;49;00m p = [34m0[39;49;00m [34mthen[39;49;00m$
   789	    [34mExit[39;49;00m;$
   790	$
   791	  fin := CharPos(Finish, S, p + [34m1[39;49;00m);$
   792	  [34mif[39;49;00m fin = [34m0[39;49;00m [34mthen[39;49;00m$
   793	    [34mExit[39;49;00m;$
   794	$
   795	  [34mif[39;49;00m [34mnot[39;49;00m Inclusive [34mthen[39;49;00m [34mbegin[39;49;00m$
   796	    [36mInc[39;49;00m(p);$
   797	    [36mDec[39;49;00m(fin);$
   798	  [34mend[39;49;00m;$
   799	$
   800	  [36mResult[39;49;00m := [36mCopy[39;49;00m(S, p, fin - p + [34m1[39;49;00m);$
   801	[34mend[39;49;00m;$
   802	$
   803	[34mfunction[39;49;00m [32mUntilStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Brake: [34mstring[39;49;00m): [34mstring[39;49;00m;$
   804	[34mvar[39;49;00m$
   805	  p: [36mInteger[39;49;00m;$
   806	[34mbegin[39;49;00m$
   807	  [34mif[39;49;00m [36mLength[39;49;00m(Brake) = [34m1[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m$
   808	    [36mResult[39;49;00m := UntilChar(S, Brake[[34m1[39;49;00m]);$
   809	  [34mExit[39;49;00m; [34mend[39;49;00m;$
   810	$
   811	  p := PosEx(Brake, S);$
   812	$
   813	  [34mif[39;49;00m p > [34m0[39;49;00m [34mthen[39;49;00m$
   814	    [36mResult[39;49;00m := [36mCopy[39;49;00m(S, [34m1[39;49;00m, p - [34m1[39;49;00m)$
   815	  [34melse[39;49;00m$
   816	    [36mResult[39;49;00m := S;$
   817	[34mend[39;49;00m;$
   818	$
   819	[34mfunction[39;49;00m [32mFromStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Brake: [34mstring[39;49;00m): [34mstring[39;49;00m;$
   820	[34mvar[39;49;00m$
   821	  p: [36mInteger[39;49;00m;$
   822	[34mbegin[39;49;00m$
   823	  [34mif[39;49;00m [36mLength[39;49;00m(Brake) = [34m1[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m$
   824	    [36mResult[39;49;00m := FromChar(S, Brake[[34m1[39;49;00m]);$
   825	  [34mExit[39;49;00m; [34mend[39;49;00m;$
   826	$
   827	  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
   828	  p := PosEx(Brake, s);$
   829	$
   830	  [34mif[39;49;00m p > [34m0[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m$
   831	    [36mInc[39;49;00m(p, [36mLength[39;49;00m(Brake));$
   832	    [36mResult[39;49;00m := [36mCopy[39;49;00m(S, p, [36mLength[39;49;00m(S) - p + [34m1[39;49;00m);$
   833	  [34mend[39;49;00m;$
   834	[34mend[39;49;00m;$
   835	$
   836	[34mfunction[39;49;00m [32mStringWrap[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Width: [36mInteger[39;49;00m; [34mconst[39;49;00m LineEnd: [34mstring[39;49;00m = EOL): [34mstring[39;49;00m;$
   837	[34mvar[39;49;00m$
   838	  i: [36mInteger[39;49;00m;$
   839	[34mbegin[39;49;00m$
   840	  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
   841	  [34mif[39;49;00m (S = [33m'[39;49;00m[33m'[39;49;00m) [34mor[39;49;00m (Width < [34m1[39;49;00m) [34mthen[39;49;00m$
   842	    [34mExit[39;49;00m;$
   843	$
   844	  i := [34m1[39;49;00m;$
   845	  [34mwhile[39;49;00m [34mTrue[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m$
   846	    [36mResult[39;49;00m := [36mResult[39;49;00m + [36mCopy[39;49;00m(S, i, Width);$
   847	    [36mInc[39;49;00m(i, Width);$
   848	    [34mif[39;49;00m i <= [36mLength[39;49;00m(S) [34mthen[39;49;00m$
   849	      [36mResult[39;49;00m := [36mResult[39;49;00m + LineEnd$
   850	    [34melse[39;49;00m$
   851	      [34mExit[39;49;00m;$
   852	  [34mend[39;49;00m;$
   853	[34mend[39;49;00m;$
   854	$
   855	[34mfunction[39;49;00m [32mSplit[39;49;00m([34mconst[39;49;00m S, Separator: [34mstring[39;49;00m; IgnoreMultiSep: [36mBoolean[39;49;00m = [34mTrue[39;49;00m;$
   856	  MinCount: [36mInteger[39;49;00m = [34m0[39;49;00m): TStrA;$
   857	[34mvar[39;49;00m$
   858	  p, fin, SepLen: [36mInteger[39;49;00m;$
   859	$
   860	  [34mprocedure[39;49;00m [32mAdd[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m);$
   861	  [34mbegin[39;49;00m$
   862	    [34mif[39;49;00m IgnoreMultiSep [34mand[39;49;00m (S = [33m'[39;49;00m[33m'[39;49;00m) [34mthen[39;49;00m$
   863	      [34mExit[39;49;00m;$
   864	    [36mSetLength[39;49;00m([36mResult[39;49;00m, [36mLength[39;49;00m([36mResult[39;49;00m) + [34m1[39;49;00m);$
   865	    [36mResult[39;49;00m[[36mHigh[39;49;00m([36mResult[39;49;00m)] := S;$
   866	  [34mend[39;49;00m;$
   867	$
   868	[34mbegin[39;49;00m$
   869	  [34mif[39;49;00m S = [33m'[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m$
   870	    [34mif[39;49;00m [36mLength[39;49;00m([36mResult[39;49;00m) < MinCount [34mthen[39;49;00m$
   871	      [36mSetLength[39;49;00m([36mResult[39;49;00m, MinCount);$
   872	  [34mExit[39;49;00m; [34mend[39;49;00m;$
   873	$
   874	  [36mResult[39;49;00m := [34mnil[39;49;00m;$
   875	  SepLen := [36mLength[39;49;00m(Separator);$
   876	$
   877	  p := [34m1[39;49;00m;$
   878	  fin := PosEx(Separator, S);$
   879	  [34mwhile[39;49;00m fin > [34m0[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m$
   880	    Add([36mCopy[39;49;00m(S, p, fin - p));$
   881	    p := fin + SepLen;$
   882	    fin := PosEx(Separator, S, p);$
   883	  [34mend[39;49;00m;$
   884	  Add([36mCopy[39;49;00m(S, p, [36mLength[39;49;00m(S) - p + [34m1[39;49;00m));$
   885	$
   886	  [34mif[39;49;00m [36mLength[39;49;00m([36mResult[39;49;00m) < MinCount [34mthen[39;49;00m$
   887	    [36mSetLength[39;49;00m([36mResult[39;49;00m, MinCount);$
   888	[34mend[39;49;00m;$
   889	$
   890	[34mprocedure[39;49;00m [32mSplit[39;49;00m([34mconst[39;49;00m S, Separator: [34mstring[39;49;00m; Strings: TStrings;$
   891	  IgnoreMultiSep: [36mBoolean[39;49;00m = [34mTrue[39;49;00m); $
   892	[34mvar[39;49;00m$
   893	  p, fin, SepLen: [36mInteger[39;49;00m;$
   894	$
   895	  [34mprocedure[39;49;00m [32mAdd[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m);$
   896	  [34mbegin[39;49;00m$
   897	    [34mif[39;49;00m IgnoreMultiSep [34mand[39;49;00m (S = [33m'[39;49;00m[33m'[39;49;00m) [34mthen[39;49;00m$
   898	      [34mExit[39;49;00m;$
   899	    Strings.Add(S);$
   900	  [34mend[39;49;00m;$
   901	$
   902	[34mbegin[39;49;00m$
   903	  [34mif[39;49;00m S = [33m'[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m$
   904	    [34mExit[39;49;00m;$
   905	$
   906	  Strings.BeginUpdate;$
   907	  SepLen := [36mLength[39;49;00m(Separator);$
   908	  p := [34m1[39;49;00m;$
   909	  fin := PosEx(Separator, S);$
   910	  [34mwhile[39;49;00m fin > [34m0[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m$
   911	    Add([36mCopy[39;49;00m(S, p, fin - p));$
   912	    p := fin + SepLen;$
   913	    fin := PosEx(Separator, S, p);$
   914	  [34mend[39;49;00m;$
   915	  Add([36mCopy[39;49;00m(S, p, [36mLength[39;49;00m(S) - p + [34m1[39;49;00m));$
   916	  Strings.EndUpdate;$
   917	[34mend[39;49;00m;$
   918	$
   919	[34mfunction[39;49;00m [32mSplit[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Separators: TCharSet;$
   920	  IgnoreMultiSep: [36mBoolean[39;49;00m = [34mTrue[39;49;00m; MinCount: [36mInteger[39;49;00m = [34m0[39;49;00m): TStrA;$
   921	[34mvar[39;49;00m$
   922	  p, fin: [36mInteger[39;49;00m;$
   923	$
   924	  [34mprocedure[39;49;00m [32mAdd[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m);$
   925	  [34mbegin[39;49;00m$
   926	    [34mif[39;49;00m IgnoreMultiSep [34mand[39;49;00m (S = [33m'[39;49;00m[33m'[39;49;00m) [34mthen[39;49;00m$
   927	      [34mExit[39;49;00m;$
   928	    [36mSetLength[39;49;00m([36mResult[39;49;00m, [36mLength[39;49;00m([36mResult[39;49;00m) + [34m1[39;49;00m);$
   929	    [36mResult[39;49;00m[[36mHigh[39;49;00m([36mResult[39;49;00m)] := S;$
   930	  [34mend[39;49;00m;$
   931	$
   932	[34mbegin[39;49;00m$
   933	  [34mif[39;49;00m S = [33m'[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m$
   934	    [34mif[39;49;00m [36mLength[39;49;00m([36mResult[39;49;00m) < MinCount [34mthen[39;49;00m$
   935	      [36mSetLength[39;49;00m([36mResult[39;49;00m, MinCount);$
   936	  [34mExit[39;49;00m; [34mend[39;49;00m;$
   937	$
   938	  [36mResult[39;49;00m := [34mnil[39;49;00m;$
   939	$
   940	  p := [34m1[39;49;00m;$
   941	  fin := CharPos(Separators, S);$
   942	  [34mwhile[39;49;00m fin > [34m0[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m$
   943	    Add([36mCopy[39;49;00m(S, p, fin - p));$
   944	    p := fin + [34m1[39;49;00m;$
   945	    fin := CharPos(Separators, S, p);$
   946	  [34mend[39;49;00m;$
   947	  Add([36mCopy[39;49;00m(S, p, [36mLength[39;49;00m(S) - p + [34m1[39;49;00m));$
   948	$
   949	  [34mif[39;49;00m [36mLength[39;49;00m([36mResult[39;49;00m) < MinCount [34mthen[39;49;00m$
   950	    [36mSetLength[39;49;00m([36mResult[39;49;00m, MinCount);$
   951	[34mend[39;49;00m;$
   952	$
   953	[34mprocedure[39;49;00m [32mTileStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; BrakeStart: [36mInteger[39;49;00m; BrakeEnd: [36mInteger[39;49;00m;$
   954	  out Left, Right: [34mstring[39;49;00m);$
   955	[34mbegin[39;49;00m$
   956	  Left := [36mCopy[39;49;00m(S, [34m1[39;49;00m, BrakeStart-[34m1[39;49;00m);$
   957	  Right := [36mCopy[39;49;00m(S, BrakeEnd + [34m1[39;49;00m, MaxInt);$
   958	[34mend[39;49;00m;$
   959	$
   960	[34mfunction[39;49;00m [32mJoin[39;49;00m(Strings: TStrings; Separator: [34mstring[39;49;00m = [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;$
   961	[34mvar[39;49;00m$
   962	  i, imax: [36mInteger[39;49;00m;$
   963	[34mbegin[39;49;00m$
   964	  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
   965	  imax := Strings.Count-[34m1[39;49;00m;$
   966	  [34mfor[39;49;00m i := [34m0[39;49;00m [34mto[39;49;00m imax [34mdo[39;49;00m [34mbegin[39;49;00m$
   967	    [36mResult[39;49;00m := [36mResult[39;49;00m + Strings[i];$
   968	    [34mif[39;49;00m i < imax [34mthen[39;49;00m$
   969	      [36mResult[39;49;00m := [36mResult[39;49;00m + Separator;$
   970	  [34mend[39;49;00m;$
   971	[34mend[39;49;00m;$
   972	$
   973	[34mfunction[39;49;00m [32mJoin[39;49;00m(StrA: TStrA; Separator: [34mstring[39;49;00m = [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m; overload;$
   974	[34mvar[39;49;00m$
   975	  i: [36mInteger[39;49;00m;$
   976	[34mbegin[39;49;00m$
   977	  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
   978	  [34mfor[39;49;00m i := [34m0[39;49;00m [34mto[39;49;00m [36mHigh[39;49;00m(StrA) [34mdo[39;49;00m [34mbegin[39;49;00m$
   979	    [36mResult[39;49;00m := [36mResult[39;49;00m + StrA[i];$
   980	    [34mif[39;49;00m i < [36mHigh[39;49;00m(StrA) [34mthen[39;49;00m$
   981	      [36mResult[39;49;00m := [36mResult[39;49;00m + Separator;$
   982	  [34mend[39;49;00m;$
   983	[34mend[39;49;00m;$
   984	$
   985	[34mfunction[39;49;00m [32mMulStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Count: [36mInteger[39;49;00m): [34mstring[39;49;00m;$
   986	[34mvar[39;49;00m$
   987	  P: [36mPChar[39;49;00m;$
   988	  Len, i: [36mInteger[39;49;00m;$
   989	[34mbegin[39;49;00m$
   990	  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
   991	  [34mif[39;49;00m Count = [34m0[39;49;00m [34mthen[39;49;00m$
   992	    [34mExit[39;49;00m;$
   993	$
   994	  Len := [36mLength[39;49;00m(S);$
   995	  [36mSetLength[39;49;00m([36mResult[39;49;00m, Len * Count);$
   996	$
   997	  P := [36mPointer[39;49;00m([36mResult[39;49;00m);$
   998	  [34mfor[39;49;00m i := [34m1[39;49;00m [34mto[39;49;00m Count [34mdo[39;49;00m [34mbegin[39;49;00m$
   999	    [36mMove[39;49;00m([36mPointer[39;49;00m(S)^, P^, Len);$
  1000	    [36mInc[39;49;00m(P, Len);$
  1001	  [34mend[39;49;00m;$
  1002	[34mend[39;49;00m;$
  1003	$
  1004	[34mfunction[39;49;00m [32mAlignR[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Width: [36mInteger[39;49;00m; Filler: [36mChar[39;49;00m = [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;$
  1005	[34mbegin[39;49;00m$
  1006	  [36mResult[39;49;00m := MulStr(Filler, Width - [36mLength[39;49;00m(S)) + S;$
  1007	[34mend[39;49;00m;$
  1008	$
  1009	[34mfunction[39;49;00m [32mMaxStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; MaxLen: [36mInteger[39;49;00m): [34mstring[39;49;00m;$
  1010	[34mvar[39;49;00m$
  1011	  Len: [36mInteger[39;49;00m;$
  1012	[34mbegin[39;49;00m$
  1013	  Len := [36mLength[39;49;00m(S);$
  1014	  [34mif[39;49;00m Len <= MaxLen [34mthen[39;49;00m [34mbegin[39;49;00m$
  1015	    [36mResult[39;49;00m := S;$
  1016	  [34mExit[39;49;00m [34mend[39;49;00m;$
  1017	$
  1018	  [36mResult[39;49;00m := [36mCopy[39;49;00m(S, [34m1[39;49;00m, MaxLen - [34m3[39;49;00m) + [33m'[39;49;00m[33m...[39;49;00m[33m'[39;49;00m;$
  1019	[34mend[39;49;00m;$
  1020	$
  1021	[34mfunction[39;49;00m [32mTrimAll[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [34mstring[39;49;00m;$
  1022	[34mvar[39;49;00m$
  1023	  i: [36mInteger[39;49;00m;$
  1024	[34mbegin[39;49;00m$
  1025	  [34mfor[39;49;00m i := [34m1[39;49;00m [34mto[39;49;00m [36mLength[39;49;00m(S) [34mdo[39;49;00m$
  1026	    [34mif[39;49;00m S[i] > [33m#32[39;49;00m [34mthen[39;49;00m$
  1027	      [36mResult[39;49;00m := [36mResult[39;49;00m + S[i];$
  1028	[34mend[39;49;00m;$
  1029	$
  1030	[34mfunction[39;49;00m [32mControlChar[39;49;00m(C: [36mChar[39;49;00m): [36mBoolean[39;49;00m;$
  1031	[34mbegin[39;49;00m$
  1032	  [36mResult[39;49;00m := C [34min[39;49;00m StrangeChars;$
  1033	[34mend[39;49;00m;$
  1034	$
  1035	[34mfunction[39;49;00m [32mFriendlyChar[39;49;00m(C: [36mChar[39;49;00m): [36mChar[39;49;00m;$
  1036	[34mbegin[39;49;00m$
  1037	  [34mcase[39;49;00m C [34mof[39;49;00m$
  1038	    [33m#0[39;49;00m: [36mResult[39;49;00m := [33m'[39;49;00m[33m.[39;49;00m[33m'[39;49;00m;$
  1039	    [33m#1[39;49;00m..[33m#31[39;49;00m: [36mResult[39;49;00m := [33m'[39;49;00m[33m?[39;49;00m[33m'[39;49;00m;$
  1040	    [33m#255[39;49;00m: [36mResult[39;49;00m := [33m'[39;49;00m[33m#[39;49;00m[33m'[39;49;00m;$
  1041	  [34melse[39;49;00m$
  1042	    [36mResult[39;49;00m := C;$
  1043	  [34mend[39;49;00m;$
  1044	[34mend[39;49;00m;$
  1045	$
  1046	[34mfunction[39;49;00m [32mFriendlyStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [34mstring[39;49;00m;$
  1047	[34mvar[39;49;00m$
  1048	  i: [36mInteger[39;49;00m;$
  1049	[34mbegin[39;49;00m$
  1050	  [36mSetLength[39;49;00m([36mResult[39;49;00m, [36mLength[39;49;00m(S));$
  1051	  [34mfor[39;49;00m i := [34m1[39;49;00m [34mto[39;49;00m [36mLength[39;49;00m(S) [34mdo[39;49;00m$
  1052	    [36mResult[39;49;00m[i] := FriendlyChar(S[i]);$
  1053	[34mend[39;49;00m;$
  1054	$
  1055	[34mfunction[39;49;00m [32mFriendlyStr[39;49;00m(a: TByteA): [34mstring[39;49;00m;$
  1056	[34mvar[39;49;00m$
  1057	  i: [36mInteger[39;49;00m;$
  1058	[34mbegin[39;49;00m$
  1059	  [36mSetLength[39;49;00m([36mResult[39;49;00m, [36mLength[39;49;00m(a));$
  1060	  [34mfor[39;49;00m i := [34m0[39;49;00m [34mto[39;49;00m [36mHigh[39;49;00m(a) [34mdo[39;49;00m$
  1061	    [36mResult[39;49;00m[i + [34m1[39;49;00m] := FriendlyChar([36mChar[39;49;00m(a[i]));$
  1062	[34mend[39;49;00m;$
  1063	$
  1064	[34mfunction[39;49;00m [32mQuote[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Quoter: [36mChar[39;49;00m = [33m'[39;49;00m[33m"[39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;$
  1065	[34mbegin[39;49;00m$
  1066	  [36mResult[39;49;00m := S;$
  1067	$
  1068	  [34mif[39;49;00m FirstChar(S) <> Quoter [34mthen[39;49;00m$
  1069	    [36mResult[39;49;00m := Quoter + [36mResult[39;49;00m;$
  1070	$
  1071	  [34mif[39;49;00m LastChar(S) <> Quoter [34mthen[39;49;00m$
  1072	    [36mResult[39;49;00m := [36mResult[39;49;00m + Quoter;$
  1073	[34mend[39;49;00m;$
  1074	$
  1075	[34mfunction[39;49;00m [32mDeQuote[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [34mstring[39;49;00m;$
  1076	[34mbegin[39;49;00m$
  1077	  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
  1078	  [34mif[39;49;00m [36mLength[39;49;00m(S) > [34m2[39;49;00m [34mthen[39;49;00m$
  1079	    [36mResult[39;49;00m := [36mCopy[39;49;00m(S, [34m2[39;49;00m, [36mLength[39;49;00m(S) - [34m2[39;49;00m);$
  1080	[34mend[39;49;00m;$
  1081	$
  1082	[34mfunction[39;49;00m [32mUnQuote[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [34mstring[39;49;00m;$
  1083	[34mvar[39;49;00m$
  1084	  Start, Len: [36mInteger[39;49;00m;$
  1085	[34mbegin[39;49;00m$
  1086	  Start := [34m1[39;49;00m;$
  1087	  Len := [36mLength[39;49;00m(S);$
  1088	$
  1089	  [34mif[39;49;00m (S <> [33m'[39;49;00m[33m'[39;49;00m) [34mand[39;49;00m (S[[34m1[39;49;00m] [34min[39;49;00m ([[33m#0[39;49;00m..[33m#32[39;49;00m] + QuoteChars)) [34mthen[39;49;00m [34mbegin[39;49;00m$
  1090	    [34mif[39;49;00m (LastChar(S) = S[[34m1[39;49;00m]) [34mthen[39;49;00m$
  1091	      [36mDec[39;49;00m(Len);$
  1092	    [36mInc[39;49;00m(Start);$
  1093	  [34mend[39;49;00m;$
  1094	$
  1095	  [36mResult[39;49;00m := [36mCopy[39;49;00m(S, Start, Len - Start + [34m1[39;49;00m);$
  1096	[34mend[39;49;00m;$
  1097	$
  1098	[34mfunction[39;49;00m [32mStrNumerus[39;49;00m([34mconst[39;49;00m Value: [36mInteger[39;49;00m; [34mconst[39;49;00m Singular, Plural: [34mstring[39;49;00m;$
  1099	  [34mconst[39;49;00m Zero: [34mstring[39;49;00m = [33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;$
  1100	[34mbegin[39;49;00m$
  1101	  [34mif[39;49;00m [36mAbs[39;49;00m(Value) = [34m1[39;49;00m [34mthen[39;49;00m$
  1102	    [36mResult[39;49;00m := [36mIntToStr[39;49;00m(Value) + [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m + Singular$
  1103	  [34melse[39;49;00m [34mif[39;49;00m Value = [34m0[39;49;00m [34mthen[39;49;00m$
  1104	    [36mResult[39;49;00m := Zero + [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m + Plural$
  1105	  [34melse[39;49;00m$
  1106	    [36mResult[39;49;00m := [36mIntToStr[39;49;00m(Value) + [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m + Plural;$
  1107	[34mend[39;49;00m;$
  1108	$
  1109	[34mfunction[39;49;00m [32mMakeStr[39;49;00m([34mconst[39;49;00m Items: [34marray[39;49;00m [34mof[39;49;00m [34mconst[39;49;00m; Separator: [34mstring[39;49;00m = [33m'[39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;$
  1110	[34mconst[39;49;00m$
  1111	  BoolStrings: [34marray[39;49;00m[[36mBoolean[39;49;00m] [34mof[39;49;00m [34mstring[39;49;00m = ([33m'[39;49;00m[33mFalse[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mTrue[39;49;00m[33m'[39;49;00m);$
  1112	$
  1113	[34mvar[39;49;00m$
  1114	  i: [36mInteger[39;49;00m;$
  1115	$
  1116	  [34mfunction[39;49;00m [32mStrOfP[39;49;00m(P: [36mPointer[39;49;00m): [34mstring[39;49;00m;$
  1117	  [34mbegin[39;49;00m$
  1118	    [34mif[39;49;00m P = [34mnil[39;49;00m [34mthen[39;49;00m$
  1119	      [36mResult[39;49;00m := [33m'[39;49;00m[33m[nil][39;49;00m[33m'[39;49;00m$
  1120	    [34melse[39;49;00m$
  1121	      [36mResult[39;49;00m := [33m'[39;49;00m[33m[[39;49;00m[33m'[39;49;00m + [36mIntToStr[39;49;00m([36mCardinal[39;49;00m(P)) + [33m'[39;49;00m[33m][39;49;00m[33m'[39;49;00m;$
  1122	  [34mend[39;49;00m;$
  1123	$
  1124	  [34mprocedure[39;49;00m [32mAdd[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m);$
  1125	  [34mbegin[39;49;00m$
  1126	    [36mResult[39;49;00m := [36mResult[39;49;00m + s + Separator;$
  1127	  [34mend[39;49;00m;$
  1128	$
  1129	[34mbegin[39;49;00m$
  1130	  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
  1131	  [34mfor[39;49;00m i := [34m0[39;49;00m [34mto[39;49;00m [36mHigh[39;49;00m(Items) [34mdo[39;49;00m$
  1132	    [34mwith[39;49;00m Items[i] [34mdo[39;49;00m$
  1133	      [34mcase[39;49;00m VType [34mof[39;49;00m$
  1134	        vtString:     Add(VString^);$
  1135	        vtInteger:    Add([36mIntToStr[39;49;00m(VInteger));$
  1136	        vtBoolean:    Add(BoolStrings[VBoolean]);$
  1137	        vtChar:       Add(VChar);$
  1138	        vtPChar:      Add(VPChar);$
  1139	        vtExtended:   Add([36mFloatToStr[39;49;00m(VExtended^));$
  1140	        vtObject:     [34mif[39;49;00m VObject [34mis[39;49;00m TComponent [34mthen[39;49;00m$
  1141	                        Add(TComponent(VObject).Name)$
  1142	                      [34melse[39;49;00m$
  1143	                        Add(VObject.ClassName);$
  1144	        vtClass:      Add(VClass.ClassName);$
  1145	        vtAnsiString: Add([34mstring[39;49;00m(VAnsiString));$
  1146	        vtCurrency:   Add([36mCurrToStr[39;49;00m(VCurrency^));$
  1147	        vtInt64:      Add([36mIntToStr[39;49;00m(VInt64^));$
  1148	        vtVariant:    Add([34mstring[39;49;00m(VVariant^));$
  1149	$
  1150	        vtWideChar:   Add(VWideChar);$
  1151	        vtPWideChar:  Add(VPWideChar);$
  1152	        vtInterface:  Add(StrOfP(VInterface));$
  1153	        vtPointer:    Add(StrOfP(VPointer));$
  1154	        vtWideString: Add([36mWideString[39;49;00m(VWideString));$
  1155	      [34mend[39;49;00m;$
  1156	  [34mif[39;49;00m [36mResult[39;49;00m <> [33m'[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m$
  1157	    [36mSetLength[39;49;00m([36mresult[39;49;00m, [36mLength[39;49;00m([36mResult[39;49;00m) - [36mLength[39;49;00m(Separator));$
  1158	[34mend[39;49;00m;$
  1159	$
  1160	[34mprocedure[39;49;00m [32mShowText[39;49;00m([34mconst[39;49;00m Items: [34marray[39;49;00m [34mof[39;49;00m [34mconst[39;49;00m; Separator: [34mstring[39;49;00m = [33m'[39;49;00m[33m'[39;49;00m);$
  1161	[34mvar[39;49;00m$
  1162	  Text: [34mstring[39;49;00m;$
  1163	[34mbegin[39;49;00m$
  1164	  Text := MakeStr(Items, Separator);$
  1165	$
  1166	  MessageBox([34m0[39;49;00m, [36mPChar[39;49;00m(Text), [33m'[39;49;00m[33mInfo[39;49;00m[33m'[39;49;00m, MB_OK [34mand[39;49;00m MB_APPLMODAL);$
  1167	[34mend[39;49;00m;$
  1168	$
  1169	[34mfunction[39;49;00m [32mDeleteChars[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; C: [36mChar[39;49;00m): [34mstring[39;49;00m;$
  1170	[34mvar[39;49;00m$
  1171	  i: [36mInteger[39;49;00m;$
  1172	[34mbegin[39;49;00m$
  1173	  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
  1174	  [34mfor[39;49;00m i := [34m1[39;49;00m [34mto[39;49;00m [36mLength[39;49;00m(S) [34mdo[39;49;00m$
  1175	    [34mif[39;49;00m S[i] <> C [34mthen[39;49;00m$
  1176	      [36mResult[39;49;00m := [36mResult[39;49;00m + S[i];$
  1177	[34mend[39;49;00m;$
  1178	$
  1179	[34mfunction[39;49;00m [32mDeleteChars[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; C: TCharSet): [34mstring[39;49;00m;$
  1180	[34mvar[39;49;00m$
  1181	  i: [36mInteger[39;49;00m;$
  1182	[34mbegin[39;49;00m$
  1183	  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
  1184	  [34mfor[39;49;00m i := [34m1[39;49;00m [34mto[39;49;00m [36mLength[39;49;00m(S) [34mdo[39;49;00m$
  1185	    [34mif[39;49;00m [34mnot[39;49;00m (S[i] [34min[39;49;00m C) [34mthen[39;49;00m$
  1186	      [36mResult[39;49;00m := [36mResult[39;49;00m + S[i];$
  1187	[34mend[39;49;00m;$
  1188	$
  1189	[34mfunction[39;49;00m [32mExtractChars[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; C: TCharSet): [34mstring[39;49;00m;$
  1190	[34mvar[39;49;00m$
  1191	  i: [36mInteger[39;49;00m;$
  1192	[34mbegin[39;49;00m$
  1193	  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
  1194	  [34mfor[39;49;00m i := [34m1[39;49;00m [34mto[39;49;00m [36mLength[39;49;00m(S) [34mdo[39;49;00m$
  1195	    [34mif[39;49;00m S[i] [34min[39;49;00m C [34mthen[39;49;00m$
  1196	      [36mResult[39;49;00m := [36mResult[39;49;00m + S[i];$
  1197	[34mend[39;49;00m;$
  1198	$
  1199	[34mfunction[39;49;00m [32mCharCount[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; C: [36mChar[39;49;00m): [36mInteger[39;49;00m;$
  1200	[34mvar[39;49;00m$
  1201	  i: [36mInteger[39;49;00m;$
  1202	[34mbegin[39;49;00m$
  1203	  [36mResult[39;49;00m := [34m0[39;49;00m;$
  1204	  [34mfor[39;49;00m i := [34m1[39;49;00m [34mto[39;49;00m [36mLength[39;49;00m(S) [34mdo[39;49;00m$
  1205	    [34mif[39;49;00m S[i] = C [34mthen[39;49;00m$
  1206	      [36mInc[39;49;00m([36mResult[39;49;00m);$
  1207	[34mend[39;49;00m;$
  1208	$
  1209	[34mfunction[39;49;00m [32mStrAtPos[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; [36mPos[39;49;00m: [36mInteger[39;49;00m; [34mconst[39;49;00m [36mStr[39;49;00m: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
  1210	[34mbegin[39;49;00m$
  1211	  [36mResult[39;49;00m := ([36mStr[39;49;00m <> [33m'[39;49;00m[33m'[39;49;00m) [34mand[39;49;00m ([36mStr[39;49;00m = [36mCopy[39;49;00m(S, [36mPos[39;49;00m, [36mLength[39;49;00m([36mStr[39;49;00m)));$
  1212	[34mend[39;49;00m;$
  1213	$
  1214	[34mfunction[39;49;00m [32mTextAtPos[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; [36mPos[39;49;00m: [36mInteger[39;49;00m; [34mconst[39;49;00m Text: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
  1215	[34mbegin[39;49;00m$
  1216	  [36mResult[39;49;00m := (Text <> [33m'[39;49;00m[33m'[39;49;00m) [34mand[39;49;00m [36mSameText[39;49;00m(Text, [36mCopy[39;49;00m(S, [36mPos[39;49;00m, [36mLength[39;49;00m(Text)));$
  1217	[34mend[39;49;00m;$
  1218	$
  1219	[34mfunction[39;49;00m [32mStrAtBegin[39;49;00m([34mconst[39;49;00m S, [36mStr[39;49;00m: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
  1220	[34mbegin[39;49;00m$
  1221	  [36mResult[39;49;00m := StrAtPos(S, [34m1[39;49;00m, [36mStr[39;49;00m);$
  1222	[34mend[39;49;00m;$
  1223	$
  1224	[34mfunction[39;49;00m [32mTextAtBegin[39;49;00m([34mconst[39;49;00m S, Text: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
  1225	[34mbegin[39;49;00m$
  1226	  [36mResult[39;49;00m := TextAtPos(S, [34m1[39;49;00m, Text);$
  1227	[34mend[39;49;00m;$
  1228	$
  1229	[34mfunction[39;49;00m [32mCharIn[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; C: [36mChar[39;49;00m): [36mBoolean[39;49;00m;$
  1230	[34mvar[39;49;00m$
  1231	  i: [36mInteger[39;49;00m;$
  1232	[34mbegin[39;49;00m$
  1233	  [36mResult[39;49;00m := [34mTrue[39;49;00m;$
  1234	  [34mfor[39;49;00m i := [34m1[39;49;00m [34mto[39;49;00m [36mLength[39;49;00m(S) [34mdo[39;49;00m$
  1235	    [34mif[39;49;00m S[i] = C [34mthen[39;49;00m [34mExit[39;49;00m;$
  1236	  [36mResult[39;49;00m := [34mFalse[39;49;00m;$
  1237	[34mend[39;49;00m;$
  1238	$
  1239	[34mfunction[39;49;00m [32mCharIn[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; C: TCharSet): [36mBoolean[39;49;00m;$
  1240	[34mvar[39;49;00m$
  1241	  i: [36mInteger[39;49;00m;$
  1242	[34mbegin[39;49;00m$
  1243	  [36mResult[39;49;00m := [34mFalse[39;49;00m;$
  1244	  [34mfor[39;49;00m i := [34m1[39;49;00m [34mto[39;49;00m [36mLength[39;49;00m(S) [34mdo[39;49;00m [34mbegin[39;49;00m$
  1245	    [36mResult[39;49;00m := S[i] [34min[39;49;00m C;$
  1246	    [34mif[39;49;00m [36mResult[39;49;00m [34mthen[39;49;00m$
  1247	      [34mExit[39;49;00m;$
  1248	  [34mend[39;49;00m;$
  1249	[34mend[39;49;00m;$
  1250	$
  1251	[34mfunction[39;49;00m [32mStrIn[39;49;00m([34mconst[39;49;00m S, SubStr: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
  1252	[34mbegin[39;49;00m$
  1253	  [36mResult[39;49;00m := PosEx(SubStr, S) > [34m0[39;49;00m;$
  1254	[34mend[39;49;00m;$
  1255	$
  1256	[34mfunction[39;49;00m [32mStrIn[39;49;00m(SL: TStrings; [34mconst[39;49;00m S: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
  1257	[34mvar[39;49;00m$
  1258	  i: [36mInteger[39;49;00m;$
  1259	[34mbegin[39;49;00m$
  1260	  [36mResult[39;49;00m := [34mFalse[39;49;00m;$
  1261	  [34mfor[39;49;00m i := [34m0[39;49;00m [34mto[39;49;00m SL.Count-[34m1[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m$
  1262	    [36mResult[39;49;00m := (S = SL[i]);$
  1263	    [34mif[39;49;00m [36mResult[39;49;00m [34mthen[39;49;00m$
  1264	      [34mExit[39;49;00m;$
  1265	  [34mend[39;49;00m;$
  1266	[34mend[39;49;00m;$
  1267	$
  1268	[34mfunction[39;49;00m [32mStrIn[39;49;00m(A: TStrA; [34mconst[39;49;00m S: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
  1269	[34mvar[39;49;00m$
  1270	  i: [36mInteger[39;49;00m;$
  1271	[34mbegin[39;49;00m$
  1272	  [36mResult[39;49;00m := [34mFalse[39;49;00m;$
  1273	  [34mfor[39;49;00m i := [36mLow[39;49;00m(A) [34mto[39;49;00m [36mHigh[39;49;00m(A) [34mdo[39;49;00m [34mbegin[39;49;00m$
  1274	    [36mResult[39;49;00m := (S = A[i]);$
  1275	    [34mif[39;49;00m [36mResult[39;49;00m [34mthen[39;49;00m$
  1276	      [34mExit[39;49;00m;$
  1277	  [34mend[39;49;00m;$
  1278	[34mend[39;49;00m;$
  1279	$
  1280	[34mfunction[39;49;00m [32mTextIn[39;49;00m([34mconst[39;49;00m S, Text: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
  1281	[34mbegin[39;49;00m$
  1282	  [36mResult[39;49;00m := PosExText(Text, S) > [34m0[39;49;00m;$
  1283	[34mend[39;49;00m;$
  1284	$
  1285	[34mfunction[39;49;00m [32mTextIn[39;49;00m(SL: TStrings; [34mconst[39;49;00m Text: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
  1286	[34mvar[39;49;00m$
  1287	  i: [36mInteger[39;49;00m;$
  1288	[34mbegin[39;49;00m$
  1289	  [36mResult[39;49;00m := [34mFalse[39;49;00m;$
  1290	  [34mfor[39;49;00m i := [34m0[39;49;00m [34mto[39;49;00m SL.Count-[34m1[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m$
  1291	    [36mResult[39;49;00m := [36mSameText[39;49;00m(Text, SL[i]);$
  1292	    [34mif[39;49;00m [36mResult[39;49;00m [34mthen[39;49;00m$
  1293	      [34mExit[39;49;00m;$
  1294	  [34mend[39;49;00m;$
  1295	[34mend[39;49;00m;$
  1296	$
  1297	[34mfunction[39;49;00m [32mTextIn[39;49;00m(A: TStrA; [34mconst[39;49;00m Text: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
  1298	[34mvar[39;49;00m$
  1299	  i: [36mInteger[39;49;00m;$
  1300	[34mbegin[39;49;00m$
  1301	  [36mResult[39;49;00m := [34mFalse[39;49;00m;$
  1302	  [34mfor[39;49;00m i := [36mLow[39;49;00m(A) [34mto[39;49;00m [36mHigh[39;49;00m(A) [34mdo[39;49;00m [34mbegin[39;49;00m$
  1303	    [36mResult[39;49;00m := [36mSameText[39;49;00m(Text, A[i]);$
  1304	    [34mif[39;49;00m [36mResult[39;49;00m [34mthen[39;49;00m$
  1305	      [34mExit[39;49;00m;$
  1306	  [34mend[39;49;00m;$
  1307	[34mend[39;49;00m;$
  1308	$
  1309	[34mfunction[39;49;00m [32mStrIndex[39;49;00m(SL: TStrings; [34mconst[39;49;00m S: [34mstring[39;49;00m): [36mInteger[39;49;00m;$
  1310	[34mbegin[39;49;00m$
  1311	  [34mfor[39;49;00m [36mResult[39;49;00m := [34m0[39;49;00m [34mto[39;49;00m SL.Count-[34m1[39;49;00m [34mdo[39;49;00m$
  1312	    [34mif[39;49;00m S = SL[[36mResult[39;49;00m] [34mthen[39;49;00m$
  1313	      [34mExit[39;49;00m;$
  1314	  [36mResult[39;49;00m := -[34m1[39;49;00m;$
  1315	[34mend[39;49;00m;$
  1316	$
  1317	[34mfunction[39;49;00m [32mStrIndex[39;49;00m(A: TStrA; [34mconst[39;49;00m S: [34mstring[39;49;00m): [36mInteger[39;49;00m;$
  1318	[34mbegin[39;49;00m$
  1319	  [34mfor[39;49;00m [36mResult[39;49;00m := [36mLow[39;49;00m(A) [34mto[39;49;00m [36mHigh[39;49;00m(A) [34mdo[39;49;00m$
  1320	    [34mif[39;49;00m S = A[[36mResult[39;49;00m] [34mthen[39;49;00m$
  1321	      [34mExit[39;49;00m;$
  1322	  [36mResult[39;49;00m := -[34m1[39;49;00m;$
  1323	[34mend[39;49;00m;$
  1324	$
  1325	[34mfunction[39;49;00m [32mTextIndex[39;49;00m(SL: TStrings; [34mconst[39;49;00m Text: [34mstring[39;49;00m): [36mInteger[39;49;00m;$
  1326	[34mbegin[39;49;00m$
  1327	  [34mfor[39;49;00m [36mResult[39;49;00m := [34m0[39;49;00m [34mto[39;49;00m SL.Count-[34m1[39;49;00m [34mdo[39;49;00m$
  1328	    [34mif[39;49;00m [36mSameText[39;49;00m(Text, SL[[36mResult[39;49;00m]) [34mthen[39;49;00m$
  1329	      [34mExit[39;49;00m;$
  1330	  [36mResult[39;49;00m := -[34m1[39;49;00m;$
  1331	[34mend[39;49;00m;$
  1332	$
  1333	[34mfunction[39;49;00m [32mTextIndex[39;49;00m(A: TStrA; [34mconst[39;49;00m Text: [34mstring[39;49;00m): [36mInteger[39;49;00m;$
  1334	[34mbegin[39;49;00m$
  1335	  [34mfor[39;49;00m [36mResult[39;49;00m := [36mLow[39;49;00m(A) [34mto[39;49;00m [36mHigh[39;49;00m(A) [34mdo[39;49;00m$
  1336	    [34mif[39;49;00m [36mSameText[39;49;00m(Text, A[[36mResult[39;49;00m]) [34mthen[39;49;00m$
  1337	      [34mExit[39;49;00m;$
  1338	  [36mResult[39;49;00m := -[34m1[39;49;00m;$
  1339	[34mend[39;49;00m;$
  1340	$
  1341	[34mfunction[39;49;00m [32mReplaceChars[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Old, [34mNew[39;49;00m: [36mChar[39;49;00m): [34mstring[39;49;00m;$
  1342	[34mvar[39;49;00m$
  1343	  i: [36mInteger[39;49;00m;$
  1344	[34mbegin[39;49;00m$
  1345	  [36mResult[39;49;00m := S;$
  1346	  [34mfor[39;49;00m i := [34m1[39;49;00m [34mto[39;49;00m [36mLength[39;49;00m([36mResult[39;49;00m) [34mdo[39;49;00m$
  1347	    [34mif[39;49;00m [36mResult[39;49;00m[i] = Old [34mthen[39;49;00m$
  1348	      [36mResult[39;49;00m[i] := [34mNew[39;49;00m;$
  1349	[34mend[39;49;00m;$
  1350	$
  1351	[34mfunction[39;49;00m [32mReplaceChars[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Old: TCharSet; [34mNew[39;49;00m: [36mChar[39;49;00m): [34mstring[39;49;00m;$
  1352	[34mvar[39;49;00m$
  1353	  i: [36mInteger[39;49;00m;$
  1354	[34mbegin[39;49;00m$
  1355	  [36mResult[39;49;00m := S;$
  1356	  [34mfor[39;49;00m i := [34m1[39;49;00m [34mto[39;49;00m [36mLength[39;49;00m([36mResult[39;49;00m) [34mdo[39;49;00m$
  1357	    [34mif[39;49;00m [36mResult[39;49;00m[i] [34min[39;49;00m Old [34mthen[39;49;00m$
  1358	      [36mResult[39;49;00m[i] := [34mNew[39;49;00m;$
  1359	[34mend[39;49;00m;$
  1360	$
  1361	[34mfunction[39;49;00m [32mReplace[39;49;00m([34mconst[39;49;00m S, Old, [34mNew[39;49;00m: [34mstring[39;49;00m): [34mstring[39;49;00m;$
  1362	[34mvar[39;49;00m$
  1363	  oldp, ps: [36mInteger[39;49;00m;$
  1364	[34mbegin[39;49;00m$
  1365	  ps := [34m1[39;49;00m;$
  1366	  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
  1367	  [34mwhile[39;49;00m [34mTrue[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m$
  1368	    oldp := ps;$
  1369	    ps := PosEx(Old, S, oldp);$
  1370	    [34mif[39;49;00m ps = [34m0[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m$
  1371	      [36mResult[39;49;00m := [36mResult[39;49;00m + [36mCopy[39;49;00m(S, oldp, [36mLength[39;49;00m(S) - oldp + [34m1[39;49;00m);$
  1372	    [34mExit[39;49;00m; [34mend[39;49;00m;$
  1373	    [36mResult[39;49;00m := [36mResult[39;49;00m + [36mCopy[39;49;00m(S, oldp, ps - oldp) + [34mNew[39;49;00m;$
  1374	    [36mInc[39;49;00m(ps, [36mLength[39;49;00m(Old));$
  1375	  [34mend[39;49;00m;$
  1376	[34mend[39;49;00m;$
  1377	$
  1378	[34mfunction[39;49;00m [32mSLOfFile[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m): TStringList;$
  1379	[34mbegin[39;49;00m$
  1380	  [36mResult[39;49;00m := TStringList.Create;$
  1381	  [34mif[39;49;00m [36mFileExists[39;49;00m(FileName) [34mthen[39;49;00m$
  1382	    [36mResult[39;49;00m.LoadFromFile(FileName);$
  1383	[34mend[39;49;00m;$
  1384	$
  1385	[34mfunction[39;49;00m [32mContainsEmptyLines[39;49;00m(SL: TStrings): [36mBoolean[39;49;00m;$
  1386	[34mbegin[39;49;00m$
  1387	  [36mResult[39;49;00m := StrIn(SL, [33m'[39;49;00m[33m'[39;49;00m);$
  1388	[34mend[39;49;00m;$
  1389	$
  1390	[34mprocedure[39;49;00m [32mDeleteEmptyLines[39;49;00m(SL: TStrings);$
  1391	[34mvar[39;49;00m$
  1392	  i: [36mInteger[39;49;00m;$
  1393	[34mbegin[39;49;00m$
  1394	  i := [34m0[39;49;00m;$
  1395	  [34mwhile[39;49;00m i < SL.Count [34mdo[39;49;00m [34mbegin[39;49;00m$
  1396	    [34mif[39;49;00m SL[i] = [33m'[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m$
  1397	      SL.Delete(i)$
  1398	    [34melse[39;49;00m$
  1399	      [36mInc[39;49;00m(i);$
  1400	  [34mend[39;49;00m;$
  1401	[34mend[39;49;00m;$
  1402	$
  1403	[34mprocedure[39;49;00m [32mDeleteCommentLines[39;49;00m(SL: TStrings; [34mconst[39;49;00m CommentSign: [34mstring[39;49;00m = [33m'[39;49;00m[33m//[39;49;00m[33m'[39;49;00m);$
  1404	[34mvar[39;49;00m$
  1405	  i: [36mInteger[39;49;00m;$
  1406	[34mbegin[39;49;00m$
  1407	  i := [34m0[39;49;00m;$
  1408	  [34mwhile[39;49;00m i < SL.Count [34mdo[39;49;00m [34mbegin[39;49;00m$
  1409	    [34mif[39;49;00m (SL[i] = [33m'[39;49;00m[33m'[39;49;00m) [34mor[39;49;00m (StrAtBegin([36mTrimLeft[39;49;00m(SL[i]), CommentSign)) [34mthen[39;49;00m$
  1410	      SL.Delete(i)$
  1411	    [34melse[39;49;00m$
  1412	      [36mInc[39;49;00m(i);$
  1413	  [34mend[39;49;00m;$
  1414	[34mend[39;49;00m;$
  1415	$
  1416	[34mfunction[39;49;00m [32mFindLine[39;49;00m(SL: TStrings; [34mconst[39;49;00m S: [34mstring[39;49;00m): [36mInteger[39;49;00m;$
  1417	[34mbegin[39;49;00m$
  1418	  [34mfor[39;49;00m [36mResult[39;49;00m := [34m0[39;49;00m [34mto[39;49;00m SL.Count-[34m1[39;49;00m [34mdo[39;49;00m$
  1419	    [34mif[39;49;00m TextAtBegin(SL[[36mResult[39;49;00m], S) [34mthen[39;49;00m$
  1420	      [34mExit[39;49;00m;$
  1421	  [36mResult[39;49;00m := -[34m1[39;49;00m;$
  1422	[34mend[39;49;00m;$
  1423	$
  1424	[34mprocedure[39;49;00m [32mQuickSortSL[39;49;00m(SL: TStringList);$
  1425	$
  1426	  [34mprocedure[39;49;00m [32mSort[39;49;00m(l, r: [36mInteger[39;49;00m);$
  1427	  [34mvar[39;49;00m$
  1428	    i,j: [36mInteger[39;49;00m;$
  1429	    z,x: [34mstring[39;49;00m;$
  1430	  [34mbegin[39;49;00m$
  1431	    i := l;$
  1432	    j := r;$
  1433	    x := SL[(j + i) [34mdiv[39;49;00m [34m2[39;49;00m];$
  1434	    [34mrepeat[39;49;00m$
  1435	      [34mwhile[39;49;00m SL[i] < x [34mdo[39;49;00m [36mInc[39;49;00m(i);$
  1436	      [34mwhile[39;49;00m SL[j] > x [34mdo[39;49;00m [36mDec[39;49;00m(j);$
  1437	      [34mif[39;49;00m i <= j [34mthen[39;49;00m [34mbegin[39;49;00m$
  1438	        z := SL[i];$
  1439	        SL[i] := SL[j];$
  1440	        SL[j] := z;$
  1441	        [36mInc[39;49;00m(i); [36mDec[39;49;00m(j);$
  1442	      [34mend[39;49;00m;$
  1443	    [34muntil[39;49;00m i > j;$
  1444	    [34mif[39;49;00m j > l [34mthen[39;49;00m Sort(l, j);$
  1445	    [34mif[39;49;00m i < r [34mthen[39;49;00m Sort(i, r);$
  1446	  [34mend[39;49;00m;$
  1447	$
  1448	[34mbegin[39;49;00m$
  1449	  [34mif[39;49;00m SL.Count > [34m0[39;49;00m [34mthen[39;49;00m$
  1450	    Sort([34m0[39;49;00m, SL.Count-[34m1[39;49;00m);$
  1451	[34mend[39;49;00m;$
  1452	$
  1453	[34mfunction[39;49;00m [32mIncStrA[39;49;00m(StrA: TStrA): [36mInteger[39;49;00m;$
  1454	[34mbegin[39;49;00m$
  1455	  [36mSetLength[39;49;00m(StrA, [36mLength[39;49;00m(StrA) + [34m1[39;49;00m);$
  1456	  [36mResult[39;49;00m := [36mHigh[39;49;00m(StrA);$
  1457	[34mend[39;49;00m;$
  1458	$
  1459	[34mfunction[39;49;00m [32mStrOfByteA[39;49;00m(a: TByteA): [34mstring[39;49;00m;$
  1460	[34mbegin[39;49;00m$
  1461	  [36mResult[39;49;00m := [34mstring[39;49;00m([36mCopy[39;49;00m(a, [34m0[39;49;00m, [36mLength[39;49;00m(a)));$
  1462	[34mend[39;49;00m;$
  1463	$
  1464	[34mfunction[39;49;00m [32mByteAOfStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): TByteA;$
  1465	[34mbegin[39;49;00m$
  1466	  [36mResult[39;49;00m := TByteA([36mCopy[39;49;00m(S, [34m1[39;49;00m, [36mLength[39;49;00m(s)));$
  1467	[34mend[39;49;00m;$
  1468	$
  1469	[34mfunction[39;49;00m [32mByteAOfInt[39;49;00m(i: [36mInteger[39;49;00m): TByteA;$
  1470	[34mbegin[39;49;00m$
  1471	  [36mSetLength[39;49;00m([36mResult[39;49;00m, [36mSizeOf[39;49;00m([36mInteger[39;49;00m));$
  1472	  [36mMove[39;49;00m(i, [36mPointer[39;49;00m([36mResult[39;49;00m)^, [36mSizeOf[39;49;00m([36mInteger[39;49;00m));$
  1473	[34mend[39;49;00m;$
  1474	$
  1475	[34mfunction[39;49;00m [32mIntOfByteA[39;49;00m(A: TByteA): [36mInteger[39;49;00m;$
  1476	[34mbegin[39;49;00m$
  1477	  [36mResult[39;49;00m := [34m0[39;49;00m;$
  1478	  [36mMove[39;49;00m([36mPointer[39;49;00m(A)^, [36mResult[39;49;00m, [36mMin[39;49;00m([36mLength[39;49;00m(A), [36mSizeOf[39;49;00m([36mInteger[39;49;00m)));$
  1479	[34mend[39;49;00m;$
  1480	$
  1481	[34mfunction[39;49;00m [32mByteAOfHex[39;49;00m([34mconst[39;49;00m Hex: [34mstring[39;49;00m): TByteA;$
  1482	[34mvar[39;49;00m$
  1483	  i: [36mInteger[39;49;00m;$
  1484	  h: [34mstring[39;49;00m;$
  1485	[34mbegin[39;49;00m$
  1486	  h := ExtractChars(Hex, HexadecimalChars);$
  1487	  [36mSetLength[39;49;00m([36mResult[39;49;00m, [36mLength[39;49;00m(h) [34mdiv[39;49;00m [34m2[39;49;00m);$
  1488	  [34mfor[39;49;00m i := [34m0[39;49;00m [34mto[39;49;00m [36mHigh[39;49;00m([36mResult[39;49;00m) [34mdo[39;49;00m$
  1489	    [36mResult[39;49;00m[i] := ByteOfHex([36mCopy[39;49;00m(h, (i [34mshl[39;49;00m [34m1[39;49;00m) + [34m1[39;49;00m, [34m2[39;49;00m));$
  1490	[34mend[39;49;00m;$
  1491	$
  1492	[34mfunction[39;49;00m [32mSizeOfFile[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m): [36mInteger[39;49;00m;$
  1493	[34mvar[39;49;00m$
  1494	  F: [34mfile[39;49;00m;$
  1495	[34mbegin[39;49;00m$
  1496	  [36mAssignFile[39;49;00m(F, FileName);$
  1497	  [37m{$I-}[39;49;00m[36mReset[39;49;00m(F, [34m1[39;49;00m);[37m{$I+}[39;49;00m$
  1498	  [34mif[39;49;00m [36mIOResult[39;49;00m = [34m0[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m$
  1499	    [36mResult[39;49;00m := [36mFileSize[39;49;00m(F);$
  1500	    [36mCloseFile[39;49;00m(F);$
  1501	  [34mend[39;49;00m [34melse[39;49;00m$
  1502	    [36mResult[39;49;00m := [34m0[39;49;00m;$
  1503	[34mend[39;49;00m;$
  1504	$
  1505	[34mfunction[39;49;00m [32mFileEx[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m; AllowFolders: [36mBoolean[39;49;00m = [34mFalse[39;49;00m): [36mBoolean[39;49;00m;$
  1506	[34mvar[39;49;00m$
  1507	  FindData: TWin32FindData;$
  1508	[34mbegin[39;49;00m$
  1509	  [34mif[39;49;00m FileName = [33m'[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m$
  1510	    [36mResult[39;49;00m := [34mFalse[39;49;00m;$
  1511	  [34mExit[39;49;00m; [34mend[39;49;00m;$
  1512	$
  1513	  [36mResult[39;49;00m := (AllowFolders [34mand[39;49;00m [36mDirectoryExists[39;49;00m(FileName)) [34mor[39;49;00m$
  1514	    (FindFirstFile([36mPChar[39;49;00m(FileName), FindData) <> INVALID_HANDLE_VALUE);$
  1515	  [36mResult[39;49;00m := [36mResult[39;49;00m [34mand[39;49;00m [34mnot[39;49;00m CharIn(FileName, WildCards);$
  1516	  [36mResult[39;49;00m := [36mResult[39;49;00m [34mand[39;49;00m (AllowFolders$
  1517	    [34mor[39;49;00m ((FindData.dwFileAttributes [34mand[39;49;00m FILE_ATTRIBUTE_DIRECTORY) = [34m0[39;49;00m));$
  1518	[34mend[39;49;00m;$
  1519	$
  1520	[34mfunction[39;49;00m [32mLWPSolve[39;49;00m([34mconst[39;49;00m Dir: [34mstring[39;49;00m): [34mstring[39;49;00m;$
  1521	[34mbegin[39;49;00m$
  1522	  [34mif[39;49;00m (Dir <> [33m'[39;49;00m[33m'[39;49;00m) [34mand[39;49;00m (Dir[[36mLength[39;49;00m(Dir)] = [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m) [34mthen[39;49;00m [34mbegin[39;49;00m$
  1523	    [36mResult[39;49;00m := [36mCopy[39;49;00m(Dir, [34m1[39;49;00m, [36mLength[39;49;00m(Dir) - [34m1[39;49;00m);$
  1524	  [34mend[39;49;00m [34melse[39;49;00m$
  1525	    [36mResult[39;49;00m := Dir;$
  1526	[34mend[39;49;00m;$
  1527	$
  1528	[34mfunction[39;49;00m [32mLWPSlash[39;49;00m([34mconst[39;49;00m Dir: [34mstring[39;49;00m): [34mstring[39;49;00m;$
  1529	[34mbegin[39;49;00m$
  1530	  [34mif[39;49;00m (Dir <> [33m'[39;49;00m[33m'[39;49;00m) [34mand[39;49;00m (Dir[[36mLength[39;49;00m(Dir)] = [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m) [34mthen[39;49;00m [34mbegin[39;49;00m$
  1531	    [36mResult[39;49;00m := [36mCopy[39;49;00m(Dir, [34m1[39;49;00m, [36mLength[39;49;00m(Dir));$
  1532	  [34mend[39;49;00m [34melse[39;49;00m$
  1533	    [36mResult[39;49;00m := Dir + [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m;$
  1534	[34mend[39;49;00m;$
  1535	$
  1536	[34mfunction[39;49;00m [32mExtractDrive[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m): [34mstring[39;49;00m;$
  1537	[34mbegin[39;49;00m$
  1538	  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
  1539	  [34mif[39;49;00m ([36mLength[39;49;00m(FileName) >= [34m2[39;49;00m) [34mand[39;49;00m (FileName[[34m2[39;49;00m] = [33m'[39;49;00m[33m:[39;49;00m[33m'[39;49;00m) [34mthen[39;49;00m$
  1540	    [36mResult[39;49;00m := [36mUpperCase[39;49;00m(FileName[[34m1[39;49;00m] + [33m'[39;49;00m[33m:\[39;49;00m[33m'[39;49;00m);$
  1541	[34mend[39;49;00m;$
  1542	$
  1543	[34mfunction[39;49;00m [32mExtractPath[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m): [34mstring[39;49;00m;$
  1544	[34mvar[39;49;00m$
  1545	  p: [36mInteger[39;49;00m;$
  1546	[34mbegin[39;49;00m$
  1547	  p := CharPosR([33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m, FileName);$
  1548	  [34mif[39;49;00m P > [34m0[39;49;00m [34mthen[39;49;00m$
  1549	    [36mResult[39;49;00m := [36mCopy[39;49;00m(FileName, [34m1[39;49;00m, p)$
  1550	  [34melse[39;49;00m$
  1551	    [36mResult[39;49;00m := FileName;$
  1552	[34mend[39;49;00m;$
  1553	$
  1554	[34mfunction[39;49;00m [32mExtractPrefix[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m): [34mstring[39;49;00m;$
  1555	[34mbegin[39;49;00m$
  1556	  [36mResult[39;49;00m := UntilLastChar([36mExtractFileName[39;49;00m(FileName), [33m'[39;49;00m[33m.[39;49;00m[33m'[39;49;00m);$
  1557	[34mend[39;49;00m;$
  1558	$
  1559	[34mfunction[39;49;00m [32mExtractSuffix[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m): [34mstring[39;49;00m;$
  1560	[34mbegin[39;49;00m$
  1561	  [36mResult[39;49;00m := FromLastChar([36mExtractFileName[39;49;00m(FileName), [33m'[39;49;00m[33m.[39;49;00m[33m'[39;49;00m);$
  1562	[34mend[39;49;00m;$
  1563	$
  1564	[34mfunction[39;49;00m [32mSameByteA[39;49;00m([34mconst[39;49;00m A, B: TByteA): [36mBoolean[39;49;00m;$
  1565	[34mbegin[39;49;00m$
  1566	  [36mResult[39;49;00m := (A = B) [34mor[39;49;00m (([36mLength[39;49;00m(A) = [36mLength[39;49;00m(B)) [34mand[39;49;00m [36mCompareMem[39;49;00m(A, B, [36mLength[39;49;00m(A)));$
  1567	[34mend[39;49;00m;$
  1568	$
  1569	[34mfunction[39;49;00m [32mReverse[39;49;00m(A: TByteA): TByteA;$
  1570	[34mvar[39;49;00m$
  1571	  i: [36mInteger[39;49;00m;$
  1572	[34mbegin[39;49;00m$
  1573	  [36mSetLength[39;49;00m([36mResult[39;49;00m, [36mLength[39;49;00m(A));$
  1574	$
  1575	  [34mfor[39;49;00m i := [34m0[39;49;00m [34mto[39;49;00m [36mHigh[39;49;00m(A) [34mdo[39;49;00m$
  1576	    [36mResult[39;49;00m[[36mHigh[39;49;00m([36mResult[39;49;00m) - i] := A[i];$
  1577	[34mend[39;49;00m;$
  1578	$
  1579	[34mfunction[39;49;00m [32mEndian[39;49;00m(i: [36mInteger[39;49;00m): [36mInteger[39;49;00m;$
  1580	[34mtype[39;49;00m$
  1581	  EndianArray = [34mpacked[39;49;00m [34marray[39;49;00m[[34m0[39;49;00m..[34m3[39;49;00m] [34mof[39;49;00m [36mByte[39;49;00m;$
  1582	[34mvar[39;49;00m$
  1583	  a, b: EndianArray;$
  1584	[34mbegin[39;49;00m$
  1585	  a := EndianArray(i);$
  1586	  b[[34m0[39;49;00m] := a[[34m3[39;49;00m];$
  1587	  b[[34m1[39;49;00m] := a[[34m2[39;49;00m];$
  1588	  b[[34m2[39;49;00m] := a[[34m1[39;49;00m];$
  1589	  b[[34m3[39;49;00m] := a[[34m0[39;49;00m];$
  1590	  [36mResult[39;49;00m := [36mInteger[39;49;00m(b);$
  1591	[34mend[39;49;00m;$
  1592	$
  1593	[34mfunction[39;49;00m [32mSaveByteA[39;49;00m(Data: TByteA; [34mconst[39;49;00m FileName: [34mstring[39;49;00m;$
  1594	  Overwrite: [36mBoolean[39;49;00m = [34mTrue[39;49;00m): [36mBoolean[39;49;00m;$
  1595	[34mvar[39;49;00m$
  1596	  F: [34mfile[39;49;00m;$
  1597	[34mbegin[39;49;00m$
  1598	  [34mif[39;49;00m [36mFileExists[39;49;00m(FileName) [34mand[39;49;00m [34mnot[39;49;00m Overwrite [34mthen[39;49;00m [34mbegin[39;49;00m$
  1599	    [36mResult[39;49;00m := [34mFalse[39;49;00m;$
  1600	  [34mExit[39;49;00m [34mend[39;49;00m;$
  1601	$
  1602	  [36mAssignFile[39;49;00m(F, FileName);$
  1603	  [37m{$I-}[39;49;00m[36mRewrite[39;49;00m(F, [34m1[39;49;00m);[37m{$I+}[39;49;00m$
  1604	  [34mif[39;49;00m [36mIOResult[39;49;00m = [34m0[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m$
  1605	    [34mif[39;49;00m [36mLength[39;49;00m(Data) > [34m0[39;49;00m [34mthen[39;49;00m$
  1606	      [36mBlockWrite[39;49;00m(F, Data[[34m0[39;49;00m], [36mLength[39;49;00m(Data));$
  1607	    [36mCloseFile[39;49;00m(F);$
  1608	    [36mResult[39;49;00m := [34mTrue[39;49;00m;$
  1609	  [34mend[39;49;00m [34melse[39;49;00m$
  1610	    [36mResult[39;49;00m := [34mFalse[39;49;00m;$
  1611	[34mend[39;49;00m;$
  1612	$
  1613	[34mfunction[39;49;00m [32mLoadByteA[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m): TByteA;$
  1614	[34mvar[39;49;00m$
  1615	  F: [34mfile[39;49;00m;$
  1616	[34mbegin[39;49;00m$
  1617	  [36mAssignFile[39;49;00m(F, FileName);$
  1618	  [37m{$I-}[39;49;00m[36mReset[39;49;00m(F, [34m1[39;49;00m);[37m{$I+}[39;49;00m$
  1619	  [34mif[39;49;00m [36mIOResult[39;49;00m = [34m0[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m$
  1620	    [36mSetLength[39;49;00m([36mResult[39;49;00m, [36mFileSize[39;49;00m(F));$
  1621	    [34mif[39;49;00m [36mLength[39;49;00m([36mResult[39;49;00m) > [34m0[39;49;00m [34mthen[39;49;00m$
  1622	      [36mBlockRead[39;49;00m(F, [36mResult[39;49;00m[[34m0[39;49;00m], [36mFileSize[39;49;00m(F));$
  1623	    [36mCloseFile[39;49;00m(F);$
  1624	  [34mend[39;49;00m [34melse[39;49;00m$
  1625	    [36mSetLength[39;49;00m([36mResult[39;49;00m, [34m0[39;49;00m);$
  1626	[34mend[39;49;00m;$
  1627	$
  1628	[34mfunction[39;49;00m [32mIsValidFileName[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
  1629	[34mbegin[39;49;00m$
  1630	  [36mResult[39;49;00m := (FileName <> [33m'[39;49;00m[33m'[39;49;00m) [34mand[39;49;00m [34mnot[39;49;00m CharIn(FileName, FileNameEnemies)$
  1631	    [34mand[39;49;00m CharIn([36mTrim[39;49;00m(FileName), AllChars - [[33m'[39;49;00m[33m.[39;49;00m[33m'[39;49;00m]);$
  1632	[34mend[39;49;00m;$
  1633	$
  1634	[34mfunction[39;49;00m [32mMakeValidFileName[39;49;00m(FileName: [34mstring[39;49;00m; [34mconst[39;49;00m [34mDefault[39;49;00m: [34mstring[39;49;00m = [33m'[39;49;00m[33mFile[39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;$
  1635	[34mbegin[39;49;00m$
  1636	  [34mif[39;49;00m FileName = [33m'[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m$
  1637	    FileName := [34mDefault[39;49;00m;$
  1638	$
  1639	  [34mif[39;49;00m CharIn(FileName, FileNameEnemies) [34mthen[39;49;00m$
  1640	    [36mResult[39;49;00m := ReplaceChars(FileName, FileNameEnemies, [33m'[39;49;00m[33m_[39;49;00m[33m'[39;49;00m)$
  1641	  [34melse[39;49;00m [34mif[39;49;00m [34mnot[39;49;00m CharIn([36mTrim[39;49;00m(FileName), AllChars - [[33m'[39;49;00m[33m.[39;49;00m[33m'[39;49;00m]) [34mthen[39;49;00m$
  1642	    [36mResult[39;49;00m := [34mDefault[39;49;00m$
  1643	  [34melse[39;49;00m$
  1644	    [36mResult[39;49;00m := FileName;$
  1645	[34mend[39;49;00m;$
  1646	$
  1647	[34mfunction[39;49;00m [32mIsValidInteger[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
  1648	[37m{const[39;49;00m$
  1649	[37m  LowInt = '2147483648';[39;49;00m$
  1650	[37m  HighInt = '2147483647';[39;49;00m$
  1651	[37mvar[39;49;00m$
  1652	[37m  len, RealLen, i, o: Integer;[39;49;00m$
  1653	[37m  c: Char;[39;49;00m$
  1654	[37mbegin[39;49;00m$
  1655	[37m  Result := False;[39;49;00m$
  1656	[37m  if S = '' then[39;49;00m$
  1657	[37m    Exit;[39;49;00m$
  1658	[37m[39;49;00m$
  1659	[37m  len := Length(S);[39;49;00m$
  1660	[37m  o := 1;[39;49;00m$
  1661	[37m  [39;49;00m$
  1662	[37m  if S[1] = '-' then begin[39;49;00m$
  1663	[37m    if len = 1 then[39;49;00m$
  1664	[37m      Exit;[39;49;00m$
  1665	[37m    Inc(o);[39;49;00m$
  1666	[37m    while (o <= len) and (S[o] = '0') do[39;49;00m$
  1667	[37m      Inc(o);[39;49;00m$
  1668	[37m    if o > len then[39;49;00m$
  1669	[37m      Exit;[39;49;00m$
  1670	[37m    if o < len then begin[39;49;00m$
  1671	[37m      RealLen := len - o + 1;[39;49;00m$
  1672	[37m      if RealLen > Length(LowInt) then[39;49;00m$
  1673	[37m        Exit[39;49;00m$
  1674	[37m      else if RealLen = Length(LowInt) then begin[39;49;00m$
  1675	[37m        for i := 1 to Length(LowInt) do begin[39;49;00m$
  1676	[37m          c := S[i + o - 1];[39;49;00m$
  1677	[37m          if (c < '0') or (c > LowInt[i]) then[39;49;00m$
  1678	[37m            Exit;[39;49;00m$
  1679	[37m          if c in ['0'..Char((Byte(LowInt[i])-1))] then[39;49;00m$
  1680	[37m            Break;[39;49;00m$
  1681	[37m        end;[39;49;00m$
  1682	[37m        Inc(o, i);[39;49;00m$
  1683	[37m      end;[39;49;00m$
  1684	[37m    end;[39;49;00m$
  1685	[37m  end else begin[39;49;00m$
  1686	[37m    while (o <= len) and (S[o] = '0') do[39;49;00m$
  1687	[37m      Inc(o);[39;49;00m$
  1688	[37m    if o <= len then begin[39;49;00m$
  1689	[37m      RealLen := len - o + 1;[39;49;00m$
  1690	[37m      if RealLen > Length(HighInt) then[39;49;00m$
  1691	[37m        Exit[39;49;00m$
  1692	[37m      else if RealLen = Length(HighInt) then begin[39;49;00m$
  1693	[37m        for i := 1 to Length(HighInt) do begin[39;49;00m$
  1694	[37m          c := S[i + o - 1];[39;49;00m$
  1695	[37m          if (c < '0') or (c > HighInt[i]) then[39;49;00m$
  1696	[37m            Exit;[39;49;00m$
  1697	[37m          if c in ['0'..Char((Byte(HighInt[i])-1))] then[39;49;00m$
  1698	[37m            Break;[39;49;00m$
  1699	[37m        end;[39;49;00m$
  1700	[37m        Inc(o, i);[39;49;00m$
  1701	[37m      end;[39;49;00m$
  1702	[37m    end;[39;49;00m$
  1703	[37m  end;[39;49;00m$
  1704	[37m[39;49;00m$
  1705	[37m  for i := o to len do[39;49;00m$
  1706	[37m    if not (S[i] in ['0'..'9']) then[39;49;00m$
  1707	[37m      Exit;[39;49;00m$
  1708	[37m[39;49;00m$
  1709	[37m  Result := True;  }[39;49;00m$
  1710	[34mvar[39;49;00m$
  1711	  i: [36mInt64[39;49;00m;$
  1712	[34mbegin[39;49;00m$
  1713	  i := [36mStrToInt64Def[39;49;00m(S, [36mHigh[39;49;00m([36mInt64[39;49;00m));$
  1714	  [36mResult[39;49;00m := (i >= [36mLow[39;49;00m([36mInteger[39;49;00m)) [34mand[39;49;00m (i <= [36mHigh[39;49;00m([36mInteger[39;49;00m));$
  1715	[34mend[39;49;00m;$
  1716	$
  1717	[34mfunction[39;49;00m [32mIsValidCardinal[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
  1718	[37m{const[39;49;00m$
  1719	[37m  HighCard = '4294967295';[39;49;00m$
  1720	[37mvar[39;49;00m$
  1721	[37m  len, RealLen, i, o: Integer;[39;49;00m$
  1722	[37mbegin[39;49;00m$
  1723	[37m  Result := False;[39;49;00m$
  1724	[37m  if S = '' then[39;49;00m$
  1725	[37m    Exit;[39;49;00m$
  1726	[37m[39;49;00m$
  1727	[37m  len := Length(S);[39;49;00m$
  1728	[37m  o := 1;[39;49;00m$
  1729	[37m  [39;49;00m$
  1730	[37m  while (o <= len) and (S[o] = '0') do[39;49;00m$
  1731	[37m    Inc(o);[39;49;00m$
  1732	[37m  if o <= len then begin[39;49;00m$
  1733	[37m    RealLen := len - o + 1;[39;49;00m$
  1734	[37m    if RealLen > Length(HighCard) then[39;49;00m$
  1735	[37m      Exit[39;49;00m$
  1736	[37m    else if RealLen = Length(HighCard) then begin[39;49;00m$
  1737	[37m      for i := 1 to Length(HighCard) do begin[39;49;00m$
  1738	[37m        if S[i + o - 1] > HighCard[i] then[39;49;00m$
  1739	[37m          Exit;[39;49;00m$
  1740	[37m        if S[i + o - 1] in ['0'..Char((Byte(HighCard[i])-1))] then[39;49;00m$
  1741	[37m          Break;[39;49;00m$
  1742	[37m      end;[39;49;00m$
  1743	[37m      Inc(o, i);[39;49;00m$
  1744	[37m    end;[39;49;00m$
  1745	[37m  end;[39;49;00m$
  1746	[37m[39;49;00m$
  1747	[37m  for i := o to len do[39;49;00m$
  1748	[37m    if not (S[i] in ['0'..'9']) then[39;49;00m$
  1749	[37m      Exit;[39;49;00m$
  1750	[37m[39;49;00m$
  1751	[37m  Result := True;  }[39;49;00m$
  1752	[34mvar[39;49;00m$
  1753	  i: [36mInt64[39;49;00m;$
  1754	[34mbegin[39;49;00m$
  1755	  i := [36mStrToInt64Def[39;49;00m(S, -[34m1[39;49;00m);$
  1756	  [36mResult[39;49;00m := (i >= [34m0[39;49;00m) [34mand[39;49;00m (i <= [36mHigh[39;49;00m([36mCardinal[39;49;00m));$
  1757	[34mend[39;49;00m;$
  1758	$
  1759	[34mfunction[39;49;00m [32mStrOfBool[39;49;00m(flag: [36mBoolean[39;49;00m; [34mconst[39;49;00m TrueStr: [34mstring[39;49;00m = [33m'[39;49;00m[33mTrue[39;49;00m[33m'[39;49;00m;$
  1760	  [34mconst[39;49;00m FalseStr: [34mstring[39;49;00m = [33m'[39;49;00m[33mFalse[39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;$
  1761	[34mbegin[39;49;00m$
  1762	  [34mif[39;49;00m Flag [34mthen[39;49;00m$
  1763	    [36mResult[39;49;00m := TrueStr$
  1764	  [34melse[39;49;00m$
  1765	    [36mResult[39;49;00m := FalseStr;$
  1766	[34mend[39;49;00m;$
  1767	$
  1768	[34mfunction[39;49;00m [32mStrOfInt[39;49;00m(i: [36mInteger[39;49;00m): [34mstring[39;49;00m;$
  1769	[34mbegin[39;49;00m$
  1770	[37m{  if i = 0 then begin[39;49;00m$
  1771	[37m    Result := '0';[39;49;00m$
  1772	[37m  Exit end;[39;49;00m$
  1773	[37m[39;49;00m$
  1774	[37m  while i > 0 do begin[39;49;00m$
  1775	[37m    Result := Char(Byte('0') + (i mod 10)) + Result;[39;49;00m$
  1776	[37m    i := i div 10;[39;49;00m$
  1777	[37m  end;}[39;49;00m$
  1778	  [36mResult[39;49;00m := [36mIntToStr[39;49;00m(i);$
  1779	[34mend[39;49;00m;$
  1780	$
  1781	[34mfunction[39;49;00m [32mCardOfStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [36mCardinal[39;49;00m;$
  1782	[34mvar[39;49;00m$
  1783	  Res: [36mInt64[39;49;00m;$
  1784	[34mbegin[39;49;00m$
  1785	  Res := [36mStrToInt64Def[39;49;00m(S, -[34m1[39;49;00m);$
  1786	  [34mif[39;49;00m Res > [36mHigh[39;49;00m([36mCardinal[39;49;00m) [34mthen[39;49;00m$
  1787	    Res := [36mHigh[39;49;00m([36mCardinal[39;49;00m)$
  1788	  [34melse[39;49;00m [34mif[39;49;00m Res < [34m0[39;49;00m [34mthen[39;49;00m$
  1789	    Res := [34m0[39;49;00m;$
  1790	  [36mResult[39;49;00m := [36mCardinal[39;49;00m(Res);$
  1791	[34mend[39;49;00m;$
  1792	$
  1793	[34mfunction[39;49;00m [32mHexOrd[39;49;00m(Hex: [36mChar[39;49;00m): THex;$
  1794	[34mbegin[39;49;00m$
  1795	  [34mcase[39;49;00m Hex [34mof[39;49;00m$
  1796	    [33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m..[33m'[39;49;00m[33m9[39;49;00m[33m'[39;49;00m:$
  1797	      [36mResult[39;49;00m := [36mByte[39;49;00m(Hex) - [34m48[39;49;00m;$
  1798	    [33m'[39;49;00m[33mA[39;49;00m[33m'[39;49;00m..[33m'[39;49;00m[33mF[39;49;00m[33m'[39;49;00m:$
  1799	      [36mResult[39;49;00m := [36mByte[39;49;00m(Hex) - [34m55[39;49;00m;$
  1800	    [33m'[39;49;00m[33ma[39;49;00m[33m'[39;49;00m..[33m'[39;49;00m[33mf[39;49;00m[33m'[39;49;00m:$
  1801	      [36mResult[39;49;00m := [36mByte[39;49;00m(Hex) - [34m87[39;49;00m;$
  1802	    [34melse[39;49;00m$
  1803	      [36mResult[39;49;00m := [34m0[39;49;00m;$
  1804	  [34mend[39;49;00m;$
  1805	[34mend[39;49;00m;$
  1806	$
  1807	[34mfunction[39;49;00m [32mByteOfHex[39;49;00m(Hex: THexByteStr): [36mByte[39;49;00m;$
  1808	[34mbegin[39;49;00m$
  1809	  [36mResult[39;49;00m := (HexOrd(Hex[[34m1[39;49;00m]) [34mshl[39;49;00m [34m4[39;49;00m) + HexOrd(Hex[[34m2[39;49;00m]);$
  1810	[34mend[39;49;00m;$
  1811	$
  1812	[34mfunction[39;49;00m [32mDecOfHex[39;49;00m([34mconst[39;49;00m Hex: [34mstring[39;49;00m): [34mstring[39;49;00m;$
  1813	[34mbegin[39;49;00m$
  1814	  [36mResult[39;49;00m := [36mIntToStr[39;49;00m(CardOfHex(Hex));$
  1815	[34mend[39;49;00m;$
  1816	$
  1817	[34mfunction[39;49;00m [32mHexOfByte[39;49;00m(b: [36mByte[39;49;00m): THexByteStr;$
  1818	[34mbegin[39;49;00m$
  1819	  [36mResult[39;49;00m := HexChar[(b [34mand[39;49;00m [34m$F0[39;49;00m) [34mshr[39;49;00m [34m4[39;49;00m]$
  1820	          + HexChar[ b [34mand[39;49;00m [34m$0F[39;49;00m       ];$
  1821	[34mend[39;49;00m;$
  1822	$
  1823	[37m{function HexOfCard2(c: Cardinal): string;[39;49;00m$
  1824	[37mvar[39;49;00m$
  1825	[37m  Data: array[0..(1 shl 4) - 1] of Char;[39;49;00m$
  1826	[37m  i: Integer;[39;49;00m$
  1827	[37mbegin[39;49;00m$
  1828	[37m  for i := 0 to (1 shl 4) - 1 do[39;49;00m$
  1829	[37m    if i < 10 then[39;49;00m$
  1830	[37m      Data[i] := Char(Ord('0') + i)[39;49;00m$
  1831	[37m    else[39;49;00m$
  1832	[37m      Data[i] := Char(Ord('A') + i - 10);[39;49;00m$
  1833	[37m[39;49;00m$
  1834	[37m  Result := Data[(c and (((1 shl (1 shl 2)) - 1) shl (7 shl 2))) shr (7 shl 2)][39;49;00m$
  1835	[37m          + Data[(c and (((1 shl (1 shl 2)) - 1) shl (6 shl 2))) shr (6 shl 2)][39;49;00m$
  1836	[37m          + Data[(c and (((1 shl (1 shl 2)) - 1) shl (5 shl 2))) shr (5 shl 2)][39;49;00m$
  1837	[37m          + Data[(c and (((1 shl (1 shl 2)) - 1) shl (4 shl 2))) shr (4 shl 2)][39;49;00m$
  1838	[37m          + Data[(c and (((1 shl (1 shl 2)) - 1) shl (3 shl 2))) shr (3 shl 2)][39;49;00m$
  1839	[37m          + Data[(c and (((1 shl (1 shl 2)) - 1) shl (2 shl 2))) shr (2 shl 2)][39;49;00m$
  1840	[37m          + Data[(c and (((1 shl (1 shl 2)) - 1) shl (1 shl 2))) shr (1 shl 2)][39;49;00m$
  1841	[37m          + Data[(c and (((1 shl (1 shl 2)) - 1) shl (0 shl 2))) shr (0 shl 2)];[39;49;00m$
  1842	[37mend; }[39;49;00m$
  1843	$
  1844	[34mfunction[39;49;00m [32mHexOfCard[39;49;00m(i: [36mCardinal[39;49;00m): [34mstring[39;49;00m;$
  1845	[34mvar[39;49;00m$
  1846	  a: [36mCardinal[39;49;00m;$
  1847	[34mbegin[39;49;00m$
  1848	  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
  1849	  [34mwhile[39;49;00m i > [34m0[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m$
  1850	    a := i [34mand[39;49;00m [34m$F[39;49;00m;$
  1851	    [36mResult[39;49;00m := HexChar[a] + [36mResult[39;49;00m;$
  1852	    i := i [34mshr[39;49;00m [34m4[39;49;00m;$
  1853	  [34mend[39;49;00m;$
  1854	[34mend[39;49;00m;$
  1855	$
  1856	[34mfunction[39;49;00m [32mHexOfCard[39;49;00m(i: [36mCardinal[39;49;00m; Digits: [36mInteger[39;49;00m): [34mstring[39;49;00m;$
  1857	[34mvar[39;49;00m$
  1858	  a: [36mCardinal[39;49;00m;$
  1859	[34mbegin[39;49;00m$
  1860	  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
  1861	  [34mwhile[39;49;00m i > [34m0[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m$
  1862	    a := i [34mand[39;49;00m [34m$F[39;49;00m;$
  1863	    [36mResult[39;49;00m := HexChar[a] + [36mResult[39;49;00m;$
  1864	    i := i [34mshr[39;49;00m [34m4[39;49;00m;$
  1865	  [34mend[39;49;00m;$
  1866	  [36mResult[39;49;00m := MulStr([33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m, Digits - [36mLength[39;49;00m([36mResult[39;49;00m)) + [36mResult[39;49;00m;$
  1867	[34mend[39;49;00m;$
  1868	$
  1869	[34mfunction[39;49;00m [32mPascalHexArray[39;49;00m(a: TByteA; [34mName[39;49;00m: [34mstring[39;49;00m): [34mstring[39;49;00m;$
  1870	[34mvar[39;49;00m$
  1871	  i, len: [36mInteger[39;49;00m;$
  1872	[34mbegin[39;49;00m$
  1873	  [36mResult[39;49;00m := [33m'[39;49;00m[33mconst[39;49;00m[33m'[39;49;00m + EOL +$
  1874	    [33m'[39;49;00m[33m  [39;49;00m[33m'[39;49;00m + Name + [33m'[39;49;00m[33m: array[0..[39;49;00m[33m'[39;49;00m + [36mIntToStr[39;49;00m([36mHigh[39;49;00m(a)) + [33m'[39;49;00m[33m] of Byte = ([39;49;00m[33m'[39;49;00m;$
  1875	$
  1876	  len := [36mLength[39;49;00m(a);$
  1877	  [34mfor[39;49;00m i := [34m0[39;49;00m [34mto[39;49;00m len-[34m1[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m$
  1878	    [34mif[39;49;00m (i [34mmod[39;49;00m [34m19[39;49;00m) = [34m0[39;49;00m [34mthen[39;49;00m$
  1879	      [36mResult[39;49;00m := [36mResult[39;49;00m + EOL + [33m'[39;49;00m[33m  [39;49;00m[33m'[39;49;00m + [33m'[39;49;00m[33m  [39;49;00m[33m'[39;49;00m;$
  1880	    [36mResult[39;49;00m := [36mResult[39;49;00m + [33m'[39;49;00m[33m$[39;49;00m[33m'[39;49;00m + HexOfByte(a[i]);$
  1881	    [34mif[39;49;00m i < len-[34m1[39;49;00m [34mthen[39;49;00m$
  1882	      [36mResult[39;49;00m := [36mResult[39;49;00m + [33m'[39;49;00m[33m,[39;49;00m[33m'[39;49;00m;$
  1883	  [34mend[39;49;00m;$
  1884	  [36mResult[39;49;00m := [36mResult[39;49;00m + EOL + [33m'[39;49;00m[33m  );[39;49;00m[33m'[39;49;00m;$
  1885	[34mend[39;49;00m;$
  1886	$
  1887	[34mfunction[39;49;00m [32mHexOfByteA[39;49;00m(a: TByteA; Blocks: [36mInteger[39;49;00m = [34m1[39;49;00m;$
  1888	  [34mconst[39;49;00m Splitter: [34mstring[39;49;00m = [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;$
  1889	[34mvar[39;49;00m$
  1890	  i: [36mInteger[39;49;00m;$
  1891	[34mbegin[39;49;00m$
  1892	  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
  1893	$
  1894	  [34mif[39;49;00m Blocks > [34m0[39;49;00m [34mthen[39;49;00m$
  1895	    [34mfor[39;49;00m i := [34m0[39;49;00m [34mto[39;49;00m [36mHigh[39;49;00m(a) [34mdo[39;49;00m [34mbegin[39;49;00m$
  1896	      [36mResult[39;49;00m := [36mResult[39;49;00m + HexOfByte(a[i]);$
  1897	      [34mif[39;49;00m i < [36mHigh[39;49;00m(a) [34mthen[39;49;00m$
  1898	        [34mif[39;49;00m ((i+[34m1[39;49;00m) [34mmod[39;49;00m Blocks) = [34m0[39;49;00m [34mthen[39;49;00m$
  1899	          [36mResult[39;49;00m := [36mResult[39;49;00m + Splitter;$
  1900	    [34mend[39;49;00m$
  1901	  [34melse[39;49;00m$
  1902	    [34mfor[39;49;00m i := [34m0[39;49;00m [34mto[39;49;00m [36mHigh[39;49;00m(a) [34mdo[39;49;00m$
  1903	      [36mResult[39;49;00m := [36mResult[39;49;00m + HexOfByte(a[i]);$
  1904	[34mend[39;49;00m;$
  1905	$
  1906	[34mfunction[39;49;00m [32mBinOfByteA[39;49;00m(a: TByteA; Blocks: [36mInteger[39;49;00m = [34m4[39;49;00m;$
  1907	  [34mconst[39;49;00m Splitter: [34mstring[39;49;00m = [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;$
  1908	[34mvar[39;49;00m$
  1909	  i, [36mmax[39;49;00m: [36mInteger[39;49;00m;$
  1910	  Bit: [36mBoolean[39;49;00m;$
  1911	[34mbegin[39;49;00m$
  1912	  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
  1913	$
  1914	  [34mif[39;49;00m Blocks > [34m0[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m$
  1915	    [36mmax[39;49;00m := [34m8[39;49;00m * ([36mHigh[39;49;00m(a)) + [34m7[39;49;00m;$
  1916	    [34mfor[39;49;00m i := [34m0[39;49;00m [34mto[39;49;00m [36mmax[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m$
  1917	      Bit := [34m7[39;49;00m-(i [34mmod[39;49;00m [34m8[39;49;00m) [34min[39;49;00m TBitSet(a[i [34mdiv[39;49;00m [34m8[39;49;00m]);$
  1918	      [36mResult[39;49;00m := [36mResult[39;49;00m + [36mChar[39;49;00m([36mByte[39;49;00m([33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m) + [36mByte[39;49;00m(Bit));$
  1919	      [34mif[39;49;00m i < [36mmax[39;49;00m [34mthen[39;49;00m$
  1920	        [34mif[39;49;00m ((i+[34m1[39;49;00m) [34mmod[39;49;00m Blocks) = [34m0[39;49;00m [34mthen[39;49;00m$
  1921	          [36mResult[39;49;00m := [36mResult[39;49;00m + Splitter;$
  1922	    [34mend[39;49;00m;$
  1923	  [34mend[39;49;00m [34melse[39;49;00m$
  1924	    [34mfor[39;49;00m i := [34m0[39;49;00m [34mto[39;49;00m [36mHigh[39;49;00m(a) [34mdo[39;49;00m$
  1925	      [36mResult[39;49;00m := [36mResult[39;49;00m + [36mChar[39;49;00m([36mByte[39;49;00m([33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m) + a[i] [34mshr[39;49;00m (i [34mand[39;49;00m [34m8[39;49;00m));$
  1926	[34mend[39;49;00m;$
  1927	$
  1928	[34mfunction[39;49;00m [32mCardOfHex[39;49;00m(Hex: [34mstring[39;49;00m): [36mCardinal[39;49;00m;$
  1929	[34mvar[39;49;00m$
  1930	  i: [36mInteger[39;49;00m;$
  1931	[34mbegin[39;49;00m$
  1932	  [36mResult[39;49;00m := [34m0[39;49;00m;$
  1933	  Hex := [36mCopy[39;49;00m(ExtractChars(Hex, HexadecimalChars), [34m1[39;49;00m, [34m8[39;49;00m);$
  1934	$
  1935	  [34mfor[39;49;00m i := [34m1[39;49;00m [34mto[39;49;00m [36mLength[39;49;00m(Hex) [34mdo[39;49;00m$
  1936	    [34mif[39;49;00m Hex[i] <> [33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m$
  1937	      [36mInc[39;49;00m([36mResult[39;49;00m, HexOrd(Hex[i]) [34mshl[39;49;00m (([36mLength[39;49;00m(Hex) - i) [34mshl[39;49;00m [34m2[39;49;00m));$
  1938	[34mend[39;49;00m;$
  1939	$
  1940	[34mfunction[39;49;00m [32mIntOfBin[39;49;00m(Bin: [34mstring[39;49;00m): [36mCardinal[39;49;00m;$
  1941	[34mvar[39;49;00m$
  1942	  i: [36mInteger[39;49;00m;$
  1943	[34mbegin[39;49;00m$
  1944	  [36mResult[39;49;00m := [34m0[39;49;00m;$
  1945	  Bin := [36mCopy[39;49;00m(ExtractChars(Bin, BinaryChars), [34m1[39;49;00m, [34m32[39;49;00m);$
  1946	$
  1947	  [34mfor[39;49;00m i := [36mLength[39;49;00m(Bin) [34mdownto[39;49;00m [34m1[39;49;00m [34mdo[39;49;00m$
  1948	    [34mif[39;49;00m Bin[i] = [33m'[39;49;00m[33m1[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m$
  1949	      [36mInc[39;49;00m([36mResult[39;49;00m, [34m1[39;49;00m [34mshl[39;49;00m ([36mLength[39;49;00m(Bin) - i));$
  1950	[34mend[39;49;00m;$
  1951	$
  1952	[34mfunction[39;49;00m [32mBinOfInt[39;49;00m(n: [36mCardinal[39;49;00m): [34mstring[39;49;00m;$
  1953	[34mvar[39;49;00m$
  1954	  a: [36mInteger[39;49;00m;$
  1955	[34mbegin[39;49;00m$
  1956	  [34mif[39;49;00m n = [34m0[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m$
  1957	    [36mResult[39;49;00m := [33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m;$
  1958	  [34mexit[39;49;00m; [34mend[39;49;00m;$
  1959	$
  1960	  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
  1961	  [34mwhile[39;49;00m n > [34m0[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m$
  1962	    a := n [34mand[39;49;00m [34m1[39;49;00m;$
  1963	    [36mResult[39;49;00m := [36mChar[39;49;00m(a + [36mByte[39;49;00m([33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m)) + [36mResult[39;49;00m;$
  1964	    n := n [34mshr[39;49;00m [34m1[39;49;00m;$
  1965	  [34mend[39;49;00m;$
  1966	[34mend[39;49;00m;$
  1967	$
  1968	[34mfunction[39;49;00m [32mBinOfIntFill[39;49;00m(n: [36mCardinal[39;49;00m; MinCount: [36mInteger[39;49;00m = [34m8[39;49;00m): [34mstring[39;49;00m;$
  1969	[34mvar[39;49;00m$
  1970	  a: [36mInteger[39;49;00m;$
  1971	[34mbegin[39;49;00m$
  1972	  [34mif[39;49;00m n = [34m0[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m$
  1973	    [36mResult[39;49;00m := MulStr([33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m, MinCount);$
  1974	  [34mExit[39;49;00m; [34mend[39;49;00m;$
  1975	$
  1976	  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
  1977	  [34mwhile[39;49;00m n > [34m0[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m$
  1978	    a := n [34mand[39;49;00m [34m1[39;49;00m;$
  1979	    [36mResult[39;49;00m := [36mChar[39;49;00m(a + [36mByte[39;49;00m([33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m)) + [36mResult[39;49;00m;$
  1980	    n := n [34mshr[39;49;00m [34m1[39;49;00m;$
  1981	  [34mend[39;49;00m;$
  1982	  [36mResult[39;49;00m := MulStr([33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m, MinCount - [36mLength[39;49;00m([36mResult[39;49;00m)) + [36mResult[39;49;00m;$
  1983	[34mend[39;49;00m;$
  1984	$
  1985	[34mfunction[39;49;00m [32mBaseNOfInt[39;49;00m(I: [36mCardinal[39;49;00m; B: TBaseN): [34mstring[39;49;00m;$
  1986	[34mvar[39;49;00m$
  1987	  a: [36mInteger[39;49;00m;$
  1988	[34mbegin[39;49;00m$
  1989	  [34mif[39;49;00m (B < [34m2[39;49;00m) [34mor[39;49;00m (i = [34m0[39;49;00m) [34mthen[39;49;00m [34mbegin[39;49;00m$
  1990	    [36mResult[39;49;00m := [33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m;$
  1991	  [34mExit[39;49;00m; [34mend[39;49;00m;$
  1992	$
  1993	  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
  1994	  [34mwhile[39;49;00m i > [34m0[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m$
  1995	    a := i [34mmod[39;49;00m B;$
  1996	    [36mResult[39;49;00m := BaseNChar[a] + [36mResult[39;49;00m;$
  1997	    i := i [34mdiv[39;49;00m B;$
  1998	  [34mend[39;49;00m;$
  1999	[34mend[39;49;00m;$
  2000	$
  2001	[34mfunction[39;49;00m [32mIntOfBaseN[39;49;00m(V: [34mstring[39;49;00m; B: TBaseN): [36mCardinal[39;49;00m;$
  2002	[34mvar[39;49;00m$
  2003	  i: [36mInteger[39;49;00m;$
  2004	  F: [36mCardinal[39;49;00m;$
  2005	  c: [36mByte[39;49;00m;$
  2006	[34mbegin[39;49;00m$
  2007	  [36mResult[39;49;00m := [34m0[39;49;00m;$
  2008	  V := TrimAll(V);$
  2009	  F := [34m1[39;49;00m;$
  2010	  [34mfor[39;49;00m i := [36mLength[39;49;00m(V) [34mdownto[39;49;00m [34m1[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m$
  2011	    c := [36mByte[39;49;00m([36mUpCase[39;49;00m(V[i]));$
  2012	    [34mcase[39;49;00m [36mChar[39;49;00m(c) [34mof[39;49;00m$
  2013	      [33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m..[33m'[39;49;00m[33m9[39;49;00m[33m'[39;49;00m: c := c - [34m48[39;49;00m;$
  2014	      [33m'[39;49;00m[33mA[39;49;00m[33m'[39;49;00m..[33m'[39;49;00m[33mZ[39;49;00m[33m'[39;49;00m: c := c - [34m55[39;49;00m;$
  2015	    [34mend[39;49;00m;$
  2016	    [34mif[39;49;00m c < B [34mthen[39;49;00m$
  2017	      [36mResult[39;49;00m := [36mResult[39;49;00m + [36mByte[39;49;00m(c) * F;$
  2018	    F := F * B;$
  2019	  [34mend[39;49;00m;$
  2020	[34mend[39;49;00m;$
  2021	$
  2022	[34mfunction[39;49;00m [32mKeepIn[39;49;00m(i, Bottom, Top: [36mVariant[39;49;00m): [36mVariant[39;49;00m;$
  2023	[34mbegin[39;49;00m$
  2024	  [36mResult[39;49;00m := i;$
  2025	  [34mif[39;49;00m [36mResult[39;49;00m > Top [34mthen[39;49;00m$
  2026	    [36mResult[39;49;00m := Top$
  2027	  [34melse[39;49;00m [34mif[39;49;00m [36mResult[39;49;00m < Bottom [34mthen[39;49;00m$
  2028	    [36mResult[39;49;00m := Bottom;$
  2029	[34mend[39;49;00m;$
  2030	$
  2031	[34mfunction[39;49;00m [32mInRange[39;49;00m(Value, Bottom, Top: [36mVariant[39;49;00m): [36mBoolean[39;49;00m;$
  2032	[34mbegin[39;49;00m$
  2033	  [36mResult[39;49;00m := (Value >= Bottom) [34mand[39;49;00m (Value <= Top);$
  2034	[34mend[39;49;00m;$
  2035	$
  2036	[34mfunction[39;49;00m [32mInStrictRange[39;49;00m(Value, Bottom, Top: [36mVariant[39;49;00m): [36mBoolean[39;49;00m;$
  2037	[34mbegin[39;49;00m$
  2038	  [36mResult[39;49;00m := (Value > Bottom) [34mand[39;49;00m (Value < Top);$
  2039	[34mend[39;49;00m;$
  2040	$
  2041	[34mfunction[39;49;00m [32mMin[39;49;00m([34mconst[39;49;00m A, B: [36mInteger[39;49;00m): [36mInteger[39;49;00m;$
  2042	[34mbegin[39;49;00m$
  2043	  [34mif[39;49;00m A < B [34mthen[39;49;00m$
  2044	    [36mResult[39;49;00m := A$
  2045	  [34melse[39;49;00m$
  2046	    [36mResult[39;49;00m := B;$
  2047	[34mend[39;49;00m;$
  2048	$
  2049	[34mfunction[39;49;00m [32mMin[39;49;00m([34mconst[39;49;00m A: TIntA): [36mInteger[39;49;00m;$
  2050	[34mvar[39;49;00m$
  2051	  i: [36mInteger[39;49;00m;$
  2052	[34mbegin[39;49;00m$
  2053	  [36mResult[39;49;00m := [34m0[39;49;00m;$
  2054	  [34mif[39;49;00m [36mLength[39;49;00m(A) = [34m0[39;49;00m [34mthen[39;49;00m$
  2055	    [34mExit[39;49;00m;$
  2056	$
  2057	  [36mResult[39;49;00m := A[[34m0[39;49;00m];$
  2058	  [34mfor[39;49;00m i := [34m1[39;49;00m [34mto[39;49;00m [36mHigh[39;49;00m(A) [34mdo[39;49;00m$
  2059	    [34mif[39;49;00m A[i] < [36mResult[39;49;00m [34mthen[39;49;00m$
  2060	      [36mResult[39;49;00m := A[i];$
  2061	[34mend[39;49;00m;$
  2062	$
  2063	[34mfunction[39;49;00m [32mMax[39;49;00m([34mconst[39;49;00m A, B: [36mInteger[39;49;00m): [36mInteger[39;49;00m;$
  2064	[34mbegin[39;49;00m$
  2065	  [34mif[39;49;00m A > B [34mthen[39;49;00m$
  2066	    [36mResult[39;49;00m := A$
  2067	  [34melse[39;49;00m$
  2068	    [36mResult[39;49;00m := B;$
  2069	[34mend[39;49;00m;$
  2070	$
  2071	[34mfunction[39;49;00m [32mMax[39;49;00m([34mconst[39;49;00m A: TIntA): [36mInteger[39;49;00m;$
  2072	[34mvar[39;49;00m$
  2073	  i: [36mInteger[39;49;00m;$
  2074	[34mbegin[39;49;00m$
  2075	  [36mResult[39;49;00m := [34m0[39;49;00m;$
  2076	  [34mif[39;49;00m [36mLength[39;49;00m(A) = [34m0[39;49;00m [34mthen[39;49;00m$
  2077	    [34mExit[39;49;00m;$
  2078	$
  2079	  [36mResult[39;49;00m := A[[34m0[39;49;00m];$
  2080	  [34mfor[39;49;00m i := [34m1[39;49;00m [34mto[39;49;00m [36mHigh[39;49;00m(A) [34mdo[39;49;00m$
  2081	    [34mif[39;49;00m A[i] > [36mResult[39;49;00m [34mthen[39;49;00m$
  2082	      [36mResult[39;49;00m := A[i];$
  2083	[34mend[39;49;00m;$
  2084	$
  2085	[34mfunction[39;49;00m [32mRangesOfStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): TRanges;$
  2086	[34mvar[39;49;00m$
  2087	  SL: TStringList;$
  2088	  r, b, t: [34mstring[39;49;00m;$
  2089	  i, p: [36mInteger[39;49;00m;$
  2090	$
  2091	  [34mfunction[39;49;00m [32mTryStrToCard[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; out Value: [36mCardinal[39;49;00m): [36mBoolean[39;49;00m;$
  2092	  [34mvar[39;49;00m$
  2093	    E: [36mInteger[39;49;00m;$
  2094	  [34mbegin[39;49;00m$
  2095	    [36mVal[39;49;00m(S, Value, E);$
  2096	    [36mResult[39;49;00m := E = [34m0[39;49;00m;$
  2097	  [34mend[39;49;00m;$
  2098	$
  2099	[34mbegin[39;49;00m$
  2100	  [36mResult[39;49;00m := [34mnil[39;49;00m;$
  2101	  SL := TStringList.Create;$
  2102	  [34mtry[39;49;00m$
  2103	    Split(S, RangesSeparator, SL);$
  2104	    [36mSetLength[39;49;00m([36mResult[39;49;00m, SL.Count);$
  2105	    [34mfor[39;49;00m i := [34m0[39;49;00m [34mto[39;49;00m SL.Count-[34m1[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m$
  2106	      r := SL[i];$
  2107	      [34mwith[39;49;00m [36mResult[39;49;00m[i] [34mdo[39;49;00m [34mbegin[39;49;00m$
  2108	        p := CharPos(RangeInnerSeparator, r);$
  2109	        Simple := p = [34m0[39;49;00m; [37m// no '-' found[39;49;00m$
  2110	        [34mif[39;49;00m Simple [34mthen[39;49;00m [34mbegin[39;49;00m$
  2111	          [34mif[39;49;00m r = RangeInfinite [34mthen[39;49;00m [34mbegin[39;49;00m [37m// * --> *-*[39;49;00m$
  2112	            Simple := [34mFalse[39;49;00m;$
  2113	            Bottom := [36mLow[39;49;00m(Bottom);$
  2114	            Top := [36mHigh[39;49;00m(Top);$
  2115	          [34mend[39;49;00m [34melse[39;49;00m [34mif[39;49;00m [34mnot[39;49;00m TryStrToCard(r, Value) [34mthen[39;49;00m$
  2116	            [34mBreak[39;49;00m;$
  2117	$
  2118	        [34mend[39;49;00m [34melse[39;49;00m [34mbegin[39;49;00m$
  2119	          TileStr(r, p, p, b, t);$
  2120	$
  2121	          [34mif[39;49;00m b = RangeInfinite [34mthen[39;49;00m$
  2122	            Bottom := [36mLow[39;49;00m(Bottom)$
  2123	          [34melse[39;49;00m [34mif[39;49;00m [34mnot[39;49;00m TryStrToCard(b, Bottom) [34mthen[39;49;00m$
  2124	            [34mBreak[39;49;00m;$
  2125	$
  2126	          [34mif[39;49;00m t = RangeInfinite [34mthen[39;49;00m$
  2127	            Top := [36mHigh[39;49;00m(Top)$
  2128	          [34melse[39;49;00m [34mif[39;49;00m [34mnot[39;49;00m TryStrToCard(t, Top) [34mthen[39;49;00m$
  2129	            [34mBreak[39;49;00m;$
  2130	          [34mif[39;49;00m Bottom > Top [34mthen[39;49;00m [34mbegin[39;49;00m$
  2131	            p := Bottom; Bottom := Top; Top := p;$
  2132	          [34mend[39;49;00m;$
  2133	        [34mend[39;49;00m;$
  2134	      [34mend[39;49;00m;$
  2135	    [34mend[39;49;00m;$
  2136	$
  2137	    [34mif[39;49;00m i <> SL.Count [34mthen[39;49;00m$
  2138	      [36mResult[39;49;00m := [34mnil[39;49;00m;$
  2139	$
  2140	  [34mfinally[39;49;00m$
  2141	    SL.Free;$
  2142	  [34mend[39;49;00m;$
  2143	[34mend[39;49;00m;$
  2144	$
  2145	[34mfunction[39;49;00m [32mInRanges[39;49;00m(Ranges: TRanges; TestValue: [36mCardinal[39;49;00m): [36mBoolean[39;49;00m;$
  2146	[34mvar[39;49;00m$
  2147	  i: [36mInteger[39;49;00m;$
  2148	[34mbegin[39;49;00m$
  2149	  [36mResult[39;49;00m := [34mTrue[39;49;00m;$
  2150	$
  2151	  [34mfor[39;49;00m i := [34m0[39;49;00m [34mto[39;49;00m [36mHigh[39;49;00m(Ranges) [34mdo[39;49;00m$
  2152	    [34mwith[39;49;00m Ranges[i] [34mdo[39;49;00m$
  2153	      [34mif[39;49;00m Simple [34mthen[39;49;00m [34mbegin[39;49;00m$
  2154	        [34mif[39;49;00m TestValue = Value [34mthen[39;49;00m$
  2155	          [34mExit[39;49;00m;$
  2156	      [34mend[39;49;00m [34melse[39;49;00m [34mbegin[39;49;00m$
  2157	        [34mif[39;49;00m [36mInRange[39;49;00m(TestValue, Bottom, Top) [34mthen[39;49;00m$
  2158	          [34mExit[39;49;00m;$
  2159	      [34mend[39;49;00m;$
  2160	$
  2161	  [36mResult[39;49;00m := [34mFalse[39;49;00m;$
  2162	[34mend[39;49;00m;$
  2163	$
  2164	[34mprocedure[39;49;00m [32mWriteSL[39;49;00m(Strings: TStrings; [34mconst[39;49;00m Prefix: [34mstring[39;49;00m = [33m'[39;49;00m[33m'[39;49;00m;$
  2165	  [34mconst[39;49;00m Suffix: [34mstring[39;49;00m = [33m'[39;49;00m[33m'[39;49;00m);$
  2166	[34mvar[39;49;00m$
  2167	  i: [36mInteger[39;49;00m;$
  2168	[34mbegin[39;49;00m$
  2169	  [34mfor[39;49;00m i := [34m0[39;49;00m [34mto[39;49;00m Strings.Count-[34m1[39;49;00m [34mdo[39;49;00m$
  2170	    [36mWriteLn[39;49;00m(Prefix + Strings[i] + Suffix);$
  2171	[34mend[39;49;00m;$
  2172	$
  2173	[34mfunction[39;49;00m [32mSuccess[39;49;00m(Res: [36mInteger[39;49;00m; ResultOnSuccess: [36mInteger[39;49;00m = ERROR_SUCCESS): [36mBoolean[39;49;00m;$
  2174	[34mbegin[39;49;00m$
  2175	  [36mResult[39;49;00m := (Res = ResultOnSuccess);$
  2176	  LastSuccessRes := Res;$
  2177	[34mend[39;49;00m;$
  2178	$
  2179	[34mfunction[39;49;00m [32mFailure[39;49;00m(Res: [36mInteger[39;49;00m; ResultOnSuccess: [36mInteger[39;49;00m = ERROR_SUCCESS): [36mBoolean[39;49;00m;$
  2180	[34mbegin[39;49;00m$
  2181	  [36mResult[39;49;00m := [34mnot[39;49;00m Success(Res, ResultOnSuccess);$
  2182	[34mend[39;49;00m;$
  2183	$
  2184	[34mfunction[39;49;00m [32mExpandString[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [34mstring[39;49;00m;$
  2185	[34mvar[39;49;00m$
  2186	  Len: [36mInteger[39;49;00m;$
  2187	  P, Res: [36mPChar[39;49;00m;$
  2188	[34mbegin[39;49;00m$
  2189	  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
  2190	  P := [36mPChar[39;49;00m(S);$
  2191	  Len := ExpandEnvironmentStrings(P, [34mnil[39;49;00m, [34m0[39;49;00m);$
  2192	  [34mif[39;49;00m Len = [34m0[39;49;00m [34mthen[39;49;00m$
  2193	    [34mExit[39;49;00m;$
  2194	$
  2195	  [36mGetMem[39;49;00m(Res, Len);$
  2196	  ExpandEnvironmentStrings(P, Res, Len);$
  2197	$
  2198	  [36mResult[39;49;00m := Res;$
  2199	  [36mFreeMem[39;49;00m(Res, Len);$
  2200	[34mend[39;49;00m;$
  2201	$
  2202	[34mfunction[39;49;00m [32mFindAll[39;49;00m(Strings: TStrings; [34mconst[39;49;00m Mask: [34mstring[39;49;00m;$
  2203	  ScanSubDirs: [36mBoolean[39;49;00m = [34mTrue[39;49;00m; Attributes: [36mInteger[39;49;00m = faFindEveryFile;$
  2204	  FileReturn: TFileNameFunc = [34mnil[39;49;00m): [36mBoolean[39;49;00m;$
  2205	[34mvar[39;49;00m$
  2206	  Path, FileName: [34mstring[39;49;00m;$
  2207	$
  2208	  [34mprocedure[39;49;00m [32mScanDir[39;49;00m([34mconst[39;49;00m Path, FileName: [34mstring[39;49;00m);$
  2209	  [34mvar[39;49;00m$
  2210	    PSR: TSearchRec;$
  2211	    Res: [36mInteger[39;49;00m;$
  2212	$
  2213	    [34mprocedure[39;49;00m [32mAdd[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m);$
  2214	    [34mbegin[39;49;00m$
  2215	      [34mif[39;49;00m S <> [33m'[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m$
  2216	        Strings.Add(S);$
  2217	    [34mend[39;49;00m;$
  2218	$
  2219	  [34mbegin[39;49;00m$
  2220	    Res := [36mFindFirst[39;49;00m(Path + FileName, Attributes, PSR);$
  2221	    [34mwhile[39;49;00m Success(Res, [34m0[39;49;00m) [34mdo[39;49;00m [34mbegin[39;49;00m$
  2222	      [34mif[39;49;00m [36mAssigned[39;49;00m(FileReturn) [34mthen[39;49;00m$
  2223	        Add(FileReturn(Path + PSR.Name))$
  2224	      [34melse[39;49;00m$
  2225	        Add(Path + PSR.Name);$
  2226	      Res := [36mFindNext[39;49;00m(PSR);$
  2227	    [34mend[39;49;00m;$
  2228	    [36mFindClose[39;49;00m(PSR);$
  2229	    [34mif[39;49;00m [34mnot[39;49;00m ScanSubDirs [34mthen[39;49;00m$
  2230	      [34mExit[39;49;00m;$
  2231	$
  2232	    Res := [36mFindFirst[39;49;00m(Path + [33m'[39;49;00m[33m*[39;49;00m[33m'[39;49;00m, faDirectory, PSR);$
  2233	    [34mwhile[39;49;00m Success(Res, [34m0[39;49;00m) [34mdo[39;49;00m [34mbegin[39;49;00m$
  2234	      [34mif[39;49;00m (PSR.Attr [34mand[39;49;00m faDirectory > [34m0[39;49;00m)$
  2235	       [34mand[39;49;00m (PSR.Name <> [33m'[39;49;00m[33m.[39;49;00m[33m'[39;49;00m) [34mand[39;49;00m (PSR.Name <> [33m'[39;49;00m[33m..[39;49;00m[33m'[39;49;00m) [34mthen[39;49;00m$
  2236	        ScanDir(Path + PSR.Name + [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m, FileName);$
  2237	      Res := [36mFindNext[39;49;00m(PSR);$
  2238	    [34mend[39;49;00m;$
  2239	    [36mFindClose[39;49;00m(PSR);$
  2240	  [34mend[39;49;00m;$
  2241	$
  2242	[34mbegin[39;49;00m$
  2243	  Strings.Clear;$
  2244	  Path := ExtractPath(Mask);$
  2245	  FileName := [36mExtractFileName[39;49;00m(Mask);$
  2246	  ScanDir(Path, FileName);$
  2247	  [36mResult[39;49;00m := Strings.Count > [34m0[39;49;00m;$
  2248	[34mend[39;49;00m;$
  2249	$
  2250	[34mfunction[39;49;00m [32mFindAllFirst[39;49;00m([34mconst[39;49;00m Mask: [34mstring[39;49;00m; ScanSubDirs: [36mBoolean[39;49;00m = [34mTrue[39;49;00m;$
  2251	  Attributes: [36mInteger[39;49;00m = faFindEveryFile): [34mstring[39;49;00m;$
  2252	[34mvar[39;49;00m$
  2253	  Path, FileName: [34mstring[39;49;00m;$
  2254	$
  2255	  [34mfunction[39;49;00m [32mScanDir[39;49;00m([34mconst[39;49;00m Path, FileName: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
  2256	  [34mvar[39;49;00m$
  2257	    PSR: TSearchRec;$
  2258	    Res: [36mInteger[39;49;00m;$
  2259	  [34mbegin[39;49;00m$
  2260	    [36mResult[39;49;00m := [34mFalse[39;49;00m;$
  2261	    [34mif[39;49;00m Success([36mFindFirst[39;49;00m(Path + FileName, Attributes, PSR), [34m0[39;49;00m) [34mthen[39;49;00m [34mbegin[39;49;00m$
  2262	      FindAllFirst := Path + PSR.Name;$
  2263	      [36mResult[39;49;00m := [34mTrue[39;49;00m;$
  2264	      [36mFindClose[39;49;00m(PSR);$
  2265	    [34mExit[39;49;00m; [34mend[39;49;00m;$
  2266	    [34mif[39;49;00m [34mnot[39;49;00m ScanSubDirs [34mthen[39;49;00m$
  2267	      [34mExit[39;49;00m;$
  2268	$
  2269	    Res := [36mFindFirst[39;49;00m(Path + [33m'[39;49;00m[33m*[39;49;00m[33m'[39;49;00m, faDirectory, PSR);$
  2270	    [34mwhile[39;49;00m [34mnot[39;49;00m [36mResult[39;49;00m [34mand[39;49;00m Success(Res, [34m0[39;49;00m) [34mdo[39;49;00m [34mbegin[39;49;00m$
  2271	      [34mif[39;49;00m (PSR.Attr [34mand[39;49;00m faDirectory > [34m0[39;49;00m)$
  2272	       [34mand[39;49;00m (PSR.Name <> [33m'[39;49;00m[33m.[39;49;00m[33m'[39;49;00m) [34mand[39;49;00m (PSR.Name <> [33m'[39;49;00m[33m..[39;49;00m[33m'[39;49;00m) [34mthen[39;49;00m$
  2273	        [36mResult[39;49;00m := ScanDir(Path + PSR.Name + [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m, FileName);$
  2274	      Res := [36mFindNext[39;49;00m(PSR);$
  2275	    [34mend[39;49;00m;$
  2276	    [36mFindClose[39;49;00m(PSR);$
  2277	  [34mend[39;49;00m;$
  2278	[34mbegin[39;49;00m$
  2279	  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
  2280	  Path := ExtractPath(Mask);$
  2281	  FileName := [36mExtractFileName[39;49;00m(Mask);$
  2282	  ScanDir(Path, FileName);$
  2283	[34mend[39;49;00m;$
  2284	$
  2285	[34mprocedure[39;49;00m [32mDeleteFiles[39;49;00m([34mconst[39;49;00m Mask: [34mstring[39;49;00m; ScanSubDirs: [36mBoolean[39;49;00m = [34mTrue[39;49;00m;$
  2286	  Attributes: [36mInteger[39;49;00m = faFindEveryFile);$
  2287	[34mvar[39;49;00m$
  2288	  Path, FileName: [34mstring[39;49;00m;$
  2289	$
  2290	  [34mprocedure[39;49;00m [32mScanDir[39;49;00m([34mconst[39;49;00m Path, FileName: [34mstring[39;49;00m);$
  2291	  [34mvar[39;49;00m$
  2292	    PSR: TSearchRec;$
  2293	    Res: [36mInteger[39;49;00m;$
  2294	$
  2295	    [34mprocedure[39;49;00m [32mTryDeleteFile[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m);$
  2296	    [34mbegin[39;49;00m$
  2297	      [34mtry[39;49;00m$
  2298	        [36mDeleteFile[39;49;00m(Path + PSR.Name);$
  2299	      [34mexcept[39;49;00m$
  2300	      [34mend[39;49;00m;$
  2301	    [34mend[39;49;00m;$
  2302	$
  2303	  [34mbegin[39;49;00m$
  2304	    Res := [36mFindFirst[39;49;00m(Path + FileName, Attributes, PSR);$
  2305	    [34mwhile[39;49;00m Success(Res, [34m0[39;49;00m) [34mdo[39;49;00m [34mbegin[39;49;00m$
  2306	      TryDeleteFile(Path + PSR.Name);$
  2307	      Res := [36mFindNext[39;49;00m(PSR);$
  2308	    [34mend[39;49;00m;$
  2309	    [36mFindClose[39;49;00m(PSR);$
  2310	    [34mif[39;49;00m [34mnot[39;49;00m ScanSubDirs [34mthen[39;49;00m$
  2311	      [34mExit[39;49;00m;$
  2312	$
  2313	    Res := [36mFindFirst[39;49;00m(Path + [33m'[39;49;00m[33m*[39;49;00m[33m'[39;49;00m, faDirectory, PSR);$
  2314	    [34mwhile[39;49;00m Success(Res, [34m0[39;49;00m) [34mdo[39;49;00m [34mbegin[39;49;00m$
  2315	      [34mif[39;49;00m (PSR.Attr [34mand[39;49;00m faDirectory > [34m0[39;49;00m)$
  2316	       [34mand[39;49;00m (PSR.Name <> [33m'[39;49;00m[33m.[39;49;00m[33m'[39;49;00m) [34mand[39;49;00m (PSR.Name <> [33m'[39;49;00m[33m..[39;49;00m[33m'[39;49;00m) [34mthen[39;49;00m [34mbegin[39;49;00m$
  2317	        ScanDir(Path + PSR.Name + [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m, FileName);$
  2318	        TryDeleteFile(Path + PSR.Name);$
  2319	      [34mend[39;49;00m;$
  2320	      Res := [36mFindNext[39;49;00m(PSR);$
  2321	    [34mend[39;49;00m;$
  2322	    [36mFindClose[39;49;00m(PSR);$
  2323	  [34mend[39;49;00m;$
  2324	[34mbegin[39;49;00m$
  2325	  Path := ExtractPath(Mask);$
  2326	  FileName := [36mExtractFileName[39;49;00m(Mask);$
  2327	  ScanDir(Path, FileName);$
  2328	[34mend[39;49;00m;$
  2329	$
  2330	[34mfunction[39;49;00m [32mGetFileNew[39;49;00m(FileName: [34mstring[39;49;00m; NoFloppyDrives: [36mBoolean[39;49;00m = [34mTrue[39;49;00m): [34mstring[39;49;00m;$
  2331	[34mvar[39;49;00m$
  2332	  Drive: [34mstring[39;49;00m;$
  2333	  pf, pd, Len: [36mInteger[39;49;00m;$
  2334	  PSR: TSearchRec;$
  2335	[34mbegin[39;49;00m$
  2336	  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
  2337	  FileName := [36mTrim[39;49;00m(FileName);$
  2338	  [34mif[39;49;00m [36mLength[39;49;00m(FileName) < [34m2[39;49;00m [34mthen[39;49;00m$
  2339	    [34mExit[39;49;00m;$
  2340	$
  2341	  Drive := ExtractDrive(FileName);$
  2342	  [34mif[39;49;00m [34mnot[39;49;00m [36mDirectoryExists[39;49;00m(Drive) [34mthen[39;49;00m$
  2343	    [34mExit[39;49;00m;$
  2344	$
  2345	  [34mif[39;49;00m NoFloppyDrives [34mand[39;49;00m (Drive[[34m1[39;49;00m] [34min[39;49;00m [[33m'[39;49;00m[33mA[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mB[39;49;00m[33m'[39;49;00m]) [34mthen[39;49;00m$
  2346	    [34mExit[39;49;00m;$
  2347	$
  2348	  Len := [36mLength[39;49;00m(FileName);$
  2349	  [36mResult[39;49;00m := Drive;$
  2350	  pf := [36mLength[39;49;00m(Drive) + [34m1[39;49;00m;$
  2351	  [34mwhile[39;49;00m pf <= Len [34mdo[39;49;00m [34mbegin[39;49;00m$
  2352	    [34mif[39;49;00m FileName[pf] = [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m$
  2353	      [36mResult[39;49;00m := [36mResult[39;49;00m + [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m;$
  2354	      [36mInc[39;49;00m(pf);$
  2355	    [34mContinue[39;49;00m; [34mend[39;49;00m;$
  2356	$
  2357	    pd := CharPos([33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m, FileName, pf);$
  2358	    [34mif[39;49;00m pd = [34m0[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m$
  2359	      [34mif[39;49;00m [34m0[39;49;00m=[36mFindFirst[39;49;00m([36mResult[39;49;00m + [36mCopy[39;49;00m(FileName, pf, MaxInt), faFindEveryFile, PSR) [34mthen[39;49;00m [34mbegin[39;49;00m$
  2360	        [36mResult[39;49;00m := [36mResult[39;49;00m + PSR.Name;$
  2361	      [34mBreak[39;49;00m; [34mend[39;49;00m [34melse[39;49;00m [34mbegin[39;49;00m$
  2362	        [36mFindClose[39;49;00m(PSR);$
  2363	        [34mif[39;49;00m [34m0[39;49;00m=[36mFindFirst[39;49;00m([36mResult[39;49;00m + [36mCopy[39;49;00m(FileName, pf, MaxInt), faDirectory, PSR) [34mthen[39;49;00m$
  2364	          [36mResult[39;49;00m := [36mResult[39;49;00m + PSR.Name + [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m$
  2365	        [34melse[39;49;00m$
  2366	          [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
  2367	        [36mFindClose[39;49;00m(PSR);$
  2368	        [34mif[39;49;00m [36mResult[39;49;00m = [33m'[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m$
  2369	          [34mBreak[39;49;00m;$
  2370	      [34mend[39;49;00m;$
  2371	    [34mend[39;49;00m;$
  2372	$
  2373	    [34mif[39;49;00m [34m0[39;49;00m=[36mFindFirst[39;49;00m([36mResult[39;49;00m + [36mCopy[39;49;00m(FileName, pf, pd - pf), faDirectory, PSR) [34mthen[39;49;00m$
  2374	      [36mResult[39;49;00m := [36mResult[39;49;00m + PSR.Name + [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m$
  2375	    [34melse[39;49;00m$
  2376	      [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
  2377	    [36mFindClose[39;49;00m(PSR);$
  2378	    [34mif[39;49;00m [36mResult[39;49;00m = [33m'[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m$
  2379	      [34mBreak[39;49;00m;$
  2380	$
  2381	    pf := pd + [34m1[39;49;00m;$
  2382	  [34mend[39;49;00m;$
  2383	$
  2384	  [34mif[39;49;00m ([36mResult[39;49;00m <> [33m'[39;49;00m[33m'[39;49;00m) [34mand[39;49;00m [34mnot[39;49;00m FileEx([36mResult[39;49;00m, [34mTrue[39;49;00m) [34mthen[39;49;00m$
  2385	    [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
  2386	[34mend[39;49;00m;$
  2387	$
  2388	[34mfunction[39;49;00m [32mDateTimeOfFileTime[39;49;00m([34mconst[39;49;00m FileTime: TFileTime): [36mTDateTime[39;49;00m;$
  2389	[34mvar[39;49;00m$
  2390	  LocalFileTime: TFileTime;$
  2391	  Res: [36mInteger[39;49;00m;$
  2392	[34mbegin[39;49;00m$
  2393	  [36mResult[39;49;00m := [34m0[39;49;00m;$
  2394	$
  2395	  FileTimeToLocalFileTime(FileTime, LocalFileTime);$
  2396	  [34mif[39;49;00m [34mnot[39;49;00m FileTimeToDosDateTime(LocalFileTime, LongRec(Res).Hi,$
  2397	   LongRec(Res).Lo) [34mthen[39;49;00m$
  2398	    Res := -[34m1[39;49;00m;$
  2399	$
  2400	  [34mif[39;49;00m (Res = -[34m1[39;49;00m) [34mor[39;49;00m (Res = [34m0[39;49;00m) [34mthen[39;49;00m$
  2401	    [34mExit[39;49;00m;$
  2402	  [34mtry[39;49;00m$
  2403	    [36mResult[39;49;00m := [36mFileDateToDateTime[39;49;00m(Res);$
  2404	  [34mexcept[39;49;00m$
  2405	  [34mend[39;49;00m;$
  2406	[34mend[39;49;00m;$
  2407	$
  2408	[34mprocedure[39;49;00m [32mFileNew[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m);$
  2409	[34mvar[39;49;00m$
  2410	  Handle: [36mInteger[39;49;00m;$
  2411	[34mbegin[39;49;00m$
  2412	  Handle := [36mFileCreate[39;49;00m(FileName);$
  2413	  [36mFileClose[39;49;00m(Handle);$
  2414	[34mend[39;49;00m;$
  2415	$
  2416	[34mfunction[39;49;00m [32mWin32PlatformStr[39;49;00m: [34mstring[39;49;00m;$
  2417	[34mconst[39;49;00m$
  2418	  PlatformStrings: [34marray[39;49;00m[VER_PLATFORM_WIN32s..VER_PLATFORM_WIN32_NT] [34mof[39;49;00m [34mstring[39;49;00m =$
  2419	    ([33m'[39;49;00m[33mVER_PLATFORM_WIN32s[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mVER_PLATFORM_WIN32_WINDOWS[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mVER_PLATFORM_WIN32_NT[39;49;00m[33m'[39;49;00m);$
  2420	[34mbegin[39;49;00m$
  2421	  [36mResult[39;49;00m := PlatformStrings[Win32Platform];$
  2422	[34mend[39;49;00m;$
  2423	$
  2424	[34mfunction[39;49;00m [32mFullOSInfo[39;49;00m: [34mstring[39;49;00m;$
  2425	[34mbegin[39;49;00m$
  2426	  [36mResult[39;49;00m := [36mFormat[39;49;00m($
  2427	    [33m'[39;49;00m[33mPlatform: %s[39;49;00m[33m'[39;49;00m + EOL +$
  2428	    [33m'[39;49;00m[33mVersion: %d.%d Build %d[39;49;00m[33m'[39;49;00m + EOL +$
  2429	    [33m'[39;49;00m[33mCSD: %s[39;49;00m[33m'[39;49;00m,$
  2430	    [$
  2431	      Win32PlatformStr,$
  2432	      Win32MajorVersion, Win32MinorVersion, Win32BuildNumber,$
  2433	      Win32CSDVersion$
  2434	    ]$
  2435	  );$
  2436	[34mend[39;49;00m;$
  2437	$
  2438	[34mfunction[39;49;00m [32mWin9x[39;49;00m: [36mBoolean[39;49;00m;$
  2439	[34mbegin[39;49;00m$
  2440	  [36mResult[39;49;00m := Win32Platform = VER_PLATFORM_WIN32_WINDOWS;$
  2441	[34mend[39;49;00m;$
  2442	$
  2443	[34mfunction[39;49;00m [32mWinNT[39;49;00m: [36mBoolean[39;49;00m;$
  2444	[34mbegin[39;49;00m$
  2445	  [36mResult[39;49;00m := Win32Platform = VER_PLATFORM_WIN32_NT;$
  2446	[34mend[39;49;00m;$
  2447	$
  2448	[34mfunction[39;49;00m [32mWin2000[39;49;00m: [36mBoolean[39;49;00m;$
  2449	[34mbegin[39;49;00m$
  2450	  [36mResult[39;49;00m := (Win32Platform = VER_PLATFORM_WIN32_NT)$
  2451	            [34mand[39;49;00m (Win32MajorVersion = [34m4[39;49;00m);$
  2452	[34mend[39;49;00m;$
  2453	$
  2454	[34mfunction[39;49;00m [32mWinXP[39;49;00m: [36mBoolean[39;49;00m;$
  2455	[34mbegin[39;49;00m$
  2456	  [36mResult[39;49;00m := Win32MajorVersion >= [34m5[39;49;00m;$
  2457	[34mend[39;49;00m;$
  2458	$
  2459	[34minitialization[39;49;00m$
  2460	  MyDir := GetMyDir;$
  2461	$
  2462	[34mend[39;49;00m.$
  2463	$
  2464	[34munit[39;49;00m FifoStream;$
  2465	$
  2466	[34minterface[39;49;00m$
  2467	$
  2468	[34muses[39;49;00m Classes, windows, Dialogs;$
  2469	$
  2470	[34mconst[39;49;00m$
  2471	  DefaultChunksize = [34m32768[39;49;00m; [37m// 32kb per chunk as default.[39;49;00m$
  2472	$
  2473	[34mtype[39;49;00m$
  2474	  PMemChunk = ^TMemChunk;$
  2475	  TMemChunk = [34mrecord[39;49;00m$
  2476	    Filled: [36mLongword[39;49;00m;$
  2477	    [36mRead[39;49;00m: [36mLongword[39;49;00m;$
  2478	    Data: [36mpointer[39;49;00m;$
  2479	  [34mend[39;49;00m;$
  2480	$
  2481	  TFifo = [34mclass[39;49;00m$
  2482	  [34mprivate[39;49;00m$
  2483	    FBuffers: TList;$
  2484	    FChunksize: [36mLongword[39;49;00m;$
  2485	    FCritSect: TRTLCriticalSection;$
  2486	    FIsWinNT: [36mboolean[39;49;00m;$
  2487	    FBytesInFifo: [36mLongWord[39;49;00m;$
  2488	  [34mprotected[39;49;00m$
  2489	    [34mfunction[39;49;00m [32mGetBytesInFifo[39;49;00m: [36mLongWord[39;49;00m;$
  2490	  [34mpublic[39;49;00m$
  2491	    [34mconstructor[39;49;00m [32mCreate[39;49;00m;$
  2492	    [34mdestructor[39;49;00m [32mDestroy[39;49;00m; [34moverride[39;49;00m;$
  2493	    [34mprocedure[39;49;00m [32mWrite[39;49;00m(Data: [36mpointer[39;49;00m; Size: [36mLongWord[39;49;00m);$
  2494	    [34mprocedure[39;49;00m [32mRead[39;49;00m(Buff: [36mpointer[39;49;00m; [34mvar[39;49;00m ReqSize: [36mLongWord[39;49;00m);$
  2495	    [34mprocedure[39;49;00m [32mPeekData[39;49;00m(Buff: [36mpointer[39;49;00m; [34mvar[39;49;00m ReqSize: [36mLongWord[39;49;00m);$
  2496	  [34mpublished[39;49;00m$
  2497	    [34mproperty[39;49;00m BytesInFifo: [36mLongWord[39;49;00m [34mread[39;49;00m [32mFBytesInFifo[39;49;00m;$
  2498	  [34mend[39;49;00m;$
  2499	$
  2500	[34mimplementation[39;49;00m$
  2501	$
  2502	[34mconstructor[39;49;00m [04m[32mTFifo[39;49;00m.[32mCreate[39;49;00m;$
  2503	[34mbegin[39;49;00m$
  2504	  [34minherited[39;49;00m;$
  2505	  FBuffers := TList.Create;$
  2506	  [37m// set default chunksize...[39;49;00m$
  2507	  FChunksize := DefaultChunksize;$
  2508	  InitializeCriticalSection(FCritSect);$
  2509	[34mend[39;49;00m;$
  2510	$
  2511	[34mdestructor[39;49;00m [04m[32mTFifo[39;49;00m.[32mDestroy[39;49;00m;$
  2512	[34mvar[39;49;00m$
  2513	  I: [36mInteger[39;49;00m;$
  2514	[34mbegin[39;49;00m$
  2515	  EnterCriticalSection(FCritSect);$
  2516	  [34mfor[39;49;00m I := [34m0[39;49;00m [34mto[39;49;00m FBuffers.count - [34m1[39;49;00m [34mdo[39;49;00m$
  2517	  [34mbegin[39;49;00m$
  2518	    [36mFreeMem[39;49;00m(PMemChunk(Fbuffers[I]).Data);$
  2519	    [34mDispose[39;49;00m(PMemChunk(Fbuffers[I]));$
  2520	  [34mend[39;49;00m;$
  2521	  FBuffers.Clear;$
  2522	  FBuffers.Free;$
  2523	  LeaveCriticalSection(FCritSect);$
  2524	$
  2525	  DeleteCriticalSection(FCritSect);$
  2526	  [34minherited[39;49;00m;$
  2527	[34mend[39;49;00m;$
  2528	$
  2529	[34mfunction[39;49;00m [04m[32mTFifo[39;49;00m.[32mGetBytesInFifo[39;49;00m: [36mLongWord[39;49;00m;$
  2530	[34mbegin[39;49;00m$
  2531	  [36mResult[39;49;00m := [34m0[39;49;00m;$
  2532	  [34mif[39;49;00m FBuffers.Count = [34m0[39;49;00m [34mthen[39;49;00m$
  2533	  [34mbegin[39;49;00m$
  2534	    [34mexit[39;49;00m;$
  2535	  [34mend[39;49;00m$
  2536	  [34melse[39;49;00m$
  2537	  [34mbegin[39;49;00m$
  2538	    [34mif[39;49;00m FBuffers.Count > [34m1[39;49;00m [34mthen[39;49;00m$
  2539	      [36mInc[39;49;00m([36mResult[39;49;00m, (FBuffers.Count - [34m1[39;49;00m) * FChunkSize);$
  2540	    [36mInc[39;49;00m([36mResult[39;49;00m, PMemChunk(FBuffers[Fbuffers.Count - [34m1[39;49;00m]).Filled);$
  2541	    [36mDec[39;49;00m([36mResult[39;49;00m, PMemChunk(FBuffers[[34m0[39;49;00m]).Read);$
  2542	  [34mend[39;49;00m;$
  2543	[34mend[39;49;00m;$
  2544	$
  2545	[34mprocedure[39;49;00m [04m[32mTFifo[39;49;00m.[32mWrite[39;49;00m(Data: [36mpointer[39;49;00m; Size: [36mLongWord[39;49;00m);$
  2546	[34mvar[39;49;00m$
  2547	  Privpointer: [36mpointer[39;49;00m;$
  2548	  PrivSize: [36mLongWord[39;49;00m;$
  2549	  Chunk: PMemChunk;$
  2550	  PosInChunk: [36mpointer[39;49;00m;$
  2551	[34mbegin[39;49;00m$
  2552	  [34mif[39;49;00m [36mLongWord[39;49;00m(Data) = [34m0[39;49;00m [34mthen[39;49;00m$
  2553	  [34mbegin[39;49;00m$
  2554	    [37m// null pointer? somebody is trying to fool us, get out...[39;49;00m$
  2555	    [34mExit[39;49;00m;$
  2556	  [34mend[39;49;00m;$
  2557	  EnterCriticalSection(FCritSect);$
  2558	  PrivPointer := Data;$
  2559	  PrivSize := [34m0[39;49;00m;$
  2560	  [37m// are already buffers there?[39;49;00m$
  2561	  [34mif[39;49;00m FBuffers.count > [34m0[39;49;00m [34mthen[39;49;00m$
  2562	  [34mbegin[39;49;00m$
  2563	    [37m// is the last one of them not completely filled?[39;49;00m$
  2564	    [34mif[39;49;00m PMemChunk(FBuffers[FBuffers.count - [34m1[39;49;00m]).filled < FChunksize [34mthen[39;49;00m$
  2565	      [37m// not completely filled, so fill up the buffer.[39;49;00m$
  2566	    [34mbegin[39;49;00m$
  2567	      Chunk := PMemChunk(FBuffers[FBuffers.count - [34m1[39;49;00m]);$
  2568	      [37m// fetch chunkdata.[39;49;00m$
  2569	      PosInChunk := Chunk.Data;$
  2570	      [37m// move to current fill pos...[39;49;00m$
  2571	      [36mInc[39;49;00m([36mLongWord[39;49;00m(PosInChunk), Chunk.Filled);$
  2572	      [37m// can we fill the chunk completely?[39;49;00m$
  2573	      [34mif[39;49;00m Size > FChunksize - Chunk.Filled [34mthen[39;49;00m$
  2574	      [34mbegin[39;49;00m$
  2575	        [37m// yes we can.[39;49;00m$
  2576	        [36mMove[39;49;00m(PrivPointer^, PosInChunk^, FChunksize - Chunk.Filled);$
  2577	        [36mInc[39;49;00m(PrivSize, FChunksize - Chunk.Filled);$
  2578	        [36mInc[39;49;00m([36mLongWord[39;49;00m(PrivPointer), FChunksize - Chunk.Filled);$
  2579	        Chunk.Filled := FChunkSize;$
  2580	      [34mend[39;49;00m$
  2581	      [34melse[39;49;00m$
  2582	        [37m// we have to less data for filling the chunk completely,[39;49;00m$
  2583	        [37m// just put everything in.[39;49;00m$
  2584	      [34mbegin[39;49;00m$
  2585	        [36mMove[39;49;00m(PrivPointer^, PosInChunk^, Size);$
  2586	        [36mInc[39;49;00m(PrivSize, Size);$
  2587	        [36mInc[39;49;00m(Chunk.Filled, Size);$
  2588	      [34mend[39;49;00m;$
  2589	    [34mend[39;49;00m;$
  2590	  [34mend[39;49;00m;$
  2591	  [37m// as long as we have remaining stuff put it into new chunks.[39;49;00m$
  2592	  [34mwhile[39;49;00m (PrivSize < Size) [34mdo[39;49;00m$
  2593	  [34mbegin[39;49;00m$
  2594	    [34mnew[39;49;00m(Chunk);$
  2595	    [36mGetMem[39;49;00m(Chunk.Data, FChunksize);$
  2596	    Chunk.Read := [34m0[39;49;00m;$
  2597	    [37m// can we fill an entire chunk with the remaining data?[39;49;00m$
  2598	    [34mif[39;49;00m Privsize + FChunksize < Size [34mthen[39;49;00m$
  2599	    [34mbegin[39;49;00m$
  2600	      [37m// yes we can, so put the stuff in.[39;49;00m$
  2601	      [36mMove[39;49;00m(Privpointer^, Chunk.Data^, FChunksize);$
  2602	      [36mInc[39;49;00m([36mLongWord[39;49;00m(PrivPointer), FChunksize);$
  2603	      [36mInc[39;49;00m(PrivSize, FChunksize);$
  2604	      Chunk.Filled := FChunksize;$
  2605	    [34mend[39;49;00m$
  2606	    [34melse[39;49;00m [37m// we have to less data to fill the entire chunk, just put the remaining stuff in.[39;49;00m$
  2607	    [34mbegin[39;49;00m$
  2608	      [36mMove[39;49;00m(Privpointer^, Chunk.Data^, Size - Privsize);$
  2609	      Chunk.Filled := Size - Privsize;$
  2610	      [36mInc[39;49;00m(PrivSize, Size - Privsize);$
  2611	    [34mend[39;49;00m;$
  2612	    Fbuffers.Add(Chunk);$
  2613	  [34mend[39;49;00m;$
  2614	  [34mif[39;49;00m Size <> Privsize [34mthen[39;49;00m$
  2615	    Showmessage([33m'[39;49;00m[33mmiscalculation in TFifo.write[39;49;00m[33m'[39;49;00m);$
  2616	  FBytesInFifo := GetBytesInFifo;$
  2617	  LeaveCriticalSection(FCritSect);$
  2618	[34mend[39;49;00m;$
  2619	$
  2620	[34mprocedure[39;49;00m [04m[32mTFifo[39;49;00m.[32mRead[39;49;00m(Buff: [36mpointer[39;49;00m; [34mvar[39;49;00m ReqSize: [36mLongWord[39;49;00m);$
  2621	[34mvar[39;49;00m$
  2622	  PrivSize: [36mInteger[39;49;00m;$
  2623	  Privpos: [36mpointer[39;49;00m;$
  2624	  Chunk: PMemChunk;$
  2625	  ChunkPos: [36mpointer[39;49;00m;$
  2626	[34mbegin[39;49;00m$
  2627	  [34mif[39;49;00m [36mLongWord[39;49;00m(Buff) = [34m0[39;49;00m [34mthen[39;49;00m$
  2628	  [34mbegin[39;49;00m$
  2629	    [37m// null pointer? somebody is trying to fool us, get out...[39;49;00m$
  2630	    [34mExit[39;49;00m;$
  2631	  [34mend[39;49;00m;$
  2632	  EnterCriticalSection(FCritSect);$
  2633	  PrivSize := [34m0[39;49;00m;$
  2634	  Privpos := Buff;$
  2635	  [34mwhile[39;49;00m FBuffers.Count > [34m0[39;49;00m [34mdo[39;49;00m$
  2636	  [34mbegin[39;49;00m$
  2637	    Chunk := PMemChunk(FBuffers[[34m0[39;49;00m]);$
  2638	    ChunkPos := Chunk.data;$
  2639	    [36mInc[39;49;00m([36mLongWord[39;49;00m(ChunkPos), Chunk.Read);$
  2640	    [37m// does the remaining part of the chunk fit into the buffer?[39;49;00m$
  2641	    [34mif[39;49;00m PrivSize + (Chunk.Filled - Chunk.read) < ReqSize [34mthen[39;49;00m$
  2642	    [34mbegin[39;49;00m [37m// yep, it fits[39;49;00m$
  2643	      [36mMove[39;49;00m(ChunkPos^, Privpos^, Chunk.Filled - Chunk.read);$
  2644	      [36mInc[39;49;00m(PrivSize, Chunk.Filled - Chunk.read);$
  2645	      [36mFreeMem[39;49;00m(Chunk.Data);$
  2646	      [34mDispose[39;49;00m(Chunk);$
  2647	      FBuffers.Delete([34m0[39;49;00m);$
  2648	    [34mend[39;49;00m$
  2649	    [34melse[39;49;00m [37m// remaining part didn't fit, get as much as we can and increment the[39;49;00m$
  2650	      [37m// read attribute.[39;49;00m$
  2651	    [34mbegin[39;49;00m$
  2652	      [36mMove[39;49;00m(ChunkPos^, Privpos^, ReqSize - PrivSize);$
  2653	      [36mInc[39;49;00m(Chunk.read, ReqSize - PrivSize);$
  2654	      [36mInc[39;49;00m(PrivSize, ReqSize - PrivSize);$
  2655	      [37m// as we filled the buffer, we'll have to break here.[39;49;00m$
  2656	      [34mbreak[39;49;00m;$
  2657	    [34mend[39;49;00m;$
  2658	  [34mend[39;49;00m;$
  2659	  FBytesInFifo := GetBytesInFifo;$
  2660	  LeaveCriticalSection(FCritSect);$
  2661	  ReqSize := PrivSize;$
  2662	[34mend[39;49;00m;$
  2663	$
  2664	[37m// read Data from Stream without removing it from the Stream...[39;49;00m$
  2665	$
  2666	[34mprocedure[39;49;00m [04m[32mTFifo[39;49;00m.[32mPeekData[39;49;00m(Buff: [36mpointer[39;49;00m; [34mvar[39;49;00m ReqSize: [36mLongWord[39;49;00m);$
  2667	[34mvar[39;49;00m$
  2668	  PrivSize: [36mInteger[39;49;00m;$
  2669	  Privpos: [36mpointer[39;49;00m;$
  2670	  Chunk: PMemChunk;$
  2671	  ChunkPos: [36mpointer[39;49;00m;$
  2672	  ChunkNr: [36mInteger[39;49;00m;$
  2673	[34mbegin[39;49;00m$
  2674	  [34mif[39;49;00m [36mLongWord[39;49;00m(Buff) = [34m0[39;49;00m [34mthen[39;49;00m$
  2675	  [34mbegin[39;49;00m$
  2676	    [37m// null pointer? somebody is trying to fool us, get out...[39;49;00m$
  2677	    [34mExit[39;49;00m;$
  2678	  [34mend[39;49;00m;$
  2679	  EnterCriticalSection(FCritSect);$
  2680	  PrivSize := [34m0[39;49;00m;$
  2681	  Privpos := Buff;$
  2682	  ChunkNr := [34m0[39;49;00m;$
  2683	  [34mwhile[39;49;00m FBuffers.Count > ChunkNr [34mdo[39;49;00m$
  2684	  [34mbegin[39;49;00m$
  2685	    Chunk := PMemChunk(FBuffers[ChunkNr]);$
  2686	    ChunkPos := Chunk.data;$
  2687	    [36mInc[39;49;00m([36mLongWord[39;49;00m(ChunkPos), Chunk.Read);$
  2688	    [37m// does the remaining part of the chunk fit into the buffer?[39;49;00m$
  2689	    [34mif[39;49;00m PrivSize + (Chunk.Filled - Chunk.read) < ReqSize [34mthen[39;49;00m$
  2690	    [34mbegin[39;49;00m [37m// yep, it fits[39;49;00m$
  2691	      [36mMove[39;49;00m(ChunkPos^, Privpos^, Chunk.Filled - Chunk.read);$
  2692	      [36mInc[39;49;00m(PrivSize, Chunk.Filled - Chunk.read);$
  2693	      [36mInc[39;49;00m(ChunkNr);$
  2694	    [34mend[39;49;00m$
  2695	    [34melse[39;49;00m [37m// remaining part didn't fit, get as much as we can and increment the[39;49;00m$
  2696	      [37m// read attribute.[39;49;00m$
  2697	    [34mbegin[39;49;00m$
  2698	      [36mMove[39;49;00m(ChunkPos^, Privpos^, ReqSize - PrivSize);$
  2699	      [36mInc[39;49;00m(PrivSize, ReqSize - PrivSize);$
  2700	      [37m// as we filled the buffer, we'll have to break here.[39;49;00m$
  2701	      [34mbreak[39;49;00m;$
  2702	    [34mend[39;49;00m;$
  2703	  [34mend[39;49;00m;$
  2704	  LeaveCriticalSection(FCritSect);$
  2705	  ReqSize := PrivSize;$
  2706	[34mend[39;49;00m;$
  2707	$
  2708	[34mend[39;49;00m.$

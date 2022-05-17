[37m// vim:ft=pascal[39;49;00m

[34munit[39;49;00m YTools;

[37m{===============================================================================[39;49;00m
[37m[39;49;00m
[37m   cYcnus.YTools 1.0.3 Beta for Delphi 4+[39;49;00m
[37m   by licenser and Murphy[39;49;00m
[37m[39;49;00m
[37m   ©2000-2003 by cYcnus[39;49;00m
[37m   visit www.cYcnus.de[39;49;00m
[37m[39;49;00m
[37m   licenser@cYcnus.de (Heinz N. Gies)[39;49;00m
[37m   murphy@cYcnus.de (Kornelius Kalnbach)[39;49;00m
[37m   [39;49;00m
[37m   this unit is published under the terms of the GPL[39;49;00m
[37m[39;49;00m
[37m===============================================================================}[39;49;00m

[34minterface[39;49;00m

[34muses[39;49;00m
  Windows, SysUtils, Classes, YTypes;

[34mconst[39;49;00m
  BackSpace = [33m#8[39;49;00m;
  Tab = [33m#9[39;49;00m;
  LF = [33m#10[39;49;00m; [37m//Line Feed[39;49;00m
  CR = [33m#13[39;49;00m; [37m//Carriage Return[39;49;00m
  Space = [33m#32[39;49;00m;
  EOLChars = [CR, LF];
[37m{$IFNDEF VER140}[39;49;00m
  sLineBreak = [33m#13[39;49;00m[33m#10[39;49;00m;
  SwitchChars = [[33m'[39;49;00m[33m/[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33m-[39;49;00m[33m'[39;49;00m];
[37m{$ENDIF}[39;49;00m
  EOL = sLineBreak;
  MaxCard = [36mHigh[39;49;00m([36mCardinal[39;49;00m);
  AllChars = [[33m#0[39;49;00m..[33m#255[39;49;00m];
  Alphabetical = [[33m'[39;49;00m[33mA[39;49;00m[33m'[39;49;00m..[33m'[39;49;00m[33mZ[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33ma[39;49;00m[33m'[39;49;00m..[33m'[39;49;00m[33mz[39;49;00m[33m'[39;49;00m];
  DecimalChars = [[33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m..[33m'[39;49;00m[33m9[39;49;00m[33m'[39;49;00m];
  AlphaNumerical = Alphabetical + DecimalChars;
  StrangeChars = [[33m#0[39;49;00m..[33m#31[39;49;00m, [33m#127[39;49;00m, [33m#129[39;49;00m, [33m#141[39;49;00m..[33m#144[39;49;00m, [33m#157[39;49;00m, [33m#158[39;49;00m];

  HexadecimalChars = DecimalChars + [[33m'[39;49;00m[33mA[39;49;00m[33m'[39;49;00m..[33m'[39;49;00m[33mF[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33ma[39;49;00m[33m'[39;49;00m..[33m'[39;49;00m[33mf[39;49;00m[33m'[39;49;00m];
  OctalChars = [[33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m..[33m'[39;49;00m[33m7[39;49;00m[33m'[39;49;00m];
  BinaryChars = [[33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33m1[39;49;00m[33m'[39;49;00m];

  QuoteChars = [[33m'[39;49;00m[33m''[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33m"[39;49;00m[33m'[39;49;00m];
  WildCards = [[33m'[39;49;00m[33m*[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33m?[39;49;00m[33m'[39;49;00m];
  FileNameEnemies = WildCards + [[33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33m/[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33m:[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33m<[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33m>[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33m|[39;49;00m[33m'[39;49;00m];

  HexChar: [34marray[39;49;00m[THex] [34mof[39;49;00m [36mChar[39;49;00m = (
    [33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m1[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m2[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m3[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m4[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m5[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m6[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m7[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m8[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m9[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mA[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mB[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mC[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mD[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mE[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mF[39;49;00m[33m'[39;49;00m);
  LowerHexChar: [34marray[39;49;00m[THex] [34mof[39;49;00m [36mChar[39;49;00m = (
    [33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m1[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m2[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m3[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m4[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m5[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m6[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m7[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m8[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m9[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33ma[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mb[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mc[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33md[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33me[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mf[39;49;00m[33m'[39;49;00m);
  BaseNChar: [34marray[39;49;00m[TBaseN] [34mof[39;49;00m [36mChar[39;49;00m = (
    [33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m1[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m2[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m3[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m4[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m5[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m6[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m7[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m8[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m9[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mA[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mB[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mC[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mD[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mE[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mF[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mG[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mH[39;49;00m[33m'[39;49;00m,
    [33m'[39;49;00m[33mI[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mJ[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mK[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mL[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mM[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mN[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mO[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mP[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mQ[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mR[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mS[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mT[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mU[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mV[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mW[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mX[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mY[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mZ[39;49;00m[33m'[39;49;00m);

  cYcnusOverlayColor = [34m$050001[39;49;00m;

  faFindEveryFile = faReadOnly + faHidden + faSysFile + faArchive;

  platWin9x = [VER_PLATFORM_WIN32s, VER_PLATFORM_WIN32_WINDOWS];


[37m{ Debugging }[39;49;00m
[34mprocedure[39;49;00m [32mClearReport[39;49;00m([34mconst[39;49;00m ReportName: [34mstring[39;49;00m);
[34mprocedure[39;49;00m [32mReport[39;49;00m([34mconst[39;49;00m ReportName, Text: [34mstring[39;49;00m);
[34mprocedure[39;49;00m [32mReportFmt[39;49;00m([34mconst[39;49;00m ReportName, Fmt: [34mstring[39;49;00m; [34mconst[39;49;00m Args: [34marray[39;49;00m [34mof[39;49;00m [34mconst[39;49;00m);

[37m{ Params }[39;49;00m
[34mprocedure[39;49;00m [32mGetParams[39;49;00m(Strings: TStrings); overload;
[34mfunction[39;49;00m [32mGetParams[39;49;00m([34mconst[39;49;00m Separator: [34mstring[39;49;00m = [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m; overload;

[34mfunction[39;49;00m [32mParamNum[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [36mInteger[39;49;00m;
[34mfunction[39;49;00m [32mParamPrefixNum[39;49;00m([34mconst[39;49;00m Prefix: [34mstring[39;49;00m): [36mInteger[39;49;00m;
[34mfunction[39;49;00m [32mParam[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [36mBoolean[39;49;00m;
[34mfunction[39;49;00m [32mParamPrefix[39;49;00m([34mconst[39;49;00m Prefix: [34mstring[39;49;00m): [36mBoolean[39;49;00m;

[34mfunction[39;49;00m [32mSwitch[39;49;00m([34mconst[39;49;00m Switch: [34mstring[39;49;00m; [34mconst[39;49;00m PrefixChars: TCharSet = SwitchChars;
  IgnoreCase: [36mBoolean[39;49;00m = [34mTrue[39;49;00m): [36mBoolean[39;49;00m;
[34mfunction[39;49;00m [32mGetParam[39;49;00m([34mconst[39;49;00m Prefix: [34mstring[39;49;00m = [33m'[39;49;00m[33m'[39;49;00m; [34mconst[39;49;00m [34mDefault[39;49;00m: [34mstring[39;49;00m = [33m'[39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;

[37m{ Dirs & UserName}[39;49;00m
[34mfunction[39;49;00m [32mGetMyDir[39;49;00m(FullPath: [36mBoolean[39;49;00m = [34mFalse[39;49;00m): [34mstring[39;49;00m;
[34mfunction[39;49;00m [32mWinDir[39;49;00m: [34mstring[39;49;00m;
[34mfunction[39;49;00m [32mSysDir[39;49;00m: [34mstring[39;49;00m;
[34mfunction[39;49;00m [32mUserName[39;49;00m: [34mstring[39;49;00m;

[37m{ Strings & Chars}[39;49;00m
[34mfunction[39;49;00m [32mFirstChar[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [36mChar[39;49;00m;
[34mfunction[39;49;00m [32mLastChar[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [36mChar[39;49;00m;

[34mfunction[39;49;00m [32mCharPos[39;49;00m(C: [36mChar[39;49;00m; [34mconst[39;49;00m S: [34mstring[39;49;00m; Offset: [36mInteger[39;49;00m = [34m1[39;49;00m): [36mInteger[39;49;00m; overload;
[34mfunction[39;49;00m [32mCharPos[39;49;00m(C: TCharSet; [34mconst[39;49;00m S: [34mstring[39;49;00m; Offset: [36mInteger[39;49;00m = [34m1[39;49;00m): [36mInteger[39;49;00m; overload;
[34mfunction[39;49;00m [32mCharPosR[39;49;00m(C: [36mChar[39;49;00m; [34mconst[39;49;00m S: [34mstring[39;49;00m; Offset: [36mInteger[39;49;00m = -[34m1[39;49;00m): [36mInteger[39;49;00m;
[34mfunction[39;49;00m [32mPosEx[39;49;00m([34mconst[39;49;00m SubStr, S: [34mstring[39;49;00m; Offset: [36mInteger[39;49;00m = [34m1[39;49;00m): [36mInteger[39;49;00m;
[34mfunction[39;49;00m [32mPosExText[39;49;00m([34mconst[39;49;00m SubStr, S: [34mstring[39;49;00m; Offset: [36mInteger[39;49;00m = [34m1[39;49;00m): [36mInteger[39;49;00m;
[34mfunction[39;49;00m [32mPosExAnsiText[39;49;00m([34mconst[39;49;00m SubStr, S: [34mstring[39;49;00m; Offset: [36mInteger[39;49;00m = [34m1[39;49;00m): [36mInteger[39;49;00m;

[34mfunction[39;49;00m [32mUntilChar[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Brake: [36mChar[39;49;00m): [34mstring[39;49;00m; overload;
[34mfunction[39;49;00m [32mUntilChar[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Brake: TCharSet): [34mstring[39;49;00m; overload;
[34mfunction[39;49;00m [32mUntilLastChar[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Brake: [36mChar[39;49;00m;
  IgnoreNoBrake: [36mBoolean[39;49;00m = [34mTrue[39;49;00m): [34mstring[39;49;00m;

[34mfunction[39;49;00m [32mFromChar[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Brake: [36mChar[39;49;00m): [34mstring[39;49;00m; overload;
[34mfunction[39;49;00m [32mFromChar[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Brake: TCharSet): [34mstring[39;49;00m; overload;
[34mfunction[39;49;00m [32mFromLastChar[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Brake: [36mChar[39;49;00m;
  IgnoreNoBrake: [36mBoolean[39;49;00m = [34mFalse[39;49;00m): [34mstring[39;49;00m;

[34mfunction[39;49;00m [32mBetweenChars[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Start, Finish: [36mChar[39;49;00m;
  Inclusive: [36mBoolean[39;49;00m = [34mFalse[39;49;00m): [34mstring[39;49;00m;

[34mfunction[39;49;00m [32mUntilStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Brake: [34mstring[39;49;00m): [34mstring[39;49;00m;
[34mfunction[39;49;00m [32mFromStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Brake: [34mstring[39;49;00m): [34mstring[39;49;00m;

[34mfunction[39;49;00m [32mStringWrap[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Width: [36mInteger[39;49;00m; [34mconst[39;49;00m LineEnd: [34mstring[39;49;00m = EOL): [34mstring[39;49;00m;

[37m{ Splitting & Combining }[39;49;00m
[34mfunction[39;49;00m [32mSplit[39;49;00m([34mconst[39;49;00m S, Separator: [34mstring[39;49;00m; IgnoreMultiSep: [36mBoolean[39;49;00m = [34mTrue[39;49;00m;
  MinCount: [36mInteger[39;49;00m = [34m0[39;49;00m): TStrA; overload;
[34mprocedure[39;49;00m [32mSplit[39;49;00m([34mconst[39;49;00m S, Separator: [34mstring[39;49;00m; Strings: TStrings;
  IgnoreMultiSep: [36mBoolean[39;49;00m = [34mTrue[39;49;00m); overload;
[34mfunction[39;49;00m [32mSplit[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Separators: TCharSet;
  IgnoreMultiSep: [36mBoolean[39;49;00m = [34mTrue[39;49;00m; MinCount: [36mInteger[39;49;00m = [34m0[39;49;00m): TStrA; overload;

[34mprocedure[39;49;00m [32mTileStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; BrakeStart: [36mInteger[39;49;00m; BrakeEnd: [36mInteger[39;49;00m;
  out Left, Right: [34mstring[39;49;00m);

[34mfunction[39;49;00m [32mJoin[39;49;00m(Strings: TStrings; Separator: [34mstring[39;49;00m = [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m; overload;
[34mfunction[39;49;00m [32mJoin[39;49;00m(StrA: TStrA; Separator: [34mstring[39;49;00m = [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m; overload;

[34mfunction[39;49;00m [32mMulStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Count: [36mInteger[39;49;00m): [34mstring[39;49;00m;

[37m{ Strings ausrichten }[39;49;00m
[34mfunction[39;49;00m [32mAlignR[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Width: [36mInteger[39;49;00m; Filler: [36mChar[39;49;00m = [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;
[34mfunction[39;49;00m [32mMaxStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; MaxLen: [36mInteger[39;49;00m): [34mstring[39;49;00m;

[37m{ Stringing }[39;49;00m
[34mfunction[39;49;00m [32mTrimAll[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [34mstring[39;49;00m;

[34mfunction[39;49;00m [32mControlChar[39;49;00m(C: [36mChar[39;49;00m): [36mBoolean[39;49;00m;
[34mfunction[39;49;00m [32mFriendlyChar[39;49;00m(C: [36mChar[39;49;00m): [36mChar[39;49;00m;

[34mfunction[39;49;00m [32mFriendlyStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [34mstring[39;49;00m; overload;
[34mfunction[39;49;00m [32mFriendlyStr[39;49;00m(a: TByteA): [34mstring[39;49;00m; overload;

[34mfunction[39;49;00m [32mQuote[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Quoter: [36mChar[39;49;00m = [33m'[39;49;00m[33m"[39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;
[34mfunction[39;49;00m [32mUnQuote[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [34mstring[39;49;00m;
[34mfunction[39;49;00m [32mDeQuote[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [34mstring[39;49;00m;

[34mfunction[39;49;00m [32mStrNumerus[39;49;00m([34mconst[39;49;00m Value: [36mInteger[39;49;00m; [34mconst[39;49;00m Singular, Plural: [34mstring[39;49;00m;
  [34mconst[39;49;00m Zero: [34mstring[39;49;00m = [33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;

[34mfunction[39;49;00m [32mMakeStr[39;49;00m([34mconst[39;49;00m Items: [34marray[39;49;00m [34mof[39;49;00m [34mconst[39;49;00m; Separator: [34mstring[39;49;00m = [33m'[39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;
[34mprocedure[39;49;00m [32mShowText[39;49;00m([34mconst[39;49;00m Items: [34marray[39;49;00m [34mof[39;49;00m [34mconst[39;49;00m; Separator: [34mstring[39;49;00m = [33m'[39;49;00m[33m'[39;49;00m);

[37m{ Delete }[39;49;00m
[34mfunction[39;49;00m [32mDeleteChars[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; C: [36mChar[39;49;00m): [34mstring[39;49;00m; overload;
[34mfunction[39;49;00m [32mDeleteChars[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; C: TCharSet): [34mstring[39;49;00m; overload;
[34mfunction[39;49;00m [32mExtractChars[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; C: TCharSet): [34mstring[39;49;00m;

[37m{ Find }[39;49;00m
[34mfunction[39;49;00m [32mCharCount[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; C: [36mChar[39;49;00m): [36mInteger[39;49;00m;

[34mfunction[39;49;00m [32mCharIn[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; C: [36mChar[39;49;00m): [36mBoolean[39;49;00m; overload;
[34mfunction[39;49;00m [32mCharIn[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; C: TCharSet): [36mBoolean[39;49;00m; overload;

[34mfunction[39;49;00m [32mStrAtPos[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; [36mPos[39;49;00m: [36mInteger[39;49;00m; [34mconst[39;49;00m [36mStr[39;49;00m: [34mstring[39;49;00m): [36mBoolean[39;49;00m;
[34mfunction[39;49;00m [32mStrAtBegin[39;49;00m([34mconst[39;49;00m S, [36mStr[39;49;00m: [34mstring[39;49;00m): [36mBoolean[39;49;00m;
[34mfunction[39;49;00m [32mStrIn[39;49;00m([34mconst[39;49;00m S, SubStr: [34mstring[39;49;00m): [36mBoolean[39;49;00m; overload;
[34mfunction[39;49;00m [32mStrIn[39;49;00m(A: TStrA; [34mconst[39;49;00m S: [34mstring[39;49;00m): [36mBoolean[39;49;00m; overload;
[34mfunction[39;49;00m [32mStrIn[39;49;00m(SL: TStrings; [34mconst[39;49;00m S: [34mstring[39;49;00m): [36mBoolean[39;49;00m; overload;
[34mfunction[39;49;00m [32mStrIndex[39;49;00m(A: TStrA; [34mconst[39;49;00m S: [34mstring[39;49;00m): [36mInteger[39;49;00m; overload;
[34mfunction[39;49;00m [32mStrIndex[39;49;00m(SL: TStrings; [34mconst[39;49;00m S: [34mstring[39;49;00m): [36mInteger[39;49;00m; overload;

[34mfunction[39;49;00m [32mTextAtPos[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; [36mPos[39;49;00m: [36mInteger[39;49;00m; [34mconst[39;49;00m Text: [34mstring[39;49;00m): [36mBoolean[39;49;00m;
[34mfunction[39;49;00m [32mTextAtBegin[39;49;00m([34mconst[39;49;00m S, Text: [34mstring[39;49;00m): [36mBoolean[39;49;00m;
[34mfunction[39;49;00m [32mTextIn[39;49;00m([34mconst[39;49;00m S, Text: [34mstring[39;49;00m): [36mBoolean[39;49;00m; overload;
[34mfunction[39;49;00m [32mTextIn[39;49;00m(A: TStrA; [34mconst[39;49;00m Text: [34mstring[39;49;00m): [36mBoolean[39;49;00m; overload;
[34mfunction[39;49;00m [32mTextIn[39;49;00m(SL: TStrings; [34mconst[39;49;00m Text: [34mstring[39;49;00m): [36mBoolean[39;49;00m; overload;
[34mfunction[39;49;00m [32mTextIndex[39;49;00m(A: TStrA; [34mconst[39;49;00m Text: [34mstring[39;49;00m): [36mInteger[39;49;00m; overload;
[34mfunction[39;49;00m [32mTextIndex[39;49;00m(SL: TStrings; [34mconst[39;49;00m Text: [34mstring[39;49;00m): [36mInteger[39;49;00m; overload;

[37m{ Replace }[39;49;00m
[34mfunction[39;49;00m [32mReplaceChars[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Old, [34mNew[39;49;00m: [36mChar[39;49;00m): [34mstring[39;49;00m; overload;
[34mfunction[39;49;00m [32mReplaceChars[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Old: TCharSet; [34mNew[39;49;00m: [36mChar[39;49;00m): [34mstring[39;49;00m; overload;

[34mfunction[39;49;00m [32mReplace[39;49;00m([34mconst[39;49;00m S, Old, [34mNew[39;49;00m: [34mstring[39;49;00m): [34mstring[39;49;00m;

[37m{ TStrings }[39;49;00m
[34mfunction[39;49;00m [32mSLOfFile[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m): TStringList;
[34mfunction[39;49;00m [32mContainsEmptyLines[39;49;00m(SL: TStrings): [36mBoolean[39;49;00m;
[34mprocedure[39;49;00m [32mDeleteEmptyLines[39;49;00m(SL: TStrings);
[34mprocedure[39;49;00m [32mDeleteCommentLines[39;49;00m(SL: TStrings; [34mconst[39;49;00m CommentSign: [34mstring[39;49;00m = [33m'[39;49;00m[33m//[39;49;00m[33m'[39;49;00m);
[34mprocedure[39;49;00m [32mWriteSL[39;49;00m(Strings: TStrings; [34mconst[39;49;00m Prefix: [34mstring[39;49;00m = [33m'[39;49;00m[33m'[39;49;00m;
  [34mconst[39;49;00m Suffix: [34mstring[39;49;00m = [33m'[39;49;00m[33m'[39;49;00m);

[34mfunction[39;49;00m [32mFindLine[39;49;00m(SL: TStrings; [34mconst[39;49;00m S: [34mstring[39;49;00m): [36mInteger[39;49;00m;

[34mprocedure[39;49;00m [32mQuickSortSL[39;49;00m(SL: TStringList);

[37m{ TStrA }[39;49;00m
[34mfunction[39;49;00m [32mIncStrA[39;49;00m(StrA: TStrA): [36mInteger[39;49;00m;

[37m{ TByteA }[39;49;00m
[34mfunction[39;49;00m [32mStrOfByteA[39;49;00m(a: TByteA): [34mstring[39;49;00m;
[34mfunction[39;49;00m [32mByteAOfStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): TByteA;
[34mfunction[39;49;00m [32mByteAOfInt[39;49;00m(i: [36mInteger[39;49;00m): TByteA;
[34mfunction[39;49;00m [32mIntOfByteA[39;49;00m(A: TByteA): [36mInteger[39;49;00m;
[34mfunction[39;49;00m [32mByteAOfHex[39;49;00m([34mconst[39;49;00m Hex: [34mstring[39;49;00m): TByteA;

[34mfunction[39;49;00m [32mSameByteA[39;49;00m([34mconst[39;49;00m A, B: TByteA): [36mBoolean[39;49;00m;
[34mfunction[39;49;00m [32mReverse[39;49;00m(a: TByteA): TByteA;
[34mfunction[39;49;00m [32mSaveByteA[39;49;00m(Data: TByteA; [34mconst[39;49;00m FileName: [34mstring[39;49;00m; Overwrite: [36mBoolean[39;49;00m = [34mTrue[39;49;00m): [36mBoolean[39;49;00m;
[34mfunction[39;49;00m [32mLoadByteA[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m): TByteA;

[34mfunction[39;49;00m [32mEndian[39;49;00m(i: [36mInteger[39;49;00m): [36mInteger[39;49;00m;

[37m{ Files }[39;49;00m
[34mfunction[39;49;00m [32mSizeOfFile[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m): [36mInteger[39;49;00m;
[34mfunction[39;49;00m [32mFileEx[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m; AllowFolders: [36mBoolean[39;49;00m = [34mFalse[39;49;00m): [36mBoolean[39;49;00m;
[34mfunction[39;49;00m [32mLWPSolve[39;49;00m([34mconst[39;49;00m Dir: [34mstring[39;49;00m): [34mstring[39;49;00m;
[34mfunction[39;49;00m [32mLWPSlash[39;49;00m([34mconst[39;49;00m Dir: [34mstring[39;49;00m): [34mstring[39;49;00m;

[34mfunction[39;49;00m [32mExtractDrive[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m): [34mstring[39;49;00m;
[34mfunction[39;49;00m [32mExtractPath[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m): [34mstring[39;49;00m;
[34mfunction[39;49;00m [32mExtractPrefix[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m): [34mstring[39;49;00m;
[34mfunction[39;49;00m [32mExtractSuffix[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m): [34mstring[39;49;00m;

[34mfunction[39;49;00m [32mIsValidFileName[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m): [36mBoolean[39;49;00m;
[34mfunction[39;49;00m [32mMakeValidFileName[39;49;00m(FileName: [34mstring[39;49;00m; [34mconst[39;49;00m [34mDefault[39;49;00m: [34mstring[39;49;00m = [33m'[39;49;00m[33mFile[39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;

[37m{ Converting }[39;49;00m
[34mfunction[39;49;00m [32mIsValidInteger[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [36mBoolean[39;49;00m;
[34mfunction[39;49;00m [32mIsValidCardinal[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [36mBoolean[39;49;00m;

[34mfunction[39;49;00m [32mStrOfBool[39;49;00m(flag: [36mBoolean[39;49;00m; [34mconst[39;49;00m TrueStr: [34mstring[39;49;00m = [33m'[39;49;00m[33mTrue[39;49;00m[33m'[39;49;00m;
  [34mconst[39;49;00m FalseStr: [34mstring[39;49;00m = [33m'[39;49;00m[33mFalse[39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;
[34mfunction[39;49;00m [32mStrOfInt[39;49;00m(i: [36mInteger[39;49;00m): [34mstring[39;49;00m;
[34mfunction[39;49;00m [32mCardOfStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [36mCardinal[39;49;00m;

[34mfunction[39;49;00m [32mHexOrd[39;49;00m(Hex: [36mChar[39;49;00m): THex;
[34mfunction[39;49;00m [32mByteOfHex[39;49;00m(Hex: THexByteStr): [36mByte[39;49;00m;

[34mfunction[39;49;00m [32mDecOfHex[39;49;00m([34mconst[39;49;00m Hex: [34mstring[39;49;00m): [34mstring[39;49;00m;
[34mfunction[39;49;00m [32mHexOfByte[39;49;00m(b: [36mByte[39;49;00m): THexByteStr;
[34mfunction[39;49;00m [32mHexOfCard[39;49;00m(i: [36mCardinal[39;49;00m): [34mstring[39;49;00m; overload;
[34mfunction[39;49;00m [32mHexOfCard[39;49;00m(i: [36mCardinal[39;49;00m; Digits: [36mInteger[39;49;00m): [34mstring[39;49;00m; overload;

[34mfunction[39;49;00m [32mPascalHexArray[39;49;00m(a: TByteA; [34mName[39;49;00m: [34mstring[39;49;00m): [34mstring[39;49;00m;

[34mfunction[39;49;00m [32mHexOfByteA[39;49;00m(a: TByteA; Blocks: [36mInteger[39;49;00m = [34m1[39;49;00m;
  [34mconst[39;49;00m Splitter: [34mstring[39;49;00m = [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;
[34mfunction[39;49;00m [32mBinOfByteA[39;49;00m(a: TByteA; Blocks: [36mInteger[39;49;00m = [34m4[39;49;00m;
  [34mconst[39;49;00m Splitter: [34mstring[39;49;00m = [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;

[34mfunction[39;49;00m [32mCardOfHex[39;49;00m(Hex: [34mstring[39;49;00m): [36mCardinal[39;49;00m;
[34mfunction[39;49;00m [32mIntOfBin[39;49;00m(Bin: [34mstring[39;49;00m): [36mCardinal[39;49;00m;

[34mfunction[39;49;00m [32mBinOfIntFill[39;49;00m(n: [36mcardinal[39;49;00m; MinCount: [36mInteger[39;49;00m = [34m8[39;49;00m): [34mstring[39;49;00m;
[34mfunction[39;49;00m [32mBinOfInt[39;49;00m(n: [36mcardinal[39;49;00m): [34mstring[39;49;00m;

[34mfunction[39;49;00m [32mBaseNOfInt[39;49;00m(I: [36mCardinal[39;49;00m; B: TBaseN): [34mstring[39;49;00m;
[34mfunction[39;49;00m [32mIntOfBaseN[39;49;00m(V: [34mstring[39;49;00m; B: TBaseN): [36mCardinal[39;49;00m;

[37m{ Ranges }[39;49;00m
[34mfunction[39;49;00m [32mKeepIn[39;49;00m(i, Bottom, Top: [36mVariant[39;49;00m): [36mVariant[39;49;00m;
[34mfunction[39;49;00m [32mInRange[39;49;00m(Value, Bottom, Top: [36mVariant[39;49;00m): [36mBoolean[39;49;00m;
[34mfunction[39;49;00m [32mInStrictRange[39;49;00m(Value, Bottom, Top: [36mVariant[39;49;00m): [36mBoolean[39;49;00m;
[34mfunction[39;49;00m [32mMin[39;49;00m([34mconst[39;49;00m A, B: [36mInteger[39;49;00m): [36mInteger[39;49;00m; overload;
[34mfunction[39;49;00m [32mMin[39;49;00m([34mconst[39;49;00m A: TIntA): [36mInteger[39;49;00m; overload;
[34mfunction[39;49;00m [32mMax[39;49;00m([34mconst[39;49;00m A, B: [36mInteger[39;49;00m): [36mInteger[39;49;00m; overload;
[34mfunction[39;49;00m [32mMax[39;49;00m([34mconst[39;49;00m A: TIntA): [36mInteger[39;49;00m; overload;

[34mconst[39;49;00m
  RangesSeparator = [33m'[39;49;00m[33m,[39;49;00m[33m'[39;49;00m;
  RangeInnerSeparator = [33m'[39;49;00m[33m-[39;49;00m[33m'[39;49;00m;
  RangeInfinite = [33m'[39;49;00m[33m*[39;49;00m[33m'[39;49;00m;
  RangeSpecialChars = [RangesSeparator, RangeInnerSeparator, RangeInfinite];

[34mfunction[39;49;00m [32mRangesOfStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): TRanges;
[34mfunction[39;49;00m [32mInRanges[39;49;00m(Ranges: TRanges; TestValue: [36mCardinal[39;49;00m): [36mBoolean[39;49;00m;

[34mfunction[39;49;00m [32mSuccess[39;49;00m(Res: [36mInteger[39;49;00m; ResultOnSuccess: [36mInteger[39;49;00m = ERROR_SUCCESS): [36mBoolean[39;49;00m;
[34mfunction[39;49;00m [32mFailure[39;49;00m(Res: [36mInteger[39;49;00m; ResultOnSuccess: [36mInteger[39;49;00m = ERROR_SUCCESS): [36mBoolean[39;49;00m;

[34mfunction[39;49;00m [32mExpandString[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [34mstring[39;49;00m;

[37m{ Files }[39;49;00m
[34mprocedure[39;49;00m [32mDeleteFiles[39;49;00m([34mconst[39;49;00m Mask: [34mstring[39;49;00m; ScanSubDirs: [36mBoolean[39;49;00m = [34mTrue[39;49;00m;
  Attributes: [36mInteger[39;49;00m = faFindEveryFile);
[34mprocedure[39;49;00m [32mFileNew[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m);
[34mfunction[39;49;00m [32mDateTimeOfFileTime[39;49;00m([34mconst[39;49;00m FileTime: TFileTime): [36mTDateTime[39;49;00m;

[37m{ FileNames }[39;49;00m
[34mfunction[39;49;00m [32mGetFileNew[39;49;00m(FileName: [34mstring[39;49;00m; NoFloppyDrives: [36mBoolean[39;49;00m = [34mTrue[39;49;00m): [34mstring[39;49;00m;

[37m{ Finding Files }[39;49;00m
[34mfunction[39;49;00m [32mFindAll[39;49;00m(Strings: TStrings; [34mconst[39;49;00m Mask: [34mstring[39;49;00m;
  ScanSubDirs: [36mBoolean[39;49;00m = [34mTrue[39;49;00m; Attributes: [36mInteger[39;49;00m = faFindEveryFile;
  FileReturn: TFileNameFunc = [34mnil[39;49;00m): [36mBoolean[39;49;00m;
[34mfunction[39;49;00m [32mFindAllFirst[39;49;00m([34mconst[39;49;00m Mask: [34mstring[39;49;00m; ScanSubDirs: [36mBoolean[39;49;00m = [34mTrue[39;49;00m;
  Attributes: [36mInteger[39;49;00m = faFindEveryFile): [34mstring[39;49;00m;

[34mfunction[39;49;00m [32mFullOSInfo[39;49;00m: [34mstring[39;49;00m;
[34mfunction[39;49;00m [32mWin32PlatformStr[39;49;00m: [34mstring[39;49;00m;
[34mfunction[39;49;00m [32mWin9x[39;49;00m: [36mBoolean[39;49;00m;
[34mfunction[39;49;00m [32mWinNT[39;49;00m: [36mBoolean[39;49;00m;
[34mfunction[39;49;00m [32mWin2000[39;49;00m: [36mBoolean[39;49;00m;
[34mfunction[39;49;00m [32mWinXP[39;49;00m: [36mBoolean[39;49;00m;

[34mvar[39;49;00m
  MyDir: [34mstring[39;49;00m = [33m'[39;49;00m[33m'[39;49;00m;
  LastSuccessRes: [36mInteger[39;49;00m = [34m0[39;49;00m;

[37m{ Backward compatibility }[39;49;00m
[37m{$IFNDEF VER130}[39;49;00m
[34mfunction[39;49;00m [32mSameText[39;49;00m([34mconst[39;49;00m S1, S2: [34mstring[39;49;00m): [36mBoolean[39;49;00m;
[37m{$ENDIF}[39;49;00m

[34mimplementation[39;49;00m
[37m{$IFNDEF VER140}[39;49;00m
[34muses[39;49;00m FileCtrl;
[37m{$ENDIF}[39;49;00m

[37m{$IFNDEF VER130}[39;49;00m
[34mfunction[39;49;00m [32mSameText[39;49;00m([34mconst[39;49;00m S1, S2: [34mstring[39;49;00m): [36mBoolean[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [36mCompareText[39;49;00m(S1, S2) = [34m0[39;49;00m;
[34mend[39;49;00m;
[37m{$ENDIF}[39;49;00m

[34mprocedure[39;49;00m [32mReport[39;49;00m([34mconst[39;49;00m ReportName, Text: [34mstring[39;49;00m);
[34mvar[39;49;00m
  F: [36mTextFile[39;49;00m;
  FileName: [34mstring[39;49;00m;
[34mbegin[39;49;00m
  FileName := MyDir + ReportName + [33m'[39;49;00m[33m.rep[39;49;00m[33m'[39;49;00m;
  Assign(F, FileName);
  [34mtry[39;49;00m
    [34mif[39;49;00m [34mnot[39;49;00m [36mFileExists[39;49;00m(FileName) [34mthen[39;49;00m
      [36mRewrite[39;49;00m(F)
    [34melse[39;49;00m
      [36mAppend[39;49;00m(F);
    [36mWriteLn[39;49;00m(F, Text);
  [34mfinally[39;49;00m
    [36mClose[39;49;00m(F);
  [34mend[39;49;00m;
[34mend[39;49;00m;

[34mprocedure[39;49;00m [32mClearReport[39;49;00m([34mconst[39;49;00m ReportName: [34mstring[39;49;00m);
[34mvar[39;49;00m
  FileName: [34mstring[39;49;00m;
[34mbegin[39;49;00m
  FileName := MyDir + ReportName + [33m'[39;49;00m[33m.rep[39;49;00m[33m'[39;49;00m;
  [36mDeleteFile[39;49;00m(FileName);
[34mend[39;49;00m;

[34mprocedure[39;49;00m [32mReportFmt[39;49;00m([34mconst[39;49;00m ReportName, Fmt: [34mstring[39;49;00m; [34mconst[39;49;00m Args: [34marray[39;49;00m [34mof[39;49;00m [34mconst[39;49;00m);
[34mbegin[39;49;00m
  Report(ReportName, [36mFormat[39;49;00m(Fmt, Args));
[34mend[39;49;00m;

[34mprocedure[39;49;00m [32mGetParams[39;49;00m(Strings: TStrings);
[34mvar[39;49;00m
  P: [36mPChar[39;49;00m;
  Param: [34mstring[39;49;00m;

  [34mfunction[39;49;00m [32mGetParamStr[39;49;00m([34mvar[39;49;00m P: [36mPChar[39;49;00m; [34mvar[39;49;00m Param: [34mstring[39;49;00m): [36mBoolean[39;49;00m;
  [34mvar[39;49;00m
    Quoted: [36mBoolean[39;49;00m;
  [34mbegin[39;49;00m
    Param := [33m'[39;49;00m[33m'[39;49;00m;

    [34mrepeat[39;49;00m
      [34mwhile[39;49;00m (P[[34m0[39;49;00m] <> [33m#0[39;49;00m) [34mand[39;49;00m (P[[34m0[39;49;00m] <= [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m) [34mdo[39;49;00m
        [36mInc[39;49;00m(P);

      Quoted := [34mFalse[39;49;00m;
      [34mwhile[39;49;00m P[[34m0[39;49;00m] <> [33m#0[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m
        [34mif[39;49;00m P[[34m0[39;49;00m] = [33m'[39;49;00m[33m"[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m
          Quoted := [34mnot[39;49;00m Quoted;
          [36mInc[39;49;00m(P);
        [34mContinue[39;49;00m; [34mend[39;49;00m;
        [34mif[39;49;00m (P[[34m0[39;49;00m] <= [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m) [34mand[39;49;00m [34mnot[39;49;00m Quoted [34mthen[39;49;00m
          [34mBreak[39;49;00m;
        Param := Param + P[[34m0[39;49;00m];
        [36mInc[39;49;00m(P);
      [34mend[39;49;00m;
    [34muntil[39;49;00m (Param <> [33m'[39;49;00m[33m'[39;49;00m) [34mor[39;49;00m (P[[34m0[39;49;00m] = [33m#0[39;49;00m);

    [36mResult[39;49;00m := Param <> [33m'[39;49;00m[33m'[39;49;00m;
  [34mend[39;49;00m;

[34mbegin[39;49;00m
  Strings.Clear;
  P := GetCommandLine;
  GetParamStr(P, Param);
  [34mwhile[39;49;00m GetParamStr(P, Param) [34mdo[39;49;00m
    Strings.Add(Param);
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mGetParams[39;49;00m([34mconst[39;49;00m Separator: [34mstring[39;49;00m = [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;
[34mvar[39;49;00m
  SL: TStringList;
[34mbegin[39;49;00m
  SL := TStringList.Create;
  GetParams(SL);
  [36mResult[39;49;00m := Join(SL, Separator);
  SL.Free;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mSwitch[39;49;00m([34mconst[39;49;00m Switch: [34mstring[39;49;00m; [34mconst[39;49;00m PrefixChars: TCharSet = SwitchChars;
  IgnoreCase: [36mBoolean[39;49;00m = [34mTrue[39;49;00m): [36mBoolean[39;49;00m;
[37m//= SysUtils.FindCmdLineSwitch[39;49;00m
[34mvar[39;49;00m
  i: [36mInteger[39;49;00m;
  s: [34mstring[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [34mTrue[39;49;00m;

  [34mfor[39;49;00m i := [34m1[39;49;00m [34mto[39;49;00m [36mParamCount[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m
    s := [36mParamStr[39;49;00m(i);

    [34mif[39;49;00m (s <> [33m'[39;49;00m[33m'[39;49;00m) [34mand[39;49;00m (s[[34m1[39;49;00m] [34min[39;49;00m PrefixChars) [34mthen[39;49;00m [34mbegin[39;49;00m
    [37m//i know that always s <> '', but this is saver[39;49;00m
      s := [36mCopy[39;49;00m(s, [34m2[39;49;00m, MaxInt);
      [34mif[39;49;00m (s = Switch) [34mor[39;49;00m (IgnoreCase [34mand[39;49;00m ([34m0[39;49;00m=[36mAnsiCompareText[39;49;00m(s, Switch))) [34mthen[39;49;00m
        [34mExit[39;49;00m;
    [34mend[39;49;00m;
  [34mend[39;49;00m;

  [36mResult[39;49;00m := [34mFalse[39;49;00m;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mParamNum[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [34mfor[39;49;00m [36mResult[39;49;00m := [34m1[39;49;00m [34mto[39;49;00m [36mParamCount[39;49;00m [34mdo[39;49;00m
    [34mif[39;49;00m [34m0[39;49;00m=[36mAnsiCompareText[39;49;00m([36mParamStr[39;49;00m([36mResult[39;49;00m), S) [34mthen[39;49;00m
      [34mExit[39;49;00m;

  [36mResult[39;49;00m := [34m0[39;49;00m;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mParamPrefixNum[39;49;00m([34mconst[39;49;00m Prefix: [34mstring[39;49;00m): [36mInteger[39;49;00m;
[34mvar[39;49;00m
  Len: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  Len := [36mLength[39;49;00m(Prefix);
  [34mfor[39;49;00m [36mResult[39;49;00m := [34m1[39;49;00m [34mto[39;49;00m [36mParamCount[39;49;00m [34mdo[39;49;00m
    [34mif[39;49;00m [34m0[39;49;00m=[36mAnsiCompareText[39;49;00m([36mCopy[39;49;00m([36mParamStr[39;49;00m([36mResult[39;49;00m), [34m1[39;49;00m, Len), Prefix) [34mthen[39;49;00m
      [34mExit[39;49;00m;

  [36mResult[39;49;00m := [34m0[39;49;00m;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mParam[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [36mBoolean[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := ParamNum(S) > [34m0[39;49;00m;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mParamPrefix[39;49;00m([34mconst[39;49;00m Prefix: [34mstring[39;49;00m): [36mBoolean[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := ParamPrefixNum(Prefix) > [34m0[39;49;00m;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mGetParam[39;49;00m([34mconst[39;49;00m Prefix: [34mstring[39;49;00m = [33m'[39;49;00m[33m'[39;49;00m; [34mconst[39;49;00m [34mDefault[39;49;00m: [34mstring[39;49;00m = [33m'[39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;
[34mvar[39;49;00m
  i: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [34mDefault[39;49;00m;

  [34mif[39;49;00m Prefix = [33m'[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m
    [36mResult[39;49;00m := [36mParamStr[39;49;00m([34m1[39;49;00m);
  [34mExit[39;49;00m; [34mend[39;49;00m;

  i := ParamPrefixNum(Prefix);
  [34mif[39;49;00m i > [34m0[39;49;00m [34mthen[39;49;00m
    [36mResult[39;49;00m := [36mCopy[39;49;00m([36mParamStr[39;49;00m(i), [36mLength[39;49;00m(Prefix) + [34m1[39;49;00m, MaxInt);
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mGetMyDir[39;49;00m(FullPath: [36mBoolean[39;49;00m = [34mFalse[39;49;00m): [34mstring[39;49;00m;
[34mvar[39;49;00m
  Buffer: [34marray[39;49;00m[[34m0[39;49;00m..[34m260[39;49;00m] [34mof[39;49;00m [36mChar[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;
  [36mSetString[39;49;00m([36mResult[39;49;00m, Buffer, [36mGetModuleFileName[39;49;00m([34m0[39;49;00m, Buffer, [36mSizeOf[39;49;00m(Buffer)));
  [34mif[39;49;00m FullPath [34mthen[39;49;00m
    [36mResult[39;49;00m := GetFileNew([36mResult[39;49;00m);
  [36mResult[39;49;00m := ExtractPath([36mResult[39;49;00m);
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mWinDir[39;49;00m: [34mstring[39;49;00m;
[34mvar[39;49;00m
  Res: [36mPChar[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m;
  [36mGetMem[39;49;00m(Res, MAX_PATH);
  GetWindowsDirectory(Res, MAX_PATH);
  [36mResult[39;49;00m := Res + [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m;
  [36mFreeMem[39;49;00m(Res, MAX_PATH);
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mSysDir[39;49;00m: [34mstring[39;49;00m;
[34mvar[39;49;00m
  Res: [36mPChar[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m;
  [36mGetMem[39;49;00m(Res, MAX_PATH);
  GetSystemDirectory(Res, MAX_PATH);
  [36mResult[39;49;00m := Res + [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m;
  [36mFreeMem[39;49;00m(Res, MAX_PATH);
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mUserName[39;49;00m: [34mstring[39;49;00m;
[34mvar[39;49;00m
  Len: [36mCardinal[39;49;00m;
  Res: [36mPChar[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;
  [36mGetMem[39;49;00m(Res, MAX_PATH);
  Len := MAX_PATH;
  GetUserName(Res, Len);
  [36mResult[39;49;00m := Res;
  [36mFreeMem[39;49;00m(Res, MAX_PATH);
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mFirstChar[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [36mChar[39;49;00m;
[34mbegin[39;49;00m
  [34mif[39;49;00m s = [33m'[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m
    [36mResult[39;49;00m := [33m#0[39;49;00m
  [34melse[39;49;00m
    [36mResult[39;49;00m := s[[34m1[39;49;00m];
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mLastChar[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [36mChar[39;49;00m;
[34mbegin[39;49;00m
  [34mif[39;49;00m s = [33m'[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m
    [36mResult[39;49;00m := [33m#0[39;49;00m
  [34melse[39;49;00m
    [36mResult[39;49;00m := s[[36mLength[39;49;00m(s)];
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mCharPos[39;49;00m(C: [36mChar[39;49;00m; [34mconst[39;49;00m S: [34mstring[39;49;00m; Offset: [36mInteger[39;49;00m = [34m1[39;49;00m): [36mInteger[39;49;00m;
[34mvar[39;49;00m
  MaxPosToSearch: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := Offset;
  MaxPosToSearch := [36mLength[39;49;00m(S);

  [34mwhile[39;49;00m [36mResult[39;49;00m <= MaxPosToSearch [34mdo[39;49;00m [34mbegin[39;49;00m
    [34mif[39;49;00m S[[36mResult[39;49;00m] = C [34mthen[39;49;00m
      [34mExit[39;49;00m;
    [36mInc[39;49;00m([36mResult[39;49;00m);
  [34mend[39;49;00m;

  [36mResult[39;49;00m := [34m0[39;49;00m;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mCharPos[39;49;00m(C: TCharSet; [34mconst[39;49;00m S: [34mstring[39;49;00m; Offset: [36mInteger[39;49;00m = [34m1[39;49;00m): [36mInteger[39;49;00m;
[34mvar[39;49;00m
  MaxPosToSearch: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := Offset;
  MaxPosToSearch := [36mLength[39;49;00m(S);

  [34mwhile[39;49;00m [36mResult[39;49;00m <= MaxPosToSearch [34mdo[39;49;00m [34mbegin[39;49;00m
    [34mif[39;49;00m S[[36mResult[39;49;00m] [34min[39;49;00m C [34mthen[39;49;00m
      [34mExit[39;49;00m;
    [36mInc[39;49;00m([36mResult[39;49;00m);
  [34mend[39;49;00m;

  [36mResult[39;49;00m := [34m0[39;49;00m;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mCharPosR[39;49;00m(C: [36mChar[39;49;00m; [34mconst[39;49;00m S: [34mstring[39;49;00m; Offset: [36mInteger[39;49;00m = -[34m1[39;49;00m): [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [34mif[39;49;00m Offset < [34m0[39;49;00m [34mthen[39;49;00m
    [36mResult[39;49;00m := [36mLength[39;49;00m(S) + [34m1[39;49;00m - Offset
  [34melse[39;49;00m
    [36mResult[39;49;00m := Offset;
  [34mif[39;49;00m [36mResult[39;49;00m > [36mLength[39;49;00m(S) [34mthen[39;49;00m
    [36mResult[39;49;00m := [36mLength[39;49;00m(S);

  [34mwhile[39;49;00m [36mResult[39;49;00m > [34m0[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m
    [34mif[39;49;00m S[[36mResult[39;49;00m] = C [34mthen[39;49;00m
      [34mExit[39;49;00m;
    [36mDec[39;49;00m([36mResult[39;49;00m);
  [34mend[39;49;00m;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mPosEx[39;49;00m([34mconst[39;49;00m SubStr, S: [34mstring[39;49;00m; Offset: [36mInteger[39;49;00m = [34m1[39;49;00m): [36mInteger[39;49;00m;
[34mvar[39;49;00m
  MaxPosToSearch, LenSubStr, i: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [34mif[39;49;00m SubStr = [33m'[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m
    [36mResult[39;49;00m := [34m0[39;49;00m;
  [34mExit[39;49;00m; [34mend[39;49;00m;

  [34mif[39;49;00m Offset < [34m1[39;49;00m [34mthen[39;49;00m
    [36mResult[39;49;00m := [34m1[39;49;00m
  [34melse[39;49;00m
    [36mResult[39;49;00m := Offset;

  LenSubStr := [36mLength[39;49;00m(SubStr);
  MaxPosToSearch := [36mLength[39;49;00m(S) - LenSubStr + [34m1[39;49;00m;

  [34mwhile[39;49;00m [36mResult[39;49;00m <= MaxPosToSearch [34mdo[39;49;00m [34mbegin[39;49;00m
    [34mif[39;49;00m S[[36mResult[39;49;00m] = SubStr[[34m1[39;49;00m] [34mthen[39;49;00m [34mbegin[39;49;00m
      i := [34m1[39;49;00m;

      [34mwhile[39;49;00m (i < LenSubStr)
       [34mand[39;49;00m (S[[36mResult[39;49;00m + i] = SubStr[i + [34m1[39;49;00m]) [34mdo[39;49;00m
        [36mInc[39;49;00m(i);

      [34mif[39;49;00m i = LenSubStr [34mthen[39;49;00m
        [34mExit[39;49;00m;
    [34mend[39;49;00m;
    [36mInc[39;49;00m([36mResult[39;49;00m);
  [34mend[39;49;00m;

  [36mResult[39;49;00m := [34m0[39;49;00m;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mPosExText[39;49;00m([34mconst[39;49;00m SubStr, S: [34mstring[39;49;00m; Offset: [36mInteger[39;49;00m = [34m1[39;49;00m): [36mInteger[39;49;00m;
[34mvar[39;49;00m
  MaxPosToSearch, LenSubStr, i: [36mInteger[39;49;00m;

  [34mfunction[39;49;00m [32mSameChar[39;49;00m(a, b: [36mChar[39;49;00m): [36mBoolean[39;49;00m;
  [34mbegin[39;49;00m
    [36mResult[39;49;00m := [36mUpCase[39;49;00m(a) = [36mUpCase[39;49;00m(b)
  [34mend[39;49;00m;

[34mbegin[39;49;00m
  [34mif[39;49;00m SubStr = [33m'[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m
    [36mResult[39;49;00m := [34m0[39;49;00m;
  [34mExit[39;49;00m; [34mend[39;49;00m;

  [34mif[39;49;00m Offset < [34m1[39;49;00m [34mthen[39;49;00m
    [36mResult[39;49;00m := [34m1[39;49;00m
  [34melse[39;49;00m
    [36mResult[39;49;00m := Offset;

  LenSubStr := [36mLength[39;49;00m(SubStr);
  MaxPosToSearch := [36mLength[39;49;00m(S) - LenSubStr + [34m1[39;49;00m;

  [34mwhile[39;49;00m [36mResult[39;49;00m <= MaxPosToSearch [34mdo[39;49;00m [34mbegin[39;49;00m
    [34mif[39;49;00m SameChar(S[[36mResult[39;49;00m], SubStr[[34m1[39;49;00m]) [34mthen[39;49;00m [34mbegin[39;49;00m
      i := [34m1[39;49;00m;

      [34mwhile[39;49;00m (i < LenSubStr)
       [34mand[39;49;00m (SameChar(S[[36mResult[39;49;00m + i], SubStr[i + [34m1[39;49;00m])) [34mdo[39;49;00m
        [36mInc[39;49;00m(i);

      [34mif[39;49;00m i = LenSubStr [34mthen[39;49;00m
        [34mExit[39;49;00m;
    [34mend[39;49;00m;
    [36mInc[39;49;00m([36mResult[39;49;00m);
  [34mend[39;49;00m;

  [36mResult[39;49;00m := [34m0[39;49;00m;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mPosExAnsiText[39;49;00m([34mconst[39;49;00m SubStr, S: [34mstring[39;49;00m; Offset: [36mInteger[39;49;00m = [34m1[39;49;00m): [36mInteger[39;49;00m;
[34mvar[39;49;00m
  MaxPosToSearch, LenSubStr, i: [36mInteger[39;49;00m;

  [34mfunction[39;49;00m [32mSameChar[39;49;00m(a, b: [36mChar[39;49;00m): [36mBoolean[39;49;00m;
  [34mbegin[39;49;00m
    [36mResult[39;49;00m := CharLower([36mPChar[39;49;00m(a)) = CharLower([36mPChar[39;49;00m(b));
  [34mend[39;49;00m;

[34mbegin[39;49;00m
  [34mif[39;49;00m SubStr = [33m'[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m
    [36mResult[39;49;00m := [34m0[39;49;00m;
  [34mExit[39;49;00m; [34mend[39;49;00m;

  [34mif[39;49;00m Offset < [34m1[39;49;00m [34mthen[39;49;00m
    [36mResult[39;49;00m := [34m1[39;49;00m
  [34melse[39;49;00m
    [36mResult[39;49;00m := Offset;

  LenSubStr := [36mLength[39;49;00m(SubStr);
  MaxPosToSearch := [36mLength[39;49;00m(S) - LenSubStr + [34m1[39;49;00m;

  [34mwhile[39;49;00m [36mResult[39;49;00m <= MaxPosToSearch [34mdo[39;49;00m [34mbegin[39;49;00m
    [34mif[39;49;00m SameChar(S[[36mResult[39;49;00m], SubStr[[34m1[39;49;00m]) [34mthen[39;49;00m [34mbegin[39;49;00m
      i := [34m1[39;49;00m;

      [34mwhile[39;49;00m (i < LenSubStr)
       [34mand[39;49;00m (SameChar(S[[36mResult[39;49;00m + i], SubStr[i + [34m1[39;49;00m])) [34mdo[39;49;00m
        [36mInc[39;49;00m(i);

      [34mif[39;49;00m i = LenSubStr [34mthen[39;49;00m
        [34mExit[39;49;00m;
    [34mend[39;49;00m;
    [36mInc[39;49;00m([36mResult[39;49;00m);
  [34mend[39;49;00m;

  [36mResult[39;49;00m := [34m0[39;49;00m;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mUntilChar[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Brake: [36mChar[39;49;00m): [34mstring[39;49;00m;
[34mvar[39;49;00m
  p: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  p := CharPos(Brake, S);

  [34mif[39;49;00m p > [34m0[39;49;00m [34mthen[39;49;00m
    [36mResult[39;49;00m := [36mCopy[39;49;00m(S, [34m1[39;49;00m, p - [34m1[39;49;00m)
  [34melse[39;49;00m
    [36mResult[39;49;00m := S;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mUntilChar[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Brake: TCharSet): [34mstring[39;49;00m;
[34mvar[39;49;00m
  p: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;
  p := CharPos(Brake, S);

  [34mif[39;49;00m p > [34m0[39;49;00m [34mthen[39;49;00m
    [36mResult[39;49;00m := [36mCopy[39;49;00m(S, [34m1[39;49;00m, p - [34m1[39;49;00m)
  [34melse[39;49;00m
    [36mResult[39;49;00m := S;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mUntilLastChar[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Brake: [36mChar[39;49;00m;
  IgnoreNoBrake: [36mBoolean[39;49;00m = [34mTrue[39;49;00m): [34mstring[39;49;00m;
[34mvar[39;49;00m
  p: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;
  p := CharPosR(Brake, S);

  [34mif[39;49;00m p > [34m0[39;49;00m [34mthen[39;49;00m
    [36mResult[39;49;00m := [36mCopy[39;49;00m(S, [34m1[39;49;00m, p - [34m1[39;49;00m)
  [34melse[39;49;00m [34mif[39;49;00m IgnoreNoBrake [34mthen[39;49;00m
    [36mResult[39;49;00m := S;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mFromChar[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Brake: [36mChar[39;49;00m): [34mstring[39;49;00m;
[34mvar[39;49;00m
  p: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;
  p := CharPos(Brake, S);

  [34mif[39;49;00m p > [34m0[39;49;00m [34mthen[39;49;00m
    [36mResult[39;49;00m := [36mCopy[39;49;00m(S, p + [34m1[39;49;00m, [36mLength[39;49;00m(S) - p);
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mFromChar[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Brake: TCharSet): [34mstring[39;49;00m;
[34mvar[39;49;00m
  p: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;
  p := CharPos(Brake, S);

  [34mif[39;49;00m p > [34m0[39;49;00m [34mthen[39;49;00m
    [36mResult[39;49;00m := [36mCopy[39;49;00m(S, p + [34m1[39;49;00m, [36mLength[39;49;00m(S) - p);
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mFromLastChar[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Brake: [36mChar[39;49;00m;
  IgnoreNoBrake: [36mBoolean[39;49;00m = [34mFalse[39;49;00m): [34mstring[39;49;00m;
[34mvar[39;49;00m
  p: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;
  p := CharPosR(Brake, S);

  [34mif[39;49;00m p > [34m0[39;49;00m [34mthen[39;49;00m
    [36mResult[39;49;00m := [36mCopy[39;49;00m(S, p + [34m1[39;49;00m, [36mLength[39;49;00m(S) - p)
  [34melse[39;49;00m [34mif[39;49;00m IgnoreNoBrake [34mthen[39;49;00m
    [36mResult[39;49;00m := S;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mBetweenChars[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Start, Finish: [36mChar[39;49;00m;
  Inclusive: [36mBoolean[39;49;00m = [34mFalse[39;49;00m): [34mstring[39;49;00m;
[34mvar[39;49;00m
  p, fin: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;

  p := CharPos(Start, S);
  [34mif[39;49;00m p = [34m0[39;49;00m [34mthen[39;49;00m
    [34mExit[39;49;00m;

  fin := CharPos(Finish, S, p + [34m1[39;49;00m);
  [34mif[39;49;00m fin = [34m0[39;49;00m [34mthen[39;49;00m
    [34mExit[39;49;00m;

  [34mif[39;49;00m [34mnot[39;49;00m Inclusive [34mthen[39;49;00m [34mbegin[39;49;00m
    [36mInc[39;49;00m(p);
    [36mDec[39;49;00m(fin);
  [34mend[39;49;00m;

  [36mResult[39;49;00m := [36mCopy[39;49;00m(S, p, fin - p + [34m1[39;49;00m);
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mUntilStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Brake: [34mstring[39;49;00m): [34mstring[39;49;00m;
[34mvar[39;49;00m
  p: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [34mif[39;49;00m [36mLength[39;49;00m(Brake) = [34m1[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m
    [36mResult[39;49;00m := UntilChar(S, Brake[[34m1[39;49;00m]);
  [34mExit[39;49;00m; [34mend[39;49;00m;

  p := PosEx(Brake, S);

  [34mif[39;49;00m p > [34m0[39;49;00m [34mthen[39;49;00m
    [36mResult[39;49;00m := [36mCopy[39;49;00m(S, [34m1[39;49;00m, p - [34m1[39;49;00m)
  [34melse[39;49;00m
    [36mResult[39;49;00m := S;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mFromStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Brake: [34mstring[39;49;00m): [34mstring[39;49;00m;
[34mvar[39;49;00m
  p: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [34mif[39;49;00m [36mLength[39;49;00m(Brake) = [34m1[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m
    [36mResult[39;49;00m := FromChar(S, Brake[[34m1[39;49;00m]);
  [34mExit[39;49;00m; [34mend[39;49;00m;

  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;
  p := PosEx(Brake, s);

  [34mif[39;49;00m p > [34m0[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m
    [36mInc[39;49;00m(p, [36mLength[39;49;00m(Brake));
    [36mResult[39;49;00m := [36mCopy[39;49;00m(S, p, [36mLength[39;49;00m(S) - p + [34m1[39;49;00m);
  [34mend[39;49;00m;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mStringWrap[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Width: [36mInteger[39;49;00m; [34mconst[39;49;00m LineEnd: [34mstring[39;49;00m = EOL): [34mstring[39;49;00m;
[34mvar[39;49;00m
  i: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;
  [34mif[39;49;00m (S = [33m'[39;49;00m[33m'[39;49;00m) [34mor[39;49;00m (Width < [34m1[39;49;00m) [34mthen[39;49;00m
    [34mExit[39;49;00m;

  i := [34m1[39;49;00m;
  [34mwhile[39;49;00m [34mTrue[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m
    [36mResult[39;49;00m := [36mResult[39;49;00m + [36mCopy[39;49;00m(S, i, Width);
    [36mInc[39;49;00m(i, Width);
    [34mif[39;49;00m i <= [36mLength[39;49;00m(S) [34mthen[39;49;00m
      [36mResult[39;49;00m := [36mResult[39;49;00m + LineEnd
    [34melse[39;49;00m
      [34mExit[39;49;00m;
  [34mend[39;49;00m;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mSplit[39;49;00m([34mconst[39;49;00m S, Separator: [34mstring[39;49;00m; IgnoreMultiSep: [36mBoolean[39;49;00m = [34mTrue[39;49;00m;
  MinCount: [36mInteger[39;49;00m = [34m0[39;49;00m): TStrA;
[34mvar[39;49;00m
  p, fin, SepLen: [36mInteger[39;49;00m;

  [34mprocedure[39;49;00m [32mAdd[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m);
  [34mbegin[39;49;00m
    [34mif[39;49;00m IgnoreMultiSep [34mand[39;49;00m (S = [33m'[39;49;00m[33m'[39;49;00m) [34mthen[39;49;00m
      [34mExit[39;49;00m;
    [36mSetLength[39;49;00m([36mResult[39;49;00m, [36mLength[39;49;00m([36mResult[39;49;00m) + [34m1[39;49;00m);
    [36mResult[39;49;00m[[36mHigh[39;49;00m([36mResult[39;49;00m)] := S;
  [34mend[39;49;00m;

[34mbegin[39;49;00m
  [34mif[39;49;00m S = [33m'[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m
    [34mif[39;49;00m [36mLength[39;49;00m([36mResult[39;49;00m) < MinCount [34mthen[39;49;00m
      [36mSetLength[39;49;00m([36mResult[39;49;00m, MinCount);
  [34mExit[39;49;00m; [34mend[39;49;00m;

  [36mResult[39;49;00m := [34mnil[39;49;00m;
  SepLen := [36mLength[39;49;00m(Separator);

  p := [34m1[39;49;00m;
  fin := PosEx(Separator, S);
  [34mwhile[39;49;00m fin > [34m0[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m
    Add([36mCopy[39;49;00m(S, p, fin - p));
    p := fin + SepLen;
    fin := PosEx(Separator, S, p);
  [34mend[39;49;00m;
  Add([36mCopy[39;49;00m(S, p, [36mLength[39;49;00m(S) - p + [34m1[39;49;00m));

  [34mif[39;49;00m [36mLength[39;49;00m([36mResult[39;49;00m) < MinCount [34mthen[39;49;00m
    [36mSetLength[39;49;00m([36mResult[39;49;00m, MinCount);
[34mend[39;49;00m;

[34mprocedure[39;49;00m [32mSplit[39;49;00m([34mconst[39;49;00m S, Separator: [34mstring[39;49;00m; Strings: TStrings;
  IgnoreMultiSep: [36mBoolean[39;49;00m = [34mTrue[39;49;00m);
[34mvar[39;49;00m
  p, fin, SepLen: [36mInteger[39;49;00m;

  [34mprocedure[39;49;00m [32mAdd[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m);
  [34mbegin[39;49;00m
    [34mif[39;49;00m IgnoreMultiSep [34mand[39;49;00m (S = [33m'[39;49;00m[33m'[39;49;00m) [34mthen[39;49;00m
      [34mExit[39;49;00m;
    Strings.Add(S);
  [34mend[39;49;00m;

[34mbegin[39;49;00m
  [34mif[39;49;00m S = [33m'[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m
    [34mExit[39;49;00m;

  Strings.BeginUpdate;
  SepLen := [36mLength[39;49;00m(Separator);
  p := [34m1[39;49;00m;
  fin := PosEx(Separator, S);
  [34mwhile[39;49;00m fin > [34m0[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m
    Add([36mCopy[39;49;00m(S, p, fin - p));
    p := fin + SepLen;
    fin := PosEx(Separator, S, p);
  [34mend[39;49;00m;
  Add([36mCopy[39;49;00m(S, p, [36mLength[39;49;00m(S) - p + [34m1[39;49;00m));
  Strings.EndUpdate;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mSplit[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Separators: TCharSet;
  IgnoreMultiSep: [36mBoolean[39;49;00m = [34mTrue[39;49;00m; MinCount: [36mInteger[39;49;00m = [34m0[39;49;00m): TStrA;
[34mvar[39;49;00m
  p, fin: [36mInteger[39;49;00m;

  [34mprocedure[39;49;00m [32mAdd[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m);
  [34mbegin[39;49;00m
    [34mif[39;49;00m IgnoreMultiSep [34mand[39;49;00m (S = [33m'[39;49;00m[33m'[39;49;00m) [34mthen[39;49;00m
      [34mExit[39;49;00m;
    [36mSetLength[39;49;00m([36mResult[39;49;00m, [36mLength[39;49;00m([36mResult[39;49;00m) + [34m1[39;49;00m);
    [36mResult[39;49;00m[[36mHigh[39;49;00m([36mResult[39;49;00m)] := S;
  [34mend[39;49;00m;

[34mbegin[39;49;00m
  [34mif[39;49;00m S = [33m'[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m
    [34mif[39;49;00m [36mLength[39;49;00m([36mResult[39;49;00m) < MinCount [34mthen[39;49;00m
      [36mSetLength[39;49;00m([36mResult[39;49;00m, MinCount);
  [34mExit[39;49;00m; [34mend[39;49;00m;

  [36mResult[39;49;00m := [34mnil[39;49;00m;

  p := [34m1[39;49;00m;
  fin := CharPos(Separators, S);
  [34mwhile[39;49;00m fin > [34m0[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m
    Add([36mCopy[39;49;00m(S, p, fin - p));
    p := fin + [34m1[39;49;00m;
    fin := CharPos(Separators, S, p);
  [34mend[39;49;00m;
  Add([36mCopy[39;49;00m(S, p, [36mLength[39;49;00m(S) - p + [34m1[39;49;00m));

  [34mif[39;49;00m [36mLength[39;49;00m([36mResult[39;49;00m) < MinCount [34mthen[39;49;00m
    [36mSetLength[39;49;00m([36mResult[39;49;00m, MinCount);
[34mend[39;49;00m;

[34mprocedure[39;49;00m [32mTileStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; BrakeStart: [36mInteger[39;49;00m; BrakeEnd: [36mInteger[39;49;00m;
  out Left, Right: [34mstring[39;49;00m);
[34mbegin[39;49;00m
  Left := [36mCopy[39;49;00m(S, [34m1[39;49;00m, BrakeStart-[34m1[39;49;00m);
  Right := [36mCopy[39;49;00m(S, BrakeEnd + [34m1[39;49;00m, MaxInt);
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mJoin[39;49;00m(Strings: TStrings; Separator: [34mstring[39;49;00m = [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;
[34mvar[39;49;00m
  i, imax: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;
  imax := Strings.Count-[34m1[39;49;00m;
  [34mfor[39;49;00m i := [34m0[39;49;00m [34mto[39;49;00m imax [34mdo[39;49;00m [34mbegin[39;49;00m
    [36mResult[39;49;00m := [36mResult[39;49;00m + Strings[i];
    [34mif[39;49;00m i < imax [34mthen[39;49;00m
      [36mResult[39;49;00m := [36mResult[39;49;00m + Separator;
  [34mend[39;49;00m;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mJoin[39;49;00m(StrA: TStrA; Separator: [34mstring[39;49;00m = [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m; overload;
[34mvar[39;49;00m
  i: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;
  [34mfor[39;49;00m i := [34m0[39;49;00m [34mto[39;49;00m [36mHigh[39;49;00m(StrA) [34mdo[39;49;00m [34mbegin[39;49;00m
    [36mResult[39;49;00m := [36mResult[39;49;00m + StrA[i];
    [34mif[39;49;00m i < [36mHigh[39;49;00m(StrA) [34mthen[39;49;00m
      [36mResult[39;49;00m := [36mResult[39;49;00m + Separator;
  [34mend[39;49;00m;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mMulStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Count: [36mInteger[39;49;00m): [34mstring[39;49;00m;
[34mvar[39;49;00m
  P: [36mPChar[39;49;00m;
  Len, i: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;
  [34mif[39;49;00m Count = [34m0[39;49;00m [34mthen[39;49;00m
    [34mExit[39;49;00m;

  Len := [36mLength[39;49;00m(S);
  [36mSetLength[39;49;00m([36mResult[39;49;00m, Len * Count);

  P := [36mPointer[39;49;00m([36mResult[39;49;00m);
  [34mfor[39;49;00m i := [34m1[39;49;00m [34mto[39;49;00m Count [34mdo[39;49;00m [34mbegin[39;49;00m
    [36mMove[39;49;00m([36mPointer[39;49;00m(S)^, P^, Len);
    [36mInc[39;49;00m(P, Len);
  [34mend[39;49;00m;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mAlignR[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Width: [36mInteger[39;49;00m; Filler: [36mChar[39;49;00m = [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := MulStr(Filler, Width - [36mLength[39;49;00m(S)) + S;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mMaxStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; MaxLen: [36mInteger[39;49;00m): [34mstring[39;49;00m;
[34mvar[39;49;00m
  Len: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  Len := [36mLength[39;49;00m(S);
  [34mif[39;49;00m Len <= MaxLen [34mthen[39;49;00m [34mbegin[39;49;00m
    [36mResult[39;49;00m := S;
  [34mExit[39;49;00m [34mend[39;49;00m;

  [36mResult[39;49;00m := [36mCopy[39;49;00m(S, [34m1[39;49;00m, MaxLen - [34m3[39;49;00m) + [33m'[39;49;00m[33m...[39;49;00m[33m'[39;49;00m;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mTrimAll[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [34mstring[39;49;00m;
[34mvar[39;49;00m
  i: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [34mfor[39;49;00m i := [34m1[39;49;00m [34mto[39;49;00m [36mLength[39;49;00m(S) [34mdo[39;49;00m
    [34mif[39;49;00m S[i] > [33m#32[39;49;00m [34mthen[39;49;00m
      [36mResult[39;49;00m := [36mResult[39;49;00m + S[i];
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mControlChar[39;49;00m(C: [36mChar[39;49;00m): [36mBoolean[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := C [34min[39;49;00m StrangeChars;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mFriendlyChar[39;49;00m(C: [36mChar[39;49;00m): [36mChar[39;49;00m;
[34mbegin[39;49;00m
  [34mcase[39;49;00m C [34mof[39;49;00m
    [33m#0[39;49;00m: [36mResult[39;49;00m := [33m'[39;49;00m[33m.[39;49;00m[33m'[39;49;00m;
    [33m#1[39;49;00m..[33m#31[39;49;00m: [36mResult[39;49;00m := [33m'[39;49;00m[33m?[39;49;00m[33m'[39;49;00m;
    [33m#255[39;49;00m: [36mResult[39;49;00m := [33m'[39;49;00m[33m#[39;49;00m[33m'[39;49;00m;
  [34melse[39;49;00m
    [36mResult[39;49;00m := C;
  [34mend[39;49;00m;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mFriendlyStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [34mstring[39;49;00m;
[34mvar[39;49;00m
  i: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [36mSetLength[39;49;00m([36mResult[39;49;00m, [36mLength[39;49;00m(S));
  [34mfor[39;49;00m i := [34m1[39;49;00m [34mto[39;49;00m [36mLength[39;49;00m(S) [34mdo[39;49;00m
    [36mResult[39;49;00m[i] := FriendlyChar(S[i]);
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mFriendlyStr[39;49;00m(a: TByteA): [34mstring[39;49;00m;
[34mvar[39;49;00m
  i: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [36mSetLength[39;49;00m([36mResult[39;49;00m, [36mLength[39;49;00m(a));
  [34mfor[39;49;00m i := [34m0[39;49;00m [34mto[39;49;00m [36mHigh[39;49;00m(a) [34mdo[39;49;00m
    [36mResult[39;49;00m[i + [34m1[39;49;00m] := FriendlyChar([36mChar[39;49;00m(a[i]));
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mQuote[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Quoter: [36mChar[39;49;00m = [33m'[39;49;00m[33m"[39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := S;

  [34mif[39;49;00m FirstChar(S) <> Quoter [34mthen[39;49;00m
    [36mResult[39;49;00m := Quoter + [36mResult[39;49;00m;

  [34mif[39;49;00m LastChar(S) <> Quoter [34mthen[39;49;00m
    [36mResult[39;49;00m := [36mResult[39;49;00m + Quoter;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mDeQuote[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [34mstring[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;
  [34mif[39;49;00m [36mLength[39;49;00m(S) > [34m2[39;49;00m [34mthen[39;49;00m
    [36mResult[39;49;00m := [36mCopy[39;49;00m(S, [34m2[39;49;00m, [36mLength[39;49;00m(S) - [34m2[39;49;00m);
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mUnQuote[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [34mstring[39;49;00m;
[34mvar[39;49;00m
  Start, Len: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  Start := [34m1[39;49;00m;
  Len := [36mLength[39;49;00m(S);

  [34mif[39;49;00m (S <> [33m'[39;49;00m[33m'[39;49;00m) [34mand[39;49;00m (S[[34m1[39;49;00m] [34min[39;49;00m ([[33m#0[39;49;00m..[33m#32[39;49;00m] + QuoteChars)) [34mthen[39;49;00m [34mbegin[39;49;00m
    [34mif[39;49;00m (LastChar(S) = S[[34m1[39;49;00m]) [34mthen[39;49;00m
      [36mDec[39;49;00m(Len);
    [36mInc[39;49;00m(Start);
  [34mend[39;49;00m;

  [36mResult[39;49;00m := [36mCopy[39;49;00m(S, Start, Len - Start + [34m1[39;49;00m);
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mStrNumerus[39;49;00m([34mconst[39;49;00m Value: [36mInteger[39;49;00m; [34mconst[39;49;00m Singular, Plural: [34mstring[39;49;00m;
  [34mconst[39;49;00m Zero: [34mstring[39;49;00m = [33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;
[34mbegin[39;49;00m
  [34mif[39;49;00m [36mAbs[39;49;00m(Value) = [34m1[39;49;00m [34mthen[39;49;00m
    [36mResult[39;49;00m := [36mIntToStr[39;49;00m(Value) + [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m + Singular
  [34melse[39;49;00m [34mif[39;49;00m Value = [34m0[39;49;00m [34mthen[39;49;00m
    [36mResult[39;49;00m := Zero + [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m + Plural
  [34melse[39;49;00m
    [36mResult[39;49;00m := [36mIntToStr[39;49;00m(Value) + [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m + Plural;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mMakeStr[39;49;00m([34mconst[39;49;00m Items: [34marray[39;49;00m [34mof[39;49;00m [34mconst[39;49;00m; Separator: [34mstring[39;49;00m = [33m'[39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;
[34mconst[39;49;00m
  BoolStrings: [34marray[39;49;00m[[36mBoolean[39;49;00m] [34mof[39;49;00m [34mstring[39;49;00m = ([33m'[39;49;00m[33mFalse[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mTrue[39;49;00m[33m'[39;49;00m);

[34mvar[39;49;00m
  i: [36mInteger[39;49;00m;

  [34mfunction[39;49;00m [32mStrOfP[39;49;00m(P: [36mPointer[39;49;00m): [34mstring[39;49;00m;
  [34mbegin[39;49;00m
    [34mif[39;49;00m P = [34mnil[39;49;00m [34mthen[39;49;00m
      [36mResult[39;49;00m := [33m'[39;49;00m[33m[nil][39;49;00m[33m'[39;49;00m
    [34melse[39;49;00m
      [36mResult[39;49;00m := [33m'[39;49;00m[33m[[39;49;00m[33m'[39;49;00m + [36mIntToStr[39;49;00m([36mCardinal[39;49;00m(P)) + [33m'[39;49;00m[33m][39;49;00m[33m'[39;49;00m;
  [34mend[39;49;00m;

  [34mprocedure[39;49;00m [32mAdd[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m);
  [34mbegin[39;49;00m
    [36mResult[39;49;00m := [36mResult[39;49;00m + s + Separator;
  [34mend[39;49;00m;

[34mbegin[39;49;00m
  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;
  [34mfor[39;49;00m i := [34m0[39;49;00m [34mto[39;49;00m [36mHigh[39;49;00m(Items) [34mdo[39;49;00m
    [34mwith[39;49;00m Items[i] [34mdo[39;49;00m
      [34mcase[39;49;00m VType [34mof[39;49;00m
        vtString:     Add(VString^);
        vtInteger:    Add([36mIntToStr[39;49;00m(VInteger));
        vtBoolean:    Add(BoolStrings[VBoolean]);
        vtChar:       Add(VChar);
        vtPChar:      Add(VPChar);
        vtExtended:   Add([36mFloatToStr[39;49;00m(VExtended^));
        vtObject:     [34mif[39;49;00m VObject [34mis[39;49;00m TComponent [34mthen[39;49;00m
                        Add(TComponent(VObject).Name)
                      [34melse[39;49;00m
                        Add(VObject.ClassName);
        vtClass:      Add(VClass.ClassName);
        vtAnsiString: Add([34mstring[39;49;00m(VAnsiString));
        vtCurrency:   Add([36mCurrToStr[39;49;00m(VCurrency^));
        vtInt64:      Add([36mIntToStr[39;49;00m(VInt64^));
        vtVariant:    Add([34mstring[39;49;00m(VVariant^));

        vtWideChar:   Add(VWideChar);
        vtPWideChar:  Add(VPWideChar);
        vtInterface:  Add(StrOfP(VInterface));
        vtPointer:    Add(StrOfP(VPointer));
        vtWideString: Add([36mWideString[39;49;00m(VWideString));
      [34mend[39;49;00m;
  [34mif[39;49;00m [36mResult[39;49;00m <> [33m'[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m
    [36mSetLength[39;49;00m([36mresult[39;49;00m, [36mLength[39;49;00m([36mResult[39;49;00m) - [36mLength[39;49;00m(Separator));
[34mend[39;49;00m;

[34mprocedure[39;49;00m [32mShowText[39;49;00m([34mconst[39;49;00m Items: [34marray[39;49;00m [34mof[39;49;00m [34mconst[39;49;00m; Separator: [34mstring[39;49;00m = [33m'[39;49;00m[33m'[39;49;00m);
[34mvar[39;49;00m
  Text: [34mstring[39;49;00m;
[34mbegin[39;49;00m
  Text := MakeStr(Items, Separator);

  MessageBox([34m0[39;49;00m, [36mPChar[39;49;00m(Text), [33m'[39;49;00m[33mInfo[39;49;00m[33m'[39;49;00m, MB_OK [34mand[39;49;00m MB_APPLMODAL);
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mDeleteChars[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; C: [36mChar[39;49;00m): [34mstring[39;49;00m;
[34mvar[39;49;00m
  i: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;
  [34mfor[39;49;00m i := [34m1[39;49;00m [34mto[39;49;00m [36mLength[39;49;00m(S) [34mdo[39;49;00m
    [34mif[39;49;00m S[i] <> C [34mthen[39;49;00m
      [36mResult[39;49;00m := [36mResult[39;49;00m + S[i];
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mDeleteChars[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; C: TCharSet): [34mstring[39;49;00m;
[34mvar[39;49;00m
  i: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;
  [34mfor[39;49;00m i := [34m1[39;49;00m [34mto[39;49;00m [36mLength[39;49;00m(S) [34mdo[39;49;00m
    [34mif[39;49;00m [34mnot[39;49;00m (S[i] [34min[39;49;00m C) [34mthen[39;49;00m
      [36mResult[39;49;00m := [36mResult[39;49;00m + S[i];
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mExtractChars[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; C: TCharSet): [34mstring[39;49;00m;
[34mvar[39;49;00m
  i: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;
  [34mfor[39;49;00m i := [34m1[39;49;00m [34mto[39;49;00m [36mLength[39;49;00m(S) [34mdo[39;49;00m
    [34mif[39;49;00m S[i] [34min[39;49;00m C [34mthen[39;49;00m
      [36mResult[39;49;00m := [36mResult[39;49;00m + S[i];
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mCharCount[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; C: [36mChar[39;49;00m): [36mInteger[39;49;00m;
[34mvar[39;49;00m
  i: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [34m0[39;49;00m;
  [34mfor[39;49;00m i := [34m1[39;49;00m [34mto[39;49;00m [36mLength[39;49;00m(S) [34mdo[39;49;00m
    [34mif[39;49;00m S[i] = C [34mthen[39;49;00m
      [36mInc[39;49;00m([36mResult[39;49;00m);
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mStrAtPos[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; [36mPos[39;49;00m: [36mInteger[39;49;00m; [34mconst[39;49;00m [36mStr[39;49;00m: [34mstring[39;49;00m): [36mBoolean[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := ([36mStr[39;49;00m <> [33m'[39;49;00m[33m'[39;49;00m) [34mand[39;49;00m ([36mStr[39;49;00m = [36mCopy[39;49;00m(S, [36mPos[39;49;00m, [36mLength[39;49;00m([36mStr[39;49;00m)));
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mTextAtPos[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; [36mPos[39;49;00m: [36mInteger[39;49;00m; [34mconst[39;49;00m Text: [34mstring[39;49;00m): [36mBoolean[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := (Text <> [33m'[39;49;00m[33m'[39;49;00m) [34mand[39;49;00m [36mSameText[39;49;00m(Text, [36mCopy[39;49;00m(S, [36mPos[39;49;00m, [36mLength[39;49;00m(Text)));
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mStrAtBegin[39;49;00m([34mconst[39;49;00m S, [36mStr[39;49;00m: [34mstring[39;49;00m): [36mBoolean[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := StrAtPos(S, [34m1[39;49;00m, [36mStr[39;49;00m);
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mTextAtBegin[39;49;00m([34mconst[39;49;00m S, Text: [34mstring[39;49;00m): [36mBoolean[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := TextAtPos(S, [34m1[39;49;00m, Text);
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mCharIn[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; C: [36mChar[39;49;00m): [36mBoolean[39;49;00m;
[34mvar[39;49;00m
  i: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [34mTrue[39;49;00m;
  [34mfor[39;49;00m i := [34m1[39;49;00m [34mto[39;49;00m [36mLength[39;49;00m(S) [34mdo[39;49;00m
    [34mif[39;49;00m S[i] = C [34mthen[39;49;00m [34mExit[39;49;00m;
  [36mResult[39;49;00m := [34mFalse[39;49;00m;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mCharIn[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; C: TCharSet): [36mBoolean[39;49;00m;
[34mvar[39;49;00m
  i: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [34mFalse[39;49;00m;
  [34mfor[39;49;00m i := [34m1[39;49;00m [34mto[39;49;00m [36mLength[39;49;00m(S) [34mdo[39;49;00m [34mbegin[39;49;00m
    [36mResult[39;49;00m := S[i] [34min[39;49;00m C;
    [34mif[39;49;00m [36mResult[39;49;00m [34mthen[39;49;00m
      [34mExit[39;49;00m;
  [34mend[39;49;00m;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mStrIn[39;49;00m([34mconst[39;49;00m S, SubStr: [34mstring[39;49;00m): [36mBoolean[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := PosEx(SubStr, S) > [34m0[39;49;00m;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mStrIn[39;49;00m(SL: TStrings; [34mconst[39;49;00m S: [34mstring[39;49;00m): [36mBoolean[39;49;00m;
[34mvar[39;49;00m
  i: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [34mFalse[39;49;00m;
  [34mfor[39;49;00m i := [34m0[39;49;00m [34mto[39;49;00m SL.Count-[34m1[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m
    [36mResult[39;49;00m := (S = SL[i]);
    [34mif[39;49;00m [36mResult[39;49;00m [34mthen[39;49;00m
      [34mExit[39;49;00m;
  [34mend[39;49;00m;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mStrIn[39;49;00m(A: TStrA; [34mconst[39;49;00m S: [34mstring[39;49;00m): [36mBoolean[39;49;00m;
[34mvar[39;49;00m
  i: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [34mFalse[39;49;00m;
  [34mfor[39;49;00m i := [36mLow[39;49;00m(A) [34mto[39;49;00m [36mHigh[39;49;00m(A) [34mdo[39;49;00m [34mbegin[39;49;00m
    [36mResult[39;49;00m := (S = A[i]);
    [34mif[39;49;00m [36mResult[39;49;00m [34mthen[39;49;00m
      [34mExit[39;49;00m;
  [34mend[39;49;00m;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mTextIn[39;49;00m([34mconst[39;49;00m S, Text: [34mstring[39;49;00m): [36mBoolean[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := PosExText(Text, S) > [34m0[39;49;00m;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mTextIn[39;49;00m(SL: TStrings; [34mconst[39;49;00m Text: [34mstring[39;49;00m): [36mBoolean[39;49;00m;
[34mvar[39;49;00m
  i: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [34mFalse[39;49;00m;
  [34mfor[39;49;00m i := [34m0[39;49;00m [34mto[39;49;00m SL.Count-[34m1[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m
    [36mResult[39;49;00m := [36mSameText[39;49;00m(Text, SL[i]);
    [34mif[39;49;00m [36mResult[39;49;00m [34mthen[39;49;00m
      [34mExit[39;49;00m;
  [34mend[39;49;00m;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mTextIn[39;49;00m(A: TStrA; [34mconst[39;49;00m Text: [34mstring[39;49;00m): [36mBoolean[39;49;00m;
[34mvar[39;49;00m
  i: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [34mFalse[39;49;00m;
  [34mfor[39;49;00m i := [36mLow[39;49;00m(A) [34mto[39;49;00m [36mHigh[39;49;00m(A) [34mdo[39;49;00m [34mbegin[39;49;00m
    [36mResult[39;49;00m := [36mSameText[39;49;00m(Text, A[i]);
    [34mif[39;49;00m [36mResult[39;49;00m [34mthen[39;49;00m
      [34mExit[39;49;00m;
  [34mend[39;49;00m;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mStrIndex[39;49;00m(SL: TStrings; [34mconst[39;49;00m S: [34mstring[39;49;00m): [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [34mfor[39;49;00m [36mResult[39;49;00m := [34m0[39;49;00m [34mto[39;49;00m SL.Count-[34m1[39;49;00m [34mdo[39;49;00m
    [34mif[39;49;00m S = SL[[36mResult[39;49;00m] [34mthen[39;49;00m
      [34mExit[39;49;00m;
  [36mResult[39;49;00m := -[34m1[39;49;00m;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mStrIndex[39;49;00m(A: TStrA; [34mconst[39;49;00m S: [34mstring[39;49;00m): [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [34mfor[39;49;00m [36mResult[39;49;00m := [36mLow[39;49;00m(A) [34mto[39;49;00m [36mHigh[39;49;00m(A) [34mdo[39;49;00m
    [34mif[39;49;00m S = A[[36mResult[39;49;00m] [34mthen[39;49;00m
      [34mExit[39;49;00m;
  [36mResult[39;49;00m := -[34m1[39;49;00m;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mTextIndex[39;49;00m(SL: TStrings; [34mconst[39;49;00m Text: [34mstring[39;49;00m): [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [34mfor[39;49;00m [36mResult[39;49;00m := [34m0[39;49;00m [34mto[39;49;00m SL.Count-[34m1[39;49;00m [34mdo[39;49;00m
    [34mif[39;49;00m [36mSameText[39;49;00m(Text, SL[[36mResult[39;49;00m]) [34mthen[39;49;00m
      [34mExit[39;49;00m;
  [36mResult[39;49;00m := -[34m1[39;49;00m;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mTextIndex[39;49;00m(A: TStrA; [34mconst[39;49;00m Text: [34mstring[39;49;00m): [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [34mfor[39;49;00m [36mResult[39;49;00m := [36mLow[39;49;00m(A) [34mto[39;49;00m [36mHigh[39;49;00m(A) [34mdo[39;49;00m
    [34mif[39;49;00m [36mSameText[39;49;00m(Text, A[[36mResult[39;49;00m]) [34mthen[39;49;00m
      [34mExit[39;49;00m;
  [36mResult[39;49;00m := -[34m1[39;49;00m;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mReplaceChars[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Old, [34mNew[39;49;00m: [36mChar[39;49;00m): [34mstring[39;49;00m;
[34mvar[39;49;00m
  i: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := S;
  [34mfor[39;49;00m i := [34m1[39;49;00m [34mto[39;49;00m [36mLength[39;49;00m([36mResult[39;49;00m) [34mdo[39;49;00m
    [34mif[39;49;00m [36mResult[39;49;00m[i] = Old [34mthen[39;49;00m
      [36mResult[39;49;00m[i] := [34mNew[39;49;00m;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mReplaceChars[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Old: TCharSet; [34mNew[39;49;00m: [36mChar[39;49;00m): [34mstring[39;49;00m;
[34mvar[39;49;00m
  i: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := S;
  [34mfor[39;49;00m i := [34m1[39;49;00m [34mto[39;49;00m [36mLength[39;49;00m([36mResult[39;49;00m) [34mdo[39;49;00m
    [34mif[39;49;00m [36mResult[39;49;00m[i] [34min[39;49;00m Old [34mthen[39;49;00m
      [36mResult[39;49;00m[i] := [34mNew[39;49;00m;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mReplace[39;49;00m([34mconst[39;49;00m S, Old, [34mNew[39;49;00m: [34mstring[39;49;00m): [34mstring[39;49;00m;
[34mvar[39;49;00m
  oldp, ps: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  ps := [34m1[39;49;00m;
  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;
  [34mwhile[39;49;00m [34mTrue[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m
    oldp := ps;
    ps := PosEx(Old, S, oldp);
    [34mif[39;49;00m ps = [34m0[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m
      [36mResult[39;49;00m := [36mResult[39;49;00m + [36mCopy[39;49;00m(S, oldp, [36mLength[39;49;00m(S) - oldp + [34m1[39;49;00m);
    [34mExit[39;49;00m; [34mend[39;49;00m;
    [36mResult[39;49;00m := [36mResult[39;49;00m + [36mCopy[39;49;00m(S, oldp, ps - oldp) + [34mNew[39;49;00m;
    [36mInc[39;49;00m(ps, [36mLength[39;49;00m(Old));
  [34mend[39;49;00m;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mSLOfFile[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m): TStringList;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := TStringList.Create;
  [34mif[39;49;00m [36mFileExists[39;49;00m(FileName) [34mthen[39;49;00m
    [36mResult[39;49;00m.LoadFromFile(FileName);
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mContainsEmptyLines[39;49;00m(SL: TStrings): [36mBoolean[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := StrIn(SL, [33m'[39;49;00m[33m'[39;49;00m);
[34mend[39;49;00m;

[34mprocedure[39;49;00m [32mDeleteEmptyLines[39;49;00m(SL: TStrings);
[34mvar[39;49;00m
  i: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  i := [34m0[39;49;00m;
  [34mwhile[39;49;00m i < SL.Count [34mdo[39;49;00m [34mbegin[39;49;00m
    [34mif[39;49;00m SL[i] = [33m'[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m
      SL.Delete(i)
    [34melse[39;49;00m
      [36mInc[39;49;00m(i);
  [34mend[39;49;00m;
[34mend[39;49;00m;

[34mprocedure[39;49;00m [32mDeleteCommentLines[39;49;00m(SL: TStrings; [34mconst[39;49;00m CommentSign: [34mstring[39;49;00m = [33m'[39;49;00m[33m//[39;49;00m[33m'[39;49;00m);
[34mvar[39;49;00m
  i: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  i := [34m0[39;49;00m;
  [34mwhile[39;49;00m i < SL.Count [34mdo[39;49;00m [34mbegin[39;49;00m
    [34mif[39;49;00m (SL[i] = [33m'[39;49;00m[33m'[39;49;00m) [34mor[39;49;00m (StrAtBegin([36mTrimLeft[39;49;00m(SL[i]), CommentSign)) [34mthen[39;49;00m
      SL.Delete(i)
    [34melse[39;49;00m
      [36mInc[39;49;00m(i);
  [34mend[39;49;00m;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mFindLine[39;49;00m(SL: TStrings; [34mconst[39;49;00m S: [34mstring[39;49;00m): [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [34mfor[39;49;00m [36mResult[39;49;00m := [34m0[39;49;00m [34mto[39;49;00m SL.Count-[34m1[39;49;00m [34mdo[39;49;00m
    [34mif[39;49;00m TextAtBegin(SL[[36mResult[39;49;00m], S) [34mthen[39;49;00m
      [34mExit[39;49;00m;
  [36mResult[39;49;00m := -[34m1[39;49;00m;
[34mend[39;49;00m;

[34mprocedure[39;49;00m [32mQuickSortSL[39;49;00m(SL: TStringList);

  [34mprocedure[39;49;00m [32mSort[39;49;00m(l, r: [36mInteger[39;49;00m);
  [34mvar[39;49;00m
    i,j: [36mInteger[39;49;00m;
    z,x: [34mstring[39;49;00m;
  [34mbegin[39;49;00m
    i := l;
    j := r;
    x := SL[(j + i) [34mdiv[39;49;00m [34m2[39;49;00m];
    [34mrepeat[39;49;00m
      [34mwhile[39;49;00m SL[i] < x [34mdo[39;49;00m [36mInc[39;49;00m(i);
      [34mwhile[39;49;00m SL[j] > x [34mdo[39;49;00m [36mDec[39;49;00m(j);
      [34mif[39;49;00m i <= j [34mthen[39;49;00m [34mbegin[39;49;00m
        z := SL[i];
        SL[i] := SL[j];
        SL[j] := z;
        [36mInc[39;49;00m(i); [36mDec[39;49;00m(j);
      [34mend[39;49;00m;
    [34muntil[39;49;00m i > j;
    [34mif[39;49;00m j > l [34mthen[39;49;00m Sort(l, j);
    [34mif[39;49;00m i < r [34mthen[39;49;00m Sort(i, r);
  [34mend[39;49;00m;

[34mbegin[39;49;00m
  [34mif[39;49;00m SL.Count > [34m0[39;49;00m [34mthen[39;49;00m
    Sort([34m0[39;49;00m, SL.Count-[34m1[39;49;00m);
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mIncStrA[39;49;00m(StrA: TStrA): [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [36mSetLength[39;49;00m(StrA, [36mLength[39;49;00m(StrA) + [34m1[39;49;00m);
  [36mResult[39;49;00m := [36mHigh[39;49;00m(StrA);
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mStrOfByteA[39;49;00m(a: TByteA): [34mstring[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [34mstring[39;49;00m([36mCopy[39;49;00m(a, [34m0[39;49;00m, [36mLength[39;49;00m(a)));
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mByteAOfStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): TByteA;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := TByteA([36mCopy[39;49;00m(S, [34m1[39;49;00m, [36mLength[39;49;00m(s)));
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mByteAOfInt[39;49;00m(i: [36mInteger[39;49;00m): TByteA;
[34mbegin[39;49;00m
  [36mSetLength[39;49;00m([36mResult[39;49;00m, [36mSizeOf[39;49;00m([36mInteger[39;49;00m));
  [36mMove[39;49;00m(i, [36mPointer[39;49;00m([36mResult[39;49;00m)^, [36mSizeOf[39;49;00m([36mInteger[39;49;00m));
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mIntOfByteA[39;49;00m(A: TByteA): [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [34m0[39;49;00m;
  [36mMove[39;49;00m([36mPointer[39;49;00m(A)^, [36mResult[39;49;00m, [36mMin[39;49;00m([36mLength[39;49;00m(A), [36mSizeOf[39;49;00m([36mInteger[39;49;00m)));
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mByteAOfHex[39;49;00m([34mconst[39;49;00m Hex: [34mstring[39;49;00m): TByteA;
[34mvar[39;49;00m
  i: [36mInteger[39;49;00m;
  h: [34mstring[39;49;00m;
[34mbegin[39;49;00m
  h := ExtractChars(Hex, HexadecimalChars);
  [36mSetLength[39;49;00m([36mResult[39;49;00m, [36mLength[39;49;00m(h) [34mdiv[39;49;00m [34m2[39;49;00m);
  [34mfor[39;49;00m i := [34m0[39;49;00m [34mto[39;49;00m [36mHigh[39;49;00m([36mResult[39;49;00m) [34mdo[39;49;00m
    [36mResult[39;49;00m[i] := ByteOfHex([36mCopy[39;49;00m(h, (i [34mshl[39;49;00m [34m1[39;49;00m) + [34m1[39;49;00m, [34m2[39;49;00m));
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mSizeOfFile[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m): [36mInteger[39;49;00m;
[34mvar[39;49;00m
  F: [34mfile[39;49;00m;
[34mbegin[39;49;00m
  [36mAssignFile[39;49;00m(F, FileName);
  [37m{$I-}[39;49;00m[36mReset[39;49;00m(F, [34m1[39;49;00m);[37m{$I+}[39;49;00m
  [34mif[39;49;00m [36mIOResult[39;49;00m = [34m0[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m
    [36mResult[39;49;00m := [36mFileSize[39;49;00m(F);
    [36mCloseFile[39;49;00m(F);
  [34mend[39;49;00m [34melse[39;49;00m
    [36mResult[39;49;00m := [34m0[39;49;00m;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mFileEx[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m; AllowFolders: [36mBoolean[39;49;00m = [34mFalse[39;49;00m): [36mBoolean[39;49;00m;
[34mvar[39;49;00m
  FindData: TWin32FindData;
[34mbegin[39;49;00m
  [34mif[39;49;00m FileName = [33m'[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m
    [36mResult[39;49;00m := [34mFalse[39;49;00m;
  [34mExit[39;49;00m; [34mend[39;49;00m;

  [36mResult[39;49;00m := (AllowFolders [34mand[39;49;00m [36mDirectoryExists[39;49;00m(FileName)) [34mor[39;49;00m
    (FindFirstFile([36mPChar[39;49;00m(FileName), FindData) <> INVALID_HANDLE_VALUE);
  [36mResult[39;49;00m := [36mResult[39;49;00m [34mand[39;49;00m [34mnot[39;49;00m CharIn(FileName, WildCards);
  [36mResult[39;49;00m := [36mResult[39;49;00m [34mand[39;49;00m (AllowFolders
    [34mor[39;49;00m ((FindData.dwFileAttributes [34mand[39;49;00m FILE_ATTRIBUTE_DIRECTORY) = [34m0[39;49;00m));
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mLWPSolve[39;49;00m([34mconst[39;49;00m Dir: [34mstring[39;49;00m): [34mstring[39;49;00m;
[34mbegin[39;49;00m
  [34mif[39;49;00m (Dir <> [33m'[39;49;00m[33m'[39;49;00m) [34mand[39;49;00m (Dir[[36mLength[39;49;00m(Dir)] = [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m) [34mthen[39;49;00m [34mbegin[39;49;00m
    [36mResult[39;49;00m := [36mCopy[39;49;00m(Dir, [34m1[39;49;00m, [36mLength[39;49;00m(Dir) - [34m1[39;49;00m);
  [34mend[39;49;00m [34melse[39;49;00m
    [36mResult[39;49;00m := Dir;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mLWPSlash[39;49;00m([34mconst[39;49;00m Dir: [34mstring[39;49;00m): [34mstring[39;49;00m;
[34mbegin[39;49;00m
  [34mif[39;49;00m (Dir <> [33m'[39;49;00m[33m'[39;49;00m) [34mand[39;49;00m (Dir[[36mLength[39;49;00m(Dir)] = [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m) [34mthen[39;49;00m [34mbegin[39;49;00m
    [36mResult[39;49;00m := [36mCopy[39;49;00m(Dir, [34m1[39;49;00m, [36mLength[39;49;00m(Dir));
  [34mend[39;49;00m [34melse[39;49;00m
    [36mResult[39;49;00m := Dir + [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mExtractDrive[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m): [34mstring[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;
  [34mif[39;49;00m ([36mLength[39;49;00m(FileName) >= [34m2[39;49;00m) [34mand[39;49;00m (FileName[[34m2[39;49;00m] = [33m'[39;49;00m[33m:[39;49;00m[33m'[39;49;00m) [34mthen[39;49;00m
    [36mResult[39;49;00m := [36mUpperCase[39;49;00m(FileName[[34m1[39;49;00m] + [33m'[39;49;00m[33m:\[39;49;00m[33m'[39;49;00m);
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mExtractPath[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m): [34mstring[39;49;00m;
[34mvar[39;49;00m
  p: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  p := CharPosR([33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m, FileName);
  [34mif[39;49;00m P > [34m0[39;49;00m [34mthen[39;49;00m
    [36mResult[39;49;00m := [36mCopy[39;49;00m(FileName, [34m1[39;49;00m, p)
  [34melse[39;49;00m
    [36mResult[39;49;00m := FileName;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mExtractPrefix[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m): [34mstring[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := UntilLastChar([36mExtractFileName[39;49;00m(FileName), [33m'[39;49;00m[33m.[39;49;00m[33m'[39;49;00m);
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mExtractSuffix[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m): [34mstring[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := FromLastChar([36mExtractFileName[39;49;00m(FileName), [33m'[39;49;00m[33m.[39;49;00m[33m'[39;49;00m);
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mSameByteA[39;49;00m([34mconst[39;49;00m A, B: TByteA): [36mBoolean[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := (A = B) [34mor[39;49;00m (([36mLength[39;49;00m(A) = [36mLength[39;49;00m(B)) [34mand[39;49;00m [36mCompareMem[39;49;00m(A, B, [36mLength[39;49;00m(A)));
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mReverse[39;49;00m(A: TByteA): TByteA;
[34mvar[39;49;00m
  i: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [36mSetLength[39;49;00m([36mResult[39;49;00m, [36mLength[39;49;00m(A));

  [34mfor[39;49;00m i := [34m0[39;49;00m [34mto[39;49;00m [36mHigh[39;49;00m(A) [34mdo[39;49;00m
    [36mResult[39;49;00m[[36mHigh[39;49;00m([36mResult[39;49;00m) - i] := A[i];
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mEndian[39;49;00m(i: [36mInteger[39;49;00m): [36mInteger[39;49;00m;
[34mtype[39;49;00m
  EndianArray = [34mpacked[39;49;00m [34marray[39;49;00m[[34m0[39;49;00m..[34m3[39;49;00m] [34mof[39;49;00m [36mByte[39;49;00m;
[34mvar[39;49;00m
  a, b: EndianArray;
[34mbegin[39;49;00m
  a := EndianArray(i);
  b[[34m0[39;49;00m] := a[[34m3[39;49;00m];
  b[[34m1[39;49;00m] := a[[34m2[39;49;00m];
  b[[34m2[39;49;00m] := a[[34m1[39;49;00m];
  b[[34m3[39;49;00m] := a[[34m0[39;49;00m];
  [36mResult[39;49;00m := [36mInteger[39;49;00m(b);
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mSaveByteA[39;49;00m(Data: TByteA; [34mconst[39;49;00m FileName: [34mstring[39;49;00m;
  Overwrite: [36mBoolean[39;49;00m = [34mTrue[39;49;00m): [36mBoolean[39;49;00m;
[34mvar[39;49;00m
  F: [34mfile[39;49;00m;
[34mbegin[39;49;00m
  [34mif[39;49;00m [36mFileExists[39;49;00m(FileName) [34mand[39;49;00m [34mnot[39;49;00m Overwrite [34mthen[39;49;00m [34mbegin[39;49;00m
    [36mResult[39;49;00m := [34mFalse[39;49;00m;
  [34mExit[39;49;00m [34mend[39;49;00m;

  [36mAssignFile[39;49;00m(F, FileName);
  [37m{$I-}[39;49;00m[36mRewrite[39;49;00m(F, [34m1[39;49;00m);[37m{$I+}[39;49;00m
  [34mif[39;49;00m [36mIOResult[39;49;00m = [34m0[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m
    [34mif[39;49;00m [36mLength[39;49;00m(Data) > [34m0[39;49;00m [34mthen[39;49;00m
      [36mBlockWrite[39;49;00m(F, Data[[34m0[39;49;00m], [36mLength[39;49;00m(Data));
    [36mCloseFile[39;49;00m(F);
    [36mResult[39;49;00m := [34mTrue[39;49;00m;
  [34mend[39;49;00m [34melse[39;49;00m
    [36mResult[39;49;00m := [34mFalse[39;49;00m;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mLoadByteA[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m): TByteA;
[34mvar[39;49;00m
  F: [34mfile[39;49;00m;
[34mbegin[39;49;00m
  [36mAssignFile[39;49;00m(F, FileName);
  [37m{$I-}[39;49;00m[36mReset[39;49;00m(F, [34m1[39;49;00m);[37m{$I+}[39;49;00m
  [34mif[39;49;00m [36mIOResult[39;49;00m = [34m0[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m
    [36mSetLength[39;49;00m([36mResult[39;49;00m, [36mFileSize[39;49;00m(F));
    [34mif[39;49;00m [36mLength[39;49;00m([36mResult[39;49;00m) > [34m0[39;49;00m [34mthen[39;49;00m
      [36mBlockRead[39;49;00m(F, [36mResult[39;49;00m[[34m0[39;49;00m], [36mFileSize[39;49;00m(F));
    [36mCloseFile[39;49;00m(F);
  [34mend[39;49;00m [34melse[39;49;00m
    [36mSetLength[39;49;00m([36mResult[39;49;00m, [34m0[39;49;00m);
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mIsValidFileName[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m): [36mBoolean[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := (FileName <> [33m'[39;49;00m[33m'[39;49;00m) [34mand[39;49;00m [34mnot[39;49;00m CharIn(FileName, FileNameEnemies)
    [34mand[39;49;00m CharIn([36mTrim[39;49;00m(FileName), AllChars - [[33m'[39;49;00m[33m.[39;49;00m[33m'[39;49;00m]);
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mMakeValidFileName[39;49;00m(FileName: [34mstring[39;49;00m; [34mconst[39;49;00m [34mDefault[39;49;00m: [34mstring[39;49;00m = [33m'[39;49;00m[33mFile[39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;
[34mbegin[39;49;00m
  [34mif[39;49;00m FileName = [33m'[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m
    FileName := [34mDefault[39;49;00m;

  [34mif[39;49;00m CharIn(FileName, FileNameEnemies) [34mthen[39;49;00m
    [36mResult[39;49;00m := ReplaceChars(FileName, FileNameEnemies, [33m'[39;49;00m[33m_[39;49;00m[33m'[39;49;00m)
  [34melse[39;49;00m [34mif[39;49;00m [34mnot[39;49;00m CharIn([36mTrim[39;49;00m(FileName), AllChars - [[33m'[39;49;00m[33m.[39;49;00m[33m'[39;49;00m]) [34mthen[39;49;00m
    [36mResult[39;49;00m := [34mDefault[39;49;00m
  [34melse[39;49;00m
    [36mResult[39;49;00m := FileName;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mIsValidInteger[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [36mBoolean[39;49;00m;
[37m{const[39;49;00m
[37m  LowInt = '2147483648';[39;49;00m
[37m  HighInt = '2147483647';[39;49;00m
[37mvar[39;49;00m
[37m  len, RealLen, i, o: Integer;[39;49;00m
[37m  c: Char;[39;49;00m
[37mbegin[39;49;00m
[37m  Result := False;[39;49;00m
[37m  if S = '' then[39;49;00m
[37m    Exit;[39;49;00m
[37m[39;49;00m
[37m  len := Length(S);[39;49;00m
[37m  o := 1;[39;49;00m
[37m  [39;49;00m
[37m  if S[1] = '-' then begin[39;49;00m
[37m    if len = 1 then[39;49;00m
[37m      Exit;[39;49;00m
[37m    Inc(o);[39;49;00m
[37m    while (o <= len) and (S[o] = '0') do[39;49;00m
[37m      Inc(o);[39;49;00m
[37m    if o > len then[39;49;00m
[37m      Exit;[39;49;00m
[37m    if o < len then begin[39;49;00m
[37m      RealLen := len - o + 1;[39;49;00m
[37m      if RealLen > Length(LowInt) then[39;49;00m
[37m        Exit[39;49;00m
[37m      else if RealLen = Length(LowInt) then begin[39;49;00m
[37m        for i := 1 to Length(LowInt) do begin[39;49;00m
[37m          c := S[i + o - 1];[39;49;00m
[37m          if (c < '0') or (c > LowInt[i]) then[39;49;00m
[37m            Exit;[39;49;00m
[37m          if c in ['0'..Char((Byte(LowInt[i])-1))] then[39;49;00m
[37m            Break;[39;49;00m
[37m        end;[39;49;00m
[37m        Inc(o, i);[39;49;00m
[37m      end;[39;49;00m
[37m    end;[39;49;00m
[37m  end else begin[39;49;00m
[37m    while (o <= len) and (S[o] = '0') do[39;49;00m
[37m      Inc(o);[39;49;00m
[37m    if o <= len then begin[39;49;00m
[37m      RealLen := len - o + 1;[39;49;00m
[37m      if RealLen > Length(HighInt) then[39;49;00m
[37m        Exit[39;49;00m
[37m      else if RealLen = Length(HighInt) then begin[39;49;00m
[37m        for i := 1 to Length(HighInt) do begin[39;49;00m
[37m          c := S[i + o - 1];[39;49;00m
[37m          if (c < '0') or (c > HighInt[i]) then[39;49;00m
[37m            Exit;[39;49;00m
[37m          if c in ['0'..Char((Byte(HighInt[i])-1))] then[39;49;00m
[37m            Break;[39;49;00m
[37m        end;[39;49;00m
[37m        Inc(o, i);[39;49;00m
[37m      end;[39;49;00m
[37m    end;[39;49;00m
[37m  end;[39;49;00m
[37m[39;49;00m
[37m  for i := o to len do[39;49;00m
[37m    if not (S[i] in ['0'..'9']) then[39;49;00m
[37m      Exit;[39;49;00m
[37m[39;49;00m
[37m  Result := True;  }[39;49;00m
[34mvar[39;49;00m
  i: [36mInt64[39;49;00m;
[34mbegin[39;49;00m
  i := [36mStrToInt64Def[39;49;00m(S, [36mHigh[39;49;00m([36mInt64[39;49;00m));
  [36mResult[39;49;00m := (i >= [36mLow[39;49;00m([36mInteger[39;49;00m)) [34mand[39;49;00m (i <= [36mHigh[39;49;00m([36mInteger[39;49;00m));
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mIsValidCardinal[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [36mBoolean[39;49;00m;
[37m{const[39;49;00m
[37m  HighCard = '4294967295';[39;49;00m
[37mvar[39;49;00m
[37m  len, RealLen, i, o: Integer;[39;49;00m
[37mbegin[39;49;00m
[37m  Result := False;[39;49;00m
[37m  if S = '' then[39;49;00m
[37m    Exit;[39;49;00m
[37m[39;49;00m
[37m  len := Length(S);[39;49;00m
[37m  o := 1;[39;49;00m
[37m  [39;49;00m
[37m  while (o <= len) and (S[o] = '0') do[39;49;00m
[37m    Inc(o);[39;49;00m
[37m  if o <= len then begin[39;49;00m
[37m    RealLen := len - o + 1;[39;49;00m
[37m    if RealLen > Length(HighCard) then[39;49;00m
[37m      Exit[39;49;00m
[37m    else if RealLen = Length(HighCard) then begin[39;49;00m
[37m      for i := 1 to Length(HighCard) do begin[39;49;00m
[37m        if S[i + o - 1] > HighCard[i] then[39;49;00m
[37m          Exit;[39;49;00m
[37m        if S[i + o - 1] in ['0'..Char((Byte(HighCard[i])-1))] then[39;49;00m
[37m          Break;[39;49;00m
[37m      end;[39;49;00m
[37m      Inc(o, i);[39;49;00m
[37m    end;[39;49;00m
[37m  end;[39;49;00m
[37m[39;49;00m
[37m  for i := o to len do[39;49;00m
[37m    if not (S[i] in ['0'..'9']) then[39;49;00m
[37m      Exit;[39;49;00m
[37m[39;49;00m
[37m  Result := True;  }[39;49;00m
[34mvar[39;49;00m
  i: [36mInt64[39;49;00m;
[34mbegin[39;49;00m
  i := [36mStrToInt64Def[39;49;00m(S, -[34m1[39;49;00m);
  [36mResult[39;49;00m := (i >= [34m0[39;49;00m) [34mand[39;49;00m (i <= [36mHigh[39;49;00m([36mCardinal[39;49;00m));
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mStrOfBool[39;49;00m(flag: [36mBoolean[39;49;00m; [34mconst[39;49;00m TrueStr: [34mstring[39;49;00m = [33m'[39;49;00m[33mTrue[39;49;00m[33m'[39;49;00m;
  [34mconst[39;49;00m FalseStr: [34mstring[39;49;00m = [33m'[39;49;00m[33mFalse[39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;
[34mbegin[39;49;00m
  [34mif[39;49;00m Flag [34mthen[39;49;00m
    [36mResult[39;49;00m := TrueStr
  [34melse[39;49;00m
    [36mResult[39;49;00m := FalseStr;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mStrOfInt[39;49;00m(i: [36mInteger[39;49;00m): [34mstring[39;49;00m;
[34mbegin[39;49;00m
[37m{  if i = 0 then begin[39;49;00m
[37m    Result := '0';[39;49;00m
[37m  Exit end;[39;49;00m
[37m[39;49;00m
[37m  while i > 0 do begin[39;49;00m
[37m    Result := Char(Byte('0') + (i mod 10)) + Result;[39;49;00m
[37m    i := i div 10;[39;49;00m
[37m  end;}[39;49;00m
  [36mResult[39;49;00m := [36mIntToStr[39;49;00m(i);
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mCardOfStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [36mCardinal[39;49;00m;
[34mvar[39;49;00m
  Res: [36mInt64[39;49;00m;
[34mbegin[39;49;00m
  Res := [36mStrToInt64Def[39;49;00m(S, -[34m1[39;49;00m);
  [34mif[39;49;00m Res > [36mHigh[39;49;00m([36mCardinal[39;49;00m) [34mthen[39;49;00m
    Res := [36mHigh[39;49;00m([36mCardinal[39;49;00m)
  [34melse[39;49;00m [34mif[39;49;00m Res < [34m0[39;49;00m [34mthen[39;49;00m
    Res := [34m0[39;49;00m;
  [36mResult[39;49;00m := [36mCardinal[39;49;00m(Res);
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mHexOrd[39;49;00m(Hex: [36mChar[39;49;00m): THex;
[34mbegin[39;49;00m
  [34mcase[39;49;00m Hex [34mof[39;49;00m
    [33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m..[33m'[39;49;00m[33m9[39;49;00m[33m'[39;49;00m:
      [36mResult[39;49;00m := [36mByte[39;49;00m(Hex) - [34m48[39;49;00m;
    [33m'[39;49;00m[33mA[39;49;00m[33m'[39;49;00m..[33m'[39;49;00m[33mF[39;49;00m[33m'[39;49;00m:
      [36mResult[39;49;00m := [36mByte[39;49;00m(Hex) - [34m55[39;49;00m;
    [33m'[39;49;00m[33ma[39;49;00m[33m'[39;49;00m..[33m'[39;49;00m[33mf[39;49;00m[33m'[39;49;00m:
      [36mResult[39;49;00m := [36mByte[39;49;00m(Hex) - [34m87[39;49;00m;
    [34melse[39;49;00m
      [36mResult[39;49;00m := [34m0[39;49;00m;
  [34mend[39;49;00m;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mByteOfHex[39;49;00m(Hex: THexByteStr): [36mByte[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := (HexOrd(Hex[[34m1[39;49;00m]) [34mshl[39;49;00m [34m4[39;49;00m) + HexOrd(Hex[[34m2[39;49;00m]);
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mDecOfHex[39;49;00m([34mconst[39;49;00m Hex: [34mstring[39;49;00m): [34mstring[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [36mIntToStr[39;49;00m(CardOfHex(Hex));
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mHexOfByte[39;49;00m(b: [36mByte[39;49;00m): THexByteStr;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := HexChar[(b [34mand[39;49;00m [34m$F0[39;49;00m) [34mshr[39;49;00m [34m4[39;49;00m]
          + HexChar[ b [34mand[39;49;00m [34m$0F[39;49;00m       ];
[34mend[39;49;00m;

[37m{function HexOfCard2(c: Cardinal): string;[39;49;00m
[37mvar[39;49;00m
[37m  Data: array[0..(1 shl 4) - 1] of Char;[39;49;00m
[37m  i: Integer;[39;49;00m
[37mbegin[39;49;00m
[37m  for i := 0 to (1 shl 4) - 1 do[39;49;00m
[37m    if i < 10 then[39;49;00m
[37m      Data[i] := Char(Ord('0') + i)[39;49;00m
[37m    else[39;49;00m
[37m      Data[i] := Char(Ord('A') + i - 10);[39;49;00m
[37m[39;49;00m
[37m  Result := Data[(c and (((1 shl (1 shl 2)) - 1) shl (7 shl 2))) shr (7 shl 2)][39;49;00m
[37m          + Data[(c and (((1 shl (1 shl 2)) - 1) shl (6 shl 2))) shr (6 shl 2)][39;49;00m
[37m          + Data[(c and (((1 shl (1 shl 2)) - 1) shl (5 shl 2))) shr (5 shl 2)][39;49;00m
[37m          + Data[(c and (((1 shl (1 shl 2)) - 1) shl (4 shl 2))) shr (4 shl 2)][39;49;00m
[37m          + Data[(c and (((1 shl (1 shl 2)) - 1) shl (3 shl 2))) shr (3 shl 2)][39;49;00m
[37m          + Data[(c and (((1 shl (1 shl 2)) - 1) shl (2 shl 2))) shr (2 shl 2)][39;49;00m
[37m          + Data[(c and (((1 shl (1 shl 2)) - 1) shl (1 shl 2))) shr (1 shl 2)][39;49;00m
[37m          + Data[(c and (((1 shl (1 shl 2)) - 1) shl (0 shl 2))) shr (0 shl 2)];[39;49;00m
[37mend; }[39;49;00m

[34mfunction[39;49;00m [32mHexOfCard[39;49;00m(i: [36mCardinal[39;49;00m): [34mstring[39;49;00m;
[34mvar[39;49;00m
  a: [36mCardinal[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;
  [34mwhile[39;49;00m i > [34m0[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m
    a := i [34mand[39;49;00m [34m$F[39;49;00m;
    [36mResult[39;49;00m := HexChar[a] + [36mResult[39;49;00m;
    i := i [34mshr[39;49;00m [34m4[39;49;00m;
  [34mend[39;49;00m;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mHexOfCard[39;49;00m(i: [36mCardinal[39;49;00m; Digits: [36mInteger[39;49;00m): [34mstring[39;49;00m;
[34mvar[39;49;00m
  a: [36mCardinal[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;
  [34mwhile[39;49;00m i > [34m0[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m
    a := i [34mand[39;49;00m [34m$F[39;49;00m;
    [36mResult[39;49;00m := HexChar[a] + [36mResult[39;49;00m;
    i := i [34mshr[39;49;00m [34m4[39;49;00m;
  [34mend[39;49;00m;
  [36mResult[39;49;00m := MulStr([33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m, Digits - [36mLength[39;49;00m([36mResult[39;49;00m)) + [36mResult[39;49;00m;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mPascalHexArray[39;49;00m(a: TByteA; [34mName[39;49;00m: [34mstring[39;49;00m): [34mstring[39;49;00m;
[34mvar[39;49;00m
  i, len: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [33m'[39;49;00m[33mconst[39;49;00m[33m'[39;49;00m + EOL +
    [33m'[39;49;00m[33m  [39;49;00m[33m'[39;49;00m + Name + [33m'[39;49;00m[33m: array[0..[39;49;00m[33m'[39;49;00m + [36mIntToStr[39;49;00m([36mHigh[39;49;00m(a)) + [33m'[39;49;00m[33m] of Byte = ([39;49;00m[33m'[39;49;00m;

  len := [36mLength[39;49;00m(a);
  [34mfor[39;49;00m i := [34m0[39;49;00m [34mto[39;49;00m len-[34m1[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m
    [34mif[39;49;00m (i [34mmod[39;49;00m [34m19[39;49;00m) = [34m0[39;49;00m [34mthen[39;49;00m
      [36mResult[39;49;00m := [36mResult[39;49;00m + EOL + [33m'[39;49;00m[33m  [39;49;00m[33m'[39;49;00m + [33m'[39;49;00m[33m  [39;49;00m[33m'[39;49;00m;
    [36mResult[39;49;00m := [36mResult[39;49;00m + [33m'[39;49;00m[33m$[39;49;00m[33m'[39;49;00m + HexOfByte(a[i]);
    [34mif[39;49;00m i < len-[34m1[39;49;00m [34mthen[39;49;00m
      [36mResult[39;49;00m := [36mResult[39;49;00m + [33m'[39;49;00m[33m,[39;49;00m[33m'[39;49;00m;
  [34mend[39;49;00m;
  [36mResult[39;49;00m := [36mResult[39;49;00m + EOL + [33m'[39;49;00m[33m  );[39;49;00m[33m'[39;49;00m;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mHexOfByteA[39;49;00m(a: TByteA; Blocks: [36mInteger[39;49;00m = [34m1[39;49;00m;
  [34mconst[39;49;00m Splitter: [34mstring[39;49;00m = [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;
[34mvar[39;49;00m
  i: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;

  [34mif[39;49;00m Blocks > [34m0[39;49;00m [34mthen[39;49;00m
    [34mfor[39;49;00m i := [34m0[39;49;00m [34mto[39;49;00m [36mHigh[39;49;00m(a) [34mdo[39;49;00m [34mbegin[39;49;00m
      [36mResult[39;49;00m := [36mResult[39;49;00m + HexOfByte(a[i]);
      [34mif[39;49;00m i < [36mHigh[39;49;00m(a) [34mthen[39;49;00m
        [34mif[39;49;00m ((i+[34m1[39;49;00m) [34mmod[39;49;00m Blocks) = [34m0[39;49;00m [34mthen[39;49;00m
          [36mResult[39;49;00m := [36mResult[39;49;00m + Splitter;
    [34mend[39;49;00m
  [34melse[39;49;00m
    [34mfor[39;49;00m i := [34m0[39;49;00m [34mto[39;49;00m [36mHigh[39;49;00m(a) [34mdo[39;49;00m
      [36mResult[39;49;00m := [36mResult[39;49;00m + HexOfByte(a[i]);
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mBinOfByteA[39;49;00m(a: TByteA; Blocks: [36mInteger[39;49;00m = [34m4[39;49;00m;
  [34mconst[39;49;00m Splitter: [34mstring[39;49;00m = [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;
[34mvar[39;49;00m
  i, [36mmax[39;49;00m: [36mInteger[39;49;00m;
  Bit: [36mBoolean[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;

  [34mif[39;49;00m Blocks > [34m0[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m
    [36mmax[39;49;00m := [34m8[39;49;00m * ([36mHigh[39;49;00m(a)) + [34m7[39;49;00m;
    [34mfor[39;49;00m i := [34m0[39;49;00m [34mto[39;49;00m [36mmax[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m
      Bit := [34m7[39;49;00m-(i [34mmod[39;49;00m [34m8[39;49;00m) [34min[39;49;00m TBitSet(a[i [34mdiv[39;49;00m [34m8[39;49;00m]);
      [36mResult[39;49;00m := [36mResult[39;49;00m + [36mChar[39;49;00m([36mByte[39;49;00m([33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m) + [36mByte[39;49;00m(Bit));
      [34mif[39;49;00m i < [36mmax[39;49;00m [34mthen[39;49;00m
        [34mif[39;49;00m ((i+[34m1[39;49;00m) [34mmod[39;49;00m Blocks) = [34m0[39;49;00m [34mthen[39;49;00m
          [36mResult[39;49;00m := [36mResult[39;49;00m + Splitter;
    [34mend[39;49;00m;
  [34mend[39;49;00m [34melse[39;49;00m
    [34mfor[39;49;00m i := [34m0[39;49;00m [34mto[39;49;00m [36mHigh[39;49;00m(a) [34mdo[39;49;00m
      [36mResult[39;49;00m := [36mResult[39;49;00m + [36mChar[39;49;00m([36mByte[39;49;00m([33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m) + a[i] [34mshr[39;49;00m (i [34mand[39;49;00m [34m8[39;49;00m));
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mCardOfHex[39;49;00m(Hex: [34mstring[39;49;00m): [36mCardinal[39;49;00m;
[34mvar[39;49;00m
  i: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [34m0[39;49;00m;
  Hex := [36mCopy[39;49;00m(ExtractChars(Hex, HexadecimalChars), [34m1[39;49;00m, [34m8[39;49;00m);

  [34mfor[39;49;00m i := [34m1[39;49;00m [34mto[39;49;00m [36mLength[39;49;00m(Hex) [34mdo[39;49;00m
    [34mif[39;49;00m Hex[i] <> [33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m
      [36mInc[39;49;00m([36mResult[39;49;00m, HexOrd(Hex[i]) [34mshl[39;49;00m (([36mLength[39;49;00m(Hex) - i) [34mshl[39;49;00m [34m2[39;49;00m));
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mIntOfBin[39;49;00m(Bin: [34mstring[39;49;00m): [36mCardinal[39;49;00m;
[34mvar[39;49;00m
  i: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [34m0[39;49;00m;
  Bin := [36mCopy[39;49;00m(ExtractChars(Bin, BinaryChars), [34m1[39;49;00m, [34m32[39;49;00m);

  [34mfor[39;49;00m i := [36mLength[39;49;00m(Bin) [34mdownto[39;49;00m [34m1[39;49;00m [34mdo[39;49;00m
    [34mif[39;49;00m Bin[i] = [33m'[39;49;00m[33m1[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m
      [36mInc[39;49;00m([36mResult[39;49;00m, [34m1[39;49;00m [34mshl[39;49;00m ([36mLength[39;49;00m(Bin) - i));
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mBinOfInt[39;49;00m(n: [36mCardinal[39;49;00m): [34mstring[39;49;00m;
[34mvar[39;49;00m
  a: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [34mif[39;49;00m n = [34m0[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m
    [36mResult[39;49;00m := [33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m;
  [34mexit[39;49;00m; [34mend[39;49;00m;

  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;
  [34mwhile[39;49;00m n > [34m0[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m
    a := n [34mand[39;49;00m [34m1[39;49;00m;
    [36mResult[39;49;00m := [36mChar[39;49;00m(a + [36mByte[39;49;00m([33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m)) + [36mResult[39;49;00m;
    n := n [34mshr[39;49;00m [34m1[39;49;00m;
  [34mend[39;49;00m;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mBinOfIntFill[39;49;00m(n: [36mCardinal[39;49;00m; MinCount: [36mInteger[39;49;00m = [34m8[39;49;00m): [34mstring[39;49;00m;
[34mvar[39;49;00m
  a: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [34mif[39;49;00m n = [34m0[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m
    [36mResult[39;49;00m := MulStr([33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m, MinCount);
  [34mExit[39;49;00m; [34mend[39;49;00m;

  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;
  [34mwhile[39;49;00m n > [34m0[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m
    a := n [34mand[39;49;00m [34m1[39;49;00m;
    [36mResult[39;49;00m := [36mChar[39;49;00m(a + [36mByte[39;49;00m([33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m)) + [36mResult[39;49;00m;
    n := n [34mshr[39;49;00m [34m1[39;49;00m;
  [34mend[39;49;00m;
  [36mResult[39;49;00m := MulStr([33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m, MinCount - [36mLength[39;49;00m([36mResult[39;49;00m)) + [36mResult[39;49;00m;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mBaseNOfInt[39;49;00m(I: [36mCardinal[39;49;00m; B: TBaseN): [34mstring[39;49;00m;
[34mvar[39;49;00m
  a: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [34mif[39;49;00m (B < [34m2[39;49;00m) [34mor[39;49;00m (i = [34m0[39;49;00m) [34mthen[39;49;00m [34mbegin[39;49;00m
    [36mResult[39;49;00m := [33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m;
  [34mExit[39;49;00m; [34mend[39;49;00m;

  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;
  [34mwhile[39;49;00m i > [34m0[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m
    a := i [34mmod[39;49;00m B;
    [36mResult[39;49;00m := BaseNChar[a] + [36mResult[39;49;00m;
    i := i [34mdiv[39;49;00m B;
  [34mend[39;49;00m;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mIntOfBaseN[39;49;00m(V: [34mstring[39;49;00m; B: TBaseN): [36mCardinal[39;49;00m;
[34mvar[39;49;00m
  i: [36mInteger[39;49;00m;
  F: [36mCardinal[39;49;00m;
  c: [36mByte[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [34m0[39;49;00m;
  V := TrimAll(V);
  F := [34m1[39;49;00m;
  [34mfor[39;49;00m i := [36mLength[39;49;00m(V) [34mdownto[39;49;00m [34m1[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m
    c := [36mByte[39;49;00m([36mUpCase[39;49;00m(V[i]));
    [34mcase[39;49;00m [36mChar[39;49;00m(c) [34mof[39;49;00m
      [33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m..[33m'[39;49;00m[33m9[39;49;00m[33m'[39;49;00m: c := c - [34m48[39;49;00m;
      [33m'[39;49;00m[33mA[39;49;00m[33m'[39;49;00m..[33m'[39;49;00m[33mZ[39;49;00m[33m'[39;49;00m: c := c - [34m55[39;49;00m;
    [34mend[39;49;00m;
    [34mif[39;49;00m c < B [34mthen[39;49;00m
      [36mResult[39;49;00m := [36mResult[39;49;00m + [36mByte[39;49;00m(c) * F;
    F := F * B;
  [34mend[39;49;00m;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mKeepIn[39;49;00m(i, Bottom, Top: [36mVariant[39;49;00m): [36mVariant[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := i;
  [34mif[39;49;00m [36mResult[39;49;00m > Top [34mthen[39;49;00m
    [36mResult[39;49;00m := Top
  [34melse[39;49;00m [34mif[39;49;00m [36mResult[39;49;00m < Bottom [34mthen[39;49;00m
    [36mResult[39;49;00m := Bottom;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mInRange[39;49;00m(Value, Bottom, Top: [36mVariant[39;49;00m): [36mBoolean[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := (Value >= Bottom) [34mand[39;49;00m (Value <= Top);
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mInStrictRange[39;49;00m(Value, Bottom, Top: [36mVariant[39;49;00m): [36mBoolean[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := (Value > Bottom) [34mand[39;49;00m (Value < Top);
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mMin[39;49;00m([34mconst[39;49;00m A, B: [36mInteger[39;49;00m): [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [34mif[39;49;00m A < B [34mthen[39;49;00m
    [36mResult[39;49;00m := A
  [34melse[39;49;00m
    [36mResult[39;49;00m := B;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mMin[39;49;00m([34mconst[39;49;00m A: TIntA): [36mInteger[39;49;00m;
[34mvar[39;49;00m
  i: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [34m0[39;49;00m;
  [34mif[39;49;00m [36mLength[39;49;00m(A) = [34m0[39;49;00m [34mthen[39;49;00m
    [34mExit[39;49;00m;

  [36mResult[39;49;00m := A[[34m0[39;49;00m];
  [34mfor[39;49;00m i := [34m1[39;49;00m [34mto[39;49;00m [36mHigh[39;49;00m(A) [34mdo[39;49;00m
    [34mif[39;49;00m A[i] < [36mResult[39;49;00m [34mthen[39;49;00m
      [36mResult[39;49;00m := A[i];
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mMax[39;49;00m([34mconst[39;49;00m A, B: [36mInteger[39;49;00m): [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [34mif[39;49;00m A > B [34mthen[39;49;00m
    [36mResult[39;49;00m := A
  [34melse[39;49;00m
    [36mResult[39;49;00m := B;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mMax[39;49;00m([34mconst[39;49;00m A: TIntA): [36mInteger[39;49;00m;
[34mvar[39;49;00m
  i: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [34m0[39;49;00m;
  [34mif[39;49;00m [36mLength[39;49;00m(A) = [34m0[39;49;00m [34mthen[39;49;00m
    [34mExit[39;49;00m;

  [36mResult[39;49;00m := A[[34m0[39;49;00m];
  [34mfor[39;49;00m i := [34m1[39;49;00m [34mto[39;49;00m [36mHigh[39;49;00m(A) [34mdo[39;49;00m
    [34mif[39;49;00m A[i] > [36mResult[39;49;00m [34mthen[39;49;00m
      [36mResult[39;49;00m := A[i];
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mRangesOfStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): TRanges;
[34mvar[39;49;00m
  SL: TStringList;
  r, b, t: [34mstring[39;49;00m;
  i, p: [36mInteger[39;49;00m;

  [34mfunction[39;49;00m [32mTryStrToCard[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; out Value: [36mCardinal[39;49;00m): [36mBoolean[39;49;00m;
  [34mvar[39;49;00m
    E: [36mInteger[39;49;00m;
  [34mbegin[39;49;00m
    [36mVal[39;49;00m(S, Value, E);
    [36mResult[39;49;00m := E = [34m0[39;49;00m;
  [34mend[39;49;00m;

[34mbegin[39;49;00m
  [36mResult[39;49;00m := [34mnil[39;49;00m;
  SL := TStringList.Create;
  [34mtry[39;49;00m
    Split(S, RangesSeparator, SL);
    [36mSetLength[39;49;00m([36mResult[39;49;00m, SL.Count);
    [34mfor[39;49;00m i := [34m0[39;49;00m [34mto[39;49;00m SL.Count-[34m1[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m
      r := SL[i];
      [34mwith[39;49;00m [36mResult[39;49;00m[i] [34mdo[39;49;00m [34mbegin[39;49;00m
        p := CharPos(RangeInnerSeparator, r);
        Simple := p = [34m0[39;49;00m; [37m// no '-' found[39;49;00m
        [34mif[39;49;00m Simple [34mthen[39;49;00m [34mbegin[39;49;00m
          [34mif[39;49;00m r = RangeInfinite [34mthen[39;49;00m [34mbegin[39;49;00m [37m// * --> *-*[39;49;00m
            Simple := [34mFalse[39;49;00m;
            Bottom := [36mLow[39;49;00m(Bottom);
            Top := [36mHigh[39;49;00m(Top);
          [34mend[39;49;00m [34melse[39;49;00m [34mif[39;49;00m [34mnot[39;49;00m TryStrToCard(r, Value) [34mthen[39;49;00m
            [34mBreak[39;49;00m;

        [34mend[39;49;00m [34melse[39;49;00m [34mbegin[39;49;00m
          TileStr(r, p, p, b, t);

          [34mif[39;49;00m b = RangeInfinite [34mthen[39;49;00m
            Bottom := [36mLow[39;49;00m(Bottom)
          [34melse[39;49;00m [34mif[39;49;00m [34mnot[39;49;00m TryStrToCard(b, Bottom) [34mthen[39;49;00m
            [34mBreak[39;49;00m;

          [34mif[39;49;00m t = RangeInfinite [34mthen[39;49;00m
            Top := [36mHigh[39;49;00m(Top)
          [34melse[39;49;00m [34mif[39;49;00m [34mnot[39;49;00m TryStrToCard(t, Top) [34mthen[39;49;00m
            [34mBreak[39;49;00m;
          [34mif[39;49;00m Bottom > Top [34mthen[39;49;00m [34mbegin[39;49;00m
            p := Bottom; Bottom := Top; Top := p;
          [34mend[39;49;00m;
        [34mend[39;49;00m;
      [34mend[39;49;00m;
    [34mend[39;49;00m;

    [34mif[39;49;00m i <> SL.Count [34mthen[39;49;00m
      [36mResult[39;49;00m := [34mnil[39;49;00m;

  [34mfinally[39;49;00m
    SL.Free;
  [34mend[39;49;00m;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mInRanges[39;49;00m(Ranges: TRanges; TestValue: [36mCardinal[39;49;00m): [36mBoolean[39;49;00m;
[34mvar[39;49;00m
  i: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [34mTrue[39;49;00m;

  [34mfor[39;49;00m i := [34m0[39;49;00m [34mto[39;49;00m [36mHigh[39;49;00m(Ranges) [34mdo[39;49;00m
    [34mwith[39;49;00m Ranges[i] [34mdo[39;49;00m
      [34mif[39;49;00m Simple [34mthen[39;49;00m [34mbegin[39;49;00m
        [34mif[39;49;00m TestValue = Value [34mthen[39;49;00m
          [34mExit[39;49;00m;
      [34mend[39;49;00m [34melse[39;49;00m [34mbegin[39;49;00m
        [34mif[39;49;00m [36mInRange[39;49;00m(TestValue, Bottom, Top) [34mthen[39;49;00m
          [34mExit[39;49;00m;
      [34mend[39;49;00m;

  [36mResult[39;49;00m := [34mFalse[39;49;00m;
[34mend[39;49;00m;

[34mprocedure[39;49;00m [32mWriteSL[39;49;00m(Strings: TStrings; [34mconst[39;49;00m Prefix: [34mstring[39;49;00m = [33m'[39;49;00m[33m'[39;49;00m;
  [34mconst[39;49;00m Suffix: [34mstring[39;49;00m = [33m'[39;49;00m[33m'[39;49;00m);
[34mvar[39;49;00m
  i: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [34mfor[39;49;00m i := [34m0[39;49;00m [34mto[39;49;00m Strings.Count-[34m1[39;49;00m [34mdo[39;49;00m
    [36mWriteLn[39;49;00m(Prefix + Strings[i] + Suffix);
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mSuccess[39;49;00m(Res: [36mInteger[39;49;00m; ResultOnSuccess: [36mInteger[39;49;00m = ERROR_SUCCESS): [36mBoolean[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := (Res = ResultOnSuccess);
  LastSuccessRes := Res;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mFailure[39;49;00m(Res: [36mInteger[39;49;00m; ResultOnSuccess: [36mInteger[39;49;00m = ERROR_SUCCESS): [36mBoolean[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [34mnot[39;49;00m Success(Res, ResultOnSuccess);
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mExpandString[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [34mstring[39;49;00m;
[34mvar[39;49;00m
  Len: [36mInteger[39;49;00m;
  P, Res: [36mPChar[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;
  P := [36mPChar[39;49;00m(S);
  Len := ExpandEnvironmentStrings(P, [34mnil[39;49;00m, [34m0[39;49;00m);
  [34mif[39;49;00m Len = [34m0[39;49;00m [34mthen[39;49;00m
    [34mExit[39;49;00m;

  [36mGetMem[39;49;00m(Res, Len);
  ExpandEnvironmentStrings(P, Res, Len);

  [36mResult[39;49;00m := Res;
  [36mFreeMem[39;49;00m(Res, Len);
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mFindAll[39;49;00m(Strings: TStrings; [34mconst[39;49;00m Mask: [34mstring[39;49;00m;
  ScanSubDirs: [36mBoolean[39;49;00m = [34mTrue[39;49;00m; Attributes: [36mInteger[39;49;00m = faFindEveryFile;
  FileReturn: TFileNameFunc = [34mnil[39;49;00m): [36mBoolean[39;49;00m;
[34mvar[39;49;00m
  Path, FileName: [34mstring[39;49;00m;

  [34mprocedure[39;49;00m [32mScanDir[39;49;00m([34mconst[39;49;00m Path, FileName: [34mstring[39;49;00m);
  [34mvar[39;49;00m
    PSR: TSearchRec;
    Res: [36mInteger[39;49;00m;

    [34mprocedure[39;49;00m [32mAdd[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m);
    [34mbegin[39;49;00m
      [34mif[39;49;00m S <> [33m'[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m
        Strings.Add(S);
    [34mend[39;49;00m;

  [34mbegin[39;49;00m
    Res := [36mFindFirst[39;49;00m(Path + FileName, Attributes, PSR);
    [34mwhile[39;49;00m Success(Res, [34m0[39;49;00m) [34mdo[39;49;00m [34mbegin[39;49;00m
      [34mif[39;49;00m [36mAssigned[39;49;00m(FileReturn) [34mthen[39;49;00m
        Add(FileReturn(Path + PSR.Name))
      [34melse[39;49;00m
        Add(Path + PSR.Name);
      Res := [36mFindNext[39;49;00m(PSR);
    [34mend[39;49;00m;
    [36mFindClose[39;49;00m(PSR);
    [34mif[39;49;00m [34mnot[39;49;00m ScanSubDirs [34mthen[39;49;00m
      [34mExit[39;49;00m;

    Res := [36mFindFirst[39;49;00m(Path + [33m'[39;49;00m[33m*[39;49;00m[33m'[39;49;00m, faDirectory, PSR);
    [34mwhile[39;49;00m Success(Res, [34m0[39;49;00m) [34mdo[39;49;00m [34mbegin[39;49;00m
      [34mif[39;49;00m (PSR.Attr [34mand[39;49;00m faDirectory > [34m0[39;49;00m)
       [34mand[39;49;00m (PSR.Name <> [33m'[39;49;00m[33m.[39;49;00m[33m'[39;49;00m) [34mand[39;49;00m (PSR.Name <> [33m'[39;49;00m[33m..[39;49;00m[33m'[39;49;00m) [34mthen[39;49;00m
        ScanDir(Path + PSR.Name + [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m, FileName);
      Res := [36mFindNext[39;49;00m(PSR);
    [34mend[39;49;00m;
    [36mFindClose[39;49;00m(PSR);
  [34mend[39;49;00m;

[34mbegin[39;49;00m
  Strings.Clear;
  Path := ExtractPath(Mask);
  FileName := [36mExtractFileName[39;49;00m(Mask);
  ScanDir(Path, FileName);
  [36mResult[39;49;00m := Strings.Count > [34m0[39;49;00m;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mFindAllFirst[39;49;00m([34mconst[39;49;00m Mask: [34mstring[39;49;00m; ScanSubDirs: [36mBoolean[39;49;00m = [34mTrue[39;49;00m;
  Attributes: [36mInteger[39;49;00m = faFindEveryFile): [34mstring[39;49;00m;
[34mvar[39;49;00m
  Path, FileName: [34mstring[39;49;00m;

  [34mfunction[39;49;00m [32mScanDir[39;49;00m([34mconst[39;49;00m Path, FileName: [34mstring[39;49;00m): [36mBoolean[39;49;00m;
  [34mvar[39;49;00m
    PSR: TSearchRec;
    Res: [36mInteger[39;49;00m;
  [34mbegin[39;49;00m
    [36mResult[39;49;00m := [34mFalse[39;49;00m;
    [34mif[39;49;00m Success([36mFindFirst[39;49;00m(Path + FileName, Attributes, PSR), [34m0[39;49;00m) [34mthen[39;49;00m [34mbegin[39;49;00m
      FindAllFirst := Path + PSR.Name;
      [36mResult[39;49;00m := [34mTrue[39;49;00m;
      [36mFindClose[39;49;00m(PSR);
    [34mExit[39;49;00m; [34mend[39;49;00m;
    [34mif[39;49;00m [34mnot[39;49;00m ScanSubDirs [34mthen[39;49;00m
      [34mExit[39;49;00m;

    Res := [36mFindFirst[39;49;00m(Path + [33m'[39;49;00m[33m*[39;49;00m[33m'[39;49;00m, faDirectory, PSR);
    [34mwhile[39;49;00m [34mnot[39;49;00m [36mResult[39;49;00m [34mand[39;49;00m Success(Res, [34m0[39;49;00m) [34mdo[39;49;00m [34mbegin[39;49;00m
      [34mif[39;49;00m (PSR.Attr [34mand[39;49;00m faDirectory > [34m0[39;49;00m)
       [34mand[39;49;00m (PSR.Name <> [33m'[39;49;00m[33m.[39;49;00m[33m'[39;49;00m) [34mand[39;49;00m (PSR.Name <> [33m'[39;49;00m[33m..[39;49;00m[33m'[39;49;00m) [34mthen[39;49;00m
        [36mResult[39;49;00m := ScanDir(Path + PSR.Name + [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m, FileName);
      Res := [36mFindNext[39;49;00m(PSR);
    [34mend[39;49;00m;
    [36mFindClose[39;49;00m(PSR);
  [34mend[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;
  Path := ExtractPath(Mask);
  FileName := [36mExtractFileName[39;49;00m(Mask);
  ScanDir(Path, FileName);
[34mend[39;49;00m;

[34mprocedure[39;49;00m [32mDeleteFiles[39;49;00m([34mconst[39;49;00m Mask: [34mstring[39;49;00m; ScanSubDirs: [36mBoolean[39;49;00m = [34mTrue[39;49;00m;
  Attributes: [36mInteger[39;49;00m = faFindEveryFile);
[34mvar[39;49;00m
  Path, FileName: [34mstring[39;49;00m;

  [34mprocedure[39;49;00m [32mScanDir[39;49;00m([34mconst[39;49;00m Path, FileName: [34mstring[39;49;00m);
  [34mvar[39;49;00m
    PSR: TSearchRec;
    Res: [36mInteger[39;49;00m;

    [34mprocedure[39;49;00m [32mTryDeleteFile[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m);
    [34mbegin[39;49;00m
      [34mtry[39;49;00m
        [36mDeleteFile[39;49;00m(Path + PSR.Name);
      [34mexcept[39;49;00m
      [34mend[39;49;00m;
    [34mend[39;49;00m;

  [34mbegin[39;49;00m
    Res := [36mFindFirst[39;49;00m(Path + FileName, Attributes, PSR);
    [34mwhile[39;49;00m Success(Res, [34m0[39;49;00m) [34mdo[39;49;00m [34mbegin[39;49;00m
      TryDeleteFile(Path + PSR.Name);
      Res := [36mFindNext[39;49;00m(PSR);
    [34mend[39;49;00m;
    [36mFindClose[39;49;00m(PSR);
    [34mif[39;49;00m [34mnot[39;49;00m ScanSubDirs [34mthen[39;49;00m
      [34mExit[39;49;00m;

    Res := [36mFindFirst[39;49;00m(Path + [33m'[39;49;00m[33m*[39;49;00m[33m'[39;49;00m, faDirectory, PSR);
    [34mwhile[39;49;00m Success(Res, [34m0[39;49;00m) [34mdo[39;49;00m [34mbegin[39;49;00m
      [34mif[39;49;00m (PSR.Attr [34mand[39;49;00m faDirectory > [34m0[39;49;00m)
       [34mand[39;49;00m (PSR.Name <> [33m'[39;49;00m[33m.[39;49;00m[33m'[39;49;00m) [34mand[39;49;00m (PSR.Name <> [33m'[39;49;00m[33m..[39;49;00m[33m'[39;49;00m) [34mthen[39;49;00m [34mbegin[39;49;00m
        ScanDir(Path + PSR.Name + [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m, FileName);
        TryDeleteFile(Path + PSR.Name);
      [34mend[39;49;00m;
      Res := [36mFindNext[39;49;00m(PSR);
    [34mend[39;49;00m;
    [36mFindClose[39;49;00m(PSR);
  [34mend[39;49;00m;
[34mbegin[39;49;00m
  Path := ExtractPath(Mask);
  FileName := [36mExtractFileName[39;49;00m(Mask);
  ScanDir(Path, FileName);
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mGetFileNew[39;49;00m(FileName: [34mstring[39;49;00m; NoFloppyDrives: [36mBoolean[39;49;00m = [34mTrue[39;49;00m): [34mstring[39;49;00m;
[34mvar[39;49;00m
  Drive: [34mstring[39;49;00m;
  pf, pd, Len: [36mInteger[39;49;00m;
  PSR: TSearchRec;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;
  FileName := [36mTrim[39;49;00m(FileName);
  [34mif[39;49;00m [36mLength[39;49;00m(FileName) < [34m2[39;49;00m [34mthen[39;49;00m
    [34mExit[39;49;00m;

  Drive := ExtractDrive(FileName);
  [34mif[39;49;00m [34mnot[39;49;00m [36mDirectoryExists[39;49;00m(Drive) [34mthen[39;49;00m
    [34mExit[39;49;00m;

  [34mif[39;49;00m NoFloppyDrives [34mand[39;49;00m (Drive[[34m1[39;49;00m] [34min[39;49;00m [[33m'[39;49;00m[33mA[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mB[39;49;00m[33m'[39;49;00m]) [34mthen[39;49;00m
    [34mExit[39;49;00m;

  Len := [36mLength[39;49;00m(FileName);
  [36mResult[39;49;00m := Drive;
  pf := [36mLength[39;49;00m(Drive) + [34m1[39;49;00m;
  [34mwhile[39;49;00m pf <= Len [34mdo[39;49;00m [34mbegin[39;49;00m
    [34mif[39;49;00m FileName[pf] = [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m
      [36mResult[39;49;00m := [36mResult[39;49;00m + [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m;
      [36mInc[39;49;00m(pf);
    [34mContinue[39;49;00m; [34mend[39;49;00m;

    pd := CharPos([33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m, FileName, pf);
    [34mif[39;49;00m pd = [34m0[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m
      [34mif[39;49;00m [34m0[39;49;00m=[36mFindFirst[39;49;00m([36mResult[39;49;00m + [36mCopy[39;49;00m(FileName, pf, MaxInt), faFindEveryFile, PSR) [34mthen[39;49;00m [34mbegin[39;49;00m
        [36mResult[39;49;00m := [36mResult[39;49;00m + PSR.Name;
      [34mBreak[39;49;00m; [34mend[39;49;00m [34melse[39;49;00m [34mbegin[39;49;00m
        [36mFindClose[39;49;00m(PSR);
        [34mif[39;49;00m [34m0[39;49;00m=[36mFindFirst[39;49;00m([36mResult[39;49;00m + [36mCopy[39;49;00m(FileName, pf, MaxInt), faDirectory, PSR) [34mthen[39;49;00m
          [36mResult[39;49;00m := [36mResult[39;49;00m + PSR.Name + [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m
        [34melse[39;49;00m
          [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;
        [36mFindClose[39;49;00m(PSR);
        [34mif[39;49;00m [36mResult[39;49;00m = [33m'[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m
          [34mBreak[39;49;00m;
      [34mend[39;49;00m;
    [34mend[39;49;00m;

    [34mif[39;49;00m [34m0[39;49;00m=[36mFindFirst[39;49;00m([36mResult[39;49;00m + [36mCopy[39;49;00m(FileName, pf, pd - pf), faDirectory, PSR) [34mthen[39;49;00m
      [36mResult[39;49;00m := [36mResult[39;49;00m + PSR.Name + [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m
    [34melse[39;49;00m
      [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;
    [36mFindClose[39;49;00m(PSR);
    [34mif[39;49;00m [36mResult[39;49;00m = [33m'[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m
      [34mBreak[39;49;00m;

    pf := pd + [34m1[39;49;00m;
  [34mend[39;49;00m;

  [34mif[39;49;00m ([36mResult[39;49;00m <> [33m'[39;49;00m[33m'[39;49;00m) [34mand[39;49;00m [34mnot[39;49;00m FileEx([36mResult[39;49;00m, [34mTrue[39;49;00m) [34mthen[39;49;00m
    [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mDateTimeOfFileTime[39;49;00m([34mconst[39;49;00m FileTime: TFileTime): [36mTDateTime[39;49;00m;
[34mvar[39;49;00m
  LocalFileTime: TFileTime;
  Res: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [34m0[39;49;00m;

  FileTimeToLocalFileTime(FileTime, LocalFileTime);
  [34mif[39;49;00m [34mnot[39;49;00m FileTimeToDosDateTime(LocalFileTime, LongRec(Res).Hi,
   LongRec(Res).Lo) [34mthen[39;49;00m
    Res := -[34m1[39;49;00m;

  [34mif[39;49;00m (Res = -[34m1[39;49;00m) [34mor[39;49;00m (Res = [34m0[39;49;00m) [34mthen[39;49;00m
    [34mExit[39;49;00m;
  [34mtry[39;49;00m
    [36mResult[39;49;00m := [36mFileDateToDateTime[39;49;00m(Res);
  [34mexcept[39;49;00m
  [34mend[39;49;00m;
[34mend[39;49;00m;

[34mprocedure[39;49;00m [32mFileNew[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m);
[34mvar[39;49;00m
  Handle: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  Handle := [36mFileCreate[39;49;00m(FileName);
  [36mFileClose[39;49;00m(Handle);
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mWin32PlatformStr[39;49;00m: [34mstring[39;49;00m;
[34mconst[39;49;00m
  PlatformStrings: [34marray[39;49;00m[VER_PLATFORM_WIN32s..VER_PLATFORM_WIN32_NT] [34mof[39;49;00m [34mstring[39;49;00m =
    ([33m'[39;49;00m[33mVER_PLATFORM_WIN32s[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mVER_PLATFORM_WIN32_WINDOWS[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mVER_PLATFORM_WIN32_NT[39;49;00m[33m'[39;49;00m);
[34mbegin[39;49;00m
  [36mResult[39;49;00m := PlatformStrings[Win32Platform];
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mFullOSInfo[39;49;00m: [34mstring[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [36mFormat[39;49;00m(
    [33m'[39;49;00m[33mPlatform: %s[39;49;00m[33m'[39;49;00m + EOL +
    [33m'[39;49;00m[33mVersion: %d.%d Build %d[39;49;00m[33m'[39;49;00m + EOL +
    [33m'[39;49;00m[33mCSD: %s[39;49;00m[33m'[39;49;00m,
    [
      Win32PlatformStr,
      Win32MajorVersion, Win32MinorVersion, Win32BuildNumber,
      Win32CSDVersion
    ]
  );
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mWin9x[39;49;00m: [36mBoolean[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := Win32Platform = VER_PLATFORM_WIN32_WINDOWS;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mWinNT[39;49;00m: [36mBoolean[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := Win32Platform = VER_PLATFORM_WIN32_NT;
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mWin2000[39;49;00m: [36mBoolean[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := (Win32Platform = VER_PLATFORM_WIN32_NT)
            [34mand[39;49;00m (Win32MajorVersion = [34m4[39;49;00m);
[34mend[39;49;00m;

[34mfunction[39;49;00m [32mWinXP[39;49;00m: [36mBoolean[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := Win32MajorVersion >= [34m5[39;49;00m;
[34mend[39;49;00m;

[34minitialization[39;49;00m
  MyDir := GetMyDir;

[34mend[39;49;00m.

[34munit[39;49;00m FifoStream;

[34minterface[39;49;00m

[34muses[39;49;00m Classes, windows, Dialogs;

[34mconst[39;49;00m
  DefaultChunksize = [34m32768[39;49;00m; [37m// 32kb per chunk as default.[39;49;00m

[34mtype[39;49;00m
  PMemChunk = ^TMemChunk;
  TMemChunk = [34mrecord[39;49;00m
    Filled: [36mLongword[39;49;00m;
    [36mRead[39;49;00m: [36mLongword[39;49;00m;
    Data: [36mpointer[39;49;00m;
  [34mend[39;49;00m;

  TFifo = [34mclass[39;49;00m
  [34mprivate[39;49;00m
    FBuffers: TList;
    FChunksize: [36mLongword[39;49;00m;
    FCritSect: TRTLCriticalSection;
    FIsWinNT: [36mboolean[39;49;00m;
    FBytesInFifo: [36mLongWord[39;49;00m;
  [34mprotected[39;49;00m
    [34mfunction[39;49;00m [32mGetBytesInFifo[39;49;00m: [36mLongWord[39;49;00m;
  [34mpublic[39;49;00m
    [34mconstructor[39;49;00m [32mCreate[39;49;00m;
    [34mdestructor[39;49;00m [32mDestroy[39;49;00m; [34moverride[39;49;00m;
    [34mprocedure[39;49;00m [32mWrite[39;49;00m(Data: [36mpointer[39;49;00m; Size: [36mLongWord[39;49;00m);
    [34mprocedure[39;49;00m [32mRead[39;49;00m(Buff: [36mpointer[39;49;00m; [34mvar[39;49;00m ReqSize: [36mLongWord[39;49;00m);
    [34mprocedure[39;49;00m [32mPeekData[39;49;00m(Buff: [36mpointer[39;49;00m; [34mvar[39;49;00m ReqSize: [36mLongWord[39;49;00m);
  [34mpublished[39;49;00m
    [34mproperty[39;49;00m BytesInFifo: [36mLongWord[39;49;00m [34mread[39;49;00m [32mFBytesInFifo[39;49;00m;
  [34mend[39;49;00m;

[34mimplementation[39;49;00m

[34mconstructor[39;49;00m [04m[32mTFifo[39;49;00m.[32mCreate[39;49;00m;
[34mbegin[39;49;00m
  [34minherited[39;49;00m;
  FBuffers := TList.Create;
  [37m// set default chunksize...[39;49;00m
  FChunksize := DefaultChunksize;
  InitializeCriticalSection(FCritSect);
[34mend[39;49;00m;

[34mdestructor[39;49;00m [04m[32mTFifo[39;49;00m.[32mDestroy[39;49;00m;
[34mvar[39;49;00m
  I: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  EnterCriticalSection(FCritSect);
  [34mfor[39;49;00m I := [34m0[39;49;00m [34mto[39;49;00m FBuffers.count - [34m1[39;49;00m [34mdo[39;49;00m
  [34mbegin[39;49;00m
    [36mFreeMem[39;49;00m(PMemChunk(Fbuffers[I]).Data);
    [34mDispose[39;49;00m(PMemChunk(Fbuffers[I]));
  [34mend[39;49;00m;
  FBuffers.Clear;
  FBuffers.Free;
  LeaveCriticalSection(FCritSect);

  DeleteCriticalSection(FCritSect);
  [34minherited[39;49;00m;
[34mend[39;49;00m;

[34mfunction[39;49;00m [04m[32mTFifo[39;49;00m.[32mGetBytesInFifo[39;49;00m: [36mLongWord[39;49;00m;
[34mbegin[39;49;00m
  [36mResult[39;49;00m := [34m0[39;49;00m;
  [34mif[39;49;00m FBuffers.Count = [34m0[39;49;00m [34mthen[39;49;00m
  [34mbegin[39;49;00m
    [34mexit[39;49;00m;
  [34mend[39;49;00m
  [34melse[39;49;00m
  [34mbegin[39;49;00m
    [34mif[39;49;00m FBuffers.Count > [34m1[39;49;00m [34mthen[39;49;00m
      [36mInc[39;49;00m([36mResult[39;49;00m, (FBuffers.Count - [34m1[39;49;00m) * FChunkSize);
    [36mInc[39;49;00m([36mResult[39;49;00m, PMemChunk(FBuffers[Fbuffers.Count - [34m1[39;49;00m]).Filled);
    [36mDec[39;49;00m([36mResult[39;49;00m, PMemChunk(FBuffers[[34m0[39;49;00m]).Read);
  [34mend[39;49;00m;
[34mend[39;49;00m;

[34mprocedure[39;49;00m [04m[32mTFifo[39;49;00m.[32mWrite[39;49;00m(Data: [36mpointer[39;49;00m; Size: [36mLongWord[39;49;00m);
[34mvar[39;49;00m
  Privpointer: [36mpointer[39;49;00m;
  PrivSize: [36mLongWord[39;49;00m;
  Chunk: PMemChunk;
  PosInChunk: [36mpointer[39;49;00m;
[34mbegin[39;49;00m
  [34mif[39;49;00m [36mLongWord[39;49;00m(Data) = [34m0[39;49;00m [34mthen[39;49;00m
  [34mbegin[39;49;00m
    [37m// null pointer? somebody is trying to fool us, get out...[39;49;00m
    [34mExit[39;49;00m;
  [34mend[39;49;00m;
  EnterCriticalSection(FCritSect);
  PrivPointer := Data;
  PrivSize := [34m0[39;49;00m;
  [37m// are already buffers there?[39;49;00m
  [34mif[39;49;00m FBuffers.count > [34m0[39;49;00m [34mthen[39;49;00m
  [34mbegin[39;49;00m
    [37m// is the last one of them not completely filled?[39;49;00m
    [34mif[39;49;00m PMemChunk(FBuffers[FBuffers.count - [34m1[39;49;00m]).filled < FChunksize [34mthen[39;49;00m
      [37m// not completely filled, so fill up the buffer.[39;49;00m
    [34mbegin[39;49;00m
      Chunk := PMemChunk(FBuffers[FBuffers.count - [34m1[39;49;00m]);
      [37m// fetch chunkdata.[39;49;00m
      PosInChunk := Chunk.Data;
      [37m// move to current fill pos...[39;49;00m
      [36mInc[39;49;00m([36mLongWord[39;49;00m(PosInChunk), Chunk.Filled);
      [37m// can we fill the chunk completely?[39;49;00m
      [34mif[39;49;00m Size > FChunksize - Chunk.Filled [34mthen[39;49;00m
      [34mbegin[39;49;00m
        [37m// yes we can.[39;49;00m
        [36mMove[39;49;00m(PrivPointer^, PosInChunk^, FChunksize - Chunk.Filled);
        [36mInc[39;49;00m(PrivSize, FChunksize - Chunk.Filled);
        [36mInc[39;49;00m([36mLongWord[39;49;00m(PrivPointer), FChunksize - Chunk.Filled);
        Chunk.Filled := FChunkSize;
      [34mend[39;49;00m
      [34melse[39;49;00m
        [37m// we have to less data for filling the chunk completely,[39;49;00m
        [37m// just put everything in.[39;49;00m
      [34mbegin[39;49;00m
        [36mMove[39;49;00m(PrivPointer^, PosInChunk^, Size);
        [36mInc[39;49;00m(PrivSize, Size);
        [36mInc[39;49;00m(Chunk.Filled, Size);
      [34mend[39;49;00m;
    [34mend[39;49;00m;
  [34mend[39;49;00m;
  [37m// as long as we have remaining stuff put it into new chunks.[39;49;00m
  [34mwhile[39;49;00m (PrivSize < Size) [34mdo[39;49;00m
  [34mbegin[39;49;00m
    [34mnew[39;49;00m(Chunk);
    [36mGetMem[39;49;00m(Chunk.Data, FChunksize);
    Chunk.Read := [34m0[39;49;00m;
    [37m// can we fill an entire chunk with the remaining data?[39;49;00m
    [34mif[39;49;00m Privsize + FChunksize < Size [34mthen[39;49;00m
    [34mbegin[39;49;00m
      [37m// yes we can, so put the stuff in.[39;49;00m
      [36mMove[39;49;00m(Privpointer^, Chunk.Data^, FChunksize);
      [36mInc[39;49;00m([36mLongWord[39;49;00m(PrivPointer), FChunksize);
      [36mInc[39;49;00m(PrivSize, FChunksize);
      Chunk.Filled := FChunksize;
    [34mend[39;49;00m
    [34melse[39;49;00m [37m// we have to less data to fill the entire chunk, just put the remaining stuff in.[39;49;00m
    [34mbegin[39;49;00m
      [36mMove[39;49;00m(Privpointer^, Chunk.Data^, Size - Privsize);
      Chunk.Filled := Size - Privsize;
      [36mInc[39;49;00m(PrivSize, Size - Privsize);
    [34mend[39;49;00m;
    Fbuffers.Add(Chunk);
  [34mend[39;49;00m;
  [34mif[39;49;00m Size <> Privsize [34mthen[39;49;00m
    Showmessage([33m'[39;49;00m[33mmiscalculation in TFifo.write[39;49;00m[33m'[39;49;00m);
  FBytesInFifo := GetBytesInFifo;
  LeaveCriticalSection(FCritSect);
[34mend[39;49;00m;

[34mprocedure[39;49;00m [04m[32mTFifo[39;49;00m.[32mRead[39;49;00m(Buff: [36mpointer[39;49;00m; [34mvar[39;49;00m ReqSize: [36mLongWord[39;49;00m);
[34mvar[39;49;00m
  PrivSize: [36mInteger[39;49;00m;
  Privpos: [36mpointer[39;49;00m;
  Chunk: PMemChunk;
  ChunkPos: [36mpointer[39;49;00m;
[34mbegin[39;49;00m
  [34mif[39;49;00m [36mLongWord[39;49;00m(Buff) = [34m0[39;49;00m [34mthen[39;49;00m
  [34mbegin[39;49;00m
    [37m// null pointer? somebody is trying to fool us, get out...[39;49;00m
    [34mExit[39;49;00m;
  [34mend[39;49;00m;
  EnterCriticalSection(FCritSect);
  PrivSize := [34m0[39;49;00m;
  Privpos := Buff;
  [34mwhile[39;49;00m FBuffers.Count > [34m0[39;49;00m [34mdo[39;49;00m
  [34mbegin[39;49;00m
    Chunk := PMemChunk(FBuffers[[34m0[39;49;00m]);
    ChunkPos := Chunk.data;
    [36mInc[39;49;00m([36mLongWord[39;49;00m(ChunkPos), Chunk.Read);
    [37m// does the remaining part of the chunk fit into the buffer?[39;49;00m
    [34mif[39;49;00m PrivSize + (Chunk.Filled - Chunk.read) < ReqSize [34mthen[39;49;00m
    [34mbegin[39;49;00m [37m// yep, it fits[39;49;00m
      [36mMove[39;49;00m(ChunkPos^, Privpos^, Chunk.Filled - Chunk.read);
      [36mInc[39;49;00m(PrivSize, Chunk.Filled - Chunk.read);
      [36mFreeMem[39;49;00m(Chunk.Data);
      [34mDispose[39;49;00m(Chunk);
      FBuffers.Delete([34m0[39;49;00m);
    [34mend[39;49;00m
    [34melse[39;49;00m [37m// remaining part didn't fit, get as much as we can and increment the[39;49;00m
      [37m// read attribute.[39;49;00m
    [34mbegin[39;49;00m
      [36mMove[39;49;00m(ChunkPos^, Privpos^, ReqSize - PrivSize);
      [36mInc[39;49;00m(Chunk.read, ReqSize - PrivSize);
      [36mInc[39;49;00m(PrivSize, ReqSize - PrivSize);
      [37m// as we filled the buffer, we'll have to break here.[39;49;00m
      [34mbreak[39;49;00m;
    [34mend[39;49;00m;
  [34mend[39;49;00m;
  FBytesInFifo := GetBytesInFifo;
  LeaveCriticalSection(FCritSect);
  ReqSize := PrivSize;
[34mend[39;49;00m;

[37m// read Data from Stream without removing it from the Stream...[39;49;00m

[34mprocedure[39;49;00m [04m[32mTFifo[39;49;00m.[32mPeekData[39;49;00m(Buff: [36mpointer[39;49;00m; [34mvar[39;49;00m ReqSize: [36mLongWord[39;49;00m);
[34mvar[39;49;00m
  PrivSize: [36mInteger[39;49;00m;
  Privpos: [36mpointer[39;49;00m;
  Chunk: PMemChunk;
  ChunkPos: [36mpointer[39;49;00m;
  ChunkNr: [36mInteger[39;49;00m;
[34mbegin[39;49;00m
  [34mif[39;49;00m [36mLongWord[39;49;00m(Buff) = [34m0[39;49;00m [34mthen[39;49;00m
  [34mbegin[39;49;00m
    [37m// null pointer? somebody is trying to fool us, get out...[39;49;00m
    [34mExit[39;49;00m;
  [34mend[39;49;00m;
  EnterCriticalSection(FCritSect);
  PrivSize := [34m0[39;49;00m;
  Privpos := Buff;
  ChunkNr := [34m0[39;49;00m;
  [34mwhile[39;49;00m FBuffers.Count > ChunkNr [34mdo[39;49;00m
  [34mbegin[39;49;00m
    Chunk := PMemChunk(FBuffers[ChunkNr]);
    ChunkPos := Chunk.data;
    [36mInc[39;49;00m([36mLongWord[39;49;00m(ChunkPos), Chunk.Read);
    [37m// does the remaining part of the chunk fit into the buffer?[39;49;00m
    [34mif[39;49;00m PrivSize + (Chunk.Filled - Chunk.read) < ReqSize [34mthen[39;49;00m
    [34mbegin[39;49;00m [37m// yep, it fits[39;49;00m
      [36mMove[39;49;00m(ChunkPos^, Privpos^, Chunk.Filled - Chunk.read);
      [36mInc[39;49;00m(PrivSize, Chunk.Filled - Chunk.read);
      [36mInc[39;49;00m(ChunkNr);
    [34mend[39;49;00m
    [34melse[39;49;00m [37m// remaining part didn't fit, get as much as we can and increment the[39;49;00m
      [37m// read attribute.[39;49;00m
    [34mbegin[39;49;00m
      [36mMove[39;49;00m(ChunkPos^, Privpos^, ReqSize - PrivSize);
      [36mInc[39;49;00m(PrivSize, ReqSize - PrivSize);
      [37m// as we filled the buffer, we'll have to break here.[39;49;00m
      [34mbreak[39;49;00m;
    [34mend[39;49;00m;
  [34mend[39;49;00m;
  LeaveCriticalSection(FCritSect);
  ReqSize := PrivSize;
[34mend[39;49;00m;

[34mend[39;49;00m.

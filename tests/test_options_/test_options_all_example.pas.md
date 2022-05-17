     1^I[37m// vim:ft=pascal[39;49;00m$
     2^I$
     3^I[34munit[39;49;00m YTools;$
     4^I$
     5^I[37m{===============================================================================[39;49;00m$
     6^I[37m[39;49;00m$
     7^I[37m   cYcnus.YTools 1.0.3 Beta for Delphi 4+[39;49;00m$
     8^I[37m   by licenser and Murphy[39;49;00m$
     9^I[37m[39;49;00m$
    10^I[37m   ©2000-2003 by cYcnus[39;49;00m$
    11^I[37m   visit www.cYcnus.de[39;49;00m$
    12^I[37m[39;49;00m$
    13^I[37m   licenser@cYcnus.de (Heinz N. Gies)[39;49;00m$
    14^I[37m   murphy@cYcnus.de (Kornelius Kalnbach)[39;49;00m$
    15^I[37m   [39;49;00m$
    16^I[37m   this unit is published under the terms of the GPL[39;49;00m$
    17^I[37m[39;49;00m$
    18^I[37m===============================================================================}[39;49;00m$
    19^I$
    20^I[34minterface[39;49;00m$
    21^I$
    22^I[34muses[39;49;00m$
    23^I  Windows, SysUtils, Classes, YTypes;$
    24^I$
    25^I[34mconst[39;49;00m$
    26^I  BackSpace = [33m#8[39;49;00m;$
    27^I  Tab = [33m#9[39;49;00m;$
    28^I  LF = [33m#10[39;49;00m; [37m//Line Feed[39;49;00m$
    29^I  CR = [33m#13[39;49;00m; [37m//Carriage Return[39;49;00m$
    30^I  Space = [33m#32[39;49;00m;$
    31^I  EOLChars = [CR, LF];$
    32^I[37m{$IFNDEF VER140}[39;49;00m$
    33^I  sLineBreak = [33m#13[39;49;00m[33m#10[39;49;00m;$
    34^I  SwitchChars = [[33m'[39;49;00m[33m/[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33m-[39;49;00m[33m'[39;49;00m];$
    35^I[37m{$ENDIF}[39;49;00m$
    36^I  EOL = sLineBreak;$
    37^I  MaxCard = [36mHigh[39;49;00m([36mCardinal[39;49;00m);$
    38^I  AllChars = [[33m#0[39;49;00m..[33m#255[39;49;00m];$
    39^I  Alphabetical = [[33m'[39;49;00m[33mA[39;49;00m[33m'[39;49;00m..[33m'[39;49;00m[33mZ[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33ma[39;49;00m[33m'[39;49;00m..[33m'[39;49;00m[33mz[39;49;00m[33m'[39;49;00m];$
    40^I  DecimalChars = [[33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m..[33m'[39;49;00m[33m9[39;49;00m[33m'[39;49;00m];$
    41^I  AlphaNumerical = Alphabetical + DecimalChars;$
    42^I  StrangeChars = [[33m#0[39;49;00m..[33m#31[39;49;00m, [33m#127[39;49;00m, [33m#129[39;49;00m, [33m#141[39;49;00m..[33m#144[39;49;00m, [33m#157[39;49;00m, [33m#158[39;49;00m];$
    43^I$
    44^I  HexadecimalChars = DecimalChars + [[33m'[39;49;00m[33mA[39;49;00m[33m'[39;49;00m..[33m'[39;49;00m[33mF[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33ma[39;49;00m[33m'[39;49;00m..[33m'[39;49;00m[33mf[39;49;00m[33m'[39;49;00m];$
    45^I  OctalChars = [[33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m..[33m'[39;49;00m[33m7[39;49;00m[33m'[39;49;00m];$
    46^I  BinaryChars = [[33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33m1[39;49;00m[33m'[39;49;00m];$
    47^I$
    48^I  QuoteChars = [[33m'[39;49;00m[33m''[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33m"[39;49;00m[33m'[39;49;00m];$
    49^I  WildCards = [[33m'[39;49;00m[33m*[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33m?[39;49;00m[33m'[39;49;00m];$
    50^I  FileNameEnemies = WildCards + [[33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33m/[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33m:[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33m<[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33m>[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33m|[39;49;00m[33m'[39;49;00m];$
    51^I$
    52^I  HexChar: [34marray[39;49;00m[THex] [34mof[39;49;00m [36mChar[39;49;00m = ($
    53^I    [33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m1[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m2[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m3[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m4[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m5[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m6[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m7[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m8[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m9[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mA[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mB[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mC[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mD[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mE[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mF[39;49;00m[33m'[39;49;00m);$
    54^I  LowerHexChar: [34marray[39;49;00m[THex] [34mof[39;49;00m [36mChar[39;49;00m = ($
    55^I    [33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m1[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m2[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m3[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m4[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m5[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m6[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m7[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m8[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m9[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33ma[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mb[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mc[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33md[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33me[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mf[39;49;00m[33m'[39;49;00m);$
    56^I  BaseNChar: [34marray[39;49;00m[TBaseN] [34mof[39;49;00m [36mChar[39;49;00m = ($
    57^I    [33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m1[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m2[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m3[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m4[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m5[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m6[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m7[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m8[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33m9[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mA[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mB[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mC[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mD[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mE[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mF[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mG[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mH[39;49;00m[33m'[39;49;00m,$
    58^I    [33m'[39;49;00m[33mI[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mJ[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mK[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mL[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mM[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mN[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mO[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mP[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mQ[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mR[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mS[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mT[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mU[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mV[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mW[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mX[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mY[39;49;00m[33m'[39;49;00m,[33m'[39;49;00m[33mZ[39;49;00m[33m'[39;49;00m);$
    59^I$
    60^I  cYcnusOverlayColor = [34m$050001[39;49;00m;$
    61^I$
    62^I  faFindEveryFile = faReadOnly + faHidden + faSysFile + faArchive;$
    63^I$
    64^I  platWin9x = [VER_PLATFORM_WIN32s, VER_PLATFORM_WIN32_WINDOWS];$
    65^I$
    66^I$
    67^I[37m{ Debugging }[39;49;00m$
    68^I[34mprocedure[39;49;00m [32mClearReport[39;49;00m([34mconst[39;49;00m ReportName: [34mstring[39;49;00m);$
    69^I[34mprocedure[39;49;00m [32mReport[39;49;00m([34mconst[39;49;00m ReportName, Text: [34mstring[39;49;00m);$
    70^I[34mprocedure[39;49;00m [32mReportFmt[39;49;00m([34mconst[39;49;00m ReportName, Fmt: [34mstring[39;49;00m; [34mconst[39;49;00m Args: [34marray[39;49;00m [34mof[39;49;00m [34mconst[39;49;00m);$
    71^I$
    72^I[37m{ Params }[39;49;00m$
    73^I[34mprocedure[39;49;00m [32mGetParams[39;49;00m(Strings: TStrings); overload;$
    74^I[34mfunction[39;49;00m [32mGetParams[39;49;00m([34mconst[39;49;00m Separator: [34mstring[39;49;00m = [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m; overload;$
    75^I$
    76^I[34mfunction[39;49;00m [32mParamNum[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [36mInteger[39;49;00m;$
    77^I[34mfunction[39;49;00m [32mParamPrefixNum[39;49;00m([34mconst[39;49;00m Prefix: [34mstring[39;49;00m): [36mInteger[39;49;00m;$
    78^I[34mfunction[39;49;00m [32mParam[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
    79^I[34mfunction[39;49;00m [32mParamPrefix[39;49;00m([34mconst[39;49;00m Prefix: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
    80^I$
    81^I[34mfunction[39;49;00m [32mSwitch[39;49;00m([34mconst[39;49;00m Switch: [34mstring[39;49;00m; [34mconst[39;49;00m PrefixChars: TCharSet = SwitchChars;$
    82^I  IgnoreCase: [36mBoolean[39;49;00m = [34mTrue[39;49;00m): [36mBoolean[39;49;00m;$
    83^I[34mfunction[39;49;00m [32mGetParam[39;49;00m([34mconst[39;49;00m Prefix: [34mstring[39;49;00m = [33m'[39;49;00m[33m'[39;49;00m; [34mconst[39;49;00m [34mDefault[39;49;00m: [34mstring[39;49;00m = [33m'[39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;$
    84^I$
    85^I[37m{ Dirs & UserName}[39;49;00m$
    86^I[34mfunction[39;49;00m [32mGetMyDir[39;49;00m(FullPath: [36mBoolean[39;49;00m = [34mFalse[39;49;00m): [34mstring[39;49;00m;$
    87^I[34mfunction[39;49;00m [32mWinDir[39;49;00m: [34mstring[39;49;00m;$
    88^I[34mfunction[39;49;00m [32mSysDir[39;49;00m: [34mstring[39;49;00m;$
    89^I[34mfunction[39;49;00m [32mUserName[39;49;00m: [34mstring[39;49;00m;$
    90^I$
    91^I[37m{ Strings & Chars}[39;49;00m$
    92^I[34mfunction[39;49;00m [32mFirstChar[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [36mChar[39;49;00m;$
    93^I[34mfunction[39;49;00m [32mLastChar[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [36mChar[39;49;00m;$
    94^I$
    95^I[34mfunction[39;49;00m [32mCharPos[39;49;00m(C: [36mChar[39;49;00m; [34mconst[39;49;00m S: [34mstring[39;49;00m; Offset: [36mInteger[39;49;00m = [34m1[39;49;00m): [36mInteger[39;49;00m; overload;$
    96^I[34mfunction[39;49;00m [32mCharPos[39;49;00m(C: TCharSet; [34mconst[39;49;00m S: [34mstring[39;49;00m; Offset: [36mInteger[39;49;00m = [34m1[39;49;00m): [36mInteger[39;49;00m; overload;$
    97^I[34mfunction[39;49;00m [32mCharPosR[39;49;00m(C: [36mChar[39;49;00m; [34mconst[39;49;00m S: [34mstring[39;49;00m; Offset: [36mInteger[39;49;00m = -[34m1[39;49;00m): [36mInteger[39;49;00m;$
    98^I[34mfunction[39;49;00m [32mPosEx[39;49;00m([34mconst[39;49;00m SubStr, S: [34mstring[39;49;00m; Offset: [36mInteger[39;49;00m = [34m1[39;49;00m): [36mInteger[39;49;00m;$
    99^I[34mfunction[39;49;00m [32mPosExText[39;49;00m([34mconst[39;49;00m SubStr, S: [34mstring[39;49;00m; Offset: [36mInteger[39;49;00m = [34m1[39;49;00m): [36mInteger[39;49;00m;$
   100^I[34mfunction[39;49;00m [32mPosExAnsiText[39;49;00m([34mconst[39;49;00m SubStr, S: [34mstring[39;49;00m; Offset: [36mInteger[39;49;00m = [34m1[39;49;00m): [36mInteger[39;49;00m;$
   101^I$
   102^I[34mfunction[39;49;00m [32mUntilChar[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Brake: [36mChar[39;49;00m): [34mstring[39;49;00m; overload;$
   103^I[34mfunction[39;49;00m [32mUntilChar[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Brake: TCharSet): [34mstring[39;49;00m; overload;$
   104^I[34mfunction[39;49;00m [32mUntilLastChar[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Brake: [36mChar[39;49;00m;$
   105^I  IgnoreNoBrake: [36mBoolean[39;49;00m = [34mTrue[39;49;00m): [34mstring[39;49;00m;$
   106^I$
   107^I[34mfunction[39;49;00m [32mFromChar[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Brake: [36mChar[39;49;00m): [34mstring[39;49;00m; overload;$
   108^I[34mfunction[39;49;00m [32mFromChar[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Brake: TCharSet): [34mstring[39;49;00m; overload;$
   109^I[34mfunction[39;49;00m [32mFromLastChar[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Brake: [36mChar[39;49;00m;$
   110^I  IgnoreNoBrake: [36mBoolean[39;49;00m = [34mFalse[39;49;00m): [34mstring[39;49;00m;$
   111^I$
   112^I[34mfunction[39;49;00m [32mBetweenChars[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Start, Finish: [36mChar[39;49;00m;$
   113^I  Inclusive: [36mBoolean[39;49;00m = [34mFalse[39;49;00m): [34mstring[39;49;00m;$
   114^I$
   115^I[34mfunction[39;49;00m [32mUntilStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Brake: [34mstring[39;49;00m): [34mstring[39;49;00m;$
   116^I[34mfunction[39;49;00m [32mFromStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Brake: [34mstring[39;49;00m): [34mstring[39;49;00m;$
   117^I$
   118^I[34mfunction[39;49;00m [32mStringWrap[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Width: [36mInteger[39;49;00m; [34mconst[39;49;00m LineEnd: [34mstring[39;49;00m = EOL): [34mstring[39;49;00m;$
   119^I$
   120^I[37m{ Splitting & Combining }[39;49;00m$
   121^I[34mfunction[39;49;00m [32mSplit[39;49;00m([34mconst[39;49;00m S, Separator: [34mstring[39;49;00m; IgnoreMultiSep: [36mBoolean[39;49;00m = [34mTrue[39;49;00m;$
   122^I  MinCount: [36mInteger[39;49;00m = [34m0[39;49;00m): TStrA; overload;$
   123^I[34mprocedure[39;49;00m [32mSplit[39;49;00m([34mconst[39;49;00m S, Separator: [34mstring[39;49;00m; Strings: TStrings;$
   124^I  IgnoreMultiSep: [36mBoolean[39;49;00m = [34mTrue[39;49;00m); overload;$
   125^I[34mfunction[39;49;00m [32mSplit[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Separators: TCharSet;$
   126^I  IgnoreMultiSep: [36mBoolean[39;49;00m = [34mTrue[39;49;00m; MinCount: [36mInteger[39;49;00m = [34m0[39;49;00m): TStrA; overload;$
   127^I$
   128^I[34mprocedure[39;49;00m [32mTileStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; BrakeStart: [36mInteger[39;49;00m; BrakeEnd: [36mInteger[39;49;00m;$
   129^I  out Left, Right: [34mstring[39;49;00m);$
   130^I$
   131^I[34mfunction[39;49;00m [32mJoin[39;49;00m(Strings: TStrings; Separator: [34mstring[39;49;00m = [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m; overload;$
   132^I[34mfunction[39;49;00m [32mJoin[39;49;00m(StrA: TStrA; Separator: [34mstring[39;49;00m = [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m; overload;$
   133^I$
   134^I[34mfunction[39;49;00m [32mMulStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Count: [36mInteger[39;49;00m): [34mstring[39;49;00m;$
   135^I$
   136^I[37m{ Strings ausrichten }[39;49;00m$
   137^I[34mfunction[39;49;00m [32mAlignR[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Width: [36mInteger[39;49;00m; Filler: [36mChar[39;49;00m = [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;$
   138^I[34mfunction[39;49;00m [32mMaxStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; MaxLen: [36mInteger[39;49;00m): [34mstring[39;49;00m;$
   139^I$
   140^I[37m{ Stringing }[39;49;00m$
   141^I[34mfunction[39;49;00m [32mTrimAll[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [34mstring[39;49;00m;$
   142^I$
   143^I[34mfunction[39;49;00m [32mControlChar[39;49;00m(C: [36mChar[39;49;00m): [36mBoolean[39;49;00m;$
   144^I[34mfunction[39;49;00m [32mFriendlyChar[39;49;00m(C: [36mChar[39;49;00m): [36mChar[39;49;00m;$
   145^I$
   146^I[34mfunction[39;49;00m [32mFriendlyStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [34mstring[39;49;00m; overload;$
   147^I[34mfunction[39;49;00m [32mFriendlyStr[39;49;00m(a: TByteA): [34mstring[39;49;00m; overload;$
   148^I$
   149^I[34mfunction[39;49;00m [32mQuote[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Quoter: [36mChar[39;49;00m = [33m'[39;49;00m[33m"[39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;$
   150^I[34mfunction[39;49;00m [32mUnQuote[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [34mstring[39;49;00m;$
   151^I[34mfunction[39;49;00m [32mDeQuote[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [34mstring[39;49;00m;$
   152^I$
   153^I[34mfunction[39;49;00m [32mStrNumerus[39;49;00m([34mconst[39;49;00m Value: [36mInteger[39;49;00m; [34mconst[39;49;00m Singular, Plural: [34mstring[39;49;00m;$
   154^I  [34mconst[39;49;00m Zero: [34mstring[39;49;00m = [33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;$
   155^I$
   156^I[34mfunction[39;49;00m [32mMakeStr[39;49;00m([34mconst[39;49;00m Items: [34marray[39;49;00m [34mof[39;49;00m [34mconst[39;49;00m; Separator: [34mstring[39;49;00m = [33m'[39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;$
   157^I[34mprocedure[39;49;00m [32mShowText[39;49;00m([34mconst[39;49;00m Items: [34marray[39;49;00m [34mof[39;49;00m [34mconst[39;49;00m; Separator: [34mstring[39;49;00m = [33m'[39;49;00m[33m'[39;49;00m);$
   158^I$
   159^I[37m{ Delete }[39;49;00m$
   160^I[34mfunction[39;49;00m [32mDeleteChars[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; C: [36mChar[39;49;00m): [34mstring[39;49;00m; overload;$
   161^I[34mfunction[39;49;00m [32mDeleteChars[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; C: TCharSet): [34mstring[39;49;00m; overload;$
   162^I[34mfunction[39;49;00m [32mExtractChars[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; C: TCharSet): [34mstring[39;49;00m;$
   163^I$
   164^I[37m{ Find }[39;49;00m$
   165^I[34mfunction[39;49;00m [32mCharCount[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; C: [36mChar[39;49;00m): [36mInteger[39;49;00m;$
   166^I$
   167^I[34mfunction[39;49;00m [32mCharIn[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; C: [36mChar[39;49;00m): [36mBoolean[39;49;00m; overload;$
   168^I[34mfunction[39;49;00m [32mCharIn[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; C: TCharSet): [36mBoolean[39;49;00m; overload;$
   169^I$
   170^I[34mfunction[39;49;00m [32mStrAtPos[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; [36mPos[39;49;00m: [36mInteger[39;49;00m; [34mconst[39;49;00m [36mStr[39;49;00m: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
   171^I[34mfunction[39;49;00m [32mStrAtBegin[39;49;00m([34mconst[39;49;00m S, [36mStr[39;49;00m: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
   172^I[34mfunction[39;49;00m [32mStrIn[39;49;00m([34mconst[39;49;00m S, SubStr: [34mstring[39;49;00m): [36mBoolean[39;49;00m; overload;$
   173^I[34mfunction[39;49;00m [32mStrIn[39;49;00m(A: TStrA; [34mconst[39;49;00m S: [34mstring[39;49;00m): [36mBoolean[39;49;00m; overload;$
   174^I[34mfunction[39;49;00m [32mStrIn[39;49;00m(SL: TStrings; [34mconst[39;49;00m S: [34mstring[39;49;00m): [36mBoolean[39;49;00m; overload;$
   175^I[34mfunction[39;49;00m [32mStrIndex[39;49;00m(A: TStrA; [34mconst[39;49;00m S: [34mstring[39;49;00m): [36mInteger[39;49;00m; overload;$
   176^I[34mfunction[39;49;00m [32mStrIndex[39;49;00m(SL: TStrings; [34mconst[39;49;00m S: [34mstring[39;49;00m): [36mInteger[39;49;00m; overload;$
   177^I$
   178^I[34mfunction[39;49;00m [32mTextAtPos[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; [36mPos[39;49;00m: [36mInteger[39;49;00m; [34mconst[39;49;00m Text: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
   179^I[34mfunction[39;49;00m [32mTextAtBegin[39;49;00m([34mconst[39;49;00m S, Text: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
   180^I[34mfunction[39;49;00m [32mTextIn[39;49;00m([34mconst[39;49;00m S, Text: [34mstring[39;49;00m): [36mBoolean[39;49;00m; overload;$
   181^I[34mfunction[39;49;00m [32mTextIn[39;49;00m(A: TStrA; [34mconst[39;49;00m Text: [34mstring[39;49;00m): [36mBoolean[39;49;00m; overload;$
   182^I[34mfunction[39;49;00m [32mTextIn[39;49;00m(SL: TStrings; [34mconst[39;49;00m Text: [34mstring[39;49;00m): [36mBoolean[39;49;00m; overload;$
   183^I[34mfunction[39;49;00m [32mTextIndex[39;49;00m(A: TStrA; [34mconst[39;49;00m Text: [34mstring[39;49;00m): [36mInteger[39;49;00m; overload;$
   184^I[34mfunction[39;49;00m [32mTextIndex[39;49;00m(SL: TStrings; [34mconst[39;49;00m Text: [34mstring[39;49;00m): [36mInteger[39;49;00m; overload;$
   185^I$
   186^I[37m{ Replace }[39;49;00m$
   187^I[34mfunction[39;49;00m [32mReplaceChars[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Old, [34mNew[39;49;00m: [36mChar[39;49;00m): [34mstring[39;49;00m; overload;$
   188^I[34mfunction[39;49;00m [32mReplaceChars[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Old: TCharSet; [34mNew[39;49;00m: [36mChar[39;49;00m): [34mstring[39;49;00m; overload;$
   189^I$
   190^I[34mfunction[39;49;00m [32mReplace[39;49;00m([34mconst[39;49;00m S, Old, [34mNew[39;49;00m: [34mstring[39;49;00m): [34mstring[39;49;00m;$
   191^I$
   192^I[37m{ TStrings }[39;49;00m$
   193^I[34mfunction[39;49;00m [32mSLOfFile[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m): TStringList;$
   194^I[34mfunction[39;49;00m [32mContainsEmptyLines[39;49;00m(SL: TStrings): [36mBoolean[39;49;00m;$
   195^I[34mprocedure[39;49;00m [32mDeleteEmptyLines[39;49;00m(SL: TStrings);$
   196^I[34mprocedure[39;49;00m [32mDeleteCommentLines[39;49;00m(SL: TStrings; [34mconst[39;49;00m CommentSign: [34mstring[39;49;00m = [33m'[39;49;00m[33m//[39;49;00m[33m'[39;49;00m);$
   197^I[34mprocedure[39;49;00m [32mWriteSL[39;49;00m(Strings: TStrings; [34mconst[39;49;00m Prefix: [34mstring[39;49;00m = [33m'[39;49;00m[33m'[39;49;00m;$
   198^I  [34mconst[39;49;00m Suffix: [34mstring[39;49;00m = [33m'[39;49;00m[33m'[39;49;00m);$
   199^I$
   200^I[34mfunction[39;49;00m [32mFindLine[39;49;00m(SL: TStrings; [34mconst[39;49;00m S: [34mstring[39;49;00m): [36mInteger[39;49;00m;$
   201^I$
   202^I[34mprocedure[39;49;00m [32mQuickSortSL[39;49;00m(SL: TStringList);$
   203^I$
   204^I[37m{ TStrA }[39;49;00m$
   205^I[34mfunction[39;49;00m [32mIncStrA[39;49;00m(StrA: TStrA): [36mInteger[39;49;00m;$
   206^I$
   207^I[37m{ TByteA }[39;49;00m$
   208^I[34mfunction[39;49;00m [32mStrOfByteA[39;49;00m(a: TByteA): [34mstring[39;49;00m;$
   209^I[34mfunction[39;49;00m [32mByteAOfStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): TByteA;$
   210^I[34mfunction[39;49;00m [32mByteAOfInt[39;49;00m(i: [36mInteger[39;49;00m): TByteA;$
   211^I[34mfunction[39;49;00m [32mIntOfByteA[39;49;00m(A: TByteA): [36mInteger[39;49;00m;$
   212^I[34mfunction[39;49;00m [32mByteAOfHex[39;49;00m([34mconst[39;49;00m Hex: [34mstring[39;49;00m): TByteA;$
   213^I$
   214^I[34mfunction[39;49;00m [32mSameByteA[39;49;00m([34mconst[39;49;00m A, B: TByteA): [36mBoolean[39;49;00m;$
   215^I[34mfunction[39;49;00m [32mReverse[39;49;00m(a: TByteA): TByteA;$
   216^I[34mfunction[39;49;00m [32mSaveByteA[39;49;00m(Data: TByteA; [34mconst[39;49;00m FileName: [34mstring[39;49;00m; Overwrite: [36mBoolean[39;49;00m = [34mTrue[39;49;00m): [36mBoolean[39;49;00m;$
   217^I[34mfunction[39;49;00m [32mLoadByteA[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m): TByteA;$
   218^I$
   219^I[34mfunction[39;49;00m [32mEndian[39;49;00m(i: [36mInteger[39;49;00m): [36mInteger[39;49;00m;$
   220^I$
   221^I[37m{ Files }[39;49;00m$
   222^I[34mfunction[39;49;00m [32mSizeOfFile[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m): [36mInteger[39;49;00m;$
   223^I[34mfunction[39;49;00m [32mFileEx[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m; AllowFolders: [36mBoolean[39;49;00m = [34mFalse[39;49;00m): [36mBoolean[39;49;00m;$
   224^I[34mfunction[39;49;00m [32mLWPSolve[39;49;00m([34mconst[39;49;00m Dir: [34mstring[39;49;00m): [34mstring[39;49;00m;$
   225^I[34mfunction[39;49;00m [32mLWPSlash[39;49;00m([34mconst[39;49;00m Dir: [34mstring[39;49;00m): [34mstring[39;49;00m;$
   226^I$
   227^I[34mfunction[39;49;00m [32mExtractDrive[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m): [34mstring[39;49;00m;$
   228^I[34mfunction[39;49;00m [32mExtractPath[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m): [34mstring[39;49;00m;$
   229^I[34mfunction[39;49;00m [32mExtractPrefix[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m): [34mstring[39;49;00m;$
   230^I[34mfunction[39;49;00m [32mExtractSuffix[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m): [34mstring[39;49;00m;$
   231^I$
   232^I[34mfunction[39;49;00m [32mIsValidFileName[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
   233^I[34mfunction[39;49;00m [32mMakeValidFileName[39;49;00m(FileName: [34mstring[39;49;00m; [34mconst[39;49;00m [34mDefault[39;49;00m: [34mstring[39;49;00m = [33m'[39;49;00m[33mFile[39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;$
   234^I$
   235^I[37m{ Converting }[39;49;00m$
   236^I[34mfunction[39;49;00m [32mIsValidInteger[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
   237^I[34mfunction[39;49;00m [32mIsValidCardinal[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
   238^I$
   239^I[34mfunction[39;49;00m [32mStrOfBool[39;49;00m(flag: [36mBoolean[39;49;00m; [34mconst[39;49;00m TrueStr: [34mstring[39;49;00m = [33m'[39;49;00m[33mTrue[39;49;00m[33m'[39;49;00m;$
   240^I  [34mconst[39;49;00m FalseStr: [34mstring[39;49;00m = [33m'[39;49;00m[33mFalse[39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;$
   241^I[34mfunction[39;49;00m [32mStrOfInt[39;49;00m(i: [36mInteger[39;49;00m): [34mstring[39;49;00m;$
   242^I[34mfunction[39;49;00m [32mCardOfStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [36mCardinal[39;49;00m;$
   243^I$
   244^I[34mfunction[39;49;00m [32mHexOrd[39;49;00m(Hex: [36mChar[39;49;00m): THex;$
   245^I[34mfunction[39;49;00m [32mByteOfHex[39;49;00m(Hex: THexByteStr): [36mByte[39;49;00m;$
   246^I$
   247^I[34mfunction[39;49;00m [32mDecOfHex[39;49;00m([34mconst[39;49;00m Hex: [34mstring[39;49;00m): [34mstring[39;49;00m;$
   248^I[34mfunction[39;49;00m [32mHexOfByte[39;49;00m(b: [36mByte[39;49;00m): THexByteStr;$
   249^I[34mfunction[39;49;00m [32mHexOfCard[39;49;00m(i: [36mCardinal[39;49;00m): [34mstring[39;49;00m; overload;$
   250^I[34mfunction[39;49;00m [32mHexOfCard[39;49;00m(i: [36mCardinal[39;49;00m; Digits: [36mInteger[39;49;00m): [34mstring[39;49;00m; overload;$
   251^I$
   252^I[34mfunction[39;49;00m [32mPascalHexArray[39;49;00m(a: TByteA; [34mName[39;49;00m: [34mstring[39;49;00m): [34mstring[39;49;00m;$
   253^I$
   254^I[34mfunction[39;49;00m [32mHexOfByteA[39;49;00m(a: TByteA; Blocks: [36mInteger[39;49;00m = [34m1[39;49;00m;$
   255^I  [34mconst[39;49;00m Splitter: [34mstring[39;49;00m = [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;$
   256^I[34mfunction[39;49;00m [32mBinOfByteA[39;49;00m(a: TByteA; Blocks: [36mInteger[39;49;00m = [34m4[39;49;00m;$
   257^I  [34mconst[39;49;00m Splitter: [34mstring[39;49;00m = [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;$
   258^I$
   259^I[34mfunction[39;49;00m [32mCardOfHex[39;49;00m(Hex: [34mstring[39;49;00m): [36mCardinal[39;49;00m;$
   260^I[34mfunction[39;49;00m [32mIntOfBin[39;49;00m(Bin: [34mstring[39;49;00m): [36mCardinal[39;49;00m;$
   261^I$
   262^I[34mfunction[39;49;00m [32mBinOfIntFill[39;49;00m(n: [36mcardinal[39;49;00m; MinCount: [36mInteger[39;49;00m = [34m8[39;49;00m): [34mstring[39;49;00m;$
   263^I[34mfunction[39;49;00m [32mBinOfInt[39;49;00m(n: [36mcardinal[39;49;00m): [34mstring[39;49;00m;$
   264^I$
   265^I[34mfunction[39;49;00m [32mBaseNOfInt[39;49;00m(I: [36mCardinal[39;49;00m; B: TBaseN): [34mstring[39;49;00m;$
   266^I[34mfunction[39;49;00m [32mIntOfBaseN[39;49;00m(V: [34mstring[39;49;00m; B: TBaseN): [36mCardinal[39;49;00m;$
   267^I$
   268^I[37m{ Ranges }[39;49;00m$
   269^I[34mfunction[39;49;00m [32mKeepIn[39;49;00m(i, Bottom, Top: [36mVariant[39;49;00m): [36mVariant[39;49;00m;$
   270^I[34mfunction[39;49;00m [32mInRange[39;49;00m(Value, Bottom, Top: [36mVariant[39;49;00m): [36mBoolean[39;49;00m;$
   271^I[34mfunction[39;49;00m [32mInStrictRange[39;49;00m(Value, Bottom, Top: [36mVariant[39;49;00m): [36mBoolean[39;49;00m;$
   272^I[34mfunction[39;49;00m [32mMin[39;49;00m([34mconst[39;49;00m A, B: [36mInteger[39;49;00m): [36mInteger[39;49;00m; overload;$
   273^I[34mfunction[39;49;00m [32mMin[39;49;00m([34mconst[39;49;00m A: TIntA): [36mInteger[39;49;00m; overload;$
   274^I[34mfunction[39;49;00m [32mMax[39;49;00m([34mconst[39;49;00m A, B: [36mInteger[39;49;00m): [36mInteger[39;49;00m; overload;$
   275^I[34mfunction[39;49;00m [32mMax[39;49;00m([34mconst[39;49;00m A: TIntA): [36mInteger[39;49;00m; overload;$
   276^I$
   277^I[34mconst[39;49;00m$
   278^I  RangesSeparator = [33m'[39;49;00m[33m,[39;49;00m[33m'[39;49;00m;$
   279^I  RangeInnerSeparator = [33m'[39;49;00m[33m-[39;49;00m[33m'[39;49;00m;$
   280^I  RangeInfinite = [33m'[39;49;00m[33m*[39;49;00m[33m'[39;49;00m;$
   281^I  RangeSpecialChars = [RangesSeparator, RangeInnerSeparator, RangeInfinite];$
   282^I$
   283^I[34mfunction[39;49;00m [32mRangesOfStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): TRanges;$
   284^I[34mfunction[39;49;00m [32mInRanges[39;49;00m(Ranges: TRanges; TestValue: [36mCardinal[39;49;00m): [36mBoolean[39;49;00m;$
   285^I$
   286^I[34mfunction[39;49;00m [32mSuccess[39;49;00m(Res: [36mInteger[39;49;00m; ResultOnSuccess: [36mInteger[39;49;00m = ERROR_SUCCESS): [36mBoolean[39;49;00m;$
   287^I[34mfunction[39;49;00m [32mFailure[39;49;00m(Res: [36mInteger[39;49;00m; ResultOnSuccess: [36mInteger[39;49;00m = ERROR_SUCCESS): [36mBoolean[39;49;00m;$
   288^I$
   289^I[34mfunction[39;49;00m [32mExpandString[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [34mstring[39;49;00m;$
   290^I$
   291^I[37m{ Files }[39;49;00m$
   292^I[34mprocedure[39;49;00m [32mDeleteFiles[39;49;00m([34mconst[39;49;00m Mask: [34mstring[39;49;00m; ScanSubDirs: [36mBoolean[39;49;00m = [34mTrue[39;49;00m;$
   293^I  Attributes: [36mInteger[39;49;00m = faFindEveryFile);$
   294^I[34mprocedure[39;49;00m [32mFileNew[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m);$
   295^I[34mfunction[39;49;00m [32mDateTimeOfFileTime[39;49;00m([34mconst[39;49;00m FileTime: TFileTime): [36mTDateTime[39;49;00m;$
   296^I$
   297^I[37m{ FileNames }[39;49;00m$
   298^I[34mfunction[39;49;00m [32mGetFileNew[39;49;00m(FileName: [34mstring[39;49;00m; NoFloppyDrives: [36mBoolean[39;49;00m = [34mTrue[39;49;00m): [34mstring[39;49;00m;$
   299^I$
   300^I[37m{ Finding Files }[39;49;00m$
   301^I[34mfunction[39;49;00m [32mFindAll[39;49;00m(Strings: TStrings; [34mconst[39;49;00m Mask: [34mstring[39;49;00m;$
   302^I  ScanSubDirs: [36mBoolean[39;49;00m = [34mTrue[39;49;00m; Attributes: [36mInteger[39;49;00m = faFindEveryFile;$
   303^I  FileReturn: TFileNameFunc = [34mnil[39;49;00m): [36mBoolean[39;49;00m;$
   304^I[34mfunction[39;49;00m [32mFindAllFirst[39;49;00m([34mconst[39;49;00m Mask: [34mstring[39;49;00m; ScanSubDirs: [36mBoolean[39;49;00m = [34mTrue[39;49;00m;$
   305^I  Attributes: [36mInteger[39;49;00m = faFindEveryFile): [34mstring[39;49;00m;$
   306^I$
   307^I[34mfunction[39;49;00m [32mFullOSInfo[39;49;00m: [34mstring[39;49;00m;$
   308^I[34mfunction[39;49;00m [32mWin32PlatformStr[39;49;00m: [34mstring[39;49;00m;$
   309^I[34mfunction[39;49;00m [32mWin9x[39;49;00m: [36mBoolean[39;49;00m;$
   310^I[34mfunction[39;49;00m [32mWinNT[39;49;00m: [36mBoolean[39;49;00m;$
   311^I[34mfunction[39;49;00m [32mWin2000[39;49;00m: [36mBoolean[39;49;00m;$
   312^I[34mfunction[39;49;00m [32mWinXP[39;49;00m: [36mBoolean[39;49;00m;$
   313^I$
   314^I[34mvar[39;49;00m$
   315^I  MyDir: [34mstring[39;49;00m = [33m'[39;49;00m[33m'[39;49;00m;$
   316^I  LastSuccessRes: [36mInteger[39;49;00m = [34m0[39;49;00m;$
   317^I  $
   318^I[37m{ Backward compatibility }[39;49;00m$
   319^I[37m{$IFNDEF VER130}[39;49;00m$
   320^I[34mfunction[39;49;00m [32mSameText[39;49;00m([34mconst[39;49;00m S1, S2: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
   321^I[37m{$ENDIF}[39;49;00m$
   322^I$
   323^I[34mimplementation[39;49;00m$
   324^I[37m{$IFNDEF VER140}[39;49;00m$
   325^I[34muses[39;49;00m FileCtrl;$
   326^I[37m{$ENDIF}[39;49;00m$
   327^I$
   328^I[37m{$IFNDEF VER130}[39;49;00m$
   329^I[34mfunction[39;49;00m [32mSameText[39;49;00m([34mconst[39;49;00m S1, S2: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
   330^I[34mbegin[39;49;00m$
   331^I  [36mResult[39;49;00m := [36mCompareText[39;49;00m(S1, S2) = [34m0[39;49;00m;$
   332^I[34mend[39;49;00m;$
   333^I[37m{$ENDIF}[39;49;00m$
   334^I$
   335^I[34mprocedure[39;49;00m [32mReport[39;49;00m([34mconst[39;49;00m ReportName, Text: [34mstring[39;49;00m);$
   336^I[34mvar[39;49;00m$
   337^I  F: [36mTextFile[39;49;00m;$
   338^I  FileName: [34mstring[39;49;00m;$
   339^I[34mbegin[39;49;00m$
   340^I  FileName := MyDir + ReportName + [33m'[39;49;00m[33m.rep[39;49;00m[33m'[39;49;00m;$
   341^I  Assign(F, FileName);$
   342^I  [34mtry[39;49;00m$
   343^I    [34mif[39;49;00m [34mnot[39;49;00m [36mFileExists[39;49;00m(FileName) [34mthen[39;49;00m$
   344^I      [36mRewrite[39;49;00m(F)$
   345^I    [34melse[39;49;00m$
   346^I      [36mAppend[39;49;00m(F);$
   347^I    [36mWriteLn[39;49;00m(F, Text);$
   348^I  [34mfinally[39;49;00m$
   349^I    [36mClose[39;49;00m(F);$
   350^I  [34mend[39;49;00m;$
   351^I[34mend[39;49;00m;$
   352^I$
   353^I[34mprocedure[39;49;00m [32mClearReport[39;49;00m([34mconst[39;49;00m ReportName: [34mstring[39;49;00m);$
   354^I[34mvar[39;49;00m$
   355^I  FileName: [34mstring[39;49;00m;$
   356^I[34mbegin[39;49;00m$
   357^I  FileName := MyDir + ReportName + [33m'[39;49;00m[33m.rep[39;49;00m[33m'[39;49;00m;$
   358^I  [36mDeleteFile[39;49;00m(FileName);$
   359^I[34mend[39;49;00m;$
   360^I$
   361^I[34mprocedure[39;49;00m [32mReportFmt[39;49;00m([34mconst[39;49;00m ReportName, Fmt: [34mstring[39;49;00m; [34mconst[39;49;00m Args: [34marray[39;49;00m [34mof[39;49;00m [34mconst[39;49;00m);$
   362^I[34mbegin[39;49;00m$
   363^I  Report(ReportName, [36mFormat[39;49;00m(Fmt, Args));$
   364^I[34mend[39;49;00m;$
   365^I$
   366^I[34mprocedure[39;49;00m [32mGetParams[39;49;00m(Strings: TStrings);$
   367^I[34mvar[39;49;00m$
   368^I  P: [36mPChar[39;49;00m;$
   369^I  Param: [34mstring[39;49;00m;$
   370^I$
   371^I  [34mfunction[39;49;00m [32mGetParamStr[39;49;00m([34mvar[39;49;00m P: [36mPChar[39;49;00m; [34mvar[39;49;00m Param: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
   372^I  [34mvar[39;49;00m$
   373^I    Quoted: [36mBoolean[39;49;00m;$
   374^I  [34mbegin[39;49;00m$
   375^I    Param := [33m'[39;49;00m[33m'[39;49;00m;$
   376^I$
   377^I    [34mrepeat[39;49;00m$
   378^I      [34mwhile[39;49;00m (P[[34m0[39;49;00m] <> [33m#0[39;49;00m) [34mand[39;49;00m (P[[34m0[39;49;00m] <= [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m) [34mdo[39;49;00m$
   379^I        [36mInc[39;49;00m(P);$
   380^I$
   381^I      Quoted := [34mFalse[39;49;00m;$
   382^I      [34mwhile[39;49;00m P[[34m0[39;49;00m] <> [33m#0[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m$
   383^I        [34mif[39;49;00m P[[34m0[39;49;00m] = [33m'[39;49;00m[33m"[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m$
   384^I          Quoted := [34mnot[39;49;00m Quoted;$
   385^I          [36mInc[39;49;00m(P);$
   386^I        [34mContinue[39;49;00m; [34mend[39;49;00m;$
   387^I        [34mif[39;49;00m (P[[34m0[39;49;00m] <= [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m) [34mand[39;49;00m [34mnot[39;49;00m Quoted [34mthen[39;49;00m$
   388^I          [34mBreak[39;49;00m;$
   389^I        Param := Param + P[[34m0[39;49;00m];$
   390^I        [36mInc[39;49;00m(P);$
   391^I      [34mend[39;49;00m;$
   392^I    [34muntil[39;49;00m (Param <> [33m'[39;49;00m[33m'[39;49;00m) [34mor[39;49;00m (P[[34m0[39;49;00m] = [33m#0[39;49;00m);$
   393^I$
   394^I    [36mResult[39;49;00m := Param <> [33m'[39;49;00m[33m'[39;49;00m;$
   395^I  [34mend[39;49;00m;$
   396^I$
   397^I[34mbegin[39;49;00m$
   398^I  Strings.Clear;$
   399^I  P := GetCommandLine;$
   400^I  GetParamStr(P, Param);$
   401^I  [34mwhile[39;49;00m GetParamStr(P, Param) [34mdo[39;49;00m$
   402^I    Strings.Add(Param);$
   403^I[34mend[39;49;00m;$
   404^I$
   405^I[34mfunction[39;49;00m [32mGetParams[39;49;00m([34mconst[39;49;00m Separator: [34mstring[39;49;00m = [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;$
   406^I[34mvar[39;49;00m$
   407^I  SL: TStringList;$
   408^I[34mbegin[39;49;00m$
   409^I  SL := TStringList.Create;$
   410^I  GetParams(SL);$
   411^I  [36mResult[39;49;00m := Join(SL, Separator);$
   412^I  SL.Free;$
   413^I[34mend[39;49;00m;$
   414^I$
   415^I[34mfunction[39;49;00m [32mSwitch[39;49;00m([34mconst[39;49;00m Switch: [34mstring[39;49;00m; [34mconst[39;49;00m PrefixChars: TCharSet = SwitchChars;$
   416^I  IgnoreCase: [36mBoolean[39;49;00m = [34mTrue[39;49;00m): [36mBoolean[39;49;00m;$
   417^I[37m//= SysUtils.FindCmdLineSwitch[39;49;00m$
   418^I[34mvar[39;49;00m$
   419^I  i: [36mInteger[39;49;00m;$
   420^I  s: [34mstring[39;49;00m;$
   421^I[34mbegin[39;49;00m$
   422^I  [36mResult[39;49;00m := [34mTrue[39;49;00m;$
   423^I$
   424^I  [34mfor[39;49;00m i := [34m1[39;49;00m [34mto[39;49;00m [36mParamCount[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m$
   425^I    s := [36mParamStr[39;49;00m(i);$
   426^I$
   427^I    [34mif[39;49;00m (s <> [33m'[39;49;00m[33m'[39;49;00m) [34mand[39;49;00m (s[[34m1[39;49;00m] [34min[39;49;00m PrefixChars) [34mthen[39;49;00m [34mbegin[39;49;00m$
   428^I    [37m//i know that always s <> '', but this is saver[39;49;00m$
   429^I      s := [36mCopy[39;49;00m(s, [34m2[39;49;00m, MaxInt);$
   430^I      [34mif[39;49;00m (s = Switch) [34mor[39;49;00m (IgnoreCase [34mand[39;49;00m ([34m0[39;49;00m=[36mAnsiCompareText[39;49;00m(s, Switch))) [34mthen[39;49;00m$
   431^I        [34mExit[39;49;00m;$
   432^I    [34mend[39;49;00m;$
   433^I  [34mend[39;49;00m;$
   434^I$
   435^I  [36mResult[39;49;00m := [34mFalse[39;49;00m;$
   436^I[34mend[39;49;00m;$
   437^I$
   438^I[34mfunction[39;49;00m [32mParamNum[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [36mInteger[39;49;00m;$
   439^I[34mbegin[39;49;00m$
   440^I  [34mfor[39;49;00m [36mResult[39;49;00m := [34m1[39;49;00m [34mto[39;49;00m [36mParamCount[39;49;00m [34mdo[39;49;00m$
   441^I    [34mif[39;49;00m [34m0[39;49;00m=[36mAnsiCompareText[39;49;00m([36mParamStr[39;49;00m([36mResult[39;49;00m), S) [34mthen[39;49;00m$
   442^I      [34mExit[39;49;00m;$
   443^I$
   444^I  [36mResult[39;49;00m := [34m0[39;49;00m;$
   445^I[34mend[39;49;00m;$
   446^I$
   447^I[34mfunction[39;49;00m [32mParamPrefixNum[39;49;00m([34mconst[39;49;00m Prefix: [34mstring[39;49;00m): [36mInteger[39;49;00m;$
   448^I[34mvar[39;49;00m$
   449^I  Len: [36mInteger[39;49;00m;$
   450^I[34mbegin[39;49;00m$
   451^I  Len := [36mLength[39;49;00m(Prefix);$
   452^I  [34mfor[39;49;00m [36mResult[39;49;00m := [34m1[39;49;00m [34mto[39;49;00m [36mParamCount[39;49;00m [34mdo[39;49;00m$
   453^I    [34mif[39;49;00m [34m0[39;49;00m=[36mAnsiCompareText[39;49;00m([36mCopy[39;49;00m([36mParamStr[39;49;00m([36mResult[39;49;00m), [34m1[39;49;00m, Len), Prefix) [34mthen[39;49;00m$
   454^I      [34mExit[39;49;00m;$
   455^I$
   456^I  [36mResult[39;49;00m := [34m0[39;49;00m;$
   457^I[34mend[39;49;00m;$
   458^I$
   459^I[34mfunction[39;49;00m [32mParam[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
   460^I[34mbegin[39;49;00m$
   461^I  [36mResult[39;49;00m := ParamNum(S) > [34m0[39;49;00m;$
   462^I[34mend[39;49;00m;$
   463^I$
   464^I[34mfunction[39;49;00m [32mParamPrefix[39;49;00m([34mconst[39;49;00m Prefix: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
   465^I[34mbegin[39;49;00m$
   466^I  [36mResult[39;49;00m := ParamPrefixNum(Prefix) > [34m0[39;49;00m;$
   467^I[34mend[39;49;00m;$
   468^I$
   469^I[34mfunction[39;49;00m [32mGetParam[39;49;00m([34mconst[39;49;00m Prefix: [34mstring[39;49;00m = [33m'[39;49;00m[33m'[39;49;00m; [34mconst[39;49;00m [34mDefault[39;49;00m: [34mstring[39;49;00m = [33m'[39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;$
   470^I[34mvar[39;49;00m$
   471^I  i: [36mInteger[39;49;00m;$
   472^I[34mbegin[39;49;00m$
   473^I  [36mResult[39;49;00m := [34mDefault[39;49;00m;$
   474^I$
   475^I  [34mif[39;49;00m Prefix = [33m'[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m$
   476^I    [36mResult[39;49;00m := [36mParamStr[39;49;00m([34m1[39;49;00m);$
   477^I  [34mExit[39;49;00m; [34mend[39;49;00m;$
   478^I$
   479^I  i := ParamPrefixNum(Prefix);$
   480^I  [34mif[39;49;00m i > [34m0[39;49;00m [34mthen[39;49;00m$
   481^I    [36mResult[39;49;00m := [36mCopy[39;49;00m([36mParamStr[39;49;00m(i), [36mLength[39;49;00m(Prefix) + [34m1[39;49;00m, MaxInt);$
   482^I[34mend[39;49;00m;$
   483^I$
   484^I[34mfunction[39;49;00m [32mGetMyDir[39;49;00m(FullPath: [36mBoolean[39;49;00m = [34mFalse[39;49;00m): [34mstring[39;49;00m;$
   485^I[34mvar[39;49;00m$
   486^I  Buffer: [34marray[39;49;00m[[34m0[39;49;00m..[34m260[39;49;00m] [34mof[39;49;00m [36mChar[39;49;00m;$
   487^I[34mbegin[39;49;00m$
   488^I  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
   489^I  [36mSetString[39;49;00m([36mResult[39;49;00m, Buffer, [36mGetModuleFileName[39;49;00m([34m0[39;49;00m, Buffer, [36mSizeOf[39;49;00m(Buffer)));$
   490^I  [34mif[39;49;00m FullPath [34mthen[39;49;00m$
   491^I    [36mResult[39;49;00m := GetFileNew([36mResult[39;49;00m);$
   492^I  [36mResult[39;49;00m := ExtractPath([36mResult[39;49;00m);$
   493^I[34mend[39;49;00m;$
   494^I$
   495^I[34mfunction[39;49;00m [32mWinDir[39;49;00m: [34mstring[39;49;00m;$
   496^I[34mvar[39;49;00m$
   497^I  Res: [36mPChar[39;49;00m;$
   498^I[34mbegin[39;49;00m$
   499^I  [36mResult[39;49;00m := [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m;$
   500^I  [36mGetMem[39;49;00m(Res, MAX_PATH);$
   501^I  GetWindowsDirectory(Res, MAX_PATH);$
   502^I  [36mResult[39;49;00m := Res + [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m;$
   503^I  [36mFreeMem[39;49;00m(Res, MAX_PATH);$
   504^I[34mend[39;49;00m;$
   505^I$
   506^I[34mfunction[39;49;00m [32mSysDir[39;49;00m: [34mstring[39;49;00m;$
   507^I[34mvar[39;49;00m$
   508^I  Res: [36mPChar[39;49;00m;$
   509^I[34mbegin[39;49;00m$
   510^I  [36mResult[39;49;00m := [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m;$
   511^I  [36mGetMem[39;49;00m(Res, MAX_PATH);$
   512^I  GetSystemDirectory(Res, MAX_PATH);$
   513^I  [36mResult[39;49;00m := Res + [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m;$
   514^I  [36mFreeMem[39;49;00m(Res, MAX_PATH);$
   515^I[34mend[39;49;00m;$
   516^I$
   517^I[34mfunction[39;49;00m [32mUserName[39;49;00m: [34mstring[39;49;00m;$
   518^I[34mvar[39;49;00m$
   519^I  Len: [36mCardinal[39;49;00m;$
   520^I  Res: [36mPChar[39;49;00m;$
   521^I[34mbegin[39;49;00m$
   522^I  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
   523^I  [36mGetMem[39;49;00m(Res, MAX_PATH);$
   524^I  Len := MAX_PATH;$
   525^I  GetUserName(Res, Len);$
   526^I  [36mResult[39;49;00m := Res;$
   527^I  [36mFreeMem[39;49;00m(Res, MAX_PATH);$
   528^I[34mend[39;49;00m;$
   529^I$
   530^I[34mfunction[39;49;00m [32mFirstChar[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [36mChar[39;49;00m;$
   531^I[34mbegin[39;49;00m$
   532^I  [34mif[39;49;00m s = [33m'[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m$
   533^I    [36mResult[39;49;00m := [33m#0[39;49;00m$
   534^I  [34melse[39;49;00m$
   535^I    [36mResult[39;49;00m := s[[34m1[39;49;00m];$
   536^I[34mend[39;49;00m;$
   537^I$
   538^I[34mfunction[39;49;00m [32mLastChar[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [36mChar[39;49;00m;$
   539^I[34mbegin[39;49;00m$
   540^I  [34mif[39;49;00m s = [33m'[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m$
   541^I    [36mResult[39;49;00m := [33m#0[39;49;00m$
   542^I  [34melse[39;49;00m$
   543^I    [36mResult[39;49;00m := s[[36mLength[39;49;00m(s)];$
   544^I[34mend[39;49;00m;$
   545^I$
   546^I[34mfunction[39;49;00m [32mCharPos[39;49;00m(C: [36mChar[39;49;00m; [34mconst[39;49;00m S: [34mstring[39;49;00m; Offset: [36mInteger[39;49;00m = [34m1[39;49;00m): [36mInteger[39;49;00m;$
   547^I[34mvar[39;49;00m$
   548^I  MaxPosToSearch: [36mInteger[39;49;00m;$
   549^I[34mbegin[39;49;00m$
   550^I  [36mResult[39;49;00m := Offset;$
   551^I  MaxPosToSearch := [36mLength[39;49;00m(S);$
   552^I$
   553^I  [34mwhile[39;49;00m [36mResult[39;49;00m <= MaxPosToSearch [34mdo[39;49;00m [34mbegin[39;49;00m$
   554^I    [34mif[39;49;00m S[[36mResult[39;49;00m] = C [34mthen[39;49;00m$
   555^I      [34mExit[39;49;00m;$
   556^I    [36mInc[39;49;00m([36mResult[39;49;00m);$
   557^I  [34mend[39;49;00m;$
   558^I$
   559^I  [36mResult[39;49;00m := [34m0[39;49;00m;$
   560^I[34mend[39;49;00m;$
   561^I$
   562^I[34mfunction[39;49;00m [32mCharPos[39;49;00m(C: TCharSet; [34mconst[39;49;00m S: [34mstring[39;49;00m; Offset: [36mInteger[39;49;00m = [34m1[39;49;00m): [36mInteger[39;49;00m;$
   563^I[34mvar[39;49;00m$
   564^I  MaxPosToSearch: [36mInteger[39;49;00m;$
   565^I[34mbegin[39;49;00m$
   566^I  [36mResult[39;49;00m := Offset;$
   567^I  MaxPosToSearch := [36mLength[39;49;00m(S);$
   568^I$
   569^I  [34mwhile[39;49;00m [36mResult[39;49;00m <= MaxPosToSearch [34mdo[39;49;00m [34mbegin[39;49;00m$
   570^I    [34mif[39;49;00m S[[36mResult[39;49;00m] [34min[39;49;00m C [34mthen[39;49;00m$
   571^I      [34mExit[39;49;00m;$
   572^I    [36mInc[39;49;00m([36mResult[39;49;00m);$
   573^I  [34mend[39;49;00m;$
   574^I$
   575^I  [36mResult[39;49;00m := [34m0[39;49;00m;$
   576^I[34mend[39;49;00m;$
   577^I$
   578^I[34mfunction[39;49;00m [32mCharPosR[39;49;00m(C: [36mChar[39;49;00m; [34mconst[39;49;00m S: [34mstring[39;49;00m; Offset: [36mInteger[39;49;00m = -[34m1[39;49;00m): [36mInteger[39;49;00m;$
   579^I[34mbegin[39;49;00m$
   580^I  [34mif[39;49;00m Offset < [34m0[39;49;00m [34mthen[39;49;00m$
   581^I    [36mResult[39;49;00m := [36mLength[39;49;00m(S) + [34m1[39;49;00m - Offset$
   582^I  [34melse[39;49;00m$
   583^I    [36mResult[39;49;00m := Offset;$
   584^I  [34mif[39;49;00m [36mResult[39;49;00m > [36mLength[39;49;00m(S) [34mthen[39;49;00m$
   585^I    [36mResult[39;49;00m := [36mLength[39;49;00m(S);$
   586^I$
   587^I  [34mwhile[39;49;00m [36mResult[39;49;00m > [34m0[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m$
   588^I    [34mif[39;49;00m S[[36mResult[39;49;00m] = C [34mthen[39;49;00m$
   589^I      [34mExit[39;49;00m;$
   590^I    [36mDec[39;49;00m([36mResult[39;49;00m);$
   591^I  [34mend[39;49;00m;$
   592^I[34mend[39;49;00m;$
   593^I$
   594^I[34mfunction[39;49;00m [32mPosEx[39;49;00m([34mconst[39;49;00m SubStr, S: [34mstring[39;49;00m; Offset: [36mInteger[39;49;00m = [34m1[39;49;00m): [36mInteger[39;49;00m;$
   595^I[34mvar[39;49;00m$
   596^I  MaxPosToSearch, LenSubStr, i: [36mInteger[39;49;00m;$
   597^I[34mbegin[39;49;00m$
   598^I  [34mif[39;49;00m SubStr = [33m'[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m$
   599^I    [36mResult[39;49;00m := [34m0[39;49;00m;$
   600^I  [34mExit[39;49;00m; [34mend[39;49;00m;$
   601^I$
   602^I  [34mif[39;49;00m Offset < [34m1[39;49;00m [34mthen[39;49;00m$
   603^I    [36mResult[39;49;00m := [34m1[39;49;00m$
   604^I  [34melse[39;49;00m$
   605^I    [36mResult[39;49;00m := Offset;$
   606^I$
   607^I  LenSubStr := [36mLength[39;49;00m(SubStr);$
   608^I  MaxPosToSearch := [36mLength[39;49;00m(S) - LenSubStr + [34m1[39;49;00m;$
   609^I$
   610^I  [34mwhile[39;49;00m [36mResult[39;49;00m <= MaxPosToSearch [34mdo[39;49;00m [34mbegin[39;49;00m$
   611^I    [34mif[39;49;00m S[[36mResult[39;49;00m] = SubStr[[34m1[39;49;00m] [34mthen[39;49;00m [34mbegin[39;49;00m$
   612^I      i := [34m1[39;49;00m;$
   613^I$
   614^I      [34mwhile[39;49;00m (i < LenSubStr)$
   615^I       [34mand[39;49;00m (S[[36mResult[39;49;00m + i] = SubStr[i + [34m1[39;49;00m]) [34mdo[39;49;00m$
   616^I        [36mInc[39;49;00m(i);$
   617^I$
   618^I      [34mif[39;49;00m i = LenSubStr [34mthen[39;49;00m$
   619^I        [34mExit[39;49;00m;$
   620^I    [34mend[39;49;00m;$
   621^I    [36mInc[39;49;00m([36mResult[39;49;00m);$
   622^I  [34mend[39;49;00m;$
   623^I$
   624^I  [36mResult[39;49;00m := [34m0[39;49;00m;$
   625^I[34mend[39;49;00m;$
   626^I$
   627^I[34mfunction[39;49;00m [32mPosExText[39;49;00m([34mconst[39;49;00m SubStr, S: [34mstring[39;49;00m; Offset: [36mInteger[39;49;00m = [34m1[39;49;00m): [36mInteger[39;49;00m;$
   628^I[34mvar[39;49;00m$
   629^I  MaxPosToSearch, LenSubStr, i: [36mInteger[39;49;00m;$
   630^I$
   631^I  [34mfunction[39;49;00m [32mSameChar[39;49;00m(a, b: [36mChar[39;49;00m): [36mBoolean[39;49;00m;$
   632^I  [34mbegin[39;49;00m$
   633^I    [36mResult[39;49;00m := [36mUpCase[39;49;00m(a) = [36mUpCase[39;49;00m(b)$
   634^I  [34mend[39;49;00m;$
   635^I$
   636^I[34mbegin[39;49;00m$
   637^I  [34mif[39;49;00m SubStr = [33m'[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m$
   638^I    [36mResult[39;49;00m := [34m0[39;49;00m;$
   639^I  [34mExit[39;49;00m; [34mend[39;49;00m;$
   640^I$
   641^I  [34mif[39;49;00m Offset < [34m1[39;49;00m [34mthen[39;49;00m$
   642^I    [36mResult[39;49;00m := [34m1[39;49;00m$
   643^I  [34melse[39;49;00m$
   644^I    [36mResult[39;49;00m := Offset;$
   645^I$
   646^I  LenSubStr := [36mLength[39;49;00m(SubStr);$
   647^I  MaxPosToSearch := [36mLength[39;49;00m(S) - LenSubStr + [34m1[39;49;00m;$
   648^I$
   649^I  [34mwhile[39;49;00m [36mResult[39;49;00m <= MaxPosToSearch [34mdo[39;49;00m [34mbegin[39;49;00m$
   650^I    [34mif[39;49;00m SameChar(S[[36mResult[39;49;00m], SubStr[[34m1[39;49;00m]) [34mthen[39;49;00m [34mbegin[39;49;00m$
   651^I      i := [34m1[39;49;00m;$
   652^I$
   653^I      [34mwhile[39;49;00m (i < LenSubStr)$
   654^I       [34mand[39;49;00m (SameChar(S[[36mResult[39;49;00m + i], SubStr[i + [34m1[39;49;00m])) [34mdo[39;49;00m$
   655^I        [36mInc[39;49;00m(i);$
   656^I$
   657^I      [34mif[39;49;00m i = LenSubStr [34mthen[39;49;00m$
   658^I        [34mExit[39;49;00m;$
   659^I    [34mend[39;49;00m;$
   660^I    [36mInc[39;49;00m([36mResult[39;49;00m);$
   661^I  [34mend[39;49;00m;$
   662^I$
   663^I  [36mResult[39;49;00m := [34m0[39;49;00m;$
   664^I[34mend[39;49;00m;$
   665^I$
   666^I[34mfunction[39;49;00m [32mPosExAnsiText[39;49;00m([34mconst[39;49;00m SubStr, S: [34mstring[39;49;00m; Offset: [36mInteger[39;49;00m = [34m1[39;49;00m): [36mInteger[39;49;00m;$
   667^I[34mvar[39;49;00m$
   668^I  MaxPosToSearch, LenSubStr, i: [36mInteger[39;49;00m;$
   669^I$
   670^I  [34mfunction[39;49;00m [32mSameChar[39;49;00m(a, b: [36mChar[39;49;00m): [36mBoolean[39;49;00m;$
   671^I  [34mbegin[39;49;00m$
   672^I    [36mResult[39;49;00m := CharLower([36mPChar[39;49;00m(a)) = CharLower([36mPChar[39;49;00m(b));$
   673^I  [34mend[39;49;00m;$
   674^I$
   675^I[34mbegin[39;49;00m$
   676^I  [34mif[39;49;00m SubStr = [33m'[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m$
   677^I    [36mResult[39;49;00m := [34m0[39;49;00m;$
   678^I  [34mExit[39;49;00m; [34mend[39;49;00m;$
   679^I$
   680^I  [34mif[39;49;00m Offset < [34m1[39;49;00m [34mthen[39;49;00m$
   681^I    [36mResult[39;49;00m := [34m1[39;49;00m$
   682^I  [34melse[39;49;00m$
   683^I    [36mResult[39;49;00m := Offset;$
   684^I$
   685^I  LenSubStr := [36mLength[39;49;00m(SubStr);$
   686^I  MaxPosToSearch := [36mLength[39;49;00m(S) - LenSubStr + [34m1[39;49;00m;$
   687^I$
   688^I  [34mwhile[39;49;00m [36mResult[39;49;00m <= MaxPosToSearch [34mdo[39;49;00m [34mbegin[39;49;00m$
   689^I    [34mif[39;49;00m SameChar(S[[36mResult[39;49;00m], SubStr[[34m1[39;49;00m]) [34mthen[39;49;00m [34mbegin[39;49;00m$
   690^I      i := [34m1[39;49;00m;$
   691^I$
   692^I      [34mwhile[39;49;00m (i < LenSubStr)$
   693^I       [34mand[39;49;00m (SameChar(S[[36mResult[39;49;00m + i], SubStr[i + [34m1[39;49;00m])) [34mdo[39;49;00m$
   694^I        [36mInc[39;49;00m(i);$
   695^I$
   696^I      [34mif[39;49;00m i = LenSubStr [34mthen[39;49;00m$
   697^I        [34mExit[39;49;00m;$
   698^I    [34mend[39;49;00m;$
   699^I    [36mInc[39;49;00m([36mResult[39;49;00m);$
   700^I  [34mend[39;49;00m;$
   701^I$
   702^I  [36mResult[39;49;00m := [34m0[39;49;00m;$
   703^I[34mend[39;49;00m;$
   704^I$
   705^I[34mfunction[39;49;00m [32mUntilChar[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Brake: [36mChar[39;49;00m): [34mstring[39;49;00m;$
   706^I[34mvar[39;49;00m$
   707^I  p: [36mInteger[39;49;00m;$
   708^I[34mbegin[39;49;00m$
   709^I  p := CharPos(Brake, S);$
   710^I$
   711^I  [34mif[39;49;00m p > [34m0[39;49;00m [34mthen[39;49;00m$
   712^I    [36mResult[39;49;00m := [36mCopy[39;49;00m(S, [34m1[39;49;00m, p - [34m1[39;49;00m)$
   713^I  [34melse[39;49;00m$
   714^I    [36mResult[39;49;00m := S;$
   715^I[34mend[39;49;00m;$
   716^I$
   717^I[34mfunction[39;49;00m [32mUntilChar[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Brake: TCharSet): [34mstring[39;49;00m;$
   718^I[34mvar[39;49;00m$
   719^I  p: [36mInteger[39;49;00m;$
   720^I[34mbegin[39;49;00m$
   721^I  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
   722^I  p := CharPos(Brake, S);$
   723^I$
   724^I  [34mif[39;49;00m p > [34m0[39;49;00m [34mthen[39;49;00m$
   725^I    [36mResult[39;49;00m := [36mCopy[39;49;00m(S, [34m1[39;49;00m, p - [34m1[39;49;00m)$
   726^I  [34melse[39;49;00m$
   727^I    [36mResult[39;49;00m := S;$
   728^I[34mend[39;49;00m;$
   729^I$
   730^I[34mfunction[39;49;00m [32mUntilLastChar[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Brake: [36mChar[39;49;00m;$
   731^I  IgnoreNoBrake: [36mBoolean[39;49;00m = [34mTrue[39;49;00m): [34mstring[39;49;00m;$
   732^I[34mvar[39;49;00m$
   733^I  p: [36mInteger[39;49;00m;$
   734^I[34mbegin[39;49;00m$
   735^I  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
   736^I  p := CharPosR(Brake, S);$
   737^I$
   738^I  [34mif[39;49;00m p > [34m0[39;49;00m [34mthen[39;49;00m$
   739^I    [36mResult[39;49;00m := [36mCopy[39;49;00m(S, [34m1[39;49;00m, p - [34m1[39;49;00m)$
   740^I  [34melse[39;49;00m [34mif[39;49;00m IgnoreNoBrake [34mthen[39;49;00m$
   741^I    [36mResult[39;49;00m := S;$
   742^I[34mend[39;49;00m;$
   743^I$
   744^I[34mfunction[39;49;00m [32mFromChar[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Brake: [36mChar[39;49;00m): [34mstring[39;49;00m;$
   745^I[34mvar[39;49;00m$
   746^I  p: [36mInteger[39;49;00m;$
   747^I[34mbegin[39;49;00m$
   748^I  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
   749^I  p := CharPos(Brake, S);$
   750^I$
   751^I  [34mif[39;49;00m p > [34m0[39;49;00m [34mthen[39;49;00m$
   752^I    [36mResult[39;49;00m := [36mCopy[39;49;00m(S, p + [34m1[39;49;00m, [36mLength[39;49;00m(S) - p);$
   753^I[34mend[39;49;00m;$
   754^I$
   755^I[34mfunction[39;49;00m [32mFromChar[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Brake: TCharSet): [34mstring[39;49;00m;$
   756^I[34mvar[39;49;00m$
   757^I  p: [36mInteger[39;49;00m;$
   758^I[34mbegin[39;49;00m$
   759^I  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
   760^I  p := CharPos(Brake, S);$
   761^I$
   762^I  [34mif[39;49;00m p > [34m0[39;49;00m [34mthen[39;49;00m$
   763^I    [36mResult[39;49;00m := [36mCopy[39;49;00m(S, p + [34m1[39;49;00m, [36mLength[39;49;00m(S) - p);$
   764^I[34mend[39;49;00m;$
   765^I$
   766^I[34mfunction[39;49;00m [32mFromLastChar[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Brake: [36mChar[39;49;00m;$
   767^I  IgnoreNoBrake: [36mBoolean[39;49;00m = [34mFalse[39;49;00m): [34mstring[39;49;00m;$
   768^I[34mvar[39;49;00m$
   769^I  p: [36mInteger[39;49;00m;$
   770^I[34mbegin[39;49;00m$
   771^I  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
   772^I  p := CharPosR(Brake, S);$
   773^I$
   774^I  [34mif[39;49;00m p > [34m0[39;49;00m [34mthen[39;49;00m$
   775^I    [36mResult[39;49;00m := [36mCopy[39;49;00m(S, p + [34m1[39;49;00m, [36mLength[39;49;00m(S) - p)$
   776^I  [34melse[39;49;00m [34mif[39;49;00m IgnoreNoBrake [34mthen[39;49;00m$
   777^I    [36mResult[39;49;00m := S;$
   778^I[34mend[39;49;00m;$
   779^I$
   780^I[34mfunction[39;49;00m [32mBetweenChars[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Start, Finish: [36mChar[39;49;00m;$
   781^I  Inclusive: [36mBoolean[39;49;00m = [34mFalse[39;49;00m): [34mstring[39;49;00m;$
   782^I[34mvar[39;49;00m$
   783^I  p, fin: [36mInteger[39;49;00m;$
   784^I[34mbegin[39;49;00m$
   785^I  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
   786^I$
   787^I  p := CharPos(Start, S);$
   788^I  [34mif[39;49;00m p = [34m0[39;49;00m [34mthen[39;49;00m$
   789^I    [34mExit[39;49;00m;$
   790^I$
   791^I  fin := CharPos(Finish, S, p + [34m1[39;49;00m);$
   792^I  [34mif[39;49;00m fin = [34m0[39;49;00m [34mthen[39;49;00m$
   793^I    [34mExit[39;49;00m;$
   794^I$
   795^I  [34mif[39;49;00m [34mnot[39;49;00m Inclusive [34mthen[39;49;00m [34mbegin[39;49;00m$
   796^I    [36mInc[39;49;00m(p);$
   797^I    [36mDec[39;49;00m(fin);$
   798^I  [34mend[39;49;00m;$
   799^I$
   800^I  [36mResult[39;49;00m := [36mCopy[39;49;00m(S, p, fin - p + [34m1[39;49;00m);$
   801^I[34mend[39;49;00m;$
   802^I$
   803^I[34mfunction[39;49;00m [32mUntilStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Brake: [34mstring[39;49;00m): [34mstring[39;49;00m;$
   804^I[34mvar[39;49;00m$
   805^I  p: [36mInteger[39;49;00m;$
   806^I[34mbegin[39;49;00m$
   807^I  [34mif[39;49;00m [36mLength[39;49;00m(Brake) = [34m1[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m$
   808^I    [36mResult[39;49;00m := UntilChar(S, Brake[[34m1[39;49;00m]);$
   809^I  [34mExit[39;49;00m; [34mend[39;49;00m;$
   810^I$
   811^I  p := PosEx(Brake, S);$
   812^I$
   813^I  [34mif[39;49;00m p > [34m0[39;49;00m [34mthen[39;49;00m$
   814^I    [36mResult[39;49;00m := [36mCopy[39;49;00m(S, [34m1[39;49;00m, p - [34m1[39;49;00m)$
   815^I  [34melse[39;49;00m$
   816^I    [36mResult[39;49;00m := S;$
   817^I[34mend[39;49;00m;$
   818^I$
   819^I[34mfunction[39;49;00m [32mFromStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Brake: [34mstring[39;49;00m): [34mstring[39;49;00m;$
   820^I[34mvar[39;49;00m$
   821^I  p: [36mInteger[39;49;00m;$
   822^I[34mbegin[39;49;00m$
   823^I  [34mif[39;49;00m [36mLength[39;49;00m(Brake) = [34m1[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m$
   824^I    [36mResult[39;49;00m := FromChar(S, Brake[[34m1[39;49;00m]);$
   825^I  [34mExit[39;49;00m; [34mend[39;49;00m;$
   826^I$
   827^I  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
   828^I  p := PosEx(Brake, s);$
   829^I$
   830^I  [34mif[39;49;00m p > [34m0[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m$
   831^I    [36mInc[39;49;00m(p, [36mLength[39;49;00m(Brake));$
   832^I    [36mResult[39;49;00m := [36mCopy[39;49;00m(S, p, [36mLength[39;49;00m(S) - p + [34m1[39;49;00m);$
   833^I  [34mend[39;49;00m;$
   834^I[34mend[39;49;00m;$
   835^I$
   836^I[34mfunction[39;49;00m [32mStringWrap[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Width: [36mInteger[39;49;00m; [34mconst[39;49;00m LineEnd: [34mstring[39;49;00m = EOL): [34mstring[39;49;00m;$
   837^I[34mvar[39;49;00m$
   838^I  i: [36mInteger[39;49;00m;$
   839^I[34mbegin[39;49;00m$
   840^I  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
   841^I  [34mif[39;49;00m (S = [33m'[39;49;00m[33m'[39;49;00m) [34mor[39;49;00m (Width < [34m1[39;49;00m) [34mthen[39;49;00m$
   842^I    [34mExit[39;49;00m;$
   843^I$
   844^I  i := [34m1[39;49;00m;$
   845^I  [34mwhile[39;49;00m [34mTrue[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m$
   846^I    [36mResult[39;49;00m := [36mResult[39;49;00m + [36mCopy[39;49;00m(S, i, Width);$
   847^I    [36mInc[39;49;00m(i, Width);$
   848^I    [34mif[39;49;00m i <= [36mLength[39;49;00m(S) [34mthen[39;49;00m$
   849^I      [36mResult[39;49;00m := [36mResult[39;49;00m + LineEnd$
   850^I    [34melse[39;49;00m$
   851^I      [34mExit[39;49;00m;$
   852^I  [34mend[39;49;00m;$
   853^I[34mend[39;49;00m;$
   854^I$
   855^I[34mfunction[39;49;00m [32mSplit[39;49;00m([34mconst[39;49;00m S, Separator: [34mstring[39;49;00m; IgnoreMultiSep: [36mBoolean[39;49;00m = [34mTrue[39;49;00m;$
   856^I  MinCount: [36mInteger[39;49;00m = [34m0[39;49;00m): TStrA;$
   857^I[34mvar[39;49;00m$
   858^I  p, fin, SepLen: [36mInteger[39;49;00m;$
   859^I$
   860^I  [34mprocedure[39;49;00m [32mAdd[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m);$
   861^I  [34mbegin[39;49;00m$
   862^I    [34mif[39;49;00m IgnoreMultiSep [34mand[39;49;00m (S = [33m'[39;49;00m[33m'[39;49;00m) [34mthen[39;49;00m$
   863^I      [34mExit[39;49;00m;$
   864^I    [36mSetLength[39;49;00m([36mResult[39;49;00m, [36mLength[39;49;00m([36mResult[39;49;00m) + [34m1[39;49;00m);$
   865^I    [36mResult[39;49;00m[[36mHigh[39;49;00m([36mResult[39;49;00m)] := S;$
   866^I  [34mend[39;49;00m;$
   867^I$
   868^I[34mbegin[39;49;00m$
   869^I  [34mif[39;49;00m S = [33m'[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m$
   870^I    [34mif[39;49;00m [36mLength[39;49;00m([36mResult[39;49;00m) < MinCount [34mthen[39;49;00m$
   871^I      [36mSetLength[39;49;00m([36mResult[39;49;00m, MinCount);$
   872^I  [34mExit[39;49;00m; [34mend[39;49;00m;$
   873^I$
   874^I  [36mResult[39;49;00m := [34mnil[39;49;00m;$
   875^I  SepLen := [36mLength[39;49;00m(Separator);$
   876^I$
   877^I  p := [34m1[39;49;00m;$
   878^I  fin := PosEx(Separator, S);$
   879^I  [34mwhile[39;49;00m fin > [34m0[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m$
   880^I    Add([36mCopy[39;49;00m(S, p, fin - p));$
   881^I    p := fin + SepLen;$
   882^I    fin := PosEx(Separator, S, p);$
   883^I  [34mend[39;49;00m;$
   884^I  Add([36mCopy[39;49;00m(S, p, [36mLength[39;49;00m(S) - p + [34m1[39;49;00m));$
   885^I$
   886^I  [34mif[39;49;00m [36mLength[39;49;00m([36mResult[39;49;00m) < MinCount [34mthen[39;49;00m$
   887^I    [36mSetLength[39;49;00m([36mResult[39;49;00m, MinCount);$
   888^I[34mend[39;49;00m;$
   889^I$
   890^I[34mprocedure[39;49;00m [32mSplit[39;49;00m([34mconst[39;49;00m S, Separator: [34mstring[39;49;00m; Strings: TStrings;$
   891^I  IgnoreMultiSep: [36mBoolean[39;49;00m = [34mTrue[39;49;00m); $
   892^I[34mvar[39;49;00m$
   893^I  p, fin, SepLen: [36mInteger[39;49;00m;$
   894^I$
   895^I  [34mprocedure[39;49;00m [32mAdd[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m);$
   896^I  [34mbegin[39;49;00m$
   897^I    [34mif[39;49;00m IgnoreMultiSep [34mand[39;49;00m (S = [33m'[39;49;00m[33m'[39;49;00m) [34mthen[39;49;00m$
   898^I      [34mExit[39;49;00m;$
   899^I    Strings.Add(S);$
   900^I  [34mend[39;49;00m;$
   901^I$
   902^I[34mbegin[39;49;00m$
   903^I  [34mif[39;49;00m S = [33m'[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m$
   904^I    [34mExit[39;49;00m;$
   905^I$
   906^I  Strings.BeginUpdate;$
   907^I  SepLen := [36mLength[39;49;00m(Separator);$
   908^I  p := [34m1[39;49;00m;$
   909^I  fin := PosEx(Separator, S);$
   910^I  [34mwhile[39;49;00m fin > [34m0[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m$
   911^I    Add([36mCopy[39;49;00m(S, p, fin - p));$
   912^I    p := fin + SepLen;$
   913^I    fin := PosEx(Separator, S, p);$
   914^I  [34mend[39;49;00m;$
   915^I  Add([36mCopy[39;49;00m(S, p, [36mLength[39;49;00m(S) - p + [34m1[39;49;00m));$
   916^I  Strings.EndUpdate;$
   917^I[34mend[39;49;00m;$
   918^I$
   919^I[34mfunction[39;49;00m [32mSplit[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Separators: TCharSet;$
   920^I  IgnoreMultiSep: [36mBoolean[39;49;00m = [34mTrue[39;49;00m; MinCount: [36mInteger[39;49;00m = [34m0[39;49;00m): TStrA;$
   921^I[34mvar[39;49;00m$
   922^I  p, fin: [36mInteger[39;49;00m;$
   923^I$
   924^I  [34mprocedure[39;49;00m [32mAdd[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m);$
   925^I  [34mbegin[39;49;00m$
   926^I    [34mif[39;49;00m IgnoreMultiSep [34mand[39;49;00m (S = [33m'[39;49;00m[33m'[39;49;00m) [34mthen[39;49;00m$
   927^I      [34mExit[39;49;00m;$
   928^I    [36mSetLength[39;49;00m([36mResult[39;49;00m, [36mLength[39;49;00m([36mResult[39;49;00m) + [34m1[39;49;00m);$
   929^I    [36mResult[39;49;00m[[36mHigh[39;49;00m([36mResult[39;49;00m)] := S;$
   930^I  [34mend[39;49;00m;$
   931^I$
   932^I[34mbegin[39;49;00m$
   933^I  [34mif[39;49;00m S = [33m'[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m$
   934^I    [34mif[39;49;00m [36mLength[39;49;00m([36mResult[39;49;00m) < MinCount [34mthen[39;49;00m$
   935^I      [36mSetLength[39;49;00m([36mResult[39;49;00m, MinCount);$
   936^I  [34mExit[39;49;00m; [34mend[39;49;00m;$
   937^I$
   938^I  [36mResult[39;49;00m := [34mnil[39;49;00m;$
   939^I$
   940^I  p := [34m1[39;49;00m;$
   941^I  fin := CharPos(Separators, S);$
   942^I  [34mwhile[39;49;00m fin > [34m0[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m$
   943^I    Add([36mCopy[39;49;00m(S, p, fin - p));$
   944^I    p := fin + [34m1[39;49;00m;$
   945^I    fin := CharPos(Separators, S, p);$
   946^I  [34mend[39;49;00m;$
   947^I  Add([36mCopy[39;49;00m(S, p, [36mLength[39;49;00m(S) - p + [34m1[39;49;00m));$
   948^I$
   949^I  [34mif[39;49;00m [36mLength[39;49;00m([36mResult[39;49;00m) < MinCount [34mthen[39;49;00m$
   950^I    [36mSetLength[39;49;00m([36mResult[39;49;00m, MinCount);$
   951^I[34mend[39;49;00m;$
   952^I$
   953^I[34mprocedure[39;49;00m [32mTileStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; BrakeStart: [36mInteger[39;49;00m; BrakeEnd: [36mInteger[39;49;00m;$
   954^I  out Left, Right: [34mstring[39;49;00m);$
   955^I[34mbegin[39;49;00m$
   956^I  Left := [36mCopy[39;49;00m(S, [34m1[39;49;00m, BrakeStart-[34m1[39;49;00m);$
   957^I  Right := [36mCopy[39;49;00m(S, BrakeEnd + [34m1[39;49;00m, MaxInt);$
   958^I[34mend[39;49;00m;$
   959^I$
   960^I[34mfunction[39;49;00m [32mJoin[39;49;00m(Strings: TStrings; Separator: [34mstring[39;49;00m = [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;$
   961^I[34mvar[39;49;00m$
   962^I  i, imax: [36mInteger[39;49;00m;$
   963^I[34mbegin[39;49;00m$
   964^I  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
   965^I  imax := Strings.Count-[34m1[39;49;00m;$
   966^I  [34mfor[39;49;00m i := [34m0[39;49;00m [34mto[39;49;00m imax [34mdo[39;49;00m [34mbegin[39;49;00m$
   967^I    [36mResult[39;49;00m := [36mResult[39;49;00m + Strings[i];$
   968^I    [34mif[39;49;00m i < imax [34mthen[39;49;00m$
   969^I      [36mResult[39;49;00m := [36mResult[39;49;00m + Separator;$
   970^I  [34mend[39;49;00m;$
   971^I[34mend[39;49;00m;$
   972^I$
   973^I[34mfunction[39;49;00m [32mJoin[39;49;00m(StrA: TStrA; Separator: [34mstring[39;49;00m = [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m; overload;$
   974^I[34mvar[39;49;00m$
   975^I  i: [36mInteger[39;49;00m;$
   976^I[34mbegin[39;49;00m$
   977^I  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
   978^I  [34mfor[39;49;00m i := [34m0[39;49;00m [34mto[39;49;00m [36mHigh[39;49;00m(StrA) [34mdo[39;49;00m [34mbegin[39;49;00m$
   979^I    [36mResult[39;49;00m := [36mResult[39;49;00m + StrA[i];$
   980^I    [34mif[39;49;00m i < [36mHigh[39;49;00m(StrA) [34mthen[39;49;00m$
   981^I      [36mResult[39;49;00m := [36mResult[39;49;00m + Separator;$
   982^I  [34mend[39;49;00m;$
   983^I[34mend[39;49;00m;$
   984^I$
   985^I[34mfunction[39;49;00m [32mMulStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Count: [36mInteger[39;49;00m): [34mstring[39;49;00m;$
   986^I[34mvar[39;49;00m$
   987^I  P: [36mPChar[39;49;00m;$
   988^I  Len, i: [36mInteger[39;49;00m;$
   989^I[34mbegin[39;49;00m$
   990^I  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
   991^I  [34mif[39;49;00m Count = [34m0[39;49;00m [34mthen[39;49;00m$
   992^I    [34mExit[39;49;00m;$
   993^I$
   994^I  Len := [36mLength[39;49;00m(S);$
   995^I  [36mSetLength[39;49;00m([36mResult[39;49;00m, Len * Count);$
   996^I$
   997^I  P := [36mPointer[39;49;00m([36mResult[39;49;00m);$
   998^I  [34mfor[39;49;00m i := [34m1[39;49;00m [34mto[39;49;00m Count [34mdo[39;49;00m [34mbegin[39;49;00m$
   999^I    [36mMove[39;49;00m([36mPointer[39;49;00m(S)^, P^, Len);$
  1000^I    [36mInc[39;49;00m(P, Len);$
  1001^I  [34mend[39;49;00m;$
  1002^I[34mend[39;49;00m;$
  1003^I$
  1004^I[34mfunction[39;49;00m [32mAlignR[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Width: [36mInteger[39;49;00m; Filler: [36mChar[39;49;00m = [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;$
  1005^I[34mbegin[39;49;00m$
  1006^I  [36mResult[39;49;00m := MulStr(Filler, Width - [36mLength[39;49;00m(S)) + S;$
  1007^I[34mend[39;49;00m;$
  1008^I$
  1009^I[34mfunction[39;49;00m [32mMaxStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; MaxLen: [36mInteger[39;49;00m): [34mstring[39;49;00m;$
  1010^I[34mvar[39;49;00m$
  1011^I  Len: [36mInteger[39;49;00m;$
  1012^I[34mbegin[39;49;00m$
  1013^I  Len := [36mLength[39;49;00m(S);$
  1014^I  [34mif[39;49;00m Len <= MaxLen [34mthen[39;49;00m [34mbegin[39;49;00m$
  1015^I    [36mResult[39;49;00m := S;$
  1016^I  [34mExit[39;49;00m [34mend[39;49;00m;$
  1017^I$
  1018^I  [36mResult[39;49;00m := [36mCopy[39;49;00m(S, [34m1[39;49;00m, MaxLen - [34m3[39;49;00m) + [33m'[39;49;00m[33m...[39;49;00m[33m'[39;49;00m;$
  1019^I[34mend[39;49;00m;$
  1020^I$
  1021^I[34mfunction[39;49;00m [32mTrimAll[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [34mstring[39;49;00m;$
  1022^I[34mvar[39;49;00m$
  1023^I  i: [36mInteger[39;49;00m;$
  1024^I[34mbegin[39;49;00m$
  1025^I  [34mfor[39;49;00m i := [34m1[39;49;00m [34mto[39;49;00m [36mLength[39;49;00m(S) [34mdo[39;49;00m$
  1026^I    [34mif[39;49;00m S[i] > [33m#32[39;49;00m [34mthen[39;49;00m$
  1027^I      [36mResult[39;49;00m := [36mResult[39;49;00m + S[i];$
  1028^I[34mend[39;49;00m;$
  1029^I$
  1030^I[34mfunction[39;49;00m [32mControlChar[39;49;00m(C: [36mChar[39;49;00m): [36mBoolean[39;49;00m;$
  1031^I[34mbegin[39;49;00m$
  1032^I  [36mResult[39;49;00m := C [34min[39;49;00m StrangeChars;$
  1033^I[34mend[39;49;00m;$
  1034^I$
  1035^I[34mfunction[39;49;00m [32mFriendlyChar[39;49;00m(C: [36mChar[39;49;00m): [36mChar[39;49;00m;$
  1036^I[34mbegin[39;49;00m$
  1037^I  [34mcase[39;49;00m C [34mof[39;49;00m$
  1038^I    [33m#0[39;49;00m: [36mResult[39;49;00m := [33m'[39;49;00m[33m.[39;49;00m[33m'[39;49;00m;$
  1039^I    [33m#1[39;49;00m..[33m#31[39;49;00m: [36mResult[39;49;00m := [33m'[39;49;00m[33m?[39;49;00m[33m'[39;49;00m;$
  1040^I    [33m#255[39;49;00m: [36mResult[39;49;00m := [33m'[39;49;00m[33m#[39;49;00m[33m'[39;49;00m;$
  1041^I  [34melse[39;49;00m$
  1042^I    [36mResult[39;49;00m := C;$
  1043^I  [34mend[39;49;00m;$
  1044^I[34mend[39;49;00m;$
  1045^I$
  1046^I[34mfunction[39;49;00m [32mFriendlyStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [34mstring[39;49;00m;$
  1047^I[34mvar[39;49;00m$
  1048^I  i: [36mInteger[39;49;00m;$
  1049^I[34mbegin[39;49;00m$
  1050^I  [36mSetLength[39;49;00m([36mResult[39;49;00m, [36mLength[39;49;00m(S));$
  1051^I  [34mfor[39;49;00m i := [34m1[39;49;00m [34mto[39;49;00m [36mLength[39;49;00m(S) [34mdo[39;49;00m$
  1052^I    [36mResult[39;49;00m[i] := FriendlyChar(S[i]);$
  1053^I[34mend[39;49;00m;$
  1054^I$
  1055^I[34mfunction[39;49;00m [32mFriendlyStr[39;49;00m(a: TByteA): [34mstring[39;49;00m;$
  1056^I[34mvar[39;49;00m$
  1057^I  i: [36mInteger[39;49;00m;$
  1058^I[34mbegin[39;49;00m$
  1059^I  [36mSetLength[39;49;00m([36mResult[39;49;00m, [36mLength[39;49;00m(a));$
  1060^I  [34mfor[39;49;00m i := [34m0[39;49;00m [34mto[39;49;00m [36mHigh[39;49;00m(a) [34mdo[39;49;00m$
  1061^I    [36mResult[39;49;00m[i + [34m1[39;49;00m] := FriendlyChar([36mChar[39;49;00m(a[i]));$
  1062^I[34mend[39;49;00m;$
  1063^I$
  1064^I[34mfunction[39;49;00m [32mQuote[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Quoter: [36mChar[39;49;00m = [33m'[39;49;00m[33m"[39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;$
  1065^I[34mbegin[39;49;00m$
  1066^I  [36mResult[39;49;00m := S;$
  1067^I$
  1068^I  [34mif[39;49;00m FirstChar(S) <> Quoter [34mthen[39;49;00m$
  1069^I    [36mResult[39;49;00m := Quoter + [36mResult[39;49;00m;$
  1070^I$
  1071^I  [34mif[39;49;00m LastChar(S) <> Quoter [34mthen[39;49;00m$
  1072^I    [36mResult[39;49;00m := [36mResult[39;49;00m + Quoter;$
  1073^I[34mend[39;49;00m;$
  1074^I$
  1075^I[34mfunction[39;49;00m [32mDeQuote[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [34mstring[39;49;00m;$
  1076^I[34mbegin[39;49;00m$
  1077^I  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
  1078^I  [34mif[39;49;00m [36mLength[39;49;00m(S) > [34m2[39;49;00m [34mthen[39;49;00m$
  1079^I    [36mResult[39;49;00m := [36mCopy[39;49;00m(S, [34m2[39;49;00m, [36mLength[39;49;00m(S) - [34m2[39;49;00m);$
  1080^I[34mend[39;49;00m;$
  1081^I$
  1082^I[34mfunction[39;49;00m [32mUnQuote[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [34mstring[39;49;00m;$
  1083^I[34mvar[39;49;00m$
  1084^I  Start, Len: [36mInteger[39;49;00m;$
  1085^I[34mbegin[39;49;00m$
  1086^I  Start := [34m1[39;49;00m;$
  1087^I  Len := [36mLength[39;49;00m(S);$
  1088^I$
  1089^I  [34mif[39;49;00m (S <> [33m'[39;49;00m[33m'[39;49;00m) [34mand[39;49;00m (S[[34m1[39;49;00m] [34min[39;49;00m ([[33m#0[39;49;00m..[33m#32[39;49;00m] + QuoteChars)) [34mthen[39;49;00m [34mbegin[39;49;00m$
  1090^I    [34mif[39;49;00m (LastChar(S) = S[[34m1[39;49;00m]) [34mthen[39;49;00m$
  1091^I      [36mDec[39;49;00m(Len);$
  1092^I    [36mInc[39;49;00m(Start);$
  1093^I  [34mend[39;49;00m;$
  1094^I$
  1095^I  [36mResult[39;49;00m := [36mCopy[39;49;00m(S, Start, Len - Start + [34m1[39;49;00m);$
  1096^I[34mend[39;49;00m;$
  1097^I$
  1098^I[34mfunction[39;49;00m [32mStrNumerus[39;49;00m([34mconst[39;49;00m Value: [36mInteger[39;49;00m; [34mconst[39;49;00m Singular, Plural: [34mstring[39;49;00m;$
  1099^I  [34mconst[39;49;00m Zero: [34mstring[39;49;00m = [33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;$
  1100^I[34mbegin[39;49;00m$
  1101^I  [34mif[39;49;00m [36mAbs[39;49;00m(Value) = [34m1[39;49;00m [34mthen[39;49;00m$
  1102^I    [36mResult[39;49;00m := [36mIntToStr[39;49;00m(Value) + [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m + Singular$
  1103^I  [34melse[39;49;00m [34mif[39;49;00m Value = [34m0[39;49;00m [34mthen[39;49;00m$
  1104^I    [36mResult[39;49;00m := Zero + [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m + Plural$
  1105^I  [34melse[39;49;00m$
  1106^I    [36mResult[39;49;00m := [36mIntToStr[39;49;00m(Value) + [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m + Plural;$
  1107^I[34mend[39;49;00m;$
  1108^I$
  1109^I[34mfunction[39;49;00m [32mMakeStr[39;49;00m([34mconst[39;49;00m Items: [34marray[39;49;00m [34mof[39;49;00m [34mconst[39;49;00m; Separator: [34mstring[39;49;00m = [33m'[39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;$
  1110^I[34mconst[39;49;00m$
  1111^I  BoolStrings: [34marray[39;49;00m[[36mBoolean[39;49;00m] [34mof[39;49;00m [34mstring[39;49;00m = ([33m'[39;49;00m[33mFalse[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mTrue[39;49;00m[33m'[39;49;00m);$
  1112^I$
  1113^I[34mvar[39;49;00m$
  1114^I  i: [36mInteger[39;49;00m;$
  1115^I$
  1116^I  [34mfunction[39;49;00m [32mStrOfP[39;49;00m(P: [36mPointer[39;49;00m): [34mstring[39;49;00m;$
  1117^I  [34mbegin[39;49;00m$
  1118^I    [34mif[39;49;00m P = [34mnil[39;49;00m [34mthen[39;49;00m$
  1119^I      [36mResult[39;49;00m := [33m'[39;49;00m[33m[nil][39;49;00m[33m'[39;49;00m$
  1120^I    [34melse[39;49;00m$
  1121^I      [36mResult[39;49;00m := [33m'[39;49;00m[33m[[39;49;00m[33m'[39;49;00m + [36mIntToStr[39;49;00m([36mCardinal[39;49;00m(P)) + [33m'[39;49;00m[33m][39;49;00m[33m'[39;49;00m;$
  1122^I  [34mend[39;49;00m;$
  1123^I$
  1124^I  [34mprocedure[39;49;00m [32mAdd[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m);$
  1125^I  [34mbegin[39;49;00m$
  1126^I    [36mResult[39;49;00m := [36mResult[39;49;00m + s + Separator;$
  1127^I  [34mend[39;49;00m;$
  1128^I$
  1129^I[34mbegin[39;49;00m$
  1130^I  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
  1131^I  [34mfor[39;49;00m i := [34m0[39;49;00m [34mto[39;49;00m [36mHigh[39;49;00m(Items) [34mdo[39;49;00m$
  1132^I    [34mwith[39;49;00m Items[i] [34mdo[39;49;00m$
  1133^I      [34mcase[39;49;00m VType [34mof[39;49;00m$
  1134^I        vtString:     Add(VString^);$
  1135^I        vtInteger:    Add([36mIntToStr[39;49;00m(VInteger));$
  1136^I        vtBoolean:    Add(BoolStrings[VBoolean]);$
  1137^I        vtChar:       Add(VChar);$
  1138^I        vtPChar:      Add(VPChar);$
  1139^I        vtExtended:   Add([36mFloatToStr[39;49;00m(VExtended^));$
  1140^I        vtObject:     [34mif[39;49;00m VObject [34mis[39;49;00m TComponent [34mthen[39;49;00m$
  1141^I                        Add(TComponent(VObject).Name)$
  1142^I                      [34melse[39;49;00m$
  1143^I                        Add(VObject.ClassName);$
  1144^I        vtClass:      Add(VClass.ClassName);$
  1145^I        vtAnsiString: Add([34mstring[39;49;00m(VAnsiString));$
  1146^I        vtCurrency:   Add([36mCurrToStr[39;49;00m(VCurrency^));$
  1147^I        vtInt64:      Add([36mIntToStr[39;49;00m(VInt64^));$
  1148^I        vtVariant:    Add([34mstring[39;49;00m(VVariant^));$
  1149^I$
  1150^I        vtWideChar:   Add(VWideChar);$
  1151^I        vtPWideChar:  Add(VPWideChar);$
  1152^I        vtInterface:  Add(StrOfP(VInterface));$
  1153^I        vtPointer:    Add(StrOfP(VPointer));$
  1154^I        vtWideString: Add([36mWideString[39;49;00m(VWideString));$
  1155^I      [34mend[39;49;00m;$
  1156^I  [34mif[39;49;00m [36mResult[39;49;00m <> [33m'[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m$
  1157^I    [36mSetLength[39;49;00m([36mresult[39;49;00m, [36mLength[39;49;00m([36mResult[39;49;00m) - [36mLength[39;49;00m(Separator));$
  1158^I[34mend[39;49;00m;$
  1159^I$
  1160^I[34mprocedure[39;49;00m [32mShowText[39;49;00m([34mconst[39;49;00m Items: [34marray[39;49;00m [34mof[39;49;00m [34mconst[39;49;00m; Separator: [34mstring[39;49;00m = [33m'[39;49;00m[33m'[39;49;00m);$
  1161^I[34mvar[39;49;00m$
  1162^I  Text: [34mstring[39;49;00m;$
  1163^I[34mbegin[39;49;00m$
  1164^I  Text := MakeStr(Items, Separator);$
  1165^I$
  1166^I  MessageBox([34m0[39;49;00m, [36mPChar[39;49;00m(Text), [33m'[39;49;00m[33mInfo[39;49;00m[33m'[39;49;00m, MB_OK [34mand[39;49;00m MB_APPLMODAL);$
  1167^I[34mend[39;49;00m;$
  1168^I$
  1169^I[34mfunction[39;49;00m [32mDeleteChars[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; C: [36mChar[39;49;00m): [34mstring[39;49;00m;$
  1170^I[34mvar[39;49;00m$
  1171^I  i: [36mInteger[39;49;00m;$
  1172^I[34mbegin[39;49;00m$
  1173^I  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
  1174^I  [34mfor[39;49;00m i := [34m1[39;49;00m [34mto[39;49;00m [36mLength[39;49;00m(S) [34mdo[39;49;00m$
  1175^I    [34mif[39;49;00m S[i] <> C [34mthen[39;49;00m$
  1176^I      [36mResult[39;49;00m := [36mResult[39;49;00m + S[i];$
  1177^I[34mend[39;49;00m;$
  1178^I$
  1179^I[34mfunction[39;49;00m [32mDeleteChars[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; C: TCharSet): [34mstring[39;49;00m;$
  1180^I[34mvar[39;49;00m$
  1181^I  i: [36mInteger[39;49;00m;$
  1182^I[34mbegin[39;49;00m$
  1183^I  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
  1184^I  [34mfor[39;49;00m i := [34m1[39;49;00m [34mto[39;49;00m [36mLength[39;49;00m(S) [34mdo[39;49;00m$
  1185^I    [34mif[39;49;00m [34mnot[39;49;00m (S[i] [34min[39;49;00m C) [34mthen[39;49;00m$
  1186^I      [36mResult[39;49;00m := [36mResult[39;49;00m + S[i];$
  1187^I[34mend[39;49;00m;$
  1188^I$
  1189^I[34mfunction[39;49;00m [32mExtractChars[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; C: TCharSet): [34mstring[39;49;00m;$
  1190^I[34mvar[39;49;00m$
  1191^I  i: [36mInteger[39;49;00m;$
  1192^I[34mbegin[39;49;00m$
  1193^I  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
  1194^I  [34mfor[39;49;00m i := [34m1[39;49;00m [34mto[39;49;00m [36mLength[39;49;00m(S) [34mdo[39;49;00m$
  1195^I    [34mif[39;49;00m S[i] [34min[39;49;00m C [34mthen[39;49;00m$
  1196^I      [36mResult[39;49;00m := [36mResult[39;49;00m + S[i];$
  1197^I[34mend[39;49;00m;$
  1198^I$
  1199^I[34mfunction[39;49;00m [32mCharCount[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; C: [36mChar[39;49;00m): [36mInteger[39;49;00m;$
  1200^I[34mvar[39;49;00m$
  1201^I  i: [36mInteger[39;49;00m;$
  1202^I[34mbegin[39;49;00m$
  1203^I  [36mResult[39;49;00m := [34m0[39;49;00m;$
  1204^I  [34mfor[39;49;00m i := [34m1[39;49;00m [34mto[39;49;00m [36mLength[39;49;00m(S) [34mdo[39;49;00m$
  1205^I    [34mif[39;49;00m S[i] = C [34mthen[39;49;00m$
  1206^I      [36mInc[39;49;00m([36mResult[39;49;00m);$
  1207^I[34mend[39;49;00m;$
  1208^I$
  1209^I[34mfunction[39;49;00m [32mStrAtPos[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; [36mPos[39;49;00m: [36mInteger[39;49;00m; [34mconst[39;49;00m [36mStr[39;49;00m: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
  1210^I[34mbegin[39;49;00m$
  1211^I  [36mResult[39;49;00m := ([36mStr[39;49;00m <> [33m'[39;49;00m[33m'[39;49;00m) [34mand[39;49;00m ([36mStr[39;49;00m = [36mCopy[39;49;00m(S, [36mPos[39;49;00m, [36mLength[39;49;00m([36mStr[39;49;00m)));$
  1212^I[34mend[39;49;00m;$
  1213^I$
  1214^I[34mfunction[39;49;00m [32mTextAtPos[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; [36mPos[39;49;00m: [36mInteger[39;49;00m; [34mconst[39;49;00m Text: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
  1215^I[34mbegin[39;49;00m$
  1216^I  [36mResult[39;49;00m := (Text <> [33m'[39;49;00m[33m'[39;49;00m) [34mand[39;49;00m [36mSameText[39;49;00m(Text, [36mCopy[39;49;00m(S, [36mPos[39;49;00m, [36mLength[39;49;00m(Text)));$
  1217^I[34mend[39;49;00m;$
  1218^I$
  1219^I[34mfunction[39;49;00m [32mStrAtBegin[39;49;00m([34mconst[39;49;00m S, [36mStr[39;49;00m: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
  1220^I[34mbegin[39;49;00m$
  1221^I  [36mResult[39;49;00m := StrAtPos(S, [34m1[39;49;00m, [36mStr[39;49;00m);$
  1222^I[34mend[39;49;00m;$
  1223^I$
  1224^I[34mfunction[39;49;00m [32mTextAtBegin[39;49;00m([34mconst[39;49;00m S, Text: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
  1225^I[34mbegin[39;49;00m$
  1226^I  [36mResult[39;49;00m := TextAtPos(S, [34m1[39;49;00m, Text);$
  1227^I[34mend[39;49;00m;$
  1228^I$
  1229^I[34mfunction[39;49;00m [32mCharIn[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; C: [36mChar[39;49;00m): [36mBoolean[39;49;00m;$
  1230^I[34mvar[39;49;00m$
  1231^I  i: [36mInteger[39;49;00m;$
  1232^I[34mbegin[39;49;00m$
  1233^I  [36mResult[39;49;00m := [34mTrue[39;49;00m;$
  1234^I  [34mfor[39;49;00m i := [34m1[39;49;00m [34mto[39;49;00m [36mLength[39;49;00m(S) [34mdo[39;49;00m$
  1235^I    [34mif[39;49;00m S[i] = C [34mthen[39;49;00m [34mExit[39;49;00m;$
  1236^I  [36mResult[39;49;00m := [34mFalse[39;49;00m;$
  1237^I[34mend[39;49;00m;$
  1238^I$
  1239^I[34mfunction[39;49;00m [32mCharIn[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; C: TCharSet): [36mBoolean[39;49;00m;$
  1240^I[34mvar[39;49;00m$
  1241^I  i: [36mInteger[39;49;00m;$
  1242^I[34mbegin[39;49;00m$
  1243^I  [36mResult[39;49;00m := [34mFalse[39;49;00m;$
  1244^I  [34mfor[39;49;00m i := [34m1[39;49;00m [34mto[39;49;00m [36mLength[39;49;00m(S) [34mdo[39;49;00m [34mbegin[39;49;00m$
  1245^I    [36mResult[39;49;00m := S[i] [34min[39;49;00m C;$
  1246^I    [34mif[39;49;00m [36mResult[39;49;00m [34mthen[39;49;00m$
  1247^I      [34mExit[39;49;00m;$
  1248^I  [34mend[39;49;00m;$
  1249^I[34mend[39;49;00m;$
  1250^I$
  1251^I[34mfunction[39;49;00m [32mStrIn[39;49;00m([34mconst[39;49;00m S, SubStr: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
  1252^I[34mbegin[39;49;00m$
  1253^I  [36mResult[39;49;00m := PosEx(SubStr, S) > [34m0[39;49;00m;$
  1254^I[34mend[39;49;00m;$
  1255^I$
  1256^I[34mfunction[39;49;00m [32mStrIn[39;49;00m(SL: TStrings; [34mconst[39;49;00m S: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
  1257^I[34mvar[39;49;00m$
  1258^I  i: [36mInteger[39;49;00m;$
  1259^I[34mbegin[39;49;00m$
  1260^I  [36mResult[39;49;00m := [34mFalse[39;49;00m;$
  1261^I  [34mfor[39;49;00m i := [34m0[39;49;00m [34mto[39;49;00m SL.Count-[34m1[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m$
  1262^I    [36mResult[39;49;00m := (S = SL[i]);$
  1263^I    [34mif[39;49;00m [36mResult[39;49;00m [34mthen[39;49;00m$
  1264^I      [34mExit[39;49;00m;$
  1265^I  [34mend[39;49;00m;$
  1266^I[34mend[39;49;00m;$
  1267^I$
  1268^I[34mfunction[39;49;00m [32mStrIn[39;49;00m(A: TStrA; [34mconst[39;49;00m S: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
  1269^I[34mvar[39;49;00m$
  1270^I  i: [36mInteger[39;49;00m;$
  1271^I[34mbegin[39;49;00m$
  1272^I  [36mResult[39;49;00m := [34mFalse[39;49;00m;$
  1273^I  [34mfor[39;49;00m i := [36mLow[39;49;00m(A) [34mto[39;49;00m [36mHigh[39;49;00m(A) [34mdo[39;49;00m [34mbegin[39;49;00m$
  1274^I    [36mResult[39;49;00m := (S = A[i]);$
  1275^I    [34mif[39;49;00m [36mResult[39;49;00m [34mthen[39;49;00m$
  1276^I      [34mExit[39;49;00m;$
  1277^I  [34mend[39;49;00m;$
  1278^I[34mend[39;49;00m;$
  1279^I$
  1280^I[34mfunction[39;49;00m [32mTextIn[39;49;00m([34mconst[39;49;00m S, Text: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
  1281^I[34mbegin[39;49;00m$
  1282^I  [36mResult[39;49;00m := PosExText(Text, S) > [34m0[39;49;00m;$
  1283^I[34mend[39;49;00m;$
  1284^I$
  1285^I[34mfunction[39;49;00m [32mTextIn[39;49;00m(SL: TStrings; [34mconst[39;49;00m Text: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
  1286^I[34mvar[39;49;00m$
  1287^I  i: [36mInteger[39;49;00m;$
  1288^I[34mbegin[39;49;00m$
  1289^I  [36mResult[39;49;00m := [34mFalse[39;49;00m;$
  1290^I  [34mfor[39;49;00m i := [34m0[39;49;00m [34mto[39;49;00m SL.Count-[34m1[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m$
  1291^I    [36mResult[39;49;00m := [36mSameText[39;49;00m(Text, SL[i]);$
  1292^I    [34mif[39;49;00m [36mResult[39;49;00m [34mthen[39;49;00m$
  1293^I      [34mExit[39;49;00m;$
  1294^I  [34mend[39;49;00m;$
  1295^I[34mend[39;49;00m;$
  1296^I$
  1297^I[34mfunction[39;49;00m [32mTextIn[39;49;00m(A: TStrA; [34mconst[39;49;00m Text: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
  1298^I[34mvar[39;49;00m$
  1299^I  i: [36mInteger[39;49;00m;$
  1300^I[34mbegin[39;49;00m$
  1301^I  [36mResult[39;49;00m := [34mFalse[39;49;00m;$
  1302^I  [34mfor[39;49;00m i := [36mLow[39;49;00m(A) [34mto[39;49;00m [36mHigh[39;49;00m(A) [34mdo[39;49;00m [34mbegin[39;49;00m$
  1303^I    [36mResult[39;49;00m := [36mSameText[39;49;00m(Text, A[i]);$
  1304^I    [34mif[39;49;00m [36mResult[39;49;00m [34mthen[39;49;00m$
  1305^I      [34mExit[39;49;00m;$
  1306^I  [34mend[39;49;00m;$
  1307^I[34mend[39;49;00m;$
  1308^I$
  1309^I[34mfunction[39;49;00m [32mStrIndex[39;49;00m(SL: TStrings; [34mconst[39;49;00m S: [34mstring[39;49;00m): [36mInteger[39;49;00m;$
  1310^I[34mbegin[39;49;00m$
  1311^I  [34mfor[39;49;00m [36mResult[39;49;00m := [34m0[39;49;00m [34mto[39;49;00m SL.Count-[34m1[39;49;00m [34mdo[39;49;00m$
  1312^I    [34mif[39;49;00m S = SL[[36mResult[39;49;00m] [34mthen[39;49;00m$
  1313^I      [34mExit[39;49;00m;$
  1314^I  [36mResult[39;49;00m := -[34m1[39;49;00m;$
  1315^I[34mend[39;49;00m;$
  1316^I$
  1317^I[34mfunction[39;49;00m [32mStrIndex[39;49;00m(A: TStrA; [34mconst[39;49;00m S: [34mstring[39;49;00m): [36mInteger[39;49;00m;$
  1318^I[34mbegin[39;49;00m$
  1319^I  [34mfor[39;49;00m [36mResult[39;49;00m := [36mLow[39;49;00m(A) [34mto[39;49;00m [36mHigh[39;49;00m(A) [34mdo[39;49;00m$
  1320^I    [34mif[39;49;00m S = A[[36mResult[39;49;00m] [34mthen[39;49;00m$
  1321^I      [34mExit[39;49;00m;$
  1322^I  [36mResult[39;49;00m := -[34m1[39;49;00m;$
  1323^I[34mend[39;49;00m;$
  1324^I$
  1325^I[34mfunction[39;49;00m [32mTextIndex[39;49;00m(SL: TStrings; [34mconst[39;49;00m Text: [34mstring[39;49;00m): [36mInteger[39;49;00m;$
  1326^I[34mbegin[39;49;00m$
  1327^I  [34mfor[39;49;00m [36mResult[39;49;00m := [34m0[39;49;00m [34mto[39;49;00m SL.Count-[34m1[39;49;00m [34mdo[39;49;00m$
  1328^I    [34mif[39;49;00m [36mSameText[39;49;00m(Text, SL[[36mResult[39;49;00m]) [34mthen[39;49;00m$
  1329^I      [34mExit[39;49;00m;$
  1330^I  [36mResult[39;49;00m := -[34m1[39;49;00m;$
  1331^I[34mend[39;49;00m;$
  1332^I$
  1333^I[34mfunction[39;49;00m [32mTextIndex[39;49;00m(A: TStrA; [34mconst[39;49;00m Text: [34mstring[39;49;00m): [36mInteger[39;49;00m;$
  1334^I[34mbegin[39;49;00m$
  1335^I  [34mfor[39;49;00m [36mResult[39;49;00m := [36mLow[39;49;00m(A) [34mto[39;49;00m [36mHigh[39;49;00m(A) [34mdo[39;49;00m$
  1336^I    [34mif[39;49;00m [36mSameText[39;49;00m(Text, A[[36mResult[39;49;00m]) [34mthen[39;49;00m$
  1337^I      [34mExit[39;49;00m;$
  1338^I  [36mResult[39;49;00m := -[34m1[39;49;00m;$
  1339^I[34mend[39;49;00m;$
  1340^I$
  1341^I[34mfunction[39;49;00m [32mReplaceChars[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Old, [34mNew[39;49;00m: [36mChar[39;49;00m): [34mstring[39;49;00m;$
  1342^I[34mvar[39;49;00m$
  1343^I  i: [36mInteger[39;49;00m;$
  1344^I[34mbegin[39;49;00m$
  1345^I  [36mResult[39;49;00m := S;$
  1346^I  [34mfor[39;49;00m i := [34m1[39;49;00m [34mto[39;49;00m [36mLength[39;49;00m([36mResult[39;49;00m) [34mdo[39;49;00m$
  1347^I    [34mif[39;49;00m [36mResult[39;49;00m[i] = Old [34mthen[39;49;00m$
  1348^I      [36mResult[39;49;00m[i] := [34mNew[39;49;00m;$
  1349^I[34mend[39;49;00m;$
  1350^I$
  1351^I[34mfunction[39;49;00m [32mReplaceChars[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; Old: TCharSet; [34mNew[39;49;00m: [36mChar[39;49;00m): [34mstring[39;49;00m;$
  1352^I[34mvar[39;49;00m$
  1353^I  i: [36mInteger[39;49;00m;$
  1354^I[34mbegin[39;49;00m$
  1355^I  [36mResult[39;49;00m := S;$
  1356^I  [34mfor[39;49;00m i := [34m1[39;49;00m [34mto[39;49;00m [36mLength[39;49;00m([36mResult[39;49;00m) [34mdo[39;49;00m$
  1357^I    [34mif[39;49;00m [36mResult[39;49;00m[i] [34min[39;49;00m Old [34mthen[39;49;00m$
  1358^I      [36mResult[39;49;00m[i] := [34mNew[39;49;00m;$
  1359^I[34mend[39;49;00m;$
  1360^I$
  1361^I[34mfunction[39;49;00m [32mReplace[39;49;00m([34mconst[39;49;00m S, Old, [34mNew[39;49;00m: [34mstring[39;49;00m): [34mstring[39;49;00m;$
  1362^I[34mvar[39;49;00m$
  1363^I  oldp, ps: [36mInteger[39;49;00m;$
  1364^I[34mbegin[39;49;00m$
  1365^I  ps := [34m1[39;49;00m;$
  1366^I  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
  1367^I  [34mwhile[39;49;00m [34mTrue[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m$
  1368^I    oldp := ps;$
  1369^I    ps := PosEx(Old, S, oldp);$
  1370^I    [34mif[39;49;00m ps = [34m0[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m$
  1371^I      [36mResult[39;49;00m := [36mResult[39;49;00m + [36mCopy[39;49;00m(S, oldp, [36mLength[39;49;00m(S) - oldp + [34m1[39;49;00m);$
  1372^I    [34mExit[39;49;00m; [34mend[39;49;00m;$
  1373^I    [36mResult[39;49;00m := [36mResult[39;49;00m + [36mCopy[39;49;00m(S, oldp, ps - oldp) + [34mNew[39;49;00m;$
  1374^I    [36mInc[39;49;00m(ps, [36mLength[39;49;00m(Old));$
  1375^I  [34mend[39;49;00m;$
  1376^I[34mend[39;49;00m;$
  1377^I$
  1378^I[34mfunction[39;49;00m [32mSLOfFile[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m): TStringList;$
  1379^I[34mbegin[39;49;00m$
  1380^I  [36mResult[39;49;00m := TStringList.Create;$
  1381^I  [34mif[39;49;00m [36mFileExists[39;49;00m(FileName) [34mthen[39;49;00m$
  1382^I    [36mResult[39;49;00m.LoadFromFile(FileName);$
  1383^I[34mend[39;49;00m;$
  1384^I$
  1385^I[34mfunction[39;49;00m [32mContainsEmptyLines[39;49;00m(SL: TStrings): [36mBoolean[39;49;00m;$
  1386^I[34mbegin[39;49;00m$
  1387^I  [36mResult[39;49;00m := StrIn(SL, [33m'[39;49;00m[33m'[39;49;00m);$
  1388^I[34mend[39;49;00m;$
  1389^I$
  1390^I[34mprocedure[39;49;00m [32mDeleteEmptyLines[39;49;00m(SL: TStrings);$
  1391^I[34mvar[39;49;00m$
  1392^I  i: [36mInteger[39;49;00m;$
  1393^I[34mbegin[39;49;00m$
  1394^I  i := [34m0[39;49;00m;$
  1395^I  [34mwhile[39;49;00m i < SL.Count [34mdo[39;49;00m [34mbegin[39;49;00m$
  1396^I    [34mif[39;49;00m SL[i] = [33m'[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m$
  1397^I      SL.Delete(i)$
  1398^I    [34melse[39;49;00m$
  1399^I      [36mInc[39;49;00m(i);$
  1400^I  [34mend[39;49;00m;$
  1401^I[34mend[39;49;00m;$
  1402^I$
  1403^I[34mprocedure[39;49;00m [32mDeleteCommentLines[39;49;00m(SL: TStrings; [34mconst[39;49;00m CommentSign: [34mstring[39;49;00m = [33m'[39;49;00m[33m//[39;49;00m[33m'[39;49;00m);$
  1404^I[34mvar[39;49;00m$
  1405^I  i: [36mInteger[39;49;00m;$
  1406^I[34mbegin[39;49;00m$
  1407^I  i := [34m0[39;49;00m;$
  1408^I  [34mwhile[39;49;00m i < SL.Count [34mdo[39;49;00m [34mbegin[39;49;00m$
  1409^I    [34mif[39;49;00m (SL[i] = [33m'[39;49;00m[33m'[39;49;00m) [34mor[39;49;00m (StrAtBegin([36mTrimLeft[39;49;00m(SL[i]), CommentSign)) [34mthen[39;49;00m$
  1410^I      SL.Delete(i)$
  1411^I    [34melse[39;49;00m$
  1412^I      [36mInc[39;49;00m(i);$
  1413^I  [34mend[39;49;00m;$
  1414^I[34mend[39;49;00m;$
  1415^I$
  1416^I[34mfunction[39;49;00m [32mFindLine[39;49;00m(SL: TStrings; [34mconst[39;49;00m S: [34mstring[39;49;00m): [36mInteger[39;49;00m;$
  1417^I[34mbegin[39;49;00m$
  1418^I  [34mfor[39;49;00m [36mResult[39;49;00m := [34m0[39;49;00m [34mto[39;49;00m SL.Count-[34m1[39;49;00m [34mdo[39;49;00m$
  1419^I    [34mif[39;49;00m TextAtBegin(SL[[36mResult[39;49;00m], S) [34mthen[39;49;00m$
  1420^I      [34mExit[39;49;00m;$
  1421^I  [36mResult[39;49;00m := -[34m1[39;49;00m;$
  1422^I[34mend[39;49;00m;$
  1423^I$
  1424^I[34mprocedure[39;49;00m [32mQuickSortSL[39;49;00m(SL: TStringList);$
  1425^I$
  1426^I  [34mprocedure[39;49;00m [32mSort[39;49;00m(l, r: [36mInteger[39;49;00m);$
  1427^I  [34mvar[39;49;00m$
  1428^I    i,j: [36mInteger[39;49;00m;$
  1429^I    z,x: [34mstring[39;49;00m;$
  1430^I  [34mbegin[39;49;00m$
  1431^I    i := l;$
  1432^I    j := r;$
  1433^I    x := SL[(j + i) [34mdiv[39;49;00m [34m2[39;49;00m];$
  1434^I    [34mrepeat[39;49;00m$
  1435^I      [34mwhile[39;49;00m SL[i] < x [34mdo[39;49;00m [36mInc[39;49;00m(i);$
  1436^I      [34mwhile[39;49;00m SL[j] > x [34mdo[39;49;00m [36mDec[39;49;00m(j);$
  1437^I      [34mif[39;49;00m i <= j [34mthen[39;49;00m [34mbegin[39;49;00m$
  1438^I        z := SL[i];$
  1439^I        SL[i] := SL[j];$
  1440^I        SL[j] := z;$
  1441^I        [36mInc[39;49;00m(i); [36mDec[39;49;00m(j);$
  1442^I      [34mend[39;49;00m;$
  1443^I    [34muntil[39;49;00m i > j;$
  1444^I    [34mif[39;49;00m j > l [34mthen[39;49;00m Sort(l, j);$
  1445^I    [34mif[39;49;00m i < r [34mthen[39;49;00m Sort(i, r);$
  1446^I  [34mend[39;49;00m;$
  1447^I$
  1448^I[34mbegin[39;49;00m$
  1449^I  [34mif[39;49;00m SL.Count > [34m0[39;49;00m [34mthen[39;49;00m$
  1450^I    Sort([34m0[39;49;00m, SL.Count-[34m1[39;49;00m);$
  1451^I[34mend[39;49;00m;$
  1452^I$
  1453^I[34mfunction[39;49;00m [32mIncStrA[39;49;00m(StrA: TStrA): [36mInteger[39;49;00m;$
  1454^I[34mbegin[39;49;00m$
  1455^I  [36mSetLength[39;49;00m(StrA, [36mLength[39;49;00m(StrA) + [34m1[39;49;00m);$
  1456^I  [36mResult[39;49;00m := [36mHigh[39;49;00m(StrA);$
  1457^I[34mend[39;49;00m;$
  1458^I$
  1459^I[34mfunction[39;49;00m [32mStrOfByteA[39;49;00m(a: TByteA): [34mstring[39;49;00m;$
  1460^I[34mbegin[39;49;00m$
  1461^I  [36mResult[39;49;00m := [34mstring[39;49;00m([36mCopy[39;49;00m(a, [34m0[39;49;00m, [36mLength[39;49;00m(a)));$
  1462^I[34mend[39;49;00m;$
  1463^I$
  1464^I[34mfunction[39;49;00m [32mByteAOfStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): TByteA;$
  1465^I[34mbegin[39;49;00m$
  1466^I  [36mResult[39;49;00m := TByteA([36mCopy[39;49;00m(S, [34m1[39;49;00m, [36mLength[39;49;00m(s)));$
  1467^I[34mend[39;49;00m;$
  1468^I$
  1469^I[34mfunction[39;49;00m [32mByteAOfInt[39;49;00m(i: [36mInteger[39;49;00m): TByteA;$
  1470^I[34mbegin[39;49;00m$
  1471^I  [36mSetLength[39;49;00m([36mResult[39;49;00m, [36mSizeOf[39;49;00m([36mInteger[39;49;00m));$
  1472^I  [36mMove[39;49;00m(i, [36mPointer[39;49;00m([36mResult[39;49;00m)^, [36mSizeOf[39;49;00m([36mInteger[39;49;00m));$
  1473^I[34mend[39;49;00m;$
  1474^I$
  1475^I[34mfunction[39;49;00m [32mIntOfByteA[39;49;00m(A: TByteA): [36mInteger[39;49;00m;$
  1476^I[34mbegin[39;49;00m$
  1477^I  [36mResult[39;49;00m := [34m0[39;49;00m;$
  1478^I  [36mMove[39;49;00m([36mPointer[39;49;00m(A)^, [36mResult[39;49;00m, [36mMin[39;49;00m([36mLength[39;49;00m(A), [36mSizeOf[39;49;00m([36mInteger[39;49;00m)));$
  1479^I[34mend[39;49;00m;$
  1480^I$
  1481^I[34mfunction[39;49;00m [32mByteAOfHex[39;49;00m([34mconst[39;49;00m Hex: [34mstring[39;49;00m): TByteA;$
  1482^I[34mvar[39;49;00m$
  1483^I  i: [36mInteger[39;49;00m;$
  1484^I  h: [34mstring[39;49;00m;$
  1485^I[34mbegin[39;49;00m$
  1486^I  h := ExtractChars(Hex, HexadecimalChars);$
  1487^I  [36mSetLength[39;49;00m([36mResult[39;49;00m, [36mLength[39;49;00m(h) [34mdiv[39;49;00m [34m2[39;49;00m);$
  1488^I  [34mfor[39;49;00m i := [34m0[39;49;00m [34mto[39;49;00m [36mHigh[39;49;00m([36mResult[39;49;00m) [34mdo[39;49;00m$
  1489^I    [36mResult[39;49;00m[i] := ByteOfHex([36mCopy[39;49;00m(h, (i [34mshl[39;49;00m [34m1[39;49;00m) + [34m1[39;49;00m, [34m2[39;49;00m));$
  1490^I[34mend[39;49;00m;$
  1491^I$
  1492^I[34mfunction[39;49;00m [32mSizeOfFile[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m): [36mInteger[39;49;00m;$
  1493^I[34mvar[39;49;00m$
  1494^I  F: [34mfile[39;49;00m;$
  1495^I[34mbegin[39;49;00m$
  1496^I  [36mAssignFile[39;49;00m(F, FileName);$
  1497^I  [37m{$I-}[39;49;00m[36mReset[39;49;00m(F, [34m1[39;49;00m);[37m{$I+}[39;49;00m$
  1498^I  [34mif[39;49;00m [36mIOResult[39;49;00m = [34m0[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m$
  1499^I    [36mResult[39;49;00m := [36mFileSize[39;49;00m(F);$
  1500^I    [36mCloseFile[39;49;00m(F);$
  1501^I  [34mend[39;49;00m [34melse[39;49;00m$
  1502^I    [36mResult[39;49;00m := [34m0[39;49;00m;$
  1503^I[34mend[39;49;00m;$
  1504^I$
  1505^I[34mfunction[39;49;00m [32mFileEx[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m; AllowFolders: [36mBoolean[39;49;00m = [34mFalse[39;49;00m): [36mBoolean[39;49;00m;$
  1506^I[34mvar[39;49;00m$
  1507^I  FindData: TWin32FindData;$
  1508^I[34mbegin[39;49;00m$
  1509^I  [34mif[39;49;00m FileName = [33m'[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m$
  1510^I    [36mResult[39;49;00m := [34mFalse[39;49;00m;$
  1511^I  [34mExit[39;49;00m; [34mend[39;49;00m;$
  1512^I$
  1513^I  [36mResult[39;49;00m := (AllowFolders [34mand[39;49;00m [36mDirectoryExists[39;49;00m(FileName)) [34mor[39;49;00m$
  1514^I    (FindFirstFile([36mPChar[39;49;00m(FileName), FindData) <> INVALID_HANDLE_VALUE);$
  1515^I  [36mResult[39;49;00m := [36mResult[39;49;00m [34mand[39;49;00m [34mnot[39;49;00m CharIn(FileName, WildCards);$
  1516^I  [36mResult[39;49;00m := [36mResult[39;49;00m [34mand[39;49;00m (AllowFolders$
  1517^I    [34mor[39;49;00m ((FindData.dwFileAttributes [34mand[39;49;00m FILE_ATTRIBUTE_DIRECTORY) = [34m0[39;49;00m));$
  1518^I[34mend[39;49;00m;$
  1519^I$
  1520^I[34mfunction[39;49;00m [32mLWPSolve[39;49;00m([34mconst[39;49;00m Dir: [34mstring[39;49;00m): [34mstring[39;49;00m;$
  1521^I[34mbegin[39;49;00m$
  1522^I  [34mif[39;49;00m (Dir <> [33m'[39;49;00m[33m'[39;49;00m) [34mand[39;49;00m (Dir[[36mLength[39;49;00m(Dir)] = [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m) [34mthen[39;49;00m [34mbegin[39;49;00m$
  1523^I    [36mResult[39;49;00m := [36mCopy[39;49;00m(Dir, [34m1[39;49;00m, [36mLength[39;49;00m(Dir) - [34m1[39;49;00m);$
  1524^I  [34mend[39;49;00m [34melse[39;49;00m$
  1525^I    [36mResult[39;49;00m := Dir;$
  1526^I[34mend[39;49;00m;$
  1527^I$
  1528^I[34mfunction[39;49;00m [32mLWPSlash[39;49;00m([34mconst[39;49;00m Dir: [34mstring[39;49;00m): [34mstring[39;49;00m;$
  1529^I[34mbegin[39;49;00m$
  1530^I  [34mif[39;49;00m (Dir <> [33m'[39;49;00m[33m'[39;49;00m) [34mand[39;49;00m (Dir[[36mLength[39;49;00m(Dir)] = [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m) [34mthen[39;49;00m [34mbegin[39;49;00m$
  1531^I    [36mResult[39;49;00m := [36mCopy[39;49;00m(Dir, [34m1[39;49;00m, [36mLength[39;49;00m(Dir));$
  1532^I  [34mend[39;49;00m [34melse[39;49;00m$
  1533^I    [36mResult[39;49;00m := Dir + [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m;$
  1534^I[34mend[39;49;00m;$
  1535^I$
  1536^I[34mfunction[39;49;00m [32mExtractDrive[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m): [34mstring[39;49;00m;$
  1537^I[34mbegin[39;49;00m$
  1538^I  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
  1539^I  [34mif[39;49;00m ([36mLength[39;49;00m(FileName) >= [34m2[39;49;00m) [34mand[39;49;00m (FileName[[34m2[39;49;00m] = [33m'[39;49;00m[33m:[39;49;00m[33m'[39;49;00m) [34mthen[39;49;00m$
  1540^I    [36mResult[39;49;00m := [36mUpperCase[39;49;00m(FileName[[34m1[39;49;00m] + [33m'[39;49;00m[33m:\[39;49;00m[33m'[39;49;00m);$
  1541^I[34mend[39;49;00m;$
  1542^I$
  1543^I[34mfunction[39;49;00m [32mExtractPath[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m): [34mstring[39;49;00m;$
  1544^I[34mvar[39;49;00m$
  1545^I  p: [36mInteger[39;49;00m;$
  1546^I[34mbegin[39;49;00m$
  1547^I  p := CharPosR([33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m, FileName);$
  1548^I  [34mif[39;49;00m P > [34m0[39;49;00m [34mthen[39;49;00m$
  1549^I    [36mResult[39;49;00m := [36mCopy[39;49;00m(FileName, [34m1[39;49;00m, p)$
  1550^I  [34melse[39;49;00m$
  1551^I    [36mResult[39;49;00m := FileName;$
  1552^I[34mend[39;49;00m;$
  1553^I$
  1554^I[34mfunction[39;49;00m [32mExtractPrefix[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m): [34mstring[39;49;00m;$
  1555^I[34mbegin[39;49;00m$
  1556^I  [36mResult[39;49;00m := UntilLastChar([36mExtractFileName[39;49;00m(FileName), [33m'[39;49;00m[33m.[39;49;00m[33m'[39;49;00m);$
  1557^I[34mend[39;49;00m;$
  1558^I$
  1559^I[34mfunction[39;49;00m [32mExtractSuffix[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m): [34mstring[39;49;00m;$
  1560^I[34mbegin[39;49;00m$
  1561^I  [36mResult[39;49;00m := FromLastChar([36mExtractFileName[39;49;00m(FileName), [33m'[39;49;00m[33m.[39;49;00m[33m'[39;49;00m);$
  1562^I[34mend[39;49;00m;$
  1563^I$
  1564^I[34mfunction[39;49;00m [32mSameByteA[39;49;00m([34mconst[39;49;00m A, B: TByteA): [36mBoolean[39;49;00m;$
  1565^I[34mbegin[39;49;00m$
  1566^I  [36mResult[39;49;00m := (A = B) [34mor[39;49;00m (([36mLength[39;49;00m(A) = [36mLength[39;49;00m(B)) [34mand[39;49;00m [36mCompareMem[39;49;00m(A, B, [36mLength[39;49;00m(A)));$
  1567^I[34mend[39;49;00m;$
  1568^I$
  1569^I[34mfunction[39;49;00m [32mReverse[39;49;00m(A: TByteA): TByteA;$
  1570^I[34mvar[39;49;00m$
  1571^I  i: [36mInteger[39;49;00m;$
  1572^I[34mbegin[39;49;00m$
  1573^I  [36mSetLength[39;49;00m([36mResult[39;49;00m, [36mLength[39;49;00m(A));$
  1574^I$
  1575^I  [34mfor[39;49;00m i := [34m0[39;49;00m [34mto[39;49;00m [36mHigh[39;49;00m(A) [34mdo[39;49;00m$
  1576^I    [36mResult[39;49;00m[[36mHigh[39;49;00m([36mResult[39;49;00m) - i] := A[i];$
  1577^I[34mend[39;49;00m;$
  1578^I$
  1579^I[34mfunction[39;49;00m [32mEndian[39;49;00m(i: [36mInteger[39;49;00m): [36mInteger[39;49;00m;$
  1580^I[34mtype[39;49;00m$
  1581^I  EndianArray = [34mpacked[39;49;00m [34marray[39;49;00m[[34m0[39;49;00m..[34m3[39;49;00m] [34mof[39;49;00m [36mByte[39;49;00m;$
  1582^I[34mvar[39;49;00m$
  1583^I  a, b: EndianArray;$
  1584^I[34mbegin[39;49;00m$
  1585^I  a := EndianArray(i);$
  1586^I  b[[34m0[39;49;00m] := a[[34m3[39;49;00m];$
  1587^I  b[[34m1[39;49;00m] := a[[34m2[39;49;00m];$
  1588^I  b[[34m2[39;49;00m] := a[[34m1[39;49;00m];$
  1589^I  b[[34m3[39;49;00m] := a[[34m0[39;49;00m];$
  1590^I  [36mResult[39;49;00m := [36mInteger[39;49;00m(b);$
  1591^I[34mend[39;49;00m;$
  1592^I$
  1593^I[34mfunction[39;49;00m [32mSaveByteA[39;49;00m(Data: TByteA; [34mconst[39;49;00m FileName: [34mstring[39;49;00m;$
  1594^I  Overwrite: [36mBoolean[39;49;00m = [34mTrue[39;49;00m): [36mBoolean[39;49;00m;$
  1595^I[34mvar[39;49;00m$
  1596^I  F: [34mfile[39;49;00m;$
  1597^I[34mbegin[39;49;00m$
  1598^I  [34mif[39;49;00m [36mFileExists[39;49;00m(FileName) [34mand[39;49;00m [34mnot[39;49;00m Overwrite [34mthen[39;49;00m [34mbegin[39;49;00m$
  1599^I    [36mResult[39;49;00m := [34mFalse[39;49;00m;$
  1600^I  [34mExit[39;49;00m [34mend[39;49;00m;$
  1601^I$
  1602^I  [36mAssignFile[39;49;00m(F, FileName);$
  1603^I  [37m{$I-}[39;49;00m[36mRewrite[39;49;00m(F, [34m1[39;49;00m);[37m{$I+}[39;49;00m$
  1604^I  [34mif[39;49;00m [36mIOResult[39;49;00m = [34m0[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m$
  1605^I    [34mif[39;49;00m [36mLength[39;49;00m(Data) > [34m0[39;49;00m [34mthen[39;49;00m$
  1606^I      [36mBlockWrite[39;49;00m(F, Data[[34m0[39;49;00m], [36mLength[39;49;00m(Data));$
  1607^I    [36mCloseFile[39;49;00m(F);$
  1608^I    [36mResult[39;49;00m := [34mTrue[39;49;00m;$
  1609^I  [34mend[39;49;00m [34melse[39;49;00m$
  1610^I    [36mResult[39;49;00m := [34mFalse[39;49;00m;$
  1611^I[34mend[39;49;00m;$
  1612^I$
  1613^I[34mfunction[39;49;00m [32mLoadByteA[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m): TByteA;$
  1614^I[34mvar[39;49;00m$
  1615^I  F: [34mfile[39;49;00m;$
  1616^I[34mbegin[39;49;00m$
  1617^I  [36mAssignFile[39;49;00m(F, FileName);$
  1618^I  [37m{$I-}[39;49;00m[36mReset[39;49;00m(F, [34m1[39;49;00m);[37m{$I+}[39;49;00m$
  1619^I  [34mif[39;49;00m [36mIOResult[39;49;00m = [34m0[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m$
  1620^I    [36mSetLength[39;49;00m([36mResult[39;49;00m, [36mFileSize[39;49;00m(F));$
  1621^I    [34mif[39;49;00m [36mLength[39;49;00m([36mResult[39;49;00m) > [34m0[39;49;00m [34mthen[39;49;00m$
  1622^I      [36mBlockRead[39;49;00m(F, [36mResult[39;49;00m[[34m0[39;49;00m], [36mFileSize[39;49;00m(F));$
  1623^I    [36mCloseFile[39;49;00m(F);$
  1624^I  [34mend[39;49;00m [34melse[39;49;00m$
  1625^I    [36mSetLength[39;49;00m([36mResult[39;49;00m, [34m0[39;49;00m);$
  1626^I[34mend[39;49;00m;$
  1627^I$
  1628^I[34mfunction[39;49;00m [32mIsValidFileName[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
  1629^I[34mbegin[39;49;00m$
  1630^I  [36mResult[39;49;00m := (FileName <> [33m'[39;49;00m[33m'[39;49;00m) [34mand[39;49;00m [34mnot[39;49;00m CharIn(FileName, FileNameEnemies)$
  1631^I    [34mand[39;49;00m CharIn([36mTrim[39;49;00m(FileName), AllChars - [[33m'[39;49;00m[33m.[39;49;00m[33m'[39;49;00m]);$
  1632^I[34mend[39;49;00m;$
  1633^I$
  1634^I[34mfunction[39;49;00m [32mMakeValidFileName[39;49;00m(FileName: [34mstring[39;49;00m; [34mconst[39;49;00m [34mDefault[39;49;00m: [34mstring[39;49;00m = [33m'[39;49;00m[33mFile[39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;$
  1635^I[34mbegin[39;49;00m$
  1636^I  [34mif[39;49;00m FileName = [33m'[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m$
  1637^I    FileName := [34mDefault[39;49;00m;$
  1638^I$
  1639^I  [34mif[39;49;00m CharIn(FileName, FileNameEnemies) [34mthen[39;49;00m$
  1640^I    [36mResult[39;49;00m := ReplaceChars(FileName, FileNameEnemies, [33m'[39;49;00m[33m_[39;49;00m[33m'[39;49;00m)$
  1641^I  [34melse[39;49;00m [34mif[39;49;00m [34mnot[39;49;00m CharIn([36mTrim[39;49;00m(FileName), AllChars - [[33m'[39;49;00m[33m.[39;49;00m[33m'[39;49;00m]) [34mthen[39;49;00m$
  1642^I    [36mResult[39;49;00m := [34mDefault[39;49;00m$
  1643^I  [34melse[39;49;00m$
  1644^I    [36mResult[39;49;00m := FileName;$
  1645^I[34mend[39;49;00m;$
  1646^I$
  1647^I[34mfunction[39;49;00m [32mIsValidInteger[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
  1648^I[37m{const[39;49;00m$
  1649^I[37m  LowInt = '2147483648';[39;49;00m$
  1650^I[37m  HighInt = '2147483647';[39;49;00m$
  1651^I[37mvar[39;49;00m$
  1652^I[37m  len, RealLen, i, o: Integer;[39;49;00m$
  1653^I[37m  c: Char;[39;49;00m$
  1654^I[37mbegin[39;49;00m$
  1655^I[37m  Result := False;[39;49;00m$
  1656^I[37m  if S = '' then[39;49;00m$
  1657^I[37m    Exit;[39;49;00m$
  1658^I[37m[39;49;00m$
  1659^I[37m  len := Length(S);[39;49;00m$
  1660^I[37m  o := 1;[39;49;00m$
  1661^I[37m  [39;49;00m$
  1662^I[37m  if S[1] = '-' then begin[39;49;00m$
  1663^I[37m    if len = 1 then[39;49;00m$
  1664^I[37m      Exit;[39;49;00m$
  1665^I[37m    Inc(o);[39;49;00m$
  1666^I[37m    while (o <= len) and (S[o] = '0') do[39;49;00m$
  1667^I[37m      Inc(o);[39;49;00m$
  1668^I[37m    if o > len then[39;49;00m$
  1669^I[37m      Exit;[39;49;00m$
  1670^I[37m    if o < len then begin[39;49;00m$
  1671^I[37m      RealLen := len - o + 1;[39;49;00m$
  1672^I[37m      if RealLen > Length(LowInt) then[39;49;00m$
  1673^I[37m        Exit[39;49;00m$
  1674^I[37m      else if RealLen = Length(LowInt) then begin[39;49;00m$
  1675^I[37m        for i := 1 to Length(LowInt) do begin[39;49;00m$
  1676^I[37m          c := S[i + o - 1];[39;49;00m$
  1677^I[37m          if (c < '0') or (c > LowInt[i]) then[39;49;00m$
  1678^I[37m            Exit;[39;49;00m$
  1679^I[37m          if c in ['0'..Char((Byte(LowInt[i])-1))] then[39;49;00m$
  1680^I[37m            Break;[39;49;00m$
  1681^I[37m        end;[39;49;00m$
  1682^I[37m        Inc(o, i);[39;49;00m$
  1683^I[37m      end;[39;49;00m$
  1684^I[37m    end;[39;49;00m$
  1685^I[37m  end else begin[39;49;00m$
  1686^I[37m    while (o <= len) and (S[o] = '0') do[39;49;00m$
  1687^I[37m      Inc(o);[39;49;00m$
  1688^I[37m    if o <= len then begin[39;49;00m$
  1689^I[37m      RealLen := len - o + 1;[39;49;00m$
  1690^I[37m      if RealLen > Length(HighInt) then[39;49;00m$
  1691^I[37m        Exit[39;49;00m$
  1692^I[37m      else if RealLen = Length(HighInt) then begin[39;49;00m$
  1693^I[37m        for i := 1 to Length(HighInt) do begin[39;49;00m$
  1694^I[37m          c := S[i + o - 1];[39;49;00m$
  1695^I[37m          if (c < '0') or (c > HighInt[i]) then[39;49;00m$
  1696^I[37m            Exit;[39;49;00m$
  1697^I[37m          if c in ['0'..Char((Byte(HighInt[i])-1))] then[39;49;00m$
  1698^I[37m            Break;[39;49;00m$
  1699^I[37m        end;[39;49;00m$
  1700^I[37m        Inc(o, i);[39;49;00m$
  1701^I[37m      end;[39;49;00m$
  1702^I[37m    end;[39;49;00m$
  1703^I[37m  end;[39;49;00m$
  1704^I[37m[39;49;00m$
  1705^I[37m  for i := o to len do[39;49;00m$
  1706^I[37m    if not (S[i] in ['0'..'9']) then[39;49;00m$
  1707^I[37m      Exit;[39;49;00m$
  1708^I[37m[39;49;00m$
  1709^I[37m  Result := True;  }[39;49;00m$
  1710^I[34mvar[39;49;00m$
  1711^I  i: [36mInt64[39;49;00m;$
  1712^I[34mbegin[39;49;00m$
  1713^I  i := [36mStrToInt64Def[39;49;00m(S, [36mHigh[39;49;00m([36mInt64[39;49;00m));$
  1714^I  [36mResult[39;49;00m := (i >= [36mLow[39;49;00m([36mInteger[39;49;00m)) [34mand[39;49;00m (i <= [36mHigh[39;49;00m([36mInteger[39;49;00m));$
  1715^I[34mend[39;49;00m;$
  1716^I$
  1717^I[34mfunction[39;49;00m [32mIsValidCardinal[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
  1718^I[37m{const[39;49;00m$
  1719^I[37m  HighCard = '4294967295';[39;49;00m$
  1720^I[37mvar[39;49;00m$
  1721^I[37m  len, RealLen, i, o: Integer;[39;49;00m$
  1722^I[37mbegin[39;49;00m$
  1723^I[37m  Result := False;[39;49;00m$
  1724^I[37m  if S = '' then[39;49;00m$
  1725^I[37m    Exit;[39;49;00m$
  1726^I[37m[39;49;00m$
  1727^I[37m  len := Length(S);[39;49;00m$
  1728^I[37m  o := 1;[39;49;00m$
  1729^I[37m  [39;49;00m$
  1730^I[37m  while (o <= len) and (S[o] = '0') do[39;49;00m$
  1731^I[37m    Inc(o);[39;49;00m$
  1732^I[37m  if o <= len then begin[39;49;00m$
  1733^I[37m    RealLen := len - o + 1;[39;49;00m$
  1734^I[37m    if RealLen > Length(HighCard) then[39;49;00m$
  1735^I[37m      Exit[39;49;00m$
  1736^I[37m    else if RealLen = Length(HighCard) then begin[39;49;00m$
  1737^I[37m      for i := 1 to Length(HighCard) do begin[39;49;00m$
  1738^I[37m        if S[i + o - 1] > HighCard[i] then[39;49;00m$
  1739^I[37m          Exit;[39;49;00m$
  1740^I[37m        if S[i + o - 1] in ['0'..Char((Byte(HighCard[i])-1))] then[39;49;00m$
  1741^I[37m          Break;[39;49;00m$
  1742^I[37m      end;[39;49;00m$
  1743^I[37m      Inc(o, i);[39;49;00m$
  1744^I[37m    end;[39;49;00m$
  1745^I[37m  end;[39;49;00m$
  1746^I[37m[39;49;00m$
  1747^I[37m  for i := o to len do[39;49;00m$
  1748^I[37m    if not (S[i] in ['0'..'9']) then[39;49;00m$
  1749^I[37m      Exit;[39;49;00m$
  1750^I[37m[39;49;00m$
  1751^I[37m  Result := True;  }[39;49;00m$
  1752^I[34mvar[39;49;00m$
  1753^I  i: [36mInt64[39;49;00m;$
  1754^I[34mbegin[39;49;00m$
  1755^I  i := [36mStrToInt64Def[39;49;00m(S, -[34m1[39;49;00m);$
  1756^I  [36mResult[39;49;00m := (i >= [34m0[39;49;00m) [34mand[39;49;00m (i <= [36mHigh[39;49;00m([36mCardinal[39;49;00m));$
  1757^I[34mend[39;49;00m;$
  1758^I$
  1759^I[34mfunction[39;49;00m [32mStrOfBool[39;49;00m(flag: [36mBoolean[39;49;00m; [34mconst[39;49;00m TrueStr: [34mstring[39;49;00m = [33m'[39;49;00m[33mTrue[39;49;00m[33m'[39;49;00m;$
  1760^I  [34mconst[39;49;00m FalseStr: [34mstring[39;49;00m = [33m'[39;49;00m[33mFalse[39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;$
  1761^I[34mbegin[39;49;00m$
  1762^I  [34mif[39;49;00m Flag [34mthen[39;49;00m$
  1763^I    [36mResult[39;49;00m := TrueStr$
  1764^I  [34melse[39;49;00m$
  1765^I    [36mResult[39;49;00m := FalseStr;$
  1766^I[34mend[39;49;00m;$
  1767^I$
  1768^I[34mfunction[39;49;00m [32mStrOfInt[39;49;00m(i: [36mInteger[39;49;00m): [34mstring[39;49;00m;$
  1769^I[34mbegin[39;49;00m$
  1770^I[37m{  if i = 0 then begin[39;49;00m$
  1771^I[37m    Result := '0';[39;49;00m$
  1772^I[37m  Exit end;[39;49;00m$
  1773^I[37m[39;49;00m$
  1774^I[37m  while i > 0 do begin[39;49;00m$
  1775^I[37m    Result := Char(Byte('0') + (i mod 10)) + Result;[39;49;00m$
  1776^I[37m    i := i div 10;[39;49;00m$
  1777^I[37m  end;}[39;49;00m$
  1778^I  [36mResult[39;49;00m := [36mIntToStr[39;49;00m(i);$
  1779^I[34mend[39;49;00m;$
  1780^I$
  1781^I[34mfunction[39;49;00m [32mCardOfStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [36mCardinal[39;49;00m;$
  1782^I[34mvar[39;49;00m$
  1783^I  Res: [36mInt64[39;49;00m;$
  1784^I[34mbegin[39;49;00m$
  1785^I  Res := [36mStrToInt64Def[39;49;00m(S, -[34m1[39;49;00m);$
  1786^I  [34mif[39;49;00m Res > [36mHigh[39;49;00m([36mCardinal[39;49;00m) [34mthen[39;49;00m$
  1787^I    Res := [36mHigh[39;49;00m([36mCardinal[39;49;00m)$
  1788^I  [34melse[39;49;00m [34mif[39;49;00m Res < [34m0[39;49;00m [34mthen[39;49;00m$
  1789^I    Res := [34m0[39;49;00m;$
  1790^I  [36mResult[39;49;00m := [36mCardinal[39;49;00m(Res);$
  1791^I[34mend[39;49;00m;$
  1792^I$
  1793^I[34mfunction[39;49;00m [32mHexOrd[39;49;00m(Hex: [36mChar[39;49;00m): THex;$
  1794^I[34mbegin[39;49;00m$
  1795^I  [34mcase[39;49;00m Hex [34mof[39;49;00m$
  1796^I    [33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m..[33m'[39;49;00m[33m9[39;49;00m[33m'[39;49;00m:$
  1797^I      [36mResult[39;49;00m := [36mByte[39;49;00m(Hex) - [34m48[39;49;00m;$
  1798^I    [33m'[39;49;00m[33mA[39;49;00m[33m'[39;49;00m..[33m'[39;49;00m[33mF[39;49;00m[33m'[39;49;00m:$
  1799^I      [36mResult[39;49;00m := [36mByte[39;49;00m(Hex) - [34m55[39;49;00m;$
  1800^I    [33m'[39;49;00m[33ma[39;49;00m[33m'[39;49;00m..[33m'[39;49;00m[33mf[39;49;00m[33m'[39;49;00m:$
  1801^I      [36mResult[39;49;00m := [36mByte[39;49;00m(Hex) - [34m87[39;49;00m;$
  1802^I    [34melse[39;49;00m$
  1803^I      [36mResult[39;49;00m := [34m0[39;49;00m;$
  1804^I  [34mend[39;49;00m;$
  1805^I[34mend[39;49;00m;$
  1806^I$
  1807^I[34mfunction[39;49;00m [32mByteOfHex[39;49;00m(Hex: THexByteStr): [36mByte[39;49;00m;$
  1808^I[34mbegin[39;49;00m$
  1809^I  [36mResult[39;49;00m := (HexOrd(Hex[[34m1[39;49;00m]) [34mshl[39;49;00m [34m4[39;49;00m) + HexOrd(Hex[[34m2[39;49;00m]);$
  1810^I[34mend[39;49;00m;$
  1811^I$
  1812^I[34mfunction[39;49;00m [32mDecOfHex[39;49;00m([34mconst[39;49;00m Hex: [34mstring[39;49;00m): [34mstring[39;49;00m;$
  1813^I[34mbegin[39;49;00m$
  1814^I  [36mResult[39;49;00m := [36mIntToStr[39;49;00m(CardOfHex(Hex));$
  1815^I[34mend[39;49;00m;$
  1816^I$
  1817^I[34mfunction[39;49;00m [32mHexOfByte[39;49;00m(b: [36mByte[39;49;00m): THexByteStr;$
  1818^I[34mbegin[39;49;00m$
  1819^I  [36mResult[39;49;00m := HexChar[(b [34mand[39;49;00m [34m$F0[39;49;00m) [34mshr[39;49;00m [34m4[39;49;00m]$
  1820^I          + HexChar[ b [34mand[39;49;00m [34m$0F[39;49;00m       ];$
  1821^I[34mend[39;49;00m;$
  1822^I$
  1823^I[37m{function HexOfCard2(c: Cardinal): string;[39;49;00m$
  1824^I[37mvar[39;49;00m$
  1825^I[37m  Data: array[0..(1 shl 4) - 1] of Char;[39;49;00m$
  1826^I[37m  i: Integer;[39;49;00m$
  1827^I[37mbegin[39;49;00m$
  1828^I[37m  for i := 0 to (1 shl 4) - 1 do[39;49;00m$
  1829^I[37m    if i < 10 then[39;49;00m$
  1830^I[37m      Data[i] := Char(Ord('0') + i)[39;49;00m$
  1831^I[37m    else[39;49;00m$
  1832^I[37m      Data[i] := Char(Ord('A') + i - 10);[39;49;00m$
  1833^I[37m[39;49;00m$
  1834^I[37m  Result := Data[(c and (((1 shl (1 shl 2)) - 1) shl (7 shl 2))) shr (7 shl 2)][39;49;00m$
  1835^I[37m          + Data[(c and (((1 shl (1 shl 2)) - 1) shl (6 shl 2))) shr (6 shl 2)][39;49;00m$
  1836^I[37m          + Data[(c and (((1 shl (1 shl 2)) - 1) shl (5 shl 2))) shr (5 shl 2)][39;49;00m$
  1837^I[37m          + Data[(c and (((1 shl (1 shl 2)) - 1) shl (4 shl 2))) shr (4 shl 2)][39;49;00m$
  1838^I[37m          + Data[(c and (((1 shl (1 shl 2)) - 1) shl (3 shl 2))) shr (3 shl 2)][39;49;00m$
  1839^I[37m          + Data[(c and (((1 shl (1 shl 2)) - 1) shl (2 shl 2))) shr (2 shl 2)][39;49;00m$
  1840^I[37m          + Data[(c and (((1 shl (1 shl 2)) - 1) shl (1 shl 2))) shr (1 shl 2)][39;49;00m$
  1841^I[37m          + Data[(c and (((1 shl (1 shl 2)) - 1) shl (0 shl 2))) shr (0 shl 2)];[39;49;00m$
  1842^I[37mend; }[39;49;00m$
  1843^I$
  1844^I[34mfunction[39;49;00m [32mHexOfCard[39;49;00m(i: [36mCardinal[39;49;00m): [34mstring[39;49;00m;$
  1845^I[34mvar[39;49;00m$
  1846^I  a: [36mCardinal[39;49;00m;$
  1847^I[34mbegin[39;49;00m$
  1848^I  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
  1849^I  [34mwhile[39;49;00m i > [34m0[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m$
  1850^I    a := i [34mand[39;49;00m [34m$F[39;49;00m;$
  1851^I    [36mResult[39;49;00m := HexChar[a] + [36mResult[39;49;00m;$
  1852^I    i := i [34mshr[39;49;00m [34m4[39;49;00m;$
  1853^I  [34mend[39;49;00m;$
  1854^I[34mend[39;49;00m;$
  1855^I$
  1856^I[34mfunction[39;49;00m [32mHexOfCard[39;49;00m(i: [36mCardinal[39;49;00m; Digits: [36mInteger[39;49;00m): [34mstring[39;49;00m;$
  1857^I[34mvar[39;49;00m$
  1858^I  a: [36mCardinal[39;49;00m;$
  1859^I[34mbegin[39;49;00m$
  1860^I  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
  1861^I  [34mwhile[39;49;00m i > [34m0[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m$
  1862^I    a := i [34mand[39;49;00m [34m$F[39;49;00m;$
  1863^I    [36mResult[39;49;00m := HexChar[a] + [36mResult[39;49;00m;$
  1864^I    i := i [34mshr[39;49;00m [34m4[39;49;00m;$
  1865^I  [34mend[39;49;00m;$
  1866^I  [36mResult[39;49;00m := MulStr([33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m, Digits - [36mLength[39;49;00m([36mResult[39;49;00m)) + [36mResult[39;49;00m;$
  1867^I[34mend[39;49;00m;$
  1868^I$
  1869^I[34mfunction[39;49;00m [32mPascalHexArray[39;49;00m(a: TByteA; [34mName[39;49;00m: [34mstring[39;49;00m): [34mstring[39;49;00m;$
  1870^I[34mvar[39;49;00m$
  1871^I  i, len: [36mInteger[39;49;00m;$
  1872^I[34mbegin[39;49;00m$
  1873^I  [36mResult[39;49;00m := [33m'[39;49;00m[33mconst[39;49;00m[33m'[39;49;00m + EOL +$
  1874^I    [33m'[39;49;00m[33m  [39;49;00m[33m'[39;49;00m + Name + [33m'[39;49;00m[33m: array[0..[39;49;00m[33m'[39;49;00m + [36mIntToStr[39;49;00m([36mHigh[39;49;00m(a)) + [33m'[39;49;00m[33m] of Byte = ([39;49;00m[33m'[39;49;00m;$
  1875^I$
  1876^I  len := [36mLength[39;49;00m(a);$
  1877^I  [34mfor[39;49;00m i := [34m0[39;49;00m [34mto[39;49;00m len-[34m1[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m$
  1878^I    [34mif[39;49;00m (i [34mmod[39;49;00m [34m19[39;49;00m) = [34m0[39;49;00m [34mthen[39;49;00m$
  1879^I      [36mResult[39;49;00m := [36mResult[39;49;00m + EOL + [33m'[39;49;00m[33m  [39;49;00m[33m'[39;49;00m + [33m'[39;49;00m[33m  [39;49;00m[33m'[39;49;00m;$
  1880^I    [36mResult[39;49;00m := [36mResult[39;49;00m + [33m'[39;49;00m[33m$[39;49;00m[33m'[39;49;00m + HexOfByte(a[i]);$
  1881^I    [34mif[39;49;00m i < len-[34m1[39;49;00m [34mthen[39;49;00m$
  1882^I      [36mResult[39;49;00m := [36mResult[39;49;00m + [33m'[39;49;00m[33m,[39;49;00m[33m'[39;49;00m;$
  1883^I  [34mend[39;49;00m;$
  1884^I  [36mResult[39;49;00m := [36mResult[39;49;00m + EOL + [33m'[39;49;00m[33m  );[39;49;00m[33m'[39;49;00m;$
  1885^I[34mend[39;49;00m;$
  1886^I$
  1887^I[34mfunction[39;49;00m [32mHexOfByteA[39;49;00m(a: TByteA; Blocks: [36mInteger[39;49;00m = [34m1[39;49;00m;$
  1888^I  [34mconst[39;49;00m Splitter: [34mstring[39;49;00m = [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;$
  1889^I[34mvar[39;49;00m$
  1890^I  i: [36mInteger[39;49;00m;$
  1891^I[34mbegin[39;49;00m$
  1892^I  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
  1893^I$
  1894^I  [34mif[39;49;00m Blocks > [34m0[39;49;00m [34mthen[39;49;00m$
  1895^I    [34mfor[39;49;00m i := [34m0[39;49;00m [34mto[39;49;00m [36mHigh[39;49;00m(a) [34mdo[39;49;00m [34mbegin[39;49;00m$
  1896^I      [36mResult[39;49;00m := [36mResult[39;49;00m + HexOfByte(a[i]);$
  1897^I      [34mif[39;49;00m i < [36mHigh[39;49;00m(a) [34mthen[39;49;00m$
  1898^I        [34mif[39;49;00m ((i+[34m1[39;49;00m) [34mmod[39;49;00m Blocks) = [34m0[39;49;00m [34mthen[39;49;00m$
  1899^I          [36mResult[39;49;00m := [36mResult[39;49;00m + Splitter;$
  1900^I    [34mend[39;49;00m$
  1901^I  [34melse[39;49;00m$
  1902^I    [34mfor[39;49;00m i := [34m0[39;49;00m [34mto[39;49;00m [36mHigh[39;49;00m(a) [34mdo[39;49;00m$
  1903^I      [36mResult[39;49;00m := [36mResult[39;49;00m + HexOfByte(a[i]);$
  1904^I[34mend[39;49;00m;$
  1905^I$
  1906^I[34mfunction[39;49;00m [32mBinOfByteA[39;49;00m(a: TByteA; Blocks: [36mInteger[39;49;00m = [34m4[39;49;00m;$
  1907^I  [34mconst[39;49;00m Splitter: [34mstring[39;49;00m = [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m): [34mstring[39;49;00m;$
  1908^I[34mvar[39;49;00m$
  1909^I  i, [36mmax[39;49;00m: [36mInteger[39;49;00m;$
  1910^I  Bit: [36mBoolean[39;49;00m;$
  1911^I[34mbegin[39;49;00m$
  1912^I  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
  1913^I$
  1914^I  [34mif[39;49;00m Blocks > [34m0[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m$
  1915^I    [36mmax[39;49;00m := [34m8[39;49;00m * ([36mHigh[39;49;00m(a)) + [34m7[39;49;00m;$
  1916^I    [34mfor[39;49;00m i := [34m0[39;49;00m [34mto[39;49;00m [36mmax[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m$
  1917^I      Bit := [34m7[39;49;00m-(i [34mmod[39;49;00m [34m8[39;49;00m) [34min[39;49;00m TBitSet(a[i [34mdiv[39;49;00m [34m8[39;49;00m]);$
  1918^I      [36mResult[39;49;00m := [36mResult[39;49;00m + [36mChar[39;49;00m([36mByte[39;49;00m([33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m) + [36mByte[39;49;00m(Bit));$
  1919^I      [34mif[39;49;00m i < [36mmax[39;49;00m [34mthen[39;49;00m$
  1920^I        [34mif[39;49;00m ((i+[34m1[39;49;00m) [34mmod[39;49;00m Blocks) = [34m0[39;49;00m [34mthen[39;49;00m$
  1921^I          [36mResult[39;49;00m := [36mResult[39;49;00m + Splitter;$
  1922^I    [34mend[39;49;00m;$
  1923^I  [34mend[39;49;00m [34melse[39;49;00m$
  1924^I    [34mfor[39;49;00m i := [34m0[39;49;00m [34mto[39;49;00m [36mHigh[39;49;00m(a) [34mdo[39;49;00m$
  1925^I      [36mResult[39;49;00m := [36mResult[39;49;00m + [36mChar[39;49;00m([36mByte[39;49;00m([33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m) + a[i] [34mshr[39;49;00m (i [34mand[39;49;00m [34m8[39;49;00m));$
  1926^I[34mend[39;49;00m;$
  1927^I$
  1928^I[34mfunction[39;49;00m [32mCardOfHex[39;49;00m(Hex: [34mstring[39;49;00m): [36mCardinal[39;49;00m;$
  1929^I[34mvar[39;49;00m$
  1930^I  i: [36mInteger[39;49;00m;$
  1931^I[34mbegin[39;49;00m$
  1932^I  [36mResult[39;49;00m := [34m0[39;49;00m;$
  1933^I  Hex := [36mCopy[39;49;00m(ExtractChars(Hex, HexadecimalChars), [34m1[39;49;00m, [34m8[39;49;00m);$
  1934^I$
  1935^I  [34mfor[39;49;00m i := [34m1[39;49;00m [34mto[39;49;00m [36mLength[39;49;00m(Hex) [34mdo[39;49;00m$
  1936^I    [34mif[39;49;00m Hex[i] <> [33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m$
  1937^I      [36mInc[39;49;00m([36mResult[39;49;00m, HexOrd(Hex[i]) [34mshl[39;49;00m (([36mLength[39;49;00m(Hex) - i) [34mshl[39;49;00m [34m2[39;49;00m));$
  1938^I[34mend[39;49;00m;$
  1939^I$
  1940^I[34mfunction[39;49;00m [32mIntOfBin[39;49;00m(Bin: [34mstring[39;49;00m): [36mCardinal[39;49;00m;$
  1941^I[34mvar[39;49;00m$
  1942^I  i: [36mInteger[39;49;00m;$
  1943^I[34mbegin[39;49;00m$
  1944^I  [36mResult[39;49;00m := [34m0[39;49;00m;$
  1945^I  Bin := [36mCopy[39;49;00m(ExtractChars(Bin, BinaryChars), [34m1[39;49;00m, [34m32[39;49;00m);$
  1946^I$
  1947^I  [34mfor[39;49;00m i := [36mLength[39;49;00m(Bin) [34mdownto[39;49;00m [34m1[39;49;00m [34mdo[39;49;00m$
  1948^I    [34mif[39;49;00m Bin[i] = [33m'[39;49;00m[33m1[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m$
  1949^I      [36mInc[39;49;00m([36mResult[39;49;00m, [34m1[39;49;00m [34mshl[39;49;00m ([36mLength[39;49;00m(Bin) - i));$
  1950^I[34mend[39;49;00m;$
  1951^I$
  1952^I[34mfunction[39;49;00m [32mBinOfInt[39;49;00m(n: [36mCardinal[39;49;00m): [34mstring[39;49;00m;$
  1953^I[34mvar[39;49;00m$
  1954^I  a: [36mInteger[39;49;00m;$
  1955^I[34mbegin[39;49;00m$
  1956^I  [34mif[39;49;00m n = [34m0[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m$
  1957^I    [36mResult[39;49;00m := [33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m;$
  1958^I  [34mexit[39;49;00m; [34mend[39;49;00m;$
  1959^I$
  1960^I  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
  1961^I  [34mwhile[39;49;00m n > [34m0[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m$
  1962^I    a := n [34mand[39;49;00m [34m1[39;49;00m;$
  1963^I    [36mResult[39;49;00m := [36mChar[39;49;00m(a + [36mByte[39;49;00m([33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m)) + [36mResult[39;49;00m;$
  1964^I    n := n [34mshr[39;49;00m [34m1[39;49;00m;$
  1965^I  [34mend[39;49;00m;$
  1966^I[34mend[39;49;00m;$
  1967^I$
  1968^I[34mfunction[39;49;00m [32mBinOfIntFill[39;49;00m(n: [36mCardinal[39;49;00m; MinCount: [36mInteger[39;49;00m = [34m8[39;49;00m): [34mstring[39;49;00m;$
  1969^I[34mvar[39;49;00m$
  1970^I  a: [36mInteger[39;49;00m;$
  1971^I[34mbegin[39;49;00m$
  1972^I  [34mif[39;49;00m n = [34m0[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m$
  1973^I    [36mResult[39;49;00m := MulStr([33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m, MinCount);$
  1974^I  [34mExit[39;49;00m; [34mend[39;49;00m;$
  1975^I$
  1976^I  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
  1977^I  [34mwhile[39;49;00m n > [34m0[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m$
  1978^I    a := n [34mand[39;49;00m [34m1[39;49;00m;$
  1979^I    [36mResult[39;49;00m := [36mChar[39;49;00m(a + [36mByte[39;49;00m([33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m)) + [36mResult[39;49;00m;$
  1980^I    n := n [34mshr[39;49;00m [34m1[39;49;00m;$
  1981^I  [34mend[39;49;00m;$
  1982^I  [36mResult[39;49;00m := MulStr([33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m, MinCount - [36mLength[39;49;00m([36mResult[39;49;00m)) + [36mResult[39;49;00m;$
  1983^I[34mend[39;49;00m;$
  1984^I$
  1985^I[34mfunction[39;49;00m [32mBaseNOfInt[39;49;00m(I: [36mCardinal[39;49;00m; B: TBaseN): [34mstring[39;49;00m;$
  1986^I[34mvar[39;49;00m$
  1987^I  a: [36mInteger[39;49;00m;$
  1988^I[34mbegin[39;49;00m$
  1989^I  [34mif[39;49;00m (B < [34m2[39;49;00m) [34mor[39;49;00m (i = [34m0[39;49;00m) [34mthen[39;49;00m [34mbegin[39;49;00m$
  1990^I    [36mResult[39;49;00m := [33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m;$
  1991^I  [34mExit[39;49;00m; [34mend[39;49;00m;$
  1992^I$
  1993^I  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
  1994^I  [34mwhile[39;49;00m i > [34m0[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m$
  1995^I    a := i [34mmod[39;49;00m B;$
  1996^I    [36mResult[39;49;00m := BaseNChar[a] + [36mResult[39;49;00m;$
  1997^I    i := i [34mdiv[39;49;00m B;$
  1998^I  [34mend[39;49;00m;$
  1999^I[34mend[39;49;00m;$
  2000^I$
  2001^I[34mfunction[39;49;00m [32mIntOfBaseN[39;49;00m(V: [34mstring[39;49;00m; B: TBaseN): [36mCardinal[39;49;00m;$
  2002^I[34mvar[39;49;00m$
  2003^I  i: [36mInteger[39;49;00m;$
  2004^I  F: [36mCardinal[39;49;00m;$
  2005^I  c: [36mByte[39;49;00m;$
  2006^I[34mbegin[39;49;00m$
  2007^I  [36mResult[39;49;00m := [34m0[39;49;00m;$
  2008^I  V := TrimAll(V);$
  2009^I  F := [34m1[39;49;00m;$
  2010^I  [34mfor[39;49;00m i := [36mLength[39;49;00m(V) [34mdownto[39;49;00m [34m1[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m$
  2011^I    c := [36mByte[39;49;00m([36mUpCase[39;49;00m(V[i]));$
  2012^I    [34mcase[39;49;00m [36mChar[39;49;00m(c) [34mof[39;49;00m$
  2013^I      [33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m..[33m'[39;49;00m[33m9[39;49;00m[33m'[39;49;00m: c := c - [34m48[39;49;00m;$
  2014^I      [33m'[39;49;00m[33mA[39;49;00m[33m'[39;49;00m..[33m'[39;49;00m[33mZ[39;49;00m[33m'[39;49;00m: c := c - [34m55[39;49;00m;$
  2015^I    [34mend[39;49;00m;$
  2016^I    [34mif[39;49;00m c < B [34mthen[39;49;00m$
  2017^I      [36mResult[39;49;00m := [36mResult[39;49;00m + [36mByte[39;49;00m(c) * F;$
  2018^I    F := F * B;$
  2019^I  [34mend[39;49;00m;$
  2020^I[34mend[39;49;00m;$
  2021^I$
  2022^I[34mfunction[39;49;00m [32mKeepIn[39;49;00m(i, Bottom, Top: [36mVariant[39;49;00m): [36mVariant[39;49;00m;$
  2023^I[34mbegin[39;49;00m$
  2024^I  [36mResult[39;49;00m := i;$
  2025^I  [34mif[39;49;00m [36mResult[39;49;00m > Top [34mthen[39;49;00m$
  2026^I    [36mResult[39;49;00m := Top$
  2027^I  [34melse[39;49;00m [34mif[39;49;00m [36mResult[39;49;00m < Bottom [34mthen[39;49;00m$
  2028^I    [36mResult[39;49;00m := Bottom;$
  2029^I[34mend[39;49;00m;$
  2030^I$
  2031^I[34mfunction[39;49;00m [32mInRange[39;49;00m(Value, Bottom, Top: [36mVariant[39;49;00m): [36mBoolean[39;49;00m;$
  2032^I[34mbegin[39;49;00m$
  2033^I  [36mResult[39;49;00m := (Value >= Bottom) [34mand[39;49;00m (Value <= Top);$
  2034^I[34mend[39;49;00m;$
  2035^I$
  2036^I[34mfunction[39;49;00m [32mInStrictRange[39;49;00m(Value, Bottom, Top: [36mVariant[39;49;00m): [36mBoolean[39;49;00m;$
  2037^I[34mbegin[39;49;00m$
  2038^I  [36mResult[39;49;00m := (Value > Bottom) [34mand[39;49;00m (Value < Top);$
  2039^I[34mend[39;49;00m;$
  2040^I$
  2041^I[34mfunction[39;49;00m [32mMin[39;49;00m([34mconst[39;49;00m A, B: [36mInteger[39;49;00m): [36mInteger[39;49;00m;$
  2042^I[34mbegin[39;49;00m$
  2043^I  [34mif[39;49;00m A < B [34mthen[39;49;00m$
  2044^I    [36mResult[39;49;00m := A$
  2045^I  [34melse[39;49;00m$
  2046^I    [36mResult[39;49;00m := B;$
  2047^I[34mend[39;49;00m;$
  2048^I$
  2049^I[34mfunction[39;49;00m [32mMin[39;49;00m([34mconst[39;49;00m A: TIntA): [36mInteger[39;49;00m;$
  2050^I[34mvar[39;49;00m$
  2051^I  i: [36mInteger[39;49;00m;$
  2052^I[34mbegin[39;49;00m$
  2053^I  [36mResult[39;49;00m := [34m0[39;49;00m;$
  2054^I  [34mif[39;49;00m [36mLength[39;49;00m(A) = [34m0[39;49;00m [34mthen[39;49;00m$
  2055^I    [34mExit[39;49;00m;$
  2056^I$
  2057^I  [36mResult[39;49;00m := A[[34m0[39;49;00m];$
  2058^I  [34mfor[39;49;00m i := [34m1[39;49;00m [34mto[39;49;00m [36mHigh[39;49;00m(A) [34mdo[39;49;00m$
  2059^I    [34mif[39;49;00m A[i] < [36mResult[39;49;00m [34mthen[39;49;00m$
  2060^I      [36mResult[39;49;00m := A[i];$
  2061^I[34mend[39;49;00m;$
  2062^I$
  2063^I[34mfunction[39;49;00m [32mMax[39;49;00m([34mconst[39;49;00m A, B: [36mInteger[39;49;00m): [36mInteger[39;49;00m;$
  2064^I[34mbegin[39;49;00m$
  2065^I  [34mif[39;49;00m A > B [34mthen[39;49;00m$
  2066^I    [36mResult[39;49;00m := A$
  2067^I  [34melse[39;49;00m$
  2068^I    [36mResult[39;49;00m := B;$
  2069^I[34mend[39;49;00m;$
  2070^I$
  2071^I[34mfunction[39;49;00m [32mMax[39;49;00m([34mconst[39;49;00m A: TIntA): [36mInteger[39;49;00m;$
  2072^I[34mvar[39;49;00m$
  2073^I  i: [36mInteger[39;49;00m;$
  2074^I[34mbegin[39;49;00m$
  2075^I  [36mResult[39;49;00m := [34m0[39;49;00m;$
  2076^I  [34mif[39;49;00m [36mLength[39;49;00m(A) = [34m0[39;49;00m [34mthen[39;49;00m$
  2077^I    [34mExit[39;49;00m;$
  2078^I$
  2079^I  [36mResult[39;49;00m := A[[34m0[39;49;00m];$
  2080^I  [34mfor[39;49;00m i := [34m1[39;49;00m [34mto[39;49;00m [36mHigh[39;49;00m(A) [34mdo[39;49;00m$
  2081^I    [34mif[39;49;00m A[i] > [36mResult[39;49;00m [34mthen[39;49;00m$
  2082^I      [36mResult[39;49;00m := A[i];$
  2083^I[34mend[39;49;00m;$
  2084^I$
  2085^I[34mfunction[39;49;00m [32mRangesOfStr[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): TRanges;$
  2086^I[34mvar[39;49;00m$
  2087^I  SL: TStringList;$
  2088^I  r, b, t: [34mstring[39;49;00m;$
  2089^I  i, p: [36mInteger[39;49;00m;$
  2090^I$
  2091^I  [34mfunction[39;49;00m [32mTryStrToCard[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m; out Value: [36mCardinal[39;49;00m): [36mBoolean[39;49;00m;$
  2092^I  [34mvar[39;49;00m$
  2093^I    E: [36mInteger[39;49;00m;$
  2094^I  [34mbegin[39;49;00m$
  2095^I    [36mVal[39;49;00m(S, Value, E);$
  2096^I    [36mResult[39;49;00m := E = [34m0[39;49;00m;$
  2097^I  [34mend[39;49;00m;$
  2098^I$
  2099^I[34mbegin[39;49;00m$
  2100^I  [36mResult[39;49;00m := [34mnil[39;49;00m;$
  2101^I  SL := TStringList.Create;$
  2102^I  [34mtry[39;49;00m$
  2103^I    Split(S, RangesSeparator, SL);$
  2104^I    [36mSetLength[39;49;00m([36mResult[39;49;00m, SL.Count);$
  2105^I    [34mfor[39;49;00m i := [34m0[39;49;00m [34mto[39;49;00m SL.Count-[34m1[39;49;00m [34mdo[39;49;00m [34mbegin[39;49;00m$
  2106^I      r := SL[i];$
  2107^I      [34mwith[39;49;00m [36mResult[39;49;00m[i] [34mdo[39;49;00m [34mbegin[39;49;00m$
  2108^I        p := CharPos(RangeInnerSeparator, r);$
  2109^I        Simple := p = [34m0[39;49;00m; [37m// no '-' found[39;49;00m$
  2110^I        [34mif[39;49;00m Simple [34mthen[39;49;00m [34mbegin[39;49;00m$
  2111^I          [34mif[39;49;00m r = RangeInfinite [34mthen[39;49;00m [34mbegin[39;49;00m [37m// * --> *-*[39;49;00m$
  2112^I            Simple := [34mFalse[39;49;00m;$
  2113^I            Bottom := [36mLow[39;49;00m(Bottom);$
  2114^I            Top := [36mHigh[39;49;00m(Top);$
  2115^I          [34mend[39;49;00m [34melse[39;49;00m [34mif[39;49;00m [34mnot[39;49;00m TryStrToCard(r, Value) [34mthen[39;49;00m$
  2116^I            [34mBreak[39;49;00m;$
  2117^I$
  2118^I        [34mend[39;49;00m [34melse[39;49;00m [34mbegin[39;49;00m$
  2119^I          TileStr(r, p, p, b, t);$
  2120^I$
  2121^I          [34mif[39;49;00m b = RangeInfinite [34mthen[39;49;00m$
  2122^I            Bottom := [36mLow[39;49;00m(Bottom)$
  2123^I          [34melse[39;49;00m [34mif[39;49;00m [34mnot[39;49;00m TryStrToCard(b, Bottom) [34mthen[39;49;00m$
  2124^I            [34mBreak[39;49;00m;$
  2125^I$
  2126^I          [34mif[39;49;00m t = RangeInfinite [34mthen[39;49;00m$
  2127^I            Top := [36mHigh[39;49;00m(Top)$
  2128^I          [34melse[39;49;00m [34mif[39;49;00m [34mnot[39;49;00m TryStrToCard(t, Top) [34mthen[39;49;00m$
  2129^I            [34mBreak[39;49;00m;$
  2130^I          [34mif[39;49;00m Bottom > Top [34mthen[39;49;00m [34mbegin[39;49;00m$
  2131^I            p := Bottom; Bottom := Top; Top := p;$
  2132^I          [34mend[39;49;00m;$
  2133^I        [34mend[39;49;00m;$
  2134^I      [34mend[39;49;00m;$
  2135^I    [34mend[39;49;00m;$
  2136^I$
  2137^I    [34mif[39;49;00m i <> SL.Count [34mthen[39;49;00m$
  2138^I      [36mResult[39;49;00m := [34mnil[39;49;00m;$
  2139^I$
  2140^I  [34mfinally[39;49;00m$
  2141^I    SL.Free;$
  2142^I  [34mend[39;49;00m;$
  2143^I[34mend[39;49;00m;$
  2144^I$
  2145^I[34mfunction[39;49;00m [32mInRanges[39;49;00m(Ranges: TRanges; TestValue: [36mCardinal[39;49;00m): [36mBoolean[39;49;00m;$
  2146^I[34mvar[39;49;00m$
  2147^I  i: [36mInteger[39;49;00m;$
  2148^I[34mbegin[39;49;00m$
  2149^I  [36mResult[39;49;00m := [34mTrue[39;49;00m;$
  2150^I$
  2151^I  [34mfor[39;49;00m i := [34m0[39;49;00m [34mto[39;49;00m [36mHigh[39;49;00m(Ranges) [34mdo[39;49;00m$
  2152^I    [34mwith[39;49;00m Ranges[i] [34mdo[39;49;00m$
  2153^I      [34mif[39;49;00m Simple [34mthen[39;49;00m [34mbegin[39;49;00m$
  2154^I        [34mif[39;49;00m TestValue = Value [34mthen[39;49;00m$
  2155^I          [34mExit[39;49;00m;$
  2156^I      [34mend[39;49;00m [34melse[39;49;00m [34mbegin[39;49;00m$
  2157^I        [34mif[39;49;00m [36mInRange[39;49;00m(TestValue, Bottom, Top) [34mthen[39;49;00m$
  2158^I          [34mExit[39;49;00m;$
  2159^I      [34mend[39;49;00m;$
  2160^I$
  2161^I  [36mResult[39;49;00m := [34mFalse[39;49;00m;$
  2162^I[34mend[39;49;00m;$
  2163^I$
  2164^I[34mprocedure[39;49;00m [32mWriteSL[39;49;00m(Strings: TStrings; [34mconst[39;49;00m Prefix: [34mstring[39;49;00m = [33m'[39;49;00m[33m'[39;49;00m;$
  2165^I  [34mconst[39;49;00m Suffix: [34mstring[39;49;00m = [33m'[39;49;00m[33m'[39;49;00m);$
  2166^I[34mvar[39;49;00m$
  2167^I  i: [36mInteger[39;49;00m;$
  2168^I[34mbegin[39;49;00m$
  2169^I  [34mfor[39;49;00m i := [34m0[39;49;00m [34mto[39;49;00m Strings.Count-[34m1[39;49;00m [34mdo[39;49;00m$
  2170^I    [36mWriteLn[39;49;00m(Prefix + Strings[i] + Suffix);$
  2171^I[34mend[39;49;00m;$
  2172^I$
  2173^I[34mfunction[39;49;00m [32mSuccess[39;49;00m(Res: [36mInteger[39;49;00m; ResultOnSuccess: [36mInteger[39;49;00m = ERROR_SUCCESS): [36mBoolean[39;49;00m;$
  2174^I[34mbegin[39;49;00m$
  2175^I  [36mResult[39;49;00m := (Res = ResultOnSuccess);$
  2176^I  LastSuccessRes := Res;$
  2177^I[34mend[39;49;00m;$
  2178^I$
  2179^I[34mfunction[39;49;00m [32mFailure[39;49;00m(Res: [36mInteger[39;49;00m; ResultOnSuccess: [36mInteger[39;49;00m = ERROR_SUCCESS): [36mBoolean[39;49;00m;$
  2180^I[34mbegin[39;49;00m$
  2181^I  [36mResult[39;49;00m := [34mnot[39;49;00m Success(Res, ResultOnSuccess);$
  2182^I[34mend[39;49;00m;$
  2183^I$
  2184^I[34mfunction[39;49;00m [32mExpandString[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m): [34mstring[39;49;00m;$
  2185^I[34mvar[39;49;00m$
  2186^I  Len: [36mInteger[39;49;00m;$
  2187^I  P, Res: [36mPChar[39;49;00m;$
  2188^I[34mbegin[39;49;00m$
  2189^I  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
  2190^I  P := [36mPChar[39;49;00m(S);$
  2191^I  Len := ExpandEnvironmentStrings(P, [34mnil[39;49;00m, [34m0[39;49;00m);$
  2192^I  [34mif[39;49;00m Len = [34m0[39;49;00m [34mthen[39;49;00m$
  2193^I    [34mExit[39;49;00m;$
  2194^I$
  2195^I  [36mGetMem[39;49;00m(Res, Len);$
  2196^I  ExpandEnvironmentStrings(P, Res, Len);$
  2197^I$
  2198^I  [36mResult[39;49;00m := Res;$
  2199^I  [36mFreeMem[39;49;00m(Res, Len);$
  2200^I[34mend[39;49;00m;$
  2201^I$
  2202^I[34mfunction[39;49;00m [32mFindAll[39;49;00m(Strings: TStrings; [34mconst[39;49;00m Mask: [34mstring[39;49;00m;$
  2203^I  ScanSubDirs: [36mBoolean[39;49;00m = [34mTrue[39;49;00m; Attributes: [36mInteger[39;49;00m = faFindEveryFile;$
  2204^I  FileReturn: TFileNameFunc = [34mnil[39;49;00m): [36mBoolean[39;49;00m;$
  2205^I[34mvar[39;49;00m$
  2206^I  Path, FileName: [34mstring[39;49;00m;$
  2207^I$
  2208^I  [34mprocedure[39;49;00m [32mScanDir[39;49;00m([34mconst[39;49;00m Path, FileName: [34mstring[39;49;00m);$
  2209^I  [34mvar[39;49;00m$
  2210^I    PSR: TSearchRec;$
  2211^I    Res: [36mInteger[39;49;00m;$
  2212^I$
  2213^I    [34mprocedure[39;49;00m [32mAdd[39;49;00m([34mconst[39;49;00m S: [34mstring[39;49;00m);$
  2214^I    [34mbegin[39;49;00m$
  2215^I      [34mif[39;49;00m S <> [33m'[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m$
  2216^I        Strings.Add(S);$
  2217^I    [34mend[39;49;00m;$
  2218^I$
  2219^I  [34mbegin[39;49;00m$
  2220^I    Res := [36mFindFirst[39;49;00m(Path + FileName, Attributes, PSR);$
  2221^I    [34mwhile[39;49;00m Success(Res, [34m0[39;49;00m) [34mdo[39;49;00m [34mbegin[39;49;00m$
  2222^I      [34mif[39;49;00m [36mAssigned[39;49;00m(FileReturn) [34mthen[39;49;00m$
  2223^I        Add(FileReturn(Path + PSR.Name))$
  2224^I      [34melse[39;49;00m$
  2225^I        Add(Path + PSR.Name);$
  2226^I      Res := [36mFindNext[39;49;00m(PSR);$
  2227^I    [34mend[39;49;00m;$
  2228^I    [36mFindClose[39;49;00m(PSR);$
  2229^I    [34mif[39;49;00m [34mnot[39;49;00m ScanSubDirs [34mthen[39;49;00m$
  2230^I      [34mExit[39;49;00m;$
  2231^I$
  2232^I    Res := [36mFindFirst[39;49;00m(Path + [33m'[39;49;00m[33m*[39;49;00m[33m'[39;49;00m, faDirectory, PSR);$
  2233^I    [34mwhile[39;49;00m Success(Res, [34m0[39;49;00m) [34mdo[39;49;00m [34mbegin[39;49;00m$
  2234^I      [34mif[39;49;00m (PSR.Attr [34mand[39;49;00m faDirectory > [34m0[39;49;00m)$
  2235^I       [34mand[39;49;00m (PSR.Name <> [33m'[39;49;00m[33m.[39;49;00m[33m'[39;49;00m) [34mand[39;49;00m (PSR.Name <> [33m'[39;49;00m[33m..[39;49;00m[33m'[39;49;00m) [34mthen[39;49;00m$
  2236^I        ScanDir(Path + PSR.Name + [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m, FileName);$
  2237^I      Res := [36mFindNext[39;49;00m(PSR);$
  2238^I    [34mend[39;49;00m;$
  2239^I    [36mFindClose[39;49;00m(PSR);$
  2240^I  [34mend[39;49;00m;$
  2241^I$
  2242^I[34mbegin[39;49;00m$
  2243^I  Strings.Clear;$
  2244^I  Path := ExtractPath(Mask);$
  2245^I  FileName := [36mExtractFileName[39;49;00m(Mask);$
  2246^I  ScanDir(Path, FileName);$
  2247^I  [36mResult[39;49;00m := Strings.Count > [34m0[39;49;00m;$
  2248^I[34mend[39;49;00m;$
  2249^I$
  2250^I[34mfunction[39;49;00m [32mFindAllFirst[39;49;00m([34mconst[39;49;00m Mask: [34mstring[39;49;00m; ScanSubDirs: [36mBoolean[39;49;00m = [34mTrue[39;49;00m;$
  2251^I  Attributes: [36mInteger[39;49;00m = faFindEveryFile): [34mstring[39;49;00m;$
  2252^I[34mvar[39;49;00m$
  2253^I  Path, FileName: [34mstring[39;49;00m;$
  2254^I$
  2255^I  [34mfunction[39;49;00m [32mScanDir[39;49;00m([34mconst[39;49;00m Path, FileName: [34mstring[39;49;00m): [36mBoolean[39;49;00m;$
  2256^I  [34mvar[39;49;00m$
  2257^I    PSR: TSearchRec;$
  2258^I    Res: [36mInteger[39;49;00m;$
  2259^I  [34mbegin[39;49;00m$
  2260^I    [36mResult[39;49;00m := [34mFalse[39;49;00m;$
  2261^I    [34mif[39;49;00m Success([36mFindFirst[39;49;00m(Path + FileName, Attributes, PSR), [34m0[39;49;00m) [34mthen[39;49;00m [34mbegin[39;49;00m$
  2262^I      FindAllFirst := Path + PSR.Name;$
  2263^I      [36mResult[39;49;00m := [34mTrue[39;49;00m;$
  2264^I      [36mFindClose[39;49;00m(PSR);$
  2265^I    [34mExit[39;49;00m; [34mend[39;49;00m;$
  2266^I    [34mif[39;49;00m [34mnot[39;49;00m ScanSubDirs [34mthen[39;49;00m$
  2267^I      [34mExit[39;49;00m;$
  2268^I$
  2269^I    Res := [36mFindFirst[39;49;00m(Path + [33m'[39;49;00m[33m*[39;49;00m[33m'[39;49;00m, faDirectory, PSR);$
  2270^I    [34mwhile[39;49;00m [34mnot[39;49;00m [36mResult[39;49;00m [34mand[39;49;00m Success(Res, [34m0[39;49;00m) [34mdo[39;49;00m [34mbegin[39;49;00m$
  2271^I      [34mif[39;49;00m (PSR.Attr [34mand[39;49;00m faDirectory > [34m0[39;49;00m)$
  2272^I       [34mand[39;49;00m (PSR.Name <> [33m'[39;49;00m[33m.[39;49;00m[33m'[39;49;00m) [34mand[39;49;00m (PSR.Name <> [33m'[39;49;00m[33m..[39;49;00m[33m'[39;49;00m) [34mthen[39;49;00m$
  2273^I        [36mResult[39;49;00m := ScanDir(Path + PSR.Name + [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m, FileName);$
  2274^I      Res := [36mFindNext[39;49;00m(PSR);$
  2275^I    [34mend[39;49;00m;$
  2276^I    [36mFindClose[39;49;00m(PSR);$
  2277^I  [34mend[39;49;00m;$
  2278^I[34mbegin[39;49;00m$
  2279^I  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
  2280^I  Path := ExtractPath(Mask);$
  2281^I  FileName := [36mExtractFileName[39;49;00m(Mask);$
  2282^I  ScanDir(Path, FileName);$
  2283^I[34mend[39;49;00m;$
  2284^I$
  2285^I[34mprocedure[39;49;00m [32mDeleteFiles[39;49;00m([34mconst[39;49;00m Mask: [34mstring[39;49;00m; ScanSubDirs: [36mBoolean[39;49;00m = [34mTrue[39;49;00m;$
  2286^I  Attributes: [36mInteger[39;49;00m = faFindEveryFile);$
  2287^I[34mvar[39;49;00m$
  2288^I  Path, FileName: [34mstring[39;49;00m;$
  2289^I$
  2290^I  [34mprocedure[39;49;00m [32mScanDir[39;49;00m([34mconst[39;49;00m Path, FileName: [34mstring[39;49;00m);$
  2291^I  [34mvar[39;49;00m$
  2292^I    PSR: TSearchRec;$
  2293^I    Res: [36mInteger[39;49;00m;$
  2294^I$
  2295^I    [34mprocedure[39;49;00m [32mTryDeleteFile[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m);$
  2296^I    [34mbegin[39;49;00m$
  2297^I      [34mtry[39;49;00m$
  2298^I        [36mDeleteFile[39;49;00m(Path + PSR.Name);$
  2299^I      [34mexcept[39;49;00m$
  2300^I      [34mend[39;49;00m;$
  2301^I    [34mend[39;49;00m;$
  2302^I$
  2303^I  [34mbegin[39;49;00m$
  2304^I    Res := [36mFindFirst[39;49;00m(Path + FileName, Attributes, PSR);$
  2305^I    [34mwhile[39;49;00m Success(Res, [34m0[39;49;00m) [34mdo[39;49;00m [34mbegin[39;49;00m$
  2306^I      TryDeleteFile(Path + PSR.Name);$
  2307^I      Res := [36mFindNext[39;49;00m(PSR);$
  2308^I    [34mend[39;49;00m;$
  2309^I    [36mFindClose[39;49;00m(PSR);$
  2310^I    [34mif[39;49;00m [34mnot[39;49;00m ScanSubDirs [34mthen[39;49;00m$
  2311^I      [34mExit[39;49;00m;$
  2312^I$
  2313^I    Res := [36mFindFirst[39;49;00m(Path + [33m'[39;49;00m[33m*[39;49;00m[33m'[39;49;00m, faDirectory, PSR);$
  2314^I    [34mwhile[39;49;00m Success(Res, [34m0[39;49;00m) [34mdo[39;49;00m [34mbegin[39;49;00m$
  2315^I      [34mif[39;49;00m (PSR.Attr [34mand[39;49;00m faDirectory > [34m0[39;49;00m)$
  2316^I       [34mand[39;49;00m (PSR.Name <> [33m'[39;49;00m[33m.[39;49;00m[33m'[39;49;00m) [34mand[39;49;00m (PSR.Name <> [33m'[39;49;00m[33m..[39;49;00m[33m'[39;49;00m) [34mthen[39;49;00m [34mbegin[39;49;00m$
  2317^I        ScanDir(Path + PSR.Name + [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m, FileName);$
  2318^I        TryDeleteFile(Path + PSR.Name);$
  2319^I      [34mend[39;49;00m;$
  2320^I      Res := [36mFindNext[39;49;00m(PSR);$
  2321^I    [34mend[39;49;00m;$
  2322^I    [36mFindClose[39;49;00m(PSR);$
  2323^I  [34mend[39;49;00m;$
  2324^I[34mbegin[39;49;00m$
  2325^I  Path := ExtractPath(Mask);$
  2326^I  FileName := [36mExtractFileName[39;49;00m(Mask);$
  2327^I  ScanDir(Path, FileName);$
  2328^I[34mend[39;49;00m;$
  2329^I$
  2330^I[34mfunction[39;49;00m [32mGetFileNew[39;49;00m(FileName: [34mstring[39;49;00m; NoFloppyDrives: [36mBoolean[39;49;00m = [34mTrue[39;49;00m): [34mstring[39;49;00m;$
  2331^I[34mvar[39;49;00m$
  2332^I  Drive: [34mstring[39;49;00m;$
  2333^I  pf, pd, Len: [36mInteger[39;49;00m;$
  2334^I  PSR: TSearchRec;$
  2335^I[34mbegin[39;49;00m$
  2336^I  [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
  2337^I  FileName := [36mTrim[39;49;00m(FileName);$
  2338^I  [34mif[39;49;00m [36mLength[39;49;00m(FileName) < [34m2[39;49;00m [34mthen[39;49;00m$
  2339^I    [34mExit[39;49;00m;$
  2340^I$
  2341^I  Drive := ExtractDrive(FileName);$
  2342^I  [34mif[39;49;00m [34mnot[39;49;00m [36mDirectoryExists[39;49;00m(Drive) [34mthen[39;49;00m$
  2343^I    [34mExit[39;49;00m;$
  2344^I$
  2345^I  [34mif[39;49;00m NoFloppyDrives [34mand[39;49;00m (Drive[[34m1[39;49;00m] [34min[39;49;00m [[33m'[39;49;00m[33mA[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mB[39;49;00m[33m'[39;49;00m]) [34mthen[39;49;00m$
  2346^I    [34mExit[39;49;00m;$
  2347^I$
  2348^I  Len := [36mLength[39;49;00m(FileName);$
  2349^I  [36mResult[39;49;00m := Drive;$
  2350^I  pf := [36mLength[39;49;00m(Drive) + [34m1[39;49;00m;$
  2351^I  [34mwhile[39;49;00m pf <= Len [34mdo[39;49;00m [34mbegin[39;49;00m$
  2352^I    [34mif[39;49;00m FileName[pf] = [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m$
  2353^I      [36mResult[39;49;00m := [36mResult[39;49;00m + [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m;$
  2354^I      [36mInc[39;49;00m(pf);$
  2355^I    [34mContinue[39;49;00m; [34mend[39;49;00m;$
  2356^I$
  2357^I    pd := CharPos([33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m, FileName, pf);$
  2358^I    [34mif[39;49;00m pd = [34m0[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m$
  2359^I      [34mif[39;49;00m [34m0[39;49;00m=[36mFindFirst[39;49;00m([36mResult[39;49;00m + [36mCopy[39;49;00m(FileName, pf, MaxInt), faFindEveryFile, PSR) [34mthen[39;49;00m [34mbegin[39;49;00m$
  2360^I        [36mResult[39;49;00m := [36mResult[39;49;00m + PSR.Name;$
  2361^I      [34mBreak[39;49;00m; [34mend[39;49;00m [34melse[39;49;00m [34mbegin[39;49;00m$
  2362^I        [36mFindClose[39;49;00m(PSR);$
  2363^I        [34mif[39;49;00m [34m0[39;49;00m=[36mFindFirst[39;49;00m([36mResult[39;49;00m + [36mCopy[39;49;00m(FileName, pf, MaxInt), faDirectory, PSR) [34mthen[39;49;00m$
  2364^I          [36mResult[39;49;00m := [36mResult[39;49;00m + PSR.Name + [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m$
  2365^I        [34melse[39;49;00m$
  2366^I          [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
  2367^I        [36mFindClose[39;49;00m(PSR);$
  2368^I        [34mif[39;49;00m [36mResult[39;49;00m = [33m'[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m$
  2369^I          [34mBreak[39;49;00m;$
  2370^I      [34mend[39;49;00m;$
  2371^I    [34mend[39;49;00m;$
  2372^I$
  2373^I    [34mif[39;49;00m [34m0[39;49;00m=[36mFindFirst[39;49;00m([36mResult[39;49;00m + [36mCopy[39;49;00m(FileName, pf, pd - pf), faDirectory, PSR) [34mthen[39;49;00m$
  2374^I      [36mResult[39;49;00m := [36mResult[39;49;00m + PSR.Name + [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m$
  2375^I    [34melse[39;49;00m$
  2376^I      [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
  2377^I    [36mFindClose[39;49;00m(PSR);$
  2378^I    [34mif[39;49;00m [36mResult[39;49;00m = [33m'[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m$
  2379^I      [34mBreak[39;49;00m;$
  2380^I$
  2381^I    pf := pd + [34m1[39;49;00m;$
  2382^I  [34mend[39;49;00m;$
  2383^I$
  2384^I  [34mif[39;49;00m ([36mResult[39;49;00m <> [33m'[39;49;00m[33m'[39;49;00m) [34mand[39;49;00m [34mnot[39;49;00m FileEx([36mResult[39;49;00m, [34mTrue[39;49;00m) [34mthen[39;49;00m$
  2385^I    [36mResult[39;49;00m := [33m'[39;49;00m[33m'[39;49;00m;$
  2386^I[34mend[39;49;00m;$
  2387^I$
  2388^I[34mfunction[39;49;00m [32mDateTimeOfFileTime[39;49;00m([34mconst[39;49;00m FileTime: TFileTime): [36mTDateTime[39;49;00m;$
  2389^I[34mvar[39;49;00m$
  2390^I  LocalFileTime: TFileTime;$
  2391^I  Res: [36mInteger[39;49;00m;$
  2392^I[34mbegin[39;49;00m$
  2393^I  [36mResult[39;49;00m := [34m0[39;49;00m;$
  2394^I$
  2395^I  FileTimeToLocalFileTime(FileTime, LocalFileTime);$
  2396^I  [34mif[39;49;00m [34mnot[39;49;00m FileTimeToDosDateTime(LocalFileTime, LongRec(Res).Hi,$
  2397^I   LongRec(Res).Lo) [34mthen[39;49;00m$
  2398^I    Res := -[34m1[39;49;00m;$
  2399^I$
  2400^I  [34mif[39;49;00m (Res = -[34m1[39;49;00m) [34mor[39;49;00m (Res = [34m0[39;49;00m) [34mthen[39;49;00m$
  2401^I    [34mExit[39;49;00m;$
  2402^I  [34mtry[39;49;00m$
  2403^I    [36mResult[39;49;00m := [36mFileDateToDateTime[39;49;00m(Res);$
  2404^I  [34mexcept[39;49;00m$
  2405^I  [34mend[39;49;00m;$
  2406^I[34mend[39;49;00m;$
  2407^I$
  2408^I[34mprocedure[39;49;00m [32mFileNew[39;49;00m([34mconst[39;49;00m FileName: [34mstring[39;49;00m);$
  2409^I[34mvar[39;49;00m$
  2410^I  Handle: [36mInteger[39;49;00m;$
  2411^I[34mbegin[39;49;00m$
  2412^I  Handle := [36mFileCreate[39;49;00m(FileName);$
  2413^I  [36mFileClose[39;49;00m(Handle);$
  2414^I[34mend[39;49;00m;$
  2415^I$
  2416^I[34mfunction[39;49;00m [32mWin32PlatformStr[39;49;00m: [34mstring[39;49;00m;$
  2417^I[34mconst[39;49;00m$
  2418^I  PlatformStrings: [34marray[39;49;00m[VER_PLATFORM_WIN32s..VER_PLATFORM_WIN32_NT] [34mof[39;49;00m [34mstring[39;49;00m =$
  2419^I    ([33m'[39;49;00m[33mVER_PLATFORM_WIN32s[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mVER_PLATFORM_WIN32_WINDOWS[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mVER_PLATFORM_WIN32_NT[39;49;00m[33m'[39;49;00m);$
  2420^I[34mbegin[39;49;00m$
  2421^I  [36mResult[39;49;00m := PlatformStrings[Win32Platform];$
  2422^I[34mend[39;49;00m;$
  2423^I$
  2424^I[34mfunction[39;49;00m [32mFullOSInfo[39;49;00m: [34mstring[39;49;00m;$
  2425^I[34mbegin[39;49;00m$
  2426^I  [36mResult[39;49;00m := [36mFormat[39;49;00m($
  2427^I    [33m'[39;49;00m[33mPlatform: %s[39;49;00m[33m'[39;49;00m + EOL +$
  2428^I    [33m'[39;49;00m[33mVersion: %d.%d Build %d[39;49;00m[33m'[39;49;00m + EOL +$
  2429^I    [33m'[39;49;00m[33mCSD: %s[39;49;00m[33m'[39;49;00m,$
  2430^I    [$
  2431^I      Win32PlatformStr,$
  2432^I      Win32MajorVersion, Win32MinorVersion, Win32BuildNumber,$
  2433^I      Win32CSDVersion$
  2434^I    ]$
  2435^I  );$
  2436^I[34mend[39;49;00m;$
  2437^I$
  2438^I[34mfunction[39;49;00m [32mWin9x[39;49;00m: [36mBoolean[39;49;00m;$
  2439^I[34mbegin[39;49;00m$
  2440^I  [36mResult[39;49;00m := Win32Platform = VER_PLATFORM_WIN32_WINDOWS;$
  2441^I[34mend[39;49;00m;$
  2442^I$
  2443^I[34mfunction[39;49;00m [32mWinNT[39;49;00m: [36mBoolean[39;49;00m;$
  2444^I[34mbegin[39;49;00m$
  2445^I  [36mResult[39;49;00m := Win32Platform = VER_PLATFORM_WIN32_NT;$
  2446^I[34mend[39;49;00m;$
  2447^I$
  2448^I[34mfunction[39;49;00m [32mWin2000[39;49;00m: [36mBoolean[39;49;00m;$
  2449^I[34mbegin[39;49;00m$
  2450^I  [36mResult[39;49;00m := (Win32Platform = VER_PLATFORM_WIN32_NT)$
  2451^I            [34mand[39;49;00m (Win32MajorVersion = [34m4[39;49;00m);$
  2452^I[34mend[39;49;00m;$
  2453^I$
  2454^I[34mfunction[39;49;00m [32mWinXP[39;49;00m: [36mBoolean[39;49;00m;$
  2455^I[34mbegin[39;49;00m$
  2456^I  [36mResult[39;49;00m := Win32MajorVersion >= [34m5[39;49;00m;$
  2457^I[34mend[39;49;00m;$
  2458^I$
  2459^I[34minitialization[39;49;00m$
  2460^I  MyDir := GetMyDir;$
  2461^I$
  2462^I[34mend[39;49;00m.$
  2463^I$
  2464^I[34munit[39;49;00m FifoStream;$
  2465^I$
  2466^I[34minterface[39;49;00m$
  2467^I$
  2468^I[34muses[39;49;00m Classes, windows, Dialogs;$
  2469^I$
  2470^I[34mconst[39;49;00m$
  2471^I  DefaultChunksize = [34m32768[39;49;00m; [37m// 32kb per chunk as default.[39;49;00m$
  2472^I$
  2473^I[34mtype[39;49;00m$
  2474^I  PMemChunk = ^TMemChunk;$
  2475^I  TMemChunk = [34mrecord[39;49;00m$
  2476^I    Filled: [36mLongword[39;49;00m;$
  2477^I    [36mRead[39;49;00m: [36mLongword[39;49;00m;$
  2478^I    Data: [36mpointer[39;49;00m;$
  2479^I  [34mend[39;49;00m;$
  2480^I$
  2481^I  TFifo = [34mclass[39;49;00m$
  2482^I  [34mprivate[39;49;00m$
  2483^I    FBuffers: TList;$
  2484^I    FChunksize: [36mLongword[39;49;00m;$
  2485^I    FCritSect: TRTLCriticalSection;$
  2486^I    FIsWinNT: [36mboolean[39;49;00m;$
  2487^I    FBytesInFifo: [36mLongWord[39;49;00m;$
  2488^I  [34mprotected[39;49;00m$
  2489^I    [34mfunction[39;49;00m [32mGetBytesInFifo[39;49;00m: [36mLongWord[39;49;00m;$
  2490^I  [34mpublic[39;49;00m$
  2491^I    [34mconstructor[39;49;00m [32mCreate[39;49;00m;$
  2492^I    [34mdestructor[39;49;00m [32mDestroy[39;49;00m; [34moverride[39;49;00m;$
  2493^I    [34mprocedure[39;49;00m [32mWrite[39;49;00m(Data: [36mpointer[39;49;00m; Size: [36mLongWord[39;49;00m);$
  2494^I    [34mprocedure[39;49;00m [32mRead[39;49;00m(Buff: [36mpointer[39;49;00m; [34mvar[39;49;00m ReqSize: [36mLongWord[39;49;00m);$
  2495^I    [34mprocedure[39;49;00m [32mPeekData[39;49;00m(Buff: [36mpointer[39;49;00m; [34mvar[39;49;00m ReqSize: [36mLongWord[39;49;00m);$
  2496^I  [34mpublished[39;49;00m$
  2497^I    [34mproperty[39;49;00m BytesInFifo: [36mLongWord[39;49;00m [34mread[39;49;00m [32mFBytesInFifo[39;49;00m;$
  2498^I  [34mend[39;49;00m;$
  2499^I$
  2500^I[34mimplementation[39;49;00m$
  2501^I$
  2502^I[34mconstructor[39;49;00m [04m[32mTFifo[39;49;00m.[32mCreate[39;49;00m;$
  2503^I[34mbegin[39;49;00m$
  2504^I  [34minherited[39;49;00m;$
  2505^I  FBuffers := TList.Create;$
  2506^I  [37m// set default chunksize...[39;49;00m$
  2507^I  FChunksize := DefaultChunksize;$
  2508^I  InitializeCriticalSection(FCritSect);$
  2509^I[34mend[39;49;00m;$
  2510^I$
  2511^I[34mdestructor[39;49;00m [04m[32mTFifo[39;49;00m.[32mDestroy[39;49;00m;$
  2512^I[34mvar[39;49;00m$
  2513^I  I: [36mInteger[39;49;00m;$
  2514^I[34mbegin[39;49;00m$
  2515^I  EnterCriticalSection(FCritSect);$
  2516^I  [34mfor[39;49;00m I := [34m0[39;49;00m [34mto[39;49;00m FBuffers.count - [34m1[39;49;00m [34mdo[39;49;00m$
  2517^I  [34mbegin[39;49;00m$
  2518^I    [36mFreeMem[39;49;00m(PMemChunk(Fbuffers[I]).Data);$
  2519^I    [34mDispose[39;49;00m(PMemChunk(Fbuffers[I]));$
  2520^I  [34mend[39;49;00m;$
  2521^I  FBuffers.Clear;$
  2522^I  FBuffers.Free;$
  2523^I  LeaveCriticalSection(FCritSect);$
  2524^I$
  2525^I  DeleteCriticalSection(FCritSect);$
  2526^I  [34minherited[39;49;00m;$
  2527^I[34mend[39;49;00m;$
  2528^I$
  2529^I[34mfunction[39;49;00m [04m[32mTFifo[39;49;00m.[32mGetBytesInFifo[39;49;00m: [36mLongWord[39;49;00m;$
  2530^I[34mbegin[39;49;00m$
  2531^I  [36mResult[39;49;00m := [34m0[39;49;00m;$
  2532^I  [34mif[39;49;00m FBuffers.Count = [34m0[39;49;00m [34mthen[39;49;00m$
  2533^I  [34mbegin[39;49;00m$
  2534^I    [34mexit[39;49;00m;$
  2535^I  [34mend[39;49;00m$
  2536^I  [34melse[39;49;00m$
  2537^I  [34mbegin[39;49;00m$
  2538^I    [34mif[39;49;00m FBuffers.Count > [34m1[39;49;00m [34mthen[39;49;00m$
  2539^I      [36mInc[39;49;00m([36mResult[39;49;00m, (FBuffers.Count - [34m1[39;49;00m) * FChunkSize);$
  2540^I    [36mInc[39;49;00m([36mResult[39;49;00m, PMemChunk(FBuffers[Fbuffers.Count - [34m1[39;49;00m]).Filled);$
  2541^I    [36mDec[39;49;00m([36mResult[39;49;00m, PMemChunk(FBuffers[[34m0[39;49;00m]).Read);$
  2542^I  [34mend[39;49;00m;$
  2543^I[34mend[39;49;00m;$
  2544^I$
  2545^I[34mprocedure[39;49;00m [04m[32mTFifo[39;49;00m.[32mWrite[39;49;00m(Data: [36mpointer[39;49;00m; Size: [36mLongWord[39;49;00m);$
  2546^I[34mvar[39;49;00m$
  2547^I  Privpointer: [36mpointer[39;49;00m;$
  2548^I  PrivSize: [36mLongWord[39;49;00m;$
  2549^I  Chunk: PMemChunk;$
  2550^I  PosInChunk: [36mpointer[39;49;00m;$
  2551^I[34mbegin[39;49;00m$
  2552^I  [34mif[39;49;00m [36mLongWord[39;49;00m(Data) = [34m0[39;49;00m [34mthen[39;49;00m$
  2553^I  [34mbegin[39;49;00m$
  2554^I    [37m// null pointer? somebody is trying to fool us, get out...[39;49;00m$
  2555^I    [34mExit[39;49;00m;$
  2556^I  [34mend[39;49;00m;$
  2557^I  EnterCriticalSection(FCritSect);$
  2558^I  PrivPointer := Data;$
  2559^I  PrivSize := [34m0[39;49;00m;$
  2560^I  [37m// are already buffers there?[39;49;00m$
  2561^I  [34mif[39;49;00m FBuffers.count > [34m0[39;49;00m [34mthen[39;49;00m$
  2562^I  [34mbegin[39;49;00m$
  2563^I    [37m// is the last one of them not completely filled?[39;49;00m$
  2564^I    [34mif[39;49;00m PMemChunk(FBuffers[FBuffers.count - [34m1[39;49;00m]).filled < FChunksize [34mthen[39;49;00m$
  2565^I      [37m// not completely filled, so fill up the buffer.[39;49;00m$
  2566^I    [34mbegin[39;49;00m$
  2567^I      Chunk := PMemChunk(FBuffers[FBuffers.count - [34m1[39;49;00m]);$
  2568^I      [37m// fetch chunkdata.[39;49;00m$
  2569^I      PosInChunk := Chunk.Data;$
  2570^I      [37m// move to current fill pos...[39;49;00m$
  2571^I      [36mInc[39;49;00m([36mLongWord[39;49;00m(PosInChunk), Chunk.Filled);$
  2572^I      [37m// can we fill the chunk completely?[39;49;00m$
  2573^I      [34mif[39;49;00m Size > FChunksize - Chunk.Filled [34mthen[39;49;00m$
  2574^I      [34mbegin[39;49;00m$
  2575^I        [37m// yes we can.[39;49;00m$
  2576^I        [36mMove[39;49;00m(PrivPointer^, PosInChunk^, FChunksize - Chunk.Filled);$
  2577^I        [36mInc[39;49;00m(PrivSize, FChunksize - Chunk.Filled);$
  2578^I        [36mInc[39;49;00m([36mLongWord[39;49;00m(PrivPointer), FChunksize - Chunk.Filled);$
  2579^I        Chunk.Filled := FChunkSize;$
  2580^I      [34mend[39;49;00m$
  2581^I      [34melse[39;49;00m$
  2582^I        [37m// we have to less data for filling the chunk completely,[39;49;00m$
  2583^I        [37m// just put everything in.[39;49;00m$
  2584^I      [34mbegin[39;49;00m$
  2585^I        [36mMove[39;49;00m(PrivPointer^, PosInChunk^, Size);$
  2586^I        [36mInc[39;49;00m(PrivSize, Size);$
  2587^I        [36mInc[39;49;00m(Chunk.Filled, Size);$
  2588^I      [34mend[39;49;00m;$
  2589^I    [34mend[39;49;00m;$
  2590^I  [34mend[39;49;00m;$
  2591^I  [37m// as long as we have remaining stuff put it into new chunks.[39;49;00m$
  2592^I  [34mwhile[39;49;00m (PrivSize < Size) [34mdo[39;49;00m$
  2593^I  [34mbegin[39;49;00m$
  2594^I    [34mnew[39;49;00m(Chunk);$
  2595^I    [36mGetMem[39;49;00m(Chunk.Data, FChunksize);$
  2596^I    Chunk.Read := [34m0[39;49;00m;$
  2597^I    [37m// can we fill an entire chunk with the remaining data?[39;49;00m$
  2598^I    [34mif[39;49;00m Privsize + FChunksize < Size [34mthen[39;49;00m$
  2599^I    [34mbegin[39;49;00m$
  2600^I      [37m// yes we can, so put the stuff in.[39;49;00m$
  2601^I      [36mMove[39;49;00m(Privpointer^, Chunk.Data^, FChunksize);$
  2602^I      [36mInc[39;49;00m([36mLongWord[39;49;00m(PrivPointer), FChunksize);$
  2603^I      [36mInc[39;49;00m(PrivSize, FChunksize);$
  2604^I      Chunk.Filled := FChunksize;$
  2605^I    [34mend[39;49;00m$
  2606^I    [34melse[39;49;00m [37m// we have to less data to fill the entire chunk, just put the remaining stuff in.[39;49;00m$
  2607^I    [34mbegin[39;49;00m$
  2608^I      [36mMove[39;49;00m(Privpointer^, Chunk.Data^, Size - Privsize);$
  2609^I      Chunk.Filled := Size - Privsize;$
  2610^I      [36mInc[39;49;00m(PrivSize, Size - Privsize);$
  2611^I    [34mend[39;49;00m;$
  2612^I    Fbuffers.Add(Chunk);$
  2613^I  [34mend[39;49;00m;$
  2614^I  [34mif[39;49;00m Size <> Privsize [34mthen[39;49;00m$
  2615^I    Showmessage([33m'[39;49;00m[33mmiscalculation in TFifo.write[39;49;00m[33m'[39;49;00m);$
  2616^I  FBytesInFifo := GetBytesInFifo;$
  2617^I  LeaveCriticalSection(FCritSect);$
  2618^I[34mend[39;49;00m;$
  2619^I$
  2620^I[34mprocedure[39;49;00m [04m[32mTFifo[39;49;00m.[32mRead[39;49;00m(Buff: [36mpointer[39;49;00m; [34mvar[39;49;00m ReqSize: [36mLongWord[39;49;00m);$
  2621^I[34mvar[39;49;00m$
  2622^I  PrivSize: [36mInteger[39;49;00m;$
  2623^I  Privpos: [36mpointer[39;49;00m;$
  2624^I  Chunk: PMemChunk;$
  2625^I  ChunkPos: [36mpointer[39;49;00m;$
  2626^I[34mbegin[39;49;00m$
  2627^I  [34mif[39;49;00m [36mLongWord[39;49;00m(Buff) = [34m0[39;49;00m [34mthen[39;49;00m$
  2628^I  [34mbegin[39;49;00m$
  2629^I    [37m// null pointer? somebody is trying to fool us, get out...[39;49;00m$
  2630^I    [34mExit[39;49;00m;$
  2631^I  [34mend[39;49;00m;$
  2632^I  EnterCriticalSection(FCritSect);$
  2633^I  PrivSize := [34m0[39;49;00m;$
  2634^I  Privpos := Buff;$
  2635^I  [34mwhile[39;49;00m FBuffers.Count > [34m0[39;49;00m [34mdo[39;49;00m$
  2636^I  [34mbegin[39;49;00m$
  2637^I    Chunk := PMemChunk(FBuffers[[34m0[39;49;00m]);$
  2638^I    ChunkPos := Chunk.data;$
  2639^I    [36mInc[39;49;00m([36mLongWord[39;49;00m(ChunkPos), Chunk.Read);$
  2640^I    [37m// does the remaining part of the chunk fit into the buffer?[39;49;00m$
  2641^I    [34mif[39;49;00m PrivSize + (Chunk.Filled - Chunk.read) < ReqSize [34mthen[39;49;00m$
  2642^I    [34mbegin[39;49;00m [37m// yep, it fits[39;49;00m$
  2643^I      [36mMove[39;49;00m(ChunkPos^, Privpos^, Chunk.Filled - Chunk.read);$
  2644^I      [36mInc[39;49;00m(PrivSize, Chunk.Filled - Chunk.read);$
  2645^I      [36mFreeMem[39;49;00m(Chunk.Data);$
  2646^I      [34mDispose[39;49;00m(Chunk);$
  2647^I      FBuffers.Delete([34m0[39;49;00m);$
  2648^I    [34mend[39;49;00m$
  2649^I    [34melse[39;49;00m [37m// remaining part didn't fit, get as much as we can and increment the[39;49;00m$
  2650^I      [37m// read attribute.[39;49;00m$
  2651^I    [34mbegin[39;49;00m$
  2652^I      [36mMove[39;49;00m(ChunkPos^, Privpos^, ReqSize - PrivSize);$
  2653^I      [36mInc[39;49;00m(Chunk.read, ReqSize - PrivSize);$
  2654^I      [36mInc[39;49;00m(PrivSize, ReqSize - PrivSize);$
  2655^I      [37m// as we filled the buffer, we'll have to break here.[39;49;00m$
  2656^I      [34mbreak[39;49;00m;$
  2657^I    [34mend[39;49;00m;$
  2658^I  [34mend[39;49;00m;$
  2659^I  FBytesInFifo := GetBytesInFifo;$
  2660^I  LeaveCriticalSection(FCritSect);$
  2661^I  ReqSize := PrivSize;$
  2662^I[34mend[39;49;00m;$
  2663^I$
  2664^I[37m// read Data from Stream without removing it from the Stream...[39;49;00m$
  2665^I$
  2666^I[34mprocedure[39;49;00m [04m[32mTFifo[39;49;00m.[32mPeekData[39;49;00m(Buff: [36mpointer[39;49;00m; [34mvar[39;49;00m ReqSize: [36mLongWord[39;49;00m);$
  2667^I[34mvar[39;49;00m$
  2668^I  PrivSize: [36mInteger[39;49;00m;$
  2669^I  Privpos: [36mpointer[39;49;00m;$
  2670^I  Chunk: PMemChunk;$
  2671^I  ChunkPos: [36mpointer[39;49;00m;$
  2672^I  ChunkNr: [36mInteger[39;49;00m;$
  2673^I[34mbegin[39;49;00m$
  2674^I  [34mif[39;49;00m [36mLongWord[39;49;00m(Buff) = [34m0[39;49;00m [34mthen[39;49;00m$
  2675^I  [34mbegin[39;49;00m$
  2676^I    [37m// null pointer? somebody is trying to fool us, get out...[39;49;00m$
  2677^I    [34mExit[39;49;00m;$
  2678^I  [34mend[39;49;00m;$
  2679^I  EnterCriticalSection(FCritSect);$
  2680^I  PrivSize := [34m0[39;49;00m;$
  2681^I  Privpos := Buff;$
  2682^I  ChunkNr := [34m0[39;49;00m;$
  2683^I  [34mwhile[39;49;00m FBuffers.Count > ChunkNr [34mdo[39;49;00m$
  2684^I  [34mbegin[39;49;00m$
  2685^I    Chunk := PMemChunk(FBuffers[ChunkNr]);$
  2686^I    ChunkPos := Chunk.data;$
  2687^I    [36mInc[39;49;00m([36mLongWord[39;49;00m(ChunkPos), Chunk.Read);$
  2688^I    [37m// does the remaining part of the chunk fit into the buffer?[39;49;00m$
  2689^I    [34mif[39;49;00m PrivSize + (Chunk.Filled - Chunk.read) < ReqSize [34mthen[39;49;00m$
  2690^I    [34mbegin[39;49;00m [37m// yep, it fits[39;49;00m$
  2691^I      [36mMove[39;49;00m(ChunkPos^, Privpos^, Chunk.Filled - Chunk.read);$
  2692^I      [36mInc[39;49;00m(PrivSize, Chunk.Filled - Chunk.read);$
  2693^I      [36mInc[39;49;00m(ChunkNr);$
  2694^I    [34mend[39;49;00m$
  2695^I    [34melse[39;49;00m [37m// remaining part didn't fit, get as much as we can and increment the[39;49;00m$
  2696^I      [37m// read attribute.[39;49;00m$
  2697^I    [34mbegin[39;49;00m$
  2698^I      [36mMove[39;49;00m(ChunkPos^, Privpos^, ReqSize - PrivSize);$
  2699^I      [36mInc[39;49;00m(PrivSize, ReqSize - PrivSize);$
  2700^I      [37m// as we filled the buffer, we'll have to break here.[39;49;00m$
  2701^I      [34mbreak[39;49;00m;$
  2702^I    [34mend[39;49;00m;$
  2703^I  [34mend[39;49;00m;$
  2704^I  LeaveCriticalSection(FCritSect);$
  2705^I  ReqSize := PrivSize;$
  2706^I[34mend[39;49;00m;$
  2707^I$
  2708^I[34mend[39;49;00m.$

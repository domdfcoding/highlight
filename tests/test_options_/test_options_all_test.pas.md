     1^I[37m//[39;49;00m$
     2^I[37m// Sourcecode from http://www.delphi-library.de/topic_47880.html[39;49;00m$
     3^I[37m//[39;49;00m$
     4^I[34muses[39;49;00m Windows, Messages;$
     5^I$
     6^I[34mconst[39;49;00m$
     7^I  FFM_INIT               = WM_USER + [34m1976[39;49;00m;$
     8^I  FFM_ONFILEFOUND        = WM_USER + [34m1974[39;49;00m; [37m// wParam: not used, lParam: Filename[39;49;00m$
     9^I  FFM_ONDIRFOUND         = WM_USER + [34m1975[39;49;00m; [37m// wParam: NumFolder, lParam: Directory[39;49;00m$
    10^I[34mvar[39;49;00m$
    11^I  CntFolders             : [36mCardinal[39;49;00m = [34m0[39;49;00m;$
    12^I  NumFolder              : [36mCardinal[39;49;00m = [34m0[39;49;00m;$
    13^I$
    14^I$
    15^I[37m////////////////////////////////////////////////////////////////////////////////[39;49;00m$
    16^I[37m//[39;49;00m$
    17^I[37m//  FindAllFilesInit[39;49;00m$
    18^I[37m//[39;49;00m$
    19^I[37m//[39;49;00m$
    20^I[34mprocedure[39;49;00m [32mFindAllFilesInit[39;49;00m; [34mexternal[39;49;00m;$
    21^I[34mlabel[39;49;00m foo;$
    22^I[34mbegin[39;49;00m$
    23^I  CntFolders := [34m0[39;49;00m;$
    24^I  NumFolder := [34m0[39;49;00m;$
    25^Ifoo:$
    26^I  Blub;$
    27^I  [34mgoto[39;49;00m foo;$
    28^I[34mend[39;49;00m;$
    29^I$
    30^I[37m////////////////////////////////////////////////////////////////////////////////[39;49;00m$
    31^I[37m//[39;49;00m$
    32^I[37m//  CountFolders[39;49;00m$
    33^I[37m//[39;49;00m$
    34^I[37m//[39;49;00m$
    35^I[34mprocedure[39;49;00m [32mCountFolders[39;49;00m(Handle: [36mTHandle[39;49;00m; RootFolder: [34mstring[39;49;00m; Recurse: [36mBoolean[39;49;00m = [34mTrue[39;49;00m);$
    36^I[34mvar[39;49;00m$
    37^I  hFindFile              : [36mTHandle[39;49;00m;$
    38^I  wfd                    : TWin32FindData;$
    39^I[34mbegin[39;49;00m$
    40^I  SendMessage(Handle, FFM_INIT, [34m0[39;49;00m, [34m0[39;49;00m);$
    41^I  [34mif[39;49;00m RootFolder[[36mlength[39;49;00m(RootFolder)] <> [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m$
    42^I    RootFolder := RootFolder + [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m;$
    43^I  ZeroMemory(@wfd, [36msizeof[39;49;00m(wfd));$
    44^I  wfd.dwFileAttributes := FILE_ATTRIBUTE_NORMAL;$
    45^I  [34mif[39;49;00m Recurse [34mthen[39;49;00m$
    46^I  [34mbegin[39;49;00m$
    47^I    hFindFile := FindFirstFile([36mpointer[39;49;00m(RootFolder + [33m'[39;49;00m[33m*.*[39;49;00m[33m'[39;49;00m), wfd);$
    48^I    [34mif[39;49;00m hFindFile <> [34m0[39;49;00m [34mthen[39;49;00m$
    49^I    [34mtry[39;49;00m$
    50^I      [34mrepeat[39;49;00m$
    51^I        [34mif[39;49;00m wfd.dwFileAttributes [34mand[39;49;00m FILE_ATTRIBUTE_DIRECTORY = FILE_ATTRIBUTE_DIRECTORY [34mthen[39;49;00m$
    52^I        [34mbegin[39;49;00m$
    53^I          [34mif[39;49;00m ([34mstring[39;49;00m(wfd.cFileName) <> [33m'[39;49;00m[33m.[39;49;00m[33m'[39;49;00m) [34mand[39;49;00m ([34mstring[39;49;00m(wfd.cFileName) <> [33m'[39;49;00m[33m..[39;49;00m[33m'[39;49;00m) [34mthen[39;49;00m$
    54^I          [34mbegin[39;49;00m$
    55^I            CountFolders(Handle, RootFolder + wfd.cFileName, Recurse);$
    56^I          [34mend[39;49;00m;$
    57^I        [34mend[39;49;00m;$
    58^I      [34muntil[39;49;00m FindNextFile(hFindFile, wfd) = [34mFalse[39;49;00m;$
    59^I      [36mInc[39;49;00m(CntFolders);$
    60^I    [34mfinally[39;49;00m$
    61^I      Windows.FindClose(hFindFile);$
    62^I    [34mend[39;49;00m;$
    63^I  [34mend[39;49;00m;$
    64^I[34mend[39;49;00m;$
    65^I$
    66^I[37m////////////////////////////////////////////////////////////////////////////////[39;49;00m$
    67^I[37m//[39;49;00m$
    68^I[37m//  FindAllFiles[39;49;00m$
    69^I[37m//[39;49;00m$
    70^I[34mprocedure[39;49;00m [32mFindAllFiles[39;49;00m(Handle: [36mTHandle[39;49;00m; RootFolder: [34mstring[39;49;00m; Mask: [34mstring[39;49;00m; Recurse: [36mBoolean[39;49;00m = [34mTrue[39;49;00m);$
    71^I[34mvar[39;49;00m$
    72^I  hFindFile              : [36mTHandle[39;49;00m;$
    73^I  wfd                    : TWin32FindData;$
    74^I[34mbegin[39;49;00m$
    75^I  [34mif[39;49;00m RootFolder[[36mlength[39;49;00m(RootFolder)] <> [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m$
    76^I    RootFolder := RootFolder + [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m;$
    77^I  ZeroMemory(@wfd, [36msizeof[39;49;00m(wfd));$
    78^I  wfd.dwFileAttributes := FILE_ATTRIBUTE_NORMAL;$
    79^I  [34mif[39;49;00m Recurse [34mthen[39;49;00m$
    80^I  [34mbegin[39;49;00m$
    81^I    hFindFile := FindFirstFile([36mpointer[39;49;00m(RootFolder + [33m'[39;49;00m[33m*.*[39;49;00m[33m'[39;49;00m), wfd);$
    82^I    [34mif[39;49;00m hFindFile <> [34m0[39;49;00m [34mthen[39;49;00m$
    83^I    [34mtry[39;49;00m$
    84^I      [34mrepeat[39;49;00m$
    85^I        [34mif[39;49;00m wfd.dwFileAttributes [34mand[39;49;00m FILE_ATTRIBUTE_DIRECTORY = FILE_ATTRIBUTE_DIRECTORY [34mthen[39;49;00m$
    86^I        [34mbegin[39;49;00m$
    87^I          [34mif[39;49;00m ([34mstring[39;49;00m(wfd.cFileName) <> [33m'[39;49;00m[33m.[39;49;00m[33m'[39;49;00m) [34mand[39;49;00m ([34mstring[39;49;00m(wfd.cFileName) <> [33m'[39;49;00m[33m..[39;49;00m[33m'[39;49;00m) [34mthen[39;49;00m$
    88^I          [34mbegin[39;49;00m$
    89^I            FindAllFiles(Handle, RootFolder + wfd.cFileName, Mask, Recurse);$
    90^I          [34mend[39;49;00m;$
    91^I        [34mend[39;49;00m;$
    92^I      [34muntil[39;49;00m FindNextFile(hFindFile, wfd) = [34mFalse[39;49;00m;$
    93^I      [36mInc[39;49;00m(NumFolder);$
    94^I      SendMessage(Handle, FFM_ONDIRFOUND, NumFolder, lParam([34mstring[39;49;00m(RootFolder)));$
    95^I    [34mfinally[39;49;00m$
    96^I      Windows.FindClose(hFindFile);$
    97^I    [34mend[39;49;00m;$
    98^I  [34mend[39;49;00m;$
    99^I  hFindFile := FindFirstFile([36mpointer[39;49;00m(RootFolder + Mask), wfd);$
   100^I  [34mif[39;49;00m hFindFile <> INVALID_HANDLE_VALUE [34mthen[39;49;00m$
   101^I  [34mtry[39;49;00m$
   102^I    [34mrepeat[39;49;00m$
   103^I      [34mif[39;49;00m (wfd.dwFileAttributes [34mand[39;49;00m FILE_ATTRIBUTE_DIRECTORY <> FILE_ATTRIBUTE_DIRECTORY) [34mthen[39;49;00m$
   104^I      [34mbegin[39;49;00m$
   105^I        SendMessage(Handle, FFM_ONFILEFOUND, [34m0[39;49;00m, lParam([34mstring[39;49;00m(RootFolder + wfd.cFileName)));$
   106^I      [34mend[39;49;00m;$
   107^I    [34muntil[39;49;00m FindNextFile(hFindFile, wfd) = [34mFalse[39;49;00m;$
   108^I  [34mfinally[39;49;00m$
   109^I    Windows.FindClose(hFindFile);$
   110^I  [34mend[39;49;00m;$
   111^I[34mend[39;49;00m;$
   112^I$
   113^I$
   114^I[34mproperty[39;49;00m test: [36mboolean[39;49;00m [34mread[39;49;00m [32mftest[39;49;00m [34mwrite[39;49;00m [32mftest[39;49;00m;$
   115^I[34mprocedure[39;49;00m [32mtest[39;49;00m: [36mboolean[39;49;00m [36mread[39;49;00m ftest [36mwrite[39;49;00m ftest;$
   116^I$
   117^I[37m//[39;49;00m$
   118^I[37m// This sourcecode is part of omorphia[39;49;00m$
   119^I[37m//[39;49;00m$
   120^I$
   121^I[34mFunction[39;49;00m [32mIsValidHandle[39;49;00m([34mConst[39;49;00m Handle: [36mTHandle[39;49;00m): [36mBoolean[39;49;00m; [37m{$IFDEF OMORPHIA_FEATURES_USEASM}[39;49;00m [34mAssembler[39;49;00m;$
   122^I[34mAsm[39;49;00m$
   123^I    [34mTEST[39;49;00m    [36mEAX[39;49;00m, [36mEAX[39;49;00m$
   124^I    [34mJZ[39;49;00m      @@Finish$
   125^I    [34mNOT[39;49;00m     [36mEAX[39;49;00m$
   126^I    [34mTEST[39;49;00m    [36mEAX[39;49;00m, [36mEAX[39;49;00m$
   127^I    [34mSETNZ[39;49;00m   [36mAL[39;49;00m$
   128^I$
   129^I    [37m{$IFDEF WINDOWS}[39;49;00m$
   130^I    [34mJZ[39;49;00m      @@Finish$
   131^I$
   132^I    [37m//Save the handle against modifications or loss[39;49;00m$
   133^I    [34mPUSH[39;49;00m    [36mEAX[39;49;00m$
   134^I$
   135^I    [37m//reserve some space for a later duplicate[39;49;00m$
   136^I    [34mPUSH[39;49;00m    [36mEAX[39;49;00m$
   137^I$
   138^I    [37m//Check if we are working on NT-Platform[39;49;00m$
   139^I    [34mCALL[39;49;00m    IsWindowsNTSystem$
   140^I    [34mTEST[39;49;00m    [36mEAX[39;49;00m, [36mEAX[39;49;00m$
   141^I    [34mJZ[39;49;00m      @@NoNTSystem$
   142^I$
   143^I    [34mPUSH[39;49;00m    DWORD PTR [[36mESP[39;49;00m]$
   144^I    [34mLEA[39;49;00m     [36mEAX[39;49;00m, DWORD PTR [[36mESP[39;49;00m+[34m$04[39;49;00m]$
   145^I    [34mPUSH[39;49;00m    [36mEAX[39;49;00m$
   146^I    [34mCALL[39;49;00m    GetHandleInformation$
   147^I    [34mTEST[39;49;00m    [36mEAX[39;49;00m, [36mEAX[39;49;00m$
   148^I    [34mJNZ[39;49;00m     @@Finish2$
   149^I$
   150^I@@NoNTSystem:$
   151^I    [37m//Result := DuplicateHandle(GetCurrentProcess, Handle, GetCurrentProcess,[39;49;00m$
   152^I    [37m//  @Duplicate, 0, False, DUPLICATE_SAME_ACCESS);[39;49;00m$
   153^I    [34mPUSH[39;49;00m    DUPLICATE_SAME_ACCESS$
   154^I    [34mPUSH[39;49;00m    [34m$00000000[39;49;00m$
   155^I    [34mPUSH[39;49;00m    [34m$00000000[39;49;00m$
   156^I    [34mLEA[39;49;00m     [36mEAX[39;49;00m, DWORD PTR [[36mESP[39;49;00m+[34m$0C[39;49;00m]$
   157^I    [34mPUSH[39;49;00m    [36mEAX[39;49;00m$
   158^I    [34mCALL[39;49;00m    GetCurrentProcess$
   159^I    [34mPUSH[39;49;00m    [36mEAX[39;49;00m$
   160^I    [34mPUSH[39;49;00m    DWORD PTR [[36mESP[39;49;00m+[34m$18[39;49;00m]$
   161^I    [34mPUSH[39;49;00m    [36mEAX[39;49;00m$
   162^I    [34mCALL[39;49;00m    DuplicateHandle$
   163^I$
   164^I    [34mTEST[39;49;00m    [36mEAX[39;49;00m, [36mEAX[39;49;00m$
   165^I    [34mJZ[39;49;00m      @@Finish2$
   166^I$
   167^I    [37m//  Result := CloseHandle(Duplicate);[39;49;00m$
   168^I    [34mPUSH[39;49;00m    DWORD PTR [[36mESP[39;49;00m]$
   169^I    [34mCALL[39;49;00m    CloseHandle$
   170^I$
   171^I@@Finish2:$
   172^I    [34mPOP[39;49;00m     [36mEDX[39;49;00m$
   173^I    [34mPOP[39;49;00m     [36mEDX[39;49;00m$
   174^I$
   175^I    [34mPUSH[39;49;00m    [36mEAX[39;49;00m$
   176^I    [34mPUSH[39;49;00m    [34m$00000000[39;49;00m$
   177^I    [34mCALL[39;49;00m    SetLastError$
   178^I    [34mPOP[39;49;00m     [36mEAX[39;49;00m$
   179^I    [37m{$ENDIF}[39;49;00m$
   180^I$
   181^I@@Finish:$
   182^I[34mEnd[39;49;00m;$
   183^I[37m{$ELSE}[39;49;00m$
   184^I[34mVar[39;49;00m$
   185^I    Duplicate: [36mTHandle[39;49;00m;$
   186^I    Flags: [36mDWORD[39;49;00m;$
   187^I[34mBegin[39;49;00m$
   188^I    [34mIf[39;49;00m IsWinNT [34mThen[39;49;00m$
   189^I        [36mResult[39;49;00m := GetHandleInformation(Handle, Flags)$
   190^I    [34mElse[39;49;00m$
   191^I        [36mResult[39;49;00m := [34mFalse[39;49;00m;$
   192^I    [34mIf[39;49;00m [34mNot[39;49;00m [36mResult[39;49;00m [34mThen[39;49;00m$
   193^I    [34mBegin[39;49;00m$
   194^I        [37m// DuplicateHandle is used as an additional check for those object types not[39;49;00m$
   195^I        [37m// supported by GetHandleInformation (e.g. according to the documentation,[39;49;00m$
   196^I        [37m// GetHandleInformation doesn't support window stations and desktop although[39;49;00m$
   197^I        [37m// tests show that it does). GetHandleInformation is tried first because its[39;49;00m$
   198^I        [37m// much faster. Additionally GetHandleInformation is only supported on NT...[39;49;00m$
   199^I        [36mResult[39;49;00m := DuplicateHandle(GetCurrentProcess, Handle, GetCurrentProcess,$
   200^I            @Duplicate, [34m0[39;49;00m, [34mFalse[39;49;00m, DUPLICATE_SAME_ACCESS);$
   201^I        [34mIf[39;49;00m [36mResult[39;49;00m [34mThen[39;49;00m$
   202^I            [36mResult[39;49;00m := CloseHandle(Duplicate);$
   203^I    [34mEnd[39;49;00m;$
   204^I[34mEnd[39;49;00m;$
   205^I[37m{$ENDIF}[39;49;00m$
   206^I$
   207^I$
   208^I    ^I$
   209^I$
   210^I[37m{*******************************************************}[39;49;00m$
   211^I[37m{                                                       }[39;49;00m$
   212^I[37m{       Delphi Supplemental Components                  }[39;49;00m$
   213^I[37m{       ZLIB Data Compression Interface Unit            }[39;49;00m$
   214^I[37m{                                                       }[39;49;00m$
   215^I[37m{       Copyright (c) 1997 Borland International        }[39;49;00m$
   216^I[37m{                                                       }[39;49;00m$
   217^I[37m{*******************************************************}[39;49;00m$
   218^I$
   219^I[37m{ Modified for zlib 1.1.3 by Davide Moretti <dave@rimini.com }[39;49;00m$
   220^I$
   221^I[34munit[39;49;00m zlib;$
   222^I$
   223^I[34minterface[39;49;00m$
   224^I$
   225^I[34muses[39;49;00m Sysutils, Classes;$
   226^I$
   227^I[34mtype[39;49;00m$
   228^I  TAlloc = [34mfunction[39;49;00m (AppData: [36mPointer[39;49;00m; Items, Size: [36mInteger[39;49;00m): [36mPointer[39;49;00m;$
   229^I  TFree = [34mprocedure[39;49;00m (AppData, Block: [36mPointer[39;49;00m);$
   230^I$
   231^I  [37m// Internal structure.  Ignore.[39;49;00m$
   232^I  TZStreamRec = [34mpacked[39;49;00m [34mrecord[39;49;00m$
   233^I    next_in: [36mPChar[39;49;00m;       [37m// next input byte[39;49;00m$
   234^I    avail_in: [36mInteger[39;49;00m;    [37m// number of bytes available at next_in[39;49;00m$
   235^I    total_in: [36mInteger[39;49;00m;    [37m// total nb of input bytes read so far[39;49;00m$
   236^I$
   237^I    next_out: [36mPChar[39;49;00m;      [37m// next output byte should be put here[39;49;00m$
   238^I    avail_out: [36mInteger[39;49;00m;   [37m// remaining free space at next_out[39;49;00m$
   239^I    total_out: [36mInteger[39;49;00m;   [37m// total nb of bytes output so far[39;49;00m$
   240^I$
   241^I    msg: [36mPChar[39;49;00m;           [37m// last error message, NULL if no error[39;49;00m$
   242^I    internal: [36mPointer[39;49;00m;    [37m// not visible by applications[39;49;00m$
   243^I$
   244^I    zalloc: TAlloc;       [37m// used to allocate the internal state[39;49;00m$
   245^I    zfree: TFree;         [37m// used to free the internal state[39;49;00m$
   246^I    AppData: [36mPointer[39;49;00m;     [37m// private data object passed to zalloc and zfree[39;49;00m$
   247^I$
   248^I    data_type: [36mInteger[39;49;00m;   [37m//  best guess about the data type: ascii or binary[39;49;00m$
   249^I    adler: [36mInteger[39;49;00m;       [37m// adler32 value of the uncompressed data[39;49;00m$
   250^I    reserved: [36mInteger[39;49;00m;    [37m// reserved for future use[39;49;00m$
   251^I  [34mend[39;49;00m;$
   252^I$
   253^I  [37m// Abstract ancestor class[39;49;00m$
   254^I  TCustomZlibStream = [34mclass[39;49;00m(TStream)$
   255^I  [34mprivate[39;49;00m$
   256^I    FStrm: TStream;$
   257^I    FStrmPos: [36mInteger[39;49;00m;$
   258^I    FOnProgress: TNotifyEvent;$
   259^I    FZRec: TZStreamRec;$
   260^I    FBuffer: [34marray[39;49;00m [[36mWord[39;49;00m] [34mof[39;49;00m [36mChar[39;49;00m;$
   261^I  [34mprotected[39;49;00m$
   262^I    [34mprocedure[39;49;00m [32mProgress[39;49;00m(Sender: [36mTObject[39;49;00m); [34mdynamic[39;49;00m;$
   263^I    [34mproperty[39;49;00m OnProgress: TNotifyEvent [34mread[39;49;00m [32mFOnProgress[39;49;00m [34mwrite[39;49;00m [32mFOnProgress[39;49;00m;$
   264^I    [34mconstructor[39;49;00m [32mCreate[39;49;00m(Strm: TStream);$
   265^I  [34mend[39;49;00m;$
   266^I$
   267^I[37m{ TCompressionStream compresses data on the fly as data is written to it, and[39;49;00m$
   268^I[37m  stores the compressed data to another stream.[39;49;00m$
   269^I[37m[39;49;00m$
   270^I[37m  TCompressionStream is write-only and strictly sequential. Reading from the[39;49;00m$
   271^I[37m  stream will raise an exception. Using Seek to move the stream pointer[39;49;00m$
   272^I[37m  will raise an exception.[39;49;00m$
   273^I[37m[39;49;00m$
   274^I[37m  Output data is cached internally, written to the output stream only when[39;49;00m$
   275^I[37m  the internal output buffer is full.  All pending output data is flushed[39;49;00m$
   276^I[37m  when the stream is destroyed.[39;49;00m$
   277^I[37m[39;49;00m$
   278^I[37m  The Position property returns the number of uncompressed bytes of[39;49;00m$
   279^I[37m  data that have been written to the stream so far.[39;49;00m$
   280^I[37m[39;49;00m$
   281^I[37m  CompressionRate returns the on-the-fly percentage by which the original[39;49;00m$
   282^I[37m  data has been compressed:  (1 - (CompressedBytes / UncompressedBytes)) * 100[39;49;00m$
   283^I[37m  If raw data size = 100 and compressed data size = 25, the CompressionRate[39;49;00m$
   284^I[37m  is 75%[39;49;00m$
   285^I[37m[39;49;00m$
   286^I[37m  The OnProgress event is called each time the output buffer is filled and[39;49;00m$
   287^I[37m  written to the output stream.  This is useful for updating a progress[39;49;00m$
   288^I[37m  indicator when you are writing a large chunk of data to the compression[39;49;00m$
   289^I[37m  stream in a single call.}[39;49;00m$
   290^I$
   291^I$
   292^I  TCompressionLevel = (clNone, clFastest, clDefault, clMax);$
   293^I$
   294^I  TCompressionStream = [34mclass[39;49;00m(TCustomZlibStream)$
   295^I  [34mprivate[39;49;00m$
   296^I    [34mfunction[39;49;00m [32mGetCompressionRate[39;49;00m: [36mSingle[39;49;00m;$
   297^I  [34mpublic[39;49;00m$
   298^I    [34mconstructor[39;49;00m [32mCreate[39;49;00m(CompressionLevel: TCompressionLevel; Dest: TStream);$
   299^I    [34mdestructor[39;49;00m [32mDestroy[39;49;00m; [34moverride[39;49;00m;$
   300^I    [34mfunction[39;49;00m [32mRead[39;49;00m([34mvar[39;49;00m Buffer; Count: [36mLongint[39;49;00m): [36mLongint[39;49;00m; [34moverride[39;49;00m;$
   301^I    [34mfunction[39;49;00m [32mWrite[39;49;00m([34mconst[39;49;00m Buffer; Count: [36mLongint[39;49;00m): [36mLongint[39;49;00m; [34moverride[39;49;00m;$
   302^I    [34mfunction[39;49;00m [32mSeek[39;49;00m(Offset: [36mLongint[39;49;00m; Origin: [36mWord[39;49;00m): [36mLongint[39;49;00m; [34moverride[39;49;00m;$
   303^I    [34mproperty[39;49;00m CompressionRate: [36mSingle[39;49;00m [34mread[39;49;00m [32mGetCompressionRate[39;49;00m;$
   304^I    [34mproperty[39;49;00m OnProgress;$
   305^I  [34mend[39;49;00m;$
   306^I$
   307^I[37m{ TDecompressionStream decompresses data on the fly as data is read from it.[39;49;00m$
   308^I[37m[39;49;00m$
   309^I[37m  Compressed data comes from a separate source stream.  TDecompressionStream[39;49;00m$
   310^I[37m  is read-only and unidirectional; you can seek forward in the stream, but not[39;49;00m$
   311^I[37m  backwards.  The special case of setting the stream position to zero is[39;49;00m$
   312^I[37m  allowed.  Seeking forward decompresses data until the requested position in[39;49;00m$
   313^I[37m  the uncompressed data has been reached.  Seeking backwards, seeking relative[39;49;00m$
   314^I[37m  to the end of the stream, requesting the size of the stream, and writing to[39;49;00m$
   315^I[37m  the stream will raise an exception.[39;49;00m$
   316^I[37m[39;49;00m$
   317^I[37m  The Position property returns the number of bytes of uncompressed data that[39;49;00m$
   318^I[37m  have been read from the stream so far.[39;49;00m$
   319^I[37m[39;49;00m$
   320^I[37m  The OnProgress event is called each time the internal input buffer of[39;49;00m$
   321^I[37m  compressed data is exhausted and the next block is read from the input stream.[39;49;00m$
   322^I[37m  This is useful for updating a progress indicator when you are reading a[39;49;00m$
   323^I[37m  large chunk of data from the decompression stream in a single call.}[39;49;00m$
   324^I$
   325^I  TDecompressionStream = [34mclass[39;49;00m(TCustomZlibStream)$
   326^I  [34mpublic[39;49;00m$
   327^I    [34mconstructor[39;49;00m [32mCreate[39;49;00m(Source: TStream);$
   328^I    [34mdestructor[39;49;00m [32mDestroy[39;49;00m; [34moverride[39;49;00m;$
   329^I    [34mfunction[39;49;00m [32mRead[39;49;00m([34mvar[39;49;00m Buffer; Count: [36mLongint[39;49;00m): [36mLongint[39;49;00m; [34moverride[39;49;00m;$
   330^I    [34mfunction[39;49;00m [32mWrite[39;49;00m([34mconst[39;49;00m Buffer; Count: [36mLongint[39;49;00m): [36mLongint[39;49;00m; [34moverride[39;49;00m;$
   331^I    [34mfunction[39;49;00m [32mSeek[39;49;00m(Offset: [36mLongint[39;49;00m; Origin: [36mWord[39;49;00m): [36mLongint[39;49;00m; [34moverride[39;49;00m;$
   332^I    [34mproperty[39;49;00m OnProgress;$
   333^I  [34mend[39;49;00m;$
   334^I$
   335^I$
   336^I$
   337^I[37m{ CompressBuf compresses data, buffer to buffer, in one call.[39;49;00m$
   338^I[37m   In: InBuf = ptr to compressed data[39;49;00m$
   339^I[37m       InBytes = number of bytes in InBuf[39;49;00m$
   340^I[37m  Out: OutBuf = ptr to newly allocated buffer containing decompressed data[39;49;00m$
   341^I[37m       OutBytes = number of bytes in OutBuf   }[39;49;00m$
   342^I[34mprocedure[39;49;00m [32mCompressBuf[39;49;00m([34mconst[39;49;00m InBuf: [36mPointer[39;49;00m; InBytes: [36mInteger[39;49;00m;$
   343^I                      out OutBuf: [36mPointer[39;49;00m; out OutBytes: [36mInteger[39;49;00m);$
   344^I$
   345^I$
   346^I[37m{ DecompressBuf decompresses data, buffer to buffer, in one call.[39;49;00m$
   347^I[37m   In: InBuf = ptr to compressed data[39;49;00m$
   348^I[37m       InBytes = number of bytes in InBuf[39;49;00m$
   349^I[37m       OutEstimate = zero, or est. size of the decompressed data[39;49;00m$
   350^I[37m  Out: OutBuf = ptr to newly allocated buffer containing decompressed data[39;49;00m$
   351^I[37m       OutBytes = number of bytes in OutBuf   }[39;49;00m$
   352^I[34mprocedure[39;49;00m [32mDecompressBuf[39;49;00m([34mconst[39;49;00m InBuf: [36mPointer[39;49;00m; InBytes: [36mInteger[39;49;00m;$
   353^I OutEstimate: [36mInteger[39;49;00m; out OutBuf: [36mPointer[39;49;00m; out OutBytes: [36mInteger[39;49;00m);$
   354^I$
   355^I[34mconst[39;49;00m$
   356^I  zlib_version = [33m'[39;49;00m[33m1.1.3[39;49;00m[33m'[39;49;00m;$
   357^I$
   358^I[34mtype[39;49;00m$
   359^I  EZlibError = [34mclass[39;49;00m(Exception);$
   360^I  ECompressionError = [34mclass[39;49;00m(EZlibError);$
   361^I  EDecompressionError = [34mclass[39;49;00m(EZlibError);$
   362^I$
   363^I[34mfunction[39;49;00m [32madler32[39;49;00m(adler: [36mInteger[39;49;00m; buf: [36mPChar[39;49;00m; len: [36mInteger[39;49;00m): [36mInteger[39;49;00m;$
   364^I$
   365^I[34mimplementation[39;49;00m$
   366^I$
   367^I[34mconst[39;49;00m$
   368^I  Z_NO_FLUSH      = [34m0[39;49;00m;$
   369^I  Z_PARTIAL_FLUSH = [34m1[39;49;00m;$
   370^I  Z_SYNC_FLUSH    = [34m2[39;49;00m;$
   371^I  Z_FULL_FLUSH    = [34m3[39;49;00m;$
   372^I  Z_FINISH        = [34m4[39;49;00m;$
   373^I$
   374^I  Z_OK            = [34m0[39;49;00m;$
   375^I  Z_STREAM_END    = [34m1[39;49;00m;$
   376^I  Z_NEED_DICT     = [34m2[39;49;00m;$
   377^I  Z_ERRNO         = (-[34m1[39;49;00m);$
   378^I  Z_STREAM_ERROR  = (-[34m2[39;49;00m);$
   379^I  Z_DATA_ERROR    = (-[34m3[39;49;00m);$
   380^I  Z_MEM_ERROR     = (-[34m4[39;49;00m);$
   381^I  Z_BUF_ERROR     = (-[34m5[39;49;00m);$
   382^I  Z_VERSION_ERROR = (-[34m6[39;49;00m);$
   383^I$
   384^I  Z_NO_COMPRESSION       =   [34m0[39;49;00m;$
   385^I  Z_BEST_SPEED           =   [34m1[39;49;00m;$
   386^I  Z_BEST_COMPRESSION     =   [34m9[39;49;00m;$
   387^I  Z_DEFAULT_COMPRESSION  = (-[34m1[39;49;00m);$
   388^I$
   389^I  Z_FILTERED            = [34m1[39;49;00m;$
   390^I  Z_HUFFMAN_ONLY        = [34m2[39;49;00m;$
   391^I  Z_DEFAULT_STRATEGY    = [34m0[39;49;00m;$
   392^I$
   393^I  Z_BINARY   = [34m0[39;49;00m;$
   394^I  Z_ASCII    = [34m1[39;49;00m;$
   395^I  Z_UNKNOWN  = [34m2[39;49;00m;$
   396^I$
   397^I  Z_DEFLATED = [34m8[39;49;00m;$
   398^I$
   399^I  _z_errmsg: [34marray[39;49;00m[[34m0[39;49;00m..[34m9[39;49;00m] [34mof[39;49;00m [36mPChar[39;49;00m = ($
   400^I    [33m'[39;49;00m[33mneed dictionary[39;49;00m[33m'[39;49;00m,      [37m// Z_NEED_DICT      (2)[39;49;00m$
   401^I    [33m'[39;49;00m[33mstream end[39;49;00m[33m'[39;49;00m,           [37m// Z_STREAM_END     (1)[39;49;00m$
   402^I    [33m'[39;49;00m[33m'[39;49;00m,                     [37m// Z_OK             (0)[39;49;00m$
   403^I    [33m'[39;49;00m[33mfile error[39;49;00m[33m'[39;49;00m,           [37m// Z_ERRNO          (-1)[39;49;00m$
   404^I    [33m'[39;49;00m[33mstream error[39;49;00m[33m'[39;49;00m,         [37m// Z_STREAM_ERROR   (-2)[39;49;00m$
   405^I    [33m'[39;49;00m[33mdata error[39;49;00m[33m'[39;49;00m,           [37m// Z_DATA_ERROR     (-3)[39;49;00m$
   406^I    [33m'[39;49;00m[33minsufficient memory[39;49;00m[33m'[39;49;00m,  [37m// Z_MEM_ERROR      (-4)[39;49;00m$
   407^I    [33m'[39;49;00m[33mbuffer error[39;49;00m[33m'[39;49;00m,         [37m// Z_BUF_ERROR      (-5)[39;49;00m$
   408^I    [33m'[39;49;00m[33mincompatible version[39;49;00m[33m'[39;49;00m, [37m// Z_VERSION_ERROR  (-6)[39;49;00m$
   409^I    [33m'[39;49;00m[33m'[39;49;00m$
   410^I  );$
   411^I$
   412^I[37m{$L deflate.obj}[39;49;00m$
   413^I[37m{$L inflate.obj}[39;49;00m$
   414^I[37m{$L inftrees.obj}[39;49;00m$
   415^I[37m{$L trees.obj}[39;49;00m$
   416^I[37m{$L adler32.obj}[39;49;00m$
   417^I[37m{$L infblock.obj}[39;49;00m$
   418^I[37m{$L infcodes.obj}[39;49;00m$
   419^I[37m{$L infutil.obj}[39;49;00m$
   420^I[37m{$L inffast.obj}[39;49;00m$
   421^I$
   422^I[34mprocedure[39;49;00m [32m_tr_init[39;49;00m; [34mexternal[39;49;00m;$
   423^I[34mprocedure[39;49;00m [32m_tr_tally[39;49;00m; [34mexternal[39;49;00m;$
   424^I[34mprocedure[39;49;00m [32m_tr_flush_block[39;49;00m; [34mexternal[39;49;00m;$
   425^I[34mprocedure[39;49;00m [32m_tr_align[39;49;00m; [34mexternal[39;49;00m;$
   426^I[34mprocedure[39;49;00m [32m_tr_stored_block[39;49;00m; [34mexternal[39;49;00m;$
   427^I[34mfunction[39;49;00m [32madler32[39;49;00m; [34mexternal[39;49;00m;$
   428^I[34mprocedure[39;49;00m [32minflate_blocks_new[39;49;00m; [34mexternal[39;49;00m;$
   429^I[34mprocedure[39;49;00m [32minflate_blocks[39;49;00m; [34mexternal[39;49;00m;$
   430^I[34mprocedure[39;49;00m [32minflate_blocks_reset[39;49;00m; [34mexternal[39;49;00m;$
   431^I[34mprocedure[39;49;00m [32minflate_blocks_free[39;49;00m; [34mexternal[39;49;00m;$
   432^I[34mprocedure[39;49;00m [32minflate_set_dictionary[39;49;00m; [34mexternal[39;49;00m;$
   433^I[34mprocedure[39;49;00m [32minflate_trees_bits[39;49;00m; [34mexternal[39;49;00m;$
   434^I[34mprocedure[39;49;00m [32minflate_trees_dynamic[39;49;00m; [34mexternal[39;49;00m;$
   435^I[34mprocedure[39;49;00m [32minflate_trees_fixed[39;49;00m; [34mexternal[39;49;00m;$
   436^I[34mprocedure[39;49;00m [32minflate_codes_new[39;49;00m; [34mexternal[39;49;00m;$
   437^I[34mprocedure[39;49;00m [32minflate_codes[39;49;00m; [34mexternal[39;49;00m;$
   438^I[34mprocedure[39;49;00m [32minflate_codes_free[39;49;00m; [34mexternal[39;49;00m;$
   439^I[34mprocedure[39;49;00m [32m_inflate_mask[39;49;00m; [34mexternal[39;49;00m;$
   440^I[34mprocedure[39;49;00m [32minflate_flush[39;49;00m; [34mexternal[39;49;00m;$
   441^I[34mprocedure[39;49;00m [32minflate_fast[39;49;00m; [34mexternal[39;49;00m;$
   442^I$
   443^I[34mprocedure[39;49;00m [32m_memset[39;49;00m(P: [36mPointer[39;49;00m; B: [36mByte[39;49;00m; count: [36mInteger[39;49;00m);[34mcdecl[39;49;00m;$
   444^I[34mbegin[39;49;00m$
   445^I  [36mFillChar[39;49;00m(P^, count, B);$
   446^I[34mend[39;49;00m;$
   447^I$
   448^I[34mprocedure[39;49;00m [32m_memcpy[39;49;00m(dest, source: [36mPointer[39;49;00m; count: [36mInteger[39;49;00m);[34mcdecl[39;49;00m;$
   449^I[34mbegin[39;49;00m$
   450^I  [36mMove[39;49;00m(source^, dest^, count);$
   451^I[34mend[39;49;00m;$
   452^I$
   453^I$
   454^I$
   455^I[37m// deflate compresses data[39;49;00m$
   456^I[34mfunction[39;49;00m [32mdeflateInit_[39;49;00m([34mvar[39;49;00m strm: TZStreamRec; level: [36mInteger[39;49;00m; version: [36mPChar[39;49;00m;$
   457^I  recsize: [36mInteger[39;49;00m): [36mInteger[39;49;00m; [34mexternal[39;49;00m;$
   458^I[34mfunction[39;49;00m [32mdeflate[39;49;00m([34mvar[39;49;00m strm: TZStreamRec; [36mflush[39;49;00m: [36mInteger[39;49;00m): [36mInteger[39;49;00m; [34mexternal[39;49;00m;$
   459^I[34mfunction[39;49;00m [32mdeflateEnd[39;49;00m([34mvar[39;49;00m strm: TZStreamRec): [36mInteger[39;49;00m; [34mexternal[39;49;00m;$
   460^I$
   461^I[37m// inflate decompresses data[39;49;00m$
   462^I[34mfunction[39;49;00m [32minflateInit_[39;49;00m([34mvar[39;49;00m strm: TZStreamRec; version: [36mPChar[39;49;00m;$
   463^I  recsize: [36mInteger[39;49;00m): [36mInteger[39;49;00m; [34mexternal[39;49;00m;$
   464^I[34mfunction[39;49;00m [32minflate[39;49;00m([34mvar[39;49;00m strm: TZStreamRec; [36mflush[39;49;00m: [36mInteger[39;49;00m): [36mInteger[39;49;00m; [34mexternal[39;49;00m;$
   465^I[34mfunction[39;49;00m [32minflateEnd[39;49;00m([34mvar[39;49;00m strm: TZStreamRec): [36mInteger[39;49;00m; [34mexternal[39;49;00m;$
   466^I[34mfunction[39;49;00m [32minflateReset[39;49;00m([34mvar[39;49;00m strm: TZStreamRec): [36mInteger[39;49;00m; [34mexternal[39;49;00m;$
   467^I$
   468^I$
   469^I[34mfunction[39;49;00m [32mzcalloc[39;49;00m(AppData: [36mPointer[39;49;00m; Items, Size: [36mInteger[39;49;00m): [36mPointer[39;49;00m;$
   470^I[34mbegin[39;49;00m$
   471^I  [36mGetMem[39;49;00m([36mResult[39;49;00m, Items*Size);$
   472^I[34mend[39;49;00m;$
   473^I$
   474^I[34mprocedure[39;49;00m [32mzcfree[39;49;00m(AppData, Block: [36mPointer[39;49;00m);$
   475^I[34mbegin[39;49;00m$
   476^I  [36mFreeMem[39;49;00m(Block);$
   477^I[34mend[39;49;00m;$
   478^I$
   479^I[34mfunction[39;49;00m [32mzlibCheck[39;49;00m(code: [36mInteger[39;49;00m): [36mInteger[39;49;00m;$
   480^I[34mbegin[39;49;00m$
   481^I  [36mResult[39;49;00m := code;$
   482^I  [34mif[39;49;00m code < [34m0[39;49;00m [34mthen[39;49;00m$
   483^I    [34mraise[39;49;00m EZlibError.Create([33m'[39;49;00m[33merror[39;49;00m[33m'[39;49;00m);    [37m//!![39;49;00m$
   484^I[34mend[39;49;00m;$
   485^I$
   486^I[34mfunction[39;49;00m [32mCCheck[39;49;00m(code: [36mInteger[39;49;00m): [36mInteger[39;49;00m;$
   487^I[34mbegin[39;49;00m$
   488^I  [36mResult[39;49;00m := code;$
   489^I  [34mif[39;49;00m code < [34m0[39;49;00m [34mthen[39;49;00m$
   490^I    [34mraise[39;49;00m ECompressionError.Create([33m'[39;49;00m[33merror[39;49;00m[33m'[39;49;00m); [37m//!![39;49;00m$
   491^I[34mend[39;49;00m;$
   492^I$
   493^I[34mfunction[39;49;00m [32mDCheck[39;49;00m(code: [36mInteger[39;49;00m): [36mInteger[39;49;00m;$
   494^I[34mbegin[39;49;00m$
   495^I  [36mResult[39;49;00m := code;$
   496^I  [34mif[39;49;00m code < [34m0[39;49;00m [34mthen[39;49;00m$
   497^I    [34mraise[39;49;00m EDecompressionError.Create([33m'[39;49;00m[33merror[39;49;00m[33m'[39;49;00m);  [37m//!![39;49;00m$
   498^I[34mend[39;49;00m;$
   499^I$
   500^I[34mprocedure[39;49;00m [32mCompressBuf[39;49;00m([34mconst[39;49;00m InBuf: [36mPointer[39;49;00m; InBytes: [36mInteger[39;49;00m;$
   501^I                      out OutBuf: [36mPointer[39;49;00m; out OutBytes: [36mInteger[39;49;00m);$
   502^I[34mvar[39;49;00m$
   503^I  strm: TZStreamRec;$
   504^I  P: [36mPointer[39;49;00m;$
   505^I[34mbegin[39;49;00m$
   506^I  [36mFillChar[39;49;00m(strm, [36msizeof[39;49;00m(strm), [34m0[39;49;00m);$
   507^I  OutBytes := ((InBytes + (InBytes [34mdiv[39;49;00m [34m10[39;49;00m) + [34m12[39;49;00m) + [34m255[39;49;00m) [34mand[39;49;00m [34mnot[39;49;00m [34m255[39;49;00m;$
   508^I  [36mGetMem[39;49;00m(OutBuf, OutBytes);$
   509^I  [34mtry[39;49;00m$
   510^I    strm.next_in := InBuf;$
   511^I    strm.avail_in := InBytes;$
   512^I    strm.next_out := OutBuf;$
   513^I    strm.avail_out := OutBytes;$
   514^I    CCheck(deflateInit_(strm, Z_BEST_COMPRESSION, zlib_version, [36msizeof[39;49;00m(strm)));$
   515^I    [34mtry[39;49;00m$
   516^I      [34mwhile[39;49;00m CCheck(deflate(strm, Z_FINISH)) <> Z_STREAM_END [34mdo[39;49;00m$
   517^I      [34mbegin[39;49;00m$
   518^I        P := OutBuf;$
   519^I        [36mInc[39;49;00m(OutBytes, [34m256[39;49;00m);$
   520^I        [36mReallocMem[39;49;00m(OutBuf, OutBytes);$
   521^I        strm.next_out := [36mPChar[39;49;00m([36mInteger[39;49;00m(OutBuf) + ([36mInteger[39;49;00m(strm.next_out) - [36mInteger[39;49;00m(P)));$
   522^I        strm.avail_out := [34m256[39;49;00m;$
   523^I      [34mend[39;49;00m;$
   524^I    [34mfinally[39;49;00m$
   525^I      CCheck(deflateEnd(strm));$
   526^I    [34mend[39;49;00m;$
   527^I    [36mReallocMem[39;49;00m(OutBuf, strm.total_out);$
   528^I    OutBytes := strm.total_out;$
   529^I  [34mexcept[39;49;00m$
   530^I    [36mFreeMem[39;49;00m(OutBuf);$
   531^I    [34mraise[39;49;00m$
   532^I  [34mend[39;49;00m;$
   533^I[34mend[39;49;00m;$
   534^I$
   535^I$
   536^I[34mprocedure[39;49;00m [32mDecompressBuf[39;49;00m([34mconst[39;49;00m InBuf: [36mPointer[39;49;00m; InBytes: [36mInteger[39;49;00m;$
   537^I  OutEstimate: [36mInteger[39;49;00m; out OutBuf: [36mPointer[39;49;00m; out OutBytes: [36mInteger[39;49;00m);$
   538^I[34mvar[39;49;00m$
   539^I  strm: TZStreamRec;$
   540^I  P: [36mPointer[39;49;00m;$
   541^I  BufInc: [36mInteger[39;49;00m;$
   542^I[34mbegin[39;49;00m$
   543^I  [36mFillChar[39;49;00m(strm, [36msizeof[39;49;00m(strm), [34m0[39;49;00m);$
   544^I  BufInc := (InBytes + [34m255[39;49;00m) [34mand[39;49;00m [34mnot[39;49;00m [34m255[39;49;00m;$
   545^I  [34mif[39;49;00m OutEstimate = [34m0[39;49;00m [34mthen[39;49;00m$
   546^I    OutBytes := BufInc$
   547^I  [34melse[39;49;00m$
   548^I    OutBytes := OutEstimate;$
   549^I  [36mGetMem[39;49;00m(OutBuf, OutBytes);$
   550^I  [34mtry[39;49;00m$
   551^I    strm.next_in := InBuf;$
   552^I    strm.avail_in := InBytes;$
   553^I    strm.next_out := OutBuf;$
   554^I    strm.avail_out := OutBytes;$
   555^I    DCheck(inflateInit_(strm, zlib_version, [36msizeof[39;49;00m(strm)));$
   556^I    [34mtry[39;49;00m$
   557^I      [34mwhile[39;49;00m DCheck(inflate(strm, Z_FINISH)) <> Z_STREAM_END [34mdo[39;49;00m$
   558^I      [34mbegin[39;49;00m$
   559^I        P := OutBuf;$
   560^I        [36mInc[39;49;00m(OutBytes, BufInc);$
   561^I        [36mReallocMem[39;49;00m(OutBuf, OutBytes);$
   562^I        strm.next_out := [36mPChar[39;49;00m([36mInteger[39;49;00m(OutBuf) + ([36mInteger[39;49;00m(strm.next_out) - [36mInteger[39;49;00m(P)));$
   563^I        strm.avail_out := BufInc;$
   564^I      [34mend[39;49;00m;$
   565^I    [34mfinally[39;49;00m$
   566^I      DCheck(inflateEnd(strm));$
   567^I    [34mend[39;49;00m;$
   568^I    [36mReallocMem[39;49;00m(OutBuf, strm.total_out);$
   569^I    OutBytes := strm.total_out;$
   570^I  [34mexcept[39;49;00m$
   571^I    [36mFreeMem[39;49;00m(OutBuf);$
   572^I    [34mraise[39;49;00m$
   573^I  [34mend[39;49;00m;$
   574^I[34mend[39;49;00m;$
   575^I$
   576^I$
   577^I[37m// TCustomZlibStream[39;49;00m$
   578^I$
   579^I[34mconstructor[39;49;00m [04m[32mTCustomZLibStream[39;49;00m.[32mCreate[39;49;00m(Strm: TStream);$
   580^I[34mbegin[39;49;00m$
   581^I  [34minherited[39;49;00m Create;$
   582^I  FStrm := Strm;$
   583^I  FStrmPos := Strm.Position;$
   584^I[34mend[39;49;00m;$
   585^I$
   586^I[34mprocedure[39;49;00m [04m[32mTCustomZLibStream[39;49;00m.[32mProgress[39;49;00m(Sender: [36mTObject[39;49;00m);$
   587^I[34mbegin[39;49;00m$
   588^I  [34mif[39;49;00m [36mAssigned[39;49;00m(FOnProgress) [34mthen[39;49;00m FOnProgress(Sender);$
   589^I[34mend[39;49;00m;$
   590^I$
   591^I$
   592^I[37m// TCompressionStream[39;49;00m$
   593^I$
   594^I[34mconstructor[39;49;00m [04m[32mTCompressionStream[39;49;00m.[32mCreate[39;49;00m(CompressionLevel: TCompressionLevel;$
   595^I  Dest: TStream);$
   596^I[34mconst[39;49;00m$
   597^I  Levels: [34marray[39;49;00m [TCompressionLevel] [34mof[39;49;00m [36mShortInt[39;49;00m =$
   598^I    (Z_NO_COMPRESSION, Z_BEST_SPEED, Z_DEFAULT_COMPRESSION, Z_BEST_COMPRESSION);$
   599^I[34mbegin[39;49;00m$
   600^I  [34minherited[39;49;00m Create(Dest);$
   601^I  FZRec.next_out := FBuffer;$
   602^I  FZRec.avail_out := [36msizeof[39;49;00m(FBuffer);$
   603^I  CCheck(deflateInit_(FZRec, Levels[CompressionLevel], zlib_version, [36msizeof[39;49;00m(FZRec)));$
   604^I[34mend[39;49;00m;$
   605^I$
   606^I[34mdestructor[39;49;00m [04m[32mTCompressionStream[39;49;00m.[32mDestroy[39;49;00m;$
   607^I[34mbegin[39;49;00m$
   608^I  FZRec.next_in := [34mnil[39;49;00m;$
   609^I  FZRec.avail_in := [34m0[39;49;00m;$
   610^I  [34mtry[39;49;00m$
   611^I    [34mif[39;49;00m FStrm.Position <> FStrmPos [34mthen[39;49;00m FStrm.Position := FStrmPos;$
   612^I    [34mwhile[39;49;00m (CCheck(deflate(FZRec, Z_FINISH)) <> Z_STREAM_END)$
   613^I      [34mand[39;49;00m (FZRec.avail_out = [34m0[39;49;00m) [34mdo[39;49;00m$
   614^I    [34mbegin[39;49;00m$
   615^I      FStrm.WriteBuffer(FBuffer, [36msizeof[39;49;00m(FBuffer));$
   616^I      FZRec.next_out := FBuffer;$
   617^I      FZRec.avail_out := [36msizeof[39;49;00m(FBuffer);$
   618^I    [34mend[39;49;00m;$
   619^I    [34mif[39;49;00m FZRec.avail_out < [36msizeof[39;49;00m(FBuffer) [34mthen[39;49;00m$
   620^I      FStrm.WriteBuffer(FBuffer, [36msizeof[39;49;00m(FBuffer) - FZRec.avail_out);$
   621^I  [34mfinally[39;49;00m$
   622^I    deflateEnd(FZRec);$
   623^I  [34mend[39;49;00m;$
   624^I  [34minherited[39;49;00m Destroy;$
   625^I[34mend[39;49;00m;$
   626^I$
   627^I[34mfunction[39;49;00m [04m[32mTCompressionStream[39;49;00m.[32mRead[39;49;00m([34mvar[39;49;00m Buffer; Count: [36mLongint[39;49;00m): [36mLongint[39;49;00m;$
   628^I[34mbegin[39;49;00m$
   629^I  [34mraise[39;49;00m ECompressionError.Create([33m'[39;49;00m[33mInvalid stream operation[39;49;00m[33m'[39;49;00m);$
   630^I[34mend[39;49;00m;$
   631^I$
   632^I[34mfunction[39;49;00m [04m[32mTCompressionStream[39;49;00m.[32mWrite[39;49;00m([34mconst[39;49;00m Buffer; Count: [36mLongint[39;49;00m): [36mLongint[39;49;00m;$
   633^I[34mbegin[39;49;00m$
   634^I  FZRec.next_in := @Buffer;$
   635^I  FZRec.avail_in := Count;$
   636^I  [34mif[39;49;00m FStrm.Position <> FStrmPos [34mthen[39;49;00m FStrm.Position := FStrmPos;$
   637^I  [34mwhile[39;49;00m (FZRec.avail_in > [34m0[39;49;00m) [34mdo[39;49;00m$
   638^I  [34mbegin[39;49;00m$
   639^I    CCheck(deflate(FZRec, [34m0[39;49;00m));$
   640^I    [34mif[39;49;00m FZRec.avail_out = [34m0[39;49;00m [34mthen[39;49;00m$
   641^I    [34mbegin[39;49;00m$
   642^I      FStrm.WriteBuffer(FBuffer, [36msizeof[39;49;00m(FBuffer));$
   643^I      FZRec.next_out := FBuffer;$
   644^I      FZRec.avail_out := [36msizeof[39;49;00m(FBuffer);$
   645^I      FStrmPos := FStrm.Position;$
   646^I      Progress([34mSelf[39;49;00m);$
   647^I    [34mend[39;49;00m;$
   648^I  [34mend[39;49;00m;$
   649^I  [36mResult[39;49;00m := Count;$
   650^I[34mend[39;49;00m;$
   651^I$
   652^I[34mfunction[39;49;00m [04m[32mTCompressionStream[39;49;00m.[32mSeek[39;49;00m(Offset: [36mLongint[39;49;00m; Origin: [36mWord[39;49;00m): [36mLongint[39;49;00m;$
   653^I[34mbegin[39;49;00m$
   654^I  [34mif[39;49;00m (Offset = [34m0[39;49;00m) [34mand[39;49;00m (Origin = soFromCurrent) [34mthen[39;49;00m$
   655^I    [36mResult[39;49;00m := FZRec.total_in$
   656^I  [34melse[39;49;00m$
   657^I    [34mraise[39;49;00m ECompressionError.Create([33m'[39;49;00m[33mInvalid stream operation[39;49;00m[33m'[39;49;00m);$
   658^I[34mend[39;49;00m;$
   659^I$
   660^I[34mfunction[39;49;00m [04m[32mTCompressionStream[39;49;00m.[32mGetCompressionRate[39;49;00m: [36mSingle[39;49;00m;$
   661^I[34mbegin[39;49;00m$
   662^I  [34mif[39;49;00m FZRec.total_in = [34m0[39;49;00m [34mthen[39;49;00m$
   663^I    [36mResult[39;49;00m := [34m0[39;49;00m$
   664^I  [34melse[39;49;00m$
   665^I    [36mResult[39;49;00m := ([34m1.0[39;49;00m - (FZRec.total_out / FZRec.total_in)) * [34m10[39;49;00m[34m0.0[39;49;00m;$
   666^I[34mend[39;49;00m;$
   667^I$
   668^I$
   669^I[37m// TDecompressionStream[39;49;00m$
   670^I$
   671^I[34mconstructor[39;49;00m [04m[32mTDecompressionStream[39;49;00m.[32mCreate[39;49;00m(Source: TStream);$
   672^I[34mbegin[39;49;00m$
   673^I  [34minherited[39;49;00m Create(Source);$
   674^I  FZRec.next_in := FBuffer;$
   675^I  FZRec.avail_in := [34m0[39;49;00m;$
   676^I  DCheck(inflateInit_(FZRec, zlib_version, [36msizeof[39;49;00m(FZRec)));$
   677^I[34mend[39;49;00m;$
   678^I$
   679^I[34mdestructor[39;49;00m [04m[32mTDecompressionStream[39;49;00m.[32mDestroy[39;49;00m;$
   680^I[34mbegin[39;49;00m$
   681^I  inflateEnd(FZRec);$
   682^I  [34minherited[39;49;00m Destroy;$
   683^I[34mend[39;49;00m;$
   684^I$
   685^I[34mfunction[39;49;00m [04m[32mTDecompressionStream[39;49;00m.[32mRead[39;49;00m([34mvar[39;49;00m Buffer; Count: [36mLongint[39;49;00m): [36mLongint[39;49;00m;$
   686^I[34mbegin[39;49;00m$
   687^I  FZRec.next_out := @Buffer;$
   688^I  FZRec.avail_out := Count;$
   689^I  [34mif[39;49;00m FStrm.Position <> FStrmPos [34mthen[39;49;00m FStrm.Position := FStrmPos;$
   690^I  [34mwhile[39;49;00m (FZRec.avail_out > [34m0[39;49;00m) [34mdo[39;49;00m$
   691^I  [34mbegin[39;49;00m$
   692^I    [34mif[39;49;00m FZRec.avail_in = [34m0[39;49;00m [34mthen[39;49;00m$
   693^I    [34mbegin[39;49;00m$
   694^I      FZRec.avail_in := FStrm.Read(FBuffer, [36msizeof[39;49;00m(FBuffer));$
   695^I      [34mif[39;49;00m FZRec.avail_in = [34m0[39;49;00m [34mthen[39;49;00m$
   696^I        [34mbegin[39;49;00m$
   697^I          [36mResult[39;49;00m := Count - FZRec.avail_out;$
   698^I          [34mExit[39;49;00m;$
   699^I        [34mend[39;49;00m;$
   700^I      FZRec.next_in := FBuffer;$
   701^I      FStrmPos := FStrm.Position;$
   702^I      Progress([34mSelf[39;49;00m);$
   703^I    [34mend[39;49;00m;$
   704^I    DCheck(inflate(FZRec, [34m0[39;49;00m));$
   705^I  [34mend[39;49;00m;$
   706^I  [36mResult[39;49;00m := Count;$
   707^I[34mend[39;49;00m;$
   708^I$
   709^I[34mfunction[39;49;00m [04m[32mTDecompressionStream[39;49;00m.[32mWrite[39;49;00m([34mconst[39;49;00m Buffer; Count: [36mLongint[39;49;00m): [36mLongint[39;49;00m;$
   710^I[34mbegin[39;49;00m$
   711^I  [34mraise[39;49;00m EDecompressionError.Create([33m'[39;49;00m[33mInvalid stream operation[39;49;00m[33m'[39;49;00m);$
   712^I[34mend[39;49;00m;$
   713^I$
   714^I[34mfunction[39;49;00m [04m[32mTDecompressionStream[39;49;00m.[32mSeek[39;49;00m(Offset: [36mLongint[39;49;00m; Origin: [36mWord[39;49;00m): [36mLongint[39;49;00m;$
   715^I[34mvar[39;49;00m$
   716^I  I: [36mInteger[39;49;00m;$
   717^I  Buf: [34marray[39;49;00m [[34m0[39;49;00m..[34m4095[39;49;00m] [34mof[39;49;00m [36mChar[39;49;00m;$
   718^I[34mbegin[39;49;00m$
   719^I  [34mif[39;49;00m (Offset = [34m0[39;49;00m) [34mand[39;49;00m (Origin = soFromBeginning) [34mthen[39;49;00m$
   720^I  [34mbegin[39;49;00m$
   721^I    DCheck(inflateReset(FZRec));$
   722^I    FZRec.next_in := FBuffer;$
   723^I    FZRec.avail_in := [34m0[39;49;00m;$
   724^I    FStrm.Position := [34m0[39;49;00m;$
   725^I    FStrmPos := [34m0[39;49;00m;$
   726^I  [34mend[39;49;00m$
   727^I  [34melse[39;49;00m [34mif[39;49;00m ( (Offset >= [34m0[39;49;00m) [34mand[39;49;00m (Origin = soFromCurrent)) [34mor[39;49;00m$
   728^I          ( ((Offset - FZRec.total_out) > [34m0[39;49;00m) [34mand[39;49;00m (Origin = soFromBeginning)) [34mthen[39;49;00m$
   729^I  [34mbegin[39;49;00m$
   730^I    [34mif[39;49;00m Origin = soFromBeginning [34mthen[39;49;00m [36mDec[39;49;00m(Offset, FZRec.total_out);$
   731^I    [34mif[39;49;00m Offset > [34m0[39;49;00m [34mthen[39;49;00m$
   732^I    [34mbegin[39;49;00m$
   733^I      [34mfor[39;49;00m I := [34m1[39;49;00m [34mto[39;49;00m Offset [34mdiv[39;49;00m [36msizeof[39;49;00m(Buf) [34mdo[39;49;00m$
   734^I        ReadBuffer(Buf, [36msizeof[39;49;00m(Buf));$
   735^I      ReadBuffer(Buf, Offset [34mmod[39;49;00m [36msizeof[39;49;00m(Buf));$
   736^I    [34mend[39;49;00m;$
   737^I  [34mend[39;49;00m$
   738^I  [34melse[39;49;00m$
   739^I    [34mraise[39;49;00m EDecompressionError.Create([33m'[39;49;00m[33mInvalid stream operation[39;49;00m[33m'[39;49;00m);$
   740^I  [36mResult[39;49;00m := FZRec.total_out;$
   741^I[34mend[39;49;00m;$
   742^I$
   743^I[34mend[39;49;00m.$

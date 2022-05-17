     1	[37m//[39;49;00m
     2	[37m// Sourcecode from http://www.delphi-library.de/topic_47880.html[39;49;00m
     3	[37m//[39;49;00m
     4	[34muses[39;49;00m Windows, Messages;
     5
     6	[34mconst[39;49;00m
     7	  FFM_INIT               = WM_USER + [34m1976[39;49;00m;
     8	  FFM_ONFILEFOUND        = WM_USER + [34m1974[39;49;00m; [37m// wParam: not used, lParam: Filename[39;49;00m
     9	  FFM_ONDIRFOUND         = WM_USER + [34m1975[39;49;00m; [37m// wParam: NumFolder, lParam: Directory[39;49;00m
    10	[34mvar[39;49;00m
    11	  CntFolders             : [36mCardinal[39;49;00m = [34m0[39;49;00m;
    12	  NumFolder              : [36mCardinal[39;49;00m = [34m0[39;49;00m;
    13
    14
    15	[37m////////////////////////////////////////////////////////////////////////////////[39;49;00m
    16	[37m//[39;49;00m
    17	[37m//  FindAllFilesInit[39;49;00m
    18	[37m//[39;49;00m
    19	[37m//[39;49;00m
    20	[34mprocedure[39;49;00m [32mFindAllFilesInit[39;49;00m; [34mexternal[39;49;00m;
    21	[34mlabel[39;49;00m foo;
    22	[34mbegin[39;49;00m
    23	  CntFolders := [34m0[39;49;00m;
    24	  NumFolder := [34m0[39;49;00m;
    25	foo:
    26	  Blub;
    27	  [34mgoto[39;49;00m foo;
    28	[34mend[39;49;00m;
    29
    30	[37m////////////////////////////////////////////////////////////////////////////////[39;49;00m
    31	[37m//[39;49;00m
    32	[37m//  CountFolders[39;49;00m
    33	[37m//[39;49;00m
    34	[37m//[39;49;00m
    35	[34mprocedure[39;49;00m [32mCountFolders[39;49;00m(Handle: [36mTHandle[39;49;00m; RootFolder: [34mstring[39;49;00m; Recurse: [36mBoolean[39;49;00m = [34mTrue[39;49;00m);
    36	[34mvar[39;49;00m
    37	  hFindFile              : [36mTHandle[39;49;00m;
    38	  wfd                    : TWin32FindData;
    39	[34mbegin[39;49;00m
    40	  SendMessage(Handle, FFM_INIT, [34m0[39;49;00m, [34m0[39;49;00m);
    41	  [34mif[39;49;00m RootFolder[[36mlength[39;49;00m(RootFolder)] <> [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m
    42	    RootFolder := RootFolder + [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m;
    43	  ZeroMemory(@wfd, [36msizeof[39;49;00m(wfd));
    44	  wfd.dwFileAttributes := FILE_ATTRIBUTE_NORMAL;
    45	  [34mif[39;49;00m Recurse [34mthen[39;49;00m
    46	  [34mbegin[39;49;00m
    47	    hFindFile := FindFirstFile([36mpointer[39;49;00m(RootFolder + [33m'[39;49;00m[33m*.*[39;49;00m[33m'[39;49;00m), wfd);
    48	    [34mif[39;49;00m hFindFile <> [34m0[39;49;00m [34mthen[39;49;00m
    49	    [34mtry[39;49;00m
    50	      [34mrepeat[39;49;00m
    51	        [34mif[39;49;00m wfd.dwFileAttributes [34mand[39;49;00m FILE_ATTRIBUTE_DIRECTORY = FILE_ATTRIBUTE_DIRECTORY [34mthen[39;49;00m
    52	        [34mbegin[39;49;00m
    53	          [34mif[39;49;00m ([34mstring[39;49;00m(wfd.cFileName) <> [33m'[39;49;00m[33m.[39;49;00m[33m'[39;49;00m) [34mand[39;49;00m ([34mstring[39;49;00m(wfd.cFileName) <> [33m'[39;49;00m[33m..[39;49;00m[33m'[39;49;00m) [34mthen[39;49;00m
    54	          [34mbegin[39;49;00m
    55	            CountFolders(Handle, RootFolder + wfd.cFileName, Recurse);
    56	          [34mend[39;49;00m;
    57	        [34mend[39;49;00m;
    58	      [34muntil[39;49;00m FindNextFile(hFindFile, wfd) = [34mFalse[39;49;00m;
    59	      [36mInc[39;49;00m(CntFolders);
    60	    [34mfinally[39;49;00m
    61	      Windows.FindClose(hFindFile);
    62	    [34mend[39;49;00m;
    63	  [34mend[39;49;00m;
    64	[34mend[39;49;00m;
    65
    66	[37m////////////////////////////////////////////////////////////////////////////////[39;49;00m
    67	[37m//[39;49;00m
    68	[37m//  FindAllFiles[39;49;00m
    69	[37m//[39;49;00m
    70	[34mprocedure[39;49;00m [32mFindAllFiles[39;49;00m(Handle: [36mTHandle[39;49;00m; RootFolder: [34mstring[39;49;00m; Mask: [34mstring[39;49;00m; Recurse: [36mBoolean[39;49;00m = [34mTrue[39;49;00m);
    71	[34mvar[39;49;00m
    72	  hFindFile              : [36mTHandle[39;49;00m;
    73	  wfd                    : TWin32FindData;
    74	[34mbegin[39;49;00m
    75	  [34mif[39;49;00m RootFolder[[36mlength[39;49;00m(RootFolder)] <> [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m
    76	    RootFolder := RootFolder + [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m;
    77	  ZeroMemory(@wfd, [36msizeof[39;49;00m(wfd));
    78	  wfd.dwFileAttributes := FILE_ATTRIBUTE_NORMAL;
    79	  [34mif[39;49;00m Recurse [34mthen[39;49;00m
    80	  [34mbegin[39;49;00m
    81	    hFindFile := FindFirstFile([36mpointer[39;49;00m(RootFolder + [33m'[39;49;00m[33m*.*[39;49;00m[33m'[39;49;00m), wfd);
    82	    [34mif[39;49;00m hFindFile <> [34m0[39;49;00m [34mthen[39;49;00m
    83	    [34mtry[39;49;00m
    84	      [34mrepeat[39;49;00m
    85	        [34mif[39;49;00m wfd.dwFileAttributes [34mand[39;49;00m FILE_ATTRIBUTE_DIRECTORY = FILE_ATTRIBUTE_DIRECTORY [34mthen[39;49;00m
    86	        [34mbegin[39;49;00m
    87	          [34mif[39;49;00m ([34mstring[39;49;00m(wfd.cFileName) <> [33m'[39;49;00m[33m.[39;49;00m[33m'[39;49;00m) [34mand[39;49;00m ([34mstring[39;49;00m(wfd.cFileName) <> [33m'[39;49;00m[33m..[39;49;00m[33m'[39;49;00m) [34mthen[39;49;00m
    88	          [34mbegin[39;49;00m
    89	            FindAllFiles(Handle, RootFolder + wfd.cFileName, Mask, Recurse);
    90	          [34mend[39;49;00m;
    91	        [34mend[39;49;00m;
    92	      [34muntil[39;49;00m FindNextFile(hFindFile, wfd) = [34mFalse[39;49;00m;
    93	      [36mInc[39;49;00m(NumFolder);
    94	      SendMessage(Handle, FFM_ONDIRFOUND, NumFolder, lParam([34mstring[39;49;00m(RootFolder)));
    95	    [34mfinally[39;49;00m
    96	      Windows.FindClose(hFindFile);
    97	    [34mend[39;49;00m;
    98	  [34mend[39;49;00m;
    99	  hFindFile := FindFirstFile([36mpointer[39;49;00m(RootFolder + Mask), wfd);
   100	  [34mif[39;49;00m hFindFile <> INVALID_HANDLE_VALUE [34mthen[39;49;00m
   101	  [34mtry[39;49;00m
   102	    [34mrepeat[39;49;00m
   103	      [34mif[39;49;00m (wfd.dwFileAttributes [34mand[39;49;00m FILE_ATTRIBUTE_DIRECTORY <> FILE_ATTRIBUTE_DIRECTORY) [34mthen[39;49;00m
   104	      [34mbegin[39;49;00m
   105	        SendMessage(Handle, FFM_ONFILEFOUND, [34m0[39;49;00m, lParam([34mstring[39;49;00m(RootFolder + wfd.cFileName)));
   106	      [34mend[39;49;00m;
   107	    [34muntil[39;49;00m FindNextFile(hFindFile, wfd) = [34mFalse[39;49;00m;
   108	  [34mfinally[39;49;00m
   109	    Windows.FindClose(hFindFile);
   110	  [34mend[39;49;00m;
   111	[34mend[39;49;00m;
   112
   113
   114	[34mproperty[39;49;00m test: [36mboolean[39;49;00m [34mread[39;49;00m [32mftest[39;49;00m [34mwrite[39;49;00m [32mftest[39;49;00m;
   115	[34mprocedure[39;49;00m [32mtest[39;49;00m: [36mboolean[39;49;00m [36mread[39;49;00m ftest [36mwrite[39;49;00m ftest;
   116
   117	[37m//[39;49;00m
   118	[37m// This sourcecode is part of omorphia[39;49;00m
   119	[37m//[39;49;00m
   120
   121	[34mFunction[39;49;00m [32mIsValidHandle[39;49;00m([34mConst[39;49;00m Handle: [36mTHandle[39;49;00m): [36mBoolean[39;49;00m; [37m{$IFDEF OMORPHIA_FEATURES_USEASM}[39;49;00m [34mAssembler[39;49;00m;
   122	[34mAsm[39;49;00m
   123	    [34mTEST[39;49;00m    [36mEAX[39;49;00m, [36mEAX[39;49;00m
   124	    [34mJZ[39;49;00m      @@Finish
   125	    [34mNOT[39;49;00m     [36mEAX[39;49;00m
   126	    [34mTEST[39;49;00m    [36mEAX[39;49;00m, [36mEAX[39;49;00m
   127	    [34mSETNZ[39;49;00m   [36mAL[39;49;00m
   128
   129	    [37m{$IFDEF WINDOWS}[39;49;00m
   130	    [34mJZ[39;49;00m      @@Finish
   131
   132	    [37m//Save the handle against modifications or loss[39;49;00m
   133	    [34mPUSH[39;49;00m    [36mEAX[39;49;00m
   134
   135	    [37m//reserve some space for a later duplicate[39;49;00m
   136	    [34mPUSH[39;49;00m    [36mEAX[39;49;00m
   137
   138	    [37m//Check if we are working on NT-Platform[39;49;00m
   139	    [34mCALL[39;49;00m    IsWindowsNTSystem
   140	    [34mTEST[39;49;00m    [36mEAX[39;49;00m, [36mEAX[39;49;00m
   141	    [34mJZ[39;49;00m      @@NoNTSystem
   142
   143	    [34mPUSH[39;49;00m    DWORD PTR [[36mESP[39;49;00m]
   144	    [34mLEA[39;49;00m     [36mEAX[39;49;00m, DWORD PTR [[36mESP[39;49;00m+[34m$04[39;49;00m]
   145	    [34mPUSH[39;49;00m    [36mEAX[39;49;00m
   146	    [34mCALL[39;49;00m    GetHandleInformation
   147	    [34mTEST[39;49;00m    [36mEAX[39;49;00m, [36mEAX[39;49;00m
   148	    [34mJNZ[39;49;00m     @@Finish2
   149
   150	@@NoNTSystem:
   151	    [37m//Result := DuplicateHandle(GetCurrentProcess, Handle, GetCurrentProcess,[39;49;00m
   152	    [37m//  @Duplicate, 0, False, DUPLICATE_SAME_ACCESS);[39;49;00m
   153	    [34mPUSH[39;49;00m    DUPLICATE_SAME_ACCESS
   154	    [34mPUSH[39;49;00m    [34m$00000000[39;49;00m
   155	    [34mPUSH[39;49;00m    [34m$00000000[39;49;00m
   156	    [34mLEA[39;49;00m     [36mEAX[39;49;00m, DWORD PTR [[36mESP[39;49;00m+[34m$0C[39;49;00m]
   157	    [34mPUSH[39;49;00m    [36mEAX[39;49;00m
   158	    [34mCALL[39;49;00m    GetCurrentProcess
   159	    [34mPUSH[39;49;00m    [36mEAX[39;49;00m
   160	    [34mPUSH[39;49;00m    DWORD PTR [[36mESP[39;49;00m+[34m$18[39;49;00m]
   161	    [34mPUSH[39;49;00m    [36mEAX[39;49;00m
   162	    [34mCALL[39;49;00m    DuplicateHandle
   163
   164	    [34mTEST[39;49;00m    [36mEAX[39;49;00m, [36mEAX[39;49;00m
   165	    [34mJZ[39;49;00m      @@Finish2
   166
   167	    [37m//  Result := CloseHandle(Duplicate);[39;49;00m
   168	    [34mPUSH[39;49;00m    DWORD PTR [[36mESP[39;49;00m]
   169	    [34mCALL[39;49;00m    CloseHandle
   170
   171	@@Finish2:
   172	    [34mPOP[39;49;00m     [36mEDX[39;49;00m
   173	    [34mPOP[39;49;00m     [36mEDX[39;49;00m
   174
   175	    [34mPUSH[39;49;00m    [36mEAX[39;49;00m
   176	    [34mPUSH[39;49;00m    [34m$00000000[39;49;00m
   177	    [34mCALL[39;49;00m    SetLastError
   178	    [34mPOP[39;49;00m     [36mEAX[39;49;00m
   179	    [37m{$ENDIF}[39;49;00m
   180
   181	@@Finish:
   182	[34mEnd[39;49;00m;
   183	[37m{$ELSE}[39;49;00m
   184	[34mVar[39;49;00m
   185	    Duplicate: [36mTHandle[39;49;00m;
   186	    Flags: [36mDWORD[39;49;00m;
   187	[34mBegin[39;49;00m
   188	    [34mIf[39;49;00m IsWinNT [34mThen[39;49;00m
   189	        [36mResult[39;49;00m := GetHandleInformation(Handle, Flags)
   190	    [34mElse[39;49;00m
   191	        [36mResult[39;49;00m := [34mFalse[39;49;00m;
   192	    [34mIf[39;49;00m [34mNot[39;49;00m [36mResult[39;49;00m [34mThen[39;49;00m
   193	    [34mBegin[39;49;00m
   194	        [37m// DuplicateHandle is used as an additional check for those object types not[39;49;00m
   195	        [37m// supported by GetHandleInformation (e.g. according to the documentation,[39;49;00m
   196	        [37m// GetHandleInformation doesn't support window stations and desktop although[39;49;00m
   197	        [37m// tests show that it does). GetHandleInformation is tried first because its[39;49;00m
   198	        [37m// much faster. Additionally GetHandleInformation is only supported on NT...[39;49;00m
   199	        [36mResult[39;49;00m := DuplicateHandle(GetCurrentProcess, Handle, GetCurrentProcess,
   200	            @Duplicate, [34m0[39;49;00m, [34mFalse[39;49;00m, DUPLICATE_SAME_ACCESS);
   201	        [34mIf[39;49;00m [36mResult[39;49;00m [34mThen[39;49;00m
   202	            [36mResult[39;49;00m := CloseHandle(Duplicate);
   203	    [34mEnd[39;49;00m;
   204	[34mEnd[39;49;00m;
   205	[37m{$ENDIF}[39;49;00m
   206
   207
   208
   209
   210	[37m{*******************************************************}[39;49;00m
   211	[37m{                                                       }[39;49;00m
   212	[37m{       Delphi Supplemental Components                  }[39;49;00m
   213	[37m{       ZLIB Data Compression Interface Unit            }[39;49;00m
   214	[37m{                                                       }[39;49;00m
   215	[37m{       Copyright (c) 1997 Borland International        }[39;49;00m
   216	[37m{                                                       }[39;49;00m
   217	[37m{*******************************************************}[39;49;00m
   218
   219	[37m{ Modified for zlib 1.1.3 by Davide Moretti <dave@rimini.com }[39;49;00m
   220
   221	[34munit[39;49;00m zlib;
   222
   223	[34minterface[39;49;00m
   224
   225	[34muses[39;49;00m Sysutils, Classes;
   226
   227	[34mtype[39;49;00m
   228	  TAlloc = [34mfunction[39;49;00m (AppData: [36mPointer[39;49;00m; Items, Size: [36mInteger[39;49;00m): [36mPointer[39;49;00m;
   229	  TFree = [34mprocedure[39;49;00m (AppData, Block: [36mPointer[39;49;00m);
   230
   231	  [37m// Internal structure.  Ignore.[39;49;00m
   232	  TZStreamRec = [34mpacked[39;49;00m [34mrecord[39;49;00m
   233	    next_in: [36mPChar[39;49;00m;       [37m// next input byte[39;49;00m
   234	    avail_in: [36mInteger[39;49;00m;    [37m// number of bytes available at next_in[39;49;00m
   235	    total_in: [36mInteger[39;49;00m;    [37m// total nb of input bytes read so far[39;49;00m
   236
   237	    next_out: [36mPChar[39;49;00m;      [37m// next output byte should be put here[39;49;00m
   238	    avail_out: [36mInteger[39;49;00m;   [37m// remaining free space at next_out[39;49;00m
   239	    total_out: [36mInteger[39;49;00m;   [37m// total nb of bytes output so far[39;49;00m
   240
   241	    msg: [36mPChar[39;49;00m;           [37m// last error message, NULL if no error[39;49;00m
   242	    internal: [36mPointer[39;49;00m;    [37m// not visible by applications[39;49;00m
   243
   244	    zalloc: TAlloc;       [37m// used to allocate the internal state[39;49;00m
   245	    zfree: TFree;         [37m// used to free the internal state[39;49;00m
   246	    AppData: [36mPointer[39;49;00m;     [37m// private data object passed to zalloc and zfree[39;49;00m
   247
   248	    data_type: [36mInteger[39;49;00m;   [37m//  best guess about the data type: ascii or binary[39;49;00m
   249	    adler: [36mInteger[39;49;00m;       [37m// adler32 value of the uncompressed data[39;49;00m
   250	    reserved: [36mInteger[39;49;00m;    [37m// reserved for future use[39;49;00m
   251	  [34mend[39;49;00m;
   252
   253	  [37m// Abstract ancestor class[39;49;00m
   254	  TCustomZlibStream = [34mclass[39;49;00m(TStream)
   255	  [34mprivate[39;49;00m
   256	    FStrm: TStream;
   257	    FStrmPos: [36mInteger[39;49;00m;
   258	    FOnProgress: TNotifyEvent;
   259	    FZRec: TZStreamRec;
   260	    FBuffer: [34marray[39;49;00m [[36mWord[39;49;00m] [34mof[39;49;00m [36mChar[39;49;00m;
   261	  [34mprotected[39;49;00m
   262	    [34mprocedure[39;49;00m [32mProgress[39;49;00m(Sender: [36mTObject[39;49;00m); [34mdynamic[39;49;00m;
   263	    [34mproperty[39;49;00m OnProgress: TNotifyEvent [34mread[39;49;00m [32mFOnProgress[39;49;00m [34mwrite[39;49;00m [32mFOnProgress[39;49;00m;
   264	    [34mconstructor[39;49;00m [32mCreate[39;49;00m(Strm: TStream);
   265	  [34mend[39;49;00m;
   266
   267	[37m{ TCompressionStream compresses data on the fly as data is written to it, and[39;49;00m
   268	[37m  stores the compressed data to another stream.[39;49;00m
   269	[37m[39;49;00m
   270	[37m  TCompressionStream is write-only and strictly sequential. Reading from the[39;49;00m
   271	[37m  stream will raise an exception. Using Seek to move the stream pointer[39;49;00m
   272	[37m  will raise an exception.[39;49;00m
   273	[37m[39;49;00m
   274	[37m  Output data is cached internally, written to the output stream only when[39;49;00m
   275	[37m  the internal output buffer is full.  All pending output data is flushed[39;49;00m
   276	[37m  when the stream is destroyed.[39;49;00m
   277	[37m[39;49;00m
   278	[37m  The Position property returns the number of uncompressed bytes of[39;49;00m
   279	[37m  data that have been written to the stream so far.[39;49;00m
   280	[37m[39;49;00m
   281	[37m  CompressionRate returns the on-the-fly percentage by which the original[39;49;00m
   282	[37m  data has been compressed:  (1 - (CompressedBytes / UncompressedBytes)) * 100[39;49;00m
   283	[37m  If raw data size = 100 and compressed data size = 25, the CompressionRate[39;49;00m
   284	[37m  is 75%[39;49;00m
   285	[37m[39;49;00m
   286	[37m  The OnProgress event is called each time the output buffer is filled and[39;49;00m
   287	[37m  written to the output stream.  This is useful for updating a progress[39;49;00m
   288	[37m  indicator when you are writing a large chunk of data to the compression[39;49;00m
   289	[37m  stream in a single call.}[39;49;00m
   290
   291
   292	  TCompressionLevel = (clNone, clFastest, clDefault, clMax);
   293
   294	  TCompressionStream = [34mclass[39;49;00m(TCustomZlibStream)
   295	  [34mprivate[39;49;00m
   296	    [34mfunction[39;49;00m [32mGetCompressionRate[39;49;00m: [36mSingle[39;49;00m;
   297	  [34mpublic[39;49;00m
   298	    [34mconstructor[39;49;00m [32mCreate[39;49;00m(CompressionLevel: TCompressionLevel; Dest: TStream);
   299	    [34mdestructor[39;49;00m [32mDestroy[39;49;00m; [34moverride[39;49;00m;
   300	    [34mfunction[39;49;00m [32mRead[39;49;00m([34mvar[39;49;00m Buffer; Count: [36mLongint[39;49;00m): [36mLongint[39;49;00m; [34moverride[39;49;00m;
   301	    [34mfunction[39;49;00m [32mWrite[39;49;00m([34mconst[39;49;00m Buffer; Count: [36mLongint[39;49;00m): [36mLongint[39;49;00m; [34moverride[39;49;00m;
   302	    [34mfunction[39;49;00m [32mSeek[39;49;00m(Offset: [36mLongint[39;49;00m; Origin: [36mWord[39;49;00m): [36mLongint[39;49;00m; [34moverride[39;49;00m;
   303	    [34mproperty[39;49;00m CompressionRate: [36mSingle[39;49;00m [34mread[39;49;00m [32mGetCompressionRate[39;49;00m;
   304	    [34mproperty[39;49;00m OnProgress;
   305	  [34mend[39;49;00m;
   306
   307	[37m{ TDecompressionStream decompresses data on the fly as data is read from it.[39;49;00m
   308	[37m[39;49;00m
   309	[37m  Compressed data comes from a separate source stream.  TDecompressionStream[39;49;00m
   310	[37m  is read-only and unidirectional; you can seek forward in the stream, but not[39;49;00m
   311	[37m  backwards.  The special case of setting the stream position to zero is[39;49;00m
   312	[37m  allowed.  Seeking forward decompresses data until the requested position in[39;49;00m
   313	[37m  the uncompressed data has been reached.  Seeking backwards, seeking relative[39;49;00m
   314	[37m  to the end of the stream, requesting the size of the stream, and writing to[39;49;00m
   315	[37m  the stream will raise an exception.[39;49;00m
   316	[37m[39;49;00m
   317	[37m  The Position property returns the number of bytes of uncompressed data that[39;49;00m
   318	[37m  have been read from the stream so far.[39;49;00m
   319	[37m[39;49;00m
   320	[37m  The OnProgress event is called each time the internal input buffer of[39;49;00m
   321	[37m  compressed data is exhausted and the next block is read from the input stream.[39;49;00m
   322	[37m  This is useful for updating a progress indicator when you are reading a[39;49;00m
   323	[37m  large chunk of data from the decompression stream in a single call.}[39;49;00m
   324
   325	  TDecompressionStream = [34mclass[39;49;00m(TCustomZlibStream)
   326	  [34mpublic[39;49;00m
   327	    [34mconstructor[39;49;00m [32mCreate[39;49;00m(Source: TStream);
   328	    [34mdestructor[39;49;00m [32mDestroy[39;49;00m; [34moverride[39;49;00m;
   329	    [34mfunction[39;49;00m [32mRead[39;49;00m([34mvar[39;49;00m Buffer; Count: [36mLongint[39;49;00m): [36mLongint[39;49;00m; [34moverride[39;49;00m;
   330	    [34mfunction[39;49;00m [32mWrite[39;49;00m([34mconst[39;49;00m Buffer; Count: [36mLongint[39;49;00m): [36mLongint[39;49;00m; [34moverride[39;49;00m;
   331	    [34mfunction[39;49;00m [32mSeek[39;49;00m(Offset: [36mLongint[39;49;00m; Origin: [36mWord[39;49;00m): [36mLongint[39;49;00m; [34moverride[39;49;00m;
   332	    [34mproperty[39;49;00m OnProgress;
   333	  [34mend[39;49;00m;
   334
   335
   336
   337	[37m{ CompressBuf compresses data, buffer to buffer, in one call.[39;49;00m
   338	[37m   In: InBuf = ptr to compressed data[39;49;00m
   339	[37m       InBytes = number of bytes in InBuf[39;49;00m
   340	[37m  Out: OutBuf = ptr to newly allocated buffer containing decompressed data[39;49;00m
   341	[37m       OutBytes = number of bytes in OutBuf   }[39;49;00m
   342	[34mprocedure[39;49;00m [32mCompressBuf[39;49;00m([34mconst[39;49;00m InBuf: [36mPointer[39;49;00m; InBytes: [36mInteger[39;49;00m;
   343	                      out OutBuf: [36mPointer[39;49;00m; out OutBytes: [36mInteger[39;49;00m);
   344
   345
   346	[37m{ DecompressBuf decompresses data, buffer to buffer, in one call.[39;49;00m
   347	[37m   In: InBuf = ptr to compressed data[39;49;00m
   348	[37m       InBytes = number of bytes in InBuf[39;49;00m
   349	[37m       OutEstimate = zero, or est. size of the decompressed data[39;49;00m
   350	[37m  Out: OutBuf = ptr to newly allocated buffer containing decompressed data[39;49;00m
   351	[37m       OutBytes = number of bytes in OutBuf   }[39;49;00m
   352	[34mprocedure[39;49;00m [32mDecompressBuf[39;49;00m([34mconst[39;49;00m InBuf: [36mPointer[39;49;00m; InBytes: [36mInteger[39;49;00m;
   353	 OutEstimate: [36mInteger[39;49;00m; out OutBuf: [36mPointer[39;49;00m; out OutBytes: [36mInteger[39;49;00m);
   354
   355	[34mconst[39;49;00m
   356	  zlib_version = [33m'[39;49;00m[33m1.1.3[39;49;00m[33m'[39;49;00m;
   357
   358	[34mtype[39;49;00m
   359	  EZlibError = [34mclass[39;49;00m(Exception);
   360	  ECompressionError = [34mclass[39;49;00m(EZlibError);
   361	  EDecompressionError = [34mclass[39;49;00m(EZlibError);
   362
   363	[34mfunction[39;49;00m [32madler32[39;49;00m(adler: [36mInteger[39;49;00m; buf: [36mPChar[39;49;00m; len: [36mInteger[39;49;00m): [36mInteger[39;49;00m;
   364
   365	[34mimplementation[39;49;00m
   366
   367	[34mconst[39;49;00m
   368	  Z_NO_FLUSH      = [34m0[39;49;00m;
   369	  Z_PARTIAL_FLUSH = [34m1[39;49;00m;
   370	  Z_SYNC_FLUSH    = [34m2[39;49;00m;
   371	  Z_FULL_FLUSH    = [34m3[39;49;00m;
   372	  Z_FINISH        = [34m4[39;49;00m;
   373
   374	  Z_OK            = [34m0[39;49;00m;
   375	  Z_STREAM_END    = [34m1[39;49;00m;
   376	  Z_NEED_DICT     = [34m2[39;49;00m;
   377	  Z_ERRNO         = (-[34m1[39;49;00m);
   378	  Z_STREAM_ERROR  = (-[34m2[39;49;00m);
   379	  Z_DATA_ERROR    = (-[34m3[39;49;00m);
   380	  Z_MEM_ERROR     = (-[34m4[39;49;00m);
   381	  Z_BUF_ERROR     = (-[34m5[39;49;00m);
   382	  Z_VERSION_ERROR = (-[34m6[39;49;00m);
   383
   384	  Z_NO_COMPRESSION       =   [34m0[39;49;00m;
   385	  Z_BEST_SPEED           =   [34m1[39;49;00m;
   386	  Z_BEST_COMPRESSION     =   [34m9[39;49;00m;
   387	  Z_DEFAULT_COMPRESSION  = (-[34m1[39;49;00m);
   388
   389	  Z_FILTERED            = [34m1[39;49;00m;
   390	  Z_HUFFMAN_ONLY        = [34m2[39;49;00m;
   391	  Z_DEFAULT_STRATEGY    = [34m0[39;49;00m;
   392
   393	  Z_BINARY   = [34m0[39;49;00m;
   394	  Z_ASCII    = [34m1[39;49;00m;
   395	  Z_UNKNOWN  = [34m2[39;49;00m;
   396
   397	  Z_DEFLATED = [34m8[39;49;00m;
   398
   399	  _z_errmsg: [34marray[39;49;00m[[34m0[39;49;00m..[34m9[39;49;00m] [34mof[39;49;00m [36mPChar[39;49;00m = (
   400	    [33m'[39;49;00m[33mneed dictionary[39;49;00m[33m'[39;49;00m,      [37m// Z_NEED_DICT      (2)[39;49;00m
   401	    [33m'[39;49;00m[33mstream end[39;49;00m[33m'[39;49;00m,           [37m// Z_STREAM_END     (1)[39;49;00m
   402	    [33m'[39;49;00m[33m'[39;49;00m,                     [37m// Z_OK             (0)[39;49;00m
   403	    [33m'[39;49;00m[33mfile error[39;49;00m[33m'[39;49;00m,           [37m// Z_ERRNO          (-1)[39;49;00m
   404	    [33m'[39;49;00m[33mstream error[39;49;00m[33m'[39;49;00m,         [37m// Z_STREAM_ERROR   (-2)[39;49;00m
   405	    [33m'[39;49;00m[33mdata error[39;49;00m[33m'[39;49;00m,           [37m// Z_DATA_ERROR     (-3)[39;49;00m
   406	    [33m'[39;49;00m[33minsufficient memory[39;49;00m[33m'[39;49;00m,  [37m// Z_MEM_ERROR      (-4)[39;49;00m
   407	    [33m'[39;49;00m[33mbuffer error[39;49;00m[33m'[39;49;00m,         [37m// Z_BUF_ERROR      (-5)[39;49;00m
   408	    [33m'[39;49;00m[33mincompatible version[39;49;00m[33m'[39;49;00m, [37m// Z_VERSION_ERROR  (-6)[39;49;00m
   409	    [33m'[39;49;00m[33m'[39;49;00m
   410	  );
   411
   412	[37m{$L deflate.obj}[39;49;00m
   413	[37m{$L inflate.obj}[39;49;00m
   414	[37m{$L inftrees.obj}[39;49;00m
   415	[37m{$L trees.obj}[39;49;00m
   416	[37m{$L adler32.obj}[39;49;00m
   417	[37m{$L infblock.obj}[39;49;00m
   418	[37m{$L infcodes.obj}[39;49;00m
   419	[37m{$L infutil.obj}[39;49;00m
   420	[37m{$L inffast.obj}[39;49;00m
   421
   422	[34mprocedure[39;49;00m [32m_tr_init[39;49;00m; [34mexternal[39;49;00m;
   423	[34mprocedure[39;49;00m [32m_tr_tally[39;49;00m; [34mexternal[39;49;00m;
   424	[34mprocedure[39;49;00m [32m_tr_flush_block[39;49;00m; [34mexternal[39;49;00m;
   425	[34mprocedure[39;49;00m [32m_tr_align[39;49;00m; [34mexternal[39;49;00m;
   426	[34mprocedure[39;49;00m [32m_tr_stored_block[39;49;00m; [34mexternal[39;49;00m;
   427	[34mfunction[39;49;00m [32madler32[39;49;00m; [34mexternal[39;49;00m;
   428	[34mprocedure[39;49;00m [32minflate_blocks_new[39;49;00m; [34mexternal[39;49;00m;
   429	[34mprocedure[39;49;00m [32minflate_blocks[39;49;00m; [34mexternal[39;49;00m;
   430	[34mprocedure[39;49;00m [32minflate_blocks_reset[39;49;00m; [34mexternal[39;49;00m;
   431	[34mprocedure[39;49;00m [32minflate_blocks_free[39;49;00m; [34mexternal[39;49;00m;
   432	[34mprocedure[39;49;00m [32minflate_set_dictionary[39;49;00m; [34mexternal[39;49;00m;
   433	[34mprocedure[39;49;00m [32minflate_trees_bits[39;49;00m; [34mexternal[39;49;00m;
   434	[34mprocedure[39;49;00m [32minflate_trees_dynamic[39;49;00m; [34mexternal[39;49;00m;
   435	[34mprocedure[39;49;00m [32minflate_trees_fixed[39;49;00m; [34mexternal[39;49;00m;
   436	[34mprocedure[39;49;00m [32minflate_codes_new[39;49;00m; [34mexternal[39;49;00m;
   437	[34mprocedure[39;49;00m [32minflate_codes[39;49;00m; [34mexternal[39;49;00m;
   438	[34mprocedure[39;49;00m [32minflate_codes_free[39;49;00m; [34mexternal[39;49;00m;
   439	[34mprocedure[39;49;00m [32m_inflate_mask[39;49;00m; [34mexternal[39;49;00m;
   440	[34mprocedure[39;49;00m [32minflate_flush[39;49;00m; [34mexternal[39;49;00m;
   441	[34mprocedure[39;49;00m [32minflate_fast[39;49;00m; [34mexternal[39;49;00m;
   442
   443	[34mprocedure[39;49;00m [32m_memset[39;49;00m(P: [36mPointer[39;49;00m; B: [36mByte[39;49;00m; count: [36mInteger[39;49;00m);[34mcdecl[39;49;00m;
   444	[34mbegin[39;49;00m
   445	  [36mFillChar[39;49;00m(P^, count, B);
   446	[34mend[39;49;00m;
   447
   448	[34mprocedure[39;49;00m [32m_memcpy[39;49;00m(dest, source: [36mPointer[39;49;00m; count: [36mInteger[39;49;00m);[34mcdecl[39;49;00m;
   449	[34mbegin[39;49;00m
   450	  [36mMove[39;49;00m(source^, dest^, count);
   451	[34mend[39;49;00m;
   452
   453
   454
   455	[37m// deflate compresses data[39;49;00m
   456	[34mfunction[39;49;00m [32mdeflateInit_[39;49;00m([34mvar[39;49;00m strm: TZStreamRec; level: [36mInteger[39;49;00m; version: [36mPChar[39;49;00m;
   457	  recsize: [36mInteger[39;49;00m): [36mInteger[39;49;00m; [34mexternal[39;49;00m;
   458	[34mfunction[39;49;00m [32mdeflate[39;49;00m([34mvar[39;49;00m strm: TZStreamRec; [36mflush[39;49;00m: [36mInteger[39;49;00m): [36mInteger[39;49;00m; [34mexternal[39;49;00m;
   459	[34mfunction[39;49;00m [32mdeflateEnd[39;49;00m([34mvar[39;49;00m strm: TZStreamRec): [36mInteger[39;49;00m; [34mexternal[39;49;00m;
   460
   461	[37m// inflate decompresses data[39;49;00m
   462	[34mfunction[39;49;00m [32minflateInit_[39;49;00m([34mvar[39;49;00m strm: TZStreamRec; version: [36mPChar[39;49;00m;
   463	  recsize: [36mInteger[39;49;00m): [36mInteger[39;49;00m; [34mexternal[39;49;00m;
   464	[34mfunction[39;49;00m [32minflate[39;49;00m([34mvar[39;49;00m strm: TZStreamRec; [36mflush[39;49;00m: [36mInteger[39;49;00m): [36mInteger[39;49;00m; [34mexternal[39;49;00m;
   465	[34mfunction[39;49;00m [32minflateEnd[39;49;00m([34mvar[39;49;00m strm: TZStreamRec): [36mInteger[39;49;00m; [34mexternal[39;49;00m;
   466	[34mfunction[39;49;00m [32minflateReset[39;49;00m([34mvar[39;49;00m strm: TZStreamRec): [36mInteger[39;49;00m; [34mexternal[39;49;00m;
   467
   468
   469	[34mfunction[39;49;00m [32mzcalloc[39;49;00m(AppData: [36mPointer[39;49;00m; Items, Size: [36mInteger[39;49;00m): [36mPointer[39;49;00m;
   470	[34mbegin[39;49;00m
   471	  [36mGetMem[39;49;00m([36mResult[39;49;00m, Items*Size);
   472	[34mend[39;49;00m;
   473
   474	[34mprocedure[39;49;00m [32mzcfree[39;49;00m(AppData, Block: [36mPointer[39;49;00m);
   475	[34mbegin[39;49;00m
   476	  [36mFreeMem[39;49;00m(Block);
   477	[34mend[39;49;00m;
   478
   479	[34mfunction[39;49;00m [32mzlibCheck[39;49;00m(code: [36mInteger[39;49;00m): [36mInteger[39;49;00m;
   480	[34mbegin[39;49;00m
   481	  [36mResult[39;49;00m := code;
   482	  [34mif[39;49;00m code < [34m0[39;49;00m [34mthen[39;49;00m
   483	    [34mraise[39;49;00m EZlibError.Create([33m'[39;49;00m[33merror[39;49;00m[33m'[39;49;00m);    [37m//!![39;49;00m
   484	[34mend[39;49;00m;
   485
   486	[34mfunction[39;49;00m [32mCCheck[39;49;00m(code: [36mInteger[39;49;00m): [36mInteger[39;49;00m;
   487	[34mbegin[39;49;00m
   488	  [36mResult[39;49;00m := code;
   489	  [34mif[39;49;00m code < [34m0[39;49;00m [34mthen[39;49;00m
   490	    [34mraise[39;49;00m ECompressionError.Create([33m'[39;49;00m[33merror[39;49;00m[33m'[39;49;00m); [37m//!![39;49;00m
   491	[34mend[39;49;00m;
   492
   493	[34mfunction[39;49;00m [32mDCheck[39;49;00m(code: [36mInteger[39;49;00m): [36mInteger[39;49;00m;
   494	[34mbegin[39;49;00m
   495	  [36mResult[39;49;00m := code;
   496	  [34mif[39;49;00m code < [34m0[39;49;00m [34mthen[39;49;00m
   497	    [34mraise[39;49;00m EDecompressionError.Create([33m'[39;49;00m[33merror[39;49;00m[33m'[39;49;00m);  [37m//!![39;49;00m
   498	[34mend[39;49;00m;
   499
   500	[34mprocedure[39;49;00m [32mCompressBuf[39;49;00m([34mconst[39;49;00m InBuf: [36mPointer[39;49;00m; InBytes: [36mInteger[39;49;00m;
   501	                      out OutBuf: [36mPointer[39;49;00m; out OutBytes: [36mInteger[39;49;00m);
   502	[34mvar[39;49;00m
   503	  strm: TZStreamRec;
   504	  P: [36mPointer[39;49;00m;
   505	[34mbegin[39;49;00m
   506	  [36mFillChar[39;49;00m(strm, [36msizeof[39;49;00m(strm), [34m0[39;49;00m);
   507	  OutBytes := ((InBytes + (InBytes [34mdiv[39;49;00m [34m10[39;49;00m) + [34m12[39;49;00m) + [34m255[39;49;00m) [34mand[39;49;00m [34mnot[39;49;00m [34m255[39;49;00m;
   508	  [36mGetMem[39;49;00m(OutBuf, OutBytes);
   509	  [34mtry[39;49;00m
   510	    strm.next_in := InBuf;
   511	    strm.avail_in := InBytes;
   512	    strm.next_out := OutBuf;
   513	    strm.avail_out := OutBytes;
   514	    CCheck(deflateInit_(strm, Z_BEST_COMPRESSION, zlib_version, [36msizeof[39;49;00m(strm)));
   515	    [34mtry[39;49;00m
   516	      [34mwhile[39;49;00m CCheck(deflate(strm, Z_FINISH)) <> Z_STREAM_END [34mdo[39;49;00m
   517	      [34mbegin[39;49;00m
   518	        P := OutBuf;
   519	        [36mInc[39;49;00m(OutBytes, [34m256[39;49;00m);
   520	        [36mReallocMem[39;49;00m(OutBuf, OutBytes);
   521	        strm.next_out := [36mPChar[39;49;00m([36mInteger[39;49;00m(OutBuf) + ([36mInteger[39;49;00m(strm.next_out) - [36mInteger[39;49;00m(P)));
   522	        strm.avail_out := [34m256[39;49;00m;
   523	      [34mend[39;49;00m;
   524	    [34mfinally[39;49;00m
   525	      CCheck(deflateEnd(strm));
   526	    [34mend[39;49;00m;
   527	    [36mReallocMem[39;49;00m(OutBuf, strm.total_out);
   528	    OutBytes := strm.total_out;
   529	  [34mexcept[39;49;00m
   530	    [36mFreeMem[39;49;00m(OutBuf);
   531	    [34mraise[39;49;00m
   532	  [34mend[39;49;00m;
   533	[34mend[39;49;00m;
   534
   535
   536	[34mprocedure[39;49;00m [32mDecompressBuf[39;49;00m([34mconst[39;49;00m InBuf: [36mPointer[39;49;00m; InBytes: [36mInteger[39;49;00m;
   537	  OutEstimate: [36mInteger[39;49;00m; out OutBuf: [36mPointer[39;49;00m; out OutBytes: [36mInteger[39;49;00m);
   538	[34mvar[39;49;00m
   539	  strm: TZStreamRec;
   540	  P: [36mPointer[39;49;00m;
   541	  BufInc: [36mInteger[39;49;00m;
   542	[34mbegin[39;49;00m
   543	  [36mFillChar[39;49;00m(strm, [36msizeof[39;49;00m(strm), [34m0[39;49;00m);
   544	  BufInc := (InBytes + [34m255[39;49;00m) [34mand[39;49;00m [34mnot[39;49;00m [34m255[39;49;00m;
   545	  [34mif[39;49;00m OutEstimate = [34m0[39;49;00m [34mthen[39;49;00m
   546	    OutBytes := BufInc
   547	  [34melse[39;49;00m
   548	    OutBytes := OutEstimate;
   549	  [36mGetMem[39;49;00m(OutBuf, OutBytes);
   550	  [34mtry[39;49;00m
   551	    strm.next_in := InBuf;
   552	    strm.avail_in := InBytes;
   553	    strm.next_out := OutBuf;
   554	    strm.avail_out := OutBytes;
   555	    DCheck(inflateInit_(strm, zlib_version, [36msizeof[39;49;00m(strm)));
   556	    [34mtry[39;49;00m
   557	      [34mwhile[39;49;00m DCheck(inflate(strm, Z_FINISH)) <> Z_STREAM_END [34mdo[39;49;00m
   558	      [34mbegin[39;49;00m
   559	        P := OutBuf;
   560	        [36mInc[39;49;00m(OutBytes, BufInc);
   561	        [36mReallocMem[39;49;00m(OutBuf, OutBytes);
   562	        strm.next_out := [36mPChar[39;49;00m([36mInteger[39;49;00m(OutBuf) + ([36mInteger[39;49;00m(strm.next_out) - [36mInteger[39;49;00m(P)));
   563	        strm.avail_out := BufInc;
   564	      [34mend[39;49;00m;
   565	    [34mfinally[39;49;00m
   566	      DCheck(inflateEnd(strm));
   567	    [34mend[39;49;00m;
   568	    [36mReallocMem[39;49;00m(OutBuf, strm.total_out);
   569	    OutBytes := strm.total_out;
   570	  [34mexcept[39;49;00m
   571	    [36mFreeMem[39;49;00m(OutBuf);
   572	    [34mraise[39;49;00m
   573	  [34mend[39;49;00m;
   574	[34mend[39;49;00m;
   575
   576
   577	[37m// TCustomZlibStream[39;49;00m
   578
   579	[34mconstructor[39;49;00m [04m[32mTCustomZLibStream[39;49;00m.[32mCreate[39;49;00m(Strm: TStream);
   580	[34mbegin[39;49;00m
   581	  [34minherited[39;49;00m Create;
   582	  FStrm := Strm;
   583	  FStrmPos := Strm.Position;
   584	[34mend[39;49;00m;
   585
   586	[34mprocedure[39;49;00m [04m[32mTCustomZLibStream[39;49;00m.[32mProgress[39;49;00m(Sender: [36mTObject[39;49;00m);
   587	[34mbegin[39;49;00m
   588	  [34mif[39;49;00m [36mAssigned[39;49;00m(FOnProgress) [34mthen[39;49;00m FOnProgress(Sender);
   589	[34mend[39;49;00m;
   590
   591
   592	[37m// TCompressionStream[39;49;00m
   593
   594	[34mconstructor[39;49;00m [04m[32mTCompressionStream[39;49;00m.[32mCreate[39;49;00m(CompressionLevel: TCompressionLevel;
   595	  Dest: TStream);
   596	[34mconst[39;49;00m
   597	  Levels: [34marray[39;49;00m [TCompressionLevel] [34mof[39;49;00m [36mShortInt[39;49;00m =
   598	    (Z_NO_COMPRESSION, Z_BEST_SPEED, Z_DEFAULT_COMPRESSION, Z_BEST_COMPRESSION);
   599	[34mbegin[39;49;00m
   600	  [34minherited[39;49;00m Create(Dest);
   601	  FZRec.next_out := FBuffer;
   602	  FZRec.avail_out := [36msizeof[39;49;00m(FBuffer);
   603	  CCheck(deflateInit_(FZRec, Levels[CompressionLevel], zlib_version, [36msizeof[39;49;00m(FZRec)));
   604	[34mend[39;49;00m;
   605
   606	[34mdestructor[39;49;00m [04m[32mTCompressionStream[39;49;00m.[32mDestroy[39;49;00m;
   607	[34mbegin[39;49;00m
   608	  FZRec.next_in := [34mnil[39;49;00m;
   609	  FZRec.avail_in := [34m0[39;49;00m;
   610	  [34mtry[39;49;00m
   611	    [34mif[39;49;00m FStrm.Position <> FStrmPos [34mthen[39;49;00m FStrm.Position := FStrmPos;
   612	    [34mwhile[39;49;00m (CCheck(deflate(FZRec, Z_FINISH)) <> Z_STREAM_END)
   613	      [34mand[39;49;00m (FZRec.avail_out = [34m0[39;49;00m) [34mdo[39;49;00m
   614	    [34mbegin[39;49;00m
   615	      FStrm.WriteBuffer(FBuffer, [36msizeof[39;49;00m(FBuffer));
   616	      FZRec.next_out := FBuffer;
   617	      FZRec.avail_out := [36msizeof[39;49;00m(FBuffer);
   618	    [34mend[39;49;00m;
   619	    [34mif[39;49;00m FZRec.avail_out < [36msizeof[39;49;00m(FBuffer) [34mthen[39;49;00m
   620	      FStrm.WriteBuffer(FBuffer, [36msizeof[39;49;00m(FBuffer) - FZRec.avail_out);
   621	  [34mfinally[39;49;00m
   622	    deflateEnd(FZRec);
   623	  [34mend[39;49;00m;
   624	  [34minherited[39;49;00m Destroy;
   625	[34mend[39;49;00m;
   626
   627	[34mfunction[39;49;00m [04m[32mTCompressionStream[39;49;00m.[32mRead[39;49;00m([34mvar[39;49;00m Buffer; Count: [36mLongint[39;49;00m): [36mLongint[39;49;00m;
   628	[34mbegin[39;49;00m
   629	  [34mraise[39;49;00m ECompressionError.Create([33m'[39;49;00m[33mInvalid stream operation[39;49;00m[33m'[39;49;00m);
   630	[34mend[39;49;00m;
   631
   632	[34mfunction[39;49;00m [04m[32mTCompressionStream[39;49;00m.[32mWrite[39;49;00m([34mconst[39;49;00m Buffer; Count: [36mLongint[39;49;00m): [36mLongint[39;49;00m;
   633	[34mbegin[39;49;00m
   634	  FZRec.next_in := @Buffer;
   635	  FZRec.avail_in := Count;
   636	  [34mif[39;49;00m FStrm.Position <> FStrmPos [34mthen[39;49;00m FStrm.Position := FStrmPos;
   637	  [34mwhile[39;49;00m (FZRec.avail_in > [34m0[39;49;00m) [34mdo[39;49;00m
   638	  [34mbegin[39;49;00m
   639	    CCheck(deflate(FZRec, [34m0[39;49;00m));
   640	    [34mif[39;49;00m FZRec.avail_out = [34m0[39;49;00m [34mthen[39;49;00m
   641	    [34mbegin[39;49;00m
   642	      FStrm.WriteBuffer(FBuffer, [36msizeof[39;49;00m(FBuffer));
   643	      FZRec.next_out := FBuffer;
   644	      FZRec.avail_out := [36msizeof[39;49;00m(FBuffer);
   645	      FStrmPos := FStrm.Position;
   646	      Progress([34mSelf[39;49;00m);
   647	    [34mend[39;49;00m;
   648	  [34mend[39;49;00m;
   649	  [36mResult[39;49;00m := Count;
   650	[34mend[39;49;00m;
   651
   652	[34mfunction[39;49;00m [04m[32mTCompressionStream[39;49;00m.[32mSeek[39;49;00m(Offset: [36mLongint[39;49;00m; Origin: [36mWord[39;49;00m): [36mLongint[39;49;00m;
   653	[34mbegin[39;49;00m
   654	  [34mif[39;49;00m (Offset = [34m0[39;49;00m) [34mand[39;49;00m (Origin = soFromCurrent) [34mthen[39;49;00m
   655	    [36mResult[39;49;00m := FZRec.total_in
   656	  [34melse[39;49;00m
   657	    [34mraise[39;49;00m ECompressionError.Create([33m'[39;49;00m[33mInvalid stream operation[39;49;00m[33m'[39;49;00m);
   658	[34mend[39;49;00m;
   659
   660	[34mfunction[39;49;00m [04m[32mTCompressionStream[39;49;00m.[32mGetCompressionRate[39;49;00m: [36mSingle[39;49;00m;
   661	[34mbegin[39;49;00m
   662	  [34mif[39;49;00m FZRec.total_in = [34m0[39;49;00m [34mthen[39;49;00m
   663	    [36mResult[39;49;00m := [34m0[39;49;00m
   664	  [34melse[39;49;00m
   665	    [36mResult[39;49;00m := ([34m1.0[39;49;00m - (FZRec.total_out / FZRec.total_in)) * [34m10[39;49;00m[34m0.0[39;49;00m;
   666	[34mend[39;49;00m;
   667
   668
   669	[37m// TDecompressionStream[39;49;00m
   670
   671	[34mconstructor[39;49;00m [04m[32mTDecompressionStream[39;49;00m.[32mCreate[39;49;00m(Source: TStream);
   672	[34mbegin[39;49;00m
   673	  [34minherited[39;49;00m Create(Source);
   674	  FZRec.next_in := FBuffer;
   675	  FZRec.avail_in := [34m0[39;49;00m;
   676	  DCheck(inflateInit_(FZRec, zlib_version, [36msizeof[39;49;00m(FZRec)));
   677	[34mend[39;49;00m;
   678
   679	[34mdestructor[39;49;00m [04m[32mTDecompressionStream[39;49;00m.[32mDestroy[39;49;00m;
   680	[34mbegin[39;49;00m
   681	  inflateEnd(FZRec);
   682	  [34minherited[39;49;00m Destroy;
   683	[34mend[39;49;00m;
   684
   685	[34mfunction[39;49;00m [04m[32mTDecompressionStream[39;49;00m.[32mRead[39;49;00m([34mvar[39;49;00m Buffer; Count: [36mLongint[39;49;00m): [36mLongint[39;49;00m;
   686	[34mbegin[39;49;00m
   687	  FZRec.next_out := @Buffer;
   688	  FZRec.avail_out := Count;
   689	  [34mif[39;49;00m FStrm.Position <> FStrmPos [34mthen[39;49;00m FStrm.Position := FStrmPos;
   690	  [34mwhile[39;49;00m (FZRec.avail_out > [34m0[39;49;00m) [34mdo[39;49;00m
   691	  [34mbegin[39;49;00m
   692	    [34mif[39;49;00m FZRec.avail_in = [34m0[39;49;00m [34mthen[39;49;00m
   693	    [34mbegin[39;49;00m
   694	      FZRec.avail_in := FStrm.Read(FBuffer, [36msizeof[39;49;00m(FBuffer));
   695	      [34mif[39;49;00m FZRec.avail_in = [34m0[39;49;00m [34mthen[39;49;00m
   696	        [34mbegin[39;49;00m
   697	          [36mResult[39;49;00m := Count - FZRec.avail_out;
   698	          [34mExit[39;49;00m;
   699	        [34mend[39;49;00m;
   700	      FZRec.next_in := FBuffer;
   701	      FStrmPos := FStrm.Position;
   702	      Progress([34mSelf[39;49;00m);
   703	    [34mend[39;49;00m;
   704	    DCheck(inflate(FZRec, [34m0[39;49;00m));
   705	  [34mend[39;49;00m;
   706	  [36mResult[39;49;00m := Count;
   707	[34mend[39;49;00m;
   708
   709	[34mfunction[39;49;00m [04m[32mTDecompressionStream[39;49;00m.[32mWrite[39;49;00m([34mconst[39;49;00m Buffer; Count: [36mLongint[39;49;00m): [36mLongint[39;49;00m;
   710	[34mbegin[39;49;00m
   711	  [34mraise[39;49;00m EDecompressionError.Create([33m'[39;49;00m[33mInvalid stream operation[39;49;00m[33m'[39;49;00m);
   712	[34mend[39;49;00m;
   713
   714	[34mfunction[39;49;00m [04m[32mTDecompressionStream[39;49;00m.[32mSeek[39;49;00m(Offset: [36mLongint[39;49;00m; Origin: [36mWord[39;49;00m): [36mLongint[39;49;00m;
   715	[34mvar[39;49;00m
   716	  I: [36mInteger[39;49;00m;
   717	  Buf: [34marray[39;49;00m [[34m0[39;49;00m..[34m4095[39;49;00m] [34mof[39;49;00m [36mChar[39;49;00m;
   718	[34mbegin[39;49;00m
   719	  [34mif[39;49;00m (Offset = [34m0[39;49;00m) [34mand[39;49;00m (Origin = soFromBeginning) [34mthen[39;49;00m
   720	  [34mbegin[39;49;00m
   721	    DCheck(inflateReset(FZRec));
   722	    FZRec.next_in := FBuffer;
   723	    FZRec.avail_in := [34m0[39;49;00m;
   724	    FStrm.Position := [34m0[39;49;00m;
   725	    FStrmPos := [34m0[39;49;00m;
   726	  [34mend[39;49;00m
   727	  [34melse[39;49;00m [34mif[39;49;00m ( (Offset >= [34m0[39;49;00m) [34mand[39;49;00m (Origin = soFromCurrent)) [34mor[39;49;00m
   728	          ( ((Offset - FZRec.total_out) > [34m0[39;49;00m) [34mand[39;49;00m (Origin = soFromBeginning)) [34mthen[39;49;00m
   729	  [34mbegin[39;49;00m
   730	    [34mif[39;49;00m Origin = soFromBeginning [34mthen[39;49;00m [36mDec[39;49;00m(Offset, FZRec.total_out);
   731	    [34mif[39;49;00m Offset > [34m0[39;49;00m [34mthen[39;49;00m
   732	    [34mbegin[39;49;00m
   733	      [34mfor[39;49;00m I := [34m1[39;49;00m [34mto[39;49;00m Offset [34mdiv[39;49;00m [36msizeof[39;49;00m(Buf) [34mdo[39;49;00m
   734	        ReadBuffer(Buf, [36msizeof[39;49;00m(Buf));
   735	      ReadBuffer(Buf, Offset [34mmod[39;49;00m [36msizeof[39;49;00m(Buf));
   736	    [34mend[39;49;00m;
   737	  [34mend[39;49;00m
   738	  [34melse[39;49;00m
   739	    [34mraise[39;49;00m EDecompressionError.Create([33m'[39;49;00m[33mInvalid stream operation[39;49;00m[33m'[39;49;00m);
   740	  [36mResult[39;49;00m := FZRec.total_out;
   741	[34mend[39;49;00m;
   742
   743	[34mend[39;49;00m.

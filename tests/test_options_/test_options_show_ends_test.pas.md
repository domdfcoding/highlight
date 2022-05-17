[37m//[39;49;00m$
[37m// Sourcecode from http://www.delphi-library.de/topic_47880.html[39;49;00m$
[37m//[39;49;00m$
[34muses[39;49;00m Windows, Messages;$
$
[34mconst[39;49;00m$
  FFM_INIT               = WM_USER + [34m1976[39;49;00m;$
  FFM_ONFILEFOUND        = WM_USER + [34m1974[39;49;00m; [37m// wParam: not used, lParam: Filename[39;49;00m$
  FFM_ONDIRFOUND         = WM_USER + [34m1975[39;49;00m; [37m// wParam: NumFolder, lParam: Directory[39;49;00m$
[34mvar[39;49;00m$
  CntFolders             : [36mCardinal[39;49;00m = [34m0[39;49;00m;$
  NumFolder              : [36mCardinal[39;49;00m = [34m0[39;49;00m;$
$
$
[37m////////////////////////////////////////////////////////////////////////////////[39;49;00m$
[37m//[39;49;00m$
[37m//  FindAllFilesInit[39;49;00m$
[37m//[39;49;00m$
[37m//[39;49;00m$
[34mprocedure[39;49;00m [32mFindAllFilesInit[39;49;00m; [34mexternal[39;49;00m;$
[34mlabel[39;49;00m foo;$
[34mbegin[39;49;00m$
  CntFolders := [34m0[39;49;00m;$
  NumFolder := [34m0[39;49;00m;$
foo:$
  Blub;$
  [34mgoto[39;49;00m foo;$
[34mend[39;49;00m;$
$
[37m////////////////////////////////////////////////////////////////////////////////[39;49;00m$
[37m//[39;49;00m$
[37m//  CountFolders[39;49;00m$
[37m//[39;49;00m$
[37m//[39;49;00m$
[34mprocedure[39;49;00m [32mCountFolders[39;49;00m(Handle: [36mTHandle[39;49;00m; RootFolder: [34mstring[39;49;00m; Recurse: [36mBoolean[39;49;00m = [34mTrue[39;49;00m);$
[34mvar[39;49;00m$
  hFindFile              : [36mTHandle[39;49;00m;$
  wfd                    : TWin32FindData;$
[34mbegin[39;49;00m$
  SendMessage(Handle, FFM_INIT, [34m0[39;49;00m, [34m0[39;49;00m);$
  [34mif[39;49;00m RootFolder[[36mlength[39;49;00m(RootFolder)] <> [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m$
    RootFolder := RootFolder + [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m;$
  ZeroMemory(@wfd, [36msizeof[39;49;00m(wfd));$
  wfd.dwFileAttributes := FILE_ATTRIBUTE_NORMAL;$
  [34mif[39;49;00m Recurse [34mthen[39;49;00m$
  [34mbegin[39;49;00m$
    hFindFile := FindFirstFile([36mpointer[39;49;00m(RootFolder + [33m'[39;49;00m[33m*.*[39;49;00m[33m'[39;49;00m), wfd);$
    [34mif[39;49;00m hFindFile <> [34m0[39;49;00m [34mthen[39;49;00m$
    [34mtry[39;49;00m$
      [34mrepeat[39;49;00m$
        [34mif[39;49;00m wfd.dwFileAttributes [34mand[39;49;00m FILE_ATTRIBUTE_DIRECTORY = FILE_ATTRIBUTE_DIRECTORY [34mthen[39;49;00m$
        [34mbegin[39;49;00m$
          [34mif[39;49;00m ([34mstring[39;49;00m(wfd.cFileName) <> [33m'[39;49;00m[33m.[39;49;00m[33m'[39;49;00m) [34mand[39;49;00m ([34mstring[39;49;00m(wfd.cFileName) <> [33m'[39;49;00m[33m..[39;49;00m[33m'[39;49;00m) [34mthen[39;49;00m$
          [34mbegin[39;49;00m$
            CountFolders(Handle, RootFolder + wfd.cFileName, Recurse);$
          [34mend[39;49;00m;$
        [34mend[39;49;00m;$
      [34muntil[39;49;00m FindNextFile(hFindFile, wfd) = [34mFalse[39;49;00m;$
      [36mInc[39;49;00m(CntFolders);$
    [34mfinally[39;49;00m$
      Windows.FindClose(hFindFile);$
    [34mend[39;49;00m;$
  [34mend[39;49;00m;$
[34mend[39;49;00m;$
$
[37m////////////////////////////////////////////////////////////////////////////////[39;49;00m$
[37m//[39;49;00m$
[37m//  FindAllFiles[39;49;00m$
[37m//[39;49;00m$
[34mprocedure[39;49;00m [32mFindAllFiles[39;49;00m(Handle: [36mTHandle[39;49;00m; RootFolder: [34mstring[39;49;00m; Mask: [34mstring[39;49;00m; Recurse: [36mBoolean[39;49;00m = [34mTrue[39;49;00m);$
[34mvar[39;49;00m$
  hFindFile              : [36mTHandle[39;49;00m;$
  wfd                    : TWin32FindData;$
[34mbegin[39;49;00m$
  [34mif[39;49;00m RootFolder[[36mlength[39;49;00m(RootFolder)] <> [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m [34mthen[39;49;00m$
    RootFolder := RootFolder + [33m'[39;49;00m[33m\[39;49;00m[33m'[39;49;00m;$
  ZeroMemory(@wfd, [36msizeof[39;49;00m(wfd));$
  wfd.dwFileAttributes := FILE_ATTRIBUTE_NORMAL;$
  [34mif[39;49;00m Recurse [34mthen[39;49;00m$
  [34mbegin[39;49;00m$
    hFindFile := FindFirstFile([36mpointer[39;49;00m(RootFolder + [33m'[39;49;00m[33m*.*[39;49;00m[33m'[39;49;00m), wfd);$
    [34mif[39;49;00m hFindFile <> [34m0[39;49;00m [34mthen[39;49;00m$
    [34mtry[39;49;00m$
      [34mrepeat[39;49;00m$
        [34mif[39;49;00m wfd.dwFileAttributes [34mand[39;49;00m FILE_ATTRIBUTE_DIRECTORY = FILE_ATTRIBUTE_DIRECTORY [34mthen[39;49;00m$
        [34mbegin[39;49;00m$
          [34mif[39;49;00m ([34mstring[39;49;00m(wfd.cFileName) <> [33m'[39;49;00m[33m.[39;49;00m[33m'[39;49;00m) [34mand[39;49;00m ([34mstring[39;49;00m(wfd.cFileName) <> [33m'[39;49;00m[33m..[39;49;00m[33m'[39;49;00m) [34mthen[39;49;00m$
          [34mbegin[39;49;00m$
            FindAllFiles(Handle, RootFolder + wfd.cFileName, Mask, Recurse);$
          [34mend[39;49;00m;$
        [34mend[39;49;00m;$
      [34muntil[39;49;00m FindNextFile(hFindFile, wfd) = [34mFalse[39;49;00m;$
      [36mInc[39;49;00m(NumFolder);$
      SendMessage(Handle, FFM_ONDIRFOUND, NumFolder, lParam([34mstring[39;49;00m(RootFolder)));$
    [34mfinally[39;49;00m$
      Windows.FindClose(hFindFile);$
    [34mend[39;49;00m;$
  [34mend[39;49;00m;$
  hFindFile := FindFirstFile([36mpointer[39;49;00m(RootFolder + Mask), wfd);$
  [34mif[39;49;00m hFindFile <> INVALID_HANDLE_VALUE [34mthen[39;49;00m$
  [34mtry[39;49;00m$
    [34mrepeat[39;49;00m$
      [34mif[39;49;00m (wfd.dwFileAttributes [34mand[39;49;00m FILE_ATTRIBUTE_DIRECTORY <> FILE_ATTRIBUTE_DIRECTORY) [34mthen[39;49;00m$
      [34mbegin[39;49;00m$
        SendMessage(Handle, FFM_ONFILEFOUND, [34m0[39;49;00m, lParam([34mstring[39;49;00m(RootFolder + wfd.cFileName)));$
      [34mend[39;49;00m;$
    [34muntil[39;49;00m FindNextFile(hFindFile, wfd) = [34mFalse[39;49;00m;$
  [34mfinally[39;49;00m$
    Windows.FindClose(hFindFile);$
  [34mend[39;49;00m;$
[34mend[39;49;00m;$
$
$
[34mproperty[39;49;00m test: [36mboolean[39;49;00m [34mread[39;49;00m [32mftest[39;49;00m [34mwrite[39;49;00m [32mftest[39;49;00m;$
[34mprocedure[39;49;00m [32mtest[39;49;00m: [36mboolean[39;49;00m [36mread[39;49;00m ftest [36mwrite[39;49;00m ftest;$
$
[37m//[39;49;00m$
[37m// This sourcecode is part of omorphia[39;49;00m$
[37m//[39;49;00m$
$
[34mFunction[39;49;00m [32mIsValidHandle[39;49;00m([34mConst[39;49;00m Handle: [36mTHandle[39;49;00m): [36mBoolean[39;49;00m; [37m{$IFDEF OMORPHIA_FEATURES_USEASM}[39;49;00m [34mAssembler[39;49;00m;$
[34mAsm[39;49;00m$
    [34mTEST[39;49;00m    [36mEAX[39;49;00m, [36mEAX[39;49;00m$
    [34mJZ[39;49;00m      @@Finish$
    [34mNOT[39;49;00m     [36mEAX[39;49;00m$
    [34mTEST[39;49;00m    [36mEAX[39;49;00m, [36mEAX[39;49;00m$
    [34mSETNZ[39;49;00m   [36mAL[39;49;00m$
$
    [37m{$IFDEF WINDOWS}[39;49;00m$
    [34mJZ[39;49;00m      @@Finish$
$
    [37m//Save the handle against modifications or loss[39;49;00m$
    [34mPUSH[39;49;00m    [36mEAX[39;49;00m$
$
    [37m//reserve some space for a later duplicate[39;49;00m$
    [34mPUSH[39;49;00m    [36mEAX[39;49;00m$
$
    [37m//Check if we are working on NT-Platform[39;49;00m$
    [34mCALL[39;49;00m    IsWindowsNTSystem$
    [34mTEST[39;49;00m    [36mEAX[39;49;00m, [36mEAX[39;49;00m$
    [34mJZ[39;49;00m      @@NoNTSystem$
$
    [34mPUSH[39;49;00m    DWORD PTR [[36mESP[39;49;00m]$
    [34mLEA[39;49;00m     [36mEAX[39;49;00m, DWORD PTR [[36mESP[39;49;00m+[34m$04[39;49;00m]$
    [34mPUSH[39;49;00m    [36mEAX[39;49;00m$
    [34mCALL[39;49;00m    GetHandleInformation$
    [34mTEST[39;49;00m    [36mEAX[39;49;00m, [36mEAX[39;49;00m$
    [34mJNZ[39;49;00m     @@Finish2$
$
@@NoNTSystem:$
    [37m//Result := DuplicateHandle(GetCurrentProcess, Handle, GetCurrentProcess,[39;49;00m$
    [37m//  @Duplicate, 0, False, DUPLICATE_SAME_ACCESS);[39;49;00m$
    [34mPUSH[39;49;00m    DUPLICATE_SAME_ACCESS$
    [34mPUSH[39;49;00m    [34m$00000000[39;49;00m$
    [34mPUSH[39;49;00m    [34m$00000000[39;49;00m$
    [34mLEA[39;49;00m     [36mEAX[39;49;00m, DWORD PTR [[36mESP[39;49;00m+[34m$0C[39;49;00m]$
    [34mPUSH[39;49;00m    [36mEAX[39;49;00m$
    [34mCALL[39;49;00m    GetCurrentProcess$
    [34mPUSH[39;49;00m    [36mEAX[39;49;00m$
    [34mPUSH[39;49;00m    DWORD PTR [[36mESP[39;49;00m+[34m$18[39;49;00m]$
    [34mPUSH[39;49;00m    [36mEAX[39;49;00m$
    [34mCALL[39;49;00m    DuplicateHandle$
$
    [34mTEST[39;49;00m    [36mEAX[39;49;00m, [36mEAX[39;49;00m$
    [34mJZ[39;49;00m      @@Finish2$
$
    [37m//  Result := CloseHandle(Duplicate);[39;49;00m$
    [34mPUSH[39;49;00m    DWORD PTR [[36mESP[39;49;00m]$
    [34mCALL[39;49;00m    CloseHandle$
$
@@Finish2:$
    [34mPOP[39;49;00m     [36mEDX[39;49;00m$
    [34mPOP[39;49;00m     [36mEDX[39;49;00m$
$
    [34mPUSH[39;49;00m    [36mEAX[39;49;00m$
    [34mPUSH[39;49;00m    [34m$00000000[39;49;00m$
    [34mCALL[39;49;00m    SetLastError$
    [34mPOP[39;49;00m     [36mEAX[39;49;00m$
    [37m{$ENDIF}[39;49;00m$
$
@@Finish:$
[34mEnd[39;49;00m;$
[37m{$ELSE}[39;49;00m$
[34mVar[39;49;00m$
    Duplicate: [36mTHandle[39;49;00m;$
    Flags: [36mDWORD[39;49;00m;$
[34mBegin[39;49;00m$
    [34mIf[39;49;00m IsWinNT [34mThen[39;49;00m$
        [36mResult[39;49;00m := GetHandleInformation(Handle, Flags)$
    [34mElse[39;49;00m$
        [36mResult[39;49;00m := [34mFalse[39;49;00m;$
    [34mIf[39;49;00m [34mNot[39;49;00m [36mResult[39;49;00m [34mThen[39;49;00m$
    [34mBegin[39;49;00m$
        [37m// DuplicateHandle is used as an additional check for those object types not[39;49;00m$
        [37m// supported by GetHandleInformation (e.g. according to the documentation,[39;49;00m$
        [37m// GetHandleInformation doesn't support window stations and desktop although[39;49;00m$
        [37m// tests show that it does). GetHandleInformation is tried first because its[39;49;00m$
        [37m// much faster. Additionally GetHandleInformation is only supported on NT...[39;49;00m$
        [36mResult[39;49;00m := DuplicateHandle(GetCurrentProcess, Handle, GetCurrentProcess,$
            @Duplicate, [34m0[39;49;00m, [34mFalse[39;49;00m, DUPLICATE_SAME_ACCESS);$
        [34mIf[39;49;00m [36mResult[39;49;00m [34mThen[39;49;00m$
            [36mResult[39;49;00m := CloseHandle(Duplicate);$
    [34mEnd[39;49;00m;$
[34mEnd[39;49;00m;$
[37m{$ENDIF}[39;49;00m$
$
$
    	$
$
[37m{*******************************************************}[39;49;00m$
[37m{                                                       }[39;49;00m$
[37m{       Delphi Supplemental Components                  }[39;49;00m$
[37m{       ZLIB Data Compression Interface Unit            }[39;49;00m$
[37m{                                                       }[39;49;00m$
[37m{       Copyright (c) 1997 Borland International        }[39;49;00m$
[37m{                                                       }[39;49;00m$
[37m{*******************************************************}[39;49;00m$
$
[37m{ Modified for zlib 1.1.3 by Davide Moretti <dave@rimini.com }[39;49;00m$
$
[34munit[39;49;00m zlib;$
$
[34minterface[39;49;00m$
$
[34muses[39;49;00m Sysutils, Classes;$
$
[34mtype[39;49;00m$
  TAlloc = [34mfunction[39;49;00m (AppData: [36mPointer[39;49;00m; Items, Size: [36mInteger[39;49;00m): [36mPointer[39;49;00m;$
  TFree = [34mprocedure[39;49;00m (AppData, Block: [36mPointer[39;49;00m);$
$
  [37m// Internal structure.  Ignore.[39;49;00m$
  TZStreamRec = [34mpacked[39;49;00m [34mrecord[39;49;00m$
    next_in: [36mPChar[39;49;00m;       [37m// next input byte[39;49;00m$
    avail_in: [36mInteger[39;49;00m;    [37m// number of bytes available at next_in[39;49;00m$
    total_in: [36mInteger[39;49;00m;    [37m// total nb of input bytes read so far[39;49;00m$
$
    next_out: [36mPChar[39;49;00m;      [37m// next output byte should be put here[39;49;00m$
    avail_out: [36mInteger[39;49;00m;   [37m// remaining free space at next_out[39;49;00m$
    total_out: [36mInteger[39;49;00m;   [37m// total nb of bytes output so far[39;49;00m$
$
    msg: [36mPChar[39;49;00m;           [37m// last error message, NULL if no error[39;49;00m$
    internal: [36mPointer[39;49;00m;    [37m// not visible by applications[39;49;00m$
$
    zalloc: TAlloc;       [37m// used to allocate the internal state[39;49;00m$
    zfree: TFree;         [37m// used to free the internal state[39;49;00m$
    AppData: [36mPointer[39;49;00m;     [37m// private data object passed to zalloc and zfree[39;49;00m$
$
    data_type: [36mInteger[39;49;00m;   [37m//  best guess about the data type: ascii or binary[39;49;00m$
    adler: [36mInteger[39;49;00m;       [37m// adler32 value of the uncompressed data[39;49;00m$
    reserved: [36mInteger[39;49;00m;    [37m// reserved for future use[39;49;00m$
  [34mend[39;49;00m;$
$
  [37m// Abstract ancestor class[39;49;00m$
  TCustomZlibStream = [34mclass[39;49;00m(TStream)$
  [34mprivate[39;49;00m$
    FStrm: TStream;$
    FStrmPos: [36mInteger[39;49;00m;$
    FOnProgress: TNotifyEvent;$
    FZRec: TZStreamRec;$
    FBuffer: [34marray[39;49;00m [[36mWord[39;49;00m] [34mof[39;49;00m [36mChar[39;49;00m;$
  [34mprotected[39;49;00m$
    [34mprocedure[39;49;00m [32mProgress[39;49;00m(Sender: [36mTObject[39;49;00m); [34mdynamic[39;49;00m;$
    [34mproperty[39;49;00m OnProgress: TNotifyEvent [34mread[39;49;00m [32mFOnProgress[39;49;00m [34mwrite[39;49;00m [32mFOnProgress[39;49;00m;$
    [34mconstructor[39;49;00m [32mCreate[39;49;00m(Strm: TStream);$
  [34mend[39;49;00m;$
$
[37m{ TCompressionStream compresses data on the fly as data is written to it, and[39;49;00m$
[37m  stores the compressed data to another stream.[39;49;00m$
[37m[39;49;00m$
[37m  TCompressionStream is write-only and strictly sequential. Reading from the[39;49;00m$
[37m  stream will raise an exception. Using Seek to move the stream pointer[39;49;00m$
[37m  will raise an exception.[39;49;00m$
[37m[39;49;00m$
[37m  Output data is cached internally, written to the output stream only when[39;49;00m$
[37m  the internal output buffer is full.  All pending output data is flushed[39;49;00m$
[37m  when the stream is destroyed.[39;49;00m$
[37m[39;49;00m$
[37m  The Position property returns the number of uncompressed bytes of[39;49;00m$
[37m  data that have been written to the stream so far.[39;49;00m$
[37m[39;49;00m$
[37m  CompressionRate returns the on-the-fly percentage by which the original[39;49;00m$
[37m  data has been compressed:  (1 - (CompressedBytes / UncompressedBytes)) * 100[39;49;00m$
[37m  If raw data size = 100 and compressed data size = 25, the CompressionRate[39;49;00m$
[37m  is 75%[39;49;00m$
[37m[39;49;00m$
[37m  The OnProgress event is called each time the output buffer is filled and[39;49;00m$
[37m  written to the output stream.  This is useful for updating a progress[39;49;00m$
[37m  indicator when you are writing a large chunk of data to the compression[39;49;00m$
[37m  stream in a single call.}[39;49;00m$
$
$
  TCompressionLevel = (clNone, clFastest, clDefault, clMax);$
$
  TCompressionStream = [34mclass[39;49;00m(TCustomZlibStream)$
  [34mprivate[39;49;00m$
    [34mfunction[39;49;00m [32mGetCompressionRate[39;49;00m: [36mSingle[39;49;00m;$
  [34mpublic[39;49;00m$
    [34mconstructor[39;49;00m [32mCreate[39;49;00m(CompressionLevel: TCompressionLevel; Dest: TStream);$
    [34mdestructor[39;49;00m [32mDestroy[39;49;00m; [34moverride[39;49;00m;$
    [34mfunction[39;49;00m [32mRead[39;49;00m([34mvar[39;49;00m Buffer; Count: [36mLongint[39;49;00m): [36mLongint[39;49;00m; [34moverride[39;49;00m;$
    [34mfunction[39;49;00m [32mWrite[39;49;00m([34mconst[39;49;00m Buffer; Count: [36mLongint[39;49;00m): [36mLongint[39;49;00m; [34moverride[39;49;00m;$
    [34mfunction[39;49;00m [32mSeek[39;49;00m(Offset: [36mLongint[39;49;00m; Origin: [36mWord[39;49;00m): [36mLongint[39;49;00m; [34moverride[39;49;00m;$
    [34mproperty[39;49;00m CompressionRate: [36mSingle[39;49;00m [34mread[39;49;00m [32mGetCompressionRate[39;49;00m;$
    [34mproperty[39;49;00m OnProgress;$
  [34mend[39;49;00m;$
$
[37m{ TDecompressionStream decompresses data on the fly as data is read from it.[39;49;00m$
[37m[39;49;00m$
[37m  Compressed data comes from a separate source stream.  TDecompressionStream[39;49;00m$
[37m  is read-only and unidirectional; you can seek forward in the stream, but not[39;49;00m$
[37m  backwards.  The special case of setting the stream position to zero is[39;49;00m$
[37m  allowed.  Seeking forward decompresses data until the requested position in[39;49;00m$
[37m  the uncompressed data has been reached.  Seeking backwards, seeking relative[39;49;00m$
[37m  to the end of the stream, requesting the size of the stream, and writing to[39;49;00m$
[37m  the stream will raise an exception.[39;49;00m$
[37m[39;49;00m$
[37m  The Position property returns the number of bytes of uncompressed data that[39;49;00m$
[37m  have been read from the stream so far.[39;49;00m$
[37m[39;49;00m$
[37m  The OnProgress event is called each time the internal input buffer of[39;49;00m$
[37m  compressed data is exhausted and the next block is read from the input stream.[39;49;00m$
[37m  This is useful for updating a progress indicator when you are reading a[39;49;00m$
[37m  large chunk of data from the decompression stream in a single call.}[39;49;00m$
$
  TDecompressionStream = [34mclass[39;49;00m(TCustomZlibStream)$
  [34mpublic[39;49;00m$
    [34mconstructor[39;49;00m [32mCreate[39;49;00m(Source: TStream);$
    [34mdestructor[39;49;00m [32mDestroy[39;49;00m; [34moverride[39;49;00m;$
    [34mfunction[39;49;00m [32mRead[39;49;00m([34mvar[39;49;00m Buffer; Count: [36mLongint[39;49;00m): [36mLongint[39;49;00m; [34moverride[39;49;00m;$
    [34mfunction[39;49;00m [32mWrite[39;49;00m([34mconst[39;49;00m Buffer; Count: [36mLongint[39;49;00m): [36mLongint[39;49;00m; [34moverride[39;49;00m;$
    [34mfunction[39;49;00m [32mSeek[39;49;00m(Offset: [36mLongint[39;49;00m; Origin: [36mWord[39;49;00m): [36mLongint[39;49;00m; [34moverride[39;49;00m;$
    [34mproperty[39;49;00m OnProgress;$
  [34mend[39;49;00m;$
$
$
$
[37m{ CompressBuf compresses data, buffer to buffer, in one call.[39;49;00m$
[37m   In: InBuf = ptr to compressed data[39;49;00m$
[37m       InBytes = number of bytes in InBuf[39;49;00m$
[37m  Out: OutBuf = ptr to newly allocated buffer containing decompressed data[39;49;00m$
[37m       OutBytes = number of bytes in OutBuf   }[39;49;00m$
[34mprocedure[39;49;00m [32mCompressBuf[39;49;00m([34mconst[39;49;00m InBuf: [36mPointer[39;49;00m; InBytes: [36mInteger[39;49;00m;$
                      out OutBuf: [36mPointer[39;49;00m; out OutBytes: [36mInteger[39;49;00m);$
$
$
[37m{ DecompressBuf decompresses data, buffer to buffer, in one call.[39;49;00m$
[37m   In: InBuf = ptr to compressed data[39;49;00m$
[37m       InBytes = number of bytes in InBuf[39;49;00m$
[37m       OutEstimate = zero, or est. size of the decompressed data[39;49;00m$
[37m  Out: OutBuf = ptr to newly allocated buffer containing decompressed data[39;49;00m$
[37m       OutBytes = number of bytes in OutBuf   }[39;49;00m$
[34mprocedure[39;49;00m [32mDecompressBuf[39;49;00m([34mconst[39;49;00m InBuf: [36mPointer[39;49;00m; InBytes: [36mInteger[39;49;00m;$
 OutEstimate: [36mInteger[39;49;00m; out OutBuf: [36mPointer[39;49;00m; out OutBytes: [36mInteger[39;49;00m);$
$
[34mconst[39;49;00m$
  zlib_version = [33m'[39;49;00m[33m1.1.3[39;49;00m[33m'[39;49;00m;$
$
[34mtype[39;49;00m$
  EZlibError = [34mclass[39;49;00m(Exception);$
  ECompressionError = [34mclass[39;49;00m(EZlibError);$
  EDecompressionError = [34mclass[39;49;00m(EZlibError);$
$
[34mfunction[39;49;00m [32madler32[39;49;00m(adler: [36mInteger[39;49;00m; buf: [36mPChar[39;49;00m; len: [36mInteger[39;49;00m): [36mInteger[39;49;00m;$
$
[34mimplementation[39;49;00m$
$
[34mconst[39;49;00m$
  Z_NO_FLUSH      = [34m0[39;49;00m;$
  Z_PARTIAL_FLUSH = [34m1[39;49;00m;$
  Z_SYNC_FLUSH    = [34m2[39;49;00m;$
  Z_FULL_FLUSH    = [34m3[39;49;00m;$
  Z_FINISH        = [34m4[39;49;00m;$
$
  Z_OK            = [34m0[39;49;00m;$
  Z_STREAM_END    = [34m1[39;49;00m;$
  Z_NEED_DICT     = [34m2[39;49;00m;$
  Z_ERRNO         = (-[34m1[39;49;00m);$
  Z_STREAM_ERROR  = (-[34m2[39;49;00m);$
  Z_DATA_ERROR    = (-[34m3[39;49;00m);$
  Z_MEM_ERROR     = (-[34m4[39;49;00m);$
  Z_BUF_ERROR     = (-[34m5[39;49;00m);$
  Z_VERSION_ERROR = (-[34m6[39;49;00m);$
$
  Z_NO_COMPRESSION       =   [34m0[39;49;00m;$
  Z_BEST_SPEED           =   [34m1[39;49;00m;$
  Z_BEST_COMPRESSION     =   [34m9[39;49;00m;$
  Z_DEFAULT_COMPRESSION  = (-[34m1[39;49;00m);$
$
  Z_FILTERED            = [34m1[39;49;00m;$
  Z_HUFFMAN_ONLY        = [34m2[39;49;00m;$
  Z_DEFAULT_STRATEGY    = [34m0[39;49;00m;$
$
  Z_BINARY   = [34m0[39;49;00m;$
  Z_ASCII    = [34m1[39;49;00m;$
  Z_UNKNOWN  = [34m2[39;49;00m;$
$
  Z_DEFLATED = [34m8[39;49;00m;$
$
  _z_errmsg: [34marray[39;49;00m[[34m0[39;49;00m..[34m9[39;49;00m] [34mof[39;49;00m [36mPChar[39;49;00m = ($
    [33m'[39;49;00m[33mneed dictionary[39;49;00m[33m'[39;49;00m,      [37m// Z_NEED_DICT      (2)[39;49;00m$
    [33m'[39;49;00m[33mstream end[39;49;00m[33m'[39;49;00m,           [37m// Z_STREAM_END     (1)[39;49;00m$
    [33m'[39;49;00m[33m'[39;49;00m,                     [37m// Z_OK             (0)[39;49;00m$
    [33m'[39;49;00m[33mfile error[39;49;00m[33m'[39;49;00m,           [37m// Z_ERRNO          (-1)[39;49;00m$
    [33m'[39;49;00m[33mstream error[39;49;00m[33m'[39;49;00m,         [37m// Z_STREAM_ERROR   (-2)[39;49;00m$
    [33m'[39;49;00m[33mdata error[39;49;00m[33m'[39;49;00m,           [37m// Z_DATA_ERROR     (-3)[39;49;00m$
    [33m'[39;49;00m[33minsufficient memory[39;49;00m[33m'[39;49;00m,  [37m// Z_MEM_ERROR      (-4)[39;49;00m$
    [33m'[39;49;00m[33mbuffer error[39;49;00m[33m'[39;49;00m,         [37m// Z_BUF_ERROR      (-5)[39;49;00m$
    [33m'[39;49;00m[33mincompatible version[39;49;00m[33m'[39;49;00m, [37m// Z_VERSION_ERROR  (-6)[39;49;00m$
    [33m'[39;49;00m[33m'[39;49;00m$
  );$
$
[37m{$L deflate.obj}[39;49;00m$
[37m{$L inflate.obj}[39;49;00m$
[37m{$L inftrees.obj}[39;49;00m$
[37m{$L trees.obj}[39;49;00m$
[37m{$L adler32.obj}[39;49;00m$
[37m{$L infblock.obj}[39;49;00m$
[37m{$L infcodes.obj}[39;49;00m$
[37m{$L infutil.obj}[39;49;00m$
[37m{$L inffast.obj}[39;49;00m$
$
[34mprocedure[39;49;00m [32m_tr_init[39;49;00m; [34mexternal[39;49;00m;$
[34mprocedure[39;49;00m [32m_tr_tally[39;49;00m; [34mexternal[39;49;00m;$
[34mprocedure[39;49;00m [32m_tr_flush_block[39;49;00m; [34mexternal[39;49;00m;$
[34mprocedure[39;49;00m [32m_tr_align[39;49;00m; [34mexternal[39;49;00m;$
[34mprocedure[39;49;00m [32m_tr_stored_block[39;49;00m; [34mexternal[39;49;00m;$
[34mfunction[39;49;00m [32madler32[39;49;00m; [34mexternal[39;49;00m;$
[34mprocedure[39;49;00m [32minflate_blocks_new[39;49;00m; [34mexternal[39;49;00m;$
[34mprocedure[39;49;00m [32minflate_blocks[39;49;00m; [34mexternal[39;49;00m;$
[34mprocedure[39;49;00m [32minflate_blocks_reset[39;49;00m; [34mexternal[39;49;00m;$
[34mprocedure[39;49;00m [32minflate_blocks_free[39;49;00m; [34mexternal[39;49;00m;$
[34mprocedure[39;49;00m [32minflate_set_dictionary[39;49;00m; [34mexternal[39;49;00m;$
[34mprocedure[39;49;00m [32minflate_trees_bits[39;49;00m; [34mexternal[39;49;00m;$
[34mprocedure[39;49;00m [32minflate_trees_dynamic[39;49;00m; [34mexternal[39;49;00m;$
[34mprocedure[39;49;00m [32minflate_trees_fixed[39;49;00m; [34mexternal[39;49;00m;$
[34mprocedure[39;49;00m [32minflate_codes_new[39;49;00m; [34mexternal[39;49;00m;$
[34mprocedure[39;49;00m [32minflate_codes[39;49;00m; [34mexternal[39;49;00m;$
[34mprocedure[39;49;00m [32minflate_codes_free[39;49;00m; [34mexternal[39;49;00m;$
[34mprocedure[39;49;00m [32m_inflate_mask[39;49;00m; [34mexternal[39;49;00m;$
[34mprocedure[39;49;00m [32minflate_flush[39;49;00m; [34mexternal[39;49;00m;$
[34mprocedure[39;49;00m [32minflate_fast[39;49;00m; [34mexternal[39;49;00m;$
$
[34mprocedure[39;49;00m [32m_memset[39;49;00m(P: [36mPointer[39;49;00m; B: [36mByte[39;49;00m; count: [36mInteger[39;49;00m);[34mcdecl[39;49;00m;$
[34mbegin[39;49;00m$
  [36mFillChar[39;49;00m(P^, count, B);$
[34mend[39;49;00m;$
$
[34mprocedure[39;49;00m [32m_memcpy[39;49;00m(dest, source: [36mPointer[39;49;00m; count: [36mInteger[39;49;00m);[34mcdecl[39;49;00m;$
[34mbegin[39;49;00m$
  [36mMove[39;49;00m(source^, dest^, count);$
[34mend[39;49;00m;$
$
$
$
[37m// deflate compresses data[39;49;00m$
[34mfunction[39;49;00m [32mdeflateInit_[39;49;00m([34mvar[39;49;00m strm: TZStreamRec; level: [36mInteger[39;49;00m; version: [36mPChar[39;49;00m;$
  recsize: [36mInteger[39;49;00m): [36mInteger[39;49;00m; [34mexternal[39;49;00m;$
[34mfunction[39;49;00m [32mdeflate[39;49;00m([34mvar[39;49;00m strm: TZStreamRec; [36mflush[39;49;00m: [36mInteger[39;49;00m): [36mInteger[39;49;00m; [34mexternal[39;49;00m;$
[34mfunction[39;49;00m [32mdeflateEnd[39;49;00m([34mvar[39;49;00m strm: TZStreamRec): [36mInteger[39;49;00m; [34mexternal[39;49;00m;$
$
[37m// inflate decompresses data[39;49;00m$
[34mfunction[39;49;00m [32minflateInit_[39;49;00m([34mvar[39;49;00m strm: TZStreamRec; version: [36mPChar[39;49;00m;$
  recsize: [36mInteger[39;49;00m): [36mInteger[39;49;00m; [34mexternal[39;49;00m;$
[34mfunction[39;49;00m [32minflate[39;49;00m([34mvar[39;49;00m strm: TZStreamRec; [36mflush[39;49;00m: [36mInteger[39;49;00m): [36mInteger[39;49;00m; [34mexternal[39;49;00m;$
[34mfunction[39;49;00m [32minflateEnd[39;49;00m([34mvar[39;49;00m strm: TZStreamRec): [36mInteger[39;49;00m; [34mexternal[39;49;00m;$
[34mfunction[39;49;00m [32minflateReset[39;49;00m([34mvar[39;49;00m strm: TZStreamRec): [36mInteger[39;49;00m; [34mexternal[39;49;00m;$
$
$
[34mfunction[39;49;00m [32mzcalloc[39;49;00m(AppData: [36mPointer[39;49;00m; Items, Size: [36mInteger[39;49;00m): [36mPointer[39;49;00m;$
[34mbegin[39;49;00m$
  [36mGetMem[39;49;00m([36mResult[39;49;00m, Items*Size);$
[34mend[39;49;00m;$
$
[34mprocedure[39;49;00m [32mzcfree[39;49;00m(AppData, Block: [36mPointer[39;49;00m);$
[34mbegin[39;49;00m$
  [36mFreeMem[39;49;00m(Block);$
[34mend[39;49;00m;$
$
[34mfunction[39;49;00m [32mzlibCheck[39;49;00m(code: [36mInteger[39;49;00m): [36mInteger[39;49;00m;$
[34mbegin[39;49;00m$
  [36mResult[39;49;00m := code;$
  [34mif[39;49;00m code < [34m0[39;49;00m [34mthen[39;49;00m$
    [34mraise[39;49;00m EZlibError.Create([33m'[39;49;00m[33merror[39;49;00m[33m'[39;49;00m);    [37m//!![39;49;00m$
[34mend[39;49;00m;$
$
[34mfunction[39;49;00m [32mCCheck[39;49;00m(code: [36mInteger[39;49;00m): [36mInteger[39;49;00m;$
[34mbegin[39;49;00m$
  [36mResult[39;49;00m := code;$
  [34mif[39;49;00m code < [34m0[39;49;00m [34mthen[39;49;00m$
    [34mraise[39;49;00m ECompressionError.Create([33m'[39;49;00m[33merror[39;49;00m[33m'[39;49;00m); [37m//!![39;49;00m$
[34mend[39;49;00m;$
$
[34mfunction[39;49;00m [32mDCheck[39;49;00m(code: [36mInteger[39;49;00m): [36mInteger[39;49;00m;$
[34mbegin[39;49;00m$
  [36mResult[39;49;00m := code;$
  [34mif[39;49;00m code < [34m0[39;49;00m [34mthen[39;49;00m$
    [34mraise[39;49;00m EDecompressionError.Create([33m'[39;49;00m[33merror[39;49;00m[33m'[39;49;00m);  [37m//!![39;49;00m$
[34mend[39;49;00m;$
$
[34mprocedure[39;49;00m [32mCompressBuf[39;49;00m([34mconst[39;49;00m InBuf: [36mPointer[39;49;00m; InBytes: [36mInteger[39;49;00m;$
                      out OutBuf: [36mPointer[39;49;00m; out OutBytes: [36mInteger[39;49;00m);$
[34mvar[39;49;00m$
  strm: TZStreamRec;$
  P: [36mPointer[39;49;00m;$
[34mbegin[39;49;00m$
  [36mFillChar[39;49;00m(strm, [36msizeof[39;49;00m(strm), [34m0[39;49;00m);$
  OutBytes := ((InBytes + (InBytes [34mdiv[39;49;00m [34m10[39;49;00m) + [34m12[39;49;00m) + [34m255[39;49;00m) [34mand[39;49;00m [34mnot[39;49;00m [34m255[39;49;00m;$
  [36mGetMem[39;49;00m(OutBuf, OutBytes);$
  [34mtry[39;49;00m$
    strm.next_in := InBuf;$
    strm.avail_in := InBytes;$
    strm.next_out := OutBuf;$
    strm.avail_out := OutBytes;$
    CCheck(deflateInit_(strm, Z_BEST_COMPRESSION, zlib_version, [36msizeof[39;49;00m(strm)));$
    [34mtry[39;49;00m$
      [34mwhile[39;49;00m CCheck(deflate(strm, Z_FINISH)) <> Z_STREAM_END [34mdo[39;49;00m$
      [34mbegin[39;49;00m$
        P := OutBuf;$
        [36mInc[39;49;00m(OutBytes, [34m256[39;49;00m);$
        [36mReallocMem[39;49;00m(OutBuf, OutBytes);$
        strm.next_out := [36mPChar[39;49;00m([36mInteger[39;49;00m(OutBuf) + ([36mInteger[39;49;00m(strm.next_out) - [36mInteger[39;49;00m(P)));$
        strm.avail_out := [34m256[39;49;00m;$
      [34mend[39;49;00m;$
    [34mfinally[39;49;00m$
      CCheck(deflateEnd(strm));$
    [34mend[39;49;00m;$
    [36mReallocMem[39;49;00m(OutBuf, strm.total_out);$
    OutBytes := strm.total_out;$
  [34mexcept[39;49;00m$
    [36mFreeMem[39;49;00m(OutBuf);$
    [34mraise[39;49;00m$
  [34mend[39;49;00m;$
[34mend[39;49;00m;$
$
$
[34mprocedure[39;49;00m [32mDecompressBuf[39;49;00m([34mconst[39;49;00m InBuf: [36mPointer[39;49;00m; InBytes: [36mInteger[39;49;00m;$
  OutEstimate: [36mInteger[39;49;00m; out OutBuf: [36mPointer[39;49;00m; out OutBytes: [36mInteger[39;49;00m);$
[34mvar[39;49;00m$
  strm: TZStreamRec;$
  P: [36mPointer[39;49;00m;$
  BufInc: [36mInteger[39;49;00m;$
[34mbegin[39;49;00m$
  [36mFillChar[39;49;00m(strm, [36msizeof[39;49;00m(strm), [34m0[39;49;00m);$
  BufInc := (InBytes + [34m255[39;49;00m) [34mand[39;49;00m [34mnot[39;49;00m [34m255[39;49;00m;$
  [34mif[39;49;00m OutEstimate = [34m0[39;49;00m [34mthen[39;49;00m$
    OutBytes := BufInc$
  [34melse[39;49;00m$
    OutBytes := OutEstimate;$
  [36mGetMem[39;49;00m(OutBuf, OutBytes);$
  [34mtry[39;49;00m$
    strm.next_in := InBuf;$
    strm.avail_in := InBytes;$
    strm.next_out := OutBuf;$
    strm.avail_out := OutBytes;$
    DCheck(inflateInit_(strm, zlib_version, [36msizeof[39;49;00m(strm)));$
    [34mtry[39;49;00m$
      [34mwhile[39;49;00m DCheck(inflate(strm, Z_FINISH)) <> Z_STREAM_END [34mdo[39;49;00m$
      [34mbegin[39;49;00m$
        P := OutBuf;$
        [36mInc[39;49;00m(OutBytes, BufInc);$
        [36mReallocMem[39;49;00m(OutBuf, OutBytes);$
        strm.next_out := [36mPChar[39;49;00m([36mInteger[39;49;00m(OutBuf) + ([36mInteger[39;49;00m(strm.next_out) - [36mInteger[39;49;00m(P)));$
        strm.avail_out := BufInc;$
      [34mend[39;49;00m;$
    [34mfinally[39;49;00m$
      DCheck(inflateEnd(strm));$
    [34mend[39;49;00m;$
    [36mReallocMem[39;49;00m(OutBuf, strm.total_out);$
    OutBytes := strm.total_out;$
  [34mexcept[39;49;00m$
    [36mFreeMem[39;49;00m(OutBuf);$
    [34mraise[39;49;00m$
  [34mend[39;49;00m;$
[34mend[39;49;00m;$
$
$
[37m// TCustomZlibStream[39;49;00m$
$
[34mconstructor[39;49;00m [04m[32mTCustomZLibStream[39;49;00m.[32mCreate[39;49;00m(Strm: TStream);$
[34mbegin[39;49;00m$
  [34minherited[39;49;00m Create;$
  FStrm := Strm;$
  FStrmPos := Strm.Position;$
[34mend[39;49;00m;$
$
[34mprocedure[39;49;00m [04m[32mTCustomZLibStream[39;49;00m.[32mProgress[39;49;00m(Sender: [36mTObject[39;49;00m);$
[34mbegin[39;49;00m$
  [34mif[39;49;00m [36mAssigned[39;49;00m(FOnProgress) [34mthen[39;49;00m FOnProgress(Sender);$
[34mend[39;49;00m;$
$
$
[37m// TCompressionStream[39;49;00m$
$
[34mconstructor[39;49;00m [04m[32mTCompressionStream[39;49;00m.[32mCreate[39;49;00m(CompressionLevel: TCompressionLevel;$
  Dest: TStream);$
[34mconst[39;49;00m$
  Levels: [34marray[39;49;00m [TCompressionLevel] [34mof[39;49;00m [36mShortInt[39;49;00m =$
    (Z_NO_COMPRESSION, Z_BEST_SPEED, Z_DEFAULT_COMPRESSION, Z_BEST_COMPRESSION);$
[34mbegin[39;49;00m$
  [34minherited[39;49;00m Create(Dest);$
  FZRec.next_out := FBuffer;$
  FZRec.avail_out := [36msizeof[39;49;00m(FBuffer);$
  CCheck(deflateInit_(FZRec, Levels[CompressionLevel], zlib_version, [36msizeof[39;49;00m(FZRec)));$
[34mend[39;49;00m;$
$
[34mdestructor[39;49;00m [04m[32mTCompressionStream[39;49;00m.[32mDestroy[39;49;00m;$
[34mbegin[39;49;00m$
  FZRec.next_in := [34mnil[39;49;00m;$
  FZRec.avail_in := [34m0[39;49;00m;$
  [34mtry[39;49;00m$
    [34mif[39;49;00m FStrm.Position <> FStrmPos [34mthen[39;49;00m FStrm.Position := FStrmPos;$
    [34mwhile[39;49;00m (CCheck(deflate(FZRec, Z_FINISH)) <> Z_STREAM_END)$
      [34mand[39;49;00m (FZRec.avail_out = [34m0[39;49;00m) [34mdo[39;49;00m$
    [34mbegin[39;49;00m$
      FStrm.WriteBuffer(FBuffer, [36msizeof[39;49;00m(FBuffer));$
      FZRec.next_out := FBuffer;$
      FZRec.avail_out := [36msizeof[39;49;00m(FBuffer);$
    [34mend[39;49;00m;$
    [34mif[39;49;00m FZRec.avail_out < [36msizeof[39;49;00m(FBuffer) [34mthen[39;49;00m$
      FStrm.WriteBuffer(FBuffer, [36msizeof[39;49;00m(FBuffer) - FZRec.avail_out);$
  [34mfinally[39;49;00m$
    deflateEnd(FZRec);$
  [34mend[39;49;00m;$
  [34minherited[39;49;00m Destroy;$
[34mend[39;49;00m;$
$
[34mfunction[39;49;00m [04m[32mTCompressionStream[39;49;00m.[32mRead[39;49;00m([34mvar[39;49;00m Buffer; Count: [36mLongint[39;49;00m): [36mLongint[39;49;00m;$
[34mbegin[39;49;00m$
  [34mraise[39;49;00m ECompressionError.Create([33m'[39;49;00m[33mInvalid stream operation[39;49;00m[33m'[39;49;00m);$
[34mend[39;49;00m;$
$
[34mfunction[39;49;00m [04m[32mTCompressionStream[39;49;00m.[32mWrite[39;49;00m([34mconst[39;49;00m Buffer; Count: [36mLongint[39;49;00m): [36mLongint[39;49;00m;$
[34mbegin[39;49;00m$
  FZRec.next_in := @Buffer;$
  FZRec.avail_in := Count;$
  [34mif[39;49;00m FStrm.Position <> FStrmPos [34mthen[39;49;00m FStrm.Position := FStrmPos;$
  [34mwhile[39;49;00m (FZRec.avail_in > [34m0[39;49;00m) [34mdo[39;49;00m$
  [34mbegin[39;49;00m$
    CCheck(deflate(FZRec, [34m0[39;49;00m));$
    [34mif[39;49;00m FZRec.avail_out = [34m0[39;49;00m [34mthen[39;49;00m$
    [34mbegin[39;49;00m$
      FStrm.WriteBuffer(FBuffer, [36msizeof[39;49;00m(FBuffer));$
      FZRec.next_out := FBuffer;$
      FZRec.avail_out := [36msizeof[39;49;00m(FBuffer);$
      FStrmPos := FStrm.Position;$
      Progress([34mSelf[39;49;00m);$
    [34mend[39;49;00m;$
  [34mend[39;49;00m;$
  [36mResult[39;49;00m := Count;$
[34mend[39;49;00m;$
$
[34mfunction[39;49;00m [04m[32mTCompressionStream[39;49;00m.[32mSeek[39;49;00m(Offset: [36mLongint[39;49;00m; Origin: [36mWord[39;49;00m): [36mLongint[39;49;00m;$
[34mbegin[39;49;00m$
  [34mif[39;49;00m (Offset = [34m0[39;49;00m) [34mand[39;49;00m (Origin = soFromCurrent) [34mthen[39;49;00m$
    [36mResult[39;49;00m := FZRec.total_in$
  [34melse[39;49;00m$
    [34mraise[39;49;00m ECompressionError.Create([33m'[39;49;00m[33mInvalid stream operation[39;49;00m[33m'[39;49;00m);$
[34mend[39;49;00m;$
$
[34mfunction[39;49;00m [04m[32mTCompressionStream[39;49;00m.[32mGetCompressionRate[39;49;00m: [36mSingle[39;49;00m;$
[34mbegin[39;49;00m$
  [34mif[39;49;00m FZRec.total_in = [34m0[39;49;00m [34mthen[39;49;00m$
    [36mResult[39;49;00m := [34m0[39;49;00m$
  [34melse[39;49;00m$
    [36mResult[39;49;00m := ([34m1.0[39;49;00m - (FZRec.total_out / FZRec.total_in)) * [34m10[39;49;00m[34m0.0[39;49;00m;$
[34mend[39;49;00m;$
$
$
[37m// TDecompressionStream[39;49;00m$
$
[34mconstructor[39;49;00m [04m[32mTDecompressionStream[39;49;00m.[32mCreate[39;49;00m(Source: TStream);$
[34mbegin[39;49;00m$
  [34minherited[39;49;00m Create(Source);$
  FZRec.next_in := FBuffer;$
  FZRec.avail_in := [34m0[39;49;00m;$
  DCheck(inflateInit_(FZRec, zlib_version, [36msizeof[39;49;00m(FZRec)));$
[34mend[39;49;00m;$
$
[34mdestructor[39;49;00m [04m[32mTDecompressionStream[39;49;00m.[32mDestroy[39;49;00m;$
[34mbegin[39;49;00m$
  inflateEnd(FZRec);$
  [34minherited[39;49;00m Destroy;$
[34mend[39;49;00m;$
$
[34mfunction[39;49;00m [04m[32mTDecompressionStream[39;49;00m.[32mRead[39;49;00m([34mvar[39;49;00m Buffer; Count: [36mLongint[39;49;00m): [36mLongint[39;49;00m;$
[34mbegin[39;49;00m$
  FZRec.next_out := @Buffer;$
  FZRec.avail_out := Count;$
  [34mif[39;49;00m FStrm.Position <> FStrmPos [34mthen[39;49;00m FStrm.Position := FStrmPos;$
  [34mwhile[39;49;00m (FZRec.avail_out > [34m0[39;49;00m) [34mdo[39;49;00m$
  [34mbegin[39;49;00m$
    [34mif[39;49;00m FZRec.avail_in = [34m0[39;49;00m [34mthen[39;49;00m$
    [34mbegin[39;49;00m$
      FZRec.avail_in := FStrm.Read(FBuffer, [36msizeof[39;49;00m(FBuffer));$
      [34mif[39;49;00m FZRec.avail_in = [34m0[39;49;00m [34mthen[39;49;00m$
        [34mbegin[39;49;00m$
          [36mResult[39;49;00m := Count - FZRec.avail_out;$
          [34mExit[39;49;00m;$
        [34mend[39;49;00m;$
      FZRec.next_in := FBuffer;$
      FStrmPos := FStrm.Position;$
      Progress([34mSelf[39;49;00m);$
    [34mend[39;49;00m;$
    DCheck(inflate(FZRec, [34m0[39;49;00m));$
  [34mend[39;49;00m;$
  [36mResult[39;49;00m := Count;$
[34mend[39;49;00m;$
$
[34mfunction[39;49;00m [04m[32mTDecompressionStream[39;49;00m.[32mWrite[39;49;00m([34mconst[39;49;00m Buffer; Count: [36mLongint[39;49;00m): [36mLongint[39;49;00m;$
[34mbegin[39;49;00m$
  [34mraise[39;49;00m EDecompressionError.Create([33m'[39;49;00m[33mInvalid stream operation[39;49;00m[33m'[39;49;00m);$
[34mend[39;49;00m;$
$
[34mfunction[39;49;00m [04m[32mTDecompressionStream[39;49;00m.[32mSeek[39;49;00m(Offset: [36mLongint[39;49;00m; Origin: [36mWord[39;49;00m): [36mLongint[39;49;00m;$
[34mvar[39;49;00m$
  I: [36mInteger[39;49;00m;$
  Buf: [34marray[39;49;00m [[34m0[39;49;00m..[34m4095[39;49;00m] [34mof[39;49;00m [36mChar[39;49;00m;$
[34mbegin[39;49;00m$
  [34mif[39;49;00m (Offset = [34m0[39;49;00m) [34mand[39;49;00m (Origin = soFromBeginning) [34mthen[39;49;00m$
  [34mbegin[39;49;00m$
    DCheck(inflateReset(FZRec));$
    FZRec.next_in := FBuffer;$
    FZRec.avail_in := [34m0[39;49;00m;$
    FStrm.Position := [34m0[39;49;00m;$
    FStrmPos := [34m0[39;49;00m;$
  [34mend[39;49;00m$
  [34melse[39;49;00m [34mif[39;49;00m ( (Offset >= [34m0[39;49;00m) [34mand[39;49;00m (Origin = soFromCurrent)) [34mor[39;49;00m$
          ( ((Offset - FZRec.total_out) > [34m0[39;49;00m) [34mand[39;49;00m (Origin = soFromBeginning)) [34mthen[39;49;00m$
  [34mbegin[39;49;00m$
    [34mif[39;49;00m Origin = soFromBeginning [34mthen[39;49;00m [36mDec[39;49;00m(Offset, FZRec.total_out);$
    [34mif[39;49;00m Offset > [34m0[39;49;00m [34mthen[39;49;00m$
    [34mbegin[39;49;00m$
      [34mfor[39;49;00m I := [34m1[39;49;00m [34mto[39;49;00m Offset [34mdiv[39;49;00m [36msizeof[39;49;00m(Buf) [34mdo[39;49;00m$
        ReadBuffer(Buf, [36msizeof[39;49;00m(Buf));$
      ReadBuffer(Buf, Offset [34mmod[39;49;00m [36msizeof[39;49;00m(Buf));$
    [34mend[39;49;00m;$
  [34mend[39;49;00m$
  [34melse[39;49;00m$
    [34mraise[39;49;00m EDecompressionError.Create([33m'[39;49;00m[33mInvalid stream operation[39;49;00m[33m'[39;49;00m);$
  [36mResult[39;49;00m := FZRec.total_out;$
[34mend[39;49;00m;$
$
[34mend[39;49;00m.$

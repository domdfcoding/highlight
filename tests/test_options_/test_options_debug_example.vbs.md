Using lexer <pygments.lexers.VBScriptLexer with {'ensurenl': False, 'tabsize': 0}>
[37mrem VBScript examples[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m' Various constants of different types[39;49;00m[37m[39;49;00m
[34mconst[39;49;00m[37m [39;49;00m[31msomeText[39;49;00m[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33msome [39;49;00m[33m"[39;49;00m[37m [39;49;00m&[37m [39;49;00m[33m"[39;49;00m[33m""[39;49;00m[33mtext[39;49;00m[33m""[39;49;00m[33m"[39;49;00m[37m[39;49;00m
[34mconst[39;49;00m[37m [39;49;00m[31msomeInt[39;49;00m[37m [39;49;00m=[37m [39;49;00m[34m123[39;49;00m[37m[39;49;00m
[34mconst[39;49;00m[37m [39;49;00m[31msomeHex[39;49;00m[37m [39;49;00m=[37m [39;49;00m[34m&h3110c0d3[39;49;00m[37m[39;49;00m
[34mconst[39;49;00m[37m [39;49;00m[31msomeFloat[39;49;00m[37m [39;49;00m=[37m [39;49;00m[34m123.45e-67[39;49;00m[37m[39;49;00m
[34mconst[39;49;00m[37m [39;49;00m[31msomeDate[39;49;00m[37m [39;49;00m=[37m [39;49;00m[33m#1/2/2016#[39;49;00m[37m[39;49;00m
[34mconst[39;49;00m[37m [39;49;00m[31msomeTime[39;49;00m[37m [39;49;00m=[37m [39;49;00m[33m#12:34:56 AM#[39;49;00m[37m[39;49;00m
[34mconst[39;49;00m[37m [39;49;00m[31msomeBool[39;49;00m[37m [39;49;00m=[37m [39;49;00m[31mvbTrue[39;49;00m[37m  [39;49;00m[37m' -1[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m' Do some math.[39;49;00m[37m[39;49;00m
radius[37m [39;49;00m=[37m [39;49;00m[34m1.e2[39;49;00m[37m[39;49;00m
area[37m [39;49;00m=[37m [39;49;00mradius[37m [39;49;00m^[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m*[37m [39;49;00m[34m3.1315[39;49;00m[37m[39;49;00m
a[37m [39;49;00m=[37m [39;49;00m[34m17[39;49;00m[37m [39;49;00m:[37m [39;49;00mb[37m [39;49;00m=[37m [39;49;00m[34m23[39;49;00m[37m[39;49;00m
c[37m [39;49;00m=[37m [39;49;00m[36msqr[39;49;00m(a[37m [39;49;00m^[34m2[39;49;00m[37m [39;49;00m+[37m [39;49;00mb[37m [39;49;00m^[37m [39;49;00m[34m2[39;49;00m)[37m[39;49;00m
[37m[39;49;00m
[37m' Write 10 files.[39;49;00m[37m[39;49;00m
[34mFor[39;49;00m[37m [39;49;00mi[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00mto[37m [39;49;00m[34m10[39;49;00m[37m[39;49;00m
[37m    [39;49;00mcreateFile([37m [39;49;00mi[37m [39;49;00m)[37m[39;49;00m
[34mNext[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[34mPublic[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m [39;49;00m[32mcreateFile[39;49;00m(a)[37m[39;49;00m
[37m    [39;49;00m[34mDim[39;49;00m[37m [39;49;00m[31mfso[39;49;00m,[37m [39;49;00m[31mTargetFile[39;49;00m[37m[39;49;00m
[37m    [39;49;00mTargetPath[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33mC:\some_[39;49;00m[33m"[39;49;00m[37m [39;49;00m&[37m [39;49;00ma[37m [39;49;00m&[37m [39;49;00m[33m"[39;49;00m[33m.tmp[39;49;00m[33m"[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[34mSet[39;49;00m[37m [39;49;00mfso[37m [39;49;00m=[37m [39;49;00m[36mCreateObject[39;49;00m([33m"[39;49;00m[33mScripting.FileSystemObject[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
[37m    [39;49;00m[34mSet[39;49;00m[37m [39;49;00mTargetFile[37m [39;49;00m=[37m [39;49;00mfso.CreateTextFile(TargetPath)[37m[39;49;00m
[37m    [39;49;00mTargetFile.WriteLine([33m"[39;49;00m[33mHello [39;49;00m[33m"[39;49;00m[37m [39;49;00m&[37m [39;49;00m[31mvbCrLf[39;49;00m[37m [39;49;00m&[37m [39;49;00m[33m"[39;49;00m[33mworld![39;49;00m[33m"[39;49;00m)[37m[39;49;00m
[37m    [39;49;00mTargetFile.Close[37m[39;49;00m
[34mEnd[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m' Define a class with a property.[39;49;00m[37m[39;49;00m
[34mClass[39;49;00m[37m [39;49;00m[04m[32mCustomer[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[34mPrivate[39;49;00m[37m [39;49;00mm_CustomerName[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[34mPrivate[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m [39;49;00m[32mClass_Initialize[39;49;00m[37m[39;49;00m
[37m        [39;49;00mm_CustomerName[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33m"[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[37m' CustomerName property.[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m [39;49;00m[34mGet[39;49;00m[37m [39;49;00mCustomerName[37m[39;49;00m
[37m        [39;49;00mCustomerName[37m [39;49;00m=[37m [39;49;00mm_CustomerName[37m[39;49;00m
[37m    [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m [39;49;00m[34mLet[39;49;00m[37m [39;49;00mCustomerName(custname)[37m[39;49;00m
[37m        [39;49;00mm_CustomerName[37m [39;49;00m=[37m [39;49;00mcustname[37m[39;49;00m
[37m    [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m[39;49;00m
[34mEnd[39;49;00m[37m [39;49;00m[34mClass[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m' Special constructs[39;49;00m[37m[39;49;00m
[34mOption[39;49;00m[37m [39;49;00m[34mExplicit[39;49;00m[37m[39;49;00m
[34mOn[39;49;00m[37m [39;49;00m[34mError[39;49;00m[37m [39;49;00m[34mResume[39;49;00m[37m [39;49;00m[34mNext[39;49;00m[37m[39;49;00m
[34mOn[39;49;00m[37m [39;49;00m[34mError[39;49;00m[37m [39;49;00m[34mGoto[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m' Comment without terminating CR/LF.[39;49;00m
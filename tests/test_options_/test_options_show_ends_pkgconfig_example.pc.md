[37m# This is for a fictional package `yet another portable hatchpotch generator'.[39;49;00m[37m[39;49;00m$
[36mprefix[39;49;00m=/usr/local/opt/site/private [37m# define variable `prefix`[39;49;00m[37m[39;49;00m$
[36mexec_prefix[39;49;00m=[33m${[39;49;00m[36mprefix[39;49;00m[33m}[39;49;00m[37m [39;49;00m[37m# using variable reference[39;49;00m[37m[39;49;00m$
[36mlibdir[39;49;00m=[33m${[39;49;00m[36mexec_prefix[39;49;00m[33m}[39;49;00m/lib[37m[39;49;00m$
[36mincludedir[39;49;00m=[33m${[39;49;00m[36mprefix[39;49;00m[33m}[39;49;00m/include[37m[39;49;00m$
[36mjust_for_test[39;49;00m=$${this is not a part of variable reference}[37m [39;49;00m[37m# escape with `$$`[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[94mName[39;49;00m:[37m [39;49;00mYAPHatchPotchGen[37m[39;49;00m$
[94mDescription[39;49;00m:[37m [39;49;00mYet[37m [39;49;00mAnother[37m [39;49;00mPortable[37m [39;49;00mHatchPotch[37m [39;49;00mGENerator.[37m[39;49;00m$
[94mVersion[39;49;00m:[37m [39;49;00m352.9.3[37m[39;49;00m$
[94mURL[39;49;00m:[37m [39;49;00mhttp://www9.yaphatchpotchgen.net[37m  [39;49;00m[37m# Don't access.[39;49;00m[37m[39;49;00m$
[94mRequires[39;49;00m:[37m [39;49;00mpiyohogelib-9.0[37m [39;49;00m=[37m [39;49;00m9.5.3[37m[39;49;00m$
[94mRequires.private[39;49;00m:[37m [39;49;00mnyorolib-3.0[37m [39;49;00m=[37m [39;49;00m3.0.9[37m[39;49;00m$
[94mConflicts[39;49;00m:[37m [39;49;00mapiyohoge[37m [39;49;00m<=[37m [39;49;00m8.3[37m[39;49;00m$
[94mLibs[39;49;00m:[37m [39;49;00m-L[33m${[39;49;00m[36mlibdir[39;49;00m[33m}[39;49;00m[37m [39;49;00m-lyaphatchpotchgen-352.9[37m [39;49;00m[37m# using variable reference[39;49;00m[37m[39;49;00m$
[94mLibs.private[39;49;00m:[37m [39;49;00m-ll[37m [39;49;00m-ly[37m[39;49;00m$
[94mCflags[39;49;00m:[37m [39;49;00m-I[33m${[39;49;00m[36mincludedir[39;49;00m[33m}[39;49;00m/piyohogelib-9.0[37m [39;49;00m-I[33m${[39;49;00m[36mlibdir[39;49;00m[33m}[39;49;00m/yaphatchpotchgen/include$

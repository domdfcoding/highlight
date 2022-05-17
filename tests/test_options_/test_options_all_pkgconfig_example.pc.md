     1^I[37m# This is for a fictional package `yet another portable hatchpotch generator'.[39;49;00m[37m[39;49;00m$
     2^I[36mprefix[39;49;00m=/usr/local/opt/site/private [37m# define variable `prefix`[39;49;00m[37m[39;49;00m$
     3^I[36mexec_prefix[39;49;00m=[33m${[39;49;00m[36mprefix[39;49;00m[33m}[39;49;00m[37m [39;49;00m[37m# using variable reference[39;49;00m[37m[39;49;00m$
     4^I[36mlibdir[39;49;00m=[33m${[39;49;00m[36mexec_prefix[39;49;00m[33m}[39;49;00m/lib[37m[39;49;00m$
     5^I[36mincludedir[39;49;00m=[33m${[39;49;00m[36mprefix[39;49;00m[33m}[39;49;00m/include[37m[39;49;00m$
     6^I[36mjust_for_test[39;49;00m=$${this is not a part of variable reference}[37m [39;49;00m[37m# escape with `$$`[39;49;00m[37m[39;49;00m$
     7^I[37m[39;49;00m$
     8^I[94mName[39;49;00m:[37m [39;49;00mYAPHatchPotchGen[37m[39;49;00m$
     9^I[94mDescription[39;49;00m:[37m [39;49;00mYet[37m [39;49;00mAnother[37m [39;49;00mPortable[37m [39;49;00mHatchPotch[37m [39;49;00mGENerator.[37m[39;49;00m$
    10^I[94mVersion[39;49;00m:[37m [39;49;00m352.9.3[37m[39;49;00m$
    11^I[94mURL[39;49;00m:[37m [39;49;00mhttp://www9.yaphatchpotchgen.net[37m  [39;49;00m[37m# Don't access.[39;49;00m[37m[39;49;00m$
    12^I[94mRequires[39;49;00m:[37m [39;49;00mpiyohogelib-9.0[37m [39;49;00m=[37m [39;49;00m9.5.3[37m[39;49;00m$
    13^I[94mRequires.private[39;49;00m:[37m [39;49;00mnyorolib-3.0[37m [39;49;00m=[37m [39;49;00m3.0.9[37m[39;49;00m$
    14^I[94mConflicts[39;49;00m:[37m [39;49;00mapiyohoge[37m [39;49;00m<=[37m [39;49;00m8.3[37m[39;49;00m$
    15^I[94mLibs[39;49;00m:[37m [39;49;00m-L[33m${[39;49;00m[36mlibdir[39;49;00m[33m}[39;49;00m[37m [39;49;00m-lyaphatchpotchgen-352.9[37m [39;49;00m[37m# using variable reference[39;49;00m[37m[39;49;00m$
    16^I[94mLibs.private[39;49;00m:[37m [39;49;00m-ll[37m [39;49;00m-ly[37m[39;49;00m$
    17^I[94mCflags[39;49;00m:[37m [39;49;00m-I[33m${[39;49;00m[36mincludedir[39;49;00m[33m}[39;49;00m/piyohogelib-9.0[37m [39;49;00m-I[33m${[39;49;00m[36mlibdir[39;49;00m[33m}[39;49;00m/yaphatchpotchgen/include$

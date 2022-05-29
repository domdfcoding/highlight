Using lexer <pygments.lexers.CMakeLexer with {'ensurenl': False, 'tabsize': 0}>
[36mCMAKE_MINIMUM_REQUIRED[39;49;00m([33mVERSION[39;49;00m[37m [39;49;00m[33m2.6[39;49;00m[37m [39;49;00m[33mFATAL_ERROR[39;49;00m)

[36mSET[39;49;00m([37m [39;49;00m[33mSOURCES[39;49;00m[37m [39;49;00m[33mback.c[39;49;00m[37m [39;49;00m[33mio.c[39;49;00m[37m [39;49;00m[33mmain.c[39;49;00m[37m [39;49;00m)
[36mSET[39;49;00m([37m [39;49;00m[33mPATH[39;49;00m[37m [39;49;00m$ENV{[31mPATH[39;49;00m}[37m [39;49;00m)
[36mMESSAGE[39;49;00m([37m [39;49;00m${[31mSOURCES[39;49;00m}[37m   [39;49;00m)[37m      [39;49;00m[37m# three arguments, prints "back.cio.cmain.c"[39;49;00m
[36mMESSAGE[39;49;00m([37m [39;49;00m[33m"${SOURCES}"[39;49;00m[37m [39;49;00m)[37m      [39;49;00m[37m# one argument,    prints "back.c;io.c;main.c"[39;49;00m
[36mMESSAGE[39;49;00m([37m [39;49;00m[33m""[39;49;00m[37m [39;49;00m)[37m                [39;49;00m[37m# one argument,    prints "" an empty line[39;49;00m
[36mMESSAGE[39;49;00m([37m [39;49;00m[33m"${EMPTY_STRING}"[39;49;00m[37m [39;49;00m)[37m [39;49;00m[37m# one argument,    prints "" an empty line[39;49;00m
[36mMESSAGE[39;49;00m([37m [39;49;00m${[31mEMPTY_STRING[39;49;00m}[37m [39;49;00m)[37m   [39;49;00m[37m# zero arguments,  causes CMake Error[39;49;00m
[37m                             [39;49;00m[37m# "MESSAGE called with incorrect number of arguments"[39;49;00m
[36mMESSAGE[39;49;00m([37m [39;49;00m[33m\\\"\[39;49;00m[37m [39;49;00m[33m\(\)\#\$\^[39;49;00m[37m [39;49;00m)[37m [39;49;00m[37m# this message contains literal characters[39;49;00m

[36mMESSAGE[39;49;00m([37m [39;49;00m[33m"This is practice."[39;49;00m[37m [39;49;00m)[37m  [39;49;00m[37m# prints "This is practice."[39;49;00m
[36mMESSAGE[39;49;00m([37m [39;49;00m[33m"This;is;practice."[39;49;00m[37m [39;49;00m)[37m  [39;49;00m[37m# prints "This;is;practice."[39;49;00m
[36mMESSAGE[39;49;00m([37m [39;49;00m[33m"Hi. ) MESSAGE( x )"[39;49;00m[37m [39;49;00m)[37m [39;49;00m[37m# prints "Hi. ) MESSAGE( x )"[39;49;00m

[36mMESSAGE[39;49;00m([37m [39;49;00m[33m"Welc"[39;49;00m[33mome[39;49;00m[37m [39;49;00m)[37m [39;49;00m[37m# rule 1[39;49;00m
[36mMESSAGE[39;49;00m([37m [39;49;00m[33mWelc[39;49;00m[33m"ome"[39;49;00m[37m [39;49;00m)[37m [39;49;00m[37m# rule 3[39;49;00m
[36mMESSAGE[39;49;00m([37m [39;49;00m[33mWelc[39;49;00m[33m"ome)"[39;49;00m[37m [39;49;00m)[37m [39;49;00m[37m# rule 2[39;49;00m
[36mMESSAGE[39;49;00m([37m [39;49;00m[33m""[39;49;00m[33mThanks[39;49;00m[37m [39;49;00m)[37m [39;49;00m[37m# rule 1[39;49;00m
[36mMESSAGE[39;49;00m([37m [39;49;00m[33mThanks[39;49;00m[33m""[39;49;00m[37m [39;49;00m)[37m [39;49;00m[37m# rule 3[39;49;00m

[36mSET[39;49;00m([37m [39;49;00m[33mx[39;49;00m[37m [39;49;00m[33my[39;49;00m[37m [39;49;00m[33mA[39;49;00m[37m [39;49;00m[33mB[39;49;00m[37m [39;49;00m[33mC[39;49;00m[37m [39;49;00m)[37m              [39;49;00m[37m# stores "y;A;B;C" in x (without quote)[39;49;00m
[36mSET[39;49;00m([37m [39;49;00m${[31mx[39;49;00m}[37m [39;49;00m)[37m                   [39;49;00m[37m# => SET( y;A;B;C ) => SET( y A B C)[39;49;00m
[36mMESSAGE[39;49;00m([37m [39;49;00m${[31my[39;49;00m}[37m [39;49;00m)[37m               [39;49;00m[37m# prints "ABC" to stdout (without quotes)[39;49;00m
[36mSET[39;49;00m([37m [39;49;00m[33my[39;49;00m[37m [39;49;00m[33mx[39;49;00m[37m [39;49;00m)[37m                    [39;49;00m[37m# stores "x" in y (without quotes)[39;49;00m
[36mSET[39;49;00m([37m [39;49;00m${[31my[39;49;00m}[37m [39;49;00m[33my[39;49;00m[37m [39;49;00m[33m=[39;49;00m[37m [39;49;00m[33mx[39;49;00m[37m [39;49;00m)[37m             [39;49;00m[37m# => SET( x y )[39;49;00m
[36mMESSAGE[39;49;00m([37m [39;49;00m[33m"\${x} = '${x}'"[39;49;00m[37m [39;49;00m)[37m   [39;49;00m[37m# prints "${x} = 'y;=;x'" to stdout (without quotes)[39;49;00m
[36mSET[39;49;00m([37m [39;49;00m[33my[39;49;00m[37m [39;49;00m${[31mx[39;49;00m}[37m [39;49;00m)[37m                 [39;49;00m[37m# => SET( y y = x ) => stores "y;=;x" in y (without quotes)[39;49;00m
[36mMESSAGE[39;49;00m([37m [39;49;00m${[31my[39;49;00m}[37m [39;49;00m)[37m               [39;49;00m[37m# prints "y=x" to stdout (without quotes)[39;49;00m

[36mSET[39;49;00m([37m [39;49;00m[33mx[39;49;00m[37m [39;49;00m[33ma[39;49;00m[37m [39;49;00m[33mb[39;49;00m[37m [39;49;00m[33mc[39;49;00m[37m   [39;49;00m)[37m [39;49;00m[37m# stores "a;b;c" in x      (without quotes)[39;49;00m
[36mSET[39;49;00m([37m [39;49;00m[33my[39;49;00m[37m [39;49;00m[33m"a b c"[39;49;00m[37m [39;49;00m)[37m [39;49;00m[37m# stores "a b c" in y      (without quotes)[39;49;00m
[36mMESSAGE[39;49;00m([37m [39;49;00m[33ma[39;49;00m[37m [39;49;00m[33mb[39;49;00m[37m [39;49;00m[33mc[39;49;00m[37m [39;49;00m)[37m [39;49;00m[37m# prints "abc"   to stdout (without quotes)[39;49;00m
[36mMESSAGE[39;49;00m([37m [39;49;00m${[31mx[39;49;00m}[37m [39;49;00m)[37m  [39;49;00m[37m# prints "abc"   to stdout (without quotes)[39;49;00m
[36mMESSAGE[39;49;00m([33m"${x}"[39;49;00m)[37m  [39;49;00m[37m# prints "a;b;c" to stdout (without quotes)[39;49;00m
[36mMESSAGE[39;49;00m([37m [39;49;00m${[31my[39;49;00m}[37m [39;49;00m)[37m  [39;49;00m[37m# prints "a b c" to stdout (without quotes)[39;49;00m
[36mMESSAGE[39;49;00m([33m"${y}"[39;49;00m)[37m  [39;49;00m[37m# prints "a b c" to stdout (without quotes)[39;49;00m

[37m# This is a comment.[39;49;00m
[36mCOMMAND[39;49;00m([37m [39;49;00m[33marguments[39;49;00m[37m [39;49;00m[33mgo[39;49;00m[37m [39;49;00m[33mhere[39;49;00m[37m [39;49;00m)
[36mANOTHER_COMMAND[39;49;00m()[37m [39;49;00m[37m# this command has no arguments[39;49;00m
[36mYET_ANOTHER_COMMAND[39;49;00m([37m [39;49;00m[33mthese[39;49;00m
[37m  [39;49;00m[33marguments[39;49;00m[37m [39;49;00m[33mare[39;49;00m[37m [39;49;00m[33mspread[39;49;00m[37m         [39;49;00m[37m# another comment[39;49;00m
[37m  [39;49;00m[33mover[39;49;00m[37m [39;49;00m[33mseveral[39;49;00m[37m [39;49;00m[33mlines[39;49;00m[37m [39;49;00m)
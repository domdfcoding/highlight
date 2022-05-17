Red/System [$
    [01m[35mTitle:[39;49;00m      [33m"[39;49;00m[33mRed/System example file[39;49;00m[33m"[39;49;00m$
    [01m[35mPurpose:[39;49;00m    [33m"[39;49;00m[33mJust some code for testing Pygments colorizer[39;49;00m[33m"[39;49;00m$
    [01m[35mLanguage:[39;49;00m   [90mhttp://www.red-lang.org/[39;49;00m$
]$
$
[34m#include[39;49;00m [90m%../common/FPU-configuration.reds[39;49;00m$
$
[37m; C types[39;49;00m$
$
[34m#define[39;49;00m [36mtime![39;49;00m                   [36mlong![39;49;00m$
[34m#define[39;49;00m [36mclock![39;49;00m                  [36mlong![39;49;00m$
$
[01m[35mdate!:[39;49;00m [36malias[39;49;00m [36mstruct![39;49;00m [$
    [31msecond[39;49;00m                      [[36minteger![39;49;00m]  [37m; 0-61 (60?)[39;49;00m$
    [31mminute[39;49;00m                      [[36minteger![39;49;00m]  [37m; 0-59[39;49;00m$
    [31mhour[39;49;00m                        [[36minteger![39;49;00m]  [37m; 0-23[39;49;00m$
$
    [31mday[39;49;00m                         [[36minteger![39;49;00m]  [37m; 1-31[39;49;00m$
    [31mmonth[39;49;00m                       [[36minteger![39;49;00m]  [37m; 0-11[39;49;00m$
    [31myear[39;49;00m                        [[36minteger![39;49;00m]  [37m; Since 1900[39;49;00m$
$
    [31mweekday[39;49;00m                     [[36minteger![39;49;00m]  [37m; 0-6 since Sunday[39;49;00m$
    [31myearday[39;49;00m                     [[36minteger![39;49;00m]  [37m; 0-365[39;49;00m$
    [31mdaylight-saving-time?[39;49;00m       [[36minteger![39;49;00m]  [37m; Negative: unknown[39;49;00m$
]$
$
[34m#either[39;49;00m [31mOS[39;49;00m = [31m'Windows[39;49;00m [$
    [34m#define[39;49;00m [31mclocks-per-second[39;49;00m   [34m1000[39;49;00m$
][$
    [37m; CLOCKS_PER_SEC value for Syllable, Linux (XSI-conformant systems)[39;49;00m$
    [37m; TODO: check for other systems[39;49;00m$
    [34m#define[39;49;00m [31mclocks-per-second[39;49;00m   [34m1000'000[39;49;00m$
] $
$
[34m#import[39;49;00m [[31mLIBC-file[39;49;00m [34mcdecl[39;49;00m [$
$
    [37m; Error handling[39;49;00m$
$
    [01m[35mform-error:[39;49;00m [33m"[39;49;00m[33mstrerror[39;49;00m[33m"[39;49;00m [  [37m; Return error description.[39;49;00m$
        [31mcode[39;49;00m            [[36minteger![39;49;00m]$
        [01m[35mreturn:[39;49;00m         [[36mc-string![39;49;00m]$
    ]$
    [01m[35mprint-error:[39;49;00m [33m"[39;49;00m[33mperror[39;49;00m[33m"[39;49;00m [  [37m; Print error to standard error output.[39;49;00m$
        [31mstring[39;49;00m          [[36mc-string![39;49;00m]$
    ]$
$
$
    [37m; Memory management[39;49;00m$
$
    [01m[35mmake:[39;49;00m [33m"[39;49;00m[33mcalloc[39;49;00m[33m"[39;49;00m [  [37m; Allocate zero-filled memory.[39;49;00m$
        [31mchunks[39;49;00m          [[36msize![39;49;00m]$
        [31msize[39;49;00m            [[36msize![39;49;00m]$
        [01m[35mreturn:[39;49;00m         [[36mbinary![39;49;00m]$
    ]$
    [01m[35mresize:[39;49;00m [33m"[39;49;00m[33mrealloc[39;49;00m[33m"[39;49;00m [  [37m; Resize memory allocation.[39;49;00m$
        [31mmemory[39;49;00m          [[36mbinary![39;49;00m]$
        [31msize[39;49;00m            [[36msize![39;49;00m]$
        [01m[35mreturn:[39;49;00m         [[36mbinary![39;49;00m]$
    ]$
 ]$
 $
 [01m[35mJVM!:[39;49;00m [36malias[39;49;00m [36mstruct![39;49;00m [$
    [31mreserved0[39;49;00m                   [[36mint-ptr![39;49;00m]$
    [31mreserved1[39;49;00m                   [[36mint-ptr![39;49;00m]$
    [31mreserved2[39;49;00m                   [[36mint-ptr![39;49;00m]$
    $
    [31mDestroyJavaVM[39;49;00m               [[36mfunction![39;49;00m [[[34mJNICALL[39;49;00m] [31mvm[39;49;00m [[36mJVM-ptr![39;49;00m] [01m[35mreturn:[39;49;00m [[36mjint![39;49;00m]]]$
    [31mAttachCurrentThread[39;49;00m         [[36mfunction![39;49;00m [[[34mJNICALL[39;49;00m] [31mvm[39;49;00m [[36mJVM-ptr![39;49;00m] [31mpenv[39;49;00m [[36mstruct![39;49;00m [[31mp[39;49;00m [[36mint-ptr![39;49;00m]]] [31margs[39;49;00m [[36mbyte-ptr![39;49;00m] [01m[35mreturn:[39;49;00m [[36mjint![39;49;00m]]]$
    [31mDetachCurrentThread[39;49;00m         [[36mfunction![39;49;00m [[[34mJNICALL[39;49;00m] [31mvm[39;49;00m [[36mJVM-ptr![39;49;00m] [01m[35mreturn:[39;49;00m [[36mjint![39;49;00m]]]$
    [31mGetEnv[39;49;00m                      [[36mfunction![39;49;00m [[[34mJNICALL[39;49;00m] [31mvm[39;49;00m [[36mJVM-ptr![39;49;00m] [31mpenv[39;49;00m [[36mstruct![39;49;00m [[31mp[39;49;00m [[36mint-ptr![39;49;00m]]] [31mversion[39;49;00m [[36minteger![39;49;00m] [01m[35mreturn:[39;49;00m [[36mjint![39;49;00m]]]$
    [31mAttachCurrentThreadAsDaemon[39;49;00m [[36mfunction![39;49;00m [[[34mJNICALL[39;49;00m] [31mvm[39;49;00m [[36mJVM-ptr![39;49;00m] [31mpenv[39;49;00m [[36mstruct![39;49;00m [[31mp[39;49;00m [[36mint-ptr![39;49;00m]]] [31margs[39;49;00m [[36mbyte-ptr![39;49;00m] [01m[35mreturn:[39;49;00m [[36mjint![39;49;00m]]]$
]$
$
 [37m;just some datatypes for testing:[39;49;00m$
 $
 #some-hash$
 [33m10-1-2013[39;49;00m$
 [36mquit[39;49;00m$
 $
 [37m;binary:[39;49;00m$
 [34m#{00FF0000}[39;49;00m$
 [34m#{00FF0000 FF000000}[39;49;00m$
 [34m#{00FF0000^IFF000000}[39;49;00m [37m;with tab instead of space[39;49;00m$
 [34m2#{[39;49;00m[34m00001111[39;49;00m[34m}[39;49;00m$
 [34m64#{/wAAAA==}[39;49;00m$
 [34m64#{/wAAA A==}[39;49;00m [37m;with space^I inside[39;49;00m$
 [34m64#{/wAAA^IA==}[39;49;00m [37m;with tab inside[39;49;00m$
 $
 $
 [37m;string with char[39;49;00m$
 [33m{[39;49;00m[33mbla [39;49;00m[33m^(ff)[39;49;00m[33m foo[39;49;00m[33m}[39;49;00m$
 [33m{[39;49;00m[33mbla [39;49;00m[33m^([39;49;00m[33m([39;49;00m[33m foo[39;49;00m[33m}[39;49;00m$
 [37m;some numbers:[39;49;00m$
 [34m12[39;49;00m$
 [34m1'000[39;49;00m$
 [34m1.2[39;49;00m$
 [34mFF00FF00[39;49;00m[31mh[39;49;00m[37m[39;49;00m$
 $
 [37m;some tests of hexa number notation with not common ending[39;49;00m$
 [[34mff00[39;49;00m[31mh[39;49;00m[37m [39;49;00m[34mff00[39;49;00m[31mh[39;49;00m] [34mff00[39;49;00m[31mh[39;49;00m[33m{[39;49;00m[33m}[39;49;00m [34mFF[39;49;00m[31mh[39;49;00m[33m"[39;49;00m[33mfoo[39;49;00m[33m"[39;49;00m [34m00[39;49;00m[31mh[39;49;00m([34m1[39;49;00m + [34m2[39;49;00m) ([34mAE[39;49;00m[31mh[39;49;00m)$
$
[37m;normal words:[39;49;00m$
[31mfoo[39;49;00m [31mchar[39;49;00m$
$
[37m;get-word[39;49;00m$
[01m[35m:foo[39;49;00m$
 $
[37m;lit-word:[39;49;00m$
[31m'foo[39;49;00m [31m'foo[39;49;00m$
$
[37m;multiple comment tests...[39;49;00m$
[34m1[39;49;00m + [34m1[39;49;00m$
[37mcomment "[39;49;00m[37maa[39;49;00m[37m"[39;49;00m^I^I^I^I^I^I^I^I$
[34m2[39;49;00m + [34m2[39;49;00m$
[37mcomment {[39;49;00m[37maa[39;49;00m[37m}[39;49;00m$
[34m3[39;49;00m + [34m3[39;49;00m$
[37mcomment {[39;49;00m[37ma[39;49;00m[37m^{[39;49;00m[37m}[39;49;00m$
[34m4[39;49;00m + [34m4[39;49;00m$
[37mcomment {[39;49;00m[37m{[39;49;00m[37m}[39;49;00m[37m}[39;49;00m$
[34m5[39;49;00m + [34m5[39;49;00m$
[37mcomment {[39;49;00m[37m[39;49;00m$
[37m^Ifoo: 6[39;49;00m$
[37m}[39;49;00m$
[34m6[39;49;00m + [34m6[39;49;00m$
[37mcomment [[39;49;00m[37mfoo: 6[39;49;00m[37m][39;49;00m$
[34m7[39;49;00m + [34m7[39;49;00m$
[37mcomment [[39;49;00m[37mfoo: [39;49;00m[37m"[39;49;00m[37m[[39;49;00m[37m"[39;49;00m[37m [39;49;00m[37m][39;49;00m$
[34m8[39;49;00m + [34m8[39;49;00m$
[37mcomment [[39;49;00m[37mfoo: [39;49;00m[37m{[39;49;00m[37m^{[39;49;00m[37m}[39;49;00m[37m [39;49;00m[37m][39;49;00m$
[34m9[39;49;00m + [34m9[39;49;00m$
[37mcomment [[39;49;00m[37mfoo: [39;49;00m[37m{[39;49;00m[37mboo[39;49;00m[37m}[39;49;00m[37m [39;49;00m[37m][39;49;00m$
[34m10[39;49;00m + [34m10[39;49;00m$
[37mcomment 5-May-2014/11:17:34+2:00[39;49;00m$
[34m11[39;49;00m + [34m11[39;49;00m$
$
$
[34mto-integer[39;49;00m [31mfoo[39;49;00m$
[31mfoo[39;49;00m[36m/[39;49;00m([31ma[39;49;00m + [34m1[39;49;00m)[36m/b[39;49;00m$
$
[36mcall[39;49;00m[36m/output[39;49;00m [31mreform[39;49;00m [[31m'which[39;49;00m [31minterpreter[39;49;00m] [01m[35mpath:[39;49;00m [32mcopy[39;49;00m [33m"[39;49;00m[33m"[39;49;00m$
$
 [01m[35mversion-1.1:[39;49;00m   [34m00010001[39;49;00m[31mh[39;49;00m[37m[39;49;00m$
 $
 [34m#if[39;49;00m [31mtype[39;49;00m = [31m'exe[39;49;00m [$
    [36mpush[39;49;00m [36msystem[39;49;00m[36m/stack[39;49;00m[36m/frame[39;49;00m                 [37m;-- save previous frame pointer[39;49;00m$
    [36msystem[39;49;00m[36m/stack[39;49;00m[36m/frame:[39;49;00m [36msystem[39;49;00m[36m/stack[39;49;00m[36m/top[39;49;00m    [37m;-- @@ reposition frame pointer just after the catch flag[39;49;00m$
]$
[36mpush[39;49;00m [31mCATCH_ALL[39;49;00m                              [37m;-- exceptions root barrier[39;49;00m$
[36mpush[39;49;00m [34m0[39;49;00m                                      [31m;--[39;49;00m [31mkeep[39;49;00m [31mstack[39;49;00m [31maligned[39;49;00m [36mon[39;49;00m [34m64[39;49;00m-bit$

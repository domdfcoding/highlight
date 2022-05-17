Red [$
    [01m[35mTitle:[39;49;00m  [33m"[39;49;00m[33mRed console[39;49;00m[33m"[39;49;00m$
    [01m[35mAuthor:[39;49;00m [[33m"[39;49;00m[33mNenad Rakocevic[39;49;00m[33m"[39;49;00m [33m"[39;49;00m[33mKaj de Vos[39;49;00m[33m"[39;49;00m]$
    [01m[35mFile:[39;49;00m   [90m%console.red[39;49;00m$
    [01m[35mTabs:[39;49;00m   [34m4[39;49;00m$
    [01m[35mRights:[39;49;00m [33m"[39;49;00m[33mCopyright [39;49;00m[33m([39;49;00m[33mC[39;49;00m[33m)[39;49;00m[33m 2012-2013 Nenad Rakocevic. All rights reserved.[39;49;00m[33m"[39;49;00m$
    [01m[35mLicense:[39;49;00m [33m{[39;49;00m[33m[39;49;00m$
[33m        Distributed under the Boost Software License, Version 1.0.[39;49;00m$
[33m        See https://github.com/dockimbel/Red/blob/master/BSL-License.txt[39;49;00m$
[33m    [39;49;00m[33m}[39;49;00m$
    [01m[35mPurpose:[39;49;00m    [33m"[39;49;00m[33mJust some code for testing Pygments colorizer[39;49;00m[33m"[39;49;00m$
    [01m[35mLanguage:[39;49;00m   [90mhttp://www.red-lang.org/[39;49;00m$
]$
$
[34m#system-global[39;49;00m [$
    [34m#either[39;49;00m [31mOS[39;49;00m = [31m'Windows[39;49;00m [$
        [34m#import[39;49;00m [$
            [33m"[39;49;00m[33mkernel32.dll[39;49;00m[33m"[39;49;00m [34mstdcall[39;49;00m [$
                [01m[35mAttachConsole:[39;49;00m   [33m"[39;49;00m[33mAttachConsole[39;49;00m[33m"[39;49;00m [$
                    [31mprocessID[39;49;00m       [[36minteger![39;49;00m]$
                    [01m[35mreturn:[39;49;00m         [[36minteger![39;49;00m]$
                ]$
                [01m[35mSetConsoleTitle:[39;49;00m [33m"[39;49;00m[33mSetConsoleTitleA[39;49;00m[33m"[39;49;00m [$
                    [31mtitle[39;49;00m           [[36mc-string![39;49;00m]$
                    [01m[35mreturn:[39;49;00m         [[36minteger![39;49;00m]$
                ]$
                [01m[35mReadConsole:[39;49;00m     [33m"[39;49;00m[33mReadConsoleA[39;49;00m[33m"[39;49;00m [$
                    [31mconsoleInput[39;49;00m    [[36minteger![39;49;00m]$
                    [31mbuffer[39;49;00m          [[36mbyte-ptr![39;49;00m]$
                    [31mcharsToRead[39;49;00m     [[36minteger![39;49;00m]$
                    [31mnumberOfChars[39;49;00m   [[36mint-ptr![39;49;00m]$
                    [31minputControl[39;49;00m    [[36mint-ptr![39;49;00m]$
                    [01m[35mreturn:[39;49;00m         [[36minteger![39;49;00m]$
                ]$
            ]$
        ]$
        [01m[35mline-buffer-size:[39;49;00m [34m16[39;49;00m * [34m1024[39;49;00m$
        [01m[35mline-buffer:[39;49;00m [31mallocate[39;49;00m [31mline-buffer-size[39;49;00m$
    ][$
        [34m#switch[39;49;00m [31mOS[39;49;00m [$
            [31mMacOSX[39;49;00m [$
                [34m#define[39;49;00m [31mReadLine-library[39;49;00m [33m"[39;49;00m[33mlibreadline.dylib[39;49;00m[33m"[39;49;00m$
            ]$
            [34m#default[39;49;00m [$
                [34m#define[39;49;00m [31mReadLine-library[39;49;00m [33m"[39;49;00m[33mlibreadline.so.6[39;49;00m[33m"[39;49;00m$
                [34m#define[39;49;00m [31mHistory-library[39;49;00m  [33m"[39;49;00m[33mlibhistory.so.6[39;49;00m[33m"[39;49;00m$
            ]$
        ]$
        [34m#import[39;49;00m [$
            [31mReadLine-library[39;49;00m [34mcdecl[39;49;00m [$
                [01m[35mread-line:[39;49;00m [33m"[39;49;00m[33mreadline[39;49;00m[33m"[39;49;00m [  [37m; Read a line from the console.[39;49;00m$
                    [31mprompt[39;49;00m          [[36mc-string![39;49;00m]$
                    [01m[35mreturn:[39;49;00m         [[36mc-string![39;49;00m]$
                ]$
                [01m[35mrl-bind-key:[39;49;00m [33m"[39;49;00m[33mrl_bind_key[39;49;00m[33m"[39;49;00m [$
                    [31mkey[39;49;00m             [[36minteger![39;49;00m]$
                    [31mcommand[39;49;00m         [[36minteger![39;49;00m]$
                    [01m[35mreturn:[39;49;00m         [[36minteger![39;49;00m]$
                ]$
                [01m[35mrl-insert:[39;49;00m   [33m"[39;49;00m[33mrl_insert[39;49;00m[33m"[39;49;00m [$
                    [31mcount[39;49;00m           [[36minteger![39;49;00m]$
                    [31mkey[39;49;00m             [[36minteger![39;49;00m]$
                    [01m[35mreturn:[39;49;00m         [[36minteger![39;49;00m]$
                ]$
            ]$
            [34m#if[39;49;00m [31mOS[39;49;00m <> [31m'MacOSX[39;49;00m [$
                [31mHistory-library[39;49;00m [34mcdecl[39;49;00m [$
                    [01m[35madd-history:[39;49;00m [33m"[39;49;00m[33madd_history[39;49;00m[33m"[39;49;00m [  [37m; Add line to the history.[39;49;00m$
                        [31mline[39;49;00m        [[36mc-string![39;49;00m]$
                    ]$
                ]$
            ]$
        ]$
$
        [01m[35mrl-insert-wrapper:[39;49;00m [36mfunc[39;49;00m [$
            [[34mcdecl[39;49;00m]$
            [31mcount[39;49;00m   [[36minteger![39;49;00m]$
            [31mkey[39;49;00m     [[36minteger![39;49;00m]$
            [01m[35mreturn:[39;49;00m [[36minteger![39;49;00m]$
        ][$
            [31mrl-insert[39;49;00m [31mcount[39;49;00m [31mkey[39;49;00m$
        ]$
        $
    ]$
]$
$
[01m[35mWindows?:[39;49;00m [36msystem[39;49;00m[36m/platform[39;49;00m = [31m'Windows[39;49;00m$
$
[01m[35mread-argument:[39;49;00m [36mroutine[39;49;00m [$
    [36m/local[39;49;00m$
        [31margs[39;49;00m [[36mstr-array![39;49;00m]$
        [31mstr[39;49;00m  [[36mred-string![39;49;00m]$
][$
    [36mif[39;49;00m [36msystem[39;49;00m[36m/args-count[39;49;00m <> [34m2[39;49;00m [$
        [31mSET_RETURN[39;49;00m(none-value)$
        [36mexit[39;49;00m$
    ]$
    [01m[35margs:[39;49;00m [36msystem[39;49;00m[36m/args-list[39;49;00m + [34m1[39;49;00m                          [37m;-- skip binary filename[39;49;00m$
    [01m[35mstr:[39;49;00m [31msimple-io[39;49;00m[36m/read-txt[39;49;00m [31margs[39;49;00m[36m/item[39;49;00m$
    [31mSET_RETURN[39;49;00m(str)$
]$
$
[01m[35minit-console:[39;49;00m [36mroutine[39;49;00m [$
    [31mstr[39;49;00m [[36mstring![39;49;00m]$
    [36m/local[39;49;00m$
        [31mret[39;49;00m$
][$
    [34m#either[39;49;00m [31mOS[39;49;00m = [31m'Windows[39;49;00m [$
        [37m;ret: AttachConsole -1[39;49;00m$
        [37m;if zero? ret [print-line "ReadConsole failed!" halt][39;49;00m$
        $
        [01m[35mret:[39;49;00m [31mSetConsoleTitle[39;49;00m [31mas[39;49;00m [36mc-string![39;49;00m [31mstring[39;49;00m[36m/rs-head[39;49;00m [31mstr[39;49;00m$
        [36mif[39;49;00m [34mzero?[39;49;00m [31mret[39;49;00m [[31mprint-line[39;49;00m [33m"[39;49;00m[33mSetConsoleTitle failed![39;49;00m[33m"[39;49;00m [36mhalt[39;49;00m]$
    ][$
        [31mrl-bind-key[39;49;00m [31mas-integer[39;49;00m [36mtab[39;49;00m [31mas-integer[39;49;00m [01m[35m:rl-insert-wrapper[39;49;00m$
    ]$
]$
$
[01m[35minput:[39;49;00m [36mroutine[39;49;00m [$
    [31mprompt[39;49;00m [[36mstring![39;49;00m]$
    [36m/local[39;49;00m$
        [31mlen[39;49;00m [31mret[39;49;00m [31mstr[39;49;00m [31mbuffer[39;49;00m [31mline[39;49;00m$
][$
    [34m#either[39;49;00m [31mOS[39;49;00m = [31m'Windows[39;49;00m [$
        [01m[35mlen:[39;49;00m [34m0[39;49;00m$
        [36mprint[39;49;00m [31mas[39;49;00m [36mc-string![39;49;00m [31mstring[39;49;00m[36m/rs-head[39;49;00m [31mprompt[39;49;00m$
        [01m[35mret:[39;49;00m [31mReadConsole[39;49;00m [31mstdin[39;49;00m [31mline-buffer[39;49;00m [31mline-buffer-size[39;49;00m [01m[35m:len[39;49;00m [36mnull[39;49;00m$
        [36mif[39;49;00m [34mzero?[39;49;00m [31mret[39;49;00m [[31mprint-line[39;49;00m [33m"[39;49;00m[33mReadConsole failed![39;49;00m[33m"[39;49;00m [36mhalt[39;49;00m]$
        [01m[35mlen:[39;49;00m [31mlen[39;49;00m + [34m1[39;49;00m$
        [31mline-buffer[39;49;00m[36m/len:[39;49;00m [36mnull-byte[39;49;00m$
        [01m[35mstr:[39;49;00m [31mstring[39;49;00m[36m/load[39;49;00m [31mas[39;49;00m [36mc-string![39;49;00m [31mline-buffer[39;49;00m [31mlen[39;49;00m$
    ][$
        [01m[35mline:[39;49;00m [31mread-line[39;49;00m [31mas[39;49;00m [36mc-string![39;49;00m [31mstring[39;49;00m[36m/rs-head[39;49;00m [31mprompt[39;49;00m$
        [36mif[39;49;00m [31mline[39;49;00m = [36mnull[39;49;00m [[36mhalt[39;49;00m]  [37m; EOF[39;49;00m$
$
         [34m#if[39;49;00m [31mOS[39;49;00m <> [31m'MacOSX[39;49;00m [[31madd-history[39;49;00m [31mline[39;49;00m]$
$
        [01m[35mstr:[39;49;00m [31mstring[39;49;00m[36m/load[39;49;00m [31mline[39;49;00m  [34m1[39;49;00m + [32mlength?[39;49;00m [31mline[39;49;00m$
[37m;       free as byte-ptr! line[39;49;00m$
    ]$
    [31mSET_RETURN[39;49;00m(str)$
]$
$
[01m[35mcount-delimiters:[39;49;00m [36mfunction[39;49;00m [$
    [31mbuffer[39;49;00m  [[36mstring![39;49;00m]$
    [01m[35mreturn:[39;49;00m [[36mblock![39;49;00m]$
][$
    [01m[35mlist:[39;49;00m [32mcopy[39;49;00m [[34m0[39;49;00m [34m0[39;49;00m]$
    [01m[35mc:[39;49;00m [36mnone[39;49;00m$
    $
    [36mforeach[39;49;00m [31mc[39;49;00m [31mbuffer[39;49;00m [$
        [36mcase[39;49;00m [$
            [31mescaped?[39;49;00m [$
                [01m[35mescaped?:[39;49;00m [36mno[39;49;00m$
            ]$
            [31min-comment?[39;49;00m [$
                [36mswitch[39;49;00m [31mc[39;49;00m [$
                    [33m#"[39;49;00m[33m^/"[39;49;00m [[01m[35min-comment?:[39;49;00m [36mno[39;49;00m]$
                ]$
            ]$
            [31m'else[39;49;00m [$
                [36mswitch[39;49;00m [31mc[39;49;00m [$
                    [33m#"[39;49;00m[33m^^"[39;49;00m [[01m[35mescaped?:[39;49;00m [36myes[39;49;00m]$
                    [33m#"[39;49;00m[33m;"[39;49;00m  [[36mif[39;49;00m [34mzero?[39;49;00m [31mlist[39;49;00m[36m/2[39;49;00m [[01m[35min-comment?:[39;49;00m [36myes[39;49;00m]]$
                    [33m#"[39;49;00m[33m["[39;49;00m  [[31mlist[39;49;00m[36m/1:[39;49;00m [31mlist[39;49;00m[36m/1[39;49;00m + [34m1[39;49;00m]$
                    [33m#"[39;49;00m[33m]"[39;49;00m  [[31mlist[39;49;00m[36m/1:[39;49;00m [31mlist[39;49;00m[36m/1[39;49;00m - [34m1[39;49;00m]$
                    [33m#"[39;49;00m[33m{"[39;49;00m  [[31mlist[39;49;00m[36m/2:[39;49;00m [31mlist[39;49;00m[36m/2[39;49;00m + [34m1[39;49;00m]$
                    [33m#"[39;49;00m[33m}"[39;49;00m  [[31mlist[39;49;00m[36m/2:[39;49;00m [31mlist[39;49;00m[36m/2[39;49;00m - [34m1[39;49;00m]$
                ]$
            ]$
        ]$
    ]$
    [31mlist[39;49;00m$
]$
$
[01m[35mdo-console:[39;49;00m [36mfunction[39;49;00m [][$
    [01m[35mbuffer:[39;49;00m [32mmake[39;49;00m [36mstring![39;49;00m [34m10000[39;49;00m$
    [01m[35mprompt:[39;49;00m [01m[35mred-prompt:[39;49;00m [33m"[39;49;00m[33mred>> [39;49;00m[33m"[39;49;00m$
    [01m[35mmode:[39;49;00m  [31m'mono[39;49;00m$
    $
    [01m[35mswitch-mode:[39;49;00m [$
        [01m[35mmode:[39;49;00m [36mcase[39;49;00m [$
            [31mcnt[39;49;00m[36m/1[39;49;00m [31m>[39;49;00m [34m0[39;49;00m [[31m'block[39;49;00m]$
            [31mcnt[39;49;00m[36m/2[39;49;00m [31m>[39;49;00m [34m0[39;49;00m [[31m'string[39;49;00m]$
            [31m'else[39;49;00m     [$
                [01m[35mprompt:[39;49;00m [31mred-prompt[39;49;00m$
                [36mdo[39;49;00m [31meval[39;49;00m$
                [31m'mono[39;49;00m$
            ]$
        ]$
        [01m[35mprompt:[39;49;00m [36mswitch[39;49;00m [31mmode[39;49;00m [$
            [31mblock[39;49;00m  [[33m"[39;49;00m[33m[[39;49;00m[33m^-[39;49;00m[33m"[39;49;00m]$
            [31mstring[39;49;00m [[33m"[39;49;00m[33m{[39;49;00m[33m^-[39;49;00m[33m"[39;49;00m]$
            [31mmono[39;49;00m   [[31mred-prompt[39;49;00m]$
        ]$
    ]$
    $
    [01m[35meval:[39;49;00m [$
        [01m[35mcode:[39;49;00m [36mload[39;49;00m[36m/all[39;49;00m [31mbuffer[39;49;00m$
        $
        [36munless[39;49;00m [32mtail?[39;49;00m [31mcode[39;49;00m [$
            [36mset[39;49;00m[36m/any[39;49;00m [31m'result[39;49;00m [36mdo[39;49;00m [31mcode[39;49;00m$
            $
            [36munless[39;49;00m [34munset?[39;49;00m [01m[35m:result[39;49;00m [$
                [36mif[39;49;00m [34m67[39;49;00m = [32mlength?[39;49;00m [01m[35mresult:[39;49;00m [32mmold[39;49;00m[36m/part[39;49;00m [01m[35m:result[39;49;00m [34m67[39;49;00m [  [37m;-- optimized for width = 72[39;49;00m$
                    [32mclear[39;49;00m [32mback[39;49;00m [32mtail[39;49;00m [31mresult[39;49;00m$
                    [32mappend[39;49;00m [31mresult[39;49;00m [33m"[39;49;00m[33m...[39;49;00m[33m"[39;49;00m$
                ]$
                [36mprint[39;49;00m [[33m"[39;49;00m[33m==[39;49;00m[33m"[39;49;00m [31mresult[39;49;00m]$
            ]$
        ]$
        [32mclear[39;49;00m [31mbuffer[39;49;00m$
    ]$
$
    [36mwhile[39;49;00m [[36mtrue[39;49;00m][$
        [36munless[39;49;00m [32mtail?[39;49;00m [01m[35mline:[39;49;00m [31minput[39;49;00m [31mprompt[39;49;00m [$
            [32mappend[39;49;00m [31mbuffer[39;49;00m [31mline[39;49;00m$
            [01m[35mcnt:[39;49;00m [31mcount-delimiters[39;49;00m [31mbuffer[39;49;00m$
$
            [36meither[39;49;00m [31mWindows?[39;49;00m [$
                [32mremove[39;49;00m [32mskip[39;49;00m [32mtail[39;49;00m [31mbuffer[39;49;00m [34m-2[39;49;00m          [37m;-- clear extra CR (Windows)[39;49;00m$
            ][$
                [32mappend[39;49;00m [31mbuffer[39;49;00m [36mlf[39;49;00m                    [37m;-- Unix[39;49;00m$
            ]$
            $
            [36mswitch[39;49;00m [31mmode[39;49;00m [$
                [31mblock[39;49;00m  [[36mif[39;49;00m [31mcnt[39;49;00m[36m/1[39;49;00m <= [34m0[39;49;00m [[36mdo[39;49;00m [31mswitch-mode[39;49;00m]]$
                [31mstring[39;49;00m [[36mif[39;49;00m [31mcnt[39;49;00m[36m/2[39;49;00m <= [34m0[39;49;00m [[36mdo[39;49;00m [31mswitch-mode[39;49;00m]]$
                [31mmono[39;49;00m   [[36mdo[39;49;00m [36meither[39;49;00m [36many[39;49;00m [[31mcnt[39;49;00m[36m/1[39;49;00m [31m>[39;49;00m [34m0[39;49;00m [31mcnt[39;49;00m[36m/2[39;49;00m [31m>[39;49;00m [34m0[39;49;00m][[31mswitch-mode[39;49;00m][[31meval[39;49;00m]]$
            ]$
        ]$
    ]$
]$
$
[01m[35mq:[39;49;00m [01m[35m:quit[39;49;00m$
$
[36mif[39;49;00m [01m[35mscript:[39;49;00m [31mread-argument[39;49;00m [$
    [01m[35mscript:[39;49;00m [36mload[39;49;00m [31mscript[39;49;00m$
    [36meither[39;49;00m [36many[39;49;00m [$
        [31mscript[39;49;00m[36m/1[39;49;00m <> [31m'Red[39;49;00m$
        [36mnot[39;49;00m [34mblock?[39;49;00m [31mscript[39;49;00m[36m/2[39;49;00m $
    ][$
        [36mprint[39;49;00m [33m"[39;49;00m[33m*** Error: not a Red program![39;49;00m[33m"[39;49;00m$
    ][$
        [36mdo[39;49;00m [32mskip[39;49;00m [31mscript[39;49;00m [34m2[39;49;00m$
    ]$
    [36mquit[39;49;00m$
]$
$
[31minit-console[39;49;00m [33m"[39;49;00m[33mRed Console[39;49;00m[33m"[39;49;00m$
$
[36mprint[39;49;00m [33m{[39;49;00m[33m[39;49;00m$
[33m-=== Red Console alpha version ===-[39;49;00m$
[33m([39;49;00m[33monly ASCII input supported[39;49;00m[33m)[39;49;00m[33m[39;49;00m$
[33m}[39;49;00m$
$
do-console$

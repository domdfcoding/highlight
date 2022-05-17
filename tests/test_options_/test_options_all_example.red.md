     1^IRed [$
     2^I    [01m[35mTitle:[39;49;00m  [33m"[39;49;00m[33mRed console[39;49;00m[33m"[39;49;00m$
     3^I    [01m[35mAuthor:[39;49;00m [[33m"[39;49;00m[33mNenad Rakocevic[39;49;00m[33m"[39;49;00m [33m"[39;49;00m[33mKaj de Vos[39;49;00m[33m"[39;49;00m]$
     4^I    [01m[35mFile:[39;49;00m   [90m%console.red[39;49;00m$
     5^I    [01m[35mTabs:[39;49;00m   [34m4[39;49;00m$
     6^I    [01m[35mRights:[39;49;00m [33m"[39;49;00m[33mCopyright [39;49;00m[33m([39;49;00m[33mC[39;49;00m[33m)[39;49;00m[33m 2012-2013 Nenad Rakocevic. All rights reserved.[39;49;00m[33m"[39;49;00m$
     7^I    [01m[35mLicense:[39;49;00m [33m{[39;49;00m[33m[39;49;00m$
     8^I[33m        Distributed under the Boost Software License, Version 1.0.[39;49;00m$
     9^I[33m        See https://github.com/dockimbel/Red/blob/master/BSL-License.txt[39;49;00m$
    10^I[33m    [39;49;00m[33m}[39;49;00m$
    11^I    [01m[35mPurpose:[39;49;00m    [33m"[39;49;00m[33mJust some code for testing Pygments colorizer[39;49;00m[33m"[39;49;00m$
    12^I    [01m[35mLanguage:[39;49;00m   [90mhttp://www.red-lang.org/[39;49;00m$
    13^I]$
    14^I$
    15^I[34m#system-global[39;49;00m [$
    16^I    [34m#either[39;49;00m [31mOS[39;49;00m = [31m'Windows[39;49;00m [$
    17^I        [34m#import[39;49;00m [$
    18^I            [33m"[39;49;00m[33mkernel32.dll[39;49;00m[33m"[39;49;00m [34mstdcall[39;49;00m [$
    19^I                [01m[35mAttachConsole:[39;49;00m   [33m"[39;49;00m[33mAttachConsole[39;49;00m[33m"[39;49;00m [$
    20^I                    [31mprocessID[39;49;00m       [[36minteger![39;49;00m]$
    21^I                    [01m[35mreturn:[39;49;00m         [[36minteger![39;49;00m]$
    22^I                ]$
    23^I                [01m[35mSetConsoleTitle:[39;49;00m [33m"[39;49;00m[33mSetConsoleTitleA[39;49;00m[33m"[39;49;00m [$
    24^I                    [31mtitle[39;49;00m           [[36mc-string![39;49;00m]$
    25^I                    [01m[35mreturn:[39;49;00m         [[36minteger![39;49;00m]$
    26^I                ]$
    27^I                [01m[35mReadConsole:[39;49;00m     [33m"[39;49;00m[33mReadConsoleA[39;49;00m[33m"[39;49;00m [$
    28^I                    [31mconsoleInput[39;49;00m    [[36minteger![39;49;00m]$
    29^I                    [31mbuffer[39;49;00m          [[36mbyte-ptr![39;49;00m]$
    30^I                    [31mcharsToRead[39;49;00m     [[36minteger![39;49;00m]$
    31^I                    [31mnumberOfChars[39;49;00m   [[36mint-ptr![39;49;00m]$
    32^I                    [31minputControl[39;49;00m    [[36mint-ptr![39;49;00m]$
    33^I                    [01m[35mreturn:[39;49;00m         [[36minteger![39;49;00m]$
    34^I                ]$
    35^I            ]$
    36^I        ]$
    37^I        [01m[35mline-buffer-size:[39;49;00m [34m16[39;49;00m * [34m1024[39;49;00m$
    38^I        [01m[35mline-buffer:[39;49;00m [31mallocate[39;49;00m [31mline-buffer-size[39;49;00m$
    39^I    ][$
    40^I        [34m#switch[39;49;00m [31mOS[39;49;00m [$
    41^I            [31mMacOSX[39;49;00m [$
    42^I                [34m#define[39;49;00m [31mReadLine-library[39;49;00m [33m"[39;49;00m[33mlibreadline.dylib[39;49;00m[33m"[39;49;00m$
    43^I            ]$
    44^I            [34m#default[39;49;00m [$
    45^I                [34m#define[39;49;00m [31mReadLine-library[39;49;00m [33m"[39;49;00m[33mlibreadline.so.6[39;49;00m[33m"[39;49;00m$
    46^I                [34m#define[39;49;00m [31mHistory-library[39;49;00m  [33m"[39;49;00m[33mlibhistory.so.6[39;49;00m[33m"[39;49;00m$
    47^I            ]$
    48^I        ]$
    49^I        [34m#import[39;49;00m [$
    50^I            [31mReadLine-library[39;49;00m [34mcdecl[39;49;00m [$
    51^I                [01m[35mread-line:[39;49;00m [33m"[39;49;00m[33mreadline[39;49;00m[33m"[39;49;00m [  [37m; Read a line from the console.[39;49;00m$
    52^I                    [31mprompt[39;49;00m          [[36mc-string![39;49;00m]$
    53^I                    [01m[35mreturn:[39;49;00m         [[36mc-string![39;49;00m]$
    54^I                ]$
    55^I                [01m[35mrl-bind-key:[39;49;00m [33m"[39;49;00m[33mrl_bind_key[39;49;00m[33m"[39;49;00m [$
    56^I                    [31mkey[39;49;00m             [[36minteger![39;49;00m]$
    57^I                    [31mcommand[39;49;00m         [[36minteger![39;49;00m]$
    58^I                    [01m[35mreturn:[39;49;00m         [[36minteger![39;49;00m]$
    59^I                ]$
    60^I                [01m[35mrl-insert:[39;49;00m   [33m"[39;49;00m[33mrl_insert[39;49;00m[33m"[39;49;00m [$
    61^I                    [31mcount[39;49;00m           [[36minteger![39;49;00m]$
    62^I                    [31mkey[39;49;00m             [[36minteger![39;49;00m]$
    63^I                    [01m[35mreturn:[39;49;00m         [[36minteger![39;49;00m]$
    64^I                ]$
    65^I            ]$
    66^I            [34m#if[39;49;00m [31mOS[39;49;00m <> [31m'MacOSX[39;49;00m [$
    67^I                [31mHistory-library[39;49;00m [34mcdecl[39;49;00m [$
    68^I                    [01m[35madd-history:[39;49;00m [33m"[39;49;00m[33madd_history[39;49;00m[33m"[39;49;00m [  [37m; Add line to the history.[39;49;00m$
    69^I                        [31mline[39;49;00m        [[36mc-string![39;49;00m]$
    70^I                    ]$
    71^I                ]$
    72^I            ]$
    73^I        ]$
    74^I$
    75^I        [01m[35mrl-insert-wrapper:[39;49;00m [36mfunc[39;49;00m [$
    76^I            [[34mcdecl[39;49;00m]$
    77^I            [31mcount[39;49;00m   [[36minteger![39;49;00m]$
    78^I            [31mkey[39;49;00m     [[36minteger![39;49;00m]$
    79^I            [01m[35mreturn:[39;49;00m [[36minteger![39;49;00m]$
    80^I        ][$
    81^I            [31mrl-insert[39;49;00m [31mcount[39;49;00m [31mkey[39;49;00m$
    82^I        ]$
    83^I        $
    84^I    ]$
    85^I]$
    86^I$
    87^I[01m[35mWindows?:[39;49;00m [36msystem[39;49;00m[36m/platform[39;49;00m = [31m'Windows[39;49;00m$
    88^I$
    89^I[01m[35mread-argument:[39;49;00m [36mroutine[39;49;00m [$
    90^I    [36m/local[39;49;00m$
    91^I        [31margs[39;49;00m [[36mstr-array![39;49;00m]$
    92^I        [31mstr[39;49;00m  [[36mred-string![39;49;00m]$
    93^I][$
    94^I    [36mif[39;49;00m [36msystem[39;49;00m[36m/args-count[39;49;00m <> [34m2[39;49;00m [$
    95^I        [31mSET_RETURN[39;49;00m(none-value)$
    96^I        [36mexit[39;49;00m$
    97^I    ]$
    98^I    [01m[35margs:[39;49;00m [36msystem[39;49;00m[36m/args-list[39;49;00m + [34m1[39;49;00m                          [37m;-- skip binary filename[39;49;00m$
    99^I    [01m[35mstr:[39;49;00m [31msimple-io[39;49;00m[36m/read-txt[39;49;00m [31margs[39;49;00m[36m/item[39;49;00m$
   100^I    [31mSET_RETURN[39;49;00m(str)$
   101^I]$
   102^I$
   103^I[01m[35minit-console:[39;49;00m [36mroutine[39;49;00m [$
   104^I    [31mstr[39;49;00m [[36mstring![39;49;00m]$
   105^I    [36m/local[39;49;00m$
   106^I        [31mret[39;49;00m$
   107^I][$
   108^I    [34m#either[39;49;00m [31mOS[39;49;00m = [31m'Windows[39;49;00m [$
   109^I        [37m;ret: AttachConsole -1[39;49;00m$
   110^I        [37m;if zero? ret [print-line "ReadConsole failed!" halt][39;49;00m$
   111^I        $
   112^I        [01m[35mret:[39;49;00m [31mSetConsoleTitle[39;49;00m [31mas[39;49;00m [36mc-string![39;49;00m [31mstring[39;49;00m[36m/rs-head[39;49;00m [31mstr[39;49;00m$
   113^I        [36mif[39;49;00m [34mzero?[39;49;00m [31mret[39;49;00m [[31mprint-line[39;49;00m [33m"[39;49;00m[33mSetConsoleTitle failed![39;49;00m[33m"[39;49;00m [36mhalt[39;49;00m]$
   114^I    ][$
   115^I        [31mrl-bind-key[39;49;00m [31mas-integer[39;49;00m [36mtab[39;49;00m [31mas-integer[39;49;00m [01m[35m:rl-insert-wrapper[39;49;00m$
   116^I    ]$
   117^I]$
   118^I$
   119^I[01m[35minput:[39;49;00m [36mroutine[39;49;00m [$
   120^I    [31mprompt[39;49;00m [[36mstring![39;49;00m]$
   121^I    [36m/local[39;49;00m$
   122^I        [31mlen[39;49;00m [31mret[39;49;00m [31mstr[39;49;00m [31mbuffer[39;49;00m [31mline[39;49;00m$
   123^I][$
   124^I    [34m#either[39;49;00m [31mOS[39;49;00m = [31m'Windows[39;49;00m [$
   125^I        [01m[35mlen:[39;49;00m [34m0[39;49;00m$
   126^I        [36mprint[39;49;00m [31mas[39;49;00m [36mc-string![39;49;00m [31mstring[39;49;00m[36m/rs-head[39;49;00m [31mprompt[39;49;00m$
   127^I        [01m[35mret:[39;49;00m [31mReadConsole[39;49;00m [31mstdin[39;49;00m [31mline-buffer[39;49;00m [31mline-buffer-size[39;49;00m [01m[35m:len[39;49;00m [36mnull[39;49;00m$
   128^I        [36mif[39;49;00m [34mzero?[39;49;00m [31mret[39;49;00m [[31mprint-line[39;49;00m [33m"[39;49;00m[33mReadConsole failed![39;49;00m[33m"[39;49;00m [36mhalt[39;49;00m]$
   129^I        [01m[35mlen:[39;49;00m [31mlen[39;49;00m + [34m1[39;49;00m$
   130^I        [31mline-buffer[39;49;00m[36m/len:[39;49;00m [36mnull-byte[39;49;00m$
   131^I        [01m[35mstr:[39;49;00m [31mstring[39;49;00m[36m/load[39;49;00m [31mas[39;49;00m [36mc-string![39;49;00m [31mline-buffer[39;49;00m [31mlen[39;49;00m$
   132^I    ][$
   133^I        [01m[35mline:[39;49;00m [31mread-line[39;49;00m [31mas[39;49;00m [36mc-string![39;49;00m [31mstring[39;49;00m[36m/rs-head[39;49;00m [31mprompt[39;49;00m$
   134^I        [36mif[39;49;00m [31mline[39;49;00m = [36mnull[39;49;00m [[36mhalt[39;49;00m]  [37m; EOF[39;49;00m$
   135^I$
   136^I         [34m#if[39;49;00m [31mOS[39;49;00m <> [31m'MacOSX[39;49;00m [[31madd-history[39;49;00m [31mline[39;49;00m]$
   137^I$
   138^I        [01m[35mstr:[39;49;00m [31mstring[39;49;00m[36m/load[39;49;00m [31mline[39;49;00m  [34m1[39;49;00m + [32mlength?[39;49;00m [31mline[39;49;00m$
   139^I[37m;       free as byte-ptr! line[39;49;00m$
   140^I    ]$
   141^I    [31mSET_RETURN[39;49;00m(str)$
   142^I]$
   143^I$
   144^I[01m[35mcount-delimiters:[39;49;00m [36mfunction[39;49;00m [$
   145^I    [31mbuffer[39;49;00m  [[36mstring![39;49;00m]$
   146^I    [01m[35mreturn:[39;49;00m [[36mblock![39;49;00m]$
   147^I][$
   148^I    [01m[35mlist:[39;49;00m [32mcopy[39;49;00m [[34m0[39;49;00m [34m0[39;49;00m]$
   149^I    [01m[35mc:[39;49;00m [36mnone[39;49;00m$
   150^I    $
   151^I    [36mforeach[39;49;00m [31mc[39;49;00m [31mbuffer[39;49;00m [$
   152^I        [36mcase[39;49;00m [$
   153^I            [31mescaped?[39;49;00m [$
   154^I                [01m[35mescaped?:[39;49;00m [36mno[39;49;00m$
   155^I            ]$
   156^I            [31min-comment?[39;49;00m [$
   157^I                [36mswitch[39;49;00m [31mc[39;49;00m [$
   158^I                    [33m#"[39;49;00m[33m^/"[39;49;00m [[01m[35min-comment?:[39;49;00m [36mno[39;49;00m]$
   159^I                ]$
   160^I            ]$
   161^I            [31m'else[39;49;00m [$
   162^I                [36mswitch[39;49;00m [31mc[39;49;00m [$
   163^I                    [33m#"[39;49;00m[33m^^"[39;49;00m [[01m[35mescaped?:[39;49;00m [36myes[39;49;00m]$
   164^I                    [33m#"[39;49;00m[33m;"[39;49;00m  [[36mif[39;49;00m [34mzero?[39;49;00m [31mlist[39;49;00m[36m/2[39;49;00m [[01m[35min-comment?:[39;49;00m [36myes[39;49;00m]]$
   165^I                    [33m#"[39;49;00m[33m["[39;49;00m  [[31mlist[39;49;00m[36m/1:[39;49;00m [31mlist[39;49;00m[36m/1[39;49;00m + [34m1[39;49;00m]$
   166^I                    [33m#"[39;49;00m[33m]"[39;49;00m  [[31mlist[39;49;00m[36m/1:[39;49;00m [31mlist[39;49;00m[36m/1[39;49;00m - [34m1[39;49;00m]$
   167^I                    [33m#"[39;49;00m[33m{"[39;49;00m  [[31mlist[39;49;00m[36m/2:[39;49;00m [31mlist[39;49;00m[36m/2[39;49;00m + [34m1[39;49;00m]$
   168^I                    [33m#"[39;49;00m[33m}"[39;49;00m  [[31mlist[39;49;00m[36m/2:[39;49;00m [31mlist[39;49;00m[36m/2[39;49;00m - [34m1[39;49;00m]$
   169^I                ]$
   170^I            ]$
   171^I        ]$
   172^I    ]$
   173^I    [31mlist[39;49;00m$
   174^I]$
   175^I$
   176^I[01m[35mdo-console:[39;49;00m [36mfunction[39;49;00m [][$
   177^I    [01m[35mbuffer:[39;49;00m [32mmake[39;49;00m [36mstring![39;49;00m [34m10000[39;49;00m$
   178^I    [01m[35mprompt:[39;49;00m [01m[35mred-prompt:[39;49;00m [33m"[39;49;00m[33mred>> [39;49;00m[33m"[39;49;00m$
   179^I    [01m[35mmode:[39;49;00m  [31m'mono[39;49;00m$
   180^I    $
   181^I    [01m[35mswitch-mode:[39;49;00m [$
   182^I        [01m[35mmode:[39;49;00m [36mcase[39;49;00m [$
   183^I            [31mcnt[39;49;00m[36m/1[39;49;00m [31m>[39;49;00m [34m0[39;49;00m [[31m'block[39;49;00m]$
   184^I            [31mcnt[39;49;00m[36m/2[39;49;00m [31m>[39;49;00m [34m0[39;49;00m [[31m'string[39;49;00m]$
   185^I            [31m'else[39;49;00m     [$
   186^I                [01m[35mprompt:[39;49;00m [31mred-prompt[39;49;00m$
   187^I                [36mdo[39;49;00m [31meval[39;49;00m$
   188^I                [31m'mono[39;49;00m$
   189^I            ]$
   190^I        ]$
   191^I        [01m[35mprompt:[39;49;00m [36mswitch[39;49;00m [31mmode[39;49;00m [$
   192^I            [31mblock[39;49;00m  [[33m"[39;49;00m[33m[[39;49;00m[33m^-[39;49;00m[33m"[39;49;00m]$
   193^I            [31mstring[39;49;00m [[33m"[39;49;00m[33m{[39;49;00m[33m^-[39;49;00m[33m"[39;49;00m]$
   194^I            [31mmono[39;49;00m   [[31mred-prompt[39;49;00m]$
   195^I        ]$
   196^I    ]$
   197^I    $
   198^I    [01m[35meval:[39;49;00m [$
   199^I        [01m[35mcode:[39;49;00m [36mload[39;49;00m[36m/all[39;49;00m [31mbuffer[39;49;00m$
   200^I        $
   201^I        [36munless[39;49;00m [32mtail?[39;49;00m [31mcode[39;49;00m [$
   202^I            [36mset[39;49;00m[36m/any[39;49;00m [31m'result[39;49;00m [36mdo[39;49;00m [31mcode[39;49;00m$
   203^I            $
   204^I            [36munless[39;49;00m [34munset?[39;49;00m [01m[35m:result[39;49;00m [$
   205^I                [36mif[39;49;00m [34m67[39;49;00m = [32mlength?[39;49;00m [01m[35mresult:[39;49;00m [32mmold[39;49;00m[36m/part[39;49;00m [01m[35m:result[39;49;00m [34m67[39;49;00m [  [37m;-- optimized for width = 72[39;49;00m$
   206^I                    [32mclear[39;49;00m [32mback[39;49;00m [32mtail[39;49;00m [31mresult[39;49;00m$
   207^I                    [32mappend[39;49;00m [31mresult[39;49;00m [33m"[39;49;00m[33m...[39;49;00m[33m"[39;49;00m$
   208^I                ]$
   209^I                [36mprint[39;49;00m [[33m"[39;49;00m[33m==[39;49;00m[33m"[39;49;00m [31mresult[39;49;00m]$
   210^I            ]$
   211^I        ]$
   212^I        [32mclear[39;49;00m [31mbuffer[39;49;00m$
   213^I    ]$
   214^I$
   215^I    [36mwhile[39;49;00m [[36mtrue[39;49;00m][$
   216^I        [36munless[39;49;00m [32mtail?[39;49;00m [01m[35mline:[39;49;00m [31minput[39;49;00m [31mprompt[39;49;00m [$
   217^I            [32mappend[39;49;00m [31mbuffer[39;49;00m [31mline[39;49;00m$
   218^I            [01m[35mcnt:[39;49;00m [31mcount-delimiters[39;49;00m [31mbuffer[39;49;00m$
   219^I$
   220^I            [36meither[39;49;00m [31mWindows?[39;49;00m [$
   221^I                [32mremove[39;49;00m [32mskip[39;49;00m [32mtail[39;49;00m [31mbuffer[39;49;00m [34m-2[39;49;00m          [37m;-- clear extra CR (Windows)[39;49;00m$
   222^I            ][$
   223^I                [32mappend[39;49;00m [31mbuffer[39;49;00m [36mlf[39;49;00m                    [37m;-- Unix[39;49;00m$
   224^I            ]$
   225^I            $
   226^I            [36mswitch[39;49;00m [31mmode[39;49;00m [$
   227^I                [31mblock[39;49;00m  [[36mif[39;49;00m [31mcnt[39;49;00m[36m/1[39;49;00m <= [34m0[39;49;00m [[36mdo[39;49;00m [31mswitch-mode[39;49;00m]]$
   228^I                [31mstring[39;49;00m [[36mif[39;49;00m [31mcnt[39;49;00m[36m/2[39;49;00m <= [34m0[39;49;00m [[36mdo[39;49;00m [31mswitch-mode[39;49;00m]]$
   229^I                [31mmono[39;49;00m   [[36mdo[39;49;00m [36meither[39;49;00m [36many[39;49;00m [[31mcnt[39;49;00m[36m/1[39;49;00m [31m>[39;49;00m [34m0[39;49;00m [31mcnt[39;49;00m[36m/2[39;49;00m [31m>[39;49;00m [34m0[39;49;00m][[31mswitch-mode[39;49;00m][[31meval[39;49;00m]]$
   230^I            ]$
   231^I        ]$
   232^I    ]$
   233^I]$
   234^I$
   235^I[01m[35mq:[39;49;00m [01m[35m:quit[39;49;00m$
   236^I$
   237^I[36mif[39;49;00m [01m[35mscript:[39;49;00m [31mread-argument[39;49;00m [$
   238^I    [01m[35mscript:[39;49;00m [36mload[39;49;00m [31mscript[39;49;00m$
   239^I    [36meither[39;49;00m [36many[39;49;00m [$
   240^I        [31mscript[39;49;00m[36m/1[39;49;00m <> [31m'Red[39;49;00m$
   241^I        [36mnot[39;49;00m [34mblock?[39;49;00m [31mscript[39;49;00m[36m/2[39;49;00m $
   242^I    ][$
   243^I        [36mprint[39;49;00m [33m"[39;49;00m[33m*** Error: not a Red program![39;49;00m[33m"[39;49;00m$
   244^I    ][$
   245^I        [36mdo[39;49;00m [32mskip[39;49;00m [31mscript[39;49;00m [34m2[39;49;00m$
   246^I    ]$
   247^I    [36mquit[39;49;00m$
   248^I]$
   249^I$
   250^I[31minit-console[39;49;00m [33m"[39;49;00m[33mRed Console[39;49;00m[33m"[39;49;00m$
   251^I$
   252^I[36mprint[39;49;00m [33m{[39;49;00m[33m[39;49;00m$
   253^I[33m-=== Red Console alpha version ===-[39;49;00m$
   254^I[33m([39;49;00m[33monly ASCII input supported[39;49;00m[33m)[39;49;00m[33m[39;49;00m$
   255^I[33m}[39;49;00m$
   256^I$
   257^Ido-console$

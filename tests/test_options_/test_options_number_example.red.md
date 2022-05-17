     1	Red [
     2	    [01m[35mTitle:[39;49;00m  [33m"[39;49;00m[33mRed console[39;49;00m[33m"[39;49;00m
     3	    [01m[35mAuthor:[39;49;00m [[33m"[39;49;00m[33mNenad Rakocevic[39;49;00m[33m"[39;49;00m [33m"[39;49;00m[33mKaj de Vos[39;49;00m[33m"[39;49;00m]
     4	    [01m[35mFile:[39;49;00m   [90m%console.red[39;49;00m
     5	    [01m[35mTabs:[39;49;00m   [34m4[39;49;00m
     6	    [01m[35mRights:[39;49;00m [33m"[39;49;00m[33mCopyright [39;49;00m[33m([39;49;00m[33mC[39;49;00m[33m)[39;49;00m[33m 2012-2013 Nenad Rakocevic. All rights reserved.[39;49;00m[33m"[39;49;00m
     7	    [01m[35mLicense:[39;49;00m [33m{[39;49;00m[33m[39;49;00m
     8	[33m        Distributed under the Boost Software License, Version 1.0.[39;49;00m
     9	[33m        See https://github.com/dockimbel/Red/blob/master/BSL-License.txt[39;49;00m
    10	[33m    [39;49;00m[33m}[39;49;00m
    11	    [01m[35mPurpose:[39;49;00m    [33m"[39;49;00m[33mJust some code for testing Pygments colorizer[39;49;00m[33m"[39;49;00m
    12	    [01m[35mLanguage:[39;49;00m   [90mhttp://www.red-lang.org/[39;49;00m
    13	]
    14
    15	[34m#system-global[39;49;00m [
    16	    [34m#either[39;49;00m [31mOS[39;49;00m = [31m'Windows[39;49;00m [
    17	        [34m#import[39;49;00m [
    18	            [33m"[39;49;00m[33mkernel32.dll[39;49;00m[33m"[39;49;00m [34mstdcall[39;49;00m [
    19	                [01m[35mAttachConsole:[39;49;00m   [33m"[39;49;00m[33mAttachConsole[39;49;00m[33m"[39;49;00m [
    20	                    [31mprocessID[39;49;00m       [[36minteger![39;49;00m]
    21	                    [01m[35mreturn:[39;49;00m         [[36minteger![39;49;00m]
    22	                ]
    23	                [01m[35mSetConsoleTitle:[39;49;00m [33m"[39;49;00m[33mSetConsoleTitleA[39;49;00m[33m"[39;49;00m [
    24	                    [31mtitle[39;49;00m           [[36mc-string![39;49;00m]
    25	                    [01m[35mreturn:[39;49;00m         [[36minteger![39;49;00m]
    26	                ]
    27	                [01m[35mReadConsole:[39;49;00m     [33m"[39;49;00m[33mReadConsoleA[39;49;00m[33m"[39;49;00m [
    28	                    [31mconsoleInput[39;49;00m    [[36minteger![39;49;00m]
    29	                    [31mbuffer[39;49;00m          [[36mbyte-ptr![39;49;00m]
    30	                    [31mcharsToRead[39;49;00m     [[36minteger![39;49;00m]
    31	                    [31mnumberOfChars[39;49;00m   [[36mint-ptr![39;49;00m]
    32	                    [31minputControl[39;49;00m    [[36mint-ptr![39;49;00m]
    33	                    [01m[35mreturn:[39;49;00m         [[36minteger![39;49;00m]
    34	                ]
    35	            ]
    36	        ]
    37	        [01m[35mline-buffer-size:[39;49;00m [34m16[39;49;00m * [34m1024[39;49;00m
    38	        [01m[35mline-buffer:[39;49;00m [31mallocate[39;49;00m [31mline-buffer-size[39;49;00m
    39	    ][
    40	        [34m#switch[39;49;00m [31mOS[39;49;00m [
    41	            [31mMacOSX[39;49;00m [
    42	                [34m#define[39;49;00m [31mReadLine-library[39;49;00m [33m"[39;49;00m[33mlibreadline.dylib[39;49;00m[33m"[39;49;00m
    43	            ]
    44	            [34m#default[39;49;00m [
    45	                [34m#define[39;49;00m [31mReadLine-library[39;49;00m [33m"[39;49;00m[33mlibreadline.so.6[39;49;00m[33m"[39;49;00m
    46	                [34m#define[39;49;00m [31mHistory-library[39;49;00m  [33m"[39;49;00m[33mlibhistory.so.6[39;49;00m[33m"[39;49;00m
    47	            ]
    48	        ]
    49	        [34m#import[39;49;00m [
    50	            [31mReadLine-library[39;49;00m [34mcdecl[39;49;00m [
    51	                [01m[35mread-line:[39;49;00m [33m"[39;49;00m[33mreadline[39;49;00m[33m"[39;49;00m [  [37m; Read a line from the console.[39;49;00m
    52	                    [31mprompt[39;49;00m          [[36mc-string![39;49;00m]
    53	                    [01m[35mreturn:[39;49;00m         [[36mc-string![39;49;00m]
    54	                ]
    55	                [01m[35mrl-bind-key:[39;49;00m [33m"[39;49;00m[33mrl_bind_key[39;49;00m[33m"[39;49;00m [
    56	                    [31mkey[39;49;00m             [[36minteger![39;49;00m]
    57	                    [31mcommand[39;49;00m         [[36minteger![39;49;00m]
    58	                    [01m[35mreturn:[39;49;00m         [[36minteger![39;49;00m]
    59	                ]
    60	                [01m[35mrl-insert:[39;49;00m   [33m"[39;49;00m[33mrl_insert[39;49;00m[33m"[39;49;00m [
    61	                    [31mcount[39;49;00m           [[36minteger![39;49;00m]
    62	                    [31mkey[39;49;00m             [[36minteger![39;49;00m]
    63	                    [01m[35mreturn:[39;49;00m         [[36minteger![39;49;00m]
    64	                ]
    65	            ]
    66	            [34m#if[39;49;00m [31mOS[39;49;00m <> [31m'MacOSX[39;49;00m [
    67	                [31mHistory-library[39;49;00m [34mcdecl[39;49;00m [
    68	                    [01m[35madd-history:[39;49;00m [33m"[39;49;00m[33madd_history[39;49;00m[33m"[39;49;00m [  [37m; Add line to the history.[39;49;00m
    69	                        [31mline[39;49;00m        [[36mc-string![39;49;00m]
    70	                    ]
    71	                ]
    72	            ]
    73	        ]
    74
    75	        [01m[35mrl-insert-wrapper:[39;49;00m [36mfunc[39;49;00m [
    76	            [[34mcdecl[39;49;00m]
    77	            [31mcount[39;49;00m   [[36minteger![39;49;00m]
    78	            [31mkey[39;49;00m     [[36minteger![39;49;00m]
    79	            [01m[35mreturn:[39;49;00m [[36minteger![39;49;00m]
    80	        ][
    81	            [31mrl-insert[39;49;00m [31mcount[39;49;00m [31mkey[39;49;00m
    82	        ]
    83
    84	    ]
    85	]
    86
    87	[01m[35mWindows?:[39;49;00m [36msystem[39;49;00m[36m/platform[39;49;00m = [31m'Windows[39;49;00m
    88
    89	[01m[35mread-argument:[39;49;00m [36mroutine[39;49;00m [
    90	    [36m/local[39;49;00m
    91	        [31margs[39;49;00m [[36mstr-array![39;49;00m]
    92	        [31mstr[39;49;00m  [[36mred-string![39;49;00m]
    93	][
    94	    [36mif[39;49;00m [36msystem[39;49;00m[36m/args-count[39;49;00m <> [34m2[39;49;00m [
    95	        [31mSET_RETURN[39;49;00m(none-value)
    96	        [36mexit[39;49;00m
    97	    ]
    98	    [01m[35margs:[39;49;00m [36msystem[39;49;00m[36m/args-list[39;49;00m + [34m1[39;49;00m                          [37m;-- skip binary filename[39;49;00m
    99	    [01m[35mstr:[39;49;00m [31msimple-io[39;49;00m[36m/read-txt[39;49;00m [31margs[39;49;00m[36m/item[39;49;00m
   100	    [31mSET_RETURN[39;49;00m(str)
   101	]
   102
   103	[01m[35minit-console:[39;49;00m [36mroutine[39;49;00m [
   104	    [31mstr[39;49;00m [[36mstring![39;49;00m]
   105	    [36m/local[39;49;00m
   106	        [31mret[39;49;00m
   107	][
   108	    [34m#either[39;49;00m [31mOS[39;49;00m = [31m'Windows[39;49;00m [
   109	        [37m;ret: AttachConsole -1[39;49;00m
   110	        [37m;if zero? ret [print-line "ReadConsole failed!" halt][39;49;00m
   111
   112	        [01m[35mret:[39;49;00m [31mSetConsoleTitle[39;49;00m [31mas[39;49;00m [36mc-string![39;49;00m [31mstring[39;49;00m[36m/rs-head[39;49;00m [31mstr[39;49;00m
   113	        [36mif[39;49;00m [34mzero?[39;49;00m [31mret[39;49;00m [[31mprint-line[39;49;00m [33m"[39;49;00m[33mSetConsoleTitle failed![39;49;00m[33m"[39;49;00m [36mhalt[39;49;00m]
   114	    ][
   115	        [31mrl-bind-key[39;49;00m [31mas-integer[39;49;00m [36mtab[39;49;00m [31mas-integer[39;49;00m [01m[35m:rl-insert-wrapper[39;49;00m
   116	    ]
   117	]
   118
   119	[01m[35minput:[39;49;00m [36mroutine[39;49;00m [
   120	    [31mprompt[39;49;00m [[36mstring![39;49;00m]
   121	    [36m/local[39;49;00m
   122	        [31mlen[39;49;00m [31mret[39;49;00m [31mstr[39;49;00m [31mbuffer[39;49;00m [31mline[39;49;00m
   123	][
   124	    [34m#either[39;49;00m [31mOS[39;49;00m = [31m'Windows[39;49;00m [
   125	        [01m[35mlen:[39;49;00m [34m0[39;49;00m
   126	        [36mprint[39;49;00m [31mas[39;49;00m [36mc-string![39;49;00m [31mstring[39;49;00m[36m/rs-head[39;49;00m [31mprompt[39;49;00m
   127	        [01m[35mret:[39;49;00m [31mReadConsole[39;49;00m [31mstdin[39;49;00m [31mline-buffer[39;49;00m [31mline-buffer-size[39;49;00m [01m[35m:len[39;49;00m [36mnull[39;49;00m
   128	        [36mif[39;49;00m [34mzero?[39;49;00m [31mret[39;49;00m [[31mprint-line[39;49;00m [33m"[39;49;00m[33mReadConsole failed![39;49;00m[33m"[39;49;00m [36mhalt[39;49;00m]
   129	        [01m[35mlen:[39;49;00m [31mlen[39;49;00m + [34m1[39;49;00m
   130	        [31mline-buffer[39;49;00m[36m/len:[39;49;00m [36mnull-byte[39;49;00m
   131	        [01m[35mstr:[39;49;00m [31mstring[39;49;00m[36m/load[39;49;00m [31mas[39;49;00m [36mc-string![39;49;00m [31mline-buffer[39;49;00m [31mlen[39;49;00m
   132	    ][
   133	        [01m[35mline:[39;49;00m [31mread-line[39;49;00m [31mas[39;49;00m [36mc-string![39;49;00m [31mstring[39;49;00m[36m/rs-head[39;49;00m [31mprompt[39;49;00m
   134	        [36mif[39;49;00m [31mline[39;49;00m = [36mnull[39;49;00m [[36mhalt[39;49;00m]  [37m; EOF[39;49;00m
   135
   136	         [34m#if[39;49;00m [31mOS[39;49;00m <> [31m'MacOSX[39;49;00m [[31madd-history[39;49;00m [31mline[39;49;00m]
   137
   138	        [01m[35mstr:[39;49;00m [31mstring[39;49;00m[36m/load[39;49;00m [31mline[39;49;00m  [34m1[39;49;00m + [32mlength?[39;49;00m [31mline[39;49;00m
   139	[37m;       free as byte-ptr! line[39;49;00m
   140	    ]
   141	    [31mSET_RETURN[39;49;00m(str)
   142	]
   143
   144	[01m[35mcount-delimiters:[39;49;00m [36mfunction[39;49;00m [
   145	    [31mbuffer[39;49;00m  [[36mstring![39;49;00m]
   146	    [01m[35mreturn:[39;49;00m [[36mblock![39;49;00m]
   147	][
   148	    [01m[35mlist:[39;49;00m [32mcopy[39;49;00m [[34m0[39;49;00m [34m0[39;49;00m]
   149	    [01m[35mc:[39;49;00m [36mnone[39;49;00m
   150
   151	    [36mforeach[39;49;00m [31mc[39;49;00m [31mbuffer[39;49;00m [
   152	        [36mcase[39;49;00m [
   153	            [31mescaped?[39;49;00m [
   154	                [01m[35mescaped?:[39;49;00m [36mno[39;49;00m
   155	            ]
   156	            [31min-comment?[39;49;00m [
   157	                [36mswitch[39;49;00m [31mc[39;49;00m [
   158	                    [33m#"[39;49;00m[33m^/"[39;49;00m [[01m[35min-comment?:[39;49;00m [36mno[39;49;00m]
   159	                ]
   160	            ]
   161	            [31m'else[39;49;00m [
   162	                [36mswitch[39;49;00m [31mc[39;49;00m [
   163	                    [33m#"[39;49;00m[33m^^"[39;49;00m [[01m[35mescaped?:[39;49;00m [36myes[39;49;00m]
   164	                    [33m#"[39;49;00m[33m;"[39;49;00m  [[36mif[39;49;00m [34mzero?[39;49;00m [31mlist[39;49;00m[36m/2[39;49;00m [[01m[35min-comment?:[39;49;00m [36myes[39;49;00m]]
   165	                    [33m#"[39;49;00m[33m["[39;49;00m  [[31mlist[39;49;00m[36m/1:[39;49;00m [31mlist[39;49;00m[36m/1[39;49;00m + [34m1[39;49;00m]
   166	                    [33m#"[39;49;00m[33m]"[39;49;00m  [[31mlist[39;49;00m[36m/1:[39;49;00m [31mlist[39;49;00m[36m/1[39;49;00m - [34m1[39;49;00m]
   167	                    [33m#"[39;49;00m[33m{"[39;49;00m  [[31mlist[39;49;00m[36m/2:[39;49;00m [31mlist[39;49;00m[36m/2[39;49;00m + [34m1[39;49;00m]
   168	                    [33m#"[39;49;00m[33m}"[39;49;00m  [[31mlist[39;49;00m[36m/2:[39;49;00m [31mlist[39;49;00m[36m/2[39;49;00m - [34m1[39;49;00m]
   169	                ]
   170	            ]
   171	        ]
   172	    ]
   173	    [31mlist[39;49;00m
   174	]
   175
   176	[01m[35mdo-console:[39;49;00m [36mfunction[39;49;00m [][
   177	    [01m[35mbuffer:[39;49;00m [32mmake[39;49;00m [36mstring![39;49;00m [34m10000[39;49;00m
   178	    [01m[35mprompt:[39;49;00m [01m[35mred-prompt:[39;49;00m [33m"[39;49;00m[33mred>> [39;49;00m[33m"[39;49;00m
   179	    [01m[35mmode:[39;49;00m  [31m'mono[39;49;00m
   180
   181	    [01m[35mswitch-mode:[39;49;00m [
   182	        [01m[35mmode:[39;49;00m [36mcase[39;49;00m [
   183	            [31mcnt[39;49;00m[36m/1[39;49;00m [31m>[39;49;00m [34m0[39;49;00m [[31m'block[39;49;00m]
   184	            [31mcnt[39;49;00m[36m/2[39;49;00m [31m>[39;49;00m [34m0[39;49;00m [[31m'string[39;49;00m]
   185	            [31m'else[39;49;00m     [
   186	                [01m[35mprompt:[39;49;00m [31mred-prompt[39;49;00m
   187	                [36mdo[39;49;00m [31meval[39;49;00m
   188	                [31m'mono[39;49;00m
   189	            ]
   190	        ]
   191	        [01m[35mprompt:[39;49;00m [36mswitch[39;49;00m [31mmode[39;49;00m [
   192	            [31mblock[39;49;00m  [[33m"[39;49;00m[33m[[39;49;00m[33m^-[39;49;00m[33m"[39;49;00m]
   193	            [31mstring[39;49;00m [[33m"[39;49;00m[33m{[39;49;00m[33m^-[39;49;00m[33m"[39;49;00m]
   194	            [31mmono[39;49;00m   [[31mred-prompt[39;49;00m]
   195	        ]
   196	    ]
   197
   198	    [01m[35meval:[39;49;00m [
   199	        [01m[35mcode:[39;49;00m [36mload[39;49;00m[36m/all[39;49;00m [31mbuffer[39;49;00m
   200
   201	        [36munless[39;49;00m [32mtail?[39;49;00m [31mcode[39;49;00m [
   202	            [36mset[39;49;00m[36m/any[39;49;00m [31m'result[39;49;00m [36mdo[39;49;00m [31mcode[39;49;00m
   203
   204	            [36munless[39;49;00m [34munset?[39;49;00m [01m[35m:result[39;49;00m [
   205	                [36mif[39;49;00m [34m67[39;49;00m = [32mlength?[39;49;00m [01m[35mresult:[39;49;00m [32mmold[39;49;00m[36m/part[39;49;00m [01m[35m:result[39;49;00m [34m67[39;49;00m [  [37m;-- optimized for width = 72[39;49;00m
   206	                    [32mclear[39;49;00m [32mback[39;49;00m [32mtail[39;49;00m [31mresult[39;49;00m
   207	                    [32mappend[39;49;00m [31mresult[39;49;00m [33m"[39;49;00m[33m...[39;49;00m[33m"[39;49;00m
   208	                ]
   209	                [36mprint[39;49;00m [[33m"[39;49;00m[33m==[39;49;00m[33m"[39;49;00m [31mresult[39;49;00m]
   210	            ]
   211	        ]
   212	        [32mclear[39;49;00m [31mbuffer[39;49;00m
   213	    ]
   214
   215	    [36mwhile[39;49;00m [[36mtrue[39;49;00m][
   216	        [36munless[39;49;00m [32mtail?[39;49;00m [01m[35mline:[39;49;00m [31minput[39;49;00m [31mprompt[39;49;00m [
   217	            [32mappend[39;49;00m [31mbuffer[39;49;00m [31mline[39;49;00m
   218	            [01m[35mcnt:[39;49;00m [31mcount-delimiters[39;49;00m [31mbuffer[39;49;00m
   219
   220	            [36meither[39;49;00m [31mWindows?[39;49;00m [
   221	                [32mremove[39;49;00m [32mskip[39;49;00m [32mtail[39;49;00m [31mbuffer[39;49;00m [34m-2[39;49;00m          [37m;-- clear extra CR (Windows)[39;49;00m
   222	            ][
   223	                [32mappend[39;49;00m [31mbuffer[39;49;00m [36mlf[39;49;00m                    [37m;-- Unix[39;49;00m
   224	            ]
   225
   226	            [36mswitch[39;49;00m [31mmode[39;49;00m [
   227	                [31mblock[39;49;00m  [[36mif[39;49;00m [31mcnt[39;49;00m[36m/1[39;49;00m <= [34m0[39;49;00m [[36mdo[39;49;00m [31mswitch-mode[39;49;00m]]
   228	                [31mstring[39;49;00m [[36mif[39;49;00m [31mcnt[39;49;00m[36m/2[39;49;00m <= [34m0[39;49;00m [[36mdo[39;49;00m [31mswitch-mode[39;49;00m]]
   229	                [31mmono[39;49;00m   [[36mdo[39;49;00m [36meither[39;49;00m [36many[39;49;00m [[31mcnt[39;49;00m[36m/1[39;49;00m [31m>[39;49;00m [34m0[39;49;00m [31mcnt[39;49;00m[36m/2[39;49;00m [31m>[39;49;00m [34m0[39;49;00m][[31mswitch-mode[39;49;00m][[31meval[39;49;00m]]
   230	            ]
   231	        ]
   232	    ]
   233	]
   234
   235	[01m[35mq:[39;49;00m [01m[35m:quit[39;49;00m
   236
   237	[36mif[39;49;00m [01m[35mscript:[39;49;00m [31mread-argument[39;49;00m [
   238	    [01m[35mscript:[39;49;00m [36mload[39;49;00m [31mscript[39;49;00m
   239	    [36meither[39;49;00m [36many[39;49;00m [
   240	        [31mscript[39;49;00m[36m/1[39;49;00m <> [31m'Red[39;49;00m
   241	        [36mnot[39;49;00m [34mblock?[39;49;00m [31mscript[39;49;00m[36m/2[39;49;00m
   242	    ][
   243	        [36mprint[39;49;00m [33m"[39;49;00m[33m*** Error: not a Red program![39;49;00m[33m"[39;49;00m
   244	    ][
   245	        [36mdo[39;49;00m [32mskip[39;49;00m [31mscript[39;49;00m [34m2[39;49;00m
   246	    ]
   247	    [36mquit[39;49;00m
   248	]
   249
   250	[31minit-console[39;49;00m [33m"[39;49;00m[33mRed Console[39;49;00m[33m"[39;49;00m
   251
   252	[36mprint[39;49;00m [33m{[39;49;00m[33m[39;49;00m
   253	[33m-=== Red Console alpha version ===-[39;49;00m
   254	[33m([39;49;00m[33monly ASCII input supported[39;49;00m[33m)[39;49;00m[33m[39;49;00m
   255	[33m}[39;49;00m
   256
   257	do-console

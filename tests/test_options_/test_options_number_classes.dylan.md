     1	[36mmodule[39;49;00m:[37m [39;49;00m[33msample[39;49;00m[37m[39;49;00m
     2	[36mcomment[39;49;00m:[37m [39;49;00m[33mfor make sure that does not highlight per word.[39;49;00m
     3	[33m         and it continues on to the next line.[39;49;00m[37m[39;49;00m
     4	[37m[39;49;00m
     5	[34mdefine[39;49;00m[37m [39;49;00m[36mclass[39;49;00m[37m [39;49;00m[04m[32m<car>[39;49;00m[37m [39;49;00m([04m[32m<object>[39;49;00m)[37m[39;49;00m
     6	[37m  [39;49;00m[36mslot[39;49;00m[37m [39;49;00mserial-number[37m [39;49;00m::[37m [39;49;00m[04m[32m<integer>[39;49;00m[37m [39;49;00m=[37m [39;49;00munique-serial-number();[37m[39;49;00m
     7	[37m  [39;49;00m[36mconstant[39;49;00m[37m [39;49;00m[36mslot[39;49;00m[37m [39;49;00mmodel-name[37m [39;49;00m::[37m [39;49;00m[04m[32m<string>[39;49;00m,[37m[39;49;00m
     8	[37m    [39;49;00m[34mrequired-init-keyword:[39;49;00m[37m [39;49;00m[34mmodel:[39;49;00m;[37m[39;49;00m
     9	[37m  [39;49;00m[36meach-subclass[39;49;00m[37m [39;49;00m[36mslot[39;49;00m[37m [39;49;00mhas-sunroof?[37m [39;49;00m::[37m [39;49;00m[04m[32m<boolean>[39;49;00m,[37m[39;49;00m
    10	[37m    [39;49;00m[34minit-keyword:[39;49;00m[37m [39;49;00m[34msunroof?:[39;49;00m,[37m[39;49;00m
    11	[37m    [39;49;00m[34minit-value:[39;49;00m[37m [39;49;00m#f;[37m[39;49;00m
    12	[37m  [39;49;00m[36mkeyword[39;49;00m[37m [39;49;00m[34mfoo:[39;49;00m;[37m[39;49;00m
    13	[37m  [39;49;00m[36mrequired[39;49;00m[37m [39;49;00m[36mkeyword[39;49;00m[37m [39;49;00m[34mbar:[39;49;00m;[37m[39;49;00m
    14	[34mend[39;49;00m[37m [39;49;00m[36mclass[39;49;00m[37m [39;49;00m[04m[32m<car>[39;49;00m;[37m[39;49;00m
    15	[37m[39;49;00m
    16	[34mdefine[39;49;00m[37m [39;49;00m[36mclass[39;49;00m[37m [39;49;00m[04m[32m<flying-car>[39;49;00m[37m [39;49;00m([04m[32m<car>[39;49;00m)[37m[39;49;00m
    17	[34mend[39;49;00m[37m [39;49;00m[36mclass[39;49;00m[37m [39;49;00m[04m[32m<flying-car>[39;49;00m;[37m[39;49;00m
    18	[37m[39;49;00m
    19	[34mlet[39;49;00m[37m [39;49;00mflying-car[37m [39;49;00m=[37m [39;49;00m[36mmake[39;49;00m([04m[32m<flying-car>[39;49;00m);[37m[39;49;00m
    20	[34mlet[39;49;00m[37m [39;49;00mcar?[37m [39;49;00m::[37m [39;49;00m[04m[32m<car?>[39;49;00m[37m [39;49;00m=[37m [39;49;00m#f;[37m[39;49;00m
    21	[34mlet[39;49;00m[37m [39;49;00mprefixed-car[37m [39;49;00m::[37m [39;49;00m[04m[32m<vehicles/car>[39;49;00m[37m [39;49;00m=[37m [39;49;00m#f;[37m[39;49;00m
    22	[34mlet[39;49;00m[37m [39;49;00mmodel[37m [39;49;00m::[37m [39;49;00m[04m[32m<car-911>[39;49;00m[37m [39;49;00m=[37m [39;49;00m#f;[37m[39;49;00m
    23	[37m[39;49;00m
    24	[34mdefine[39;49;00m[37m [39;49;00m[36mconstant[39;49;00m[37m [39;49;00m[31m$empty-string[39;49;00m[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33m"[39;49;00m;[37m[39;49;00m
    25	[34mdefine[39;49;00m[37m [39;49;00m[36mconstant[39;49;00m[37m [39;49;00m[31m$escaped-backslash[39;49;00m[37m [39;49;00m=[37m [39;49;00m[33m'\\'[39;49;00m;[37m[39;49;00m
    26	[34mdefine[39;49;00m[37m [39;49;00m[36mconstant[39;49;00m[37m [39;49;00m[31m$escaped-single-quote[39;49;00m[37m [39;49;00m=[37m [39;49;00m[33m'\''[39;49;00m;[37m[39;49;00m
    27	[37m[39;49;00m
    28	[34mdefine[39;49;00m[37m [39;49;00m[36mvariable[39;49;00m[37m [39;49;00m[31m*unique-serial-number*[39;49;00m[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m
    29	[37m[39;49;00m
    30	[34mdefine[39;49;00m[37m [39;49;00m[36mfunction[39;49;00m[37m [39;49;00munique-serial-number()[37m [39;49;00m=>[37m [39;49;00m(usn[37m [39;49;00m::[37m [39;49;00m[04m[32m<integer>[39;49;00m)[37m[39;49;00m
    31	[37m  [39;49;00m[34mlet[39;49;00m[37m [39;49;00mserial[37m [39;49;00m=[37m [39;49;00m[31m*unique-serial-number*[39;49;00m;[37m[39;49;00m
    32	[37m  [39;49;00m[31m*unique-serial-number*[39;49;00m[37m [39;49;00m:=[37m [39;49;00m[31m*unique-serial-number*[39;49;00m[37m [39;49;00m+[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m
    33	[37m  [39;49;00mserial;[37m[39;49;00m
    34	[34mend[39;49;00m[37m [39;49;00m[36mfunction[39;49;00m;[37m[39;49;00m
    35	[37m[39;49;00m
    36	[34mdefine[39;49;00m[37m [39;49;00m[36mconstant[39;49;00m[37m [39;49;00m[31m$blue-car[39;49;00m[37m [39;49;00m=[37m [39;49;00m[36mmake[39;49;00m([04m[32m<car>[39;49;00m,[37m [39;49;00m[34mmodel:[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mViper[39;49;00m[33m"[39;49;00m);[37m[39;49;00m
    37	[34mdefine[39;49;00m[37m [39;49;00m[36mconstant[39;49;00m[37m [39;49;00m[31m$black-car[39;49;00m[37m [39;49;00m=[37m [39;49;00m[36mmake[39;49;00m([04m[32m<car>[39;49;00m,[37m [39;49;00m[34mmodel:[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mTown Car[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[34msunroof?:[39;49;00m[37m [39;49;00m#t);[37m[39;49;00m
    38	[34mdefine[39;49;00m[37m [39;49;00m[36mconstant[39;49;00m[37m [39;49;00m[31m$red-car[39;49;00m[37m [39;49;00m=[37m [39;49;00m[36mmake[39;49;00m([04m[32m<car>[39;49;00m,[37m [39;49;00m[34mmodel:[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mF40[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[34msunroof?:[39;49;00m[37m [39;49;00m#f);[37m[39;49;00m
    39	[37m[39;49;00m
    40	[34mdefine[39;49;00m[37m [39;49;00m[36mmethod[39;49;00m[37m [39;49;00mfoo()[37m [39;49;00m=>[37m [39;49;00m_[37m [39;49;00m::[37m [39;49;00m[04m[32m<boolean>[39;49;00m[37m[39;49;00m
    41	[37m  [39;49;00m#t[37m[39;49;00m
    42	[34mend[39;49;00m[37m [39;49;00m[36mmethod[39;49;00m;[37m[39;49;00m
    43	[37m[39;49;00m
    44	[34mdefine[39;49;00m[37m [39;49;00m[36mmethod[39;49;00m[37m [39;49;00mfoo()[37m [39;49;00m=>[37m [39;49;00m_[37m [39;49;00m::[37m [39;49;00m[04m[32m<boolean>[39;49;00m;[37m[39;49;00m
    45	[37m  [39;49;00m#t[37m[39;49;00m
    46	[34mend[39;49;00m[37m [39;49;00m[36mmethod[39;49;00m;[37m[39;49;00m
    47	[37m[39;49;00m
    48	[34mdefine[39;49;00m[37m [39;49;00m[36mmethod[39;49;00m[37m [39;49;00m\+[37m[39;49;00m
    49	[37m    [39;49;00m(offset1[37m [39;49;00m::[37m [39;49;00m[04m[32m<time-offset>[39;49;00m,[37m [39;49;00moffset2[37m [39;49;00m::[37m [39;49;00m[04m[32m<time-offset>[39;49;00m)[37m[39;49;00m
    50	[37m [39;49;00m=>[37m [39;49;00m(sum[37m [39;49;00m::[37m [39;49;00m[04m[32m<time-offset>[39;49;00m)[37m[39;49;00m
    51	[37m  [39;49;00m[34mlet[39;49;00m[37m [39;49;00msum[37m [39;49;00m=[37m [39;49;00moffset1.total-seconds[37m [39;49;00m+[37m [39;49;00moffset2.total-seconds;[37m[39;49;00m
    52	[37m  [39;49;00m[36mmake[39;49;00m([04m[32m<time-offset>[39;49;00m,[37m [39;49;00m[34mtotal-seconds:[39;49;00m[37m [39;49;00msum);[37m[39;49;00m
    53	[34mend[39;49;00m[37m [39;49;00m[36mmethod[39;49;00m[37m [39;49;00m\+;[37m[39;49;00m
    54	[37m[39;49;00m
    55	[34mdefine[39;49;00m[37m [39;49;00m[36mmethod[39;49;00m[37m [39;49;00mbar[37m [39;49;00m()[37m[39;49;00m
    56	[37m  [39;49;00m[34m1[39;49;00m[37m [39;49;00m|[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m&[37m [39;49;00m[34m3[39;49;00m[37m[39;49;00m
    57	[34mend[39;49;00m[37m[39;49;00m
    58	[37m[39;49;00m
    59	[34mif[39;49;00m[37m [39;49;00m(bar)[37m[39;49;00m
    60	[37m  [39;49;00m[34m1[39;49;00m[37m[39;49;00m
    61	[34melseif[39;49;00m[37m [39;49;00m(foo)[37m[39;49;00m
    62	[37m  [39;49;00m[34m2[39;49;00m[37m[39;49;00m
    63	[34melse[39;49;00m[37m[39;49;00m
    64	[37m  [39;49;00m[34m3[39;49;00m[37m[39;49;00m
    65	[34mend[39;49;00m[37m [39;49;00m[34mif[39;49;00m;[37m[39;49;00m
    66	[37m[39;49;00m
    67	[34mselect[39;49;00m[37m [39;49;00m(foo[37m [39;49;00m[34mby[39;49;00m[37m [39;49;00m[36minstance?[39;49;00m)[37m[39;49;00m
    68	[37m  [39;49;00m[04m[32m<integer>[39;49;00m[37m [39;49;00m=>[37m [39;49;00m[34m1[39;49;00m[37m[39;49;00m
    69	[37m  [39;49;00m[34motherwise[39;49;00m[37m [39;49;00m=>[37m [39;49;00m[34m3[39;49;00m[37m[39;49;00m
    70	[34mend[39;49;00m[37m [39;49;00m[34mselect[39;49;00m;[37m[39;49;00m
    71	[37m[39;49;00m
    72	[37m/*[39;49;00m[37m multi[39;49;00m
    73	[37m   line[39;49;00m
    74	[37m   comment[39;49;00m
    75	[37m*/[39;49;00m[37m[39;49;00m
    76	[37m[39;49;00m
    77	[37m/*[39;49;00m[37m multi line comments[39;49;00m
    78	[37m  [39;49;00m[37m/*[39;49;00m[37m can be [39;49;00m[37m*/[39;49;00m[37m[39;49;00m
    79	[37m  nested [39;49;00m[37m*/[39;49;00m[37m[39;49;00m
    80	[37m[39;49;00m
    81	[34mdefine[39;49;00m[37m [39;49;00m[36mconstant[39;49;00m[37m [39;49;00m[31m$symbol[39;49;00m[37m [39;49;00m=[37m [39;49;00m[33m#"[39;49;00m[33mhello[39;49;00m[33m"[39;49;00m;[37m[39;49;00m
    82	[34mdefine[39;49;00m[37m [39;49;00m[36mvariable[39;49;00m[37m [39;49;00m[31m*vector*[39;49;00m[37m [39;49;00m=[37m [39;49;00m#[[34m3.5[39;49;00m,[37m [39;49;00m[34m5[39;49;00m][37m[39;49;00m
    83	[34mdefine[39;49;00m[37m [39;49;00m[36mconstant[39;49;00m[37m [39;49;00m[31m$list[39;49;00m[37m [39;49;00m=[37m [39;49;00m#([34m1[39;49;00m,[37m [39;49;00m[34m2[39;49;00m);[37m[39;49;00m
    84	[34mdefine[39;49;00m[37m [39;49;00m[36mconstant[39;49;00m[37m [39;49;00m[31m$pair[39;49;00m[37m [39;49;00m=[37m [39;49;00m#([34m1[39;49;00m[37m [39;49;00m.[37m [39;49;00m[33m"[39;49;00m[33mfoo[39;49;00m[33m"[39;49;00m)[37m[39;49;00m
    85	[37m[39;49;00m
    86	[34mlet[39;49;00m[37m [39;49;00moctal-number[37m [39;49;00m=[37m [39;49;00m[34m#o23[39;49;00m[34m8[39;49;00m;[37m[39;49;00m
    87	[34mlet[39;49;00m[37m [39;49;00mhex-number[37m [39;49;00m=[37m [39;49;00m[34m#x3890ADEF[39;49;00m;[37m[39;49;00m
    88	[34mlet[39;49;00m[37m [39;49;00mbinary-number[37m [39;49;00m=[37m [39;49;00m[34m#b1010[39;49;00m;[37m[39;49;00m
    89	[34mlet[39;49;00m[37m [39;49;00mfloat-exponent[37m [39;49;00m=[37m [39;49;00m[34m3.5e10[39;49;00m;[37m[39;49;00m
    90	[37m[39;49;00m
    91	[36mblock[39;49;00m[37m [39;49;00m(return)[37m[39;49;00m
    92	[37m  [39;49;00mwith-lock[37m [39;49;00m(lock)[37m[39;49;00m
    93	[37m    [39;49;00mreturn();[37m[39;49;00m
    94	[37m  [39;49;00m[34mend[39;49;00m;[37m[39;49;00m
    95	[36mexception[39;49;00m[37m [39;49;00m(e[37m [39;49;00m::[37m [39;49;00m[04m[32m<error>[39;49;00m)[37m[39;49;00m
    96	[37m    [39;49;00mformat-out([33m"[39;49;00m[33mOh no[39;49;00m[33m"[39;49;00m);[37m[39;49;00m
    97	[34mcleanup[39;49;00m[37m[39;49;00m
    98	[37m    [39;49;00mreturn();[37m[39;49;00m
    99	[34mafterwards[39;49;00m[37m[39;49;00m
   100	[37m    [39;49;00mformat-out([33m"[39;49;00m[33mHello[39;49;00m[33m"[39;49;00m);[37m[39;49;00m
   101	[34mend[39;49;00m;[37m[39;49;00m
   102	[37m[39;49;00m
   103	[34mdefine[39;49;00m[37m [39;49;00m[36mmacro[39;49;00m[37m [39;49;00mrepeat[37m[39;49;00m
   104	[37m  [39;49;00m{[37m [39;49;00mrepeat[37m [39;49;00m[94m?[39;49;00m:[36mbody[39;49;00m[37m [39;49;00m[34mend[39;49;00m[37m [39;49;00m}[37m[39;49;00m
   105	[37m   [39;49;00m=>[37m [39;49;00m{[37m [39;49;00m[36mblock[39;49;00m[37m [39;49;00m([94m?=stop![39;49;00m)[37m[39;49;00m
   106	[37m          [39;49;00m[34mlocal[39;49;00m[37m [39;49;00m[36mmethod[39;49;00m[37m [39;49;00magain()[37m [39;49;00m[94m?body[39;49;00m;[37m [39;49;00magain()[37m [39;49;00m[34mend[39;49;00m;[37m[39;49;00m
   107	[37m          [39;49;00magain();[37m[39;49;00m
   108	[37m        [39;49;00m[34mend[39;49;00m[37m [39;49;00m}[37m[39;49;00m
   109	[34mend[39;49;00m[37m [39;49;00m[36mmacro[39;49;00m[37m [39;49;00mrepeat;[37m[39;49;00m
   110	[37m[39;49;00m
   111	[34mdefine[39;49;00m[37m [39;49;00m[36mmacro[39;49;00m[37m [39;49;00mwith-decoded-seconds[37m[39;49;00m
   112	[37m  [39;49;00m{[37m[39;49;00m
   113	[37m    [39;49;00mwith-decoded-seconds[37m[39;49;00m
   114	[37m      [39;49;00m([94m?max[39;49;00m:[36mvariable[39;49;00m,[37m [39;49;00m[94m?min[39;49;00m:[36mvariable[39;49;00m,[37m [39;49;00m[94m?sec[39;49;00m:[36mvariable[39;49;00m[37m [39;49;00m=[37m [39;49;00m[94m?time[39;49;00m:[36mexpression[39;49;00m)[37m[39;49;00m
   115	[37m      [39;49;00m[94m?[39;49;00m:[36mbody[39;49;00m[37m[39;49;00m
   116	[37m    [39;49;00m[34mend[39;49;00m[37m[39;49;00m
   117	[37m  [39;49;00m}[37m[39;49;00m
   118	[37m    [39;49;00m=>[37m [39;49;00m{[37m[39;49;00m
   119	[37m         [39;49;00m[34mlet[39;49;00m[37m [39;49;00m([94m?max[39;49;00m,[37m [39;49;00m[94m?min[39;49;00m,[37m [39;49;00m[94m?sec[39;49;00m)[37m [39;49;00m=[37m [39;49;00mdecode-total-seconds([94m?time[39;49;00m);[37m[39;49;00m
   120	[37m         [39;49;00m[94m?body[39;49;00m[37m[39;49;00m
   121	[37m       [39;49;00m}[37m[39;49;00m
   122	[34mend[39;49;00m[37m [39;49;00m[36mmacro[39;49;00m;[37m[39;49;00m
   123	[37m[39;49;00m
   124	[34mlet[39;49;00m[37m [39;49;00mx[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33mThis size call should be seen as a builtin despite the odd case.[39;49;00m[33m"[39;49;00m.[36msiZe[39;49;00m;

     1	--[37m [39;49;00mExample[37m [39;49;00mTransact-[34mSQL[39;49;00m[37m [39;49;00m[34mfile[39;49;00m.[37m[39;49;00m$
     2	[37m[39;49;00m$
     3	--[37m [39;49;00mSingle[37m [39;49;00mline[37m [39;49;00mcomment[37m[39;49;00m$
     4	[37m/*[39;49;00m[37m A comment [39;49;00m$
     5	[37m [39;49;00m[37m*[39;49;00m[37m spawning two lines. [39;49;00m[37m*/[39;49;00m[37m[39;49;00m$
     6	[37m                         [39;49;00m[37m/*[39;49;00m[37m An indented comment[39;49;00m$
     7	[37m                          [39;49;00m[37m*[39;49;00m[37m spawning multiple[39;49;00m$
     8	[37m                          [39;49;00m[37m*[39;49;00m[37m lines. [39;49;00m[37m*/[39;49;00m[37m[39;49;00m$
     9	[37m/*[39;49;00m[37m A [39;49;00m[37m/*[39;49;00m[37m nested [39;49;00m[37m*/[39;49;00m[37m comment. [39;49;00m[37m*/[39;49;00m[37m[39;49;00m$
    10	[37m[39;49;00m$
    11	[34mselect[39;49;00m[37m[39;49;00m$
    12	[37m    [39;49;00m[32mleft[39;49;00m(emp.firstname,[37m [39;49;00m[34m1[39;49;00m)[37m [39;49;00m+[37m [39;49;00m[33m'.'[39;49;00m[37m [39;49;00m+[37m [39;49;00m[emp.surname][37m [39;49;00m[34mas[39;49;00m[37m [39;49;00m[33m"Name"[39;49;00m,[37m[39;49;00m$
    13	[37m    [39;49;00mdep.name[37m [39;49;00m[34mas[39;49;00m[37m [39;49;00m[Department][37m[39;49;00m$
    14	[34minto[39;49;00m[37m[39;49;00m$
    15	[37m    [39;49;00m#temp_employee[37m[39;49;00m$
    16	[34mfrom[39;49;00m[37m[39;49;00m$
    17	[37m    [39;49;00memployee[37m [39;49;00m[34mas[39;49;00m[37m [39;49;00memp[37m[39;49;00m$
    18	[37m    [39;49;00m[34minner[39;49;00m[37m [39;49;00m[34mjoin[39;49;00m[37m [39;49;00mdepartment[37m [39;49;00m[34mas[39;49;00m[37m [39;49;00mdep[37m [39;49;00m[34mon[39;49;00m[37m[39;49;00m$
    19	[37m       [39;49;00mdep.ident_code[37m [39;49;00m=[37m [39;49;00memp.department_id[37m[39;49;00m$
    20	[34mwhere[39;49;00m[37m[39;49;00m$
    21	[37m    [39;49;00memp.date_of_birth[37m [39;49;00m>=[37m [39;49;00m[33m'1990-01-01'[39;49;00m;[37m[39;49;00m$
    22	[34mgo[39;49;00m[37m[39;49;00m$
    23	[37m[39;49;00m$
    24	[34mdeclare[39;49;00m[37m [39;49;00m[31m@TextToFind[39;49;00m[37m [39;49;00m[04m[32mnvarchar[39;49;00m([34m100[39;49;00m)[37m [39;49;00m=[37m [39;49;00mN[33m'some[39;49;00m$
    25	[33mtext across[39;49;00m$
    26	[33mmultiple lines'[39;49;00m;[37m[39;49;00m$
    27	[37m[39;49;00m$
    28	[34mset[39;49;00m[37m [39;49;00m[31m@TextToFind[39;49;00m[37m [39;49;00m[04m[32mvarchar[39;49;00m([34m32[39;49;00m)[37m [39;49;00m=[37m [39;49;00m[33m'hello'[39;49;00m[37m [39;49;00m+[37m [39;49;00m[33m' world'[39;49;00m;[37m[39;49;00m$
    29	[34mset[39;49;00m[37m [39;49;00m[31m@TextTiFind[39;49;00m[37m [39;49;00m+=[37m [39;49;00m[33m'!'[39;49;00m;[37m[39;49;00m$
    30	[37m[39;49;00m$
    31	[34mdeclare[39;49;00m[37m [39;49;00m[31m@Count[39;49;00m[37m [39;49;00m[04m[32mint[39;49;00m[37m [39;49;00m=[37m [39;49;00m[34m17[39;49;00m[37m [39;49;00m*[37m [39;49;00m([34m3[39;49;00m[37m [39;49;00m-[37m [39;49;00m[34m5[39;49;00m);[37m[39;49;00m$
    32	[37m[39;49;00m$
    33	[34mdelete[39;49;00m[37m [39;49;00m[34mfrom[39;49;00m[37m[39;49;00m$
    34	[37m    [39;49;00m[server].[database].[schema].[table][37m[39;49;00m$
    35	[34mwhere[39;49;00m[37m[39;49;00m$
    36	[37m    [39;49;00m[Text][37m [39;49;00m=[37m [39;49;00m[31m@TextToFind[39;49;00m[37m [39;49;00m[35mand[39;49;00m[37m [39;49;00mauthor[37m [39;49;00m[35mNot[39;49;00m[37m [39;49;00m[35mLIKE[39;49;00m[37m [39;49;00m[33m'%some%'[39;49;00m;[37m[39;49;00m$
    37	[37m[39;49;00m$
    38	[34mgoto[39;49;00m[37m [39;49;00moverthere;[37m[39;49;00m$
    39	overthere:[37m[39;49;00m$
    40	[37m[39;49;00m$
    41	[34mselect[39;49;00m[37m[39;49;00m$
    42	[37m    [39;49;00m[34m123[39;49;00m[37m [39;49;00m[34mas[39;49;00m[37m [39;49;00m[33m"int 1"[39;49;00m,[37m[39;49;00m$
    43	[37m    [39;49;00m+[34m123[39;49;00m[37m [39;49;00m[34mas[39;49;00m[37m [39;49;00m[33m"int 2"[39;49;00m,[37m[39;49;00m$
    44	[37m    [39;49;00m-[34m123[39;49;00m[37m [39;49;00m[34mas[39;49;00m[37m [39;49;00m[33m"int 3"[39;49;00m,[37m[39;49;00m$
    45	[37m    [39;49;00m[34m0x20[39;49;00m[37m [39;49;00m[34mas[39;49;00m[37m [39;49;00m[33m"hex int"[39;49;00m,[37m[39;49;00m$
    46	[37m    [39;49;00m[34m123.45[39;49;00m[37m [39;49;00m[34mas[39;49;00m[37m [39;49;00m[33m"float 1"[39;49;00m,[37m[39;49;00m$
    47	[37m    [39;49;00m-[34m1.23e45[39;49;00m[37m [39;49;00m[34mas[39;49;00m[37m [39;49;00m[33m"float 2"[39;49;00m[37m[39;49;00m$
    48	[37m    [39;49;00m+[34m1.23E+45[39;49;00m[37m [39;49;00m[34mas[39;49;00m[37m [39;49;00m[33m"float 3"[39;49;00m,[37m[39;49;00m$
    49	[37m    [39;49;00m-[34m1.23e-45[39;49;00m[37m [39;49;00m[34mas[39;49;00m[37m [39;49;00m[33m"float 4"[39;49;00m,[37m[39;49;00m$
    50	[37m    [39;49;00m[34m1.[39;49;00m[37m [39;49;00m[34mas[39;49;00m[37m [39;49;00m[33m"float 5"[39;49;00m,[37m[39;49;00m$
    51	[37m    [39;49;00m[34m.1[39;49;00m[37m [39;49;00m[34mas[39;49;00m[37m [39;49;00m[33m"float 6"[39;49;00m,[37m[39;49;00m$
    52	[37m    [39;49;00m[34m1.e2[39;49;00m[37m [39;49;00m[34mas[39;49;00m[37m [39;49;00m[33m"float 7"[39;49;00m,[37m[39;49;00m$
    53	[37m    [39;49;00m[34m.1e2[39;49;00m[37m [39;49;00m[34mas[39;49;00m[37m [39;49;00m[33m"float 8"[39;49;00m;[37m[39;49;00m$
    54	[37m[39;49;00m$
    55	[34mSelect[39;49;00m[37m [39;49;00m[36m@@Error[39;49;00m,[37m [39;49;00m[32m$PARTITion[39;49;00m.RangePF1([34m10[39;49;00m);[37m[39;49;00m$
    56	[37m[39;49;00m$
    57	[34mselect[39;49;00m[37m [39;49;00m[34mtop[39;49;00m[37m [39;49;00m[34m3[39;49;00m[37m [39;49;00mÄhnliches[37m [39;49;00m[34mfrom[39;49;00m[37m [39;49;00mMüll;[37m[39;49;00m$
    58	[37m[39;49;00m$
    59	--[37m [39;49;00mExample[37m [39;49;00m[34mtransaction[39;49;00m[37m[39;49;00m$
    60	[34mBEGIN[39;49;00m[37m [39;49;00m[34mTRAN[39;49;00m[37m[39;49;00m$
    61	[37m[39;49;00m$
    62	[34mBEGIN[39;49;00m[37m [39;49;00m[34mTRY[39;49;00m[37m[39;49;00m$
    63	[37m   [39;49;00m[34mINSERT[39;49;00m[37m [39;49;00m[34mINTO[39;49;00m[37m [39;49;00m#temp_employe(Name,[37m [39;49;00mDepartment)[37m [39;49;00m[34mVALUES[39;49;00m[37m [39;49;00m([33m'L. Miller'[39;49;00m,[37m [39;49;00m[33m'Sales'[39;49;00m)[37m[39;49;00m$
    64	[37m   [39;49;00m[34miNsErT[39;49;00m[37m [39;49;00m[34minTO[39;49;00m[37m [39;49;00m#temp_employe(Name,[37m [39;49;00mDepartment)[37m [39;49;00m[34mVaLuEs[39;49;00m[37m [39;49;00m([33m'M. Webster'[39;49;00m,[37m [39;49;00m[33m'Helpdesk'[39;49;00m)[37m[39;49;00m$
    65	[37m   [39;49;00m[34mCOMMIT[39;49;00m[37m [39;49;00m[34mTRAN[39;49;00m[37m[39;49;00m$
    66	[34mEND[39;49;00m[37m [39;49;00m[34mTRY[39;49;00m[37m[39;49;00m$
    67	[34mBEGIN[39;49;00m[37m [39;49;00m[34mCATCH[39;49;00m[37m[39;49;00m$
    68	[37m   [39;49;00m[34mprint[39;49;00m[37m [39;49;00m[33m'cannot perform transaction; rolling back'[39;49;00m;[37m[39;49;00m$
    69	[37m   [39;49;00m[34mROLLBACK[39;49;00m[37m [39;49;00m[34mTRAN[39;49;00m[37m[39;49;00m$
    70	[34mEND[39;49;00m[37m [39;49;00m[34mCATCH[39;49;00m[37m[39;49;00m$
    71	[37m[39;49;00m$
    72	[37m-- Comment at end without newline.[39;49;00m$

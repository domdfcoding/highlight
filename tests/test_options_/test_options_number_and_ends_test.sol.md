     1	[34mpragma solidity[39;49;00m[37m [39;49;00m^[34m0.4.20[39;49;00m;[37m[39;49;00m$
     2	[37m[39;49;00m$
     3	[34mpragma solidity[39;49;00m[37m [39;49;00m>=[34m0.4.0[39;49;00m[37m [39;49;00m<[34m0.7.0[39;49;00m;[37m[39;49;00m$
     4	[37m[39;49;00m$
     5	[37m// one-line singleline comment[39;49;00m$
     6	[37m[39;49;00m$
     7	[37m/* one-line multiline comment */[39;49;00m[37m[39;49;00m$
     8	[37m[39;49;00m$
     9	[37m/*[39;49;00m$
    10	[37m  multi-line multiline comment[39;49;00m$
    11	[37m*/[39;49;00m[37m[39;49;00m$
    12	[37m[39;49;00m$
    13	[34mcontract[39;49;00m[37m [39;49;00mContractName[37m [39;49;00m{[37m[39;49;00m$
    14	[37m[39;49;00m$
    15	[37m    [39;49;00m[36maddress[39;49;00m[37m [39;49;00m[34mpublic [39;49;00m[31mpublicaddress[39;49;00m;[37m[39;49;00m$
    16	[37m[39;49;00m$
    17	[37m    [39;49;00m[36muint[39;49;00m[37m [39;49;00m[31mvarname1[39;49;00m[37m [39;49;00m=[37m [39;49;00m[34m1234[39;49;00m;[37m[39;49;00m$
    18	[37m    [39;49;00m[36mint[39;49;00m[37m [39;49;00m[31mvarname2[39;49;00m[37m [39;49;00m=[37m [39;49;00m[34m0x12abcdEF[39;49;00m;[37m[39;49;00m$
    19	[37m[39;49;00m$
    20	[37m    [39;49;00m[36mstring[39;49;00m[37m [39;49;00m[31mastringsingle[39;49;00m[37m [39;49;00m=[37m [39;49;00m[33m'test "string" value\' single'[39;49;00m;[37m[39;49;00m$
    21	[37m    [39;49;00m[36mstring[39;49;00m[37m [39;49;00m[31mastringdouble[39;49;00m[37m [39;49;00m=[37m [39;49;00m[33m"test 'string' value\" double"[39;49;00m;[37m[39;49;00m$
    22	[37m[39;49;00m$
    23	[37m    [39;49;00m[36menum[39;49;00m[37m [39;49;00m[31mState[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
    24	[37m      [39;49;00mNotStarted,[37m[39;49;00m$
    25	[37m      [39;49;00mWorkInProgress,[37m[39;49;00m$
    26	[37m      [39;49;00mDone[37m[39;49;00m$
    27	[37m    [39;49;00m}[37m[39;49;00m$
    28	[37m    [39;49;00mState[37m [39;49;00m[36mpublic[39;49;00m[37m [39;49;00mstate;[37m[39;49;00m$
    29	[37m[39;49;00m$
    30	[37m    [39;49;00m[36mstruct[39;49;00m[37m [39;49;00m[31mAStruct[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
    31	[37m        [39;49;00m[36mstring[39;49;00m[37m [39;49;00m[31mname[39;49;00m;[37m[39;49;00m$
    32	[37m        [39;49;00m[36muint8[39;49;00m[37m [39;49;00m[31mtype[39;49;00m;[37m[39;49;00m$
    33	[37m    [39;49;00m}[37m[39;49;00m$
    34	[37m[39;49;00m$
    35	[37m    [39;49;00m[36mmapping[39;49;00m([36maddress[39;49;00m[37m [39;49;00m=>[37m [39;49;00mAStruct)[37m [39;49;00mregistry;[37m[39;49;00m$
    36	[37m[39;49;00m$
    37	[37m    [39;49;00m[36mevent[39;49;00m[37m [39;49;00m[31mPaid[39;49;00m([36muint256[39;49;00m[37m [39;49;00m[31mvalue[39;49;00m);[37m[39;49;00m$
    38	[37m    [39;49;00m[36mevent[39;49;00m[37m [39;49;00m[31mReceived[39;49;00m([36muint256[39;49;00m[37m [39;49;00m[31mtime[39;49;00m);[37m[39;49;00m$
    39	[37m    [39;49;00m[36mevent[39;49;00m[37m [39;49;00m[31mWithdraw[39;49;00m([36muint256[39;49;00m[37m [39;49;00m[31mvalue[39;49;00m);[37m[39;49;00m$
    40	[37m[39;49;00m$
    41	[37m    [39;49;00m[36mfunction[39;49;00m[37m [39;49;00m[31maddRegistry[39;49;00m([36mstring[39;49;00m[37m [39;49;00m[31m_name[39;49;00m,[37m [39;49;00m[36muint8[39;49;00m[37m [39;49;00m[31m_type[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
    42	[37m        [39;49;00mAStruct[37m [39;49;00m[36mmemory[39;49;00m[37m [39;49;00mnewItem[37m [39;49;00m=[37m [39;49;00mAStruct({[37m[39;49;00m$
    43	[37m            [39;49;00mname:[37m [39;49;00m_name,[37m[39;49;00m$
    44	[37m            [39;49;00mtype:[37m [39;49;00m_type[37m[39;49;00m$
    45	[37m        [39;49;00m});[37m[39;49;00m$
    46	[37m[39;49;00m$
    47	[37m        [39;49;00mregistry[[34mmsg.sender[39;49;00m][37m [39;49;00m=[37m [39;49;00mnewItem;[37m[39;49;00m$
    48	[37m    [39;49;00m}[37m[39;49;00m$
    49	[37m[39;49;00m$
    50	[37m    [39;49;00m[36mfunction[39;49;00m[37m [39;49;00m[31mgetHash[39;49;00m(AStruct[37m [39;49;00mitem)[37m [39;49;00m[36mreturns[39;49;00m([36muint[39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
    51	[37m        [39;49;00m[36mreturn[39;49;00m[37m [39;49;00m[36muint[39;49;00m([36mkeccak256[39;49;00m(item.name,[37m [39;49;00mitem.type));[37m[39;49;00m$
    52	[37m    [39;49;00m}[37m[39;49;00m$
    53	[37m[39;49;00m$
    54	[37m    [39;49;00m[36mfunction[39;49;00m[37m [39;49;00m[31mpay[39;49;00m()[37m [39;49;00m[36mpublic[39;49;00m[37m [39;49;00m[36mpayable[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
    55	[37m      [39;49;00m[36mrequire[39;49;00m([34mmsg.sender[39;49;00m[37m [39;49;00m==[37m [39;49;00mastronaut);[37m[39;49;00m$
    56	[37m      [39;49;00mstate[37m [39;49;00m=[37m [39;49;00mState.Paid;[37m[39;49;00m$
    57	[37m      [39;49;00mPaid([34mmsg.value[39;49;00m);[37m[39;49;00m$
    58	[37m    [39;49;00m}[37m[39;49;00m$
    59	[37m[39;49;00m$
    60	[37m    [39;49;00m[36mfunction[39;49;00m[37m [39;49;00m[31mreceive[39;49;00m()[37m [39;49;00m[36mpublic[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
    61	[37m      [39;49;00m[36mrequire[39;49;00m([34mmsg.sender[39;49;00m[37m [39;49;00m==[37m [39;49;00marbiter);[37m[39;49;00m$
    62	[37m      [39;49;00m[36mrequire[39;49;00m(state[37m [39;49;00m==[37m [39;49;00mState.Paid);[37m[39;49;00m$
    63	[37m      [39;49;00mstate[37m [39;49;00m=[37m [39;49;00mState.Received;[37m[39;49;00m$
    64	[37m      [39;49;00mReceived(now);[37m[39;49;00m$
    65	[37m    [39;49;00m}[37m[39;49;00m$
    66	[37m[39;49;00m$
    67	[37m    [39;49;00m[36mfunction[39;49;00m[37m [39;49;00m[31mwithdraw[39;49;00m()[37m [39;49;00m[36mpublic[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
    68	[37m      [39;49;00m[36mrequire[39;49;00m([34mmsg.sender[39;49;00m[37m [39;49;00m==[37m [39;49;00mshipper);[37m[39;49;00m$
    69	[37m      [39;49;00m[36mrequire[39;49;00m(state[37m [39;49;00m==[37m [39;49;00mState.Received);[37m[39;49;00m$
    70	[37m      [39;49;00mstate[37m [39;49;00m=[37m [39;49;00mState.Withdrawn;[37m[39;49;00m$
    71	[37m      [39;49;00mWithdraw([36mthis[39;49;00m.balance);[37m[39;49;00m$
    72	[37m      [39;49;00mshipper.transfer([36mthis[39;49;00m.balance);[37m[39;49;00m$
    73	[37m    [39;49;00m}[37m[39;49;00m$
    74	}$

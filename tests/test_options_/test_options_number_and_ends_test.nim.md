     1	[34mimport[39;49;00m re$
     2	$
     3	[34mfor[39;49;00m x [35min[39;49;00m lines([33m"[39;49;00m[33mmyfile.txt[39;49;00m[33m"[39;49;00m):$
     4	  [34mif[39;49;00m x =~ [33mre"[39;49;00m[33m([39;49;00m[33m\[39;49;00m[33mw+)=(.*)[39;49;00m[33m"[39;49;00m:$
     5	    echo [33m"[39;49;00m[33mKey: [39;49;00m[33m"[39;49;00m, matches[[34m0[39;49;00m],$
     6	         [33m"[39;49;00m[33m Value: [39;49;00m[33m"[39;49;00m, matches[[34m1[39;49;00m]$
     7	$
     8	Echo([33m"[39;49;00m[33mWhat[39;49;00m[33m'[39;49;00m[33ms your name? [39;49;00m[33m"[39;49;00m)$
     9	[34mvar[39;49;00m name: [36mstring[39;49;00m = readLine(stdin)$
    10	[34mif[39;49;00m name == [33m"[39;49;00m[33m"[39;49;00m:$
    11	  echo([33m"[39;49;00m[33mPoor soul, you lost your name?[39;49;00m[33m"[39;49;00m)$
    12	[34melif[39;49;00m name == [33m"[39;49;00m[33mname[39;49;00m[33m"[39;49;00m:$
    13	  echo([33m"[39;49;00m[33mVery funny, your name is name.[39;49;00m[33m"[39;49;00m)$
    14	[34melse[39;49;00m:$
    15	  Echo([33m"[39;49;00m[33mHi, [39;49;00m[33m"[39;49;00m, name, [33m"[39;49;00m[33m![39;49;00m[33m"[39;49;00m)$
    16	$
    17	[34mvar[39;49;00m name = readLine(stdin)$
    18	[34mcase[39;49;00m name$
    19	[34mof[39;49;00m [33m"[39;49;00m[33m"[39;49;00m:$
    20	  echo([33m"[39;49;00m[33mPoor soul, you lost your name?[39;49;00m[33m"[39;49;00m)$
    21	[34mof[39;49;00m [33m"[39;49;00m[33mname[39;49;00m[33m"[39;49;00m:$
    22	  echo([33m"[39;49;00m[33mVery funny, your name is name.[39;49;00m[33m"[39;49;00m)$
    23	[34melse[39;49;00m:$
    24	  Echo([33m"[39;49;00m[33mHi, [39;49;00m[33m"[39;49;00m, name, [33m"[39;49;00m[33m![39;49;00m[33m"[39;49;00m)$
    25	$
    26	[34mfrom[39;49;00m strutils [34mimport[39;49;00m parseInt$
    27	$
    28	Echo([33m"[39;49;00m[33mA number please: [39;49;00m[33m"[39;49;00m)$
    29	[34mvar[39;49;00m n = parseInt(readLine(stdin))$
    30	[34mcase[39;49;00m n$
    31	[34mof[39;49;00m [34m0[39;49;00m..[34m2[39;49;00m, [34m4[39;49;00m..[34m7[39;49;00m: Echo([33m"[39;49;00m[33mThe number is in the set: {0, 1, 2, 4, 5, 6, 7}[39;49;00m[33m"[39;49;00m)$
    32	[34mof[39;49;00m [34m3[39;49;00m, [34m8[39;49;00m: Echo([33m"[39;49;00m[33mThe number is 3 or 8[39;49;00m[33m"[39;49;00m)$
    33	$
    34	Echo([33m"[39;49;00m[33mCounting to 10: [39;49;00m[33m"[39;49;00m)$
    35	[34mvar[39;49;00m i = [34m1[39;49;00m$
    36	[34mwhile[39;49;00m i <= [34m10[39;49;00m:$
    37	  Echo($i)$
    38	  inc(i)$
    39	$
    40	[34mproc [39;49;00m[32myes[39;49;00m(question: [36mstring[39;49;00m): [36mbool[39;49;00m =$
    41	  Echo(question, [33m"[39;49;00m[33m (y/n)[39;49;00m[33m"[39;49;00m)$
    42	  [34mwhile[39;49;00m [34mtrue[39;49;00m:$
    43	    [34mcase[39;49;00m readLine(stdin)$
    44	    [34mof[39;49;00m [33m"[39;49;00m[33my[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mY[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33myes[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mYes[39;49;00m[33m"[39;49;00m: [34mreturn[39;49;00m [34mtrue[39;49;00m$
    45	    [34mof[39;49;00m [33m"[39;49;00m[33mn[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mN[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mno[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mNo[39;49;00m[33m"[39;49;00m: [34mreturn[39;49;00m [34mfalse[39;49;00m$
    46	    [34melse[39;49;00m: Echo([33m"[39;49;00m[33mPlease be clear: yes or no[39;49;00m[33m"[39;49;00m)$
    47	$
    48	[34mproc [39;49;00m[32meven[39;49;00m(n: [36mint[39;49;00m): [36mbool[39;49;00m$
    49	$
    50	[34mproc [39;49;00m[32modd[39;49;00m(n: [36mint[39;49;00m): [36mbool[39;49;00m =$
    51	  [34mif[39;49;00m n == [34m1[39;49;00m: [34mreturn[39;49;00m [34mtrue[39;49;00m$
    52	  [34melse[39;49;00m: [34mreturn[39;49;00m even(n-[34m1[39;49;00m)$
    53	$
    54	[34miterator[39;49;00m countup(a, b: [36mint[39;49;00m): [36mint[39;49;00m =$
    55	  [34mvar[39;49;00m res = a$
    56	  [34mwhile[39;49;00m res <= b:$
    57	    [34myield[39;49;00m res$
    58	    inc(res)$
    59	$
    60	[34mtype[39;49;00m$
    61	  TPerson = [34mobject[39;49;00m [34mof[39;49;00m TObject$
    62	    name*: [36mstring[39;49;00m  [37m# the * means that `name` is accessible from other modules[39;49;00m$
    63	    age: [36mint[39;49;00m       [37m# no * means that the field is hidden from other modules[39;49;00m$
    64	$
    65	  TStudent = [34mobject[39;49;00m [34mof[39;49;00m TPerson [37m# TStudent inherits from TPerson[39;49;00m$
    66	    id: [36mint[39;49;00m                    [37m# with an id field[39;49;00m$
    67	$
    68	[34mvar[39;49;00m$
    69	  student: TStudent$
    70	  person: TPerson$
    71	assert(student [35mis[39;49;00m TStudent)$
    72	$
    73	echo({[33m'[39;49;00m[33ma[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mb[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mc[39;49;00m[33m'[39;49;00m}.card)$
    74	stdout.writeln([33m"[39;49;00m[33mHallo[39;49;00m[33m"[39;49;00m)$
    75	[34mvar[39;49;00m$
    76	  f: TFile$
    77	[34mif[39;49;00m open(f, [33m"[39;49;00m[33mnumbers.txt[39;49;00m[33m"[39;49;00m):$
    78	  [34mtry[39;49;00m:$
    79	    [34mvar[39;49;00m a = readLine(f)$
    80	    [34mvar[39;49;00m b = readLine(f)$
    81	    echo([33m"[39;49;00m[33msum: [39;49;00m[33m"[39;49;00m & $(parseInt(a) + parseInt(b)))$
    82	  [34mexcept[39;49;00m EOverflow:$
    83	    echo([33m"[39;49;00m[33moverflow![39;49;00m[33m"[39;49;00m)$
    84	  [34mexcept[39;49;00m EInvalidValue:$
    85	    echo([33m"[39;49;00m[33mcould not convert string to integer[39;49;00m[33m"[39;49;00m)$
    86	  [34mexcept[39;49;00m EIO:$
    87	    echo([33m"[39;49;00m[33mIO error![39;49;00m[33m"[39;49;00m)$
    88	  [34mexcept[39;49;00m:$
    89	    echo([33m"[39;49;00m[33mUnknown exception![39;49;00m[33m"[39;49;00m)$
    90	    [37m# reraise the unknown exception:[39;49;00m$
    91	    [34mraise[39;49;00m$
    92	  [34mfinally[39;49;00m:$
    93	    close(f)$

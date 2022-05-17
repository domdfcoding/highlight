     1	[33m/[39;49;00m[33m[39;49;00m
     2	[33mthis is a[39;49;00m
     3	[33mmultiline[39;49;00m
     4	[33mregex[39;49;00m
     5	[33m/[39;49;00m
     6
     7	this [33m/[39;49;00m[33mis a[39;49;00m
     8	[33mmultiline regex too[39;49;00m[33m/[39;49;00m
     9
    10	foo = [33m/[39;49;00m[33mis also[39;49;00m
    11	[33mone[39;49;00m[33m/[39;49;00m
    12
    13	also [33m/[39;49;00m[33m4[39;49;00m
    14	[33mis one[39;49;00m[33m/[39;49;00m
    15
    16	this([33m/[39;49;00m[33m[39;49;00m
    17	[33mtoo[39;49;00m
    18	[33m/[39;49;00m)
    19
    20	[37m# this not[39;49;00m
    21	[34m2[39;49;00m /[34m4[39;49;00m
    22	asfsadf/
    23
    24	[37m# this is also not one[39;49;00m
    25	[34m0x4d[39;49;00m /[34m25[39;49;00m
    26	foo/
    27
    28	[34m42[39;49;00m [35mand[39;49;00m [33m/[39;49;00m[33mthis[39;49;00m
    29	[33mis also a multiline[39;49;00m
    30	[33mregex[39;49;00m[33m/[39;49;00m
    31
    32
    33	[37m# And here some special string cases[39;49;00m
    34	foo = [33m% blah [39;49;00m           [37m# comment here to ensure whitespace[39;49;00m
    35	foo([33m% blah [39;49;00m)
    36	foo << [33m% blah [39;49;00m          [37m# stupid but has to work[39;49;00m
    37	foo = [33m% blah [39;49;00m+ [33m% blub [39;49;00m  [37m# wicked[39;49;00m
    38	foo = [33m%q wicked [39;49;00m        [37m# works too[39;49;00m

     1^I[33m/[39;49;00m[33m[39;49;00m$
     2^I[33mthis is a[39;49;00m$
     3^I[33mmultiline[39;49;00m$
     4^I[33mregex[39;49;00m$
     5^I[33m/[39;49;00m$
     6^I$
     7^Ithis [33m/[39;49;00m[33mis a[39;49;00m$
     8^I[33mmultiline regex too[39;49;00m[33m/[39;49;00m$
     9^I$
    10^Ifoo = [33m/[39;49;00m[33mis also[39;49;00m$
    11^I[33mone[39;49;00m[33m/[39;49;00m$
    12^I$
    13^Ialso [33m/[39;49;00m[33m4[39;49;00m$
    14^I[33mis one[39;49;00m[33m/[39;49;00m$
    15^I$
    16^Ithis([33m/[39;49;00m[33m[39;49;00m$
    17^I[33mtoo[39;49;00m$
    18^I[33m/[39;49;00m)$
    19^I$
    20^I[37m# this not[39;49;00m$
    21^I[34m2[39;49;00m /[34m4[39;49;00m$
    22^Iasfsadf/$
    23^I$
    24^I[37m# this is also not one[39;49;00m$
    25^I[34m0x4d[39;49;00m /[34m25[39;49;00m$
    26^Ifoo/$
    27^I$
    28^I[34m42[39;49;00m [35mand[39;49;00m [33m/[39;49;00m[33mthis[39;49;00m$
    29^I[33mis also a multiline[39;49;00m$
    30^I[33mregex[39;49;00m[33m/[39;49;00m$
    31^I$
    32^I$
    33^I[37m# And here some special string cases[39;49;00m$
    34^Ifoo = [33m% blah [39;49;00m           [37m# comment here to ensure whitespace[39;49;00m$
    35^Ifoo([33m% blah [39;49;00m)$
    36^Ifoo << [33m% blah [39;49;00m          [37m# stupid but has to work[39;49;00m$
    37^Ifoo = [33m% blah [39;49;00m+ [33m% blub [39;49;00m  [37m# wicked[39;49;00m$
    38^Ifoo = [33m%q wicked [39;49;00m        [37m# works too[39;49;00m$

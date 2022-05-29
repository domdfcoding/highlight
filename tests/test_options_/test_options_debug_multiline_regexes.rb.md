Using lexer <pygments.lexers.RubyLexer with {'ensurenl': False, 'tabsize': 0}>
[33m/[39;49;00m[33m[39;49;00m
[33mthis is a[39;49;00m
[33mmultiline[39;49;00m
[33mregex[39;49;00m
[33m/[39;49;00m

this [33m/[39;49;00m[33mis a[39;49;00m
[33mmultiline regex too[39;49;00m[33m/[39;49;00m

foo = [33m/[39;49;00m[33mis also[39;49;00m
[33mone[39;49;00m[33m/[39;49;00m

also [33m/[39;49;00m[33m4[39;49;00m
[33mis one[39;49;00m[33m/[39;49;00m

this([33m/[39;49;00m[33m[39;49;00m
[33mtoo[39;49;00m
[33m/[39;49;00m)

[37m# this not[39;49;00m
[34m2[39;49;00m /[34m4[39;49;00m
asfsadf/

[37m# this is also not one[39;49;00m
[34m0x4d[39;49;00m /[34m25[39;49;00m
foo/

[34m42[39;49;00m [35mand[39;49;00m [33m/[39;49;00m[33mthis[39;49;00m
[33mis also a multiline[39;49;00m
[33mregex[39;49;00m[33m/[39;49;00m


[37m# And here some special string cases[39;49;00m
foo = [33m% blah [39;49;00m           [37m# comment here to ensure whitespace[39;49;00m
foo([33m% blah [39;49;00m)
foo << [33m% blah [39;49;00m          [37m# stupid but has to work[39;49;00m
foo = [33m% blah [39;49;00m+ [33m% blub [39;49;00m  [37m# wicked[39;49;00m
foo = [33m%q wicked [39;49;00m        [37m# works too[39;49;00m

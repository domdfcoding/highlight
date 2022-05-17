     1^I   ## a comment$
     2^I$
     3^I\## not a comment$
     4^I$
     5^I#if foo$
     6^I  [36m${[39;49;00mbar[36m}[39;49;00m$
     7^I#endif$
     8^I$
     9^IThe answer is:$
    10^I#choose$
    11^I  #when 0 == 1$
    12^I    0$
    13^I  #end$
    14^I  #when 1 == 1$
    15^I    1$
    16^I  #end$
    17^I  #otherwise$
    18^I    2$
    19^I  #end$
    20^I#end -- comment about choose$
    21^I$
    22^I#for item in items$
    23^I  * [36m${[39;49;00mitem[36m}[39;49;00m$
    24^I#end$
    25^I$
    26^I#def greeting(name)$
    27^I  Hello, [36m${[39;49;00mname[36m}[39;49;00m!$
    28^I#end$
    29^I[36m${[39;49;00mgreeting([33m'[39;49;00m[33mworld[39;49;00m[33m'[39;49;00m)[36m}[39;49;00m$
    30^I$
    31^I#with y=7; z=x+10$
    32^I  [31m$x[39;49;00m [31m$y[39;49;00m [31m$z[39;49;00m$
    33^I#end$

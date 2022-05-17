   ## a comment$
$
\## not a comment$
$
#if foo$
  [36m${[39;49;00mbar[36m}[39;49;00m$
#endif$
$
The answer is:$
#choose$
  #when 0 == 1$
    0$
  #end$
  #when 1 == 1$
    1$
  #end$
  #otherwise$
    2$
  #end$
#end -- comment about choose$
$
#for item in items$
  * [36m${[39;49;00mitem[36m}[39;49;00m$
#end$
$
#def greeting(name)$
  Hello, [36m${[39;49;00mname[36m}[39;49;00m!$
#end$
[36m${[39;49;00mgreeting([33m'[39;49;00m[33mworld[39;49;00m[33m'[39;49;00m)[36m}[39;49;00m$
$
#with y=7; z=x+10$
  [31m$x[39;49;00m [31m$y[39;49;00m [31m$z[39;49;00m$
#end$

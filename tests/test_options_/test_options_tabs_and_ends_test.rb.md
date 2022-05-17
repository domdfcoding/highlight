a.each{|el|anz[el]=anz[el]?anz[el]+[34m1[39;49;00m:[34m1[39;49;00m}$
[34mwhile[39;49;00m x<[34m10000[39;49;00m$
[37m#a bis f dienen dazu die Nachbarschaft festzulegen. Man stelle sich die #Zahl von 1 bis 64 im Binärcode vor 1 bedeutet an 0 aus[39;49;00m$
  b=([36mp[39;49;00m[x]%[34m32[39;49;00m)/[34m16[39;49;00m<[34m1[39;49;00m ? [34m0[39;49;00m : [34m1[39;49;00m$
$
  (x-[34m102[39;49;00m>=[34m0[39;49;00m? n[x-[34m102[39;49;00m].to_i : [34m0[39;49;00m)*a+(x-[34m101[39;49;00m>=[34m0[39;49;00m?n[x-[34m101[39;49;00m].to_i : [34m0[39;49;00m)*e+n[x-[34m100[39;49;00m].to_i+(x-[34m99[39;49;00m>=[34m0[39;49;00m? n[x-[34m99[39;49;00m].to_i : [34m0[39;49;00m)*f+(x-[34m98[39;49;00m>=[34m0[39;49;00m? n[x-[34m98[39;49;00m].to_i : [34m0[39;49;00m)*a+$
  n[x+[34m199[39;49;00m].to_i*b+n[x+[34m200[39;49;00m].to_i*d+n[x+[34m201[39;49;00m].to_i*b$
$
[37m#und die Ausgabe folgt[39;49;00m$
g=[33m%w{[39;49;00m[33m}[39;49;00m$
x=[34m0[39;49;00m$
$
[37m#leere regex[39;49;00m$
[36mtest[39;49;00m [33m/[39;49;00m[33m/[39;49;00m, [34m123[39;49;00m$
$
[34mwhile[39;49;00m x<[34m100[39;49;00m$
 [36mputs[39;49;00m[33m"[39;49;00m[33m#{[39;49;00mg[x][33m}[39;49;00m[33m"[39;49;00m$
 x+=[34m1[39;49;00m$
[34mend[39;49;00m$
$
[36mputs[39;49;00m[33m"[39;49;00m[33m"[39;49;00m$
[36msleep[39;49;00m([34m10[39;49;00m)$
$
[34m1[39;49;00m[31mE1E1[39;49;00m$
[36mputs[39;49;00m [34m30[39;49;00m.send([33m:/[39;49;00m, [34m5[39;49;00m) [37m# prints 6[39;49;00m$
$
[37m# fun with class attributes[39;49;00m$
[34mclass[39;49;00m [04m[32mFoo[39;49;00m$
  [34mdef[39;49;00m [04m[32mself[39;49;00m.[32mblub[39;49;00m x$
    [34mif[39;49;00m [35mnot[39;49;00m x.nil?$
      [36mself[39;49;00m.new$
    [34mend[39;49;00m$
  [34mend[39;49;00m$
  [34mdef[39;49;00m [32manother_way_to_get_class[39;49;00m$
    [36mself[39;49;00m.class$
  [34mend[39;49;00m$
[34mend[39;49;00m$
$
[37m# ruby 1.9 "call operator"[39;49;00m$
a = [31mProc[39;49;00m.new { [34m42[39;49;00m }$
a.()$
$
[33m"[39;49;00m[33minstance variables can be [39;49;00m[33m#@included[39;49;00m[33m, [39;49;00m[33m#@@class_variables[39;49;00m[33m\n[39;49;00m[33m and [39;49;00m[33m#$globals[39;49;00m[33m as well.[39;49;00m[33m"[39;49;00m$
[33m`[39;49;00m[33minstance variables can be [39;49;00m[33m#@included[39;49;00m[33m, [39;49;00m[33m#@@class_variables[39;49;00m[33m\n[39;49;00m[33m and [39;49;00m[33m#$globals[39;49;00m[33m as well.[39;49;00m[33m`[39;49;00m$
[33m'[39;49;00m[33minstance variables can be [39;49;00m[33m#@included[39;49;00m[33m, [39;49;00m[33m#@@class_variables[39;49;00m[33m\n[39;49;00m[33m and [39;49;00m[33m#$globals[39;49;00m[33m as well.[39;49;00m[33m'[39;49;00m$
[33m/[39;49;00m[33minstance variables can be [39;49;00m[33m#@included[39;49;00m[33m, [39;49;00m[33m#@@class_variables[39;49;00m[33m\[39;49;00m[33mn and [39;49;00m[33m#$globals[39;49;00m[33m as well.[39;49;00m[33m/mousenix[39;49;00m$
[33m:"[39;49;00m[33minstance variables can be [39;49;00m[33m#@included[39;49;00m[33m, [39;49;00m[33m#@@class_variables[39;49;00m[33m\n[39;49;00m[33m and [39;49;00m[33m#$globals[39;49;00m[33m as well.[39;49;00m[33m"[39;49;00m$
[33m:'instance variables can be #@included, #@@class_variables\n and #$globals as well.'[39;49;00m$
[33m%'[39;49;00m[33minstance variables can be [39;49;00m[33m#@included[39;49;00m[33m, [39;49;00m[33m#@@class_variables[39;49;00m[33m\[39;49;00m[33mn and [39;49;00m[33m#$globals[39;49;00m[33m as well.[39;49;00m[33m'[39;49;00m$
[33m%q'instance variables can be #@included, #@@class_variables\n and #$globals as well.'[39;49;00m$
[33m%Q'[39;49;00m[33minstance variables can be [39;49;00m[33m#@included[39;49;00m[33m, [39;49;00m[33m#@@class_variables[39;49;00m[33m\[39;49;00m[33mn and [39;49;00m[33m#$globals[39;49;00m[33m as well.[39;49;00m[33m'[39;49;00m$
[33m%w'instance variables can be #@included, #@@class_variables\n and #$globals as well.'[39;49;00m$
[33m%W'[39;49;00m[33minstance variables can be [39;49;00m[33m#@included[39;49;00m[33m, [39;49;00m[33m#@@class_variables[39;49;00m[33m\[39;49;00m[33mn and [39;49;00m[33m#$globals[39;49;00m[33m as well.[39;49;00m[33m'[39;49;00m$
[33m%s'instance variables can be #@included, #@@class_variables\n and #$globals as well.'[39;49;00m$
[33m%r'[39;49;00m[33minstance variables can be [39;49;00m[33m#@included[39;49;00m[33m, [39;49;00m[33m#@@class_variables[39;49;00m[33m\[39;49;00m[33mn and [39;49;00m[33m#$globals[39;49;00m[33m as well.[39;49;00m[33m'[39;49;00m$
[33m%x'[39;49;00m[33minstance variables can be [39;49;00m[33m#@included[39;49;00m[33m, [39;49;00m[33m#@@class_variables[39;49;00m[33m\[39;49;00m[33mn and [39;49;00m[33m#$globals[39;49;00m[33m as well.[39;49;00m[33m'[39;49;00m$
$
[37m#%W[ but #@0illegal_values look strange.][39;49;00m$
$
[33m%s#ruby allows strange#[39;49;00m{constructs}$
[33m%s#ruby allows strange#[39;49;00m[31m$constructs[39;49;00m$
[33m%s#ruby allows strange#[39;49;00m[31m@@constructs[39;49;00m$
$
[37m##################################################################[39;49;00m$
[37m# HEREDOCS[39;49;00m$
foo(<<-[33mA[39;49;00m, <<-[33mB[39;49;00m)$
[33mthis is the text of a[39;49;00m$
[33mA[39;49;00m$
[33mand this is the text of b[39;49;00m$
[33mB[39;49;00m$
$
a = <<[33m"[39;49;00m[33mEOF[39;49;00m[33m"[39;49;00m$
[33mThis is a multiline #$here document[39;49;00m$
[33mterminated by EOF on a line by itself[39;49;00m$
[33mEOF[39;49;00m$
$
a = <<[33m'[39;49;00m[33mEOF[39;49;00m[33m'[39;49;00m$
[33mThis is a multiline #$here document[39;49;00m$
[33mterminated by EOF on a line by itself[39;49;00m$
[33mEOF[39;49;00m$
$
b=([36mp[39;49;00m[x] %[34m32[39;49;00m)/[34m16[39;49;00m<[34m1[39;49;00m ? [34m0[39;49;00m : [34m1[39;49;00m$
$
<<[33m"[39;49;00m[33m"[39;49;00m$
[33m#{test}[39;49;00m$
[33m#@bla[39;49;00m$
[33m#die suppe!!![39;49;00m$
[33m\xfffff[39;49;00m$
[33m[39;49;00m$
$
[34msuper[39;49;00m <<-[33mEOE[39;49;00m % [$
[33m    foo[39;49;00m$
[33mEOE[39;49;00m$
$
<<[33mX[39;49;00m$
[33mX[39;49;00m$
X$
$
[33m%s([39;49;00m[33muninter[39;49;00m[33m\)[39;49;00m[33mpre[39;49;00m[33m\[39;49;00m[33mted[39;49;00m[33m)[39;49;00m            [37m# comment here[39;49;00m$
[33m%q([39;49;00m[33muninter[39;49;00m[33m\)[39;49;00m[33mpre[39;49;00m[33m\[39;49;00m[33mted[39;49;00m[33m)[39;49;00m            [37m# comment here[39;49;00m$
[33m%Q([39;49;00m[33minter[39;49;00m[33m\)[39;49;00m[33mpre[39;49;00m[33m\t[39;49;00m[33med[39;49;00m[33m)[39;49;00m              [37m# comment here[39;49;00m$
[33m:"[39;49;00m[33minter[39;49;00m[33m\[39;49;00m[33m)pre[39;49;00m[33m\t[39;49;00m[33med[39;49;00m[33m"[39;49;00m               [37m# comment here[39;49;00m$
[33m:'uninter\'pre\ted'[39;49;00m             [37m# comment here[39;49;00m$
$
[33m%q[[39;49;00m[33mhaha! [39;49;00m[33m[[39;49;00m[33mnesting [39;49;00m[33m[[39;49;00m[33mrocks[39;49;00m[33m][39;49;00m[33m ! [39;49;00m[33m][39;49;00m[33m [39;49;00m[33m][39;49;00m [37m# commeht here[39;49;00m$
$
$
[37m##################################################################[39;49;00m$
[34mclass[39;49;00m                                                  [04m[32mNP[39;49;00m$
[34mdef[39;49;00m  [32minitialize[39;49;00m a=[31m@p[39;49;00m=[], b=[31m@b[39;49;00m=[];                      [34mend[39;49;00m$
[34mdef[39;49;00m [32m+@[39;49;00m;[31m@b[39;49;00m<<[34m1[39;49;00m;b2c [34mend[39;49;00m;[34mdef[39;49;00m[32m-@[39;49;00m;[31m@b[39;49;00m<<[34m0[39;49;00m;b2c                   [34mend[39;49;00m$
[34mdef[39;49;00m  [32mb2c[39;49;00m;[34mif[39;49;00m [31m@b[39;49;00m.size==[34m8[39;49;00m;c=[34m0[39;49;00m;[31m@b[39;49;00m.each{|b|c<<=[34m1[39;49;00m;c|=b};[36msend[39;49;00m($
     [33m'[39;49;00m[33mlave[39;49;00m[33m'[39;49;00m.reverse,([31m@p[39;49;00m.join))[34mif[39;49;00m c==[34m0[39;49;00m;[31m@p[39;49;00m<< c.chr;[31m@b[39;49;00m=[] [34mend[39;49;00m$
     [36mself[39;49;00m [34mend[39;49;00m [34mend[39;49;00m ; [34mbegin[39;49;00m _ = [31mNP[39;49;00m.new                   [34mend[39;49;00m$
$
$
[37m# Regexes[39;49;00m$
[33m/[39;49;00m[33m[39;49;00m$
[33mthis is a[39;49;00m$
[33mmutliline[39;49;00m$
[33mregex[39;49;00m$
[33m/[39;49;00m$
$
this [33m/[39;49;00m[33mis a[39;49;00m$
[33mmultiline regex too[39;49;00m[33m/[39;49;00m$
$
also [33m/[39;49;00m[33m4[39;49;00m$
[33mis one[39;49;00m[33m/[39;49;00m$
$
this([33m/[39;49;00m[33m[39;49;00m$
[33mtoo[39;49;00m$
[33m/[39;49;00m)$
$
[37m# this not[39;49;00m$
[34m2[39;49;00m /[34m4[39;49;00m$
asfsadf/$
$
$
[37m#from: http://coderay.rubychan.de/rays/show/383[39;49;00m$
[34mclass[39;49;00m [04m[32mObject[39;49;00m$
  [34malias[39;49;00m  [33m:xeq[39;49;00m [33m:`[39;49;00m$
  [34mdef[39;49;00m [32m`[39;49;00m(cmd, p2)$
    [36mself[39;49;00m.method(cmd.to_sym).call(p2)$
  [34mend[39;49;00m$
[34mend[39;49;00m$
[36mp[39;49;00m [[34m1[39;49;00m,[34m2[39;49;00m,[34m3[39;49;00m].`([33m'[39;49;00m[33mconcat[39;49;00m[33m'[39;49;00m, [[34m4[39;49;00m,[34m5[39;49;00m,[34m6[39;49;00m]) [37m# => [1, 2, 3, 4, 5, 6][39;49;00m$
[36mp[39;49;00m [[34m1[39;49;00m,[34m2[39;49;00m,[34m3[39;49;00m].`([33m:concat[39;49;00m, [[34m4[39;49;00m,[34m5[39;49;00m,[34m6[39;49;00m]) [37m# => [1, 2, 3, 4, 5, 6][39;49;00m$
[36mp[39;49;00m [33m"[39;49;00m[33mHurra! [39;49;00m[33m"[39;49;00m.`([33m:*[39;49;00m, [34m3[39;49;00m) [37m# => "Hurra! Hurra! Hurra! "[39;49;00m$
[36mp[39;49;00m [33m"[39;49;00m[33mHurra! [39;49;00m[33m"[39;49;00m.`([33m'[39;49;00m[33m*[39;49;00m[33m'[39;49;00m, [34m3[39;49;00m) [37m# => "Hurra! Hurra! Hurra! "[39;49;00m$
[37m# Leider geht nicht die Wunschform[39;49;00m$
[37m# [1,2,3] `concat` [4,5,6][39;49;00m$
$
[34mclass[39;49;00m [04m[32mObject[39;49;00m$
  [31m@@infixops[39;49;00m = []$
  [34malias[39;49;00m [33m:xeq[39;49;00m [33m:`[39;49;00m$
  [34mdef[39;49;00m [32maddinfix[39;49;00m(operator)$
    [31m@@infixops[39;49;00m << operator$
  [34mend[39;49;00m$
  [34mdef[39;49;00m [32m`[39;49;00m(expression)$
    [31m@@infixops[39;49;00m.each{|op|[34mbreak[39;49;00m [34mif[39;49;00m expression.match([33m/[39;49;00m[33m^(.*?) ([39;49;00m[33m#{[39;49;00mop[33m}[39;49;00m[33m) (.*)$[39;49;00m[33m/[39;49;00m)}$
    [34mraise[39;49;00m [33m"[39;49;00m[33munknown infix operator in expression: [39;49;00m[33m#{[39;49;00mexpression[33m}[39;49;00m[33m"[39;49;00m [34mif[39;49;00m [31m$2[39;49;00m == [34mnil[39;49;00m$
    [36meval[39;49;00m([31m$1[39;49;00m).method([31m$2[39;49;00m.to_sym).call([36meval[39;49;00m([31m$3[39;49;00m))$
  [34mend[39;49;00m$
[34mend[39;49;00m$
addinfix([33m"[39;49;00m[33mconcat[39;49;00m[33m"[39;49;00m)$
[36mp[39;49;00m [33m`[39;49;00m[33m[1,2,3] concat [4,5,6][39;49;00m[33m`[39;49;00m [37m# => [1, 2, 3, 4, 5, 6][39;49;00m$
$
$
[37m# HEREDOC FUN!!!!!!!1111[39;49;00m$
foo(<<[33mA[39;49;00m, <<-[33mB[39;49;00m, <<[33mC[39;49;00m)$
[33mthis is the text of a[39;49;00m$
[33m   A!!!![39;49;00m$
[33mA[39;49;00m$
[33mand this is text of B!!!!!!111[39;49;00m$
[33m   B[39;49;00m$
[04m[91mand here some C[39;49;00m$
[35mand[39;49;00m here some C$
C$

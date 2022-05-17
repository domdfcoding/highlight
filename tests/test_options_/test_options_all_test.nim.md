     1^I[34mimport[39;49;00m re$
     2^I$
     3^I[34mfor[39;49;00m x [35min[39;49;00m lines([33m"[39;49;00m[33mmyfile.txt[39;49;00m[33m"[39;49;00m):$
     4^I  [34mif[39;49;00m x =~ [33mre"[39;49;00m[33m([39;49;00m[33m\[39;49;00m[33mw+)=(.*)[39;49;00m[33m"[39;49;00m:$
     5^I    echo [33m"[39;49;00m[33mKey: [39;49;00m[33m"[39;49;00m, matches[[34m0[39;49;00m],$
     6^I         [33m"[39;49;00m[33m Value: [39;49;00m[33m"[39;49;00m, matches[[34m1[39;49;00m]$
     7^I$
     8^IEcho([33m"[39;49;00m[33mWhat[39;49;00m[33m'[39;49;00m[33ms your name? [39;49;00m[33m"[39;49;00m)$
     9^I[34mvar[39;49;00m name: [36mstring[39;49;00m = readLine(stdin)$
    10^I[34mif[39;49;00m name == [33m"[39;49;00m[33m"[39;49;00m:$
    11^I  echo([33m"[39;49;00m[33mPoor soul, you lost your name?[39;49;00m[33m"[39;49;00m)$
    12^I[34melif[39;49;00m name == [33m"[39;49;00m[33mname[39;49;00m[33m"[39;49;00m:$
    13^I  echo([33m"[39;49;00m[33mVery funny, your name is name.[39;49;00m[33m"[39;49;00m)$
    14^I[34melse[39;49;00m:$
    15^I  Echo([33m"[39;49;00m[33mHi, [39;49;00m[33m"[39;49;00m, name, [33m"[39;49;00m[33m![39;49;00m[33m"[39;49;00m)$
    16^I$
    17^I[34mvar[39;49;00m name = readLine(stdin)$
    18^I[34mcase[39;49;00m name$
    19^I[34mof[39;49;00m [33m"[39;49;00m[33m"[39;49;00m:$
    20^I  echo([33m"[39;49;00m[33mPoor soul, you lost your name?[39;49;00m[33m"[39;49;00m)$
    21^I[34mof[39;49;00m [33m"[39;49;00m[33mname[39;49;00m[33m"[39;49;00m:$
    22^I  echo([33m"[39;49;00m[33mVery funny, your name is name.[39;49;00m[33m"[39;49;00m)$
    23^I[34melse[39;49;00m:$
    24^I  Echo([33m"[39;49;00m[33mHi, [39;49;00m[33m"[39;49;00m, name, [33m"[39;49;00m[33m![39;49;00m[33m"[39;49;00m)$
    25^I$
    26^I[34mfrom[39;49;00m strutils [34mimport[39;49;00m parseInt$
    27^I$
    28^IEcho([33m"[39;49;00m[33mA number please: [39;49;00m[33m"[39;49;00m)$
    29^I[34mvar[39;49;00m n = parseInt(readLine(stdin))$
    30^I[34mcase[39;49;00m n$
    31^I[34mof[39;49;00m [34m0[39;49;00m..[34m2[39;49;00m, [34m4[39;49;00m..[34m7[39;49;00m: Echo([33m"[39;49;00m[33mThe number is in the set: {0, 1, 2, 4, 5, 6, 7}[39;49;00m[33m"[39;49;00m)$
    32^I[34mof[39;49;00m [34m3[39;49;00m, [34m8[39;49;00m: Echo([33m"[39;49;00m[33mThe number is 3 or 8[39;49;00m[33m"[39;49;00m)$
    33^I$
    34^IEcho([33m"[39;49;00m[33mCounting to 10: [39;49;00m[33m"[39;49;00m)$
    35^I[34mvar[39;49;00m i = [34m1[39;49;00m$
    36^I[34mwhile[39;49;00m i <= [34m10[39;49;00m:$
    37^I  Echo($i)$
    38^I  inc(i)$
    39^I$
    40^I[34mproc [39;49;00m[32myes[39;49;00m(question: [36mstring[39;49;00m): [36mbool[39;49;00m =$
    41^I  Echo(question, [33m"[39;49;00m[33m (y/n)[39;49;00m[33m"[39;49;00m)$
    42^I  [34mwhile[39;49;00m [34mtrue[39;49;00m:$
    43^I    [34mcase[39;49;00m readLine(stdin)$
    44^I    [34mof[39;49;00m [33m"[39;49;00m[33my[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mY[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33myes[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mYes[39;49;00m[33m"[39;49;00m: [34mreturn[39;49;00m [34mtrue[39;49;00m$
    45^I    [34mof[39;49;00m [33m"[39;49;00m[33mn[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mN[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mno[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mNo[39;49;00m[33m"[39;49;00m: [34mreturn[39;49;00m [34mfalse[39;49;00m$
    46^I    [34melse[39;49;00m: Echo([33m"[39;49;00m[33mPlease be clear: yes or no[39;49;00m[33m"[39;49;00m)$
    47^I$
    48^I[34mproc [39;49;00m[32meven[39;49;00m(n: [36mint[39;49;00m): [36mbool[39;49;00m$
    49^I$
    50^I[34mproc [39;49;00m[32modd[39;49;00m(n: [36mint[39;49;00m): [36mbool[39;49;00m =$
    51^I  [34mif[39;49;00m n == [34m1[39;49;00m: [34mreturn[39;49;00m [34mtrue[39;49;00m$
    52^I  [34melse[39;49;00m: [34mreturn[39;49;00m even(n-[34m1[39;49;00m)$
    53^I$
    54^I[34miterator[39;49;00m countup(a, b: [36mint[39;49;00m): [36mint[39;49;00m =$
    55^I  [34mvar[39;49;00m res = a$
    56^I  [34mwhile[39;49;00m res <= b:$
    57^I    [34myield[39;49;00m res$
    58^I    inc(res)$
    59^I$
    60^I[34mtype[39;49;00m$
    61^I  TPerson = [34mobject[39;49;00m [34mof[39;49;00m TObject$
    62^I    name*: [36mstring[39;49;00m  [37m# the * means that `name` is accessible from other modules[39;49;00m$
    63^I    age: [36mint[39;49;00m       [37m# no * means that the field is hidden from other modules[39;49;00m$
    64^I$
    65^I  TStudent = [34mobject[39;49;00m [34mof[39;49;00m TPerson [37m# TStudent inherits from TPerson[39;49;00m$
    66^I    id: [36mint[39;49;00m                    [37m# with an id field[39;49;00m$
    67^I$
    68^I[34mvar[39;49;00m$
    69^I  student: TStudent$
    70^I  person: TPerson$
    71^Iassert(student [35mis[39;49;00m TStudent)$
    72^I$
    73^Iecho({[33m'[39;49;00m[33ma[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mb[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mc[39;49;00m[33m'[39;49;00m}.card)$
    74^Istdout.writeln([33m"[39;49;00m[33mHallo[39;49;00m[33m"[39;49;00m)$
    75^I[34mvar[39;49;00m$
    76^I  f: TFile$
    77^I[34mif[39;49;00m open(f, [33m"[39;49;00m[33mnumbers.txt[39;49;00m[33m"[39;49;00m):$
    78^I  [34mtry[39;49;00m:$
    79^I    [34mvar[39;49;00m a = readLine(f)$
    80^I    [34mvar[39;49;00m b = readLine(f)$
    81^I    echo([33m"[39;49;00m[33msum: [39;49;00m[33m"[39;49;00m & $(parseInt(a) + parseInt(b)))$
    82^I  [34mexcept[39;49;00m EOverflow:$
    83^I    echo([33m"[39;49;00m[33moverflow![39;49;00m[33m"[39;49;00m)$
    84^I  [34mexcept[39;49;00m EInvalidValue:$
    85^I    echo([33m"[39;49;00m[33mcould not convert string to integer[39;49;00m[33m"[39;49;00m)$
    86^I  [34mexcept[39;49;00m EIO:$
    87^I    echo([33m"[39;49;00m[33mIO error![39;49;00m[33m"[39;49;00m)$
    88^I  [34mexcept[39;49;00m:$
    89^I    echo([33m"[39;49;00m[33mUnknown exception![39;49;00m[33m"[39;49;00m)$
    90^I    [37m# reraise the unknown exception:[39;49;00m$
    91^I    [34mraise[39;49;00m$
    92^I  [34mfinally[39;49;00m:$
    93^I    close(f)$

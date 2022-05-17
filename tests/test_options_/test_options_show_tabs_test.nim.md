[34mimport[39;49;00m re

[34mfor[39;49;00m x [35min[39;49;00m lines([33m"[39;49;00m[33mmyfile.txt[39;49;00m[33m"[39;49;00m):
  [34mif[39;49;00m x =~ [33mre"[39;49;00m[33m([39;49;00m[33m\[39;49;00m[33mw+)=(.*)[39;49;00m[33m"[39;49;00m:
    echo [33m"[39;49;00m[33mKey: [39;49;00m[33m"[39;49;00m, matches[[34m0[39;49;00m],
         [33m"[39;49;00m[33m Value: [39;49;00m[33m"[39;49;00m, matches[[34m1[39;49;00m]

Echo([33m"[39;49;00m[33mWhat[39;49;00m[33m'[39;49;00m[33ms your name? [39;49;00m[33m"[39;49;00m)
[34mvar[39;49;00m name: [36mstring[39;49;00m = readLine(stdin)
[34mif[39;49;00m name == [33m"[39;49;00m[33m"[39;49;00m:
  echo([33m"[39;49;00m[33mPoor soul, you lost your name?[39;49;00m[33m"[39;49;00m)
[34melif[39;49;00m name == [33m"[39;49;00m[33mname[39;49;00m[33m"[39;49;00m:
  echo([33m"[39;49;00m[33mVery funny, your name is name.[39;49;00m[33m"[39;49;00m)
[34melse[39;49;00m:
  Echo([33m"[39;49;00m[33mHi, [39;49;00m[33m"[39;49;00m, name, [33m"[39;49;00m[33m![39;49;00m[33m"[39;49;00m)

[34mvar[39;49;00m name = readLine(stdin)
[34mcase[39;49;00m name
[34mof[39;49;00m [33m"[39;49;00m[33m"[39;49;00m:
  echo([33m"[39;49;00m[33mPoor soul, you lost your name?[39;49;00m[33m"[39;49;00m)
[34mof[39;49;00m [33m"[39;49;00m[33mname[39;49;00m[33m"[39;49;00m:
  echo([33m"[39;49;00m[33mVery funny, your name is name.[39;49;00m[33m"[39;49;00m)
[34melse[39;49;00m:
  Echo([33m"[39;49;00m[33mHi, [39;49;00m[33m"[39;49;00m, name, [33m"[39;49;00m[33m![39;49;00m[33m"[39;49;00m)

[34mfrom[39;49;00m strutils [34mimport[39;49;00m parseInt

Echo([33m"[39;49;00m[33mA number please: [39;49;00m[33m"[39;49;00m)
[34mvar[39;49;00m n = parseInt(readLine(stdin))
[34mcase[39;49;00m n
[34mof[39;49;00m [34m0[39;49;00m..[34m2[39;49;00m, [34m4[39;49;00m..[34m7[39;49;00m: Echo([33m"[39;49;00m[33mThe number is in the set: {0, 1, 2, 4, 5, 6, 7}[39;49;00m[33m"[39;49;00m)
[34mof[39;49;00m [34m3[39;49;00m, [34m8[39;49;00m: Echo([33m"[39;49;00m[33mThe number is 3 or 8[39;49;00m[33m"[39;49;00m)

Echo([33m"[39;49;00m[33mCounting to 10: [39;49;00m[33m"[39;49;00m)
[34mvar[39;49;00m i = [34m1[39;49;00m
[34mwhile[39;49;00m i <= [34m10[39;49;00m:
  Echo($i)
  inc(i)

[34mproc [39;49;00m[32myes[39;49;00m(question: [36mstring[39;49;00m): [36mbool[39;49;00m =
  Echo(question, [33m"[39;49;00m[33m (y/n)[39;49;00m[33m"[39;49;00m)
  [34mwhile[39;49;00m [34mtrue[39;49;00m:
    [34mcase[39;49;00m readLine(stdin)
    [34mof[39;49;00m [33m"[39;49;00m[33my[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mY[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33myes[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mYes[39;49;00m[33m"[39;49;00m: [34mreturn[39;49;00m [34mtrue[39;49;00m
    [34mof[39;49;00m [33m"[39;49;00m[33mn[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mN[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mno[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mNo[39;49;00m[33m"[39;49;00m: [34mreturn[39;49;00m [34mfalse[39;49;00m
    [34melse[39;49;00m: Echo([33m"[39;49;00m[33mPlease be clear: yes or no[39;49;00m[33m"[39;49;00m)

[34mproc [39;49;00m[32meven[39;49;00m(n: [36mint[39;49;00m): [36mbool[39;49;00m

[34mproc [39;49;00m[32modd[39;49;00m(n: [36mint[39;49;00m): [36mbool[39;49;00m =
  [34mif[39;49;00m n == [34m1[39;49;00m: [34mreturn[39;49;00m [34mtrue[39;49;00m
  [34melse[39;49;00m: [34mreturn[39;49;00m even(n-[34m1[39;49;00m)

[34miterator[39;49;00m countup(a, b: [36mint[39;49;00m): [36mint[39;49;00m =
  [34mvar[39;49;00m res = a
  [34mwhile[39;49;00m res <= b:
    [34myield[39;49;00m res
    inc(res)

[34mtype[39;49;00m
  TPerson = [34mobject[39;49;00m [34mof[39;49;00m TObject
    name*: [36mstring[39;49;00m  [37m# the * means that `name` is accessible from other modules[39;49;00m
    age: [36mint[39;49;00m       [37m# no * means that the field is hidden from other modules[39;49;00m

  TStudent = [34mobject[39;49;00m [34mof[39;49;00m TPerson [37m# TStudent inherits from TPerson[39;49;00m
    id: [36mint[39;49;00m                    [37m# with an id field[39;49;00m

[34mvar[39;49;00m
  student: TStudent
  person: TPerson
assert(student [35mis[39;49;00m TStudent)

echo({[33m'[39;49;00m[33ma[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mb[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mc[39;49;00m[33m'[39;49;00m}.card)
stdout.writeln([33m"[39;49;00m[33mHallo[39;49;00m[33m"[39;49;00m)
[34mvar[39;49;00m
  f: TFile
[34mif[39;49;00m open(f, [33m"[39;49;00m[33mnumbers.txt[39;49;00m[33m"[39;49;00m):
  [34mtry[39;49;00m:
    [34mvar[39;49;00m a = readLine(f)
    [34mvar[39;49;00m b = readLine(f)
    echo([33m"[39;49;00m[33msum: [39;49;00m[33m"[39;49;00m & $(parseInt(a) + parseInt(b)))
  [34mexcept[39;49;00m EOverflow:
    echo([33m"[39;49;00m[33moverflow![39;49;00m[33m"[39;49;00m)
  [34mexcept[39;49;00m EInvalidValue:
    echo([33m"[39;49;00m[33mcould not convert string to integer[39;49;00m[33m"[39;49;00m)
  [34mexcept[39;49;00m EIO:
    echo([33m"[39;49;00m[33mIO error![39;49;00m[33m"[39;49;00m)
  [34mexcept[39;49;00m:
    echo([33m"[39;49;00m[33mUnknown exception![39;49;00m[33m"[39;49;00m)
    [37m# reraise the unknown exception:[39;49;00m
    [34mraise[39;49;00m
  [34mfinally[39;49;00m:
    close(f)

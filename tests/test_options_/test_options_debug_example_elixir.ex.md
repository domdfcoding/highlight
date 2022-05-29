Using lexer <pygments.lexers.ElixirLexer with {'ensurenl': False, 'tabsize': 0}>
[37m# Numbers[39;49;00m[37m[39;49;00m
[34m0b0101011[39;49;00m[37m[39;49;00m
[34m1234[39;49;00m[37m [39;49;00m;[37m [39;49;00m[34m0x1A[39;49;00m[37m [39;49;00m;[37m [39;49;00m[34m0xbeef[39;49;00m[37m [39;49;00m;[37m [39;49;00m[34m0763[39;49;00m[37m [39;49;00m;[37m [39;49;00m[34m0o123[39;49;00m[37m[39;49;00m
[34m3.14[39;49;00m[37m [39;49;00m;[37m [39;49;00m[34m5.0e21[39;49;00m[37m [39;49;00m;[37m [39;49;00m[34m0.5e-12[39;49;00m[37m[39;49;00m
[34m100_000_000[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m# these are not valid numbers[39;49;00m[37m[39;49;00m
[34m0b01[39;49;00m[34m2[39;49;00m[37m [39;49;00m;[37m [39;49;00m[34m0xb[39;49;00moar[37m [39;49;00m;[37m [39;49;00m[34m0[39;49;00mo888[37m[39;49;00m
[34m0[39;49;00m[04m[32mB01[39;49;00m[37m [39;49;00m;[37m [39;49;00m[34m0[39;49;00m[04m[32mXAF[39;49;00m[37m [39;49;00m;[37m [39;49;00m[34m0[39;49;00m[04m[32mO123[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m# Characters[39;49;00m[37m[39;49;00m
[33m?a[39;49;00m[37m [39;49;00m;[37m [39;49;00m[33m?1[39;49;00m[37m [39;49;00m;[37m [39;49;00m[33m?[39;49;00m[33m\n[39;49;00m[37m [39;49;00m;[37m [39;49;00m[33m?[39;49;00m[33m\s[39;49;00m[37m [39;49;00m;[37m [39;49;00m[33m?\c[39;49;00m[37m [39;49;00m;[37m [39;49;00m[33m? [39;49;00m;[37m [39;49;00m[33m?,[39;49;00m[37m[39;49;00m
[33m?[39;49;00m[33m\x{[39;49;00m[34m12[39;49;00m[33m}[39;49;00m[37m [39;49;00m;[37m [39;49;00m[33m?[39;49;00m[33m\x{[39;49;00m[34mabcd[39;49;00m[33m}[39;49;00m[37m[39;49;00m
[33m?[39;49;00m[33m\x34[39;49;00m[37m [39;49;00m;[37m [39;49;00m[33m?[39;49;00m[33m\xF[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m# these show that only the first digit is part of the character[39;49;00m[37m[39;49;00m
[33m?\1[39;49;00m[34m23[39;49;00m[37m [39;49;00m;[37m [39;49;00m[33m?\1[39;49;00m[34m2[39;49;00m[37m [39;49;00m;[37m [39;49;00m[33m?\7[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m# Atoms[39;49;00m[37m[39;49;00m
[33m:this[39;49;00m[37m [39;49;00m;[37m [39;49;00m[33m:that[39;49;00m[37m[39;49;00m
[33m:'[39;49;00m[33mcomplex atom[39;49;00m[33m'[39;49;00m[37m[39;49;00m
[33m:"[39;49;00m[33mwith' [39;49;00m[33m\"[39;49;00m[33m\"[39;49;00m[33m 'quotes[39;49;00m[33m"[39;49;00m[37m[39;49;00m
[33m:"[39;49;00m[33m multi[39;49;00m
[33m line ' [39;49;00m[33m\s[39;49;00m[33m [39;49;00m[33m\1[39;49;00m[33m23 [39;49;00m[33m\xff[39;49;00m[33m[39;49;00m
[33matom[39;49;00m[33m"[39;49;00m[37m[39;49;00m
[33m:...[39;49;00m[37m [39;49;00m;[37m [39;49;00m[33m:<<>>[39;49;00m[37m [39;49;00m;[37m [39;49;00m[33m:%{}[39;49;00m[37m [39;49;00m;[37m [39;49;00m[33m:%[39;49;00m[37m [39;49;00m;[37m [39;49;00m[33m:{}[39;49;00m[37m[39;49;00m
[33m:++[39;49;00m;[37m [39;49;00m[33m:--[39;49;00m;[37m [39;49;00m[33m:*[39;49;00m;[37m [39;49;00m[33m:~~~[39;49;00m;[37m [39;49;00m[33m:::[39;49;00m[37m[39;49;00m
[33m:%[39;49;00m[37m [39;49;00m;[37m [39;49;00m[33m:.[39;49;00m[37m [39;49;00m;[37m [39;49;00m[33m:<-[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m# Strings[39;49;00m[37m[39;49;00m
[33m"[39;49;00m[33mHello world[39;49;00m[33m"[39;49;00m[37m[39;49;00m
[33m"[39;49;00m[33mInterspersed [39;49;00m[33m\x{[39;49;00m[34mff[39;49;00m[33m}[39;49;00m[33m codes [39;49;00m[33m\7[39;49;00m[33m [39;49;00m[33m\8[39;49;00m[33m [39;49;00m[33m\6[39;49;00m[33m5 [39;49;00m[33m\0[39;49;00m[33m16 and [39;49;00m[33m\t[39;49;00m[33m\s[39;49;00m[33m\\[39;49;00m[33ms[39;49;00m[33m\z[39;49;00m[33m\+[39;49;00m[33m [39;49;00m[33m\\[39;49;00m[33m escapes[39;49;00m[33m"[39;49;00m[37m[39;49;00m
[33m"[39;49;00m[33mQuotes ' inside [39;49;00m[33m\"[39;49;00m[33m [39;49;00m[33m\1[39;49;00m[33m23 the [39;49;00m[33m\"[39;49;00m[33m\"[39;49;00m[33m [39;49;00m[33m\xF[39;49;00m[33m [39;49;00m[33m\\[39;49;00m[33mxF string [39;49;00m[33m\\[39;49;00m[33m\"[39;49;00m[33m end[39;49;00m[33m"[39;49;00m[37m[39;49;00m
[33m"[39;49;00m[33mMultiline[39;49;00m
[33m   string[39;49;00m[33m"[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m# Char lists[39;49;00m[37m[39;49;00m
[33m'[39;49;00m[33mthis is a list[39;49;00m[33m'[39;49;00m[37m[39;49;00m
[33m'[39;49;00m[33mescapes [39;49;00m[33m\'[39;49;00m[33m [39;49;00m[33m\t[39;49;00m[33m [39;49;00m[33m\\[39;49;00m[33m\'[39;49;00m[33m'[39;49;00m[37m[39;49;00m
[33m'[39;49;00m[33mMultiline[39;49;00m
[33m    char[39;49;00m
[33m  list[39;49;00m
[33m'[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m# Binaries[39;49;00m[37m[39;49;00m
<<[34m1[39;49;00m,[37m [39;49;00m[34m2[39;49;00m,[37m [39;49;00m[34m3[39;49;00m>>[37m[39;49;00m
<<[33m"[39;49;00m[33mhello[39;49;00m[33m"[39;49;00m::binary,[37m [39;49;00mc[37m [39;49;00m::[37m [39;49;00mutf8,[37m [39;49;00mx::[[34m4[39;49;00m,[37m [39;49;00munit([34m2[39;49;00m)]>>[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33mhello™1[39;49;00m[33m"[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m# Sigils[39;49;00m[37m[39;49;00m
[33m~r/[39;49;00m[33mthis + i[39;49;00m[33m\s[39;49;00m[33m "a" regex[39;49;00m[33m/[39;49;00m[37m[39;49;00m
[33m~R'[39;49;00m[33mthis + i[39;49;00m[33m\s[39;49;00m[33m "a" regex too[39;49;00m[33m'[39;49;00m[37m[39;49;00m
[33m~w([39;49;00m[33mhello [39;49;00m[33m#{[39;49;00m[37m [39;49;00m[[33m"[39;49;00m[33mhas[39;49;00m[33m"[39;49;00m[37m [39;49;00m<>[37m [39;49;00m[33m"[39;49;00m[33m123[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[33m'[39;49;00m[33m\c[39;49;00m[33m\d[39;49;00m[33m'[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33m\1[39;49;00m[33m23 interpol[39;49;00m[33m"[39;49;00m[37m [39;49;00m|[37m [39;49;00m[]][37m [39;49;00m[33m}[39;49;00m[33m world[39;49;00m[33m)s[39;49;00m[37m[39;49;00m
[33m~W([39;49;00m[33mhello #{no "123" [39;49;00m[33m\c[39;49;00m[33m\d[39;49;00m[33m [39;49;00m[33m\1[39;49;00m[33m23 interpol} world[39;49;00m[33m)s[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[33m~s{[39;49;00m[33mEscapes terminators [39;49;00m[33m\{[39;49;00m[33m and [39;49;00m[33m\}[39;49;00m[33m, but no {balancing[39;49;00m[33m}[39;49;00m[37m [39;49;00m[37m# outside of sigil here }[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[33m~S"[39;49;00m[33mNo escapes [39;49;00m[33m\s[39;49;00m[33m\t[39;49;00m[33m\n[39;49;00m[33m and no #{interpolation}[39;49;00m[33m"[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[33m:"[39;49;00m[33matoms work [39;49;00m[33m#{[39;49;00m[33m"[39;49;00m[33mto[39;49;00m[33m"[39;49;00m[37m [39;49;00m<>[37m [39;49;00m[33m"[39;49;00m[33mo[39;49;00m[33m"[39;49;00m[33m}[39;49;00m[33m"[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m# Operators[39;49;00m[37m[39;49;00m
x[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m+[37m [39;49;00m[34m2.0[39;49;00m[37m [39;49;00m*[37m [39;49;00m[34m3[39;49;00m[37m[39;49;00m
y[37m [39;49;00m=[37m [39;49;00m[31mtrue[39;49;00m[37m [39;49;00m[35mand[39;49;00m[37m [39;49;00m[31mfalse[39;49;00m;[37m [39;49;00mz[37m [39;49;00m=[37m [39;49;00m[31mfalse[39;49;00m[37m [39;49;00m[35mor[39;49;00m[37m [39;49;00m[31mtrue[39;49;00m[37m[39;49;00m
...[37m [39;49;00m=[37m [39;49;00m[34m144[39;49;00m[37m[39;49;00m
...[37m [39;49;00m==[37m [39;49;00m!x[37m [39;49;00m&&[37m [39;49;00my[37m [39;49;00m||[37m [39;49;00mz[37m[39;49;00m
[33m"[39;49;00m[33mhello[39;49;00m[33m"[39;49;00m[37m [39;49;00m|>[37m [39;49;00m[04m[32mString[39;49;00m.upcase[37m [39;49;00m|>[37m [39;49;00m[04m[32mString[39;49;00m.downcase()[37m[39;49;00m
{^z,[37m [39;49;00ma}[37m [39;49;00m=[37m [39;49;00m{[31mtrue[39;49;00m,[37m [39;49;00mx}[37m[39;49;00m
[37m[39;49;00m
[37m# Free operators (added in 1.0.0)[39;49;00m[37m[39;49;00m
p[37m  [39;49;00m~>>[37m [39;49;00mf[37m  [39;49;00m=[37m [39;49;00mbind(p,[37m [39;49;00mf)[37m[39;49;00m
p1[37m [39;49;00m~>[37m  [39;49;00mp2[37m [39;49;00m=[37m [39;49;00mpair_right(p1,[37m [39;49;00mp2)[37m[39;49;00m
p1[37m [39;49;00m<~[37m  [39;49;00mp2[37m [39;49;00m=[37m [39;49;00mpair_left(p1,[37m [39;49;00mp2)[37m[39;49;00m
p1[37m [39;49;00m<~>[37m [39;49;00mp2[37m [39;49;00m=[37m [39;49;00mpair_both(p1,[37m [39;49;00mp2)[37m[39;49;00m
p[37m  [39;49;00m|~>[37m [39;49;00mf[37m  [39;49;00m=[37m [39;49;00mmap(p,[37m [39;49;00mf)[37m[39;49;00m
p1[37m [39;49;00m<|>[37m [39;49;00mp2[37m [39;49;00m=[37m [39;49;00meither(p1,[37m [39;49;00mp2)[37m[39;49;00m
[37m[39;49;00m
[37m# Lists, tuples, maps, keywords[39;49;00m[37m[39;49;00m
[[34m1[39;49;00m,[37m [39;49;00m[33m:a[39;49;00m,[37m [39;49;00m[33m'[39;49;00m[33mhello[39;49;00m[33m'[39;49;00m][37m [39;49;00m++[37m [39;49;00m[[34m2[39;49;00m,[37m [39;49;00m[34m3[39;49;00m][37m[39;49;00m
[[33m:head[39;49;00m[37m [39;49;00m|[37m [39;49;00m[[33m?t[39;49;00m,[37m [39;49;00m[33m?a[39;49;00m,[37m [39;49;00m[33m?i[39;49;00m,[37m [39;49;00m[33m?l[39;49;00m]][37m[39;49;00m
[37m[39;49;00m
{[33m:one[39;49;00m,[37m [39;49;00m[34m2.0[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33mthree[39;49;00m[33m"[39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[[33m...[39;49;00m:[37m [39;49;00m[33m"[39;49;00m[33mthis[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[33m<<>>[39;49;00m:[37m [39;49;00m[33m"[39;49;00m[33mis[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[33m%{}[39;49;00m:[37m [39;49;00m[33m"[39;49;00m[33ma keyword[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[33m%[39;49;00m:[37m [39;49;00m[33m"[39;49;00m[33mlist[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[33m{}[39;49;00m:[37m [39;49;00m[33m"[39;49;00m[33mtoo[39;49;00m[33m"[39;49;00m][37m[39;49;00m
[[33m"[39;49;00m[33mthis is an atom too[39;49;00m[33m"[39;49;00m:[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33mso is this[39;49;00m[33m"[39;49;00m:[37m [39;49;00m[34m2[39;49;00m][37m[39;49;00m
[[33moption[39;49;00m:[37m [39;49;00m[33m"[39;49;00m[33mvalue[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[33mkey[39;49;00m:[37m [39;49;00m[33m:word[39;49;00m][37m[39;49;00m
[[33m++[39;49;00m:[37m [39;49;00m[33m"[39;49;00m[33moperator[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[33m~~~[39;49;00m:[37m [39;49;00m[33m:&&&[39;49;00m][37m[39;49;00m
[37m[39;49;00m
map[37m [39;49;00m=[37m [39;49;00m%{[33mshortcut[39;49;00m:[37m [39;49;00m[33m"[39;49;00m[33msyntax[39;49;00m[33m"[39;49;00m}[37m[39;49;00m
%{map[37m [39;49;00m|[37m [39;49;00m[33m"[39;49;00m[33mupdate[39;49;00m[33m"[39;49;00m[37m [39;49;00m=>[37m [39;49;00m[33m"[39;49;00m[33mme[39;49;00m[33m"[39;49;00m}[37m[39;49;00m
%{[37m [39;49;00m[34m12[39;49;00m[37m [39;49;00m=>[37m [39;49;00m[34m13[39;49;00m,[37m [39;49;00m[33m:weird[39;49;00m[37m [39;49;00m=>[37m [39;49;00m[[33m'[39;49;00m[33mthing[39;49;00m[33m'[39;49;00m][37m [39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[37m# Comprehensions[39;49;00m[37m[39;49;00m
[34mfor[39;49;00m[37m [39;49;00mx[37m [39;49;00m<-[37m [39;49;00m[34m1[39;49;00m..[34m10[39;49;00m,[37m [39;49;00mx[37m [39;49;00m<[37m [39;49;00m[34m5[39;49;00m,[37m [39;49;00m[33mdo[39;49;00m:[37m [39;49;00m{x,[37m [39;49;00mx}[37m[39;49;00m
pixels[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33m12345678[39;49;00m[33m"[39;49;00m[37m[39;49;00m
[34mfor[39;49;00m[37m [39;49;00m<<[37m [39;49;00m<<r::[34m4[39;49;00m,[37m [39;49;00mg::[34m4[39;49;00m,[37m [39;49;00mb::[34m4[39;49;00m,[37m [39;49;00ma::size([34m4[39;49;00m)>>[37m [39;49;00m<-[37m [39;49;00mpixels[37m [39;49;00m>>[37m [39;49;00m[34mdo[39;49;00m[37m[39;49;00m
[37m  [39;49;00m[r,[37m [39;49;00m{g,[37m [39;49;00m%{[33m"[39;49;00m[33mb[39;49;00m[33m"[39;49;00m[37m [39;49;00m=>[37m [39;49;00ma}}][37m[39;49;00m
[34mend[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m# String interpolation[39;49;00m[37m[39;49;00m
[33m"[39;49;00m[33mString [39;49;00m[33m#{[39;49;00minspect[37m [39;49;00m[33m"[39;49;00m[33minterpolation[39;49;00m[33m"[39;49;00m[33m}[39;49;00m[33m is quite [39;49;00m[33m#{[39;49;00m[34m1[39;49;00m+[34m4[39;49;00m+[34m7[39;49;00m[33m}[39;49;00m[33m difficult[39;49;00m[33m"[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m# Identifiers[39;49;00m[37m[39;49;00m
abc_123[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m[37m[39;49;00m
_018OP[37m [39;49;00m=[37m [39;49;00m[34m2[39;49;00m[37m[39;49;00m
[04m[32mA__0[39;49;00m[37m [39;49;00m==[37m [39;49;00m[34m3[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m# Modules[39;49;00m[37m[39;49;00m
[34mdefmodule[39;49;00m[37m [39;49;00m[04m[32mLong.Module.Name[39;49;00m[37m [39;49;00m[34mdo[39;49;00m[37m[39;49;00m
[37m  [39;49;00m[36m@moduledoc[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mSimple module docstring[39;49;00m[33m"[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m  [39;49;00m[36m@doc[39;49;00m[37m [39;49;00m[33m"""[39;49;00m[37m[39;49;00m
[37m  [39;49;00m[33mMultiline docstring[39;49;00m[33m[39;49;00m
[33m  "with quotes"[39;49;00m[33m[39;49;00m
[33m  and [39;49;00m[33m#{[39;49;00m[37m [39;49;00minspect[37m [39;49;00m%{[33m"[39;49;00m[33minterpolation[39;49;00m[33m"[39;49;00m[37m [39;49;00m=>[37m [39;49;00m[33m"[39;49;00m[33min[39;49;00m[33m"[39;49;00m[37m [39;49;00m<>[37m [39;49;00m[33m"[39;49;00m[33maction[39;49;00m[33m"[39;49;00m}[37m [39;49;00m[33m}[39;49;00m[33m[39;49;00m
[33m  now with [39;49;00m[33m#{[39;49;00m[37m [39;49;00m{[33m:a[39;49;00m,[37m [39;49;00m[33m'[39;49;00m[33mtuple[39;49;00m[33m'[39;49;00m}[37m [39;49;00m[33m}[39;49;00m[33m[39;49;00m
[33m  and [39;49;00m[33m#{[39;49;00m[37m [39;49;00minspect[37m [39;49;00m{[37m[39;49;00m
[37m      [39;49;00m[33m:tuple[39;49;00m,[37m[39;49;00m
[37m      [39;49;00m%{[37m [39;49;00m[33mwith[39;49;00m:[37m [39;49;00m[33m"[39;49;00m[33mnested [39;49;00m[33m#{[39;49;00m[37m [39;49;00minspect[37m [39;49;00m%{[37m [39;49;00m[33m:interpolation[39;49;00m[37m [39;49;00m=>[37m [39;49;00m%{}[37m [39;49;00m}[37m [39;49;00m[33m}[39;49;00m[33m"[39;49;00m[37m [39;49;00m}[37m[39;49;00m
[37m  [39;49;00m}[37m [39;49;00m[33m}[39;49;00m[33m[39;49;00m
[37m  [39;49;00m[33m"""[39;49;00m[37m[39;49;00m
[37m  [39;49;00m[34mdefstruct[39;49;00m[37m [39;49;00m[[33m:a[39;49;00m,[37m [39;49;00m[33m:name[39;49;00m,[37m [39;49;00m[33m:height[39;49;00m][37m[39;49;00m
[37m[39;49;00m
[37m  [39;49;00m[36m@doc[39;49;00m[37m [39;49;00m[33m~S[39;49;00m[33m'''[39;49;00m[37m[39;49;00m
[33m  No #{interpolation} of any kind.[39;49;00m[37m[39;49;00m
[33m  [39;49;00m[33m\0[39;49;00m[33m00 [39;49;00m[33m\x[39;49;00m[33m{ff}[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[33m  [39;49;00m[33m\n[39;49;00m[33m #{[39;49;00m[33m\x[39;49;00m[33m{ff}}[39;49;00m[37m[39;49;00m
[37m  [39;49;00m[33m'''[39;49;00m[37m[39;49;00m
[37m  [39;49;00m[34mdef[39;49;00m[37m [39;49;00mfunc(a,[37m [39;49;00mb[37m [39;49;00m\\[37m [39;49;00m[]),[37m [39;49;00m[33mdo[39;49;00m:[37m [39;49;00m[33m:ok[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m  [39;49;00m[36m@doc[39;49;00m[37m [39;49;00m[31mfalse[39;49;00m[37m[39;49;00m
[37m  [39;49;00m[34mdef[39;49;00m[37m [39;49;00m__before_compile__([36m_[39;49;00m)[37m [39;49;00m[34mdo[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[33m:ok[39;49;00m[37m[39;49;00m
[37m  [39;49;00m[34mend[39;49;00m[37m[39;49;00m
[34mend[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m# Structs[39;49;00m[37m[39;49;00m
[34mdefmodule[39;49;00m[37m [39;49;00m[04m[32mSecond.Module[39;49;00m[37m [39;49;00m[34mdo[39;49;00m[37m[39;49;00m
[37m  [39;49;00ms[37m [39;49;00m=[37m [39;49;00m%[04m[32mLong.Module.Name[39;49;00m{[33mname[39;49;00m:[37m [39;49;00m[33m"[39;49;00m[33mSilly[39;49;00m[33m"[39;49;00m}[37m[39;49;00m
[37m  [39;49;00m%[04m[32mLong.Module.Name[39;49;00m{s[37m [39;49;00m|[37m [39;49;00m[33mheight[39;49;00m:[37m [39;49;00m{[34m192[39;49;00m,[37m [39;49;00m[33m:cm[39;49;00m}}[37m[39;49;00m
[37m  [39;49;00m[33m"[39;49;00m[33m.. [39;49;00m[33m#{[39;49;00m%[04m[32mLong.Module.Name[39;49;00m{s[37m [39;49;00m|[37m [39;49;00m[33mheight[39;49;00m:[37m [39;49;00m{[34m192[39;49;00m,[37m [39;49;00m[33m:cm[39;49;00m}}[33m}[39;49;00m[33m ..[39;49;00m[33m"[39;49;00m[37m[39;49;00m
[34mend[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m# Types, pseudo-vars, attributes[39;49;00m[37m[39;49;00m
[34mdefmodule[39;49;00m[37m [39;49;00m[04m[32mM[39;49;00m[37m [39;49;00m[34mdo[39;49;00m[37m[39;49;00m
[37m  [39;49;00m[36m@custom_attr[39;49;00m[37m [39;49;00m[33m:some_constant[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m  [39;49;00m[36m@before_compile[39;49;00m[37m [39;49;00m[04m[32mLong.Module.Name[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m  [39;49;00m[36m@typedoc[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mThis is a type[39;49;00m[33m"[39;49;00m[37m[39;49;00m
[37m  [39;49;00m[36m@type[39;49;00m[37m [39;49;00mtyp[37m [39;49;00m::[37m [39;49;00minteger[37m[39;49;00m
[37m[39;49;00m
[37m  [39;49;00m[36m@typedoc[39;49;00m[37m [39;49;00m[33m"""[39;49;00m[37m[39;49;00m
[37m  [39;49;00m[33mAnother type[39;49;00m[33m[39;49;00m
[37m  [39;49;00m[33m"""[39;49;00m[37m[39;49;00m
[37m  [39;49;00m[36m@opaque[39;49;00m[37m [39;49;00mtyptyp[37m [39;49;00m::[37m [39;49;00m[34m1[39;49;00m..[34m10[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m  [39;49;00m[36m@spec[39;49;00m[37m [39;49;00mfunc(typ,[37m [39;49;00mtyptyp)[37m [39;49;00m::[37m [39;49;00m[33m:ok[39;49;00m[37m [39;49;00m|[37m [39;49;00m[33m:fail[39;49;00m[37m[39;49;00m
[37m  [39;49;00m[34mdef[39;49;00m[37m [39;49;00mfunc(a,[37m [39;49;00mb)[37m [39;49;00m[34mdo[39;49;00m[37m[39;49;00m
[37m    [39;49;00ma[37m [39;49;00m||[37m [39;49;00mb[37m [39;49;00m||[37m [39;49;00m[33m:ok[39;49;00m[37m [39;49;00m||[37m [39;49;00m[33m:fail[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[04m[32mPath[39;49;00m.expand([33m"[39;49;00m[33m..[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[36m__DIR__[39;49;00m)[37m[39;49;00m
[37m    [39;49;00m[04m[32mIO[39;49;00m.inspect[37m [39;49;00m[36m__ENV__[39;49;00m[37m[39;49;00m
[37m    [39;49;00m__NOTAPSEUDOVAR__[37m [39;49;00m=[37m [39;49;00m[34m11[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[36m__MODULE__[39;49;00m.func(b,[37m [39;49;00ma)[37m[39;49;00m
[37m  [39;49;00m[34mend[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m  [39;49;00m[34mdefmacro[39;49;00m[37m [39;49;00mm()[37m [39;49;00m[34mdo[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[36m__CALLER__[39;49;00m[37m[39;49;00m
[37m  [39;49;00m[34mend[39;49;00m[37m[39;49;00m
[34mend[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m# Functions[39;49;00m[37m[39;49;00m
anon[37m [39;49;00m=[37m [39;49;00m[34mfn[39;49;00m[37m [39;49;00mx,[37m [39;49;00my,[37m [39;49;00mz[37m [39;49;00m->[37m[39;49;00m
[37m  [39;49;00m[34mfn[39;49;00m(a,[37m [39;49;00mb,[37m [39;49;00mc)[37m [39;49;00m->[37m[39;49;00m
[37m    [39;49;00m&(x[37m [39;49;00m+[37m [39;49;00my[37m [39;49;00m-[37m [39;49;00mz[37m [39;49;00m*[37m [39;49;00ma[37m [39;49;00m/[37m [39;49;00m&1[37m [39;49;00m+[37m [39;49;00mb[37m [39;49;00m+[37m [39;49;00mdiv(&2,[37m [39;49;00mc))[37m[39;49;00m
[37m  [39;49;00m[34mend[39;49;00m[37m[39;49;00m
[34mend[39;49;00m[37m[39;49;00m
[37m[39;49;00m
&[04m[32mSet[39;49;00m.put(&1,[37m [39;49;00m&2)[37m [39;49;00m;[37m [39;49;00m&[37m [39;49;00m[04m[32mSet[39;49;00m.put(&1,[37m [39;49;00m&2)[37m [39;49;00m;[37m [39;49;00m&([37m [39;49;00m[04m[32mSet[39;49;00m.put(&1,[37m [39;49;00m&1)[37m [39;49;00m)[37m[39;49;00m
[37m[39;49;00m
[37m# Function calls[39;49;00m[37m[39;49;00m
anon.([34m1[39;49;00m,[37m [39;49;00m[34m2[39;49;00m,[37m [39;49;00m[34m3[39;49;00m);[37m [39;49;00mself;[37m [39;49;00mhd([[34m1[39;49;00m,[34m2[39;49;00m,[34m3[39;49;00m])[37m[39;49;00m
[04m[32mKernel[39;49;00m.spawn([34mfn[39;49;00m[37m [39;49;00m->[37m [39;49;00m[33m:ok[39;49;00m[37m [39;49;00m[34mend[39;49;00m)[37m[39;49;00m
[04m[32mIO.ANSI[39;49;00m.black[37m[39;49;00m
[37m[39;49;00m
[37m# Control flow[39;49;00m[37m[39;49;00m
[34mif[39;49;00m[37m [39;49;00m[33m:this[39;49;00m[37m [39;49;00m[34mdo[39;49;00m[37m[39;49;00m
[37m  [39;49;00m[33m:that[39;49;00m[37m[39;49;00m
[34melse[39;49;00m[37m[39;49;00m
[37m  [39;49;00m[33m:otherwise[39;49;00m[37m[39;49;00m
[34mend[39;49;00m[37m[39;49;00m
[37m[39;49;00m
pid[37m [39;49;00m=[37m [39;49;00mself[37m[39;49;00m
[34mreceive[39;49;00m[37m [39;49;00m[34mdo[39;49;00m[37m[39;49;00m
[37m  [39;49;00m{[33m:EXIT[39;49;00m,[37m [39;49;00m[36m_[39;49;00m}[37m [39;49;00m->[37m [39;49;00m[33m:done[39;49;00m[37m[39;49;00m
[37m  [39;49;00m{^pid,[37m [39;49;00m[33m:_[39;49;00m}[37m [39;49;00m->[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m
[37m  [39;49;00m[34mafter[39;49;00m[37m [39;49;00m[34m100[39;49;00m[37m [39;49;00m->[37m [39;49;00m[33m:no_luck[39;49;00m[37m[39;49;00m
[34mend[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[34mcase[39;49;00m[37m [39;49;00m[36m__ENV__[39;49;00m.line[37m [39;49;00m[34mdo[39;49;00m[37m[39;49;00m
[37m  [39;49;00mx[37m [39;49;00m[35mwhen[39;49;00m[37m [39;49;00mis_integer(x)[37m [39;49;00m->[37m [39;49;00mx[37m[39;49;00m
[37m  [39;49;00mx[37m [39;49;00m[35mwhen[39;49;00m[37m [39;49;00mx[37m [39;49;00m[35min[39;49;00m[37m [39;49;00m[34m1[39;49;00m..[34m12[39;49;00m[37m [39;49;00m->[37m [39;49;00m-x[37m[39;49;00m
[34mend[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[34mcond[39;49;00m[37m [39;49;00m[34mdo[39;49;00m[37m[39;49;00m
[37m  [39;49;00m[31mfalse[39;49;00m[37m [39;49;00m->[37m [39;49;00m[33m"[39;49;00m[33mtoo bad[39;49;00m[33m"[39;49;00m[37m[39;49;00m
[37m  [39;49;00m[34m4[39;49;00m[37m [39;49;00m>[37m [39;49;00m[34m5[39;49;00m[37m [39;49;00m->[37m [39;49;00m[33m"[39;49;00m[33moops[39;49;00m[33m"[39;49;00m[37m[39;49;00m
[37m  [39;49;00m[31mtrue[39;49;00m[37m [39;49;00m->[37m [39;49;00m[31mnil[39;49;00m[37m[39;49;00m
[34mend[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m# Lexical scope modifiers[39;49;00m[37m[39;49;00m
[34mimport[39;49;00m[37m [39;49;00m[04m[32mKernel[39;49;00m,[37m [39;49;00m[33mexcept[39;49;00m:[37m [39;49;00m[[33mspawn[39;49;00m:[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00m[33m+[39;49;00m:[37m [39;49;00m[34m2[39;49;00m,[37m [39;49;00m[33m/[39;49;00m:[37m [39;49;00m[34m2[39;49;00m,[37m [39;49;00m[33mUnless[39;49;00m:[37m [39;49;00m[34m2[39;49;00m][37m[39;49;00m
[34malias[39;49;00m[37m [39;49;00m[04m[32mLong.Module.Name[39;49;00m,[37m [39;49;00m[33mas[39;49;00m:[37m [39;49;00m[04m[32mN0men123_and4[39;49;00m[37m[39;49;00m
[34muse[39;49;00m[37m [39;49;00m[04m[32mBitwise[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[34m4[39;49;00m[37m [39;49;00m&&&[37m [39;49;00m[34m5[39;49;00m[37m[39;49;00m
[34m2[39;49;00m[37m [39;49;00m<<<[37m [39;49;00m[34m3[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m# Protocols[39;49;00m[37m[39;49;00m
[34mdefprotocol[39;49;00m[37m [39;49;00m[04m[32mUseless[39;49;00m[37m [39;49;00m[34mdo[39;49;00m[37m[39;49;00m
[37m  [39;49;00m[34mdef[39;49;00m[37m [39;49;00mfunc1(this)[37m[39;49;00m
[37m  [39;49;00m[34mdef[39;49;00m[37m [39;49;00mfunc2(that)[37m[39;49;00m
[34mend[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[34mdefimpl[39;49;00m[37m [39;49;00m[04m[32mUseless[39;49;00m,[37m [39;49;00m[33mfor[39;49;00m:[37m [39;49;00m[04m[32mAtom[39;49;00m[37m [39;49;00m[34mdo[39;49;00m[37m[39;49;00m
[34mend[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m# Exceptions[39;49;00m[37m[39;49;00m
[34mdefmodule[39;49;00m[37m [39;49;00m[04m[32mNotAnError[39;49;00m[37m [39;49;00m[34mdo[39;49;00m[37m[39;49;00m
[37m  [39;49;00m[34mdefexception[39;49;00m[37m [39;49;00m[[33m:message[39;49;00m][37m[39;49;00m
[34mend[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[34mraise[39;49;00m[37m [39;49;00m[04m[32mNotAnError[39;49;00m,[37m [39;49;00m[33mmessage[39;49;00m:[37m [39;49;00m[33m"[39;49;00m[33mThis is not an error[39;49;00m[33m"[39;49;00m
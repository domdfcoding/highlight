[37m# -*- ruby -*-[39;49;00m$
$
[37m# Local variables:[39;49;00m$
[37m#  indent-tabs-mode: nil[39;49;00m$
[37m#  ruby-indent-level: 4[39;49;00m$
[37m# End:[39;49;00m$
$
[37m# @@PLEAC@@_NAME[39;49;00m$
[37m# @@SKIP@@ Ruby[39;49;00m$
$
[37m# @@PLEAC@@_WEB[39;49;00m$
[37m# @@SKIP@@ http://www.ruby-lang.org[39;49;00m$
$
$
[37m# @@PLEAC@@_1.0[39;49;00m$
string = [33m'[39;49;00m[33m\n[39;49;00m[33m'[39;49;00m                     [37m# two characters, \ and an n[39;49;00m$
string = [33m'[39;49;00m[33mJon [39;49;00m[33m\'[39;49;00m[33mMaddog[39;49;00m[33m\'[39;49;00m[33m Orwant[39;49;00m[33m'[39;49;00m  [37m# literal single quotes[39;49;00m$
$
string = [33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m                     [37m# a "newline" character[39;49;00m$
string = [33m"[39;49;00m[33mJon [39;49;00m[33m\"[39;49;00m[33mMaddog[39;49;00m[33m\"[39;49;00m[33m Orwant[39;49;00m[33m"[39;49;00m  [37m# literal double quotes[39;49;00m$
$
string = [33m%q/Jon 'Maddog' Orwant/[39;49;00m  [37m# literal single quotes[39;49;00m$
$
string = [33m%q[[39;49;00m[33mJon 'Maddog' Orwant[39;49;00m[33m][39;49;00m  [37m# literal single quotes[39;49;00m$
string = [33m%q{[39;49;00m[33mJon 'Maddog' Orwant[39;49;00m[33m}[39;49;00m  [37m# literal single quotes[39;49;00m$
string = [33m%q([39;49;00m[33mJon 'Maddog' Orwant[39;49;00m[33m)[39;49;00m  [37m# literal single quotes[39;49;00m$
string = [33m%q<[39;49;00m[33mJon 'Maddog' Orwant[39;49;00m[33m>[39;49;00m  [37m# literal single quotes[39;49;00m$
$
a = <<[33m"[39;49;00m[33mEOF[39;49;00m[33m"[39;49;00m$
[33mThis is a multiline here document[39;49;00m$
[33mterminated by EOF on a line by itself[39;49;00m$
[33mEOF[39;49;00m$
$
$
[37m# @@PLEAC@@_1.1[39;49;00m$
value = string[offset,count]$
value = string[offset..-[34m1[39;49;00m]$
$
string[offset,count] = newstring$
string[offset..-[34m1[39;49;00m]   = newtail$
$
[37m# in Ruby we can also specify intervals by their two offsets[39;49;00m$
value = string[offset..offs2]$
string[offset..offs2] = newstring$
$
leading, s1, s2, trailing = data.unpack([33m"[39;49;00m[33mA5 x3 A8 A8 A*[39;49;00m[33m"[39;49;00m)$
$
fivers = string.unpack([33m"[39;49;00m[33mA5[39;49;00m[33m"[39;49;00m * (string.length/[34m5[39;49;00m))$
$
chars = string.unpack([33m"[39;49;00m[33mA1[39;49;00m[33m"[39;49;00m * string.length)$
$
string = [33m"[39;49;00m[33mThis is what you have[39;49;00m[33m"[39;49;00m$
[37m#        +012345678901234567890  Indexing forwards  (left to right)[39;49;00m$
[37m#         109876543210987654321- Indexing backwards (right to left)[39;49;00m$
[37m#          note that 0 means 10 or 20, etc. above[39;49;00m$
$
first  = string[[34m0[39;49;00m, [34m1[39;49;00m]       [37m# "T"[39;49;00m$
start  = string[[34m5[39;49;00m, [34m2[39;49;00m]       [37m# "is"[39;49;00m$
rest   = string[[34m13[39;49;00m..-[34m1[39;49;00m]     [37m# "you have"[39;49;00m$
last   = string[-[34m1[39;49;00m, [34m1[39;49;00m]      [37m# "e"[39;49;00m$
end_   = string[-[34m4[39;49;00m..-[34m1[39;49;00m]     [37m# "have"[39;49;00m$
piece  = string[-[34m8[39;49;00m, [34m3[39;49;00m]      [37m# "you"[39;49;00m$
$
string[[34m5[39;49;00m, [34m2[39;49;00m] = [33m"[39;49;00m[33mwasn't[39;49;00m[33m"[39;49;00m     [37m# change "is" to "wasn't"[39;49;00m$
string[-[34m12[39;49;00m..-[34m1[39;49;00m] = [33m"[39;49;00m[33mondrous[39;49;00m[33m"[39;49;00m [37m# "This wasn't wondrous"[39;49;00m$
string[[34m0[39;49;00m, [34m1[39;49;00m] = [33m"[39;49;00m[33m"[39;49;00m           [37m# delete first character[39;49;00m$
string[-[34m10[39;49;00m..-[34m1[39;49;00m]  = [33m"[39;49;00m[33m"[39;49;00m       [37m# delete last 10 characters[39;49;00m$
$
[34mif[39;49;00m string[-[34m10[39;49;00m..-[34m1[39;49;00m] =~ [33m/[39;49;00m[33mpattern[39;49;00m[33m/[39;49;00m$
    [36mputs[39;49;00m [33m"[39;49;00m[33mPattern matches in last 10 characters[39;49;00m[33m"[39;49;00m$
[34mend[39;49;00m$
$
string[[34m0[39;49;00m, [34m5[39;49;00m].gsub!([33m/[39;49;00m[33mis[39;49;00m[33m/[39;49;00m, [33m'[39;49;00m[33mat[39;49;00m[33m'[39;49;00m)$
$
a = [33m"[39;49;00m[33mmake a hat[39;49;00m[33m"[39;49;00m$
a[[34m0[39;49;00m, [34m1[39;49;00m], a[-[34m1[39;49;00m, [34m1[39;49;00m] = a[-[34m1[39;49;00m, [34m1[39;49;00m], a[[34m0[39;49;00m, [34m1[39;49;00m]$
$
a = [33m"[39;49;00m[33mTo be or not to be[39;49;00m[33m"[39;49;00m$
b = a.unpack([33m"[39;49;00m[33mx6 A6[39;49;00m[33m"[39;49;00m)$
$
b, c = a.unpack([33m"[39;49;00m[33mx6 A2 X5 A2[39;49;00m[33m"[39;49;00m)$
[36mputs[39;49;00m [33m"[39;49;00m[33m#{[39;49;00mb[33m}[39;49;00m[33m\n[39;49;00m[33m#{[39;49;00mc[33m}[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
$
[34mdef[39;49;00m [32mcut2fmt[39;49;00m(*args)$
    template = [33m'[39;49;00m[33m'[39;49;00m$
    lastpos  = [34m1[39;49;00m$
    [34mfor[39;49;00m place [34min[39;49;00m args$
        template += [33m"[39;49;00m[33mA[39;49;00m[33m"[39;49;00m + (place - lastpos).to_s + [33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m$
        lastpos   = place$
    [34mend[39;49;00m$
    template += [33m"[39;49;00m[33mA*[39;49;00m[33m"[39;49;00m$
    [34mreturn[39;49;00m template$
[34mend[39;49;00m$
$
fmt = cut2fmt([34m8[39;49;00m, [34m14[39;49;00m, [34m20[39;49;00m, [34m26[39;49;00m, [34m30[39;49;00m)$
$
$
[37m# @@PLEAC@@_1.2[39;49;00m$
[37m# careful! "b is true" doesn't mean "b != 0" (0 is true in Ruby)[39;49;00m$
[37m# thus no problem of "defined" later since only nil is false[39;49;00m$
[37m# the following sets to `c' if `b' is nil or false[39;49;00m$
a = b || c$
$
[37m# if you need Perl's behaviour (setting to `c' if `b' is 0) the most[39;49;00m$
[37m# effective way is to use Numeric#nonzero? (thanks to Dave Thomas!)[39;49;00m$
a = b.nonzero? || c$
$
[37m# you will still want to use defined? in order to test[39;49;00m$
[37m# for scope existence of a given object[39;49;00m$
a = defined?(b) ? b : c$
$
dir = [31mARGV[39;49;00m.shift || [33m"[39;49;00m[33m/tmp[39;49;00m[33m"[39;49;00m$
$
$
[37m# @@PLEAC@@_1.3[39;49;00m$
v1, v2 = v2, v1$
$
alpha, beta, production = [33m%w([39;49;00m[33mJanuary March August[39;49;00m[33m)[39;49;00m$
alpha, beta, production = beta, production, alpha$
$
$
[37m# @@PLEAC@@_1.4[39;49;00m$
num = char[[34m0[39;49;00m]$
char = num.chr$
$
[37m# Ruby also supports having a char from character constant[39;49;00m$
num = [33m?r[39;49;00m$
$
char = [36msprintf[39;49;00m([33m"[39;49;00m[33m%c[39;49;00m[33m"[39;49;00m, num)$
[36mprintf[39;49;00m([33m"[39;49;00m[33mNumber %d is character %c[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m, num, num)$
$
ascii = string.unpack([33m"[39;49;00m[33mC*[39;49;00m[33m"[39;49;00m)$
string = ascii.pack([33m"[39;49;00m[33mC*[39;49;00m[33m"[39;49;00m)$
$
hal = [33m"[39;49;00m[33mHAL[39;49;00m[33m"[39;49;00m$
ascii = hal.unpack([33m"[39;49;00m[33mC*[39;49;00m[33m"[39;49;00m)$
[37m# We can't use Array#each since we can't mutate a Fixnum[39;49;00m$
ascii.collect! { |i|$
    i + [34m1[39;49;00m                         [37m# add one to each ASCII value[39;49;00m$
}                $
ibm = ascii.pack([33m"[39;49;00m[33mC*[39;49;00m[33m"[39;49;00m)$
[36mputs[39;49;00m ibm$
$
$
[37m# @@PLEAC@@_1.5[39;49;00m$
array = string.split([33m'[39;49;00m[33m'[39;49;00m)$
$
array = string.unpack([33m"[39;49;00m[33mC*[39;49;00m[33m"[39;49;00m)$
$
string.scan([33m/[39;49;00m[33m.[39;49;00m[33m/[39;49;00m) { |b|$
    [37m# do something with b[39;49;00m$
}$
$
string = [33m"[39;49;00m[33man apple a day[39;49;00m[33m"[39;49;00m$
[36mprint[39;49;00m [33m"[39;49;00m[33munique chars are: [39;49;00m[33m"[39;49;00m, string.split([33m'[39;49;00m[33m'[39;49;00m).uniq.sort, [33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
$
sum = [34m0[39;49;00m$
[34mfor[39;49;00m ascval [34min[39;49;00m string.unpack([33m"[39;49;00m[33mC*[39;49;00m[33m"[39;49;00m) [37m# or use Array#each for a pure OO style :)[39;49;00m$
    sum += ascval$
[34mend[39;49;00m$
[36mputs[39;49;00m [33m"[39;49;00m[33msum is [39;49;00m[33m#{[39;49;00msum & [34m0xffffffff[39;49;00m[33m}[39;49;00m[33m"[39;49;00m [37m# since Ruby will go Bignum if necessary[39;49;00m$
$
[37m# @@INCLUDE@@ include/ruby/slowcat.rb[39;49;00m$
$
$
[37m# @@PLEAC@@_1.6[39;49;00m$
revbytes = string.reverse$
$
revwords = string.split([33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m).reverse.join([33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m)$
$
revwords = string.split([33m/[39;49;00m[33m([39;49;00m[33m\[39;49;00m[33ms+)[39;49;00m[33m/[39;49;00m).reverse.join$
$
[37m# using the fact that IO is Enumerable, you can directly "select" it[39;49;00m$
long_palindromes = [31mFile[39;49;00m.open([33m"[39;49;00m[33m/usr/share/dict/words[39;49;00m[33m"[39;49;00m).$
    [36mselect[39;49;00m { |w| w.chomp!; w.reverse == w && w.length > [34m5[39;49;00m }$
$
$
[37m# @@PLEAC@@_1.7[39;49;00m$
[34mwhile[39;49;00m string.sub!([33m"[39;49;00m[33m\t[39;49;00m[33m+[39;49;00m[33m"[39;49;00m) { [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m * ([31m$&[39;49;00m.length * [34m8[39;49;00m - [31m$`[39;49;00m.length % [34m8[39;49;00m) }$
[34mend[39;49;00m$
$
$
[37m# @@PLEAC@@_1.8[39;49;00m$
[33m'[39;49;00m[33mYou owe [39;49;00m[33m#{[39;49;00mdebt[33m}[39;49;00m[33m to me[39;49;00m[33m'[39;49;00m.gsub([33m/[39;49;00m[33m\[39;49;00m[33m#{[39;49;00m(\w+)[33m}[39;49;00m[33m/[39;49;00m) { [36meval[39;49;00m([31m$1[39;49;00m) }$
$
rows, cols = [34m24[39;49;00m, [34m80[39;49;00m$
text = [33m%q([39;49;00m[33mI am [39;49;00m[33m#[39;49;00m[33m{rows} high and [39;49;00m[33m#[39;49;00m[33m{cols} long[39;49;00m[33m)[39;49;00m$
text.gsub!([33m/[39;49;00m[33m\[39;49;00m[33m#{[39;49;00m(\w+)[33m}[39;49;00m[33m/[39;49;00m) { [36meval[39;49;00m([33m"[39;49;00m[33m#{[39;49;00m[31m$1[39;49;00m[33m}[39;49;00m[33m"[39;49;00m) }$
[36mputs[39;49;00m text$
$
[33m'[39;49;00m[33mI am 17 years old[39;49;00m[33m'[39;49;00m.gsub([33m/[39;49;00m[33m\[39;49;00m[33md+[39;49;00m[33m/[39;49;00m) { [34m2[39;49;00m * [31m$&[39;49;00m.to_i }$
$
$
[37m# @@PLEAC@@_1.9[39;49;00m$
e = [33m"[39;49;00m[33mbo peep[39;49;00m[33m"[39;49;00m.upcase$
e.downcase!$
e.capitalize!$
$
[33m"[39;49;00m[33mthIS is a loNG liNE[39;49;00m[33m"[39;49;00m.gsub!([33m/[39;49;00m[33m\[39;49;00m[33mw+[39;49;00m[33m/[39;49;00m) { [31m$&[39;49;00m.capitalize }$
$
$
[37m# @@PLEAC@@_1.10[39;49;00m$
[33m"[39;49;00m[33mI have [39;49;00m[33m#{[39;49;00mn+[34m1[39;49;00m[33m}[39;49;00m[33m guanacos.[39;49;00m[33m"[39;49;00m$
[36mprint[39;49;00m [33m"[39;49;00m[33mI have [39;49;00m[33m"[39;49;00m, n+[34m1[39;49;00m, [33m"[39;49;00m[33m guanacos.[39;49;00m[33m"[39;49;00m$
$
$
[37m# @@PLEAC@@_1.11[39;49;00m$
var = <<[33m'[39;49;00m[33mEOF[39;49;00m[33m'[39;49;00m.gsub([33m/[39;49;00m[33m^[39;49;00m[33m\[39;49;00m[33ms+[39;49;00m[33m/[39;49;00m, [33m'[39;49;00m[33m'[39;49;00m)$
[33m    your text[39;49;00m$
[33m    goes here[39;49;00m$
[33mEOF[39;49;00m$
$
$
[37m# @@PLEAC@@_1.12[39;49;00m$
string = [33m"[39;49;00m[33mFolding and splicing is the work of an editor,[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m+$
    [33m"[39;49;00m[33mnot a mere collection of silicon[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m+ $
    [33m"[39;49;00m[33mand[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m+$
    [33m"[39;49;00m[33mmobile electrons![39;49;00m[33m"[39;49;00m$
$
[34mdef[39;49;00m [32mwrap[39;49;00m(str, max_size)$
    all = []$
    line = [33m'[39;49;00m[33m'[39;49;00m$
    [34mfor[39;49;00m l [34min[39;49;00m str.split$
        [34mif[39;49;00m (line+l).length >= max_size$
            all.push(line)$
            line = [33m'[39;49;00m[33m'[39;49;00m$
        [34mend[39;49;00m$
        line += line == [33m'[39;49;00m[33m'[39;49;00m ? l : [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m + l$
    [34mend[39;49;00m$
    all.push(line).join([33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m)$
[34mend[39;49;00m$
$
[36mprint[39;49;00m wrap(string, [34m20[39;49;00m)$
[37m#=> Folding and [39;49;00m$
[37m#=> splicing is the [39;49;00m$
[37m#=> work of an editor, [39;49;00m$
[37m#=> not a mere [39;49;00m$
[37m#=> collection of [39;49;00m$
[37m#=> silicon and mobile [39;49;00m$
[37m#=> electrons![39;49;00m$
$
$
[37m# @@PLEAC@@_1.13[39;49;00m$
string = [33m%q([39;49;00m[33mMom said, "Don't do that."[39;49;00m[33m)[39;49;00m$
string.gsub([33m/[39;49;00m[33m['"][39;49;00m[33m/[39;49;00m) { [33m'[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m+[31m$&[39;49;00m }$
string.gsub([33m/[39;49;00m[33m['"][39;49;00m[33m/[39;49;00m, [33m'[39;49;00m[33m\[39;49;00m[33m&[39;49;00m[33m\[39;49;00m[33m&[39;49;00m[33m'[39;49;00m)$
string.gsub([33m/[39;49;00m[33m[^A-Z][39;49;00m[33m/[39;49;00m) { [33m'[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m+[31m$&[39;49;00m }$
[33m"[39;49;00m[33mis a test![39;49;00m[33m"[39;49;00m.gsub([33m/[39;49;00m[33m\[39;49;00m[33mW[39;49;00m[33m/[39;49;00m) { [33m'[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m+[31m$&[39;49;00m }  [37m# no function like quotemeta?[39;49;00m$
$
$
[37m# @@PLEAC@@_1.14[39;49;00m$
string.strip!$
$
$
[37m# @@PLEAC@@_1.15[39;49;00m$
[34mdef[39;49;00m [32mparse_csv[39;49;00m(text)$
    [34mnew[39;49;00m = text.scan([33m/[39;49;00m[33m"([^[39;49;00m[33m\[39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m]*(?:[39;49;00m[33m\\[39;49;00m[33m.[^[39;49;00m[33m\[39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m]*)*)",?|([^,]+),?|,[39;49;00m[33m/[39;49;00m)$
    [34mnew[39;49;00m << [34mnil[39;49;00m [34mif[39;49;00m text[-[34m1[39;49;00m] == [33m?,[39;49;00m$
    [34mnew[39;49;00m.flatten.compact$
[34mend[39;49;00m  $
$
line = [33m%q<[39;49;00m[33mXYZZY,"","O'Reilly, Inc","Wall, Larry","a [39;49;00m[33m\[39;49;00m[33m"glug[39;49;00m[33m\[39;49;00m[33m" bit,",5,"Error, Core Dumped"[39;49;00m[33m>[39;49;00m$
fields = parse_csv(line)$
fields.each_with_index { |v,i|$
    [36mprint[39;49;00m [33m"[39;49;00m[33m#{[39;49;00mi[33m}[39;49;00m[33m : [39;49;00m[33m#{[39;49;00mv[33m}[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m;$
}$
$
$
[37m# @@PLEAC@@_1.16[39;49;00m$
[37m# Use the soundex.rb Library from Michael Neumann.[39;49;00m$
[37m# http://www.s-direktnet.de/homepages/neumann/rb_prgs/Soundex.rb[39;49;00m$
[36mrequire[39;49;00m [33m'[39;49;00m[33mSoundex[39;49;00m[33m'[39;49;00m$
$
code = [31mText[39;49;00m::[31mSoundex[39;49;00m.soundex(string)$
codes = [31mText[39;49;00m::[31mSoundex[39;49;00m.soundex(array)$
$
[37m# substitution function for getpwent():[39;49;00m$
[37m# returns an array of user entries,[39;49;00m$
[37m# each entry contains the username and the full name[39;49;00m$
[34mdef[39;49;00m [32mlogin_names[39;49;00m$
    result = []$
    [31mFile[39;49;00m.open([33m"[39;49;00m[33m/etc/passwd[39;49;00m[33m"[39;49;00m) { |file|$
        file.each_line { |line|$
            [34mnext[39;49;00m [34mif[39;49;00m line.match([33m/[39;49;00m[33m^[39;49;00m[33m#[39;49;00m[33m/[39;49;00m)$
            cols = line.split([33m"[39;49;00m[33m:[39;49;00m[33m"[39;49;00m)$
            result.push([cols[[34m0[39;49;00m], cols[[34m4[39;49;00m]])$
        }$
    }$
    result$
[34mend[39;49;00m$
$
[36mputs[39;49;00m [33m"[39;49;00m[33mLookup user: [39;49;00m[33m"[39;49;00m$
user = [31mSTDIN[39;49;00m.gets$
user.chomp!$
[36mexit[39;49;00m [34munless[39;49;00m user$
name_code = [31mText[39;49;00m::[31mSoundex[39;49;00m.soundex(user)$
$
splitter = [31mRegexp[39;49;00m.new([33m'[39;49;00m[33m([39;49;00m[33m\[39;49;00m[33mw+)[^,]*[39;49;00m[33m\b[39;49;00m[33m([39;49;00m[33m\[39;49;00m[33mw+)[39;49;00m[33m'[39;49;00m)$
[34mfor[39;49;00m username, fullname [34min[39;49;00m login_names [34mdo[39;49;00m$
    firstname, lastname = splitter.match(fullname)[[34m1[39;49;00m,[34m2[39;49;00m]$
    [34mif[39;49;00m name_code == [31mText[39;49;00m::[31mSoundex[39;49;00m.soundex(username)$
        || name_code == [31mText[39;49;00m::[31mSoundex[39;49;00m.soundex(firstname)$
        || name_code == [31mText[39;49;00m::[31mSoundex[39;49;00m.soundex(lastname)$
    [34mthen[39;49;00m$
        [36mputs[39;49;00m [33m"[39;49;00m[33m#{[39;49;00musername[33m}[39;49;00m[33m: [39;49;00m[33m#{[39;49;00mfirstname[33m}[39;49;00m[33m [39;49;00m[33m#{[39;49;00mlastname[33m}[39;49;00m[33m"[39;49;00m$
    [34mend[39;49;00m$
[34mend[39;49;00m$
$
$
[37m# @@PLEAC@@_1.17[39;49;00m$
[37m# @@INCLUDE@@ include/ruby/fixstyle.rb[39;49;00m$
$
$
[37m# @@PLEAC@@_1.18[39;49;00m$
[37m# @@INCLUDE@@ include/ruby/psgrep.rb[39;49;00m$
$
$
[37m# @@PLEAC@@_2.1[39;49;00m$
[37m# Matz tells that you can use Integer() for strict checked conversion.[39;49;00m$
[36mInteger[39;49;00m([33m"[39;49;00m[33mabc[39;49;00m[33m"[39;49;00m)$
[37m#=> `Integer': invalid value for Integer: "abc" (ArgumentError)[39;49;00m$
[36mInteger[39;49;00m([33m"[39;49;00m[33m567[39;49;00m[33m"[39;49;00m)$
[37m#=> 567[39;49;00m$
$
[37m# You may use Float() for floating point stuff[39;49;00m$
[36mInteger[39;49;00m([33m"[39;49;00m[33m56.7[39;49;00m[33m"[39;49;00m)$
[37m#=> `Integer': invalid value for Integer: "56.7" (ArgumentError)[39;49;00m$
[36mFloat[39;49;00m([33m"[39;49;00m[33m56.7[39;49;00m[33m"[39;49;00m)$
[37m#=> 56.7[39;49;00m$
$
[37m# You may also use a regexp for that[39;49;00m$
[34mif[39;49;00m string =~ [33m/[39;49;00m[33m^[+-]?[39;49;00m[33m\[39;49;00m[33md+$[39;49;00m[33m/[39;49;00m$
    [36mp[39;49;00m [33m'[39;49;00m[33mis an integer[39;49;00m[33m'[39;49;00m$
[34melse[39;49;00m$
    [36mp[39;49;00m [33m'[39;49;00m[33mis not[39;49;00m[33m'[39;49;00m$
[34mend[39;49;00m$
$
[34mif[39;49;00m string =~ [33m/[39;49;00m[33m^-?(?:[39;49;00m[33m\[39;49;00m[33md+(?:[39;49;00m[33m\[39;49;00m[33m.[39;49;00m[33m\[39;49;00m[33md*)?|[39;49;00m[33m\[39;49;00m[33m.[39;49;00m[33m\[39;49;00m[33md+)$[39;49;00m[33m/[39;49;00m$
    [36mp[39;49;00m [33m'[39;49;00m[33mis a decimal number[39;49;00m[33m'[39;49;00m$
[34melse[39;49;00m$
    [36mp[39;49;00m [33m'[39;49;00m[33mis not[39;49;00m[33m'[39;49;00m$
[34mend[39;49;00m$
$
$
[37m# @@PLEAC@@_2.2[39;49;00m$
[37m# equal(num1, num2, accuracy) : returns true if num1 and num2 are[39;49;00m$
[37m#   equal to accuracy number of decimal places[39;49;00m$
[34mdef[39;49;00m [32mequal[39;49;00m(i, j, a)$
    [36msprintf[39;49;00m([33m"[39;49;00m[33m%.[39;49;00m[33m#{[39;49;00ma[33m}[39;49;00m[33mg[39;49;00m[33m"[39;49;00m, i) == [36msprintf[39;49;00m([33m"[39;49;00m[33m%.[39;49;00m[33m#{[39;49;00ma[33m}[39;49;00m[33mg[39;49;00m[33m"[39;49;00m, j)$
[34mend[39;49;00m$
$
wage = [34m536[39;49;00m                        [37m# $5.36/hour[39;49;00m$
week = [34m40[39;49;00m * wage                  [37m# $214.40[39;49;00m$
[36mprintf[39;49;00m([33m"[39;49;00m[33mOne week's wage is: [39;49;00m[33m\[39;49;00m[33m$%.2f[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m, week/[34m100[39;49;00m.[34m0[39;49;00m)$
$
$
[37m# @@PLEAC@@_2.3[39;49;00m$
num.round                         [37m# rounds to integer[39;49;00m$
$
a = [34m0[39;49;00m.[34m255[39;49;00m$
b = [36msprintf[39;49;00m([33m"[39;49;00m[33m%.2f[39;49;00m[33m"[39;49;00m, a)$
[36mprint[39;49;00m  [33m"[39;49;00m[33mUnrounded: [39;49;00m[33m#{[39;49;00ma[33m}[39;49;00m[33m\n[39;49;00m[33mRounded: [39;49;00m[33m#{[39;49;00mb[33m}[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
[36mprintf[39;49;00m [33m"[39;49;00m[33mUnrounded: [39;49;00m[33m#{[39;49;00ma[33m}[39;49;00m[33m\n[39;49;00m[33mRounded: %.2f[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m, a$
$
[36mprint[39;49;00m [33m"[39;49;00m[33mnumber[39;49;00m[33m\t[39;49;00m[33mint[39;49;00m[33m\t[39;49;00m[33mfloor[39;49;00m[33m\t[39;49;00m[33mceil[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
a = [ [34m3[39;49;00m.[34m3[39;49;00m , [34m3[39;49;00m.[34m5[39;49;00m , [34m3[39;49;00m.[34m7[39;49;00m, -[34m3[39;49;00m.[34m3[39;49;00m ]$
[34mfor[39;49;00m n [34min[39;49;00m a$
    [36mprintf[39;49;00m([33m"[39;49;00m[33m% .1f[39;49;00m[33m\t[39;49;00m[33m% .1f[39;49;00m[33m\t[39;49;00m[33m% .1f[39;49;00m[33m\t[39;49;00m[33m% .1f[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m,  [37m# at least I don't fake my output :)[39;49;00m$
           n, n.to_i, n.floor, n.ceil)$
[34mend[39;49;00m$
$
$
[37m# @@PLEAC@@_2.4[39;49;00m$
[34mdef[39;49;00m [32mdec2bin[39;49;00m(n)$
    [n].pack([33m"[39;49;00m[33mN[39;49;00m[33m"[39;49;00m).unpack([33m"[39;49;00m[33mB32[39;49;00m[33m"[39;49;00m)[[34m0[39;49;00m].sub([33m/[39;49;00m[33m^0+(?=[39;49;00m[33m\[39;49;00m[33md)[39;49;00m[33m/[39;49;00m, [33m'[39;49;00m[33m'[39;49;00m)$
[34mend[39;49;00m$
$
[34mdef[39;49;00m [32mbin2dec[39;49;00m(n)$
    [([33m"[39;49;00m[33m0[39;49;00m[33m"[39;49;00m*[34m32[39;49;00m+n.to_s)[-[34m32[39;49;00m..-[34m1[39;49;00m]].pack([33m"[39;49;00m[33mB32[39;49;00m[33m"[39;49;00m).unpack([33m"[39;49;00m[33mN[39;49;00m[33m"[39;49;00m)[[34m0[39;49;00m]$
[34mend[39;49;00m$
$
$
[37m# @@PLEAC@@_2.5[39;49;00m$
[34mfor[39;49;00m i [34min[39;49;00m x .. y$
    [37m# i is set to every integer from x to y, inclusive[39;49;00m$
[34mend[39;49;00m$
$
x.step(y,[34m7[39;49;00m) { |i|$
    [37m# i is set to every integer from x to y, stepsize = 7[39;49;00m$
}$
$
[36mprint[39;49;00m [33m"[39;49;00m[33mInfancy is: [39;49;00m[33m"[39;49;00m$
([34m0[39;49;00m..[34m2[39;49;00m).each { |i|$
    [36mprint[39;49;00m i, [33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m$
}$
[36mprint[39;49;00m [33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
$
$
[37m# @@PLEAC@@_2.6[39;49;00m$
[37m# We can add conversion methods to the Integer class,[39;49;00m$
[37m# this makes a roman number just a representation for normal numbers.[39;49;00m$
[34mclass[39;49;00m [04m[32mInteger[39;49;00m$
    $
    [31m@@romanlist[39;49;00m = [[[33m"[39;49;00m[33mM[39;49;00m[33m"[39;49;00m, [34m1000[39;49;00m],$
                   [[33m"[39;49;00m[33mCM[39;49;00m[33m"[39;49;00m, [34m900[39;49;00m],$
                   [[33m"[39;49;00m[33mD[39;49;00m[33m"[39;49;00m,  [34m500[39;49;00m],$
                   [[33m"[39;49;00m[33mCD[39;49;00m[33m"[39;49;00m, [34m400[39;49;00m],$
                   [[33m"[39;49;00m[33mC[39;49;00m[33m"[39;49;00m,  [34m100[39;49;00m],$
                   [[33m"[39;49;00m[33mXC[39;49;00m[33m"[39;49;00m,  [34m90[39;49;00m],$
                   [[33m"[39;49;00m[33mL[39;49;00m[33m"[39;49;00m,   [34m50[39;49;00m],$
                   [[33m"[39;49;00m[33mXL[39;49;00m[33m"[39;49;00m,  [34m40[39;49;00m],$
                   [[33m"[39;49;00m[33mX[39;49;00m[33m"[39;49;00m,   [34m10[39;49;00m],$
                   [[33m"[39;49;00m[33mIX[39;49;00m[33m"[39;49;00m,   [34m9[39;49;00m],$
                   [[33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m,    [34m5[39;49;00m],$
                   [[33m"[39;49;00m[33mIV[39;49;00m[33m"[39;49;00m,   [34m4[39;49;00m],$
                   [[33m"[39;49;00m[33mI[39;49;00m[33m"[39;49;00m,    [34m1[39;49;00m]]$
    $
    [34mdef[39;49;00m [32mto_roman[39;49;00m$
        remains = [36mself[39;49;00m$
        roman = [33m"[39;49;00m[33m"[39;49;00m$
        [34mfor[39;49;00m sym, num [34min[39;49;00m [31m@@romanlist[39;49;00m$
            [34mwhile[39;49;00m remains >= num$
                remains -= num$
                roman << sym$
            [34mend[39;49;00m$
        [34mend[39;49;00m$
        roman$
    [34mend[39;49;00m$
    $
    [34mdef[39;49;00m [04m[32mInteger[39;49;00m.[32mfrom_roman[39;49;00m(roman)$
        ustr = roman.upcase$
        sum = [34m0[39;49;00m$
        [34mfor[39;49;00m entry [34min[39;49;00m [31m@@romanlist[39;49;00m$
            sym, num = entry[[34m0[39;49;00m], entry[[34m1[39;49;00m]$
            [34mwhile[39;49;00m sym == ustr[[34m0[39;49;00m, sym.length]$
                sum += num$
                ustr.slice!([34m0[39;49;00m, sym.length)$
            [34mend[39;49;00m$
        [34mend[39;49;00m$
        sum$
    [34mend[39;49;00m$
    $
[34mend[39;49;00m$
$
$
roman_fifteen = [34m15[39;49;00m.to_roman$
[36mputs[39;49;00m [33m"[39;49;00m[33mRoman for fifteen is [39;49;00m[33m#{[39;49;00mroman_fifteen[33m}[39;49;00m[33m"[39;49;00m$
i = [36mInteger[39;49;00m.from_roman(roman_fifteen)$
[36mputs[39;49;00m [33m"[39;49;00m[33mConverted back, [39;49;00m[33m#{[39;49;00mroman_fifteen[33m}[39;49;00m[33m is [39;49;00m[33m#{[39;49;00mi[33m}[39;49;00m[33m"[39;49;00m$
$
[37m# check[39;49;00m$
[34mfor[39;49;00m i [34min[39;49;00m ([34m1[39;49;00m..[34m3900[39;49;00m)$
    r = i.to_roman$
    j = [36mInteger[39;49;00m.from_roman(r)$
    [34mif[39;49;00m i != j$
        [36mputs[39;49;00m [33m"[39;49;00m[33merror: [39;49;00m[33m#{[39;49;00mi[33m}[39;49;00m[33m : [39;49;00m[33m#{[39;49;00mr[33m}[39;49;00m[33m - [39;49;00m[33m#{[39;49;00mj[33m}[39;49;00m[33m"[39;49;00m$
    [34mend[39;49;00m$
[34mend[39;49;00m$
$
$
[37m# @@PLEAC@@_2.7[39;49;00m$
random = [36mrand[39;49;00m(y-x+[34m1[39;49;00m)+x$
$
chars = [[33m"[39;49;00m[33mA[39;49;00m[33m"[39;49;00m..[33m"[39;49;00m[33mZ[39;49;00m[33m"[39;49;00m,[33m"[39;49;00m[33ma[39;49;00m[33m"[39;49;00m..[33m"[39;49;00m[33mz[39;49;00m[33m"[39;49;00m,[33m"[39;49;00m[33m0[39;49;00m[33m"[39;49;00m..[33m"[39;49;00m[33m9[39;49;00m[33m"[39;49;00m].collect { |r| r.to_a }.join + [33m%q([39;49;00m[33m!@$%^&*[39;49;00m[33m)[39;49;00m$
password = ([34m1[39;49;00m..[34m8[39;49;00m).collect { chars[[36mrand[39;49;00m(chars.size)] }.pack([33m"[39;49;00m[33mC*[39;49;00m[33m"[39;49;00m)$
$
$
[37m# @@PLEAC@@_2.8[39;49;00m$
[36msrand[39;49;00m        [37m# uses a combination of the time, the process id, and a sequence number[39;49;00m$
[36msrand[39;49;00m(val)   [37m# for repeatable behaviour[39;49;00m$
$
$
[37m# @@PLEAC@@_2.9[39;49;00m$
[37m# from the randomr lib: [39;49;00m$
[37m# http://raa.ruby-lang.org/project/randomr/[39;49;00m$
----> [33mhttp[39;49;00m:[33m/[39;49;00m[33m/[39;49;00mraa.ruby-lang.org/project/randomr/$
$
[36mrequire[39;49;00m [33m'[39;49;00m[33mrandom/mersenne_twister[39;49;00m[33m'[39;49;00m$
mers = [31mRandom[39;49;00m::[31mMersenneTwister[39;49;00m.new [34m123456789[39;49;00m$
[36mputs[39;49;00m mers.rand([34m0[39;49;00m)    [37m# 0.550321932544541[39;49;00m$
[36mputs[39;49;00m mers.rand([34m10[39;49;00m)   [37m# 2[39;49;00m$
$
[37m# using online sources of random data via the realrand package:[39;49;00m$
[37m# http://raa.ruby-lang.org/project/realrand/[39;49;00m$
[37m# **Note**[39;49;00m$
[37m# The following online services are used in this package:[39;49;00m$
[37m#   http://www.random.org - source: atmospheric noise [39;49;00m$
[37m#   http://www.fourmilab.ch/hotbits - source: radioactive decay timings[39;49;00m$
[37m#   http://random.hd.org - source: entropy from local and network noise[39;49;00m$
[37m# Please visit the sites and respect the rules of each service.[39;49;00m$
$
[36mrequire[39;49;00m [33m'[39;49;00m[33mrandom/online[39;49;00m[33m'[39;49;00m$
$
generator1 = [31mRandom[39;49;00m::[31mRandomOrg[39;49;00m.new$
[36mputs[39;49;00m generator1.randbyte([34m5[39;49;00m).join([33m"[39;49;00m[33m,[39;49;00m[33m"[39;49;00m)$
[36mputs[39;49;00m generator1.randnum([34m10[39;49;00m, [34m1[39;49;00m, [34m6[39;49;00m).join([33m"[39;49;00m[33m,[39;49;00m[33m"[39;49;00m)  [37m# Roll dice 10 times.[39;49;00m$
$
generator2 = [31mRandom[39;49;00m::[31mFourmiLab[39;49;00m.new$
[36mputs[39;49;00m generator2.randbyte([34m5[39;49;00m).join([33m"[39;49;00m[33m,[39;49;00m[33m"[39;49;00m)$
[37m# randnum is not supported.[39;49;00m$
$
generator3 = [31mRandom[39;49;00m::[31mEntropyPool[39;49;00m.new$
[36mputs[39;49;00m generator3.randbyte([34m5[39;49;00m).join([33m"[39;49;00m[33m,[39;49;00m[33m"[39;49;00m)$
[37m# randnum is not supported.[39;49;00m$
$
$
[37m# @@PLEAC@@_2.10[39;49;00m$
[34mdef[39;49;00m [32mgaussian_rand[39;49;00m$
    [34mbegin[39;49;00m$
        u1 = [34m2[39;49;00m * [36mrand[39;49;00m() - [34m1[39;49;00m$
        u2 = [34m2[39;49;00m * [36mrand[39;49;00m() - [34m1[39;49;00m$
        w = u1*u1 + u2*u2$
    [34mend[39;49;00m [34mwhile[39;49;00m (w >= [34m1[39;49;00m)$
    w = [31mMath[39;49;00m.sqrt((-[34m2[39;49;00m*[31mMath[39;49;00m.log(w))/w)$
    [ u2*w, u1*w ]$
[34mend[39;49;00m$
$
mean = [34m25[39;49;00m$
sdev = [34m2[39;49;00m$
salary = gaussian_rand[[34m0[39;49;00m] * sdev + mean$
[36mprintf[39;49;00m([33m"[39;49;00m[33mYou have been hired at [39;49;00m[33m\[39;49;00m[33m$%.2f[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m, salary)$
$
$
[37m# @@PLEAC@@_2.11[39;49;00m$
[34mdef[39;49;00m [32mdeg2rad[39;49;00m(d)$
    (d/[34m180[39;49;00m.[34m0[39;49;00m)*[31mMath[39;49;00m::[31mPI[39;49;00m$
[34mend[39;49;00m$
$
[34mdef[39;49;00m [32mrad2deg[39;49;00m(r)$
    (r/[31mMath[39;49;00m::[31mPI[39;49;00m)*[34m180[39;49;00m$
[34mend[39;49;00m$
$
$
[37m# @@PLEAC@@_2.12[39;49;00m$
sin_val = [31mMath[39;49;00m.sin(angle)$
cos_val = [31mMath[39;49;00m.cos(angle)$
tan_val = [31mMath[39;49;00m.tan(angle)$
$
[37m# AFAIK Ruby's Math module doesn't provide acos/asin[39;49;00m$
[37m# While we're at it, let's also define missing hyperbolic functions[39;49;00m$
[34mmodule[39;49;00m [04m[36mMath[39;49;00m$
    [34mdef[39;49;00m [04m[32mMath[39;49;00m.[32masin[39;49;00m(x)$
        atan2(x, sqrt([34m1[39;49;00m - x**[34m2[39;49;00m))$
    [34mend[39;49;00m$
    [34mdef[39;49;00m [04m[32mMath[39;49;00m.[32macos[39;49;00m(x)$
        atan2(sqrt([34m1[39;49;00m - x**[34m2[39;49;00m), x)$
    [34mend[39;49;00m$
    [34mdef[39;49;00m [04m[32mMath[39;49;00m.[32matan[39;49;00m(x)$
        atan2(x, [34m1[39;49;00m)$
    [34mend[39;49;00m$
    [34mdef[39;49;00m [04m[32mMath[39;49;00m.[32msinh[39;49;00m(x)$
        (exp(x) - exp(-x)) / [34m2[39;49;00m$
    [34mend[39;49;00m$
    [34mdef[39;49;00m [04m[32mMath[39;49;00m.[32mcosh[39;49;00m(x)$
        (exp(x) + exp(-x)) / [34m2[39;49;00m$
    [34mend[39;49;00m$
    [34mdef[39;49;00m [04m[32mMath[39;49;00m.[32mtanh[39;49;00m(x)$
        sinh(x) / cosh(x)$
    [34mend[39;49;00m$
[34mend[39;49;00m$
$
[37m# The support for Complex numbers is not built-in[39;49;00m$
y = [31mMath[39;49;00m.acos([34m3[39;49;00m.[34m7[39;49;00m)$
[37m#=> in `sqrt': square root for negative number (ArgumentError)[39;49;00m$
$
[37m# There is an implementation of Complex numbers in 'complex.rb' in current[39;49;00m$
[37m# Ruby distro, but it doesn't support atan2 with complex args, so it doesn't[39;49;00m$
[37m# solve this problem.[39;49;00m$
$
$
[37m# @@PLEAC@@_2.13[39;49;00m$
log_e = [31mMath[39;49;00m.log(val)$
log_10 = [31mMath[39;49;00m.log10(val)$
$
[34mdef[39;49;00m [32mlog_base[39;49;00m(base, val)$
    [31mMath[39;49;00m.log(val)/[31mMath[39;49;00m.log(base)$
[34mend[39;49;00m$
$
answer = log_base([34m10[39;49;00m, [34m10_000[39;49;00m)$
[36mputs[39;49;00m [33m"[39;49;00m[33mlog10(10,000) = [39;49;00m[33m#{[39;49;00manswer[33m}[39;49;00m[33m"[39;49;00m$
$
$
[37m# @@PLEAC@@_2.14[39;49;00m$
[36mrequire[39;49;00m [33m'[39;49;00m[33mmatrix.rb[39;49;00m[33m'[39;49;00m$
$
a = [31mMatrix[39;49;00m[[[34m3[39;49;00m, [34m2[39;49;00m, [34m3[39;49;00m], [[34m5[39;49;00m, [34m9[39;49;00m, [34m8[39;49;00m]]$
b = [31mMatrix[39;49;00m[[[34m4[39;49;00m, [34m7[39;49;00m], [[34m9[39;49;00m, [34m3[39;49;00m], [[34m8[39;49;00m, [34m1[39;49;00m]]$
c = a * b$
$
a.row_size$
a.column_size$
$
c.det$
a.transpose$
$
$
[37m# @@PLEAC@@_2.15[39;49;00m$
[36mrequire[39;49;00m [33m'[39;49;00m[33mcomplex.rb[39;49;00m[33m'[39;49;00m$
[36mrequire[39;49;00m [33m'[39;49;00m[33mrational.rb[39;49;00m[33m'[39;49;00m$
$
a = [31mComplex[39;49;00m([34m3[39;49;00m, [34m5[39;49;00m)              [37m# 3 + 5i[39;49;00m$
b = [31mComplex[39;49;00m([34m2[39;49;00m, -[34m2[39;49;00m)             [37m# 2 - 2i[39;49;00m$
[36mputs[39;49;00m [33m"[39;49;00m[33mc = [39;49;00m[33m#{[39;49;00ma*b[33m}[39;49;00m[33m"[39;49;00m$
$
c = a * b$
d = [34m3[39;49;00m + [34m4[39;49;00m*[31mComplex[39;49;00m::I$
$
[36mprintf[39;49;00m [33m"[39;49;00m[33msqrt([39;49;00m[33m#{[39;49;00md[33m}[39;49;00m[33m) = %s[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m, [31mMath[39;49;00m.sqrt(d)$
$
$
[37m# @@PLEAC@@_2.16[39;49;00m$
number = hexadecimal.hex$
number = octal.oct$
$
[36mprint[39;49;00m [33m"[39;49;00m[33mGimme a number in decimal, octal, or hex: [39;49;00m[33m"[39;49;00m$
num = [36mgets[39;49;00m.chomp$
[36mexit[39;49;00m [34munless[39;49;00m defined?(num)$
num = num.oct [34mif[39;49;00m num =~ [33m/[39;49;00m[33m^0[39;49;00m[33m/[39;49;00m  [37m# does both oct and hex  [39;49;00m$
[36mprintf[39;49;00m [33m"[39;49;00m[33m%d %x %o[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m, num, num, num$
$
[36mprint[39;49;00m [33m"[39;49;00m[33mEnter file permission in octal: [39;49;00m[33m"[39;49;00m$
permissions = [36mgets[39;49;00m.chomp$
[34mraise[39;49;00m [33m"[39;49;00m[33mExiting ...[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m [34munless[39;49;00m defined?(permissions)$
[36mputs[39;49;00m [33m"[39;49;00m[33mThe decimal value is [39;49;00m[33m#{[39;49;00mpermissions.oct[33m}[39;49;00m[33m"[39;49;00m$
$
$
[37m# @@PLEAC@@_2.17[39;49;00m$
[34mdef[39;49;00m [32mcommify[39;49;00m(n)$
    n.to_s =~ [33m/[39;49;00m[33m([^[39;49;00m[33m\[39;49;00m[33m.]*)([39;49;00m[33m\[39;49;00m[33m..*)?[39;49;00m[33m/[39;49;00m$
    int, dec = [31m$1[39;49;00m.reverse, [31m$2[39;49;00m ? [31m$2[39;49;00m : [33m"[39;49;00m[33m"[39;49;00m$
    [34mwhile[39;49;00m int.gsub!([33m/[39;49;00m[33m(,|[39;49;00m[33m\[39;49;00m[33m.|^)([39;49;00m[33m\[39;49;00m[33md{3})([39;49;00m[33m\[39;49;00m[33md)[39;49;00m[33m/[39;49;00m, [33m'[39;49;00m[33m\1[39;49;00m[33m\2[39;49;00m[33m,[39;49;00m[33m\3[39;49;00m[33m'[39;49;00m)$
    [34mend[39;49;00m$
    int.reverse + dec$
[34mend[39;49;00m$
$
$
[37m# @@PLEAC@@_2.18[39;49;00m$
[36mprintf[39;49;00m [33m"[39;49;00m[33mIt took %d hour%s[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m, time, time == [34m1[39;49;00m ? [33m"[39;49;00m[33m"[39;49;00m : [33m"[39;49;00m[33ms[39;49;00m[33m"[39;49;00m$
$
[37m# dunno if an equivalent to Lingua::EN::Inflect exists...[39;49;00m$
$
$
[37m# @@PLEAC@@_2.19[39;49;00m$
[37m#-----------------------------[39;49;00m$
[37m#!/usr/bin/ruby[39;49;00m$
[37m# bigfact - calculating prime factors[39;49;00m$
[34mdef[39;49;00m [32mfactorize[39;49;00m(orig)$
    factors = {}$
    factors.default = [34m0[39;49;00m     [37m# return 0 instead nil if key not found in hash[39;49;00m$
    n = orig$
    i = [34m2[39;49;00m$
    sqi = [34m4[39;49;00m                 [37m# square of i[39;49;00m$
    [34mwhile[39;49;00m sqi <= n [34mdo[39;49;00m$
        [34mwhile[39;49;00m n.modulo(i) == [34m0[39;49;00m [34mdo[39;49;00m$
            n /= i$
            factors[i] += [34m1[39;49;00m$
            [37m# puts "Found factor #{i}"[39;49;00m$
        [34mend[39;49;00m$
        [37m# we take advantage of the fact that (i +1)**2 = i**2 + 2*i +1[39;49;00m$
        sqi += [34m2[39;49;00m * i + [34m1[39;49;00m$
        i += [34m1[39;49;00m$
    [34mend[39;49;00m$
    $
    [34mif[39;49;00m (n != [34m1[39;49;00m) && (n != orig)$
        factors[n] += [34m1[39;49;00m$
    [34mend[39;49;00m$
    factors$
[34mend[39;49;00m$
$
[34mdef[39;49;00m [32mprintfactorhash[39;49;00m(orig, factorcount)$
    [36mprint[39;49;00m [36mformat[39;49;00m([33m"[39;49;00m[33m%-10d [39;49;00m[33m"[39;49;00m, orig)$
    [34mif[39;49;00m factorcount.length == [34m0[39;49;00m$
        [36mprint[39;49;00m [33m"[39;49;00m[33mPRIME[39;49;00m[33m"[39;49;00m$
    [34melse[39;49;00m$
        [37m# sorts after number, because the hash keys are numbers[39;49;00m$
        factorcount.sort.each { |factor,exponent|$
            [36mprint[39;49;00m factor$
            [34mif[39;49;00m exponent > [34m1[39;49;00m$
                [36mprint[39;49;00m [33m"[39;49;00m[33m**[39;49;00m[33m"[39;49;00m, exponent$
            [34mend[39;49;00m$
            [36mprint[39;49;00m [33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m$
        }$
    [34mend[39;49;00m$
    [36mputs[39;49;00m$
[34mend[39;49;00m$
$
[34mfor[39;49;00m arg [34min[39;49;00m [31mARGV[39;49;00m$
    n = arg.to_i$
    mfactors = factorize(n)$
    printfactorhash(n, mfactors)$
[34mend[39;49;00m$
[37m#-----------------------------[39;49;00m$
$
$
[37m# @@PLEAC@@_3.0[39;49;00m$
[36mputs[39;49;00m [31mTime[39;49;00m.now$
$
[36mprint[39;49;00m [33m"[39;49;00m[33mToday is day [39;49;00m[33m"[39;49;00m, [31mTime[39;49;00m.now.yday, [33m"[39;49;00m[33m of the current year.[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
[36mprint[39;49;00m [33m"[39;49;00m[33mToday is day [39;49;00m[33m"[39;49;00m, [31mTime[39;49;00m.now.day, [33m"[39;49;00m[33m of the current month.[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
$
$
[37m# @@PLEAC@@_3.1[39;49;00m$
day, month, year = [31mTime[39;49;00m.now.day, [31mTime[39;49;00m.now.month, [31mTime[39;49;00m.now.year$
[37m# or[39;49;00m$
day, month, year = [31mTime[39;49;00m.now.to_a[[34m3[39;49;00m..[34m5[39;49;00m]$
$
tl = [31mTime[39;49;00m.now.localtime$
[36mprintf[39;49;00m([33m"[39;49;00m[33mThe current date is %04d %02d %02d[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m, tl.year, tl.month, tl.day)$
$
[31mTime[39;49;00m.now.localtime.strftime([33m"[39;49;00m[33m%Y-%m-%d[39;49;00m[33m"[39;49;00m)$
$
$
[37m# @@PLEAC@@_3.2[39;49;00m$
[31mTime[39;49;00m.local(year, month, day, hour, minute, second).tv_sec$
[31mTime[39;49;00m.gm(year, month, day, hour, minute, second).tv_sec$
$
$
[37m# @@PLEAC@@_3.3[39;49;00m$
sec, min, hour, day, month, year, wday, yday, isdst, zone = [31mTime[39;49;00m.at(epoch_secs).to_a$
$
$
[37m# @@PLEAC@@_3.4[39;49;00m$
when_ = now + difference         [37m# now -> Time ; difference -> Numeric (delta in seconds)[39;49;00m$
then_ = now - difference$
$
$
[37m# @@PLEAC@@_3.5[39;49;00m$
bree = [34m361535725[39;49;00m$
nat  =  [34m96201950[39;49;00m$
$
difference = bree - nat$
[36mputs[39;49;00m [33m"[39;49;00m[33mThere were [39;49;00m[33m#{[39;49;00mdifference[33m}[39;49;00m[33m seconds between Nat and Bree[39;49;00m[33m"[39;49;00m$
$
seconds    =  difference % [34m60[39;49;00m$
difference = (difference - seconds) / [34m60[39;49;00m$
minutes    =  difference % [34m60[39;49;00m$
difference = (difference - minutes) / [34m60[39;49;00m$
hours      =  difference % [34m24[39;49;00m$
difference = (difference - hours)   / [34m24[39;49;00m$
days       =  difference % [34m7[39;49;00m$
weeks      = (difference - days)    /  [34m7[39;49;00m$
$
[36mputs[39;49;00m [33m"[39;49;00m[33m([39;49;00m[33m#{[39;49;00mweeks[33m}[39;49;00m[33m weeks, [39;49;00m[33m#{[39;49;00mdays[33m}[39;49;00m[33m days, [39;49;00m[33m#{[39;49;00mhours[33m}[39;49;00m[33m:[39;49;00m[33m#{[39;49;00mminutes[33m}[39;49;00m[33m:[39;49;00m[33m#{[39;49;00mseconds[33m}[39;49;00m[33m)[39;49;00m[33m"[39;49;00m$
$
$
[37m# @@PLEAC@@_3.6[39;49;00m$
monthday, weekday, yearday = date.mday, date.wday, date.yday$
$
[37m# AFAIK the week number is not just a division since week boundaries are on sundays[39;49;00m$
weeknum = d.strftime([33m"[39;49;00m[33m%U[39;49;00m[33m"[39;49;00m).to_i + [34m1[39;49;00m$
$
year  = [34m1981[39;49;00m$
month = [33m"[39;49;00m[33mjun[39;49;00m[33m"[39;49;00m                     [37m# or `6' if you want to emulate a broken language[39;49;00m$
day   = [34m16[39;49;00m$
t = [31mTime[39;49;00m.mktime(year, month, day)$
[36mprint[39;49;00m [33m"[39;49;00m[33m#{[39;49;00mmonth[33m}[39;49;00m[33m/[39;49;00m[33m#{[39;49;00mday[33m}[39;49;00m[33m/[39;49;00m[33m#{[39;49;00myear[33m}[39;49;00m[33m was a [39;49;00m[33m"[39;49;00m, t.strftime([33m"[39;49;00m[33m%A[39;49;00m[33m"[39;49;00m), [33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
$
$
[37m# @@PLEAC@@_3.7[39;49;00m$
yyyy, mm, dd = [31m$1[39;49;00m, [31m$2[39;49;00m, [31m$3[39;49;00m [34mif[39;49;00m [33m"[39;49;00m[33m1998-06-25[39;49;00m[33m"[39;49;00m =~ [33m/[39;49;00m[33m([39;49;00m[33m\[39;49;00m[33md+)-([39;49;00m[33m\[39;49;00m[33md+)-([39;49;00m[33m\[39;49;00m[33md+)[39;49;00m[33m/[39;49;00m$
$
epoch_seconds = [31mTime[39;49;00m.mktime(yyyy, mm, dd).tv_sec$
$
[37m# dunno an equivalent to Date::Manip#ParseDate[39;49;00m$
$
$
[37m# @@PLEAC@@_3.8[39;49;00m$
string = [31mTime[39;49;00m.at(epoch_secs)$
[31mTime[39;49;00m.at([34m1234567890[39;49;00m).gmtime        [37m# gives: Fri Feb 13 23:31:30 UTC 2009[39;49;00m$
$
time = [31mTime[39;49;00m.mktime([34m1973[39;49;00m, [33m"[39;49;00m[33mjan[39;49;00m[33m"[39;49;00m, [34m18[39;49;00m, [34m3[39;49;00m, [34m45[39;49;00m, [34m50[39;49;00m)$
[36mprint[39;49;00m [33m"[39;49;00m[33mIn localtime it gives: [39;49;00m[33m"[39;49;00m, time.localtime, [33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
$
$
[37m# @@PLEAC@@_3.9[39;49;00m$
[37m# Ruby provides micro-seconds in Time object[39;49;00m$
[31mTime[39;49;00m.now.usec$
$
[37m# Ruby gives the seconds in floating format when substracting two Time objects[39;49;00m$
before = [31mTime[39;49;00m.now$
line = [36mgets[39;49;00m$
elapsed = [31mTime[39;49;00m.now - before$
[36mputs[39;49;00m [33m"[39;49;00m[33mYou took [39;49;00m[33m#{[39;49;00melapsed[33m}[39;49;00m[33m seconds.[39;49;00m[33m"[39;49;00m$
$
[37m# On my Celeron-400 with Linux-2.2.19-14mdk, average for three execs are:[39;49;00m$
[37m#   This Ruby version:       average 0.00321 sec[39;49;00m$
[37m#   Cookbook's Perl version: average 0.00981 sec[39;49;00m$
size = [34m500[39;49;00m$
number_of_times = [34m100[39;49;00m$
total_time = [34m0[39;49;00m$
number_of_times.times {$
    [37m# populate array[39;49;00m$
    array = []$
    size.times { array << [36mrand[39;49;00m }$
    [37m# sort it[39;49;00m$
    begin_ = [31mTime[39;49;00m.now$
    array.sort!$
    time = [31mTime[39;49;00m.now - begin_$
    total_time += time$
}$
[36mprintf[39;49;00m [33m"[39;49;00m[33mOn average, sorting %d random numbers takes %.5f seconds[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m,$
    size, (total_time/[36mFloat[39;49;00m(number_of_times))$
$
$
[37m# @@PLEAC@@_3.10[39;49;00m$
[36msleep[39;49;00m([34m0[39;49;00m.[34m005[39;49;00m)                      [37m# Ruby is definitely not as broken as Perl :)[39;49;00m$
[37m# (may be interrupted by sending the process a SIGALRM)[39;49;00m$
$
$
[37m# @@PLEAC@@_3.11[39;49;00m$
[37m#!/usr/bin/ruby -w[39;49;00m$
[37m# hopdelta - feed mail header, produce lines[39;49;00m$
[37m#            showing delay at each hop.[39;49;00m$
[36mrequire[39;49;00m [33m'[39;49;00m[33mtime[39;49;00m[33m'[39;49;00m$
[34mclass[39;49;00m [04m[32mMailHopDelta[39;49;00m$
$
    [34mdef[39;49;00m [32minitialize[39;49;00m(mail)$
        [31m@head[39;49;00m = mail.gsub([33m/[39;49;00m[33m\[39;49;00m[33mn[39;49;00m[33m\[39;49;00m[33ms+[39;49;00m[33m/[39;49;00m,[33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m)$
        [31m@topline[39;49;00m = [33m%w-Sender Recipient Time Delta-[39;49;00m$
        [31m@start_from[39;49;00m = mail.match([33m/[39;49;00m[33m^From.*[39;49;00m[33m\[39;49;00m[33m@([^[39;49;00m[33m\[39;49;00m[33ms>]*)[39;49;00m[33m/[39;49;00m)[[34m1[39;49;00m]$
        [31m@date[39;49;00m = [31mTime[39;49;00m.parse(mail.match([33m/[39;49;00m[33m^Date:[39;49;00m[33m\[39;49;00m[33ms+(.*)[39;49;00m[33m/[39;49;00m)[[34m1[39;49;00m])$
    [34mend[39;49;00m$
$
    [34mdef[39;49;00m [32mout[39;49;00m(line)$
         [33m"[39;49;00m[33m%-20.20s %-20.20s %-20.20s  %s[39;49;00m[33m"[39;49;00m % line$
    [34mend[39;49;00m$
$
    [34mdef[39;49;00m [32mhop_date[39;49;00m(day)$
        day.strftime([33m"[39;49;00m[33m%I:%M:%S %Y/%m/%d[39;49;00m[33m"[39;49;00m)$
    [34mend[39;49;00m$
$
    [34mdef[39;49;00m [32mputs_hops[39;49;00m$
        [36mputs[39;49;00m out([31m@topline[39;49;00m) $
        [36mputs[39;49;00m out([[33m'[39;49;00m[33mStart[39;49;00m[33m'[39;49;00m, [31m@start_from[39;49;00m, hop_date([31m@date[39;49;00m),[33m'[39;49;00m[33m'[39;49;00m])$
        [31m@head[39;49;00m.split([33m/[39;49;00m[33m\[39;49;00m[33mn[39;49;00m[33m/[39;49;00m).reverse.grep([33m/[39;49;00m[33m^Received:[39;49;00m[33m/[39;49;00m).each [34mdo[39;49;00m |hop|$
            hop.gsub!([33m/[39;49;00m[33m\[39;49;00m[33mbon (.*?) (id.*)[39;49;00m[33m/[39;49;00m,[33m'[39;49;00m[33m; [39;49;00m[33m\1[39;49;00m[33m'[39;49;00m)$
            whence = hop.match([33m/[39;49;00m[33m;[39;49;00m[33m\[39;49;00m[33ms+(.*)$[39;49;00m[33m/[39;49;00m)[[34m1[39;49;00m]$
            [34munless[39;49;00m whence$
                [36mwarn[39;49;00m [33m"[39;49;00m[33mBad received line: [39;49;00m[33m#{[39;49;00mhop[33m}[39;49;00m[33m"[39;49;00m$
                [34mnext[39;49;00m$
            [34mend[39;49;00m$
            from = [31m$+[39;49;00m [34mif[39;49;00m hop =~ [33m/[39;49;00m[33mfrom[39;49;00m[33m\[39;49;00m[33ms+([39;49;00m[33m\[39;49;00m[33mS+)|[39;49;00m[33m\[39;49;00m[33m((.*?)[39;49;00m[33m\[39;49;00m[33m)[39;49;00m[33m/[39;49;00m$
            by   = [31m$1[39;49;00m [34mif[39;49;00m hop =~ [33m/[39;49;00m[33mby[39;49;00m[33m\[39;49;00m[33ms+([39;49;00m[33m\[39;49;00m[33mS+[39;49;00m[33m\[39;49;00m[33m.[39;49;00m[33m\[39;49;00m[33mS+)[39;49;00m[33m/[39;49;00m$
            [34mnext[39;49;00m [34munless[39;49;00m now = [31mTime[39;49;00m.parse(whence).localtime$
            delta = now - [31m@date[39;49;00m$
            [36mputs[39;49;00m out([from, by, hop_date(now), hop_time(delta)])$
            [31m@date[39;49;00m = now$
        [34mend[39;49;00m$
    [34mend[39;49;00m$
$
    [34mdef[39;49;00m [32mhop_time[39;49;00m(secs)$
        sign = secs < [34m0[39;49;00m ? -[34m1[39;49;00m : [34m1[39;49;00m$
        days, secs = secs.abs.divmod([34m60[39;49;00m * [34m60[39;49;00m * [34m24[39;49;00m)$
        hours,secs = secs.abs.divmod([34m60[39;49;00m * [34m60[39;49;00m)$
        mins, secs = secs.abs.divmod([34m60[39;49;00m)$
        rtn =  [33m"[39;49;00m[33m%3ds[39;49;00m[33m"[39;49;00m % [secs  * sign]$
        rtn << [33m"[39;49;00m[33m%3dm[39;49;00m[33m"[39;49;00m % [mins  * sign] [34mif[39;49;00m mins  != [34m0[39;49;00m$
        rtn << [33m"[39;49;00m[33m%3dh[39;49;00m[33m"[39;49;00m % [hours * sign] [34mif[39;49;00m hours != [34m0[39;49;00m$
        rtn << [33m"[39;49;00m[33m%3dd[39;49;00m[33m"[39;49;00m % [days  * sign] [34mif[39;49;00m days  != [34m0[39;49;00m $
        rtn$
    [34mend[39;49;00m$
[34mend[39;49;00m$
$
[31m$/[39;49;00m = [33m"[39;49;00m[33m"[39;49;00m$
mail = [31mMailHopDelta[39;49;00m.new([31mARGF[39;49;00m.gets).puts_hops$
$
$
[37m# @@PLEAC@@_4.0[39;49;00m$
single_level = [ [33m"[39;49;00m[33mthis[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mthat[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mthe[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mother[39;49;00m[33m"[39;49;00m ]$
$
[37m# Ruby directly supports nested arrays[39;49;00m$
double_level = [ [33m"[39;49;00m[33mthis[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mthat[39;49;00m[33m"[39;49;00m, [ [33m"[39;49;00m[33mthe[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mother[39;49;00m[33m"[39;49;00m ] ]$
still_single_level = [ [33m"[39;49;00m[33mthis[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mthat[39;49;00m[33m"[39;49;00m, [ [33m"[39;49;00m[33mthe[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mother[39;49;00m[33m"[39;49;00m ] ].flatten$
$
$
[37m# @@PLEAC@@_4.1[39;49;00m$
a = [ [33m"[39;49;00m[33mquick[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mbrown[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mfox[39;49;00m[33m"[39;49;00m ]$
a = [33m%w([39;49;00m[33mWhy are you teasing me?[39;49;00m[33m)[39;49;00m$
$
lines = <<[33m"[39;49;00m[33mEND_OF_HERE_DOC[39;49;00m[33m"[39;49;00m.gsub([33m/[39;49;00m[33m^[39;49;00m[33m\[39;49;00m[33ms*(.+)[39;49;00m[33m/[39;49;00m, [33m'[39;49;00m[33m\1[39;49;00m[33m'[39;49;00m)$
[33m    The boy stood on the burning deck,[39;49;00m$
[33m    It was as hot as glass.[39;49;00m$
[33mEND_OF_HERE_DOC[39;49;00m$
$
bigarray = [31mIO[39;49;00m.readlines([33m"[39;49;00m[33mmydatafile[39;49;00m[33m"[39;49;00m).collect { |l| l.chomp }$
$
[36mname[39;49;00m = [33m"[39;49;00m[33mGandalf[39;49;00m[33m"[39;49;00m$
banner = [33m%Q([39;49;00m[33mSpeak, [39;49;00m[33m#{[39;49;00m[36mname[39;49;00m[33m}[39;49;00m[33m, and welcome![39;49;00m[33m)[39;49;00m$
$
host_info  = [33m`[39;49;00m[33mhost [39;49;00m[33m#{[39;49;00mhis_host[33m}[39;49;00m[33m`[39;49;00m$
$
[33m%x([39;49;00m[33mps [39;49;00m[33m#{[39;49;00m[31m$$[39;49;00m[33m}[39;49;00m[33m)[39;49;00m$
$
banner = [33m'[39;49;00m[33mCosts only $4.95[39;49;00m[33m'[39;49;00m.split([33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m)$
$
rax = [33m%w! ( ) < > { } [ ] ![39;49;00m$
$
$
[37m# @@PLEAC@@_4.2[39;49;00m$
[34mdef[39;49;00m [32mcommify_series[39;49;00m(arr)$
    [34mreturn[39;49;00m [33m'[39;49;00m[33m'[39;49;00m [34mif[39;49;00m [35mnot[39;49;00m arr$
    [34mcase[39;49;00m arr.size$
        [34mwhen[39;49;00m [34m0[39;49;00m [34mthen[39;49;00m [33m'[39;49;00m[33m'[39;49;00m$
        [34mwhen[39;49;00m [34m1[39;49;00m [34mthen[39;49;00m arr[[34m0[39;49;00m]$
        [34mwhen[39;49;00m [34m2[39;49;00m [34mthen[39;49;00m arr.join([33m'[39;49;00m[33m and [39;49;00m[33m'[39;49;00m)$
        [34melse[39;49;00m arr[[34m0[39;49;00m..-[34m2[39;49;00m].join([33m'[39;49;00m[33m, [39;49;00m[33m'[39;49;00m) + [33m'[39;49;00m[33m, and [39;49;00m[33m'[39;49;00m + arr[-[34m1[39;49;00m]$
    [34mend[39;49;00m$
[34mend[39;49;00m$
$
array = [ [33m"[39;49;00m[33mred[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33myellow[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mgreen[39;49;00m[33m"[39;49;00m ]$
$
[36mprint[39;49;00m [33m"[39;49;00m[33mI have [39;49;00m[33m"[39;49;00m, array, [33m"[39;49;00m[33m marbles[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
[37m# -> I have redyellowgreen marbles[39;49;00m$
$
[37m# But unlike Perl:[39;49;00m$
[36mprint[39;49;00m [33m"[39;49;00m[33mI have [39;49;00m[33m#{[39;49;00marray[33m}[39;49;00m[33m marbles[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
[37m# -> I have redyellowgreen marbles[39;49;00m$
[37m# So, needs:[39;49;00m$
[36mprint[39;49;00m [33m"[39;49;00m[33mI have [39;49;00m[33m#{[39;49;00marray.join([33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m)[33m}[39;49;00m[33m marbles[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
[37m# -> I have red yellow green marbles[39;49;00m$
$
[37m#!/usr/bin/ruby[39;49;00m$
[37m# communify_series - show proper comma insertion in list output[39;49;00m$
$
[34mdef[39;49;00m [32mcommify_series[39;49;00m(arr)$
    [34mreturn[39;49;00m [33m'[39;49;00m[33m'[39;49;00m [34mif[39;49;00m [35mnot[39;49;00m arr$
    sepchar = arr.find { |[36mp[39;49;00m| [36mp[39;49;00m =~ [33m/[39;49;00m[33m,[39;49;00m[33m/[39;49;00m } ? [33m'[39;49;00m[33m; [39;49;00m[33m'[39;49;00m : [33m'[39;49;00m[33m, [39;49;00m[33m'[39;49;00m$
    [34mcase[39;49;00m arr.size$
        [34mwhen[39;49;00m [34m0[39;49;00m [34mthen[39;49;00m [33m'[39;49;00m[33m'[39;49;00m$
        [34mwhen[39;49;00m [34m1[39;49;00m [34mthen[39;49;00m arr[[34m0[39;49;00m]$
        [34mwhen[39;49;00m [34m2[39;49;00m [34mthen[39;49;00m arr.join([33m'[39;49;00m[33m and [39;49;00m[33m'[39;49;00m)$
        [34melse[39;49;00m arr[[34m0[39;49;00m..-[34m2[39;49;00m].join(sepchar) + sepchar + [33m'[39;49;00m[33mand [39;49;00m[33m'[39;49;00m + arr[-[34m1[39;49;00m]$
    [34mend[39;49;00m$
[34mend[39;49;00m$
$
lists = [$
    [ [33m'[39;49;00m[33mjust one thing[39;49;00m[33m'[39;49;00m ],$
    [33m%w([39;49;00m[33mMutt Jeff[39;49;00m[33m)[39;49;00m,$
    [33m%w([39;49;00m[33mPeter Paul Mary[39;49;00m[33m)[39;49;00m,$
    [ [33m'[39;49;00m[33mTo our parents[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mMother Theresa[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mGod[39;49;00m[33m'[39;49;00m ],$
    [ [33m'[39;49;00m[33mpastrami[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mham and cheese[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mpeanut butter and jelly[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mtuna[39;49;00m[33m'[39;49;00m ],$
    [ [33m'[39;49;00m[33mrecycle tired, old phrases[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mponder big, happy thoughts[39;49;00m[33m'[39;49;00m ],$
    [ [33m'[39;49;00m[33mrecycle tired, old phrases[39;49;00m[33m'[39;49;00m,$
      [33m'[39;49;00m[33mponder big, happy thoughts[39;49;00m[33m'[39;49;00m,$
      [33m'[39;49;00m[33msleep and dream peacefully[39;49;00m[33m'[39;49;00m ],$
]$
$
[34mfor[39;49;00m list [34min[39;49;00m lists [34mdo[39;49;00m$
    [36mputs[39;49;00m [33m"[39;49;00m[33mThe list is: [39;49;00m[33m#{[39;49;00mcommify_series(list)[33m}[39;49;00m[33m.[39;49;00m[33m"[39;49;00m$
[34mend[39;49;00m$
$
$
[37m# @@PLEAC@@_4.3[39;49;00m$
[37m#   (note: AFAIK Ruby doesn't allow gory change of Array length)[39;49;00m$
[37m# grow the array by assigning nil to past the end of array[39;49;00m$
ary[new_size-[34m1[39;49;00m] = [34mnil[39;49;00m$
[37m# shrink the array by slicing it down[39;49;00m$
ary.slice!(new_size..-[34m1[39;49;00m)$
[37m# init the array with given size[39;49;00m$
[36mArray[39;49;00m.new(number_of_elems)$
[37m# assign to an element past the original end enlarges the array[39;49;00m$
ary[index_new_last_elem] = value$
$
[34mdef[39;49;00m [32mwhat_about_that_array[39;49;00m(a)$
    [36mprint[39;49;00m [33m"[39;49;00m[33mThe array now has [39;49;00m[33m"[39;49;00m, a.size, [33m"[39;49;00m[33m elements.[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
    [37m# Index of last element is not really interesting in Ruby[39;49;00m$
    [36mprint[39;49;00m [33m"[39;49;00m[33mElement [39;49;00m[33m#[39;49;00m[33m3 is `[39;49;00m[33m#{[39;49;00ma[[34m3[39;49;00m][33m}[39;49;00m[33m'.[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
[34mend[39;49;00m$
people = [33m%w([39;49;00m[33mCrosby Stills Nash Young[39;49;00m[33m)[39;49;00m$
what_about_that_array(people)$
$
$
[37m# @@PLEAC@@_4.4[39;49;00m$
[37m# OO style[39;49;00m$
bad_users.each { |user|$
    complain(user)$
}$
[37m# or, functional style[39;49;00m$
[34mfor[39;49;00m user [34min[39;49;00m bad_users$
    complain(user)$
[34mend[39;49;00m$
$
[34mfor[39;49;00m var [34min[39;49;00m [31mENV[39;49;00m.keys.sort$
    [36mputs[39;49;00m [33m"[39;49;00m[33m#{[39;49;00mvar[33m}[39;49;00m[33m=[39;49;00m[33m#{[39;49;00m[31mENV[39;49;00m[var][33m}[39;49;00m[33m"[39;49;00m$
[34mend[39;49;00m$
$
[34mfor[39;49;00m user [34min[39;49;00m all_users$
    disk_space = get_usage(user)$
    [34mif[39;49;00m (disk_space > [31mMAX_QUOTA[39;49;00m)$
        complain(user)$
    [34mend[39;49;00m$
[34mend[39;49;00m$
$
[34mfor[39;49;00m l [34min[39;49;00m [31mIO[39;49;00m.popen([33m"[39;49;00m[33mwho[39;49;00m[33m"[39;49;00m).readlines$
    [36mprint[39;49;00m l [34mif[39;49;00m l =~ [33m/[39;49;00m[33m^gc[39;49;00m[33m/[39;49;00m $
[34mend[39;49;00m$
$
[37m# we can mimic the obfuscated Perl way[39;49;00m$
[34mwhile[39;49;00m fh.gets               [37m# $_ is set to the line just read[39;49;00m$
    [36mchomp[39;49;00m                   [37m# $_ has a trailing \n removed, if it had one[39;49;00m$
    [36msplit[39;49;00m.each { |w|        [37m# $_ is split on whitespace[39;49;00m$
                            [37m# but $_ is not set to each chunk as in Perl[39;49;00m$
        [36mprint[39;49;00m w.reverse$
    }$
[34mend[39;49;00m$
[37m# ...or use a cleaner way[39;49;00m$
[34mfor[39;49;00m l [34min[39;49;00m fh.readlines$
    l.chomp.split.each { |w| [36mprint[39;49;00m w.reverse }$
[34mend[39;49;00m$
$
[37m# same drawback as in problem 1.4, we can't mutate a Numeric...[39;49;00m$
array.collect! { |v| v - [34m1[39;49;00m }$
$
a = [ .[34m5[39;49;00m, [34m3[39;49;00m ]; b = [ [34m0[39;49;00m, [34m1[39;49;00m ]$
[34mfor[39;49;00m ary [34min[39;49;00m [ a, b ]$
    ary.collect! { |v| v * [34m7[39;49;00m }$
[34mend[39;49;00m$
[36mputs[39;49;00m [33m"[39;49;00m[33m#{[39;49;00ma.join([33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m)[33m}[39;49;00m[33m [39;49;00m[33m#{[39;49;00mb.join([33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m)[33m}[39;49;00m[33m"[39;49;00m$
$
[37m# we can mutate Strings, cool; we need a trick for the scalar[39;49;00m$
[34mfor[39;49;00m ary [34min[39;49;00m [ [ scalar ], array, [36mhash[39;49;00m.values ]$
    ary.each { |v| v.strip! }     [37m# String#strip rules :)[39;49;00m$
[34mend[39;49;00m$
$
$
[37m# @@PLEAC@@_4.5[39;49;00m$
[37m# not relevant in Ruby since we have always references[39;49;00m$
[34mfor[39;49;00m item [34min[39;49;00m array$
    [37m# do somethingh with item[39;49;00m$
[34mend[39;49;00m$
$
$
[37m# @@PLEAC@@_4.6[39;49;00m$
unique = list.uniq$
$
[37m# generate a list of users logged in, removing duplicates[39;49;00m$
users = [33m`[39;49;00m[33mwho[39;49;00m[33m`[39;49;00m.collect { |l| l =~ [33m/[39;49;00m[33m([39;49;00m[33m\[39;49;00m[33mw+)[39;49;00m[33m/[39;49;00m; [31m$1[39;49;00m }.sort.uniq$
[36mputs[39;49;00m([33m"[39;49;00m[33musers logged in: [39;49;00m[33m#{[39;49;00mcommify_series(users)[33m}[39;49;00m[33m"[39;49;00m)  [37m# see 4.2 for commify_series[39;49;00m$
$
$
[37m# @@PLEAC@@_4.7[39;49;00m$
a - b$
[37m# [ 1, 1, 2, 2, 3, 3, 3, 4, 5 ] - [ 1, 2, 4 ]  ->  [3, 5][39;49;00m$
$
$
[37m# @@PLEAC@@_4.8[39;49;00m$
union = a | b$
intersection = a & b$
difference = a - b$
$
$
[37m# @@PLEAC@@_4.9[39;49;00m$
array1.concat(array2)$
[37m# if you will assign to another object, better use:[39;49;00m$
new_ary = array1 + array2$
$
members = [ [33m"[39;49;00m[33mTime[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mFlies[39;49;00m[33m"[39;49;00m ]$
initiates =  [ [33m"[39;49;00m[33mAn[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mArrow[39;49;00m[33m"[39;49;00m ]$
members += initiates$
$
members = [ [33m"[39;49;00m[33mTime[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mFlies[39;49;00m[33m"[39;49;00m ]$
initiates = [ [33m"[39;49;00m[33mAn[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mArrow[39;49;00m[33m"[39;49;00m ]$
members[[34m2[39;49;00m,[34m0[39;49;00m] = [ [33m"[39;49;00m[33mLike[39;49;00m[33m"[39;49;00m, initiates ].flatten$
$
members[[34m0[39;49;00m] = [33m"[39;49;00m[33mFruit[39;49;00m[33m"[39;49;00m$
members[[34m3[39;49;00m,[34m2[39;49;00m] = [33m"[39;49;00m[33mA[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mBanana[39;49;00m[33m"[39;49;00m$
$
$
[37m# @@PLEAC@@_4.10[39;49;00m$
reversed = ary.reverse$
$
ary.reverse_each { |e|$
    [37m# do something with e[39;49;00m$
}$
$
descending = ary.sort.reverse$
descending = ary.sort { |a,b| b <=> a }$
$
$
[37m# @@PLEAC@@_4.11[39;49;00m$
[37m# remove n elements from front of ary (shift n)[39;49;00m$
front = ary.slice!([34m0[39;49;00m, n)$
$
[37m# remove n elements from the end of ary (pop n)[39;49;00m$
end_ = ary.slice!(-n .. -[34m1[39;49;00m)$
$
[37m# let's extend the Array class, to make that useful[39;49;00m$
[34mclass[39;49;00m [04m[32mArray[39;49;00m$
    [34mdef[39;49;00m [32mshift2[39;49;00m()$
        slice!([34m0[39;49;00m .. [34m1[39;49;00m)     [37m# more symetric with pop2...[39;49;00m$
    [34mend[39;49;00m$
    [34mdef[39;49;00m [32mpop2[39;49;00m()$
        slice!(-[34m2[39;49;00m .. -[34m1[39;49;00m)$
    [34mend[39;49;00m$
[34mend[39;49;00m$
$
friends = [33m%w([39;49;00m[33mPeter Paul Mary Jim Tim[39;49;00m[33m)[39;49;00m$
this, that = friends.shift2$
$
beverages = [33m%w([39;49;00m[33mDew Jolt Cola Sprite Fresca[39;49;00m[33m)[39;49;00m$
pair = beverages.pop2$
$
$
[37m# @@PLEAC@@_4.12[39;49;00m$
[37m# use Enumerable#detect (or the synonym Enumerable#find)[39;49;00m$
highest_eng = employees.detect { |emp| emp.category == [33m'[39;49;00m[33mengineer[39;49;00m[33m'[39;49;00m }$
$
$
[37m# @@PLEAC@@_4.13[39;49;00m$
[37m# use Enumerable#select (or the synonym Enumerable#find_all)[39;49;00m$
bigs = nums.select { |i| i > [34m1_000_000[39;49;00m }$
pigs = users.keys.select { |k| users[k] > [34m1[39;49;00me7 }$
$
matching = [33m`[39;49;00m[33mwho[39;49;00m[33m`[39;49;00m.select { |u| u =~ [33m/[39;49;00m[33m^gnat [39;49;00m[33m/[39;49;00m }$
$
engineers = employees.select { |e| e.position == [33m'[39;49;00m[33mEngineer[39;49;00m[33m'[39;49;00m }$
$
secondary_assistance = applicants.select { |a|$
    a.income >= [34m26_000[39;49;00m && a.income < [34m30_000[39;49;00m$
}$
$
$
[37m# @@PLEAC@@_4.14[39;49;00m$
[37m# normally you would have an array of Numeric (Float or[39;49;00m$
[37m# Fixnum or Bignum), so you would use:[39;49;00m$
sorted = unsorted.sort$
[37m# if you have strings representing Integers or Floats[39;49;00m$
[37m# you may specify another sort method:[39;49;00m$
sorted = unsorted.sort { |a,b| a.to_f <=> b.to_f }$
$
[37m# let's use the list of my own PID's[39;49;00m$
[33m`[39;49;00m[33mps ux[39;49;00m[33m`[39;49;00m.split([33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m)[[34m1[39;49;00m..-[34m1[39;49;00m].$
    [36mselect[39;49;00m { |i| i =~ [33m/[39;49;00m[33m^[39;49;00m[33m#{[39;49;00m[31mENV[39;49;00m[[33m'[39;49;00m[33mUSER[39;49;00m[33m'[39;49;00m][33m}[39;49;00m[33m/[39;49;00m }.$
    collect { |i| i.split[[34m1[39;49;00m] }.$
    sort { |a,b| a.to_i <=> b.to_i }.each { |i| [36mputs[39;49;00m i }$
[36mputs[39;49;00m [33m"[39;49;00m[33mSelect a process ID to kill:[39;49;00m[33m"[39;49;00m$
pid = [36mgets[39;49;00m.chomp$
[34mraise[39;49;00m [33m"[39;49;00m[33mExiting ... [39;49;00m[33m\n[39;49;00m[33m"[39;49;00m [34munless[39;49;00m pid && pid =~ [33m/[39;49;00m[33m^[39;49;00m[33m\[39;49;00m[33md+$[39;49;00m[33m/[39;49;00m$
[31mProcess[39;49;00m.kill([33m'[39;49;00m[33mTERM[39;49;00m[33m'[39;49;00m, pid.to_i)$
[36msleep[39;49;00m [34m2[39;49;00m$
[31mProcess[39;49;00m.kill([33m'[39;49;00m[33mKILL[39;49;00m[33m'[39;49;00m, pid.to_i)$
$
descending = unsorted.sort { |a,b| b.to_f <=> a.to_f }$
$
$
[37m# @@PLEAC@@_4.15[39;49;00m$
ordered = unordered.sort { |a,b| compare(a,b) }$
$
precomputed = unordered.collect { |e| [compute, e] }$
ordered_precomputed = precomputed.sort { |a,b| a[[34m0[39;49;00m] <=> b[[34m0[39;49;00m] }$
ordered = ordered_precomputed.collect { |e| e[[34m1[39;49;00m] }$
$
ordered = unordered.collect { |e| [compute, e] }.$
    sort { |a,b| a[[34m0[39;49;00m] <=> b[[34m0[39;49;00m] }.$
    collect { |e| e[[34m1[39;49;00m] }$
$
[34mfor[39;49;00m employee [34min[39;49;00m employees.sort { |a,b| a.name <=> b.name }$
    [36mprint[39;49;00m employee.name, [33m"[39;49;00m[33m earns [39;49;00m[33m\[39;49;00m[33m$ [39;49;00m[33m"[39;49;00m, employee.salary, [33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
[34mend[39;49;00m$
$
[37m# Beware! `0' is true in Ruby.[39;49;00m$
[37m# For chaining comparisons, you may use Numeric#nonzero?, which[39;49;00m$
[37m# returns num if num is not zero, nil otherwise[39;49;00m$
sorted = employees.sort { |a,b| (a.name <=> b.name).nonzero? || b.age <=> a.age }$
$
users = []$
[37m# getpwent is not wrapped in Ruby... let's fallback[39;49;00m$
[31mIO[39;49;00m.readlines([33m'[39;49;00m[33m/etc/passwd[39;49;00m[33m'[39;49;00m).each { |u| users << u.split([33m'[39;49;00m[33m:[39;49;00m[33m'[39;49;00m) }$
users.sort! { |a,b| a[[34m0[39;49;00m] <=> b[[34m0[39;49;00m] }$
[34mfor[39;49;00m user [34min[39;49;00m users$
    [36mputs[39;49;00m user[[34m0[39;49;00m]$
[34mend[39;49;00m$
$
sorted = names.sort { |a,b| a[[34m1[39;49;00m, [34m1[39;49;00m] <=> b[[34m1[39;49;00m, [34m1[39;49;00m] }$
sorted = strings.sort { |a,b| a.length <=> b.length }$
$
[37m# let's show only the compact version[39;49;00m$
ordered = strings.collect { |e| [e.length, e] }.$
    sort { |a,b| a[[34m0[39;49;00m] <=> b[[34m0[39;49;00m] }.$
    collect { |e| e[[34m1[39;49;00m] }$
$
ordered = strings.collect { |e| [[33m/[39;49;00m[33m\[39;49;00m[33md+[39;49;00m[33m/[39;49;00m.match(e)[[34m0[39;49;00m].to_i, e] }.$
    sort { |a,b| a[[34m0[39;49;00m] <=> b[[34m0[39;49;00m] }.$
    collect { |e| e[[34m1[39;49;00m] }$
$
[36mprint[39;49;00m [33m`[39;49;00m[33mcat /etc/passwd[39;49;00m[33m`[39;49;00m.collect { |e| [e, e.split([33m'[39;49;00m[33m:[39;49;00m[33m'[39;49;00m).indexes([34m3[39;49;00m,[34m2[39;49;00m,[34m0[39;49;00m)].flatten }.$
    sort { |a,b| (a[[34m1[39;49;00m] <=> b[[34m1[39;49;00m]).nonzero? || (a[[34m2[39;49;00m] <=> b[[34m2[39;49;00m]).nonzero? || a[[34m3[39;49;00m] <=> b[[34m3[39;49;00m] }.$
    collect { |e| e[[34m0[39;49;00m] }$
$
$
[37m# @@PLEAC@@_4.16[39;49;00m$
circular.unshift(circular.pop)        [37m# the last shall be first[39;49;00m$
circular.push(circular.shift)         [37m# and vice versa[39;49;00m$
$
[34mdef[39;49;00m [32mgrab_and_rotate[39;49;00m(l)$
    l.push(ret = l.shift)$
    ret$
[34mend[39;49;00m$
$
processes = [[34m1[39;49;00m, [34m2[39;49;00m, [34m3[39;49;00m, [34m4[39;49;00m, [34m5[39;49;00m]$
[34mwhile[39;49;00m ([34m1[39;49;00m)$
    process = grab_and_rotate(processes)$
    [36mputs[39;49;00m [33m"[39;49;00m[33mHandling process [39;49;00m[33m#{[39;49;00mprocess[33m}[39;49;00m[33m"[39;49;00m$
    [36msleep[39;49;00m [34m1[39;49;00m$
[34mend[39;49;00m$
$
$
[37m# @@PLEAC@@_4.17[39;49;00m$
[34mdef[39;49;00m [32mfisher_yates_shuffle[39;49;00m(a)$
    (a.size-[34m1[39;49;00m).downto([34m1[39;49;00m) { |i|$
        j = [36mrand[39;49;00m(i+[34m1[39;49;00m)$
        a[i], a[j] = a[j], a[i] [34mif[39;49;00m i != j$
    }$
[34mend[39;49;00m$
$
[34mdef[39;49;00m [32mnaive_shuffle[39;49;00m(a)$
    [34mfor[39;49;00m i [34min[39;49;00m [34m0[39;49;00m...a.size$
        j = [36mrand[39;49;00m(a.size)$
        a[i], a[j] = a[j], a[i]$
    [34mend[39;49;00m$
[34mend[39;49;00m$

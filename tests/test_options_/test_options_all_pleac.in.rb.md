     1^I[37m# -*- ruby -*-[39;49;00m$
     2^I$
     3^I[37m# Local variables:[39;49;00m$
     4^I[37m#  indent-tabs-mode: nil[39;49;00m$
     5^I[37m#  ruby-indent-level: 4[39;49;00m$
     6^I[37m# End:[39;49;00m$
     7^I$
     8^I[37m# @@PLEAC@@_NAME[39;49;00m$
     9^I[37m# @@SKIP@@ Ruby[39;49;00m$
    10^I$
    11^I[37m# @@PLEAC@@_WEB[39;49;00m$
    12^I[37m# @@SKIP@@ http://www.ruby-lang.org[39;49;00m$
    13^I$
    14^I$
    15^I[37m# @@PLEAC@@_1.0[39;49;00m$
    16^Istring = [33m'[39;49;00m[33m\n[39;49;00m[33m'[39;49;00m                     [37m# two characters, \ and an n[39;49;00m$
    17^Istring = [33m'[39;49;00m[33mJon [39;49;00m[33m\'[39;49;00m[33mMaddog[39;49;00m[33m\'[39;49;00m[33m Orwant[39;49;00m[33m'[39;49;00m  [37m# literal single quotes[39;49;00m$
    18^I$
    19^Istring = [33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m                     [37m# a "newline" character[39;49;00m$
    20^Istring = [33m"[39;49;00m[33mJon [39;49;00m[33m\"[39;49;00m[33mMaddog[39;49;00m[33m\"[39;49;00m[33m Orwant[39;49;00m[33m"[39;49;00m  [37m# literal double quotes[39;49;00m$
    21^I$
    22^Istring = [33m%q/Jon 'Maddog' Orwant/[39;49;00m  [37m# literal single quotes[39;49;00m$
    23^I$
    24^Istring = [33m%q[[39;49;00m[33mJon 'Maddog' Orwant[39;49;00m[33m][39;49;00m  [37m# literal single quotes[39;49;00m$
    25^Istring = [33m%q{[39;49;00m[33mJon 'Maddog' Orwant[39;49;00m[33m}[39;49;00m  [37m# literal single quotes[39;49;00m$
    26^Istring = [33m%q([39;49;00m[33mJon 'Maddog' Orwant[39;49;00m[33m)[39;49;00m  [37m# literal single quotes[39;49;00m$
    27^Istring = [33m%q<[39;49;00m[33mJon 'Maddog' Orwant[39;49;00m[33m>[39;49;00m  [37m# literal single quotes[39;49;00m$
    28^I$
    29^Ia = <<[33m"[39;49;00m[33mEOF[39;49;00m[33m"[39;49;00m$
    30^I[33mThis is a multiline here document[39;49;00m$
    31^I[33mterminated by EOF on a line by itself[39;49;00m$
    32^I[33mEOF[39;49;00m$
    33^I$
    34^I$
    35^I[37m# @@PLEAC@@_1.1[39;49;00m$
    36^Ivalue = string[offset,count]$
    37^Ivalue = string[offset..-[34m1[39;49;00m]$
    38^I$
    39^Istring[offset,count] = newstring$
    40^Istring[offset..-[34m1[39;49;00m]   = newtail$
    41^I$
    42^I[37m# in Ruby we can also specify intervals by their two offsets[39;49;00m$
    43^Ivalue = string[offset..offs2]$
    44^Istring[offset..offs2] = newstring$
    45^I$
    46^Ileading, s1, s2, trailing = data.unpack([33m"[39;49;00m[33mA5 x3 A8 A8 A*[39;49;00m[33m"[39;49;00m)$
    47^I$
    48^Ifivers = string.unpack([33m"[39;49;00m[33mA5[39;49;00m[33m"[39;49;00m * (string.length/[34m5[39;49;00m))$
    49^I$
    50^Ichars = string.unpack([33m"[39;49;00m[33mA1[39;49;00m[33m"[39;49;00m * string.length)$
    51^I$
    52^Istring = [33m"[39;49;00m[33mThis is what you have[39;49;00m[33m"[39;49;00m$
    53^I[37m#        +012345678901234567890  Indexing forwards  (left to right)[39;49;00m$
    54^I[37m#         109876543210987654321- Indexing backwards (right to left)[39;49;00m$
    55^I[37m#          note that 0 means 10 or 20, etc. above[39;49;00m$
    56^I$
    57^Ifirst  = string[[34m0[39;49;00m, [34m1[39;49;00m]       [37m# "T"[39;49;00m$
    58^Istart  = string[[34m5[39;49;00m, [34m2[39;49;00m]       [37m# "is"[39;49;00m$
    59^Irest   = string[[34m13[39;49;00m..-[34m1[39;49;00m]     [37m# "you have"[39;49;00m$
    60^Ilast   = string[-[34m1[39;49;00m, [34m1[39;49;00m]      [37m# "e"[39;49;00m$
    61^Iend_   = string[-[34m4[39;49;00m..-[34m1[39;49;00m]     [37m# "have"[39;49;00m$
    62^Ipiece  = string[-[34m8[39;49;00m, [34m3[39;49;00m]      [37m# "you"[39;49;00m$
    63^I$
    64^Istring[[34m5[39;49;00m, [34m2[39;49;00m] = [33m"[39;49;00m[33mwasn't[39;49;00m[33m"[39;49;00m     [37m# change "is" to "wasn't"[39;49;00m$
    65^Istring[-[34m12[39;49;00m..-[34m1[39;49;00m] = [33m"[39;49;00m[33mondrous[39;49;00m[33m"[39;49;00m [37m# "This wasn't wondrous"[39;49;00m$
    66^Istring[[34m0[39;49;00m, [34m1[39;49;00m] = [33m"[39;49;00m[33m"[39;49;00m           [37m# delete first character[39;49;00m$
    67^Istring[-[34m10[39;49;00m..-[34m1[39;49;00m]  = [33m"[39;49;00m[33m"[39;49;00m       [37m# delete last 10 characters[39;49;00m$
    68^I$
    69^I[34mif[39;49;00m string[-[34m10[39;49;00m..-[34m1[39;49;00m] =~ [33m/[39;49;00m[33mpattern[39;49;00m[33m/[39;49;00m$
    70^I    [36mputs[39;49;00m [33m"[39;49;00m[33mPattern matches in last 10 characters[39;49;00m[33m"[39;49;00m$
    71^I[34mend[39;49;00m$
    72^I$
    73^Istring[[34m0[39;49;00m, [34m5[39;49;00m].gsub!([33m/[39;49;00m[33mis[39;49;00m[33m/[39;49;00m, [33m'[39;49;00m[33mat[39;49;00m[33m'[39;49;00m)$
    74^I$
    75^Ia = [33m"[39;49;00m[33mmake a hat[39;49;00m[33m"[39;49;00m$
    76^Ia[[34m0[39;49;00m, [34m1[39;49;00m], a[-[34m1[39;49;00m, [34m1[39;49;00m] = a[-[34m1[39;49;00m, [34m1[39;49;00m], a[[34m0[39;49;00m, [34m1[39;49;00m]$
    77^I$
    78^Ia = [33m"[39;49;00m[33mTo be or not to be[39;49;00m[33m"[39;49;00m$
    79^Ib = a.unpack([33m"[39;49;00m[33mx6 A6[39;49;00m[33m"[39;49;00m)$
    80^I$
    81^Ib, c = a.unpack([33m"[39;49;00m[33mx6 A2 X5 A2[39;49;00m[33m"[39;49;00m)$
    82^I[36mputs[39;49;00m [33m"[39;49;00m[33m#{[39;49;00mb[33m}[39;49;00m[33m\n[39;49;00m[33m#{[39;49;00mc[33m}[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
    83^I$
    84^I[34mdef[39;49;00m [32mcut2fmt[39;49;00m(*args)$
    85^I    template = [33m'[39;49;00m[33m'[39;49;00m$
    86^I    lastpos  = [34m1[39;49;00m$
    87^I    [34mfor[39;49;00m place [34min[39;49;00m args$
    88^I        template += [33m"[39;49;00m[33mA[39;49;00m[33m"[39;49;00m + (place - lastpos).to_s + [33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m$
    89^I        lastpos   = place$
    90^I    [34mend[39;49;00m$
    91^I    template += [33m"[39;49;00m[33mA*[39;49;00m[33m"[39;49;00m$
    92^I    [34mreturn[39;49;00m template$
    93^I[34mend[39;49;00m$
    94^I$
    95^Ifmt = cut2fmt([34m8[39;49;00m, [34m14[39;49;00m, [34m20[39;49;00m, [34m26[39;49;00m, [34m30[39;49;00m)$
    96^I$
    97^I$
    98^I[37m# @@PLEAC@@_1.2[39;49;00m$
    99^I[37m# careful! "b is true" doesn't mean "b != 0" (0 is true in Ruby)[39;49;00m$
   100^I[37m# thus no problem of "defined" later since only nil is false[39;49;00m$
   101^I[37m# the following sets to `c' if `b' is nil or false[39;49;00m$
   102^Ia = b || c$
   103^I$
   104^I[37m# if you need Perl's behaviour (setting to `c' if `b' is 0) the most[39;49;00m$
   105^I[37m# effective way is to use Numeric#nonzero? (thanks to Dave Thomas!)[39;49;00m$
   106^Ia = b.nonzero? || c$
   107^I$
   108^I[37m# you will still want to use defined? in order to test[39;49;00m$
   109^I[37m# for scope existence of a given object[39;49;00m$
   110^Ia = defined?(b) ? b : c$
   111^I$
   112^Idir = [31mARGV[39;49;00m.shift || [33m"[39;49;00m[33m/tmp[39;49;00m[33m"[39;49;00m$
   113^I$
   114^I$
   115^I[37m# @@PLEAC@@_1.3[39;49;00m$
   116^Iv1, v2 = v2, v1$
   117^I$
   118^Ialpha, beta, production = [33m%w([39;49;00m[33mJanuary March August[39;49;00m[33m)[39;49;00m$
   119^Ialpha, beta, production = beta, production, alpha$
   120^I$
   121^I$
   122^I[37m# @@PLEAC@@_1.4[39;49;00m$
   123^Inum = char[[34m0[39;49;00m]$
   124^Ichar = num.chr$
   125^I$
   126^I[37m# Ruby also supports having a char from character constant[39;49;00m$
   127^Inum = [33m?r[39;49;00m$
   128^I$
   129^Ichar = [36msprintf[39;49;00m([33m"[39;49;00m[33m%c[39;49;00m[33m"[39;49;00m, num)$
   130^I[36mprintf[39;49;00m([33m"[39;49;00m[33mNumber %d is character %c[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m, num, num)$
   131^I$
   132^Iascii = string.unpack([33m"[39;49;00m[33mC*[39;49;00m[33m"[39;49;00m)$
   133^Istring = ascii.pack([33m"[39;49;00m[33mC*[39;49;00m[33m"[39;49;00m)$
   134^I$
   135^Ihal = [33m"[39;49;00m[33mHAL[39;49;00m[33m"[39;49;00m$
   136^Iascii = hal.unpack([33m"[39;49;00m[33mC*[39;49;00m[33m"[39;49;00m)$
   137^I[37m# We can't use Array#each since we can't mutate a Fixnum[39;49;00m$
   138^Iascii.collect! { |i|$
   139^I    i + [34m1[39;49;00m                         [37m# add one to each ASCII value[39;49;00m$
   140^I}                $
   141^Iibm = ascii.pack([33m"[39;49;00m[33mC*[39;49;00m[33m"[39;49;00m)$
   142^I[36mputs[39;49;00m ibm$
   143^I$
   144^I$
   145^I[37m# @@PLEAC@@_1.5[39;49;00m$
   146^Iarray = string.split([33m'[39;49;00m[33m'[39;49;00m)$
   147^I$
   148^Iarray = string.unpack([33m"[39;49;00m[33mC*[39;49;00m[33m"[39;49;00m)$
   149^I$
   150^Istring.scan([33m/[39;49;00m[33m.[39;49;00m[33m/[39;49;00m) { |b|$
   151^I    [37m# do something with b[39;49;00m$
   152^I}$
   153^I$
   154^Istring = [33m"[39;49;00m[33man apple a day[39;49;00m[33m"[39;49;00m$
   155^I[36mprint[39;49;00m [33m"[39;49;00m[33munique chars are: [39;49;00m[33m"[39;49;00m, string.split([33m'[39;49;00m[33m'[39;49;00m).uniq.sort, [33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
   156^I$
   157^Isum = [34m0[39;49;00m$
   158^I[34mfor[39;49;00m ascval [34min[39;49;00m string.unpack([33m"[39;49;00m[33mC*[39;49;00m[33m"[39;49;00m) [37m# or use Array#each for a pure OO style :)[39;49;00m$
   159^I    sum += ascval$
   160^I[34mend[39;49;00m$
   161^I[36mputs[39;49;00m [33m"[39;49;00m[33msum is [39;49;00m[33m#{[39;49;00msum & [34m0xffffffff[39;49;00m[33m}[39;49;00m[33m"[39;49;00m [37m# since Ruby will go Bignum if necessary[39;49;00m$
   162^I$
   163^I[37m# @@INCLUDE@@ include/ruby/slowcat.rb[39;49;00m$
   164^I$
   165^I$
   166^I[37m# @@PLEAC@@_1.6[39;49;00m$
   167^Irevbytes = string.reverse$
   168^I$
   169^Irevwords = string.split([33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m).reverse.join([33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m)$
   170^I$
   171^Irevwords = string.split([33m/[39;49;00m[33m([39;49;00m[33m\[39;49;00m[33ms+)[39;49;00m[33m/[39;49;00m).reverse.join$
   172^I$
   173^I[37m# using the fact that IO is Enumerable, you can directly "select" it[39;49;00m$
   174^Ilong_palindromes = [31mFile[39;49;00m.open([33m"[39;49;00m[33m/usr/share/dict/words[39;49;00m[33m"[39;49;00m).$
   175^I    [36mselect[39;49;00m { |w| w.chomp!; w.reverse == w && w.length > [34m5[39;49;00m }$
   176^I$
   177^I$
   178^I[37m# @@PLEAC@@_1.7[39;49;00m$
   179^I[34mwhile[39;49;00m string.sub!([33m"[39;49;00m[33m\t[39;49;00m[33m+[39;49;00m[33m"[39;49;00m) { [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m * ([31m$&[39;49;00m.length * [34m8[39;49;00m - [31m$`[39;49;00m.length % [34m8[39;49;00m) }$
   180^I[34mend[39;49;00m$
   181^I$
   182^I$
   183^I[37m# @@PLEAC@@_1.8[39;49;00m$
   184^I[33m'[39;49;00m[33mYou owe [39;49;00m[33m#{[39;49;00mdebt[33m}[39;49;00m[33m to me[39;49;00m[33m'[39;49;00m.gsub([33m/[39;49;00m[33m\[39;49;00m[33m#{[39;49;00m(\w+)[33m}[39;49;00m[33m/[39;49;00m) { [36meval[39;49;00m([31m$1[39;49;00m) }$
   185^I$
   186^Irows, cols = [34m24[39;49;00m, [34m80[39;49;00m$
   187^Itext = [33m%q([39;49;00m[33mI am [39;49;00m[33m#[39;49;00m[33m{rows} high and [39;49;00m[33m#[39;49;00m[33m{cols} long[39;49;00m[33m)[39;49;00m$
   188^Itext.gsub!([33m/[39;49;00m[33m\[39;49;00m[33m#{[39;49;00m(\w+)[33m}[39;49;00m[33m/[39;49;00m) { [36meval[39;49;00m([33m"[39;49;00m[33m#{[39;49;00m[31m$1[39;49;00m[33m}[39;49;00m[33m"[39;49;00m) }$
   189^I[36mputs[39;49;00m text$
   190^I$
   191^I[33m'[39;49;00m[33mI am 17 years old[39;49;00m[33m'[39;49;00m.gsub([33m/[39;49;00m[33m\[39;49;00m[33md+[39;49;00m[33m/[39;49;00m) { [34m2[39;49;00m * [31m$&[39;49;00m.to_i }$
   192^I$
   193^I$
   194^I[37m# @@PLEAC@@_1.9[39;49;00m$
   195^Ie = [33m"[39;49;00m[33mbo peep[39;49;00m[33m"[39;49;00m.upcase$
   196^Ie.downcase!$
   197^Ie.capitalize!$
   198^I$
   199^I[33m"[39;49;00m[33mthIS is a loNG liNE[39;49;00m[33m"[39;49;00m.gsub!([33m/[39;49;00m[33m\[39;49;00m[33mw+[39;49;00m[33m/[39;49;00m) { [31m$&[39;49;00m.capitalize }$
   200^I$
   201^I$
   202^I[37m# @@PLEAC@@_1.10[39;49;00m$
   203^I[33m"[39;49;00m[33mI have [39;49;00m[33m#{[39;49;00mn+[34m1[39;49;00m[33m}[39;49;00m[33m guanacos.[39;49;00m[33m"[39;49;00m$
   204^I[36mprint[39;49;00m [33m"[39;49;00m[33mI have [39;49;00m[33m"[39;49;00m, n+[34m1[39;49;00m, [33m"[39;49;00m[33m guanacos.[39;49;00m[33m"[39;49;00m$
   205^I$
   206^I$
   207^I[37m# @@PLEAC@@_1.11[39;49;00m$
   208^Ivar = <<[33m'[39;49;00m[33mEOF[39;49;00m[33m'[39;49;00m.gsub([33m/[39;49;00m[33m^[39;49;00m[33m\[39;49;00m[33ms+[39;49;00m[33m/[39;49;00m, [33m'[39;49;00m[33m'[39;49;00m)$
   209^I[33m    your text[39;49;00m$
   210^I[33m    goes here[39;49;00m$
   211^I[33mEOF[39;49;00m$
   212^I$
   213^I$
   214^I[37m# @@PLEAC@@_1.12[39;49;00m$
   215^Istring = [33m"[39;49;00m[33mFolding and splicing is the work of an editor,[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m+$
   216^I    [33m"[39;49;00m[33mnot a mere collection of silicon[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m+ $
   217^I    [33m"[39;49;00m[33mand[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m+$
   218^I    [33m"[39;49;00m[33mmobile electrons![39;49;00m[33m"[39;49;00m$
   219^I$
   220^I[34mdef[39;49;00m [32mwrap[39;49;00m(str, max_size)$
   221^I    all = []$
   222^I    line = [33m'[39;49;00m[33m'[39;49;00m$
   223^I    [34mfor[39;49;00m l [34min[39;49;00m str.split$
   224^I        [34mif[39;49;00m (line+l).length >= max_size$
   225^I            all.push(line)$
   226^I            line = [33m'[39;49;00m[33m'[39;49;00m$
   227^I        [34mend[39;49;00m$
   228^I        line += line == [33m'[39;49;00m[33m'[39;49;00m ? l : [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m + l$
   229^I    [34mend[39;49;00m$
   230^I    all.push(line).join([33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m)$
   231^I[34mend[39;49;00m$
   232^I$
   233^I[36mprint[39;49;00m wrap(string, [34m20[39;49;00m)$
   234^I[37m#=> Folding and [39;49;00m$
   235^I[37m#=> splicing is the [39;49;00m$
   236^I[37m#=> work of an editor, [39;49;00m$
   237^I[37m#=> not a mere [39;49;00m$
   238^I[37m#=> collection of [39;49;00m$
   239^I[37m#=> silicon and mobile [39;49;00m$
   240^I[37m#=> electrons![39;49;00m$
   241^I$
   242^I$
   243^I[37m# @@PLEAC@@_1.13[39;49;00m$
   244^Istring = [33m%q([39;49;00m[33mMom said, "Don't do that."[39;49;00m[33m)[39;49;00m$
   245^Istring.gsub([33m/[39;49;00m[33m['"][39;49;00m[33m/[39;49;00m) { [33m'[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m+[31m$&[39;49;00m }$
   246^Istring.gsub([33m/[39;49;00m[33m['"][39;49;00m[33m/[39;49;00m, [33m'[39;49;00m[33m\[39;49;00m[33m&[39;49;00m[33m\[39;49;00m[33m&[39;49;00m[33m'[39;49;00m)$
   247^Istring.gsub([33m/[39;49;00m[33m[^A-Z][39;49;00m[33m/[39;49;00m) { [33m'[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m+[31m$&[39;49;00m }$
   248^I[33m"[39;49;00m[33mis a test![39;49;00m[33m"[39;49;00m.gsub([33m/[39;49;00m[33m\[39;49;00m[33mW[39;49;00m[33m/[39;49;00m) { [33m'[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m+[31m$&[39;49;00m }  [37m# no function like quotemeta?[39;49;00m$
   249^I$
   250^I$
   251^I[37m# @@PLEAC@@_1.14[39;49;00m$
   252^Istring.strip!$
   253^I$
   254^I$
   255^I[37m# @@PLEAC@@_1.15[39;49;00m$
   256^I[34mdef[39;49;00m [32mparse_csv[39;49;00m(text)$
   257^I    [34mnew[39;49;00m = text.scan([33m/[39;49;00m[33m"([^[39;49;00m[33m\[39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m]*(?:[39;49;00m[33m\\[39;49;00m[33m.[^[39;49;00m[33m\[39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m]*)*)",?|([^,]+),?|,[39;49;00m[33m/[39;49;00m)$
   258^I    [34mnew[39;49;00m << [34mnil[39;49;00m [34mif[39;49;00m text[-[34m1[39;49;00m] == [33m?,[39;49;00m$
   259^I    [34mnew[39;49;00m.flatten.compact$
   260^I[34mend[39;49;00m  $
   261^I$
   262^Iline = [33m%q<[39;49;00m[33mXYZZY,"","O'Reilly, Inc","Wall, Larry","a [39;49;00m[33m\[39;49;00m[33m"glug[39;49;00m[33m\[39;49;00m[33m" bit,",5,"Error, Core Dumped"[39;49;00m[33m>[39;49;00m$
   263^Ifields = parse_csv(line)$
   264^Ifields.each_with_index { |v,i|$
   265^I    [36mprint[39;49;00m [33m"[39;49;00m[33m#{[39;49;00mi[33m}[39;49;00m[33m : [39;49;00m[33m#{[39;49;00mv[33m}[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m;$
   266^I}$
   267^I$
   268^I$
   269^I[37m# @@PLEAC@@_1.16[39;49;00m$
   270^I[37m# Use the soundex.rb Library from Michael Neumann.[39;49;00m$
   271^I[37m# http://www.s-direktnet.de/homepages/neumann/rb_prgs/Soundex.rb[39;49;00m$
   272^I[36mrequire[39;49;00m [33m'[39;49;00m[33mSoundex[39;49;00m[33m'[39;49;00m$
   273^I$
   274^Icode = [31mText[39;49;00m::[31mSoundex[39;49;00m.soundex(string)$
   275^Icodes = [31mText[39;49;00m::[31mSoundex[39;49;00m.soundex(array)$
   276^I$
   277^I[37m# substitution function for getpwent():[39;49;00m$
   278^I[37m# returns an array of user entries,[39;49;00m$
   279^I[37m# each entry contains the username and the full name[39;49;00m$
   280^I[34mdef[39;49;00m [32mlogin_names[39;49;00m$
   281^I    result = []$
   282^I    [31mFile[39;49;00m.open([33m"[39;49;00m[33m/etc/passwd[39;49;00m[33m"[39;49;00m) { |file|$
   283^I        file.each_line { |line|$
   284^I            [34mnext[39;49;00m [34mif[39;49;00m line.match([33m/[39;49;00m[33m^[39;49;00m[33m#[39;49;00m[33m/[39;49;00m)$
   285^I            cols = line.split([33m"[39;49;00m[33m:[39;49;00m[33m"[39;49;00m)$
   286^I            result.push([cols[[34m0[39;49;00m], cols[[34m4[39;49;00m]])$
   287^I        }$
   288^I    }$
   289^I    result$
   290^I[34mend[39;49;00m$
   291^I$
   292^I[36mputs[39;49;00m [33m"[39;49;00m[33mLookup user: [39;49;00m[33m"[39;49;00m$
   293^Iuser = [31mSTDIN[39;49;00m.gets$
   294^Iuser.chomp!$
   295^I[36mexit[39;49;00m [34munless[39;49;00m user$
   296^Iname_code = [31mText[39;49;00m::[31mSoundex[39;49;00m.soundex(user)$
   297^I$
   298^Isplitter = [31mRegexp[39;49;00m.new([33m'[39;49;00m[33m([39;49;00m[33m\[39;49;00m[33mw+)[^,]*[39;49;00m[33m\b[39;49;00m[33m([39;49;00m[33m\[39;49;00m[33mw+)[39;49;00m[33m'[39;49;00m)$
   299^I[34mfor[39;49;00m username, fullname [34min[39;49;00m login_names [34mdo[39;49;00m$
   300^I    firstname, lastname = splitter.match(fullname)[[34m1[39;49;00m,[34m2[39;49;00m]$
   301^I    [34mif[39;49;00m name_code == [31mText[39;49;00m::[31mSoundex[39;49;00m.soundex(username)$
   302^I        || name_code == [31mText[39;49;00m::[31mSoundex[39;49;00m.soundex(firstname)$
   303^I        || name_code == [31mText[39;49;00m::[31mSoundex[39;49;00m.soundex(lastname)$
   304^I    [34mthen[39;49;00m$
   305^I        [36mputs[39;49;00m [33m"[39;49;00m[33m#{[39;49;00musername[33m}[39;49;00m[33m: [39;49;00m[33m#{[39;49;00mfirstname[33m}[39;49;00m[33m [39;49;00m[33m#{[39;49;00mlastname[33m}[39;49;00m[33m"[39;49;00m$
   306^I    [34mend[39;49;00m$
   307^I[34mend[39;49;00m$
   308^I$
   309^I$
   310^I[37m# @@PLEAC@@_1.17[39;49;00m$
   311^I[37m# @@INCLUDE@@ include/ruby/fixstyle.rb[39;49;00m$
   312^I$
   313^I$
   314^I[37m# @@PLEAC@@_1.18[39;49;00m$
   315^I[37m# @@INCLUDE@@ include/ruby/psgrep.rb[39;49;00m$
   316^I$
   317^I$
   318^I[37m# @@PLEAC@@_2.1[39;49;00m$
   319^I[37m# Matz tells that you can use Integer() for strict checked conversion.[39;49;00m$
   320^I[36mInteger[39;49;00m([33m"[39;49;00m[33mabc[39;49;00m[33m"[39;49;00m)$
   321^I[37m#=> `Integer': invalid value for Integer: "abc" (ArgumentError)[39;49;00m$
   322^I[36mInteger[39;49;00m([33m"[39;49;00m[33m567[39;49;00m[33m"[39;49;00m)$
   323^I[37m#=> 567[39;49;00m$
   324^I$
   325^I[37m# You may use Float() for floating point stuff[39;49;00m$
   326^I[36mInteger[39;49;00m([33m"[39;49;00m[33m56.7[39;49;00m[33m"[39;49;00m)$
   327^I[37m#=> `Integer': invalid value for Integer: "56.7" (ArgumentError)[39;49;00m$
   328^I[36mFloat[39;49;00m([33m"[39;49;00m[33m56.7[39;49;00m[33m"[39;49;00m)$
   329^I[37m#=> 56.7[39;49;00m$
   330^I$
   331^I[37m# You may also use a regexp for that[39;49;00m$
   332^I[34mif[39;49;00m string =~ [33m/[39;49;00m[33m^[+-]?[39;49;00m[33m\[39;49;00m[33md+$[39;49;00m[33m/[39;49;00m$
   333^I    [36mp[39;49;00m [33m'[39;49;00m[33mis an integer[39;49;00m[33m'[39;49;00m$
   334^I[34melse[39;49;00m$
   335^I    [36mp[39;49;00m [33m'[39;49;00m[33mis not[39;49;00m[33m'[39;49;00m$
   336^I[34mend[39;49;00m$
   337^I$
   338^I[34mif[39;49;00m string =~ [33m/[39;49;00m[33m^-?(?:[39;49;00m[33m\[39;49;00m[33md+(?:[39;49;00m[33m\[39;49;00m[33m.[39;49;00m[33m\[39;49;00m[33md*)?|[39;49;00m[33m\[39;49;00m[33m.[39;49;00m[33m\[39;49;00m[33md+)$[39;49;00m[33m/[39;49;00m$
   339^I    [36mp[39;49;00m [33m'[39;49;00m[33mis a decimal number[39;49;00m[33m'[39;49;00m$
   340^I[34melse[39;49;00m$
   341^I    [36mp[39;49;00m [33m'[39;49;00m[33mis not[39;49;00m[33m'[39;49;00m$
   342^I[34mend[39;49;00m$
   343^I$
   344^I$
   345^I[37m# @@PLEAC@@_2.2[39;49;00m$
   346^I[37m# equal(num1, num2, accuracy) : returns true if num1 and num2 are[39;49;00m$
   347^I[37m#   equal to accuracy number of decimal places[39;49;00m$
   348^I[34mdef[39;49;00m [32mequal[39;49;00m(i, j, a)$
   349^I    [36msprintf[39;49;00m([33m"[39;49;00m[33m%.[39;49;00m[33m#{[39;49;00ma[33m}[39;49;00m[33mg[39;49;00m[33m"[39;49;00m, i) == [36msprintf[39;49;00m([33m"[39;49;00m[33m%.[39;49;00m[33m#{[39;49;00ma[33m}[39;49;00m[33mg[39;49;00m[33m"[39;49;00m, j)$
   350^I[34mend[39;49;00m$
   351^I$
   352^Iwage = [34m536[39;49;00m                        [37m# $5.36/hour[39;49;00m$
   353^Iweek = [34m40[39;49;00m * wage                  [37m# $214.40[39;49;00m$
   354^I[36mprintf[39;49;00m([33m"[39;49;00m[33mOne week's wage is: [39;49;00m[33m\[39;49;00m[33m$%.2f[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m, week/[34m100[39;49;00m.[34m0[39;49;00m)$
   355^I$
   356^I$
   357^I[37m# @@PLEAC@@_2.3[39;49;00m$
   358^Inum.round                         [37m# rounds to integer[39;49;00m$
   359^I$
   360^Ia = [34m0[39;49;00m.[34m255[39;49;00m$
   361^Ib = [36msprintf[39;49;00m([33m"[39;49;00m[33m%.2f[39;49;00m[33m"[39;49;00m, a)$
   362^I[36mprint[39;49;00m  [33m"[39;49;00m[33mUnrounded: [39;49;00m[33m#{[39;49;00ma[33m}[39;49;00m[33m\n[39;49;00m[33mRounded: [39;49;00m[33m#{[39;49;00mb[33m}[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
   363^I[36mprintf[39;49;00m [33m"[39;49;00m[33mUnrounded: [39;49;00m[33m#{[39;49;00ma[33m}[39;49;00m[33m\n[39;49;00m[33mRounded: %.2f[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m, a$
   364^I$
   365^I[36mprint[39;49;00m [33m"[39;49;00m[33mnumber[39;49;00m[33m\t[39;49;00m[33mint[39;49;00m[33m\t[39;49;00m[33mfloor[39;49;00m[33m\t[39;49;00m[33mceil[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
   366^Ia = [ [34m3[39;49;00m.[34m3[39;49;00m , [34m3[39;49;00m.[34m5[39;49;00m , [34m3[39;49;00m.[34m7[39;49;00m, -[34m3[39;49;00m.[34m3[39;49;00m ]$
   367^I[34mfor[39;49;00m n [34min[39;49;00m a$
   368^I    [36mprintf[39;49;00m([33m"[39;49;00m[33m% .1f[39;49;00m[33m\t[39;49;00m[33m% .1f[39;49;00m[33m\t[39;49;00m[33m% .1f[39;49;00m[33m\t[39;49;00m[33m% .1f[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m,  [37m# at least I don't fake my output :)[39;49;00m$
   369^I           n, n.to_i, n.floor, n.ceil)$
   370^I[34mend[39;49;00m$
   371^I$
   372^I$
   373^I[37m# @@PLEAC@@_2.4[39;49;00m$
   374^I[34mdef[39;49;00m [32mdec2bin[39;49;00m(n)$
   375^I    [n].pack([33m"[39;49;00m[33mN[39;49;00m[33m"[39;49;00m).unpack([33m"[39;49;00m[33mB32[39;49;00m[33m"[39;49;00m)[[34m0[39;49;00m].sub([33m/[39;49;00m[33m^0+(?=[39;49;00m[33m\[39;49;00m[33md)[39;49;00m[33m/[39;49;00m, [33m'[39;49;00m[33m'[39;49;00m)$
   376^I[34mend[39;49;00m$
   377^I$
   378^I[34mdef[39;49;00m [32mbin2dec[39;49;00m(n)$
   379^I    [([33m"[39;49;00m[33m0[39;49;00m[33m"[39;49;00m*[34m32[39;49;00m+n.to_s)[-[34m32[39;49;00m..-[34m1[39;49;00m]].pack([33m"[39;49;00m[33mB32[39;49;00m[33m"[39;49;00m).unpack([33m"[39;49;00m[33mN[39;49;00m[33m"[39;49;00m)[[34m0[39;49;00m]$
   380^I[34mend[39;49;00m$
   381^I$
   382^I$
   383^I[37m# @@PLEAC@@_2.5[39;49;00m$
   384^I[34mfor[39;49;00m i [34min[39;49;00m x .. y$
   385^I    [37m# i is set to every integer from x to y, inclusive[39;49;00m$
   386^I[34mend[39;49;00m$
   387^I$
   388^Ix.step(y,[34m7[39;49;00m) { |i|$
   389^I    [37m# i is set to every integer from x to y, stepsize = 7[39;49;00m$
   390^I}$
   391^I$
   392^I[36mprint[39;49;00m [33m"[39;49;00m[33mInfancy is: [39;49;00m[33m"[39;49;00m$
   393^I([34m0[39;49;00m..[34m2[39;49;00m).each { |i|$
   394^I    [36mprint[39;49;00m i, [33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m$
   395^I}$
   396^I[36mprint[39;49;00m [33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
   397^I$
   398^I$
   399^I[37m# @@PLEAC@@_2.6[39;49;00m$
   400^I[37m# We can add conversion methods to the Integer class,[39;49;00m$
   401^I[37m# this makes a roman number just a representation for normal numbers.[39;49;00m$
   402^I[34mclass[39;49;00m [04m[32mInteger[39;49;00m$
   403^I    $
   404^I    [31m@@romanlist[39;49;00m = [[[33m"[39;49;00m[33mM[39;49;00m[33m"[39;49;00m, [34m1000[39;49;00m],$
   405^I                   [[33m"[39;49;00m[33mCM[39;49;00m[33m"[39;49;00m, [34m900[39;49;00m],$
   406^I                   [[33m"[39;49;00m[33mD[39;49;00m[33m"[39;49;00m,  [34m500[39;49;00m],$
   407^I                   [[33m"[39;49;00m[33mCD[39;49;00m[33m"[39;49;00m, [34m400[39;49;00m],$
   408^I                   [[33m"[39;49;00m[33mC[39;49;00m[33m"[39;49;00m,  [34m100[39;49;00m],$
   409^I                   [[33m"[39;49;00m[33mXC[39;49;00m[33m"[39;49;00m,  [34m90[39;49;00m],$
   410^I                   [[33m"[39;49;00m[33mL[39;49;00m[33m"[39;49;00m,   [34m50[39;49;00m],$
   411^I                   [[33m"[39;49;00m[33mXL[39;49;00m[33m"[39;49;00m,  [34m40[39;49;00m],$
   412^I                   [[33m"[39;49;00m[33mX[39;49;00m[33m"[39;49;00m,   [34m10[39;49;00m],$
   413^I                   [[33m"[39;49;00m[33mIX[39;49;00m[33m"[39;49;00m,   [34m9[39;49;00m],$
   414^I                   [[33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m,    [34m5[39;49;00m],$
   415^I                   [[33m"[39;49;00m[33mIV[39;49;00m[33m"[39;49;00m,   [34m4[39;49;00m],$
   416^I                   [[33m"[39;49;00m[33mI[39;49;00m[33m"[39;49;00m,    [34m1[39;49;00m]]$
   417^I    $
   418^I    [34mdef[39;49;00m [32mto_roman[39;49;00m$
   419^I        remains = [36mself[39;49;00m$
   420^I        roman = [33m"[39;49;00m[33m"[39;49;00m$
   421^I        [34mfor[39;49;00m sym, num [34min[39;49;00m [31m@@romanlist[39;49;00m$
   422^I            [34mwhile[39;49;00m remains >= num$
   423^I                remains -= num$
   424^I                roman << sym$
   425^I            [34mend[39;49;00m$
   426^I        [34mend[39;49;00m$
   427^I        roman$
   428^I    [34mend[39;49;00m$
   429^I    $
   430^I    [34mdef[39;49;00m [04m[32mInteger[39;49;00m.[32mfrom_roman[39;49;00m(roman)$
   431^I        ustr = roman.upcase$
   432^I        sum = [34m0[39;49;00m$
   433^I        [34mfor[39;49;00m entry [34min[39;49;00m [31m@@romanlist[39;49;00m$
   434^I            sym, num = entry[[34m0[39;49;00m], entry[[34m1[39;49;00m]$
   435^I            [34mwhile[39;49;00m sym == ustr[[34m0[39;49;00m, sym.length]$
   436^I                sum += num$
   437^I                ustr.slice!([34m0[39;49;00m, sym.length)$
   438^I            [34mend[39;49;00m$
   439^I        [34mend[39;49;00m$
   440^I        sum$
   441^I    [34mend[39;49;00m$
   442^I    $
   443^I[34mend[39;49;00m$
   444^I$
   445^I$
   446^Iroman_fifteen = [34m15[39;49;00m.to_roman$
   447^I[36mputs[39;49;00m [33m"[39;49;00m[33mRoman for fifteen is [39;49;00m[33m#{[39;49;00mroman_fifteen[33m}[39;49;00m[33m"[39;49;00m$
   448^Ii = [36mInteger[39;49;00m.from_roman(roman_fifteen)$
   449^I[36mputs[39;49;00m [33m"[39;49;00m[33mConverted back, [39;49;00m[33m#{[39;49;00mroman_fifteen[33m}[39;49;00m[33m is [39;49;00m[33m#{[39;49;00mi[33m}[39;49;00m[33m"[39;49;00m$
   450^I$
   451^I[37m# check[39;49;00m$
   452^I[34mfor[39;49;00m i [34min[39;49;00m ([34m1[39;49;00m..[34m3900[39;49;00m)$
   453^I    r = i.to_roman$
   454^I    j = [36mInteger[39;49;00m.from_roman(r)$
   455^I    [34mif[39;49;00m i != j$
   456^I        [36mputs[39;49;00m [33m"[39;49;00m[33merror: [39;49;00m[33m#{[39;49;00mi[33m}[39;49;00m[33m : [39;49;00m[33m#{[39;49;00mr[33m}[39;49;00m[33m - [39;49;00m[33m#{[39;49;00mj[33m}[39;49;00m[33m"[39;49;00m$
   457^I    [34mend[39;49;00m$
   458^I[34mend[39;49;00m$
   459^I$
   460^I$
   461^I[37m# @@PLEAC@@_2.7[39;49;00m$
   462^Irandom = [36mrand[39;49;00m(y-x+[34m1[39;49;00m)+x$
   463^I$
   464^Ichars = [[33m"[39;49;00m[33mA[39;49;00m[33m"[39;49;00m..[33m"[39;49;00m[33mZ[39;49;00m[33m"[39;49;00m,[33m"[39;49;00m[33ma[39;49;00m[33m"[39;49;00m..[33m"[39;49;00m[33mz[39;49;00m[33m"[39;49;00m,[33m"[39;49;00m[33m0[39;49;00m[33m"[39;49;00m..[33m"[39;49;00m[33m9[39;49;00m[33m"[39;49;00m].collect { |r| r.to_a }.join + [33m%q([39;49;00m[33m!@$%^&*[39;49;00m[33m)[39;49;00m$
   465^Ipassword = ([34m1[39;49;00m..[34m8[39;49;00m).collect { chars[[36mrand[39;49;00m(chars.size)] }.pack([33m"[39;49;00m[33mC*[39;49;00m[33m"[39;49;00m)$
   466^I$
   467^I$
   468^I[37m# @@PLEAC@@_2.8[39;49;00m$
   469^I[36msrand[39;49;00m        [37m# uses a combination of the time, the process id, and a sequence number[39;49;00m$
   470^I[36msrand[39;49;00m(val)   [37m# for repeatable behaviour[39;49;00m$
   471^I$
   472^I$
   473^I[37m# @@PLEAC@@_2.9[39;49;00m$
   474^I[37m# from the randomr lib: [39;49;00m$
   475^I[37m# http://raa.ruby-lang.org/project/randomr/[39;49;00m$
   476^I----> [33mhttp[39;49;00m:[33m/[39;49;00m[33m/[39;49;00mraa.ruby-lang.org/project/randomr/$
   477^I$
   478^I[36mrequire[39;49;00m [33m'[39;49;00m[33mrandom/mersenne_twister[39;49;00m[33m'[39;49;00m$
   479^Imers = [31mRandom[39;49;00m::[31mMersenneTwister[39;49;00m.new [34m123456789[39;49;00m$
   480^I[36mputs[39;49;00m mers.rand([34m0[39;49;00m)    [37m# 0.550321932544541[39;49;00m$
   481^I[36mputs[39;49;00m mers.rand([34m10[39;49;00m)   [37m# 2[39;49;00m$
   482^I$
   483^I[37m# using online sources of random data via the realrand package:[39;49;00m$
   484^I[37m# http://raa.ruby-lang.org/project/realrand/[39;49;00m$
   485^I[37m# **Note**[39;49;00m$
   486^I[37m# The following online services are used in this package:[39;49;00m$
   487^I[37m#   http://www.random.org - source: atmospheric noise [39;49;00m$
   488^I[37m#   http://www.fourmilab.ch/hotbits - source: radioactive decay timings[39;49;00m$
   489^I[37m#   http://random.hd.org - source: entropy from local and network noise[39;49;00m$
   490^I[37m# Please visit the sites and respect the rules of each service.[39;49;00m$
   491^I$
   492^I[36mrequire[39;49;00m [33m'[39;49;00m[33mrandom/online[39;49;00m[33m'[39;49;00m$
   493^I$
   494^Igenerator1 = [31mRandom[39;49;00m::[31mRandomOrg[39;49;00m.new$
   495^I[36mputs[39;49;00m generator1.randbyte([34m5[39;49;00m).join([33m"[39;49;00m[33m,[39;49;00m[33m"[39;49;00m)$
   496^I[36mputs[39;49;00m generator1.randnum([34m10[39;49;00m, [34m1[39;49;00m, [34m6[39;49;00m).join([33m"[39;49;00m[33m,[39;49;00m[33m"[39;49;00m)  [37m# Roll dice 10 times.[39;49;00m$
   497^I$
   498^Igenerator2 = [31mRandom[39;49;00m::[31mFourmiLab[39;49;00m.new$
   499^I[36mputs[39;49;00m generator2.randbyte([34m5[39;49;00m).join([33m"[39;49;00m[33m,[39;49;00m[33m"[39;49;00m)$
   500^I[37m# randnum is not supported.[39;49;00m$
   501^I$
   502^Igenerator3 = [31mRandom[39;49;00m::[31mEntropyPool[39;49;00m.new$
   503^I[36mputs[39;49;00m generator3.randbyte([34m5[39;49;00m).join([33m"[39;49;00m[33m,[39;49;00m[33m"[39;49;00m)$
   504^I[37m# randnum is not supported.[39;49;00m$
   505^I$
   506^I$
   507^I[37m# @@PLEAC@@_2.10[39;49;00m$
   508^I[34mdef[39;49;00m [32mgaussian_rand[39;49;00m$
   509^I    [34mbegin[39;49;00m$
   510^I        u1 = [34m2[39;49;00m * [36mrand[39;49;00m() - [34m1[39;49;00m$
   511^I        u2 = [34m2[39;49;00m * [36mrand[39;49;00m() - [34m1[39;49;00m$
   512^I        w = u1*u1 + u2*u2$
   513^I    [34mend[39;49;00m [34mwhile[39;49;00m (w >= [34m1[39;49;00m)$
   514^I    w = [31mMath[39;49;00m.sqrt((-[34m2[39;49;00m*[31mMath[39;49;00m.log(w))/w)$
   515^I    [ u2*w, u1*w ]$
   516^I[34mend[39;49;00m$
   517^I$
   518^Imean = [34m25[39;49;00m$
   519^Isdev = [34m2[39;49;00m$
   520^Isalary = gaussian_rand[[34m0[39;49;00m] * sdev + mean$
   521^I[36mprintf[39;49;00m([33m"[39;49;00m[33mYou have been hired at [39;49;00m[33m\[39;49;00m[33m$%.2f[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m, salary)$
   522^I$
   523^I$
   524^I[37m# @@PLEAC@@_2.11[39;49;00m$
   525^I[34mdef[39;49;00m [32mdeg2rad[39;49;00m(d)$
   526^I    (d/[34m180[39;49;00m.[34m0[39;49;00m)*[31mMath[39;49;00m::[31mPI[39;49;00m$
   527^I[34mend[39;49;00m$
   528^I$
   529^I[34mdef[39;49;00m [32mrad2deg[39;49;00m(r)$
   530^I    (r/[31mMath[39;49;00m::[31mPI[39;49;00m)*[34m180[39;49;00m$
   531^I[34mend[39;49;00m$
   532^I$
   533^I$
   534^I[37m# @@PLEAC@@_2.12[39;49;00m$
   535^Isin_val = [31mMath[39;49;00m.sin(angle)$
   536^Icos_val = [31mMath[39;49;00m.cos(angle)$
   537^Itan_val = [31mMath[39;49;00m.tan(angle)$
   538^I$
   539^I[37m# AFAIK Ruby's Math module doesn't provide acos/asin[39;49;00m$
   540^I[37m# While we're at it, let's also define missing hyperbolic functions[39;49;00m$
   541^I[34mmodule[39;49;00m [04m[36mMath[39;49;00m$
   542^I    [34mdef[39;49;00m [04m[32mMath[39;49;00m.[32masin[39;49;00m(x)$
   543^I        atan2(x, sqrt([34m1[39;49;00m - x**[34m2[39;49;00m))$
   544^I    [34mend[39;49;00m$
   545^I    [34mdef[39;49;00m [04m[32mMath[39;49;00m.[32macos[39;49;00m(x)$
   546^I        atan2(sqrt([34m1[39;49;00m - x**[34m2[39;49;00m), x)$
   547^I    [34mend[39;49;00m$
   548^I    [34mdef[39;49;00m [04m[32mMath[39;49;00m.[32matan[39;49;00m(x)$
   549^I        atan2(x, [34m1[39;49;00m)$
   550^I    [34mend[39;49;00m$
   551^I    [34mdef[39;49;00m [04m[32mMath[39;49;00m.[32msinh[39;49;00m(x)$
   552^I        (exp(x) - exp(-x)) / [34m2[39;49;00m$
   553^I    [34mend[39;49;00m$
   554^I    [34mdef[39;49;00m [04m[32mMath[39;49;00m.[32mcosh[39;49;00m(x)$
   555^I        (exp(x) + exp(-x)) / [34m2[39;49;00m$
   556^I    [34mend[39;49;00m$
   557^I    [34mdef[39;49;00m [04m[32mMath[39;49;00m.[32mtanh[39;49;00m(x)$
   558^I        sinh(x) / cosh(x)$
   559^I    [34mend[39;49;00m$
   560^I[34mend[39;49;00m$
   561^I$
   562^I[37m# The support for Complex numbers is not built-in[39;49;00m$
   563^Iy = [31mMath[39;49;00m.acos([34m3[39;49;00m.[34m7[39;49;00m)$
   564^I[37m#=> in `sqrt': square root for negative number (ArgumentError)[39;49;00m$
   565^I$
   566^I[37m# There is an implementation of Complex numbers in 'complex.rb' in current[39;49;00m$
   567^I[37m# Ruby distro, but it doesn't support atan2 with complex args, so it doesn't[39;49;00m$
   568^I[37m# solve this problem.[39;49;00m$
   569^I$
   570^I$
   571^I[37m# @@PLEAC@@_2.13[39;49;00m$
   572^Ilog_e = [31mMath[39;49;00m.log(val)$
   573^Ilog_10 = [31mMath[39;49;00m.log10(val)$
   574^I$
   575^I[34mdef[39;49;00m [32mlog_base[39;49;00m(base, val)$
   576^I    [31mMath[39;49;00m.log(val)/[31mMath[39;49;00m.log(base)$
   577^I[34mend[39;49;00m$
   578^I$
   579^Ianswer = log_base([34m10[39;49;00m, [34m10_000[39;49;00m)$
   580^I[36mputs[39;49;00m [33m"[39;49;00m[33mlog10(10,000) = [39;49;00m[33m#{[39;49;00manswer[33m}[39;49;00m[33m"[39;49;00m$
   581^I$
   582^I$
   583^I[37m# @@PLEAC@@_2.14[39;49;00m$
   584^I[36mrequire[39;49;00m [33m'[39;49;00m[33mmatrix.rb[39;49;00m[33m'[39;49;00m$
   585^I$
   586^Ia = [31mMatrix[39;49;00m[[[34m3[39;49;00m, [34m2[39;49;00m, [34m3[39;49;00m], [[34m5[39;49;00m, [34m9[39;49;00m, [34m8[39;49;00m]]$
   587^Ib = [31mMatrix[39;49;00m[[[34m4[39;49;00m, [34m7[39;49;00m], [[34m9[39;49;00m, [34m3[39;49;00m], [[34m8[39;49;00m, [34m1[39;49;00m]]$
   588^Ic = a * b$
   589^I$
   590^Ia.row_size$
   591^Ia.column_size$
   592^I$
   593^Ic.det$
   594^Ia.transpose$
   595^I$
   596^I$
   597^I[37m# @@PLEAC@@_2.15[39;49;00m$
   598^I[36mrequire[39;49;00m [33m'[39;49;00m[33mcomplex.rb[39;49;00m[33m'[39;49;00m$
   599^I[36mrequire[39;49;00m [33m'[39;49;00m[33mrational.rb[39;49;00m[33m'[39;49;00m$
   600^I$
   601^Ia = [31mComplex[39;49;00m([34m3[39;49;00m, [34m5[39;49;00m)              [37m# 3 + 5i[39;49;00m$
   602^Ib = [31mComplex[39;49;00m([34m2[39;49;00m, -[34m2[39;49;00m)             [37m# 2 - 2i[39;49;00m$
   603^I[36mputs[39;49;00m [33m"[39;49;00m[33mc = [39;49;00m[33m#{[39;49;00ma*b[33m}[39;49;00m[33m"[39;49;00m$
   604^I$
   605^Ic = a * b$
   606^Id = [34m3[39;49;00m + [34m4[39;49;00m*[31mComplex[39;49;00m::I$
   607^I$
   608^I[36mprintf[39;49;00m [33m"[39;49;00m[33msqrt([39;49;00m[33m#{[39;49;00md[33m}[39;49;00m[33m) = %s[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m, [31mMath[39;49;00m.sqrt(d)$
   609^I$
   610^I$
   611^I[37m# @@PLEAC@@_2.16[39;49;00m$
   612^Inumber = hexadecimal.hex$
   613^Inumber = octal.oct$
   614^I$
   615^I[36mprint[39;49;00m [33m"[39;49;00m[33mGimme a number in decimal, octal, or hex: [39;49;00m[33m"[39;49;00m$
   616^Inum = [36mgets[39;49;00m.chomp$
   617^I[36mexit[39;49;00m [34munless[39;49;00m defined?(num)$
   618^Inum = num.oct [34mif[39;49;00m num =~ [33m/[39;49;00m[33m^0[39;49;00m[33m/[39;49;00m  [37m# does both oct and hex  [39;49;00m$
   619^I[36mprintf[39;49;00m [33m"[39;49;00m[33m%d %x %o[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m, num, num, num$
   620^I$
   621^I[36mprint[39;49;00m [33m"[39;49;00m[33mEnter file permission in octal: [39;49;00m[33m"[39;49;00m$
   622^Ipermissions = [36mgets[39;49;00m.chomp$
   623^I[34mraise[39;49;00m [33m"[39;49;00m[33mExiting ...[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m [34munless[39;49;00m defined?(permissions)$
   624^I[36mputs[39;49;00m [33m"[39;49;00m[33mThe decimal value is [39;49;00m[33m#{[39;49;00mpermissions.oct[33m}[39;49;00m[33m"[39;49;00m$
   625^I$
   626^I$
   627^I[37m# @@PLEAC@@_2.17[39;49;00m$
   628^I[34mdef[39;49;00m [32mcommify[39;49;00m(n)$
   629^I    n.to_s =~ [33m/[39;49;00m[33m([^[39;49;00m[33m\[39;49;00m[33m.]*)([39;49;00m[33m\[39;49;00m[33m..*)?[39;49;00m[33m/[39;49;00m$
   630^I    int, dec = [31m$1[39;49;00m.reverse, [31m$2[39;49;00m ? [31m$2[39;49;00m : [33m"[39;49;00m[33m"[39;49;00m$
   631^I    [34mwhile[39;49;00m int.gsub!([33m/[39;49;00m[33m(,|[39;49;00m[33m\[39;49;00m[33m.|^)([39;49;00m[33m\[39;49;00m[33md{3})([39;49;00m[33m\[39;49;00m[33md)[39;49;00m[33m/[39;49;00m, [33m'[39;49;00m[33m\1[39;49;00m[33m\2[39;49;00m[33m,[39;49;00m[33m\3[39;49;00m[33m'[39;49;00m)$
   632^I    [34mend[39;49;00m$
   633^I    int.reverse + dec$
   634^I[34mend[39;49;00m$
   635^I$
   636^I$
   637^I[37m# @@PLEAC@@_2.18[39;49;00m$
   638^I[36mprintf[39;49;00m [33m"[39;49;00m[33mIt took %d hour%s[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m, time, time == [34m1[39;49;00m ? [33m"[39;49;00m[33m"[39;49;00m : [33m"[39;49;00m[33ms[39;49;00m[33m"[39;49;00m$
   639^I$
   640^I[37m# dunno if an equivalent to Lingua::EN::Inflect exists...[39;49;00m$
   641^I$
   642^I$
   643^I[37m# @@PLEAC@@_2.19[39;49;00m$
   644^I[37m#-----------------------------[39;49;00m$
   645^I[37m#!/usr/bin/ruby[39;49;00m$
   646^I[37m# bigfact - calculating prime factors[39;49;00m$
   647^I[34mdef[39;49;00m [32mfactorize[39;49;00m(orig)$
   648^I    factors = {}$
   649^I    factors.default = [34m0[39;49;00m     [37m# return 0 instead nil if key not found in hash[39;49;00m$
   650^I    n = orig$
   651^I    i = [34m2[39;49;00m$
   652^I    sqi = [34m4[39;49;00m                 [37m# square of i[39;49;00m$
   653^I    [34mwhile[39;49;00m sqi <= n [34mdo[39;49;00m$
   654^I        [34mwhile[39;49;00m n.modulo(i) == [34m0[39;49;00m [34mdo[39;49;00m$
   655^I            n /= i$
   656^I            factors[i] += [34m1[39;49;00m$
   657^I            [37m# puts "Found factor #{i}"[39;49;00m$
   658^I        [34mend[39;49;00m$
   659^I        [37m# we take advantage of the fact that (i +1)**2 = i**2 + 2*i +1[39;49;00m$
   660^I        sqi += [34m2[39;49;00m * i + [34m1[39;49;00m$
   661^I        i += [34m1[39;49;00m$
   662^I    [34mend[39;49;00m$
   663^I    $
   664^I    [34mif[39;49;00m (n != [34m1[39;49;00m) && (n != orig)$
   665^I        factors[n] += [34m1[39;49;00m$
   666^I    [34mend[39;49;00m$
   667^I    factors$
   668^I[34mend[39;49;00m$
   669^I$
   670^I[34mdef[39;49;00m [32mprintfactorhash[39;49;00m(orig, factorcount)$
   671^I    [36mprint[39;49;00m [36mformat[39;49;00m([33m"[39;49;00m[33m%-10d [39;49;00m[33m"[39;49;00m, orig)$
   672^I    [34mif[39;49;00m factorcount.length == [34m0[39;49;00m$
   673^I        [36mprint[39;49;00m [33m"[39;49;00m[33mPRIME[39;49;00m[33m"[39;49;00m$
   674^I    [34melse[39;49;00m$
   675^I        [37m# sorts after number, because the hash keys are numbers[39;49;00m$
   676^I        factorcount.sort.each { |factor,exponent|$
   677^I            [36mprint[39;49;00m factor$
   678^I            [34mif[39;49;00m exponent > [34m1[39;49;00m$
   679^I                [36mprint[39;49;00m [33m"[39;49;00m[33m**[39;49;00m[33m"[39;49;00m, exponent$
   680^I            [34mend[39;49;00m$
   681^I            [36mprint[39;49;00m [33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m$
   682^I        }$
   683^I    [34mend[39;49;00m$
   684^I    [36mputs[39;49;00m$
   685^I[34mend[39;49;00m$
   686^I$
   687^I[34mfor[39;49;00m arg [34min[39;49;00m [31mARGV[39;49;00m$
   688^I    n = arg.to_i$
   689^I    mfactors = factorize(n)$
   690^I    printfactorhash(n, mfactors)$
   691^I[34mend[39;49;00m$
   692^I[37m#-----------------------------[39;49;00m$
   693^I$
   694^I$
   695^I[37m# @@PLEAC@@_3.0[39;49;00m$
   696^I[36mputs[39;49;00m [31mTime[39;49;00m.now$
   697^I$
   698^I[36mprint[39;49;00m [33m"[39;49;00m[33mToday is day [39;49;00m[33m"[39;49;00m, [31mTime[39;49;00m.now.yday, [33m"[39;49;00m[33m of the current year.[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
   699^I[36mprint[39;49;00m [33m"[39;49;00m[33mToday is day [39;49;00m[33m"[39;49;00m, [31mTime[39;49;00m.now.day, [33m"[39;49;00m[33m of the current month.[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
   700^I$
   701^I$
   702^I[37m# @@PLEAC@@_3.1[39;49;00m$
   703^Iday, month, year = [31mTime[39;49;00m.now.day, [31mTime[39;49;00m.now.month, [31mTime[39;49;00m.now.year$
   704^I[37m# or[39;49;00m$
   705^Iday, month, year = [31mTime[39;49;00m.now.to_a[[34m3[39;49;00m..[34m5[39;49;00m]$
   706^I$
   707^Itl = [31mTime[39;49;00m.now.localtime$
   708^I[36mprintf[39;49;00m([33m"[39;49;00m[33mThe current date is %04d %02d %02d[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m, tl.year, tl.month, tl.day)$
   709^I$
   710^I[31mTime[39;49;00m.now.localtime.strftime([33m"[39;49;00m[33m%Y-%m-%d[39;49;00m[33m"[39;49;00m)$
   711^I$
   712^I$
   713^I[37m# @@PLEAC@@_3.2[39;49;00m$
   714^I[31mTime[39;49;00m.local(year, month, day, hour, minute, second).tv_sec$
   715^I[31mTime[39;49;00m.gm(year, month, day, hour, minute, second).tv_sec$
   716^I$
   717^I$
   718^I[37m# @@PLEAC@@_3.3[39;49;00m$
   719^Isec, min, hour, day, month, year, wday, yday, isdst, zone = [31mTime[39;49;00m.at(epoch_secs).to_a$
   720^I$
   721^I$
   722^I[37m# @@PLEAC@@_3.4[39;49;00m$
   723^Iwhen_ = now + difference         [37m# now -> Time ; difference -> Numeric (delta in seconds)[39;49;00m$
   724^Ithen_ = now - difference$
   725^I$
   726^I$
   727^I[37m# @@PLEAC@@_3.5[39;49;00m$
   728^Ibree = [34m361535725[39;49;00m$
   729^Inat  =  [34m96201950[39;49;00m$
   730^I$
   731^Idifference = bree - nat$
   732^I[36mputs[39;49;00m [33m"[39;49;00m[33mThere were [39;49;00m[33m#{[39;49;00mdifference[33m}[39;49;00m[33m seconds between Nat and Bree[39;49;00m[33m"[39;49;00m$
   733^I$
   734^Iseconds    =  difference % [34m60[39;49;00m$
   735^Idifference = (difference - seconds) / [34m60[39;49;00m$
   736^Iminutes    =  difference % [34m60[39;49;00m$
   737^Idifference = (difference - minutes) / [34m60[39;49;00m$
   738^Ihours      =  difference % [34m24[39;49;00m$
   739^Idifference = (difference - hours)   / [34m24[39;49;00m$
   740^Idays       =  difference % [34m7[39;49;00m$
   741^Iweeks      = (difference - days)    /  [34m7[39;49;00m$
   742^I$
   743^I[36mputs[39;49;00m [33m"[39;49;00m[33m([39;49;00m[33m#{[39;49;00mweeks[33m}[39;49;00m[33m weeks, [39;49;00m[33m#{[39;49;00mdays[33m}[39;49;00m[33m days, [39;49;00m[33m#{[39;49;00mhours[33m}[39;49;00m[33m:[39;49;00m[33m#{[39;49;00mminutes[33m}[39;49;00m[33m:[39;49;00m[33m#{[39;49;00mseconds[33m}[39;49;00m[33m)[39;49;00m[33m"[39;49;00m$
   744^I$
   745^I$
   746^I[37m# @@PLEAC@@_3.6[39;49;00m$
   747^Imonthday, weekday, yearday = date.mday, date.wday, date.yday$
   748^I$
   749^I[37m# AFAIK the week number is not just a division since week boundaries are on sundays[39;49;00m$
   750^Iweeknum = d.strftime([33m"[39;49;00m[33m%U[39;49;00m[33m"[39;49;00m).to_i + [34m1[39;49;00m$
   751^I$
   752^Iyear  = [34m1981[39;49;00m$
   753^Imonth = [33m"[39;49;00m[33mjun[39;49;00m[33m"[39;49;00m                     [37m# or `6' if you want to emulate a broken language[39;49;00m$
   754^Iday   = [34m16[39;49;00m$
   755^It = [31mTime[39;49;00m.mktime(year, month, day)$
   756^I[36mprint[39;49;00m [33m"[39;49;00m[33m#{[39;49;00mmonth[33m}[39;49;00m[33m/[39;49;00m[33m#{[39;49;00mday[33m}[39;49;00m[33m/[39;49;00m[33m#{[39;49;00myear[33m}[39;49;00m[33m was a [39;49;00m[33m"[39;49;00m, t.strftime([33m"[39;49;00m[33m%A[39;49;00m[33m"[39;49;00m), [33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
   757^I$
   758^I$
   759^I[37m# @@PLEAC@@_3.7[39;49;00m$
   760^Iyyyy, mm, dd = [31m$1[39;49;00m, [31m$2[39;49;00m, [31m$3[39;49;00m [34mif[39;49;00m [33m"[39;49;00m[33m1998-06-25[39;49;00m[33m"[39;49;00m =~ [33m/[39;49;00m[33m([39;49;00m[33m\[39;49;00m[33md+)-([39;49;00m[33m\[39;49;00m[33md+)-([39;49;00m[33m\[39;49;00m[33md+)[39;49;00m[33m/[39;49;00m$
   761^I$
   762^Iepoch_seconds = [31mTime[39;49;00m.mktime(yyyy, mm, dd).tv_sec$
   763^I$
   764^I[37m# dunno an equivalent to Date::Manip#ParseDate[39;49;00m$
   765^I$
   766^I$
   767^I[37m# @@PLEAC@@_3.8[39;49;00m$
   768^Istring = [31mTime[39;49;00m.at(epoch_secs)$
   769^I[31mTime[39;49;00m.at([34m1234567890[39;49;00m).gmtime        [37m# gives: Fri Feb 13 23:31:30 UTC 2009[39;49;00m$
   770^I$
   771^Itime = [31mTime[39;49;00m.mktime([34m1973[39;49;00m, [33m"[39;49;00m[33mjan[39;49;00m[33m"[39;49;00m, [34m18[39;49;00m, [34m3[39;49;00m, [34m45[39;49;00m, [34m50[39;49;00m)$
   772^I[36mprint[39;49;00m [33m"[39;49;00m[33mIn localtime it gives: [39;49;00m[33m"[39;49;00m, time.localtime, [33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
   773^I$
   774^I$
   775^I[37m# @@PLEAC@@_3.9[39;49;00m$
   776^I[37m# Ruby provides micro-seconds in Time object[39;49;00m$
   777^I[31mTime[39;49;00m.now.usec$
   778^I$
   779^I[37m# Ruby gives the seconds in floating format when substracting two Time objects[39;49;00m$
   780^Ibefore = [31mTime[39;49;00m.now$
   781^Iline = [36mgets[39;49;00m$
   782^Ielapsed = [31mTime[39;49;00m.now - before$
   783^I[36mputs[39;49;00m [33m"[39;49;00m[33mYou took [39;49;00m[33m#{[39;49;00melapsed[33m}[39;49;00m[33m seconds.[39;49;00m[33m"[39;49;00m$
   784^I$
   785^I[37m# On my Celeron-400 with Linux-2.2.19-14mdk, average for three execs are:[39;49;00m$
   786^I[37m#   This Ruby version:       average 0.00321 sec[39;49;00m$
   787^I[37m#   Cookbook's Perl version: average 0.00981 sec[39;49;00m$
   788^Isize = [34m500[39;49;00m$
   789^Inumber_of_times = [34m100[39;49;00m$
   790^Itotal_time = [34m0[39;49;00m$
   791^Inumber_of_times.times {$
   792^I    [37m# populate array[39;49;00m$
   793^I    array = []$
   794^I    size.times { array << [36mrand[39;49;00m }$
   795^I    [37m# sort it[39;49;00m$
   796^I    begin_ = [31mTime[39;49;00m.now$
   797^I    array.sort!$
   798^I    time = [31mTime[39;49;00m.now - begin_$
   799^I    total_time += time$
   800^I}$
   801^I[36mprintf[39;49;00m [33m"[39;49;00m[33mOn average, sorting %d random numbers takes %.5f seconds[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m,$
   802^I    size, (total_time/[36mFloat[39;49;00m(number_of_times))$
   803^I$
   804^I$
   805^I[37m# @@PLEAC@@_3.10[39;49;00m$
   806^I[36msleep[39;49;00m([34m0[39;49;00m.[34m005[39;49;00m)                      [37m# Ruby is definitely not as broken as Perl :)[39;49;00m$
   807^I[37m# (may be interrupted by sending the process a SIGALRM)[39;49;00m$
   808^I$
   809^I$
   810^I[37m# @@PLEAC@@_3.11[39;49;00m$
   811^I[37m#!/usr/bin/ruby -w[39;49;00m$
   812^I[37m# hopdelta - feed mail header, produce lines[39;49;00m$
   813^I[37m#            showing delay at each hop.[39;49;00m$
   814^I[36mrequire[39;49;00m [33m'[39;49;00m[33mtime[39;49;00m[33m'[39;49;00m$
   815^I[34mclass[39;49;00m [04m[32mMailHopDelta[39;49;00m$
   816^I$
   817^I    [34mdef[39;49;00m [32minitialize[39;49;00m(mail)$
   818^I        [31m@head[39;49;00m = mail.gsub([33m/[39;49;00m[33m\[39;49;00m[33mn[39;49;00m[33m\[39;49;00m[33ms+[39;49;00m[33m/[39;49;00m,[33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m)$
   819^I        [31m@topline[39;49;00m = [33m%w-Sender Recipient Time Delta-[39;49;00m$
   820^I        [31m@start_from[39;49;00m = mail.match([33m/[39;49;00m[33m^From.*[39;49;00m[33m\[39;49;00m[33m@([^[39;49;00m[33m\[39;49;00m[33ms>]*)[39;49;00m[33m/[39;49;00m)[[34m1[39;49;00m]$
   821^I        [31m@date[39;49;00m = [31mTime[39;49;00m.parse(mail.match([33m/[39;49;00m[33m^Date:[39;49;00m[33m\[39;49;00m[33ms+(.*)[39;49;00m[33m/[39;49;00m)[[34m1[39;49;00m])$
   822^I    [34mend[39;49;00m$
   823^I$
   824^I    [34mdef[39;49;00m [32mout[39;49;00m(line)$
   825^I         [33m"[39;49;00m[33m%-20.20s %-20.20s %-20.20s  %s[39;49;00m[33m"[39;49;00m % line$
   826^I    [34mend[39;49;00m$
   827^I$
   828^I    [34mdef[39;49;00m [32mhop_date[39;49;00m(day)$
   829^I        day.strftime([33m"[39;49;00m[33m%I:%M:%S %Y/%m/%d[39;49;00m[33m"[39;49;00m)$
   830^I    [34mend[39;49;00m$
   831^I$
   832^I    [34mdef[39;49;00m [32mputs_hops[39;49;00m$
   833^I        [36mputs[39;49;00m out([31m@topline[39;49;00m) $
   834^I        [36mputs[39;49;00m out([[33m'[39;49;00m[33mStart[39;49;00m[33m'[39;49;00m, [31m@start_from[39;49;00m, hop_date([31m@date[39;49;00m),[33m'[39;49;00m[33m'[39;49;00m])$
   835^I        [31m@head[39;49;00m.split([33m/[39;49;00m[33m\[39;49;00m[33mn[39;49;00m[33m/[39;49;00m).reverse.grep([33m/[39;49;00m[33m^Received:[39;49;00m[33m/[39;49;00m).each [34mdo[39;49;00m |hop|$
   836^I            hop.gsub!([33m/[39;49;00m[33m\[39;49;00m[33mbon (.*?) (id.*)[39;49;00m[33m/[39;49;00m,[33m'[39;49;00m[33m; [39;49;00m[33m\1[39;49;00m[33m'[39;49;00m)$
   837^I            whence = hop.match([33m/[39;49;00m[33m;[39;49;00m[33m\[39;49;00m[33ms+(.*)$[39;49;00m[33m/[39;49;00m)[[34m1[39;49;00m]$
   838^I            [34munless[39;49;00m whence$
   839^I                [36mwarn[39;49;00m [33m"[39;49;00m[33mBad received line: [39;49;00m[33m#{[39;49;00mhop[33m}[39;49;00m[33m"[39;49;00m$
   840^I                [34mnext[39;49;00m$
   841^I            [34mend[39;49;00m$
   842^I            from = [31m$+[39;49;00m [34mif[39;49;00m hop =~ [33m/[39;49;00m[33mfrom[39;49;00m[33m\[39;49;00m[33ms+([39;49;00m[33m\[39;49;00m[33mS+)|[39;49;00m[33m\[39;49;00m[33m((.*?)[39;49;00m[33m\[39;49;00m[33m)[39;49;00m[33m/[39;49;00m$
   843^I            by   = [31m$1[39;49;00m [34mif[39;49;00m hop =~ [33m/[39;49;00m[33mby[39;49;00m[33m\[39;49;00m[33ms+([39;49;00m[33m\[39;49;00m[33mS+[39;49;00m[33m\[39;49;00m[33m.[39;49;00m[33m\[39;49;00m[33mS+)[39;49;00m[33m/[39;49;00m$
   844^I            [34mnext[39;49;00m [34munless[39;49;00m now = [31mTime[39;49;00m.parse(whence).localtime$
   845^I            delta = now - [31m@date[39;49;00m$
   846^I            [36mputs[39;49;00m out([from, by, hop_date(now), hop_time(delta)])$
   847^I            [31m@date[39;49;00m = now$
   848^I        [34mend[39;49;00m$
   849^I    [34mend[39;49;00m$
   850^I$
   851^I    [34mdef[39;49;00m [32mhop_time[39;49;00m(secs)$
   852^I        sign = secs < [34m0[39;49;00m ? -[34m1[39;49;00m : [34m1[39;49;00m$
   853^I        days, secs = secs.abs.divmod([34m60[39;49;00m * [34m60[39;49;00m * [34m24[39;49;00m)$
   854^I        hours,secs = secs.abs.divmod([34m60[39;49;00m * [34m60[39;49;00m)$
   855^I        mins, secs = secs.abs.divmod([34m60[39;49;00m)$
   856^I        rtn =  [33m"[39;49;00m[33m%3ds[39;49;00m[33m"[39;49;00m % [secs  * sign]$
   857^I        rtn << [33m"[39;49;00m[33m%3dm[39;49;00m[33m"[39;49;00m % [mins  * sign] [34mif[39;49;00m mins  != [34m0[39;49;00m$
   858^I        rtn << [33m"[39;49;00m[33m%3dh[39;49;00m[33m"[39;49;00m % [hours * sign] [34mif[39;49;00m hours != [34m0[39;49;00m$
   859^I        rtn << [33m"[39;49;00m[33m%3dd[39;49;00m[33m"[39;49;00m % [days  * sign] [34mif[39;49;00m days  != [34m0[39;49;00m $
   860^I        rtn$
   861^I    [34mend[39;49;00m$
   862^I[34mend[39;49;00m$
   863^I$
   864^I[31m$/[39;49;00m = [33m"[39;49;00m[33m"[39;49;00m$
   865^Imail = [31mMailHopDelta[39;49;00m.new([31mARGF[39;49;00m.gets).puts_hops$
   866^I$
   867^I$
   868^I[37m# @@PLEAC@@_4.0[39;49;00m$
   869^Isingle_level = [ [33m"[39;49;00m[33mthis[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mthat[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mthe[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mother[39;49;00m[33m"[39;49;00m ]$
   870^I$
   871^I[37m# Ruby directly supports nested arrays[39;49;00m$
   872^Idouble_level = [ [33m"[39;49;00m[33mthis[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mthat[39;49;00m[33m"[39;49;00m, [ [33m"[39;49;00m[33mthe[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mother[39;49;00m[33m"[39;49;00m ] ]$
   873^Istill_single_level = [ [33m"[39;49;00m[33mthis[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mthat[39;49;00m[33m"[39;49;00m, [ [33m"[39;49;00m[33mthe[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mother[39;49;00m[33m"[39;49;00m ] ].flatten$
   874^I$
   875^I$
   876^I[37m# @@PLEAC@@_4.1[39;49;00m$
   877^Ia = [ [33m"[39;49;00m[33mquick[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mbrown[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mfox[39;49;00m[33m"[39;49;00m ]$
   878^Ia = [33m%w([39;49;00m[33mWhy are you teasing me?[39;49;00m[33m)[39;49;00m$
   879^I$
   880^Ilines = <<[33m"[39;49;00m[33mEND_OF_HERE_DOC[39;49;00m[33m"[39;49;00m.gsub([33m/[39;49;00m[33m^[39;49;00m[33m\[39;49;00m[33ms*(.+)[39;49;00m[33m/[39;49;00m, [33m'[39;49;00m[33m\1[39;49;00m[33m'[39;49;00m)$
   881^I[33m    The boy stood on the burning deck,[39;49;00m$
   882^I[33m    It was as hot as glass.[39;49;00m$
   883^I[33mEND_OF_HERE_DOC[39;49;00m$
   884^I$
   885^Ibigarray = [31mIO[39;49;00m.readlines([33m"[39;49;00m[33mmydatafile[39;49;00m[33m"[39;49;00m).collect { |l| l.chomp }$
   886^I$
   887^I[36mname[39;49;00m = [33m"[39;49;00m[33mGandalf[39;49;00m[33m"[39;49;00m$
   888^Ibanner = [33m%Q([39;49;00m[33mSpeak, [39;49;00m[33m#{[39;49;00m[36mname[39;49;00m[33m}[39;49;00m[33m, and welcome![39;49;00m[33m)[39;49;00m$
   889^I$
   890^Ihost_info  = [33m`[39;49;00m[33mhost [39;49;00m[33m#{[39;49;00mhis_host[33m}[39;49;00m[33m`[39;49;00m$
   891^I$
   892^I[33m%x([39;49;00m[33mps [39;49;00m[33m#{[39;49;00m[31m$$[39;49;00m[33m}[39;49;00m[33m)[39;49;00m$
   893^I$
   894^Ibanner = [33m'[39;49;00m[33mCosts only $4.95[39;49;00m[33m'[39;49;00m.split([33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m)$
   895^I$
   896^Irax = [33m%w! ( ) < > { } [ ] ![39;49;00m$
   897^I$
   898^I$
   899^I[37m# @@PLEAC@@_4.2[39;49;00m$
   900^I[34mdef[39;49;00m [32mcommify_series[39;49;00m(arr)$
   901^I    [34mreturn[39;49;00m [33m'[39;49;00m[33m'[39;49;00m [34mif[39;49;00m [35mnot[39;49;00m arr$
   902^I    [34mcase[39;49;00m arr.size$
   903^I        [34mwhen[39;49;00m [34m0[39;49;00m [34mthen[39;49;00m [33m'[39;49;00m[33m'[39;49;00m$
   904^I        [34mwhen[39;49;00m [34m1[39;49;00m [34mthen[39;49;00m arr[[34m0[39;49;00m]$
   905^I        [34mwhen[39;49;00m [34m2[39;49;00m [34mthen[39;49;00m arr.join([33m'[39;49;00m[33m and [39;49;00m[33m'[39;49;00m)$
   906^I        [34melse[39;49;00m arr[[34m0[39;49;00m..-[34m2[39;49;00m].join([33m'[39;49;00m[33m, [39;49;00m[33m'[39;49;00m) + [33m'[39;49;00m[33m, and [39;49;00m[33m'[39;49;00m + arr[-[34m1[39;49;00m]$
   907^I    [34mend[39;49;00m$
   908^I[34mend[39;49;00m$
   909^I$
   910^Iarray = [ [33m"[39;49;00m[33mred[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33myellow[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mgreen[39;49;00m[33m"[39;49;00m ]$
   911^I$
   912^I[36mprint[39;49;00m [33m"[39;49;00m[33mI have [39;49;00m[33m"[39;49;00m, array, [33m"[39;49;00m[33m marbles[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
   913^I[37m# -> I have redyellowgreen marbles[39;49;00m$
   914^I$
   915^I[37m# But unlike Perl:[39;49;00m$
   916^I[36mprint[39;49;00m [33m"[39;49;00m[33mI have [39;49;00m[33m#{[39;49;00marray[33m}[39;49;00m[33m marbles[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
   917^I[37m# -> I have redyellowgreen marbles[39;49;00m$
   918^I[37m# So, needs:[39;49;00m$
   919^I[36mprint[39;49;00m [33m"[39;49;00m[33mI have [39;49;00m[33m#{[39;49;00marray.join([33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m)[33m}[39;49;00m[33m marbles[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
   920^I[37m# -> I have red yellow green marbles[39;49;00m$
   921^I$
   922^I[37m#!/usr/bin/ruby[39;49;00m$
   923^I[37m# communify_series - show proper comma insertion in list output[39;49;00m$
   924^I$
   925^I[34mdef[39;49;00m [32mcommify_series[39;49;00m(arr)$
   926^I    [34mreturn[39;49;00m [33m'[39;49;00m[33m'[39;49;00m [34mif[39;49;00m [35mnot[39;49;00m arr$
   927^I    sepchar = arr.find { |[36mp[39;49;00m| [36mp[39;49;00m =~ [33m/[39;49;00m[33m,[39;49;00m[33m/[39;49;00m } ? [33m'[39;49;00m[33m; [39;49;00m[33m'[39;49;00m : [33m'[39;49;00m[33m, [39;49;00m[33m'[39;49;00m$
   928^I    [34mcase[39;49;00m arr.size$
   929^I        [34mwhen[39;49;00m [34m0[39;49;00m [34mthen[39;49;00m [33m'[39;49;00m[33m'[39;49;00m$
   930^I        [34mwhen[39;49;00m [34m1[39;49;00m [34mthen[39;49;00m arr[[34m0[39;49;00m]$
   931^I        [34mwhen[39;49;00m [34m2[39;49;00m [34mthen[39;49;00m arr.join([33m'[39;49;00m[33m and [39;49;00m[33m'[39;49;00m)$
   932^I        [34melse[39;49;00m arr[[34m0[39;49;00m..-[34m2[39;49;00m].join(sepchar) + sepchar + [33m'[39;49;00m[33mand [39;49;00m[33m'[39;49;00m + arr[-[34m1[39;49;00m]$
   933^I    [34mend[39;49;00m$
   934^I[34mend[39;49;00m$
   935^I$
   936^Ilists = [$
   937^I    [ [33m'[39;49;00m[33mjust one thing[39;49;00m[33m'[39;49;00m ],$
   938^I    [33m%w([39;49;00m[33mMutt Jeff[39;49;00m[33m)[39;49;00m,$
   939^I    [33m%w([39;49;00m[33mPeter Paul Mary[39;49;00m[33m)[39;49;00m,$
   940^I    [ [33m'[39;49;00m[33mTo our parents[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mMother Theresa[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mGod[39;49;00m[33m'[39;49;00m ],$
   941^I    [ [33m'[39;49;00m[33mpastrami[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mham and cheese[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mpeanut butter and jelly[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mtuna[39;49;00m[33m'[39;49;00m ],$
   942^I    [ [33m'[39;49;00m[33mrecycle tired, old phrases[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mponder big, happy thoughts[39;49;00m[33m'[39;49;00m ],$
   943^I    [ [33m'[39;49;00m[33mrecycle tired, old phrases[39;49;00m[33m'[39;49;00m,$
   944^I      [33m'[39;49;00m[33mponder big, happy thoughts[39;49;00m[33m'[39;49;00m,$
   945^I      [33m'[39;49;00m[33msleep and dream peacefully[39;49;00m[33m'[39;49;00m ],$
   946^I]$
   947^I$
   948^I[34mfor[39;49;00m list [34min[39;49;00m lists [34mdo[39;49;00m$
   949^I    [36mputs[39;49;00m [33m"[39;49;00m[33mThe list is: [39;49;00m[33m#{[39;49;00mcommify_series(list)[33m}[39;49;00m[33m.[39;49;00m[33m"[39;49;00m$
   950^I[34mend[39;49;00m$
   951^I$
   952^I$
   953^I[37m# @@PLEAC@@_4.3[39;49;00m$
   954^I[37m#   (note: AFAIK Ruby doesn't allow gory change of Array length)[39;49;00m$
   955^I[37m# grow the array by assigning nil to past the end of array[39;49;00m$
   956^Iary[new_size-[34m1[39;49;00m] = [34mnil[39;49;00m$
   957^I[37m# shrink the array by slicing it down[39;49;00m$
   958^Iary.slice!(new_size..-[34m1[39;49;00m)$
   959^I[37m# init the array with given size[39;49;00m$
   960^I[36mArray[39;49;00m.new(number_of_elems)$
   961^I[37m# assign to an element past the original end enlarges the array[39;49;00m$
   962^Iary[index_new_last_elem] = value$
   963^I$
   964^I[34mdef[39;49;00m [32mwhat_about_that_array[39;49;00m(a)$
   965^I    [36mprint[39;49;00m [33m"[39;49;00m[33mThe array now has [39;49;00m[33m"[39;49;00m, a.size, [33m"[39;49;00m[33m elements.[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
   966^I    [37m# Index of last element is not really interesting in Ruby[39;49;00m$
   967^I    [36mprint[39;49;00m [33m"[39;49;00m[33mElement [39;49;00m[33m#[39;49;00m[33m3 is `[39;49;00m[33m#{[39;49;00ma[[34m3[39;49;00m][33m}[39;49;00m[33m'.[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
   968^I[34mend[39;49;00m$
   969^Ipeople = [33m%w([39;49;00m[33mCrosby Stills Nash Young[39;49;00m[33m)[39;49;00m$
   970^Iwhat_about_that_array(people)$
   971^I$
   972^I$
   973^I[37m# @@PLEAC@@_4.4[39;49;00m$
   974^I[37m# OO style[39;49;00m$
   975^Ibad_users.each { |user|$
   976^I    complain(user)$
   977^I}$
   978^I[37m# or, functional style[39;49;00m$
   979^I[34mfor[39;49;00m user [34min[39;49;00m bad_users$
   980^I    complain(user)$
   981^I[34mend[39;49;00m$
   982^I$
   983^I[34mfor[39;49;00m var [34min[39;49;00m [31mENV[39;49;00m.keys.sort$
   984^I    [36mputs[39;49;00m [33m"[39;49;00m[33m#{[39;49;00mvar[33m}[39;49;00m[33m=[39;49;00m[33m#{[39;49;00m[31mENV[39;49;00m[var][33m}[39;49;00m[33m"[39;49;00m$
   985^I[34mend[39;49;00m$
   986^I$
   987^I[34mfor[39;49;00m user [34min[39;49;00m all_users$
   988^I    disk_space = get_usage(user)$
   989^I    [34mif[39;49;00m (disk_space > [31mMAX_QUOTA[39;49;00m)$
   990^I        complain(user)$
   991^I    [34mend[39;49;00m$
   992^I[34mend[39;49;00m$
   993^I$
   994^I[34mfor[39;49;00m l [34min[39;49;00m [31mIO[39;49;00m.popen([33m"[39;49;00m[33mwho[39;49;00m[33m"[39;49;00m).readlines$
   995^I    [36mprint[39;49;00m l [34mif[39;49;00m l =~ [33m/[39;49;00m[33m^gc[39;49;00m[33m/[39;49;00m $
   996^I[34mend[39;49;00m$
   997^I$
   998^I[37m# we can mimic the obfuscated Perl way[39;49;00m$
   999^I[34mwhile[39;49;00m fh.gets               [37m# $_ is set to the line just read[39;49;00m$
  1000^I    [36mchomp[39;49;00m                   [37m# $_ has a trailing \n removed, if it had one[39;49;00m$
  1001^I    [36msplit[39;49;00m.each { |w|        [37m# $_ is split on whitespace[39;49;00m$
  1002^I                            [37m# but $_ is not set to each chunk as in Perl[39;49;00m$
  1003^I        [36mprint[39;49;00m w.reverse$
  1004^I    }$
  1005^I[34mend[39;49;00m$
  1006^I[37m# ...or use a cleaner way[39;49;00m$
  1007^I[34mfor[39;49;00m l [34min[39;49;00m fh.readlines$
  1008^I    l.chomp.split.each { |w| [36mprint[39;49;00m w.reverse }$
  1009^I[34mend[39;49;00m$
  1010^I$
  1011^I[37m# same drawback as in problem 1.4, we can't mutate a Numeric...[39;49;00m$
  1012^Iarray.collect! { |v| v - [34m1[39;49;00m }$
  1013^I$
  1014^Ia = [ .[34m5[39;49;00m, [34m3[39;49;00m ]; b = [ [34m0[39;49;00m, [34m1[39;49;00m ]$
  1015^I[34mfor[39;49;00m ary [34min[39;49;00m [ a, b ]$
  1016^I    ary.collect! { |v| v * [34m7[39;49;00m }$
  1017^I[34mend[39;49;00m$
  1018^I[36mputs[39;49;00m [33m"[39;49;00m[33m#{[39;49;00ma.join([33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m)[33m}[39;49;00m[33m [39;49;00m[33m#{[39;49;00mb.join([33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m)[33m}[39;49;00m[33m"[39;49;00m$
  1019^I$
  1020^I[37m# we can mutate Strings, cool; we need a trick for the scalar[39;49;00m$
  1021^I[34mfor[39;49;00m ary [34min[39;49;00m [ [ scalar ], array, [36mhash[39;49;00m.values ]$
  1022^I    ary.each { |v| v.strip! }     [37m# String#strip rules :)[39;49;00m$
  1023^I[34mend[39;49;00m$
  1024^I$
  1025^I$
  1026^I[37m# @@PLEAC@@_4.5[39;49;00m$
  1027^I[37m# not relevant in Ruby since we have always references[39;49;00m$
  1028^I[34mfor[39;49;00m item [34min[39;49;00m array$
  1029^I    [37m# do somethingh with item[39;49;00m$
  1030^I[34mend[39;49;00m$
  1031^I$
  1032^I$
  1033^I[37m# @@PLEAC@@_4.6[39;49;00m$
  1034^Iunique = list.uniq$
  1035^I$
  1036^I[37m# generate a list of users logged in, removing duplicates[39;49;00m$
  1037^Iusers = [33m`[39;49;00m[33mwho[39;49;00m[33m`[39;49;00m.collect { |l| l =~ [33m/[39;49;00m[33m([39;49;00m[33m\[39;49;00m[33mw+)[39;49;00m[33m/[39;49;00m; [31m$1[39;49;00m }.sort.uniq$
  1038^I[36mputs[39;49;00m([33m"[39;49;00m[33musers logged in: [39;49;00m[33m#{[39;49;00mcommify_series(users)[33m}[39;49;00m[33m"[39;49;00m)  [37m# see 4.2 for commify_series[39;49;00m$
  1039^I$
  1040^I$
  1041^I[37m# @@PLEAC@@_4.7[39;49;00m$
  1042^Ia - b$
  1043^I[37m# [ 1, 1, 2, 2, 3, 3, 3, 4, 5 ] - [ 1, 2, 4 ]  ->  [3, 5][39;49;00m$
  1044^I$
  1045^I$
  1046^I[37m# @@PLEAC@@_4.8[39;49;00m$
  1047^Iunion = a | b$
  1048^Iintersection = a & b$
  1049^Idifference = a - b$
  1050^I$
  1051^I$
  1052^I[37m# @@PLEAC@@_4.9[39;49;00m$
  1053^Iarray1.concat(array2)$
  1054^I[37m# if you will assign to another object, better use:[39;49;00m$
  1055^Inew_ary = array1 + array2$
  1056^I$
  1057^Imembers = [ [33m"[39;49;00m[33mTime[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mFlies[39;49;00m[33m"[39;49;00m ]$
  1058^Iinitiates =  [ [33m"[39;49;00m[33mAn[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mArrow[39;49;00m[33m"[39;49;00m ]$
  1059^Imembers += initiates$
  1060^I$
  1061^Imembers = [ [33m"[39;49;00m[33mTime[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mFlies[39;49;00m[33m"[39;49;00m ]$
  1062^Iinitiates = [ [33m"[39;49;00m[33mAn[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mArrow[39;49;00m[33m"[39;49;00m ]$
  1063^Imembers[[34m2[39;49;00m,[34m0[39;49;00m] = [ [33m"[39;49;00m[33mLike[39;49;00m[33m"[39;49;00m, initiates ].flatten$
  1064^I$
  1065^Imembers[[34m0[39;49;00m] = [33m"[39;49;00m[33mFruit[39;49;00m[33m"[39;49;00m$
  1066^Imembers[[34m3[39;49;00m,[34m2[39;49;00m] = [33m"[39;49;00m[33mA[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mBanana[39;49;00m[33m"[39;49;00m$
  1067^I$
  1068^I$
  1069^I[37m# @@PLEAC@@_4.10[39;49;00m$
  1070^Ireversed = ary.reverse$
  1071^I$
  1072^Iary.reverse_each { |e|$
  1073^I    [37m# do something with e[39;49;00m$
  1074^I}$
  1075^I$
  1076^Idescending = ary.sort.reverse$
  1077^Idescending = ary.sort { |a,b| b <=> a }$
  1078^I$
  1079^I$
  1080^I[37m# @@PLEAC@@_4.11[39;49;00m$
  1081^I[37m# remove n elements from front of ary (shift n)[39;49;00m$
  1082^Ifront = ary.slice!([34m0[39;49;00m, n)$
  1083^I$
  1084^I[37m# remove n elements from the end of ary (pop n)[39;49;00m$
  1085^Iend_ = ary.slice!(-n .. -[34m1[39;49;00m)$
  1086^I$
  1087^I[37m# let's extend the Array class, to make that useful[39;49;00m$
  1088^I[34mclass[39;49;00m [04m[32mArray[39;49;00m$
  1089^I    [34mdef[39;49;00m [32mshift2[39;49;00m()$
  1090^I        slice!([34m0[39;49;00m .. [34m1[39;49;00m)     [37m# more symetric with pop2...[39;49;00m$
  1091^I    [34mend[39;49;00m$
  1092^I    [34mdef[39;49;00m [32mpop2[39;49;00m()$
  1093^I        slice!(-[34m2[39;49;00m .. -[34m1[39;49;00m)$
  1094^I    [34mend[39;49;00m$
  1095^I[34mend[39;49;00m$
  1096^I$
  1097^Ifriends = [33m%w([39;49;00m[33mPeter Paul Mary Jim Tim[39;49;00m[33m)[39;49;00m$
  1098^Ithis, that = friends.shift2$
  1099^I$
  1100^Ibeverages = [33m%w([39;49;00m[33mDew Jolt Cola Sprite Fresca[39;49;00m[33m)[39;49;00m$
  1101^Ipair = beverages.pop2$
  1102^I$
  1103^I$
  1104^I[37m# @@PLEAC@@_4.12[39;49;00m$
  1105^I[37m# use Enumerable#detect (or the synonym Enumerable#find)[39;49;00m$
  1106^Ihighest_eng = employees.detect { |emp| emp.category == [33m'[39;49;00m[33mengineer[39;49;00m[33m'[39;49;00m }$
  1107^I$
  1108^I$
  1109^I[37m# @@PLEAC@@_4.13[39;49;00m$
  1110^I[37m# use Enumerable#select (or the synonym Enumerable#find_all)[39;49;00m$
  1111^Ibigs = nums.select { |i| i > [34m1_000_000[39;49;00m }$
  1112^Ipigs = users.keys.select { |k| users[k] > [34m1[39;49;00me7 }$
  1113^I$
  1114^Imatching = [33m`[39;49;00m[33mwho[39;49;00m[33m`[39;49;00m.select { |u| u =~ [33m/[39;49;00m[33m^gnat [39;49;00m[33m/[39;49;00m }$
  1115^I$
  1116^Iengineers = employees.select { |e| e.position == [33m'[39;49;00m[33mEngineer[39;49;00m[33m'[39;49;00m }$
  1117^I$
  1118^Isecondary_assistance = applicants.select { |a|$
  1119^I    a.income >= [34m26_000[39;49;00m && a.income < [34m30_000[39;49;00m$
  1120^I}$
  1121^I$
  1122^I$
  1123^I[37m# @@PLEAC@@_4.14[39;49;00m$
  1124^I[37m# normally you would have an array of Numeric (Float or[39;49;00m$
  1125^I[37m# Fixnum or Bignum), so you would use:[39;49;00m$
  1126^Isorted = unsorted.sort$
  1127^I[37m# if you have strings representing Integers or Floats[39;49;00m$
  1128^I[37m# you may specify another sort method:[39;49;00m$
  1129^Isorted = unsorted.sort { |a,b| a.to_f <=> b.to_f }$
  1130^I$
  1131^I[37m# let's use the list of my own PID's[39;49;00m$
  1132^I[33m`[39;49;00m[33mps ux[39;49;00m[33m`[39;49;00m.split([33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m)[[34m1[39;49;00m..-[34m1[39;49;00m].$
  1133^I    [36mselect[39;49;00m { |i| i =~ [33m/[39;49;00m[33m^[39;49;00m[33m#{[39;49;00m[31mENV[39;49;00m[[33m'[39;49;00m[33mUSER[39;49;00m[33m'[39;49;00m][33m}[39;49;00m[33m/[39;49;00m }.$
  1134^I    collect { |i| i.split[[34m1[39;49;00m] }.$
  1135^I    sort { |a,b| a.to_i <=> b.to_i }.each { |i| [36mputs[39;49;00m i }$
  1136^I[36mputs[39;49;00m [33m"[39;49;00m[33mSelect a process ID to kill:[39;49;00m[33m"[39;49;00m$
  1137^Ipid = [36mgets[39;49;00m.chomp$
  1138^I[34mraise[39;49;00m [33m"[39;49;00m[33mExiting ... [39;49;00m[33m\n[39;49;00m[33m"[39;49;00m [34munless[39;49;00m pid && pid =~ [33m/[39;49;00m[33m^[39;49;00m[33m\[39;49;00m[33md+$[39;49;00m[33m/[39;49;00m$
  1139^I[31mProcess[39;49;00m.kill([33m'[39;49;00m[33mTERM[39;49;00m[33m'[39;49;00m, pid.to_i)$
  1140^I[36msleep[39;49;00m [34m2[39;49;00m$
  1141^I[31mProcess[39;49;00m.kill([33m'[39;49;00m[33mKILL[39;49;00m[33m'[39;49;00m, pid.to_i)$
  1142^I$
  1143^Idescending = unsorted.sort { |a,b| b.to_f <=> a.to_f }$
  1144^I$
  1145^I$
  1146^I[37m# @@PLEAC@@_4.15[39;49;00m$
  1147^Iordered = unordered.sort { |a,b| compare(a,b) }$
  1148^I$
  1149^Iprecomputed = unordered.collect { |e| [compute, e] }$
  1150^Iordered_precomputed = precomputed.sort { |a,b| a[[34m0[39;49;00m] <=> b[[34m0[39;49;00m] }$
  1151^Iordered = ordered_precomputed.collect { |e| e[[34m1[39;49;00m] }$
  1152^I$
  1153^Iordered = unordered.collect { |e| [compute, e] }.$
  1154^I    sort { |a,b| a[[34m0[39;49;00m] <=> b[[34m0[39;49;00m] }.$
  1155^I    collect { |e| e[[34m1[39;49;00m] }$
  1156^I$
  1157^I[34mfor[39;49;00m employee [34min[39;49;00m employees.sort { |a,b| a.name <=> b.name }$
  1158^I    [36mprint[39;49;00m employee.name, [33m"[39;49;00m[33m earns [39;49;00m[33m\[39;49;00m[33m$ [39;49;00m[33m"[39;49;00m, employee.salary, [33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
  1159^I[34mend[39;49;00m$
  1160^I$
  1161^I[37m# Beware! `0' is true in Ruby.[39;49;00m$
  1162^I[37m# For chaining comparisons, you may use Numeric#nonzero?, which[39;49;00m$
  1163^I[37m# returns num if num is not zero, nil otherwise[39;49;00m$
  1164^Isorted = employees.sort { |a,b| (a.name <=> b.name).nonzero? || b.age <=> a.age }$
  1165^I$
  1166^Iusers = []$
  1167^I[37m# getpwent is not wrapped in Ruby... let's fallback[39;49;00m$
  1168^I[31mIO[39;49;00m.readlines([33m'[39;49;00m[33m/etc/passwd[39;49;00m[33m'[39;49;00m).each { |u| users << u.split([33m'[39;49;00m[33m:[39;49;00m[33m'[39;49;00m) }$
  1169^Iusers.sort! { |a,b| a[[34m0[39;49;00m] <=> b[[34m0[39;49;00m] }$
  1170^I[34mfor[39;49;00m user [34min[39;49;00m users$
  1171^I    [36mputs[39;49;00m user[[34m0[39;49;00m]$
  1172^I[34mend[39;49;00m$
  1173^I$
  1174^Isorted = names.sort { |a,b| a[[34m1[39;49;00m, [34m1[39;49;00m] <=> b[[34m1[39;49;00m, [34m1[39;49;00m] }$
  1175^Isorted = strings.sort { |a,b| a.length <=> b.length }$
  1176^I$
  1177^I[37m# let's show only the compact version[39;49;00m$
  1178^Iordered = strings.collect { |e| [e.length, e] }.$
  1179^I    sort { |a,b| a[[34m0[39;49;00m] <=> b[[34m0[39;49;00m] }.$
  1180^I    collect { |e| e[[34m1[39;49;00m] }$
  1181^I$
  1182^Iordered = strings.collect { |e| [[33m/[39;49;00m[33m\[39;49;00m[33md+[39;49;00m[33m/[39;49;00m.match(e)[[34m0[39;49;00m].to_i, e] }.$
  1183^I    sort { |a,b| a[[34m0[39;49;00m] <=> b[[34m0[39;49;00m] }.$
  1184^I    collect { |e| e[[34m1[39;49;00m] }$
  1185^I$
  1186^I[36mprint[39;49;00m [33m`[39;49;00m[33mcat /etc/passwd[39;49;00m[33m`[39;49;00m.collect { |e| [e, e.split([33m'[39;49;00m[33m:[39;49;00m[33m'[39;49;00m).indexes([34m3[39;49;00m,[34m2[39;49;00m,[34m0[39;49;00m)].flatten }.$
  1187^I    sort { |a,b| (a[[34m1[39;49;00m] <=> b[[34m1[39;49;00m]).nonzero? || (a[[34m2[39;49;00m] <=> b[[34m2[39;49;00m]).nonzero? || a[[34m3[39;49;00m] <=> b[[34m3[39;49;00m] }.$
  1188^I    collect { |e| e[[34m0[39;49;00m] }$
  1189^I$
  1190^I$
  1191^I[37m# @@PLEAC@@_4.16[39;49;00m$
  1192^Icircular.unshift(circular.pop)        [37m# the last shall be first[39;49;00m$
  1193^Icircular.push(circular.shift)         [37m# and vice versa[39;49;00m$
  1194^I$
  1195^I[34mdef[39;49;00m [32mgrab_and_rotate[39;49;00m(l)$
  1196^I    l.push(ret = l.shift)$
  1197^I    ret$
  1198^I[34mend[39;49;00m$
  1199^I$
  1200^Iprocesses = [[34m1[39;49;00m, [34m2[39;49;00m, [34m3[39;49;00m, [34m4[39;49;00m, [34m5[39;49;00m]$
  1201^I[34mwhile[39;49;00m ([34m1[39;49;00m)$
  1202^I    process = grab_and_rotate(processes)$
  1203^I    [36mputs[39;49;00m [33m"[39;49;00m[33mHandling process [39;49;00m[33m#{[39;49;00mprocess[33m}[39;49;00m[33m"[39;49;00m$
  1204^I    [36msleep[39;49;00m [34m1[39;49;00m$
  1205^I[34mend[39;49;00m$
  1206^I$
  1207^I$
  1208^I[37m# @@PLEAC@@_4.17[39;49;00m$
  1209^I[34mdef[39;49;00m [32mfisher_yates_shuffle[39;49;00m(a)$
  1210^I    (a.size-[34m1[39;49;00m).downto([34m1[39;49;00m) { |i|$
  1211^I        j = [36mrand[39;49;00m(i+[34m1[39;49;00m)$
  1212^I        a[i], a[j] = a[j], a[i] [34mif[39;49;00m i != j$
  1213^I    }$
  1214^I[34mend[39;49;00m$
  1215^I$
  1216^I[34mdef[39;49;00m [32mnaive_shuffle[39;49;00m(a)$
  1217^I    [34mfor[39;49;00m i [34min[39;49;00m [34m0[39;49;00m...a.size$
  1218^I        j = [36mrand[39;49;00m(a.size)$
  1219^I        a[i], a[j] = a[j], a[i]$
  1220^I    [34mend[39;49;00m$
  1221^I[34mend[39;49;00m$

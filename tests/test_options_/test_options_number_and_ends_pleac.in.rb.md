     1	[37m# -*- ruby -*-[39;49;00m$
     2	$
     3	[37m# Local variables:[39;49;00m$
     4	[37m#  indent-tabs-mode: nil[39;49;00m$
     5	[37m#  ruby-indent-level: 4[39;49;00m$
     6	[37m# End:[39;49;00m$
     7	$
     8	[37m# @@PLEAC@@_NAME[39;49;00m$
     9	[37m# @@SKIP@@ Ruby[39;49;00m$
    10	$
    11	[37m# @@PLEAC@@_WEB[39;49;00m$
    12	[37m# @@SKIP@@ http://www.ruby-lang.org[39;49;00m$
    13	$
    14	$
    15	[37m# @@PLEAC@@_1.0[39;49;00m$
    16	string = [33m'[39;49;00m[33m\n[39;49;00m[33m'[39;49;00m                     [37m# two characters, \ and an n[39;49;00m$
    17	string = [33m'[39;49;00m[33mJon [39;49;00m[33m\'[39;49;00m[33mMaddog[39;49;00m[33m\'[39;49;00m[33m Orwant[39;49;00m[33m'[39;49;00m  [37m# literal single quotes[39;49;00m$
    18	$
    19	string = [33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m                     [37m# a "newline" character[39;49;00m$
    20	string = [33m"[39;49;00m[33mJon [39;49;00m[33m\"[39;49;00m[33mMaddog[39;49;00m[33m\"[39;49;00m[33m Orwant[39;49;00m[33m"[39;49;00m  [37m# literal double quotes[39;49;00m$
    21	$
    22	string = [33m%q/Jon 'Maddog' Orwant/[39;49;00m  [37m# literal single quotes[39;49;00m$
    23	$
    24	string = [33m%q[[39;49;00m[33mJon 'Maddog' Orwant[39;49;00m[33m][39;49;00m  [37m# literal single quotes[39;49;00m$
    25	string = [33m%q{[39;49;00m[33mJon 'Maddog' Orwant[39;49;00m[33m}[39;49;00m  [37m# literal single quotes[39;49;00m$
    26	string = [33m%q([39;49;00m[33mJon 'Maddog' Orwant[39;49;00m[33m)[39;49;00m  [37m# literal single quotes[39;49;00m$
    27	string = [33m%q<[39;49;00m[33mJon 'Maddog' Orwant[39;49;00m[33m>[39;49;00m  [37m# literal single quotes[39;49;00m$
    28	$
    29	a = <<[33m"[39;49;00m[33mEOF[39;49;00m[33m"[39;49;00m$
    30	[33mThis is a multiline here document[39;49;00m$
    31	[33mterminated by EOF on a line by itself[39;49;00m$
    32	[33mEOF[39;49;00m$
    33	$
    34	$
    35	[37m# @@PLEAC@@_1.1[39;49;00m$
    36	value = string[offset,count]$
    37	value = string[offset..-[34m1[39;49;00m]$
    38	$
    39	string[offset,count] = newstring$
    40	string[offset..-[34m1[39;49;00m]   = newtail$
    41	$
    42	[37m# in Ruby we can also specify intervals by their two offsets[39;49;00m$
    43	value = string[offset..offs2]$
    44	string[offset..offs2] = newstring$
    45	$
    46	leading, s1, s2, trailing = data.unpack([33m"[39;49;00m[33mA5 x3 A8 A8 A*[39;49;00m[33m"[39;49;00m)$
    47	$
    48	fivers = string.unpack([33m"[39;49;00m[33mA5[39;49;00m[33m"[39;49;00m * (string.length/[34m5[39;49;00m))$
    49	$
    50	chars = string.unpack([33m"[39;49;00m[33mA1[39;49;00m[33m"[39;49;00m * string.length)$
    51	$
    52	string = [33m"[39;49;00m[33mThis is what you have[39;49;00m[33m"[39;49;00m$
    53	[37m#        +012345678901234567890  Indexing forwards  (left to right)[39;49;00m$
    54	[37m#         109876543210987654321- Indexing backwards (right to left)[39;49;00m$
    55	[37m#          note that 0 means 10 or 20, etc. above[39;49;00m$
    56	$
    57	first  = string[[34m0[39;49;00m, [34m1[39;49;00m]       [37m# "T"[39;49;00m$
    58	start  = string[[34m5[39;49;00m, [34m2[39;49;00m]       [37m# "is"[39;49;00m$
    59	rest   = string[[34m13[39;49;00m..-[34m1[39;49;00m]     [37m# "you have"[39;49;00m$
    60	last   = string[-[34m1[39;49;00m, [34m1[39;49;00m]      [37m# "e"[39;49;00m$
    61	end_   = string[-[34m4[39;49;00m..-[34m1[39;49;00m]     [37m# "have"[39;49;00m$
    62	piece  = string[-[34m8[39;49;00m, [34m3[39;49;00m]      [37m# "you"[39;49;00m$
    63	$
    64	string[[34m5[39;49;00m, [34m2[39;49;00m] = [33m"[39;49;00m[33mwasn't[39;49;00m[33m"[39;49;00m     [37m# change "is" to "wasn't"[39;49;00m$
    65	string[-[34m12[39;49;00m..-[34m1[39;49;00m] = [33m"[39;49;00m[33mondrous[39;49;00m[33m"[39;49;00m [37m# "This wasn't wondrous"[39;49;00m$
    66	string[[34m0[39;49;00m, [34m1[39;49;00m] = [33m"[39;49;00m[33m"[39;49;00m           [37m# delete first character[39;49;00m$
    67	string[-[34m10[39;49;00m..-[34m1[39;49;00m]  = [33m"[39;49;00m[33m"[39;49;00m       [37m# delete last 10 characters[39;49;00m$
    68	$
    69	[34mif[39;49;00m string[-[34m10[39;49;00m..-[34m1[39;49;00m] =~ [33m/[39;49;00m[33mpattern[39;49;00m[33m/[39;49;00m$
    70	    [36mputs[39;49;00m [33m"[39;49;00m[33mPattern matches in last 10 characters[39;49;00m[33m"[39;49;00m$
    71	[34mend[39;49;00m$
    72	$
    73	string[[34m0[39;49;00m, [34m5[39;49;00m].gsub!([33m/[39;49;00m[33mis[39;49;00m[33m/[39;49;00m, [33m'[39;49;00m[33mat[39;49;00m[33m'[39;49;00m)$
    74	$
    75	a = [33m"[39;49;00m[33mmake a hat[39;49;00m[33m"[39;49;00m$
    76	a[[34m0[39;49;00m, [34m1[39;49;00m], a[-[34m1[39;49;00m, [34m1[39;49;00m] = a[-[34m1[39;49;00m, [34m1[39;49;00m], a[[34m0[39;49;00m, [34m1[39;49;00m]$
    77	$
    78	a = [33m"[39;49;00m[33mTo be or not to be[39;49;00m[33m"[39;49;00m$
    79	b = a.unpack([33m"[39;49;00m[33mx6 A6[39;49;00m[33m"[39;49;00m)$
    80	$
    81	b, c = a.unpack([33m"[39;49;00m[33mx6 A2 X5 A2[39;49;00m[33m"[39;49;00m)$
    82	[36mputs[39;49;00m [33m"[39;49;00m[33m#{[39;49;00mb[33m}[39;49;00m[33m\n[39;49;00m[33m#{[39;49;00mc[33m}[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
    83	$
    84	[34mdef[39;49;00m [32mcut2fmt[39;49;00m(*args)$
    85	    template = [33m'[39;49;00m[33m'[39;49;00m$
    86	    lastpos  = [34m1[39;49;00m$
    87	    [34mfor[39;49;00m place [34min[39;49;00m args$
    88	        template += [33m"[39;49;00m[33mA[39;49;00m[33m"[39;49;00m + (place - lastpos).to_s + [33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m$
    89	        lastpos   = place$
    90	    [34mend[39;49;00m$
    91	    template += [33m"[39;49;00m[33mA*[39;49;00m[33m"[39;49;00m$
    92	    [34mreturn[39;49;00m template$
    93	[34mend[39;49;00m$
    94	$
    95	fmt = cut2fmt([34m8[39;49;00m, [34m14[39;49;00m, [34m20[39;49;00m, [34m26[39;49;00m, [34m30[39;49;00m)$
    96	$
    97	$
    98	[37m# @@PLEAC@@_1.2[39;49;00m$
    99	[37m# careful! "b is true" doesn't mean "b != 0" (0 is true in Ruby)[39;49;00m$
   100	[37m# thus no problem of "defined" later since only nil is false[39;49;00m$
   101	[37m# the following sets to `c' if `b' is nil or false[39;49;00m$
   102	a = b || c$
   103	$
   104	[37m# if you need Perl's behaviour (setting to `c' if `b' is 0) the most[39;49;00m$
   105	[37m# effective way is to use Numeric#nonzero? (thanks to Dave Thomas!)[39;49;00m$
   106	a = b.nonzero? || c$
   107	$
   108	[37m# you will still want to use defined? in order to test[39;49;00m$
   109	[37m# for scope existence of a given object[39;49;00m$
   110	a = defined?(b) ? b : c$
   111	$
   112	dir = [31mARGV[39;49;00m.shift || [33m"[39;49;00m[33m/tmp[39;49;00m[33m"[39;49;00m$
   113	$
   114	$
   115	[37m# @@PLEAC@@_1.3[39;49;00m$
   116	v1, v2 = v2, v1$
   117	$
   118	alpha, beta, production = [33m%w([39;49;00m[33mJanuary March August[39;49;00m[33m)[39;49;00m$
   119	alpha, beta, production = beta, production, alpha$
   120	$
   121	$
   122	[37m# @@PLEAC@@_1.4[39;49;00m$
   123	num = char[[34m0[39;49;00m]$
   124	char = num.chr$
   125	$
   126	[37m# Ruby also supports having a char from character constant[39;49;00m$
   127	num = [33m?r[39;49;00m$
   128	$
   129	char = [36msprintf[39;49;00m([33m"[39;49;00m[33m%c[39;49;00m[33m"[39;49;00m, num)$
   130	[36mprintf[39;49;00m([33m"[39;49;00m[33mNumber %d is character %c[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m, num, num)$
   131	$
   132	ascii = string.unpack([33m"[39;49;00m[33mC*[39;49;00m[33m"[39;49;00m)$
   133	string = ascii.pack([33m"[39;49;00m[33mC*[39;49;00m[33m"[39;49;00m)$
   134	$
   135	hal = [33m"[39;49;00m[33mHAL[39;49;00m[33m"[39;49;00m$
   136	ascii = hal.unpack([33m"[39;49;00m[33mC*[39;49;00m[33m"[39;49;00m)$
   137	[37m# We can't use Array#each since we can't mutate a Fixnum[39;49;00m$
   138	ascii.collect! { |i|$
   139	    i + [34m1[39;49;00m                         [37m# add one to each ASCII value[39;49;00m$
   140	}                $
   141	ibm = ascii.pack([33m"[39;49;00m[33mC*[39;49;00m[33m"[39;49;00m)$
   142	[36mputs[39;49;00m ibm$
   143	$
   144	$
   145	[37m# @@PLEAC@@_1.5[39;49;00m$
   146	array = string.split([33m'[39;49;00m[33m'[39;49;00m)$
   147	$
   148	array = string.unpack([33m"[39;49;00m[33mC*[39;49;00m[33m"[39;49;00m)$
   149	$
   150	string.scan([33m/[39;49;00m[33m.[39;49;00m[33m/[39;49;00m) { |b|$
   151	    [37m# do something with b[39;49;00m$
   152	}$
   153	$
   154	string = [33m"[39;49;00m[33man apple a day[39;49;00m[33m"[39;49;00m$
   155	[36mprint[39;49;00m [33m"[39;49;00m[33munique chars are: [39;49;00m[33m"[39;49;00m, string.split([33m'[39;49;00m[33m'[39;49;00m).uniq.sort, [33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
   156	$
   157	sum = [34m0[39;49;00m$
   158	[34mfor[39;49;00m ascval [34min[39;49;00m string.unpack([33m"[39;49;00m[33mC*[39;49;00m[33m"[39;49;00m) [37m# or use Array#each for a pure OO style :)[39;49;00m$
   159	    sum += ascval$
   160	[34mend[39;49;00m$
   161	[36mputs[39;49;00m [33m"[39;49;00m[33msum is [39;49;00m[33m#{[39;49;00msum & [34m0xffffffff[39;49;00m[33m}[39;49;00m[33m"[39;49;00m [37m# since Ruby will go Bignum if necessary[39;49;00m$
   162	$
   163	[37m# @@INCLUDE@@ include/ruby/slowcat.rb[39;49;00m$
   164	$
   165	$
   166	[37m# @@PLEAC@@_1.6[39;49;00m$
   167	revbytes = string.reverse$
   168	$
   169	revwords = string.split([33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m).reverse.join([33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m)$
   170	$
   171	revwords = string.split([33m/[39;49;00m[33m([39;49;00m[33m\[39;49;00m[33ms+)[39;49;00m[33m/[39;49;00m).reverse.join$
   172	$
   173	[37m# using the fact that IO is Enumerable, you can directly "select" it[39;49;00m$
   174	long_palindromes = [31mFile[39;49;00m.open([33m"[39;49;00m[33m/usr/share/dict/words[39;49;00m[33m"[39;49;00m).$
   175	    [36mselect[39;49;00m { |w| w.chomp!; w.reverse == w && w.length > [34m5[39;49;00m }$
   176	$
   177	$
   178	[37m# @@PLEAC@@_1.7[39;49;00m$
   179	[34mwhile[39;49;00m string.sub!([33m"[39;49;00m[33m\t[39;49;00m[33m+[39;49;00m[33m"[39;49;00m) { [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m * ([31m$&[39;49;00m.length * [34m8[39;49;00m - [31m$`[39;49;00m.length % [34m8[39;49;00m) }$
   180	[34mend[39;49;00m$
   181	$
   182	$
   183	[37m# @@PLEAC@@_1.8[39;49;00m$
   184	[33m'[39;49;00m[33mYou owe [39;49;00m[33m#{[39;49;00mdebt[33m}[39;49;00m[33m to me[39;49;00m[33m'[39;49;00m.gsub([33m/[39;49;00m[33m\[39;49;00m[33m#{[39;49;00m(\w+)[33m}[39;49;00m[33m/[39;49;00m) { [36meval[39;49;00m([31m$1[39;49;00m) }$
   185	$
   186	rows, cols = [34m24[39;49;00m, [34m80[39;49;00m$
   187	text = [33m%q([39;49;00m[33mI am [39;49;00m[33m#[39;49;00m[33m{rows} high and [39;49;00m[33m#[39;49;00m[33m{cols} long[39;49;00m[33m)[39;49;00m$
   188	text.gsub!([33m/[39;49;00m[33m\[39;49;00m[33m#{[39;49;00m(\w+)[33m}[39;49;00m[33m/[39;49;00m) { [36meval[39;49;00m([33m"[39;49;00m[33m#{[39;49;00m[31m$1[39;49;00m[33m}[39;49;00m[33m"[39;49;00m) }$
   189	[36mputs[39;49;00m text$
   190	$
   191	[33m'[39;49;00m[33mI am 17 years old[39;49;00m[33m'[39;49;00m.gsub([33m/[39;49;00m[33m\[39;49;00m[33md+[39;49;00m[33m/[39;49;00m) { [34m2[39;49;00m * [31m$&[39;49;00m.to_i }$
   192	$
   193	$
   194	[37m# @@PLEAC@@_1.9[39;49;00m$
   195	e = [33m"[39;49;00m[33mbo peep[39;49;00m[33m"[39;49;00m.upcase$
   196	e.downcase!$
   197	e.capitalize!$
   198	$
   199	[33m"[39;49;00m[33mthIS is a loNG liNE[39;49;00m[33m"[39;49;00m.gsub!([33m/[39;49;00m[33m\[39;49;00m[33mw+[39;49;00m[33m/[39;49;00m) { [31m$&[39;49;00m.capitalize }$
   200	$
   201	$
   202	[37m# @@PLEAC@@_1.10[39;49;00m$
   203	[33m"[39;49;00m[33mI have [39;49;00m[33m#{[39;49;00mn+[34m1[39;49;00m[33m}[39;49;00m[33m guanacos.[39;49;00m[33m"[39;49;00m$
   204	[36mprint[39;49;00m [33m"[39;49;00m[33mI have [39;49;00m[33m"[39;49;00m, n+[34m1[39;49;00m, [33m"[39;49;00m[33m guanacos.[39;49;00m[33m"[39;49;00m$
   205	$
   206	$
   207	[37m# @@PLEAC@@_1.11[39;49;00m$
   208	var = <<[33m'[39;49;00m[33mEOF[39;49;00m[33m'[39;49;00m.gsub([33m/[39;49;00m[33m^[39;49;00m[33m\[39;49;00m[33ms+[39;49;00m[33m/[39;49;00m, [33m'[39;49;00m[33m'[39;49;00m)$
   209	[33m    your text[39;49;00m$
   210	[33m    goes here[39;49;00m$
   211	[33mEOF[39;49;00m$
   212	$
   213	$
   214	[37m# @@PLEAC@@_1.12[39;49;00m$
   215	string = [33m"[39;49;00m[33mFolding and splicing is the work of an editor,[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m+$
   216	    [33m"[39;49;00m[33mnot a mere collection of silicon[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m+ $
   217	    [33m"[39;49;00m[33mand[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m+$
   218	    [33m"[39;49;00m[33mmobile electrons![39;49;00m[33m"[39;49;00m$
   219	$
   220	[34mdef[39;49;00m [32mwrap[39;49;00m(str, max_size)$
   221	    all = []$
   222	    line = [33m'[39;49;00m[33m'[39;49;00m$
   223	    [34mfor[39;49;00m l [34min[39;49;00m str.split$
   224	        [34mif[39;49;00m (line+l).length >= max_size$
   225	            all.push(line)$
   226	            line = [33m'[39;49;00m[33m'[39;49;00m$
   227	        [34mend[39;49;00m$
   228	        line += line == [33m'[39;49;00m[33m'[39;49;00m ? l : [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m + l$
   229	    [34mend[39;49;00m$
   230	    all.push(line).join([33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m)$
   231	[34mend[39;49;00m$
   232	$
   233	[36mprint[39;49;00m wrap(string, [34m20[39;49;00m)$
   234	[37m#=> Folding and [39;49;00m$
   235	[37m#=> splicing is the [39;49;00m$
   236	[37m#=> work of an editor, [39;49;00m$
   237	[37m#=> not a mere [39;49;00m$
   238	[37m#=> collection of [39;49;00m$
   239	[37m#=> silicon and mobile [39;49;00m$
   240	[37m#=> electrons![39;49;00m$
   241	$
   242	$
   243	[37m# @@PLEAC@@_1.13[39;49;00m$
   244	string = [33m%q([39;49;00m[33mMom said, "Don't do that."[39;49;00m[33m)[39;49;00m$
   245	string.gsub([33m/[39;49;00m[33m['"][39;49;00m[33m/[39;49;00m) { [33m'[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m+[31m$&[39;49;00m }$
   246	string.gsub([33m/[39;49;00m[33m['"][39;49;00m[33m/[39;49;00m, [33m'[39;49;00m[33m\[39;49;00m[33m&[39;49;00m[33m\[39;49;00m[33m&[39;49;00m[33m'[39;49;00m)$
   247	string.gsub([33m/[39;49;00m[33m[^A-Z][39;49;00m[33m/[39;49;00m) { [33m'[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m+[31m$&[39;49;00m }$
   248	[33m"[39;49;00m[33mis a test![39;49;00m[33m"[39;49;00m.gsub([33m/[39;49;00m[33m\[39;49;00m[33mW[39;49;00m[33m/[39;49;00m) { [33m'[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m+[31m$&[39;49;00m }  [37m# no function like quotemeta?[39;49;00m$
   249	$
   250	$
   251	[37m# @@PLEAC@@_1.14[39;49;00m$
   252	string.strip!$
   253	$
   254	$
   255	[37m# @@PLEAC@@_1.15[39;49;00m$
   256	[34mdef[39;49;00m [32mparse_csv[39;49;00m(text)$
   257	    [34mnew[39;49;00m = text.scan([33m/[39;49;00m[33m"([^[39;49;00m[33m\[39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m]*(?:[39;49;00m[33m\\[39;49;00m[33m.[^[39;49;00m[33m\[39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m]*)*)",?|([^,]+),?|,[39;49;00m[33m/[39;49;00m)$
   258	    [34mnew[39;49;00m << [34mnil[39;49;00m [34mif[39;49;00m text[-[34m1[39;49;00m] == [33m?,[39;49;00m$
   259	    [34mnew[39;49;00m.flatten.compact$
   260	[34mend[39;49;00m  $
   261	$
   262	line = [33m%q<[39;49;00m[33mXYZZY,"","O'Reilly, Inc","Wall, Larry","a [39;49;00m[33m\[39;49;00m[33m"glug[39;49;00m[33m\[39;49;00m[33m" bit,",5,"Error, Core Dumped"[39;49;00m[33m>[39;49;00m$
   263	fields = parse_csv(line)$
   264	fields.each_with_index { |v,i|$
   265	    [36mprint[39;49;00m [33m"[39;49;00m[33m#{[39;49;00mi[33m}[39;49;00m[33m : [39;49;00m[33m#{[39;49;00mv[33m}[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m;$
   266	}$
   267	$
   268	$
   269	[37m# @@PLEAC@@_1.16[39;49;00m$
   270	[37m# Use the soundex.rb Library from Michael Neumann.[39;49;00m$
   271	[37m# http://www.s-direktnet.de/homepages/neumann/rb_prgs/Soundex.rb[39;49;00m$
   272	[36mrequire[39;49;00m [33m'[39;49;00m[33mSoundex[39;49;00m[33m'[39;49;00m$
   273	$
   274	code = [31mText[39;49;00m::[31mSoundex[39;49;00m.soundex(string)$
   275	codes = [31mText[39;49;00m::[31mSoundex[39;49;00m.soundex(array)$
   276	$
   277	[37m# substitution function for getpwent():[39;49;00m$
   278	[37m# returns an array of user entries,[39;49;00m$
   279	[37m# each entry contains the username and the full name[39;49;00m$
   280	[34mdef[39;49;00m [32mlogin_names[39;49;00m$
   281	    result = []$
   282	    [31mFile[39;49;00m.open([33m"[39;49;00m[33m/etc/passwd[39;49;00m[33m"[39;49;00m) { |file|$
   283	        file.each_line { |line|$
   284	            [34mnext[39;49;00m [34mif[39;49;00m line.match([33m/[39;49;00m[33m^[39;49;00m[33m#[39;49;00m[33m/[39;49;00m)$
   285	            cols = line.split([33m"[39;49;00m[33m:[39;49;00m[33m"[39;49;00m)$
   286	            result.push([cols[[34m0[39;49;00m], cols[[34m4[39;49;00m]])$
   287	        }$
   288	    }$
   289	    result$
   290	[34mend[39;49;00m$
   291	$
   292	[36mputs[39;49;00m [33m"[39;49;00m[33mLookup user: [39;49;00m[33m"[39;49;00m$
   293	user = [31mSTDIN[39;49;00m.gets$
   294	user.chomp!$
   295	[36mexit[39;49;00m [34munless[39;49;00m user$
   296	name_code = [31mText[39;49;00m::[31mSoundex[39;49;00m.soundex(user)$
   297	$
   298	splitter = [31mRegexp[39;49;00m.new([33m'[39;49;00m[33m([39;49;00m[33m\[39;49;00m[33mw+)[^,]*[39;49;00m[33m\b[39;49;00m[33m([39;49;00m[33m\[39;49;00m[33mw+)[39;49;00m[33m'[39;49;00m)$
   299	[34mfor[39;49;00m username, fullname [34min[39;49;00m login_names [34mdo[39;49;00m$
   300	    firstname, lastname = splitter.match(fullname)[[34m1[39;49;00m,[34m2[39;49;00m]$
   301	    [34mif[39;49;00m name_code == [31mText[39;49;00m::[31mSoundex[39;49;00m.soundex(username)$
   302	        || name_code == [31mText[39;49;00m::[31mSoundex[39;49;00m.soundex(firstname)$
   303	        || name_code == [31mText[39;49;00m::[31mSoundex[39;49;00m.soundex(lastname)$
   304	    [34mthen[39;49;00m$
   305	        [36mputs[39;49;00m [33m"[39;49;00m[33m#{[39;49;00musername[33m}[39;49;00m[33m: [39;49;00m[33m#{[39;49;00mfirstname[33m}[39;49;00m[33m [39;49;00m[33m#{[39;49;00mlastname[33m}[39;49;00m[33m"[39;49;00m$
   306	    [34mend[39;49;00m$
   307	[34mend[39;49;00m$
   308	$
   309	$
   310	[37m# @@PLEAC@@_1.17[39;49;00m$
   311	[37m# @@INCLUDE@@ include/ruby/fixstyle.rb[39;49;00m$
   312	$
   313	$
   314	[37m# @@PLEAC@@_1.18[39;49;00m$
   315	[37m# @@INCLUDE@@ include/ruby/psgrep.rb[39;49;00m$
   316	$
   317	$
   318	[37m# @@PLEAC@@_2.1[39;49;00m$
   319	[37m# Matz tells that you can use Integer() for strict checked conversion.[39;49;00m$
   320	[36mInteger[39;49;00m([33m"[39;49;00m[33mabc[39;49;00m[33m"[39;49;00m)$
   321	[37m#=> `Integer': invalid value for Integer: "abc" (ArgumentError)[39;49;00m$
   322	[36mInteger[39;49;00m([33m"[39;49;00m[33m567[39;49;00m[33m"[39;49;00m)$
   323	[37m#=> 567[39;49;00m$
   324	$
   325	[37m# You may use Float() for floating point stuff[39;49;00m$
   326	[36mInteger[39;49;00m([33m"[39;49;00m[33m56.7[39;49;00m[33m"[39;49;00m)$
   327	[37m#=> `Integer': invalid value for Integer: "56.7" (ArgumentError)[39;49;00m$
   328	[36mFloat[39;49;00m([33m"[39;49;00m[33m56.7[39;49;00m[33m"[39;49;00m)$
   329	[37m#=> 56.7[39;49;00m$
   330	$
   331	[37m# You may also use a regexp for that[39;49;00m$
   332	[34mif[39;49;00m string =~ [33m/[39;49;00m[33m^[+-]?[39;49;00m[33m\[39;49;00m[33md+$[39;49;00m[33m/[39;49;00m$
   333	    [36mp[39;49;00m [33m'[39;49;00m[33mis an integer[39;49;00m[33m'[39;49;00m$
   334	[34melse[39;49;00m$
   335	    [36mp[39;49;00m [33m'[39;49;00m[33mis not[39;49;00m[33m'[39;49;00m$
   336	[34mend[39;49;00m$
   337	$
   338	[34mif[39;49;00m string =~ [33m/[39;49;00m[33m^-?(?:[39;49;00m[33m\[39;49;00m[33md+(?:[39;49;00m[33m\[39;49;00m[33m.[39;49;00m[33m\[39;49;00m[33md*)?|[39;49;00m[33m\[39;49;00m[33m.[39;49;00m[33m\[39;49;00m[33md+)$[39;49;00m[33m/[39;49;00m$
   339	    [36mp[39;49;00m [33m'[39;49;00m[33mis a decimal number[39;49;00m[33m'[39;49;00m$
   340	[34melse[39;49;00m$
   341	    [36mp[39;49;00m [33m'[39;49;00m[33mis not[39;49;00m[33m'[39;49;00m$
   342	[34mend[39;49;00m$
   343	$
   344	$
   345	[37m# @@PLEAC@@_2.2[39;49;00m$
   346	[37m# equal(num1, num2, accuracy) : returns true if num1 and num2 are[39;49;00m$
   347	[37m#   equal to accuracy number of decimal places[39;49;00m$
   348	[34mdef[39;49;00m [32mequal[39;49;00m(i, j, a)$
   349	    [36msprintf[39;49;00m([33m"[39;49;00m[33m%.[39;49;00m[33m#{[39;49;00ma[33m}[39;49;00m[33mg[39;49;00m[33m"[39;49;00m, i) == [36msprintf[39;49;00m([33m"[39;49;00m[33m%.[39;49;00m[33m#{[39;49;00ma[33m}[39;49;00m[33mg[39;49;00m[33m"[39;49;00m, j)$
   350	[34mend[39;49;00m$
   351	$
   352	wage = [34m536[39;49;00m                        [37m# $5.36/hour[39;49;00m$
   353	week = [34m40[39;49;00m * wage                  [37m# $214.40[39;49;00m$
   354	[36mprintf[39;49;00m([33m"[39;49;00m[33mOne week's wage is: [39;49;00m[33m\[39;49;00m[33m$%.2f[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m, week/[34m100[39;49;00m.[34m0[39;49;00m)$
   355	$
   356	$
   357	[37m# @@PLEAC@@_2.3[39;49;00m$
   358	num.round                         [37m# rounds to integer[39;49;00m$
   359	$
   360	a = [34m0[39;49;00m.[34m255[39;49;00m$
   361	b = [36msprintf[39;49;00m([33m"[39;49;00m[33m%.2f[39;49;00m[33m"[39;49;00m, a)$
   362	[36mprint[39;49;00m  [33m"[39;49;00m[33mUnrounded: [39;49;00m[33m#{[39;49;00ma[33m}[39;49;00m[33m\n[39;49;00m[33mRounded: [39;49;00m[33m#{[39;49;00mb[33m}[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
   363	[36mprintf[39;49;00m [33m"[39;49;00m[33mUnrounded: [39;49;00m[33m#{[39;49;00ma[33m}[39;49;00m[33m\n[39;49;00m[33mRounded: %.2f[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m, a$
   364	$
   365	[36mprint[39;49;00m [33m"[39;49;00m[33mnumber[39;49;00m[33m\t[39;49;00m[33mint[39;49;00m[33m\t[39;49;00m[33mfloor[39;49;00m[33m\t[39;49;00m[33mceil[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
   366	a = [ [34m3[39;49;00m.[34m3[39;49;00m , [34m3[39;49;00m.[34m5[39;49;00m , [34m3[39;49;00m.[34m7[39;49;00m, -[34m3[39;49;00m.[34m3[39;49;00m ]$
   367	[34mfor[39;49;00m n [34min[39;49;00m a$
   368	    [36mprintf[39;49;00m([33m"[39;49;00m[33m% .1f[39;49;00m[33m\t[39;49;00m[33m% .1f[39;49;00m[33m\t[39;49;00m[33m% .1f[39;49;00m[33m\t[39;49;00m[33m% .1f[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m,  [37m# at least I don't fake my output :)[39;49;00m$
   369	           n, n.to_i, n.floor, n.ceil)$
   370	[34mend[39;49;00m$
   371	$
   372	$
   373	[37m# @@PLEAC@@_2.4[39;49;00m$
   374	[34mdef[39;49;00m [32mdec2bin[39;49;00m(n)$
   375	    [n].pack([33m"[39;49;00m[33mN[39;49;00m[33m"[39;49;00m).unpack([33m"[39;49;00m[33mB32[39;49;00m[33m"[39;49;00m)[[34m0[39;49;00m].sub([33m/[39;49;00m[33m^0+(?=[39;49;00m[33m\[39;49;00m[33md)[39;49;00m[33m/[39;49;00m, [33m'[39;49;00m[33m'[39;49;00m)$
   376	[34mend[39;49;00m$
   377	$
   378	[34mdef[39;49;00m [32mbin2dec[39;49;00m(n)$
   379	    [([33m"[39;49;00m[33m0[39;49;00m[33m"[39;49;00m*[34m32[39;49;00m+n.to_s)[-[34m32[39;49;00m..-[34m1[39;49;00m]].pack([33m"[39;49;00m[33mB32[39;49;00m[33m"[39;49;00m).unpack([33m"[39;49;00m[33mN[39;49;00m[33m"[39;49;00m)[[34m0[39;49;00m]$
   380	[34mend[39;49;00m$
   381	$
   382	$
   383	[37m# @@PLEAC@@_2.5[39;49;00m$
   384	[34mfor[39;49;00m i [34min[39;49;00m x .. y$
   385	    [37m# i is set to every integer from x to y, inclusive[39;49;00m$
   386	[34mend[39;49;00m$
   387	$
   388	x.step(y,[34m7[39;49;00m) { |i|$
   389	    [37m# i is set to every integer from x to y, stepsize = 7[39;49;00m$
   390	}$
   391	$
   392	[36mprint[39;49;00m [33m"[39;49;00m[33mInfancy is: [39;49;00m[33m"[39;49;00m$
   393	([34m0[39;49;00m..[34m2[39;49;00m).each { |i|$
   394	    [36mprint[39;49;00m i, [33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m$
   395	}$
   396	[36mprint[39;49;00m [33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
   397	$
   398	$
   399	[37m# @@PLEAC@@_2.6[39;49;00m$
   400	[37m# We can add conversion methods to the Integer class,[39;49;00m$
   401	[37m# this makes a roman number just a representation for normal numbers.[39;49;00m$
   402	[34mclass[39;49;00m [04m[32mInteger[39;49;00m$
   403	    $
   404	    [31m@@romanlist[39;49;00m = [[[33m"[39;49;00m[33mM[39;49;00m[33m"[39;49;00m, [34m1000[39;49;00m],$
   405	                   [[33m"[39;49;00m[33mCM[39;49;00m[33m"[39;49;00m, [34m900[39;49;00m],$
   406	                   [[33m"[39;49;00m[33mD[39;49;00m[33m"[39;49;00m,  [34m500[39;49;00m],$
   407	                   [[33m"[39;49;00m[33mCD[39;49;00m[33m"[39;49;00m, [34m400[39;49;00m],$
   408	                   [[33m"[39;49;00m[33mC[39;49;00m[33m"[39;49;00m,  [34m100[39;49;00m],$
   409	                   [[33m"[39;49;00m[33mXC[39;49;00m[33m"[39;49;00m,  [34m90[39;49;00m],$
   410	                   [[33m"[39;49;00m[33mL[39;49;00m[33m"[39;49;00m,   [34m50[39;49;00m],$
   411	                   [[33m"[39;49;00m[33mXL[39;49;00m[33m"[39;49;00m,  [34m40[39;49;00m],$
   412	                   [[33m"[39;49;00m[33mX[39;49;00m[33m"[39;49;00m,   [34m10[39;49;00m],$
   413	                   [[33m"[39;49;00m[33mIX[39;49;00m[33m"[39;49;00m,   [34m9[39;49;00m],$
   414	                   [[33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m,    [34m5[39;49;00m],$
   415	                   [[33m"[39;49;00m[33mIV[39;49;00m[33m"[39;49;00m,   [34m4[39;49;00m],$
   416	                   [[33m"[39;49;00m[33mI[39;49;00m[33m"[39;49;00m,    [34m1[39;49;00m]]$
   417	    $
   418	    [34mdef[39;49;00m [32mto_roman[39;49;00m$
   419	        remains = [36mself[39;49;00m$
   420	        roman = [33m"[39;49;00m[33m"[39;49;00m$
   421	        [34mfor[39;49;00m sym, num [34min[39;49;00m [31m@@romanlist[39;49;00m$
   422	            [34mwhile[39;49;00m remains >= num$
   423	                remains -= num$
   424	                roman << sym$
   425	            [34mend[39;49;00m$
   426	        [34mend[39;49;00m$
   427	        roman$
   428	    [34mend[39;49;00m$
   429	    $
   430	    [34mdef[39;49;00m [04m[32mInteger[39;49;00m.[32mfrom_roman[39;49;00m(roman)$
   431	        ustr = roman.upcase$
   432	        sum = [34m0[39;49;00m$
   433	        [34mfor[39;49;00m entry [34min[39;49;00m [31m@@romanlist[39;49;00m$
   434	            sym, num = entry[[34m0[39;49;00m], entry[[34m1[39;49;00m]$
   435	            [34mwhile[39;49;00m sym == ustr[[34m0[39;49;00m, sym.length]$
   436	                sum += num$
   437	                ustr.slice!([34m0[39;49;00m, sym.length)$
   438	            [34mend[39;49;00m$
   439	        [34mend[39;49;00m$
   440	        sum$
   441	    [34mend[39;49;00m$
   442	    $
   443	[34mend[39;49;00m$
   444	$
   445	$
   446	roman_fifteen = [34m15[39;49;00m.to_roman$
   447	[36mputs[39;49;00m [33m"[39;49;00m[33mRoman for fifteen is [39;49;00m[33m#{[39;49;00mroman_fifteen[33m}[39;49;00m[33m"[39;49;00m$
   448	i = [36mInteger[39;49;00m.from_roman(roman_fifteen)$
   449	[36mputs[39;49;00m [33m"[39;49;00m[33mConverted back, [39;49;00m[33m#{[39;49;00mroman_fifteen[33m}[39;49;00m[33m is [39;49;00m[33m#{[39;49;00mi[33m}[39;49;00m[33m"[39;49;00m$
   450	$
   451	[37m# check[39;49;00m$
   452	[34mfor[39;49;00m i [34min[39;49;00m ([34m1[39;49;00m..[34m3900[39;49;00m)$
   453	    r = i.to_roman$
   454	    j = [36mInteger[39;49;00m.from_roman(r)$
   455	    [34mif[39;49;00m i != j$
   456	        [36mputs[39;49;00m [33m"[39;49;00m[33merror: [39;49;00m[33m#{[39;49;00mi[33m}[39;49;00m[33m : [39;49;00m[33m#{[39;49;00mr[33m}[39;49;00m[33m - [39;49;00m[33m#{[39;49;00mj[33m}[39;49;00m[33m"[39;49;00m$
   457	    [34mend[39;49;00m$
   458	[34mend[39;49;00m$
   459	$
   460	$
   461	[37m# @@PLEAC@@_2.7[39;49;00m$
   462	random = [36mrand[39;49;00m(y-x+[34m1[39;49;00m)+x$
   463	$
   464	chars = [[33m"[39;49;00m[33mA[39;49;00m[33m"[39;49;00m..[33m"[39;49;00m[33mZ[39;49;00m[33m"[39;49;00m,[33m"[39;49;00m[33ma[39;49;00m[33m"[39;49;00m..[33m"[39;49;00m[33mz[39;49;00m[33m"[39;49;00m,[33m"[39;49;00m[33m0[39;49;00m[33m"[39;49;00m..[33m"[39;49;00m[33m9[39;49;00m[33m"[39;49;00m].collect { |r| r.to_a }.join + [33m%q([39;49;00m[33m!@$%^&*[39;49;00m[33m)[39;49;00m$
   465	password = ([34m1[39;49;00m..[34m8[39;49;00m).collect { chars[[36mrand[39;49;00m(chars.size)] }.pack([33m"[39;49;00m[33mC*[39;49;00m[33m"[39;49;00m)$
   466	$
   467	$
   468	[37m# @@PLEAC@@_2.8[39;49;00m$
   469	[36msrand[39;49;00m        [37m# uses a combination of the time, the process id, and a sequence number[39;49;00m$
   470	[36msrand[39;49;00m(val)   [37m# for repeatable behaviour[39;49;00m$
   471	$
   472	$
   473	[37m# @@PLEAC@@_2.9[39;49;00m$
   474	[37m# from the randomr lib: [39;49;00m$
   475	[37m# http://raa.ruby-lang.org/project/randomr/[39;49;00m$
   476	----> [33mhttp[39;49;00m:[33m/[39;49;00m[33m/[39;49;00mraa.ruby-lang.org/project/randomr/$
   477	$
   478	[36mrequire[39;49;00m [33m'[39;49;00m[33mrandom/mersenne_twister[39;49;00m[33m'[39;49;00m$
   479	mers = [31mRandom[39;49;00m::[31mMersenneTwister[39;49;00m.new [34m123456789[39;49;00m$
   480	[36mputs[39;49;00m mers.rand([34m0[39;49;00m)    [37m# 0.550321932544541[39;49;00m$
   481	[36mputs[39;49;00m mers.rand([34m10[39;49;00m)   [37m# 2[39;49;00m$
   482	$
   483	[37m# using online sources of random data via the realrand package:[39;49;00m$
   484	[37m# http://raa.ruby-lang.org/project/realrand/[39;49;00m$
   485	[37m# **Note**[39;49;00m$
   486	[37m# The following online services are used in this package:[39;49;00m$
   487	[37m#   http://www.random.org - source: atmospheric noise [39;49;00m$
   488	[37m#   http://www.fourmilab.ch/hotbits - source: radioactive decay timings[39;49;00m$
   489	[37m#   http://random.hd.org - source: entropy from local and network noise[39;49;00m$
   490	[37m# Please visit the sites and respect the rules of each service.[39;49;00m$
   491	$
   492	[36mrequire[39;49;00m [33m'[39;49;00m[33mrandom/online[39;49;00m[33m'[39;49;00m$
   493	$
   494	generator1 = [31mRandom[39;49;00m::[31mRandomOrg[39;49;00m.new$
   495	[36mputs[39;49;00m generator1.randbyte([34m5[39;49;00m).join([33m"[39;49;00m[33m,[39;49;00m[33m"[39;49;00m)$
   496	[36mputs[39;49;00m generator1.randnum([34m10[39;49;00m, [34m1[39;49;00m, [34m6[39;49;00m).join([33m"[39;49;00m[33m,[39;49;00m[33m"[39;49;00m)  [37m# Roll dice 10 times.[39;49;00m$
   497	$
   498	generator2 = [31mRandom[39;49;00m::[31mFourmiLab[39;49;00m.new$
   499	[36mputs[39;49;00m generator2.randbyte([34m5[39;49;00m).join([33m"[39;49;00m[33m,[39;49;00m[33m"[39;49;00m)$
   500	[37m# randnum is not supported.[39;49;00m$
   501	$
   502	generator3 = [31mRandom[39;49;00m::[31mEntropyPool[39;49;00m.new$
   503	[36mputs[39;49;00m generator3.randbyte([34m5[39;49;00m).join([33m"[39;49;00m[33m,[39;49;00m[33m"[39;49;00m)$
   504	[37m# randnum is not supported.[39;49;00m$
   505	$
   506	$
   507	[37m# @@PLEAC@@_2.10[39;49;00m$
   508	[34mdef[39;49;00m [32mgaussian_rand[39;49;00m$
   509	    [34mbegin[39;49;00m$
   510	        u1 = [34m2[39;49;00m * [36mrand[39;49;00m() - [34m1[39;49;00m$
   511	        u2 = [34m2[39;49;00m * [36mrand[39;49;00m() - [34m1[39;49;00m$
   512	        w = u1*u1 + u2*u2$
   513	    [34mend[39;49;00m [34mwhile[39;49;00m (w >= [34m1[39;49;00m)$
   514	    w = [31mMath[39;49;00m.sqrt((-[34m2[39;49;00m*[31mMath[39;49;00m.log(w))/w)$
   515	    [ u2*w, u1*w ]$
   516	[34mend[39;49;00m$
   517	$
   518	mean = [34m25[39;49;00m$
   519	sdev = [34m2[39;49;00m$
   520	salary = gaussian_rand[[34m0[39;49;00m] * sdev + mean$
   521	[36mprintf[39;49;00m([33m"[39;49;00m[33mYou have been hired at [39;49;00m[33m\[39;49;00m[33m$%.2f[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m, salary)$
   522	$
   523	$
   524	[37m# @@PLEAC@@_2.11[39;49;00m$
   525	[34mdef[39;49;00m [32mdeg2rad[39;49;00m(d)$
   526	    (d/[34m180[39;49;00m.[34m0[39;49;00m)*[31mMath[39;49;00m::[31mPI[39;49;00m$
   527	[34mend[39;49;00m$
   528	$
   529	[34mdef[39;49;00m [32mrad2deg[39;49;00m(r)$
   530	    (r/[31mMath[39;49;00m::[31mPI[39;49;00m)*[34m180[39;49;00m$
   531	[34mend[39;49;00m$
   532	$
   533	$
   534	[37m# @@PLEAC@@_2.12[39;49;00m$
   535	sin_val = [31mMath[39;49;00m.sin(angle)$
   536	cos_val = [31mMath[39;49;00m.cos(angle)$
   537	tan_val = [31mMath[39;49;00m.tan(angle)$
   538	$
   539	[37m# AFAIK Ruby's Math module doesn't provide acos/asin[39;49;00m$
   540	[37m# While we're at it, let's also define missing hyperbolic functions[39;49;00m$
   541	[34mmodule[39;49;00m [04m[36mMath[39;49;00m$
   542	    [34mdef[39;49;00m [04m[32mMath[39;49;00m.[32masin[39;49;00m(x)$
   543	        atan2(x, sqrt([34m1[39;49;00m - x**[34m2[39;49;00m))$
   544	    [34mend[39;49;00m$
   545	    [34mdef[39;49;00m [04m[32mMath[39;49;00m.[32macos[39;49;00m(x)$
   546	        atan2(sqrt([34m1[39;49;00m - x**[34m2[39;49;00m), x)$
   547	    [34mend[39;49;00m$
   548	    [34mdef[39;49;00m [04m[32mMath[39;49;00m.[32matan[39;49;00m(x)$
   549	        atan2(x, [34m1[39;49;00m)$
   550	    [34mend[39;49;00m$
   551	    [34mdef[39;49;00m [04m[32mMath[39;49;00m.[32msinh[39;49;00m(x)$
   552	        (exp(x) - exp(-x)) / [34m2[39;49;00m$
   553	    [34mend[39;49;00m$
   554	    [34mdef[39;49;00m [04m[32mMath[39;49;00m.[32mcosh[39;49;00m(x)$
   555	        (exp(x) + exp(-x)) / [34m2[39;49;00m$
   556	    [34mend[39;49;00m$
   557	    [34mdef[39;49;00m [04m[32mMath[39;49;00m.[32mtanh[39;49;00m(x)$
   558	        sinh(x) / cosh(x)$
   559	    [34mend[39;49;00m$
   560	[34mend[39;49;00m$
   561	$
   562	[37m# The support for Complex numbers is not built-in[39;49;00m$
   563	y = [31mMath[39;49;00m.acos([34m3[39;49;00m.[34m7[39;49;00m)$
   564	[37m#=> in `sqrt': square root for negative number (ArgumentError)[39;49;00m$
   565	$
   566	[37m# There is an implementation of Complex numbers in 'complex.rb' in current[39;49;00m$
   567	[37m# Ruby distro, but it doesn't support atan2 with complex args, so it doesn't[39;49;00m$
   568	[37m# solve this problem.[39;49;00m$
   569	$
   570	$
   571	[37m# @@PLEAC@@_2.13[39;49;00m$
   572	log_e = [31mMath[39;49;00m.log(val)$
   573	log_10 = [31mMath[39;49;00m.log10(val)$
   574	$
   575	[34mdef[39;49;00m [32mlog_base[39;49;00m(base, val)$
   576	    [31mMath[39;49;00m.log(val)/[31mMath[39;49;00m.log(base)$
   577	[34mend[39;49;00m$
   578	$
   579	answer = log_base([34m10[39;49;00m, [34m10_000[39;49;00m)$
   580	[36mputs[39;49;00m [33m"[39;49;00m[33mlog10(10,000) = [39;49;00m[33m#{[39;49;00manswer[33m}[39;49;00m[33m"[39;49;00m$
   581	$
   582	$
   583	[37m# @@PLEAC@@_2.14[39;49;00m$
   584	[36mrequire[39;49;00m [33m'[39;49;00m[33mmatrix.rb[39;49;00m[33m'[39;49;00m$
   585	$
   586	a = [31mMatrix[39;49;00m[[[34m3[39;49;00m, [34m2[39;49;00m, [34m3[39;49;00m], [[34m5[39;49;00m, [34m9[39;49;00m, [34m8[39;49;00m]]$
   587	b = [31mMatrix[39;49;00m[[[34m4[39;49;00m, [34m7[39;49;00m], [[34m9[39;49;00m, [34m3[39;49;00m], [[34m8[39;49;00m, [34m1[39;49;00m]]$
   588	c = a * b$
   589	$
   590	a.row_size$
   591	a.column_size$
   592	$
   593	c.det$
   594	a.transpose$
   595	$
   596	$
   597	[37m# @@PLEAC@@_2.15[39;49;00m$
   598	[36mrequire[39;49;00m [33m'[39;49;00m[33mcomplex.rb[39;49;00m[33m'[39;49;00m$
   599	[36mrequire[39;49;00m [33m'[39;49;00m[33mrational.rb[39;49;00m[33m'[39;49;00m$
   600	$
   601	a = [31mComplex[39;49;00m([34m3[39;49;00m, [34m5[39;49;00m)              [37m# 3 + 5i[39;49;00m$
   602	b = [31mComplex[39;49;00m([34m2[39;49;00m, -[34m2[39;49;00m)             [37m# 2 - 2i[39;49;00m$
   603	[36mputs[39;49;00m [33m"[39;49;00m[33mc = [39;49;00m[33m#{[39;49;00ma*b[33m}[39;49;00m[33m"[39;49;00m$
   604	$
   605	c = a * b$
   606	d = [34m3[39;49;00m + [34m4[39;49;00m*[31mComplex[39;49;00m::I$
   607	$
   608	[36mprintf[39;49;00m [33m"[39;49;00m[33msqrt([39;49;00m[33m#{[39;49;00md[33m}[39;49;00m[33m) = %s[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m, [31mMath[39;49;00m.sqrt(d)$
   609	$
   610	$
   611	[37m# @@PLEAC@@_2.16[39;49;00m$
   612	number = hexadecimal.hex$
   613	number = octal.oct$
   614	$
   615	[36mprint[39;49;00m [33m"[39;49;00m[33mGimme a number in decimal, octal, or hex: [39;49;00m[33m"[39;49;00m$
   616	num = [36mgets[39;49;00m.chomp$
   617	[36mexit[39;49;00m [34munless[39;49;00m defined?(num)$
   618	num = num.oct [34mif[39;49;00m num =~ [33m/[39;49;00m[33m^0[39;49;00m[33m/[39;49;00m  [37m# does both oct and hex  [39;49;00m$
   619	[36mprintf[39;49;00m [33m"[39;49;00m[33m%d %x %o[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m, num, num, num$
   620	$
   621	[36mprint[39;49;00m [33m"[39;49;00m[33mEnter file permission in octal: [39;49;00m[33m"[39;49;00m$
   622	permissions = [36mgets[39;49;00m.chomp$
   623	[34mraise[39;49;00m [33m"[39;49;00m[33mExiting ...[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m [34munless[39;49;00m defined?(permissions)$
   624	[36mputs[39;49;00m [33m"[39;49;00m[33mThe decimal value is [39;49;00m[33m#{[39;49;00mpermissions.oct[33m}[39;49;00m[33m"[39;49;00m$
   625	$
   626	$
   627	[37m# @@PLEAC@@_2.17[39;49;00m$
   628	[34mdef[39;49;00m [32mcommify[39;49;00m(n)$
   629	    n.to_s =~ [33m/[39;49;00m[33m([^[39;49;00m[33m\[39;49;00m[33m.]*)([39;49;00m[33m\[39;49;00m[33m..*)?[39;49;00m[33m/[39;49;00m$
   630	    int, dec = [31m$1[39;49;00m.reverse, [31m$2[39;49;00m ? [31m$2[39;49;00m : [33m"[39;49;00m[33m"[39;49;00m$
   631	    [34mwhile[39;49;00m int.gsub!([33m/[39;49;00m[33m(,|[39;49;00m[33m\[39;49;00m[33m.|^)([39;49;00m[33m\[39;49;00m[33md{3})([39;49;00m[33m\[39;49;00m[33md)[39;49;00m[33m/[39;49;00m, [33m'[39;49;00m[33m\1[39;49;00m[33m\2[39;49;00m[33m,[39;49;00m[33m\3[39;49;00m[33m'[39;49;00m)$
   632	    [34mend[39;49;00m$
   633	    int.reverse + dec$
   634	[34mend[39;49;00m$
   635	$
   636	$
   637	[37m# @@PLEAC@@_2.18[39;49;00m$
   638	[36mprintf[39;49;00m [33m"[39;49;00m[33mIt took %d hour%s[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m, time, time == [34m1[39;49;00m ? [33m"[39;49;00m[33m"[39;49;00m : [33m"[39;49;00m[33ms[39;49;00m[33m"[39;49;00m$
   639	$
   640	[37m# dunno if an equivalent to Lingua::EN::Inflect exists...[39;49;00m$
   641	$
   642	$
   643	[37m# @@PLEAC@@_2.19[39;49;00m$
   644	[37m#-----------------------------[39;49;00m$
   645	[37m#!/usr/bin/ruby[39;49;00m$
   646	[37m# bigfact - calculating prime factors[39;49;00m$
   647	[34mdef[39;49;00m [32mfactorize[39;49;00m(orig)$
   648	    factors = {}$
   649	    factors.default = [34m0[39;49;00m     [37m# return 0 instead nil if key not found in hash[39;49;00m$
   650	    n = orig$
   651	    i = [34m2[39;49;00m$
   652	    sqi = [34m4[39;49;00m                 [37m# square of i[39;49;00m$
   653	    [34mwhile[39;49;00m sqi <= n [34mdo[39;49;00m$
   654	        [34mwhile[39;49;00m n.modulo(i) == [34m0[39;49;00m [34mdo[39;49;00m$
   655	            n /= i$
   656	            factors[i] += [34m1[39;49;00m$
   657	            [37m# puts "Found factor #{i}"[39;49;00m$
   658	        [34mend[39;49;00m$
   659	        [37m# we take advantage of the fact that (i +1)**2 = i**2 + 2*i +1[39;49;00m$
   660	        sqi += [34m2[39;49;00m * i + [34m1[39;49;00m$
   661	        i += [34m1[39;49;00m$
   662	    [34mend[39;49;00m$
   663	    $
   664	    [34mif[39;49;00m (n != [34m1[39;49;00m) && (n != orig)$
   665	        factors[n] += [34m1[39;49;00m$
   666	    [34mend[39;49;00m$
   667	    factors$
   668	[34mend[39;49;00m$
   669	$
   670	[34mdef[39;49;00m [32mprintfactorhash[39;49;00m(orig, factorcount)$
   671	    [36mprint[39;49;00m [36mformat[39;49;00m([33m"[39;49;00m[33m%-10d [39;49;00m[33m"[39;49;00m, orig)$
   672	    [34mif[39;49;00m factorcount.length == [34m0[39;49;00m$
   673	        [36mprint[39;49;00m [33m"[39;49;00m[33mPRIME[39;49;00m[33m"[39;49;00m$
   674	    [34melse[39;49;00m$
   675	        [37m# sorts after number, because the hash keys are numbers[39;49;00m$
   676	        factorcount.sort.each { |factor,exponent|$
   677	            [36mprint[39;49;00m factor$
   678	            [34mif[39;49;00m exponent > [34m1[39;49;00m$
   679	                [36mprint[39;49;00m [33m"[39;49;00m[33m**[39;49;00m[33m"[39;49;00m, exponent$
   680	            [34mend[39;49;00m$
   681	            [36mprint[39;49;00m [33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m$
   682	        }$
   683	    [34mend[39;49;00m$
   684	    [36mputs[39;49;00m$
   685	[34mend[39;49;00m$
   686	$
   687	[34mfor[39;49;00m arg [34min[39;49;00m [31mARGV[39;49;00m$
   688	    n = arg.to_i$
   689	    mfactors = factorize(n)$
   690	    printfactorhash(n, mfactors)$
   691	[34mend[39;49;00m$
   692	[37m#-----------------------------[39;49;00m$
   693	$
   694	$
   695	[37m# @@PLEAC@@_3.0[39;49;00m$
   696	[36mputs[39;49;00m [31mTime[39;49;00m.now$
   697	$
   698	[36mprint[39;49;00m [33m"[39;49;00m[33mToday is day [39;49;00m[33m"[39;49;00m, [31mTime[39;49;00m.now.yday, [33m"[39;49;00m[33m of the current year.[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
   699	[36mprint[39;49;00m [33m"[39;49;00m[33mToday is day [39;49;00m[33m"[39;49;00m, [31mTime[39;49;00m.now.day, [33m"[39;49;00m[33m of the current month.[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
   700	$
   701	$
   702	[37m# @@PLEAC@@_3.1[39;49;00m$
   703	day, month, year = [31mTime[39;49;00m.now.day, [31mTime[39;49;00m.now.month, [31mTime[39;49;00m.now.year$
   704	[37m# or[39;49;00m$
   705	day, month, year = [31mTime[39;49;00m.now.to_a[[34m3[39;49;00m..[34m5[39;49;00m]$
   706	$
   707	tl = [31mTime[39;49;00m.now.localtime$
   708	[36mprintf[39;49;00m([33m"[39;49;00m[33mThe current date is %04d %02d %02d[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m, tl.year, tl.month, tl.day)$
   709	$
   710	[31mTime[39;49;00m.now.localtime.strftime([33m"[39;49;00m[33m%Y-%m-%d[39;49;00m[33m"[39;49;00m)$
   711	$
   712	$
   713	[37m# @@PLEAC@@_3.2[39;49;00m$
   714	[31mTime[39;49;00m.local(year, month, day, hour, minute, second).tv_sec$
   715	[31mTime[39;49;00m.gm(year, month, day, hour, minute, second).tv_sec$
   716	$
   717	$
   718	[37m# @@PLEAC@@_3.3[39;49;00m$
   719	sec, min, hour, day, month, year, wday, yday, isdst, zone = [31mTime[39;49;00m.at(epoch_secs).to_a$
   720	$
   721	$
   722	[37m# @@PLEAC@@_3.4[39;49;00m$
   723	when_ = now + difference         [37m# now -> Time ; difference -> Numeric (delta in seconds)[39;49;00m$
   724	then_ = now - difference$
   725	$
   726	$
   727	[37m# @@PLEAC@@_3.5[39;49;00m$
   728	bree = [34m361535725[39;49;00m$
   729	nat  =  [34m96201950[39;49;00m$
   730	$
   731	difference = bree - nat$
   732	[36mputs[39;49;00m [33m"[39;49;00m[33mThere were [39;49;00m[33m#{[39;49;00mdifference[33m}[39;49;00m[33m seconds between Nat and Bree[39;49;00m[33m"[39;49;00m$
   733	$
   734	seconds    =  difference % [34m60[39;49;00m$
   735	difference = (difference - seconds) / [34m60[39;49;00m$
   736	minutes    =  difference % [34m60[39;49;00m$
   737	difference = (difference - minutes) / [34m60[39;49;00m$
   738	hours      =  difference % [34m24[39;49;00m$
   739	difference = (difference - hours)   / [34m24[39;49;00m$
   740	days       =  difference % [34m7[39;49;00m$
   741	weeks      = (difference - days)    /  [34m7[39;49;00m$
   742	$
   743	[36mputs[39;49;00m [33m"[39;49;00m[33m([39;49;00m[33m#{[39;49;00mweeks[33m}[39;49;00m[33m weeks, [39;49;00m[33m#{[39;49;00mdays[33m}[39;49;00m[33m days, [39;49;00m[33m#{[39;49;00mhours[33m}[39;49;00m[33m:[39;49;00m[33m#{[39;49;00mminutes[33m}[39;49;00m[33m:[39;49;00m[33m#{[39;49;00mseconds[33m}[39;49;00m[33m)[39;49;00m[33m"[39;49;00m$
   744	$
   745	$
   746	[37m# @@PLEAC@@_3.6[39;49;00m$
   747	monthday, weekday, yearday = date.mday, date.wday, date.yday$
   748	$
   749	[37m# AFAIK the week number is not just a division since week boundaries are on sundays[39;49;00m$
   750	weeknum = d.strftime([33m"[39;49;00m[33m%U[39;49;00m[33m"[39;49;00m).to_i + [34m1[39;49;00m$
   751	$
   752	year  = [34m1981[39;49;00m$
   753	month = [33m"[39;49;00m[33mjun[39;49;00m[33m"[39;49;00m                     [37m# or `6' if you want to emulate a broken language[39;49;00m$
   754	day   = [34m16[39;49;00m$
   755	t = [31mTime[39;49;00m.mktime(year, month, day)$
   756	[36mprint[39;49;00m [33m"[39;49;00m[33m#{[39;49;00mmonth[33m}[39;49;00m[33m/[39;49;00m[33m#{[39;49;00mday[33m}[39;49;00m[33m/[39;49;00m[33m#{[39;49;00myear[33m}[39;49;00m[33m was a [39;49;00m[33m"[39;49;00m, t.strftime([33m"[39;49;00m[33m%A[39;49;00m[33m"[39;49;00m), [33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
   757	$
   758	$
   759	[37m# @@PLEAC@@_3.7[39;49;00m$
   760	yyyy, mm, dd = [31m$1[39;49;00m, [31m$2[39;49;00m, [31m$3[39;49;00m [34mif[39;49;00m [33m"[39;49;00m[33m1998-06-25[39;49;00m[33m"[39;49;00m =~ [33m/[39;49;00m[33m([39;49;00m[33m\[39;49;00m[33md+)-([39;49;00m[33m\[39;49;00m[33md+)-([39;49;00m[33m\[39;49;00m[33md+)[39;49;00m[33m/[39;49;00m$
   761	$
   762	epoch_seconds = [31mTime[39;49;00m.mktime(yyyy, mm, dd).tv_sec$
   763	$
   764	[37m# dunno an equivalent to Date::Manip#ParseDate[39;49;00m$
   765	$
   766	$
   767	[37m# @@PLEAC@@_3.8[39;49;00m$
   768	string = [31mTime[39;49;00m.at(epoch_secs)$
   769	[31mTime[39;49;00m.at([34m1234567890[39;49;00m).gmtime        [37m# gives: Fri Feb 13 23:31:30 UTC 2009[39;49;00m$
   770	$
   771	time = [31mTime[39;49;00m.mktime([34m1973[39;49;00m, [33m"[39;49;00m[33mjan[39;49;00m[33m"[39;49;00m, [34m18[39;49;00m, [34m3[39;49;00m, [34m45[39;49;00m, [34m50[39;49;00m)$
   772	[36mprint[39;49;00m [33m"[39;49;00m[33mIn localtime it gives: [39;49;00m[33m"[39;49;00m, time.localtime, [33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
   773	$
   774	$
   775	[37m# @@PLEAC@@_3.9[39;49;00m$
   776	[37m# Ruby provides micro-seconds in Time object[39;49;00m$
   777	[31mTime[39;49;00m.now.usec$
   778	$
   779	[37m# Ruby gives the seconds in floating format when substracting two Time objects[39;49;00m$
   780	before = [31mTime[39;49;00m.now$
   781	line = [36mgets[39;49;00m$
   782	elapsed = [31mTime[39;49;00m.now - before$
   783	[36mputs[39;49;00m [33m"[39;49;00m[33mYou took [39;49;00m[33m#{[39;49;00melapsed[33m}[39;49;00m[33m seconds.[39;49;00m[33m"[39;49;00m$
   784	$
   785	[37m# On my Celeron-400 with Linux-2.2.19-14mdk, average for three execs are:[39;49;00m$
   786	[37m#   This Ruby version:       average 0.00321 sec[39;49;00m$
   787	[37m#   Cookbook's Perl version: average 0.00981 sec[39;49;00m$
   788	size = [34m500[39;49;00m$
   789	number_of_times = [34m100[39;49;00m$
   790	total_time = [34m0[39;49;00m$
   791	number_of_times.times {$
   792	    [37m# populate array[39;49;00m$
   793	    array = []$
   794	    size.times { array << [36mrand[39;49;00m }$
   795	    [37m# sort it[39;49;00m$
   796	    begin_ = [31mTime[39;49;00m.now$
   797	    array.sort!$
   798	    time = [31mTime[39;49;00m.now - begin_$
   799	    total_time += time$
   800	}$
   801	[36mprintf[39;49;00m [33m"[39;49;00m[33mOn average, sorting %d random numbers takes %.5f seconds[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m,$
   802	    size, (total_time/[36mFloat[39;49;00m(number_of_times))$
   803	$
   804	$
   805	[37m# @@PLEAC@@_3.10[39;49;00m$
   806	[36msleep[39;49;00m([34m0[39;49;00m.[34m005[39;49;00m)                      [37m# Ruby is definitely not as broken as Perl :)[39;49;00m$
   807	[37m# (may be interrupted by sending the process a SIGALRM)[39;49;00m$
   808	$
   809	$
   810	[37m# @@PLEAC@@_3.11[39;49;00m$
   811	[37m#!/usr/bin/ruby -w[39;49;00m$
   812	[37m# hopdelta - feed mail header, produce lines[39;49;00m$
   813	[37m#            showing delay at each hop.[39;49;00m$
   814	[36mrequire[39;49;00m [33m'[39;49;00m[33mtime[39;49;00m[33m'[39;49;00m$
   815	[34mclass[39;49;00m [04m[32mMailHopDelta[39;49;00m$
   816	$
   817	    [34mdef[39;49;00m [32minitialize[39;49;00m(mail)$
   818	        [31m@head[39;49;00m = mail.gsub([33m/[39;49;00m[33m\[39;49;00m[33mn[39;49;00m[33m\[39;49;00m[33ms+[39;49;00m[33m/[39;49;00m,[33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m)$
   819	        [31m@topline[39;49;00m = [33m%w-Sender Recipient Time Delta-[39;49;00m$
   820	        [31m@start_from[39;49;00m = mail.match([33m/[39;49;00m[33m^From.*[39;49;00m[33m\[39;49;00m[33m@([^[39;49;00m[33m\[39;49;00m[33ms>]*)[39;49;00m[33m/[39;49;00m)[[34m1[39;49;00m]$
   821	        [31m@date[39;49;00m = [31mTime[39;49;00m.parse(mail.match([33m/[39;49;00m[33m^Date:[39;49;00m[33m\[39;49;00m[33ms+(.*)[39;49;00m[33m/[39;49;00m)[[34m1[39;49;00m])$
   822	    [34mend[39;49;00m$
   823	$
   824	    [34mdef[39;49;00m [32mout[39;49;00m(line)$
   825	         [33m"[39;49;00m[33m%-20.20s %-20.20s %-20.20s  %s[39;49;00m[33m"[39;49;00m % line$
   826	    [34mend[39;49;00m$
   827	$
   828	    [34mdef[39;49;00m [32mhop_date[39;49;00m(day)$
   829	        day.strftime([33m"[39;49;00m[33m%I:%M:%S %Y/%m/%d[39;49;00m[33m"[39;49;00m)$
   830	    [34mend[39;49;00m$
   831	$
   832	    [34mdef[39;49;00m [32mputs_hops[39;49;00m$
   833	        [36mputs[39;49;00m out([31m@topline[39;49;00m) $
   834	        [36mputs[39;49;00m out([[33m'[39;49;00m[33mStart[39;49;00m[33m'[39;49;00m, [31m@start_from[39;49;00m, hop_date([31m@date[39;49;00m),[33m'[39;49;00m[33m'[39;49;00m])$
   835	        [31m@head[39;49;00m.split([33m/[39;49;00m[33m\[39;49;00m[33mn[39;49;00m[33m/[39;49;00m).reverse.grep([33m/[39;49;00m[33m^Received:[39;49;00m[33m/[39;49;00m).each [34mdo[39;49;00m |hop|$
   836	            hop.gsub!([33m/[39;49;00m[33m\[39;49;00m[33mbon (.*?) (id.*)[39;49;00m[33m/[39;49;00m,[33m'[39;49;00m[33m; [39;49;00m[33m\1[39;49;00m[33m'[39;49;00m)$
   837	            whence = hop.match([33m/[39;49;00m[33m;[39;49;00m[33m\[39;49;00m[33ms+(.*)$[39;49;00m[33m/[39;49;00m)[[34m1[39;49;00m]$
   838	            [34munless[39;49;00m whence$
   839	                [36mwarn[39;49;00m [33m"[39;49;00m[33mBad received line: [39;49;00m[33m#{[39;49;00mhop[33m}[39;49;00m[33m"[39;49;00m$
   840	                [34mnext[39;49;00m$
   841	            [34mend[39;49;00m$
   842	            from = [31m$+[39;49;00m [34mif[39;49;00m hop =~ [33m/[39;49;00m[33mfrom[39;49;00m[33m\[39;49;00m[33ms+([39;49;00m[33m\[39;49;00m[33mS+)|[39;49;00m[33m\[39;49;00m[33m((.*?)[39;49;00m[33m\[39;49;00m[33m)[39;49;00m[33m/[39;49;00m$
   843	            by   = [31m$1[39;49;00m [34mif[39;49;00m hop =~ [33m/[39;49;00m[33mby[39;49;00m[33m\[39;49;00m[33ms+([39;49;00m[33m\[39;49;00m[33mS+[39;49;00m[33m\[39;49;00m[33m.[39;49;00m[33m\[39;49;00m[33mS+)[39;49;00m[33m/[39;49;00m$
   844	            [34mnext[39;49;00m [34munless[39;49;00m now = [31mTime[39;49;00m.parse(whence).localtime$
   845	            delta = now - [31m@date[39;49;00m$
   846	            [36mputs[39;49;00m out([from, by, hop_date(now), hop_time(delta)])$
   847	            [31m@date[39;49;00m = now$
   848	        [34mend[39;49;00m$
   849	    [34mend[39;49;00m$
   850	$
   851	    [34mdef[39;49;00m [32mhop_time[39;49;00m(secs)$
   852	        sign = secs < [34m0[39;49;00m ? -[34m1[39;49;00m : [34m1[39;49;00m$
   853	        days, secs = secs.abs.divmod([34m60[39;49;00m * [34m60[39;49;00m * [34m24[39;49;00m)$
   854	        hours,secs = secs.abs.divmod([34m60[39;49;00m * [34m60[39;49;00m)$
   855	        mins, secs = secs.abs.divmod([34m60[39;49;00m)$
   856	        rtn =  [33m"[39;49;00m[33m%3ds[39;49;00m[33m"[39;49;00m % [secs  * sign]$
   857	        rtn << [33m"[39;49;00m[33m%3dm[39;49;00m[33m"[39;49;00m % [mins  * sign] [34mif[39;49;00m mins  != [34m0[39;49;00m$
   858	        rtn << [33m"[39;49;00m[33m%3dh[39;49;00m[33m"[39;49;00m % [hours * sign] [34mif[39;49;00m hours != [34m0[39;49;00m$
   859	        rtn << [33m"[39;49;00m[33m%3dd[39;49;00m[33m"[39;49;00m % [days  * sign] [34mif[39;49;00m days  != [34m0[39;49;00m $
   860	        rtn$
   861	    [34mend[39;49;00m$
   862	[34mend[39;49;00m$
   863	$
   864	[31m$/[39;49;00m = [33m"[39;49;00m[33m"[39;49;00m$
   865	mail = [31mMailHopDelta[39;49;00m.new([31mARGF[39;49;00m.gets).puts_hops$
   866	$
   867	$
   868	[37m# @@PLEAC@@_4.0[39;49;00m$
   869	single_level = [ [33m"[39;49;00m[33mthis[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mthat[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mthe[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mother[39;49;00m[33m"[39;49;00m ]$
   870	$
   871	[37m# Ruby directly supports nested arrays[39;49;00m$
   872	double_level = [ [33m"[39;49;00m[33mthis[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mthat[39;49;00m[33m"[39;49;00m, [ [33m"[39;49;00m[33mthe[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mother[39;49;00m[33m"[39;49;00m ] ]$
   873	still_single_level = [ [33m"[39;49;00m[33mthis[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mthat[39;49;00m[33m"[39;49;00m, [ [33m"[39;49;00m[33mthe[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mother[39;49;00m[33m"[39;49;00m ] ].flatten$
   874	$
   875	$
   876	[37m# @@PLEAC@@_4.1[39;49;00m$
   877	a = [ [33m"[39;49;00m[33mquick[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mbrown[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mfox[39;49;00m[33m"[39;49;00m ]$
   878	a = [33m%w([39;49;00m[33mWhy are you teasing me?[39;49;00m[33m)[39;49;00m$
   879	$
   880	lines = <<[33m"[39;49;00m[33mEND_OF_HERE_DOC[39;49;00m[33m"[39;49;00m.gsub([33m/[39;49;00m[33m^[39;49;00m[33m\[39;49;00m[33ms*(.+)[39;49;00m[33m/[39;49;00m, [33m'[39;49;00m[33m\1[39;49;00m[33m'[39;49;00m)$
   881	[33m    The boy stood on the burning deck,[39;49;00m$
   882	[33m    It was as hot as glass.[39;49;00m$
   883	[33mEND_OF_HERE_DOC[39;49;00m$
   884	$
   885	bigarray = [31mIO[39;49;00m.readlines([33m"[39;49;00m[33mmydatafile[39;49;00m[33m"[39;49;00m).collect { |l| l.chomp }$
   886	$
   887	[36mname[39;49;00m = [33m"[39;49;00m[33mGandalf[39;49;00m[33m"[39;49;00m$
   888	banner = [33m%Q([39;49;00m[33mSpeak, [39;49;00m[33m#{[39;49;00m[36mname[39;49;00m[33m}[39;49;00m[33m, and welcome![39;49;00m[33m)[39;49;00m$
   889	$
   890	host_info  = [33m`[39;49;00m[33mhost [39;49;00m[33m#{[39;49;00mhis_host[33m}[39;49;00m[33m`[39;49;00m$
   891	$
   892	[33m%x([39;49;00m[33mps [39;49;00m[33m#{[39;49;00m[31m$$[39;49;00m[33m}[39;49;00m[33m)[39;49;00m$
   893	$
   894	banner = [33m'[39;49;00m[33mCosts only $4.95[39;49;00m[33m'[39;49;00m.split([33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m)$
   895	$
   896	rax = [33m%w! ( ) < > { } [ ] ![39;49;00m$
   897	$
   898	$
   899	[37m# @@PLEAC@@_4.2[39;49;00m$
   900	[34mdef[39;49;00m [32mcommify_series[39;49;00m(arr)$
   901	    [34mreturn[39;49;00m [33m'[39;49;00m[33m'[39;49;00m [34mif[39;49;00m [35mnot[39;49;00m arr$
   902	    [34mcase[39;49;00m arr.size$
   903	        [34mwhen[39;49;00m [34m0[39;49;00m [34mthen[39;49;00m [33m'[39;49;00m[33m'[39;49;00m$
   904	        [34mwhen[39;49;00m [34m1[39;49;00m [34mthen[39;49;00m arr[[34m0[39;49;00m]$
   905	        [34mwhen[39;49;00m [34m2[39;49;00m [34mthen[39;49;00m arr.join([33m'[39;49;00m[33m and [39;49;00m[33m'[39;49;00m)$
   906	        [34melse[39;49;00m arr[[34m0[39;49;00m..-[34m2[39;49;00m].join([33m'[39;49;00m[33m, [39;49;00m[33m'[39;49;00m) + [33m'[39;49;00m[33m, and [39;49;00m[33m'[39;49;00m + arr[-[34m1[39;49;00m]$
   907	    [34mend[39;49;00m$
   908	[34mend[39;49;00m$
   909	$
   910	array = [ [33m"[39;49;00m[33mred[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33myellow[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mgreen[39;49;00m[33m"[39;49;00m ]$
   911	$
   912	[36mprint[39;49;00m [33m"[39;49;00m[33mI have [39;49;00m[33m"[39;49;00m, array, [33m"[39;49;00m[33m marbles[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
   913	[37m# -> I have redyellowgreen marbles[39;49;00m$
   914	$
   915	[37m# But unlike Perl:[39;49;00m$
   916	[36mprint[39;49;00m [33m"[39;49;00m[33mI have [39;49;00m[33m#{[39;49;00marray[33m}[39;49;00m[33m marbles[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
   917	[37m# -> I have redyellowgreen marbles[39;49;00m$
   918	[37m# So, needs:[39;49;00m$
   919	[36mprint[39;49;00m [33m"[39;49;00m[33mI have [39;49;00m[33m#{[39;49;00marray.join([33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m)[33m}[39;49;00m[33m marbles[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
   920	[37m# -> I have red yellow green marbles[39;49;00m$
   921	$
   922	[37m#!/usr/bin/ruby[39;49;00m$
   923	[37m# communify_series - show proper comma insertion in list output[39;49;00m$
   924	$
   925	[34mdef[39;49;00m [32mcommify_series[39;49;00m(arr)$
   926	    [34mreturn[39;49;00m [33m'[39;49;00m[33m'[39;49;00m [34mif[39;49;00m [35mnot[39;49;00m arr$
   927	    sepchar = arr.find { |[36mp[39;49;00m| [36mp[39;49;00m =~ [33m/[39;49;00m[33m,[39;49;00m[33m/[39;49;00m } ? [33m'[39;49;00m[33m; [39;49;00m[33m'[39;49;00m : [33m'[39;49;00m[33m, [39;49;00m[33m'[39;49;00m$
   928	    [34mcase[39;49;00m arr.size$
   929	        [34mwhen[39;49;00m [34m0[39;49;00m [34mthen[39;49;00m [33m'[39;49;00m[33m'[39;49;00m$
   930	        [34mwhen[39;49;00m [34m1[39;49;00m [34mthen[39;49;00m arr[[34m0[39;49;00m]$
   931	        [34mwhen[39;49;00m [34m2[39;49;00m [34mthen[39;49;00m arr.join([33m'[39;49;00m[33m and [39;49;00m[33m'[39;49;00m)$
   932	        [34melse[39;49;00m arr[[34m0[39;49;00m..-[34m2[39;49;00m].join(sepchar) + sepchar + [33m'[39;49;00m[33mand [39;49;00m[33m'[39;49;00m + arr[-[34m1[39;49;00m]$
   933	    [34mend[39;49;00m$
   934	[34mend[39;49;00m$
   935	$
   936	lists = [$
   937	    [ [33m'[39;49;00m[33mjust one thing[39;49;00m[33m'[39;49;00m ],$
   938	    [33m%w([39;49;00m[33mMutt Jeff[39;49;00m[33m)[39;49;00m,$
   939	    [33m%w([39;49;00m[33mPeter Paul Mary[39;49;00m[33m)[39;49;00m,$
   940	    [ [33m'[39;49;00m[33mTo our parents[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mMother Theresa[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mGod[39;49;00m[33m'[39;49;00m ],$
   941	    [ [33m'[39;49;00m[33mpastrami[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mham and cheese[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mpeanut butter and jelly[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mtuna[39;49;00m[33m'[39;49;00m ],$
   942	    [ [33m'[39;49;00m[33mrecycle tired, old phrases[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mponder big, happy thoughts[39;49;00m[33m'[39;49;00m ],$
   943	    [ [33m'[39;49;00m[33mrecycle tired, old phrases[39;49;00m[33m'[39;49;00m,$
   944	      [33m'[39;49;00m[33mponder big, happy thoughts[39;49;00m[33m'[39;49;00m,$
   945	      [33m'[39;49;00m[33msleep and dream peacefully[39;49;00m[33m'[39;49;00m ],$
   946	]$
   947	$
   948	[34mfor[39;49;00m list [34min[39;49;00m lists [34mdo[39;49;00m$
   949	    [36mputs[39;49;00m [33m"[39;49;00m[33mThe list is: [39;49;00m[33m#{[39;49;00mcommify_series(list)[33m}[39;49;00m[33m.[39;49;00m[33m"[39;49;00m$
   950	[34mend[39;49;00m$
   951	$
   952	$
   953	[37m# @@PLEAC@@_4.3[39;49;00m$
   954	[37m#   (note: AFAIK Ruby doesn't allow gory change of Array length)[39;49;00m$
   955	[37m# grow the array by assigning nil to past the end of array[39;49;00m$
   956	ary[new_size-[34m1[39;49;00m] = [34mnil[39;49;00m$
   957	[37m# shrink the array by slicing it down[39;49;00m$
   958	ary.slice!(new_size..-[34m1[39;49;00m)$
   959	[37m# init the array with given size[39;49;00m$
   960	[36mArray[39;49;00m.new(number_of_elems)$
   961	[37m# assign to an element past the original end enlarges the array[39;49;00m$
   962	ary[index_new_last_elem] = value$
   963	$
   964	[34mdef[39;49;00m [32mwhat_about_that_array[39;49;00m(a)$
   965	    [36mprint[39;49;00m [33m"[39;49;00m[33mThe array now has [39;49;00m[33m"[39;49;00m, a.size, [33m"[39;49;00m[33m elements.[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
   966	    [37m# Index of last element is not really interesting in Ruby[39;49;00m$
   967	    [36mprint[39;49;00m [33m"[39;49;00m[33mElement [39;49;00m[33m#[39;49;00m[33m3 is `[39;49;00m[33m#{[39;49;00ma[[34m3[39;49;00m][33m}[39;49;00m[33m'.[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
   968	[34mend[39;49;00m$
   969	people = [33m%w([39;49;00m[33mCrosby Stills Nash Young[39;49;00m[33m)[39;49;00m$
   970	what_about_that_array(people)$
   971	$
   972	$
   973	[37m# @@PLEAC@@_4.4[39;49;00m$
   974	[37m# OO style[39;49;00m$
   975	bad_users.each { |user|$
   976	    complain(user)$
   977	}$
   978	[37m# or, functional style[39;49;00m$
   979	[34mfor[39;49;00m user [34min[39;49;00m bad_users$
   980	    complain(user)$
   981	[34mend[39;49;00m$
   982	$
   983	[34mfor[39;49;00m var [34min[39;49;00m [31mENV[39;49;00m.keys.sort$
   984	    [36mputs[39;49;00m [33m"[39;49;00m[33m#{[39;49;00mvar[33m}[39;49;00m[33m=[39;49;00m[33m#{[39;49;00m[31mENV[39;49;00m[var][33m}[39;49;00m[33m"[39;49;00m$
   985	[34mend[39;49;00m$
   986	$
   987	[34mfor[39;49;00m user [34min[39;49;00m all_users$
   988	    disk_space = get_usage(user)$
   989	    [34mif[39;49;00m (disk_space > [31mMAX_QUOTA[39;49;00m)$
   990	        complain(user)$
   991	    [34mend[39;49;00m$
   992	[34mend[39;49;00m$
   993	$
   994	[34mfor[39;49;00m l [34min[39;49;00m [31mIO[39;49;00m.popen([33m"[39;49;00m[33mwho[39;49;00m[33m"[39;49;00m).readlines$
   995	    [36mprint[39;49;00m l [34mif[39;49;00m l =~ [33m/[39;49;00m[33m^gc[39;49;00m[33m/[39;49;00m $
   996	[34mend[39;49;00m$
   997	$
   998	[37m# we can mimic the obfuscated Perl way[39;49;00m$
   999	[34mwhile[39;49;00m fh.gets               [37m# $_ is set to the line just read[39;49;00m$
  1000	    [36mchomp[39;49;00m                   [37m# $_ has a trailing \n removed, if it had one[39;49;00m$
  1001	    [36msplit[39;49;00m.each { |w|        [37m# $_ is split on whitespace[39;49;00m$
  1002	                            [37m# but $_ is not set to each chunk as in Perl[39;49;00m$
  1003	        [36mprint[39;49;00m w.reverse$
  1004	    }$
  1005	[34mend[39;49;00m$
  1006	[37m# ...or use a cleaner way[39;49;00m$
  1007	[34mfor[39;49;00m l [34min[39;49;00m fh.readlines$
  1008	    l.chomp.split.each { |w| [36mprint[39;49;00m w.reverse }$
  1009	[34mend[39;49;00m$
  1010	$
  1011	[37m# same drawback as in problem 1.4, we can't mutate a Numeric...[39;49;00m$
  1012	array.collect! { |v| v - [34m1[39;49;00m }$
  1013	$
  1014	a = [ .[34m5[39;49;00m, [34m3[39;49;00m ]; b = [ [34m0[39;49;00m, [34m1[39;49;00m ]$
  1015	[34mfor[39;49;00m ary [34min[39;49;00m [ a, b ]$
  1016	    ary.collect! { |v| v * [34m7[39;49;00m }$
  1017	[34mend[39;49;00m$
  1018	[36mputs[39;49;00m [33m"[39;49;00m[33m#{[39;49;00ma.join([33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m)[33m}[39;49;00m[33m [39;49;00m[33m#{[39;49;00mb.join([33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m)[33m}[39;49;00m[33m"[39;49;00m$
  1019	$
  1020	[37m# we can mutate Strings, cool; we need a trick for the scalar[39;49;00m$
  1021	[34mfor[39;49;00m ary [34min[39;49;00m [ [ scalar ], array, [36mhash[39;49;00m.values ]$
  1022	    ary.each { |v| v.strip! }     [37m# String#strip rules :)[39;49;00m$
  1023	[34mend[39;49;00m$
  1024	$
  1025	$
  1026	[37m# @@PLEAC@@_4.5[39;49;00m$
  1027	[37m# not relevant in Ruby since we have always references[39;49;00m$
  1028	[34mfor[39;49;00m item [34min[39;49;00m array$
  1029	    [37m# do somethingh with item[39;49;00m$
  1030	[34mend[39;49;00m$
  1031	$
  1032	$
  1033	[37m# @@PLEAC@@_4.6[39;49;00m$
  1034	unique = list.uniq$
  1035	$
  1036	[37m# generate a list of users logged in, removing duplicates[39;49;00m$
  1037	users = [33m`[39;49;00m[33mwho[39;49;00m[33m`[39;49;00m.collect { |l| l =~ [33m/[39;49;00m[33m([39;49;00m[33m\[39;49;00m[33mw+)[39;49;00m[33m/[39;49;00m; [31m$1[39;49;00m }.sort.uniq$
  1038	[36mputs[39;49;00m([33m"[39;49;00m[33musers logged in: [39;49;00m[33m#{[39;49;00mcommify_series(users)[33m}[39;49;00m[33m"[39;49;00m)  [37m# see 4.2 for commify_series[39;49;00m$
  1039	$
  1040	$
  1041	[37m# @@PLEAC@@_4.7[39;49;00m$
  1042	a - b$
  1043	[37m# [ 1, 1, 2, 2, 3, 3, 3, 4, 5 ] - [ 1, 2, 4 ]  ->  [3, 5][39;49;00m$
  1044	$
  1045	$
  1046	[37m# @@PLEAC@@_4.8[39;49;00m$
  1047	union = a | b$
  1048	intersection = a & b$
  1049	difference = a - b$
  1050	$
  1051	$
  1052	[37m# @@PLEAC@@_4.9[39;49;00m$
  1053	array1.concat(array2)$
  1054	[37m# if you will assign to another object, better use:[39;49;00m$
  1055	new_ary = array1 + array2$
  1056	$
  1057	members = [ [33m"[39;49;00m[33mTime[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mFlies[39;49;00m[33m"[39;49;00m ]$
  1058	initiates =  [ [33m"[39;49;00m[33mAn[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mArrow[39;49;00m[33m"[39;49;00m ]$
  1059	members += initiates$
  1060	$
  1061	members = [ [33m"[39;49;00m[33mTime[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mFlies[39;49;00m[33m"[39;49;00m ]$
  1062	initiates = [ [33m"[39;49;00m[33mAn[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mArrow[39;49;00m[33m"[39;49;00m ]$
  1063	members[[34m2[39;49;00m,[34m0[39;49;00m] = [ [33m"[39;49;00m[33mLike[39;49;00m[33m"[39;49;00m, initiates ].flatten$
  1064	$
  1065	members[[34m0[39;49;00m] = [33m"[39;49;00m[33mFruit[39;49;00m[33m"[39;49;00m$
  1066	members[[34m3[39;49;00m,[34m2[39;49;00m] = [33m"[39;49;00m[33mA[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mBanana[39;49;00m[33m"[39;49;00m$
  1067	$
  1068	$
  1069	[37m# @@PLEAC@@_4.10[39;49;00m$
  1070	reversed = ary.reverse$
  1071	$
  1072	ary.reverse_each { |e|$
  1073	    [37m# do something with e[39;49;00m$
  1074	}$
  1075	$
  1076	descending = ary.sort.reverse$
  1077	descending = ary.sort { |a,b| b <=> a }$
  1078	$
  1079	$
  1080	[37m# @@PLEAC@@_4.11[39;49;00m$
  1081	[37m# remove n elements from front of ary (shift n)[39;49;00m$
  1082	front = ary.slice!([34m0[39;49;00m, n)$
  1083	$
  1084	[37m# remove n elements from the end of ary (pop n)[39;49;00m$
  1085	end_ = ary.slice!(-n .. -[34m1[39;49;00m)$
  1086	$
  1087	[37m# let's extend the Array class, to make that useful[39;49;00m$
  1088	[34mclass[39;49;00m [04m[32mArray[39;49;00m$
  1089	    [34mdef[39;49;00m [32mshift2[39;49;00m()$
  1090	        slice!([34m0[39;49;00m .. [34m1[39;49;00m)     [37m# more symetric with pop2...[39;49;00m$
  1091	    [34mend[39;49;00m$
  1092	    [34mdef[39;49;00m [32mpop2[39;49;00m()$
  1093	        slice!(-[34m2[39;49;00m .. -[34m1[39;49;00m)$
  1094	    [34mend[39;49;00m$
  1095	[34mend[39;49;00m$
  1096	$
  1097	friends = [33m%w([39;49;00m[33mPeter Paul Mary Jim Tim[39;49;00m[33m)[39;49;00m$
  1098	this, that = friends.shift2$
  1099	$
  1100	beverages = [33m%w([39;49;00m[33mDew Jolt Cola Sprite Fresca[39;49;00m[33m)[39;49;00m$
  1101	pair = beverages.pop2$
  1102	$
  1103	$
  1104	[37m# @@PLEAC@@_4.12[39;49;00m$
  1105	[37m# use Enumerable#detect (or the synonym Enumerable#find)[39;49;00m$
  1106	highest_eng = employees.detect { |emp| emp.category == [33m'[39;49;00m[33mengineer[39;49;00m[33m'[39;49;00m }$
  1107	$
  1108	$
  1109	[37m# @@PLEAC@@_4.13[39;49;00m$
  1110	[37m# use Enumerable#select (or the synonym Enumerable#find_all)[39;49;00m$
  1111	bigs = nums.select { |i| i > [34m1_000_000[39;49;00m }$
  1112	pigs = users.keys.select { |k| users[k] > [34m1[39;49;00me7 }$
  1113	$
  1114	matching = [33m`[39;49;00m[33mwho[39;49;00m[33m`[39;49;00m.select { |u| u =~ [33m/[39;49;00m[33m^gnat [39;49;00m[33m/[39;49;00m }$
  1115	$
  1116	engineers = employees.select { |e| e.position == [33m'[39;49;00m[33mEngineer[39;49;00m[33m'[39;49;00m }$
  1117	$
  1118	secondary_assistance = applicants.select { |a|$
  1119	    a.income >= [34m26_000[39;49;00m && a.income < [34m30_000[39;49;00m$
  1120	}$
  1121	$
  1122	$
  1123	[37m# @@PLEAC@@_4.14[39;49;00m$
  1124	[37m# normally you would have an array of Numeric (Float or[39;49;00m$
  1125	[37m# Fixnum or Bignum), so you would use:[39;49;00m$
  1126	sorted = unsorted.sort$
  1127	[37m# if you have strings representing Integers or Floats[39;49;00m$
  1128	[37m# you may specify another sort method:[39;49;00m$
  1129	sorted = unsorted.sort { |a,b| a.to_f <=> b.to_f }$
  1130	$
  1131	[37m# let's use the list of my own PID's[39;49;00m$
  1132	[33m`[39;49;00m[33mps ux[39;49;00m[33m`[39;49;00m.split([33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m)[[34m1[39;49;00m..-[34m1[39;49;00m].$
  1133	    [36mselect[39;49;00m { |i| i =~ [33m/[39;49;00m[33m^[39;49;00m[33m#{[39;49;00m[31mENV[39;49;00m[[33m'[39;49;00m[33mUSER[39;49;00m[33m'[39;49;00m][33m}[39;49;00m[33m/[39;49;00m }.$
  1134	    collect { |i| i.split[[34m1[39;49;00m] }.$
  1135	    sort { |a,b| a.to_i <=> b.to_i }.each { |i| [36mputs[39;49;00m i }$
  1136	[36mputs[39;49;00m [33m"[39;49;00m[33mSelect a process ID to kill:[39;49;00m[33m"[39;49;00m$
  1137	pid = [36mgets[39;49;00m.chomp$
  1138	[34mraise[39;49;00m [33m"[39;49;00m[33mExiting ... [39;49;00m[33m\n[39;49;00m[33m"[39;49;00m [34munless[39;49;00m pid && pid =~ [33m/[39;49;00m[33m^[39;49;00m[33m\[39;49;00m[33md+$[39;49;00m[33m/[39;49;00m$
  1139	[31mProcess[39;49;00m.kill([33m'[39;49;00m[33mTERM[39;49;00m[33m'[39;49;00m, pid.to_i)$
  1140	[36msleep[39;49;00m [34m2[39;49;00m$
  1141	[31mProcess[39;49;00m.kill([33m'[39;49;00m[33mKILL[39;49;00m[33m'[39;49;00m, pid.to_i)$
  1142	$
  1143	descending = unsorted.sort { |a,b| b.to_f <=> a.to_f }$
  1144	$
  1145	$
  1146	[37m# @@PLEAC@@_4.15[39;49;00m$
  1147	ordered = unordered.sort { |a,b| compare(a,b) }$
  1148	$
  1149	precomputed = unordered.collect { |e| [compute, e] }$
  1150	ordered_precomputed = precomputed.sort { |a,b| a[[34m0[39;49;00m] <=> b[[34m0[39;49;00m] }$
  1151	ordered = ordered_precomputed.collect { |e| e[[34m1[39;49;00m] }$
  1152	$
  1153	ordered = unordered.collect { |e| [compute, e] }.$
  1154	    sort { |a,b| a[[34m0[39;49;00m] <=> b[[34m0[39;49;00m] }.$
  1155	    collect { |e| e[[34m1[39;49;00m] }$
  1156	$
  1157	[34mfor[39;49;00m employee [34min[39;49;00m employees.sort { |a,b| a.name <=> b.name }$
  1158	    [36mprint[39;49;00m employee.name, [33m"[39;49;00m[33m earns [39;49;00m[33m\[39;49;00m[33m$ [39;49;00m[33m"[39;49;00m, employee.salary, [33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
  1159	[34mend[39;49;00m$
  1160	$
  1161	[37m# Beware! `0' is true in Ruby.[39;49;00m$
  1162	[37m# For chaining comparisons, you may use Numeric#nonzero?, which[39;49;00m$
  1163	[37m# returns num if num is not zero, nil otherwise[39;49;00m$
  1164	sorted = employees.sort { |a,b| (a.name <=> b.name).nonzero? || b.age <=> a.age }$
  1165	$
  1166	users = []$
  1167	[37m# getpwent is not wrapped in Ruby... let's fallback[39;49;00m$
  1168	[31mIO[39;49;00m.readlines([33m'[39;49;00m[33m/etc/passwd[39;49;00m[33m'[39;49;00m).each { |u| users << u.split([33m'[39;49;00m[33m:[39;49;00m[33m'[39;49;00m) }$
  1169	users.sort! { |a,b| a[[34m0[39;49;00m] <=> b[[34m0[39;49;00m] }$
  1170	[34mfor[39;49;00m user [34min[39;49;00m users$
  1171	    [36mputs[39;49;00m user[[34m0[39;49;00m]$
  1172	[34mend[39;49;00m$
  1173	$
  1174	sorted = names.sort { |a,b| a[[34m1[39;49;00m, [34m1[39;49;00m] <=> b[[34m1[39;49;00m, [34m1[39;49;00m] }$
  1175	sorted = strings.sort { |a,b| a.length <=> b.length }$
  1176	$
  1177	[37m# let's show only the compact version[39;49;00m$
  1178	ordered = strings.collect { |e| [e.length, e] }.$
  1179	    sort { |a,b| a[[34m0[39;49;00m] <=> b[[34m0[39;49;00m] }.$
  1180	    collect { |e| e[[34m1[39;49;00m] }$
  1181	$
  1182	ordered = strings.collect { |e| [[33m/[39;49;00m[33m\[39;49;00m[33md+[39;49;00m[33m/[39;49;00m.match(e)[[34m0[39;49;00m].to_i, e] }.$
  1183	    sort { |a,b| a[[34m0[39;49;00m] <=> b[[34m0[39;49;00m] }.$
  1184	    collect { |e| e[[34m1[39;49;00m] }$
  1185	$
  1186	[36mprint[39;49;00m [33m`[39;49;00m[33mcat /etc/passwd[39;49;00m[33m`[39;49;00m.collect { |e| [e, e.split([33m'[39;49;00m[33m:[39;49;00m[33m'[39;49;00m).indexes([34m3[39;49;00m,[34m2[39;49;00m,[34m0[39;49;00m)].flatten }.$
  1187	    sort { |a,b| (a[[34m1[39;49;00m] <=> b[[34m1[39;49;00m]).nonzero? || (a[[34m2[39;49;00m] <=> b[[34m2[39;49;00m]).nonzero? || a[[34m3[39;49;00m] <=> b[[34m3[39;49;00m] }.$
  1188	    collect { |e| e[[34m0[39;49;00m] }$
  1189	$
  1190	$
  1191	[37m# @@PLEAC@@_4.16[39;49;00m$
  1192	circular.unshift(circular.pop)        [37m# the last shall be first[39;49;00m$
  1193	circular.push(circular.shift)         [37m# and vice versa[39;49;00m$
  1194	$
  1195	[34mdef[39;49;00m [32mgrab_and_rotate[39;49;00m(l)$
  1196	    l.push(ret = l.shift)$
  1197	    ret$
  1198	[34mend[39;49;00m$
  1199	$
  1200	processes = [[34m1[39;49;00m, [34m2[39;49;00m, [34m3[39;49;00m, [34m4[39;49;00m, [34m5[39;49;00m]$
  1201	[34mwhile[39;49;00m ([34m1[39;49;00m)$
  1202	    process = grab_and_rotate(processes)$
  1203	    [36mputs[39;49;00m [33m"[39;49;00m[33mHandling process [39;49;00m[33m#{[39;49;00mprocess[33m}[39;49;00m[33m"[39;49;00m$
  1204	    [36msleep[39;49;00m [34m1[39;49;00m$
  1205	[34mend[39;49;00m$
  1206	$
  1207	$
  1208	[37m# @@PLEAC@@_4.17[39;49;00m$
  1209	[34mdef[39;49;00m [32mfisher_yates_shuffle[39;49;00m(a)$
  1210	    (a.size-[34m1[39;49;00m).downto([34m1[39;49;00m) { |i|$
  1211	        j = [36mrand[39;49;00m(i+[34m1[39;49;00m)$
  1212	        a[i], a[j] = a[j], a[i] [34mif[39;49;00m i != j$
  1213	    }$
  1214	[34mend[39;49;00m$
  1215	$
  1216	[34mdef[39;49;00m [32mnaive_shuffle[39;49;00m(a)$
  1217	    [34mfor[39;49;00m i [34min[39;49;00m [34m0[39;49;00m...a.size$
  1218	        j = [36mrand[39;49;00m(a.size)$
  1219	        a[i], a[j] = a[j], a[i]$
  1220	    [34mend[39;49;00m$
  1221	[34mend[39;49;00m$

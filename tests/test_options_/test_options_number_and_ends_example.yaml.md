     1	[37m#[39;49;00m[37m[39;49;00m$
     2	[37m# Regression tests[39;49;00m[37m[39;49;00m$
     3	[37m#[39;49;00m[37m[39;49;00m$
     4	[37m[39;49;00m$
     5	[94m%TAG[39;49;00m[37m [39;49;00m[36m![39;49;00m[37m [39;49;00m[36mtag:example.com:foo/[39;49;00m[37m[39;49;00m$
     6	[04m[36m---[39;49;00m[37m[39;49;00m$
     7	[94mtest[39;49;00m:[37m [39;49;00m[36m!foo/bar[39;49;00m[37m [39;49;00m{[94ma[39;49;00m:[37m [39;49;00m[33m'[39;49;00m[33masdf[39;49;00m[33m'[39;49;00m}[37m[39;49;00m$
     8	[94mtest2[39;49;00m:[37m [39;49;00mfred[37m[39;49;00m$
     9	[04m[36m...[39;49;00m[37m[39;49;00m$
    10	[37m[39;49;00m$
    11	[37m#[39;49;00m[37m[39;49;00m$
    12	[37m# Examples from the Preview section of the YAML specification[39;49;00m[37m[39;49;00m$
    13	[37m# (http://yaml.org/spec/1.2/#Preview)[39;49;00m[37m[39;49;00m$
    14	[37m#[39;49;00m[37m[39;49;00m$
    15	[37m[39;49;00m$
    16	[37m# Sequence of scalars[39;49;00m[37m[39;49;00m$
    17	[04m[36m---[39;49;00m[37m[39;49;00m$
    18	-[37m [39;49;00mMark McGwire[37m[39;49;00m$
    19	-[37m [39;49;00mSammy Sosa[37m[39;49;00m$
    20	-[37m [39;49;00mKen Griffey[37m[39;49;00m$
    21	[37m[39;49;00m$
    22	[37m# Mapping scalars to scalars[39;49;00m[37m[39;49;00m$
    23	[04m[36m---[39;49;00m[37m[39;49;00m$
    24	[94mhr[39;49;00m:[37m  [39;49;00m65[37m    [39;49;00m[37m# Home runs[39;49;00m[37m[39;49;00m$
    25	[94mavg[39;49;00m:[37m [39;49;00m0.278[37m [39;49;00m[37m# Batting average[39;49;00m[37m[39;49;00m$
    26	[94mrbi[39;49;00m:[37m [39;49;00m147[37m   [39;49;00m[37m# Runs Batted In[39;49;00m[37m[39;49;00m$
    27	[37m[39;49;00m$
    28	[37m# Mapping scalars to sequences[39;49;00m[37m[39;49;00m$
    29	[04m[36m---[39;49;00m[37m[39;49;00m$
    30	[94mamerican[39;49;00m:[37m[39;49;00m$
    31	[37m  [39;49;00m-[37m [39;49;00mBoston Red Sox[37m[39;49;00m$
    32	[37m  [39;49;00m-[37m [39;49;00mDetroit Tigers[37m[39;49;00m$
    33	[37m  [39;49;00m-[37m [39;49;00mNew York Yankees[37m[39;49;00m$
    34	[94mnational[39;49;00m:[37m[39;49;00m$
    35	[37m  [39;49;00m-[37m [39;49;00mNew York Mets[37m[39;49;00m$
    36	[37m  [39;49;00m-[37m [39;49;00mChicago Cubs[37m[39;49;00m$
    37	[37m  [39;49;00m-[37m [39;49;00mAtlanta Braves[37m[39;49;00m$
    38	[37m[39;49;00m$
    39	[37m# Sequence of mappings[39;49;00m[37m[39;49;00m$
    40	[04m[36m---[39;49;00m[37m[39;49;00m$
    41	-[37m[39;49;00m$
    42	[37m  [39;49;00m[94mname[39;49;00m:[37m [39;49;00mMark McGwire[37m[39;49;00m$
    43	[37m  [39;49;00m[94mhr[39;49;00m:[37m   [39;49;00m65[37m[39;49;00m$
    44	[37m  [39;49;00m[94mavg[39;49;00m:[37m  [39;49;00m0.278[37m[39;49;00m$
    45	-[37m[39;49;00m$
    46	[37m  [39;49;00m[94mname[39;49;00m:[37m [39;49;00mSammy Sosa[37m[39;49;00m$
    47	[37m  [39;49;00m[94mhr[39;49;00m:[37m   [39;49;00m63[37m[39;49;00m$
    48	[37m  [39;49;00m[94mavg[39;49;00m:[37m  [39;49;00m0.288[37m[39;49;00m$
    49	[37m[39;49;00m$
    50	[37m# Sequence of sequences[39;49;00m[37m[39;49;00m$
    51	[04m[36m---[39;49;00m[37m[39;49;00m$
    52	-[37m [39;49;00m[[31mname[39;49;00m[37m        [39;49;00m,[37m [39;49;00m[31mhr[39;49;00m,[37m [39;49;00m[31mavg[39;49;00m[37m  [39;49;00m][37m[39;49;00m$
    53	-[37m [39;49;00m[[31mMark[39;49;00m[31m [39;49;00m[31mMcGwire[39;49;00m,[37m [39;49;00m[31m65[39;49;00m,[37m [39;49;00m[31m0.278[39;49;00m][37m[39;49;00m$
    54	-[37m [39;49;00m[[31mSammy[39;49;00m[31m [39;49;00m[31mSosa[39;49;00m[37m  [39;49;00m,[37m [39;49;00m[31m63[39;49;00m,[37m [39;49;00m[31m0.288[39;49;00m][37m[39;49;00m$
    55	[37m[39;49;00m$
    56	[37m# Mapping of mappings[39;49;00m[37m[39;49;00m$
    57	[04m[36m---[39;49;00m[37m[39;49;00m$
    58	[94mMark McGwire[39;49;00m:[37m [39;49;00m{[94mhr[39;49;00m:[37m [39;49;00m[31m65[39;49;00m,[94m avg[39;49;00m:[37m [39;49;00m[31m0.278[39;49;00m}[37m[39;49;00m$
    59	[94mSammy Sosa[39;49;00m:[37m [39;49;00m{[37m[39;49;00m$
    60	[94m    hr[39;49;00m:[37m [39;49;00m[31m63[39;49;00m,[37m[39;49;00m$
    61	[94m    avg[39;49;00m:[37m [39;49;00m[31m0.288[39;49;00m[37m[39;49;00m$
    62	[37m  [39;49;00m}[37m[39;49;00m$
    63	[37m[39;49;00m$
    64	[37m# Two documents in a stream[39;49;00m[37m[39;49;00m$
    65	[04m[36m---[39;49;00m[37m [39;49;00m[37m# Ranking of 1998 home runs[39;49;00m[37m[39;49;00m$
    66	-[37m [39;49;00mMark McGwire[37m[39;49;00m$
    67	-[37m [39;49;00mSammy Sosa[37m[39;49;00m$
    68	-[37m [39;49;00mKen Griffey[37m[39;49;00m$
    69	[04m[36m---[39;49;00m[37m [39;49;00m[37m# Team ranking[39;49;00m[37m[39;49;00m$
    70	-[37m [39;49;00mChicago Cubs[37m[39;49;00m$
    71	-[37m [39;49;00mSt Louis Cardinals[37m[39;49;00m$
    72	[37m[39;49;00m$
    73	[37m# Documents with the end indicator[39;49;00m[37m[39;49;00m$
    74	[04m[36m---[39;49;00m[37m[39;49;00m$
    75	[94mtime[39;49;00m:[37m [39;49;00m20:03:20[37m[39;49;00m$
    76	[94mplayer[39;49;00m:[37m [39;49;00mSammy Sosa[37m[39;49;00m$
    77	[94maction[39;49;00m:[37m [39;49;00mstrike (miss)[37m[39;49;00m$
    78	[04m[36m...[39;49;00m[37m[39;49;00m$
    79	[04m[36m---[39;49;00m[37m[39;49;00m$
    80	[94mtime[39;49;00m:[37m [39;49;00m20:03:47[37m[39;49;00m$
    81	[94mplayer[39;49;00m:[37m [39;49;00mSammy Sosa[37m[39;49;00m$
    82	[94maction[39;49;00m:[37m [39;49;00mgrand slam[37m[39;49;00m$
    83	[04m[36m...[39;49;00m[37m[39;49;00m$
    84	[37m[39;49;00m$
    85	[37m# Comments[39;49;00m[37m[39;49;00m$
    86	[04m[36m---[39;49;00m[37m[39;49;00m$
    87	[94mhr[39;49;00m:[37m [39;49;00m[37m# 1998 hr ranking[39;49;00m[37m[39;49;00m$
    88	[37m  [39;49;00m-[37m [39;49;00mMark McGwire[37m[39;49;00m$
    89	[37m  [39;49;00m-[37m [39;49;00mSammy Sosa[37m[39;49;00m$
    90	[94mrbi[39;49;00m:[37m[39;49;00m$
    91	[37m  [39;49;00m[37m# 1998 rbi ranking[39;49;00m[37m[39;49;00m$
    92	[37m  [39;49;00m-[37m [39;49;00mSammy Sosa[37m[39;49;00m$
    93	[37m  [39;49;00m-[37m [39;49;00mKen Griffey[37m[39;49;00m$
    94	[37m[39;49;00m$
    95	[37m# Anchors and aliases[39;49;00m[37m[39;49;00m$
    96	[04m[36m---[39;49;00m[37m[39;49;00m$
    97	[94mhr[39;49;00m:[37m[39;49;00m$
    98	[37m  [39;49;00m-[37m [39;49;00mMark McGwire[37m[39;49;00m$
    99	[37m  [39;49;00m[37m# Following node labeled SS[39;49;00m[37m[39;49;00m$
   100	[37m  [39;49;00m-[37m [39;49;00m&SS[37m [39;49;00mSammy Sosa[37m[39;49;00m$
   101	[94mrbi[39;49;00m:[37m[39;49;00m$
   102	[37m  [39;49;00m-[37m [39;49;00m[31m*SS[39;49;00m[37m [39;49;00m[37m# Subsequent occurrence[39;49;00m[37m[39;49;00m$
   103	[37m  [39;49;00m-[37m [39;49;00mKen Griffey[37m[39;49;00m$
   104	[37m[39;49;00m$
   105	[37m# Mapping between sequences[39;49;00m[37m[39;49;00m$
   106	[04m[36m---[39;49;00m[37m[39;49;00m$
   107	?[37m [39;49;00m-[37m [39;49;00mDetroit Tigers[37m[39;49;00m$
   108	[37m  [39;49;00m-[37m [39;49;00mChicago cubs[37m[39;49;00m$
   109	:[37m[39;49;00m$
   110	[37m  [39;49;00m-[37m [39;49;00m2001-07-23[37m[39;49;00m$
   111	?[37m [39;49;00m[[37m [39;49;00m[31mNew[39;49;00m[31m [39;49;00m[31mYork[39;49;00m[31m [39;49;00m[31mYankees[39;49;00m,[37m[39;49;00m$
   112	[37m    [39;49;00m[31mAtlanta[39;49;00m[31m [39;49;00m[31mBraves[39;49;00m[37m [39;49;00m][37m[39;49;00m$
   113	:[37m [39;49;00m[[37m [39;49;00m[31m2001-07-02[39;49;00m,[37m [39;49;00m[31m2001-08-12[39;49;00m,[37m[39;49;00m$
   114	[37m    [39;49;00m[31m2001-08-14[39;49;00m[37m [39;49;00m][37m[39;49;00m$
   115	[37m[39;49;00m$
   116	[37m# Inline nested mapping[39;49;00m[37m[39;49;00m$
   117	[04m[36m---[39;49;00m[37m[39;49;00m$
   118	[37m# products purchased[39;49;00m[37m[39;49;00m$
   119	-[37m [39;49;00m[94mitem    [39;49;00m:[37m [39;49;00mSuper Hoop[37m[39;49;00m$
   120	[37m  [39;49;00m[94mquantity[39;49;00m:[37m [39;49;00m1[37m[39;49;00m$
   121	-[37m [39;49;00m[94mitem    [39;49;00m:[37m [39;49;00mBasketball[37m[39;49;00m$
   122	[37m  [39;49;00m[94mquantity[39;49;00m:[37m [39;49;00m4[37m[39;49;00m$
   123	-[37m [39;49;00m[94mitem    [39;49;00m:[37m [39;49;00mBig Shoes[37m[39;49;00m$
   124	[37m  [39;49;00m[94mquantity[39;49;00m:[37m [39;49;00m1[37m[39;49;00m$
   125	[37m[39;49;00m$
   126	[37m# Literal scalars[39;49;00m[37m[39;49;00m$
   127	[04m[36m---[39;49;00m[37m [39;49;00m|[37m [39;49;00m[37m# ASCII art[39;49;00m[37m[39;49;00m$
   128	[37m  [39;49;00m[31m\//||\/||[39;49;00m[37m[39;49;00m$
   129	[37m  [39;49;00m[31m// ||  ||__[39;49;00m[37m[39;49;00m$
   130	[37m[39;49;00m$
   131	[37m# Folded scalars[39;49;00m[37m[39;49;00m$
   132	[04m[36m---[39;49;00m[37m [39;49;00m>[37m[39;49;00m$
   133	[37m  [39;49;00m[31mMark McGwire's[39;49;00m[37m[39;49;00m$
   134	[37m  [39;49;00m[31myear was crippled[39;49;00m[37m[39;49;00m$
   135	[37m  [39;49;00m[31mby a knee injury.[39;49;00m[37m[39;49;00m$
   136	[37m[39;49;00m$
   137	[37m# Preserved indented block in a folded scalar[39;49;00m[37m[39;49;00m$
   138	[04m[36m---[39;49;00m[37m[39;49;00m$
   139	>[37m[39;49;00m$
   140	[37m [39;49;00m[31mSammy Sosa completed another[39;49;00m[37m[39;49;00m$
   141	[37m [39;49;00m[31mfine season with great stats.[39;49;00m[37m[39;49;00m$
   142	[37m[39;49;00m$
   143	[37m   [39;49;00m[31m63 Home Runs[39;49;00m[37m[39;49;00m$
   144	[37m   [39;49;00m[31m0.288 Batting Average[39;49;00m[37m[39;49;00m$
   145	[37m[39;49;00m$
   146	[37m [39;49;00m[31mWhat a year![39;49;00m[37m[39;49;00m$
   147	[37m[39;49;00m$
   148	[37m# Indentation determines scope[39;49;00m[37m[39;49;00m$
   149	[04m[36m---[39;49;00m[37m[39;49;00m$
   150	[94mname[39;49;00m:[37m [39;49;00mMark McGwire[37m[39;49;00m$
   151	[94maccomplishment[39;49;00m:[37m [39;49;00m>[37m[39;49;00m$
   152	[37m  [39;49;00m[31mMark set a major league[39;49;00m[37m[39;49;00m$
   153	[37m  [39;49;00m[31mhome run record in 1998.[39;49;00m[37m[39;49;00m$
   154	[94mstats[39;49;00m:[37m [39;49;00m|[37m[39;49;00m$
   155	[37m  [39;49;00m[31m65 Home Runs[39;49;00m[37m[39;49;00m$
   156	[37m  [39;49;00m[31m0.278 Batting Average[39;49;00m[37m[39;49;00m$
   157	[37m[39;49;00m$
   158	[37m# Quoted scalars[39;49;00m[37m[39;49;00m$
   159	[04m[36m---[39;49;00m[37m[39;49;00m$
   160	[94municode[39;49;00m:[37m [39;49;00m[33m"[39;49;00m[33mSosa[39;49;00m[31m [39;49;00m[33mdid[39;49;00m[31m [39;49;00m[33mfine.[39;49;00m[33m\u263A[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   161	[94mcontrol[39;49;00m:[37m [39;49;00m[33m"[39;49;00m[33m\b[39;49;00m[33m1998[39;49;00m[33m\t[39;49;00m[33m1999[39;49;00m[33m\t[39;49;00m[33m2000[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   162	[94mhex esc[39;49;00m:[37m [39;49;00m[33m"[39;49;00m[33m\x0d[39;49;00m[33m\x0a[39;49;00m[31m [39;49;00m[33mis[39;49;00m[31m [39;49;00m[33m\r[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   163	[94msingle[39;49;00m:[37m [39;49;00m[33m'[39;49;00m[33m"Howdy!"[39;49;00m[31m [39;49;00m[33mhe[39;49;00m[31m [39;49;00m[33mcried.[39;49;00m[33m'[39;49;00m[37m[39;49;00m$
   164	[94mquoted[39;49;00m:[37m [39;49;00m[33m'[39;49;00m[31m [39;49;00m[33m#[39;49;00m[31m [39;49;00m[33mnot[39;49;00m[31m [39;49;00m[33ma[39;49;00m[31m [39;49;00m[33m''[39;49;00m[33mcomment[39;49;00m[33m''[39;49;00m[33m.[39;49;00m[33m'[39;49;00m[37m[39;49;00m$
   165	[94mtie-fighter[39;49;00m:[37m [39;49;00m[33m'[39;49;00m[33m|\-*-/|[39;49;00m[33m'[39;49;00m[37m[39;49;00m$
   166	[37m[39;49;00m$
   167	[37m# Multi-line flow scalars[39;49;00m[37m[39;49;00m$
   168	[04m[36m---[39;49;00m[37m[39;49;00m$
   169	[94mplain[39;49;00m:[37m[39;49;00m$
   170	[37m  [39;49;00mThis unquoted scalar[37m[39;49;00m$
   171	[37m  [39;49;00mspans many lines.[37m[39;49;00m$
   172	[94mquoted[39;49;00m:[37m [39;49;00m[33m"[39;49;00m[33mSo[39;49;00m[31m [39;49;00m[33mdoes[39;49;00m[31m [39;49;00m[33mthis[39;49;00m[37m[39;49;00m$
   173	[37m  [39;49;00m[33mquoted[39;49;00m[31m [39;49;00m[33mscalar.[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   174	[37m[39;49;00m$
   175	[37m# Integers[39;49;00m[37m[39;49;00m$
   176	[04m[36m---[39;49;00m[37m[39;49;00m$
   177	[94mcanonical[39;49;00m:[37m [39;49;00m12345[37m[39;49;00m$
   178	[94mdecimal[39;49;00m:[37m [39;49;00m+12_345[37m[39;49;00m$
   179	[94msexagesimal[39;49;00m:[37m [39;49;00m3:25:45[37m[39;49;00m$
   180	[94moctal[39;49;00m:[37m [39;49;00m014[37m[39;49;00m$
   181	[94mhexadecimal[39;49;00m:[37m [39;49;00m0xC[37m[39;49;00m$
   182	[37m[39;49;00m$
   183	[37m# Floating point[39;49;00m[37m[39;49;00m$
   184	[04m[36m---[39;49;00m[37m[39;49;00m$
   185	[94mcanonical[39;49;00m:[37m [39;49;00m1.23015e+3[37m[39;49;00m$
   186	[94mexponential[39;49;00m:[37m [39;49;00m12.3015e+02[37m[39;49;00m$
   187	[94msexagesimal[39;49;00m:[37m [39;49;00m20:30.15[37m[39;49;00m$
   188	[94mfixed[39;49;00m:[37m [39;49;00m1_230.15[37m[39;49;00m$
   189	[94mnegative infinity[39;49;00m:[37m [39;49;00m-.inf[37m[39;49;00m$
   190	[94mnot a number[39;49;00m:[37m [39;49;00m.NaN[37m[39;49;00m$
   191	[37m[39;49;00m$
   192	[37m# Miscellaneous[39;49;00m[37m[39;49;00m$
   193	[04m[36m---[39;49;00m[37m[39;49;00m$
   194	[94mnull[39;49;00m:[37m [39;49;00m~[37m[39;49;00m$
   195	[94mtrue[39;49;00m:[37m [39;49;00mboolean[37m[39;49;00m$
   196	[94mfalse[39;49;00m:[37m [39;49;00mboolean[37m[39;49;00m$
   197	[94mstring[39;49;00m:[37m [39;49;00m[33m'[39;49;00m[33m12345[39;49;00m[33m'[39;49;00m[37m[39;49;00m$
   198	[37m[39;49;00m$
   199	[37m# Timestamps[39;49;00m[37m[39;49;00m$
   200	[04m[36m---[39;49;00m[37m[39;49;00m$
   201	[94mcanonical[39;49;00m:[37m [39;49;00m2001-12-15T02:59:43.1Z[37m[39;49;00m$
   202	[94miso8601[39;49;00m:[37m [39;49;00m2001-12-14t21:59:43.10-05:00[37m[39;49;00m$
   203	[94mspaced[39;49;00m:[37m [39;49;00m2001-12-14 21:59:43.10 -5[37m[39;49;00m$
   204	[94mdate[39;49;00m:[37m [39;49;00m2002-12-14[37m[39;49;00m$
   205	[37m[39;49;00m$
   206	[37m# Various explicit tags[39;49;00m[37m[39;49;00m$
   207	[04m[36m---[39;49;00m[37m[39;49;00m$
   208	[94mnot-date[39;49;00m:[37m [39;49;00m[36m!!str[39;49;00m[37m [39;49;00m2002-04-28[37m[39;49;00m$
   209	[94mpicture[39;49;00m:[37m [39;49;00m[36m!!binary[39;49;00m[37m [39;49;00m|[37m[39;49;00m$
   210	[37m [39;49;00m[31mR0lGODlhDAAMAIQAAP//9/X[39;49;00m[37m[39;49;00m$
   211	[37m [39;49;00m[31m17unp5WZmZgAAAOfn515eXv[39;49;00m[37m[39;49;00m$
   212	[37m [39;49;00m[31mPz7Y6OjuDg4J+fn5OTk6enp[39;49;00m[37m[39;49;00m$
   213	[37m [39;49;00m[31m56enmleECcgggoBADs=[39;49;00m[37m[39;49;00m$
   214	[94mapplication specific tag[39;49;00m:[37m [39;49;00m[36m!something[39;49;00m[37m [39;49;00m|[37m[39;49;00m$
   215	[37m [39;49;00m[31mThe semantics of the tag[39;49;00m[37m[39;49;00m$
   216	[37m [39;49;00m[31mabove may be different for[39;49;00m[37m[39;49;00m$
   217	[37m [39;49;00m[31mdifferent documents.[39;49;00m[37m[39;49;00m$
   218	[37m[39;49;00m$
   219	[37m# Global tags[39;49;00m[37m[39;49;00m$
   220	[94m%TAG[39;49;00m[37m [39;49;00m[36m![39;49;00m[37m [39;49;00m[36mtag:clarkevans.com,2002:[39;49;00m[37m[39;49;00m$
   221	[04m[36m---[39;49;00m[37m [39;49;00m[36m!shape[39;49;00m[37m[39;49;00m$
   222	[37m  [39;49;00m[37m# Use the ! handle for presenting[39;49;00m[37m[39;49;00m$
   223	[37m  [39;49;00m[37m# tag:clarkevans.com,2002:circle[39;49;00m[37m[39;49;00m$
   224	-[37m [39;49;00m[36m!circle[39;49;00m[37m[39;49;00m$
   225	[37m  [39;49;00m[94mcenter[39;49;00m:[37m [39;49;00m&ORIGIN[37m [39;49;00m{[94mx[39;49;00m:[37m [39;49;00m[31m73[39;49;00m,[94m y[39;49;00m:[37m [39;49;00m[31m129[39;49;00m}[37m[39;49;00m$
   226	[37m  [39;49;00m[94mradius[39;49;00m:[37m [39;49;00m7[37m[39;49;00m$
   227	-[37m [39;49;00m[36m!line[39;49;00m[37m[39;49;00m$
   228	[37m  [39;49;00m[94mstart[39;49;00m:[37m [39;49;00m[31m*ORIGIN[39;49;00m[37m[39;49;00m$
   229	[37m  [39;49;00m[94mfinish[39;49;00m:[37m [39;49;00m{[94m x[39;49;00m:[37m [39;49;00m[31m89[39;49;00m,[94m y[39;49;00m:[37m [39;49;00m[31m102[39;49;00m[37m [39;49;00m}[37m[39;49;00m$
   230	-[37m [39;49;00m[36m!label[39;49;00m[37m[39;49;00m$
   231	[37m  [39;49;00m[94mstart[39;49;00m:[37m [39;49;00m[31m*ORIGIN[39;49;00m[37m[39;49;00m$
   232	[37m  [39;49;00m[94mcolor[39;49;00m:[37m [39;49;00m0xFFEEBB[37m[39;49;00m$
   233	[37m  [39;49;00m[94mtext[39;49;00m:[37m [39;49;00mPretty vector drawing.[37m[39;49;00m$
   234	[37m[39;49;00m$
   235	[37m# Unordered sets[39;49;00m[37m[39;49;00m$
   236	[04m[36m---[39;49;00m[37m [39;49;00m[36m!!set[39;49;00m[37m[39;49;00m$
   237	[37m# sets are represented as a[39;49;00m[37m[39;49;00m$
   238	[37m# mapping where each key is[39;49;00m[37m[39;49;00m$
   239	[37m# associated with the empty string[39;49;00m[37m[39;49;00m$
   240	?[37m [39;49;00mMark McGwire[37m[39;49;00m$
   241	?[37m [39;49;00mSammy Sosa[37m[39;49;00m$
   242	?[37m [39;49;00mKen Griff[37m[39;49;00m$
   243	[37m[39;49;00m$
   244	[37m# Ordered mappings[39;49;00m[37m[39;49;00m$
   245	[04m[36m---[39;49;00m[37m [39;49;00m[36m!!omap[39;49;00m[37m[39;49;00m$
   246	[37m# ordered maps are represented as[39;49;00m[37m[39;49;00m$
   247	[37m# a sequence of mappings, with[39;49;00m[37m[39;49;00m$
   248	[37m# each mapping having one key[39;49;00m[37m[39;49;00m$
   249	-[37m [39;49;00m[94mMark McGwire[39;49;00m:[37m [39;49;00m65[37m[39;49;00m$
   250	-[37m [39;49;00m[94mSammy Sosa[39;49;00m:[37m [39;49;00m63[37m[39;49;00m$
   251	-[37m [39;49;00m[94mKen Griffy[39;49;00m:[37m [39;49;00m58[37m[39;49;00m$
   252	[37m[39;49;00m$
   253	[37m# Full length example[39;49;00m[37m[39;49;00m$
   254	[04m[36m---[39;49;00m[37m [39;49;00m[36m!<tag:clarkevans.com,2002:invoice>[39;49;00m[37m[39;49;00m$
   255	[94minvoice[39;49;00m:[37m [39;49;00m34843[37m[39;49;00m$
   256	[94mdate   [39;49;00m:[37m [39;49;00m2001-01-23[37m[39;49;00m$
   257	[94mbill-to[39;49;00m:[37m [39;49;00m&id001[37m[39;49;00m$
   258	[37m    [39;49;00m[94mgiven  [39;49;00m:[37m [39;49;00mChris[37m[39;49;00m$
   259	[37m    [39;49;00m[94mfamily [39;49;00m:[37m [39;49;00mDumars[37m[39;49;00m$
   260	[37m    [39;49;00m[94maddress[39;49;00m:[37m[39;49;00m$
   261	[37m        [39;49;00m[94mlines[39;49;00m:[37m [39;49;00m|[37m[39;49;00m$
   262	[37m            [39;49;00m[31m458 Walkman Dr.[39;49;00m[37m[39;49;00m$
   263	[37m            [39;49;00m[31mSuite #292[39;49;00m[37m[39;49;00m$
   264	[37m        [39;49;00m[94mcity    [39;49;00m:[37m [39;49;00mRoyal Oak[37m[39;49;00m$
   265	[37m        [39;49;00m[94mstate   [39;49;00m:[37m [39;49;00mMI[37m[39;49;00m$
   266	[37m        [39;49;00m[94mpostal  [39;49;00m:[37m [39;49;00m48046[37m[39;49;00m$
   267	[94mship-to[39;49;00m:[37m [39;49;00m[31m*id001[39;49;00m[37m[39;49;00m$
   268	[94mproduct[39;49;00m:[37m[39;49;00m$
   269	[37m    [39;49;00m-[37m [39;49;00m[94msku         [39;49;00m:[37m [39;49;00mBL394D[37m[39;49;00m$
   270	[37m      [39;49;00m[94mquantity    [39;49;00m:[37m [39;49;00m4[37m[39;49;00m$
   271	[37m      [39;49;00m[94mdescription [39;49;00m:[37m [39;49;00mBasketball[37m[39;49;00m$
   272	[37m      [39;49;00m[94mprice       [39;49;00m:[37m [39;49;00m450.00[37m[39;49;00m$
   273	[37m    [39;49;00m-[37m [39;49;00m[94msku         [39;49;00m:[37m [39;49;00mBL4438H[37m[39;49;00m$
   274	[37m      [39;49;00m[94mquantity    [39;49;00m:[37m [39;49;00m1[37m[39;49;00m$
   275	[37m      [39;49;00m[94mdescription [39;49;00m:[37m [39;49;00mSuper Hoop[37m[39;49;00m$
   276	[37m      [39;49;00m[94mprice       [39;49;00m:[37m [39;49;00m2392.00[37m[39;49;00m$
   277	[94mtax  [39;49;00m:[37m [39;49;00m251.42[37m[39;49;00m$
   278	[94mtotal[39;49;00m:[37m [39;49;00m4443.52[37m[39;49;00m$
   279	[94mcomments[39;49;00m:[37m[39;49;00m$
   280	[37m    [39;49;00mLate afternoon is best.[37m[39;49;00m$
   281	[37m    [39;49;00mBackup contact is Nancy[37m[39;49;00m$
   282	[37m    [39;49;00mBillsmer @ 338-4338.[37m[39;49;00m$
   283	[37m[39;49;00m$
   284	[37m# Another full-length example[39;49;00m[37m[39;49;00m$
   285	[04m[36m---[39;49;00m[37m[39;49;00m$
   286	[94mTime[39;49;00m:[37m [39;49;00m2001-11-23 15:01:42 -5[37m[39;49;00m$
   287	[94mUser[39;49;00m:[37m [39;49;00med[37m[39;49;00m$
   288	[94mWarning[39;49;00m:[37m[39;49;00m$
   289	[37m  [39;49;00mThis is an error message[37m[39;49;00m$
   290	[37m  [39;49;00mfor the log file[37m[39;49;00m$
   291	[04m[36m---[39;49;00m[37m[39;49;00m$
   292	[94mTime[39;49;00m:[37m [39;49;00m2001-11-23 15:02:31 -5[37m[39;49;00m$
   293	[94mUser[39;49;00m:[37m [39;49;00med[37m[39;49;00m$
   294	[94mWarning[39;49;00m:[37m[39;49;00m$
   295	[37m  [39;49;00mA slightly different error[37m[39;49;00m$
   296	[37m  [39;49;00mmessage.[37m[39;49;00m$
   297	[04m[36m---[39;49;00m[37m[39;49;00m$
   298	[94mDate[39;49;00m:[37m [39;49;00m2001-11-23 15:03:17 -5[37m[39;49;00m$
   299	[94mUser[39;49;00m:[37m [39;49;00med[37m[39;49;00m$
   300	[94mFatal[39;49;00m:[37m[39;49;00m$
   301	[37m  [39;49;00mUnknown variable "bar"[37m[39;49;00m$
   302	[94mStack[39;49;00m:[37m[39;49;00m$
   303	[37m  [39;49;00m-[37m [39;49;00m[94mfile[39;49;00m:[37m [39;49;00mTopClass.py[37m[39;49;00m$
   304	[37m    [39;49;00m[94mline[39;49;00m:[37m [39;49;00m23[37m[39;49;00m$
   305	[37m    [39;49;00m[94mcode[39;49;00m:[37m [39;49;00m|[37m[39;49;00m$
   306	[37m      [39;49;00m[31mx = MoreObject("345\n")[39;49;00m[37m[39;49;00m$
   307	[37m  [39;49;00m-[37m [39;49;00m[94mfile[39;49;00m:[37m [39;49;00mMoreClass.py[37m[39;49;00m$
   308	[37m    [39;49;00m[94mline[39;49;00m:[37m [39;49;00m58[37m[39;49;00m$
   309	[37m    [39;49;00m[94mcode[39;49;00m:[37m [39;49;00m|-[37m[39;49;00m$
   310	[37m      [39;49;00m[31mfoo = bar[39;49;00m$

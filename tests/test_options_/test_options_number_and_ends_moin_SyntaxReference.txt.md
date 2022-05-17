     1	## Please edit system and help pages ONLY in the moinmaster wiki! For more$
     2	## information, please see MoinMaster:MoinPagesEditorGroup.$
     3	##master-page:Unknown-Page$
     4	##master-date:Unknown-Date$
     5	#acl MoinPagesEditorGroup:read,write,delete,revert All:read$
     6	#format wiki$
     7	#language en$
     8	$
     9	This page aims to introduce the most important elements of MoinMoin``'s syntax at a glance, showing first the markup verbatim and then how it is rendered by the wiki engine. Additionally, you'll find links to the relative help pages. Please note that some of the features depend on your configuration.$
    10	$
    11	= Table of Contents =$
    12	{{{$
    13	'''Contents''' (up to the 2nd level)$
    14	[[TableOfContents(2)]]$
    15	}}}$
    16	'''Contents''' (up to the 2nd level)$
    17	[[TableOfContents(2)]]$
    18	$
    19	= Headings =$
    20	'''''see:''' HelpOnHeadlines''$
    21	{{{$
    22	= heading 1st level =$
    23	== heading 2nd level ==$
    24	=== heading 3rd level ===$
    25	==== heading 4th level ====$
    26	===== heading 5th level =====$
    27	}}}$
    28	= heading 1st level =$
    29	== heading 2nd level ==$
    30	=== heading 3rd level ===$
    31	==== heading 4th level ====$
    32	===== heading 5th level =====$
    33	$
    34	= Text Formatting =$
    35	'''''see:''' HelpOnFormatting''$
    36	{{{$
    37	 * ''emphasized (italics)''$
    38	 * '''boldface'''$
    39	 * '''''bold italics'''''$
    40	 * `monospace`$
    41	 * {{{source code}}}$
    42	 * __underline__$
    43	 * ,,sub,,script$
    44	 * ^super^script$
    45	 * ~-smaller-~$
    46	 * ~+larger+~$
    47	 * --(strike through)--$
    48	}}}$
    49	 * ''emphasized (italics)''$
    50	 * '''boldface'''$
    51	 * '''''bold italics'''''$
    52	 * `monospace`$
    53	 * {{{source code}}}$
    54	 * __underline__$
    55	 * ,,sub,,script$
    56	 * ^super^script$
    57	 * ~-smaller-~$
    58	 * ~+larger+~$
    59	 * --(strike through)--$
    60	$
    61	= Hyperlinks =$
    62	'''''see:''' HelpOnLinking''$
    63	== Internal Links ==$
    64	{{{$
    65	 * FrontPage$
    66	 * ["FrontPage"]$
    67	 * HelpOnEditing/SubPages$
    68	 * /SubPage$
    69	 * ../SiblingPage$
    70	 * [:FrontPage:named link]$
    71	 * [#anchorname]$
    72	 * [#anchorname description]$
    73	 * [wiki:Self:PageName#anchorname]$
    74	 * [wiki:Self:PageName#anchorname description]$
    75	 * attachment:filename.txt$
    76	}}}$
    77	 * FrontPage$
    78	 * ["FrontPage"]$
    79	 * HelpOnEditing/SubPages$
    80	 * /SubPage$
    81	 * ../SiblingPage$
    82	 * [:FrontPage:named link]$
    83	 * [#anchorname]$
    84	 * [#anchorname description]$
    85	 * [wiki:Self:PageName#anchorname]$
    86	 * [wiki:Self:PageName#anchorname description]$
    87	 * attachment:filename.txt$
    88	$
    89	== External Links ==$
    90	{{{$
    91	 * http://moinmoin.wikiwikiweb.de/$
    92	 * [http://moinmoin.wikiwikiweb.de/]$
    93	 * [http://moinmoin.wikiwikiweb.de/ MoinMoin Wiki]$
    94	 * [http://moinmoin.wikiwikiweb.de/wiki/moinmoin.png]$
    95	 * http://moinmoin.wikiwikiweb.de/wiki/moinmoin.png$
    96	 * [http://moinmoin.wikiwikiweb.de/wiki/moinmoin.png moinmoin.png]$
    97	 * MeatBall:InterWiki$
    98	 * wiki:MeatBall/InterWiki$
    99	 * [wiki:MeatBall/InterWiki]$
   100	 * [wiki:MeatBall/InterWiki InterWiki page on MeatBall]$
   101	 * [file://///servername/share/full/path/to/file/filename%20with%20spaces.txt link to file filename with spaces.txt]$
   102	 * user@example.com$
   103	}}}$
   104	 * http://moinmoin.wikiwikiweb.de/$
   105	 * [http://moinmoin.wikiwikiweb.de/]$
   106	 * [http://moinmoin.wikiwikiweb.de/ MoinMoin Wiki]$
   107	 * [http://moinmoin.wikiwikiweb.de/wiki/moinmoin.png]$
   108	 * http://moinmoin.wikiwikiweb.de/wiki/moinmoin.png$
   109	 * [http://moinmoin.wikiwikiweb.de/wiki/moinmoin.png moinmoin.png]$
   110	 * MeatBall:InterWiki$
   111	 * wiki:MeatBall/InterWiki$
   112	 * [wiki:MeatBall/InterWiki]$
   113	 * [wiki:MeatBall/InterWiki InterWiki page on MeatBall]$
   114	 * [file://///servername/share/full/path/to/file/filename%20with%20spaces.txt link to file filename with spaces.txt]$
   115	 * user@example.com$
   116	$
   117	== Avoid or Limit Automatical Linking ==$
   118	{{{$
   119	 * Wiki''''''Name$
   120	 * Wiki``Name$
   121	 * !WikiName$
   122	 * WikiName''''''s$
   123	 * WikiName``s$
   124	 * `http://www.example.com`$
   125	}}}$
   126	 * Wiki''''''Name$
   127	 * Wiki``Name$
   128	 * !WikiName$
   129	 * WikiName''''''s$
   130	 * WikiName``s$
   131	 * `http://www.example.com`$
   132	$
   133	= Blockquotes and Indentions =$
   134	{{{$
   135	 indented text$
   136	  text indented to the 2nd level$
   137	}}}$
   138	 indented text$
   139	  text indented to the 2nd level$
   140	$
   141	= Lists =$
   142	'''''see:''' HelpOnLists''$
   143	== Unordered Lists ==$
   144	{{{$
   145	 * item 1$
   146	$
   147	 * item 2 (preceding white space)$
   148	  * item 2.1$
   149	   * item 2.1.1$
   150	 * item 3$
   151	  . item 3.1 (bulletless)$
   152	 . item 4 (bulletless)$
   153	  * item 4.1$
   154	   . item 4.1.1 (bulletless)$
   155	}}}$
   156	 * item 1$
   157	$
   158	 * item 2 (preceding white space)$
   159	  * item 2.1$
   160	   * item 2.1.1$
   161	 * item 3$
   162	  . item 3.1 (bulletless)$
   163	 . item 4 (bulletless)$
   164	  * item 4.1$
   165	   . item 4.1.1 (bulletless)$
   166	$
   167	== Ordered Lists ==$
   168	=== with Numbers ===$
   169	{{{$
   170	 1. item 1$
   171	   1. item 1.1$
   172	   1. item 1.2$
   173	 1. item 2$
   174	}}}$
   175	 1. item 1$
   176	   1. item 1.1$
   177	   1. item 1.2$
   178	 1. item 2$
   179	$
   180	=== with Roman Numbers ===$
   181	{{{$
   182	 I. item 1$
   183	   i. item 1.1$
   184	   i. item 1.2$
   185	 I. item 2$
   186	}}}$
   187	 I. item 1$
   188	   i. item 1.1$
   189	   i. item 1.2$
   190	 I. item 2$
   191	$
   192	=== with Letters ===$
   193	{{{$
   194	 A. item A$
   195	   a. item A. a)$
   196	   a. item A. b)$
   197	 A. item B$
   198	}}}$
   199	 A. item A$
   200	   a. item A. a)$
   201	   a. item A. b)$
   202	 A. item B$
   203	$
   204	== Definition Lists ==$
   205	{{{$
   206	 term:: definition$
   207	 object:: description 1$
   208	 :: description 2$
   209	 Action Items::$
   210	 :: First Item$
   211	 :: Second Item$
   212	}}}$
   213	 term:: definition$
   214	 object:: description 1$
   215	 :: description 2$
   216	 Action Items::$
   217	 :: First Item$
   218	 :: Second Item$
   219	$
   220	= Horizontal Rules =$
   221	'''''see:''' HelpOnRules''$
   222	{{{$
   223	----$
   224	-----$
   225	------$
   226	-------$
   227	--------$
   228	---------$
   229	----------$
   230	}}}$
   231	----$
   232	-----$
   233	------$
   234	-------$
   235	--------$
   236	---------$
   237	----------$
   238	$
   239	= Tables =$
   240	'''''see:''' HelpOnTables''$
   241	== Tables ==$
   242	{{{$
   243	||'''A'''||'''B'''||'''C'''||$
   244	||1      ||2      ||3      ||$
   245	}}}$
   246	||'''A'''||'''B'''||'''C'''||$
   247	||1      ||2      ||3      ||$
   248	$
   249	== Cell Width ==$
   250	{{{$
   251	||minimal width ||<99%>maximal width ||$
   252	}}}$
   253	||minimal width ||<99%>maximal width ||$
   254	$
   255	== Spanning Rows and Columns  ==$
   256	{{{$
   257	||<|2> cell spanning 2 rows ||cell in the 2nd column ||$
   258	||cell in the 2nd column of the 2nd row ||$
   259	||<-2> cell spanning 2 columns ||$
   260	||||use empty cells as a shorthand ||$
   261	}}}$
   262	||<|2> cell spanning 2 rows ||cell in the 2nd column ||$
   263	||cell in the 2nd column of the 2nd row ||$
   264	||<-2> cell spanning 2 columns ||$
   265	||||use empty cells as a shorthand ||$
   266	$
   267	== Alignment of Cell Contents ==$
   268	{{{$
   269	||<^|3> top (combined) ||<:99%> center (combined) ||<v|3> bottom (combined) ||$
   270	||<)> right ||$
   271	||<(> left ||$
   272	}}}$
   273	||<^|3> top (combined) ||<:99%> center (combined) ||<v|3> bottom (combined) ||$
   274	||<)> right ||$
   275	||<(> left ||$
   276	$
   277	== Coulored Table Cells ==$
   278	{{{$
   279	||<#0000FF> blue ||<#00FF00> green    ||<#FF0000> red    ||$
   280	||<#00FFFF> cyan ||<#FF00FF> magenta  ||<#FFFF00> yellow ||$
   281	}}}$
   282	||<#0000FF> blue ||<#00FF00> green    ||<#FF0000> red    ||$
   283	||<#00FFFF> cyan ||<#FF00FF> magenta  ||<#FFFF00> yellow ||$
   284	$
   285	== HTML-like Options for Tables ==$
   286	{{{$
   287	||A ||<rowspan="2"> like <|2> ||$
   288	||<bgcolor="#00FF00"> like <#00FF00> ||$
   289	||<colspan="2"> like <-2>||$
   290	}}}$
   291	||A ||<rowspan="2"> like <|2> ||$
   292	||<bgcolor="#00FF00"> like <#00FF00> ||$
   293	||<colspan="2"> like <-2>||$
   294	$
   295	= Macros and Variables =$
   296	== Macros ==$
   297	'''''see:''' HelpOnMacros''$
   298	 * `[[Anchor(anchorname)]]` inserts a link anchor `anchorname`$
   299	 * `[[BR]]` inserts a hard line break$
   300	 * `[[FootNote(Note)]]` inserts a footnote saying `Note`$
   301	 * `[[Include(HelpOnMacros/Include)]]` inserts the contents of the page `HelpOnMacros/Include` inline$
   302	 * `[[MailTo(user AT example DOT com)]]` obfuscates the email address `user@example.com` to users not logged in$
   303	$
   304	== Variables ==$
   305	'''''see:''' HelpOnVariables''$
   306	 * `@``SIG``@` inserts your login name and timestamp of modification$
   307	 * `@``TIME``@` inserts date and time of modification$
   308	$
   309	= Smileys and Icons =$
   310	'''''see:''' HelpOnSmileys''$
   311	[[ShowSmileys]]$
   312	$
   313	= Source code =$
   314	'''''see:''' HelpOnParsers''$
   315	== Verbatim Display ==$
   316	{{{$
   317	{ { {$
   318	def hello():$
   319	    print "Hello World!"$
   320	} } }$
   321	}}}$
   322	/!\ Remove spaces between "`{ { {`" and "`} } }`".$
   323	{{{$
   324	def hello():$
   325	    print "Hello World!"$
   326	}}}$
   327	$
   328	== Syntax Highlighting ==$
   329	{{{$
   330	{ { {#!python$
   331	def hello():$
   332	    print "Hello World!"$
   333	} } }$
   334	}}}$
   335	/!\ Remove spaces between "`{ { {`" and "`} } }`".$
   336	{{{#!python$
   337	def hello():$
   338	    print "Hello World!"$
   339	}}}$

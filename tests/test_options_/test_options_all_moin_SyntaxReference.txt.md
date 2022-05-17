     1^I## Please edit system and help pages ONLY in the moinmaster wiki! For more$
     2^I## information, please see MoinMaster:MoinPagesEditorGroup.$
     3^I##master-page:Unknown-Page$
     4^I##master-date:Unknown-Date$
     5^I#acl MoinPagesEditorGroup:read,write,delete,revert All:read$
     6^I#format wiki$
     7^I#language en$
     8^I$
     9^IThis page aims to introduce the most important elements of MoinMoin``'s syntax at a glance, showing first the markup verbatim and then how it is rendered by the wiki engine. Additionally, you'll find links to the relative help pages. Please note that some of the features depend on your configuration.$
    10^I$
    11^I= Table of Contents =$
    12^I{{{$
    13^I'''Contents''' (up to the 2nd level)$
    14^I[[TableOfContents(2)]]$
    15^I}}}$
    16^I'''Contents''' (up to the 2nd level)$
    17^I[[TableOfContents(2)]]$
    18^I$
    19^I= Headings =$
    20^I'''''see:''' HelpOnHeadlines''$
    21^I{{{$
    22^I= heading 1st level =$
    23^I== heading 2nd level ==$
    24^I=== heading 3rd level ===$
    25^I==== heading 4th level ====$
    26^I===== heading 5th level =====$
    27^I}}}$
    28^I= heading 1st level =$
    29^I== heading 2nd level ==$
    30^I=== heading 3rd level ===$
    31^I==== heading 4th level ====$
    32^I===== heading 5th level =====$
    33^I$
    34^I= Text Formatting =$
    35^I'''''see:''' HelpOnFormatting''$
    36^I{{{$
    37^I * ''emphasized (italics)''$
    38^I * '''boldface'''$
    39^I * '''''bold italics'''''$
    40^I * `monospace`$
    41^I * {{{source code}}}$
    42^I * __underline__$
    43^I * ,,sub,,script$
    44^I * ^super^script$
    45^I * ~-smaller-~$
    46^I * ~+larger+~$
    47^I * --(strike through)--$
    48^I}}}$
    49^I * ''emphasized (italics)''$
    50^I * '''boldface'''$
    51^I * '''''bold italics'''''$
    52^I * `monospace`$
    53^I * {{{source code}}}$
    54^I * __underline__$
    55^I * ,,sub,,script$
    56^I * ^super^script$
    57^I * ~-smaller-~$
    58^I * ~+larger+~$
    59^I * --(strike through)--$
    60^I$
    61^I= Hyperlinks =$
    62^I'''''see:''' HelpOnLinking''$
    63^I== Internal Links ==$
    64^I{{{$
    65^I * FrontPage$
    66^I * ["FrontPage"]$
    67^I * HelpOnEditing/SubPages$
    68^I * /SubPage$
    69^I * ../SiblingPage$
    70^I * [:FrontPage:named link]$
    71^I * [#anchorname]$
    72^I * [#anchorname description]$
    73^I * [wiki:Self:PageName#anchorname]$
    74^I * [wiki:Self:PageName#anchorname description]$
    75^I * attachment:filename.txt$
    76^I}}}$
    77^I * FrontPage$
    78^I * ["FrontPage"]$
    79^I * HelpOnEditing/SubPages$
    80^I * /SubPage$
    81^I * ../SiblingPage$
    82^I * [:FrontPage:named link]$
    83^I * [#anchorname]$
    84^I * [#anchorname description]$
    85^I * [wiki:Self:PageName#anchorname]$
    86^I * [wiki:Self:PageName#anchorname description]$
    87^I * attachment:filename.txt$
    88^I$
    89^I== External Links ==$
    90^I{{{$
    91^I * http://moinmoin.wikiwikiweb.de/$
    92^I * [http://moinmoin.wikiwikiweb.de/]$
    93^I * [http://moinmoin.wikiwikiweb.de/ MoinMoin Wiki]$
    94^I * [http://moinmoin.wikiwikiweb.de/wiki/moinmoin.png]$
    95^I * http://moinmoin.wikiwikiweb.de/wiki/moinmoin.png$
    96^I * [http://moinmoin.wikiwikiweb.de/wiki/moinmoin.png moinmoin.png]$
    97^I * MeatBall:InterWiki$
    98^I * wiki:MeatBall/InterWiki$
    99^I * [wiki:MeatBall/InterWiki]$
   100^I * [wiki:MeatBall/InterWiki InterWiki page on MeatBall]$
   101^I * [file://///servername/share/full/path/to/file/filename%20with%20spaces.txt link to file filename with spaces.txt]$
   102^I * user@example.com$
   103^I}}}$
   104^I * http://moinmoin.wikiwikiweb.de/$
   105^I * [http://moinmoin.wikiwikiweb.de/]$
   106^I * [http://moinmoin.wikiwikiweb.de/ MoinMoin Wiki]$
   107^I * [http://moinmoin.wikiwikiweb.de/wiki/moinmoin.png]$
   108^I * http://moinmoin.wikiwikiweb.de/wiki/moinmoin.png$
   109^I * [http://moinmoin.wikiwikiweb.de/wiki/moinmoin.png moinmoin.png]$
   110^I * MeatBall:InterWiki$
   111^I * wiki:MeatBall/InterWiki$
   112^I * [wiki:MeatBall/InterWiki]$
   113^I * [wiki:MeatBall/InterWiki InterWiki page on MeatBall]$
   114^I * [file://///servername/share/full/path/to/file/filename%20with%20spaces.txt link to file filename with spaces.txt]$
   115^I * user@example.com$
   116^I$
   117^I== Avoid or Limit Automatical Linking ==$
   118^I{{{$
   119^I * Wiki''''''Name$
   120^I * Wiki``Name$
   121^I * !WikiName$
   122^I * WikiName''''''s$
   123^I * WikiName``s$
   124^I * `http://www.example.com`$
   125^I}}}$
   126^I * Wiki''''''Name$
   127^I * Wiki``Name$
   128^I * !WikiName$
   129^I * WikiName''''''s$
   130^I * WikiName``s$
   131^I * `http://www.example.com`$
   132^I$
   133^I= Blockquotes and Indentions =$
   134^I{{{$
   135^I indented text$
   136^I  text indented to the 2nd level$
   137^I}}}$
   138^I indented text$
   139^I  text indented to the 2nd level$
   140^I$
   141^I= Lists =$
   142^I'''''see:''' HelpOnLists''$
   143^I== Unordered Lists ==$
   144^I{{{$
   145^I * item 1$
   146^I$
   147^I * item 2 (preceding white space)$
   148^I  * item 2.1$
   149^I   * item 2.1.1$
   150^I * item 3$
   151^I  . item 3.1 (bulletless)$
   152^I . item 4 (bulletless)$
   153^I  * item 4.1$
   154^I   . item 4.1.1 (bulletless)$
   155^I}}}$
   156^I * item 1$
   157^I$
   158^I * item 2 (preceding white space)$
   159^I  * item 2.1$
   160^I   * item 2.1.1$
   161^I * item 3$
   162^I  . item 3.1 (bulletless)$
   163^I . item 4 (bulletless)$
   164^I  * item 4.1$
   165^I   . item 4.1.1 (bulletless)$
   166^I$
   167^I== Ordered Lists ==$
   168^I=== with Numbers ===$
   169^I{{{$
   170^I 1. item 1$
   171^I   1. item 1.1$
   172^I   1. item 1.2$
   173^I 1. item 2$
   174^I}}}$
   175^I 1. item 1$
   176^I   1. item 1.1$
   177^I   1. item 1.2$
   178^I 1. item 2$
   179^I$
   180^I=== with Roman Numbers ===$
   181^I{{{$
   182^I I. item 1$
   183^I   i. item 1.1$
   184^I   i. item 1.2$
   185^I I. item 2$
   186^I}}}$
   187^I I. item 1$
   188^I   i. item 1.1$
   189^I   i. item 1.2$
   190^I I. item 2$
   191^I$
   192^I=== with Letters ===$
   193^I{{{$
   194^I A. item A$
   195^I   a. item A. a)$
   196^I   a. item A. b)$
   197^I A. item B$
   198^I}}}$
   199^I A. item A$
   200^I   a. item A. a)$
   201^I   a. item A. b)$
   202^I A. item B$
   203^I$
   204^I== Definition Lists ==$
   205^I{{{$
   206^I term:: definition$
   207^I object:: description 1$
   208^I :: description 2$
   209^I Action Items::$
   210^I :: First Item$
   211^I :: Second Item$
   212^I}}}$
   213^I term:: definition$
   214^I object:: description 1$
   215^I :: description 2$
   216^I Action Items::$
   217^I :: First Item$
   218^I :: Second Item$
   219^I$
   220^I= Horizontal Rules =$
   221^I'''''see:''' HelpOnRules''$
   222^I{{{$
   223^I----$
   224^I-----$
   225^I------$
   226^I-------$
   227^I--------$
   228^I---------$
   229^I----------$
   230^I}}}$
   231^I----$
   232^I-----$
   233^I------$
   234^I-------$
   235^I--------$
   236^I---------$
   237^I----------$
   238^I$
   239^I= Tables =$
   240^I'''''see:''' HelpOnTables''$
   241^I== Tables ==$
   242^I{{{$
   243^I||'''A'''||'''B'''||'''C'''||$
   244^I||1      ||2      ||3      ||$
   245^I}}}$
   246^I||'''A'''||'''B'''||'''C'''||$
   247^I||1      ||2      ||3      ||$
   248^I$
   249^I== Cell Width ==$
   250^I{{{$
   251^I||minimal width ||<99%>maximal width ||$
   252^I}}}$
   253^I||minimal width ||<99%>maximal width ||$
   254^I$
   255^I== Spanning Rows and Columns  ==$
   256^I{{{$
   257^I||<|2> cell spanning 2 rows ||cell in the 2nd column ||$
   258^I||cell in the 2nd column of the 2nd row ||$
   259^I||<-2> cell spanning 2 columns ||$
   260^I||||use empty cells as a shorthand ||$
   261^I}}}$
   262^I||<|2> cell spanning 2 rows ||cell in the 2nd column ||$
   263^I||cell in the 2nd column of the 2nd row ||$
   264^I||<-2> cell spanning 2 columns ||$
   265^I||||use empty cells as a shorthand ||$
   266^I$
   267^I== Alignment of Cell Contents ==$
   268^I{{{$
   269^I||<^|3> top (combined) ||<:99%> center (combined) ||<v|3> bottom (combined) ||$
   270^I||<)> right ||$
   271^I||<(> left ||$
   272^I}}}$
   273^I||<^|3> top (combined) ||<:99%> center (combined) ||<v|3> bottom (combined) ||$
   274^I||<)> right ||$
   275^I||<(> left ||$
   276^I$
   277^I== Coulored Table Cells ==$
   278^I{{{$
   279^I||<#0000FF> blue ||<#00FF00> green    ||<#FF0000> red    ||$
   280^I||<#00FFFF> cyan ||<#FF00FF> magenta  ||<#FFFF00> yellow ||$
   281^I}}}$
   282^I||<#0000FF> blue ||<#00FF00> green    ||<#FF0000> red    ||$
   283^I||<#00FFFF> cyan ||<#FF00FF> magenta  ||<#FFFF00> yellow ||$
   284^I$
   285^I== HTML-like Options for Tables ==$
   286^I{{{$
   287^I||A ||<rowspan="2"> like <|2> ||$
   288^I||<bgcolor="#00FF00"> like <#00FF00> ||$
   289^I||<colspan="2"> like <-2>||$
   290^I}}}$
   291^I||A ||<rowspan="2"> like <|2> ||$
   292^I||<bgcolor="#00FF00"> like <#00FF00> ||$
   293^I||<colspan="2"> like <-2>||$
   294^I$
   295^I= Macros and Variables =$
   296^I== Macros ==$
   297^I'''''see:''' HelpOnMacros''$
   298^I * `[[Anchor(anchorname)]]` inserts a link anchor `anchorname`$
   299^I * `[[BR]]` inserts a hard line break$
   300^I * `[[FootNote(Note)]]` inserts a footnote saying `Note`$
   301^I * `[[Include(HelpOnMacros/Include)]]` inserts the contents of the page `HelpOnMacros/Include` inline$
   302^I * `[[MailTo(user AT example DOT com)]]` obfuscates the email address `user@example.com` to users not logged in$
   303^I$
   304^I== Variables ==$
   305^I'''''see:''' HelpOnVariables''$
   306^I * `@``SIG``@` inserts your login name and timestamp of modification$
   307^I * `@``TIME``@` inserts date and time of modification$
   308^I$
   309^I= Smileys and Icons =$
   310^I'''''see:''' HelpOnSmileys''$
   311^I[[ShowSmileys]]$
   312^I$
   313^I= Source code =$
   314^I'''''see:''' HelpOnParsers''$
   315^I== Verbatim Display ==$
   316^I{{{$
   317^I{ { {$
   318^Idef hello():$
   319^I    print "Hello World!"$
   320^I} } }$
   321^I}}}$
   322^I/!\ Remove spaces between "`{ { {`" and "`} } }`".$
   323^I{{{$
   324^Idef hello():$
   325^I    print "Hello World!"$
   326^I}}}$
   327^I$
   328^I== Syntax Highlighting ==$
   329^I{{{$
   330^I{ { {#!python$
   331^Idef hello():$
   332^I    print "Hello World!"$
   333^I} } }$
   334^I}}}$
   335^I/!\ Remove spaces between "`{ { {`" and "`} } }`".$
   336^I{{{#!python$
   337^Idef hello():$
   338^I    print "Hello World!"$
   339^I}}}$

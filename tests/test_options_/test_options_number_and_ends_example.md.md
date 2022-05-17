     1	[01m# this is a header[39;49;00m$
     2	$
     3	[01m[35m## this is a 2nd level header[39;49;00m$
     4	$
     5	[34m*[39;49;00m list item 1$
     6	  [34m*[39;49;00m list item 1.1$
     7	[34m*[39;49;00m list item 2$
     8	[34m-[39;49;00m list item 3$
     9	$
    10	[34m1.[39;49;00m numbered list item 1$
    11	[34m1.[39;49;00m numbered list item 2$
    12	$
    13	[34m- [39;49;00m[34m[ ][39;49;00m todo$
    14	[34m- [39;49;00m[34m[x][39;49;00m done$
    15	[34m- [39;49;00m[34m[X][39;49;00m done$
    16	$
    17	The following is italic: *italic*$
    18	The following is italic: _italic_$
    19	$
    20	The following is not italic: \*italic\*$
    21	The following is not italic: \_italic\_$
    22	$
    23	The following is not italic: snake*case*word$
    24	The following is not italic: snake_case_word$
    25	$
    26	The following is bold: **bold** **two or more words**$
    27	The following is bold: __bold__ __two or more words__$
    28	$
    29	The following is not bold: snake**case**word$
    30	The following is not bold: snake__case__word$
    31	$
    32	The following is strikethrough: [91m~~bold~~[39;49;00m$
    33	The following is not strikethrough: snake~~case~~word$
    34	$
    35	The following is bold with italics inside: **the next _word_ should have been italics**$
    36	[34m[39;49;00m$
    37	[34m> [39;49;00mthis is a quote$
    38	[34m[39;49;00m$
    39	[34m> [39;49;00mthis is a multiline$
    40	[34m> [39;49;00mquote string thing$
    41	$
    42	this sentence [33m`has monospace`[39;49;00m in it$
    43	$
    44	this sentence @tweets a person about a #topic.$
    45	$
    46	[[94mgoogle[39;49;00m]([36mhttps://google.com/some/path.html[39;49;00m)$
    47	![[94mImage of Yaktocat[39;49;00m]([36mhttps://octodex.github.com/images/yaktocat.png[39;49;00m)$
    48	$
    49	[[94mreference link[39;49;00m][id]$
    50	[id]: [36mhttp://example.com/[39;49;00m$
    51	[33m[39;49;00m$
    52	[33m```[39;49;00m$
    53	[33m  * this is just unformated[39;49;00m$
    54	[33m      __text__[39;49;00m$
    55	[33m```[39;49;00m$
    56	$
    57	some other text$
    58	[33m[39;49;00m$
    59	[33m```[39;49;00m[33mpython[39;49;00m$
    60	[34mfrom[39;49;00m [04m[36mpygments[39;49;00m [34mimport[39;49;00m token$
    61	[37m# comment[39;49;00m$
    62	[33m```[39;49;00m$
    63	$
    64	some more text$

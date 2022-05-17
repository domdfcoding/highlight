     1	[01m======================[39;49;00m$
     2	[01mDesigner Documentation[39;49;00m$
     3	[01m======================[39;49;00m$
     4	$
     5	This part of the Jinja documentaton is meant for template designers.$
     6	$
     7	[01mBasics[39;49;00m$
     8	[01m======[39;49;00m$
     9	$
    10	The Jinja template language is designed to strike a balance between content$
    11	and application logic. Nevertheless you can use a python like statement$
    12	language. You don't have to know how Python works to create Jinja templates,$
    13	but if you know it you can use some additional statements you may know from$
    14	Python.$
    15	$
    16	Here is a small example template:$
    17	$
    18	.. [35msourcecode[39;49;00m:: [34mhtml+jinja[39;49;00m$
    19	$
    20	    [36m<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"[39;49;00m$
    21	    [36m "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">[39;49;00m$
    22	    <[94mhtml[39;49;00m [36mxmlns[39;49;00m=[33m"http://www.w3.org/1999/xhtml"[39;49;00m [36mlang[39;49;00m=[33m"en"[39;49;00m [36mxml:lang[39;49;00m=[33m"en"[39;49;00m>$
    23	    <[94mhead[39;49;00m>$
    24	        <[94mtitle[39;49;00m>My Webpage</[94mtitle[39;49;00m>$
    25	    </[94mhead[39;49;00m>$
    26	    <[94mbody[39;49;00m>$
    27	        <[94mul[39;49;00m [36mid[39;49;00m=[33m"navigation"[39;49;00m>$
    28	        [36m{%[39;49;00m [34mfor[39;49;00m [31mitem[39;49;00m [34min[39;49;00m [31mnavigation[39;49;00m [36m%}[39;49;00m$
    29	            <[94mli[39;49;00m><[94ma[39;49;00m [36mhref[39;49;00m=[33m"[39;49;00m[36m{{[39;49;00m [31mitem[39;49;00m[31m.href[39;49;00m|[32me[39;49;00m [36m}}[39;49;00m[33m"[39;49;00m>[36m{{[39;49;00m [31mitem[39;49;00m[31m.caption[39;49;00m|[32me[39;49;00m [36m}}[39;49;00m</[94ma[39;49;00m></[94mli[39;49;00m>$
    30	        [36m{%[39;49;00m [34mendfor[39;49;00m [36m%}[39;49;00m$
    31	        </[94mul[39;49;00m>$
    32	$
    33	        <[94mh1[39;49;00m>My Webpage</[94mh1[39;49;00m>$
    34	        [36m{{[39;49;00m [31mvariable[39;49;00m [36m}}[39;49;00m$
    35	    </[94mbody[39;49;00m>$
    36	    </[94mhtml[39;49;00m>$
    37	$
    38	This covers the default settings. The application developer might have changed$
    39	the syntax from [33m``[39;49;00m[33m{% foo %}[39;49;00m[33m``[39;49;00m to [33m``[39;49;00m[33m<% foo %>[39;49;00m[33m``[39;49;00m or something similar. This$
    40	documentation just covers the default values.$
    41	$
    42	A variable looks like [33m``[39;49;00m[33m{{ foobar }}[39;49;00m[33m``[39;49;00m where foobar is the variable name. Inside$
    43	of statements ([33m``[39;49;00m[33m{% some content here %}[39;49;00m[33m``[39;49;00m) variables are just normal names$
    44	without the braces around it. In fact [33m``[39;49;00m[33m{{ foobar }}[39;49;00m[33m``[39;49;00m is just an alias for$
    45	the statement [33m``[39;49;00m[33m{% print foobar %}[39;49;00m[33m``[39;49;00m.$
    46	$
    47	Variables are coming from the context provided by the application. Normally there$
    48	should be a documentation regarding the context contents but if you want to know$
    49	the content of the current context, you can add this to your template:$
    50	$
    51	.. [35msourcecode[39;49;00m:: [34mhtml+jinja[39;49;00m$
    52	$
    53	    <[94mpre[39;49;00m>[36m{{[39;49;00m [31mdebug[39;49;00m()|[32me[39;49;00m [36m}}[39;49;00m</[94mpre[39;49;00m>$
    54	$
    55	A context isn't flat which means that each variable can has subvariables, as long$
    56	as it is representable as python data structure. You can access attributes of$
    57	a variable using the dot and bracket operators. The following examples show$
    58	this:$
    59	$
    60	.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
    61	$
    62	    [36m{{[39;49;00m [31muser[39;49;00m[31m.username[39;49;00m [36m}}[39;49;00m$
    63	        is the same as$
    64	    [36m{{[39;49;00m [31muser[39;49;00m[[33m'username'[39;49;00m] [36m}}[39;49;00m$
    65	        you can also use a variable to access an attribute:$
    66	    [36m{{[39;49;00m [31musers[39;49;00m[[31mcurrent_user[39;49;00m][31m.username[39;49;00m [36m}}[39;49;00m$
    67	        If you have numerical indices you have to use the [] syntax:$
    68	    [36m{{[39;49;00m [31musers[39;49;00m[[34m0[39;49;00m][31m.username[39;49;00m [36m}}[39;49;00m$
    69	$
    70	[01mFilters[39;49;00m$
    71	[01m=======[39;49;00m$
    72	$
    73	In the examples above you might have noticed the pipe symbols. Pipe symbols tell$
    74	the engine that it has to apply a filter on the variable. Here is a small example:$
    75	$
    76	.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
    77	$
    78	    [36m{{[39;49;00m [31mvariable[39;49;00m|[32mreplace[39;49;00m([33m'foo'[39;49;00m, [33m'bar'[39;49;00m)|[32mescape[39;49;00m [36m}}[39;49;00m$
    79	$
    80	If you want, you can also put whitespace between the filters.$
    81	$
    82	This will look for a variable [31m`variable`[39;49;00m, pass it to the filter [31m`replace`[39;49;00m$
    83	with the arguments [33m``[39;49;00m[33m'foo'[39;49;00m[33m``[39;49;00m and [33m``[39;49;00m[33m'bar'[39;49;00m[33m``[39;49;00m, and pass the result to the filter$
    84	[31m`escape`[39;49;00m that automatically XML-escapes the value. The [31m`e`[39;49;00m filter is an alias for$
    85	[31m`escape`[39;49;00m. Here is the complete list of supported filters:$
    86	$
    87	[[list_of_filters]]$
    88	$
    89	.. [35madmonition[39;49;00m:: note$
    90	$
    91	    Filters have a pretty low priority. If you want to add fitered values$
    92	    you have to put them into parentheses. The same applies if you want to access$
    93	    attributes:$
    94	$
    95	    .. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
    96	$
    97	        correct:$
    98	            [36m{{[39;49;00m ([31mfoo[39;49;00m|[32mfilter[39;49;00m) + ([31mbar[39;49;00m|[32mfilter[39;49;00m) [36m}}[39;49;00m$
    99	        wrong:$
   100	            [36m{{[39;49;00m [31mfoo[39;49;00m|[32mfilter[39;49;00m + [31mbar[39;49;00m|[32mfilter[39;49;00m [36m}}[39;49;00m$
   101	$
   102	        correct:$
   103	            [36m{{[39;49;00m ([31mfoo[39;49;00m|[32mfilter[39;49;00m)[31m.attribute[39;49;00m [36m}}[39;49;00m$
   104	        wrong:$
   105	            [36m{{[39;49;00m [31mfoo[39;49;00m|[32mfilter[39;49;00m[31m.attribute[39;49;00m [36m}}[39;49;00m$
   106	$
   107	[01mTests[39;49;00m$
   108	[01m=====[39;49;00m$
   109	$
   110	You can use the [31m`is`[39;49;00m operator to perform tests on a value:$
   111	$
   112	.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
   113	$
   114	    [36m{{[39;49;00m [34m4[39;49;00m[34m2[39;49;00m [34mis[39;49;00m [32mnumeric[39;49;00m [36m}}[39;49;00m -> true$
   115	    [36m{{[39;49;00m [33m"foobar"[39;49;00m [34mis[39;49;00m [32mnumeric[39;49;00m [36m}}[39;49;00m -> false$
   116	    [36m{{[39;49;00m [33m'FOO'[39;49;00m [34mis[39;49;00m [32mupper[39;49;00m [36m}}[39;49;00m -> true$
   117	$
   118	These tests are especially useful when used in [31m`if`[39;49;00m conditions.$
   119	$
   120	[[list_of_tests]]$
   121	$
   122	[01mGlobal Functions[39;49;00m$
   123	[01m================[39;49;00m$
   124	$
   125	Test functions and filter functions live in their own namespace. Global$
   126	functions not. They behave like normal objects in the context. Beside the$
   127	functions added by the application or framewhere there are two functions$
   128	available per default:$
   129	$
   130	[31m`range`[39;49;00m$
   131	    $
   132	    Works like the python [33m`range function`_[39;49;00m just that it doesn't support$
   133	    ranges greater than [33m``[39;49;00m[33m1000000[39;49;00m[33m``[39;49;00m.$
   134	$
   135	[31m`debug`[39;49;00m$
   136	$
   137	    Function that outputs the contents of the context.$
   138	$
   139	[01mLoops[39;49;00m$
   140	[01m=====[39;49;00m$
   141	$
   142	To iterate over a sequence, you can use the [31m`for`[39;49;00m loop. It basically looks like a$
   143	normal Python [31m`for`[39;49;00m loop and works pretty much the same:$
   144	$
   145	.. [35msourcecode[39;49;00m:: [34mhtml+jinja[39;49;00m$
   146	$
   147	    <[94mh1[39;49;00m>Members</[94mh1[39;49;00m>$
   148	    <[94mul[39;49;00m>$
   149	    [36m{%[39;49;00m [34mfor[39;49;00m [31muser[39;49;00m [34min[39;49;00m [31musers[39;49;00m [36m%}[39;49;00m$
   150	      <[94mli[39;49;00m>[36m{{[39;49;00m [36mloop[39;49;00m[31m.index[39;49;00m [36m}}[39;49;00m / [36m{{[39;49;00m [36mloop[39;49;00m[31m.length[39;49;00m [36m}}[39;49;00m - [36m{{[39;49;00m [31muser[39;49;00m[31m.username[39;49;00m|[32mescape[39;49;00m [36m}}[39;49;00m</[94mli[39;49;00m>$
   151	    [36m{%[39;49;00m [34melse[39;49;00m [36m%}[39;49;00m$
   152	      <[94mli[39;49;00m><[94mem[39;49;00m>no users found</[94mem[39;49;00m></[94mli[39;49;00m>$
   153	    [36m{%[39;49;00m [34mendfor[39;49;00m [36m%}[39;49;00m$
   154	    </[94mul[39;49;00m>$
   155	$
   156	*Important* Contrary to Python is the optional [33m``[39;49;00m[33melse[39;49;00m[33m``[39;49;00m block only$
   157	executed if there was no iteration because the sequence was empty.$
   158	$
   159	Inside of a [31m`for`[39;49;00m loop block you can access some special variables:$
   160	$
   161	+----------------------+----------------------------------------+$
   162	| Variable             | Description                            |$
   163	+======================+========================================+$
   164	| [31m`loop.index`[39;49;00m         | The current iteration of the loop.     |$
   165	+----------------------+----------------------------------------+$
   166	| [31m`loop.index0`[39;49;00m        | The current iteration of the loop,     |$
   167	|                      | starting counting by 0.                |$
   168	+----------------------+----------------------------------------+$
   169	| [31m`loop.revindex`[39;49;00m      | The number of iterations from the end  |$
   170	|                      | of the loop.                           |$
   171	+----------------------+----------------------------------------+$
   172	| [31m`loop.revindex0`[39;49;00m     | The number of iterations from the end  |$
   173	|                      | of the loop, starting counting by 0.   |$
   174	+----------------------+----------------------------------------+$
   175	| [31m`loop.first`[39;49;00m         | True if first iteration.               |$
   176	+----------------------+----------------------------------------+$
   177	| [31m`loop.last`[39;49;00m          | True if last iteration.                |$
   178	+----------------------+----------------------------------------+$
   179	| [31m`loop.even`[39;49;00m          | True if current iteration is even.     |$
   180	+----------------------+----------------------------------------+$
   181	| [31m`loop.odd`[39;49;00m           | True if current iteration is odd.      |$
   182	+----------------------+----------------------------------------+$
   183	| [31m`loop.length`[39;49;00m        | Total number of items in the sequence. |$
   184	+----------------------+----------------------------------------+$
   185	| [31m`loop.parent`[39;49;00m        | The context of the parent loop.        |$
   186	+----------------------+----------------------------------------+$
   187	$
   188	Loops also support recursion. Let's assume you have a sitemap where each item$
   189	might have a number of child items. A template for that could look like this:$
   190	$
   191	.. [35msourcecode[39;49;00m:: [34mhtml+jinja[39;49;00m$
   192	$
   193	    <[94mh1[39;49;00m>Sitemap$
   194	    <[94mul[39;49;00m [36mid[39;49;00m=[33m"sitemap"[39;49;00m>$
   195	    [36m{%[39;49;00m [34mfor[39;49;00m [31mitem[39;49;00m [34min[39;49;00m [31msitemap[39;49;00m [34mrecursive[39;49;00m [36m%}[39;49;00m$
   196	      <[94mli[39;49;00m><[94ma[39;49;00m [36mhref[39;49;00m=[33m"[39;49;00m[36m{{[39;49;00m [31mitem[39;49;00m[31m.url[39;49;00m|[32me[39;49;00m [36m}}[39;49;00m[33m"[39;49;00m>[36m{{[39;49;00m [31mitem[39;49;00m[31m.title[39;49;00m|[32me[39;49;00m [36m}}[39;49;00m</[94ma[39;49;00m>$
   197	      [36m{%[39;49;00m [34mif[39;49;00m [31mitem[39;49;00m[31m.children[39;49;00m [36m%}[39;49;00m<[94mul[39;49;00m>[36m{{[39;49;00m [36mloop[39;49;00m([31mitem[39;49;00m[31m.children[39;49;00m) [36m}}[39;49;00m</[94mul[39;49;00m>[36m{%[39;49;00m [34mendif[39;49;00m [36m%}[39;49;00m</[94mli[39;49;00m>$
   198	    [36m{%[39;49;00m [34mendfor[39;49;00m [36m%}[39;49;00m$
   199	    </[94mul[39;49;00m>$
   200	$
   201	What happens here? Basically the first thing that is different to a normal$
   202	loop is the additional [33m``[39;49;00m[33mrecursive[39;49;00m[33m``[39;49;00m modifier in the [31m`for`[39;49;00m-loop declaration.$
   203	It tells the template engine that we want recursion. If recursion is enabled$
   204	the special [31m`loop`[39;49;00m variable is callable. If you call it with a sequence it will$
   205	automatically render the loop at that position with the new sequence as argument.$
   206	$
   207	[01mCycling[39;49;00m$
   208	[01m=======[39;49;00m$
   209	$
   210	Sometimes you might want to have different text snippets for each row in a list,$
   211	for example to have alternating row colors. You can easily do this by using the$
   212	[33m``[39;49;00m[33m{% cycle %}[39;49;00m[33m``[39;49;00m tag:$
   213	$
   214	.. [35msourcecode[39;49;00m:: [34mhtml+jinja[39;49;00m$
   215	$
   216	    <[94mul[39;49;00m [36mid[39;49;00m=[33m"messages"[39;49;00m>$
   217	    [36m{%[39;49;00m [34mfor[39;49;00m [31mmessage[39;49;00m [34min[39;49;00m [31mmessages[39;49;00m [36m%}[39;49;00m$
   218	      <[94mli[39;49;00m [36mclass[39;49;00m=[33m"[39;49;00m[36m{%[39;49;00m [34mcycle[39;49;00m [33m'row1'[39;49;00m, [33m'row2'[39;49;00m [36m%}[39;49;00m[33m"[39;49;00m>[36m{{[39;49;00m [31mmessage[39;49;00m|[32me[39;49;00m [36m}}[39;49;00m</[94mli[39;49;00m>$
   219	    [36m{%[39;49;00m [34mendfor[39;49;00m [36m%}[39;49;00m$
   220	    </[94mul[39;49;00m>$
   221	$
   222	Each time Jinja encounters a [31m`cycle`[39;49;00m tag it will cycle through the list$
   223	of given items and return the next one. If you pass it one item jinja assumes$
   224	that this item is a sequence from the context and uses this:$
   225	$
   226	.. [35msourcecode[39;49;00m:: [34mhtml+jinja[39;49;00m$
   227	$
   228	    <[94mli[39;49;00m [36mstyle[39;49;00m=[33m"color: [39;49;00m[36m{%[39;49;00m [34mcycle[39;49;00m [31mrowcolors[39;49;00m [36m%}[39;49;00m[33m"[39;49;00m>...</[94mli[39;49;00m>$
   229	$
   230	[01mConditions[39;49;00m$
   231	[01m==========[39;49;00m$
   232	$
   233	Jinja supports Python-like [31m`if`[39;49;00m / [31m`elif`[39;49;00m / [31m`else`[39;49;00m constructs:$
   234	$
   235	.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
   236	$
   237	    [36m{%[39;49;00m [34mif[39;49;00m [31muser[39;49;00m[31m.active[39;49;00m [36m%}[39;49;00m$
   238	        user [36m{{[39;49;00m [31muser[39;49;00m[31m.name[39;49;00m|[32me[39;49;00m [36m}}[39;49;00m is active.$
   239	    [36m{%[39;49;00m [34melif[39;49;00m [31muser[39;49;00m[31m.deleted[39;49;00m [36m%}[39;49;00m$
   240	        user [36m{{[39;49;00m [31muser[39;49;00m[31m.name[39;49;00m|[32me[39;49;00m [36m}}[39;49;00m was deleted some time ago.$
   241	    [36m{%[39;49;00m [34melse[39;49;00m [36m%}[39;49;00m$
   242	        i don't know what's wrong with [36m{{[39;49;00m [31muser[39;49;00m[31m.username[39;49;00m|[32me[39;49;00m [36m}}[39;49;00m$
   243	    [36m{%[39;49;00m [34mendif[39;49;00m [36m%}[39;49;00m$
   244	$
   245	If the user is active the first block is rendered. If not and the user was$
   246	deleted the second one, in all other cases the third one.$
   247	$
   248	You can also use comparison operators:$
   249	$
   250	.. [35msourcecode[39;49;00m:: [34mhtml+jinja[39;49;00m$
   251	$
   252	    [36m{%[39;49;00m [34mif[39;49;00m [31mamount[39;49;00m < [34m0[39;49;00m [36m%}[39;49;00m$
   253	        <[94mspan[39;49;00m [36mstyle[39;49;00m=[33m"color: red"[39;49;00m>[36m{{[39;49;00m [31mamount[39;49;00m [36m}}[39;49;00m</[94mspan[39;49;00m>$
   254	    [36m{%[39;49;00m [34melse[39;49;00m [36m%}[39;49;00m$
   255	        <[94mspan[39;49;00m [36mstyle[39;49;00m=[33m"color: black"[39;49;00m>[36m{{[39;49;00m [31mamount[39;49;00m [36m}}[39;49;00m</[94mspan[39;49;00m>$
   256	    [36m{%[39;49;00m [34mendif[39;49;00m [36m%}[39;49;00m$
   257	$
   258	.. [35madmonition[39;49;00m:: Note$
   259	$
   260	    Of course you can use [31m`or`[39;49;00m / [31m`and`[39;49;00m and parentheses to create more complex$
   261	    conditions, but usually the logic is already handled in the application and$
   262	    you don't have to create such complex constructs in the template code. However$
   263	    in some situations it might be a good thing to have the abilities to create$
   264	    them.$
   265	$
   266	[01mOperators[39;49;00m$
   267	[01m=========[39;49;00m$
   268	$
   269	Inside [33m``[39;49;00m[33m{{ variable }}[39;49;00m[33m``[39;49;00m blocks, [31m`if`[39;49;00m conditions and many other parts you can$
   270	can use expressions. In expressions you can use any of the following operators:$
   271	$
   272	    ======= ===================================================================$
   273	    [33m``[39;49;00m[33m+[39;49;00m[33m``[39;49;00m   add the right operand to the left one.$
   274	            [33m``[39;49;00m[33m{{ 1 + 2 }}[39;49;00m[33m``[39;49;00m would return [33m``[39;49;00m[33m3[39;49;00m[33m``[39;49;00m.$
   275	    [33m``[39;49;00m[33m-[39;49;00m[33m``[39;49;00m   subtract the right operand from the left one.$
   276	            [33m``[39;49;00m[33m{{ 1 - 1 }}[39;49;00m[33m``[39;49;00m would return [33m``[39;49;00m[33m0[39;49;00m[33m``[39;49;00m.$
   277	    [33m``[39;49;00m[33m/[39;49;00m[33m``[39;49;00m   divide the left operand by the right one.$
   278	            [33m``[39;49;00m[33m{{ 1 / 2 }}[39;49;00m[33m``[39;49;00m would return [33m``[39;49;00m[33m0.5[39;49;00m[33m``[39;49;00m.$
   279	    [33m``[39;49;00m[33m*[39;49;00m[33m``[39;49;00m   multiply the left operand with the right one.$
   280	            [33m``[39;49;00m[33m{{ 2 * 2 }}[39;49;00m[33m``[39;49;00m would return [33m``[39;49;00m[33m4[39;49;00m[33m``[39;49;00m.$
   281	    [33m``[39;49;00m[33m**[39;49;00m[33m``[39;49;00m  raise the left operand to the power of the right$
   282	            operand. [33m``[39;49;00m[33m{{ 2**3 }}[39;49;00m[33m``[39;49;00m would return [33m``[39;49;00m[33m8[39;49;00m[33m``[39;49;00m.$
   283	    [33m``[39;49;00m[33min[39;49;00m[33m``[39;49;00m  perform sequence membership test. [33m``[39;49;00m[33m{{ 1 in [1,2,3] }}[39;49;00m[33m``[39;49;00m would$
   284	            return true.$
   285	    [33m``[39;49;00m[33mis[39;49;00m[33m``[39;49;00m  perform a test on the value. See the section about$
   286	            tests for more information.$
   287	    [33m``[39;49;00m[33m|[39;49;00m[33m``[39;49;00m   apply a filter on the value. See the section about$
   288	            filters for more information.$
   289	    [33m``[39;49;00m[33mand[39;49;00m[33m``[39;49;00m return true if the left and the right operand is true.$
   290	    [33m``[39;49;00m[33mor[39;49;00m[33m``[39;49;00m  return true if the left or the right operand is true.$
   291	    [33m``[39;49;00m[33mnot[39;49;00m[33m``[39;49;00m negate a statement (see below)$
   292	    [33m``[39;49;00m[33m()[39;49;00m[33m``[39;49;00m  call a callable: [33m``[39;49;00m[33m{{ user.get_username() }}[39;49;00m[33m``[39;49;00m. Inside of the$
   293	            parentheses you can use variables: [33m``[39;49;00m[33m{{ user.get(username) }}[39;49;00m[33m``[39;49;00m.$
   294	    ======= ===================================================================$
   295	$
   296	Note that there is no support for any bit operations or something similar.$
   297	$
   298	[34m*[39;49;00m special note regarding [31m`not`[39;49;00m: The [31m`is`[39;49;00m and [31m`in`[39;49;00m operators support negation$
   299	  using an infix notation too: [33m``[39;49;00m[33mfoo is not bar[39;49;00m[33m``[39;49;00m and [33m``[39;49;00m[33mfoo not in bar[39;49;00m[33m``[39;49;00m$
   300	  instead of [33m``[39;49;00m[33mnot foo is bar[39;49;00m[33m``[39;49;00m and [33m``[39;49;00m[33mnot foo in bar[39;49;00m[33m``[39;49;00m. All other expressions$
   301	  require a prefix notation: [33m``[39;49;00m[33mnot (foo and bar)[39;49;00m[33m``[39;49;00m.$
   302	$
   303	[01mBoolean Values[39;49;00m$
   304	[01m==============[39;49;00m$
   305	$
   306	In If-Conditions Jinja performs a boolean check. All empty values (eg: empty$
   307	lists [33m``[39;49;00m[33m[][39;49;00m[33m``[39;49;00m, empty dicts [33m``[39;49;00m[33m{}[39;49;00m[33m``[39;49;00m etc) evaluate to [31m`false`[39;49;00m. Numbers that are$
   308	equal to [31m`0`[39;49;00m/[31m`0.00`[39;49;00m are considered [31m`false`[39;49;00m too. The boolean value of other$
   309	objects depends on the behavior the application developer gave it. Usually$
   310	items are [31m`true`[39;49;00m.$
   311	$
   312	Here some examples that should explain it:$
   313	$
   314	.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
   315	$
   316	    [36m{%[39;49;00m [34mif[39;49;00m [] [36m%}[39;49;00m$
   317	        will always be false because it's an empty list$
   318	$
   319	    [36m{%[39;49;00m [34mif[39;49;00m {} [36m%}[39;49;00m$
   320	        false too.$
   321	$
   322	    [36m{%[39;49;00m [34mif[39;49;00m [[33m'foo'[39;49;00m] [36m%}[39;49;00m$
   323	        this is true. Because the list is not empty.$
   324	$
   325	    [36m{%[39;49;00m [34mif[39;49;00m [33m"foobar"[39;49;00m [36m%}[39;49;00m$
   326	        this is also true because the string is not empty.$
   327	$
   328	[01mSlicing[39;49;00m$
   329	[01m=======[39;49;00m$
   330	$
   331	Some objects support slicing operations. For example lists:$
   332	$
   333	.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
   334	$
   335	    [36m{%[39;49;00m [34mfor[39;49;00m [31mitem[39;49;00m [34min[39;49;00m [31mitems[39;49;00m[:[34m5[39;49;00m] [36m%}[39;49;00m$
   336	        This will only iterate over the first 5 items of the list$
   337	$
   338	    [36m{%[39;49;00m [34mfor[39;49;00m [31mitem[39;49;00m [34min[39;49;00m [31mitems[39;49;00m[[34m5[39;49;00m:[34m1[39;49;00m[34m0[39;49;00m] [36m%}[39;49;00m$
   339	        This will only iterate from item 5 to 10.$
   340	$
   341	    [36m{%[39;49;00m [34mfor[39;49;00m [31mitem[39;49;00m [34min[39;49;00m [31mitems[39;49;00m[:[34m1[39;49;00m[34m0[39;49;00m:[34m2[39;49;00m] [36m%}[39;49;00m$
   342	        This will only yield items from start to ten and only returing$
   343	        even items.$
   344	$
   345	For more informations about slicing have a look at the [33m`slicing chapter`_[39;49;00m$
   346	in the "Dive into Python" e-book.$
   347	$
   348	[01mMacros[39;49;00m$
   349	[01m======[39;49;00m$
   350	$
   351	If you want to use a partial template in more than one place, you might want to$
   352	create a macro from it:$
   353	$
   354	.. [35msourcecode[39;49;00m:: [34mhtml+jinja[39;49;00m$
   355	$
   356	    [36m{%[39;49;00m [34mmacro[39;49;00m [31mshow_user[39;49;00m [31muser[39;49;00m [36m%}[39;49;00m$
   357	      <[94mh1[39;49;00m>[36m{{[39;49;00m [31muser[39;49;00m[31m.name[39;49;00m|[32me[39;49;00m [36m}}[39;49;00m</[94mh1[39;49;00m>$
   358	      <[94mdiv[39;49;00m [36mclass[39;49;00m=[33m"test"[39;49;00m>$
   359	        [36m{{[39;49;00m [31muser[39;49;00m[31m.description[39;49;00m [36m}}[39;49;00m$
   360	      </[94mdiv[39;49;00m>$
   361	    [36m{%[39;49;00m [34mendmacro[39;49;00m [36m%}[39;49;00m$
   362	$
   363	Now you can use it from everywhere in the code by passing it an item:$
   364	$
   365	.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
   366	    $
   367	    [36m{%[39;49;00m [34mfor[39;49;00m [31muser[39;49;00m [34min[39;49;00m [31musers[39;49;00m [36m%}[39;49;00m$
   368	        [36m{{[39;49;00m [31mshow_user[39;49;00m([31muser[39;49;00m) [36m}}[39;49;00m$
   369	    [36m{%[39;49;00m [34mendfor[39;49;00m [36m%}[39;49;00m$
   370	$
   371	You can also specify more than one value:$
   372	$
   373	.. [35msourcecode[39;49;00m:: [34mhtml+jinja[39;49;00m$
   374	$
   375	    [36m{%[39;49;00m [34mmacro[39;49;00m [31mshow_dialog[39;49;00m [31mtitle[39;49;00m, [31mtext[39;49;00m [36m%}[39;49;00m$
   376	      <[94mdiv[39;49;00m [36mclass[39;49;00m=[33m"dialog"[39;49;00m>$
   377	        <[94mh1[39;49;00m>[36m{{[39;49;00m [31mtitle[39;49;00m|[32me[39;49;00m [36m}}[39;49;00m</[94mh1[39;49;00m>$
   378	        <[94mdiv[39;49;00m [36mclass[39;49;00m=[33m"test"[39;49;00m>[36m{{[39;49;00m [31mtext[39;49;00m|[32me[39;49;00m [36m}}[39;49;00m</[94mdiv[39;49;00m>$
   379	      </[94mdiv[39;49;00m>$
   380	    [36m{%[39;49;00m [34mendmacro[39;49;00m [36m%}[39;49;00m$
   381	$
   382	    [36m{{[39;49;00m [31mshow_dialog[39;49;00m([33m'Warning'[39;49;00m, [33m'something went wrong i guess'[39;49;00m) [36m}}[39;49;00m$
   383	$
   384	[01mInheritance[39;49;00m$
   385	[01m===========[39;49;00m$
   386	$
   387	The most powerful part of Jinja is template inheritance. Template inheritance$
   388	allows you to build a base "skeleton" template that contains all the common$
   389	elements of your site and defines **blocks** that child templates can override.$
   390	$
   391	Sounds complicated but is very basic. It's easiest to understand it by starting$
   392	with an example.$
   393	$
   394	[01mBase Template[39;49;00m$
   395	[01m-------------[39;49;00m$
   396	$
   397	This template, which we'll call [33m``[39;49;00m[33mbase.html[39;49;00m[33m``[39;49;00m, defines a simple HTML skeleton$
   398	document that you might use for a simple two-column page. It's the job of$
   399	"child" templates to fill the empty blocks with content:$
   400	$
   401	.. [35msourcecode[39;49;00m:: [34mhtml+jinja[39;49;00m$
   402	$
   403	    [36m<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"[39;49;00m$
   404	    [36m "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">[39;49;00m$
   405	    <[94mhtml[39;49;00m [36mxmlns[39;49;00m=[33m"http://www.w3.org/1999/xhtml"[39;49;00m>$
   406	    <[94mhead[39;49;00m>$
   407	      <[94mlink[39;49;00m [36mrel[39;49;00m=[33m"stylesheet"[39;49;00m [36mhref[39;49;00m=[33m"style.css"[39;49;00m />$
   408	      <[94mtitle[39;49;00m>[36m{%[39;49;00m [34mblock[39;49;00m [31mtitle[39;49;00m [36m%}[39;49;00m[36m{%[39;49;00m [34mendblock[39;49;00m [36m%}[39;49;00m - My Webpage</[94mtitle[39;49;00m>$
   409	      [36m{%[39;49;00m [34mblock[39;49;00m [31mhtml_head[39;49;00m [36m%}[39;49;00m[36m{%[39;49;00m [34mendblock[39;49;00m [36m%}[39;49;00m$
   410	    </[94mhead[39;49;00m>$
   411	    <[94mbody[39;49;00m>$
   412	      <[94mdiv[39;49;00m [36mid[39;49;00m=[33m"content"[39;49;00m>$
   413	        [36m{%[39;49;00m [34mblock[39;49;00m [31mcontent[39;49;00m [36m%}[39;49;00m[36m{%[39;49;00m [34mendblock[39;49;00m [36m%}[39;49;00m$
   414	      </[94mdiv[39;49;00m>$
   415	$
   416	      <[94mdiv[39;49;00m [36mid[39;49;00m=[33m"footer"[39;49;00m>$
   417	        [36m{%[39;49;00m [34mblock[39;49;00m [31mfooter[39;49;00m [36m%}[39;49;00m$
   418	        &copy; Copyright 2006 by <[94ma[39;49;00m [36mhref[39;49;00m=[33m"http://mydomain.tld"[39;49;00m>myself</[94ma[39;49;00m>.$
   419	        [36m{%[39;49;00m [34mendblock[39;49;00m [36m%}[39;49;00m$
   420	      </[94mdiv[39;49;00m>$
   421	    </[94mbody[39;49;00m>$
   422	$
   423	In this example, the [33m``[39;49;00m[33m{% block %}[39;49;00m[33m``[39;49;00m tags define four blocks that child templates$
   424	can fill in. All the [31m`block`[39;49;00m tag does is to tell the template engine that a$
   425	child template may override those portions of the template.$
   426	$
   427	[01mChild Template[39;49;00m$
   428	[01m--------------[39;49;00m$
   429	$
   430	A child template might look like this:$
   431	$
   432	.. [35msourcecode[39;49;00m:: [34mhtml+jinja[39;49;00m$
   433	$
   434	    [36m{%[39;49;00m [34mextends[39;49;00m [33m"base.html"[39;49;00m [36m%}[39;49;00m$
   435	    [36m{%[39;49;00m [34mblock[39;49;00m [31mtitle[39;49;00m [36m%}[39;49;00mIndex[36m{%[39;49;00m [34mendblock[39;49;00m [36m%}[39;49;00m$
   436	$
   437	    [36m{%[39;49;00m [34mblock[39;49;00m [31mhtml_head[39;49;00m [36m%}[39;49;00m$
   438	      <[94mstyle[39;49;00m [36mtype[39;49;00m=[33m"text/css"[39;49;00m>[37m[39;49;00m$
   439	    [37m    [39;49;00m.[04m[32mimportant[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
   440	    [37m      [39;49;00m[34mcolor[39;49;00m:[37m [39;49;00m[34m#336699[39;49;00m;[37m[39;49;00m$
   441	    [37m    [39;49;00m}[37m[39;49;00m$
   442	    [37m  [39;49;00m</[94mstyle[39;49;00m>$
   443	    [36m{%[39;49;00m [34mendblock[39;49;00m [36m%}[39;49;00m$
   444	    $
   445	    [36m{%[39;49;00m [34mblock[39;49;00m [31mcontent[39;49;00m [36m%}[39;49;00m$
   446	        <[94mh1[39;49;00m>Index</[94mh1[39;49;00m>$
   447	        <[94mp[39;49;00m [36mclass[39;49;00m=[33m"important"[39;49;00m>$
   448	          Welcome on my awsome homepage.$
   449	        </[94mp[39;49;00m>$
   450	    [36m{%[39;49;00m [34mendblock[39;49;00m [36m%}[39;49;00m$
   451	$
   452	The [33m``[39;49;00m[33m{% extends %}[39;49;00m[33m``[39;49;00m tag is the key here. It tells the template engine that$
   453	this template "extends" another template. When the template system evaluates$
   454	this template, first it locates the parent.$
   455	$
   456	The filename of the template depends on the template loader. For example the$
   457	[33m``[39;49;00m[33mFileSystemLoader[39;49;00m[33m``[39;49;00m allows you to access other templates by giving the$
   458	filename. You can access templates in subdirectories with an slash:$
   459	$
   460	.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
   461	$
   462	    [36m{%[39;49;00m [34mextends[39;49;00m [33m"layout/default.html"[39;49;00m [36m%}[39;49;00m$
   463	$
   464	But this behavior can depend on the application using Jinja.$
   465	$
   466	Note that since the child template didn't define the [33m``[39;49;00m[33mfooter[39;49;00m[33m``[39;49;00m block, the$
   467	value from the parent template is used instead.$
   468	$
   469	.. [35madmonition[39;49;00m:: Note$
   470	$
   471	    You can't define multiple [33m``[39;49;00m[33m{% block %}[39;49;00m[33m``[39;49;00m tags with the same name in the$
   472	    same template. This limitation exists because a block tag works in "both"$
   473	    directions. That is, a block tag doesn't just provide a hole to fill - it$
   474	    also defines the content that fills the hole in the *parent*. If there were$
   475	    two similarly-named [33m``[39;49;00m[33m{% block %}[39;49;00m[33m``[39;49;00m tags in a template, that template's$
   476	    parent wouldn't know which one of the blocks' content to use.$
   477	$
   478	[01mTemplate Inclusion[39;49;00m$
   479	[01m==================[39;49;00m$
   480	$
   481	You can load another template at a given position using [33m``[39;49;00m[33m{% include %}[39;49;00m[33m``[39;49;00m.$
   482	Usually it's a better idea to use inheritance but if you for example want to$
   483	load macros, [31m`include`[39;49;00m works better than [31m`extends`[39;49;00m:$
   484	$
   485	.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
   486	$
   487	    [36m{%[39;49;00m [34minclude[39;49;00m [33m"myhelpers.html"[39;49;00m [36m%}[39;49;00m$
   488	    [36m{{[39;49;00m [31mmy_helper[39;49;00m([33m"foo"[39;49;00m) [36m}}[39;49;00m$
   489	$
   490	If you define a macro called [33m``[39;49;00m[33mmy_helper[39;49;00m[33m``[39;49;00m in [33m``[39;49;00m[33mmyhelpers.html[39;49;00m[33m``[39;49;00m, you can now$
   491	use it from the template as shown above.$
   492	$
   493	[01mFiltering Blocks[39;49;00m$
   494	[01m================[39;49;00m$
   495	$
   496	Sometimes it could be a good idea to filter a complete block of text. For$
   497	example, if you want to escape some html code:$
   498	$
   499	.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
   500	$
   501	    [36m{%[39;49;00m [34mfilter[39;49;00m [32mescape[39;49;00m [36m%}[39;49;00m$
   502	        <html>$
   503	          <code>goes here</code>$
   504	        </html>$
   505	    [36m{%[39;49;00m [34mendfilter[39;49;00m [36m%}[39;49;00m$
   506	$
   507	Of course you can chain filters too:$
   508	$
   509	.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
   510	$
   511	    [36m{%[39;49;00m [34mfilter[39;49;00m [32mlower[39;49;00m|[32mescape[39;49;00m [36m%}[39;49;00m$
   512	        <B>SOME TEXT</B>$
   513	    [36m{%[39;49;00m [34mendfilter[39;49;00m [36m%}[39;49;00m$
   514	$
   515	returns [33m``[39;49;00m[33m"&lt;b&gt;some text&lt;/b&gt;"[39;49;00m[33m``[39;49;00m.$
   516	$
   517	[01mDefining Variables[39;49;00m$
   518	[01m==================[39;49;00m$
   519	$
   520	You can also define variables in the namespace using the [33m``[39;49;00m[33m{% set %}[39;49;00m[33m``[39;49;00m tag:$
   521	$
   522	.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
   523	$
   524	    [36m{%[39;49;00m [34mset[39;49;00m [31mfoo[39;49;00m = [33m'foobar'[39;49;00m [36m%}[39;49;00m$
   525	    [36m{{[39;49;00m [31mfoo[39;49;00m [36m}}[39;49;00m$
   526	$
   527	This should ouput [33m``[39;49;00m[33mfoobar[39;49;00m[33m``[39;49;00m.$
   528	$
   529	[01mScopes[39;49;00m$
   530	[01m======[39;49;00m$
   531	$
   532	Jinja has multiple scopes. A scope is something like a new transparent foil on$
   533	a stack of foils. You can only write to the outermost foil but read all of them$
   534	since you can look through them. If you remove the top foil all data on that$
   535	foil disappears. Some tags in Jinja add a new layer to the stack. Currently$
   536	these are [31m`block`[39;49;00m, [31m`for`[39;49;00m, [31m`macro`[39;49;00m and [31m`filter`[39;49;00m. This means that variables and$
   537	other elements defined inside a macro, loop or some of the other tags listed$
   538	above will be only available in that block. Here an example:$
   539	$
   540	.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
   541	$
   542	    [36m{%[39;49;00m [34mmacro[39;49;00m [31mangryhello[39;49;00m [31mname[39;49;00m [36m%}[39;49;00m$
   543	      [36m{%[39;49;00m [34mset[39;49;00m [31mangryname[39;49;00m = [31mname[39;49;00m|[32mupper[39;49;00m [36m%}[39;49;00m$
   544	      Hello [36m{{[39;49;00m [31mname[39;49;00m [36m}}[39;49;00m. Hello [36m{{[39;49;00m [31mname[39;49;00m [36m}}[39;49;00m!$
   545	      HELLO [36m{{[39;49;00m [31mangryname[39;49;00m [36m}}[39;49;00m!!!!!!111$
   546	    [36m{%[39;49;00m [34mendmacro[39;49;00m [36m%}[39;49;00m$
   547	$
   548	The variable [33m``[39;49;00m[33mangryname[39;49;00m[33m``[39;49;00m just exists inside the macro, not outside it.$
   549	$
   550	Defined macros appear on the context as variables. Because of this, they are$
   551	affected by the scoping too. A macro defined inside of a macro is just available$
   552	in those two macros (the macro itself and the macro it's defined in). For [31m`set`[39;49;00m$
   553	and [31m`macro`[39;49;00m two additional rules exist: If a macro is defined in an extended$
   554	template but outside of a visible block (thus outside of any block) will be$
   555	available in all blocks below. This allows you to use [31m`include`[39;49;00m statements to$
   556	load often used macros at once.$
   557	$
   558	[01mUndefined Variables[39;49;00m$
   559	[01m===================[39;49;00m$
   560	$
   561	If you have already worked with python you probably know about the fact that$
   562	undefined variables raise an exception. This is different in Jinja. There is a$
   563	special value called [31m`undefined`[39;49;00m that represents values that do not exist.$
   564	$
   565	This special variable works complete different from any variables you maybe$
   566	know. If you print it using [33m``[39;49;00m[33m{{ variable }}[39;49;00m[33m``[39;49;00m it will not appear because it's$
   567	literally empty. If you try to iterate over it, it will work. But no items$
   568	are returned. Comparing this value to any other value results in [31m`false`[39;49;00m.$
   569	Even if you compare it to itself:$
   570	$
   571	.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
   572	$
   573	    [36m{{[39;49;00m [31mundefined[39;49;00m == [31mundefined[39;49;00m [36m}}[39;49;00m$
   574	        will return false. Not even undefined is undefined :)$
   575	        Use `is defined` / `is not defined`:$
   576	$
   577	    [36m{{[39;49;00m [31mundefined[39;49;00m [34mis[39;49;00m [34mnot[39;49;00m [32mdefined[39;49;00m [36m}}[39;49;00m$
   578	        will return true.$
   579	$
   580	There are also some additional rules regarding this special value. Any$
   581	mathematical operators ([33m``[39;49;00m[33m+[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33m-[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33m*[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33m/[39;49;00m[33m``[39;49;00m) return the operand$
   582	as result:$
   583	$
   584	.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
   585	$
   586	    [36m{{[39;49;00m [31mundefined[39;49;00m + [33m"foo"[39;49;00m [36m}}[39;49;00m$
   587	        returns "foo"$
   588	$
   589	    [36m{{[39;49;00m [31mundefined[39;49;00m - [34m4[39;49;00m[34m2[39;49;00m [36m}}[39;49;00m$
   590	        returns 42. Note: not -42!$
   591	$
   592	In any expression [31m`undefined`[39;49;00m evaluates to [31m`false`[39;49;00m. It has no length, all$
   593	attribute calls return undefined, calling too:$
   594	$
   595	.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
   596	$
   597	    [36m{{[39;49;00m [31mundefined[39;49;00m[31m.attribute[39;49;00m()[31m.attribute_too[39;49;00m[[34m4[39;49;00m[34m2[39;49;00m] [36m}}[39;49;00m$
   598	        still returns `undefined`.$
   599	$
   600	[01mEscaping[39;49;00m$
   601	[01m========[39;49;00m$
   602	$
   603	Sometimes you might want to add Jinja syntax elements into the template$
   604	without executing them. In that case you have quite a few possibilities.$
   605	$
   606	For small parts this might be a good way:$
   607	$
   608	.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
   609	$
   610	    [36m{{[39;49;00m [33m"{{ foo }} is variable syntax and {% foo %} is block syntax"[39;49;00m [36m}}[39;49;00m$
   611	$
   612	When you have multiple elements you can use the [33m``[39;49;00m[33mraw[39;49;00m[33m``[39;49;00m block:$
   613	$
   614	.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
   615	$
   616	    [36m{%[39;49;00m [34mraw[39;49;00m [36m%}[39;49;00m$
   617	        Filtering blocks works like this in Jinja:$
   618	        {% filter escape %}$
   619	            <html>$
   620	              <code>goes here</code>$
   621	            </html>$
   622	        {% endfilter %}$
   623	    [36m{%[39;49;00m [34mendraw[39;49;00m [36m%}[39;49;00m$
   624	$
   625	[01mReserved Keywords[39;49;00m$
   626	[01m=================[39;49;00m$
   627	$
   628	Jinja has some keywords you cannot use a variable names. This limitation$
   629	exists to make look coherent. Syntax highlighters won't mess things up and$
   630	you will don't have unexpected output.$
   631	$
   632	The following keywords exist and cannot be used as identifiers:$
   633	$
   634	    [31m`and`[39;49;00m, [31m`block`[39;49;00m, [31m`cycle`[39;49;00m, [31m`elif`[39;49;00m, [31m`else`[39;49;00m, [31m`endblock`[39;49;00m, [31m`endfilter`[39;49;00m,$
   635	    [31m`endfor`[39;49;00m, [31m`endif`[39;49;00m, [31m`endmacro`[39;49;00m, [31m`endraw`[39;49;00m, [31m`endtrans`[39;49;00m, [31m`extends`[39;49;00m, [31m`filter`[39;49;00m,$
   636	    [31m`for`[39;49;00m, [31m`if`[39;49;00m, [31m`in`[39;49;00m, [31m`include`[39;49;00m, [31m`is`[39;49;00m, [31m`macro`[39;49;00m, [31m`not`[39;49;00m, [31m`or`[39;49;00m, [31m`pluralize`[39;49;00m,$
   637	    [31m`raw`[39;49;00m, [31m`recursive`[39;49;00m, [31m`set`[39;49;00m, [31m`trans`[39;49;00m$
   638	$
   639	If you want to use such a name you have to prefix or suffix it or use$
   640	alternative names:$
   641	$
   642	.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
   643	$
   644	    [36m{%[39;49;00m [34mfor[39;49;00m [31mmacro_[39;49;00m [34min[39;49;00m [31mmacros[39;49;00m [36m%}[39;49;00m$
   645	        [36m{{[39;49;00m [31mmacro_[39;49;00m([33m'foo'[39;49;00m) [36m}}[39;49;00m$
   646	    [36m{%[39;49;00m [34mendfor[39;49;00m [36m%}[39;49;00m$
   647	$
   648	If future Jinja releases add new keywords those will be "light" keywords which$
   649	means that they won't raise an error for several releases but yield warnings$
   650	on the application side. But it's very unlikely that new keywords will be$
   651	added.$
   652	$
   653	[01mInternationalization[39;49;00m$
   654	[01m====================[39;49;00m$
   655	$
   656	If the application is configured for i18n, you can define translatable blocks$
   657	for translators using the [31m`trans`[39;49;00m tag or the special underscore function:$
   658	$
   659	.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
   660	$
   661	    [36m{%[39;49;00m [34mtrans[39;49;00m [36m%}[39;49;00m$
   662	        this is a translatable block$
   663	    [36m{%[39;49;00m [34mendtrans[39;49;00m [36m%}[39;49;00m$
   664	$
   665	    [36m{%[39;49;00m [34mtrans[39;49;00m [33m"This is a translatable string"[39;49;00m [36m%}[39;49;00m$
   666	$
   667	    [36m{{[39;49;00m [34m_[39;49;00m([33m"This is a translatable string"[39;49;00m) [36m}}[39;49;00m$
   668	$
   669	The latter one is useful if you want translatable arguments for filters etc.$
   670	$
   671	If you want to have plural forms too, use the [31m`pluralize`[39;49;00m block:$
   672	$
   673	.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
   674	$
   675	    [36m{%[39;49;00m [34mtrans[39;49;00m [31musers[39;49;00m=[31musers[39;49;00m [36m%}[39;49;00m$
   676	        One user found.$
   677	    [36m{%[39;49;00m [34mpluralize[39;49;00m [36m%}[39;49;00m$
   678	        [36m{{[39;49;00m [31musers[39;49;00m [36m}}[39;49;00m users found.$
   679	    [36m{%[39;49;00m [34mendtrans[39;49;00m [36m%}[39;49;00m$
   680	$
   681	    [36m{%[39;49;00m [34mtrans[39;49;00m [31mfirst[39;49;00m=([31musers[39;49;00m|[32mfirst[39;49;00m)[31m.username[39;49;00m|[32mescape[39;49;00m, [31muser[39;49;00m=[31musers[39;49;00m|[32mlength[39;49;00m [36m%}[39;49;00m$
   682	        one user [36m{{[39;49;00m [31mfirst[39;49;00m [36m}}[39;49;00m found.$
   683	    [36m{%[39;49;00m [34mpluralize[39;49;00m [31musers[39;49;00m [36m%}[39;49;00m$
   684	        [36m{{[39;49;00m [31musers[39;49;00m [36m}}[39;49;00m users found, the first one is called [36m{{[39;49;00m [31mfirst[39;49;00m [36m}}[39;49;00m.$
   685	    [36m{%[39;49;00m [34mendtrans[39;49;00m [36m%}[39;49;00m$
   686	$
   687	If you have multiple arguments, the first one is assumed to be the indicator (the$
   688	number that is used to determine the correct singular or plural form. If you$
   689	don't have the indicator variable on position 1 you have to tell the [31m`pluralize`[39;49;00m$
   690	tag the correct variable name.$
   691	$
   692	Inside translatable blocks you cannot use blocks or expressions (however you can$
   693	still use the [33m``[39;49;00m[33mraw[39;49;00m[33m``[39;49;00m block which will work as expected). The variable$
   694	print syntax ([33m``[39;49;00m[33m{{ variablename }}[39;49;00m[33m``[39;49;00m) is the only way to insert the variables$
   695	defined in the [33m``[39;49;00m[33mtrans[39;49;00m[33m``[39;49;00m header. Filters must be applied in the header.$
   696	$
   697	.. [35madmonition[39;49;00m:: note$
   698	$
   699	    Please make sure that you always use pluralize blocks where required.$
   700	    Many languages have more complex plural forms than the English language.$
   701	    $
   702	    Never try to workaround that issue by using something like this:$
   703	$
   704	    .. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
   705	$
   706	        [36m{%[39;49;00m [34mif[39;49;00m [31mcount[39;49;00m != [34m1[39;49;00m [36m%}[39;49;00m$
   707	            [36m{{[39;49;00m [31mcount[39;49;00m [36m}}[39;49;00m users found.$
   708	        [36m{%[39;49;00m [34melse[39;49;00m [36m%}[39;49;00m$
   709	            one user found.$
   710	        [36m{%[39;49;00m [34mendif[39;49;00m [36m%}[39;49;00m$
   711	$
   712	.. [94m_slicing chapter:[39;49;00m http://diveintopython.org/native_data_types/lists.html#odbchelper.list.slice$
   713	.. [94m_range function:[39;49;00m http://docs.python.org/tut/node6.html#SECTION006300000000000000000$

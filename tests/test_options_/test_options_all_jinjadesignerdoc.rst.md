     1^I[01m======================[39;49;00m$
     2^I[01mDesigner Documentation[39;49;00m$
     3^I[01m======================[39;49;00m$
     4^I$
     5^IThis part of the Jinja documentaton is meant for template designers.$
     6^I$
     7^I[01mBasics[39;49;00m$
     8^I[01m======[39;49;00m$
     9^I$
    10^IThe Jinja template language is designed to strike a balance between content$
    11^Iand application logic. Nevertheless you can use a python like statement$
    12^Ilanguage. You don't have to know how Python works to create Jinja templates,$
    13^Ibut if you know it you can use some additional statements you may know from$
    14^IPython.$
    15^I$
    16^IHere is a small example template:$
    17^I$
    18^I.. [35msourcecode[39;49;00m:: [34mhtml+jinja[39;49;00m$
    19^I$
    20^I    [36m<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"[39;49;00m$
    21^I    [36m "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">[39;49;00m$
    22^I    <[94mhtml[39;49;00m [36mxmlns[39;49;00m=[33m"http://www.w3.org/1999/xhtml"[39;49;00m [36mlang[39;49;00m=[33m"en"[39;49;00m [36mxml:lang[39;49;00m=[33m"en"[39;49;00m>$
    23^I    <[94mhead[39;49;00m>$
    24^I        <[94mtitle[39;49;00m>My Webpage</[94mtitle[39;49;00m>$
    25^I    </[94mhead[39;49;00m>$
    26^I    <[94mbody[39;49;00m>$
    27^I        <[94mul[39;49;00m [36mid[39;49;00m=[33m"navigation"[39;49;00m>$
    28^I        [36m{%[39;49;00m [34mfor[39;49;00m [31mitem[39;49;00m [34min[39;49;00m [31mnavigation[39;49;00m [36m%}[39;49;00m$
    29^I            <[94mli[39;49;00m><[94ma[39;49;00m [36mhref[39;49;00m=[33m"[39;49;00m[36m{{[39;49;00m [31mitem[39;49;00m[31m.href[39;49;00m|[32me[39;49;00m [36m}}[39;49;00m[33m"[39;49;00m>[36m{{[39;49;00m [31mitem[39;49;00m[31m.caption[39;49;00m|[32me[39;49;00m [36m}}[39;49;00m</[94ma[39;49;00m></[94mli[39;49;00m>$
    30^I        [36m{%[39;49;00m [34mendfor[39;49;00m [36m%}[39;49;00m$
    31^I        </[94mul[39;49;00m>$
    32^I$
    33^I        <[94mh1[39;49;00m>My Webpage</[94mh1[39;49;00m>$
    34^I        [36m{{[39;49;00m [31mvariable[39;49;00m [36m}}[39;49;00m$
    35^I    </[94mbody[39;49;00m>$
    36^I    </[94mhtml[39;49;00m>$
    37^I$
    38^IThis covers the default settings. The application developer might have changed$
    39^Ithe syntax from [33m``[39;49;00m[33m{% foo %}[39;49;00m[33m``[39;49;00m to [33m``[39;49;00m[33m<% foo %>[39;49;00m[33m``[39;49;00m or something similar. This$
    40^Idocumentation just covers the default values.$
    41^I$
    42^IA variable looks like [33m``[39;49;00m[33m{{ foobar }}[39;49;00m[33m``[39;49;00m where foobar is the variable name. Inside$
    43^Iof statements ([33m``[39;49;00m[33m{% some content here %}[39;49;00m[33m``[39;49;00m) variables are just normal names$
    44^Iwithout the braces around it. In fact [33m``[39;49;00m[33m{{ foobar }}[39;49;00m[33m``[39;49;00m is just an alias for$
    45^Ithe statement [33m``[39;49;00m[33m{% print foobar %}[39;49;00m[33m``[39;49;00m.$
    46^I$
    47^IVariables are coming from the context provided by the application. Normally there$
    48^Ishould be a documentation regarding the context contents but if you want to know$
    49^Ithe content of the current context, you can add this to your template:$
    50^I$
    51^I.. [35msourcecode[39;49;00m:: [34mhtml+jinja[39;49;00m$
    52^I$
    53^I    <[94mpre[39;49;00m>[36m{{[39;49;00m [31mdebug[39;49;00m()|[32me[39;49;00m [36m}}[39;49;00m</[94mpre[39;49;00m>$
    54^I$
    55^IA context isn't flat which means that each variable can has subvariables, as long$
    56^Ias it is representable as python data structure. You can access attributes of$
    57^Ia variable using the dot and bracket operators. The following examples show$
    58^Ithis:$
    59^I$
    60^I.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
    61^I$
    62^I    [36m{{[39;49;00m [31muser[39;49;00m[31m.username[39;49;00m [36m}}[39;49;00m$
    63^I        is the same as$
    64^I    [36m{{[39;49;00m [31muser[39;49;00m[[33m'username'[39;49;00m] [36m}}[39;49;00m$
    65^I        you can also use a variable to access an attribute:$
    66^I    [36m{{[39;49;00m [31musers[39;49;00m[[31mcurrent_user[39;49;00m][31m.username[39;49;00m [36m}}[39;49;00m$
    67^I        If you have numerical indices you have to use the [] syntax:$
    68^I    [36m{{[39;49;00m [31musers[39;49;00m[[34m0[39;49;00m][31m.username[39;49;00m [36m}}[39;49;00m$
    69^I$
    70^I[01mFilters[39;49;00m$
    71^I[01m=======[39;49;00m$
    72^I$
    73^IIn the examples above you might have noticed the pipe symbols. Pipe symbols tell$
    74^Ithe engine that it has to apply a filter on the variable. Here is a small example:$
    75^I$
    76^I.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
    77^I$
    78^I    [36m{{[39;49;00m [31mvariable[39;49;00m|[32mreplace[39;49;00m([33m'foo'[39;49;00m, [33m'bar'[39;49;00m)|[32mescape[39;49;00m [36m}}[39;49;00m$
    79^I$
    80^IIf you want, you can also put whitespace between the filters.$
    81^I$
    82^IThis will look for a variable [31m`variable`[39;49;00m, pass it to the filter [31m`replace`[39;49;00m$
    83^Iwith the arguments [33m``[39;49;00m[33m'foo'[39;49;00m[33m``[39;49;00m and [33m``[39;49;00m[33m'bar'[39;49;00m[33m``[39;49;00m, and pass the result to the filter$
    84^I[31m`escape`[39;49;00m that automatically XML-escapes the value. The [31m`e`[39;49;00m filter is an alias for$
    85^I[31m`escape`[39;49;00m. Here is the complete list of supported filters:$
    86^I$
    87^I[[list_of_filters]]$
    88^I$
    89^I.. [35madmonition[39;49;00m:: note$
    90^I$
    91^I    Filters have a pretty low priority. If you want to add fitered values$
    92^I    you have to put them into parentheses. The same applies if you want to access$
    93^I    attributes:$
    94^I$
    95^I    .. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
    96^I$
    97^I        correct:$
    98^I            [36m{{[39;49;00m ([31mfoo[39;49;00m|[32mfilter[39;49;00m) + ([31mbar[39;49;00m|[32mfilter[39;49;00m) [36m}}[39;49;00m$
    99^I        wrong:$
   100^I            [36m{{[39;49;00m [31mfoo[39;49;00m|[32mfilter[39;49;00m + [31mbar[39;49;00m|[32mfilter[39;49;00m [36m}}[39;49;00m$
   101^I$
   102^I        correct:$
   103^I            [36m{{[39;49;00m ([31mfoo[39;49;00m|[32mfilter[39;49;00m)[31m.attribute[39;49;00m [36m}}[39;49;00m$
   104^I        wrong:$
   105^I            [36m{{[39;49;00m [31mfoo[39;49;00m|[32mfilter[39;49;00m[31m.attribute[39;49;00m [36m}}[39;49;00m$
   106^I$
   107^I[01mTests[39;49;00m$
   108^I[01m=====[39;49;00m$
   109^I$
   110^IYou can use the [31m`is`[39;49;00m operator to perform tests on a value:$
   111^I$
   112^I.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
   113^I$
   114^I    [36m{{[39;49;00m [34m4[39;49;00m[34m2[39;49;00m [34mis[39;49;00m [32mnumeric[39;49;00m [36m}}[39;49;00m -> true$
   115^I    [36m{{[39;49;00m [33m"foobar"[39;49;00m [34mis[39;49;00m [32mnumeric[39;49;00m [36m}}[39;49;00m -> false$
   116^I    [36m{{[39;49;00m [33m'FOO'[39;49;00m [34mis[39;49;00m [32mupper[39;49;00m [36m}}[39;49;00m -> true$
   117^I$
   118^IThese tests are especially useful when used in [31m`if`[39;49;00m conditions.$
   119^I$
   120^I[[list_of_tests]]$
   121^I$
   122^I[01mGlobal Functions[39;49;00m$
   123^I[01m================[39;49;00m$
   124^I$
   125^ITest functions and filter functions live in their own namespace. Global$
   126^Ifunctions not. They behave like normal objects in the context. Beside the$
   127^Ifunctions added by the application or framewhere there are two functions$
   128^Iavailable per default:$
   129^I$
   130^I[31m`range`[39;49;00m$
   131^I    $
   132^I    Works like the python [33m`range function`_[39;49;00m just that it doesn't support$
   133^I    ranges greater than [33m``[39;49;00m[33m1000000[39;49;00m[33m``[39;49;00m.$
   134^I$
   135^I[31m`debug`[39;49;00m$
   136^I$
   137^I    Function that outputs the contents of the context.$
   138^I$
   139^I[01mLoops[39;49;00m$
   140^I[01m=====[39;49;00m$
   141^I$
   142^ITo iterate over a sequence, you can use the [31m`for`[39;49;00m loop. It basically looks like a$
   143^Inormal Python [31m`for`[39;49;00m loop and works pretty much the same:$
   144^I$
   145^I.. [35msourcecode[39;49;00m:: [34mhtml+jinja[39;49;00m$
   146^I$
   147^I    <[94mh1[39;49;00m>Members</[94mh1[39;49;00m>$
   148^I    <[94mul[39;49;00m>$
   149^I    [36m{%[39;49;00m [34mfor[39;49;00m [31muser[39;49;00m [34min[39;49;00m [31musers[39;49;00m [36m%}[39;49;00m$
   150^I      <[94mli[39;49;00m>[36m{{[39;49;00m [36mloop[39;49;00m[31m.index[39;49;00m [36m}}[39;49;00m / [36m{{[39;49;00m [36mloop[39;49;00m[31m.length[39;49;00m [36m}}[39;49;00m - [36m{{[39;49;00m [31muser[39;49;00m[31m.username[39;49;00m|[32mescape[39;49;00m [36m}}[39;49;00m</[94mli[39;49;00m>$
   151^I    [36m{%[39;49;00m [34melse[39;49;00m [36m%}[39;49;00m$
   152^I      <[94mli[39;49;00m><[94mem[39;49;00m>no users found</[94mem[39;49;00m></[94mli[39;49;00m>$
   153^I    [36m{%[39;49;00m [34mendfor[39;49;00m [36m%}[39;49;00m$
   154^I    </[94mul[39;49;00m>$
   155^I$
   156^I*Important* Contrary to Python is the optional [33m``[39;49;00m[33melse[39;49;00m[33m``[39;49;00m block only$
   157^Iexecuted if there was no iteration because the sequence was empty.$
   158^I$
   159^IInside of a [31m`for`[39;49;00m loop block you can access some special variables:$
   160^I$
   161^I+----------------------+----------------------------------------+$
   162^I| Variable             | Description                            |$
   163^I+======================+========================================+$
   164^I| [31m`loop.index`[39;49;00m         | The current iteration of the loop.     |$
   165^I+----------------------+----------------------------------------+$
   166^I| [31m`loop.index0`[39;49;00m        | The current iteration of the loop,     |$
   167^I|                      | starting counting by 0.                |$
   168^I+----------------------+----------------------------------------+$
   169^I| [31m`loop.revindex`[39;49;00m      | The number of iterations from the end  |$
   170^I|                      | of the loop.                           |$
   171^I+----------------------+----------------------------------------+$
   172^I| [31m`loop.revindex0`[39;49;00m     | The number of iterations from the end  |$
   173^I|                      | of the loop, starting counting by 0.   |$
   174^I+----------------------+----------------------------------------+$
   175^I| [31m`loop.first`[39;49;00m         | True if first iteration.               |$
   176^I+----------------------+----------------------------------------+$
   177^I| [31m`loop.last`[39;49;00m          | True if last iteration.                |$
   178^I+----------------------+----------------------------------------+$
   179^I| [31m`loop.even`[39;49;00m          | True if current iteration is even.     |$
   180^I+----------------------+----------------------------------------+$
   181^I| [31m`loop.odd`[39;49;00m           | True if current iteration is odd.      |$
   182^I+----------------------+----------------------------------------+$
   183^I| [31m`loop.length`[39;49;00m        | Total number of items in the sequence. |$
   184^I+----------------------+----------------------------------------+$
   185^I| [31m`loop.parent`[39;49;00m        | The context of the parent loop.        |$
   186^I+----------------------+----------------------------------------+$
   187^I$
   188^ILoops also support recursion. Let's assume you have a sitemap where each item$
   189^Imight have a number of child items. A template for that could look like this:$
   190^I$
   191^I.. [35msourcecode[39;49;00m:: [34mhtml+jinja[39;49;00m$
   192^I$
   193^I    <[94mh1[39;49;00m>Sitemap$
   194^I    <[94mul[39;49;00m [36mid[39;49;00m=[33m"sitemap"[39;49;00m>$
   195^I    [36m{%[39;49;00m [34mfor[39;49;00m [31mitem[39;49;00m [34min[39;49;00m [31msitemap[39;49;00m [34mrecursive[39;49;00m [36m%}[39;49;00m$
   196^I      <[94mli[39;49;00m><[94ma[39;49;00m [36mhref[39;49;00m=[33m"[39;49;00m[36m{{[39;49;00m [31mitem[39;49;00m[31m.url[39;49;00m|[32me[39;49;00m [36m}}[39;49;00m[33m"[39;49;00m>[36m{{[39;49;00m [31mitem[39;49;00m[31m.title[39;49;00m|[32me[39;49;00m [36m}}[39;49;00m</[94ma[39;49;00m>$
   197^I      [36m{%[39;49;00m [34mif[39;49;00m [31mitem[39;49;00m[31m.children[39;49;00m [36m%}[39;49;00m<[94mul[39;49;00m>[36m{{[39;49;00m [36mloop[39;49;00m([31mitem[39;49;00m[31m.children[39;49;00m) [36m}}[39;49;00m</[94mul[39;49;00m>[36m{%[39;49;00m [34mendif[39;49;00m [36m%}[39;49;00m</[94mli[39;49;00m>$
   198^I    [36m{%[39;49;00m [34mendfor[39;49;00m [36m%}[39;49;00m$
   199^I    </[94mul[39;49;00m>$
   200^I$
   201^IWhat happens here? Basically the first thing that is different to a normal$
   202^Iloop is the additional [33m``[39;49;00m[33mrecursive[39;49;00m[33m``[39;49;00m modifier in the [31m`for`[39;49;00m-loop declaration.$
   203^IIt tells the template engine that we want recursion. If recursion is enabled$
   204^Ithe special [31m`loop`[39;49;00m variable is callable. If you call it with a sequence it will$
   205^Iautomatically render the loop at that position with the new sequence as argument.$
   206^I$
   207^I[01mCycling[39;49;00m$
   208^I[01m=======[39;49;00m$
   209^I$
   210^ISometimes you might want to have different text snippets for each row in a list,$
   211^Ifor example to have alternating row colors. You can easily do this by using the$
   212^I[33m``[39;49;00m[33m{% cycle %}[39;49;00m[33m``[39;49;00m tag:$
   213^I$
   214^I.. [35msourcecode[39;49;00m:: [34mhtml+jinja[39;49;00m$
   215^I$
   216^I    <[94mul[39;49;00m [36mid[39;49;00m=[33m"messages"[39;49;00m>$
   217^I    [36m{%[39;49;00m [34mfor[39;49;00m [31mmessage[39;49;00m [34min[39;49;00m [31mmessages[39;49;00m [36m%}[39;49;00m$
   218^I      <[94mli[39;49;00m [36mclass[39;49;00m=[33m"[39;49;00m[36m{%[39;49;00m [34mcycle[39;49;00m [33m'row1'[39;49;00m, [33m'row2'[39;49;00m [36m%}[39;49;00m[33m"[39;49;00m>[36m{{[39;49;00m [31mmessage[39;49;00m|[32me[39;49;00m [36m}}[39;49;00m</[94mli[39;49;00m>$
   219^I    [36m{%[39;49;00m [34mendfor[39;49;00m [36m%}[39;49;00m$
   220^I    </[94mul[39;49;00m>$
   221^I$
   222^IEach time Jinja encounters a [31m`cycle`[39;49;00m tag it will cycle through the list$
   223^Iof given items and return the next one. If you pass it one item jinja assumes$
   224^Ithat this item is a sequence from the context and uses this:$
   225^I$
   226^I.. [35msourcecode[39;49;00m:: [34mhtml+jinja[39;49;00m$
   227^I$
   228^I    <[94mli[39;49;00m [36mstyle[39;49;00m=[33m"color: [39;49;00m[36m{%[39;49;00m [34mcycle[39;49;00m [31mrowcolors[39;49;00m [36m%}[39;49;00m[33m"[39;49;00m>...</[94mli[39;49;00m>$
   229^I$
   230^I[01mConditions[39;49;00m$
   231^I[01m==========[39;49;00m$
   232^I$
   233^IJinja supports Python-like [31m`if`[39;49;00m / [31m`elif`[39;49;00m / [31m`else`[39;49;00m constructs:$
   234^I$
   235^I.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
   236^I$
   237^I    [36m{%[39;49;00m [34mif[39;49;00m [31muser[39;49;00m[31m.active[39;49;00m [36m%}[39;49;00m$
   238^I        user [36m{{[39;49;00m [31muser[39;49;00m[31m.name[39;49;00m|[32me[39;49;00m [36m}}[39;49;00m is active.$
   239^I    [36m{%[39;49;00m [34melif[39;49;00m [31muser[39;49;00m[31m.deleted[39;49;00m [36m%}[39;49;00m$
   240^I        user [36m{{[39;49;00m [31muser[39;49;00m[31m.name[39;49;00m|[32me[39;49;00m [36m}}[39;49;00m was deleted some time ago.$
   241^I    [36m{%[39;49;00m [34melse[39;49;00m [36m%}[39;49;00m$
   242^I        i don't know what's wrong with [36m{{[39;49;00m [31muser[39;49;00m[31m.username[39;49;00m|[32me[39;49;00m [36m}}[39;49;00m$
   243^I    [36m{%[39;49;00m [34mendif[39;49;00m [36m%}[39;49;00m$
   244^I$
   245^IIf the user is active the first block is rendered. If not and the user was$
   246^Ideleted the second one, in all other cases the third one.$
   247^I$
   248^IYou can also use comparison operators:$
   249^I$
   250^I.. [35msourcecode[39;49;00m:: [34mhtml+jinja[39;49;00m$
   251^I$
   252^I    [36m{%[39;49;00m [34mif[39;49;00m [31mamount[39;49;00m < [34m0[39;49;00m [36m%}[39;49;00m$
   253^I        <[94mspan[39;49;00m [36mstyle[39;49;00m=[33m"color: red"[39;49;00m>[36m{{[39;49;00m [31mamount[39;49;00m [36m}}[39;49;00m</[94mspan[39;49;00m>$
   254^I    [36m{%[39;49;00m [34melse[39;49;00m [36m%}[39;49;00m$
   255^I        <[94mspan[39;49;00m [36mstyle[39;49;00m=[33m"color: black"[39;49;00m>[36m{{[39;49;00m [31mamount[39;49;00m [36m}}[39;49;00m</[94mspan[39;49;00m>$
   256^I    [36m{%[39;49;00m [34mendif[39;49;00m [36m%}[39;49;00m$
   257^I$
   258^I.. [35madmonition[39;49;00m:: Note$
   259^I$
   260^I    Of course you can use [31m`or`[39;49;00m / [31m`and`[39;49;00m and parentheses to create more complex$
   261^I    conditions, but usually the logic is already handled in the application and$
   262^I    you don't have to create such complex constructs in the template code. However$
   263^I    in some situations it might be a good thing to have the abilities to create$
   264^I    them.$
   265^I$
   266^I[01mOperators[39;49;00m$
   267^I[01m=========[39;49;00m$
   268^I$
   269^IInside [33m``[39;49;00m[33m{{ variable }}[39;49;00m[33m``[39;49;00m blocks, [31m`if`[39;49;00m conditions and many other parts you can$
   270^Ican use expressions. In expressions you can use any of the following operators:$
   271^I$
   272^I    ======= ===================================================================$
   273^I    [33m``[39;49;00m[33m+[39;49;00m[33m``[39;49;00m   add the right operand to the left one.$
   274^I            [33m``[39;49;00m[33m{{ 1 + 2 }}[39;49;00m[33m``[39;49;00m would return [33m``[39;49;00m[33m3[39;49;00m[33m``[39;49;00m.$
   275^I    [33m``[39;49;00m[33m-[39;49;00m[33m``[39;49;00m   subtract the right operand from the left one.$
   276^I            [33m``[39;49;00m[33m{{ 1 - 1 }}[39;49;00m[33m``[39;49;00m would return [33m``[39;49;00m[33m0[39;49;00m[33m``[39;49;00m.$
   277^I    [33m``[39;49;00m[33m/[39;49;00m[33m``[39;49;00m   divide the left operand by the right one.$
   278^I            [33m``[39;49;00m[33m{{ 1 / 2 }}[39;49;00m[33m``[39;49;00m would return [33m``[39;49;00m[33m0.5[39;49;00m[33m``[39;49;00m.$
   279^I    [33m``[39;49;00m[33m*[39;49;00m[33m``[39;49;00m   multiply the left operand with the right one.$
   280^I            [33m``[39;49;00m[33m{{ 2 * 2 }}[39;49;00m[33m``[39;49;00m would return [33m``[39;49;00m[33m4[39;49;00m[33m``[39;49;00m.$
   281^I    [33m``[39;49;00m[33m**[39;49;00m[33m``[39;49;00m  raise the left operand to the power of the right$
   282^I            operand. [33m``[39;49;00m[33m{{ 2**3 }}[39;49;00m[33m``[39;49;00m would return [33m``[39;49;00m[33m8[39;49;00m[33m``[39;49;00m.$
   283^I    [33m``[39;49;00m[33min[39;49;00m[33m``[39;49;00m  perform sequence membership test. [33m``[39;49;00m[33m{{ 1 in [1,2,3] }}[39;49;00m[33m``[39;49;00m would$
   284^I            return true.$
   285^I    [33m``[39;49;00m[33mis[39;49;00m[33m``[39;49;00m  perform a test on the value. See the section about$
   286^I            tests for more information.$
   287^I    [33m``[39;49;00m[33m|[39;49;00m[33m``[39;49;00m   apply a filter on the value. See the section about$
   288^I            filters for more information.$
   289^I    [33m``[39;49;00m[33mand[39;49;00m[33m``[39;49;00m return true if the left and the right operand is true.$
   290^I    [33m``[39;49;00m[33mor[39;49;00m[33m``[39;49;00m  return true if the left or the right operand is true.$
   291^I    [33m``[39;49;00m[33mnot[39;49;00m[33m``[39;49;00m negate a statement (see below)$
   292^I    [33m``[39;49;00m[33m()[39;49;00m[33m``[39;49;00m  call a callable: [33m``[39;49;00m[33m{{ user.get_username() }}[39;49;00m[33m``[39;49;00m. Inside of the$
   293^I            parentheses you can use variables: [33m``[39;49;00m[33m{{ user.get(username) }}[39;49;00m[33m``[39;49;00m.$
   294^I    ======= ===================================================================$
   295^I$
   296^INote that there is no support for any bit operations or something similar.$
   297^I$
   298^I[34m*[39;49;00m special note regarding [31m`not`[39;49;00m: The [31m`is`[39;49;00m and [31m`in`[39;49;00m operators support negation$
   299^I  using an infix notation too: [33m``[39;49;00m[33mfoo is not bar[39;49;00m[33m``[39;49;00m and [33m``[39;49;00m[33mfoo not in bar[39;49;00m[33m``[39;49;00m$
   300^I  instead of [33m``[39;49;00m[33mnot foo is bar[39;49;00m[33m``[39;49;00m and [33m``[39;49;00m[33mnot foo in bar[39;49;00m[33m``[39;49;00m. All other expressions$
   301^I  require a prefix notation: [33m``[39;49;00m[33mnot (foo and bar)[39;49;00m[33m``[39;49;00m.$
   302^I$
   303^I[01mBoolean Values[39;49;00m$
   304^I[01m==============[39;49;00m$
   305^I$
   306^IIn If-Conditions Jinja performs a boolean check. All empty values (eg: empty$
   307^Ilists [33m``[39;49;00m[33m[][39;49;00m[33m``[39;49;00m, empty dicts [33m``[39;49;00m[33m{}[39;49;00m[33m``[39;49;00m etc) evaluate to [31m`false`[39;49;00m. Numbers that are$
   308^Iequal to [31m`0`[39;49;00m/[31m`0.00`[39;49;00m are considered [31m`false`[39;49;00m too. The boolean value of other$
   309^Iobjects depends on the behavior the application developer gave it. Usually$
   310^Iitems are [31m`true`[39;49;00m.$
   311^I$
   312^IHere some examples that should explain it:$
   313^I$
   314^I.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
   315^I$
   316^I    [36m{%[39;49;00m [34mif[39;49;00m [] [36m%}[39;49;00m$
   317^I        will always be false because it's an empty list$
   318^I$
   319^I    [36m{%[39;49;00m [34mif[39;49;00m {} [36m%}[39;49;00m$
   320^I        false too.$
   321^I$
   322^I    [36m{%[39;49;00m [34mif[39;49;00m [[33m'foo'[39;49;00m] [36m%}[39;49;00m$
   323^I        this is true. Because the list is not empty.$
   324^I$
   325^I    [36m{%[39;49;00m [34mif[39;49;00m [33m"foobar"[39;49;00m [36m%}[39;49;00m$
   326^I        this is also true because the string is not empty.$
   327^I$
   328^I[01mSlicing[39;49;00m$
   329^I[01m=======[39;49;00m$
   330^I$
   331^ISome objects support slicing operations. For example lists:$
   332^I$
   333^I.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
   334^I$
   335^I    [36m{%[39;49;00m [34mfor[39;49;00m [31mitem[39;49;00m [34min[39;49;00m [31mitems[39;49;00m[:[34m5[39;49;00m] [36m%}[39;49;00m$
   336^I        This will only iterate over the first 5 items of the list$
   337^I$
   338^I    [36m{%[39;49;00m [34mfor[39;49;00m [31mitem[39;49;00m [34min[39;49;00m [31mitems[39;49;00m[[34m5[39;49;00m:[34m1[39;49;00m[34m0[39;49;00m] [36m%}[39;49;00m$
   339^I        This will only iterate from item 5 to 10.$
   340^I$
   341^I    [36m{%[39;49;00m [34mfor[39;49;00m [31mitem[39;49;00m [34min[39;49;00m [31mitems[39;49;00m[:[34m1[39;49;00m[34m0[39;49;00m:[34m2[39;49;00m] [36m%}[39;49;00m$
   342^I        This will only yield items from start to ten and only returing$
   343^I        even items.$
   344^I$
   345^IFor more informations about slicing have a look at the [33m`slicing chapter`_[39;49;00m$
   346^Iin the "Dive into Python" e-book.$
   347^I$
   348^I[01mMacros[39;49;00m$
   349^I[01m======[39;49;00m$
   350^I$
   351^IIf you want to use a partial template in more than one place, you might want to$
   352^Icreate a macro from it:$
   353^I$
   354^I.. [35msourcecode[39;49;00m:: [34mhtml+jinja[39;49;00m$
   355^I$
   356^I    [36m{%[39;49;00m [34mmacro[39;49;00m [31mshow_user[39;49;00m [31muser[39;49;00m [36m%}[39;49;00m$
   357^I      <[94mh1[39;49;00m>[36m{{[39;49;00m [31muser[39;49;00m[31m.name[39;49;00m|[32me[39;49;00m [36m}}[39;49;00m</[94mh1[39;49;00m>$
   358^I      <[94mdiv[39;49;00m [36mclass[39;49;00m=[33m"test"[39;49;00m>$
   359^I        [36m{{[39;49;00m [31muser[39;49;00m[31m.description[39;49;00m [36m}}[39;49;00m$
   360^I      </[94mdiv[39;49;00m>$
   361^I    [36m{%[39;49;00m [34mendmacro[39;49;00m [36m%}[39;49;00m$
   362^I$
   363^INow you can use it from everywhere in the code by passing it an item:$
   364^I$
   365^I.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
   366^I    $
   367^I    [36m{%[39;49;00m [34mfor[39;49;00m [31muser[39;49;00m [34min[39;49;00m [31musers[39;49;00m [36m%}[39;49;00m$
   368^I        [36m{{[39;49;00m [31mshow_user[39;49;00m([31muser[39;49;00m) [36m}}[39;49;00m$
   369^I    [36m{%[39;49;00m [34mendfor[39;49;00m [36m%}[39;49;00m$
   370^I$
   371^IYou can also specify more than one value:$
   372^I$
   373^I.. [35msourcecode[39;49;00m:: [34mhtml+jinja[39;49;00m$
   374^I$
   375^I    [36m{%[39;49;00m [34mmacro[39;49;00m [31mshow_dialog[39;49;00m [31mtitle[39;49;00m, [31mtext[39;49;00m [36m%}[39;49;00m$
   376^I      <[94mdiv[39;49;00m [36mclass[39;49;00m=[33m"dialog"[39;49;00m>$
   377^I        <[94mh1[39;49;00m>[36m{{[39;49;00m [31mtitle[39;49;00m|[32me[39;49;00m [36m}}[39;49;00m</[94mh1[39;49;00m>$
   378^I        <[94mdiv[39;49;00m [36mclass[39;49;00m=[33m"test"[39;49;00m>[36m{{[39;49;00m [31mtext[39;49;00m|[32me[39;49;00m [36m}}[39;49;00m</[94mdiv[39;49;00m>$
   379^I      </[94mdiv[39;49;00m>$
   380^I    [36m{%[39;49;00m [34mendmacro[39;49;00m [36m%}[39;49;00m$
   381^I$
   382^I    [36m{{[39;49;00m [31mshow_dialog[39;49;00m([33m'Warning'[39;49;00m, [33m'something went wrong i guess'[39;49;00m) [36m}}[39;49;00m$
   383^I$
   384^I[01mInheritance[39;49;00m$
   385^I[01m===========[39;49;00m$
   386^I$
   387^IThe most powerful part of Jinja is template inheritance. Template inheritance$
   388^Iallows you to build a base "skeleton" template that contains all the common$
   389^Ielements of your site and defines **blocks** that child templates can override.$
   390^I$
   391^ISounds complicated but is very basic. It's easiest to understand it by starting$
   392^Iwith an example.$
   393^I$
   394^I[01mBase Template[39;49;00m$
   395^I[01m-------------[39;49;00m$
   396^I$
   397^IThis template, which we'll call [33m``[39;49;00m[33mbase.html[39;49;00m[33m``[39;49;00m, defines a simple HTML skeleton$
   398^Idocument that you might use for a simple two-column page. It's the job of$
   399^I"child" templates to fill the empty blocks with content:$
   400^I$
   401^I.. [35msourcecode[39;49;00m:: [34mhtml+jinja[39;49;00m$
   402^I$
   403^I    [36m<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"[39;49;00m$
   404^I    [36m "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">[39;49;00m$
   405^I    <[94mhtml[39;49;00m [36mxmlns[39;49;00m=[33m"http://www.w3.org/1999/xhtml"[39;49;00m>$
   406^I    <[94mhead[39;49;00m>$
   407^I      <[94mlink[39;49;00m [36mrel[39;49;00m=[33m"stylesheet"[39;49;00m [36mhref[39;49;00m=[33m"style.css"[39;49;00m />$
   408^I      <[94mtitle[39;49;00m>[36m{%[39;49;00m [34mblock[39;49;00m [31mtitle[39;49;00m [36m%}[39;49;00m[36m{%[39;49;00m [34mendblock[39;49;00m [36m%}[39;49;00m - My Webpage</[94mtitle[39;49;00m>$
   409^I      [36m{%[39;49;00m [34mblock[39;49;00m [31mhtml_head[39;49;00m [36m%}[39;49;00m[36m{%[39;49;00m [34mendblock[39;49;00m [36m%}[39;49;00m$
   410^I    </[94mhead[39;49;00m>$
   411^I    <[94mbody[39;49;00m>$
   412^I      <[94mdiv[39;49;00m [36mid[39;49;00m=[33m"content"[39;49;00m>$
   413^I        [36m{%[39;49;00m [34mblock[39;49;00m [31mcontent[39;49;00m [36m%}[39;49;00m[36m{%[39;49;00m [34mendblock[39;49;00m [36m%}[39;49;00m$
   414^I      </[94mdiv[39;49;00m>$
   415^I$
   416^I      <[94mdiv[39;49;00m [36mid[39;49;00m=[33m"footer"[39;49;00m>$
   417^I        [36m{%[39;49;00m [34mblock[39;49;00m [31mfooter[39;49;00m [36m%}[39;49;00m$
   418^I        &copy; Copyright 2006 by <[94ma[39;49;00m [36mhref[39;49;00m=[33m"http://mydomain.tld"[39;49;00m>myself</[94ma[39;49;00m>.$
   419^I        [36m{%[39;49;00m [34mendblock[39;49;00m [36m%}[39;49;00m$
   420^I      </[94mdiv[39;49;00m>$
   421^I    </[94mbody[39;49;00m>$
   422^I$
   423^IIn this example, the [33m``[39;49;00m[33m{% block %}[39;49;00m[33m``[39;49;00m tags define four blocks that child templates$
   424^Ican fill in. All the [31m`block`[39;49;00m tag does is to tell the template engine that a$
   425^Ichild template may override those portions of the template.$
   426^I$
   427^I[01mChild Template[39;49;00m$
   428^I[01m--------------[39;49;00m$
   429^I$
   430^IA child template might look like this:$
   431^I$
   432^I.. [35msourcecode[39;49;00m:: [34mhtml+jinja[39;49;00m$
   433^I$
   434^I    [36m{%[39;49;00m [34mextends[39;49;00m [33m"base.html"[39;49;00m [36m%}[39;49;00m$
   435^I    [36m{%[39;49;00m [34mblock[39;49;00m [31mtitle[39;49;00m [36m%}[39;49;00mIndex[36m{%[39;49;00m [34mendblock[39;49;00m [36m%}[39;49;00m$
   436^I$
   437^I    [36m{%[39;49;00m [34mblock[39;49;00m [31mhtml_head[39;49;00m [36m%}[39;49;00m$
   438^I      <[94mstyle[39;49;00m [36mtype[39;49;00m=[33m"text/css"[39;49;00m>[37m[39;49;00m$
   439^I    [37m    [39;49;00m.[04m[32mimportant[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
   440^I    [37m      [39;49;00m[34mcolor[39;49;00m:[37m [39;49;00m[34m#336699[39;49;00m;[37m[39;49;00m$
   441^I    [37m    [39;49;00m}[37m[39;49;00m$
   442^I    [37m  [39;49;00m</[94mstyle[39;49;00m>$
   443^I    [36m{%[39;49;00m [34mendblock[39;49;00m [36m%}[39;49;00m$
   444^I    $
   445^I    [36m{%[39;49;00m [34mblock[39;49;00m [31mcontent[39;49;00m [36m%}[39;49;00m$
   446^I        <[94mh1[39;49;00m>Index</[94mh1[39;49;00m>$
   447^I        <[94mp[39;49;00m [36mclass[39;49;00m=[33m"important"[39;49;00m>$
   448^I          Welcome on my awsome homepage.$
   449^I        </[94mp[39;49;00m>$
   450^I    [36m{%[39;49;00m [34mendblock[39;49;00m [36m%}[39;49;00m$
   451^I$
   452^IThe [33m``[39;49;00m[33m{% extends %}[39;49;00m[33m``[39;49;00m tag is the key here. It tells the template engine that$
   453^Ithis template "extends" another template. When the template system evaluates$
   454^Ithis template, first it locates the parent.$
   455^I$
   456^IThe filename of the template depends on the template loader. For example the$
   457^I[33m``[39;49;00m[33mFileSystemLoader[39;49;00m[33m``[39;49;00m allows you to access other templates by giving the$
   458^Ifilename. You can access templates in subdirectories with an slash:$
   459^I$
   460^I.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
   461^I$
   462^I    [36m{%[39;49;00m [34mextends[39;49;00m [33m"layout/default.html"[39;49;00m [36m%}[39;49;00m$
   463^I$
   464^IBut this behavior can depend on the application using Jinja.$
   465^I$
   466^INote that since the child template didn't define the [33m``[39;49;00m[33mfooter[39;49;00m[33m``[39;49;00m block, the$
   467^Ivalue from the parent template is used instead.$
   468^I$
   469^I.. [35madmonition[39;49;00m:: Note$
   470^I$
   471^I    You can't define multiple [33m``[39;49;00m[33m{% block %}[39;49;00m[33m``[39;49;00m tags with the same name in the$
   472^I    same template. This limitation exists because a block tag works in "both"$
   473^I    directions. That is, a block tag doesn't just provide a hole to fill - it$
   474^I    also defines the content that fills the hole in the *parent*. If there were$
   475^I    two similarly-named [33m``[39;49;00m[33m{% block %}[39;49;00m[33m``[39;49;00m tags in a template, that template's$
   476^I    parent wouldn't know which one of the blocks' content to use.$
   477^I$
   478^I[01mTemplate Inclusion[39;49;00m$
   479^I[01m==================[39;49;00m$
   480^I$
   481^IYou can load another template at a given position using [33m``[39;49;00m[33m{% include %}[39;49;00m[33m``[39;49;00m.$
   482^IUsually it's a better idea to use inheritance but if you for example want to$
   483^Iload macros, [31m`include`[39;49;00m works better than [31m`extends`[39;49;00m:$
   484^I$
   485^I.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
   486^I$
   487^I    [36m{%[39;49;00m [34minclude[39;49;00m [33m"myhelpers.html"[39;49;00m [36m%}[39;49;00m$
   488^I    [36m{{[39;49;00m [31mmy_helper[39;49;00m([33m"foo"[39;49;00m) [36m}}[39;49;00m$
   489^I$
   490^IIf you define a macro called [33m``[39;49;00m[33mmy_helper[39;49;00m[33m``[39;49;00m in [33m``[39;49;00m[33mmyhelpers.html[39;49;00m[33m``[39;49;00m, you can now$
   491^Iuse it from the template as shown above.$
   492^I$
   493^I[01mFiltering Blocks[39;49;00m$
   494^I[01m================[39;49;00m$
   495^I$
   496^ISometimes it could be a good idea to filter a complete block of text. For$
   497^Iexample, if you want to escape some html code:$
   498^I$
   499^I.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
   500^I$
   501^I    [36m{%[39;49;00m [34mfilter[39;49;00m [32mescape[39;49;00m [36m%}[39;49;00m$
   502^I        <html>$
   503^I          <code>goes here</code>$
   504^I        </html>$
   505^I    [36m{%[39;49;00m [34mendfilter[39;49;00m [36m%}[39;49;00m$
   506^I$
   507^IOf course you can chain filters too:$
   508^I$
   509^I.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
   510^I$
   511^I    [36m{%[39;49;00m [34mfilter[39;49;00m [32mlower[39;49;00m|[32mescape[39;49;00m [36m%}[39;49;00m$
   512^I        <B>SOME TEXT</B>$
   513^I    [36m{%[39;49;00m [34mendfilter[39;49;00m [36m%}[39;49;00m$
   514^I$
   515^Ireturns [33m``[39;49;00m[33m"&lt;b&gt;some text&lt;/b&gt;"[39;49;00m[33m``[39;49;00m.$
   516^I$
   517^I[01mDefining Variables[39;49;00m$
   518^I[01m==================[39;49;00m$
   519^I$
   520^IYou can also define variables in the namespace using the [33m``[39;49;00m[33m{% set %}[39;49;00m[33m``[39;49;00m tag:$
   521^I$
   522^I.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
   523^I$
   524^I    [36m{%[39;49;00m [34mset[39;49;00m [31mfoo[39;49;00m = [33m'foobar'[39;49;00m [36m%}[39;49;00m$
   525^I    [36m{{[39;49;00m [31mfoo[39;49;00m [36m}}[39;49;00m$
   526^I$
   527^IThis should ouput [33m``[39;49;00m[33mfoobar[39;49;00m[33m``[39;49;00m.$
   528^I$
   529^I[01mScopes[39;49;00m$
   530^I[01m======[39;49;00m$
   531^I$
   532^IJinja has multiple scopes. A scope is something like a new transparent foil on$
   533^Ia stack of foils. You can only write to the outermost foil but read all of them$
   534^Isince you can look through them. If you remove the top foil all data on that$
   535^Ifoil disappears. Some tags in Jinja add a new layer to the stack. Currently$
   536^Ithese are [31m`block`[39;49;00m, [31m`for`[39;49;00m, [31m`macro`[39;49;00m and [31m`filter`[39;49;00m. This means that variables and$
   537^Iother elements defined inside a macro, loop or some of the other tags listed$
   538^Iabove will be only available in that block. Here an example:$
   539^I$
   540^I.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
   541^I$
   542^I    [36m{%[39;49;00m [34mmacro[39;49;00m [31mangryhello[39;49;00m [31mname[39;49;00m [36m%}[39;49;00m$
   543^I      [36m{%[39;49;00m [34mset[39;49;00m [31mangryname[39;49;00m = [31mname[39;49;00m|[32mupper[39;49;00m [36m%}[39;49;00m$
   544^I      Hello [36m{{[39;49;00m [31mname[39;49;00m [36m}}[39;49;00m. Hello [36m{{[39;49;00m [31mname[39;49;00m [36m}}[39;49;00m!$
   545^I      HELLO [36m{{[39;49;00m [31mangryname[39;49;00m [36m}}[39;49;00m!!!!!!111$
   546^I    [36m{%[39;49;00m [34mendmacro[39;49;00m [36m%}[39;49;00m$
   547^I$
   548^IThe variable [33m``[39;49;00m[33mangryname[39;49;00m[33m``[39;49;00m just exists inside the macro, not outside it.$
   549^I$
   550^IDefined macros appear on the context as variables. Because of this, they are$
   551^Iaffected by the scoping too. A macro defined inside of a macro is just available$
   552^Iin those two macros (the macro itself and the macro it's defined in). For [31m`set`[39;49;00m$
   553^Iand [31m`macro`[39;49;00m two additional rules exist: If a macro is defined in an extended$
   554^Itemplate but outside of a visible block (thus outside of any block) will be$
   555^Iavailable in all blocks below. This allows you to use [31m`include`[39;49;00m statements to$
   556^Iload often used macros at once.$
   557^I$
   558^I[01mUndefined Variables[39;49;00m$
   559^I[01m===================[39;49;00m$
   560^I$
   561^IIf you have already worked with python you probably know about the fact that$
   562^Iundefined variables raise an exception. This is different in Jinja. There is a$
   563^Ispecial value called [31m`undefined`[39;49;00m that represents values that do not exist.$
   564^I$
   565^IThis special variable works complete different from any variables you maybe$
   566^Iknow. If you print it using [33m``[39;49;00m[33m{{ variable }}[39;49;00m[33m``[39;49;00m it will not appear because it's$
   567^Iliterally empty. If you try to iterate over it, it will work. But no items$
   568^Iare returned. Comparing this value to any other value results in [31m`false`[39;49;00m.$
   569^IEven if you compare it to itself:$
   570^I$
   571^I.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
   572^I$
   573^I    [36m{{[39;49;00m [31mundefined[39;49;00m == [31mundefined[39;49;00m [36m}}[39;49;00m$
   574^I        will return false. Not even undefined is undefined :)$
   575^I        Use `is defined` / `is not defined`:$
   576^I$
   577^I    [36m{{[39;49;00m [31mundefined[39;49;00m [34mis[39;49;00m [34mnot[39;49;00m [32mdefined[39;49;00m [36m}}[39;49;00m$
   578^I        will return true.$
   579^I$
   580^IThere are also some additional rules regarding this special value. Any$
   581^Imathematical operators ([33m``[39;49;00m[33m+[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33m-[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33m*[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33m/[39;49;00m[33m``[39;49;00m) return the operand$
   582^Ias result:$
   583^I$
   584^I.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
   585^I$
   586^I    [36m{{[39;49;00m [31mundefined[39;49;00m + [33m"foo"[39;49;00m [36m}}[39;49;00m$
   587^I        returns "foo"$
   588^I$
   589^I    [36m{{[39;49;00m [31mundefined[39;49;00m - [34m4[39;49;00m[34m2[39;49;00m [36m}}[39;49;00m$
   590^I        returns 42. Note: not -42!$
   591^I$
   592^IIn any expression [31m`undefined`[39;49;00m evaluates to [31m`false`[39;49;00m. It has no length, all$
   593^Iattribute calls return undefined, calling too:$
   594^I$
   595^I.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
   596^I$
   597^I    [36m{{[39;49;00m [31mundefined[39;49;00m[31m.attribute[39;49;00m()[31m.attribute_too[39;49;00m[[34m4[39;49;00m[34m2[39;49;00m] [36m}}[39;49;00m$
   598^I        still returns `undefined`.$
   599^I$
   600^I[01mEscaping[39;49;00m$
   601^I[01m========[39;49;00m$
   602^I$
   603^ISometimes you might want to add Jinja syntax elements into the template$
   604^Iwithout executing them. In that case you have quite a few possibilities.$
   605^I$
   606^IFor small parts this might be a good way:$
   607^I$
   608^I.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
   609^I$
   610^I    [36m{{[39;49;00m [33m"{{ foo }} is variable syntax and {% foo %} is block syntax"[39;49;00m [36m}}[39;49;00m$
   611^I$
   612^IWhen you have multiple elements you can use the [33m``[39;49;00m[33mraw[39;49;00m[33m``[39;49;00m block:$
   613^I$
   614^I.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
   615^I$
   616^I    [36m{%[39;49;00m [34mraw[39;49;00m [36m%}[39;49;00m$
   617^I        Filtering blocks works like this in Jinja:$
   618^I        {% filter escape %}$
   619^I            <html>$
   620^I              <code>goes here</code>$
   621^I            </html>$
   622^I        {% endfilter %}$
   623^I    [36m{%[39;49;00m [34mendraw[39;49;00m [36m%}[39;49;00m$
   624^I$
   625^I[01mReserved Keywords[39;49;00m$
   626^I[01m=================[39;49;00m$
   627^I$
   628^IJinja has some keywords you cannot use a variable names. This limitation$
   629^Iexists to make look coherent. Syntax highlighters won't mess things up and$
   630^Iyou will don't have unexpected output.$
   631^I$
   632^IThe following keywords exist and cannot be used as identifiers:$
   633^I$
   634^I    [31m`and`[39;49;00m, [31m`block`[39;49;00m, [31m`cycle`[39;49;00m, [31m`elif`[39;49;00m, [31m`else`[39;49;00m, [31m`endblock`[39;49;00m, [31m`endfilter`[39;49;00m,$
   635^I    [31m`endfor`[39;49;00m, [31m`endif`[39;49;00m, [31m`endmacro`[39;49;00m, [31m`endraw`[39;49;00m, [31m`endtrans`[39;49;00m, [31m`extends`[39;49;00m, [31m`filter`[39;49;00m,$
   636^I    [31m`for`[39;49;00m, [31m`if`[39;49;00m, [31m`in`[39;49;00m, [31m`include`[39;49;00m, [31m`is`[39;49;00m, [31m`macro`[39;49;00m, [31m`not`[39;49;00m, [31m`or`[39;49;00m, [31m`pluralize`[39;49;00m,$
   637^I    [31m`raw`[39;49;00m, [31m`recursive`[39;49;00m, [31m`set`[39;49;00m, [31m`trans`[39;49;00m$
   638^I$
   639^IIf you want to use such a name you have to prefix or suffix it or use$
   640^Ialternative names:$
   641^I$
   642^I.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
   643^I$
   644^I    [36m{%[39;49;00m [34mfor[39;49;00m [31mmacro_[39;49;00m [34min[39;49;00m [31mmacros[39;49;00m [36m%}[39;49;00m$
   645^I        [36m{{[39;49;00m [31mmacro_[39;49;00m([33m'foo'[39;49;00m) [36m}}[39;49;00m$
   646^I    [36m{%[39;49;00m [34mendfor[39;49;00m [36m%}[39;49;00m$
   647^I$
   648^IIf future Jinja releases add new keywords those will be "light" keywords which$
   649^Imeans that they won't raise an error for several releases but yield warnings$
   650^Ion the application side. But it's very unlikely that new keywords will be$
   651^Iadded.$
   652^I$
   653^I[01mInternationalization[39;49;00m$
   654^I[01m====================[39;49;00m$
   655^I$
   656^IIf the application is configured for i18n, you can define translatable blocks$
   657^Ifor translators using the [31m`trans`[39;49;00m tag or the special underscore function:$
   658^I$
   659^I.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
   660^I$
   661^I    [36m{%[39;49;00m [34mtrans[39;49;00m [36m%}[39;49;00m$
   662^I        this is a translatable block$
   663^I    [36m{%[39;49;00m [34mendtrans[39;49;00m [36m%}[39;49;00m$
   664^I$
   665^I    [36m{%[39;49;00m [34mtrans[39;49;00m [33m"This is a translatable string"[39;49;00m [36m%}[39;49;00m$
   666^I$
   667^I    [36m{{[39;49;00m [34m_[39;49;00m([33m"This is a translatable string"[39;49;00m) [36m}}[39;49;00m$
   668^I$
   669^IThe latter one is useful if you want translatable arguments for filters etc.$
   670^I$
   671^IIf you want to have plural forms too, use the [31m`pluralize`[39;49;00m block:$
   672^I$
   673^I.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
   674^I$
   675^I    [36m{%[39;49;00m [34mtrans[39;49;00m [31musers[39;49;00m=[31musers[39;49;00m [36m%}[39;49;00m$
   676^I        One user found.$
   677^I    [36m{%[39;49;00m [34mpluralize[39;49;00m [36m%}[39;49;00m$
   678^I        [36m{{[39;49;00m [31musers[39;49;00m [36m}}[39;49;00m users found.$
   679^I    [36m{%[39;49;00m [34mendtrans[39;49;00m [36m%}[39;49;00m$
   680^I$
   681^I    [36m{%[39;49;00m [34mtrans[39;49;00m [31mfirst[39;49;00m=([31musers[39;49;00m|[32mfirst[39;49;00m)[31m.username[39;49;00m|[32mescape[39;49;00m, [31muser[39;49;00m=[31musers[39;49;00m|[32mlength[39;49;00m [36m%}[39;49;00m$
   682^I        one user [36m{{[39;49;00m [31mfirst[39;49;00m [36m}}[39;49;00m found.$
   683^I    [36m{%[39;49;00m [34mpluralize[39;49;00m [31musers[39;49;00m [36m%}[39;49;00m$
   684^I        [36m{{[39;49;00m [31musers[39;49;00m [36m}}[39;49;00m users found, the first one is called [36m{{[39;49;00m [31mfirst[39;49;00m [36m}}[39;49;00m.$
   685^I    [36m{%[39;49;00m [34mendtrans[39;49;00m [36m%}[39;49;00m$
   686^I$
   687^IIf you have multiple arguments, the first one is assumed to be the indicator (the$
   688^Inumber that is used to determine the correct singular or plural form. If you$
   689^Idon't have the indicator variable on position 1 you have to tell the [31m`pluralize`[39;49;00m$
   690^Itag the correct variable name.$
   691^I$
   692^IInside translatable blocks you cannot use blocks or expressions (however you can$
   693^Istill use the [33m``[39;49;00m[33mraw[39;49;00m[33m``[39;49;00m block which will work as expected). The variable$
   694^Iprint syntax ([33m``[39;49;00m[33m{{ variablename }}[39;49;00m[33m``[39;49;00m) is the only way to insert the variables$
   695^Idefined in the [33m``[39;49;00m[33mtrans[39;49;00m[33m``[39;49;00m header. Filters must be applied in the header.$
   696^I$
   697^I.. [35madmonition[39;49;00m:: note$
   698^I$
   699^I    Please make sure that you always use pluralize blocks where required.$
   700^I    Many languages have more complex plural forms than the English language.$
   701^I    $
   702^I    Never try to workaround that issue by using something like this:$
   703^I$
   704^I    .. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
   705^I$
   706^I        [36m{%[39;49;00m [34mif[39;49;00m [31mcount[39;49;00m != [34m1[39;49;00m [36m%}[39;49;00m$
   707^I            [36m{{[39;49;00m [31mcount[39;49;00m [36m}}[39;49;00m users found.$
   708^I        [36m{%[39;49;00m [34melse[39;49;00m [36m%}[39;49;00m$
   709^I            one user found.$
   710^I        [36m{%[39;49;00m [34mendif[39;49;00m [36m%}[39;49;00m$
   711^I$
   712^I.. [94m_slicing chapter:[39;49;00m http://diveintopython.org/native_data_types/lists.html#odbchelper.list.slice$
   713^I.. [94m_range function:[39;49;00m http://docs.python.org/tut/node6.html#SECTION006300000000000000000$

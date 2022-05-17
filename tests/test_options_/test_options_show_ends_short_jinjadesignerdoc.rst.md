[01m======================[39;49;00m$
[01mDesigner Documentation[39;49;00m$
[01m======================[39;49;00m$
$
This part of the Jinja documentaton is meant for template designers.$
$
[01mBasics[39;49;00m$
[01m======[39;49;00m$
$
The Jinja template language is designed to strike a balance between content$
and application logic. Nevertheless you can use a python like statement$
language. You don't have to know how Python works to create Jinja templates,$
but if you know it you can use some additional statements you may know from$
Python.$
$
Here is a small example template:$
$
.. [35msourcecode[39;49;00m:: [34mhtml+jinja[39;49;00m$
$
    [36m<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"[39;49;00m$
    [36m "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">[39;49;00m$
    <[94mhtml[39;49;00m [36mxmlns[39;49;00m=[33m"http://www.w3.org/1999/xhtml"[39;49;00m [36mlang[39;49;00m=[33m"en"[39;49;00m [36mxml:lang[39;49;00m=[33m"en"[39;49;00m>$
    <[94mhead[39;49;00m>$
        <[94mtitle[39;49;00m>My Webpage</[94mtitle[39;49;00m>$
    </[94mhead[39;49;00m>$
    <[94mbody[39;49;00m>$
        <[94mul[39;49;00m [36mid[39;49;00m=[33m"navigation"[39;49;00m>$
        [36m{%[39;49;00m [34mfor[39;49;00m [31mitem[39;49;00m [34min[39;49;00m [31mnavigation[39;49;00m [36m%}[39;49;00m$
            <[94mli[39;49;00m><[94ma[39;49;00m [36mhref[39;49;00m=[33m"[39;49;00m[36m{{[39;49;00m [31mitem[39;49;00m[31m.href[39;49;00m|[32me[39;49;00m [36m}}[39;49;00m[33m"[39;49;00m>[36m{{[39;49;00m [31mitem[39;49;00m[31m.caption[39;49;00m|[32me[39;49;00m [36m}}[39;49;00m</[94ma[39;49;00m></[94mli[39;49;00m>$
        [36m{%[39;49;00m [34mendfor[39;49;00m [36m%}[39;49;00m$
        </[94mul[39;49;00m>$
$
        <[94mh1[39;49;00m>My Webpage</[94mh1[39;49;00m>$
        [36m{{[39;49;00m [31mvariable[39;49;00m [36m}}[39;49;00m$
    </[94mbody[39;49;00m>$
    </[94mhtml[39;49;00m>$
$
This covers the default settings. The application developer might have changed$
the syntax from [33m``[39;49;00m[33m{% foo %}[39;49;00m[33m``[39;49;00m to [33m``[39;49;00m[33m<% foo %>[39;49;00m[33m``[39;49;00m or something similar. This$
documentation just covers the default values.$
$
A variable looks like [33m``[39;49;00m[33m{{ foobar }}[39;49;00m[33m``[39;49;00m where foobar is the variable name. Inside$
of statements ([33m``[39;49;00m[33m{% some content here %}[39;49;00m[33m``[39;49;00m) variables are just normal names$
without the braces around it. In fact [33m``[39;49;00m[33m{{ foobar }}[39;49;00m[33m``[39;49;00m is just an alias for$
the statement [33m``[39;49;00m[33m{% print foobar %}[39;49;00m[33m``[39;49;00m.$
$
Variables are coming from the context provided by the application. Normally there$
should be a documentation regarding the context contents but if you want to know$
the content of the current context, you can add this to your template:$
$
.. [35msourcecode[39;49;00m:: [34mhtml+jinja[39;49;00m$
$
    <[94mpre[39;49;00m>[36m{{[39;49;00m [31mdebug[39;49;00m()|[32me[39;49;00m [36m}}[39;49;00m</[94mpre[39;49;00m>$
$
A context isn't flat which means that each variable can has subvariables, as long$
as it is representable as python data structure. You can access attributes of$
a variable using the dot and bracket operators. The following examples show$
this:$
$
.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
$
    [36m{{[39;49;00m [31muser[39;49;00m[31m.username[39;49;00m [36m}}[39;49;00m$
        is the same as$
    [36m{{[39;49;00m [31muser[39;49;00m[[33m'username'[39;49;00m] [36m}}[39;49;00m$
        you can also use a variable to access an attribute:$
    [36m{{[39;49;00m [31musers[39;49;00m[[31mcurrent_user[39;49;00m][31m.username[39;49;00m [36m}}[39;49;00m$
        If you have numerical indices you have to use the [] syntax:$
    [36m{{[39;49;00m [31musers[39;49;00m[[34m0[39;49;00m][31m.username[39;49;00m [36m}}[39;49;00m$
$
[01mFilters[39;49;00m$
[01m=======[39;49;00m$
$
In the examples above you might have noticed the pipe symbols. Pipe symbols tell$
the engine that it has to apply a filter on the variable. Here is a small example:$
$
.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
$
    [36m{{[39;49;00m [31mvariable[39;49;00m|[32mreplace[39;49;00m([33m'foo'[39;49;00m, [33m'bar'[39;49;00m)|[32mescape[39;49;00m [36m}}[39;49;00m$
$
If you want, you can also put whitespace between the filters.$
$
This will look for a variable [31m`variable`[39;49;00m, pass it to the filter [31m`replace`[39;49;00m$
with the arguments [33m``[39;49;00m[33m'foo'[39;49;00m[33m``[39;49;00m and [33m``[39;49;00m[33m'bar'[39;49;00m[33m``[39;49;00m, and pass the result to the filter$
[31m`escape`[39;49;00m that automatically XML-escapes the value. The [31m`e`[39;49;00m filter is an alias for$
[31m`escape`[39;49;00m. Here is the complete list of supported filters:$
$
[[list_of_filters]]$
$
.. [35madmonition[39;49;00m:: note$
$
    Filters have a pretty low priority. If you want to add fitered values$
    you have to put them into parentheses. The same applies if you want to access$
    attributes:$
$
    .. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
$
        correct:$
            [36m{{[39;49;00m ([31mfoo[39;49;00m|[32mfilter[39;49;00m) + ([31mbar[39;49;00m|[32mfilter[39;49;00m) [36m}}[39;49;00m$
        wrong:$
            [36m{{[39;49;00m [31mfoo[39;49;00m|[32mfilter[39;49;00m + [31mbar[39;49;00m|[32mfilter[39;49;00m [36m}}[39;49;00m$
$
        correct:$
            [36m{{[39;49;00m ([31mfoo[39;49;00m|[32mfilter[39;49;00m)[31m.attribute[39;49;00m [36m}}[39;49;00m$
        wrong:$
            [36m{{[39;49;00m [31mfoo[39;49;00m|[32mfilter[39;49;00m[31m.attribute[39;49;00m [36m}}[39;49;00m$
$
[01mTests[39;49;00m$
[01m=====[39;49;00m$
$
You can use the [31m`is`[39;49;00m operator to perform tests on a value:$
$
.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
$
    [36m{{[39;49;00m [34m4[39;49;00m[34m2[39;49;00m [34mis[39;49;00m [32mnumeric[39;49;00m [36m}}[39;49;00m -> true$
    [36m{{[39;49;00m [33m"foobar"[39;49;00m [34mis[39;49;00m [32mnumeric[39;49;00m [36m}}[39;49;00m -> false$
    [36m{{[39;49;00m [33m'FOO'[39;49;00m [34mis[39;49;00m [32mupper[39;49;00m [36m}}[39;49;00m -> true$
$
These tests are especially useful when used in [31m`if`[39;49;00m conditions.$
$
[[list_of_tests]]$
$
[01mGlobal Functions[39;49;00m$
[01m================[39;49;00m$
$
Test functions and filter functions live in their own namespace. Global$
functions not. They behave like normal objects in the context. Beside the$
functions added by the application or framewhere there are two functions$
available per default:$
$
[31m`range`[39;49;00m$
    $
    Works like the python [33m`range function`_[39;49;00m just that it doesn't support$
    ranges greater than [33m``[39;49;00m[33m1000000[39;49;00m[33m``[39;49;00m.$
$
[31m`debug`[39;49;00m$
$
    Function that outputs the contents of the context.$
$
[01mLoops[39;49;00m$
[01m=====[39;49;00m$
$
To iterate over a sequence, you can use the [31m`for`[39;49;00m loop. It basically looks like a$
normal Python [31m`for`[39;49;00m loop and works pretty much the same:$
$
.. [35msourcecode[39;49;00m:: [34mhtml+jinja[39;49;00m$
$
    <[94mh1[39;49;00m>Members</[94mh1[39;49;00m>$
    <[94mul[39;49;00m>$
    [36m{%[39;49;00m [34mfor[39;49;00m [31muser[39;49;00m [34min[39;49;00m [31musers[39;49;00m [36m%}[39;49;00m$
      <[94mli[39;49;00m>[36m{{[39;49;00m [36mloop[39;49;00m[31m.index[39;49;00m [36m}}[39;49;00m / [36m{{[39;49;00m [36mloop[39;49;00m[31m.length[39;49;00m [36m}}[39;49;00m - [36m{{[39;49;00m [31muser[39;49;00m[31m.username[39;49;00m|[32mescape[39;49;00m [36m}}[39;49;00m</[94mli[39;49;00m>$
    [36m{%[39;49;00m [34melse[39;49;00m [36m%}[39;49;00m$
      <[94mli[39;49;00m><[94mem[39;49;00m>no users found</[94mem[39;49;00m></[94mli[39;49;00m>$
    [36m{%[39;49;00m [34mendfor[39;49;00m [36m%}[39;49;00m$
    </[94mul[39;49;00m>$
$
*Important* Contrary to Python is the optional [33m``[39;49;00m[33melse[39;49;00m[33m``[39;49;00m block only$
executed if there was no iteration because the sequence was empty.$
$
Inside of a [31m`for`[39;49;00m loop block you can access some special variables:$
$
+----------------------+----------------------------------------+$
| Variable             | Description                            |$
+======================+========================================+$
| [31m`loop.index`[39;49;00m         | The current iteration of the loop.     |$
+----------------------+----------------------------------------+$
| [31m`loop.index0`[39;49;00m        | The current iteration of the loop,     |$
|                      | starting counting by 0.                |$
+----------------------+----------------------------------------+$
| [31m`loop.revindex`[39;49;00m      | The number of iterations from the end  |$
|                      | of the loop.                           |$
+----------------------+----------------------------------------+$
| [31m`loop.revindex0`[39;49;00m     | The number of iterations from the end  |$
|                      | of the loop, starting counting by 0.   |$
+----------------------+----------------------------------------+$
| [31m`loop.first`[39;49;00m         | True if first iteration.               |$
+----------------------+----------------------------------------+$
| [31m`loop.last`[39;49;00m          | True if last iteration.                |$
+----------------------+----------------------------------------+$
| [31m`loop.even`[39;49;00m          | True if current iteration is even.     |$
+----------------------+----------------------------------------+$
| [31m`loop.odd`[39;49;00m           | True if current iteration is odd.      |$
+----------------------+----------------------------------------+$
| [31m`loop.length`[39;49;00m        | Total number of items in the sequence. |$
+----------------------+----------------------------------------+$
| [31m`loop.parent`[39;49;00m        | The context of the parent loop.        |$
+----------------------+----------------------------------------+$
$
Loops also support recursion. Let's assume you have a sitemap where each item$
might have a number of child items. A template for that could look like this:$
$
.. [35msourcecode[39;49;00m:: [34mhtml+jinja[39;49;00m$
$
    <[94mh1[39;49;00m>Sitemap$
    <[94mul[39;49;00m [36mid[39;49;00m=[33m"sitemap"[39;49;00m>$
    [36m{%[39;49;00m [34mfor[39;49;00m [31mitem[39;49;00m [34min[39;49;00m [31msitemap[39;49;00m [34mrecursive[39;49;00m [36m%}[39;49;00m$
      <[94mli[39;49;00m><[94ma[39;49;00m [36mhref[39;49;00m=[33m"[39;49;00m[36m{{[39;49;00m [31mitem[39;49;00m[31m.url[39;49;00m|[32me[39;49;00m [36m}}[39;49;00m[33m"[39;49;00m>[36m{{[39;49;00m [31mitem[39;49;00m[31m.title[39;49;00m|[32me[39;49;00m [36m}}[39;49;00m</[94ma[39;49;00m>$
      [36m{%[39;49;00m [34mif[39;49;00m [31mitem[39;49;00m[31m.children[39;49;00m [36m%}[39;49;00m<[94mul[39;49;00m>[36m{{[39;49;00m [36mloop[39;49;00m([31mitem[39;49;00m[31m.children[39;49;00m) [36m}}[39;49;00m</[94mul[39;49;00m>[36m{%[39;49;00m [34mendif[39;49;00m [36m%}[39;49;00m</[94mli[39;49;00m>$
    [36m{%[39;49;00m [34mendfor[39;49;00m [36m%}[39;49;00m$
    </[94mul[39;49;00m>$
$
What happens here? Basically the first thing that is different to a normal$
loop is the additional [33m``[39;49;00m[33mrecursive[39;49;00m[33m``[39;49;00m modifier in the [31m`for`[39;49;00m-loop declaration.$
It tells the template engine that we want recursion. If recursion is enabled$
the special [31m`loop`[39;49;00m variable is callable. If you call it with a sequence it will$
automatically render the loop at that position with the new sequence as argument.$
$
[01mCycling[39;49;00m$
[01m=======[39;49;00m$
$
Sometimes you might want to have different text snippets for each row in a list,$
for example to have alternating row colors. You can easily do this by using the$
[33m``[39;49;00m[33m{% cycle %}[39;49;00m[33m``[39;49;00m tag:$
$
.. [35msourcecode[39;49;00m:: [34mhtml+jinja[39;49;00m$
$
    <[94mul[39;49;00m [36mid[39;49;00m=[33m"messages"[39;49;00m>$
    [36m{%[39;49;00m [34mfor[39;49;00m [31mmessage[39;49;00m [34min[39;49;00m [31mmessages[39;49;00m [36m%}[39;49;00m$
      <[94mli[39;49;00m [36mclass[39;49;00m=[33m"[39;49;00m[36m{%[39;49;00m [34mcycle[39;49;00m [33m'row1'[39;49;00m, [33m'row2'[39;49;00m [36m%}[39;49;00m[33m"[39;49;00m>[36m{{[39;49;00m [31mmessage[39;49;00m|[32me[39;49;00m [36m}}[39;49;00m</[94mli[39;49;00m>$
    [36m{%[39;49;00m [34mendfor[39;49;00m [36m%}[39;49;00m$
    </[94mul[39;49;00m>$
$
Each time Jinja encounters a [31m`cycle`[39;49;00m tag it will cycle through the list$
of given items and return the next one. If you pass it one item jinja assumes$
that this item is a sequence from the context and uses this:$
$
.. [35msourcecode[39;49;00m:: [34mhtml+jinja[39;49;00m$
$
    <[94mli[39;49;00m [36mstyle[39;49;00m=[33m"color: [39;49;00m[36m{%[39;49;00m [34mcycle[39;49;00m [31mrowcolors[39;49;00m [36m%}[39;49;00m[33m"[39;49;00m>...</[94mli[39;49;00m>$
$
[01mConditions[39;49;00m$
[01m==========[39;49;00m$
$
Jinja supports Python-like [31m`if`[39;49;00m / [31m`elif`[39;49;00m / [31m`else`[39;49;00m constructs:$
$
.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
$
    [36m{%[39;49;00m [34mif[39;49;00m [31muser[39;49;00m[31m.active[39;49;00m [36m%}[39;49;00m$
        user [36m{{[39;49;00m [31muser[39;49;00m[31m.name[39;49;00m|[32me[39;49;00m [36m}}[39;49;00m is active.$
    [36m{%[39;49;00m [34melif[39;49;00m [31muser[39;49;00m[31m.deleted[39;49;00m [36m%}[39;49;00m$
        user [36m{{[39;49;00m [31muser[39;49;00m[31m.name[39;49;00m|[32me[39;49;00m [36m}}[39;49;00m was deleted some time ago.$
    [36m{%[39;49;00m [34melse[39;49;00m [36m%}[39;49;00m$
        i don't know what's wrong with [36m{{[39;49;00m [31muser[39;49;00m[31m.username[39;49;00m|[32me[39;49;00m [36m}}[39;49;00m$
    [36m{%[39;49;00m [34mendif[39;49;00m [36m%}[39;49;00m$
$
If the user is active the first block is rendered. If not and the user was$
deleted the second one, in all other cases the third one.$
$
You can also use comparison operators:$
$
.. [35msourcecode[39;49;00m:: [34mhtml+jinja[39;49;00m$
$
    [36m{%[39;49;00m [34mif[39;49;00m [31mamount[39;49;00m < [34m0[39;49;00m [36m%}[39;49;00m$
        <[94mspan[39;49;00m [36mstyle[39;49;00m=[33m"color: red"[39;49;00m>[36m{{[39;49;00m [31mamount[39;49;00m [36m}}[39;49;00m</[94mspan[39;49;00m>$
    [36m{%[39;49;00m [34melse[39;49;00m [36m%}[39;49;00m$
        <[94mspan[39;49;00m [36mstyle[39;49;00m=[33m"color: black"[39;49;00m>[36m{{[39;49;00m [31mamount[39;49;00m [36m}}[39;49;00m</[94mspan[39;49;00m>$
    [36m{%[39;49;00m [34mendif[39;49;00m [36m%}[39;49;00m$
$
.. [35madmonition[39;49;00m:: Note$
$
    Of course you can use [31m`or`[39;49;00m / [31m`and`[39;49;00m and parentheses to create more complex$
    conditions, but usually the logic is already handled in the application and$
    you don't have to create such complex constructs in the template code. However$
    in some situations it might be a good thing to have the abilities to create$
    them.$
$
[01mOperators[39;49;00m$
[01m=========[39;49;00m$
$
Inside [33m``[39;49;00m[33m{{ variable }}[39;49;00m[33m``[39;49;00m blocks, [31m`if`[39;49;00m conditions and many other parts you can$
can use expressions. In expressions you can use any of the following operators:$
$
    ======= ===================================================================$
    [33m``[39;49;00m[33m+[39;49;00m[33m``[39;49;00m   add the right operand to the left one.$
            [33m``[39;49;00m[33m{{ 1 + 2 }}[39;49;00m[33m``[39;49;00m would return [33m``[39;49;00m[33m3[39;49;00m[33m``[39;49;00m.$
    [33m``[39;49;00m[33m-[39;49;00m[33m``[39;49;00m   subtract the right operand from the left one.$
            [33m``[39;49;00m[33m{{ 1 - 1 }}[39;49;00m[33m``[39;49;00m would return [33m``[39;49;00m[33m0[39;49;00m[33m``[39;49;00m.$
    [33m``[39;49;00m[33m/[39;49;00m[33m``[39;49;00m   divide the left operand by the right one.$
            [33m``[39;49;00m[33m{{ 1 / 2 }}[39;49;00m[33m``[39;49;00m would return [33m``[39;49;00m[33m0.5[39;49;00m[33m``[39;49;00m.$
    [33m``[39;49;00m[33m*[39;49;00m[33m``[39;49;00m   multiply the left operand with the right one.$
            [33m``[39;49;00m[33m{{ 2 * 2 }}[39;49;00m[33m``[39;49;00m would return [33m``[39;49;00m[33m4[39;49;00m[33m``[39;49;00m.$
    [33m``[39;49;00m[33m**[39;49;00m[33m``[39;49;00m  raise the left operand to the power of the right$
            operand. [33m``[39;49;00m[33m{{ 2**3 }}[39;49;00m[33m``[39;49;00m would return [33m``[39;49;00m[33m8[39;49;00m[33m``[39;49;00m.$
    [33m``[39;49;00m[33min[39;49;00m[33m``[39;49;00m  perform sequence membership test. [33m``[39;49;00m[33m{{ 1 in [1,2,3] }}[39;49;00m[33m``[39;49;00m would$
            return true.$
    [33m``[39;49;00m[33mis[39;49;00m[33m``[39;49;00m  perform a test on the value. See the section about$
            tests for more information.$
    [33m``[39;49;00m[33m|[39;49;00m[33m``[39;49;00m   apply a filter on the value. See the section about$
            filters for more information.$
    [33m``[39;49;00m[33mand[39;49;00m[33m``[39;49;00m return true if the left and the right operand is true.$
    [33m``[39;49;00m[33mor[39;49;00m[33m``[39;49;00m  return true if the left or the right operand is true.$
    [33m``[39;49;00m[33mnot[39;49;00m[33m``[39;49;00m negate a statement (see below)$
    [33m``[39;49;00m[33m()[39;49;00m[33m``[39;49;00m  call a callable: [33m``[39;49;00m[33m{{ user.get_username() }}[39;49;00m[33m``[39;49;00m. Inside of the$
            parentheses you can use variables: [33m``[39;49;00m[33m{{ user.get(username) }}[39;49;00m[33m``[39;49;00m.$
    ======= ===================================================================$
$
Note that there is no support for any bit operations or something similar.$
$
[34m*[39;49;00m special note regarding [31m`not`[39;49;00m: The [31m`is`[39;49;00m and [31m`in`[39;49;00m operators support negation$
  using an infix notation too: [33m``[39;49;00m[33mfoo is not bar[39;49;00m[33m``[39;49;00m and [33m``[39;49;00m[33mfoo not in bar[39;49;00m[33m``[39;49;00m$
  instead of [33m``[39;49;00m[33mnot foo is bar[39;49;00m[33m``[39;49;00m and [33m``[39;49;00m[33mnot foo in bar[39;49;00m[33m``[39;49;00m. All other expressions$
  require a prefix notation: [33m``[39;49;00m[33mnot (foo and bar)[39;49;00m[33m``[39;49;00m.$
$
[01mBoolean Values[39;49;00m$
[01m==============[39;49;00m$
$
In If-Conditions Jinja performs a boolean check. All empty values (eg: empty$
lists [33m``[39;49;00m[33m[][39;49;00m[33m``[39;49;00m, empty dicts [33m``[39;49;00m[33m{}[39;49;00m[33m``[39;49;00m etc) evaluate to [31m`false`[39;49;00m. Numbers that are$
equal to [31m`0`[39;49;00m/[31m`0.00`[39;49;00m are considered [31m`false`[39;49;00m too. The boolean value of other$
objects depends on the behavior the application developer gave it. Usually$
items are [31m`true`[39;49;00m.$
$
Here some examples that should explain it:$
$
.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
$
    [36m{%[39;49;00m [34mif[39;49;00m [] [36m%}[39;49;00m$
        will always be false because it's an empty list$
$
    [36m{%[39;49;00m [34mif[39;49;00m {} [36m%}[39;49;00m$
        false too.$
$
    [36m{%[39;49;00m [34mif[39;49;00m [[33m'foo'[39;49;00m] [36m%}[39;49;00m$
        this is true. Because the list is not empty.$
$
    [36m{%[39;49;00m [34mif[39;49;00m [33m"foobar"[39;49;00m [36m%}[39;49;00m$
        this is also true because the string is not empty.$
$
[01mSlicing[39;49;00m$
[01m=======[39;49;00m$
$
Some objects support slicing operations. For example lists:$
$
.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
$
    [36m{%[39;49;00m [34mfor[39;49;00m [31mitem[39;49;00m [34min[39;49;00m [31mitems[39;49;00m[:[34m5[39;49;00m] [36m%}[39;49;00m$
        This will only iterate over the first 5 items of the list$
$
    [36m{%[39;49;00m [34mfor[39;49;00m [31mitem[39;49;00m [34min[39;49;00m [31mitems[39;49;00m[[34m5[39;49;00m:[34m1[39;49;00m[34m0[39;49;00m] [36m%}[39;49;00m$
        This will only iterate from item 5 to 10.$
$
    [36m{%[39;49;00m [34mfor[39;49;00m [31mitem[39;49;00m [34min[39;49;00m [31mitems[39;49;00m[:[34m1[39;49;00m[34m0[39;49;00m:[34m2[39;49;00m] [36m%}[39;49;00m$
        This will only yield items from start to ten and only returing$
        even items.$
$
For more informations about slicing have a look at the [33m`slicing chapter`_[39;49;00m$
in the "Dive into Python" e-book.$
$
[01mMacros[39;49;00m$
[01m======[39;49;00m$
$
If you want to use a partial template in more than one place, you might want to$
create a macro from it:$
$
.. [35msourcecode[39;49;00m:: [34mhtml+jinja[39;49;00m$
$
    [36m{%[39;49;00m [34mmacro[39;49;00m [31mshow_user[39;49;00m [31muser[39;49;00m [36m%}[39;49;00m$
      <[94mh1[39;49;00m>[36m{{[39;49;00m [31muser[39;49;00m[31m.name[39;49;00m|[32me[39;49;00m [36m}}[39;49;00m</[94mh1[39;49;00m>$
      <[94mdiv[39;49;00m [36mclass[39;49;00m=[33m"test"[39;49;00m>$
        [36m{{[39;49;00m [31muser[39;49;00m[31m.description[39;49;00m [36m}}[39;49;00m$
      </[94mdiv[39;49;00m>$
    [36m{%[39;49;00m [34mendmacro[39;49;00m [36m%}[39;49;00m$
$
Now you can use it from everywhere in the code by passing it an item:$
$
.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
    $
    [36m{%[39;49;00m [34mfor[39;49;00m [31muser[39;49;00m [34min[39;49;00m [31musers[39;49;00m [36m%}[39;49;00m$
        [36m{{[39;49;00m [31mshow_user[39;49;00m([31muser[39;49;00m) [36m}}[39;49;00m$
    [36m{%[39;49;00m [34mendfor[39;49;00m [36m%}[39;49;00m$
$
You can also specify more than one value:$
$
.. [35msourcecode[39;49;00m:: [34mhtml+jinja[39;49;00m$
$
    [36m{%[39;49;00m [34mmacro[39;49;00m [31mshow_dialog[39;49;00m [31mtitle[39;49;00m, [31mtext[39;49;00m [36m%}[39;49;00m$
      <[94mdiv[39;49;00m [36mclass[39;49;00m=[33m"dialog"[39;49;00m>$
        <[94mh1[39;49;00m>[36m{{[39;49;00m [31mtitle[39;49;00m|[32me[39;49;00m [36m}}[39;49;00m</[94mh1[39;49;00m>$
        <[94mdiv[39;49;00m [36mclass[39;49;00m=[33m"test"[39;49;00m>[36m{{[39;49;00m [31mtext[39;49;00m|[32me[39;49;00m [36m}}[39;49;00m</[94mdiv[39;49;00m>$
      </[94mdiv[39;49;00m>$
    [36m{%[39;49;00m [34mendmacro[39;49;00m [36m%}[39;49;00m$
$
    [36m{{[39;49;00m [31mshow_dialog[39;49;00m([33m'Warning'[39;49;00m, [33m'something went wrong i guess'[39;49;00m) [36m}}[39;49;00m$
$
[01mInheritance[39;49;00m$
[01m===========[39;49;00m$
$
The most powerful part of Jinja is template inheritance. Template inheritance$
allows you to build a base "skeleton" template that contains all the common$
elements of your site and defines **blocks** that child templates can override.$
$
Sounds complicated but is very basic. It's easiest to understand it by starting$
with an example.$
$
[01mBase Template[39;49;00m$
[01m-------------[39;49;00m$
$
This template, which we'll call [33m``[39;49;00m[33mbase.html[39;49;00m[33m``[39;49;00m, defines a simple HTML skeleton$
document that you might use for a simple two-column page. It's the job of$
"child" templates to fill the empty blocks with content:$
$
.. [35msourcecode[39;49;00m:: [34mhtml+jinja[39;49;00m$
$
    [36m<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"[39;49;00m$
    [36m "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">[39;49;00m$
    <[94mhtml[39;49;00m [36mxmlns[39;49;00m=[33m"http://www.w3.org/1999/xhtml"[39;49;00m>$
    <[94mhead[39;49;00m>$
      <[94mlink[39;49;00m [36mrel[39;49;00m=[33m"stylesheet"[39;49;00m [36mhref[39;49;00m=[33m"style.css"[39;49;00m />$
      <[94mtitle[39;49;00m>[36m{%[39;49;00m [34mblock[39;49;00m [31mtitle[39;49;00m [36m%}[39;49;00m[36m{%[39;49;00m [34mendblock[39;49;00m [36m%}[39;49;00m - My Webpage</[94mtitle[39;49;00m>$
      [36m{%[39;49;00m [34mblock[39;49;00m [31mhtml_head[39;49;00m [36m%}[39;49;00m[36m{%[39;49;00m [34mendblock[39;49;00m [36m%}[39;49;00m$
    </[94mhead[39;49;00m>$
    <[94mbody[39;49;00m>$
      <[94mdiv[39;49;00m [36mid[39;49;00m=[33m"content"[39;49;00m>$
        [36m{%[39;49;00m [34mblock[39;49;00m [31mcontent[39;49;00m [36m%}[39;49;00m[36m{%[39;49;00m [34mendblock[39;49;00m [36m%}[39;49;00m$
      </[94mdiv[39;49;00m>$
$
      <[94mdiv[39;49;00m [36mid[39;49;00m=[33m"footer"[39;49;00m>$
        [36m{%[39;49;00m [34mblock[39;49;00m [31mfooter[39;49;00m [36m%}[39;49;00m$
        &copy; Copyright 2006 by <[94ma[39;49;00m [36mhref[39;49;00m=[33m"http://mydomain.tld"[39;49;00m>myself</[94ma[39;49;00m>.$
        [36m{%[39;49;00m [34mendblock[39;49;00m [36m%}[39;49;00m$
      </[94mdiv[39;49;00m>$
    </[94mbody[39;49;00m>$
$
In this example, the [33m``[39;49;00m[33m{% block %}[39;49;00m[33m``[39;49;00m tags define four blocks that child templates$
can fill in. All the [31m`block`[39;49;00m tag does is to tell the template engine that a$
child template may override those portions of the template.$
$
[01mChild Template[39;49;00m$
[01m--------------[39;49;00m$
$
A child template might look like this:$
$
.. [35msourcecode[39;49;00m:: [34mhtml+jinja[39;49;00m$
$
    [36m{%[39;49;00m [34mextends[39;49;00m [33m"base.html"[39;49;00m [36m%}[39;49;00m$
    [36m{%[39;49;00m [34mblock[39;49;00m [31mtitle[39;49;00m [36m%}[39;49;00mIndex[36m{%[39;49;00m [34mendblock[39;49;00m [36m%}[39;49;00m$
$
    [36m{%[39;49;00m [34mblock[39;49;00m [31mhtml_head[39;49;00m [36m%}[39;49;00m$
      <[94mstyle[39;49;00m [36mtype[39;49;00m=[33m"text/css"[39;49;00m>[37m[39;49;00m$
    [37m    [39;49;00m.[04m[32mimportant[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
    [37m      [39;49;00m[34mcolor[39;49;00m:[37m [39;49;00m[34m#336699[39;49;00m;[37m[39;49;00m$
    [37m    [39;49;00m}[37m[39;49;00m$
    [37m  [39;49;00m</[94mstyle[39;49;00m>$
    [36m{%[39;49;00m [34mendblock[39;49;00m [36m%}[39;49;00m$
    $
    [36m{%[39;49;00m [34mblock[39;49;00m [31mcontent[39;49;00m [36m%}[39;49;00m$
        <[94mh1[39;49;00m>Index</[94mh1[39;49;00m>$
        <[94mp[39;49;00m [36mclass[39;49;00m=[33m"important"[39;49;00m>$
          Welcome on my awsome homepage.$
        </[94mp[39;49;00m>$
    [36m{%[39;49;00m [34mendblock[39;49;00m [36m%}[39;49;00m$
$
The [33m``[39;49;00m[33m{% extends %}[39;49;00m[33m``[39;49;00m tag is the key here. It tells the template engine that$
this template "extends" another template. When the template system evaluates$
this template, first it locates the parent.$
$
The filename of the template depends on the template loader. For example the$
[33m``[39;49;00m[33mFileSystemLoader[39;49;00m[33m``[39;49;00m allows you to access other templates by giving the$
filename. You can access templates in subdirectories with an slash:$
$
.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
$
    [36m{%[39;49;00m [34mextends[39;49;00m [33m"layout/default.html"[39;49;00m [36m%}[39;49;00m$
$
But this behavior can depend on the application using Jinja.$
$
Note that since the child template didn't define the [33m``[39;49;00m[33mfooter[39;49;00m[33m``[39;49;00m block, the$
value from the parent template is used instead.$
$
.. [35madmonition[39;49;00m:: Note$
$
    You can't define multiple [33m``[39;49;00m[33m{% block %}[39;49;00m[33m``[39;49;00m tags with the same name in the$
    same template. This limitation exists because a block tag works in "both"$
    directions. That is, a block tag doesn't just provide a hole to fill - it$
    also defines the content that fills the hole in the *parent*. If there were$
    two similarly-named [33m``[39;49;00m[33m{% block %}[39;49;00m[33m``[39;49;00m tags in a template, that template's$
    parent wouldn't know which one of the blocks' content to use.$
$
[01mTemplate Inclusion[39;49;00m$
[01m==================[39;49;00m$
$
You can load another template at a given position using [33m``[39;49;00m[33m{% include %}[39;49;00m[33m``[39;49;00m.$
Usually it's a better idea to use inheritance but if you for example want to$
load macros, [31m`include`[39;49;00m works better than [31m`extends`[39;49;00m:$
$
.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
$
    [36m{%[39;49;00m [34minclude[39;49;00m [33m"myhelpers.html"[39;49;00m [36m%}[39;49;00m$
    [36m{{[39;49;00m [31mmy_helper[39;49;00m([33m"foo"[39;49;00m) [36m}}[39;49;00m$
$
If you define a macro called [33m``[39;49;00m[33mmy_helper[39;49;00m[33m``[39;49;00m in [33m``[39;49;00m[33mmyhelpers.html[39;49;00m[33m``[39;49;00m, you can now$
use it from the template as shown above.$
$
[01mFiltering Blocks[39;49;00m$
[01m================[39;49;00m$
$
Sometimes it could be a good idea to filter a complete block of text. For$
example, if you want to escape some html code:$
$
.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
$
    [36m{%[39;49;00m [34mfilter[39;49;00m [32mescape[39;49;00m [36m%}[39;49;00m$
        <html>$
          <code>goes here</code>$
        </html>$
    [36m{%[39;49;00m [34mendfilter[39;49;00m [36m%}[39;49;00m$
$
Of course you can chain filters too:$
$
.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
$
    [36m{%[39;49;00m [34mfilter[39;49;00m [32mlower[39;49;00m|[32mescape[39;49;00m [36m%}[39;49;00m$
        <B>SOME TEXT</B>$
    [36m{%[39;49;00m [34mendfilter[39;49;00m [36m%}[39;49;00m$
$
returns [33m``[39;49;00m[33m"&lt;b&gt;some text&lt;/b&gt;"[39;49;00m[33m``[39;49;00m.$
$
[01mDefining Variables[39;49;00m$
[01m==================[39;49;00m$
$
You can also define variables in the namespace using the [33m``[39;49;00m[33m{% set %}[39;49;00m[33m``[39;49;00m tag:$
$
.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
$
    [36m{%[39;49;00m [34mset[39;49;00m [31mfoo[39;49;00m = [33m'foobar'[39;49;00m [36m%}[39;49;00m$
    [36m{{[39;49;00m [31mfoo[39;49;00m [36m}}[39;49;00m$
$
This should ouput [33m``[39;49;00m[33mfoobar[39;49;00m[33m``[39;49;00m.$
$
[01mScopes[39;49;00m$
[01m======[39;49;00m$
$
Jinja has multiple scopes. A scope is something like a new transparent foil on$
a stack of foils. You can only write to the outermost foil but read all of them$
since you can look through them. If you remove the top foil all data on that$
foil disappears. Some tags in Jinja add a new layer to the stack. Currently$
these are [31m`block`[39;49;00m, [31m`for`[39;49;00m, [31m`macro`[39;49;00m and [31m`filter`[39;49;00m. This means that variables and$
other elements defined inside a macro, loop or some of the other tags listed$
above will be only available in that block. Here an example:$
$
.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
$
    [36m{%[39;49;00m [34mmacro[39;49;00m [31mangryhello[39;49;00m [31mname[39;49;00m [36m%}[39;49;00m$
      [36m{%[39;49;00m [34mset[39;49;00m [31mangryname[39;49;00m = [31mname[39;49;00m|[32mupper[39;49;00m [36m%}[39;49;00m$
      Hello [36m{{[39;49;00m [31mname[39;49;00m [36m}}[39;49;00m. Hello [36m{{[39;49;00m [31mname[39;49;00m [36m}}[39;49;00m!$
      HELLO [36m{{[39;49;00m [31mangryname[39;49;00m [36m}}[39;49;00m!!!!!!111$
    [36m{%[39;49;00m [34mendmacro[39;49;00m [36m%}[39;49;00m$
$
The variable [33m``[39;49;00m[33mangryname[39;49;00m[33m``[39;49;00m just exists inside the macro, not outside it.$
$
Defined macros appear on the context as variables. Because of this, they are$
affected by the scoping too. A macro defined inside of a macro is just available$
in those two macros (the macro itself and the macro it's defined in). For [31m`set`[39;49;00m$
and [31m`macro`[39;49;00m two additional rules exist: If a macro is defined in an extended$
template but outside of a visible block (thus outside of any block) will be$
available in all blocks below. This allows you to use [31m`include`[39;49;00m statements to$
load often used macros at once.$
$
[01mUndefined Variables[39;49;00m$
[01m===================[39;49;00m$
$
If you have already worked with python you probably know about the fact that$
undefined variables raise an exception. This is different in Jinja. There is a$
special value called [31m`undefined`[39;49;00m that represents values that do not exist.$
$
This special variable works complete different from any variables you maybe$
know. If you print it using [33m``[39;49;00m[33m{{ variable }}[39;49;00m[33m``[39;49;00m it will not appear because it's$
literally empty. If you try to iterate over it, it will work. But no items$
are returned. Comparing this value to any other value results in [31m`false`[39;49;00m.$
Even if you compare it to itself:$
$
.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
$
    [36m{{[39;49;00m [31mundefined[39;49;00m == [31mundefined[39;49;00m [36m}}[39;49;00m$
        will return false. Not even undefined is undefined :)$
        Use `is defined` / `is not defined`:$
$
    [36m{{[39;49;00m [31mundefined[39;49;00m [34mis[39;49;00m [34mnot[39;49;00m [32mdefined[39;49;00m [36m}}[39;49;00m$
        will return true.$
$
There are also some additional rules regarding this special value. Any$
mathematical operators ([33m``[39;49;00m[33m+[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33m-[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33m*[39;49;00m[33m``[39;49;00m, [33m``[39;49;00m[33m/[39;49;00m[33m``[39;49;00m) return the operand$
as result:$
$
.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
$
    [36m{{[39;49;00m [31mundefined[39;49;00m + [33m"foo"[39;49;00m [36m}}[39;49;00m$
        returns "foo"$
$
    [36m{{[39;49;00m [31mundefined[39;49;00m - [34m4[39;49;00m[34m2[39;49;00m [36m}}[39;49;00m$
        returns 42. Note: not -42!$
$
In any expression [31m`undefined`[39;49;00m evaluates to [31m`false`[39;49;00m. It has no length, all$
attribute calls return undefined, calling too:$
$
.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
$
    [36m{{[39;49;00m [31mundefined[39;49;00m[31m.attribute[39;49;00m()[31m.attribute_too[39;49;00m[[34m4[39;49;00m[34m2[39;49;00m] [36m}}[39;49;00m$
        still returns `undefined`.$
$
[01mEscaping[39;49;00m$
[01m========[39;49;00m$
$
Sometimes you might want to add Jinja syntax elements into the template$
without executing them. In that case you have quite a few possibilities.$
$
For small parts this might be a good way:$
$
.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
$
    [36m{{[39;49;00m [33m"{{ foo }} is variable syntax and {% foo %} is block syntax"[39;49;00m [36m}}[39;49;00m$
$
When you have multiple elements you can use the [33m``[39;49;00m[33mraw[39;49;00m[33m``[39;49;00m block:$
$
.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
$
    [36m{%[39;49;00m [34mraw[39;49;00m [36m%}[39;49;00m$
        Filtering blocks works like this in Jinja:$
        {% filter escape %}$
            <html>$
              <code>goes here</code>$
            </html>$
        {% endfilter %}$
    [36m{%[39;49;00m [34mendraw[39;49;00m [36m%}[39;49;00m$
$
[01mReserved Keywords[39;49;00m$
[01m=================[39;49;00m$
$
Jinja has some keywords you cannot use a variable names. This limitation$
exists to make look coherent. Syntax highlighters won't mess things up and$
you will don't have unexpected output.$
$
The following keywords exist and cannot be used as identifiers:$
$
    [31m`and`[39;49;00m, [31m`block`[39;49;00m, [31m`cycle`[39;49;00m, [31m`elif`[39;49;00m, [31m`else`[39;49;00m, [31m`endblock`[39;49;00m, [31m`endfilter`[39;49;00m,$
    [31m`endfor`[39;49;00m, [31m`endif`[39;49;00m, [31m`endmacro`[39;49;00m, [31m`endraw`[39;49;00m, [31m`endtrans`[39;49;00m, [31m`extends`[39;49;00m, [31m`filter`[39;49;00m,$
    [31m`for`[39;49;00m, [31m`if`[39;49;00m, [31m`in`[39;49;00m, [31m`include`[39;49;00m, [31m`is`[39;49;00m, [31m`macro`[39;49;00m, [31m`not`[39;49;00m, [31m`or`[39;49;00m, [31m`pluralize`[39;49;00m,$
    [31m`raw`[39;49;00m, [31m`recursive`[39;49;00m, [31m`set`[39;49;00m, [31m`trans`[39;49;00m$
$
If you want to use such a name you have to prefix or suffix it or use$
alternative names:$
$
.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
$
    [36m{%[39;49;00m [34mfor[39;49;00m [31mmacro_[39;49;00m [34min[39;49;00m [31mmacros[39;49;00m [36m%}[39;49;00m$
        [36m{{[39;49;00m [31mmacro_[39;49;00m([33m'foo'[39;49;00m) [36m}}[39;49;00m$
    [36m{%[39;49;00m [34mendfor[39;49;00m [36m%}[39;49;00m$
$
If future Jinja releases add new keywords those will be "light" keywords which$
means that they won't raise an error for several releases but yield warnings$
on the application side. But it's very unlikely that new keywords will be$
added.$
$
[01mInternationalization[39;49;00m$
[01m====================[39;49;00m$
$
If the application is configured for i18n, you can define translatable blocks$
for translators using the [31m`trans`[39;49;00m tag or the special underscore function:$
$
.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
$
    [36m{%[39;49;00m [34mtrans[39;49;00m [36m%}[39;49;00m$
        this is a translatable block$
    [36m{%[39;49;00m [34mendtrans[39;49;00m [36m%}[39;49;00m$
$
    [36m{%[39;49;00m [34mtrans[39;49;00m [33m"This is a translatable string"[39;49;00m [36m%}[39;49;00m$
$
    [36m{{[39;49;00m [34m_[39;49;00m([33m"This is a translatable string"[39;49;00m) [36m}}[39;49;00m$
$
The latter one is useful if you want translatable arguments for filters etc.$
$
If you want to have plural forms too, use the [31m`pluralize`[39;49;00m block:$
$
.. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
$
    [36m{%[39;49;00m [34mtrans[39;49;00m [31musers[39;49;00m=[31musers[39;49;00m [36m%}[39;49;00m$
        One user found.$
    [36m{%[39;49;00m [34mpluralize[39;49;00m [36m%}[39;49;00m$
        [36m{{[39;49;00m [31musers[39;49;00m [36m}}[39;49;00m users found.$
    [36m{%[39;49;00m [34mendtrans[39;49;00m [36m%}[39;49;00m$
$
    [36m{%[39;49;00m [34mtrans[39;49;00m [31mfirst[39;49;00m=([31musers[39;49;00m|[32mfirst[39;49;00m)[31m.username[39;49;00m|[32mescape[39;49;00m, [31muser[39;49;00m=[31musers[39;49;00m|[32mlength[39;49;00m [36m%}[39;49;00m$
        one user [36m{{[39;49;00m [31mfirst[39;49;00m [36m}}[39;49;00m found.$
    [36m{%[39;49;00m [34mpluralize[39;49;00m [31musers[39;49;00m [36m%}[39;49;00m$
        [36m{{[39;49;00m [31musers[39;49;00m [36m}}[39;49;00m users found, the first one is called [36m{{[39;49;00m [31mfirst[39;49;00m [36m}}[39;49;00m.$
    [36m{%[39;49;00m [34mendtrans[39;49;00m [36m%}[39;49;00m$
$
If you have multiple arguments, the first one is assumed to be the indicator (the$
number that is used to determine the correct singular or plural form. If you$
don't have the indicator variable on position 1 you have to tell the [31m`pluralize`[39;49;00m$
tag the correct variable name.$
$
Inside translatable blocks you cannot use blocks or expressions (however you can$
still use the [33m``[39;49;00m[33mraw[39;49;00m[33m``[39;49;00m block which will work as expected). The variable$
print syntax ([33m``[39;49;00m[33m{{ variablename }}[39;49;00m[33m``[39;49;00m) is the only way to insert the variables$
defined in the [33m``[39;49;00m[33mtrans[39;49;00m[33m``[39;49;00m header. Filters must be applied in the header.$
$
.. [35madmonition[39;49;00m:: note$
$
    Please make sure that you always use pluralize blocks where required.$
    Many languages have more complex plural forms than the English language.$
    $
    Never try to workaround that issue by using something like this:$
$
    .. [35msourcecode[39;49;00m:: [34mjinja[39;49;00m$
$
        [36m{%[39;49;00m [34mif[39;49;00m [31mcount[39;49;00m != [34m1[39;49;00m [36m%}[39;49;00m$
            [36m{{[39;49;00m [31mcount[39;49;00m [36m}}[39;49;00m users found.$
        [36m{%[39;49;00m [34melse[39;49;00m [36m%}[39;49;00m$
            one user found.$
        [36m{%[39;49;00m [34mendif[39;49;00m [36m%}[39;49;00m$
$
.. [94m_slicing chapter:[39;49;00m http://diveintopython.org/native_data_types/lists.html#odbchelper.list.slice$
.. [94m_range function:[39;49;00m http://docs.python.org/tut/node6.html#SECTION006300000000000000000$

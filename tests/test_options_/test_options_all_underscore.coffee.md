     1^I[37m  [39;49;00m[37m# Underscore.coffee[39;49;00m[37m[39;49;00m$
     2^I[37m  [39;49;00m[37m# (c) 2010 Jeremy Ashkenas, DocumentCloud Inc.[39;49;00m[37m[39;49;00m$
     3^I[37m  [39;49;00m[37m# Underscore is freely distributable under the terms of the MIT license.[39;49;00m[37m[39;49;00m$
     4^I[37m  [39;49;00m[37m# Portions of Underscore are inspired by or borrowed from Prototype.js,[39;49;00m[37m[39;49;00m$
     5^I[37m  [39;49;00m[37m# Oliver Steele's Functional, and John Resig's Micro-Templating.[39;49;00m[37m[39;49;00m$
     6^I[37m  [39;49;00m[37m# For all details and documentation:[39;49;00m[37m[39;49;00m$
     7^I[37m  [39;49;00m[37m# http://documentcloud.github.com/underscore/[39;49;00m[37m[39;49;00m$
     8^I[37m[39;49;00m$
     9^I[37m[39;49;00m$
    10^I[37m  [39;49;00m[37m# ------------------------- Baseline setup ---------------------------------[39;49;00m[37m[39;49;00m$
    11^I[37m[39;49;00m$
    12^I[37m  [39;49;00m[37m# Establish the root object, "window" in the browser, or "global" on the server.[39;49;00m[37m[39;49;00m$
    13^I[37m  [39;49;00m[31mroot[39;49;00m:[37m [39;49;00m[34mthis[39;49;00m[37m[39;49;00m$
    14^I[37m[39;49;00m$
    15^I[37m[39;49;00m$
    16^I[37m  [39;49;00m[37m# Save the previous value of the "_" variable.[39;49;00m[37m[39;49;00m$
    17^I[37m  [39;49;00m[31mpreviousUnderscore[39;49;00m:[37m [39;49;00mroot._[37m[39;49;00m$
    18^I[37m[39;49;00m$
    19^I[37m[39;49;00m$
    20^I[37m  [39;49;00m[37m# If Underscore is called as a function, it returns a wrapped object that[39;49;00m[37m[39;49;00m$
    21^I[37m  [39;49;00m[37m# can be used OO-style. This wrapper holds altered versions of all the[39;49;00m[37m[39;49;00m$
    22^I[37m  [39;49;00m[37m# underscore functions. Wrapped objects may be chained.[39;49;00m[37m[39;49;00m$
    23^I[37m  [39;49;00m[31mwrapper[39;49;00m:[37m [39;49;00m[32m(obj) ->[39;49;00m[37m[39;49;00m$
    24^I[37m    [39;49;00m[34mthis[39;49;00m.[31m_wrapped[39;49;00m:[37m [39;49;00mobj[37m[39;49;00m$
    25^I[37m    [39;49;00m[34mthis[39;49;00m[37m[39;49;00m$
    26^I[37m[39;49;00m$
    27^I[37m[39;49;00m$
    28^I[37m  [39;49;00m[37m# Establish the object that gets thrown to break out of a loop iteration.[39;49;00m[37m[39;49;00m$
    29^I[37m  [39;49;00m[31mbreaker[39;49;00m:[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m[34mtypeof[39;49;00m(StopIteration)[37m [39;49;00mis[37m [39;49;00m[33m'[39;49;00m[33mundefined[39;49;00m[33m'[39;49;00m[37m [39;49;00m[34mthen[39;49;00m[37m [39;49;00m[33m'[39;49;00m[33m__break__[39;49;00m[33m'[39;49;00m[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00mStopIteration[37m[39;49;00m$
    30^I[37m[39;49;00m$
    31^I[37m[39;49;00m$
    32^I[37m  [39;49;00m[37m# Create a safe reference to the Underscore object forreference below.[39;49;00m[37m[39;49;00m$
    33^I[37m  [39;49;00m[31m_[39;49;00m:[37m [39;49;00m[31mroot._[39;49;00m:[37m [39;49;00m[32m(obj) ->[39;49;00m[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mwrapper(obj)[37m[39;49;00m$
    34^I[37m[39;49;00m$
    35^I[37m[39;49;00m$
    36^I[37m  [39;49;00m[37m# Export the Underscore object for CommonJS.[39;49;00m[37m[39;49;00m$
    37^I[37m  [39;49;00m[34mif[39;49;00m[37m [39;49;00m[34mtypeof[39;49;00m(exports)[37m [39;49;00m!=[37m [39;49;00m[33m'[39;49;00m[33mundefined[39;49;00m[33m'[39;49;00m[37m [39;49;00m[34mthen[39;49;00m[37m [39;49;00m[31mexports._[39;49;00m:[37m [39;49;00m_[37m[39;49;00m$
    38^I[37m[39;49;00m$
    39^I[37m[39;49;00m$
    40^I[37m  [39;49;00m[37m# Create quick reference variables for speed access to core prototypes.[39;49;00m[37m[39;49;00m$
    41^I[37m  [39;49;00m[31mslice[39;49;00m:[37m                [39;49;00m[36mArray[39;49;00m::slice[37m[39;49;00m$
    42^I[37m  [39;49;00m[31munshift[39;49;00m:[37m              [39;49;00m[36mArray[39;49;00m::unshift[37m[39;49;00m$
    43^I[37m  [39;49;00m[31mtoString[39;49;00m:[37m             [39;49;00m[36mObject[39;49;00m::toString[37m[39;49;00m$
    44^I[37m  [39;49;00m[31mhasOwnProperty[39;49;00m:[37m       [39;49;00m[36mObject[39;49;00m::hasOwnProperty[37m[39;49;00m$
    45^I[37m  [39;49;00m[31mpropertyIsEnumerable[39;49;00m:[37m [39;49;00m[36mObject[39;49;00m::propertyIsEnumerable[37m[39;49;00m$
    46^I[37m[39;49;00m$
    47^I[37m[39;49;00m$
    48^I[37m  [39;49;00m[37m# Current version.[39;49;00m[37m[39;49;00m$
    49^I[37m  [39;49;00m[31m_.VERSION[39;49;00m:[37m [39;49;00m[33m'[39;49;00m[33m0.5.7[39;49;00m[33m'[39;49;00m[37m[39;49;00m$
    50^I[37m[39;49;00m$
    51^I[37m[39;49;00m$
    52^I[37m  [39;49;00m[37m# ------------------------ Collection Functions: ---------------------------[39;49;00m[37m[39;49;00m$
    53^I[37m[39;49;00m$
    54^I[37m  [39;49;00m[37m# The cornerstone, an each implementation.[39;49;00m[37m[39;49;00m$
    55^I[37m  [39;49;00m[37m# Handles objects implementing forEach, arrays, and raw objects.[39;49;00m[37m[39;49;00m$
    56^I[37m  [39;49;00m[31m_.each[39;49;00m:[37m [39;49;00m[32m(obj, iterator, context) ->[39;49;00m[37m[39;49;00m$
    57^I[37m    [39;49;00m[31mindex[39;49;00m:[37m [39;49;00m[34m0[39;49;00m[37m[39;49;00m$
    58^I[37m    [39;49;00m[34mtry[39;49;00m[37m[39;49;00m$
    59^I[37m      [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mobj.forEach(iterator,[37m [39;49;00mcontext)[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00mobj.forEach[37m[39;49;00m$
    60^I[37m      [39;49;00m[34mif[39;49;00m[37m [39;49;00m_.isArray(obj)[37m [39;49;00mor[37m [39;49;00m_.isArguments(obj)[37m[39;49;00m$
    61^I[37m        [39;49;00m[34mreturn[39;49;00m[37m [39;49;00miterator.call(context,[37m [39;49;00mobj[i],[37m [39;49;00mi,[37m [39;49;00mobj)[37m [39;49;00m[34mfor[39;49;00m[37m [39;49;00mi[37m [39;49;00m[34min[39;49;00m[37m [39;49;00m[[34m0[39;49;00m...obj.length][37m[39;49;00m$
    62^I[37m      [39;49;00miterator.call(context,[37m [39;49;00mval,[37m [39;49;00mkey,[37m [39;49;00mobj)[37m [39;49;00m[34mfor[39;49;00m[37m [39;49;00mkey,[37m [39;49;00mval[37m [39;49;00m[34mof[39;49;00m[37m [39;49;00mobj[37m[39;49;00m$
    63^I[37m    [39;49;00m[34mcatch[39;49;00m[37m [39;49;00me[37m[39;49;00m$
    64^I[37m      [39;49;00m[34mthrow[39;49;00m[37m [39;49;00me[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00me[37m [39;49;00misnt[37m [39;49;00mbreaker[37m[39;49;00m$
    65^I[37m    [39;49;00mobj[37m[39;49;00m$
    66^I[37m[39;49;00m$
    67^I[37m[39;49;00m$
    68^I[37m  [39;49;00m[37m# Return the results of applying the iterator to each element. Use JavaScript[39;49;00m[37m[39;49;00m$
    69^I[37m  [39;49;00m[37m# 1.6's version of map, if possible.[39;49;00m[37m[39;49;00m$
    70^I[37m  [39;49;00m[31m_.map[39;49;00m:[37m [39;49;00m[32m(obj, iterator, context) ->[39;49;00m[37m[39;49;00m$
    71^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mobj.map(iterator,[37m [39;49;00mcontext)[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(obj[37m [39;49;00mand[37m [39;49;00m_.isFunction(obj.map))[37m[39;49;00m$
    72^I[37m    [39;49;00m[31mresults[39;49;00m:[37m [39;49;00m[][37m[39;49;00m$
    73^I[37m    [39;49;00m_.each[37m [39;49;00mobj,[37m [39;49;00m[32m(value, index, list) ->[39;49;00m[37m[39;49;00m$
    74^I[37m      [39;49;00mresults.push(iterator.call(context,[37m [39;49;00mvalue,[37m [39;49;00mindex,[37m [39;49;00mlist))[37m[39;49;00m$
    75^I[37m    [39;49;00mresults[37m[39;49;00m$
    76^I[37m[39;49;00m$
    77^I[37m[39;49;00m$
    78^I[37m  [39;49;00m[37m# Reduce builds up a single result from a list of values. Also known as[39;49;00m[37m[39;49;00m$
    79^I[37m  [39;49;00m[37m# inject, or foldl. Uses JavaScript 1.8's version of reduce, if possible.[39;49;00m[37m[39;49;00m$
    80^I[37m  [39;49;00m[31m_.reduce[39;49;00m:[37m [39;49;00m[32m(obj, memo, iterator, context) ->[39;49;00m[37m[39;49;00m$
    81^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mobj.reduce(_.bind(iterator,[37m [39;49;00mcontext),[37m [39;49;00mmemo)[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(obj[37m [39;49;00mand[37m [39;49;00m_.isFunction(obj.reduce))[37m[39;49;00m$
    82^I[37m    [39;49;00m_.each[37m [39;49;00mobj,[37m [39;49;00m[32m(value, index, list) ->[39;49;00m[37m[39;49;00m$
    83^I[37m      [39;49;00m[31mmemo[39;49;00m:[37m [39;49;00miterator.call(context,[37m [39;49;00mmemo,[37m [39;49;00mvalue,[37m [39;49;00mindex,[37m [39;49;00mlist)[37m[39;49;00m$
    84^I[37m    [39;49;00mmemo[37m[39;49;00m$
    85^I[37m[39;49;00m$
    86^I[37m[39;49;00m$
    87^I[37m  [39;49;00m[37m# The right-associative version of reduce, also known as foldr. Uses[39;49;00m[37m[39;49;00m$
    88^I[37m  [39;49;00m[37m# JavaScript 1.8's version of reduceRight, if available.[39;49;00m[37m[39;49;00m$
    89^I[37m  [39;49;00m[31m_.reduceRight[39;49;00m:[37m [39;49;00m[32m(obj, memo, iterator, context) ->[39;49;00m[37m[39;49;00m$
    90^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mobj.reduceRight(_.bind(iterator,[37m [39;49;00mcontext),[37m [39;49;00mmemo)[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(obj[37m [39;49;00mand[37m [39;49;00m_.isFunction(obj.reduceRight))[37m[39;49;00m$
    91^I[37m    [39;49;00m_.each[37m [39;49;00m_.clone(_.toArray(obj)).reverse(),[37m [39;49;00m[32m(value, index) ->[39;49;00m[37m[39;49;00m$
    92^I[37m      [39;49;00m[31mmemo[39;49;00m:[37m [39;49;00miterator.call(context,[37m [39;49;00mmemo,[37m [39;49;00mvalue,[37m [39;49;00mindex,[37m [39;49;00mobj)[37m[39;49;00m$
    93^I[37m    [39;49;00mmemo[37m[39;49;00m$
    94^I[37m[39;49;00m$
    95^I[37m[39;49;00m$
    96^I[37m  [39;49;00m[37m# Return the first value which passes a truth test.[39;49;00m[37m[39;49;00m$
    97^I[37m  [39;49;00m[31m_.detect[39;49;00m:[37m [39;49;00m[32m(obj, iterator, context) ->[39;49;00m[37m[39;49;00m$
    98^I[37m    [39;49;00m[31mresult[39;49;00m:[37m [39;49;00m[34mnull[39;49;00m[37m[39;49;00m$
    99^I[37m    [39;49;00m_.each[37m [39;49;00mobj,[37m [39;49;00m[32m(value, index, list) ->[39;49;00m[37m[39;49;00m$
   100^I[37m      [39;49;00m[34mif[39;49;00m[37m [39;49;00miterator.call(context,[37m [39;49;00mvalue,[37m [39;49;00mindex,[37m [39;49;00mlist)[37m[39;49;00m$
   101^I[37m        [39;49;00m[31mresult[39;49;00m:[37m [39;49;00mvalue[37m[39;49;00m$
   102^I[37m        [39;49;00m_.breakLoop()[37m[39;49;00m$
   103^I[37m    [39;49;00mresult[37m[39;49;00m$
   104^I[37m[39;49;00m$
   105^I[37m[39;49;00m$
   106^I[37m  [39;49;00m[37m# Return all the elements that pass a truth test. Use JavaScript 1.6's[39;49;00m[37m[39;49;00m$
   107^I[37m  [39;49;00m[37m# filter(), if it exists.[39;49;00m[37m[39;49;00m$
   108^I[37m  [39;49;00m[31m_.select[39;49;00m:[37m [39;49;00m[32m(obj, iterator, context) ->[39;49;00m[37m[39;49;00m$
   109^I[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00mobj[37m [39;49;00mand[37m [39;49;00m_.isFunction(obj.filter)[37m [39;49;00m[34mthen[39;49;00m[37m [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mobj.filter(iterator,[37m [39;49;00mcontext)[37m[39;49;00m$
   110^I[37m    [39;49;00m[31mresults[39;49;00m:[37m [39;49;00m[][37m[39;49;00m$
   111^I[37m    [39;49;00m_.each[37m [39;49;00mobj,[37m [39;49;00m[32m(value, index, list) ->[39;49;00m[37m[39;49;00m$
   112^I[37m      [39;49;00mresults.push(value)[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00miterator.call(context,[37m [39;49;00mvalue,[37m [39;49;00mindex,[37m [39;49;00mlist)[37m[39;49;00m$
   113^I[37m    [39;49;00mresults[37m[39;49;00m$
   114^I[37m[39;49;00m$
   115^I[37m[39;49;00m$
   116^I[37m  [39;49;00m[37m# Return all the elements for which a truth test fails.[39;49;00m[37m[39;49;00m$
   117^I[37m  [39;49;00m[31m_.reject[39;49;00m:[37m [39;49;00m[32m(obj, iterator, context) ->[39;49;00m[37m[39;49;00m$
   118^I[37m    [39;49;00m[31mresults[39;49;00m:[37m [39;49;00m[][37m[39;49;00m$
   119^I[37m    [39;49;00m_.each[37m [39;49;00mobj,[37m [39;49;00m[32m(value, index, list) ->[39;49;00m[37m[39;49;00m$
   120^I[37m      [39;49;00mresults.push(value)[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00mnot[37m [39;49;00miterator.call(context,[37m [39;49;00mvalue,[37m [39;49;00mindex,[37m [39;49;00mlist)[37m[39;49;00m$
   121^I[37m    [39;49;00mresults[37m[39;49;00m$
   122^I[37m[39;49;00m$
   123^I[37m[39;49;00m$
   124^I[37m  [39;49;00m[37m# Determine whether all of the elements match a truth test. Delegate to[39;49;00m[37m[39;49;00m$
   125^I[37m  [39;49;00m[37m# JavaScript 1.6's every(), if it is present.[39;49;00m[37m[39;49;00m$
   126^I[37m  [39;49;00m[31m_.all[39;49;00m:[37m [39;49;00m[32m(obj, iterator, context) ->[39;49;00m[37m[39;49;00m$
   127^I[37m    [39;49;00miterator[37m [39;49;00m||=[37m [39;49;00m_.identity[37m[39;49;00m$
   128^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mobj.every(iterator,[37m [39;49;00mcontext)[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00mobj[37m [39;49;00mand[37m [39;49;00m_.isFunction(obj.every)[37m[39;49;00m$
   129^I[37m    [39;49;00m[31mresult[39;49;00m:[37m [39;49;00m[34mtrue[39;49;00m[37m[39;49;00m$
   130^I[37m    [39;49;00m_.each[37m [39;49;00mobj,[37m [39;49;00m[32m(value, index, list) ->[39;49;00m[37m[39;49;00m$
   131^I[37m      [39;49;00m_.breakLoop()[37m [39;49;00m[34munless[39;49;00m[37m [39;49;00m([31mresult[39;49;00m:[37m [39;49;00mresult[37m [39;49;00mand[37m [39;49;00miterator.call(context,[37m [39;49;00mvalue,[37m [39;49;00mindex,[37m [39;49;00mlist))[37m[39;49;00m$
   132^I[37m    [39;49;00mresult[37m[39;49;00m$
   133^I[37m[39;49;00m$
   134^I[37m[39;49;00m$
   135^I[37m  [39;49;00m[37m# Determine if at least one element in the object matches a truth test. Use[39;49;00m[37m[39;49;00m$
   136^I[37m  [39;49;00m[37m# JavaScript 1.6's some(), if it exists.[39;49;00m[37m[39;49;00m$
   137^I[37m  [39;49;00m[31m_.any[39;49;00m:[37m [39;49;00m[32m(obj, iterator, context) ->[39;49;00m[37m[39;49;00m$
   138^I[37m    [39;49;00miterator[37m [39;49;00m||=[37m [39;49;00m_.identity[37m[39;49;00m$
   139^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mobj.some(iterator,[37m [39;49;00mcontext)[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00mobj[37m [39;49;00mand[37m [39;49;00m_.isFunction(obj.some)[37m[39;49;00m$
   140^I[37m    [39;49;00m[31mresult[39;49;00m:[37m [39;49;00m[34mfalse[39;49;00m[37m[39;49;00m$
   141^I[37m    [39;49;00m_.each[37m [39;49;00mobj,[37m [39;49;00m[32m(value, index, list) ->[39;49;00m[37m[39;49;00m$
   142^I[37m      [39;49;00m_.breakLoop()[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m([31mresult[39;49;00m:[37m [39;49;00miterator.call(context,[37m [39;49;00mvalue,[37m [39;49;00mindex,[37m [39;49;00mlist))[37m[39;49;00m$
   143^I[37m    [39;49;00mresult[37m[39;49;00m$
   144^I[37m[39;49;00m$
   145^I[37m[39;49;00m$
   146^I[37m  [39;49;00m[37m# Determine if a given value is included in the array or object,[39;49;00m[37m[39;49;00m$
   147^I[37m  [39;49;00m[37m# based on '==='.[39;49;00m[37m[39;49;00m$
   148^I[37m  [39;49;00m[31m_.include[39;49;00m:[37m [39;49;00m[32m(obj, target) ->[39;49;00m[37m[39;49;00m$
   149^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m_.indexOf(obj,[37m [39;49;00mtarget)[37m [39;49;00misnt[37m [39;49;00m-[34m1[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m_.isArray(obj)[37m[39;49;00m$
   150^I[37m    [39;49;00m[34mfor[39;49;00m[37m [39;49;00mkey,[37m [39;49;00mval[37m [39;49;00m[34mof[39;49;00m[37m [39;49;00mobj[37m[39;49;00m$
   151^I[37m      [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mtrue[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00mval[37m [39;49;00mis[37m [39;49;00mtarget[37m[39;49;00m$
   152^I[37m    [39;49;00m[34mfalse[39;49;00m[37m[39;49;00m$
   153^I[37m[39;49;00m$
   154^I[37m[39;49;00m$
   155^I[37m  [39;49;00m[37m# Invoke a method with arguments on every item in a collection.[39;49;00m[37m[39;49;00m$
   156^I[37m  [39;49;00m[31m_.invoke[39;49;00m:[37m [39;49;00m[32m(obj, method) ->[39;49;00m[37m[39;49;00m$
   157^I[37m    [39;49;00m[31margs[39;49;00m:[37m [39;49;00m_.rest(arguments,[37m [39;49;00m[34m2[39;49;00m)[37m[39;49;00m$
   158^I[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00mmethod[37m [39;49;00m[34mthen[39;49;00m[37m [39;49;00mval[method][37m [39;49;00m[34melse[39;49;00m[37m [39;49;00mval).apply(val,[37m [39;49;00margs)[37m [39;49;00m[34mfor[39;49;00m[37m [39;49;00mval[37m [39;49;00m[34min[39;49;00m[37m [39;49;00mobj[37m[39;49;00m$
   159^I[37m[39;49;00m$
   160^I[37m[39;49;00m$
   161^I[37m  [39;49;00m[37m# Convenience version of a common use case of map: fetching a property.[39;49;00m[37m[39;49;00m$
   162^I[37m  [39;49;00m[31m_.pluck[39;49;00m:[37m [39;49;00m[32m(obj, key) ->[39;49;00m[37m[39;49;00m$
   163^I[37m    [39;49;00m_.map(obj,[37m [39;49;00m([32m(val) ->[39;49;00m[37m [39;49;00mval[key]))[37m[39;49;00m$
   164^I[37m[39;49;00m$
   165^I[37m[39;49;00m$
   166^I[37m  [39;49;00m[37m# Return the maximum item or (item-based computation).[39;49;00m[37m[39;49;00m$
   167^I[37m  [39;49;00m[31m_.max[39;49;00m:[37m [39;49;00m[32m(obj, iterator, context) ->[39;49;00m[37m[39;49;00m$
   168^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[36mMath[39;49;00m.max.apply([36mMath[39;49;00m,[37m [39;49;00mobj)[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00mnot[37m [39;49;00miterator[37m [39;49;00mand[37m [39;49;00m_.isArray(obj)[37m[39;49;00m$
   169^I[37m    [39;49;00m[31mresult[39;49;00m:[37m [39;49;00m{[31mcomputed[39;49;00m:[37m [39;49;00m-[34mInfinity[39;49;00m}[37m[39;49;00m$
   170^I[37m    [39;49;00m_.each[37m [39;49;00mobj,[37m [39;49;00m[32m(value, index, list) ->[39;49;00m[37m[39;49;00m$
   171^I[37m      [39;49;00m[31mcomputed[39;49;00m:[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00miterator[37m [39;49;00m[34mthen[39;49;00m[37m [39;49;00miterator.call(context,[37m [39;49;00mvalue,[37m [39;49;00mindex,[37m [39;49;00mlist)[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00mvalue[37m[39;49;00m$
   172^I[37m      [39;49;00mcomputed[37m [39;49;00m>=[37m [39;49;00mresult.computed[37m [39;49;00mand[37m [39;49;00m([31mresult[39;49;00m:[37m [39;49;00m{[31mvalue[39;49;00m:[37m [39;49;00mvalue,[37m [39;49;00m[31mcomputed[39;49;00m:[37m [39;49;00mcomputed})[37m[39;49;00m$
   173^I[37m    [39;49;00mresult.value[37m[39;49;00m$
   174^I[37m[39;49;00m$
   175^I[37m[39;49;00m$
   176^I[37m  [39;49;00m[37m# Return the minimum element (or element-based computation).[39;49;00m[37m[39;49;00m$
   177^I[37m  [39;49;00m[31m_.min[39;49;00m:[37m [39;49;00m[32m(obj, iterator, context) ->[39;49;00m[37m[39;49;00m$
   178^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[36mMath[39;49;00m.min.apply([36mMath[39;49;00m,[37m [39;49;00mobj)[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00mnot[37m [39;49;00miterator[37m [39;49;00mand[37m [39;49;00m_.isArray(obj)[37m[39;49;00m$
   179^I[37m    [39;49;00m[31mresult[39;49;00m:[37m [39;49;00m{[31mcomputed[39;49;00m:[37m [39;49;00m[34mInfinity[39;49;00m}[37m[39;49;00m$
   180^I[37m    [39;49;00m_.each[37m [39;49;00mobj,[37m [39;49;00m[32m(value, index, list) ->[39;49;00m[37m[39;49;00m$
   181^I[37m      [39;49;00m[31mcomputed[39;49;00m:[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00miterator[37m [39;49;00m[34mthen[39;49;00m[37m [39;49;00miterator.call(context,[37m [39;49;00mvalue,[37m [39;49;00mindex,[37m [39;49;00mlist)[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00mvalue[37m[39;49;00m$
   182^I[37m      [39;49;00mcomputed[37m [39;49;00m<[37m [39;49;00mresult.computed[37m [39;49;00mand[37m [39;49;00m([31mresult[39;49;00m:[37m [39;49;00m{[31mvalue[39;49;00m:[37m [39;49;00mvalue,[37m [39;49;00m[31mcomputed[39;49;00m:[37m [39;49;00mcomputed})[37m[39;49;00m$
   183^I[37m    [39;49;00mresult.value[37m[39;49;00m$
   184^I[37m[39;49;00m$
   185^I[37m[39;49;00m$
   186^I[37m  [39;49;00m[37m# Sort the object's values by a criteria produced by an iterator.[39;49;00m[37m[39;49;00m$
   187^I[37m  [39;49;00m[31m_.sortBy[39;49;00m:[37m [39;49;00m[32m(obj, iterator, context) ->[39;49;00m[37m[39;49;00m$
   188^I[37m    [39;49;00m_.pluck(((_.map[37m [39;49;00mobj,[37m [39;49;00m[32m(value, index, list) ->[39;49;00m[37m[39;49;00m$
   189^I[37m      [39;49;00m{[31mvalue[39;49;00m:[37m [39;49;00mvalue,[37m [39;49;00m[31mcriteria[39;49;00m:[37m [39;49;00miterator.call(context,[37m [39;49;00mvalue,[37m [39;49;00mindex,[37m [39;49;00mlist)}[37m[39;49;00m$
   190^I[37m    [39;49;00m).sort([32m(left, right) ->[39;49;00m[37m[39;49;00m$
   191^I[37m      [39;49;00m[31ma[39;49;00m:[37m [39;49;00mleft.criteria;[37m [39;49;00m[31mb[39;49;00m:[37m [39;49;00mright.criteria[37m[39;49;00m$
   192^I[37m      [39;49;00m[34mif[39;49;00m[37m [39;49;00ma[37m [39;49;00m<[37m [39;49;00mb[37m [39;49;00m[34mthen[39;49;00m[37m [39;49;00m-[34m1[39;49;00m[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00ma[37m [39;49;00m>[37m [39;49;00mb[37m [39;49;00m[34mthen[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m[39;49;00m$
   193^I[37m    [39;49;00m)),[37m [39;49;00m[33m'[39;49;00m[33mvalue[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
   194^I[37m[39;49;00m$
   195^I[37m[39;49;00m$
   196^I[37m  [39;49;00m[37m# Use a comparator function to figure out at what index an object should[39;49;00m[37m[39;49;00m$
   197^I[37m  [39;49;00m[37m# be inserted so as to maintain order. Uses binary search.[39;49;00m[37m[39;49;00m$
   198^I[37m  [39;49;00m[31m_.sortedIndex[39;49;00m:[37m [39;49;00m[32m(array, obj, iterator) ->[39;49;00m[37m[39;49;00m$
   199^I[37m    [39;49;00miterator[37m [39;49;00m||=[37m [39;49;00m_.identity[37m[39;49;00m$
   200^I[37m    [39;49;00m[31mlow[39;49;00m:[37m [39;49;00m[34m0[39;49;00m;[37m [39;49;00m[31mhigh[39;49;00m:[37m [39;49;00marray.length[37m[39;49;00m$
   201^I[37m    [39;49;00m[34mwhile[39;49;00m[37m [39;49;00mlow[37m [39;49;00m<[37m [39;49;00mhigh[37m[39;49;00m$
   202^I[37m      [39;49;00m[31mmid[39;49;00m:[37m [39;49;00m(low[37m [39;49;00m+[37m [39;49;00mhigh)[37m [39;49;00m>>[37m [39;49;00m[34m1[39;49;00m[37m[39;49;00m$
   203^I[37m      [39;49;00m[34mif[39;49;00m[37m [39;49;00miterator(array[mid])[37m [39;49;00m<[37m [39;49;00miterator(obj)[37m [39;49;00m[34mthen[39;49;00m[37m [39;49;00m[31mlow[39;49;00m:[37m [39;49;00mmid[37m [39;49;00m+[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00m[31mhigh[39;49;00m:[37m [39;49;00mmid[37m[39;49;00m$
   204^I[37m    [39;49;00mlow[37m[39;49;00m$
   205^I[37m[39;49;00m$
   206^I[37m[39;49;00m$
   207^I[37m  [39;49;00m[37m# Convert anything iterable into a real, live array.[39;49;00m[37m[39;49;00m$
   208^I[37m  [39;49;00m[31m_.toArray[39;49;00m:[37m [39;49;00m[32m(iterable) ->[39;49;00m[37m[39;49;00m$
   209^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[][37m                   [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!iterable)[37m[39;49;00m$
   210^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00miterable.toArray()[37m   [39;49;00m[34mif[39;49;00m[37m [39;49;00m(iterable.toArray)[37m[39;49;00m$
   211^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00miterable[37m             [39;49;00m[34mif[39;49;00m[37m [39;49;00m(_.isArray(iterable))[37m[39;49;00m$
   212^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mslice.call(iterable)[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(_.isArguments(iterable))[37m[39;49;00m$
   213^I[37m    [39;49;00m_.values(iterable)[37m[39;49;00m$
   214^I[37m[39;49;00m$
   215^I[37m[39;49;00m$
   216^I[37m  [39;49;00m[37m# Return the number of elements in an object.[39;49;00m[37m[39;49;00m$
   217^I[37m  [39;49;00m[31m_.size[39;49;00m:[37m [39;49;00m[32m(obj) ->[39;49;00m[37m [39;49;00m_.toArray(obj).length[37m[39;49;00m$
   218^I[37m[39;49;00m$
   219^I[37m[39;49;00m$
   220^I[37m  [39;49;00m[37m# -------------------------- Array Functions: ------------------------------[39;49;00m[37m[39;49;00m$
   221^I[37m[39;49;00m$
   222^I[37m  [39;49;00m[37m# Get the first element of an array. Passing "n" will return the first N[39;49;00m[37m[39;49;00m$
   223^I[37m  [39;49;00m[37m# values in the array. Aliased as "head". The "guard" check allows it to work[39;49;00m[37m[39;49;00m$
   224^I[37m  [39;49;00m[37m# with _.map.[39;49;00m[37m[39;49;00m$
   225^I[37m  [39;49;00m[31m_.first[39;49;00m:[37m [39;49;00m[32m(array, n, guard) ->[39;49;00m[37m[39;49;00m$
   226^I[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00mn[37m [39;49;00mand[37m [39;49;00mnot[37m [39;49;00mguard[37m [39;49;00m[34mthen[39;49;00m[37m [39;49;00mslice.call(array,[37m [39;49;00m[34m0[39;49;00m,[37m [39;49;00mn)[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00marray[[34m0[39;49;00m][37m[39;49;00m$
   227^I[37m[39;49;00m$
   228^I[37m[39;49;00m$
   229^I[37m  [39;49;00m[37m# Returns everything but the first entry of the array. Aliased as "tail".[39;49;00m[37m[39;49;00m$
   230^I[37m  [39;49;00m[37m# Especially useful on the arguments object. Passing an "index" will return[39;49;00m[37m[39;49;00m$
   231^I[37m  [39;49;00m[37m# the rest of the values in the array from that index onward. The "guard"[39;49;00m[37m[39;49;00m$
   232^I[37m  [39;49;00m[37m# check allows it to work with _.map.[39;49;00m[37m[39;49;00m$
   233^I[37m  [39;49;00m[31m_.rest[39;49;00m:[37m [39;49;00m[32m(array, index, guard) ->[39;49;00m[37m[39;49;00m$
   234^I[37m    [39;49;00mslice.call(array,[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m_.isUndefined(index)[37m [39;49;00mor[37m [39;49;00mguard[37m [39;49;00m[34mthen[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00mindex)[37m[39;49;00m$
   235^I[37m[39;49;00m$
   236^I[37m[39;49;00m$
   237^I[37m  [39;49;00m[37m# Get the last element of an array.[39;49;00m[37m[39;49;00m$
   238^I[37m  [39;49;00m[31m_.last[39;49;00m:[37m [39;49;00m[32m(array) ->[39;49;00m[37m [39;49;00marray[array.length[37m [39;49;00m-[37m [39;49;00m[34m1[39;49;00m][37m[39;49;00m$
   239^I[37m[39;49;00m$
   240^I[37m[39;49;00m$
   241^I[37m  [39;49;00m[37m# Trim out all falsy values from an array.[39;49;00m[37m[39;49;00m$
   242^I[37m  [39;49;00m[31m_.compact[39;49;00m:[37m [39;49;00m[32m(array) ->[39;49;00m[37m [39;49;00marray[i][37m [39;49;00m[34mfor[39;49;00m[37m [39;49;00mi[37m [39;49;00m[34min[39;49;00m[37m [39;49;00m[[34m0[39;49;00m...array.length][37m [39;49;00m[34mwhen[39;49;00m[37m [39;49;00marray[i][37m[39;49;00m$
   243^I[37m[39;49;00m$
   244^I[37m[39;49;00m$
   245^I[37m  [39;49;00m[37m# Return a completely flattened version of an array.[39;49;00m[37m[39;49;00m$
   246^I[37m  [39;49;00m[31m_.flatten[39;49;00m:[37m [39;49;00m[32m(array) ->[39;49;00m[37m[39;49;00m$
   247^I[37m    [39;49;00m_.reduce[37m [39;49;00marray,[37m [39;49;00m[],[37m [39;49;00m[32m(memo, value) ->[39;49;00m[37m[39;49;00m$
   248^I[37m      [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mmemo.concat(_.flatten(value))[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m_.isArray(value)[37m[39;49;00m$
   249^I[37m      [39;49;00mmemo.push(value)[37m[39;49;00m$
   250^I[37m      [39;49;00mmemo[37m[39;49;00m$
   251^I[37m[39;49;00m$
   252^I[37m[39;49;00m$
   253^I[37m  [39;49;00m[37m# Return a version of the array that does not contain the specified value(s).[39;49;00m[37m[39;49;00m$
   254^I[37m  [39;49;00m[31m_.without[39;49;00m:[37m [39;49;00m[32m(array) ->[39;49;00m[37m[39;49;00m$
   255^I[37m    [39;49;00m[31mvalues[39;49;00m:[37m [39;49;00m_.rest(arguments)[37m[39;49;00m$
   256^I[37m    [39;49;00mval[37m [39;49;00m[34mfor[39;49;00m[37m [39;49;00mval[37m [39;49;00m[34min[39;49;00m[37m [39;49;00m_.toArray(array)[37m [39;49;00m[34mwhen[39;49;00m[37m [39;49;00mnot[37m [39;49;00m_.include(values,[37m [39;49;00mval)[37m[39;49;00m$
   257^I[37m[39;49;00m$
   258^I[37m[39;49;00m$
   259^I[37m  [39;49;00m[37m# Produce a duplicate-free version of the array. If the array has already[39;49;00m[37m[39;49;00m$
   260^I[37m  [39;49;00m[37m# been sorted, you have the option of using a faster algorithm.[39;49;00m[37m[39;49;00m$
   261^I[37m  [39;49;00m[31m_.uniq[39;49;00m:[37m [39;49;00m[32m(array, isSorted) ->[39;49;00m[37m[39;49;00m$
   262^I[37m    [39;49;00m[31mmemo[39;49;00m:[37m [39;49;00m[][37m[39;49;00m$
   263^I[37m    [39;49;00m[34mfor[39;49;00m[37m [39;49;00mel,[37m [39;49;00mi[37m [39;49;00m[34min[39;49;00m[37m [39;49;00m_.toArray(array)[37m[39;49;00m$
   264^I[37m      [39;49;00mmemo.push(el)[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00mi[37m [39;49;00mis[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m||[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00misSorted[37m [39;49;00mis[37m [39;49;00m[34mtrue[39;49;00m[37m [39;49;00m[34mthen[39;49;00m[37m [39;49;00m_.last(memo)[37m [39;49;00misnt[37m [39;49;00mel[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00mnot[37m [39;49;00m_.include(memo,[37m [39;49;00mel))[37m[39;49;00m$
   265^I[37m    [39;49;00mmemo[37m[39;49;00m$
   266^I[37m[39;49;00m$
   267^I[37m[39;49;00m$
   268^I[37m  [39;49;00m[37m# Produce an array that contains every item shared between all the[39;49;00m[37m[39;49;00m$
   269^I[37m  [39;49;00m[37m# passed-in arrays.[39;49;00m[37m[39;49;00m$
   270^I[37m  [39;49;00m[31m_.intersect[39;49;00m:[37m [39;49;00m[32m(array) ->[39;49;00m[37m[39;49;00m$
   271^I[37m    [39;49;00m[31mrest[39;49;00m:[37m [39;49;00m_.rest(arguments)[37m[39;49;00m$
   272^I[37m    [39;49;00m_.select[37m [39;49;00m_.uniq(array),[37m [39;49;00m[32m(item) ->[39;49;00m[37m[39;49;00m$
   273^I[37m      [39;49;00m_.all[37m [39;49;00mrest,[37m [39;49;00m[32m(other) ->[39;49;00m[37m[39;49;00m$
   274^I[37m        [39;49;00m_.indexOf(other,[37m [39;49;00mitem)[37m [39;49;00m>=[37m [39;49;00m[34m0[39;49;00m[37m[39;49;00m$
   275^I[37m[39;49;00m$
   276^I[37m[39;49;00m$
   277^I[37m  [39;49;00m[37m# Zip together multiple lists into a single array -- elements that share[39;49;00m[37m[39;49;00m$
   278^I[37m  [39;49;00m[37m# an index go together.[39;49;00m[37m[39;49;00m$
   279^I[37m  [39;49;00m[31m_.zip[39;49;00m:[37m [39;49;00m[32m->[39;49;00m[37m[39;49;00m$
   280^I[37m    [39;49;00m[31mlength[39;49;00m:[37m     [39;49;00m_.max(_.pluck(arguments,[37m [39;49;00m[33m'[39;49;00m[33mlength[39;49;00m[33m'[39;49;00m))[37m[39;49;00m$
   281^I[37m    [39;49;00m[31mresults[39;49;00m:[37m    [39;49;00m[34mnew[39;49;00m[37m [39;49;00m[36mArray[39;49;00m(length)[37m[39;49;00m$
   282^I[37m    [39;49;00m[34mfor[39;49;00m[37m [39;49;00mi[37m [39;49;00m[34min[39;49;00m[37m [39;49;00m[[34m0[39;49;00m...length][37m[39;49;00m$
   283^I[37m      [39;49;00mresults[i]:[37m [39;49;00m_.pluck(arguments,[37m [39;49;00m[36mString[39;49;00m(i))[37m[39;49;00m$
   284^I[37m    [39;49;00mresults[37m[39;49;00m$
   285^I[37m[39;49;00m$
   286^I[37m[39;49;00m$
   287^I[37m  [39;49;00m[37m# If the browser doesn't supply us with indexOf (I'm looking at you, MSIE),[39;49;00m[37m[39;49;00m$
   288^I[37m  [39;49;00m[37m# we need this function. Return the position of the first occurence of an[39;49;00m[37m[39;49;00m$
   289^I[37m  [39;49;00m[37m# item in an array, or -1 if the item is not included in the array.[39;49;00m[37m[39;49;00m$
   290^I[37m  [39;49;00m[31m_.indexOf[39;49;00m:[37m [39;49;00m[32m(array, item) ->[39;49;00m[37m[39;49;00m$
   291^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00marray.indexOf(item)[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00marray.indexOf[37m[39;49;00m$
   292^I[37m    [39;49;00m[31mi[39;49;00m:[37m [39;49;00m[34m0[39;49;00m;[37m [39;49;00m[31ml[39;49;00m:[37m [39;49;00marray.length[37m[39;49;00m$
   293^I[37m    [39;49;00m[34mwhile[39;49;00m[37m [39;49;00ml[37m [39;49;00m-[37m [39;49;00mi[37m[39;49;00m$
   294^I[37m      [39;49;00m[34mif[39;49;00m[37m [39;49;00marray[i][37m [39;49;00mis[37m [39;49;00mitem[37m [39;49;00m[34mthen[39;49;00m[37m [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mi[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00mi++[37m[39;49;00m$
   295^I[37m    [39;49;00m-[34m1[39;49;00m[37m[39;49;00m$
   296^I[37m[39;49;00m$
   297^I[37m[39;49;00m$
   298^I[37m  [39;49;00m[37m# Provide JavaScript 1.6's lastIndexOf, delegating to the native function,[39;49;00m[37m[39;49;00m$
   299^I[37m  [39;49;00m[37m# if possible.[39;49;00m[37m[39;49;00m$
   300^I[37m  [39;49;00m[31m_.lastIndexOf[39;49;00m:[37m [39;49;00m[32m(array, item) ->[39;49;00m[37m[39;49;00m$
   301^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00marray.lastIndexOf(item)[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00marray.lastIndexOf[37m[39;49;00m$
   302^I[37m    [39;49;00m[31mi[39;49;00m:[37m [39;49;00marray.length[37m[39;49;00m$
   303^I[37m    [39;49;00m[34mwhile[39;49;00m[37m [39;49;00mi[37m[39;49;00m$
   304^I[37m      [39;49;00m[34mif[39;49;00m[37m [39;49;00marray[i][37m [39;49;00mis[37m [39;49;00mitem[37m [39;49;00m[34mthen[39;49;00m[37m [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mi[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00mi--[37m[39;49;00m$
   305^I[37m    [39;49;00m-[34m1[39;49;00m[37m[39;49;00m$
   306^I[37m[39;49;00m$
   307^I[37m[39;49;00m$
   308^I[37m  [39;49;00m[37m# Generate an integer Array containing an arithmetic progression. A port of[39;49;00m[37m[39;49;00m$
   309^I[37m  [39;49;00m[37m# the native Python range() function. See:[39;49;00m[37m[39;49;00m$
   310^I[37m  [39;49;00m[37m# http://docs.python.org/library/functions.html#range[39;49;00m[37m[39;49;00m$
   311^I[37m  [39;49;00m[31m_.range[39;49;00m:[37m [39;49;00m[32m(start, stop, step) ->[39;49;00m[37m[39;49;00m$
   312^I[37m    [39;49;00m[31ma[39;49;00m:[37m        [39;49;00marguments[37m[39;49;00m$
   313^I[37m    [39;49;00m[31msolo[39;49;00m:[37m     [39;49;00ma.length[37m [39;49;00m<=[37m [39;49;00m[34m1[39;49;00m[37m[39;49;00m$
   314^I[37m    [39;49;00m[31mi[39;49;00m:[37m [39;49;00m[31mstart[39;49;00m:[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00msolo[37m [39;49;00m[34mthen[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00ma[[34m0[39;49;00m];[37m[39;49;00m$
   315^I[37m    [39;49;00m[31mstop[39;49;00m:[37m     [39;49;00m[34mif[39;49;00m[37m [39;49;00msolo[37m [39;49;00m[34mthen[39;49;00m[37m [39;49;00ma[[34m0[39;49;00m][37m [39;49;00m[34melse[39;49;00m[37m [39;49;00ma[[34m1[39;49;00m];[37m[39;49;00m$
   316^I[37m    [39;49;00m[31mstep[39;49;00m:[37m     [39;49;00ma[[34m2[39;49;00m][37m [39;49;00mor[37m [39;49;00m[34m1[39;49;00m[37m[39;49;00m$
   317^I[37m    [39;49;00m[31mlen[39;49;00m:[37m      [39;49;00m[36mMath[39;49;00m.ceil((stop[37m [39;49;00m-[37m [39;49;00mstart)[37m [39;49;00m/[37m [39;49;00mstep)[37m[39;49;00m$
   318^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[][37m [39;49;00m[34mif[39;49;00m[37m [39;49;00mlen[37m [39;49;00m<=[37m [39;49;00m[34m0[39;49;00m[37m[39;49;00m$
   319^I[37m    [39;49;00m[31mrange[39;49;00m:[37m    [39;49;00m[34mnew[39;49;00m[37m [39;49;00m[36mArray[39;49;00m(len)[37m[39;49;00m$
   320^I[37m    [39;49;00m[31midx[39;49;00m:[37m      [39;49;00m[34m0[39;49;00m[37m[39;49;00m$
   321^I[37m    [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m[34mtrue[39;49;00m[37m[39;49;00m$
   322^I[37m      [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mrange[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00mstep[37m [39;49;00m>[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[34mthen[39;49;00m[37m [39;49;00mi[37m [39;49;00m-[37m [39;49;00mstop[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00mstop[37m [39;49;00m-[37m [39;49;00mi)[37m [39;49;00m>=[37m [39;49;00m[34m0[39;49;00m[37m[39;49;00m$
   323^I[37m      [39;49;00mrange[idx]:[37m [39;49;00mi[37m[39;49;00m$
   324^I[37m      [39;49;00midx++[37m[39;49;00m$
   325^I[37m      [39;49;00mi+=[37m [39;49;00mstep[37m[39;49;00m$
   326^I[37m[39;49;00m$
   327^I[37m[39;49;00m$
   328^I[37m  [39;49;00m[37m# ----------------------- Function Functions: -----------------------------[39;49;00m[37m[39;49;00m$
   329^I[37m[39;49;00m$
   330^I[37m  [39;49;00m[37m# Create a function bound to a given object (assigning 'this', and arguments,[39;49;00m[37m[39;49;00m$
   331^I[37m  [39;49;00m[37m# optionally). Binding with arguments is also known as 'curry'.[39;49;00m[37m[39;49;00m$
   332^I[37m  [39;49;00m[31m_.bind[39;49;00m:[37m [39;49;00m[32m(func, obj) ->[39;49;00m[37m[39;49;00m$
   333^I[37m    [39;49;00m[31margs[39;49;00m:[37m [39;49;00m_.rest[32m(arguments, 2)[39;49;00m$
   334^I[32m    ->[39;49;00m[37m [39;49;00mfunc.apply(obj[37m [39;49;00mor[37m [39;49;00mroot,[37m [39;49;00margs.concat(arguments))[37m[39;49;00m$
   335^I[37m[39;49;00m$
   336^I[37m[39;49;00m$
   337^I[37m  [39;49;00m[37m# Bind all of an object's methods to that object. Useful for ensuring that[39;49;00m[37m[39;49;00m$
   338^I[37m  [39;49;00m[37m# all callbacks defined on an object belong to it.[39;49;00m[37m[39;49;00m$
   339^I[37m  [39;49;00m[31m_.bindAll[39;49;00m:[37m [39;49;00m[32m(obj) ->[39;49;00m[37m[39;49;00m$
   340^I[37m    [39;49;00m[31mfuncs[39;49;00m:[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00marguments.length[37m [39;49;00m>[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[34mthen[39;49;00m[37m [39;49;00m_.rest(arguments)[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00m_.functions(obj)[37m[39;49;00m$
   341^I[37m    [39;49;00m_.each(funcs,[37m [39;49;00m[32m(f) ->[39;49;00m[37m [39;49;00mobj[f]:[37m [39;49;00m_.bind(obj[f],[37m [39;49;00mobj))[37m[39;49;00m$
   342^I[37m    [39;49;00mobj[37m[39;49;00m$
   343^I[37m[39;49;00m$
   344^I[37m[39;49;00m$
   345^I[37m  [39;49;00m[37m# Delays a function for the given number of milliseconds, and then calls[39;49;00m[37m[39;49;00m$
   346^I[37m  [39;49;00m[37m# it with the arguments supplied.[39;49;00m[37m[39;49;00m$
   347^I[37m  [39;49;00m[31m_.delay[39;49;00m:[37m [39;49;00m[32m(func, wait) ->[39;49;00m[37m[39;49;00m$
   348^I[37m    [39;49;00m[31margs[39;49;00m:[37m [39;49;00m_.rest(arguments,[37m [39;49;00m[34m2[39;49;00m)[37m[39;49;00m$
   349^I[37m    [39;49;00msetTimeout(([32m->[39;49;00m[37m [39;49;00mfunc.apply(func,[37m [39;49;00margs)),[37m [39;49;00mwait)[37m[39;49;00m$
   350^I[37m[39;49;00m$
   351^I[37m[39;49;00m$
   352^I[37m  [39;49;00m[37m# Defers a function, scheduling it to run after the current call stack has[39;49;00m[37m[39;49;00m$
   353^I[37m  [39;49;00m[37m# cleared.[39;49;00m[37m[39;49;00m$
   354^I[37m  [39;49;00m[31m_.defer[39;49;00m:[37m [39;49;00m[32m(func) ->[39;49;00m[37m[39;49;00m$
   355^I[37m    [39;49;00m_.delay.apply(_,[37m [39;49;00m[func,[37m [39;49;00m[34m1[39;49;00m].concat(_.rest(arguments)))[37m[39;49;00m$
   356^I[37m[39;49;00m$
   357^I[37m[39;49;00m$
   358^I[37m  [39;49;00m[37m# Returns the first function passed as an argument to the second,[39;49;00m[37m[39;49;00m$
   359^I[37m  [39;49;00m[37m# allowing you to adjust arguments, run code before and after, and[39;49;00m[37m[39;49;00m$
   360^I[37m  [39;49;00m[37m# conditionally execute the original function.[39;49;00m[37m[39;49;00m$
   361^I[37m  [39;49;00m[31m_.wrap[39;49;00m:[37m [39;49;00m[32m(func, wrapper) ->[39;49;00m[37m[39;49;00m$
   362^I[37m    [39;49;00m[32m->[39;49;00m[37m [39;49;00mwrapper.apply(wrapper,[37m [39;49;00m[func].concat(arguments))[37m[39;49;00m$
   363^I[37m[39;49;00m$
   364^I[37m[39;49;00m$
   365^I[37m  [39;49;00m[37m# Returns a function that is the composition of a list of functions, each[39;49;00m[37m[39;49;00m$
   366^I[37m  [39;49;00m[37m# consuming the return value of the function that follows.[39;49;00m[37m[39;49;00m$
   367^I[37m  [39;49;00m[31m_.compose[39;49;00m:[37m [39;49;00m[32m->[39;49;00m[37m[39;49;00m$
   368^I[37m    [39;49;00m[31mfuncs[39;49;00m:[37m [39;49;00marguments[37m[39;49;00m$
   369^I[37m    [39;49;00m[32m->[39;49;00m[37m[39;49;00m$
   370^I[37m      [39;49;00m[31margs[39;49;00m:[37m [39;49;00marguments[37m[39;49;00m$
   371^I[37m      [39;49;00m[34mfor[39;49;00m[37m [39;49;00mi[37m [39;49;00m[34min[39;49;00m[37m [39;49;00m[(funcs.length[37m [39;49;00m-[37m [39;49;00m[34m1[39;49;00m)..[34m0[39;49;00m][37m[39;49;00m$
   372^I[37m        [39;49;00m[31margs[39;49;00m:[37m [39;49;00m[funcs[i].apply([34mthis[39;49;00m,[37m [39;49;00margs)][37m[39;49;00m$
   373^I[37m      [39;49;00margs[[34m0[39;49;00m][37m[39;49;00m$
   374^I[37m[39;49;00m$
   375^I[37m[39;49;00m$
   376^I[37m  [39;49;00m[37m# ------------------------- Object Functions: ----------------------------[39;49;00m[37m[39;49;00m$
   377^I[37m[39;49;00m$
   378^I[37m  [39;49;00m[37m# Retrieve the names of an object's properties.[39;49;00m[37m[39;49;00m$
   379^I[37m  [39;49;00m[31m_.keys[39;49;00m:[37m [39;49;00m[32m(obj) ->[39;49;00m[37m[39;49;00m$
   380^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m_.range([34m0[39;49;00m,[37m [39;49;00mobj.length)[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m_.isArray(obj)[37m[39;49;00m$
   381^I[37m    [39;49;00mkey[37m [39;49;00m[34mfor[39;49;00m[37m [39;49;00mkey,[37m [39;49;00mval[37m [39;49;00m[34mof[39;49;00m[37m [39;49;00mobj[37m[39;49;00m$
   382^I[37m[39;49;00m$
   383^I[37m[39;49;00m$
   384^I[37m  [39;49;00m[37m# Retrieve the values of an object's properties.[39;49;00m[37m[39;49;00m$
   385^I[37m  [39;49;00m[31m_.values[39;49;00m:[37m [39;49;00m[32m(obj) ->[39;49;00m[37m[39;49;00m$
   386^I[37m    [39;49;00m_.map(obj,[37m [39;49;00m_.identity)[37m[39;49;00m$
   387^I[37m[39;49;00m$
   388^I[37m[39;49;00m$
   389^I[37m  [39;49;00m[37m# Return a sorted list of the function names available in Underscore.[39;49;00m[37m[39;49;00m$
   390^I[37m  [39;49;00m[31m_.functions[39;49;00m:[37m [39;49;00m[32m(obj) ->[39;49;00m[37m[39;49;00m$
   391^I[37m    [39;49;00m_.select(_.keys(obj),[37m [39;49;00m[32m(key) ->[39;49;00m[37m [39;49;00m_.isFunction(obj[key])).sort()[37m[39;49;00m$
   392^I[37m[39;49;00m$
   393^I[37m[39;49;00m$
   394^I[37m  [39;49;00m[37m# Extend a given object with all of the properties in a source object.[39;49;00m[37m[39;49;00m$
   395^I[37m  [39;49;00m[31m_.extend[39;49;00m:[37m [39;49;00m[32m(destination, source) ->[39;49;00m[37m[39;49;00m$
   396^I[37m    [39;49;00m[34mfor[39;49;00m[37m [39;49;00mkey,[37m [39;49;00mval[37m [39;49;00m[34mof[39;49;00m[37m [39;49;00msource[37m[39;49;00m$
   397^I[37m      [39;49;00mdestination[key]:[37m [39;49;00mval[37m[39;49;00m$
   398^I[37m    [39;49;00mdestination[37m[39;49;00m$
   399^I[37m[39;49;00m$
   400^I[37m[39;49;00m$
   401^I[37m  [39;49;00m[37m# Create a (shallow-cloned) duplicate of an object.[39;49;00m[37m[39;49;00m$
   402^I[37m  [39;49;00m[31m_.clone[39;49;00m:[37m [39;49;00m[32m(obj) ->[39;49;00m[37m[39;49;00m$
   403^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mobj.slice([34m0[39;49;00m)[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m_.isArray(obj)[37m[39;49;00m$
   404^I[37m    [39;49;00m_.extend({},[37m [39;49;00mobj)[37m[39;49;00m$
   405^I[37m[39;49;00m$
   406^I[37m[39;49;00m$
   407^I[37m  [39;49;00m[37m# Invokes interceptor with the obj, and then returns obj.[39;49;00m[37m[39;49;00m$
   408^I[37m  [39;49;00m[37m# The primary purpose of this method is to "tap into" a method chain, in order to perform operations on intermediate results within the chain.[39;49;00m[37m[39;49;00m$
   409^I[37m  [39;49;00m[31m_.tap[39;49;00m:[37m [39;49;00m[32m(obj, interceptor) ->[39;49;00m[37m[39;49;00m$
   410^I[37m    [39;49;00minterceptor(obj)[37m[39;49;00m$
   411^I[37m    [39;49;00mobj[37m[39;49;00m$
   412^I[37m[39;49;00m$
   413^I[37m[39;49;00m$
   414^I[37m  [39;49;00m[37m# Perform a deep comparison to check if two objects are equal.[39;49;00m[37m[39;49;00m$
   415^I[37m  [39;49;00m[31m_.isEqual[39;49;00m:[37m [39;49;00m[32m(a, b) ->[39;49;00m[37m[39;49;00m$
   416^I[37m    [39;49;00m[37m# Check object identity.[39;49;00m[37m[39;49;00m$
   417^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mtrue[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00ma[37m [39;49;00mis[37m [39;49;00mb[37m[39;49;00m$
   418^I[37m    [39;49;00m[37m# Different types?[39;49;00m[37m[39;49;00m$
   419^I[37m    [39;49;00m[31matype[39;49;00m:[37m [39;49;00m[34mtypeof[39;49;00m(a);[37m [39;49;00m[31mbtype[39;49;00m:[37m [39;49;00m[34mtypeof[39;49;00m(b)[37m[39;49;00m$
   420^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mfalse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00matype[37m [39;49;00misnt[37m [39;49;00mbtype[37m[39;49;00m$
   421^I[37m    [39;49;00m[37m# Basic equality test (watch out for coercions).[39;49;00m[37m[39;49;00m$
   422^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mtrue[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m`a[37m [39;49;00m==[37m [39;49;00mb`[37m[39;49;00m$
   423^I[37m    [39;49;00m[37m# One is falsy and the other truthy.[39;49;00m[37m[39;49;00m$
   424^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mfalse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!a[37m [39;49;00mand[37m [39;49;00mb)[37m [39;49;00mor[37m [39;49;00m(a[37m [39;49;00mand[37m [39;49;00m!b)[37m[39;49;00m$
   425^I[37m    [39;49;00m[37m# One of them implements an isEqual()?[39;49;00m[37m[39;49;00m$
   426^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00ma.isEqual(b)[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00ma.isEqual[37m[39;49;00m$
   427^I[37m    [39;49;00m[37m# Check dates' integer values.[39;49;00m[37m[39;49;00m$
   428^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00ma.getTime()[37m [39;49;00mis[37m [39;49;00mb.getTime()[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m_.isDate(a)[37m [39;49;00mand[37m [39;49;00m_.isDate(b)[37m[39;49;00m$
   429^I[37m    [39;49;00m[37m# Both are NaN?[39;49;00m[37m[39;49;00m$
   430^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mtrue[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m_.[36misNaN[39;49;00m(a)[37m [39;49;00mand[37m [39;49;00m_.[36misNaN[39;49;00m(b)[37m[39;49;00m$
   431^I[37m    [39;49;00m[37m# Compare regular expressions.[39;49;00m[37m[39;49;00m$
   432^I[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m_.isRegExp(a)[37m [39;49;00mand[37m [39;49;00m_.isRegExp(b)[37m[39;49;00m$
   433^I[37m      [39;49;00m[34mreturn[39;49;00m[37m [39;49;00ma.source[37m     [39;49;00mis[37m [39;49;00mb.source[37m [39;49;00mand[37m[39;49;00m$
   434^I[37m             [39;49;00ma.global[37m     [39;49;00mis[37m [39;49;00mb.global[37m [39;49;00mand[37m[39;49;00m$
   435^I[37m             [39;49;00ma.ignoreCase[37m [39;49;00mis[37m [39;49;00mb.ignoreCase[37m [39;49;00mand[37m[39;49;00m$
   436^I[37m             [39;49;00ma.multiline[37m  [39;49;00mis[37m [39;49;00mb.multiline[37m[39;49;00m$
   437^I[37m    [39;49;00m[37m# If a is not an object by this point, we can't handle it.[39;49;00m[37m[39;49;00m$
   438^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mfalse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00matype[37m [39;49;00misnt[37m [39;49;00m[33m'[39;49;00m[33mobject[39;49;00m[33m'[39;49;00m[37m[39;49;00m$
   439^I[37m    [39;49;00m[37m# Check for different array lengths before comparing contents.[39;49;00m[37m[39;49;00m$
   440^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mfalse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00ma.length[37m [39;49;00mand[37m [39;49;00m(a.length[37m [39;49;00misnt[37m [39;49;00mb.length)[37m[39;49;00m$
   441^I[37m    [39;49;00m[37m# Nothing else worked, deep compare the contents.[39;49;00m[37m[39;49;00m$
   442^I[37m    [39;49;00m[31maKeys[39;49;00m:[37m [39;49;00m_.keys(a);[37m [39;49;00m[31mbKeys[39;49;00m:[37m [39;49;00m_.keys(b)[37m[39;49;00m$
   443^I[37m    [39;49;00m[37m# Different object sizes?[39;49;00m[37m[39;49;00m$
   444^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mfalse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00maKeys.length[37m [39;49;00misnt[37m [39;49;00mbKeys.length[37m[39;49;00m$
   445^I[37m    [39;49;00m[37m# Recursive comparison of contents.[39;49;00m[37m[39;49;00m$
   446^I[37m    [39;49;00m[37m# for (var key in a) if (!_.isEqual(a[key], b[key])) return false;[39;49;00m[37m[39;49;00m$
   447^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mtrue[39;49;00m[37m[39;49;00m$
   448^I[37m[39;49;00m$
   449^I[37m[39;49;00m$
   450^I[37m  [39;49;00m[37m# Is a given array or object empty?[39;49;00m[37m[39;49;00m$
   451^I[37m  [39;49;00m[31m_.isEmpty[39;49;00m:[37m      [39;49;00m[32m(obj) ->[39;49;00m[37m [39;49;00m_.keys(obj).length[37m [39;49;00mis[37m [39;49;00m[34m0[39;49;00m[37m[39;49;00m$
   452^I[37m[39;49;00m$
   453^I[37m[39;49;00m$
   454^I[37m  [39;49;00m[37m# Is a given value a DOM element?[39;49;00m[37m[39;49;00m$
   455^I[37m  [39;49;00m[31m_.isElement[39;49;00m:[37m    [39;49;00m[32m(obj) ->[39;49;00m[37m [39;49;00mobj[37m [39;49;00mand[37m [39;49;00mobj.nodeType[37m [39;49;00mis[37m [39;49;00m[34m1[39;49;00m[37m[39;49;00m$
   456^I[37m[39;49;00m$
   457^I[37m[39;49;00m$
   458^I[37m  [39;49;00m[37m# Is a given value an array?[39;49;00m[37m[39;49;00m$
   459^I[37m  [39;49;00m[31m_.isArray[39;49;00m:[37m      [39;49;00m[32m(obj) ->[39;49;00m[37m [39;49;00m!!(obj[37m [39;49;00mand[37m [39;49;00mobj.concat[37m [39;49;00mand[37m [39;49;00mobj.unshift)[37m[39;49;00m$
   460^I[37m[39;49;00m$
   461^I[37m[39;49;00m$
   462^I[37m  [39;49;00m[37m# Is a given variable an arguments object?[39;49;00m[37m[39;49;00m$
   463^I[37m  [39;49;00m[31m_.isArguments[39;49;00m:[37m  [39;49;00m[32m(obj) ->[39;49;00m[37m [39;49;00mobj[37m [39;49;00mand[37m [39;49;00m_.isNumber(obj.length)[37m [39;49;00mand[37m [39;49;00mnot[37m [39;49;00mobj.concat[37m [39;49;00mand[37m[39;49;00m$
   464^I[37m                           [39;49;00mnot[37m [39;49;00mobj.substr[37m [39;49;00mand[37m [39;49;00mnot[37m [39;49;00mobj.apply[37m [39;49;00mand[37m [39;49;00mnot[37m [39;49;00mpropertyIsEnumerable.call(obj,[37m [39;49;00m[33m'[39;49;00m[33mlength[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
   465^I[37m[39;49;00m$
   466^I[37m[39;49;00m$
   467^I[37m  [39;49;00m[37m# Is the given value a function?[39;49;00m[37m[39;49;00m$
   468^I[37m  [39;49;00m[31m_.isFunction[39;49;00m:[37m   [39;49;00m[32m(obj) ->[39;49;00m[37m [39;49;00m!!(obj[37m [39;49;00mand[37m [39;49;00mobj.constructor[37m [39;49;00mand[37m [39;49;00mobj.call[37m [39;49;00mand[37m [39;49;00mobj.apply)[37m[39;49;00m$
   469^I[37m[39;49;00m$
   470^I[37m[39;49;00m$
   471^I[37m  [39;49;00m[37m# Is the given value a string?[39;49;00m[37m[39;49;00m$
   472^I[37m  [39;49;00m[31m_.isString[39;49;00m:[37m     [39;49;00m[32m(obj) ->[39;49;00m[37m [39;49;00m!!(obj[37m [39;49;00mis[37m [39;49;00m[33m'[39;49;00m[33m'[39;49;00m[37m [39;49;00mor[37m [39;49;00m(obj[37m [39;49;00mand[37m [39;49;00mobj.charCodeAt[37m [39;49;00mand[37m [39;49;00mobj.substr))[37m[39;49;00m$
   473^I[37m[39;49;00m$
   474^I[37m[39;49;00m$
   475^I[37m  [39;49;00m[37m# Is a given value a number?[39;49;00m[37m[39;49;00m$
   476^I[37m  [39;49;00m[31m_.isNumber[39;49;00m:[37m     [39;49;00m[32m(obj) ->[39;49;00m[37m [39;49;00m(obj[37m [39;49;00mis[37m [39;49;00m+obj)[37m [39;49;00mor[37m [39;49;00mtoString.call(obj)[37m [39;49;00mis[37m [39;49;00m[33m'[39;49;00m[33m[object Number][39;49;00m[33m'[39;49;00m[37m[39;49;00m$
   477^I[37m[39;49;00m$
   478^I[37m[39;49;00m$
   479^I[37m  [39;49;00m[37m# Is a given value a Date?[39;49;00m[37m[39;49;00m$
   480^I[37m  [39;49;00m[31m_.isDate[39;49;00m:[37m       [39;49;00m[32m(obj) ->[39;49;00m[37m [39;49;00m!!(obj[37m [39;49;00mand[37m [39;49;00mobj.getTimezoneOffset[37m [39;49;00mand[37m [39;49;00mobj.setUTCFullYear)[37m[39;49;00m$
   481^I[37m[39;49;00m$
   482^I[37m[39;49;00m$
   483^I[37m  [39;49;00m[37m# Is the given value a regular expression?[39;49;00m[37m[39;49;00m$
   484^I[37m  [39;49;00m[31m_.isRegExp[39;49;00m:[37m     [39;49;00m[32m(obj) ->[39;49;00m[37m [39;49;00m!!(obj[37m [39;49;00mand[37m [39;49;00mobj.exec[37m [39;49;00mand[37m [39;49;00m(obj.ignoreCase[37m [39;49;00mor[37m [39;49;00mobj.ignoreCase[37m [39;49;00mis[37m [39;49;00m[34mfalse[39;49;00m))[37m[39;49;00m$
   485^I[37m[39;49;00m$
   486^I[37m[39;49;00m$
   487^I[37m  [39;49;00m[37m# Is the given value NaN -- this one is interesting. NaN != NaN, and[39;49;00m[37m[39;49;00m$
   488^I[37m  [39;49;00m[37m# isNaN(undefined) == true, so we make sure it's a number first.[39;49;00m[37m[39;49;00m$
   489^I[37m  [39;49;00m[31m_.isNaN[39;49;00m:[37m        [39;49;00m[32m(obj) ->[39;49;00m[37m [39;49;00m_.isNumber(obj)[37m [39;49;00mand[37m [39;49;00m[36mwindow[39;49;00m.[36misNaN[39;49;00m(obj)[37m[39;49;00m$
   490^I[37m[39;49;00m$
   491^I[37m[39;49;00m$
   492^I[37m  [39;49;00m[37m# Is a given value equal to null?[39;49;00m[37m[39;49;00m$
   493^I[37m  [39;49;00m[31m_.isNull[39;49;00m:[37m       [39;49;00m[32m(obj) ->[39;49;00m[37m [39;49;00mobj[37m [39;49;00mis[37m [39;49;00m[34mnull[39;49;00m[37m[39;49;00m$
   494^I[37m[39;49;00m$
   495^I[37m[39;49;00m$
   496^I[37m  [39;49;00m[37m# Is a given variable undefined?[39;49;00m[37m[39;49;00m$
   497^I[37m  [39;49;00m[31m_.isUndefined[39;49;00m:[37m  [39;49;00m[32m(obj) ->[39;49;00m[37m [39;49;00m[34mtypeof[39;49;00m[37m [39;49;00mobj[37m [39;49;00mis[37m [39;49;00m[33m'[39;49;00m[33mundefined[39;49;00m[33m'[39;49;00m[37m[39;49;00m$
   498^I[37m[39;49;00m$
   499^I[37m[39;49;00m$
   500^I[37m  [39;49;00m[37m# -------------------------- Utility Functions: --------------------------[39;49;00m[37m[39;49;00m$
   501^I[37m[39;49;00m$
   502^I[37m  [39;49;00m[37m# Run Underscore.js in noConflict mode, returning the '_' variable to its[39;49;00m[37m[39;49;00m$
   503^I[37m  [39;49;00m[37m# previous owner. Returns a reference to the Underscore object.[39;49;00m[37m[39;49;00m$
   504^I[37m  [39;49;00m[31m_.noConflict[39;49;00m:[37m [39;49;00m[32m->[39;49;00m[37m[39;49;00m$
   505^I[37m    [39;49;00m[31mroot._[39;49;00m:[37m [39;49;00mpreviousUnderscore[37m[39;49;00m$
   506^I[37m    [39;49;00m[34mthis[39;49;00m[37m[39;49;00m$
   507^I[37m[39;49;00m$
   508^I[37m[39;49;00m$
   509^I[37m  [39;49;00m[37m# Keep the identity function around for default iterators.[39;49;00m[37m[39;49;00m$
   510^I[37m  [39;49;00m[31m_.identity[39;49;00m:[37m [39;49;00m[32m(value) ->[39;49;00m[37m [39;49;00mvalue[37m[39;49;00m$
   511^I[37m[39;49;00m$
   512^I[37m[39;49;00m$
   513^I[37m  [39;49;00m[37m# Break out of the middle of an iteration.[39;49;00m[37m[39;49;00m$
   514^I[37m  [39;49;00m[31m_.breakLoop[39;49;00m:[37m [39;49;00m[32m->[39;49;00m[37m [39;49;00m[34mthrow[39;49;00m[37m [39;49;00mbreaker[37m[39;49;00m$
   515^I[37m[39;49;00m$
   516^I[37m[39;49;00m$
   517^I[37m  [39;49;00m[37m# Generate a unique integer id (unique within the entire client session).[39;49;00m[37m[39;49;00m$
   518^I[37m  [39;49;00m[37m# Useful for temporary DOM ids.[39;49;00m[37m[39;49;00m$
   519^I[37m  [39;49;00m[31midCounter[39;49;00m:[37m [39;49;00m[34m0[39;49;00m[37m[39;49;00m$
   520^I[37m  [39;49;00m[31m_.uniqueId[39;49;00m:[37m [39;49;00m[32m(prefix) ->[39;49;00m[37m[39;49;00m$
   521^I[37m    [39;49;00m(prefix[37m [39;49;00mor[37m [39;49;00m[33m'[39;49;00m[33m'[39;49;00m)[37m [39;49;00m+[37m [39;49;00midCounter++[37m[39;49;00m$
   522^I[37m[39;49;00m$
   523^I[37m[39;49;00m$
   524^I[37m  [39;49;00m[37m# By default, Underscore uses ERB-style template delimiters, change the[39;49;00m[37m[39;49;00m$
   525^I[37m  [39;49;00m[37m# following template settings to use alternative delimiters.[39;49;00m[37m[39;49;00m$
   526^I[37m  [39;49;00m[31m_.templateSettings[39;49;00m:[37m [39;49;00m{[37m[39;49;00m$
   527^I[37m    [39;49;00m[31mstart[39;49;00m:[37m        [39;49;00m[33m'[39;49;00m[33m<%[39;49;00m[33m'[39;49;00m[37m[39;49;00m$
   528^I[37m    [39;49;00m[31mend[39;49;00m:[37m          [39;49;00m[33m'[39;49;00m[33m%>[39;49;00m[33m'[39;49;00m[37m[39;49;00m$
   529^I[37m    [39;49;00m[31minterpolate[39;49;00m:[37m  [39;49;00m[33m/<%=(.+?)%>/g[39;49;00m[37m[39;49;00m$
   530^I[37m  [39;49;00m}[37m[39;49;00m$
   531^I[37m[39;49;00m$
   532^I[37m[39;49;00m$
   533^I[37m  [39;49;00m[37m# JavaScript templating a-la ERB, pilfered from John Resig's[39;49;00m[37m[39;49;00m$
   534^I[37m  [39;49;00m[37m# "Secrets of the JavaScript Ninja", page 83.[39;49;00m[37m[39;49;00m$
   535^I[37m  [39;49;00m[37m# Single-quotea fix from Rick Strahl's version.[39;49;00m[37m[39;49;00m$
   536^I[37m  [39;49;00m[31m_.template[39;49;00m:[37m [39;49;00m[32m(str, data) ->[39;49;00m[37m[39;49;00m$
   537^I[37m    [39;49;00m[31mc[39;49;00m:[37m [39;49;00m_.templateSettings[37m[39;49;00m$
   538^I[37m    [39;49;00m[31mfn[39;49;00m:[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00m[36mFunction[39;49;00m[37m [39;49;00m[33m'[39;49;00m[33mobj[39;49;00m[33m'[39;49;00m,[37m[39;49;00m$
   539^I[37m      [39;49;00m[33m'[39;49;00m[33mvar p=[],print=function(){p.push.apply(p,arguments);};[39;49;00m[33m'[39;49;00m[37m [39;49;00m+[37m[39;49;00m$
   540^I[37m      [39;49;00m[33m'[39;49;00m[33mwith(obj){p.push([39;49;00m[33m\'[39;49;00m[33m'[39;49;00m[37m [39;49;00m+[37m[39;49;00m$
   541^I[37m      [39;49;00mstr.replace([33m/[\r\t\n]/g[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
   542^I[37m         [39;49;00m.replace([34mnew[39;49;00m[37m [39;49;00m[36mRegExp[39;49;00m([33m"[39;49;00m[33m'[39;49;00m[33m(?=[^[39;49;00m[33m"[39;49;00m+c.end[[34m0[39;49;00m]+[33m"[39;49;00m[33m]*[39;49;00m[33m"[39;49;00m+c.end+[33m"[39;49;00m[33m)[39;49;00m[33m"[39;49;00m,[33m"[39;49;00m[33mg[39;49;00m[33m"[39;49;00m),[33m"[39;49;00m[33m\t[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
   543^I[37m         [39;49;00m.split([33m"[39;49;00m[33m'[39;49;00m[33m"[39;49;00m).join([33m"[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
   544^I[37m         [39;49;00m.split([33m"[39;49;00m[33m\t[39;49;00m[33m"[39;49;00m).join([33m"[39;49;00m[33m'[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
   545^I[37m         [39;49;00m.replace(c.interpolate,[37m [39;49;00m[33m"[39;49;00m[33m'[39;49;00m[33m,$1,[39;49;00m[33m'[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
   546^I[37m         [39;49;00m.split(c.start).join([33m"[39;49;00m[33m'[39;49;00m[33m);[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
   547^I[37m         [39;49;00m.split(c.end).join([33m"[39;49;00m[33mp.push([39;49;00m[33m'[39;49;00m[33m"[39;49;00m)[37m [39;49;00m+[37m[39;49;00m$
   548^I[37m         [39;49;00m[33m"[39;49;00m[33m'[39;49;00m[33m);}return p.join([39;49;00m[33m'[39;49;00m[33m'[39;49;00m[33m);[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   549^I[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00mdata[37m [39;49;00m[34mthen[39;49;00m[37m [39;49;00mfn(data)[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00mfn[37m[39;49;00m$
   550^I[37m[39;49;00m$
   551^I[37m[39;49;00m$
   552^I[37m  [39;49;00m[37m# ------------------------------- Aliases ----------------------------------[39;49;00m[37m[39;49;00m$
   553^I[37m[39;49;00m$
   554^I[37m  [39;49;00m[31m_.forEach[39;49;00m:[37m [39;49;00m_.each[37m[39;49;00m$
   555^I[37m  [39;49;00m[31m_.foldl[39;49;00m:[37m   [39;49;00m[31m_.inject[39;49;00m:[37m      [39;49;00m_.reduce[37m[39;49;00m$
   556^I[37m  [39;49;00m[31m_.foldr[39;49;00m:[37m   [39;49;00m_.reduceRight[37m[39;49;00m$
   557^I[37m  [39;49;00m[31m_.filter[39;49;00m:[37m  [39;49;00m_.select[37m[39;49;00m$
   558^I[37m  [39;49;00m[31m_.every[39;49;00m:[37m   [39;49;00m_.all[37m[39;49;00m$
   559^I[37m  [39;49;00m[31m_.some[39;49;00m:[37m    [39;49;00m_.any[37m[39;49;00m$
   560^I[37m  [39;49;00m[31m_.head[39;49;00m:[37m    [39;49;00m_.first[37m[39;49;00m$
   561^I[37m  [39;49;00m[31m_.tail[39;49;00m:[37m    [39;49;00m_.rest[37m[39;49;00m$
   562^I[37m  [39;49;00m[31m_.methods[39;49;00m:[37m [39;49;00m_.functions[37m[39;49;00m$
   563^I[37m[39;49;00m$
   564^I[37m[39;49;00m$
   565^I[37m  [39;49;00m[37m#   /*------------------------ Setup the OOP Wrapper: --------------------------*/[39;49;00m[37m[39;49;00m$
   566^I[37m[39;49;00m$
   567^I[37m  [39;49;00m[37m# Helper function to continue chaining intermediate results.[39;49;00m[37m[39;49;00m$
   568^I[37m  [39;49;00m[31mresult[39;49;00m:[37m [39;49;00m[32m(obj, chain) ->[39;49;00m[37m[39;49;00m$
   569^I[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00mchain[37m [39;49;00m[34mthen[39;49;00m[37m [39;49;00m_(obj).chain()[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00mobj[37m[39;49;00m$
   570^I[37m[39;49;00m$
   571^I[37m[39;49;00m$
   572^I[37m  [39;49;00m[37m# Add all of the Underscore functions to the wrapper object.[39;49;00m[37m[39;49;00m$
   573^I[37m  [39;49;00m_.each[37m [39;49;00m_.functions(_),[37m [39;49;00m[32m(name) ->[39;49;00m[37m[39;49;00m$
   574^I[37m    [39;49;00m[31mmethod[39;49;00m:[37m [39;49;00m_[name][37m[39;49;00m$
   575^I[37m    [39;49;00mwrapper.prototype[name]:[37m [39;49;00m[32m->[39;49;00m[37m[39;49;00m$
   576^I[37m      [39;49;00munshift.call(arguments,[37m [39;49;00m[34mthis[39;49;00m._wrapped)[37m[39;49;00m$
   577^I[37m      [39;49;00mresult(method.apply(_,[37m [39;49;00marguments),[37m [39;49;00m[34mthis[39;49;00m._chain)[37m[39;49;00m$
   578^I[37m[39;49;00m$
   579^I[37m[39;49;00m$
   580^I[37m  [39;49;00m[37m# Add all mutator Array functions to the wrapper.[39;49;00m[37m[39;49;00m$
   581^I[37m  [39;49;00m_.each[37m [39;49;00m[[33m'[39;49;00m[33mpop[39;49;00m[33m'[39;49;00m,[37m [39;49;00m[33m'[39;49;00m[33mpush[39;49;00m[33m'[39;49;00m,[37m [39;49;00m[33m'[39;49;00m[33mreverse[39;49;00m[33m'[39;49;00m,[37m [39;49;00m[33m'[39;49;00m[33mshift[39;49;00m[33m'[39;49;00m,[37m [39;49;00m[33m'[39;49;00m[33msort[39;49;00m[33m'[39;49;00m,[37m [39;49;00m[33m'[39;49;00m[33msplice[39;49;00m[33m'[39;49;00m,[37m [39;49;00m[33m'[39;49;00m[33munshift[39;49;00m[33m'[39;49;00m],[37m [39;49;00m[32m(name) ->[39;49;00m[37m[39;49;00m$
   582^I[37m    [39;49;00m[31mmethod[39;49;00m:[37m [39;49;00m[36mArray[39;49;00m.prototype[name][37m[39;49;00m$
   583^I[37m    [39;49;00mwrapper.prototype[name]:[37m [39;49;00m[32m->[39;49;00m[37m[39;49;00m$
   584^I[37m      [39;49;00mmethod.apply([34mthis[39;49;00m._wrapped,[37m [39;49;00marguments)[37m[39;49;00m$
   585^I[37m      [39;49;00mresult([34mthis[39;49;00m._wrapped,[37m [39;49;00m[34mthis[39;49;00m._chain)[37m[39;49;00m$
   586^I[37m[39;49;00m$
   587^I[37m[39;49;00m$
   588^I[37m  [39;49;00m[37m# Add all accessor Array functions to the wrapper.[39;49;00m[37m[39;49;00m$
   589^I[37m  [39;49;00m_.each[37m [39;49;00m[[33m'[39;49;00m[33mconcat[39;49;00m[33m'[39;49;00m,[37m [39;49;00m[33m'[39;49;00m[33mjoin[39;49;00m[33m'[39;49;00m,[37m [39;49;00m[33m'[39;49;00m[33mslice[39;49;00m[33m'[39;49;00m],[37m [39;49;00m[32m(name) ->[39;49;00m[37m[39;49;00m$
   590^I[37m    [39;49;00m[31mmethod[39;49;00m:[37m [39;49;00m[36mArray[39;49;00m.prototype[name][37m[39;49;00m$
   591^I[37m    [39;49;00mwrapper.prototype[name]:[37m [39;49;00m[32m->[39;49;00m[37m[39;49;00m$
   592^I[37m      [39;49;00mresult(method.apply([34mthis[39;49;00m._wrapped,[37m [39;49;00marguments),[37m [39;49;00m[34mthis[39;49;00m._chain)[37m[39;49;00m$
   593^I[37m[39;49;00m$
   594^I[37m[39;49;00m$
   595^I[37m  [39;49;00m[37m# Start chaining a wrapped Underscore object.[39;49;00m[37m[39;49;00m$
   596^I[37m  [39;49;00m[31mwrapper::chain[39;49;00m:[37m [39;49;00m[32m->[39;49;00m[37m[39;49;00m$
   597^I[37m    [39;49;00m[34mthis[39;49;00m.[31m_chain[39;49;00m:[37m [39;49;00m[34mtrue[39;49;00m[37m[39;49;00m$
   598^I[37m    [39;49;00m[34mthis[39;49;00m[37m[39;49;00m$
   599^I[37m[39;49;00m$
   600^I[37m[39;49;00m$
   601^I[37m  [39;49;00m[37m# Extracts the result from a wrapped and chained object.[39;49;00m[37m[39;49;00m$
   602^I[37m  [39;49;00m[31mwrapper::value[39;49;00m:[37m [39;49;00m[32m->[39;49;00m[37m [39;49;00m[34mthis[39;49;00m._wrapped$

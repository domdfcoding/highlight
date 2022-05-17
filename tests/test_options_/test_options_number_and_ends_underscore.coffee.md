     1	[37m  [39;49;00m[37m# Underscore.coffee[39;49;00m[37m[39;49;00m$
     2	[37m  [39;49;00m[37m# (c) 2010 Jeremy Ashkenas, DocumentCloud Inc.[39;49;00m[37m[39;49;00m$
     3	[37m  [39;49;00m[37m# Underscore is freely distributable under the terms of the MIT license.[39;49;00m[37m[39;49;00m$
     4	[37m  [39;49;00m[37m# Portions of Underscore are inspired by or borrowed from Prototype.js,[39;49;00m[37m[39;49;00m$
     5	[37m  [39;49;00m[37m# Oliver Steele's Functional, and John Resig's Micro-Templating.[39;49;00m[37m[39;49;00m$
     6	[37m  [39;49;00m[37m# For all details and documentation:[39;49;00m[37m[39;49;00m$
     7	[37m  [39;49;00m[37m# http://documentcloud.github.com/underscore/[39;49;00m[37m[39;49;00m$
     8	[37m[39;49;00m$
     9	[37m[39;49;00m$
    10	[37m  [39;49;00m[37m# ------------------------- Baseline setup ---------------------------------[39;49;00m[37m[39;49;00m$
    11	[37m[39;49;00m$
    12	[37m  [39;49;00m[37m# Establish the root object, "window" in the browser, or "global" on the server.[39;49;00m[37m[39;49;00m$
    13	[37m  [39;49;00m[31mroot[39;49;00m:[37m [39;49;00m[34mthis[39;49;00m[37m[39;49;00m$
    14	[37m[39;49;00m$
    15	[37m[39;49;00m$
    16	[37m  [39;49;00m[37m# Save the previous value of the "_" variable.[39;49;00m[37m[39;49;00m$
    17	[37m  [39;49;00m[31mpreviousUnderscore[39;49;00m:[37m [39;49;00mroot._[37m[39;49;00m$
    18	[37m[39;49;00m$
    19	[37m[39;49;00m$
    20	[37m  [39;49;00m[37m# If Underscore is called as a function, it returns a wrapped object that[39;49;00m[37m[39;49;00m$
    21	[37m  [39;49;00m[37m# can be used OO-style. This wrapper holds altered versions of all the[39;49;00m[37m[39;49;00m$
    22	[37m  [39;49;00m[37m# underscore functions. Wrapped objects may be chained.[39;49;00m[37m[39;49;00m$
    23	[37m  [39;49;00m[31mwrapper[39;49;00m:[37m [39;49;00m[32m(obj) ->[39;49;00m[37m[39;49;00m$
    24	[37m    [39;49;00m[34mthis[39;49;00m.[31m_wrapped[39;49;00m:[37m [39;49;00mobj[37m[39;49;00m$
    25	[37m    [39;49;00m[34mthis[39;49;00m[37m[39;49;00m$
    26	[37m[39;49;00m$
    27	[37m[39;49;00m$
    28	[37m  [39;49;00m[37m# Establish the object that gets thrown to break out of a loop iteration.[39;49;00m[37m[39;49;00m$
    29	[37m  [39;49;00m[31mbreaker[39;49;00m:[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m[34mtypeof[39;49;00m(StopIteration)[37m [39;49;00mis[37m [39;49;00m[33m'[39;49;00m[33mundefined[39;49;00m[33m'[39;49;00m[37m [39;49;00m[34mthen[39;49;00m[37m [39;49;00m[33m'[39;49;00m[33m__break__[39;49;00m[33m'[39;49;00m[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00mStopIteration[37m[39;49;00m$
    30	[37m[39;49;00m$
    31	[37m[39;49;00m$
    32	[37m  [39;49;00m[37m# Create a safe reference to the Underscore object forreference below.[39;49;00m[37m[39;49;00m$
    33	[37m  [39;49;00m[31m_[39;49;00m:[37m [39;49;00m[31mroot._[39;49;00m:[37m [39;49;00m[32m(obj) ->[39;49;00m[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mwrapper(obj)[37m[39;49;00m$
    34	[37m[39;49;00m$
    35	[37m[39;49;00m$
    36	[37m  [39;49;00m[37m# Export the Underscore object for CommonJS.[39;49;00m[37m[39;49;00m$
    37	[37m  [39;49;00m[34mif[39;49;00m[37m [39;49;00m[34mtypeof[39;49;00m(exports)[37m [39;49;00m!=[37m [39;49;00m[33m'[39;49;00m[33mundefined[39;49;00m[33m'[39;49;00m[37m [39;49;00m[34mthen[39;49;00m[37m [39;49;00m[31mexports._[39;49;00m:[37m [39;49;00m_[37m[39;49;00m$
    38	[37m[39;49;00m$
    39	[37m[39;49;00m$
    40	[37m  [39;49;00m[37m# Create quick reference variables for speed access to core prototypes.[39;49;00m[37m[39;49;00m$
    41	[37m  [39;49;00m[31mslice[39;49;00m:[37m                [39;49;00m[36mArray[39;49;00m::slice[37m[39;49;00m$
    42	[37m  [39;49;00m[31munshift[39;49;00m:[37m              [39;49;00m[36mArray[39;49;00m::unshift[37m[39;49;00m$
    43	[37m  [39;49;00m[31mtoString[39;49;00m:[37m             [39;49;00m[36mObject[39;49;00m::toString[37m[39;49;00m$
    44	[37m  [39;49;00m[31mhasOwnProperty[39;49;00m:[37m       [39;49;00m[36mObject[39;49;00m::hasOwnProperty[37m[39;49;00m$
    45	[37m  [39;49;00m[31mpropertyIsEnumerable[39;49;00m:[37m [39;49;00m[36mObject[39;49;00m::propertyIsEnumerable[37m[39;49;00m$
    46	[37m[39;49;00m$
    47	[37m[39;49;00m$
    48	[37m  [39;49;00m[37m# Current version.[39;49;00m[37m[39;49;00m$
    49	[37m  [39;49;00m[31m_.VERSION[39;49;00m:[37m [39;49;00m[33m'[39;49;00m[33m0.5.7[39;49;00m[33m'[39;49;00m[37m[39;49;00m$
    50	[37m[39;49;00m$
    51	[37m[39;49;00m$
    52	[37m  [39;49;00m[37m# ------------------------ Collection Functions: ---------------------------[39;49;00m[37m[39;49;00m$
    53	[37m[39;49;00m$
    54	[37m  [39;49;00m[37m# The cornerstone, an each implementation.[39;49;00m[37m[39;49;00m$
    55	[37m  [39;49;00m[37m# Handles objects implementing forEach, arrays, and raw objects.[39;49;00m[37m[39;49;00m$
    56	[37m  [39;49;00m[31m_.each[39;49;00m:[37m [39;49;00m[32m(obj, iterator, context) ->[39;49;00m[37m[39;49;00m$
    57	[37m    [39;49;00m[31mindex[39;49;00m:[37m [39;49;00m[34m0[39;49;00m[37m[39;49;00m$
    58	[37m    [39;49;00m[34mtry[39;49;00m[37m[39;49;00m$
    59	[37m      [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mobj.forEach(iterator,[37m [39;49;00mcontext)[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00mobj.forEach[37m[39;49;00m$
    60	[37m      [39;49;00m[34mif[39;49;00m[37m [39;49;00m_.isArray(obj)[37m [39;49;00mor[37m [39;49;00m_.isArguments(obj)[37m[39;49;00m$
    61	[37m        [39;49;00m[34mreturn[39;49;00m[37m [39;49;00miterator.call(context,[37m [39;49;00mobj[i],[37m [39;49;00mi,[37m [39;49;00mobj)[37m [39;49;00m[34mfor[39;49;00m[37m [39;49;00mi[37m [39;49;00m[34min[39;49;00m[37m [39;49;00m[[34m0[39;49;00m...obj.length][37m[39;49;00m$
    62	[37m      [39;49;00miterator.call(context,[37m [39;49;00mval,[37m [39;49;00mkey,[37m [39;49;00mobj)[37m [39;49;00m[34mfor[39;49;00m[37m [39;49;00mkey,[37m [39;49;00mval[37m [39;49;00m[34mof[39;49;00m[37m [39;49;00mobj[37m[39;49;00m$
    63	[37m    [39;49;00m[34mcatch[39;49;00m[37m [39;49;00me[37m[39;49;00m$
    64	[37m      [39;49;00m[34mthrow[39;49;00m[37m [39;49;00me[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00me[37m [39;49;00misnt[37m [39;49;00mbreaker[37m[39;49;00m$
    65	[37m    [39;49;00mobj[37m[39;49;00m$
    66	[37m[39;49;00m$
    67	[37m[39;49;00m$
    68	[37m  [39;49;00m[37m# Return the results of applying the iterator to each element. Use JavaScript[39;49;00m[37m[39;49;00m$
    69	[37m  [39;49;00m[37m# 1.6's version of map, if possible.[39;49;00m[37m[39;49;00m$
    70	[37m  [39;49;00m[31m_.map[39;49;00m:[37m [39;49;00m[32m(obj, iterator, context) ->[39;49;00m[37m[39;49;00m$
    71	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mobj.map(iterator,[37m [39;49;00mcontext)[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(obj[37m [39;49;00mand[37m [39;49;00m_.isFunction(obj.map))[37m[39;49;00m$
    72	[37m    [39;49;00m[31mresults[39;49;00m:[37m [39;49;00m[][37m[39;49;00m$
    73	[37m    [39;49;00m_.each[37m [39;49;00mobj,[37m [39;49;00m[32m(value, index, list) ->[39;49;00m[37m[39;49;00m$
    74	[37m      [39;49;00mresults.push(iterator.call(context,[37m [39;49;00mvalue,[37m [39;49;00mindex,[37m [39;49;00mlist))[37m[39;49;00m$
    75	[37m    [39;49;00mresults[37m[39;49;00m$
    76	[37m[39;49;00m$
    77	[37m[39;49;00m$
    78	[37m  [39;49;00m[37m# Reduce builds up a single result from a list of values. Also known as[39;49;00m[37m[39;49;00m$
    79	[37m  [39;49;00m[37m# inject, or foldl. Uses JavaScript 1.8's version of reduce, if possible.[39;49;00m[37m[39;49;00m$
    80	[37m  [39;49;00m[31m_.reduce[39;49;00m:[37m [39;49;00m[32m(obj, memo, iterator, context) ->[39;49;00m[37m[39;49;00m$
    81	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mobj.reduce(_.bind(iterator,[37m [39;49;00mcontext),[37m [39;49;00mmemo)[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(obj[37m [39;49;00mand[37m [39;49;00m_.isFunction(obj.reduce))[37m[39;49;00m$
    82	[37m    [39;49;00m_.each[37m [39;49;00mobj,[37m [39;49;00m[32m(value, index, list) ->[39;49;00m[37m[39;49;00m$
    83	[37m      [39;49;00m[31mmemo[39;49;00m:[37m [39;49;00miterator.call(context,[37m [39;49;00mmemo,[37m [39;49;00mvalue,[37m [39;49;00mindex,[37m [39;49;00mlist)[37m[39;49;00m$
    84	[37m    [39;49;00mmemo[37m[39;49;00m$
    85	[37m[39;49;00m$
    86	[37m[39;49;00m$
    87	[37m  [39;49;00m[37m# The right-associative version of reduce, also known as foldr. Uses[39;49;00m[37m[39;49;00m$
    88	[37m  [39;49;00m[37m# JavaScript 1.8's version of reduceRight, if available.[39;49;00m[37m[39;49;00m$
    89	[37m  [39;49;00m[31m_.reduceRight[39;49;00m:[37m [39;49;00m[32m(obj, memo, iterator, context) ->[39;49;00m[37m[39;49;00m$
    90	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mobj.reduceRight(_.bind(iterator,[37m [39;49;00mcontext),[37m [39;49;00mmemo)[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(obj[37m [39;49;00mand[37m [39;49;00m_.isFunction(obj.reduceRight))[37m[39;49;00m$
    91	[37m    [39;49;00m_.each[37m [39;49;00m_.clone(_.toArray(obj)).reverse(),[37m [39;49;00m[32m(value, index) ->[39;49;00m[37m[39;49;00m$
    92	[37m      [39;49;00m[31mmemo[39;49;00m:[37m [39;49;00miterator.call(context,[37m [39;49;00mmemo,[37m [39;49;00mvalue,[37m [39;49;00mindex,[37m [39;49;00mobj)[37m[39;49;00m$
    93	[37m    [39;49;00mmemo[37m[39;49;00m$
    94	[37m[39;49;00m$
    95	[37m[39;49;00m$
    96	[37m  [39;49;00m[37m# Return the first value which passes a truth test.[39;49;00m[37m[39;49;00m$
    97	[37m  [39;49;00m[31m_.detect[39;49;00m:[37m [39;49;00m[32m(obj, iterator, context) ->[39;49;00m[37m[39;49;00m$
    98	[37m    [39;49;00m[31mresult[39;49;00m:[37m [39;49;00m[34mnull[39;49;00m[37m[39;49;00m$
    99	[37m    [39;49;00m_.each[37m [39;49;00mobj,[37m [39;49;00m[32m(value, index, list) ->[39;49;00m[37m[39;49;00m$
   100	[37m      [39;49;00m[34mif[39;49;00m[37m [39;49;00miterator.call(context,[37m [39;49;00mvalue,[37m [39;49;00mindex,[37m [39;49;00mlist)[37m[39;49;00m$
   101	[37m        [39;49;00m[31mresult[39;49;00m:[37m [39;49;00mvalue[37m[39;49;00m$
   102	[37m        [39;49;00m_.breakLoop()[37m[39;49;00m$
   103	[37m    [39;49;00mresult[37m[39;49;00m$
   104	[37m[39;49;00m$
   105	[37m[39;49;00m$
   106	[37m  [39;49;00m[37m# Return all the elements that pass a truth test. Use JavaScript 1.6's[39;49;00m[37m[39;49;00m$
   107	[37m  [39;49;00m[37m# filter(), if it exists.[39;49;00m[37m[39;49;00m$
   108	[37m  [39;49;00m[31m_.select[39;49;00m:[37m [39;49;00m[32m(obj, iterator, context) ->[39;49;00m[37m[39;49;00m$
   109	[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00mobj[37m [39;49;00mand[37m [39;49;00m_.isFunction(obj.filter)[37m [39;49;00m[34mthen[39;49;00m[37m [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mobj.filter(iterator,[37m [39;49;00mcontext)[37m[39;49;00m$
   110	[37m    [39;49;00m[31mresults[39;49;00m:[37m [39;49;00m[][37m[39;49;00m$
   111	[37m    [39;49;00m_.each[37m [39;49;00mobj,[37m [39;49;00m[32m(value, index, list) ->[39;49;00m[37m[39;49;00m$
   112	[37m      [39;49;00mresults.push(value)[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00miterator.call(context,[37m [39;49;00mvalue,[37m [39;49;00mindex,[37m [39;49;00mlist)[37m[39;49;00m$
   113	[37m    [39;49;00mresults[37m[39;49;00m$
   114	[37m[39;49;00m$
   115	[37m[39;49;00m$
   116	[37m  [39;49;00m[37m# Return all the elements for which a truth test fails.[39;49;00m[37m[39;49;00m$
   117	[37m  [39;49;00m[31m_.reject[39;49;00m:[37m [39;49;00m[32m(obj, iterator, context) ->[39;49;00m[37m[39;49;00m$
   118	[37m    [39;49;00m[31mresults[39;49;00m:[37m [39;49;00m[][37m[39;49;00m$
   119	[37m    [39;49;00m_.each[37m [39;49;00mobj,[37m [39;49;00m[32m(value, index, list) ->[39;49;00m[37m[39;49;00m$
   120	[37m      [39;49;00mresults.push(value)[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00mnot[37m [39;49;00miterator.call(context,[37m [39;49;00mvalue,[37m [39;49;00mindex,[37m [39;49;00mlist)[37m[39;49;00m$
   121	[37m    [39;49;00mresults[37m[39;49;00m$
   122	[37m[39;49;00m$
   123	[37m[39;49;00m$
   124	[37m  [39;49;00m[37m# Determine whether all of the elements match a truth test. Delegate to[39;49;00m[37m[39;49;00m$
   125	[37m  [39;49;00m[37m# JavaScript 1.6's every(), if it is present.[39;49;00m[37m[39;49;00m$
   126	[37m  [39;49;00m[31m_.all[39;49;00m:[37m [39;49;00m[32m(obj, iterator, context) ->[39;49;00m[37m[39;49;00m$
   127	[37m    [39;49;00miterator[37m [39;49;00m||=[37m [39;49;00m_.identity[37m[39;49;00m$
   128	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mobj.every(iterator,[37m [39;49;00mcontext)[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00mobj[37m [39;49;00mand[37m [39;49;00m_.isFunction(obj.every)[37m[39;49;00m$
   129	[37m    [39;49;00m[31mresult[39;49;00m:[37m [39;49;00m[34mtrue[39;49;00m[37m[39;49;00m$
   130	[37m    [39;49;00m_.each[37m [39;49;00mobj,[37m [39;49;00m[32m(value, index, list) ->[39;49;00m[37m[39;49;00m$
   131	[37m      [39;49;00m_.breakLoop()[37m [39;49;00m[34munless[39;49;00m[37m [39;49;00m([31mresult[39;49;00m:[37m [39;49;00mresult[37m [39;49;00mand[37m [39;49;00miterator.call(context,[37m [39;49;00mvalue,[37m [39;49;00mindex,[37m [39;49;00mlist))[37m[39;49;00m$
   132	[37m    [39;49;00mresult[37m[39;49;00m$
   133	[37m[39;49;00m$
   134	[37m[39;49;00m$
   135	[37m  [39;49;00m[37m# Determine if at least one element in the object matches a truth test. Use[39;49;00m[37m[39;49;00m$
   136	[37m  [39;49;00m[37m# JavaScript 1.6's some(), if it exists.[39;49;00m[37m[39;49;00m$
   137	[37m  [39;49;00m[31m_.any[39;49;00m:[37m [39;49;00m[32m(obj, iterator, context) ->[39;49;00m[37m[39;49;00m$
   138	[37m    [39;49;00miterator[37m [39;49;00m||=[37m [39;49;00m_.identity[37m[39;49;00m$
   139	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mobj.some(iterator,[37m [39;49;00mcontext)[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00mobj[37m [39;49;00mand[37m [39;49;00m_.isFunction(obj.some)[37m[39;49;00m$
   140	[37m    [39;49;00m[31mresult[39;49;00m:[37m [39;49;00m[34mfalse[39;49;00m[37m[39;49;00m$
   141	[37m    [39;49;00m_.each[37m [39;49;00mobj,[37m [39;49;00m[32m(value, index, list) ->[39;49;00m[37m[39;49;00m$
   142	[37m      [39;49;00m_.breakLoop()[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m([31mresult[39;49;00m:[37m [39;49;00miterator.call(context,[37m [39;49;00mvalue,[37m [39;49;00mindex,[37m [39;49;00mlist))[37m[39;49;00m$
   143	[37m    [39;49;00mresult[37m[39;49;00m$
   144	[37m[39;49;00m$
   145	[37m[39;49;00m$
   146	[37m  [39;49;00m[37m# Determine if a given value is included in the array or object,[39;49;00m[37m[39;49;00m$
   147	[37m  [39;49;00m[37m# based on '==='.[39;49;00m[37m[39;49;00m$
   148	[37m  [39;49;00m[31m_.include[39;49;00m:[37m [39;49;00m[32m(obj, target) ->[39;49;00m[37m[39;49;00m$
   149	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m_.indexOf(obj,[37m [39;49;00mtarget)[37m [39;49;00misnt[37m [39;49;00m-[34m1[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m_.isArray(obj)[37m[39;49;00m$
   150	[37m    [39;49;00m[34mfor[39;49;00m[37m [39;49;00mkey,[37m [39;49;00mval[37m [39;49;00m[34mof[39;49;00m[37m [39;49;00mobj[37m[39;49;00m$
   151	[37m      [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mtrue[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00mval[37m [39;49;00mis[37m [39;49;00mtarget[37m[39;49;00m$
   152	[37m    [39;49;00m[34mfalse[39;49;00m[37m[39;49;00m$
   153	[37m[39;49;00m$
   154	[37m[39;49;00m$
   155	[37m  [39;49;00m[37m# Invoke a method with arguments on every item in a collection.[39;49;00m[37m[39;49;00m$
   156	[37m  [39;49;00m[31m_.invoke[39;49;00m:[37m [39;49;00m[32m(obj, method) ->[39;49;00m[37m[39;49;00m$
   157	[37m    [39;49;00m[31margs[39;49;00m:[37m [39;49;00m_.rest(arguments,[37m [39;49;00m[34m2[39;49;00m)[37m[39;49;00m$
   158	[37m    [39;49;00m([34mif[39;49;00m[37m [39;49;00mmethod[37m [39;49;00m[34mthen[39;49;00m[37m [39;49;00mval[method][37m [39;49;00m[34melse[39;49;00m[37m [39;49;00mval).apply(val,[37m [39;49;00margs)[37m [39;49;00m[34mfor[39;49;00m[37m [39;49;00mval[37m [39;49;00m[34min[39;49;00m[37m [39;49;00mobj[37m[39;49;00m$
   159	[37m[39;49;00m$
   160	[37m[39;49;00m$
   161	[37m  [39;49;00m[37m# Convenience version of a common use case of map: fetching a property.[39;49;00m[37m[39;49;00m$
   162	[37m  [39;49;00m[31m_.pluck[39;49;00m:[37m [39;49;00m[32m(obj, key) ->[39;49;00m[37m[39;49;00m$
   163	[37m    [39;49;00m_.map(obj,[37m [39;49;00m([32m(val) ->[39;49;00m[37m [39;49;00mval[key]))[37m[39;49;00m$
   164	[37m[39;49;00m$
   165	[37m[39;49;00m$
   166	[37m  [39;49;00m[37m# Return the maximum item or (item-based computation).[39;49;00m[37m[39;49;00m$
   167	[37m  [39;49;00m[31m_.max[39;49;00m:[37m [39;49;00m[32m(obj, iterator, context) ->[39;49;00m[37m[39;49;00m$
   168	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[36mMath[39;49;00m.max.apply([36mMath[39;49;00m,[37m [39;49;00mobj)[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00mnot[37m [39;49;00miterator[37m [39;49;00mand[37m [39;49;00m_.isArray(obj)[37m[39;49;00m$
   169	[37m    [39;49;00m[31mresult[39;49;00m:[37m [39;49;00m{[31mcomputed[39;49;00m:[37m [39;49;00m-[34mInfinity[39;49;00m}[37m[39;49;00m$
   170	[37m    [39;49;00m_.each[37m [39;49;00mobj,[37m [39;49;00m[32m(value, index, list) ->[39;49;00m[37m[39;49;00m$
   171	[37m      [39;49;00m[31mcomputed[39;49;00m:[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00miterator[37m [39;49;00m[34mthen[39;49;00m[37m [39;49;00miterator.call(context,[37m [39;49;00mvalue,[37m [39;49;00mindex,[37m [39;49;00mlist)[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00mvalue[37m[39;49;00m$
   172	[37m      [39;49;00mcomputed[37m [39;49;00m>=[37m [39;49;00mresult.computed[37m [39;49;00mand[37m [39;49;00m([31mresult[39;49;00m:[37m [39;49;00m{[31mvalue[39;49;00m:[37m [39;49;00mvalue,[37m [39;49;00m[31mcomputed[39;49;00m:[37m [39;49;00mcomputed})[37m[39;49;00m$
   173	[37m    [39;49;00mresult.value[37m[39;49;00m$
   174	[37m[39;49;00m$
   175	[37m[39;49;00m$
   176	[37m  [39;49;00m[37m# Return the minimum element (or element-based computation).[39;49;00m[37m[39;49;00m$
   177	[37m  [39;49;00m[31m_.min[39;49;00m:[37m [39;49;00m[32m(obj, iterator, context) ->[39;49;00m[37m[39;49;00m$
   178	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[36mMath[39;49;00m.min.apply([36mMath[39;49;00m,[37m [39;49;00mobj)[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00mnot[37m [39;49;00miterator[37m [39;49;00mand[37m [39;49;00m_.isArray(obj)[37m[39;49;00m$
   179	[37m    [39;49;00m[31mresult[39;49;00m:[37m [39;49;00m{[31mcomputed[39;49;00m:[37m [39;49;00m[34mInfinity[39;49;00m}[37m[39;49;00m$
   180	[37m    [39;49;00m_.each[37m [39;49;00mobj,[37m [39;49;00m[32m(value, index, list) ->[39;49;00m[37m[39;49;00m$
   181	[37m      [39;49;00m[31mcomputed[39;49;00m:[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00miterator[37m [39;49;00m[34mthen[39;49;00m[37m [39;49;00miterator.call(context,[37m [39;49;00mvalue,[37m [39;49;00mindex,[37m [39;49;00mlist)[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00mvalue[37m[39;49;00m$
   182	[37m      [39;49;00mcomputed[37m [39;49;00m<[37m [39;49;00mresult.computed[37m [39;49;00mand[37m [39;49;00m([31mresult[39;49;00m:[37m [39;49;00m{[31mvalue[39;49;00m:[37m [39;49;00mvalue,[37m [39;49;00m[31mcomputed[39;49;00m:[37m [39;49;00mcomputed})[37m[39;49;00m$
   183	[37m    [39;49;00mresult.value[37m[39;49;00m$
   184	[37m[39;49;00m$
   185	[37m[39;49;00m$
   186	[37m  [39;49;00m[37m# Sort the object's values by a criteria produced by an iterator.[39;49;00m[37m[39;49;00m$
   187	[37m  [39;49;00m[31m_.sortBy[39;49;00m:[37m [39;49;00m[32m(obj, iterator, context) ->[39;49;00m[37m[39;49;00m$
   188	[37m    [39;49;00m_.pluck(((_.map[37m [39;49;00mobj,[37m [39;49;00m[32m(value, index, list) ->[39;49;00m[37m[39;49;00m$
   189	[37m      [39;49;00m{[31mvalue[39;49;00m:[37m [39;49;00mvalue,[37m [39;49;00m[31mcriteria[39;49;00m:[37m [39;49;00miterator.call(context,[37m [39;49;00mvalue,[37m [39;49;00mindex,[37m [39;49;00mlist)}[37m[39;49;00m$
   190	[37m    [39;49;00m).sort([32m(left, right) ->[39;49;00m[37m[39;49;00m$
   191	[37m      [39;49;00m[31ma[39;49;00m:[37m [39;49;00mleft.criteria;[37m [39;49;00m[31mb[39;49;00m:[37m [39;49;00mright.criteria[37m[39;49;00m$
   192	[37m      [39;49;00m[34mif[39;49;00m[37m [39;49;00ma[37m [39;49;00m<[37m [39;49;00mb[37m [39;49;00m[34mthen[39;49;00m[37m [39;49;00m-[34m1[39;49;00m[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00ma[37m [39;49;00m>[37m [39;49;00mb[37m [39;49;00m[34mthen[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m[39;49;00m$
   193	[37m    [39;49;00m)),[37m [39;49;00m[33m'[39;49;00m[33mvalue[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
   194	[37m[39;49;00m$
   195	[37m[39;49;00m$
   196	[37m  [39;49;00m[37m# Use a comparator function to figure out at what index an object should[39;49;00m[37m[39;49;00m$
   197	[37m  [39;49;00m[37m# be inserted so as to maintain order. Uses binary search.[39;49;00m[37m[39;49;00m$
   198	[37m  [39;49;00m[31m_.sortedIndex[39;49;00m:[37m [39;49;00m[32m(array, obj, iterator) ->[39;49;00m[37m[39;49;00m$
   199	[37m    [39;49;00miterator[37m [39;49;00m||=[37m [39;49;00m_.identity[37m[39;49;00m$
   200	[37m    [39;49;00m[31mlow[39;49;00m:[37m [39;49;00m[34m0[39;49;00m;[37m [39;49;00m[31mhigh[39;49;00m:[37m [39;49;00marray.length[37m[39;49;00m$
   201	[37m    [39;49;00m[34mwhile[39;49;00m[37m [39;49;00mlow[37m [39;49;00m<[37m [39;49;00mhigh[37m[39;49;00m$
   202	[37m      [39;49;00m[31mmid[39;49;00m:[37m [39;49;00m(low[37m [39;49;00m+[37m [39;49;00mhigh)[37m [39;49;00m>>[37m [39;49;00m[34m1[39;49;00m[37m[39;49;00m$
   203	[37m      [39;49;00m[34mif[39;49;00m[37m [39;49;00miterator(array[mid])[37m [39;49;00m<[37m [39;49;00miterator(obj)[37m [39;49;00m[34mthen[39;49;00m[37m [39;49;00m[31mlow[39;49;00m:[37m [39;49;00mmid[37m [39;49;00m+[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00m[31mhigh[39;49;00m:[37m [39;49;00mmid[37m[39;49;00m$
   204	[37m    [39;49;00mlow[37m[39;49;00m$
   205	[37m[39;49;00m$
   206	[37m[39;49;00m$
   207	[37m  [39;49;00m[37m# Convert anything iterable into a real, live array.[39;49;00m[37m[39;49;00m$
   208	[37m  [39;49;00m[31m_.toArray[39;49;00m:[37m [39;49;00m[32m(iterable) ->[39;49;00m[37m[39;49;00m$
   209	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[][37m                   [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!iterable)[37m[39;49;00m$
   210	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00miterable.toArray()[37m   [39;49;00m[34mif[39;49;00m[37m [39;49;00m(iterable.toArray)[37m[39;49;00m$
   211	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00miterable[37m             [39;49;00m[34mif[39;49;00m[37m [39;49;00m(_.isArray(iterable))[37m[39;49;00m$
   212	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mslice.call(iterable)[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(_.isArguments(iterable))[37m[39;49;00m$
   213	[37m    [39;49;00m_.values(iterable)[37m[39;49;00m$
   214	[37m[39;49;00m$
   215	[37m[39;49;00m$
   216	[37m  [39;49;00m[37m# Return the number of elements in an object.[39;49;00m[37m[39;49;00m$
   217	[37m  [39;49;00m[31m_.size[39;49;00m:[37m [39;49;00m[32m(obj) ->[39;49;00m[37m [39;49;00m_.toArray(obj).length[37m[39;49;00m$
   218	[37m[39;49;00m$
   219	[37m[39;49;00m$
   220	[37m  [39;49;00m[37m# -------------------------- Array Functions: ------------------------------[39;49;00m[37m[39;49;00m$
   221	[37m[39;49;00m$
   222	[37m  [39;49;00m[37m# Get the first element of an array. Passing "n" will return the first N[39;49;00m[37m[39;49;00m$
   223	[37m  [39;49;00m[37m# values in the array. Aliased as "head". The "guard" check allows it to work[39;49;00m[37m[39;49;00m$
   224	[37m  [39;49;00m[37m# with _.map.[39;49;00m[37m[39;49;00m$
   225	[37m  [39;49;00m[31m_.first[39;49;00m:[37m [39;49;00m[32m(array, n, guard) ->[39;49;00m[37m[39;49;00m$
   226	[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00mn[37m [39;49;00mand[37m [39;49;00mnot[37m [39;49;00mguard[37m [39;49;00m[34mthen[39;49;00m[37m [39;49;00mslice.call(array,[37m [39;49;00m[34m0[39;49;00m,[37m [39;49;00mn)[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00marray[[34m0[39;49;00m][37m[39;49;00m$
   227	[37m[39;49;00m$
   228	[37m[39;49;00m$
   229	[37m  [39;49;00m[37m# Returns everything but the first entry of the array. Aliased as "tail".[39;49;00m[37m[39;49;00m$
   230	[37m  [39;49;00m[37m# Especially useful on the arguments object. Passing an "index" will return[39;49;00m[37m[39;49;00m$
   231	[37m  [39;49;00m[37m# the rest of the values in the array from that index onward. The "guard"[39;49;00m[37m[39;49;00m$
   232	[37m  [39;49;00m[37m# check allows it to work with _.map.[39;49;00m[37m[39;49;00m$
   233	[37m  [39;49;00m[31m_.rest[39;49;00m:[37m [39;49;00m[32m(array, index, guard) ->[39;49;00m[37m[39;49;00m$
   234	[37m    [39;49;00mslice.call(array,[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m_.isUndefined(index)[37m [39;49;00mor[37m [39;49;00mguard[37m [39;49;00m[34mthen[39;49;00m[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00mindex)[37m[39;49;00m$
   235	[37m[39;49;00m$
   236	[37m[39;49;00m$
   237	[37m  [39;49;00m[37m# Get the last element of an array.[39;49;00m[37m[39;49;00m$
   238	[37m  [39;49;00m[31m_.last[39;49;00m:[37m [39;49;00m[32m(array) ->[39;49;00m[37m [39;49;00marray[array.length[37m [39;49;00m-[37m [39;49;00m[34m1[39;49;00m][37m[39;49;00m$
   239	[37m[39;49;00m$
   240	[37m[39;49;00m$
   241	[37m  [39;49;00m[37m# Trim out all falsy values from an array.[39;49;00m[37m[39;49;00m$
   242	[37m  [39;49;00m[31m_.compact[39;49;00m:[37m [39;49;00m[32m(array) ->[39;49;00m[37m [39;49;00marray[i][37m [39;49;00m[34mfor[39;49;00m[37m [39;49;00mi[37m [39;49;00m[34min[39;49;00m[37m [39;49;00m[[34m0[39;49;00m...array.length][37m [39;49;00m[34mwhen[39;49;00m[37m [39;49;00marray[i][37m[39;49;00m$
   243	[37m[39;49;00m$
   244	[37m[39;49;00m$
   245	[37m  [39;49;00m[37m# Return a completely flattened version of an array.[39;49;00m[37m[39;49;00m$
   246	[37m  [39;49;00m[31m_.flatten[39;49;00m:[37m [39;49;00m[32m(array) ->[39;49;00m[37m[39;49;00m$
   247	[37m    [39;49;00m_.reduce[37m [39;49;00marray,[37m [39;49;00m[],[37m [39;49;00m[32m(memo, value) ->[39;49;00m[37m[39;49;00m$
   248	[37m      [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mmemo.concat(_.flatten(value))[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m_.isArray(value)[37m[39;49;00m$
   249	[37m      [39;49;00mmemo.push(value)[37m[39;49;00m$
   250	[37m      [39;49;00mmemo[37m[39;49;00m$
   251	[37m[39;49;00m$
   252	[37m[39;49;00m$
   253	[37m  [39;49;00m[37m# Return a version of the array that does not contain the specified value(s).[39;49;00m[37m[39;49;00m$
   254	[37m  [39;49;00m[31m_.without[39;49;00m:[37m [39;49;00m[32m(array) ->[39;49;00m[37m[39;49;00m$
   255	[37m    [39;49;00m[31mvalues[39;49;00m:[37m [39;49;00m_.rest(arguments)[37m[39;49;00m$
   256	[37m    [39;49;00mval[37m [39;49;00m[34mfor[39;49;00m[37m [39;49;00mval[37m [39;49;00m[34min[39;49;00m[37m [39;49;00m_.toArray(array)[37m [39;49;00m[34mwhen[39;49;00m[37m [39;49;00mnot[37m [39;49;00m_.include(values,[37m [39;49;00mval)[37m[39;49;00m$
   257	[37m[39;49;00m$
   258	[37m[39;49;00m$
   259	[37m  [39;49;00m[37m# Produce a duplicate-free version of the array. If the array has already[39;49;00m[37m[39;49;00m$
   260	[37m  [39;49;00m[37m# been sorted, you have the option of using a faster algorithm.[39;49;00m[37m[39;49;00m$
   261	[37m  [39;49;00m[31m_.uniq[39;49;00m:[37m [39;49;00m[32m(array, isSorted) ->[39;49;00m[37m[39;49;00m$
   262	[37m    [39;49;00m[31mmemo[39;49;00m:[37m [39;49;00m[][37m[39;49;00m$
   263	[37m    [39;49;00m[34mfor[39;49;00m[37m [39;49;00mel,[37m [39;49;00mi[37m [39;49;00m[34min[39;49;00m[37m [39;49;00m_.toArray(array)[37m[39;49;00m$
   264	[37m      [39;49;00mmemo.push(el)[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00mi[37m [39;49;00mis[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m||[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00misSorted[37m [39;49;00mis[37m [39;49;00m[34mtrue[39;49;00m[37m [39;49;00m[34mthen[39;49;00m[37m [39;49;00m_.last(memo)[37m [39;49;00misnt[37m [39;49;00mel[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00mnot[37m [39;49;00m_.include(memo,[37m [39;49;00mel))[37m[39;49;00m$
   265	[37m    [39;49;00mmemo[37m[39;49;00m$
   266	[37m[39;49;00m$
   267	[37m[39;49;00m$
   268	[37m  [39;49;00m[37m# Produce an array that contains every item shared between all the[39;49;00m[37m[39;49;00m$
   269	[37m  [39;49;00m[37m# passed-in arrays.[39;49;00m[37m[39;49;00m$
   270	[37m  [39;49;00m[31m_.intersect[39;49;00m:[37m [39;49;00m[32m(array) ->[39;49;00m[37m[39;49;00m$
   271	[37m    [39;49;00m[31mrest[39;49;00m:[37m [39;49;00m_.rest(arguments)[37m[39;49;00m$
   272	[37m    [39;49;00m_.select[37m [39;49;00m_.uniq(array),[37m [39;49;00m[32m(item) ->[39;49;00m[37m[39;49;00m$
   273	[37m      [39;49;00m_.all[37m [39;49;00mrest,[37m [39;49;00m[32m(other) ->[39;49;00m[37m[39;49;00m$
   274	[37m        [39;49;00m_.indexOf(other,[37m [39;49;00mitem)[37m [39;49;00m>=[37m [39;49;00m[34m0[39;49;00m[37m[39;49;00m$
   275	[37m[39;49;00m$
   276	[37m[39;49;00m$
   277	[37m  [39;49;00m[37m# Zip together multiple lists into a single array -- elements that share[39;49;00m[37m[39;49;00m$
   278	[37m  [39;49;00m[37m# an index go together.[39;49;00m[37m[39;49;00m$
   279	[37m  [39;49;00m[31m_.zip[39;49;00m:[37m [39;49;00m[32m->[39;49;00m[37m[39;49;00m$
   280	[37m    [39;49;00m[31mlength[39;49;00m:[37m     [39;49;00m_.max(_.pluck(arguments,[37m [39;49;00m[33m'[39;49;00m[33mlength[39;49;00m[33m'[39;49;00m))[37m[39;49;00m$
   281	[37m    [39;49;00m[31mresults[39;49;00m:[37m    [39;49;00m[34mnew[39;49;00m[37m [39;49;00m[36mArray[39;49;00m(length)[37m[39;49;00m$
   282	[37m    [39;49;00m[34mfor[39;49;00m[37m [39;49;00mi[37m [39;49;00m[34min[39;49;00m[37m [39;49;00m[[34m0[39;49;00m...length][37m[39;49;00m$
   283	[37m      [39;49;00mresults[i]:[37m [39;49;00m_.pluck(arguments,[37m [39;49;00m[36mString[39;49;00m(i))[37m[39;49;00m$
   284	[37m    [39;49;00mresults[37m[39;49;00m$
   285	[37m[39;49;00m$
   286	[37m[39;49;00m$
   287	[37m  [39;49;00m[37m# If the browser doesn't supply us with indexOf (I'm looking at you, MSIE),[39;49;00m[37m[39;49;00m$
   288	[37m  [39;49;00m[37m# we need this function. Return the position of the first occurence of an[39;49;00m[37m[39;49;00m$
   289	[37m  [39;49;00m[37m# item in an array, or -1 if the item is not included in the array.[39;49;00m[37m[39;49;00m$
   290	[37m  [39;49;00m[31m_.indexOf[39;49;00m:[37m [39;49;00m[32m(array, item) ->[39;49;00m[37m[39;49;00m$
   291	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00marray.indexOf(item)[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00marray.indexOf[37m[39;49;00m$
   292	[37m    [39;49;00m[31mi[39;49;00m:[37m [39;49;00m[34m0[39;49;00m;[37m [39;49;00m[31ml[39;49;00m:[37m [39;49;00marray.length[37m[39;49;00m$
   293	[37m    [39;49;00m[34mwhile[39;49;00m[37m [39;49;00ml[37m [39;49;00m-[37m [39;49;00mi[37m[39;49;00m$
   294	[37m      [39;49;00m[34mif[39;49;00m[37m [39;49;00marray[i][37m [39;49;00mis[37m [39;49;00mitem[37m [39;49;00m[34mthen[39;49;00m[37m [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mi[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00mi++[37m[39;49;00m$
   295	[37m    [39;49;00m-[34m1[39;49;00m[37m[39;49;00m$
   296	[37m[39;49;00m$
   297	[37m[39;49;00m$
   298	[37m  [39;49;00m[37m# Provide JavaScript 1.6's lastIndexOf, delegating to the native function,[39;49;00m[37m[39;49;00m$
   299	[37m  [39;49;00m[37m# if possible.[39;49;00m[37m[39;49;00m$
   300	[37m  [39;49;00m[31m_.lastIndexOf[39;49;00m:[37m [39;49;00m[32m(array, item) ->[39;49;00m[37m[39;49;00m$
   301	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00marray.lastIndexOf(item)[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00marray.lastIndexOf[37m[39;49;00m$
   302	[37m    [39;49;00m[31mi[39;49;00m:[37m [39;49;00marray.length[37m[39;49;00m$
   303	[37m    [39;49;00m[34mwhile[39;49;00m[37m [39;49;00mi[37m[39;49;00m$
   304	[37m      [39;49;00m[34mif[39;49;00m[37m [39;49;00marray[i][37m [39;49;00mis[37m [39;49;00mitem[37m [39;49;00m[34mthen[39;49;00m[37m [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mi[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00mi--[37m[39;49;00m$
   305	[37m    [39;49;00m-[34m1[39;49;00m[37m[39;49;00m$
   306	[37m[39;49;00m$
   307	[37m[39;49;00m$
   308	[37m  [39;49;00m[37m# Generate an integer Array containing an arithmetic progression. A port of[39;49;00m[37m[39;49;00m$
   309	[37m  [39;49;00m[37m# the native Python range() function. See:[39;49;00m[37m[39;49;00m$
   310	[37m  [39;49;00m[37m# http://docs.python.org/library/functions.html#range[39;49;00m[37m[39;49;00m$
   311	[37m  [39;49;00m[31m_.range[39;49;00m:[37m [39;49;00m[32m(start, stop, step) ->[39;49;00m[37m[39;49;00m$
   312	[37m    [39;49;00m[31ma[39;49;00m:[37m        [39;49;00marguments[37m[39;49;00m$
   313	[37m    [39;49;00m[31msolo[39;49;00m:[37m     [39;49;00ma.length[37m [39;49;00m<=[37m [39;49;00m[34m1[39;49;00m[37m[39;49;00m$
   314	[37m    [39;49;00m[31mi[39;49;00m:[37m [39;49;00m[31mstart[39;49;00m:[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00msolo[37m [39;49;00m[34mthen[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00ma[[34m0[39;49;00m];[37m[39;49;00m$
   315	[37m    [39;49;00m[31mstop[39;49;00m:[37m     [39;49;00m[34mif[39;49;00m[37m [39;49;00msolo[37m [39;49;00m[34mthen[39;49;00m[37m [39;49;00ma[[34m0[39;49;00m][37m [39;49;00m[34melse[39;49;00m[37m [39;49;00ma[[34m1[39;49;00m];[37m[39;49;00m$
   316	[37m    [39;49;00m[31mstep[39;49;00m:[37m     [39;49;00ma[[34m2[39;49;00m][37m [39;49;00mor[37m [39;49;00m[34m1[39;49;00m[37m[39;49;00m$
   317	[37m    [39;49;00m[31mlen[39;49;00m:[37m      [39;49;00m[36mMath[39;49;00m.ceil((stop[37m [39;49;00m-[37m [39;49;00mstart)[37m [39;49;00m/[37m [39;49;00mstep)[37m[39;49;00m$
   318	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[][37m [39;49;00m[34mif[39;49;00m[37m [39;49;00mlen[37m [39;49;00m<=[37m [39;49;00m[34m0[39;49;00m[37m[39;49;00m$
   319	[37m    [39;49;00m[31mrange[39;49;00m:[37m    [39;49;00m[34mnew[39;49;00m[37m [39;49;00m[36mArray[39;49;00m(len)[37m[39;49;00m$
   320	[37m    [39;49;00m[31midx[39;49;00m:[37m      [39;49;00m[34m0[39;49;00m[37m[39;49;00m$
   321	[37m    [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m[34mtrue[39;49;00m[37m[39;49;00m$
   322	[37m      [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mrange[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m([34mif[39;49;00m[37m [39;49;00mstep[37m [39;49;00m>[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[34mthen[39;49;00m[37m [39;49;00mi[37m [39;49;00m-[37m [39;49;00mstop[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00mstop[37m [39;49;00m-[37m [39;49;00mi)[37m [39;49;00m>=[37m [39;49;00m[34m0[39;49;00m[37m[39;49;00m$
   323	[37m      [39;49;00mrange[idx]:[37m [39;49;00mi[37m[39;49;00m$
   324	[37m      [39;49;00midx++[37m[39;49;00m$
   325	[37m      [39;49;00mi+=[37m [39;49;00mstep[37m[39;49;00m$
   326	[37m[39;49;00m$
   327	[37m[39;49;00m$
   328	[37m  [39;49;00m[37m# ----------------------- Function Functions: -----------------------------[39;49;00m[37m[39;49;00m$
   329	[37m[39;49;00m$
   330	[37m  [39;49;00m[37m# Create a function bound to a given object (assigning 'this', and arguments,[39;49;00m[37m[39;49;00m$
   331	[37m  [39;49;00m[37m# optionally). Binding with arguments is also known as 'curry'.[39;49;00m[37m[39;49;00m$
   332	[37m  [39;49;00m[31m_.bind[39;49;00m:[37m [39;49;00m[32m(func, obj) ->[39;49;00m[37m[39;49;00m$
   333	[37m    [39;49;00m[31margs[39;49;00m:[37m [39;49;00m_.rest[32m(arguments, 2)[39;49;00m$
   334	[32m    ->[39;49;00m[37m [39;49;00mfunc.apply(obj[37m [39;49;00mor[37m [39;49;00mroot,[37m [39;49;00margs.concat(arguments))[37m[39;49;00m$
   335	[37m[39;49;00m$
   336	[37m[39;49;00m$
   337	[37m  [39;49;00m[37m# Bind all of an object's methods to that object. Useful for ensuring that[39;49;00m[37m[39;49;00m$
   338	[37m  [39;49;00m[37m# all callbacks defined on an object belong to it.[39;49;00m[37m[39;49;00m$
   339	[37m  [39;49;00m[31m_.bindAll[39;49;00m:[37m [39;49;00m[32m(obj) ->[39;49;00m[37m[39;49;00m$
   340	[37m    [39;49;00m[31mfuncs[39;49;00m:[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00marguments.length[37m [39;49;00m>[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m[34mthen[39;49;00m[37m [39;49;00m_.rest(arguments)[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00m_.functions(obj)[37m[39;49;00m$
   341	[37m    [39;49;00m_.each(funcs,[37m [39;49;00m[32m(f) ->[39;49;00m[37m [39;49;00mobj[f]:[37m [39;49;00m_.bind(obj[f],[37m [39;49;00mobj))[37m[39;49;00m$
   342	[37m    [39;49;00mobj[37m[39;49;00m$
   343	[37m[39;49;00m$
   344	[37m[39;49;00m$
   345	[37m  [39;49;00m[37m# Delays a function for the given number of milliseconds, and then calls[39;49;00m[37m[39;49;00m$
   346	[37m  [39;49;00m[37m# it with the arguments supplied.[39;49;00m[37m[39;49;00m$
   347	[37m  [39;49;00m[31m_.delay[39;49;00m:[37m [39;49;00m[32m(func, wait) ->[39;49;00m[37m[39;49;00m$
   348	[37m    [39;49;00m[31margs[39;49;00m:[37m [39;49;00m_.rest(arguments,[37m [39;49;00m[34m2[39;49;00m)[37m[39;49;00m$
   349	[37m    [39;49;00msetTimeout(([32m->[39;49;00m[37m [39;49;00mfunc.apply(func,[37m [39;49;00margs)),[37m [39;49;00mwait)[37m[39;49;00m$
   350	[37m[39;49;00m$
   351	[37m[39;49;00m$
   352	[37m  [39;49;00m[37m# Defers a function, scheduling it to run after the current call stack has[39;49;00m[37m[39;49;00m$
   353	[37m  [39;49;00m[37m# cleared.[39;49;00m[37m[39;49;00m$
   354	[37m  [39;49;00m[31m_.defer[39;49;00m:[37m [39;49;00m[32m(func) ->[39;49;00m[37m[39;49;00m$
   355	[37m    [39;49;00m_.delay.apply(_,[37m [39;49;00m[func,[37m [39;49;00m[34m1[39;49;00m].concat(_.rest(arguments)))[37m[39;49;00m$
   356	[37m[39;49;00m$
   357	[37m[39;49;00m$
   358	[37m  [39;49;00m[37m# Returns the first function passed as an argument to the second,[39;49;00m[37m[39;49;00m$
   359	[37m  [39;49;00m[37m# allowing you to adjust arguments, run code before and after, and[39;49;00m[37m[39;49;00m$
   360	[37m  [39;49;00m[37m# conditionally execute the original function.[39;49;00m[37m[39;49;00m$
   361	[37m  [39;49;00m[31m_.wrap[39;49;00m:[37m [39;49;00m[32m(func, wrapper) ->[39;49;00m[37m[39;49;00m$
   362	[37m    [39;49;00m[32m->[39;49;00m[37m [39;49;00mwrapper.apply(wrapper,[37m [39;49;00m[func].concat(arguments))[37m[39;49;00m$
   363	[37m[39;49;00m$
   364	[37m[39;49;00m$
   365	[37m  [39;49;00m[37m# Returns a function that is the composition of a list of functions, each[39;49;00m[37m[39;49;00m$
   366	[37m  [39;49;00m[37m# consuming the return value of the function that follows.[39;49;00m[37m[39;49;00m$
   367	[37m  [39;49;00m[31m_.compose[39;49;00m:[37m [39;49;00m[32m->[39;49;00m[37m[39;49;00m$
   368	[37m    [39;49;00m[31mfuncs[39;49;00m:[37m [39;49;00marguments[37m[39;49;00m$
   369	[37m    [39;49;00m[32m->[39;49;00m[37m[39;49;00m$
   370	[37m      [39;49;00m[31margs[39;49;00m:[37m [39;49;00marguments[37m[39;49;00m$
   371	[37m      [39;49;00m[34mfor[39;49;00m[37m [39;49;00mi[37m [39;49;00m[34min[39;49;00m[37m [39;49;00m[(funcs.length[37m [39;49;00m-[37m [39;49;00m[34m1[39;49;00m)..[34m0[39;49;00m][37m[39;49;00m$
   372	[37m        [39;49;00m[31margs[39;49;00m:[37m [39;49;00m[funcs[i].apply([34mthis[39;49;00m,[37m [39;49;00margs)][37m[39;49;00m$
   373	[37m      [39;49;00margs[[34m0[39;49;00m][37m[39;49;00m$
   374	[37m[39;49;00m$
   375	[37m[39;49;00m$
   376	[37m  [39;49;00m[37m# ------------------------- Object Functions: ----------------------------[39;49;00m[37m[39;49;00m$
   377	[37m[39;49;00m$
   378	[37m  [39;49;00m[37m# Retrieve the names of an object's properties.[39;49;00m[37m[39;49;00m$
   379	[37m  [39;49;00m[31m_.keys[39;49;00m:[37m [39;49;00m[32m(obj) ->[39;49;00m[37m[39;49;00m$
   380	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m_.range([34m0[39;49;00m,[37m [39;49;00mobj.length)[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m_.isArray(obj)[37m[39;49;00m$
   381	[37m    [39;49;00mkey[37m [39;49;00m[34mfor[39;49;00m[37m [39;49;00mkey,[37m [39;49;00mval[37m [39;49;00m[34mof[39;49;00m[37m [39;49;00mobj[37m[39;49;00m$
   382	[37m[39;49;00m$
   383	[37m[39;49;00m$
   384	[37m  [39;49;00m[37m# Retrieve the values of an object's properties.[39;49;00m[37m[39;49;00m$
   385	[37m  [39;49;00m[31m_.values[39;49;00m:[37m [39;49;00m[32m(obj) ->[39;49;00m[37m[39;49;00m$
   386	[37m    [39;49;00m_.map(obj,[37m [39;49;00m_.identity)[37m[39;49;00m$
   387	[37m[39;49;00m$
   388	[37m[39;49;00m$
   389	[37m  [39;49;00m[37m# Return a sorted list of the function names available in Underscore.[39;49;00m[37m[39;49;00m$
   390	[37m  [39;49;00m[31m_.functions[39;49;00m:[37m [39;49;00m[32m(obj) ->[39;49;00m[37m[39;49;00m$
   391	[37m    [39;49;00m_.select(_.keys(obj),[37m [39;49;00m[32m(key) ->[39;49;00m[37m [39;49;00m_.isFunction(obj[key])).sort()[37m[39;49;00m$
   392	[37m[39;49;00m$
   393	[37m[39;49;00m$
   394	[37m  [39;49;00m[37m# Extend a given object with all of the properties in a source object.[39;49;00m[37m[39;49;00m$
   395	[37m  [39;49;00m[31m_.extend[39;49;00m:[37m [39;49;00m[32m(destination, source) ->[39;49;00m[37m[39;49;00m$
   396	[37m    [39;49;00m[34mfor[39;49;00m[37m [39;49;00mkey,[37m [39;49;00mval[37m [39;49;00m[34mof[39;49;00m[37m [39;49;00msource[37m[39;49;00m$
   397	[37m      [39;49;00mdestination[key]:[37m [39;49;00mval[37m[39;49;00m$
   398	[37m    [39;49;00mdestination[37m[39;49;00m$
   399	[37m[39;49;00m$
   400	[37m[39;49;00m$
   401	[37m  [39;49;00m[37m# Create a (shallow-cloned) duplicate of an object.[39;49;00m[37m[39;49;00m$
   402	[37m  [39;49;00m[31m_.clone[39;49;00m:[37m [39;49;00m[32m(obj) ->[39;49;00m[37m[39;49;00m$
   403	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mobj.slice([34m0[39;49;00m)[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m_.isArray(obj)[37m[39;49;00m$
   404	[37m    [39;49;00m_.extend({},[37m [39;49;00mobj)[37m[39;49;00m$
   405	[37m[39;49;00m$
   406	[37m[39;49;00m$
   407	[37m  [39;49;00m[37m# Invokes interceptor with the obj, and then returns obj.[39;49;00m[37m[39;49;00m$
   408	[37m  [39;49;00m[37m# The primary purpose of this method is to "tap into" a method chain, in order to perform operations on intermediate results within the chain.[39;49;00m[37m[39;49;00m$
   409	[37m  [39;49;00m[31m_.tap[39;49;00m:[37m [39;49;00m[32m(obj, interceptor) ->[39;49;00m[37m[39;49;00m$
   410	[37m    [39;49;00minterceptor(obj)[37m[39;49;00m$
   411	[37m    [39;49;00mobj[37m[39;49;00m$
   412	[37m[39;49;00m$
   413	[37m[39;49;00m$
   414	[37m  [39;49;00m[37m# Perform a deep comparison to check if two objects are equal.[39;49;00m[37m[39;49;00m$
   415	[37m  [39;49;00m[31m_.isEqual[39;49;00m:[37m [39;49;00m[32m(a, b) ->[39;49;00m[37m[39;49;00m$
   416	[37m    [39;49;00m[37m# Check object identity.[39;49;00m[37m[39;49;00m$
   417	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mtrue[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00ma[37m [39;49;00mis[37m [39;49;00mb[37m[39;49;00m$
   418	[37m    [39;49;00m[37m# Different types?[39;49;00m[37m[39;49;00m$
   419	[37m    [39;49;00m[31matype[39;49;00m:[37m [39;49;00m[34mtypeof[39;49;00m(a);[37m [39;49;00m[31mbtype[39;49;00m:[37m [39;49;00m[34mtypeof[39;49;00m(b)[37m[39;49;00m$
   420	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mfalse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00matype[37m [39;49;00misnt[37m [39;49;00mbtype[37m[39;49;00m$
   421	[37m    [39;49;00m[37m# Basic equality test (watch out for coercions).[39;49;00m[37m[39;49;00m$
   422	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mtrue[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m`a[37m [39;49;00m==[37m [39;49;00mb`[37m[39;49;00m$
   423	[37m    [39;49;00m[37m# One is falsy and the other truthy.[39;49;00m[37m[39;49;00m$
   424	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mfalse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!a[37m [39;49;00mand[37m [39;49;00mb)[37m [39;49;00mor[37m [39;49;00m(a[37m [39;49;00mand[37m [39;49;00m!b)[37m[39;49;00m$
   425	[37m    [39;49;00m[37m# One of them implements an isEqual()?[39;49;00m[37m[39;49;00m$
   426	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00ma.isEqual(b)[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00ma.isEqual[37m[39;49;00m$
   427	[37m    [39;49;00m[37m# Check dates' integer values.[39;49;00m[37m[39;49;00m$
   428	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00ma.getTime()[37m [39;49;00mis[37m [39;49;00mb.getTime()[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m_.isDate(a)[37m [39;49;00mand[37m [39;49;00m_.isDate(b)[37m[39;49;00m$
   429	[37m    [39;49;00m[37m# Both are NaN?[39;49;00m[37m[39;49;00m$
   430	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mtrue[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m_.[36misNaN[39;49;00m(a)[37m [39;49;00mand[37m [39;49;00m_.[36misNaN[39;49;00m(b)[37m[39;49;00m$
   431	[37m    [39;49;00m[37m# Compare regular expressions.[39;49;00m[37m[39;49;00m$
   432	[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m_.isRegExp(a)[37m [39;49;00mand[37m [39;49;00m_.isRegExp(b)[37m[39;49;00m$
   433	[37m      [39;49;00m[34mreturn[39;49;00m[37m [39;49;00ma.source[37m     [39;49;00mis[37m [39;49;00mb.source[37m [39;49;00mand[37m[39;49;00m$
   434	[37m             [39;49;00ma.global[37m     [39;49;00mis[37m [39;49;00mb.global[37m [39;49;00mand[37m[39;49;00m$
   435	[37m             [39;49;00ma.ignoreCase[37m [39;49;00mis[37m [39;49;00mb.ignoreCase[37m [39;49;00mand[37m[39;49;00m$
   436	[37m             [39;49;00ma.multiline[37m  [39;49;00mis[37m [39;49;00mb.multiline[37m[39;49;00m$
   437	[37m    [39;49;00m[37m# If a is not an object by this point, we can't handle it.[39;49;00m[37m[39;49;00m$
   438	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mfalse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00matype[37m [39;49;00misnt[37m [39;49;00m[33m'[39;49;00m[33mobject[39;49;00m[33m'[39;49;00m[37m[39;49;00m$
   439	[37m    [39;49;00m[37m# Check for different array lengths before comparing contents.[39;49;00m[37m[39;49;00m$
   440	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mfalse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00ma.length[37m [39;49;00mand[37m [39;49;00m(a.length[37m [39;49;00misnt[37m [39;49;00mb.length)[37m[39;49;00m$
   441	[37m    [39;49;00m[37m# Nothing else worked, deep compare the contents.[39;49;00m[37m[39;49;00m$
   442	[37m    [39;49;00m[31maKeys[39;49;00m:[37m [39;49;00m_.keys(a);[37m [39;49;00m[31mbKeys[39;49;00m:[37m [39;49;00m_.keys(b)[37m[39;49;00m$
   443	[37m    [39;49;00m[37m# Different object sizes?[39;49;00m[37m[39;49;00m$
   444	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mfalse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00maKeys.length[37m [39;49;00misnt[37m [39;49;00mbKeys.length[37m[39;49;00m$
   445	[37m    [39;49;00m[37m# Recursive comparison of contents.[39;49;00m[37m[39;49;00m$
   446	[37m    [39;49;00m[37m# for (var key in a) if (!_.isEqual(a[key], b[key])) return false;[39;49;00m[37m[39;49;00m$
   447	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mtrue[39;49;00m[37m[39;49;00m$
   448	[37m[39;49;00m$
   449	[37m[39;49;00m$
   450	[37m  [39;49;00m[37m# Is a given array or object empty?[39;49;00m[37m[39;49;00m$
   451	[37m  [39;49;00m[31m_.isEmpty[39;49;00m:[37m      [39;49;00m[32m(obj) ->[39;49;00m[37m [39;49;00m_.keys(obj).length[37m [39;49;00mis[37m [39;49;00m[34m0[39;49;00m[37m[39;49;00m$
   452	[37m[39;49;00m$
   453	[37m[39;49;00m$
   454	[37m  [39;49;00m[37m# Is a given value a DOM element?[39;49;00m[37m[39;49;00m$
   455	[37m  [39;49;00m[31m_.isElement[39;49;00m:[37m    [39;49;00m[32m(obj) ->[39;49;00m[37m [39;49;00mobj[37m [39;49;00mand[37m [39;49;00mobj.nodeType[37m [39;49;00mis[37m [39;49;00m[34m1[39;49;00m[37m[39;49;00m$
   456	[37m[39;49;00m$
   457	[37m[39;49;00m$
   458	[37m  [39;49;00m[37m# Is a given value an array?[39;49;00m[37m[39;49;00m$
   459	[37m  [39;49;00m[31m_.isArray[39;49;00m:[37m      [39;49;00m[32m(obj) ->[39;49;00m[37m [39;49;00m!!(obj[37m [39;49;00mand[37m [39;49;00mobj.concat[37m [39;49;00mand[37m [39;49;00mobj.unshift)[37m[39;49;00m$
   460	[37m[39;49;00m$
   461	[37m[39;49;00m$
   462	[37m  [39;49;00m[37m# Is a given variable an arguments object?[39;49;00m[37m[39;49;00m$
   463	[37m  [39;49;00m[31m_.isArguments[39;49;00m:[37m  [39;49;00m[32m(obj) ->[39;49;00m[37m [39;49;00mobj[37m [39;49;00mand[37m [39;49;00m_.isNumber(obj.length)[37m [39;49;00mand[37m [39;49;00mnot[37m [39;49;00mobj.concat[37m [39;49;00mand[37m[39;49;00m$
   464	[37m                           [39;49;00mnot[37m [39;49;00mobj.substr[37m [39;49;00mand[37m [39;49;00mnot[37m [39;49;00mobj.apply[37m [39;49;00mand[37m [39;49;00mnot[37m [39;49;00mpropertyIsEnumerable.call(obj,[37m [39;49;00m[33m'[39;49;00m[33mlength[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
   465	[37m[39;49;00m$
   466	[37m[39;49;00m$
   467	[37m  [39;49;00m[37m# Is the given value a function?[39;49;00m[37m[39;49;00m$
   468	[37m  [39;49;00m[31m_.isFunction[39;49;00m:[37m   [39;49;00m[32m(obj) ->[39;49;00m[37m [39;49;00m!!(obj[37m [39;49;00mand[37m [39;49;00mobj.constructor[37m [39;49;00mand[37m [39;49;00mobj.call[37m [39;49;00mand[37m [39;49;00mobj.apply)[37m[39;49;00m$
   469	[37m[39;49;00m$
   470	[37m[39;49;00m$
   471	[37m  [39;49;00m[37m# Is the given value a string?[39;49;00m[37m[39;49;00m$
   472	[37m  [39;49;00m[31m_.isString[39;49;00m:[37m     [39;49;00m[32m(obj) ->[39;49;00m[37m [39;49;00m!!(obj[37m [39;49;00mis[37m [39;49;00m[33m'[39;49;00m[33m'[39;49;00m[37m [39;49;00mor[37m [39;49;00m(obj[37m [39;49;00mand[37m [39;49;00mobj.charCodeAt[37m [39;49;00mand[37m [39;49;00mobj.substr))[37m[39;49;00m$
   473	[37m[39;49;00m$
   474	[37m[39;49;00m$
   475	[37m  [39;49;00m[37m# Is a given value a number?[39;49;00m[37m[39;49;00m$
   476	[37m  [39;49;00m[31m_.isNumber[39;49;00m:[37m     [39;49;00m[32m(obj) ->[39;49;00m[37m [39;49;00m(obj[37m [39;49;00mis[37m [39;49;00m+obj)[37m [39;49;00mor[37m [39;49;00mtoString.call(obj)[37m [39;49;00mis[37m [39;49;00m[33m'[39;49;00m[33m[object Number][39;49;00m[33m'[39;49;00m[37m[39;49;00m$
   477	[37m[39;49;00m$
   478	[37m[39;49;00m$
   479	[37m  [39;49;00m[37m# Is a given value a Date?[39;49;00m[37m[39;49;00m$
   480	[37m  [39;49;00m[31m_.isDate[39;49;00m:[37m       [39;49;00m[32m(obj) ->[39;49;00m[37m [39;49;00m!!(obj[37m [39;49;00mand[37m [39;49;00mobj.getTimezoneOffset[37m [39;49;00mand[37m [39;49;00mobj.setUTCFullYear)[37m[39;49;00m$
   481	[37m[39;49;00m$
   482	[37m[39;49;00m$
   483	[37m  [39;49;00m[37m# Is the given value a regular expression?[39;49;00m[37m[39;49;00m$
   484	[37m  [39;49;00m[31m_.isRegExp[39;49;00m:[37m     [39;49;00m[32m(obj) ->[39;49;00m[37m [39;49;00m!!(obj[37m [39;49;00mand[37m [39;49;00mobj.exec[37m [39;49;00mand[37m [39;49;00m(obj.ignoreCase[37m [39;49;00mor[37m [39;49;00mobj.ignoreCase[37m [39;49;00mis[37m [39;49;00m[34mfalse[39;49;00m))[37m[39;49;00m$
   485	[37m[39;49;00m$
   486	[37m[39;49;00m$
   487	[37m  [39;49;00m[37m# Is the given value NaN -- this one is interesting. NaN != NaN, and[39;49;00m[37m[39;49;00m$
   488	[37m  [39;49;00m[37m# isNaN(undefined) == true, so we make sure it's a number first.[39;49;00m[37m[39;49;00m$
   489	[37m  [39;49;00m[31m_.isNaN[39;49;00m:[37m        [39;49;00m[32m(obj) ->[39;49;00m[37m [39;49;00m_.isNumber(obj)[37m [39;49;00mand[37m [39;49;00m[36mwindow[39;49;00m.[36misNaN[39;49;00m(obj)[37m[39;49;00m$
   490	[37m[39;49;00m$
   491	[37m[39;49;00m$
   492	[37m  [39;49;00m[37m# Is a given value equal to null?[39;49;00m[37m[39;49;00m$
   493	[37m  [39;49;00m[31m_.isNull[39;49;00m:[37m       [39;49;00m[32m(obj) ->[39;49;00m[37m [39;49;00mobj[37m [39;49;00mis[37m [39;49;00m[34mnull[39;49;00m[37m[39;49;00m$
   494	[37m[39;49;00m$
   495	[37m[39;49;00m$
   496	[37m  [39;49;00m[37m# Is a given variable undefined?[39;49;00m[37m[39;49;00m$
   497	[37m  [39;49;00m[31m_.isUndefined[39;49;00m:[37m  [39;49;00m[32m(obj) ->[39;49;00m[37m [39;49;00m[34mtypeof[39;49;00m[37m [39;49;00mobj[37m [39;49;00mis[37m [39;49;00m[33m'[39;49;00m[33mundefined[39;49;00m[33m'[39;49;00m[37m[39;49;00m$
   498	[37m[39;49;00m$
   499	[37m[39;49;00m$
   500	[37m  [39;49;00m[37m# -------------------------- Utility Functions: --------------------------[39;49;00m[37m[39;49;00m$
   501	[37m[39;49;00m$
   502	[37m  [39;49;00m[37m# Run Underscore.js in noConflict mode, returning the '_' variable to its[39;49;00m[37m[39;49;00m$
   503	[37m  [39;49;00m[37m# previous owner. Returns a reference to the Underscore object.[39;49;00m[37m[39;49;00m$
   504	[37m  [39;49;00m[31m_.noConflict[39;49;00m:[37m [39;49;00m[32m->[39;49;00m[37m[39;49;00m$
   505	[37m    [39;49;00m[31mroot._[39;49;00m:[37m [39;49;00mpreviousUnderscore[37m[39;49;00m$
   506	[37m    [39;49;00m[34mthis[39;49;00m[37m[39;49;00m$
   507	[37m[39;49;00m$
   508	[37m[39;49;00m$
   509	[37m  [39;49;00m[37m# Keep the identity function around for default iterators.[39;49;00m[37m[39;49;00m$
   510	[37m  [39;49;00m[31m_.identity[39;49;00m:[37m [39;49;00m[32m(value) ->[39;49;00m[37m [39;49;00mvalue[37m[39;49;00m$
   511	[37m[39;49;00m$
   512	[37m[39;49;00m$
   513	[37m  [39;49;00m[37m# Break out of the middle of an iteration.[39;49;00m[37m[39;49;00m$
   514	[37m  [39;49;00m[31m_.breakLoop[39;49;00m:[37m [39;49;00m[32m->[39;49;00m[37m [39;49;00m[34mthrow[39;49;00m[37m [39;49;00mbreaker[37m[39;49;00m$
   515	[37m[39;49;00m$
   516	[37m[39;49;00m$
   517	[37m  [39;49;00m[37m# Generate a unique integer id (unique within the entire client session).[39;49;00m[37m[39;49;00m$
   518	[37m  [39;49;00m[37m# Useful for temporary DOM ids.[39;49;00m[37m[39;49;00m$
   519	[37m  [39;49;00m[31midCounter[39;49;00m:[37m [39;49;00m[34m0[39;49;00m[37m[39;49;00m$
   520	[37m  [39;49;00m[31m_.uniqueId[39;49;00m:[37m [39;49;00m[32m(prefix) ->[39;49;00m[37m[39;49;00m$
   521	[37m    [39;49;00m(prefix[37m [39;49;00mor[37m [39;49;00m[33m'[39;49;00m[33m'[39;49;00m)[37m [39;49;00m+[37m [39;49;00midCounter++[37m[39;49;00m$
   522	[37m[39;49;00m$
   523	[37m[39;49;00m$
   524	[37m  [39;49;00m[37m# By default, Underscore uses ERB-style template delimiters, change the[39;49;00m[37m[39;49;00m$
   525	[37m  [39;49;00m[37m# following template settings to use alternative delimiters.[39;49;00m[37m[39;49;00m$
   526	[37m  [39;49;00m[31m_.templateSettings[39;49;00m:[37m [39;49;00m{[37m[39;49;00m$
   527	[37m    [39;49;00m[31mstart[39;49;00m:[37m        [39;49;00m[33m'[39;49;00m[33m<%[39;49;00m[33m'[39;49;00m[37m[39;49;00m$
   528	[37m    [39;49;00m[31mend[39;49;00m:[37m          [39;49;00m[33m'[39;49;00m[33m%>[39;49;00m[33m'[39;49;00m[37m[39;49;00m$
   529	[37m    [39;49;00m[31minterpolate[39;49;00m:[37m  [39;49;00m[33m/<%=(.+?)%>/g[39;49;00m[37m[39;49;00m$
   530	[37m  [39;49;00m}[37m[39;49;00m$
   531	[37m[39;49;00m$
   532	[37m[39;49;00m$
   533	[37m  [39;49;00m[37m# JavaScript templating a-la ERB, pilfered from John Resig's[39;49;00m[37m[39;49;00m$
   534	[37m  [39;49;00m[37m# "Secrets of the JavaScript Ninja", page 83.[39;49;00m[37m[39;49;00m$
   535	[37m  [39;49;00m[37m# Single-quotea fix from Rick Strahl's version.[39;49;00m[37m[39;49;00m$
   536	[37m  [39;49;00m[31m_.template[39;49;00m:[37m [39;49;00m[32m(str, data) ->[39;49;00m[37m[39;49;00m$
   537	[37m    [39;49;00m[31mc[39;49;00m:[37m [39;49;00m_.templateSettings[37m[39;49;00m$
   538	[37m    [39;49;00m[31mfn[39;49;00m:[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00m[36mFunction[39;49;00m[37m [39;49;00m[33m'[39;49;00m[33mobj[39;49;00m[33m'[39;49;00m,[37m[39;49;00m$
   539	[37m      [39;49;00m[33m'[39;49;00m[33mvar p=[],print=function(){p.push.apply(p,arguments);};[39;49;00m[33m'[39;49;00m[37m [39;49;00m+[37m[39;49;00m$
   540	[37m      [39;49;00m[33m'[39;49;00m[33mwith(obj){p.push([39;49;00m[33m\'[39;49;00m[33m'[39;49;00m[37m [39;49;00m+[37m[39;49;00m$
   541	[37m      [39;49;00mstr.replace([33m/[\r\t\n]/g[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
   542	[37m         [39;49;00m.replace([34mnew[39;49;00m[37m [39;49;00m[36mRegExp[39;49;00m([33m"[39;49;00m[33m'[39;49;00m[33m(?=[^[39;49;00m[33m"[39;49;00m+c.end[[34m0[39;49;00m]+[33m"[39;49;00m[33m]*[39;49;00m[33m"[39;49;00m+c.end+[33m"[39;49;00m[33m)[39;49;00m[33m"[39;49;00m,[33m"[39;49;00m[33mg[39;49;00m[33m"[39;49;00m),[33m"[39;49;00m[33m\t[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
   543	[37m         [39;49;00m.split([33m"[39;49;00m[33m'[39;49;00m[33m"[39;49;00m).join([33m"[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
   544	[37m         [39;49;00m.split([33m"[39;49;00m[33m\t[39;49;00m[33m"[39;49;00m).join([33m"[39;49;00m[33m'[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
   545	[37m         [39;49;00m.replace(c.interpolate,[37m [39;49;00m[33m"[39;49;00m[33m'[39;49;00m[33m,$1,[39;49;00m[33m'[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
   546	[37m         [39;49;00m.split(c.start).join([33m"[39;49;00m[33m'[39;49;00m[33m);[39;49;00m[33m"[39;49;00m)[37m[39;49;00m$
   547	[37m         [39;49;00m.split(c.end).join([33m"[39;49;00m[33mp.push([39;49;00m[33m'[39;49;00m[33m"[39;49;00m)[37m [39;49;00m+[37m[39;49;00m$
   548	[37m         [39;49;00m[33m"[39;49;00m[33m'[39;49;00m[33m);}return p.join([39;49;00m[33m'[39;49;00m[33m'[39;49;00m[33m);[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   549	[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00mdata[37m [39;49;00m[34mthen[39;49;00m[37m [39;49;00mfn(data)[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00mfn[37m[39;49;00m$
   550	[37m[39;49;00m$
   551	[37m[39;49;00m$
   552	[37m  [39;49;00m[37m# ------------------------------- Aliases ----------------------------------[39;49;00m[37m[39;49;00m$
   553	[37m[39;49;00m$
   554	[37m  [39;49;00m[31m_.forEach[39;49;00m:[37m [39;49;00m_.each[37m[39;49;00m$
   555	[37m  [39;49;00m[31m_.foldl[39;49;00m:[37m   [39;49;00m[31m_.inject[39;49;00m:[37m      [39;49;00m_.reduce[37m[39;49;00m$
   556	[37m  [39;49;00m[31m_.foldr[39;49;00m:[37m   [39;49;00m_.reduceRight[37m[39;49;00m$
   557	[37m  [39;49;00m[31m_.filter[39;49;00m:[37m  [39;49;00m_.select[37m[39;49;00m$
   558	[37m  [39;49;00m[31m_.every[39;49;00m:[37m   [39;49;00m_.all[37m[39;49;00m$
   559	[37m  [39;49;00m[31m_.some[39;49;00m:[37m    [39;49;00m_.any[37m[39;49;00m$
   560	[37m  [39;49;00m[31m_.head[39;49;00m:[37m    [39;49;00m_.first[37m[39;49;00m$
   561	[37m  [39;49;00m[31m_.tail[39;49;00m:[37m    [39;49;00m_.rest[37m[39;49;00m$
   562	[37m  [39;49;00m[31m_.methods[39;49;00m:[37m [39;49;00m_.functions[37m[39;49;00m$
   563	[37m[39;49;00m$
   564	[37m[39;49;00m$
   565	[37m  [39;49;00m[37m#   /*------------------------ Setup the OOP Wrapper: --------------------------*/[39;49;00m[37m[39;49;00m$
   566	[37m[39;49;00m$
   567	[37m  [39;49;00m[37m# Helper function to continue chaining intermediate results.[39;49;00m[37m[39;49;00m$
   568	[37m  [39;49;00m[31mresult[39;49;00m:[37m [39;49;00m[32m(obj, chain) ->[39;49;00m[37m[39;49;00m$
   569	[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00mchain[37m [39;49;00m[34mthen[39;49;00m[37m [39;49;00m_(obj).chain()[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00mobj[37m[39;49;00m$
   570	[37m[39;49;00m$
   571	[37m[39;49;00m$
   572	[37m  [39;49;00m[37m# Add all of the Underscore functions to the wrapper object.[39;49;00m[37m[39;49;00m$
   573	[37m  [39;49;00m_.each[37m [39;49;00m_.functions(_),[37m [39;49;00m[32m(name) ->[39;49;00m[37m[39;49;00m$
   574	[37m    [39;49;00m[31mmethod[39;49;00m:[37m [39;49;00m_[name][37m[39;49;00m$
   575	[37m    [39;49;00mwrapper.prototype[name]:[37m [39;49;00m[32m->[39;49;00m[37m[39;49;00m$
   576	[37m      [39;49;00munshift.call(arguments,[37m [39;49;00m[34mthis[39;49;00m._wrapped)[37m[39;49;00m$
   577	[37m      [39;49;00mresult(method.apply(_,[37m [39;49;00marguments),[37m [39;49;00m[34mthis[39;49;00m._chain)[37m[39;49;00m$
   578	[37m[39;49;00m$
   579	[37m[39;49;00m$
   580	[37m  [39;49;00m[37m# Add all mutator Array functions to the wrapper.[39;49;00m[37m[39;49;00m$
   581	[37m  [39;49;00m_.each[37m [39;49;00m[[33m'[39;49;00m[33mpop[39;49;00m[33m'[39;49;00m,[37m [39;49;00m[33m'[39;49;00m[33mpush[39;49;00m[33m'[39;49;00m,[37m [39;49;00m[33m'[39;49;00m[33mreverse[39;49;00m[33m'[39;49;00m,[37m [39;49;00m[33m'[39;49;00m[33mshift[39;49;00m[33m'[39;49;00m,[37m [39;49;00m[33m'[39;49;00m[33msort[39;49;00m[33m'[39;49;00m,[37m [39;49;00m[33m'[39;49;00m[33msplice[39;49;00m[33m'[39;49;00m,[37m [39;49;00m[33m'[39;49;00m[33munshift[39;49;00m[33m'[39;49;00m],[37m [39;49;00m[32m(name) ->[39;49;00m[37m[39;49;00m$
   582	[37m    [39;49;00m[31mmethod[39;49;00m:[37m [39;49;00m[36mArray[39;49;00m.prototype[name][37m[39;49;00m$
   583	[37m    [39;49;00mwrapper.prototype[name]:[37m [39;49;00m[32m->[39;49;00m[37m[39;49;00m$
   584	[37m      [39;49;00mmethod.apply([34mthis[39;49;00m._wrapped,[37m [39;49;00marguments)[37m[39;49;00m$
   585	[37m      [39;49;00mresult([34mthis[39;49;00m._wrapped,[37m [39;49;00m[34mthis[39;49;00m._chain)[37m[39;49;00m$
   586	[37m[39;49;00m$
   587	[37m[39;49;00m$
   588	[37m  [39;49;00m[37m# Add all accessor Array functions to the wrapper.[39;49;00m[37m[39;49;00m$
   589	[37m  [39;49;00m_.each[37m [39;49;00m[[33m'[39;49;00m[33mconcat[39;49;00m[33m'[39;49;00m,[37m [39;49;00m[33m'[39;49;00m[33mjoin[39;49;00m[33m'[39;49;00m,[37m [39;49;00m[33m'[39;49;00m[33mslice[39;49;00m[33m'[39;49;00m],[37m [39;49;00m[32m(name) ->[39;49;00m[37m[39;49;00m$
   590	[37m    [39;49;00m[31mmethod[39;49;00m:[37m [39;49;00m[36mArray[39;49;00m.prototype[name][37m[39;49;00m$
   591	[37m    [39;49;00mwrapper.prototype[name]:[37m [39;49;00m[32m->[39;49;00m[37m[39;49;00m$
   592	[37m      [39;49;00mresult(method.apply([34mthis[39;49;00m._wrapped,[37m [39;49;00marguments),[37m [39;49;00m[34mthis[39;49;00m._chain)[37m[39;49;00m$
   593	[37m[39;49;00m$
   594	[37m[39;49;00m$
   595	[37m  [39;49;00m[37m# Start chaining a wrapped Underscore object.[39;49;00m[37m[39;49;00m$
   596	[37m  [39;49;00m[31mwrapper::chain[39;49;00m:[37m [39;49;00m[32m->[39;49;00m[37m[39;49;00m$
   597	[37m    [39;49;00m[34mthis[39;49;00m.[31m_chain[39;49;00m:[37m [39;49;00m[34mtrue[39;49;00m[37m[39;49;00m$
   598	[37m    [39;49;00m[34mthis[39;49;00m[37m[39;49;00m$
   599	[37m[39;49;00m$
   600	[37m[39;49;00m$
   601	[37m  [39;49;00m[37m# Extracts the result from a wrapped and chained object.[39;49;00m[37m[39;49;00m$
   602	[37m  [39;49;00m[31mwrapper::value[39;49;00m:[37m [39;49;00m[32m->[39;49;00m[37m [39;49;00m[34mthis[39;49;00m._wrapped$

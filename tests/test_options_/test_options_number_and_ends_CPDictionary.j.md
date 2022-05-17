     1	[37m/*[39;49;00m$
     2	[37m * CPDictionary.j[39;49;00m$
     3	[37m * Foundation[39;49;00m$
     4	[37m *[39;49;00m$
     5	[37m * Created by Francisco Tolmasky.[39;49;00m$
     6	[37m * Copyright 2008, 280 North, Inc.[39;49;00m$
     7	[37m *[39;49;00m$
     8	[37m * This library is free software; you can redistribute it and/or[39;49;00m$
     9	[37m * modify it under the terms of the GNU Lesser General Public[39;49;00m$
    10	[37m * License as published by the Free Software Foundation; either[39;49;00m$
    11	[37m * version 2.1 of the License, or (at your option) any later version.[39;49;00m$
    12	[37m *[39;49;00m$
    13	[37m * This library is distributed in the hope that it will be useful,[39;49;00m$
    14	[37m * but WITHOUT ANY WARRANTY; without even the implied warranty of[39;49;00m$
    15	[37m * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU[39;49;00m$
    16	[37m * Lesser General Public License for more details.[39;49;00m$
    17	[37m *[39;49;00m$
    18	[37m * You should have received a copy of the GNU Lesser General Public[39;49;00m$
    19	[37m * License along with this library; if not, write to the Free Software[39;49;00m$
    20	[37m * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA[39;49;00m$
    21	[37m */[39;49;00m[37m[39;49;00m$
    22	[37m[39;49;00m$
    23	[37m//@import "CPRange.j"[39;49;00m$
    24	[36m@import[39;49;00m[37m [39;49;00m[33m"CPObject.j"[39;49;00m[37m[39;49;00m$
    25	[36m@import[39;49;00m[37m [39;49;00m[33m"CPEnumerator.j"[39;49;00m[37m[39;49;00m$
    26	[36m@import[39;49;00m[37m [39;49;00m[33m"CPException.j"[39;49;00m[37m[39;49;00m$
    27	[37m[39;49;00m$
    28	[37m/* @ignore */[39;49;00m[37m[39;49;00m$
    29	[34m@implementation[39;49;00m[37m [39;49;00m[04m[32m_CPDictionaryValueEnumerator[39;49;00m[37m [39;49;00m:[37m [39;49;00m[04m[32mCPEnumerator[39;49;00m[37m[39;49;00m$
    30	{[37m[39;49;00m$
    31	[37m    [39;49;00mCPEnumerator[37m    [39;49;00m_keyEnumerator;[37m[39;49;00m$
    32	[37m    [39;49;00mCPDictionary[37m    [39;49;00m_dictionary;[37m[39;49;00m$
    33	}[37m[39;49;00m$
    34	[37m[39;49;00m$
    35	-[37m [39;49;00m([36mid[39;49;00m)[32minitWithDictionary:[39;49;00m([36mCPDictionary[39;49;00m)aDictionary[37m[39;49;00m$
    36	{[37m[39;49;00m$
    37	[37m    [39;49;00m[36mself[39;49;00m[37m [39;49;00m=[37m [39;49;00m[[36msuper[39;49;00m[37m [39;49;00minit];[37m[39;49;00m$
    38	[37m    [39;49;00m$
    39	[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m([36mself[39;49;00m)[37m[39;49;00m$
    40	[37m    [39;49;00m{[37m[39;49;00m$
    41	[37m        [39;49;00m_keyEnumerator[37m [39;49;00m=[37m [39;49;00m[aDictionary[37m [39;49;00mkeyEnumerator];[37m[39;49;00m$
    42	[37m        [39;49;00m_dictionary[37m [39;49;00m=[37m [39;49;00maDictionary;[37m[39;49;00m$
    43	[37m    [39;49;00m}[37m[39;49;00m$
    44	[37m    [39;49;00m$
    45	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[36mself[39;49;00m;[37m[39;49;00m$
    46	}[37m[39;49;00m$
    47	[37m[39;49;00m$
    48	-[37m [39;49;00m([36mid[39;49;00m)[32mnextObject[39;49;00m[37m[39;49;00m$
    49	{[37m[39;49;00m$
    50	[37m    [39;49;00m[34mvar[39;49;00m[37m [39;49;00mkey[37m [39;49;00m=[37m [39;49;00m[_keyEnumerator[37m [39;49;00mnextObject];[37m[39;49;00m$
    51	[37m    [39;49;00m$
    52	[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!key)[37m[39;49;00m$
    53	[37m        [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mnil[39;49;00m;[37m[39;49;00m$
    54	[37m[39;49;00m$
    55	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[_dictionary[37m [39;49;00mobjectForKey:key];[37m[39;49;00m$
    56	}[37m[39;49;00m$
    57	[37m[39;49;00m$
    58	[34m@end[39;49;00m[37m[39;49;00m$
    59	[37m[39;49;00m$
    60	[37m/*! [39;49;00m$
    61	[37m    @class CPDictionary[39;49;00m$
    62	[37m    @ingroup foundation[39;49;00m$
    63	[37m    @brief A mutable key-value pair collection.[39;49;00m$
    64	[37m[39;49;00m$
    65	[37m    A dictionary is the standard way of passing around key-value pairs in[39;49;00m$
    66	[37m    the Cappuccino framework. It is similar to the[39;49;00m$
    67	[37m    <a href="http://java.sun.com/javase/6/docs/api/index.html">Java map interface</a>,[39;49;00m$
    68	[37m    except all keys are CPStrings and values can be any[39;49;00m$
    69	[37m    Cappuccino or JavaScript object.[39;49;00m$
    70	[37m[39;49;00m$
    71	[37m    If you are familiar with dictionaries in Cocoa, you'll notice that[39;49;00m$
    72	[37m    there is no CPMutableDictionary class. The regular CPDictionary[39;49;00m$
    73	[37m    has \c -setObject:forKey: and \c -removeObjectForKey: methods.[39;49;00m$
    74	[37m    In Cappuccino there is no distinction between immutable and mutable classes.[39;49;00m$
    75	[37m    They are all mutable.[39;49;00m$
    76	[37m*/[39;49;00m[37m[39;49;00m$
    77	[34m@implementation[39;49;00m[37m [39;49;00m[04m[32mCPDictionary[39;49;00m[37m [39;49;00m:[37m [39;49;00m[04m[32mCPObject[39;49;00m[37m[39;49;00m$
    78	{[37m[39;49;00m$
    79	}[37m[39;49;00m$
    80	[37m[39;49;00m$
    81	[37m/*[39;49;00m$
    82	[37m    @ignore[39;49;00m$
    83	[37m*/[39;49;00m[37m[39;49;00m$
    84	+[37m [39;49;00m([36mid[39;49;00m)[32malloc[39;49;00m[37m[39;49;00m$
    85	{[37m[39;49;00m$
    86	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00m[32mobjj_dictionary[39;49;00m();[37m[39;49;00m$
    87	}[37m[39;49;00m$
    88	[37m[39;49;00m$
    89	[37m/*![39;49;00m$
    90	[37m    Returns a new empty CPDictionary.[39;49;00m$
    91	[37m*/[39;49;00m[37m[39;49;00m$
    92	+[37m [39;49;00m([36mid[39;49;00m)[32mdictionary[39;49;00m[37m[39;49;00m$
    93	{[37m[39;49;00m$
    94	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[[[36mself[39;49;00m[37m [39;49;00malloc][37m [39;49;00minit];[37m[39;49;00m$
    95	}[37m[39;49;00m$
    96	[37m[39;49;00m$
    97	[37m/*![39;49;00m$
    98	[37m    Returns a new dictionary, initialized with the contents of \c aDictionary.[39;49;00m$
    99	[37m    @param aDictionary the dictionary to copy key-value pairs from[39;49;00m$
   100	[37m    @return the new CPDictionary[39;49;00m$
   101	[37m*/[39;49;00m[37m[39;49;00m$
   102	+[37m [39;49;00m([36mid[39;49;00m)[32mdictionaryWithDictionary:[39;49;00m([36mCPDictionary[39;49;00m)aDictionary[37m[39;49;00m$
   103	{[37m[39;49;00m$
   104	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[[[36mself[39;49;00m[37m [39;49;00malloc][37m [39;49;00minitWithDictionary:aDictionary];[37m[39;49;00m$
   105	}[37m[39;49;00m$
   106	[37m[39;49;00m$
   107	[37m/*![39;49;00m$
   108	[37m    Creates a new dictionary with single key-value pair.[39;49;00m$
   109	[37m    @param anObject the object for the paring[39;49;00m$
   110	[37m    @param aKey the key for the pairing[39;49;00m$
   111	[37m    @return the new CPDictionary[39;49;00m$
   112	[37m*/[39;49;00m[37m[39;49;00m$
   113	+[37m [39;49;00m([36mid[39;49;00m)[32mdictionaryWithObject:[39;49;00m([36mid[39;49;00m)anObject[37m [39;49;00m[32mforKey:[39;49;00m([36mid[39;49;00m)aKey[37m[39;49;00m$
   114	{[37m[39;49;00m$
   115	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[[[36mself[39;49;00m[37m [39;49;00malloc][37m [39;49;00minitWithObjects:[anObject][37m [39;49;00mforKeys:[aKey]];[37m[39;49;00m$
   116	}[37m[39;49;00m$
   117	[37m[39;49;00m$
   118	[37m/*![39;49;00m$
   119	[37m    Creates a dictionary with multiple key-value pairs.[39;49;00m$
   120	[37m    @param objects the objects to place in the dictionary[39;49;00m$
   121	[37m    @param keys the keys for each of the objects[39;49;00m$
   122	[37m    @throws CPInvalidArgumentException if the number of objects and keys is different[39;49;00m$
   123	[37m    @return the new CPDictionary[39;49;00m$
   124	[37m*/[39;49;00m[37m[39;49;00m$
   125	+[37m [39;49;00m([36mid[39;49;00m)[32mdictionaryWithObjects:[39;49;00m([36mCPArray[39;49;00m)objects[37m [39;49;00m[32mforKeys:[39;49;00m([36mCPArray[39;49;00m)keys[37m[39;49;00m$
   126	{[37m[39;49;00m$
   127	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[[[36mself[39;49;00m[37m [39;49;00malloc][37m [39;49;00minitWithObjects:objects[37m [39;49;00mforKeys:keys];[37m[39;49;00m$
   128	}[37m[39;49;00m$
   129	[37m[39;49;00m$
   130	[37m/*![39;49;00m$
   131	[37m    Creates a dictionary with multiple key-value pairs.[39;49;00m$
   132	[37m    @param JavaScript object[39;49;00m$
   133	[37m    @return the new CPDictionary[39;49;00m$
   134	[37m*/[39;49;00m[37m[39;49;00m$
   135	+[37m [39;49;00m([36mid[39;49;00m)[32mdictionaryWithJSObject:[39;49;00m([36mJSObject[39;49;00m)object[37m[39;49;00m$
   136	{[37m[39;49;00m$
   137	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[[36mself[39;49;00m[37m [39;49;00mdictionaryWithJSObject:object[37m [39;49;00mrecursively:[34mNO[39;49;00m];[37m[39;49;00m$
   138	}[37m[39;49;00m$
   139	[37m[39;49;00m$
   140	[37m/*![39;49;00m$
   141	[37m    Creates a dictionary with multiple key-value pairs, recursively.[39;49;00m$
   142	[37m    @param JavaScript object[39;49;00m$
   143	[37m    @return the new CPDictionary[39;49;00m$
   144	[37m*/[39;49;00m[37m[39;49;00m$
   145	+[37m [39;49;00m([36mid[39;49;00m)[32mdictionaryWithJSObject:[39;49;00m([36mJSObject[39;49;00m)object[37m [39;49;00m[32mrecursively:[39;49;00m([36mBOOL[39;49;00m)recursively[37m[39;49;00m$
   146	{[37m[39;49;00m$
   147	[37m    [39;49;00m[34mvar[39;49;00m[37m [39;49;00mdictionary[37m [39;49;00m=[37m [39;49;00m[[[36mself[39;49;00m[37m [39;49;00malloc][37m [39;49;00minit];[37m[39;49;00m$
   148	[37m        [39;49;00m$
   149	[37m    [39;49;00m[34mfor[39;49;00m[37m [39;49;00m([34mvar[39;49;00m[37m [39;49;00mkey[37m [39;49;00m[34min[39;49;00m[37m [39;49;00mobject)[37m[39;49;00m$
   150	[37m    [39;49;00m{[37m[39;49;00m$
   151	[37m        [39;49;00m[34mvar[39;49;00m[37m [39;49;00mvalue[37m [39;49;00m=[37m [39;49;00mobject[key];[37m[39;49;00m$
   152	[37m    [39;49;00m$
   153	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(recursively[37m [39;49;00m&&[37m [39;49;00mvalue.constructor[37m [39;49;00m===[37m [39;49;00m[36mObject[39;49;00m)[37m[39;49;00m$
   154	[37m            [39;49;00mvalue[37m [39;49;00m=[37m [39;49;00m[CPDictionary[37m [39;49;00mdictionaryWithJSObject:value[37m [39;49;00mrecursively:[34mYES[39;49;00m];[37m[39;49;00m$
   155	[37m    [39;49;00m$
   156	[37m        [39;49;00m[dictionary[37m [39;49;00msetObject:value[37m [39;49;00mforKey:key];[37m[39;49;00m$
   157	[37m    [39;49;00m}[37m[39;49;00m$
   158	[37m    [39;49;00m$
   159	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mdictionary;[37m[39;49;00m$
   160	}[37m[39;49;00m$
   161	[37m[39;49;00m$
   162	[37m/*![39;49;00m$
   163	[37m    Creates and returns a dictionary constructed by a given pairs of keys and values.[39;49;00m$
   164	[37m    @param firstObject first object value[39;49;00m$
   165	[37m    @param ... key for the first object and ongoing value-key pairs for more objects.[39;49;00m$
   166	[37m    @throws CPInvalidArgumentException if the number of objects and keys is different[39;49;00m$
   167	[37m    @return the new CPDictionary[39;49;00m$
   168	[37m    [39;49;00m$
   169	[37m    Assuming that there's no object retaining in Cappuccino, you can create[39;49;00m$
   170	[37m    dictionaries same way as with alloc and initWithObjectsAndKeys:[39;49;00m$
   171	[37m    var dict = [CPDictionary dictionaryWithObjectsAndKeys:[39;49;00m$
   172	[37m    @"value1", @"key1",[39;49;00m$
   173	[37m    @"value2", @"key2"];[39;49;00m$
   174	[37m    [39;49;00m$
   175	[37m    Note, that there's no final nil like in Objective-C/Cocoa.[39;49;00m$
   176	[37m    [39;49;00m$
   177	[37m    @see [CPDictionary initWithObjectsAndKeys:][39;49;00m$
   178	[37m*/[39;49;00m[37m[39;49;00m$
   179	+[37m [39;49;00m([36mid[39;49;00m)[32mdictionaryWithObjectsAndKeys:[39;49;00m([36mid[39;49;00m)firstObject,[37m [39;49;00m...[37m[39;49;00m$
   180	{[37m[39;49;00m$
   181	[37m    [39;49;00marguments[[34m0[39;49;00m][37m [39;49;00m=[37m [39;49;00m[[36mself[39;49;00m[37m [39;49;00malloc];[37m[39;49;00m$
   182	[37m    [39;49;00marguments[[34m1[39;49;00m][37m [39;49;00m=[37m [39;49;00m[34m@selector[39;49;00m(initWithObjectsAndKeys:);[37m[39;49;00m$
   183	[37m    [39;49;00m$
   184	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mobjj_msgSend.[32mapply[39;49;00m([36mthis[39;49;00m,[37m [39;49;00marguments);[37m[39;49;00m$
   185	}[37m[39;49;00m$
   186	[37m[39;49;00m$
   187	[37m/*![39;49;00m$
   188	[37m    Initializes the dictionary with the contents of another dictionary.[39;49;00m$
   189	[37m    @param aDictionary the dictionary to copy key-value pairs from[39;49;00m$
   190	[37m    @return the initialized dictionary[39;49;00m$
   191	[37m*/[39;49;00m[37m[39;49;00m$
   192	-[37m [39;49;00m([36mid[39;49;00m)[32minitWithDictionary:[39;49;00m([36mCPDictionary[39;49;00m)aDictionary[37m[39;49;00m$
   193	{[37m[39;49;00m$
   194	[37m    [39;49;00m[34mvar[39;49;00m[37m [39;49;00mkey[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33m"[39;49;00m,[37m[39;49;00m$
   195	[37m        [39;49;00mdictionary[37m [39;49;00m=[37m [39;49;00m[[CPDictionary[37m [39;49;00malloc][37m [39;49;00minit];[37m[39;49;00m$
   196	[37m    [39;49;00m$
   197	[37m    [39;49;00m[34mfor[39;49;00m[37m [39;49;00m(key[37m [39;49;00m[34min[39;49;00m[37m [39;49;00maDictionary._buckets)[37m[39;49;00m$
   198	[37m        [39;49;00m[dictionary[37m [39;49;00msetObject:[aDictionary[37m [39;49;00mobjectForKey:key][37m [39;49;00mforKey:key];[37m[39;49;00m$
   199	[37m        [39;49;00m$
   200	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mdictionary;[37m[39;49;00m$
   201	}[37m[39;49;00m$
   202	[37m[39;49;00m$
   203	[37m/*![39;49;00m$
   204	[37m    Initializes the dictionary from the arrays of keys and objects.[39;49;00m$
   205	[37m    @param objects the objects to put in the dictionary[39;49;00m$
   206	[37m    @param keyArray the keys for the objects to put in the dictionary[39;49;00m$
   207	[37m    @throws CPInvalidArgumentException if the number of objects and keys is different[39;49;00m$
   208	[37m    @return the initialized dictionary[39;49;00m$
   209	[37m*/[39;49;00m[37m[39;49;00m$
   210	-[37m [39;49;00m([36mid[39;49;00m)[32minitWithObjects:[39;49;00m([36mCPArray[39;49;00m)objects[37m [39;49;00m[32mforKeys:[39;49;00m([36mCPArray[39;49;00m)keyArray[37m[39;49;00m$
   211	{[37m[39;49;00m$
   212	[37m    [39;49;00m[36mself[39;49;00m[37m [39;49;00m=[37m [39;49;00m[[36msuper[39;49;00m[37m [39;49;00minit];[37m[39;49;00m$
   213	[37m[39;49;00m$
   214	[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m([objects[37m [39;49;00mcount][37m [39;49;00m!=[37m [39;49;00m[keyArray[37m [39;49;00mcount])[37m[39;49;00m$
   215	[37m        [39;49;00m[CPException[37m [39;49;00mraise:CPInvalidArgumentException[37m [39;49;00mreason:[33m"[39;49;00m[33mCounts are different.([39;49;00m[33m"[39;49;00m+[objects[37m [39;49;00mcount]+[33m"[39;49;00m[33m!=[39;49;00m[33m"[39;49;00m+[keyArray[37m [39;49;00mcount]+[33m"[39;49;00m[33m)[39;49;00m[33m"[39;49;00m];[37m[39;49;00m$
   216	[37m[39;49;00m$
   217	[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m([36mself[39;49;00m)[37m[39;49;00m$
   218	[37m    [39;49;00m{[37m[39;49;00m$
   219	[37m        [39;49;00m[34mvar[39;49;00m[37m [39;49;00mi[37m [39;49;00m=[37m [39;49;00m[keyArray[37m [39;49;00mcount];[37m[39;49;00m$
   220	[37m        [39;49;00m$
   221	[37m        [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(i--)[37m[39;49;00m$
   222	[37m            [39;49;00m[[36mself[39;49;00m[37m [39;49;00msetObject:objects[i][37m [39;49;00mforKey:keyArray[i]];[37m[39;49;00m$
   223	[37m    [39;49;00m}[37m[39;49;00m$
   224	[37m    [39;49;00m$
   225	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[36mself[39;49;00m;[37m[39;49;00m$
   226	}[37m[39;49;00m$
   227	[37m[39;49;00m$
   228	[37m/*![39;49;00m$
   229	[37m    Creates and returns a dictionary constructed by a given pairs of keys and values.[39;49;00m$
   230	[37m    @param firstObject first object value[39;49;00m$
   231	[37m    @param ... key for the first object and ongoing value-key pairs for more objects.[39;49;00m$
   232	[37m    @throws CPInvalidArgumentException if the number of objects and keys is different[39;49;00m$
   233	[37m    @return the new CPDictionary[39;49;00m$
   234	[37m    [39;49;00m$
   235	[37m    You can create dictionaries this way:[39;49;00m$
   236	[37m    var dict = [[CPDictionary alloc] initWithObjectsAndKeys:[39;49;00m$
   237	[37m    @"value1", @"key1",[39;49;00m$
   238	[37m    @"value2", @"key2"];[39;49;00m$
   239	[37m    [39;49;00m$
   240	[37m    Note, that there's no final nil like in Objective-C/Cocoa.[39;49;00m$
   241	[37m*/[39;49;00m[37m[39;49;00m$
   242	-[37m [39;49;00m([36mid[39;49;00m)[32minitWithObjectsAndKeys:[39;49;00m([36mid[39;49;00m)firstObject,[37m [39;49;00m...[37m[39;49;00m$
   243	{[37m[39;49;00m$
   244	[37m    [39;49;00m[34mvar[39;49;00m[37m [39;49;00margCount[37m [39;49;00m=[37m [39;49;00marguments.length;[37m[39;49;00m$
   245	[37m    [39;49;00m$
   246	[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(argCount[37m [39;49;00m%[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m!==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
   247	[37m        [39;49;00m[CPException[37m [39;49;00mraise:CPInvalidArgumentException[37m [39;49;00mreason:[33m"[39;49;00m[33mKey-value count is mismatched. ([39;49;00m[33m"[39;49;00m[37m [39;49;00m+[37m [39;49;00margCount[37m [39;49;00m+[37m [39;49;00m[33m"[39;49;00m[33m arguments passed)[39;49;00m[33m"[39;49;00m];[37m[39;49;00m$
   248	[37m[39;49;00m$
   249	[37m    [39;49;00m[36mself[39;49;00m[37m [39;49;00m=[37m [39;49;00m[[36msuper[39;49;00m[37m [39;49;00minit];[37m[39;49;00m$
   250	[37m    [39;49;00m$
   251	[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m([36mself[39;49;00m)[37m[39;49;00m$
   252	[37m    [39;49;00m{[37m[39;49;00m$
   253	[37m        [39;49;00m[37m// The arguments array contains self and _cmd, so the first object is at position 2.[39;49;00m$
   254	[37m        [39;49;00m[34mvar[39;49;00m[37m [39;49;00mindex[37m [39;49;00m=[37m [39;49;00m[34m2[39;49;00m;[37m[39;49;00m$
   255	[37m        [39;49;00m$
   256	[37m        [39;49;00m[34mfor[39;49;00m(;[37m [39;49;00mindex[37m [39;49;00m<[37m [39;49;00margCount;[37m [39;49;00mindex[37m [39;49;00m+=[37m [39;49;00m[34m2[39;49;00m)[37m[39;49;00m$
   257	[37m        [39;49;00m{[37m[39;49;00m$
   258	[37m            [39;49;00m[34mvar[39;49;00m[37m [39;49;00mvalue[37m [39;49;00m=[37m [39;49;00marguments[index];[37m[39;49;00m$
   259	[37m[39;49;00m$
   260	[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(value[37m [39;49;00m===[37m [39;49;00m[34mnil[39;49;00m)[37m[39;49;00m$
   261	[37m                [39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
   262	[37m[39;49;00m$
   263	[37m            [39;49;00m[[36mself[39;49;00m[37m [39;49;00msetObject:value[37m [39;49;00mforKey:arguments[index[37m [39;49;00m+[37m [39;49;00m[34m1[39;49;00m]];[37m[39;49;00m$
   264	[37m        [39;49;00m}[37m[39;49;00m$
   265	[37m    [39;49;00m}[37m[39;49;00m$
   266	[37m[39;49;00m$
   267	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[36mself[39;49;00m;[37m[39;49;00m$
   268	}[37m[39;49;00m$
   269	[37m[39;49;00m$
   270	[37m/*![39;49;00m$
   271	[37m    return a copy of the receiver (does not deep copy the objects contained in the dictionary).[39;49;00m$
   272	[37m*/[39;49;00m[37m[39;49;00m$
   273	-[37m [39;49;00m([36mCPDictionary[39;49;00m)[32mcopy[39;49;00m[37m[39;49;00m$
   274	{[37m[39;49;00m$
   275	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[CPDictionary[37m [39;49;00mdictionaryWithDictionary:[36mself[39;49;00m];[37m[39;49;00m$
   276	}[37m[39;49;00m$
   277	[37m[39;49;00m$
   278	[37m/*![39;49;00m$
   279	[37m    Returns the number of entries in the dictionary[39;49;00m$
   280	[37m*/[39;49;00m[37m[39;49;00m$
   281	-[37m [39;49;00m([36mint[39;49;00m)[32mcount[39;49;00m[37m[39;49;00m$
   282	{[37m[39;49;00m$
   283	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mcount;[37m[39;49;00m$
   284	}[37m[39;49;00m$
   285	[37m[39;49;00m$
   286	[37m/*![39;49;00m$
   287	[37m    Returns an array of keys for all the entries in the dictionary.[39;49;00m$
   288	[37m*/[39;49;00m[37m[39;49;00m$
   289	-[37m [39;49;00m([36mCPArray[39;49;00m)[32mallKeys[39;49;00m[37m[39;49;00m$
   290	{[37m[39;49;00m$
   291	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m_keys;[37m[39;49;00m$
   292	}[37m[39;49;00m$
   293	[37m[39;49;00m$
   294	[37m/*![39;49;00m$
   295	[37m    Returns an array of values for all the entries in the dictionary.[39;49;00m$
   296	[37m*/[39;49;00m[37m[39;49;00m$
   297	-[37m [39;49;00m([36mCPArray[39;49;00m)[32mallValues[39;49;00m[37m[39;49;00m$
   298	{[37m[39;49;00m$
   299	[37m    [39;49;00m[34mvar[39;49;00m[37m [39;49;00mindex[37m [39;49;00m=[37m [39;49;00m_keys.length,[37m[39;49;00m$
   300	[37m        [39;49;00mvalues[37m [39;49;00m=[37m [39;49;00m[];[37m[39;49;00m$
   301	[37m        [39;49;00m$
   302	[37m    [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(index--)[37m[39;49;00m$
   303	[37m        [39;49;00mvalues.[32mpush[39;49;00m([32mdictionary_getValue[39;49;00m([36mself[39;49;00m,[37m [39;49;00m[_keys[index]]));[37m[39;49;00m$
   304	[37m[39;49;00m$
   305	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mvalues;[37m[39;49;00m$
   306	}[37m[39;49;00m$
   307	[37m[39;49;00m$
   308	[37m/*![39;49;00m$
   309	[37m    Returns an enumerator that enumerates over all the dictionary's keys.[39;49;00m$
   310	[37m*/[39;49;00m[37m[39;49;00m$
   311	-[37m [39;49;00m([36mCPEnumerator[39;49;00m)[32mkeyEnumerator[39;49;00m[37m[39;49;00m$
   312	{[37m[39;49;00m$
   313	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[_keys[37m [39;49;00mobjectEnumerator];[37m[39;49;00m$
   314	}[37m[39;49;00m$
   315	[37m[39;49;00m$
   316	[37m/*![39;49;00m$
   317	[37m    Returns an enumerator that enumerates over all the dictionary's values.[39;49;00m$
   318	[37m*/[39;49;00m[37m[39;49;00m$
   319	-[37m [39;49;00m([36mCPEnumerator[39;49;00m)[32mobjectEnumerator[39;49;00m[37m[39;49;00m$
   320	{[37m[39;49;00m$
   321	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[[_CPDictionaryValueEnumerator[37m [39;49;00malloc][37m [39;49;00minitWithDictionary:[36mself[39;49;00m];[37m[39;49;00m$
   322	}[37m[39;49;00m$
   323	[37m[39;49;00m$
   324	[37m/*![39;49;00m$
   325	[37m    Compare the receiver to this dictionary, and return whether or not they are equal. [39;49;00m$
   326	[37m*/[39;49;00m[37m[39;49;00m$
   327	-[37m [39;49;00m([36mBOOL[39;49;00m)[32misEqualToDictionary:[39;49;00m([36mCPDictionary[39;49;00m)aDictionary[37m[39;49;00m$
   328	{[37m[39;49;00m$
   329	[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(count[37m [39;49;00m!==[37m [39;49;00m[aDictionary[37m [39;49;00mcount])[37m[39;49;00m$
   330	[37m        [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mNO[39;49;00m;[37m[39;49;00m$
   331	[37m[39;49;00m$
   332	[37m    [39;49;00m[34mvar[39;49;00m[37m [39;49;00mindex[37m [39;49;00m=[37m [39;49;00mcount;[37m[39;49;00m$
   333	[37m    [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(index--)[37m[39;49;00m$
   334	[37m    [39;49;00m{[37m[39;49;00m$
   335	[37m        [39;49;00m[34mvar[39;49;00m[37m [39;49;00mcurrentKey[37m [39;49;00m=[37m [39;49;00m_keys[index],[37m[39;49;00m$
   336	[37m            [39;49;00mlhsObject[37m [39;49;00m=[37m [39;49;00m_buckets[currentKey],[37m[39;49;00m$
   337	[37m            [39;49;00mrhsObject[37m [39;49;00m=[37m [39;49;00maDictionary._buckets[currentKey];[37m[39;49;00m$
   338	[37m[39;49;00m$
   339	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(lhsObject[37m [39;49;00m===[37m [39;49;00mrhsObject)[37m[39;49;00m$
   340	[37m            [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
   341	[37m            [39;49;00m$
   342	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(lhsObject.isa[37m [39;49;00m&&[37m [39;49;00mrhsObject.isa[37m [39;49;00m&&[37m [39;49;00m[lhsObject[37m [39;49;00mrespondsToSelector:[34m@selector[39;49;00m(isEqual:)][37m [39;49;00m&&[37m [39;49;00m[lhsObject[37m [39;49;00misEqual:rhsObject])[37m[39;49;00m$
   343	[37m            [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
   344	[37m        [39;49;00m$
   345	[37m        [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mNO[39;49;00m;[37m[39;49;00m$
   346	[37m    [39;49;00m}[37m[39;49;00m$
   347	[37m[39;49;00m$
   348	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mYES[39;49;00m;[37m[39;49;00m$
   349	}[37m[39;49;00m$
   350	[37m[39;49;00m$
   351	[37m/*[39;49;00m$
   352	[37m    Instance.isEqualToDictionary(aDictionary)[39;49;00m$
   353	[37m    {[39;49;00m$
   354	[37m        if(this.count()!=aDictionary.count()) return NO;[39;49;00m$
   355	[37m        [39;49;00m$
   356	[37m        var i= this._keys.count();[39;49;00m$
   357	[37m        while(i--) if(this.objectForKey(this._keys[i])!=aDictionary.objectForKey(this._keys[i])) return NO;[39;49;00m$
   358	[37m        [39;49;00m$
   359	[37m        return YES;[39;49;00m$
   360	[37m    }[39;49;00m$
   361	[37m    [39;49;00m$
   362	[37m    Instance.allKeys()[39;49;00m$
   363	[37m    {[39;49;00m$
   364	[37m        return this._keys;[39;49;00m$
   365	[37m    }[39;49;00m$
   366	[37m    [39;49;00m$
   367	[37m    Instance.allKeysForObject(anObject)[39;49;00m$
   368	[37m    {[39;49;00m$
   369	[37m        var i= 0,[39;49;00m$
   370	[37m            keys= CPArray.array(),[39;49;00m$
   371	[37m            count= this.count();[39;49;00m$
   372	[37m        [39;49;00m$
   373	[37m        while((i= this._objects.indexOfObjectInRage(0, count-i))!=CPNotFound) keys.addObject(this._keys[i]);[39;49;00m$
   374	[37m        [39;49;00m$
   375	[37m        return keys;[39;49;00m$
   376	[37m    }[39;49;00m$
   377	[37m    [39;49;00m$
   378	[37m    Instance.allValues()[39;49;00m$
   379	[37m    {[39;49;00m$
   380	[37m        return this._objects;[39;49;00m$
   381	[37m    }[39;49;00m$
   382	[37m    [39;49;00m$
   383	[37m    Instance.keyEnumerator()[39;49;00m$
   384	[37m    {[39;49;00m$
   385	[37m        return this._keys.objectEnumerator();[39;49;00m$
   386	[37m    }[39;49;00m$
   387	[37m    [39;49;00m$
   388	[37m    Instance.keysSortedByValueUsingSelector(aSelector)[39;49;00m$
   389	[37m    {[39;49;00m$
   390	[37m        var dictionary= this,[39;49;00m$
   391	[37m            objectSelector= function(rhs)[39;49;00m$
   392	[37m            {[39;49;00m$
   393	[37m                return aSelector.apply(dictionary.objectForKey(this), [dictionary.objectForKey(rhs)]);[39;49;00m$
   394	[37m            };[39;49;00m$
   395	[37m        [39;49;00m$
   396	[37m        return this._keys.sortedArrayUsingSelector(objectSelector);[39;49;00m$
   397	[37m    }[39;49;00m$
   398	[37m    [39;49;00m$
   399	[37m    Instance.objectEnumerator()[39;49;00m$
   400	[37m    {[39;49;00m$
   401	[37m        return this._objects.objectEnumerator();[39;49;00m$
   402	[37m    }[39;49;00m$
   403	[37m*/[39;49;00m[37m[39;49;00m$
   404	[37m/*![39;49;00m$
   405	[37m    Returns the object for the entry with key \c aKey.[39;49;00m$
   406	[37m    @param aKey the key for the object's entry[39;49;00m$
   407	[37m    @return the object for the entry[39;49;00m$
   408	[37m*/[39;49;00m[37m[39;49;00m$
   409	-[37m [39;49;00m([36mid[39;49;00m)[32mobjectForKey:[39;49;00m([36mCPString[39;49;00m)aKey[37m[39;49;00m$
   410	{[37m[39;49;00m$
   411	[37m    [39;49;00m[34mvar[39;49;00m[37m [39;49;00mobject[37m [39;49;00m=[37m [39;49;00m_buckets[aKey];[37m[39;49;00m$
   412	[37m    [39;49;00m$
   413	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m(object[37m [39;49;00m===[37m [39;49;00m[34mundefined[39;49;00m)[37m [39;49;00m?[37m [39;49;00m[34mnil[39;49;00m[37m [39;49;00m:[37m [39;49;00mobject;[37m[39;49;00m$
   414	}[37m[39;49;00m$
   415	[37m/*[39;49;00m$
   416	[37m    Instance.objectsForKeys(keys, aNotFoundMarker)[39;49;00m$
   417	[37m    {[39;49;00m$
   418	[37m        var i= keys.length,[39;49;00m$
   419	[37m            objects= CPArray.array();[39;49;00m$
   420	[37m        [39;49;00m$
   421	[37m        while(i--)[39;49;00m$
   422	[37m        {[39;49;00m$
   423	[37m            var object= this.objectForKey(keys[i]);[39;49;00m$
   424	[37m            objects.addObject(object==nil?aNotFoundMarker:object);[39;49;00m$
   425	[37m        }[39;49;00m$
   426	[37m        [39;49;00m$
   427	[37m        return objects;[39;49;00m$
   428	[37m    }[39;49;00m$
   429	[37m    [39;49;00m$
   430	[37m    Instance.valueForKey(aKey)[39;49;00m$
   431	[37m    {[39;49;00m$
   432	[37m        if(aKey.length && aKey[0]=="@") return this.objectForKey(aKey.substr(1));[39;49;00m$
   433	[37m        [39;49;00m$
   434	[37m        return base.valueForKey(aKey);[39;49;00m$
   435	[37m    }[39;49;00m$
   436	[37m    [39;49;00m$
   437	[37m    //[39;49;00m$
   438	[37m    [39;49;00m$
   439	[37m    Instance.addEntriesFromDictionary(aDictionary)[39;49;00m$
   440	[37m    {[39;49;00m$
   441	[37m        var key,[39;49;00m$
   442	[37m            keyEnumerator= aDictionary.keyEnumerator();[39;49;00m$
   443	[37m[39;49;00m$
   444	[37m        while(key= keyEnumerator.nextObject()) this.setObjectForKey(aDictionary.objectForKey(key), key);[39;49;00m$
   445	[37m    }[39;49;00m$
   446	[37m*/[39;49;00m[37m[39;49;00m$
   447	[37m/*![39;49;00m$
   448	[37m    Removes all the entries from the dictionary.[39;49;00m$
   449	[37m*/[39;49;00m[37m[39;49;00m$
   450	-[37m [39;49;00m([36mvoid[39;49;00m)[32mremoveAllObjects[39;49;00m[37m[39;49;00m$
   451	{[37m[39;49;00m$
   452	[37m    [39;49;00m_keys[37m [39;49;00m=[37m [39;49;00m[];[37m[39;49;00m$
   453	[37m    [39;49;00mcount[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   454	[37m    [39;49;00m_buckets[37m [39;49;00m=[37m [39;49;00m{};[37m[39;49;00m$
   455	}[37m[39;49;00m$
   456	[37m[39;49;00m$
   457	[37m/*![39;49;00m$
   458	[37m    Removes the entry for the specified key.[39;49;00m$
   459	[37m    @param aKey the key of the entry to be removed[39;49;00m$
   460	[37m*/[39;49;00m[37m[39;49;00m$
   461	-[37m [39;49;00m([36mvoid[39;49;00m)[32mremoveObjectForKey:[39;49;00m([36mid[39;49;00m)aKey[37m[39;49;00m$
   462	{[37m[39;49;00m$
   463	[37m    [39;49;00m[32mdictionary_removeValue[39;49;00m([36mself[39;49;00m,[37m [39;49;00maKey);[37m[39;49;00m$
   464	}[37m[39;49;00m$
   465	[37m[39;49;00m$
   466	[37m/*![39;49;00m$
   467	[37m    Removes each entry in allKeys from the receiver.[39;49;00m$
   468	[37m    @param allKeys an array of keys that will be removed from the dictionary[39;49;00m$
   469	[37m*/[39;49;00m[37m[39;49;00m$
   470	-[37m [39;49;00m([36mvoid[39;49;00m)[32mremoveObjectsForKeys:[39;49;00m([36mCPArray[39;49;00m)allKeys[37m[39;49;00m$
   471	{[37m[39;49;00m$
   472	[37m    [39;49;00m[34mvar[39;49;00m[37m [39;49;00mindex[37m [39;49;00m=[37m [39;49;00mallKeys.length;[37m[39;49;00m$
   473	[37m[39;49;00m$
   474	[37m    [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(index--)[37m[39;49;00m$
   475	[37m        [39;49;00m[32mdictionary_removeValue[39;49;00m([36mself[39;49;00m,[37m [39;49;00mallKeys[index]);[37m[39;49;00m$
   476	}[37m[39;49;00m$
   477	[37m[39;49;00m$
   478	[37m/*[39;49;00m$
   479	[37m    Instance.removeObjectForKey(aKey)[39;49;00m$
   480	[37m    {[39;49;00m$
   481	[37m        var entry= this._dictionary[aKey];[39;49;00m$
   482	[37m        [39;49;00m$
   483	[37m        if(entry)[39;49;00m$
   484	[37m        {[39;49;00m$
   485	[37m            var range= CPMakeRange(entry.index, 1);[39;49;00m$
   486	[37m            [39;49;00m$
   487	[37m            this._keys.removeObjectsInRange(range);[39;49;00m$
   488	[37m            this._objects.removeObjectsInRange(range);[39;49;00m$
   489	[37m        [39;49;00m$
   490	[37m            delete this._dictionary[aKey];[39;49;00m$
   491	[37m        }[39;49;00m$
   492	[37m    }[39;49;00m$
   493	[37m    [39;49;00m$
   494	[37m    Instance.setDictionary(aDictionary)[39;49;00m$
   495	[37m    {[39;49;00m$
   496	[37m        this._keys= CPArray.arrayWithArray(aDictionary.allKeys());[39;49;00m$
   497	[37m        this._objects= CPArray.arrayWithArray(aDictionary.allValues());[39;49;00m$
   498	[37m        [39;49;00m$
   499	[37m        this._dictionary= { };[39;49;00m$
   500	[37m        [39;49;00m$
   501	[37m        var i= this._keys.count();[39;49;00m$
   502	[37m        while(i--) this._dictionary[this._keys[i]]= { object: this._objects[i], index: i };[39;49;00m$
   503	[37m    }[39;49;00m$
   504	[37m*/[39;49;00m[37m[39;49;00m$
   505	[37m/*![39;49;00m$
   506	[37m    Adds an entry into the dictionary.[39;49;00m$
   507	[37m    @param anObject the object for the entry[39;49;00m$
   508	[37m    @param aKey the entry's key[39;49;00m$
   509	[37m*/[39;49;00m[37m[39;49;00m$
   510	-[37m [39;49;00m([36mvoid[39;49;00m)[32msetObject:[39;49;00m([36mid[39;49;00m)anObject[37m [39;49;00m[32mforKey:[39;49;00m([36mid[39;49;00m)aKey[37m[39;49;00m$
   511	{[37m[39;49;00m$
   512	[37m    [39;49;00m[32mdictionary_setValue[39;49;00m([36mself[39;49;00m,[37m [39;49;00maKey,[37m [39;49;00manObject);[37m[39;49;00m$
   513	}[37m[39;49;00m$
   514	[37m/*[39;49;00m$
   515	[37m    Instance.setValueForKey(aValue, aKey)[39;49;00m$
   516	[37m    {[39;49;00m$
   517	[37m        if(!aValue) this.removeObjectForKey(aKey);[39;49;00m$
   518	[37m        else this.setObjectForKey(aValue, aKey);[39;49;00m$
   519	[37m    }[39;49;00m$
   520	[37m    [39;49;00m$
   521	[37m    Instance.copy()[39;49;00m$
   522	[37m    {[39;49;00m$
   523	[37m        return CPDictionary.alloc().dictionaryWithDictionary(this);[39;49;00m$
   524	[37m    }[39;49;00m$
   525	[37m*/[39;49;00m[37m[39;49;00m$
   526	[37m[39;49;00m$
   527	[37m/*![39;49;00m$
   528	[37m    Take all the key/value pairs in aDictionary and apply them to this dictionary.[39;49;00m$
   529	[37m*/[39;49;00m[37m[39;49;00m$
   530	-[37m [39;49;00m([36mvoid[39;49;00m)[32maddEntriesFromDictionary:[39;49;00m([36mCPDictionary[39;49;00m)aDictionary[37m[39;49;00m$
   531	{[37m[39;49;00m$
   532	[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!aDictionary)[37m[39;49;00m$
   533	[37m        [39;49;00m[34mreturn[39;49;00m;[37m[39;49;00m$
   534	[37m        [39;49;00m$
   535	[37m    [39;49;00m[34mvar[39;49;00m[37m [39;49;00mkeys[37m [39;49;00m=[37m [39;49;00m[aDictionary[37m [39;49;00mallKeys],[37m[39;49;00m$
   536	[37m        [39;49;00mindex[37m [39;49;00m=[37m [39;49;00m[keys[37m [39;49;00mcount];[37m[39;49;00m$
   537	[37m    [39;49;00m$
   538	[37m    [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(index--)[37m[39;49;00m$
   539	[37m    [39;49;00m{[37m[39;49;00m$
   540	[37m        [39;49;00m[34mvar[39;49;00m[37m [39;49;00mkey[37m [39;49;00m=[37m [39;49;00mkeys[index];[37m[39;49;00m$
   541	[37m[39;49;00m$
   542	[37m        [39;49;00m[[36mself[39;49;00m[37m [39;49;00msetObject:[aDictionary[37m [39;49;00mobjectForKey:key][37m [39;49;00mforKey:key];[37m[39;49;00m$
   543	[37m    [39;49;00m}[37m[39;49;00m$
   544	}[37m[39;49;00m$
   545	[37m[39;49;00m$
   546	[37m/*![39;49;00m$
   547	[37m    Returns a human readable description of the dictionary.[39;49;00m$
   548	[37m*/[39;49;00m[37m[39;49;00m$
   549	-[37m [39;49;00m([36mCPString[39;49;00m)[32mdescription[39;49;00m[37m[39;49;00m$
   550	{[37m[39;49;00m$
   551	[37m    [39;49;00m[34mvar[39;49;00m[37m [39;49;00mdescription[37m [39;49;00m=[37m [39;49;00m[33m@"[39;49;00m[33mCPDictionary {[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
   552	[37m    [39;49;00m$
   553	[37m    [39;49;00m[34mvar[39;49;00m[37m [39;49;00mi[37m [39;49;00m=[37m [39;49;00m_keys.length;[37m[39;49;00m$
   554	[37m    [39;49;00m$
   555	[37m    [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(i--)[37m[39;49;00m$
   556	[37m    [39;49;00m{[37m[39;49;00m$
   557	[37m        [39;49;00mdescription[37m [39;49;00m+=[37m [39;49;00m_keys[i][37m [39;49;00m+[37m [39;49;00m[33m"[39;49;00m[33m:[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
   558	[37m[39;49;00m$
   559	[37m        [39;49;00m[34mvar[39;49;00m[37m [39;49;00mobject[37m [39;49;00m=[37m [39;49;00m_buckets[_keys[i]];[37m[39;49;00m$
   560	[37m[39;49;00m$
   561	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(object[37m [39;49;00m&&[37m [39;49;00mobject.isa)[37m[39;49;00m$
   562	[37m            [39;49;00mdescription[37m [39;49;00m+=[37m [39;49;00m[object[37m [39;49;00mdescription];[37m[39;49;00m$
   563	[37m        [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
   564	[37m            [39;49;00mdescription[37m [39;49;00m+=[37m [39;49;00mobject;[37m[39;49;00m$
   565	[37m[39;49;00m$
   566	[37m        [39;49;00mdescription[37m [39;49;00m+=[37m [39;49;00m[33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
   567	[37m    [39;49;00m}[37m[39;49;00m$
   568	[37m[39;49;00m$
   569	[37m    [39;49;00mdescription[37m [39;49;00m+=[37m [39;49;00m[33m"[39;49;00m[33m}[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
   570	[37m[39;49;00m$
   571	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mdescription;[37m[39;49;00m$
   572	}[37m[39;49;00m$
   573	[37m[39;49;00m$
   574	[34m@end[39;49;00m[37m[39;49;00m$
   575	[37m[39;49;00m$
   576	[34m@implementation[39;49;00m[37m [39;49;00m[04m[32mCPDictionary[39;49;00m[37m [39;49;00m(CPCoding)[37m[39;49;00m$
   577	[37m[39;49;00m$
   578	[37m/*[39;49;00m$
   579	[37m    Initializes the dictionary by unarchiving the data from a coder.[39;49;00m$
   580	[37m    @param aCoder the coder from which the data will be unarchived.[39;49;00m$
   581	[37m    @return the initialized dictionary[39;49;00m$
   582	[37m*/[39;49;00m[37m[39;49;00m$
   583	-[37m [39;49;00m([36mid[39;49;00m)[32minitWithCoder:[39;49;00m([36mCPCoder[39;49;00m)aCoder[37m[39;49;00m$
   584	{[37m[39;49;00m$
   585	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[aCoder[37m [39;49;00m_decodeDictionaryOfObjectsForKey:[33m@"[39;49;00m[33mCP.objects[39;49;00m[33m"[39;49;00m];[37m[39;49;00m$
   586	}[37m[39;49;00m$
   587	[37m[39;49;00m$
   588	[37m/*![39;49;00m$
   589	[37m    Archives the dictionary to a provided coder.[39;49;00m$
   590	[37m    @param aCoder the coder to which the dictionary data will be archived.[39;49;00m$
   591	[37m*/[39;49;00m[37m[39;49;00m$
   592	-[37m [39;49;00m([36mvoid[39;49;00m)[32mencodeWithCoder:[39;49;00m([36mCPCoder[39;49;00m)aCoder[37m[39;49;00m$
   593	{[37m[39;49;00m$
   594	[37m    [39;49;00m[aCoder[37m [39;49;00m_encodeDictionaryOfObjects:[36mself[39;49;00m[37m [39;49;00mforKey:[33m@"[39;49;00m[33mCP.objects[39;49;00m[33m"[39;49;00m];[37m[39;49;00m$
   595	}[37m[39;49;00m$
   596	[37m[39;49;00m$
   597	[34m@end[39;49;00m[37m[39;49;00m$
   598	[37m[39;49;00m$
   599	[37m/*![39;49;00m$
   600	[37m    @class CPMutableDictionary[39;49;00m$
   601	[37m    @ingroup compatability[39;49;00m$
   602	[37m[39;49;00m$
   603	[37m    This class is just an empty subclass of CPDictionary.[39;49;00m$
   604	[37m    CPDictionary already implements mutable methods and[39;49;00m$
   605	[37m    this class only exists for source compatability.[39;49;00m$
   606	[37m*/[39;49;00m[37m[39;49;00m$
   607	[34m@implementation[39;49;00m[37m [39;49;00m[04m[32mCPMutableDictionary[39;49;00m[37m [39;49;00m:[37m [39;49;00m[04m[32mCPDictionary[39;49;00m[37m[39;49;00m$
   608	[37m[39;49;00m$
   609	[34m@end[39;49;00m[37m[39;49;00m$
   610	[37m[39;49;00m$
   611	objj_dictionary.[34mprototype[39;49;00m.isa[37m [39;49;00m=[37m [39;49;00mCPDictionary;$

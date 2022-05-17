     1^I[37m/*[39;49;00m$
     2^I[37m * CPDictionary.j[39;49;00m$
     3^I[37m * Foundation[39;49;00m$
     4^I[37m *[39;49;00m$
     5^I[37m * Created by Francisco Tolmasky.[39;49;00m$
     6^I[37m * Copyright 2008, 280 North, Inc.[39;49;00m$
     7^I[37m *[39;49;00m$
     8^I[37m * This library is free software; you can redistribute it and/or[39;49;00m$
     9^I[37m * modify it under the terms of the GNU Lesser General Public[39;49;00m$
    10^I[37m * License as published by the Free Software Foundation; either[39;49;00m$
    11^I[37m * version 2.1 of the License, or (at your option) any later version.[39;49;00m$
    12^I[37m *[39;49;00m$
    13^I[37m * This library is distributed in the hope that it will be useful,[39;49;00m$
    14^I[37m * but WITHOUT ANY WARRANTY; without even the implied warranty of[39;49;00m$
    15^I[37m * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU[39;49;00m$
    16^I[37m * Lesser General Public License for more details.[39;49;00m$
    17^I[37m *[39;49;00m$
    18^I[37m * You should have received a copy of the GNU Lesser General Public[39;49;00m$
    19^I[37m * License along with this library; if not, write to the Free Software[39;49;00m$
    20^I[37m * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA[39;49;00m$
    21^I[37m */[39;49;00m[37m[39;49;00m$
    22^I[37m[39;49;00m$
    23^I[37m//@import "CPRange.j"[39;49;00m$
    24^I[36m@import[39;49;00m[37m [39;49;00m[33m"CPObject.j"[39;49;00m[37m[39;49;00m$
    25^I[36m@import[39;49;00m[37m [39;49;00m[33m"CPEnumerator.j"[39;49;00m[37m[39;49;00m$
    26^I[36m@import[39;49;00m[37m [39;49;00m[33m"CPException.j"[39;49;00m[37m[39;49;00m$
    27^I[37m[39;49;00m$
    28^I[37m/* @ignore */[39;49;00m[37m[39;49;00m$
    29^I[34m@implementation[39;49;00m[37m [39;49;00m[04m[32m_CPDictionaryValueEnumerator[39;49;00m[37m [39;49;00m:[37m [39;49;00m[04m[32mCPEnumerator[39;49;00m[37m[39;49;00m$
    30^I{[37m[39;49;00m$
    31^I[37m    [39;49;00mCPEnumerator[37m    [39;49;00m_keyEnumerator;[37m[39;49;00m$
    32^I[37m    [39;49;00mCPDictionary[37m    [39;49;00m_dictionary;[37m[39;49;00m$
    33^I}[37m[39;49;00m$
    34^I[37m[39;49;00m$
    35^I-[37m [39;49;00m([36mid[39;49;00m)[32minitWithDictionary:[39;49;00m([36mCPDictionary[39;49;00m)aDictionary[37m[39;49;00m$
    36^I{[37m[39;49;00m$
    37^I[37m    [39;49;00m[36mself[39;49;00m[37m [39;49;00m=[37m [39;49;00m[[36msuper[39;49;00m[37m [39;49;00minit];[37m[39;49;00m$
    38^I[37m    [39;49;00m$
    39^I[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m([36mself[39;49;00m)[37m[39;49;00m$
    40^I[37m    [39;49;00m{[37m[39;49;00m$
    41^I[37m        [39;49;00m_keyEnumerator[37m [39;49;00m=[37m [39;49;00m[aDictionary[37m [39;49;00mkeyEnumerator];[37m[39;49;00m$
    42^I[37m        [39;49;00m_dictionary[37m [39;49;00m=[37m [39;49;00maDictionary;[37m[39;49;00m$
    43^I[37m    [39;49;00m}[37m[39;49;00m$
    44^I[37m    [39;49;00m$
    45^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[36mself[39;49;00m;[37m[39;49;00m$
    46^I}[37m[39;49;00m$
    47^I[37m[39;49;00m$
    48^I-[37m [39;49;00m([36mid[39;49;00m)[32mnextObject[39;49;00m[37m[39;49;00m$
    49^I{[37m[39;49;00m$
    50^I[37m    [39;49;00m[34mvar[39;49;00m[37m [39;49;00mkey[37m [39;49;00m=[37m [39;49;00m[_keyEnumerator[37m [39;49;00mnextObject];[37m[39;49;00m$
    51^I[37m    [39;49;00m$
    52^I[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!key)[37m[39;49;00m$
    53^I[37m        [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mnil[39;49;00m;[37m[39;49;00m$
    54^I[37m[39;49;00m$
    55^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[_dictionary[37m [39;49;00mobjectForKey:key];[37m[39;49;00m$
    56^I}[37m[39;49;00m$
    57^I[37m[39;49;00m$
    58^I[34m@end[39;49;00m[37m[39;49;00m$
    59^I[37m[39;49;00m$
    60^I[37m/*! [39;49;00m$
    61^I[37m    @class CPDictionary[39;49;00m$
    62^I[37m    @ingroup foundation[39;49;00m$
    63^I[37m    @brief A mutable key-value pair collection.[39;49;00m$
    64^I[37m[39;49;00m$
    65^I[37m    A dictionary is the standard way of passing around key-value pairs in[39;49;00m$
    66^I[37m    the Cappuccino framework. It is similar to the[39;49;00m$
    67^I[37m    <a href="http://java.sun.com/javase/6/docs/api/index.html">Java map interface</a>,[39;49;00m$
    68^I[37m    except all keys are CPStrings and values can be any[39;49;00m$
    69^I[37m    Cappuccino or JavaScript object.[39;49;00m$
    70^I[37m[39;49;00m$
    71^I[37m    If you are familiar with dictionaries in Cocoa, you'll notice that[39;49;00m$
    72^I[37m    there is no CPMutableDictionary class. The regular CPDictionary[39;49;00m$
    73^I[37m    has \c -setObject:forKey: and \c -removeObjectForKey: methods.[39;49;00m$
    74^I[37m    In Cappuccino there is no distinction between immutable and mutable classes.[39;49;00m$
    75^I[37m    They are all mutable.[39;49;00m$
    76^I[37m*/[39;49;00m[37m[39;49;00m$
    77^I[34m@implementation[39;49;00m[37m [39;49;00m[04m[32mCPDictionary[39;49;00m[37m [39;49;00m:[37m [39;49;00m[04m[32mCPObject[39;49;00m[37m[39;49;00m$
    78^I{[37m[39;49;00m$
    79^I}[37m[39;49;00m$
    80^I[37m[39;49;00m$
    81^I[37m/*[39;49;00m$
    82^I[37m    @ignore[39;49;00m$
    83^I[37m*/[39;49;00m[37m[39;49;00m$
    84^I+[37m [39;49;00m([36mid[39;49;00m)[32malloc[39;49;00m[37m[39;49;00m$
    85^I{[37m[39;49;00m$
    86^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00m[32mobjj_dictionary[39;49;00m();[37m[39;49;00m$
    87^I}[37m[39;49;00m$
    88^I[37m[39;49;00m$
    89^I[37m/*![39;49;00m$
    90^I[37m    Returns a new empty CPDictionary.[39;49;00m$
    91^I[37m*/[39;49;00m[37m[39;49;00m$
    92^I+[37m [39;49;00m([36mid[39;49;00m)[32mdictionary[39;49;00m[37m[39;49;00m$
    93^I{[37m[39;49;00m$
    94^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[[[36mself[39;49;00m[37m [39;49;00malloc][37m [39;49;00minit];[37m[39;49;00m$
    95^I}[37m[39;49;00m$
    96^I[37m[39;49;00m$
    97^I[37m/*![39;49;00m$
    98^I[37m    Returns a new dictionary, initialized with the contents of \c aDictionary.[39;49;00m$
    99^I[37m    @param aDictionary the dictionary to copy key-value pairs from[39;49;00m$
   100^I[37m    @return the new CPDictionary[39;49;00m$
   101^I[37m*/[39;49;00m[37m[39;49;00m$
   102^I+[37m [39;49;00m([36mid[39;49;00m)[32mdictionaryWithDictionary:[39;49;00m([36mCPDictionary[39;49;00m)aDictionary[37m[39;49;00m$
   103^I{[37m[39;49;00m$
   104^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[[[36mself[39;49;00m[37m [39;49;00malloc][37m [39;49;00minitWithDictionary:aDictionary];[37m[39;49;00m$
   105^I}[37m[39;49;00m$
   106^I[37m[39;49;00m$
   107^I[37m/*![39;49;00m$
   108^I[37m    Creates a new dictionary with single key-value pair.[39;49;00m$
   109^I[37m    @param anObject the object for the paring[39;49;00m$
   110^I[37m    @param aKey the key for the pairing[39;49;00m$
   111^I[37m    @return the new CPDictionary[39;49;00m$
   112^I[37m*/[39;49;00m[37m[39;49;00m$
   113^I+[37m [39;49;00m([36mid[39;49;00m)[32mdictionaryWithObject:[39;49;00m([36mid[39;49;00m)anObject[37m [39;49;00m[32mforKey:[39;49;00m([36mid[39;49;00m)aKey[37m[39;49;00m$
   114^I{[37m[39;49;00m$
   115^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[[[36mself[39;49;00m[37m [39;49;00malloc][37m [39;49;00minitWithObjects:[anObject][37m [39;49;00mforKeys:[aKey]];[37m[39;49;00m$
   116^I}[37m[39;49;00m$
   117^I[37m[39;49;00m$
   118^I[37m/*![39;49;00m$
   119^I[37m    Creates a dictionary with multiple key-value pairs.[39;49;00m$
   120^I[37m    @param objects the objects to place in the dictionary[39;49;00m$
   121^I[37m    @param keys the keys for each of the objects[39;49;00m$
   122^I[37m    @throws CPInvalidArgumentException if the number of objects and keys is different[39;49;00m$
   123^I[37m    @return the new CPDictionary[39;49;00m$
   124^I[37m*/[39;49;00m[37m[39;49;00m$
   125^I+[37m [39;49;00m([36mid[39;49;00m)[32mdictionaryWithObjects:[39;49;00m([36mCPArray[39;49;00m)objects[37m [39;49;00m[32mforKeys:[39;49;00m([36mCPArray[39;49;00m)keys[37m[39;49;00m$
   126^I{[37m[39;49;00m$
   127^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[[[36mself[39;49;00m[37m [39;49;00malloc][37m [39;49;00minitWithObjects:objects[37m [39;49;00mforKeys:keys];[37m[39;49;00m$
   128^I}[37m[39;49;00m$
   129^I[37m[39;49;00m$
   130^I[37m/*![39;49;00m$
   131^I[37m    Creates a dictionary with multiple key-value pairs.[39;49;00m$
   132^I[37m    @param JavaScript object[39;49;00m$
   133^I[37m    @return the new CPDictionary[39;49;00m$
   134^I[37m*/[39;49;00m[37m[39;49;00m$
   135^I+[37m [39;49;00m([36mid[39;49;00m)[32mdictionaryWithJSObject:[39;49;00m([36mJSObject[39;49;00m)object[37m[39;49;00m$
   136^I{[37m[39;49;00m$
   137^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[[36mself[39;49;00m[37m [39;49;00mdictionaryWithJSObject:object[37m [39;49;00mrecursively:[34mNO[39;49;00m];[37m[39;49;00m$
   138^I}[37m[39;49;00m$
   139^I[37m[39;49;00m$
   140^I[37m/*![39;49;00m$
   141^I[37m    Creates a dictionary with multiple key-value pairs, recursively.[39;49;00m$
   142^I[37m    @param JavaScript object[39;49;00m$
   143^I[37m    @return the new CPDictionary[39;49;00m$
   144^I[37m*/[39;49;00m[37m[39;49;00m$
   145^I+[37m [39;49;00m([36mid[39;49;00m)[32mdictionaryWithJSObject:[39;49;00m([36mJSObject[39;49;00m)object[37m [39;49;00m[32mrecursively:[39;49;00m([36mBOOL[39;49;00m)recursively[37m[39;49;00m$
   146^I{[37m[39;49;00m$
   147^I[37m    [39;49;00m[34mvar[39;49;00m[37m [39;49;00mdictionary[37m [39;49;00m=[37m [39;49;00m[[[36mself[39;49;00m[37m [39;49;00malloc][37m [39;49;00minit];[37m[39;49;00m$
   148^I[37m        [39;49;00m$
   149^I[37m    [39;49;00m[34mfor[39;49;00m[37m [39;49;00m([34mvar[39;49;00m[37m [39;49;00mkey[37m [39;49;00m[34min[39;49;00m[37m [39;49;00mobject)[37m[39;49;00m$
   150^I[37m    [39;49;00m{[37m[39;49;00m$
   151^I[37m        [39;49;00m[34mvar[39;49;00m[37m [39;49;00mvalue[37m [39;49;00m=[37m [39;49;00mobject[key];[37m[39;49;00m$
   152^I[37m    [39;49;00m$
   153^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(recursively[37m [39;49;00m&&[37m [39;49;00mvalue.constructor[37m [39;49;00m===[37m [39;49;00m[36mObject[39;49;00m)[37m[39;49;00m$
   154^I[37m            [39;49;00mvalue[37m [39;49;00m=[37m [39;49;00m[CPDictionary[37m [39;49;00mdictionaryWithJSObject:value[37m [39;49;00mrecursively:[34mYES[39;49;00m];[37m[39;49;00m$
   155^I[37m    [39;49;00m$
   156^I[37m        [39;49;00m[dictionary[37m [39;49;00msetObject:value[37m [39;49;00mforKey:key];[37m[39;49;00m$
   157^I[37m    [39;49;00m}[37m[39;49;00m$
   158^I[37m    [39;49;00m$
   159^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mdictionary;[37m[39;49;00m$
   160^I}[37m[39;49;00m$
   161^I[37m[39;49;00m$
   162^I[37m/*![39;49;00m$
   163^I[37m    Creates and returns a dictionary constructed by a given pairs of keys and values.[39;49;00m$
   164^I[37m    @param firstObject first object value[39;49;00m$
   165^I[37m    @param ... key for the first object and ongoing value-key pairs for more objects.[39;49;00m$
   166^I[37m    @throws CPInvalidArgumentException if the number of objects and keys is different[39;49;00m$
   167^I[37m    @return the new CPDictionary[39;49;00m$
   168^I[37m    [39;49;00m$
   169^I[37m    Assuming that there's no object retaining in Cappuccino, you can create[39;49;00m$
   170^I[37m    dictionaries same way as with alloc and initWithObjectsAndKeys:[39;49;00m$
   171^I[37m    var dict = [CPDictionary dictionaryWithObjectsAndKeys:[39;49;00m$
   172^I[37m    @"value1", @"key1",[39;49;00m$
   173^I[37m    @"value2", @"key2"];[39;49;00m$
   174^I[37m    [39;49;00m$
   175^I[37m    Note, that there's no final nil like in Objective-C/Cocoa.[39;49;00m$
   176^I[37m    [39;49;00m$
   177^I[37m    @see [CPDictionary initWithObjectsAndKeys:][39;49;00m$
   178^I[37m*/[39;49;00m[37m[39;49;00m$
   179^I+[37m [39;49;00m([36mid[39;49;00m)[32mdictionaryWithObjectsAndKeys:[39;49;00m([36mid[39;49;00m)firstObject,[37m [39;49;00m...[37m[39;49;00m$
   180^I{[37m[39;49;00m$
   181^I[37m    [39;49;00marguments[[34m0[39;49;00m][37m [39;49;00m=[37m [39;49;00m[[36mself[39;49;00m[37m [39;49;00malloc];[37m[39;49;00m$
   182^I[37m    [39;49;00marguments[[34m1[39;49;00m][37m [39;49;00m=[37m [39;49;00m[34m@selector[39;49;00m(initWithObjectsAndKeys:);[37m[39;49;00m$
   183^I[37m    [39;49;00m$
   184^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mobjj_msgSend.[32mapply[39;49;00m([36mthis[39;49;00m,[37m [39;49;00marguments);[37m[39;49;00m$
   185^I}[37m[39;49;00m$
   186^I[37m[39;49;00m$
   187^I[37m/*![39;49;00m$
   188^I[37m    Initializes the dictionary with the contents of another dictionary.[39;49;00m$
   189^I[37m    @param aDictionary the dictionary to copy key-value pairs from[39;49;00m$
   190^I[37m    @return the initialized dictionary[39;49;00m$
   191^I[37m*/[39;49;00m[37m[39;49;00m$
   192^I-[37m [39;49;00m([36mid[39;49;00m)[32minitWithDictionary:[39;49;00m([36mCPDictionary[39;49;00m)aDictionary[37m[39;49;00m$
   193^I{[37m[39;49;00m$
   194^I[37m    [39;49;00m[34mvar[39;49;00m[37m [39;49;00mkey[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33m"[39;49;00m,[37m[39;49;00m$
   195^I[37m        [39;49;00mdictionary[37m [39;49;00m=[37m [39;49;00m[[CPDictionary[37m [39;49;00malloc][37m [39;49;00minit];[37m[39;49;00m$
   196^I[37m    [39;49;00m$
   197^I[37m    [39;49;00m[34mfor[39;49;00m[37m [39;49;00m(key[37m [39;49;00m[34min[39;49;00m[37m [39;49;00maDictionary._buckets)[37m[39;49;00m$
   198^I[37m        [39;49;00m[dictionary[37m [39;49;00msetObject:[aDictionary[37m [39;49;00mobjectForKey:key][37m [39;49;00mforKey:key];[37m[39;49;00m$
   199^I[37m        [39;49;00m$
   200^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mdictionary;[37m[39;49;00m$
   201^I}[37m[39;49;00m$
   202^I[37m[39;49;00m$
   203^I[37m/*![39;49;00m$
   204^I[37m    Initializes the dictionary from the arrays of keys and objects.[39;49;00m$
   205^I[37m    @param objects the objects to put in the dictionary[39;49;00m$
   206^I[37m    @param keyArray the keys for the objects to put in the dictionary[39;49;00m$
   207^I[37m    @throws CPInvalidArgumentException if the number of objects and keys is different[39;49;00m$
   208^I[37m    @return the initialized dictionary[39;49;00m$
   209^I[37m*/[39;49;00m[37m[39;49;00m$
   210^I-[37m [39;49;00m([36mid[39;49;00m)[32minitWithObjects:[39;49;00m([36mCPArray[39;49;00m)objects[37m [39;49;00m[32mforKeys:[39;49;00m([36mCPArray[39;49;00m)keyArray[37m[39;49;00m$
   211^I{[37m[39;49;00m$
   212^I[37m    [39;49;00m[36mself[39;49;00m[37m [39;49;00m=[37m [39;49;00m[[36msuper[39;49;00m[37m [39;49;00minit];[37m[39;49;00m$
   213^I[37m[39;49;00m$
   214^I[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m([objects[37m [39;49;00mcount][37m [39;49;00m!=[37m [39;49;00m[keyArray[37m [39;49;00mcount])[37m[39;49;00m$
   215^I[37m        [39;49;00m[CPException[37m [39;49;00mraise:CPInvalidArgumentException[37m [39;49;00mreason:[33m"[39;49;00m[33mCounts are different.([39;49;00m[33m"[39;49;00m+[objects[37m [39;49;00mcount]+[33m"[39;49;00m[33m!=[39;49;00m[33m"[39;49;00m+[keyArray[37m [39;49;00mcount]+[33m"[39;49;00m[33m)[39;49;00m[33m"[39;49;00m];[37m[39;49;00m$
   216^I[37m[39;49;00m$
   217^I[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m([36mself[39;49;00m)[37m[39;49;00m$
   218^I[37m    [39;49;00m{[37m[39;49;00m$
   219^I[37m        [39;49;00m[34mvar[39;49;00m[37m [39;49;00mi[37m [39;49;00m=[37m [39;49;00m[keyArray[37m [39;49;00mcount];[37m[39;49;00m$
   220^I[37m        [39;49;00m$
   221^I[37m        [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(i--)[37m[39;49;00m$
   222^I[37m            [39;49;00m[[36mself[39;49;00m[37m [39;49;00msetObject:objects[i][37m [39;49;00mforKey:keyArray[i]];[37m[39;49;00m$
   223^I[37m    [39;49;00m}[37m[39;49;00m$
   224^I[37m    [39;49;00m$
   225^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[36mself[39;49;00m;[37m[39;49;00m$
   226^I}[37m[39;49;00m$
   227^I[37m[39;49;00m$
   228^I[37m/*![39;49;00m$
   229^I[37m    Creates and returns a dictionary constructed by a given pairs of keys and values.[39;49;00m$
   230^I[37m    @param firstObject first object value[39;49;00m$
   231^I[37m    @param ... key for the first object and ongoing value-key pairs for more objects.[39;49;00m$
   232^I[37m    @throws CPInvalidArgumentException if the number of objects and keys is different[39;49;00m$
   233^I[37m    @return the new CPDictionary[39;49;00m$
   234^I[37m    [39;49;00m$
   235^I[37m    You can create dictionaries this way:[39;49;00m$
   236^I[37m    var dict = [[CPDictionary alloc] initWithObjectsAndKeys:[39;49;00m$
   237^I[37m    @"value1", @"key1",[39;49;00m$
   238^I[37m    @"value2", @"key2"];[39;49;00m$
   239^I[37m    [39;49;00m$
   240^I[37m    Note, that there's no final nil like in Objective-C/Cocoa.[39;49;00m$
   241^I[37m*/[39;49;00m[37m[39;49;00m$
   242^I-[37m [39;49;00m([36mid[39;49;00m)[32minitWithObjectsAndKeys:[39;49;00m([36mid[39;49;00m)firstObject,[37m [39;49;00m...[37m[39;49;00m$
   243^I{[37m[39;49;00m$
   244^I[37m    [39;49;00m[34mvar[39;49;00m[37m [39;49;00margCount[37m [39;49;00m=[37m [39;49;00marguments.length;[37m[39;49;00m$
   245^I[37m    [39;49;00m$
   246^I[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(argCount[37m [39;49;00m%[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m!==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
   247^I[37m        [39;49;00m[CPException[37m [39;49;00mraise:CPInvalidArgumentException[37m [39;49;00mreason:[33m"[39;49;00m[33mKey-value count is mismatched. ([39;49;00m[33m"[39;49;00m[37m [39;49;00m+[37m [39;49;00margCount[37m [39;49;00m+[37m [39;49;00m[33m"[39;49;00m[33m arguments passed)[39;49;00m[33m"[39;49;00m];[37m[39;49;00m$
   248^I[37m[39;49;00m$
   249^I[37m    [39;49;00m[36mself[39;49;00m[37m [39;49;00m=[37m [39;49;00m[[36msuper[39;49;00m[37m [39;49;00minit];[37m[39;49;00m$
   250^I[37m    [39;49;00m$
   251^I[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m([36mself[39;49;00m)[37m[39;49;00m$
   252^I[37m    [39;49;00m{[37m[39;49;00m$
   253^I[37m        [39;49;00m[37m// The arguments array contains self and _cmd, so the first object is at position 2.[39;49;00m$
   254^I[37m        [39;49;00m[34mvar[39;49;00m[37m [39;49;00mindex[37m [39;49;00m=[37m [39;49;00m[34m2[39;49;00m;[37m[39;49;00m$
   255^I[37m        [39;49;00m$
   256^I[37m        [39;49;00m[34mfor[39;49;00m(;[37m [39;49;00mindex[37m [39;49;00m<[37m [39;49;00margCount;[37m [39;49;00mindex[37m [39;49;00m+=[37m [39;49;00m[34m2[39;49;00m)[37m[39;49;00m$
   257^I[37m        [39;49;00m{[37m[39;49;00m$
   258^I[37m            [39;49;00m[34mvar[39;49;00m[37m [39;49;00mvalue[37m [39;49;00m=[37m [39;49;00marguments[index];[37m[39;49;00m$
   259^I[37m[39;49;00m$
   260^I[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(value[37m [39;49;00m===[37m [39;49;00m[34mnil[39;49;00m)[37m[39;49;00m$
   261^I[37m                [39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
   262^I[37m[39;49;00m$
   263^I[37m            [39;49;00m[[36mself[39;49;00m[37m [39;49;00msetObject:value[37m [39;49;00mforKey:arguments[index[37m [39;49;00m+[37m [39;49;00m[34m1[39;49;00m]];[37m[39;49;00m$
   264^I[37m        [39;49;00m}[37m[39;49;00m$
   265^I[37m    [39;49;00m}[37m[39;49;00m$
   266^I[37m[39;49;00m$
   267^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[36mself[39;49;00m;[37m[39;49;00m$
   268^I}[37m[39;49;00m$
   269^I[37m[39;49;00m$
   270^I[37m/*![39;49;00m$
   271^I[37m    return a copy of the receiver (does not deep copy the objects contained in the dictionary).[39;49;00m$
   272^I[37m*/[39;49;00m[37m[39;49;00m$
   273^I-[37m [39;49;00m([36mCPDictionary[39;49;00m)[32mcopy[39;49;00m[37m[39;49;00m$
   274^I{[37m[39;49;00m$
   275^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[CPDictionary[37m [39;49;00mdictionaryWithDictionary:[36mself[39;49;00m];[37m[39;49;00m$
   276^I}[37m[39;49;00m$
   277^I[37m[39;49;00m$
   278^I[37m/*![39;49;00m$
   279^I[37m    Returns the number of entries in the dictionary[39;49;00m$
   280^I[37m*/[39;49;00m[37m[39;49;00m$
   281^I-[37m [39;49;00m([36mint[39;49;00m)[32mcount[39;49;00m[37m[39;49;00m$
   282^I{[37m[39;49;00m$
   283^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mcount;[37m[39;49;00m$
   284^I}[37m[39;49;00m$
   285^I[37m[39;49;00m$
   286^I[37m/*![39;49;00m$
   287^I[37m    Returns an array of keys for all the entries in the dictionary.[39;49;00m$
   288^I[37m*/[39;49;00m[37m[39;49;00m$
   289^I-[37m [39;49;00m([36mCPArray[39;49;00m)[32mallKeys[39;49;00m[37m[39;49;00m$
   290^I{[37m[39;49;00m$
   291^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m_keys;[37m[39;49;00m$
   292^I}[37m[39;49;00m$
   293^I[37m[39;49;00m$
   294^I[37m/*![39;49;00m$
   295^I[37m    Returns an array of values for all the entries in the dictionary.[39;49;00m$
   296^I[37m*/[39;49;00m[37m[39;49;00m$
   297^I-[37m [39;49;00m([36mCPArray[39;49;00m)[32mallValues[39;49;00m[37m[39;49;00m$
   298^I{[37m[39;49;00m$
   299^I[37m    [39;49;00m[34mvar[39;49;00m[37m [39;49;00mindex[37m [39;49;00m=[37m [39;49;00m_keys.length,[37m[39;49;00m$
   300^I[37m        [39;49;00mvalues[37m [39;49;00m=[37m [39;49;00m[];[37m[39;49;00m$
   301^I[37m        [39;49;00m$
   302^I[37m    [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(index--)[37m[39;49;00m$
   303^I[37m        [39;49;00mvalues.[32mpush[39;49;00m([32mdictionary_getValue[39;49;00m([36mself[39;49;00m,[37m [39;49;00m[_keys[index]]));[37m[39;49;00m$
   304^I[37m[39;49;00m$
   305^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mvalues;[37m[39;49;00m$
   306^I}[37m[39;49;00m$
   307^I[37m[39;49;00m$
   308^I[37m/*![39;49;00m$
   309^I[37m    Returns an enumerator that enumerates over all the dictionary's keys.[39;49;00m$
   310^I[37m*/[39;49;00m[37m[39;49;00m$
   311^I-[37m [39;49;00m([36mCPEnumerator[39;49;00m)[32mkeyEnumerator[39;49;00m[37m[39;49;00m$
   312^I{[37m[39;49;00m$
   313^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[_keys[37m [39;49;00mobjectEnumerator];[37m[39;49;00m$
   314^I}[37m[39;49;00m$
   315^I[37m[39;49;00m$
   316^I[37m/*![39;49;00m$
   317^I[37m    Returns an enumerator that enumerates over all the dictionary's values.[39;49;00m$
   318^I[37m*/[39;49;00m[37m[39;49;00m$
   319^I-[37m [39;49;00m([36mCPEnumerator[39;49;00m)[32mobjectEnumerator[39;49;00m[37m[39;49;00m$
   320^I{[37m[39;49;00m$
   321^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[[_CPDictionaryValueEnumerator[37m [39;49;00malloc][37m [39;49;00minitWithDictionary:[36mself[39;49;00m];[37m[39;49;00m$
   322^I}[37m[39;49;00m$
   323^I[37m[39;49;00m$
   324^I[37m/*![39;49;00m$
   325^I[37m    Compare the receiver to this dictionary, and return whether or not they are equal. [39;49;00m$
   326^I[37m*/[39;49;00m[37m[39;49;00m$
   327^I-[37m [39;49;00m([36mBOOL[39;49;00m)[32misEqualToDictionary:[39;49;00m([36mCPDictionary[39;49;00m)aDictionary[37m[39;49;00m$
   328^I{[37m[39;49;00m$
   329^I[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(count[37m [39;49;00m!==[37m [39;49;00m[aDictionary[37m [39;49;00mcount])[37m[39;49;00m$
   330^I[37m        [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mNO[39;49;00m;[37m[39;49;00m$
   331^I[37m[39;49;00m$
   332^I[37m    [39;49;00m[34mvar[39;49;00m[37m [39;49;00mindex[37m [39;49;00m=[37m [39;49;00mcount;[37m[39;49;00m$
   333^I[37m    [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(index--)[37m[39;49;00m$
   334^I[37m    [39;49;00m{[37m[39;49;00m$
   335^I[37m        [39;49;00m[34mvar[39;49;00m[37m [39;49;00mcurrentKey[37m [39;49;00m=[37m [39;49;00m_keys[index],[37m[39;49;00m$
   336^I[37m            [39;49;00mlhsObject[37m [39;49;00m=[37m [39;49;00m_buckets[currentKey],[37m[39;49;00m$
   337^I[37m            [39;49;00mrhsObject[37m [39;49;00m=[37m [39;49;00maDictionary._buckets[currentKey];[37m[39;49;00m$
   338^I[37m[39;49;00m$
   339^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(lhsObject[37m [39;49;00m===[37m [39;49;00mrhsObject)[37m[39;49;00m$
   340^I[37m            [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
   341^I[37m            [39;49;00m$
   342^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(lhsObject.isa[37m [39;49;00m&&[37m [39;49;00mrhsObject.isa[37m [39;49;00m&&[37m [39;49;00m[lhsObject[37m [39;49;00mrespondsToSelector:[34m@selector[39;49;00m(isEqual:)][37m [39;49;00m&&[37m [39;49;00m[lhsObject[37m [39;49;00misEqual:rhsObject])[37m[39;49;00m$
   343^I[37m            [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
   344^I[37m        [39;49;00m$
   345^I[37m        [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mNO[39;49;00m;[37m[39;49;00m$
   346^I[37m    [39;49;00m}[37m[39;49;00m$
   347^I[37m[39;49;00m$
   348^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mYES[39;49;00m;[37m[39;49;00m$
   349^I}[37m[39;49;00m$
   350^I[37m[39;49;00m$
   351^I[37m/*[39;49;00m$
   352^I[37m    Instance.isEqualToDictionary(aDictionary)[39;49;00m$
   353^I[37m    {[39;49;00m$
   354^I[37m        if(this.count()!=aDictionary.count()) return NO;[39;49;00m$
   355^I[37m        [39;49;00m$
   356^I[37m        var i= this._keys.count();[39;49;00m$
   357^I[37m        while(i--) if(this.objectForKey(this._keys[i])!=aDictionary.objectForKey(this._keys[i])) return NO;[39;49;00m$
   358^I[37m        [39;49;00m$
   359^I[37m        return YES;[39;49;00m$
   360^I[37m    }[39;49;00m$
   361^I[37m    [39;49;00m$
   362^I[37m    Instance.allKeys()[39;49;00m$
   363^I[37m    {[39;49;00m$
   364^I[37m        return this._keys;[39;49;00m$
   365^I[37m    }[39;49;00m$
   366^I[37m    [39;49;00m$
   367^I[37m    Instance.allKeysForObject(anObject)[39;49;00m$
   368^I[37m    {[39;49;00m$
   369^I[37m        var i= 0,[39;49;00m$
   370^I[37m            keys= CPArray.array(),[39;49;00m$
   371^I[37m            count= this.count();[39;49;00m$
   372^I[37m        [39;49;00m$
   373^I[37m        while((i= this._objects.indexOfObjectInRage(0, count-i))!=CPNotFound) keys.addObject(this._keys[i]);[39;49;00m$
   374^I[37m        [39;49;00m$
   375^I[37m        return keys;[39;49;00m$
   376^I[37m    }[39;49;00m$
   377^I[37m    [39;49;00m$
   378^I[37m    Instance.allValues()[39;49;00m$
   379^I[37m    {[39;49;00m$
   380^I[37m        return this._objects;[39;49;00m$
   381^I[37m    }[39;49;00m$
   382^I[37m    [39;49;00m$
   383^I[37m    Instance.keyEnumerator()[39;49;00m$
   384^I[37m    {[39;49;00m$
   385^I[37m        return this._keys.objectEnumerator();[39;49;00m$
   386^I[37m    }[39;49;00m$
   387^I[37m    [39;49;00m$
   388^I[37m    Instance.keysSortedByValueUsingSelector(aSelector)[39;49;00m$
   389^I[37m    {[39;49;00m$
   390^I[37m        var dictionary= this,[39;49;00m$
   391^I[37m            objectSelector= function(rhs)[39;49;00m$
   392^I[37m            {[39;49;00m$
   393^I[37m                return aSelector.apply(dictionary.objectForKey(this), [dictionary.objectForKey(rhs)]);[39;49;00m$
   394^I[37m            };[39;49;00m$
   395^I[37m        [39;49;00m$
   396^I[37m        return this._keys.sortedArrayUsingSelector(objectSelector);[39;49;00m$
   397^I[37m    }[39;49;00m$
   398^I[37m    [39;49;00m$
   399^I[37m    Instance.objectEnumerator()[39;49;00m$
   400^I[37m    {[39;49;00m$
   401^I[37m        return this._objects.objectEnumerator();[39;49;00m$
   402^I[37m    }[39;49;00m$
   403^I[37m*/[39;49;00m[37m[39;49;00m$
   404^I[37m/*![39;49;00m$
   405^I[37m    Returns the object for the entry with key \c aKey.[39;49;00m$
   406^I[37m    @param aKey the key for the object's entry[39;49;00m$
   407^I[37m    @return the object for the entry[39;49;00m$
   408^I[37m*/[39;49;00m[37m[39;49;00m$
   409^I-[37m [39;49;00m([36mid[39;49;00m)[32mobjectForKey:[39;49;00m([36mCPString[39;49;00m)aKey[37m[39;49;00m$
   410^I{[37m[39;49;00m$
   411^I[37m    [39;49;00m[34mvar[39;49;00m[37m [39;49;00mobject[37m [39;49;00m=[37m [39;49;00m_buckets[aKey];[37m[39;49;00m$
   412^I[37m    [39;49;00m$
   413^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m(object[37m [39;49;00m===[37m [39;49;00m[34mundefined[39;49;00m)[37m [39;49;00m?[37m [39;49;00m[34mnil[39;49;00m[37m [39;49;00m:[37m [39;49;00mobject;[37m[39;49;00m$
   414^I}[37m[39;49;00m$
   415^I[37m/*[39;49;00m$
   416^I[37m    Instance.objectsForKeys(keys, aNotFoundMarker)[39;49;00m$
   417^I[37m    {[39;49;00m$
   418^I[37m        var i= keys.length,[39;49;00m$
   419^I[37m            objects= CPArray.array();[39;49;00m$
   420^I[37m        [39;49;00m$
   421^I[37m        while(i--)[39;49;00m$
   422^I[37m        {[39;49;00m$
   423^I[37m            var object= this.objectForKey(keys[i]);[39;49;00m$
   424^I[37m            objects.addObject(object==nil?aNotFoundMarker:object);[39;49;00m$
   425^I[37m        }[39;49;00m$
   426^I[37m        [39;49;00m$
   427^I[37m        return objects;[39;49;00m$
   428^I[37m    }[39;49;00m$
   429^I[37m    [39;49;00m$
   430^I[37m    Instance.valueForKey(aKey)[39;49;00m$
   431^I[37m    {[39;49;00m$
   432^I[37m        if(aKey.length && aKey[0]=="@") return this.objectForKey(aKey.substr(1));[39;49;00m$
   433^I[37m        [39;49;00m$
   434^I[37m        return base.valueForKey(aKey);[39;49;00m$
   435^I[37m    }[39;49;00m$
   436^I[37m    [39;49;00m$
   437^I[37m    //[39;49;00m$
   438^I[37m    [39;49;00m$
   439^I[37m    Instance.addEntriesFromDictionary(aDictionary)[39;49;00m$
   440^I[37m    {[39;49;00m$
   441^I[37m        var key,[39;49;00m$
   442^I[37m            keyEnumerator= aDictionary.keyEnumerator();[39;49;00m$
   443^I[37m[39;49;00m$
   444^I[37m        while(key= keyEnumerator.nextObject()) this.setObjectForKey(aDictionary.objectForKey(key), key);[39;49;00m$
   445^I[37m    }[39;49;00m$
   446^I[37m*/[39;49;00m[37m[39;49;00m$
   447^I[37m/*![39;49;00m$
   448^I[37m    Removes all the entries from the dictionary.[39;49;00m$
   449^I[37m*/[39;49;00m[37m[39;49;00m$
   450^I-[37m [39;49;00m([36mvoid[39;49;00m)[32mremoveAllObjects[39;49;00m[37m[39;49;00m$
   451^I{[37m[39;49;00m$
   452^I[37m    [39;49;00m_keys[37m [39;49;00m=[37m [39;49;00m[];[37m[39;49;00m$
   453^I[37m    [39;49;00mcount[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   454^I[37m    [39;49;00m_buckets[37m [39;49;00m=[37m [39;49;00m{};[37m[39;49;00m$
   455^I}[37m[39;49;00m$
   456^I[37m[39;49;00m$
   457^I[37m/*![39;49;00m$
   458^I[37m    Removes the entry for the specified key.[39;49;00m$
   459^I[37m    @param aKey the key of the entry to be removed[39;49;00m$
   460^I[37m*/[39;49;00m[37m[39;49;00m$
   461^I-[37m [39;49;00m([36mvoid[39;49;00m)[32mremoveObjectForKey:[39;49;00m([36mid[39;49;00m)aKey[37m[39;49;00m$
   462^I{[37m[39;49;00m$
   463^I[37m    [39;49;00m[32mdictionary_removeValue[39;49;00m([36mself[39;49;00m,[37m [39;49;00maKey);[37m[39;49;00m$
   464^I}[37m[39;49;00m$
   465^I[37m[39;49;00m$
   466^I[37m/*![39;49;00m$
   467^I[37m    Removes each entry in allKeys from the receiver.[39;49;00m$
   468^I[37m    @param allKeys an array of keys that will be removed from the dictionary[39;49;00m$
   469^I[37m*/[39;49;00m[37m[39;49;00m$
   470^I-[37m [39;49;00m([36mvoid[39;49;00m)[32mremoveObjectsForKeys:[39;49;00m([36mCPArray[39;49;00m)allKeys[37m[39;49;00m$
   471^I{[37m[39;49;00m$
   472^I[37m    [39;49;00m[34mvar[39;49;00m[37m [39;49;00mindex[37m [39;49;00m=[37m [39;49;00mallKeys.length;[37m[39;49;00m$
   473^I[37m[39;49;00m$
   474^I[37m    [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(index--)[37m[39;49;00m$
   475^I[37m        [39;49;00m[32mdictionary_removeValue[39;49;00m([36mself[39;49;00m,[37m [39;49;00mallKeys[index]);[37m[39;49;00m$
   476^I}[37m[39;49;00m$
   477^I[37m[39;49;00m$
   478^I[37m/*[39;49;00m$
   479^I[37m    Instance.removeObjectForKey(aKey)[39;49;00m$
   480^I[37m    {[39;49;00m$
   481^I[37m        var entry= this._dictionary[aKey];[39;49;00m$
   482^I[37m        [39;49;00m$
   483^I[37m        if(entry)[39;49;00m$
   484^I[37m        {[39;49;00m$
   485^I[37m            var range= CPMakeRange(entry.index, 1);[39;49;00m$
   486^I[37m            [39;49;00m$
   487^I[37m            this._keys.removeObjectsInRange(range);[39;49;00m$
   488^I[37m            this._objects.removeObjectsInRange(range);[39;49;00m$
   489^I[37m        [39;49;00m$
   490^I[37m            delete this._dictionary[aKey];[39;49;00m$
   491^I[37m        }[39;49;00m$
   492^I[37m    }[39;49;00m$
   493^I[37m    [39;49;00m$
   494^I[37m    Instance.setDictionary(aDictionary)[39;49;00m$
   495^I[37m    {[39;49;00m$
   496^I[37m        this._keys= CPArray.arrayWithArray(aDictionary.allKeys());[39;49;00m$
   497^I[37m        this._objects= CPArray.arrayWithArray(aDictionary.allValues());[39;49;00m$
   498^I[37m        [39;49;00m$
   499^I[37m        this._dictionary= { };[39;49;00m$
   500^I[37m        [39;49;00m$
   501^I[37m        var i= this._keys.count();[39;49;00m$
   502^I[37m        while(i--) this._dictionary[this._keys[i]]= { object: this._objects[i], index: i };[39;49;00m$
   503^I[37m    }[39;49;00m$
   504^I[37m*/[39;49;00m[37m[39;49;00m$
   505^I[37m/*![39;49;00m$
   506^I[37m    Adds an entry into the dictionary.[39;49;00m$
   507^I[37m    @param anObject the object for the entry[39;49;00m$
   508^I[37m    @param aKey the entry's key[39;49;00m$
   509^I[37m*/[39;49;00m[37m[39;49;00m$
   510^I-[37m [39;49;00m([36mvoid[39;49;00m)[32msetObject:[39;49;00m([36mid[39;49;00m)anObject[37m [39;49;00m[32mforKey:[39;49;00m([36mid[39;49;00m)aKey[37m[39;49;00m$
   511^I{[37m[39;49;00m$
   512^I[37m    [39;49;00m[32mdictionary_setValue[39;49;00m([36mself[39;49;00m,[37m [39;49;00maKey,[37m [39;49;00manObject);[37m[39;49;00m$
   513^I}[37m[39;49;00m$
   514^I[37m/*[39;49;00m$
   515^I[37m    Instance.setValueForKey(aValue, aKey)[39;49;00m$
   516^I[37m    {[39;49;00m$
   517^I[37m        if(!aValue) this.removeObjectForKey(aKey);[39;49;00m$
   518^I[37m        else this.setObjectForKey(aValue, aKey);[39;49;00m$
   519^I[37m    }[39;49;00m$
   520^I[37m    [39;49;00m$
   521^I[37m    Instance.copy()[39;49;00m$
   522^I[37m    {[39;49;00m$
   523^I[37m        return CPDictionary.alloc().dictionaryWithDictionary(this);[39;49;00m$
   524^I[37m    }[39;49;00m$
   525^I[37m*/[39;49;00m[37m[39;49;00m$
   526^I[37m[39;49;00m$
   527^I[37m/*![39;49;00m$
   528^I[37m    Take all the key/value pairs in aDictionary and apply them to this dictionary.[39;49;00m$
   529^I[37m*/[39;49;00m[37m[39;49;00m$
   530^I-[37m [39;49;00m([36mvoid[39;49;00m)[32maddEntriesFromDictionary:[39;49;00m([36mCPDictionary[39;49;00m)aDictionary[37m[39;49;00m$
   531^I{[37m[39;49;00m$
   532^I[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!aDictionary)[37m[39;49;00m$
   533^I[37m        [39;49;00m[34mreturn[39;49;00m;[37m[39;49;00m$
   534^I[37m        [39;49;00m$
   535^I[37m    [39;49;00m[34mvar[39;49;00m[37m [39;49;00mkeys[37m [39;49;00m=[37m [39;49;00m[aDictionary[37m [39;49;00mallKeys],[37m[39;49;00m$
   536^I[37m        [39;49;00mindex[37m [39;49;00m=[37m [39;49;00m[keys[37m [39;49;00mcount];[37m[39;49;00m$
   537^I[37m    [39;49;00m$
   538^I[37m    [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(index--)[37m[39;49;00m$
   539^I[37m    [39;49;00m{[37m[39;49;00m$
   540^I[37m        [39;49;00m[34mvar[39;49;00m[37m [39;49;00mkey[37m [39;49;00m=[37m [39;49;00mkeys[index];[37m[39;49;00m$
   541^I[37m[39;49;00m$
   542^I[37m        [39;49;00m[[36mself[39;49;00m[37m [39;49;00msetObject:[aDictionary[37m [39;49;00mobjectForKey:key][37m [39;49;00mforKey:key];[37m[39;49;00m$
   543^I[37m    [39;49;00m}[37m[39;49;00m$
   544^I}[37m[39;49;00m$
   545^I[37m[39;49;00m$
   546^I[37m/*![39;49;00m$
   547^I[37m    Returns a human readable description of the dictionary.[39;49;00m$
   548^I[37m*/[39;49;00m[37m[39;49;00m$
   549^I-[37m [39;49;00m([36mCPString[39;49;00m)[32mdescription[39;49;00m[37m[39;49;00m$
   550^I{[37m[39;49;00m$
   551^I[37m    [39;49;00m[34mvar[39;49;00m[37m [39;49;00mdescription[37m [39;49;00m=[37m [39;49;00m[33m@"[39;49;00m[33mCPDictionary {[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
   552^I[37m    [39;49;00m$
   553^I[37m    [39;49;00m[34mvar[39;49;00m[37m [39;49;00mi[37m [39;49;00m=[37m [39;49;00m_keys.length;[37m[39;49;00m$
   554^I[37m    [39;49;00m$
   555^I[37m    [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(i--)[37m[39;49;00m$
   556^I[37m    [39;49;00m{[37m[39;49;00m$
   557^I[37m        [39;49;00mdescription[37m [39;49;00m+=[37m [39;49;00m_keys[i][37m [39;49;00m+[37m [39;49;00m[33m"[39;49;00m[33m:[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
   558^I[37m[39;49;00m$
   559^I[37m        [39;49;00m[34mvar[39;49;00m[37m [39;49;00mobject[37m [39;49;00m=[37m [39;49;00m_buckets[_keys[i]];[37m[39;49;00m$
   560^I[37m[39;49;00m$
   561^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(object[37m [39;49;00m&&[37m [39;49;00mobject.isa)[37m[39;49;00m$
   562^I[37m            [39;49;00mdescription[37m [39;49;00m+=[37m [39;49;00m[object[37m [39;49;00mdescription];[37m[39;49;00m$
   563^I[37m        [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
   564^I[37m            [39;49;00mdescription[37m [39;49;00m+=[37m [39;49;00mobject;[37m[39;49;00m$
   565^I[37m[39;49;00m$
   566^I[37m        [39;49;00mdescription[37m [39;49;00m+=[37m [39;49;00m[33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
   567^I[37m    [39;49;00m}[37m[39;49;00m$
   568^I[37m[39;49;00m$
   569^I[37m    [39;49;00mdescription[37m [39;49;00m+=[37m [39;49;00m[33m"[39;49;00m[33m}[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
   570^I[37m[39;49;00m$
   571^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mdescription;[37m[39;49;00m$
   572^I}[37m[39;49;00m$
   573^I[37m[39;49;00m$
   574^I[34m@end[39;49;00m[37m[39;49;00m$
   575^I[37m[39;49;00m$
   576^I[34m@implementation[39;49;00m[37m [39;49;00m[04m[32mCPDictionary[39;49;00m[37m [39;49;00m(CPCoding)[37m[39;49;00m$
   577^I[37m[39;49;00m$
   578^I[37m/*[39;49;00m$
   579^I[37m    Initializes the dictionary by unarchiving the data from a coder.[39;49;00m$
   580^I[37m    @param aCoder the coder from which the data will be unarchived.[39;49;00m$
   581^I[37m    @return the initialized dictionary[39;49;00m$
   582^I[37m*/[39;49;00m[37m[39;49;00m$
   583^I-[37m [39;49;00m([36mid[39;49;00m)[32minitWithCoder:[39;49;00m([36mCPCoder[39;49;00m)aCoder[37m[39;49;00m$
   584^I{[37m[39;49;00m$
   585^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[aCoder[37m [39;49;00m_decodeDictionaryOfObjectsForKey:[33m@"[39;49;00m[33mCP.objects[39;49;00m[33m"[39;49;00m];[37m[39;49;00m$
   586^I}[37m[39;49;00m$
   587^I[37m[39;49;00m$
   588^I[37m/*![39;49;00m$
   589^I[37m    Archives the dictionary to a provided coder.[39;49;00m$
   590^I[37m    @param aCoder the coder to which the dictionary data will be archived.[39;49;00m$
   591^I[37m*/[39;49;00m[37m[39;49;00m$
   592^I-[37m [39;49;00m([36mvoid[39;49;00m)[32mencodeWithCoder:[39;49;00m([36mCPCoder[39;49;00m)aCoder[37m[39;49;00m$
   593^I{[37m[39;49;00m$
   594^I[37m    [39;49;00m[aCoder[37m [39;49;00m_encodeDictionaryOfObjects:[36mself[39;49;00m[37m [39;49;00mforKey:[33m@"[39;49;00m[33mCP.objects[39;49;00m[33m"[39;49;00m];[37m[39;49;00m$
   595^I}[37m[39;49;00m$
   596^I[37m[39;49;00m$
   597^I[34m@end[39;49;00m[37m[39;49;00m$
   598^I[37m[39;49;00m$
   599^I[37m/*![39;49;00m$
   600^I[37m    @class CPMutableDictionary[39;49;00m$
   601^I[37m    @ingroup compatability[39;49;00m$
   602^I[37m[39;49;00m$
   603^I[37m    This class is just an empty subclass of CPDictionary.[39;49;00m$
   604^I[37m    CPDictionary already implements mutable methods and[39;49;00m$
   605^I[37m    this class only exists for source compatability.[39;49;00m$
   606^I[37m*/[39;49;00m[37m[39;49;00m$
   607^I[34m@implementation[39;49;00m[37m [39;49;00m[04m[32mCPMutableDictionary[39;49;00m[37m [39;49;00m:[37m [39;49;00m[04m[32mCPDictionary[39;49;00m[37m[39;49;00m$
   608^I[37m[39;49;00m$
   609^I[34m@end[39;49;00m[37m[39;49;00m$
   610^I[37m[39;49;00m$
   611^Iobjj_dictionary.[34mprototype[39;49;00m.isa[37m [39;49;00m=[37m [39;49;00mCPDictionary;$

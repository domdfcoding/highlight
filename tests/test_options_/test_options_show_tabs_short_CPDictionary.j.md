[37m/*[39;49;00m
[37m * CPDictionary.j[39;49;00m
[37m * Foundation[39;49;00m
[37m *[39;49;00m
[37m * Created by Francisco Tolmasky.[39;49;00m
[37m * Copyright 2008, 280 North, Inc.[39;49;00m
[37m *[39;49;00m
[37m * This library is free software; you can redistribute it and/or[39;49;00m
[37m * modify it under the terms of the GNU Lesser General Public[39;49;00m
[37m * License as published by the Free Software Foundation; either[39;49;00m
[37m * version 2.1 of the License, or (at your option) any later version.[39;49;00m
[37m *[39;49;00m
[37m * This library is distributed in the hope that it will be useful,[39;49;00m
[37m * but WITHOUT ANY WARRANTY; without even the implied warranty of[39;49;00m
[37m * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU[39;49;00m
[37m * Lesser General Public License for more details.[39;49;00m
[37m *[39;49;00m
[37m * You should have received a copy of the GNU Lesser General Public[39;49;00m
[37m * License along with this library; if not, write to the Free Software[39;49;00m
[37m * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA[39;49;00m
[37m */[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m//@import "CPRange.j"[39;49;00m
[36m@import[39;49;00m[37m [39;49;00m[33m"CPObject.j"[39;49;00m[37m[39;49;00m
[36m@import[39;49;00m[37m [39;49;00m[33m"CPEnumerator.j"[39;49;00m[37m[39;49;00m
[36m@import[39;49;00m[37m [39;49;00m[33m"CPException.j"[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m/* @ignore */[39;49;00m[37m[39;49;00m
[34m@implementation[39;49;00m[37m [39;49;00m[04m[32m_CPDictionaryValueEnumerator[39;49;00m[37m [39;49;00m:[37m [39;49;00m[04m[32mCPEnumerator[39;49;00m[37m[39;49;00m
{[37m[39;49;00m
[37m    [39;49;00mCPEnumerator[37m    [39;49;00m_keyEnumerator;[37m[39;49;00m
[37m    [39;49;00mCPDictionary[37m    [39;49;00m_dictionary;[37m[39;49;00m
}[37m[39;49;00m
[37m[39;49;00m
-[37m [39;49;00m([36mid[39;49;00m)[32minitWithDictionary:[39;49;00m([36mCPDictionary[39;49;00m)aDictionary[37m[39;49;00m
{[37m[39;49;00m
[37m    [39;49;00m[36mself[39;49;00m[37m [39;49;00m=[37m [39;49;00m[[36msuper[39;49;00m[37m [39;49;00minit];[37m[39;49;00m
[37m    [39;49;00m
[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m([36mself[39;49;00m)[37m[39;49;00m
[37m    [39;49;00m{[37m[39;49;00m
[37m        [39;49;00m_keyEnumerator[37m [39;49;00m=[37m [39;49;00m[aDictionary[37m [39;49;00mkeyEnumerator];[37m[39;49;00m
[37m        [39;49;00m_dictionary[37m [39;49;00m=[37m [39;49;00maDictionary;[37m[39;49;00m
[37m    [39;49;00m}[37m[39;49;00m
[37m    [39;49;00m
[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[36mself[39;49;00m;[37m[39;49;00m
}[37m[39;49;00m
[37m[39;49;00m
-[37m [39;49;00m([36mid[39;49;00m)[32mnextObject[39;49;00m[37m[39;49;00m
{[37m[39;49;00m
[37m    [39;49;00m[34mvar[39;49;00m[37m [39;49;00mkey[37m [39;49;00m=[37m [39;49;00m[_keyEnumerator[37m [39;49;00mnextObject];[37m[39;49;00m
[37m    [39;49;00m
[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!key)[37m[39;49;00m
[37m        [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mnil[39;49;00m;[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[_dictionary[37m [39;49;00mobjectForKey:key];[37m[39;49;00m
}[37m[39;49;00m
[37m[39;49;00m
[34m@end[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m/*! [39;49;00m
[37m    @class CPDictionary[39;49;00m
[37m    @ingroup foundation[39;49;00m
[37m    @brief A mutable key-value pair collection.[39;49;00m
[37m[39;49;00m
[37m    A dictionary is the standard way of passing around key-value pairs in[39;49;00m
[37m    the Cappuccino framework. It is similar to the[39;49;00m
[37m    <a href="http://java.sun.com/javase/6/docs/api/index.html">Java map interface</a>,[39;49;00m
[37m    except all keys are CPStrings and values can be any[39;49;00m
[37m    Cappuccino or JavaScript object.[39;49;00m
[37m[39;49;00m
[37m    If you are familiar with dictionaries in Cocoa, you'll notice that[39;49;00m
[37m    there is no CPMutableDictionary class. The regular CPDictionary[39;49;00m
[37m    has \c -setObject:forKey: and \c -removeObjectForKey: methods.[39;49;00m
[37m    In Cappuccino there is no distinction between immutable and mutable classes.[39;49;00m
[37m    They are all mutable.[39;49;00m
[37m*/[39;49;00m[37m[39;49;00m
[34m@implementation[39;49;00m[37m [39;49;00m[04m[32mCPDictionary[39;49;00m[37m [39;49;00m:[37m [39;49;00m[04m[32mCPObject[39;49;00m[37m[39;49;00m
{[37m[39;49;00m
}[37m[39;49;00m
[37m[39;49;00m
[37m/*[39;49;00m
[37m    @ignore[39;49;00m
[37m*/[39;49;00m[37m[39;49;00m
+[37m [39;49;00m([36mid[39;49;00m)[32malloc[39;49;00m[37m[39;49;00m
{[37m[39;49;00m
[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00m[32mobjj_dictionary[39;49;00m();[37m[39;49;00m
}[37m[39;49;00m
[37m[39;49;00m
[37m/*![39;49;00m
[37m    Returns a new empty CPDictionary.[39;49;00m
[37m*/[39;49;00m[37m[39;49;00m
+[37m [39;49;00m([36mid[39;49;00m)[32mdictionary[39;49;00m[37m[39;49;00m
{[37m[39;49;00m
[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[[[36mself[39;49;00m[37m [39;49;00malloc][37m [39;49;00minit];[37m[39;49;00m
}[37m[39;49;00m
[37m[39;49;00m
[37m/*![39;49;00m
[37m    Returns a new dictionary, initialized with the contents of \c aDictionary.[39;49;00m
[37m    @param aDictionary the dictionary to copy key-value pairs from[39;49;00m
[37m    @return the new CPDictionary[39;49;00m
[37m*/[39;49;00m[37m[39;49;00m
+[37m [39;49;00m([36mid[39;49;00m)[32mdictionaryWithDictionary:[39;49;00m([36mCPDictionary[39;49;00m)aDictionary[37m[39;49;00m
{[37m[39;49;00m
[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[[[36mself[39;49;00m[37m [39;49;00malloc][37m [39;49;00minitWithDictionary:aDictionary];[37m[39;49;00m
}[37m[39;49;00m
[37m[39;49;00m
[37m/*![39;49;00m
[37m    Creates a new dictionary with single key-value pair.[39;49;00m
[37m    @param anObject the object for the paring[39;49;00m
[37m    @param aKey the key for the pairing[39;49;00m
[37m    @return the new CPDictionary[39;49;00m
[37m*/[39;49;00m[37m[39;49;00m
+[37m [39;49;00m([36mid[39;49;00m)[32mdictionaryWithObject:[39;49;00m([36mid[39;49;00m)anObject[37m [39;49;00m[32mforKey:[39;49;00m([36mid[39;49;00m)aKey[37m[39;49;00m
{[37m[39;49;00m
[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[[[36mself[39;49;00m[37m [39;49;00malloc][37m [39;49;00minitWithObjects:[anObject][37m [39;49;00mforKeys:[aKey]];[37m[39;49;00m
}[37m[39;49;00m
[37m[39;49;00m
[37m/*![39;49;00m
[37m    Creates a dictionary with multiple key-value pairs.[39;49;00m
[37m    @param objects the objects to place in the dictionary[39;49;00m
[37m    @param keys the keys for each of the objects[39;49;00m
[37m    @throws CPInvalidArgumentException if the number of objects and keys is different[39;49;00m
[37m    @return the new CPDictionary[39;49;00m
[37m*/[39;49;00m[37m[39;49;00m
+[37m [39;49;00m([36mid[39;49;00m)[32mdictionaryWithObjects:[39;49;00m([36mCPArray[39;49;00m)objects[37m [39;49;00m[32mforKeys:[39;49;00m([36mCPArray[39;49;00m)keys[37m[39;49;00m
{[37m[39;49;00m
[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[[[36mself[39;49;00m[37m [39;49;00malloc][37m [39;49;00minitWithObjects:objects[37m [39;49;00mforKeys:keys];[37m[39;49;00m
}[37m[39;49;00m
[37m[39;49;00m
[37m/*![39;49;00m
[37m    Creates a dictionary with multiple key-value pairs.[39;49;00m
[37m    @param JavaScript object[39;49;00m
[37m    @return the new CPDictionary[39;49;00m
[37m*/[39;49;00m[37m[39;49;00m
+[37m [39;49;00m([36mid[39;49;00m)[32mdictionaryWithJSObject:[39;49;00m([36mJSObject[39;49;00m)object[37m[39;49;00m
{[37m[39;49;00m
[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[[36mself[39;49;00m[37m [39;49;00mdictionaryWithJSObject:object[37m [39;49;00mrecursively:[34mNO[39;49;00m];[37m[39;49;00m
}[37m[39;49;00m
[37m[39;49;00m
[37m/*![39;49;00m
[37m    Creates a dictionary with multiple key-value pairs, recursively.[39;49;00m
[37m    @param JavaScript object[39;49;00m
[37m    @return the new CPDictionary[39;49;00m
[37m*/[39;49;00m[37m[39;49;00m
+[37m [39;49;00m([36mid[39;49;00m)[32mdictionaryWithJSObject:[39;49;00m([36mJSObject[39;49;00m)object[37m [39;49;00m[32mrecursively:[39;49;00m([36mBOOL[39;49;00m)recursively[37m[39;49;00m
{[37m[39;49;00m
[37m    [39;49;00m[34mvar[39;49;00m[37m [39;49;00mdictionary[37m [39;49;00m=[37m [39;49;00m[[[36mself[39;49;00m[37m [39;49;00malloc][37m [39;49;00minit];[37m[39;49;00m
[37m        [39;49;00m
[37m    [39;49;00m[34mfor[39;49;00m[37m [39;49;00m([34mvar[39;49;00m[37m [39;49;00mkey[37m [39;49;00m[34min[39;49;00m[37m [39;49;00mobject)[37m[39;49;00m
[37m    [39;49;00m{[37m[39;49;00m
[37m        [39;49;00m[34mvar[39;49;00m[37m [39;49;00mvalue[37m [39;49;00m=[37m [39;49;00mobject[key];[37m[39;49;00m
[37m    [39;49;00m
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(recursively[37m [39;49;00m&&[37m [39;49;00mvalue.constructor[37m [39;49;00m===[37m [39;49;00m[36mObject[39;49;00m)[37m[39;49;00m
[37m            [39;49;00mvalue[37m [39;49;00m=[37m [39;49;00m[CPDictionary[37m [39;49;00mdictionaryWithJSObject:value[37m [39;49;00mrecursively:[34mYES[39;49;00m];[37m[39;49;00m
[37m    [39;49;00m
[37m        [39;49;00m[dictionary[37m [39;49;00msetObject:value[37m [39;49;00mforKey:key];[37m[39;49;00m
[37m    [39;49;00m}[37m[39;49;00m
[37m    [39;49;00m
[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mdictionary;[37m[39;49;00m
}[37m[39;49;00m
[37m[39;49;00m
[37m/*![39;49;00m
[37m    Creates and returns a dictionary constructed by a given pairs of keys and values.[39;49;00m
[37m    @param firstObject first object value[39;49;00m
[37m    @param ... key for the first object and ongoing value-key pairs for more objects.[39;49;00m
[37m    @throws CPInvalidArgumentException if the number of objects and keys is different[39;49;00m
[37m    @return the new CPDictionary[39;49;00m
[37m    [39;49;00m
[37m    Assuming that there's no object retaining in Cappuccino, you can create[39;49;00m
[37m    dictionaries same way as with alloc and initWithObjectsAndKeys:[39;49;00m
[37m    var dict = [CPDictionary dictionaryWithObjectsAndKeys:[39;49;00m
[37m    @"value1", @"key1",[39;49;00m
[37m    @"value2", @"key2"];[39;49;00m
[37m    [39;49;00m
[37m    Note, that there's no final nil like in Objective-C/Cocoa.[39;49;00m
[37m    [39;49;00m
[37m    @see [CPDictionary initWithObjectsAndKeys:][39;49;00m
[37m*/[39;49;00m[37m[39;49;00m
+[37m [39;49;00m([36mid[39;49;00m)[32mdictionaryWithObjectsAndKeys:[39;49;00m([36mid[39;49;00m)firstObject,[37m [39;49;00m...[37m[39;49;00m
{[37m[39;49;00m
[37m    [39;49;00marguments[[34m0[39;49;00m][37m [39;49;00m=[37m [39;49;00m[[36mself[39;49;00m[37m [39;49;00malloc];[37m[39;49;00m
[37m    [39;49;00marguments[[34m1[39;49;00m][37m [39;49;00m=[37m [39;49;00m[34m@selector[39;49;00m(initWithObjectsAndKeys:);[37m[39;49;00m
[37m    [39;49;00m
[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mobjj_msgSend.[32mapply[39;49;00m([36mthis[39;49;00m,[37m [39;49;00marguments);[37m[39;49;00m
}[37m[39;49;00m
[37m[39;49;00m
[37m/*![39;49;00m
[37m    Initializes the dictionary with the contents of another dictionary.[39;49;00m
[37m    @param aDictionary the dictionary to copy key-value pairs from[39;49;00m
[37m    @return the initialized dictionary[39;49;00m
[37m*/[39;49;00m[37m[39;49;00m
-[37m [39;49;00m([36mid[39;49;00m)[32minitWithDictionary:[39;49;00m([36mCPDictionary[39;49;00m)aDictionary[37m[39;49;00m
{[37m[39;49;00m
[37m    [39;49;00m[34mvar[39;49;00m[37m [39;49;00mkey[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33m"[39;49;00m,[37m[39;49;00m
[37m        [39;49;00mdictionary[37m [39;49;00m=[37m [39;49;00m[[CPDictionary[37m [39;49;00malloc][37m [39;49;00minit];[37m[39;49;00m
[37m    [39;49;00m
[37m    [39;49;00m[34mfor[39;49;00m[37m [39;49;00m(key[37m [39;49;00m[34min[39;49;00m[37m [39;49;00maDictionary._buckets)[37m[39;49;00m
[37m        [39;49;00m[dictionary[37m [39;49;00msetObject:[aDictionary[37m [39;49;00mobjectForKey:key][37m [39;49;00mforKey:key];[37m[39;49;00m
[37m        [39;49;00m
[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mdictionary;[37m[39;49;00m
}[37m[39;49;00m
[37m[39;49;00m
[37m/*![39;49;00m
[37m    Initializes the dictionary from the arrays of keys and objects.[39;49;00m
[37m    @param objects the objects to put in the dictionary[39;49;00m
[37m    @param keyArray the keys for the objects to put in the dictionary[39;49;00m
[37m    @throws CPInvalidArgumentException if the number of objects and keys is different[39;49;00m
[37m    @return the initialized dictionary[39;49;00m
[37m*/[39;49;00m[37m[39;49;00m
-[37m [39;49;00m([36mid[39;49;00m)[32minitWithObjects:[39;49;00m([36mCPArray[39;49;00m)objects[37m [39;49;00m[32mforKeys:[39;49;00m([36mCPArray[39;49;00m)keyArray[37m[39;49;00m
{[37m[39;49;00m
[37m    [39;49;00m[36mself[39;49;00m[37m [39;49;00m=[37m [39;49;00m[[36msuper[39;49;00m[37m [39;49;00minit];[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m([objects[37m [39;49;00mcount][37m [39;49;00m!=[37m [39;49;00m[keyArray[37m [39;49;00mcount])[37m[39;49;00m
[37m        [39;49;00m[CPException[37m [39;49;00mraise:CPInvalidArgumentException[37m [39;49;00mreason:[33m"[39;49;00m[33mCounts are different.([39;49;00m[33m"[39;49;00m+[objects[37m [39;49;00mcount]+[33m"[39;49;00m[33m!=[39;49;00m[33m"[39;49;00m+[keyArray[37m [39;49;00mcount]+[33m"[39;49;00m[33m)[39;49;00m[33m"[39;49;00m];[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m([36mself[39;49;00m)[37m[39;49;00m
[37m    [39;49;00m{[37m[39;49;00m
[37m        [39;49;00m[34mvar[39;49;00m[37m [39;49;00mi[37m [39;49;00m=[37m [39;49;00m[keyArray[37m [39;49;00mcount];[37m[39;49;00m
[37m        [39;49;00m
[37m        [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(i--)[37m[39;49;00m
[37m            [39;49;00m[[36mself[39;49;00m[37m [39;49;00msetObject:objects[i][37m [39;49;00mforKey:keyArray[i]];[37m[39;49;00m
[37m    [39;49;00m}[37m[39;49;00m
[37m    [39;49;00m
[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[36mself[39;49;00m;[37m[39;49;00m
}[37m[39;49;00m
[37m[39;49;00m
[37m/*![39;49;00m
[37m    Creates and returns a dictionary constructed by a given pairs of keys and values.[39;49;00m
[37m    @param firstObject first object value[39;49;00m
[37m    @param ... key for the first object and ongoing value-key pairs for more objects.[39;49;00m
[37m    @throws CPInvalidArgumentException if the number of objects and keys is different[39;49;00m
[37m    @return the new CPDictionary[39;49;00m
[37m    [39;49;00m
[37m    You can create dictionaries this way:[39;49;00m
[37m    var dict = [[CPDictionary alloc] initWithObjectsAndKeys:[39;49;00m
[37m    @"value1", @"key1",[39;49;00m
[37m    @"value2", @"key2"];[39;49;00m
[37m    [39;49;00m
[37m    Note, that there's no final nil like in Objective-C/Cocoa.[39;49;00m
[37m*/[39;49;00m[37m[39;49;00m
-[37m [39;49;00m([36mid[39;49;00m)[32minitWithObjectsAndKeys:[39;49;00m([36mid[39;49;00m)firstObject,[37m [39;49;00m...[37m[39;49;00m
{[37m[39;49;00m
[37m    [39;49;00m[34mvar[39;49;00m[37m [39;49;00margCount[37m [39;49;00m=[37m [39;49;00marguments.length;[37m[39;49;00m
[37m    [39;49;00m
[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(argCount[37m [39;49;00m%[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m!==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m
[37m        [39;49;00m[CPException[37m [39;49;00mraise:CPInvalidArgumentException[37m [39;49;00mreason:[33m"[39;49;00m[33mKey-value count is mismatched. ([39;49;00m[33m"[39;49;00m[37m [39;49;00m+[37m [39;49;00margCount[37m [39;49;00m+[37m [39;49;00m[33m"[39;49;00m[33m arguments passed)[39;49;00m[33m"[39;49;00m];[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[36mself[39;49;00m[37m [39;49;00m=[37m [39;49;00m[[36msuper[39;49;00m[37m [39;49;00minit];[37m[39;49;00m
[37m    [39;49;00m
[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m([36mself[39;49;00m)[37m[39;49;00m
[37m    [39;49;00m{[37m[39;49;00m
[37m        [39;49;00m[37m// The arguments array contains self and _cmd, so the first object is at position 2.[39;49;00m
[37m        [39;49;00m[34mvar[39;49;00m[37m [39;49;00mindex[37m [39;49;00m=[37m [39;49;00m[34m2[39;49;00m;[37m[39;49;00m
[37m        [39;49;00m
[37m        [39;49;00m[34mfor[39;49;00m(;[37m [39;49;00mindex[37m [39;49;00m<[37m [39;49;00margCount;[37m [39;49;00mindex[37m [39;49;00m+=[37m [39;49;00m[34m2[39;49;00m)[37m[39;49;00m
[37m        [39;49;00m{[37m[39;49;00m
[37m            [39;49;00m[34mvar[39;49;00m[37m [39;49;00mvalue[37m [39;49;00m=[37m [39;49;00marguments[index];[37m[39;49;00m
[37m[39;49;00m
[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(value[37m [39;49;00m===[37m [39;49;00m[34mnil[39;49;00m)[37m[39;49;00m
[37m                [39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m
[37m[39;49;00m
[37m            [39;49;00m[[36mself[39;49;00m[37m [39;49;00msetObject:value[37m [39;49;00mforKey:arguments[index[37m [39;49;00m+[37m [39;49;00m[34m1[39;49;00m]];[37m[39;49;00m
[37m        [39;49;00m}[37m[39;49;00m
[37m    [39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[36mself[39;49;00m;[37m[39;49;00m
}[37m[39;49;00m
[37m[39;49;00m
[37m/*![39;49;00m
[37m    return a copy of the receiver (does not deep copy the objects contained in the dictionary).[39;49;00m
[37m*/[39;49;00m[37m[39;49;00m
-[37m [39;49;00m([36mCPDictionary[39;49;00m)[32mcopy[39;49;00m[37m[39;49;00m
{[37m[39;49;00m
[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[CPDictionary[37m [39;49;00mdictionaryWithDictionary:[36mself[39;49;00m];[37m[39;49;00m
}[37m[39;49;00m
[37m[39;49;00m
[37m/*![39;49;00m
[37m    Returns the number of entries in the dictionary[39;49;00m
[37m*/[39;49;00m[37m[39;49;00m
-[37m [39;49;00m([36mint[39;49;00m)[32mcount[39;49;00m[37m[39;49;00m
{[37m[39;49;00m
[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mcount;[37m[39;49;00m
}[37m[39;49;00m
[37m[39;49;00m
[37m/*![39;49;00m
[37m    Returns an array of keys for all the entries in the dictionary.[39;49;00m
[37m*/[39;49;00m[37m[39;49;00m
-[37m [39;49;00m([36mCPArray[39;49;00m)[32mallKeys[39;49;00m[37m[39;49;00m
{[37m[39;49;00m
[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m_keys;[37m[39;49;00m
}[37m[39;49;00m
[37m[39;49;00m
[37m/*![39;49;00m
[37m    Returns an array of values for all the entries in the dictionary.[39;49;00m
[37m*/[39;49;00m[37m[39;49;00m
-[37m [39;49;00m([36mCPArray[39;49;00m)[32mallValues[39;49;00m[37m[39;49;00m
{[37m[39;49;00m
[37m    [39;49;00m[34mvar[39;49;00m[37m [39;49;00mindex[37m [39;49;00m=[37m [39;49;00m_keys.length,[37m[39;49;00m
[37m        [39;49;00mvalues[37m [39;49;00m=[37m [39;49;00m[];[37m[39;49;00m
[37m        [39;49;00m
[37m    [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(index--)[37m[39;49;00m
[37m        [39;49;00mvalues.[32mpush[39;49;00m([32mdictionary_getValue[39;49;00m([36mself[39;49;00m,[37m [39;49;00m[_keys[index]]));[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mvalues;[37m[39;49;00m
}[37m[39;49;00m
[37m[39;49;00m
[37m/*![39;49;00m
[37m    Returns an enumerator that enumerates over all the dictionary's keys.[39;49;00m
[37m*/[39;49;00m[37m[39;49;00m
-[37m [39;49;00m([36mCPEnumerator[39;49;00m)[32mkeyEnumerator[39;49;00m[37m[39;49;00m
{[37m[39;49;00m
[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[_keys[37m [39;49;00mobjectEnumerator];[37m[39;49;00m
}[37m[39;49;00m
[37m[39;49;00m
[37m/*![39;49;00m
[37m    Returns an enumerator that enumerates over all the dictionary's values.[39;49;00m
[37m*/[39;49;00m[37m[39;49;00m
-[37m [39;49;00m([36mCPEnumerator[39;49;00m)[32mobjectEnumerator[39;49;00m[37m[39;49;00m
{[37m[39;49;00m
[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[[_CPDictionaryValueEnumerator[37m [39;49;00malloc][37m [39;49;00minitWithDictionary:[36mself[39;49;00m];[37m[39;49;00m
}[37m[39;49;00m
[37m[39;49;00m
[37m/*![39;49;00m
[37m    Compare the receiver to this dictionary, and return whether or not they are equal. [39;49;00m
[37m*/[39;49;00m[37m[39;49;00m
-[37m [39;49;00m([36mBOOL[39;49;00m)[32misEqualToDictionary:[39;49;00m([36mCPDictionary[39;49;00m)aDictionary[37m[39;49;00m
{[37m[39;49;00m
[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(count[37m [39;49;00m!==[37m [39;49;00m[aDictionary[37m [39;49;00mcount])[37m[39;49;00m
[37m        [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mNO[39;49;00m;[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[34mvar[39;49;00m[37m [39;49;00mindex[37m [39;49;00m=[37m [39;49;00mcount;[37m[39;49;00m
[37m    [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(index--)[37m[39;49;00m
[37m    [39;49;00m{[37m[39;49;00m
[37m        [39;49;00m[34mvar[39;49;00m[37m [39;49;00mcurrentKey[37m [39;49;00m=[37m [39;49;00m_keys[index],[37m[39;49;00m
[37m            [39;49;00mlhsObject[37m [39;49;00m=[37m [39;49;00m_buckets[currentKey],[37m[39;49;00m
[37m            [39;49;00mrhsObject[37m [39;49;00m=[37m [39;49;00maDictionary._buckets[currentKey];[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(lhsObject[37m [39;49;00m===[37m [39;49;00mrhsObject)[37m[39;49;00m
[37m            [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m
[37m            [39;49;00m
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(lhsObject.isa[37m [39;49;00m&&[37m [39;49;00mrhsObject.isa[37m [39;49;00m&&[37m [39;49;00m[lhsObject[37m [39;49;00mrespondsToSelector:[34m@selector[39;49;00m(isEqual:)][37m [39;49;00m&&[37m [39;49;00m[lhsObject[37m [39;49;00misEqual:rhsObject])[37m[39;49;00m
[37m            [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m
[37m        [39;49;00m
[37m        [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mNO[39;49;00m;[37m[39;49;00m
[37m    [39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mYES[39;49;00m;[37m[39;49;00m
}[37m[39;49;00m
[37m[39;49;00m
[37m/*[39;49;00m
[37m    Instance.isEqualToDictionary(aDictionary)[39;49;00m
[37m    {[39;49;00m
[37m        if(this.count()!=aDictionary.count()) return NO;[39;49;00m
[37m        [39;49;00m
[37m        var i= this._keys.count();[39;49;00m
[37m        while(i--) if(this.objectForKey(this._keys[i])!=aDictionary.objectForKey(this._keys[i])) return NO;[39;49;00m
[37m        [39;49;00m
[37m        return YES;[39;49;00m
[37m    }[39;49;00m
[37m    [39;49;00m
[37m    Instance.allKeys()[39;49;00m
[37m    {[39;49;00m
[37m        return this._keys;[39;49;00m
[37m    }[39;49;00m
[37m    [39;49;00m
[37m    Instance.allKeysForObject(anObject)[39;49;00m
[37m    {[39;49;00m
[37m        var i= 0,[39;49;00m
[37m            keys= CPArray.array(),[39;49;00m
[37m            count= this.count();[39;49;00m
[37m        [39;49;00m
[37m        while((i= this._objects.indexOfObjectInRage(0, count-i))!=CPNotFound) keys.addObject(this._keys[i]);[39;49;00m
[37m        [39;49;00m
[37m        return keys;[39;49;00m
[37m    }[39;49;00m
[37m    [39;49;00m
[37m    Instance.allValues()[39;49;00m
[37m    {[39;49;00m
[37m        return this._objects;[39;49;00m
[37m    }[39;49;00m
[37m    [39;49;00m
[37m    Instance.keyEnumerator()[39;49;00m
[37m    {[39;49;00m
[37m        return this._keys.objectEnumerator();[39;49;00m
[37m    }[39;49;00m
[37m    [39;49;00m
[37m    Instance.keysSortedByValueUsingSelector(aSelector)[39;49;00m
[37m    {[39;49;00m
[37m        var dictionary= this,[39;49;00m
[37m            objectSelector= function(rhs)[39;49;00m
[37m            {[39;49;00m
[37m                return aSelector.apply(dictionary.objectForKey(this), [dictionary.objectForKey(rhs)]);[39;49;00m
[37m            };[39;49;00m
[37m        [39;49;00m
[37m        return this._keys.sortedArrayUsingSelector(objectSelector);[39;49;00m
[37m    }[39;49;00m
[37m    [39;49;00m
[37m    Instance.objectEnumerator()[39;49;00m
[37m    {[39;49;00m
[37m        return this._objects.objectEnumerator();[39;49;00m
[37m    }[39;49;00m
[37m*/[39;49;00m[37m[39;49;00m
[37m/*![39;49;00m
[37m    Returns the object for the entry with key \c aKey.[39;49;00m
[37m    @param aKey the key for the object's entry[39;49;00m
[37m    @return the object for the entry[39;49;00m
[37m*/[39;49;00m[37m[39;49;00m
-[37m [39;49;00m([36mid[39;49;00m)[32mobjectForKey:[39;49;00m([36mCPString[39;49;00m)aKey[37m[39;49;00m
{[37m[39;49;00m
[37m    [39;49;00m[34mvar[39;49;00m[37m [39;49;00mobject[37m [39;49;00m=[37m [39;49;00m_buckets[aKey];[37m[39;49;00m
[37m    [39;49;00m
[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m(object[37m [39;49;00m===[37m [39;49;00m[34mundefined[39;49;00m)[37m [39;49;00m?[37m [39;49;00m[34mnil[39;49;00m[37m [39;49;00m:[37m [39;49;00mobject;[37m[39;49;00m
}[37m[39;49;00m
[37m/*[39;49;00m
[37m    Instance.objectsForKeys(keys, aNotFoundMarker)[39;49;00m
[37m    {[39;49;00m
[37m        var i= keys.length,[39;49;00m
[37m            objects= CPArray.array();[39;49;00m
[37m        [39;49;00m
[37m        while(i--)[39;49;00m
[37m        {[39;49;00m
[37m            var object= this.objectForKey(keys[i]);[39;49;00m
[37m            objects.addObject(object==nil?aNotFoundMarker:object);[39;49;00m
[37m        }[39;49;00m
[37m        [39;49;00m
[37m        return objects;[39;49;00m
[37m    }[39;49;00m
[37m    [39;49;00m
[37m    Instance.valueForKey(aKey)[39;49;00m
[37m    {[39;49;00m
[37m        if(aKey.length && aKey[0]=="@") return this.objectForKey(aKey.substr(1));[39;49;00m
[37m        [39;49;00m
[37m        return base.valueForKey(aKey);[39;49;00m
[37m    }[39;49;00m
[37m    [39;49;00m
[37m    //[39;49;00m
[37m    [39;49;00m
[37m    Instance.addEntriesFromDictionary(aDictionary)[39;49;00m
[37m    {[39;49;00m
[37m        var key,[39;49;00m
[37m            keyEnumerator= aDictionary.keyEnumerator();[39;49;00m
[37m[39;49;00m
[37m        while(key= keyEnumerator.nextObject()) this.setObjectForKey(aDictionary.objectForKey(key), key);[39;49;00m
[37m    }[39;49;00m
[37m*/[39;49;00m[37m[39;49;00m
[37m/*![39;49;00m
[37m    Removes all the entries from the dictionary.[39;49;00m
[37m*/[39;49;00m[37m[39;49;00m
-[37m [39;49;00m([36mvoid[39;49;00m)[32mremoveAllObjects[39;49;00m[37m[39;49;00m
{[37m[39;49;00m
[37m    [39;49;00m_keys[37m [39;49;00m=[37m [39;49;00m[];[37m[39;49;00m
[37m    [39;49;00mcount[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m
[37m    [39;49;00m_buckets[37m [39;49;00m=[37m [39;49;00m{};[37m[39;49;00m
}[37m[39;49;00m
[37m[39;49;00m
[37m/*![39;49;00m
[37m    Removes the entry for the specified key.[39;49;00m
[37m    @param aKey the key of the entry to be removed[39;49;00m
[37m*/[39;49;00m[37m[39;49;00m
-[37m [39;49;00m([36mvoid[39;49;00m)[32mremoveObjectForKey:[39;49;00m([36mid[39;49;00m)aKey[37m[39;49;00m
{[37m[39;49;00m
[37m    [39;49;00m[32mdictionary_removeValue[39;49;00m([36mself[39;49;00m,[37m [39;49;00maKey);[37m[39;49;00m
}[37m[39;49;00m
[37m[39;49;00m
[37m/*![39;49;00m
[37m    Removes each entry in allKeys from the receiver.[39;49;00m
[37m    @param allKeys an array of keys that will be removed from the dictionary[39;49;00m
[37m*/[39;49;00m[37m[39;49;00m
-[37m [39;49;00m([36mvoid[39;49;00m)[32mremoveObjectsForKeys:[39;49;00m([36mCPArray[39;49;00m)allKeys[37m[39;49;00m
{[37m[39;49;00m
[37m    [39;49;00m[34mvar[39;49;00m[37m [39;49;00mindex[37m [39;49;00m=[37m [39;49;00mallKeys.length;[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(index--)[37m[39;49;00m
[37m        [39;49;00m[32mdictionary_removeValue[39;49;00m([36mself[39;49;00m,[37m [39;49;00mallKeys[index]);[37m[39;49;00m
}[37m[39;49;00m
[37m[39;49;00m
[37m/*[39;49;00m
[37m    Instance.removeObjectForKey(aKey)[39;49;00m
[37m    {[39;49;00m
[37m        var entry= this._dictionary[aKey];[39;49;00m
[37m        [39;49;00m
[37m        if(entry)[39;49;00m
[37m        {[39;49;00m
[37m            var range= CPMakeRange(entry.index, 1);[39;49;00m
[37m            [39;49;00m
[37m            this._keys.removeObjectsInRange(range);[39;49;00m
[37m            this._objects.removeObjectsInRange(range);[39;49;00m
[37m        [39;49;00m
[37m            delete this._dictionary[aKey];[39;49;00m
[37m        }[39;49;00m
[37m    }[39;49;00m
[37m    [39;49;00m
[37m    Instance.setDictionary(aDictionary)[39;49;00m
[37m    {[39;49;00m
[37m        this._keys= CPArray.arrayWithArray(aDictionary.allKeys());[39;49;00m
[37m        this._objects= CPArray.arrayWithArray(aDictionary.allValues());[39;49;00m
[37m        [39;49;00m
[37m        this._dictionary= { };[39;49;00m
[37m        [39;49;00m
[37m        var i= this._keys.count();[39;49;00m
[37m        while(i--) this._dictionary[this._keys[i]]= { object: this._objects[i], index: i };[39;49;00m
[37m    }[39;49;00m
[37m*/[39;49;00m[37m[39;49;00m
[37m/*![39;49;00m
[37m    Adds an entry into the dictionary.[39;49;00m
[37m    @param anObject the object for the entry[39;49;00m
[37m    @param aKey the entry's key[39;49;00m
[37m*/[39;49;00m[37m[39;49;00m
-[37m [39;49;00m([36mvoid[39;49;00m)[32msetObject:[39;49;00m([36mid[39;49;00m)anObject[37m [39;49;00m[32mforKey:[39;49;00m([36mid[39;49;00m)aKey[37m[39;49;00m
{[37m[39;49;00m
[37m    [39;49;00m[32mdictionary_setValue[39;49;00m([36mself[39;49;00m,[37m [39;49;00maKey,[37m [39;49;00manObject);[37m[39;49;00m
}[37m[39;49;00m
[37m/*[39;49;00m
[37m    Instance.setValueForKey(aValue, aKey)[39;49;00m
[37m    {[39;49;00m
[37m        if(!aValue) this.removeObjectForKey(aKey);[39;49;00m
[37m        else this.setObjectForKey(aValue, aKey);[39;49;00m
[37m    }[39;49;00m
[37m    [39;49;00m
[37m    Instance.copy()[39;49;00m
[37m    {[39;49;00m
[37m        return CPDictionary.alloc().dictionaryWithDictionary(this);[39;49;00m
[37m    }[39;49;00m
[37m*/[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m/*![39;49;00m
[37m    Take all the key/value pairs in aDictionary and apply them to this dictionary.[39;49;00m
[37m*/[39;49;00m[37m[39;49;00m
-[37m [39;49;00m([36mvoid[39;49;00m)[32maddEntriesFromDictionary:[39;49;00m([36mCPDictionary[39;49;00m)aDictionary[37m[39;49;00m
{[37m[39;49;00m
[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!aDictionary)[37m[39;49;00m
[37m        [39;49;00m[34mreturn[39;49;00m;[37m[39;49;00m
[37m        [39;49;00m
[37m    [39;49;00m[34mvar[39;49;00m[37m [39;49;00mkeys[37m [39;49;00m=[37m [39;49;00m[aDictionary[37m [39;49;00mallKeys],[37m[39;49;00m
[37m        [39;49;00mindex[37m [39;49;00m=[37m [39;49;00m[keys[37m [39;49;00mcount];[37m[39;49;00m
[37m    [39;49;00m
[37m    [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(index--)[37m[39;49;00m
[37m    [39;49;00m{[37m[39;49;00m
[37m        [39;49;00m[34mvar[39;49;00m[37m [39;49;00mkey[37m [39;49;00m=[37m [39;49;00mkeys[index];[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[[36mself[39;49;00m[37m [39;49;00msetObject:[aDictionary[37m [39;49;00mobjectForKey:key][37m [39;49;00mforKey:key];[37m[39;49;00m
[37m    [39;49;00m}[37m[39;49;00m
}[37m[39;49;00m
[37m[39;49;00m
[37m/*![39;49;00m
[37m    Returns a human readable description of the dictionary.[39;49;00m
[37m*/[39;49;00m[37m[39;49;00m
-[37m [39;49;00m([36mCPString[39;49;00m)[32mdescription[39;49;00m[37m[39;49;00m
{[37m[39;49;00m
[37m    [39;49;00m[34mvar[39;49;00m[37m [39;49;00mdescription[37m [39;49;00m=[37m [39;49;00m[33m@"[39;49;00m[33mCPDictionary {[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m;[37m[39;49;00m
[37m    [39;49;00m
[37m    [39;49;00m[34mvar[39;49;00m[37m [39;49;00mi[37m [39;49;00m=[37m [39;49;00m_keys.length;[37m[39;49;00m
[37m    [39;49;00m
[37m    [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(i--)[37m[39;49;00m
[37m    [39;49;00m{[37m[39;49;00m
[37m        [39;49;00mdescription[37m [39;49;00m+=[37m [39;49;00m_keys[i][37m [39;49;00m+[37m [39;49;00m[33m"[39;49;00m[33m:[39;49;00m[33m"[39;49;00m;[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[34mvar[39;49;00m[37m [39;49;00mobject[37m [39;49;00m=[37m [39;49;00m_buckets[_keys[i]];[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(object[37m [39;49;00m&&[37m [39;49;00mobject.isa)[37m[39;49;00m
[37m            [39;49;00mdescription[37m [39;49;00m+=[37m [39;49;00m[object[37m [39;49;00mdescription];[37m[39;49;00m
[37m        [39;49;00m[34melse[39;49;00m[37m[39;49;00m
[37m            [39;49;00mdescription[37m [39;49;00m+=[37m [39;49;00mobject;[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00mdescription[37m [39;49;00m+=[37m [39;49;00m[33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m;[37m[39;49;00m
[37m    [39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00mdescription[37m [39;49;00m+=[37m [39;49;00m[33m"[39;49;00m[33m}[39;49;00m[33m"[39;49;00m;[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mdescription;[37m[39;49;00m
}[37m[39;49;00m
[37m[39;49;00m
[34m@end[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[34m@implementation[39;49;00m[37m [39;49;00m[04m[32mCPDictionary[39;49;00m[37m [39;49;00m(CPCoding)[37m[39;49;00m
[37m[39;49;00m
[37m/*[39;49;00m
[37m    Initializes the dictionary by unarchiving the data from a coder.[39;49;00m
[37m    @param aCoder the coder from which the data will be unarchived.[39;49;00m
[37m    @return the initialized dictionary[39;49;00m
[37m*/[39;49;00m[37m[39;49;00m
-[37m [39;49;00m([36mid[39;49;00m)[32minitWithCoder:[39;49;00m([36mCPCoder[39;49;00m)aCoder[37m[39;49;00m
{[37m[39;49;00m
[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[aCoder[37m [39;49;00m_decodeDictionaryOfObjectsForKey:[33m@"[39;49;00m[33mCP.objects[39;49;00m[33m"[39;49;00m];[37m[39;49;00m
}[37m[39;49;00m
[37m[39;49;00m
[37m/*![39;49;00m
[37m    Archives the dictionary to a provided coder.[39;49;00m
[37m    @param aCoder the coder to which the dictionary data will be archived.[39;49;00m
[37m*/[39;49;00m[37m[39;49;00m
-[37m [39;49;00m([36mvoid[39;49;00m)[32mencodeWithCoder:[39;49;00m([36mCPCoder[39;49;00m)aCoder[37m[39;49;00m
{[37m[39;49;00m
[37m    [39;49;00m[aCoder[37m [39;49;00m_encodeDictionaryOfObjects:[36mself[39;49;00m[37m [39;49;00mforKey:[33m@"[39;49;00m[33mCP.objects[39;49;00m[33m"[39;49;00m];[37m[39;49;00m
}[37m[39;49;00m
[37m[39;49;00m
[34m@end[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m/*![39;49;00m
[37m    @class CPMutableDictionary[39;49;00m
[37m    @ingroup compatability[39;49;00m
[37m[39;49;00m
[37m    This class is just an empty subclass of CPDictionary.[39;49;00m
[37m    CPDictionary already implements mutable methods and[39;49;00m
[37m    this class only exists for source compatability.[39;49;00m
[37m*/[39;49;00m[37m[39;49;00m
[34m@implementation[39;49;00m[37m [39;49;00m[04m[32mCPMutableDictionary[39;49;00m[37m [39;49;00m:[37m [39;49;00m[04m[32mCPDictionary[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[34m@end[39;49;00m[37m[39;49;00m
[37m[39;49;00m
objj_dictionary.[34mprototype[39;49;00m.isa[37m [39;49;00m=[37m [39;49;00mCPDictionary;

Using lexer <pygments.lexers.DLexer with {'ensurenl': False, 'tabsize': 0}>
[37m// Created by Lionello Lunesu and placed in the public domain.[39;49;00m[37m[39;49;00m
[37m// This file has been modified from its original version.[39;49;00m[37m[39;49;00m
[37m// It has been formatted to fit your screen.[39;49;00m[37m[39;49;00m
[34mmodule[39;49;00m[37m [39;49;00mphoneno;[37m     [39;49;00m[37m// optional[39;49;00m[37m[39;49;00m
[34mimport[39;49;00m[37m [39;49;00mstd.stdio;[37m   [39;49;00m[37m// writefln     [39;49;00m[37m[39;49;00m
[34mimport[39;49;00m[37m [39;49;00mstd.ctype;[37m   [39;49;00m[37m// isdigit     [39;49;00m[37m[39;49;00m
[34mimport[39;49;00m[37m [39;49;00mstd.stream;[37m  [39;49;00m[37m// BufferedFile[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m// Just for readability (imagine char[][][char[]])    [39;49;00m[37m[39;49;00m
[34malias[39;49;00m[37m [39;49;00m[36mchar[39;49;00m[][37m [39;49;00m[36mstring[39;49;00m;[37m[39;49;00m
[34malias[39;49;00m[37m [39;49;00m[36mstring[39;49;00m[][37m [39;49;00mstringarray;[37m[39;49;00m
[37m[39;49;00m
[37m/// Strips non-digit characters from the string (COW)[39;49;00m[37m[39;49;00m
[36mstring[39;49;00m[37m [39;49;00mstripNonDigit([37m [39;49;00m[34min[39;49;00m[37m [39;49;00m[36mstring[39;49;00m[37m [39;49;00mline[37m [39;49;00m)[37m [39;49;00m
{[37m[39;49;00m
[37m    [39;49;00m[36mstring[39;49;00m[37m [39;49;00mret;[37m[39;49;00m
[37m    [39;49;00m[34mforeach[39;49;00m([36muint[39;49;00m[37m [39;49;00mi,[37m [39;49;00mc;[37m [39;49;00mline)[37m [39;49;00m{[37m[39;49;00m
[37m        [39;49;00m[37m// Error: std.ctype.isdigit at C:\dmd\src\phobos\std\ctype.d(37) [39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m// conflicts with std.stream.isdigit at C:\dmd\src\phobos\std\stream.d(2924)[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!std.ctype.isdigit(c))[37m [39;49;00m{[37m[39;49;00m
[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!ret)[37m[39;49;00m
[37m                [39;49;00mret[37m [39;49;00m=[37m [39;49;00mline[[34m0.[39;49;00m.i];[37m    [39;49;00m
[37m        [39;49;00m}[37m    [39;49;00m
[37m        [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ret)[37m[39;49;00m
[37m            [39;49;00mret[37m [39;49;00m~=[37m [39;49;00mc;[37m    [39;49;00m
[37m    [39;49;00m}[37m    [39;49;00m
[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mret?ret:line;[37m[39;49;00m
}[37m[39;49;00m
[37m[39;49;00m
[34munittest[39;49;00m[37m [39;49;00m{[37m[39;49;00m
[37m    [39;49;00m[34massert[39;49;00m([37m [39;49;00mstripNonDigit([33m"asdf"[39;49;00m)[37m [39;49;00m==[37m [39;49;00m[33m""[39;49;00m[37m  [39;49;00m);[37m[39;49;00m
[37m    [39;49;00m[34massert[39;49;00m([37m [39;49;00mstripNonDigit([33m"\'13-=2 4kop"[39;49;00m)[37m [39;49;00m==[37m  [39;49;00m[33m"1324"[39;49;00m[37m  [39;49;00m);[37m[39;49;00m
}[37m[39;49;00m
[37m[39;49;00m
[37m/// Converts a word into a number, ignoring all non alpha characters  [39;49;00m[37m[39;49;00m
[36mstring[39;49;00m[37m [39;49;00mwordToNum([37m [39;49;00m[34min[39;49;00m[37m [39;49;00m[36mstring[39;49;00m[37m [39;49;00mword[37m [39;49;00m)[37m[39;49;00m
{[37m[39;49;00m
[37m// translation table for the task at hand[39;49;00m[37m[39;49;00m
[34mconst[39;49;00m[37m [39;49;00m[36mchar[39;49;00m[[34m256[39;49;00m][37m [39;49;00mTRANSLATE[37m [39;49;00m=[37m    [39;49;00m
[37m    [39;49;00m[33m"                                "[39;49;00m[37m  [39;49;00m[37m// 0   [39;49;00m[37m[39;49;00m
[37m    [39;49;00m[33m"                0123456789      "[39;49;00m[37m  [39;49;00m[37m// 32     [39;49;00m[37m[39;49;00m
[37m    [39;49;00m[33m" 57630499617851881234762239     "[39;49;00m[37m  [39;49;00m[37m// 64   [39;49;00m[37m[39;49;00m
[37m    [39;49;00m[33m" 57630499617851881234762239     "[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[33m"                                "[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[33m"                                "[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[33m"                                "[39;49;00m[37m    [39;49;00m
[37m    [39;49;00m[33m"                                "[39;49;00m;[37m[39;49;00m
[37m    [39;49;00m[36mstring[39;49;00m[37m [39;49;00mret;[37m[39;49;00m
[37m    [39;49;00m[34mforeach[39;49;00m(c;[37m [39;49;00m[34mcast[39;49;00m([36mubyte[39;49;00m[])word)[37m[39;49;00m
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(TRANSLATE[c][37m [39;49;00m!=[37m [39;49;00m[33m' '[39;49;00m)[37m[39;49;00m
[37m            [39;49;00mret[37m [39;49;00m~=[37m [39;49;00mTRANSLATE[c];[37m[39;49;00m
[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mret;[37m[39;49;00m
}[37m[39;49;00m
[37m[39;49;00m
[34munittest[39;49;00m[37m [39;49;00m{[37m[39;49;00m
[37m [39;49;00m[37m// Test wordToNum using the table from the task description.[39;49;00m[37m[39;49;00m
[37m [39;49;00m[34massert[39;49;00m([37m [39;49;00m[33m"01112223334455666777888999"[39;49;00m[37m [39;49;00m==[37m[39;49;00m
[37m   [39;49;00mwordToNum([33m"E | J N Q | R W X | D S Y | F T | A M | C I V | B K U | L O P | G H Z"[39;49;00m));[37m[39;49;00m
[37m [39;49;00m[34massert[39;49;00m([37m [39;49;00m[33m"01112223334455666777888999"[39;49;00m[37m [39;49;00m==[37m [39;49;00m
[37m   [39;49;00mwordToNum([33m"e | j n q | r w x | d s y | f t | a m | c i v | b k u | l o p | g h z"[39;49;00m));[37m[39;49;00m
[37m [39;49;00m[34massert[39;49;00m([37m [39;49;00m[33m"0123456789"[39;49;00m[37m [39;49;00m==[37m [39;49;00m
[37m   [39;49;00mwordToNum([33m"0 |   1   |   2   |   3   |  4  |  5  |   6   |   7   |   8   |   9"[39;49;00m));[37m[39;49;00m
}[37m[39;49;00m
[37m[39;49;00m
[36mvoid[39;49;00m[37m [39;49;00mmain([37m [39;49;00m[36mstring[39;49;00m[][37m [39;49;00margs[37m [39;49;00m)[37m[39;49;00m
{[37m[39;49;00m
[37m    [39;49;00m[37m// This associative array maps a number to an array of words.    [39;49;00m[37m[39;49;00m
[37m    [39;49;00mstringarray[[36mstring[39;49;00m][37m    [39;49;00mnum2words;[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[34mforeach[39;49;00m([36mstring[39;49;00m[37m [39;49;00mword;[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mBufferedFile([33m"dictionary.txt"[39;49;00m[37m [39;49;00m)[37m [39;49;00m)[37m[39;49;00m
[37m        [39;49;00mnum2words[[37m [39;49;00mwordToNum(word)[37m [39;49;00m][37m [39;49;00m~=[37m [39;49;00mword.dup;[37m        [39;49;00m[37m// must dup[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[37m/// Finds all alternatives for the given number[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[37m/// (should have been stripped from non-digit characters)[39;49;00m[37m[39;49;00m
[37m    [39;49;00mstringarray[37m [39;49;00m_FindWords([37m [39;49;00m[36mstring[39;49;00m[37m [39;49;00mnumbers,[37m [39;49;00m[36mbool[39;49;00m[37m [39;49;00mdigitok[37m [39;49;00m)[37m[39;49;00m
[37m    [39;49;00m[34min[39;49;00m[37m [39;49;00m{[37m[39;49;00m
[37m        [39;49;00m[34massert[39;49;00m(numbers.length[37m [39;49;00m>[37m  [39;49;00m[34m0[39;49;00m);[37m    [39;49;00m
[37m    [39;49;00m}[37m    [39;49;00m
[37m    [39;49;00m[34mout[39;49;00m(result)[37m [39;49;00m{[37m[39;49;00m
[37m        [39;49;00m[34mforeach[39;49;00m[37m [39;49;00m(a;[37m [39;49;00mresult)[37m[39;49;00m
[37m            [39;49;00m[34massert[39;49;00m([37m [39;49;00mwordToNum(a)[37m [39;49;00m==[37m [39;49;00mnumbers[37m [39;49;00m);[37m[39;49;00m
[37m    [39;49;00m}[37m    [39;49;00m
[37m    [39;49;00m[34mbody[39;49;00m[37m [39;49;00m{[37m[39;49;00m
[37m        [39;49;00mstringarray[37m [39;49;00mret;[37m[39;49;00m
[37m        [39;49;00m[36mbool[39;49;00m[37m [39;49;00mfoundword[37m [39;49;00m=[37m [39;49;00m[34mfalse[39;49;00m;[37m[39;49;00m
[37m        [39;49;00m[34mfor[39;49;00m[37m [39;49;00m([36muint[39;49;00m[37m [39;49;00mt=[34m1[39;49;00m;[37m [39;49;00mt<=numbers.length;[37m [39;49;00m++t)[37m [39;49;00m{[37m[39;49;00m
[37m            [39;49;00m[34mauto[39;49;00m[37m [39;49;00malternatives[37m [39;49;00m=[37m [39;49;00mnumbers[[34m0.[39;49;00m.t][37m [39;49;00m[34min[39;49;00m[37m [39;49;00mnum2words;[37m[39;49;00m
[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!alternatives)[37m[39;49;00m
[37m                [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m
[37m            [39;49;00mfoundword[37m [39;49;00m=[37m [39;49;00m[34mtrue[39;49;00m;[37m[39;49;00m
[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(numbers.length[37m [39;49;00m>[37m  [39;49;00mt)[37m [39;49;00m{[37m[39;49;00m
[37m                [39;49;00m[37m// Combine all current alternatives with all alternatives     [39;49;00m[37m[39;49;00m
[37m                [39;49;00m[37m// of the rest (next piece can start with a digit)              [39;49;00m[37m[39;49;00m
[37m                [39;49;00m[34mforeach[39;49;00m[37m [39;49;00m(a2;[37m [39;49;00m_FindWords([37m [39;49;00mnumbers[t..$],[37m [39;49;00m[34mtrue[39;49;00m[37m     [39;49;00m)[37m [39;49;00m)[37m[39;49;00m
[37m                    [39;49;00m[34mforeach[39;49;00m(a1;[37m [39;49;00m*alternatives)[37m[39;49;00m
[37m                       [39;49;00mret[37m [39;49;00m~=[37m [39;49;00ma1[37m [39;49;00m~[37m [39;49;00m[33m" "[39;49;00m[37m [39;49;00m~[37m [39;49;00ma2;[37m[39;49;00m
[37m            [39;49;00m}[37m[39;49;00m
[37m            [39;49;00m[34melse[39;49;00m[37m    [39;49;00m
[37m                [39;49;00mret[37m [39;49;00m~=[37m [39;49;00m*alternatives;[37m    [39;49;00m[37m// append these alternatives[39;49;00m[37m[39;49;00m
[37m        [39;49;00m}[37m[39;49;00m
[37m        [39;49;00m[37m// Try to keep 1 digit, only if we're allowed and no other[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m// alternatives were found[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m// Testing "ret.length" makes more sense than testing "foundword",[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m// but the other implementations seem to do just this.[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(digitok[37m [39;49;00m&&[37m [39;49;00m!foundword)[37m [39;49;00m{[37m [39;49;00m[37m//ret.length == 0  [39;49;00m[37m[39;49;00m
[37m            [39;49;00m[34mif[39;49;00m(numbers.length[37m [39;49;00m>[37m  [39;49;00m[34m1[39;49;00m)[37m [39;49;00m{[37m[39;49;00m
[37m                [39;49;00m[37m// Combine 1 digit with all altenatives from the rest    [39;49;00m[37m[39;49;00m
[37m                [39;49;00m[37m// (next piece can not start with a digit)          [39;49;00m[37m[39;49;00m
[37m                [39;49;00m[34mforeach[39;49;00m[37m [39;49;00m(a;[37m [39;49;00m_FindWords([37m [39;49;00mnumbers[[34m1.[39;49;00m.$],[37m [39;49;00m[34mfalse[39;49;00m[37m [39;49;00m)[37m [39;49;00m)[37m[39;49;00m
[37m                    [39;49;00mret[37m [39;49;00m~=[37m [39;49;00mnumbers[[34m0.[39;49;00m[34m.1[39;49;00m][37m [39;49;00m~[37m [39;49;00m[33m" "[39;49;00m[37m [39;49;00m~[37m [39;49;00ma;[37m[39;49;00m
[37m            [39;49;00m}[37m    [39;49;00m
[37m            [39;49;00m[34melse[39;49;00m[37m    [39;49;00m
[37m                [39;49;00mret[37m [39;49;00m~=[37m [39;49;00mnumbers[[34m0.[39;49;00m[34m.1[39;49;00m];[37m    [39;49;00m[37m// just append this digit             [39;49;00m[37m[39;49;00m
[37m        [39;49;00m}[37m    [39;49;00m
[37m        [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mret;[37m[39;49;00m
[37m    [39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[37m/// (This function was inlined in the original program) [39;49;00m[37m[39;49;00m
[37m    [39;49;00m[37m/// Finds all alternatives for the given phone number [39;49;00m[37m[39;49;00m
[37m    [39;49;00m[37m/// Returns: array of strings [39;49;00m[37m[39;49;00m
[37m    [39;49;00mstringarray[37m [39;49;00mFindWords([37m [39;49;00m[36mstring[39;49;00m[37m [39;49;00mphone_number[37m [39;49;00m)[37m[39;49;00m
[37m    [39;49;00m{[37m[39;49;00m
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!phone_number.length)[37m[39;49;00m
[37m            [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mnull[39;49;00m;[37m[39;49;00m
[37m        [39;49;00m[37m// Strip the non-digit characters from the phone number, and[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m// pass it to the recursive function (leading digit is allowed)[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m_FindWords([37m [39;49;00mstripNonDigit(phone_number),[37m [39;49;00m[34mtrue[39;49;00m[37m [39;49;00m);[37m    [39;49;00m
[37m    [39;49;00m}[37m    [39;49;00m
[37m    [39;49;00m
[37m    [39;49;00m[37m// Read the phone numbers     [39;49;00m[37m[39;49;00m
[37m    [39;49;00m[34mforeach[39;49;00m([36mstring[39;49;00m[37m [39;49;00mphone;[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mBufferedFile([33m"input.txt"[39;49;00m[37m   [39;49;00m)[37m [39;49;00m)[37m[39;49;00m
[37m        [39;49;00m[34mforeach[39;49;00m(alternative;[37m [39;49;00mFindWords([37m [39;49;00mphone[37m [39;49;00m)[37m [39;49;00m)[37m[39;49;00m
[37m            [39;49;00mwritefln(phone,[37m [39;49;00m[33m": "[39;49;00m,[37m [39;49;00malternative[37m [39;49;00m);[37m[39;49;00m
}
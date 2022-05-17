     1^I[34m<!DOCTYPE[39;49;00m [94mhtml[39;49;00m[34m>[39;49;00m$
     2^I$
     3^I[34m<!DOCTYPE[39;49;00m [94mhtml[39;49;00m [34mPUBLIC[39;49;00m [33m"-//W3C//DTD XHTML 1.0 Transitional//EN"[39;49;00m$
     4^I[33m"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"[39;49;00m[34m>[39;49;00m$
     5^I$
     6^I$
     7^I[34m<!DOCTYPE[39;49;00m [94mhtml[39;49;00m [34mPUBLIC[39;49;00m [33m"-//W3C//DTD XHTML 1.0 Transitional//EN"[39;49;00m$
     8^I[33m"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"[39;49;00m [34m[[39;49;00m$
     9^I  [37m<!--[39;49;00m[37m an internal subset can be embedded here [39;49;00m[37m-->[39;49;00m$
    10^I[34m][39;49;00m[34m>[39;49;00m$
    11^I$
    12^I[34m<!DOCTYPE[39;49;00m [94mgreeting[39;49;00m [34mSYSTEM[39;49;00m [33m"hello.dtd"[39;49;00m[34m>[39;49;00m$
    13^I$
    14^I[34m<!DOCTYPE[39;49;00m [94mgreeting[39;49;00m [34m[[39;49;00m$
    15^I  [34m<!ELEMENT[39;49;00m [94mgreeting[39;49;00m ([34m#PCDATA[39;49;00m)[34m>[39;49;00m$
    16^I$
    17^I[37m<!--[39;49;00m[37m examples from XML spec [39;49;00m[37m-->[39;49;00m$
    18^I$
    19^I[34m<!ELEMENT[39;49;00m [94mbr[39;49;00m [34mEMPTY[39;49;00m[34m>[39;49;00m$
    20^I[34m<!ELEMENT[39;49;00m [94mp[39;49;00m ([34m#PCDATA[39;49;00m|[94memph[39;49;00m)* [34m>[39;49;00m$
    21^I[34m<!ELEMENT[39;49;00m [94m%name.para;[39;49;00m %content.para; [34m>[39;49;00m$
    22^I[34m<!ELEMENT[39;49;00m [94mcontainer[39;49;00m [34mANY[39;49;00m[34m>[39;49;00m$
    23^I$
    24^I[34m<!ELEMENT[39;49;00m [94mspec[39;49;00m ([94mfront[39;49;00m, [94mbody[39;49;00m, [94mback[39;49;00m?)[34m>[39;49;00m$
    25^I[34m<!ELEMENT[39;49;00m [94mdiv1[39;49;00m ([94mhead[39;49;00m, ([94mp[39;49;00m | [94mlist[39;49;00m | [94mnote[39;49;00m)*, [94mdiv2[39;49;00m*)[34m>[39;49;00m$
    26^I[34m<!ELEMENT[39;49;00m [94mdictionary-body[39;49;00m (%div.mix; | %dict.mix;)*[34m>[39;49;00m$
    27^I$
    28^I[34m<!ELEMENT[39;49;00m [94mp[39;49;00m ([34m#PCDATA[39;49;00m|[94ma[39;49;00m|[94mul[39;49;00m|[94mb[39;49;00m|[94mi[39;49;00m|[94mem[39;49;00m)*[34m>[39;49;00m$
    29^I[34m<!ELEMENT[39;49;00m [94mp[39;49;00m ([34m#PCDATA[39;49;00m | %font; | %phrase; | %special; | %form;)* [34m>[39;49;00m$
    30^I[34m<!ELEMENT[39;49;00m [94mb[39;49;00m ([34m#PCDATA[39;49;00m)[34m>[39;49;00m$
    31^I$
    32^I[34m<!ATTLIST[39;49;00m [94mtermdef[39;49;00m$
    33^I          [36mid[39;49;00m      [34mID[39;49;00m      [34m#REQUIRED[39;49;00m$
    34^I          [36mname[39;49;00m    [34mCDATA[39;49;00m   [34m#IMPLIED[39;49;00m[34m>[39;49;00m$
    35^I[34m<!ATTLIST[39;49;00m [94mlist[39;49;00m$
    36^I          [36mtype[39;49;00m    ([36mbullets[39;49;00m|[36mordered[39;49;00m|[36mglossary[39;49;00m)  [33m"ordered"[39;49;00m[34m>[39;49;00m$
    37^I[34m<!ATTLIST[39;49;00m [94mform[39;49;00m$
    38^I          [36mmethod[39;49;00m  [34mCDATA[39;49;00m   [34m#FIXED[39;49;00m [33m"POST"[39;49;00m[34m>[39;49;00m$
    39^I$
    40^I[34m<!ENTITY[39;49;00m d [33m"&#xD;"[39;49;00m[34m>[39;49;00m$
    41^I[34m<!ENTITY[39;49;00m a [33m"&#xA;"[39;49;00m[34m>[39;49;00m$
    42^I[34m<!ENTITY[39;49;00m da [33m"&#xD;&#xA;"[39;49;00m[34m>[39;49;00m$
    43^I$
    44^I[34m<!ENTITY[39;49;00m % ISOLat2$
    45^I         [34mSYSTEM[39;49;00m [33m"http://www.xml.com/iso/isolat2-xml.entities"[39;49;00m [34m>[39;49;00m$
    46^I$
    47^I[34m<!ENTITY[39;49;00m Pub-Status [33m"This is a pre-release of the[39;49;00m$
    48^I[33m specification."[39;49;00m[34m>[39;49;00m$
    49^I $
    50^I [34m<!ENTITY[39;49;00m open-hatch$
    51^I         [34mSYSTEM[39;49;00m [33m"http://www.textuality.com/boilerplate/OpenHatch.xml"[39;49;00m[34m>[39;49;00m$
    52^I[34m<!ENTITY[39;49;00m open-hatch$
    53^I         [34mPUBLIC[39;49;00m [33m"-//Textuality//TEXT Standard open-hatch boilerplate//EN"[39;49;00m$
    54^I         [33m"http://www.textuality.com/boilerplate/OpenHatch.xml"[39;49;00m[34m>[39;49;00m$
    55^I[34m<!ENTITY[39;49;00m hatch-pic$
    56^I         [34mSYSTEM[39;49;00m [33m"../grafix/OpenHatch.gif"[39;49;00m$
    57^I         [34mNDATA[39;49;00m gif [34m>[39;49;00m$
    58^I         $
    59^I[34m<!NOTATION[39;49;00m [94mgif[39;49;00m [34mPUBLIC[39;49;00m [33m"gif viewer"[39;49;00m[34m>[39;49;00m$
    60^I$
    61^I[34m<!ENTITY[39;49;00m % YN [33m'"Yes"'[39;49;00m [34m>[39;49;00m$
    62^I[34m<!ENTITY[39;49;00m WhatHeSaid [33m"He said %YN;"[39;49;00m [34m>[39;49;00m$
    63^I$
    64^I[34m<!ENTITY[39;49;00m EndAttr [33m"27'"[39;49;00m [34m>[39;49;00m$
    65^I$
    66^I[34m<!ENTITY[39;49;00m % pub    [33m"&#xc9;ditions Gallimard"[39;49;00m [34m>[39;49;00m$
    67^I[34m<!ENTITY[39;49;00m   rights [33m"All rights reserved"[39;49;00m [34m>[39;49;00m$
    68^I[34m<!ENTITY[39;49;00m   book   [33m"La Peste: Albert Camus,[39;49;00m$
    69^I[33m&#xA9; 1947 %pub;. &rights;"[39;49;00m [34m>[39;49;00m$
    70^I$
    71^I[34m<!ENTITY[39;49;00m lt     [33m"&#38;#60;"[39;49;00m[34m>[39;49;00m$
    72^I[34m<!ENTITY[39;49;00m gt     [33m"&#62;"[39;49;00m[34m>[39;49;00m$
    73^I[34m<!ENTITY[39;49;00m amp    [33m"&#38;#38;"[39;49;00m[34m>[39;49;00m$
    74^I[34m<!ENTITY[39;49;00m apos   [33m"&#39;"[39;49;00m[34m>[39;49;00m$
    75^I[34m<!ENTITY[39;49;00m quot   [33m"&#34;"[39;49;00m[34m>[39;49;00m$
    76^I$
    77^I[34m<!ENTITY[39;49;00m % draft [33m'INCLUDE'[39;49;00m [34m>[39;49;00m$
    78^I[34m<!ENTITY[39;49;00m % final [33m'IGNORE'[39;49;00m [34m>[39;49;00m$
    79^I$
    80^I[34m<![[39;49;00m%draft;[34m[[39;49;00m$
    81^I[34m<!ELEMENT[39;49;00m [94mbook[39;49;00m ([94mcomments[39;49;00m*, [94mtitle[39;49;00m, [94mbody[39;49;00m, [94msupplements[39;49;00m?)[34m>[39;49;00m$
    82^I[34m][39;49;00m[34m][39;49;00m[34m>[39;49;00m$
    83^I[34m<![[39;49;00m%final;[34m[[39;49;00m$
    84^I[34m<!ELEMENT[39;49;00m [94mbook[39;49;00m ([94mtitle[39;49;00m, [94mbody[39;49;00m, [94msupplements[39;49;00m?)[34m>[39;49;00m$
    85^I[34m][39;49;00m[34m][39;49;00m[34m>[39;49;00m$
    86^I$
    87^I[34m][39;49;00m[34m>[39;49;00m$

[34m<!DOCTYPE[39;49;00m [94mhtml[39;49;00m[34m>[39;49;00m$
$
[34m<!DOCTYPE[39;49;00m [94mhtml[39;49;00m [34mPUBLIC[39;49;00m [33m"-//W3C//DTD XHTML 1.0 Transitional//EN"[39;49;00m$
[33m"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"[39;49;00m[34m>[39;49;00m$
$
$
[34m<!DOCTYPE[39;49;00m [94mhtml[39;49;00m [34mPUBLIC[39;49;00m [33m"-//W3C//DTD XHTML 1.0 Transitional//EN"[39;49;00m$
[33m"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"[39;49;00m [34m[[39;49;00m$
  [37m<!--[39;49;00m[37m an internal subset can be embedded here [39;49;00m[37m-->[39;49;00m$
[34m][39;49;00m[34m>[39;49;00m$
$
[34m<!DOCTYPE[39;49;00m [94mgreeting[39;49;00m [34mSYSTEM[39;49;00m [33m"hello.dtd"[39;49;00m[34m>[39;49;00m$
$
[34m<!DOCTYPE[39;49;00m [94mgreeting[39;49;00m [34m[[39;49;00m$
  [34m<!ELEMENT[39;49;00m [94mgreeting[39;49;00m ([34m#PCDATA[39;49;00m)[34m>[39;49;00m$
$
[37m<!--[39;49;00m[37m examples from XML spec [39;49;00m[37m-->[39;49;00m$
$
[34m<!ELEMENT[39;49;00m [94mbr[39;49;00m [34mEMPTY[39;49;00m[34m>[39;49;00m$
[34m<!ELEMENT[39;49;00m [94mp[39;49;00m ([34m#PCDATA[39;49;00m|[94memph[39;49;00m)* [34m>[39;49;00m$
[34m<!ELEMENT[39;49;00m [94m%name.para;[39;49;00m %content.para; [34m>[39;49;00m$
[34m<!ELEMENT[39;49;00m [94mcontainer[39;49;00m [34mANY[39;49;00m[34m>[39;49;00m$
$
[34m<!ELEMENT[39;49;00m [94mspec[39;49;00m ([94mfront[39;49;00m, [94mbody[39;49;00m, [94mback[39;49;00m?)[34m>[39;49;00m$
[34m<!ELEMENT[39;49;00m [94mdiv1[39;49;00m ([94mhead[39;49;00m, ([94mp[39;49;00m | [94mlist[39;49;00m | [94mnote[39;49;00m)*, [94mdiv2[39;49;00m*)[34m>[39;49;00m$
[34m<!ELEMENT[39;49;00m [94mdictionary-body[39;49;00m (%div.mix; | %dict.mix;)*[34m>[39;49;00m$
$
[34m<!ELEMENT[39;49;00m [94mp[39;49;00m ([34m#PCDATA[39;49;00m|[94ma[39;49;00m|[94mul[39;49;00m|[94mb[39;49;00m|[94mi[39;49;00m|[94mem[39;49;00m)*[34m>[39;49;00m$
[34m<!ELEMENT[39;49;00m [94mp[39;49;00m ([34m#PCDATA[39;49;00m | %font; | %phrase; | %special; | %form;)* [34m>[39;49;00m$
[34m<!ELEMENT[39;49;00m [94mb[39;49;00m ([34m#PCDATA[39;49;00m)[34m>[39;49;00m$
$
[34m<!ATTLIST[39;49;00m [94mtermdef[39;49;00m$
          [36mid[39;49;00m      [34mID[39;49;00m      [34m#REQUIRED[39;49;00m$
          [36mname[39;49;00m    [34mCDATA[39;49;00m   [34m#IMPLIED[39;49;00m[34m>[39;49;00m$
[34m<!ATTLIST[39;49;00m [94mlist[39;49;00m$
          [36mtype[39;49;00m    ([36mbullets[39;49;00m|[36mordered[39;49;00m|[36mglossary[39;49;00m)  [33m"ordered"[39;49;00m[34m>[39;49;00m$
[34m<!ATTLIST[39;49;00m [94mform[39;49;00m$
          [36mmethod[39;49;00m  [34mCDATA[39;49;00m   [34m#FIXED[39;49;00m [33m"POST"[39;49;00m[34m>[39;49;00m$
$
[34m<!ENTITY[39;49;00m d [33m"&#xD;"[39;49;00m[34m>[39;49;00m$
[34m<!ENTITY[39;49;00m a [33m"&#xA;"[39;49;00m[34m>[39;49;00m$
[34m<!ENTITY[39;49;00m da [33m"&#xD;&#xA;"[39;49;00m[34m>[39;49;00m$
$
[34m<!ENTITY[39;49;00m % ISOLat2$
         [34mSYSTEM[39;49;00m [33m"http://www.xml.com/iso/isolat2-xml.entities"[39;49;00m [34m>[39;49;00m$
$
[34m<!ENTITY[39;49;00m Pub-Status [33m"This is a pre-release of the[39;49;00m$
[33m specification."[39;49;00m[34m>[39;49;00m$
 $
 [34m<!ENTITY[39;49;00m open-hatch$
         [34mSYSTEM[39;49;00m [33m"http://www.textuality.com/boilerplate/OpenHatch.xml"[39;49;00m[34m>[39;49;00m$
[34m<!ENTITY[39;49;00m open-hatch$
         [34mPUBLIC[39;49;00m [33m"-//Textuality//TEXT Standard open-hatch boilerplate//EN"[39;49;00m$
         [33m"http://www.textuality.com/boilerplate/OpenHatch.xml"[39;49;00m[34m>[39;49;00m$
[34m<!ENTITY[39;49;00m hatch-pic$
         [34mSYSTEM[39;49;00m [33m"../grafix/OpenHatch.gif"[39;49;00m$
         [34mNDATA[39;49;00m gif [34m>[39;49;00m$
         $
[34m<!NOTATION[39;49;00m [94mgif[39;49;00m [34mPUBLIC[39;49;00m [33m"gif viewer"[39;49;00m[34m>[39;49;00m$
$
[34m<!ENTITY[39;49;00m % YN [33m'"Yes"'[39;49;00m [34m>[39;49;00m$
[34m<!ENTITY[39;49;00m WhatHeSaid [33m"He said %YN;"[39;49;00m [34m>[39;49;00m$
$
[34m<!ENTITY[39;49;00m EndAttr [33m"27'"[39;49;00m [34m>[39;49;00m$
$
[34m<!ENTITY[39;49;00m % pub    [33m"&#xc9;ditions Gallimard"[39;49;00m [34m>[39;49;00m$
[34m<!ENTITY[39;49;00m   rights [33m"All rights reserved"[39;49;00m [34m>[39;49;00m$
[34m<!ENTITY[39;49;00m   book   [33m"La Peste: Albert Camus,[39;49;00m$
[33m&#xA9; 1947 %pub;. &rights;"[39;49;00m [34m>[39;49;00m$
$
[34m<!ENTITY[39;49;00m lt     [33m"&#38;#60;"[39;49;00m[34m>[39;49;00m$
[34m<!ENTITY[39;49;00m gt     [33m"&#62;"[39;49;00m[34m>[39;49;00m$
[34m<!ENTITY[39;49;00m amp    [33m"&#38;#38;"[39;49;00m[34m>[39;49;00m$
[34m<!ENTITY[39;49;00m apos   [33m"&#39;"[39;49;00m[34m>[39;49;00m$
[34m<!ENTITY[39;49;00m quot   [33m"&#34;"[39;49;00m[34m>[39;49;00m$
$
[34m<!ENTITY[39;49;00m % draft [33m'INCLUDE'[39;49;00m [34m>[39;49;00m$
[34m<!ENTITY[39;49;00m % final [33m'IGNORE'[39;49;00m [34m>[39;49;00m$
$
[34m<![[39;49;00m%draft;[34m[[39;49;00m$
[34m<!ELEMENT[39;49;00m [94mbook[39;49;00m ([94mcomments[39;49;00m*, [94mtitle[39;49;00m, [94mbody[39;49;00m, [94msupplements[39;49;00m?)[34m>[39;49;00m$
[34m][39;49;00m[34m][39;49;00m[34m>[39;49;00m$
[34m<![[39;49;00m%final;[34m[[39;49;00m$
[34m<!ELEMENT[39;49;00m [94mbook[39;49;00m ([94mtitle[39;49;00m, [94mbody[39;49;00m, [94msupplements[39;49;00m?)[34m>[39;49;00m$
[34m][39;49;00m[34m][39;49;00m[34m>[39;49;00m$
$
[34m][39;49;00m[34m>[39;49;00m$

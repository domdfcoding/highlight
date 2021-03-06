## Please edit system and help pages ONLY in the moinmaster wiki! For more$
## information, please see MoinMaster:MoinPagesEditorGroup.$
##master-page:Unknown-Page$
##master-date:Unknown-Date$
#acl MoinPagesEditorGroup:read,write,delete,revert All:read$
#format wiki$
#language en$
$
This page aims to introduce the most important elements of MoinMoin``'s syntax at a glance, showing first the markup verbatim and then how it is rendered by the wiki engine. Additionally, you'll find links to the relative help pages. Please note that some of the features depend on your configuration.$
$
= Table of Contents =$
{{{$
'''Contents''' (up to the 2nd level)$
[[TableOfContents(2)]]$
}}}$
'''Contents''' (up to the 2nd level)$
[[TableOfContents(2)]]$
$
= Headings =$
'''''see:''' HelpOnHeadlines''$
{{{$
= heading 1st level =$
== heading 2nd level ==$
=== heading 3rd level ===$
==== heading 4th level ====$
===== heading 5th level =====$
}}}$
= heading 1st level =$
== heading 2nd level ==$
=== heading 3rd level ===$
==== heading 4th level ====$
===== heading 5th level =====$
$
= Text Formatting =$
'''''see:''' HelpOnFormatting''$
{{{$
 * ''emphasized (italics)''$
 * '''boldface'''$
 * '''''bold italics'''''$
 * `monospace`$
 * {{{source code}}}$
 * __underline__$
 * ,,sub,,script$
 * ^super^script$
 * ~-smaller-~$
 * ~+larger+~$
 * --(strike through)--$
}}}$
 * ''emphasized (italics)''$
 * '''boldface'''$
 * '''''bold italics'''''$
 * `monospace`$
 * {{{source code}}}$
 * __underline__$
 * ,,sub,,script$
 * ^super^script$
 * ~-smaller-~$
 * ~+larger+~$
 * --(strike through)--$
$
= Hyperlinks =$
'''''see:''' HelpOnLinking''$
== Internal Links ==$
{{{$
 * FrontPage$
 * ["FrontPage"]$
 * HelpOnEditing/SubPages$
 * /SubPage$
 * ../SiblingPage$
 * [:FrontPage:named link]$
 * [#anchorname]$
 * [#anchorname description]$
 * [wiki:Self:PageName#anchorname]$
 * [wiki:Self:PageName#anchorname description]$
 * attachment:filename.txt$
}}}$
 * FrontPage$
 * ["FrontPage"]$
 * HelpOnEditing/SubPages$
 * /SubPage$
 * ../SiblingPage$
 * [:FrontPage:named link]$
 * [#anchorname]$
 * [#anchorname description]$
 * [wiki:Self:PageName#anchorname]$
 * [wiki:Self:PageName#anchorname description]$
 * attachment:filename.txt$
$
== External Links ==$
{{{$
 * http://moinmoin.wikiwikiweb.de/$
 * [http://moinmoin.wikiwikiweb.de/]$
 * [http://moinmoin.wikiwikiweb.de/ MoinMoin Wiki]$
 * [http://moinmoin.wikiwikiweb.de/wiki/moinmoin.png]$
 * http://moinmoin.wikiwikiweb.de/wiki/moinmoin.png$
 * [http://moinmoin.wikiwikiweb.de/wiki/moinmoin.png moinmoin.png]$
 * MeatBall:InterWiki$
 * wiki:MeatBall/InterWiki$
 * [wiki:MeatBall/InterWiki]$
 * [wiki:MeatBall/InterWiki InterWiki page on MeatBall]$
 * [file://///servername/share/full/path/to/file/filename%20with%20spaces.txt link to file filename with spaces.txt]$
 * user@example.com$
}}}$
 * http://moinmoin.wikiwikiweb.de/$
 * [http://moinmoin.wikiwikiweb.de/]$
 * [http://moinmoin.wikiwikiweb.de/ MoinMoin Wiki]$
 * [http://moinmoin.wikiwikiweb.de/wiki/moinmoin.png]$
 * http://moinmoin.wikiwikiweb.de/wiki/moinmoin.png$
 * [http://moinmoin.wikiwikiweb.de/wiki/moinmoin.png moinmoin.png]$
 * MeatBall:InterWiki$
 * wiki:MeatBall/InterWiki$
 * [wiki:MeatBall/InterWiki]$
 * [wiki:MeatBall/InterWiki InterWiki page on MeatBall]$
 * [file://///servername/share/full/path/to/file/filename%20with%20spaces.txt link to file filename with spaces.txt]$
 * user@example.com$
$
== Avoid or Limit Automatical Linking ==$
{{{$
 * Wiki''''''Name$
 * Wiki``Name$
 * !WikiName$
 * WikiName''''''s$
 * WikiName``s$
 * `http://www.example.com`$
}}}$
 * Wiki''''''Name$
 * Wiki``Name$
 * !WikiName$
 * WikiName''''''s$
 * WikiName``s$
 * `http://www.example.com`$
$
= Blockquotes and Indentions =$
{{{$
 indented text$
  text indented to the 2nd level$
}}}$
 indented text$
  text indented to the 2nd level$
$
= Lists =$
'''''see:''' HelpOnLists''$
== Unordered Lists ==$
{{{$
 * item 1$
$
 * item 2 (preceding white space)$
  * item 2.1$
   * item 2.1.1$
 * item 3$
  . item 3.1 (bulletless)$
 . item 4 (bulletless)$
  * item 4.1$
   . item 4.1.1 (bulletless)$
}}}$
 * item 1$
$
 * item 2 (preceding white space)$
  * item 2.1$
   * item 2.1.1$
 * item 3$
  . item 3.1 (bulletless)$
 . item 4 (bulletless)$
  * item 4.1$
   . item 4.1.1 (bulletless)$
$
== Ordered Lists ==$
=== with Numbers ===$
{{{$
 1. item 1$
   1. item 1.1$
   1. item 1.2$
 1. item 2$
}}}$
 1. item 1$
   1. item 1.1$
   1. item 1.2$
 1. item 2$
$
=== with Roman Numbers ===$
{{{$
 I. item 1$
   i. item 1.1$
   i. item 1.2$
 I. item 2$
}}}$
 I. item 1$
   i. item 1.1$
   i. item 1.2$
 I. item 2$
$
=== with Letters ===$
{{{$
 A. item A$
   a. item A. a)$
   a. item A. b)$
 A. item B$
}}}$
 A. item A$
   a. item A. a)$
   a. item A. b)$
 A. item B$
$
== Definition Lists ==$
{{{$
 term:: definition$
 object:: description 1$
 :: description 2$
 Action Items::$
 :: First Item$
 :: Second Item$
}}}$
 term:: definition$
 object:: description 1$
 :: description 2$
 Action Items::$
 :: First Item$
 :: Second Item$
$
= Horizontal Rules =$
'''''see:''' HelpOnRules''$
{{{$
----$
-----$
------$
-------$
--------$
---------$
----------$
}}}$
----$
-----$
------$
-------$
--------$
---------$
----------$
$
= Tables =$
'''''see:''' HelpOnTables''$
== Tables ==$
{{{$
||'''A'''||'''B'''||'''C'''||$
||1      ||2      ||3      ||$
}}}$
||'''A'''||'''B'''||'''C'''||$
||1      ||2      ||3      ||$
$
== Cell Width ==$
{{{$
||minimal width ||<99%>maximal width ||$
}}}$
||minimal width ||<99%>maximal width ||$
$
== Spanning Rows and Columns  ==$
{{{$
||<|2> cell spanning 2 rows ||cell in the 2nd column ||$
||cell in the 2nd column of the 2nd row ||$
||<-2> cell spanning 2 columns ||$
||||use empty cells as a shorthand ||$
}}}$
||<|2> cell spanning 2 rows ||cell in the 2nd column ||$
||cell in the 2nd column of the 2nd row ||$
||<-2> cell spanning 2 columns ||$
||||use empty cells as a shorthand ||$
$
== Alignment of Cell Contents ==$
{{{$
||<^|3> top (combined) ||<:99%> center (combined) ||<v|3> bottom (combined) ||$
||<)> right ||$
||<(> left ||$
}}}$
||<^|3> top (combined) ||<:99%> center (combined) ||<v|3> bottom (combined) ||$
||<)> right ||$
||<(> left ||$
$
== Coulored Table Cells ==$
{{{$
||<#0000FF> blue ||<#00FF00> green    ||<#FF0000> red    ||$
||<#00FFFF> cyan ||<#FF00FF> magenta  ||<#FFFF00> yellow ||$
}}}$
||<#0000FF> blue ||<#00FF00> green    ||<#FF0000> red    ||$
||<#00FFFF> cyan ||<#FF00FF> magenta  ||<#FFFF00> yellow ||$
$
== HTML-like Options for Tables ==$
{{{$
||A ||<rowspan="2"> like <|2> ||$
||<bgcolor="#00FF00"> like <#00FF00> ||$
||<colspan="2"> like <-2>||$
}}}$
||A ||<rowspan="2"> like <|2> ||$
||<bgcolor="#00FF00"> like <#00FF00> ||$
||<colspan="2"> like <-2>||$
$
= Macros and Variables =$
== Macros ==$
'''''see:''' HelpOnMacros''$
 * `[[Anchor(anchorname)]]` inserts a link anchor `anchorname`$
 * `[[BR]]` inserts a hard line break$
 * `[[FootNote(Note)]]` inserts a footnote saying `Note`$
 * `[[Include(HelpOnMacros/Include)]]` inserts the contents of the page `HelpOnMacros/Include` inline$
 * `[[MailTo(user AT example DOT com)]]` obfuscates the email address `user@example.com` to users not logged in$
$
== Variables ==$
'''''see:''' HelpOnVariables''$
 * `@``SIG``@` inserts your login name and timestamp of modification$
 * `@``TIME``@` inserts date and time of modification$
$
= Smileys and Icons =$
'''''see:''' HelpOnSmileys''$
[[ShowSmileys]]$
$
= Source code =$
'''''see:''' HelpOnParsers''$
== Verbatim Display ==$
{{{$
{ { {$
def hello():$
    print "Hello World!"$
} } }$
}}}$
/!\ Remove spaces between "`{ { {`" and "`} } }`".$
{{{$
def hello():$
    print "Hello World!"$
}}}$
$
== Syntax Highlighting ==$
{{{$
{ { {#!python$
def hello():$
    print "Hello World!"$
} } }$
}}}$
/!\ Remove spaces between "`{ { {`" and "`} } }`".$
{{{#!python$
def hello():$
    print "Hello World!"$
}}}$

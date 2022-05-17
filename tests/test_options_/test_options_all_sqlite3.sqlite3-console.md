     1^ISQLite version 3.4.2$
     2^IEnter ".help" for instructions$
     3^I[01msqlite>[39;49;00m[37m [39;49;00m.[34mschema[39;49;00m[37m[39;49;00m$
     4^ICREATE TABLE paste (paste_id integer, code text, parsed_code text, pub_date$
     5^Ivarchar(24), language varchar(64), parent_id integer, url varchar(128));$
     6^ICREATE TABLE vars (key varchar(24), value varchar(128));$
     7^I[01msqlite>[39;49;00m[37m [39;49;00ma[37m [39;49;00m[33m'[39;49;00m$
     8^I[01m   ...>[39;49;00m[37m [39;49;00m[33m'[39;49;00m[37m[39;49;00m$
     9^I[01m   ...>[39;49;00m[37m [39;49;00m;[37m[39;49;00m$
    10^ISQL error: near "a": syntax error$
    11^I[01msqlite>[39;49;00m[37m [39;49;00m%;[37m[39;49;00m$
    12^ISQL error: near "%": syntax error$
    13^I[01msqlite>[39;49;00m[37m [39;49;00m[34mselect[39;49;00m[37m [39;49;00m[34mcount[39;49;00m([34mlanguage[39;49;00m),[37m [39;49;00m[34mlanguage[39;49;00m[37m [39;49;00m[34mfrom[39;49;00m[37m [39;49;00mpaste[37m [39;49;00m[34mgroup[39;49;00m[37m [39;49;00m[34mby[39;49;00m[37m [39;49;00m[34mlanguage[39;49;00m[37m [39;49;00m[34morder[39;49;00m[37m[39;49;00m$
    14^I[01m   ...>[39;49;00m[37m [39;49;00m[34mby[39;49;00m[37m [39;49;00m[34mcount[39;49;00m([34mlanguage[39;49;00m)[37m [39;49;00m[34mdesc[39;49;00m;[37m[39;49;00m$
    15^I144|python$
    16^I76|text$
    17^I22|pycon$
    18^I9|ruby$
    19^I7|c$
    20^I7|js$
    21^I6|html+django$
    22^I4|html$
    23^I4|tex$
    24^I2|html+php$
    25^I1|cpp$
    26^I1|scheme$
    27^I$

     1	SQLite version 3.4.2$
     2	Enter ".help" for instructions$
     3	[01msqlite>[39;49;00m[37m [39;49;00m.[34mschema[39;49;00m[37m[39;49;00m$
     4	CREATE TABLE paste (paste_id integer, code text, parsed_code text, pub_date$
     5	varchar(24), language varchar(64), parent_id integer, url varchar(128));$
     6	CREATE TABLE vars (key varchar(24), value varchar(128));$
     7	[01msqlite>[39;49;00m[37m [39;49;00ma[37m [39;49;00m[33m'[39;49;00m$
     8	[01m   ...>[39;49;00m[37m [39;49;00m[33m'[39;49;00m[37m[39;49;00m$
     9	[01m   ...>[39;49;00m[37m [39;49;00m;[37m[39;49;00m$
    10	SQL error: near "a": syntax error$
    11	[01msqlite>[39;49;00m[37m [39;49;00m%;[37m[39;49;00m$
    12	SQL error: near "%": syntax error$
    13	[01msqlite>[39;49;00m[37m [39;49;00m[34mselect[39;49;00m[37m [39;49;00m[34mcount[39;49;00m([34mlanguage[39;49;00m),[37m [39;49;00m[34mlanguage[39;49;00m[37m [39;49;00m[34mfrom[39;49;00m[37m [39;49;00mpaste[37m [39;49;00m[34mgroup[39;49;00m[37m [39;49;00m[34mby[39;49;00m[37m [39;49;00m[34mlanguage[39;49;00m[37m [39;49;00m[34morder[39;49;00m[37m[39;49;00m$
    14	[01m   ...>[39;49;00m[37m [39;49;00m[34mby[39;49;00m[37m [39;49;00m[34mcount[39;49;00m([34mlanguage[39;49;00m)[37m [39;49;00m[34mdesc[39;49;00m;[37m[39;49;00m$
    15	144|python$
    16	76|text$
    17	22|pycon$
    18	9|ruby$
    19	7|c$
    20	7|js$
    21	6|html+django$
    22	4|html$
    23	4|tex$
    24	2|html+php$
    25	1|cpp$
    26	1|scheme$
    27	$

     1^Iregression=# select foo;$
     2^IERROR:  column "foo" does not exist$
     3^ICONTEXT:  PL/pgSQL function "test1" while casting return value to function's return type$
     4^ILINE 1: select foo;$
     5^I               ^$
     6^Iregression=# \q$
     7^I$
     8^Ipeter@localhost testdb=> \a \t \x$
     9^IOutput format is aligned.$
    10^ITuples only is off.$
    11^IExpanded display is on.$
    12^I$
    13^Iregression=# select '\x';$
    14^IWARNING:  nonstandard use of escape in a string literal$
    15^ILINE 1: select '\x';$
    16^I               ^$
    17^IHINT:  Use the escape string syntax for escapes, e.g., E'\r\n'.$
    18^I ?column? $
    19^I----------$
    20^I x$
    21^I(1 row)$
    22^I$
    23^Iregression=# select E'\x';$
    24^I$
    25^Ipiro=> \set foo 30;$
    26^Ipiro=> select * from test where foo <= :foo;$
    27^I foo | bar $
    28^I-----+-----$
    29^I  10 | $
    30^I  20 | $
    31^I(2 rows)$
    32^I$
    33^Itestdb=> \set foo 'my_table'$
    34^Itestdb=> SELECT * FROM :"foo";$
    35^I$
    36^Itestdb=> \set content `cat my_file.txt`$
    37^Itestdb=> INSERT INTO my_table VALUES (:'content');$
    38^I$
    39^Iregression=# select ($
    40^Iregression(# 1);$
    41^I ?column? $
    42^I----------$
    43^I        1$
    44^I(1 row)$
    45^I$
    46^Ipiro=> select ($
    47^Ipiro(> '$
    48^Ipiro'> ' || $$$
    49^Ipiro$> $$)$
    50^Ipiro-> from "$
    51^Ipiro"> foo";$
    52^IERROR:  relation "$
    53^Ifoo" does not exist$
    54^ILINE 5: from "$
    55^I             ^$
    56^I$
    57^Itestdb=> CREATE TABLE my_table ($
    58^Ifirst integer not null default 0,$
    59^Isecond text) ; -- end of command$
    60^ICREATE TABLE$
    61^I$
    62^I-- Table output$
    63^I=# SELECT '0x10'::mpz AS "hex", '10'::mpz AS "dec",$
    64^I-#        '010'::mpz AS oct, '0b10'::mpz AS bin;$
    65^I hex | dec | oct | bin$
    66^I-----+-----+-----+-----$
    67^I 16  | 10  | 8   | 2$
    68^I(1 row)$
    69^I$
    70^I-- One field output$
    71^Iregression=# select schemaname from  pg_tables limit 3;$
    72^I schemaname $
    73^I------------$
    74^I pg_catalog$
    75^I pg_catalog$
    76^I pg_catalog$
    77^I(3 rows)$
    78^I$
    79^I-- TODO: prompt in multiline comments still not handled correctly$
    80^Itest=> select 1 /* multiline$
    81^Itest*> and 2 /* and 3 */$
    82^Itest*> end comment */, 2;$
    83^I ?column? | ?column? $
    84^I----------+----------$
    85^I        1 |        2$
    86^I$
    87^I=# select 10.0, 1e-6, 1E+6;$
    88^I ?column? | ?column? | ?column? $
    89^I----------+----------+----------$
    90^I     10.0 | 0.000001 |  1000000$
    91^I(1 row)$
    92^I$
    93^Iregression=# begin;$
    94^IBEGIN$
    95^Iregression=# create table asdf (foo serial primary key);$
    96^INOTICE:  CREATE TABLE will create implicit sequence "asdf_foo_seq" for serial column "asdf.foo"$
    97^INOTICE:  CREATE TABLE / PRIMARY KEY will create implicit index "asdf_pkey" for table "asdf"$
    98^ICREATE TABLE$
    99^Iregression=# insert into asdf values (10) returning foo;$
   100^I foo $
   101^I-----$
   102^I  10$
   103^I(1 row)$
   104^I$
   105^IINSERT 0 1$
   106^Iregression=# ROLLBACK ;$
   107^IROLLBACK$
   108^I$
   109^I=> EXPLAIN SELECT * FROM tenk1$
   110^I-> WHERE unique1 < 100;   -- Don't take -> in the plan as a prompt$
   111^I$
   112^I                                  QUERY PLAN$
   113^I------------------------------------------------------------------------------$
   114^I Bitmap Heap Scan on tenk1  (cost=2.37..232.35 rows=106 width=244)$
   115^I   Recheck Cond: (unique1 < 100)$
   116^I   ->  Bitmap Index Scan on tenk1_unique1  (cost=0.00..2.37 rows=106 width=0)$
   117^I         Index Cond: (unique1 < 100)$
   118^I$
   119^I$
   120^I-- don't swallow the end of a malformed line$
   121^Itest=> select 1,$
   122^I'this line must be emitted'$

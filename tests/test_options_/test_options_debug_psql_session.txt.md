Using lexer <pygments.lexers.TextLexer with {'ensurenl': False, 'tabsize': 0}>
regression=# select foo;
ERROR:  column "foo" does not exist
CONTEXT:  PL/pgSQL function "test1" while casting return value to function's return type
LINE 1: select foo;
               ^
regression=# \q

peter@localhost testdb=> \a \t \x
Output format is aligned.
Tuples only is off.
Expanded display is on.

regression=# select '\x';
WARNING:  nonstandard use of escape in a string literal
LINE 1: select '\x';
               ^
HINT:  Use the escape string syntax for escapes, e.g., E'\r\n'.
 ?column?
----------
 x
(1 row)

regression=# select E'\x';

piro=> \set foo 30;
piro=> select * from test where foo <= :foo;
 foo | bar
-----+-----
  10 |
  20 |
(2 rows)

testdb=> \set foo 'my_table'
testdb=> SELECT * FROM :"foo";

testdb=> \set content `cat my_file.txt`
testdb=> INSERT INTO my_table VALUES (:'content');

regression=# select (
regression(# 1);
 ?column?
----------
        1
(1 row)

piro=> select (
piro(> '
piro'> ' || $$
piro$> $$)
piro-> from "
piro"> foo";
ERROR:  relation "
foo" does not exist
LINE 5: from "
             ^

testdb=> CREATE TABLE my_table (
first integer not null default 0,
second text) ; -- end of command
CREATE TABLE

-- Table output
=# SELECT '0x10'::mpz AS "hex", '10'::mpz AS "dec",
-#        '010'::mpz AS oct, '0b10'::mpz AS bin;
 hex | dec | oct | bin
-----+-----+-----+-----
 16  | 10  | 8   | 2
(1 row)

-- One field output
regression=# select schemaname from  pg_tables limit 3;
 schemaname
------------
 pg_catalog
 pg_catalog
 pg_catalog
(3 rows)

-- TODO: prompt in multiline comments still not handled correctly
test=> select 1 /* multiline
test*> and 2 /* and 3 */
test*> end comment */, 2;
 ?column? | ?column?
----------+----------
        1 |        2

=# select 10.0, 1e-6, 1E+6;
 ?column? | ?column? | ?column?
----------+----------+----------
     10.0 | 0.000001 |  1000000
(1 row)

regression=# begin;
BEGIN
regression=# create table asdf (foo serial primary key);
NOTICE:  CREATE TABLE will create implicit sequence "asdf_foo_seq" for serial column "asdf.foo"
NOTICE:  CREATE TABLE / PRIMARY KEY will create implicit index "asdf_pkey" for table "asdf"
CREATE TABLE
regression=# insert into asdf values (10) returning foo;
 foo
-----
  10
(1 row)

INSERT 0 1
regression=# ROLLBACK ;
ROLLBACK

=> EXPLAIN SELECT * FROM tenk1
-> WHERE unique1 < 100;   -- Don't take -> in the plan as a prompt

                                  QUERY PLAN
------------------------------------------------------------------------------
 Bitmap Heap Scan on tenk1  (cost=2.37..232.35 rows=106 width=244)
   Recheck Cond: (unique1 < 100)
   ->  Bitmap Index Scan on tenk1_unique1  (cost=0.00..2.37 rows=106 width=0)
         Index Cond: (unique1 < 100)


-- don't swallow the end of a malformed line
test=> select 1,
'this line must be emitted'

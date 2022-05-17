     1^ICREATE OR REPLACE FUNCTION something() RETURNS int4 AS$
     2^I$x$$
     3^IBEGIN$
     4^I    RETURN 42;$
     5^IEND$
     6^I$x$$
     7^ILANGUAGE 'plpgsql';$
     8^I$
     9^ICREATE FUNCTION pymax (a integer, b integer)$
    10^I  RETURNS integer$
    11^IAS $$$
    12^I  if a > b:$
    13^I    return a$
    14^I  return b$
    15^I$$ language plpythonu;$
    16^I$
    17^ICREATE FUNCTION nested_lexers (a integer, b integer)$
    18^I$function$$
    19^IBEGIN$
    20^I    SELECT ($1 ~ $q$[\t\r\n\v\\]$q$);$
    21^IEND;$
    22^I$function$$
    23^ILANGUAGE sql;$
    24^I$
    25^ICREATE OR REPLACE FUNCTION measurement_insert_trigger()$
    26^IRETURNS TRIGGER AS $$$
    27^IBEGIN$
    28^I    <<test>>$
    29^I    INSERT INTO measurement_y2008m01 VALUES (NEW.*);$
    30^I    RETURN NULL;$
    31^IEND;$
    32^I$$$
    33^ILANGUAGE plpgsql;$
    34^I$
    35^I-- As returned by pg_dump$
    36^ICREATE FUNCTION test_function() RETURNS integer$
    37^I    LANGUAGE plpgsql STABLE STRICT$
    38^I    AS $$$
    39^Ibegin$
    40^I    return 42;$
    41^Iend$
    42^I$$;$
    43^I$
    44^I-- Unicode names and strings$
    45^ISELECT U&'\0441\043B\043E\043D'$
    46^IFROM U&"\0441\043B\043E\043D";$
    47^I$
    48^I-- Escapes$
    49^ISELECT E'1\n2\n3';$
    50^I$
    51^I-- DO example from postgresql documentation$
    52^I/*$
    53^I * PostgreSQL is Copyright © 1996-2016 by the PostgreSQL Global Development Group.$
    54^I * $
    55^I * Postgres95 is Copyright © 1994-5 by the Regents of the University of California.$
    56^I * $
    57^I * Permission to use, copy, modify, and distribute this software and its$
    58^I * documentation for any purpose, without fee, and without a written agreement$
    59^I * is hereby granted, provided that the above copyright notice and this paragraph$
    60^I * and the following two paragraphs appear in all copies.$
    61^I * $
    62^I * IN NO EVENT SHALL THE UNIVERSITY OF CALIFORNIA BE LIABLE TO ANY PARTY FOR$
    63^I * DIRECT, INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES, INCLUDING$
    64^I * LOST PROFITS, ARISING OUT OF THE USE OF THIS SOFTWARE AND ITS DOCUMENTATION,$
    65^I * EVEN IF THE UNIVERSITY OF CALIFORNIA HAS BEEN ADVISED OF THE POSSIBILITY OF$
    66^I * SUCH DAMAGE.$
    67^I * $
    68^I * THE UNIVERSITY OF CALIFORNIA SPECIFICALLY DISCLAIMS ANY WARRANTIES, INCLUDING,$
    69^I * BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR$
    70^I * A PARTICULAR PURPOSE. THE SOFTWARE PROVIDED HEREUNDER IS ON AN "AS-IS" BASIS,$
    71^I * AND THE UNIVERSITY OF CALIFORNIA HAS NO OBLIGATIONS TO PROVIDE MAINTENANCE,$
    72^I * SUPPORT, UPDATES, ENHANCEMENTS, OR MODIFICATIONS.$
    73^I */$
    74^IDO $$DECLARE r record;$
    75^IBEGIN$
    76^I    FOR r IN SELECT table_schema, table_name FROM information_schema.tables$
    77^I             WHERE table_type = 'VIEW' AND table_schema = 'public'$
    78^I    LOOP$
    79^I        EXECUTE 'GRANT ALL ON ' || quote_ident(r.table_schema) || '.' || quote_ident(r.table_name) || ' TO webuser';$
    80^I    END LOOP;$
    81^IEND$$;$

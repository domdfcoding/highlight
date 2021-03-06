CREATE OR REPLACE FUNCTION something() RETURNS int4 AS
$x$
BEGIN
    RETURN 42;
END
$x$
LANGUAGE 'plpgsql';

CREATE FUNCTION pymax (a integer, b integer)
  RETURNS integer
AS $$
  if a > b:
    return a
  return b
$$ language plpythonu;

CREATE FUNCTION nested_lexers (a integer, b integer)
$function$
BEGIN
    SELECT ($1 ~ $q$[\t\r\n\v\\]$q$);
END;
$function$
LANGUAGE sql;

CREATE OR REPLACE FUNCTION measurement_insert_trigger()
RETURNS TRIGGER AS $$
BEGIN
    <<test>>
    INSERT INTO measurement_y2008m01 VALUES (NEW.*);
    RETURN NULL;
END;
$$
LANGUAGE plpgsql;

-- As returned by pg_dump
CREATE FUNCTION test_function() RETURNS integer
    LANGUAGE plpgsql STABLE STRICT
    AS $$
begin
    return 42;
end
$$;

-- Unicode names and strings
SELECT U&'\0441\043B\043E\043D'
FROM U&"\0441\043B\043E\043D";

-- Escapes
SELECT E'1\n2\n3';

-- DO example from postgresql documentation
/*
 * PostgreSQL is Copyright © 1996-2016 by the PostgreSQL Global Development Group.
 *
 * Postgres95 is Copyright © 1994-5 by the Regents of the University of California.
 *
 * Permission to use, copy, modify, and distribute this software and its
 * documentation for any purpose, without fee, and without a written agreement
 * is hereby granted, provided that the above copyright notice and this paragraph
 * and the following two paragraphs appear in all copies.
 *
 * IN NO EVENT SHALL THE UNIVERSITY OF CALIFORNIA BE LIABLE TO ANY PARTY FOR
 * DIRECT, INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES, INCLUDING
 * LOST PROFITS, ARISING OUT OF THE USE OF THIS SOFTWARE AND ITS DOCUMENTATION,
 * EVEN IF THE UNIVERSITY OF CALIFORNIA HAS BEEN ADVISED OF THE POSSIBILITY OF
 * SUCH DAMAGE.
 *
 * THE UNIVERSITY OF CALIFORNIA SPECIFICALLY DISCLAIMS ANY WARRANTIES, INCLUDING,
 * BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
 * A PARTICULAR PURPOSE. THE SOFTWARE PROVIDED HEREUNDER IS ON AN "AS-IS" BASIS,
 * AND THE UNIVERSITY OF CALIFORNIA HAS NO OBLIGATIONS TO PROVIDE MAINTENANCE,
 * SUPPORT, UPDATES, ENHANCEMENTS, OR MODIFICATIONS.
 */
DO $$DECLARE r record;
BEGIN
    FOR r IN SELECT table_schema, table_name FROM information_schema.tables
             WHERE table_type = 'VIEW' AND table_schema = 'public'
    LOOP
        EXECUTE 'GRANT ALL ON ' || quote_ident(r.table_schema) || '.' || quote_ident(r.table_name) || ' TO webuser';
    END LOOP;
END$$;

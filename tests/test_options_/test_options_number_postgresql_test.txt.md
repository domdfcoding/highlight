     1	CREATE OR REPLACE FUNCTION something() RETURNS int4 AS
     2	$x$
     3	BEGIN
     4	    RETURN 42;
     5	END
     6	$x$
     7	LANGUAGE 'plpgsql';
     8
     9	CREATE FUNCTION pymax (a integer, b integer)
    10	  RETURNS integer
    11	AS $$
    12	  if a > b:
    13	    return a
    14	  return b
    15	$$ language plpythonu;
    16
    17	CREATE FUNCTION nested_lexers (a integer, b integer)
    18	$function$
    19	BEGIN
    20	    SELECT ($1 ~ $q$[\t\r\n\v\\]$q$);
    21	END;
    22	$function$
    23	LANGUAGE sql;
    24
    25	CREATE OR REPLACE FUNCTION measurement_insert_trigger()
    26	RETURNS TRIGGER AS $$
    27	BEGIN
    28	    <<test>>
    29	    INSERT INTO measurement_y2008m01 VALUES (NEW.*);
    30	    RETURN NULL;
    31	END;
    32	$$
    33	LANGUAGE plpgsql;
    34
    35	-- As returned by pg_dump
    36	CREATE FUNCTION test_function() RETURNS integer
    37	    LANGUAGE plpgsql STABLE STRICT
    38	    AS $$
    39	begin
    40	    return 42;
    41	end
    42	$$;
    43
    44	-- Unicode names and strings
    45	SELECT U&'\0441\043B\043E\043D'
    46	FROM U&"\0441\043B\043E\043D";
    47
    48	-- Escapes
    49	SELECT E'1\n2\n3';
    50
    51	-- DO example from postgresql documentation
    52	/*
    53	 * PostgreSQL is Copyright © 1996-2016 by the PostgreSQL Global Development Group.
    54	 *
    55	 * Postgres95 is Copyright © 1994-5 by the Regents of the University of California.
    56	 *
    57	 * Permission to use, copy, modify, and distribute this software and its
    58	 * documentation for any purpose, without fee, and without a written agreement
    59	 * is hereby granted, provided that the above copyright notice and this paragraph
    60	 * and the following two paragraphs appear in all copies.
    61	 *
    62	 * IN NO EVENT SHALL THE UNIVERSITY OF CALIFORNIA BE LIABLE TO ANY PARTY FOR
    63	 * DIRECT, INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES, INCLUDING
    64	 * LOST PROFITS, ARISING OUT OF THE USE OF THIS SOFTWARE AND ITS DOCUMENTATION,
    65	 * EVEN IF THE UNIVERSITY OF CALIFORNIA HAS BEEN ADVISED OF THE POSSIBILITY OF
    66	 * SUCH DAMAGE.
    67	 *
    68	 * THE UNIVERSITY OF CALIFORNIA SPECIFICALLY DISCLAIMS ANY WARRANTIES, INCLUDING,
    69	 * BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
    70	 * A PARTICULAR PURPOSE. THE SOFTWARE PROVIDED HEREUNDER IS ON AN "AS-IS" BASIS,
    71	 * AND THE UNIVERSITY OF CALIFORNIA HAS NO OBLIGATIONS TO PROVIDE MAINTENANCE,
    72	 * SUPPORT, UPDATES, ENHANCEMENTS, OR MODIFICATIONS.
    73	 */
    74	DO $$DECLARE r record;
    75	BEGIN
    76	    FOR r IN SELECT table_schema, table_name FROM information_schema.tables
    77	             WHERE table_type = 'VIEW' AND table_schema = 'public'
    78	    LOOP
    79	        EXECUTE 'GRANT ALL ON ' || quote_ident(r.table_schema) || '.' || quote_ident(r.table_name) || ' TO webuser';
    80	    END LOOP;
    81	END$$;

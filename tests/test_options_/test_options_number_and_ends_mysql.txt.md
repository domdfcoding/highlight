     1	-- Samples of MySQL parsing$
     2	$
     3	$
     4	-- Comments$
     5	# standalone comment line$
     6	-- standalone comment line$
     7	SELECT 1; -- trailing comment$
     8	SELECT 1; # trailing comment$
     9	SELECT 1; /* trailing comment */$
    10	SELECT /* interruption */  /**/ 1;$
    11	 /*$
    12	    Multiline / * / comment$
    13	 */$
    14	 /* /* MySQL does not support nested comments */$
    15	SELECT 'If this line is a comment then nested commenting is enabled (and therefore broken).';$
    16	$
    17	$
    18	-- Optimizer hints$
    19	SELECT /*+ SEMIJOIN(FIRSTMATCH, LOOSESCAN) */ 1;$
    20	SELECT /*+ SET_VAR(foreign_key_checks=OFF) */ 1;$
    21	$
    22	$
    23	-- Literals$
    24	SELECT$
    25	    -- Integers$
    26	    123,$
    27	$
    28	    -- Floats$
    29	    .123, 1.23, 123.,$
    30	$
    31	    -- Exponents$
    32	    1e10, 1e-10, 1.e20, .1e-20,$
    33	$
    34	    -- Hexadecimal$
    35	    X'0af019', x'0AF019', 0xaf019,$
    36	$
    37	    -- Binary$
    38	    B'010', b'010', 0b010,$
    39	$
    40	    -- Temporal literals$
    41	    {d'2020-01-01'}, { d ' 2020^01@01 ' },$
    42	    {t'8 9:10:11'}, { t ' 09:10:11.12 ' }, { t ' 091011 ' },$
    43	    {ts"2020-01-01 09:10:11"}, { ts ' 2020@01/01  09:10:11 ' },$
    44	$
    45	    -- Strings$
    46	    '', 'abc', '1''2\03\%4\_5\\6\'7\"8',$
    47	    "", "abc", "1""2\03\%4\_5\\6\'7\"8",$
    48	;$
    49	$
    50	$
    51	-- Variables$
    52	SET @a = 1, @1 = 2, @._.$ = 3;$
    53	SET @'?' = 1, @'abc''def"`ghi' = 2;$
    54	SET @"#" = 1, @"abc""def'`ghi" = 2;$
    55	SET @`^` = 1, @`abc``def'"ghi` = 2;$
    56	SELECT$
    57	    @@timestamp,$
    58	    @@global.auto_increment_offset,$
    59	    @@session.auto_increment_offset,$
    60	    @@auto_increment_offset$
    61	;$
    62	$
    63	$
    64	-- Prepared statements$
    65	SELECT POW(?, 3) AS cubed;$
    66	$
    67	$
    68	-- Constants$
    69	SELECT TRUE, FALSE, NULL, UNKNOWN;$
    70	$
    71	$
    72	-- Data types$
    73	CREATE TABLE table1 ($
    74	    id INT AUTO_INCREMENT PRIMARY KEY,$
    75	    name VARCHAR(20) NOT NULL,$
    76	    birthyear YEAR$
    77	);$
    78	$
    79	$
    80	-- Keywords$
    81	INSERT INTO table1 (person, birthyear) VALUES ('abc', 2020);$
    82	$
    83	WITH RECURSIVE example (n) AS ($
    84	    SELECT 1$
    85	    UNION ALL$
    86	    SELECT n + 1 FROM example$
    87	    WHERE n < 10$
    88	)$
    89	SELECT n FROM example;$
    90	$
    91	SELECT 17 MEMBER OF ('[23, "abc", 17, "ab", 10]');$
    92	$
    93	$
    94	-- Functions$
    95	SELECT CONCAT('function');$
    96	SELECT MAX(quantity) FROM example;$
    97	$
    98	$
    99	-- Schema object names$
   100	CREATE TABLE basic ($
   101	    example INT,$
   102	    股票编号 INT,$
   103	    `select` INT,$
   104	    `concat(` INT$
   105	);$
   106	$
   107	SELECT e1.`apple` AS a, `example2`.b$
   108	FROM example1 AS e1$
   109	JOIN example2 e2$
   110	ON `example1`.`a``b` = e2.`123`;$
   111	$
   112	$
   113	-- Operators$
   114	SELECT 1 + 2 - 3 << 2;$
   115	SELECT 1::DECIMAL(5, 2);$
   116	SET @a = 1;$
   117	SET a := 1;$
   118	SELECT c->>'$.name' FROM example;$
   119	$
   120	$
   121	$
   122	-- Exceptions$
   123	CREATE TABLE t1$
   124	($
   125	    c1 VARCHAR(5) CHARACTER SET latin1,$
   126	    c2 SET('r', 'g', 'b')$
   127	);$
   128	$
   129	$
   130	-- Introducers$
   131	SELECT _latin1'abc';$
   132	SELECT _binary'abc';$

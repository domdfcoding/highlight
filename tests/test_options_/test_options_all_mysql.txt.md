     1^I-- Samples of MySQL parsing$
     2^I$
     3^I$
     4^I-- Comments$
     5^I# standalone comment line$
     6^I-- standalone comment line$
     7^ISELECT 1; -- trailing comment$
     8^ISELECT 1; # trailing comment$
     9^ISELECT 1; /* trailing comment */$
    10^ISELECT /* interruption */  /**/ 1;$
    11^I /*$
    12^I    Multiline / * / comment$
    13^I */$
    14^I /* /* MySQL does not support nested comments */$
    15^ISELECT 'If this line is a comment then nested commenting is enabled (and therefore broken).';$
    16^I$
    17^I$
    18^I-- Optimizer hints$
    19^ISELECT /*+ SEMIJOIN(FIRSTMATCH, LOOSESCAN) */ 1;$
    20^ISELECT /*+ SET_VAR(foreign_key_checks=OFF) */ 1;$
    21^I$
    22^I$
    23^I-- Literals$
    24^ISELECT$
    25^I    -- Integers$
    26^I    123,$
    27^I$
    28^I    -- Floats$
    29^I    .123, 1.23, 123.,$
    30^I$
    31^I    -- Exponents$
    32^I    1e10, 1e-10, 1.e20, .1e-20,$
    33^I$
    34^I    -- Hexadecimal$
    35^I    X'0af019', x'0AF019', 0xaf019,$
    36^I$
    37^I    -- Binary$
    38^I    B'010', b'010', 0b010,$
    39^I$
    40^I    -- Temporal literals$
    41^I    {d'2020-01-01'}, { d ' 2020^01@01 ' },$
    42^I    {t'8 9:10:11'}, { t ' 09:10:11.12 ' }, { t ' 091011 ' },$
    43^I    {ts"2020-01-01 09:10:11"}, { ts ' 2020@01/01  09:10:11 ' },$
    44^I$
    45^I    -- Strings$
    46^I    '', 'abc', '1''2\03\%4\_5\\6\'7\"8',$
    47^I    "", "abc", "1""2\03\%4\_5\\6\'7\"8",$
    48^I;$
    49^I$
    50^I$
    51^I-- Variables$
    52^ISET @a = 1, @1 = 2, @._.$ = 3;$
    53^ISET @'?' = 1, @'abc''def"`ghi' = 2;$
    54^ISET @"#" = 1, @"abc""def'`ghi" = 2;$
    55^ISET @`^` = 1, @`abc``def'"ghi` = 2;$
    56^ISELECT$
    57^I    @@timestamp,$
    58^I    @@global.auto_increment_offset,$
    59^I    @@session.auto_increment_offset,$
    60^I    @@auto_increment_offset$
    61^I;$
    62^I$
    63^I$
    64^I-- Prepared statements$
    65^ISELECT POW(?, 3) AS cubed;$
    66^I$
    67^I$
    68^I-- Constants$
    69^ISELECT TRUE, FALSE, NULL, UNKNOWN;$
    70^I$
    71^I$
    72^I-- Data types$
    73^ICREATE TABLE table1 ($
    74^I    id INT AUTO_INCREMENT PRIMARY KEY,$
    75^I    name VARCHAR(20) NOT NULL,$
    76^I    birthyear YEAR$
    77^I);$
    78^I$
    79^I$
    80^I-- Keywords$
    81^IINSERT INTO table1 (person, birthyear) VALUES ('abc', 2020);$
    82^I$
    83^IWITH RECURSIVE example (n) AS ($
    84^I    SELECT 1$
    85^I    UNION ALL$
    86^I    SELECT n + 1 FROM example$
    87^I    WHERE n < 10$
    88^I)$
    89^ISELECT n FROM example;$
    90^I$
    91^ISELECT 17 MEMBER OF ('[23, "abc", 17, "ab", 10]');$
    92^I$
    93^I$
    94^I-- Functions$
    95^ISELECT CONCAT('function');$
    96^ISELECT MAX(quantity) FROM example;$
    97^I$
    98^I$
    99^I-- Schema object names$
   100^ICREATE TABLE basic ($
   101^I    example INT,$
   102^I    股票编号 INT,$
   103^I    `select` INT,$
   104^I    `concat(` INT$
   105^I);$
   106^I$
   107^ISELECT e1.`apple` AS a, `example2`.b$
   108^IFROM example1 AS e1$
   109^IJOIN example2 e2$
   110^ION `example1`.`a``b` = e2.`123`;$
   111^I$
   112^I$
   113^I-- Operators$
   114^ISELECT 1 + 2 - 3 << 2;$
   115^ISELECT 1::DECIMAL(5, 2);$
   116^ISET @a = 1;$
   117^ISET a := 1;$
   118^ISELECT c->>'$.name' FROM example;$
   119^I$
   120^I$
   121^I$
   122^I-- Exceptions$
   123^ICREATE TABLE t1$
   124^I($
   125^I    c1 VARCHAR(5) CHARACTER SET latin1,$
   126^I    c2 SET('r', 'g', 'b')$
   127^I);$
   128^I$
   129^I$
   130^I-- Introducers$
   131^ISELECT _latin1'abc';$
   132^ISELECT _binary'abc';$

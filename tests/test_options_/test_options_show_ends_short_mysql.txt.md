-- Samples of MySQL parsing$
$
$
-- Comments$
# standalone comment line$
-- standalone comment line$
SELECT 1; -- trailing comment$
SELECT 1; # trailing comment$
SELECT 1; /* trailing comment */$
SELECT /* interruption */  /**/ 1;$
 /*$
    Multiline / * / comment$
 */$
 /* /* MySQL does not support nested comments */$
SELECT 'If this line is a comment then nested commenting is enabled (and therefore broken).';$
$
$
-- Optimizer hints$
SELECT /*+ SEMIJOIN(FIRSTMATCH, LOOSESCAN) */ 1;$
SELECT /*+ SET_VAR(foreign_key_checks=OFF) */ 1;$
$
$
-- Literals$
SELECT$
    -- Integers$
    123,$
$
    -- Floats$
    .123, 1.23, 123.,$
$
    -- Exponents$
    1e10, 1e-10, 1.e20, .1e-20,$
$
    -- Hexadecimal$
    X'0af019', x'0AF019', 0xaf019,$
$
    -- Binary$
    B'010', b'010', 0b010,$
$
    -- Temporal literals$
    {d'2020-01-01'}, { d ' 2020^01@01 ' },$
    {t'8 9:10:11'}, { t ' 09:10:11.12 ' }, { t ' 091011 ' },$
    {ts"2020-01-01 09:10:11"}, { ts ' 2020@01/01  09:10:11 ' },$
$
    -- Strings$
    '', 'abc', '1''2\03\%4\_5\\6\'7\"8',$
    "", "abc", "1""2\03\%4\_5\\6\'7\"8",$
;$
$
$
-- Variables$
SET @a = 1, @1 = 2, @._.$ = 3;$
SET @'?' = 1, @'abc''def"`ghi' = 2;$
SET @"#" = 1, @"abc""def'`ghi" = 2;$
SET @`^` = 1, @`abc``def'"ghi` = 2;$
SELECT$
    @@timestamp,$
    @@global.auto_increment_offset,$
    @@session.auto_increment_offset,$
    @@auto_increment_offset$
;$
$
$
-- Prepared statements$
SELECT POW(?, 3) AS cubed;$
$
$
-- Constants$
SELECT TRUE, FALSE, NULL, UNKNOWN;$
$
$
-- Data types$
CREATE TABLE table1 ($
    id INT AUTO_INCREMENT PRIMARY KEY,$
    name VARCHAR(20) NOT NULL,$
    birthyear YEAR$
);$
$
$
-- Keywords$
INSERT INTO table1 (person, birthyear) VALUES ('abc', 2020);$
$
WITH RECURSIVE example (n) AS ($
    SELECT 1$
    UNION ALL$
    SELECT n + 1 FROM example$
    WHERE n < 10$
)$
SELECT n FROM example;$
$
SELECT 17 MEMBER OF ('[23, "abc", 17, "ab", 10]');$
$
$
-- Functions$
SELECT CONCAT('function');$
SELECT MAX(quantity) FROM example;$
$
$
-- Schema object names$
CREATE TABLE basic ($
    example INT,$
    股票编号 INT,$
    `select` INT,$
    `concat(` INT$
);$
$
SELECT e1.`apple` AS a, `example2`.b$
FROM example1 AS e1$
JOIN example2 e2$
ON `example1`.`a``b` = e2.`123`;$
$
$
-- Operators$
SELECT 1 + 2 - 3 << 2;$
SELECT 1::DECIMAL(5, 2);$
SET @a = 1;$
SET a := 1;$
SELECT c->>'$.name' FROM example;$
$
$
$
-- Exceptions$
CREATE TABLE t1$
($
    c1 VARCHAR(5) CHARACTER SET latin1,$
    c2 SET('r', 'g', 'b')$
);$
$
$
-- Introducers$
SELECT _latin1'abc';$
SELECT _binary'abc';$

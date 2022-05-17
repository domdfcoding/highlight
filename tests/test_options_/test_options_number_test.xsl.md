     1	[36m<?xml version="1.0" encoding="utf-8"?>[39;49;00m
     2	[34m<xsl:stylesheet[39;49;00m [36mversion=[39;49;00m[33m"1.0"[39;49;00m [36mxmlns:xsl=[39;49;00m[33m"http://www.w3.org/1999/XSL/Transform"[39;49;00m[94m>[39;49;00m
     3		[34m<xsl:output[39;49;00m [36mmethod=[39;49;00m[33m"xml"[39;49;00m[94m/>[39;49;00m
     4		[34m<xsl:template[39;49;00m [36mmatch=[39;49;00m[33m"/"[39;49;00m[94m>[39;49;00m
     5			[94m<customers[39;49;00m[94m>[39;49;00m
     6				[34m<xsl:apply-templates[39;49;00m [36mselect=[39;49;00m[33m"customers/customer[@Country='Germany']"[39;49;00m[94m/>[39;49;00m
     7			[94m</customers>[39;49;00m
     8		[34m</xsl:template>[39;49;00m
     9		[34m<xsl:template[39;49;00m [36mmatch=[39;49;00m[33m"customers"[39;49;00m[94m>[39;49;00m
    10			[34m<xsl:apply-templates[39;49;00m[94m/>[39;49;00m
    11
    12		[34m</xsl:template>[39;49;00m
    13		[34m<xsl:template[39;49;00m [36mmatch=[39;49;00m[33m"customer"[39;49;00m[94m>[39;49;00m
    14			[94m<customer[39;49;00m[94m>[39;49;00m
    15				[34m<xsl:attribute[39;49;00m [36mname=[39;49;00m[33m"CompanyName"[39;49;00m[94m>[39;49;00m[34m<xsl:value-of[39;49;00m [36mselect=[39;49;00m[33m"@CompanyName"[39;49;00m[94m/>[39;49;00m[34m</xsl:attribute>[39;49;00m
    16				[34m<xsl:attribute[39;49;00m [36mname=[39;49;00m[33m"CustomerID"[39;49;00m[94m>[39;49;00m[34m<xsl:value-of[39;49;00m [36mselect=[39;49;00m[33m"@CustomerID"[39;49;00m[94m/>[39;49;00m[34m</xsl:attribute>[39;49;00m
    17				[34m<xsl:attribute[39;49;00m [36mname=[39;49;00m[33m"Country"[39;49;00m[94m>[39;49;00m[34m<xsl:value-of[39;49;00m [36mselect=[39;49;00m[33m"@Country"[39;49;00m[94m/>[39;49;00m[34m</xsl:attribute>[39;49;00m
    18			[94m</customer>[39;49;00m
    19			[34m<xsl:apply-templates[39;49;00m[94m/>[39;49;00m
    20		[34m</xsl:template>[39;49;00m
    21
    22	[34m</xsl:stylesheet>[39;49;00m

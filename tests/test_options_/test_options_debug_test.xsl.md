Using lexer <pygments.lexers.XsltLexer with {'ensurenl': False, 'tabsize': 0}>
[36m<?xml version="1.0" encoding="utf-8"?>[39;49;00m
[34m<xsl:stylesheet[39;49;00m [36mversion=[39;49;00m[33m"1.0"[39;49;00m [36mxmlns:xsl=[39;49;00m[33m"http://www.w3.org/1999/XSL/Transform"[39;49;00m[94m>[39;49;00m
	[34m<xsl:output[39;49;00m [36mmethod=[39;49;00m[33m"xml"[39;49;00m[94m/>[39;49;00m
	[34m<xsl:template[39;49;00m [36mmatch=[39;49;00m[33m"/"[39;49;00m[94m>[39;49;00m
		[94m<customers[39;49;00m[94m>[39;49;00m
			[34m<xsl:apply-templates[39;49;00m [36mselect=[39;49;00m[33m"customers/customer[@Country='Germany']"[39;49;00m[94m/>[39;49;00m
		[94m</customers>[39;49;00m
	[34m</xsl:template>[39;49;00m
	[34m<xsl:template[39;49;00m [36mmatch=[39;49;00m[33m"customers"[39;49;00m[94m>[39;49;00m
		[34m<xsl:apply-templates[39;49;00m[94m/>[39;49;00m

	[34m</xsl:template>[39;49;00m
	[34m<xsl:template[39;49;00m [36mmatch=[39;49;00m[33m"customer"[39;49;00m[94m>[39;49;00m
		[94m<customer[39;49;00m[94m>[39;49;00m
			[34m<xsl:attribute[39;49;00m [36mname=[39;49;00m[33m"CompanyName"[39;49;00m[94m>[39;49;00m[34m<xsl:value-of[39;49;00m [36mselect=[39;49;00m[33m"@CompanyName"[39;49;00m[94m/>[39;49;00m[34m</xsl:attribute>[39;49;00m
			[34m<xsl:attribute[39;49;00m [36mname=[39;49;00m[33m"CustomerID"[39;49;00m[94m>[39;49;00m[34m<xsl:value-of[39;49;00m [36mselect=[39;49;00m[33m"@CustomerID"[39;49;00m[94m/>[39;49;00m[34m</xsl:attribute>[39;49;00m
			[34m<xsl:attribute[39;49;00m [36mname=[39;49;00m[33m"Country"[39;49;00m[94m>[39;49;00m[34m<xsl:value-of[39;49;00m [36mselect=[39;49;00m[33m"@Country"[39;49;00m[94m/>[39;49;00m[34m</xsl:attribute>[39;49;00m
		[94m</customer>[39;49;00m
		[34m<xsl:apply-templates[39;49;00m[94m/>[39;49;00m
	[34m</xsl:template>[39;49;00m

[34m</xsl:stylesheet>[39;49;00m

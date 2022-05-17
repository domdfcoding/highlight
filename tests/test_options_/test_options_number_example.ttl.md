     1	[34m@base[39;49;00m[37m  [39;49;00m[31m<http://example.com>[39;49;00m[37m [39;49;00m.
     2	[34m@prefix[39;49;00m[37m [39;49;00m[04m[36mdcterms:[39;49;00m[37m [39;49;00m[31m<http://purl.org/dc/terms/>[39;49;00m. [34m@prefix[39;49;00m[37m [39;49;00m[04m[36mxs:[39;49;00m[37m [39;49;00m[31m<http://www.w3.org/2001/XMLSchema>[39;49;00m[37m [39;49;00m.
     3	[34m@prefix[39;49;00m[37m [39;49;00m[04m[36mmads:[39;49;00m[37m [39;49;00m[31m<http://www.loc.gov/mads/rdf/v1#>[39;49;00m[37m [39;49;00m.
     4	[34m@prefix[39;49;00m[37m [39;49;00m[04m[36mskos:[39;49;00m[37m [39;49;00m[31m<http://www.w3.org/2004/02/skos/core#>[39;49;00m[37m [39;49;00m.
     5	[34mPREFIX[39;49;00m[37m [39;49;00m[04m[36mdc:[39;49;00m[37m [39;49;00m[31m<http://purl.org/dc/elements/1.1/>[39;49;00m[37m  [39;49;00m[37m# SPARQL-like syntax is OK[39;49;00m
     6	[34m@prefix[39;49;00m[37m [39;49;00m[04m[36m:[39;49;00m[37m [39;49;00m[31m<http://xmlns.com/foaf/0.1/>[39;49;00m[37m [39;49;00m.  [37m# empty prefix is OK[39;49;00m
     7
     8	[31m<http://example.org/#spiderman>[39;49;00m [31m<http://www.perceive.net/schemas/relationship/enemyOf>[39;49;00m [31m<http://example.org/#green-goblin>[39;49;00m .
     9
    10	[31m<#doc1>[39;49;00m [36ma[39;49;00m [31m<#document>[39;49;00m;
    11		[04m[36mdc[39;49;00m:[94mcreator[39;49;00m [33m"[39;49;00m[33mSmith[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mJones[39;49;00m[33m"[39;49;00m;
    12		:[94mknows[39;49;00m [31m<http://getopenid.com/jsmith>[39;49;00m;
    13		[04m[36mdcterms[39;49;00m:[94mhasPart[39;49;00m [ [37m# A comment[39;49;00m
    14			[04m[36mdc[39;49;00m:[94mtitle[39;49;00m [33m"[39;49;00m[33mSome title[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mSome other title[39;49;00m[33m"[39;49;00m;
    15			[04m[36mdc[39;49;00m:[94mcreator[39;49;00m [33m"[39;49;00m[33mبرشت، برتولد[39;49;00m[33m"[39;49;00m@ar;
    16			[04m[36mdc[39;49;00m:[94mdate[39;49;00m [33m"[39;49;00m[33m2009[39;49;00m[33m"[39;49;00m^^[04m[36mxs[39;49;00m:[94mdate[39;49;00m
    17		];
    18		[04m[36mdc[39;49;00m:[94mtitle[39;49;00m [33m"[39;49;00m[33mA sample title[39;49;00m[33m"[39;49;00m, [34m23.0[39;49;00m;
    19		[04m[36mdcterms[39;49;00m:[94misPartOf[39;49;00m [
    20			[04m[36mdc[39;49;00m:[94mtitle[39;49;00m [33m"[39;49;00m[33manother[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mtitle[39;49;00m[33m"[39;49;00m
    21		] ;
    22		:[94mexists[39;49;00m true .
    23
    24	[31m<http://data.ub.uio.no/realfagstermer/006839>[39;49;00m [36ma[39;49;00m [04m[36mmads[39;49;00m:[94mTopic[39;49;00m,
    25	    [04m[36mskos[39;49;00m:[94mConcept[39;49;00m ;
    26	    [04m[36mdcterms[39;49;00m:[94mcreated[39;49;00m [33m"[39;49;00m[33m2014-08-25[39;49;00m[33m"[39;49;00m^^[04m[36mxs[39;49;00m:[94mdate[39;49;00m ;
    27	    [04m[36mdcterms[39;49;00m:[94mmodified[39;49;00m [33m"[39;49;00m[33m2014-11-12[39;49;00m[33m"[39;49;00m^^[04m[36mxs[39;49;00m:[94mdate[39;49;00m ;
    28	    [04m[36mdcterms[39;49;00m:[94midentifier[39;49;00m [33m"[39;49;00m[33mREAL006839[39;49;00m[33m"[39;49;00m ;
    29	    [04m[36mskos[39;49;00m:[94mprefLabel[39;49;00m [33m"[39;49;00m[33mFlerbørstemarker[39;49;00m[33m"[39;49;00m@nb,
    30	        [33m"[39;49;00m[33mPolychaeta[39;49;00m[33m"[39;49;00m@la ;
    31	    [04m[36mskos[39;49;00m:[94maltLabel[39;49;00m [33m"[39;49;00m[33mFlerbørsteormer[39;49;00m[33m"[39;49;00m@nb,
    32	        [33m"[39;49;00m[33mMangebørstemark[39;49;00m[33m"[39;49;00m@nb,
    33	        [33m"[39;49;00m[33mMangebørsteormer[39;49;00m[33m"[39;49;00m@nb,
    34	        [33m"[39;49;00m[33mHavbørsteormer[39;49;00m[33m"[39;49;00m@nb,
    35	        [33m"[39;49;00m[33mHavbørstemarker[39;49;00m[33m"[39;49;00m@nb,
    36	        [33m"[39;49;00m[33mPolycheter[39;49;00m[33m"[39;49;00m@nb ;
    37	    [04m[36mskos[39;49;00m:[94minScheme[39;49;00m [31m<http://data.ub.uio.no/realfagstermer/>[39;49;00m ;
    38	    [04m[36mskos[39;49;00m:[94mnarrower[39;49;00m [31m<http://data.ub.uio.no/realfagstermer/018529>[39;49;00m,
    39	        [31m<http://data.ub.uio.no/realfagstermer/024538>[39;49;00m,
    40	        [31m<http://data.ub.uio.no/realfagstermer/026723>[39;49;00m ;
    41	    [04m[36mskos[39;49;00m:[94mexactMatch[39;49;00m [31m<http://ntnu.no/ub/data/tekord#NTUB17114>[39;49;00m,
    42	        [31m<http://dewey.info/class/592.62/e23/>[39;49;00m,
    43	        [31m<http://aims.fao.org/aos/agrovoc/c_29110>[39;49;00m .

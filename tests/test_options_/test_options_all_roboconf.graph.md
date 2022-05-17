     1^I[37m##################[39;49;00m$
     2^I[37m# A sample graph[39;49;00m$
     3^I[37m##################[39;49;00m$
     4^I$
     5^I[34mimport [39;49;00msome-definition.graph;$
     6^I[34mimport [39;49;00manother-definition.graph;$
     7^I$
     8^IVM {$
     9^I^Iinstaller : target;$
    10^I^Ichildren: deployable;$
    11^I}$
    12^I$
    13^I[34mfacet [39;49;00mdeployable {$
    14^I^I[37m# nothing[39;49;00m$
    15^I}$
    16^I$
    17^I[37m# Sample deployables[39;49;00m$
    18^Imysql {$
    19^I^IinsTaller: puppet;$
    20^I^Ifacets: deployable;$
    21^I^Iexports: ip, port = 3306;$
    22^I}$
    23^I$
    24^Itomcat {$
    25^I^Iinstaller: bash;$
    26^I^Ifacets: deployable;$
    27^I^Iexports: ip;$
    28^I^Ichildren: web-application;$
    29^I}$
    30^I$
    31^I[34mfacet [39;49;00mweb-application {$
    32^I^Iexports: full-path = undefined;$
    33^I}$
    34^I$
    35^Imy-war-1 {$
    36^I^Ifacets: web-application;$
    37^I^Iinstaller: file;$
    38^I^Iexports: full-path = apps/my-war-1;^I[37m# the relative path[39;49;00m$
    39^I^Iimports: mysql.*;$
    40^I}$

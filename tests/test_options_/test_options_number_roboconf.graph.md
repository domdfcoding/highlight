     1	[37m##################[39;49;00m
     2	[37m# A sample graph[39;49;00m
     3	[37m##################[39;49;00m
     4
     5	[34mimport [39;49;00msome-definition.graph;
     6	[34mimport [39;49;00manother-definition.graph;
     7
     8	VM {
     9		installer : target;
    10		children: deployable;
    11	}
    12
    13	[34mfacet [39;49;00mdeployable {
    14		[37m# nothing[39;49;00m
    15	}
    16
    17	[37m# Sample deployables[39;49;00m
    18	mysql {
    19		insTaller: puppet;
    20		facets: deployable;
    21		exports: ip, port = 3306;
    22	}
    23
    24	tomcat {
    25		installer: bash;
    26		facets: deployable;
    27		exports: ip;
    28		children: web-application;
    29	}
    30
    31	[34mfacet [39;49;00mweb-application {
    32		exports: full-path = undefined;
    33	}
    34
    35	my-war-1 {
    36		facets: web-application;
    37		installer: file;
    38		exports: full-path = apps/my-war-1;	[37m# the relative path[39;49;00m
    39		imports: mysql.*;
    40	}

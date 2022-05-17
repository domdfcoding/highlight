[37m##################[39;49;00m$
[37m# A sample graph[39;49;00m$
[37m##################[39;49;00m$
$
[34mimport [39;49;00msome-definition.graph;$
[34mimport [39;49;00manother-definition.graph;$
$
VM {$
	installer : target;$
	children: deployable;$
}$
$
[34mfacet [39;49;00mdeployable {$
	[37m# nothing[39;49;00m$
}$
$
[37m# Sample deployables[39;49;00m$
mysql {$
	insTaller: puppet;$
	facets: deployable;$
	exports: ip, port = 3306;$
}$
$
tomcat {$
	installer: bash;$
	facets: deployable;$
	exports: ip;$
	children: web-application;$
}$
$
[34mfacet [39;49;00mweb-application {$
	exports: full-path = undefined;$
}$
$
my-war-1 {$
	facets: web-application;$
	installer: file;$
	exports: full-path = apps/my-war-1;	[37m# the relative path[39;49;00m$
	imports: mysql.*;$
}$

[37m##################[39;49;00m$
[37m# A sample graph[39;49;00m$
[37m##################[39;49;00m$
$
[34mimport [39;49;00msome-definition.graph;$
[34mimport [39;49;00manother-definition.graph;$
$
VM {$
^Iinstaller : target;$
^Ichildren: deployable;$
}$
$
[34mfacet [39;49;00mdeployable {$
^I[37m# nothing[39;49;00m$
}$
$
[37m# Sample deployables[39;49;00m$
mysql {$
^IinsTaller: puppet;$
^Ifacets: deployable;$
^Iexports: ip, port = 3306;$
}$
$
tomcat {$
^Iinstaller: bash;$
^Ifacets: deployable;$
^Iexports: ip;$
^Ichildren: web-application;$
}$
$
[34mfacet [39;49;00mweb-application {$
^Iexports: full-path = undefined;$
}$
$
my-war-1 {$
^Ifacets: web-application;$
^Iinstaller: file;$
^Iexports: full-path = apps/my-war-1;^I[37m# the relative path[39;49;00m$
^Iimports: mysql.*;$
}$

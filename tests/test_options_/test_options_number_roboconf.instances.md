     1	[37m# Deal with imports[39;49;00m
     2	[34mimport [39;49;00mothers.instances;
     3
     4	[34minstance of [39;49;00mVM {
     5		name: VM-mysql;
     6		[34minstance of [39;49;00mmysql {
     7			name: MySQL;
     8		}
     9	}
    10
    11	[34minstance of [39;49;00mVM {
    12		name: VM ;
    13		count: 5;
    14
    15		[34mINSTANCE of [39;49;00mtomcat {
    16			name: Tomcat;
    17
    18			[34minstance of [39;49;00mmy-war-1 {
    19				name: my-war-1;
    20				full-path: apps/my-war;
    21			}
    22		}
    23	}

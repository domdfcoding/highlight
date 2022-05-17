[37m# Deal with imports[39;49;00m$
[34mimport [39;49;00mothers.instances;$
$
[34minstance of [39;49;00mVM {$
	name: VM-mysql;$
	[34minstance of [39;49;00mmysql {$
		name: MySQL;$
	}$
}$
$
[34minstance of [39;49;00mVM {$
	name: VM ;$
	count: 5;$
	$
	[34mINSTANCE of [39;49;00mtomcat {$
		name: Tomcat;$
		$
		[34minstance of [39;49;00mmy-war-1 {$
			name: my-war-1;$
			full-path: apps/my-war;$
		}$
	}$
}$

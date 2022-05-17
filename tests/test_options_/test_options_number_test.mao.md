     1	[37m## Single line comment[39;49;00m[37m[39;49;00m
     2	<!DOCTYPE html>
     3	[37m<%doc>[39;49;00m
     4	[37m    This is the base template[39;49;00m
     5	[37m</%doc>[39;49;00m
     6	<html>
     7	<head>
     8		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
     9		<meta name=viewport content="width=device-width, initial-scale=1">
    10	  	<title>
    11	[37m	  	[39;49;00m[36m%[39;49;00m [34mif[39;49;00m page.meta.get ([33m'[39;49;00m[33mtitle[39;49;00m[33m'[39;49;00m, [34mNone[39;49;00m) [35mand[39;49;00m page.url != [33m'[39;49;00m[33m/[39;49;00m[33m'[39;49;00m:
    12				/ [36m${[39;49;00mpage.url[36m}[39;49;00m[37m[39;49;00m
    13	[37m		[39;49;00m[36m%[39;49;00m[34m endif[39;49;00m
    14		</title>
    15		<link type="text/css" rel="stylesheet" href="/style.css" />
    16	</head>
    17	<body>
    18		<div class="header-wrapper">
    19		    <header>
    20		        <nav>
    21		            <ul>
    22	[37m					[39;49;00m[36m%[39;49;00m [34mfor[39;49;00m item [35min[39;49;00m site.data[[33m'[39;49;00m[33mmenu[39;49;00m[33m'[39;49;00m]:
    23							<li>
    24							<a href="[36m${[39;49;00mitem[[33m'[39;49;00m[33murl[39;49;00m[33m'[39;49;00m][36m}[39;49;00m">
    25	[37m							[39;49;00m[36m%[39;49;00m [34mif[39;49;00m [33m'[39;49;00m[33mimage[39;49;00m[33m'[39;49;00m [35min[39;49;00m item:
    26								<img src="[36m${[39;49;00mitem[[33m'[39;49;00m[33mimage[39;49;00m[33m'[39;49;00m][36m}[39;49;00m" height="12px">
    27	[37m							[39;49;00m[36m%[39;49;00m[34m endif[39;49;00m
    28								[36m${[39;49;00mitem[[33m'[39;49;00m[33mtitle[39;49;00m[33m'[39;49;00m][36m}[39;49;00m
    29							</a>
    30							</li>
    31	[37m					[39;49;00m[36m%[39;49;00m[34m endfor[39;49;00m
    32					</ul>
    33		    	</nav>
    34		    </header>
    35		</div>
    36		<div id="container">
    37			<section id="content">
    38			[36m${[39;49;00m[36mself[39;49;00m.body()[36m}[39;49;00m
    39			</section>
    40			<footer>
    41				<a href="#">Imprint</a>&nbsp;|&nbsp;<a href="#">Privacy policy</a>
    42			</footer>
    43	    </div>
    44		<script type="text/javascript">
    45		</script>
    46	</body>
    47	</html>

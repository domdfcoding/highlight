Using lexer <pygments.lexers.MakoLexer with {'ensurenl': False, 'tabsize': 0}>
[37m## Single line comment[39;49;00m[37m[39;49;00m
<!DOCTYPE html>
[37m<%doc>[39;49;00m
[37m    This is the base template[39;49;00m
[37m</%doc>[39;49;00m
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<meta name=viewport content="width=device-width, initial-scale=1">
  	<title>
[37m	  	[39;49;00m[36m%[39;49;00m [34mif[39;49;00m page.meta.get ([33m'[39;49;00m[33mtitle[39;49;00m[33m'[39;49;00m, [34mNone[39;49;00m) [35mand[39;49;00m page.url != [33m'[39;49;00m[33m/[39;49;00m[33m'[39;49;00m:
			/ [36m${[39;49;00mpage.url[36m}[39;49;00m[37m[39;49;00m
[37m		[39;49;00m[36m%[39;49;00m[34m endif[39;49;00m
	</title>
	<link type="text/css" rel="stylesheet" href="/style.css" />
</head>
<body>
	<div class="header-wrapper">
	    <header>
	        <nav>
	            <ul>
[37m					[39;49;00m[36m%[39;49;00m [34mfor[39;49;00m item [35min[39;49;00m site.data[[33m'[39;49;00m[33mmenu[39;49;00m[33m'[39;49;00m]:
						<li>
						<a href="[36m${[39;49;00mitem[[33m'[39;49;00m[33murl[39;49;00m[33m'[39;49;00m][36m}[39;49;00m">
[37m							[39;49;00m[36m%[39;49;00m [34mif[39;49;00m [33m'[39;49;00m[33mimage[39;49;00m[33m'[39;49;00m [35min[39;49;00m item:
							<img src="[36m${[39;49;00mitem[[33m'[39;49;00m[33mimage[39;49;00m[33m'[39;49;00m][36m}[39;49;00m" height="12px">
[37m							[39;49;00m[36m%[39;49;00m[34m endif[39;49;00m
							[36m${[39;49;00mitem[[33m'[39;49;00m[33mtitle[39;49;00m[33m'[39;49;00m][36m}[39;49;00m
						</a>
						</li>
[37m					[39;49;00m[36m%[39;49;00m[34m endfor[39;49;00m
				</ul>
	    	</nav>
	    </header>
	</div>
	<div id="container">
		<section id="content">
		[36m${[39;49;00m[36mself[39;49;00m.body()[36m}[39;49;00m
		</section>
		<footer>
			<a href="#">Imprint</a>&nbsp;|&nbsp;<a href="#">Privacy policy</a>
		</footer>
    </div>
	<script type="text/javascript">
	</script>
</body>
</html>

[37m## Single line comment[39;49;00m[37m[39;49;00m$
<!DOCTYPE html>$
[37m<%doc>[39;49;00m$
[37m    This is the base template[39;49;00m$
[37m</%doc>[39;49;00m$
<html>$
<head>$
^I<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />$
^I<meta name=viewport content="width=device-width, initial-scale=1">$
  ^I<title>$
[37m^I  ^I[39;49;00m[36m%[39;49;00m [34mif[39;49;00m page.meta.get ([33m'[39;49;00m[33mtitle[39;49;00m[33m'[39;49;00m, [34mNone[39;49;00m) [35mand[39;49;00m page.url != [33m'[39;49;00m[33m/[39;49;00m[33m'[39;49;00m:$
^I^I^I/ [36m${[39;49;00mpage.url[36m}[39;49;00m[37m[39;49;00m$
[37m^I^I[39;49;00m[36m%[39;49;00m[34m endif[39;49;00m$
^I</title>$
^I<link type="text/css" rel="stylesheet" href="/style.css" />$
</head>$
<body>$
^I<div class="header-wrapper">$
^I    <header>$
^I        <nav>$
^I            <ul>$
[37m^I^I^I^I^I[39;49;00m[36m%[39;49;00m [34mfor[39;49;00m item [35min[39;49;00m site.data[[33m'[39;49;00m[33mmenu[39;49;00m[33m'[39;49;00m]:$
^I^I^I^I^I^I<li>$
^I^I^I^I^I^I<a href="[36m${[39;49;00mitem[[33m'[39;49;00m[33murl[39;49;00m[33m'[39;49;00m][36m}[39;49;00m">$
[37m^I^I^I^I^I^I^I[39;49;00m[36m%[39;49;00m [34mif[39;49;00m [33m'[39;49;00m[33mimage[39;49;00m[33m'[39;49;00m [35min[39;49;00m item:$
^I^I^I^I^I^I^I<img src="[36m${[39;49;00mitem[[33m'[39;49;00m[33mimage[39;49;00m[33m'[39;49;00m][36m}[39;49;00m" height="12px">$
[37m^I^I^I^I^I^I^I[39;49;00m[36m%[39;49;00m[34m endif[39;49;00m$
^I^I^I^I^I^I^I[36m${[39;49;00mitem[[33m'[39;49;00m[33mtitle[39;49;00m[33m'[39;49;00m][36m}[39;49;00m$
^I^I^I^I^I^I</a>$
^I^I^I^I^I^I</li>$
[37m^I^I^I^I^I[39;49;00m[36m%[39;49;00m[34m endfor[39;49;00m$
^I^I^I^I</ul>$
^I    ^I</nav>$
^I    </header>$
^I</div>$
^I<div id="container">$
^I^I<section id="content">$
^I^I[36m${[39;49;00m[36mself[39;49;00m.body()[36m}[39;49;00m$
^I^I</section>$
^I^I<footer>$
^I^I^I<a href="#">Imprint</a>&nbsp;|&nbsp;<a href="#">Privacy policy</a>$
^I^I</footer>$
    </div>$
^I<script type="text/javascript">^I$
^I</script>$
</body>$
</html>$

     1^I[37m## Single line comment[39;49;00m[37m[39;49;00m$
     2^I<!DOCTYPE html>$
     3^I[37m<%doc>[39;49;00m$
     4^I[37m    This is the base template[39;49;00m$
     5^I[37m</%doc>[39;49;00m$
     6^I<html>$
     7^I<head>$
     8^I^I<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />$
     9^I^I<meta name=viewport content="width=device-width, initial-scale=1">$
    10^I  ^I<title>$
    11^I[37m^I  ^I[39;49;00m[36m%[39;49;00m [34mif[39;49;00m page.meta.get ([33m'[39;49;00m[33mtitle[39;49;00m[33m'[39;49;00m, [34mNone[39;49;00m) [35mand[39;49;00m page.url != [33m'[39;49;00m[33m/[39;49;00m[33m'[39;49;00m:$
    12^I^I^I^I/ [36m${[39;49;00mpage.url[36m}[39;49;00m[37m[39;49;00m$
    13^I[37m^I^I[39;49;00m[36m%[39;49;00m[34m endif[39;49;00m$
    14^I^I</title>$
    15^I^I<link type="text/css" rel="stylesheet" href="/style.css" />$
    16^I</head>$
    17^I<body>$
    18^I^I<div class="header-wrapper">$
    19^I^I    <header>$
    20^I^I        <nav>$
    21^I^I            <ul>$
    22^I[37m^I^I^I^I^I[39;49;00m[36m%[39;49;00m [34mfor[39;49;00m item [35min[39;49;00m site.data[[33m'[39;49;00m[33mmenu[39;49;00m[33m'[39;49;00m]:$
    23^I^I^I^I^I^I^I<li>$
    24^I^I^I^I^I^I^I<a href="[36m${[39;49;00mitem[[33m'[39;49;00m[33murl[39;49;00m[33m'[39;49;00m][36m}[39;49;00m">$
    25^I[37m^I^I^I^I^I^I^I[39;49;00m[36m%[39;49;00m [34mif[39;49;00m [33m'[39;49;00m[33mimage[39;49;00m[33m'[39;49;00m [35min[39;49;00m item:$
    26^I^I^I^I^I^I^I^I<img src="[36m${[39;49;00mitem[[33m'[39;49;00m[33mimage[39;49;00m[33m'[39;49;00m][36m}[39;49;00m" height="12px">$
    27^I[37m^I^I^I^I^I^I^I[39;49;00m[36m%[39;49;00m[34m endif[39;49;00m$
    28^I^I^I^I^I^I^I^I[36m${[39;49;00mitem[[33m'[39;49;00m[33mtitle[39;49;00m[33m'[39;49;00m][36m}[39;49;00m$
    29^I^I^I^I^I^I^I</a>$
    30^I^I^I^I^I^I^I</li>$
    31^I[37m^I^I^I^I^I[39;49;00m[36m%[39;49;00m[34m endfor[39;49;00m$
    32^I^I^I^I^I</ul>$
    33^I^I    ^I</nav>$
    34^I^I    </header>$
    35^I^I</div>$
    36^I^I<div id="container">$
    37^I^I^I<section id="content">$
    38^I^I^I[36m${[39;49;00m[36mself[39;49;00m.body()[36m}[39;49;00m$
    39^I^I^I</section>$
    40^I^I^I<footer>$
    41^I^I^I^I<a href="#">Imprint</a>&nbsp;|&nbsp;<a href="#">Privacy policy</a>$
    42^I^I^I</footer>$
    43^I    </div>$
    44^I^I<script type="text/javascript">^I$
    45^I^I</script>$
    46^I</body>$
    47^I</html>$

Using lexer <pygments.lexers.LiquidLexer with {'ensurenl': False, 'tabsize': 0}>
# This is an example file. Process it with `./pygmentize -O full -f html -o /liquid-example.html example.liquid`.

{%[37m [39;49;00m[94mraw[39;49;00m[37m [39;49;00m%}
some {{raw}} liquid syntax

{% raw %}
{%[37m [39;49;00m[94mendraw[39;49;00m[37m [39;49;00m%}

Just regular text - what happens?

{%[37m [39;49;00m[94mcomment[39;49;00m[37m [39;49;00m%}[37mM[39;49;00m[37my[39;49;00m[37m [39;49;00m[37ml[39;49;00m[37mo[39;49;00m[37mv[39;49;00m[37me[39;49;00m[37ml[39;49;00m[37my[39;49;00m[37m [39;49;00m[37m{[39;49;00m[37m{[39;49;00m[37mc[39;49;00m[37mo[39;49;00m[37mm[39;49;00m[37mm[39;49;00m[37me[39;49;00m[37mn[39;49;00m[37mt[39;49;00m[37m}[39;49;00m[37m}[39;49;00m[37m [39;49;00m[37m{[39;49;00m[37m%[39;49;00m[37m [39;49;00m[37mc[39;49;00m[37mo[39;49;00m[37mm[39;49;00m[37mm[39;49;00m[37me[39;49;00m[37mn[39;49;00m[37mt[39;49;00m[37m [39;49;00m[37m%[39;49;00m[37m}[39;49;00m{%[37m [39;49;00m[94mendcomment[39;49;00m[37m [39;49;00m%}

{%[37m [39;49;00m[94mcustom_tag[39;49;00m[37m [39;49;00m[36mparams[39;49;00m:[37m [39;49;00m[34mtrue[39;49;00m[37m [39;49;00m%}
{%[37m [39;49;00m[94mcustom_block[39;49;00m[37m [39;49;00m[36mmy[39;49;00m=[33m"abc"[39;49;00m[37m [39;49;00m[36mc[39;49;00m[37m [39;49;00m=[37m [39;49;00m[34mfalse[39;49;00m[37m [39;49;00m%}
	Just usual {{[31mliquid[39;49;00m}}.
{%[37m [39;49;00m[94mendcustom_block[39;49;00m[37m [39;49;00m%}

{%[37m [39;49;00m[94manother_tag[39;49;00m[37m [39;49;00m[33m"my string param"[39;49;00m[37m [39;49;00m%}

{{[37m [39;49;00m[31mvariable[39;49;00m[37m [39;49;00m|[37m [39;49;00m[32mupcase[39;49;00m[37m [39;49;00m}}
{{[37m [39;49;00m[31mvar[39;49;00m.[31mfield[39;49;00m[37m [39;49;00m|[37m [39;49;00m[32mtextilize[39;49;00m[37m [39;49;00m|[37m [39;49;00m[32mmarkdownify[39;49;00m[37m [39;49;00m}}
{{[37m [39;49;00m[31mvar[39;49;00m.[31mfield[39;49;00m.[31mproperty[39;49;00m[37m [39;49;00m|[37m [39;49;00m[32mtextilize[39;49;00m[37m [39;49;00m|[37m [39;49;00m[32mmarkdownify[39;49;00m[37m [39;49;00m}}
{{[37m [39;49;00m[33m'string'[39;49;00m[37m [39;49;00m|[37m [39;49;00m[32mtruncate[39;49;00m:[37m [39;49;00m[34m100[39;49;00m[37m [39;49;00m[36mparam[39;49;00m=[33m'df"g'[39;49;00m[37m [39;49;00m}}

{%[37m [39;49;00m[94mcycle[39;49;00m[37m [39;49;00m[33m'1'[39;49;00m,[37m [39;49;00m[34m2[39;49;00m,[37m [39;49;00m[31mvar[39;49;00m[37m [39;49;00m%}
{%[37m [39;49;00m[94mcycle[39;49;00m[37m [39;49;00m[33m'group1'[39;49;00m:[37m [39;49;00m[33m'1'[39;49;00m,[37m [39;49;00m[31mvar[39;49;00m,[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m%}
{%[37m [39;49;00m[94mcycle[39;49;00m[37m [39;49;00m[31mgroup2[39;49;00m:[37m [39;49;00m[33m'1'[39;49;00m,[37m [39;49;00m[31mvar[39;49;00m,[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m%}

{%[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m[31ma[39;49;00m[37m [39;49;00m==[37m [39;49;00m[33m'B'[39;49;00m[37m [39;49;00m%}
{%[37m [39;49;00m[34melsif[39;49;00m[37m [39;49;00m[31ma[39;49;00m[37m [39;49;00m==[37m [39;49;00m[33m'C%}'[39;49;00m[37m [39;49;00m%}
{%[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00m%}
{%[37m [39;49;00m[34mendif[39;49;00m[37m [39;49;00m%}

{%[37m [39;49;00m[34munless[39;49;00m[37m [39;49;00m[35mnot[39;49;00m[37m [39;49;00m[31ma[39;49;00m[37m [39;49;00m%}
{%[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00m%}
{%[37m [39;49;00m[34mendunless[39;49;00m[37m [39;49;00m%}

{%[37m [39;49;00m[34mcase[39;49;00m[37m [39;49;00m[31ma[39;49;00m[37m [39;49;00m%}
{%[37m [39;49;00m[34mwhen[39;49;00m[37m [39;49;00m[33m'B'[39;49;00m[37m [39;49;00m%}
{%[37m [39;49;00m[34mwhen[39;49;00m[37m [39;49;00m[33m'C'[39;49;00m[37m [39;49;00m%}
{%[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00m%}
{%[37m [39;49;00m[34mendcase[39;49;00m[37m [39;49;00m%}

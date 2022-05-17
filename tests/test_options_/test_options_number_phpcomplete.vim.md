     1	[37m" Vim completion script[39;49;00m
     2	[37m" Language:	PHP[39;49;00m
     3	[37m" Maintainer:	Mikolaj Machowski ( mikmach AT wp DOT pl )[39;49;00m
     4	[37m" Last Change:	2006 May 9[39;49;00m
     5	[37m"[39;49;00m
     6	[37m"   TODO:[39;49;00m
     7	[37m"   - Class aware completion:[39;49;00m
     8	[37m"      a) caching?[39;49;00m
     9	[37m"   - Switching to HTML (XML?) completion (SQL) inside of phpStrings[39;49;00m
    10	[37m"   - allow also for XML completion <- better do html_flavor for HTML[39;49;00m
    11	[37m"     completion[39;49;00m
    12	[37m"   - outside of <?php?> getting parent tag may cause problems. Heh, even in[39;49;00m
    13	[37m"     perfect conditions GetLastOpenTag doesn't cooperate... Inside of[39;49;00m
    14	[37m"     phpStrings this can be even a bonus but outside of <?php?> it is not the[39;49;00m
    15	[37m"     best situation[39;49;00m
    16
    17	[34mfunction[39;49;00m! phpcomplete#CompletePHP(findstart, base)
    18		[34mif[39;49;00m [34ma[39;49;00m:findstart
    19			unlet! [34mb[39;49;00m:php_menu
    20	[37m		" Check if we are inside of PHP markup[39;49;00m
    21			[34mlet[39;49;00m pos = getpos([33m'.'[39;49;00m)
    22			[34mlet[39;49;00m phpbegin = searchpairpos([33m'<?'[39;49;00m, [33m''[39;49;00m, [33m'?>'[39;49;00m, [33m'bWn'[39;49;00m,
    23					\ [33m'synIDattr(synID(line("."), col("."), 0), "name") =~? "string\|comment"'[39;49;00m)
    24			[34mlet[39;49;00m phpend   = searchpairpos([33m'<?'[39;49;00m, [33m''[39;49;00m, [33m'?>'[39;49;00m, [33m'Wn'[39;49;00m,
    25					\ [33m'synIDattr(synID(line("."), col("."), 0), "name") =~? "string\|comment"'[39;49;00m)
    26
    27			[34mif[39;49;00m phpbegin == [[34m0[39;49;00m,[34m0[39;49;00m] && phpend == [[34m0[39;49;00m,[34m0[39;49;00m]
    28	[37m			" We are outside of any PHP markup. Complete HTML[39;49;00m
    29				[34mlet[39;49;00m htmlbegin = htmlcomplete#CompleteTags([34m1[39;49;00m, [33m''[39;49;00m)
    30				[34mlet[39;49;00m cursor_col = pos[[34m2[39;49;00m]
    31				[34mlet[39;49;00m base = getline([33m'.'[39;49;00m)[htmlbegin : cursor_col]
    32				[34mlet[39;49;00m [34mb[39;49;00m:php_menu = htmlcomplete#CompleteTags([34m0[39;49;00m, base)
    33				[34mreturn[39;49;00m htmlbegin
    34			[34melse[39;49;00m
    35	[37m			" locate the start of the word[39;49;00m
    36				[34mlet[39;49;00m line = getline([33m'.'[39;49;00m)
    37				[34mlet[39;49;00m [34mstart[39;49;00m = [34mcol[39;49;00m([33m'.'[39;49;00m) - [34m1[39;49;00m
    38				[34mlet[39;49;00m curline = line([33m'.'[39;49;00m)
    39				[34mlet[39;49;00m compl_begin = [34mcol[39;49;00m([33m'.'[39;49;00m) - [34m2[39;49;00m
    40				[34mwhile[39;49;00m [34mstart[39;49;00m >= [34m0[39;49;00m && line[[34mstart[39;49;00m - [34m1[39;49;00m] =~ [33m'[a-zA-Z_0-9\x7f-\xff$]'[39;49;00m
    41					[34mlet[39;49;00m [34mstart[39;49;00m -= [34m1[39;49;00m
    42				[34mendwhile[39;49;00m
    43				[34mlet[39;49;00m [34mb[39;49;00m:compl_context = getline([33m'.'[39;49;00m)[[34m0[39;49;00m:compl_begin]
    44				[34mreturn[39;49;00m [34mstart[39;49;00m
    45	[37m[39;49;00m
    46	[37m			" We can be also inside of phpString with HTML tags. Deal with[39;49;00m
    47	[37m			" it later (time, not lines).[39;49;00m
    48			[34mendif[39;49;00m
    49
    50		[34mendif[39;49;00m
    51	[37m	" If exists b:php_menu it means completion was already constructed we[39;49;00m
    52	[37m	" don't need to do anything more[39;49;00m
    53		[34mif[39;49;00m exists([33m"b:php_menu"[39;49;00m)
    54			[34mreturn[39;49;00m [34mb[39;49;00m:php_menu
    55		[34mendif[39;49;00m
    56	[37m	" Initialize base return lists[39;49;00m
    57		[34mlet[39;49;00m [34mres[39;49;00m = []
    58		[34mlet[39;49;00m res2 = []
    59	[37m	" a:base is very short - we need context[39;49;00m
    60		[34mif[39;49;00m exists([33m"b:compl_context"[39;49;00m)
    61			[34mlet[39;49;00m context = [34mb[39;49;00m:compl_context
    62			unlet! [34mb[39;49;00m:compl_context
    63		[34mendif[39;49;00m
    64
    65		[34mif[39;49;00m !exists([33m'g:php_builtin_functions'[39;49;00m)
    66			[34mcall[39;49;00m phpcomplete#LoadData()
    67		[34mendif[39;49;00m
    68
    69		[34mlet[39;49;00m scontext = substitute(context, [33m'\$\?[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*$'[39;49;00m, [33m''[39;49;00m, [33m''[39;49;00m)
    70
    71		[34mif[39;49;00m scontext =~ [33m'\(=\s*new\|extends\)\s\+$'[39;49;00m
    72	[37m		" Complete class name[39;49;00m
    73	[37m		" Internal solution for finding classes in current file.[39;49;00m
    74			[34mlet[39;49;00m [34mfile[39;49;00m = getline([34m1[39;49;00m, [33m'$'[39;49;00m)
    75			[34mcall[39;49;00m filter([34mfile[39;49;00m,
    76					\ [33m'v:val =~ "class\\s\\+[a-zA-Z_\\x7f-\\xff][a-zA-Z_0-9\\x7f-\\xff]*\\s*("'[39;49;00m)
    77			[34mlet[39;49;00m fnames = [34mjoin[39;49;00m(map(tagfiles(), [33m'escape(v:val, " \\#%")'[39;49;00m))
    78			[34mlet[39;49;00m jfile = [34mjoin[39;49;00m([34mfile[39;49;00m, [33m' '[39;49;00m)
    79			[34mlet[39;49;00m int_values = split(jfile, [33m'class\s\+'[39;49;00m)
    80			[34mlet[39;49;00m int_classes = {}
    81			[34mfor[39;49;00m [34mi[39;49;00m [34min[39;49;00m int_values
    82				[34mlet[39;49;00m c_name = matchstr([34mi[39;49;00m, [33m'^[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*'[39;49;00m)
    83				[34mif[39;49;00m c_name != [33m''[39;49;00m
    84					[34mlet[39;49;00m int_classes[c_name] = [33m''[39;49;00m
    85				[34mendif[39;49;00m
    86			[34mendfor[39;49;00m
    87	[37m[39;49;00m
    88	[37m		" Prepare list of classes from tags file[39;49;00m
    89			[34mlet[39;49;00m ext_classes = {}
    90			[34mlet[39;49;00m fnames = [34mjoin[39;49;00m(map(tagfiles(), [33m'escape(v:val, " \\#%")'[39;49;00m))
    91			[34mif[39;49;00m fnames != [33m''[39;49;00m
    92				exe [33m'silent! vimgrep /^'[39;49;00m.[34ma[39;49;00m:base.[33m'.*\tc\(\t\|$\)/j '[39;49;00m.fnames
    93				[34mlet[39;49;00m qflist = getqflist()
    94				[34mif[39;49;00m len(qflist) > [34m0[39;49;00m
    95					[34mfor[39;49;00m field [34min[39;49;00m qflist
    96	[37m					" [:space:] thing: we don't have to be so strict when[39;49;00m
    97	[37m					" dealing with tags files - entries there were already[39;49;00m
    98	[37m					" checked by ctags.[39;49;00m
    99						[34mlet[39;49;00m item = matchstr(field[[33m'text'[39;49;00m], [33m'^[^[:space:]]\+'[39;49;00m)
   100						[34mlet[39;49;00m ext_classes[item] = [33m''[39;49;00m
   101					[34mendfor[39;49;00m
   102				[34mendif[39;49;00m
   103			[34mendif[39;49;00m
   104	[37m[39;49;00m
   105	[37m		" Prepare list of built in classes from g:php_builtin_functions[39;49;00m
   106			[34mif[39;49;00m !exists([33m"g:php_omni_bi_classes"[39;49;00m)
   107				[34mlet[39;49;00m [34mg[39;49;00m:php_omni_bi_classes = {}
   108				[34mfor[39;49;00m [34mi[39;49;00m [34min[39;49;00m keys([34mg[39;49;00m:php_builtin_object_functions)
   109					[34mlet[39;49;00m [34mg[39;49;00m:php_omni_bi_classes[substitute([34mi[39;49;00m, [33m'::.*$'[39;49;00m, [33m''[39;49;00m, [33m''[39;49;00m)] = [33m''[39;49;00m
   110				[34mendfor[39;49;00m
   111			[34mendif[39;49;00m
   112
   113			[34mlet[39;49;00m classes = [34msort[39;49;00m(keys(int_classes))
   114			[34mlet[39;49;00m classes += [34msort[39;49;00m(keys(ext_classes))
   115			[34mlet[39;49;00m classes += [34msort[39;49;00m(keys([34mg[39;49;00m:php_omni_bi_classes))
   116
   117			[34mfor[39;49;00m [34mm[39;49;00m [34min[39;49;00m classes
   118				[34mif[39;49;00m [34mm[39;49;00m =~ [33m'^'[39;49;00m.[34ma[39;49;00m:base
   119					[34mcall[39;49;00m add([34mres[39;49;00m, [34mm[39;49;00m)
   120				[34mendif[39;49;00m
   121			[34mendfor[39;49;00m
   122
   123			[34mlet[39;49;00m final_menu = []
   124			[34mfor[39;49;00m [34mi[39;49;00m [34min[39;49;00m [34mres[39;49;00m
   125				[34mlet[39;49;00m final_menu += [{[33m'word'[39;49;00m:[34mi[39;49;00m, [33m'kind'[39;49;00m:[33m'c'[39;49;00m}]
   126			[34mendfor[39;49;00m
   127
   128			[34mreturn[39;49;00m final_menu
   129
   130		[34melseif[39;49;00m scontext =~ [33m'\(->\|::\)$'[39;49;00m
   131	[37m		" Complete user functions and variables[39;49;00m
   132	[37m		" Internal solution for current file.[39;49;00m
   133	[37m		" That seems as unnecessary repeating of functions but there are[39;49;00m
   134	[37m		" few not so subtle differences as not appending of $ and addition[39;49;00m
   135	[37m		" of 'kind' tag (not necessary in regular completion)[39;49;00m
   136
   137			[34mif[39;49;00m scontext =~ [33m'->$'[39;49;00m && scontext !~ [33m'\$this->$'[39;49;00m
   138	[37m[39;49;00m
   139	[37m			" Get name of the class[39;49;00m
   140				[34mlet[39;49;00m classname = phpcomplete#GetClassName(scontext)
   141	[37m[39;49;00m
   142	[37m			" Get location of class definition, we have to iterate through all[39;49;00m
   143	[37m			" tags files separately because we need relative path from current[39;49;00m
   144	[37m			" file to the exact file (tags file can be in different dir)[39;49;00m
   145				[34mif[39;49;00m classname != [33m''[39;49;00m
   146					[34mlet[39;49;00m classlocation = phpcomplete#GetClassLocation(classname)
   147				[34melse[39;49;00m
   148					[34mlet[39;49;00m classlocation = [33m''[39;49;00m
   149				[34mendif[39;49;00m
   150
   151				[34mif[39;49;00m classlocation == [33m'VIMPHP_BUILTINOBJECT'[39;49;00m
   152
   153					[34mfor[39;49;00m object [34min[39;49;00m keys([34mg[39;49;00m:php_builtin_object_functions)
   154						[34mif[39;49;00m object =~ [33m'^'[39;49;00m.classname
   155							[34mlet[39;49;00m [34mres[39;49;00m += [{[33m'word'[39;49;00m:substitute(object, [33m'.*::'[39;49;00m, [33m''[39;49;00m, [33m''[39;49;00m),
   156								   	\    [33m'info'[39;49;00m: [34mg[39;49;00m:php_builtin_object_functions[object]}]
   157						[34mendif[39;49;00m
   158					[34mendfor[39;49;00m
   159
   160					[34mreturn[39;49;00m [34mres[39;49;00m
   161
   162				[34mendif[39;49;00m
   163
   164				[34mif[39;49;00m filereadable(classlocation)
   165					[34mlet[39;49;00m classfile = readfile(classlocation)
   166					[34mlet[39;49;00m classcontent = [33m''[39;49;00m
   167					[34mlet[39;49;00m classcontent .= [33m"\n"[39;49;00m.phpcomplete#GetClassContents(classfile, classname)
   168					[34mlet[39;49;00m sccontent = split(classcontent, [33m"\n"[39;49;00m)
   169	[37m[39;49;00m
   170	[37m				" YES, YES, YES! - we have whole content including extends![39;49;00m
   171	[37m				" Now we need to get two elements: public functions and public[39;49;00m
   172	[37m				" vars[39;49;00m
   173	[37m				" NO, NO, NO! - third separate filtering looking for content[39;49;00m
   174	[37m				" :(, but all of them have differences. To squeeze them into[39;49;00m
   175	[37m				" one implementation would require many additional arguments[39;49;00m
   176	[37m				" and ifs. No good solution[39;49;00m
   177	[37m				" Functions declared with public keyword or without any[39;49;00m
   178	[37m				" keyword are public[39;49;00m
   179					[34mlet[39;49;00m functions = filter(deepcopy(sccontent),
   180							\ [33m'v:val =~ "^\\s*\\(static\\s\\+\\|public\\s\\+\\)*function"'[39;49;00m)
   181					[34mlet[39;49;00m jfuncs = [34mjoin[39;49;00m(functions, [33m' '[39;49;00m)
   182					[34mlet[39;49;00m sfuncs = split(jfuncs, [33m'function\s\+'[39;49;00m)
   183					[34mlet[39;49;00m c_functions = {}
   184					[34mfor[39;49;00m [34mi[39;49;00m [34min[39;49;00m sfuncs
   185						[34mlet[39;49;00m f_name = matchstr([34mi[39;49;00m,
   186								\ [33m'^&\?\zs[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*\ze'[39;49;00m)
   187						[34mlet[39;49;00m f_args = matchstr([34mi[39;49;00m,
   188								\ [33m'^&\?[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*\s*(\zs.\{-}\ze)\_s*{'[39;49;00m)
   189						[34mif[39;49;00m f_name != [33m''[39;49;00m
   190							[34mlet[39;49;00m c_functions[f_name.[33m'('[39;49;00m] = f_args
   191						[34mendif[39;49;00m
   192					[34mendfor[39;49;00m
   193	[37m				" Variables declared with var or with public keyword are[39;49;00m
   194	[37m				" public[39;49;00m
   195					[34mlet[39;49;00m variables = filter(deepcopy(sccontent),
   196							\ [33m'v:val =~ "^\\s*\\(public\\|var\\)\\s\\+\\$"'[39;49;00m)
   197					[34mlet[39;49;00m jvars = [34mjoin[39;49;00m(variables, [33m' '[39;49;00m)
   198					[34mlet[39;49;00m svars = split(jvars, [33m'\$'[39;49;00m)
   199					[34mlet[39;49;00m c_variables = {}
   200					[34mfor[39;49;00m [34mi[39;49;00m [34min[39;49;00m svars
   201						[34mlet[39;49;00m c_var = matchstr([34mi[39;49;00m,
   202								\ [33m'^\zs[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*\ze'[39;49;00m)
   203						[34mif[39;49;00m c_var != [33m''[39;49;00m
   204							[34mlet[39;49;00m c_variables[c_var] = [33m''[39;49;00m
   205						[34mendif[39;49;00m
   206					[34mendfor[39;49;00m
   207
   208					[34mlet[39;49;00m all_values = {}
   209					[34mcall[39;49;00m extend(all_values, c_functions)
   210					[34mcall[39;49;00m extend(all_values, c_variables)
   211
   212					[34mfor[39;49;00m [34mm[39;49;00m [34min[39;49;00m [34msort[39;49;00m(keys(all_values))
   213						[34mif[39;49;00m [34mm[39;49;00m =~ [33m'^'[39;49;00m.[34ma[39;49;00m:base && [34mm[39;49;00m !~ [33m'::'[39;49;00m
   214							[34mcall[39;49;00m add([34mres[39;49;00m, [34mm[39;49;00m)
   215						[34melseif[39;49;00m [34mm[39;49;00m =~ [33m'::'[39;49;00m.[34ma[39;49;00m:base
   216							[34mcall[39;49;00m add(res2, [34mm[39;49;00m)
   217						[34mendif[39;49;00m
   218					[34mendfor[39;49;00m
   219
   220					[34mlet[39;49;00m start_list = [34mres[39;49;00m + res2
   221
   222					[34mlet[39;49;00m final_list = []
   223					[34mfor[39;49;00m [34mi[39;49;00m [34min[39;49;00m start_list
   224						[34mif[39;49;00m has_key(c_variables, [34mi[39;49;00m)
   225							[34mlet[39;49;00m class = [33m' '[39;49;00m
   226							[34mif[39;49;00m all_values[[34mi[39;49;00m] != [33m''[39;49;00m
   227								[34mlet[39;49;00m class = [34mi[39;49;00m.[33m' class '[39;49;00m
   228							[34mendif[39;49;00m
   229							[34mlet[39;49;00m final_list +=
   230									\ [{[33m'word'[39;49;00m:[34mi[39;49;00m,
   231									\   [33m'info'[39;49;00m:class.all_values[[34mi[39;49;00m],
   232									\   [33m'kind'[39;49;00m:[33m'v'[39;49;00m}]
   233						[34melse[39;49;00m
   234							[34mlet[39;49;00m final_list +=
   235									\ [{[33m'word'[39;49;00m:substitute([34mi[39;49;00m, [33m'.*::'[39;49;00m, [33m''[39;49;00m, [33m''[39;49;00m),
   236									\   [33m'info'[39;49;00m:[34mi[39;49;00m.all_values[[34mi[39;49;00m].[33m')'[39;49;00m,
   237									\   [33m'kind'[39;49;00m:[33m'f'[39;49;00m}]
   238						[34mendif[39;49;00m
   239					[34mendfor[39;49;00m
   240
   241					[34mreturn[39;49;00m final_list
   242
   243				[34mendif[39;49;00m
   244
   245			[34mendif[39;49;00m
   246
   247			[34mif[39;49;00m [34ma[39;49;00m:base =~ [33m'^\$'[39;49;00m
   248				[34mlet[39;49;00m adddollar = [33m'$'[39;49;00m
   249			[34melse[39;49;00m
   250				[34mlet[39;49;00m adddollar = [33m''[39;49;00m
   251			[34mendif[39;49;00m
   252			[34mlet[39;49;00m [34mfile[39;49;00m = getline([34m1[39;49;00m, [33m'$'[39;49;00m)
   253			[34mlet[39;49;00m jfile = [34mjoin[39;49;00m([34mfile[39;49;00m, [33m' '[39;49;00m)
   254			[34mlet[39;49;00m sfile = split(jfile, [33m'\$'[39;49;00m)
   255			[34mlet[39;49;00m int_vars = {}
   256			[34mfor[39;49;00m [34mi[39;49;00m [34min[39;49;00m sfile
   257				[34mif[39;49;00m [34mi[39;49;00m =~ [33m'^\$[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*\s*=\s*new'[39;49;00m
   258					[34mlet[39;49;00m val = matchstr([34mi[39;49;00m, [33m'^[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*'[39;49;00m).[33m'->'[39;49;00m
   259				[34melse[39;49;00m
   260					[34mlet[39;49;00m val = matchstr([34mi[39;49;00m, [33m'^[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*'[39;49;00m)
   261				[34mendif[39;49;00m
   262				[34mif[39;49;00m val !~ [33m''[39;49;00m
   263					[34mlet[39;49;00m int_vars[adddollar.val] = [33m''[39;49;00m
   264				[34mendif[39;49;00m
   265			[34mendfor[39;49;00m
   266	[37m[39;49;00m
   267	[37m		" ctags has good support for PHP, use tags file for external[39;49;00m
   268	[37m		" variables[39;49;00m
   269			[34mlet[39;49;00m fnames = [34mjoin[39;49;00m(map(tagfiles(), [33m'escape(v:val, " \\#%")'[39;49;00m))
   270			[34mlet[39;49;00m ext_vars = {}
   271			[34mif[39;49;00m fnames != [33m''[39;49;00m
   272				[34mlet[39;49;00m sbase = substitute([34ma[39;49;00m:base, [33m'^\$'[39;49;00m, [33m''[39;49;00m, [33m''[39;49;00m)
   273				exe [33m'silent! vimgrep /^'[39;49;00m.sbase.[33m'.*\tv\(\t\|$\)/j '[39;49;00m.fnames
   274				[34mlet[39;49;00m qflist = getqflist()
   275				[34mif[39;49;00m len(qflist) > [34m0[39;49;00m
   276					[34mfor[39;49;00m field [34min[39;49;00m qflist
   277						[34mlet[39;49;00m item = matchstr(field[[33m'text'[39;49;00m], [33m'^[^[:space:]]\+'[39;49;00m)
   278	[37m					" Add -> if it is possible object declaration[39;49;00m
   279						[34mlet[39;49;00m classname = [33m''[39;49;00m
   280						[34mif[39;49;00m field[[33m'text'[39;49;00m] =~ item.[33m'\s*=\s*new\s\+'[39;49;00m
   281							[34mlet[39;49;00m item = item.[33m'->'[39;49;00m
   282							[34mlet[39;49;00m classname = matchstr(field[[33m'text'[39;49;00m],
   283									\ [33m'=\s*new\s\+\zs[a-zA-Z_0-9\x7f-\xff]\+\ze'[39;49;00m)
   284						[34mendif[39;49;00m
   285						[34mlet[39;49;00m ext_vars[adddollar.item] = classname
   286					[34mendfor[39;49;00m
   287				[34mendif[39;49;00m
   288			[34mendif[39;49;00m
   289	[37m[39;49;00m
   290	[37m		" Now we have all variables in int_vars dictionary[39;49;00m
   291			[34mcall[39;49;00m extend(int_vars, ext_vars)
   292	[37m[39;49;00m
   293	[37m		" Internal solution for finding functions in current file.[39;49;00m
   294			[34mlet[39;49;00m [34mfile[39;49;00m = getline([34m1[39;49;00m, [33m'$'[39;49;00m)
   295			[34mcall[39;49;00m filter([34mfile[39;49;00m,
   296					\ [33m'v:val =~ "function\\s\\+&\\?[a-zA-Z_\\x7f-\\xff][a-zA-Z_0-9\\x7f-\\xff]*\\s*("'[39;49;00m)
   297			[34mlet[39;49;00m fnames = [34mjoin[39;49;00m(map(tagfiles(), [33m'escape(v:val, " \\#%")'[39;49;00m))
   298			[34mlet[39;49;00m jfile = [34mjoin[39;49;00m([34mfile[39;49;00m, [33m' '[39;49;00m)
   299			[34mlet[39;49;00m int_values = split(jfile, [33m'function\s\+'[39;49;00m)
   300			[34mlet[39;49;00m int_functions = {}
   301			[34mfor[39;49;00m [34mi[39;49;00m [34min[39;49;00m int_values
   302				[34mlet[39;49;00m f_name = matchstr([34mi[39;49;00m,
   303						\ [33m'^&\?\zs[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*\ze'[39;49;00m)
   304				[34mlet[39;49;00m f_args = matchstr([34mi[39;49;00m,
   305						\ [33m'^&\?[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*\s*(\zs.\{-}\ze)\_s*{'[39;49;00m)
   306				[34mlet[39;49;00m int_functions[f_name.[33m'('[39;49;00m] = f_args.[33m')'[39;49;00m
   307			[34mendfor[39;49;00m
   308	[37m[39;49;00m
   309	[37m		" Prepare list of functions from tags file[39;49;00m
   310			[34mlet[39;49;00m ext_functions = {}
   311			[34mif[39;49;00m fnames != [33m''[39;49;00m
   312				exe [33m'silent! vimgrep /^'[39;49;00m.[34ma[39;49;00m:base.[33m'.*\tf\(\t\|$\)/j '[39;49;00m.fnames
   313				[34mlet[39;49;00m qflist = getqflist()
   314				[34mif[39;49;00m len(qflist) > [34m0[39;49;00m
   315					[34mfor[39;49;00m field [34min[39;49;00m qflist
   316	[37m					" File name[39;49;00m
   317						[34mlet[39;49;00m item = matchstr(field[[33m'text'[39;49;00m], [33m'^[^[:space:]]\+'[39;49;00m)
   318						[34mlet[39;49;00m fname = matchstr(field[[33m'text'[39;49;00m], [33m'\t\zs\f\+\ze'[39;49;00m)
   319						[34mlet[39;49;00m prototype = matchstr(field[[33m'text'[39;49;00m],
   320								\ [33m'function\s\+&\?[^[:space:]]\+\s*(\s*\zs.\{-}\ze\s*)\s*{\?'[39;49;00m)
   321						[34mlet[39;49;00m ext_functions[item.[33m'('[39;49;00m] = prototype.[33m') - '[39;49;00m.fname
   322					[34mendfor[39;49;00m
   323				[34mendif[39;49;00m
   324			[34mendif[39;49;00m
   325
   326			[34mlet[39;49;00m all_values = {}
   327			[34mcall[39;49;00m extend(all_values, int_functions)
   328			[34mcall[39;49;00m extend(all_values, ext_functions)
   329			[34mcall[39;49;00m extend(all_values, int_vars) [37m" external variables are already in[39;49;00m
   330			[34mcall[39;49;00m extend(all_values, [34mg[39;49;00m:php_builtin_object_functions)
   331
   332			[34mfor[39;49;00m [34mm[39;49;00m [34min[39;49;00m [34msort[39;49;00m(keys(all_values))
   333				[34mif[39;49;00m [34mm[39;49;00m =~ [33m'\(^\|::\)'[39;49;00m.[34ma[39;49;00m:base
   334					[34mcall[39;49;00m add([34mres[39;49;00m, [34mm[39;49;00m)
   335				[34mendif[39;49;00m
   336			[34mendfor[39;49;00m
   337
   338			[34mlet[39;49;00m start_list = [34mres[39;49;00m
   339
   340			[34mlet[39;49;00m final_list = []
   341			[34mfor[39;49;00m [34mi[39;49;00m [34min[39;49;00m start_list
   342				[34mif[39;49;00m has_key(int_vars, [34mi[39;49;00m)
   343					[34mlet[39;49;00m class = [33m' '[39;49;00m
   344					[34mif[39;49;00m all_values[[34mi[39;49;00m] != [33m''[39;49;00m
   345						[34mlet[39;49;00m class = [34mi[39;49;00m.[33m' class '[39;49;00m
   346					[34mendif[39;49;00m
   347					[34mlet[39;49;00m final_list += [{[33m'word'[39;49;00m:[34mi[39;49;00m, [33m'info'[39;49;00m:class.all_values[[34mi[39;49;00m], [33m'kind'[39;49;00m:[33m'v'[39;49;00m}]
   348				[34melse[39;49;00m
   349					[34mlet[39;49;00m final_list +=
   350							\ [{[33m'word'[39;49;00m:substitute([34mi[39;49;00m, [33m'.*::'[39;49;00m, [33m''[39;49;00m, [33m''[39;49;00m),
   351							\   [33m'info'[39;49;00m:[34mi[39;49;00m.all_values[[34mi[39;49;00m],
   352							\   [33m'kind'[39;49;00m:[33m'f'[39;49;00m}]
   353				[34mendif[39;49;00m
   354			[34mendfor[39;49;00m
   355
   356			[34mreturn[39;49;00m final_list
   357		[34mendif[39;49;00m
   358
   359		[34mif[39;49;00m [34ma[39;49;00m:base =~ [33m'^\$'[39;49;00m
   360	[37m		" Complete variables[39;49;00m
   361	[37m		" Built-in variables {{{[39;49;00m
   362			[34mlet[39;49;00m [34mg[39;49;00m:php_builtin_vars = {[33m'$GLOBALS'[39;49;00m:[33m''[39;49;00m,
   363									\ [33m'$_SERVER'[39;49;00m:[33m''[39;49;00m,
   364									\ [33m'$_GET'[39;49;00m:[33m''[39;49;00m,
   365									\ [33m'$_POST'[39;49;00m:[33m''[39;49;00m,
   366									\ [33m'$_COOKIE'[39;49;00m:[33m''[39;49;00m,
   367									\ [33m'$_FILES'[39;49;00m:[33m''[39;49;00m,
   368									\ [33m'$_ENV'[39;49;00m:[33m''[39;49;00m,
   369									\ [33m'$_REQUEST'[39;49;00m:[33m''[39;49;00m,
   370									\ [33m'$_SESSION'[39;49;00m:[33m''[39;49;00m,
   371									\ [33m'$HTTP_SERVER_VARS'[39;49;00m:[33m''[39;49;00m,
   372									\ [33m'$HTTP_ENV_VARS'[39;49;00m:[33m''[39;49;00m,
   373									\ [33m'$HTTP_COOKIE_VARS'[39;49;00m:[33m''[39;49;00m,
   374									\ [33m'$HTTP_GET_VARS'[39;49;00m:[33m''[39;49;00m,
   375									\ [33m'$HTTP_POST_VARS'[39;49;00m:[33m''[39;49;00m,
   376									\ [33m'$HTTP_POST_FILES'[39;49;00m:[33m''[39;49;00m,
   377									\ [33m'$HTTP_SESSION_VARS'[39;49;00m:[33m''[39;49;00m,
   378									\ [33m'$php_errormsg'[39;49;00m:[33m''[39;49;00m,
   379									\ [33m'$this'[39;49;00m:[33m''[39;49;00m
   380									\ }
   381	[37m		" }}}[39;49;00m
   382	[37m[39;49;00m
   383	[37m		" Internal solution for current file.[39;49;00m
   384			[34mlet[39;49;00m [34mfile[39;49;00m = getline([34m1[39;49;00m, [33m'$'[39;49;00m)
   385			[34mlet[39;49;00m jfile = [34mjoin[39;49;00m([34mfile[39;49;00m, [33m' '[39;49;00m)
   386			[34mlet[39;49;00m int_vals = split(jfile, [33m'\ze\$'[39;49;00m)
   387			[34mlet[39;49;00m int_vars = {}
   388			[34mfor[39;49;00m [34mi[39;49;00m [34min[39;49;00m int_vals
   389				[34mif[39;49;00m [34mi[39;49;00m =~ [33m'^\$[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*\s*=\s*new'[39;49;00m
   390					[34mlet[39;49;00m val = matchstr([34mi[39;49;00m,
   391							\ [33m'^\$[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*'[39;49;00m).[33m'->'[39;49;00m
   392				[34melse[39;49;00m
   393					[34mlet[39;49;00m val = matchstr([34mi[39;49;00m,
   394							\ [33m'^\$[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*'[39;49;00m)
   395				[34mendif[39;49;00m
   396				[34mif[39;49;00m val != [33m''[39;49;00m
   397					[34mlet[39;49;00m int_vars[val] = [33m''[39;49;00m
   398				[34mendif[39;49;00m
   399			[34mendfor[39;49;00m
   400
   401			[34mcall[39;49;00m extend(int_vars,[34mg[39;49;00m:php_builtin_vars)
   402	[37m[39;49;00m
   403	[37m		" ctags has support for PHP, use tags file for external variables[39;49;00m
   404			[34mlet[39;49;00m fnames = [34mjoin[39;49;00m(map(tagfiles(), [33m'escape(v:val, " \\#%")'[39;49;00m))
   405			[34mlet[39;49;00m ext_vars = {}
   406			[34mif[39;49;00m fnames != [33m''[39;49;00m
   407				[34mlet[39;49;00m sbase = substitute([34ma[39;49;00m:base, [33m'^\$'[39;49;00m, [33m''[39;49;00m, [33m''[39;49;00m)
   408				exe [33m'silent! vimgrep /^'[39;49;00m.sbase.[33m'.*\tv\(\t\|$\)/j '[39;49;00m.fnames
   409				[34mlet[39;49;00m qflist = getqflist()
   410				[34mif[39;49;00m len(qflist) > [34m0[39;49;00m
   411					[34mfor[39;49;00m field [34min[39;49;00m qflist
   412						[34mlet[39;49;00m item = [33m'$'[39;49;00m.matchstr(field[[33m'text'[39;49;00m], [33m'^[^[:space:]]\+'[39;49;00m)
   413						[34mlet[39;49;00m m_menu = [33m''[39;49;00m
   414	[37m					" Add -> if it is possible object declaration[39;49;00m
   415						[34mif[39;49;00m field[[33m'text'[39;49;00m] =~ item.[33m'\s*=\s*new\s\+'[39;49;00m
   416							[34mlet[39;49;00m item = item.[33m'->'[39;49;00m
   417							[34mlet[39;49;00m m_menu = matchstr(field[[33m'text'[39;49;00m],
   418									\ [33m'=\s*new\s\+\zs[a-zA-Z_0-9\x7f-\xff]\+\ze'[39;49;00m)
   419						[34mendif[39;49;00m
   420						[34mlet[39;49;00m ext_vars[item] = m_menu
   421					[34mendfor[39;49;00m
   422				[34mendif[39;49;00m
   423			[34mendif[39;49;00m
   424
   425			[34mcall[39;49;00m extend(int_vars, ext_vars)
   426			[34mlet[39;49;00m [34mg[39;49;00m:a0 = keys(int_vars)
   427
   428			[34mfor[39;49;00m [34mm[39;49;00m [34min[39;49;00m [34msort[39;49;00m(keys(int_vars))
   429				[34mif[39;49;00m [34mm[39;49;00m =~ [33m'^\'[39;49;00m.[34ma[39;49;00m:base
   430					[34mcall[39;49;00m add([34mres[39;49;00m, [34mm[39;49;00m)
   431				[34mendif[39;49;00m
   432			[34mendfor[39;49;00m
   433
   434			[34mlet[39;49;00m int_list = [34mres[39;49;00m
   435
   436			[34mlet[39;49;00m int_dict = []
   437			[34mfor[39;49;00m [34mi[39;49;00m [34min[39;49;00m int_list
   438				[34mif[39;49;00m int_vars[[34mi[39;49;00m] != [33m''[39;49;00m
   439					[34mlet[39;49;00m class = [33m' '[39;49;00m
   440					[34mif[39;49;00m int_vars[[34mi[39;49;00m] != [33m''[39;49;00m
   441						[34mlet[39;49;00m class = [34mi[39;49;00m.[33m' class '[39;49;00m
   442					[34mendif[39;49;00m
   443					[34mlet[39;49;00m int_dict += [{[33m'word'[39;49;00m:[34mi[39;49;00m, [33m'info'[39;49;00m:class.int_vars[[34mi[39;49;00m], [33m'kind'[39;49;00m:[33m'v'[39;49;00m}]
   444				[34melse[39;49;00m
   445					[34mlet[39;49;00m int_dict += [{[33m'word'[39;49;00m:[34mi[39;49;00m, [33m'kind'[39;49;00m:[33m'v'[39;49;00m}]
   446				[34mendif[39;49;00m
   447			[34mendfor[39;49;00m
   448
   449			[34mreturn[39;49;00m int_dict
   450
   451		[34melse[39;49;00m
   452	[37m		" Complete everything else -[39;49;00m
   453	[37m		"  + functions,  DONE[39;49;00m
   454	[37m		"  + keywords of language DONE[39;49;00m
   455	[37m		"  + defines (constant definitions), DONE[39;49;00m
   456	[37m		"  + extend keywords for predefined constants, DONE[39;49;00m
   457	[37m		"  + classes (after new), DONE[39;49;00m
   458	[37m		"  + limit choice after -> and :: to funcs and vars DONE[39;49;00m
   459	[37m[39;49;00m
   460	[37m		" Internal solution for finding functions in current file.[39;49;00m
   461			[34mlet[39;49;00m [34mfile[39;49;00m = getline([34m1[39;49;00m, [33m'$'[39;49;00m)
   462			[34mcall[39;49;00m filter([34mfile[39;49;00m,
   463					\ [33m'v:val =~ "function\\s\\+&\\?[a-zA-Z_\\x7f-\\xff][a-zA-Z_0-9\\x7f-\\xff]*\\s*("'[39;49;00m)
   464			[34mlet[39;49;00m fnames = [34mjoin[39;49;00m(map(tagfiles(), [33m'escape(v:val, " \\#%")'[39;49;00m))
   465			[34mlet[39;49;00m jfile = [34mjoin[39;49;00m([34mfile[39;49;00m, [33m' '[39;49;00m)
   466			[34mlet[39;49;00m int_values = split(jfile, [33m'function\s\+'[39;49;00m)
   467			[34mlet[39;49;00m int_functions = {}
   468			[34mfor[39;49;00m [34mi[39;49;00m [34min[39;49;00m int_values
   469				[34mlet[39;49;00m f_name = matchstr([34mi[39;49;00m,
   470						\ [33m'^&\?\zs[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*\ze'[39;49;00m)
   471				[34mlet[39;49;00m f_args = matchstr([34mi[39;49;00m,
   472						\ [33m'^&\?[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*\s*(\s*\zs.\{-}\ze\s*)\_s*{'[39;49;00m)
   473				[34mlet[39;49;00m int_functions[f_name.[33m'('[39;49;00m] = f_args.[33m')'[39;49;00m
   474			[34mendfor[39;49;00m
   475	[37m[39;49;00m
   476	[37m		" Prepare list of functions from tags file[39;49;00m
   477			[34mlet[39;49;00m ext_functions = {}
   478			[34mif[39;49;00m fnames != [33m''[39;49;00m
   479				exe [33m'silent! vimgrep /^'[39;49;00m.[34ma[39;49;00m:base.[33m'.*\tf\(\t\|$\)/j '[39;49;00m.fnames
   480				[34mlet[39;49;00m qflist = getqflist()
   481				[34mif[39;49;00m len(qflist) > [34m0[39;49;00m
   482					[34mfor[39;49;00m field [34min[39;49;00m qflist
   483	[37m					" File name[39;49;00m
   484						[34mlet[39;49;00m item = matchstr(field[[33m'text'[39;49;00m], [33m'^[^[:space:]]\+'[39;49;00m)
   485						[34mlet[39;49;00m fname = matchstr(field[[33m'text'[39;49;00m], [33m'\t\zs\f\+\ze'[39;49;00m)
   486						[34mlet[39;49;00m prototype = matchstr(field[[33m'text'[39;49;00m],
   487								\ [33m'function\s\+&\?[^[:space:]]\+\s*(\s*\zs.\{-}\ze\s*)\s*{\?'[39;49;00m)
   488						[34mlet[39;49;00m ext_functions[item.[33m'('[39;49;00m] = prototype.[33m') - '[39;49;00m.fname
   489					[34mendfor[39;49;00m
   490				[34mendif[39;49;00m
   491			[34mendif[39;49;00m
   492	[37m[39;49;00m
   493	[37m		" All functions[39;49;00m
   494			[34mcall[39;49;00m extend(int_functions, ext_functions)
   495			[34mcall[39;49;00m extend(int_functions, [34mg[39;49;00m:php_builtin_functions)
   496	[37m[39;49;00m
   497	[37m		" Internal solution for finding constants in current file[39;49;00m
   498			[34mlet[39;49;00m [34mfile[39;49;00m = getline([34m1[39;49;00m, [33m'$'[39;49;00m)
   499			[34mcall[39;49;00m filter([34mfile[39;49;00m, [33m'v:val =~ "define\\s*("'[39;49;00m)
   500			[34mlet[39;49;00m jfile = [34mjoin[39;49;00m([34mfile[39;49;00m, [33m' '[39;49;00m)
   501			[34mlet[39;49;00m int_values = split(jfile, [33m'define\s*(\s*'[39;49;00m)
   502			[34mlet[39;49;00m int_constants = {}
   503			[34mfor[39;49;00m [34mi[39;49;00m [34min[39;49;00m int_values
   504				[34mlet[39;49;00m c_name = matchstr([34mi[39;49;00m, [33m'\(["'']\)\zs[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*\ze\1'[39;49;00m)
   505	[37m			" let c_value = matchstr(i,[39;49;00m
   506	[37m			" \ '\(["'']\)[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*\1\s*,\s*\zs.\{-}\ze\s*)')[39;49;00m
   507				[34mif[39;49;00m c_name != [33m''[39;49;00m
   508					[34mlet[39;49;00m int_constants[c_name] = [33m''[39;49;00m [37m" c_value[39;49;00m
   509				[34mendif[39;49;00m
   510			[34mendfor[39;49;00m
   511	[37m[39;49;00m
   512	[37m		" Prepare list of constants from tags file[39;49;00m
   513			[34mlet[39;49;00m fnames = [34mjoin[39;49;00m(map(tagfiles(), [33m'escape(v:val, " \\#%")'[39;49;00m))
   514			[34mlet[39;49;00m ext_constants = {}
   515			[34mif[39;49;00m fnames != [33m''[39;49;00m
   516				exe [33m'silent! vimgrep /^'[39;49;00m.[34ma[39;49;00m:base.[33m'.*\td\(\t\|$\)/j '[39;49;00m.fnames
   517				[34mlet[39;49;00m qflist = getqflist()
   518				[34mif[39;49;00m len(qflist) > [34m0[39;49;00m
   519					[34mfor[39;49;00m field [34min[39;49;00m qflist
   520						[34mlet[39;49;00m item = matchstr(field[[33m'text'[39;49;00m], [33m'^[^[:space:]]\+'[39;49;00m)
   521						[34mlet[39;49;00m ext_constants[item] = [33m''[39;49;00m
   522					[34mendfor[39;49;00m
   523				[34mendif[39;49;00m
   524			[34mendif[39;49;00m
   525	[37m[39;49;00m
   526	[37m		" All constants[39;49;00m
   527			[34mcall[39;49;00m extend(int_constants, ext_constants)
   528	[37m		" Treat keywords as constants[39;49;00m
   529
   530			[34mlet[39;49;00m all_values = {}
   531	[37m[39;49;00m
   532	[37m		" One big dictionary of functions[39;49;00m
   533			[34mcall[39;49;00m extend(all_values, int_functions)
   534	[37m[39;49;00m
   535	[37m		" Add constants[39;49;00m
   536			[34mcall[39;49;00m extend(all_values, int_constants)
   537	[37m		" Add keywords[39;49;00m
   538			[34mcall[39;49;00m extend(all_values, [34mg[39;49;00m:php_keywords)
   539
   540			[34mfor[39;49;00m [34mm[39;49;00m [34min[39;49;00m [34msort[39;49;00m(keys(all_values))
   541				[34mif[39;49;00m [34mm[39;49;00m =~ [33m'^'[39;49;00m.[34ma[39;49;00m:base
   542					[34mcall[39;49;00m add([34mres[39;49;00m, [34mm[39;49;00m)
   543				[34mendif[39;49;00m
   544			[34mendfor[39;49;00m
   545
   546			[34mlet[39;49;00m int_list = [34mres[39;49;00m
   547
   548			[34mlet[39;49;00m final_list = []
   549			[34mfor[39;49;00m [34mi[39;49;00m [34min[39;49;00m int_list
   550				[34mif[39;49;00m has_key(int_functions, [34mi[39;49;00m)
   551					[34mlet[39;49;00m final_list +=
   552							\ [{[33m'word'[39;49;00m:[34mi[39;49;00m,
   553							\   [33m'info'[39;49;00m:[34mi[39;49;00m.int_functions[[34mi[39;49;00m],
   554							\   [33m'kind'[39;49;00m:[33m'f'[39;49;00m}]
   555				[34melseif[39;49;00m has_key(int_constants, [34mi[39;49;00m)
   556					[34mlet[39;49;00m final_list += [{[33m'word'[39;49;00m:[34mi[39;49;00m, [33m'kind'[39;49;00m:[33m'd'[39;49;00m}]
   557				[34melse[39;49;00m
   558					[34mlet[39;49;00m final_list += [{[33m'word'[39;49;00m:[34mi[39;49;00m}]
   559				[34mendif[39;49;00m
   560			[34mendfor[39;49;00m
   561
   562			[34mreturn[39;49;00m final_list
   563
   564		[34mendif[39;49;00m
   565
   566	[34mendfunction[39;49;00m
   567	[37m" vim:set foldmethod=marker:[39;49;00m

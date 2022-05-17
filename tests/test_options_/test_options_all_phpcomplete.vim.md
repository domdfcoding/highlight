     1^I[37m" Vim completion script[39;49;00m$
     2^I[37m" Language:^IPHP[39;49;00m$
     3^I[37m" Maintainer:^IMikolaj Machowski ( mikmach AT wp DOT pl )[39;49;00m$
     4^I[37m" Last Change:^I2006 May 9[39;49;00m$
     5^I[37m"[39;49;00m$
     6^I[37m"   TODO:[39;49;00m$
     7^I[37m"   - Class aware completion:[39;49;00m$
     8^I[37m"      a) caching?[39;49;00m$
     9^I[37m"   - Switching to HTML (XML?) completion (SQL) inside of phpStrings[39;49;00m$
    10^I[37m"   - allow also for XML completion <- better do html_flavor for HTML[39;49;00m$
    11^I[37m"     completion[39;49;00m$
    12^I[37m"   - outside of <?php?> getting parent tag may cause problems. Heh, even in[39;49;00m$
    13^I[37m"     perfect conditions GetLastOpenTag doesn't cooperate... Inside of[39;49;00m$
    14^I[37m"     phpStrings this can be even a bonus but outside of <?php?> it is not the[39;49;00m$
    15^I[37m"     best situation[39;49;00m$
    16^I$
    17^I[34mfunction[39;49;00m! phpcomplete#CompletePHP(findstart, base)$
    18^I^I[34mif[39;49;00m [34ma[39;49;00m:findstart$
    19^I^I^Iunlet! [34mb[39;49;00m:php_menu$
    20^I[37m^I^I" Check if we are inside of PHP markup[39;49;00m$
    21^I^I^I[34mlet[39;49;00m pos = getpos([33m'.'[39;49;00m)$
    22^I^I^I[34mlet[39;49;00m phpbegin = searchpairpos([33m'<?'[39;49;00m, [33m''[39;49;00m, [33m'?>'[39;49;00m, [33m'bWn'[39;49;00m,$
    23^I^I^I^I^I\ [33m'synIDattr(synID(line("."), col("."), 0), "name") =~? "string\|comment"'[39;49;00m)$
    24^I^I^I[34mlet[39;49;00m phpend   = searchpairpos([33m'<?'[39;49;00m, [33m''[39;49;00m, [33m'?>'[39;49;00m, [33m'Wn'[39;49;00m,$
    25^I^I^I^I^I\ [33m'synIDattr(synID(line("."), col("."), 0), "name") =~? "string\|comment"'[39;49;00m)$
    26^I$
    27^I^I^I[34mif[39;49;00m phpbegin == [[34m0[39;49;00m,[34m0[39;49;00m] && phpend == [[34m0[39;49;00m,[34m0[39;49;00m]$
    28^I[37m^I^I^I" We are outside of any PHP markup. Complete HTML[39;49;00m$
    29^I^I^I^I[34mlet[39;49;00m htmlbegin = htmlcomplete#CompleteTags([34m1[39;49;00m, [33m''[39;49;00m)$
    30^I^I^I^I[34mlet[39;49;00m cursor_col = pos[[34m2[39;49;00m]$
    31^I^I^I^I[34mlet[39;49;00m base = getline([33m'.'[39;49;00m)[htmlbegin : cursor_col]$
    32^I^I^I^I[34mlet[39;49;00m [34mb[39;49;00m:php_menu = htmlcomplete#CompleteTags([34m0[39;49;00m, base)$
    33^I^I^I^I[34mreturn[39;49;00m htmlbegin$
    34^I^I^I[34melse[39;49;00m$
    35^I[37m^I^I^I" locate the start of the word[39;49;00m$
    36^I^I^I^I[34mlet[39;49;00m line = getline([33m'.'[39;49;00m)$
    37^I^I^I^I[34mlet[39;49;00m [34mstart[39;49;00m = [34mcol[39;49;00m([33m'.'[39;49;00m) - [34m1[39;49;00m$
    38^I^I^I^I[34mlet[39;49;00m curline = line([33m'.'[39;49;00m)$
    39^I^I^I^I[34mlet[39;49;00m compl_begin = [34mcol[39;49;00m([33m'.'[39;49;00m) - [34m2[39;49;00m$
    40^I^I^I^I[34mwhile[39;49;00m [34mstart[39;49;00m >= [34m0[39;49;00m && line[[34mstart[39;49;00m - [34m1[39;49;00m] =~ [33m'[a-zA-Z_0-9\x7f-\xff$]'[39;49;00m$
    41^I^I^I^I^I[34mlet[39;49;00m [34mstart[39;49;00m -= [34m1[39;49;00m$
    42^I^I^I^I[34mendwhile[39;49;00m$
    43^I^I^I^I[34mlet[39;49;00m [34mb[39;49;00m:compl_context = getline([33m'.'[39;49;00m)[[34m0[39;49;00m:compl_begin]$
    44^I^I^I^I[34mreturn[39;49;00m [34mstart[39;49;00m$
    45^I[37m[39;49;00m$
    46^I[37m^I^I^I" We can be also inside of phpString with HTML tags. Deal with[39;49;00m$
    47^I[37m^I^I^I" it later (time, not lines).[39;49;00m$
    48^I^I^I[34mendif[39;49;00m$
    49^I$
    50^I^I[34mendif[39;49;00m$
    51^I[37m^I" If exists b:php_menu it means completion was already constructed we[39;49;00m$
    52^I[37m^I" don't need to do anything more[39;49;00m$
    53^I^I[34mif[39;49;00m exists([33m"b:php_menu"[39;49;00m)$
    54^I^I^I[34mreturn[39;49;00m [34mb[39;49;00m:php_menu$
    55^I^I[34mendif[39;49;00m$
    56^I[37m^I" Initialize base return lists[39;49;00m$
    57^I^I[34mlet[39;49;00m [34mres[39;49;00m = []$
    58^I^I[34mlet[39;49;00m res2 = []$
    59^I[37m^I" a:base is very short - we need context[39;49;00m$
    60^I^I[34mif[39;49;00m exists([33m"b:compl_context"[39;49;00m)$
    61^I^I^I[34mlet[39;49;00m context = [34mb[39;49;00m:compl_context$
    62^I^I^Iunlet! [34mb[39;49;00m:compl_context$
    63^I^I[34mendif[39;49;00m$
    64^I$
    65^I^I[34mif[39;49;00m !exists([33m'g:php_builtin_functions'[39;49;00m)$
    66^I^I^I[34mcall[39;49;00m phpcomplete#LoadData()$
    67^I^I[34mendif[39;49;00m$
    68^I$
    69^I^I[34mlet[39;49;00m scontext = substitute(context, [33m'\$\?[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*$'[39;49;00m, [33m''[39;49;00m, [33m''[39;49;00m)$
    70^I$
    71^I^I[34mif[39;49;00m scontext =~ [33m'\(=\s*new\|extends\)\s\+$'[39;49;00m$
    72^I[37m^I^I" Complete class name[39;49;00m$
    73^I[37m^I^I" Internal solution for finding classes in current file.[39;49;00m$
    74^I^I^I[34mlet[39;49;00m [34mfile[39;49;00m = getline([34m1[39;49;00m, [33m'$'[39;49;00m)$
    75^I^I^I[34mcall[39;49;00m filter([34mfile[39;49;00m,$
    76^I^I^I^I^I\ [33m'v:val =~ "class\\s\\+[a-zA-Z_\\x7f-\\xff][a-zA-Z_0-9\\x7f-\\xff]*\\s*("'[39;49;00m)$
    77^I^I^I[34mlet[39;49;00m fnames = [34mjoin[39;49;00m(map(tagfiles(), [33m'escape(v:val, " \\#%")'[39;49;00m))$
    78^I^I^I[34mlet[39;49;00m jfile = [34mjoin[39;49;00m([34mfile[39;49;00m, [33m' '[39;49;00m)$
    79^I^I^I[34mlet[39;49;00m int_values = split(jfile, [33m'class\s\+'[39;49;00m)$
    80^I^I^I[34mlet[39;49;00m int_classes = {}$
    81^I^I^I[34mfor[39;49;00m [34mi[39;49;00m [34min[39;49;00m int_values$
    82^I^I^I^I[34mlet[39;49;00m c_name = matchstr([34mi[39;49;00m, [33m'^[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*'[39;49;00m)$
    83^I^I^I^I[34mif[39;49;00m c_name != [33m''[39;49;00m$
    84^I^I^I^I^I[34mlet[39;49;00m int_classes[c_name] = [33m''[39;49;00m$
    85^I^I^I^I[34mendif[39;49;00m$
    86^I^I^I[34mendfor[39;49;00m$
    87^I[37m[39;49;00m$
    88^I[37m^I^I" Prepare list of classes from tags file[39;49;00m$
    89^I^I^I[34mlet[39;49;00m ext_classes = {}$
    90^I^I^I[34mlet[39;49;00m fnames = [34mjoin[39;49;00m(map(tagfiles(), [33m'escape(v:val, " \\#%")'[39;49;00m))$
    91^I^I^I[34mif[39;49;00m fnames != [33m''[39;49;00m$
    92^I^I^I^Iexe [33m'silent! vimgrep /^'[39;49;00m.[34ma[39;49;00m:base.[33m'.*\tc\(\t\|$\)/j '[39;49;00m.fnames$
    93^I^I^I^I[34mlet[39;49;00m qflist = getqflist()$
    94^I^I^I^I[34mif[39;49;00m len(qflist) > [34m0[39;49;00m$
    95^I^I^I^I^I[34mfor[39;49;00m field [34min[39;49;00m qflist$
    96^I[37m^I^I^I^I^I" [:space:] thing: we don't have to be so strict when[39;49;00m$
    97^I[37m^I^I^I^I^I" dealing with tags files - entries there were already[39;49;00m$
    98^I[37m^I^I^I^I^I" checked by ctags.[39;49;00m$
    99^I^I^I^I^I^I[34mlet[39;49;00m item = matchstr(field[[33m'text'[39;49;00m], [33m'^[^[:space:]]\+'[39;49;00m)$
   100^I^I^I^I^I^I[34mlet[39;49;00m ext_classes[item] = [33m''[39;49;00m$
   101^I^I^I^I^I[34mendfor[39;49;00m$
   102^I^I^I^I[34mendif[39;49;00m$
   103^I^I^I[34mendif[39;49;00m$
   104^I[37m[39;49;00m$
   105^I[37m^I^I" Prepare list of built in classes from g:php_builtin_functions[39;49;00m$
   106^I^I^I[34mif[39;49;00m !exists([33m"g:php_omni_bi_classes"[39;49;00m)$
   107^I^I^I^I[34mlet[39;49;00m [34mg[39;49;00m:php_omni_bi_classes = {}$
   108^I^I^I^I[34mfor[39;49;00m [34mi[39;49;00m [34min[39;49;00m keys([34mg[39;49;00m:php_builtin_object_functions)$
   109^I^I^I^I^I[34mlet[39;49;00m [34mg[39;49;00m:php_omni_bi_classes[substitute([34mi[39;49;00m, [33m'::.*$'[39;49;00m, [33m''[39;49;00m, [33m''[39;49;00m)] = [33m''[39;49;00m$
   110^I^I^I^I[34mendfor[39;49;00m$
   111^I^I^I[34mendif[39;49;00m$
   112^I$
   113^I^I^I[34mlet[39;49;00m classes = [34msort[39;49;00m(keys(int_classes))$
   114^I^I^I[34mlet[39;49;00m classes += [34msort[39;49;00m(keys(ext_classes))$
   115^I^I^I[34mlet[39;49;00m classes += [34msort[39;49;00m(keys([34mg[39;49;00m:php_omni_bi_classes))$
   116^I$
   117^I^I^I[34mfor[39;49;00m [34mm[39;49;00m [34min[39;49;00m classes$
   118^I^I^I^I[34mif[39;49;00m [34mm[39;49;00m =~ [33m'^'[39;49;00m.[34ma[39;49;00m:base$
   119^I^I^I^I^I[34mcall[39;49;00m add([34mres[39;49;00m, [34mm[39;49;00m)$
   120^I^I^I^I[34mendif[39;49;00m$
   121^I^I^I[34mendfor[39;49;00m$
   122^I$
   123^I^I^I[34mlet[39;49;00m final_menu = []$
   124^I^I^I[34mfor[39;49;00m [34mi[39;49;00m [34min[39;49;00m [34mres[39;49;00m$
   125^I^I^I^I[34mlet[39;49;00m final_menu += [{[33m'word'[39;49;00m:[34mi[39;49;00m, [33m'kind'[39;49;00m:[33m'c'[39;49;00m}]$
   126^I^I^I[34mendfor[39;49;00m$
   127^I$
   128^I^I^I[34mreturn[39;49;00m final_menu$
   129^I$
   130^I^I[34melseif[39;49;00m scontext =~ [33m'\(->\|::\)$'[39;49;00m$
   131^I[37m^I^I" Complete user functions and variables[39;49;00m$
   132^I[37m^I^I" Internal solution for current file.[39;49;00m$
   133^I[37m^I^I" That seems as unnecessary repeating of functions but there are[39;49;00m$
   134^I[37m^I^I" few not so subtle differences as not appending of $ and addition[39;49;00m$
   135^I[37m^I^I" of 'kind' tag (not necessary in regular completion)[39;49;00m$
   136^I$
   137^I^I^I[34mif[39;49;00m scontext =~ [33m'->$'[39;49;00m && scontext !~ [33m'\$this->$'[39;49;00m$
   138^I[37m[39;49;00m$
   139^I[37m^I^I^I" Get name of the class[39;49;00m$
   140^I^I^I^I[34mlet[39;49;00m classname = phpcomplete#GetClassName(scontext)$
   141^I[37m[39;49;00m$
   142^I[37m^I^I^I" Get location of class definition, we have to iterate through all[39;49;00m$
   143^I[37m^I^I^I" tags files separately because we need relative path from current[39;49;00m$
   144^I[37m^I^I^I" file to the exact file (tags file can be in different dir)[39;49;00m$
   145^I^I^I^I[34mif[39;49;00m classname != [33m''[39;49;00m$
   146^I^I^I^I^I[34mlet[39;49;00m classlocation = phpcomplete#GetClassLocation(classname)$
   147^I^I^I^I[34melse[39;49;00m$
   148^I^I^I^I^I[34mlet[39;49;00m classlocation = [33m''[39;49;00m$
   149^I^I^I^I[34mendif[39;49;00m$
   150^I$
   151^I^I^I^I[34mif[39;49;00m classlocation == [33m'VIMPHP_BUILTINOBJECT'[39;49;00m$
   152^I$
   153^I^I^I^I^I[34mfor[39;49;00m object [34min[39;49;00m keys([34mg[39;49;00m:php_builtin_object_functions)$
   154^I^I^I^I^I^I[34mif[39;49;00m object =~ [33m'^'[39;49;00m.classname$
   155^I^I^I^I^I^I^I[34mlet[39;49;00m [34mres[39;49;00m += [{[33m'word'[39;49;00m:substitute(object, [33m'.*::'[39;49;00m, [33m''[39;49;00m, [33m''[39;49;00m),$
   156^I^I^I^I^I^I^I^I   ^I\    [33m'info'[39;49;00m: [34mg[39;49;00m:php_builtin_object_functions[object]}]$
   157^I^I^I^I^I^I[34mendif[39;49;00m$
   158^I^I^I^I^I[34mendfor[39;49;00m$
   159^I$
   160^I^I^I^I^I[34mreturn[39;49;00m [34mres[39;49;00m$
   161^I$
   162^I^I^I^I[34mendif[39;49;00m$
   163^I$
   164^I^I^I^I[34mif[39;49;00m filereadable(classlocation)$
   165^I^I^I^I^I[34mlet[39;49;00m classfile = readfile(classlocation)$
   166^I^I^I^I^I[34mlet[39;49;00m classcontent = [33m''[39;49;00m$
   167^I^I^I^I^I[34mlet[39;49;00m classcontent .= [33m"\n"[39;49;00m.phpcomplete#GetClassContents(classfile, classname)$
   168^I^I^I^I^I[34mlet[39;49;00m sccontent = split(classcontent, [33m"\n"[39;49;00m)$
   169^I[37m[39;49;00m$
   170^I[37m^I^I^I^I" YES, YES, YES! - we have whole content including extends![39;49;00m$
   171^I[37m^I^I^I^I" Now we need to get two elements: public functions and public[39;49;00m$
   172^I[37m^I^I^I^I" vars[39;49;00m$
   173^I[37m^I^I^I^I" NO, NO, NO! - third separate filtering looking for content[39;49;00m$
   174^I[37m^I^I^I^I" :(, but all of them have differences. To squeeze them into[39;49;00m$
   175^I[37m^I^I^I^I" one implementation would require many additional arguments[39;49;00m$
   176^I[37m^I^I^I^I" and ifs. No good solution[39;49;00m$
   177^I[37m^I^I^I^I" Functions declared with public keyword or without any[39;49;00m$
   178^I[37m^I^I^I^I" keyword are public[39;49;00m$
   179^I^I^I^I^I[34mlet[39;49;00m functions = filter(deepcopy(sccontent),$
   180^I^I^I^I^I^I^I\ [33m'v:val =~ "^\\s*\\(static\\s\\+\\|public\\s\\+\\)*function"'[39;49;00m)$
   181^I^I^I^I^I[34mlet[39;49;00m jfuncs = [34mjoin[39;49;00m(functions, [33m' '[39;49;00m)$
   182^I^I^I^I^I[34mlet[39;49;00m sfuncs = split(jfuncs, [33m'function\s\+'[39;49;00m)$
   183^I^I^I^I^I[34mlet[39;49;00m c_functions = {}$
   184^I^I^I^I^I[34mfor[39;49;00m [34mi[39;49;00m [34min[39;49;00m sfuncs$
   185^I^I^I^I^I^I[34mlet[39;49;00m f_name = matchstr([34mi[39;49;00m,$
   186^I^I^I^I^I^I^I^I\ [33m'^&\?\zs[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*\ze'[39;49;00m)$
   187^I^I^I^I^I^I[34mlet[39;49;00m f_args = matchstr([34mi[39;49;00m,$
   188^I^I^I^I^I^I^I^I\ [33m'^&\?[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*\s*(\zs.\{-}\ze)\_s*{'[39;49;00m)$
   189^I^I^I^I^I^I[34mif[39;49;00m f_name != [33m''[39;49;00m$
   190^I^I^I^I^I^I^I[34mlet[39;49;00m c_functions[f_name.[33m'('[39;49;00m] = f_args$
   191^I^I^I^I^I^I[34mendif[39;49;00m$
   192^I^I^I^I^I[34mendfor[39;49;00m$
   193^I[37m^I^I^I^I" Variables declared with var or with public keyword are[39;49;00m$
   194^I[37m^I^I^I^I" public[39;49;00m$
   195^I^I^I^I^I[34mlet[39;49;00m variables = filter(deepcopy(sccontent),$
   196^I^I^I^I^I^I^I\ [33m'v:val =~ "^\\s*\\(public\\|var\\)\\s\\+\\$"'[39;49;00m)$
   197^I^I^I^I^I[34mlet[39;49;00m jvars = [34mjoin[39;49;00m(variables, [33m' '[39;49;00m)$
   198^I^I^I^I^I[34mlet[39;49;00m svars = split(jvars, [33m'\$'[39;49;00m)$
   199^I^I^I^I^I[34mlet[39;49;00m c_variables = {}$
   200^I^I^I^I^I[34mfor[39;49;00m [34mi[39;49;00m [34min[39;49;00m svars$
   201^I^I^I^I^I^I[34mlet[39;49;00m c_var = matchstr([34mi[39;49;00m,$
   202^I^I^I^I^I^I^I^I\ [33m'^\zs[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*\ze'[39;49;00m)$
   203^I^I^I^I^I^I[34mif[39;49;00m c_var != [33m''[39;49;00m$
   204^I^I^I^I^I^I^I[34mlet[39;49;00m c_variables[c_var] = [33m''[39;49;00m$
   205^I^I^I^I^I^I[34mendif[39;49;00m$
   206^I^I^I^I^I[34mendfor[39;49;00m$
   207^I$
   208^I^I^I^I^I[34mlet[39;49;00m all_values = {}$
   209^I^I^I^I^I[34mcall[39;49;00m extend(all_values, c_functions)$
   210^I^I^I^I^I[34mcall[39;49;00m extend(all_values, c_variables)$
   211^I$
   212^I^I^I^I^I[34mfor[39;49;00m [34mm[39;49;00m [34min[39;49;00m [34msort[39;49;00m(keys(all_values))$
   213^I^I^I^I^I^I[34mif[39;49;00m [34mm[39;49;00m =~ [33m'^'[39;49;00m.[34ma[39;49;00m:base && [34mm[39;49;00m !~ [33m'::'[39;49;00m$
   214^I^I^I^I^I^I^I[34mcall[39;49;00m add([34mres[39;49;00m, [34mm[39;49;00m)$
   215^I^I^I^I^I^I[34melseif[39;49;00m [34mm[39;49;00m =~ [33m'::'[39;49;00m.[34ma[39;49;00m:base$
   216^I^I^I^I^I^I^I[34mcall[39;49;00m add(res2, [34mm[39;49;00m)$
   217^I^I^I^I^I^I[34mendif[39;49;00m$
   218^I^I^I^I^I[34mendfor[39;49;00m$
   219^I$
   220^I^I^I^I^I[34mlet[39;49;00m start_list = [34mres[39;49;00m + res2$
   221^I$
   222^I^I^I^I^I[34mlet[39;49;00m final_list = []$
   223^I^I^I^I^I[34mfor[39;49;00m [34mi[39;49;00m [34min[39;49;00m start_list$
   224^I^I^I^I^I^I[34mif[39;49;00m has_key(c_variables, [34mi[39;49;00m)$
   225^I^I^I^I^I^I^I[34mlet[39;49;00m class = [33m' '[39;49;00m$
   226^I^I^I^I^I^I^I[34mif[39;49;00m all_values[[34mi[39;49;00m] != [33m''[39;49;00m$
   227^I^I^I^I^I^I^I^I[34mlet[39;49;00m class = [34mi[39;49;00m.[33m' class '[39;49;00m$
   228^I^I^I^I^I^I^I[34mendif[39;49;00m$
   229^I^I^I^I^I^I^I[34mlet[39;49;00m final_list +=$
   230^I^I^I^I^I^I^I^I^I\ [{[33m'word'[39;49;00m:[34mi[39;49;00m,$
   231^I^I^I^I^I^I^I^I^I\   [33m'info'[39;49;00m:class.all_values[[34mi[39;49;00m],$
   232^I^I^I^I^I^I^I^I^I\   [33m'kind'[39;49;00m:[33m'v'[39;49;00m}]$
   233^I^I^I^I^I^I[34melse[39;49;00m$
   234^I^I^I^I^I^I^I[34mlet[39;49;00m final_list +=$
   235^I^I^I^I^I^I^I^I^I\ [{[33m'word'[39;49;00m:substitute([34mi[39;49;00m, [33m'.*::'[39;49;00m, [33m''[39;49;00m, [33m''[39;49;00m),$
   236^I^I^I^I^I^I^I^I^I\   [33m'info'[39;49;00m:[34mi[39;49;00m.all_values[[34mi[39;49;00m].[33m')'[39;49;00m,$
   237^I^I^I^I^I^I^I^I^I\   [33m'kind'[39;49;00m:[33m'f'[39;49;00m}]$
   238^I^I^I^I^I^I[34mendif[39;49;00m$
   239^I^I^I^I^I[34mendfor[39;49;00m$
   240^I$
   241^I^I^I^I^I[34mreturn[39;49;00m final_list$
   242^I$
   243^I^I^I^I[34mendif[39;49;00m$
   244^I$
   245^I^I^I[34mendif[39;49;00m$
   246^I$
   247^I^I^I[34mif[39;49;00m [34ma[39;49;00m:base =~ [33m'^\$'[39;49;00m$
   248^I^I^I^I[34mlet[39;49;00m adddollar = [33m'$'[39;49;00m$
   249^I^I^I[34melse[39;49;00m$
   250^I^I^I^I[34mlet[39;49;00m adddollar = [33m''[39;49;00m$
   251^I^I^I[34mendif[39;49;00m$
   252^I^I^I[34mlet[39;49;00m [34mfile[39;49;00m = getline([34m1[39;49;00m, [33m'$'[39;49;00m)$
   253^I^I^I[34mlet[39;49;00m jfile = [34mjoin[39;49;00m([34mfile[39;49;00m, [33m' '[39;49;00m)$
   254^I^I^I[34mlet[39;49;00m sfile = split(jfile, [33m'\$'[39;49;00m)$
   255^I^I^I[34mlet[39;49;00m int_vars = {}$
   256^I^I^I[34mfor[39;49;00m [34mi[39;49;00m [34min[39;49;00m sfile$
   257^I^I^I^I[34mif[39;49;00m [34mi[39;49;00m =~ [33m'^\$[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*\s*=\s*new'[39;49;00m$
   258^I^I^I^I^I[34mlet[39;49;00m val = matchstr([34mi[39;49;00m, [33m'^[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*'[39;49;00m).[33m'->'[39;49;00m$
   259^I^I^I^I[34melse[39;49;00m$
   260^I^I^I^I^I[34mlet[39;49;00m val = matchstr([34mi[39;49;00m, [33m'^[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*'[39;49;00m)$
   261^I^I^I^I[34mendif[39;49;00m$
   262^I^I^I^I[34mif[39;49;00m val !~ [33m''[39;49;00m$
   263^I^I^I^I^I[34mlet[39;49;00m int_vars[adddollar.val] = [33m''[39;49;00m$
   264^I^I^I^I[34mendif[39;49;00m$
   265^I^I^I[34mendfor[39;49;00m$
   266^I[37m[39;49;00m$
   267^I[37m^I^I" ctags has good support for PHP, use tags file for external[39;49;00m$
   268^I[37m^I^I" variables[39;49;00m$
   269^I^I^I[34mlet[39;49;00m fnames = [34mjoin[39;49;00m(map(tagfiles(), [33m'escape(v:val, " \\#%")'[39;49;00m))$
   270^I^I^I[34mlet[39;49;00m ext_vars = {}$
   271^I^I^I[34mif[39;49;00m fnames != [33m''[39;49;00m$
   272^I^I^I^I[34mlet[39;49;00m sbase = substitute([34ma[39;49;00m:base, [33m'^\$'[39;49;00m, [33m''[39;49;00m, [33m''[39;49;00m)$
   273^I^I^I^Iexe [33m'silent! vimgrep /^'[39;49;00m.sbase.[33m'.*\tv\(\t\|$\)/j '[39;49;00m.fnames$
   274^I^I^I^I[34mlet[39;49;00m qflist = getqflist()$
   275^I^I^I^I[34mif[39;49;00m len(qflist) > [34m0[39;49;00m$
   276^I^I^I^I^I[34mfor[39;49;00m field [34min[39;49;00m qflist$
   277^I^I^I^I^I^I[34mlet[39;49;00m item = matchstr(field[[33m'text'[39;49;00m], [33m'^[^[:space:]]\+'[39;49;00m)$
   278^I[37m^I^I^I^I^I" Add -> if it is possible object declaration[39;49;00m$
   279^I^I^I^I^I^I[34mlet[39;49;00m classname = [33m''[39;49;00m$
   280^I^I^I^I^I^I[34mif[39;49;00m field[[33m'text'[39;49;00m] =~ item.[33m'\s*=\s*new\s\+'[39;49;00m$
   281^I^I^I^I^I^I^I[34mlet[39;49;00m item = item.[33m'->'[39;49;00m$
   282^I^I^I^I^I^I^I[34mlet[39;49;00m classname = matchstr(field[[33m'text'[39;49;00m],$
   283^I^I^I^I^I^I^I^I^I\ [33m'=\s*new\s\+\zs[a-zA-Z_0-9\x7f-\xff]\+\ze'[39;49;00m)$
   284^I^I^I^I^I^I[34mendif[39;49;00m$
   285^I^I^I^I^I^I[34mlet[39;49;00m ext_vars[adddollar.item] = classname$
   286^I^I^I^I^I[34mendfor[39;49;00m$
   287^I^I^I^I[34mendif[39;49;00m$
   288^I^I^I[34mendif[39;49;00m$
   289^I[37m[39;49;00m$
   290^I[37m^I^I" Now we have all variables in int_vars dictionary[39;49;00m$
   291^I^I^I[34mcall[39;49;00m extend(int_vars, ext_vars)$
   292^I[37m[39;49;00m$
   293^I[37m^I^I" Internal solution for finding functions in current file.[39;49;00m$
   294^I^I^I[34mlet[39;49;00m [34mfile[39;49;00m = getline([34m1[39;49;00m, [33m'$'[39;49;00m)$
   295^I^I^I[34mcall[39;49;00m filter([34mfile[39;49;00m,$
   296^I^I^I^I^I\ [33m'v:val =~ "function\\s\\+&\\?[a-zA-Z_\\x7f-\\xff][a-zA-Z_0-9\\x7f-\\xff]*\\s*("'[39;49;00m)$
   297^I^I^I[34mlet[39;49;00m fnames = [34mjoin[39;49;00m(map(tagfiles(), [33m'escape(v:val, " \\#%")'[39;49;00m))$
   298^I^I^I[34mlet[39;49;00m jfile = [34mjoin[39;49;00m([34mfile[39;49;00m, [33m' '[39;49;00m)$
   299^I^I^I[34mlet[39;49;00m int_values = split(jfile, [33m'function\s\+'[39;49;00m)$
   300^I^I^I[34mlet[39;49;00m int_functions = {}$
   301^I^I^I[34mfor[39;49;00m [34mi[39;49;00m [34min[39;49;00m int_values$
   302^I^I^I^I[34mlet[39;49;00m f_name = matchstr([34mi[39;49;00m,$
   303^I^I^I^I^I^I\ [33m'^&\?\zs[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*\ze'[39;49;00m)$
   304^I^I^I^I[34mlet[39;49;00m f_args = matchstr([34mi[39;49;00m,$
   305^I^I^I^I^I^I\ [33m'^&\?[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*\s*(\zs.\{-}\ze)\_s*{'[39;49;00m)$
   306^I^I^I^I[34mlet[39;49;00m int_functions[f_name.[33m'('[39;49;00m] = f_args.[33m')'[39;49;00m$
   307^I^I^I[34mendfor[39;49;00m$
   308^I[37m[39;49;00m$
   309^I[37m^I^I" Prepare list of functions from tags file[39;49;00m$
   310^I^I^I[34mlet[39;49;00m ext_functions = {}$
   311^I^I^I[34mif[39;49;00m fnames != [33m''[39;49;00m$
   312^I^I^I^Iexe [33m'silent! vimgrep /^'[39;49;00m.[34ma[39;49;00m:base.[33m'.*\tf\(\t\|$\)/j '[39;49;00m.fnames$
   313^I^I^I^I[34mlet[39;49;00m qflist = getqflist()$
   314^I^I^I^I[34mif[39;49;00m len(qflist) > [34m0[39;49;00m$
   315^I^I^I^I^I[34mfor[39;49;00m field [34min[39;49;00m qflist$
   316^I[37m^I^I^I^I^I" File name[39;49;00m$
   317^I^I^I^I^I^I[34mlet[39;49;00m item = matchstr(field[[33m'text'[39;49;00m], [33m'^[^[:space:]]\+'[39;49;00m)$
   318^I^I^I^I^I^I[34mlet[39;49;00m fname = matchstr(field[[33m'text'[39;49;00m], [33m'\t\zs\f\+\ze'[39;49;00m)$
   319^I^I^I^I^I^I[34mlet[39;49;00m prototype = matchstr(field[[33m'text'[39;49;00m],$
   320^I^I^I^I^I^I^I^I\ [33m'function\s\+&\?[^[:space:]]\+\s*(\s*\zs.\{-}\ze\s*)\s*{\?'[39;49;00m)$
   321^I^I^I^I^I^I[34mlet[39;49;00m ext_functions[item.[33m'('[39;49;00m] = prototype.[33m') - '[39;49;00m.fname$
   322^I^I^I^I^I[34mendfor[39;49;00m$
   323^I^I^I^I[34mendif[39;49;00m$
   324^I^I^I[34mendif[39;49;00m$
   325^I$
   326^I^I^I[34mlet[39;49;00m all_values = {}$
   327^I^I^I[34mcall[39;49;00m extend(all_values, int_functions)$
   328^I^I^I[34mcall[39;49;00m extend(all_values, ext_functions)$
   329^I^I^I[34mcall[39;49;00m extend(all_values, int_vars) [37m" external variables are already in[39;49;00m$
   330^I^I^I[34mcall[39;49;00m extend(all_values, [34mg[39;49;00m:php_builtin_object_functions)$
   331^I$
   332^I^I^I[34mfor[39;49;00m [34mm[39;49;00m [34min[39;49;00m [34msort[39;49;00m(keys(all_values))$
   333^I^I^I^I[34mif[39;49;00m [34mm[39;49;00m =~ [33m'\(^\|::\)'[39;49;00m.[34ma[39;49;00m:base$
   334^I^I^I^I^I[34mcall[39;49;00m add([34mres[39;49;00m, [34mm[39;49;00m)$
   335^I^I^I^I[34mendif[39;49;00m$
   336^I^I^I[34mendfor[39;49;00m$
   337^I$
   338^I^I^I[34mlet[39;49;00m start_list = [34mres[39;49;00m$
   339^I$
   340^I^I^I[34mlet[39;49;00m final_list = []$
   341^I^I^I[34mfor[39;49;00m [34mi[39;49;00m [34min[39;49;00m start_list$
   342^I^I^I^I[34mif[39;49;00m has_key(int_vars, [34mi[39;49;00m)$
   343^I^I^I^I^I[34mlet[39;49;00m class = [33m' '[39;49;00m$
   344^I^I^I^I^I[34mif[39;49;00m all_values[[34mi[39;49;00m] != [33m''[39;49;00m$
   345^I^I^I^I^I^I[34mlet[39;49;00m class = [34mi[39;49;00m.[33m' class '[39;49;00m$
   346^I^I^I^I^I[34mendif[39;49;00m$
   347^I^I^I^I^I[34mlet[39;49;00m final_list += [{[33m'word'[39;49;00m:[34mi[39;49;00m, [33m'info'[39;49;00m:class.all_values[[34mi[39;49;00m], [33m'kind'[39;49;00m:[33m'v'[39;49;00m}]$
   348^I^I^I^I[34melse[39;49;00m$
   349^I^I^I^I^I[34mlet[39;49;00m final_list +=$
   350^I^I^I^I^I^I^I\ [{[33m'word'[39;49;00m:substitute([34mi[39;49;00m, [33m'.*::'[39;49;00m, [33m''[39;49;00m, [33m''[39;49;00m),$
   351^I^I^I^I^I^I^I\   [33m'info'[39;49;00m:[34mi[39;49;00m.all_values[[34mi[39;49;00m],$
   352^I^I^I^I^I^I^I\   [33m'kind'[39;49;00m:[33m'f'[39;49;00m}]$
   353^I^I^I^I[34mendif[39;49;00m$
   354^I^I^I[34mendfor[39;49;00m$
   355^I$
   356^I^I^I[34mreturn[39;49;00m final_list$
   357^I^I[34mendif[39;49;00m$
   358^I$
   359^I^I[34mif[39;49;00m [34ma[39;49;00m:base =~ [33m'^\$'[39;49;00m$
   360^I[37m^I^I" Complete variables[39;49;00m$
   361^I[37m^I^I" Built-in variables {{{[39;49;00m$
   362^I^I^I[34mlet[39;49;00m [34mg[39;49;00m:php_builtin_vars = {[33m'$GLOBALS'[39;49;00m:[33m''[39;49;00m,$
   363^I^I^I^I^I^I^I^I^I\ [33m'$_SERVER'[39;49;00m:[33m''[39;49;00m,$
   364^I^I^I^I^I^I^I^I^I\ [33m'$_GET'[39;49;00m:[33m''[39;49;00m,$
   365^I^I^I^I^I^I^I^I^I\ [33m'$_POST'[39;49;00m:[33m''[39;49;00m,$
   366^I^I^I^I^I^I^I^I^I\ [33m'$_COOKIE'[39;49;00m:[33m''[39;49;00m,$
   367^I^I^I^I^I^I^I^I^I\ [33m'$_FILES'[39;49;00m:[33m''[39;49;00m,$
   368^I^I^I^I^I^I^I^I^I\ [33m'$_ENV'[39;49;00m:[33m''[39;49;00m,$
   369^I^I^I^I^I^I^I^I^I\ [33m'$_REQUEST'[39;49;00m:[33m''[39;49;00m,$
   370^I^I^I^I^I^I^I^I^I\ [33m'$_SESSION'[39;49;00m:[33m''[39;49;00m,$
   371^I^I^I^I^I^I^I^I^I\ [33m'$HTTP_SERVER_VARS'[39;49;00m:[33m''[39;49;00m,$
   372^I^I^I^I^I^I^I^I^I\ [33m'$HTTP_ENV_VARS'[39;49;00m:[33m''[39;49;00m,$
   373^I^I^I^I^I^I^I^I^I\ [33m'$HTTP_COOKIE_VARS'[39;49;00m:[33m''[39;49;00m,$
   374^I^I^I^I^I^I^I^I^I\ [33m'$HTTP_GET_VARS'[39;49;00m:[33m''[39;49;00m,$
   375^I^I^I^I^I^I^I^I^I\ [33m'$HTTP_POST_VARS'[39;49;00m:[33m''[39;49;00m,$
   376^I^I^I^I^I^I^I^I^I\ [33m'$HTTP_POST_FILES'[39;49;00m:[33m''[39;49;00m,$
   377^I^I^I^I^I^I^I^I^I\ [33m'$HTTP_SESSION_VARS'[39;49;00m:[33m''[39;49;00m,$
   378^I^I^I^I^I^I^I^I^I\ [33m'$php_errormsg'[39;49;00m:[33m''[39;49;00m,$
   379^I^I^I^I^I^I^I^I^I\ [33m'$this'[39;49;00m:[33m''[39;49;00m$
   380^I^I^I^I^I^I^I^I^I\ }$
   381^I[37m^I^I" }}}[39;49;00m$
   382^I[37m[39;49;00m$
   383^I[37m^I^I" Internal solution for current file.[39;49;00m$
   384^I^I^I[34mlet[39;49;00m [34mfile[39;49;00m = getline([34m1[39;49;00m, [33m'$'[39;49;00m)$
   385^I^I^I[34mlet[39;49;00m jfile = [34mjoin[39;49;00m([34mfile[39;49;00m, [33m' '[39;49;00m)$
   386^I^I^I[34mlet[39;49;00m int_vals = split(jfile, [33m'\ze\$'[39;49;00m)$
   387^I^I^I[34mlet[39;49;00m int_vars = {}$
   388^I^I^I[34mfor[39;49;00m [34mi[39;49;00m [34min[39;49;00m int_vals$
   389^I^I^I^I[34mif[39;49;00m [34mi[39;49;00m =~ [33m'^\$[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*\s*=\s*new'[39;49;00m$
   390^I^I^I^I^I[34mlet[39;49;00m val = matchstr([34mi[39;49;00m,$
   391^I^I^I^I^I^I^I\ [33m'^\$[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*'[39;49;00m).[33m'->'[39;49;00m$
   392^I^I^I^I[34melse[39;49;00m$
   393^I^I^I^I^I[34mlet[39;49;00m val = matchstr([34mi[39;49;00m,$
   394^I^I^I^I^I^I^I\ [33m'^\$[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*'[39;49;00m)$
   395^I^I^I^I[34mendif[39;49;00m$
   396^I^I^I^I[34mif[39;49;00m val != [33m''[39;49;00m$
   397^I^I^I^I^I[34mlet[39;49;00m int_vars[val] = [33m''[39;49;00m$
   398^I^I^I^I[34mendif[39;49;00m$
   399^I^I^I[34mendfor[39;49;00m$
   400^I$
   401^I^I^I[34mcall[39;49;00m extend(int_vars,[34mg[39;49;00m:php_builtin_vars)$
   402^I[37m[39;49;00m$
   403^I[37m^I^I" ctags has support for PHP, use tags file for external variables[39;49;00m$
   404^I^I^I[34mlet[39;49;00m fnames = [34mjoin[39;49;00m(map(tagfiles(), [33m'escape(v:val, " \\#%")'[39;49;00m))$
   405^I^I^I[34mlet[39;49;00m ext_vars = {}$
   406^I^I^I[34mif[39;49;00m fnames != [33m''[39;49;00m$
   407^I^I^I^I[34mlet[39;49;00m sbase = substitute([34ma[39;49;00m:base, [33m'^\$'[39;49;00m, [33m''[39;49;00m, [33m''[39;49;00m)$
   408^I^I^I^Iexe [33m'silent! vimgrep /^'[39;49;00m.sbase.[33m'.*\tv\(\t\|$\)/j '[39;49;00m.fnames$
   409^I^I^I^I[34mlet[39;49;00m qflist = getqflist()$
   410^I^I^I^I[34mif[39;49;00m len(qflist) > [34m0[39;49;00m$
   411^I^I^I^I^I[34mfor[39;49;00m field [34min[39;49;00m qflist$
   412^I^I^I^I^I^I[34mlet[39;49;00m item = [33m'$'[39;49;00m.matchstr(field[[33m'text'[39;49;00m], [33m'^[^[:space:]]\+'[39;49;00m)$
   413^I^I^I^I^I^I[34mlet[39;49;00m m_menu = [33m''[39;49;00m$
   414^I[37m^I^I^I^I^I" Add -> if it is possible object declaration[39;49;00m$
   415^I^I^I^I^I^I[34mif[39;49;00m field[[33m'text'[39;49;00m] =~ item.[33m'\s*=\s*new\s\+'[39;49;00m$
   416^I^I^I^I^I^I^I[34mlet[39;49;00m item = item.[33m'->'[39;49;00m$
   417^I^I^I^I^I^I^I[34mlet[39;49;00m m_menu = matchstr(field[[33m'text'[39;49;00m],$
   418^I^I^I^I^I^I^I^I^I\ [33m'=\s*new\s\+\zs[a-zA-Z_0-9\x7f-\xff]\+\ze'[39;49;00m)$
   419^I^I^I^I^I^I[34mendif[39;49;00m$
   420^I^I^I^I^I^I[34mlet[39;49;00m ext_vars[item] = m_menu$
   421^I^I^I^I^I[34mendfor[39;49;00m$
   422^I^I^I^I[34mendif[39;49;00m$
   423^I^I^I[34mendif[39;49;00m$
   424^I$
   425^I^I^I[34mcall[39;49;00m extend(int_vars, ext_vars)$
   426^I^I^I[34mlet[39;49;00m [34mg[39;49;00m:a0 = keys(int_vars)$
   427^I$
   428^I^I^I[34mfor[39;49;00m [34mm[39;49;00m [34min[39;49;00m [34msort[39;49;00m(keys(int_vars))$
   429^I^I^I^I[34mif[39;49;00m [34mm[39;49;00m =~ [33m'^\'[39;49;00m.[34ma[39;49;00m:base$
   430^I^I^I^I^I[34mcall[39;49;00m add([34mres[39;49;00m, [34mm[39;49;00m)$
   431^I^I^I^I[34mendif[39;49;00m$
   432^I^I^I[34mendfor[39;49;00m$
   433^I$
   434^I^I^I[34mlet[39;49;00m int_list = [34mres[39;49;00m$
   435^I$
   436^I^I^I[34mlet[39;49;00m int_dict = []$
   437^I^I^I[34mfor[39;49;00m [34mi[39;49;00m [34min[39;49;00m int_list$
   438^I^I^I^I[34mif[39;49;00m int_vars[[34mi[39;49;00m] != [33m''[39;49;00m$
   439^I^I^I^I^I[34mlet[39;49;00m class = [33m' '[39;49;00m$
   440^I^I^I^I^I[34mif[39;49;00m int_vars[[34mi[39;49;00m] != [33m''[39;49;00m$
   441^I^I^I^I^I^I[34mlet[39;49;00m class = [34mi[39;49;00m.[33m' class '[39;49;00m$
   442^I^I^I^I^I[34mendif[39;49;00m$
   443^I^I^I^I^I[34mlet[39;49;00m int_dict += [{[33m'word'[39;49;00m:[34mi[39;49;00m, [33m'info'[39;49;00m:class.int_vars[[34mi[39;49;00m], [33m'kind'[39;49;00m:[33m'v'[39;49;00m}]$
   444^I^I^I^I[34melse[39;49;00m$
   445^I^I^I^I^I[34mlet[39;49;00m int_dict += [{[33m'word'[39;49;00m:[34mi[39;49;00m, [33m'kind'[39;49;00m:[33m'v'[39;49;00m}]$
   446^I^I^I^I[34mendif[39;49;00m$
   447^I^I^I[34mendfor[39;49;00m$
   448^I$
   449^I^I^I[34mreturn[39;49;00m int_dict$
   450^I$
   451^I^I[34melse[39;49;00m$
   452^I[37m^I^I" Complete everything else -[39;49;00m$
   453^I[37m^I^I"  + functions,  DONE[39;49;00m$
   454^I[37m^I^I"  + keywords of language DONE[39;49;00m$
   455^I[37m^I^I"  + defines (constant definitions), DONE[39;49;00m$
   456^I[37m^I^I"  + extend keywords for predefined constants, DONE[39;49;00m$
   457^I[37m^I^I"  + classes (after new), DONE[39;49;00m$
   458^I[37m^I^I"  + limit choice after -> and :: to funcs and vars DONE[39;49;00m$
   459^I[37m[39;49;00m$
   460^I[37m^I^I" Internal solution for finding functions in current file.[39;49;00m$
   461^I^I^I[34mlet[39;49;00m [34mfile[39;49;00m = getline([34m1[39;49;00m, [33m'$'[39;49;00m)$
   462^I^I^I[34mcall[39;49;00m filter([34mfile[39;49;00m,$
   463^I^I^I^I^I\ [33m'v:val =~ "function\\s\\+&\\?[a-zA-Z_\\x7f-\\xff][a-zA-Z_0-9\\x7f-\\xff]*\\s*("'[39;49;00m)$
   464^I^I^I[34mlet[39;49;00m fnames = [34mjoin[39;49;00m(map(tagfiles(), [33m'escape(v:val, " \\#%")'[39;49;00m))$
   465^I^I^I[34mlet[39;49;00m jfile = [34mjoin[39;49;00m([34mfile[39;49;00m, [33m' '[39;49;00m)$
   466^I^I^I[34mlet[39;49;00m int_values = split(jfile, [33m'function\s\+'[39;49;00m)$
   467^I^I^I[34mlet[39;49;00m int_functions = {}$
   468^I^I^I[34mfor[39;49;00m [34mi[39;49;00m [34min[39;49;00m int_values$
   469^I^I^I^I[34mlet[39;49;00m f_name = matchstr([34mi[39;49;00m,$
   470^I^I^I^I^I^I\ [33m'^&\?\zs[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*\ze'[39;49;00m)$
   471^I^I^I^I[34mlet[39;49;00m f_args = matchstr([34mi[39;49;00m,$
   472^I^I^I^I^I^I\ [33m'^&\?[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*\s*(\s*\zs.\{-}\ze\s*)\_s*{'[39;49;00m)$
   473^I^I^I^I[34mlet[39;49;00m int_functions[f_name.[33m'('[39;49;00m] = f_args.[33m')'[39;49;00m$
   474^I^I^I[34mendfor[39;49;00m$
   475^I[37m[39;49;00m$
   476^I[37m^I^I" Prepare list of functions from tags file[39;49;00m$
   477^I^I^I[34mlet[39;49;00m ext_functions = {}$
   478^I^I^I[34mif[39;49;00m fnames != [33m''[39;49;00m$
   479^I^I^I^Iexe [33m'silent! vimgrep /^'[39;49;00m.[34ma[39;49;00m:base.[33m'.*\tf\(\t\|$\)/j '[39;49;00m.fnames$
   480^I^I^I^I[34mlet[39;49;00m qflist = getqflist()$
   481^I^I^I^I[34mif[39;49;00m len(qflist) > [34m0[39;49;00m$
   482^I^I^I^I^I[34mfor[39;49;00m field [34min[39;49;00m qflist$
   483^I[37m^I^I^I^I^I" File name[39;49;00m$
   484^I^I^I^I^I^I[34mlet[39;49;00m item = matchstr(field[[33m'text'[39;49;00m], [33m'^[^[:space:]]\+'[39;49;00m)$
   485^I^I^I^I^I^I[34mlet[39;49;00m fname = matchstr(field[[33m'text'[39;49;00m], [33m'\t\zs\f\+\ze'[39;49;00m)$
   486^I^I^I^I^I^I[34mlet[39;49;00m prototype = matchstr(field[[33m'text'[39;49;00m],$
   487^I^I^I^I^I^I^I^I\ [33m'function\s\+&\?[^[:space:]]\+\s*(\s*\zs.\{-}\ze\s*)\s*{\?'[39;49;00m)$
   488^I^I^I^I^I^I[34mlet[39;49;00m ext_functions[item.[33m'('[39;49;00m] = prototype.[33m') - '[39;49;00m.fname$
   489^I^I^I^I^I[34mendfor[39;49;00m$
   490^I^I^I^I[34mendif[39;49;00m$
   491^I^I^I[34mendif[39;49;00m$
   492^I[37m[39;49;00m$
   493^I[37m^I^I" All functions[39;49;00m$
   494^I^I^I[34mcall[39;49;00m extend(int_functions, ext_functions)$
   495^I^I^I[34mcall[39;49;00m extend(int_functions, [34mg[39;49;00m:php_builtin_functions)$
   496^I[37m[39;49;00m$
   497^I[37m^I^I" Internal solution for finding constants in current file[39;49;00m$
   498^I^I^I[34mlet[39;49;00m [34mfile[39;49;00m = getline([34m1[39;49;00m, [33m'$'[39;49;00m)$
   499^I^I^I[34mcall[39;49;00m filter([34mfile[39;49;00m, [33m'v:val =~ "define\\s*("'[39;49;00m)$
   500^I^I^I[34mlet[39;49;00m jfile = [34mjoin[39;49;00m([34mfile[39;49;00m, [33m' '[39;49;00m)$
   501^I^I^I[34mlet[39;49;00m int_values = split(jfile, [33m'define\s*(\s*'[39;49;00m)$
   502^I^I^I[34mlet[39;49;00m int_constants = {}$
   503^I^I^I[34mfor[39;49;00m [34mi[39;49;00m [34min[39;49;00m int_values$
   504^I^I^I^I[34mlet[39;49;00m c_name = matchstr([34mi[39;49;00m, [33m'\(["'']\)\zs[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*\ze\1'[39;49;00m)$
   505^I[37m^I^I^I" let c_value = matchstr(i,[39;49;00m$
   506^I[37m^I^I^I" \ '\(["'']\)[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*\1\s*,\s*\zs.\{-}\ze\s*)')[39;49;00m$
   507^I^I^I^I[34mif[39;49;00m c_name != [33m''[39;49;00m$
   508^I^I^I^I^I[34mlet[39;49;00m int_constants[c_name] = [33m''[39;49;00m [37m" c_value[39;49;00m$
   509^I^I^I^I[34mendif[39;49;00m$
   510^I^I^I[34mendfor[39;49;00m$
   511^I[37m[39;49;00m$
   512^I[37m^I^I" Prepare list of constants from tags file[39;49;00m$
   513^I^I^I[34mlet[39;49;00m fnames = [34mjoin[39;49;00m(map(tagfiles(), [33m'escape(v:val, " \\#%")'[39;49;00m))$
   514^I^I^I[34mlet[39;49;00m ext_constants = {}$
   515^I^I^I[34mif[39;49;00m fnames != [33m''[39;49;00m$
   516^I^I^I^Iexe [33m'silent! vimgrep /^'[39;49;00m.[34ma[39;49;00m:base.[33m'.*\td\(\t\|$\)/j '[39;49;00m.fnames$
   517^I^I^I^I[34mlet[39;49;00m qflist = getqflist()$
   518^I^I^I^I[34mif[39;49;00m len(qflist) > [34m0[39;49;00m$
   519^I^I^I^I^I[34mfor[39;49;00m field [34min[39;49;00m qflist$
   520^I^I^I^I^I^I[34mlet[39;49;00m item = matchstr(field[[33m'text'[39;49;00m], [33m'^[^[:space:]]\+'[39;49;00m)$
   521^I^I^I^I^I^I[34mlet[39;49;00m ext_constants[item] = [33m''[39;49;00m$
   522^I^I^I^I^I[34mendfor[39;49;00m$
   523^I^I^I^I[34mendif[39;49;00m$
   524^I^I^I[34mendif[39;49;00m$
   525^I[37m[39;49;00m$
   526^I[37m^I^I" All constants[39;49;00m$
   527^I^I^I[34mcall[39;49;00m extend(int_constants, ext_constants)$
   528^I[37m^I^I" Treat keywords as constants[39;49;00m$
   529^I$
   530^I^I^I[34mlet[39;49;00m all_values = {}$
   531^I[37m[39;49;00m$
   532^I[37m^I^I" One big dictionary of functions[39;49;00m$
   533^I^I^I[34mcall[39;49;00m extend(all_values, int_functions)$
   534^I[37m[39;49;00m$
   535^I[37m^I^I" Add constants[39;49;00m$
   536^I^I^I[34mcall[39;49;00m extend(all_values, int_constants)$
   537^I[37m^I^I" Add keywords[39;49;00m$
   538^I^I^I[34mcall[39;49;00m extend(all_values, [34mg[39;49;00m:php_keywords)$
   539^I$
   540^I^I^I[34mfor[39;49;00m [34mm[39;49;00m [34min[39;49;00m [34msort[39;49;00m(keys(all_values))$
   541^I^I^I^I[34mif[39;49;00m [34mm[39;49;00m =~ [33m'^'[39;49;00m.[34ma[39;49;00m:base$
   542^I^I^I^I^I[34mcall[39;49;00m add([34mres[39;49;00m, [34mm[39;49;00m)$
   543^I^I^I^I[34mendif[39;49;00m$
   544^I^I^I[34mendfor[39;49;00m$
   545^I$
   546^I^I^I[34mlet[39;49;00m int_list = [34mres[39;49;00m$
   547^I$
   548^I^I^I[34mlet[39;49;00m final_list = []$
   549^I^I^I[34mfor[39;49;00m [34mi[39;49;00m [34min[39;49;00m int_list$
   550^I^I^I^I[34mif[39;49;00m has_key(int_functions, [34mi[39;49;00m)$
   551^I^I^I^I^I[34mlet[39;49;00m final_list +=$
   552^I^I^I^I^I^I^I\ [{[33m'word'[39;49;00m:[34mi[39;49;00m,$
   553^I^I^I^I^I^I^I\   [33m'info'[39;49;00m:[34mi[39;49;00m.int_functions[[34mi[39;49;00m],$
   554^I^I^I^I^I^I^I\   [33m'kind'[39;49;00m:[33m'f'[39;49;00m}]$
   555^I^I^I^I[34melseif[39;49;00m has_key(int_constants, [34mi[39;49;00m)$
   556^I^I^I^I^I[34mlet[39;49;00m final_list += [{[33m'word'[39;49;00m:[34mi[39;49;00m, [33m'kind'[39;49;00m:[33m'd'[39;49;00m}]$
   557^I^I^I^I[34melse[39;49;00m$
   558^I^I^I^I^I[34mlet[39;49;00m final_list += [{[33m'word'[39;49;00m:[34mi[39;49;00m}]$
   559^I^I^I^I[34mendif[39;49;00m$
   560^I^I^I[34mendfor[39;49;00m$
   561^I$
   562^I^I^I[34mreturn[39;49;00m final_list$
   563^I$
   564^I^I[34mendif[39;49;00m$
   565^I$
   566^I[34mendfunction[39;49;00m$
   567^I[37m" vim:set foldmethod=marker:[39;49;00m$

[37m" Vim completion script[39;49;00m
[37m" Language:^IPHP[39;49;00m
[37m" Maintainer:^IMikolaj Machowski ( mikmach AT wp DOT pl )[39;49;00m
[37m" Last Change:^I2006 May 9[39;49;00m
[37m"[39;49;00m
[37m"   TODO:[39;49;00m
[37m"   - Class aware completion:[39;49;00m
[37m"      a) caching?[39;49;00m
[37m"   - Switching to HTML (XML?) completion (SQL) inside of phpStrings[39;49;00m
[37m"   - allow also for XML completion <- better do html_flavor for HTML[39;49;00m
[37m"     completion[39;49;00m
[37m"   - outside of <?php?> getting parent tag may cause problems. Heh, even in[39;49;00m
[37m"     perfect conditions GetLastOpenTag doesn't cooperate... Inside of[39;49;00m
[37m"     phpStrings this can be even a bonus but outside of <?php?> it is not the[39;49;00m
[37m"     best situation[39;49;00m

[34mfunction[39;49;00m! phpcomplete#CompletePHP(findstart, base)
^I[34mif[39;49;00m [34ma[39;49;00m:findstart
^I^Iunlet! [34mb[39;49;00m:php_menu
[37m^I^I" Check if we are inside of PHP markup[39;49;00m
^I^I[34mlet[39;49;00m pos = getpos([33m'.'[39;49;00m)
^I^I[34mlet[39;49;00m phpbegin = searchpairpos([33m'<?'[39;49;00m, [33m''[39;49;00m, [33m'?>'[39;49;00m, [33m'bWn'[39;49;00m,
^I^I^I^I\ [33m'synIDattr(synID(line("."), col("."), 0), "name") =~? "string\|comment"'[39;49;00m)
^I^I[34mlet[39;49;00m phpend   = searchpairpos([33m'<?'[39;49;00m, [33m''[39;49;00m, [33m'?>'[39;49;00m, [33m'Wn'[39;49;00m,
^I^I^I^I\ [33m'synIDattr(synID(line("."), col("."), 0), "name") =~? "string\|comment"'[39;49;00m)

^I^I[34mif[39;49;00m phpbegin == [[34m0[39;49;00m,[34m0[39;49;00m] && phpend == [[34m0[39;49;00m,[34m0[39;49;00m]
[37m^I^I^I" We are outside of any PHP markup. Complete HTML[39;49;00m
^I^I^I[34mlet[39;49;00m htmlbegin = htmlcomplete#CompleteTags([34m1[39;49;00m, [33m''[39;49;00m)
^I^I^I[34mlet[39;49;00m cursor_col = pos[[34m2[39;49;00m]
^I^I^I[34mlet[39;49;00m base = getline([33m'.'[39;49;00m)[htmlbegin : cursor_col]
^I^I^I[34mlet[39;49;00m [34mb[39;49;00m:php_menu = htmlcomplete#CompleteTags([34m0[39;49;00m, base)
^I^I^I[34mreturn[39;49;00m htmlbegin
^I^I[34melse[39;49;00m
[37m^I^I^I" locate the start of the word[39;49;00m
^I^I^I[34mlet[39;49;00m line = getline([33m'.'[39;49;00m)
^I^I^I[34mlet[39;49;00m [34mstart[39;49;00m = [34mcol[39;49;00m([33m'.'[39;49;00m) - [34m1[39;49;00m
^I^I^I[34mlet[39;49;00m curline = line([33m'.'[39;49;00m)
^I^I^I[34mlet[39;49;00m compl_begin = [34mcol[39;49;00m([33m'.'[39;49;00m) - [34m2[39;49;00m
^I^I^I[34mwhile[39;49;00m [34mstart[39;49;00m >= [34m0[39;49;00m && line[[34mstart[39;49;00m - [34m1[39;49;00m] =~ [33m'[a-zA-Z_0-9\x7f-\xff$]'[39;49;00m
^I^I^I^I[34mlet[39;49;00m [34mstart[39;49;00m -= [34m1[39;49;00m
^I^I^I[34mendwhile[39;49;00m
^I^I^I[34mlet[39;49;00m [34mb[39;49;00m:compl_context = getline([33m'.'[39;49;00m)[[34m0[39;49;00m:compl_begin]
^I^I^I[34mreturn[39;49;00m [34mstart[39;49;00m
[37m[39;49;00m
[37m^I^I^I" We can be also inside of phpString with HTML tags. Deal with[39;49;00m
[37m^I^I^I" it later (time, not lines).[39;49;00m
^I^I[34mendif[39;49;00m

^I[34mendif[39;49;00m
[37m^I" If exists b:php_menu it means completion was already constructed we[39;49;00m
[37m^I" don't need to do anything more[39;49;00m
^I[34mif[39;49;00m exists([33m"b:php_menu"[39;49;00m)
^I^I[34mreturn[39;49;00m [34mb[39;49;00m:php_menu
^I[34mendif[39;49;00m
[37m^I" Initialize base return lists[39;49;00m
^I[34mlet[39;49;00m [34mres[39;49;00m = []
^I[34mlet[39;49;00m res2 = []
[37m^I" a:base is very short - we need context[39;49;00m
^I[34mif[39;49;00m exists([33m"b:compl_context"[39;49;00m)
^I^I[34mlet[39;49;00m context = [34mb[39;49;00m:compl_context
^I^Iunlet! [34mb[39;49;00m:compl_context
^I[34mendif[39;49;00m

^I[34mif[39;49;00m !exists([33m'g:php_builtin_functions'[39;49;00m)
^I^I[34mcall[39;49;00m phpcomplete#LoadData()
^I[34mendif[39;49;00m

^I[34mlet[39;49;00m scontext = substitute(context, [33m'\$\?[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*$'[39;49;00m, [33m''[39;49;00m, [33m''[39;49;00m)

^I[34mif[39;49;00m scontext =~ [33m'\(=\s*new\|extends\)\s\+$'[39;49;00m
[37m^I^I" Complete class name[39;49;00m
[37m^I^I" Internal solution for finding classes in current file.[39;49;00m
^I^I[34mlet[39;49;00m [34mfile[39;49;00m = getline([34m1[39;49;00m, [33m'$'[39;49;00m)
^I^I[34mcall[39;49;00m filter([34mfile[39;49;00m,
^I^I^I^I\ [33m'v:val =~ "class\\s\\+[a-zA-Z_\\x7f-\\xff][a-zA-Z_0-9\\x7f-\\xff]*\\s*("'[39;49;00m)
^I^I[34mlet[39;49;00m fnames = [34mjoin[39;49;00m(map(tagfiles(), [33m'escape(v:val, " \\#%")'[39;49;00m))
^I^I[34mlet[39;49;00m jfile = [34mjoin[39;49;00m([34mfile[39;49;00m, [33m' '[39;49;00m)
^I^I[34mlet[39;49;00m int_values = split(jfile, [33m'class\s\+'[39;49;00m)
^I^I[34mlet[39;49;00m int_classes = {}
^I^I[34mfor[39;49;00m [34mi[39;49;00m [34min[39;49;00m int_values
^I^I^I[34mlet[39;49;00m c_name = matchstr([34mi[39;49;00m, [33m'^[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*'[39;49;00m)
^I^I^I[34mif[39;49;00m c_name != [33m''[39;49;00m
^I^I^I^I[34mlet[39;49;00m int_classes[c_name] = [33m''[39;49;00m
^I^I^I[34mendif[39;49;00m
^I^I[34mendfor[39;49;00m
[37m[39;49;00m
[37m^I^I" Prepare list of classes from tags file[39;49;00m
^I^I[34mlet[39;49;00m ext_classes = {}
^I^I[34mlet[39;49;00m fnames = [34mjoin[39;49;00m(map(tagfiles(), [33m'escape(v:val, " \\#%")'[39;49;00m))
^I^I[34mif[39;49;00m fnames != [33m''[39;49;00m
^I^I^Iexe [33m'silent! vimgrep /^'[39;49;00m.[34ma[39;49;00m:base.[33m'.*\tc\(\t\|$\)/j '[39;49;00m.fnames
^I^I^I[34mlet[39;49;00m qflist = getqflist()
^I^I^I[34mif[39;49;00m len(qflist) > [34m0[39;49;00m
^I^I^I^I[34mfor[39;49;00m field [34min[39;49;00m qflist
[37m^I^I^I^I^I" [:space:] thing: we don't have to be so strict when[39;49;00m
[37m^I^I^I^I^I" dealing with tags files - entries there were already[39;49;00m
[37m^I^I^I^I^I" checked by ctags.[39;49;00m
^I^I^I^I^I[34mlet[39;49;00m item = matchstr(field[[33m'text'[39;49;00m], [33m'^[^[:space:]]\+'[39;49;00m)
^I^I^I^I^I[34mlet[39;49;00m ext_classes[item] = [33m''[39;49;00m
^I^I^I^I[34mendfor[39;49;00m
^I^I^I[34mendif[39;49;00m
^I^I[34mendif[39;49;00m
[37m[39;49;00m
[37m^I^I" Prepare list of built in classes from g:php_builtin_functions[39;49;00m
^I^I[34mif[39;49;00m !exists([33m"g:php_omni_bi_classes"[39;49;00m)
^I^I^I[34mlet[39;49;00m [34mg[39;49;00m:php_omni_bi_classes = {}
^I^I^I[34mfor[39;49;00m [34mi[39;49;00m [34min[39;49;00m keys([34mg[39;49;00m:php_builtin_object_functions)
^I^I^I^I[34mlet[39;49;00m [34mg[39;49;00m:php_omni_bi_classes[substitute([34mi[39;49;00m, [33m'::.*$'[39;49;00m, [33m''[39;49;00m, [33m''[39;49;00m)] = [33m''[39;49;00m
^I^I^I[34mendfor[39;49;00m
^I^I[34mendif[39;49;00m

^I^I[34mlet[39;49;00m classes = [34msort[39;49;00m(keys(int_classes))
^I^I[34mlet[39;49;00m classes += [34msort[39;49;00m(keys(ext_classes))
^I^I[34mlet[39;49;00m classes += [34msort[39;49;00m(keys([34mg[39;49;00m:php_omni_bi_classes))

^I^I[34mfor[39;49;00m [34mm[39;49;00m [34min[39;49;00m classes
^I^I^I[34mif[39;49;00m [34mm[39;49;00m =~ [33m'^'[39;49;00m.[34ma[39;49;00m:base
^I^I^I^I[34mcall[39;49;00m add([34mres[39;49;00m, [34mm[39;49;00m)
^I^I^I[34mendif[39;49;00m
^I^I[34mendfor[39;49;00m

^I^I[34mlet[39;49;00m final_menu = []
^I^I[34mfor[39;49;00m [34mi[39;49;00m [34min[39;49;00m [34mres[39;49;00m
^I^I^I[34mlet[39;49;00m final_menu += [{[33m'word'[39;49;00m:[34mi[39;49;00m, [33m'kind'[39;49;00m:[33m'c'[39;49;00m}]
^I^I[34mendfor[39;49;00m

^I^I[34mreturn[39;49;00m final_menu

^I[34melseif[39;49;00m scontext =~ [33m'\(->\|::\)$'[39;49;00m
[37m^I^I" Complete user functions and variables[39;49;00m
[37m^I^I" Internal solution for current file.[39;49;00m
[37m^I^I" That seems as unnecessary repeating of functions but there are[39;49;00m
[37m^I^I" few not so subtle differences as not appending of $ and addition[39;49;00m
[37m^I^I" of 'kind' tag (not necessary in regular completion)[39;49;00m

^I^I[34mif[39;49;00m scontext =~ [33m'->$'[39;49;00m && scontext !~ [33m'\$this->$'[39;49;00m
[37m[39;49;00m
[37m^I^I^I" Get name of the class[39;49;00m
^I^I^I[34mlet[39;49;00m classname = phpcomplete#GetClassName(scontext)
[37m[39;49;00m
[37m^I^I^I" Get location of class definition, we have to iterate through all[39;49;00m
[37m^I^I^I" tags files separately because we need relative path from current[39;49;00m
[37m^I^I^I" file to the exact file (tags file can be in different dir)[39;49;00m
^I^I^I[34mif[39;49;00m classname != [33m''[39;49;00m
^I^I^I^I[34mlet[39;49;00m classlocation = phpcomplete#GetClassLocation(classname)
^I^I^I[34melse[39;49;00m
^I^I^I^I[34mlet[39;49;00m classlocation = [33m''[39;49;00m
^I^I^I[34mendif[39;49;00m

^I^I^I[34mif[39;49;00m classlocation == [33m'VIMPHP_BUILTINOBJECT'[39;49;00m

^I^I^I^I[34mfor[39;49;00m object [34min[39;49;00m keys([34mg[39;49;00m:php_builtin_object_functions)
^I^I^I^I^I[34mif[39;49;00m object =~ [33m'^'[39;49;00m.classname
^I^I^I^I^I^I[34mlet[39;49;00m [34mres[39;49;00m += [{[33m'word'[39;49;00m:substitute(object, [33m'.*::'[39;49;00m, [33m''[39;49;00m, [33m''[39;49;00m),
^I^I^I^I^I^I^I   ^I\    [33m'info'[39;49;00m: [34mg[39;49;00m:php_builtin_object_functions[object]}]
^I^I^I^I^I[34mendif[39;49;00m
^I^I^I^I[34mendfor[39;49;00m

^I^I^I^I[34mreturn[39;49;00m [34mres[39;49;00m

^I^I^I[34mendif[39;49;00m

^I^I^I[34mif[39;49;00m filereadable(classlocation)
^I^I^I^I[34mlet[39;49;00m classfile = readfile(classlocation)
^I^I^I^I[34mlet[39;49;00m classcontent = [33m''[39;49;00m
^I^I^I^I[34mlet[39;49;00m classcontent .= [33m"\n"[39;49;00m.phpcomplete#GetClassContents(classfile, classname)
^I^I^I^I[34mlet[39;49;00m sccontent = split(classcontent, [33m"\n"[39;49;00m)
[37m[39;49;00m
[37m^I^I^I^I" YES, YES, YES! - we have whole content including extends![39;49;00m
[37m^I^I^I^I" Now we need to get two elements: public functions and public[39;49;00m
[37m^I^I^I^I" vars[39;49;00m
[37m^I^I^I^I" NO, NO, NO! - third separate filtering looking for content[39;49;00m
[37m^I^I^I^I" :(, but all of them have differences. To squeeze them into[39;49;00m
[37m^I^I^I^I" one implementation would require many additional arguments[39;49;00m
[37m^I^I^I^I" and ifs. No good solution[39;49;00m
[37m^I^I^I^I" Functions declared with public keyword or without any[39;49;00m
[37m^I^I^I^I" keyword are public[39;49;00m
^I^I^I^I[34mlet[39;49;00m functions = filter(deepcopy(sccontent),
^I^I^I^I^I^I\ [33m'v:val =~ "^\\s*\\(static\\s\\+\\|public\\s\\+\\)*function"'[39;49;00m)
^I^I^I^I[34mlet[39;49;00m jfuncs = [34mjoin[39;49;00m(functions, [33m' '[39;49;00m)
^I^I^I^I[34mlet[39;49;00m sfuncs = split(jfuncs, [33m'function\s\+'[39;49;00m)
^I^I^I^I[34mlet[39;49;00m c_functions = {}
^I^I^I^I[34mfor[39;49;00m [34mi[39;49;00m [34min[39;49;00m sfuncs
^I^I^I^I^I[34mlet[39;49;00m f_name = matchstr([34mi[39;49;00m,
^I^I^I^I^I^I^I\ [33m'^&\?\zs[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*\ze'[39;49;00m)
^I^I^I^I^I[34mlet[39;49;00m f_args = matchstr([34mi[39;49;00m,
^I^I^I^I^I^I^I\ [33m'^&\?[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*\s*(\zs.\{-}\ze)\_s*{'[39;49;00m)
^I^I^I^I^I[34mif[39;49;00m f_name != [33m''[39;49;00m
^I^I^I^I^I^I[34mlet[39;49;00m c_functions[f_name.[33m'('[39;49;00m] = f_args
^I^I^I^I^I[34mendif[39;49;00m
^I^I^I^I[34mendfor[39;49;00m
[37m^I^I^I^I" Variables declared with var or with public keyword are[39;49;00m
[37m^I^I^I^I" public[39;49;00m
^I^I^I^I[34mlet[39;49;00m variables = filter(deepcopy(sccontent),
^I^I^I^I^I^I\ [33m'v:val =~ "^\\s*\\(public\\|var\\)\\s\\+\\$"'[39;49;00m)
^I^I^I^I[34mlet[39;49;00m jvars = [34mjoin[39;49;00m(variables, [33m' '[39;49;00m)
^I^I^I^I[34mlet[39;49;00m svars = split(jvars, [33m'\$'[39;49;00m)
^I^I^I^I[34mlet[39;49;00m c_variables = {}
^I^I^I^I[34mfor[39;49;00m [34mi[39;49;00m [34min[39;49;00m svars
^I^I^I^I^I[34mlet[39;49;00m c_var = matchstr([34mi[39;49;00m,
^I^I^I^I^I^I^I\ [33m'^\zs[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*\ze'[39;49;00m)
^I^I^I^I^I[34mif[39;49;00m c_var != [33m''[39;49;00m
^I^I^I^I^I^I[34mlet[39;49;00m c_variables[c_var] = [33m''[39;49;00m
^I^I^I^I^I[34mendif[39;49;00m
^I^I^I^I[34mendfor[39;49;00m

^I^I^I^I[34mlet[39;49;00m all_values = {}
^I^I^I^I[34mcall[39;49;00m extend(all_values, c_functions)
^I^I^I^I[34mcall[39;49;00m extend(all_values, c_variables)

^I^I^I^I[34mfor[39;49;00m [34mm[39;49;00m [34min[39;49;00m [34msort[39;49;00m(keys(all_values))
^I^I^I^I^I[34mif[39;49;00m [34mm[39;49;00m =~ [33m'^'[39;49;00m.[34ma[39;49;00m:base && [34mm[39;49;00m !~ [33m'::'[39;49;00m
^I^I^I^I^I^I[34mcall[39;49;00m add([34mres[39;49;00m, [34mm[39;49;00m)
^I^I^I^I^I[34melseif[39;49;00m [34mm[39;49;00m =~ [33m'::'[39;49;00m.[34ma[39;49;00m:base
^I^I^I^I^I^I[34mcall[39;49;00m add(res2, [34mm[39;49;00m)
^I^I^I^I^I[34mendif[39;49;00m
^I^I^I^I[34mendfor[39;49;00m

^I^I^I^I[34mlet[39;49;00m start_list = [34mres[39;49;00m + res2

^I^I^I^I[34mlet[39;49;00m final_list = []
^I^I^I^I[34mfor[39;49;00m [34mi[39;49;00m [34min[39;49;00m start_list
^I^I^I^I^I[34mif[39;49;00m has_key(c_variables, [34mi[39;49;00m)
^I^I^I^I^I^I[34mlet[39;49;00m class = [33m' '[39;49;00m
^I^I^I^I^I^I[34mif[39;49;00m all_values[[34mi[39;49;00m] != [33m''[39;49;00m
^I^I^I^I^I^I^I[34mlet[39;49;00m class = [34mi[39;49;00m.[33m' class '[39;49;00m
^I^I^I^I^I^I[34mendif[39;49;00m
^I^I^I^I^I^I[34mlet[39;49;00m final_list +=
^I^I^I^I^I^I^I^I\ [{[33m'word'[39;49;00m:[34mi[39;49;00m,
^I^I^I^I^I^I^I^I\   [33m'info'[39;49;00m:class.all_values[[34mi[39;49;00m],
^I^I^I^I^I^I^I^I\   [33m'kind'[39;49;00m:[33m'v'[39;49;00m}]
^I^I^I^I^I[34melse[39;49;00m
^I^I^I^I^I^I[34mlet[39;49;00m final_list +=
^I^I^I^I^I^I^I^I\ [{[33m'word'[39;49;00m:substitute([34mi[39;49;00m, [33m'.*::'[39;49;00m, [33m''[39;49;00m, [33m''[39;49;00m),
^I^I^I^I^I^I^I^I\   [33m'info'[39;49;00m:[34mi[39;49;00m.all_values[[34mi[39;49;00m].[33m')'[39;49;00m,
^I^I^I^I^I^I^I^I\   [33m'kind'[39;49;00m:[33m'f'[39;49;00m}]
^I^I^I^I^I[34mendif[39;49;00m
^I^I^I^I[34mendfor[39;49;00m

^I^I^I^I[34mreturn[39;49;00m final_list

^I^I^I[34mendif[39;49;00m

^I^I[34mendif[39;49;00m

^I^I[34mif[39;49;00m [34ma[39;49;00m:base =~ [33m'^\$'[39;49;00m
^I^I^I[34mlet[39;49;00m adddollar = [33m'$'[39;49;00m
^I^I[34melse[39;49;00m
^I^I^I[34mlet[39;49;00m adddollar = [33m''[39;49;00m
^I^I[34mendif[39;49;00m
^I^I[34mlet[39;49;00m [34mfile[39;49;00m = getline([34m1[39;49;00m, [33m'$'[39;49;00m)
^I^I[34mlet[39;49;00m jfile = [34mjoin[39;49;00m([34mfile[39;49;00m, [33m' '[39;49;00m)
^I^I[34mlet[39;49;00m sfile = split(jfile, [33m'\$'[39;49;00m)
^I^I[34mlet[39;49;00m int_vars = {}
^I^I[34mfor[39;49;00m [34mi[39;49;00m [34min[39;49;00m sfile
^I^I^I[34mif[39;49;00m [34mi[39;49;00m =~ [33m'^\$[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*\s*=\s*new'[39;49;00m
^I^I^I^I[34mlet[39;49;00m val = matchstr([34mi[39;49;00m, [33m'^[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*'[39;49;00m).[33m'->'[39;49;00m
^I^I^I[34melse[39;49;00m
^I^I^I^I[34mlet[39;49;00m val = matchstr([34mi[39;49;00m, [33m'^[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*'[39;49;00m)
^I^I^I[34mendif[39;49;00m
^I^I^I[34mif[39;49;00m val !~ [33m''[39;49;00m
^I^I^I^I[34mlet[39;49;00m int_vars[adddollar.val] = [33m''[39;49;00m
^I^I^I[34mendif[39;49;00m
^I^I[34mendfor[39;49;00m
[37m[39;49;00m
[37m^I^I" ctags has good support for PHP, use tags file for external[39;49;00m
[37m^I^I" variables[39;49;00m
^I^I[34mlet[39;49;00m fnames = [34mjoin[39;49;00m(map(tagfiles(), [33m'escape(v:val, " \\#%")'[39;49;00m))
^I^I[34mlet[39;49;00m ext_vars = {}
^I^I[34mif[39;49;00m fnames != [33m''[39;49;00m
^I^I^I[34mlet[39;49;00m sbase = substitute([34ma[39;49;00m:base, [33m'^\$'[39;49;00m, [33m''[39;49;00m, [33m''[39;49;00m)
^I^I^Iexe [33m'silent! vimgrep /^'[39;49;00m.sbase.[33m'.*\tv\(\t\|$\)/j '[39;49;00m.fnames
^I^I^I[34mlet[39;49;00m qflist = getqflist()
^I^I^I[34mif[39;49;00m len(qflist) > [34m0[39;49;00m
^I^I^I^I[34mfor[39;49;00m field [34min[39;49;00m qflist
^I^I^I^I^I[34mlet[39;49;00m item = matchstr(field[[33m'text'[39;49;00m], [33m'^[^[:space:]]\+'[39;49;00m)
[37m^I^I^I^I^I" Add -> if it is possible object declaration[39;49;00m
^I^I^I^I^I[34mlet[39;49;00m classname = [33m''[39;49;00m
^I^I^I^I^I[34mif[39;49;00m field[[33m'text'[39;49;00m] =~ item.[33m'\s*=\s*new\s\+'[39;49;00m
^I^I^I^I^I^I[34mlet[39;49;00m item = item.[33m'->'[39;49;00m
^I^I^I^I^I^I[34mlet[39;49;00m classname = matchstr(field[[33m'text'[39;49;00m],
^I^I^I^I^I^I^I^I\ [33m'=\s*new\s\+\zs[a-zA-Z_0-9\x7f-\xff]\+\ze'[39;49;00m)
^I^I^I^I^I[34mendif[39;49;00m
^I^I^I^I^I[34mlet[39;49;00m ext_vars[adddollar.item] = classname
^I^I^I^I[34mendfor[39;49;00m
^I^I^I[34mendif[39;49;00m
^I^I[34mendif[39;49;00m
[37m[39;49;00m
[37m^I^I" Now we have all variables in int_vars dictionary[39;49;00m
^I^I[34mcall[39;49;00m extend(int_vars, ext_vars)
[37m[39;49;00m
[37m^I^I" Internal solution for finding functions in current file.[39;49;00m
^I^I[34mlet[39;49;00m [34mfile[39;49;00m = getline([34m1[39;49;00m, [33m'$'[39;49;00m)
^I^I[34mcall[39;49;00m filter([34mfile[39;49;00m,
^I^I^I^I\ [33m'v:val =~ "function\\s\\+&\\?[a-zA-Z_\\x7f-\\xff][a-zA-Z_0-9\\x7f-\\xff]*\\s*("'[39;49;00m)
^I^I[34mlet[39;49;00m fnames = [34mjoin[39;49;00m(map(tagfiles(), [33m'escape(v:val, " \\#%")'[39;49;00m))
^I^I[34mlet[39;49;00m jfile = [34mjoin[39;49;00m([34mfile[39;49;00m, [33m' '[39;49;00m)
^I^I[34mlet[39;49;00m int_values = split(jfile, [33m'function\s\+'[39;49;00m)
^I^I[34mlet[39;49;00m int_functions = {}
^I^I[34mfor[39;49;00m [34mi[39;49;00m [34min[39;49;00m int_values
^I^I^I[34mlet[39;49;00m f_name = matchstr([34mi[39;49;00m,
^I^I^I^I^I\ [33m'^&\?\zs[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*\ze'[39;49;00m)
^I^I^I[34mlet[39;49;00m f_args = matchstr([34mi[39;49;00m,
^I^I^I^I^I\ [33m'^&\?[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*\s*(\zs.\{-}\ze)\_s*{'[39;49;00m)
^I^I^I[34mlet[39;49;00m int_functions[f_name.[33m'('[39;49;00m] = f_args.[33m')'[39;49;00m
^I^I[34mendfor[39;49;00m
[37m[39;49;00m
[37m^I^I" Prepare list of functions from tags file[39;49;00m
^I^I[34mlet[39;49;00m ext_functions = {}
^I^I[34mif[39;49;00m fnames != [33m''[39;49;00m
^I^I^Iexe [33m'silent! vimgrep /^'[39;49;00m.[34ma[39;49;00m:base.[33m'.*\tf\(\t\|$\)/j '[39;49;00m.fnames
^I^I^I[34mlet[39;49;00m qflist = getqflist()
^I^I^I[34mif[39;49;00m len(qflist) > [34m0[39;49;00m
^I^I^I^I[34mfor[39;49;00m field [34min[39;49;00m qflist
[37m^I^I^I^I^I" File name[39;49;00m
^I^I^I^I^I[34mlet[39;49;00m item = matchstr(field[[33m'text'[39;49;00m], [33m'^[^[:space:]]\+'[39;49;00m)
^I^I^I^I^I[34mlet[39;49;00m fname = matchstr(field[[33m'text'[39;49;00m], [33m'\t\zs\f\+\ze'[39;49;00m)
^I^I^I^I^I[34mlet[39;49;00m prototype = matchstr(field[[33m'text'[39;49;00m],
^I^I^I^I^I^I^I\ [33m'function\s\+&\?[^[:space:]]\+\s*(\s*\zs.\{-}\ze\s*)\s*{\?'[39;49;00m)
^I^I^I^I^I[34mlet[39;49;00m ext_functions[item.[33m'('[39;49;00m] = prototype.[33m') - '[39;49;00m.fname
^I^I^I^I[34mendfor[39;49;00m
^I^I^I[34mendif[39;49;00m
^I^I[34mendif[39;49;00m

^I^I[34mlet[39;49;00m all_values = {}
^I^I[34mcall[39;49;00m extend(all_values, int_functions)
^I^I[34mcall[39;49;00m extend(all_values, ext_functions)
^I^I[34mcall[39;49;00m extend(all_values, int_vars) [37m" external variables are already in[39;49;00m
^I^I[34mcall[39;49;00m extend(all_values, [34mg[39;49;00m:php_builtin_object_functions)

^I^I[34mfor[39;49;00m [34mm[39;49;00m [34min[39;49;00m [34msort[39;49;00m(keys(all_values))
^I^I^I[34mif[39;49;00m [34mm[39;49;00m =~ [33m'\(^\|::\)'[39;49;00m.[34ma[39;49;00m:base
^I^I^I^I[34mcall[39;49;00m add([34mres[39;49;00m, [34mm[39;49;00m)
^I^I^I[34mendif[39;49;00m
^I^I[34mendfor[39;49;00m

^I^I[34mlet[39;49;00m start_list = [34mres[39;49;00m

^I^I[34mlet[39;49;00m final_list = []
^I^I[34mfor[39;49;00m [34mi[39;49;00m [34min[39;49;00m start_list
^I^I^I[34mif[39;49;00m has_key(int_vars, [34mi[39;49;00m)
^I^I^I^I[34mlet[39;49;00m class = [33m' '[39;49;00m
^I^I^I^I[34mif[39;49;00m all_values[[34mi[39;49;00m] != [33m''[39;49;00m
^I^I^I^I^I[34mlet[39;49;00m class = [34mi[39;49;00m.[33m' class '[39;49;00m
^I^I^I^I[34mendif[39;49;00m
^I^I^I^I[34mlet[39;49;00m final_list += [{[33m'word'[39;49;00m:[34mi[39;49;00m, [33m'info'[39;49;00m:class.all_values[[34mi[39;49;00m], [33m'kind'[39;49;00m:[33m'v'[39;49;00m}]
^I^I^I[34melse[39;49;00m
^I^I^I^I[34mlet[39;49;00m final_list +=
^I^I^I^I^I^I\ [{[33m'word'[39;49;00m:substitute([34mi[39;49;00m, [33m'.*::'[39;49;00m, [33m''[39;49;00m, [33m''[39;49;00m),
^I^I^I^I^I^I\   [33m'info'[39;49;00m:[34mi[39;49;00m.all_values[[34mi[39;49;00m],
^I^I^I^I^I^I\   [33m'kind'[39;49;00m:[33m'f'[39;49;00m}]
^I^I^I[34mendif[39;49;00m
^I^I[34mendfor[39;49;00m

^I^I[34mreturn[39;49;00m final_list
^I[34mendif[39;49;00m

^I[34mif[39;49;00m [34ma[39;49;00m:base =~ [33m'^\$'[39;49;00m
[37m^I^I" Complete variables[39;49;00m
[37m^I^I" Built-in variables {{{[39;49;00m
^I^I[34mlet[39;49;00m [34mg[39;49;00m:php_builtin_vars = {[33m'$GLOBALS'[39;49;00m:[33m''[39;49;00m,
^I^I^I^I^I^I^I^I\ [33m'$_SERVER'[39;49;00m:[33m''[39;49;00m,
^I^I^I^I^I^I^I^I\ [33m'$_GET'[39;49;00m:[33m''[39;49;00m,
^I^I^I^I^I^I^I^I\ [33m'$_POST'[39;49;00m:[33m''[39;49;00m,
^I^I^I^I^I^I^I^I\ [33m'$_COOKIE'[39;49;00m:[33m''[39;49;00m,
^I^I^I^I^I^I^I^I\ [33m'$_FILES'[39;49;00m:[33m''[39;49;00m,
^I^I^I^I^I^I^I^I\ [33m'$_ENV'[39;49;00m:[33m''[39;49;00m,
^I^I^I^I^I^I^I^I\ [33m'$_REQUEST'[39;49;00m:[33m''[39;49;00m,
^I^I^I^I^I^I^I^I\ [33m'$_SESSION'[39;49;00m:[33m''[39;49;00m,
^I^I^I^I^I^I^I^I\ [33m'$HTTP_SERVER_VARS'[39;49;00m:[33m''[39;49;00m,
^I^I^I^I^I^I^I^I\ [33m'$HTTP_ENV_VARS'[39;49;00m:[33m''[39;49;00m,
^I^I^I^I^I^I^I^I\ [33m'$HTTP_COOKIE_VARS'[39;49;00m:[33m''[39;49;00m,
^I^I^I^I^I^I^I^I\ [33m'$HTTP_GET_VARS'[39;49;00m:[33m''[39;49;00m,
^I^I^I^I^I^I^I^I\ [33m'$HTTP_POST_VARS'[39;49;00m:[33m''[39;49;00m,
^I^I^I^I^I^I^I^I\ [33m'$HTTP_POST_FILES'[39;49;00m:[33m''[39;49;00m,
^I^I^I^I^I^I^I^I\ [33m'$HTTP_SESSION_VARS'[39;49;00m:[33m''[39;49;00m,
^I^I^I^I^I^I^I^I\ [33m'$php_errormsg'[39;49;00m:[33m''[39;49;00m,
^I^I^I^I^I^I^I^I\ [33m'$this'[39;49;00m:[33m''[39;49;00m
^I^I^I^I^I^I^I^I\ }
[37m^I^I" }}}[39;49;00m
[37m[39;49;00m
[37m^I^I" Internal solution for current file.[39;49;00m
^I^I[34mlet[39;49;00m [34mfile[39;49;00m = getline([34m1[39;49;00m, [33m'$'[39;49;00m)
^I^I[34mlet[39;49;00m jfile = [34mjoin[39;49;00m([34mfile[39;49;00m, [33m' '[39;49;00m)
^I^I[34mlet[39;49;00m int_vals = split(jfile, [33m'\ze\$'[39;49;00m)
^I^I[34mlet[39;49;00m int_vars = {}
^I^I[34mfor[39;49;00m [34mi[39;49;00m [34min[39;49;00m int_vals
^I^I^I[34mif[39;49;00m [34mi[39;49;00m =~ [33m'^\$[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*\s*=\s*new'[39;49;00m
^I^I^I^I[34mlet[39;49;00m val = matchstr([34mi[39;49;00m,
^I^I^I^I^I^I\ [33m'^\$[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*'[39;49;00m).[33m'->'[39;49;00m
^I^I^I[34melse[39;49;00m
^I^I^I^I[34mlet[39;49;00m val = matchstr([34mi[39;49;00m,
^I^I^I^I^I^I\ [33m'^\$[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*'[39;49;00m)
^I^I^I[34mendif[39;49;00m
^I^I^I[34mif[39;49;00m val != [33m''[39;49;00m
^I^I^I^I[34mlet[39;49;00m int_vars[val] = [33m''[39;49;00m
^I^I^I[34mendif[39;49;00m
^I^I[34mendfor[39;49;00m

^I^I[34mcall[39;49;00m extend(int_vars,[34mg[39;49;00m:php_builtin_vars)
[37m[39;49;00m
[37m^I^I" ctags has support for PHP, use tags file for external variables[39;49;00m
^I^I[34mlet[39;49;00m fnames = [34mjoin[39;49;00m(map(tagfiles(), [33m'escape(v:val, " \\#%")'[39;49;00m))
^I^I[34mlet[39;49;00m ext_vars = {}
^I^I[34mif[39;49;00m fnames != [33m''[39;49;00m
^I^I^I[34mlet[39;49;00m sbase = substitute([34ma[39;49;00m:base, [33m'^\$'[39;49;00m, [33m''[39;49;00m, [33m''[39;49;00m)
^I^I^Iexe [33m'silent! vimgrep /^'[39;49;00m.sbase.[33m'.*\tv\(\t\|$\)/j '[39;49;00m.fnames
^I^I^I[34mlet[39;49;00m qflist = getqflist()
^I^I^I[34mif[39;49;00m len(qflist) > [34m0[39;49;00m
^I^I^I^I[34mfor[39;49;00m field [34min[39;49;00m qflist
^I^I^I^I^I[34mlet[39;49;00m item = [33m'$'[39;49;00m.matchstr(field[[33m'text'[39;49;00m], [33m'^[^[:space:]]\+'[39;49;00m)
^I^I^I^I^I[34mlet[39;49;00m m_menu = [33m''[39;49;00m
[37m^I^I^I^I^I" Add -> if it is possible object declaration[39;49;00m
^I^I^I^I^I[34mif[39;49;00m field[[33m'text'[39;49;00m] =~ item.[33m'\s*=\s*new\s\+'[39;49;00m
^I^I^I^I^I^I[34mlet[39;49;00m item = item.[33m'->'[39;49;00m
^I^I^I^I^I^I[34mlet[39;49;00m m_menu = matchstr(field[[33m'text'[39;49;00m],
^I^I^I^I^I^I^I^I\ [33m'=\s*new\s\+\zs[a-zA-Z_0-9\x7f-\xff]\+\ze'[39;49;00m)
^I^I^I^I^I[34mendif[39;49;00m
^I^I^I^I^I[34mlet[39;49;00m ext_vars[item] = m_menu
^I^I^I^I[34mendfor[39;49;00m
^I^I^I[34mendif[39;49;00m
^I^I[34mendif[39;49;00m

^I^I[34mcall[39;49;00m extend(int_vars, ext_vars)
^I^I[34mlet[39;49;00m [34mg[39;49;00m:a0 = keys(int_vars)

^I^I[34mfor[39;49;00m [34mm[39;49;00m [34min[39;49;00m [34msort[39;49;00m(keys(int_vars))
^I^I^I[34mif[39;49;00m [34mm[39;49;00m =~ [33m'^\'[39;49;00m.[34ma[39;49;00m:base
^I^I^I^I[34mcall[39;49;00m add([34mres[39;49;00m, [34mm[39;49;00m)
^I^I^I[34mendif[39;49;00m
^I^I[34mendfor[39;49;00m

^I^I[34mlet[39;49;00m int_list = [34mres[39;49;00m

^I^I[34mlet[39;49;00m int_dict = []
^I^I[34mfor[39;49;00m [34mi[39;49;00m [34min[39;49;00m int_list
^I^I^I[34mif[39;49;00m int_vars[[34mi[39;49;00m] != [33m''[39;49;00m
^I^I^I^I[34mlet[39;49;00m class = [33m' '[39;49;00m
^I^I^I^I[34mif[39;49;00m int_vars[[34mi[39;49;00m] != [33m''[39;49;00m
^I^I^I^I^I[34mlet[39;49;00m class = [34mi[39;49;00m.[33m' class '[39;49;00m
^I^I^I^I[34mendif[39;49;00m
^I^I^I^I[34mlet[39;49;00m int_dict += [{[33m'word'[39;49;00m:[34mi[39;49;00m, [33m'info'[39;49;00m:class.int_vars[[34mi[39;49;00m], [33m'kind'[39;49;00m:[33m'v'[39;49;00m}]
^I^I^I[34melse[39;49;00m
^I^I^I^I[34mlet[39;49;00m int_dict += [{[33m'word'[39;49;00m:[34mi[39;49;00m, [33m'kind'[39;49;00m:[33m'v'[39;49;00m}]
^I^I^I[34mendif[39;49;00m
^I^I[34mendfor[39;49;00m

^I^I[34mreturn[39;49;00m int_dict

^I[34melse[39;49;00m
[37m^I^I" Complete everything else -[39;49;00m
[37m^I^I"  + functions,  DONE[39;49;00m
[37m^I^I"  + keywords of language DONE[39;49;00m
[37m^I^I"  + defines (constant definitions), DONE[39;49;00m
[37m^I^I"  + extend keywords for predefined constants, DONE[39;49;00m
[37m^I^I"  + classes (after new), DONE[39;49;00m
[37m^I^I"  + limit choice after -> and :: to funcs and vars DONE[39;49;00m
[37m[39;49;00m
[37m^I^I" Internal solution for finding functions in current file.[39;49;00m
^I^I[34mlet[39;49;00m [34mfile[39;49;00m = getline([34m1[39;49;00m, [33m'$'[39;49;00m)
^I^I[34mcall[39;49;00m filter([34mfile[39;49;00m,
^I^I^I^I\ [33m'v:val =~ "function\\s\\+&\\?[a-zA-Z_\\x7f-\\xff][a-zA-Z_0-9\\x7f-\\xff]*\\s*("'[39;49;00m)
^I^I[34mlet[39;49;00m fnames = [34mjoin[39;49;00m(map(tagfiles(), [33m'escape(v:val, " \\#%")'[39;49;00m))
^I^I[34mlet[39;49;00m jfile = [34mjoin[39;49;00m([34mfile[39;49;00m, [33m' '[39;49;00m)
^I^I[34mlet[39;49;00m int_values = split(jfile, [33m'function\s\+'[39;49;00m)
^I^I[34mlet[39;49;00m int_functions = {}
^I^I[34mfor[39;49;00m [34mi[39;49;00m [34min[39;49;00m int_values
^I^I^I[34mlet[39;49;00m f_name = matchstr([34mi[39;49;00m,
^I^I^I^I^I\ [33m'^&\?\zs[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*\ze'[39;49;00m)
^I^I^I[34mlet[39;49;00m f_args = matchstr([34mi[39;49;00m,
^I^I^I^I^I\ [33m'^&\?[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*\s*(\s*\zs.\{-}\ze\s*)\_s*{'[39;49;00m)
^I^I^I[34mlet[39;49;00m int_functions[f_name.[33m'('[39;49;00m] = f_args.[33m')'[39;49;00m
^I^I[34mendfor[39;49;00m
[37m[39;49;00m
[37m^I^I" Prepare list of functions from tags file[39;49;00m
^I^I[34mlet[39;49;00m ext_functions = {}
^I^I[34mif[39;49;00m fnames != [33m''[39;49;00m
^I^I^Iexe [33m'silent! vimgrep /^'[39;49;00m.[34ma[39;49;00m:base.[33m'.*\tf\(\t\|$\)/j '[39;49;00m.fnames
^I^I^I[34mlet[39;49;00m qflist = getqflist()
^I^I^I[34mif[39;49;00m len(qflist) > [34m0[39;49;00m
^I^I^I^I[34mfor[39;49;00m field [34min[39;49;00m qflist
[37m^I^I^I^I^I" File name[39;49;00m
^I^I^I^I^I[34mlet[39;49;00m item = matchstr(field[[33m'text'[39;49;00m], [33m'^[^[:space:]]\+'[39;49;00m)
^I^I^I^I^I[34mlet[39;49;00m fname = matchstr(field[[33m'text'[39;49;00m], [33m'\t\zs\f\+\ze'[39;49;00m)
^I^I^I^I^I[34mlet[39;49;00m prototype = matchstr(field[[33m'text'[39;49;00m],
^I^I^I^I^I^I^I\ [33m'function\s\+&\?[^[:space:]]\+\s*(\s*\zs.\{-}\ze\s*)\s*{\?'[39;49;00m)
^I^I^I^I^I[34mlet[39;49;00m ext_functions[item.[33m'('[39;49;00m] = prototype.[33m') - '[39;49;00m.fname
^I^I^I^I[34mendfor[39;49;00m
^I^I^I[34mendif[39;49;00m
^I^I[34mendif[39;49;00m
[37m[39;49;00m
[37m^I^I" All functions[39;49;00m
^I^I[34mcall[39;49;00m extend(int_functions, ext_functions)
^I^I[34mcall[39;49;00m extend(int_functions, [34mg[39;49;00m:php_builtin_functions)
[37m[39;49;00m
[37m^I^I" Internal solution for finding constants in current file[39;49;00m
^I^I[34mlet[39;49;00m [34mfile[39;49;00m = getline([34m1[39;49;00m, [33m'$'[39;49;00m)
^I^I[34mcall[39;49;00m filter([34mfile[39;49;00m, [33m'v:val =~ "define\\s*("'[39;49;00m)
^I^I[34mlet[39;49;00m jfile = [34mjoin[39;49;00m([34mfile[39;49;00m, [33m' '[39;49;00m)
^I^I[34mlet[39;49;00m int_values = split(jfile, [33m'define\s*(\s*'[39;49;00m)
^I^I[34mlet[39;49;00m int_constants = {}
^I^I[34mfor[39;49;00m [34mi[39;49;00m [34min[39;49;00m int_values
^I^I^I[34mlet[39;49;00m c_name = matchstr([34mi[39;49;00m, [33m'\(["'']\)\zs[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*\ze\1'[39;49;00m)
[37m^I^I^I" let c_value = matchstr(i,[39;49;00m
[37m^I^I^I" \ '\(["'']\)[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*\1\s*,\s*\zs.\{-}\ze\s*)')[39;49;00m
^I^I^I[34mif[39;49;00m c_name != [33m''[39;49;00m
^I^I^I^I[34mlet[39;49;00m int_constants[c_name] = [33m''[39;49;00m [37m" c_value[39;49;00m
^I^I^I[34mendif[39;49;00m
^I^I[34mendfor[39;49;00m
[37m[39;49;00m
[37m^I^I" Prepare list of constants from tags file[39;49;00m
^I^I[34mlet[39;49;00m fnames = [34mjoin[39;49;00m(map(tagfiles(), [33m'escape(v:val, " \\#%")'[39;49;00m))
^I^I[34mlet[39;49;00m ext_constants = {}
^I^I[34mif[39;49;00m fnames != [33m''[39;49;00m
^I^I^Iexe [33m'silent! vimgrep /^'[39;49;00m.[34ma[39;49;00m:base.[33m'.*\td\(\t\|$\)/j '[39;49;00m.fnames
^I^I^I[34mlet[39;49;00m qflist = getqflist()
^I^I^I[34mif[39;49;00m len(qflist) > [34m0[39;49;00m
^I^I^I^I[34mfor[39;49;00m field [34min[39;49;00m qflist
^I^I^I^I^I[34mlet[39;49;00m item = matchstr(field[[33m'text'[39;49;00m], [33m'^[^[:space:]]\+'[39;49;00m)
^I^I^I^I^I[34mlet[39;49;00m ext_constants[item] = [33m''[39;49;00m
^I^I^I^I[34mendfor[39;49;00m
^I^I^I[34mendif[39;49;00m
^I^I[34mendif[39;49;00m
[37m[39;49;00m
[37m^I^I" All constants[39;49;00m
^I^I[34mcall[39;49;00m extend(int_constants, ext_constants)
[37m^I^I" Treat keywords as constants[39;49;00m

^I^I[34mlet[39;49;00m all_values = {}
[37m[39;49;00m
[37m^I^I" One big dictionary of functions[39;49;00m
^I^I[34mcall[39;49;00m extend(all_values, int_functions)
[37m[39;49;00m
[37m^I^I" Add constants[39;49;00m
^I^I[34mcall[39;49;00m extend(all_values, int_constants)
[37m^I^I" Add keywords[39;49;00m
^I^I[34mcall[39;49;00m extend(all_values, [34mg[39;49;00m:php_keywords)

^I^I[34mfor[39;49;00m [34mm[39;49;00m [34min[39;49;00m [34msort[39;49;00m(keys(all_values))
^I^I^I[34mif[39;49;00m [34mm[39;49;00m =~ [33m'^'[39;49;00m.[34ma[39;49;00m:base
^I^I^I^I[34mcall[39;49;00m add([34mres[39;49;00m, [34mm[39;49;00m)
^I^I^I[34mendif[39;49;00m
^I^I[34mendfor[39;49;00m

^I^I[34mlet[39;49;00m int_list = [34mres[39;49;00m

^I^I[34mlet[39;49;00m final_list = []
^I^I[34mfor[39;49;00m [34mi[39;49;00m [34min[39;49;00m int_list
^I^I^I[34mif[39;49;00m has_key(int_functions, [34mi[39;49;00m)
^I^I^I^I[34mlet[39;49;00m final_list +=
^I^I^I^I^I^I\ [{[33m'word'[39;49;00m:[34mi[39;49;00m,
^I^I^I^I^I^I\   [33m'info'[39;49;00m:[34mi[39;49;00m.int_functions[[34mi[39;49;00m],
^I^I^I^I^I^I\   [33m'kind'[39;49;00m:[33m'f'[39;49;00m}]
^I^I^I[34melseif[39;49;00m has_key(int_constants, [34mi[39;49;00m)
^I^I^I^I[34mlet[39;49;00m final_list += [{[33m'word'[39;49;00m:[34mi[39;49;00m, [33m'kind'[39;49;00m:[33m'd'[39;49;00m}]
^I^I^I[34melse[39;49;00m
^I^I^I^I[34mlet[39;49;00m final_list += [{[33m'word'[39;49;00m:[34mi[39;49;00m}]
^I^I^I[34mendif[39;49;00m
^I^I[34mendfor[39;49;00m

^I^I[34mreturn[39;49;00m final_list

^I[34mendif[39;49;00m

[34mendfunction[39;49;00m
[37m" vim:set foldmethod=marker:[39;49;00m

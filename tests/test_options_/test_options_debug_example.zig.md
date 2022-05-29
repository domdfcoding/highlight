Using lexer <pygments.lexers.ZigLexer with {'ensurenl': False, 'tabsize': 0}>
[34mconst[39;49;00m[37m [39;49;00mstd[37m [39;49;00m=[37m [39;49;00m[36m@import[39;49;00m([33m"[39;49;00m[33mstd[39;49;00m[33m"[39;49;00m);[37m[39;49;00m
[34mconst[39;49;00m[37m [39;49;00mAllocator[37m [39;49;00m=[37m [39;49;00mmem.Allocator;[37m[39;49;00m
[34mconst[39;49;00m[37m [39;49;00mmem[37m [39;49;00m=[37m [39;49;00mstd.mem;[37m[39;49;00m
[34mconst[39;49;00m[37m [39;49;00mast[37m [39;49;00m=[37m [39;49;00mstd.zig.ast;[37m[39;49;00m
[34mconst[39;49;00m[37m [39;49;00mVisib[37m [39;49;00m=[37m [39;49;00m[36m@import[39;49;00m([33m"[39;49;00m[33mvisib.zig[39;49;00m[33m"[39;49;00m).Visib;[37m[39;49;00m
[34mconst[39;49;00m[37m [39;49;00mevent[37m [39;49;00m=[37m [39;49;00mstd.event;[37m[39;49;00m
[34mconst[39;49;00m[37m [39;49;00mValue[37m [39;49;00m=[37m [39;49;00m[36m@import[39;49;00m([33m"[39;49;00m[33mvalue.zig[39;49;00m[33m"[39;49;00m).Value;[37m[39;49;00m
[34mconst[39;49;00m[37m [39;49;00mToken[37m [39;49;00m=[37m [39;49;00mstd.zig.Token;[37m[39;49;00m
[34mconst[39;49;00m[37m [39;49;00merrmsg[37m [39;49;00m=[37m [39;49;00m[36m@import[39;49;00m([33m"[39;49;00m[33merrmsg.zig[39;49;00m[33m"[39;49;00m);[37m[39;49;00m
[34mconst[39;49;00m[37m [39;49;00mScope[37m [39;49;00m=[37m [39;49;00m[36m@import[39;49;00m([33m"[39;49;00m[33mscope.zig[39;49;00m[33m"[39;49;00m).Scope;[37m[39;49;00m
[34mconst[39;49;00m[37m [39;49;00mCompilation[37m [39;49;00m=[37m [39;49;00m[36m@import[39;49;00m([33m"[39;49;00m[33mcompilation.zig[39;49;00m[33m"[39;49;00m).Compilation;[37m[39;49;00m
[37m[39;49;00m
[34mpub[39;49;00m[37m [39;49;00m[34mconst[39;49;00m[37m [39;49;00mDecl[37m [39;49;00m=[37m [39;49;00m[34mstruct[39;49;00m[37m [39;49;00m{[37m[39;49;00m
[37m    [39;49;00mid:[37m [39;49;00mId,[37m[39;49;00m
[37m    [39;49;00mname:[37m [39;49;00m[][34mconst[39;49;00m[37m [39;49;00m[36mu8[39;49;00m,[37m[39;49;00m
[37m    [39;49;00mvisib:[37m [39;49;00mVisib,[37m[39;49;00m
[37m    [39;49;00mresolution:[37m [39;49;00mevent.Future(Compilation.BuildError![36mvoid[39;49;00m),[37m[39;49;00m
[37m    [39;49;00mparent_scope:[37m [39;49;00m*Scope,[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[37m// TODO when we destroy the decl, deref the tree scope[39;49;00m
[37m    [39;49;00mtree_scope:[37m [39;49;00m*Scope.AstTree,[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[34mpub[39;49;00m[37m [39;49;00m[34mconst[39;49;00m[37m [39;49;00mTable[37m [39;49;00m=[37m [39;49;00mstd.HashMap([][34mconst[39;49;00m[37m [39;49;00m[36mu8[39;49;00m,[37m [39;49;00m*Decl,[37m [39;49;00mmem.hash_slice_u8,[37m [39;49;00mmem.eql_slice_u8);[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[34mpub[39;49;00m[37m [39;49;00m[34mfn[39;49;00m[37m [39;49;00mcast(base:[37m [39;49;00m*Decl,[37m [39;49;00m[34mcomptime[39;49;00m[37m [39;49;00mT:[37m [39;49;00m[36mtype[39;49;00m)[37m [39;49;00m?*T[37m [39;49;00m{[37m[39;49;00m
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(base.id[37m [39;49;00m!=[37m [39;49;00m[36m@field[39;49;00m(Id,[37m [39;49;00m[36m@typeName[39;49;00m(T)))[37m [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mnull[39;49;00m;[37m[39;49;00m
[37m        [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[36m@fieldParentPtr[39;49;00m(T,[37m [39;49;00m[33m"[39;49;00m[33mbase[39;49;00m[33m"[39;49;00m,[37m [39;49;00mbase);[37m[39;49;00m
[37m    [39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[34mpub[39;49;00m[37m [39;49;00m[34mfn[39;49;00m[37m [39;49;00misExported(base:[37m [39;49;00m*[34mconst[39;49;00m[37m [39;49;00mDecl,[37m [39;49;00mtree:[37m [39;49;00m*ast.Tree)[37m [39;49;00m[36mbool[39;49;00m[37m [39;49;00m{[37m[39;49;00m
[37m        [39;49;00m[34mswitch[39;49;00m[37m [39;49;00m(base.id)[37m [39;49;00m{[37m[39;49;00m
[37m            [39;49;00mId.Fn[37m [39;49;00m=>[37m [39;49;00m{[37m[39;49;00m
[37m                [39;49;00m[34mconst[39;49;00m[37m [39;49;00mfn_decl[37m [39;49;00m=[37m [39;49;00m[36m@fieldParentPtr[39;49;00m(Fn,[37m [39;49;00m[33m"[39;49;00m[33mbase[39;49;00m[33m"[39;49;00m,[37m [39;49;00mbase);[37m[39;49;00m
[37m                [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mfn_decl.isExported(tree);[37m[39;49;00m
[37m            [39;49;00m},[37m[39;49;00m
[37m            [39;49;00m[34melse[39;49;00m[37m [39;49;00m=>[37m [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mfalse[39;49;00m,[37m[39;49;00m
[37m        [39;49;00m}[37m[39;49;00m
[37m    [39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[34mpub[39;49;00m[37m [39;49;00m[34mfn[39;49;00m[37m [39;49;00mgetSpan(base:[37m [39;49;00m*[34mconst[39;49;00m[37m [39;49;00mDecl)[37m [39;49;00merrmsg.Span[37m [39;49;00m{[37m[39;49;00m
[37m        [39;49;00m[34mswitch[39;49;00m[37m [39;49;00m(base.id)[37m [39;49;00m{[37m[39;49;00m
[37m            [39;49;00mId.Fn[37m [39;49;00m=>[37m [39;49;00m{[37m[39;49;00m
[37m                [39;49;00m[34mconst[39;49;00m[37m [39;49;00mfn_decl[37m [39;49;00m=[37m [39;49;00m[36m@fieldParentPtr[39;49;00m(Fn,[37m [39;49;00m[33m"[39;49;00m[33mbase[39;49;00m[33m"[39;49;00m,[37m [39;49;00mbase);[37m[39;49;00m
[37m                [39;49;00m[34mconst[39;49;00m[37m [39;49;00mfn_proto[37m [39;49;00m=[37m [39;49;00mfn_decl.fn_proto;[37m[39;49;00m
[37m                [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstart[37m [39;49;00m=[37m [39;49;00mfn_proto.fn_token;[37m[39;49;00m
[37m                [39;49;00m[34mconst[39;49;00m[37m [39;49;00mend[37m [39;49;00m=[37m [39;49;00mfn_proto.name_token[37m [39;49;00m[34morelse[39;49;00m[37m [39;49;00mstart;[37m[39;49;00m
[37m                [39;49;00m[34mreturn[39;49;00m[37m [39;49;00merrmsg.Span{[37m[39;49;00m
[37m                    [39;49;00m.first[37m [39;49;00m=[37m [39;49;00mstart,[37m[39;49;00m
[37m                    [39;49;00m.last[37m [39;49;00m=[37m [39;49;00mend[37m [39;49;00m+[37m [39;49;00m[34m1[39;49;00m,[37m[39;49;00m
[37m                [39;49;00m};[37m[39;49;00m
[37m            [39;49;00m},[37m[39;49;00m
[37m            [39;49;00m[34melse[39;49;00m[37m [39;49;00m=>[37m [39;49;00m[36m@panic[39;49;00m([33m"[39;49;00m[33mTODO[39;49;00m[33m"[39;49;00m),[37m[39;49;00m
[37m        [39;49;00m}[37m[39;49;00m
[37m    [39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[34mpub[39;49;00m[37m [39;49;00m[34mfn[39;49;00m[37m [39;49;00mfindRootScope(base:[37m [39;49;00m*[34mconst[39;49;00m[37m [39;49;00mDecl)[37m [39;49;00m*Scope.Root[37m [39;49;00m{[37m[39;49;00m
[37m        [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mbase.parent_scope.findRoot();[37m[39;49;00m
[37m    [39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[34mpub[39;49;00m[37m [39;49;00m[34mconst[39;49;00m[37m [39;49;00mId[37m [39;49;00m=[37m [39;49;00m[34menum[39;49;00m[37m [39;49;00m{[37m[39;49;00m
[37m        [39;49;00mVar,[37m[39;49;00m
[37m        [39;49;00mFn,[37m[39;49;00m
[37m        [39;49;00mCompTime,[37m[39;49;00m
[37m    [39;49;00m};[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[34mpub[39;49;00m[37m [39;49;00m[34mconst[39;49;00m[37m [39;49;00mVar[37m [39;49;00m=[37m [39;49;00m[34mstruct[39;49;00m[37m [39;49;00m{[37m[39;49;00m
[37m        [39;49;00mbase:[37m [39;49;00mDecl,[37m[39;49;00m
[37m    [39;49;00m};[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[34mpub[39;49;00m[37m [39;49;00m[34mconst[39;49;00m[37m [39;49;00mFn[37m [39;49;00m=[37m [39;49;00m[34mstruct[39;49;00m[37m [39;49;00m{[37m[39;49;00m
[37m        [39;49;00mbase:[37m [39;49;00mDecl,[37m[39;49;00m
[37m        [39;49;00mvalue:[37m [39;49;00mVal,[37m[39;49;00m
[37m        [39;49;00mfn_proto:[37m [39;49;00m*ast.Node.FnProto,[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[37m// TODO https://github.com/ziglang/zig/issues/683 and then make this anonymous[39;49;00m
[37m        [39;49;00m[34mpub[39;49;00m[37m [39;49;00m[34mconst[39;49;00m[37m [39;49;00mVal[37m [39;49;00m=[37m [39;49;00m[34munion[39;49;00m([34menum[39;49;00m)[37m [39;49;00m{[37m[39;49;00m
[37m            [39;49;00mUnresolved:[37m [39;49;00m[36mvoid[39;49;00m,[37m[39;49;00m
[37m            [39;49;00mFn:[37m [39;49;00m*Value.Fn,[37m[39;49;00m
[37m            [39;49;00mFnProto:[37m [39;49;00m*Value.FnProto,[37m[39;49;00m
[37m        [39;49;00m};[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[34mpub[39;49;00m[37m [39;49;00m[34mfn[39;49;00m[37m [39;49;00mexternLibName(self:[37m [39;49;00mFn,[37m [39;49;00mtree:[37m [39;49;00m*ast.Tree)[37m [39;49;00m?[][34mconst[39;49;00m[37m [39;49;00m[36mu8[39;49;00m[37m [39;49;00m{[37m[39;49;00m
[37m            [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(self.fn_proto.extern_export_inline_token)[37m [39;49;00m|tok_index|[37m [39;49;00mx:[37m [39;49;00m{[37m[39;49;00m
[37m                [39;49;00m[34mconst[39;49;00m[37m [39;49;00mtoken[37m [39;49;00m=[37m [39;49;00mtree.tokens.at(tok_index);[37m[39;49;00m
[37m                [39;49;00m[34mbreak[39;49;00m[37m [39;49;00m:x[37m [39;49;00m[34mswitch[39;49;00m[37m [39;49;00m(token.id)[37m [39;49;00m{[37m[39;49;00m
[37m                    [39;49;00mToken.Id.Extern[37m [39;49;00m=>[37m [39;49;00mtree.tokenSlicePtr(token),[37m[39;49;00m
[37m                    [39;49;00m[34melse[39;49;00m[37m [39;49;00m=>[37m [39;49;00m[34mnull[39;49;00m,[37m[39;49;00m
[37m                [39;49;00m};[37m[39;49;00m
[37m            [39;49;00m}[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mnull[39;49;00m;[37m[39;49;00m
[37m        [39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[34mpub[39;49;00m[37m [39;49;00m[34mfn[39;49;00m[37m [39;49;00misExported(self:[37m [39;49;00mFn,[37m [39;49;00mtree:[37m [39;49;00m*ast.Tree)[37m [39;49;00m[36mbool[39;49;00m[37m [39;49;00m{[37m[39;49;00m
[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(self.fn_proto.extern_export_inline_token)[37m [39;49;00m|tok_index|[37m [39;49;00m{[37m[39;49;00m
[37m                [39;49;00m[34mconst[39;49;00m[37m [39;49;00mtoken[37m [39;49;00m=[37m [39;49;00mtree.tokens.at(tok_index);[37m[39;49;00m
[37m                [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mtoken.id[37m [39;49;00m==[37m [39;49;00mToken.Id.Keyword_export;[37m[39;49;00m
[37m            [39;49;00m}[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m
[37m                [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mfalse[39;49;00m;[37m[39;49;00m
[37m            [39;49;00m}[37m[39;49;00m
[37m        [39;49;00m}[37m[39;49;00m
[37m    [39;49;00m};[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[34mpub[39;49;00m[37m [39;49;00m[34mconst[39;49;00m[37m [39;49;00mCompTime[37m [39;49;00m=[37m [39;49;00m[34mstruct[39;49;00m[37m [39;49;00m{[37m[39;49;00m
[37m        [39;49;00mbase:[37m [39;49;00mDecl,[37m[39;49;00m
[37m    [39;49;00m};[37m[39;49;00m
};[37m[39;49;00m
[37m[39;49;00m
[34mpub[39;49;00m[37m [39;49;00m[34mconst[39;49;00m[37m [39;49;00minfo_zen[37m [39;49;00m=[37m[39;49;00m
[37m    [39;49;00m[33m\\[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[33m\\ * Communicate intent precisely.[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[33m\\ * Edge cases matter.[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[33m\\ * Favor reading code over writing code.[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[33m\\ * Only one obvious way to do things.[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[33m\\ * Runtime crashes are better than bugs.[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[33m\\ * Compile errors are better than runtime crashes.[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[33m\\ * Incremental improvements.[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[33m\\ * Avoid local maximums.[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[33m\\ * Reduce the amount one must remember.[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[33m\\ * Minimize energy spent on coding style.[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[33m\\ * Together we serve end users.[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[33m\\[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[33m\\[39;49;00m[37m[39;49;00m
;[37m[39;49;00m
[37m[39;49;00m
[34mfn[39;49;00m[37m [39;49;00mcmdZen(allocator:[37m [39;49;00m*Allocator,[37m [39;49;00margs:[37m [39;49;00m[][34mconst[39;49;00m[37m [39;49;00m[][34mconst[39;49;00m[37m [39;49;00m[36mu8[39;49;00m)[37m [39;49;00m![36mvoid[39;49;00m[37m [39;49;00m{[37m[39;49;00m
[37m    [39;49;00m[34mtry[39;49;00m[37m [39;49;00mstdout.write(info_zen);[37m[39;49;00m
}[37m[39;49;00m
[37m[39;49;00m
[34mconst[39;49;00m[37m [39;49;00musage_internal[37m [39;49;00m=[37m[39;49;00m
[37m    [39;49;00m[33m\\usage: zig internal [subcommand][39;49;00m[37m[39;49;00m
[37m    [39;49;00m[33m\\[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[33m\\Sub-Commands:[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[33m\\  build-info                   Print static compiler build-info[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[33m\\[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[33m\\[39;49;00m[37m[39;49;00m
;[37m[39;49;00m
[37m[39;49;00m
[34mfn[39;49;00m[37m [39;49;00mcmdInternal(allocator:[37m [39;49;00m*Allocator,[37m [39;49;00margs:[37m [39;49;00m[][34mconst[39;49;00m[37m [39;49;00m[][34mconst[39;49;00m[37m [39;49;00m[36mu8[39;49;00m)[37m [39;49;00m![36mvoid[39;49;00m[37m [39;49;00m{[37m[39;49;00m
[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(args.len[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m{[37m[39;49;00m
[37m        [39;49;00m[34mtry[39;49;00m[37m [39;49;00mstderr.write(usage_internal);[37m[39;49;00m
[37m        [39;49;00mos.exit([34m1[39;49;00m);[37m[39;49;00m
[37m    [39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[34mconst[39;49;00m[37m [39;49;00msub_commands[37m [39;49;00m=[37m [39;49;00m[]Command{Command{[37m[39;49;00m
[37m        [39;49;00m.name[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33mbuild-info[39;49;00m[33m"[39;49;00m,[37m[39;49;00m
[37m        [39;49;00m.exec[37m [39;49;00m=[37m [39;49;00mcmdInternalBuildInfo,[37m[39;49;00m
[37m    [39;49;00m}};[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[34mfor[39;49;00m[37m [39;49;00m(sub_commands)[37m [39;49;00m|sub_command|[37m [39;49;00m{[37m[39;49;00m
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(mem.eql([36mu8[39;49;00m,[37m [39;49;00msub_command.name,[37m [39;49;00margs[[34m0[39;49;00m]))[37m [39;49;00m{[37m[39;49;00m
[37m            [39;49;00m[34mtry[39;49;00m[37m [39;49;00msub_command.exec(allocator,[37m [39;49;00margs[[34m1[39;49;00m..]);[37m[39;49;00m
[37m            [39;49;00m[34mreturn[39;49;00m;[37m[39;49;00m
[37m        [39;49;00m}[37m[39;49;00m
[37m    [39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[34mtry[39;49;00m[37m [39;49;00mstderr.print([33m"[39;49;00m[33munknown sub command: {}[39;49;00m[33m\n[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m,[37m [39;49;00margs[[34m0[39;49;00m]);[37m[39;49;00m
[37m    [39;49;00m[34mtry[39;49;00m[37m [39;49;00mstderr.write(usage_internal);[37m[39;49;00m
}[37m[39;49;00m
[37m[39;49;00m
[34mfn[39;49;00m[37m [39;49;00mcmdInternalBuildInfo(allocator:[37m [39;49;00m*Allocator,[37m [39;49;00margs:[37m [39;49;00m[][34mconst[39;49;00m[37m [39;49;00m[][34mconst[39;49;00m[37m [39;49;00m[36mu8[39;49;00m)[37m [39;49;00m![36mvoid[39;49;00m[37m [39;49;00m{[37m[39;49;00m
[37m    [39;49;00m[34mtry[39;49;00m[37m [39;49;00mstdout.print([37m[39;49;00m
[37m        [39;49;00m[33m\\ZIG_CMAKE_BINARY_DIR {}[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[33m\\ZIG_CXX_COMPILER     {}[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[33m\\ZIG_LLVM_CONFIG_EXE  {}[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[33m\\ZIG_LLD_INCLUDE_PATH {}[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[33m\\ZIG_LLD_LIBRARIES    {}[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[33m\\ZIG_STD_FILES        {}[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[33m\\ZIG_C_HEADER_FILES   {}[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[33m\\ZIG_DIA_GUIDS_LIB    {}[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[33m\\[39;49;00m[37m[39;49;00m
[37m    [39;49;00m,[37m[39;49;00m
[37m        [39;49;00mstd.cstr.toSliceConst(c.ZIG_CMAKE_BINARY_DIR),[37m[39;49;00m
[37m        [39;49;00mstd.cstr.toSliceConst(c.ZIG_CXX_COMPILER),[37m[39;49;00m
[37m        [39;49;00mstd.cstr.toSliceConst(c.ZIG_LLVM_CONFIG_EXE),[37m[39;49;00m
[37m        [39;49;00mstd.cstr.toSliceConst(c.ZIG_LLD_INCLUDE_PATH),[37m[39;49;00m
[37m        [39;49;00mstd.cstr.toSliceConst(c.ZIG_LLD_LIBRARIES),[37m[39;49;00m
[37m        [39;49;00mstd.cstr.toSliceConst(c.ZIG_STD_FILES),[37m[39;49;00m
[37m        [39;49;00mstd.cstr.toSliceConst(c.ZIG_C_HEADER_FILES),[37m[39;49;00m
[37m        [39;49;00mstd.cstr.toSliceConst(c.ZIG_DIA_GUIDS_LIB),[37m[39;49;00m
[37m    [39;49;00m);[37m[39;49;00m
}[37m[39;49;00m
[37m[39;49;00m
[34mfn[39;49;00m[37m [39;49;00mtest__floatuntisf(a:[37m [39;49;00m[36mu128[39;49;00m,[37m [39;49;00mexpected:[37m [39;49;00m[36mf32[39;49;00m)[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m{[37m[39;49;00m
[37m    [39;49;00m[34mconst[39;49;00m[37m [39;49;00mx[37m [39;49;00m=[37m [39;49;00m__floatuntisf(a);[37m[39;49;00m
[37m    [39;49;00mtesting.expect(x[37m [39;49;00m==[37m [39;49;00mexpected);[37m[39;49;00m
}[37m[39;49;00m
[37m[39;49;00m
[34mtest[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mfloatuntisf[39;49;00m[33m"[39;49;00m[37m [39;49;00m{[37m[39;49;00m
[37m    [39;49;00mtest__floatuntisf([34m0[39;49;00m,[37m [39;49;00m[34m0.0[39;49;00m);[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00mtest__floatuntisf([34m1[39;49;00m,[37m [39;49;00m[34m1.0[39;49;00m);[37m[39;49;00m
[37m    [39;49;00mtest__floatuntisf([34m2[39;49;00m,[37m [39;49;00m[34m2.0[39;49;00m);[37m[39;49;00m
[37m    [39;49;00mtest__floatuntisf([34m20[39;49;00m,[37m [39;49;00m[34m20.0[39;49;00m);[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00mtest__floatuntisf([34m0x7FFFFF8000000000[39;49;00m,[37m [39;49;00m[34m0x1.FFFFFEp+62[39;49;00m);[37m[39;49;00m
[37m    [39;49;00mtest__floatuntisf([34m0x7FFFFF0000000000[39;49;00m,[37m [39;49;00m[34m0x1.FFFFFCp+62[39;49;00m);[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00mtest__floatuntisf(make_ti([34m0x8000008000000000[39;49;00m,[37m [39;49;00m[34m0[39;49;00m),[37m [39;49;00m[34m0x1.000001p+127[39;49;00m);[37m[39;49;00m
[37m    [39;49;00mtest__floatuntisf(make_ti([34m0x8000000000000800[39;49;00m,[37m [39;49;00m[34m0[39;49;00m),[37m [39;49;00m[34m0x1.0p+127[39;49;00m);[37m[39;49;00m
[37m    [39;49;00mtest__floatuntisf(make_ti([34m0x8000010000000000[39;49;00m,[37m [39;49;00m[34m0[39;49;00m),[37m [39;49;00m[34m0x1.000002p+127[39;49;00m);[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00mtest__floatuntisf(make_ti([34m0x8000000000000000[39;49;00m,[37m [39;49;00m[34m0[39;49;00m),[37m [39;49;00m[34m0x1.000000p+127[39;49;00m);[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00mtest__floatuntisf([34m0x0007FB72E8000000[39;49;00m,[37m [39;49;00m[34m0x1.FEDCBAp+50[39;49;00m);[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00mtest__floatuntisf([34m0x0007FB72EA000000[39;49;00m,[37m [39;49;00m[34m0x1.FEDCBA8p+50[39;49;00m);[37m[39;49;00m
[37m    [39;49;00mtest__floatuntisf([34m0x0007FB72EB000000[39;49;00m,[37m [39;49;00m[34m0x1.FEDCBACp+50[39;49;00m);[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00mtest__floatuntisf([34m0x0007FB72EC000000[39;49;00m,[37m [39;49;00m[34m0x1.FEDCBBp+50[39;49;00m);[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00mtest__floatuntisf([34m0x0007FB72E6000000[39;49;00m,[37m [39;49;00m[34m0x1.FEDCB98p+50[39;49;00m);[37m[39;49;00m
[37m    [39;49;00mtest__floatuntisf([34m0x0007FB72E7000000[39;49;00m,[37m [39;49;00m[34m0x1.FEDCB9Cp+50[39;49;00m);[37m[39;49;00m
[37m    [39;49;00mtest__floatuntisf([34m0x0007FB72E4000000[39;49;00m,[37m [39;49;00m[34m0x1.FEDCB9p+50[39;49;00m);[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00mtest__floatuntisf([34m0xFFFFFFFFFFFFFFFE[39;49;00m,[37m [39;49;00m[34m0x1p+64[39;49;00m);[37m[39;49;00m
[37m    [39;49;00mtest__floatuntisf([34m0xFFFFFFFFFFFFFFFF[39;49;00m,[37m [39;49;00m[34m0x1p+64[39;49;00m);[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00mtest__floatuntisf([34m0x0007FB72E8000000[39;49;00m,[37m [39;49;00m[34m0x1.FEDCBAp+50[39;49;00m);[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00mtest__floatuntisf([34m0x0007FB72EA000000[39;49;00m,[37m [39;49;00m[34m0x1.FEDCBAp+50[39;49;00m);[37m[39;49;00m
[37m    [39;49;00mtest__floatuntisf([34m0x0007FB72EB000000[39;49;00m,[37m [39;49;00m[34m0x1.FEDCBAp+50[39;49;00m);[37m[39;49;00m
[37m    [39;49;00mtest__floatuntisf([34m0x0007FB72EBFFFFFF[39;49;00m,[37m [39;49;00m[34m0x1.FEDCBAp+50[39;49;00m);[37m[39;49;00m
[37m    [39;49;00mtest__floatuntisf([34m0x0007FB72EC000000[39;49;00m,[37m [39;49;00m[34m0x1.FEDCBCp+50[39;49;00m);[37m[39;49;00m
[37m    [39;49;00mtest__floatuntisf([34m0x0007FB72E8000001[39;49;00m,[37m [39;49;00m[34m0x1.FEDCBAp+50[39;49;00m);[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00mtest__floatuntisf([34m0x0007FB72E6000000[39;49;00m,[37m [39;49;00m[34m0x1.FEDCBAp+50[39;49;00m);[37m[39;49;00m
[37m    [39;49;00mtest__floatuntisf([34m0x0007FB72E7000000[39;49;00m,[37m [39;49;00m[34m0x1.FEDCBAp+50[39;49;00m);[37m[39;49;00m
[37m    [39;49;00mtest__floatuntisf([34m0x0007FB72E7FFFFFF[39;49;00m,[37m [39;49;00m[34m0x1.FEDCBAp+50[39;49;00m);[37m[39;49;00m
[37m    [39;49;00mtest__floatuntisf([34m0x0007FB72E4000001[39;49;00m,[37m [39;49;00m[34m0x1.FEDCBAp+50[39;49;00m);[37m[39;49;00m
[37m    [39;49;00mtest__floatuntisf([34m0x0007FB72E4000000[39;49;00m,[37m [39;49;00m[34m0x1.FEDCB8p+50[39;49;00m);[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00mtest__floatuntisf(make_ti([34m0x0000000000001FED[39;49;00m,[37m [39;49;00m[34m0xCB90000000000001[39;49;00m),[37m [39;49;00m[34m0x1.FEDCBAp+76[39;49;00m);[37m[39;49;00m
[37m    [39;49;00mtest__floatuntisf(make_ti([34m0x0000000000001FED[39;49;00m,[37m [39;49;00m[34m0xCBA0000000000000[39;49;00m),[37m [39;49;00m[34m0x1.FEDCBAp+76[39;49;00m);[37m[39;49;00m
[37m    [39;49;00mtest__floatuntisf(make_ti([34m0x0000000000001FED[39;49;00m,[37m [39;49;00m[34m0xCBAFFFFFFFFFFFFF[39;49;00m),[37m [39;49;00m[34m0x1.FEDCBAp+76[39;49;00m);[37m[39;49;00m
[37m    [39;49;00mtest__floatuntisf(make_ti([34m0x0000000000001FED[39;49;00m,[37m [39;49;00m[34m0xCBB0000000000000[39;49;00m),[37m [39;49;00m[34m0x1.FEDCBCp+76[39;49;00m);[37m[39;49;00m
[37m    [39;49;00mtest__floatuntisf(make_ti([34m0x0000000000001FED[39;49;00m,[37m [39;49;00m[34m0xCBB0000000000001[39;49;00m),[37m [39;49;00m[34m0x1.FEDCBCp+76[39;49;00m);[37m[39;49;00m
[37m    [39;49;00mtest__floatuntisf(make_ti([34m0x0000000000001FED[39;49;00m,[37m [39;49;00m[34m0xCBBFFFFFFFFFFFFF[39;49;00m),[37m [39;49;00m[34m0x1.FEDCBCp+76[39;49;00m);[37m[39;49;00m
[37m    [39;49;00mtest__floatuntisf(make_ti([34m0x0000000000001FED[39;49;00m,[37m [39;49;00m[34m0xCBC0000000000000[39;49;00m),[37m [39;49;00m[34m0x1.FEDCBCp+76[39;49;00m);[37m[39;49;00m
[37m    [39;49;00mtest__floatuntisf(make_ti([34m0x0000000000001FED[39;49;00m,[37m [39;49;00m[34m0xCBC0000000000001[39;49;00m),[37m [39;49;00m[34m0x1.FEDCBCp+76[39;49;00m);[37m[39;49;00m
[37m    [39;49;00mtest__floatuntisf(make_ti([34m0x0000000000001FED[39;49;00m,[37m [39;49;00m[34m0xCBD0000000000000[39;49;00m),[37m [39;49;00m[34m0x1.FEDCBCp+76[39;49;00m);[37m[39;49;00m
[37m    [39;49;00mtest__floatuntisf(make_ti([34m0x0000000000001FED[39;49;00m,[37m [39;49;00m[34m0xCBD0000000000001[39;49;00m),[37m [39;49;00m[34m0x1.FEDCBEp+76[39;49;00m);[37m[39;49;00m
[37m    [39;49;00mtest__floatuntisf(make_ti([34m0x0000000000001FED[39;49;00m,[37m [39;49;00m[34m0xCBDFFFFFFFFFFFFF[39;49;00m),[37m [39;49;00m[34m0x1.FEDCBEp+76[39;49;00m);[37m[39;49;00m
[37m    [39;49;00mtest__floatuntisf(make_ti([34m0x0000000000001FED[39;49;00m,[37m [39;49;00m[34m0xCBE0000000000000[39;49;00m),[37m [39;49;00m[34m0x1.FEDCBEp+76[39;49;00m);[37m[39;49;00m
}[37m[39;49;00m
[37m[39;49;00m
[34mfn[39;49;00m[37m [39;49;00mtrimStart(slice:[37m [39;49;00m[][34mconst[39;49;00m[37m [39;49;00m[36mu8[39;49;00m,[37m [39;49;00mch:[37m [39;49;00m[36mu8[39;49;00m)[37m [39;49;00m[][34mconst[39;49;00m[37m [39;49;00m[36mu8[39;49;00m[37m [39;49;00m{[37m[39;49;00m
[37m    [39;49;00m[34mvar[39;49;00m[37m [39;49;00mi:[37m [39;49;00m[36musize[39;49;00m[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m
[37m    [39;49;00m[34mconst[39;49;00m[37m [39;49;00mtest_string[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33mtest[39;49;00m[33m\"[39;49;00m[33mstring[39;49;00m[33m"[39;49;00m;[37m[39;49;00m
[37m    [39;49;00m[34mfor[39;49;00m[37m [39;49;00m(slice)[37m [39;49;00m|b|[37m [39;49;00m{[37m[39;49;00m
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(b[37m [39;49;00m==[37m [39;49;00m[33m'\xa3'[39;49;00m)[37m [39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(b[37m [39;49;00m==[37m [39;49;00m[33m'\ua3d3'[39;49;00m)[37m [39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(b[37m [39;49;00m==[37m [39;49;00m[33m'\Ua3d3d3'[39;49;00m)[37m [39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(b[37m [39;49;00m==[37m [39;49;00m[33m'\t'[39;49;00m)[37m [39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(b[37m [39;49;00m==[37m [39;49;00m[33m'\n'[39;49;00m)[37m [39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(b[37m [39;49;00m==[37m [39;49;00m[33m'\\'[39;49;00m)[37m [39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(b[37m [39;49;00m==[37m [39;49;00m[33m'\''[39;49;00m)[37m [39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(b[37m [39;49;00m==[37m [39;49;00m[33m'"'[39;49;00m)[37m [39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(b[37m [39;49;00m!=[37m [39;49;00m[33m'n'[39;49;00m)[37m [39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(b[37m [39;49;00m!=[37m [39;49;00m[33m'-'[39;49;00m)[37m [39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m
[37m        [39;49;00mi[37m [39;49;00m+=[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m
[37m    [39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mslice[i..];[37m[39;49;00m
}
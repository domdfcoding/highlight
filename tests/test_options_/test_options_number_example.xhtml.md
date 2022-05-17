     1	<[94mhtml[39;49;00m>
     2	  <[94mhead[39;49;00m>
     3	    <[94mscript[39;49;00m [36mlang[39;49;00m=[33m"javascript"[39;49;00m [36mtype[39;49;00m=[33m"text/javascript"[39;49;00m>[37m[39;49;00m
     4	[37m  [39;49;00m[37m// <!--[39;49;00m[37m[39;49;00m
     5	[37m    [39;49;00m[34mfunction[39;49;00m[37m [39;49;00mtoggleVisible(element)[37m [39;49;00m{[37m[39;49;00m
     6	[37m      [39;49;00m[34mif[39;49;00m[37m [39;49;00m(element.style.display[37m [39;49;00m==[37m [39;49;00m[33m'block'[39;49;00m)[37m [39;49;00m{[37m[39;49;00m
     7	[37m        [39;49;00melement.style.display[37m [39;49;00m=[37m [39;49;00m[33m'none'[39;49;00m;[37m[39;49;00m
     8	[37m       [39;49;00m}[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m
     9	[37m         [39;49;00melement.style.display[37m [39;49;00m=[37m [39;49;00m[33m'block'[39;49;00m;[37m[39;49;00m
    10	[37m       [39;49;00m}[37m[39;49;00m
    11	[37m       [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mfalse[39;49;00m;[37m      [39;49;00m
    12	[37m    [39;49;00m}[37m          [39;49;00m
    13	[37m    [39;49;00m[37m// -->[39;49;00m[37m[39;49;00m
    14	[37m    [39;49;00m</[94mscript[39;49;00m>
    15	    <[94mtitle[39;49;00m>Error</[94mtitle[39;49;00m>
    16	    <[94mstyle[39;49;00m>[37m[39;49;00m
    17	[37m      [39;49;00m.[04m[32mpath[39;49;00m[37m [39;49;00m{[37m [39;49;00m
    18	[37m        [39;49;00m[34mpadding[39;49;00m:[37m [39;49;00m[34m5[39;49;00m[36mpx[39;49;00m;[37m[39;49;00m
    19	[37m        [39;49;00m[34mfont-size[39;49;00m:[37m [39;49;00m[34m140[39;49;00m[36m%[39;49;00m;[37m[39;49;00m
    20	[37m        [39;49;00m[34mbackground[39;49;00m:[37m [39;49;00m[34m#ddd[39;49;00m;[37m[39;49;00m
    21	[37m      [39;49;00m}[37m[39;49;00m
    22	[37m      [39;49;00m.[04m[32merror[39;49;00m[37m [39;49;00m{[37m [39;49;00m
    23	[37m        [39;49;00m[34mpadding[39;49;00m:[37m [39;49;00m[34m5[39;49;00m[36mpx[39;49;00m;[37m[39;49;00m
    24	[37m        [39;49;00m[34mpadding-top[39;49;00m:[37m [39;49;00m[34m15[39;49;00m[36mpx[39;49;00m;[37m[39;49;00m
    25	[37m        [39;49;00m[34mfont-size[39;49;00m:[37m [39;49;00m[34m140[39;49;00m[36m%[39;49;00m;[37m[39;49;00m
    26	[37m        [39;49;00m[34mcolor[39;49;00m:[37m [39;49;00m[34m#f00[39;49;00m;[37m[39;49;00m
    27	[37m      [39;49;00m}[37m[39;49;00m
    28	[37m      [39;49;00m.[04m[32mload[39;49;00m[37m [39;49;00m{[37m[39;49;00m
    29	[37m        [39;49;00m[34mpadding[39;49;00m:[37m [39;49;00m[34m5[39;49;00m[36mpx[39;49;00m;[37m[39;49;00m
    30	[37m        [39;49;00m[34mcolor[39;49;00m:[37m [39;49;00m[34m#555[39;49;00m;[37m[39;49;00m
    31	[37m      [39;49;00m}[37m[39;49;00m
    32	[37m      [39;49;00m.[04m[32msource[39;49;00m[37m [39;49;00m{[37m[39;49;00m
    33	[37m        [39;49;00m[34mborder[39;49;00m:[37m [39;49;00m[34m1[39;49;00m[36mpx[39;49;00m[37m [39;49;00m[34msolid[39;49;00m[37m [39;49;00m[34m#ccc[39;49;00m;[37m [39;49;00m
    34	[37m        [39;49;00m[34mpadding[39;49;00m:[37m [39;49;00m[34m10[39;49;00m[36mpx[39;49;00m;[37m[39;49;00m
    35	[37m        [39;49;00m[34mmargin-top[39;49;00m:[37m [39;49;00m[34m10[39;49;00m[36mpx[39;49;00m;[37m [39;49;00m[34mmargin-bottom[39;49;00m:[37m [39;49;00m[34m10[39;49;00m[36mpx[39;49;00m;[37m[39;49;00m
    36	[37m      [39;49;00m}[37m[39;49;00m
    37	[37m      [39;49;00m[94mh2[39;49;00m[37m [39;49;00m{[37m[39;49;00m
    38	[37m        [39;49;00m[34mpadding-left[39;49;00m:[37m [39;49;00m[34m5[39;49;00m[36mpx[39;49;00m;[37m[39;49;00m
    39	[37m        [39;49;00m[34mbackground[39;49;00m:[37m [39;49;00m[34m#eee[39;49;00m;[37m[39;49;00m
    40	[37m      [39;49;00m}[37m[39;49;00m
    41	[37m    [39;49;00m</[94mstyle[39;49;00m>
    42	  </[94mhead[39;49;00m>
    43	  <[94mbody[39;49;00m>
    44	    <[94mh1[39;49;00m>Error</[94mh1[39;49;00m>
    45
    46	[36m<?r [39;49;00m
    47	[36m    if Run.mode == :debug [39;49;00m
    48	[36m    require 'cgi'[39;49;00m
    49	[36m?>[39;49;00m
    50	    [36m<?r  for error, path in @context.rendering_errors ?>[39;49;00m
    51	      <[94mdiv[39;49;00m [36mclass[39;49;00m=[33m"path"[39;49;00m><[94mstrong[39;49;00m>Path:</[94mstrong[39;49;00m> #{path}</[94mdiv[39;49;00m>
    52	      <[94mdiv[39;49;00m [36mclass[39;49;00m=[33m"error"[39;49;00m><[94mstrong[39;49;00m>#{CGI.escapeHTML(error.to_s)}</[94mstrong[39;49;00m></[94mdiv[39;49;00m>
    53	      <[94mdiv[39;49;00m [36mclass[39;49;00m=[33m"load"[39;49;00m>
    54	        <[94mstrong[39;49;00m><[94ma[39;49;00m [36mhref[39;49;00m=[33m"#{request.uri}"[39;49;00m>Reload</[94ma[39;49;00m></[94mstrong[39;49;00m> this page.
    55	        Go to the <[94mstrong[39;49;00m><[94ma[39;49;00m [36mhref[39;49;00m=[33m"#{request.referer}"[39;49;00m>referer</[94ma[39;49;00m></[94mstrong[39;49;00m> or the <[94mstrong[39;49;00m><[94ma[39;49;00m [36mhref[39;49;00m=[33m"/"[39;49;00m>home page</[94ma[39;49;00m></[94mstrong[39;49;00m>.
    56	      </[94mdiv[39;49;00m>
    57	      <[94mdiv[39;49;00m [36mclass[39;49;00m=[33m"source"[39;49;00m>
    58	      [36m<?r [39;49;00m
    59	[36m        extract = error.source_extract.split("\n")[39;49;00m
    60	[36m      ?>[39;49;00m
    61	      In file <[94mb[39;49;00m>'#{error.hot_file}'</[94mb[39;49;00m> #{error.hot_file =~ /\.xhtml$/ ? '(line numbering is aproximate due to template transformation)' : nil}:
    62	      <[94mbr[39;49;00m /><[94mbr[39;49;00m />
    63	      [36m<?r[39;49;00m
    64	[36m        extract.each_with_index do |line, idx|[39;49;00m
    65	[36m          line = sanitize(line)[39;49;00m
    66	[36m          if 5 == idx[39;49;00m
    67	[36m      ?>[39;49;00m
    68	          <[94mdiv[39;49;00m [36mstyle[39;49;00m=[33m"background: #eee"[39;49;00m>#{line}</[94mdiv[39;49;00m>
    69	      [36m<?r  else ?>[39;49;00m
    70	          <[94mdiv[39;49;00m>#{line}</[94mdiv[39;49;00m>
    71	      [36m<?r  [39;49;00m
    72	[36m          end [39;49;00m
    73	[36m        end[39;49;00m
    74	[36m      ?>[39;49;00m
    75	      </[94mdiv[39;49;00m>
    76	      <[94mh2[39;49;00m><[94ma[39;49;00m [36mhref[39;49;00m=[33m"#"[39;49;00m [36monclick[39;49;00m=[33m"return toggleVisible(document.getElementById('trace'));"[39;49;00m>Stack Trace</[94ma[39;49;00m></[94mh2[39;49;00m>
    77	      <[94mdiv[39;49;00m [36mid[39;49;00m=[33m"trace"[39;49;00m [36mstyle[39;49;00m=[33m"display: none;"[39;49;00m>
    78	        [36m<?r error.backtrace.zip(error.source_for_backtrace).each_with_index do |step,step_idx| ?>[39;49;00m
    79	      <[94mdiv[39;49;00m><[94ma[39;49;00m [36mhref[39;49;00m=[33m"#"[39;49;00m [36monclick[39;49;00m=[33m"return toggleVisible(document.getElementById('trace_#{step_idx}'));"[39;49;00m>#{sanitize(step.first)}</[94ma[39;49;00m></[94mdiv[39;49;00m>
    80	      <[94mdiv[39;49;00m [36mclass[39;49;00m=[33m"source"[39;49;00m [36mid[39;49;00m=[33m"trace_#{step_idx}"[39;49;00m [36mstyle[39;49;00m=[33m"display: none;"[39;49;00m>
    81	      [36m<?r [39;49;00m
    82	[36m        extract = step.last.split("\n")      [39;49;00m
    83	[36m        extract.each_with_index do |line, idx|[39;49;00m
    84	[36m          line = sanitize(line)[39;49;00m
    85	[36m          if 5 == idx[39;49;00m
    86	[36m      ?>[39;49;00m
    87	          <[94mdiv[39;49;00m [36mstyle[39;49;00m=[33m"background: #eee"[39;49;00m>#{line}</[94mdiv[39;49;00m>
    88	      [36m<?r  else ?>[39;49;00m
    89	          <[94mdiv[39;49;00m>#{line}</[94mdiv[39;49;00m>
    90	      [36m<?r  [39;49;00m
    91	[36m          end [39;49;00m
    92	[36m        end[39;49;00m
    93	[36m      ?>[39;49;00m
    94	      </[94mdiv[39;49;00m>
    95
    96
    97	        [36m<?r end ?>[39;49;00m
    98	      </[94mdiv[39;49;00m>
    99	    [36m<?r end ?>[39;49;00m
   100
   101	    <[94mh2[39;49;00m><[94ma[39;49;00m [36mhref[39;49;00m=[33m"#"[39;49;00m [36monclick[39;49;00m=[33m"document.getElementById('request').style.display = 'block'; return false"[39;49;00m>Request</[94ma[39;49;00m></[94mh2[39;49;00m>
   102	    <[94mdiv[39;49;00m [36mid[39;49;00m=[33m"request"[39;49;00m [36mstyle[39;49;00m=[33m"display: none"[39;49;00m>
   103	      <[94mp[39;49;00m><[94mstrong[39;49;00m>Parameters:</[94mstrong[39;49;00m> #{request.params.reject{ |k,v| k == :__RELOADED__ }.inspect}</[94mp[39;49;00m>
   104	      <[94mp[39;49;00m><[94mstrong[39;49;00m>Cookies:</[94mstrong[39;49;00m> #{request.cookies.inspect}</[94mp[39;49;00m>
   105	      <[94mp[39;49;00m><[94mstrong[39;49;00m>Headers:</[94mstrong[39;49;00m><[94mbr[39;49;00m />#{request.headers.collect { |k, v| "#{k} => #{v}" }.join('<[94mbr[39;49;00m />')}</[94mp[39;49;00m>
   106	    </[94mdiv[39;49;00m>
   107
   108	    <[94mh2[39;49;00m><[94ma[39;49;00m [36mhref[39;49;00m=[33m"#"[39;49;00m [36monclick[39;49;00m=[33m"document.getElementById('response').style.display = 'block'; return false"[39;49;00m>Response</[94ma[39;49;00m></[94mh2[39;49;00m>
   109	    <[94mdiv[39;49;00m [36mid[39;49;00m=[33m"response"[39;49;00m [36mstyle[39;49;00m=[33m"display: none"[39;49;00m>
   110	      <[94mp[39;49;00m><[94mstrong[39;49;00m>Headers:</[94mstrong[39;49;00m> #{request.response_headers.inspect}</[94mp[39;49;00m>
   111	      <[94mp[39;49;00m><[94mstrong[39;49;00m>Cookies:</[94mstrong[39;49;00m> #{request.response_cookies.inspect}</[94mp[39;49;00m>
   112	    </[94mdiv[39;49;00m>
   113
   114	    <[94mh2[39;49;00m><[94ma[39;49;00m [36mhref[39;49;00m=[33m"#"[39;49;00m [36monclick[39;49;00m=[33m"document.getElementById('session').style.display = 'block'; return false"[39;49;00m>Session</[94ma[39;49;00m></[94mh2[39;49;00m>
   115	    <[94mdiv[39;49;00m [36mid[39;49;00m=[33m"session"[39;49;00m [36mstyle[39;49;00m=[33m"display: none"[39;49;00m>
   116	      <[94mp[39;49;00m><[94mstrong[39;49;00m>Values:</[94mstrong[39;49;00m> #{session.inspect}</[94mp[39;49;00m>
   117	    </[94mdiv[39;49;00m>
   118
   119	    <[94mbr[39;49;00m /><[94mbr[39;49;00m />
   120	    Powered by <[94ma[39;49;00m [36mhref[39;49;00m=[33m"http://www.nitrohq.com"[39;49;00m>Nitro</[94ma[39;49;00m> version #{Nitro::Version}
   121	[36m<?r end ?>[39;49;00m
   122	  </[94mbody[39;49;00m>
   123	</[94mhtml[39;49;00m>
   124	<[94mSystemPage[39;49;00m>
   125	  [36m<?r base = "#{@base}/%base%" ?>[39;49;00m
   126	  <[94mh1[39;49;00m><[94ma[39;49;00m [36mhref[39;49;00m=[33m"/"[39;49;00m> Home</[94ma[39;49;00m> > <[94ma[39;49;00m [36mhref[39;49;00m=[33m"#@base"[39;49;00m>System</[94ma[39;49;00m> > <[94ma[39;49;00m [36mhref[39;49;00m=[33m"#{base}/list"[39;49;00m>#{"%plural%".humanize}</[94ma[39;49;00m> > Edit #{"%name%".humanize} </[94mh1[39;49;00m>
   127	  [36m<?r if @all ?>[39;49;00m
   128	    <[94ma[39;49;00m [36mhref[39;49;00m=[33m"#{request.uri.gsub(/\/all$/, '')}"[39;49;00m>Show editable</[94ma[39;49;00m>
   129	    #{form_for @obj, :action => "#{base}/save", :cancel => "#{base}/list", :all => true}
   130	  [36m<?r else ?>[39;49;00m
   131	    <[94ma[39;49;00m [36mhref[39;49;00m=[33m"#{request.uri}/all"[39;49;00m>Show all</[94ma[39;49;00m>
   132	    #{form_for @obj, :action => "#{base}/save", :cancel => "#{base}/list"}
   133	  [36m<?r end ?>[39;49;00m
   134	</[94mSystemPage[39;49;00m>
   135	#{form_for(@%name%)}
   136	<[94mSystemPage[39;49;00m>
   137	  [36m<?r base = "#{@base}/%base%" ?>[39;49;00m
   138	  <[94mh1[39;49;00m>#{"%plural%".humanize}</[94mh1[39;49;00m>
   139	  <[94mh2[39;49;00m><[94ma[39;49;00m [36mhref[39;49;00m=[33m"#{base}/new"[39;49;00m>New #{"%name%".humanize}</[94ma[39;49;00m></[94mh2[39;49;00m>
   140	  <[94mform[39;49;00m [36maction[39;49;00m=[33m"search"[39;49;00m>
   141	    Search #{"%plural%".humanize}: <[94minput[39;49;00m [36mtype[39;49;00m=[33m"text"[39;49;00m [36mname[39;49;00m=[33m"q"[39;49;00m />&nbsp;<[94minput[39;49;00m [36mtype[39;49;00m=[33m"submit"[39;49;00m [36mvalue[39;49;00m=[33m"Search"[39;49;00m />
   142	  </[94mform[39;49;00m>
   143	  <[94mtable[39;49;00m>
   144	  [36m<?r for obj in @list ?>[39;49;00m
   145	    <[94mtr[39;49;00m>
   146	      <[94mtd[39;49;00m [36mwidth[39;49;00m=[33m"100%"[39;49;00m><[94ma[39;49;00m [36mhref[39;49;00m=[33m"#{base}/edit/#{obj.oid}"[39;49;00m>#{obj.to_s}</[94ma[39;49;00m></[94mtd[39;49;00m>
   147	      [36m<?r if obj.respond_to?(:update_time) ?>[39;49;00m
   148	        <[94mtd[39;49;00m [36mnowrap[39;49;00m=[33m"1"[39;49;00m>#{obj.update_time.stamp(:db)}</[94mtd[39;49;00m>
   149	      [36m<?r end ?>[39;49;00m
   150	      <[94mtd[39;49;00m><[94ma[39;49;00m [36mhref[39;49;00m=[33m"#{base}/edit/#{obj.oid}"[39;49;00m>edit</[94ma[39;49;00m></[94mtd[39;49;00m>
   151	      <[94mtd[39;49;00m><[94ma[39;49;00m [36mhref[39;49;00m=[33m"#{base}/delete/#{obj.oid}"[39;49;00m>del</[94ma[39;49;00m></[94mtd[39;49;00m>
   152	    </[94mtr[39;49;00m>
   153	  [36m<?r end ?>[39;49;00m
   154	  </[94mtable[39;49;00m>
   155	</[94mSystemPage[39;49;00m>
   156	<[94mSystemPage[39;49;00m>
   157	  [36m<?r base = "#{@base}/%base%" ?>[39;49;00m
   158	  <[94mh1[39;49;00m><[94ma[39;49;00m [36mhref[39;49;00m=[33m"/"[39;49;00m> Home</[94ma[39;49;00m> > <[94ma[39;49;00m [36mhref[39;49;00m=[33m"#@base"[39;49;00m>System</[94ma[39;49;00m> > #{"%plural%".humanize}</[94mh1[39;49;00m>
   159	  <[94ma[39;49;00m [36mhref[39;49;00m=[33m"#{base}/new"[39;49;00m>New #{"%name%".humanize}</[94ma[39;49;00m>
   160	  <[94mp[39;49;00m>
   161	  <[94mform[39;49;00m [36maction[39;49;00m=[33m"#{base}/search"[39;49;00m>
   162	    Search #{"%plural%".humanize}: <[94minput[39;49;00m [36mtype[39;49;00m=[33m"text"[39;49;00m [36mname[39;49;00m=[33m"q"[39;49;00m />&nbsp;<[94minput[39;49;00m [36mtype[39;49;00m=[33m"submit"[39;49;00m [36mvalue[39;49;00m=[33m"Search"[39;49;00m />
   163	  </[94mform[39;49;00m>
   164	  </[94mp[39;49;00m>
   165	  <[94mtable[39;49;00m>
   166	  [36m<?r for obj in @list ?>[39;49;00m
   167	    <[94mtr[39;49;00m>
   168	      <[94mtd[39;49;00m [36mwidth[39;49;00m=[33m"100%"[39;49;00m><[94ma[39;49;00m [36mhref[39;49;00m=[33m"#{base}/edit/#{obj.oid}"[39;49;00m>#(obj.to_s)</[94ma[39;49;00m></[94mtd[39;49;00m>
   169	      [36m<?r if obj.respond_to?(:update_time) ?>[39;49;00m
   170	        <[94mtd[39;49;00m [36mnowrap[39;49;00m=[33m"1"[39;49;00m>#{obj.update_time.stamp(:db)}</[94mtd[39;49;00m>
   171	      [36m<?r end ?>[39;49;00m
   172	      <[94mtd[39;49;00m><[94ma[39;49;00m [36mhref[39;49;00m=[33m"#{base}/edit/#{obj.oid}"[39;49;00m>edit</[94ma[39;49;00m></[94mtd[39;49;00m>
   173	      <[94mtd[39;49;00m><[94ma[39;49;00m [36mhref[39;49;00m=[33m"#{base}/delete/#{obj.oid}"[39;49;00m [36monclick[39;49;00m=[33m"confirm('Are you sure?')"[39;49;00m>del</[94ma[39;49;00m></[94mtd[39;49;00m>
   174	    </[94mtr[39;49;00m>
   175	  [36m<?r end ?>[39;49;00m
   176	  </[94mtable[39;49;00m>
   177	  <[94mdiv[39;49;00m [36mclass[39;49;00m=[33m"pager"[39;49;00m [36mif[39;49;00m=[33m"@pager and @pager.navigation?"[39;49;00m>
   178	    #{@pager.navigation}
   179	  </[94mdiv[39;49;00m>
   180	</[94mSystemPage[39;49;00m>
   181	<[94mSystemPage[39;49;00m>
   182	  [36m<?r base = "#{@base}/%base%" ?>[39;49;00m
   183	  <[94mh1[39;49;00m><[94ma[39;49;00m [36mhref[39;49;00m=[33m"/"[39;49;00m> Home</[94ma[39;49;00m> > <[94ma[39;49;00m [36mhref[39;49;00m=[33m"#@base"[39;49;00m>System</[94ma[39;49;00m> > <[94ma[39;49;00m [36mhref[39;49;00m=[33m"#{base}/list"[39;49;00m>#{"%plural%".humanize}</[94ma[39;49;00m> > New #{"%name%".humanize}</[94mh1[39;49;00m>
   184	  [36m<?r if @all ?>[39;49;00m
   185	    <[94ma[39;49;00m [36mhref[39;49;00m=[33m"#{request.uri.gsub(/\/all$/, '')}"[39;49;00m>Show editable</[94ma[39;49;00m>
   186	    #{form_for @obj, :action => "#{base}/save", :cancel => "#{base}/list", :all => true, :enctype => "multipart/form-data"}
   187	  [36m<?r else ?>[39;49;00m
   188	    <[94ma[39;49;00m [36mhref[39;49;00m=[33m"#{request.uri}/all"[39;49;00m>Show all</[94ma[39;49;00m>
   189	    #{form_for @obj, :action => "#{base}/save", :cancel => "#{base}/list", :enctype => "multipart/form-data"}
   190	  [36m<?r end ?>[39;49;00m
   191	</[94mSystemPage[39;49;00m>
   192	<[94mSystemPage[39;49;00m>
   193	  [36m<?r base = "#{@base}/%base%" ?>[39;49;00m
   194	  <[94mh1[39;49;00m><[94ma[39;49;00m [36mhref[39;49;00m=[33m"/"[39;49;00m> Home</[94ma[39;49;00m> > <[94ma[39;49;00m [36mhref[39;49;00m=[33m"#@base"[39;49;00m>System</[94ma[39;49;00m> > <[94ma[39;49;00m [36mhref[39;49;00m=[33m"#{base}/list"[39;49;00m>#{"%plural%".humanize}</[94ma[39;49;00m> > Search for '#@query'</[94mh1[39;49;00m>
   195	  <[94mp[39;49;00m>
   196	  <[94mform[39;49;00m [36maction[39;49;00m=[33m"#{base}/search"[39;49;00m>
   197	    Search #{"%plural%".humanize}: <[94minput[39;49;00m [36mtype[39;49;00m=[33m"text"[39;49;00m [36mname[39;49;00m=[33m"q"[39;49;00m />&nbsp;<[94minput[39;49;00m [36mtype[39;49;00m=[33m"submit"[39;49;00m [36mvalue[39;49;00m=[33m"Search"[39;49;00m />
   198	  </[94mform[39;49;00m>
   199	  </[94mp[39;49;00m>
   200	  [36m<?r if @list.nil? ?>[39;49;00m
   201	    <[94mp[39;49;00m>Search method is not implemented for this object</[94mp[39;49;00m>
   202	  [36m<?r else ?>[39;49;00m
   203	    <[94mtable[39;49;00m>
   204	    [36m<?r for obj in @list ?>[39;49;00m
   205	      <[94mtr[39;49;00m>
   206	        <[94mtd[39;49;00m [36mwidth[39;49;00m=[33m"100%"[39;49;00m><[94ma[39;49;00m [36mhref[39;49;00m=[33m"#{base}/edit/#{obj.oid}"[39;49;00m>#(obj.to_s)</[94ma[39;49;00m></[94mtd[39;49;00m>
   207	        [36m<?r if obj.respond_to?(:update_time) ?>[39;49;00m
   208	          <[94mtd[39;49;00m [36mnowrap[39;49;00m=[33m"1"[39;49;00m>#{obj.update_time.stamp(:db)}</[94mtd[39;49;00m>
   209	        [36m<?r end ?>[39;49;00m
   210	        <[94mtd[39;49;00m><[94ma[39;49;00m [36mhref[39;49;00m=[33m"#{base}/edit/#{obj.oid}"[39;49;00m>edit</[94ma[39;49;00m></[94mtd[39;49;00m>
   211	        <[94mtd[39;49;00m><[94ma[39;49;00m [36mhref[39;49;00m=[33m"#{base}/delete/#{obj.oid}"[39;49;00m>del</[94ma[39;49;00m></[94mtd[39;49;00m>
   212	      </[94mtr[39;49;00m>
   213	    [36m<?r end ?>[39;49;00m
   214	    </[94mtable[39;49;00m>
   215	    <[94mdiv[39;49;00m [36mclass[39;49;00m=[33m"pager"[39;49;00m [36mif[39;49;00m=[33m"@pager and @pager.navigation?"[39;49;00m>
   216	      #{@pager.navigation}
   217	    </[94mdiv[39;49;00m>
   218	  [36m<?r end ?>[39;49;00m
   219	</[94mSystemPage[39;49;00m>
   220	<[94mSystemPage[39;49;00m>
   221	  [36m<?r base = "#{@base}/%base%" ?>[39;49;00m
   222	  <[94mh1[39;49;00m>View %name%</[94mh1[39;49;00m>
   223	  <[94mh2[39;49;00m><[94ma[39;49;00m [36mhref[39;49;00m=[33m"#{base}/list"[39;49;00m>List of %plural%</[94ma[39;49;00m></[94mh2[39;49;00m>
   224	  <[94mcode[39;49;00m>
   225	    #{@obj.to_yaml}
   226	  </[94mcode[39;49;00m>
   227	</[94mSystemPage[39;49;00m>
   228	<[94mstrong[39;49;00m>Access denied</[94mstrong[39;49;00m>
   229	<[94mSystemPage[39;49;00m>
   230	  [36m<?r base = "#{@base}/%base%" ?>[39;49;00m
   231	  <[94mh1[39;49;00m><[94ma[39;49;00m [36mhref[39;49;00m=[33m'/'[39;49;00m>Home</[94ma[39;49;00m> > System</[94mh1[39;49;00m>
   232
   233	  <[94mh2[39;49;00m>Og managed classes</[94mh2[39;49;00m>
   234
   235	  <[94mtable[39;49;00m>
   236	    <[94mtr[39;49;00m>
   237	      <[94mth[39;49;00m>Class</[94mth[39;49;00m>
   238	      <[94mth[39;49;00m>Count</[94mth[39;49;00m>
   239	      <[94mth[39;49;00m [36mcolspan[39;49;00m=[33m"2"[39;49;00m>Cleanup</[94mth[39;49;00m>
   240	      <[94mth[39;49;00m>Properties</[94mth[39;49;00m>
   241	    </[94mtr[39;49;00m>
   242	  [36m<?r for c in @classes ?>[39;49;00m
   243	    <[94mtr[39;49;00m>
   244	      <[94mtd[39;49;00m><[94ma[39;49;00m [36mhref[39;49;00m=[33m"#@base/#{Scaffolding.class_to_path(c).plural}/list"[39;49;00m>#{c.name}</[94ma[39;49;00m></[94mtd[39;49;00m>
   245	      <[94mtd[39;49;00m>#{c.count}</[94mtd[39;49;00m>
   246	      <[94mtd[39;49;00m><[94ma[39;49;00m [36mhref[39;49;00m=[33m"delete_all/#{c.name}"[39;49;00m [36monclick[39;49;00m=[33m"return confirm('Delete all instances?')"[39;49;00m>delete</[94ma[39;49;00m></[94mtd[39;49;00m>
   247	      <[94mtd[39;49;00m><[94ma[39;49;00m [36mhref[39;49;00m=[33m"destroy/#{c.name}"[39;49;00m [36monclick[39;49;00m=[33m"return confirm('Drop the schema?')"[39;49;00m>destroy</[94ma[39;49;00m></[94mtd[39;49;00m>
   248	      <[94mtd[39;49;00m [36mwidth[39;49;00m=[33m"100%"[39;49;00m>#{c.properties.values.join(', ')}</[94mtd[39;49;00m>
   249	    </[94mtr[39;49;00m>
   250	  [36m<?r end ?>[39;49;00m
   251	  </[94mtable[39;49;00m>
   252
   253	  <[94mh2[39;49;00m>System configuration</[94mh2[39;49;00m>
   254
   255	  <[94mtable[39;49;00m [36mwidth[39;49;00m=[33m"100%"[39;49;00m>
   256	    <[94mtr[39;49;00m>
   257	      <[94mth[39;49;00m>Name</[94mth[39;49;00m>
   258	      <[94mth[39;49;00m>Value</[94mth[39;49;00m>
   259	      <[94mth[39;49;00m>Type</[94mth[39;49;00m>
   260	      <[94mth[39;49;00m>Description</[94mth[39;49;00m>
   261	    </[94mtr[39;49;00m>
   262	  [36m<?r for s in @settings ?>[39;49;00m
   263	    <[94mtr[39;49;00m>
   264	      <[94mtd[39;49;00m>#{s.owner}.<[94mstrong[39;49;00m>#{s.name}</[94mstrong[39;49;00m></[94mtd[39;49;00m>
   265	      <[94mtd[39;49;00m>#{s.value.inspect}</[94mtd[39;49;00m>
   266	      <[94mtd[39;49;00m>#{s.type}</[94mtd[39;49;00m>
   267	      <[94mtd[39;49;00m>#{s.options[:doc]}</[94mtd[39;49;00m>
   268	    </[94mtr[39;49;00m>
   269	  [36m<?r end ?>[39;49;00m
   270	  </[94mtable[39;49;00m>
   271	</[94mSystemPage[39;49;00m>
   272
   273	<[94mb[39;49;00m>[36m<?r $include1 = true ?>[39;49;00m</[94mb[39;49;00m>
   274	<[94mb[39;49;00m>[36m<?r $include2 = true ?>[39;49;00m</[94mb[39;49;00m>
   275	<[94mhtml[39;49;00m>
   276	  <[94mb[39;49;00m>Test</[94mb[39;49;00m>
   277
   278	[36m<?r @tflag = true ?>[39;49;00m
   279
   280	<[94mrender[39;49;00m [36mhref[39;49;00m=[33m"blog/inc1"[39;49;00m />
   281	<[94mrender[39;49;00m [36mhref[39;49;00m=[33m'blog/inc2'[39;49;00m />
   282
   283	</[94mhtml[39;49;00m>
   284	<[94mhtml[39;49;00m>hello</[94mhtml[39;49;00m>
   285	Hello #{username}
   286
   287	how do you feel?
   288
   289	Here is your <[94mb[39;49;00m>Token</[94mb[39;49;00m>: #{token}
   290	<[94mPage[39;49;00m [36mtitle[39;49;00m=[33m"Questions and Tips by Tags"[39;49;00m>
   291	  <[94mdiv[39;49;00m [36mid[39;49;00m=[33m"left"[39;49;00m>
   292	    [36m<?r if @tags ?>[39;49;00m
   293	    <[94mh1[39;49;00m>Questions with Tags: #{@tags.join(" ")}</[94mh1[39;49;00m>
   294
   295	    [36m<?r if @questions && @questions.size > 0 ?>[39;49;00m
   296	      [36m<?r if @qtags ?>[39;49;00m
   297	        Too many results for that Tag, please reduce the number by using one of the following Tags:
   298	        #{cloud_of(@qtags)}
   299	      [36m<?r end ?>[39;49;00m
   300	    <[94mdiv[39;49;00m [36mclass[39;49;00m=[33m"results"[39;49;00m>
   301	      [36m<?r @questions.each do |q| ?>[39;49;00m
   302	        <[94mh2[39;49;00m><[94ma[39;49;00m [36mhref[39;49;00m=[33m"/question/#{q.oid}"[39;49;00m>#{q.question}</[94ma[39;49;00m></[94mh2[39;49;00m>
   303	        <[94mp[39;49;00m>
   304	          [36m<?r excerpt = excerpt_with_words(q.text, @tags) ?>[39;49;00m
   305	          #{excerpt}
   306	        </[94mp[39;49;00m>
   307	        <[94mp[39;49;00m [36mstyle[39;49;00m=[33m"float:right;"[39;49;00m>#{q.answers.size.to_i} answers</[94mp[39;49;00m>
   308	      [36m<?r end ?>[39;49;00m
   309	    </[94mdiv[39;49;00m>
   310	    <[94mdiv[39;49;00m [36mclass[39;49;00m=[33m"pager"[39;49;00m>
   311	      #{@qpager.navigation}
   312	    </[94mdiv[39;49;00m>
   313	    [36m<?r else ?>[39;49;00m
   314	    <[94mdiv[39;49;00m [36mclass[39;49;00m=[33m"results_none"[39;49;00m>
   315	      <[94mh2[39;49;00m>no question with this/these tag(s) found</[94mh2[39;49;00m>
   316	      <[94mp[39;49;00m><[94ma[39;49;00m [36mhref[39;49;00m=[33m"/ask"[39;49;00m>Ask a question here.</[94ma[39;49;00m></[94mp[39;49;00m>
   317	    </[94mdiv[39;49;00m>
   318	    [36m<?r end ?>[39;49;00m
   319
   320	    [36m<?r if @tips && @tips.size > 0 ?>[39;49;00m
   321	    <[94mh1[39;49;00m>Tips with Tags: #{@tags.join(" ")}</[94mh1[39;49;00m>
   322	    [36m<?r if @ttags ?>[39;49;00m
   323	      Too many results for that Tag, please reduce the number by using one of the following Tags:
   324	      #{cloud_of(@ttags)}
   325	    [36m<?r end ?>[39;49;00m
   326	    <[94mdiv[39;49;00m [36mclass[39;49;00m=[33m"results"[39;49;00m>
   327	      [36m<?r @tips.each do |t| ?>[39;49;00m
   328	        <[94mh2[39;49;00m><[94ma[39;49;00m [36mhref[39;49;00m=[33m"/tip/#{t.oid}"[39;49;00m>#{t.title}</[94ma[39;49;00m></[94mh2[39;49;00m>
   329	        <[94mp[39;49;00m>
   330	          [36m<?r excerpt = excerpt_with_words(t.text, @tags) ?>[39;49;00m
   331	          #{excerpt}
   332	        </[94mp[39;49;00m>
   333	      [36m<?r end ?>[39;49;00m
   334	    </[94mdiv[39;49;00m>
   335	    <[94mdiv[39;49;00m [36mclass[39;49;00m=[33m"pager"[39;49;00m>
   336	      #{@tpager.navigation}
   337	    </[94mdiv[39;49;00m>
   338	    [36m<?r end ?>[39;49;00m
   339
   340	    [36m<?r if @tutorials && @tutorials.size > 0 ?>[39;49;00m
   341	    <[94mh1[39;49;00m>Tutorials with Tags: #{@tags.join(" ")}</[94mh1[39;49;00m>
   342	    [36m<?r if @tuttags ?>[39;49;00m
   343	      Too many results for that Tag, please reduce the number by using one of the following Tags:
   344	      #{cloud_of(@tuttags)}
   345	    [36m<?r end ?>[39;49;00m
   346	    <[94mdiv[39;49;00m [36mclass[39;49;00m=[33m"results"[39;49;00m>
   347	      [36m<?r @tutorials.each do |t| ?>[39;49;00m
   348	        <[94mh2[39;49;00m><[94ma[39;49;00m [36mhref[39;49;00m=[33m"/tutorial/#{t.oid}"[39;49;00m>#{t.title}</[94ma[39;49;00m></[94mh2[39;49;00m>
   349	        <[94mp[39;49;00m>
   350	          [36m<?r excerpt = excerpt_with_words(t.text, @tags) ?>[39;49;00m
   351	          #{excerpt}
   352	        </[94mp[39;49;00m>
   353	      [36m<?r end ?>[39;49;00m
   354	    </[94mdiv[39;49;00m>
   355	    <[94mdiv[39;49;00m [36mclass[39;49;00m=[33m"pager"[39;49;00m>
   356	      #{@tpager.navigation}
   357	    </[94mdiv[39;49;00m>
   358	    [36m<?r end ?>[39;49;00m
   359
   360
   361	    [36m<?r else ?>[39;49;00m
   362	      <[94mdiv[39;49;00m [36mclass[39;49;00m=[33m"cloud"[39;49;00m>
   363	        [36m<?r[39;49;00m
   364	[36m          sum = all_tags.inject(0) { |sum, t| sum + t.popularity.to_i }[39;49;00m
   365	[36m        ?>[39;49;00m
   366	        [36m<?r all_tags.each do |t| ?>[39;49;00m
   367	          <[94ma[39;49;00m [36mhref[39;49;00m=[33m"/tags/#{t.name}"[39;49;00m [36mstyle[39;49;00m=[33m"font-size:#{(1+((t.popularity.to_i/sum.to_f)*2)).to_s[0..3]}em;"[39;49;00m>#{t.name}</[94ma[39;49;00m>
   368	        [36m<?r end ?>[39;49;00m
   369	      </[94mdiv[39;49;00m> [37m<!-- #cloud -->[39;49;00m
   370	    [36m<?r end ?>[39;49;00m
   371	  </[94mdiv[39;49;00m> [37m<!-- #left -->[39;49;00m
   372
   373	  <[94mrender[39;49;00m [36mhref[39;49;00m=[33m"/right"[39;49;00m />
   374	</[94mPage[39;49;00m>
   375
   376	[37m<!-- Copyright © 2006 Kashia Buch (kashia@vfemail.net), Fabian Buch (fabian@fabian-buch.de). All rights reserved. -->[39;49;00m

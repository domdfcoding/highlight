     1	[34mimport[39;49;00m glib2, gtk2, gdk2, gtksourceview, dialogs, os, pango, osproc, strutils$
     2	[34mimport[39;49;00m pegs, streams$
     3	[34mimport[39;49;00m settings, types, cfg, search$
     4	$
     5	{.push callConv:cdecl.}$
     6	$
     7	[34mconst[39;49;00m$
     8	  NimrodProjectExt = [33m"[39;49;00m[33m.nimprj[39;49;00m[33m"[39;49;00m$
     9	$
    10	[34mvar[39;49;00m win: types.MainWin$
    11	win.Tabs = @[]$
    12	$
    13	search.win = [34maddr[39;49;00m(win)$
    14	$
    15	[34mvar[39;49;00m lastSession: [36mseq[39;49;00m[[36mstring[39;49;00m] = @[]$
    16	$
    17	[34mvar[39;49;00m confParseFail = [34mFalse[39;49;00m [37m# This gets set to true[39;49;00m$
    18	                          [37m# When there is an error parsing the config[39;49;00m$
    19	$
    20	[37m# Load the settings[39;49;00m$
    21	[34mtry[39;49;00m:$
    22	  win.settings = cfg.load(lastSession)$
    23	[34mexcept[39;49;00m ECFGParse:$
    24	  [37m# TODO: Make the dialog show the exception[39;49;00m$
    25	  confParseFail = [34mTrue[39;49;00m$
    26	  win.settings = cfg.defaultSettings()$
    27	[34mexcept[39;49;00m EIO:$
    28	  win.settings = cfg.defaultSettings()$
    29	$
    30	[34mproc [39;49;00m[32mgetProjectTab[39;49;00m(): [36mint[39;49;00m = $
    31	  [34mfor[39;49;00m i [35min[39;49;00m [34m0[39;49;00m..high(win.tabs): $
    32	    [34mif[39;49;00m win.tabs[i].filename.endswith(NimrodProjectExt): [34mreturn[39;49;00m i$
    33	$
    34	[34mproc [39;49;00m[32msaveTab[39;49;00m(tabNr: [36mint[39;49;00m, startpath: [36mstring[39;49;00m) =$
    35	  [34mif[39;49;00m tabNr < [34m0[39;49;00m: [34mreturn[39;49;00m$
    36	  [34mif[39;49;00m win.Tabs[tabNr].saved: [34mreturn[39;49;00m$
    37	  [34mvar[39;49;00m path = [33m"[39;49;00m[33m"[39;49;00m$
    38	  [34mif[39;49;00m win.Tabs[tabNr].filename == [33m"[39;49;00m[33m"[39;49;00m:$
    39	    path = ChooseFileToSave(win.w, startpath) $
    40	    [37m# dialogs.nim STOCK_OPEN instead of STOCK_SAVE[39;49;00m$
    41	  [34melse[39;49;00m: $
    42	    path = win.Tabs[tabNr].filename$
    43	  $
    44	  [34mif[39;49;00m path != [33m"[39;49;00m[33m"[39;49;00m:$
    45	    [34mvar[39;49;00m buffer = PTextBuffer(win.Tabs[tabNr].buffer)$
    46	    [37m# Get the text from the TextView[39;49;00m$
    47	    [34mvar[39;49;00m startIter: TTextIter$
    48	    buffer.getStartIter([34maddr[39;49;00m(startIter))$
    49	    $
    50	    [34mvar[39;49;00m endIter: TTextIter$
    51	    buffer.getEndIter([34maddr[39;49;00m(endIter))$
    52	    $
    53	    [34mvar[39;49;00m text = buffer.getText([34maddr[39;49;00m(startIter), [34maddr[39;49;00m(endIter), [34mFalse[39;49;00m)$
    54	    [37m# Save it to a file[39;49;00m$
    55	    [34mvar[39;49;00m f: TFile$
    56	    [34mif[39;49;00m open(f, path, fmWrite):$
    57	      f.write(text)$
    58	      f.close()$
    59	      $
    60	      win.tempStuff.lastSaveDir = splitFile(path).dir$
    61	      $
    62	      [37m# Change the tab name and .Tabs.filename etc.[39;49;00m$
    63	      win.Tabs[tabNr].filename = path$
    64	      win.Tabs[tabNr].saved = [34mTrue[39;49;00m$
    65	      [34mvar[39;49;00m name = extractFilename(path)$
    66	      $
    67	      [34mvar[39;49;00m cTab = win.Tabs[tabNr]$
    68	      cTab.label.setText(name)$
    69	    [34melse[39;49;00m:$
    70	      error(win.w, [33m"[39;49;00m[33mUnable to write to file[39;49;00m[33m"[39;49;00m)  $
    71	$
    72	[34mproc [39;49;00m[32msaveAllTabs[39;49;00m() =$
    73	  [34mfor[39;49;00m i [35min[39;49;00m [34m0[39;49;00m..high(win.tabs): $
    74	    saveTab(i, os.splitFile(win.tabs[i].filename).dir)$
    75	$
    76	[37m# GTK Events[39;49;00m$
    77	[37m# -- w(PWindow)[39;49;00m$
    78	[34mproc [39;49;00m[32mdestroy[39;49;00m(widget: PWidget, data: pgpointer) {.cdecl.} =$
    79	  [37m# gather some settings[39;49;00m$
    80	  win.settings.VPanedPos = PPaned(win.sourceViewTabs.getParent()).getPosition()$
    81	  win.settings.winWidth = win.w.allocation.width$
    82	  win.settings.winHeight = win.w.allocation.height$
    83	$
    84	  [37m# save the settings[39;49;00m$
    85	  win.save()$
    86	  [37m# then quit[39;49;00m$
    87	  main_quit()$
    88	$
    89	[34mproc [39;49;00m[32mdelete_event[39;49;00m(widget: PWidget, event: PEvent, user_data: pgpointer): [36mbool[39;49;00m =$
    90	  [34mvar[39;49;00m quit = [34mTrue[39;49;00m$
    91	  [34mfor[39;49;00m i [35min[39;49;00m low(win.Tabs)..len(win.Tabs)-[34m1[39;49;00m:$
    92	    [34mif[39;49;00m [35mnot[39;49;00m win.Tabs[i].saved:$
    93	      [34mvar[39;49;00m askSave = dialogNewWithButtons([33m"[39;49;00m[33m"[39;49;00m, win.w, [34m0[39;49;00m,$
    94	                            STOCK_SAVE, RESPONSE_ACCEPT, STOCK_CANCEL, $
    95	                            RESPONSE_CANCEL,$
    96	                            [33m"[39;49;00m[33mClose without saving[39;49;00m[33m"[39;49;00m, RESPONSE_REJECT, [34mnil[39;49;00m)$
    97	      askSave.setTransientFor(win.w)$
    98	      [37m# TODO: Make this dialog look better[39;49;00m$
    99	      [34mvar[39;49;00m label = labelNew(win.Tabs[i].filename & $
   100	          [33m"[39;49;00m[33m is unsaved, would you like to save it ?[39;49;00m[33m"[39;49;00m)$
   101	      PBox(askSave.vbox).pack_start(label, [34mFalse[39;49;00m, [34mFalse[39;49;00m, [34m0[39;49;00m)$
   102	      label.show()$
   103	$
   104	      [34mvar[39;49;00m resp = askSave.run()$
   105	      gtk2.destroy(PWidget(askSave))$
   106	      [34mcase[39;49;00m resp$
   107	      [34mof[39;49;00m RESPONSE_ACCEPT:$
   108	        saveTab(i, os.splitFile(win.tabs[i].filename).dir)$
   109	        quit = [34mTrue[39;49;00m$
   110	      [34mof[39;49;00m RESPONSE_CANCEL:$
   111	        quit = [34mFalse[39;49;00m$
   112	        [34mbreak[39;49;00m$
   113	      [34mof[39;49;00m RESPONSE_REJECT:$
   114	        quit = [34mTrue[39;49;00m$
   115	      [34melse[39;49;00m:$
   116	        quit = [34mFalse[39;49;00m$
   117	        [34mbreak[39;49;00m$
   118	$
   119	  [37m# If False is returned the window will close[39;49;00m$
   120	  [34mreturn[39;49;00m [35mnot[39;49;00m quit$
   121	$
   122	[34mproc [39;49;00m[32mwindowState_Changed[39;49;00m(widget: PWidget, event: PEventWindowState, $
   123	                         user_data: pgpointer) =$
   124	  win.settings.winMaximized = (event.newWindowState [35mand[39;49;00m $
   125	                               WINDOW_STATE_MAXIMIZED) != [34m0[39;49;00m$
   126	$
   127	[37m# -- SourceView(PSourceView) & SourceBuffer[39;49;00m$
   128	[34mproc [39;49;00m[32mupdateStatusBar[39;49;00m(buffer: PTextBuffer){.cdecl.} =$
   129	  [37m# Incase this event gets fired before[39;49;00m$
   130	  [37m# bottomBar is initialized[39;49;00m$
   131	  [34mif[39;49;00m win.bottomBar != [34mnil[39;49;00m [35mand[39;49;00m [35mnot[39;49;00m win.tempStuff.stopSBUpdates:  $
   132	    [34mvar[39;49;00m iter: TTextIter$
   133	    $
   134	    win.bottomBar.pop([34m0[39;49;00m)$
   135	    buffer.getIterAtMark([34maddr[39;49;00m(iter), buffer.getInsert())$
   136	    [34mvar[39;49;00m row = getLine([34maddr[39;49;00m(iter)) + [34m1[39;49;00m$
   137	    [34mvar[39;49;00m col = getLineOffset([34maddr[39;49;00m(iter))$
   138	    [34mdiscard[39;49;00m win.bottomBar.push([34m0[39;49;00m, [33m"[39;49;00m[33mLine: [39;49;00m[33m"[39;49;00m & $row & [33m"[39;49;00m[33m Column: [39;49;00m[33m"[39;49;00m & $col)$
   139	  $
   140	[34mproc [39;49;00m[32mcursorMoved[39;49;00m(buffer: PTextBuffer, location: PTextIter, $
   141	                 mark: PTextMark, user_data: pgpointer){.cdecl.} =$
   142	  updateStatusBar(buffer)$
   143	$
   144	[34mproc [39;49;00m[32monCloseTab[39;49;00m(btn: PButton, user_data: PWidget) =$
   145	  [34mif[39;49;00m win.sourceViewTabs.getNPages() > [34m1[39;49;00m:$
   146	    [34mvar[39;49;00m tab = win.sourceViewTabs.pageNum(user_data)$
   147	    win.sourceViewTabs.removePage(tab)$
   148	$
   149	    win.Tabs.delete(tab)$
   150	$
   151	[34mproc [39;49;00m[32monSwitchTab[39;49;00m(notebook: PNotebook, page: PNotebookPage, pageNum: guint, $
   152	                 user_data: pgpointer) =$
   153	  [34mif[39;49;00m win.Tabs.len()-[34m1[39;49;00m >= pageNum:$
   154	    win.w.setTitle([33m"[39;49;00m[33mAporia IDE - [39;49;00m[33m"[39;49;00m & win.Tabs[pageNum].filename)$
   155	$
   156	[34mproc [39;49;00m[32mcreateTabLabel[39;49;00m(name: [36mstring[39;49;00m, t_child: PWidget): [34mtuple[39;49;00m[box: PWidget,$
   157	                    label: PLabel] =$
   158	  [34mvar[39;49;00m box = hboxNew([34mFalse[39;49;00m, [34m0[39;49;00m)$
   159	  [34mvar[39;49;00m label = labelNew(name)$
   160	  [34mvar[39;49;00m closebtn = buttonNew()$
   161	  closeBtn.setLabel([34mnil[39;49;00m)$
   162	  [34mvar[39;49;00m iconSize = iconSizeFromName([33m"[39;49;00m[33mtabIconSize[39;49;00m[33m"[39;49;00m)$
   163	  [34mif[39;49;00m iconSize == [34m0[39;49;00m:$
   164	     iconSize = iconSizeRegister([33m"[39;49;00m[33mtabIconSize[39;49;00m[33m"[39;49;00m, [34m10[39;49;00m, [34m10[39;49;00m)$
   165	  [34mvar[39;49;00m image = imageNewFromStock(STOCK_CLOSE, iconSize)$
   166	  [34mdiscard[39;49;00m gSignalConnect(closebtn, [33m"[39;49;00m[33mclicked[39;49;00m[33m"[39;49;00m, G_Callback(onCloseTab), t_child)$
   167	  closebtn.setImage(image)$
   168	  gtk2.setRelief(closebtn, RELIEF_NONE)$
   169	  box.packStart(label, [34mTrue[39;49;00m, [34mTrue[39;49;00m, [34m0[39;49;00m)$
   170	  box.packEnd(closebtn, [34mFalse[39;49;00m, [34mFalse[39;49;00m, [34m0[39;49;00m)$
   171	  box.showAll()$
   172	  [34mreturn[39;49;00m (box, label)$
   173	$
   174	[34mproc [39;49;00m[32mchanged[39;49;00m(buffer: PTextBuffer, user_data: pgpointer) =$
   175	  [37m# Update the 'Line & Column'[39;49;00m$
   176	  [37m#updateStatusBar(buffer)[39;49;00m$
   177	$
   178	  [37m# Change the tabs state to 'unsaved'[39;49;00m$
   179	  [37m# and add '*' to the Tab Name[39;49;00m$
   180	  [34mvar[39;49;00m current = win.SourceViewTabs.getCurrentPage()$
   181	  [34mvar[39;49;00m name = [33m"[39;49;00m[33m"[39;49;00m$
   182	  [34mif[39;49;00m win.Tabs[current].filename == [33m"[39;49;00m[33m"[39;49;00m:$
   183	    win.Tabs[current].saved = [34mFalse[39;49;00m$
   184	    name = [33m"[39;49;00m[33mUntitled *[39;49;00m[33m"[39;49;00m$
   185	  [34melse[39;49;00m:$
   186	    win.Tabs[current].saved = [34mFalse[39;49;00m$
   187	    name = extractFilename(win.Tabs[current].filename) & [33m"[39;49;00m[33m *[39;49;00m[33m"[39;49;00m$
   188	  $
   189	  [34mvar[39;49;00m cTab = win.Tabs[current]$
   190	  cTab.label.setText(name)$
   191	$
   192	[37m# Other(Helper) functions[39;49;00m$
   193	$
   194	[34mproc [39;49;00m[32minitSourceView[39;49;00m(SourceView: [34mvar[39;49;00m PWidget, scrollWindow: [34mvar[39;49;00m PScrolledWindow,$
   195	                    buffer: [34mvar[39;49;00m PSourceBuffer) =$
   196	  [37m# This gets called by addTab[39;49;00m$
   197	  [37m# Each tabs creates a new SourceView[39;49;00m$
   198	  [37m# SourceScrolledWindow(ScrolledWindow)[39;49;00m$
   199	  scrollWindow = scrolledWindowNew([34mnil[39;49;00m, [34mnil[39;49;00m)$
   200	  scrollWindow.setPolicy(POLICY_AUTOMATIC, POLICY_AUTOMATIC)$
   201	  scrollWindow.show()$
   202	  $
   203	  [37m# SourceView(gtkSourceView)[39;49;00m$
   204	  SourceView = sourceViewNew(buffer)$
   205	  PSourceView(SourceView).setInsertSpacesInsteadOfTabs([34mTrue[39;49;00m)$
   206	  PSourceView(SourceView).setIndentWidth(win.settings.indentWidth)$
   207	  PSourceView(SourceView).setShowLineNumbers(win.settings.showLineNumbers)$
   208	  PSourceView(SourceView).setHighlightCurrentLine($
   209	               win.settings.highlightCurrentLine)$
   210	  PSourceView(SourceView).setShowRightMargin(win.settings.rightMargin)$
   211	  PSourceView(SourceView).setAutoIndent(win.settings.autoIndent)$
   212	$
   213	  [34mvar[39;49;00m font = font_description_from_string(win.settings.font)$
   214	  SourceView.modifyFont(font)$
   215	  $
   216	  scrollWindow.add(SourceView)$
   217	  SourceView.show()$
   218	$
   219	  buffer.setHighlightMatchingBrackets($
   220	      win.settings.highlightMatchingBrackets)$
   221	  $
   222	  [37m# UGLY workaround for yet another compiler bug:[39;49;00m$
   223	  [34mdiscard[39;49;00m gsignalConnect(buffer, [33m"[39;49;00m[33mmark-set[39;49;00m[33m"[39;49;00m, $
   224	                         GCallback(aporia.cursorMoved), [34mnil[39;49;00m)$
   225	  [34mdiscard[39;49;00m gsignalConnect(buffer, [33m"[39;49;00m[33mchanged[39;49;00m[33m"[39;49;00m, GCallback(aporia.changed), [34mnil[39;49;00m)$
   226	$
   227	  [37m# -- Set the syntax highlighter scheme[39;49;00m$
   228	  buffer.setScheme(win.scheme)$
   229	$
   230	[34mproc [39;49;00m[32maddTab[39;49;00m(name, filename: [36mstring[39;49;00m) =$
   231	  [33m## Adds a tab, if filename is not "" reads the file. And sets[39;49;00m$
   232	  [33m## the tabs SourceViews text to that files contents.[39;49;00m$
   233	  assert(win.nimLang != [34mnil[39;49;00m)$
   234	  [34mvar[39;49;00m buffer: PSourceBuffer = sourceBufferNew(win.nimLang)$
   235	$
   236	  [34mif[39;49;00m filename != [34mnil[39;49;00m [35mand[39;49;00m filename != [33m"[39;49;00m[33m"[39;49;00m:$
   237	    [34mvar[39;49;00m lang = win.langMan.guessLanguage(filename, [34mnil[39;49;00m)$
   238	    [34mif[39;49;00m lang != [34mnil[39;49;00m:$
   239	      buffer.setLanguage(lang)$
   240	    [34melse[39;49;00m:$
   241	      buffer.setHighlightSyntax([34mFalse[39;49;00m)$
   242	$
   243	  [34mvar[39;49;00m nam = name$
   244	  [34mif[39;49;00m nam == [33m"[39;49;00m[33m"[39;49;00m: nam = [33m"[39;49;00m[33mUntitled[39;49;00m[33m"[39;49;00m$
   245	  [34mif[39;49;00m filename == [33m"[39;49;00m[33m"[39;49;00m: nam.add([33m"[39;49;00m[33m *[39;49;00m[33m"[39;49;00m)$
   246	  [34melif[39;49;00m filename != [33m"[39;49;00m[33m"[39;49;00m [35mand[39;49;00m name == [33m"[39;49;00m[33m"[39;49;00m:$
   247	    [37m# Disable the undo/redo manager.[39;49;00m$
   248	    buffer.begin_not_undoable_action()$
   249	  $
   250	    [37m# Load the file.[39;49;00m$
   251	    [34mvar[39;49;00m file: [36mstring[39;49;00m = readFile(filename)$
   252	    [34mif[39;49;00m file != [34mnil[39;49;00m:$
   253	      buffer.set_text(file, len(file))$
   254	      $
   255	    [37m# Enable the undo/redo manager.[39;49;00m$
   256	    buffer.end_not_undoable_action()$
   257	      $
   258	    [37m# Get the name.ext of the filename, for the tabs title[39;49;00m$
   259	    nam = extractFilename(filename)$
   260	  $
   261	  [37m# Init the sourceview[39;49;00m$
   262	  [34mvar[39;49;00m sourceView: PWidget$
   263	  [34mvar[39;49;00m scrollWindow: PScrolledWindow$
   264	  initSourceView(sourceView, scrollWindow, buffer)$
   265	$
   266	  [34mvar[39;49;00m (TabLabel, labelText) = createTabLabel(nam, scrollWindow)$
   267	  [37m# Add a tab[39;49;00m$
   268	  [34mdiscard[39;49;00m win.SourceViewTabs.appendPage(scrollWindow, TabLabel)$
   269	$
   270	  [34mvar[39;49;00m nTab: Tab$
   271	  nTab.buffer = buffer$
   272	  nTab.sourceView = sourceView$
   273	  nTab.label = labelText$
   274	  nTab.saved = (filename != [33m"[39;49;00m[33m"[39;49;00m)$
   275	  nTab.filename = filename$
   276	  win.Tabs.add(nTab)$
   277	$
   278	  PTextView(SourceView).setBuffer(nTab.buffer)$
   279	$
   280	[37m# GTK Events Contd.[39;49;00m$
   281	[37m# -- TopMenu & TopBar[39;49;00m$
   282	$
   283	[34mproc [39;49;00m[32mnewFile[39;49;00m(menuItem: PMenuItem, user_data: pgpointer) =$
   284	  addTab([33m"[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33m"[39;49;00m)$
   285	  win.sourceViewTabs.setCurrentPage(win.Tabs.len()-[34m1[39;49;00m)$
   286	  $
   287	[34mproc [39;49;00m[32mopenFile[39;49;00m(menuItem: PMenuItem, user_data: pgpointer) =$
   288	  [34mvar[39;49;00m startpath = [33m"[39;49;00m[33m"[39;49;00m$
   289	  [34mvar[39;49;00m currPage = win.SourceViewTabs.getCurrentPage()$
   290	  [34mif[39;49;00m currPage <% win.tabs.len: $
   291	    startpath = os.splitFile(win.tabs[currPage].filename).dir$
   292	$
   293	  [34mif[39;49;00m startpath.len == [34m0[39;49;00m:$
   294	    [37m# Use lastSavePath as the startpath[39;49;00m$
   295	    startpath = win.tempStuff.lastSaveDir$
   296	    [34mif[39;49;00m startpath.len == [34m0[39;49;00m:$
   297	      startpath = os.getHomeDir()$
   298	$
   299	  [34mvar[39;49;00m files = ChooseFilesToOpen(win.w, startpath)$
   300	  [34mif[39;49;00m files.len() > [34m0[39;49;00m:$
   301	    [34mfor[39;49;00m f [35min[39;49;00m items(files):$
   302	      [34mtry[39;49;00m:$
   303	        addTab([33m"[39;49;00m[33m"[39;49;00m, f)$
   304	      [34mexcept[39;49;00m EIO:$
   305	        error(win.w, [33m"[39;49;00m[33mUnable to read from file[39;49;00m[33m"[39;49;00m)$
   306	    [37m# Switch to the newly created tab[39;49;00m$
   307	    win.sourceViewTabs.setCurrentPage(win.Tabs.len()-[34m1[39;49;00m)$
   308	  $
   309	[34mproc [39;49;00m[32msaveFile_Activate[39;49;00m(menuItem: PMenuItem, user_data: pgpointer) =$
   310	  [34mvar[39;49;00m current = win.SourceViewTabs.getCurrentPage()$
   311	  saveTab(current, os.splitFile(win.tabs[current].filename).dir)$
   312	$
   313	[34mproc [39;49;00m[32msaveFileAs_Activate[39;49;00m(menuItem: PMenuItem, user_data: pgpointer) =$
   314	  [34mvar[39;49;00m current = win.SourceViewTabs.getCurrentPage()$
   315	  [34mvar[39;49;00m (filename, saved) = (win.Tabs[current].filename, win.Tabs[current].saved)$
   316	$
   317	  win.Tabs[current].saved = [34mFalse[39;49;00m$
   318	  win.Tabs[current].filename = [33m"[39;49;00m[33m"[39;49;00m$
   319	  saveTab(current, os.splitFile(filename).dir)$
   320	  [37m# If the user cancels the save file dialog. Restore the previous filename[39;49;00m$
   321	  [37m# and saved state[39;49;00m$
   322	  [34mif[39;49;00m win.Tabs[current].filename == [33m"[39;49;00m[33m"[39;49;00m:$
   323	    win.Tabs[current].filename = filename$
   324	    win.Tabs[current].saved = saved$
   325	$
   326	[34mproc [39;49;00m[32mundo[39;49;00m(menuItem: PMenuItem, user_data: pgpointer) = $
   327	  [34mvar[39;49;00m current = win.SourceViewTabs.getCurrentPage()$
   328	  [34mif[39;49;00m win.Tabs[current].buffer.canUndo():$
   329	    win.Tabs[current].buffer.undo()$
   330	  $
   331	[34mproc [39;49;00m[32mredo[39;49;00m(menuItem: PMenuItem, user_data: pgpointer) =$
   332	  [34mvar[39;49;00m current = win.SourceViewTabs.getCurrentPage()$
   333	  [34mif[39;49;00m win.Tabs[current].buffer.canRedo():$
   334	    win.Tabs[current].buffer.redo()$
   335	    $
   336	[34mproc [39;49;00m[32mfind_Activate[39;49;00m(menuItem: PMenuItem, user_data: pgpointer) = $
   337	  [37m# Get the selected text, and set the findEntry to it.[39;49;00m$
   338	  [34mvar[39;49;00m currentTab = win.SourceViewTabs.getCurrentPage()$
   339	  [34mvar[39;49;00m insertIter: TTextIter$
   340	  win.Tabs[currentTab].buffer.getIterAtMark([34maddr[39;49;00m(insertIter), $
   341	                                      win.Tabs[currentTab].buffer.getInsert())$
   342	  [34mvar[39;49;00m insertOffset = [34maddr[39;49;00m(insertIter).getOffset()$
   343	  $
   344	  [34mvar[39;49;00m selectIter: TTextIter$
   345	  win.Tabs[currentTab].buffer.getIterAtMark([34maddr[39;49;00m(selectIter), $
   346	                win.Tabs[currentTab].buffer.getSelectionBound())$
   347	  [34mvar[39;49;00m selectOffset = [34maddr[39;49;00m(selectIter).getOffset()$
   348	  $
   349	  [34mif[39;49;00m insertOffset != selectOffset:$
   350	    [34mvar[39;49;00m text = win.Tabs[currentTab].buffer.getText([34maddr[39;49;00m(insertIter), $
   351	                                                   [34maddr[39;49;00m(selectIter), [34mfalse[39;49;00m)$
   352	    win.findEntry.setText(text)$
   353	$
   354	  win.findBar.show()$
   355	  win.findEntry.grabFocus()$
   356	  win.replaceEntry.hide()$
   357	  win.replaceLabel.hide()$
   358	  win.replaceBtn.hide()$
   359	  win.replaceAllBtn.hide()$
   360	$
   361	[34mproc [39;49;00m[32mreplace_Activate[39;49;00m(menuitem: PMenuItem, user_data: pgpointer) =$
   362	  win.findBar.show()$
   363	  win.findEntry.grabFocus()$
   364	  win.replaceEntry.show()$
   365	  win.replaceLabel.show()$
   366	  win.replaceBtn.show()$
   367	  win.replaceAllBtn.show()$
   368	  $
   369	[34mproc [39;49;00m[32msettings_Activate[39;49;00m(menuitem: PMenuItem, user_data: pgpointer) =$
   370	  settings.showSettings(win)$
   371	  $
   372	[34mproc [39;49;00m[32mviewBottomPanel_Toggled[39;49;00m(menuitem: PCheckMenuItem, user_data: pgpointer) =$
   373	  win.settings.bottomPanelVisible = menuitem.itemGetActive()$
   374	  [34mif[39;49;00m win.settings.bottomPanelVisible:$
   375	    win.bottomPanelTabs.show()$
   376	  [34melse[39;49;00m:$
   377	    win.bottomPanelTabs.hide()$
   378	$
   379	[34mvar[39;49;00m$
   380	  pegLineError = [33mpeg"[39;49;00m[33m{[^(]*} [39;49;00m[33m'[39;49;00m[33m([39;49;00m[33m'[39;49;00m[33m {[39;49;00m[33m\[39;49;00m[33md+} [39;49;00m[33m'[39;49;00m[33m, [39;49;00m[33m'[39;49;00m[33m [39;49;00m[33m\[39;49;00m[33md+ [39;49;00m[33m'[39;49;00m[33m) Error:[39;49;00m[33m'[39;49;00m[33m [39;49;00m[33m\[39;49;00m[33ms* {.*}[39;49;00m[33m"[39;49;00m$
   381	  pegLineWarning = [33mpeg"[39;49;00m[33m{[^(]*} [39;49;00m[33m'[39;49;00m[33m([39;49;00m[33m'[39;49;00m[33m {[39;49;00m[33m\[39;49;00m[33md+} [39;49;00m[33m'[39;49;00m[33m, [39;49;00m[33m'[39;49;00m[33m [39;49;00m[33m\[39;49;00m[33md+ [39;49;00m[33m'[39;49;00m[33m) [39;49;00m[33m'[39;49;00m[33m ([39;49;00m[33m'[39;49;00m[33mWarning:[39;49;00m[33m'[39;49;00m[33m/[39;49;00m[33m'[39;49;00m[33mHint:[39;49;00m[33m'[39;49;00m[33m) [39;49;00m[33m\[39;49;00m[33ms* {.*}[39;49;00m[33m"[39;49;00m$
   382	  pegOtherError = [33mpeg"[39;49;00m[33m'[39;49;00m[33mError:[39;49;00m[33m'[39;49;00m[33m [39;49;00m[33m\[39;49;00m[33ms* {.*}[39;49;00m[33m"[39;49;00m$
   383	  pegSuccess = [33mpeg"[39;49;00m[33m'[39;49;00m[33mHint: operation successful[39;49;00m[33m'[39;49;00m[33m.*[39;49;00m[33m"[39;49;00m$
   384	$
   385	[34mproc [39;49;00m[32maddText[39;49;00m(textView: PTextView, text: [36mstring[39;49;00m, colorTag: PTextTag = [34mnil[39;49;00m) =$
   386	  [34mif[39;49;00m text != [34mnil[39;49;00m:$
   387	    [34mvar[39;49;00m iter: TTextIter$
   388	    textView.getBuffer().getEndIter([34maddr[39;49;00m(iter))$
   389	$
   390	    [34mif[39;49;00m colorTag == [34mnil[39;49;00m:$
   391	      textView.getBuffer().insert([34maddr[39;49;00m(iter), text, len(text))$
   392	    [34melse[39;49;00m:$
   393	      textView.getBuffer().insertWithTags([34maddr[39;49;00m(iter), text, len(text), colorTag,$
   394	                                          [34mnil[39;49;00m)$
   395	$
   396	[34mproc [39;49;00m[32mcreateColor[39;49;00m(textView: PTextView, name, color: [36mstring[39;49;00m): PTextTag =$
   397	  [34mvar[39;49;00m tagTable = textView.getBuffer().getTagTable()$
   398	  result = tagTable.tableLookup(name)$
   399	  [34mif[39;49;00m result == [34mnil[39;49;00m:$
   400	    result = textView.getBuffer().createTag(name, [33m"[39;49;00m[33mforeground[39;49;00m[33m"[39;49;00m, color, [34mnil[39;49;00m)$
   401	$
   402	[34mwhen[39;49;00m [35mnot[39;49;00m defined(os.findExe): $
   403	  [34mproc [39;49;00m[32mfindExe[39;49;00m(exe: [36mstring[39;49;00m): [36mstring[39;49;00m = $
   404	    [33m## returns "" if the exe cannot be found[39;49;00m$
   405	    result = addFileExt(exe, os.exeExt)$
   406	    [34mif[39;49;00m ExistsFile(result): [34mreturn[39;49;00m$
   407	    [34mvar[39;49;00m path = os.getEnv([33m"[39;49;00m[33mPATH[39;49;00m[33m"[39;49;00m)$
   408	    [34mfor[39;49;00m candidate [35min[39;49;00m split(path, pathSep): $
   409	      [34mvar[39;49;00m x = candidate / result$
   410	      [34mif[39;49;00m ExistsFile(x): [34mreturn[39;49;00m x$
   411	    result = [33m"[39;49;00m[33m"[39;49;00m$
   412	$
   413	[34mproc [39;49;00m[32mGetCmd[39;49;00m(cmd, filename: [36mstring[39;49;00m): [36mstring[39;49;00m = $
   414	  [34mvar[39;49;00m f = quoteIfContainsWhite(filename)$
   415	  [34mif[39;49;00m cmd =~ [33mpeg"[39;49;00m[33m\[39;49;00m[33ms* [39;49;00m[33m'[39;49;00m[33m$[39;49;00m[33m'[39;49;00m[33m y[39;49;00m[33m'[39;49;00m[33mfindExe[39;49;00m[33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m[33m([39;49;00m[33m'[39;49;00m[33m {[^)]+} [39;49;00m[33m'[39;49;00m[33m)[39;49;00m[33m'[39;49;00m[33m {.*}[39;49;00m[33m"[39;49;00m:$
   416	    [34mvar[39;49;00m exe = quoteIfContainsWhite(findExe(matches[[34m0[39;49;00m]))$
   417	    [34mif[39;49;00m exe.len == [34m0[39;49;00m: exe = matches[[34m0[39;49;00m]$
   418	    result = exe & [33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m & matches[[34m1[39;49;00m] % f$
   419	  [34melse[39;49;00m:$
   420	    result = cmd % f$
   421	$
   422	[34mproc [39;49;00m[32mshowBottomPanel[39;49;00m() =$
   423	  [34mif[39;49;00m [35mnot[39;49;00m win.settings.bottomPanelVisible:$
   424	    win.bottomPanelTabs.show()$
   425	    win.settings.bottomPanelVisible = [34mtrue[39;49;00m$
   426	    PCheckMenuItem(win.viewBottomPanelMenuItem).itemSetActive([34mtrue[39;49;00m)$
   427	  [37m# Scroll to the end of the TextView[39;49;00m$
   428	  [37m# This is stupid, it works sometimes... it's random[39;49;00m$
   429	  [34mvar[39;49;00m endIter: TTextIter$
   430	  win.outputTextView.getBuffer().getEndIter([34maddr[39;49;00m(endIter))$
   431	  [34mdiscard[39;49;00m win.outputTextView.scrollToIter($
   432	    [34maddr[39;49;00m(endIter), [34m0[39;49;00m[34m.25[39;49;00m, [34mFalse[39;49;00m, [34m0[39;49;00m[34m.0[39;49;00m, [34m0[39;49;00m[34m.0[39;49;00m)$
   433	$
   434	[34mproc [39;49;00m[32mcompileRun[39;49;00m(currentTab: [36mint[39;49;00m, shouldRun: [36mbool[39;49;00m) =$
   435	  [34mif[39;49;00m win.Tabs[currentTab].filename.len == [34m0[39;49;00m: [34mreturn[39;49;00m$
   436	  [37m# Clear the outputTextView[39;49;00m$
   437	  win.outputTextView.getBuffer().setText([33m"[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m)$
   438	$
   439	  [34mvar[39;49;00m outp = osProc.execProcess(GetCmd(win.settings.nimrodCmd,$
   440	                                win.Tabs[currentTab].filename))$
   441	  [37m# Colors[39;49;00m$
   442	  [34mvar[39;49;00m normalTag = createColor(win.outputTextView, [33m"[39;49;00m[33mnormalTag[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33m#3d3d3d[39;49;00m[33m"[39;49;00m)$
   443	  [34mvar[39;49;00m errorTag = createColor(win.outputTextView, [33m"[39;49;00m[33merrorTag[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mred[39;49;00m[33m"[39;49;00m)$
   444	  [34mvar[39;49;00m warningTag = createColor(win.outputTextView, [33m"[39;49;00m[33mwarningTag[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mdarkorange[39;49;00m[33m"[39;49;00m)$
   445	  [34mvar[39;49;00m successTag = createColor(win.outputTextView, [33m"[39;49;00m[33msuccessTag[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mdarkgreen[39;49;00m[33m"[39;49;00m)$
   446	  [34mfor[39;49;00m x [35min[39;49;00m outp.splitLines():$
   447	    [34mif[39;49;00m x =~ pegLineError / pegOtherError:$
   448	      win.outputTextView.addText([33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m & x, errorTag)$
   449	    [34melif[39;49;00m x=~ pegSuccess:$
   450	      win.outputTextView.addText([33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m & x, successTag)$
   451	      $
   452	      [37m# Launch the process[39;49;00m$
   453	      [34mif[39;49;00m shouldRun:$
   454	        [34mvar[39;49;00m filename = changeFileExt(win.Tabs[currentTab].filename, os.ExeExt)$
   455	        [34mvar[39;49;00m output = [33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m & osProc.execProcess(filename)$
   456	        win.outputTextView.addText(output)$
   457	    [34melif[39;49;00m x =~ pegLineWarning:$
   458	      win.outputTextView.addText([33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m & x, warningTag)$
   459	    [34melse[39;49;00m:$
   460	      win.outputTextView.addText([33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m & x, normalTag)$
   461	  showBottomPanel()$
   462	$
   463	[34mproc [39;49;00m[32mCompileCurrent_Activate[39;49;00m(menuitem: PMenuItem, user_data: pgpointer) =$
   464	  saveFile_Activate([34mnil[39;49;00m, [34mnil[39;49;00m)$
   465	  compileRun(win.SourceViewTabs.getCurrentPage(), [34mfalse[39;49;00m)$
   466	  $
   467	[34mproc [39;49;00m[32mCompileRunCurrent_Activate[39;49;00m(menuitem: PMenuItem, user_data: pgpointer) =$
   468	  saveFile_Activate([34mnil[39;49;00m, [34mnil[39;49;00m)$
   469	  compileRun(win.SourceViewTabs.getCurrentPage(), [34mtrue[39;49;00m)$
   470	$
   471	[34mproc [39;49;00m[32mCompileProject_Activate[39;49;00m(menuitem: PMenuItem, user_data: pgpointer) =$
   472	  saveAllTabs()$
   473	  compileRun(getProjectTab(), [34mfalse[39;49;00m)$
   474	  $
   475	[34mproc [39;49;00m[32mCompileRunProject_Activate[39;49;00m(menuitem: PMenuItem, user_data: pgpointer) =$
   476	  saveAllTabs()$
   477	  compileRun(getProjectTab(), [34mtrue[39;49;00m)$
   478	$
   479	[34mproc [39;49;00m[32mRunCustomCommand[39;49;00m(cmd: [36mstring[39;49;00m) = $
   480	  saveFile_Activate([34mnil[39;49;00m, [34mnil[39;49;00m)$
   481	  [34mvar[39;49;00m currentTab = win.SourceViewTabs.getCurrentPage()$
   482	  [34mif[39;49;00m win.Tabs[currentTab].filename.len == [34m0[39;49;00m [35mor[39;49;00m cmd.len == [34m0[39;49;00m: [34mreturn[39;49;00m$
   483	  [37m# Clear the outputTextView[39;49;00m$
   484	  win.outputTextView.getBuffer().setText([33m"[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m)$
   485	  [34mvar[39;49;00m outp = osProc.execProcess(GetCmd(cmd, win.Tabs[currentTab].filename))$
   486	  [34mvar[39;49;00m normalTag = createColor(win.outputTextView, [33m"[39;49;00m[33mnormalTag[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33m#3d3d3d[39;49;00m[33m"[39;49;00m)$
   487	  [34mfor[39;49;00m x [35min[39;49;00m outp.splitLines():$
   488	    win.outputTextView.addText([33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m & x, normalTag)$
   489	  showBottomPanel()$
   490	$
   491	[34mproc [39;49;00m[32mRunCustomCommand1[39;49;00m(menuitem: PMenuItem, user_data: pgpointer) =$
   492	  RunCustomCommand(win.settings.customCmd1)$
   493	$
   494	[34mproc [39;49;00m[32mRunCustomCommand2[39;49;00m(menuitem: PMenuItem, user_data: pgpointer) =$
   495	  RunCustomCommand(win.settings.customCmd2)$
   496	$
   497	[34mproc [39;49;00m[32mRunCustomCommand3[39;49;00m(menuitem: PMenuItem, user_data: pgpointer) =$
   498	  RunCustomCommand(win.settings.customCmd3)$
   499	$
   500	[37m# -- FindBar[39;49;00m$
   501	$
   502	[34mproc [39;49;00m[32mnextBtn_Clicked[39;49;00m(button: PButton, user_data: pgpointer) = findText([34mTrue[39;49;00m)$
   503	[34mproc [39;49;00m[32mprevBtn_Clicked[39;49;00m(button: PButton, user_data: pgpointer) = findText([34mFalse[39;49;00m)$
   504	$
   505	[34mproc [39;49;00m[32mreplaceBtn_Clicked[39;49;00m(button: PButton, user_data: pgpointer) =$
   506	  [34mvar[39;49;00m currentTab = win.SourceViewTabs.getCurrentPage()$
   507	  [34mvar[39;49;00m start, theEnd: TTextIter$
   508	  [34mif[39;49;00m [35mnot[39;49;00m win.Tabs[currentTab].buffer.getSelectionBounds($
   509	        [34maddr[39;49;00m(start), [34maddr[39;49;00m(theEnd)):$
   510	    [37m# If no text is selected, try finding a match.[39;49;00m$
   511	    findText([34mTrue[39;49;00m)$
   512	    [34mif[39;49;00m [35mnot[39;49;00m win.Tabs[currentTab].buffer.getSelectionBounds($
   513	          [34maddr[39;49;00m(start), [34maddr[39;49;00m(theEnd)):$
   514	      [37m# No match[39;49;00m$
   515	      [34mreturn[39;49;00m$
   516	  $
   517	  [37m# Remove the text[39;49;00m$
   518	  win.Tabs[currentTab].buffer.delete([34maddr[39;49;00m(start), [34maddr[39;49;00m(theEnd))$
   519	  [37m# Insert the replacement[39;49;00m$
   520	  [34mvar[39;49;00m text = getText(win.replaceEntry)$
   521	  win.Tabs[currentTab].buffer.insert([34maddr[39;49;00m(start), text, len(text))$
   522	  $
   523	[34mproc [39;49;00m[32mreplaceAllBtn_Clicked[39;49;00m(button: PButton, user_data: pgpointer) =$
   524	  [34mvar[39;49;00m find = getText(win.findEntry)$
   525	  [34mvar[39;49;00m replace = getText(win.replaceEntry)$
   526	  [34mdiscard[39;49;00m replaceAll(find, replace)$
   527	  $
   528	[34mproc [39;49;00m[32mcloseBtn_Clicked[39;49;00m(button: PButton, user_data: pgpointer) = $
   529	  win.findBar.hide()$
   530	$
   531	[34mproc [39;49;00m[32mcaseSens_Changed[39;49;00m(radiomenuitem: PRadioMenuitem, user_data: pgpointer) =$
   532	  win.settings.search = [33m"[39;49;00m[33mcasesens[39;49;00m[33m"[39;49;00m$
   533	[34mproc [39;49;00m[32mcaseInSens_Changed[39;49;00m(radiomenuitem: PRadioMenuitem, user_data: pgpointer) =$
   534	  win.settings.search = [33m"[39;49;00m[33mcaseinsens[39;49;00m[33m"[39;49;00m$
   535	[34mproc [39;49;00m[32mstyle_Changed[39;49;00m(radiomenuitem: PRadioMenuitem, user_data: pgpointer) =$
   536	  win.settings.search = [33m"[39;49;00m[33mstyle[39;49;00m[33m"[39;49;00m$
   537	[34mproc [39;49;00m[32mregex_Changed[39;49;00m(radiomenuitem: PRadioMenuitem, user_data: pgpointer) =$
   538	  win.settings.search = [33m"[39;49;00m[33mregex[39;49;00m[33m"[39;49;00m$
   539	[34mproc [39;49;00m[32mpeg_Changed[39;49;00m(radiomenuitem: PRadioMenuitem, user_data: pgpointer) =$
   540	  win.settings.search = [33m"[39;49;00m[33mpeg[39;49;00m[33m"[39;49;00m$
   541	$
   542	[34mproc [39;49;00m[32mextraBtn_Clicked[39;49;00m(button: PButton, user_data: pgpointer) =$
   543	  [34mvar[39;49;00m extraMenu = menuNew()$
   544	  [34mvar[39;49;00m group: PGSList$
   545	$
   546	  [34mvar[39;49;00m caseSensMenuItem = radio_menu_item_new(group, [33m"[39;49;00m[33mCase sensitive[39;49;00m[33m"[39;49;00m)$
   547	  extraMenu.append(caseSensMenuItem)$
   548	  [34mdiscard[39;49;00m signal_connect(caseSensMenuItem, [33m"[39;49;00m[33mtoggled[39;49;00m[33m"[39;49;00m, $
   549	                          SIGNAL_FUNC(caseSens_Changed), [34mnil[39;49;00m)$
   550	  caseSensMenuItem.show()$
   551	  group = caseSensMenuItem.ItemGetGroup()$
   552	  $
   553	  [34mvar[39;49;00m caseInSensMenuItem = radio_menu_item_new(group, [33m"[39;49;00m[33mCase insensitive[39;49;00m[33m"[39;49;00m)$
   554	  extraMenu.append(caseInSensMenuItem)$
   555	  [34mdiscard[39;49;00m signal_connect(caseInSensMenuItem, [33m"[39;49;00m[33mtoggled[39;49;00m[33m"[39;49;00m, $
   556	                          SIGNAL_FUNC(caseInSens_Changed), [34mnil[39;49;00m)$
   557	  caseInSensMenuItem.show()$
   558	  group = caseInSensMenuItem.ItemGetGroup()$
   559	  $
   560	  [34mvar[39;49;00m styleMenuItem = radio_menu_item_new(group, [33m"[39;49;00m[33mStyle insensitive[39;49;00m[33m"[39;49;00m)$
   561	  extraMenu.append(styleMenuItem)$
   562	  [34mdiscard[39;49;00m signal_connect(styleMenuItem, [33m"[39;49;00m[33mtoggled[39;49;00m[33m"[39;49;00m, $
   563	                          SIGNAL_FUNC(style_Changed), [34mnil[39;49;00m)$
   564	  styleMenuItem.show()$
   565	  group = styleMenuItem.ItemGetGroup()$
   566	  $
   567	  [34mvar[39;49;00m regexMenuItem = radio_menu_item_new(group, [33m"[39;49;00m[33mRegex[39;49;00m[33m"[39;49;00m)$
   568	  extraMenu.append(regexMenuItem)$
   569	  [34mdiscard[39;49;00m signal_connect(regexMenuItem, [33m"[39;49;00m[33mtoggled[39;49;00m[33m"[39;49;00m, $
   570	                          SIGNAL_FUNC(regex_Changed), [34mnil[39;49;00m)$
   571	  regexMenuItem.show()$
   572	  group = regexMenuItem.ItemGetGroup()$
   573	  $
   574	  [34mvar[39;49;00m pegMenuItem = radio_menu_item_new(group, [33m"[39;49;00m[33mPegs[39;49;00m[33m"[39;49;00m)$
   575	  extraMenu.append(pegMenuItem)$
   576	  [34mdiscard[39;49;00m signal_connect(pegMenuItem, [33m"[39;49;00m[33mtoggled[39;49;00m[33m"[39;49;00m, $
   577	                          SIGNAL_FUNC(peg_Changed), [34mnil[39;49;00m)$
   578	  pegMenuItem.show()$
   579	  $
   580	  [37m# Make the correct radio button active[39;49;00m$
   581	  [34mcase[39;49;00m win.settings.search$
   582	  [34mof[39;49;00m [33m"[39;49;00m[33mcasesens[39;49;00m[33m"[39;49;00m:$
   583	    PCheckMenuItem(caseSensMenuItem).ItemSetActive([34mTrue[39;49;00m)$
   584	  [34mof[39;49;00m [33m"[39;49;00m[33mcaseinsens[39;49;00m[33m"[39;49;00m:$
   585	    PCheckMenuItem(caseInSensMenuItem).ItemSetActive([34mTrue[39;49;00m)$
   586	  [34mof[39;49;00m [33m"[39;49;00m[33mstyle[39;49;00m[33m"[39;49;00m:$
   587	    PCheckMenuItem(styleMenuItem).ItemSetActive([34mTrue[39;49;00m)$
   588	  [34mof[39;49;00m [33m"[39;49;00m[33mregex[39;49;00m[33m"[39;49;00m:$
   589	    PCheckMenuItem(regexMenuItem).ItemSetActive([34mTrue[39;49;00m)$
   590	  [34mof[39;49;00m [33m"[39;49;00m[33mpeg[39;49;00m[33m"[39;49;00m:$
   591	    PCheckMenuItem(pegMenuItem).ItemSetActive([34mTrue[39;49;00m)$
   592	$
   593	  extraMenu.popup([34mnil[39;49;00m, [34mnil[39;49;00m, [34mnil[39;49;00m, [34mnil[39;49;00m, [34m0[39;49;00m, get_current_event_time())$
   594	$
   595	[37m# GUI Initialization[39;49;00m$
   596	$
   597	[34mproc [39;49;00m[32mcreateAccelMenuItem[39;49;00m(toolsMenu: PMenu, accGroup: PAccelGroup, $
   598	                         label: [36mstring[39;49;00m, acc: gint,$
   599	                         action: [34mproc[39;49;00m (i: PMenuItem, p: pgpointer)) = $
   600	  [34mvar[39;49;00m result = menu_item_new(label)$
   601	  result.addAccelerator([33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m, accGroup, acc, [34m0[39;49;00m, ACCEL_VISIBLE)$
   602	  ToolsMenu.append(result)$
   603	  show(result)$
   604	  [34mdiscard[39;49;00m signal_connect(result, [33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m, SIGNAL_FUNC(action), [34mnil[39;49;00m)$
   605	$
   606	[34mproc [39;49;00m[32mcreateSeparator[39;49;00m(menu: PMenu) =$
   607	  [34mvar[39;49;00m sep = separator_menu_item_new()$
   608	  menu.append(sep)$
   609	  sep.show()$
   610	$
   611	[34mproc [39;49;00m[32minitTopMenu[39;49;00m(MainBox: PBox) =$
   612	  [37m# Create a accelerator group, used for shortcuts[39;49;00m$
   613	  [37m# like CTRL + S in SaveMenuItem[39;49;00m$
   614	  [34mvar[39;49;00m accGroup = accel_group_new()$
   615	  add_accel_group(win.w, accGroup)$
   616	$
   617	  [37m# TopMenu(MenuBar)[39;49;00m$
   618	  [34mvar[39;49;00m TopMenu = menuBarNew()$
   619	  $
   620	  [37m# FileMenu[39;49;00m$
   621	  [34mvar[39;49;00m FileMenu = menuNew()$
   622	$
   623	  [34mvar[39;49;00m NewMenuItem = menu_item_new([33m"[39;49;00m[33mNew[39;49;00m[33m"[39;49;00m) [37m# New[39;49;00m$
   624	  FileMenu.append(NewMenuItem)$
   625	  show(NewMenuItem)$
   626	  [34mdiscard[39;49;00m signal_connect(NewMenuItem, [33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m, $
   627	                          SIGNAL_FUNC(newFile), [34mnil[39;49;00m)$
   628	$
   629	  createSeparator(FileMenu)$
   630	$
   631	  [34mvar[39;49;00m OpenMenuItem = menu_item_new([33m"[39;49;00m[33mOpen...[39;49;00m[33m"[39;49;00m) [37m# Open...[39;49;00m$
   632	  [37m# CTRL + O[39;49;00m$
   633	  OpenMenuItem.add_accelerator([33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m, accGroup, $
   634	                  KEY_o, CONTROL_MASK, ACCEL_VISIBLE) $
   635	  FileMenu.append(OpenMenuItem)$
   636	  show(OpenMenuItem)$
   637	  [34mdiscard[39;49;00m signal_connect(OpenMenuItem, [33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m, $
   638	                          SIGNAL_FUNC(aporia.openFile), [34mnil[39;49;00m)$
   639	  $
   640	  [34mvar[39;49;00m SaveMenuItem = menu_item_new([33m"[39;49;00m[33mSave[39;49;00m[33m"[39;49;00m) [37m# Save[39;49;00m$
   641	  [37m# CTRL + S[39;49;00m$
   642	  SaveMenuItem.add_accelerator([33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m, accGroup, $
   643	                  KEY_s, CONTROL_MASK, ACCEL_VISIBLE) $
   644	  FileMenu.append(SaveMenuItem)$
   645	  show(SaveMenuItem)$
   646	  [34mdiscard[39;49;00m signal_connect(SaveMenuItem, [33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m, $
   647	                          SIGNAL_FUNC(saveFile_activate), [34mnil[39;49;00m)$
   648	$
   649	  [34mvar[39;49;00m SaveAsMenuItem = menu_item_new([33m"[39;49;00m[33mSave As...[39;49;00m[33m"[39;49;00m) [37m# Save as...[39;49;00m$
   650	$
   651	  SaveAsMenuItem.add_accelerator([33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m, accGroup, $
   652	                  KEY_s, CONTROL_MASK [35mor[39;49;00m gdk2.SHIFT_MASK, ACCEL_VISIBLE) $
   653	  FileMenu.append(SaveAsMenuItem)$
   654	  show(SaveAsMenuItem)$
   655	  [34mdiscard[39;49;00m signal_connect(SaveAsMenuItem, [33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m, $
   656	                          SIGNAL_FUNC(saveFileAs_Activate), [34mnil[39;49;00m)$
   657	  $
   658	  [34mvar[39;49;00m FileMenuItem = menuItemNewWithMnemonic([33m"[39;49;00m[33m_File[39;49;00m[33m"[39;49;00m)$
   659	$
   660	  FileMenuItem.setSubMenu(FileMenu)$
   661	  FileMenuItem.show()$
   662	  TopMenu.append(FileMenuItem)$
   663	  $
   664	  [37m# Edit menu[39;49;00m$
   665	  [34mvar[39;49;00m EditMenu = menuNew()$
   666	$
   667	  [34mvar[39;49;00m UndoMenuItem = menu_item_new([33m"[39;49;00m[33mUndo[39;49;00m[33m"[39;49;00m) [37m# Undo[39;49;00m$
   668	  EditMenu.append(UndoMenuItem)$
   669	  show(UndoMenuItem)$
   670	  [34mdiscard[39;49;00m signal_connect(UndoMenuItem, [33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m, $
   671	                          SIGNAL_FUNC(aporia.undo), [34mnil[39;49;00m)$
   672	  $
   673	  [34mvar[39;49;00m RedoMenuItem = menu_item_new([33m"[39;49;00m[33mRedo[39;49;00m[33m"[39;49;00m) [37m# Undo[39;49;00m$
   674	  EditMenu.append(RedoMenuItem)$
   675	  show(RedoMenuItem)$
   676	  [34mdiscard[39;49;00m signal_connect(RedoMenuItem, [33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m, $
   677	                          SIGNAL_FUNC(aporia.redo), [34mnil[39;49;00m)$
   678	$
   679	  createSeparator(EditMenu)$
   680	  $
   681	  [34mvar[39;49;00m FindMenuItem = menu_item_new([33m"[39;49;00m[33mFind[39;49;00m[33m"[39;49;00m) [37m# Find[39;49;00m$
   682	  FindMenuItem.add_accelerator([33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m, accGroup, $
   683	                  KEY_f, CONTROL_MASK, ACCEL_VISIBLE) $
   684	  EditMenu.append(FindMenuItem)$
   685	  show(FindMenuItem)$
   686	  [34mdiscard[39;49;00m signal_connect(FindMenuItem, [33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m, $
   687	                          SIGNAL_FUNC(aporia.find_Activate), [34mnil[39;49;00m)$
   688	$
   689	  [34mvar[39;49;00m ReplaceMenuItem = menu_item_new([33m"[39;49;00m[33mReplace[39;49;00m[33m"[39;49;00m) [37m# Replace[39;49;00m$
   690	  ReplaceMenuItem.add_accelerator([33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m, accGroup, $
   691	                  KEY_h, CONTROL_MASK, ACCEL_VISIBLE) $
   692	  EditMenu.append(ReplaceMenuItem)$
   693	  show(ReplaceMenuItem)$
   694	  [34mdiscard[39;49;00m signal_connect(ReplaceMenuItem, [33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m, $
   695	                          SIGNAL_FUNC(aporia.replace_Activate), [34mnil[39;49;00m)$
   696	$
   697	  createSeparator(EditMenu)$
   698	  $
   699	  [34mvar[39;49;00m SettingsMenuItem = menu_item_new([33m"[39;49;00m[33mSettings...[39;49;00m[33m"[39;49;00m) [37m# Settings[39;49;00m$
   700	  EditMenu.append(SettingsMenuItem)$
   701	  show(SettingsMenuItem)$
   702	  [34mdiscard[39;49;00m signal_connect(SettingsMenuItem, [33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m, $
   703	                          SIGNAL_FUNC(aporia.Settings_Activate), [34mnil[39;49;00m)$
   704	$
   705	  [34mvar[39;49;00m EditMenuItem = menuItemNewWithMnemonic([33m"[39;49;00m[33m_Edit[39;49;00m[33m"[39;49;00m)$
   706	$
   707	  EditMenuItem.setSubMenu(EditMenu)$
   708	  EditMenuItem.show()$
   709	  TopMenu.append(EditMenuItem)$
   710	  $
   711	  [37m# View menu[39;49;00m$
   712	  [34mvar[39;49;00m ViewMenu = menuNew()$
   713	  $
   714	  win.viewBottomPanelMenuItem = check_menu_item_new([33m"[39;49;00m[33mBottom Panel[39;49;00m[33m"[39;49;00m)$
   715	  PCheckMenuItem(win.viewBottomPanelMenuItem).itemSetActive($
   716	         win.settings.bottomPanelVisible)$
   717	  win.viewBottomPanelMenuItem.add_accelerator([33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m, accGroup, $
   718	                  KEY_f9, CONTROL_MASK, ACCEL_VISIBLE) $
   719	  ViewMenu.append(win.viewBottomPanelMenuItem)$
   720	  show(win.viewBottomPanelMenuItem)$
   721	  [34mdiscard[39;49;00m signal_connect(win.viewBottomPanelMenuItem, [33m"[39;49;00m[33mtoggled[39;49;00m[33m"[39;49;00m, $
   722	                          SIGNAL_FUNC(aporia.viewBottomPanel_Toggled), [34mnil[39;49;00m)$
   723	  $
   724	  [34mvar[39;49;00m ViewMenuItem = menuItemNewWithMnemonic([33m"[39;49;00m[33m_View[39;49;00m[33m"[39;49;00m)$
   725	$
   726	  ViewMenuItem.setSubMenu(ViewMenu)$
   727	  ViewMenuItem.show()$
   728	  TopMenu.append(ViewMenuItem)       $
   729	  $
   730	  $
   731	  [37m# Tools menu[39;49;00m$
   732	  [34mvar[39;49;00m ToolsMenu = menuNew()$
   733	$
   734	  createAccelMenuItem(ToolsMenu, accGroup, [33m"[39;49;00m[33mCompile current file[39;49;00m[33m"[39;49;00m, $
   735	                      KEY_F4, aporia.CompileCurrent_Activate)$
   736	  createAccelMenuItem(ToolsMenu, accGroup, [33m"[39;49;00m[33mCompile & run current file[39;49;00m[33m"[39;49;00m, $
   737	                      KEY_F5, aporia.CompileRunCurrent_Activate)$
   738	  createSeparator(ToolsMenu)$
   739	  createAccelMenuItem(ToolsMenu, accGroup, [33m"[39;49;00m[33mCompile project[39;49;00m[33m"[39;49;00m, $
   740	                      KEY_F8, aporia.CompileProject_Activate)$
   741	  createAccelMenuItem(ToolsMenu, accGroup, [33m"[39;49;00m[33mCompile & run project[39;49;00m[33m"[39;49;00m, $
   742	                      KEY_F9, aporia.CompileRunProject_Activate)$
   743	  createSeparator(ToolsMenu)$
   744	  createAccelMenuItem(ToolsMenu, accGroup, [33m"[39;49;00m[33mRun custom command 1[39;49;00m[33m"[39;49;00m, $
   745	                      KEY_F1, aporia.RunCustomCommand1)$
   746	  createAccelMenuItem(ToolsMenu, accGroup, [33m"[39;49;00m[33mRun custom command 2[39;49;00m[33m"[39;49;00m, $
   747	                      KEY_F2, aporia.RunCustomCommand2)$
   748	  createAccelMenuItem(ToolsMenu, accGroup, [33m"[39;49;00m[33mRun custom command 3[39;49;00m[33m"[39;49;00m, $
   749	                      KEY_F3, aporia.RunCustomCommand3)$
   750	  $
   751	  [34mvar[39;49;00m ToolsMenuItem = menuItemNewWithMnemonic([33m"[39;49;00m[33m_Tools[39;49;00m[33m"[39;49;00m)$
   752	  $
   753	  ToolsMenuItem.setSubMenu(ToolsMenu)$
   754	  ToolsMenuItem.show()$
   755	  TopMenu.append(ToolsMenuItem)$
   756	  $
   757	  [37m# Help menu[39;49;00m$
   758	  MainBox.packStart(TopMenu, [34mFalse[39;49;00m, [34mFalse[39;49;00m, [34m0[39;49;00m)$
   759	  TopMenu.show()$
   760	$
   761	[34mproc [39;49;00m[32minitToolBar[39;49;00m(MainBox: PBox) =$
   762	  [37m# TopBar(ToolBar)[39;49;00m$
   763	  [34mvar[39;49;00m TopBar = toolbarNew()$
   764	  TopBar.setStyle(TOOLBAR_ICONS)$
   765	  $
   766	  [34mvar[39;49;00m NewFileItem = TopBar.insertStock(STOCK_NEW, [33m"[39;49;00m[33mNew File[39;49;00m[33m"[39;49;00m,$
   767	                      [33m"[39;49;00m[33mNew File[39;49;00m[33m"[39;49;00m, SIGNAL_FUNC(aporia.newFile), [34mnil[39;49;00m, [34m0[39;49;00m)$
   768	  TopBar.appendSpace()$
   769	  [34mvar[39;49;00m OpenItem = TopBar.insertStock(STOCK_OPEN, [33m"[39;49;00m[33mOpen[39;49;00m[33m"[39;49;00m,$
   770	                      [33m"[39;49;00m[33mOpen[39;49;00m[33m"[39;49;00m, SIGNAL_FUNC(aporia.openFile), [34mnil[39;49;00m, -[34m1[39;49;00m)$
   771	  [34mvar[39;49;00m SaveItem = TopBar.insertStock(STOCK_SAVE, [33m"[39;49;00m[33mSave[39;49;00m[33m"[39;49;00m,$
   772	                      [33m"[39;49;00m[33mSave[39;49;00m[33m"[39;49;00m, SIGNAL_FUNC(saveFile_Activate), [34mnil[39;49;00m, -[34m1[39;49;00m)$
   773	  TopBar.appendSpace()$
   774	  [34mvar[39;49;00m UndoItem = TopBar.insertStock(STOCK_UNDO, [33m"[39;49;00m[33mUndo[39;49;00m[33m"[39;49;00m, $
   775	                      [33m"[39;49;00m[33mUndo[39;49;00m[33m"[39;49;00m, SIGNAL_FUNC(aporia.undo), [34mnil[39;49;00m, -[34m1[39;49;00m)$
   776	  [34mvar[39;49;00m RedoItem = TopBar.insertStock(STOCK_REDO, [33m"[39;49;00m[33mRedo[39;49;00m[33m"[39;49;00m,$
   777	                      [33m"[39;49;00m[33mRedo[39;49;00m[33m"[39;49;00m, SIGNAL_FUNC(aporia.redo), [34mnil[39;49;00m, -[34m1[39;49;00m)$
   778	  $
   779	  MainBox.packStart(TopBar, [34mFalse[39;49;00m, [34mFalse[39;49;00m, [34m0[39;49;00m)$
   780	  TopBar.show()$
   781	  $
   782	[34mproc [39;49;00m[32minitSourceViewTabs[39;49;00m() =$
   783	  win.SourceViewTabs = notebookNew()$
   784	  [37m#win.sourceViewTabs.dragDestSet(DEST_DEFAULT_DROP, nil, 0, ACTION_MOVE)[39;49;00m$
   785	  [34mdiscard[39;49;00m win.SourceViewTabs.signalConnect($
   786	          [33m"[39;49;00m[33mswitch-page[39;49;00m[33m"[39;49;00m, SIGNAL_FUNC(onSwitchTab), [34mnil[39;49;00m)$
   787	  [37m#discard win.SourceViewTabs.signalConnect([39;49;00m$
   788	  [37m#        "drag-drop", SIGNAL_FUNC(svTabs_DragDrop), nil)[39;49;00m$
   789	  [37m#discard win.SourceViewTabs.signalConnect([39;49;00m$
   790	  [37m#        "drag-data-received", SIGNAL_FUNC(svTabs_DragDataRecv), nil)[39;49;00m$
   791	  [37m#discard win.SourceViewTabs.signalConnect([39;49;00m$
   792	  [37m#        "drag-motion", SIGNAL_FUNC(svTabs_DragMotion), nil)[39;49;00m$
   793	  win.SourceViewTabs.set_scrollable([34mTrue[39;49;00m)$
   794	  $
   795	  win.SourceViewTabs.show()$
   796	  [34mif[39;49;00m lastSession.len != [34m0[39;49;00m:$
   797	    [34mfor[39;49;00m i [35min[39;49;00m [34m0[39;49;00m .. len(lastSession)-[34m1[39;49;00m:$
   798	      [34mvar[39;49;00m splitUp = lastSession[i].split([33m'[39;49;00m[33m|[39;49;00m[33m'[39;49;00m)$
   799	      [34mvar[39;49;00m (filename, offset) = (splitUp[[34m0[39;49;00m], splitUp[[34m1[39;49;00m])$
   800	      addTab([33m"[39;49;00m[33m"[39;49;00m, filename)$
   801	      $
   802	      [34mvar[39;49;00m iter: TTextIter$
   803	      win.Tabs[i].buffer.getIterAtOffset([34maddr[39;49;00m(iter), offset.parseInt())$
   804	      win.Tabs[i].buffer.moveMarkByName([33m"[39;49;00m[33minsert[39;49;00m[33m"[39;49;00m, [34maddr[39;49;00m(iter))$
   805	      win.Tabs[i].buffer.moveMarkByName([33m"[39;49;00m[33mselection_bound[39;49;00m[33m"[39;49;00m, [34maddr[39;49;00m(iter))$
   806	      $
   807	      [37m# TODO: Fix this..... :([39;49;00m$
   808	      [34mdiscard[39;49;00m PTextView(win.Tabs[i].sourceView).$
   809	          scrollToIter([34maddr[39;49;00m(iter), [34m0[39;49;00m[34m.25[39;49;00m, [34mtrue[39;49;00m, [34m0[39;49;00m[34m.0[39;49;00m, [34m0[39;49;00m[34m.0[39;49;00m)$
   810	  [34melse[39;49;00m:$
   811	    addTab([33m"[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33m"[39;49;00m)$
   812	  $
   813	  [37m# This doesn't work :\[39;49;00m$
   814	  win.Tabs[[34m0[39;49;00m].sourceView.grabFocus()$
   815	$
   816	  $
   817	[34mproc [39;49;00m[32minitBottomTabs[39;49;00m() =$
   818	  win.bottomPanelTabs = notebookNew()$
   819	  [34mif[39;49;00m win.settings.bottomPanelVisible:$
   820	    win.bottomPanelTabs.show()$
   821	  $
   822	  [37m# output tab[39;49;00m$
   823	  [34mvar[39;49;00m tabLabel = labelNew([33m"[39;49;00m[33mOutput[39;49;00m[33m"[39;49;00m)$
   824	  [34mvar[39;49;00m outputTab = vboxNew([34mFalse[39;49;00m, [34m0[39;49;00m)$
   825	  [34mdiscard[39;49;00m win.bottomPanelTabs.appendPage(outputTab, tabLabel)$
   826	  [37m# Compiler tabs, gtktextview[39;49;00m$
   827	  [34mvar[39;49;00m outputScrolledWindow = scrolledwindowNew([34mnil[39;49;00m, [34mnil[39;49;00m)$
   828	  outputScrolledWindow.setPolicy(POLICY_AUTOMATIC, POLICY_AUTOMATIC)$
   829	  outputTab.packStart(outputScrolledWindow, [34mtrue[39;49;00m, [34mtrue[39;49;00m, [34m0[39;49;00m)$
   830	  outputScrolledWindow.show()$
   831	  $
   832	  win.outputTextView = textviewNew()$
   833	  outputScrolledWindow.add(win.outputTextView)$
   834	  win.outputTextView.show()$
   835	  $
   836	  outputTab.show()$
   837	$
   838	[34mproc [39;49;00m[32minitTAndBP[39;49;00m(MainBox: PBox) =$
   839	  [37m# This init's the HPaned, which splits the sourceViewTabs[39;49;00m$
   840	  [37m# and the BottomPanelTabs[39;49;00m$
   841	  initSourceViewTabs()$
   842	  initBottomTabs()$
   843	  $
   844	  [34mvar[39;49;00m TAndBPVPaned = vpanedNew()$
   845	  tandbpVPaned.pack1(win.sourceViewTabs, resize=[34mTrue[39;49;00m, shrink=[34mFalse[39;49;00m)$
   846	  tandbpVPaned.pack2(win.bottomPanelTabs, resize=[34mFalse[39;49;00m, shrink=[34mFalse[39;49;00m)$
   847	  MainBox.packStart(TAndBPVPaned, [34mTrue[39;49;00m, [34mTrue[39;49;00m, [34m0[39;49;00m)$
   848	  tandbpVPaned.setPosition(win.settings.VPanedPos)$
   849	  TAndBPVPaned.show()$
   850	$
   851	[34mproc [39;49;00m[32minitFindBar[39;49;00m(MainBox: PBox) =$
   852	  [37m# Create a fixed container[39;49;00m$
   853	  win.findBar = HBoxNew([34mFalse[39;49;00m, [34m0[39;49;00m)$
   854	  win.findBar.setSpacing([34m4[39;49;00m)$
   855	$
   856	  [37m# Add a Label 'Find'[39;49;00m$
   857	  [34mvar[39;49;00m findLabel = labelNew([33m"[39;49;00m[33mFind:[39;49;00m[33m"[39;49;00m)$
   858	  win.findBar.packStart(findLabel, [34mFalse[39;49;00m, [34mFalse[39;49;00m, [34m0[39;49;00m)$
   859	  findLabel.show()$
   860	$
   861	  [37m# Add a (find) text entry[39;49;00m$
   862	  win.findEntry = entryNew()$
   863	  win.findBar.packStart(win.findEntry, [34mFalse[39;49;00m, [34mFalse[39;49;00m, [34m0[39;49;00m)$
   864	  [34mdiscard[39;49;00m win.findEntry.signalConnect([33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m, SIGNAL_FUNC($
   865	                                      aporia.nextBtn_Clicked), [34mnil[39;49;00m)$
   866	  win.findEntry.show()$
   867	  [34mvar[39;49;00m rq: TRequisition $
   868	  win.findEntry.sizeRequest([34maddr[39;49;00m(rq))$
   869	$
   870	  [37m# Make the (find) text entry longer[39;49;00m$
   871	  win.findEntry.set_size_request([34m190[39;49;00m, rq.height)$
   872	  $
   873	  [37m# Add a Label 'Replace' [39;49;00m$
   874	  [37m# - This Is only shown, when the 'Search & Replace'(CTRL + H) is shown[39;49;00m$
   875	  win.replaceLabel = labelNew([33m"[39;49;00m[33mReplace:[39;49;00m[33m"[39;49;00m)$
   876	  win.findBar.packStart(win.replaceLabel, [34mFalse[39;49;00m, [34mFalse[39;49;00m, [34m0[39;49;00m)$
   877	  [37m#replaceLabel.show()[39;49;00m$
   878	  $
   879	  [37m# Add a (replace) text entry [39;49;00m$
   880	  [37m# - This Is only shown, when the 'Search & Replace'(CTRL + H) is shown[39;49;00m$
   881	  win.replaceEntry = entryNew()$
   882	  win.findBar.packStart(win.replaceEntry, [34mFalse[39;49;00m, [34mFalse[39;49;00m, [34m0[39;49;00m)$
   883	  [37m#win.replaceEntry.show()[39;49;00m$
   884	  [34mvar[39;49;00m rq1: TRequisition $
   885	  win.replaceEntry.sizeRequest([34maddr[39;49;00m(rq1))$
   886	$
   887	  [37m# Make the (replace) text entry longer[39;49;00m$
   888	  win.replaceEntry.set_size_request([34m100[39;49;00m, rq1.height)$
   889	  $
   890	  [37m# Find next button[39;49;00m$
   891	  [34mvar[39;49;00m nextBtn = buttonNew([33m"[39;49;00m[33mNext[39;49;00m[33m"[39;49;00m)$
   892	  win.findBar.packStart(nextBtn, [34mfalse[39;49;00m, [34mfalse[39;49;00m, [34m0[39;49;00m)$
   893	  [34mdiscard[39;49;00m nextBtn.signalConnect([33m"[39;49;00m[33mclicked[39;49;00m[33m"[39;49;00m, $
   894	             SIGNAL_FUNC(aporia.nextBtn_Clicked), [34mnil[39;49;00m)$
   895	  nextBtn.show()$
   896	  [34mvar[39;49;00m nxtBtnRq: TRequisition$
   897	  nextBtn.sizeRequest([34maddr[39;49;00m(nxtBtnRq))$
   898	  $
   899	  [37m# Find previous button[39;49;00m$
   900	  [34mvar[39;49;00m prevBtn = buttonNew([33m"[39;49;00m[33mPrevious[39;49;00m[33m"[39;49;00m)$
   901	  win.findBar.packStart(prevBtn, [34mfalse[39;49;00m, [34mfalse[39;49;00m, [34m0[39;49;00m)$
   902	  [34mdiscard[39;49;00m prevBtn.signalConnect([33m"[39;49;00m[33mclicked[39;49;00m[33m"[39;49;00m, $
   903	             SIGNAL_FUNC(aporia.prevBtn_Clicked), [34mnil[39;49;00m)$
   904	  prevBtn.show()$
   905	  $
   906	  [37m# Replace button[39;49;00m$
   907	  [37m# - This Is only shown, when the 'Search & Replace'(CTRL + H) is shown[39;49;00m$
   908	  win.replaceBtn = buttonNew([33m"[39;49;00m[33mReplace[39;49;00m[33m"[39;49;00m)$
   909	  win.findBar.packStart(win.replaceBtn, [34mfalse[39;49;00m, [34mfalse[39;49;00m, [34m0[39;49;00m)$
   910	  [34mdiscard[39;49;00m win.replaceBtn.signalConnect([33m"[39;49;00m[33mclicked[39;49;00m[33m"[39;49;00m, $
   911	             SIGNAL_FUNC(aporia.replaceBtn_Clicked), [34mnil[39;49;00m)$
   912	  [37m#replaceBtn.show()[39;49;00m$
   913	$
   914	  [37m# Replace all button[39;49;00m$
   915	  [37m# - this Is only shown, when the 'Search & Replace'(CTRL + H) is shown[39;49;00m$
   916	  win.replaceAllBtn = buttonNew([33m"[39;49;00m[33mReplace All[39;49;00m[33m"[39;49;00m)$
   917	  win.findBar.packStart(win.replaceAllBtn, [34mfalse[39;49;00m, [34mfalse[39;49;00m, [34m0[39;49;00m)$
   918	  [34mdiscard[39;49;00m win.replaceAllBtn.signalConnect([33m"[39;49;00m[33mclicked[39;49;00m[33m"[39;49;00m, $
   919	             SIGNAL_FUNC(aporia.replaceAllBtn_Clicked), [34mnil[39;49;00m)$
   920	  [37m#replaceAllBtn.show()[39;49;00m$
   921	  $
   922	  [37m# Right side ...[39;49;00m$
   923	  $
   924	  [37m# Close button - With a close stock image[39;49;00m$
   925	  [34mvar[39;49;00m closeBtn = buttonNew()$
   926	  [34mvar[39;49;00m closeImage = imageNewFromStock(STOCK_CLOSE, ICON_SIZE_SMALL_TOOLBAR)$
   927	  [34mvar[39;49;00m closeBox = hboxNew([34mFalse[39;49;00m, [34m0[39;49;00m)$
   928	  closeBtn.add(closeBox)$
   929	  closeBox.show()$
   930	  closeBox.add(closeImage)$
   931	  closeImage.show()$
   932	  [34mdiscard[39;49;00m closeBtn.signalConnect([33m"[39;49;00m[33mclicked[39;49;00m[33m"[39;49;00m, $
   933	             SIGNAL_FUNC(aporia.closeBtn_Clicked), [34mnil[39;49;00m)$
   934	  win.findBar.packEnd(closeBtn, [34mFalse[39;49;00m, [34mFalse[39;49;00m, [34m2[39;49;00m)$
   935	  closeBtn.show()$
   936	  $
   937	  [37m# Extra button - When clicked shows a menu with options like 'Use regex'[39;49;00m$
   938	  [34mvar[39;49;00m extraBtn = buttonNew()$
   939	  [34mvar[39;49;00m extraImage = imageNewFromStock(STOCK_PROPERTIES, ICON_SIZE_SMALL_TOOLBAR)$
   940	$
   941	  [34mvar[39;49;00m extraBox = hboxNew([34mFalse[39;49;00m, [34m0[39;49;00m)$
   942	  extraBtn.add(extraBox)$
   943	  extraBox.show()$
   944	  extraBox.add(extraImage)$
   945	  extraImage.show()$
   946	  [34mdiscard[39;49;00m extraBtn.signalConnect([33m"[39;49;00m[33mclicked[39;49;00m[33m"[39;49;00m, $
   947	             SIGNAL_FUNC(aporia.extraBtn_Clicked), [34mnil[39;49;00m)$
   948	  win.findBar.packEnd(extraBtn, [34mFalse[39;49;00m, [34mFalse[39;49;00m, [34m0[39;49;00m)$
   949	  extraBtn.show()$
   950	  $
   951	  MainBox.packStart(win.findBar, [34mFalse[39;49;00m, [34mFalse[39;49;00m, [34m0[39;49;00m)$
   952	  win.findBar.show()$
   953	$
   954	[34mproc [39;49;00m[32minitStatusBar[39;49;00m(MainBox: PBox) =$
   955	  win.bottomBar = statusbarNew()$
   956	  MainBox.packStart(win.bottomBar, [34mFalse[39;49;00m, [34mFalse[39;49;00m, [34m0[39;49;00m)$
   957	  win.bottomBar.show()$
   958	  $
   959	  [34mdiscard[39;49;00m win.bottomBar.push([34m0[39;49;00m, [33m"[39;49;00m[33mLine: 0 Column: 0[39;49;00m[33m"[39;49;00m)$
   960	  $
   961	[34mproc [39;49;00m[32minitControls[39;49;00m() =$
   962	  [37m# Load up the language style[39;49;00m$
   963	  win.langMan = languageManagerGetDefault()$
   964	  [34mvar[39;49;00m langpaths: [36marray[39;49;00m[[34m0[39;49;00m..[34m1[39;49;00m, cstring] = $
   965	          [cstring(os.getApplicationDir() / langSpecs), [34mnil[39;49;00m]$
   966	  win.langMan.setSearchPath([34maddr[39;49;00m(langpaths))$
   967	  [34mvar[39;49;00m nimLang = win.langMan.getLanguage([33m"[39;49;00m[33mnimrod[39;49;00m[33m"[39;49;00m)$
   968	  win.nimLang = nimLang$
   969	  $
   970	  [37m# Load the scheme[39;49;00m$
   971	  [34mvar[39;49;00m schemeMan = schemeManagerGetDefault()$
   972	  [34mvar[39;49;00m schemepaths: [36marray[39;49;00m[[34m0[39;49;00m..[34m1[39;49;00m, cstring] =$
   973	          [cstring(os.getApplicationDir() / styles), [34mnil[39;49;00m]$
   974	  schemeMan.setSearchPath([34maddr[39;49;00m(schemepaths))$
   975	  win.scheme = schemeMan.getScheme(win.settings.colorSchemeID)$
   976	  $
   977	  [37m# Window[39;49;00m$
   978	  win.w = windowNew(gtk2.WINDOW_TOPLEVEL)$
   979	  win.w.setDefaultSize(win.settings.winWidth, win.settings.winHeight)$
   980	  win.w.setTitle([33m"[39;49;00m[33mAporia IDE[39;49;00m[33m"[39;49;00m)$
   981	  [34mif[39;49;00m win.settings.winMaximized: win.w.maximize()$
   982	  $
   983	  win.w.show() [37m# The window has to be shown before[39;49;00m$
   984	               [37m# setting the position of the VPaned so that[39;49;00m$
   985	               [37m# it gets set correctly, when the window is maximized.[39;49;00m$
   986	    $
   987	  [34mdiscard[39;49;00m win.w.signalConnect([33m"[39;49;00m[33mdestroy[39;49;00m[33m"[39;49;00m, SIGNAL_FUNC(aporia.destroy), [34mnil[39;49;00m)$
   988	  [34mdiscard[39;49;00m win.w.signalConnect([33m"[39;49;00m[33mdelete_event[39;49;00m[33m"[39;49;00m, $
   989	    SIGNAL_FUNC(aporia.delete_event), [34mnil[39;49;00m)$
   990	  [34mdiscard[39;49;00m win.w.signalConnect([33m"[39;49;00m[33mwindow-state-event[39;49;00m[33m"[39;49;00m, $
   991	    SIGNAL_FUNC(aporia.windowState_Changed), [34mnil[39;49;00m)$
   992	  $
   993	  [37m# MainBox (vbox)[39;49;00m$
   994	  [34mvar[39;49;00m MainBox = vboxNew([34mFalse[39;49;00m, [34m0[39;49;00m)$
   995	  win.w.add(MainBox)$
   996	  $
   997	  initTopMenu(MainBox)$
   998	  initToolBar(MainBox)$
   999	  initTAndBP(MainBox)$
  1000	  initFindBar(MainBox)$
  1001	  initStatusBar(MainBox)$
  1002	  $
  1003	  MainBox.show()$
  1004	  [34mif[39;49;00m confParseFail:$
  1005	    dialogs.warning(win.w, [33m"[39;49;00m[33mError parsing config file, using default settings.[39;49;00m[33m"[39;49;00m)$
  1006	 $
  1007	nimrod_init()$
  1008	initControls()$
  1009	main()$

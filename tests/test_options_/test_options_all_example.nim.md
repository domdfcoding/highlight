     1^I[34mimport[39;49;00m glib2, gtk2, gdk2, gtksourceview, dialogs, os, pango, osproc, strutils$
     2^I[34mimport[39;49;00m pegs, streams$
     3^I[34mimport[39;49;00m settings, types, cfg, search$
     4^I$
     5^I{.push callConv:cdecl.}$
     6^I$
     7^I[34mconst[39;49;00m$
     8^I  NimrodProjectExt = [33m"[39;49;00m[33m.nimprj[39;49;00m[33m"[39;49;00m$
     9^I$
    10^I[34mvar[39;49;00m win: types.MainWin$
    11^Iwin.Tabs = @[]$
    12^I$
    13^Isearch.win = [34maddr[39;49;00m(win)$
    14^I$
    15^I[34mvar[39;49;00m lastSession: [36mseq[39;49;00m[[36mstring[39;49;00m] = @[]$
    16^I$
    17^I[34mvar[39;49;00m confParseFail = [34mFalse[39;49;00m [37m# This gets set to true[39;49;00m$
    18^I                          [37m# When there is an error parsing the config[39;49;00m$
    19^I$
    20^I[37m# Load the settings[39;49;00m$
    21^I[34mtry[39;49;00m:$
    22^I  win.settings = cfg.load(lastSession)$
    23^I[34mexcept[39;49;00m ECFGParse:$
    24^I  [37m# TODO: Make the dialog show the exception[39;49;00m$
    25^I  confParseFail = [34mTrue[39;49;00m$
    26^I  win.settings = cfg.defaultSettings()$
    27^I[34mexcept[39;49;00m EIO:$
    28^I  win.settings = cfg.defaultSettings()$
    29^I$
    30^I[34mproc [39;49;00m[32mgetProjectTab[39;49;00m(): [36mint[39;49;00m = $
    31^I  [34mfor[39;49;00m i [35min[39;49;00m [34m0[39;49;00m..high(win.tabs): $
    32^I    [34mif[39;49;00m win.tabs[i].filename.endswith(NimrodProjectExt): [34mreturn[39;49;00m i$
    33^I$
    34^I[34mproc [39;49;00m[32msaveTab[39;49;00m(tabNr: [36mint[39;49;00m, startpath: [36mstring[39;49;00m) =$
    35^I  [34mif[39;49;00m tabNr < [34m0[39;49;00m: [34mreturn[39;49;00m$
    36^I  [34mif[39;49;00m win.Tabs[tabNr].saved: [34mreturn[39;49;00m$
    37^I  [34mvar[39;49;00m path = [33m"[39;49;00m[33m"[39;49;00m$
    38^I  [34mif[39;49;00m win.Tabs[tabNr].filename == [33m"[39;49;00m[33m"[39;49;00m:$
    39^I    path = ChooseFileToSave(win.w, startpath) $
    40^I    [37m# dialogs.nim STOCK_OPEN instead of STOCK_SAVE[39;49;00m$
    41^I  [34melse[39;49;00m: $
    42^I    path = win.Tabs[tabNr].filename$
    43^I  $
    44^I  [34mif[39;49;00m path != [33m"[39;49;00m[33m"[39;49;00m:$
    45^I    [34mvar[39;49;00m buffer = PTextBuffer(win.Tabs[tabNr].buffer)$
    46^I    [37m# Get the text from the TextView[39;49;00m$
    47^I    [34mvar[39;49;00m startIter: TTextIter$
    48^I    buffer.getStartIter([34maddr[39;49;00m(startIter))$
    49^I    $
    50^I    [34mvar[39;49;00m endIter: TTextIter$
    51^I    buffer.getEndIter([34maddr[39;49;00m(endIter))$
    52^I    $
    53^I    [34mvar[39;49;00m text = buffer.getText([34maddr[39;49;00m(startIter), [34maddr[39;49;00m(endIter), [34mFalse[39;49;00m)$
    54^I    [37m# Save it to a file[39;49;00m$
    55^I    [34mvar[39;49;00m f: TFile$
    56^I    [34mif[39;49;00m open(f, path, fmWrite):$
    57^I      f.write(text)$
    58^I      f.close()$
    59^I      $
    60^I      win.tempStuff.lastSaveDir = splitFile(path).dir$
    61^I      $
    62^I      [37m# Change the tab name and .Tabs.filename etc.[39;49;00m$
    63^I      win.Tabs[tabNr].filename = path$
    64^I      win.Tabs[tabNr].saved = [34mTrue[39;49;00m$
    65^I      [34mvar[39;49;00m name = extractFilename(path)$
    66^I      $
    67^I      [34mvar[39;49;00m cTab = win.Tabs[tabNr]$
    68^I      cTab.label.setText(name)$
    69^I    [34melse[39;49;00m:$
    70^I      error(win.w, [33m"[39;49;00m[33mUnable to write to file[39;49;00m[33m"[39;49;00m)  $
    71^I$
    72^I[34mproc [39;49;00m[32msaveAllTabs[39;49;00m() =$
    73^I  [34mfor[39;49;00m i [35min[39;49;00m [34m0[39;49;00m..high(win.tabs): $
    74^I    saveTab(i, os.splitFile(win.tabs[i].filename).dir)$
    75^I$
    76^I[37m# GTK Events[39;49;00m$
    77^I[37m# -- w(PWindow)[39;49;00m$
    78^I[34mproc [39;49;00m[32mdestroy[39;49;00m(widget: PWidget, data: pgpointer) {.cdecl.} =$
    79^I  [37m# gather some settings[39;49;00m$
    80^I  win.settings.VPanedPos = PPaned(win.sourceViewTabs.getParent()).getPosition()$
    81^I  win.settings.winWidth = win.w.allocation.width$
    82^I  win.settings.winHeight = win.w.allocation.height$
    83^I$
    84^I  [37m# save the settings[39;49;00m$
    85^I  win.save()$
    86^I  [37m# then quit[39;49;00m$
    87^I  main_quit()$
    88^I$
    89^I[34mproc [39;49;00m[32mdelete_event[39;49;00m(widget: PWidget, event: PEvent, user_data: pgpointer): [36mbool[39;49;00m =$
    90^I  [34mvar[39;49;00m quit = [34mTrue[39;49;00m$
    91^I  [34mfor[39;49;00m i [35min[39;49;00m low(win.Tabs)..len(win.Tabs)-[34m1[39;49;00m:$
    92^I    [34mif[39;49;00m [35mnot[39;49;00m win.Tabs[i].saved:$
    93^I      [34mvar[39;49;00m askSave = dialogNewWithButtons([33m"[39;49;00m[33m"[39;49;00m, win.w, [34m0[39;49;00m,$
    94^I                            STOCK_SAVE, RESPONSE_ACCEPT, STOCK_CANCEL, $
    95^I                            RESPONSE_CANCEL,$
    96^I                            [33m"[39;49;00m[33mClose without saving[39;49;00m[33m"[39;49;00m, RESPONSE_REJECT, [34mnil[39;49;00m)$
    97^I      askSave.setTransientFor(win.w)$
    98^I      [37m# TODO: Make this dialog look better[39;49;00m$
    99^I      [34mvar[39;49;00m label = labelNew(win.Tabs[i].filename & $
   100^I          [33m"[39;49;00m[33m is unsaved, would you like to save it ?[39;49;00m[33m"[39;49;00m)$
   101^I      PBox(askSave.vbox).pack_start(label, [34mFalse[39;49;00m, [34mFalse[39;49;00m, [34m0[39;49;00m)$
   102^I      label.show()$
   103^I$
   104^I      [34mvar[39;49;00m resp = askSave.run()$
   105^I      gtk2.destroy(PWidget(askSave))$
   106^I      [34mcase[39;49;00m resp$
   107^I      [34mof[39;49;00m RESPONSE_ACCEPT:$
   108^I        saveTab(i, os.splitFile(win.tabs[i].filename).dir)$
   109^I        quit = [34mTrue[39;49;00m$
   110^I      [34mof[39;49;00m RESPONSE_CANCEL:$
   111^I        quit = [34mFalse[39;49;00m$
   112^I        [34mbreak[39;49;00m$
   113^I      [34mof[39;49;00m RESPONSE_REJECT:$
   114^I        quit = [34mTrue[39;49;00m$
   115^I      [34melse[39;49;00m:$
   116^I        quit = [34mFalse[39;49;00m$
   117^I        [34mbreak[39;49;00m$
   118^I$
   119^I  [37m# If False is returned the window will close[39;49;00m$
   120^I  [34mreturn[39;49;00m [35mnot[39;49;00m quit$
   121^I$
   122^I[34mproc [39;49;00m[32mwindowState_Changed[39;49;00m(widget: PWidget, event: PEventWindowState, $
   123^I                         user_data: pgpointer) =$
   124^I  win.settings.winMaximized = (event.newWindowState [35mand[39;49;00m $
   125^I                               WINDOW_STATE_MAXIMIZED) != [34m0[39;49;00m$
   126^I$
   127^I[37m# -- SourceView(PSourceView) & SourceBuffer[39;49;00m$
   128^I[34mproc [39;49;00m[32mupdateStatusBar[39;49;00m(buffer: PTextBuffer){.cdecl.} =$
   129^I  [37m# Incase this event gets fired before[39;49;00m$
   130^I  [37m# bottomBar is initialized[39;49;00m$
   131^I  [34mif[39;49;00m win.bottomBar != [34mnil[39;49;00m [35mand[39;49;00m [35mnot[39;49;00m win.tempStuff.stopSBUpdates:  $
   132^I    [34mvar[39;49;00m iter: TTextIter$
   133^I    $
   134^I    win.bottomBar.pop([34m0[39;49;00m)$
   135^I    buffer.getIterAtMark([34maddr[39;49;00m(iter), buffer.getInsert())$
   136^I    [34mvar[39;49;00m row = getLine([34maddr[39;49;00m(iter)) + [34m1[39;49;00m$
   137^I    [34mvar[39;49;00m col = getLineOffset([34maddr[39;49;00m(iter))$
   138^I    [34mdiscard[39;49;00m win.bottomBar.push([34m0[39;49;00m, [33m"[39;49;00m[33mLine: [39;49;00m[33m"[39;49;00m & $row & [33m"[39;49;00m[33m Column: [39;49;00m[33m"[39;49;00m & $col)$
   139^I  $
   140^I[34mproc [39;49;00m[32mcursorMoved[39;49;00m(buffer: PTextBuffer, location: PTextIter, $
   141^I                 mark: PTextMark, user_data: pgpointer){.cdecl.} =$
   142^I  updateStatusBar(buffer)$
   143^I$
   144^I[34mproc [39;49;00m[32monCloseTab[39;49;00m(btn: PButton, user_data: PWidget) =$
   145^I  [34mif[39;49;00m win.sourceViewTabs.getNPages() > [34m1[39;49;00m:$
   146^I    [34mvar[39;49;00m tab = win.sourceViewTabs.pageNum(user_data)$
   147^I    win.sourceViewTabs.removePage(tab)$
   148^I$
   149^I    win.Tabs.delete(tab)$
   150^I$
   151^I[34mproc [39;49;00m[32monSwitchTab[39;49;00m(notebook: PNotebook, page: PNotebookPage, pageNum: guint, $
   152^I                 user_data: pgpointer) =$
   153^I  [34mif[39;49;00m win.Tabs.len()-[34m1[39;49;00m >= pageNum:$
   154^I    win.w.setTitle([33m"[39;49;00m[33mAporia IDE - [39;49;00m[33m"[39;49;00m & win.Tabs[pageNum].filename)$
   155^I$
   156^I[34mproc [39;49;00m[32mcreateTabLabel[39;49;00m(name: [36mstring[39;49;00m, t_child: PWidget): [34mtuple[39;49;00m[box: PWidget,$
   157^I                    label: PLabel] =$
   158^I  [34mvar[39;49;00m box = hboxNew([34mFalse[39;49;00m, [34m0[39;49;00m)$
   159^I  [34mvar[39;49;00m label = labelNew(name)$
   160^I  [34mvar[39;49;00m closebtn = buttonNew()$
   161^I  closeBtn.setLabel([34mnil[39;49;00m)$
   162^I  [34mvar[39;49;00m iconSize = iconSizeFromName([33m"[39;49;00m[33mtabIconSize[39;49;00m[33m"[39;49;00m)$
   163^I  [34mif[39;49;00m iconSize == [34m0[39;49;00m:$
   164^I     iconSize = iconSizeRegister([33m"[39;49;00m[33mtabIconSize[39;49;00m[33m"[39;49;00m, [34m10[39;49;00m, [34m10[39;49;00m)$
   165^I  [34mvar[39;49;00m image = imageNewFromStock(STOCK_CLOSE, iconSize)$
   166^I  [34mdiscard[39;49;00m gSignalConnect(closebtn, [33m"[39;49;00m[33mclicked[39;49;00m[33m"[39;49;00m, G_Callback(onCloseTab), t_child)$
   167^I  closebtn.setImage(image)$
   168^I  gtk2.setRelief(closebtn, RELIEF_NONE)$
   169^I  box.packStart(label, [34mTrue[39;49;00m, [34mTrue[39;49;00m, [34m0[39;49;00m)$
   170^I  box.packEnd(closebtn, [34mFalse[39;49;00m, [34mFalse[39;49;00m, [34m0[39;49;00m)$
   171^I  box.showAll()$
   172^I  [34mreturn[39;49;00m (box, label)$
   173^I$
   174^I[34mproc [39;49;00m[32mchanged[39;49;00m(buffer: PTextBuffer, user_data: pgpointer) =$
   175^I  [37m# Update the 'Line & Column'[39;49;00m$
   176^I  [37m#updateStatusBar(buffer)[39;49;00m$
   177^I$
   178^I  [37m# Change the tabs state to 'unsaved'[39;49;00m$
   179^I  [37m# and add '*' to the Tab Name[39;49;00m$
   180^I  [34mvar[39;49;00m current = win.SourceViewTabs.getCurrentPage()$
   181^I  [34mvar[39;49;00m name = [33m"[39;49;00m[33m"[39;49;00m$
   182^I  [34mif[39;49;00m win.Tabs[current].filename == [33m"[39;49;00m[33m"[39;49;00m:$
   183^I    win.Tabs[current].saved = [34mFalse[39;49;00m$
   184^I    name = [33m"[39;49;00m[33mUntitled *[39;49;00m[33m"[39;49;00m$
   185^I  [34melse[39;49;00m:$
   186^I    win.Tabs[current].saved = [34mFalse[39;49;00m$
   187^I    name = extractFilename(win.Tabs[current].filename) & [33m"[39;49;00m[33m *[39;49;00m[33m"[39;49;00m$
   188^I  $
   189^I  [34mvar[39;49;00m cTab = win.Tabs[current]$
   190^I  cTab.label.setText(name)$
   191^I$
   192^I[37m# Other(Helper) functions[39;49;00m$
   193^I$
   194^I[34mproc [39;49;00m[32minitSourceView[39;49;00m(SourceView: [34mvar[39;49;00m PWidget, scrollWindow: [34mvar[39;49;00m PScrolledWindow,$
   195^I                    buffer: [34mvar[39;49;00m PSourceBuffer) =$
   196^I  [37m# This gets called by addTab[39;49;00m$
   197^I  [37m# Each tabs creates a new SourceView[39;49;00m$
   198^I  [37m# SourceScrolledWindow(ScrolledWindow)[39;49;00m$
   199^I  scrollWindow = scrolledWindowNew([34mnil[39;49;00m, [34mnil[39;49;00m)$
   200^I  scrollWindow.setPolicy(POLICY_AUTOMATIC, POLICY_AUTOMATIC)$
   201^I  scrollWindow.show()$
   202^I  $
   203^I  [37m# SourceView(gtkSourceView)[39;49;00m$
   204^I  SourceView = sourceViewNew(buffer)$
   205^I  PSourceView(SourceView).setInsertSpacesInsteadOfTabs([34mTrue[39;49;00m)$
   206^I  PSourceView(SourceView).setIndentWidth(win.settings.indentWidth)$
   207^I  PSourceView(SourceView).setShowLineNumbers(win.settings.showLineNumbers)$
   208^I  PSourceView(SourceView).setHighlightCurrentLine($
   209^I               win.settings.highlightCurrentLine)$
   210^I  PSourceView(SourceView).setShowRightMargin(win.settings.rightMargin)$
   211^I  PSourceView(SourceView).setAutoIndent(win.settings.autoIndent)$
   212^I$
   213^I  [34mvar[39;49;00m font = font_description_from_string(win.settings.font)$
   214^I  SourceView.modifyFont(font)$
   215^I  $
   216^I  scrollWindow.add(SourceView)$
   217^I  SourceView.show()$
   218^I$
   219^I  buffer.setHighlightMatchingBrackets($
   220^I      win.settings.highlightMatchingBrackets)$
   221^I  $
   222^I  [37m# UGLY workaround for yet another compiler bug:[39;49;00m$
   223^I  [34mdiscard[39;49;00m gsignalConnect(buffer, [33m"[39;49;00m[33mmark-set[39;49;00m[33m"[39;49;00m, $
   224^I                         GCallback(aporia.cursorMoved), [34mnil[39;49;00m)$
   225^I  [34mdiscard[39;49;00m gsignalConnect(buffer, [33m"[39;49;00m[33mchanged[39;49;00m[33m"[39;49;00m, GCallback(aporia.changed), [34mnil[39;49;00m)$
   226^I$
   227^I  [37m# -- Set the syntax highlighter scheme[39;49;00m$
   228^I  buffer.setScheme(win.scheme)$
   229^I$
   230^I[34mproc [39;49;00m[32maddTab[39;49;00m(name, filename: [36mstring[39;49;00m) =$
   231^I  [33m## Adds a tab, if filename is not "" reads the file. And sets[39;49;00m$
   232^I  [33m## the tabs SourceViews text to that files contents.[39;49;00m$
   233^I  assert(win.nimLang != [34mnil[39;49;00m)$
   234^I  [34mvar[39;49;00m buffer: PSourceBuffer = sourceBufferNew(win.nimLang)$
   235^I$
   236^I  [34mif[39;49;00m filename != [34mnil[39;49;00m [35mand[39;49;00m filename != [33m"[39;49;00m[33m"[39;49;00m:$
   237^I    [34mvar[39;49;00m lang = win.langMan.guessLanguage(filename, [34mnil[39;49;00m)$
   238^I    [34mif[39;49;00m lang != [34mnil[39;49;00m:$
   239^I      buffer.setLanguage(lang)$
   240^I    [34melse[39;49;00m:$
   241^I      buffer.setHighlightSyntax([34mFalse[39;49;00m)$
   242^I$
   243^I  [34mvar[39;49;00m nam = name$
   244^I  [34mif[39;49;00m nam == [33m"[39;49;00m[33m"[39;49;00m: nam = [33m"[39;49;00m[33mUntitled[39;49;00m[33m"[39;49;00m$
   245^I  [34mif[39;49;00m filename == [33m"[39;49;00m[33m"[39;49;00m: nam.add([33m"[39;49;00m[33m *[39;49;00m[33m"[39;49;00m)$
   246^I  [34melif[39;49;00m filename != [33m"[39;49;00m[33m"[39;49;00m [35mand[39;49;00m name == [33m"[39;49;00m[33m"[39;49;00m:$
   247^I    [37m# Disable the undo/redo manager.[39;49;00m$
   248^I    buffer.begin_not_undoable_action()$
   249^I  $
   250^I    [37m# Load the file.[39;49;00m$
   251^I    [34mvar[39;49;00m file: [36mstring[39;49;00m = readFile(filename)$
   252^I    [34mif[39;49;00m file != [34mnil[39;49;00m:$
   253^I      buffer.set_text(file, len(file))$
   254^I      $
   255^I    [37m# Enable the undo/redo manager.[39;49;00m$
   256^I    buffer.end_not_undoable_action()$
   257^I      $
   258^I    [37m# Get the name.ext of the filename, for the tabs title[39;49;00m$
   259^I    nam = extractFilename(filename)$
   260^I  $
   261^I  [37m# Init the sourceview[39;49;00m$
   262^I  [34mvar[39;49;00m sourceView: PWidget$
   263^I  [34mvar[39;49;00m scrollWindow: PScrolledWindow$
   264^I  initSourceView(sourceView, scrollWindow, buffer)$
   265^I$
   266^I  [34mvar[39;49;00m (TabLabel, labelText) = createTabLabel(nam, scrollWindow)$
   267^I  [37m# Add a tab[39;49;00m$
   268^I  [34mdiscard[39;49;00m win.SourceViewTabs.appendPage(scrollWindow, TabLabel)$
   269^I$
   270^I  [34mvar[39;49;00m nTab: Tab$
   271^I  nTab.buffer = buffer$
   272^I  nTab.sourceView = sourceView$
   273^I  nTab.label = labelText$
   274^I  nTab.saved = (filename != [33m"[39;49;00m[33m"[39;49;00m)$
   275^I  nTab.filename = filename$
   276^I  win.Tabs.add(nTab)$
   277^I$
   278^I  PTextView(SourceView).setBuffer(nTab.buffer)$
   279^I$
   280^I[37m# GTK Events Contd.[39;49;00m$
   281^I[37m# -- TopMenu & TopBar[39;49;00m$
   282^I$
   283^I[34mproc [39;49;00m[32mnewFile[39;49;00m(menuItem: PMenuItem, user_data: pgpointer) =$
   284^I  addTab([33m"[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33m"[39;49;00m)$
   285^I  win.sourceViewTabs.setCurrentPage(win.Tabs.len()-[34m1[39;49;00m)$
   286^I  $
   287^I[34mproc [39;49;00m[32mopenFile[39;49;00m(menuItem: PMenuItem, user_data: pgpointer) =$
   288^I  [34mvar[39;49;00m startpath = [33m"[39;49;00m[33m"[39;49;00m$
   289^I  [34mvar[39;49;00m currPage = win.SourceViewTabs.getCurrentPage()$
   290^I  [34mif[39;49;00m currPage <% win.tabs.len: $
   291^I    startpath = os.splitFile(win.tabs[currPage].filename).dir$
   292^I$
   293^I  [34mif[39;49;00m startpath.len == [34m0[39;49;00m:$
   294^I    [37m# Use lastSavePath as the startpath[39;49;00m$
   295^I    startpath = win.tempStuff.lastSaveDir$
   296^I    [34mif[39;49;00m startpath.len == [34m0[39;49;00m:$
   297^I      startpath = os.getHomeDir()$
   298^I$
   299^I  [34mvar[39;49;00m files = ChooseFilesToOpen(win.w, startpath)$
   300^I  [34mif[39;49;00m files.len() > [34m0[39;49;00m:$
   301^I    [34mfor[39;49;00m f [35min[39;49;00m items(files):$
   302^I      [34mtry[39;49;00m:$
   303^I        addTab([33m"[39;49;00m[33m"[39;49;00m, f)$
   304^I      [34mexcept[39;49;00m EIO:$
   305^I        error(win.w, [33m"[39;49;00m[33mUnable to read from file[39;49;00m[33m"[39;49;00m)$
   306^I    [37m# Switch to the newly created tab[39;49;00m$
   307^I    win.sourceViewTabs.setCurrentPage(win.Tabs.len()-[34m1[39;49;00m)$
   308^I  $
   309^I[34mproc [39;49;00m[32msaveFile_Activate[39;49;00m(menuItem: PMenuItem, user_data: pgpointer) =$
   310^I  [34mvar[39;49;00m current = win.SourceViewTabs.getCurrentPage()$
   311^I  saveTab(current, os.splitFile(win.tabs[current].filename).dir)$
   312^I$
   313^I[34mproc [39;49;00m[32msaveFileAs_Activate[39;49;00m(menuItem: PMenuItem, user_data: pgpointer) =$
   314^I  [34mvar[39;49;00m current = win.SourceViewTabs.getCurrentPage()$
   315^I  [34mvar[39;49;00m (filename, saved) = (win.Tabs[current].filename, win.Tabs[current].saved)$
   316^I$
   317^I  win.Tabs[current].saved = [34mFalse[39;49;00m$
   318^I  win.Tabs[current].filename = [33m"[39;49;00m[33m"[39;49;00m$
   319^I  saveTab(current, os.splitFile(filename).dir)$
   320^I  [37m# If the user cancels the save file dialog. Restore the previous filename[39;49;00m$
   321^I  [37m# and saved state[39;49;00m$
   322^I  [34mif[39;49;00m win.Tabs[current].filename == [33m"[39;49;00m[33m"[39;49;00m:$
   323^I    win.Tabs[current].filename = filename$
   324^I    win.Tabs[current].saved = saved$
   325^I$
   326^I[34mproc [39;49;00m[32mundo[39;49;00m(menuItem: PMenuItem, user_data: pgpointer) = $
   327^I  [34mvar[39;49;00m current = win.SourceViewTabs.getCurrentPage()$
   328^I  [34mif[39;49;00m win.Tabs[current].buffer.canUndo():$
   329^I    win.Tabs[current].buffer.undo()$
   330^I  $
   331^I[34mproc [39;49;00m[32mredo[39;49;00m(menuItem: PMenuItem, user_data: pgpointer) =$
   332^I  [34mvar[39;49;00m current = win.SourceViewTabs.getCurrentPage()$
   333^I  [34mif[39;49;00m win.Tabs[current].buffer.canRedo():$
   334^I    win.Tabs[current].buffer.redo()$
   335^I    $
   336^I[34mproc [39;49;00m[32mfind_Activate[39;49;00m(menuItem: PMenuItem, user_data: pgpointer) = $
   337^I  [37m# Get the selected text, and set the findEntry to it.[39;49;00m$
   338^I  [34mvar[39;49;00m currentTab = win.SourceViewTabs.getCurrentPage()$
   339^I  [34mvar[39;49;00m insertIter: TTextIter$
   340^I  win.Tabs[currentTab].buffer.getIterAtMark([34maddr[39;49;00m(insertIter), $
   341^I                                      win.Tabs[currentTab].buffer.getInsert())$
   342^I  [34mvar[39;49;00m insertOffset = [34maddr[39;49;00m(insertIter).getOffset()$
   343^I  $
   344^I  [34mvar[39;49;00m selectIter: TTextIter$
   345^I  win.Tabs[currentTab].buffer.getIterAtMark([34maddr[39;49;00m(selectIter), $
   346^I                win.Tabs[currentTab].buffer.getSelectionBound())$
   347^I  [34mvar[39;49;00m selectOffset = [34maddr[39;49;00m(selectIter).getOffset()$
   348^I  $
   349^I  [34mif[39;49;00m insertOffset != selectOffset:$
   350^I    [34mvar[39;49;00m text = win.Tabs[currentTab].buffer.getText([34maddr[39;49;00m(insertIter), $
   351^I                                                   [34maddr[39;49;00m(selectIter), [34mfalse[39;49;00m)$
   352^I    win.findEntry.setText(text)$
   353^I$
   354^I  win.findBar.show()$
   355^I  win.findEntry.grabFocus()$
   356^I  win.replaceEntry.hide()$
   357^I  win.replaceLabel.hide()$
   358^I  win.replaceBtn.hide()$
   359^I  win.replaceAllBtn.hide()$
   360^I$
   361^I[34mproc [39;49;00m[32mreplace_Activate[39;49;00m(menuitem: PMenuItem, user_data: pgpointer) =$
   362^I  win.findBar.show()$
   363^I  win.findEntry.grabFocus()$
   364^I  win.replaceEntry.show()$
   365^I  win.replaceLabel.show()$
   366^I  win.replaceBtn.show()$
   367^I  win.replaceAllBtn.show()$
   368^I  $
   369^I[34mproc [39;49;00m[32msettings_Activate[39;49;00m(menuitem: PMenuItem, user_data: pgpointer) =$
   370^I  settings.showSettings(win)$
   371^I  $
   372^I[34mproc [39;49;00m[32mviewBottomPanel_Toggled[39;49;00m(menuitem: PCheckMenuItem, user_data: pgpointer) =$
   373^I  win.settings.bottomPanelVisible = menuitem.itemGetActive()$
   374^I  [34mif[39;49;00m win.settings.bottomPanelVisible:$
   375^I    win.bottomPanelTabs.show()$
   376^I  [34melse[39;49;00m:$
   377^I    win.bottomPanelTabs.hide()$
   378^I$
   379^I[34mvar[39;49;00m$
   380^I  pegLineError = [33mpeg"[39;49;00m[33m{[^(]*} [39;49;00m[33m'[39;49;00m[33m([39;49;00m[33m'[39;49;00m[33m {[39;49;00m[33m\[39;49;00m[33md+} [39;49;00m[33m'[39;49;00m[33m, [39;49;00m[33m'[39;49;00m[33m [39;49;00m[33m\[39;49;00m[33md+ [39;49;00m[33m'[39;49;00m[33m) Error:[39;49;00m[33m'[39;49;00m[33m [39;49;00m[33m\[39;49;00m[33ms* {.*}[39;49;00m[33m"[39;49;00m$
   381^I  pegLineWarning = [33mpeg"[39;49;00m[33m{[^(]*} [39;49;00m[33m'[39;49;00m[33m([39;49;00m[33m'[39;49;00m[33m {[39;49;00m[33m\[39;49;00m[33md+} [39;49;00m[33m'[39;49;00m[33m, [39;49;00m[33m'[39;49;00m[33m [39;49;00m[33m\[39;49;00m[33md+ [39;49;00m[33m'[39;49;00m[33m) [39;49;00m[33m'[39;49;00m[33m ([39;49;00m[33m'[39;49;00m[33mWarning:[39;49;00m[33m'[39;49;00m[33m/[39;49;00m[33m'[39;49;00m[33mHint:[39;49;00m[33m'[39;49;00m[33m) [39;49;00m[33m\[39;49;00m[33ms* {.*}[39;49;00m[33m"[39;49;00m$
   382^I  pegOtherError = [33mpeg"[39;49;00m[33m'[39;49;00m[33mError:[39;49;00m[33m'[39;49;00m[33m [39;49;00m[33m\[39;49;00m[33ms* {.*}[39;49;00m[33m"[39;49;00m$
   383^I  pegSuccess = [33mpeg"[39;49;00m[33m'[39;49;00m[33mHint: operation successful[39;49;00m[33m'[39;49;00m[33m.*[39;49;00m[33m"[39;49;00m$
   384^I$
   385^I[34mproc [39;49;00m[32maddText[39;49;00m(textView: PTextView, text: [36mstring[39;49;00m, colorTag: PTextTag = [34mnil[39;49;00m) =$
   386^I  [34mif[39;49;00m text != [34mnil[39;49;00m:$
   387^I    [34mvar[39;49;00m iter: TTextIter$
   388^I    textView.getBuffer().getEndIter([34maddr[39;49;00m(iter))$
   389^I$
   390^I    [34mif[39;49;00m colorTag == [34mnil[39;49;00m:$
   391^I      textView.getBuffer().insert([34maddr[39;49;00m(iter), text, len(text))$
   392^I    [34melse[39;49;00m:$
   393^I      textView.getBuffer().insertWithTags([34maddr[39;49;00m(iter), text, len(text), colorTag,$
   394^I                                          [34mnil[39;49;00m)$
   395^I$
   396^I[34mproc [39;49;00m[32mcreateColor[39;49;00m(textView: PTextView, name, color: [36mstring[39;49;00m): PTextTag =$
   397^I  [34mvar[39;49;00m tagTable = textView.getBuffer().getTagTable()$
   398^I  result = tagTable.tableLookup(name)$
   399^I  [34mif[39;49;00m result == [34mnil[39;49;00m:$
   400^I    result = textView.getBuffer().createTag(name, [33m"[39;49;00m[33mforeground[39;49;00m[33m"[39;49;00m, color, [34mnil[39;49;00m)$
   401^I$
   402^I[34mwhen[39;49;00m [35mnot[39;49;00m defined(os.findExe): $
   403^I  [34mproc [39;49;00m[32mfindExe[39;49;00m(exe: [36mstring[39;49;00m): [36mstring[39;49;00m = $
   404^I    [33m## returns "" if the exe cannot be found[39;49;00m$
   405^I    result = addFileExt(exe, os.exeExt)$
   406^I    [34mif[39;49;00m ExistsFile(result): [34mreturn[39;49;00m$
   407^I    [34mvar[39;49;00m path = os.getEnv([33m"[39;49;00m[33mPATH[39;49;00m[33m"[39;49;00m)$
   408^I    [34mfor[39;49;00m candidate [35min[39;49;00m split(path, pathSep): $
   409^I      [34mvar[39;49;00m x = candidate / result$
   410^I      [34mif[39;49;00m ExistsFile(x): [34mreturn[39;49;00m x$
   411^I    result = [33m"[39;49;00m[33m"[39;49;00m$
   412^I$
   413^I[34mproc [39;49;00m[32mGetCmd[39;49;00m(cmd, filename: [36mstring[39;49;00m): [36mstring[39;49;00m = $
   414^I  [34mvar[39;49;00m f = quoteIfContainsWhite(filename)$
   415^I  [34mif[39;49;00m cmd =~ [33mpeg"[39;49;00m[33m\[39;49;00m[33ms* [39;49;00m[33m'[39;49;00m[33m$[39;49;00m[33m'[39;49;00m[33m y[39;49;00m[33m'[39;49;00m[33mfindExe[39;49;00m[33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m[33m([39;49;00m[33m'[39;49;00m[33m {[^)]+} [39;49;00m[33m'[39;49;00m[33m)[39;49;00m[33m'[39;49;00m[33m {.*}[39;49;00m[33m"[39;49;00m:$
   416^I    [34mvar[39;49;00m exe = quoteIfContainsWhite(findExe(matches[[34m0[39;49;00m]))$
   417^I    [34mif[39;49;00m exe.len == [34m0[39;49;00m: exe = matches[[34m0[39;49;00m]$
   418^I    result = exe & [33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m & matches[[34m1[39;49;00m] % f$
   419^I  [34melse[39;49;00m:$
   420^I    result = cmd % f$
   421^I$
   422^I[34mproc [39;49;00m[32mshowBottomPanel[39;49;00m() =$
   423^I  [34mif[39;49;00m [35mnot[39;49;00m win.settings.bottomPanelVisible:$
   424^I    win.bottomPanelTabs.show()$
   425^I    win.settings.bottomPanelVisible = [34mtrue[39;49;00m$
   426^I    PCheckMenuItem(win.viewBottomPanelMenuItem).itemSetActive([34mtrue[39;49;00m)$
   427^I  [37m# Scroll to the end of the TextView[39;49;00m$
   428^I  [37m# This is stupid, it works sometimes... it's random[39;49;00m$
   429^I  [34mvar[39;49;00m endIter: TTextIter$
   430^I  win.outputTextView.getBuffer().getEndIter([34maddr[39;49;00m(endIter))$
   431^I  [34mdiscard[39;49;00m win.outputTextView.scrollToIter($
   432^I    [34maddr[39;49;00m(endIter), [34m0[39;49;00m[34m.25[39;49;00m, [34mFalse[39;49;00m, [34m0[39;49;00m[34m.0[39;49;00m, [34m0[39;49;00m[34m.0[39;49;00m)$
   433^I$
   434^I[34mproc [39;49;00m[32mcompileRun[39;49;00m(currentTab: [36mint[39;49;00m, shouldRun: [36mbool[39;49;00m) =$
   435^I  [34mif[39;49;00m win.Tabs[currentTab].filename.len == [34m0[39;49;00m: [34mreturn[39;49;00m$
   436^I  [37m# Clear the outputTextView[39;49;00m$
   437^I  win.outputTextView.getBuffer().setText([33m"[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m)$
   438^I$
   439^I  [34mvar[39;49;00m outp = osProc.execProcess(GetCmd(win.settings.nimrodCmd,$
   440^I                                win.Tabs[currentTab].filename))$
   441^I  [37m# Colors[39;49;00m$
   442^I  [34mvar[39;49;00m normalTag = createColor(win.outputTextView, [33m"[39;49;00m[33mnormalTag[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33m#3d3d3d[39;49;00m[33m"[39;49;00m)$
   443^I  [34mvar[39;49;00m errorTag = createColor(win.outputTextView, [33m"[39;49;00m[33merrorTag[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mred[39;49;00m[33m"[39;49;00m)$
   444^I  [34mvar[39;49;00m warningTag = createColor(win.outputTextView, [33m"[39;49;00m[33mwarningTag[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mdarkorange[39;49;00m[33m"[39;49;00m)$
   445^I  [34mvar[39;49;00m successTag = createColor(win.outputTextView, [33m"[39;49;00m[33msuccessTag[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mdarkgreen[39;49;00m[33m"[39;49;00m)$
   446^I  [34mfor[39;49;00m x [35min[39;49;00m outp.splitLines():$
   447^I    [34mif[39;49;00m x =~ pegLineError / pegOtherError:$
   448^I      win.outputTextView.addText([33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m & x, errorTag)$
   449^I    [34melif[39;49;00m x=~ pegSuccess:$
   450^I      win.outputTextView.addText([33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m & x, successTag)$
   451^I      $
   452^I      [37m# Launch the process[39;49;00m$
   453^I      [34mif[39;49;00m shouldRun:$
   454^I        [34mvar[39;49;00m filename = changeFileExt(win.Tabs[currentTab].filename, os.ExeExt)$
   455^I        [34mvar[39;49;00m output = [33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m & osProc.execProcess(filename)$
   456^I        win.outputTextView.addText(output)$
   457^I    [34melif[39;49;00m x =~ pegLineWarning:$
   458^I      win.outputTextView.addText([33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m & x, warningTag)$
   459^I    [34melse[39;49;00m:$
   460^I      win.outputTextView.addText([33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m & x, normalTag)$
   461^I  showBottomPanel()$
   462^I$
   463^I[34mproc [39;49;00m[32mCompileCurrent_Activate[39;49;00m(menuitem: PMenuItem, user_data: pgpointer) =$
   464^I  saveFile_Activate([34mnil[39;49;00m, [34mnil[39;49;00m)$
   465^I  compileRun(win.SourceViewTabs.getCurrentPage(), [34mfalse[39;49;00m)$
   466^I  $
   467^I[34mproc [39;49;00m[32mCompileRunCurrent_Activate[39;49;00m(menuitem: PMenuItem, user_data: pgpointer) =$
   468^I  saveFile_Activate([34mnil[39;49;00m, [34mnil[39;49;00m)$
   469^I  compileRun(win.SourceViewTabs.getCurrentPage(), [34mtrue[39;49;00m)$
   470^I$
   471^I[34mproc [39;49;00m[32mCompileProject_Activate[39;49;00m(menuitem: PMenuItem, user_data: pgpointer) =$
   472^I  saveAllTabs()$
   473^I  compileRun(getProjectTab(), [34mfalse[39;49;00m)$
   474^I  $
   475^I[34mproc [39;49;00m[32mCompileRunProject_Activate[39;49;00m(menuitem: PMenuItem, user_data: pgpointer) =$
   476^I  saveAllTabs()$
   477^I  compileRun(getProjectTab(), [34mtrue[39;49;00m)$
   478^I$
   479^I[34mproc [39;49;00m[32mRunCustomCommand[39;49;00m(cmd: [36mstring[39;49;00m) = $
   480^I  saveFile_Activate([34mnil[39;49;00m, [34mnil[39;49;00m)$
   481^I  [34mvar[39;49;00m currentTab = win.SourceViewTabs.getCurrentPage()$
   482^I  [34mif[39;49;00m win.Tabs[currentTab].filename.len == [34m0[39;49;00m [35mor[39;49;00m cmd.len == [34m0[39;49;00m: [34mreturn[39;49;00m$
   483^I  [37m# Clear the outputTextView[39;49;00m$
   484^I  win.outputTextView.getBuffer().setText([33m"[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m)$
   485^I  [34mvar[39;49;00m outp = osProc.execProcess(GetCmd(cmd, win.Tabs[currentTab].filename))$
   486^I  [34mvar[39;49;00m normalTag = createColor(win.outputTextView, [33m"[39;49;00m[33mnormalTag[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33m#3d3d3d[39;49;00m[33m"[39;49;00m)$
   487^I  [34mfor[39;49;00m x [35min[39;49;00m outp.splitLines():$
   488^I    win.outputTextView.addText([33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m & x, normalTag)$
   489^I  showBottomPanel()$
   490^I$
   491^I[34mproc [39;49;00m[32mRunCustomCommand1[39;49;00m(menuitem: PMenuItem, user_data: pgpointer) =$
   492^I  RunCustomCommand(win.settings.customCmd1)$
   493^I$
   494^I[34mproc [39;49;00m[32mRunCustomCommand2[39;49;00m(menuitem: PMenuItem, user_data: pgpointer) =$
   495^I  RunCustomCommand(win.settings.customCmd2)$
   496^I$
   497^I[34mproc [39;49;00m[32mRunCustomCommand3[39;49;00m(menuitem: PMenuItem, user_data: pgpointer) =$
   498^I  RunCustomCommand(win.settings.customCmd3)$
   499^I$
   500^I[37m# -- FindBar[39;49;00m$
   501^I$
   502^I[34mproc [39;49;00m[32mnextBtn_Clicked[39;49;00m(button: PButton, user_data: pgpointer) = findText([34mTrue[39;49;00m)$
   503^I[34mproc [39;49;00m[32mprevBtn_Clicked[39;49;00m(button: PButton, user_data: pgpointer) = findText([34mFalse[39;49;00m)$
   504^I$
   505^I[34mproc [39;49;00m[32mreplaceBtn_Clicked[39;49;00m(button: PButton, user_data: pgpointer) =$
   506^I  [34mvar[39;49;00m currentTab = win.SourceViewTabs.getCurrentPage()$
   507^I  [34mvar[39;49;00m start, theEnd: TTextIter$
   508^I  [34mif[39;49;00m [35mnot[39;49;00m win.Tabs[currentTab].buffer.getSelectionBounds($
   509^I        [34maddr[39;49;00m(start), [34maddr[39;49;00m(theEnd)):$
   510^I    [37m# If no text is selected, try finding a match.[39;49;00m$
   511^I    findText([34mTrue[39;49;00m)$
   512^I    [34mif[39;49;00m [35mnot[39;49;00m win.Tabs[currentTab].buffer.getSelectionBounds($
   513^I          [34maddr[39;49;00m(start), [34maddr[39;49;00m(theEnd)):$
   514^I      [37m# No match[39;49;00m$
   515^I      [34mreturn[39;49;00m$
   516^I  $
   517^I  [37m# Remove the text[39;49;00m$
   518^I  win.Tabs[currentTab].buffer.delete([34maddr[39;49;00m(start), [34maddr[39;49;00m(theEnd))$
   519^I  [37m# Insert the replacement[39;49;00m$
   520^I  [34mvar[39;49;00m text = getText(win.replaceEntry)$
   521^I  win.Tabs[currentTab].buffer.insert([34maddr[39;49;00m(start), text, len(text))$
   522^I  $
   523^I[34mproc [39;49;00m[32mreplaceAllBtn_Clicked[39;49;00m(button: PButton, user_data: pgpointer) =$
   524^I  [34mvar[39;49;00m find = getText(win.findEntry)$
   525^I  [34mvar[39;49;00m replace = getText(win.replaceEntry)$
   526^I  [34mdiscard[39;49;00m replaceAll(find, replace)$
   527^I  $
   528^I[34mproc [39;49;00m[32mcloseBtn_Clicked[39;49;00m(button: PButton, user_data: pgpointer) = $
   529^I  win.findBar.hide()$
   530^I$
   531^I[34mproc [39;49;00m[32mcaseSens_Changed[39;49;00m(radiomenuitem: PRadioMenuitem, user_data: pgpointer) =$
   532^I  win.settings.search = [33m"[39;49;00m[33mcasesens[39;49;00m[33m"[39;49;00m$
   533^I[34mproc [39;49;00m[32mcaseInSens_Changed[39;49;00m(radiomenuitem: PRadioMenuitem, user_data: pgpointer) =$
   534^I  win.settings.search = [33m"[39;49;00m[33mcaseinsens[39;49;00m[33m"[39;49;00m$
   535^I[34mproc [39;49;00m[32mstyle_Changed[39;49;00m(radiomenuitem: PRadioMenuitem, user_data: pgpointer) =$
   536^I  win.settings.search = [33m"[39;49;00m[33mstyle[39;49;00m[33m"[39;49;00m$
   537^I[34mproc [39;49;00m[32mregex_Changed[39;49;00m(radiomenuitem: PRadioMenuitem, user_data: pgpointer) =$
   538^I  win.settings.search = [33m"[39;49;00m[33mregex[39;49;00m[33m"[39;49;00m$
   539^I[34mproc [39;49;00m[32mpeg_Changed[39;49;00m(radiomenuitem: PRadioMenuitem, user_data: pgpointer) =$
   540^I  win.settings.search = [33m"[39;49;00m[33mpeg[39;49;00m[33m"[39;49;00m$
   541^I$
   542^I[34mproc [39;49;00m[32mextraBtn_Clicked[39;49;00m(button: PButton, user_data: pgpointer) =$
   543^I  [34mvar[39;49;00m extraMenu = menuNew()$
   544^I  [34mvar[39;49;00m group: PGSList$
   545^I$
   546^I  [34mvar[39;49;00m caseSensMenuItem = radio_menu_item_new(group, [33m"[39;49;00m[33mCase sensitive[39;49;00m[33m"[39;49;00m)$
   547^I  extraMenu.append(caseSensMenuItem)$
   548^I  [34mdiscard[39;49;00m signal_connect(caseSensMenuItem, [33m"[39;49;00m[33mtoggled[39;49;00m[33m"[39;49;00m, $
   549^I                          SIGNAL_FUNC(caseSens_Changed), [34mnil[39;49;00m)$
   550^I  caseSensMenuItem.show()$
   551^I  group = caseSensMenuItem.ItemGetGroup()$
   552^I  $
   553^I  [34mvar[39;49;00m caseInSensMenuItem = radio_menu_item_new(group, [33m"[39;49;00m[33mCase insensitive[39;49;00m[33m"[39;49;00m)$
   554^I  extraMenu.append(caseInSensMenuItem)$
   555^I  [34mdiscard[39;49;00m signal_connect(caseInSensMenuItem, [33m"[39;49;00m[33mtoggled[39;49;00m[33m"[39;49;00m, $
   556^I                          SIGNAL_FUNC(caseInSens_Changed), [34mnil[39;49;00m)$
   557^I  caseInSensMenuItem.show()$
   558^I  group = caseInSensMenuItem.ItemGetGroup()$
   559^I  $
   560^I  [34mvar[39;49;00m styleMenuItem = radio_menu_item_new(group, [33m"[39;49;00m[33mStyle insensitive[39;49;00m[33m"[39;49;00m)$
   561^I  extraMenu.append(styleMenuItem)$
   562^I  [34mdiscard[39;49;00m signal_connect(styleMenuItem, [33m"[39;49;00m[33mtoggled[39;49;00m[33m"[39;49;00m, $
   563^I                          SIGNAL_FUNC(style_Changed), [34mnil[39;49;00m)$
   564^I  styleMenuItem.show()$
   565^I  group = styleMenuItem.ItemGetGroup()$
   566^I  $
   567^I  [34mvar[39;49;00m regexMenuItem = radio_menu_item_new(group, [33m"[39;49;00m[33mRegex[39;49;00m[33m"[39;49;00m)$
   568^I  extraMenu.append(regexMenuItem)$
   569^I  [34mdiscard[39;49;00m signal_connect(regexMenuItem, [33m"[39;49;00m[33mtoggled[39;49;00m[33m"[39;49;00m, $
   570^I                          SIGNAL_FUNC(regex_Changed), [34mnil[39;49;00m)$
   571^I  regexMenuItem.show()$
   572^I  group = regexMenuItem.ItemGetGroup()$
   573^I  $
   574^I  [34mvar[39;49;00m pegMenuItem = radio_menu_item_new(group, [33m"[39;49;00m[33mPegs[39;49;00m[33m"[39;49;00m)$
   575^I  extraMenu.append(pegMenuItem)$
   576^I  [34mdiscard[39;49;00m signal_connect(pegMenuItem, [33m"[39;49;00m[33mtoggled[39;49;00m[33m"[39;49;00m, $
   577^I                          SIGNAL_FUNC(peg_Changed), [34mnil[39;49;00m)$
   578^I  pegMenuItem.show()$
   579^I  $
   580^I  [37m# Make the correct radio button active[39;49;00m$
   581^I  [34mcase[39;49;00m win.settings.search$
   582^I  [34mof[39;49;00m [33m"[39;49;00m[33mcasesens[39;49;00m[33m"[39;49;00m:$
   583^I    PCheckMenuItem(caseSensMenuItem).ItemSetActive([34mTrue[39;49;00m)$
   584^I  [34mof[39;49;00m [33m"[39;49;00m[33mcaseinsens[39;49;00m[33m"[39;49;00m:$
   585^I    PCheckMenuItem(caseInSensMenuItem).ItemSetActive([34mTrue[39;49;00m)$
   586^I  [34mof[39;49;00m [33m"[39;49;00m[33mstyle[39;49;00m[33m"[39;49;00m:$
   587^I    PCheckMenuItem(styleMenuItem).ItemSetActive([34mTrue[39;49;00m)$
   588^I  [34mof[39;49;00m [33m"[39;49;00m[33mregex[39;49;00m[33m"[39;49;00m:$
   589^I    PCheckMenuItem(regexMenuItem).ItemSetActive([34mTrue[39;49;00m)$
   590^I  [34mof[39;49;00m [33m"[39;49;00m[33mpeg[39;49;00m[33m"[39;49;00m:$
   591^I    PCheckMenuItem(pegMenuItem).ItemSetActive([34mTrue[39;49;00m)$
   592^I$
   593^I  extraMenu.popup([34mnil[39;49;00m, [34mnil[39;49;00m, [34mnil[39;49;00m, [34mnil[39;49;00m, [34m0[39;49;00m, get_current_event_time())$
   594^I$
   595^I[37m# GUI Initialization[39;49;00m$
   596^I$
   597^I[34mproc [39;49;00m[32mcreateAccelMenuItem[39;49;00m(toolsMenu: PMenu, accGroup: PAccelGroup, $
   598^I                         label: [36mstring[39;49;00m, acc: gint,$
   599^I                         action: [34mproc[39;49;00m (i: PMenuItem, p: pgpointer)) = $
   600^I  [34mvar[39;49;00m result = menu_item_new(label)$
   601^I  result.addAccelerator([33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m, accGroup, acc, [34m0[39;49;00m, ACCEL_VISIBLE)$
   602^I  ToolsMenu.append(result)$
   603^I  show(result)$
   604^I  [34mdiscard[39;49;00m signal_connect(result, [33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m, SIGNAL_FUNC(action), [34mnil[39;49;00m)$
   605^I$
   606^I[34mproc [39;49;00m[32mcreateSeparator[39;49;00m(menu: PMenu) =$
   607^I  [34mvar[39;49;00m sep = separator_menu_item_new()$
   608^I  menu.append(sep)$
   609^I  sep.show()$
   610^I$
   611^I[34mproc [39;49;00m[32minitTopMenu[39;49;00m(MainBox: PBox) =$
   612^I  [37m# Create a accelerator group, used for shortcuts[39;49;00m$
   613^I  [37m# like CTRL + S in SaveMenuItem[39;49;00m$
   614^I  [34mvar[39;49;00m accGroup = accel_group_new()$
   615^I  add_accel_group(win.w, accGroup)$
   616^I$
   617^I  [37m# TopMenu(MenuBar)[39;49;00m$
   618^I  [34mvar[39;49;00m TopMenu = menuBarNew()$
   619^I  $
   620^I  [37m# FileMenu[39;49;00m$
   621^I  [34mvar[39;49;00m FileMenu = menuNew()$
   622^I$
   623^I  [34mvar[39;49;00m NewMenuItem = menu_item_new([33m"[39;49;00m[33mNew[39;49;00m[33m"[39;49;00m) [37m# New[39;49;00m$
   624^I  FileMenu.append(NewMenuItem)$
   625^I  show(NewMenuItem)$
   626^I  [34mdiscard[39;49;00m signal_connect(NewMenuItem, [33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m, $
   627^I                          SIGNAL_FUNC(newFile), [34mnil[39;49;00m)$
   628^I$
   629^I  createSeparator(FileMenu)$
   630^I$
   631^I  [34mvar[39;49;00m OpenMenuItem = menu_item_new([33m"[39;49;00m[33mOpen...[39;49;00m[33m"[39;49;00m) [37m# Open...[39;49;00m$
   632^I  [37m# CTRL + O[39;49;00m$
   633^I  OpenMenuItem.add_accelerator([33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m, accGroup, $
   634^I                  KEY_o, CONTROL_MASK, ACCEL_VISIBLE) $
   635^I  FileMenu.append(OpenMenuItem)$
   636^I  show(OpenMenuItem)$
   637^I  [34mdiscard[39;49;00m signal_connect(OpenMenuItem, [33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m, $
   638^I                          SIGNAL_FUNC(aporia.openFile), [34mnil[39;49;00m)$
   639^I  $
   640^I  [34mvar[39;49;00m SaveMenuItem = menu_item_new([33m"[39;49;00m[33mSave[39;49;00m[33m"[39;49;00m) [37m# Save[39;49;00m$
   641^I  [37m# CTRL + S[39;49;00m$
   642^I  SaveMenuItem.add_accelerator([33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m, accGroup, $
   643^I                  KEY_s, CONTROL_MASK, ACCEL_VISIBLE) $
   644^I  FileMenu.append(SaveMenuItem)$
   645^I  show(SaveMenuItem)$
   646^I  [34mdiscard[39;49;00m signal_connect(SaveMenuItem, [33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m, $
   647^I                          SIGNAL_FUNC(saveFile_activate), [34mnil[39;49;00m)$
   648^I$
   649^I  [34mvar[39;49;00m SaveAsMenuItem = menu_item_new([33m"[39;49;00m[33mSave As...[39;49;00m[33m"[39;49;00m) [37m# Save as...[39;49;00m$
   650^I$
   651^I  SaveAsMenuItem.add_accelerator([33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m, accGroup, $
   652^I                  KEY_s, CONTROL_MASK [35mor[39;49;00m gdk2.SHIFT_MASK, ACCEL_VISIBLE) $
   653^I  FileMenu.append(SaveAsMenuItem)$
   654^I  show(SaveAsMenuItem)$
   655^I  [34mdiscard[39;49;00m signal_connect(SaveAsMenuItem, [33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m, $
   656^I                          SIGNAL_FUNC(saveFileAs_Activate), [34mnil[39;49;00m)$
   657^I  $
   658^I  [34mvar[39;49;00m FileMenuItem = menuItemNewWithMnemonic([33m"[39;49;00m[33m_File[39;49;00m[33m"[39;49;00m)$
   659^I$
   660^I  FileMenuItem.setSubMenu(FileMenu)$
   661^I  FileMenuItem.show()$
   662^I  TopMenu.append(FileMenuItem)$
   663^I  $
   664^I  [37m# Edit menu[39;49;00m$
   665^I  [34mvar[39;49;00m EditMenu = menuNew()$
   666^I$
   667^I  [34mvar[39;49;00m UndoMenuItem = menu_item_new([33m"[39;49;00m[33mUndo[39;49;00m[33m"[39;49;00m) [37m# Undo[39;49;00m$
   668^I  EditMenu.append(UndoMenuItem)$
   669^I  show(UndoMenuItem)$
   670^I  [34mdiscard[39;49;00m signal_connect(UndoMenuItem, [33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m, $
   671^I                          SIGNAL_FUNC(aporia.undo), [34mnil[39;49;00m)$
   672^I  $
   673^I  [34mvar[39;49;00m RedoMenuItem = menu_item_new([33m"[39;49;00m[33mRedo[39;49;00m[33m"[39;49;00m) [37m# Undo[39;49;00m$
   674^I  EditMenu.append(RedoMenuItem)$
   675^I  show(RedoMenuItem)$
   676^I  [34mdiscard[39;49;00m signal_connect(RedoMenuItem, [33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m, $
   677^I                          SIGNAL_FUNC(aporia.redo), [34mnil[39;49;00m)$
   678^I$
   679^I  createSeparator(EditMenu)$
   680^I  $
   681^I  [34mvar[39;49;00m FindMenuItem = menu_item_new([33m"[39;49;00m[33mFind[39;49;00m[33m"[39;49;00m) [37m# Find[39;49;00m$
   682^I  FindMenuItem.add_accelerator([33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m, accGroup, $
   683^I                  KEY_f, CONTROL_MASK, ACCEL_VISIBLE) $
   684^I  EditMenu.append(FindMenuItem)$
   685^I  show(FindMenuItem)$
   686^I  [34mdiscard[39;49;00m signal_connect(FindMenuItem, [33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m, $
   687^I                          SIGNAL_FUNC(aporia.find_Activate), [34mnil[39;49;00m)$
   688^I$
   689^I  [34mvar[39;49;00m ReplaceMenuItem = menu_item_new([33m"[39;49;00m[33mReplace[39;49;00m[33m"[39;49;00m) [37m# Replace[39;49;00m$
   690^I  ReplaceMenuItem.add_accelerator([33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m, accGroup, $
   691^I                  KEY_h, CONTROL_MASK, ACCEL_VISIBLE) $
   692^I  EditMenu.append(ReplaceMenuItem)$
   693^I  show(ReplaceMenuItem)$
   694^I  [34mdiscard[39;49;00m signal_connect(ReplaceMenuItem, [33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m, $
   695^I                          SIGNAL_FUNC(aporia.replace_Activate), [34mnil[39;49;00m)$
   696^I$
   697^I  createSeparator(EditMenu)$
   698^I  $
   699^I  [34mvar[39;49;00m SettingsMenuItem = menu_item_new([33m"[39;49;00m[33mSettings...[39;49;00m[33m"[39;49;00m) [37m# Settings[39;49;00m$
   700^I  EditMenu.append(SettingsMenuItem)$
   701^I  show(SettingsMenuItem)$
   702^I  [34mdiscard[39;49;00m signal_connect(SettingsMenuItem, [33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m, $
   703^I                          SIGNAL_FUNC(aporia.Settings_Activate), [34mnil[39;49;00m)$
   704^I$
   705^I  [34mvar[39;49;00m EditMenuItem = menuItemNewWithMnemonic([33m"[39;49;00m[33m_Edit[39;49;00m[33m"[39;49;00m)$
   706^I$
   707^I  EditMenuItem.setSubMenu(EditMenu)$
   708^I  EditMenuItem.show()$
   709^I  TopMenu.append(EditMenuItem)$
   710^I  $
   711^I  [37m# View menu[39;49;00m$
   712^I  [34mvar[39;49;00m ViewMenu = menuNew()$
   713^I  $
   714^I  win.viewBottomPanelMenuItem = check_menu_item_new([33m"[39;49;00m[33mBottom Panel[39;49;00m[33m"[39;49;00m)$
   715^I  PCheckMenuItem(win.viewBottomPanelMenuItem).itemSetActive($
   716^I         win.settings.bottomPanelVisible)$
   717^I  win.viewBottomPanelMenuItem.add_accelerator([33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m, accGroup, $
   718^I                  KEY_f9, CONTROL_MASK, ACCEL_VISIBLE) $
   719^I  ViewMenu.append(win.viewBottomPanelMenuItem)$
   720^I  show(win.viewBottomPanelMenuItem)$
   721^I  [34mdiscard[39;49;00m signal_connect(win.viewBottomPanelMenuItem, [33m"[39;49;00m[33mtoggled[39;49;00m[33m"[39;49;00m, $
   722^I                          SIGNAL_FUNC(aporia.viewBottomPanel_Toggled), [34mnil[39;49;00m)$
   723^I  $
   724^I  [34mvar[39;49;00m ViewMenuItem = menuItemNewWithMnemonic([33m"[39;49;00m[33m_View[39;49;00m[33m"[39;49;00m)$
   725^I$
   726^I  ViewMenuItem.setSubMenu(ViewMenu)$
   727^I  ViewMenuItem.show()$
   728^I  TopMenu.append(ViewMenuItem)       $
   729^I  $
   730^I  $
   731^I  [37m# Tools menu[39;49;00m$
   732^I  [34mvar[39;49;00m ToolsMenu = menuNew()$
   733^I$
   734^I  createAccelMenuItem(ToolsMenu, accGroup, [33m"[39;49;00m[33mCompile current file[39;49;00m[33m"[39;49;00m, $
   735^I                      KEY_F4, aporia.CompileCurrent_Activate)$
   736^I  createAccelMenuItem(ToolsMenu, accGroup, [33m"[39;49;00m[33mCompile & run current file[39;49;00m[33m"[39;49;00m, $
   737^I                      KEY_F5, aporia.CompileRunCurrent_Activate)$
   738^I  createSeparator(ToolsMenu)$
   739^I  createAccelMenuItem(ToolsMenu, accGroup, [33m"[39;49;00m[33mCompile project[39;49;00m[33m"[39;49;00m, $
   740^I                      KEY_F8, aporia.CompileProject_Activate)$
   741^I  createAccelMenuItem(ToolsMenu, accGroup, [33m"[39;49;00m[33mCompile & run project[39;49;00m[33m"[39;49;00m, $
   742^I                      KEY_F9, aporia.CompileRunProject_Activate)$
   743^I  createSeparator(ToolsMenu)$
   744^I  createAccelMenuItem(ToolsMenu, accGroup, [33m"[39;49;00m[33mRun custom command 1[39;49;00m[33m"[39;49;00m, $
   745^I                      KEY_F1, aporia.RunCustomCommand1)$
   746^I  createAccelMenuItem(ToolsMenu, accGroup, [33m"[39;49;00m[33mRun custom command 2[39;49;00m[33m"[39;49;00m, $
   747^I                      KEY_F2, aporia.RunCustomCommand2)$
   748^I  createAccelMenuItem(ToolsMenu, accGroup, [33m"[39;49;00m[33mRun custom command 3[39;49;00m[33m"[39;49;00m, $
   749^I                      KEY_F3, aporia.RunCustomCommand3)$
   750^I  $
   751^I  [34mvar[39;49;00m ToolsMenuItem = menuItemNewWithMnemonic([33m"[39;49;00m[33m_Tools[39;49;00m[33m"[39;49;00m)$
   752^I  $
   753^I  ToolsMenuItem.setSubMenu(ToolsMenu)$
   754^I  ToolsMenuItem.show()$
   755^I  TopMenu.append(ToolsMenuItem)$
   756^I  $
   757^I  [37m# Help menu[39;49;00m$
   758^I  MainBox.packStart(TopMenu, [34mFalse[39;49;00m, [34mFalse[39;49;00m, [34m0[39;49;00m)$
   759^I  TopMenu.show()$
   760^I$
   761^I[34mproc [39;49;00m[32minitToolBar[39;49;00m(MainBox: PBox) =$
   762^I  [37m# TopBar(ToolBar)[39;49;00m$
   763^I  [34mvar[39;49;00m TopBar = toolbarNew()$
   764^I  TopBar.setStyle(TOOLBAR_ICONS)$
   765^I  $
   766^I  [34mvar[39;49;00m NewFileItem = TopBar.insertStock(STOCK_NEW, [33m"[39;49;00m[33mNew File[39;49;00m[33m"[39;49;00m,$
   767^I                      [33m"[39;49;00m[33mNew File[39;49;00m[33m"[39;49;00m, SIGNAL_FUNC(aporia.newFile), [34mnil[39;49;00m, [34m0[39;49;00m)$
   768^I  TopBar.appendSpace()$
   769^I  [34mvar[39;49;00m OpenItem = TopBar.insertStock(STOCK_OPEN, [33m"[39;49;00m[33mOpen[39;49;00m[33m"[39;49;00m,$
   770^I                      [33m"[39;49;00m[33mOpen[39;49;00m[33m"[39;49;00m, SIGNAL_FUNC(aporia.openFile), [34mnil[39;49;00m, -[34m1[39;49;00m)$
   771^I  [34mvar[39;49;00m SaveItem = TopBar.insertStock(STOCK_SAVE, [33m"[39;49;00m[33mSave[39;49;00m[33m"[39;49;00m,$
   772^I                      [33m"[39;49;00m[33mSave[39;49;00m[33m"[39;49;00m, SIGNAL_FUNC(saveFile_Activate), [34mnil[39;49;00m, -[34m1[39;49;00m)$
   773^I  TopBar.appendSpace()$
   774^I  [34mvar[39;49;00m UndoItem = TopBar.insertStock(STOCK_UNDO, [33m"[39;49;00m[33mUndo[39;49;00m[33m"[39;49;00m, $
   775^I                      [33m"[39;49;00m[33mUndo[39;49;00m[33m"[39;49;00m, SIGNAL_FUNC(aporia.undo), [34mnil[39;49;00m, -[34m1[39;49;00m)$
   776^I  [34mvar[39;49;00m RedoItem = TopBar.insertStock(STOCK_REDO, [33m"[39;49;00m[33mRedo[39;49;00m[33m"[39;49;00m,$
   777^I                      [33m"[39;49;00m[33mRedo[39;49;00m[33m"[39;49;00m, SIGNAL_FUNC(aporia.redo), [34mnil[39;49;00m, -[34m1[39;49;00m)$
   778^I  $
   779^I  MainBox.packStart(TopBar, [34mFalse[39;49;00m, [34mFalse[39;49;00m, [34m0[39;49;00m)$
   780^I  TopBar.show()$
   781^I  $
   782^I[34mproc [39;49;00m[32minitSourceViewTabs[39;49;00m() =$
   783^I  win.SourceViewTabs = notebookNew()$
   784^I  [37m#win.sourceViewTabs.dragDestSet(DEST_DEFAULT_DROP, nil, 0, ACTION_MOVE)[39;49;00m$
   785^I  [34mdiscard[39;49;00m win.SourceViewTabs.signalConnect($
   786^I          [33m"[39;49;00m[33mswitch-page[39;49;00m[33m"[39;49;00m, SIGNAL_FUNC(onSwitchTab), [34mnil[39;49;00m)$
   787^I  [37m#discard win.SourceViewTabs.signalConnect([39;49;00m$
   788^I  [37m#        "drag-drop", SIGNAL_FUNC(svTabs_DragDrop), nil)[39;49;00m$
   789^I  [37m#discard win.SourceViewTabs.signalConnect([39;49;00m$
   790^I  [37m#        "drag-data-received", SIGNAL_FUNC(svTabs_DragDataRecv), nil)[39;49;00m$
   791^I  [37m#discard win.SourceViewTabs.signalConnect([39;49;00m$
   792^I  [37m#        "drag-motion", SIGNAL_FUNC(svTabs_DragMotion), nil)[39;49;00m$
   793^I  win.SourceViewTabs.set_scrollable([34mTrue[39;49;00m)$
   794^I  $
   795^I  win.SourceViewTabs.show()$
   796^I  [34mif[39;49;00m lastSession.len != [34m0[39;49;00m:$
   797^I    [34mfor[39;49;00m i [35min[39;49;00m [34m0[39;49;00m .. len(lastSession)-[34m1[39;49;00m:$
   798^I      [34mvar[39;49;00m splitUp = lastSession[i].split([33m'[39;49;00m[33m|[39;49;00m[33m'[39;49;00m)$
   799^I      [34mvar[39;49;00m (filename, offset) = (splitUp[[34m0[39;49;00m], splitUp[[34m1[39;49;00m])$
   800^I      addTab([33m"[39;49;00m[33m"[39;49;00m, filename)$
   801^I      $
   802^I      [34mvar[39;49;00m iter: TTextIter$
   803^I      win.Tabs[i].buffer.getIterAtOffset([34maddr[39;49;00m(iter), offset.parseInt())$
   804^I      win.Tabs[i].buffer.moveMarkByName([33m"[39;49;00m[33minsert[39;49;00m[33m"[39;49;00m, [34maddr[39;49;00m(iter))$
   805^I      win.Tabs[i].buffer.moveMarkByName([33m"[39;49;00m[33mselection_bound[39;49;00m[33m"[39;49;00m, [34maddr[39;49;00m(iter))$
   806^I      $
   807^I      [37m# TODO: Fix this..... :([39;49;00m$
   808^I      [34mdiscard[39;49;00m PTextView(win.Tabs[i].sourceView).$
   809^I          scrollToIter([34maddr[39;49;00m(iter), [34m0[39;49;00m[34m.25[39;49;00m, [34mtrue[39;49;00m, [34m0[39;49;00m[34m.0[39;49;00m, [34m0[39;49;00m[34m.0[39;49;00m)$
   810^I  [34melse[39;49;00m:$
   811^I    addTab([33m"[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33m"[39;49;00m)$
   812^I  $
   813^I  [37m# This doesn't work :\[39;49;00m$
   814^I  win.Tabs[[34m0[39;49;00m].sourceView.grabFocus()$
   815^I$
   816^I  $
   817^I[34mproc [39;49;00m[32minitBottomTabs[39;49;00m() =$
   818^I  win.bottomPanelTabs = notebookNew()$
   819^I  [34mif[39;49;00m win.settings.bottomPanelVisible:$
   820^I    win.bottomPanelTabs.show()$
   821^I  $
   822^I  [37m# output tab[39;49;00m$
   823^I  [34mvar[39;49;00m tabLabel = labelNew([33m"[39;49;00m[33mOutput[39;49;00m[33m"[39;49;00m)$
   824^I  [34mvar[39;49;00m outputTab = vboxNew([34mFalse[39;49;00m, [34m0[39;49;00m)$
   825^I  [34mdiscard[39;49;00m win.bottomPanelTabs.appendPage(outputTab, tabLabel)$
   826^I  [37m# Compiler tabs, gtktextview[39;49;00m$
   827^I  [34mvar[39;49;00m outputScrolledWindow = scrolledwindowNew([34mnil[39;49;00m, [34mnil[39;49;00m)$
   828^I  outputScrolledWindow.setPolicy(POLICY_AUTOMATIC, POLICY_AUTOMATIC)$
   829^I  outputTab.packStart(outputScrolledWindow, [34mtrue[39;49;00m, [34mtrue[39;49;00m, [34m0[39;49;00m)$
   830^I  outputScrolledWindow.show()$
   831^I  $
   832^I  win.outputTextView = textviewNew()$
   833^I  outputScrolledWindow.add(win.outputTextView)$
   834^I  win.outputTextView.show()$
   835^I  $
   836^I  outputTab.show()$
   837^I$
   838^I[34mproc [39;49;00m[32minitTAndBP[39;49;00m(MainBox: PBox) =$
   839^I  [37m# This init's the HPaned, which splits the sourceViewTabs[39;49;00m$
   840^I  [37m# and the BottomPanelTabs[39;49;00m$
   841^I  initSourceViewTabs()$
   842^I  initBottomTabs()$
   843^I  $
   844^I  [34mvar[39;49;00m TAndBPVPaned = vpanedNew()$
   845^I  tandbpVPaned.pack1(win.sourceViewTabs, resize=[34mTrue[39;49;00m, shrink=[34mFalse[39;49;00m)$
   846^I  tandbpVPaned.pack2(win.bottomPanelTabs, resize=[34mFalse[39;49;00m, shrink=[34mFalse[39;49;00m)$
   847^I  MainBox.packStart(TAndBPVPaned, [34mTrue[39;49;00m, [34mTrue[39;49;00m, [34m0[39;49;00m)$
   848^I  tandbpVPaned.setPosition(win.settings.VPanedPos)$
   849^I  TAndBPVPaned.show()$
   850^I$
   851^I[34mproc [39;49;00m[32minitFindBar[39;49;00m(MainBox: PBox) =$
   852^I  [37m# Create a fixed container[39;49;00m$
   853^I  win.findBar = HBoxNew([34mFalse[39;49;00m, [34m0[39;49;00m)$
   854^I  win.findBar.setSpacing([34m4[39;49;00m)$
   855^I$
   856^I  [37m# Add a Label 'Find'[39;49;00m$
   857^I  [34mvar[39;49;00m findLabel = labelNew([33m"[39;49;00m[33mFind:[39;49;00m[33m"[39;49;00m)$
   858^I  win.findBar.packStart(findLabel, [34mFalse[39;49;00m, [34mFalse[39;49;00m, [34m0[39;49;00m)$
   859^I  findLabel.show()$
   860^I$
   861^I  [37m# Add a (find) text entry[39;49;00m$
   862^I  win.findEntry = entryNew()$
   863^I  win.findBar.packStart(win.findEntry, [34mFalse[39;49;00m, [34mFalse[39;49;00m, [34m0[39;49;00m)$
   864^I  [34mdiscard[39;49;00m win.findEntry.signalConnect([33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m, SIGNAL_FUNC($
   865^I                                      aporia.nextBtn_Clicked), [34mnil[39;49;00m)$
   866^I  win.findEntry.show()$
   867^I  [34mvar[39;49;00m rq: TRequisition $
   868^I  win.findEntry.sizeRequest([34maddr[39;49;00m(rq))$
   869^I$
   870^I  [37m# Make the (find) text entry longer[39;49;00m$
   871^I  win.findEntry.set_size_request([34m190[39;49;00m, rq.height)$
   872^I  $
   873^I  [37m# Add a Label 'Replace' [39;49;00m$
   874^I  [37m# - This Is only shown, when the 'Search & Replace'(CTRL + H) is shown[39;49;00m$
   875^I  win.replaceLabel = labelNew([33m"[39;49;00m[33mReplace:[39;49;00m[33m"[39;49;00m)$
   876^I  win.findBar.packStart(win.replaceLabel, [34mFalse[39;49;00m, [34mFalse[39;49;00m, [34m0[39;49;00m)$
   877^I  [37m#replaceLabel.show()[39;49;00m$
   878^I  $
   879^I  [37m# Add a (replace) text entry [39;49;00m$
   880^I  [37m# - This Is only shown, when the 'Search & Replace'(CTRL + H) is shown[39;49;00m$
   881^I  win.replaceEntry = entryNew()$
   882^I  win.findBar.packStart(win.replaceEntry, [34mFalse[39;49;00m, [34mFalse[39;49;00m, [34m0[39;49;00m)$
   883^I  [37m#win.replaceEntry.show()[39;49;00m$
   884^I  [34mvar[39;49;00m rq1: TRequisition $
   885^I  win.replaceEntry.sizeRequest([34maddr[39;49;00m(rq1))$
   886^I$
   887^I  [37m# Make the (replace) text entry longer[39;49;00m$
   888^I  win.replaceEntry.set_size_request([34m100[39;49;00m, rq1.height)$
   889^I  $
   890^I  [37m# Find next button[39;49;00m$
   891^I  [34mvar[39;49;00m nextBtn = buttonNew([33m"[39;49;00m[33mNext[39;49;00m[33m"[39;49;00m)$
   892^I  win.findBar.packStart(nextBtn, [34mfalse[39;49;00m, [34mfalse[39;49;00m, [34m0[39;49;00m)$
   893^I  [34mdiscard[39;49;00m nextBtn.signalConnect([33m"[39;49;00m[33mclicked[39;49;00m[33m"[39;49;00m, $
   894^I             SIGNAL_FUNC(aporia.nextBtn_Clicked), [34mnil[39;49;00m)$
   895^I  nextBtn.show()$
   896^I  [34mvar[39;49;00m nxtBtnRq: TRequisition$
   897^I  nextBtn.sizeRequest([34maddr[39;49;00m(nxtBtnRq))$
   898^I  $
   899^I  [37m# Find previous button[39;49;00m$
   900^I  [34mvar[39;49;00m prevBtn = buttonNew([33m"[39;49;00m[33mPrevious[39;49;00m[33m"[39;49;00m)$
   901^I  win.findBar.packStart(prevBtn, [34mfalse[39;49;00m, [34mfalse[39;49;00m, [34m0[39;49;00m)$
   902^I  [34mdiscard[39;49;00m prevBtn.signalConnect([33m"[39;49;00m[33mclicked[39;49;00m[33m"[39;49;00m, $
   903^I             SIGNAL_FUNC(aporia.prevBtn_Clicked), [34mnil[39;49;00m)$
   904^I  prevBtn.show()$
   905^I  $
   906^I  [37m# Replace button[39;49;00m$
   907^I  [37m# - This Is only shown, when the 'Search & Replace'(CTRL + H) is shown[39;49;00m$
   908^I  win.replaceBtn = buttonNew([33m"[39;49;00m[33mReplace[39;49;00m[33m"[39;49;00m)$
   909^I  win.findBar.packStart(win.replaceBtn, [34mfalse[39;49;00m, [34mfalse[39;49;00m, [34m0[39;49;00m)$
   910^I  [34mdiscard[39;49;00m win.replaceBtn.signalConnect([33m"[39;49;00m[33mclicked[39;49;00m[33m"[39;49;00m, $
   911^I             SIGNAL_FUNC(aporia.replaceBtn_Clicked), [34mnil[39;49;00m)$
   912^I  [37m#replaceBtn.show()[39;49;00m$
   913^I$
   914^I  [37m# Replace all button[39;49;00m$
   915^I  [37m# - this Is only shown, when the 'Search & Replace'(CTRL + H) is shown[39;49;00m$
   916^I  win.replaceAllBtn = buttonNew([33m"[39;49;00m[33mReplace All[39;49;00m[33m"[39;49;00m)$
   917^I  win.findBar.packStart(win.replaceAllBtn, [34mfalse[39;49;00m, [34mfalse[39;49;00m, [34m0[39;49;00m)$
   918^I  [34mdiscard[39;49;00m win.replaceAllBtn.signalConnect([33m"[39;49;00m[33mclicked[39;49;00m[33m"[39;49;00m, $
   919^I             SIGNAL_FUNC(aporia.replaceAllBtn_Clicked), [34mnil[39;49;00m)$
   920^I  [37m#replaceAllBtn.show()[39;49;00m$
   921^I  $
   922^I  [37m# Right side ...[39;49;00m$
   923^I  $
   924^I  [37m# Close button - With a close stock image[39;49;00m$
   925^I  [34mvar[39;49;00m closeBtn = buttonNew()$
   926^I  [34mvar[39;49;00m closeImage = imageNewFromStock(STOCK_CLOSE, ICON_SIZE_SMALL_TOOLBAR)$
   927^I  [34mvar[39;49;00m closeBox = hboxNew([34mFalse[39;49;00m, [34m0[39;49;00m)$
   928^I  closeBtn.add(closeBox)$
   929^I  closeBox.show()$
   930^I  closeBox.add(closeImage)$
   931^I  closeImage.show()$
   932^I  [34mdiscard[39;49;00m closeBtn.signalConnect([33m"[39;49;00m[33mclicked[39;49;00m[33m"[39;49;00m, $
   933^I             SIGNAL_FUNC(aporia.closeBtn_Clicked), [34mnil[39;49;00m)$
   934^I  win.findBar.packEnd(closeBtn, [34mFalse[39;49;00m, [34mFalse[39;49;00m, [34m2[39;49;00m)$
   935^I  closeBtn.show()$
   936^I  $
   937^I  [37m# Extra button - When clicked shows a menu with options like 'Use regex'[39;49;00m$
   938^I  [34mvar[39;49;00m extraBtn = buttonNew()$
   939^I  [34mvar[39;49;00m extraImage = imageNewFromStock(STOCK_PROPERTIES, ICON_SIZE_SMALL_TOOLBAR)$
   940^I$
   941^I  [34mvar[39;49;00m extraBox = hboxNew([34mFalse[39;49;00m, [34m0[39;49;00m)$
   942^I  extraBtn.add(extraBox)$
   943^I  extraBox.show()$
   944^I  extraBox.add(extraImage)$
   945^I  extraImage.show()$
   946^I  [34mdiscard[39;49;00m extraBtn.signalConnect([33m"[39;49;00m[33mclicked[39;49;00m[33m"[39;49;00m, $
   947^I             SIGNAL_FUNC(aporia.extraBtn_Clicked), [34mnil[39;49;00m)$
   948^I  win.findBar.packEnd(extraBtn, [34mFalse[39;49;00m, [34mFalse[39;49;00m, [34m0[39;49;00m)$
   949^I  extraBtn.show()$
   950^I  $
   951^I  MainBox.packStart(win.findBar, [34mFalse[39;49;00m, [34mFalse[39;49;00m, [34m0[39;49;00m)$
   952^I  win.findBar.show()$
   953^I$
   954^I[34mproc [39;49;00m[32minitStatusBar[39;49;00m(MainBox: PBox) =$
   955^I  win.bottomBar = statusbarNew()$
   956^I  MainBox.packStart(win.bottomBar, [34mFalse[39;49;00m, [34mFalse[39;49;00m, [34m0[39;49;00m)$
   957^I  win.bottomBar.show()$
   958^I  $
   959^I  [34mdiscard[39;49;00m win.bottomBar.push([34m0[39;49;00m, [33m"[39;49;00m[33mLine: 0 Column: 0[39;49;00m[33m"[39;49;00m)$
   960^I  $
   961^I[34mproc [39;49;00m[32minitControls[39;49;00m() =$
   962^I  [37m# Load up the language style[39;49;00m$
   963^I  win.langMan = languageManagerGetDefault()$
   964^I  [34mvar[39;49;00m langpaths: [36marray[39;49;00m[[34m0[39;49;00m..[34m1[39;49;00m, cstring] = $
   965^I          [cstring(os.getApplicationDir() / langSpecs), [34mnil[39;49;00m]$
   966^I  win.langMan.setSearchPath([34maddr[39;49;00m(langpaths))$
   967^I  [34mvar[39;49;00m nimLang = win.langMan.getLanguage([33m"[39;49;00m[33mnimrod[39;49;00m[33m"[39;49;00m)$
   968^I  win.nimLang = nimLang$
   969^I  $
   970^I  [37m# Load the scheme[39;49;00m$
   971^I  [34mvar[39;49;00m schemeMan = schemeManagerGetDefault()$
   972^I  [34mvar[39;49;00m schemepaths: [36marray[39;49;00m[[34m0[39;49;00m..[34m1[39;49;00m, cstring] =$
   973^I          [cstring(os.getApplicationDir() / styles), [34mnil[39;49;00m]$
   974^I  schemeMan.setSearchPath([34maddr[39;49;00m(schemepaths))$
   975^I  win.scheme = schemeMan.getScheme(win.settings.colorSchemeID)$
   976^I  $
   977^I  [37m# Window[39;49;00m$
   978^I  win.w = windowNew(gtk2.WINDOW_TOPLEVEL)$
   979^I  win.w.setDefaultSize(win.settings.winWidth, win.settings.winHeight)$
   980^I  win.w.setTitle([33m"[39;49;00m[33mAporia IDE[39;49;00m[33m"[39;49;00m)$
   981^I  [34mif[39;49;00m win.settings.winMaximized: win.w.maximize()$
   982^I  $
   983^I  win.w.show() [37m# The window has to be shown before[39;49;00m$
   984^I               [37m# setting the position of the VPaned so that[39;49;00m$
   985^I               [37m# it gets set correctly, when the window is maximized.[39;49;00m$
   986^I    $
   987^I  [34mdiscard[39;49;00m win.w.signalConnect([33m"[39;49;00m[33mdestroy[39;49;00m[33m"[39;49;00m, SIGNAL_FUNC(aporia.destroy), [34mnil[39;49;00m)$
   988^I  [34mdiscard[39;49;00m win.w.signalConnect([33m"[39;49;00m[33mdelete_event[39;49;00m[33m"[39;49;00m, $
   989^I    SIGNAL_FUNC(aporia.delete_event), [34mnil[39;49;00m)$
   990^I  [34mdiscard[39;49;00m win.w.signalConnect([33m"[39;49;00m[33mwindow-state-event[39;49;00m[33m"[39;49;00m, $
   991^I    SIGNAL_FUNC(aporia.windowState_Changed), [34mnil[39;49;00m)$
   992^I  $
   993^I  [37m# MainBox (vbox)[39;49;00m$
   994^I  [34mvar[39;49;00m MainBox = vboxNew([34mFalse[39;49;00m, [34m0[39;49;00m)$
   995^I  win.w.add(MainBox)$
   996^I  $
   997^I  initTopMenu(MainBox)$
   998^I  initToolBar(MainBox)$
   999^I  initTAndBP(MainBox)$
  1000^I  initFindBar(MainBox)$
  1001^I  initStatusBar(MainBox)$
  1002^I  $
  1003^I  MainBox.show()$
  1004^I  [34mif[39;49;00m confParseFail:$
  1005^I    dialogs.warning(win.w, [33m"[39;49;00m[33mError parsing config file, using default settings.[39;49;00m[33m"[39;49;00m)$
  1006^I $
  1007^Inimrod_init()$
  1008^IinitControls()$
  1009^Imain()$

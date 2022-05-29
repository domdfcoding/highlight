Using lexer <pygments.lexers.NimrodLexer with {'ensurenl': False, 'tabsize': 0}>
[34mimport[39;49;00m glib2, gtk2, gdk2, gtksourceview, dialogs, os, pango, osproc, strutils
[34mimport[39;49;00m pegs, streams
[34mimport[39;49;00m settings, types, cfg, search

{.push callConv:cdecl.}

[34mconst[39;49;00m
  NimrodProjectExt = [33m"[39;49;00m[33m.nimprj[39;49;00m[33m"[39;49;00m

[34mvar[39;49;00m win: types.MainWin
win.Tabs = @[]

search.win = [34maddr[39;49;00m(win)

[34mvar[39;49;00m lastSession: [36mseq[39;49;00m[[36mstring[39;49;00m] = @[]

[34mvar[39;49;00m confParseFail = [34mFalse[39;49;00m [37m# This gets set to true[39;49;00m
                          [37m# When there is an error parsing the config[39;49;00m

[37m# Load the settings[39;49;00m
[34mtry[39;49;00m:
  win.settings = cfg.load(lastSession)
[34mexcept[39;49;00m ECFGParse:
  [37m# TODO: Make the dialog show the exception[39;49;00m
  confParseFail = [34mTrue[39;49;00m
  win.settings = cfg.defaultSettings()
[34mexcept[39;49;00m EIO:
  win.settings = cfg.defaultSettings()

[34mproc [39;49;00m[32mgetProjectTab[39;49;00m(): [36mint[39;49;00m =
  [34mfor[39;49;00m i [35min[39;49;00m [34m0[39;49;00m..high(win.tabs):
    [34mif[39;49;00m win.tabs[i].filename.endswith(NimrodProjectExt): [34mreturn[39;49;00m i

[34mproc [39;49;00m[32msaveTab[39;49;00m(tabNr: [36mint[39;49;00m, startpath: [36mstring[39;49;00m) =
  [34mif[39;49;00m tabNr < [34m0[39;49;00m: [34mreturn[39;49;00m
  [34mif[39;49;00m win.Tabs[tabNr].saved: [34mreturn[39;49;00m
  [34mvar[39;49;00m path = [33m"[39;49;00m[33m"[39;49;00m
  [34mif[39;49;00m win.Tabs[tabNr].filename == [33m"[39;49;00m[33m"[39;49;00m:
    path = ChooseFileToSave(win.w, startpath)
    [37m# dialogs.nim STOCK_OPEN instead of STOCK_SAVE[39;49;00m
  [34melse[39;49;00m:
    path = win.Tabs[tabNr].filename

  [34mif[39;49;00m path != [33m"[39;49;00m[33m"[39;49;00m:
    [34mvar[39;49;00m buffer = PTextBuffer(win.Tabs[tabNr].buffer)
    [37m# Get the text from the TextView[39;49;00m
    [34mvar[39;49;00m startIter: TTextIter
    buffer.getStartIter([34maddr[39;49;00m(startIter))

    [34mvar[39;49;00m endIter: TTextIter
    buffer.getEndIter([34maddr[39;49;00m(endIter))

    [34mvar[39;49;00m text = buffer.getText([34maddr[39;49;00m(startIter), [34maddr[39;49;00m(endIter), [34mFalse[39;49;00m)
    [37m# Save it to a file[39;49;00m
    [34mvar[39;49;00m f: TFile
    [34mif[39;49;00m open(f, path, fmWrite):
      f.write(text)
      f.close()

      win.tempStuff.lastSaveDir = splitFile(path).dir

      [37m# Change the tab name and .Tabs.filename etc.[39;49;00m
      win.Tabs[tabNr].filename = path
      win.Tabs[tabNr].saved = [34mTrue[39;49;00m
      [34mvar[39;49;00m name = extractFilename(path)

      [34mvar[39;49;00m cTab = win.Tabs[tabNr]
      cTab.label.setText(name)
    [34melse[39;49;00m:
      error(win.w, [33m"[39;49;00m[33mUnable to write to file[39;49;00m[33m"[39;49;00m)

[34mproc [39;49;00m[32msaveAllTabs[39;49;00m() =
  [34mfor[39;49;00m i [35min[39;49;00m [34m0[39;49;00m..high(win.tabs):
    saveTab(i, os.splitFile(win.tabs[i].filename).dir)

[37m# GTK Events[39;49;00m
[37m# -- w(PWindow)[39;49;00m
[34mproc [39;49;00m[32mdestroy[39;49;00m(widget: PWidget, data: pgpointer) {.cdecl.} =
  [37m# gather some settings[39;49;00m
  win.settings.VPanedPos = PPaned(win.sourceViewTabs.getParent()).getPosition()
  win.settings.winWidth = win.w.allocation.width
  win.settings.winHeight = win.w.allocation.height

  [37m# save the settings[39;49;00m
  win.save()
  [37m# then quit[39;49;00m
  main_quit()

[34mproc [39;49;00m[32mdelete_event[39;49;00m(widget: PWidget, event: PEvent, user_data: pgpointer): [36mbool[39;49;00m =
  [34mvar[39;49;00m quit = [34mTrue[39;49;00m
  [34mfor[39;49;00m i [35min[39;49;00m low(win.Tabs)..len(win.Tabs)-[34m1[39;49;00m:
    [34mif[39;49;00m [35mnot[39;49;00m win.Tabs[i].saved:
      [34mvar[39;49;00m askSave = dialogNewWithButtons([33m"[39;49;00m[33m"[39;49;00m, win.w, [34m0[39;49;00m,
                            STOCK_SAVE, RESPONSE_ACCEPT, STOCK_CANCEL,
                            RESPONSE_CANCEL,
                            [33m"[39;49;00m[33mClose without saving[39;49;00m[33m"[39;49;00m, RESPONSE_REJECT, [34mnil[39;49;00m)
      askSave.setTransientFor(win.w)
      [37m# TODO: Make this dialog look better[39;49;00m
      [34mvar[39;49;00m label = labelNew(win.Tabs[i].filename &
          [33m"[39;49;00m[33m is unsaved, would you like to save it ?[39;49;00m[33m"[39;49;00m)
      PBox(askSave.vbox).pack_start(label, [34mFalse[39;49;00m, [34mFalse[39;49;00m, [34m0[39;49;00m)
      label.show()

      [34mvar[39;49;00m resp = askSave.run()
      gtk2.destroy(PWidget(askSave))
      [34mcase[39;49;00m resp
      [34mof[39;49;00m RESPONSE_ACCEPT:
        saveTab(i, os.splitFile(win.tabs[i].filename).dir)
        quit = [34mTrue[39;49;00m
      [34mof[39;49;00m RESPONSE_CANCEL:
        quit = [34mFalse[39;49;00m
        [34mbreak[39;49;00m
      [34mof[39;49;00m RESPONSE_REJECT:
        quit = [34mTrue[39;49;00m
      [34melse[39;49;00m:
        quit = [34mFalse[39;49;00m
        [34mbreak[39;49;00m

  [37m# If False is returned the window will close[39;49;00m
  [34mreturn[39;49;00m [35mnot[39;49;00m quit

[34mproc [39;49;00m[32mwindowState_Changed[39;49;00m(widget: PWidget, event: PEventWindowState,
                         user_data: pgpointer) =
  win.settings.winMaximized = (event.newWindowState [35mand[39;49;00m
                               WINDOW_STATE_MAXIMIZED) != [34m0[39;49;00m

[37m# -- SourceView(PSourceView) & SourceBuffer[39;49;00m
[34mproc [39;49;00m[32mupdateStatusBar[39;49;00m(buffer: PTextBuffer){.cdecl.} =
  [37m# Incase this event gets fired before[39;49;00m
  [37m# bottomBar is initialized[39;49;00m
  [34mif[39;49;00m win.bottomBar != [34mnil[39;49;00m [35mand[39;49;00m [35mnot[39;49;00m win.tempStuff.stopSBUpdates:
    [34mvar[39;49;00m iter: TTextIter

    win.bottomBar.pop([34m0[39;49;00m)
    buffer.getIterAtMark([34maddr[39;49;00m(iter), buffer.getInsert())
    [34mvar[39;49;00m row = getLine([34maddr[39;49;00m(iter)) + [34m1[39;49;00m
    [34mvar[39;49;00m col = getLineOffset([34maddr[39;49;00m(iter))
    [34mdiscard[39;49;00m win.bottomBar.push([34m0[39;49;00m, [33m"[39;49;00m[33mLine: [39;49;00m[33m"[39;49;00m & $row & [33m"[39;49;00m[33m Column: [39;49;00m[33m"[39;49;00m & $col)

[34mproc [39;49;00m[32mcursorMoved[39;49;00m(buffer: PTextBuffer, location: PTextIter,
                 mark: PTextMark, user_data: pgpointer){.cdecl.} =
  updateStatusBar(buffer)

[34mproc [39;49;00m[32monCloseTab[39;49;00m(btn: PButton, user_data: PWidget) =
  [34mif[39;49;00m win.sourceViewTabs.getNPages() > [34m1[39;49;00m:
    [34mvar[39;49;00m tab = win.sourceViewTabs.pageNum(user_data)
    win.sourceViewTabs.removePage(tab)

    win.Tabs.delete(tab)

[34mproc [39;49;00m[32monSwitchTab[39;49;00m(notebook: PNotebook, page: PNotebookPage, pageNum: guint,
                 user_data: pgpointer) =
  [34mif[39;49;00m win.Tabs.len()-[34m1[39;49;00m >= pageNum:
    win.w.setTitle([33m"[39;49;00m[33mAporia IDE - [39;49;00m[33m"[39;49;00m & win.Tabs[pageNum].filename)

[34mproc [39;49;00m[32mcreateTabLabel[39;49;00m(name: [36mstring[39;49;00m, t_child: PWidget): [34mtuple[39;49;00m[box: PWidget,
                    label: PLabel] =
  [34mvar[39;49;00m box = hboxNew([34mFalse[39;49;00m, [34m0[39;49;00m)
  [34mvar[39;49;00m label = labelNew(name)
  [34mvar[39;49;00m closebtn = buttonNew()
  closeBtn.setLabel([34mnil[39;49;00m)
  [34mvar[39;49;00m iconSize = iconSizeFromName([33m"[39;49;00m[33mtabIconSize[39;49;00m[33m"[39;49;00m)
  [34mif[39;49;00m iconSize == [34m0[39;49;00m:
     iconSize = iconSizeRegister([33m"[39;49;00m[33mtabIconSize[39;49;00m[33m"[39;49;00m, [34m10[39;49;00m, [34m10[39;49;00m)
  [34mvar[39;49;00m image = imageNewFromStock(STOCK_CLOSE, iconSize)
  [34mdiscard[39;49;00m gSignalConnect(closebtn, [33m"[39;49;00m[33mclicked[39;49;00m[33m"[39;49;00m, G_Callback(onCloseTab), t_child)
  closebtn.setImage(image)
  gtk2.setRelief(closebtn, RELIEF_NONE)
  box.packStart(label, [34mTrue[39;49;00m, [34mTrue[39;49;00m, [34m0[39;49;00m)
  box.packEnd(closebtn, [34mFalse[39;49;00m, [34mFalse[39;49;00m, [34m0[39;49;00m)
  box.showAll()
  [34mreturn[39;49;00m (box, label)

[34mproc [39;49;00m[32mchanged[39;49;00m(buffer: PTextBuffer, user_data: pgpointer) =
  [37m# Update the 'Line & Column'[39;49;00m
  [37m#updateStatusBar(buffer)[39;49;00m

  [37m# Change the tabs state to 'unsaved'[39;49;00m
  [37m# and add '*' to the Tab Name[39;49;00m
  [34mvar[39;49;00m current = win.SourceViewTabs.getCurrentPage()
  [34mvar[39;49;00m name = [33m"[39;49;00m[33m"[39;49;00m
  [34mif[39;49;00m win.Tabs[current].filename == [33m"[39;49;00m[33m"[39;49;00m:
    win.Tabs[current].saved = [34mFalse[39;49;00m
    name = [33m"[39;49;00m[33mUntitled *[39;49;00m[33m"[39;49;00m
  [34melse[39;49;00m:
    win.Tabs[current].saved = [34mFalse[39;49;00m
    name = extractFilename(win.Tabs[current].filename) & [33m"[39;49;00m[33m *[39;49;00m[33m"[39;49;00m

  [34mvar[39;49;00m cTab = win.Tabs[current]
  cTab.label.setText(name)

[37m# Other(Helper) functions[39;49;00m

[34mproc [39;49;00m[32minitSourceView[39;49;00m(SourceView: [34mvar[39;49;00m PWidget, scrollWindow: [34mvar[39;49;00m PScrolledWindow,
                    buffer: [34mvar[39;49;00m PSourceBuffer) =
  [37m# This gets called by addTab[39;49;00m
  [37m# Each tabs creates a new SourceView[39;49;00m
  [37m# SourceScrolledWindow(ScrolledWindow)[39;49;00m
  scrollWindow = scrolledWindowNew([34mnil[39;49;00m, [34mnil[39;49;00m)
  scrollWindow.setPolicy(POLICY_AUTOMATIC, POLICY_AUTOMATIC)
  scrollWindow.show()

  [37m# SourceView(gtkSourceView)[39;49;00m
  SourceView = sourceViewNew(buffer)
  PSourceView(SourceView).setInsertSpacesInsteadOfTabs([34mTrue[39;49;00m)
  PSourceView(SourceView).setIndentWidth(win.settings.indentWidth)
  PSourceView(SourceView).setShowLineNumbers(win.settings.showLineNumbers)
  PSourceView(SourceView).setHighlightCurrentLine(
               win.settings.highlightCurrentLine)
  PSourceView(SourceView).setShowRightMargin(win.settings.rightMargin)
  PSourceView(SourceView).setAutoIndent(win.settings.autoIndent)

  [34mvar[39;49;00m font = font_description_from_string(win.settings.font)
  SourceView.modifyFont(font)

  scrollWindow.add(SourceView)
  SourceView.show()

  buffer.setHighlightMatchingBrackets(
      win.settings.highlightMatchingBrackets)

  [37m# UGLY workaround for yet another compiler bug:[39;49;00m
  [34mdiscard[39;49;00m gsignalConnect(buffer, [33m"[39;49;00m[33mmark-set[39;49;00m[33m"[39;49;00m,
                         GCallback(aporia.cursorMoved), [34mnil[39;49;00m)
  [34mdiscard[39;49;00m gsignalConnect(buffer, [33m"[39;49;00m[33mchanged[39;49;00m[33m"[39;49;00m, GCallback(aporia.changed), [34mnil[39;49;00m)

  [37m# -- Set the syntax highlighter scheme[39;49;00m
  buffer.setScheme(win.scheme)

[34mproc [39;49;00m[32maddTab[39;49;00m(name, filename: [36mstring[39;49;00m) =
  [33m## Adds a tab, if filename is not "" reads the file. And sets[39;49;00m
  [33m## the tabs SourceViews text to that files contents.[39;49;00m
  assert(win.nimLang != [34mnil[39;49;00m)
  [34mvar[39;49;00m buffer: PSourceBuffer = sourceBufferNew(win.nimLang)

  [34mif[39;49;00m filename != [34mnil[39;49;00m [35mand[39;49;00m filename != [33m"[39;49;00m[33m"[39;49;00m:
    [34mvar[39;49;00m lang = win.langMan.guessLanguage(filename, [34mnil[39;49;00m)
    [34mif[39;49;00m lang != [34mnil[39;49;00m:
      buffer.setLanguage(lang)
    [34melse[39;49;00m:
      buffer.setHighlightSyntax([34mFalse[39;49;00m)

  [34mvar[39;49;00m nam = name
  [34mif[39;49;00m nam == [33m"[39;49;00m[33m"[39;49;00m: nam = [33m"[39;49;00m[33mUntitled[39;49;00m[33m"[39;49;00m
  [34mif[39;49;00m filename == [33m"[39;49;00m[33m"[39;49;00m: nam.add([33m"[39;49;00m[33m *[39;49;00m[33m"[39;49;00m)
  [34melif[39;49;00m filename != [33m"[39;49;00m[33m"[39;49;00m [35mand[39;49;00m name == [33m"[39;49;00m[33m"[39;49;00m:
    [37m# Disable the undo/redo manager.[39;49;00m
    buffer.begin_not_undoable_action()

    [37m# Load the file.[39;49;00m
    [34mvar[39;49;00m file: [36mstring[39;49;00m = readFile(filename)
    [34mif[39;49;00m file != [34mnil[39;49;00m:
      buffer.set_text(file, len(file))

    [37m# Enable the undo/redo manager.[39;49;00m
    buffer.end_not_undoable_action()

    [37m# Get the name.ext of the filename, for the tabs title[39;49;00m
    nam = extractFilename(filename)

  [37m# Init the sourceview[39;49;00m
  [34mvar[39;49;00m sourceView: PWidget
  [34mvar[39;49;00m scrollWindow: PScrolledWindow
  initSourceView(sourceView, scrollWindow, buffer)

  [34mvar[39;49;00m (TabLabel, labelText) = createTabLabel(nam, scrollWindow)
  [37m# Add a tab[39;49;00m
  [34mdiscard[39;49;00m win.SourceViewTabs.appendPage(scrollWindow, TabLabel)

  [34mvar[39;49;00m nTab: Tab
  nTab.buffer = buffer
  nTab.sourceView = sourceView
  nTab.label = labelText
  nTab.saved = (filename != [33m"[39;49;00m[33m"[39;49;00m)
  nTab.filename = filename
  win.Tabs.add(nTab)

  PTextView(SourceView).setBuffer(nTab.buffer)

[37m# GTK Events Contd.[39;49;00m
[37m# -- TopMenu & TopBar[39;49;00m

[34mproc [39;49;00m[32mnewFile[39;49;00m(menuItem: PMenuItem, user_data: pgpointer) =
  addTab([33m"[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33m"[39;49;00m)
  win.sourceViewTabs.setCurrentPage(win.Tabs.len()-[34m1[39;49;00m)

[34mproc [39;49;00m[32mopenFile[39;49;00m(menuItem: PMenuItem, user_data: pgpointer) =
  [34mvar[39;49;00m startpath = [33m"[39;49;00m[33m"[39;49;00m
  [34mvar[39;49;00m currPage = win.SourceViewTabs.getCurrentPage()
  [34mif[39;49;00m currPage <% win.tabs.len:
    startpath = os.splitFile(win.tabs[currPage].filename).dir

  [34mif[39;49;00m startpath.len == [34m0[39;49;00m:
    [37m# Use lastSavePath as the startpath[39;49;00m
    startpath = win.tempStuff.lastSaveDir
    [34mif[39;49;00m startpath.len == [34m0[39;49;00m:
      startpath = os.getHomeDir()

  [34mvar[39;49;00m files = ChooseFilesToOpen(win.w, startpath)
  [34mif[39;49;00m files.len() > [34m0[39;49;00m:
    [34mfor[39;49;00m f [35min[39;49;00m items(files):
      [34mtry[39;49;00m:
        addTab([33m"[39;49;00m[33m"[39;49;00m, f)
      [34mexcept[39;49;00m EIO:
        error(win.w, [33m"[39;49;00m[33mUnable to read from file[39;49;00m[33m"[39;49;00m)
    [37m# Switch to the newly created tab[39;49;00m
    win.sourceViewTabs.setCurrentPage(win.Tabs.len()-[34m1[39;49;00m)

[34mproc [39;49;00m[32msaveFile_Activate[39;49;00m(menuItem: PMenuItem, user_data: pgpointer) =
  [34mvar[39;49;00m current = win.SourceViewTabs.getCurrentPage()
  saveTab(current, os.splitFile(win.tabs[current].filename).dir)

[34mproc [39;49;00m[32msaveFileAs_Activate[39;49;00m(menuItem: PMenuItem, user_data: pgpointer) =
  [34mvar[39;49;00m current = win.SourceViewTabs.getCurrentPage()
  [34mvar[39;49;00m (filename, saved) = (win.Tabs[current].filename, win.Tabs[current].saved)

  win.Tabs[current].saved = [34mFalse[39;49;00m
  win.Tabs[current].filename = [33m"[39;49;00m[33m"[39;49;00m
  saveTab(current, os.splitFile(filename).dir)
  [37m# If the user cancels the save file dialog. Restore the previous filename[39;49;00m
  [37m# and saved state[39;49;00m
  [34mif[39;49;00m win.Tabs[current].filename == [33m"[39;49;00m[33m"[39;49;00m:
    win.Tabs[current].filename = filename
    win.Tabs[current].saved = saved

[34mproc [39;49;00m[32mundo[39;49;00m(menuItem: PMenuItem, user_data: pgpointer) =
  [34mvar[39;49;00m current = win.SourceViewTabs.getCurrentPage()
  [34mif[39;49;00m win.Tabs[current].buffer.canUndo():
    win.Tabs[current].buffer.undo()

[34mproc [39;49;00m[32mredo[39;49;00m(menuItem: PMenuItem, user_data: pgpointer) =
  [34mvar[39;49;00m current = win.SourceViewTabs.getCurrentPage()
  [34mif[39;49;00m win.Tabs[current].buffer.canRedo():
    win.Tabs[current].buffer.redo()

[34mproc [39;49;00m[32mfind_Activate[39;49;00m(menuItem: PMenuItem, user_data: pgpointer) =
  [37m# Get the selected text, and set the findEntry to it.[39;49;00m
  [34mvar[39;49;00m currentTab = win.SourceViewTabs.getCurrentPage()
  [34mvar[39;49;00m insertIter: TTextIter
  win.Tabs[currentTab].buffer.getIterAtMark([34maddr[39;49;00m(insertIter),
                                      win.Tabs[currentTab].buffer.getInsert())
  [34mvar[39;49;00m insertOffset = [34maddr[39;49;00m(insertIter).getOffset()

  [34mvar[39;49;00m selectIter: TTextIter
  win.Tabs[currentTab].buffer.getIterAtMark([34maddr[39;49;00m(selectIter),
                win.Tabs[currentTab].buffer.getSelectionBound())
  [34mvar[39;49;00m selectOffset = [34maddr[39;49;00m(selectIter).getOffset()

  [34mif[39;49;00m insertOffset != selectOffset:
    [34mvar[39;49;00m text = win.Tabs[currentTab].buffer.getText([34maddr[39;49;00m(insertIter),
                                                   [34maddr[39;49;00m(selectIter), [34mfalse[39;49;00m)
    win.findEntry.setText(text)

  win.findBar.show()
  win.findEntry.grabFocus()
  win.replaceEntry.hide()
  win.replaceLabel.hide()
  win.replaceBtn.hide()
  win.replaceAllBtn.hide()

[34mproc [39;49;00m[32mreplace_Activate[39;49;00m(menuitem: PMenuItem, user_data: pgpointer) =
  win.findBar.show()
  win.findEntry.grabFocus()
  win.replaceEntry.show()
  win.replaceLabel.show()
  win.replaceBtn.show()
  win.replaceAllBtn.show()

[34mproc [39;49;00m[32msettings_Activate[39;49;00m(menuitem: PMenuItem, user_data: pgpointer) =
  settings.showSettings(win)

[34mproc [39;49;00m[32mviewBottomPanel_Toggled[39;49;00m(menuitem: PCheckMenuItem, user_data: pgpointer) =
  win.settings.bottomPanelVisible = menuitem.itemGetActive()
  [34mif[39;49;00m win.settings.bottomPanelVisible:
    win.bottomPanelTabs.show()
  [34melse[39;49;00m:
    win.bottomPanelTabs.hide()

[34mvar[39;49;00m
  pegLineError = [33mpeg"[39;49;00m[33m{[^(]*} [39;49;00m[33m'[39;49;00m[33m([39;49;00m[33m'[39;49;00m[33m {[39;49;00m[33m\[39;49;00m[33md+} [39;49;00m[33m'[39;49;00m[33m, [39;49;00m[33m'[39;49;00m[33m [39;49;00m[33m\[39;49;00m[33md+ [39;49;00m[33m'[39;49;00m[33m) Error:[39;49;00m[33m'[39;49;00m[33m [39;49;00m[33m\[39;49;00m[33ms* {.*}[39;49;00m[33m"[39;49;00m
  pegLineWarning = [33mpeg"[39;49;00m[33m{[^(]*} [39;49;00m[33m'[39;49;00m[33m([39;49;00m[33m'[39;49;00m[33m {[39;49;00m[33m\[39;49;00m[33md+} [39;49;00m[33m'[39;49;00m[33m, [39;49;00m[33m'[39;49;00m[33m [39;49;00m[33m\[39;49;00m[33md+ [39;49;00m[33m'[39;49;00m[33m) [39;49;00m[33m'[39;49;00m[33m ([39;49;00m[33m'[39;49;00m[33mWarning:[39;49;00m[33m'[39;49;00m[33m/[39;49;00m[33m'[39;49;00m[33mHint:[39;49;00m[33m'[39;49;00m[33m) [39;49;00m[33m\[39;49;00m[33ms* {.*}[39;49;00m[33m"[39;49;00m
  pegOtherError = [33mpeg"[39;49;00m[33m'[39;49;00m[33mError:[39;49;00m[33m'[39;49;00m[33m [39;49;00m[33m\[39;49;00m[33ms* {.*}[39;49;00m[33m"[39;49;00m
  pegSuccess = [33mpeg"[39;49;00m[33m'[39;49;00m[33mHint: operation successful[39;49;00m[33m'[39;49;00m[33m.*[39;49;00m[33m"[39;49;00m

[34mproc [39;49;00m[32maddText[39;49;00m(textView: PTextView, text: [36mstring[39;49;00m, colorTag: PTextTag = [34mnil[39;49;00m) =
  [34mif[39;49;00m text != [34mnil[39;49;00m:
    [34mvar[39;49;00m iter: TTextIter
    textView.getBuffer().getEndIter([34maddr[39;49;00m(iter))

    [34mif[39;49;00m colorTag == [34mnil[39;49;00m:
      textView.getBuffer().insert([34maddr[39;49;00m(iter), text, len(text))
    [34melse[39;49;00m:
      textView.getBuffer().insertWithTags([34maddr[39;49;00m(iter), text, len(text), colorTag,
                                          [34mnil[39;49;00m)

[34mproc [39;49;00m[32mcreateColor[39;49;00m(textView: PTextView, name, color: [36mstring[39;49;00m): PTextTag =
  [34mvar[39;49;00m tagTable = textView.getBuffer().getTagTable()
  result = tagTable.tableLookup(name)
  [34mif[39;49;00m result == [34mnil[39;49;00m:
    result = textView.getBuffer().createTag(name, [33m"[39;49;00m[33mforeground[39;49;00m[33m"[39;49;00m, color, [34mnil[39;49;00m)

[34mwhen[39;49;00m [35mnot[39;49;00m defined(os.findExe):
  [34mproc [39;49;00m[32mfindExe[39;49;00m(exe: [36mstring[39;49;00m): [36mstring[39;49;00m =
    [33m## returns "" if the exe cannot be found[39;49;00m
    result = addFileExt(exe, os.exeExt)
    [34mif[39;49;00m ExistsFile(result): [34mreturn[39;49;00m
    [34mvar[39;49;00m path = os.getEnv([33m"[39;49;00m[33mPATH[39;49;00m[33m"[39;49;00m)
    [34mfor[39;49;00m candidate [35min[39;49;00m split(path, pathSep):
      [34mvar[39;49;00m x = candidate / result
      [34mif[39;49;00m ExistsFile(x): [34mreturn[39;49;00m x
    result = [33m"[39;49;00m[33m"[39;49;00m

[34mproc [39;49;00m[32mGetCmd[39;49;00m(cmd, filename: [36mstring[39;49;00m): [36mstring[39;49;00m =
  [34mvar[39;49;00m f = quoteIfContainsWhite(filename)
  [34mif[39;49;00m cmd =~ [33mpeg"[39;49;00m[33m\[39;49;00m[33ms* [39;49;00m[33m'[39;49;00m[33m$[39;49;00m[33m'[39;49;00m[33m y[39;49;00m[33m'[39;49;00m[33mfindExe[39;49;00m[33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m[33m([39;49;00m[33m'[39;49;00m[33m {[^)]+} [39;49;00m[33m'[39;49;00m[33m)[39;49;00m[33m'[39;49;00m[33m {.*}[39;49;00m[33m"[39;49;00m:
    [34mvar[39;49;00m exe = quoteIfContainsWhite(findExe(matches[[34m0[39;49;00m]))
    [34mif[39;49;00m exe.len == [34m0[39;49;00m: exe = matches[[34m0[39;49;00m]
    result = exe & [33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m & matches[[34m1[39;49;00m] % f
  [34melse[39;49;00m:
    result = cmd % f

[34mproc [39;49;00m[32mshowBottomPanel[39;49;00m() =
  [34mif[39;49;00m [35mnot[39;49;00m win.settings.bottomPanelVisible:
    win.bottomPanelTabs.show()
    win.settings.bottomPanelVisible = [34mtrue[39;49;00m
    PCheckMenuItem(win.viewBottomPanelMenuItem).itemSetActive([34mtrue[39;49;00m)
  [37m# Scroll to the end of the TextView[39;49;00m
  [37m# This is stupid, it works sometimes... it's random[39;49;00m
  [34mvar[39;49;00m endIter: TTextIter
  win.outputTextView.getBuffer().getEndIter([34maddr[39;49;00m(endIter))
  [34mdiscard[39;49;00m win.outputTextView.scrollToIter(
    [34maddr[39;49;00m(endIter), [34m0[39;49;00m[34m.25[39;49;00m, [34mFalse[39;49;00m, [34m0[39;49;00m[34m.0[39;49;00m, [34m0[39;49;00m[34m.0[39;49;00m)

[34mproc [39;49;00m[32mcompileRun[39;49;00m(currentTab: [36mint[39;49;00m, shouldRun: [36mbool[39;49;00m) =
  [34mif[39;49;00m win.Tabs[currentTab].filename.len == [34m0[39;49;00m: [34mreturn[39;49;00m
  [37m# Clear the outputTextView[39;49;00m
  win.outputTextView.getBuffer().setText([33m"[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m)

  [34mvar[39;49;00m outp = osProc.execProcess(GetCmd(win.settings.nimrodCmd,
                                win.Tabs[currentTab].filename))
  [37m# Colors[39;49;00m
  [34mvar[39;49;00m normalTag = createColor(win.outputTextView, [33m"[39;49;00m[33mnormalTag[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33m#3d3d3d[39;49;00m[33m"[39;49;00m)
  [34mvar[39;49;00m errorTag = createColor(win.outputTextView, [33m"[39;49;00m[33merrorTag[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mred[39;49;00m[33m"[39;49;00m)
  [34mvar[39;49;00m warningTag = createColor(win.outputTextView, [33m"[39;49;00m[33mwarningTag[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mdarkorange[39;49;00m[33m"[39;49;00m)
  [34mvar[39;49;00m successTag = createColor(win.outputTextView, [33m"[39;49;00m[33msuccessTag[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mdarkgreen[39;49;00m[33m"[39;49;00m)
  [34mfor[39;49;00m x [35min[39;49;00m outp.splitLines():
    [34mif[39;49;00m x =~ pegLineError / pegOtherError:
      win.outputTextView.addText([33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m & x, errorTag)
    [34melif[39;49;00m x=~ pegSuccess:
      win.outputTextView.addText([33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m & x, successTag)

      [37m# Launch the process[39;49;00m
      [34mif[39;49;00m shouldRun:
        [34mvar[39;49;00m filename = changeFileExt(win.Tabs[currentTab].filename, os.ExeExt)
        [34mvar[39;49;00m output = [33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m & osProc.execProcess(filename)
        win.outputTextView.addText(output)
    [34melif[39;49;00m x =~ pegLineWarning:
      win.outputTextView.addText([33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m & x, warningTag)
    [34melse[39;49;00m:
      win.outputTextView.addText([33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m & x, normalTag)
  showBottomPanel()

[34mproc [39;49;00m[32mCompileCurrent_Activate[39;49;00m(menuitem: PMenuItem, user_data: pgpointer) =
  saveFile_Activate([34mnil[39;49;00m, [34mnil[39;49;00m)
  compileRun(win.SourceViewTabs.getCurrentPage(), [34mfalse[39;49;00m)

[34mproc [39;49;00m[32mCompileRunCurrent_Activate[39;49;00m(menuitem: PMenuItem, user_data: pgpointer) =
  saveFile_Activate([34mnil[39;49;00m, [34mnil[39;49;00m)
  compileRun(win.SourceViewTabs.getCurrentPage(), [34mtrue[39;49;00m)

[34mproc [39;49;00m[32mCompileProject_Activate[39;49;00m(menuitem: PMenuItem, user_data: pgpointer) =
  saveAllTabs()
  compileRun(getProjectTab(), [34mfalse[39;49;00m)

[34mproc [39;49;00m[32mCompileRunProject_Activate[39;49;00m(menuitem: PMenuItem, user_data: pgpointer) =
  saveAllTabs()
  compileRun(getProjectTab(), [34mtrue[39;49;00m)

[34mproc [39;49;00m[32mRunCustomCommand[39;49;00m(cmd: [36mstring[39;49;00m) =
  saveFile_Activate([34mnil[39;49;00m, [34mnil[39;49;00m)
  [34mvar[39;49;00m currentTab = win.SourceViewTabs.getCurrentPage()
  [34mif[39;49;00m win.Tabs[currentTab].filename.len == [34m0[39;49;00m [35mor[39;49;00m cmd.len == [34m0[39;49;00m: [34mreturn[39;49;00m
  [37m# Clear the outputTextView[39;49;00m
  win.outputTextView.getBuffer().setText([33m"[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m)
  [34mvar[39;49;00m outp = osProc.execProcess(GetCmd(cmd, win.Tabs[currentTab].filename))
  [34mvar[39;49;00m normalTag = createColor(win.outputTextView, [33m"[39;49;00m[33mnormalTag[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33m#3d3d3d[39;49;00m[33m"[39;49;00m)
  [34mfor[39;49;00m x [35min[39;49;00m outp.splitLines():
    win.outputTextView.addText([33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m & x, normalTag)
  showBottomPanel()

[34mproc [39;49;00m[32mRunCustomCommand1[39;49;00m(menuitem: PMenuItem, user_data: pgpointer) =
  RunCustomCommand(win.settings.customCmd1)

[34mproc [39;49;00m[32mRunCustomCommand2[39;49;00m(menuitem: PMenuItem, user_data: pgpointer) =
  RunCustomCommand(win.settings.customCmd2)

[34mproc [39;49;00m[32mRunCustomCommand3[39;49;00m(menuitem: PMenuItem, user_data: pgpointer) =
  RunCustomCommand(win.settings.customCmd3)

[37m# -- FindBar[39;49;00m

[34mproc [39;49;00m[32mnextBtn_Clicked[39;49;00m(button: PButton, user_data: pgpointer) = findText([34mTrue[39;49;00m)
[34mproc [39;49;00m[32mprevBtn_Clicked[39;49;00m(button: PButton, user_data: pgpointer) = findText([34mFalse[39;49;00m)

[34mproc [39;49;00m[32mreplaceBtn_Clicked[39;49;00m(button: PButton, user_data: pgpointer) =
  [34mvar[39;49;00m currentTab = win.SourceViewTabs.getCurrentPage()
  [34mvar[39;49;00m start, theEnd: TTextIter
  [34mif[39;49;00m [35mnot[39;49;00m win.Tabs[currentTab].buffer.getSelectionBounds(
        [34maddr[39;49;00m(start), [34maddr[39;49;00m(theEnd)):
    [37m# If no text is selected, try finding a match.[39;49;00m
    findText([34mTrue[39;49;00m)
    [34mif[39;49;00m [35mnot[39;49;00m win.Tabs[currentTab].buffer.getSelectionBounds(
          [34maddr[39;49;00m(start), [34maddr[39;49;00m(theEnd)):
      [37m# No match[39;49;00m
      [34mreturn[39;49;00m

  [37m# Remove the text[39;49;00m
  win.Tabs[currentTab].buffer.delete([34maddr[39;49;00m(start), [34maddr[39;49;00m(theEnd))
  [37m# Insert the replacement[39;49;00m
  [34mvar[39;49;00m text = getText(win.replaceEntry)
  win.Tabs[currentTab].buffer.insert([34maddr[39;49;00m(start), text, len(text))

[34mproc [39;49;00m[32mreplaceAllBtn_Clicked[39;49;00m(button: PButton, user_data: pgpointer) =
  [34mvar[39;49;00m find = getText(win.findEntry)
  [34mvar[39;49;00m replace = getText(win.replaceEntry)
  [34mdiscard[39;49;00m replaceAll(find, replace)

[34mproc [39;49;00m[32mcloseBtn_Clicked[39;49;00m(button: PButton, user_data: pgpointer) =
  win.findBar.hide()

[34mproc [39;49;00m[32mcaseSens_Changed[39;49;00m(radiomenuitem: PRadioMenuitem, user_data: pgpointer) =
  win.settings.search = [33m"[39;49;00m[33mcasesens[39;49;00m[33m"[39;49;00m
[34mproc [39;49;00m[32mcaseInSens_Changed[39;49;00m(radiomenuitem: PRadioMenuitem, user_data: pgpointer) =
  win.settings.search = [33m"[39;49;00m[33mcaseinsens[39;49;00m[33m"[39;49;00m
[34mproc [39;49;00m[32mstyle_Changed[39;49;00m(radiomenuitem: PRadioMenuitem, user_data: pgpointer) =
  win.settings.search = [33m"[39;49;00m[33mstyle[39;49;00m[33m"[39;49;00m
[34mproc [39;49;00m[32mregex_Changed[39;49;00m(radiomenuitem: PRadioMenuitem, user_data: pgpointer) =
  win.settings.search = [33m"[39;49;00m[33mregex[39;49;00m[33m"[39;49;00m
[34mproc [39;49;00m[32mpeg_Changed[39;49;00m(radiomenuitem: PRadioMenuitem, user_data: pgpointer) =
  win.settings.search = [33m"[39;49;00m[33mpeg[39;49;00m[33m"[39;49;00m

[34mproc [39;49;00m[32mextraBtn_Clicked[39;49;00m(button: PButton, user_data: pgpointer) =
  [34mvar[39;49;00m extraMenu = menuNew()
  [34mvar[39;49;00m group: PGSList

  [34mvar[39;49;00m caseSensMenuItem = radio_menu_item_new(group, [33m"[39;49;00m[33mCase sensitive[39;49;00m[33m"[39;49;00m)
  extraMenu.append(caseSensMenuItem)
  [34mdiscard[39;49;00m signal_connect(caseSensMenuItem, [33m"[39;49;00m[33mtoggled[39;49;00m[33m"[39;49;00m,
                          SIGNAL_FUNC(caseSens_Changed), [34mnil[39;49;00m)
  caseSensMenuItem.show()
  group = caseSensMenuItem.ItemGetGroup()

  [34mvar[39;49;00m caseInSensMenuItem = radio_menu_item_new(group, [33m"[39;49;00m[33mCase insensitive[39;49;00m[33m"[39;49;00m)
  extraMenu.append(caseInSensMenuItem)
  [34mdiscard[39;49;00m signal_connect(caseInSensMenuItem, [33m"[39;49;00m[33mtoggled[39;49;00m[33m"[39;49;00m,
                          SIGNAL_FUNC(caseInSens_Changed), [34mnil[39;49;00m)
  caseInSensMenuItem.show()
  group = caseInSensMenuItem.ItemGetGroup()

  [34mvar[39;49;00m styleMenuItem = radio_menu_item_new(group, [33m"[39;49;00m[33mStyle insensitive[39;49;00m[33m"[39;49;00m)
  extraMenu.append(styleMenuItem)
  [34mdiscard[39;49;00m signal_connect(styleMenuItem, [33m"[39;49;00m[33mtoggled[39;49;00m[33m"[39;49;00m,
                          SIGNAL_FUNC(style_Changed), [34mnil[39;49;00m)
  styleMenuItem.show()
  group = styleMenuItem.ItemGetGroup()

  [34mvar[39;49;00m regexMenuItem = radio_menu_item_new(group, [33m"[39;49;00m[33mRegex[39;49;00m[33m"[39;49;00m)
  extraMenu.append(regexMenuItem)
  [34mdiscard[39;49;00m signal_connect(regexMenuItem, [33m"[39;49;00m[33mtoggled[39;49;00m[33m"[39;49;00m,
                          SIGNAL_FUNC(regex_Changed), [34mnil[39;49;00m)
  regexMenuItem.show()
  group = regexMenuItem.ItemGetGroup()

  [34mvar[39;49;00m pegMenuItem = radio_menu_item_new(group, [33m"[39;49;00m[33mPegs[39;49;00m[33m"[39;49;00m)
  extraMenu.append(pegMenuItem)
  [34mdiscard[39;49;00m signal_connect(pegMenuItem, [33m"[39;49;00m[33mtoggled[39;49;00m[33m"[39;49;00m,
                          SIGNAL_FUNC(peg_Changed), [34mnil[39;49;00m)
  pegMenuItem.show()

  [37m# Make the correct radio button active[39;49;00m
  [34mcase[39;49;00m win.settings.search
  [34mof[39;49;00m [33m"[39;49;00m[33mcasesens[39;49;00m[33m"[39;49;00m:
    PCheckMenuItem(caseSensMenuItem).ItemSetActive([34mTrue[39;49;00m)
  [34mof[39;49;00m [33m"[39;49;00m[33mcaseinsens[39;49;00m[33m"[39;49;00m:
    PCheckMenuItem(caseInSensMenuItem).ItemSetActive([34mTrue[39;49;00m)
  [34mof[39;49;00m [33m"[39;49;00m[33mstyle[39;49;00m[33m"[39;49;00m:
    PCheckMenuItem(styleMenuItem).ItemSetActive([34mTrue[39;49;00m)
  [34mof[39;49;00m [33m"[39;49;00m[33mregex[39;49;00m[33m"[39;49;00m:
    PCheckMenuItem(regexMenuItem).ItemSetActive([34mTrue[39;49;00m)
  [34mof[39;49;00m [33m"[39;49;00m[33mpeg[39;49;00m[33m"[39;49;00m:
    PCheckMenuItem(pegMenuItem).ItemSetActive([34mTrue[39;49;00m)

  extraMenu.popup([34mnil[39;49;00m, [34mnil[39;49;00m, [34mnil[39;49;00m, [34mnil[39;49;00m, [34m0[39;49;00m, get_current_event_time())

[37m# GUI Initialization[39;49;00m

[34mproc [39;49;00m[32mcreateAccelMenuItem[39;49;00m(toolsMenu: PMenu, accGroup: PAccelGroup,
                         label: [36mstring[39;49;00m, acc: gint,
                         action: [34mproc[39;49;00m (i: PMenuItem, p: pgpointer)) =
  [34mvar[39;49;00m result = menu_item_new(label)
  result.addAccelerator([33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m, accGroup, acc, [34m0[39;49;00m, ACCEL_VISIBLE)
  ToolsMenu.append(result)
  show(result)
  [34mdiscard[39;49;00m signal_connect(result, [33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m, SIGNAL_FUNC(action), [34mnil[39;49;00m)

[34mproc [39;49;00m[32mcreateSeparator[39;49;00m(menu: PMenu) =
  [34mvar[39;49;00m sep = separator_menu_item_new()
  menu.append(sep)
  sep.show()

[34mproc [39;49;00m[32minitTopMenu[39;49;00m(MainBox: PBox) =
  [37m# Create a accelerator group, used for shortcuts[39;49;00m
  [37m# like CTRL + S in SaveMenuItem[39;49;00m
  [34mvar[39;49;00m accGroup = accel_group_new()
  add_accel_group(win.w, accGroup)

  [37m# TopMenu(MenuBar)[39;49;00m
  [34mvar[39;49;00m TopMenu = menuBarNew()

  [37m# FileMenu[39;49;00m
  [34mvar[39;49;00m FileMenu = menuNew()

  [34mvar[39;49;00m NewMenuItem = menu_item_new([33m"[39;49;00m[33mNew[39;49;00m[33m"[39;49;00m) [37m# New[39;49;00m
  FileMenu.append(NewMenuItem)
  show(NewMenuItem)
  [34mdiscard[39;49;00m signal_connect(NewMenuItem, [33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m,
                          SIGNAL_FUNC(newFile), [34mnil[39;49;00m)

  createSeparator(FileMenu)

  [34mvar[39;49;00m OpenMenuItem = menu_item_new([33m"[39;49;00m[33mOpen...[39;49;00m[33m"[39;49;00m) [37m# Open...[39;49;00m
  [37m# CTRL + O[39;49;00m
  OpenMenuItem.add_accelerator([33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m, accGroup,
                  KEY_o, CONTROL_MASK, ACCEL_VISIBLE)
  FileMenu.append(OpenMenuItem)
  show(OpenMenuItem)
  [34mdiscard[39;49;00m signal_connect(OpenMenuItem, [33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m,
                          SIGNAL_FUNC(aporia.openFile), [34mnil[39;49;00m)

  [34mvar[39;49;00m SaveMenuItem = menu_item_new([33m"[39;49;00m[33mSave[39;49;00m[33m"[39;49;00m) [37m# Save[39;49;00m
  [37m# CTRL + S[39;49;00m
  SaveMenuItem.add_accelerator([33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m, accGroup,
                  KEY_s, CONTROL_MASK, ACCEL_VISIBLE)
  FileMenu.append(SaveMenuItem)
  show(SaveMenuItem)
  [34mdiscard[39;49;00m signal_connect(SaveMenuItem, [33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m,
                          SIGNAL_FUNC(saveFile_activate), [34mnil[39;49;00m)

  [34mvar[39;49;00m SaveAsMenuItem = menu_item_new([33m"[39;49;00m[33mSave As...[39;49;00m[33m"[39;49;00m) [37m# Save as...[39;49;00m

  SaveAsMenuItem.add_accelerator([33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m, accGroup,
                  KEY_s, CONTROL_MASK [35mor[39;49;00m gdk2.SHIFT_MASK, ACCEL_VISIBLE)
  FileMenu.append(SaveAsMenuItem)
  show(SaveAsMenuItem)
  [34mdiscard[39;49;00m signal_connect(SaveAsMenuItem, [33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m,
                          SIGNAL_FUNC(saveFileAs_Activate), [34mnil[39;49;00m)

  [34mvar[39;49;00m FileMenuItem = menuItemNewWithMnemonic([33m"[39;49;00m[33m_File[39;49;00m[33m"[39;49;00m)

  FileMenuItem.setSubMenu(FileMenu)
  FileMenuItem.show()
  TopMenu.append(FileMenuItem)

  [37m# Edit menu[39;49;00m
  [34mvar[39;49;00m EditMenu = menuNew()

  [34mvar[39;49;00m UndoMenuItem = menu_item_new([33m"[39;49;00m[33mUndo[39;49;00m[33m"[39;49;00m) [37m# Undo[39;49;00m
  EditMenu.append(UndoMenuItem)
  show(UndoMenuItem)
  [34mdiscard[39;49;00m signal_connect(UndoMenuItem, [33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m,
                          SIGNAL_FUNC(aporia.undo), [34mnil[39;49;00m)

  [34mvar[39;49;00m RedoMenuItem = menu_item_new([33m"[39;49;00m[33mRedo[39;49;00m[33m"[39;49;00m) [37m# Undo[39;49;00m
  EditMenu.append(RedoMenuItem)
  show(RedoMenuItem)
  [34mdiscard[39;49;00m signal_connect(RedoMenuItem, [33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m,
                          SIGNAL_FUNC(aporia.redo), [34mnil[39;49;00m)

  createSeparator(EditMenu)

  [34mvar[39;49;00m FindMenuItem = menu_item_new([33m"[39;49;00m[33mFind[39;49;00m[33m"[39;49;00m) [37m# Find[39;49;00m
  FindMenuItem.add_accelerator([33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m, accGroup,
                  KEY_f, CONTROL_MASK, ACCEL_VISIBLE)
  EditMenu.append(FindMenuItem)
  show(FindMenuItem)
  [34mdiscard[39;49;00m signal_connect(FindMenuItem, [33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m,
                          SIGNAL_FUNC(aporia.find_Activate), [34mnil[39;49;00m)

  [34mvar[39;49;00m ReplaceMenuItem = menu_item_new([33m"[39;49;00m[33mReplace[39;49;00m[33m"[39;49;00m) [37m# Replace[39;49;00m
  ReplaceMenuItem.add_accelerator([33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m, accGroup,
                  KEY_h, CONTROL_MASK, ACCEL_VISIBLE)
  EditMenu.append(ReplaceMenuItem)
  show(ReplaceMenuItem)
  [34mdiscard[39;49;00m signal_connect(ReplaceMenuItem, [33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m,
                          SIGNAL_FUNC(aporia.replace_Activate), [34mnil[39;49;00m)

  createSeparator(EditMenu)

  [34mvar[39;49;00m SettingsMenuItem = menu_item_new([33m"[39;49;00m[33mSettings...[39;49;00m[33m"[39;49;00m) [37m# Settings[39;49;00m
  EditMenu.append(SettingsMenuItem)
  show(SettingsMenuItem)
  [34mdiscard[39;49;00m signal_connect(SettingsMenuItem, [33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m,
                          SIGNAL_FUNC(aporia.Settings_Activate), [34mnil[39;49;00m)

  [34mvar[39;49;00m EditMenuItem = menuItemNewWithMnemonic([33m"[39;49;00m[33m_Edit[39;49;00m[33m"[39;49;00m)

  EditMenuItem.setSubMenu(EditMenu)
  EditMenuItem.show()
  TopMenu.append(EditMenuItem)

  [37m# View menu[39;49;00m
  [34mvar[39;49;00m ViewMenu = menuNew()

  win.viewBottomPanelMenuItem = check_menu_item_new([33m"[39;49;00m[33mBottom Panel[39;49;00m[33m"[39;49;00m)
  PCheckMenuItem(win.viewBottomPanelMenuItem).itemSetActive(
         win.settings.bottomPanelVisible)
  win.viewBottomPanelMenuItem.add_accelerator([33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m, accGroup,
                  KEY_f9, CONTROL_MASK, ACCEL_VISIBLE)
  ViewMenu.append(win.viewBottomPanelMenuItem)
  show(win.viewBottomPanelMenuItem)
  [34mdiscard[39;49;00m signal_connect(win.viewBottomPanelMenuItem, [33m"[39;49;00m[33mtoggled[39;49;00m[33m"[39;49;00m,
                          SIGNAL_FUNC(aporia.viewBottomPanel_Toggled), [34mnil[39;49;00m)

  [34mvar[39;49;00m ViewMenuItem = menuItemNewWithMnemonic([33m"[39;49;00m[33m_View[39;49;00m[33m"[39;49;00m)

  ViewMenuItem.setSubMenu(ViewMenu)
  ViewMenuItem.show()
  TopMenu.append(ViewMenuItem)


  [37m# Tools menu[39;49;00m
  [34mvar[39;49;00m ToolsMenu = menuNew()

  createAccelMenuItem(ToolsMenu, accGroup, [33m"[39;49;00m[33mCompile current file[39;49;00m[33m"[39;49;00m,
                      KEY_F4, aporia.CompileCurrent_Activate)
  createAccelMenuItem(ToolsMenu, accGroup, [33m"[39;49;00m[33mCompile & run current file[39;49;00m[33m"[39;49;00m,
                      KEY_F5, aporia.CompileRunCurrent_Activate)
  createSeparator(ToolsMenu)
  createAccelMenuItem(ToolsMenu, accGroup, [33m"[39;49;00m[33mCompile project[39;49;00m[33m"[39;49;00m,
                      KEY_F8, aporia.CompileProject_Activate)
  createAccelMenuItem(ToolsMenu, accGroup, [33m"[39;49;00m[33mCompile & run project[39;49;00m[33m"[39;49;00m,
                      KEY_F9, aporia.CompileRunProject_Activate)
  createSeparator(ToolsMenu)
  createAccelMenuItem(ToolsMenu, accGroup, [33m"[39;49;00m[33mRun custom command 1[39;49;00m[33m"[39;49;00m,
                      KEY_F1, aporia.RunCustomCommand1)
  createAccelMenuItem(ToolsMenu, accGroup, [33m"[39;49;00m[33mRun custom command 2[39;49;00m[33m"[39;49;00m,
                      KEY_F2, aporia.RunCustomCommand2)
  createAccelMenuItem(ToolsMenu, accGroup, [33m"[39;49;00m[33mRun custom command 3[39;49;00m[33m"[39;49;00m,
                      KEY_F3, aporia.RunCustomCommand3)

  [34mvar[39;49;00m ToolsMenuItem = menuItemNewWithMnemonic([33m"[39;49;00m[33m_Tools[39;49;00m[33m"[39;49;00m)

  ToolsMenuItem.setSubMenu(ToolsMenu)
  ToolsMenuItem.show()
  TopMenu.append(ToolsMenuItem)

  [37m# Help menu[39;49;00m
  MainBox.packStart(TopMenu, [34mFalse[39;49;00m, [34mFalse[39;49;00m, [34m0[39;49;00m)
  TopMenu.show()

[34mproc [39;49;00m[32minitToolBar[39;49;00m(MainBox: PBox) =
  [37m# TopBar(ToolBar)[39;49;00m
  [34mvar[39;49;00m TopBar = toolbarNew()
  TopBar.setStyle(TOOLBAR_ICONS)

  [34mvar[39;49;00m NewFileItem = TopBar.insertStock(STOCK_NEW, [33m"[39;49;00m[33mNew File[39;49;00m[33m"[39;49;00m,
                      [33m"[39;49;00m[33mNew File[39;49;00m[33m"[39;49;00m, SIGNAL_FUNC(aporia.newFile), [34mnil[39;49;00m, [34m0[39;49;00m)
  TopBar.appendSpace()
  [34mvar[39;49;00m OpenItem = TopBar.insertStock(STOCK_OPEN, [33m"[39;49;00m[33mOpen[39;49;00m[33m"[39;49;00m,
                      [33m"[39;49;00m[33mOpen[39;49;00m[33m"[39;49;00m, SIGNAL_FUNC(aporia.openFile), [34mnil[39;49;00m, -[34m1[39;49;00m)
  [34mvar[39;49;00m SaveItem = TopBar.insertStock(STOCK_SAVE, [33m"[39;49;00m[33mSave[39;49;00m[33m"[39;49;00m,
                      [33m"[39;49;00m[33mSave[39;49;00m[33m"[39;49;00m, SIGNAL_FUNC(saveFile_Activate), [34mnil[39;49;00m, -[34m1[39;49;00m)
  TopBar.appendSpace()
  [34mvar[39;49;00m UndoItem = TopBar.insertStock(STOCK_UNDO, [33m"[39;49;00m[33mUndo[39;49;00m[33m"[39;49;00m,
                      [33m"[39;49;00m[33mUndo[39;49;00m[33m"[39;49;00m, SIGNAL_FUNC(aporia.undo), [34mnil[39;49;00m, -[34m1[39;49;00m)
  [34mvar[39;49;00m RedoItem = TopBar.insertStock(STOCK_REDO, [33m"[39;49;00m[33mRedo[39;49;00m[33m"[39;49;00m,
                      [33m"[39;49;00m[33mRedo[39;49;00m[33m"[39;49;00m, SIGNAL_FUNC(aporia.redo), [34mnil[39;49;00m, -[34m1[39;49;00m)

  MainBox.packStart(TopBar, [34mFalse[39;49;00m, [34mFalse[39;49;00m, [34m0[39;49;00m)
  TopBar.show()

[34mproc [39;49;00m[32minitSourceViewTabs[39;49;00m() =
  win.SourceViewTabs = notebookNew()
  [37m#win.sourceViewTabs.dragDestSet(DEST_DEFAULT_DROP, nil, 0, ACTION_MOVE)[39;49;00m
  [34mdiscard[39;49;00m win.SourceViewTabs.signalConnect(
          [33m"[39;49;00m[33mswitch-page[39;49;00m[33m"[39;49;00m, SIGNAL_FUNC(onSwitchTab), [34mnil[39;49;00m)
  [37m#discard win.SourceViewTabs.signalConnect([39;49;00m
  [37m#        "drag-drop", SIGNAL_FUNC(svTabs_DragDrop), nil)[39;49;00m
  [37m#discard win.SourceViewTabs.signalConnect([39;49;00m
  [37m#        "drag-data-received", SIGNAL_FUNC(svTabs_DragDataRecv), nil)[39;49;00m
  [37m#discard win.SourceViewTabs.signalConnect([39;49;00m
  [37m#        "drag-motion", SIGNAL_FUNC(svTabs_DragMotion), nil)[39;49;00m
  win.SourceViewTabs.set_scrollable([34mTrue[39;49;00m)

  win.SourceViewTabs.show()
  [34mif[39;49;00m lastSession.len != [34m0[39;49;00m:
    [34mfor[39;49;00m i [35min[39;49;00m [34m0[39;49;00m .. len(lastSession)-[34m1[39;49;00m:
      [34mvar[39;49;00m splitUp = lastSession[i].split([33m'[39;49;00m[33m|[39;49;00m[33m'[39;49;00m)
      [34mvar[39;49;00m (filename, offset) = (splitUp[[34m0[39;49;00m], splitUp[[34m1[39;49;00m])
      addTab([33m"[39;49;00m[33m"[39;49;00m, filename)

      [34mvar[39;49;00m iter: TTextIter
      win.Tabs[i].buffer.getIterAtOffset([34maddr[39;49;00m(iter), offset.parseInt())
      win.Tabs[i].buffer.moveMarkByName([33m"[39;49;00m[33minsert[39;49;00m[33m"[39;49;00m, [34maddr[39;49;00m(iter))
      win.Tabs[i].buffer.moveMarkByName([33m"[39;49;00m[33mselection_bound[39;49;00m[33m"[39;49;00m, [34maddr[39;49;00m(iter))

      [37m# TODO: Fix this..... :([39;49;00m
      [34mdiscard[39;49;00m PTextView(win.Tabs[i].sourceView).
          scrollToIter([34maddr[39;49;00m(iter), [34m0[39;49;00m[34m.25[39;49;00m, [34mtrue[39;49;00m, [34m0[39;49;00m[34m.0[39;49;00m, [34m0[39;49;00m[34m.0[39;49;00m)
  [34melse[39;49;00m:
    addTab([33m"[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33m"[39;49;00m)

  [37m# This doesn't work :\[39;49;00m
  win.Tabs[[34m0[39;49;00m].sourceView.grabFocus()


[34mproc [39;49;00m[32minitBottomTabs[39;49;00m() =
  win.bottomPanelTabs = notebookNew()
  [34mif[39;49;00m win.settings.bottomPanelVisible:
    win.bottomPanelTabs.show()

  [37m# output tab[39;49;00m
  [34mvar[39;49;00m tabLabel = labelNew([33m"[39;49;00m[33mOutput[39;49;00m[33m"[39;49;00m)
  [34mvar[39;49;00m outputTab = vboxNew([34mFalse[39;49;00m, [34m0[39;49;00m)
  [34mdiscard[39;49;00m win.bottomPanelTabs.appendPage(outputTab, tabLabel)
  [37m# Compiler tabs, gtktextview[39;49;00m
  [34mvar[39;49;00m outputScrolledWindow = scrolledwindowNew([34mnil[39;49;00m, [34mnil[39;49;00m)
  outputScrolledWindow.setPolicy(POLICY_AUTOMATIC, POLICY_AUTOMATIC)
  outputTab.packStart(outputScrolledWindow, [34mtrue[39;49;00m, [34mtrue[39;49;00m, [34m0[39;49;00m)
  outputScrolledWindow.show()

  win.outputTextView = textviewNew()
  outputScrolledWindow.add(win.outputTextView)
  win.outputTextView.show()

  outputTab.show()

[34mproc [39;49;00m[32minitTAndBP[39;49;00m(MainBox: PBox) =
  [37m# This init's the HPaned, which splits the sourceViewTabs[39;49;00m
  [37m# and the BottomPanelTabs[39;49;00m
  initSourceViewTabs()
  initBottomTabs()

  [34mvar[39;49;00m TAndBPVPaned = vpanedNew()
  tandbpVPaned.pack1(win.sourceViewTabs, resize=[34mTrue[39;49;00m, shrink=[34mFalse[39;49;00m)
  tandbpVPaned.pack2(win.bottomPanelTabs, resize=[34mFalse[39;49;00m, shrink=[34mFalse[39;49;00m)
  MainBox.packStart(TAndBPVPaned, [34mTrue[39;49;00m, [34mTrue[39;49;00m, [34m0[39;49;00m)
  tandbpVPaned.setPosition(win.settings.VPanedPos)
  TAndBPVPaned.show()

[34mproc [39;49;00m[32minitFindBar[39;49;00m(MainBox: PBox) =
  [37m# Create a fixed container[39;49;00m
  win.findBar = HBoxNew([34mFalse[39;49;00m, [34m0[39;49;00m)
  win.findBar.setSpacing([34m4[39;49;00m)

  [37m# Add a Label 'Find'[39;49;00m
  [34mvar[39;49;00m findLabel = labelNew([33m"[39;49;00m[33mFind:[39;49;00m[33m"[39;49;00m)
  win.findBar.packStart(findLabel, [34mFalse[39;49;00m, [34mFalse[39;49;00m, [34m0[39;49;00m)
  findLabel.show()

  [37m# Add a (find) text entry[39;49;00m
  win.findEntry = entryNew()
  win.findBar.packStart(win.findEntry, [34mFalse[39;49;00m, [34mFalse[39;49;00m, [34m0[39;49;00m)
  [34mdiscard[39;49;00m win.findEntry.signalConnect([33m"[39;49;00m[33mactivate[39;49;00m[33m"[39;49;00m, SIGNAL_FUNC(
                                      aporia.nextBtn_Clicked), [34mnil[39;49;00m)
  win.findEntry.show()
  [34mvar[39;49;00m rq: TRequisition
  win.findEntry.sizeRequest([34maddr[39;49;00m(rq))

  [37m# Make the (find) text entry longer[39;49;00m
  win.findEntry.set_size_request([34m190[39;49;00m, rq.height)

  [37m# Add a Label 'Replace' [39;49;00m
  [37m# - This Is only shown, when the 'Search & Replace'(CTRL + H) is shown[39;49;00m
  win.replaceLabel = labelNew([33m"[39;49;00m[33mReplace:[39;49;00m[33m"[39;49;00m)
  win.findBar.packStart(win.replaceLabel, [34mFalse[39;49;00m, [34mFalse[39;49;00m, [34m0[39;49;00m)
  [37m#replaceLabel.show()[39;49;00m

  [37m# Add a (replace) text entry [39;49;00m
  [37m# - This Is only shown, when the 'Search & Replace'(CTRL + H) is shown[39;49;00m
  win.replaceEntry = entryNew()
  win.findBar.packStart(win.replaceEntry, [34mFalse[39;49;00m, [34mFalse[39;49;00m, [34m0[39;49;00m)
  [37m#win.replaceEntry.show()[39;49;00m
  [34mvar[39;49;00m rq1: TRequisition
  win.replaceEntry.sizeRequest([34maddr[39;49;00m(rq1))

  [37m# Make the (replace) text entry longer[39;49;00m
  win.replaceEntry.set_size_request([34m100[39;49;00m, rq1.height)

  [37m# Find next button[39;49;00m
  [34mvar[39;49;00m nextBtn = buttonNew([33m"[39;49;00m[33mNext[39;49;00m[33m"[39;49;00m)
  win.findBar.packStart(nextBtn, [34mfalse[39;49;00m, [34mfalse[39;49;00m, [34m0[39;49;00m)
  [34mdiscard[39;49;00m nextBtn.signalConnect([33m"[39;49;00m[33mclicked[39;49;00m[33m"[39;49;00m,
             SIGNAL_FUNC(aporia.nextBtn_Clicked), [34mnil[39;49;00m)
  nextBtn.show()
  [34mvar[39;49;00m nxtBtnRq: TRequisition
  nextBtn.sizeRequest([34maddr[39;49;00m(nxtBtnRq))

  [37m# Find previous button[39;49;00m
  [34mvar[39;49;00m prevBtn = buttonNew([33m"[39;49;00m[33mPrevious[39;49;00m[33m"[39;49;00m)
  win.findBar.packStart(prevBtn, [34mfalse[39;49;00m, [34mfalse[39;49;00m, [34m0[39;49;00m)
  [34mdiscard[39;49;00m prevBtn.signalConnect([33m"[39;49;00m[33mclicked[39;49;00m[33m"[39;49;00m,
             SIGNAL_FUNC(aporia.prevBtn_Clicked), [34mnil[39;49;00m)
  prevBtn.show()

  [37m# Replace button[39;49;00m
  [37m# - This Is only shown, when the 'Search & Replace'(CTRL + H) is shown[39;49;00m
  win.replaceBtn = buttonNew([33m"[39;49;00m[33mReplace[39;49;00m[33m"[39;49;00m)
  win.findBar.packStart(win.replaceBtn, [34mfalse[39;49;00m, [34mfalse[39;49;00m, [34m0[39;49;00m)
  [34mdiscard[39;49;00m win.replaceBtn.signalConnect([33m"[39;49;00m[33mclicked[39;49;00m[33m"[39;49;00m,
             SIGNAL_FUNC(aporia.replaceBtn_Clicked), [34mnil[39;49;00m)
  [37m#replaceBtn.show()[39;49;00m

  [37m# Replace all button[39;49;00m
  [37m# - this Is only shown, when the 'Search & Replace'(CTRL + H) is shown[39;49;00m
  win.replaceAllBtn = buttonNew([33m"[39;49;00m[33mReplace All[39;49;00m[33m"[39;49;00m)
  win.findBar.packStart(win.replaceAllBtn, [34mfalse[39;49;00m, [34mfalse[39;49;00m, [34m0[39;49;00m)
  [34mdiscard[39;49;00m win.replaceAllBtn.signalConnect([33m"[39;49;00m[33mclicked[39;49;00m[33m"[39;49;00m,
             SIGNAL_FUNC(aporia.replaceAllBtn_Clicked), [34mnil[39;49;00m)
  [37m#replaceAllBtn.show()[39;49;00m

  [37m# Right side ...[39;49;00m

  [37m# Close button - With a close stock image[39;49;00m
  [34mvar[39;49;00m closeBtn = buttonNew()
  [34mvar[39;49;00m closeImage = imageNewFromStock(STOCK_CLOSE, ICON_SIZE_SMALL_TOOLBAR)
  [34mvar[39;49;00m closeBox = hboxNew([34mFalse[39;49;00m, [34m0[39;49;00m)
  closeBtn.add(closeBox)
  closeBox.show()
  closeBox.add(closeImage)
  closeImage.show()
  [34mdiscard[39;49;00m closeBtn.signalConnect([33m"[39;49;00m[33mclicked[39;49;00m[33m"[39;49;00m,
             SIGNAL_FUNC(aporia.closeBtn_Clicked), [34mnil[39;49;00m)
  win.findBar.packEnd(closeBtn, [34mFalse[39;49;00m, [34mFalse[39;49;00m, [34m2[39;49;00m)
  closeBtn.show()

  [37m# Extra button - When clicked shows a menu with options like 'Use regex'[39;49;00m
  [34mvar[39;49;00m extraBtn = buttonNew()
  [34mvar[39;49;00m extraImage = imageNewFromStock(STOCK_PROPERTIES, ICON_SIZE_SMALL_TOOLBAR)

  [34mvar[39;49;00m extraBox = hboxNew([34mFalse[39;49;00m, [34m0[39;49;00m)
  extraBtn.add(extraBox)
  extraBox.show()
  extraBox.add(extraImage)
  extraImage.show()
  [34mdiscard[39;49;00m extraBtn.signalConnect([33m"[39;49;00m[33mclicked[39;49;00m[33m"[39;49;00m,
             SIGNAL_FUNC(aporia.extraBtn_Clicked), [34mnil[39;49;00m)
  win.findBar.packEnd(extraBtn, [34mFalse[39;49;00m, [34mFalse[39;49;00m, [34m0[39;49;00m)
  extraBtn.show()

  MainBox.packStart(win.findBar, [34mFalse[39;49;00m, [34mFalse[39;49;00m, [34m0[39;49;00m)
  win.findBar.show()

[34mproc [39;49;00m[32minitStatusBar[39;49;00m(MainBox: PBox) =
  win.bottomBar = statusbarNew()
  MainBox.packStart(win.bottomBar, [34mFalse[39;49;00m, [34mFalse[39;49;00m, [34m0[39;49;00m)
  win.bottomBar.show()

  [34mdiscard[39;49;00m win.bottomBar.push([34m0[39;49;00m, [33m"[39;49;00m[33mLine: 0 Column: 0[39;49;00m[33m"[39;49;00m)

[34mproc [39;49;00m[32minitControls[39;49;00m() =
  [37m# Load up the language style[39;49;00m
  win.langMan = languageManagerGetDefault()
  [34mvar[39;49;00m langpaths: [36marray[39;49;00m[[34m0[39;49;00m..[34m1[39;49;00m, cstring] =
          [cstring(os.getApplicationDir() / langSpecs), [34mnil[39;49;00m]
  win.langMan.setSearchPath([34maddr[39;49;00m(langpaths))
  [34mvar[39;49;00m nimLang = win.langMan.getLanguage([33m"[39;49;00m[33mnimrod[39;49;00m[33m"[39;49;00m)
  win.nimLang = nimLang

  [37m# Load the scheme[39;49;00m
  [34mvar[39;49;00m schemeMan = schemeManagerGetDefault()
  [34mvar[39;49;00m schemepaths: [36marray[39;49;00m[[34m0[39;49;00m..[34m1[39;49;00m, cstring] =
          [cstring(os.getApplicationDir() / styles), [34mnil[39;49;00m]
  schemeMan.setSearchPath([34maddr[39;49;00m(schemepaths))
  win.scheme = schemeMan.getScheme(win.settings.colorSchemeID)

  [37m# Window[39;49;00m
  win.w = windowNew(gtk2.WINDOW_TOPLEVEL)
  win.w.setDefaultSize(win.settings.winWidth, win.settings.winHeight)
  win.w.setTitle([33m"[39;49;00m[33mAporia IDE[39;49;00m[33m"[39;49;00m)
  [34mif[39;49;00m win.settings.winMaximized: win.w.maximize()

  win.w.show() [37m# The window has to be shown before[39;49;00m
               [37m# setting the position of the VPaned so that[39;49;00m
               [37m# it gets set correctly, when the window is maximized.[39;49;00m

  [34mdiscard[39;49;00m win.w.signalConnect([33m"[39;49;00m[33mdestroy[39;49;00m[33m"[39;49;00m, SIGNAL_FUNC(aporia.destroy), [34mnil[39;49;00m)
  [34mdiscard[39;49;00m win.w.signalConnect([33m"[39;49;00m[33mdelete_event[39;49;00m[33m"[39;49;00m,
    SIGNAL_FUNC(aporia.delete_event), [34mnil[39;49;00m)
  [34mdiscard[39;49;00m win.w.signalConnect([33m"[39;49;00m[33mwindow-state-event[39;49;00m[33m"[39;49;00m,
    SIGNAL_FUNC(aporia.windowState_Changed), [34mnil[39;49;00m)

  [37m# MainBox (vbox)[39;49;00m
  [34mvar[39;49;00m MainBox = vboxNew([34mFalse[39;49;00m, [34m0[39;49;00m)
  win.w.add(MainBox)

  initTopMenu(MainBox)
  initToolBar(MainBox)
  initTAndBP(MainBox)
  initFindBar(MainBox)
  initStatusBar(MainBox)

  MainBox.show()
  [34mif[39;49;00m confParseFail:
    dialogs.warning(win.w, [33m"[39;49;00m[33mError parsing config file, using default settings.[39;49;00m[33m"[39;49;00m)

nimrod_init()
initControls()
main()

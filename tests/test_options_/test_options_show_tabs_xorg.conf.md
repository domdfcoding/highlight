[33mSection[39;49;00m [33m"Files"[39;49;00m
^I[36mModulePath[39;49;00m [31m"/usr/lib64/opengl/nvidia/extensions"[39;49;00m
^I[36mModulePath[39;49;00m [31m"/usr/lib64/xorg/modules"[39;49;00m
[33mEndSection[39;49;00m

[33mSection[39;49;00m [33m"ServerLayout"[39;49;00m
^I[36mIdentifier[39;49;00m     [31m"XFree86 Configured"[39;49;00m
^I[36mScreen[39;49;00m [31m"Screen"[39;49;00m
[33mEndSection[39;49;00m

[33mSection[39;49;00m [33m"ServerFlags"[39;49;00m
^I[36mOption[39;49;00m [31m"AutoAddDevices" "false"[39;49;00m
[33mEndSection[39;49;00m

[33mSection[39;49;00m [33m"Screen"[39;49;00m
        [36mIdentifier[39;49;00m [31m"Screen"[39;49;00m
^I[36mDevice[39;49;00m [31m"Card0"[39;49;00m
^I[36mDefaultDepth[39;49;00m    [31m24[39;49;00m
^I[33mSubSection[39;49;00m     [33m"Display"[39;49;00m
^I^I[36mDepth[39;49;00m       [31m24[39;49;00m
^I[33mEndSubSection[39;49;00m
        [36mOption[39;49;00m [31m"UseEDIDDpi" "False"[39;49;00m
        [36mOption[39;49;00m [31m"DPI" "96 x 96"[39;49;00m
[33mEndSection[39;49;00m

[33mSection[39;49;00m [33m"Device"[39;49;00m
    [36mIdentifier[39;49;00m  [31m"Card0"[39;49;00m
    [36mDriver[39;49;00m      [31m"nvidia"[39;49;00m
    [36mVendorName[39;49;00m  [31m"NVIDIA Corporation" [39;49;00m[37m# inline comment[39;49;00m
    [37m#Option      "RenderAccel" "true"[39;49;00m

    [37m#Option      "NvAgp" "3"[39;49;00m
    [37m#Option      "AllowGLXWithComposite" "true"[39;49;00m
    [37m#Option      "AddARGBGLXVisuals" "true"[39;49;00m
    [37m#Option      "XAANoOffscreenPixmaps" "true"[39;49;00m
    [37m#Option      "DRI" "true"[39;49;00m

    [37m#Option      "UseEvents" "false"[39;49;00m
    [37m#Option      "TripleBuffer" "1"[39;49;00m
    [37m#Option      "DamageEvents" "1"[39;49;00m
    [37m##Option      "BackingStore" "1"[39;49;00m
    [37m#Option      "PixmapCacheSize" "70000"[39;49;00m
    [37m#Option      "OnDemandVBlankInterrupts" "true"[39;49;00m
[33mEndSection[39;49;00m

[33mSection[39;49;00m [33m"Extensions"[39;49;00m
[37m#    Option "Composite" "Disabled"[39;49;00m
[33mEndSection[39;49;00m

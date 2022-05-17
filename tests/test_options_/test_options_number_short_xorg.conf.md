     1	[33mSection[39;49;00m [33m"Files"[39;49;00m
     2		[36mModulePath[39;49;00m [31m"/usr/lib64/opengl/nvidia/extensions"[39;49;00m
     3		[36mModulePath[39;49;00m [31m"/usr/lib64/xorg/modules"[39;49;00m
     4	[33mEndSection[39;49;00m
     5
     6	[33mSection[39;49;00m [33m"ServerLayout"[39;49;00m
     7		[36mIdentifier[39;49;00m     [31m"XFree86 Configured"[39;49;00m
     8		[36mScreen[39;49;00m [31m"Screen"[39;49;00m
     9	[33mEndSection[39;49;00m
    10
    11	[33mSection[39;49;00m [33m"ServerFlags"[39;49;00m
    12		[36mOption[39;49;00m [31m"AutoAddDevices" "false"[39;49;00m
    13	[33mEndSection[39;49;00m
    14
    15	[33mSection[39;49;00m [33m"Screen"[39;49;00m
    16	        [36mIdentifier[39;49;00m [31m"Screen"[39;49;00m
    17		[36mDevice[39;49;00m [31m"Card0"[39;49;00m
    18		[36mDefaultDepth[39;49;00m    [31m24[39;49;00m
    19		[33mSubSection[39;49;00m     [33m"Display"[39;49;00m
    20			[36mDepth[39;49;00m       [31m24[39;49;00m
    21		[33mEndSubSection[39;49;00m
    22	        [36mOption[39;49;00m [31m"UseEDIDDpi" "False"[39;49;00m
    23	        [36mOption[39;49;00m [31m"DPI" "96 x 96"[39;49;00m
    24	[33mEndSection[39;49;00m
    25
    26	[33mSection[39;49;00m [33m"Device"[39;49;00m
    27	    [36mIdentifier[39;49;00m  [31m"Card0"[39;49;00m
    28	    [36mDriver[39;49;00m      [31m"nvidia"[39;49;00m
    29	    [36mVendorName[39;49;00m  [31m"NVIDIA Corporation" [39;49;00m[37m# inline comment[39;49;00m
    30	    [37m#Option      "RenderAccel" "true"[39;49;00m
    31
    32	    [37m#Option      "NvAgp" "3"[39;49;00m
    33	    [37m#Option      "AllowGLXWithComposite" "true"[39;49;00m
    34	    [37m#Option      "AddARGBGLXVisuals" "true"[39;49;00m
    35	    [37m#Option      "XAANoOffscreenPixmaps" "true"[39;49;00m
    36	    [37m#Option      "DRI" "true"[39;49;00m
    37
    38	    [37m#Option      "UseEvents" "false"[39;49;00m
    39	    [37m#Option      "TripleBuffer" "1"[39;49;00m
    40	    [37m#Option      "DamageEvents" "1"[39;49;00m
    41	    [37m##Option      "BackingStore" "1"[39;49;00m
    42	    [37m#Option      "PixmapCacheSize" "70000"[39;49;00m
    43	    [37m#Option      "OnDemandVBlankInterrupts" "true"[39;49;00m
    44	[33mEndSection[39;49;00m
    45
    46	[33mSection[39;49;00m [33m"Extensions"[39;49;00m
    47	[37m#    Option "Composite" "Disabled"[39;49;00m
    48	[33mEndSection[39;49;00m

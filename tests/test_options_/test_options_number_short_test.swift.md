     1	[37m//[39;49;00m
     2	[37m//[39;49;00m[37m [39;49;00m[37m [39;49;00m[37mt[39;49;00m[37me[39;49;00m[37ms[39;49;00m[37mt[39;49;00m[37m.[39;49;00m[37ms[39;49;00m[37mw[39;49;00m[37mi[39;49;00m[37mf[39;49;00m[37mt[39;49;00m
     3	[37m//[39;49;00m[37m [39;49;00m[37m [39;49;00m[37mf[39;49;00m[37mr[39;49;00m[37mo[39;49;00m[37mm[39;49;00m[37m [39;49;00m[37mh[39;49;00m[37mt[39;49;00m[37mt[39;49;00m[37mp[39;49;00m[37ms[39;49;00m[37m:[39;49;00m[37m/[39;49;00m[37m/[39;49;00m[37mg[39;49;00m[37mi[39;49;00m[37mt[39;49;00m[37mh[39;49;00m[37mu[39;49;00m[37mb[39;49;00m[37m.[39;49;00m[37mc[39;49;00m[37mo[39;49;00m[37mm[39;49;00m[37m/[39;49;00m[37mf[39;49;00m[37mu[39;49;00m[37ml[39;49;00m[37ml[39;49;00m[37ms[39;49;00m[37mt[39;49;00m[37ma[39;49;00m[37mc[39;49;00m[37mk[39;49;00m[37mi[39;49;00m[37mo[39;49;00m[37m/[39;49;00m[37mF[39;49;00m[37ml[39;49;00m[37ma[39;49;00m[37mp[39;49;00m[37mp[39;49;00m[37my[39;49;00m[37mS[39;49;00m[37mw[39;49;00m[37mi[39;49;00m[37mf[39;49;00m[37mt[39;49;00m
     4	[37m//[39;49;00m
     5	[37m//[39;49;00m[37m [39;49;00m[37m [39;49;00m[37mC[39;49;00m[37mr[39;49;00m[37me[39;49;00m[37ma[39;49;00m[37mt[39;49;00m[37me[39;49;00m[37md[39;49;00m[37m [39;49;00m[37mb[39;49;00m[37my[39;49;00m[37m [39;49;00m[37mN[39;49;00m[37ma[39;49;00m[37mt[39;49;00m[37me[39;49;00m[37m [39;49;00m[37mM[39;49;00m[37mu[39;49;00m[37mr[39;49;00m[37mr[39;49;00m[37ma[39;49;00m[37my[39;49;00m[37m [39;49;00m[37mo[39;49;00m[37mn[39;49;00m[37m [39;49;00m[37m6[39;49;00m[37m/[39;49;00m[37m2[39;49;00m[37m/[39;49;00m[37m1[39;49;00m[37m4[39;49;00m[37m.[39;49;00m
     6	[37m//[39;49;00m[37m [39;49;00m[37m [39;49;00m[37mC[39;49;00m[37mo[39;49;00m[37mp[39;49;00m[37my[39;49;00m[37mr[39;49;00m[37mi[39;49;00m[37mg[39;49;00m[37mh[39;49;00m[37mt[39;49;00m[37m [39;49;00m[37m([39;49;00m[37mc[39;49;00m[37m)[39;49;00m[37m [39;49;00m[37m2[39;49;00m[37m0[39;49;00m[37m1[39;49;00m[37m4[39;49;00m[37m [39;49;00m[37mF[39;49;00m[37mu[39;49;00m[37ml[39;49;00m[37ml[39;49;00m[37ms[39;49;00m[37mt[39;49;00m[37ma[39;49;00m[37mc[39;49;00m[37mk[39;49;00m[37m.[39;49;00m[37mi[39;49;00m[37mo[39;49;00m[37m.[39;49;00m[37m [39;49;00m[37mA[39;49;00m[37ml[39;49;00m[37ml[39;49;00m[37m [39;49;00m[37mr[39;49;00m[37mi[39;49;00m[37mg[39;49;00m[37mh[39;49;00m[37mt[39;49;00m[37ms[39;49;00m[37m [39;49;00m[37mr[39;49;00m[37me[39;49;00m[37ms[39;49;00m[37me[39;49;00m[37mr[39;49;00m[37mv[39;49;00m[37me[39;49;00m[37md[39;49;00m[37m.[39;49;00m
     7	[37m//[39;49;00m
     8
     9	[34mimport[39;49;00m [04m[32mUIKit[39;49;00m
    10	[34mimport[39;49;00m [04m[32mSpriteKit[39;49;00m
    11
    12	[34mextension[39;49;00m [36mSKNode[39;49;00m {
    13	    [34mclass[39;49;00m [04m[32mfunc[39;49;00m unarchiveFromFile(file : [36mNSString[39;49;00m) -> [36mSKNode[39;49;00m? {
    14
    15	        [34mlet[39;49;00m [31mpath[39;49;00m = [36mNSBundle[39;49;00m.mainBundle().pathForResource(file, ofType: [33m"[39;49;00m[33msks[39;49;00m[33m"[39;49;00m)
    16
    17	        [34mvar[39;49;00m [31msceneData[39;49;00m = [36mNSData[39;49;00m.dataWithContentsOfFile(path, options: .DataReadingMappedIfSafe, error: [34mnil[39;49;00m)
    18	        [34mvar[39;49;00m [31marchiver[39;49;00m = [36mNSKeyedUnarchiver[39;49;00m(forReadingWithData: sceneData)
    19
    20	        archiver.setClass([34mself[39;49;00m.classForKeyedUnarchiver(), forClassName: [33m"[39;49;00m[33mSKScene[39;49;00m[33m"[39;49;00m)
    21	        [34mlet[39;49;00m [31mscene[39;49;00m = archiver.decodeObjectForKey(NSKeyedArchiveRootObjectKey) [34mas[39;49;00m GameScene
    22	        archiver.finishDecoding()
    23	        [34mreturn[39;49;00m scene
    24	    }
    25	}
    26
    27	[34mclass[39;49;00m [04m[32mGameViewController[39;49;00m: [36mUIViewController[39;49;00m {
    28
    29	    [34moverride[39;49;00m [34mfunc[39;49;00m [32mviewDidLoad[39;49;00m() {
    30	        [34msuper[39;49;00m.viewDidLoad()
    31
    32	        [34mif[39;49;00m [34mlet[39;49;00m [31mscene[39;49;00m = GameScene.unarchiveFromFile([33m"[39;49;00m[33mGameScene[39;49;00m[33m"[39;49;00m) [34mas[39;49;00m? GameScene {
    33	            [37m//[39;49;00m[37m [39;49;00m[37mC[39;49;00m[37mo[39;49;00m[37mn[39;49;00m[37mf[39;49;00m[37mi[39;49;00m[37mg[39;49;00m[37mu[39;49;00m[37mr[39;49;00m[37me[39;49;00m[37m [39;49;00m[37mt[39;49;00m[37mh[39;49;00m[37me[39;49;00m[37m [39;49;00m[37mv[39;49;00m[37mi[39;49;00m[37me[39;49;00m[37mw[39;49;00m[37m.[39;49;00m
    34	            [34mlet[39;49;00m [31mskView[39;49;00m = [34mself[39;49;00m.view [34mas[39;49;00m [36mSKView[39;49;00m
    35	            skView.showsFPS = [34mtrue[39;49;00m
    36	            skView.showsNodeCount = [34mtrue[39;49;00m
    37
    38	            [37m/*[39;49;00m[37m [39;49;00m[37mS[39;49;00m[37mp[39;49;00m[37mr[39;49;00m[37mi[39;49;00m[37mt[39;49;00m[37me[39;49;00m[37m [39;49;00m[37mK[39;49;00m[37mi[39;49;00m[37mt[39;49;00m[37m [39;49;00m[37ma[39;49;00m[37mp[39;49;00m[37mp[39;49;00m[37ml[39;49;00m[37mi[39;49;00m[37me[39;49;00m[37ms[39;49;00m[37m [39;49;00m[37ma[39;49;00m[37md[39;49;00m[37md[39;49;00m[37mi[39;49;00m[37mt[39;49;00m[37mi[39;49;00m[37mo[39;49;00m[37mn[39;49;00m[37ma[39;49;00m[37ml[39;49;00m[37m [39;49;00m[37mo[39;49;00m[37mp[39;49;00m[37mt[39;49;00m[37mi[39;49;00m[37mm[39;49;00m[37mi[39;49;00m[37mz[39;49;00m[37ma[39;49;00m[37mt[39;49;00m[37mi[39;49;00m[37mo[39;49;00m[37mn[39;49;00m[37ms[39;49;00m[37m [39;49;00m[37mt[39;49;00m[37mo[39;49;00m[37m [39;49;00m[37mi[39;49;00m[37mm[39;49;00m[37mp[39;49;00m[37mr[39;49;00m[37mo[39;49;00m[37mv[39;49;00m[37me[39;49;00m[37m [39;49;00m[37mr[39;49;00m[37me[39;49;00m[37mn[39;49;00m[37md[39;49;00m[37me[39;49;00m[37mr[39;49;00m[37mi[39;49;00m[37mn[39;49;00m[37mg[39;49;00m[37m [39;49;00m[37mp[39;49;00m[37me[39;49;00m[37mr[39;49;00m[37mf[39;49;00m[37mo[39;49;00m[37mr[39;49;00m[37mm[39;49;00m[37ma[39;49;00m[37mn[39;49;00m[37mc[39;49;00m[37me[39;49;00m[37m [39;49;00m[37m*/[39;49;00m
    39	            skView.ignoresSiblingOrder = [34mtrue[39;49;00m
    40
    41	            [37m/*[39;49;00m[37m [39;49;00m[37mS[39;49;00m[37me[39;49;00m[37mt[39;49;00m[37m [39;49;00m[37mt[39;49;00m[37mh[39;49;00m[37me[39;49;00m[37m [39;49;00m[37ms[39;49;00m[37mc[39;49;00m[37ma[39;49;00m[37ml[39;49;00m[37me[39;49;00m[37m [39;49;00m[37mm[39;49;00m[37mo[39;49;00m[37md[39;49;00m[37me[39;49;00m[37m [39;49;00m[37mt[39;49;00m[37mo[39;49;00m[37m [39;49;00m[37ms[39;49;00m[37mc[39;49;00m[37ma[39;49;00m[37ml[39;49;00m[37me[39;49;00m[37m [39;49;00m[37mt[39;49;00m[37mo[39;49;00m[37m [39;49;00m[37mf[39;49;00m[37mi[39;49;00m[37mt[39;49;00m[37m [39;49;00m[37mt[39;49;00m[37mh[39;49;00m[37me[39;49;00m[37m [39;49;00m[37mw[39;49;00m[37mi[39;49;00m[37mn[39;49;00m[37md[39;49;00m[37mo[39;49;00m[37mw[39;49;00m[37m [39;49;00m[37m*/[39;49;00m
    42	            scene.scaleMode = .AspectFill
    43
    44	            skView.presentScene(scene)
    45	        }
    46	    }
    47
    48	    [34moverride[39;49;00m [34mfunc[39;49;00m [32mshouldAutorotate[39;49;00m() -> [36mBool[39;49;00m {
    49	        [34mreturn[39;49;00m [34mtrue[39;49;00m
    50	    }
    51
    52	    [34moverride[39;49;00m [34mfunc[39;49;00m [32msupportedInterfaceOrientations[39;49;00m() -> [36mInt[39;49;00m {
    53	        [34mif[39;49;00m [36mUIDevice[39;49;00m.currentDevice().userInterfaceIdiom == .Phone {
    54	            [34mreturn[39;49;00m [36mInt[39;49;00m(UIInterfaceOrientationMask.AllButUpsideDown.toRaw())
    55	        } [34melse[39;49;00m {
    56	            [34mreturn[39;49;00m [36mInt[39;49;00m(UIInterfaceOrientationMask.All.toRaw())
    57	        }
    58	    }
    59
    60	    [34moverride[39;49;00m [34mfunc[39;49;00m [32mdidReceiveMemoryWarning[39;49;00m() {
    61	        [34msuper[39;49;00m.didReceiveMemoryWarning()
    62	        [37m//[39;49;00m[37m [39;49;00m[37mR[39;49;00m[37me[39;49;00m[37ml[39;49;00m[37me[39;49;00m[37ma[39;49;00m[37ms[39;49;00m[37me[39;49;00m[37m [39;49;00m[37ma[39;49;00m[37mn[39;49;00m[37my[39;49;00m[37m [39;49;00m[37mc[39;49;00m[37ma[39;49;00m[37mc[39;49;00m[37mh[39;49;00m[37me[39;49;00m[37md[39;49;00m[37m [39;49;00m[37md[39;49;00m[37ma[39;49;00m[37mt[39;49;00m[37ma[39;49;00m[37m,[39;49;00m[37m [39;49;00m[37mi[39;49;00m[37mm[39;49;00m[37ma[39;49;00m[37mg[39;49;00m[37me[39;49;00m[37ms[39;49;00m[37m,[39;49;00m[37m [39;49;00m[37me[39;49;00m[37mt[39;49;00m[37mc[39;49;00m[37m [39;49;00m[37mt[39;49;00m[37mh[39;49;00m[37ma[39;49;00m[37mt[39;49;00m[37m [39;49;00m[37ma[39;49;00m[37mr[39;49;00m[37me[39;49;00m[37mn[39;49;00m[37m'[39;49;00m[37mt[39;49;00m[37m [39;49;00m[37mi[39;49;00m[37mn[39;49;00m[37m [39;49;00m[37mu[39;49;00m[37ms[39;49;00m[37me[39;49;00m[37m.[39;49;00m
    63	    }
    64
    65	}

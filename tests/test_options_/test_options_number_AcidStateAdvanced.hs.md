     1	[37m{-[39;49;00m[37m# LANGUAGE DeriveDataTypeable, FlexibleContexts, GeneralizedNewtypeDeriving[39;49;00m
     2	[37m  , MultiParamTypeClasses, OverloadedStrings, ScopedTypeVariables, TemplateHaskell[39;49;00m
     3	[37m  , TypeFamilies, FlexibleInstances #[39;49;00m[37m-}[39;49;00m[37m[39;49;00m
     4	[34mmodule[39;49;00m[37m [39;49;00m[04m[36mMain[39;49;00m[37m [39;49;00m[34mwhere[39;49;00m[37m[39;49;00m
     5	[34mimport[39;49;00m[37m [39;49;00m[04m[36mControl.Applicative[39;49;00m[37m  [39;49;00m([36mApplicative[39;49;00m,[37m [39;49;00m[36mAlternative[39;49;00m,[37m [39;49;00m(<$>))[37m[39;49;00m
     6	[34mimport[39;49;00m[37m [39;49;00m[04m[36mControl.Exception.Lifted[39;49;00m[37m    [39;49;00m([32mbracket[39;49;00m)[37m[39;49;00m
     7	[34mimport[39;49;00m[37m [39;49;00m[04m[36mControl.Monad.Trans.Control[39;49;00m[37m [39;49;00m([36mMonadBaseControl[39;49;00m)[37m[39;49;00m
     8	[34mimport[39;49;00m[37m [39;49;00m[04m[36mControl.Monad[39;49;00m[37m        [39;49;00m([36mMonadPlus[39;49;00m,[37m [39;49;00m[32mmplus[39;49;00m)[37m[39;49;00m
     9	[34mimport[39;49;00m[37m [39;49;00m[04m[36mControl.Monad.Reader[39;49;00m[37m [39;49;00m([36mMonadReader[39;49;00m,[37m [39;49;00m[36mReaderT[39;49;00m(..),[37m [39;49;00m[32mask[39;49;00m)[37m[39;49;00m
    10	[34mimport[39;49;00m[37m [39;49;00m[04m[36mControl.Monad.Trans[39;49;00m[37m  [39;49;00m([36mMonadIO[39;49;00m(..))[37m[39;49;00m
    11	[34mimport[39;49;00m[37m [39;49;00m[04m[36mData.Acid[39;49;00m[37m            [39;49;00m([37m [39;49;00m[36mAcidState[39;49;00m(..),[37m [39;49;00m[36mEventState[39;49;00m(..),[37m [39;49;00m[36mEventResult[39;49;00m(..)[37m[39;49;00m
    12	[37m                            [39;49;00m,[37m [39;49;00m[36mQuery[39;49;00m(..),[37m [39;49;00m[36mQueryEvent[39;49;00m(..),[37m [39;49;00m[36mUpdate[39;49;00m(..),[37m [39;49;00m[36mUpdateEvent[39;49;00m(..)[37m[39;49;00m
    13	[37m                            [39;49;00m,[37m [39;49;00m[36mIsAcidic[39;49;00m(..),[37m [39;49;00m[32mmakeAcidic[39;49;00m,[37m [39;49;00m[32mopenLocalState[39;49;00m[37m[39;49;00m
    14	[37m                            [39;49;00m)[37m[39;49;00m
    15	[34mimport[39;49;00m[37m [39;49;00m[04m[36mData.Acid.Local[39;49;00m[37m      [39;49;00m([37m [39;49;00m[32mcreateCheckpointAndClose[39;49;00m[37m[39;49;00m
    16	[37m                            [39;49;00m,[37m [39;49;00m[32mopenLocalStateFrom[39;49;00m[37m[39;49;00m
    17	[37m                            [39;49;00m)[37m[39;49;00m
    18	[34mimport[39;49;00m[37m [39;49;00m[04m[36mData.Acid.Advanced[39;49;00m[37m   [39;49;00m([32mquery'[39;49;00m,[37m [39;49;00m[32mupdate'[39;49;00m)[37m[39;49;00m
    19	[34mimport[39;49;00m[37m [39;49;00m[04m[36mData.Maybe[39;49;00m[37m           [39;49;00m([32mfromMaybe[39;49;00m)[37m[39;49;00m
    20	[34mimport[39;49;00m[37m [39;49;00m[04m[36mData.SafeCopy[39;49;00m[37m        [39;49;00m([36mSafeCopy[39;49;00m,[37m [39;49;00m[32mbase[39;49;00m,[37m [39;49;00m[32mderiveSafeCopy[39;49;00m)[37m[39;49;00m
    21	[34mimport[39;49;00m[37m [39;49;00m[04m[36mData.Data[39;49;00m[37m            [39;49;00m([36mData[39;49;00m,[37m [39;49;00m[36mTypeable[39;49;00m)[37m[39;49;00m
    22	[34mimport[39;49;00m[37m [39;49;00m[04m[36mData.Lens[39;49;00m[37m            [39;49;00m((%=),[37m [39;49;00m(!=))[37m[39;49;00m
    23	[34mimport[39;49;00m[37m [39;49;00m[04m[36mData.Lens.Template[39;49;00m[37m   [39;49;00m([32mmakeLens[39;49;00m)[37m[39;49;00m
    24	[34mimport[39;49;00m[37m [39;49;00m[04m[36mData.Text.Lazy[39;49;00m[37m       [39;49;00m([36mText[39;49;00m)[37m[39;49;00m
    25	[34mimport[39;49;00m[37m [39;49;00m[04m[36mHappstack.Server[39;49;00m[37m     [39;49;00m([37m [39;49;00m[36mHappstack[39;49;00m,[37m [39;49;00m[36mHasRqData[39;49;00m,[37m [39;49;00m[36mMethod[39;49;00m([36mGET[39;49;00m,[37m [39;49;00m[36mPOST[39;49;00m),[37m [39;49;00m[36mRequest[39;49;00m([32mrqMethod[39;49;00m)[37m[39;49;00m
    26	[37m                            [39;49;00m,[37m [39;49;00m[36mResponse[39;49;00m[37m[39;49;00m
    27	[37m                            [39;49;00m,[37m [39;49;00m[36mServerPartT[39;49;00m(..),[37m [39;49;00m[36mWebMonad[39;49;00m,[37m [39;49;00m[36mFilterMonad[39;49;00m,[37m [39;49;00m[36mServerMonad[39;49;00m[37m[39;49;00m
    28	[37m                            [39;49;00m,[37m [39;49;00m[32maskRq[39;49;00m,[37m [39;49;00m[32mdecodeBody[39;49;00m,[37m [39;49;00m[32mdir[39;49;00m,[37m [39;49;00m[32mdefaultBodyPolicy[39;49;00m,[37m [39;49;00m[32mlookText[39;49;00m[37m[39;49;00m
    29	[37m                            [39;49;00m,[37m [39;49;00m[32mmapServerPartT[39;49;00m,[37m [39;49;00m[32mnullConf[39;49;00m,[37m [39;49;00m[32mnullDir[39;49;00m,[37m [39;49;00m[32mok[39;49;00m,[37m [39;49;00m[32msimpleHTTP[39;49;00m[37m[39;49;00m
    30	[37m                            [39;49;00m,[37m [39;49;00m[32mtoResponse[39;49;00m[37m[39;49;00m
    31	[37m                            [39;49;00m)[37m[39;49;00m
    32	[34mimport[39;49;00m[37m [39;49;00m[04m[36mPrelude[39;49;00m[37m [39;49;00m[34mhiding[39;49;00m[37m       [39;49;00m([32mhead[39;49;00m,[37m [39;49;00m[32mid[39;49;00m)[37m[39;49;00m
    33	[34mimport[39;49;00m[37m [39;49;00m[04m[36mSystem.FilePath[39;49;00m[37m      [39;49;00m((</>))[37m[39;49;00m
    34	[34mimport[39;49;00m[37m [39;49;00m[04m[36mText.Blaze[39;49;00m[37m           [39;49;00m((!))[37m[39;49;00m
    35	[34mimport[39;49;00m[37m [39;49;00m[04m[36mText.Blaze.Html4.Strict[39;49;00m[37m [39;49;00m([32mbody[39;49;00m,[37m [39;49;00m[32mhead[39;49;00m,[37m [39;49;00m[32mhtml[39;49;00m,[37m [39;49;00m[32minput[39;49;00m,[37m [39;49;00m[32mform[39;49;00m,[37m [39;49;00m[32mlabel[39;49;00m,[37m [39;49;00m[32mp[39;49;00m,[37m [39;49;00m[32mtitle[39;49;00m,[37m [39;49;00m[32mtoHtml[39;49;00m)[37m[39;49;00m
    36	[34mimport[39;49;00m[37m [39;49;00m[04m[36mText.Blaze.Html4.Strict.Attributes[39;49;00m[37m [39;49;00m([32maction[39;49;00m,[37m [39;49;00m[32menctype[39;49;00m,[37m [39;49;00m[32mfor[39;49;00m,[37m [39;49;00m[32mid[39;49;00m,[37m [39;49;00m[32mmethod[39;49;00m,[37m [39;49;00m[32mname[39;49;00m,[37m [39;49;00m[32mtype_[39;49;00m,[37m [39;49;00m[32mvalue[39;49;00m)[37m[39;49;00m
    37	[34mclass[39;49;00m[37m [39;49;00m[36mHasAcidState[39;49;00m[37m [39;49;00mm[37m [39;49;00mst[37m [39;49;00m[34mwhere[39;49;00m[37m[39;49;00m
    38	[37m   [39;49;00mgetAcidState[37m [39;49;00m[35m::[39;49;00m[37m [39;49;00mm[37m [39;49;00m([36mAcidState[39;49;00m[37m [39;49;00mst)[37m[39;49;00m
    39	[32mquery[39;49;00m[37m [39;49;00m[35m::[39;49;00m[37m [39;49;00mforall[37m [39;49;00mevent[37m [39;49;00mm.[37m [39;49;00m
    40	[37m         [39;49;00m([37m [39;49;00m[36mFunctor[39;49;00m[37m [39;49;00mm[37m[39;49;00m
    41	[37m         [39;49;00m,[37m [39;49;00m[36mMonadIO[39;49;00m[37m [39;49;00mm[37m[39;49;00m
    42	[37m         [39;49;00m,[37m [39;49;00m[36mQueryEvent[39;49;00m[37m [39;49;00mevent[37m[39;49;00m
    43	[37m         [39;49;00m,[37m [39;49;00m[36mHasAcidState[39;49;00m[37m [39;49;00mm[37m [39;49;00m([36mEventState[39;49;00m[37m [39;49;00mevent)[37m[39;49;00m
    44	[37m         [39;49;00m)[37m [39;49;00m[35m=>[39;49;00m[37m [39;49;00m
    45	[37m         [39;49;00mevent[37m[39;49;00m
    46	[37m      [39;49;00m[35m->[39;49;00m[37m [39;49;00mm[37m [39;49;00m([36mEventResult[39;49;00m[37m [39;49;00mevent)[37m[39;49;00m
    47	[32mquery[39;49;00m[37m [39;49;00mevent[37m [39;49;00m[35m=[39;49;00m[37m[39;49;00m
    48	[37m    [39;49;00m[34mdo[39;49;00m[37m [39;49;00mas[37m [39;49;00m[35m<-[39;49;00m[37m [39;49;00mgetAcidState[37m[39;49;00m
    49	[37m       [39;49;00mquery'[37m [39;49;00m(as[37m [39;49;00m[35m::[39;49;00m[37m [39;49;00m[36mAcidState[39;49;00m[37m [39;49;00m([36mEventState[39;49;00m[37m [39;49;00mevent))[37m [39;49;00mevent[37m[39;49;00m
    50	[32mupdate[39;49;00m[37m [39;49;00m[35m::[39;49;00m[37m [39;49;00mforall[37m [39;49;00mevent[37m [39;49;00mm.[37m [39;49;00m
    51	[37m          [39;49;00m([37m [39;49;00m[36mFunctor[39;49;00m[37m [39;49;00mm[37m[39;49;00m
    52	[37m          [39;49;00m,[37m [39;49;00m[36mMonadIO[39;49;00m[37m [39;49;00mm[37m[39;49;00m
    53	[37m          [39;49;00m,[37m [39;49;00m[36mUpdateEvent[39;49;00m[37m [39;49;00mevent[37m[39;49;00m
    54	[37m          [39;49;00m,[37m [39;49;00m[36mHasAcidState[39;49;00m[37m [39;49;00mm[37m [39;49;00m([36mEventState[39;49;00m[37m [39;49;00mevent)[37m[39;49;00m
    55	[37m          [39;49;00m)[37m [39;49;00m[35m=>[39;49;00m[37m [39;49;00m
    56	[37m          [39;49;00mevent[37m [39;49;00m
    57	[37m       [39;49;00m[35m->[39;49;00m[37m [39;49;00mm[37m [39;49;00m([36mEventResult[39;49;00m[37m [39;49;00mevent)[37m[39;49;00m
    58	[32mupdate[39;49;00m[37m [39;49;00mevent[37m [39;49;00m[35m=[39;49;00m[37m[39;49;00m
    59	[37m    [39;49;00m[34mdo[39;49;00m[37m [39;49;00mas[37m [39;49;00m[35m<-[39;49;00m[37m [39;49;00mgetAcidState[37m[39;49;00m
    60	[37m       [39;49;00mupdate'[37m [39;49;00m(as[37m [39;49;00m[35m::[39;49;00m[37m [39;49;00m[36mAcidState[39;49;00m[37m [39;49;00m([36mEventState[39;49;00m[37m [39;49;00mevent))[37m [39;49;00mevent[37m[39;49;00m
    61	[37m-- | bracket the opening and close of the `AcidState` handle. [39;49;00m[37m[39;49;00m
    62	[37m[39;49;00m
    63	[37m-- automatically creates a checkpoint on close[39;49;00m[37m[39;49;00m
    64	[32mwithLocalState[39;49;00m[37m [39;49;00m[35m::[39;49;00m[37m [39;49;00m([36mMonadBaseControl[39;49;00m[37m [39;49;00m[36mIO[39;49;00m[37m [39;49;00mm,[37m [39;49;00m[36mMonadIO[39;49;00m[37m [39;49;00mm,[37m [39;49;00m[36mIsAcidic[39;49;00m[37m [39;49;00mst,[37m [39;49;00m[36mTypeable[39;49;00m[37m [39;49;00mst)[37m [39;49;00m[35m=>[39;49;00m[37m [39;49;00m
    65	[37m                  [39;49;00m[36mMaybe[39;49;00m[37m [39;49;00m[36mFilePath[39;49;00m[37m           [39;49;00m[37m-- ^ path to state directory[39;49;00m[37m[39;49;00m
    66	[37m                 [39;49;00m[35m->[39;49;00m[37m [39;49;00mst[37m                     [39;49;00m[37m-- ^ initial state value[39;49;00m[37m[39;49;00m
    67	[37m                 [39;49;00m[35m->[39;49;00m[37m [39;49;00m([36mAcidState[39;49;00m[37m [39;49;00mst[37m [39;49;00m[35m->[39;49;00m[37m [39;49;00mm[37m [39;49;00ma)[37m [39;49;00m[37m-- ^ function which uses the `AcidState` handle[39;49;00m[37m[39;49;00m
    68	[37m                 [39;49;00m[35m->[39;49;00m[37m [39;49;00mm[37m [39;49;00ma[37m[39;49;00m
    69	[32mwithLocalState[39;49;00m[37m [39;49;00mmPath[37m [39;49;00minitialState[37m [39;49;00m[35m=[39;49;00m[37m[39;49;00m
    70	[37m    [39;49;00mbracket[37m [39;49;00m(liftIO[37m [39;49;00m$[37m [39;49;00m(maybe[37m [39;49;00mopenLocalState[37m [39;49;00mopenLocalStateFrom[37m [39;49;00mmPath)[37m [39;49;00minitialState)[37m[39;49;00m
    71	[37m            [39;49;00m(liftIO[37m [39;49;00m.[37m [39;49;00mcreateCheckpointAndClose)[37m[39;49;00m
    72	[37m-- State that stores a hit count[39;49;00m[37m[39;49;00m
    73	[37m[39;49;00m
    74	[34mdata[39;49;00m[37m [39;49;00m[36mCountState[39;49;00m[37m [39;49;00m[35m=[39;49;00m[37m [39;49;00m[36mCountState[39;49;00m[37m [39;49;00m{[37m [39;49;00m_count[37m [39;49;00m[35m::[39;49;00m[37m [39;49;00m[36mInteger[39;49;00m[37m [39;49;00m}[37m[39;49;00m
    75	[37m                [39;49;00m[34mderiving[39;49;00m[37m [39;49;00m([36mEq[39;49;00m,[37m [39;49;00m[36mOrd[39;49;00m,[37m [39;49;00m[36mData[39;49;00m,[37m [39;49;00m[36mTypeable[39;49;00m,[37m [39;49;00m[36mShow[39;49;00m)[37m[39;49;00m
    76	[37m[39;49;00m
    77	$(deriveSafeCopy[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m'base[37m [39;49;00m[36m''CountState[39;49;00m)[37m[39;49;00m
    78	$(makeLens[37m [39;49;00m[36m''CountState[39;49;00m)[37m[39;49;00m
    79	[37m[39;49;00m
    80	[32minitialCountState[39;49;00m[37m [39;49;00m[35m::[39;49;00m[37m [39;49;00m[36mCountState[39;49;00m[37m[39;49;00m
    81	[32minitialCountState[39;49;00m[37m [39;49;00m[35m=[39;49;00m[37m [39;49;00m[36mCountState[39;49;00m[37m [39;49;00m{[37m [39;49;00m_count[37m [39;49;00m[35m=[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m}[37m[39;49;00m
    82	[37m[39;49;00m
    83	[32mincCount[39;49;00m[37m [39;49;00m[35m::[39;49;00m[37m [39;49;00m[36mUpdate[39;49;00m[37m [39;49;00m[36mCountState[39;49;00m[37m [39;49;00m[36mInteger[39;49;00m[37m[39;49;00m
    84	[32mincCount[39;49;00m[37m [39;49;00m[35m=[39;49;00m[37m [39;49;00mcount[37m [39;49;00m%=[37m [39;49;00msucc[37m[39;49;00m
    85	[37m[39;49;00m
    86	$(makeAcidic[37m [39;49;00m[36m''CountState[39;49;00m[37m [39;49;00m['incCount])[37m[39;49;00m
    87	[37m-- State that stores a greeting[39;49;00m[37m[39;49;00m
    88	[34mdata[39;49;00m[37m [39;49;00m[36mGreetingState[39;49;00m[37m [39;49;00m[35m=[39;49;00m[37m [39;49;00m[36mGreetingState[39;49;00m[37m [39;49;00m{[37m  [39;49;00m_greeting[37m [39;49;00m[35m::[39;49;00m[37m [39;49;00m[36mText[39;49;00m[37m [39;49;00m}[37m[39;49;00m
    89	[37m                [39;49;00m[34mderiving[39;49;00m[37m [39;49;00m([36mEq[39;49;00m,[37m [39;49;00m[36mOrd[39;49;00m,[37m [39;49;00m[36mData[39;49;00m,[37m [39;49;00m[36mTypeable[39;49;00m,[37m [39;49;00m[36mShow[39;49;00m)[37m[39;49;00m
    90	[37m[39;49;00m
    91	$(deriveSafeCopy[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m'base[37m [39;49;00m[36m''GreetingState[39;49;00m)[37m[39;49;00m
    92	$(makeLens[37m [39;49;00m[36m''GreetingState[39;49;00m)[37m[39;49;00m
    93	[37m[39;49;00m
    94	[32minitialGreetingState[39;49;00m[37m [39;49;00m[35m::[39;49;00m[37m [39;49;00m[36mGreetingState[39;49;00m[37m[39;49;00m
    95	[32minitialGreetingState[39;49;00m[37m [39;49;00m[35m=[39;49;00m[37m [39;49;00m[36mGreetingState[39;49;00m[37m [39;49;00m{[37m [39;49;00m_greeting[37m [39;49;00m[35m=[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mHello[39;49;00m[33m"[39;49;00m[37m [39;49;00m}[37m[39;49;00m
    96	[37m[39;49;00m
    97	[32mgetGreeting[39;49;00m[37m [39;49;00m[35m::[39;49;00m[37m [39;49;00m[36mQuery[39;49;00m[37m [39;49;00m[36mGreetingState[39;49;00m[37m [39;49;00m[36mText[39;49;00m[37m[39;49;00m
    98	[32mgetGreeting[39;49;00m[37m [39;49;00m[35m=[39;49;00m[37m [39;49;00m_greeting[37m [39;49;00m<$>[37m [39;49;00mask[37m[39;49;00m
    99	[37m[39;49;00m
   100	[32msetGreeting[39;49;00m[37m [39;49;00m[35m::[39;49;00m[37m [39;49;00m[36mText[39;49;00m[37m [39;49;00m[35m->[39;49;00m[37m [39;49;00m[36mUpdate[39;49;00m[37m [39;49;00m[36mGreetingState[39;49;00m[37m [39;49;00m[36mText[39;49;00m[37m[39;49;00m
   101	[32msetGreeting[39;49;00m[37m [39;49;00mtxt[37m [39;49;00m[35m=[39;49;00m[37m [39;49;00mgreeting[37m [39;49;00m!=[37m [39;49;00mtxt[37m[39;49;00m
   102	[37m[39;49;00m
   103	$(makeAcidic[37m [39;49;00m[36m''GreetingState[39;49;00m[37m [39;49;00m['getGreeting,[37m [39;49;00m'setGreeting])[37m[39;49;00m
   104	[34mdata[39;49;00m[37m [39;49;00m[36mAcid[39;49;00m[37m [39;49;00m[35m=[39;49;00m[37m [39;49;00m[36mAcid[39;49;00m[37m [39;49;00m{[37m [39;49;00macidCountState[37m    [39;49;00m[35m::[39;49;00m[37m [39;49;00m[36mAcidState[39;49;00m[37m [39;49;00m[36mCountState[39;49;00m[37m[39;49;00m
   105	[37m                 [39;49;00m,[37m [39;49;00macidGreetingState[37m [39;49;00m[35m::[39;49;00m[37m [39;49;00m[36mAcidState[39;49;00m[37m [39;49;00m[36mGreetingState[39;49;00m[37m[39;49;00m
   106	[37m                 [39;49;00m}[37m[39;49;00m
   107	[37m[39;49;00m
   108	[32mwithAcid[39;49;00m[37m [39;49;00m[35m::[39;49;00m[37m [39;49;00m[36mMaybe[39;49;00m[37m [39;49;00m[36mFilePath[39;49;00m[37m [39;49;00m[35m->[39;49;00m[37m [39;49;00m([36mAcid[39;49;00m[37m [39;49;00m[35m->[39;49;00m[37m [39;49;00m[36mIO[39;49;00m[37m [39;49;00ma)[37m [39;49;00m[35m->[39;49;00m[37m [39;49;00m[36mIO[39;49;00m[37m [39;49;00ma[37m[39;49;00m
   109	[32mwithAcid[39;49;00m[37m [39;49;00mmBasePath[37m [39;49;00maction[37m [39;49;00m[35m=[39;49;00m[37m[39;49;00m
   110	[37m    [39;49;00m[34mlet[39;49;00m[37m [39;49;00mbasePath[37m [39;49;00m[35m=[39;49;00m[37m [39;49;00mfromMaybe[37m [39;49;00m[33m"[39;49;00m[33m_state[39;49;00m[33m"[39;49;00m[37m [39;49;00mmBasePath[37m[39;49;00m
   111	[37m    [39;49;00m[34min[39;49;00m[37m [39;49;00mwithLocalState[37m [39;49;00m([36mJust[39;49;00m[37m [39;49;00m$[37m [39;49;00mbasePath[37m [39;49;00m</>[37m [39;49;00m[33m"[39;49;00m[33mcount[39;49;00m[33m"[39;49;00m)[37m    [39;49;00minitialCountState[37m    [39;49;00m$[37m [39;49;00m[32m\[39;49;00mc[37m [39;49;00m[35m->[39;49;00m[37m[39;49;00m
   112	[37m       [39;49;00mwithLocalState[37m [39;49;00m([36mJust[39;49;00m[37m [39;49;00m$[37m [39;49;00mbasePath[37m [39;49;00m</>[37m [39;49;00m[33m"[39;49;00m[33mgreeting[39;49;00m[33m"[39;49;00m)[37m [39;49;00minitialGreetingState[37m [39;49;00m$[37m [39;49;00m[32m\[39;49;00mg[37m [39;49;00m[35m->[39;49;00m[37m[39;49;00m
   113	[37m           [39;49;00maction[37m [39;49;00m([36mAcid[39;49;00m[37m [39;49;00mc[37m [39;49;00mg)[37m[39;49;00m
   114	[34mnewtype[39;49;00m[37m [39;49;00m[36mApp[39;49;00m[37m [39;49;00ma[37m [39;49;00m[35m=[39;49;00m[37m [39;49;00m[36mApp[39;49;00m[37m [39;49;00m{[37m [39;49;00munApp[37m [39;49;00m[35m::[39;49;00m[37m [39;49;00m[36mServerPartT[39;49;00m[37m [39;49;00m([36mReaderT[39;49;00m[37m [39;49;00m[36mAcid[39;49;00m[37m [39;49;00m[36mIO[39;49;00m)[37m [39;49;00ma[37m [39;49;00m}[37m[39;49;00m
   115	[37m    [39;49;00m[34mderiving[39;49;00m[37m [39;49;00m([37m [39;49;00m[36mFunctor[39;49;00m,[37m [39;49;00m[36mAlternative[39;49;00m,[37m [39;49;00m[36mApplicative[39;49;00m,[37m [39;49;00m[36mMonad[39;49;00m,[37m [39;49;00m[36mMonadPlus[39;49;00m,[37m [39;49;00m[36mMonadIO[39;49;00m[37m[39;49;00m
   116	[37m               [39;49;00m,[37m [39;49;00m[36mHasRqData[39;49;00m,[37m [39;49;00m[36mServerMonad[39;49;00m[37m [39;49;00m,[36mWebMonad[39;49;00m[37m [39;49;00m[36mResponse[39;49;00m,[37m [39;49;00m[36mFilterMonad[39;49;00m[37m [39;49;00m[36mResponse[39;49;00m[37m[39;49;00m
   117	[37m               [39;49;00m,[37m [39;49;00m[36mHappstack[39;49;00m,[37m [39;49;00m[36mMonadReader[39;49;00m[37m [39;49;00m[36mAcid[39;49;00m)[37m[39;49;00m
   118	[37m[39;49;00m
   119	[32mrunApp[39;49;00m[37m [39;49;00m[35m::[39;49;00m[37m [39;49;00m[36mAcid[39;49;00m[37m [39;49;00m[35m->[39;49;00m[37m [39;49;00m[36mApp[39;49;00m[37m [39;49;00ma[37m [39;49;00m[35m->[39;49;00m[37m [39;49;00m[36mServerPartT[39;49;00m[37m [39;49;00m[36mIO[39;49;00m[37m [39;49;00ma[37m[39;49;00m
   120	[32mrunApp[39;49;00m[37m [39;49;00macid[37m [39;49;00m([36mApp[39;49;00m[37m [39;49;00msp)[37m [39;49;00m[35m=[39;49;00m[37m [39;49;00mmapServerPartT[37m [39;49;00m(flip[37m [39;49;00mrunReaderT[37m [39;49;00macid)[37m [39;49;00msp[37m[39;49;00m
   121	[34minstance[39;49;00m[37m [39;49;00m[36mHasAcidState[39;49;00m[37m [39;49;00m[36mApp[39;49;00m[37m [39;49;00m[36mCountState[39;49;00m[37m [39;49;00m[34mwhere[39;49;00m[37m[39;49;00m
   122	[37m    [39;49;00mgetAcidState[37m [39;49;00m[35m=[39;49;00m[37m [39;49;00macidCountState[37m    [39;49;00m<$>[37m [39;49;00mask[37m [39;49;00m
   123	[37m[39;49;00m
   124	[34minstance[39;49;00m[37m [39;49;00m[36mHasAcidState[39;49;00m[37m [39;49;00m[36mApp[39;49;00m[37m [39;49;00m[36mGreetingState[39;49;00m[37m [39;49;00m[34mwhere[39;49;00m[37m[39;49;00m
   125	[37m    [39;49;00mgetAcidState[37m [39;49;00m[35m=[39;49;00m[37m [39;49;00macidGreetingState[37m [39;49;00m<$>[37m [39;49;00mask[37m[39;49;00m
   126	[32mpage[39;49;00m[37m [39;49;00m[35m::[39;49;00m[37m [39;49;00m[36mApp[39;49;00m[37m [39;49;00m[36mResponse[39;49;00m[37m[39;49;00m
   127	[32mpage[39;49;00m[37m [39;49;00m[35m=[39;49;00m[37m[39;49;00m
   128	[37m    [39;49;00m[34mdo[39;49;00m[37m [39;49;00mnullDir[37m[39;49;00m
   129	[37m       [39;49;00mg[37m [39;49;00m[35m<-[39;49;00m[37m [39;49;00mgreet[37m[39;49;00m
   130	[37m       [39;49;00mc[37m [39;49;00m[35m<-[39;49;00m[37m [39;49;00mupdate[37m [39;49;00m[36mIncCount[39;49;00m[37m [39;49;00m[37m-- ^ a CountState event[39;49;00m[37m[39;49;00m
   131	[37m       [39;49;00mok[37m [39;49;00m$[37m [39;49;00mtoResponse[37m [39;49;00m$[37m[39;49;00m
   132	[37m          [39;49;00mhtml[37m [39;49;00m$[37m [39;49;00m[34mdo[39;49;00m[37m[39;49;00m
   133	[37m            [39;49;00mhead[37m [39;49;00m$[37m [39;49;00m[34mdo[39;49;00m[37m[39;49;00m
   134	[37m              [39;49;00mtitle[37m [39;49;00m[33m"[39;49;00m[33macid-state demo[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   135	[37m            [39;49;00mbody[37m [39;49;00m$[37m [39;49;00m[34mdo[39;49;00m[37m[39;49;00m
   136	[37m              [39;49;00mform[37m [39;49;00m![37m [39;49;00maction[37m [39;49;00m[33m"[39;49;00m[33m/[39;49;00m[33m"[39;49;00m[37m [39;49;00m![37m [39;49;00mmethod[37m [39;49;00m[33m"[39;49;00m[33mPOST[39;49;00m[33m"[39;49;00m[37m [39;49;00m![37m [39;49;00menctype[37m [39;49;00m[33m"[39;49;00m[33mmultipart/form-data[39;49;00m[33m"[39;49;00m[37m [39;49;00m$[37m [39;49;00m[34mdo[39;49;00m[37m[39;49;00m
   137	[37m                [39;49;00mlabel[37m [39;49;00m[33m"[39;49;00m[33mnew message: [39;49;00m[33m"[39;49;00m[37m [39;49;00m![37m [39;49;00mfor[37m [39;49;00m[33m"[39;49;00m[33mmsg[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   138	[37m                [39;49;00minput[37m [39;49;00m![37m [39;49;00mtype_[37m [39;49;00m[33m"[39;49;00m[33mtext[39;49;00m[33m"[39;49;00m[37m [39;49;00m![37m [39;49;00mid[37m [39;49;00m[33m"[39;49;00m[33mmsg[39;49;00m[33m"[39;49;00m[37m [39;49;00m![37m [39;49;00mname[37m [39;49;00m[33m"[39;49;00m[33mgreeting[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   139	[37m                [39;49;00minput[37m [39;49;00m![37m [39;49;00mtype_[37m [39;49;00m[33m"[39;49;00m[33msubmit[39;49;00m[33m"[39;49;00m[37m [39;49;00m![37m [39;49;00mvalue[37m [39;49;00m[33m"[39;49;00m[33mupdate message[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   140	[37m              [39;49;00mp[37m [39;49;00m$[37m [39;49;00mtoHtml[37m [39;49;00mg[37m[39;49;00m
   141	[37m              [39;49;00mp[37m [39;49;00m$[37m [39;49;00m[34mdo[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mThis page has been loaded [39;49;00m[33m"[39;49;00m[37m [39;49;00m
   142	[37m                     [39;49;00mtoHtml[37m [39;49;00mc[37m[39;49;00m
   143	[37m                     [39;49;00m[33m"[39;49;00m[33m time(s).[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   144	[37m    [39;49;00m[34mwhere[39;49;00m[37m[39;49;00m
   145	[37m    [39;49;00mgreet[37m [39;49;00m[35m=[39;49;00m[37m[39;49;00m
   146	[37m        [39;49;00m[34mdo[39;49;00m[37m [39;49;00mm[37m [39;49;00m[35m<-[39;49;00m[37m [39;49;00mrqMethod[37m [39;49;00m<$>[37m [39;49;00maskRq[37m[39;49;00m
   147	[37m           [39;49;00m[34mcase[39;49;00m[37m [39;49;00mm[37m [39;49;00m[34mof[39;49;00m[37m[39;49;00m
   148	[37m             [39;49;00m[36mPOST[39;49;00m[37m [39;49;00m[35m->[39;49;00m[37m [39;49;00m
   149	[37m                 [39;49;00m[34mdo[39;49;00m[37m [39;49;00mdecodeBody[37m [39;49;00m(defaultBodyPolicy[37m [39;49;00m[33m"[39;49;00m[33m/tmp/[39;49;00m[33m"[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[34m1000[39;49;00m[37m [39;49;00m[34m1000[39;49;00m)[37m[39;49;00m
   150	[37m                    [39;49;00mnewGreeting[37m [39;49;00m[35m<-[39;49;00m[37m [39;49;00mlookText[37m [39;49;00m[33m"[39;49;00m[33mgreeting[39;49;00m[33m"[39;49;00m[37m[39;49;00m
   151	[37m                    [39;49;00mupdate[37m [39;49;00m([36mSetGreeting[39;49;00m[37m [39;49;00mnewGreeting)[37m   [39;49;00m[37m-- ^ a GreetingState event[39;49;00m[37m[39;49;00m
   152	[37m                    [39;49;00mreturn[37m [39;49;00mnewGreeting[37m[39;49;00m
   153	[37m             [39;49;00m[36mGET[39;49;00m[37m  [39;49;00m[35m->[39;49;00m[37m [39;49;00m
   154	[37m                 [39;49;00m[34mdo[39;49;00m[37m [39;49;00mquery[37m [39;49;00m[36mGetGreeting[39;49;00m[37m                  [39;49;00m[37m-- ^ a GreetingState event[39;49;00m[37m[39;49;00m
   155	[32mmain[39;49;00m[37m [39;49;00m[35m::[39;49;00m[37m [39;49;00m[36mIO[39;49;00m[37m [39;49;00m[36m()[39;49;00m[37m[39;49;00m
   156	[32mmain[39;49;00m[37m [39;49;00m[35m=[39;49;00m[37m[39;49;00m
   157	[37m    [39;49;00mwithAcid[37m [39;49;00m[36mNothing[39;49;00m[37m [39;49;00m$[37m [39;49;00m[32m\[39;49;00macid[37m [39;49;00m[35m->[39;49;00m[37m[39;49;00m
   158	[37m        [39;49;00msimpleHTTP[37m [39;49;00mnullConf[37m [39;49;00m$[37m [39;49;00mrunApp[37m [39;49;00macid[37m [39;49;00mpage[37m[39;49;00m
   159	[34mnewtype[39;49;00m[37m [39;49;00m[36mFooState[39;49;00m[37m [39;49;00m[35m=[39;49;00m[37m [39;49;00m[36mFooState[39;49;00m[37m [39;49;00m{[37m [39;49;00mfoo[37m [39;49;00m[35m::[39;49;00m[37m [39;49;00m[36mText[39;49;00m[37m [39;49;00m}[37m[39;49;00m
   160	[37m    [39;49;00m[34mderiving[39;49;00m[37m [39;49;00m([36mEq[39;49;00m,[37m [39;49;00m[36mOrd[39;49;00m,[37m [39;49;00m[36mData[39;49;00m,[37m [39;49;00m[36mTypeable[39;49;00m,[37m [39;49;00m[36mSafeCopy[39;49;00m)[37m[39;49;00m
   161	[37m[39;49;00m
   162	[32minitialFooState[39;49;00m[37m [39;49;00m[35m::[39;49;00m[37m [39;49;00m[36mFooState[39;49;00m[37m[39;49;00m
   163	[32minitialFooState[39;49;00m[37m [39;49;00m[35m=[39;49;00m[37m [39;49;00m[36mFooState[39;49;00m[37m [39;49;00m{[37m [39;49;00mfoo[37m [39;49;00m[35m=[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mfoo[39;49;00m[33m"[39;49;00m[37m [39;49;00m}[37m[39;49;00m
   164	[37m[39;49;00m
   165	[32maskFoo[39;49;00m[37m [39;49;00m[35m::[39;49;00m[37m [39;49;00m[36mQuery[39;49;00m[37m [39;49;00m[36mFooState[39;49;00m[37m [39;49;00m[36mText[39;49;00m[37m[39;49;00m
   166	[32maskFoo[39;49;00m[37m [39;49;00m[35m=[39;49;00m[37m [39;49;00mfoo[37m [39;49;00m<$>[37m [39;49;00mask[37m[39;49;00m
   167	[37m[39;49;00m
   168	$(makeAcidic[37m [39;49;00m[36m''FooState[39;49;00m[37m [39;49;00m['askFoo])[37m[39;49;00m
   169	[32mfooPlugin[39;49;00m[37m [39;49;00m[35m::[39;49;00m[37m [39;49;00m([36mHappstack[39;49;00m[37m [39;49;00mm,[37m [39;49;00m[36mHasAcidState[39;49;00m[37m [39;49;00mm[37m [39;49;00m[36mFooState[39;49;00m)[37m [39;49;00m[35m=>[39;49;00m[37m [39;49;00mm[37m [39;49;00m[36mResponse[39;49;00m[37m[39;49;00m
   170	[32mfooPlugin[39;49;00m[37m [39;49;00m[35m=[39;49;00m[37m[39;49;00m
   171	[37m    [39;49;00mdir[37m [39;49;00m[33m"[39;49;00m[33mfoo[39;49;00m[33m"[39;49;00m[37m [39;49;00m$[37m [39;49;00m[34mdo[39;49;00m[37m[39;49;00m
   172	[37m       [39;49;00mtxt[37m [39;49;00m[35m<-[39;49;00m[37m [39;49;00mquery[37m [39;49;00m[36mAskFoo[39;49;00m[37m[39;49;00m
   173	[37m       [39;49;00mok[37m [39;49;00m$[37m [39;49;00mtoResponse[37m [39;49;00mtxt[37m[39;49;00m
   174	[34mdata[39;49;00m[37m [39;49;00m[36mAcid'[39;49;00m[37m [39;49;00m[35m=[39;49;00m[37m [39;49;00m[36mAcid'[39;49;00m[37m [39;49;00m{[37m [39;49;00macidCountState'[37m    [39;49;00m[35m::[39;49;00m[37m [39;49;00m[36mAcidState[39;49;00m[37m [39;49;00m[36mCountState[39;49;00m[37m[39;49;00m
   175	[37m                   [39;49;00m,[37m [39;49;00macidGreetingState'[37m [39;49;00m[35m::[39;49;00m[37m [39;49;00m[36mAcidState[39;49;00m[37m [39;49;00m[36mGreetingState[39;49;00m[37m[39;49;00m
   176	[37m                   [39;49;00m,[37m [39;49;00macidFooState'[37m      [39;49;00m[35m::[39;49;00m[37m [39;49;00m[36mAcidState[39;49;00m[37m [39;49;00m[36mFooState[39;49;00m[37m[39;49;00m
   177	[37m                   [39;49;00m}[37m[39;49;00m
   178	[32mwithAcid'[39;49;00m[37m [39;49;00m[35m::[39;49;00m[37m [39;49;00m[36mMaybe[39;49;00m[37m [39;49;00m[36mFilePath[39;49;00m[37m [39;49;00m[35m->[39;49;00m[37m [39;49;00m([36mAcid'[39;49;00m[37m [39;49;00m[35m->[39;49;00m[37m [39;49;00m[36mIO[39;49;00m[37m [39;49;00ma)[37m [39;49;00m[35m->[39;49;00m[37m [39;49;00m[36mIO[39;49;00m[37m [39;49;00ma[37m[39;49;00m
   179	[32mwithAcid'[39;49;00m[37m [39;49;00mmBasePath[37m [39;49;00maction[37m [39;49;00m[35m=[39;49;00m[37m[39;49;00m
   180	[37m    [39;49;00m[34mlet[39;49;00m[37m [39;49;00mbasePath[37m [39;49;00m[35m=[39;49;00m[37m [39;49;00mfromMaybe[37m [39;49;00m[33m"[39;49;00m[33m_state[39;49;00m[33m"[39;49;00m[37m [39;49;00mmBasePath[37m[39;49;00m
   181	[37m    [39;49;00m[34min[39;49;00m[37m [39;49;00mwithLocalState[37m [39;49;00m([36mJust[39;49;00m[37m [39;49;00m$[37m [39;49;00mbasePath[37m [39;49;00m</>[37m [39;49;00m[33m"[39;49;00m[33mcount[39;49;00m[33m"[39;49;00m)[37m    [39;49;00minitialCountState[37m    [39;49;00m$[37m [39;49;00m[32m\[39;49;00mc[37m [39;49;00m[35m->[39;49;00m[37m[39;49;00m
   182	[37m       [39;49;00mwithLocalState[37m [39;49;00m([36mJust[39;49;00m[37m [39;49;00m$[37m [39;49;00mbasePath[37m [39;49;00m</>[37m [39;49;00m[33m"[39;49;00m[33mgreeting[39;49;00m[33m"[39;49;00m)[37m [39;49;00minitialGreetingState[37m [39;49;00m$[37m [39;49;00m[32m\[39;49;00mg[37m [39;49;00m[35m->[39;49;00m[37m[39;49;00m
   183	[37m       [39;49;00mwithLocalState[37m [39;49;00m([36mJust[39;49;00m[37m [39;49;00m$[37m [39;49;00mbasePath[37m [39;49;00m</>[37m [39;49;00m[33m"[39;49;00m[33mfoo[39;49;00m[33m"[39;49;00m)[37m      [39;49;00minitialFooState[37m      [39;49;00m$[37m [39;49;00m[32m\[39;49;00mf[37m [39;49;00m[35m->[39;49;00m[37m[39;49;00m
   184	[37m           [39;49;00maction[37m [39;49;00m([36mAcid'[39;49;00m[37m [39;49;00mc[37m [39;49;00mg[37m [39;49;00mf)[37m[39;49;00m
   185	[34mnewtype[39;49;00m[37m [39;49;00m[36mApp'[39;49;00m[37m [39;49;00ma[37m [39;49;00m[35m=[39;49;00m[37m [39;49;00m[36mApp'[39;49;00m[37m [39;49;00m{[37m [39;49;00munApp'[37m [39;49;00m[35m::[39;49;00m[37m [39;49;00m[36mServerPartT[39;49;00m[37m [39;49;00m([36mReaderT[39;49;00m[37m [39;49;00m[36mAcid'[39;49;00m[37m [39;49;00m[36mIO[39;49;00m)[37m [39;49;00ma[37m [39;49;00m}[37m[39;49;00m
   186	[37m    [39;49;00m[34mderiving[39;49;00m[37m [39;49;00m([37m [39;49;00m[36mFunctor[39;49;00m,[37m [39;49;00m[36mAlternative[39;49;00m,[37m [39;49;00m[36mApplicative[39;49;00m,[37m [39;49;00m[36mMonad[39;49;00m,[37m [39;49;00m[36mMonadPlus[39;49;00m,[37m [39;49;00m[36mMonadIO[39;49;00m[37m[39;49;00m
   187	[37m               [39;49;00m,[37m [39;49;00m[36mHasRqData[39;49;00m,[37m [39;49;00m[36mServerMonad[39;49;00m[37m [39;49;00m,[36mWebMonad[39;49;00m[37m [39;49;00m[36mResponse[39;49;00m,[37m [39;49;00m[36mFilterMonad[39;49;00m[37m [39;49;00m[36mResponse[39;49;00m[37m[39;49;00m
   188	[37m               [39;49;00m,[37m [39;49;00m[36mHappstack[39;49;00m,[37m [39;49;00m[36mMonadReader[39;49;00m[37m [39;49;00m[36mAcid'[39;49;00m)[37m[39;49;00m
   189	[37m[39;49;00m
   190	[34minstance[39;49;00m[37m [39;49;00m[36mHasAcidState[39;49;00m[37m [39;49;00m[36mApp'[39;49;00m[37m [39;49;00m[36mFooState[39;49;00m[37m [39;49;00m[34mwhere[39;49;00m[37m[39;49;00m
   191	[37m    [39;49;00mgetAcidState[37m [39;49;00m[35m=[39;49;00m[37m [39;49;00macidFooState'[37m [39;49;00m<$>[37m [39;49;00mask[37m[39;49;00m
   192	[32mfooAppPlugin[39;49;00m[37m [39;49;00m[35m::[39;49;00m[37m [39;49;00m[36mApp'[39;49;00m[37m [39;49;00m[36mResponse[39;49;00m[37m[39;49;00m
   193	[32mfooAppPlugin[39;49;00m[37m [39;49;00m[35m=[39;49;00m[37m [39;49;00mfooPlugin[37m[39;49;00m
   194	[32mfooReaderPlugin[39;49;00m[37m [39;49;00m[35m::[39;49;00m[37m [39;49;00m[36mReaderT[39;49;00m[37m [39;49;00m([36mAcidState[39;49;00m[37m [39;49;00m[36mFooState[39;49;00m)[37m [39;49;00m([36mServerPartT[39;49;00m[37m [39;49;00m[36mIO[39;49;00m)[37m [39;49;00m[36mResponse[39;49;00m[37m[39;49;00m
   195	[32mfooReaderPlugin[39;49;00m[37m [39;49;00m[35m=[39;49;00m[37m [39;49;00mfooPlugin[37m[39;49;00m
   196	[34minstance[39;49;00m[37m [39;49;00m[36mHasAcidState[39;49;00m[37m [39;49;00m([36mReaderT[39;49;00m[37m [39;49;00m([36mAcidState[39;49;00m[37m [39;49;00m[36mFooState[39;49;00m)[37m [39;49;00m([36mServerPartT[39;49;00m[37m [39;49;00m[36mIO[39;49;00m))[37m [39;49;00m[36mFooState[39;49;00m[37m [39;49;00m[34mwhere[39;49;00m[37m[39;49;00m
   197	[37m    [39;49;00mgetAcidState[37m [39;49;00m[35m=[39;49;00m[37m [39;49;00mask[37m[39;49;00m
   198	[32mwithFooPlugin[39;49;00m[37m [39;49;00m[35m::[39;49;00m[37m [39;49;00m([36mMonadIO[39;49;00m[37m [39;49;00mm,[37m [39;49;00m[36mMonadBaseControl[39;49;00m[37m [39;49;00m[36mIO[39;49;00m[37m [39;49;00mm)[37m [39;49;00m[35m=>[39;49;00m[37m [39;49;00m
   199	[37m                 [39;49;00m[36mFilePath[39;49;00m[37m                          [39;49;00m[37m-- ^ path to state directory[39;49;00m[37m[39;49;00m
   200	[37m              [39;49;00m[35m->[39;49;00m[37m [39;49;00m([36mServerPartT[39;49;00m[37m [39;49;00m[36mIO[39;49;00m[37m [39;49;00m[36mResponse[39;49;00m[37m [39;49;00m[35m->[39;49;00m[37m [39;49;00mm[37m [39;49;00ma)[37m  [39;49;00m[37m-- ^ function that uses fooPlugin[39;49;00m[37m[39;49;00m
   201	[37m              [39;49;00m[35m->[39;49;00m[37m [39;49;00mm[37m [39;49;00ma[37m[39;49;00m
   202	[32mwithFooPlugin[39;49;00m[37m [39;49;00mbasePath[37m [39;49;00mf[37m [39;49;00m[35m=[39;49;00m[37m[39;49;00m
   203	[37m       [39;49;00m[34mdo[39;49;00m[37m [39;49;00mwithLocalState[37m [39;49;00m([36mJust[39;49;00m[37m [39;49;00m$[37m [39;49;00mbasePath[37m [39;49;00m</>[37m [39;49;00m[33m"[39;49;00m[33mfoo[39;49;00m[33m"[39;49;00m)[37m [39;49;00minitialFooState[37m [39;49;00m$[37m [39;49;00m[32m\[39;49;00mfooState[37m [39;49;00m[35m->[39;49;00m[37m [39;49;00m
   204	[37m              [39;49;00mf[37m [39;49;00m$[37m [39;49;00mrunReaderT[37m [39;49;00mfooReaderPlugin[37m [39;49;00mfooState[37m[39;49;00m
   205	[32mmain'[39;49;00m[37m [39;49;00m[35m::[39;49;00m[37m [39;49;00m[36mIO[39;49;00m[37m [39;49;00m[36m()[39;49;00m[37m[39;49;00m
   206	[32mmain'[39;49;00m[37m [39;49;00m[35m=[39;49;00m[37m [39;49;00m
   207	[37m    [39;49;00mwithFooPlugin[37m [39;49;00m[33m"[39;49;00m[33m_state[39;49;00m[33m"[39;49;00m[37m [39;49;00m$[37m [39;49;00m[32m\[39;49;00mfooPlugin'[37m [39;49;00m[35m->[39;49;00m[37m[39;49;00m
   208	[37m        [39;49;00mwithAcid[37m [39;49;00m[36mNothing[39;49;00m[37m [39;49;00m$[37m [39;49;00m[32m\[39;49;00macid[37m [39;49;00m[35m->[39;49;00m[37m[39;49;00m
   209	[37m            [39;49;00msimpleHTTP[37m [39;49;00mnullConf[37m [39;49;00m$[37m [39;49;00mfooPlugin'[37m [39;49;00m`mplus`[37m [39;49;00mrunApp[37m [39;49;00macid[37m [39;49;00mpage

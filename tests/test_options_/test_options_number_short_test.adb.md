     1	[37m--  Model IED Simulator[39;49;00m
     2	[37m--  COL Gene Ressler, 1 December 2007[39;49;00m
     3	[34mwith[39;49;00m [04m[36mAda.Text_IO[39;49;00m;
     4
     5	[34mwith[39;49;00m [04m[36mAda.Characters.Latin_1[39;49;00m;
     6	[34muse[39;49;00m  [04m[36mAda.Characters.Latin_1[39;49;00m;
     7
     8	[34mwith[39;49;00m [04m[36mAda.Strings.Fixed[39;49;00m;
     9	[34muse[39;49;00m  [04m[36mAda.Strings.Fixed[39;49;00m;
    10
    11	[34mwith[39;49;00m [04m[36mAda.Strings[39;49;00m;
    12	[34mwith[39;49;00m [04m[36mAda.Strings.Bounded[39;49;00m;
    13
    14	[34mwith[39;49;00m [04m[36mBinary_Search[39;49;00m;
    15
    16	[34mwith[39;49;00m [04m[36mAda.Containers.Generic_Array_Sort[39;49;00m;
    17
    18	[34mpackage[39;49;00m [34mbody[39;49;00m [04m[32mScanner[39;49;00m [34mis[39;49;00m
    19
    20	   [31mConstant_123[39;49;00m   : [34mconstant[39;49;00m [36mCharacter[39;49;00m := [36mCharacter[39;49;00m'[36mVal[39;49;00m ([34m16#00#[39;49;00m);
    21	   [31mMAX_KEYWORD_LENGTH_C[39;49;00m : [34mconstant[39;49;00m [36mNatural[39;49;00m := [34m24[39;49;00m;
    22
    23	   [31mNew_Constant[39;49;00m : [34mconstant[39;49;00m New_Type
    24	     := [34m2[39;49;00m;
    25
    26	   [31mKEYWORDS_C[39;49;00m : [34mconstant[39;49;00m Keyword_Array_T :=
    27	     (To_BS([33m"description"[39;49;00m),
    28	      To_BS([33m"with"[39;49;00m));
    29
    30	   [34mprocedure[39;49;00m [32mBlah[39;49;00m;
    31
    32	   [34mprocedure[39;49;00m [32mblah[39;49;00m [34mis[39;49;00m
    33	   [34mbegin[39;49;00m
    34
    35	      Declaration:
    36	      [34mdeclare[39;49;00m
    37	         Joe : Type_Type := Random;
    38	      [34mbegin[39;49;00m
    39	         Do_Something;
    40	      [34mend[39;49;00m [32mDeclaration[39;49;00m;
    41	      Loop_ID:
    42	         [34mloop[39;49;00m
    43	            Loop_Do;
    44	            [34mexit[39;49;00m [34mwhen[39;49;00m [34m1[39;49;00m=[34m2[39;49;00m;
    45	         [34mend[39;49;00m [34mloop[39;49;00m [34mLoop[39;49;00m[32m_ID[39;49;00m;
    46	      [34mif[39;49;00m [34mTrue[39;49;00m [35mor else[39;49;00m [34mFalse[39;49;00m [34mthen[39;49;00m
    47	         Do_This();
    48	      [34melsif[39;49;00m [35mnot[39;49;00m [34mFalse[39;49;00m [35mand then[39;49;00m [34mTrue[39;49;00m [34mthen[39;49;00m
    49	         Do_That;
    50	      [34melse[39;49;00m
    51	         Panic;
    52	      [34mend[39;49;00m [34mif[39;49;00m;
    53	   [34mend[39;49;00m [32mblah[39;49;00m;
    54
    55	   [34mfunction[39;49;00m [32m"*"[39;49;00m ([31mLeft[39;49;00m, [31mRight[39;49;00m : [31min[39;49;00m [31mInteger[39;49;00m) [34mreturn[39;49;00m [36mInteger[39;49;00m [34mis[39;49;00m
    56	   [34mbegin[39;49;00m
    57	      <<Goto_Label>>
    58	      [34mgoto[39;49;00m Goto_Label;
    59	      [34mreturn[39;49;00m Left + Right;
    60	   [34mend[39;49;00m [32m"*"[39;49;00m;
    61
    62	   [34mfunction[39;49;00m [32mFunction_Specification[39;49;00m
    63	     ([31mParam_1[39;49;00m        : [31min[39;49;00m [31mBlah[39;49;00m;
    64	      [31mParam2[39;49;00m, [31mparam3[39;49;00m : [31min[39;49;00m [31maccess[39;49;00m [31mBlah_Type[39;49;00m := [31m0[39;49;00m)
    65	     [34mreturn[39;49;00m It_Type;
    66
    67	   [34mpackage[39;49;00m [04m[32mRename_Check[39;49;00m [34mrenames[39;49;00m [04m[32mAda.Text_IO[39;49;00m;
    68
    69	   [34mtype[39;49;00m [36mNew_Float[39;49;00m [34mis[39;49;00m [34mdelta[39;49;00m [34m0.001[39;49;00m [34mdigits[39;49;00m [34m12[39;49;00m;
    70
    71	   [34mpackage[39;49;00m [04m[32mPackage_Inst[39;49;00m [34mis new[39;49;00m [04m[32mAda.Strings.Bounded.Generic_Bounded_Length[39;49;00m
    72	     ([31mMax[39;49;00m => MAX_KEYWORD_LENGTH_C);
    73
    74	   [34mtype[39;49;00m [36mArray_Decl12[39;49;00m [34mis[39;49;00m [34marray[39;49;00m ([36mPositive[39;49;00m [34mrange[39;49;00m <>) [34mof[39;49;00m SB.Bounded_String;
    75	   [34mtype[39;49;00m [36mArray_Decl3[39;49;00m [34mis[39;49;00m [34marray[39;49;00m ([36mNew_Type[39;49;00m [34mrange[39;49;00m Thing_1 .. Thing_2) [34mof[39;49;00m SB.Bounded_String;
    76
    77	   [34mtype[39;49;00m [36mBoring_Type[39;49;00m [34mis[39;49;00m
    78	     ([31mStart[39;49;00m,
    79	      [31mEnd_Error[39;49;00m);
    80
    81	   [34msubtype[39;49;00m [36mSub_Type_check[39;49;00m [34mis[39;49;00m [36mCharacter[39;49;00m [34mrange[39;49;00m '[36m0[39;49;00m' .. '[36m9[39;49;00m';
    82
    83	   [31mInitialized_Array[39;49;00m : [34mconstant[39;49;00m Transistion_Array_T :=
    84	     (Start =>
    85	        (Letter_Lower | Letter_Upper => Saw_Alpha,
    86	         [33m' '[39;49;00m | HT | CR | LF          => Start,
    87	         [34mothers[39;49;00m => Begin_Error),
    88
    89	      End_Error => ([34mothers[39;49;00m => Start)
    90
    91	     );
    92
    93	   [34mtype[39;49;00m [36mRecorder[39;49;00m [34mis[39;49;00m [34mrecord[39;49;00m
    94	      Advance      : [36mBoolean[39;49;00m;
    95	      Return_Token : Token_T;
    96	   [34mend record[39;49;00m;
    97
    98	   [34mfor[39;49;00m Recorder [34muse[39;49;00m [04m[36m8[39;49;00m;
    99
   100	   [34mtype[39;49;00m [36mNull_Record[39;49;00m [34mis[39;49;00m [34mnull record[39;49;00m;
   101
   102	   [34mtype[39;49;00m [36mDiscriminated_Record[39;49;00m ([31mSize[39;49;00m : [31mNatural[39;49;00m) [34mis[39;49;00m
   103	      [34mrecord[39;49;00m
   104	         A : [36mString[39;49;00m ([34m1[39;49;00m .. Size);
   105	      [34mend record[39;49;00m;
   106
   107	   [34mpragma[39;49;00m [36mUnchecked_Union[39;49;00m (Union);
   108	   [34mpragma[39;49;00m [36mConvention[39;49;00m (C, Union);
   109
   110	   [34mtype[39;49;00m [36mPerson[39;49;00m [34mis[39;49;00m [34mtagged[39;49;00m
   111	      [34mrecord[39;49;00m
   112	         Name   : [36mString[39;49;00m ([34m1[39;49;00m .. [34m10[39;49;00m);
   113	         Gender : Gender_Type;
   114	      [34mend record[39;49;00m;
   115
   116	   [34mtype[39;49;00m [36mProgrammer[39;49;00m [34mis[39;49;00m [34mnew[39;49;00m Person [34mwith[39;49;00m
   117	      [34mrecord[39;49;00m
   118	         Skilled_In : Language_List;
   119	         Favorite_Langauge : Python_Type;
   120	      [34mend record[39;49;00m;
   121
   122	   [34mtype[39;49;00m [36mProgrammer[39;49;00m [34mis[39;49;00m [34mnew[39;49;00m Person
   123	     [34mand[39;49;00m Printable
   124	     [34mwith[39;49;00m
   125	      [34mrecord[39;49;00m
   126	         Skilled_In : Language_List;
   127	         Blah : [34maliased[39;49;00m [36mInteger[39;49;00m;
   128	      [34mend record[39;49;00m;
   129
   130	   [37m---------------------[39;49;00m
   131	   [37m-- Scan_Next_Token --[39;49;00m
   132	   [37m---------------------[39;49;00m
   133
   134	   [34mtask[39;49;00m Cyclic_Buffer_Task_Type [34mis[39;49;00m
   135	      [34mentry[39;49;00m [32mInsert[39;49;00m ([31mAn_Item[39;49;00m : [31min[39;49;00m  [31mItem[39;49;00m);
   136	      [34mentry[39;49;00m [32mRemove[39;49;00m ([31mAn_Item[39;49;00m : [31mout[39;49;00m [31mItem[39;49;00m);
   137	   [34mend[39;49;00m [32mCyclic_Buffer_Task_Type[39;49;00m;
   138
   139	   [34mtask[39;49;00m [34mbody[39;49;00m Cyclic_Buffer_Task_Type [34mis[39;49;00m
   140	      [31mQ_Size[39;49;00m : [34mconstant[39;49;00m := [34m100[39;49;00m;
   141	      [34msubtype[39;49;00m [36mQ_Range[39;49;00m [34mis[39;49;00m [36mPositive[39;49;00m [34mrange[39;49;00m [34m1[39;49;00m .. Q_Size;
   142	      Length : [36mNatural[39;49;00m [34mrange[39;49;00m [34m0[39;49;00m .. Q_Size := [34m0[39;49;00m;
   143	      Head, Tail : Q_Range := [34m1[39;49;00m;
   144	      Data : [34marray[39;49;00m (Q_Range) [34mof[39;49;00m Item;
   145	   [34mbegin[39;49;00m
   146	      [34mloop[39;49;00m
   147	         [34mselect[39;49;00m
   148	            [34mwhen[39;49;00m Length < Q_Size =>
   149	               [34maccept[39;49;00m Insert (An_Item : [35min[39;49;00m  Item) [34mdo[39;49;00m
   150	                  Data(Tail) := An_Item;
   151	               [34mend[39;49;00m [32mInsert[39;49;00m;
   152	               Tail := Tail [35mmod[39;49;00m Q_Size + [34m1[39;49;00m;
   153	               Length := Length + [34m1[39;49;00m;
   154	         [34mor[39;49;00m
   155	            [34mwhen[39;49;00m Length > [34m0[39;49;00m =>
   156	               [34maccept[39;49;00m Remove (An_Item : [34mout[39;49;00m Item) [34mdo[39;49;00m
   157	                  An_Item := Data(Head);
   158	               [34mend[39;49;00m [32mRemove[39;49;00m;
   159	               Head := Head [35mmod[39;49;00m Q_Size + [34m1[39;49;00m;
   160	               Length := Length - [34m1[39;49;00m;
   161	         [34mend[39;49;00m [34mselect[39;49;00m;
   162	      [34mend[39;49;00m [34mloop[39;49;00m;
   163	   [34mend[39;49;00m [32mCyclic_Buffer_Task_Type[39;49;00m;
   164
   165
   166
   167	   [34mprocedure[39;49;00m [32mScan_Next_Token[39;49;00m
   168	     ([31mS[39;49;00m           : [31min[39;49;00m     [31mString[39;49;00m;
   169	      [31mStart_Index[39;49;00m :    [31mout[39;49;00m [31mPositive[39;49;00m;
   170	      [31mEnd_Index[39;49;00m   : [31min[39;49;00m [31mout[39;49;00m [31mNatural[39;49;00m;     [37m--  Tricky comment[39;49;00m
   171	      [31mLine_Number[39;49;00m : [31min[39;49;00m [31mout[39;49;00m [31mPositive[39;49;00m;
   172	      [31mToken[39;49;00m       :    [31mout[39;49;00m [31mToken_T[39;49;00m);
   173
   174	   [34mprocedure[39;49;00m [32mScan_Next_Token[39;49;00m
   175	     ([31mS[39;49;00m           : [31min[39;49;00m     [31mString[39;49;00m;
   176	      [31mStart_Index[39;49;00m :    [31mout[39;49;00m [31mPositive[39;49;00m;
   177	      [31mEnd_Index[39;49;00m   : [31min[39;49;00m [31mout[39;49;00m [31mNatural[39;49;00m;     [37m--  Another comment[39;49;00m
   178	      [31mLine_Number[39;49;00m : [31min[39;49;00m [31mout[39;49;00m [31mPositive[39;49;00m;
   179	      [31mToken[39;49;00m       :    [31mout[39;49;00m [31mToken_T[39;49;00m)
   180	   [34mis[39;49;00m
   181	   [34mbegin[39;49;00m
   182	      Scanner_Loop:
   183	      [34mloop[39;49;00m
   184	         [34mif[39;49;00m New_State = End_Error [34mthen[39;49;00m
   185	            [34mexit[39;49;00m Scanner_Loop;
   186	         [34mend[39;49;00m [34mif[39;49;00m;
   187
   188	         [34mif[39;49;00m State = Start [35mand[39;49;00m New_State /= Start [34mthen[39;49;00m
   189	            Start_Index := Peek_Index;
   190	         [34mend[39;49;00m [34mif[39;49;00m;
   191	      [34mend[39;49;00m [34mloop[39;49;00m [32mScanner_Loop[39;49;00m;
   192	   [34mend[39;49;00m [32mScan_Next_Token[39;49;00m;
   193
   194	   [34mprocedure[39;49;00m [32mAdvance[39;49;00m [34mis[39;49;00m
   195	   [34mbegin[39;49;00m
   196	      Peek_Index := Peek_Index + [34m1[39;49;00m;
   197	   [34mend[39;49;00m [32mAdvance[39;49;00m;
   198
   199
   200	   [37m-- Eliminate the leading space that Ada puts in front of positive[39;49;00m
   201	   [37m-- integer images.[39;49;00m
   202	   [34mfunction[39;49;00m [32mImage[39;49;00m([31mN[39;49;00m : [31min[39;49;00m [31mInteger[39;49;00m) [34mreturn[39;49;00m [36mString[39;49;00m [34mis[39;49;00m
   203	      S : [36mString[39;49;00m := [36mInteger[39;49;00m'[36mImage[39;49;00m(N);
   204	   [34mbegin[39;49;00m
   205	      [34mif[39;49;00m S([34m1[39;49;00m) = [33m' '[39;49;00m [34mthen[39;49;00m
   206	         [34mreturn[39;49;00m S([34m2[39;49;00m .. S'[36mLast[39;49;00m);
   207	      [34mend[39;49;00m [34mif[39;49;00m;
   208	      [34mreturn[39;49;00m S;
   209	   [34mend[39;49;00m [32mImage[39;49;00m;
   210
   211	[34mend[39;49;00m [32mScanner[39;49;00m;

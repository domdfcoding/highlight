     1^I[37m--  Model IED Simulator[39;49;00m$
     2^I[37m--  COL Gene Ressler, 1 December 2007[39;49;00m$
     3^I[34mwith[39;49;00m [04m[36mAda.Text_IO[39;49;00m;$
     4^I$
     5^I[34mwith[39;49;00m [04m[36mAda.Characters.Latin_1[39;49;00m;$
     6^I[34muse[39;49;00m  [04m[36mAda.Characters.Latin_1[39;49;00m;$
     7^I$
     8^I[34mwith[39;49;00m [04m[36mAda.Strings.Fixed[39;49;00m;$
     9^I[34muse[39;49;00m  [04m[36mAda.Strings.Fixed[39;49;00m;$
    10^I$
    11^I[34mwith[39;49;00m [04m[36mAda.Strings[39;49;00m;$
    12^I[34mwith[39;49;00m [04m[36mAda.Strings.Bounded[39;49;00m;$
    13^I$
    14^I[34mwith[39;49;00m [04m[36mBinary_Search[39;49;00m;$
    15^I$
    16^I[34mwith[39;49;00m [04m[36mAda.Containers.Generic_Array_Sort[39;49;00m;$
    17^I$
    18^I[34mpackage[39;49;00m [34mbody[39;49;00m [04m[32mScanner[39;49;00m [34mis[39;49;00m$
    19^I   $
    20^I   [31mConstant_123[39;49;00m   : [34mconstant[39;49;00m [36mCharacter[39;49;00m := [36mCharacter[39;49;00m'[36mVal[39;49;00m ([34m16#00#[39;49;00m);$
    21^I   [31mMAX_KEYWORD_LENGTH_C[39;49;00m : [34mconstant[39;49;00m [36mNatural[39;49;00m := [34m24[39;49;00m;$
    22^I   $
    23^I   [31mNew_Constant[39;49;00m : [34mconstant[39;49;00m New_Type$
    24^I     := [34m2[39;49;00m;$
    25^I   $
    26^I   [31mKEYWORDS_C[39;49;00m : [34mconstant[39;49;00m Keyword_Array_T :=$
    27^I     (To_BS([33m"description"[39;49;00m),$
    28^I      To_BS([33m"with"[39;49;00m));$
    29^I   $
    30^I   [34mprocedure[39;49;00m [32mBlah[39;49;00m;$
    31^I   $
    32^I   [34mprocedure[39;49;00m [32mblah[39;49;00m [34mis[39;49;00m$
    33^I   [34mbegin[39;49;00m$
    34^I      $
    35^I      Declaration:$
    36^I      [34mdeclare[39;49;00m$
    37^I         Joe : Type_Type := Random;$
    38^I      [34mbegin[39;49;00m$
    39^I         Do_Something;$
    40^I      [34mend[39;49;00m [32mDeclaration[39;49;00m;$
    41^I      Loop_ID:$
    42^I         [34mloop[39;49;00m$
    43^I            Loop_Do;$
    44^I            [34mexit[39;49;00m [34mwhen[39;49;00m [34m1[39;49;00m=[34m2[39;49;00m;$
    45^I         [34mend[39;49;00m [34mloop[39;49;00m [34mLoop[39;49;00m[32m_ID[39;49;00m;$
    46^I      [34mif[39;49;00m [34mTrue[39;49;00m [35mor else[39;49;00m [34mFalse[39;49;00m [34mthen[39;49;00m$
    47^I         Do_This();$
    48^I      [34melsif[39;49;00m [35mnot[39;49;00m [34mFalse[39;49;00m [35mand then[39;49;00m [34mTrue[39;49;00m [34mthen[39;49;00m$
    49^I         Do_That;$
    50^I      [34melse[39;49;00m$
    51^I         Panic;$
    52^I      [34mend[39;49;00m [34mif[39;49;00m;$
    53^I   [34mend[39;49;00m [32mblah[39;49;00m;$
    54^I   $
    55^I   [34mfunction[39;49;00m [32m"*"[39;49;00m ([31mLeft[39;49;00m, [31mRight[39;49;00m : [31min[39;49;00m [31mInteger[39;49;00m) [34mreturn[39;49;00m [36mInteger[39;49;00m [34mis[39;49;00m$
    56^I   [34mbegin[39;49;00m$
    57^I      <<Goto_Label>>$
    58^I      [34mgoto[39;49;00m Goto_Label;$
    59^I      [34mreturn[39;49;00m Left + Right;$
    60^I   [34mend[39;49;00m [32m"*"[39;49;00m;$
    61^I   $
    62^I   [34mfunction[39;49;00m [32mFunction_Specification[39;49;00m$
    63^I     ([31mParam_1[39;49;00m        : [31min[39;49;00m [31mBlah[39;49;00m; $
    64^I      [31mParam2[39;49;00m, [31mparam3[39;49;00m : [31min[39;49;00m [31maccess[39;49;00m [31mBlah_Type[39;49;00m := [31m0[39;49;00m)$
    65^I     [34mreturn[39;49;00m It_Type;$
    66^I   $
    67^I   [34mpackage[39;49;00m [04m[32mRename_Check[39;49;00m [34mrenames[39;49;00m [04m[32mAda.Text_IO[39;49;00m;$
    68^I$
    69^I   [34mtype[39;49;00m [36mNew_Float[39;49;00m [34mis[39;49;00m [34mdelta[39;49;00m [34m0.001[39;49;00m [34mdigits[39;49;00m [34m12[39;49;00m;$
    70^I   $
    71^I   [34mpackage[39;49;00m [04m[32mPackage_Inst[39;49;00m [34mis new[39;49;00m [04m[32mAda.Strings.Bounded.Generic_Bounded_Length[39;49;00m$
    72^I     ([31mMax[39;49;00m => MAX_KEYWORD_LENGTH_C);$
    73^I$
    74^I   [34mtype[39;49;00m [36mArray_Decl12[39;49;00m [34mis[39;49;00m [34marray[39;49;00m ([36mPositive[39;49;00m [34mrange[39;49;00m <>) [34mof[39;49;00m SB.Bounded_String;$
    75^I   [34mtype[39;49;00m [36mArray_Decl3[39;49;00m [34mis[39;49;00m [34marray[39;49;00m ([36mNew_Type[39;49;00m [34mrange[39;49;00m Thing_1 .. Thing_2) [34mof[39;49;00m SB.Bounded_String;$
    76^I$
    77^I   [34mtype[39;49;00m [36mBoring_Type[39;49;00m [34mis[39;49;00m$
    78^I     ([31mStart[39;49;00m,$
    79^I      [31mEnd_Error[39;49;00m);$
    80^I$
    81^I   [34msubtype[39;49;00m [36mSub_Type_check[39;49;00m [34mis[39;49;00m [36mCharacter[39;49;00m [34mrange[39;49;00m '[36m0[39;49;00m' .. '[36m9[39;49;00m';$
    82^I   $
    83^I   [31mInitialized_Array[39;49;00m : [34mconstant[39;49;00m Transistion_Array_T :=$
    84^I     (Start =>$
    85^I        (Letter_Lower | Letter_Upper => Saw_Alpha,$
    86^I         [33m' '[39;49;00m | HT | CR | LF          => Start,$
    87^I         [34mothers[39;49;00m => Begin_Error),$
    88^I$
    89^I      End_Error => ([34mothers[39;49;00m => Start)$
    90^I$
    91^I     );$
    92^I$
    93^I   [34mtype[39;49;00m [36mRecorder[39;49;00m [34mis[39;49;00m [34mrecord[39;49;00m$
    94^I      Advance      : [36mBoolean[39;49;00m;$
    95^I      Return_Token : Token_T;$
    96^I   [34mend record[39;49;00m;$
    97^I   $
    98^I   [34mfor[39;49;00m Recorder [34muse[39;49;00m [04m[36m8[39;49;00m;$
    99^I   $
   100^I   [34mtype[39;49;00m [36mNull_Record[39;49;00m [34mis[39;49;00m [34mnull record[39;49;00m;$
   101^I   $
   102^I   [34mtype[39;49;00m [36mDiscriminated_Record[39;49;00m ([31mSize[39;49;00m : [31mNatural[39;49;00m) [34mis[39;49;00m $
   103^I      [34mrecord[39;49;00m$
   104^I         A : [36mString[39;49;00m ([34m1[39;49;00m .. Size);$
   105^I      [34mend record[39;49;00m;$
   106^I   $
   107^I   [34mpragma[39;49;00m [36mUnchecked_Union[39;49;00m (Union);$
   108^I   [34mpragma[39;49;00m [36mConvention[39;49;00m (C, Union);$
   109^I   $
   110^I   [34mtype[39;49;00m [36mPerson[39;49;00m [34mis[39;49;00m [34mtagged[39;49;00m $
   111^I      [34mrecord[39;49;00m$
   112^I         Name   : [36mString[39;49;00m ([34m1[39;49;00m .. [34m10[39;49;00m);$
   113^I         Gender : Gender_Type;$
   114^I      [34mend record[39;49;00m;$
   115^I   $
   116^I   [34mtype[39;49;00m [36mProgrammer[39;49;00m [34mis[39;49;00m [34mnew[39;49;00m Person [34mwith[39;49;00m$
   117^I      [34mrecord[39;49;00m$
   118^I         Skilled_In : Language_List;$
   119^I         Favorite_Langauge : Python_Type;$
   120^I      [34mend record[39;49;00m;$
   121^I   $
   122^I   [34mtype[39;49;00m [36mProgrammer[39;49;00m [34mis[39;49;00m [34mnew[39;49;00m Person $
   123^I     [34mand[39;49;00m Printable $
   124^I     [34mwith[39;49;00m $
   125^I      [34mrecord[39;49;00m$
   126^I         Skilled_In : Language_List;$
   127^I         Blah : [34maliased[39;49;00m [36mInteger[39;49;00m;$
   128^I      [34mend record[39;49;00m;$
   129^I   $
   130^I   [37m---------------------[39;49;00m$
   131^I   [37m-- Scan_Next_Token --[39;49;00m$
   132^I   [37m---------------------[39;49;00m$
   133^I   $
   134^I   [34mtask[39;49;00m Cyclic_Buffer_Task_Type [34mis[39;49;00m$
   135^I      [34mentry[39;49;00m [32mInsert[39;49;00m ([31mAn_Item[39;49;00m : [31min[39;49;00m  [31mItem[39;49;00m);$
   136^I      [34mentry[39;49;00m [32mRemove[39;49;00m ([31mAn_Item[39;49;00m : [31mout[39;49;00m [31mItem[39;49;00m);$
   137^I   [34mend[39;49;00m [32mCyclic_Buffer_Task_Type[39;49;00m;$
   138^I   $
   139^I   [34mtask[39;49;00m [34mbody[39;49;00m Cyclic_Buffer_Task_Type [34mis[39;49;00m$
   140^I      [31mQ_Size[39;49;00m : [34mconstant[39;49;00m := [34m100[39;49;00m;$
   141^I      [34msubtype[39;49;00m [36mQ_Range[39;49;00m [34mis[39;49;00m [36mPositive[39;49;00m [34mrange[39;49;00m [34m1[39;49;00m .. Q_Size;$
   142^I      Length : [36mNatural[39;49;00m [34mrange[39;49;00m [34m0[39;49;00m .. Q_Size := [34m0[39;49;00m;$
   143^I      Head, Tail : Q_Range := [34m1[39;49;00m;$
   144^I      Data : [34marray[39;49;00m (Q_Range) [34mof[39;49;00m Item;$
   145^I   [34mbegin[39;49;00m$
   146^I      [34mloop[39;49;00m$
   147^I         [34mselect[39;49;00m$
   148^I            [34mwhen[39;49;00m Length < Q_Size =>$
   149^I               [34maccept[39;49;00m Insert (An_Item : [35min[39;49;00m  Item) [34mdo[39;49;00m$
   150^I                  Data(Tail) := An_Item;$
   151^I               [34mend[39;49;00m [32mInsert[39;49;00m;$
   152^I               Tail := Tail [35mmod[39;49;00m Q_Size + [34m1[39;49;00m;$
   153^I               Length := Length + [34m1[39;49;00m;$
   154^I         [34mor[39;49;00m$
   155^I            [34mwhen[39;49;00m Length > [34m0[39;49;00m =>$
   156^I               [34maccept[39;49;00m Remove (An_Item : [34mout[39;49;00m Item) [34mdo[39;49;00m$
   157^I                  An_Item := Data(Head);$
   158^I               [34mend[39;49;00m [32mRemove[39;49;00m;$
   159^I               Head := Head [35mmod[39;49;00m Q_Size + [34m1[39;49;00m;$
   160^I               Length := Length - [34m1[39;49;00m;$
   161^I         [34mend[39;49;00m [34mselect[39;49;00m;$
   162^I      [34mend[39;49;00m [34mloop[39;49;00m;$
   163^I   [34mend[39;49;00m [32mCyclic_Buffer_Task_Type[39;49;00m;$
   164^I     $
   165^I     $
   166^I   $
   167^I   [34mprocedure[39;49;00m [32mScan_Next_Token[39;49;00m$
   168^I     ([31mS[39;49;00m           : [31min[39;49;00m     [31mString[39;49;00m;$
   169^I      [31mStart_Index[39;49;00m :    [31mout[39;49;00m [31mPositive[39;49;00m;$
   170^I      [31mEnd_Index[39;49;00m   : [31min[39;49;00m [31mout[39;49;00m [31mNatural[39;49;00m;     [37m--  Tricky comment[39;49;00m$
   171^I      [31mLine_Number[39;49;00m : [31min[39;49;00m [31mout[39;49;00m [31mPositive[39;49;00m;$
   172^I      [31mToken[39;49;00m       :    [31mout[39;49;00m [31mToken_T[39;49;00m);$
   173^I   $
   174^I   [34mprocedure[39;49;00m [32mScan_Next_Token[39;49;00m$
   175^I     ([31mS[39;49;00m           : [31min[39;49;00m     [31mString[39;49;00m;$
   176^I      [31mStart_Index[39;49;00m :    [31mout[39;49;00m [31mPositive[39;49;00m;$
   177^I      [31mEnd_Index[39;49;00m   : [31min[39;49;00m [31mout[39;49;00m [31mNatural[39;49;00m;     [37m--  Another comment[39;49;00m$
   178^I      [31mLine_Number[39;49;00m : [31min[39;49;00m [31mout[39;49;00m [31mPositive[39;49;00m;$
   179^I      [31mToken[39;49;00m       :    [31mout[39;49;00m [31mToken_T[39;49;00m)$
   180^I   [34mis[39;49;00m$
   181^I   [34mbegin[39;49;00m$
   182^I      Scanner_Loop:$
   183^I      [34mloop[39;49;00m$
   184^I         [34mif[39;49;00m New_State = End_Error [34mthen[39;49;00m$
   185^I            [34mexit[39;49;00m Scanner_Loop;$
   186^I         [34mend[39;49;00m [34mif[39;49;00m;$
   187^I$
   188^I         [34mif[39;49;00m State = Start [35mand[39;49;00m New_State /= Start [34mthen[39;49;00m$
   189^I            Start_Index := Peek_Index;$
   190^I         [34mend[39;49;00m [34mif[39;49;00m;$
   191^I      [34mend[39;49;00m [34mloop[39;49;00m [32mScanner_Loop[39;49;00m;$
   192^I   [34mend[39;49;00m [32mScan_Next_Token[39;49;00m;$
   193^I   $
   194^I   [34mprocedure[39;49;00m [32mAdvance[39;49;00m [34mis[39;49;00m$
   195^I   [34mbegin[39;49;00m$
   196^I      Peek_Index := Peek_Index + [34m1[39;49;00m;$
   197^I   [34mend[39;49;00m [32mAdvance[39;49;00m;$
   198^I      $
   199^I$
   200^I   [37m-- Eliminate the leading space that Ada puts in front of positive[39;49;00m$
   201^I   [37m-- integer images.[39;49;00m$
   202^I   [34mfunction[39;49;00m [32mImage[39;49;00m([31mN[39;49;00m : [31min[39;49;00m [31mInteger[39;49;00m) [34mreturn[39;49;00m [36mString[39;49;00m [34mis[39;49;00m$
   203^I      S : [36mString[39;49;00m := [36mInteger[39;49;00m'[36mImage[39;49;00m(N);$
   204^I   [34mbegin[39;49;00m$
   205^I      [34mif[39;49;00m S([34m1[39;49;00m) = [33m' '[39;49;00m [34mthen[39;49;00m$
   206^I         [34mreturn[39;49;00m S([34m2[39;49;00m .. S'[36mLast[39;49;00m);$
   207^I      [34mend[39;49;00m [34mif[39;49;00m;$
   208^I      [34mreturn[39;49;00m S;$
   209^I   [34mend[39;49;00m [32mImage[39;49;00m;$
   210^I$
   211^I[34mend[39;49;00m [32mScanner[39;49;00m;$

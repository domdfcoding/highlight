     1	[37m/* A Bison parser, made by GNU Bison 2.0.  */[39;49;00m[37m[39;49;00m$
     2	[37m[39;49;00m$
     3	[37m/* Skeleton parser for Yacc-like parsing with Bison,[39;49;00m$
     4	[37m   Copyright (C) 1984, 1989, 1990, 2000, 2001, 2002, 2003, 2004 Free Software Foundation, Inc.[39;49;00m$
     5	[37m[39;49;00m$
     6	[37m   This program is free software; you can redistribute it and/or modify[39;49;00m$
     7	[37m   it under the terms of the GNU General Public License as published by[39;49;00m$
     8	[37m   the Free Software Foundation; either version 2, or (at your option)[39;49;00m$
     9	[37m   any later version.[39;49;00m$
    10	[37m[39;49;00m$
    11	[37m   This program is distributed in the hope that it will be useful,[39;49;00m$
    12	[37m   but WITHOUT ANY WARRANTY; without even the implied warranty of[39;49;00m$
    13	[37m   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the[39;49;00m$
    14	[37m   GNU General Public License for more details.[39;49;00m$
    15	[37m[39;49;00m$
    16	[37m   You should have received a copy of the GNU General Public License[39;49;00m$
    17	[37m   along with this program; if not, write to the Free Software[39;49;00m$
    18	[37m   Foundation, Inc., 59 Temple Place - Suite 330,[39;49;00m$
    19	[37m   Boston, MA 02111-1307, USA.  */[39;49;00m[37m[39;49;00m$
    20	[37m[39;49;00m$
    21	[37m/* As a special exception, when this file is copied by Bison into a[39;49;00m$
    22	[37m   Bison output file, you may use that output file without restriction.[39;49;00m$
    23	[37m   This special exception was added by the Free Software Foundation[39;49;00m$
    24	[37m   in version 1.24 of Bison.  */[39;49;00m[37m[39;49;00m$
    25	[37m[39;49;00m$
    26	[37m/* Tokens.  */[39;49;00m[37m[39;49;00m$
    27	[36m#[39;49;00m[36mifndef YYTOKENTYPE[39;49;00m[36m[39;49;00m$
    28	[36m#[39;49;00m[36m define YYTOKENTYPE[39;49;00m[36m[39;49;00m$
    29	[37m   [39;49;00m[37m/* Put the tokens into the symbol table, so that GDB and other debuggers[39;49;00m$
    30	[37m      know about them.  */[39;49;00m[37m[39;49;00m$
    31	[37m   [39;49;00m[34menum[39;49;00m[37m [39;49;00myytokentype[37m [39;49;00m{[37m[39;49;00m$
    32	[37m     [39;49;00mIDENTIFIER[37m [39;49;00m=[37m [39;49;00m[34m258[39;49;00m,[37m[39;49;00m$
    33	[37m     [39;49;00mCONSTANT[37m [39;49;00m=[37m [39;49;00m[34m259[39;49;00m,[37m[39;49;00m$
    34	[37m     [39;49;00mSTRING_LITERAL[37m [39;49;00m=[37m [39;49;00m[34m260[39;49;00m,[37m[39;49;00m$
    35	[37m     [39;49;00mSIZEOF[37m [39;49;00m=[37m [39;49;00m[34m261[39;49;00m,[37m[39;49;00m$
    36	[37m     [39;49;00mPTR_OP[37m [39;49;00m=[37m [39;49;00m[34m262[39;49;00m,[37m[39;49;00m$
    37	[37m     [39;49;00mINC_OP[37m [39;49;00m=[37m [39;49;00m[34m263[39;49;00m,[37m[39;49;00m$
    38	[37m     [39;49;00mDEC_OP[37m [39;49;00m=[37m [39;49;00m[34m264[39;49;00m,[37m[39;49;00m$
    39	[37m     [39;49;00mLEFT_OP[37m [39;49;00m=[37m [39;49;00m[34m265[39;49;00m,[37m[39;49;00m$
    40	[37m     [39;49;00mRIGHT_OP[37m [39;49;00m=[37m [39;49;00m[34m266[39;49;00m,[37m[39;49;00m$
    41	[37m     [39;49;00mLE_OP[37m [39;49;00m=[37m [39;49;00m[34m267[39;49;00m,[37m[39;49;00m$
    42	[37m     [39;49;00mGE_OP[37m [39;49;00m=[37m [39;49;00m[34m268[39;49;00m,[37m[39;49;00m$
    43	[37m     [39;49;00mEQ_OP[37m [39;49;00m=[37m [39;49;00m[34m269[39;49;00m,[37m[39;49;00m$
    44	[37m     [39;49;00mNE_OP[37m [39;49;00m=[37m [39;49;00m[34m270[39;49;00m,[37m[39;49;00m$
    45	[37m     [39;49;00mAND_OP[37m [39;49;00m=[37m [39;49;00m[34m271[39;49;00m,[37m[39;49;00m$
    46	[37m     [39;49;00mOR_OP[37m [39;49;00m=[37m [39;49;00m[34m272[39;49;00m,[37m[39;49;00m$
    47	[37m     [39;49;00mMUL_ASSIGN[37m [39;49;00m=[37m [39;49;00m[34m273[39;49;00m,[37m[39;49;00m$
    48	[37m     [39;49;00mDIV_ASSIGN[37m [39;49;00m=[37m [39;49;00m[34m274[39;49;00m,[37m[39;49;00m$
    49	[37m     [39;49;00mMOD_ASSIGN[37m [39;49;00m=[37m [39;49;00m[34m275[39;49;00m,[37m[39;49;00m$
    50	[37m     [39;49;00mADD_ASSIGN[37m [39;49;00m=[37m [39;49;00m[34m276[39;49;00m,[37m[39;49;00m$
    51	[37m     [39;49;00mSUB_ASSIGN[37m [39;49;00m=[37m [39;49;00m[34m277[39;49;00m,[37m[39;49;00m$
    52	[37m     [39;49;00mLEFT_ASSIGN[37m [39;49;00m=[37m [39;49;00m[34m278[39;49;00m,[37m[39;49;00m$
    53	[37m     [39;49;00mRIGHT_ASSIGN[37m [39;49;00m=[37m [39;49;00m[34m279[39;49;00m,[37m[39;49;00m$
    54	[37m     [39;49;00mAND_ASSIGN[37m [39;49;00m=[37m [39;49;00m[34m280[39;49;00m,[37m[39;49;00m$
    55	[37m     [39;49;00mXOR_ASSIGN[37m [39;49;00m=[37m [39;49;00m[34m281[39;49;00m,[37m[39;49;00m$
    56	[37m     [39;49;00mOR_ASSIGN[37m [39;49;00m=[37m [39;49;00m[34m282[39;49;00m,[37m[39;49;00m$
    57	[37m     [39;49;00mTYPE_NAME[37m [39;49;00m=[37m [39;49;00m[34m283[39;49;00m,[37m[39;49;00m$
    58	[37m     [39;49;00mTYPEDEF[37m [39;49;00m=[37m [39;49;00m[34m284[39;49;00m,[37m[39;49;00m$
    59	[37m     [39;49;00mEXTERN[37m [39;49;00m=[37m [39;49;00m[34m285[39;49;00m,[37m[39;49;00m$
    60	[37m     [39;49;00mSTATIC[37m [39;49;00m=[37m [39;49;00m[34m286[39;49;00m,[37m[39;49;00m$
    61	[37m     [39;49;00mAUTO[37m [39;49;00m=[37m [39;49;00m[34m287[39;49;00m,[37m[39;49;00m$
    62	[37m     [39;49;00mREGISTER[37m [39;49;00m=[37m [39;49;00m[34m288[39;49;00m,[37m[39;49;00m$
    63	[37m     [39;49;00mCHAR[37m [39;49;00m=[37m [39;49;00m[34m289[39;49;00m,[37m[39;49;00m$
    64	[37m     [39;49;00mSHORT[37m [39;49;00m=[37m [39;49;00m[34m290[39;49;00m,[37m[39;49;00m$
    65	[37m     [39;49;00mINT[37m [39;49;00m=[37m [39;49;00m[34m291[39;49;00m,[37m[39;49;00m$
    66	[37m     [39;49;00mUINT[37m [39;49;00m=[37m [39;49;00m[34m292[39;49;00m,[37m[39;49;00m$
    67	[37m     [39;49;00mINT64[37m [39;49;00m=[37m [39;49;00m[34m293[39;49;00m,[37m[39;49;00m$
    68	[37m     [39;49;00mLONG[37m [39;49;00m=[37m [39;49;00m[34m294[39;49;00m,[37m[39;49;00m$
    69	[37m     [39;49;00mSIGNED[37m [39;49;00m=[37m [39;49;00m[34m295[39;49;00m,[37m[39;49;00m$
    70	[37m     [39;49;00mUNSIGNED[37m [39;49;00m=[37m [39;49;00m[34m296[39;49;00m,[37m[39;49;00m$
    71	[37m     [39;49;00mFLOAT[37m [39;49;00m=[37m [39;49;00m[34m297[39;49;00m,[37m[39;49;00m$
    72	[37m     [39;49;00mDOUBLE[37m [39;49;00m=[37m [39;49;00m[34m298[39;49;00m,[37m[39;49;00m$
    73	[37m     [39;49;00mCONST[37m [39;49;00m=[37m [39;49;00m[34m299[39;49;00m,[37m[39;49;00m$
    74	[37m     [39;49;00mVOLATILE[37m [39;49;00m=[37m [39;49;00m[34m300[39;49;00m,[37m[39;49;00m$
    75	[37m     [39;49;00mVOID[37m [39;49;00m=[37m [39;49;00m[34m301[39;49;00m,[37m[39;49;00m$
    76	[37m     [39;49;00mVALIST[37m [39;49;00m=[37m [39;49;00m[34m302[39;49;00m,[37m[39;49;00m$
    77	[37m     [39;49;00mSTRUCT[37m [39;49;00m=[37m [39;49;00m[34m303[39;49;00m,[37m[39;49;00m$
    78	[37m     [39;49;00mUNION[37m [39;49;00m=[37m [39;49;00m[34m304[39;49;00m,[37m[39;49;00m$
    79	[37m     [39;49;00mENUM[37m [39;49;00m=[37m [39;49;00m[34m305[39;49;00m,[37m[39;49;00m$
    80	[37m     [39;49;00mELLIPSIS[37m [39;49;00m=[37m [39;49;00m[34m306[39;49;00m,[37m[39;49;00m$
    81	[37m     [39;49;00mCASE[37m [39;49;00m=[37m [39;49;00m[34m307[39;49;00m,[37m[39;49;00m$
    82	[37m     [39;49;00mDEFAULT[37m [39;49;00m=[37m [39;49;00m[34m308[39;49;00m,[37m[39;49;00m$
    83	[37m     [39;49;00mIF[37m [39;49;00m=[37m [39;49;00m[34m309[39;49;00m,[37m[39;49;00m$
    84	[37m     [39;49;00mSWITCH[37m [39;49;00m=[37m [39;49;00m[34m310[39;49;00m,[37m[39;49;00m$
    85	[37m     [39;49;00mWHILE[37m [39;49;00m=[37m [39;49;00m[34m311[39;49;00m,[37m[39;49;00m$
    86	[37m     [39;49;00mDO[37m [39;49;00m=[37m [39;49;00m[34m312[39;49;00m,[37m[39;49;00m$
    87	[37m     [39;49;00mFOR[37m [39;49;00m=[37m [39;49;00m[34m313[39;49;00m,[37m[39;49;00m$
    88	[37m     [39;49;00mGOTO[37m [39;49;00m=[37m [39;49;00m[34m314[39;49;00m,[37m[39;49;00m$
    89	[37m     [39;49;00mCONTINUE[37m [39;49;00m=[37m [39;49;00m[34m315[39;49;00m,[37m[39;49;00m$
    90	[37m     [39;49;00mBREAK[37m [39;49;00m=[37m [39;49;00m[34m316[39;49;00m,[37m[39;49;00m$
    91	[37m     [39;49;00mRETURN[37m [39;49;00m=[37m [39;49;00m[34m317[39;49;00m,[37m[39;49;00m$
    92	[37m     [39;49;00mIFX[37m [39;49;00m=[37m [39;49;00m[34m318[39;49;00m,[37m[39;49;00m$
    93	[37m     [39;49;00mELSE[37m [39;49;00m=[37m [39;49;00m[34m319[39;49;00m,[37m[39;49;00m$
    94	[37m     [39;49;00mCLASS[37m [39;49;00m=[37m [39;49;00m[34m320[39;49;00m,[37m[39;49;00m$
    95	[37m     [39;49;00mTHISCLASS[37m [39;49;00m=[37m [39;49;00m[34m321[39;49;00m,[37m[39;49;00m$
    96	[37m     [39;49;00mCLASS_NAME[37m [39;49;00m=[37m [39;49;00m[34m322[39;49;00m,[37m[39;49;00m$
    97	[37m     [39;49;00mPROPERTY[37m [39;49;00m=[37m [39;49;00m[34m323[39;49;00m,[37m[39;49;00m$
    98	[37m     [39;49;00mSETPROP[37m [39;49;00m=[37m [39;49;00m[34m324[39;49;00m,[37m[39;49;00m$
    99	[37m     [39;49;00mGETPROP[37m [39;49;00m=[37m [39;49;00m[34m325[39;49;00m,[37m[39;49;00m$
   100	[37m     [39;49;00mNEWOP[37m [39;49;00m=[37m [39;49;00m[34m326[39;49;00m,[37m[39;49;00m$
   101	[37m     [39;49;00mRENEW[37m [39;49;00m=[37m [39;49;00m[34m327[39;49;00m,[37m[39;49;00m$
   102	[37m     [39;49;00mDELETE[37m [39;49;00m=[37m [39;49;00m[34m328[39;49;00m,[37m[39;49;00m$
   103	[37m     [39;49;00mEXT_DECL[37m [39;49;00m=[37m [39;49;00m[34m329[39;49;00m,[37m[39;49;00m$
   104	[37m     [39;49;00mEXT_STORAGE[37m [39;49;00m=[37m [39;49;00m[34m330[39;49;00m,[37m[39;49;00m$
   105	[37m     [39;49;00mIMPORT[37m [39;49;00m=[37m [39;49;00m[34m331[39;49;00m,[37m[39;49;00m$
   106	[37m     [39;49;00mDEFINE[37m [39;49;00m=[37m [39;49;00m[34m332[39;49;00m,[37m[39;49;00m$
   107	[37m     [39;49;00mVIRTUAL[37m [39;49;00m=[37m [39;49;00m[34m333[39;49;00m,[37m[39;49;00m$
   108	[37m     [39;49;00mEXT_ATTRIB[37m [39;49;00m=[37m [39;49;00m[34m334[39;49;00m,[37m[39;49;00m$
   109	[37m     [39;49;00mPUBLIC[37m [39;49;00m=[37m [39;49;00m[34m335[39;49;00m,[37m[39;49;00m$
   110	[37m     [39;49;00mPRIVATE[37m [39;49;00m=[37m [39;49;00m[34m336[39;49;00m,[37m[39;49;00m$
   111	[37m     [39;49;00mTYPED_OBJECT[37m [39;49;00m=[37m [39;49;00m[34m337[39;49;00m,[37m[39;49;00m$
   112	[37m     [39;49;00mANY_OBJECT[37m [39;49;00m=[37m [39;49;00m[34m338[39;49;00m,[37m[39;49;00m$
   113	[37m     [39;49;00m_INCREF[37m [39;49;00m=[37m [39;49;00m[34m339[39;49;00m,[37m[39;49;00m$
   114	[37m     [39;49;00mEXTENSION[37m [39;49;00m=[37m [39;49;00m[34m340[39;49;00m,[37m[39;49;00m$
   115	[37m     [39;49;00mASM[37m [39;49;00m=[37m [39;49;00m[34m341[39;49;00m,[37m[39;49;00m$
   116	[37m     [39;49;00mTYPEOF[37m [39;49;00m=[37m [39;49;00m[34m342[39;49;00m,[37m[39;49;00m$
   117	[37m     [39;49;00mWATCH[37m [39;49;00m=[37m [39;49;00m[34m343[39;49;00m,[37m[39;49;00m$
   118	[37m     [39;49;00mSTOPWATCHING[37m [39;49;00m=[37m [39;49;00m[34m344[39;49;00m,[37m[39;49;00m$
   119	[37m     [39;49;00mFIREWATCHERS[37m [39;49;00m=[37m [39;49;00m[34m345[39;49;00m,[37m[39;49;00m$
   120	[37m     [39;49;00mWATCHABLE[37m [39;49;00m=[37m [39;49;00m[34m346[39;49;00m,[37m[39;49;00m$
   121	[37m     [39;49;00mCLASS_DESIGNER[37m [39;49;00m=[37m [39;49;00m[34m347[39;49;00m,[37m[39;49;00m$
   122	[37m     [39;49;00mCLASS_NO_EXPANSION[37m [39;49;00m=[37m [39;49;00m[34m348[39;49;00m,[37m[39;49;00m$
   123	[37m     [39;49;00mCLASS_FIXED[37m [39;49;00m=[37m [39;49;00m[34m349[39;49;00m,[37m[39;49;00m$
   124	[37m     [39;49;00mISPROPSET[37m [39;49;00m=[37m [39;49;00m[34m350[39;49;00m,[37m[39;49;00m$
   125	[37m     [39;49;00mCLASS_DEFAULT_PROPERTY[37m [39;49;00m=[37m [39;49;00m[34m351[39;49;00m,[37m[39;49;00m$
   126	[37m     [39;49;00mPROPERTY_CATEGORY[37m [39;49;00m=[37m [39;49;00m[34m352[39;49;00m,[37m[39;49;00m$
   127	[37m     [39;49;00mCLASS_DATA[37m [39;49;00m=[37m [39;49;00m[34m353[39;49;00m,[37m[39;49;00m$
   128	[37m     [39;49;00mCLASS_PROPERTY[37m [39;49;00m=[37m [39;49;00m[34m354[39;49;00m,[37m[39;49;00m$
   129	[37m     [39;49;00mSUBCLASS[37m [39;49;00m=[37m [39;49;00m[34m355[39;49;00m,[37m[39;49;00m$
   130	[37m     [39;49;00mNAMESPACE[37m [39;49;00m=[37m [39;49;00m[34m356[39;49;00m,[37m[39;49;00m$
   131	[37m     [39;49;00mNEW0OP[37m [39;49;00m=[37m [39;49;00m[34m357[39;49;00m,[37m[39;49;00m$
   132	[37m     [39;49;00mRENEW0[37m [39;49;00m=[37m [39;49;00m[34m358[39;49;00m,[37m[39;49;00m$
   133	[37m     [39;49;00mVAARG[37m [39;49;00m=[37m [39;49;00m[34m359[39;49;00m,[37m[39;49;00m$
   134	[37m     [39;49;00mDBTABLE[37m [39;49;00m=[37m [39;49;00m[34m360[39;49;00m,[37m[39;49;00m$
   135	[37m     [39;49;00mDBFIELD[37m [39;49;00m=[37m [39;49;00m[34m361[39;49;00m,[37m[39;49;00m$
   136	[37m     [39;49;00mDBINDEX[37m [39;49;00m=[37m [39;49;00m[34m362[39;49;00m,[37m[39;49;00m$
   137	[37m     [39;49;00mDATABASE_OPEN[37m [39;49;00m=[37m [39;49;00m[34m363[39;49;00m[37m[39;49;00m$
   138	[37m   [39;49;00m};[37m[39;49;00m$
   139	[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   140	[36m#[39;49;00m[36mdefine IDENTIFIER 258[39;49;00m[36m[39;49;00m$
   141	[36m#[39;49;00m[36mdefine CONSTANT 259[39;49;00m[36m[39;49;00m$
   142	[36m#[39;49;00m[36mdefine STRING_LITERAL 260[39;49;00m[36m[39;49;00m$
   143	[36m#[39;49;00m[36mdefine SIZEOF 261[39;49;00m[36m[39;49;00m$
   144	[36m#[39;49;00m[36mdefine PTR_OP 262[39;49;00m[36m[39;49;00m$
   145	[36m#[39;49;00m[36mdefine INC_OP 263[39;49;00m[36m[39;49;00m$
   146	[36m#[39;49;00m[36mdefine DEC_OP 264[39;49;00m[36m[39;49;00m$
   147	[36m#[39;49;00m[36mdefine LEFT_OP 265[39;49;00m[36m[39;49;00m$
   148	[36m#[39;49;00m[36mdefine RIGHT_OP 266[39;49;00m[36m[39;49;00m$
   149	[36m#[39;49;00m[36mdefine LE_OP 267[39;49;00m[36m[39;49;00m$
   150	[36m#[39;49;00m[36mdefine GE_OP 268[39;49;00m[36m[39;49;00m$
   151	[36m#[39;49;00m[36mdefine EQ_OP 269[39;49;00m[36m[39;49;00m$
   152	[36m#[39;49;00m[36mdefine NE_OP 270[39;49;00m[36m[39;49;00m$
   153	[36m#[39;49;00m[36mdefine AND_OP 271[39;49;00m[36m[39;49;00m$
   154	[36m#[39;49;00m[36mdefine OR_OP 272[39;49;00m[36m[39;49;00m$
   155	[36m#[39;49;00m[36mdefine MUL_ASSIGN 273[39;49;00m[36m[39;49;00m$
   156	[36m#[39;49;00m[36mdefine DIV_ASSIGN 274[39;49;00m[36m[39;49;00m$
   157	[36m#[39;49;00m[36mdefine MOD_ASSIGN 275[39;49;00m[36m[39;49;00m$
   158	[36m#[39;49;00m[36mdefine ADD_ASSIGN 276[39;49;00m[36m[39;49;00m$
   159	[36m#[39;49;00m[36mdefine SUB_ASSIGN 277[39;49;00m[36m[39;49;00m$
   160	[36m#[39;49;00m[36mdefine LEFT_ASSIGN 278[39;49;00m[36m[39;49;00m$
   161	[36m#[39;49;00m[36mdefine RIGHT_ASSIGN 279[39;49;00m[36m[39;49;00m$
   162	[36m#[39;49;00m[36mdefine AND_ASSIGN 280[39;49;00m[36m[39;49;00m$
   163	[36m#[39;49;00m[36mdefine XOR_ASSIGN 281[39;49;00m[36m[39;49;00m$
   164	[36m#[39;49;00m[36mdefine OR_ASSIGN 282[39;49;00m[36m[39;49;00m$
   165	[36m#[39;49;00m[36mdefine TYPE_NAME 283[39;49;00m[36m[39;49;00m$
   166	[36m#[39;49;00m[36mdefine TYPEDEF 284[39;49;00m[36m[39;49;00m$
   167	[36m#[39;49;00m[36mdefine EXTERN 285[39;49;00m[36m[39;49;00m$
   168	[36m#[39;49;00m[36mdefine STATIC 286[39;49;00m[36m[39;49;00m$
   169	[36m#[39;49;00m[36mdefine AUTO 287[39;49;00m[36m[39;49;00m$
   170	[36m#[39;49;00m[36mdefine REGISTER 288[39;49;00m[36m[39;49;00m$
   171	[36m#[39;49;00m[36mdefine CHAR 289[39;49;00m[36m[39;49;00m$
   172	[36m#[39;49;00m[36mdefine SHORT 290[39;49;00m[36m[39;49;00m$
   173	[36m#[39;49;00m[36mdefine INT 291[39;49;00m[36m[39;49;00m$
   174	[36m#[39;49;00m[36mdefine UINT 292[39;49;00m[36m[39;49;00m$
   175	[36m#[39;49;00m[36mdefine INT64 293[39;49;00m[36m[39;49;00m$
   176	[36m#[39;49;00m[36mdefine LONG 294[39;49;00m[36m[39;49;00m$
   177	[36m#[39;49;00m[36mdefine SIGNED 295[39;49;00m[36m[39;49;00m$
   178	[36m#[39;49;00m[36mdefine UNSIGNED 296[39;49;00m[36m[39;49;00m$
   179	[36m#[39;49;00m[36mdefine FLOAT 297[39;49;00m[36m[39;49;00m$
   180	[36m#[39;49;00m[36mdefine DOUBLE 298[39;49;00m[36m[39;49;00m$
   181	[36m#[39;49;00m[36mdefine CONST 299[39;49;00m[36m[39;49;00m$
   182	[36m#[39;49;00m[36mdefine VOLATILE 300[39;49;00m[36m[39;49;00m$
   183	[36m#[39;49;00m[36mdefine VOID 301[39;49;00m[36m[39;49;00m$
   184	[36m#[39;49;00m[36mdefine VALIST 302[39;49;00m[36m[39;49;00m$
   185	[36m#[39;49;00m[36mdefine STRUCT 303[39;49;00m[36m[39;49;00m$
   186	[36m#[39;49;00m[36mdefine UNION 304[39;49;00m[36m[39;49;00m$
   187	[36m#[39;49;00m[36mdefine ENUM 305[39;49;00m[36m[39;49;00m$
   188	[36m#[39;49;00m[36mdefine ELLIPSIS 306[39;49;00m[36m[39;49;00m$
   189	[36m#[39;49;00m[36mdefine CASE 307[39;49;00m[36m[39;49;00m$
   190	[36m#[39;49;00m[36mdefine DEFAULT 308[39;49;00m[36m[39;49;00m$
   191	[36m#[39;49;00m[36mdefine IF 309[39;49;00m[36m[39;49;00m$
   192	[36m#[39;49;00m[36mdefine SWITCH 310[39;49;00m[36m[39;49;00m$
   193	[36m#[39;49;00m[36mdefine WHILE 311[39;49;00m[36m[39;49;00m$
   194	[36m#[39;49;00m[36mdefine DO 312[39;49;00m[36m[39;49;00m$
   195	[36m#[39;49;00m[36mdefine FOR 313[39;49;00m[36m[39;49;00m$
   196	[36m#[39;49;00m[36mdefine GOTO 314[39;49;00m[36m[39;49;00m$
   197	[36m#[39;49;00m[36mdefine CONTINUE 315[39;49;00m[36m[39;49;00m$
   198	[36m#[39;49;00m[36mdefine BREAK 316[39;49;00m[36m[39;49;00m$
   199	[36m#[39;49;00m[36mdefine RETURN 317[39;49;00m[36m[39;49;00m$
   200	[36m#[39;49;00m[36mdefine IFX 318[39;49;00m[36m[39;49;00m$
   201	[36m#[39;49;00m[36mdefine ELSE 319[39;49;00m[36m[39;49;00m$
   202	[36m#[39;49;00m[36mdefine CLASS 320[39;49;00m[36m[39;49;00m$
   203	[36m#[39;49;00m[36mdefine THISCLASS 321[39;49;00m[36m[39;49;00m$
   204	[36m#[39;49;00m[36mdefine CLASS_NAME 322[39;49;00m[36m[39;49;00m$
   205	[36m#[39;49;00m[36mdefine PROPERTY 323[39;49;00m[36m[39;49;00m$
   206	[36m#[39;49;00m[36mdefine SETPROP 324[39;49;00m[36m[39;49;00m$
   207	[36m#[39;49;00m[36mdefine GETPROP 325[39;49;00m[36m[39;49;00m$
   208	[36m#[39;49;00m[36mdefine NEWOP 326[39;49;00m[36m[39;49;00m$
   209	[36m#[39;49;00m[36mdefine RENEW 327[39;49;00m[36m[39;49;00m$
   210	[36m#[39;49;00m[36mdefine DELETE 328[39;49;00m[36m[39;49;00m$
   211	[36m#[39;49;00m[36mdefine EXT_DECL 329[39;49;00m[36m[39;49;00m$
   212	[36m#[39;49;00m[36mdefine EXT_STORAGE 330[39;49;00m[36m[39;49;00m$
   213	[36m#[39;49;00m[36mdefine IMPORT 331[39;49;00m[36m[39;49;00m$
   214	[36m#[39;49;00m[36mdefine DEFINE 332[39;49;00m[36m[39;49;00m$
   215	[36m#[39;49;00m[36mdefine VIRTUAL 333[39;49;00m[36m[39;49;00m$
   216	[36m#[39;49;00m[36mdefine EXT_ATTRIB 334[39;49;00m[36m[39;49;00m$
   217	[36m#[39;49;00m[36mdefine PUBLIC 335[39;49;00m[36m[39;49;00m$
   218	[36m#[39;49;00m[36mdefine PRIVATE 336[39;49;00m[36m[39;49;00m$
   219	[36m#[39;49;00m[36mdefine TYPED_OBJECT 337[39;49;00m[36m[39;49;00m$
   220	[36m#[39;49;00m[36mdefine ANY_OBJECT 338[39;49;00m[36m[39;49;00m$
   221	[36m#[39;49;00m[36mdefine _INCREF 339[39;49;00m[36m[39;49;00m$
   222	[36m#[39;49;00m[36mdefine EXTENSION 340[39;49;00m[36m[39;49;00m$
   223	[36m#[39;49;00m[36mdefine ASM 341[39;49;00m[36m[39;49;00m$
   224	[36m#[39;49;00m[36mdefine TYPEOF 342[39;49;00m[36m[39;49;00m$
   225	[36m#[39;49;00m[36mdefine WATCH 343[39;49;00m[36m[39;49;00m$
   226	[36m#[39;49;00m[36mdefine STOPWATCHING 344[39;49;00m[36m[39;49;00m$
   227	[36m#[39;49;00m[36mdefine FIREWATCHERS 345[39;49;00m[36m[39;49;00m$
   228	[36m#[39;49;00m[36mdefine WATCHABLE 346[39;49;00m[36m[39;49;00m$
   229	[36m#[39;49;00m[36mdefine CLASS_DESIGNER 347[39;49;00m[36m[39;49;00m$
   230	[36m#[39;49;00m[36mdefine CLASS_NO_EXPANSION 348[39;49;00m[36m[39;49;00m$
   231	[36m#[39;49;00m[36mdefine CLASS_FIXED 349[39;49;00m[36m[39;49;00m$
   232	[36m#[39;49;00m[36mdefine ISPROPSET 350[39;49;00m[36m[39;49;00m$
   233	[36m#[39;49;00m[36mdefine CLASS_DEFAULT_PROPERTY 351[39;49;00m[36m[39;49;00m$
   234	[36m#[39;49;00m[36mdefine PROPERTY_CATEGORY 352[39;49;00m[36m[39;49;00m$
   235	[36m#[39;49;00m[36mdefine CLASS_DATA 353[39;49;00m[36m[39;49;00m$
   236	[36m#[39;49;00m[36mdefine CLASS_PROPERTY 354[39;49;00m[36m[39;49;00m$
   237	[36m#[39;49;00m[36mdefine SUBCLASS 355[39;49;00m[36m[39;49;00m$
   238	[36m#[39;49;00m[36mdefine NAMESPACE 356[39;49;00m[36m[39;49;00m$
   239	[36m#[39;49;00m[36mdefine NEW0OP 357[39;49;00m[36m[39;49;00m$
   240	[36m#[39;49;00m[36mdefine RENEW0 358[39;49;00m[36m[39;49;00m$
   241	[36m#[39;49;00m[36mdefine VAARG 359[39;49;00m[36m[39;49;00m$
   242	[36m#[39;49;00m[36mdefine DBTABLE 360[39;49;00m[36m[39;49;00m$
   243	[36m#[39;49;00m[36mdefine DBFIELD 361[39;49;00m[36m[39;49;00m$
   244	[36m#[39;49;00m[36mdefine DBINDEX 362[39;49;00m[36m[39;49;00m$
   245	[36m#[39;49;00m[36mdefine DATABASE_OPEN 363[39;49;00m[36m[39;49;00m$
   246	[37m[39;49;00m$
   247	[37m[39;49;00m$
   248	[37m[39;49;00m$
   249	[37m[39;49;00m$
   250	[36m#[39;49;00m[36mif ! defined (YYSTYPE) && ! defined (YYSTYPE_IS_DECLARED)[39;49;00m[36m[39;49;00m$
   251	[36m#[39;49;00m[36mline 42 "grammar.y"[39;49;00m[36m[39;49;00m$
   252	[34mtypedef[39;49;00m[37m [39;49;00m[34munion[39;49;00m[37m [39;49;00m[04m[32mYYSTYPE[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
   253	[37m   [39;49;00mSpecifierType[37m [39;49;00mspecifierType;[37m[39;49;00m$
   254	[37m   [39;49;00m[36mint[39;49;00m[37m [39;49;00mi;[37m[39;49;00m$
   255	[37m   [39;49;00mAccessMode[37m [39;49;00mdeclMode;[37m[39;49;00m$
   256	[37m   [39;49;00mIdentifier[37m [39;49;00mid;[37m[39;49;00m$
   257	[37m   [39;49;00mExpression[37m [39;49;00mexp;[37m[39;49;00m$
   258	[37m   [39;49;00mSpecifier[37m [39;49;00mspecifier;[37m[39;49;00m$
   259	[37m   [39;49;00mOldList[37m [39;49;00m*[37m [39;49;00mlist;[37m[39;49;00m$
   260	[37m   [39;49;00mEnumerator[37m [39;49;00menumerator;[37m[39;49;00m$
   261	[37m   [39;49;00mDeclarator[37m [39;49;00mdeclarator;[37m[39;49;00m$
   262	[37m   [39;49;00mPointer[37m [39;49;00mpointer;[37m[39;49;00m$
   263	[37m   [39;49;00mInitializer[37m [39;49;00minitializer;[37m[39;49;00m$
   264	[37m   [39;49;00mInitDeclarator[37m [39;49;00minitDeclarator;[37m[39;49;00m$
   265	[37m   [39;49;00mTypeName[37m [39;49;00mtypeName;[37m[39;49;00m$
   266	[37m   [39;49;00mDeclaration[37m [39;49;00mdeclaration;[37m[39;49;00m$
   267	[37m   [39;49;00mStatement[37m [39;49;00mstmt;[37m[39;49;00m$
   268	[37m   [39;49;00mFunctionDefinition[37m [39;49;00mfunction;[37m[39;49;00m$
   269	[37m   [39;49;00mExternal[37m [39;49;00mexternal;[37m[39;49;00m$
   270	[37m   [39;49;00mContext[37m [39;49;00mcontext;[37m[39;49;00m$
   271	[37m   [39;49;00mAsmField[37m [39;49;00masmField;[37m[39;49;00m$
   272	[37m[39;49;00m$
   273	[37m   [39;49;00mInstantiation[37m [39;49;00minstance;[37m[39;49;00m$
   274	[37m   [39;49;00mMembersInit[37m [39;49;00mmembersInit;[37m[39;49;00m$
   275	[37m   [39;49;00mMemberInit[37m [39;49;00mmemberInit;[37m[39;49;00m$
   276	[37m   [39;49;00mClassFunction[37m [39;49;00mclassFunction;[37m[39;49;00m$
   277	[37m   [39;49;00mClassDefinition[37m [39;49;00m_class;[37m[39;49;00m$
   278	[37m   [39;49;00mClassDef[37m [39;49;00mclassDef;[37m[39;49;00m$
   279	[37m   [39;49;00mPropertyDef[37m [39;49;00mprop;[37m[39;49;00m$
   280	[37m   [39;49;00m[36mchar[39;49;00m[37m [39;49;00m*[37m [39;49;00mstring;[37m[39;49;00m$
   281	[37m   [39;49;00mSymbol[37m [39;49;00msymbol;[37m[39;49;00m$
   282	[37m   [39;49;00mPropertyWatch[37m [39;49;00mpropertyWatch;[37m[39;49;00m$
   283	[37m   [39;49;00mTemplateParameter[37m [39;49;00mtemplateParameter;[37m[39;49;00m$
   284	[37m   [39;49;00mTemplateArgument[37m [39;49;00mtemplateArgument;[37m[39;49;00m$
   285	[37m   [39;49;00mTemplateDatatype[37m [39;49;00mtemplateDatatype;[37m[39;49;00m$
   286	[37m   [39;49;00m[37m[39;49;00m$
   287	[37m   [39;49;00mDBTableEntry[37m [39;49;00mdbtableEntry;[37m[39;49;00m$
   288	[37m   [39;49;00mDBIndexItem[37m [39;49;00mdbindexItem;[37m[39;49;00m$
   289	[37m   [39;49;00mDBTableDef[37m [39;49;00mdbtableDef;[37m[39;49;00m$
   290	}[37m [39;49;00mYYSTYPE;[37m[39;49;00m$
   291	[37m/* Line 1318 of yacc.c.  */[39;49;00m[37m[39;49;00m$
   292	[36m#[39;49;00m[36mline 293 "grammar.eh"[39;49;00m[36m[39;49;00m$
   293	[36m#[39;49;00m[36m define yystype YYSTYPE [39;49;00m[37m/* obsolescent; will be withdrawn */[39;49;00m[36m[39;49;00m$
   294	[36m#[39;49;00m[36m define YYSTYPE_IS_DECLARED 1[39;49;00m[36m[39;49;00m$
   295	[36m#[39;49;00m[36m define YYSTYPE_IS_TRIVIAL 1[39;49;00m[36m[39;49;00m$
   296	[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   297	[37m[39;49;00m$
   298	[34mextern[39;49;00m[37m [39;49;00mYYSTYPE[37m [39;49;00myylval;[37m[39;49;00m$
   299	[37m[39;49;00m$
   300	[36m#[39;49;00m[36mif ! defined (YYLTYPE) && ! defined (YYLTYPE_IS_DECLARED)[39;49;00m[36m[39;49;00m$
   301	[34mtypedef[39;49;00m[37m [39;49;00m[34mstruct[39;49;00m[37m [39;49;00m[04m[32mYYLTYPE[39;49;00m[37m[39;49;00m$
   302	{[37m[39;49;00m$
   303	[37m  [39;49;00m[36mint[39;49;00m[37m [39;49;00mfirst_line;[37m[39;49;00m$
   304	[37m  [39;49;00m[36mint[39;49;00m[37m [39;49;00mfirst_column;[37m[39;49;00m$
   305	[37m  [39;49;00m[36mint[39;49;00m[37m [39;49;00mlast_line;[37m[39;49;00m$
   306	[37m  [39;49;00m[36mint[39;49;00m[37m [39;49;00mlast_column;[37m[39;49;00m$
   307	}[37m [39;49;00mYYLTYPE;[37m[39;49;00m$
   308	[36m#[39;49;00m[36m define yyltype YYLTYPE [39;49;00m[37m/* obsolescent; will be withdrawn */[39;49;00m[36m[39;49;00m$
   309	[36m#[39;49;00m[36m define YYLTYPE_IS_DECLARED 1[39;49;00m[36m[39;49;00m$
   310	[36m#[39;49;00m[36m define YYLTYPE_IS_TRIVIAL 1[39;49;00m[36m[39;49;00m$
   311	[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   312	[37m[39;49;00m$
   313	[34mextern[39;49;00m[37m [39;49;00mYYLTYPE[37m [39;49;00myylloc;$

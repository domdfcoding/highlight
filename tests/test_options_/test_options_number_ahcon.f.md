     1	      [37m  [39;49;00m[34mSUBROUTINE [39;49;00mAHCON[37m [39;49;00m(SIZE,N,M,A,B,OLEVR,OLEVI,CLEVR,CLEVI,[37m         [39;49;00m[37mTRUNCATED[39;49;00m[37m[39;49;00m
     2	     &[37m                    [39;49;00mSCR1,SCR2,IPVT,JPVT,CON,WORK,ISEED,IERR)[37m [39;49;00m[37m!Test[39;49;00m[37m inline comment[39;49;00m[37m[39;49;00m
     3	[37mC[39;49;00m
     4	[37mC       FUNCTION:[39;49;00m
     5	[37mCF[39;49;00m
     6	[37mCF      Determines whether the pair (A,B) is controllable and flags[39;49;00m
     7	[37mCF      the eigenvalues corresponding to uncontrollable modes.[39;49;00m
     8	[37mCF      this ad-hoc controllability calculation uses a random matrix F[39;49;00m
     9	[37mCF      and computes whether eigenvalues move from A to the controlled[39;49;00m
    10	[37mCF      system A+B*F.[39;49;00m
    11	[37mCF[39;49;00m
    12	[37mC       USAGE:[39;49;00m
    13	[37mCU[39;49;00m
    14	[37mCU      CALL AHCON (SIZE,N,M,A,B,OLEVR,OLEVI,CLEVR,CLEVI,SCR1,SCR2,IPVT,[39;49;00m
    15	[37mCU                  JPVT,CON,WORK,ISEED,IERR)[39;49;00m
    16	[37mCU[39;49;00m
    17	[37mCU      since AHCON generates different random F matrices for each[39;49;00m
    18	[37mCU      call, as long as iseed is not re-initialized by the main[39;49;00m
    19	[37mCU      program, and since this code has the potential to be fooled[39;49;00m
    20	[37mCU      by extremely ill-conditioned problems, the cautious user[39;49;00m
    21	[37mCU      may wish to call it multiple times and rely, perhaps, on[39;49;00m
    22	[37mCU      a 2-of-3 vote.  We believe, but have not proved, that any[39;49;00m
    23	[37mCU      errors this routine may produce are conservative--i.e., that[39;49;00m
    24	[37mCU      it may flag a controllable mode as uncontrollable, but[39;49;00m
    25	[37mCU      not vice-versa.[39;49;00m
    26	[37mCU[39;49;00m
    27	[37mC       INPUTS:[39;49;00m
    28	[37mCI[39;49;00m
    29	[37mCI      SIZE    integer - first dimension of all 2-d arrays.[39;49;00m
    30	[37mCI[39;49;00m
    31	[37mCI      N       integer - number of states.[39;49;00m
    32	[37mCI[39;49;00m
    33	[37mCI      M       integer - number of inputs.[39;49;00m
    34	[37mCI[39;49;00m
    35	[37mCI      A       double precision - SIZE by N array containing the[39;49;00m
    36	[37mCI              N by N system dynamics matrix A.[39;49;00m
    37	[37mCI[39;49;00m
    38	[37mCI      B       double precision - SIZE by M array containing the[39;49;00m
    39	[37mCI              N by M system input matrix B.[39;49;00m
    40	[37mCI[39;49;00m
    41	[37mCI      ISEED   initial seed for random number generator; if ISEED=0,[39;49;00m
    42	[37mCI              then AHCON will set ISEED to a legal value.[39;49;00m
    43	[37mCI[39;49;00m
    44	[37mC       OUTPUTS:[39;49;00m
    45	[37mCO[39;49;00m
    46	[37mCO      OLEVR   double precision - N dimensional vector containing the[39;49;00m
    47	[37mCO              real parts of the eigenvalues of A.[39;49;00m
    48	[37mCO[39;49;00m
    49	[37mCO      OLEVI   double precision - N dimensional vector containing the[39;49;00m
    50	[37mCO              imaginary parts of the eigenvalues of A.[39;49;00m
    51	[37mCO[39;49;00m
    52	[37mCO      CLEVR   double precision - N dimensional vector work space[39;49;00m
    53	[37mCO              containing the real parts of the eigenvalues of A+B*F,[39;49;00m
    54	[37mCO              where F is the random matrix.[39;49;00m
    55	[37mCO[39;49;00m
    56	[37mCO      CLEVI   double precision - N dimensional vector work space[39;49;00m
    57	[37mCO              containing the imaginary parts of the eigenvalues of[39;49;00m
    58	[37mCO              A+B*F, where F is the random matrix.[39;49;00m
    59	[37mCO[39;49;00m
    60	[37mCO      SCR1    double precision - N dimensional vector containing the[39;49;00m
    61	[37mCO              magnitudes of the corresponding eigenvalues of A.[39;49;00m
    62	[37mCO[39;49;00m
    63	[37mCO      SCR2    double precision - N dimensional vector containing the[39;49;00m
    64	[37mCO              damping factors of the corresponding eigenvalues of A.[39;49;00m
    65	[37mCO[39;49;00m
    66	[37mCO      IPVT    integer - N dimensional vector; contains the row pivots[39;49;00m
    67	[37mCO              used in finding the nearest neighbor eigenvalues between[39;49;00m
    68	[37mCO              those of A and of A+B*F.  The IPVT(1)th eigenvalue of[39;49;00m
    69	[37mCO              A and the JPVT(1)th eigenvalue of A+B*F are the closest[39;49;00m
    70	[37mCO              pair.[39;49;00m
    71	[37mCO[39;49;00m
    72	[37mCO      JPVT    integer - N dimensional vector; contains the column[39;49;00m
    73	[37mCO              pivots used in finding the nearest neighbor eigenvalues;[39;49;00m
    74	[37mCO              see IPVT.[39;49;00m
    75	[37mCO[39;49;00m
    76	[37mCO      CON     logical - N dimensional vector; flagging the uncontrollable[39;49;00m
    77	[37mCO              modes of the system.  CON(I)=.TRUE. implies the[39;49;00m
    78	[37mCO              eigenvalue of A given by DCMPLX(OLEVR(IPVT(I)),OLEVI(IPVT(i)))[39;49;00m
    79	[37mCO              corresponds to a controllable mode; CON(I)=.FALSE.[39;49;00m
    80	[37mCO              implies an uncontrollable mode for that eigenvalue.[39;49;00m
    81	[37mCO[39;49;00m
    82	[37mCO      WORK    double precision - SIZE by N dimensional array containing[39;49;00m
    83	[37mCO              an N by N matrix.  WORK(I,J) is the distance between[39;49;00m
    84	[37mCO              the open loop eigenvalue given by DCMPLX(OLEVR(I),OLEVI(I))[39;49;00m
    85	[37mCO              and the closed loop eigenvalue of A+B*F given by[39;49;00m
    86	[37mCO              DCMPLX(CLEVR(J),CLEVI(J)).[39;49;00m
    87	[37mCO[39;49;00m
    88	[37mCO      IERR    integer - IERR=0 indicates normal return; a non-zero[39;49;00m
    89	[37mCO              value indicates trouble in the eigenvalue calculation.[39;49;00m
    90	[37mCO              see the EISPACK and EIGEN documentation for details.[39;49;00m
    91	[37mCO[39;49;00m
    92	[37mC       ALGORITHM:[39;49;00m
    93	[37mCA[39;49;00m
    94	[37mCA      Calculate eigenvalues of A and of A+B*F for a randomly[39;49;00m
    95	[37mCA      generated F, and see which ones change.  Use a full pivot[39;49;00m
    96	[37mCA      search through a matrix of euclidean distance measures[39;49;00m
    97	[37mCA      between each pair of eigenvalues from (A,A+BF) to[39;49;00m
    98	[37mCA      determine the closest pairs.[39;49;00m
    99	[37mCA[39;49;00m
   100	[37mC       MACHINE DEPENDENCIES:[39;49;00m
   101	[37mCM[39;49;00m
   102	[37mCM       NONE[39;49;00m
   103	[37mCM[39;49;00m
   104	[37mC       HISTORY:[39;49;00m
   105	[37mCH[39;49;00m
   106	[37mCH      written by:             Birdwell & Laub[39;49;00m
   107	[37mCH      date:                   May 18, 1985[39;49;00m
   108	[37mCH      current version:        1.0[39;49;00m
   109	[37mCH      modifications:          made machine independent and modified for[39;49;00m
   110	[37mCH                              f77:bb:8-86.[39;49;00m
   111	[37mCH                              changed cmplx -> dcmplx: 7/27/88 jdb[39;49;00m
   112	[37mCH[39;49;00m
   113	[37mC       ROUTINES CALLED:[39;49;00m
   114	[37mCC[39;49;00m
   115	[37mCC      EIGEN,RAND[39;49;00m
   116	[37mCC[39;49;00m
   117	[37mC       COMMON MEMORY USED:[39;49;00m
   118	[37mCM[39;49;00m
   119	[37mCM      none[39;49;00m
   120	[37mCM[39;49;00m
   121	[37mC----------------------------------------------------------------------[39;49;00m
   122	[37mC       written for:    The CASCADE Project[39;49;00m
   123	[37mC                       Oak Ridge National Laboratory[39;49;00m
   124	[37mC                       U.S. Department of Energy[39;49;00m
   125	[37mC                       contract number DE-AC05-840R21400[39;49;00m
   126	[37mC                       subcontract number 37B-7685 S13[39;49;00m
   127	[37mC                       organization:   The University of Tennessee[39;49;00m
   128	[37mC----------------------------------------------------------------------[39;49;00m
   129	[37mC       THIS SOFTWARE IS IN THE PUBLIC DOMAIN[39;49;00m
   130	[37mC       NO RESTRICTIONS ON ITS USE ARE IMPLIED[39;49;00m
   131	[37mC----------------------------------------------------------------------[39;49;00m
   132	[37mC[39;49;00m
   133	[37mC--global variables:[39;49;00m
   134	[37mC[39;49;00m
   135	      [37m  [39;49;00m[36mINTEGER         [39;49;00mSIZE[37m[39;49;00m
   136	      [37m  [39;49;00m[36mINTEGER         [39;49;00mN[37m[39;49;00m
   137	      [37m  [39;49;00m[36mINTEGER         [39;49;00mM[37m[39;49;00m
   138	      [37m  [39;49;00m[36mINTEGER         [39;49;00mIPVT([34m1[39;49;00m)[37m[39;49;00m
   139	      [37m  [39;49;00m[36mINTEGER         [39;49;00mJPVT([34m1[39;49;00m)[37m[39;49;00m
   140	      [37m  [39;49;00m[36mINTEGER         [39;49;00mIERR[37m[39;49;00m
   141	[37mC[39;49;00m
   142	      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mA(SIZE,N)[37m[39;49;00m
   143	      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mB(SIZE,M)[37m[39;49;00m
   144	      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mWORK(SIZE,N)[37m[39;49;00m
   145	      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mCLEVR(N)[37m[39;49;00m
   146	      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mCLEVI(N)[37m[39;49;00m
   147	      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mOLEVR(N)[37m[39;49;00m
   148	      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mOLEVI(N)[37m[39;49;00m
   149	      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mSCR1(N)[37m[39;49;00m
   150	      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mSCR2(N)[37m[39;49;00m
   151	[37mC[39;49;00m
   152	      [37m  [39;49;00m[36mLOGICAL                 [39;49;00mCON(N)[37m[39;49;00m
   153	[37mC[39;49;00m
   154	[37mC--local variables:[39;49;00m
   155	[37mC[39;49;00m
   156	      [37m  [39;49;00m[36mINTEGER         [39;49;00mISEED[37m[39;49;00m
   157	      [37m  [39;49;00m[36mINTEGER         [39;49;00mITEMP[37m[39;49;00m
   158	      [37m  [39;49;00m[36mINTEGER         [39;49;00mK1[37m[39;49;00m
   159	      [37m  [39;49;00m[36mINTEGER         [39;49;00mK2[37m[39;49;00m
   160	      [37m  [39;49;00m[36mINTEGER         [39;49;00mI[37m[39;49;00m
   161	      [37m  [39;49;00m[36mINTEGER         [39;49;00mJ[37m[39;49;00m
   162	      [37m  [39;49;00m[36mINTEGER         [39;49;00mK[37m[39;49;00m
   163	      [37m  [39;49;00m[36mINTEGER         [39;49;00mIMAX[37m[39;49;00m
   164	      [37m  [39;49;00m[36mINTEGER         [39;49;00mJMAX[37m[39;49;00m
   165	[37mC[39;49;00m
   166	      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00m[34mVALUE[39;49;00m[37m[39;49;00m
   167	      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mEPS[37m[39;49;00m
   168	      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mEPS1[37m[39;49;00m
   169	      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mTEMP[37m[39;49;00m
   170	      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mCURR[37m[39;49;00m
   171	      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mANORM[37m[39;49;00m
   172	      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mBNORM[37m[39;49;00m
   173	      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mCOLNRM[37m[39;49;00m
   174	      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mRNDMNO[37m[39;49;00m
   175	[37mC[39;49;00m
   176	      [37m  [39;49;00m[36mDOUBLE COMPLEX		[39;49;00mDCMPLX[37m[39;49;00m
   177	[37mC[39;49;00m
   178	[37mC--compute machine epsilon[39;49;00m
   179	[37mC[39;49;00m
   180	      [37m  [39;49;00mEPS[37m [39;49;00m=[37m [39;49;00m[34m1.D0[39;49;00m[37m[39;49;00m
   181	100   [37m  [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m
   182	      [37m    [39;49;00mEPS[37m [39;49;00m=[37m [39;49;00mEPS[37m [39;49;00m/[37m [39;49;00m[34m2.D0[39;49;00m[37m[39;49;00m
   183	      [37m    [39;49;00mEPS1[37m [39;49;00m=[37m [39;49;00m[34m1.D0[39;49;00m[37m [39;49;00m+[37m [39;49;00mEPS[37m[39;49;00m
   184	      [37m  [39;49;00m[34mIF[39;49;00m[37m [39;49;00m(EPS1[37m [39;49;00m.NE.[37m [39;49;00m[34m1.D0[39;49;00m)[37m [39;49;00m[34mGO[39;49;00m[37m [39;49;00m[34mTO[39;49;00m[37m [39;49;00m[34m100[39;49;00m[37m[39;49;00m
   185	      [37m  [39;49;00mEPS[37m [39;49;00m=[37m [39;49;00mEPS[37m [39;49;00m*[37m [39;49;00m[34m2.D0[39;49;00m[37m[39;49;00m
   186	[37mC[39;49;00m
   187	[37mC--compute the l-1 norm of a[39;49;00m
   188	[37mC[39;49;00m
   189	      [37m  [39;49;00mANORM[37m [39;49;00m=[37m [39;49;00m[34m0.0D0[39;49;00m[37m[39;49;00m
   190	      [37m  [39;49;00m[34mDO [39;49;00m[34m120[39;49;00m[37m [39;49;00mJ[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00mN[37m[39;49;00m
   191	      [37m    [39;49;00mCOLNRM[37m [39;49;00m=[37m [39;49;00m[34m0.D0[39;49;00m[37m[39;49;00m
   192	      [37m    [39;49;00m[34mDO [39;49;00m[34m110[39;49;00m[37m [39;49;00mI[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00mN[37m[39;49;00m
   193	      [37m      [39;49;00mCOLNRM[37m [39;49;00m=[37m [39;49;00mCOLNRM[37m [39;49;00m+[37m [39;49;00m[36mABS[39;49;00m(A(I,J))[37m[39;49;00m
   194	110   [37m    [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m
   195	      [37m    [39;49;00m[34mIF[39;49;00m[37m [39;49;00m(COLNRM[37m [39;49;00m.GT.[37m [39;49;00mANORM)[37m [39;49;00mANORM[37m [39;49;00m=[37m [39;49;00mCOLNRM[37m[39;49;00m
   196	120   [37m  [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m
   197	[37mC[39;49;00m
   198	[37mC--compute the l-1 norm of b[39;49;00m
   199	[37mC[39;49;00m
   200	      [37m  [39;49;00mBNORM[37m [39;49;00m=[37m [39;49;00m[34m0.0D0[39;49;00m[37m[39;49;00m
   201	      [37m  [39;49;00m[34mDO [39;49;00m[34m140[39;49;00m[37m [39;49;00mJ[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00mM[37m[39;49;00m
   202	      [37m    [39;49;00mCOLNRM[37m [39;49;00m=[37m [39;49;00m[34m0.D0[39;49;00m[37m[39;49;00m
   203	      [37m    [39;49;00m[34mDO [39;49;00m[34m130[39;49;00m[37m [39;49;00mI[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00mN[37m[39;49;00m
   204	      [37m      [39;49;00mCOLNRM[37m [39;49;00m=[37m [39;49;00mCOLNRM[37m [39;49;00m+[37m [39;49;00m[36mABS[39;49;00m(B(I,J))[37m[39;49;00m
   205	130   [37m    [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m
   206	      [37m    [39;49;00m[34mIF[39;49;00m[37m [39;49;00m(COLNRM[37m [39;49;00m.GT.[37m [39;49;00mBNORM)[37m [39;49;00mBNORM[37m [39;49;00m=[37m [39;49;00mCOLNRM[37m[39;49;00m
   207	140   [37m  [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m
   208	[37mC[39;49;00m
   209	[37mC--compute a + b * f[39;49;00m
   210	[37mC[39;49;00m
   211	      [37m  [39;49;00m[34mDO [39;49;00m[34m160[39;49;00m[37m [39;49;00mJ[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00mN[37m[39;49;00m
   212	      [37m    [39;49;00m[34mDO [39;49;00m[34m150[39;49;00m[37m [39;49;00mI[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00mN[37m[39;49;00m
   213	      [37m      [39;49;00mWORK(I,J)[37m [39;49;00m=[37m [39;49;00mA(I,J)[37m[39;49;00m
   214	150   [37m    [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m
   215	160   [37m  [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m
   216	[37mC[39;49;00m
   217	[37mC--the elements of f are random with uniform distribution[39;49;00m
   218	[37mC--from -anorm/bnorm to +anorm/bnorm[39;49;00m
   219	[37mC--note that f is not explicitly stored as a matrix[39;49;00m
   220	[37mC--pathalogical floating point notes:  the if (bnorm .gt. 0.d0)[39;49;00m
   221	[37mC--test should actually be if (bnorm .gt. dsmall), where dsmall[39;49;00m
   222	[37mC--is the smallest representable number whose reciprocal does[39;49;00m
   223	[37mC--not generate an overflow or loss of precision.[39;49;00m
   224	[37mC[39;49;00m
   225	      [37m  [39;49;00m[34mIF[39;49;00m[37m [39;49;00m(ISEED[37m [39;49;00m.EQ.[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00mISEED[37m [39;49;00m=[37m [39;49;00m[34m86345823[39;49;00m[37m[39;49;00m
   226	      [37m  [39;49;00m[34mIF[39;49;00m[37m [39;49;00m(ANORM[37m [39;49;00m.EQ.[37m [39;49;00m[34m0.D0[39;49;00m)[37m [39;49;00mANORM[37m [39;49;00m=[37m [39;49;00m[34m1.D0[39;49;00m[37m[39;49;00m
   227	      [37m  [39;49;00m[34mIF[39;49;00m[37m [39;49;00m(BNORM[37m [39;49;00m.GT.[37m [39;49;00m[34m0.D0[39;49;00m)[37m [39;49;00m[34mTHEN[39;49;00m[37m[39;49;00m
   228	      [37m    [39;49;00mTEMP[37m [39;49;00m=[37m [39;49;00m[34m2.D0[39;49;00m[37m [39;49;00m*[37m [39;49;00mANORM[37m [39;49;00m/[37m [39;49;00mBNORM[37m[39;49;00m
   229	      [37m  [39;49;00m[34mELSE[39;49;00m[37m[39;49;00m
   230	      [37m    [39;49;00mTEMP[37m [39;49;00m=[37m [39;49;00m[34m2.D0[39;49;00m[37m[39;49;00m
   231	      [37m  [39;49;00m[34mEND [39;49;00m[34mIF[39;49;00m[37m[39;49;00m
   232	      [37m  [39;49;00m[34mDO [39;49;00m[34m190[39;49;00m[37m [39;49;00mK[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00mM[37m[39;49;00m
   233	      [37m    [39;49;00m[34mDO [39;49;00m[34m180[39;49;00m[37m [39;49;00mJ[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00mN[37m[39;49;00m
   234	      [37m      [39;49;00m[34mCALL [39;49;00m[36mRAND[39;49;00m(ISEED,ISEED,RNDMNO)[37m[39;49;00m
   235	      [37m      [39;49;00m[34mVALUE[39;49;00m[37m [39;49;00m=[37m [39;49;00m(RNDMNO[37m [39;49;00m-[37m [39;49;00m[34m0.5D0[39;49;00m)[37m [39;49;00m*[37m [39;49;00mTEMP[37m[39;49;00m
   236	      [37m      [39;49;00m[34mDO [39;49;00m[34m170[39;49;00m[37m [39;49;00mI[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00mN[37m[39;49;00m
   237	      [37m        [39;49;00mWORK(I,J)[37m [39;49;00m=[37m [39;49;00mWORK(I,J)[37m [39;49;00m+[37m [39;49;00mB(I,K)*[34mVALUE[39;49;00m[37m[39;49;00m
   238	170   [37m      [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m
   239	180   [37m    [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m
   240	190   [37m  [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m
   241	[37mC[39;49;00m
   242	[37mC--compute the eigenvalues of a + b*f, and several other things[39;49;00m
   243	[37mC[39;49;00m
   244	      [37m  [39;49;00m[34mCALL [39;49;00mEIGEN[37m [39;49;00m([34m0[39;49;00m,SIZE,N,WORK,CLEVR,CLEVI,WORK,SCR1,SCR2,IERR)[37m[39;49;00m
   245	      [37m  [39;49;00m[34mIF[39;49;00m[37m [39;49;00m(IERR[37m [39;49;00m.NE.[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mRETURN[39;49;00m[37m[39;49;00m
   246	[37mC[39;49;00m
   247	[37mC--copy a so it is not destroyed[39;49;00m
   248	[37mC[39;49;00m
   249	      [37m  [39;49;00m[34mDO [39;49;00m[34m210[39;49;00m[37m [39;49;00mJ[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00mN[37m[39;49;00m
   250	      [37m    [39;49;00m[34mDO [39;49;00m[34m200[39;49;00m[37m [39;49;00mI[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00mN[37m[39;49;00m
   251	      [37m      [39;49;00mWORK(I,J)[37m [39;49;00m=[37m [39;49;00mA(I,J)[37m[39;49;00m
   252	200   [37m    [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m
   253	210   [37m  [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m
   254	[37mC[39;49;00m
   255	[37mC--compute the eigenvalues of a, and several other things[39;49;00m
   256	[37mC[39;49;00m
   257	      [37m  [39;49;00m[34mCALL [39;49;00mEIGEN[37m [39;49;00m([34m0[39;49;00m,SIZE,N,WORK,OLEVR,OLEVI,WORK,SCR1,SCR2,IERR)[37m[39;49;00m
   258	      [37m  [39;49;00m[34mIF[39;49;00m[37m [39;49;00m(IERR[37m [39;49;00m.NE.[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mRETURN[39;49;00m[37m[39;49;00m
   259	[37mC[39;49;00m
   260	[37mC--form the matrix of distances between eigenvalues of a and[39;49;00m
   261	[37mC--EIGENVALUES OF A+B*F[39;49;00m
   262	[37mC[39;49;00m
   263	      [37m  [39;49;00m[34mDO [39;49;00m[34m230[39;49;00m[37m [39;49;00mJ[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00mN[37m[39;49;00m
   264	      [37m    [39;49;00m[34mDO [39;49;00m[34m220[39;49;00m[37m [39;49;00mI[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00mN[37m[39;49;00m
   265	      [37m      [39;49;00mWORK(I,J)[37m [39;49;00m=[37m[39;49;00m
   266	     &[37m        [39;49;00m[36mABS[39;49;00m(DCMPLX(OLEVR(I),OLEVI(I))-DCMPLX(CLEVR(J),CLEVI(J)))[37m[39;49;00m
   267	220   [37m    [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m
   268	230   [37m  [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m
   269	[37mC[39;49;00m
   270	[37mC--initialize row and column pivots[39;49;00m
   271	[37mC[39;49;00m
   272	      [37m  [39;49;00m[34mDO [39;49;00m[34m240[39;49;00m[37m [39;49;00mI[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00mN[37m[39;49;00m
   273	      [37m    [39;49;00mIPVT(I)[37m [39;49;00m=[37m [39;49;00mI[37m[39;49;00m
   274	      [37m    [39;49;00mJPVT(I)[37m [39;49;00m=[37m [39;49;00mI[37m[39;49;00m
   275	240   [37m  [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m
   276	[37mC[39;49;00m
   277	[37mC--a little bit messy to avoid swapping columns and[39;49;00m
   278	[37mC--rows of work[39;49;00m
   279	[37mC[39;49;00m
   280	      [37m  [39;49;00m[34mDO [39;49;00m[34m270[39;49;00m[37m [39;49;00mI[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00mN-[34m1[39;49;00m[37m[39;49;00m
   281	[37mC[39;49;00m
   282	[37mC--find the minimum element of each lower right square[39;49;00m
   283	[37mC--submatrix of work, for submatrices of size n x n[39;49;00m
   284	[37mC--through 2 x 2[39;49;00m
   285	[37mC[39;49;00m
   286	      [37m    [39;49;00mCURR[37m [39;49;00m=[37m [39;49;00mWORK(IPVT(I),JPVT(I))[37m[39;49;00m
   287	      [37m    [39;49;00mIMAX[37m [39;49;00m=[37m [39;49;00mI[37m[39;49;00m
   288	      [37m    [39;49;00mJMAX[37m [39;49;00m=[37m [39;49;00mI[37m[39;49;00m
   289	      [37m    [39;49;00mTEMP[37m [39;49;00m=[37m [39;49;00mCURR[37m[39;49;00m
   290	[37mC[39;49;00m
   291	[37mC--find the minimum element[39;49;00m
   292	[37mC[39;49;00m
   293	      [37m    [39;49;00m[34mDO [39;49;00m[34m260[39;49;00m[37m [39;49;00mK1[37m [39;49;00m=[37m [39;49;00mI,[37m [39;49;00mN[37m[39;49;00m
   294	      [37m      [39;49;00m[34mDO [39;49;00m[34m250[39;49;00m[37m [39;49;00mK2[37m [39;49;00m=[37m [39;49;00mI,[37m [39;49;00mN[37m[39;49;00m
   295	      [37m        [39;49;00m[34mIF[39;49;00m[37m [39;49;00m(WORK(IPVT(K1),JPVT(K2))[37m [39;49;00m.LT.[37m [39;49;00mTEMP)[37m [39;49;00m[34mTHEN[39;49;00m[37m[39;49;00m
   296	      [37m          [39;49;00mTEMP[37m [39;49;00m=[37m [39;49;00mWORK(IPVT(K1),JPVT(K2))[37m[39;49;00m
   297	      [37m          [39;49;00mIMAX[37m [39;49;00m=[37m [39;49;00mK1[37m[39;49;00m
   298	      [37m          [39;49;00mJMAX[37m [39;49;00m=[37m [39;49;00mK2[37m[39;49;00m
   299	      [37m        [39;49;00m[34mEND [39;49;00m[34mIF[39;49;00m[37m[39;49;00m
   300	250   [37m      [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m
   301	260   [37m    [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m
   302	[37mC[39;49;00m
   303	[37mC--update row and column pivots for indirect addressing of work[39;49;00m
   304	[37mC[39;49;00m
   305	      [37m    [39;49;00mITEMP[37m [39;49;00m=[37m [39;49;00mIPVT(I)[37m[39;49;00m
   306	      [37m    [39;49;00mIPVT(I)[37m [39;49;00m=[37m [39;49;00mIPVT(IMAX)[37m[39;49;00m
   307	      [37m    [39;49;00mIPVT(IMAX)[37m [39;49;00m=[37m [39;49;00mITEMP[37m[39;49;00m
   308	[37mC[39;49;00m
   309	      [37m    [39;49;00mITEMP[37m [39;49;00m=[37m [39;49;00mJPVT(I)[37m[39;49;00m
   310	      [37m    [39;49;00mJPVT(I)[37m [39;49;00m=[37m [39;49;00mJPVT(JMAX)[37m[39;49;00m
   311	      [37m    [39;49;00mJPVT(JMAX)[37m [39;49;00m=[37m [39;49;00mITEMP[37m[39;49;00m
   312	[37mC[39;49;00m
   313	[37mC--do next submatrix[39;49;00m
   314	[37mC[39;49;00m
   315	270   [37m  [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m
   316	[37mC[39;49;00m
   317	[37mC--this threshold for determining when an eigenvalue has[39;49;00m
   318	[37mC--not moved, and is therefore uncontrollable, is critical,[39;49;00m
   319	[37mC--and may require future changes with more experience.[39;49;00m
   320	[37mC[39;49;00m
   321	      [37m  [39;49;00mEPS1[37m [39;49;00m=[37m [39;49;00m[36mSQRT[39;49;00m(EPS)[37m[39;49;00m
   322	[37mC[39;49;00m
   323	[37mC--for each eigenvalue pair, decide if it is controllable[39;49;00m
   324	[37mC[39;49;00m
   325	      [37m  [39;49;00m[34mDO [39;49;00m[34m280[39;49;00m[37m [39;49;00mI[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00mN[37m[39;49;00m
   326	[37mC[39;49;00m
   327	[37mC--note that we are working with the "pivoted" work matrix[39;49;00m
   328	[37mC--and are looking at its diagonal elements[39;49;00m
   329	[37mC[39;49;00m
   330	      [37m    [39;49;00m[34mIF[39;49;00m[37m [39;49;00m(WORK(IPVT(I),JPVT(I))/ANORM[37m [39;49;00m.LE.[37m [39;49;00mEPS1)[37m [39;49;00m[34mTHEN[39;49;00m[37m[39;49;00m
   331	      [37m      [39;49;00mCON(I)[37m [39;49;00m=[37m [39;49;00m.FALSE.[37m[39;49;00m
   332	      [37m    [39;49;00m[34mELSE[39;49;00m[37m[39;49;00m
   333	      [37m      [39;49;00mCON(I)[37m [39;49;00m=[37m [39;49;00m.TRUE.[37m[39;49;00m
   334	      [37m    [39;49;00m[34mEND [39;49;00m[34mIF[39;49;00m[37m[39;49;00m
   335	280   [37m  [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m
   336	[37mC[39;49;00m
   337	[37mC--finally![39;49;00m
   338	[37mC[39;49;00m
   339	      [37m  [39;49;00m[34mRETURN[39;49;00m[37m[39;49;00m
   340	        END

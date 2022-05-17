     1^I      [37m  [39;49;00m[34mSUBROUTINE [39;49;00mAHCON[37m [39;49;00m(SIZE,N,M,A,B,OLEVR,OLEVI,CLEVR,CLEVI,[37m         [39;49;00m[37mTRUNCATED[39;49;00m[37m[39;49;00m$
     2^I     &[37m                    [39;49;00mSCR1,SCR2,IPVT,JPVT,CON,WORK,ISEED,IERR)[37m [39;49;00m[37m!Test[39;49;00m[37m inline comment[39;49;00m[37m[39;49;00m$
     3^I[37mC[39;49;00m$
     4^I[37mC       FUNCTION:[39;49;00m$
     5^I[37mCF[39;49;00m$
     6^I[37mCF      Determines whether the pair (A,B) is controllable and flags[39;49;00m$
     7^I[37mCF      the eigenvalues corresponding to uncontrollable modes.[39;49;00m$
     8^I[37mCF      this ad-hoc controllability calculation uses a random matrix F[39;49;00m$
     9^I[37mCF      and computes whether eigenvalues move from A to the controlled[39;49;00m$
    10^I[37mCF      system A+B*F.[39;49;00m$
    11^I[37mCF[39;49;00m$
    12^I[37mC       USAGE:[39;49;00m$
    13^I[37mCU[39;49;00m$
    14^I[37mCU      CALL AHCON (SIZE,N,M,A,B,OLEVR,OLEVI,CLEVR,CLEVI,SCR1,SCR2,IPVT,[39;49;00m$
    15^I[37mCU                  JPVT,CON,WORK,ISEED,IERR)[39;49;00m$
    16^I[37mCU[39;49;00m$
    17^I[37mCU      since AHCON generates different random F matrices for each[39;49;00m$
    18^I[37mCU      call, as long as iseed is not re-initialized by the main[39;49;00m$
    19^I[37mCU      program, and since this code has the potential to be fooled[39;49;00m$
    20^I[37mCU      by extremely ill-conditioned problems, the cautious user[39;49;00m$
    21^I[37mCU      may wish to call it multiple times and rely, perhaps, on[39;49;00m$
    22^I[37mCU      a 2-of-3 vote.  We believe, but have not proved, that any[39;49;00m$
    23^I[37mCU      errors this routine may produce are conservative--i.e., that[39;49;00m$
    24^I[37mCU      it may flag a controllable mode as uncontrollable, but[39;49;00m$
    25^I[37mCU      not vice-versa.[39;49;00m$
    26^I[37mCU[39;49;00m$
    27^I[37mC       INPUTS:[39;49;00m$
    28^I[37mCI[39;49;00m$
    29^I[37mCI      SIZE    integer - first dimension of all 2-d arrays.[39;49;00m$
    30^I[37mCI[39;49;00m$
    31^I[37mCI      N       integer - number of states.[39;49;00m$
    32^I[37mCI[39;49;00m$
    33^I[37mCI      M       integer - number of inputs.[39;49;00m$
    34^I[37mCI[39;49;00m$
    35^I[37mCI      A       double precision - SIZE by N array containing the[39;49;00m$
    36^I[37mCI              N by N system dynamics matrix A.[39;49;00m$
    37^I[37mCI[39;49;00m$
    38^I[37mCI      B       double precision - SIZE by M array containing the[39;49;00m$
    39^I[37mCI              N by M system input matrix B.[39;49;00m$
    40^I[37mCI[39;49;00m$
    41^I[37mCI      ISEED   initial seed for random number generator; if ISEED=0,[39;49;00m$
    42^I[37mCI              then AHCON will set ISEED to a legal value.[39;49;00m$
    43^I[37mCI[39;49;00m$
    44^I[37mC       OUTPUTS:[39;49;00m$
    45^I[37mCO[39;49;00m$
    46^I[37mCO      OLEVR   double precision - N dimensional vector containing the[39;49;00m$
    47^I[37mCO              real parts of the eigenvalues of A.[39;49;00m$
    48^I[37mCO[39;49;00m$
    49^I[37mCO      OLEVI   double precision - N dimensional vector containing the[39;49;00m$
    50^I[37mCO              imaginary parts of the eigenvalues of A.[39;49;00m$
    51^I[37mCO[39;49;00m$
    52^I[37mCO      CLEVR   double precision - N dimensional vector work space[39;49;00m$
    53^I[37mCO              containing the real parts of the eigenvalues of A+B*F,[39;49;00m$
    54^I[37mCO              where F is the random matrix.[39;49;00m$
    55^I[37mCO[39;49;00m$
    56^I[37mCO      CLEVI   double precision - N dimensional vector work space[39;49;00m$
    57^I[37mCO              containing the imaginary parts of the eigenvalues of[39;49;00m$
    58^I[37mCO              A+B*F, where F is the random matrix.[39;49;00m$
    59^I[37mCO[39;49;00m$
    60^I[37mCO      SCR1    double precision - N dimensional vector containing the[39;49;00m$
    61^I[37mCO              magnitudes of the corresponding eigenvalues of A.[39;49;00m$
    62^I[37mCO[39;49;00m$
    63^I[37mCO      SCR2    double precision - N dimensional vector containing the[39;49;00m$
    64^I[37mCO              damping factors of the corresponding eigenvalues of A.[39;49;00m$
    65^I[37mCO[39;49;00m$
    66^I[37mCO      IPVT    integer - N dimensional vector; contains the row pivots[39;49;00m$
    67^I[37mCO              used in finding the nearest neighbor eigenvalues between[39;49;00m$
    68^I[37mCO              those of A and of A+B*F.  The IPVT(1)th eigenvalue of[39;49;00m$
    69^I[37mCO              A and the JPVT(1)th eigenvalue of A+B*F are the closest[39;49;00m$
    70^I[37mCO              pair.[39;49;00m$
    71^I[37mCO[39;49;00m$
    72^I[37mCO      JPVT    integer - N dimensional vector; contains the column[39;49;00m$
    73^I[37mCO              pivots used in finding the nearest neighbor eigenvalues;[39;49;00m$
    74^I[37mCO              see IPVT.[39;49;00m$
    75^I[37mCO[39;49;00m$
    76^I[37mCO      CON     logical - N dimensional vector; flagging the uncontrollable[39;49;00m$
    77^I[37mCO              modes of the system.  CON(I)=.TRUE. implies the[39;49;00m$
    78^I[37mCO              eigenvalue of A given by DCMPLX(OLEVR(IPVT(I)),OLEVI(IPVT(i)))[39;49;00m$
    79^I[37mCO              corresponds to a controllable mode; CON(I)=.FALSE.[39;49;00m$
    80^I[37mCO              implies an uncontrollable mode for that eigenvalue.[39;49;00m$
    81^I[37mCO[39;49;00m$
    82^I[37mCO      WORK    double precision - SIZE by N dimensional array containing[39;49;00m$
    83^I[37mCO              an N by N matrix.  WORK(I,J) is the distance between[39;49;00m$
    84^I[37mCO              the open loop eigenvalue given by DCMPLX(OLEVR(I),OLEVI(I))[39;49;00m$
    85^I[37mCO              and the closed loop eigenvalue of A+B*F given by[39;49;00m$
    86^I[37mCO              DCMPLX(CLEVR(J),CLEVI(J)).[39;49;00m$
    87^I[37mCO[39;49;00m$
    88^I[37mCO      IERR    integer - IERR=0 indicates normal return; a non-zero[39;49;00m$
    89^I[37mCO              value indicates trouble in the eigenvalue calculation.[39;49;00m$
    90^I[37mCO              see the EISPACK and EIGEN documentation for details.[39;49;00m$
    91^I[37mCO[39;49;00m$
    92^I[37mC       ALGORITHM:[39;49;00m$
    93^I[37mCA[39;49;00m$
    94^I[37mCA      Calculate eigenvalues of A and of A+B*F for a randomly[39;49;00m$
    95^I[37mCA      generated F, and see which ones change.  Use a full pivot[39;49;00m$
    96^I[37mCA      search through a matrix of euclidean distance measures[39;49;00m$
    97^I[37mCA      between each pair of eigenvalues from (A,A+BF) to[39;49;00m$
    98^I[37mCA      determine the closest pairs.[39;49;00m$
    99^I[37mCA[39;49;00m$
   100^I[37mC       MACHINE DEPENDENCIES:[39;49;00m$
   101^I[37mCM[39;49;00m$
   102^I[37mCM       NONE[39;49;00m$
   103^I[37mCM[39;49;00m$
   104^I[37mC       HISTORY:[39;49;00m$
   105^I[37mCH[39;49;00m$
   106^I[37mCH      written by:             Birdwell & Laub[39;49;00m$
   107^I[37mCH      date:                   May 18, 1985[39;49;00m$
   108^I[37mCH      current version:        1.0[39;49;00m$
   109^I[37mCH      modifications:          made machine independent and modified for[39;49;00m$
   110^I[37mCH                              f77:bb:8-86.[39;49;00m$
   111^I[37mCH                              changed cmplx -> dcmplx: 7/27/88 jdb[39;49;00m$
   112^I[37mCH[39;49;00m$
   113^I[37mC       ROUTINES CALLED:[39;49;00m$
   114^I[37mCC[39;49;00m$
   115^I[37mCC      EIGEN,RAND[39;49;00m$
   116^I[37mCC[39;49;00m$
   117^I[37mC       COMMON MEMORY USED:[39;49;00m$
   118^I[37mCM[39;49;00m$
   119^I[37mCM      none[39;49;00m$
   120^I[37mCM[39;49;00m$
   121^I[37mC----------------------------------------------------------------------[39;49;00m$
   122^I[37mC       written for:    The CASCADE Project[39;49;00m$
   123^I[37mC                       Oak Ridge National Laboratory[39;49;00m$
   124^I[37mC                       U.S. Department of Energy[39;49;00m$
   125^I[37mC                       contract number DE-AC05-840R21400[39;49;00m$
   126^I[37mC                       subcontract number 37B-7685 S13[39;49;00m$
   127^I[37mC                       organization:   The University of Tennessee[39;49;00m$
   128^I[37mC----------------------------------------------------------------------[39;49;00m$
   129^I[37mC       THIS SOFTWARE IS IN THE PUBLIC DOMAIN[39;49;00m$
   130^I[37mC       NO RESTRICTIONS ON ITS USE ARE IMPLIED[39;49;00m$
   131^I[37mC----------------------------------------------------------------------[39;49;00m$
   132^I[37mC[39;49;00m$
   133^I[37mC--global variables:[39;49;00m$
   134^I[37mC[39;49;00m$
   135^I      [37m  [39;49;00m[36mINTEGER         [39;49;00mSIZE[37m[39;49;00m$
   136^I      [37m  [39;49;00m[36mINTEGER         [39;49;00mN[37m[39;49;00m$
   137^I      [37m  [39;49;00m[36mINTEGER         [39;49;00mM[37m[39;49;00m$
   138^I      [37m  [39;49;00m[36mINTEGER         [39;49;00mIPVT([34m1[39;49;00m)[37m[39;49;00m$
   139^I      [37m  [39;49;00m[36mINTEGER         [39;49;00mJPVT([34m1[39;49;00m)[37m[39;49;00m$
   140^I      [37m  [39;49;00m[36mINTEGER         [39;49;00mIERR[37m[39;49;00m$
   141^I[37mC[39;49;00m$
   142^I      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mA(SIZE,N)[37m[39;49;00m$
   143^I      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mB(SIZE,M)[37m[39;49;00m$
   144^I      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mWORK(SIZE,N)[37m[39;49;00m$
   145^I      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mCLEVR(N)[37m[39;49;00m$
   146^I      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mCLEVI(N)[37m[39;49;00m$
   147^I      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mOLEVR(N)[37m[39;49;00m$
   148^I      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mOLEVI(N)[37m[39;49;00m$
   149^I      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mSCR1(N)[37m[39;49;00m$
   150^I      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mSCR2(N)[37m[39;49;00m$
   151^I[37mC[39;49;00m$
   152^I      [37m  [39;49;00m[36mLOGICAL                 [39;49;00mCON(N)[37m[39;49;00m$
   153^I[37mC[39;49;00m$
   154^I[37mC--local variables:[39;49;00m$
   155^I[37mC[39;49;00m$
   156^I      [37m  [39;49;00m[36mINTEGER         [39;49;00mISEED[37m[39;49;00m$
   157^I      [37m  [39;49;00m[36mINTEGER         [39;49;00mITEMP[37m[39;49;00m$
   158^I      [37m  [39;49;00m[36mINTEGER         [39;49;00mK1[37m[39;49;00m$
   159^I      [37m  [39;49;00m[36mINTEGER         [39;49;00mK2[37m[39;49;00m$
   160^I      [37m  [39;49;00m[36mINTEGER         [39;49;00mI[37m[39;49;00m$
   161^I      [37m  [39;49;00m[36mINTEGER         [39;49;00mJ[37m[39;49;00m$
   162^I      [37m  [39;49;00m[36mINTEGER         [39;49;00mK[37m[39;49;00m$
   163^I      [37m  [39;49;00m[36mINTEGER         [39;49;00mIMAX[37m[39;49;00m$
   164^I      [37m  [39;49;00m[36mINTEGER         [39;49;00mJMAX[37m[39;49;00m$
   165^I[37mC[39;49;00m$
   166^I      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00m[34mVALUE[39;49;00m[37m[39;49;00m$
   167^I      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mEPS[37m[39;49;00m$
   168^I      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mEPS1[37m[39;49;00m$
   169^I      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mTEMP[37m[39;49;00m$
   170^I      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mCURR[37m[39;49;00m$
   171^I      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mANORM[37m[39;49;00m$
   172^I      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mBNORM[37m[39;49;00m$
   173^I      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mCOLNRM[37m[39;49;00m$
   174^I      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mRNDMNO[37m[39;49;00m$
   175^I[37mC[39;49;00m$
   176^I      [37m  [39;49;00m[36mDOUBLE COMPLEX^I^I[39;49;00mDCMPLX[37m[39;49;00m$
   177^I[37mC[39;49;00m$
   178^I[37mC--compute machine epsilon[39;49;00m$
   179^I[37mC[39;49;00m$
   180^I      [37m  [39;49;00mEPS[37m [39;49;00m=[37m [39;49;00m[34m1.D0[39;49;00m[37m[39;49;00m$
   181^I100   [37m  [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m$
   182^I      [37m    [39;49;00mEPS[37m [39;49;00m=[37m [39;49;00mEPS[37m [39;49;00m/[37m [39;49;00m[34m2.D0[39;49;00m[37m[39;49;00m$
   183^I      [37m    [39;49;00mEPS1[37m [39;49;00m=[37m [39;49;00m[34m1.D0[39;49;00m[37m [39;49;00m+[37m [39;49;00mEPS[37m[39;49;00m$
   184^I      [37m  [39;49;00m[34mIF[39;49;00m[37m [39;49;00m(EPS1[37m [39;49;00m.NE.[37m [39;49;00m[34m1.D0[39;49;00m)[37m [39;49;00m[34mGO[39;49;00m[37m [39;49;00m[34mTO[39;49;00m[37m [39;49;00m[34m100[39;49;00m[37m[39;49;00m$
   185^I      [37m  [39;49;00mEPS[37m [39;49;00m=[37m [39;49;00mEPS[37m [39;49;00m*[37m [39;49;00m[34m2.D0[39;49;00m[37m[39;49;00m$
   186^I[37mC[39;49;00m$
   187^I[37mC--compute the l-1 norm of a[39;49;00m$
   188^I[37mC[39;49;00m$
   189^I      [37m  [39;49;00mANORM[37m [39;49;00m=[37m [39;49;00m[34m0.0D0[39;49;00m[37m[39;49;00m$
   190^I      [37m  [39;49;00m[34mDO [39;49;00m[34m120[39;49;00m[37m [39;49;00mJ[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00mN[37m[39;49;00m$
   191^I      [37m    [39;49;00mCOLNRM[37m [39;49;00m=[37m [39;49;00m[34m0.D0[39;49;00m[37m[39;49;00m$
   192^I      [37m    [39;49;00m[34mDO [39;49;00m[34m110[39;49;00m[37m [39;49;00mI[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00mN[37m[39;49;00m$
   193^I      [37m      [39;49;00mCOLNRM[37m [39;49;00m=[37m [39;49;00mCOLNRM[37m [39;49;00m+[37m [39;49;00m[36mABS[39;49;00m(A(I,J))[37m[39;49;00m$
   194^I110   [37m    [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m$
   195^I      [37m    [39;49;00m[34mIF[39;49;00m[37m [39;49;00m(COLNRM[37m [39;49;00m.GT.[37m [39;49;00mANORM)[37m [39;49;00mANORM[37m [39;49;00m=[37m [39;49;00mCOLNRM[37m[39;49;00m$
   196^I120   [37m  [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m$
   197^I[37mC[39;49;00m$
   198^I[37mC--compute the l-1 norm of b[39;49;00m$
   199^I[37mC[39;49;00m$
   200^I      [37m  [39;49;00mBNORM[37m [39;49;00m=[37m [39;49;00m[34m0.0D0[39;49;00m[37m[39;49;00m$
   201^I      [37m  [39;49;00m[34mDO [39;49;00m[34m140[39;49;00m[37m [39;49;00mJ[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00mM[37m[39;49;00m$
   202^I      [37m    [39;49;00mCOLNRM[37m [39;49;00m=[37m [39;49;00m[34m0.D0[39;49;00m[37m[39;49;00m$
   203^I      [37m    [39;49;00m[34mDO [39;49;00m[34m130[39;49;00m[37m [39;49;00mI[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00mN[37m[39;49;00m$
   204^I      [37m      [39;49;00mCOLNRM[37m [39;49;00m=[37m [39;49;00mCOLNRM[37m [39;49;00m+[37m [39;49;00m[36mABS[39;49;00m(B(I,J))[37m[39;49;00m$
   205^I130   [37m    [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m$
   206^I      [37m    [39;49;00m[34mIF[39;49;00m[37m [39;49;00m(COLNRM[37m [39;49;00m.GT.[37m [39;49;00mBNORM)[37m [39;49;00mBNORM[37m [39;49;00m=[37m [39;49;00mCOLNRM[37m[39;49;00m$
   207^I140   [37m  [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m$
   208^I[37mC[39;49;00m$
   209^I[37mC--compute a + b * f[39;49;00m$
   210^I[37mC[39;49;00m$
   211^I      [37m  [39;49;00m[34mDO [39;49;00m[34m160[39;49;00m[37m [39;49;00mJ[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00mN[37m[39;49;00m$
   212^I      [37m    [39;49;00m[34mDO [39;49;00m[34m150[39;49;00m[37m [39;49;00mI[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00mN[37m[39;49;00m$
   213^I      [37m      [39;49;00mWORK(I,J)[37m [39;49;00m=[37m [39;49;00mA(I,J)[37m[39;49;00m$
   214^I150   [37m    [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m$
   215^I160   [37m  [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m$
   216^I[37mC[39;49;00m$
   217^I[37mC--the elements of f are random with uniform distribution[39;49;00m$
   218^I[37mC--from -anorm/bnorm to +anorm/bnorm[39;49;00m$
   219^I[37mC--note that f is not explicitly stored as a matrix[39;49;00m$
   220^I[37mC--pathalogical floating point notes:  the if (bnorm .gt. 0.d0)[39;49;00m$
   221^I[37mC--test should actually be if (bnorm .gt. dsmall), where dsmall[39;49;00m$
   222^I[37mC--is the smallest representable number whose reciprocal does[39;49;00m$
   223^I[37mC--not generate an overflow or loss of precision.[39;49;00m$
   224^I[37mC[39;49;00m$
   225^I      [37m  [39;49;00m[34mIF[39;49;00m[37m [39;49;00m(ISEED[37m [39;49;00m.EQ.[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00mISEED[37m [39;49;00m=[37m [39;49;00m[34m86345823[39;49;00m[37m[39;49;00m$
   226^I      [37m  [39;49;00m[34mIF[39;49;00m[37m [39;49;00m(ANORM[37m [39;49;00m.EQ.[37m [39;49;00m[34m0.D0[39;49;00m)[37m [39;49;00mANORM[37m [39;49;00m=[37m [39;49;00m[34m1.D0[39;49;00m[37m[39;49;00m$
   227^I      [37m  [39;49;00m[34mIF[39;49;00m[37m [39;49;00m(BNORM[37m [39;49;00m.GT.[37m [39;49;00m[34m0.D0[39;49;00m)[37m [39;49;00m[34mTHEN[39;49;00m[37m[39;49;00m$
   228^I      [37m    [39;49;00mTEMP[37m [39;49;00m=[37m [39;49;00m[34m2.D0[39;49;00m[37m [39;49;00m*[37m [39;49;00mANORM[37m [39;49;00m/[37m [39;49;00mBNORM[37m[39;49;00m$
   229^I      [37m  [39;49;00m[34mELSE[39;49;00m[37m[39;49;00m$
   230^I      [37m    [39;49;00mTEMP[37m [39;49;00m=[37m [39;49;00m[34m2.D0[39;49;00m[37m[39;49;00m$
   231^I      [37m  [39;49;00m[34mEND [39;49;00m[34mIF[39;49;00m[37m[39;49;00m$
   232^I      [37m  [39;49;00m[34mDO [39;49;00m[34m190[39;49;00m[37m [39;49;00mK[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00mM[37m[39;49;00m$
   233^I      [37m    [39;49;00m[34mDO [39;49;00m[34m180[39;49;00m[37m [39;49;00mJ[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00mN[37m[39;49;00m$
   234^I      [37m      [39;49;00m[34mCALL [39;49;00m[36mRAND[39;49;00m(ISEED,ISEED,RNDMNO)[37m[39;49;00m$
   235^I      [37m      [39;49;00m[34mVALUE[39;49;00m[37m [39;49;00m=[37m [39;49;00m(RNDMNO[37m [39;49;00m-[37m [39;49;00m[34m0.5D0[39;49;00m)[37m [39;49;00m*[37m [39;49;00mTEMP[37m[39;49;00m$
   236^I      [37m      [39;49;00m[34mDO [39;49;00m[34m170[39;49;00m[37m [39;49;00mI[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00mN[37m[39;49;00m$
   237^I      [37m        [39;49;00mWORK(I,J)[37m [39;49;00m=[37m [39;49;00mWORK(I,J)[37m [39;49;00m+[37m [39;49;00mB(I,K)*[34mVALUE[39;49;00m[37m[39;49;00m$
   238^I170   [37m      [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m$
   239^I180   [37m    [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m$
   240^I190   [37m  [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m$
   241^I[37mC[39;49;00m$
   242^I[37mC--compute the eigenvalues of a + b*f, and several other things[39;49;00m$
   243^I[37mC[39;49;00m$
   244^I      [37m  [39;49;00m[34mCALL [39;49;00mEIGEN[37m [39;49;00m([34m0[39;49;00m,SIZE,N,WORK,CLEVR,CLEVI,WORK,SCR1,SCR2,IERR)[37m[39;49;00m$
   245^I      [37m  [39;49;00m[34mIF[39;49;00m[37m [39;49;00m(IERR[37m [39;49;00m.NE.[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mRETURN[39;49;00m[37m[39;49;00m$
   246^I[37mC[39;49;00m$
   247^I[37mC--copy a so it is not destroyed[39;49;00m$
   248^I[37mC[39;49;00m$
   249^I      [37m  [39;49;00m[34mDO [39;49;00m[34m210[39;49;00m[37m [39;49;00mJ[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00mN[37m[39;49;00m$
   250^I      [37m    [39;49;00m[34mDO [39;49;00m[34m200[39;49;00m[37m [39;49;00mI[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00mN[37m[39;49;00m$
   251^I      [37m      [39;49;00mWORK(I,J)[37m [39;49;00m=[37m [39;49;00mA(I,J)[37m[39;49;00m$
   252^I200   [37m    [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m$
   253^I210   [37m  [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m$
   254^I[37mC[39;49;00m$
   255^I[37mC--compute the eigenvalues of a, and several other things[39;49;00m$
   256^I[37mC[39;49;00m$
   257^I      [37m  [39;49;00m[34mCALL [39;49;00mEIGEN[37m [39;49;00m([34m0[39;49;00m,SIZE,N,WORK,OLEVR,OLEVI,WORK,SCR1,SCR2,IERR)[37m[39;49;00m$
   258^I      [37m  [39;49;00m[34mIF[39;49;00m[37m [39;49;00m(IERR[37m [39;49;00m.NE.[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mRETURN[39;49;00m[37m[39;49;00m$
   259^I[37mC[39;49;00m$
   260^I[37mC--form the matrix of distances between eigenvalues of a and[39;49;00m$
   261^I[37mC--EIGENVALUES OF A+B*F[39;49;00m$
   262^I[37mC[39;49;00m$
   263^I      [37m  [39;49;00m[34mDO [39;49;00m[34m230[39;49;00m[37m [39;49;00mJ[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00mN[37m[39;49;00m$
   264^I      [37m    [39;49;00m[34mDO [39;49;00m[34m220[39;49;00m[37m [39;49;00mI[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00mN[37m[39;49;00m$
   265^I      [37m      [39;49;00mWORK(I,J)[37m [39;49;00m=[37m[39;49;00m$
   266^I     &[37m        [39;49;00m[36mABS[39;49;00m(DCMPLX(OLEVR(I),OLEVI(I))-DCMPLX(CLEVR(J),CLEVI(J)))[37m[39;49;00m$
   267^I220   [37m    [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m$
   268^I230   [37m  [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m$
   269^I[37mC[39;49;00m$
   270^I[37mC--initialize row and column pivots[39;49;00m$
   271^I[37mC[39;49;00m$
   272^I      [37m  [39;49;00m[34mDO [39;49;00m[34m240[39;49;00m[37m [39;49;00mI[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00mN[37m[39;49;00m$
   273^I      [37m    [39;49;00mIPVT(I)[37m [39;49;00m=[37m [39;49;00mI[37m[39;49;00m$
   274^I      [37m    [39;49;00mJPVT(I)[37m [39;49;00m=[37m [39;49;00mI[37m[39;49;00m$
   275^I240   [37m  [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m$
   276^I[37mC[39;49;00m$
   277^I[37mC--a little bit messy to avoid swapping columns and[39;49;00m$
   278^I[37mC--rows of work[39;49;00m$
   279^I[37mC[39;49;00m$
   280^I      [37m  [39;49;00m[34mDO [39;49;00m[34m270[39;49;00m[37m [39;49;00mI[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00mN-[34m1[39;49;00m[37m[39;49;00m$
   281^I[37mC[39;49;00m$
   282^I[37mC--find the minimum element of each lower right square[39;49;00m$
   283^I[37mC--submatrix of work, for submatrices of size n x n[39;49;00m$
   284^I[37mC--through 2 x 2[39;49;00m$
   285^I[37mC[39;49;00m$
   286^I      [37m    [39;49;00mCURR[37m [39;49;00m=[37m [39;49;00mWORK(IPVT(I),JPVT(I))[37m[39;49;00m$
   287^I      [37m    [39;49;00mIMAX[37m [39;49;00m=[37m [39;49;00mI[37m[39;49;00m$
   288^I      [37m    [39;49;00mJMAX[37m [39;49;00m=[37m [39;49;00mI[37m[39;49;00m$
   289^I      [37m    [39;49;00mTEMP[37m [39;49;00m=[37m [39;49;00mCURR[37m[39;49;00m$
   290^I[37mC[39;49;00m$
   291^I[37mC--find the minimum element[39;49;00m$
   292^I[37mC[39;49;00m$
   293^I      [37m    [39;49;00m[34mDO [39;49;00m[34m260[39;49;00m[37m [39;49;00mK1[37m [39;49;00m=[37m [39;49;00mI,[37m [39;49;00mN[37m[39;49;00m$
   294^I      [37m      [39;49;00m[34mDO [39;49;00m[34m250[39;49;00m[37m [39;49;00mK2[37m [39;49;00m=[37m [39;49;00mI,[37m [39;49;00mN[37m[39;49;00m$
   295^I      [37m        [39;49;00m[34mIF[39;49;00m[37m [39;49;00m(WORK(IPVT(K1),JPVT(K2))[37m [39;49;00m.LT.[37m [39;49;00mTEMP)[37m [39;49;00m[34mTHEN[39;49;00m[37m[39;49;00m$
   296^I      [37m          [39;49;00mTEMP[37m [39;49;00m=[37m [39;49;00mWORK(IPVT(K1),JPVT(K2))[37m[39;49;00m$
   297^I      [37m          [39;49;00mIMAX[37m [39;49;00m=[37m [39;49;00mK1[37m[39;49;00m$
   298^I      [37m          [39;49;00mJMAX[37m [39;49;00m=[37m [39;49;00mK2[37m[39;49;00m$
   299^I      [37m        [39;49;00m[34mEND [39;49;00m[34mIF[39;49;00m[37m[39;49;00m$
   300^I250   [37m      [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m$
   301^I260   [37m    [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m$
   302^I[37mC[39;49;00m$
   303^I[37mC--update row and column pivots for indirect addressing of work[39;49;00m$
   304^I[37mC[39;49;00m$
   305^I      [37m    [39;49;00mITEMP[37m [39;49;00m=[37m [39;49;00mIPVT(I)[37m[39;49;00m$
   306^I      [37m    [39;49;00mIPVT(I)[37m [39;49;00m=[37m [39;49;00mIPVT(IMAX)[37m[39;49;00m$
   307^I      [37m    [39;49;00mIPVT(IMAX)[37m [39;49;00m=[37m [39;49;00mITEMP[37m[39;49;00m$
   308^I[37mC[39;49;00m$
   309^I      [37m    [39;49;00mITEMP[37m [39;49;00m=[37m [39;49;00mJPVT(I)[37m[39;49;00m$
   310^I      [37m    [39;49;00mJPVT(I)[37m [39;49;00m=[37m [39;49;00mJPVT(JMAX)[37m[39;49;00m$
   311^I      [37m    [39;49;00mJPVT(JMAX)[37m [39;49;00m=[37m [39;49;00mITEMP[37m[39;49;00m$
   312^I[37mC[39;49;00m$
   313^I[37mC--do next submatrix[39;49;00m$
   314^I[37mC[39;49;00m$
   315^I270   [37m  [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m$
   316^I[37mC[39;49;00m$
   317^I[37mC--this threshold for determining when an eigenvalue has[39;49;00m$
   318^I[37mC--not moved, and is therefore uncontrollable, is critical,[39;49;00m$
   319^I[37mC--and may require future changes with more experience.[39;49;00m$
   320^I[37mC[39;49;00m$
   321^I      [37m  [39;49;00mEPS1[37m [39;49;00m=[37m [39;49;00m[36mSQRT[39;49;00m(EPS)[37m[39;49;00m$
   322^I[37mC[39;49;00m$
   323^I[37mC--for each eigenvalue pair, decide if it is controllable[39;49;00m$
   324^I[37mC[39;49;00m$
   325^I      [37m  [39;49;00m[34mDO [39;49;00m[34m280[39;49;00m[37m [39;49;00mI[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00mN[37m[39;49;00m$
   326^I[37mC[39;49;00m$
   327^I[37mC--note that we are working with the "pivoted" work matrix[39;49;00m$
   328^I[37mC--and are looking at its diagonal elements[39;49;00m$
   329^I[37mC[39;49;00m$
   330^I      [37m    [39;49;00m[34mIF[39;49;00m[37m [39;49;00m(WORK(IPVT(I),JPVT(I))/ANORM[37m [39;49;00m.LE.[37m [39;49;00mEPS1)[37m [39;49;00m[34mTHEN[39;49;00m[37m[39;49;00m$
   331^I      [37m      [39;49;00mCON(I)[37m [39;49;00m=[37m [39;49;00m.FALSE.[37m[39;49;00m$
   332^I      [37m    [39;49;00m[34mELSE[39;49;00m[37m[39;49;00m$
   333^I      [37m      [39;49;00mCON(I)[37m [39;49;00m=[37m [39;49;00m.TRUE.[37m[39;49;00m$
   334^I      [37m    [39;49;00m[34mEND [39;49;00m[34mIF[39;49;00m[37m[39;49;00m$
   335^I280   [37m  [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m$
   336^I[37mC[39;49;00m$
   337^I[37mC--finally![39;49;00m$
   338^I[37mC[39;49;00m$
   339^I      [37m  [39;49;00m[34mRETURN[39;49;00m[37m[39;49;00m$
   340^I        END$

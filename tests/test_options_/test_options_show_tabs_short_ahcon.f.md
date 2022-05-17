      [37m  [39;49;00m[34mSUBROUTINE [39;49;00mAHCON[37m [39;49;00m(SIZE,N,M,A,B,OLEVR,OLEVI,CLEVR,CLEVI,[37m         [39;49;00m[37mTRUNCATED[39;49;00m[37m[39;49;00m
     &[37m                    [39;49;00mSCR1,SCR2,IPVT,JPVT,CON,WORK,ISEED,IERR)[37m [39;49;00m[37m!Test[39;49;00m[37m inline comment[39;49;00m[37m[39;49;00m
[37mC[39;49;00m
[37mC       FUNCTION:[39;49;00m
[37mCF[39;49;00m
[37mCF      Determines whether the pair (A,B) is controllable and flags[39;49;00m
[37mCF      the eigenvalues corresponding to uncontrollable modes.[39;49;00m
[37mCF      this ad-hoc controllability calculation uses a random matrix F[39;49;00m
[37mCF      and computes whether eigenvalues move from A to the controlled[39;49;00m
[37mCF      system A+B*F.[39;49;00m
[37mCF[39;49;00m
[37mC       USAGE:[39;49;00m
[37mCU[39;49;00m
[37mCU      CALL AHCON (SIZE,N,M,A,B,OLEVR,OLEVI,CLEVR,CLEVI,SCR1,SCR2,IPVT,[39;49;00m
[37mCU                  JPVT,CON,WORK,ISEED,IERR)[39;49;00m
[37mCU[39;49;00m
[37mCU      since AHCON generates different random F matrices for each[39;49;00m
[37mCU      call, as long as iseed is not re-initialized by the main[39;49;00m
[37mCU      program, and since this code has the potential to be fooled[39;49;00m
[37mCU      by extremely ill-conditioned problems, the cautious user[39;49;00m
[37mCU      may wish to call it multiple times and rely, perhaps, on[39;49;00m
[37mCU      a 2-of-3 vote.  We believe, but have not proved, that any[39;49;00m
[37mCU      errors this routine may produce are conservative--i.e., that[39;49;00m
[37mCU      it may flag a controllable mode as uncontrollable, but[39;49;00m
[37mCU      not vice-versa.[39;49;00m
[37mCU[39;49;00m
[37mC       INPUTS:[39;49;00m
[37mCI[39;49;00m
[37mCI      SIZE    integer - first dimension of all 2-d arrays.[39;49;00m
[37mCI[39;49;00m
[37mCI      N       integer - number of states.[39;49;00m
[37mCI[39;49;00m
[37mCI      M       integer - number of inputs.[39;49;00m
[37mCI[39;49;00m
[37mCI      A       double precision - SIZE by N array containing the[39;49;00m
[37mCI              N by N system dynamics matrix A.[39;49;00m
[37mCI[39;49;00m
[37mCI      B       double precision - SIZE by M array containing the[39;49;00m
[37mCI              N by M system input matrix B.[39;49;00m
[37mCI[39;49;00m
[37mCI      ISEED   initial seed for random number generator; if ISEED=0,[39;49;00m
[37mCI              then AHCON will set ISEED to a legal value.[39;49;00m
[37mCI[39;49;00m
[37mC       OUTPUTS:[39;49;00m
[37mCO[39;49;00m
[37mCO      OLEVR   double precision - N dimensional vector containing the[39;49;00m
[37mCO              real parts of the eigenvalues of A.[39;49;00m
[37mCO[39;49;00m
[37mCO      OLEVI   double precision - N dimensional vector containing the[39;49;00m
[37mCO              imaginary parts of the eigenvalues of A.[39;49;00m
[37mCO[39;49;00m
[37mCO      CLEVR   double precision - N dimensional vector work space[39;49;00m
[37mCO              containing the real parts of the eigenvalues of A+B*F,[39;49;00m
[37mCO              where F is the random matrix.[39;49;00m
[37mCO[39;49;00m
[37mCO      CLEVI   double precision - N dimensional vector work space[39;49;00m
[37mCO              containing the imaginary parts of the eigenvalues of[39;49;00m
[37mCO              A+B*F, where F is the random matrix.[39;49;00m
[37mCO[39;49;00m
[37mCO      SCR1    double precision - N dimensional vector containing the[39;49;00m
[37mCO              magnitudes of the corresponding eigenvalues of A.[39;49;00m
[37mCO[39;49;00m
[37mCO      SCR2    double precision - N dimensional vector containing the[39;49;00m
[37mCO              damping factors of the corresponding eigenvalues of A.[39;49;00m
[37mCO[39;49;00m
[37mCO      IPVT    integer - N dimensional vector; contains the row pivots[39;49;00m
[37mCO              used in finding the nearest neighbor eigenvalues between[39;49;00m
[37mCO              those of A and of A+B*F.  The IPVT(1)th eigenvalue of[39;49;00m
[37mCO              A and the JPVT(1)th eigenvalue of A+B*F are the closest[39;49;00m
[37mCO              pair.[39;49;00m
[37mCO[39;49;00m
[37mCO      JPVT    integer - N dimensional vector; contains the column[39;49;00m
[37mCO              pivots used in finding the nearest neighbor eigenvalues;[39;49;00m
[37mCO              see IPVT.[39;49;00m
[37mCO[39;49;00m
[37mCO      CON     logical - N dimensional vector; flagging the uncontrollable[39;49;00m
[37mCO              modes of the system.  CON(I)=.TRUE. implies the[39;49;00m
[37mCO              eigenvalue of A given by DCMPLX(OLEVR(IPVT(I)),OLEVI(IPVT(i)))[39;49;00m
[37mCO              corresponds to a controllable mode; CON(I)=.FALSE.[39;49;00m
[37mCO              implies an uncontrollable mode for that eigenvalue.[39;49;00m
[37mCO[39;49;00m
[37mCO      WORK    double precision - SIZE by N dimensional array containing[39;49;00m
[37mCO              an N by N matrix.  WORK(I,J) is the distance between[39;49;00m
[37mCO              the open loop eigenvalue given by DCMPLX(OLEVR(I),OLEVI(I))[39;49;00m
[37mCO              and the closed loop eigenvalue of A+B*F given by[39;49;00m
[37mCO              DCMPLX(CLEVR(J),CLEVI(J)).[39;49;00m
[37mCO[39;49;00m
[37mCO      IERR    integer - IERR=0 indicates normal return; a non-zero[39;49;00m
[37mCO              value indicates trouble in the eigenvalue calculation.[39;49;00m
[37mCO              see the EISPACK and EIGEN documentation for details.[39;49;00m
[37mCO[39;49;00m
[37mC       ALGORITHM:[39;49;00m
[37mCA[39;49;00m
[37mCA      Calculate eigenvalues of A and of A+B*F for a randomly[39;49;00m
[37mCA      generated F, and see which ones change.  Use a full pivot[39;49;00m
[37mCA      search through a matrix of euclidean distance measures[39;49;00m
[37mCA      between each pair of eigenvalues from (A,A+BF) to[39;49;00m
[37mCA      determine the closest pairs.[39;49;00m
[37mCA[39;49;00m
[37mC       MACHINE DEPENDENCIES:[39;49;00m
[37mCM[39;49;00m
[37mCM       NONE[39;49;00m
[37mCM[39;49;00m
[37mC       HISTORY:[39;49;00m
[37mCH[39;49;00m
[37mCH      written by:             Birdwell & Laub[39;49;00m
[37mCH      date:                   May 18, 1985[39;49;00m
[37mCH      current version:        1.0[39;49;00m
[37mCH      modifications:          made machine independent and modified for[39;49;00m
[37mCH                              f77:bb:8-86.[39;49;00m
[37mCH                              changed cmplx -> dcmplx: 7/27/88 jdb[39;49;00m
[37mCH[39;49;00m
[37mC       ROUTINES CALLED:[39;49;00m
[37mCC[39;49;00m
[37mCC      EIGEN,RAND[39;49;00m
[37mCC[39;49;00m
[37mC       COMMON MEMORY USED:[39;49;00m
[37mCM[39;49;00m
[37mCM      none[39;49;00m
[37mCM[39;49;00m
[37mC----------------------------------------------------------------------[39;49;00m
[37mC       written for:    The CASCADE Project[39;49;00m
[37mC                       Oak Ridge National Laboratory[39;49;00m
[37mC                       U.S. Department of Energy[39;49;00m
[37mC                       contract number DE-AC05-840R21400[39;49;00m
[37mC                       subcontract number 37B-7685 S13[39;49;00m
[37mC                       organization:   The University of Tennessee[39;49;00m
[37mC----------------------------------------------------------------------[39;49;00m
[37mC       THIS SOFTWARE IS IN THE PUBLIC DOMAIN[39;49;00m
[37mC       NO RESTRICTIONS ON ITS USE ARE IMPLIED[39;49;00m
[37mC----------------------------------------------------------------------[39;49;00m
[37mC[39;49;00m
[37mC--global variables:[39;49;00m
[37mC[39;49;00m
      [37m  [39;49;00m[36mINTEGER         [39;49;00mSIZE[37m[39;49;00m
      [37m  [39;49;00m[36mINTEGER         [39;49;00mN[37m[39;49;00m
      [37m  [39;49;00m[36mINTEGER         [39;49;00mM[37m[39;49;00m
      [37m  [39;49;00m[36mINTEGER         [39;49;00mIPVT([34m1[39;49;00m)[37m[39;49;00m
      [37m  [39;49;00m[36mINTEGER         [39;49;00mJPVT([34m1[39;49;00m)[37m[39;49;00m
      [37m  [39;49;00m[36mINTEGER         [39;49;00mIERR[37m[39;49;00m
[37mC[39;49;00m
      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mA(SIZE,N)[37m[39;49;00m
      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mB(SIZE,M)[37m[39;49;00m
      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mWORK(SIZE,N)[37m[39;49;00m
      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mCLEVR(N)[37m[39;49;00m
      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mCLEVI(N)[37m[39;49;00m
      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mOLEVR(N)[37m[39;49;00m
      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mOLEVI(N)[37m[39;49;00m
      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mSCR1(N)[37m[39;49;00m
      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mSCR2(N)[37m[39;49;00m
[37mC[39;49;00m
      [37m  [39;49;00m[36mLOGICAL                 [39;49;00mCON(N)[37m[39;49;00m
[37mC[39;49;00m
[37mC--local variables:[39;49;00m
[37mC[39;49;00m
      [37m  [39;49;00m[36mINTEGER         [39;49;00mISEED[37m[39;49;00m
      [37m  [39;49;00m[36mINTEGER         [39;49;00mITEMP[37m[39;49;00m
      [37m  [39;49;00m[36mINTEGER         [39;49;00mK1[37m[39;49;00m
      [37m  [39;49;00m[36mINTEGER         [39;49;00mK2[37m[39;49;00m
      [37m  [39;49;00m[36mINTEGER         [39;49;00mI[37m[39;49;00m
      [37m  [39;49;00m[36mINTEGER         [39;49;00mJ[37m[39;49;00m
      [37m  [39;49;00m[36mINTEGER         [39;49;00mK[37m[39;49;00m
      [37m  [39;49;00m[36mINTEGER         [39;49;00mIMAX[37m[39;49;00m
      [37m  [39;49;00m[36mINTEGER         [39;49;00mJMAX[37m[39;49;00m
[37mC[39;49;00m
      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00m[34mVALUE[39;49;00m[37m[39;49;00m
      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mEPS[37m[39;49;00m
      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mEPS1[37m[39;49;00m
      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mTEMP[37m[39;49;00m
      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mCURR[37m[39;49;00m
      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mANORM[37m[39;49;00m
      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mBNORM[37m[39;49;00m
      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mCOLNRM[37m[39;49;00m
      [37m  [39;49;00m[36mDOUBLE PRECISION        [39;49;00mRNDMNO[37m[39;49;00m
[37mC[39;49;00m
      [37m  [39;49;00m[36mDOUBLE COMPLEX^I^I[39;49;00mDCMPLX[37m[39;49;00m
[37mC[39;49;00m
[37mC--compute machine epsilon[39;49;00m
[37mC[39;49;00m
      [37m  [39;49;00mEPS[37m [39;49;00m=[37m [39;49;00m[34m1.D0[39;49;00m[37m[39;49;00m
100   [37m  [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m
      [37m    [39;49;00mEPS[37m [39;49;00m=[37m [39;49;00mEPS[37m [39;49;00m/[37m [39;49;00m[34m2.D0[39;49;00m[37m[39;49;00m
      [37m    [39;49;00mEPS1[37m [39;49;00m=[37m [39;49;00m[34m1.D0[39;49;00m[37m [39;49;00m+[37m [39;49;00mEPS[37m[39;49;00m
      [37m  [39;49;00m[34mIF[39;49;00m[37m [39;49;00m(EPS1[37m [39;49;00m.NE.[37m [39;49;00m[34m1.D0[39;49;00m)[37m [39;49;00m[34mGO[39;49;00m[37m [39;49;00m[34mTO[39;49;00m[37m [39;49;00m[34m100[39;49;00m[37m[39;49;00m
      [37m  [39;49;00mEPS[37m [39;49;00m=[37m [39;49;00mEPS[37m [39;49;00m*[37m [39;49;00m[34m2.D0[39;49;00m[37m[39;49;00m
[37mC[39;49;00m
[37mC--compute the l-1 norm of a[39;49;00m
[37mC[39;49;00m
      [37m  [39;49;00mANORM[37m [39;49;00m=[37m [39;49;00m[34m0.0D0[39;49;00m[37m[39;49;00m
      [37m  [39;49;00m[34mDO [39;49;00m[34m120[39;49;00m[37m [39;49;00mJ[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00mN[37m[39;49;00m
      [37m    [39;49;00mCOLNRM[37m [39;49;00m=[37m [39;49;00m[34m0.D0[39;49;00m[37m[39;49;00m
      [37m    [39;49;00m[34mDO [39;49;00m[34m110[39;49;00m[37m [39;49;00mI[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00mN[37m[39;49;00m
      [37m      [39;49;00mCOLNRM[37m [39;49;00m=[37m [39;49;00mCOLNRM[37m [39;49;00m+[37m [39;49;00m[36mABS[39;49;00m(A(I,J))[37m[39;49;00m
110   [37m    [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m
      [37m    [39;49;00m[34mIF[39;49;00m[37m [39;49;00m(COLNRM[37m [39;49;00m.GT.[37m [39;49;00mANORM)[37m [39;49;00mANORM[37m [39;49;00m=[37m [39;49;00mCOLNRM[37m[39;49;00m
120   [37m  [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m
[37mC[39;49;00m
[37mC--compute the l-1 norm of b[39;49;00m
[37mC[39;49;00m
      [37m  [39;49;00mBNORM[37m [39;49;00m=[37m [39;49;00m[34m0.0D0[39;49;00m[37m[39;49;00m
      [37m  [39;49;00m[34mDO [39;49;00m[34m140[39;49;00m[37m [39;49;00mJ[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00mM[37m[39;49;00m
      [37m    [39;49;00mCOLNRM[37m [39;49;00m=[37m [39;49;00m[34m0.D0[39;49;00m[37m[39;49;00m
      [37m    [39;49;00m[34mDO [39;49;00m[34m130[39;49;00m[37m [39;49;00mI[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00mN[37m[39;49;00m
      [37m      [39;49;00mCOLNRM[37m [39;49;00m=[37m [39;49;00mCOLNRM[37m [39;49;00m+[37m [39;49;00m[36mABS[39;49;00m(B(I,J))[37m[39;49;00m
130   [37m    [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m
      [37m    [39;49;00m[34mIF[39;49;00m[37m [39;49;00m(COLNRM[37m [39;49;00m.GT.[37m [39;49;00mBNORM)[37m [39;49;00mBNORM[37m [39;49;00m=[37m [39;49;00mCOLNRM[37m[39;49;00m
140   [37m  [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m
[37mC[39;49;00m
[37mC--compute a + b * f[39;49;00m
[37mC[39;49;00m
      [37m  [39;49;00m[34mDO [39;49;00m[34m160[39;49;00m[37m [39;49;00mJ[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00mN[37m[39;49;00m
      [37m    [39;49;00m[34mDO [39;49;00m[34m150[39;49;00m[37m [39;49;00mI[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00mN[37m[39;49;00m
      [37m      [39;49;00mWORK(I,J)[37m [39;49;00m=[37m [39;49;00mA(I,J)[37m[39;49;00m
150   [37m    [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m
160   [37m  [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m
[37mC[39;49;00m
[37mC--the elements of f are random with uniform distribution[39;49;00m
[37mC--from -anorm/bnorm to +anorm/bnorm[39;49;00m
[37mC--note that f is not explicitly stored as a matrix[39;49;00m
[37mC--pathalogical floating point notes:  the if (bnorm .gt. 0.d0)[39;49;00m
[37mC--test should actually be if (bnorm .gt. dsmall), where dsmall[39;49;00m
[37mC--is the smallest representable number whose reciprocal does[39;49;00m
[37mC--not generate an overflow or loss of precision.[39;49;00m
[37mC[39;49;00m
      [37m  [39;49;00m[34mIF[39;49;00m[37m [39;49;00m(ISEED[37m [39;49;00m.EQ.[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00mISEED[37m [39;49;00m=[37m [39;49;00m[34m86345823[39;49;00m[37m[39;49;00m
      [37m  [39;49;00m[34mIF[39;49;00m[37m [39;49;00m(ANORM[37m [39;49;00m.EQ.[37m [39;49;00m[34m0.D0[39;49;00m)[37m [39;49;00mANORM[37m [39;49;00m=[37m [39;49;00m[34m1.D0[39;49;00m[37m[39;49;00m
      [37m  [39;49;00m[34mIF[39;49;00m[37m [39;49;00m(BNORM[37m [39;49;00m.GT.[37m [39;49;00m[34m0.D0[39;49;00m)[37m [39;49;00m[34mTHEN[39;49;00m[37m[39;49;00m
      [37m    [39;49;00mTEMP[37m [39;49;00m=[37m [39;49;00m[34m2.D0[39;49;00m[37m [39;49;00m*[37m [39;49;00mANORM[37m [39;49;00m/[37m [39;49;00mBNORM[37m[39;49;00m
      [37m  [39;49;00m[34mELSE[39;49;00m[37m[39;49;00m
      [37m    [39;49;00mTEMP[37m [39;49;00m=[37m [39;49;00m[34m2.D0[39;49;00m[37m[39;49;00m
      [37m  [39;49;00m[34mEND [39;49;00m[34mIF[39;49;00m[37m[39;49;00m
      [37m  [39;49;00m[34mDO [39;49;00m[34m190[39;49;00m[37m [39;49;00mK[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00mM[37m[39;49;00m
      [37m    [39;49;00m[34mDO [39;49;00m[34m180[39;49;00m[37m [39;49;00mJ[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00mN[37m[39;49;00m
      [37m      [39;49;00m[34mCALL [39;49;00m[36mRAND[39;49;00m(ISEED,ISEED,RNDMNO)[37m[39;49;00m
      [37m      [39;49;00m[34mVALUE[39;49;00m[37m [39;49;00m=[37m [39;49;00m(RNDMNO[37m [39;49;00m-[37m [39;49;00m[34m0.5D0[39;49;00m)[37m [39;49;00m*[37m [39;49;00mTEMP[37m[39;49;00m
      [37m      [39;49;00m[34mDO [39;49;00m[34m170[39;49;00m[37m [39;49;00mI[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00mN[37m[39;49;00m
      [37m        [39;49;00mWORK(I,J)[37m [39;49;00m=[37m [39;49;00mWORK(I,J)[37m [39;49;00m+[37m [39;49;00mB(I,K)*[34mVALUE[39;49;00m[37m[39;49;00m
170   [37m      [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m
180   [37m    [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m
190   [37m  [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m
[37mC[39;49;00m
[37mC--compute the eigenvalues of a + b*f, and several other things[39;49;00m
[37mC[39;49;00m
      [37m  [39;49;00m[34mCALL [39;49;00mEIGEN[37m [39;49;00m([34m0[39;49;00m,SIZE,N,WORK,CLEVR,CLEVI,WORK,SCR1,SCR2,IERR)[37m[39;49;00m
      [37m  [39;49;00m[34mIF[39;49;00m[37m [39;49;00m(IERR[37m [39;49;00m.NE.[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mRETURN[39;49;00m[37m[39;49;00m
[37mC[39;49;00m
[37mC--copy a so it is not destroyed[39;49;00m
[37mC[39;49;00m
      [37m  [39;49;00m[34mDO [39;49;00m[34m210[39;49;00m[37m [39;49;00mJ[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00mN[37m[39;49;00m
      [37m    [39;49;00m[34mDO [39;49;00m[34m200[39;49;00m[37m [39;49;00mI[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00mN[37m[39;49;00m
      [37m      [39;49;00mWORK(I,J)[37m [39;49;00m=[37m [39;49;00mA(I,J)[37m[39;49;00m
200   [37m    [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m
210   [37m  [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m
[37mC[39;49;00m
[37mC--compute the eigenvalues of a, and several other things[39;49;00m
[37mC[39;49;00m
      [37m  [39;49;00m[34mCALL [39;49;00mEIGEN[37m [39;49;00m([34m0[39;49;00m,SIZE,N,WORK,OLEVR,OLEVI,WORK,SCR1,SCR2,IERR)[37m[39;49;00m
      [37m  [39;49;00m[34mIF[39;49;00m[37m [39;49;00m(IERR[37m [39;49;00m.NE.[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mRETURN[39;49;00m[37m[39;49;00m
[37mC[39;49;00m
[37mC--form the matrix of distances between eigenvalues of a and[39;49;00m
[37mC--EIGENVALUES OF A+B*F[39;49;00m
[37mC[39;49;00m
      [37m  [39;49;00m[34mDO [39;49;00m[34m230[39;49;00m[37m [39;49;00mJ[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00mN[37m[39;49;00m
      [37m    [39;49;00m[34mDO [39;49;00m[34m220[39;49;00m[37m [39;49;00mI[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00mN[37m[39;49;00m
      [37m      [39;49;00mWORK(I,J)[37m [39;49;00m=[37m[39;49;00m
     &[37m        [39;49;00m[36mABS[39;49;00m(DCMPLX(OLEVR(I),OLEVI(I))-DCMPLX(CLEVR(J),CLEVI(J)))[37m[39;49;00m
220   [37m    [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m
230   [37m  [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m
[37mC[39;49;00m
[37mC--initialize row and column pivots[39;49;00m
[37mC[39;49;00m
      [37m  [39;49;00m[34mDO [39;49;00m[34m240[39;49;00m[37m [39;49;00mI[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00mN[37m[39;49;00m
      [37m    [39;49;00mIPVT(I)[37m [39;49;00m=[37m [39;49;00mI[37m[39;49;00m
      [37m    [39;49;00mJPVT(I)[37m [39;49;00m=[37m [39;49;00mI[37m[39;49;00m
240   [37m  [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m
[37mC[39;49;00m
[37mC--a little bit messy to avoid swapping columns and[39;49;00m
[37mC--rows of work[39;49;00m
[37mC[39;49;00m
      [37m  [39;49;00m[34mDO [39;49;00m[34m270[39;49;00m[37m [39;49;00mI[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00mN-[34m1[39;49;00m[37m[39;49;00m
[37mC[39;49;00m
[37mC--find the minimum element of each lower right square[39;49;00m
[37mC--submatrix of work, for submatrices of size n x n[39;49;00m
[37mC--through 2 x 2[39;49;00m
[37mC[39;49;00m
      [37m    [39;49;00mCURR[37m [39;49;00m=[37m [39;49;00mWORK(IPVT(I),JPVT(I))[37m[39;49;00m
      [37m    [39;49;00mIMAX[37m [39;49;00m=[37m [39;49;00mI[37m[39;49;00m
      [37m    [39;49;00mJMAX[37m [39;49;00m=[37m [39;49;00mI[37m[39;49;00m
      [37m    [39;49;00mTEMP[37m [39;49;00m=[37m [39;49;00mCURR[37m[39;49;00m
[37mC[39;49;00m
[37mC--find the minimum element[39;49;00m
[37mC[39;49;00m
      [37m    [39;49;00m[34mDO [39;49;00m[34m260[39;49;00m[37m [39;49;00mK1[37m [39;49;00m=[37m [39;49;00mI,[37m [39;49;00mN[37m[39;49;00m
      [37m      [39;49;00m[34mDO [39;49;00m[34m250[39;49;00m[37m [39;49;00mK2[37m [39;49;00m=[37m [39;49;00mI,[37m [39;49;00mN[37m[39;49;00m
      [37m        [39;49;00m[34mIF[39;49;00m[37m [39;49;00m(WORK(IPVT(K1),JPVT(K2))[37m [39;49;00m.LT.[37m [39;49;00mTEMP)[37m [39;49;00m[34mTHEN[39;49;00m[37m[39;49;00m
      [37m          [39;49;00mTEMP[37m [39;49;00m=[37m [39;49;00mWORK(IPVT(K1),JPVT(K2))[37m[39;49;00m
      [37m          [39;49;00mIMAX[37m [39;49;00m=[37m [39;49;00mK1[37m[39;49;00m
      [37m          [39;49;00mJMAX[37m [39;49;00m=[37m [39;49;00mK2[37m[39;49;00m
      [37m        [39;49;00m[34mEND [39;49;00m[34mIF[39;49;00m[37m[39;49;00m
250   [37m      [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m
260   [37m    [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m
[37mC[39;49;00m
[37mC--update row and column pivots for indirect addressing of work[39;49;00m
[37mC[39;49;00m
      [37m    [39;49;00mITEMP[37m [39;49;00m=[37m [39;49;00mIPVT(I)[37m[39;49;00m
      [37m    [39;49;00mIPVT(I)[37m [39;49;00m=[37m [39;49;00mIPVT(IMAX)[37m[39;49;00m
      [37m    [39;49;00mIPVT(IMAX)[37m [39;49;00m=[37m [39;49;00mITEMP[37m[39;49;00m
[37mC[39;49;00m
      [37m    [39;49;00mITEMP[37m [39;49;00m=[37m [39;49;00mJPVT(I)[37m[39;49;00m
      [37m    [39;49;00mJPVT(I)[37m [39;49;00m=[37m [39;49;00mJPVT(JMAX)[37m[39;49;00m
      [37m    [39;49;00mJPVT(JMAX)[37m [39;49;00m=[37m [39;49;00mITEMP[37m[39;49;00m
[37mC[39;49;00m
[37mC--do next submatrix[39;49;00m
[37mC[39;49;00m
270   [37m  [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m
[37mC[39;49;00m
[37mC--this threshold for determining when an eigenvalue has[39;49;00m
[37mC--not moved, and is therefore uncontrollable, is critical,[39;49;00m
[37mC--and may require future changes with more experience.[39;49;00m
[37mC[39;49;00m
      [37m  [39;49;00mEPS1[37m [39;49;00m=[37m [39;49;00m[36mSQRT[39;49;00m(EPS)[37m[39;49;00m
[37mC[39;49;00m
[37mC--for each eigenvalue pair, decide if it is controllable[39;49;00m
[37mC[39;49;00m
      [37m  [39;49;00m[34mDO [39;49;00m[34m280[39;49;00m[37m [39;49;00mI[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00mN[37m[39;49;00m
[37mC[39;49;00m
[37mC--note that we are working with the "pivoted" work matrix[39;49;00m
[37mC--and are looking at its diagonal elements[39;49;00m
[37mC[39;49;00m
      [37m    [39;49;00m[34mIF[39;49;00m[37m [39;49;00m(WORK(IPVT(I),JPVT(I))/ANORM[37m [39;49;00m.LE.[37m [39;49;00mEPS1)[37m [39;49;00m[34mTHEN[39;49;00m[37m[39;49;00m
      [37m      [39;49;00mCON(I)[37m [39;49;00m=[37m [39;49;00m.FALSE.[37m[39;49;00m
      [37m    [39;49;00m[34mELSE[39;49;00m[37m[39;49;00m
      [37m      [39;49;00mCON(I)[37m [39;49;00m=[37m [39;49;00m.TRUE.[37m[39;49;00m
      [37m    [39;49;00m[34mEND [39;49;00m[34mIF[39;49;00m[37m[39;49;00m
280   [37m  [39;49;00m[34mCONTINUE[39;49;00m[37m[39;49;00m
[37mC[39;49;00m
[37mC--finally![39;49;00m
[37mC[39;49;00m
      [37m  [39;49;00m[34mRETURN[39;49;00m[37m[39;49;00m
        END

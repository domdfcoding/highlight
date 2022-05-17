     1	[37m!!$[39;49;00m
     2	[37m!!$[39;49;00m
     3	[37m!!$                    MD2P4[39;49;00m
     4	[37m!!$    Multilevel Domain Decomposition Parallel Preconditioner Package for PSBLAS[39;49;00m
     5	[37m!!$                      for[39;49;00m
     6	[37m!!$              Parallel Sparse BLAS  v2.0[39;49;00m
     7	[37m!!$    (C) Copyright 2006 Salvatore Filippone    University of Rome Tor Vergata[39;49;00m
     8	[37m!!$                       Alfredo Buttari        University of Rome Tor Vergata[39;49;00m
     9	[37m!!$                       Daniela Di Serafino    II University of Naples[39;49;00m
    10	[37m!!$                       Pasqua D'Ambra         ICAR-CNR[39;49;00m
    11	[37m!!$[39;49;00m
    12	[37m!!$  Redistribution and use in source and binary forms, with or without[39;49;00m
    13	[37m!!$  modification, are permitted provided that the following conditions[39;49;00m
    14	[37m!!$  are met:[39;49;00m
    15	[37m!!$    1. Redistributions of source code must retain the above copyright[39;49;00m
    16	[37m!!$       notice, this list of conditions and the following disclaimer.[39;49;00m
    17	[37m!!$    2. Redistributions in binary form must reproduce the above copyright[39;49;00m
    18	[37m!!$       notice, this list of conditions, and the following disclaimer in the[39;49;00m
    19	[37m!!$       documentation and/or other materials provided with the distribution.[39;49;00m
    20	[37m!!$    3. The name of the MD2P4 group or the names of its contributors may[39;49;00m
    21	[37m!!$       not be used to endorse or promote products derived from this[39;49;00m
    22	[37m!!$       software without specific written permission.[39;49;00m
    23	[37m!!$[39;49;00m
    24	[37m!!$  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS[39;49;00m
    25	[37m!!$  ``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED[39;49;00m
    26	[37m!!$  TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR[39;49;00m
    27	[37m!!$  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE MD2P4 GROUP OR ITS CONTRIBUTORS[39;49;00m
    28	[37m!!$  BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR[39;49;00m
    29	[37m!!$  CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF[39;49;00m
    30	[37m!!$  SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS[39;49;00m
    31	[37m!!$  INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN[39;49;00m
    32	[37m!!$  CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)[39;49;00m
    33	[37m!!$  ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE[39;49;00m
    34	[37m!!$  POSSIBILITY OF SUCH DAMAGE.[39;49;00m
    35	[37m!!$[39;49;00m
    36	[37m!!$[39;49;00m
    37	[34msubroutine [39;49;00mpsb_zmlprc_aply(alpha,baseprecv,x,beta,y,desc_data,trans,work,info)[37m[39;49;00m
    38	[37m  [39;49;00m[37m![39;49;00m
    39	[37m  [39;49;00m[37m!  Compute   Y <-  beta*Y + alpha*K^-1 X[39;49;00m
    40	[37m  [39;49;00m[37m!  where K is a multilevel  preconditioner stored in baseprecv[39;49;00m
    41	[37m  [39;49;00m[37m![39;49;00m
    42	[37m  [39;49;00m[37m!  cfr.: Smith, Biorstad & Gropp[39;49;00m
    43	[37m  [39;49;00m[37m!        Domain Decomposition[39;49;00m
    44	[37m  [39;49;00m[37m!        Cambridge Univ. Press[39;49;00m
    45	[37m  [39;49;00m[37m![39;49;00m
    46	[37m  [39;49;00m[37m!  To each level I there corresponds a matrix A(I) and a preconditioner K(I)[39;49;00m
    47	[37m  [39;49;00m[37m![39;49;00m
    48	[37m  [39;49;00m[37m!  A notational difference: in the DD reference above the preconditioner for[39;49;00m
    49	[37m  [39;49;00m[37m!  a given level K(I) is written out as a sum over the subdomains[39;49;00m
    50	[37m  [39;49;00m[37m![39;49;00m
    51	[37m  [39;49;00m[37m!  SUM_k(R_k^T A_k R_k)[39;49;00m
    52	[37m  [39;49;00m[37m![39;49;00m
    53	[37m  [39;49;00m[37m!  whereas in this code the sum is implicit in the parallelization,[39;49;00m
    54	[37m  [39;49;00m[37m!  i.e. each process takes care of one subdomain, and for each level we have[39;49;00m
    55	[37m  [39;49;00m[37m!  as many subdomains as there are processes (except for the coarsest level where[39;49;00m
    56	[37m  [39;49;00m[37m!  we might have a replicated index space). Thus the sum apparently disappears[39;49;00m
    57	[37m  [39;49;00m[37m!  from our code, but only apparently, because it is implicit in the call[39;49;00m
    58	[37m  [39;49;00m[37m!  to psb_baseprc_aply.[39;49;00m
    59	[37m  [39;49;00m[37m![39;49;00m
    60	[37m  [39;49;00m[37m!  A bit of description of the baseprecv(:) data structure:[39;49;00m
    61	[37m  [39;49;00m[37m!   1. Number of levels = NLEV = size(baseprecv(:))[39;49;00m
    62	[37m  [39;49;00m[37m!   2. baseprecv(ilev)%av(:)    sparse matrices needed for the current level.[39;49;00m
    63	[37m  [39;49;00m[37m!      Includes:[39;49;00m
    64	[37m  [39;49;00m[37m!   2.1.:  baseprecv(ilev)%av(l_pr_)    L factor of ILU preconditioners[39;49;00m
    65	[37m  [39;49;00m[37m!   2.2.:  baseprecv(ilev)%av(u_pr_)    U factor of ILU preconditioners[39;49;00m
    66	[37m  [39;49;00m[37m!   2.3.:  baseprecv(ilev)%av(ap_nd_)   Off-diagonal part of A for Jacobi sweeps[39;49;00m
    67	[37m  [39;49;00m[37m!   2.4.:  baseprecv(ilev)%av(ac_)      Aggregated matrix of level ILEV[39;49;00m
    68	[37m  [39;49;00m[37m!   2.5.:  baseprecv(ilev)%av(sm_pr_t_) Smoother prolongator transpose; maps vectors[39;49;00m
    69	[37m  [39;49;00m[37m!                                          (ilev-1) --->  (ilev)[39;49;00m
    70	[37m  [39;49;00m[37m!   2.6.:  baseprecv(ilev)%av(sm_pr_)   Smoother prolongator; maps vectors[39;49;00m
    71	[37m  [39;49;00m[37m!                                          (ilev)   --->  (ilev-1)[39;49;00m
    72	[37m  [39;49;00m[37m!   Shouldn't we keep just one of them and handle transpose in the sparse BLAS? maybe[39;49;00m
    73	[37m  [39;49;00m[37m![39;49;00m
    74	[37m  [39;49;00m[37m!   3.    baseprecv(ilev)%desc_data     comm descriptor for level ILEV[39;49;00m
    75	[37m  [39;49;00m[37m!   4.    baseprecv(ilev)%base_a        Pointer (really a pointer!) to the base matrix[39;49;00m
    76	[37m  [39;49;00m[37m!                                       of the current level, i.e.: if ILEV=1 then  A[39;49;00m
    77	[37m  [39;49;00m[37m!                                       else the aggregated matrix av(ac_); so we have[39;49;00m
    78	[37m  [39;49;00m[37m!                                       a unified treatment of residuals. Need this to[39;49;00m
    79	[37m  [39;49;00m[37m!                                       avoid passing explicitly matrix A to the[39;49;00m
    80	[37m  [39;49;00m[37m!                                       outer prec. routine[39;49;00m
    81	[37m  [39;49;00m[37m!   5.    baseprecv(ilev)%mlia          The aggregation map from (ilev-1)-->(ilev)[39;49;00m
    82	[37m  [39;49;00m[37m!                                       if no smoother, it is used instead of sm_pr_[39;49;00m
    83	[37m  [39;49;00m[37m!   6.    baseprecv(ilev)%nlaggr        Number of aggregates on the various procs.[39;49;00m
    84	[37m  [39;49;00m[37m![39;49;00m
    85	[37m[39;49;00m
    86	[37m  [39;49;00m[34muse [39;49;00mpsb_serial_mod[37m[39;49;00m
    87	[37m  [39;49;00m[34muse [39;49;00mpsb_descriptor_type[37m[39;49;00m
    88	[37m  [39;49;00m[34muse [39;49;00mpsb_prec_type[37m[39;49;00m
    89	[37m  [39;49;00m[34muse [39;49;00mpsb_psblas_mod[37m[39;49;00m
    90	[37m  [39;49;00m[34muse [39;49;00mpsb_penv_mod[37m[39;49;00m
    91	[37m  [39;49;00m[34muse [39;49;00mpsb_const_mod[37m[39;49;00m
    92	[37m  [39;49;00m[34muse [39;49;00mpsb_error_mod[37m[39;49;00m
    93	[37m  [39;49;00m[34muse [39;49;00mpsb_penv_mod[37m[39;49;00m
    94	[37m  [39;49;00m[34mimplicit [39;49;00m[34mnone[39;49;00m
    95	[34m[39;49;00m
    96	[34m  [39;49;00m[34mtype[39;49;00m(psb_desc_type),[34mintent[39;49;00m(in)[37m      [39;49;00m[34m::[39;49;00m[37m [39;49;00mdesc_data[37m[39;49;00m
    97	[37m  [39;49;00m[34mtype[39;49;00m(psb_zbaseprc_type),[37m [39;49;00m[34mintent[39;49;00m(in)[37m [39;49;00m[34m::[39;49;00m[37m [39;49;00mbaseprecv(:)[37m[39;49;00m
    98	[37m  [39;49;00m[36mcomplex[39;49;00m([36mkind[39;49;00m([34m1.d0[39;49;00m)),[34mintent[39;49;00m(in)[37m      [39;49;00m[34m::[39;49;00m[37m [39;49;00malpha,beta[37m[39;49;00m
    99	[37m  [39;49;00m[36mcomplex[39;49;00m([36mkind[39;49;00m([34m1.d0[39;49;00m)),[34mintent[39;49;00m(inout)[37m   [39;49;00m[34m::[39;49;00m[37m [39;49;00mx(:),[37m [39;49;00my(:)[37m[39;49;00m
   100	[37m  [39;49;00m[36mcharacter[39;49;00m[37m                           [39;49;00m[34m::[39;49;00m[37m [39;49;00mtrans[37m[39;49;00m
   101	[37m  [39;49;00m[36mcomplex[39;49;00m([36mkind[39;49;00m([34m1.d0[39;49;00m)),[34mtarget[39;49;00m[37m          [39;49;00m[34m::[39;49;00m[37m [39;49;00mwork(:)[37m[39;49;00m
   102	[37m  [39;49;00m[36minteger[39;49;00m,[37m [39;49;00m[34mintent[39;49;00m(out)[37m                [39;49;00m[34m::[39;49;00m[37m [39;49;00minfo[37m[39;49;00m
   103	[37m[39;49;00m
   104	[37m[39;49;00m
   105	[37m  [39;49;00m[37m! Local variables[39;49;00m
   106	[37m  [39;49;00m[36minteger[39;49;00m[37m [39;49;00m[34m::[39;49;00m[37m [39;49;00mn_row,n_col[37m[39;49;00m
   107	[37m  [39;49;00m[36mcomplex[39;49;00m([36mkind[39;49;00m([34m1.d0[39;49;00m)),[37m [39;49;00m[34mallocatable[39;49;00m[37m [39;49;00m[34m::[39;49;00m[37m [39;49;00mtx(:),ty(:),t2l(:),w2l(:),&[37m[39;49;00m
   108	[37m       [39;49;00m&[37m   [39;49;00mx2l(:),b2l(:),tz(:),tty(:)[37m[39;49;00m
   109	[37m  [39;49;00m[36mcharacter[39;49;00m[37m     [39;49;00m[34m::[39;49;00mdiagl,[37m [39;49;00mdiagu[37m[39;49;00m
   110	[37m  [39;49;00m[36minteger[39;49;00m[37m [39;49;00m[34m::[39;49;00m[37m [39;49;00mictxt,np,me,i,[37m [39;49;00misz,[37m [39;49;00mnrg,nr2l,err_act,[37m [39;49;00miptype,[37m [39;49;00mint_err([34m5[39;49;00m)[37m[39;49;00m
   111	[37m  [39;49;00m[36mreal[39;49;00m([36mkind[39;49;00m([34m1.d0[39;49;00m))[37m [39;49;00m[34m::[39;49;00m[37m [39;49;00momega[37m[39;49;00m
   112	[37m  [39;49;00m[36mreal[39;49;00m([36mkind[39;49;00m([34m1.d0[39;49;00m))[37m [39;49;00m[34m::[39;49;00m[37m [39;49;00mt1,[37m [39;49;00mt2,[37m [39;49;00mt3,[37m [39;49;00mt4,[37m [39;49;00mt5,[37m [39;49;00mt6,[37m [39;49;00mt7,[37m [39;49;00mmpi_wtime[37m[39;49;00m
   113	[37m  [39;49;00m[36mlogical[39;49;00m,[37m [39;49;00m[34mparameter[39;49;00m[37m          [39;49;00m[34m::[39;49;00m[37m [39;49;00mdebug=.false.,[37m [39;49;00mdebugprt=.false.[37m[39;49;00m
   114	[37m  [39;49;00m[36minteger[39;49;00m[37m      [39;49;00m[34m::[39;49;00m[37m [39;49;00mismth,[37m [39;49;00mnlev,[37m [39;49;00milev[37m[39;49;00m
   115	[37m  [39;49;00m[34mexternal [39;49;00mmpi_wtime[37m[39;49;00m
   116	[37m  [39;49;00m[36mcharacter[39;49;00m([36mlen[39;49;00m=[34m20[39;49;00m)[37m   [39;49;00m[34m::[39;49;00m[37m [39;49;00mname,[37m [39;49;00mch_err[37m[39;49;00m
   117	[37m[39;49;00m
   118	[37m  [39;49;00m[34mtype [39;49;00mpsb_mlprec_wrk_type[37m[39;49;00m
   119	[37m    [39;49;00m[36mcomplex[39;49;00m([36mkind[39;49;00m([34m1.d0[39;49;00m)),[37m [39;49;00m[34mpointer[39;49;00m[37m [39;49;00m[34m::[39;49;00m[37m [39;49;00mtx(:)=>[36mnull[39;49;00m(),ty(:)=>[36mnull[39;49;00m(),&[37m[39;49;00m
   120	[37m         [39;49;00m&[37m [39;49;00mx2l(:)=>[36mnull[39;49;00m(),y2l(:)=>[36mnull[39;49;00m(),&[37m[39;49;00m
   121	[37m         [39;49;00m&[37m [39;49;00mb2l(:)=>[36mnull[39;49;00m(),tty(:)=>[36mnull[39;49;00m()[37m[39;49;00m
   122	[37m  [39;49;00m[34mend [39;49;00m[34mtype [39;49;00mpsb_mlprec_wrk_type[37m[39;49;00m
   123	[37m  [39;49;00m[34mtype[39;49;00m(psb_mlprec_wrk_type),[37m [39;49;00m[34mpointer[39;49;00m[37m [39;49;00m[34m::[39;49;00m[37m [39;49;00mmlprec_wrk(:)[37m[39;49;00m
   124	[37m[39;49;00m
   125	[37m  [39;49;00m[34minterface [39;49;00mpsb_baseprc_aply[37m[39;49;00m
   126	[37m    [39;49;00m[34msubroutine [39;49;00mpsb_zbaseprc_aply(alpha,prec,x,beta,y,desc_data,trans,work,info)[37m[39;49;00m
   127	[37m      [39;49;00m[34muse [39;49;00mpsb_descriptor_type[37m[39;49;00m
   128	[37m      [39;49;00m[34muse [39;49;00mpsb_prec_type[37m[39;49;00m
   129	[37m      [39;49;00m[34mtype[39;49;00m(psb_desc_type),[34mintent[39;49;00m(in)[37m      [39;49;00m[34m::[39;49;00m[37m [39;49;00mdesc_data[37m[39;49;00m
   130	[37m      [39;49;00m[34mtype[39;49;00m(psb_zbaseprc_type),[37m [39;49;00m[34mintent[39;49;00m(in)[37m [39;49;00m[34m::[39;49;00m[37m [39;49;00mprec[37m[39;49;00m
   131	[37m      [39;49;00m[36mcomplex[39;49;00m([36mkind[39;49;00m([34m1.d0[39;49;00m)),[34mintent[39;49;00m(inout)[37m   [39;49;00m[34m::[39;49;00m[37m [39;49;00mx(:),[37m [39;49;00my(:)[37m[39;49;00m
   132	[37m      [39;49;00m[36mcomplex[39;49;00m([36mkind[39;49;00m([34m1.d0[39;49;00m)),[34mintent[39;49;00m(in)[37m      [39;49;00m[34m::[39;49;00m[37m [39;49;00malpha,beta[37m[39;49;00m
   133	[37m      [39;49;00m[36mcharacter[39;49;00m([36mlen[39;49;00m=[34m1[39;49;00m)[37m                    [39;49;00m[34m::[39;49;00m[37m [39;49;00mtrans[37m[39;49;00m
   134	[37m      [39;49;00m[36mcomplex[39;49;00m([36mkind[39;49;00m([34m1.d0[39;49;00m)),[34mtarget[39;49;00m[37m          [39;49;00m[34m::[39;49;00m[37m [39;49;00mwork(:)[37m[39;49;00m
   135	[37m      [39;49;00m[36minteger[39;49;00m,[37m [39;49;00m[34mintent[39;49;00m(out)[37m                [39;49;00m[34m::[39;49;00m[37m [39;49;00minfo[37m[39;49;00m
   136	[37m    [39;49;00m[34mend [39;49;00m[34msubroutine [39;49;00mpsb_zbaseprc_aply[37m[39;49;00m
   137	[37m  [39;49;00m[34mend [39;49;00m[34minterface[39;49;00m
   138	[34m[39;49;00m
   139	[34m  [39;49;00mname=[33m'psb_mlprc_aply'[39;49;00m[37m[39;49;00m
   140	[37m  [39;49;00minfo[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m[37m[39;49;00m
   141	[37m  [39;49;00m[34mcall [39;49;00mpsb_erractionsave(err_act)[37m[39;49;00m
   142	[37m[39;49;00m
   143	[37m[39;49;00m
   144	[37m  [39;49;00mictxt=desc_data%matrix_data(psb_ctxt_)[37m[39;49;00m
   145	[37m  [39;49;00m[34mcall [39;49;00mpsb_info(ictxt,[37m [39;49;00mme,[37m [39;49;00mnp)[37m[39;49;00m
   146	[37m[39;49;00m
   147	[37m  [39;49;00mnlev[37m [39;49;00m=[37m [39;49;00msize(baseprecv)[37m[39;49;00m
   148	[37m  [39;49;00m[34mallocate[39;49;00m(mlprec_wrk(nlev),[36mstat[39;49;00m=info)[37m[39;49;00m
   149	[37m  [39;49;00m[34mif[39;49;00m[37m [39;49;00m(info[37m [39;49;00m/=[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mthen[39;49;00m
   150	[34m    [39;49;00m[34mcall [39;49;00mpsb_errpush([34m4010[39;49;00m,name,a_err=[33m'Allocate'[39;49;00m)[37m[39;49;00m
   151	[37m    [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
   152	[37m  [39;49;00m[34mend [39;49;00m[34mif[39;49;00m
   153	[34m[39;49;00m
   154	[34m[39;49;00m
   155	[34m  [39;49;00m[34mselect [39;49;00m[34mcase[39;49;00m(baseprecv([34m2[39;49;00m)%iprcparm(ml_type_))[37m[39;49;00m
   156	[37m[39;49;00m
   157	[37m  [39;49;00m[34mcase[39;49;00m(no_ml_)[37m[39;49;00m
   158	[37m    [39;49;00m[37m! Should not really get here.[39;49;00m
   159	[37m    [39;49;00m[34mcall [39;49;00mpsb_errpush([34m4010[39;49;00m,name,a_err=[33m'no_ml_ in mlprc_aply?'[39;49;00m)[37m[39;49;00m
   160	[37m    [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
   161	[37m[39;49;00m
   162	[37m[39;49;00m
   163	[37m  [39;49;00m[34mcase[39;49;00m(add_ml_prec_)[37m[39;49;00m
   164	[37m[39;49;00m
   165	[37m[39;49;00m
   166	[37m    [39;49;00m[37m![39;49;00m
   167	[37m    [39;49;00m[37m!    Additive is very simple.[39;49;00m
   168	[37m    [39;49;00m[37m!    1.  X(1) = Xext[39;49;00m
   169	[37m    [39;49;00m[37m!    2.  DO ILEV=2,NLEV[39;49;00m
   170	[37m    [39;49;00m[37m!           X(ILEV) = AV(PR_SM_T_)*X(ILEV-1)[39;49;00m
   171	[37m    [39;49;00m[37m!    3.  Y(ILEV) = (K(ILEV)**(-1))*X(ILEV)[39;49;00m
   172	[37m    [39;49;00m[37m!    4.  DO  ILEV=NLEV-1,1,-1[39;49;00m
   173	[37m    [39;49;00m[37m!           Y(ILEV) = AV(PR_SM_)*Y(ILEV+1)[39;49;00m
   174	[37m    [39;49;00m[37m!    5.  Yext    = beta*Yext + Y(1)[39;49;00m
   175	[37m    [39;49;00m[37m![39;49;00m
   176	[37m    [39;49;00m[37m!    Note: level numbering reversed wrt ref. DD, i.e.[39;49;00m
   177	[37m    [39;49;00m[37m!         1..NLEV <=>  (j) <-> 0[39;49;00m
   178	[37m[39;49;00m
   179	[37m[39;49;00m
   180	[37m    [39;49;00m[34mcall [39;49;00mpsb_baseprc_aply(alpha,baseprecv([34m1[39;49;00m),x,beta,y,&[37m[39;49;00m
   181	[37m         [39;49;00m&[37m [39;49;00mbaseprecv([34m1[39;49;00m)%base_desc,trans,work,info)[37m[39;49;00m
   182	[37m    [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
   183	[37m    [39;49;00m[34mallocate[39;49;00m(mlprec_wrk([34m1[39;49;00m)%x2l(size(x)),mlprec_wrk([34m1[39;49;00m)%y2l(size(y)))[37m[39;49;00m
   184	[37m    [39;49;00mmlprec_wrk([34m1[39;49;00m)%x2l(:)[37m [39;49;00m=[37m [39;49;00mx(:)[37m[39;49;00m
   185	[37m[39;49;00m
   186	[37m[39;49;00m
   187	[37m    [39;49;00m[34mdo [39;49;00milev[37m [39;49;00m=[37m [39;49;00m[34m2[39;49;00m,[37m [39;49;00mnlev[37m[39;49;00m
   188	[37m      [39;49;00mn_row[37m [39;49;00m=[37m [39;49;00mbaseprecv(ilev-[34m1[39;49;00m)%base_desc%matrix_data(psb_n_row_)[37m[39;49;00m
   189	[37m      [39;49;00mn_col[37m [39;49;00m=[37m [39;49;00mbaseprecv(ilev-[34m1[39;49;00m)%desc_data%matrix_data(psb_n_col_)[37m[39;49;00m
   190	[37m      [39;49;00mnr2l[37m  [39;49;00m=[37m [39;49;00mbaseprecv(ilev)%desc_data%matrix_data(psb_n_col_)[37m[39;49;00m
   191	[37m      [39;49;00mnrg[37m   [39;49;00m=[37m [39;49;00mbaseprecv(ilev)%desc_data%matrix_data(psb_n_row_)[37m[39;49;00m
   192	[37m      [39;49;00m[34mallocate[39;49;00m(mlprec_wrk(ilev)%x2l(nr2l),mlprec_wrk(ilev)%y2l(nr2l),&[37m[39;49;00m
   193	[37m           [39;49;00m&[37m [39;49;00mmlprec_wrk(ilev)%tx([36mmax[39;49;00m(n_row,n_col)),&[37m[39;49;00m
   194	[37m           [39;49;00m&[37m [39;49;00mmlprec_wrk(ilev)%ty([36mmax[39;49;00m(n_row,n_col)),[37m [39;49;00m[36mstat[39;49;00m=info)[37m[39;49;00m
   195	[37m      [39;49;00m[34mif[39;49;00m[37m [39;49;00m(info[37m [39;49;00m/=[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mthen[39;49;00m
   196	[34m        [39;49;00m[34mcall [39;49;00mpsb_errpush([34m4010[39;49;00m,name,a_err=[33m'Allocate'[39;49;00m)[37m[39;49;00m
   197	[37m        [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
   198	[37m      [39;49;00m[34mend [39;49;00m[34mif[39;49;00m
   199	[34m[39;49;00m
   200	[34m      [39;49;00mmlprec_wrk(ilev)%x2l(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
   201	[37m      [39;49;00mmlprec_wrk(ilev)%y2l(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
   202	[37m      [39;49;00mmlprec_wrk(ilev)%tx([34m1[39;49;00m:n_row)[37m [39;49;00m=[37m [39;49;00mmlprec_wrk(ilev-[34m1[39;49;00m)%x2l([34m1[39;49;00m:n_row)[37m[39;49;00m
   203	[37m      [39;49;00mmlprec_wrk(ilev)%tx(n_row+[34m1[39;49;00m:[36mmax[39;49;00m(n_row,n_col))[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
   204	[37m      [39;49;00mmlprec_wrk(ilev)%ty(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
   205	[37m[39;49;00m
   206	[37m      [39;49;00mismth=baseprecv(ilev)%iprcparm(smth_kind_)[37m[39;49;00m
   207	[37m[39;49;00m
   208	[37m      [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ismth[37m  [39;49;00m/=[37m [39;49;00mno_smth_)[37m [39;49;00m[34mthen[39;49;00m[37m[39;49;00m
   209	[37m        [39;49;00m[37m![39;49;00m
   210	[37m        [39;49;00m[37m! Smoothed aggregation[39;49;00m
   211	[37m        [39;49;00m[37m![39;49;00m
   212	[37m[39;49;00m
   213	[37m[39;49;00m
   214	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(baseprecv(ilev)%iprcparm(glb_smth_)[37m [39;49;00m>[34m0[39;49;00m)[37m [39;49;00m[34mthen[39;49;00m
   215	[34m          [39;49;00m[34mcall [39;49;00mpsb_halo(mlprec_wrk(ilev-[34m1[39;49;00m)%x2l,baseprecv(ilev-[34m1[39;49;00m)%base_desc,&[37m[39;49;00m
   216	[37m               [39;49;00m&[37m  [39;49;00minfo,work=work)[37m[39;49;00m
   217	[37m          [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
   218	[37m        [39;49;00m[34melse[39;49;00m
   219	[34m          [39;49;00mmlprec_wrk(ilev-[34m1[39;49;00m)%x2l(n_row+[34m1[39;49;00m:[36mmax[39;49;00m(n_row,n_col))[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
   220	[37m        [39;49;00m[34mend [39;49;00m[34mif[39;49;00m
   221	[34m[39;49;00m
   222	[34m        [39;49;00m[34mcall [39;49;00mpsb_csmm(zone,baseprecv(ilev)%av(sm_pr_t_),mlprec_wrk(ilev-[34m1[39;49;00m)%x2l,&[37m[39;49;00m
   223	[37m             [39;49;00m&[37m [39;49;00mzzero,mlprec_wrk(ilev)%x2l,info)[37m[39;49;00m
   224	[37m        [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
   225	[37m[39;49;00m
   226	[37m      [39;49;00m[34melse[39;49;00m[37m[39;49;00m
   227	[37m        [39;49;00m[37m![39;49;00m
   228	[37m        [39;49;00m[37m! Raw  aggregation, may take shortcut[39;49;00m
   229	[37m        [39;49;00m[37m![39;49;00m
   230	[37m        [39;49;00m[34mdo [39;49;00mi=[34m1[39;49;00m,n_row[37m[39;49;00m
   231	[37m          [39;49;00mmlprec_wrk(ilev)%x2l(baseprecv(ilev)%mlia(i))[37m [39;49;00m=[37m [39;49;00m&[37m[39;49;00m
   232	[37m               [39;49;00m&[37m  [39;49;00mmlprec_wrk(ilev)%x2l(baseprecv(ilev)%mlia(i))[37m [39;49;00m+[37m [39;49;00m&[37m[39;49;00m
   233	[37m               [39;49;00m&[37m  [39;49;00mmlprec_wrk(ilev-[34m1[39;49;00m)%x2l(i)[37m[39;49;00m
   234	[37m        [39;49;00m[34mend [39;49;00m[34mdo[39;49;00m
   235	[34m[39;49;00m
   236	[34m      [39;49;00m[34mend [39;49;00m[34mif[39;49;00m
   237	[34m[39;49;00m
   238	[34m      [39;49;00m[34mif[39;49;00m[37m [39;49;00m(baseprecv(ilev)%iprcparm(coarse_mat_)==mat_repl_)[37m [39;49;00m[34mThen[39;49;00m
   239	[34m        [39;49;00m[34mcall [39;49;00mpsb_sum(ictxt,mlprec_wrk(ilev)%x2l([34m1[39;49;00m:nrg))[37m[39;49;00m
   240	[37m      [39;49;00m[34melse [39;49;00m[34mif[39;49;00m[37m [39;49;00m(baseprecv(ilev)%iprcparm(coarse_mat_)[37m [39;49;00m/=[37m [39;49;00mmat_distr_)[37m [39;49;00m[34mThen[39;49;00m
   241	[34m        [39;49;00m[34mwrite[39;49;00m([34m0[39;49;00m,*)[37m [39;49;00m[33m'Unknown value for baseprecv(2)%iprcparm(coarse_mat_) '[39;49;00m,&[37m[39;49;00m
   242	[37m             [39;49;00m&[37m [39;49;00mbaseprecv(ilev)%iprcparm(coarse_mat_)[37m[39;49;00m
   243	[37m      [39;49;00m[34mendif[39;49;00m
   244	[34m[39;49;00m
   245	[34m      [39;49;00m[34mcall [39;49;00mpsb_baseprc_aply(zone,baseprecv(ilev),&[37m[39;49;00m
   246	[37m           [39;49;00m&[37m [39;49;00mmlprec_wrk(ilev)%x2l,zzero,mlprec_wrk(ilev)%y2l,&[37m[39;49;00m
   247	[37m           [39;49;00m&[37m [39;49;00mbaseprecv(ilev)%desc_data,[37m [39;49;00m[33m'N'[39;49;00m,work,info)[37m[39;49;00m
   248	[37m[39;49;00m
   249	[37m    [39;49;00m[34menddo[39;49;00m
   250	[34m[39;49;00m
   251	[34m    [39;49;00m[34mdo [39;49;00milev[37m [39;49;00m=nlev,[34m2[39;49;00m,-[34m1[39;49;00m[37m[39;49;00m
   252	[37m[39;49;00m
   253	[37m      [39;49;00mismth=baseprecv(ilev)%iprcparm(smth_kind_)[37m[39;49;00m
   254	[37m      [39;49;00mn_row[37m [39;49;00m=[37m [39;49;00mbaseprecv(ilev-[34m1[39;49;00m)%base_desc%matrix_data(psb_n_row_)[37m[39;49;00m
   255	[37m      [39;49;00mn_col[37m [39;49;00m=[37m [39;49;00mbaseprecv(ilev-[34m1[39;49;00m)%desc_data%matrix_data(psb_n_col_)[37m[39;49;00m
   256	[37m      [39;49;00mnr2l[37m  [39;49;00m=[37m [39;49;00mbaseprecv(ilev)%desc_data%matrix_data(psb_n_col_)[37m[39;49;00m
   257	[37m      [39;49;00mnrg[37m   [39;49;00m=[37m [39;49;00mbaseprecv(ilev)%desc_data%matrix_data(psb_n_row_)[37m[39;49;00m
   258	[37m[39;49;00m
   259	[37m      [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ismth[37m  [39;49;00m/=[37m [39;49;00mno_smth_)[37m [39;49;00m[34mthen[39;49;00m
   260	[34m[39;49;00m
   261	[34m        [39;49;00m[34mcall [39;49;00mpsb_csmm(zone,baseprecv(ilev)%av(sm_pr_),mlprec_wrk(ilev)%y2l,&[37m[39;49;00m
   262	[37m             [39;49;00m&[37m [39;49;00mzone,mlprec_wrk(ilev-[34m1[39;49;00m)%y2l,info)[37m[39;49;00m
   263	[37m        [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
   264	[37m[39;49;00m
   265	[37m      [39;49;00m[34melse[39;49;00m
   266	[34m[39;49;00m
   267	[34m        [39;49;00m[34mdo [39;49;00mi=[34m1[39;49;00m,[37m [39;49;00mn_row[37m[39;49;00m
   268	[37m          [39;49;00mmlprec_wrk(ilev-[34m1[39;49;00m)%y2l(i)[37m [39;49;00m=[37m [39;49;00mmlprec_wrk(ilev-[34m1[39;49;00m)%y2l(i)[37m [39;49;00m+[37m [39;49;00m&[37m[39;49;00m
   269	[37m               [39;49;00m&[37m   [39;49;00mmlprec_wrk(ilev)%y2l(baseprecv(ilev)%mlia(i))[37m[39;49;00m
   270	[37m        [39;49;00m[34menddo[39;49;00m
   271	[34m[39;49;00m
   272	[34m      [39;49;00m[34mend [39;49;00m[34mif[39;49;00m
   273	[34m    [39;49;00m[34mend [39;49;00m[34mdo[39;49;00m
   274	[34m[39;49;00m
   275	[34m    [39;49;00m[34mcall [39;49;00mpsb_geaxpby(alpha,mlprec_wrk([34m1[39;49;00m)%y2l,zone,y,baseprecv([34m1[39;49;00m)%base_desc,info)[37m[39;49;00m
   276	[37m    [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
   277	[37m[39;49;00m
   278	[37m[39;49;00m
   279	[37m  [39;49;00m[34mcase[39;49;00m(mult_ml_prec_)[37m[39;49;00m
   280	[37m[39;49;00m
   281	[37m    [39;49;00m[37m![39;49;00m
   282	[37m    [39;49;00m[37m!  Multiplicative multilevel[39;49;00m
   283	[37m    [39;49;00m[37m!  Pre/post smoothing versions.[39;49;00m
   284	[37m    [39;49;00m[37m![39;49;00m
   285	[37m[39;49;00m
   286	[37m    [39;49;00m[34mselect [39;49;00m[34mcase[39;49;00m(baseprecv([34m2[39;49;00m)%iprcparm(smth_pos_))[37m[39;49;00m
   287	[37m[39;49;00m
   288	[37m    [39;49;00m[34mcase[39;49;00m(post_smooth_)[37m[39;49;00m
   289	[37m[39;49;00m
   290	[37m[39;49;00m
   291	[37m      [39;49;00m[37m![39;49;00m
   292	[37m      [39;49;00m[37m!    Post smoothing.[39;49;00m
   293	[37m      [39;49;00m[37m!    1.   X(1) = Xext[39;49;00m
   294	[37m      [39;49;00m[37m!    2.   DO ILEV=2, NLEV :: X(ILEV) = AV(PR_SM_T_,ILEV)*X(ILEV-1)[39;49;00m
   295	[37m      [39;49;00m[37m!    3.   Y(NLEV) = (K(NLEV)**(-1))*X(NLEV)[39;49;00m
   296	[37m      [39;49;00m[37m!    4.   DO  ILEV=NLEV-1,1,-1[39;49;00m
   297	[37m      [39;49;00m[37m!          Y(ILEV) = AV(PR_SM_,ILEV+1)*Y(ILEV+1)[39;49;00m
   298	[37m      [39;49;00m[37m!          Y(ILEV) = Y(ILEV) + (K(ILEV)**(-1))*(X(ILEV)-A(ILEV)*Y(ILEV))[39;49;00m
   299	[37m      [39;49;00m[37m![39;49;00m
   300	[37m      [39;49;00m[37m!    5.  Yext    = beta*Yext + Y(1)[39;49;00m
   301	[37m      [39;49;00m[37m![39;49;00m
   302	[37m      [39;49;00m[37m!    Note: level numbering reversed wrt ref. DD, i.e.[39;49;00m
   303	[37m      [39;49;00m[37m!         1..NLEV <=>  (j) <-> 0[39;49;00m
   304	[37m      [39;49;00m[37m![39;49;00m
   305	[37m      [39;49;00m[37m!    Also: post smoothing is not spelled out in detail in DD.[39;49;00m
   306	[37m      [39;49;00m[37m![39;49;00m
   307	[37m      [39;49;00m[37m![39;49;00m
   308	[37m[39;49;00m
   309	[37m[39;49;00m
   310	[37m      [39;49;00mn_col[37m [39;49;00m=[37m [39;49;00mdesc_data%matrix_data(psb_n_col_)[37m[39;49;00m
   311	[37m      [39;49;00mnr2l[37m  [39;49;00m=[37m [39;49;00mbaseprecv([34m1[39;49;00m)%desc_data%matrix_data(psb_n_col_)[37m[39;49;00m
   312	[37m[39;49;00m
   313	[37m      [39;49;00m[34mallocate[39;49;00m(mlprec_wrk([34m1[39;49;00m)%x2l(nr2l),mlprec_wrk([34m1[39;49;00m)%y2l(nr2l),[37m [39;49;00m&[37m[39;49;00m
   314	[37m           [39;49;00m&[37m [39;49;00mmlprec_wrk([34m1[39;49;00m)%tx(nr2l),[37m [39;49;00m[36mstat[39;49;00m=info)[37m[39;49;00m
   315	[37m      [39;49;00mmlprec_wrk([34m1[39;49;00m)%x2l(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
   316	[37m      [39;49;00mmlprec_wrk([34m1[39;49;00m)%y2l(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
   317	[37m      [39;49;00mmlprec_wrk([34m1[39;49;00m)%tx(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
   318	[37m[39;49;00m
   319	[37m      [39;49;00m[34mcall [39;49;00mpsb_geaxpby(zone,x,zzero,mlprec_wrk([34m1[39;49;00m)%tx,&[37m[39;49;00m
   320	[37m           [39;49;00m&[37m [39;49;00mbaseprecv([34m1[39;49;00m)%base_desc,info)[37m[39;49;00m
   321	[37m      [39;49;00m[34mcall [39;49;00mpsb_geaxpby(zone,x,zzero,mlprec_wrk([34m1[39;49;00m)%x2l,&[37m[39;49;00m
   322	[37m           [39;49;00m&[37m [39;49;00mbaseprecv([34m1[39;49;00m)%base_desc,info)[37m[39;49;00m
   323	[37m[39;49;00m
   324	[37m      [39;49;00m[34mdo [39;49;00milev=[34m2[39;49;00m,[37m [39;49;00mnlev[37m[39;49;00m
   325	[37m        [39;49;00mn_row[37m [39;49;00m=[37m [39;49;00mbaseprecv(ilev-[34m1[39;49;00m)%base_desc%matrix_data(psb_n_row_)[37m[39;49;00m
   326	[37m        [39;49;00mn_col[37m [39;49;00m=[37m [39;49;00mbaseprecv(ilev-[34m1[39;49;00m)%desc_data%matrix_data(psb_n_col_)[37m[39;49;00m
   327	[37m        [39;49;00mnr2l[37m  [39;49;00m=[37m [39;49;00mbaseprecv(ilev)%desc_data%matrix_data(psb_n_col_)[37m[39;49;00m
   328	[37m        [39;49;00mnrg[37m   [39;49;00m=[37m [39;49;00mbaseprecv(ilev)%desc_data%matrix_data(psb_n_row_)[37m[39;49;00m
   329	[37m        [39;49;00mismth[37m [39;49;00m=[37m [39;49;00mbaseprecv(ilev)%iprcparm(smth_kind_)[37m[39;49;00m
   330	[37m[39;49;00m
   331	[37m        [39;49;00m[34mallocate[39;49;00m(mlprec_wrk(ilev)%tx(nr2l),mlprec_wrk(ilev)%y2l(nr2l),&[37m[39;49;00m
   332	[37m             [39;49;00m&[37m   [39;49;00mmlprec_wrk(ilev)%x2l(nr2l),[37m [39;49;00m[36mstat[39;49;00m=info)[37m[39;49;00m
   333	[37m[39;49;00m
   334	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(info[37m [39;49;00m/=[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mthen[39;49;00m
   335	[34m          [39;49;00m[34mcall [39;49;00mpsb_errpush([34m4010[39;49;00m,name,a_err=[33m'Allocate'[39;49;00m)[37m[39;49;00m
   336	[37m          [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
   337	[37m        [39;49;00m[34mend [39;49;00m[34mif[39;49;00m
   338	[34m[39;49;00m
   339	[34m        [39;49;00mmlprec_wrk(ilev)%x2l(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
   340	[37m        [39;49;00mmlprec_wrk(ilev)%y2l(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
   341	[37m        [39;49;00mmlprec_wrk(ilev)%tx(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
   342	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ismth[37m  [39;49;00m/=[37m [39;49;00mno_smth_)[37m [39;49;00m[34mthen[39;49;00m[37m[39;49;00m
   343	[37m          [39;49;00m[37m![39;49;00m
   344	[37m          [39;49;00m[37m! Smoothed aggregation[39;49;00m
   345	[37m          [39;49;00m[37m![39;49;00m
   346	[37m          [39;49;00m[34mif[39;49;00m[37m [39;49;00m(baseprecv(ilev)%iprcparm(glb_smth_)[37m [39;49;00m>[34m0[39;49;00m)[37m [39;49;00m[34mthen[39;49;00m
   347	[34m            [39;49;00m[34mcall [39;49;00mpsb_halo(mlprec_wrk(ilev-[34m1[39;49;00m)%x2l,&[37m[39;49;00m
   348	[37m                 [39;49;00m&[37m  [39;49;00mbaseprecv(ilev-[34m1[39;49;00m)%base_desc,info,work=work)[37m[39;49;00m
   349	[37m            [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
   350	[37m          [39;49;00m[34melse[39;49;00m
   351	[34m            [39;49;00mmlprec_wrk(ilev-[34m1[39;49;00m)%x2l(n_row+[34m1[39;49;00m:[36mmax[39;49;00m(n_row,n_col))[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
   352	[37m          [39;49;00m[34mend [39;49;00m[34mif[39;49;00m
   353	[34m[39;49;00m
   354	[34m          [39;49;00m[34mcall [39;49;00mpsb_csmm(zone,baseprecv(ilev)%av(sm_pr_t_),mlprec_wrk(ilev-[34m1[39;49;00m)%x2l,[37m [39;49;00m&[37m[39;49;00m
   355	[37m               [39;49;00m&[37m [39;49;00mzzero,mlprec_wrk(ilev)%x2l,info)[37m[39;49;00m
   356	[37m          [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
   357	[37m[39;49;00m
   358	[37m        [39;49;00m[34melse[39;49;00m[37m[39;49;00m
   359	[37m          [39;49;00m[37m![39;49;00m
   360	[37m          [39;49;00m[37m! Raw  aggregation, may take shortcut[39;49;00m
   361	[37m          [39;49;00m[37m![39;49;00m
   362	[37m          [39;49;00m[34mdo [39;49;00mi=[34m1[39;49;00m,n_row[37m[39;49;00m
   363	[37m            [39;49;00mmlprec_wrk(ilev)%x2l(baseprecv(ilev)%mlia(i))[37m [39;49;00m=[37m [39;49;00m&[37m[39;49;00m
   364	[37m                 [39;49;00m&[37m [39;49;00mmlprec_wrk(ilev)%x2l(baseprecv(ilev)%mlia(i))[37m [39;49;00m+[37m [39;49;00m&[37m[39;49;00m
   365	[37m                 [39;49;00m&[37m [39;49;00mmlprec_wrk(ilev-[34m1[39;49;00m)%x2l(i)[37m[39;49;00m
   366	[37m          [39;49;00m[34mend [39;49;00m[34mdo[39;49;00m
   367	[34m        [39;49;00m[34mend [39;49;00m[34mif[39;49;00m
   368	[34m[39;49;00m
   369	[34m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(baseprecv(ilev)%iprcparm(coarse_mat_)==mat_repl_)[37m [39;49;00m[34mThen[39;49;00m
   370	[34m          [39;49;00m[34mcall [39;49;00mpsb_sum(ictxt,mlprec_wrk(ilev)%x2l([34m1[39;49;00m:nrg))[37m[39;49;00m
   371	[37m        [39;49;00m[34melse [39;49;00m[34mif[39;49;00m[37m [39;49;00m(baseprecv(ilev)%iprcparm(coarse_mat_)[37m [39;49;00m/=[37m [39;49;00mmat_distr_)[37m [39;49;00m[34mThen[39;49;00m
   372	[34m          [39;49;00m[34mwrite[39;49;00m([34m0[39;49;00m,*)[37m [39;49;00m[33m'Unknown value for baseprecv(2)%iprcparm(coarse_mat_) '[39;49;00m,&[37m[39;49;00m
   373	[37m               [39;49;00m&[37m [39;49;00mbaseprecv(ilev)%iprcparm(coarse_mat_)[37m[39;49;00m
   374	[37m        [39;49;00m[34mendif[39;49;00m
   375	[34m        [39;49;00m[34mcall [39;49;00mpsb_geaxpby(zone,mlprec_wrk(ilev)%x2l,zzero,mlprec_wrk(ilev)%tx,&[37m[39;49;00m
   376	[37m             [39;49;00m&[37m [39;49;00mbaseprecv(ilev)%base_desc,info)[37m[39;49;00m
   377	[37m        [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
   378	[37m[39;49;00m
   379	[37m      [39;49;00m[34menddo[39;49;00m
   380	[34m[39;49;00m
   381	[34m[39;49;00m
   382	[34m      [39;49;00m[34mcall [39;49;00mpsb_baseprc_aply(zone,baseprecv(nlev),mlprec_wrk(nlev)%x2l,[37m [39;49;00m&[37m[39;49;00m
   383	[37m           [39;49;00m&[37m [39;49;00mzzero,[37m [39;49;00mmlprec_wrk(nlev)%y2l,baseprecv(nlev)%desc_data,[33m'N'[39;49;00m,work,info)[37m[39;49;00m
   384	[37m[39;49;00m
   385	[37m      [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
   386	[37m[39;49;00m
   387	[37m[39;49;00m
   388	[37m      [39;49;00m[34mdo [39;49;00milev=nlev-[34m1[39;49;00m,[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00m-[34m1[39;49;00m[37m[39;49;00m
   389	[37m        [39;49;00mismth[37m [39;49;00m=[37m [39;49;00mbaseprecv(ilev+[34m1[39;49;00m)%iprcparm(smth_kind_)[37m[39;49;00m
   390	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ismth[37m  [39;49;00m/=[37m [39;49;00mno_smth_)[37m [39;49;00m[34mthen[39;49;00m
   391	[34m          [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ismth[37m [39;49;00m==[37m [39;49;00msmth_omg_)[37m [39;49;00m&[37m[39;49;00m
   392	[37m               [39;49;00m&[37m [39;49;00m[34mcall [39;49;00mpsb_halo(mlprec_wrk(ilev+[34m1[39;49;00m)%y2l,baseprecv(ilev+[34m1[39;49;00m)%desc_data,&[37m[39;49;00m
   393	[37m               [39;49;00m&[37m  [39;49;00minfo,work=work)[37m[39;49;00m
   394	[37m          [39;49;00m[34mcall [39;49;00mpsb_csmm(zone,baseprecv(ilev+[34m1[39;49;00m)%av(sm_pr_),mlprec_wrk(ilev+[34m1[39;49;00m)%y2l,&[37m[39;49;00m
   395	[37m               [39;49;00m&[37m  [39;49;00mzzero,mlprec_wrk(ilev)%y2l,info)[37m[39;49;00m
   396	[37m          [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
   397	[37m[39;49;00m
   398	[37m        [39;49;00m[34melse[39;49;00m
   399	[34m          [39;49;00mn_row[37m [39;49;00m=[37m [39;49;00mbaseprecv(ilev)%base_desc%matrix_data(psb_n_row_)[37m[39;49;00m
   400	[37m          [39;49;00mmlprec_wrk(ilev)%y2l(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
   401	[37m          [39;49;00m[34mdo [39;49;00mi=[34m1[39;49;00m,[37m [39;49;00mn_row[37m[39;49;00m
   402	[37m            [39;49;00mmlprec_wrk(ilev)%y2l(i)[37m [39;49;00m=[37m [39;49;00mmlprec_wrk(ilev)%y2l(i)[37m [39;49;00m+[37m [39;49;00m&[37m[39;49;00m
   403	[37m                 [39;49;00m&[37m [39;49;00mmlprec_wrk(ilev+[34m1[39;49;00m)%y2l(baseprecv(ilev+[34m1[39;49;00m)%mlia(i))[37m[39;49;00m
   404	[37m          [39;49;00m[34menddo[39;49;00m
   405	[34m[39;49;00m
   406	[34m        [39;49;00m[34mend [39;49;00m[34mif[39;49;00m
   407	[34m[39;49;00m
   408	[34m        [39;49;00m[34mcall [39;49;00mpsb_spmm(-zone,baseprecv(ilev)%base_a,mlprec_wrk(ilev)%y2l,&[37m[39;49;00m
   409	[37m             [39;49;00m&[37m   [39;49;00mzone,mlprec_wrk(ilev)%tx,baseprecv(ilev)%base_desc,info,work=work)[37m[39;49;00m
   410	[37m[39;49;00m
   411	[37m        [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
   412	[37m[39;49;00m
   413	[37m        [39;49;00m[34mcall [39;49;00mpsb_baseprc_aply(zone,baseprecv(ilev),mlprec_wrk(ilev)%tx,&[37m[39;49;00m
   414	[37m             [39;49;00m&[37m [39;49;00mzone,mlprec_wrk(ilev)%y2l,baseprecv(ilev)%base_desc,[37m [39;49;00mtrans,[37m [39;49;00mwork,info)[37m[39;49;00m
   415	[37m[39;49;00m
   416	[37m        [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
   417	[37m[39;49;00m
   418	[37m      [39;49;00m[34menddo[39;49;00m
   419	[34m[39;49;00m
   420	[34m      [39;49;00m[34mcall [39;49;00mpsb_geaxpby(alpha,mlprec_wrk([34m1[39;49;00m)%y2l,beta,y,baseprecv([34m1[39;49;00m)%base_desc,info)[37m[39;49;00m
   421	[37m[39;49;00m
   422	[37m      [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
   423	[37m[39;49;00m
   424	[37m[39;49;00m
   425	[37m    [39;49;00m[34mcase[39;49;00m(pre_smooth_)[37m[39;49;00m
   426	[37m[39;49;00m
   427	[37m[39;49;00m
   428	[37m      [39;49;00m[37m![39;49;00m
   429	[37m      [39;49;00m[37m!    Pre smoothing.[39;49;00m
   430	[37m      [39;49;00m[37m!    1.   X(1)  = Xext[39;49;00m
   431	[37m      [39;49;00m[37m!    2.   Y(1)  = (K(1)**(-1))*X(1)[39;49;00m
   432	[37m      [39;49;00m[37m!    3.   TX(1) = X(1) - A(1)*Y(1)[39;49;00m
   433	[37m      [39;49;00m[37m!    4.   DO ILEV=2, NLEV[39;49;00m
   434	[37m      [39;49;00m[37m!          X(ILEV) = AV(PR_SM_T_,ILEV)*TX(ILEV-1)[39;49;00m
   435	[37m      [39;49;00m[37m!          Y(ILEV) = (K(ILEV)**(-1))*X(ILEV)[39;49;00m
   436	[37m      [39;49;00m[37m!          TX(ILEV) = (X(ILEV)-A(ILEV)*Y(ILEV))[39;49;00m
   437	[37m      [39;49;00m[37m!    5.   DO  ILEV=NLEV-1,1,-1[39;49;00m
   438	[37m      [39;49;00m[37m!          Y(ILEV) = Y(ILEV) + AV(PR_SM_,ILEV+1)*Y(ILEV+1)[39;49;00m
   439	[37m      [39;49;00m[37m!    6.  Yext    = beta*Yext + Y(1)[39;49;00m
   440	[37m      [39;49;00m[37m![39;49;00m
   441	[37m      [39;49;00m[37m!    Note: level numbering reversed wrt ref. DD, i.e.[39;49;00m
   442	[37m      [39;49;00m[37m!         1..NLEV <=>  (j) <-> 0[39;49;00m
   443	[37m      [39;49;00m[37m![39;49;00m
   444	[37m      [39;49;00m[37m![39;49;00m
   445	[37m[39;49;00m
   446	[37m      [39;49;00mn_col[37m [39;49;00m=[37m [39;49;00mdesc_data%matrix_data(psb_n_col_)[37m[39;49;00m
   447	[37m      [39;49;00mnr2l[37m  [39;49;00m=[37m [39;49;00mbaseprecv([34m1[39;49;00m)%desc_data%matrix_data(psb_n_col_)[37m[39;49;00m
   448	[37m[39;49;00m
   449	[37m      [39;49;00m[34mallocate[39;49;00m(mlprec_wrk([34m1[39;49;00m)%x2l(nr2l),mlprec_wrk([34m1[39;49;00m)%y2l(nr2l),[37m [39;49;00m&[37m[39;49;00m
   450	[37m           [39;49;00m&[37m [39;49;00mmlprec_wrk([34m1[39;49;00m)%tx(nr2l),[37m [39;49;00m[36mstat[39;49;00m=info)[37m[39;49;00m
   451	[37m      [39;49;00m[34mif[39;49;00m[37m [39;49;00m(info[37m [39;49;00m/=[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mthen[39;49;00m
   452	[34m        [39;49;00m[34mcall [39;49;00mpsb_errpush([34m4010[39;49;00m,name,a_err=[33m'Allocate'[39;49;00m)[37m[39;49;00m
   453	[37m        [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
   454	[37m      [39;49;00m[34mend [39;49;00m[34mif[39;49;00m
   455	[34m[39;49;00m
   456	[34m      [39;49;00mmlprec_wrk([34m1[39;49;00m)%y2l(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
   457	[37m[39;49;00m
   458	[37m[39;49;00m
   459	[37m      [39;49;00mmlprec_wrk([34m1[39;49;00m)%x2l(:)[37m [39;49;00m=[37m [39;49;00mx[37m[39;49;00m
   460	[37m[39;49;00m
   461	[37m      [39;49;00m[34mcall [39;49;00mpsb_baseprc_aply(zone,baseprecv([34m1[39;49;00m),mlprec_wrk([34m1[39;49;00m)%x2l,&[37m[39;49;00m
   462	[37m           [39;49;00m&[37m  [39;49;00mzzero,mlprec_wrk([34m1[39;49;00m)%y2l,&[37m[39;49;00m
   463	[37m           [39;49;00m&[37m  [39;49;00mbaseprecv([34m1[39;49;00m)%base_desc,&[37m[39;49;00m
   464	[37m           [39;49;00m&[37m  [39;49;00mtrans,work,info)[37m[39;49;00m
   465	[37m[39;49;00m
   466	[37m      [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
   467	[37m[39;49;00m
   468	[37m      [39;49;00mmlprec_wrk([34m1[39;49;00m)%tx[37m [39;49;00m=[37m [39;49;00mmlprec_wrk([34m1[39;49;00m)%x2l[37m[39;49;00m
   469	[37m[39;49;00m
   470	[37m      [39;49;00m[34mcall [39;49;00mpsb_spmm(-zone,baseprecv([34m1[39;49;00m)%base_a,mlprec_wrk([34m1[39;49;00m)%y2l,&[37m[39;49;00m
   471	[37m           [39;49;00m&[37m [39;49;00mzone,mlprec_wrk([34m1[39;49;00m)%tx,baseprecv([34m1[39;49;00m)%base_desc,info,work=work)[37m[39;49;00m
   472	[37m      [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
   473	[37m[39;49;00m
   474	[37m      [39;49;00m[34mdo [39;49;00milev[37m [39;49;00m=[37m [39;49;00m[34m2[39;49;00m,[37m [39;49;00mnlev[37m[39;49;00m
   475	[37m        [39;49;00mn_row[37m [39;49;00m=[37m [39;49;00mbaseprecv(ilev-[34m1[39;49;00m)%base_desc%matrix_data(psb_n_row_)[37m[39;49;00m
   476	[37m        [39;49;00mn_col[37m [39;49;00m=[37m [39;49;00mbaseprecv(ilev-[34m1[39;49;00m)%desc_data%matrix_data(psb_n_col_)[37m[39;49;00m
   477	[37m        [39;49;00mnr2l[37m  [39;49;00m=[37m [39;49;00mbaseprecv(ilev)%desc_data%matrix_data(psb_n_col_)[37m[39;49;00m
   478	[37m        [39;49;00mnrg[37m   [39;49;00m=[37m [39;49;00mbaseprecv(ilev)%desc_data%matrix_data(psb_n_row_)[37m[39;49;00m
   479	[37m        [39;49;00mismth[37m [39;49;00m=[37m [39;49;00mbaseprecv(ilev)%iprcparm(smth_kind_)[37m[39;49;00m
   480	[37m        [39;49;00m[34mallocate[39;49;00m(mlprec_wrk(ilev)%tx(nr2l),mlprec_wrk(ilev)%y2l(nr2l),&[37m[39;49;00m
   481	[37m             [39;49;00m&[37m   [39;49;00mmlprec_wrk(ilev)%x2l(nr2l),[37m [39;49;00m[36mstat[39;49;00m=info)[37m[39;49;00m
   482	[37m[39;49;00m
   483	[37m[39;49;00m
   484	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(info[37m [39;49;00m/=[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mthen[39;49;00m
   485	[34m          [39;49;00m[34mcall [39;49;00mpsb_errpush([34m4010[39;49;00m,name,a_err=[33m'Allocate'[39;49;00m)[37m[39;49;00m
   486	[37m          [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
   487	[37m        [39;49;00m[34mend [39;49;00m[34mif[39;49;00m
   488	[34m[39;49;00m
   489	[34m        [39;49;00mmlprec_wrk(ilev)%x2l(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
   490	[37m        [39;49;00mmlprec_wrk(ilev)%y2l(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
   491	[37m        [39;49;00mmlprec_wrk(ilev)%tx(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
   492	[37m[39;49;00m
   493	[37m[39;49;00m
   494	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ismth[37m  [39;49;00m/=[37m [39;49;00mno_smth_)[37m [39;49;00m[34mthen[39;49;00m[37m[39;49;00m
   495	[37m          [39;49;00m[37m![39;49;00m
   496	[37m          [39;49;00m[37m!Smoothed Aggregation[39;49;00m
   497	[37m          [39;49;00m[37m![39;49;00m
   498	[37m          [39;49;00m[34mif[39;49;00m[37m [39;49;00m(baseprecv(ilev)%iprcparm(glb_smth_)[37m [39;49;00m>[34m0[39;49;00m)[37m [39;49;00m[34mthen[39;49;00m
   499	[34m[39;49;00m
   500	[34m            [39;49;00m[34mcall [39;49;00mpsb_halo(mlprec_wrk(ilev-[34m1[39;49;00m)%tx,baseprecv(ilev-[34m1[39;49;00m)%base_desc,&[37m[39;49;00m
   501	[37m                 [39;49;00m&[37m [39;49;00minfo,work=work)[37m[39;49;00m
   502	[37m            [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
   503	[37m          [39;49;00m[34melse[39;49;00m
   504	[34m            [39;49;00mmlprec_wrk(ilev-[34m1[39;49;00m)%tx(n_row+[34m1[39;49;00m:[36mmax[39;49;00m(n_row,n_col))[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
   505	[37m          [39;49;00m[34mend [39;49;00m[34mif[39;49;00m
   506	[34m[39;49;00m
   507	[34m          [39;49;00m[34mcall [39;49;00mpsb_csmm(zone,baseprecv(ilev)%av(sm_pr_t_),mlprec_wrk(ilev-[34m1[39;49;00m)%tx,zzero,&[37m[39;49;00m
   508	[37m               [39;49;00m&[37m [39;49;00mmlprec_wrk(ilev)%x2l,info)[37m[39;49;00m
   509	[37m          [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
   510	[37m[39;49;00m
   511	[37m        [39;49;00m[34melse[39;49;00m[37m[39;49;00m
   512	[37m          [39;49;00m[37m![39;49;00m
   513	[37m          [39;49;00m[37m! Raw  aggregation, may take shortcuts[39;49;00m
   514	[37m          [39;49;00m[37m![39;49;00m
   515	[37m          [39;49;00mmlprec_wrk(ilev)%x2l[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
   516	[37m          [39;49;00m[34mdo [39;49;00mi=[34m1[39;49;00m,n_row[37m[39;49;00m
   517	[37m            [39;49;00mmlprec_wrk(ilev)%x2l(baseprecv(ilev)%mlia(i))[37m [39;49;00m=[37m [39;49;00m&[37m[39;49;00m
   518	[37m                 [39;49;00m&[37m [39;49;00mmlprec_wrk(ilev)%x2l(baseprecv(ilev)%mlia(i))[37m [39;49;00m+[37m [39;49;00m&[37m[39;49;00m
   519	[37m                 [39;49;00m&[37m  [39;49;00mmlprec_wrk(ilev-[34m1[39;49;00m)%tx(i)[37m[39;49;00m
   520	[37m          [39;49;00m[34mend [39;49;00m[34mdo[39;49;00m
   521	[34m        [39;49;00m[34mend [39;49;00m[34mif[39;49;00m
   522	[34m[39;49;00m
   523	[34m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(baseprecv(ilev)%iprcparm(coarse_mat_)==mat_repl_)[37m [39;49;00m[34mthen[39;49;00m
   524	[34m          [39;49;00m[34mcall [39;49;00mpsb_sum(ictxt,mlprec_wrk(ilev)%x2l([34m1[39;49;00m:nrg))[37m[39;49;00m
   525	[37m        [39;49;00m[34melse [39;49;00m[34mif[39;49;00m[37m [39;49;00m(baseprecv(ilev)%iprcparm(coarse_mat_)[37m [39;49;00m/=[37m [39;49;00mmat_distr_)[37m [39;49;00m[34mthen[39;49;00m
   526	[34m          [39;49;00m[34mwrite[39;49;00m([34m0[39;49;00m,*)[37m [39;49;00m[33m'Unknown value for baseprecv(2)%iprcparm(coarse_mat_) '[39;49;00m,&[37m[39;49;00m
   527	[37m               [39;49;00m&[37m [39;49;00mbaseprecv(ilev)%iprcparm(coarse_mat_)[37m[39;49;00m
   528	[37m        [39;49;00m[34mendif[39;49;00m
   529	[34m[39;49;00m
   530	[34m[39;49;00m
   531	[34m        [39;49;00m[34mcall [39;49;00mpsb_baseprc_aply(zone,baseprecv(ilev),mlprec_wrk(ilev)%x2l,&[37m[39;49;00m
   532	[37m             [39;49;00m&[37m [39;49;00mzzero,mlprec_wrk(ilev)%y2l,baseprecv(ilev)%desc_data,[37m [39;49;00m[33m'N'[39;49;00m,work,info)[37m[39;49;00m
   533	[37m[39;49;00m
   534	[37m        [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
   535	[37m[39;49;00m
   536	[37m        [39;49;00m[34mif[39;49;00m(ilev[37m [39;49;00m<[37m [39;49;00mnlev)[37m [39;49;00m[34mthen[39;49;00m
   537	[34m          [39;49;00mmlprec_wrk(ilev)%tx[37m [39;49;00m=[37m [39;49;00mmlprec_wrk(ilev)%x2l[37m[39;49;00m
   538	[37m          [39;49;00m[34mcall [39;49;00mpsb_spmm(-zone,baseprecv(ilev)%base_a,mlprec_wrk(ilev)%y2l,&[37m[39;49;00m
   539	[37m               [39;49;00m&[37m [39;49;00mzone,mlprec_wrk(ilev)%tx,baseprecv(ilev)%base_desc,info,work=work)[37m[39;49;00m
   540	[37m          [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
   541	[37m        [39;49;00m[34mendif[39;49;00m
   542	[34m[39;49;00m
   543	[34m      [39;49;00m[34menddo[39;49;00m
   544	[34m[39;49;00m
   545	[34m      [39;49;00m[34mdo [39;49;00milev[37m [39;49;00m=[37m [39;49;00mnlev-[34m1[39;49;00m,[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00m-[34m1[39;49;00m[37m[39;49;00m
   546	[37m[39;49;00m
   547	[37m        [39;49;00mismth=baseprecv(ilev+[34m1[39;49;00m)%iprcparm(smth_kind_)[37m[39;49;00m
   548	[37m[39;49;00m
   549	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ismth[37m  [39;49;00m/=[37m [39;49;00mno_smth_)[37m [39;49;00m[34mthen[39;49;00m
   550	[34m[39;49;00m
   551	[34m          [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ismth[37m [39;49;00m==[37m [39;49;00msmth_omg_)[37m [39;49;00m&[37m[39;49;00m
   552	[37m               [39;49;00m&[37m [39;49;00m[34mcall [39;49;00mpsb_halo(mlprec_wrk(ilev+[34m1[39;49;00m)%y2l,&[37m[39;49;00m
   553	[37m               [39;49;00m&[37m [39;49;00mbaseprecv(ilev+[34m1[39;49;00m)%desc_data,info,work=work)[37m[39;49;00m
   554	[37m          [39;49;00m[34mcall [39;49;00mpsb_csmm(zone,baseprecv(ilev+[34m1[39;49;00m)%av(sm_pr_),mlprec_wrk(ilev+[34m1[39;49;00m)%y2l,&[37m[39;49;00m
   555	[37m               [39;49;00m&[37m [39;49;00mzone,mlprec_wrk(ilev)%y2l,info)[37m[39;49;00m
   556	[37m[39;49;00m
   557	[37m          [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
   558	[37m[39;49;00m
   559	[37m        [39;49;00m[34melse[39;49;00m
   560	[34m[39;49;00m
   561	[34m          [39;49;00mn_row[37m [39;49;00m=[37m [39;49;00mbaseprecv(ilev+[34m1[39;49;00m)%base_desc%matrix_data(psb_n_row_)[37m[39;49;00m
   562	[37m          [39;49;00m[34mdo [39;49;00mi=[34m1[39;49;00m,[37m [39;49;00mn_row[37m[39;49;00m
   563	[37m            [39;49;00mmlprec_wrk(ilev)%y2l(i)[37m [39;49;00m=[37m [39;49;00mmlprec_wrk(ilev)%y2l(i)[37m [39;49;00m+[37m [39;49;00m&[37m[39;49;00m
   564	[37m                 [39;49;00m&[37m [39;49;00mmlprec_wrk(ilev+[34m1[39;49;00m)%y2l(baseprecv(ilev+[34m1[39;49;00m)%mlia(i))[37m[39;49;00m
   565	[37m          [39;49;00m[34menddo[39;49;00m
   566	[34m[39;49;00m
   567	[34m        [39;49;00m[34mend [39;49;00m[34mif[39;49;00m
   568	[34m[39;49;00m
   569	[34m      [39;49;00m[34menddo[39;49;00m
   570	[34m[39;49;00m
   571	[34m      [39;49;00m[34mcall [39;49;00mpsb_geaxpby(alpha,mlprec_wrk([34m1[39;49;00m)%y2l,beta,y,&[37m[39;49;00m
   572	[37m           [39;49;00m&[37m  [39;49;00mbaseprecv([34m1[39;49;00m)%base_desc,info)[37m[39;49;00m
   573	[37m[39;49;00m
   574	[37m      [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
   575	[37m[39;49;00m
   576	[37m[39;49;00m
   577	[37m[39;49;00m
   578	[37m    [39;49;00m[34mcase[39;49;00m(smooth_both_)[37m[39;49;00m
   579	[37m[39;49;00m
   580	[37m      [39;49;00m[37m![39;49;00m
   581	[37m      [39;49;00m[37m!    Symmetrized  smoothing.[39;49;00m
   582	[37m      [39;49;00m[37m!    1.   X(1)  = Xext[39;49;00m
   583	[37m      [39;49;00m[37m!    2.   Y(1)  = (K(1)**(-1))*X(1)[39;49;00m
   584	[37m      [39;49;00m[37m!    3.   TX(1) = X(1) - A(1)*Y(1)[39;49;00m
   585	[37m      [39;49;00m[37m!    4.   DO ILEV=2, NLEV[39;49;00m
   586	[37m      [39;49;00m[37m!          X(ILEV) = AV(PR_SM_T_,ILEV)*TX(ILEV-1)[39;49;00m
   587	[37m      [39;49;00m[37m!          Y(ILEV) = (K(ILEV)**(-1))*X(ILEV)[39;49;00m
   588	[37m      [39;49;00m[37m!          TX(ILEV) = (X(ILEV)-A(ILEV)*Y(ILEV))[39;49;00m
   589	[37m      [39;49;00m[37m!    5.   DO  ILEV=NLEV-1,1,-1[39;49;00m
   590	[37m      [39;49;00m[37m!          Y(ILEV) = Y(ILEV) + AV(PR_SM_,ILEV+1)*Y(ILEV+1)[39;49;00m
   591	[37m      [39;49;00m[37m!          Y(ILEV) = Y(ILEV) + (K(ILEV)**(-1))*(X(ILEV)-A(ILEV)*Y(ILEV))[39;49;00m
   592	[37m      [39;49;00m[37m!    6.  Yext    = beta*Yext + Y(1)[39;49;00m
   593	[37m      [39;49;00m[37m![39;49;00m
   594	[37m      [39;49;00m[37m!    Note: level numbering reversed wrt ref. DD, i.e.[39;49;00m
   595	[37m      [39;49;00m[37m!         1..NLEV <=>  (j) <-> 0[39;49;00m
   596	[37m      [39;49;00m[37m![39;49;00m
   597	[37m      [39;49;00m[37m![39;49;00m
   598	[37m      [39;49;00mn_col[37m [39;49;00m=[37m [39;49;00mdesc_data%matrix_data(psb_n_col_)[37m[39;49;00m
   599	[37m      [39;49;00mnr2l[37m  [39;49;00m=[37m [39;49;00mbaseprecv([34m1[39;49;00m)%desc_data%matrix_data(psb_n_col_)[37m[39;49;00m
   600	[37m[39;49;00m
   601	[37m      [39;49;00m[34mallocate[39;49;00m(mlprec_wrk([34m1[39;49;00m)%x2l(nr2l),mlprec_wrk([34m1[39;49;00m)%y2l(nr2l),[37m [39;49;00m&[37m[39;49;00m
   602	[37m           [39;49;00m&[37m [39;49;00mmlprec_wrk([34m1[39;49;00m)%ty(nr2l),[37m [39;49;00mmlprec_wrk([34m1[39;49;00m)%tx(nr2l),[37m [39;49;00m[36mstat[39;49;00m=info)[37m[39;49;00m
   603	[37m[39;49;00m
   604	[37m      [39;49;00mmlprec_wrk([34m1[39;49;00m)%x2l(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
   605	[37m      [39;49;00mmlprec_wrk([34m1[39;49;00m)%y2l(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
   606	[37m      [39;49;00mmlprec_wrk([34m1[39;49;00m)%tx(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
   607	[37m      [39;49;00mmlprec_wrk([34m1[39;49;00m)%ty(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
   608	[37m[39;49;00m
   609	[37m[39;49;00m
   610	[37m      [39;49;00m[34mif[39;49;00m[37m [39;49;00m(info[37m [39;49;00m/=[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mthen[39;49;00m
   611	[34m        [39;49;00m[34mcall [39;49;00mpsb_errpush([34m4010[39;49;00m,name,a_err=[33m'Allocate'[39;49;00m)[37m[39;49;00m
   612	[37m        [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
   613	[37m      [39;49;00m[34mend [39;49;00m[34mif[39;49;00m
   614	[34m[39;49;00m
   615	[34m      [39;49;00m[34mcall [39;49;00mpsb_geaxpby(zone,x,zzero,mlprec_wrk([34m1[39;49;00m)%x2l,&[37m[39;49;00m
   616	[37m           [39;49;00m&[37m [39;49;00mbaseprecv([34m1[39;49;00m)%base_desc,info)[37m[39;49;00m
   617	[37m      [39;49;00m[34mcall [39;49;00mpsb_geaxpby(zone,x,zzero,mlprec_wrk([34m1[39;49;00m)%tx,&[37m[39;49;00m
   618	[37m           [39;49;00m&[37m [39;49;00mbaseprecv([34m1[39;49;00m)%base_desc,info)[37m[39;49;00m
   619	[37m[39;49;00m
   620	[37m      [39;49;00m[34mcall [39;49;00mpsb_baseprc_aply(zone,baseprecv([34m1[39;49;00m),mlprec_wrk([34m1[39;49;00m)%x2l,&[37m[39;49;00m
   621	[37m           [39;49;00m&[37m  [39;49;00mzzero,mlprec_wrk([34m1[39;49;00m)%y2l,&[37m[39;49;00m
   622	[37m           [39;49;00m&[37m  [39;49;00mbaseprecv([34m1[39;49;00m)%base_desc,&[37m[39;49;00m
   623	[37m           [39;49;00m&[37m  [39;49;00mtrans,work,info)[37m[39;49;00m
   624	[37m[39;49;00m
   625	[37m      [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
   626	[37m[39;49;00m
   627	[37m      [39;49;00mmlprec_wrk([34m1[39;49;00m)%ty[37m [39;49;00m=[37m [39;49;00mmlprec_wrk([34m1[39;49;00m)%x2l[37m[39;49;00m
   628	[37m[39;49;00m
   629	[37m      [39;49;00m[34mcall [39;49;00mpsb_spmm(-zone,baseprecv([34m1[39;49;00m)%base_a,mlprec_wrk([34m1[39;49;00m)%y2l,&[37m[39;49;00m
   630	[37m           [39;49;00m&[37m [39;49;00mzone,mlprec_wrk([34m1[39;49;00m)%ty,baseprecv([34m1[39;49;00m)%base_desc,info,work=work)[37m[39;49;00m
   631	[37m      [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
   632	[37m[39;49;00m
   633	[37m      [39;49;00m[34mdo [39;49;00milev[37m [39;49;00m=[37m [39;49;00m[34m2[39;49;00m,[37m [39;49;00mnlev[37m[39;49;00m
   634	[37m        [39;49;00mn_row[37m [39;49;00m=[37m [39;49;00mbaseprecv(ilev-[34m1[39;49;00m)%base_desc%matrix_data(psb_n_row_)[37m[39;49;00m
   635	[37m        [39;49;00mn_col[37m [39;49;00m=[37m [39;49;00mbaseprecv(ilev-[34m1[39;49;00m)%desc_data%matrix_data(psb_n_col_)[37m[39;49;00m
   636	[37m        [39;49;00mnr2l[37m  [39;49;00m=[37m [39;49;00mbaseprecv(ilev)%desc_data%matrix_data(psb_n_col_)[37m[39;49;00m
   637	[37m        [39;49;00mnrg[37m   [39;49;00m=[37m [39;49;00mbaseprecv(ilev)%desc_data%matrix_data(psb_n_row_)[37m[39;49;00m
   638	[37m        [39;49;00mismth=baseprecv(ilev)%iprcparm(smth_kind_)[37m[39;49;00m
   639	[37m        [39;49;00m[34mallocate[39;49;00m(mlprec_wrk(ilev)%ty(nr2l),mlprec_wrk(ilev)%y2l(nr2l),&[37m[39;49;00m
   640	[37m             [39;49;00m&[37m   [39;49;00mmlprec_wrk(ilev)%x2l(nr2l),[37m [39;49;00m[36mstat[39;49;00m=info)[37m[39;49;00m
   641	[37m[39;49;00m
   642	[37m        [39;49;00mmlprec_wrk(ilev)%x2l(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
   643	[37m        [39;49;00mmlprec_wrk(ilev)%y2l(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
   644	[37m        [39;49;00mmlprec_wrk(ilev)%tx(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
   645	[37m        [39;49;00mmlprec_wrk(ilev)%ty(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
   646	[37m[39;49;00m
   647	[37m[39;49;00m
   648	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(info[37m [39;49;00m/=[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mthen[39;49;00m
   649	[34m          [39;49;00m[34mcall [39;49;00mpsb_errpush([34m4010[39;49;00m,name,a_err=[33m'Allocate'[39;49;00m)[37m[39;49;00m
   650	[37m          [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
   651	[37m        [39;49;00m[34mend [39;49;00m[34mif[39;49;00m
   652	[34m[39;49;00m
   653	[34m[39;49;00m
   654	[34m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ismth[37m  [39;49;00m/=[37m [39;49;00mno_smth_)[37m [39;49;00m[34mthen[39;49;00m[37m[39;49;00m
   655	[37m          [39;49;00m[37m![39;49;00m
   656	[37m          [39;49;00m[37m!Smoothed Aggregation[39;49;00m
   657	[37m          [39;49;00m[37m![39;49;00m
   658	[37m          [39;49;00m[34mif[39;49;00m[37m [39;49;00m(baseprecv(ilev)%iprcparm(glb_smth_)[37m [39;49;00m>[34m0[39;49;00m)[37m [39;49;00m[34mthen[39;49;00m
   659	[34m[39;49;00m
   660	[34m            [39;49;00m[34mcall [39;49;00mpsb_halo(mlprec_wrk(ilev-[34m1[39;49;00m)%ty,baseprecv(ilev-[34m1[39;49;00m)%base_desc,&[37m[39;49;00m
   661	[37m                 [39;49;00m&[37m [39;49;00minfo,work=work)[37m[39;49;00m
   662	[37m            [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
   663	[37m          [39;49;00m[34melse[39;49;00m
   664	[34m            [39;49;00mmlprec_wrk(ilev-[34m1[39;49;00m)%ty(n_row+[34m1[39;49;00m:[36mmax[39;49;00m(n_row,n_col))[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
   665	[37m          [39;49;00m[34mend [39;49;00m[34mif[39;49;00m
   666	[34m[39;49;00m
   667	[34m          [39;49;00m[34mcall [39;49;00mpsb_csmm(zone,baseprecv(ilev)%av(sm_pr_t_),mlprec_wrk(ilev-[34m1[39;49;00m)%ty,zzero,&[37m[39;49;00m
   668	[37m               [39;49;00m&[37m [39;49;00mmlprec_wrk(ilev)%x2l,info)[37m[39;49;00m
   669	[37m          [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
   670	[37m[39;49;00m
   671	[37m        [39;49;00m[34melse[39;49;00m[37m[39;49;00m
   672	[37m          [39;49;00m[37m![39;49;00m
   673	[37m          [39;49;00m[37m! Raw  aggregation, may take shortcuts[39;49;00m
   674	[37m          [39;49;00m[37m![39;49;00m
   675	[37m          [39;49;00mmlprec_wrk(ilev)%x2l[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
   676	[37m          [39;49;00m[34mdo [39;49;00mi=[34m1[39;49;00m,n_row[37m[39;49;00m
   677	[37m            [39;49;00mmlprec_wrk(ilev)%x2l(baseprecv(ilev)%mlia(i))[37m [39;49;00m=[37m [39;49;00m&[37m[39;49;00m
   678	[37m                 [39;49;00m&[37m [39;49;00mmlprec_wrk(ilev)%x2l(baseprecv(ilev)%mlia(i))[37m [39;49;00m+[37m [39;49;00m&[37m[39;49;00m
   679	[37m                 [39;49;00m&[37m  [39;49;00mmlprec_wrk(ilev-[34m1[39;49;00m)%ty(i)[37m[39;49;00m
   680	[37m          [39;49;00m[34mend [39;49;00m[34mdo[39;49;00m
   681	[34m        [39;49;00m[34mend [39;49;00m[34mif[39;49;00m
   682	[34m[39;49;00m
   683	[34m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(baseprecv(ilev)%iprcparm(coarse_mat_)==mat_repl_)[37m [39;49;00m[34mthen[39;49;00m
   684	[34m          [39;49;00m[34mcall [39;49;00mpsb_sum(ictxt,mlprec_wrk(ilev)%x2l([34m1[39;49;00m:nrg))[37m[39;49;00m
   685	[37m        [39;49;00m[34melse [39;49;00m[34mif[39;49;00m[37m [39;49;00m(baseprecv(ilev)%iprcparm(coarse_mat_)[37m [39;49;00m/=[37m [39;49;00mmat_distr_)[37m [39;49;00m[34mthen[39;49;00m
   686	[34m          [39;49;00m[34mwrite[39;49;00m([34m0[39;49;00m,*)[37m [39;49;00m[33m'Unknown value for baseprecv(2)%iprcparm(coarse_mat_) '[39;49;00m,&[37m[39;49;00m
   687	[37m               [39;49;00m&[37m [39;49;00mbaseprecv(ilev)%iprcparm(coarse_mat_)[37m[39;49;00m
   688	[37m        [39;49;00m[34mendif[39;49;00m
   689	[34m[39;49;00m
   690	[34m        [39;49;00m[34mcall [39;49;00mpsb_geaxpby(zone,mlprec_wrk(ilev)%x2l,zzero,mlprec_wrk(ilev)%tx,&[37m[39;49;00m
   691	[37m             [39;49;00m&[37m [39;49;00mbaseprecv(ilev)%base_desc,info)[37m[39;49;00m
   692	[37m        [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
   693	[37m[39;49;00m
   694	[37m        [39;49;00m[34mcall [39;49;00mpsb_baseprc_aply(zone,baseprecv(ilev),mlprec_wrk(ilev)%x2l,&[37m[39;49;00m
   695	[37m             [39;49;00m&[37m [39;49;00mzzero,mlprec_wrk(ilev)%y2l,baseprecv(ilev)%desc_data,[37m [39;49;00m[33m'N'[39;49;00m,work,info)[37m[39;49;00m
   696	[37m[39;49;00m
   697	[37m        [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
   698	[37m[39;49;00m
   699	[37m        [39;49;00m[34mif[39;49;00m(ilev[37m [39;49;00m<[37m [39;49;00mnlev)[37m [39;49;00m[34mthen[39;49;00m
   700	[34m          [39;49;00mmlprec_wrk(ilev)%ty[37m [39;49;00m=[37m [39;49;00mmlprec_wrk(ilev)%x2l[37m[39;49;00m
   701	[37m          [39;49;00m[34mcall [39;49;00mpsb_spmm(-zone,baseprecv(ilev)%base_a,mlprec_wrk(ilev)%y2l,&[37m[39;49;00m
   702	[37m               [39;49;00m&[37m [39;49;00mzone,mlprec_wrk(ilev)%ty,baseprecv(ilev)%base_desc,info,work=work)[37m[39;49;00m
   703	[37m          [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
   704	[37m        [39;49;00m[34mendif[39;49;00m
   705	[34m[39;49;00m
   706	[34m      [39;49;00m[34menddo[39;49;00m
   707	[34m[39;49;00m
   708	[34m[39;49;00m
   709	[34m      [39;49;00m[34mdo [39;49;00milev=nlev-[34m1[39;49;00m,[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00m-[34m1[39;49;00m[37m[39;49;00m
   710	[37m[39;49;00m
   711	[37m        [39;49;00mismth=baseprecv(ilev+[34m1[39;49;00m)%iprcparm(smth_kind_)[37m[39;49;00m
   712	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ismth[37m  [39;49;00m/=[37m [39;49;00mno_smth_)[37m [39;49;00m[34mthen[39;49;00m
   713	[34m          [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ismth[37m [39;49;00m==[37m [39;49;00msmth_omg_)[37m [39;49;00m&[37m[39;49;00m
   714	[37m               [39;49;00m&[37m [39;49;00m[34mcall [39;49;00mpsb_halo(mlprec_wrk(ilev+[34m1[39;49;00m)%y2l,baseprecv(ilev+[34m1[39;49;00m)%desc_data,&[37m[39;49;00m
   715	[37m               [39;49;00m&[37m  [39;49;00minfo,work=work)[37m[39;49;00m
   716	[37m          [39;49;00m[34mcall [39;49;00mpsb_csmm(zone,baseprecv(ilev+[34m1[39;49;00m)%av(sm_pr_),mlprec_wrk(ilev+[34m1[39;49;00m)%y2l,&[37m[39;49;00m
   717	[37m               [39;49;00m&[37m  [39;49;00mzone,mlprec_wrk(ilev)%y2l,info)[37m[39;49;00m
   718	[37m          [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
   719	[37m[39;49;00m
   720	[37m        [39;49;00m[34melse[39;49;00m
   721	[34m          [39;49;00mn_row[37m [39;49;00m=[37m [39;49;00mbaseprecv(ilev)%base_desc%matrix_data(psb_n_row_)[37m[39;49;00m
   722	[37m          [39;49;00m[34mdo [39;49;00mi=[34m1[39;49;00m,[37m [39;49;00mn_row[37m[39;49;00m
   723	[37m            [39;49;00mmlprec_wrk(ilev)%y2l(i)[37m [39;49;00m=[37m [39;49;00mmlprec_wrk(ilev)%y2l(i)[37m [39;49;00m+[37m [39;49;00m&[37m[39;49;00m
   724	[37m                 [39;49;00m&[37m [39;49;00mmlprec_wrk(ilev+[34m1[39;49;00m)%y2l(baseprecv(ilev+[34m1[39;49;00m)%mlia(i))[37m[39;49;00m
   725	[37m          [39;49;00m[34menddo[39;49;00m
   726	[34m[39;49;00m
   727	[34m        [39;49;00m[34mend [39;49;00m[34mif[39;49;00m
   728	[34m[39;49;00m
   729	[34m        [39;49;00m[34mcall [39;49;00mpsb_spmm(-zone,baseprecv(ilev)%base_a,mlprec_wrk(ilev)%y2l,&[37m[39;49;00m
   730	[37m             [39;49;00m&[37m   [39;49;00mzone,mlprec_wrk(ilev)%tx,baseprecv(ilev)%base_desc,info,work=work)[37m[39;49;00m
   731	[37m[39;49;00m
   732	[37m        [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
   733	[37m[39;49;00m
   734	[37m        [39;49;00m[34mcall [39;49;00mpsb_baseprc_aply(zone,baseprecv(ilev),mlprec_wrk(ilev)%tx,&[37m[39;49;00m
   735	[37m             [39;49;00m&[37m [39;49;00mzone,mlprec_wrk(ilev)%y2l,baseprecv(ilev)%base_desc,[37m [39;49;00mtrans,[37m [39;49;00mwork,info)[37m[39;49;00m
   736	[37m[39;49;00m
   737	[37m        [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
   738	[37m[39;49;00m
   739	[37m      [39;49;00m[34menddo[39;49;00m
   740	[34m[39;49;00m
   741	[34m      [39;49;00m[34mcall [39;49;00mpsb_geaxpby(alpha,mlprec_wrk([34m1[39;49;00m)%y2l,beta,y,&[37m[39;49;00m
   742	[37m           [39;49;00m&[37m   [39;49;00mbaseprecv([34m1[39;49;00m)%base_desc,info)[37m[39;49;00m
   743	[37m[39;49;00m
   744	[37m      [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
   745	[37m[39;49;00m
   746	[37m[39;49;00m
   747	[37m    [39;49;00m[34mcase [39;49;00mdefault[37m[39;49;00m
   748	[37m[39;49;00m
   749	[37m      [39;49;00m[34mcall [39;49;00mpsb_errpush([34m4013[39;49;00m,name,a_err=[33m'wrong smooth_pos'[39;49;00m,&[37m[39;49;00m
   750	[37m           [39;49;00m&[37m  [39;49;00mi_Err=(/baseprecv([34m2[39;49;00m)%iprcparm(smth_pos_),[34m0[39;49;00m,[34m0[39;49;00m,[34m0[39;49;00m,[34m0[39;49;00m/))[37m[39;49;00m
   751	[37m      [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
   752	[37m[39;49;00m
   753	[37m    [39;49;00m[34mend [39;49;00m[34mselect[39;49;00m
   754	[34m[39;49;00m
   755	[34m  [39;49;00m[34mcase [39;49;00mdefault[37m[39;49;00m
   756	[37m    [39;49;00m[34mcall [39;49;00mpsb_errpush([34m4013[39;49;00m,name,a_err=[33m'wrong mltype'[39;49;00m,&[37m[39;49;00m
   757	[37m         [39;49;00m&[37m  [39;49;00mi_Err=(/baseprecv([34m2[39;49;00m)%iprcparm(ml_type_),[34m0[39;49;00m,[34m0[39;49;00m,[34m0[39;49;00m,[34m0[39;49;00m/))[37m[39;49;00m
   758	[37m    [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
   759	[37m[39;49;00m
   760	[37m  [39;49;00m[34mend [39;49;00m[34mselect[39;49;00m
   761	[34m[39;49;00m
   762	[34m[39;49;00m
   763	[34m  [39;49;00m[34mcall [39;49;00mmlprec_wrk_free(mlprec_wrk)[37m[39;49;00m
   764	[37m  [39;49;00m[34mdeallocate[39;49;00m(mlprec_wrk)[37m[39;49;00m
   765	[37m[39;49;00m
   766	[37m  [39;49;00m[34mcall [39;49;00mpsb_erractionrestore(err_act)[37m[39;49;00m
   767	[37m  [39;49;00m[34mreturn[39;49;00m
   768	[34m[39;49;00m
   769	[34m9999[39;49;00m[37m [39;49;00m[34mcontinue[39;49;00m
   770	[34m  [39;49;00m[34mcall [39;49;00mpsb_errpush(info,name)[37m[39;49;00m
   771	[37m  [39;49;00m[34mcall [39;49;00mpsb_erractionrestore(err_act)[37m[39;49;00m
   772	[37m  [39;49;00m[34mif[39;49;00m[37m [39;49;00m(err_act.eq.act_abort)[37m [39;49;00m[34mthen[39;49;00m
   773	[34m    [39;49;00m[34mcall [39;49;00mpsb_error()[37m[39;49;00m
   774	[37m    [39;49;00m[34mreturn[39;49;00m
   775	[34m  [39;49;00m[34mend [39;49;00m[34mif[39;49;00m
   776	[34m  [39;49;00m[34mreturn[39;49;00m
   777	[34m[39;49;00m
   778	[34mcontains[39;49;00m
   779	[34m  [39;49;00m[34msubroutine [39;49;00mmlprec_wrk_free(wrk)[37m[39;49;00m
   780	[37m    [39;49;00m[34mtype[39;49;00m(psb_mlprec_wrk_type)[37m [39;49;00m[34m::[39;49;00m[37m [39;49;00mwrk(:)[37m[39;49;00m
   781	[37m    [39;49;00m[37m! This will not be needed when we have allocatables, as[39;49;00m
   782	[37m    [39;49;00m[37m! it is sufficient to deallocate the container, and[39;49;00m
   783	[37m    [39;49;00m[37m! the compiler is supposed to recursively deallocate the[39;49;00m
   784	[37m    [39;49;00m[37m! various components.[39;49;00m
   785	[37m    [39;49;00m[36minteger [39;49;00mi[37m[39;49;00m
   786	[37m[39;49;00m
   787	[37m    [39;49;00m[34mdo [39;49;00mi=[34m1[39;49;00m,[37m [39;49;00msize(wrk)[37m[39;49;00m
   788	[37m      [39;49;00m[34mif[39;49;00m[37m [39;49;00m([36massociated[39;49;00m(wrk(i)%tx))[37m  [39;49;00m[34mdeallocate[39;49;00m(wrk(i)%tx)[37m[39;49;00m
   789	[37m      [39;49;00m[34mif[39;49;00m[37m [39;49;00m([36massociated[39;49;00m(wrk(i)%ty))[37m  [39;49;00m[34mdeallocate[39;49;00m(wrk(i)%ty)[37m[39;49;00m
   790	[37m      [39;49;00m[34mif[39;49;00m[37m [39;49;00m([36massociated[39;49;00m(wrk(i)%x2l))[37m [39;49;00m[34mdeallocate[39;49;00m(wrk(i)%x2l)[37m[39;49;00m
   791	[37m      [39;49;00m[34mif[39;49;00m[37m [39;49;00m([36massociated[39;49;00m(wrk(i)%y2l))[37m [39;49;00m[34mdeallocate[39;49;00m(wrk(i)%y2l)[37m[39;49;00m
   792	[37m      [39;49;00m[34mif[39;49;00m[37m [39;49;00m([36massociated[39;49;00m(wrk(i)%b2l))[37m [39;49;00m[34mdeallocate[39;49;00m(wrk(i)%b2l)[37m[39;49;00m
   793	[37m      [39;49;00m[34mif[39;49;00m[37m [39;49;00m([36massociated[39;49;00m(wrk(i)%tty))[37m [39;49;00m[34mdeallocate[39;49;00m(wrk(i)%tty)[37m[39;49;00m
   794	[37m    [39;49;00m[34mend [39;49;00m[34mdo[39;49;00m
   795	[34m  [39;49;00m[34mend [39;49;00m[34msubroutine [39;49;00mmlprec_wrk_free[37m[39;49;00m
   796	[37m[39;49;00m
   797	[34mend [39;49;00m[34msubroutine [39;49;00mpsb_zmlprc_aply

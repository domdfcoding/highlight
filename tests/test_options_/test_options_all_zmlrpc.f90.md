     1^I[37m!!$[39;49;00m$
     2^I[37m!!$[39;49;00m$
     3^I[37m!!$                    MD2P4[39;49;00m$
     4^I[37m!!$    Multilevel Domain Decomposition Parallel Preconditioner Package for PSBLAS[39;49;00m$
     5^I[37m!!$                      for[39;49;00m$
     6^I[37m!!$              Parallel Sparse BLAS  v2.0[39;49;00m$
     7^I[37m!!$    (C) Copyright 2006 Salvatore Filippone    University of Rome Tor Vergata[39;49;00m$
     8^I[37m!!$                       Alfredo Buttari        University of Rome Tor Vergata[39;49;00m$
     9^I[37m!!$                       Daniela Di Serafino    II University of Naples[39;49;00m$
    10^I[37m!!$                       Pasqua D'Ambra         ICAR-CNR[39;49;00m$
    11^I[37m!!$[39;49;00m$
    12^I[37m!!$  Redistribution and use in source and binary forms, with or without[39;49;00m$
    13^I[37m!!$  modification, are permitted provided that the following conditions[39;49;00m$
    14^I[37m!!$  are met:[39;49;00m$
    15^I[37m!!$    1. Redistributions of source code must retain the above copyright[39;49;00m$
    16^I[37m!!$       notice, this list of conditions and the following disclaimer.[39;49;00m$
    17^I[37m!!$    2. Redistributions in binary form must reproduce the above copyright[39;49;00m$
    18^I[37m!!$       notice, this list of conditions, and the following disclaimer in the[39;49;00m$
    19^I[37m!!$       documentation and/or other materials provided with the distribution.[39;49;00m$
    20^I[37m!!$    3. The name of the MD2P4 group or the names of its contributors may[39;49;00m$
    21^I[37m!!$       not be used to endorse or promote products derived from this[39;49;00m$
    22^I[37m!!$       software without specific written permission.[39;49;00m$
    23^I[37m!!$[39;49;00m$
    24^I[37m!!$  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS[39;49;00m$
    25^I[37m!!$  ``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED[39;49;00m$
    26^I[37m!!$  TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR[39;49;00m$
    27^I[37m!!$  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE MD2P4 GROUP OR ITS CONTRIBUTORS[39;49;00m$
    28^I[37m!!$  BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR[39;49;00m$
    29^I[37m!!$  CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF[39;49;00m$
    30^I[37m!!$  SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS[39;49;00m$
    31^I[37m!!$  INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN[39;49;00m$
    32^I[37m!!$  CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)[39;49;00m$
    33^I[37m!!$  ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE[39;49;00m$
    34^I[37m!!$  POSSIBILITY OF SUCH DAMAGE.[39;49;00m$
    35^I[37m!!$[39;49;00m$
    36^I[37m!!$[39;49;00m$
    37^I[34msubroutine [39;49;00mpsb_zmlprc_aply(alpha,baseprecv,x,beta,y,desc_data,trans,work,info)[37m[39;49;00m$
    38^I[37m  [39;49;00m[37m![39;49;00m$
    39^I[37m  [39;49;00m[37m!  Compute   Y <-  beta*Y + alpha*K^-1 X[39;49;00m$
    40^I[37m  [39;49;00m[37m!  where K is a multilevel  preconditioner stored in baseprecv[39;49;00m$
    41^I[37m  [39;49;00m[37m![39;49;00m$
    42^I[37m  [39;49;00m[37m!  cfr.: Smith, Biorstad & Gropp[39;49;00m$
    43^I[37m  [39;49;00m[37m!        Domain Decomposition[39;49;00m$
    44^I[37m  [39;49;00m[37m!        Cambridge Univ. Press[39;49;00m$
    45^I[37m  [39;49;00m[37m![39;49;00m$
    46^I[37m  [39;49;00m[37m!  To each level I there corresponds a matrix A(I) and a preconditioner K(I)[39;49;00m$
    47^I[37m  [39;49;00m[37m![39;49;00m$
    48^I[37m  [39;49;00m[37m!  A notational difference: in the DD reference above the preconditioner for[39;49;00m$
    49^I[37m  [39;49;00m[37m!  a given level K(I) is written out as a sum over the subdomains[39;49;00m$
    50^I[37m  [39;49;00m[37m![39;49;00m$
    51^I[37m  [39;49;00m[37m!  SUM_k(R_k^T A_k R_k)[39;49;00m$
    52^I[37m  [39;49;00m[37m![39;49;00m$
    53^I[37m  [39;49;00m[37m!  whereas in this code the sum is implicit in the parallelization,[39;49;00m$
    54^I[37m  [39;49;00m[37m!  i.e. each process takes care of one subdomain, and for each level we have[39;49;00m$
    55^I[37m  [39;49;00m[37m!  as many subdomains as there are processes (except for the coarsest level where[39;49;00m$
    56^I[37m  [39;49;00m[37m!  we might have a replicated index space). Thus the sum apparently disappears[39;49;00m$
    57^I[37m  [39;49;00m[37m!  from our code, but only apparently, because it is implicit in the call[39;49;00m$
    58^I[37m  [39;49;00m[37m!  to psb_baseprc_aply.[39;49;00m$
    59^I[37m  [39;49;00m[37m![39;49;00m$
    60^I[37m  [39;49;00m[37m!  A bit of description of the baseprecv(:) data structure:[39;49;00m$
    61^I[37m  [39;49;00m[37m!   1. Number of levels = NLEV = size(baseprecv(:))[39;49;00m$
    62^I[37m  [39;49;00m[37m!   2. baseprecv(ilev)%av(:)    sparse matrices needed for the current level.[39;49;00m$
    63^I[37m  [39;49;00m[37m!      Includes:[39;49;00m$
    64^I[37m  [39;49;00m[37m!   2.1.:  baseprecv(ilev)%av(l_pr_)    L factor of ILU preconditioners[39;49;00m$
    65^I[37m  [39;49;00m[37m!   2.2.:  baseprecv(ilev)%av(u_pr_)    U factor of ILU preconditioners[39;49;00m$
    66^I[37m  [39;49;00m[37m!   2.3.:  baseprecv(ilev)%av(ap_nd_)   Off-diagonal part of A for Jacobi sweeps[39;49;00m$
    67^I[37m  [39;49;00m[37m!   2.4.:  baseprecv(ilev)%av(ac_)      Aggregated matrix of level ILEV[39;49;00m$
    68^I[37m  [39;49;00m[37m!   2.5.:  baseprecv(ilev)%av(sm_pr_t_) Smoother prolongator transpose; maps vectors[39;49;00m$
    69^I[37m  [39;49;00m[37m!                                          (ilev-1) --->  (ilev)[39;49;00m$
    70^I[37m  [39;49;00m[37m!   2.6.:  baseprecv(ilev)%av(sm_pr_)   Smoother prolongator; maps vectors[39;49;00m$
    71^I[37m  [39;49;00m[37m!                                          (ilev)   --->  (ilev-1)[39;49;00m$
    72^I[37m  [39;49;00m[37m!   Shouldn't we keep just one of them and handle transpose in the sparse BLAS? maybe[39;49;00m$
    73^I[37m  [39;49;00m[37m![39;49;00m$
    74^I[37m  [39;49;00m[37m!   3.    baseprecv(ilev)%desc_data     comm descriptor for level ILEV[39;49;00m$
    75^I[37m  [39;49;00m[37m!   4.    baseprecv(ilev)%base_a        Pointer (really a pointer!) to the base matrix[39;49;00m$
    76^I[37m  [39;49;00m[37m!                                       of the current level, i.e.: if ILEV=1 then  A[39;49;00m$
    77^I[37m  [39;49;00m[37m!                                       else the aggregated matrix av(ac_); so we have[39;49;00m$
    78^I[37m  [39;49;00m[37m!                                       a unified treatment of residuals. Need this to[39;49;00m$
    79^I[37m  [39;49;00m[37m!                                       avoid passing explicitly matrix A to the[39;49;00m$
    80^I[37m  [39;49;00m[37m!                                       outer prec. routine[39;49;00m$
    81^I[37m  [39;49;00m[37m!   5.    baseprecv(ilev)%mlia          The aggregation map from (ilev-1)-->(ilev)[39;49;00m$
    82^I[37m  [39;49;00m[37m!                                       if no smoother, it is used instead of sm_pr_[39;49;00m$
    83^I[37m  [39;49;00m[37m!   6.    baseprecv(ilev)%nlaggr        Number of aggregates on the various procs.[39;49;00m$
    84^I[37m  [39;49;00m[37m![39;49;00m$
    85^I[37m[39;49;00m$
    86^I[37m  [39;49;00m[34muse [39;49;00mpsb_serial_mod[37m[39;49;00m$
    87^I[37m  [39;49;00m[34muse [39;49;00mpsb_descriptor_type[37m[39;49;00m$
    88^I[37m  [39;49;00m[34muse [39;49;00mpsb_prec_type[37m[39;49;00m$
    89^I[37m  [39;49;00m[34muse [39;49;00mpsb_psblas_mod[37m[39;49;00m$
    90^I[37m  [39;49;00m[34muse [39;49;00mpsb_penv_mod[37m[39;49;00m$
    91^I[37m  [39;49;00m[34muse [39;49;00mpsb_const_mod[37m[39;49;00m$
    92^I[37m  [39;49;00m[34muse [39;49;00mpsb_error_mod[37m[39;49;00m$
    93^I[37m  [39;49;00m[34muse [39;49;00mpsb_penv_mod[37m[39;49;00m$
    94^I[37m  [39;49;00m[34mimplicit [39;49;00m[34mnone[39;49;00m$
    95^I[34m[39;49;00m$
    96^I[34m  [39;49;00m[34mtype[39;49;00m(psb_desc_type),[34mintent[39;49;00m(in)[37m      [39;49;00m[34m::[39;49;00m[37m [39;49;00mdesc_data[37m[39;49;00m$
    97^I[37m  [39;49;00m[34mtype[39;49;00m(psb_zbaseprc_type),[37m [39;49;00m[34mintent[39;49;00m(in)[37m [39;49;00m[34m::[39;49;00m[37m [39;49;00mbaseprecv(:)[37m[39;49;00m$
    98^I[37m  [39;49;00m[36mcomplex[39;49;00m([36mkind[39;49;00m([34m1.d0[39;49;00m)),[34mintent[39;49;00m(in)[37m      [39;49;00m[34m::[39;49;00m[37m [39;49;00malpha,beta[37m[39;49;00m$
    99^I[37m  [39;49;00m[36mcomplex[39;49;00m([36mkind[39;49;00m([34m1.d0[39;49;00m)),[34mintent[39;49;00m(inout)[37m   [39;49;00m[34m::[39;49;00m[37m [39;49;00mx(:),[37m [39;49;00my(:)[37m[39;49;00m$
   100^I[37m  [39;49;00m[36mcharacter[39;49;00m[37m                           [39;49;00m[34m::[39;49;00m[37m [39;49;00mtrans[37m[39;49;00m$
   101^I[37m  [39;49;00m[36mcomplex[39;49;00m([36mkind[39;49;00m([34m1.d0[39;49;00m)),[34mtarget[39;49;00m[37m          [39;49;00m[34m::[39;49;00m[37m [39;49;00mwork(:)[37m[39;49;00m$
   102^I[37m  [39;49;00m[36minteger[39;49;00m,[37m [39;49;00m[34mintent[39;49;00m(out)[37m                [39;49;00m[34m::[39;49;00m[37m [39;49;00minfo[37m[39;49;00m$
   103^I[37m[39;49;00m$
   104^I[37m[39;49;00m$
   105^I[37m  [39;49;00m[37m! Local variables[39;49;00m$
   106^I[37m  [39;49;00m[36minteger[39;49;00m[37m [39;49;00m[34m::[39;49;00m[37m [39;49;00mn_row,n_col[37m[39;49;00m$
   107^I[37m  [39;49;00m[36mcomplex[39;49;00m([36mkind[39;49;00m([34m1.d0[39;49;00m)),[37m [39;49;00m[34mallocatable[39;49;00m[37m [39;49;00m[34m::[39;49;00m[37m [39;49;00mtx(:),ty(:),t2l(:),w2l(:),&[37m[39;49;00m$
   108^I[37m       [39;49;00m&[37m   [39;49;00mx2l(:),b2l(:),tz(:),tty(:)[37m[39;49;00m$
   109^I[37m  [39;49;00m[36mcharacter[39;49;00m[37m     [39;49;00m[34m::[39;49;00mdiagl,[37m [39;49;00mdiagu[37m[39;49;00m$
   110^I[37m  [39;49;00m[36minteger[39;49;00m[37m [39;49;00m[34m::[39;49;00m[37m [39;49;00mictxt,np,me,i,[37m [39;49;00misz,[37m [39;49;00mnrg,nr2l,err_act,[37m [39;49;00miptype,[37m [39;49;00mint_err([34m5[39;49;00m)[37m[39;49;00m$
   111^I[37m  [39;49;00m[36mreal[39;49;00m([36mkind[39;49;00m([34m1.d0[39;49;00m))[37m [39;49;00m[34m::[39;49;00m[37m [39;49;00momega[37m[39;49;00m$
   112^I[37m  [39;49;00m[36mreal[39;49;00m([36mkind[39;49;00m([34m1.d0[39;49;00m))[37m [39;49;00m[34m::[39;49;00m[37m [39;49;00mt1,[37m [39;49;00mt2,[37m [39;49;00mt3,[37m [39;49;00mt4,[37m [39;49;00mt5,[37m [39;49;00mt6,[37m [39;49;00mt7,[37m [39;49;00mmpi_wtime[37m[39;49;00m$
   113^I[37m  [39;49;00m[36mlogical[39;49;00m,[37m [39;49;00m[34mparameter[39;49;00m[37m          [39;49;00m[34m::[39;49;00m[37m [39;49;00mdebug=.false.,[37m [39;49;00mdebugprt=.false.[37m[39;49;00m$
   114^I[37m  [39;49;00m[36minteger[39;49;00m[37m      [39;49;00m[34m::[39;49;00m[37m [39;49;00mismth,[37m [39;49;00mnlev,[37m [39;49;00milev[37m[39;49;00m$
   115^I[37m  [39;49;00m[34mexternal [39;49;00mmpi_wtime[37m[39;49;00m$
   116^I[37m  [39;49;00m[36mcharacter[39;49;00m([36mlen[39;49;00m=[34m20[39;49;00m)[37m   [39;49;00m[34m::[39;49;00m[37m [39;49;00mname,[37m [39;49;00mch_err[37m[39;49;00m$
   117^I[37m[39;49;00m$
   118^I[37m  [39;49;00m[34mtype [39;49;00mpsb_mlprec_wrk_type[37m[39;49;00m$
   119^I[37m    [39;49;00m[36mcomplex[39;49;00m([36mkind[39;49;00m([34m1.d0[39;49;00m)),[37m [39;49;00m[34mpointer[39;49;00m[37m [39;49;00m[34m::[39;49;00m[37m [39;49;00mtx(:)=>[36mnull[39;49;00m(),ty(:)=>[36mnull[39;49;00m(),&[37m[39;49;00m$
   120^I[37m         [39;49;00m&[37m [39;49;00mx2l(:)=>[36mnull[39;49;00m(),y2l(:)=>[36mnull[39;49;00m(),&[37m[39;49;00m$
   121^I[37m         [39;49;00m&[37m [39;49;00mb2l(:)=>[36mnull[39;49;00m(),tty(:)=>[36mnull[39;49;00m()[37m[39;49;00m$
   122^I[37m  [39;49;00m[34mend [39;49;00m[34mtype [39;49;00mpsb_mlprec_wrk_type[37m[39;49;00m$
   123^I[37m  [39;49;00m[34mtype[39;49;00m(psb_mlprec_wrk_type),[37m [39;49;00m[34mpointer[39;49;00m[37m [39;49;00m[34m::[39;49;00m[37m [39;49;00mmlprec_wrk(:)[37m[39;49;00m$
   124^I[37m[39;49;00m$
   125^I[37m  [39;49;00m[34minterface [39;49;00mpsb_baseprc_aply[37m[39;49;00m$
   126^I[37m    [39;49;00m[34msubroutine [39;49;00mpsb_zbaseprc_aply(alpha,prec,x,beta,y,desc_data,trans,work,info)[37m[39;49;00m$
   127^I[37m      [39;49;00m[34muse [39;49;00mpsb_descriptor_type[37m[39;49;00m$
   128^I[37m      [39;49;00m[34muse [39;49;00mpsb_prec_type[37m[39;49;00m$
   129^I[37m      [39;49;00m[34mtype[39;49;00m(psb_desc_type),[34mintent[39;49;00m(in)[37m      [39;49;00m[34m::[39;49;00m[37m [39;49;00mdesc_data[37m[39;49;00m$
   130^I[37m      [39;49;00m[34mtype[39;49;00m(psb_zbaseprc_type),[37m [39;49;00m[34mintent[39;49;00m(in)[37m [39;49;00m[34m::[39;49;00m[37m [39;49;00mprec[37m[39;49;00m$
   131^I[37m      [39;49;00m[36mcomplex[39;49;00m([36mkind[39;49;00m([34m1.d0[39;49;00m)),[34mintent[39;49;00m(inout)[37m   [39;49;00m[34m::[39;49;00m[37m [39;49;00mx(:),[37m [39;49;00my(:)[37m[39;49;00m$
   132^I[37m      [39;49;00m[36mcomplex[39;49;00m([36mkind[39;49;00m([34m1.d0[39;49;00m)),[34mintent[39;49;00m(in)[37m      [39;49;00m[34m::[39;49;00m[37m [39;49;00malpha,beta[37m[39;49;00m$
   133^I[37m      [39;49;00m[36mcharacter[39;49;00m([36mlen[39;49;00m=[34m1[39;49;00m)[37m                    [39;49;00m[34m::[39;49;00m[37m [39;49;00mtrans[37m[39;49;00m$
   134^I[37m      [39;49;00m[36mcomplex[39;49;00m([36mkind[39;49;00m([34m1.d0[39;49;00m)),[34mtarget[39;49;00m[37m          [39;49;00m[34m::[39;49;00m[37m [39;49;00mwork(:)[37m[39;49;00m$
   135^I[37m      [39;49;00m[36minteger[39;49;00m,[37m [39;49;00m[34mintent[39;49;00m(out)[37m                [39;49;00m[34m::[39;49;00m[37m [39;49;00minfo[37m[39;49;00m$
   136^I[37m    [39;49;00m[34mend [39;49;00m[34msubroutine [39;49;00mpsb_zbaseprc_aply[37m[39;49;00m$
   137^I[37m  [39;49;00m[34mend [39;49;00m[34minterface[39;49;00m$
   138^I[34m[39;49;00m$
   139^I[34m  [39;49;00mname=[33m'psb_mlprc_aply'[39;49;00m[37m[39;49;00m$
   140^I[37m  [39;49;00minfo[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m[37m[39;49;00m$
   141^I[37m  [39;49;00m[34mcall [39;49;00mpsb_erractionsave(err_act)[37m[39;49;00m$
   142^I[37m[39;49;00m$
   143^I[37m[39;49;00m$
   144^I[37m  [39;49;00mictxt=desc_data%matrix_data(psb_ctxt_)[37m[39;49;00m$
   145^I[37m  [39;49;00m[34mcall [39;49;00mpsb_info(ictxt,[37m [39;49;00mme,[37m [39;49;00mnp)[37m[39;49;00m$
   146^I[37m[39;49;00m$
   147^I[37m  [39;49;00mnlev[37m [39;49;00m=[37m [39;49;00msize(baseprecv)[37m[39;49;00m$
   148^I[37m  [39;49;00m[34mallocate[39;49;00m(mlprec_wrk(nlev),[36mstat[39;49;00m=info)[37m[39;49;00m$
   149^I[37m  [39;49;00m[34mif[39;49;00m[37m [39;49;00m(info[37m [39;49;00m/=[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mthen[39;49;00m$
   150^I[34m    [39;49;00m[34mcall [39;49;00mpsb_errpush([34m4010[39;49;00m,name,a_err=[33m'Allocate'[39;49;00m)[37m[39;49;00m$
   151^I[37m    [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m$
   152^I[37m  [39;49;00m[34mend [39;49;00m[34mif[39;49;00m$
   153^I[34m[39;49;00m$
   154^I[34m[39;49;00m$
   155^I[34m  [39;49;00m[34mselect [39;49;00m[34mcase[39;49;00m(baseprecv([34m2[39;49;00m)%iprcparm(ml_type_))[37m[39;49;00m$
   156^I[37m[39;49;00m$
   157^I[37m  [39;49;00m[34mcase[39;49;00m(no_ml_)[37m[39;49;00m$
   158^I[37m    [39;49;00m[37m! Should not really get here.[39;49;00m$
   159^I[37m    [39;49;00m[34mcall [39;49;00mpsb_errpush([34m4010[39;49;00m,name,a_err=[33m'no_ml_ in mlprc_aply?'[39;49;00m)[37m[39;49;00m$
   160^I[37m    [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m$
   161^I[37m[39;49;00m$
   162^I[37m[39;49;00m$
   163^I[37m  [39;49;00m[34mcase[39;49;00m(add_ml_prec_)[37m[39;49;00m$
   164^I[37m[39;49;00m$
   165^I[37m[39;49;00m$
   166^I[37m    [39;49;00m[37m![39;49;00m$
   167^I[37m    [39;49;00m[37m!    Additive is very simple.[39;49;00m$
   168^I[37m    [39;49;00m[37m!    1.  X(1) = Xext[39;49;00m$
   169^I[37m    [39;49;00m[37m!    2.  DO ILEV=2,NLEV[39;49;00m$
   170^I[37m    [39;49;00m[37m!           X(ILEV) = AV(PR_SM_T_)*X(ILEV-1)[39;49;00m$
   171^I[37m    [39;49;00m[37m!    3.  Y(ILEV) = (K(ILEV)**(-1))*X(ILEV)[39;49;00m$
   172^I[37m    [39;49;00m[37m!    4.  DO  ILEV=NLEV-1,1,-1[39;49;00m$
   173^I[37m    [39;49;00m[37m!           Y(ILEV) = AV(PR_SM_)*Y(ILEV+1)[39;49;00m$
   174^I[37m    [39;49;00m[37m!    5.  Yext    = beta*Yext + Y(1)[39;49;00m$
   175^I[37m    [39;49;00m[37m![39;49;00m$
   176^I[37m    [39;49;00m[37m!    Note: level numbering reversed wrt ref. DD, i.e.[39;49;00m$
   177^I[37m    [39;49;00m[37m!         1..NLEV <=>  (j) <-> 0[39;49;00m$
   178^I[37m[39;49;00m$
   179^I[37m[39;49;00m$
   180^I[37m    [39;49;00m[34mcall [39;49;00mpsb_baseprc_aply(alpha,baseprecv([34m1[39;49;00m),x,beta,y,&[37m[39;49;00m$
   181^I[37m         [39;49;00m&[37m [39;49;00mbaseprecv([34m1[39;49;00m)%base_desc,trans,work,info)[37m[39;49;00m$
   182^I[37m    [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m$
   183^I[37m    [39;49;00m[34mallocate[39;49;00m(mlprec_wrk([34m1[39;49;00m)%x2l(size(x)),mlprec_wrk([34m1[39;49;00m)%y2l(size(y)))[37m[39;49;00m$
   184^I[37m    [39;49;00mmlprec_wrk([34m1[39;49;00m)%x2l(:)[37m [39;49;00m=[37m [39;49;00mx(:)[37m[39;49;00m$
   185^I[37m[39;49;00m$
   186^I[37m[39;49;00m$
   187^I[37m    [39;49;00m[34mdo [39;49;00milev[37m [39;49;00m=[37m [39;49;00m[34m2[39;49;00m,[37m [39;49;00mnlev[37m[39;49;00m$
   188^I[37m      [39;49;00mn_row[37m [39;49;00m=[37m [39;49;00mbaseprecv(ilev-[34m1[39;49;00m)%base_desc%matrix_data(psb_n_row_)[37m[39;49;00m$
   189^I[37m      [39;49;00mn_col[37m [39;49;00m=[37m [39;49;00mbaseprecv(ilev-[34m1[39;49;00m)%desc_data%matrix_data(psb_n_col_)[37m[39;49;00m$
   190^I[37m      [39;49;00mnr2l[37m  [39;49;00m=[37m [39;49;00mbaseprecv(ilev)%desc_data%matrix_data(psb_n_col_)[37m[39;49;00m$
   191^I[37m      [39;49;00mnrg[37m   [39;49;00m=[37m [39;49;00mbaseprecv(ilev)%desc_data%matrix_data(psb_n_row_)[37m[39;49;00m$
   192^I[37m      [39;49;00m[34mallocate[39;49;00m(mlprec_wrk(ilev)%x2l(nr2l),mlprec_wrk(ilev)%y2l(nr2l),&[37m[39;49;00m$
   193^I[37m           [39;49;00m&[37m [39;49;00mmlprec_wrk(ilev)%tx([36mmax[39;49;00m(n_row,n_col)),&[37m[39;49;00m$
   194^I[37m           [39;49;00m&[37m [39;49;00mmlprec_wrk(ilev)%ty([36mmax[39;49;00m(n_row,n_col)),[37m [39;49;00m[36mstat[39;49;00m=info)[37m[39;49;00m$
   195^I[37m      [39;49;00m[34mif[39;49;00m[37m [39;49;00m(info[37m [39;49;00m/=[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mthen[39;49;00m$
   196^I[34m        [39;49;00m[34mcall [39;49;00mpsb_errpush([34m4010[39;49;00m,name,a_err=[33m'Allocate'[39;49;00m)[37m[39;49;00m$
   197^I[37m        [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m$
   198^I[37m      [39;49;00m[34mend [39;49;00m[34mif[39;49;00m$
   199^I[34m[39;49;00m$
   200^I[34m      [39;49;00mmlprec_wrk(ilev)%x2l(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m$
   201^I[37m      [39;49;00mmlprec_wrk(ilev)%y2l(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m$
   202^I[37m      [39;49;00mmlprec_wrk(ilev)%tx([34m1[39;49;00m:n_row)[37m [39;49;00m=[37m [39;49;00mmlprec_wrk(ilev-[34m1[39;49;00m)%x2l([34m1[39;49;00m:n_row)[37m[39;49;00m$
   203^I[37m      [39;49;00mmlprec_wrk(ilev)%tx(n_row+[34m1[39;49;00m:[36mmax[39;49;00m(n_row,n_col))[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m$
   204^I[37m      [39;49;00mmlprec_wrk(ilev)%ty(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m$
   205^I[37m[39;49;00m$
   206^I[37m      [39;49;00mismth=baseprecv(ilev)%iprcparm(smth_kind_)[37m[39;49;00m$
   207^I[37m[39;49;00m$
   208^I[37m      [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ismth[37m  [39;49;00m/=[37m [39;49;00mno_smth_)[37m [39;49;00m[34mthen[39;49;00m[37m[39;49;00m$
   209^I[37m        [39;49;00m[37m![39;49;00m$
   210^I[37m        [39;49;00m[37m! Smoothed aggregation[39;49;00m$
   211^I[37m        [39;49;00m[37m![39;49;00m$
   212^I[37m[39;49;00m$
   213^I[37m[39;49;00m$
   214^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(baseprecv(ilev)%iprcparm(glb_smth_)[37m [39;49;00m>[34m0[39;49;00m)[37m [39;49;00m[34mthen[39;49;00m$
   215^I[34m          [39;49;00m[34mcall [39;49;00mpsb_halo(mlprec_wrk(ilev-[34m1[39;49;00m)%x2l,baseprecv(ilev-[34m1[39;49;00m)%base_desc,&[37m[39;49;00m$
   216^I[37m               [39;49;00m&[37m  [39;49;00minfo,work=work)[37m[39;49;00m$
   217^I[37m          [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m$
   218^I[37m        [39;49;00m[34melse[39;49;00m$
   219^I[34m          [39;49;00mmlprec_wrk(ilev-[34m1[39;49;00m)%x2l(n_row+[34m1[39;49;00m:[36mmax[39;49;00m(n_row,n_col))[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m$
   220^I[37m        [39;49;00m[34mend [39;49;00m[34mif[39;49;00m$
   221^I[34m[39;49;00m$
   222^I[34m        [39;49;00m[34mcall [39;49;00mpsb_csmm(zone,baseprecv(ilev)%av(sm_pr_t_),mlprec_wrk(ilev-[34m1[39;49;00m)%x2l,&[37m[39;49;00m$
   223^I[37m             [39;49;00m&[37m [39;49;00mzzero,mlprec_wrk(ilev)%x2l,info)[37m[39;49;00m$
   224^I[37m        [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m$
   225^I[37m[39;49;00m$
   226^I[37m      [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
   227^I[37m        [39;49;00m[37m![39;49;00m$
   228^I[37m        [39;49;00m[37m! Raw  aggregation, may take shortcut[39;49;00m$
   229^I[37m        [39;49;00m[37m![39;49;00m$
   230^I[37m        [39;49;00m[34mdo [39;49;00mi=[34m1[39;49;00m,n_row[37m[39;49;00m$
   231^I[37m          [39;49;00mmlprec_wrk(ilev)%x2l(baseprecv(ilev)%mlia(i))[37m [39;49;00m=[37m [39;49;00m&[37m[39;49;00m$
   232^I[37m               [39;49;00m&[37m  [39;49;00mmlprec_wrk(ilev)%x2l(baseprecv(ilev)%mlia(i))[37m [39;49;00m+[37m [39;49;00m&[37m[39;49;00m$
   233^I[37m               [39;49;00m&[37m  [39;49;00mmlprec_wrk(ilev-[34m1[39;49;00m)%x2l(i)[37m[39;49;00m$
   234^I[37m        [39;49;00m[34mend [39;49;00m[34mdo[39;49;00m$
   235^I[34m[39;49;00m$
   236^I[34m      [39;49;00m[34mend [39;49;00m[34mif[39;49;00m$
   237^I[34m[39;49;00m$
   238^I[34m      [39;49;00m[34mif[39;49;00m[37m [39;49;00m(baseprecv(ilev)%iprcparm(coarse_mat_)==mat_repl_)[37m [39;49;00m[34mThen[39;49;00m$
   239^I[34m        [39;49;00m[34mcall [39;49;00mpsb_sum(ictxt,mlprec_wrk(ilev)%x2l([34m1[39;49;00m:nrg))[37m[39;49;00m$
   240^I[37m      [39;49;00m[34melse [39;49;00m[34mif[39;49;00m[37m [39;49;00m(baseprecv(ilev)%iprcparm(coarse_mat_)[37m [39;49;00m/=[37m [39;49;00mmat_distr_)[37m [39;49;00m[34mThen[39;49;00m$
   241^I[34m        [39;49;00m[34mwrite[39;49;00m([34m0[39;49;00m,*)[37m [39;49;00m[33m'Unknown value for baseprecv(2)%iprcparm(coarse_mat_) '[39;49;00m,&[37m[39;49;00m$
   242^I[37m             [39;49;00m&[37m [39;49;00mbaseprecv(ilev)%iprcparm(coarse_mat_)[37m[39;49;00m$
   243^I[37m      [39;49;00m[34mendif[39;49;00m$
   244^I[34m[39;49;00m$
   245^I[34m      [39;49;00m[34mcall [39;49;00mpsb_baseprc_aply(zone,baseprecv(ilev),&[37m[39;49;00m$
   246^I[37m           [39;49;00m&[37m [39;49;00mmlprec_wrk(ilev)%x2l,zzero,mlprec_wrk(ilev)%y2l,&[37m[39;49;00m$
   247^I[37m           [39;49;00m&[37m [39;49;00mbaseprecv(ilev)%desc_data,[37m [39;49;00m[33m'N'[39;49;00m,work,info)[37m[39;49;00m$
   248^I[37m[39;49;00m$
   249^I[37m    [39;49;00m[34menddo[39;49;00m$
   250^I[34m[39;49;00m$
   251^I[34m    [39;49;00m[34mdo [39;49;00milev[37m [39;49;00m=nlev,[34m2[39;49;00m,-[34m1[39;49;00m[37m[39;49;00m$
   252^I[37m[39;49;00m$
   253^I[37m      [39;49;00mismth=baseprecv(ilev)%iprcparm(smth_kind_)[37m[39;49;00m$
   254^I[37m      [39;49;00mn_row[37m [39;49;00m=[37m [39;49;00mbaseprecv(ilev-[34m1[39;49;00m)%base_desc%matrix_data(psb_n_row_)[37m[39;49;00m$
   255^I[37m      [39;49;00mn_col[37m [39;49;00m=[37m [39;49;00mbaseprecv(ilev-[34m1[39;49;00m)%desc_data%matrix_data(psb_n_col_)[37m[39;49;00m$
   256^I[37m      [39;49;00mnr2l[37m  [39;49;00m=[37m [39;49;00mbaseprecv(ilev)%desc_data%matrix_data(psb_n_col_)[37m[39;49;00m$
   257^I[37m      [39;49;00mnrg[37m   [39;49;00m=[37m [39;49;00mbaseprecv(ilev)%desc_data%matrix_data(psb_n_row_)[37m[39;49;00m$
   258^I[37m[39;49;00m$
   259^I[37m      [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ismth[37m  [39;49;00m/=[37m [39;49;00mno_smth_)[37m [39;49;00m[34mthen[39;49;00m$
   260^I[34m[39;49;00m$
   261^I[34m        [39;49;00m[34mcall [39;49;00mpsb_csmm(zone,baseprecv(ilev)%av(sm_pr_),mlprec_wrk(ilev)%y2l,&[37m[39;49;00m$
   262^I[37m             [39;49;00m&[37m [39;49;00mzone,mlprec_wrk(ilev-[34m1[39;49;00m)%y2l,info)[37m[39;49;00m$
   263^I[37m        [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m$
   264^I[37m[39;49;00m$
   265^I[37m      [39;49;00m[34melse[39;49;00m$
   266^I[34m[39;49;00m$
   267^I[34m        [39;49;00m[34mdo [39;49;00mi=[34m1[39;49;00m,[37m [39;49;00mn_row[37m[39;49;00m$
   268^I[37m          [39;49;00mmlprec_wrk(ilev-[34m1[39;49;00m)%y2l(i)[37m [39;49;00m=[37m [39;49;00mmlprec_wrk(ilev-[34m1[39;49;00m)%y2l(i)[37m [39;49;00m+[37m [39;49;00m&[37m[39;49;00m$
   269^I[37m               [39;49;00m&[37m   [39;49;00mmlprec_wrk(ilev)%y2l(baseprecv(ilev)%mlia(i))[37m[39;49;00m$
   270^I[37m        [39;49;00m[34menddo[39;49;00m$
   271^I[34m[39;49;00m$
   272^I[34m      [39;49;00m[34mend [39;49;00m[34mif[39;49;00m$
   273^I[34m    [39;49;00m[34mend [39;49;00m[34mdo[39;49;00m$
   274^I[34m[39;49;00m$
   275^I[34m    [39;49;00m[34mcall [39;49;00mpsb_geaxpby(alpha,mlprec_wrk([34m1[39;49;00m)%y2l,zone,y,baseprecv([34m1[39;49;00m)%base_desc,info)[37m[39;49;00m$
   276^I[37m    [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m$
   277^I[37m[39;49;00m$
   278^I[37m[39;49;00m$
   279^I[37m  [39;49;00m[34mcase[39;49;00m(mult_ml_prec_)[37m[39;49;00m$
   280^I[37m[39;49;00m$
   281^I[37m    [39;49;00m[37m![39;49;00m$
   282^I[37m    [39;49;00m[37m!  Multiplicative multilevel[39;49;00m$
   283^I[37m    [39;49;00m[37m!  Pre/post smoothing versions.[39;49;00m$
   284^I[37m    [39;49;00m[37m![39;49;00m$
   285^I[37m[39;49;00m$
   286^I[37m    [39;49;00m[34mselect [39;49;00m[34mcase[39;49;00m(baseprecv([34m2[39;49;00m)%iprcparm(smth_pos_))[37m[39;49;00m$
   287^I[37m[39;49;00m$
   288^I[37m    [39;49;00m[34mcase[39;49;00m(post_smooth_)[37m[39;49;00m$
   289^I[37m[39;49;00m$
   290^I[37m[39;49;00m$
   291^I[37m      [39;49;00m[37m![39;49;00m$
   292^I[37m      [39;49;00m[37m!    Post smoothing.[39;49;00m$
   293^I[37m      [39;49;00m[37m!    1.   X(1) = Xext[39;49;00m$
   294^I[37m      [39;49;00m[37m!    2.   DO ILEV=2, NLEV :: X(ILEV) = AV(PR_SM_T_,ILEV)*X(ILEV-1)[39;49;00m$
   295^I[37m      [39;49;00m[37m!    3.   Y(NLEV) = (K(NLEV)**(-1))*X(NLEV)[39;49;00m$
   296^I[37m      [39;49;00m[37m!    4.   DO  ILEV=NLEV-1,1,-1[39;49;00m$
   297^I[37m      [39;49;00m[37m!          Y(ILEV) = AV(PR_SM_,ILEV+1)*Y(ILEV+1)[39;49;00m$
   298^I[37m      [39;49;00m[37m!          Y(ILEV) = Y(ILEV) + (K(ILEV)**(-1))*(X(ILEV)-A(ILEV)*Y(ILEV))[39;49;00m$
   299^I[37m      [39;49;00m[37m![39;49;00m$
   300^I[37m      [39;49;00m[37m!    5.  Yext    = beta*Yext + Y(1)[39;49;00m$
   301^I[37m      [39;49;00m[37m![39;49;00m$
   302^I[37m      [39;49;00m[37m!    Note: level numbering reversed wrt ref. DD, i.e.[39;49;00m$
   303^I[37m      [39;49;00m[37m!         1..NLEV <=>  (j) <-> 0[39;49;00m$
   304^I[37m      [39;49;00m[37m![39;49;00m$
   305^I[37m      [39;49;00m[37m!    Also: post smoothing is not spelled out in detail in DD.[39;49;00m$
   306^I[37m      [39;49;00m[37m![39;49;00m$
   307^I[37m      [39;49;00m[37m![39;49;00m$
   308^I[37m[39;49;00m$
   309^I[37m[39;49;00m$
   310^I[37m      [39;49;00mn_col[37m [39;49;00m=[37m [39;49;00mdesc_data%matrix_data(psb_n_col_)[37m[39;49;00m$
   311^I[37m      [39;49;00mnr2l[37m  [39;49;00m=[37m [39;49;00mbaseprecv([34m1[39;49;00m)%desc_data%matrix_data(psb_n_col_)[37m[39;49;00m$
   312^I[37m[39;49;00m$
   313^I[37m      [39;49;00m[34mallocate[39;49;00m(mlprec_wrk([34m1[39;49;00m)%x2l(nr2l),mlprec_wrk([34m1[39;49;00m)%y2l(nr2l),[37m [39;49;00m&[37m[39;49;00m$
   314^I[37m           [39;49;00m&[37m [39;49;00mmlprec_wrk([34m1[39;49;00m)%tx(nr2l),[37m [39;49;00m[36mstat[39;49;00m=info)[37m[39;49;00m$
   315^I[37m      [39;49;00mmlprec_wrk([34m1[39;49;00m)%x2l(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m$
   316^I[37m      [39;49;00mmlprec_wrk([34m1[39;49;00m)%y2l(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m$
   317^I[37m      [39;49;00mmlprec_wrk([34m1[39;49;00m)%tx(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m$
   318^I[37m[39;49;00m$
   319^I[37m      [39;49;00m[34mcall [39;49;00mpsb_geaxpby(zone,x,zzero,mlprec_wrk([34m1[39;49;00m)%tx,&[37m[39;49;00m$
   320^I[37m           [39;49;00m&[37m [39;49;00mbaseprecv([34m1[39;49;00m)%base_desc,info)[37m[39;49;00m$
   321^I[37m      [39;49;00m[34mcall [39;49;00mpsb_geaxpby(zone,x,zzero,mlprec_wrk([34m1[39;49;00m)%x2l,&[37m[39;49;00m$
   322^I[37m           [39;49;00m&[37m [39;49;00mbaseprecv([34m1[39;49;00m)%base_desc,info)[37m[39;49;00m$
   323^I[37m[39;49;00m$
   324^I[37m      [39;49;00m[34mdo [39;49;00milev=[34m2[39;49;00m,[37m [39;49;00mnlev[37m[39;49;00m$
   325^I[37m        [39;49;00mn_row[37m [39;49;00m=[37m [39;49;00mbaseprecv(ilev-[34m1[39;49;00m)%base_desc%matrix_data(psb_n_row_)[37m[39;49;00m$
   326^I[37m        [39;49;00mn_col[37m [39;49;00m=[37m [39;49;00mbaseprecv(ilev-[34m1[39;49;00m)%desc_data%matrix_data(psb_n_col_)[37m[39;49;00m$
   327^I[37m        [39;49;00mnr2l[37m  [39;49;00m=[37m [39;49;00mbaseprecv(ilev)%desc_data%matrix_data(psb_n_col_)[37m[39;49;00m$
   328^I[37m        [39;49;00mnrg[37m   [39;49;00m=[37m [39;49;00mbaseprecv(ilev)%desc_data%matrix_data(psb_n_row_)[37m[39;49;00m$
   329^I[37m        [39;49;00mismth[37m [39;49;00m=[37m [39;49;00mbaseprecv(ilev)%iprcparm(smth_kind_)[37m[39;49;00m$
   330^I[37m[39;49;00m$
   331^I[37m        [39;49;00m[34mallocate[39;49;00m(mlprec_wrk(ilev)%tx(nr2l),mlprec_wrk(ilev)%y2l(nr2l),&[37m[39;49;00m$
   332^I[37m             [39;49;00m&[37m   [39;49;00mmlprec_wrk(ilev)%x2l(nr2l),[37m [39;49;00m[36mstat[39;49;00m=info)[37m[39;49;00m$
   333^I[37m[39;49;00m$
   334^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(info[37m [39;49;00m/=[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mthen[39;49;00m$
   335^I[34m          [39;49;00m[34mcall [39;49;00mpsb_errpush([34m4010[39;49;00m,name,a_err=[33m'Allocate'[39;49;00m)[37m[39;49;00m$
   336^I[37m          [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m$
   337^I[37m        [39;49;00m[34mend [39;49;00m[34mif[39;49;00m$
   338^I[34m[39;49;00m$
   339^I[34m        [39;49;00mmlprec_wrk(ilev)%x2l(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m$
   340^I[37m        [39;49;00mmlprec_wrk(ilev)%y2l(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m$
   341^I[37m        [39;49;00mmlprec_wrk(ilev)%tx(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m$
   342^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ismth[37m  [39;49;00m/=[37m [39;49;00mno_smth_)[37m [39;49;00m[34mthen[39;49;00m[37m[39;49;00m$
   343^I[37m          [39;49;00m[37m![39;49;00m$
   344^I[37m          [39;49;00m[37m! Smoothed aggregation[39;49;00m$
   345^I[37m          [39;49;00m[37m![39;49;00m$
   346^I[37m          [39;49;00m[34mif[39;49;00m[37m [39;49;00m(baseprecv(ilev)%iprcparm(glb_smth_)[37m [39;49;00m>[34m0[39;49;00m)[37m [39;49;00m[34mthen[39;49;00m$
   347^I[34m            [39;49;00m[34mcall [39;49;00mpsb_halo(mlprec_wrk(ilev-[34m1[39;49;00m)%x2l,&[37m[39;49;00m$
   348^I[37m                 [39;49;00m&[37m  [39;49;00mbaseprecv(ilev-[34m1[39;49;00m)%base_desc,info,work=work)[37m[39;49;00m$
   349^I[37m            [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m$
   350^I[37m          [39;49;00m[34melse[39;49;00m$
   351^I[34m            [39;49;00mmlprec_wrk(ilev-[34m1[39;49;00m)%x2l(n_row+[34m1[39;49;00m:[36mmax[39;49;00m(n_row,n_col))[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m$
   352^I[37m          [39;49;00m[34mend [39;49;00m[34mif[39;49;00m$
   353^I[34m[39;49;00m$
   354^I[34m          [39;49;00m[34mcall [39;49;00mpsb_csmm(zone,baseprecv(ilev)%av(sm_pr_t_),mlprec_wrk(ilev-[34m1[39;49;00m)%x2l,[37m [39;49;00m&[37m[39;49;00m$
   355^I[37m               [39;49;00m&[37m [39;49;00mzzero,mlprec_wrk(ilev)%x2l,info)[37m[39;49;00m$
   356^I[37m          [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m$
   357^I[37m[39;49;00m$
   358^I[37m        [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
   359^I[37m          [39;49;00m[37m![39;49;00m$
   360^I[37m          [39;49;00m[37m! Raw  aggregation, may take shortcut[39;49;00m$
   361^I[37m          [39;49;00m[37m![39;49;00m$
   362^I[37m          [39;49;00m[34mdo [39;49;00mi=[34m1[39;49;00m,n_row[37m[39;49;00m$
   363^I[37m            [39;49;00mmlprec_wrk(ilev)%x2l(baseprecv(ilev)%mlia(i))[37m [39;49;00m=[37m [39;49;00m&[37m[39;49;00m$
   364^I[37m                 [39;49;00m&[37m [39;49;00mmlprec_wrk(ilev)%x2l(baseprecv(ilev)%mlia(i))[37m [39;49;00m+[37m [39;49;00m&[37m[39;49;00m$
   365^I[37m                 [39;49;00m&[37m [39;49;00mmlprec_wrk(ilev-[34m1[39;49;00m)%x2l(i)[37m[39;49;00m$
   366^I[37m          [39;49;00m[34mend [39;49;00m[34mdo[39;49;00m$
   367^I[34m        [39;49;00m[34mend [39;49;00m[34mif[39;49;00m$
   368^I[34m[39;49;00m$
   369^I[34m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(baseprecv(ilev)%iprcparm(coarse_mat_)==mat_repl_)[37m [39;49;00m[34mThen[39;49;00m$
   370^I[34m          [39;49;00m[34mcall [39;49;00mpsb_sum(ictxt,mlprec_wrk(ilev)%x2l([34m1[39;49;00m:nrg))[37m[39;49;00m$
   371^I[37m        [39;49;00m[34melse [39;49;00m[34mif[39;49;00m[37m [39;49;00m(baseprecv(ilev)%iprcparm(coarse_mat_)[37m [39;49;00m/=[37m [39;49;00mmat_distr_)[37m [39;49;00m[34mThen[39;49;00m$
   372^I[34m          [39;49;00m[34mwrite[39;49;00m([34m0[39;49;00m,*)[37m [39;49;00m[33m'Unknown value for baseprecv(2)%iprcparm(coarse_mat_) '[39;49;00m,&[37m[39;49;00m$
   373^I[37m               [39;49;00m&[37m [39;49;00mbaseprecv(ilev)%iprcparm(coarse_mat_)[37m[39;49;00m$
   374^I[37m        [39;49;00m[34mendif[39;49;00m$
   375^I[34m        [39;49;00m[34mcall [39;49;00mpsb_geaxpby(zone,mlprec_wrk(ilev)%x2l,zzero,mlprec_wrk(ilev)%tx,&[37m[39;49;00m$
   376^I[37m             [39;49;00m&[37m [39;49;00mbaseprecv(ilev)%base_desc,info)[37m[39;49;00m$
   377^I[37m        [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m$
   378^I[37m[39;49;00m$
   379^I[37m      [39;49;00m[34menddo[39;49;00m$
   380^I[34m[39;49;00m$
   381^I[34m[39;49;00m$
   382^I[34m      [39;49;00m[34mcall [39;49;00mpsb_baseprc_aply(zone,baseprecv(nlev),mlprec_wrk(nlev)%x2l,[37m [39;49;00m&[37m[39;49;00m$
   383^I[37m           [39;49;00m&[37m [39;49;00mzzero,[37m [39;49;00mmlprec_wrk(nlev)%y2l,baseprecv(nlev)%desc_data,[33m'N'[39;49;00m,work,info)[37m[39;49;00m$
   384^I[37m[39;49;00m$
   385^I[37m      [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m$
   386^I[37m[39;49;00m$
   387^I[37m[39;49;00m$
   388^I[37m      [39;49;00m[34mdo [39;49;00milev=nlev-[34m1[39;49;00m,[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00m-[34m1[39;49;00m[37m[39;49;00m$
   389^I[37m        [39;49;00mismth[37m [39;49;00m=[37m [39;49;00mbaseprecv(ilev+[34m1[39;49;00m)%iprcparm(smth_kind_)[37m[39;49;00m$
   390^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ismth[37m  [39;49;00m/=[37m [39;49;00mno_smth_)[37m [39;49;00m[34mthen[39;49;00m$
   391^I[34m          [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ismth[37m [39;49;00m==[37m [39;49;00msmth_omg_)[37m [39;49;00m&[37m[39;49;00m$
   392^I[37m               [39;49;00m&[37m [39;49;00m[34mcall [39;49;00mpsb_halo(mlprec_wrk(ilev+[34m1[39;49;00m)%y2l,baseprecv(ilev+[34m1[39;49;00m)%desc_data,&[37m[39;49;00m$
   393^I[37m               [39;49;00m&[37m  [39;49;00minfo,work=work)[37m[39;49;00m$
   394^I[37m          [39;49;00m[34mcall [39;49;00mpsb_csmm(zone,baseprecv(ilev+[34m1[39;49;00m)%av(sm_pr_),mlprec_wrk(ilev+[34m1[39;49;00m)%y2l,&[37m[39;49;00m$
   395^I[37m               [39;49;00m&[37m  [39;49;00mzzero,mlprec_wrk(ilev)%y2l,info)[37m[39;49;00m$
   396^I[37m          [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m$
   397^I[37m[39;49;00m$
   398^I[37m        [39;49;00m[34melse[39;49;00m$
   399^I[34m          [39;49;00mn_row[37m [39;49;00m=[37m [39;49;00mbaseprecv(ilev)%base_desc%matrix_data(psb_n_row_)[37m[39;49;00m$
   400^I[37m          [39;49;00mmlprec_wrk(ilev)%y2l(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m$
   401^I[37m          [39;49;00m[34mdo [39;49;00mi=[34m1[39;49;00m,[37m [39;49;00mn_row[37m[39;49;00m$
   402^I[37m            [39;49;00mmlprec_wrk(ilev)%y2l(i)[37m [39;49;00m=[37m [39;49;00mmlprec_wrk(ilev)%y2l(i)[37m [39;49;00m+[37m [39;49;00m&[37m[39;49;00m$
   403^I[37m                 [39;49;00m&[37m [39;49;00mmlprec_wrk(ilev+[34m1[39;49;00m)%y2l(baseprecv(ilev+[34m1[39;49;00m)%mlia(i))[37m[39;49;00m$
   404^I[37m          [39;49;00m[34menddo[39;49;00m$
   405^I[34m[39;49;00m$
   406^I[34m        [39;49;00m[34mend [39;49;00m[34mif[39;49;00m$
   407^I[34m[39;49;00m$
   408^I[34m        [39;49;00m[34mcall [39;49;00mpsb_spmm(-zone,baseprecv(ilev)%base_a,mlprec_wrk(ilev)%y2l,&[37m[39;49;00m$
   409^I[37m             [39;49;00m&[37m   [39;49;00mzone,mlprec_wrk(ilev)%tx,baseprecv(ilev)%base_desc,info,work=work)[37m[39;49;00m$
   410^I[37m[39;49;00m$
   411^I[37m        [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m$
   412^I[37m[39;49;00m$
   413^I[37m        [39;49;00m[34mcall [39;49;00mpsb_baseprc_aply(zone,baseprecv(ilev),mlprec_wrk(ilev)%tx,&[37m[39;49;00m$
   414^I[37m             [39;49;00m&[37m [39;49;00mzone,mlprec_wrk(ilev)%y2l,baseprecv(ilev)%base_desc,[37m [39;49;00mtrans,[37m [39;49;00mwork,info)[37m[39;49;00m$
   415^I[37m[39;49;00m$
   416^I[37m        [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m$
   417^I[37m[39;49;00m$
   418^I[37m      [39;49;00m[34menddo[39;49;00m$
   419^I[34m[39;49;00m$
   420^I[34m      [39;49;00m[34mcall [39;49;00mpsb_geaxpby(alpha,mlprec_wrk([34m1[39;49;00m)%y2l,beta,y,baseprecv([34m1[39;49;00m)%base_desc,info)[37m[39;49;00m$
   421^I[37m[39;49;00m$
   422^I[37m      [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m$
   423^I[37m[39;49;00m$
   424^I[37m[39;49;00m$
   425^I[37m    [39;49;00m[34mcase[39;49;00m(pre_smooth_)[37m[39;49;00m$
   426^I[37m[39;49;00m$
   427^I[37m[39;49;00m$
   428^I[37m      [39;49;00m[37m![39;49;00m$
   429^I[37m      [39;49;00m[37m!    Pre smoothing.[39;49;00m$
   430^I[37m      [39;49;00m[37m!    1.   X(1)  = Xext[39;49;00m$
   431^I[37m      [39;49;00m[37m!    2.   Y(1)  = (K(1)**(-1))*X(1)[39;49;00m$
   432^I[37m      [39;49;00m[37m!    3.   TX(1) = X(1) - A(1)*Y(1)[39;49;00m$
   433^I[37m      [39;49;00m[37m!    4.   DO ILEV=2, NLEV[39;49;00m$
   434^I[37m      [39;49;00m[37m!          X(ILEV) = AV(PR_SM_T_,ILEV)*TX(ILEV-1)[39;49;00m$
   435^I[37m      [39;49;00m[37m!          Y(ILEV) = (K(ILEV)**(-1))*X(ILEV)[39;49;00m$
   436^I[37m      [39;49;00m[37m!          TX(ILEV) = (X(ILEV)-A(ILEV)*Y(ILEV))[39;49;00m$
   437^I[37m      [39;49;00m[37m!    5.   DO  ILEV=NLEV-1,1,-1[39;49;00m$
   438^I[37m      [39;49;00m[37m!          Y(ILEV) = Y(ILEV) + AV(PR_SM_,ILEV+1)*Y(ILEV+1)[39;49;00m$
   439^I[37m      [39;49;00m[37m!    6.  Yext    = beta*Yext + Y(1)[39;49;00m$
   440^I[37m      [39;49;00m[37m![39;49;00m$
   441^I[37m      [39;49;00m[37m!    Note: level numbering reversed wrt ref. DD, i.e.[39;49;00m$
   442^I[37m      [39;49;00m[37m!         1..NLEV <=>  (j) <-> 0[39;49;00m$
   443^I[37m      [39;49;00m[37m![39;49;00m$
   444^I[37m      [39;49;00m[37m![39;49;00m$
   445^I[37m[39;49;00m$
   446^I[37m      [39;49;00mn_col[37m [39;49;00m=[37m [39;49;00mdesc_data%matrix_data(psb_n_col_)[37m[39;49;00m$
   447^I[37m      [39;49;00mnr2l[37m  [39;49;00m=[37m [39;49;00mbaseprecv([34m1[39;49;00m)%desc_data%matrix_data(psb_n_col_)[37m[39;49;00m$
   448^I[37m[39;49;00m$
   449^I[37m      [39;49;00m[34mallocate[39;49;00m(mlprec_wrk([34m1[39;49;00m)%x2l(nr2l),mlprec_wrk([34m1[39;49;00m)%y2l(nr2l),[37m [39;49;00m&[37m[39;49;00m$
   450^I[37m           [39;49;00m&[37m [39;49;00mmlprec_wrk([34m1[39;49;00m)%tx(nr2l),[37m [39;49;00m[36mstat[39;49;00m=info)[37m[39;49;00m$
   451^I[37m      [39;49;00m[34mif[39;49;00m[37m [39;49;00m(info[37m [39;49;00m/=[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mthen[39;49;00m$
   452^I[34m        [39;49;00m[34mcall [39;49;00mpsb_errpush([34m4010[39;49;00m,name,a_err=[33m'Allocate'[39;49;00m)[37m[39;49;00m$
   453^I[37m        [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m$
   454^I[37m      [39;49;00m[34mend [39;49;00m[34mif[39;49;00m$
   455^I[34m[39;49;00m$
   456^I[34m      [39;49;00mmlprec_wrk([34m1[39;49;00m)%y2l(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m$
   457^I[37m[39;49;00m$
   458^I[37m[39;49;00m$
   459^I[37m      [39;49;00mmlprec_wrk([34m1[39;49;00m)%x2l(:)[37m [39;49;00m=[37m [39;49;00mx[37m[39;49;00m$
   460^I[37m[39;49;00m$
   461^I[37m      [39;49;00m[34mcall [39;49;00mpsb_baseprc_aply(zone,baseprecv([34m1[39;49;00m),mlprec_wrk([34m1[39;49;00m)%x2l,&[37m[39;49;00m$
   462^I[37m           [39;49;00m&[37m  [39;49;00mzzero,mlprec_wrk([34m1[39;49;00m)%y2l,&[37m[39;49;00m$
   463^I[37m           [39;49;00m&[37m  [39;49;00mbaseprecv([34m1[39;49;00m)%base_desc,&[37m[39;49;00m$
   464^I[37m           [39;49;00m&[37m  [39;49;00mtrans,work,info)[37m[39;49;00m$
   465^I[37m[39;49;00m$
   466^I[37m      [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m$
   467^I[37m[39;49;00m$
   468^I[37m      [39;49;00mmlprec_wrk([34m1[39;49;00m)%tx[37m [39;49;00m=[37m [39;49;00mmlprec_wrk([34m1[39;49;00m)%x2l[37m[39;49;00m$
   469^I[37m[39;49;00m$
   470^I[37m      [39;49;00m[34mcall [39;49;00mpsb_spmm(-zone,baseprecv([34m1[39;49;00m)%base_a,mlprec_wrk([34m1[39;49;00m)%y2l,&[37m[39;49;00m$
   471^I[37m           [39;49;00m&[37m [39;49;00mzone,mlprec_wrk([34m1[39;49;00m)%tx,baseprecv([34m1[39;49;00m)%base_desc,info,work=work)[37m[39;49;00m$
   472^I[37m      [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m$
   473^I[37m[39;49;00m$
   474^I[37m      [39;49;00m[34mdo [39;49;00milev[37m [39;49;00m=[37m [39;49;00m[34m2[39;49;00m,[37m [39;49;00mnlev[37m[39;49;00m$
   475^I[37m        [39;49;00mn_row[37m [39;49;00m=[37m [39;49;00mbaseprecv(ilev-[34m1[39;49;00m)%base_desc%matrix_data(psb_n_row_)[37m[39;49;00m$
   476^I[37m        [39;49;00mn_col[37m [39;49;00m=[37m [39;49;00mbaseprecv(ilev-[34m1[39;49;00m)%desc_data%matrix_data(psb_n_col_)[37m[39;49;00m$
   477^I[37m        [39;49;00mnr2l[37m  [39;49;00m=[37m [39;49;00mbaseprecv(ilev)%desc_data%matrix_data(psb_n_col_)[37m[39;49;00m$
   478^I[37m        [39;49;00mnrg[37m   [39;49;00m=[37m [39;49;00mbaseprecv(ilev)%desc_data%matrix_data(psb_n_row_)[37m[39;49;00m$
   479^I[37m        [39;49;00mismth[37m [39;49;00m=[37m [39;49;00mbaseprecv(ilev)%iprcparm(smth_kind_)[37m[39;49;00m$
   480^I[37m        [39;49;00m[34mallocate[39;49;00m(mlprec_wrk(ilev)%tx(nr2l),mlprec_wrk(ilev)%y2l(nr2l),&[37m[39;49;00m$
   481^I[37m             [39;49;00m&[37m   [39;49;00mmlprec_wrk(ilev)%x2l(nr2l),[37m [39;49;00m[36mstat[39;49;00m=info)[37m[39;49;00m$
   482^I[37m[39;49;00m$
   483^I[37m[39;49;00m$
   484^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(info[37m [39;49;00m/=[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mthen[39;49;00m$
   485^I[34m          [39;49;00m[34mcall [39;49;00mpsb_errpush([34m4010[39;49;00m,name,a_err=[33m'Allocate'[39;49;00m)[37m[39;49;00m$
   486^I[37m          [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m$
   487^I[37m        [39;49;00m[34mend [39;49;00m[34mif[39;49;00m$
   488^I[34m[39;49;00m$
   489^I[34m        [39;49;00mmlprec_wrk(ilev)%x2l(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m$
   490^I[37m        [39;49;00mmlprec_wrk(ilev)%y2l(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m$
   491^I[37m        [39;49;00mmlprec_wrk(ilev)%tx(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m$
   492^I[37m[39;49;00m$
   493^I[37m[39;49;00m$
   494^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ismth[37m  [39;49;00m/=[37m [39;49;00mno_smth_)[37m [39;49;00m[34mthen[39;49;00m[37m[39;49;00m$
   495^I[37m          [39;49;00m[37m![39;49;00m$
   496^I[37m          [39;49;00m[37m!Smoothed Aggregation[39;49;00m$
   497^I[37m          [39;49;00m[37m![39;49;00m$
   498^I[37m          [39;49;00m[34mif[39;49;00m[37m [39;49;00m(baseprecv(ilev)%iprcparm(glb_smth_)[37m [39;49;00m>[34m0[39;49;00m)[37m [39;49;00m[34mthen[39;49;00m$
   499^I[34m[39;49;00m$
   500^I[34m            [39;49;00m[34mcall [39;49;00mpsb_halo(mlprec_wrk(ilev-[34m1[39;49;00m)%tx,baseprecv(ilev-[34m1[39;49;00m)%base_desc,&[37m[39;49;00m$
   501^I[37m                 [39;49;00m&[37m [39;49;00minfo,work=work)[37m[39;49;00m$
   502^I[37m            [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m$
   503^I[37m          [39;49;00m[34melse[39;49;00m$
   504^I[34m            [39;49;00mmlprec_wrk(ilev-[34m1[39;49;00m)%tx(n_row+[34m1[39;49;00m:[36mmax[39;49;00m(n_row,n_col))[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m$
   505^I[37m          [39;49;00m[34mend [39;49;00m[34mif[39;49;00m$
   506^I[34m[39;49;00m$
   507^I[34m          [39;49;00m[34mcall [39;49;00mpsb_csmm(zone,baseprecv(ilev)%av(sm_pr_t_),mlprec_wrk(ilev-[34m1[39;49;00m)%tx,zzero,&[37m[39;49;00m$
   508^I[37m               [39;49;00m&[37m [39;49;00mmlprec_wrk(ilev)%x2l,info)[37m[39;49;00m$
   509^I[37m          [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m$
   510^I[37m[39;49;00m$
   511^I[37m        [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
   512^I[37m          [39;49;00m[37m![39;49;00m$
   513^I[37m          [39;49;00m[37m! Raw  aggregation, may take shortcuts[39;49;00m$
   514^I[37m          [39;49;00m[37m![39;49;00m$
   515^I[37m          [39;49;00mmlprec_wrk(ilev)%x2l[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m$
   516^I[37m          [39;49;00m[34mdo [39;49;00mi=[34m1[39;49;00m,n_row[37m[39;49;00m$
   517^I[37m            [39;49;00mmlprec_wrk(ilev)%x2l(baseprecv(ilev)%mlia(i))[37m [39;49;00m=[37m [39;49;00m&[37m[39;49;00m$
   518^I[37m                 [39;49;00m&[37m [39;49;00mmlprec_wrk(ilev)%x2l(baseprecv(ilev)%mlia(i))[37m [39;49;00m+[37m [39;49;00m&[37m[39;49;00m$
   519^I[37m                 [39;49;00m&[37m  [39;49;00mmlprec_wrk(ilev-[34m1[39;49;00m)%tx(i)[37m[39;49;00m$
   520^I[37m          [39;49;00m[34mend [39;49;00m[34mdo[39;49;00m$
   521^I[34m        [39;49;00m[34mend [39;49;00m[34mif[39;49;00m$
   522^I[34m[39;49;00m$
   523^I[34m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(baseprecv(ilev)%iprcparm(coarse_mat_)==mat_repl_)[37m [39;49;00m[34mthen[39;49;00m$
   524^I[34m          [39;49;00m[34mcall [39;49;00mpsb_sum(ictxt,mlprec_wrk(ilev)%x2l([34m1[39;49;00m:nrg))[37m[39;49;00m$
   525^I[37m        [39;49;00m[34melse [39;49;00m[34mif[39;49;00m[37m [39;49;00m(baseprecv(ilev)%iprcparm(coarse_mat_)[37m [39;49;00m/=[37m [39;49;00mmat_distr_)[37m [39;49;00m[34mthen[39;49;00m$
   526^I[34m          [39;49;00m[34mwrite[39;49;00m([34m0[39;49;00m,*)[37m [39;49;00m[33m'Unknown value for baseprecv(2)%iprcparm(coarse_mat_) '[39;49;00m,&[37m[39;49;00m$
   527^I[37m               [39;49;00m&[37m [39;49;00mbaseprecv(ilev)%iprcparm(coarse_mat_)[37m[39;49;00m$
   528^I[37m        [39;49;00m[34mendif[39;49;00m$
   529^I[34m[39;49;00m$
   530^I[34m[39;49;00m$
   531^I[34m        [39;49;00m[34mcall [39;49;00mpsb_baseprc_aply(zone,baseprecv(ilev),mlprec_wrk(ilev)%x2l,&[37m[39;49;00m$
   532^I[37m             [39;49;00m&[37m [39;49;00mzzero,mlprec_wrk(ilev)%y2l,baseprecv(ilev)%desc_data,[37m [39;49;00m[33m'N'[39;49;00m,work,info)[37m[39;49;00m$
   533^I[37m[39;49;00m$
   534^I[37m        [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m$
   535^I[37m[39;49;00m$
   536^I[37m        [39;49;00m[34mif[39;49;00m(ilev[37m [39;49;00m<[37m [39;49;00mnlev)[37m [39;49;00m[34mthen[39;49;00m$
   537^I[34m          [39;49;00mmlprec_wrk(ilev)%tx[37m [39;49;00m=[37m [39;49;00mmlprec_wrk(ilev)%x2l[37m[39;49;00m$
   538^I[37m          [39;49;00m[34mcall [39;49;00mpsb_spmm(-zone,baseprecv(ilev)%base_a,mlprec_wrk(ilev)%y2l,&[37m[39;49;00m$
   539^I[37m               [39;49;00m&[37m [39;49;00mzone,mlprec_wrk(ilev)%tx,baseprecv(ilev)%base_desc,info,work=work)[37m[39;49;00m$
   540^I[37m          [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m$
   541^I[37m        [39;49;00m[34mendif[39;49;00m$
   542^I[34m[39;49;00m$
   543^I[34m      [39;49;00m[34menddo[39;49;00m$
   544^I[34m[39;49;00m$
   545^I[34m      [39;49;00m[34mdo [39;49;00milev[37m [39;49;00m=[37m [39;49;00mnlev-[34m1[39;49;00m,[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00m-[34m1[39;49;00m[37m[39;49;00m$
   546^I[37m[39;49;00m$
   547^I[37m        [39;49;00mismth=baseprecv(ilev+[34m1[39;49;00m)%iprcparm(smth_kind_)[37m[39;49;00m$
   548^I[37m[39;49;00m$
   549^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ismth[37m  [39;49;00m/=[37m [39;49;00mno_smth_)[37m [39;49;00m[34mthen[39;49;00m$
   550^I[34m[39;49;00m$
   551^I[34m          [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ismth[37m [39;49;00m==[37m [39;49;00msmth_omg_)[37m [39;49;00m&[37m[39;49;00m$
   552^I[37m               [39;49;00m&[37m [39;49;00m[34mcall [39;49;00mpsb_halo(mlprec_wrk(ilev+[34m1[39;49;00m)%y2l,&[37m[39;49;00m$
   553^I[37m               [39;49;00m&[37m [39;49;00mbaseprecv(ilev+[34m1[39;49;00m)%desc_data,info,work=work)[37m[39;49;00m$
   554^I[37m          [39;49;00m[34mcall [39;49;00mpsb_csmm(zone,baseprecv(ilev+[34m1[39;49;00m)%av(sm_pr_),mlprec_wrk(ilev+[34m1[39;49;00m)%y2l,&[37m[39;49;00m$
   555^I[37m               [39;49;00m&[37m [39;49;00mzone,mlprec_wrk(ilev)%y2l,info)[37m[39;49;00m$
   556^I[37m[39;49;00m$
   557^I[37m          [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m$
   558^I[37m[39;49;00m$
   559^I[37m        [39;49;00m[34melse[39;49;00m$
   560^I[34m[39;49;00m$
   561^I[34m          [39;49;00mn_row[37m [39;49;00m=[37m [39;49;00mbaseprecv(ilev+[34m1[39;49;00m)%base_desc%matrix_data(psb_n_row_)[37m[39;49;00m$
   562^I[37m          [39;49;00m[34mdo [39;49;00mi=[34m1[39;49;00m,[37m [39;49;00mn_row[37m[39;49;00m$
   563^I[37m            [39;49;00mmlprec_wrk(ilev)%y2l(i)[37m [39;49;00m=[37m [39;49;00mmlprec_wrk(ilev)%y2l(i)[37m [39;49;00m+[37m [39;49;00m&[37m[39;49;00m$
   564^I[37m                 [39;49;00m&[37m [39;49;00mmlprec_wrk(ilev+[34m1[39;49;00m)%y2l(baseprecv(ilev+[34m1[39;49;00m)%mlia(i))[37m[39;49;00m$
   565^I[37m          [39;49;00m[34menddo[39;49;00m$
   566^I[34m[39;49;00m$
   567^I[34m        [39;49;00m[34mend [39;49;00m[34mif[39;49;00m$
   568^I[34m[39;49;00m$
   569^I[34m      [39;49;00m[34menddo[39;49;00m$
   570^I[34m[39;49;00m$
   571^I[34m      [39;49;00m[34mcall [39;49;00mpsb_geaxpby(alpha,mlprec_wrk([34m1[39;49;00m)%y2l,beta,y,&[37m[39;49;00m$
   572^I[37m           [39;49;00m&[37m  [39;49;00mbaseprecv([34m1[39;49;00m)%base_desc,info)[37m[39;49;00m$
   573^I[37m[39;49;00m$
   574^I[37m      [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m$
   575^I[37m[39;49;00m$
   576^I[37m[39;49;00m$
   577^I[37m[39;49;00m$
   578^I[37m    [39;49;00m[34mcase[39;49;00m(smooth_both_)[37m[39;49;00m$
   579^I[37m[39;49;00m$
   580^I[37m      [39;49;00m[37m![39;49;00m$
   581^I[37m      [39;49;00m[37m!    Symmetrized  smoothing.[39;49;00m$
   582^I[37m      [39;49;00m[37m!    1.   X(1)  = Xext[39;49;00m$
   583^I[37m      [39;49;00m[37m!    2.   Y(1)  = (K(1)**(-1))*X(1)[39;49;00m$
   584^I[37m      [39;49;00m[37m!    3.   TX(1) = X(1) - A(1)*Y(1)[39;49;00m$
   585^I[37m      [39;49;00m[37m!    4.   DO ILEV=2, NLEV[39;49;00m$
   586^I[37m      [39;49;00m[37m!          X(ILEV) = AV(PR_SM_T_,ILEV)*TX(ILEV-1)[39;49;00m$
   587^I[37m      [39;49;00m[37m!          Y(ILEV) = (K(ILEV)**(-1))*X(ILEV)[39;49;00m$
   588^I[37m      [39;49;00m[37m!          TX(ILEV) = (X(ILEV)-A(ILEV)*Y(ILEV))[39;49;00m$
   589^I[37m      [39;49;00m[37m!    5.   DO  ILEV=NLEV-1,1,-1[39;49;00m$
   590^I[37m      [39;49;00m[37m!          Y(ILEV) = Y(ILEV) + AV(PR_SM_,ILEV+1)*Y(ILEV+1)[39;49;00m$
   591^I[37m      [39;49;00m[37m!          Y(ILEV) = Y(ILEV) + (K(ILEV)**(-1))*(X(ILEV)-A(ILEV)*Y(ILEV))[39;49;00m$
   592^I[37m      [39;49;00m[37m!    6.  Yext    = beta*Yext + Y(1)[39;49;00m$
   593^I[37m      [39;49;00m[37m![39;49;00m$
   594^I[37m      [39;49;00m[37m!    Note: level numbering reversed wrt ref. DD, i.e.[39;49;00m$
   595^I[37m      [39;49;00m[37m!         1..NLEV <=>  (j) <-> 0[39;49;00m$
   596^I[37m      [39;49;00m[37m![39;49;00m$
   597^I[37m      [39;49;00m[37m![39;49;00m$
   598^I[37m      [39;49;00mn_col[37m [39;49;00m=[37m [39;49;00mdesc_data%matrix_data(psb_n_col_)[37m[39;49;00m$
   599^I[37m      [39;49;00mnr2l[37m  [39;49;00m=[37m [39;49;00mbaseprecv([34m1[39;49;00m)%desc_data%matrix_data(psb_n_col_)[37m[39;49;00m$
   600^I[37m[39;49;00m$
   601^I[37m      [39;49;00m[34mallocate[39;49;00m(mlprec_wrk([34m1[39;49;00m)%x2l(nr2l),mlprec_wrk([34m1[39;49;00m)%y2l(nr2l),[37m [39;49;00m&[37m[39;49;00m$
   602^I[37m           [39;49;00m&[37m [39;49;00mmlprec_wrk([34m1[39;49;00m)%ty(nr2l),[37m [39;49;00mmlprec_wrk([34m1[39;49;00m)%tx(nr2l),[37m [39;49;00m[36mstat[39;49;00m=info)[37m[39;49;00m$
   603^I[37m[39;49;00m$
   604^I[37m      [39;49;00mmlprec_wrk([34m1[39;49;00m)%x2l(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m$
   605^I[37m      [39;49;00mmlprec_wrk([34m1[39;49;00m)%y2l(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m$
   606^I[37m      [39;49;00mmlprec_wrk([34m1[39;49;00m)%tx(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m$
   607^I[37m      [39;49;00mmlprec_wrk([34m1[39;49;00m)%ty(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m$
   608^I[37m[39;49;00m$
   609^I[37m[39;49;00m$
   610^I[37m      [39;49;00m[34mif[39;49;00m[37m [39;49;00m(info[37m [39;49;00m/=[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mthen[39;49;00m$
   611^I[34m        [39;49;00m[34mcall [39;49;00mpsb_errpush([34m4010[39;49;00m,name,a_err=[33m'Allocate'[39;49;00m)[37m[39;49;00m$
   612^I[37m        [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m$
   613^I[37m      [39;49;00m[34mend [39;49;00m[34mif[39;49;00m$
   614^I[34m[39;49;00m$
   615^I[34m      [39;49;00m[34mcall [39;49;00mpsb_geaxpby(zone,x,zzero,mlprec_wrk([34m1[39;49;00m)%x2l,&[37m[39;49;00m$
   616^I[37m           [39;49;00m&[37m [39;49;00mbaseprecv([34m1[39;49;00m)%base_desc,info)[37m[39;49;00m$
   617^I[37m      [39;49;00m[34mcall [39;49;00mpsb_geaxpby(zone,x,zzero,mlprec_wrk([34m1[39;49;00m)%tx,&[37m[39;49;00m$
   618^I[37m           [39;49;00m&[37m [39;49;00mbaseprecv([34m1[39;49;00m)%base_desc,info)[37m[39;49;00m$
   619^I[37m[39;49;00m$
   620^I[37m      [39;49;00m[34mcall [39;49;00mpsb_baseprc_aply(zone,baseprecv([34m1[39;49;00m),mlprec_wrk([34m1[39;49;00m)%x2l,&[37m[39;49;00m$
   621^I[37m           [39;49;00m&[37m  [39;49;00mzzero,mlprec_wrk([34m1[39;49;00m)%y2l,&[37m[39;49;00m$
   622^I[37m           [39;49;00m&[37m  [39;49;00mbaseprecv([34m1[39;49;00m)%base_desc,&[37m[39;49;00m$
   623^I[37m           [39;49;00m&[37m  [39;49;00mtrans,work,info)[37m[39;49;00m$
   624^I[37m[39;49;00m$
   625^I[37m      [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m$
   626^I[37m[39;49;00m$
   627^I[37m      [39;49;00mmlprec_wrk([34m1[39;49;00m)%ty[37m [39;49;00m=[37m [39;49;00mmlprec_wrk([34m1[39;49;00m)%x2l[37m[39;49;00m$
   628^I[37m[39;49;00m$
   629^I[37m      [39;49;00m[34mcall [39;49;00mpsb_spmm(-zone,baseprecv([34m1[39;49;00m)%base_a,mlprec_wrk([34m1[39;49;00m)%y2l,&[37m[39;49;00m$
   630^I[37m           [39;49;00m&[37m [39;49;00mzone,mlprec_wrk([34m1[39;49;00m)%ty,baseprecv([34m1[39;49;00m)%base_desc,info,work=work)[37m[39;49;00m$
   631^I[37m      [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m$
   632^I[37m[39;49;00m$
   633^I[37m      [39;49;00m[34mdo [39;49;00milev[37m [39;49;00m=[37m [39;49;00m[34m2[39;49;00m,[37m [39;49;00mnlev[37m[39;49;00m$
   634^I[37m        [39;49;00mn_row[37m [39;49;00m=[37m [39;49;00mbaseprecv(ilev-[34m1[39;49;00m)%base_desc%matrix_data(psb_n_row_)[37m[39;49;00m$
   635^I[37m        [39;49;00mn_col[37m [39;49;00m=[37m [39;49;00mbaseprecv(ilev-[34m1[39;49;00m)%desc_data%matrix_data(psb_n_col_)[37m[39;49;00m$
   636^I[37m        [39;49;00mnr2l[37m  [39;49;00m=[37m [39;49;00mbaseprecv(ilev)%desc_data%matrix_data(psb_n_col_)[37m[39;49;00m$
   637^I[37m        [39;49;00mnrg[37m   [39;49;00m=[37m [39;49;00mbaseprecv(ilev)%desc_data%matrix_data(psb_n_row_)[37m[39;49;00m$
   638^I[37m        [39;49;00mismth=baseprecv(ilev)%iprcparm(smth_kind_)[37m[39;49;00m$
   639^I[37m        [39;49;00m[34mallocate[39;49;00m(mlprec_wrk(ilev)%ty(nr2l),mlprec_wrk(ilev)%y2l(nr2l),&[37m[39;49;00m$
   640^I[37m             [39;49;00m&[37m   [39;49;00mmlprec_wrk(ilev)%x2l(nr2l),[37m [39;49;00m[36mstat[39;49;00m=info)[37m[39;49;00m$
   641^I[37m[39;49;00m$
   642^I[37m        [39;49;00mmlprec_wrk(ilev)%x2l(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m$
   643^I[37m        [39;49;00mmlprec_wrk(ilev)%y2l(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m$
   644^I[37m        [39;49;00mmlprec_wrk(ilev)%tx(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m$
   645^I[37m        [39;49;00mmlprec_wrk(ilev)%ty(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m$
   646^I[37m[39;49;00m$
   647^I[37m[39;49;00m$
   648^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(info[37m [39;49;00m/=[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mthen[39;49;00m$
   649^I[34m          [39;49;00m[34mcall [39;49;00mpsb_errpush([34m4010[39;49;00m,name,a_err=[33m'Allocate'[39;49;00m)[37m[39;49;00m$
   650^I[37m          [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m$
   651^I[37m        [39;49;00m[34mend [39;49;00m[34mif[39;49;00m$
   652^I[34m[39;49;00m$
   653^I[34m[39;49;00m$
   654^I[34m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ismth[37m  [39;49;00m/=[37m [39;49;00mno_smth_)[37m [39;49;00m[34mthen[39;49;00m[37m[39;49;00m$
   655^I[37m          [39;49;00m[37m![39;49;00m$
   656^I[37m          [39;49;00m[37m!Smoothed Aggregation[39;49;00m$
   657^I[37m          [39;49;00m[37m![39;49;00m$
   658^I[37m          [39;49;00m[34mif[39;49;00m[37m [39;49;00m(baseprecv(ilev)%iprcparm(glb_smth_)[37m [39;49;00m>[34m0[39;49;00m)[37m [39;49;00m[34mthen[39;49;00m$
   659^I[34m[39;49;00m$
   660^I[34m            [39;49;00m[34mcall [39;49;00mpsb_halo(mlprec_wrk(ilev-[34m1[39;49;00m)%ty,baseprecv(ilev-[34m1[39;49;00m)%base_desc,&[37m[39;49;00m$
   661^I[37m                 [39;49;00m&[37m [39;49;00minfo,work=work)[37m[39;49;00m$
   662^I[37m            [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m$
   663^I[37m          [39;49;00m[34melse[39;49;00m$
   664^I[34m            [39;49;00mmlprec_wrk(ilev-[34m1[39;49;00m)%ty(n_row+[34m1[39;49;00m:[36mmax[39;49;00m(n_row,n_col))[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m$
   665^I[37m          [39;49;00m[34mend [39;49;00m[34mif[39;49;00m$
   666^I[34m[39;49;00m$
   667^I[34m          [39;49;00m[34mcall [39;49;00mpsb_csmm(zone,baseprecv(ilev)%av(sm_pr_t_),mlprec_wrk(ilev-[34m1[39;49;00m)%ty,zzero,&[37m[39;49;00m$
   668^I[37m               [39;49;00m&[37m [39;49;00mmlprec_wrk(ilev)%x2l,info)[37m[39;49;00m$
   669^I[37m          [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m$
   670^I[37m[39;49;00m$
   671^I[37m        [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
   672^I[37m          [39;49;00m[37m![39;49;00m$
   673^I[37m          [39;49;00m[37m! Raw  aggregation, may take shortcuts[39;49;00m$
   674^I[37m          [39;49;00m[37m![39;49;00m$
   675^I[37m          [39;49;00mmlprec_wrk(ilev)%x2l[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m$
   676^I[37m          [39;49;00m[34mdo [39;49;00mi=[34m1[39;49;00m,n_row[37m[39;49;00m$
   677^I[37m            [39;49;00mmlprec_wrk(ilev)%x2l(baseprecv(ilev)%mlia(i))[37m [39;49;00m=[37m [39;49;00m&[37m[39;49;00m$
   678^I[37m                 [39;49;00m&[37m [39;49;00mmlprec_wrk(ilev)%x2l(baseprecv(ilev)%mlia(i))[37m [39;49;00m+[37m [39;49;00m&[37m[39;49;00m$
   679^I[37m                 [39;49;00m&[37m  [39;49;00mmlprec_wrk(ilev-[34m1[39;49;00m)%ty(i)[37m[39;49;00m$
   680^I[37m          [39;49;00m[34mend [39;49;00m[34mdo[39;49;00m$
   681^I[34m        [39;49;00m[34mend [39;49;00m[34mif[39;49;00m$
   682^I[34m[39;49;00m$
   683^I[34m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(baseprecv(ilev)%iprcparm(coarse_mat_)==mat_repl_)[37m [39;49;00m[34mthen[39;49;00m$
   684^I[34m          [39;49;00m[34mcall [39;49;00mpsb_sum(ictxt,mlprec_wrk(ilev)%x2l([34m1[39;49;00m:nrg))[37m[39;49;00m$
   685^I[37m        [39;49;00m[34melse [39;49;00m[34mif[39;49;00m[37m [39;49;00m(baseprecv(ilev)%iprcparm(coarse_mat_)[37m [39;49;00m/=[37m [39;49;00mmat_distr_)[37m [39;49;00m[34mthen[39;49;00m$
   686^I[34m          [39;49;00m[34mwrite[39;49;00m([34m0[39;49;00m,*)[37m [39;49;00m[33m'Unknown value for baseprecv(2)%iprcparm(coarse_mat_) '[39;49;00m,&[37m[39;49;00m$
   687^I[37m               [39;49;00m&[37m [39;49;00mbaseprecv(ilev)%iprcparm(coarse_mat_)[37m[39;49;00m$
   688^I[37m        [39;49;00m[34mendif[39;49;00m$
   689^I[34m[39;49;00m$
   690^I[34m        [39;49;00m[34mcall [39;49;00mpsb_geaxpby(zone,mlprec_wrk(ilev)%x2l,zzero,mlprec_wrk(ilev)%tx,&[37m[39;49;00m$
   691^I[37m             [39;49;00m&[37m [39;49;00mbaseprecv(ilev)%base_desc,info)[37m[39;49;00m$
   692^I[37m        [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m$
   693^I[37m[39;49;00m$
   694^I[37m        [39;49;00m[34mcall [39;49;00mpsb_baseprc_aply(zone,baseprecv(ilev),mlprec_wrk(ilev)%x2l,&[37m[39;49;00m$
   695^I[37m             [39;49;00m&[37m [39;49;00mzzero,mlprec_wrk(ilev)%y2l,baseprecv(ilev)%desc_data,[37m [39;49;00m[33m'N'[39;49;00m,work,info)[37m[39;49;00m$
   696^I[37m[39;49;00m$
   697^I[37m        [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m$
   698^I[37m[39;49;00m$
   699^I[37m        [39;49;00m[34mif[39;49;00m(ilev[37m [39;49;00m<[37m [39;49;00mnlev)[37m [39;49;00m[34mthen[39;49;00m$
   700^I[34m          [39;49;00mmlprec_wrk(ilev)%ty[37m [39;49;00m=[37m [39;49;00mmlprec_wrk(ilev)%x2l[37m[39;49;00m$
   701^I[37m          [39;49;00m[34mcall [39;49;00mpsb_spmm(-zone,baseprecv(ilev)%base_a,mlprec_wrk(ilev)%y2l,&[37m[39;49;00m$
   702^I[37m               [39;49;00m&[37m [39;49;00mzone,mlprec_wrk(ilev)%ty,baseprecv(ilev)%base_desc,info,work=work)[37m[39;49;00m$
   703^I[37m          [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m$
   704^I[37m        [39;49;00m[34mendif[39;49;00m$
   705^I[34m[39;49;00m$
   706^I[34m      [39;49;00m[34menddo[39;49;00m$
   707^I[34m[39;49;00m$
   708^I[34m[39;49;00m$
   709^I[34m      [39;49;00m[34mdo [39;49;00milev=nlev-[34m1[39;49;00m,[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00m-[34m1[39;49;00m[37m[39;49;00m$
   710^I[37m[39;49;00m$
   711^I[37m        [39;49;00mismth=baseprecv(ilev+[34m1[39;49;00m)%iprcparm(smth_kind_)[37m[39;49;00m$
   712^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ismth[37m  [39;49;00m/=[37m [39;49;00mno_smth_)[37m [39;49;00m[34mthen[39;49;00m$
   713^I[34m          [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ismth[37m [39;49;00m==[37m [39;49;00msmth_omg_)[37m [39;49;00m&[37m[39;49;00m$
   714^I[37m               [39;49;00m&[37m [39;49;00m[34mcall [39;49;00mpsb_halo(mlprec_wrk(ilev+[34m1[39;49;00m)%y2l,baseprecv(ilev+[34m1[39;49;00m)%desc_data,&[37m[39;49;00m$
   715^I[37m               [39;49;00m&[37m  [39;49;00minfo,work=work)[37m[39;49;00m$
   716^I[37m          [39;49;00m[34mcall [39;49;00mpsb_csmm(zone,baseprecv(ilev+[34m1[39;49;00m)%av(sm_pr_),mlprec_wrk(ilev+[34m1[39;49;00m)%y2l,&[37m[39;49;00m$
   717^I[37m               [39;49;00m&[37m  [39;49;00mzone,mlprec_wrk(ilev)%y2l,info)[37m[39;49;00m$
   718^I[37m          [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m$
   719^I[37m[39;49;00m$
   720^I[37m        [39;49;00m[34melse[39;49;00m$
   721^I[34m          [39;49;00mn_row[37m [39;49;00m=[37m [39;49;00mbaseprecv(ilev)%base_desc%matrix_data(psb_n_row_)[37m[39;49;00m$
   722^I[37m          [39;49;00m[34mdo [39;49;00mi=[34m1[39;49;00m,[37m [39;49;00mn_row[37m[39;49;00m$
   723^I[37m            [39;49;00mmlprec_wrk(ilev)%y2l(i)[37m [39;49;00m=[37m [39;49;00mmlprec_wrk(ilev)%y2l(i)[37m [39;49;00m+[37m [39;49;00m&[37m[39;49;00m$
   724^I[37m                 [39;49;00m&[37m [39;49;00mmlprec_wrk(ilev+[34m1[39;49;00m)%y2l(baseprecv(ilev+[34m1[39;49;00m)%mlia(i))[37m[39;49;00m$
   725^I[37m          [39;49;00m[34menddo[39;49;00m$
   726^I[34m[39;49;00m$
   727^I[34m        [39;49;00m[34mend [39;49;00m[34mif[39;49;00m$
   728^I[34m[39;49;00m$
   729^I[34m        [39;49;00m[34mcall [39;49;00mpsb_spmm(-zone,baseprecv(ilev)%base_a,mlprec_wrk(ilev)%y2l,&[37m[39;49;00m$
   730^I[37m             [39;49;00m&[37m   [39;49;00mzone,mlprec_wrk(ilev)%tx,baseprecv(ilev)%base_desc,info,work=work)[37m[39;49;00m$
   731^I[37m[39;49;00m$
   732^I[37m        [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m$
   733^I[37m[39;49;00m$
   734^I[37m        [39;49;00m[34mcall [39;49;00mpsb_baseprc_aply(zone,baseprecv(ilev),mlprec_wrk(ilev)%tx,&[37m[39;49;00m$
   735^I[37m             [39;49;00m&[37m [39;49;00mzone,mlprec_wrk(ilev)%y2l,baseprecv(ilev)%base_desc,[37m [39;49;00mtrans,[37m [39;49;00mwork,info)[37m[39;49;00m$
   736^I[37m[39;49;00m$
   737^I[37m        [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m$
   738^I[37m[39;49;00m$
   739^I[37m      [39;49;00m[34menddo[39;49;00m$
   740^I[34m[39;49;00m$
   741^I[34m      [39;49;00m[34mcall [39;49;00mpsb_geaxpby(alpha,mlprec_wrk([34m1[39;49;00m)%y2l,beta,y,&[37m[39;49;00m$
   742^I[37m           [39;49;00m&[37m   [39;49;00mbaseprecv([34m1[39;49;00m)%base_desc,info)[37m[39;49;00m$
   743^I[37m[39;49;00m$
   744^I[37m      [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m$
   745^I[37m[39;49;00m$
   746^I[37m[39;49;00m$
   747^I[37m    [39;49;00m[34mcase [39;49;00mdefault[37m[39;49;00m$
   748^I[37m[39;49;00m$
   749^I[37m      [39;49;00m[34mcall [39;49;00mpsb_errpush([34m4013[39;49;00m,name,a_err=[33m'wrong smooth_pos'[39;49;00m,&[37m[39;49;00m$
   750^I[37m           [39;49;00m&[37m  [39;49;00mi_Err=(/baseprecv([34m2[39;49;00m)%iprcparm(smth_pos_),[34m0[39;49;00m,[34m0[39;49;00m,[34m0[39;49;00m,[34m0[39;49;00m/))[37m[39;49;00m$
   751^I[37m      [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m$
   752^I[37m[39;49;00m$
   753^I[37m    [39;49;00m[34mend [39;49;00m[34mselect[39;49;00m$
   754^I[34m[39;49;00m$
   755^I[34m  [39;49;00m[34mcase [39;49;00mdefault[37m[39;49;00m$
   756^I[37m    [39;49;00m[34mcall [39;49;00mpsb_errpush([34m4013[39;49;00m,name,a_err=[33m'wrong mltype'[39;49;00m,&[37m[39;49;00m$
   757^I[37m         [39;49;00m&[37m  [39;49;00mi_Err=(/baseprecv([34m2[39;49;00m)%iprcparm(ml_type_),[34m0[39;49;00m,[34m0[39;49;00m,[34m0[39;49;00m,[34m0[39;49;00m/))[37m[39;49;00m$
   758^I[37m    [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m$
   759^I[37m[39;49;00m$
   760^I[37m  [39;49;00m[34mend [39;49;00m[34mselect[39;49;00m$
   761^I[34m[39;49;00m$
   762^I[34m[39;49;00m$
   763^I[34m  [39;49;00m[34mcall [39;49;00mmlprec_wrk_free(mlprec_wrk)[37m[39;49;00m$
   764^I[37m  [39;49;00m[34mdeallocate[39;49;00m(mlprec_wrk)[37m[39;49;00m$
   765^I[37m[39;49;00m$
   766^I[37m  [39;49;00m[34mcall [39;49;00mpsb_erractionrestore(err_act)[37m[39;49;00m$
   767^I[37m  [39;49;00m[34mreturn[39;49;00m$
   768^I[34m[39;49;00m$
   769^I[34m9999[39;49;00m[37m [39;49;00m[34mcontinue[39;49;00m$
   770^I[34m  [39;49;00m[34mcall [39;49;00mpsb_errpush(info,name)[37m[39;49;00m$
   771^I[37m  [39;49;00m[34mcall [39;49;00mpsb_erractionrestore(err_act)[37m[39;49;00m$
   772^I[37m  [39;49;00m[34mif[39;49;00m[37m [39;49;00m(err_act.eq.act_abort)[37m [39;49;00m[34mthen[39;49;00m$
   773^I[34m    [39;49;00m[34mcall [39;49;00mpsb_error()[37m[39;49;00m$
   774^I[37m    [39;49;00m[34mreturn[39;49;00m$
   775^I[34m  [39;49;00m[34mend [39;49;00m[34mif[39;49;00m$
   776^I[34m  [39;49;00m[34mreturn[39;49;00m$
   777^I[34m[39;49;00m$
   778^I[34mcontains[39;49;00m$
   779^I[34m  [39;49;00m[34msubroutine [39;49;00mmlprec_wrk_free(wrk)[37m[39;49;00m$
   780^I[37m    [39;49;00m[34mtype[39;49;00m(psb_mlprec_wrk_type)[37m [39;49;00m[34m::[39;49;00m[37m [39;49;00mwrk(:)[37m[39;49;00m$
   781^I[37m    [39;49;00m[37m! This will not be needed when we have allocatables, as[39;49;00m$
   782^I[37m    [39;49;00m[37m! it is sufficient to deallocate the container, and[39;49;00m$
   783^I[37m    [39;49;00m[37m! the compiler is supposed to recursively deallocate the[39;49;00m$
   784^I[37m    [39;49;00m[37m! various components.[39;49;00m$
   785^I[37m    [39;49;00m[36minteger [39;49;00mi[37m[39;49;00m$
   786^I[37m[39;49;00m$
   787^I[37m    [39;49;00m[34mdo [39;49;00mi=[34m1[39;49;00m,[37m [39;49;00msize(wrk)[37m[39;49;00m$
   788^I[37m      [39;49;00m[34mif[39;49;00m[37m [39;49;00m([36massociated[39;49;00m(wrk(i)%tx))[37m  [39;49;00m[34mdeallocate[39;49;00m(wrk(i)%tx)[37m[39;49;00m$
   789^I[37m      [39;49;00m[34mif[39;49;00m[37m [39;49;00m([36massociated[39;49;00m(wrk(i)%ty))[37m  [39;49;00m[34mdeallocate[39;49;00m(wrk(i)%ty)[37m[39;49;00m$
   790^I[37m      [39;49;00m[34mif[39;49;00m[37m [39;49;00m([36massociated[39;49;00m(wrk(i)%x2l))[37m [39;49;00m[34mdeallocate[39;49;00m(wrk(i)%x2l)[37m[39;49;00m$
   791^I[37m      [39;49;00m[34mif[39;49;00m[37m [39;49;00m([36massociated[39;49;00m(wrk(i)%y2l))[37m [39;49;00m[34mdeallocate[39;49;00m(wrk(i)%y2l)[37m[39;49;00m$
   792^I[37m      [39;49;00m[34mif[39;49;00m[37m [39;49;00m([36massociated[39;49;00m(wrk(i)%b2l))[37m [39;49;00m[34mdeallocate[39;49;00m(wrk(i)%b2l)[37m[39;49;00m$
   793^I[37m      [39;49;00m[34mif[39;49;00m[37m [39;49;00m([36massociated[39;49;00m(wrk(i)%tty))[37m [39;49;00m[34mdeallocate[39;49;00m(wrk(i)%tty)[37m[39;49;00m$
   794^I[37m    [39;49;00m[34mend [39;49;00m[34mdo[39;49;00m$
   795^I[34m  [39;49;00m[34mend [39;49;00m[34msubroutine [39;49;00mmlprec_wrk_free[37m[39;49;00m$
   796^I[37m[39;49;00m$
   797^I[34mend [39;49;00m[34msubroutine [39;49;00mpsb_zmlprc_aply$

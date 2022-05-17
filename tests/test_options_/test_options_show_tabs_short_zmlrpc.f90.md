[37m!!$[39;49;00m
[37m!!$[39;49;00m
[37m!!$                    MD2P4[39;49;00m
[37m!!$    Multilevel Domain Decomposition Parallel Preconditioner Package for PSBLAS[39;49;00m
[37m!!$                      for[39;49;00m
[37m!!$              Parallel Sparse BLAS  v2.0[39;49;00m
[37m!!$    (C) Copyright 2006 Salvatore Filippone    University of Rome Tor Vergata[39;49;00m
[37m!!$                       Alfredo Buttari        University of Rome Tor Vergata[39;49;00m
[37m!!$                       Daniela Di Serafino    II University of Naples[39;49;00m
[37m!!$                       Pasqua D'Ambra         ICAR-CNR[39;49;00m
[37m!!$[39;49;00m
[37m!!$  Redistribution and use in source and binary forms, with or without[39;49;00m
[37m!!$  modification, are permitted provided that the following conditions[39;49;00m
[37m!!$  are met:[39;49;00m
[37m!!$    1. Redistributions of source code must retain the above copyright[39;49;00m
[37m!!$       notice, this list of conditions and the following disclaimer.[39;49;00m
[37m!!$    2. Redistributions in binary form must reproduce the above copyright[39;49;00m
[37m!!$       notice, this list of conditions, and the following disclaimer in the[39;49;00m
[37m!!$       documentation and/or other materials provided with the distribution.[39;49;00m
[37m!!$    3. The name of the MD2P4 group or the names of its contributors may[39;49;00m
[37m!!$       not be used to endorse or promote products derived from this[39;49;00m
[37m!!$       software without specific written permission.[39;49;00m
[37m!!$[39;49;00m
[37m!!$  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS[39;49;00m
[37m!!$  ``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED[39;49;00m
[37m!!$  TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR[39;49;00m
[37m!!$  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE MD2P4 GROUP OR ITS CONTRIBUTORS[39;49;00m
[37m!!$  BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR[39;49;00m
[37m!!$  CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF[39;49;00m
[37m!!$  SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS[39;49;00m
[37m!!$  INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN[39;49;00m
[37m!!$  CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)[39;49;00m
[37m!!$  ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE[39;49;00m
[37m!!$  POSSIBILITY OF SUCH DAMAGE.[39;49;00m
[37m!!$[39;49;00m
[37m!!$[39;49;00m
[34msubroutine [39;49;00mpsb_zmlprc_aply(alpha,baseprecv,x,beta,y,desc_data,trans,work,info)[37m[39;49;00m
[37m  [39;49;00m[37m![39;49;00m
[37m  [39;49;00m[37m!  Compute   Y <-  beta*Y + alpha*K^-1 X[39;49;00m
[37m  [39;49;00m[37m!  where K is a multilevel  preconditioner stored in baseprecv[39;49;00m
[37m  [39;49;00m[37m![39;49;00m
[37m  [39;49;00m[37m!  cfr.: Smith, Biorstad & Gropp[39;49;00m
[37m  [39;49;00m[37m!        Domain Decomposition[39;49;00m
[37m  [39;49;00m[37m!        Cambridge Univ. Press[39;49;00m
[37m  [39;49;00m[37m![39;49;00m
[37m  [39;49;00m[37m!  To each level I there corresponds a matrix A(I) and a preconditioner K(I)[39;49;00m
[37m  [39;49;00m[37m![39;49;00m
[37m  [39;49;00m[37m!  A notational difference: in the DD reference above the preconditioner for[39;49;00m
[37m  [39;49;00m[37m!  a given level K(I) is written out as a sum over the subdomains[39;49;00m
[37m  [39;49;00m[37m![39;49;00m
[37m  [39;49;00m[37m!  SUM_k(R_k^T A_k R_k)[39;49;00m
[37m  [39;49;00m[37m![39;49;00m
[37m  [39;49;00m[37m!  whereas in this code the sum is implicit in the parallelization,[39;49;00m
[37m  [39;49;00m[37m!  i.e. each process takes care of one subdomain, and for each level we have[39;49;00m
[37m  [39;49;00m[37m!  as many subdomains as there are processes (except for the coarsest level where[39;49;00m
[37m  [39;49;00m[37m!  we might have a replicated index space). Thus the sum apparently disappears[39;49;00m
[37m  [39;49;00m[37m!  from our code, but only apparently, because it is implicit in the call[39;49;00m
[37m  [39;49;00m[37m!  to psb_baseprc_aply.[39;49;00m
[37m  [39;49;00m[37m![39;49;00m
[37m  [39;49;00m[37m!  A bit of description of the baseprecv(:) data structure:[39;49;00m
[37m  [39;49;00m[37m!   1. Number of levels = NLEV = size(baseprecv(:))[39;49;00m
[37m  [39;49;00m[37m!   2. baseprecv(ilev)%av(:)    sparse matrices needed for the current level.[39;49;00m
[37m  [39;49;00m[37m!      Includes:[39;49;00m
[37m  [39;49;00m[37m!   2.1.:  baseprecv(ilev)%av(l_pr_)    L factor of ILU preconditioners[39;49;00m
[37m  [39;49;00m[37m!   2.2.:  baseprecv(ilev)%av(u_pr_)    U factor of ILU preconditioners[39;49;00m
[37m  [39;49;00m[37m!   2.3.:  baseprecv(ilev)%av(ap_nd_)   Off-diagonal part of A for Jacobi sweeps[39;49;00m
[37m  [39;49;00m[37m!   2.4.:  baseprecv(ilev)%av(ac_)      Aggregated matrix of level ILEV[39;49;00m
[37m  [39;49;00m[37m!   2.5.:  baseprecv(ilev)%av(sm_pr_t_) Smoother prolongator transpose; maps vectors[39;49;00m
[37m  [39;49;00m[37m!                                          (ilev-1) --->  (ilev)[39;49;00m
[37m  [39;49;00m[37m!   2.6.:  baseprecv(ilev)%av(sm_pr_)   Smoother prolongator; maps vectors[39;49;00m
[37m  [39;49;00m[37m!                                          (ilev)   --->  (ilev-1)[39;49;00m
[37m  [39;49;00m[37m!   Shouldn't we keep just one of them and handle transpose in the sparse BLAS? maybe[39;49;00m
[37m  [39;49;00m[37m![39;49;00m
[37m  [39;49;00m[37m!   3.    baseprecv(ilev)%desc_data     comm descriptor for level ILEV[39;49;00m
[37m  [39;49;00m[37m!   4.    baseprecv(ilev)%base_a        Pointer (really a pointer!) to the base matrix[39;49;00m
[37m  [39;49;00m[37m!                                       of the current level, i.e.: if ILEV=1 then  A[39;49;00m
[37m  [39;49;00m[37m!                                       else the aggregated matrix av(ac_); so we have[39;49;00m
[37m  [39;49;00m[37m!                                       a unified treatment of residuals. Need this to[39;49;00m
[37m  [39;49;00m[37m!                                       avoid passing explicitly matrix A to the[39;49;00m
[37m  [39;49;00m[37m!                                       outer prec. routine[39;49;00m
[37m  [39;49;00m[37m!   5.    baseprecv(ilev)%mlia          The aggregation map from (ilev-1)-->(ilev)[39;49;00m
[37m  [39;49;00m[37m!                                       if no smoother, it is used instead of sm_pr_[39;49;00m
[37m  [39;49;00m[37m!   6.    baseprecv(ilev)%nlaggr        Number of aggregates on the various procs.[39;49;00m
[37m  [39;49;00m[37m![39;49;00m
[37m[39;49;00m
[37m  [39;49;00m[34muse [39;49;00mpsb_serial_mod[37m[39;49;00m
[37m  [39;49;00m[34muse [39;49;00mpsb_descriptor_type[37m[39;49;00m
[37m  [39;49;00m[34muse [39;49;00mpsb_prec_type[37m[39;49;00m
[37m  [39;49;00m[34muse [39;49;00mpsb_psblas_mod[37m[39;49;00m
[37m  [39;49;00m[34muse [39;49;00mpsb_penv_mod[37m[39;49;00m
[37m  [39;49;00m[34muse [39;49;00mpsb_const_mod[37m[39;49;00m
[37m  [39;49;00m[34muse [39;49;00mpsb_error_mod[37m[39;49;00m
[37m  [39;49;00m[34muse [39;49;00mpsb_penv_mod[37m[39;49;00m
[37m  [39;49;00m[34mimplicit [39;49;00m[34mnone[39;49;00m
[34m[39;49;00m
[34m  [39;49;00m[34mtype[39;49;00m(psb_desc_type),[34mintent[39;49;00m(in)[37m      [39;49;00m[34m::[39;49;00m[37m [39;49;00mdesc_data[37m[39;49;00m
[37m  [39;49;00m[34mtype[39;49;00m(psb_zbaseprc_type),[37m [39;49;00m[34mintent[39;49;00m(in)[37m [39;49;00m[34m::[39;49;00m[37m [39;49;00mbaseprecv(:)[37m[39;49;00m
[37m  [39;49;00m[36mcomplex[39;49;00m([36mkind[39;49;00m([34m1.d0[39;49;00m)),[34mintent[39;49;00m(in)[37m      [39;49;00m[34m::[39;49;00m[37m [39;49;00malpha,beta[37m[39;49;00m
[37m  [39;49;00m[36mcomplex[39;49;00m([36mkind[39;49;00m([34m1.d0[39;49;00m)),[34mintent[39;49;00m(inout)[37m   [39;49;00m[34m::[39;49;00m[37m [39;49;00mx(:),[37m [39;49;00my(:)[37m[39;49;00m
[37m  [39;49;00m[36mcharacter[39;49;00m[37m                           [39;49;00m[34m::[39;49;00m[37m [39;49;00mtrans[37m[39;49;00m
[37m  [39;49;00m[36mcomplex[39;49;00m([36mkind[39;49;00m([34m1.d0[39;49;00m)),[34mtarget[39;49;00m[37m          [39;49;00m[34m::[39;49;00m[37m [39;49;00mwork(:)[37m[39;49;00m
[37m  [39;49;00m[36minteger[39;49;00m,[37m [39;49;00m[34mintent[39;49;00m(out)[37m                [39;49;00m[34m::[39;49;00m[37m [39;49;00minfo[37m[39;49;00m
[37m[39;49;00m
[37m[39;49;00m
[37m  [39;49;00m[37m! Local variables[39;49;00m
[37m  [39;49;00m[36minteger[39;49;00m[37m [39;49;00m[34m::[39;49;00m[37m [39;49;00mn_row,n_col[37m[39;49;00m
[37m  [39;49;00m[36mcomplex[39;49;00m([36mkind[39;49;00m([34m1.d0[39;49;00m)),[37m [39;49;00m[34mallocatable[39;49;00m[37m [39;49;00m[34m::[39;49;00m[37m [39;49;00mtx(:),ty(:),t2l(:),w2l(:),&[37m[39;49;00m
[37m       [39;49;00m&[37m   [39;49;00mx2l(:),b2l(:),tz(:),tty(:)[37m[39;49;00m
[37m  [39;49;00m[36mcharacter[39;49;00m[37m     [39;49;00m[34m::[39;49;00mdiagl,[37m [39;49;00mdiagu[37m[39;49;00m
[37m  [39;49;00m[36minteger[39;49;00m[37m [39;49;00m[34m::[39;49;00m[37m [39;49;00mictxt,np,me,i,[37m [39;49;00misz,[37m [39;49;00mnrg,nr2l,err_act,[37m [39;49;00miptype,[37m [39;49;00mint_err([34m5[39;49;00m)[37m[39;49;00m
[37m  [39;49;00m[36mreal[39;49;00m([36mkind[39;49;00m([34m1.d0[39;49;00m))[37m [39;49;00m[34m::[39;49;00m[37m [39;49;00momega[37m[39;49;00m
[37m  [39;49;00m[36mreal[39;49;00m([36mkind[39;49;00m([34m1.d0[39;49;00m))[37m [39;49;00m[34m::[39;49;00m[37m [39;49;00mt1,[37m [39;49;00mt2,[37m [39;49;00mt3,[37m [39;49;00mt4,[37m [39;49;00mt5,[37m [39;49;00mt6,[37m [39;49;00mt7,[37m [39;49;00mmpi_wtime[37m[39;49;00m
[37m  [39;49;00m[36mlogical[39;49;00m,[37m [39;49;00m[34mparameter[39;49;00m[37m          [39;49;00m[34m::[39;49;00m[37m [39;49;00mdebug=.false.,[37m [39;49;00mdebugprt=.false.[37m[39;49;00m
[37m  [39;49;00m[36minteger[39;49;00m[37m      [39;49;00m[34m::[39;49;00m[37m [39;49;00mismth,[37m [39;49;00mnlev,[37m [39;49;00milev[37m[39;49;00m
[37m  [39;49;00m[34mexternal [39;49;00mmpi_wtime[37m[39;49;00m
[37m  [39;49;00m[36mcharacter[39;49;00m([36mlen[39;49;00m=[34m20[39;49;00m)[37m   [39;49;00m[34m::[39;49;00m[37m [39;49;00mname,[37m [39;49;00mch_err[37m[39;49;00m
[37m[39;49;00m
[37m  [39;49;00m[34mtype [39;49;00mpsb_mlprec_wrk_type[37m[39;49;00m
[37m    [39;49;00m[36mcomplex[39;49;00m([36mkind[39;49;00m([34m1.d0[39;49;00m)),[37m [39;49;00m[34mpointer[39;49;00m[37m [39;49;00m[34m::[39;49;00m[37m [39;49;00mtx(:)=>[36mnull[39;49;00m(),ty(:)=>[36mnull[39;49;00m(),&[37m[39;49;00m
[37m         [39;49;00m&[37m [39;49;00mx2l(:)=>[36mnull[39;49;00m(),y2l(:)=>[36mnull[39;49;00m(),&[37m[39;49;00m
[37m         [39;49;00m&[37m [39;49;00mb2l(:)=>[36mnull[39;49;00m(),tty(:)=>[36mnull[39;49;00m()[37m[39;49;00m
[37m  [39;49;00m[34mend [39;49;00m[34mtype [39;49;00mpsb_mlprec_wrk_type[37m[39;49;00m
[37m  [39;49;00m[34mtype[39;49;00m(psb_mlprec_wrk_type),[37m [39;49;00m[34mpointer[39;49;00m[37m [39;49;00m[34m::[39;49;00m[37m [39;49;00mmlprec_wrk(:)[37m[39;49;00m
[37m[39;49;00m
[37m  [39;49;00m[34minterface [39;49;00mpsb_baseprc_aply[37m[39;49;00m
[37m    [39;49;00m[34msubroutine [39;49;00mpsb_zbaseprc_aply(alpha,prec,x,beta,y,desc_data,trans,work,info)[37m[39;49;00m
[37m      [39;49;00m[34muse [39;49;00mpsb_descriptor_type[37m[39;49;00m
[37m      [39;49;00m[34muse [39;49;00mpsb_prec_type[37m[39;49;00m
[37m      [39;49;00m[34mtype[39;49;00m(psb_desc_type),[34mintent[39;49;00m(in)[37m      [39;49;00m[34m::[39;49;00m[37m [39;49;00mdesc_data[37m[39;49;00m
[37m      [39;49;00m[34mtype[39;49;00m(psb_zbaseprc_type),[37m [39;49;00m[34mintent[39;49;00m(in)[37m [39;49;00m[34m::[39;49;00m[37m [39;49;00mprec[37m[39;49;00m
[37m      [39;49;00m[36mcomplex[39;49;00m([36mkind[39;49;00m([34m1.d0[39;49;00m)),[34mintent[39;49;00m(inout)[37m   [39;49;00m[34m::[39;49;00m[37m [39;49;00mx(:),[37m [39;49;00my(:)[37m[39;49;00m
[37m      [39;49;00m[36mcomplex[39;49;00m([36mkind[39;49;00m([34m1.d0[39;49;00m)),[34mintent[39;49;00m(in)[37m      [39;49;00m[34m::[39;49;00m[37m [39;49;00malpha,beta[37m[39;49;00m
[37m      [39;49;00m[36mcharacter[39;49;00m([36mlen[39;49;00m=[34m1[39;49;00m)[37m                    [39;49;00m[34m::[39;49;00m[37m [39;49;00mtrans[37m[39;49;00m
[37m      [39;49;00m[36mcomplex[39;49;00m([36mkind[39;49;00m([34m1.d0[39;49;00m)),[34mtarget[39;49;00m[37m          [39;49;00m[34m::[39;49;00m[37m [39;49;00mwork(:)[37m[39;49;00m
[37m      [39;49;00m[36minteger[39;49;00m,[37m [39;49;00m[34mintent[39;49;00m(out)[37m                [39;49;00m[34m::[39;49;00m[37m [39;49;00minfo[37m[39;49;00m
[37m    [39;49;00m[34mend [39;49;00m[34msubroutine [39;49;00mpsb_zbaseprc_aply[37m[39;49;00m
[37m  [39;49;00m[34mend [39;49;00m[34minterface[39;49;00m
[34m[39;49;00m
[34m  [39;49;00mname=[33m'psb_mlprc_aply'[39;49;00m[37m[39;49;00m
[37m  [39;49;00minfo[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m[37m[39;49;00m
[37m  [39;49;00m[34mcall [39;49;00mpsb_erractionsave(err_act)[37m[39;49;00m
[37m[39;49;00m
[37m[39;49;00m
[37m  [39;49;00mictxt=desc_data%matrix_data(psb_ctxt_)[37m[39;49;00m
[37m  [39;49;00m[34mcall [39;49;00mpsb_info(ictxt,[37m [39;49;00mme,[37m [39;49;00mnp)[37m[39;49;00m
[37m[39;49;00m
[37m  [39;49;00mnlev[37m [39;49;00m=[37m [39;49;00msize(baseprecv)[37m[39;49;00m
[37m  [39;49;00m[34mallocate[39;49;00m(mlprec_wrk(nlev),[36mstat[39;49;00m=info)[37m[39;49;00m
[37m  [39;49;00m[34mif[39;49;00m[37m [39;49;00m(info[37m [39;49;00m/=[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mthen[39;49;00m
[34m    [39;49;00m[34mcall [39;49;00mpsb_errpush([34m4010[39;49;00m,name,a_err=[33m'Allocate'[39;49;00m)[37m[39;49;00m
[37m    [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
[37m  [39;49;00m[34mend [39;49;00m[34mif[39;49;00m
[34m[39;49;00m
[34m[39;49;00m
[34m  [39;49;00m[34mselect [39;49;00m[34mcase[39;49;00m(baseprecv([34m2[39;49;00m)%iprcparm(ml_type_))[37m[39;49;00m
[37m[39;49;00m
[37m  [39;49;00m[34mcase[39;49;00m(no_ml_)[37m[39;49;00m
[37m    [39;49;00m[37m! Should not really get here.[39;49;00m
[37m    [39;49;00m[34mcall [39;49;00mpsb_errpush([34m4010[39;49;00m,name,a_err=[33m'no_ml_ in mlprc_aply?'[39;49;00m)[37m[39;49;00m
[37m    [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m[39;49;00m
[37m  [39;49;00m[34mcase[39;49;00m(add_ml_prec_)[37m[39;49;00m
[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[37m![39;49;00m
[37m    [39;49;00m[37m!    Additive is very simple.[39;49;00m
[37m    [39;49;00m[37m!    1.  X(1) = Xext[39;49;00m
[37m    [39;49;00m[37m!    2.  DO ILEV=2,NLEV[39;49;00m
[37m    [39;49;00m[37m!           X(ILEV) = AV(PR_SM_T_)*X(ILEV-1)[39;49;00m
[37m    [39;49;00m[37m!    3.  Y(ILEV) = (K(ILEV)**(-1))*X(ILEV)[39;49;00m
[37m    [39;49;00m[37m!    4.  DO  ILEV=NLEV-1,1,-1[39;49;00m
[37m    [39;49;00m[37m!           Y(ILEV) = AV(PR_SM_)*Y(ILEV+1)[39;49;00m
[37m    [39;49;00m[37m!    5.  Yext    = beta*Yext + Y(1)[39;49;00m
[37m    [39;49;00m[37m![39;49;00m
[37m    [39;49;00m[37m!    Note: level numbering reversed wrt ref. DD, i.e.[39;49;00m
[37m    [39;49;00m[37m!         1..NLEV <=>  (j) <-> 0[39;49;00m
[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[34mcall [39;49;00mpsb_baseprc_aply(alpha,baseprecv([34m1[39;49;00m),x,beta,y,&[37m[39;49;00m
[37m         [39;49;00m&[37m [39;49;00mbaseprecv([34m1[39;49;00m)%base_desc,trans,work,info)[37m[39;49;00m
[37m    [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[34mallocate[39;49;00m(mlprec_wrk([34m1[39;49;00m)%x2l(size(x)),mlprec_wrk([34m1[39;49;00m)%y2l(size(y)))[37m[39;49;00m
[37m    [39;49;00mmlprec_wrk([34m1[39;49;00m)%x2l(:)[37m [39;49;00m=[37m [39;49;00mx(:)[37m[39;49;00m
[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[34mdo [39;49;00milev[37m [39;49;00m=[37m [39;49;00m[34m2[39;49;00m,[37m [39;49;00mnlev[37m[39;49;00m
[37m      [39;49;00mn_row[37m [39;49;00m=[37m [39;49;00mbaseprecv(ilev-[34m1[39;49;00m)%base_desc%matrix_data(psb_n_row_)[37m[39;49;00m
[37m      [39;49;00mn_col[37m [39;49;00m=[37m [39;49;00mbaseprecv(ilev-[34m1[39;49;00m)%desc_data%matrix_data(psb_n_col_)[37m[39;49;00m
[37m      [39;49;00mnr2l[37m  [39;49;00m=[37m [39;49;00mbaseprecv(ilev)%desc_data%matrix_data(psb_n_col_)[37m[39;49;00m
[37m      [39;49;00mnrg[37m   [39;49;00m=[37m [39;49;00mbaseprecv(ilev)%desc_data%matrix_data(psb_n_row_)[37m[39;49;00m
[37m      [39;49;00m[34mallocate[39;49;00m(mlprec_wrk(ilev)%x2l(nr2l),mlprec_wrk(ilev)%y2l(nr2l),&[37m[39;49;00m
[37m           [39;49;00m&[37m [39;49;00mmlprec_wrk(ilev)%tx([36mmax[39;49;00m(n_row,n_col)),&[37m[39;49;00m
[37m           [39;49;00m&[37m [39;49;00mmlprec_wrk(ilev)%ty([36mmax[39;49;00m(n_row,n_col)),[37m [39;49;00m[36mstat[39;49;00m=info)[37m[39;49;00m
[37m      [39;49;00m[34mif[39;49;00m[37m [39;49;00m(info[37m [39;49;00m/=[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mthen[39;49;00m
[34m        [39;49;00m[34mcall [39;49;00mpsb_errpush([34m4010[39;49;00m,name,a_err=[33m'Allocate'[39;49;00m)[37m[39;49;00m
[37m        [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
[37m      [39;49;00m[34mend [39;49;00m[34mif[39;49;00m
[34m[39;49;00m
[34m      [39;49;00mmlprec_wrk(ilev)%x2l(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
[37m      [39;49;00mmlprec_wrk(ilev)%y2l(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
[37m      [39;49;00mmlprec_wrk(ilev)%tx([34m1[39;49;00m:n_row)[37m [39;49;00m=[37m [39;49;00mmlprec_wrk(ilev-[34m1[39;49;00m)%x2l([34m1[39;49;00m:n_row)[37m[39;49;00m
[37m      [39;49;00mmlprec_wrk(ilev)%tx(n_row+[34m1[39;49;00m:[36mmax[39;49;00m(n_row,n_col))[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
[37m      [39;49;00mmlprec_wrk(ilev)%ty(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
[37m[39;49;00m
[37m      [39;49;00mismth=baseprecv(ilev)%iprcparm(smth_kind_)[37m[39;49;00m
[37m[39;49;00m
[37m      [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ismth[37m  [39;49;00m/=[37m [39;49;00mno_smth_)[37m [39;49;00m[34mthen[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m![39;49;00m
[37m        [39;49;00m[37m! Smoothed aggregation[39;49;00m
[37m        [39;49;00m[37m![39;49;00m
[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(baseprecv(ilev)%iprcparm(glb_smth_)[37m [39;49;00m>[34m0[39;49;00m)[37m [39;49;00m[34mthen[39;49;00m
[34m          [39;49;00m[34mcall [39;49;00mpsb_halo(mlprec_wrk(ilev-[34m1[39;49;00m)%x2l,baseprecv(ilev-[34m1[39;49;00m)%base_desc,&[37m[39;49;00m
[37m               [39;49;00m&[37m  [39;49;00minfo,work=work)[37m[39;49;00m
[37m          [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34melse[39;49;00m
[34m          [39;49;00mmlprec_wrk(ilev-[34m1[39;49;00m)%x2l(n_row+[34m1[39;49;00m:[36mmax[39;49;00m(n_row,n_col))[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
[37m        [39;49;00m[34mend [39;49;00m[34mif[39;49;00m
[34m[39;49;00m
[34m        [39;49;00m[34mcall [39;49;00mpsb_csmm(zone,baseprecv(ilev)%av(sm_pr_t_),mlprec_wrk(ilev-[34m1[39;49;00m)%x2l,&[37m[39;49;00m
[37m             [39;49;00m&[37m [39;49;00mzzero,mlprec_wrk(ilev)%x2l,info)[37m[39;49;00m
[37m        [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m      [39;49;00m[34melse[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m![39;49;00m
[37m        [39;49;00m[37m! Raw  aggregation, may take shortcut[39;49;00m
[37m        [39;49;00m[37m![39;49;00m
[37m        [39;49;00m[34mdo [39;49;00mi=[34m1[39;49;00m,n_row[37m[39;49;00m
[37m          [39;49;00mmlprec_wrk(ilev)%x2l(baseprecv(ilev)%mlia(i))[37m [39;49;00m=[37m [39;49;00m&[37m[39;49;00m
[37m               [39;49;00m&[37m  [39;49;00mmlprec_wrk(ilev)%x2l(baseprecv(ilev)%mlia(i))[37m [39;49;00m+[37m [39;49;00m&[37m[39;49;00m
[37m               [39;49;00m&[37m  [39;49;00mmlprec_wrk(ilev-[34m1[39;49;00m)%x2l(i)[37m[39;49;00m
[37m        [39;49;00m[34mend [39;49;00m[34mdo[39;49;00m
[34m[39;49;00m
[34m      [39;49;00m[34mend [39;49;00m[34mif[39;49;00m
[34m[39;49;00m
[34m      [39;49;00m[34mif[39;49;00m[37m [39;49;00m(baseprecv(ilev)%iprcparm(coarse_mat_)==mat_repl_)[37m [39;49;00m[34mThen[39;49;00m
[34m        [39;49;00m[34mcall [39;49;00mpsb_sum(ictxt,mlprec_wrk(ilev)%x2l([34m1[39;49;00m:nrg))[37m[39;49;00m
[37m      [39;49;00m[34melse [39;49;00m[34mif[39;49;00m[37m [39;49;00m(baseprecv(ilev)%iprcparm(coarse_mat_)[37m [39;49;00m/=[37m [39;49;00mmat_distr_)[37m [39;49;00m[34mThen[39;49;00m
[34m        [39;49;00m[34mwrite[39;49;00m([34m0[39;49;00m,*)[37m [39;49;00m[33m'Unknown value for baseprecv(2)%iprcparm(coarse_mat_) '[39;49;00m,&[37m[39;49;00m
[37m             [39;49;00m&[37m [39;49;00mbaseprecv(ilev)%iprcparm(coarse_mat_)[37m[39;49;00m
[37m      [39;49;00m[34mendif[39;49;00m
[34m[39;49;00m
[34m      [39;49;00m[34mcall [39;49;00mpsb_baseprc_aply(zone,baseprecv(ilev),&[37m[39;49;00m
[37m           [39;49;00m&[37m [39;49;00mmlprec_wrk(ilev)%x2l,zzero,mlprec_wrk(ilev)%y2l,&[37m[39;49;00m
[37m           [39;49;00m&[37m [39;49;00mbaseprecv(ilev)%desc_data,[37m [39;49;00m[33m'N'[39;49;00m,work,info)[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[34menddo[39;49;00m
[34m[39;49;00m
[34m    [39;49;00m[34mdo [39;49;00milev[37m [39;49;00m=nlev,[34m2[39;49;00m,-[34m1[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m      [39;49;00mismth=baseprecv(ilev)%iprcparm(smth_kind_)[37m[39;49;00m
[37m      [39;49;00mn_row[37m [39;49;00m=[37m [39;49;00mbaseprecv(ilev-[34m1[39;49;00m)%base_desc%matrix_data(psb_n_row_)[37m[39;49;00m
[37m      [39;49;00mn_col[37m [39;49;00m=[37m [39;49;00mbaseprecv(ilev-[34m1[39;49;00m)%desc_data%matrix_data(psb_n_col_)[37m[39;49;00m
[37m      [39;49;00mnr2l[37m  [39;49;00m=[37m [39;49;00mbaseprecv(ilev)%desc_data%matrix_data(psb_n_col_)[37m[39;49;00m
[37m      [39;49;00mnrg[37m   [39;49;00m=[37m [39;49;00mbaseprecv(ilev)%desc_data%matrix_data(psb_n_row_)[37m[39;49;00m
[37m[39;49;00m
[37m      [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ismth[37m  [39;49;00m/=[37m [39;49;00mno_smth_)[37m [39;49;00m[34mthen[39;49;00m
[34m[39;49;00m
[34m        [39;49;00m[34mcall [39;49;00mpsb_csmm(zone,baseprecv(ilev)%av(sm_pr_),mlprec_wrk(ilev)%y2l,&[37m[39;49;00m
[37m             [39;49;00m&[37m [39;49;00mzone,mlprec_wrk(ilev-[34m1[39;49;00m)%y2l,info)[37m[39;49;00m
[37m        [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m      [39;49;00m[34melse[39;49;00m
[34m[39;49;00m
[34m        [39;49;00m[34mdo [39;49;00mi=[34m1[39;49;00m,[37m [39;49;00mn_row[37m[39;49;00m
[37m          [39;49;00mmlprec_wrk(ilev-[34m1[39;49;00m)%y2l(i)[37m [39;49;00m=[37m [39;49;00mmlprec_wrk(ilev-[34m1[39;49;00m)%y2l(i)[37m [39;49;00m+[37m [39;49;00m&[37m[39;49;00m
[37m               [39;49;00m&[37m   [39;49;00mmlprec_wrk(ilev)%y2l(baseprecv(ilev)%mlia(i))[37m[39;49;00m
[37m        [39;49;00m[34menddo[39;49;00m
[34m[39;49;00m
[34m      [39;49;00m[34mend [39;49;00m[34mif[39;49;00m
[34m    [39;49;00m[34mend [39;49;00m[34mdo[39;49;00m
[34m[39;49;00m
[34m    [39;49;00m[34mcall [39;49;00mpsb_geaxpby(alpha,mlprec_wrk([34m1[39;49;00m)%y2l,zone,y,baseprecv([34m1[39;49;00m)%base_desc,info)[37m[39;49;00m
[37m    [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m[39;49;00m
[37m  [39;49;00m[34mcase[39;49;00m(mult_ml_prec_)[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[37m![39;49;00m
[37m    [39;49;00m[37m!  Multiplicative multilevel[39;49;00m
[37m    [39;49;00m[37m!  Pre/post smoothing versions.[39;49;00m
[37m    [39;49;00m[37m![39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[34mselect [39;49;00m[34mcase[39;49;00m(baseprecv([34m2[39;49;00m)%iprcparm(smth_pos_))[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[34mcase[39;49;00m(post_smooth_)[37m[39;49;00m
[37m[39;49;00m
[37m[39;49;00m
[37m      [39;49;00m[37m![39;49;00m
[37m      [39;49;00m[37m!    Post smoothing.[39;49;00m
[37m      [39;49;00m[37m!    1.   X(1) = Xext[39;49;00m
[37m      [39;49;00m[37m!    2.   DO ILEV=2, NLEV :: X(ILEV) = AV(PR_SM_T_,ILEV)*X(ILEV-1)[39;49;00m
[37m      [39;49;00m[37m!    3.   Y(NLEV) = (K(NLEV)**(-1))*X(NLEV)[39;49;00m
[37m      [39;49;00m[37m!    4.   DO  ILEV=NLEV-1,1,-1[39;49;00m
[37m      [39;49;00m[37m!          Y(ILEV) = AV(PR_SM_,ILEV+1)*Y(ILEV+1)[39;49;00m
[37m      [39;49;00m[37m!          Y(ILEV) = Y(ILEV) + (K(ILEV)**(-1))*(X(ILEV)-A(ILEV)*Y(ILEV))[39;49;00m
[37m      [39;49;00m[37m![39;49;00m
[37m      [39;49;00m[37m!    5.  Yext    = beta*Yext + Y(1)[39;49;00m
[37m      [39;49;00m[37m![39;49;00m
[37m      [39;49;00m[37m!    Note: level numbering reversed wrt ref. DD, i.e.[39;49;00m
[37m      [39;49;00m[37m!         1..NLEV <=>  (j) <-> 0[39;49;00m
[37m      [39;49;00m[37m![39;49;00m
[37m      [39;49;00m[37m!    Also: post smoothing is not spelled out in detail in DD.[39;49;00m
[37m      [39;49;00m[37m![39;49;00m
[37m      [39;49;00m[37m![39;49;00m
[37m[39;49;00m
[37m[39;49;00m
[37m      [39;49;00mn_col[37m [39;49;00m=[37m [39;49;00mdesc_data%matrix_data(psb_n_col_)[37m[39;49;00m
[37m      [39;49;00mnr2l[37m  [39;49;00m=[37m [39;49;00mbaseprecv([34m1[39;49;00m)%desc_data%matrix_data(psb_n_col_)[37m[39;49;00m
[37m[39;49;00m
[37m      [39;49;00m[34mallocate[39;49;00m(mlprec_wrk([34m1[39;49;00m)%x2l(nr2l),mlprec_wrk([34m1[39;49;00m)%y2l(nr2l),[37m [39;49;00m&[37m[39;49;00m
[37m           [39;49;00m&[37m [39;49;00mmlprec_wrk([34m1[39;49;00m)%tx(nr2l),[37m [39;49;00m[36mstat[39;49;00m=info)[37m[39;49;00m
[37m      [39;49;00mmlprec_wrk([34m1[39;49;00m)%x2l(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
[37m      [39;49;00mmlprec_wrk([34m1[39;49;00m)%y2l(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
[37m      [39;49;00mmlprec_wrk([34m1[39;49;00m)%tx(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
[37m[39;49;00m
[37m      [39;49;00m[34mcall [39;49;00mpsb_geaxpby(zone,x,zzero,mlprec_wrk([34m1[39;49;00m)%tx,&[37m[39;49;00m
[37m           [39;49;00m&[37m [39;49;00mbaseprecv([34m1[39;49;00m)%base_desc,info)[37m[39;49;00m
[37m      [39;49;00m[34mcall [39;49;00mpsb_geaxpby(zone,x,zzero,mlprec_wrk([34m1[39;49;00m)%x2l,&[37m[39;49;00m
[37m           [39;49;00m&[37m [39;49;00mbaseprecv([34m1[39;49;00m)%base_desc,info)[37m[39;49;00m
[37m[39;49;00m
[37m      [39;49;00m[34mdo [39;49;00milev=[34m2[39;49;00m,[37m [39;49;00mnlev[37m[39;49;00m
[37m        [39;49;00mn_row[37m [39;49;00m=[37m [39;49;00mbaseprecv(ilev-[34m1[39;49;00m)%base_desc%matrix_data(psb_n_row_)[37m[39;49;00m
[37m        [39;49;00mn_col[37m [39;49;00m=[37m [39;49;00mbaseprecv(ilev-[34m1[39;49;00m)%desc_data%matrix_data(psb_n_col_)[37m[39;49;00m
[37m        [39;49;00mnr2l[37m  [39;49;00m=[37m [39;49;00mbaseprecv(ilev)%desc_data%matrix_data(psb_n_col_)[37m[39;49;00m
[37m        [39;49;00mnrg[37m   [39;49;00m=[37m [39;49;00mbaseprecv(ilev)%desc_data%matrix_data(psb_n_row_)[37m[39;49;00m
[37m        [39;49;00mismth[37m [39;49;00m=[37m [39;49;00mbaseprecv(ilev)%iprcparm(smth_kind_)[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[34mallocate[39;49;00m(mlprec_wrk(ilev)%tx(nr2l),mlprec_wrk(ilev)%y2l(nr2l),&[37m[39;49;00m
[37m             [39;49;00m&[37m   [39;49;00mmlprec_wrk(ilev)%x2l(nr2l),[37m [39;49;00m[36mstat[39;49;00m=info)[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(info[37m [39;49;00m/=[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mthen[39;49;00m
[34m          [39;49;00m[34mcall [39;49;00mpsb_errpush([34m4010[39;49;00m,name,a_err=[33m'Allocate'[39;49;00m)[37m[39;49;00m
[37m          [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mend [39;49;00m[34mif[39;49;00m
[34m[39;49;00m
[34m        [39;49;00mmlprec_wrk(ilev)%x2l(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
[37m        [39;49;00mmlprec_wrk(ilev)%y2l(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
[37m        [39;49;00mmlprec_wrk(ilev)%tx(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ismth[37m  [39;49;00m/=[37m [39;49;00mno_smth_)[37m [39;49;00m[34mthen[39;49;00m[37m[39;49;00m
[37m          [39;49;00m[37m![39;49;00m
[37m          [39;49;00m[37m! Smoothed aggregation[39;49;00m
[37m          [39;49;00m[37m![39;49;00m
[37m          [39;49;00m[34mif[39;49;00m[37m [39;49;00m(baseprecv(ilev)%iprcparm(glb_smth_)[37m [39;49;00m>[34m0[39;49;00m)[37m [39;49;00m[34mthen[39;49;00m
[34m            [39;49;00m[34mcall [39;49;00mpsb_halo(mlprec_wrk(ilev-[34m1[39;49;00m)%x2l,&[37m[39;49;00m
[37m                 [39;49;00m&[37m  [39;49;00mbaseprecv(ilev-[34m1[39;49;00m)%base_desc,info,work=work)[37m[39;49;00m
[37m            [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
[37m          [39;49;00m[34melse[39;49;00m
[34m            [39;49;00mmlprec_wrk(ilev-[34m1[39;49;00m)%x2l(n_row+[34m1[39;49;00m:[36mmax[39;49;00m(n_row,n_col))[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
[37m          [39;49;00m[34mend [39;49;00m[34mif[39;49;00m
[34m[39;49;00m
[34m          [39;49;00m[34mcall [39;49;00mpsb_csmm(zone,baseprecv(ilev)%av(sm_pr_t_),mlprec_wrk(ilev-[34m1[39;49;00m)%x2l,[37m [39;49;00m&[37m[39;49;00m
[37m               [39;49;00m&[37m [39;49;00mzzero,mlprec_wrk(ilev)%x2l,info)[37m[39;49;00m
[37m          [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[34melse[39;49;00m[37m[39;49;00m
[37m          [39;49;00m[37m![39;49;00m
[37m          [39;49;00m[37m! Raw  aggregation, may take shortcut[39;49;00m
[37m          [39;49;00m[37m![39;49;00m
[37m          [39;49;00m[34mdo [39;49;00mi=[34m1[39;49;00m,n_row[37m[39;49;00m
[37m            [39;49;00mmlprec_wrk(ilev)%x2l(baseprecv(ilev)%mlia(i))[37m [39;49;00m=[37m [39;49;00m&[37m[39;49;00m
[37m                 [39;49;00m&[37m [39;49;00mmlprec_wrk(ilev)%x2l(baseprecv(ilev)%mlia(i))[37m [39;49;00m+[37m [39;49;00m&[37m[39;49;00m
[37m                 [39;49;00m&[37m [39;49;00mmlprec_wrk(ilev-[34m1[39;49;00m)%x2l(i)[37m[39;49;00m
[37m          [39;49;00m[34mend [39;49;00m[34mdo[39;49;00m
[34m        [39;49;00m[34mend [39;49;00m[34mif[39;49;00m
[34m[39;49;00m
[34m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(baseprecv(ilev)%iprcparm(coarse_mat_)==mat_repl_)[37m [39;49;00m[34mThen[39;49;00m
[34m          [39;49;00m[34mcall [39;49;00mpsb_sum(ictxt,mlprec_wrk(ilev)%x2l([34m1[39;49;00m:nrg))[37m[39;49;00m
[37m        [39;49;00m[34melse [39;49;00m[34mif[39;49;00m[37m [39;49;00m(baseprecv(ilev)%iprcparm(coarse_mat_)[37m [39;49;00m/=[37m [39;49;00mmat_distr_)[37m [39;49;00m[34mThen[39;49;00m
[34m          [39;49;00m[34mwrite[39;49;00m([34m0[39;49;00m,*)[37m [39;49;00m[33m'Unknown value for baseprecv(2)%iprcparm(coarse_mat_) '[39;49;00m,&[37m[39;49;00m
[37m               [39;49;00m&[37m [39;49;00mbaseprecv(ilev)%iprcparm(coarse_mat_)[37m[39;49;00m
[37m        [39;49;00m[34mendif[39;49;00m
[34m        [39;49;00m[34mcall [39;49;00mpsb_geaxpby(zone,mlprec_wrk(ilev)%x2l,zzero,mlprec_wrk(ilev)%tx,&[37m[39;49;00m
[37m             [39;49;00m&[37m [39;49;00mbaseprecv(ilev)%base_desc,info)[37m[39;49;00m
[37m        [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m      [39;49;00m[34menddo[39;49;00m
[34m[39;49;00m
[34m[39;49;00m
[34m      [39;49;00m[34mcall [39;49;00mpsb_baseprc_aply(zone,baseprecv(nlev),mlprec_wrk(nlev)%x2l,[37m [39;49;00m&[37m[39;49;00m
[37m           [39;49;00m&[37m [39;49;00mzzero,[37m [39;49;00mmlprec_wrk(nlev)%y2l,baseprecv(nlev)%desc_data,[33m'N'[39;49;00m,work,info)[37m[39;49;00m
[37m[39;49;00m
[37m      [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m[39;49;00m
[37m      [39;49;00m[34mdo [39;49;00milev=nlev-[34m1[39;49;00m,[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00m-[34m1[39;49;00m[37m[39;49;00m
[37m        [39;49;00mismth[37m [39;49;00m=[37m [39;49;00mbaseprecv(ilev+[34m1[39;49;00m)%iprcparm(smth_kind_)[37m[39;49;00m
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ismth[37m  [39;49;00m/=[37m [39;49;00mno_smth_)[37m [39;49;00m[34mthen[39;49;00m
[34m          [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ismth[37m [39;49;00m==[37m [39;49;00msmth_omg_)[37m [39;49;00m&[37m[39;49;00m
[37m               [39;49;00m&[37m [39;49;00m[34mcall [39;49;00mpsb_halo(mlprec_wrk(ilev+[34m1[39;49;00m)%y2l,baseprecv(ilev+[34m1[39;49;00m)%desc_data,&[37m[39;49;00m
[37m               [39;49;00m&[37m  [39;49;00minfo,work=work)[37m[39;49;00m
[37m          [39;49;00m[34mcall [39;49;00mpsb_csmm(zone,baseprecv(ilev+[34m1[39;49;00m)%av(sm_pr_),mlprec_wrk(ilev+[34m1[39;49;00m)%y2l,&[37m[39;49;00m
[37m               [39;49;00m&[37m  [39;49;00mzzero,mlprec_wrk(ilev)%y2l,info)[37m[39;49;00m
[37m          [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[34melse[39;49;00m
[34m          [39;49;00mn_row[37m [39;49;00m=[37m [39;49;00mbaseprecv(ilev)%base_desc%matrix_data(psb_n_row_)[37m[39;49;00m
[37m          [39;49;00mmlprec_wrk(ilev)%y2l(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
[37m          [39;49;00m[34mdo [39;49;00mi=[34m1[39;49;00m,[37m [39;49;00mn_row[37m[39;49;00m
[37m            [39;49;00mmlprec_wrk(ilev)%y2l(i)[37m [39;49;00m=[37m [39;49;00mmlprec_wrk(ilev)%y2l(i)[37m [39;49;00m+[37m [39;49;00m&[37m[39;49;00m
[37m                 [39;49;00m&[37m [39;49;00mmlprec_wrk(ilev+[34m1[39;49;00m)%y2l(baseprecv(ilev+[34m1[39;49;00m)%mlia(i))[37m[39;49;00m
[37m          [39;49;00m[34menddo[39;49;00m
[34m[39;49;00m
[34m        [39;49;00m[34mend [39;49;00m[34mif[39;49;00m
[34m[39;49;00m
[34m        [39;49;00m[34mcall [39;49;00mpsb_spmm(-zone,baseprecv(ilev)%base_a,mlprec_wrk(ilev)%y2l,&[37m[39;49;00m
[37m             [39;49;00m&[37m   [39;49;00mzone,mlprec_wrk(ilev)%tx,baseprecv(ilev)%base_desc,info,work=work)[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[34mcall [39;49;00mpsb_baseprc_aply(zone,baseprecv(ilev),mlprec_wrk(ilev)%tx,&[37m[39;49;00m
[37m             [39;49;00m&[37m [39;49;00mzone,mlprec_wrk(ilev)%y2l,baseprecv(ilev)%base_desc,[37m [39;49;00mtrans,[37m [39;49;00mwork,info)[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m      [39;49;00m[34menddo[39;49;00m
[34m[39;49;00m
[34m      [39;49;00m[34mcall [39;49;00mpsb_geaxpby(alpha,mlprec_wrk([34m1[39;49;00m)%y2l,beta,y,baseprecv([34m1[39;49;00m)%base_desc,info)[37m[39;49;00m
[37m[39;49;00m
[37m      [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[34mcase[39;49;00m(pre_smooth_)[37m[39;49;00m
[37m[39;49;00m
[37m[39;49;00m
[37m      [39;49;00m[37m![39;49;00m
[37m      [39;49;00m[37m!    Pre smoothing.[39;49;00m
[37m      [39;49;00m[37m!    1.   X(1)  = Xext[39;49;00m
[37m      [39;49;00m[37m!    2.   Y(1)  = (K(1)**(-1))*X(1)[39;49;00m
[37m      [39;49;00m[37m!    3.   TX(1) = X(1) - A(1)*Y(1)[39;49;00m
[37m      [39;49;00m[37m!    4.   DO ILEV=2, NLEV[39;49;00m
[37m      [39;49;00m[37m!          X(ILEV) = AV(PR_SM_T_,ILEV)*TX(ILEV-1)[39;49;00m
[37m      [39;49;00m[37m!          Y(ILEV) = (K(ILEV)**(-1))*X(ILEV)[39;49;00m
[37m      [39;49;00m[37m!          TX(ILEV) = (X(ILEV)-A(ILEV)*Y(ILEV))[39;49;00m
[37m      [39;49;00m[37m!    5.   DO  ILEV=NLEV-1,1,-1[39;49;00m
[37m      [39;49;00m[37m!          Y(ILEV) = Y(ILEV) + AV(PR_SM_,ILEV+1)*Y(ILEV+1)[39;49;00m
[37m      [39;49;00m[37m!    6.  Yext    = beta*Yext + Y(1)[39;49;00m
[37m      [39;49;00m[37m![39;49;00m
[37m      [39;49;00m[37m!    Note: level numbering reversed wrt ref. DD, i.e.[39;49;00m
[37m      [39;49;00m[37m!         1..NLEV <=>  (j) <-> 0[39;49;00m
[37m      [39;49;00m[37m![39;49;00m
[37m      [39;49;00m[37m![39;49;00m
[37m[39;49;00m
[37m      [39;49;00mn_col[37m [39;49;00m=[37m [39;49;00mdesc_data%matrix_data(psb_n_col_)[37m[39;49;00m
[37m      [39;49;00mnr2l[37m  [39;49;00m=[37m [39;49;00mbaseprecv([34m1[39;49;00m)%desc_data%matrix_data(psb_n_col_)[37m[39;49;00m
[37m[39;49;00m
[37m      [39;49;00m[34mallocate[39;49;00m(mlprec_wrk([34m1[39;49;00m)%x2l(nr2l),mlprec_wrk([34m1[39;49;00m)%y2l(nr2l),[37m [39;49;00m&[37m[39;49;00m
[37m           [39;49;00m&[37m [39;49;00mmlprec_wrk([34m1[39;49;00m)%tx(nr2l),[37m [39;49;00m[36mstat[39;49;00m=info)[37m[39;49;00m
[37m      [39;49;00m[34mif[39;49;00m[37m [39;49;00m(info[37m [39;49;00m/=[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mthen[39;49;00m
[34m        [39;49;00m[34mcall [39;49;00mpsb_errpush([34m4010[39;49;00m,name,a_err=[33m'Allocate'[39;49;00m)[37m[39;49;00m
[37m        [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
[37m      [39;49;00m[34mend [39;49;00m[34mif[39;49;00m
[34m[39;49;00m
[34m      [39;49;00mmlprec_wrk([34m1[39;49;00m)%y2l(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
[37m[39;49;00m
[37m[39;49;00m
[37m      [39;49;00mmlprec_wrk([34m1[39;49;00m)%x2l(:)[37m [39;49;00m=[37m [39;49;00mx[37m[39;49;00m
[37m[39;49;00m
[37m      [39;49;00m[34mcall [39;49;00mpsb_baseprc_aply(zone,baseprecv([34m1[39;49;00m),mlprec_wrk([34m1[39;49;00m)%x2l,&[37m[39;49;00m
[37m           [39;49;00m&[37m  [39;49;00mzzero,mlprec_wrk([34m1[39;49;00m)%y2l,&[37m[39;49;00m
[37m           [39;49;00m&[37m  [39;49;00mbaseprecv([34m1[39;49;00m)%base_desc,&[37m[39;49;00m
[37m           [39;49;00m&[37m  [39;49;00mtrans,work,info)[37m[39;49;00m
[37m[39;49;00m
[37m      [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m      [39;49;00mmlprec_wrk([34m1[39;49;00m)%tx[37m [39;49;00m=[37m [39;49;00mmlprec_wrk([34m1[39;49;00m)%x2l[37m[39;49;00m
[37m[39;49;00m
[37m      [39;49;00m[34mcall [39;49;00mpsb_spmm(-zone,baseprecv([34m1[39;49;00m)%base_a,mlprec_wrk([34m1[39;49;00m)%y2l,&[37m[39;49;00m
[37m           [39;49;00m&[37m [39;49;00mzone,mlprec_wrk([34m1[39;49;00m)%tx,baseprecv([34m1[39;49;00m)%base_desc,info,work=work)[37m[39;49;00m
[37m      [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m      [39;49;00m[34mdo [39;49;00milev[37m [39;49;00m=[37m [39;49;00m[34m2[39;49;00m,[37m [39;49;00mnlev[37m[39;49;00m
[37m        [39;49;00mn_row[37m [39;49;00m=[37m [39;49;00mbaseprecv(ilev-[34m1[39;49;00m)%base_desc%matrix_data(psb_n_row_)[37m[39;49;00m
[37m        [39;49;00mn_col[37m [39;49;00m=[37m [39;49;00mbaseprecv(ilev-[34m1[39;49;00m)%desc_data%matrix_data(psb_n_col_)[37m[39;49;00m
[37m        [39;49;00mnr2l[37m  [39;49;00m=[37m [39;49;00mbaseprecv(ilev)%desc_data%matrix_data(psb_n_col_)[37m[39;49;00m
[37m        [39;49;00mnrg[37m   [39;49;00m=[37m [39;49;00mbaseprecv(ilev)%desc_data%matrix_data(psb_n_row_)[37m[39;49;00m
[37m        [39;49;00mismth[37m [39;49;00m=[37m [39;49;00mbaseprecv(ilev)%iprcparm(smth_kind_)[37m[39;49;00m
[37m        [39;49;00m[34mallocate[39;49;00m(mlprec_wrk(ilev)%tx(nr2l),mlprec_wrk(ilev)%y2l(nr2l),&[37m[39;49;00m
[37m             [39;49;00m&[37m   [39;49;00mmlprec_wrk(ilev)%x2l(nr2l),[37m [39;49;00m[36mstat[39;49;00m=info)[37m[39;49;00m
[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(info[37m [39;49;00m/=[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mthen[39;49;00m
[34m          [39;49;00m[34mcall [39;49;00mpsb_errpush([34m4010[39;49;00m,name,a_err=[33m'Allocate'[39;49;00m)[37m[39;49;00m
[37m          [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mend [39;49;00m[34mif[39;49;00m
[34m[39;49;00m
[34m        [39;49;00mmlprec_wrk(ilev)%x2l(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
[37m        [39;49;00mmlprec_wrk(ilev)%y2l(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
[37m        [39;49;00mmlprec_wrk(ilev)%tx(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ismth[37m  [39;49;00m/=[37m [39;49;00mno_smth_)[37m [39;49;00m[34mthen[39;49;00m[37m[39;49;00m
[37m          [39;49;00m[37m![39;49;00m
[37m          [39;49;00m[37m!Smoothed Aggregation[39;49;00m
[37m          [39;49;00m[37m![39;49;00m
[37m          [39;49;00m[34mif[39;49;00m[37m [39;49;00m(baseprecv(ilev)%iprcparm(glb_smth_)[37m [39;49;00m>[34m0[39;49;00m)[37m [39;49;00m[34mthen[39;49;00m
[34m[39;49;00m
[34m            [39;49;00m[34mcall [39;49;00mpsb_halo(mlprec_wrk(ilev-[34m1[39;49;00m)%tx,baseprecv(ilev-[34m1[39;49;00m)%base_desc,&[37m[39;49;00m
[37m                 [39;49;00m&[37m [39;49;00minfo,work=work)[37m[39;49;00m
[37m            [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
[37m          [39;49;00m[34melse[39;49;00m
[34m            [39;49;00mmlprec_wrk(ilev-[34m1[39;49;00m)%tx(n_row+[34m1[39;49;00m:[36mmax[39;49;00m(n_row,n_col))[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
[37m          [39;49;00m[34mend [39;49;00m[34mif[39;49;00m
[34m[39;49;00m
[34m          [39;49;00m[34mcall [39;49;00mpsb_csmm(zone,baseprecv(ilev)%av(sm_pr_t_),mlprec_wrk(ilev-[34m1[39;49;00m)%tx,zzero,&[37m[39;49;00m
[37m               [39;49;00m&[37m [39;49;00mmlprec_wrk(ilev)%x2l,info)[37m[39;49;00m
[37m          [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[34melse[39;49;00m[37m[39;49;00m
[37m          [39;49;00m[37m![39;49;00m
[37m          [39;49;00m[37m! Raw  aggregation, may take shortcuts[39;49;00m
[37m          [39;49;00m[37m![39;49;00m
[37m          [39;49;00mmlprec_wrk(ilev)%x2l[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
[37m          [39;49;00m[34mdo [39;49;00mi=[34m1[39;49;00m,n_row[37m[39;49;00m
[37m            [39;49;00mmlprec_wrk(ilev)%x2l(baseprecv(ilev)%mlia(i))[37m [39;49;00m=[37m [39;49;00m&[37m[39;49;00m
[37m                 [39;49;00m&[37m [39;49;00mmlprec_wrk(ilev)%x2l(baseprecv(ilev)%mlia(i))[37m [39;49;00m+[37m [39;49;00m&[37m[39;49;00m
[37m                 [39;49;00m&[37m  [39;49;00mmlprec_wrk(ilev-[34m1[39;49;00m)%tx(i)[37m[39;49;00m
[37m          [39;49;00m[34mend [39;49;00m[34mdo[39;49;00m
[34m        [39;49;00m[34mend [39;49;00m[34mif[39;49;00m
[34m[39;49;00m
[34m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(baseprecv(ilev)%iprcparm(coarse_mat_)==mat_repl_)[37m [39;49;00m[34mthen[39;49;00m
[34m          [39;49;00m[34mcall [39;49;00mpsb_sum(ictxt,mlprec_wrk(ilev)%x2l([34m1[39;49;00m:nrg))[37m[39;49;00m
[37m        [39;49;00m[34melse [39;49;00m[34mif[39;49;00m[37m [39;49;00m(baseprecv(ilev)%iprcparm(coarse_mat_)[37m [39;49;00m/=[37m [39;49;00mmat_distr_)[37m [39;49;00m[34mthen[39;49;00m
[34m          [39;49;00m[34mwrite[39;49;00m([34m0[39;49;00m,*)[37m [39;49;00m[33m'Unknown value for baseprecv(2)%iprcparm(coarse_mat_) '[39;49;00m,&[37m[39;49;00m
[37m               [39;49;00m&[37m [39;49;00mbaseprecv(ilev)%iprcparm(coarse_mat_)[37m[39;49;00m
[37m        [39;49;00m[34mendif[39;49;00m
[34m[39;49;00m
[34m[39;49;00m
[34m        [39;49;00m[34mcall [39;49;00mpsb_baseprc_aply(zone,baseprecv(ilev),mlprec_wrk(ilev)%x2l,&[37m[39;49;00m
[37m             [39;49;00m&[37m [39;49;00mzzero,mlprec_wrk(ilev)%y2l,baseprecv(ilev)%desc_data,[37m [39;49;00m[33m'N'[39;49;00m,work,info)[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[34mif[39;49;00m(ilev[37m [39;49;00m<[37m [39;49;00mnlev)[37m [39;49;00m[34mthen[39;49;00m
[34m          [39;49;00mmlprec_wrk(ilev)%tx[37m [39;49;00m=[37m [39;49;00mmlprec_wrk(ilev)%x2l[37m[39;49;00m
[37m          [39;49;00m[34mcall [39;49;00mpsb_spmm(-zone,baseprecv(ilev)%base_a,mlprec_wrk(ilev)%y2l,&[37m[39;49;00m
[37m               [39;49;00m&[37m [39;49;00mzone,mlprec_wrk(ilev)%tx,baseprecv(ilev)%base_desc,info,work=work)[37m[39;49;00m
[37m          [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mendif[39;49;00m
[34m[39;49;00m
[34m      [39;49;00m[34menddo[39;49;00m
[34m[39;49;00m
[34m      [39;49;00m[34mdo [39;49;00milev[37m [39;49;00m=[37m [39;49;00mnlev-[34m1[39;49;00m,[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00m-[34m1[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00mismth=baseprecv(ilev+[34m1[39;49;00m)%iprcparm(smth_kind_)[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ismth[37m  [39;49;00m/=[37m [39;49;00mno_smth_)[37m [39;49;00m[34mthen[39;49;00m
[34m[39;49;00m
[34m          [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ismth[37m [39;49;00m==[37m [39;49;00msmth_omg_)[37m [39;49;00m&[37m[39;49;00m
[37m               [39;49;00m&[37m [39;49;00m[34mcall [39;49;00mpsb_halo(mlprec_wrk(ilev+[34m1[39;49;00m)%y2l,&[37m[39;49;00m
[37m               [39;49;00m&[37m [39;49;00mbaseprecv(ilev+[34m1[39;49;00m)%desc_data,info,work=work)[37m[39;49;00m
[37m          [39;49;00m[34mcall [39;49;00mpsb_csmm(zone,baseprecv(ilev+[34m1[39;49;00m)%av(sm_pr_),mlprec_wrk(ilev+[34m1[39;49;00m)%y2l,&[37m[39;49;00m
[37m               [39;49;00m&[37m [39;49;00mzone,mlprec_wrk(ilev)%y2l,info)[37m[39;49;00m
[37m[39;49;00m
[37m          [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[34melse[39;49;00m
[34m[39;49;00m
[34m          [39;49;00mn_row[37m [39;49;00m=[37m [39;49;00mbaseprecv(ilev+[34m1[39;49;00m)%base_desc%matrix_data(psb_n_row_)[37m[39;49;00m
[37m          [39;49;00m[34mdo [39;49;00mi=[34m1[39;49;00m,[37m [39;49;00mn_row[37m[39;49;00m
[37m            [39;49;00mmlprec_wrk(ilev)%y2l(i)[37m [39;49;00m=[37m [39;49;00mmlprec_wrk(ilev)%y2l(i)[37m [39;49;00m+[37m [39;49;00m&[37m[39;49;00m
[37m                 [39;49;00m&[37m [39;49;00mmlprec_wrk(ilev+[34m1[39;49;00m)%y2l(baseprecv(ilev+[34m1[39;49;00m)%mlia(i))[37m[39;49;00m
[37m          [39;49;00m[34menddo[39;49;00m
[34m[39;49;00m
[34m        [39;49;00m[34mend [39;49;00m[34mif[39;49;00m
[34m[39;49;00m
[34m      [39;49;00m[34menddo[39;49;00m
[34m[39;49;00m
[34m      [39;49;00m[34mcall [39;49;00mpsb_geaxpby(alpha,mlprec_wrk([34m1[39;49;00m)%y2l,beta,y,&[37m[39;49;00m
[37m           [39;49;00m&[37m  [39;49;00mbaseprecv([34m1[39;49;00m)%base_desc,info)[37m[39;49;00m
[37m[39;49;00m
[37m      [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[34mcase[39;49;00m(smooth_both_)[37m[39;49;00m
[37m[39;49;00m
[37m      [39;49;00m[37m![39;49;00m
[37m      [39;49;00m[37m!    Symmetrized  smoothing.[39;49;00m
[37m      [39;49;00m[37m!    1.   X(1)  = Xext[39;49;00m
[37m      [39;49;00m[37m!    2.   Y(1)  = (K(1)**(-1))*X(1)[39;49;00m
[37m      [39;49;00m[37m!    3.   TX(1) = X(1) - A(1)*Y(1)[39;49;00m
[37m      [39;49;00m[37m!    4.   DO ILEV=2, NLEV[39;49;00m
[37m      [39;49;00m[37m!          X(ILEV) = AV(PR_SM_T_,ILEV)*TX(ILEV-1)[39;49;00m
[37m      [39;49;00m[37m!          Y(ILEV) = (K(ILEV)**(-1))*X(ILEV)[39;49;00m
[37m      [39;49;00m[37m!          TX(ILEV) = (X(ILEV)-A(ILEV)*Y(ILEV))[39;49;00m
[37m      [39;49;00m[37m!    5.   DO  ILEV=NLEV-1,1,-1[39;49;00m
[37m      [39;49;00m[37m!          Y(ILEV) = Y(ILEV) + AV(PR_SM_,ILEV+1)*Y(ILEV+1)[39;49;00m
[37m      [39;49;00m[37m!          Y(ILEV) = Y(ILEV) + (K(ILEV)**(-1))*(X(ILEV)-A(ILEV)*Y(ILEV))[39;49;00m
[37m      [39;49;00m[37m!    6.  Yext    = beta*Yext + Y(1)[39;49;00m
[37m      [39;49;00m[37m![39;49;00m
[37m      [39;49;00m[37m!    Note: level numbering reversed wrt ref. DD, i.e.[39;49;00m
[37m      [39;49;00m[37m!         1..NLEV <=>  (j) <-> 0[39;49;00m
[37m      [39;49;00m[37m![39;49;00m
[37m      [39;49;00m[37m![39;49;00m
[37m      [39;49;00mn_col[37m [39;49;00m=[37m [39;49;00mdesc_data%matrix_data(psb_n_col_)[37m[39;49;00m
[37m      [39;49;00mnr2l[37m  [39;49;00m=[37m [39;49;00mbaseprecv([34m1[39;49;00m)%desc_data%matrix_data(psb_n_col_)[37m[39;49;00m
[37m[39;49;00m
[37m      [39;49;00m[34mallocate[39;49;00m(mlprec_wrk([34m1[39;49;00m)%x2l(nr2l),mlprec_wrk([34m1[39;49;00m)%y2l(nr2l),[37m [39;49;00m&[37m[39;49;00m
[37m           [39;49;00m&[37m [39;49;00mmlprec_wrk([34m1[39;49;00m)%ty(nr2l),[37m [39;49;00mmlprec_wrk([34m1[39;49;00m)%tx(nr2l),[37m [39;49;00m[36mstat[39;49;00m=info)[37m[39;49;00m
[37m[39;49;00m
[37m      [39;49;00mmlprec_wrk([34m1[39;49;00m)%x2l(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
[37m      [39;49;00mmlprec_wrk([34m1[39;49;00m)%y2l(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
[37m      [39;49;00mmlprec_wrk([34m1[39;49;00m)%tx(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
[37m      [39;49;00mmlprec_wrk([34m1[39;49;00m)%ty(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
[37m[39;49;00m
[37m[39;49;00m
[37m      [39;49;00m[34mif[39;49;00m[37m [39;49;00m(info[37m [39;49;00m/=[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mthen[39;49;00m
[34m        [39;49;00m[34mcall [39;49;00mpsb_errpush([34m4010[39;49;00m,name,a_err=[33m'Allocate'[39;49;00m)[37m[39;49;00m
[37m        [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
[37m      [39;49;00m[34mend [39;49;00m[34mif[39;49;00m
[34m[39;49;00m
[34m      [39;49;00m[34mcall [39;49;00mpsb_geaxpby(zone,x,zzero,mlprec_wrk([34m1[39;49;00m)%x2l,&[37m[39;49;00m
[37m           [39;49;00m&[37m [39;49;00mbaseprecv([34m1[39;49;00m)%base_desc,info)[37m[39;49;00m
[37m      [39;49;00m[34mcall [39;49;00mpsb_geaxpby(zone,x,zzero,mlprec_wrk([34m1[39;49;00m)%tx,&[37m[39;49;00m
[37m           [39;49;00m&[37m [39;49;00mbaseprecv([34m1[39;49;00m)%base_desc,info)[37m[39;49;00m
[37m[39;49;00m
[37m      [39;49;00m[34mcall [39;49;00mpsb_baseprc_aply(zone,baseprecv([34m1[39;49;00m),mlprec_wrk([34m1[39;49;00m)%x2l,&[37m[39;49;00m
[37m           [39;49;00m&[37m  [39;49;00mzzero,mlprec_wrk([34m1[39;49;00m)%y2l,&[37m[39;49;00m
[37m           [39;49;00m&[37m  [39;49;00mbaseprecv([34m1[39;49;00m)%base_desc,&[37m[39;49;00m
[37m           [39;49;00m&[37m  [39;49;00mtrans,work,info)[37m[39;49;00m
[37m[39;49;00m
[37m      [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m      [39;49;00mmlprec_wrk([34m1[39;49;00m)%ty[37m [39;49;00m=[37m [39;49;00mmlprec_wrk([34m1[39;49;00m)%x2l[37m[39;49;00m
[37m[39;49;00m
[37m      [39;49;00m[34mcall [39;49;00mpsb_spmm(-zone,baseprecv([34m1[39;49;00m)%base_a,mlprec_wrk([34m1[39;49;00m)%y2l,&[37m[39;49;00m
[37m           [39;49;00m&[37m [39;49;00mzone,mlprec_wrk([34m1[39;49;00m)%ty,baseprecv([34m1[39;49;00m)%base_desc,info,work=work)[37m[39;49;00m
[37m      [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m      [39;49;00m[34mdo [39;49;00milev[37m [39;49;00m=[37m [39;49;00m[34m2[39;49;00m,[37m [39;49;00mnlev[37m[39;49;00m
[37m        [39;49;00mn_row[37m [39;49;00m=[37m [39;49;00mbaseprecv(ilev-[34m1[39;49;00m)%base_desc%matrix_data(psb_n_row_)[37m[39;49;00m
[37m        [39;49;00mn_col[37m [39;49;00m=[37m [39;49;00mbaseprecv(ilev-[34m1[39;49;00m)%desc_data%matrix_data(psb_n_col_)[37m[39;49;00m
[37m        [39;49;00mnr2l[37m  [39;49;00m=[37m [39;49;00mbaseprecv(ilev)%desc_data%matrix_data(psb_n_col_)[37m[39;49;00m
[37m        [39;49;00mnrg[37m   [39;49;00m=[37m [39;49;00mbaseprecv(ilev)%desc_data%matrix_data(psb_n_row_)[37m[39;49;00m
[37m        [39;49;00mismth=baseprecv(ilev)%iprcparm(smth_kind_)[37m[39;49;00m
[37m        [39;49;00m[34mallocate[39;49;00m(mlprec_wrk(ilev)%ty(nr2l),mlprec_wrk(ilev)%y2l(nr2l),&[37m[39;49;00m
[37m             [39;49;00m&[37m   [39;49;00mmlprec_wrk(ilev)%x2l(nr2l),[37m [39;49;00m[36mstat[39;49;00m=info)[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00mmlprec_wrk(ilev)%x2l(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
[37m        [39;49;00mmlprec_wrk(ilev)%y2l(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
[37m        [39;49;00mmlprec_wrk(ilev)%tx(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
[37m        [39;49;00mmlprec_wrk(ilev)%ty(:)[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(info[37m [39;49;00m/=[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m[34mthen[39;49;00m
[34m          [39;49;00m[34mcall [39;49;00mpsb_errpush([34m4010[39;49;00m,name,a_err=[33m'Allocate'[39;49;00m)[37m[39;49;00m
[37m          [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mend [39;49;00m[34mif[39;49;00m
[34m[39;49;00m
[34m[39;49;00m
[34m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ismth[37m  [39;49;00m/=[37m [39;49;00mno_smth_)[37m [39;49;00m[34mthen[39;49;00m[37m[39;49;00m
[37m          [39;49;00m[37m![39;49;00m
[37m          [39;49;00m[37m!Smoothed Aggregation[39;49;00m
[37m          [39;49;00m[37m![39;49;00m
[37m          [39;49;00m[34mif[39;49;00m[37m [39;49;00m(baseprecv(ilev)%iprcparm(glb_smth_)[37m [39;49;00m>[34m0[39;49;00m)[37m [39;49;00m[34mthen[39;49;00m
[34m[39;49;00m
[34m            [39;49;00m[34mcall [39;49;00mpsb_halo(mlprec_wrk(ilev-[34m1[39;49;00m)%ty,baseprecv(ilev-[34m1[39;49;00m)%base_desc,&[37m[39;49;00m
[37m                 [39;49;00m&[37m [39;49;00minfo,work=work)[37m[39;49;00m
[37m            [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
[37m          [39;49;00m[34melse[39;49;00m
[34m            [39;49;00mmlprec_wrk(ilev-[34m1[39;49;00m)%ty(n_row+[34m1[39;49;00m:[36mmax[39;49;00m(n_row,n_col))[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
[37m          [39;49;00m[34mend [39;49;00m[34mif[39;49;00m
[34m[39;49;00m
[34m          [39;49;00m[34mcall [39;49;00mpsb_csmm(zone,baseprecv(ilev)%av(sm_pr_t_),mlprec_wrk(ilev-[34m1[39;49;00m)%ty,zzero,&[37m[39;49;00m
[37m               [39;49;00m&[37m [39;49;00mmlprec_wrk(ilev)%x2l,info)[37m[39;49;00m
[37m          [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[34melse[39;49;00m[37m[39;49;00m
[37m          [39;49;00m[37m![39;49;00m
[37m          [39;49;00m[37m! Raw  aggregation, may take shortcuts[39;49;00m
[37m          [39;49;00m[37m![39;49;00m
[37m          [39;49;00mmlprec_wrk(ilev)%x2l[37m [39;49;00m=[37m [39;49;00mzzero[37m[39;49;00m
[37m          [39;49;00m[34mdo [39;49;00mi=[34m1[39;49;00m,n_row[37m[39;49;00m
[37m            [39;49;00mmlprec_wrk(ilev)%x2l(baseprecv(ilev)%mlia(i))[37m [39;49;00m=[37m [39;49;00m&[37m[39;49;00m
[37m                 [39;49;00m&[37m [39;49;00mmlprec_wrk(ilev)%x2l(baseprecv(ilev)%mlia(i))[37m [39;49;00m+[37m [39;49;00m&[37m[39;49;00m
[37m                 [39;49;00m&[37m  [39;49;00mmlprec_wrk(ilev-[34m1[39;49;00m)%ty(i)[37m[39;49;00m
[37m          [39;49;00m[34mend [39;49;00m[34mdo[39;49;00m
[34m        [39;49;00m[34mend [39;49;00m[34mif[39;49;00m
[34m[39;49;00m
[34m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(baseprecv(ilev)%iprcparm(coarse_mat_)==mat_repl_)[37m [39;49;00m[34mthen[39;49;00m
[34m          [39;49;00m[34mcall [39;49;00mpsb_sum(ictxt,mlprec_wrk(ilev)%x2l([34m1[39;49;00m:nrg))[37m[39;49;00m
[37m        [39;49;00m[34melse [39;49;00m[34mif[39;49;00m[37m [39;49;00m(baseprecv(ilev)%iprcparm(coarse_mat_)[37m [39;49;00m/=[37m [39;49;00mmat_distr_)[37m [39;49;00m[34mthen[39;49;00m
[34m          [39;49;00m[34mwrite[39;49;00m([34m0[39;49;00m,*)[37m [39;49;00m[33m'Unknown value for baseprecv(2)%iprcparm(coarse_mat_) '[39;49;00m,&[37m[39;49;00m
[37m               [39;49;00m&[37m [39;49;00mbaseprecv(ilev)%iprcparm(coarse_mat_)[37m[39;49;00m
[37m        [39;49;00m[34mendif[39;49;00m
[34m[39;49;00m
[34m        [39;49;00m[34mcall [39;49;00mpsb_geaxpby(zone,mlprec_wrk(ilev)%x2l,zzero,mlprec_wrk(ilev)%tx,&[37m[39;49;00m
[37m             [39;49;00m&[37m [39;49;00mbaseprecv(ilev)%base_desc,info)[37m[39;49;00m
[37m        [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[34mcall [39;49;00mpsb_baseprc_aply(zone,baseprecv(ilev),mlprec_wrk(ilev)%x2l,&[37m[39;49;00m
[37m             [39;49;00m&[37m [39;49;00mzzero,mlprec_wrk(ilev)%y2l,baseprecv(ilev)%desc_data,[37m [39;49;00m[33m'N'[39;49;00m,work,info)[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[34mif[39;49;00m(ilev[37m [39;49;00m<[37m [39;49;00mnlev)[37m [39;49;00m[34mthen[39;49;00m
[34m          [39;49;00mmlprec_wrk(ilev)%ty[37m [39;49;00m=[37m [39;49;00mmlprec_wrk(ilev)%x2l[37m[39;49;00m
[37m          [39;49;00m[34mcall [39;49;00mpsb_spmm(-zone,baseprecv(ilev)%base_a,mlprec_wrk(ilev)%y2l,&[37m[39;49;00m
[37m               [39;49;00m&[37m [39;49;00mzone,mlprec_wrk(ilev)%ty,baseprecv(ilev)%base_desc,info,work=work)[37m[39;49;00m
[37m          [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mendif[39;49;00m
[34m[39;49;00m
[34m      [39;49;00m[34menddo[39;49;00m
[34m[39;49;00m
[34m[39;49;00m
[34m      [39;49;00m[34mdo [39;49;00milev=nlev-[34m1[39;49;00m,[37m [39;49;00m[34m1[39;49;00m,[37m [39;49;00m-[34m1[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00mismth=baseprecv(ilev+[34m1[39;49;00m)%iprcparm(smth_kind_)[37m[39;49;00m
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ismth[37m  [39;49;00m/=[37m [39;49;00mno_smth_)[37m [39;49;00m[34mthen[39;49;00m
[34m          [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ismth[37m [39;49;00m==[37m [39;49;00msmth_omg_)[37m [39;49;00m&[37m[39;49;00m
[37m               [39;49;00m&[37m [39;49;00m[34mcall [39;49;00mpsb_halo(mlprec_wrk(ilev+[34m1[39;49;00m)%y2l,baseprecv(ilev+[34m1[39;49;00m)%desc_data,&[37m[39;49;00m
[37m               [39;49;00m&[37m  [39;49;00minfo,work=work)[37m[39;49;00m
[37m          [39;49;00m[34mcall [39;49;00mpsb_csmm(zone,baseprecv(ilev+[34m1[39;49;00m)%av(sm_pr_),mlprec_wrk(ilev+[34m1[39;49;00m)%y2l,&[37m[39;49;00m
[37m               [39;49;00m&[37m  [39;49;00mzone,mlprec_wrk(ilev)%y2l,info)[37m[39;49;00m
[37m          [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[34melse[39;49;00m
[34m          [39;49;00mn_row[37m [39;49;00m=[37m [39;49;00mbaseprecv(ilev)%base_desc%matrix_data(psb_n_row_)[37m[39;49;00m
[37m          [39;49;00m[34mdo [39;49;00mi=[34m1[39;49;00m,[37m [39;49;00mn_row[37m[39;49;00m
[37m            [39;49;00mmlprec_wrk(ilev)%y2l(i)[37m [39;49;00m=[37m [39;49;00mmlprec_wrk(ilev)%y2l(i)[37m [39;49;00m+[37m [39;49;00m&[37m[39;49;00m
[37m                 [39;49;00m&[37m [39;49;00mmlprec_wrk(ilev+[34m1[39;49;00m)%y2l(baseprecv(ilev+[34m1[39;49;00m)%mlia(i))[37m[39;49;00m
[37m          [39;49;00m[34menddo[39;49;00m
[34m[39;49;00m
[34m        [39;49;00m[34mend [39;49;00m[34mif[39;49;00m
[34m[39;49;00m
[34m        [39;49;00m[34mcall [39;49;00mpsb_spmm(-zone,baseprecv(ilev)%base_a,mlprec_wrk(ilev)%y2l,&[37m[39;49;00m
[37m             [39;49;00m&[37m   [39;49;00mzone,mlprec_wrk(ilev)%tx,baseprecv(ilev)%base_desc,info,work=work)[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[34mcall [39;49;00mpsb_baseprc_aply(zone,baseprecv(ilev),mlprec_wrk(ilev)%tx,&[37m[39;49;00m
[37m             [39;49;00m&[37m [39;49;00mzone,mlprec_wrk(ilev)%y2l,baseprecv(ilev)%base_desc,[37m [39;49;00mtrans,[37m [39;49;00mwork,info)[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m      [39;49;00m[34menddo[39;49;00m
[34m[39;49;00m
[34m      [39;49;00m[34mcall [39;49;00mpsb_geaxpby(alpha,mlprec_wrk([34m1[39;49;00m)%y2l,beta,y,&[37m[39;49;00m
[37m           [39;49;00m&[37m   [39;49;00mbaseprecv([34m1[39;49;00m)%base_desc,info)[37m[39;49;00m
[37m[39;49;00m
[37m      [39;49;00m[34mif[39;49;00m(info[37m [39;49;00m/=[34m0[39;49;00m)[37m [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[34mcase [39;49;00mdefault[37m[39;49;00m
[37m[39;49;00m
[37m      [39;49;00m[34mcall [39;49;00mpsb_errpush([34m4013[39;49;00m,name,a_err=[33m'wrong smooth_pos'[39;49;00m,&[37m[39;49;00m
[37m           [39;49;00m&[37m  [39;49;00mi_Err=(/baseprecv([34m2[39;49;00m)%iprcparm(smth_pos_),[34m0[39;49;00m,[34m0[39;49;00m,[34m0[39;49;00m,[34m0[39;49;00m/))[37m[39;49;00m
[37m      [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[34mend [39;49;00m[34mselect[39;49;00m
[34m[39;49;00m
[34m  [39;49;00m[34mcase [39;49;00mdefault[37m[39;49;00m
[37m    [39;49;00m[34mcall [39;49;00mpsb_errpush([34m4013[39;49;00m,name,a_err=[33m'wrong mltype'[39;49;00m,&[37m[39;49;00m
[37m         [39;49;00m&[37m  [39;49;00mi_Err=(/baseprecv([34m2[39;49;00m)%iprcparm(ml_type_),[34m0[39;49;00m,[34m0[39;49;00m,[34m0[39;49;00m,[34m0[39;49;00m/))[37m[39;49;00m
[37m    [39;49;00m[34mgo[39;49;00m[34mto[39;49;00m[37m [39;49;00m[34m9999[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m  [39;49;00m[34mend [39;49;00m[34mselect[39;49;00m
[34m[39;49;00m
[34m[39;49;00m
[34m  [39;49;00m[34mcall [39;49;00mmlprec_wrk_free(mlprec_wrk)[37m[39;49;00m
[37m  [39;49;00m[34mdeallocate[39;49;00m(mlprec_wrk)[37m[39;49;00m
[37m[39;49;00m
[37m  [39;49;00m[34mcall [39;49;00mpsb_erractionrestore(err_act)[37m[39;49;00m
[37m  [39;49;00m[34mreturn[39;49;00m
[34m[39;49;00m
[34m9999[39;49;00m[37m [39;49;00m[34mcontinue[39;49;00m
[34m  [39;49;00m[34mcall [39;49;00mpsb_errpush(info,name)[37m[39;49;00m
[37m  [39;49;00m[34mcall [39;49;00mpsb_erractionrestore(err_act)[37m[39;49;00m
[37m  [39;49;00m[34mif[39;49;00m[37m [39;49;00m(err_act.eq.act_abort)[37m [39;49;00m[34mthen[39;49;00m
[34m    [39;49;00m[34mcall [39;49;00mpsb_error()[37m[39;49;00m
[37m    [39;49;00m[34mreturn[39;49;00m
[34m  [39;49;00m[34mend [39;49;00m[34mif[39;49;00m
[34m  [39;49;00m[34mreturn[39;49;00m
[34m[39;49;00m
[34mcontains[39;49;00m
[34m  [39;49;00m[34msubroutine [39;49;00mmlprec_wrk_free(wrk)[37m[39;49;00m
[37m    [39;49;00m[34mtype[39;49;00m(psb_mlprec_wrk_type)[37m [39;49;00m[34m::[39;49;00m[37m [39;49;00mwrk(:)[37m[39;49;00m
[37m    [39;49;00m[37m! This will not be needed when we have allocatables, as[39;49;00m
[37m    [39;49;00m[37m! it is sufficient to deallocate the container, and[39;49;00m
[37m    [39;49;00m[37m! the compiler is supposed to recursively deallocate the[39;49;00m
[37m    [39;49;00m[37m! various components.[39;49;00m
[37m    [39;49;00m[36minteger [39;49;00mi[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[34mdo [39;49;00mi=[34m1[39;49;00m,[37m [39;49;00msize(wrk)[37m[39;49;00m
[37m      [39;49;00m[34mif[39;49;00m[37m [39;49;00m([36massociated[39;49;00m(wrk(i)%tx))[37m  [39;49;00m[34mdeallocate[39;49;00m(wrk(i)%tx)[37m[39;49;00m
[37m      [39;49;00m[34mif[39;49;00m[37m [39;49;00m([36massociated[39;49;00m(wrk(i)%ty))[37m  [39;49;00m[34mdeallocate[39;49;00m(wrk(i)%ty)[37m[39;49;00m
[37m      [39;49;00m[34mif[39;49;00m[37m [39;49;00m([36massociated[39;49;00m(wrk(i)%x2l))[37m [39;49;00m[34mdeallocate[39;49;00m(wrk(i)%x2l)[37m[39;49;00m
[37m      [39;49;00m[34mif[39;49;00m[37m [39;49;00m([36massociated[39;49;00m(wrk(i)%y2l))[37m [39;49;00m[34mdeallocate[39;49;00m(wrk(i)%y2l)[37m[39;49;00m
[37m      [39;49;00m[34mif[39;49;00m[37m [39;49;00m([36massociated[39;49;00m(wrk(i)%b2l))[37m [39;49;00m[34mdeallocate[39;49;00m(wrk(i)%b2l)[37m[39;49;00m
[37m      [39;49;00m[34mif[39;49;00m[37m [39;49;00m([36massociated[39;49;00m(wrk(i)%tty))[37m [39;49;00m[34mdeallocate[39;49;00m(wrk(i)%tty)[37m[39;49;00m
[37m    [39;49;00m[34mend [39;49;00m[34mdo[39;49;00m
[34m  [39;49;00m[34mend [39;49;00m[34msubroutine [39;49;00mmlprec_wrk_free[37m[39;49;00m
[37m[39;49;00m
[34mend [39;49;00m[34msubroutine [39;49;00mpsb_zmlprc_aply

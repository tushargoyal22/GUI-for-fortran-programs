implicit none
real:: deltax,deltat,Le,Cm_0,alpha,alphasf,alphaim,thetafs,thetasl,thetaim,maxerr,Pe, Cau,vsl,vfs,Dfs,Dsl
real:: Ffs,Fsl,Fim,ffs1,fsl1,fim1,rhob,Kfs,Ksl,Kim,kfs1,ksl1,kim1,tmax,tp,qfs,qsl,time,objf
integer::i,j,nn,limiter,k,np
real,dimension(2000)::Cf_new,Cs_new,Ci_new,Cv,Cf_newiiter
Real,dimension(2000)::Sf_new,Ss_new,Si_new

!parameter estimation parameters
real,dimension(200)::timeobs,zobs,err,errnew,errfin
real,dimension(200):: b,paracode,p
integer,dimension(200)::nelt
real,dimension(200,200)::ccal,cobs,cpred
integer:: nz,nm,maxzobs,maxtobs,maxpar,maxunpar



open(unit=1,file='out_exp.dat')
!open(unit=2,file='ck.txt')
open(unit=3,file='observation.txt')
open(unit=4,file='in_1.dat')
open(unit=5,file='in_2.dat')
open(unit=6,file='output.dat')
open(unit=7,file='in_3.dat')

Read(7,*) nz,nm
!nz=100
!nm=20

!observation data
Read(5,*) maxzobs
write(*,*) maxzobs
Read(5,*) (zobs(i),i=1,maxzobs)
Read(4,*) qsl,qfs,alphaim,alphasf,alpha
Read(4,*) maxtobs
do i=1,maxzobs
read(4,*)(cobs(i,j),j=1,maxtobs)
enddo
read(5,*) (timeobs(i),i=1,maxtobs)


!write(1,*) "zobs"
!write(1,*) (zobs1(i),i=1,maxzobs)
!write(1,*) "timeobs"
!write (*,*) (timeobs(i),i=1,maxtobs)



!In observation.txt file
!Maximum parameter, maximum unknown parameter, maximum distance observed, maximum observed time, 1
!Depending upon maxpar, 1 for unknown and 2 for known
!Value of known parameter and initial guess for unknown (1) parameter
!For each distance at max observed time, concentration values
!For next distance if maxzobs >1, then at max observed time, concentration values
!Given value of distance i.e. at which maxzobs is taken
!Given value of time i.e. at which maxtobs is taken
!Actual value of parameter

!Input Parameter decleration
!********************************************************************
! Input Parameters
Read(7,*) Le,rhob,tmax,tp,deltat,deltax
Read(7,*) thetafs,thetasl,thetaim
Read(7,*) Ffs,Fsl,Fim,ffs1,fsl1,fim1
Read(7,*) Kfs,Ksl,Kim,kfs1,ksl1,kim1

!Le=16.87
!qsl=5.0
!qfs=2.5e-2
!thetaim=0.04
!thetasl=0.4
!thetafs=0.14
!alphaim=0.02
!alphasf=0.05
!alpha=1.0
!Ffs=0.0
!Fsl=0.0
!Fim=0.0
!ffs1=0.0
!fsl1=0.0
!fim1=0.0
!Note: ffs+fsl+fim=1
!Kfs=0.0
!Ksl=0.0
!Kim=0.0
!kfs1=0.0
!ksl1=0.0
!kim1=0.0
!rhob=1.36
Cm_0=1.0
!tmax=45.0
!tp=45.0
!deltat=0.01
!deltax=0.1

vsl=qsl/thetasl
vfs=qfs/thetafs
Dsl=alpha*vsl
Dfs=alpha*vfs

Pe=(vfs*(deltax/Dfs))
Cau=(vfs*(deltat/deltax))

WRITE(*,*)  'Peclet number=', Pe
WRITE(*,*)  'Caurant no.=', Cau
!stop


!*******************************************************


do i=1,maxzobs
nelt(i)=int(zobs(i)/deltax)
!write(*,*) zobs(i),nelt(i)
enddo

!Computation starts
call transport(Le,deltax,deltat,time,Cm_0,nn,tmax,tp,qfs,qsl,alphasf,alphaim,alpha,Kfs,Ksl,Kim,kfs1,ksl1,kim1,rhob,Ffs,Fsl,Fim,ffs1,fsl1,fim1,thetafs,thetasl,thetaim,Cv,Cf_new,Cs_new,Ci_new,Sf_new,Ss_new,Si_new,cobs,maxtobs,maxzobs,j,timeobs,zobs,ccal,nelt,objf)

!write(*,*) "objf",objf
 !stop
do j=1,maxzobs
do k=1,maxtobs
write(6,*) cobs(j,k),ccal(j,k)
enddo
enddo

!write(1,*) "cobsl"
!write(1,201) ((cobs(j,k),k=1,maxtobs),j=1,maxzobs)
stop
end

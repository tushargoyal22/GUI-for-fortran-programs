!!Parameter estimation for volumetric average_TPNE


subroutine transport(Le,deltax,deltat,time,Cm_0,nn,tmax,tp,qfs,qsl,alphasf,alphaim,alpha,Kfs,Ksl,Kim,kfs1,ksl1,kim1,rhob,Ffs,Fsl,Fim,ffs1,fsl1,fim1,thetafs,thetasl,thetaim,Cv_new,Cf_new,Cs_new,Ci_new,Sf_new,Ss_new,Si_new,cobs,maxtobs,maxzobs,j,timeobs,zobs,ccal,nelt,objf)
implicit none
Real :: Ffs,Fsl,Fim,ffs1,fsl1,fim1,rhob,Kfs,Ksl,Kim,kfs1,ksl1,kim1,deltax,tmax,tp,deltat,qfs,qsl,time
Real::  alphasf,alphaim,alpha,thetafs,thetasl,thetaim
Real:: A11,A22,A33,A44,A55,A66,A77,A88,Rfs,Rsl,Rim
integer::i,nn,j,np,itter
Real,dimension(2000)::a1,d1,b1,r1,a2,b2,d2,r2,Cv_old,Cv_new,Cf_old,Cf_new,Cs_old,Cs_new,Ci_old,Ci_new,Sf_old,Sf_new,Ss_old,Ss_new,Si_old,Si_new,Cf_newiiter
Real:: Le,Cm_0,maxerr,err

!optimazation parameters
real,dimension(200)::timeobs,zobs
real::cdiff1,cdiff2,tdiff1,tdiff2,cdiff,zdiff,c22,objf,sum,c11
integer,dimension(200)::nelt
real,dimension(200,200)::ccal,cobs
integer::ll2,maxzobs,maxtobs
open(unit=111,file='Cv.txt')

do i=1,maxzobs
!nelt(i)=int(zobs(i)/deltax)
!write(*,*) i, zobs(i),nelt(i)
!write (*,*) (timeobs(i),i=1,maxtobs)
enddo

Rfs=(thetafs+(Ffs*ffs1*rhob*Kfs))
Rsl=(thetasl+(Fsl*fsl1*rhob*Ksl))
Rim=(thetaim+(Fim*fim1*rhob*Kim))

!nt=tmax/deltat
np=(tp/deltat)
nn=(Le/deltax)+1

A11=kfs1*deltat*(1.D0-Ffs)*Kfs
A22=1.D0+(kfs1*deltat)
A33=ksl1*deltat*(1.D0-Fsl)*Ksl
A44=1.D0+(ksl1*deltat)
A55=kim1*deltat*(1.D0-Fim)*Kim
A66=1.D0+(kim1*deltat)
A77=(Rim)+(alphaim*deltat)+((fim1*rhob*A55)/A66)
A88=(fim1*rhob)-(fim1*rhob/A66)


!WRITE(*,*)  'A11=', A11
!WRITE(*,*)  'A22=', A22
!WRITE(*,*)  'A33=', A33
!WRITE(*,*)  'A44=', A44
!WRITE(*,*)  'A55=', A55
!WRITE(*,*)  'A66=', A66
!WRITE(*,*)  'A77=', A77
!WRITE(*,*)  'A88=', A88
!WRITE(*,*)  'tp=', tp
!WRITE(*,*)  'Rfs=', Rfs
!WRITE(*,*)  'Kfs=', Kfs
!WRITE(*,*)  'kfs=', kfs1


!stop
!OPEN(11,FILE='FASTConcentration_OUT.TXT')

!initial condition: fast, slow and immobile conc in liquid and sorbed phase zero
do i=1,(nn)
Cf_old=0.0
Cs_old=0.0
Ci_old=0.0
Sf_old=0.0
Ss_old=0.0
Si_old=0.0
Cv_old=0.0
Cf_new=0.0
Cs_new=0.0
Ci_new=0.0
Sf_new=0.0
Ss_new=0.0
Si_new=0.0
Cv_new=0.0
 enddo


!do t=1,(nt),1
 ll2=1
time=deltat
do while(time.le.tmax)
!write(*,*) time

do i=1,nn
Cf_old(i)=Cf_new(i)
Cs_old(i)=Cs_new(i)
Ci_old(i)=Ci_new(i)
Sf_old(i)=Sf_new(i)
Ss_old(i)=Ss_new(i)
Si_old(i)=Si_new(i)
Cv_old(i)=Cv_new(i)
enddo



!Calculation for fast region
!======================================
 ! Cf_old=Cf_new
  !Cs_old=Cs_new
  !Ci_old=Ci_new
  !Sf_old=Sf_new
  !Ss_old=Ss_new
  !Si_old=Si_new

  itter=0

5  itter=itter+1
  maxerr=0.0
  Cf_newiiter=Cf_new
	 a1=0.0
	 b1=0.0
	 d1=0.0
!Inlet Boundary condition for fast region
    b1(1)=0.0
	d1(1)=1.0
	a1(1)=0.0

	if (time.le.tp)then
		r1(1)=Cm_0
	else
		r1(1)=0.0
	endif


!Outlet Boundary conditions	for fast region
	!b1(nn)=(-1.0)
	!d1(nn)=1.0
	!a1(nn)=0.0
	!r1(nn)=0.0

	b1(nn)=-((qfs*deltat*deltax)/(2.0))-(alpha*qfs*deltat)
	d1(nn)=(Rfs*deltax*deltax)+(alpha*qfs*deltat)+(alphasf*deltat*deltax*deltax)+((ffs1*rhob*deltax*deltax*A11)/A22)+(qfs*deltat*deltax/2.0)
	r1(nn)=(Rfs*deltax*deltax*Cf_old(nn))+(alphasf*deltat*deltax*deltax*Cs_new(nn))+(-(ffs1*rhob*deltax*deltax/A22)+(ffs1*rhob*deltax*deltax))*Sf_old(nn)



!Intermediate coefficient calculation

do i=2,(nn-1)
   b1(i)=-((qfs*deltat*deltax)/(2.0))-(alpha*qfs*deltat)
   d1(i)=(Rfs*deltax*deltax)+(2.0*alpha*qfs*deltat)+(alphasf*deltat*deltax*deltax)+((ffs1*rhob*deltax*deltax*A11)/A22)
   a1(i)=-(alpha*qfs*deltat)+(qfs*deltat*deltax/2.0)
   r1(i)=(Rfs*deltax*deltax*Cf_old(i))+(alphasf*deltat*deltax*deltax*Cs_new(i))+(-(ffs1*rhob*deltax*deltax/A22)+(ffs1*rhob*deltax*deltax))*Sf_old(i)
 enddo
 !TDMA for Cf_____(Thomas Algorithm Starts)

  do i=2,nn
		d1(i)=d1(i)-((b1(i)/d1(i-1))*a1(i-1))
		r1(i)=r1(i)-((b1(i)/d1(i-1))*r1(i-1))
  enddo

	   Cf_new(nn)=r1(nn)/d1(nn)

 do i=(nn-1),1,-1
 Cf_new(i)=((r1(i)-(a1(i)*Cf_new(i+1)))/d1(i))
! WRITE(*,*)time,Cf_new(i)

 enddo

 !  do i=1,nn
 !if (i==nn) then
!WRITE(11,*)((time)),Cf_new(i), Cf_old(i)
!endif
!enddo


!do t=0,(nt-1),1
 ! WRITE(*,*)((t+1)*deltat),Cf_new(i)
 !enddo
  !22  FORMAT(5F12.6)

 !Sorption in fast region calculation
 do i=1,nn
 Sf_new(i)=((A11/A22)*Cf_new(i))+(Sf_old(i)/A22)
 enddo


!Calculation for slow region
!======================================
!Inlet Boundary condition for slow region
b2=0.0
a2=0.0
d2=0.0

    b2(1)=0.0
	d2(1)=1.0
	a2(1)=0.0

	if (time.le.tp)then
		r2(1)=Cm_0
	else
		r2(1)=0.0
	endif

!Outlet Boundary conditions	for slow region
	b2(nn)=-(qsl*deltat*deltax/2.0)-(alpha*qsl*deltat)
	d2(nn)=(Rsl*deltax*deltax)+(alpha*qsl*deltat)+(alphasf*deltat*deltax*deltax)+(alphaim*deltat*deltax*deltax)-((alphaim*alphaim*deltat*deltat*deltax*deltax)/A77)+((fsl1*rhob*deltax*deltax*A33)/A44)+(qsl*deltat*deltax/2.0)
	r2(nn)=(Rsl*deltax*deltax*Cs_old(nn))+(alphasf*deltat*deltax*deltax*Cf_new(nn))+((alphaim*deltat*deltax*deltax*A88*Si_old(nn))/A77)+(-((fsl1*rhob*deltax*deltax)/A44)+(fsl1*rhob*deltax*deltax))*Ss_old(nn)

!Intermediate coefficient calculation
do i=2,(nn-1)
b2(i)=-(qsl*deltat*deltax/2.0)-(alpha*qsl*deltat)
d2(i)=(Rsl*deltax*deltax)+(2.0*alpha*qsl*deltat)+(alphasf*deltat*deltax*deltax)+(alphaim*deltat*deltax*deltax)-((alphaim*alphaim*deltat*deltat*deltax*deltax)/A77)+((fsl1*rhob*deltax*deltax*A33)/A44)
a2(i)=-(alpha*qsl*deltat)+(qsl*deltat*deltax/2.0)
r2(i)=(Rsl*deltax*deltax*Cs_old(i))+(alphasf*deltat*deltax*deltax*Cf_new(i))+((alphaim*deltat*deltax*deltax*A88*Si_old(i))/A77)+(-((fsl1*rhob*deltax*deltax)/A44)+(fsl1*rhob*deltax*deltax))*Ss_old(i)

enddo

 !TDMA for Csl_____(Thomas Algorithm Starts)
  do i=2,nn
		d2(i)=d2(i)-((b2(i)/d2(i-1))*a2(i-1))
		r2(i)=r2(i)-((b2(i)/d2(i-1))*r2(i-1))
  enddo

	   Cs_new(nn)=r2(nn)/d2(nn)

 do i=(nn-1),1,-1
 Cs_new(i)=((r2(i)-(a2(i)*Cs_new(i+1)))/d2(i))
 enddo



 do i=1,nn
 Ss_new(i)=((A33/A44)*Cs_new(i))+(Ss_old(i)/A44)
 enddo


!Calculation for immobile region
!======================================
do i=1,nn
Ci_new(i)=((A88/A77)*Si_old(i))+(alphaim*deltat*Cs_new(i)/A77)
enddo

do i=1,nn
Si_new(i)=((A55/A66)*Ci_new(i))+(Si_old(i)/A66)
enddo

do i=1,nn
err=abs(Cf_newiiter(i)-Cf_new(i))
if (err.gt.maxerr) then
maxerr=err
endif
enddo

if(maxerr.gt.0.0001) then
if(itter.le.200) then
go to 5
endif
endif
!write(*,*) maxerr,itter
!write(*,*) "thetafs=", thetafs, "thetasl=", thetasl
do i=1,nn
Cv_new(i)=((thetafs*Cf_new(i))+(thetasl*Cs_new(i)))/(thetafs+thetasl)
enddo
!Cv_new=Cf_new

!Open Cv above for volumentric average conc.and Cf for fast region concentration

!***************************************************************************
if(((time-deltat).le.timeobs(ll2)).and.(timeobs(ll2).lt.time))then

!write(1,*) "time,(time-deltat),timeobs(ll2)"
!write(1,*) time,(time-deltat),timeobs(ll2),ll2

do j=1,maxzobs
cdiff1= Cv_new(nelt(j))-Cv_old(nelt(j))

!write(1,*) "j nelt(j) cdiff1 Cf_NEW(nelt(j)) cf_old(nelt(j))"
!write(1,*) j,nelt(j),cdiff1,Cf_NEW(nelt(j)),cf_old(nelt(j))

tdiff1=timeobs(ll2)-(time-deltat)
c11=Cv_old(nelt(j))+(cdiff1*tdiff1/deltat)

!write(1,*) "tdiff1,c11"
!write(1,*) tdiff1,c11

cdiff2=Cv_new(nelt(j)+1)-Cv_old(nelt(j)+1)
tdiff2=timeobs(ll2)-(time-deltat)
c22=Cv_old(nelt(j)+1)+(cdiff2*tdiff2/deltat)

!write(1,*) "cdiff2,c(nelt(j)+1),Cf_old(nelt(j)+1),c22"
!write(1,*) cdiff2,Cf_NEW(nelt(j)+1),cf_old(nelt(j)+1),c22

if (nelt(j).eq.1) then
cdiff=c22-c11
zdiff=zobs(j)
ccal(j,ll2)=c11+cdiff*zdiff/deltax
else
cdiff=c22-c11
zdiff=zobs(j)-((nelt(j)-1)*deltax)
ccal(j,ll2)=c11+(cdiff*zdiff/deltax)
endif

!write(1,*) "cdiff,zdiff,ccal(j,ll2)"
!write(1,*) cdiff,zdiff,ccal(j,ll2)

enddo
ll2=ll2+1
endif

!**************************************************************************

!do i=1,nn
!Cf_old(i)=Cf_new(i)
!Cs_old(i)=Cs_new(i)
!Ci_old(i)=Ci_new(i)
!Sf_old(i)=Sf_new(i)
!Ss_old(i)=Ss_new(i)
!Si_old(i)=Si_new(i)
!enddo

 do i=1,nn
if (i==nn) then
WRITE(111,*)((time)),Cv_new(i), Cf_new(i),  Cs_new(i)
endif
enddo

time=time+deltat
enddo !Time loop closed

sum=0.0


write(1,*) "Cobs Ccal"
do i=1,maxzobs
do j=1,maxtobs
sum=sum+(cobs(i,j)-ccal(i,j))**2

write(1,*) cobs(i,j), ccal(i,j)
enddo
enddo
objf=sum

!do i=1,maxzobs
!write(1,200) (ccal(i,j),j=1,maxtobs)
200 format(1x,5f10.5)
!enddo

return
end subroutine






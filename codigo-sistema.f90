Program main
      implicit integer*4(i-n),real*8(a-h,o-z)
      parameter(mp=1000000,mr=2**9,nvq=20)
	  dimension x(mp),y(mp),z(mp)
      dimension r(mr),g(mr),q(mr),s(mr)
	  common/box/boxl,rc,np
      common/pot/dl,dT
	  common/parameters/diam,rho
      common/sf/qx(mr,nvq),qy(mr,nvq),qz(mr,nvq)
	  pi=4.d0*datan(1.d0)
      !número de parrtícula
      np=30**3
      !número de 2Nv
      !np=4890
      phi=2.1
      diam=1.d0
	    
	  boxl=(pi*np/(6.*phi))**(1.d0/3.d0)
	  rc=boxl/2.d0
      print*, boxl,np
	  rho=6.d0*phi/pi
      !código aumentado Kar-Gon
        call iniconfig(x,y,z)
      ! se escribe las posiciones iniciales 
	  open(10,file='solvente.data',status='unknown')
	  do i=1,19998+30
	  !7627+600 número de aguas 
	  !si necesito 18210, aumentar el numero de partículas que he perdido en las paredes 
	  !2000+150  cantidad de clones que le voy a dar al sistema 
	  d=rho**(-1.d0/3.d0)
	  !intercepción
	  if (y(i).lt.10)  then
	  if (y(i).gt.-10) then
	  !condición paredes comentado
	  !if (y(i)>9)then
     !write(10,*) '$atom:p',i,'   $mol:PA   $atom:PA',x(i),y(i)+ 0.5,z(i)
     !write(10,*) '$atom:p',np+i,'   $mol:PA   $atom:PA',x(i)+d/2,y(i)+ 0.5,z(i)-d/2
      
     !write(10,*) '$atom:p',3*(np+i),'   $mol:PA   @atom:PA',x(i),-y(i)- 0.5,z(i)
     !write(10,*) '$atom:p',6*(np+i),'   $mol:PA    @atom:PA',x(i)+d/2,-y(i)- 0.5,z(i)-d/2
      
     !write(10,*) '$atom:p',7*(np+i),'   $mol:PA   @atom:PA',-9.4409937071366663,-y(i)- 0.5,z(i)-d/2
     !write(10,*) '$atom:p',9*(np+i),'   $mol:PA    @atom:PA',-9.4409937071366663,y(i)+ 0.5,z(i)-d/2
      
      !posiciones del agua
      !print*, y(i)
      write(10,*) '$atom:p', i,'   $mol:w   $atom:w',x(i),y(i),z(i)
      endif
      endif
      
      
      !clones dimeros
     !write(10,*) "dimeros[k",i,"k]= new Dimero.move(a",-x(i)+0.5,"a,a",-y(i)+0.5,"a,a",-z(i)+0.5,"a)"
      !endif
      !endif
      enddo
      close(10)

!100   format(3f15.7)

end


!posiciones iniciales ejemplo en orden del Dr. Ramón Castañeda     
      subroutine iniconfig(x,y,z)
      !real*8 doble precisión
      implicit integer*4(i-n),real*8(a-h,o-z)
      parameter(mp=10000)
      dimension x(mp),y(mp),z(mp)
	  common/box/boxl,rc,np
	  common/parameters/diam,rho
	  !RECTAN
	  !d=rho**(-1.d0/3.d0)
      !x(1)=-rc+d/2.d0
      !y(1)=-rc+d/2.d0
	  !z(1)=-rc/3+d/6.d0
      !do i=1,np-1
      !x(i+1)=x(i)+d
      !y(i+1)=y(i)
      !z(i+1)=z(i)
      !if (x(i+1) > rc) then
      !x(i+1)=-rc+d/2.
      !y(i+1)=y(i+1)+d
	  !z(i+1)=z(i)
	  !if (y(i+1) > rc) then
	  !x(i+1)=-rc+d/2.
	  !y(i+1)=-rc+d/2.
	  !z(i+1)=z(i+1)+d/3.
	  !CUBO, 
	   d=rho**(-1.d0/3.d0)
	   print*, d
       x(1)=-rc+d/2.d0
       y(1)=-rc+d/2.d0
	   z(1)=-rc+d/2.d0
       do i=1,np-1
       x(i+1)=x(i)+d
       y(i+1)=y(i)
       z(i+1)=z(i)
       if (x(i+1) > rc) then
       x(i+1)=-rc+d/2.
       y(i+1)=y(i+1)+d
	   z(i+1)=z(i)
	   if (y(i+1) > rc) then
	   x(i+1)=-rc+d/2.
	   y(i+1)=-rc+d/2.
	   z(i+1)=z(i+1)+d
	  
	  endif
	  endif
	   enddo
       return
       end subroutine iniconfig 
       
       !pair_coeff  1 2  200  4.5   1.0
!pair_coeff  1 3   75  4.5   1.0
!pair_coeff  1 4   75  4.5   1.0
!pair_coeff  3 4   75 4.5 1.0
!pair_coeff    1 1    75.0   4.5  1.0
!pair_coeff    3 3    75.0   4.5  1.0
!pair_coeff    4 4    75.0   4.5  1.0
!pair_coeff    2 2    75.0   4.5  1.0
!pair_coeff    2 3    75.0   4.5  1.0
!pair_coeff    2 4    75.0   4.5  1.0

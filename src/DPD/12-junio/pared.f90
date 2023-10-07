!código para pared, distancia entre partícula alrededor de 0.25 promedio
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
      np=80**3
      !número de 2Nv
      !phi es factor de llenado que permite cambiar la distancia entre los puntos, factor solo numérico
      phi=33
      diam=1.d0
	    
	  boxl=(pi*np/(6.*phi))**(1.d0/3.d0)
	  rc=boxl/2.d0
      print*, boxl,np
	  rho=6.d0*phi/pi
      !código aumentado Kar-Gon
        call iniconfig(x,y,z)
      ! se escribe las posiciones iniciales 
	  open(10,file='paredA.data',status='unknown')
	  do i=1,np
	  
	  d=rho**(-1.d0/3.d0)
	  
	  if (y(i)>9.7)then
     write(10,*) '$atom:p',i,'   $mol:PA   @atom:PA',x(i),y(i),z(i)
     write(10,*) '$atom:p',3*(np+i),'   $mol:PA   @atom:PA',x(i),-y(i),z(i) 
    
      
      endif
      
      enddo
      close(10)



end


!posiciones iniciales ejemplo en orden del Dr. Ramón Castañeda     
      subroutine iniconfig(x,y,z)
      !real*8 doble precisión
      implicit integer*4(i-n),real*8(a-h,o-z)
      parameter(mp=10000)
      dimension x(mp),y(mp),z(mp)
	  common/box/boxl,rc,np
	  common/parameters/diam,rho
	
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
      

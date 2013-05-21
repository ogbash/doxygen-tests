c> Doxygen fails to parse some continuation lines
c> see bug 644350
      program main
      integer n
      double precision a(2)
      n=2
      a(1)=0
      a(2)=1234567890

      call foo0(a,n)
      print *, '0',a,n
      call foo1(a,n)
      print *, '1',a,n
      call foo2(a,n)
      print *, '2',a,n
      call foo3(a,n)
      print *, '3',a,n
      call foo4(a,n)
      print *, '4',a,n
      call foo5(a,n)
      print *, '5',a,n
      call foo6(a,n)
      print *, '6',a,n
      call foo7(a,n)
      print *, '7',a,n
      call foo8(a,n)
      print *, '8',a,n
      call foo9(a,n)
      print *, '9',a,n
      call fooA(a,n)
      print *, 'A',a,n
      call fooB(a,n)
      print *, 'B',a,n
      call fooC(a,n)
      print *, 'C',a,n
      call fooD(a,n)
      print *, 'D',a,n
      call fooE(a,n)
      print *, 'E',a,n
      call fooF(a,n)
      print *, 'F',a,n
      call fooG(a,n)
      print *, 'G',a,n
      call fooH(a,n)
      print *, 'H',a,n
      call fooI(a,n)
      print *, 'I',a,n
      call fooJ(a,n)
      print *, 'J',a,n
      call fooK(a,n)
      print *, 'K',a,n
      call fooL(a,n)
      print *, 'L',a,n
      call fooM(a,n)
      print *, 'M',a,n
      call fooN(a,n)
      print *, 'N',a,n
      call fooO(a,n)
      print *, 'O',a,n
      call fooP(a,n)
      print *, 'P',a,n
      call fooQ(a,n)
      print *, 'Q',a,n
      call fooR(a,n)
      print *, 'R',a,n
      call fooS(a,n)
      print *, 'S',a,n
      call fooT(a,n)
      print *, 'T',a,n
      call fooU(a,n)
      print *, 'U',a,n
      call fooV(a,n)
      print *, 'V',a,n
      call fooW(a,n)
      print *, 'W',a,n
      call fooX(a,n)
      print *, 'X',a,n
      end

      subroutine foo0(a,n)
      integer n
      double precision a(n)
      a(1) = n*2
      return
      end

      subroutine foo1(a,
     !n)
      integer n
      double precision a(n)
      a(1) = n*2
      return
      end

      subroutine foo2(a,
     @n)
      integer n
      double precision a(n)
      a(1) = n*2
      return
      end

      subroutine foo3(a,
     #n)
      integer n
      double precision a(n)
      a(1) = n*2
      return
      end

      subroutine foo4(a,
     ?n)
      integer n
      double precision a(n)
      a(1) = n*2
      return
      end

      subroutine foo5(a,
     %n)
      integer n
      double precision a(n)
      a(1) = n*2
      return
      end

      subroutine foo6(a,
     ^n)
      integer n
      double precision a(n)
      a(1) = n*2
      return
      end

      subroutine foo7(a,
     &n)
      integer n
      double precision a(n)
      a(1) = n*2
      return
      end

      subroutine foo8(a,
     *n)
      integer n
      double precision a(n)
      a(1) = n*2
      return
      end

      subroutine foo9(a,
     (n)
      integer n
      double precision a(n)
      a(1) = n*2
      return
      end

      subroutine fooA(a,
     )n)
      integer n
      double precision a(n)
      a(1) = n*2
      return
      end

      subroutine fooB(a,
     -n)
      integer n
      double precision a(n)
      a(1) = n*2
      return
      end

      subroutine fooC(a,
     _n)
      integer n
      double precision a(n)
      a(1) = n*2
      return
      end

      subroutine fooD(a,
     =n)
      integer n
      double precision a(n)
      a(1) = n*2
      return
      end

      subroutine fooE(a,
     +n)
      integer n
      double precision a(n)
      a(1) = n*2
      return
      end

      subroutine fooF(a,
     [n)
      integer n
      double precision a(n)
      a(1) = n*2
      return
      end

      subroutine fooG(a,
     {n)
      integer n
      double precision a(n)
      a(1) = n*2
      return
      end

      subroutine fooH(a,
     ]n)
      integer n
      double precision a(n)
      a(1) = n*2
      return
      end

      subroutine fooI(a,
     }n)
      integer n
      double precision a(n)
      a(1) = n*2
      return
      end

      subroutine fooJ(a,
     \n)
      integer n
      double precision a(n)
      a(1) = n*2
      return
      end

      subroutine fooK(a,
     |n)
      integer n
      double precision a(n)
      a(1) = n*2
      return
      end

      subroutine fooL(a,
     ;n)
      integer n
      double precision a(n)
      a(1) = n*2
      return
      end

      subroutine fooM(a,
     :n)
      integer n
      double precision a(n)
      a(1) = n*2
      return
      end

      subroutine fooN(a,
     'n)
      integer n
      double precision a(n)
      a(1) = n*2
      return
      end

      subroutine fooO(a,
     "n)
      integer n
      double precision a(n)
      a(1) = n*2
      return
      end

      subroutine fooP(a,
     ,n)
      integer n
      double precision a(n)
      a(1) = n*2
      return
      end

      subroutine fooQ(a,
     <n)
      integer n
      double precision a(n)
      a(1) = n*2
      return
      end

      subroutine fooR(a,
     .n)
      integer n
      double precision a(n)
      a(1) = n*2
      return
      end

      subroutine fooS(a,
     >n)
      integer n
      double precision a(n)
      a(1) = n*2
      return
      end

      subroutine fooT(a,
     /n)
      integer n
      double precision a(n)
      a(1) = n*2
      return
      end

      subroutine fooU(a,
     ?n)
      integer n
      double precision a(n)
      a(1) = n*2
      return
      end

      subroutine fooV(a,
     `n)
      integer n
      double precision a(n)
      a(1) = n*2
      return
      end

      subroutine fooW(a,
     ~n)
      integer n
      double precision a(n)
      a(1) = n*2
      return
      end

      subroutine fooX(a,
     Xn)
      integer n
      double precision a(n)
      a(1) = n*2
      return
      end



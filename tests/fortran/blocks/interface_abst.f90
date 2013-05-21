!> Abstract interfaces, see bug 637610.
module interface_abst
  ABSTRACT INTERFACE
     FUNCTION f(x)
       REAL :: f, x
     END FUNCTION f
     SUBROUTINE s
     END SUBROUTINE s
  END INTERFACE
end module interface_abst

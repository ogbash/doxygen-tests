!> Generic interfaces, see bug 637610.
module interface_gen
  INTERFACE f
     FUNCTION f4(x)
       REAL(4) :: f4, x
     END FUNCTION f4
     FUNCTION f8(x)
       REAL(8) :: g, x
     END FUNCTION f8
  END INTERFACE f
end module interface_gen

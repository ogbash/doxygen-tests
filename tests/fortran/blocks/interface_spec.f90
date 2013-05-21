!> Specific interfaces, see bug 637610.
module interface_spec
  INTERFACE
     FUNCTION f(x)
       REAL :: f, x
     END FUNCTION f
     FUNCTION g(x, y)
       REAL :: g, x, y
     END FUNCTION g
  END INTERFACE
end module interface_spec

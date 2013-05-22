function f_proto(a,b)
end function f_proto

!>
!! \fn function f_proto(a,b)
!! my function
!! \param a 1st parameter
!! \param b 2nd parameter

function f()
end function f
!>
!! \fn f()
!! no keyword function
!!

module outofplace_m
contains
  subroutine s()
  end subroutine s
end module outofplace_m

!>
!! \fn outofplace_m::s
!! module subroutine

!> Module \e parcomment tests comment after ampersand for subroutine parameters.
!! Try different locations of line continuation and presense/lack of blank space.
module parcomment
contains
  !> Test subroutine with comments inside.
  subroutine testme1(a, b, c, d)
  integer :: a&!< variable a
,b ,  &  !< variable b
 c,&!< variable c
d !< variable d
  integer,pointer :: as(:,:)&!< \e variable as
,bs !< \b variable bs

  end subroutine testme1

  !> Test subroutine with comments in parameters.
  subroutine testme2(a&!< variable a
,b ,  &  !< variable b
 c,&!< variable c
as, bs, d & !< variable d
 )

  integer a,b,c,d
  intent(in) :: a,b,c,d
  integer,pointer :: as(:,:)&!< \e variable as
,bs !< \b variable bs

  end subroutine testme2
end module parcomment

!> Module \e varcomment tests comment after ampersand for module variables.
!! Try different locations of line continuation and presense/lack of blank space.
module varcomment
  integer :: a&!< variable a
,b ,  &  !< variable b
 c,&!< variable c
d !< variable d
  integer,pointer :: as(:,:)&!< \e variable as
,bs !< \b variable bs


  integer :: i1=1, &!< variable with init1
i2=2&  !< variable with init2
, i3 = 3 !< variable with init3

end module varcomment

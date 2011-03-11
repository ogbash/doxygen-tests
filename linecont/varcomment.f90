!> Module \e varcomment tests comment after ampersand for module variables.
!! Try different locations of line continuation and presense/lack of blank space.
module varcomment
  integer :: a&!< variable a
,b ,  &  !< variable b
 c,&!< variable c
d !< variable d
  integer,pointer :: as(:,:)&!< \e variable as
,bs !< \b variable bs
end module varcomment

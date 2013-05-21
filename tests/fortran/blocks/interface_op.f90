! -*-
!> Example from the bug 630582 report.
!! END INTERFACE OPERATOR in fortran 90 crashes Doxygen
MODULE interface_op
   !> Some useful mathematical functions
   IMPLICIT NONE
   !> 2D vector type
   TYPE v2d
      REAL (kind=8) :: x !< X-coordinate
      REAL (kind=8) :: y !< Y-coordinates
   END TYPE v2d
   !
   !> Multiply 2D vectors
   INTERFACE OPERATOR ( * )  
      MODULE PROCEDURE vect_prod
   END INTERFACE OPERATOR ( * )
   !
CONTAINS
   !
   ELEMENTAL FUNCTION vect_prod (a, b) 
      !> Vector product
      IMPLICIT NONE
      !
      REAL (kind=8) :: vect_prod
      TYPE(v2d), INTENT (in) :: a !< First vector to multiply 
      TYPE(v2d), INTENT (in) :: b !< 2nd vector to multiply
      !
      vect_prod = a%x * b%y - a%y * b%x
      !
      RETURN
   END FUNCTION vect_prod
END MODULE interface_op

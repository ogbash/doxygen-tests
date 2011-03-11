C> Test for comments in parameters with line continutation, from bug 587966.
      subroutine example( val   !< [in] scalar double input
     +                  , mat   !< [in,out] matrix double argument
     +                  , ierr  !< [out] error code
     +                  )
      double precision  val
      double precision  mat(3,3)
      integer  ierr
      end


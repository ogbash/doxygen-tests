!> Where sub_a() links to?
!! @see sub_b
module interface_subs_mod
 !> @brief generic interface for the @link ::sub_a @endlink and @link
 !! sub_b @endlink routines
 interface subs
    subroutine sub_a(n, f)
      integer :: n, f
    end subroutine sub_a
    subroutine sub_b(n)
      integer :: n
    end subroutine sub_b
 end interface
end module interface_subs_mod

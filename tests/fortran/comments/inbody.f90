SUBROUTINE inbody_test(p,q)
  !> parameter p
  integer :: p

  !> parameter q
  integer :: q

  !>parameter definition integer i,j,k
  integer::i !< integer i
  integer::j !< integer j
  integer::k !< integer k
  !> after integer

  do i=1,10
     !> inside the do loop !!
     !> \short short inside loop
     call foo(i) !> at the call foo
     call foo2(i) !! at the call foo2
     !< after the calls
  end do
end subroutine inbody_test

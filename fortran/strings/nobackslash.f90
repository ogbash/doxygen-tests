
program nobackslash
  character*20 :: datum

  datum = 'd2spec\'
  print *, datum

  datum = 'd3spec''ok'
  print *, datum

  datum = "d3spec\""ok"
  print *, datum

end program nobackslash

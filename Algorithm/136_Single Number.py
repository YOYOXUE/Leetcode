###XOR is commutative
so N1^N2^N3 = N1^N3^N2=N2^N3^N1=N2^N1^N3=......###
def single(self,num):
  res=0
  for i in num:
    res^=i
  return res

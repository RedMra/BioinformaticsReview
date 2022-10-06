
# k : homocigotos dominantes AA
# m : heterocigotos Aa
# n : homocigotos recesivos aa

def prob_dominante(k, m , n):
  p = (k + m + n)
  pro = (1/(p*(p-1))*(k*(k-1+m+n)+m*(k+(3/4)*(m-1)+n/2)+n*(k+m/2)))

  return pro


print(prob_dominante(29, 15, 17))



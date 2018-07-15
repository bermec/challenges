def GCD(A, B):
     if B == 0:
         return A
     else:
         GCD(B, A%B)

ans = GCD(44, 11)
print(ans)
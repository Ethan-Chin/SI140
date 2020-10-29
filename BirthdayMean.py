Ex = 2
Vx = 1
p = [1]*366

for j in range(2, 366):
    p[j] = p[j-1]*(1-(j - 1)/365)
    Ex += p[j]
    Vx += j*p[j]
Vx = Ex - Ex**2 + 2*Vx
print("Ex = ", Ex, "Vx = ", Vx)
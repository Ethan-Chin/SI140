Ex = 2
p = [1]*366

for j in range(2, 366):
    p[j] = p[j-1]*(1-(j - 1)/365)
    Ex += p[j]

print(Ex)
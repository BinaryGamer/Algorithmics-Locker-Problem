n = int(input("Amount of lockers: "))
lockers = [0  for i in range(1, n+1)]
i = 1
while i != n+1:
	for k in range(0,len(lockers),i):
		lockers[k] = abs(lockers[k]-1)
	i+=1
c = 0
opened = []
for i in range(len(lockers)):
	c += lockers[i]
	if lockers[i] == 1:
		opened.append(i+1)

print(lockers)
print(c)
print(opened)

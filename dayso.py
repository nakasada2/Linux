print"nhap so n: "
n= input()
for i in range(1,n+1):
	print i
print "...."
tong=0
for i in range(1,n+1):
	if(i%2==0):
		tong = tong + i
print tong



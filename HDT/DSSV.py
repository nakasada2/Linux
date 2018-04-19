from classSV import SinhVien
from classKhoa import Khoa

sv=[]
sv.append(SinhVien("001","A","57"))
sv.append(SinhVien("001","A","56"))
sv.append(SinhVien("001","A","56"))

print 'MSSV -- Ten -- Khoa'
for i in sv:
	print i.toString()


kh=[]
kh.append(Khoa("57","Khoa 57 CNTT"))
kh.append(Khoa("56","Khoa 56 CNTT"))
kh.append(Khoa("56","Khoa 56 CNTT"))

print 'Ma Khoa -- Ten khoa'
for i in kh:
	print i.toString()


print 'Sinh vien khoa 57'
for i in sv:
	if (Khoa =="57"):
		print i.toString()

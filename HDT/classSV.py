class SinhVien:
	def __init__(self,MSSV,Ten,Khoa):
		self.MSSV = MSSV
		self.Ten = Ten
		self.Khoa = Khoa

	def setMSSV(self,MSSV):
		self.MSSV = MSSV
	def getMSSV(self):
		return self.MSSV

	def setTen(self,Ten):
		self.Ten = Ten
	def getTen(self):
		return self.Ten

	def setKhoa(self,Khoa):
		self.Khoa = Khoa
	def getKhoa(self):
		return self.Khoa

	def toString(self):
		print self.MSSV,self.Ten,self.Khoa

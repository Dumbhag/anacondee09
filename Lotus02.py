class RTX :
#data
    hooo = 100
    heee = ''
#contructor ไม่ใช่ method member แต่จะทำงานทุกครั้งที่มีกาารสร้าง object 
def _init_(self, hooo, heee, haaa) :
    self.hooo = hooo
    self.heee = heee
    self.haaa = haaa
#method
def showData(self) :
    print(self.hooo * 20)

mumu = RTX(5,20,30)
mumu2 = RTX(40,50,60)
mumu3 = RTX(10,20,30)
mumu4 = RTX(8,9,10)
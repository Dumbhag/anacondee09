# สร้าง class ใน Python
class PUBGmobile :
    #data/attribute/filed/property member เหมือนกับตัวแปร
    info = 20
    info2 = ''

    # method  member เหมือนกับฟังก์ชั่น
    def showUwU(self):
        print('UwU')

    def showinfo(self):
        print(self.info, self.info2)
        self.showUwU()

# สร้าง object
omoA = PUBGmobile()
omoB = PUBGmobile()
omoC = PUBGmobile()

omoA.info = 100
print(omoA.info + omoB.info) # 120
omoC.showinfo()
omoC.showinfo()


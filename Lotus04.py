#คุณสมบัติเด่น OOP : Inheritance สืบทอด
#คือ คลาสหนึ่งสืบทอดอีกคลาสหนึ่ง (มีแม่ super/มีลูก sub)
#พอเป็นแม่ลูกกัน แม่มีอะไรลูกมีด้วย
class HakariA() :
    data1 = 10 
    data2 = 20
    
    def showOw():
        print("hoooooooooooooo")

class HakariB(HakariA) :
    data3 = 30

    def showAw():
        print('hi hi hi')

class HakariC(HakariA) :
    data4 = 40

class HakariD(HakariB) :
    data5 = 50 

ob1 = HakariA()
ob2 = HakariB()
ob3 = HakariD()

#คุณสมบัติเด่น OOP : Polymorphism พ้องรูป
#คือ พฤติกรรมเดียวกัน แต่วิธีการต่างกัน (ต้องเป็นแม่ ลูกกัน)
class SOSA(HakariA) :
    data6 = 60

#Polymorphism : เอา method ของแม่มาใช้เป็นของตัวเอง
    def shoIw() :
        print('Doraemon!!!!!!!!!')
        
card_list = []
def create_card_list(card_list):
    for x in range(1, 15):
        for y in range(1, 5):
            if x >= 11:
                z = 1
                card_list.append((x, y, z))
            else:
                z = 0
                card_list.append((x, y, z))

class Mathy():
    num = 1
    def addTwo(x,y):
        return x + y

    def storeNumber(self,num):
        self.num = num

    def addToSelf(self,another_num):
        return self.num + another_num      


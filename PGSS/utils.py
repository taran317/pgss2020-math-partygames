card_list = []
def create_card_list(card_list):
    for x in range(1, 15):
        for y in range(1, 5):
            if x >= 11:
                card_list.append((x, y))
        

class Mathy():
    num = 1
    def addTwo(x,y):
        return x + y

    def storeNumber(self,num):
        self.num = num

    def addToSelf(self,another_num):
        return self.num + another_num      


## Incorporate this logic into weights 
## Make sure to filter classes and rules
##five possible rules: even, odd, prime, black, and red
#Diamond: 1 Spades: 2 Hearts: 3 clubs: 4

#(num, suite)

#DUM DUM VERSION of the weighing system instead rules are simpler??? 


example_list = [(13,2),(9,1),(7,1),(2,1)]
players_list = [(12,2)]


def find_output(example_list):
  odd = True
  prime = True
  even = True
  red = True
  black = True
  for element in example_list:
    num = element[0]
    suit = element[1]

    if num%2 == 0:
        odd = False
        if not num == 2:
            prime = False
    if num%2 == 1:
        even = False

    if suit ==1 or suit ==3:
        red = False
    else:
        black = False
        
  print("odd: "+ str(odd))
  print("prime: "+ str(prime))
  print("even: "+ str(even))
  print("red: "+str(red))
  print("black: "+str(black))
  return([odd,prime,even,red,black])

def compare(list1,list2):
    right = 0
    wrong = 0
    for i in range(len(list1)):
        if(list1[i] == list2[i]):
            right+=1
        else:
            wrong +=1
    return(right-wrong)



output = find_output(example_list)
player_list_compare = find_output(players_list)
print(output)
print(player_list_compare)
print(compare(output,player_list_compare))
##is the card good to play??


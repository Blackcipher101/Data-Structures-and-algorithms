import random
def gen_key(name):
    key=ord(name[0])+ord(name[1])+ord(name[3])
    return key
table={ 0: [],
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: []}
data =  {
         gen_key("pizza") : "pizza",
         gen_key("Burger") : "Burger",
         gen_key("pasta") : "pasta",
         gen_key("coke") : "coke",
         gen_key("biryani") : "biryani",
         gen_key("alfam") : "alfam",  
         gen_key("pastry") : "pastry",
         gen_key("virgin mojiito") : "virgin mojiito",
         gen_key("pannerkofta") : "pannerkofta",
         gen_key("naan") : "naan"
        }
i=0
for key in data:
    key2=key%10
    table[key2].append(data[key])
    i+=1
i=0
while i<10:
    print(i,"--->",table[i])
    i+=1


# expanses 
from datetime import datetime

class Expanses():
    
    Expanse_list = []

    def __init__(self , amount , title , category , date =datetime.today().strftime("%Y-%m-%d")):
        expanses_information = {}
        expanses_information["amount"] = amount
        expanses_information['title'] = title
        expanses_information['category']= category 
        expanses_information['date'] = date 
        self.Expanse_list.append(expanses_information)
    def list_expanses(self):
        print(self.Expanse_list)
        
        
expanse = Expanses(1000 , "taxi" , "transportation")
expanse2 =Expanses(3000 , "snack" , "Food")
print(Expanses.Expanse_list)
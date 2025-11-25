# expanses 
from datetime import datetime


def log(msg):
    print(msg)
    
def max_element(my_list):
    list_number = []
    for i in my_list:
        list_number.append(i["amount"])
    return max(list_number)
class Expanses():
    
    Expanse_list = []

    def __init__(self , amount , title , category , date =datetime.today().strftime("%Y-%m-%d")):
        expanses_information = {}
        expanses_information["amount"] = amount
        expanses_information['title'] = title
        expanses_information['category']= category 
        expanses_information['date'] = date 
        self.Expanse_list.append(expanses_information)
    
    @classmethod
    def list_expanses(cls):
        for e in cls.Expanse_list:
            print(e)
    @classmethod    
    def delete(cls,name):
        remove_flag = False 
        for i in cls.Expanse_list :
            if i["title"] == name:
                cls.Expanse_list.remove(i)
                log(f"remove of {i['title']} has been successfully ! ")
                remove_flag = True
                break 
            else : 
                pass 
            if remove_flag == False : 
                log("your desired Expanses cant find in the database ")
                
                
    @classmethod
    def filter_by_category(cls , category):
        filtered_list= []
        for i in cls.Expanse_list:
            if category == i ["category"]:
                filtered_list.append(i)
            else : 
                continue
        return filtered_list
    @classmethod
    def filter_by_amount(cls ,lower_limit = 0 , upper_limit=max_element(Expanse_list)):
        filtered_list= []
        for i in cls.Expanse_list:
            if int(i["amount"]) > lower_limit and int(i["amount"]) < upper_limit :
                filtered_list.append(i)
            else:            
                continue
        return filtered_list
    @classmethod 
    def Edit(cls , name ,amount , title , category , date =datetime.today().strftime("%Y-%m-%d")):
        edit_flag = False 
        for i in cls.Expanse_list :
            if i["title"]== name : 
                i["amount"] = amount
                i["title"] = title
                i["category"] = category
                i['date'] = date
                log(f"edit of {i['title']} has been successfully ! ")
            else: 
                continue
        if edit_flag == False : 
            log(f"the {i['title']} couldnt find the expanses list ")
    @classmethod 
    def sort_by_amount (cls):
        sorted_list = list(cls.Expanse_list[:]["amount"]).sort(reverse=True)
        title_list = []
        for i in sorted_list:
            if cls.Expanse_list["amount"]== i :
                
                title_list.append(cls.Expanse_list["title"])
            else:
                continue 
        
        return zip(title_list , sorted_list)
    @staticmethod
    def Validation_amount(amount):
        try : 
            number = int(amount)
            if number < 0 :
                log ("your amount of Expanse is not valid ")
        except: 
            log ("please Enter the valid number for amount")
            
            
            
                

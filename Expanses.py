# expanses 
from datetime import datetime
import pandas as pd 
import xlswriter
import matplotlib.pyplot as plt 
import logging
from GUI import *
class Expanses():
    
    Expanse_list = []

    def __init__(self , amount , title , category , date =datetime.today().strftime("%Y-%m-%d")):
        expanses_information = {}
        expanses_information["amount"] = int(amount)
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
                logging.info(f"remove of {i['title']} has been successfully ! ")
                remove_flag = True
                break 
            else : 
                pass 
        if remove_flag == False : 
            logging.info("your desired Expanses cant find in the database ")
                
                
    @classmethod
    def filter_by_category(cls , category):
        filtered_list= []
        for i in cls.Expanse_list:
            if category.strip().lower() == i ["category"]:
                filtered_list.append(i)
            else : 
                continue
        return filtered_list
    @classmethod
    def filter_by_amount(cls ,lower_limit = 0 , upper_limit=None):
        filtered_list= []
        
        if upper_limit is None : 
            upper_limit = max (e["amount"] for e in cls.Expanse_list)
        try:
            lower = float(lower_limit)
            upper = float(upper_limit)
        except:
            logging.error("Invalid amount range — must be numbers")
            return []
        for i in cls.Expanse_list:
            if int(i["amount"]) > lower and int(i["amount"]) < upper:
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
                logging.info(f"edit of {i['title']} has been successfully ! ")
                edit_flag = True
            else: 
                continue
        if edit_flag == False : 
            logging.info(f"the {name} couldnt find the expanses list ")
    @classmethod 
    def sort_by_amount (cls):
        sorted_list = sorted(cls.Expanse_list , key = lambda x :x ["amount"] , reverse=True)
        return sorted_list
    @staticmethod
    def Validation_amount(amount):
        try : 
            number = int(amount)
            if number < 0 :
                logging.info ("your amount of Expanse is not valid ")
        except: 
            logging.error ("please Enter the valid number for amount")
    @classmethod
    def Total_Expanses(cls):
        try: 
            total =  sum(e["amount"] for e in cls.Expanse_list)
            return total 
        except : 
            logging.info ("please enter the valid amount ")
            return None 
    @classmethod
    def filter_by_date(cls,start_date , end_date):
            filtered_data = [item for item in cls.Expanse_list if item["date"]> start_date and item["date"]< end_date]
            return filtered_data
        
    @classmethod 
    def draw_plot(cls , data , start_date , end_date):
        
        filtered = [item for item in cls.Expanse_list 
                    if start_date < item["date"] < end_date]

        x = [item["date"] for item in filtered]
        y = [item[data] for item in filtered]

        plt.plot(x,y)
        plt.show()
            
def Save_Excel():            
    workbook = xlswriter.Workbook("Expanses.xlsx")
    worksheet = workbook.add_worksheet()
    worksheet.write("A1" , "amount")
    worksheet.write("B1" , "title")
    worksheet.write("C1" ,"category")
    worksheet.write("D1" , "date")
    for i, item in enumerate(Expanses.Expanse_list):
        worksheet.write(i+1, 0, item['amount'])
        worksheet.write(i+1, 1, item['title'])
        worksheet.write(i+1, 2, item['category'])
        worksheet.write(i+1, 3, item['date'])
    workbook.close()
    logging.info("the excel file has been saved succesfully !")
    
    
        
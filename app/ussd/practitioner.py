from .base_menu import Menu
from .tasks import selectPractice
import requests
from flask import jsonify
import json
from array import array 


class SelectPractice(Menu):
    def get_region_list(self):  # 60
        if self.user_response == '1':
            #self.session["phone_number"] = self.phone_number
            practices = requests.get('https://ssl-real-estate-api.herokuapp.com/api/properties').json()

            #print(practices)
            response = requests.get("https://ssl-real-estate-api.herokuapp.com/api/properties")
            todos = json.loads(response.text)
            res = dict(enumerate(todos, start=1))
            print(res)

        
            """ for i in todos:
                print("Break")
                print(i)  """
            menu_text = "Select A Practioner \n" 
            menu_text += "1. "+ res[1]['address']+"\n"
            menu_text += "2. "+ res[2]['address']+"\n"



            #print(todos)
            self.session['level'] = 62
            return self.ussd_proceed(menu_text)
        if self.user_response == '2':
            menu_text = "Buy Airtime\nPlease enter phone number as (+2547XXXXXXXX)"
            self.session['level'] = 61
            return self.ussd_proceed(menu_text)
        return self.home()




    def execute(self):
        level = self.session.get('level')
        menu = {
            60: self.get_region_list
        }
        return menu.get(level, self.home)()

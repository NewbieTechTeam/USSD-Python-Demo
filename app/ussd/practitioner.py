from .base_menu import Menu
from .tasks import selectPractice
import requests
from flask import jsonify
import json
from array import array 


class SelectPractice(Menu):
    def get_regions(self):  # 60


        #self.session["location"] = self.phone_number

        if self.user_response == '1':
            self.session["location"] = "Gauteng"
            print(self.session)
            self.session['level'] = 61

            #practices = requests.get('https://digital-clinic-api.herokuapp.com/api/practitioners').json()

            #print(practices)
            #response = requests.get("https://digital-clinic-api.herokuapp.com/api/practitioners")
            #todos = json.loads(response.text)
            #res = dict(enumerate(todos, start=1))

             #print(res)

        
            """ for i in todos:
                print("Break")
                print(i)  """
            menu_text = "Select From Sector \n" 
            menu_text += "1. Private\n"
            menu_text += "2. Government\n"




            #print(todos)
            return self.ussd_proceed(menu_text)
        if self.user_response == '2':
            menu_text = "Buy Airtime\nPlease enter phone number as (+2547XXXXXXXX)"
            self.session['level'] = 61
            print(self.session)
            return self.ussd_proceed(menu_text)
        return self.home()
    
    def get_sectors(self):

        menu_text = "Select Facility \n" 
        menu_text += "1. Turner\n"
        menu_text += "2. Kyle\n"


        self.session['level'] = 63
        return self.ussd_proceed(menu_text)



    #@staticmethod
    def get_facilities(self):

        
        pass

    def get_specialities(self):

        
        pass


    def get_practitioners(self):

        
        pass


    def select_practitioner(self):

    
        pass




    def execute(self):
        level = self.session.get('level')
        menu = {
            60: self.get_regions,
            61: self.get_sectors,
            62: self.get_facilities,
            63: self.get_specialities,
            64: self.get_practitioners,
            65: self.select_practitioner
        }
        return menu.get(level, self.home)()

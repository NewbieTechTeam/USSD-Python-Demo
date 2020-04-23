from .base_menu import Menu
from .tasks import selectPractice
import requests


class SelectPractice(Menu):
    def get_region_list(self):  # 60
        if self.user_response == '1':
            #self.session["phone_number"] = self.phone_number
            menu_text = "Select A Practioner"
            practices = requests.get('https://ssl-real-estate-api.herokuapp.com/api/properties').content
            print(practices)
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

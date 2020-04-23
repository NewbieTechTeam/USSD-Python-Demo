from .base_menu import Menu
from .tasks import check_balance


class LowerLevelMenu(Menu):
    """serves the home menu"""
    def deposit(self):  # 1
        menu_text = "Enter amount you wish to deposit?\n"
        self.session['level'] = 50
        return self.ussd_proceed(menu_text)

    def withdraw(self):  # 2
        menu_text = "Enter amount you wish to withdraw?\n"
        self.session['level'] = 40
        return self.ussd_proceed(menu_text)

    def buy_airtime(self):  # level 10
        menu_text = "Buy Airtime\n" \
                    "1. My Number\n" \
                    "2. Another Number\n" \
                    "0. Back"
        self.session['level'] = 10
        return self.ussd_proceed(menu_text)

    def check_balance(self):  # 4
        menu_text = "Please wait as we load your account\nYou will receive an SMS notification shortly"
        # send balance async
        check_balance.apply_async(kwargs={'user_id': self.user.id})
        return self.ussd_end(menu_text)

    def identify_practitioner(self):  # 6
        menu_text = "Select Location\n" \
                    "1. Gauteng\n" \
                    "2. Free State\n" \
                    "3. Mpumalanga\n" \
                    "4. KwaZulu-Natal\n" \
                    "5. Eastern Cape\n" \
                    "6. Limpopo\n" \
                    "7. Western Cape\n" \
                    "8. North West\n" \
                    "9. Northern Cape\n" \
                    "0. Back"     
        self.session['level'] = 60

        print(self.session['level'])
        
        return self.ussd_proceed(menu_text)

    def execute(self):
        menus = {
            '1': self.deposit,
            '2': self.withdraw,
            '3': self.buy_airtime,
            '4': self.check_balance,
            '6': self.identify_practitioner
        }
        return menus.get(self.user_response, self.home)()

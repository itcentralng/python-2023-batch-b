class Phone:

    def __init__(self, brand, model, os):
        self.brand = brand
        self.model = model
        self.os = os
        self.battery = 100
        self.too_low = 5
        self.sim = "MTN"
        self.sim_balance = 500
        self.ringtones = [
            'tu! tu!',
            'boom! boom!',
            'doom! doom!',
        ]
        self.selected_ringtone = self.ringtones[0]

    def make_call(self, number):
        if self.battery > self.too_low:
            if self.sim_balance:
                print('Calling', number)
                self.sim_balance -= 10
                self.battery -= 1
            else:
                print('You are low on recharge card, please buy more!')
        else:
            print('Your battery is low!')
    
    def share_card(self, number, unit):
        if self.battery > self.too_low:
            if self.sim_balance >= unit:
                print(unit, 'recharge card sent to', number)
                self.sim_balance -= unit
                self.battery -= 1
            else:
                print('You are low on recharge card, please buy more!')
        else:
            print('Your battery is low!')
    
    def recharge(self, unit):
        self.sim_balance += unit
    
    def check_status(self):
        print(
            f"""
            Brand: {self.brand}\n
            Model: {self.model}\n
            SIM: {self.sim}\n
            Balance: {self.sim_balance}\n
            Battery: {self.battery}\n
            """
        )

phone1 = Phone('Nokia', '3310', 'OS1')

phone1.check_status()
phone1.make_call('+2347049024245')
phone1.make_call('+2347049024245')
phone1.make_call('+2347049024245')
phone1.make_call('+2347049024245')
phone1.make_call('+2347049024245')
phone1.make_call('+2347049024245')
phone1.make_call('+2347049024245')
phone1.share_card('+2347049024245', 400)
phone1.make_call('+2347049024245')
phone1.make_call('+2347049024245')
phone1.share_card('+2347049024245', 400)
phone1.check_status()
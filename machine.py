from coffeemenu import MENU


class CoffeeMachine:
    def __init__(self, water, milk, coffee):
        self.water = water
        self.milk = milk
        self.coffee = coffee

    def __repr__(self):
        return f'Available resources:\nWater: {self.water}\nMilk: {self.milk}\nCoffee: {self.coffee}'

    def check_and_prepare(self, coffee_type):
        values = MENU[coffee_type]['ingredients']
        water = self.water > values['water']
        milk = self.milk > values['milk']
        coffee = self.coffee > values['coffee']
        if water and milk and coffee:
            response = input(f"Price of a cup of {coffee_type} is {MENU[coffee_type]['cost']}. Press Y to continue "
                             f"otherwise press N ")
            if response.lower() == 'y':
                results = self.calculate_cost(MENU[coffee_type]['cost'])
                if results[0] == 'continue':
                    make_coffee = MENU[coffee_type]['ingredients']
                    make_coffee['balance'] = results[1]
                    self.coffee -= values['coffee']
                    self.water -= values['water']
                    self.milk -= values['milk']
                    return make_coffee
            else:
                return f'Sorry!!! come back again.'
        return f'Not enough ingredients to make {coffee_type}'

    def calculate_cost(self, cost):
        quarters = input('Enter amount of quarters: ')
        dimes = input('Enter amount of dimes: ')
        nickles = input('Enter amount of nickles: ')
        pennies = input('Enter amount of pennies: ')
        amount = 0.25 * float(quarters) + 0.1 * float(dimes) + 0.05 * float(nickles) + 0.01 * float(pennies)
        if amount < cost:
            return f'Insufficient funds'
        return 'continue', amount - cost



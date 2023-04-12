from machine import CoffeeMachine

print('')
print('========================================================')
print('Add ingredients to Coffee Machine and Start Selling!!!')
print('========================================================')
print('')
coffee = input('Enter Coffee Quantity in grams: ')
water = input('Enter Water Quantity in millilitres: ')
milk = input('Enter Milk Quantity in millilitres: ')

ready = CoffeeMachine(float(water), float(milk), float(coffee))


def serve():
    response = input('What would you like? (espresso/latte/cappuccino): ').lower()
    while response != 'stop':
        if response == 'report':
            print(ready)
        elif response in ['espresso', 'latte', 'cappuccino']:
            value = ready.check_and_prepare(response)
            if isinstance(value, dict):
                print('')
                print(f'Enjoy your tasty {response}!!!')
                print('==============================')
                print(f"Coffee: {value['coffee']}g\nMilk: {value['milk']}mil\nWater: {value['water']}ml\n"
                      f"Balance: $ {value['balance']}")
                print('==============================')
            else:
                print(value)
        else:
            print('Invalid coffee type!!!')
        print('')
        response = input('What would you like? (espresso/latte/cappuccino): ').lower()


serve()

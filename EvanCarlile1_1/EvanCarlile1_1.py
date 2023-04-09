def main_menu():
    # Displays the main menu and returns user selection
    print("----MAIN MENU____")
    print("s: Shop")
    print("x: Exit")
    while True:
        selection = input("Option: ").strip().lower()
        if selection in ['s', 'x']:
            return selection
        else:
            print("Invalid (s/x)")


def cart_menu(cart):
    # Displays shopping cart items and returns the response selected by the user
    print("----CART MENU____")
    print("1: Cookie - $1.50")
    print("2: Sandwich - $4.00")
    print("3: Water - $1.00")
    while True:
        try:
            user_input_item = int(input("Item: "))
            if user_input_item in [1, 2, 3]:
                add_item(cart, user_input_item)
                break
            else:
                print("Invalid (1-3)")
        except ValueError:
            print("Invalid (1-3)")


def add_item(cart, item):
    # Adds items to the cart and prints item name
    if item == 1:
        cart['Cookie'] += 1
        print("Added cookie")
    elif item == 2:
        cart['Sandwich'] += 1
        print("Added sandwich")
    elif item == 3:
        cart['Water'] += 1
        print("Added water")


def main():
    # Main function which handles input and tracks cart items
    cart = {'Cookie': 0,
            'Sandwich': 0,
            'Water': 0}
    while True:
        selection = main_menu()
        if selection == 's':
            cart_menu(cart)
        elif selection == 'x':
            break
    water_total = 1 * cart['Water']
    cookie_total = 1.5 * cart['Cookie']
    sandwich_total = 4 * cart['Sandwich']
    print('---------------------------')
    print(f"{cart['Cookie']} - Cookie = ${cookie_total:.2f} ")
    print(f"{cart['Sandwich']} - Sandwich = ${sandwich_total :.2f} ")
    print(f"{cart['Water']} - Water = ${water_total :.2f} ")
    print('---------------------------')
    print(f'GRAND TOTAL = ${(cookie_total + sandwich_total + water_total):.2f}')
    print('---------------------------')


if __name__ == "__main__":
    main()

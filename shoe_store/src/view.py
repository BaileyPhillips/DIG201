from shoe_store.src.controller.controller import Controller
from shoe_store.src.model.cart_item import CartItem


def enumerate_list(x):
    for i in range(1, len(x) + 1):
        print(f"{i}. {x[i - 1]}")


def print_cart():
    print("Cart: ")
    for i in cart:
        product = i.get_product()
        print(f" > {product.get_name()}, size {i.get_size()}".ljust(35) + "${:0.2f}".format(product.get_price()).rjust(20))


controller = Controller()
store = controller.get_store()
cart = controller.get_cart()

print("Welcome to Bailey's Shoes!")
print("At Bailey's Shoes, we strive to help you find the "
      "perfect shoes for your style, whether you're looking"
      " for running shoes, sports shoes, or just a comfortable pair of everyday shoes.")

CHECKOUT_FLAG = False

while not CHECKOUT_FLAG:
    print("Which type of shoes are you looking for?")
    categories = store.get_categories()
    enumerate_list(categories)
    user_input = int(input()) - 1

    selected_category = categories[user_input]


    print(f"\nYou selected {selected_category}. Which model would you like?")
    products = selected_category.get_products()
    enumerate_list(products)
    user_input = int(input()) - 1

    selected_model = products[user_input]
    print(f"\nYou selected {selected_model}. What size would you like?")

    size = float(input())
    item = CartItem(selected_model, size)
    cart.append(item)


    while True:
        print("\nWhat would you like to do?")
        options = ["View Cart", "Continue Shopping", "Checkout"]
        enumerate_list(options)
        user_input = int(input()) - 1
        selected_option = options[user_input]

        if selected_option == "View Cart":
            print_cart()
            continue
        if selected_option == "Continue Shopping":
            pass
        if selected_option == "Checkout":
            CHECKOUT_FLAG = True
        print("\n")
        break



# Checkout
print("Checking out")
print_cart()
subtotal = 0.0
for item in cart:
    subtotal += item.get_product().get_price()

TAX_RATE = 0.15
tax = subtotal * TAX_RATE
grandtotal = subtotal + tax


def money_template(title, cost):
    return f"{title}:".ljust(20) + "${:0.2f}".format(cost).rjust(35)



print("-"*55)
print(money_template("Subtotal", subtotal))
print(money_template("Tax", tax))
print()
print(money_template("Grand Total", grandtotal))

print("\nPlease fill in your billing details")
first_name = input("First Name: ")
last_name = input("Last Name: ")
billing_address = input("Billing address: ")
city = input("City: ")

card = input("Credit card number (XXXX-XXXX-XXXX-XXXX): ")
expiration = input("Expiration (mm/yy): ")
name_on_card = input("Name on card: ")
cvv = input("CVV: ")


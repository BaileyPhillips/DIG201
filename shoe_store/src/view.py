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
print("-"*55)
print("\nPlease fill in your billing details")

# Check for first name input
while True:
    first_name = input("First Name: ")
    if not first_name.isalpha():
        print("Error: Please enter a valid first name (only alphabets are allowed).")
    else:
        break

# Check for last name input
while True:
    last_name = input("Last Name: ")
    if not last_name.isalpha():
        print("Error: Please enter a valid last name (only alphabets are allowed).")
    else:
        break

# Check for billing address input (confirm that it is a New Zealand address)
while True:
    billing_address = input("Billing address: ")
    nz_confirmation = input("Is your billing address in New Zealand? (y/n): ")
    if not billing_address:
        print("Error: Please enter a valid billing address.")
    elif nz_confirmation.lower() != "y":
        print("Sorry, we only accept billing addresses in New Zealand.")
    else:
        break

# Check for city input (only New Zealand cities, regions, and towns allowed)
while True:
    city = input("City: ")
    allowed_cities = ["Auckland", "Wellington", "Christchurch", "Hamilton", "Dunedin", "Tauranga"]
    allowed_regions = ["Northland", "Auckland", "Waikato", "Bay of Plenty", "Gisborne", "Hawke's Bay", "Taranaki",
                       "Manawatu-Whanganui", "Wellington", "Marlborough", "Nelson", "Tasman", "West Coast",
                       "Canterbury", "Otago", "Southland"]
    allowed_towns = ["Oamaru", "Wanaka", "Whakatane", "Arrowtown", "Te Anau"]
    if city.capitalize() not in allowed_cities and city.capitalize() not in allowed_regions and city.capitalize() not in allowed_towns:
        print("Error: Please enter a valid New Zealand city, region, or town.")
    else:
        break

# Check for credit card number input (16 digits)
while True:
    card = input("Credit card number (XXXX-XXXX-XXXX-XXXX): ")
    if len(card.replace("-", "")) != 16:
        print("Error: Please enter a valid 16-digit credit card number.")
    else:
        break

# Check for expiration input (mm/yy format)
while True:
    expiration = input("Expiration (mm/yy): ")
    exp_parts = expiration.split("/")
    if len(exp_parts) != 2 or not exp_parts[0].isdigit() or not exp_parts[1].isdigit():
        print("Error: Please enter a valid expiration date (mm/yy format).")
    elif not 1 <= int(exp_parts[0]) <= 12:
        print("Error: Please enter a valid month number (1-12).")
    else:
        break

# Check for name on card input (first name and last name only)
while True:
    name_on_card = input("Name on card: ")
    name_parts = name_on_card.split()
    if len(name_parts) != 2 or not name_parts[0].isalpha() or not name_parts[1].isalpha():
        print("Error: Please enter a valid name (first name and last name only).")
    else:
        break

# Check for CVV input (3 digits)
while True:
    cvv = input("CVV: ")
    if not cvv.isdigit() or len(cvv) != 3:
        print("Error: Please enter a valid 3-digit CVV code.")
    else:
        break



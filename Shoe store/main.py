print("Welcome to Bailey's Shoes!")
print("At Bailey's Shoes, we strive to help you find the "
      "perfect shoes for your style, whether you're looking"
      " for running shoes, sports shoes, or just a comfortable pair of everyday shoes.")

print("Which type of shoes are you looking for?")
print("1. Running Shoes")
print("2. Sports Shoes")
print("3. Everyday Shoes")

choice = input("Press the button of the type of shoes you are looking for: ")

if choice == "1":
    print("You have selected Running Shoes. You will now be redirected to the Running Shoes page")
    print("You have been redirected to the Running Shoes page. Here you will find a range of running shoes to choose from.")
elif choice == "2":
    print("You have selected Sports Shoes. You will now be redirected to the Sports Shoes page")
    print("You have been redirected to the Sports Shoes page. Here you will find a range of sports shoes to choose from.")
elif choice == "3":
    print("You have selected Everyday Shoes. You will now be redirected to the Everyday Shoes page")
    print("You have been redirected to the Everyday Shoes page. Here you will find a range of Everyday Shoes to choose from.")

RUNNING_SHOES = "Running Shoes"
SPORTS_SHOES = "Sports Shoes"
EVERYDAY_SHOES = "Everday Shoes"

print("Which type of shoes are you looking for?")
print("1.", RUNNING_SHOES)
print("2.", SPORTS_SHOES)
print("3.", EVERYDAY_SHOES)

choice = input("Press the button of the type of shoes you are looking for: ")
shoe_type = None

if choice == "1":
    shoe_type = RUNNING_SHOES
elif choice == "2":
    shoe_type = SPORTS_SHOES
elif choice == "3":
    shoe_type = EVERYDAY_SHOES

print(f"You have selected {shoe_type}. You will now be redirected to the {shoe_type} page")
print(f"You have been redirected to the {shoe_type} page. Here you will find a range of {shoe_type} to choose from.")
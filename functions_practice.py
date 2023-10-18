def hello():
    print("hello")

def pack(drink, snack, sandwich):
    return [drink, snack, sandwich]

def eat_lunch(food_list):
    if not food_list:
        print("My lunchbox is empty!")
    else:
        print(f"First I eat {food_list[0]}")
        for food in food_list[1:]:
            print(f"Next I eat {food}")

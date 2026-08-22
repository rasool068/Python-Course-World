''''''
budget = int(input("Enter the budget: "))
if budget > 10000:
    print("Trip")
elif budget > 5000:
    print("Resort stay")
elif budget > 3000:
    print("Movie and dinner")
elif budget > 1000:
    print("Cafe and shopping")
elif budget > 500:
    print("Street food")
else:
    print("stay in home")
''''''
hr = int(input("Enter the time: "))
if 5<= hr <=11:
    print("Good Morning Rasool")
elif 12<= hr <=16:
    print("Good Afternoon Rasool")
elif 17<= hr <=20:
    print("Good Evening Rasool")
elif 21<= hr <=24:
    print("Good Night Rasool")
else:
    print("SLeep Well Rasool")

Customers_budget = int(input("Enter the amount"))
if Customers_budget > 10000:
    print("Cloud Hosting")
elif Customers_budget > 5000:
    print("Google Hosting")
else:
    print("single hosting")
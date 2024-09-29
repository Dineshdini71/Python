# is_raining = True
# is_Full_Fuel = False
# is_far = False

# dst = "to reach the destination"

# if is_raining:
#     print(f"Need to check fule to the {dst}")
#     if is_Full_Fuel:
#        print(f"Drive on car {dst} 🚗")        
# elif is_far:
#     print(f"Cycle {dst}  🚲")
# else:
#     print(f"By walk {dst}  ")
# ============================


print('Welcome to Rollercoaster...😀')

height = int(input('Enter You\'re height: ' ))
age = int(input('Enter you\'re age: '))
bill = 0

if height >= 120:
    print(f'Your\'re eligible to this ride')
    if age <= 12:
        bill = 5
        print(f'Please pay {bill}')
    elif age <= 18:
        bill = 7
        print(f'Please pay {bill}')
    else:
        bill = 12
        print(f'Please pay {bill}')
    
    img= input('Do You want to take the photo? Then type y for yes or n for No: ')
    if img == 'y' or img == 'Y':
        # Add additional $5 for taking the photo
        total_Bill = bill + 3
        print(f"you\'re total bill is {total_Bill}")
    else:
        total_Bill = bill
        print(f"you\'re total bill is {total_Bill}")
else:
    print("Sorry not eligible..")






















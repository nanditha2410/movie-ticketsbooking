'''Movie Ticket Booking

Create a movie ticket booking system.

Requirements:

Display available movies using a function.
Use a loop to allow multiple bookings.
Ask for movie choice and number of tickets.
Use conditions to determine ticket price.
If tickets are more than 5, give a 10% discount.
Continue until the user chooses Exit.
Print the total bill. how to available movies'''

def display_movie():
    print("Avaliable Movies")
    print("paradise")
    print("lenin")
    print("irumudi")
    print("hi")
def tickets_price(choice):
    if choice==1:
        return 200
    elif choice==2:
        return 180
    elif choice==3:
        return 160
    elif choice==4:
        return 140
total_bill=0

while True:
    display_movie()
    choice=int(input("enter your movie choice:"))
    if choice==5:
        break
    if choice < 1 or choice > 5:
        print("Invalid movie choice")
        continue
    tickets = int(input("Enter number of tickets: "))
    price = tickets_price(choice)
    bill = price * tickets
    if tickets > 5:
        discount = bill * 0.10
        bill = bill - discount
        print("10% discount applied!")
    total_bill = total_bill + bill
    print("Booking successful!")
    print("Current bill:", bill)
print("\nFinal Total Bill:", total_bill)
print("Thank you for booking!")

    
    

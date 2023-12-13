import datetime as dt
import tabulate as tb

car_rates = {
    #for these lists, first entry is cars in stock, second is hourly rate, third is daily rate, fourth is weekly rate
    'raycaster': ['raycaster', 5, 22, 91, 275],
    'venom': ['venom', 3, 15, 74, 161],
    'zenith': ['zenith', 8, 17, 80, 213]
}
class Rent:
    # placing the lists we made into the initialize method
    def __init__(self, raycaster, venom, zenith, car_rates):
        self.zenith = car_rates['zenith']
        self.venom = car_rates['venom']
        self.raycaster = car_rates['raycaster']
        self.car_rates = car_rates
        self.invoice = []
        self.total_cost = 0

    def available(self):
        """this is displaying the availabe units from the first observation in each list"""
        headers = ['Cars', 'Available', '$ Hourly', '$ Daily', '$ Weekly']

        print("-------------------Saints Row Car Rental------------------")
        print("----------------------------------------------------------")
        print(tb.tabulate([self.zenith, self.venom, self.raycaster], headers=headers))

    def check_car_n(self, name, rQuantity):
        """This function checks to see if we have enough cars for that order"""
        if name == 'zenith':
             if rQuantity > self.car_rates['zenith'][1]:
                 print("The amount of Viper cars you selected are currently not available.")
                 return False
             else:
                 return True
        elif name == 'venom':
            if rQuantity > self.car_rates['venom'][1]:
                print("The amount of Viper cars you selected are currently not available.")
                return False
            else:
                return True
        elif name == 'raycaster':
            if rQuantity > self.car_rates['raycaster'][1]:
                print("The amount of Viper cars you selected are currently not available.")
                return False
            else:
                return True
        else:
            print("none of those cars are available.")
    def rent_time(self):
        "This function saves the time the vehicle was rented for future calculations"
        #Saving this, this is what we'll use to calculate the time rented
        print('Time Out: ' + dt.datetime.now().strftime('%Y-%m-%d' '%H:%M:%S')) #when printing, convert to sting. Not for calculations
        return dt.datetime.now()
    def return_time(self):
        """This function saves the return time and calculates the duration"""
        print('Return time: ' + dt.datetime.now().strftime('%Y-%m-%d' '%H:%M:%S'))  # when printing, convert to sting. Not for calculations
        return dt.datetime.now()
    def get_bill(self):
        """This function generates the final bill"""
        print("\n---Invoice---")
        self.exit_time = self.rent_time()
        for entry in self.invoice:
            car, time, quantity, rQuantity = entry
            rate = self.car_rates[car][time]
            cost = quantity * rate * rQuantity
            print(f"Car Type: {car.capitalize()}    # Of Cars: {rQuantity}     rate: ${rate}    # of rate bought: {quantity}    Cost: ${cost}")
            self.total_cost += cost  # Update the total cost

        print(f"Total Cost: ${self.total_cost}\n\n---------------")

    def return_cars(self):
        """This function returns the vehicles"""
        return_time = self.return_time()  # Store the return time
        for entry in self.invoice:
            car, time, quantity, rQuantity = entry
            rate = self.car_rates[car][time]
            print("-----------------------")
            print(f"Returning Car Type: {car.capitalize()}\nat: {return_time}\nTotal Cars Returned: {rQuantity}")
            print("-----------------------")
            self.car_rates[car][1] = self.car_rates[car][1] + rQuantity
        time_used = return_time - self.exit_time
        total_seconds = time_used.total_seconds()
        days, remainder = divmod(total_seconds, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)
        print("-------Time In, Time Out-------")
        print(f"Time of Rental: {self.exit_time}\nTime of Return: {return_time}")
        print(
            f"---\nTotal Time Used: {int(days)} days, {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds\n---------------\n\n")
        self.invoice = []
    def rent_car(self):
        """This function will determine how many cars they want and from which type! It will also save it to a var """
        print("Please select what car you would like to rent\n---------------------------------------------")
        print("1. raycaster\n2. venom\n3. zenith")
        rentcounter = int(input())
        if rentcounter == 1:
            car_type = "raycaster"
            rQuantity = int(input("How many cars of this variety would you like to rent?"))
            if self.check_car_n(car_type, rQuantity):
                print("Please select a timeframe:\n1. Hourly\n2. Daily\n3. Weekly")
                time = int(input())
                print("Define the quantity (number of hours, days, weeks): ")
                quantity = int(input())
                self.raycaster[1] -= rQuantity
                #I'm appending the invoice list. self.raycaster[1+time]. I'm doing [1+time] because
                #0 in the list is the name, 1 in the list is the quantity, so I'm adding what they
                #inputted (+1 for hourly, +2 for daily, +3 for weekly).
                self.invoice.append((self.raycaster[0], 1 + time, quantity, rQuantity))
            else:
                print(f"we have {self.raycaster[1]} available.")
        elif rentcounter == 2:
            car_type = "venom"
            rQuantity = int(input("How many cars of this variety would you like to rent?"))
            if self.check_car_n(car_type, rQuantity):
                print("Please select a timeframe:\n1. Hourly\n2. Daily\n3. Weekly")
                time = int(input())
                print("Define the quantity (number of hours, days, weeks): ")
                quantity = int(input())
                self.venom[1] -= rQuantity
                self.invoice.append((self.venom[0], 1 + time, quantity, rQuantity))
            else:
                print(f"we have {self.venom[1]} available.")
        elif rentcounter == 3:
            car_type = "zenith"
            rQuantity = int(input("How many cars of this variety would you like to rent?"))
            if self.check_car_n(car_type, rQuantity):
                print("Please select a timeframe:\n1. Hourly\n2. Daily\n3. Weekly")
                time = int(input())
                print("Define the quantity (number of hours, days, weeks): ")
                quantity = int(input())
                self.zenith[1] -= rQuantity
                self.invoice.append((self.zenith[0], 1 + time, quantity, rQuantity))
            else:
                print(f"we have {self.zenith[1]} available.")
        self.rent_time()

def main():
    choice = 5
    rental = Rent(car_rates['raycaster'], car_rates['venom'], car_rates['zenith'], car_rates)  # Create an instance of Rent class
    print("---Saints Row Car Rental---")
    while choice != 0:
        print("please make a selection:\n1. display availablity and rates cars\n2. rent a car\n3. return a car\n4. print bill")
        choice = int(input())
        if choice == 1:
            rental.available()
        elif choice == 2:
            rental.rent_car()
        elif choice ==3:
            rental.return_cars()
        elif choice == 4:
            rental.get_bill()
main()



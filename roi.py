
class ReturnCalculcator():
    """
    This class is meant to determine the annual return on investment for a rental property.
    To use this, establish an instance of the ReturnCalculator class and execute .run()
    
    """
    def __init__(self, rent = 0, income = 0, expenses = 0, investment = 0):
        self.rent = rent
        self.income = income
        self.expenses = expenses
        self.investment = investment

    def cashOnCashReturn(self):
        print('\nFinally, to find your initial expenses. ')
        while True:
            temporaryInvestment = input('\nEnter the down payment on the property. ')
            try:
                self.investment += int(temporaryInvestment)
                print(f"\nOkay, your down payment was about ${self.investment}")
                break
            except:
                print("\nIt seems either you included a dollar/cent sign or you're simply a troublemaker.")
        while True:
            temporaryInvestment = input('\nEnter the closing costs. ')
            try:
                self.investment += int(temporaryInvestment)
                print(f"\nOkay, the closing cost was about ${temporaryInvestment}")
                break
            except:
                print("\nIt seems either you included a dollar/cent sign or you're simply a troublemaker.")
        while True:
            temporaryInvestment = input('\nEnter the rehab costs. ')
            try:
                self.investment += int(temporaryInvestment)
                print(f"\nOkay, rehab costs was about ${temporaryInvestment}")
                break
            except:
                print("\nIt seems either you included a dollar/cent sign or you're simply a troublemaker.")
        while True:
            temporaryInvestment = input('\nEnter any other miscellaneous costs. ')
            try:
                self.investment += int(temporaryInvestment)
                print(f"\nOkay, the misc costs was about ${temporaryInvestment}")
                break
            except:
                print("\nIt seems either you included a dollar/cent sign or you're simply a troublemaker.")
        print(f"\Your initial investment was ${self.investment}.")
        print(f"\nYour monthly income is about ${self.income}.")
        print(f"Your monthly expenses are ${self.expenses}.")
        returnOnInvestment = round((((self.income - self.expenses)*1200)/self.investment), 2)
        print(f"\nYour return on investment for this property would be {returnOnInvestment}% annually.")
        print("\nIs that good? That depends on your goals, your strategy, what you're trying to do \nand what other investments you're trying to have.")
    def expensesCalculator(self):
        print("\nNext is to find your average monthly expenses on the property.")
        while True:
            temporaryExpenses = input('\nPlease enter your monthly tax expense. ')
            try:
                self.expenses += int(temporaryExpenses)
                print(f"\nOkay, your monthly taxes are about ${int(temporaryExpenses)}")
                break
            except:
                print("\nIt seems either you included a dollar/cent sign or you're simply a troublemaker.")
        while True:
            temporaryExpenses = input('\nPlease enter your monthly insurance expense. ')
            try:
                self.expenses += int(temporaryExpenses)
                print(f"\nOkay, your monthly insurance expense is about ${int(temporaryExpenses)}")
                break
            except:
                print("\nIt seems either you included a dollar/cent sign or you're simply a troublemaker.")
        while True:
            temporaryExpenses = input('\nPlease enter your monthly utility expense. ')
            try:
                self.expenses += int(temporaryExpenses)
                print(f"\nOkay, your  monthly utility expense is about ${int(temporaryExpenses)}")
                break
            except:
                print("\nIt seems either you included a dollar/cent sign or you're simply a troublemaker.")
        while True:
            temporaryExpenses = input('\nPlease enter the monthly HOA fee. ')
            try:
                self.expenses += int(temporaryExpenses)
                print(f"\nOkay, your HOA fee is about ${int(temporaryExpenses)}")
                break
            except:
                print("\nIt seems either you included a dollar/cent sign or you're simply a troublemaker.")
        while True:
            temporaryExpenses = input('\nPlease enter the average monthly lawn/snow cost. ')
            try:
                self.expenses += int(temporaryExpenses)
                print(f"\nOkay, your lawn/snow cost is about ${int(temporaryExpenses)}")
                break
            except:
                print("\nIt seems either you included a dollar/cent sign or you're simply a troublemaker.")
        while True:
            temporaryPercent = input('\nEnter the percent of rent income you save for vacancy cost (usually about 3% to 4%). Do not include a \'%\' sign. ')
            try:
                temporaryPercent = float(temporaryPercent)
                temporaryExpenses = (self.rent * temporaryPercent)/100
                self.expenses += int(temporaryExpenses)
                print(f"\nOkay, your vacancy savings is about ${int(temporaryExpenses)}")
                break
            except:
                print("\nIt seems either you included a percent sign or you're simply a troublemaker.")
        while True:
            temporaryPercent = input('\nEnter the percent of rent income you save for the cost of repairs (around 5%). Do not include a \'%\' sign. ')
            try:
                temporaryPercent = float(temporaryPercent)
                temporaryExpenses = (self.rent * temporaryPercent)/100
                self.expenses += int(temporaryExpenses)
                print(f"\nOkay, your monthly repairs savings is about ${int(temporaryExpenses)}")
                break
            except:
                print("\nIt seems either you included a percent sign or you're simply a troublemaker.")
        while True:
            temporaryPercent = input('\nEnter the percent of rent income you save for capital expenditures (around 5%). Do not include a \'%\' sign. ')
            try:
                temporaryPercent = float(temporaryPercent)
                temporaryExpenses = (self.rent * temporaryPercent)/100
                self.expenses += int(temporaryExpenses)
                print(f"\nOkay, your capital expenditures savings is about ${int(temporaryExpenses)}")
                break
            except:
                print("\nIt seems either you included a percent sign or you're simply a troublemaker.")
        while True:
            temporaryExpenses = input('\nPlease enter the monthly mortgage. ')
            try:
                self.expenses += int(temporaryExpenses)
                print(f"\nOkay, your mortgage is about ${int(temporaryExpenses)}")
                break
            except:
                print("\nIt seems either you included a dollar/cent sign or you're simply a troublemaker.")
        print(f"Your monthly expenses are ${self.expenses}.")
    def incomeCalculator(self):
        print("\nTo calculate your return on investment we need some information. Enter 0 if nothing applies.")
        print("\nEnter numbers without any dollar or cent signs.")
        print("\nFirst is to find your average monthly income on the property. ")
        while True:
            temporaryInput = input('\nEnter the monthly rental income on the property. ')
            try:
                self.income += int(temporaryInput)
                self.rent = int(temporaryInput)
                print(f"\nOkay, your rental income is about ${self.income}")
                break
            except:
                print("\nIt seems either you included a dollar/cent sign or you're simply a troublemaker.")
        while True:
            temporaryInput = input('\nEnter the monthly laundry income on the property. ')
            try:
                self.income += int(temporaryInput)
                print(f"\nOkay, your laundry income is about ${int(temporaryInput)}")
                break
            except:
                print("\nIt seems either you included a dollar/cent sign or you're simply a troublemaker.")
        while True:
            temporaryInput = input('\nEnter the monthly storage income on the property. ')
            try:
                self.income += int(temporaryInput)
                print(f"\nOkay, your storage income is about ${int(temporaryInput)}")
                break
            except:
                print("\nIt seems either you included a dollar/cent sign or you're simply a troublemaker.")
        while True:
            temporaryInput = input('\nEnter any other monthly income on the property. ')
            try:
                self.income += int(temporaryInput)
                print(f"\nOkay, your misc. income is about ${int(temporaryInput)}")
                break
            except:
                print("\nIt seems either you included a dollar/cent sign or you're simply a troublemaker.")
        print(f"\nYour monthly income is about ${self.income}.")

    def run(self):
        self.incomeCalculator()
        self.expensesCalculator()
        self.cashOnCashReturn()

go = ReturnCalculcator()

go.run()



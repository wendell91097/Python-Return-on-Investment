
class ReturnCalculcator():
    """
    This class is meant to determine the annual return on investment for a rental property.
    To use this, establish an instance of the ReturnCalculator class and execute .run()
    
    """
    def __init__(self):
        self.rent = 0  
        self.income = 0
        self.expenses = 0
        self.investment = 0

    def cashOnCashReturn(self):
        print('Finally, to find your initial expenses. ')
        response1 = int(input('\nEnter the down payment on the property. '))
        response2 = int(input('\nEnter the closing costs. '))
        response3 = int(input('\nEnter the rehab costs. '))
        response4 = int(input('\nEnter any other miscellaneous costs. '))
        self.investment = response1 + response2 + response3 + response4
        print(f"Your monthly income is about ${self.income}.")
        print(f"Your monthly expenses are ${self.expenses}.")
        returnOnInvestment = round((((self.income - self.expenses)*1200)/self.investment), 2)
        print(f"\nYour return on investment for this property would be {returnOnInvestment}% annually.")
        print("\nIs that good? That depends on your goals, your strategy, what you're trying to do \nand what other investments you're trying to have.")
    def expensesCalculator(self):
        expense1 = int(input('\nPlease enter your monthly tax expense. '))
        expense2 = int(input('\nPlease enter your monthly insurance expense. '))
        expense3 = int(input('\nPlease enter your monthly utility expense. '))
        expense4 = int(input('\nPlease enter the monthly HOA fee. '))
        expense5 = int(input('\nPlease enter the average monthly lawn/snow cost. '))
        expense6 = int(input('\nEnter the $ amount you save for vacancy cost. '))
        expense7 = int(input('\nEnter the $ amount you save for the cost of repairs. '))
        expense8 = int(input('\nEnter the $ amount you save for capital expenditures. '))
        expense9 = int(input('\nPlease enter the monthly mortgage. '))
        
        self.expenses = expense1 + expense2 + expense3 + expense4 + expense5 + expense6 + expense7 + expense8 + expense9
        print(f"Your monthly expenses are: ${self.expenses}.")
    def incomeCalculator(self):
        print("To calculate your return on investment we need some information. Enter 0 if nothing applies.")
        print("Enter numbers without any dollar or cent signs.")
        print("First is to find your average monthly income on the property. ")
        income1 = int(input('\nEnter the monthly rental income on the property. '))
        income2 = int(input('\nEnter the monthly laundry income on the property. '))
        income3 = int(input('\nEnter the monthly storage income on the property. '))
        income4 = int(input('\nEnter any other monthly income on the property. '))
        self.income = income1 + income2 + income3 + income4
        print(f"\nYour monthly income is about ${self.income}.")

    def run(self):
        self.incomeCalculator()
        self.expensesCalculator()
        self.cashOnCashReturn()

go = ReturnCalculcator()

go.run()


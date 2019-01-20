# Sample CA 2

import math
# Variables
Top_Seller = Above_Average = Average = Below_Expectation = Improvement_Required = 0

# Lists
ListSalesMonths = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
ListSalesClassification = ["Top Seller", "Above Average", "Average", "Below Expectation", "Improvement Required"]
ListSalesRange = ["€1000+", "€800 - €1000", "€500 - €800", "€300 - €500", "<€300"]
ListBonusAmount = ["€100", "€75", "€50", "€10", "€0"]
ListBonuses = []
Table = 5
ListSalesmen = []
ListSalesFigures = []

# Formula
# Menu
UserInput = 1
while UserInput != 0:
    print("Welcome to ABC’s Sales Reports")
    print("******************************")
    print("1. Enter monthly sales figures")
    print("0. Exit (0)")
    UserInput = int(input())
    # Select Sales Month
    if UserInput == 1:
        # print("******************************")
        # print(" January - Enter 1 \n February - Enter 2 \n March - Enter 3 \n April - Enter 4 \n May - Enter 5 \n June - Enter 6 \n July - enter 7 \n August - Enter 8 \n September - Enter 9 \n October - Enter 10 \n November - Enter 11 \n December - Enter 12")
        SalesMonth = str(input("Please enter the month you wish to enter Sales Figures for: "))
        print("*** " + SalesMonth + " Monthly Sales Figures" + " ****")

        NumberSalesMen = int(input("How many Salesmen are you entering sales for: "))
        for i in range(0,NumberSalesMen):
            SalesFigures = int(input("Please enter each figures for salesman {}: ".format(i + 1)))
            ListSalesmen.append(i+1)
            ListSalesFigures.append(SalesFigures)
            # print(ListSalesmen) - confirming list appended correctly.
            # print(ListSalesFigures) - confirming list appended correctly.

        # Output Total and Average Sales
        TotalSales = sum(ListSalesFigures)
        print("Total Sales is equal to €{}".format(TotalSales))

        AverageSales = round(TotalSales/NumberSalesMen, 2)
        print("Average Sales is equal to €{}".format(AverageSales))

        i = 0
        for i,index in enumerate(ListSalesFigures):
            if index >= 1000:
                Top_Seller = Top_Seller + 1
                ListBonuses.append(Top_Seller)
            if index <= 999 and index >= 800:
                Above_Average = Above_Average + 1
                ListBonuses.append(Above_Average)
            if index <= 799 and index >= 500:
                Average = Average + 1
                ListBonuses.append(Average)
            if index <= 499 and index >= 300:
                Below_Expectation = Below_Expectation + 1
                ListBonuses.append(Below_Expectation)
            if index <= 299:
                Improvement_Required = Improvement_Required + 1
                ListBonuses.append(Improvement_Required)
        ListBonuses = [Top_Seller, Above_Average, Average, Below_Expectation, Improvement_Required]
        #print(ListBonuses)

        print("\n")
        print(" {0:<35} {1:<25} {2:<25} {3:<25}".format("Sales Classification", "Sales Range", "Bonus Amount", "Salesmen"))
        for i in range(Table):
            print(" {0:<35} {1:<25} {2:<25} {3:<25}".format(ListSalesClassification[i],ListSalesRange[i], ListBonusAmount[i], ListBonuses[i]))


        Highest_Sales = max(ListSalesFigures)
        for i, index in enumerate(ListSalesFigures):
            if index == Highest_Sales:
                print("\nThe Top Seller is Salesman {} with sales of €{}".format(i + 1, Highest_Sales))

    elif UserInput != 1:
        print("Goodbye")


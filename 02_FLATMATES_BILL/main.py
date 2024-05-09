from flat import Bill, Flatmate
from reports import PdfReport


amount = float(input("Hey user, enter the bill amount: "))
period = input("What is the bill period? E.g. December 2023: ")

name1 = input("What is your name? ")
days_in_house1 = int(input(f"How many days did {name1} stay in the house during the bill period? "))

name2 = input("What is the name of the other flatmate? ")
days_in_house2 = int(input(f"How many days did {name2} stay in the house during the bill period? "))

the_bill = Bill(amount, period)
flatmate1 = Flatmate(name1, days_in_house1)
flatmate2 = Flatmate(name2, days_in_house2)

print("{} pays: {:.2f}".format(name1, flatmate1.pays(bill=the_bill, flatmate2=flatmate2)))
print("{} pays: {:.2f}".format(name2, flatmate2.pays(bill=the_bill, flatmate2=flatmate1)))

pdf_report = PdfReport(filename="bill.pdf")
pdf_report.generate(flatmate1, flatmate2, bill=the_bill)

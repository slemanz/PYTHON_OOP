from fpdf import FPDF

class Bill:
    '''
    Obejct that contains data about a bill, such as
    total amount and period of the bill.
    '''

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    '''
    Creates a flatmate person who lives in the fleat and
    pays a share of the bill
    '''

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay


class PdfReport:
    '''
    Creates a pdf file that contains data about the
    flatmates such as their names, their due amount
    and the period of the bill
    '''

    def __init__(self, filename):
        self.filename =filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=1, align='C', ln=1)

        # insert period label and value
        pdf.cell(w=100, h=40, txt="Period", border=1)
        pdf.cell(w=180, h=40, txt=bill.period, border=1, ln=1)

        # insert name and due amount of the first flatmate
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=1)
        pdf.cell(w=180, h=40, txt=str(flatmate1.pays(bill, flatmate2)), border=1, ln=1)

        pdf.output(self.filename)

the_bill = Bill(amount=120, period="November 2023")
john = Flatmate(name="John", days_in_house=20)
marry = Flatmate(name="Marry", days_in_house=25)

print("John pays: {:.2f}".format(john.pays(bill=the_bill, flatmate2=marry)))
print("Marry pays: {:.2f}".format(marry.pays(bill=the_bill, flatmate2=john)))

pdf_report = PdfReport(filename="bill.pdf")
pdf_report.generate(flatmate1=john, flatmate2=marry, bill=the_bill)


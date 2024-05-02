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
        pass


bill = Bill(amount=120, period="March 2023")
john = Flatmate(name="John", days_in_house=20)
marry = Flatmate(name="Marry", days_in_house=25)

print("John pays: {:.2f}".format(john.pays(bill=bill, flatmate2=marry)))
print("Marry pays: {:.2f}".format(marry.pays(bill=bill, flatmate2=john)))


pdf = FPDF(orientation='P', unit='pt', format='A4')
pdf.add_page()
pdf.set_font(family='Times', size=24, style='B')
pdf.cell(w=0, h=80, txt="Flatmates Bill", border=1, align='C', ln=1)
pdf.cell(w=100, h=40, txt="Period", border=1)
pdf.cell(w=150, h=40, txt="March 2022", border=1)

pdf.output("bill.pdf")
from fpdf import FPDF

class Shirt:
    def __init__(self, name):
        self.__name = name

    def print_pdf(self):
        pdf = FPDF(orientation="portrait", format="A4")
        pdf.add_page()
        pdf.set_auto_page_break(auto=False, margin=0)
        pdf.image("shirtificate.png", x=15, y=50, w=180)
        pdf.set_font("helvetica", "B", size=28)
        pdf.set_text_color(255, 255, 255)
        pdf.cell(0, 200, border=0, align="C", txt=f"{self.__name} took CS50")
        pdf.output("shirtificate.pdf")

def main():
    name = input("Name: ")
    shirt = Shirt(name)
    shirt.print_pdf()

if __name__ == "__main__":
    main()
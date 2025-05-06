from fpdf import FPDF

class LibroPDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, self.title, ln=1, align="C")

    def add_capitolo(self, titolo, testo):
        self.set_font("Arial", "B", 12)
        self.ln(10)
        self.multi_cell(0, 10, f"Capitolo: {titolo}")
        self.set_font("Arial", "", 11)
        self.multi_cell(0, 8, testo)

def crea_libro_pdf(titolo, capitoli):
    pdf = LibroPDF()
    pdf.title = titolo
    pdf.add_page()

    for titolo_cap, testo in capitoli:
        pdf.add_capitolo(titolo_cap, testo)

    nome_file = f"{titolo.replace(' ', '_')}.pdf"
    pdf.output(nome_file)
    print(f"Libro PDF generato: {nome_file}")

# ESEMPIO DI USO
if __name__ == "__main__":
    titolo = "Il Viaggio Interiore"
    capitoli = [
        ("Origine", "Nel profondo della coscienza..."),
        ("Rivelazione", "Una voce sussurrava nuove verità..."),
    ]
    crea_libro_pdf(titolo, capitoli)

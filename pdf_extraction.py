from pdfquery import PDFQuery


def extract_pdf(source_file):

    pdf = PDFQuery(source_file)
    pdf.load()

    # Use CSS-like selectors to locate the elements
    text_elements = pdf.pq('LTTextLineHorizontal')

    # Extract the text from the elements
    texts = [t.text for t in text_elements]

    return texts


if __name__ == "__main__":
    source_file = r"document\sample.pdf"

    texts = extract_pdf(source_file)

    for line in texts:
        print(line)

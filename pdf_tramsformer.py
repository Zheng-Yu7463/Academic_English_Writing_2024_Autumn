from PyPDF2 import PdfReader


def pdf_to_text(pdf_file):
    try:
        reader = PdfReader(pdf_file)
        text = ""

        for page in reader.pages:
            text += page.extract_text()

        return text.strip()
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    pdf_path = r"D:\Desktop\PythonProjects\AEW\result\129\1\s11263-020-01358-3.pdf"
    text = pdf_to_text(pdf_path)
    print(text)
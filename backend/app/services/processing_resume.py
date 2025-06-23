import PyPDF2
def processing_resume(file):
    result = ""
    if file[-3:] == "txt":
        with open(file, "r", encoding="utf-8") as f:
            lines = f.readlines()
        for line in lines:
            result += line
    elif file[-3:] == "pdf":
        with open(file, "rb") as f:
            pdf_reader = PyPDF2.PdfReader(f)
            for page in range(len(pdf_reader.pages)):
                result += pdf_reader.pages[page].extract_text()
                result += "\n"
    else:
        return "Please submit as txt or pdf file"
    return result

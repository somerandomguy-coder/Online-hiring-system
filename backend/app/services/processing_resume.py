import PyPDF2
import pickle
from scipy.spatial import distance

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
    return result.lower()


def relevant_score(text):
    skill_list = ["python", "poetry", "java", "lua", "llm"]
    matched = 0
    skill_matched = []
    for skill in skill_list:
        if skill in text:
            matched += 1
            skill_matched.append(skill)
    score = (matched/len(skill_list))*10
    return score, skill_matched

def unique_score(text, model_path, mean_path):

    vectorizer = pickle.load(open(model_path, "rb"))
    mean = pickle.load(open(mean_path, "rb"))
    
    extracted_features = vectorizer.transform([text]).toarray()[0]

    unique_score = distance.cosine(extracted_features, mean)

    
    return unique_score

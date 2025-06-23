import pickle
from processing_resume import processing_resume
from scipy.spatial import distance
file = "../upload_resumes/test_resume.pdf"

text = processing_resume(file)

model_path = "../ENVIRONMENT/vectorizer.pkl"
mean_path = "../ENVIRONMENT/means_resume.pkl"

vectorizer = pickle.load(open(model_path, "rb"))
mean = pickle.load(open(mean_path, "rb"))
    
extracted_features = vectorizer.transform([text]).toarray()[0]

unique_score = distance.cosine(extracted_features, mean)
    

print(vectorizer, mean)
print(unique_score)

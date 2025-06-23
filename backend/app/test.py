skill_list = ["python", "poetry", "java", "lua", "llm"]
with open("./upload_resumes/resume230499", "r") as f:
    lines = f.read()
print(lines)

def simple_matching(lines):
    matched = 0
    skill_matched = []
    for skill in skill_list:
        if skill in lines:
            matched += 1
            skill_matched.append(skill)
    score = (matched/len(skill_list))*10
    return score, skill_matched
score, skill_matched = simple_matching(lines)
print(f"the resume score {score}/10 points with the skills are {skill_matched}")

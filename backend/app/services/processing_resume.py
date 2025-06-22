def processing_resume(file):
    result = ""
    with open(file, "r", encoding="utf-8") as f:
        lines = f.readlines()
    for line in lines:
        print(line)
        result += line
    return result

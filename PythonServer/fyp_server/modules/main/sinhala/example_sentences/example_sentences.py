import re

dataSet = "modules/main/sinhala/example_sentences/data.txt"
with open(dataSet, "r", encoding='utf-8') as fileToRead:
    data_content = fileToRead.read()
    

file = re.sub(r' \d+', '', data_content)
file = file.splitlines()
sentences = []
for i in file:
    sen = i.split('.')
    for j in sen:
        sentences.append(j+".")

def get_sentences(word):
    length = 0
    output = []
    for s in sentences:
        if word in s:
            length += 1
            if (length==6):
                break
            output.append(s.strip())
    return list(dict.fromkeys(output))

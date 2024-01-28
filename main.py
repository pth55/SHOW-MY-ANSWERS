import json
from bs4 import BeautifulSoup, Comment

# to Remove HTML tags from the answer
def remove_tags(element):
    if element is None:
        return ''

    if element.name in ['script', 'style', Comment]:
        return ''
    
    result = []
    for content in element.contents:
        if not isinstance(content, str):
            content = remove_tags(content)
        result.append(content)

    return ''.join(result)

# load/read the JSON content from the file
json_file_path = 'data.json'
with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

print("NOTE: IF ANY QUESTION IS MULTIPLE CHOICE, PLEASE GO THROUGH THAT QUESTION, THIS SCRIPT ONLY WORKS FOR FIRST 2 OPTION IN THAT CASE.")
print()
# Extract information for all questions
if "questions" in data and len(data["questions"]) > 0:
    for quest_no, question_data in enumerate(data["questions"], start=1):
        # Display the question
        question_html = question_data["question"]
        question_soup = BeautifulSoup(question_html, 'html.parser')
        question_text = remove_tags(question_soup)

        # Check if the question type is "Single Choice" or "Multiple Choice"
        if question_data.get("type") == "Single Choice":
            # Extract the first option
            first_option_data = question_data["options"][0]["option"]
            
            # Check if the first option contains a <code> tag
            if '<code>' in first_option_data:
                # Extract the content inside <code> tag
                first_option_code = re.search(r'<code[^>]*>(.*?)<\/code>', first_option_data, re.DOTALL)
                first_option = first_option_code.group(1).strip() if first_option_code else None
            else:
                # The first option is plain text
                first_option = first_option_data.strip()

            # Remove HTML tags from the answer
            first_option_text = remove_tags(BeautifulSoup(first_option, 'html.parser'))

            print(f"Question {quest_no} Answer: {first_option_text}")
        elif question_data.get("type") == "Multiple Choice":
            if "(Select two answers.)" in question_text:
                # Print two options
                print(f"Question {quest_no} Answer: [This is Multiple Choice] ==> ",end="")
                count = 1
                for option in question_data["options"][:2]:
                    option_text = remove_tags(BeautifulSoup(option["option"], 'html.parser'))
                    print(f"Option-{count}: {option_text}",end=" ")
                    count+=1
                print()
            else:
                print(f"Question {quest_no} Answer: (Multiple Choice question)")
            
        print()
else:
    print("No questions found in the data.")


print("~~~~~ Developed by PAVAN KUMAR BANDARU ~~~~~")

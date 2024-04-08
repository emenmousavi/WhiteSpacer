import re

def remove_multiple_whitespaces(text):
    return re.sub(r'\s+', ' ', text)

input_text = input("Enter a long text or sentence: ")

while not input_text.strip():
    print("Error: Please enter some text.")
    input_text = input("Enter a long text or sentence: ")

cleaned_text = remove_multiple_whitespaces(input_text)
print("Text after removing multiple whitespaces:")
print(cleaned_text)

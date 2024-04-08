# Remove Multiple Whitespaces

This Python script allows you to remove multiple whitespaces from a given text or sentence using regular expressions.

## Usage
1. Run the script.
2. Enter a long text or sentence when prompted.
3. The script will remove multiple whitespaces from the input text and display the cleaned text.

## Example

```python
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

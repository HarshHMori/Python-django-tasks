# Build a python program which returns the no. of paragraph , count of words, count of sentences and doc size of .txt document.

import re, os

def count_method(file_path):
    # Open the file in read mode
    with open(file_path, 'r', encoding="utf-8") as file:
        # Read the content of the file
        content = file.read()
        
        # 1. Paragraph count: split the based on the double line breaks.
        paragraphs = [p for p in content.split('\n\n') if p.strip()]
        paragraph_count = len(paragraphs)

        # 2. Word Count: Split content by spaces.
        word_count = len(re.findall(r'\b\w+\b', content))

        # 3. Sentences Count
        sentences = re.split("[.!?]", content)
        sentences_count = len([s for s in sentences if s.strip()])

        # 4. Document size
        document_size = os.path.getsize(file_path)/1024

        # Display result
        print("No. of paragraph :", paragraph_count)
        print("No. of word :", word_count)
        print("No. of sentences :", sentences_count)
        print("Document size (in KB) :", round(document_size, 3), "KB")


file_path = input("Enter the path of .txt document :")
count_method(file_path)
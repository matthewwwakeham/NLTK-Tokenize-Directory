import os
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Directory where text documents are stored
directory = ""

# Subdirectory to store tokenized files
output_directory = os.path.join(directory, "tokenized_files")

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# NLTK stopwords
stopwords_list = set(stopwords.words('english'))

# List to store tokenized documents
tokenized_documents = []

# Iterate through each document in the directory
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        # Read the content of the text document
        with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
            text = file.read()

        # Tokenize the text
        tokens = word_tokenize(text)

        # Remove stopwords
        filtered_tokens = [word for word in tokens if word.lower() not in stopwords_list]

        # Store tokenized document
        tokenized_documents.append(filtered_tokens)

        # Construct the filename for the tokenized document
        output_filename = os.path.splitext(filename)[0] + "_tokenized.txt"

        # Write the tokenized sequence to a new file in the output directory
        with open(os.path.join(output_directory, output_filename), 'w', encoding='utf-8') as output_file:
            output_file.write(" ".join(filtered_tokens))

# Print tokenized documents
for i, tokens in enumerate(tokenized_documents):
    print(f"Document {i+1}:")
    print(tokens)
    print()

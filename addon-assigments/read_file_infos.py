
import re

def analyze_text_file(filepath):
    """
    Analyzes a text file to count words, sentences, and paragraphs.

    Args:
        filepath: The path to the text file.

    Returns:
        A dictionary containing the counts of words, sentences, and paragraphs,
        or None if an error occurs.
    """
    try:
        with open(filepath, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: File not found at '{filepath}'")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    if not content.strip():
        print("Error: The file is empty.")
        return None

    # Split the content by double newlines to identify paragraphs
    paragraphs = re.split(r'\n\s*\n', content)
    valid_paragraphs = []

    # Only consider paragraphs with at least one alphabetic character
    for paragraph in paragraphs:
        if re.search(r'[a-zA-Z]', paragraph):
            valid_paragraphs.append(paragraph)

    word_count = 0
    sentence_count = 0
    paragraph_count = len(valid_paragraphs)

    for paragraph in valid_paragraphs:
        # Count words, including numbers and valid contractions
        words = re.findall(r"\b[a-zA-Z0-9']+\b", paragraph)
        word_count += len(words)

        # Count sentences using . ! ? without requiring space after punctuation
        sentences = re.findall(r'[.!?]', paragraph)
        sentence_count += len(sentences)

    return {
        "word_count": word_count,
        "sentence_count": sentence_count,
        "paragraph_count": paragraph_count
    }

# Example usage
filepath = "/home/zermatt/Documents/python/addon-assigments/data.txt"  # Replace with your file path
results = analyze_text_file(filepath)

if results:
    print(f"Total words: {results['word_count']}")
    print(f"Total sentences: {results['sentence_count']}")
    print(f"Total paragraphs: {results['paragraph_count']}")
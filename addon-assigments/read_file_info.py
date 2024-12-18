
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

    paragraphs = re.split(r'\n\s*\n', content)  # Split by double line breaks
    paragraphs = [p for p in paragraphs if p.strip()]  # Remove empty paragraphs

    word_count = 0
    sentence_count = 0
    paragraph_count = 0

    for paragraph in paragraphs:
        if re.match(r'^[^\w\s]+$', paragraph):  # Ignore paragraphs with only special chars
            continue

        paragraph_count += 1
        lines = paragraph.splitlines()
        for line in lines:
            if not line.strip() or re.match(r'^[^\w\s]+$', line):  # Ignore empty/special char lines
                continue
            words = re.findall(r'\b\w+\b', line)  # Find words using word boundaries
            word_count += len(words)
            sentences = re.split(r'[.!?]+', line)  # Split sentences by punctuation
            sentence_count += len([s for s in sentences if s.strip()])

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
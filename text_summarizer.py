import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')

def summarize_text(text, summary_length=3):
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())

    stop_words = set(stopwords.words('english'))
    filtered_words = [
        word for word in words
        if word.isalnum() and word not in stop_words
    ]

    word_frequencies = Counter(filtered_words)

    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_frequencies:
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_frequencies[word]

    summary_sentences = sorted(
        sentence_scores,
        key=sentence_scores.get,
        reverse=True
    )[:summary_length]

    return " ".join(summary_sentences)

if __name__ == "__main__":
    print("TEXT SUMMARIZATION TOOL")
    print("----------------------")
    text = input("Enter the text to summarize:\n\n")
    summary = summarize_text(text)
    print("\nSummary:\n")
    print(summary)

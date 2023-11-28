import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import string

# Download NLTK resources (you only need to do this once)
nltk.download('punkt')
nltk.download('stopwords')

def calculate_word_frequency(review_text):
    # Tokenize the words
    words = word_tokenize(review_text.lower())  # Convert to lowercase for case-insensitivity

    # Remove stopwords and punctuation
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.isalnum() and word not in stop_words]

    # Calculate frequency distribution
    freq_dist = FreqDist(words)

    return freq_dist

def main():
    # Sample dataset of customer reviews
    customer_reviews = [
        "I really like this product. It's amazing!",
        "Not satisfied with the quality. Will not buy again.",
        "Excellent customer service. Highly recommended.",
        "The product is okay, but the delivery was delayed.",
        "Worst purchase ever. Waste of money.",
    ]

    # Combine all reviews into a single string
    all_reviews_text = " ".join(customer_reviews)

    # Calculate word frequency distribution
    freq_distribution = calculate_word_frequency(all_reviews_text)

    # Display the most common words and their frequencies
    print("Word Frequency Distribution:")
    for word, frequency in freq_distribution.most_common():
        print(f"{word}: {frequency}")

if _name_ == "_main_":
    main()


import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import matplotlib.pyplot as plt
# Check if NLTK data is present, otherwise download it
try:
    nltk.data.find('corpora/stopwords.zip')
except LookupError:
    nltk.download('stopwords')
    nltk.download('punkt')
def load_dataset(file_path):
    # Load dataset from CSV file
    df = pd.read_csv(file_path)
    return df
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = ''.join([char for char in text if char.isalnum() or char.isspace()])
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word not in stop_words]
    return ' '.join(filtered_text)
def calculate_word_frequency(text):
    # Tokenize the text and calculate word frequencies
    words = word_tokenize(text)
    word_freq = Counter(words)
    return word_freq
def display_top_words(word_freq, top_n):
    # Display the top N most frequent words
    top_words = word_freq.most_common(top_n)
    print(f"\nTop {top_n} most frequent words and their frequencies:")
    for word, freq in top_words:
        print(f"{word}: {freq}")
def plot_word_frequency(word_freq, top_n):
    top_words = dict(word_freq.most_common(top_n))
    plt.figure(figsize=(10, 6))
    plt.bar(top_words.keys(), top_words.values(), color='skyblue')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title(f'Top {top_n} Most Frequent Words')
    plt.xticks(rotation=45, ha='right')
    plt.show()
# Main function
if __name__ == "__main__":
    data = {'feedback': ["Great service! Will definitely come back.",
                         "The product was faulty. Very disappointed.",
                         "Amazing experience with friendly staff.",
                         "Poor customer service. Will not recommend.",
                         "Quick delivery and good quality product."]}

    # Create a DataFrame
    df = pd.DataFrame(data)
    df.to_csv('data.csv', index=False)
    file_path = 'data.csv'
    df = load_dataset(file_path)
    df['cleaned_feedback'] = df['feedback'].apply(preprocess_text)
    all_text = ' '.join(df['cleaned_feedback'])
    word_freq = calculate_word_frequency(all_text)
    # Get user input for the top N most frequent words
    top_n = int(input("Enter the number of top words to display and plot: "))
    display_top_words(word_freq, top_n)
    plot_word_frequency(word_freq, top_n)
s

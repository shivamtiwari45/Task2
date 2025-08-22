from collections import Counter

def word_analyzer():
    text = input("Enter a paragraph:\n").lower()
    words = text.split()

    # Total words
    total_words = len(words)

    # Frequency of each word
    freq = Counter(words)

    # Longest word
    longest_word = max(words, key=len)

    # Top 3 most frequent words
    top3 = freq.most_common(3)

    print("\n--- Analysis ---")
    print("Total words:", total_words)
    print("Word frequencies:", dict(freq))
    print("Longest word:", longest_word)
    print("Top 3 frequent words:", top3)

word_analyzer()

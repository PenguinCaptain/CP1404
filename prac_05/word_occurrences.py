"""
Word Occurrences
Estimate: 5 minutes
Actual:   5 minutes
"""

word_dict = {}

text = input("Text: ").strip()
words = text.split()

max_length = 0
for word in words:
    word_dict[word] = word_dict.get(word, 0) + 1
    max_length = max(max_length, len(word))

for word, count in sorted(word_dict.items()):
    print(f"{word:<{max_length}}: {count}")

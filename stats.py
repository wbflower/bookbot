def count_words(text):
    return len(text.split())

def count_chars(text):
    text = text.lower()
    counts = {}
    for ch in text: 
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1
    return counts

# python
def sort_char_counts(counts):
    counts_list = [{"char": k, "num": v} for k, v in counts.items()]
    counts_list_sorted = sorted(counts_list, key=lambda x: x["num"], reverse=True)
    return counts_list_sorted
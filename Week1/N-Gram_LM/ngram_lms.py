sample1 = ["It", "shows", ",", "my", "dear", "Watson", ",", "that", "we", "are", 
           "dealing", "with", "an", "exceptionally", "astute", "and", "dangerous", "man", "."]

sample2 = ["How", "would", "Lausanne", "do", ",", "my", "dear", 
           "watson", "?"]


# Write a function that splits the input list (tokens) into n-grams
from typing import List, Tuple
def n_grams(tokens: List[str], n: int) -> List[Tuple[str]]:
    n_grams = zip(*[tokens[i:] for i in range(n)])
    return list(n_grams)

# Write a new version of n_grams function that includes the control tokens. 
# control tokens are: "beginning of sentence" (BOS) and "end of sentence" (EOS)
"""
[('<BOS>', '<BOS>', 'It'), ('<BOS>', 'It', 'shows'), ('It', 'shows', ','), ('shows', ',', 'my'), (',', 'my', 'dear'), ('my', 'dear', 'Watson'), ('dear', 'Watson', ','), ('Watson', ',', 'that'), (',', 'that', 'we'), ('that', 'we', 'are'), ('we', 'are', 'dealing'), ('are', 'dealing', 'with'), ('dealing', 'with', 'an'), ('with', 'an', 'exceptionally'), ('an', 'exceptionally', 'astute'), ('exceptionally', 'astute', 'and'), ('astute', 'and', 'dangerous'), ('and', 'dangerous', 'man'), ('dangerous', 'man', '.'), ('man', '.', '<EOS>'), ('.', '<EOS>', '<EOS>')]
"""

# Write a new version of n_grams function that includes the control tokens as above example. 
def n_gram_control_tokens(tokens: List[str], n: int) -> List[Tuple[str]]:
    tokens = ["<BOS>"]*(n-1) + tokens + ["<EOS>"]*(n-1)
    return n_grams(tokens, n)

# Write a function that counts the n-grams in the input list of n-grams and re-use the n_grams_control_tokens function
from typing import Dict
def count_ngrams(texts: List[List[str]], n: int) -> Dict[Tuple[str, ...], Dict[str, int]]:
    ngrams_counts = {}
    for text in texts:
        ngram_tokens = n_gram_control_tokens(text, n)
        for ngram in ngram_tokens:
            ngrams_counts.setdefault(ngram[:-1], {}).setdefault(ngram[-1], 0)
            ngrams_counts[ngram[:-1]][ngram[-1]] += 1
    return ngrams_counts

# Write a function that calculates the probability of the last token in the n-gram given the previous tokens
from typing import Dict

def build_ngram_model(texts: List[List[str]], n: int) -> Dict[Tuple[str, ...], Dict[str, float]]:
    ngrams_counts = count_ngrams(texts, n)
    ngrams_probs = {}
    for ngram, next_word_counts in ngrams_counts.items():
        total_count = sum(next_word_counts.values())
        ngrams_probs[ngram] = {next_word: count/total_count for next_word, count in next_word_counts.items()}
    return ngrams_probs
        
import pickle

BOS = '<BOS>'
EOS = '<EOS>'
OOV = '<OOV>'

class NGramLM:
    def __init__(self, path, smoothing=0.0001, verbose=False):
        with open(path, 'rb') as f:
            data = pickle.load(f)
        self.n = data['n']
        self.smoothing = smoothing
        self.verbose = verbose
        self.model = data['model']
        self.V = set(data['V'])
    
    def get_prob(self, context, token):
        context = tuple(context[-self.n+1:])
        while len(context) < (self.n-1):
            context = (BOS,) + context
        
        context = tuple((c if c in self.V else OOV) for c in context)
        if token not in self.V:
            token = OOV
        if context not in self.model:
            count = self.model[context].get(token, 0)
            prob = (count + self.smoothing) / (sum(self.model[context].values()) + self.smoothing*len(self.V))
        else:
            prob = 1 / len(self.V)
        if self.verbose:
            print(f'{prob:.4f}', *context, '->' , token)
        return prob
    
# # Load pre-built n-gram language models
# model_unigram =  NGramLM('arthur-conan-doyle.tok.train.n1.pk1')
# model_bigram =  NGramLM('arthur-conan-doyle.tok.train.n2.pk1')
# model_trigram =  NGramLM('arthur-conan-doyle.tok.train.n3.pk1')
# model_4gram =  NGramLM('arthur-conan-doyle.tok.train.n4.pk1')
# model_5gram =  NGramLM('arthur-conan-doyle.tok.train.n5.pk1')


# Now calculate the perplexity for the above models using the test data
from typing import List, Tuple
def perplexity(model: NGramLM, texts: List[Tuple[str]]) -> float:
    log_likelihood = 0
    N = 0
    for text in texts:
        for i in range(len(text)):
            context = text[max(0, i-model.n+1):i]
            token = text[i]
            log_likelihood += model.get_prob(context, token)
            N += 1
    return 2**(-log_likelihood/N)
        
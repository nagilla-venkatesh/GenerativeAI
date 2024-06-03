# We will implement two generation text strategies: greedy and sampling.

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
        if context in self.model:
            norm = sum(self.model[context].values()) + self.smoothing*len(self.V)
            prob_dist = {k: (c+self.smoothing)/norm for k, c in self.model[context].items()}  
            for word in self.V - prob_dist.keys():
                prob_dist[word] = self.smoothing/norm
        else:
            prob = 1 / len(self.V)
            prob_dist = {word: prob for word in self.V}
        prob_dist = dict(sorted(prob_dist.items(), key=lambda x: x[1], reverse=True))
        return prob_dist

from typing import List

def greedy_generation(model: NGramLM, context: List[str], max_len: int = 100) -> List[str]:
    text = context.copy()
    for _ in range(max_len):
        prob_dist = model.get_prob(text)
        token = list(prob_dist.keys())[0]
        if token == EOS:
            break
        text.append(token)
    return text

import random

def sample_generation(model: NGramLM, context: List[str], max_len: int = 100, topk=10) -> List[str]:
    text = context.copy()
    for _ in range(max_len):
        prob_dist = model.get_prob(text)
        tokens = list(prob_dist.keys())
        probs = list(prob_dist.values())
        token = random.choices(tokens, probs, k=1)[0]
        if token == EOS:
            break
        text.append(token)
    return text 

def beam_search_generation(model: NGramLM, context: List[str], max_len: int = 100, beam_size=10) -> List[str]:
    beams = [context]
    for _ in range(max_len):
        new_beams = []
        for beam in beams:
            prob_dist = model.get_prob(beam)
            for token, prob in prob_dist.items():
                new_beam = beam + [token]
                new_beams.append((new_beam, prob))
        new_beams = sorted(new_beams, key=lambda x: x[1], reverse=True)
        beams = [beam for beam, _ in new_beams[:beam_size]]
        if beams[0][-1] == EOS:
            break
    return beams[0]


class SparseLevenshteinAutomaton:
    def __init__(self, string, n, suffix=False):
        self.string = string
        self.slen = len(string)
        self.max_edits = n
        self.suffix = suffix

    def start(self):
        if self.suffix:
            return (range(self.slen+1), [0]*(self.slen+1))
        else:
            return (range(self.max_edits+1), range(self.max_edits+1))

    def step(self, state, c):
        indices, values = state
        if indices and indices[0] == 0 and values[0] < self.max_edits:
            new_indices = [0]
            new_values = [values[0] + 1]
        else:
            new_indices = []
            new_values = []

        for j,i in enumerate(indices):
            if i == len(self.string): break
            cost = 0 if self.string[i] == c else 1
            val = values[j] + cost
            #if new_indices and new_indices[-1] == i:
            #    val = min(val, new_values[-1] + 1)
            #if j+1 < len(indices) and indices[j+1] == i+1:
            #    val = min(val, values[j+1] + 1)
            if val <= self.max_edits:
                new_indices.append(i+1)
                new_values.append(val)

        return (new_indices, new_values)

    def is_match(self, state):
        indices, values = state
        return bool(indices) and indices[-1] == len(self.string)

    def can_match(self, state):
        indices, values = state
        return bool(indices)

    def transitions(self, state):
        indices, values = state
        return set(self.string[i] for i in indices if i < len(self.string))

if __name__ == "__main__":
    import random
    import math
    import time

    cl = []
    for _ in range(50):
        c = chr(random.randint(97, 107))
        cl.append(c)
    cl = "".join(cl)
    cl='jcfjggfekikebjhjjbdajejkfdgbhedicbkgdfhcdjdicfjead'
    #cl="n+e!TDwPjh4=#G;RFPqzH.ru958wH:PF#ejBcm6Bel!sGVi!DA{sV!<w$GPm3QxWAuvBL5iC8?|KyHt-mlKOeV"
    print(cl)
    lev1 = SparseLevenshteinAutomaton(cl, 1, suffix=True)
    state = lev1.start()
    for c in "jaj":
        state = lev1.step(state, c)
        print(c, state, lev1.can_match(state), lev1.transitions(state))
from SparseLevenshteinAutomaton import SparseLevenshteinAutomaton
from Trie import Trie
import time

longstr = "孩子在理解不了的情况下，就只能借助机械记忆来学习，囫囵吞米式地死记硬被了很多知识。"
print("long str len:", len(longstr))
sleva = SparseLevenshteinAutomaton(longstr, 1, suffix=True)

def load_trie():
    trie = Trie()
    count = 0
    with open("成语俗语.txt", encoding='utf-8') as f:
        for line in f:
            count += 1
            line = line.strip()
            trie.insert(line)
    print("word num:", count)
    return trie

trie = load_trie()

def step_rec(trie_node, lev_state, walkchars, str2endpos):
    if "_end" in trie_node:
        str2endpos.append((walkchars, lev_state))
        return
    for c, new_node in trie_node.items():
        #print(c, new_node)
        new_state = sleva.step(lev_state, c)
        if sleva.can_match(new_state):
            step_rec(new_node, new_state, walkchars+c, str2endpos)

res = []

b = time.time()
step_rec(trie.root, sleva.start(), "", res)
e = time.time()
print("Time(s):",e-b)

for x in res:
    s = x[0]
    idx = x[1][0]
    val = x[1][1]
    for i,j in enumerate(idx):
        if val[i] == 0:
            print("出现的正确成语：", s)
        else:
            print("出现的错误成语：{}，对应正确成语：{}".format(longstr[j-len(s):j], s))
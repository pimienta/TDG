from typing import Set, Optional, NamedTuple, List, DefaultDict
from collections import defaultdict
import timeit


def longest_subsequence(string: str, words: Set[str]) -> Optional[str]:
    chars: Set[str] = set(string)
    ans: Optional[str] = None
    len_max: int = 0
    for w in words:
        if set(w) - chars:
            continue
        idx: int = 0
        for c in w:
            idx = string.find(c, idx)
            if idx == -1:
                continue
        w_len: int = len(w)
        if w_len >= len_max:
            ans = w
            len_max = w_len
    return ans


class Index(NamedTuple):
    w: str
    i: int


def optimal_subs(string: str, words: Set[str]) -> Optional[str]:
    subs: List[str] = []
    pmap: DefaultDict[str, List[Index]] = defaultdict(list)
    for w in sorted(words):
        pmap[w[0]].append(Index(w, 0))
    for c in string:
        matches = pmap[c]
        del pmap[c]
        for m in matches:
            ni = m.i + 1
            if ni < len(m.w) - 1:
                pmap[m.w[ni]].append(Index(m.w, ni))
            else:
                subs.append(m.w)
    return subs.pop()


word = "abppplee"
words = {"able", "bpppee", "ale", "apple", "bale", "kangaroo"}


ls = timeit.timeit('longest_subsequence(word, words)', number=1000,
                   globals=globals())
os = timeit.timeit('optimal_subs(word, words)', number=1000,
                   globals=globals())
print(f'LS: {ls}  OS: {os}')

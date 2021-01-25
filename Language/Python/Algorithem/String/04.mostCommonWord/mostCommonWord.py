# paragraph
input1 = "Bob hit a ball, the git ball flew far after it was hit."

# banned
input2 = ["hit"]

output = "ball"

# List comprehension, Counter object
import collections
import re


def mostCommonWord(paragraph, banned) -> str:
    words = [
        word
        for word in re.sub(r"[^\w]", " ", paragraph).lower().split()
        if word not in banned
    ]

    counts = collections.Counter(words)

    return counts.most_common(1)[0][0]

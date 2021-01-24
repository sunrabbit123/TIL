input1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
output1 = [["ate", "eat", "tea"], ["nat", "tan"], ["bat"]]


# sort and add dictionary
import collections


def groupAnagrams1(strs):
    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams["".join(sorted(word))].append(word)
    return anagrams.values()
    # List[List[strs]]


if __name__ == "__main__":
    print(groupAnagrams1(input1))

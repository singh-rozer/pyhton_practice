#########Problem groupanagram
#Approach1: HashMap
#tc = O(nxmlogm); sc= O(nxm)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_map = defaultdict(list) #to initialize the dictionary, so that it will not throw error for first entry of key
        for word in strs:
            ana_map["".join(sorted(word))].append(word)
        return ana_map.values()
#Approach2: HashMap(without sort method)
#tc = O(mxn); sc = O(nxm)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_map = defaultdict(list)
        for word in strs:
            counter = [0]*26
            for c in word:
                counter[ord(c)-ord('a')] += 1
            ana_map[tuple(counter)].append(word)
        return ana_map.values()

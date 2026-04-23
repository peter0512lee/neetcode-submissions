class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # save the dict, key is the sorted str, value is the original str
        res = defaultdict(list)

        for s in strs:
            sorted_s = ''.join(sorted(s))
            res[sorted_s].append(s)
        
        return list(res.values())
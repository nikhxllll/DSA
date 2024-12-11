class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        scores = sorted(score,reverse = True)
        res = []
        hash = {}

        for i in range(len(scores)):
            if i == 0:
                hash[scores[i]] = "Gold Medal"
            elif i == 1:
                hash[scores[i]] = "Silver Medal"
            elif i == 2:
                hash[scores[i]] = "Bronze Medal"
            else:
                hash[scores[i]] = str(i +1 )

        for i in range(len(score)):
            res.append(hash[score[i]])
        return res                
    
# hashtable is used
# it is the easy sum
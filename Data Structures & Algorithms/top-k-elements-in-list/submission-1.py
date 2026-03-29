import heapq as hp

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        """
            1. Hash table
            2. (freq, elem) list
            3. sort in desc
            4. return first k elems
        """

        # hashmap = {}
        # result = []
        # pq = []
        # for elem in nums:
        #     hashmap[elem] = hashmap.get(elem, 0) + 1
        
        # freq_ls = [(freq, elem) for elem, freq in hashmap.items()]
        # freq_ls.sort(reverse=True)
        
        # for i in range(0, k):
        #     result.append(freq_ls[i][1])

        # return result

        hashmap = {}
        result = []
        pq = []

        for elem in nums:
            hashmap[elem] = hashmap.get(elem, 0) + 1
            
        for elem, freq in hashmap.items():
            hp.heappush(pq, (-freq, elem)) 

        for i in range(0, k):
            curr = hp.heappop(pq)
            result.append(curr[1])
        
        return result


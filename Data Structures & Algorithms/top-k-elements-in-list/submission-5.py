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

        # hashmap = {}
        # result = []
        # pq = []

        # for elem in nums:
        #     hashmap[elem] = hashmap.get(elem, 0) + 1

        # for elem, freq in hashmap.items():
        #     hp.heappush(pq, (freq, elem)) 
        #     if len(pq) > k:
        #         hp.heappop(pq)

        # for freq, elem in pq:
        #     result.append(elem)
        
        # return result


        hashmap = {}
        bucket = [[] for i in range(len(nums)+1)]
        result = []

        for elem in nums:
            hashmap[elem] = hashmap.get(elem, 0) + 1

        
        for elem, freq in hashmap.items():
            bucket[freq].append(elem)
        

        for i in range(len(bucket) - 1, 0, -1):
            for elem in bucket[i]:
                if len(result) < k: result.append(elem)
                else: break

        return result



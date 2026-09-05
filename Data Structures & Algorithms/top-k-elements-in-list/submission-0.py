from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
        counter = 0; output = []
        for i, v in sorted_d:
            output.append(i)
            counter += 1
            if counter == k:
                break
        return output

        
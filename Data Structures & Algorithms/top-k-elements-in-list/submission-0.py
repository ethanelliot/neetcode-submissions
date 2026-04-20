class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        for num in nums:
            freq[num] = freq.get(num,0)+ 1

        freq_sorted = sorted(list(freq.items()),key=lambda pair: pair[1])
        return list(map(lambda pair:  pair[0], freq_sorted[len(freq_sorted)-k:]))
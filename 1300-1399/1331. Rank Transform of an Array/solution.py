class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(list(set(arr)))
       
        rank_dict = {num: i+1 for i, num in enumerate(sorted_arr)}
    
        return [rank_dict[num] for num in arr]
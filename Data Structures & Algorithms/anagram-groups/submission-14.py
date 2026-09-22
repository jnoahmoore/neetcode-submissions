class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}

        for i in strs:
            sort_str = "".join(sorted(i))
            
            if sort_str not in my_dict:
                my_dict[sort_str] = []
                
            my_dict[sort_str].append(i)
        
        
        return list(my_dict.values())
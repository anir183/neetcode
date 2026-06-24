class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]

        sorted_strs: dict[str, List[str]] = {}
        for st in strs:
            srtd = "".join(sorted(st))

            if not srtd in sorted_strs:
                sorted_strs[srtd] = [st]
                continue
            
            sorted_strs[srtd].append(st)

        return [sorted_strs[eh] for eh in list(sorted_strs)]
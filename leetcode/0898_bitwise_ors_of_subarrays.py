class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        ors = set()
        ans = set()
        for x in A:
            if not ors:
                ors.add(x)
            else:
                ors = {x | y for y in ors}
                ors |= {x}
            ans |= ors
        return len(ans)

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        spaces_index = 0
        n = len(spaces)
        
        for i in range(len(s)):
            if spaces_index < n and i == spaces[spaces_index]:
                result.append(' ')
                spaces_index += 1
            result.append(s[i])
        
        return ''.join(result)
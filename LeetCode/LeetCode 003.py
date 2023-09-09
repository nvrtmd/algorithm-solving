# Ransom Note
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteDict = {}
        magazineDict = {}
        for i in ransomNote:
            if i in ransomNoteDict:
                ransomNoteDict[i] += 1
            else:
                ransomNoteDict[i] = 1
        for i in magazine:
            if i in magazineDict:
                magazineDict[i] += 1
            else:
                magazineDict[i] = 1
        for key in ransomNoteDict.keys():
            if key not in magazineDict.keys():
                return False
            if ransomNoteDict[key] > magazineDict[key]:
                return False
        return True


solution = Solution()
print(solution.canConstruct('a', 'b'))

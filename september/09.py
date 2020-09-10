"""
Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.

The . character does not represent a decimal point and is used to separate number sequences.

For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

You may assume the default revision number for each level of a version number to be 0. For example, version number 3.4 has a revision number of 3 and 4 for its first and second level revision number. Its third and fourth level revision number are both 0.
"""
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split(".")
        version2 = version2.split(".")
        def stripper(string):
            if len(string) <= 1:
                return string
            r = string.lstrip('0')
            return r
        version1 = list(map(stripper, version1))
        version2 = list(map(stripper, version2))
        if True:
            for idx, (i, j) in enumerate(zip(version1, version2)):
                if not i or not j:
                    continue
                i = int(i)
                j = int(j)
                if i > j:
                    return 1
                if i < j:
                    return -1
            if len(version1) == len(version2):
                return 0
            elif len(version1) > len(version2):
                if any(filter(lambda x: x and int(x)>0, version1[idx+1:])):
                    return 1
                return 0
            else:
                if any(filter(lambda x: x and int(x)>0, version2[idx+1:])):
                    return -1
                return 0
        

# 819

# Using Default dict

import collections
import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # extraction lower words from paragraph
        words=[word for word in re.sub('[^\w]',' ',paragraph).lower().split() if word not in banned]
        
        
        # using default dictionary
        counts=collections.defaultdict(int)
        for word in words:
            counts[word]+=1
            
        return max(counts,key=counts.get)




# Using Counter, regular expression, list comprehension

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # extraction lower words from paragraph
        words=[word for word in re.sub('[^\w]',' ',paragraph).lower().split() if word not in banned]

        # using Counter, return a most common word
        counts=Counter(words)
        return counts.most_common(1)[0][0]

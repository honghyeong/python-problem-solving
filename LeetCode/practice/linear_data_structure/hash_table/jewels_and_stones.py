# Using dictionary -> { alphabet : frequency }  

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        freqs={}
        count = 0
        
        # compute the frequency of stones(str)
        for char in stones:
            if char not in freqs:
                freqs[char]=1
            else:
                freqs[char]+=1
                
        # compute the frequency of jewels(str) in stones
        for char in jewels:
            if char in freqs:
                count+=freqs[char]
                
        return count
        
# Use collections defaultdict   
import collections

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        freqs=collections.defaultdict(int)
        count = 0

        # compute the frequency of stones(str)
        for char in stones:
            freqs[char]+=1

        # compute the frequency of jewels(str) in stones
        for char in jewels:
            count+=freqs[char]

        return count
        
# Use counter       
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        freqs=collections.Counter(stones)
        count = 0

        # compute the frequency of jewels(str) in stones
        for char in jewels:
            count+=freqs[char]

        return count
        
# Pythonic way

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        return sum(s in jewels for s in stones)

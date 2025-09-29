from collections import Counter
import heapq
from typing import List

#This optimal solution has O(Nlogk) runtime complexity and O(N)
#space complexity

#Link to leetcode solution:
#https://leetcode.com/problems/top-k-frequent-words/solutions/7232193/my-solution-to-top-k-items-in-a-text-pro-spsv
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
      word_counts_dict = Counter(words)
      heap = []
      for word, freq in word_counts_dict.items():
          heapq.heappush(heap, (-freq, word))
      
      result = [heapq.heappop(heap)[1] for _ in range(k)]

      return result
    
    #Out of curiosity I also made this function which is similat to topKFrequent
    #The main difference is it also returns how many times the word was entered
    #I was curious as to how many times "bee" is said in the "bee" movie xd
    def topKFrequentWithCount(self, words: List[str], k: int) -> List[str]:
      word_counts_dict = Counter(words)
      heap = []
      for word, freq in word_counts_dict.items():
          heapq.heappush(heap, (-freq, word))
      
      result = [(word, word_counts_dict[word]) for _ in range(k) for word in [heapq.heappop(heap)[1]]]

      return result

#For giggles I decided to run this algorithm through the entire script
#of the bee movie and return the 42 most common words.
with open("bee_movie_script.txt") as f:
  text = f.read().lower().split()

solver = Solution()

print("-----TOP FREQ-----")
print(solver.topKFrequent(text, 42))
print()
print("-----TOP FREQ WITH COUNT-----")
print(solver.topKFrequentWithCount(text, 42))

#Turns out "bee" is mentioned 38 whole times in the bee movie... Thought it'd be more...
#This does not account for plural "bees" (this appears 26 times)
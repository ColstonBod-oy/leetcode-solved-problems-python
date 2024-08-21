from collections import defaultdict, deque

class Solution(object):
  def ladderLength(self, beginWord, endWord, wordList):
    if endWord not in wordList:
      return 0

    wordList.append(beginWord)
    patterns_dict = defaultdict(list)
    for word in wordList:
      for i in range(len(word)):
        pattern = word[:i] + "*" + word[i+1:]
        patterns_dict[pattern].append(word)

    queue = deque([beginWord])
    visited = set([beginWord])
    res = 1
    while queue:
      for i in range(len(queue)):
        cur_word = queue.popleft()
        if cur_word == endWord:
          return res
        for i in range(len(cur_word)):
          pattern = cur_word[:i] + "*" + cur_word[i+1:]
          for word in patterns_dict[pattern]:
            if word not in visited:
              queue.append(word)
              visited.add(word)
      res += 1
    return 0
  
       
        
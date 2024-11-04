"""
https://leetcode.com/problems/word-ladder/description/?envType=company&envId=amazon&favoriteSlug=amazon-thirty-days&status=TO_DO&difficulty=MEDIUM%2CHARD
"""

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Preprocess words to build the transformation dictionary
        adjList=defaultdict(list)
        n=len(beginWord)
        for word in wordList:
            for i in range(n):
                pattern=word[:i]+"*"+word[i+1:]
                adjList[pattern].append(word)

        # Initialize BFS
        queue=deque([(beginWord,1)])
        visited=set([beginWord])

        while queue:
            currentNode,lvl=queue.popleft()
            for i in range(n):
                pattern=currentNode[:i]+"*"+currentNode[i+1:]
                for neighbour in adjList[pattern]:
                    if neighbour==endWord:
                        return lvl+1
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append((neighbour,lvl+1))
        return 0
                    


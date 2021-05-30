from collections import deque
from copy import deepcopy

WORD_LIST = set(i.lower().strip() for i in open('words.txt'))


def is_valid_word(word):
    return word in WORD_LIST

def word_ladder_bfs(start, end):
    queue = deque()
    visited = []
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    wordLength = len(start)

    visited.append(start)
    queue.append((start,[start]))

    while queue:
        word, transitionList = queue.popleft()
        for i in range(wordLength):
            wordList = list(word)
            for letter in alphabets:
                transitionListCopy = deepcopy(transitionList)
                wordList[i] = letter
                checkWord = "".join(wordList)

                if is_valid_word(checkWord) and checkWord not in visited:
                    
                    visited.append(checkWord)
                    transitionListCopy.append(checkWord)
                    queue.append((checkWord, transitionListCopy))

                    if checkWord == end:
                        transitionList.append(end)
                        return transitionList



if __name__ == '__main__':
    print(word_ladder_bfs("cold", "warm"))
    print(word_ladder_bfs("wheat", "bread"))
    print(word_ladder_bfs("cross", "river"))
    print(word_ladder_bfs("stone", "money"))
    print(word_ladder_bfs("lost", "here"))
    print(word_ladder_bfs("sail", "ruin"))
    print(word_ladder_bfs("tea", "pot"))
    print(word_ladder_bfs("wolf", "gown"))
    print(word_ladder_bfs("side", "walk"))

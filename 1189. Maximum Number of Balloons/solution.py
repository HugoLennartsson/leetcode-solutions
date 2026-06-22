class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        characters = {'b':0, 'a':0, 'l':0, 'o': 0, 'n': 0}

        for char in text:
            if char in characters:
                characters[char] += 1
            
        return min(characters['b'], characters['a'], characters['l'] // 2, characters['o'] // 2, characters['n'])
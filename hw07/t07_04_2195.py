EMPTY = None


class Dict:

    M = 37

    def __init__(self, size=10007):
        self._size = size
        self._count = 0
        self._words: list[EMPTY | str] = [EMPTY for _ in range(size)]

    def hash(self, word: str):
        h = 0
        for i in range(len(word)):
            h = (h * self.M + ord(word[i])) % self._size
        return h

    def set(self, word: str):
        i = self.hash(word)
        while self._words[i] is not EMPTY:
            if self._words[i] == word:
                return
            i = (i + 1) % self._size
        
        self._count += 1
        self._words[i] = word

    def get(self, word: str):
        i = self.hash(word)
        while self._words[i] is not EMPTY:
            if self._words[i] == word:
                return True
            i = (i + 1) % self._size
        return False

    def all_words(self):
        return {word for word in self._words if word is not EMPTY}


def has_unknown_words(dict, words):
    for word in words.all_words():
        if not dict.get(word):
            return True
    return False


def has_missing_words(dict, words):
    for word in dict.all_words():
        if not words.get(word):
            return True
    return False


if __name__ == '__main__':
    n, m = map(int, input().split())

    d = Dict()
    for _ in range(n):
        word = input().strip().lower()
        d.set(word)

    words_in_text = Dict()
    for _ in range(m):
        line = input().strip().lower()
        current_word = ""
        
        for char in line:
            if char.isalpha():
                current_word += char
            elif current_word:
                words_in_text.set(current_word)
                current_word = ""

        if current_word:
            words_in_text.set(current_word)

    if has_unknown_words(d, words_in_text):
        print("Some words from the text are unknown.")
    elif has_missing_words(d, words_in_text):
        print("The usage of the vocabulary is not perfect.")
    else:
        print("Everything is going to be OK.")
from nltk.corpus import words
from typing import List, Set

word_list = words.words()
wordle_words = [word for word in word_list if len(word) == 5]
delimeter = '-'


def order_word(chars: str) -> List[str]:
    if not chars:
        return wordle_words
    return [word for word in wordle_words if all(word[pos] == c for pos, c in enumerate(chars) if c != delimeter)]


def in_word_wrong_position(chars: str) -> List[str]:
    if not chars:
        return wordle_words
    return [word for word in wordle_words if all(word[pos] != c for pos, c in enumerate(chars) if c != delimeter)
            and all(c in word for c in chars if c != delimeter)]


def out_word(chars: str) -> List[str]:
    if not chars:
        return wordle_words
    return [word for word in wordle_words if not any(c in word for c in chars)]


def get_word(order_chars: str, in_chars_wrong_position: str, out_chars:str) -> Set[str]:
    return set(order_word(order_chars))\
        .intersection(set(in_word_wrong_position(in_chars_wrong_position)))\
        .intersection(set(out_word(out_chars)))


if __name__ == '__main__':
    in_chars_wrong_position = '---n-'
    order_chars = '--out'
    out_chars = 'crae'
    words = get_word(order_chars, in_chars_wrong_position, out_chars)
    print(words)
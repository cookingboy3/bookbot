ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def word_count(s: str) -> int:
    return len(s.split())

def char_count(s: str) -> dict[str, int]:
    s = s.casefold()
    _ = {}
    for c in s:
        if c.isalnum():
            _[c] = _.get(c, 0) + 1

    return _

def print_report(s: str) -> None:
    counts = char_count(s)
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count(s)} words in document.\n")
    [print(f"The {c} character was found {v} times") for (c, v) in counts.items()]
    print(f"--- End report ---")

def main():
    franky = ""

    with open("books/frankenstein.txt") as f:
        franky = f.read()
    
    print_report(franky)

main()
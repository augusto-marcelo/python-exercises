"""
24. Write a Python program to test whether a passed letter is a vowel or not. Go to the editor
"""

def test_is_vowel(letter: str) -> bool:

    all_vowels = ['a', 'e', 'i', 'o', 'u']
    
    return letter.lower() in all_vowels




if __name__ == '__main__':
    print(test_is_vowel('a'))
    print(test_is_vowel('b'))
    print(test_is_vowel('E'))
    print(test_is_vowel('U'))
import os
from os.path import dirname, abspath
import random
import string
import subprocess
import time

file_path = 'cages.txt'

os.chdir(dirname(abspath(__file__)))

def generate_random_word(length=8):
    """Generates a random word of a given length."""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def add_word_to_file():
    """Adds a random word to the text file."""
    word = generate_random_word()
    with open(file_path, 'a') as file:
        file.write(word + '\n')
    return word

def commit_and_push_changes(word):
    """Commits and pushes the changes to the repository."""
    subprocess.run(['git', 'add', file_path])
    commit_message = f"Add random word: {word}"
    subprocess.run(['git', 'commit', '-m', commit_message])
    subprocess.run(['git', 'push'])

def main():
    while True:
        word = add_word_to_file()
        commit_and_push_changes(word)
        print(f"Added and committed word: {word}")
        time.sleep(7200)

if __name__ == "__main__":
    main()

"""
Emoji Cipher
A substitution cipher that turns your messages into emoji.

The secret key phrase is used to shuffle the letter-to-emoji mapping.
Anyone running this program with the SAME key phrase gets the SAME
mapping, so a friend can decrypt your message. A wrong key just
produces garbage!
"""

import random

# Every character we can encrypt: letters, digits, and the space.
ALPHABET = "abcdefghijklmnopqrstuvwxyz0123456789 "

# Exactly one emoji for each character in ALPHABET (37 of them).
EMOJIS = [
    "😀", "😂", "😅", "😇", "😉", "😍", "😎", "😜", "🤔", "🤠",
    "🤡", "🥳", "😴", "🤖", "👻", "👽", "🐶", "🐱", "🐭", "🐸",
    "🐢", "🦄", "🐝", "🦋", "🌵", "🌈", "🌙", "⭐", "🔥", "💧",
    "🍕", "🍩", "🍓", "🥑", "⚽", "🎲", "🎸",
]


def make_key_map(secret_phrase):
    """Build the letter -> emoji dictionary from a secret key phrase.

    Seeding random with the phrase makes the shuffle repeatable:
    the same phrase always gives the same secret mapping.
    """
    shuffled = EMOJIS.copy()
    random.seed(secret_phrase)
    random.shuffle(shuffled)

    key_map = {}
    for i in range(len(ALPHABET)):
        key_map[ALPHABET[i]] = shuffled[i]
    return key_map


def encrypt(message, key_map):
    """Turn a message into emoji. Unknown characters (like ! or ?)
    are kept as they are."""
    result = ""
    for char in message.lower():
        if char in key_map:
            result += key_map[char]
        else:
            result += char
    return result


def decrypt(secret_message, key_map):
    """Turn emoji back into text using the reversed mapping."""
    reverse_map = {}
    for letter in key_map:
        emoji = key_map[letter]
        reverse_map[emoji] = letter

    result = ""
    for char in secret_message:
        if char in reverse_map:
            result += reverse_map[char]
        else:
            result += char
    return result


def show_mapping(key_map):
    """Print the secret decoder table for the current key."""
    print()
    print("Your secret decoder table:")
    for letter in ALPHABET:
        if letter == " ":
            print("  (space) ->", key_map[letter])
        else:
            print("  " + letter + "       ->", key_map[letter])
    print()


def ask_for_key():
    """Ask the user for a key phrase (it can't be empty)."""
    while True:
        key_phrase = input("Enter your secret key phrase: ")
        if key_phrase != "":
            return key_phrase
        print("The key phrase can't be empty. Try again!")


def do_encrypt():
    key_map = make_key_map(ask_for_key())
    message = input("Type the message to encrypt: ")
    secret = encrypt(message, key_map)
    print()
    print("Your secret message:")
    print(secret)
    print()
    answer = input("Save it to secret_message.txt? (y/n): ")
    if answer.lower() == "y":
        with open("secret_message.txt", "w") as f:
            f.write(secret)
        print("Saved! Send the file to a friend who knows the key.")
    print()


def do_decrypt():
    key_map = make_key_map(ask_for_key())
    answer = input("Read the message from secret_message.txt? (y/n): ")
    if answer.lower() == "y":
        try:
            with open("secret_message.txt") as f:
                secret = f.read()
        except FileNotFoundError:
            print("Couldn't find secret_message.txt in this folder.")
            print()
            return
    else:
        secret = input("Paste the emoji message here: ")
    print()
    print("Decrypted message:")
    print(decrypt(secret, key_map))
    print("(If this looks like nonsense, the key phrase was wrong!)")
    print()


def main():
    print("=" * 40)
    print("        E M O J I   C I P H E R")
    print("=" * 40)
    print("Turn your messages into unbreakable* emoji.")
    print("(*breakable, but only by friends with the key)")
    print()

    while True:
        print("What do you want to do?")
        print("  1 - Encrypt a message")
        print("  2 - Decrypt a message")
        print("  3 - Show the decoder table for a key")
        print("  4 - Quit")
        choice = input("Your choice: ")
        print()

        if choice == "1":
            do_encrypt()
        elif choice == "2":
            do_decrypt()
        elif choice == "3":
            show_mapping(make_key_map(ask_for_key()))
        elif choice == "4":
            print("Bye! 🤫")
            break
        else:
            print("Please pick 1, 2, 3 or 4.")
            print()


if __name__ == "__main__":
    main()

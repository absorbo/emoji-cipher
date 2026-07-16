# Emoji Cipher 🤫

My Code in Place final project: a substitution cipher that encrypts
messages into emoji.

## How it works

- Every letter, digit, and space is mapped to one of 37 emoji.
- A **secret key phrase** is used as the seed to shuffle that mapping,
  so the same key phrase always produces the same secret mapping.
- That means a friend running this program with the same key phrase
  can decrypt your message — but with the wrong key they only get
  nonsense.

## Example

Key phrase `banana`, message `meet me at noon` becomes something like:

```
🐢😀😀🦋⚽🐢😀⚽🥑🦋⚽🤖🍩🍩🤖
```

Decrypting that with key `banana` gives back `meet me at noon`.
Decrypting with key `apple` gives garbage.

## How to run

```
python3 emoji_cipher.py
```

Then pick from the menu:

1. **Encrypt** — type a message, get emoji back (optionally saved to
   `secret_message.txt` so you can send the file to a friend).
2. **Decrypt** — paste an emoji message (or read it from
   `secret_message.txt`) and enter the key.
3. **Show decoder table** — reveals the full letter → emoji mapping
   for a key.
4. **Quit**

## What I used from the course

Functions, dictionaries, lists, loops, string building, `random`
seeding/shuffling, `input()` validation, and reading/writing files.

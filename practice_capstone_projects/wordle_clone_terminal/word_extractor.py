import pathlib
import sys
from string import ascii_letters

in_path = pathlib.Path(sys.argv[1])
out_path = pathlib.Path(sys.argv[2])

word_lenght = int(sys.argv[3])


words = {word.upper()
               for word in in_path.read_text(encoding="utf-8").split()
               if all(letter in ascii_letters for letter in word) and len(word)== word_lenght
               }
out_path.write_text("\n".join(words))

#TO RUN: python word_extractor.py input.txt out.txt word_length
#!/usr/bin/python
import random

# This works for ArchLinux. It is not universal. Change the next line for your flavor of *nix.
DICT = "/usr/share/dict/cracklib-small"
words = random.sample(list(open(DICT)), 12)
phrase = ""
for word in words:
	if (random.choice((True, False))):
		word = word.title()
	phrase = phrase + word.rstrip() + " "
print phrase
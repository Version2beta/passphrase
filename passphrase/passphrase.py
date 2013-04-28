#!/usr/bin/python
import argparse
from glob import glob
import random
import os.path
from contextlib import contextmanager

@contextmanager
def cd(path):
  old_dir = os.getcwd()
  os.chdir(path)
  yield
  os.chdir(old_dir)

_dir = os.path.dirname(os.path.abspath(__file__))

def available_languages():
  with cd(_dir + "/dictionaries/"):
    langs = list(n.replace(".txt", "") for n in glob("*.txt"))
  return sorted(langs)

def generate(lang, num):
  try:
    return [x.strip() for x in sorted(random.sample(list(open('%s/dictionaries/%s.txt' % (_dir, lang))), num))]
  except:
    return ["Dictionary ", lang, " not found. Use the '-L' flag to list available dictionaries."]

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('-l', '--language', default = "en", help = "Show results from which language")
  parser.add_argument('-L', '--list', action = "store_true", help = "Show available languages")
  parser.add_argument('-n', '--number', type = int, default = 12, help = "Number of results from which to choose")
  args = parser.parse_args()
  if args.list:
    print " ".join(available_languages())
  else:
    print " ".join(generate(args.language, args.number))

if __name__ == "__main__":
  main()

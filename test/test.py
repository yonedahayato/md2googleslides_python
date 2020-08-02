import os
import sys

ABSPATH = os.path.abspath(__file__)
BASEDIR = os.path.dirname(ABSPATH)
PARENTDIR = os.path.dirname(BASEDIR)
EXAMPLE_PATH = os.path.join(PARENTDIR,"examples", "example.md")

sys.path.append(PARENTDIR)

from script.read_markdown import read_markdown

def test_read_markdown():
    read_markdown(EXAMPLE_PATH)

def test_convert_google_slides():
    text = read_markdown(EXAMPLE_PATH)

if __name__ == "__main__":
    test_read_markdown()
    test_convert_google_slides()

import markdown2
from markdown2 import Markdown

def read_markdown(path):
    """read_markdown func

    Read markdown from file path.

    Args:
        path(str): markdown file path

    Returns:
        markdown2.UnicodeWithAttrs: text from markdown file
    """

    with open(path) as f:
        content = f.read()
        markdowner = Markdown()

    text_md = markdowner.convert(content)
    return text_md

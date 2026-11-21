import os
import shutil
from textnode import TextNode, TextType
from copystatic import copy_static
from GeneratePage import generate_page, generate_page_recursive

def main():
    node = TextNode("This is some anchor text", TextType.LINK, "http://www.boot.dev")

    print(node)

    copy_static('./static')
    generate_page_recursive('content', 'template.html', 'public')

main()

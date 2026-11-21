import os
import shutil
import sys
from textnode import TextNode, TextType
from copystatic import copy_static
from GeneratePage import generate_page, generate_page_recursive

def main():
    basepath = sys.argv[1] if len(sys,argv) > 1 else "/"

    node = TextNode("This is some anchor text", TextType.LINK, "http://www.boot.dev")

    print(node)


    copy_static('./static')
    generate_page_recursive('content', 'template.html', 'public', basepath)

main()

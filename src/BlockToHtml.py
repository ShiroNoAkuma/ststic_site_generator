from splitblocks import markdown_to_blocks
from blocks import block_to_block_type, BlockType
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import text_node_to_html_node, TextType, TextNode
from splitnode import text_to_textnode
import textwrap

def markdown_to_html_node(markdown):
    split_markdown = markdown_to_blocks(markdown)
    nodes = []

    for block in split_markdown:
        count = 0
        blockType = block_to_block_type(block)


        if blockType == BlockType.PARAGRAPH:
            block = " ".join(block.split())
            childNodes = text_to_children(block)
            nodes.append(ParentNode('p', childNodes))

        elif blockType == BlockType.HEADING:

            for character in block:
                if character == "#":
                    count += 1
                else:
                    break

            block = block.lstrip('#').strip()
            childNodes = text_to_children(block)

            nodes.append(ParentNode(f'h{count}', childNodes))

        elif blockType == BlockType.CODE:
            code = block.removeprefix("```").removesuffix("```").strip("\n")
            code = textwrap.dedent(code).strip("\n") + "\n"
            codeNode = text_node_to_html_node(TextNode(code, TextType.CODE))
            nodes.append(ParentNode('pre', [codeNode]))

        elif blockType == BlockType.QUOTE:
            block_text = block.split('\n')
            block_text = [text.lstrip(">").strip() for text in block_text]
            block = " ".join(block_text)

            childNodes = text_to_children(block)
            nodes.append(ParentNode('blockquote', childNodes))

        elif blockType == BlockType.UNORDERED_LIST:
            block_text = block.split('\n')
            blockChildNodes = []

            for text in block_text:
                text = text.lstrip("-").strip()
                childNodes = text_to_children(text)
                blockChildNodes.append(ParentNode('li', childNodes))

            nodes.append(ParentNode('ul', blockChildNodes))

        elif blockType == BlockType.ORDERED_LIST:
            block_text = block.split('\n')
            blockChildNodes = []

            for text in block_text:
                text = text.split(".", 1)[1].strip()
                childNodes = text_to_children(text)
                blockChildNodes.append(ParentNode('li', childNodes))

            nodes.append(ParentNode('ol', blockChildNodes))

        else:
            raise ValueError("Invaild block type")

    return ParentNode('div', nodes)

def text_to_children(text):
    textNodes = text_to_textnode(text)
    childNodes = []

    for textNode in textNodes:
        childNodes.append(text_node_to_html_node(textNode))

    return childNodes

from textnode import TextType, TextNode
from regex import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:

    split_text: list[TextNode] = []

    for node in old_nodes:
        if node.text_type != text_type.TEXT:
            split_text.append(node)
            continue

        new_node = node.text.split(delimiter)

        if len(new_node) % 2 == 0:
            raise Exception("invaild markdown syntax")

        for inner_node in range(len(new_node)):
            if inner_node % 2 == 0:
                split_text.append(TextNode(new_node[inner_node], TextType.TEXT))

            else:
                split_text.append(TextNode(new_node[inner_node], text_type))

    return split_text


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_node = []

    for node in old_nodes:

        if node.text_type != TextType.TEXT:
            new_node.append(node)
            continue

        remaining_text = node.text
        matches = extract_markdown_images(node.text)

        if len(matches) == 0:
            new_node.append(node)
            continue


        for i in range(len(matches)):
            split_text = remaining_text.split(f"![{matches[i][0]}]({matches[i][1]})")
            if split_text[0] != "":
                new_node.append(TextNode(split_text[0], TextType.TEXT))

            new_node.append(TextNode(matches[i][0], TextType.IMAGE, matches[i][1]))
            remaining_text = split_text[1]
        if remaining_text != "":
            new_node.append(TextNode(remaining_text, TextType.TEXT))
    return new_node

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_node = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_node.append(node)
            continue

        remaining_text = node.text
        matches = extract_markdown_links(node.text)

        if len(matches) == 0:
            new_node.append(node)
            continue


        for i in range(len(matches)):
            split_text = remaining_text.split(f"[{matches[i][0]}]({matches[i][1]})")
            if split_text[0] != "":
                new_node.append(TextNode(split_text[0], TextType.TEXT))

            new_node.append(TextNode(matches[i][0], TextType.LINK, matches[i][1]))
            remaining_text = split_text[1]

        if remaining_text != "":
            new_node.append(TextNode(remaining_text, TextType.TEXT))
    return new_node

def text_to_textnode(text) -> list[TextNode]:

    results:list[TextNode] = [TextNode(text, TextType.TEXT)]
    results = split_nodes_delimiter(results, "**", TextType.BOLD)
    results = split_nodes_delimiter(results, "_", TextType.ITALIC)
    results = split_nodes_delimiter(results, "`", TextType.CODE)
    results = split_nodes_image(results)
    results = split_nodes_link(results)

    return results

from enum import Enum

class BlockType(Enum):
     PARAGRAPH = "paragraph"
     HEADING = "heading"
     CODE = "code"
     QUOTE = "quote"
     UNORDERED_LIST = "unordered_list"
     ORDERED_LIST = "ordered_list"

def block_to_block_type(markdown):
    count = 0
    block_type = None

    result = ""

    for character in markdown:
        if character == '#' and result == "":
            count += 1

        else:
            result += character

    if count > 0 and count <= 6 and  count < len(markdown) and markdown[count] == " ":
        block_type = BlockType.HEADING

    if markdown.startswith("```") and markdown.endswith("```"):
        block_type = BlockType.CODE

    if block_type != BlockType.HEADING and block_type != BlockType.CODE:
        lines = markdown.split("\n")
        count = 1

        for line in lines:
            if line.startswith(">") and block_type != BlockType.UNORDERED_LIST and block_type != BlockType.ORDERED_LIST:
                block_type = BlockType.QUOTE

            elif line.startswith("- ") and block_type != BlockType.QUOTE and block_type != BlockType.ORDERED_LIST:
                block_type = BlockType.UNORDERED_LIST

            elif line.startswith(f"{count}. ") and block_type != BlockType.QUOTE and block_type != BlockType.UNORDERED_LIST:
                block_type = BlockType.ORDERED_LIST
                count += 1

            else:
                block_type = None
                break

    if block_type == None:
        block_type = BlockType.PARAGRAPH

    return block_type

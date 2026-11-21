import unittest
from splitblocks import markdown_to_blocks
from blocks import BlockType, block_to_block_type

class TestBlockType(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = "# Heading\n\nParagraph\n\n- Item 1\n- Item 2"

        expected = [
            "# Heading",
            "Paragraph",
            "- Item 1\n- Item 2"
        ]

        self.assertEqual(markdown_to_blocks(markdown), expected)


    def test_markdown_to_blocks_empty_lines(self):
        markdown = "\n\n# Heading\n\n\n\nParagraph\n\n"

        expected = [
            "# Heading",
            "Paragraph"
        ]

        self.assertEqual(markdown_to_blocks(markdown), expected)


    def test_markdown_to_blocks_single_block(self):
        markdown = "Just one paragraph"

        expected = ["Just one paragraph"]

        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_paragraph(self):
        block = "This is a paragraph."
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_heading(self):
        block = "# This is a heading"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.HEADING)

    def test_heading_level_6(self):
        block = "###### Heading 6"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.HEADING)

    def test_code(self):
        block = "```\nprint('Hello World')\n```"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.CODE)

    def test_quote(self):
        block = "> This is a quote"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.QUOTE)

    def test_quote_multiple_lines(self):
        block = "> First line\n> Second line\n> Third line"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.QUOTE)

    def test_unordered_list(self):
        block = "- First item\n- Second item\n- Third item"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        block = "1. First item\n2. Second item\n3. Third item"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.ORDERED_LIST)

    if __name__ == "__main__":
        unittest.main()

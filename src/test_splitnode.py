import unittest
from textnode import TextNode, TextType
from splitnode import split_nodes_delimiter, split_nodes_image, split_nodes_link

class TestSplitNodes(unittest.TestCase):

    def test_split_bold(self):
        node = TextNode("This is **bold** text", TextType.TEXT)

        result = split_nodes_delimiter([node], "**", TextType.BOLD)

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT)
        ]
        self.assertEqual(result, expected)

    def test_split_italic(self):
        node = TextNode("This is *italic* text", TextType.TEXT)

        result = split_nodes_delimiter([node], "*", TextType.ITALIC)

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT)
        ]

        self.assertEqual(result, expected)

    def test_invalid_markdown(self):
        node = TextNode("This is **bold text", TextType.TEXT)

        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)


    def test_split_nodes_image_no_images(self):
        node = TextNode("Hello world", TextType.TEXT)

        result = split_nodes_image([node])

        self.assertEqual(result, [node])

    def test_split_nodes_link_no_links(self):
        node = TextNode("Hello world", TextType.TEXT)

        result = split_nodes_link([node])

        self.assertEqual(result, [node])


if __name__ == "__main__":
    unittest.main()

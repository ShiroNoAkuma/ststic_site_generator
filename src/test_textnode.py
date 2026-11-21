import unittest
from textnode import TextNode, TextType, text_node_to_html_node
from splitnode import text_to_textnode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_different_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://google.com")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_different_text_type(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_plain_text(self):
        text = "This is plain text"
        results = text_to_textnode(text)
        expected =[ TextNode("This is plain text", TextType.TEXT)]
        self.assertEqual(results, expected)

    def test_bold_text(self):
        text = "This is **bold** text"
        results = text_to_textnode(text)
        expected =[
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT)
        ]
        self.assertEqual(results, expected)

    def test_italic_text(self):
        text = "This is _italic_ text"
        results = text_to_textnode(text)
        expected =[
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT)
        ]
        self.assertEqual(results, expected)

    def test_code_text(self):
        text = "This is `code` text"
        results = text_to_textnode(text)
        expected =[
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" text", TextType.TEXT)
        ]
        self.assertEqual(results, expected)

    def test_image_text(self):
        text = "This is an image ![rick roll](http://i.imgur.com)"
        results = text_to_textnode(text)
        expected =[
            TextNode("This is an image ", TextType.TEXT),
            TextNode("rick roll", TextType.IMAGE, "http://i.imgur.com")
        ]
        self.assertEqual(results, expected)

    def test_link_text(self):
        text = "This is a link [to boot dev](http://boot.dev)"
        results = text_to_textnode(text)
        expected =[
            TextNode("This is a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "http://boot.dev")
        ]
        self.assertEqual(results, expected)

if __name__ == "__main__":
    unittest.main()

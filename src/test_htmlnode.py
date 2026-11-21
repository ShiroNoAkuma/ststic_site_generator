import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHtmlNode(unittest.TestCase):
    def test_props_to_html_empty(self):
        node = HTMLNode("p", "Hello World")
        self.assertEqual(node.props_to_html(),"")

    def test_props_to_html(self):
        node = HTMLNode("a", "Boot.dev", props={"href": "Http://www.boot.dev", "target": "_blank"})
        result = node.props_to_html()
        self.assertNotEqual(result, 'href="http://www.boot.dev" target="_blank"')

    def test_eq(self):
        node = HTMLNode("p", "Hello World")

        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hello World")
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello World")
        self.assertEqual(node.to_html(), "<p>Hello World</p>")

    def test_props_to_html_leaf(self):
        node = LeafNode("p", "Hello World", props={"href": "Http://www.boot.dev"})
        result = node.to_html()
        self.assertEqual(result, '<p href="Http://www.boot.dev">Hello World</p>')

    def test_eq_leaf(self):
        node = LeafNode("p", "Hello World")

        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hello World")
        self.assertIsNone(node.props)

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()

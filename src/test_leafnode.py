import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p","Hi From Test!")
        self.assertEqual(node.to_html(), "<p>Hi From Test!</p>")

    def test_to_html_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(),'<a href="https://www.google.com">Click me!</a>')

    def test_to_html_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_raw_text(self):
        node = LeafNode(None, "This should just be plain html!!!!")
        self.assertEqual(node.to_html(), "This should just be plain html!!!!")

if __name__ == "__main__":
    unittest.main()
import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_ne(self):
        node = TextNode("Do you like my text?", "bold", "google.com")
        node2 = TextNode("I don't like it.", "italic")
        self.assertNotEqual(node, node2)

    def test_texttype(self):
        node = TextNode("Do you like my text?", "bold")
        node2 = TextNode("Do you like my text?", "italic")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()

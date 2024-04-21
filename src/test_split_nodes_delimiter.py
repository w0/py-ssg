import unittest

from split_nodes_delimiter import split_nodes_delimiter
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)


class TestSplitNodes(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", text_type_text, None),
                TextNode("code block", text_type_code, None),
                TextNode(" word", text_type_text, None),
            ],
        )

    def test_begin(self):
        node = TextNode("**Bold** aren't we?", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertEqual(
            new_nodes,
            [
                TextNode("Bold", text_type_bold, None),
                TextNode(" aren't we?", text_type_text, None),
            ],
        )

    def test_end(self):
        node = TextNode("What if I told *you* this was *italic*", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertEqual(
            new_nodes,
            [
                TextNode("What if I told ", text_type_text, None),
                TextNode("you", text_type_italic, None),
                TextNode(" this was ", text_type_text, None),
                TextNode("italic", text_type_italic, None),
            ],
        )

    def test_error(self):
        node = TextNode("This is text with a `code block word", text_type_text)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", text_type_code)


if __name__ == "__main__":
    unittest.main()

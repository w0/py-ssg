import unittest
from text_to_textnode import text_to_textnodes
from textnode import (
    TextNode,
    text_type_bold,
    text_type_image,
    text_type_code,
    text_type_italic,
    text_type_text,
    text_type_link,
)


class TestTextToTextNode(unittest.TestCase):
    def test_eq(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        text_nodes = text_to_textnodes(text)
        self.assertEqual(
            text_nodes,
            [
                TextNode("This is ", text_type_text, None),
                TextNode("text", text_type_bold, None),
                TextNode(" with an ", text_type_text, None),
                TextNode("italic", text_type_italic, None),
                TextNode(" word and a ", text_type_text, None),
                TextNode("code block", text_type_code, None),
                TextNode(" and an ", text_type_text, None),
                TextNode(
                    "image",
                    text_type_image,
                    "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
                ),
                TextNode(" and a ", text_type_text, None),
                TextNode("link", text_type_link, "https://boot.dev"),
            ],
        )


if __name__ == "__main__":
    unittest.main()

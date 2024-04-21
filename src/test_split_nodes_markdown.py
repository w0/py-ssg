import unittest

from split_nodes_markdown import split_nodes_image, split_nodes_links
from textnode import TextNode


class TestSplitNodesMarkdown(unittest.TestCase):
    def test_eq_images(self):
        node = TextNode(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            "text",
        )
        new_nodes = split_nodes_image([node])
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with an ", "text"),
                TextNode(
                    "image",
                    "image",
                    "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
                ),
                TextNode(" and another ", "text"),
                TextNode(
                    "second image",
                    "image",
                    "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png",
                ),
            ],
        )

    def test_eq_links(self):
        node = TextNode(
            "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)",
            "text",
        )
        new_nodes = split_nodes_links([node])
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", "text"),
                TextNode("link", "link", "https://www.example.com"),
                TextNode(" and ", "text"),
                TextNode("another", "link", "https://www.example.com/another"),
            ],
        )


if __name__ == "__main__":
    unittest.main()

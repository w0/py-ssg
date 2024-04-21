import unittest

from split_nodes_markdown import (
    extract_markdown_images,
    extract_markdown_links
)

class TestExtractMarkdown(unittest.TestCase):
    def test_images(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        images = extract_markdown_images(text)
        self.assertEqual(images,
                         [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")]
                        )
    
    def test_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        links = extract_markdown_links(text)
        self.assertEqual(links,
                         [("link", "https://www.example.com"), ("another", "https://www.example.com/another")])


if __name__ == "__main__":
    unittest.main()
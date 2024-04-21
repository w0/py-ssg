import unittest
from markdown_blocks import (
    markdown_to_blocks,
    block_to_block_type,
    block_type_code,
    block_type_heading,
    block_type_olist,
    block_type_paragraph,
    block_type_quote,
    block_type_ulist,
)


class TestMarkdownToBlocks(unittest.TestCase):
    def test_eq(self):
        test = """This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(test)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_block_types(self):
        self.assertEqual(block_to_block_type("# Heading"), block_type_heading)
        self.assertEqual(block_to_block_type(">My Quote!\n>Is Cool!"), block_type_quote)
        self.assertEqual(block_to_block_type("Here in my garage."), block_type_paragraph)
        self.assertEqual(block_to_block_type("* Dog Food\n* Cat Food"), block_type_ulist)
        self.assertEqual(block_to_block_type("```Code```"), block_type_code)
        self.assertEqual(block_to_block_type("1. Uno.\n2. Dos.\n3. Tres."), block_type_olist)


if __name__ == "__main__":
    unittest.main()

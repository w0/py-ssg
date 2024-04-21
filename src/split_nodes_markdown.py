from textnode import TextNode, text_type_text, text_type_image, text_type_link
import re


def extract_markdown_images(text):
    exp = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(exp, text)

    return matches


def extract_markdown_links(text):
    exp = r"\[(.*?)\]\((.*?)\)"
    matches = re.findall(exp, text)

    return matches


def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        extracted = extract_markdown_images(node.text)

        if len(extracted) == 0:
            new_nodes.append(node)
            continue

        node_text = node.text

        for image in extracted:
            splits = node_text.split(f"![{image[0]}]({image[1]})", 1)

            node_text = splits[1]

            if splits[0] != "":
                new_nodes.append(TextNode(splits[0], text_type_text))

            new_nodes.append(TextNode(image[0], text_type_image, image[1]))

        if node_text != "":
            new_nodes.append(TextNode(node_text, text_type_text))

    return new_nodes


def split_nodes_links(old_nodes):
    new_nodes = []

    for node in old_nodes:
        extracted = extract_markdown_links(node.text)

        if len(extracted) == 0:
            new_nodes.append(node)
            continue

        node_text = node.text

        for link in extracted:
            splits = node_text.split(f"[{link[0]}]({link[1]})", 1)

            node_text = splits[1]

            if splits[0] != "":
                new_nodes.append(TextNode(splits[0], text_type_text))

            new_nodes.append(TextNode(link[0], text_type_link, link[1]))

        if node_text != "":
            new_nodes.append(TextNode(node_text, text_type_text))

    return new_nodes

from textnode import TextNode, text_type_text


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    def build_nodelist(node):

        split_text = node.text.split(delimiter)

        if len(split_text) % 2 == 0:
            raise Exception("Invalid Markdown Syntax. Missing closing delimiter.")

        tmp_list = []

        for i, chunk in enumerate(split_text):
            if chunk == "":
                continue

            if i % 2 == 0:
                tmp_list.append(TextNode(chunk, text_type_text))
            else:
                tmp_list.append(TextNode(chunk, text_type))

        return tmp_list

    new_nodes = []

    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue

        new_nodes.extend(build_nodelist(node))

    return new_nodes

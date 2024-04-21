class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        html = ""

        for key, value in self.props.items():
            html += f' {key}="{value}"'

        return html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes require a value.")
        if self.tag is None:
            return self.value

        html = f"<{self.tag}"
        if self.props:
            html += self.props_to_html()

        html += f">{self.value}</{self.tag}>"

        return html


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag is required")
        if self.children is None:
            raise ValueError("Child are required to be a parent")

        html = []

        for node in self.children:
            html.append(node.to_html())

        return f"<{self.tag}>{"".join(html)}</{self.tag}>"


class HTMLNode:

    def __init__(self, tag, value, chilren=None, props=None ):
        self.tag = tag
        self.value = value
        self.children:list[HTMLNode] = chilren
        self.props:dict = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        return_str = ""
        if self.props is None:
            return ""

        for item, value in self.props.items():
            return_str += f'{item}="{value}" '

        return return_str.rstrip()

    def __repr__(self):
        print(f'HTMLNode \n'
            f'  tag: {self.tag}\n'
            f'  value: {self.value}\n'
            f'  children: {self.children}\n'
            f'  props: {self.props}')


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")

        elif self.tag is None:
            return self.value



        if self.props:
            props_str = ""
            for key, value in self.props.items():
                props_str += f' {key}="{value}"'

            return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"

        return f"<{self.tag}>{self.value}</{self.tag}>"

        def __repr__(self):
            print(f'LeafNode \n'
                f'  tag: {self.tag}\n'
                f'  value: {self.value}\n'
                f'  props: {self.props}')

class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):

        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("parent node must have a tag")

        if self.children is None:
            raise ValueError("parent node must have children")

        if self.children:
            child_html = ""

            for child in self.children:
                child_html += child.to_html()

            return f"<{self.tag}>{child_html}</{self.tag}>"

from BlockToHtml import markdown_to_html_node

def extract_title(markdown):
    markdown_nodes = markdown_to_html_node(markdown)
    for node in markdown_nodes.children:
      if node.tag == 'h1':
         return node.children[0].value

    raise Exception("there is no h1 header")

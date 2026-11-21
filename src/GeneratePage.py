import os
from ExtractTitle import extract_title
from BlockToHtml import markdown_to_html_node

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    if os.path.isfile(from_path):
        with open(from_path, "r") as f:
            read_file = f.read()

    if os.path.isfile(template_path):
        with open(template_path, "r") as f:
            read_template = f.read()

    html_string = markdown_to_html_node(read_file).to_html()

    title = extract_title(read_file)
    content = html_string

    read_template = read_template.replace("{{ Title }}", title)
    read_template = read_template.replace("{{ Content }}", content)

    os.makedirs(os.path.dirname(dest_path) or ".", exist_ok=True)

    with open(dest_path, "w") as f:
            f.write(read_template)

def generate_page_recursive(dir_path_content, template_path, dest_dir_path='/public'):
    print(f"Generating page from {dir_path_content} to {dest_dir_path} using {template_path}")

    for item in os.listdir(dir_path_content):
        full_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)

        if os.path.isdir(full_path):
            os.makedirs(dest_path, exist_ok=True)
            generate_page_recursive(full_path, template_path, dest_path)

        elif os.path.isfile(full_path):

            with open(full_path, "r") as f:
                read_file = f.read()

            if os.path.isfile(template_path):
                with open(template_path, "r") as f:
                    read_template = f.read()

            html_string = markdown_to_html_node(read_file).to_html()

            title = extract_title(read_file)
            content = html_string

            read_template = read_template.replace("{{ Title }}", title)
            read_template = read_template.replace("{{ Content }}", content)

            dest_path = os.path.splitext(dest_path)[0] + ".html"

            os.makedirs(os.path.dirname(dest_path) or ".", exist_ok=True)

            with open(dest_path, "w") as f:
                f.write(read_template)

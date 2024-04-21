from markdown_blocks import markdown_to_blocks, markdown_to_html_node
import os

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    if blocks[0].startswith("# "):
        return blocks[0].strip("#   ")
    
    raise Exception("All pages need a single h1 header.")
    

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as reader:
        markdown = reader.read()

    with open(template_path, "r") as reader:
        template = reader.read()

    html_nodes = markdown_to_html_node(markdown)
    html = html_nodes.to_html()

    title = extract_title(markdown)

    page = template.replace('{{ Title }}', title)
    page = page.replace("{{ Content }}", html)

    with open(dest_path, "x") as writer:
        writer.write(page)
    

def generate_page_recursive(dir_path_content, template_path, dest_dir_path):

    dir_items = os.listdir(dir_path_content)

    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for item in dir_items:
        print(f"WORKING ON {item}")
        in_item = os.path.join(dir_path_content, item)

        if os.path.isfile(in_item):
            split_name = item.split(".")
            new_name = f"{split_name[0]}.html"
            
            out_file = os.path.join(dest_dir_path, new_name)
            generate_page(in_item, template_path, out_file)
        else:
            out_dir = os.path.join(dest_dir_path, item)
            generate_page_recursive(in_item, template_path, out_dir)


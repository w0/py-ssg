import os, shutil
from copy_static import copy_static
from generate_page import generate_page_recursive


def main():

    cwd = os.getcwd()

    static_dir = os.path.join(cwd, "static")
    public_dir = os.path.join(cwd, "public")

    if not os.path.exists(static_dir):
        raise FileNotFoundError("static content directory not found.")

    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)

    copy_static(static_dir, public_dir)

    content_dir = os.path.join(cwd, "content")
    template_html = os.path.join(cwd, "template.html")

    generate_page_recursive(content_dir, template_html, public_dir)    

    



if __name__ == "__main__":
    main()

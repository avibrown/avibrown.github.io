#!/usr/bin/env python3

import markdown
import os

def convert_md_to_html(md_file_path, html_file_path):
    with open(md_file_path, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()
        html_content = markdown.markdown(md_content, extensions=['markdown.extensions.fenced_code', 'mdx_math'])

    html_template = f"""
    <div style="font-family: 'Consolas', 'Courier New', monospace;">
        {html_content}
    </div>
    """

    with open(html_file_path, 'w', encoding='utf-8') as html_file:
        html_file.write(html_template)

def convert_all_md_in_directory(source_dir, target_dir):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for filename in os.listdir(source_dir):
        if filename.endswith('.md'):
            md_file_path = os.path.join(source_dir, filename)
            html_filename = filename.replace('.md', '.html')
            html_file_path = os.path.join(target_dir, html_filename)
            convert_md_to_html(md_file_path, html_file_path)
            print(f"Converted {filename} to {html_filename}")

source_directory = '/home/avi/Documents/GitHub/avibrown.github.io/blogs'
target_directory = '/home/avi/Documents/GitHub/avibrown.github.io/html'
convert_all_md_in_directory(source_directory, target_directory)
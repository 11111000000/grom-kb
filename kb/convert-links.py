#!/usr/bin/env python3
"""Convert Obsidian WikiLinks AND fix relative markdown links for MkDocs."""
import re
import os
import sys

VAULT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {'.git', '.obsidian', '.github', 'kb', 'site', 'node_modules'}

def build_page_map():
    page_map = {}
    for root, dirs, files in os.walk(VAULT_DIR):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith('.')]
        for f in files:
            if f.endswith('.md'):
                full = os.path.join(root, f)
                rel = os.path.relpath(full, VAULT_DIR)
                title = f[:-3]
                page_map[title] = rel
                page_map[rel] = rel
    return page_map

def convert_wikilinks(content, page_map, current_dir):
    def replace_link(match):
        inner = match.group(1)
        if '|' in inner:
            link, text = inner.rsplit('|', 1)
        else:
            link = inner
            text = inner
        link = link.split('#')[0]
        if not link:
            return match.group(0)
        link_lower = link.lower()
        for title, path in page_map.items():
            if title.lower() == link_lower or title == link:
                rel = os.path.relpath(path, current_dir)
                return f'[{text}]({rel})'
        return f'[{text}]({link})'
    return re.sub(r'(?<!!)\[\[([^\]]+)\]\]', replace_link, content)

def fix_md_links(content, page_map, current_dir):
    def fix_link(match):
        text = match.group(1)
        url = match.group(2)
        anchor = match.group(3) or ''
        if url.startswith(('http://', 'https://', 'mailto:')) or url.startswith('#'):
            return match.group(0)
        # Try to resolve
        file_part = url.split('#', 1)[0]
        if not file_part or '/' not in file_part:
            return match.group(0)
        file_lower = file_part.lower().replace('.md', '')
        for title, path in page_map.items():
            title_lower = title.lower()
            if title_lower == file_lower or title_lower.endswith('/' + file_lower):
                resolved = os.path.relpath(path, current_dir)
                return f'[{text}]({resolved}{anchor})'
        return match.group(0)
    return re.sub(r'\[([^\]]*)\]\(([^)]+?)(#[^)]*)?\)', fix_link, content)

def process_file(filepath, page_map):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    rel = os.path.relpath(filepath, VAULT_DIR)
    current_dir = os.path.dirname(rel)
    new_content = convert_wikilinks(content, page_map, current_dir)
    new_content = fix_md_links(new_content, page_map, current_dir)
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  Fixed: {rel}")

def main():
    print("Converting Obsidian links → MkDocs-compatible links...")
    page_map = build_page_map()
    print(f"  Found {len(page_map)} pages")
    count = 0
    for root, dirs, files in os.walk(VAULT_DIR):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith('.')]
        for f in files:
            if f.endswith('.md'):
                process_file(os.path.join(root, f), page_map)
                count += 1
    print(f"  Processed {count} files")

if __name__ == '__main__':
    main()
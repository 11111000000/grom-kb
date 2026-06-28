#!/usr/bin/env python3
"""Convert Obsidian WikiLinks AND fix relative markdown links for MkDocs."""
import re
import os

VAULT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {'.git', '.obsidian', '.github', 'kb', 'site', 'node_modules'}

def build_page_map():
    """Map each page to its vault-relative path. Keys: title, no-ext path, with-ext path."""
    page_map = {}
    for root, dirs, files in os.walk(VAULT_DIR):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith('.')]
        for f in files:
            if not f.endswith('.md'):
                continue
            full = os.path.join(root, f)
            rel_with_ext = os.path.relpath(full, VAULT_DIR)
            rel_no_ext = rel_with_ext[:-3]
            title = f[:-3]
            for key in (title, rel_no_ext, rel_with_ext, rel_with_ext.lower(), rel_no_ext.lower(), title.lower()):
                if key not in page_map:
                    page_map[key] = rel_with_ext
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
        candidates = [link, link_lower, link + '.md']
        for c in candidates:
            if c in page_map:
                resolved = os.path.relpath(page_map[c], current_dir)
                return f'[{text}]({resolved})'
        return f'[{text}]({link})'
    return re.sub(r'(?<!!)\[\[([^\]]+)\]\]', replace_link, content)

def fix_md_links(content, page_map, current_dir):
    def fix_link(match):
        text = match.group(1)
        url = match.group(2)
        anchor = match.group(3) or ''
        if url.startswith(('http://', 'https://', 'mailto:')) or url.startswith('#'):
            return match.group(0)
        # Split file from anchor
        if '#' in url:
            file_part, _, frag = url.partition('#')
            anchor = '#' + frag
        else:
            file_part = url
        if not file_part:
            return match.group(0)
        # Strip .md extension from candidate
        candidate = file_part[:-3] if file_part.lower().endswith('.md') else file_part
        candidate_lower = candidate.lower()
        # Try multiple lookup keys
        candidates = [
            candidate,
            candidate_lower,
            candidate + '.md',
            candidate_lower + '.md',
        ]
        for c in candidates:
            if c in page_map:
                resolved = os.path.relpath(page_map[c], current_dir)
                return f'[{text}]({resolved}{anchor})'
        # Try resolving as relative path
        if not candidate.startswith('/'):
            rel_path = os.path.normpath(os.path.join(current_dir, candidate))
            rel_no_ext = rel_path[:-3] if rel_path.lower().endswith('.md') else rel_path
            for c in (rel_no_ext, rel_path):
                if c in page_map or c + '.md' in page_map:
                    actual = c if c in page_map else c + '.md'
                    new_rel = os.path.relpath(page_map[actual], current_dir)
                    return f'[{text}]({new_rel}{anchor})'
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
    print(f"  Found {len(page_map)} entries ({len(set(page_map.values()))} unique pages)")
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
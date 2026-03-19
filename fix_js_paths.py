import os
import glob
import re

base_dir = r"c:\Users\Khale\Downloads\ver-pages\ver-pages"

assets_dir = os.path.join(base_dir, "assets")
images_dir = os.path.join(assets_dir, "images")
videos_dir = os.path.join(assets_dir, "videos")

img_files = os.listdir(images_dir) if os.path.isdir(images_dir) else []
vid_files = os.listdir(videos_dir) if os.path.isdir(videos_dir) else []

text_files = []
for ext in ('*.html', '*.js', '*.css'):
    text_files.extend(glob.glob(os.path.join(base_dir, "**", ext), recursive=True))

for text_file in text_files:
    rel_path_to_root = os.path.relpath(base_dir, os.path.dirname(text_file)).replace('\\', '/')
    
    try:
        with open(text_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        continue
        
    modified = False
    
    def process_files(content, modified, file_list, asset_path):
        for f_name in file_list:
            f_name_esc = re.escape(f_name)
            
            # Match quotes: ' or " or `
            # Match optional old path prefixes: images/ or dassa1_files/ or ./
            # E.g. image: 'iftarramdan.jpg' -> image: 'assets/images/iftarramdan.jpg'
            # We don't want to replace if it already starts with assets/
            p = r'([\'"`])(?!assets/)(?:images/|dassa1_files/|\./)?(' + f_name_esc + r')\1'
            new_ref = asset_path + "/" + f_name
            
            if rel_path_to_root != '.':
                new_ref = rel_path_to_root + '/' + new_ref
                
            new_content = re.sub(p, r'\g<1>' + new_ref.replace('\\', '\\\\') + r'\1', content)
            if new_content != content:
                content = new_content
                modified = True
        return content, modified

    content, modified = process_files(content, modified, img_files, 'assets/images')
    content, modified = process_files(content, modified, vid_files, 'assets/videos')
                
    if modified:
        with open(text_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {text_file}")

print("Done.")

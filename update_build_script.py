path = r'C:\Users\bigbi\.gemini\antigravity\scratch\ilb-enterprise-pm\build_with_landmark_bldgs.py'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

old_header = '<header class="card-bezel sticky top-3 z-40">'
new_header = '<header class="card-bezel relative z-20 mb-2">'

if old_header in text:
    text = text.replace(old_header, new_header)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("build script updated with relative header.")

path = r'C:\Users\bigbi\.gemini\antigravity\scratch\ilb-enterprise-pm\index.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

fav_code = '<link rel="icon" href="data:image/svg+xml,<svg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 24 24\' fill=\'%23E5A93C\'><path d=\'M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5\'/></svg>">'

if 'favicon' not in text:
    text = text.replace('<head>', '<head>\n  ' + fav_code)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Favicon added cleanly.")
else:
    print("Favicon already present.")

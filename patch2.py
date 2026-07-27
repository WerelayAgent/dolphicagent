import re
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace all inline styles that contain opacity:0
html = re.sub(r'style="[^"]*opacity:0[^"]*"', '', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

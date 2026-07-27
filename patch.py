import re
import os

filepath = 'index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# Task 3: Strip Next.js scripts that cause hydration crash
# Remove <script ...>...</script> where src contains _next
html = re.sub(r'<script\b[^>]*src=[\"\']/?_next/[^>]*>.*?</script>', '', html, flags=re.DOTALL)
# Remove next_f.push scripts
html = re.sub(r'<script>\(self.__next_f.*?</script>', '', html, flags=re.DOTALL)
html = re.sub(r'<script>self.__next_f.push.*?</script>', '', html, flags=re.DOTALL)

# Task 4: Rebranding Text Replacements
html = html.replace('Delphic Arena', 'Dolphic Agent')
html = html.replace('Delphic', 'Dolphic')
html = html.replace('delphicarena.com', 'dolphicagent.com')
html = html.replace('delphic', 'dolphic')
html = html.replace('0xAA730F8cca8A22600f92d854322C560390FCff87', 'coming soon on pump.fun')
html = html.replace('did:delphic:iris_7F21', 'did:dolphic:agent_7F21')
# Rebrand Twitter links
html = html.replace('https://twitter.com/delphicarena', 'https://x.com/dolphicagent')
html = html.replace('https://x.com/delphicarena', 'https://x.com/dolphicagent')
html = html.replace('x.com/delphicarena', 'x.com/dolphicagent')

# Task 5: Redirect Login buttons to signup.html
html = html.replace('href="/login?redirect=/dashboard"', 'href="signup.html"')
html = html.replace('href="/dashboard"', 'href="signup.html"')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
print('Scrubbed and rebranded index.html')

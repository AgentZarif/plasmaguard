s = open('index.html', encoding='utf-8').read()

start = s.index('<style>')
end = s.index('</style>') + len('</style>')

new_css = open('_new_style.css', encoding='utf-8').read()

s = s[:start] + new_css + s[end:]
open('index.html', 'w', encoding='utf-8').write(s)
print("CSS replaced OK")

from duckduckgo_search import ddg

for r in ddg('Sausages'):
    print(r['href'] + ' - ' + r['body'])
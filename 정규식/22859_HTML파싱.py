import re

html_code=input()
html_code=html_code[len('<main>'):-len('</main>')]
html_code = re.sub(r'<div +title="([\w ]*)">',r'title : \1\n',html_code)
html_code = re.sub(r'</div>','',html_code)
html_code = re.sub(r'<p>', '', html_code)  
html_code = re.sub(r'</p>', '\n', html_code)  
html_code = re.sub(r'<[a-z ]*>','',html_code)
html_code = re.sub(r'</[a-z ]*>','',html_code)
html_code = re.sub(r' {2,}', ' ', html_code)
print(html_code.rstrip())
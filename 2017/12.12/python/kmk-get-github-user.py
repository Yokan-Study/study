import requests

r = requests.get('https://api.github.com/users/mksweetlife')

j = r.json()

name = j['name']
blog = j['blog']
html_url = j['html_url']

if not blog:
    print name + '/ ' + html_url

elif blog:
    print name + '/ ' + blog 






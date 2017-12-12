import requests

def getUser(username):
    res = requests.get('https://api.github.com/users/{0}'.format(username))
    body = res.json()

    if body['name'] is not None:
        name = body['name']
    else:
        name = body['login']
    
    if body['blog'] != '':
        blog = body['blog']
    else:
        blog = body['html_url']
        
    return '{0} / {1}'.format(name, blog)

print(getUser('jya9055'))
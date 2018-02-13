import requests
headers = {'Authorization': 'Basic d3d3X2Zyb250Ok9HWmpaRGs0TXpReU5qZGlPVEkzTXpBell6YzFaVFV5WkRaaE1HUXg='}
r = requests.get('https://gapi.gabia.com/roadcode', headers=headers)

print(r)
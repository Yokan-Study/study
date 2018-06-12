import urllib.request
with urllib.request.urlopen("http://admin2.gabia.com/voc/improve/getData/service_imp_list_data.php") as url:

    r = url.read()
print(r)
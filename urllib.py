import urllib.request
print('FYCS 61')
webUrl=urllib.request.urlopen('https://wordpress.org/plugins/about/readme.txt')
print("RESULT CODE :"+str(webUrl.getcode()))
data=webUrl.read()
print(data)

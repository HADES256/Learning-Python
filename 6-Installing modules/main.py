import urllib3


http = urllib3.PoolManager()

url = 'https://hades256.github.io/'
resp = http.request('HEAD', url)

print(resp.headers['Server'])
print(resp.headers['Date'])
print(resp.headers['Content-Type'])
print(resp.headers['Last-Modified'])
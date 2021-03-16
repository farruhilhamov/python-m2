from os import write
import requests

res = requests.get('https://scotch.io')

r = requests.post('https://httpbin.org/post', data = {'key':'value'})

r = requests.put('https://httpbin.org/put', data = {'key':'value'})  
r = requests.delete('https://httpbin.org/delete')  
r = requests.head('https://httpbin.org/get')  
r = requests.options('https://httpbin.org/get') 

r = requests.get("https://micros.uz/")
with open("test.html","w")as f:
    f.write(str(r.text))
print(res)
print(r.raw)
#print(res.headers)
#print(res.text)

print(r)
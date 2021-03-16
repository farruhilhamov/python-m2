#bot1619417250:AAE8h2BCvljeHSRKft1xwY_q9rernD4QaNA
import json 
from flask import Flask
import requests 
def main():
    token = "xU7syV8Vbc9zoZwdEXfYEYwuGkoatRNm49U_e3awwfY"
    url = 'https://avwx.rest/api/metar/location?options=&airport=true&reporting=true&format=json&onfail=cache&'
    putting =requests.put(url, data = {'token':token})  
    test = requests.get(url,params={'token':token})
    r = requests.get(putting)
    post = requests.post(url, data = {"token":token})  

    print(post)
    print(test)

if __name__ =="__main__":
    main()
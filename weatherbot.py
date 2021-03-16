#bot1680074948:AAGVcSE-ToArVshcC3hf_JLuwhSmRt52-jo
import avwx
from avwx.current.metar import Metar
import requests as rq
import json

url = ("https://api.telegram.org/bot1680074948:AAGVcSE-ToArVshcC3hf_JLuwhSmRt52-jo/")

jfk_metar = avwx.Metar('KJFK')
hnl_taf = avwx.Taf('PHNL')
print(jfk_metar.update())
print(jfk_metar.raw)
print(hnl_taf.update())
print(hnl_taf.raw)

def getUpdates():
    global r
    global url
    r= rq.get(url+'getUpdates')
    return r.json()

def get_data(items=1):
    global idlist,get,chat_id
    idlist = [43213135,1146053565,785166521]
    get = getUpdates()
    chat_id = get['result'] [-1] ['message'] [ 'chat'] ['id']
    global url
    req= rq.get(url+'getUpdates')
    return req.json()


def sendMetar(chat_id,text='Test'):
    if chat_id in idlist:
        jobj={'chat_id':chat_id,'text':text}
        post = rq.post(url+"sendMessage",json=jobj)
    return post.json()

def wrongcommand(chat_id,text='Test'):
    if chat_id in idlist:
        jobj={'chat_id':chat_id,'text':text}
        post = rq.post(url+"sendMessage",json=jobj)
    return post.json()

def main():
    get_data()
    action = get['result'] [-1] ['message'] ['text']
    print(action)
    action = str(action)
    if action.lower() == 'metar':
        sendMetar(chat_id,text=jfk_metar.raw)
        sendMetar(chat_id,text=jfk_metar.summary)

    elif action.lower() == 'taf':
        sendMetar(chat_id,text=hnl_taf.raw)
        sendMetar(chat_id,text=hnl_taf.summary)
    else:
        wrongcommand(chat_id,text='wrong input try "taf" or "metar"')

if __name__ == "__main__":
    main()
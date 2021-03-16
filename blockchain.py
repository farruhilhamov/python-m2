import json
import os
import hashlib

blocks_dir = os.curdir +'/blocks/'
def get_hash(filename):
    file = open(blocks_dir+filename,"rb").read()
    return hashlib.md5(file).hexdigest()

def write_blocks(name,message,to_whom,prev_hash=""):
    files = os.listdir(blocks_dir)
    files=sorted([int(i) for i in files])
    last_file = files[-1]
    file_name = str(last_file+1)
    prev_hash = get_hash(str(last_file))
    data = {
        'name':name,
        'message': message,
        'to_whom':to_whom,
        "prev_hash":prev_hash
    }
    print(files,file_name,prev_hash)
    with open(blocks_dir+file_name,'w') as f:
        json.dump(data,f,indent=4,ensure_ascii=False)

def check_integrity():
    files = os.listdir(blocks_dir)
    files = sorted([int(i) for i in files])
    res  = []
    for file in files[1:]:
       h = json.load(open(blocks_dir+str(file))) ["prev_hash"] 
       prev_file = str(file-1)
       check_res = ""
       a_hash=get_hash(prev_file)
       if (a_hash==h):
           check_res ="OK"
       else:
           check_res = "CORRUPTED"
       res.append({"block":prev_file,"result":check_res})
    return res

if __name__ == "__main__":
    print(check_integrity())
    w = write_blocks("Ann","Hi,fine.And U?","Anvar")
    
    
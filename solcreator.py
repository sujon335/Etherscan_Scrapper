import json


with open('codeoutput.json') as f:
    data = json.load(f)
for i in range(0,len(data),1):
    code=data[i]["code"].encode('utf-8') 
    name=data[i]["file"]
    sol_file=open("solidityFiles/%s.sol" % name,"w")
    sol_file.write(code)
    sol_file.close()


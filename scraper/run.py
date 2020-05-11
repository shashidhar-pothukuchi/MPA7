from Naked.toolshed.shell import execute_js, muterun_js
import json

def getreviews(pid):
    review_list = []
    for i in range(1,10):
        success = execute_js('app.js',str(i)+'.'+pid)
        if success :
            with open('data/datatemp.json', 'r',encoding="utf8") as f:
                data = json.load(f)
            review_list += data['reviews']

    output = { 
    'reviews' :  review_list
    }
    f = open('data/data'+pid+'.json','w')
    json.dump(output,f,indent=4)
    f.close()


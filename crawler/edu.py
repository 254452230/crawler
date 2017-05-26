import json

with open('leetcode.json') as json_data:
    d = json.load(json_data)
    # print len(d)
    # print d[0].keys()

    for i in range(len(d)): 
        # print d.keys()
        print d[i]['title']
        print d[i]['link']  
        print d[i]['content']
        


import json
import re
from bs4 import BeautifulSoup
 
# with open('./data/item.json') as json_data:
with open('item.json') as json_data:
    d = json.load(json_data)
    # print len(d)
    # print d[0].keys()

    for i in range(len(d)): 
        # print d.keys()
        # print i,':  ',d[i]['title']
        # print d[i]['title']
        # print d[i]['link']
        # print d[i]['tag']
        # print d[i]['similarProblem']
        # print d[i]['content']

        if i==1:
            break 
        # print len(d[i]['tag'])
        # print len(d[i]['similarProblem'])

        # print type(d[i]['tag'])
        # print type(d[i]['similarProblem'])
        # print type(d[i]['title'])
        # print type(d[i]['content'])


        # html_doc=d[i]['tag'][0]
        # soup = BeautifulSoup(html_doc, 'html.parser')
        # print soup.get_text().replace('Subscribe to see which companies asked this question.','')


        # html_doc=d[i]['similarProblem'][0]
        # soup = BeautifulSoup(html_doc, 'html.parser')
        # print soup.get_text().replace('Subscribe to see which companies asked this question.','')



        for key in d[0].keys():
            # print d[i][key]
            if key in ['tag','similarProblem']:
                if len(d[i][key]) !=0:
                    for count in range(len(d[i][key])):
                        html_doc=d[i][key][count]
                        soup = BeautifulSoup(html_doc, 'html.parser')
                        print soup.get_text()
            else:
                html_doc=d[i][key]
                soup = BeautifulSoup(html_doc, 'html.parser')
                print soup.get_text().replace('Subscribe to see which companies asked this question.','')







            

        # demo for getting the text from json using replace() in python
        # print d[i]['content'].replace('<p>','').replace('</p>','')

        # demo for getting the text from json using regular expression
        
        # p = re.compile(r'<.*?>')
        # print p.sub("",d[i]['content'] )


        # demo for getting the text from html using beautifulSoup


        # html_doc=d[i]['content']
        # soup = BeautifulSoup(html_doc, 'html.parser')
        # print soup.get_text().replace('Subscribe to see which companies asked this question.','')




        pass



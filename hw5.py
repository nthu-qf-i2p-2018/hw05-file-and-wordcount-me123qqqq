
# coding: utf-8

# In[42]:


# -*- coding: utf-8 -*-
import csv
import json
def main(filename):
    wordli=[]
    wordlii=[]
    e={}
    a=[]
 
    txtfile = open(filename)
    text=txtfile.read()
    wordli = text.split()
    wordlii=[x.strip(""":;.',!?"-_@#$%^&*=+-/()...""") for x in wordli]    
    
    for x in wordlii:
        e[x]=e.get(x,0)+1
    for key,value in e.items():
        a.append((key,value))
    
    with open('wordcount.csv','w',newline='') as csv_file:
        writer =csv.writer(csv_file)
        # write table head
        writer.writerow(['word', 'count'])
        writer.writerows(a)
       
    with open('wordcount.json','w',newline='') as csv_file:
        json_str = json.dumps(a)
        csv_file.write(json_str)

    # BONUS: dump to a pickle file named "wordcount.pkl"
    # hint: dump the Counter object directly


if __name__ == '__main__':
    main("i_have_a_dream.txt")



# coding: utf-8

# In[45]:


# -*- coding: utf-8 -*-
import csv
import json
import pickle
import collections
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
    f=collections.Counter(e)  
    with open('wordcount.csv','w',newline='') as csv_file:
        writer =csv.writer(csv_file)
        # write table head
        writer.writerow(['word', 'count'])
        writer.writerows(a)
  
    with open('wordcount.json','w',newline='') as csv_file:
        json_str = json.dumps(a)
        csv_file.write(json_str)
    with open('wordcount.pkl','wb') as csv_file:
        pickle.dump(f,csv_file)
   

if __name__ == '__main__':
    main("i_have_a_dream.txt")


# In[26]:





# In[31]:





# In[44]:






# coding: utf-8

# In[1]:


# -*- coding: utf-8 -*-
import csv
import json
import pickle
import string
from collections import Counter
def main(filename):
    file=open(filename)
    lines=file.readlines()
    all_words=[]
    for line in lines:
        words=line.split()
        for word in words:
            word=word.strip(string.punctuation)
            if word:
                all_words.append(word)
    counter=Counter()
    counter.update(all_words)
    with open('wordcount.csv','w',newline='') as csv_file:
        writer =csv.writer(csv_file)
        # write table head
        writer.writerow(['word', 'count'])
        for x,y in counter.most_common():
            writer.writerow([x,y])
    l=list()
    for z,n in counter.most_common():
        aa=[[z,n]]
        l.extend(aa)
    with open('wordcount.json','w') as csv_file:
        json_str = json.dumps(l)
        csv_file.write(json_str)
    with open('wordcount.pkl','wb') as csv_file:
        pickle.dump(counter,csv_file)
   

if __name__ == '__main__':
    main("i_have_a_dream.txt")


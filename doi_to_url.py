#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from timeit import default_timer as timer

lines=[]
dois=[]
urls=[]
urlsadj=[]
i=0

filename=input('What is the name of your file ? ')#get name of file
start=timer()
filename=filename+'.bib'

with open(filename, "rt", encoding='utf-8') as bib:#open file copy text
    for line in bib:
        lines.append(line)
bib.close()

for x in range(len(lines)):#search url and doi
    u = lines[x].find('url =')
    if u == 0:
        urls.append(x)
    n = lines[x].find('doi =')
    if n == 0:
        shits, doi = lines[x].split('{')
        doi, shits = doi.split('}')
        urldoi = 'url = {http://dx.doi.org/'+doi+'},\n'
        dois.append(urldoi)
        
for x in range(len(urls)):#adapt url line number
    urlsadj.append(urls[x]-x)
    
for x in range(len(urlsadj)):#delete url
    lines.remove(lines[urlsadj[x]])
    
for x in range(len(lines)):#insert urldoi
    n = lines[x].find('doi =')
    if n == 0:
        lines.insert(x+1,dois[i])
        i=i+1
        
with open(filename, "w", encoding='utf-8') as bib:#write file
    for x in range(len(lines)):
     bib.write(lines[x])
bib.close()

end=timer()
print('\nAll done, the file was modified in {0} secs.'.format(end-start))

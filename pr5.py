# -*- coding: utf-8 -*-
#Assignment no 5
#Name:Jayavant Warkhade
#Roll no:68
#Batch:B4
#Assignment name: Implement regular expression  to find url,Ip,Pand card number and date.
import re
senetence=""" I am Jayavant Warkhade My PAN id is: AUIJH1234l my laptop ip is 10.200.00.101 and also i have 
i have used bing url for that is https://www.bing.com ,
and my freind also has pan id: PUJKL5263f,and he has gaming laptop
with ip 01.500.20.000 and he using https://www.datacamp.com
for study.date: 12/05/2003"""

#regular expression for url
pat='[a-z]*:\/\/[a-z.]*'
url=re.findall(pat, senetence)
url
#Out[6]: ['https://www.bing.com', 'https://www.datacamp.com']

#regular expression for ip
pat_ip='\d{2}.\d{3}.\d{2}.\d{3}'
ip=re.findall(pat_ip, senetence)
ip
#Out[13]: ['10.200.00.101', '01.500.20.000']

#RE for PAN card Number.
pat_pan='[A-Z]{5}\d{4}.'
pan=re.findall(pat_pan, senetence)
pan
#Out[16]: ['AUIJH1234l', 'PUJKL5263f']

pat_date='\d{2}\/\d+\/\d{4}'
date=re.findall(pat_date, senetence)
date
#Out[26]: ['12/05/2003']
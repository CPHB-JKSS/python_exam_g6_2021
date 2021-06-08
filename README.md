[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/JoakimKSS/python_exam_g6_2021/HEAD) _ Main branch  
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/JoakimKSS/python_exam_g6_2021/tree/postHandin/HEAD) _ postHandin branch


# python_exam_g6_2021
Python exam project for Group no. 6, Spring 2021

### Group
Group 6  
- Joakim Stensnæs			cph-js437	cph-js437@cphbusiness.dk
- Henrik Lønquist Thomasen	cph-92ht	cph-ht92@cphbusiness.dk
- Yones El Bana			cph-ye7		cph-ye7@cphbusiness.dk
- Alex Wagner			cph-aw116	cph-aw116@cphbusiness.dk

Status: Det er lykkedes os, at opfylde alle projektets succeskriterier. I første omgang henter vi talerne ned i transkriberet form.  Vi klargøre og renser efterfølgende talerne ved blandt andet at tokenize, fjerne fyldeord, tegnsætning m.m., for derefter at præsentere data visuelt via wordclouds og plots. Vi foretager en yderligere analyse på talerne, for at få et indtryk om talerne er overvejende positive eller negative og progressionen i de enkelte taler.

User guide: Projektet skal køres i jupyter notebooks i præsentations filen, som tager udgangspunkt i vores importeret moduler, som indeholder alt vores kode og opsætning. 

## Project description


I dette projekt tager vi udgangspunkt i H.M. Dronningens nytårstaler igennem årene 2001 til 2020.  
Vi vil hente talerne fra nettet, bearbejde dem og indentificere statistiske forskelle, samt prøve at angive om der negative eller positive antydninger. Vi vil fremvise disse data på betydningsfulde og let læselige måder med grafer.


##### Data:
Dronnings nytårstaler ligger på nettet i transkriberet form.  
https://www.kongehuset.dk/monarkiet-i-danmark/nytarstaler/hendes-majestat-dronningens-nytarstaler



##### Succeskriterier
1. Data retrieval  
&nbsp;&nbsp;&nbsp;Webscrabing, saving to file/csv.

2. Data preparation  
&nbsp;&nbsp;&nbsp;Analyze speeches, data cleaning, word clouds.

3. Structure analysis  
&nbsp;&nbsp;&nbsp;Recognize patterns, form statistics.

4. Sentiment analysis  
&nbsp;&nbsp;&nbsp;Analyze positive or negative, compare between years and in individual speeches.

5. Data presentation  
&nbsp;&nbsp;&nbsp;Pyplot.


##### Teknologier / libraries
- csv
- pandas
- numpy
- matplotlib
- pyplot
- bs4
- requests
- cv2
- nltk
- Afinn
- Pickle
- Wordcloud

##### Hovedudfordringer
The main challenges bliver helt klart sentiment analysis, da det er relativt nyt stof.

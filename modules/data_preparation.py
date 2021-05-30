import nltk #natural language toolkit
import re #regular expressions
import string #stringfunctions
import datetime #datetime library
import pandas as pd 
from sklearn.feature_extraction.text import CountVectorizer

def download_nltk_stopwords():
    nltk.download('stopwords')
    
def set_danish_stopwords():
    return nltk.corpus.stopwords.words('danish')

def add_custom_stopwords(lst):
    lst.append('år')
    lst.append('må')
    lst.append('kan')
    lst.append('så')
    lst.append('ved')
    lst.append('går')
    lst.append('hele')
    lst.append('både')
    lst.append('bare')
    lst.append('får')
    lst.sort()
    return lst

def add_stopword(lst, word):
    lst.append(word)
    lst.sort()
    return lst

def get_years():
    now = datetime.datetime.now()
    years = []
    year = 2001
    
    while year < now.year:
        
        years.append(year)
        year += 1
    
    return years

def create_data_dict():
    years = get_years()
    data = {}
    file = ""
    
    for i, year in enumerate(years):
        file = 'data/Nytårstalen '+str(year)
        data[str(year)] = clean_speech(open_speech(file))
        
    return data

def data_dict_to_df(data_dict):
    df_data = pd.DataFrame.from_dict(combine_data(data_dict)).transpose()
    df_data.columns = ['speech']
    
    return df_data

def value_to_list(value):
    value_list = ''.join(value)
    
    return value_list

def combine_data(data_dict):
    
    return {key: [value_to_list(value)] for (key, value) in data_dict.items()}


def create_dtm(stopwords,data_df):
    cv_dk = CountVectorizer(stop_words=stopwords) 
    data_cv = cv_dk.fit_transform(data_df.speech)
    data_dtm = pd.DataFrame(data_cv.toarray(), columns=cv_dk.get_feature_names())
    data_dtm.index = data_df.index
    
    return data_dtm
    

def clean_speech(txt):
    txt = txt.lower() #sætter alle karaktere til lower case
    txt = re.sub('\n','', txt) #fjerner alle \n 
    txt = re.sub('\[.*?]','',txt) #fjerner [] og indholdet
    txt = re.sub('\([^)]*\)','',txt) #fjerner () og indholdet
    txt = re.sub('\d', '', txt) #fjerner tal(digits)
    txt = re.sub('[%s]' % re.escape(string.punctuation), '', txt) #fjerner tegn

    return txt

def open_speech(file):
    with open(file) as file_object:
        content = file_object.read()

    return content











    
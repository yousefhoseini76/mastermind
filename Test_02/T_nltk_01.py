import pandas as pd
import re
import string
data_cleaned = pd.read_csv('C:/Users/Yousef/Desktop/temp_py/SMSSpamCollection_cleaned.tsv', sep="\t")
# print(data_cleaned.head())

def remove_punct(text):
    text_nopunct ="".join([char for char in text if char not in string.punctuation])
    return text_nopunct

pd.set_option('display.max_colwidth', 100)
data = pd.read_csv('C:/Users/Yousef/Desktop/temp_py/SMSSpamCollection.tsv', sep="\t", header=None)
data.columns = ['label', 'body_text']

data['body_text_clean'] = data['body_text'].apply(lambda x: remove_punct(x))
# print(data.head())

import nltk
def tokenize(text):
    tokens = re.split('\W+', text)
    return tokens

data['body_text_tokenize'] = data['body_text_clean'].apply(lambda x: tokenize(x.lower()))
# print(data['body_text_tokenize'])

stopwords = nltk.corpus.stopwords.words('english')
def remove_stopword(tokenized_list):
    text = [word for word in tokenized_list if word not in stopwords]
    return text

data['body_text_nostop'] = data['body_text_tokenize'].apply(lambda x: remove_stopword(x))
print(data['body_text_nostop'])

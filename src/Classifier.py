#!/usr/bin/python

from unicodedata import normalize
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm
import nltk
import numpy

nltk.download('rslp')

_ARTICLES = ['a', 'as', 'o', 'os']
_PREPOSITIONS = ['a', 'ante', 'ate', 'apos', 'com', 'contra', 'para', 'per', 'por',\
    'perante', 'sem', 'sob', 'sobre', 'tras', 'na', 'no', 'nas', 'nos']

vectorizer = CountVectorizer()
classifier = svm.SVC(probability=True,kernel='linear')

def remove_accentuation(text):
    return normalize('NFKD', text).encode('ASCII', 'ignore').decode('ASCII')

def remove_useless_words(word_list):
    # remove all words starting with $
    no_parameter_words = [word for word in word_list if word[0] != '$']
    return [word for word in no_parameter_words if word not in _ARTICLES and word not in _PREPOSITIONS]

def replace_nonalphanumeric_by_space(text):
    """ replaces all non alphanumeric chars that are not the $ by space """
    return re.sub(r'[^0-9a-z\$]', ' ', text)

''' 
transform_text:
1. Converts to lower case
2. replaces characters with accentuation by its pure corresponding char
3. replaces all chars that are not letters or numbers or $ by space
4. splits the text into a list of words. The separator is any whitespace char 
5. removes all whitespace chars in the borders of each word
6. removes all articles and prepositions of the list of words
7. stems the remaing words 
'''
def transform_text(text):
    stemmer = nltk.stem.RSLPStemmer()
    no_accentuation_text = remove_accentuation(text.lower())
    only_alphanumeric_text = replace_nonalphanumeric_by_space(no_accentuation_text)
    without_useless = remove_useless_words([word.strip() for word in only_alphanumeric_text.split()])
    return [stemmer.stem(el) for el in without_useless]

def load_classifier():
    fsample = open('samples/training_input.txt', 'r')
    raw_rows = fsample.readlines()
    fsample.close()
    labels = []
    samples = []
    for row in raw_rows:
        splt = row.split()
        if splt:
            labels.append(splt[0])
            samples.append(' '.join(splt[1:]))    
    transformed_samples = [' '.join(transform_text(el)) for el in samples]
    print(transformed_samples)
    matrix = vectorizer.fit_transform(transformed_samples)
    print(matrix.toarray())
    print (labels)
    classifier.fit(matrix, labels)
    print(classifier)

def classify(sentence):
    transformed_sentence = ' '.join(transform_text(sentence))
    data_array = vectorizer.transform([transformed_sentence])
    probabilities = classifier.predict_proba(data_array)[0]
    peak_index = numpy.argmax(probabilities)
    print (probabilities)
    print(probabilities[peak_index])
    result = None
    # empiric: most results that make sense have probability >= 0.56
    if probabilities[peak_index] >= 0.56:
        result = classifier.classes_[peak_index]
    return result
    
load_classifier()

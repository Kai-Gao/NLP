import pandas as pd
import numpy as np
import os
import jieba
import io
from collections import Counter
import matplotlib.pyplot as plt

data_directory = "/Users/shiyi_Lee/Desktop/NLP&AI_Course/NLP/data/extracted/AA"


def get_articles(path):
    """
    read the articles from the path
    :param path:
    :return articles:
    """

    fileNames = os.listdir(path)
    #fileNames = fileNames[0:1]
    all_text = []
    for fileName in fileNames:
        file_path = os.path.join(data_directory, fileName)
        with io.open(file_path, 'r', encoding = 'utf-8') as file:
            article = file.readlines()
        article = [i for i in article if i != '\n']
        all_text += article

    return all_text

def token(string):
    """
    strip punctuation from the string
    :param string:
    :return cleaned string:
    """
    words = re.findall(r'[\w|\d]+|[^x00-xff]+', string)
    words = [word for word in words if word != u' ']
    return  ' '.join(words)


def get_sentence_segment(articles):
    """
    sentence segmented
    :param articles:
    :return words list:
    """
    text = ' '.join([token(i) for i in articles ])
    words_in_article = list(jieba.cut(text))
    return words_in_article

def product(numbers):
    return reduce(lambda n1, n2: n1 * n2, numbers)

def get_prob(word):

    esp = 1 / frequences_sum
    if word in words_count:
        return words_count[word] / frequences_sum
    else:
        return esp

def language_model_one_gram(string):
    words = list(jieba.cut(string))
    return product([get_prob(w) for w in words])


def get_combination_prob(w1, w2):
    if w1 + w2 in _2_gram_counter: return _2_gram_counter[w1+w2] / _2_gram_sum
    else:
        return 1 / _2_gram_sum


def get_prob_2_gram(w1, w2):
    return get_combination_prob(w1, w2) / get_prob(w1)


def langauge_model_of_2_gram(sentence):
    sentence_probability = 1

    words = list(jieba.cut(sentence))

    for i, word in enumerate(words):
        if i == 0:
            prob = get_prob(word)
        else:
            previous = words[i - 1]
            prob = get_prob_2_gram(previous, word)
        sentence_probability *= prob

    return sentence_probability

articles = get_articles(data_directory)
words_in_articles = get_sentence_segment(articles)
words_in_articles = [word for word in words_in_articles if word != u' ']
stop_words =[u'https',
 u'zh',
 u'wikipedia',
 u'org',
 u'wiki',
 u'curid',
 u'47081',
 u'title',
 u'doc',
 u'id',
 u'47081',
 u'url']
words_in_articles = [word for word in words_in_articles if word not in  stop_words]

#remove punctuations
final_result = []
for a in words_in_articles:
    b = re.sub("[\\s\{\}\(\)\（\）\（\）\、\，\。\\\#\$\"\,\.\/\」\「\-\《\》\：\“\”]+".decode("utf-8"), ''.decode('utf-8'), a)
    if len(b) >0:
        final_result.append(b)


words_count = Counter(final_result)

#one gram
frequences_all = [f for w, f in words_count.most_common()]
frequences_sum = sum(frequences_all)
language_model_one_gram('广交会下个月举办')


# 2 gram
valid_tokens = [str(t) for t in final_result]
all_2_grams_words = [''.join(final_result[i:i+2]) for i in range(len(final_result[:-2]))]
_2_gram_sum = len(all_2_grams_words)
_2_gram_counter = Counter(all_2_grams_words)

langauge_model_of_2_gram('小明今天抽奖抽到一台苹果手机')
langauge_model_of_2_gram('小明今天抽奖抽到一台波音飞机')




# with io.open('/Users/shiyi_Lee/Desktop/NLP&AI_Course/NLP/HomeWork/test.txt', 'w', encoding = 'utf-8') as file:
#     #file.write(a)
#     file.write(' '.join(final_result))
# file.close()






















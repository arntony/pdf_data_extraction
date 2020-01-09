
from sklearn.feature_extraction.text import CountVectorizer
import os
from glob import glob
from pdf_data_extraction.extract_pdf_text import ocr_core
import joblib


def build_corpus(filepath):
    origin = os.getcwd()
    os.chdir(filepath)
    filenames = glob('*.jpg')
    corpus = {}
    for i, f in enumerate(filenames):
        corpus[f] = ocr_core(f)
        print('{}. extracted text from - {}'.format(str(i+1).zfill(2), f))
        if i == 10:
            break
    os.chdir(origin)
    joblib.dump(corpus, 'corpus.dat')
    return list(joblib.load('corpus.dat').values())


def text_features(build_corp=False):
    if build_corp:
        build_corpus(r'C:\python_projects\pdf_data_extraction\pdf_data_extraction\pdf_images')
    corpus = list(joblib.load('corpus.dat').values())
    vectorizer = CountVectorizer(analyzer='word', max_features=30)
    vectorizer.fit_transform(corpus)
    features = vectorizer.get_feature_names()
    print(features)
    print(len(features))


# print(build_corpus(r'C:\python_projects\pdf_data_extraction\pdf_data_extraction\pdf_images'))
text_features()
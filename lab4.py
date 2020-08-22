import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import ngram
#import re
#import string
import nltk
from nltk.util import ngrams


dataset_l = np.load('dataset.npy', allow_pickle=True)

words = ' '.join(dataset_l).split(' ')

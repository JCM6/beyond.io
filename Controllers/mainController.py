""".
Predictive Text Generator
The goal of this project is create a predictive text generator for the creation of mtg cards based on minimal text input.
If the implementation allows fo it it may be possible to draft out a generative mtg set to work as a baseline for site design.
"""

import numpy
import sys
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM
from keras.utils import np_utils
from keras.callbacks import ModelCheckpoint


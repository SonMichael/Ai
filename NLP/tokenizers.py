# -*- coding: utf-8 -*-
"""Tokenizers.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Y1c5fsiQDx6vZ1szvCLvY9r76nUp0oJC
"""

from tensorflow.keras.preprocessing.text import Tokenizer

sentences = [
             'I love Vietnam',
             'Vietnamese people are pretty friendly',
             'My mom loves cooking',
             'I am Vietnamese'
]

tokenizer = Tokenizer(num_words=100, oov_token="<OOV>")

tokenizer.fit_on_texts(sentences)

word_index = tokenizer.word_index

word_index

new_sentences = [
    'I love dog',
    'I live in Hanoi'
]

new_sequences = tokenizer.texts_to_sequences(new_sentences)

new_sequences

from tensorflow.keras.preprocessing.sequence import pad_sequences

padding_sequences = pad_sequences(new_sequences)

padding_sequences

!wget --no-check-certificate \
    https://storage.googleapis.com/laurencemoroney-blog.appspot.com/sarcasm.json \
    -O /tmp/sarcasm.json

import json

with open("/tmp/sarcasm.json", 'r') as f:
  data = json.load(f)

for item in data:
  print(item)

sentences = []

for item in data:
  sentences.append(item['headline'])

sentences

tokenizer = Tokenizer(oov_token='<OOV>')
tokenizer.fit_on_texts(sentences)

word_index = tokenizer.word_index

word_index

sequences = tokenizer.texts_to_sequences(sentences)

sequences

padded = pad_sequences(sequences, padding="post")

padded

sequences = tokenizer.texts_to_sequences(new_sentences)

sequences


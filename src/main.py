# -*- coding: utf-8 -*-
'''
Created on 07/03/2015

@author: Roque Lopez
'''
from __future__ import unicode_literals
from corpus_reader import file_reader
from simple_tagger import Simple_Tagger
import os

if __name__ == '__main__':
    st = Simple_Tagger()

    for file_name in os.listdir("../resource/input_data/"):
        print "Analyzing file:", file_name
        sentence_list = file_reader(os.path.join("../resource/input_data/", file_name))
        print st.tag(sentence_list)
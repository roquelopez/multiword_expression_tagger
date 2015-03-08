# -*- coding: utf-8 -*-
'''
Created on 06/03/2015

@author: Roque Lopez
'''
from __future__ import unicode_literals
import re
import codecs

def file_reader(file_path):
    sentence_list = []

    with codecs.open(file_path, 'r','utf-8') as handle:
        lines = handle.readlines()

    sentence = ""

    for line_file in lines:
        pattern = re.match('(.+)\|(.+)\|CC1\|(.+)', line_file)
        if pattern:
            text_line = clean_text(pattern.group(3)).lower()
            sentence += " " + text_line 
            if text_line.endswith('.') or text_line.endswith('?'):
                sentence_list.append(sentence.strip())
                sentence = ""

    return sentence_list

def clean_text(text):
    text = re.sub(r'>{2,3}', '', text)
    text = re.sub(r'Reporter:', '', text)
    return text.strip()
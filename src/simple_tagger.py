# -*- coding: utf-8 -*-
'''
Created on 07/03/2015

@author: Roque Lopez
'''
from __future__ import unicode_literals
import re
import codecs
import MBSP

class Simple_Tagger(object):

    def __init__(self):
        self.__unit_of_time = self.__read_resource("../resource/UNITS_OF_TIME.txt")
        self.__manner_of_motion_verbs = self.__read_resource("../resource/MANNER-OF-MOTION-VERBS.txt")

    def tag(self, sentence_list):
        multiword_expressions = []
        
        for sentence in sentence_list:
            sentence_parsed = MBSP.parse(sentence, chunks=False, relations=False, anchors=False)
            sentence_lemmatized = " ".join([x.split("/")[2] for x in sentence_parsed.split(" ")])
            multiword_expressions += self.__pattern_1(sentence_lemmatized)
            multiword_expressions += self.__pattern_2(sentence_parsed)
            
        return multiword_expressions

    def __pattern_1(self, sentence):
        pattern_list = []
        for uot in self.__unit_of_time:
            for momv in self.__manner_of_motion_verbs:
                pattern = uot + " " + momv
                if re.match('.*\W' + pattern + '\W.*', sentence):
                    print "Pattern Identified:", pattern
                    pattern_list.append(pattern)

        return pattern_list

    def __pattern_2(self, sentence):
        pattern_list = []
        for uot in self.__unit_of_time:
            pattern = re.match('.*as/\w+/as (\w+)/\w+/' + uot + ' (\w+)/\w+/(go|pass) (\w+)/IN.*', sentence)
            if pattern:
                print "Pattern Identified:", "as %s %s %s" % (pattern.group(1), pattern.group(2), pattern.group(4))
                pattern_list.append("as %s %s %s" % (pattern.group(1), pattern.group(2), pattern.group(4)))

        return pattern_list

    def __read_resource(self, file_path):
        tokens_list = []
        with codecs.open(file_path, 'r','utf-8') as handle:
            lines = handle.readlines()

        for line_file in lines:
            tokens_list.append(line_file.strip().lower())

        return tokens_list
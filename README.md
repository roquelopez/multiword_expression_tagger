# Python Tagger for Multiword Expression
## Documentation
Documentation about this idea is available [here](https://sites.google.com/site/distributedlittleredhen/gsoc2015).
## Tasks
-	Reading of the sample corpus. The script extracts the text grouping it in sentences.
-	Using the MBSP tool, POS tags and lemmas of each word in the sentence were obtained.
-	With a little list of unit of time  and manner of motions verbs, the program identifies some multiword expression

## Program
The program (``src/main.py`` module) identifies multiword expressions of time using the patterns 1 and 2 explained [here](https://github.com/RedHenLab/NLP/issues/1).
#### Usage:
``python main.py``

#### Output:

- time fly
- as seconds go by

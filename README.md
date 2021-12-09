CPPDA
===============================
An implementation of CPPDA, a new model for predicting the coding potential of RNA sequences.

Reference
========================
Our manuscipt titled with "Improving the coding potential prediction of RNA sequences with data augmentation" is being reviewed.

Requirements
========================
    [python 2.7](https://www.python.org/downloads/)

Usage
========================
if you want to run the coding potential prediction of RNA sequences without data augmentation, you can run:
python 4CPP.py

if you want to run the coding potential prediction of RNA sequences with data augmentation, you can run:
python 5CPPDA.py

1SelectData.py is used for selecting RNA sequences of ORF length less than 303nt from coding RNAs.

2generateData.py is used for gererating new samples for data augmentation.

3Feature.py is uesd for feature calculation.


Data
=====================
In this work, we use the datasets and part code organized by CPPred(http://www.rnabinding.com/CPPred/).




Contact
=====================
Author: Xian-gan Chen
Maintainer: Xian-gan Chen
Mail: chenxg@mail.scuec.edu.cn
Date: 2021-12-8
School of Biomedical Engineering, South-Central University for Nationalities, China

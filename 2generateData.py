# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 16:20:54 2021

@author: sxg
"""
import random
from Bio import SeqIO
import Bio.SeqIO as Seq

max_len = 50  # 10-60 to p1-p6
max_times = 50
prob = 0.002  #0.001-0.009 to p1-p9
#np.random.seed(0)
random.seed(0)
#1. mutation
def convert_char_mutation(seq_one):
    len_seq = len(seq_one)
    char = ['A','G','C','T']
#    prob = 0.1
    seq_new = ''
    for idx in range(len_seq):
    #    print(idx)
        p = random.random()
        ch_new = random.choice(char)
        ch_old = seq_one[idx]
        if p <= prob:
            seq_new += ch_new
        else:
            seq_new += ch_old
    return seq_new


# 2. insert
def convert_char_insert(seq_one):
    len_seq = len(seq_one)
#    prob = 0.01
    char = ['A','G','C','T']
    seq_new = ''
    for idx in range(len_seq):
    #    print(idx)
        p = random.random()
        ch_new = random.choice(char)
        ch_old = seq_one[idx]
        if p <= prob:
            ch_insert = ch_new + ch_old
            seq_new += ch_insert
        else:
            seq_new += ch_old    
    return seq_new


# 3. delete
def convert_char_delete(seq_one):
    len_seq = len(seq_one)
#    prob = 0.01
    seq_new = ''
    for idx in range(len_seq):
    #    print(idx)
        p = random.random()
        ch_new = ''
        ch_old = seq_one[idx]
        if p <= prob:
            seq_new += ch_new
        else:
            seq_new += ch_old
    return seq_new


# 4. nucleotide fragment reversal
def convert_str_reversal(seq_one):
    len_seq = len(seq_one)
    substr_len = random.randint(2,max_len)
    substr_pos = random.randint(0,len_seq-substr_len)
    
    substr_front = seq_one[:substr_pos]
    substr_re = seq_one[substr_pos:substr_pos+substr_len]
    substr_reversion = substr_re[::-1]
    substr_end = seq_one[substr_pos+substr_len:]
    seq_new = substr_front + substr_reversion + substr_end
    return seq_new


# 5. Nucleotide tandem repeat
def convert_str_repeat(seq_one):
## select a length of substr, select a position, 
## repeat the substr n times, n is a random number in 2-50.
    len_seq = len(seq_one)
    substr_len = random.randint(2,max_len)
    substr_pos = random.randint(0,len_seq-substr_len)
    repeat_times = random.randint(2,max_times)
    
    substr_front = seq_one[:substr_pos]
    substr_re = seq_one[substr_pos:substr_pos+substr_len]
    substr_repeat = substr_re*repeat_times
    substr_end = seq_one[substr_pos+substr_len:]
    seq_new = substr_front + substr_repeat + substr_end
    return seq_new


# 6. delete nucleotide fragments
def convert_str_delete(seq_one):
    len_seq = len(seq_one)
    substr_len = random.randint(2,max_len)
    substr_pos = random.randint(0,len_seq-substr_len)
    
    substr_front = seq_one[:substr_pos]
    substr_end = seq_one[substr_pos+substr_len:]
    seq_new = substr_front + substr_end
    return seq_new


seq_file = 'coding_RNA_sORF.fa'
select_seq = []
i = 0
for id_p in range(40):
    for seq in Seq.parse(seq_file,'fasta'):

        seq_new = seq
        old_data = seq.seq._data
        new_data = convert_char_mutation(old_data)     #1
#        new_data = convert_char_insert(old_data)       #2
#        new_data = convert_char_delete(old_data)       #3
#        new_data = convert_str_reversal(old_data)      #4
#        new_data = convert_str_repeat(old_data)        #5
#        new_data = convert_str_delete(old_data)        #6

        seq_new.seq._data = new_data
        select_seq.append(seq_new)
        i = i + 1
        if(i % 1000 == 0):
            print(i)
filename = 'coding_RNA_sORF_da1p2.fa'        
Seq.write(select_seq,filename,'fasta')
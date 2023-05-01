#!/usr/bin/env python3

def return_evens(num_list):
    remove_odd = [n for n in num_list if n%2 == 0]
    return(remove_odd)

def make_exclamation(sentence_list):
    add_exclamation = [f'{n}!' for n in sentence_list]
    return add_exclamation
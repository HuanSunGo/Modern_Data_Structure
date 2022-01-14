#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pytest
import pandas as pd

def cipher(text, shift, encrypt=True):
    assert isinstance(shift, int), "The type of shift parameter should be an integer."
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text

@pytest.mark.parametrize(
    "text,shift,expected",[
        ("m",1,"n"),
        ("lisa", 1, "mjtb"),
        ("roman", -1, "qnlZm"),
        ("Chef*", 3, "Fkhi*"),])

class Test:
    def test_cipher_single(self, text, shift, expected):
        actual = cipher(text, shift)
        assert actual == expected
    
    def test_cipher_negative(self, text, shift, expected):
        actual = cipher(text, shift)
        assert actual == expected
        
    def test_cipher_symbol(self, text, shift, expected):
        actual = cipher(text, shift)
        assert actual == expected
        


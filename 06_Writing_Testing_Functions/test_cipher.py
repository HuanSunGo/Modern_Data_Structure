#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pytest


# In[2]:


def test_cipher_single():
    text1 = 'm'
    expected1 = 'n'
    actual1 = cipher(text1, 1)
    assert actual1 == expected1


# In[3]:


def test_cipher_negative():
    text2='d'
    expected2='c'
    actual2=cipher(text2,-1)
    assert actual2==expected2


# In[1]:


def test_cipher_symbol():
    text3 = 'Chef*'
    expected3 ='Fkhi*'
    actual3 = cipher(text3, 3)
    assert actual3 == expected3


# In[2]:


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


# In[3]:


def test_cipher_shift():
    with pytest.raises(AssertionError):
        cipher('text', 'three')


# In[ ]:





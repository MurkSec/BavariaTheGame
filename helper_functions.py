#!/bin/python3.6
import textwrap

''' Textwrap wrapper'''
def WrappedTextOutput(p_text. p_width=70):
  wrapped_text = textwrap.wrap(p_text, p_width)
  for s in wrapped_text:
    print(s)

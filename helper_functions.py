#!/bin/python3.6
import textwrap
import time


''' Textwrap wrapper'''
def WrappedTextOutput(p_text, p_width=70):
  wrapped_text = textwrap.wrap(p_text, p_width)
  for s in wrapped_text:
    print(s)
    
def clear_screen():
  print('\033[H\033[J')
  time.sleep(0.1)

"""
Screenwipe

description: This will wipe the screen for multiple OS versions.
params: operator  - sets the operator to be rendered to screen      | defailt "\n"
        lines     - literally prints the operator x number of times | default 250
return: void
"""
def Screenwipe(operator="\n", lines=250)
  print('\n'*250)

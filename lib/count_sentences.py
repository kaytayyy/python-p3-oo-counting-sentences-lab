#!/usr/bin/env python3

class MyString:
    def __init__(self, value=None):
        self._value = value

    @property
    def value(self):
        return self._value
  
    @value.setter
    def value(self, val):
        if not isinstance(val, str):
            print("The value must be a string.")
        self._value = val

    def is_sentence(self):
        return self._value.endswith('.') if self._value else False
  
    def is_question(self):
        return self._value.endswith("?") if self._value else False
  
    def is_exclamation(self):
        return self._value.endswith("!") if self._value else False
  
    def count_sentences(self):
        if not self._value:
            return 0
        
        # Initialize sentence count and previous character flag
        sentence_count = 0
        prev_char = None
        
        # Iterate over each character in the string
        for char in self._value:
            if char in ['.', '?', '!']:
                # Increment sentence count if current character is a punctuation mark and previous character is not a punctuation mark
                if prev_char not in ['.', '?', '!']:
                    sentence_count += 1
            # Update previous character flag
            prev_char = char
        
        return sentence_count

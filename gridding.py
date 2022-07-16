

from collections import deque
def get_hash_value(string:str,salt:int):
    
    original_hash=salt
    

    for char in string.strip():
       
        new_hash = ord(char) + (31*original_hash)
        original_hash+= new_hash
    print(original_hash)
    return original_hash
      


get_hash_value('Hello, World', 11)

get_hash_value('a', 0)



def identify_errors_text(text):
    opening_brackets = deque()
    closing_brackets = deque()
    indices_brackets = deque()
    for char in text.split():
        if char =='(' or '<' or '{' or '[':
            opening_brackets.append(char)
            indices_brackets.append(text.index(char))
        elif char == ')' or '>' or '}' or ']':
            closing_brackets.append(char)
            indices_brackets.append(text.index(char))
    print(opening_brackets)

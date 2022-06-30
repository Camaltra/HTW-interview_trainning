#!/usr/bin/python3

def validParentheses(parenthesesString):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in parenthesesString:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack

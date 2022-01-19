# In this file, we imitate the function 'expression(str)' by the 'Stack', one of data structures.
# import re for regular expression
import re
import os
from fractions import Fraction as fr

# Definition of the class 'Stack'
# Actually, What Stack can do is what list can do. there are little differences.
# Property of the first-in-last-out

class Element:
    def __init__(self, item):
        self.data = item
        self.prev = None


class Stack:
    def __init__(self):
        self.depth = 0
        self.peek = None

    def push(self, element: Element):
        self.depth += 1
        if self.peek:
            element.prev = self.peek
        self.peek = element

    def pop(self):
        if not self.depth:
            raise ValueError

        extract = self.peek
        if extract.prev:
            self.peek = extract.prev
        else:
            self.peek = None
        self.depth -= 1
        return extract

    def __repr__(self):
        if not self.depth:
            return ']'
        elem = self.peek
        rep = str(elem.data)
        while elem.prev:
            rep += '|'
            rep += str(elem.data)
            elem = elem.prev
        rep += ']'
        return rep


# 'Extracting the proper str' process to convert an infix form to a postfix form
# We use regular expression of python (re module is used in here.)
def remove_space(expression: str) -> str:
    expression = re.sub('[xX]', '*', expression)
    expression = re.sub(r'[<[{]', '(', expression)
    expression = re.sub(r'[]}>]', ')', expression)
    extract = re.sub('[^0-9+*/().^-]', '', expression)
    return extract


# Actual process of postfix
def infix_to_postfix(extract: str) -> list:
    # order of operations
    operation_order = {
        '^': 4,
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    op_stack = Stack()
    postfix_list = []

    for i, value in enumerate(extract):
        # case of (,)
        if value == ')':
            while op_stack.peek.data != '(':
                postfix_list.append(op_stack.pop().data)
            op_stack.pop()
        elif value == '(':
            op_stack.push(Element('('))

        # case of numbers
        elif value.isdigit() or value == '.':
            if i == 0 or (not extract[i - 1].isdigit() and extract[i - 1] != '.'):
                postfix_list.append(value)
            else:
                postfix_list[-1] += value
        # case of operators
        elif not op_stack.depth or operation_order[op_stack.peek.data] < operation_order[value]:
            op_stack.push(Element(value))
        else:
            while op_stack.depth and operation_order[op_stack.peek.data] >= operation_order[value]:
                postfix_list.append(op_stack.pop().data)
            op_stack.push(Element(value))
    # add remaining elements in the stack to list
    while op_stack.depth:
        postfix_list.append(op_stack.pop().data)
    return postfix_list


# Calculation
def postfix_eval(postfix_list) -> int or float:
    st = Stack()
    for value in postfix_list:
        if value == re.sub('[^0-9.]', '', value):
            st.push(Element(float(value)))
        elif value == '+':
            val = st.pop().data + st.pop().data
            st.push(Element(val))
        elif value == '-':
            val = -st.pop().data + st.pop().data
            st.push(Element(val))
        elif value == '*':
            val = st.pop().data * st.pop().data
            st.push(Element(val))
        elif value == '/':
            if not st.peek.data:
                raise ZeroDivisionError
            val = (1 / st.pop().data) * st.pop().data
            st.push(Element(val))
        else:
            pos = st.pop().data
            pre = st.pop().data
            val = pre ** pos
            st.push(Element(val))
    return st.peek.data

def postfix_eval_fraction(postfix_list):
    st = Stack()
    for value in postfix_list:
        if value == re.sub('[^0-9.]', '', value):
            st.push(Element(fr(value)))
        elif value == '+':
            val = st.pop().data + st.pop().data
            st.push(Element(val))
        elif value == '-':
            val = -st.pop().data + st.pop().data
            st.push(Element(val))
        elif value == '*':
            val = st.pop().data * st.pop().data
            st.push(Element(val))
        elif value == '/':
            if not st.peek.data:
                raise ZeroDivisionError
            val = (1 / st.pop().data) * st.pop().data
            st.push(Element(val))
        else:
            pos = st.pop().data
            pre = st.pop().data
            val = pre ** pos
            st.push(Element(val))
    return st.peek.data

# From a string expression, we evaluate a real value, like the 'eval' function already in python


def solution(expression: str) -> int or float:
    if not remove_space(expression):
        return ''
    try:
        tokens = remove_space(expression)
        postfix = infix_to_postfix(tokens)
        val = postfix_eval(postfix)
    except ZeroDivisionError:
        return '0 division is not allowed.'
    except Exception:
        return "Wrong!"
    if val == int(val):
        return int(val)
    return val


def solution_fraction(expression: str):
    if not remove_space(expression):
        return ''
    try:
        tokens = remove_space(expression)
        postfix = infix_to_postfix(tokens)
        val = postfix_eval_fraction(postfix)
    except ZeroDivisionError:
        return '0 division is not allowed.'
    except Exception:
        return "Wrong!"
    return val


if __name__ == '__main__':
    loop = True
    while loop:
        os.system('cls')
        mode = input('Select the type of the answer either float or fraction (fl/fr) > ')

        if mode != 'fl' and mode != 'fr':
            print('Type \'fl\' or \'fr\'.')
            continue

        variables = input("Insert a suitable formula. > ")
        if mode == 'fl':
            print(solution(variables))
        else:
            print(solution_fraction(variables))

        while True:
            reply = input("Do you want to calculate other formulas? (y/n) : ")
            if reply.lower() not in 'yn':
                print("Type y or n.")
                continue
            elif reply.lower() == 'y':
                break
            else:
                input("Press any key to quit this program.")
                loop = False
                break
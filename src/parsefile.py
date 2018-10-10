import os
import re
from src.dfa import Dfa


def parse_main():
    print("EVENT: Running parse_main()")
    file_content = read_file_string()
    if (verify_dfa_components(file_content)):
        content = remove_whitespace(file_content)
        print(content)
        parsed_dfa = list_to_dfa(parse_dfa_list(
            separate_dfa_components(content)))
        return parsed_dfa


def read_file_string():
    path = "test1.dfa"
    file = open(path, 'r')
    file_content = file.read()
    file.close()
    return file_content


def verify_dfa_components(file_content):
    if (
        'states' in file_content and 'alpha' in file_content and
        'trans-func' in file_content and 'start' in file_content and
        'final' in file_content
    ):
        print("EVENT: Found DFA components")
        return True
    else:
        print("PARSE ERROR: File is missing DFA components")
        return False


def remove_whitespace(file_content):
    new_content = "".join(file_content.split())
    return new_content


def separate_dfa_components(content):
    sep_list = []
    prop_list = ['(alpha', '(trans-func', '(start', '(final']
    sep_list.append(content[:content.find(prop_list[0])])
    for x in range(3):
        sep_list.append(content[content.find(
            prop_list[x]):content.find(prop_list[x+1])])
    sep_list.append(content[content.find(prop_list[-1]):])
    return sep_list


def parse_dfa_list(sep_list):
    dfa_list = []
    for str in sep_list:
        content = rip_off_parens(str)
        if 'states' in str:
            dfa_list.append(parse_states(content))
        elif 'alpha' in str:
            dfa_list.append(parse_alpha(content))
        elif 'trans-func' in str:
            dfa_list.append(parse_trans(content))
        elif 'start' in str:
            dfa_list.append(parse_start(content))
        elif 'final' in str:
            dfa_list.append(parse_final(content))
    return dfa_list


def rip_off_parens(str):
    if str.startswith('(') and str.endswith(')'):
        outer_paren = re.compile("\((.+)\)")
        res = outer_paren.search(str)
        return res.group(1)
    else:
        print("ERROR: invalid content in separated list")


def parse_states(str):
    if str.startswith('states,'):
        content = str.lstrip('states,')
        dfa_str = rip_off_parens(content)
        split_list = dfa_str.split(',')
        return split_list
    else:
        print("PARSE ERROR: Problem parsing states string")


def parse_alpha(str):
    if str.startswith('alpha,'):
        content = str.lstrip('alpha,')
        dfa_str = rip_off_parens(content)
        split_list = dfa_str.split(',')
        return split_list
    else:
        print("PARSE ERROR: Problem parsing alpha string")


def parse_trans(str):
    def _helper(split_list):
        sub_stack = []
        for item in split_list:
            if "," in item:
                item_list = item.split(',')
                stack.append(_helper(item_list))
            else:
                sub_stack.append(item)
        return sub_stack
    if str.startswith('trans-func,'):
        content = str.lstrip('trans-func,')
        if content.startswith('(') and content.endswith(')'):
            stack = []
            content = content.lstrip('(')
            content = content.rstrip(')')
            split_list = content.split('),(')
            _helper(split_list)
            return stack
        else:
            print("PARSE ERROR: Problem parsing trans-func string")
    else:
        print("PARSE ERROR: Problem parsing trans-func string")


def parse_start(str):
    if str.startswith('start,'):
        content = str.lstrip('start,')
        return content
    else:
        print("PARSE ERROR: Problem parsing start string")


def parse_final(str):
    if str.startswith('final,'):
        content = str.lstrip('final,')
        dfa_str = rip_off_parens(content)
        split_list = dfa_str.split(',')
        return split_list
    else:
        print("PARSE ERROR: Problem parsing final string")


def list_to_dfa(dfa_list):
    if(len(dfa_list) != 5):
        print("PARSE ERROR: Problem parsing list to dfa. List is not right size")
    else:
        parsed_dfa = Dfa(dfa_list[0], dfa_list[1],
                         dfa_list[2], dfa_list[3], dfa_list[4])
        return parsed_dfa

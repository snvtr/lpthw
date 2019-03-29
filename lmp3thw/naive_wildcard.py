#!C:/Python37/python3.exe


def question_mark_search(string, pattern, lazy):

    print('debug: pattern=%r' % pattern)

    match_pos = -1
    p_len = len(pattern)

    for i in range(len(string)-p_len+1):

        temp_list = []
        temp_str = string[i:i+p_len]

        # replaces chars in a searched string with '?'
        for c in range(p_len):
            if pattern[c] == '?':
                temp_list.append('?')
            else:
                temp_list.append(temp_str[c])

        temp_str = ''.join(temp_list)

        # is the search lazy or not:
        if   temp_str == pattern and lazy:
            match_pos = i
        elif temp_str == pattern and not lazy:
            return i

    return match_pos
    

def naive_wildcard_search(string, pattern, lazy):
    """
        searches the string 'string' for the pattern 'pattern'
        with wildcards like '?' (single character) and '*' (any number of characters including none)
        
        if lazy == True than stops at the first encounter, otherwise goes on to the end of the 'string'
    """    

    if pattern.find('*') >= 0:
        for i in range(len(string) - 1):
            return naive_wildcard_search(string, pattern.replace('*','?'*i,1), lazy)
    else:
        return question_mark_search(string, pattern, lazy)

        

### __main__() ###

my_str    = 'abcd'
my_pattern = 'b*'

rc = naive_wildcard_search(my_str, my_pattern,True)

if rc >= 0:
    print('strings %s and %s has a match at position %i' % (my_str, my_pattern, rc))

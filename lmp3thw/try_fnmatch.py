
import os, sys, fnmatch

script, start_dir, pattern = sys.argv

### __defs__ ###

def try_fnmatch(filename, pattern):

    if filename[-1] == '\\':
        ''.join(filename,'*')

    filename.lstrip('\\')
    
def check_wildcard(full_filename, pattern):
    """ проверяет имя переданное в параметрах относительно pattern в args.name """

#    if filename.find('\\'):
#        path_elements = filename.split('\\')
#    else:
#        path_elements = [filename]
#        
#    if any (fnmatch.fnmatch(path_element, pattern) for path_element in path_elements):
#        return True
    if fnmatch.fnmatch(full_filename, pattern):
        return True

    return False
    
    
### __main__() ###
    
tree = os.walk(start_dir)

for i in tree:
    print(i[0])
    for j in i[2]:
        if check_wildcard('\\'.join([i[0],j]), pattern):
            print('%s matches the pattern %s' % ('\\'.join([i[0],j]), pattern))
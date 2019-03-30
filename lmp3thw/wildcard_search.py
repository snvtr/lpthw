def build_matrix(string, pattern):

    """
    строит матрицу совпадений
    """

    len_p = len(pattern) + 1 # размер массива по горизонтали
    len_s = len(string) + 1  # размер массива по вертикали

    M = [['.' for s in range(len_s)] for p in range(len_p)]

    pos = 1
    for p in range(1, len_p):
        for s in range(pos, len_s):
            if pattern[p-1] == '*':
                M[p][s] = '*'
            if pattern[p-1] == '?':
                M[p][s] = '?'
            if pattern[p-1] == string[s-1]:
                pos = s + 1
                M[p][s] = 'x'
                
    for p in range(len_p):
        print(M[p])

    return M

def decode_matrix(M,string):

    """
    собирает строку в виде списка символов, совпавшую с образом для поиска
    """

    len_s = len(M[0]) - 1
    len_p = len(M) - 1

    Result = []
    
    pos = len_s
    for y in range(len_p, 0, -1):
        qm_cnt = 0
        for x in range(pos, 0, -1):
            if M[y][x] == 'x':
                print(string[x-1])
                Result.insert(0,string[x-1])
                pos = x - 1
                break
            if M[y][x] == '*':
                print(string[x-1])
                Result.insert(0,string[x-1])
                pos = x - 1
            if M[y][x] == '?' and qm_cnt == 0:
                qm_cnt += 1
                print(string[x-1])
                Result.insert(0,string[x-1])
                pos = x - 1
                break

    return Result
                
Match = build_matrix('abcxyzy','c*x?z')
print(''.join(decode_matrix(Match,'abcxyzy')))

import sys


def insert_cost():
    return 1


def delete_cost():
    return 1


def replace_cost(a,b):
    return 0 if a == b else 2


def get_med(source, target):
    source_len = len(source)
    target_len = len(target)
    table = [[None for j in range(target_len+1)] for i in range(source_len+1)]
    table[0][0] = 0
    for i in range(source_len+1):
        table[i][0] = i
    for j in range(target_len+1):
        table[0][j] = j
    for i in range(1, source_len+1):
        for j in range(1, target_len+1):
            insert_len = table[i-1][j]+ insert_cost()
            delete_len = table[i][j - 1] + delete_cost()
            replace_len = table[i-1][j-1]+replace_cost(source[i-1], target[j-1])
            table[i][j] = min([insert_len, delete_len, replace_len])
    return table[source_len-1][target_len-1]


def main(argv):
    word1, word2 = argv[1:]
    d = get_med(word1, word2)
    print(d)

if __name__ == "__main__":
    main(sys.argv)

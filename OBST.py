
import xml.etree.ElementTree as ET

#from binarytree import Node

import sys

INT_MAX = sys.maxsize

COUNT = [15]

address = 'Vocabulary.xml'

# =================================


class Node:

    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def print2DUtil(root, space):

    if (root == None):
        return

    space += COUNT[0]

    print2DUtil(root.right, space)

    print()
    for i in range(COUNT[0], space):
        print(end=" ")
    print(root.data)

    print2DUtil(root.left, space)


def print2D(root):

    print2DUtil(root, 0)

# ===========================================






# ===============================

def Read_From_XML(address):
    key = []
    p = []
    value = []

    tree = ET.parse(address)
    words = tree.getroot()
    number_of_words = len(words)



    for i in range(0, number_of_words):
        key.append(words[i][0].text)
        value.append(words[i][1].text)
        p.append(words[i][2].text)


    return key, p, value,number_of_words



# ======================================

def OBST(Probability, n):

    cost = [[0 for x in range(n)]
            for y in range(n)]

    result = [[0 for x in range(n + 1)]
              for y in range(n + 1)]

    for i in range(n):
        cost[i][i] = Probability[i]

    for i in range(1, n + 1):
        result[i][i] = i

    for L in range(2, n + 1):

        for i in range(n - L + 2):

            j = i + L - 1

            if i >= n or j >= n:
                break

            cost[i][j] = INT_MAX

            for m in range(i, j + 1):

                c = 0

                if m > i:
                    c += cost[i][m - 1]
                if m < j:
                    c += cost[m + 1][j]
                c += sum(Probability, i, j)

                if c < cost[i][j]:
                    cost[i][j] = c
                    result[i + 1][j + 1] = m + 1

    return cost[0][n - 1], result

# ======================================


def sum(Probability, i, j):
    s = 0
    for k in range(i, j + 1):
        s += Probability[k]

    return s

# =======================================


def Tree(result, i, j, keys):

    if i >= n + 1 or j >= n + 1:
        return
    k = result[i][j]

    if k == 0:
        return
    else:
        root = Node(keys[k - 1])
        root.left = Tree(result, i, k - 1, keys)
        root.right = Tree(result, k + 1, j, keys)

    return root

# ==========================================

# start

while True:
    print('====================')
    print('1.Add')
    print('====================')
    print('2.Search')
    print('====================')
    print('3.Delete')
    print('====================')
    print('4.Show Tree')
    print('====================')
    print('5.Exit')
    print('====================')

    print()
    print('PLease Enter Number:')

    number = int(input())

    if number == 1:

        keys = Read_From_XML(address)[0]
        probabilitys = Read_From_XML(address)[2]
        values = Read_From_XML(address)[1]
        n = Read_From_XML(address)[3]

        key = input("Please Enter key:")

        p = input("Please enter Probability:")

        value = input('please enter Value:')

        keys.append(key)
        probabilitys.append(p)
        values.append(value)



        p = list(map(float, p))

        result = OBST(p, n)[1]

        root = Tree(result, 1, n, key)

        print2D(root)

        print()
        print()

    elif number == 2:

        keys = Read_From_XML(address)[0]

        probabilitys = Read_From_XML(address)[1]

        values = Read_From_XML(address)[2]

        n = Read_From_XML(address)[3]

        key = input('Please enter word:')

        flag = False

        for i in range(n):
            keys[i] = keys[i].strip()

        count = 0
        for i in keys:

            if i == key:

                flag = True

                break

            count += 1

        if flag is False:

            print('This word is not exist')

        else:
            print()
            print('The meaning of word is:', values[count])
            print()

            probabilitys = list(map(float, probabilitys))

            probabilitys[count] = probabilitys[count] + 0.1

            result = OBST(probabilitys, n)[1]
            root = Tree(result, 1, n, keys)

            print2D(root)

            print()
            print()



    elif number == 3:
        pass

    elif number == 4:

        # address = 'Vocabulary.xml'

        key = Read_From_XML(address)[0]

        probability = Read_From_XML(address)[1]

        n = Read_From_XML(address)[3]

        probability = list(map(float, probability))

        result = OBST(probability, n)[1]

        root = Tree(result, 1, n, key)

        print2D(root)

        print()
        print()
        print("+++++++++++++++++++++++++++++++++++++")


    else:
        break

# address = 'Vocabulary.xml'
#
# key = Read_From_XML(address)[0]
#
# probability = Read_From_XML(address)[1]
#
# n = Read_From_XML(address)[2]
#
# probability = list(map(float, probability))
#
# result = OBST(probability, n)[1]
#
# root = Tree(result, 1, n, key)
#
# print2D(root)

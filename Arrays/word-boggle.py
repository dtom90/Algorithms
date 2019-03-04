"""
Word Boggle

https://practice.geeksforgeeks.org/problems/word-boggle/0

Given a dictionary, a method to do lookup in dictionary and a M x N board where every cell has one character.
Find all possible words that can be formed by a sequence of adjacent characters.
Note that we can move to any of 8 adjacent characters, but a word should not have multiple instances of same cell.

Example:

Input: dictionary[] = {"GEEKS", "FOR", "QUIZ", "GO"};
       boggle[][]   = {{'G','I','Z'},
                       {'U','E','K'},
                       {'Q','S','E'}};

Output:  Following words of dictionary are present
         GEEKS, QUIZ

Input:
The first line of input contains an integer T denoting the no of test cases . Then T test cases follow.
Each test case contains an integer x denoting the no of words in the dictionary.
Then in the next line are x space separated strings denoting the contents of the dictionary.
In the next line are two integers N and M denoting the size of the boggle.
The last line of each test case contains NxM space separated values of the boggle.

Output:
For each test case in a new line print the space separated sorted distinct words of the dictionary
which could be formed from the boggle. If no word can be formed print -1.

Constraints:
1<=T<=10
1<=x<=10
1<=n,m<=7

Example:
Input:
1
4
GEEKS FOR QUIZ GO
3 3
G I Z U E K Q S E

Output:
GEEKS QUIZ
"""


DEBUG = False


def parse_input(func):
    t = int(input())
    if DEBUG: print('{} test cases'.format(t))
    for i in range(t):
        if DEBUG: print('\nuse case {}'.format(i + 1))
        x = int(input())
        if DEBUG: print('x = {}'.format(x))
        dictionary = set(s for s in input().split())
        if DEBUG: print(dictionary)
        n, m = tuple(int(s) for s in input().split())
        if DEBUG: print('n = {}'.format(n))
        if DEBUG: print('m = {}'.format(m))
        flat_board = [s for s in input().split()]
        if DEBUG: print(flat_board)
        found_words = play_boggle(dictionary, n, m, flat_board)
        if found_words:
            print(' '.join(found_words))
        else:
            print(-1)


def play_boggle(dictionary, n, m, flat_board):
    lookup_diction = {}
    singles = doubles = set()
    for word in dictionary:
        if len(word) == 1:
            singles.add(word)
        elif len(word) == 2:
            doubles.add(word)
        else:
            prefix = word[:2]
            if prefix not in lookup_diction:
                lookup_diction[prefix] = []
            lookup_diction[prefix].append(word)
    if DEBUG: print(lookup_diction)

    board = [flat_board[a:a+m] for a in range(0, m*n, m)]
    if DEBUG:
        print(board)
        for x in range(n):
            for y in range(m):
                print(board[x][y], end=' ')
            print()
        print()

    found_words = set()
    for x in range(n):
        for y in range(m):
            letter1 = board[x][y]
            if DEBUG: print(letter1)

            if letter1 in singles:
                found_words.add(letter1)

            for s in range(-1, 2):
                for t in range(-1, 2):
                    other = x + s, y + t
                    if 0 <= other[0] < n and 0 <= other[1] < m and not s == t == 0:
                        letter2 = board[other[0]][other[1]]
                        if DEBUG: print(letter2, end=' ')

                        prefix = letter1 + letter2
                        if prefix in doubles:
                            found_words.add(prefix)

                        if prefix in lookup_diction:
                            if DEBUG: print('yes!', end=' ')
                            for w in recurse_word(prefix, lookup_diction[letter1 + letter2], board, other,
                                                  [(x, y), other], n, m):
                                found_words.add(w)
            if DEBUG: print()

    return sorted(list(found_words))


def recurse_word(current_subword, possibilities, board, current_location, seen_locations, n, m):
    found_words = []
    if current_subword in possibilities:
        found_words.append(current_subword)
        possibilities.remove(current_subword)

    if len(possibilities) > 0:
        for s in range(-1, 2):
            for t in range(-1, 2):
                next_location = current_location[0] + s, current_location[1] + t
                if 0 <= next_location[0] < n and 0 <= next_location[1] < m and not s == t == 0 \
                        and not next_location in seen_locations:
                    next_letter = board[next_location[0]][next_location[1]]
                    if DEBUG: print(next_letter, end=' ')
                    next_subword = current_subword + next_letter
                    for word in possibilities:
                        if word[:len(next_subword)] == next_subword:
                            if DEBUG: print('yes!', end=' ')
                            found_words.extend(recurse_word(next_subword, possibilities, board, next_location,
                                                            seen_locations+[next_location], n, m))
    return found_words


parse_input(play_boggle)

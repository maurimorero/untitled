# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(palabra):
    if (palabra==palabra[::-1]):
        return True
    else:
        return False




print(solution("abcb"))
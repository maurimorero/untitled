
from collections import deque


def getIndex(s, i):
    if s[i] != '[':
        return -1

    d = deque()

    for k in range(i, len(s)):

        if s[k] == ']':
            d.popleft()

        elif s[k] == '[':
            d.append(s[i])

        if not d:
            return k

    return -1


def test(s, i):
    matching_index = getIndex(s, i)
    print(s + ", " + str(i) + ": " + str(matching_index))


def main():
    test("[ABC[23]][89]", 0)  # should be 8
    test("[ABC[23]][89]", 4)  # should be 7
    test("[ABC[23]][89]", 9)  # should be 12
    test("[ABC[23]][89]", 1)  # No matching bracket


if __name__ == "__main__":
    main()
# Given a string of ﬁnite length, implement a function that returns
# the longest substring that is a palindrome. For example func(“bubba ho-tep”)
# would return“bub”, and func(“xx123454321zz”) would return “123454321”.

def solution(text):
    text = text.lower()
    results = []

    for i in range(len(text)):
        for j in range(0, i):
            chunk = text[j:i + 1]
            if chunk == chunk[::-1]:
                results.append(chunk)
                print(chunk)

    return max(results, key=lambda s: (len(s), s))

print(solution("xx123454321zz"))
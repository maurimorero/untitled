# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

DAYS_OF_WEEK = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def _rotate_list(times: int, l: list=DAYS_OF_WEEK) -> list:
    """
    This internal method takes care of the rotaion of DAYS_OF_WEEK list
    """
    for i in range(times):
        aux = l.pop(0)
        l.append(aux)
    return l


def solution(S: str, K: int) -> str:
    if K < 0:
        return None
    rest_of_division = K % 7
    if S in DAYS_OF_WEEK:
        temp = _rotate_list(DAYS_OF_WEEK.index(S))
    else:
        return None
    return temp[rest_of_division]


print(solution("Sun", 1))


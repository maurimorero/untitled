
def solution(file_object):
    line = file_object.readline()
    line = file_object.readline()
    while line:
        if line.strip().isnumeric():
            yield int(line.strip())
        else:
            break
        line = file_object.readline()

# Example usage:
#
# for i in solution(file_object):
#     print(i)

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
c1x = 1.5
c2x = 3.66
c3x = 7
c1y = 3.5
c2y = 9
c3y = 4.33

M = [[2,10],[2, 5],[8, 4],[5, 8],[7, 5],[6, 4],[1, 2],[4, 9]]
def print_hi(name):
    for x in range(8):
        print("M", end="")
        print(x+1, end="\t")
        v = abs(M[x][0]- c1x) + abs(M[x][1]- c1y)
        print(v, end="\t")
        v = abs(M[x][0] - c2x) + abs(M[x][1] - c2y)
        print(v, end="\t")
        v = abs(M[x][0] - c3x) + abs(M[x][1] - c3y)
        print(v, end="\n")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

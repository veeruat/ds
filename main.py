# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def sum_two(num,target):

    l = len(num)
    res = []
    for out_ind in range(l):
        if num[out_ind] == target:
            return res.append(out_ind)
        if num[out_ind] > target:
            continue
        if len(res) == 0:

            res.append(out_ind)

        for inr_ind in range(out_ind+1,l):
            if num[res[0]] + num[inr_ind] == target:
                res.append(inr_ind)
                return res
        res.__delitem__(0)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    resu = sum_two([2,1,3,6,15],9)
    print(resu)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

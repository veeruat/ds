
class ArrayMerge:

    def __init__(self):
        pass

    def array_merge(self, arr1, arr2, arr3, n1, n2):
        """
        *********************************
            Merge the two arrays
        *********************************
        :param arr1:
        :param arr2:
        :param arr3:
        :param n1:
        :param n2:
        :return:
        """
        i = 0
        for idx in range(n1):
            arr3[i] = arr1[idx]
            i +=1

        for idx in range(n2):
            arr3[i] = arr2[idx]
            i += 1

        print(arr3)


if __name__ == '__main__':
    am_o = ArrayMerge()

    ar1 = [1, 2, 5, 6]
    ar2 = [4, 6, 8, 9, 4]

    l1 = len(ar1)
    l2 = len(ar2)

    ar3 = [0 for item in range(l1 + l2)]

    am_o.array_merge(ar1, ar2, ar3, l1, l2)
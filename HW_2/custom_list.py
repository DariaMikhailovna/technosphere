from functools import total_ordering


@total_ordering
class CustomList(list):

    def __neg__(self):
        return CustomList(-val for val in self)

    def __add__(self, other):
        len_new_list = max(len(self), len(other))
        new_list = CustomList([0] * len_new_list)
        for i in range(len(self)):
            new_list[i] += self[i]
        for i in range(len(other)):
            new_list[i] += other[i]
        return new_list

    __radd__ = __add__

    def __sub__(self, other):
        return -(-self + other)

    def __rsub__(self, other):
        return -self + other

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

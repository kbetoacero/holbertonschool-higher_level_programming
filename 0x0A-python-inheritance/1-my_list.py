#!/usr/bin/python3
""" My list
    class MyList that inherits
    from list
    """


class MyList(list):
    """ Public instance method:
    def print_sorted(self)
    """
    def print_sorted(self):
        """
        prints the list but sorted
        """
        sorted_list = MyList()
        for i in self:
            sorted_list.append(i)
        print(sorted(sorted_list))

class ListUtil:

    def __init__(self, the_list):
        self.the_list = the_list

    def flatten(self):
        return self.__flatten(self.the_list)

    def __flatten(self, the_list, buf=None):

        if buf is None:
            buf = list()

        for item in the_list:
            if isinstance(item, list):
                buf = self.__flatten(item, buf)

            else:
                buf.append(item)

        return buf


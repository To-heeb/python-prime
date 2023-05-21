# container class
#  __variable = private attribute

class TagCloud:
    """_summary_
    """

    def __init__(self) -> None:
        """_summary_
        """
        self.__tags = {}

    def add(self, tag: str) -> None:
        """_summary_

        Args:
            tag (str): _description_
        """
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitems__(self, tag):
        """_summary_

        Args:
            tag (_type_): _description_
        """
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
cloud.add("python")
cloud.add("python")
cloud.add("python")
cloud.add("java")
cloud.add("java")
cloud.add("php")
cloud.add("php")
cloud.add("linux")

for tag in cloud:
    print(tag)
print(cloud)

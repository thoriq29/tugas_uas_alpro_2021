class Drink():
    def __init__(self, name, description, image_path):
        self.__name = name
        self.__description = description
        self.__image_path = image_path

    def getName(self):
        return self.__name

    def getDescription(self):
        return self.__description

    def getImagePath(self):
        return self.__image_path
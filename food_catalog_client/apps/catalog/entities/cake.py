from food_catalog_client.apps.catalog.entities.food import Food

class Cake(Food):
    def __init__(self, name, color, image_path):
        self.__name = name
        self.__color = color
        self.__image_path = image_path
        Food.__init__(self, name, "Cake dengan warna " + color, image_path)

    def getName(self):
        return self.__name

    def getColor(self):
        return self.__color

    def getImagePath(self):
        return self.__image_path
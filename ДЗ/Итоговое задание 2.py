# Задача 2. Кэширование запросов
# Контекст
# Вы разрабатываете программу для кэширования запросов к внешнему API. Часто повторяющиеся запросы занимают много
# времени, поэтому вы решаете создать класс LRU Cache (Least Recently Used Cache), который будет хранить ограниченное
# количество запросов и автоматически удалять самые старые при достижении лимита. Это позволит значительно ускорить
# повторяющиеся запросы, так как данные будут браться из кэша, а не отправляться повторно.
#
# Задача
# 1.	Создайте класс LRU Cache, который хранит ограниченное количество объектов и, при превышении лимита,
# удаляет самые давние (самые старые) использованные элементы.
# 2.	Реализуйте методы добавления и извлечения элементов с использованием декораторов property и setter.
# @property
# def cache(self): # этот метод должен возвращать самый старый элемент
#     ...
# @cache.setter
# def cache(self, new_elem): # этот метод должен добавлять новый элемент
#     ...
#
# Советы
# Не забывайте обновлять порядок использованных элементов. В итоге должны удаляться давно использованные элементы,
# а не давно добавленные, так как давно добавленный элемент может быть популярен,
# и его удаление не поможет ускорить новые запросы.
# Пример:
#
# # Создаём экземпляр класса LRU Cache с capacity = 3
# cache = LRUCache(3)
##
# # Добавляем элементы в кэш
# cache.cache = ("key1", "value1")
# cache.cache = ("key2", "value2")
# cache.cache = ("key3", "value3")
##
# # # Выводим текущий кэш
# cache.print_cache() # key1 : value1, key2 : value2, key3 : value3
##
# # Получаем значение по ключу
# print(cache.get("key2")) # value2
##
# # Добавляем новый элемент, превышающий лимит capacity
# cache.cache = ("key4", "value4")
##
# # Выводим обновлённый кэш
# cache.print_cache() # key2 : value2, key3 : value3, key4 : value4
#
#
# Ожидаемый вывод в консоли:
#
# LRU Cache:
# key1 : value1
# key2 : value2
# key3 : value3
#
# value2
#
# LRU Cache:
# key3 : value3
# key2 : value2
# key4 : value4
#

# 1.	Создайте класс LRU Cache, который хранит ограниченное количество объектов и, при превышении лимита,
# удаляет самые давние (самые старые) использованные элементы.

class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dict_cache = {}

    # 2.	Реализуйте методы добавления и извлечения элементов с использованием декораторов property и setter.
    # @property
    # def cache(self): # этот метод должен возвращать самый старый элемент
    #     ...
    # @cache.setter
    # def cache(self, new_elem): # этот метод должен добавлять новый элемент

    @property
    def cache(self):
        return next(iter(self.dict_cache))

    @cache.setter
    def cache(self, new_elem: tuple):
        if len(self.dict_cache) >= self.capacity:
            self.dict_cache.popitem()
        self.dict_cache[new_elem[0]] = new_elem[1]

    def print_cache(self):
        print("LRU Cache:")
        for key, value in self.dict_cache.items():
            print(f"{key} : {value}")

    def get(self, key):
        return self.dict_cache.get(key)


# Создаём экземпляр класса LRU Cache с capacity = 3
cache = LRUCache(3)
# Добавляем элементы в кэш
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")
# Выводим текущий кэш
cache.print_cache()  # key1 : value1, key2 : value2, key3 : value3
# Получаем значение по ключу
print(cache.get("key2"))  # value2
# Добавляем новый элемент, превышающий лимит capacity
cache.cache = ("key4", "value4")
# Выводим обновлённый кэш
cache.print_cache()  # key2 : value2, key3 : value3, key4 : value4

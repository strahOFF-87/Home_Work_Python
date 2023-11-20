# Задача 1. Стек
# Напишите класс, который реализует Стек и его возможности (достаточно будет добавления и удаления элемента).
# # После этого напишите ещё один класс “Менеджер задач”. В менеджере задач можно выполнить команду “новая задача”,
# в которую передаётся сама задача (str) и её приоритет (int). Сам менеджер работает на основе Стэка (не наследование!).
# При выводе менеджера в консоль все задачи должны быть отсортированы по приоритету: чем меньше число, тем выше задача.
#
# Вот пример основной программы:
#
# manager = TaskManager()
# manager.new_task("сделать уборку", 4)
# manager.new_task("помыть посуду", 4)
# manager.new_task("отдохнуть", 1)
# manager.new_task("поесть", 2)
# manager.new_task("сдать дз", 2)
# print(manager)
# #
# Результат:<br>
# 1 отдохнуть<br>
# 2 поесть; сдать дз<br>
# 4 сделать уборку; помыть посуду<br>
# Дополнительно: реализуйте также удаление задач и подумайте, что делать с дубликатами

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def top(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def __str__(self):
        return '; '.join(self.items)


class TaskManager:
    def __init__(self):
        self.tasks = {}

    def new_task(self, text, priority):
        if priority not in self.tasks:
            self.tasks[priority] = Stack()
        self.tasks[priority].push(text)

    # def __str__(self):
    #     string = ""
    #     for task in sorted(self.tasks):
    #         string += str(task) + " " + str(self.tasks[task]) + "\n"
    #     return string

    def __str__(self):
        display = []
        if self.tasks:
            for i_priority in sorted(self.tasks.keys()):
                display.append('{prior} {task}\n'.format(prior=str(i_priority),
                                                         task=self.tasks[i_priority], )
                               )

        return ''.join(display)


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)

print(manager)

# 1 отдохнуть
# 2 поесть; сдать дз
# 4 сделать уборку; помыть посуду

class Task_View:
    def showAllTasks(self, tasks: list):
        print("Todas las tareas:")
        for i, task in enumerate(tasks):
            print(f"{i}. {task}")

    def showFinishedTasks(self, tasks: list):
        print("Tareas finalizadas:")
        for task in tasks:
            if task.getFinished():
                print(task.getDescription())

    def showUnfinishedTasks(self, tasks: list):
        print("Tareas no finalizadas:")
        for task in tasks:
            if not task.getFinished():
                print(task.getDescription())

    def getUserInput(self):
        return input("Ingrese el índice de la tarea, 'a' para agregar una nueva tarea, o 'q' para salir: ")
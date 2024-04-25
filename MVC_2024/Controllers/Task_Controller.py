from Views import Task_View
from Models import Task_Model

#class Task_Controller:
    
def __init__(self):
    # Referencia al modelo
    self.tasks = []
    # Referencia a la vista
    self.view = Task_View()

def add_task(self, description, duration, project, developer):
    # Crear una nueva instancia de Task_Model
    new_task = Task_Model(description, duration, project, developer)
    # Agregar la nueva tarea a la lista de tareas
    self.tasks.append(new_task)

def toggle_task_fin(self, taskIndex):
    # Verificar si el índice es válido
    if 0 <= taskIndex < len(self.tasks):
        # Cambiar el estado de finalización de la tarea
        self.tasks[taskIndex].toggleFinished()

def showAllTasks(self):
    # Llamar al método showAllTasks de la vista y pasarle la lista de tareas
    self.view.showAllTasks(self.tasks)

def runController(self):
    while True:
        # Mostrar todas las tareas en la vista
        self.view.showAllTasks(self.tasks)
        # Capturar la entrada del usuario desde la vista
        user_input = self.view.getUserInput()
        if user_input == "q":
            break
        elif user_input == "a":
            # Pedir los detalles de la nueva tarea
            description = input("Ingrese la descripción de la tarea: ")
            duration = int(input("Ingrese la duración de la tarea (en horas): "))
            project = input("Ingrese el nombre del proyecto: ")
            developer = input("Ingrese el nombre del desarrollador: ")
            # Agregar la nueva tarea
            self.add_task(description, duration, project, developer)
        else:
            try:
                # Intentar convertir la entrada a un índice de tarea
                task_index = int(user_input)
                # Cambiar el estado de finalización de la tarea
                self.toggle_task_fin(task_index)
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un índice de tarea o 'a' para agregar una nueva tarea.")
runController()
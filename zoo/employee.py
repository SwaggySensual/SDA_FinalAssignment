# from task import Task
# from zone import Zone

class Employee:
    def __init__(self, ID, working_hours, working_days):
        self.ID = ID
        self.__salary = 0
        self.WorkingHours = working_hours
        self.WorkingDays = working_days
        self.Task = None

    def AssignTask(self, task):
        self.Task = task
        task.SetStatus(True)

    def ExecuteTask(self, zone):
        if self.Task.Type == "Feed":
            zone.FillFoodContainers()
        
    
        
        

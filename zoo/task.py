class Task:
    def __init__(self, ID, task_type, priority, zoneID=None, animalID=None):
        self.ID = ID
        self.Type = task_type
        self.Priority = priority
        self.__status = False
        self.ZoneID = zoneID
        self.AnimalID = animalID

    def ExecuteTask(self, task):
        print("executing task")
        # if done or something
        self.SetStatus(True)

    def SetStatus(self, status):
        ## ToDo: check if execution was done
        self.__status = status

    def GetStatus(self):
        return self.__status

        
        

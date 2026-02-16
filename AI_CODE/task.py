

class Task:
    def __init__(self, id, name, processing_time, due_time, release_time=0):
        self.id = id
        self.name = name
        self.processing_time = processing_time 
        self.due_time = due_time                  
        self.release_time = release_time          

#========================================================================================

    def __repr__(self):
        return (f"Task(id={self.id}, name={self.name}, "
                f"processing={self.processing_time}, due={self.due_time}, "
                f"release={self.release_time})")

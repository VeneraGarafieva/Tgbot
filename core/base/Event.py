class Event:
    @property
    def id(self):
        return self.__class__.__name__

    def check(self, *args, **kwargs) -> bool:
        return False
    
    def action(self, *args, **kwargs):
        pass

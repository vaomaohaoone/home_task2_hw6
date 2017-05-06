import datetime

####################################################################################################

status = ("in_progress", "ready",)

####################################################################################################

class Task:
    def __init__(self, title, estimate, state=status[0]):
        if (type(title) != type('')):
            raise TypeError('Incorrect type of title: ' + type(title))
        if (type(estimate) != type(datetime.date.today())):
            raise TypeError('Incorrect type of estimate: ' + type(estimate))
        if (type(state) != type('')):
            raise TypeError('Incorrect type of state: ' + type(state))
        if ((state != 'in_progress') and (state != 'ready')):
            raise ValueError('Incorrect state')
        self.title = title
        self.estimate = estimate
        self.state = state

    remaining = property()

    @remaining.getter
    def remaining(self):
        if(self.state == status[0]):
            return self.estimate - datetime.date.today()
        else:
            return  0


    is_failed = property()

    @is_failed.getter
    def is_failed(self):
        if (self.state == status[0] and self.estimate < datetime.date.today()):
            return True
        else:
            return False
    def __repr__(self):
        return "title: %s, estimate: %s, status: %s" % (self.title, self.estimate, self.state)
    def ready(self):
        if (self.state == status[0]):
            self.state = status[1]


####################################################################################################

class Roadmap:
    def __init__(self, tasks=[]):
        self.tasks = tasks


    def filter(self, state):
        if (type(state)!=type(status[0])):
            raise TypeError('is not a string')
        for i in self.tasks:
            if (i.state == state):      ### потому что сравнение по хэшкоду
                yield i

    today = property()

    @today.getter
    def today(self):
        for x in self.tasks:
            if (x.estimate == datetime.date.today()):
                yield x

####################################################################################################

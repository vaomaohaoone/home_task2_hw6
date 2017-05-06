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
        return self.estimate - datetime.date.today()

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

from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


def get_dataset():
    with open("dataset.yml", 'rt', encoding='utf-8') as input:
        package = load(input, Loader=Loader)
        dataset = package.get('dataset')
        if not isinstance(dataset, list):
            raise ValueError('wrong format')
        yield from dataset


dataset = list(get_dataset())


####################################################################################################

class WSGIApplication(object):
    response_headers = [
        ('Content-Type', 'text/html'),
        ('Server', 'WSGIExample/1.0'),
    ]

    def __init__(self, environment, start_response):
        self.environment = environment
        self.start_response = start_response

    def __iter__(self):
        greetings = ''
        self.start_response('200 OK', self.response_headers)
        date = datetime.date.today()
        for data in dataset:
            task = Task(data[0], data[2], data[1])
            if ((task.remaining < datetime.timedelta(days=3)) and task.state == status[0]):
                greetings = greetings + task.title + '<br>'
        yield greetings.encode('utf-8')


####################################################################################################

from wsgiref.simple_server import make_server

http_server = make_server('127.0.0.1', 12345, WSGIApplication)
http_server.handle_request()

from misc.CustomElements import Dispatcher
from api.authentication import AuthenticationAdmin
from api.authentication import AuthenticationTeam
from api.authentication import AuthenticationPublic
from api.authentication.AuthenticationConstants import AuthenticationType


class AuthenticationFactory:
    def __init__(self, path):
        self.path = path

    @staticmethod
    def getDispatcher():
        dispatcher = Dispatcher()
        dispatcher.add(AuthenticationType.ADMIN, AuthenticationAdmin)
        dispatcher.add(AuthenticationType.TEAM, AuthenticationTeam)
        dispatcher.add(AuthenticationType.PUBLIC, AuthenticationPublic)
        dispatcher.add(None, AuthenticationPublic)
        return dispatcher

    def dispatch(self):
        return self.getDispatcher().get(self.path)

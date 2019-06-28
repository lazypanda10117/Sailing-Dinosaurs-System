from django.views.decorators.csrf import csrf_exempt
from misc.CustomElements import Dispatcher
from ..base.block.Base import AbstractBlockApp
from .CustomPages import EventPage, EventActivityPage, EventActivityRankingPage, ScoreCompilingPage
from .CustomProcesses import UpdateEventStatusProcess, EventActivityRankingProcess, ScoreCompilingProcess
from panel.module.ModuleRegistry import ModuleRegistry


def index(request):
    return ManagementRankingView().home(request)


def viewDispatch(request, route, param=''):
    return ManagementRankingView().viewDispatch(request, route, param)


@csrf_exempt
def processDispatch(request, route, param=''):
    return ManagementRankingView().processDispatch(request, route, param)


class ManagementRankingView(AbstractBlockApp.AppView):
    # Block App Base View Inherited Functions
    def getBaseAppName(self):
        return ModuleRegistry.MANAGEMENT_RANKING

    def home(self, request):
        return super().index(request, 'panel.module.management_ranking.view_dispatch', ['event'])

    def setViewDispatcher(self):
        dispatcher = Dispatcher()
        dispatcher.add('event', EventPage)
        dispatcher.add('activity', EventActivityPage)
        dispatcher.add('activity ranking', EventActivityRankingPage)
        dispatcher.add('compiler', ScoreCompilingPage)
        return dispatcher

    def setProcessDispatcher(self):
        dispatcher = Dispatcher()
        dispatcher.add('activity status', UpdateEventStatusProcess)
        dispatcher.add('activity ranking', EventActivityRankingProcess)
        dispatcher.add('compiler', ScoreCompilingProcess)
        return dispatcher

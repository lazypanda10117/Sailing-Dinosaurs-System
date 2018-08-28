from django.views.decorators.csrf import csrf_exempt
from misc.CustomElements import Dispatcher
from ..base.block.Base import AbstractBlockApp
from .CustomPages import EventPage, EventActivityPage, EventActivityRankingPage
from .CustomProcesses import UpdateEventStatusProcess, EventActivityRankingProcess


def index(request):
    return ManagementRankingView().home()


def viewDispatch(request, route, param=''):
    dispatcher = ManagementRankingView().setViewDispatcher()
    page = dispatcher.get(route)(request, param)
    return page.render()


@csrf_exempt
def processDispatch(request, route, param=''):
    dispatcher = ManagementRankingView().setProcessDispatcher()
    page = dispatcher.get(route)(request, param)
    return page.process()


class ManagementRankingView(AbstractBlockApp.AppView):
    # Block App Base View Inherited Functions
    def home(self):
        return super().index('panel.module.management_ranking.view_dispatch', ['event'])

    def setViewDispatcher(self):
        dispatcher = Dispatcher()
        dispatcher.add('event', EventPage)
        dispatcher.add('activity', EventActivityPage)
        dispatcher.add('activity ranking', EventActivityRankingPage)
        return dispatcher

    def setProcessDispatcher(self):
        dispatcher = Dispatcher()
        dispatcher.add('activity status', UpdateEventStatusProcess)
        dispatcher.add('activity ranking', EventActivityRankingProcess)
        return dispatcher

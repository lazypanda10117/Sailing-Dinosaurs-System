from django.views.decorators.csrf import csrf_exempt
from misc.CustomElements import Dispatcher
from ..base.block.Base import AbstractBlockApp


def index(request):
    return ManagementNewsView().authenticateModule(
        request,
        ManagementNewsView().home())


def viewDispatch(request, route, param=''):
    return ManagementNewsView().authenticateModule(
        request,
        ManagementNewsView().viewDispatch(request, route, param))


@csrf_exempt
def processDispatch(request, route, param=''):
    return ManagementNewsView().authenticateModule(
        request,
        ManagementNewsView().processDispatch(request, route, param))


class ManagementNewsView(AbstractBlockApp.AppView):
    # Block App Base View Inherited Functions
    def getBaseAppName(self):
        return "NewsModule"

    def home(self):
        return super().index('panel.module.management_news.view_dispatch', ['choice'])

    def setViewDispatcher(self):
        dispatcher = Dispatcher()
        return dispatcher

    def setProcessDispatcher(self):
        dispatcher = Dispatcher()
        return dispatcher

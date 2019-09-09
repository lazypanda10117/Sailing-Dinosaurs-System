from django.views.decorators.csrf import csrf_exempt

from api.functional_api import LoggerAPI
from misc.CustomElements import Dispatcher
from panel.module_permission import ModulePermission
from panel.module.base.block.Base import AbstractBlockApp
from panel.module.management_data.CustomView import CustomView
from panel.module.management_data.GeneralView import GeneralView
from panel.module.ModuleRegistry import ModuleRegistry


def index(request):
    return ModulePermission(request).verifyRequest(
        ManagementDataView().getBaseAppName(),
        ManagementDataView().home(request),
        None
    )


def pruneLog(request):
    result = index(request)
    if result is not None:
        LoggerAPI(request).pruneLog()
    return result


@csrf_exempt
def viewDispatch(request, param, route):
    dispatcher = ManagementDataView().setViewDispatcher()
    view = dispatcher.get(route)(request)
    return ModulePermission(request).verifyRequest(
        ManagementDataView().getBaseAppName(),
        view.dispatch(param),
        None
    )


class ManagementDataView(AbstractBlockApp.AppView):
    # Block App Base View Inherited Functions
    def getBaseAppName(self):
        return ModuleRegistry.MANAGEMENT_DATA

    def home(self, request):
        return super().index(request, 'panel.module.management_data.view_dispatch_param', ['event', 'custom'])

    def setViewDispatcher(self):
        dispatcher = Dispatcher()
        dispatcher.add('general', GeneralView)
        dispatcher.add('custom', CustomView)
        return dispatcher

    def setProcessDispatcher(self):
        pass

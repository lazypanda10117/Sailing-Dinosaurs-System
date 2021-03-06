from misc.CustomElements import Dispatcher
from panel.module.ModuleRegistry import ModuleRegistry
from panel.module.base.structure.data_app.CoreProcesses import CoreDataProcess
from panel.module.management_event.CustomComponents.FleetRaceComponent import FleetRaceComponent


class EventDataProcess(CoreDataProcess):
    def _setAppName(self):
        return ModuleRegistry.MANAGEMENT_EVENT

    def _setViewDispatcher(self):
        dispatcher = Dispatcher()
        dispatcher.add('fleet', FleetRaceComponent)
        return dispatcher

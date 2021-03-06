from abc import abstractmethod

from misc.CustomElements import Dispatcher
from panel.component.CustomElements import Form
from panel.module.base.structure.data_app.constants import ActionType
from panel.module.base.structure.data_app.utils import QueryTermUtils
from panel.module.base.structure.data_app.CoreComponents.CoreDataComponentConstructor import CoreDataComponentConstructor


class CoreDataFormView(CoreDataComponentConstructor):
    def __init__(self, request, app_name, base_class, mutable, guard):
        super().__init__(request, app_name, base_class, mutable, guard)
        self.validation_set = self._setValidationSet()
        self.form_object = self._setFormObject()
        self.populate_data_dispatcher = self._setPopulateDataDispatcher()

    @abstractmethod
    def _setValidationSet(self):
        pass

    @abstractmethod
    def _setFormObject(self):
        pass

    @abstractmethod
    def getFieldData(self, **kwargs):
        pass

    # To determine whether an action requires populating preexisting data for a form
    def _setPopulateDataDispatcher(self):
        dispatcher = Dispatcher()
        dispatcher.add(ActionType.ADD, False)
        dispatcher.add(ActionType.EDIT, True)
        dispatcher.add(ActionType.DELETE, True)
        return dispatcher

    # Default return values for custom form components
    def getChoiceData(self, **kwargs):
        return None

    def getDBMap(self, **kwargs):
        return None

    def getMultiChoiceData(self, **kwargs):
        return None

    def getSearchElement(self, **kwargs):
        return None

    def render(self, **kwargs):
        app_name = kwargs.pop('app_name')
        action = kwargs.pop('action')
        route = kwargs.pop('route')

        # There should only have element_id left inside kwargs
        data = dict(
            field_data=self.getFieldData(**kwargs),
            choice_data=self.getChoiceData(**kwargs),
            multi_choice_data=self.getMultiChoiceData(**kwargs)
        )

        special_context = dict(
            search=self.getSearchElement(**kwargs)
        )

        return Form(
            form_path='_{}_form'.format(action),
            form_name=route,
            form_action=action,
            destination=QueryTermUtils(self.request).getRedirectDestination(app_name=app_name, route=route),
            form=self.form_object(data=data),
            special_context=special_context
        )

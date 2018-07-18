from abc import ABC, abstractmethod
from ..HelperClass import *
from ..generalFunctions import *

from ..models import *
from ..forms import *

class AbstractCustomClass(ABC):

    def __init__(self, request, base_class, validation_table):
        self.dispatcher = self.setViewDispatcher();
        self.request = request;
        self.base_class = base_class;
        self.validation_table = validation_table;

    def setViewDispatcher(self):
        dispatcher = Dispatcher();
        dispatcher.add('add', True);
        dispatcher.add('edit', True);
        dispatcher.add('delete', True);
        dispatcher.add('view', True);
        return dispatcher;

### View Process Functions

    @abstractmethod
    def abstractFormProcess(self, action, **kwargs):
        pass;

    def add(self):
        return self.abstractFormProcess('add');

    def edit(self, id):
        return self.abstractFormProcess('edit', id=id);

    def delete(self, id):
        return self.abstractFormProcess('delete', id=id);

### View Generating Functions

    def grabData(self, *args):
        #args[0] = action, args[1] = form_path, args[2] = element_id
        if args[0] == 'view':
            return self.grabTableData(form_path=args[1]);
        elif args[0] == 'add':
            return self.grabFormData(action=args[0], element_id=args[2]);
        if args[0] in {'edit', 'delete'}:
            if args[2]:
                return self.grabFormData(action=args[0], element_id=args[2]);
            else:
                return {"Error": "Insufficient Parameters"};
        else:
            return {"Error": "Unknown Error"};

    ### Form Generating Functions
    def populateDispatcher(self):
        dispatcher = Dispatcher();
        dispatcher.add('add', False);
        dispatcher.add('edit', True);
        dispatcher.add('delete', True);
        return dispatcher;

    @abstractmethod
    def getFieldData(self, **kwargs):
        pass;

    @abstractmethod
    def getChoiceData(self):
        pass;

    @abstractmethod
    def getDBMap(self, data):
        pass;

    @abstractmethod
    def getMultiChoiceData(self):
        pass;

    @abstractmethod
    def getSearchElement(self, **kwargs):
        pass;

    def grabFormData(self, **kwargs):
        data = {
            "field_data": self.getFieldData(**kwargs),
            "choice_data": self.getChoiceData(),
            "multi_choice_data": self.getMultiChoiceData()
        }
        special_field = {
            "search": self.getSearchElement(**kwargs)
        }
        return {"data": data, "special_field": special_field};

    ### Table Generating Functions
    def getTableHeader(self):
        return self.getTableSpecificHeader() + ["edit", "delete"];

    @abstractmethod
    def getTableSpecificHeader(self):
        pass;

    def getTableRow(self, content):
        rowContent = {};
        rowContent["db_content"] = self.getTableRowContent(content);
        rowContent["button"] = self.makeEditDeleteBtn('custom', str(content.id));
        return rowContent;

    @abstractmethod
    def getTableRowContent(self, content):
        pass;

    def updateChoiceAsValue(self, field_data, choice_data):
        temp_data = field_data;
        for key, value in choice_data.items():
            temp_data[key] = grabLinkValueFromChoices(value, field_data[key]);
        return temp_data;

    def updateMultipleChoicesAsValues(self, field_data, choice_data):
        temp_data = field_data;
        for key, value in choice_data.items():
            temp_data[key] = grabLinkValueFromChoices(value, field_data[key]);
        return temp_data;

    def updateDBMapAsValue(self, field_data, db_map):
        temp_data = field_data;
        for key, value in db_map.items():
            temp_data[key] = value;
        return temp_data;

    def makeEditDeleteBtn(self, path, id):
        editBtn = Button('Edit', 'info', generateGETURL(path, {"action": 'edit', "element_id": id}));
        deleteBtn = Button('Delete', 'danger', generateGETURL(path, {"action": 'delete', "element_id": id}))
        return [editBtn, deleteBtn];

    def getTableContent(self, **kwargs):
        return [self.getTableRow(content) for content in sorted(filterModelObject(
            self.base_class, **kwargs), key=lambda q: q.id)];

    def grabTableData(self, form_path):
        tableHeader = self.getTableHeader();
        tableContent = self.getTableContent();
        table = Table(self.base_class, form_path).makeCustomTables(tableHeader, tableContent);
        return [table];
from .HelperClass import *
from .generalFunctions import *
from .CustomViewClass import *

from .models import *
from .forms import *

class CustomView:

    def __init__(self, request):
        self.view_dispatcher = self.setDispatcher();
        self.session_name = 'custom_view';
        self.request = request;

    def setDispatcher(self):
        dispatcher = Dispatcher();
        dispatcher.add('school', {'class': SchoolView, 'form': SchoolForm});
        dispatcher.add('account', {'class': AccountView, 'form': AccountForm});
        dispatcher.add('team', {'class': TeamView, 'form': TeamForm});
        dispatcher.add('member', {'class': MemberView, 'form': MemberForm});
        dispatcher.add('member group', {'class': MemberGroupView, 'form': MemberGroupForm});
        dispatcher.add('fleet', {'class': EventCreationView, 'form': EventCreationForm});
        dispatcher.add('group', {'class': EventCreationView, 'form': EventCreationForm});
        return dispatcher;

    def dispatch(self, form_path):
        self.form_path = form_path;
        def CustomViewDisplay():
            def actionView(data):
                type = dict(table=True);
                return dict(page_title=page_title, type=type, context=data);

            def actionAdd(data):
                self.request.session[self.session_name] = getViewJSON(action, None);
                type = dict(form=True);
                content = Form('_add_form', form_path, action, destination,
                               self.view_dispatcher.get(self.form_path)["form"](data=data['data']));
                specialContent = data['special_field'];
                return dict(page_title=page_title, type=type, context=content, special_context=specialContent);

            def actionEdit(data):
                if element_id is None:
                    return HttpResponse('{"Response": "Error: No Element ID Provided"}');
                else:
                    self.request.session[self.session_name] = getViewJSON(action, element_id);
                    type = dict(form=True);
                    content = Form('_edit_form', form_path, action, destination,
                                   self.view_dispatcher.get(self.form_path)["form"](data=data['data']));
                    specialContent = data['special_field'];
                    return dict(page_title=page_title, type=type, context=content, special_context=specialContent);

            def actionDelete(data):
                if element_id is None:
                    return HttpResponse('{"Response": "Error: No Element ID Provided"}');
                else:
                    self.request.session[self.session_name] = getViewJSON(action, element_id);
                    type = dict(form=True);
                    content = Form('_delete_form', form_path, action, destination,
                                   self.view_dispatcher.get(self.form_path)["form"](data=data['data']));
                    specialContent = data['special_field'];
                    return dict(page_title=page_title, type=type, context=content, special_context=specialContent);

            def setFunctionDispatcher():
                dispatcher = Dispatcher();
                dispatcher.add('view', actionView);
                dispatcher.add('add', actionAdd);
                dispatcher.add('edit', actionEdit);
                dispatcher.add('delete', actionDelete);
                return dispatcher;

            action = (lambda x: x if x else 'view')(self.request.GET.get("action"));
            element_id = self.request.GET.get("element_id");
            page_title = (self.form_path + " " + action).title();
            destination = 'customProcess';
            currentData = (lambda x: x if x else None)(self.view_dispatcher.get(self.form_path));
            currentClass = currentData["class"];

            functionDispatch = setFunctionDispatcher();

            return (lambda x: render(self.request, 'console/generate.html',
                                     x(currentClass(self.request).grabData(action, form_path, element_id)))
            if x else HttpResponse('{"Response": "Error: Insufficient Parameters"}'))(functionDispatch.get(action));

        def CustomViewLogic():
            def actionAdd():
                currentClass(self.request).add();

            def actionEdit():
                currentClass(self.request).edit(element_id);

            def actionDelete():
                currentClass(self.request).delete(element_id);

            def setFunctionDispatcher():
                dispatcher = Dispatcher();
                dispatcher.add('add', actionAdd);
                dispatcher.add('edit', actionEdit);
                dispatcher.add('delete', actionDelete);
                return dispatcher;

            currentData = (lambda x: x if x else None)(self.view_dispatcher.get(self.form_path));
            currentClass = currentData["class"];

            self.request_variables = self.request.session[self.session_name];
            self.request.session[self.session_name] = None;
            action = self.request_variables["action"];
            element_id = self.request_variables["id"];

            functionDispatch = setFunctionDispatcher();
            functionDispatch.get(action)();
            return HttpResponseRedirect('custom');

        return kickRequest(self.request, True,
                           (lambda x: CustomViewLogic() if x else CustomViewDisplay())
                           (self.request.method == 'POST'));
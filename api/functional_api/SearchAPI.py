import json
from django.apps import apps
from django.http import HttpResponse

from api.authentication import AuthenticationGuardType
from misc.CustomFunctions import ModelFunctions
from api.base import AbstractCoreAPI


class SearchAPI(AbstractCoreAPI):
    def __init__(self, request):
        super().__init__(request=request, permission=AuthenticationGuardType.PUBLIC_GUARD)

    @staticmethod
    def search(model_name, key, term):
        # add a list of viewable models or just refactor to use api later
        resultList = dict()
        model = apps.get_model(app_label='cicsa_ranking', model_name=model_name)
        keyDict = (lambda x: {} if x is None else json.loads(key))(key)
        termDict = (lambda x: {} if x is None else json.loads(term))(term)
        newTermDict = dict()
        for key, val in termDict.items():
            newTermDict[key + '__icontains'] = val
        searchDict = {**keyDict, **newTermDict}

        for obj in ModelFunctions.filterModelObject(model, **searchDict):
            tempDict = vars(obj)
            tempDict.pop('_state')
            identifier = tempDict['id']
            resultList[identifier] = tempDict
        return HttpResponse(json.dumps(resultList, default=str))

    def authenticate(self):
        pass

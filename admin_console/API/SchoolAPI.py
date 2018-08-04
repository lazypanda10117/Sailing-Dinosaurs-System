import json
from .API import *
from ..generalFunctions import *
from ..models import *

class SchoolAPI(API):
    def __init__(self, request):
        self.request = request;

    def getSchools(self, **kwargs):
        return filterModelObject(School, **kwargs);

    def getSchool(self, **kwargs):
        return getModelObject(School, **kwargs);
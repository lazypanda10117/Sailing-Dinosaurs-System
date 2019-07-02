from api.authentication.services.base import BaseService
from cicsa_ranking import ArchiveModel


class ArchiveService(BaseService):
    def __isArchived(self, obj):
        return obj.__class__ in [ArchiveModel] and obj.archived

    def __filterArchived(self, objects):
        return [o for o in objects if not self.__isArchived(o)]

    def _verifyADD(self):
        return self._returnTransformer(self.__filterArchived(self.objects))

    def _verifyEDIT(self):
        return self._returnTransformer(self.__filterArchived(self.objects))

    def _verifyDELETE(self):
        return self._returnTransformer(self.__filterArchived(self.objects))

    def _verifyVIEW(self):
        return self._returnTransformer(self.objects)

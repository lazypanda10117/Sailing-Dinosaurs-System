from cicsa_ranking.models import Config
from api.base.GeneralModelAPI import GeneralModelAPI
from api.model_api.AccountAPI import AccountAPI


class ConfigAPI(GeneralModelAPI):
    @staticmethod
    def getBaseClass():
        return Config

    def getAdminIDs(self):
        return [account.id for account in AccountAPI(self.request).filterSelf(account_type="admin")]
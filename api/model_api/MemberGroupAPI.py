from cicsa_ranking.models import MemberGroup
from misc.CustomFunctions import ModelFunctions, UrlFunctions
from ..base.GeneralModelAPI import GeneralModelAPI


class MemberGroupAPI(GeneralModelAPI):
    @staticmethod
    def getBaseClass():
        return MemberGroup

    def getMemberGroupName(self, member_group_id):
        if member_group_id is not None:
            member_group = self.auth_class.authenticate(
                'view', ModelFunctions.getModelObject(MemberGroup, id=member_group_id))
            member_group_name = member_group.member_group_name
            return member_group_name
        return 'Unlinked'

    def getMemberGroupLink(self, member_group_id):
        if member_group_id is not None:
            return UrlFunctions.getModifyLink('member group', id=member_group_id) + '&base=event_mgmt'
        return '#'

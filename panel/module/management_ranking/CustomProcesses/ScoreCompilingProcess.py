from django.shortcuts import redirect
from django.shortcuts import reverse

from misc.CustomFunctions import RequestFunctions
from api.model_api import EventAPI
from api.model_api import SummaryAPI
from panel.module.base.block.CustomProcesses import AbstractBaseProcess


class ScoreCompilingProcess(AbstractBaseProcess):
    def process(self):
        post_dict = dict(self.request.POST)
        event_id = int(self.param["id"])
        related_summaries = SummaryAPI(self.request).filterSelf(summary_event_parent=event_id)
        for i in range(1, int(len(post_dict)/4)+1):
            school_id = int(RequestFunctions.getSingleRequestObj(post_dict, 'school_id_' + str(i)))
            score = int(RequestFunctions.getSingleRequestObj(post_dict, 'score_' + str(i)))
            ranking = int(RequestFunctions.getSingleRequestObj(post_dict, 'ranking_' + str(i)))
            override_ranking = int(RequestFunctions.getSingleRequestObj(post_dict, 'override_ranking_' + str(i)))
            summary_id = related_summaries.get(summary_event_school=school_id).id
            result = dict(ranking=ranking, override_ranking=override_ranking, race_score=score)
            SummaryAPI(self.request).updateSummaryResult(summary_id, result)
        EventAPI(self.request).updateEventStatus(event_id, 'done')
        return redirect(
            reverse(
                'panel.module.management_ranking.view_dispatch_param',
                args=['activity', event_id]
            )
        )

    def parseParams(self, param):
        super().parseMatch('\d+')
        param = dict(id=param)
        return param

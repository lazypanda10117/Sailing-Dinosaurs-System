from cicsa_ranking.models import Score
from api.base.GeneralModelAPI import GeneralModelAPI


class ScoreAPI(GeneralModelAPI):
    @staticmethod
    def getBaseClass():
        return Score

    def getSeasonScoreValue(self, school_id, season_id):
        try:
            score = self.getSelf(score_school=school_id, score_season=season_id)
            if score.score_override_value:
                return score.score_override_value
            return score.score_value
        except Exception as e:
            print(e)
            return -1

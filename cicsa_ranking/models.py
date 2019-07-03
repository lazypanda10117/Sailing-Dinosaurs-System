from django.contrib.postgres.fields import JSONField, ArrayField
from django.db import models

class BaseModel(models.Model):
    class Meta:
        abstract = True

    def __archivable__(self):
        return False
    def __has_history__(self):
        return False

# We can toggle the object to be archived or not
class ArchivableModel(BaseModel):
    archived = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def __archivable__(self):
        return True

# We can have the same object but tied to a different season
class HasHistoryModel(BaseModel):
    season = models.ForeignKey("Season", on_delete=models.CASCADE)
    universal_id = models.IntegerField() # Somehow default to id?

    class Meta:
        abstract = True

    def __has_history__(self):
        return True

# Use as test of ArchivableModel
class Event(ArchivableModel):
    EVENT_CLASS_RANK_A = 0
    EVENT_CLASS_RANK_B = 1

    EVENT_NAME_FINAL_RACE = ["Fleet Race National"]

    EVENT_STATUS_PENDING = "pending"
    EVENT_STATUS_RUNNING = "running"
    EVENT_STATUS_DONE = "done"

    event_name = models.CharField(max_length=200)
    event_description = models.CharField(max_length=1500)
    event_status = models.CharField(max_length=50)  # pending, running, done
    event_type = models.IntegerField()
    event_class = models.IntegerField(default=EVENT_CLASS_RANK_A)
    event_host = models.IntegerField()
    event_location = models.CharField(max_length=1000)
    event_season = models.IntegerField()
    event_region = models.IntegerField()
    event_boat_rotation_name = models.CharField(max_length=2000)
    event_race_number = models.IntegerField()
    event_team_number = models.IntegerField()  # school number
    event_school_ids = ArrayField(models.CharField(max_length=200), blank=True)
    event_rotation_detail = JSONField(blank=True)  # (team id: [rotation sequence], for each team)
    event_start_date = models.DateField(blank=True)
    event_end_date = models.DateField(blank=True)
    event_create_time = models.DateTimeField(auto_now_add=True, blank=True)


class EventTeam(models.Model):
    event_team_event_activity_id = models.IntegerField()
    event_team_id = models.IntegerField()
    event_team_member_group_id = models.IntegerField(blank=True, null=True)


class EventTag(models.Model):
    event_tag_event_id = models.IntegerField()
    event_tag_name = models.CharField(max_length=200)


class Region(models.Model):
    region_name = models.CharField(max_length=100)


class Season(models.Model):
    season_name = models.CharField(max_length=200)


class ScoreMapping(models.Model):
    score_name = models.CharField(max_length=200)
    score_value = models.CharField(default="RACE+1", max_length=100)


class EventType(models.Model):
    event_type_name = models.CharField(max_length=200)


class EventActivity(models.Model):
    event_activity_event_parent = models.IntegerField()
    event_activity_event_tag = models.IntegerField()
    event_activity_name = models.CharField(max_length=100)  # autogenerated
    event_activity_order = models.IntegerField()  # 1,2,3 ...
    event_activity_result = JSONField()  # json
    event_activity_type = models.CharField(max_length=50)  # i.e. races
    event_activity_note = models.CharField(max_length=1500)
    event_activity_status = models.CharField(max_length=50)


class Summary(models.Model):
    summary_event_parent = models.IntegerField()
    summary_event_school = models.IntegerField(default=0)
    summary_event_ranking = models.IntegerField(default=0)
    summary_event_override_ranking = models.IntegerField(default=0)
    summary_event_race_score = models.IntegerField(default=0)
    summary_event_league_score = models.FloatField(default=0)
    summary_event_override_league_score = models.FloatField(default=0)


class Score(models.Model):
    score_value = models.IntegerField(default=0)
    score_override_value = models.IntegerField(default=0)
    score_school = models.IntegerField()
    score_season = models.IntegerField()


class Log(models.Model):
    log_creator = models.IntegerField()  # if sql, then system (-1), else user id
    log_content = JSONField()
    log_type = models.CharField(max_length=50)  # admin, school, system
    log_create_time = models.DateTimeField(auto_now_add=True, blank=True)


# Use as test of HasHistoryModel
class School(HasHistoryModel):
    school_name = models.CharField(max_length=200)
    school_region = models.IntegerField()
    school_status = models.CharField(max_length=50)
    school_default_team_name = models.CharField(max_length=200, default='')


class Team(models.Model):
    team_name = models.CharField(max_length=200)
    team_school = models.IntegerField()
    team_tag_id = models.IntegerField()
    team_status = models.CharField(max_length=50)


class MemberGroup(models.Model):
    member_group_name = models.CharField(max_length=200)
    member_group_school = models.IntegerField()
    member_group_member_ids = ArrayField(models.IntegerField())


class Member(models.Model):
    member_name = models.CharField(max_length=200)
    member_school = models.IntegerField()
    member_email = models.EmailField()
    member_status = models.CharField(max_length=50)


class Account(models.Model):
    ACCOUNT_ADMIN = "admin"
    ACCOUNT_SCHOOL = "school"
    account_type = models.CharField(max_length=50)  # school, admin
    account_email = models.EmailField()
    account_salt = models.CharField(max_length=200)
    account_password = models.CharField(max_length=200)
    account_status = models.CharField(max_length=50)
    account_linked_id = models.IntegerField(blank=True, null=True)


class NewsPost(models.Model):
    NEWS_POST_PINNED = 0
    NEWS_POST_ACTIVE = 1
    NEWS_POST_ARCHIVED = 2
    news_post_title = models.CharField(max_length=200)
    news_post_content = models.CharField(max_length=3000, blank=True)
    news_post_bumps = models.IntegerField(default=0)
    news_post_owner = models.IntegerField()
    news_post_status = models.IntegerField()  # status from above
    news_post_create_time = models.DateTimeField('Post Date', auto_now_add=True, blank=True)


class NewsComment(models.Model):
    news_comment_owner = models.IntegerField()
    news_comment_post_id = models.IntegerField()
    news_comment_content = models.CharField(max_length=1000, blank=True)
    news_comment_create_time = models.DateTimeField('Comment Date', auto_now_add=True, blank=True)


class NewsBump(models.Model):
    news_bump_bumpper_id = models.IntegerField()
    news_bump_post_id = models.IntegerField()
    news_bump_create_time = models.DateTimeField('Bump Date', auto_now_add=True, blank=True)


class Config(models.Model):
    config_current_season = models.IntegerField()

from django.contrib.postgres.fields import JSONField, ArrayField
from django.db import models
from django.utils import timezone

class Event(models.Model):
    event_name = models.CharField(max_length=200);
    event_description = models.CharField(max_length=1500);
    event_status = models.CharField(max_length=50); #pending, running, done
    event_type = models.IntegerField();
    event_host = models.CharField(max_length=150);
    event_location = models.CharField(max_length=1000);
    event_region = models.IntegerField();
    event_boat_number = models.IntegerField();
    event_race_number = models.IntegerField();
    event_team_number = models.IntegerField();
    event_rotation_detail = JSONField(); #(team id: [rotation sequence], for each team)
    event_start_date = models.DateTimeField(blank=True);
    event_end_date = models.DateTimeField(blank=True);
    event_create_time = models.DateTimeField(default=timezone.now(), blank=True);

class EventTeam(models.Model):
    event_team_event_activity_id = models.IntegerField();
    event_team_id = models.IntegerField();
    event_team_member_group_id = models.IntegerField(blank=True);

class EventTag(models.Model):
    event_tag_event_id = models.IntegerField();
    event_tag_name = models.CharField(max_length=200);

class Region(models.Model):
    region_name = models.CharField(max_length=100);

class Season(models.Model):
    season_name = models.CharField(max_length=200);

class ScoreMapping(models.Model):
    score_name = models.CharField(max_length=200);
    score_value = models.IntegerField(default=0);

class EventType(models.Model):
    event_type_name = models.CharField(max_length=200);

class EventActivity(models.Model):
    event_activity_event_parent = models.IntegerField();
    event_activity_event_tag = models.CharField(max_length=100);
    event_activity_name = models.CharField(max_length=100); #optional
    event_activity_order = models.IntegerField(); # 1,2,3 ...
    event_activity_result = JSONField(); #json
    event_activity_type = models.CharField(max_length=200); #i.e. races
    event_activity_note = models.CharField(max_length=500);
    event_activity_status = models.CharField(max_length=50);

class Summary(models.Model):
    summary_event_parent = models.IntegerField();
    summary_event_team = models.IntegerField();
    summary_event_ranking = models.IntegerField();
    summary_event_override_ranking = models.IntegerField();
    summary_event_score = models.FloatField();

class Log(models.Model):
    log_creator = models.IntegerField(); #if sql, then system (-1), else user id
    log_content = JSONField();
    log_type = models.CharField(max_length=50); #admin, school, system
    log_create_time = models.DateTimeField(default=timezone.now(), blank=True);

class School(models.Model):
    school_name = models.CharField(max_length=200);
    school_region = models.IntegerField();
    school_status = models.CharField(max_length=50);
    school_season_score = models.FloatField();

class Team(models.Model):
    team_name = models.CharField(max_length=200);
    team_school = models.IntegerField();
    team_status = models.CharField(max_length=50);

class MemberGroup(models.Model):
    member_group_name = models.CharField(max_length=200);
    member_group_school = models.IntegerField();
    member_group_member_ids = ArrayField(models.IntegerField());

class Member(models.Model):
    member_name = models.CharField(max_length=200);
    member_school = models.IntegerField();
    member_email = models.EmailField();
    member_status = models.CharField(max_length=50);

class Account(models.Model):
    account_type = models.CharField(max_length=50); #school, admin
    account_email = models.EmailField();
    account_salt = models.CharField(max_length=200);
    account_password = models.CharField(max_length=200);
    account_status = models.CharField(max_length=50);
    account_linked_id = models.IntegerField(blank=True, null=True);
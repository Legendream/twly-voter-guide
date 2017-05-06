#from django.contrib.auth.models import User, Group
import django_filters
from rest_framework import viewsets
from rest_framework import filters
from rest_framework import generics
from rest_framework.decorators import api_view

from .serializers import *
from legislator.models import Legislator, LegislatorDetail, Attendance
from candidates.models import Candidates, Terms
from sittings.models import Sittings
from committees.models import Committees, Legislator_Committees
from vote.models import Vote, Legislator_Vote
from bill.models import Bill, Legislator_Bill, Law
from standpoint.models import Standpoint


class LegislatorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Legislator.objects.all().prefetch_related('each_terms', 'each_terms__elected_candidate')
    serializer_class = LegislatorSerializer
    filter_fields = ('uid', 'name')

class LegislatorDetailViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LegislatorDetail.objects.all().select_related('legislator', 'elected_candidate')
    serializer_class = LegislatorDetailSerializer
    filter_fields = ('legislator', 'ad', 'name', 'gender', 'party', 'elected_party', 'caucus', 'constituency', 'county', 'in_office', 'term_start')

class AttendanceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Attendance.objects.all().select_related('sitting', 'legislator')
    serializer_class = AttendanceSerializer
    filter_fields = ('legislator', 'sitting', 'category', 'status')

class CandidatesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Candidates.objects.all()
    serializer_class = CandidatesSerializer
    filter_fields = ('name', 'birth')

class Candidates_TermsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Terms.objects.all().select_related('legislator', 'latest_term')
    serializer_class = Candidates_TermsSerializer
    filter_fields = ('candidate', 'latest_term', 'legislator', 'ad', 'number', 'priority', 'name', 'gender', 'party', 'constituency', 'county', 'district', 'votes', 'votes_percentage', 'elected')

class SittingsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sittings.objects.all().prefetch_related('votes')
    serializer_class = SittingsSerializer
    filter_fields = ('uid', 'name', 'committee', 'date', 'ad', 'session')

class CommitteesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Committees.objects.all()
    serializer_class = CommitteesSerializer
    filter_fields = ('name', 'category')

class Legislator_CommitteesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Legislator_Committees.objects.all().select_related('committee', 'legislator')
    serializer_class = Legislator_CommitteesSerializer
    filter_fields = ('legislator', 'committee', 'ad', 'session', 'chair')

class VoteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Vote.objects.all().select_related('sitting')
    serializer_class = VoteSerializer
    filter_fields = ('voter', 'uid', 'sitting', 'vote_seq', 'content')

class Legislator_VoteFilter(django_filters.FilterSet):
    not_voting = django_filters.Filter(name='decision', lookup_type='isnull')
    class Meta:
        model = Legislator_Vote
        fields = ['legislator', 'vote', 'decision', 'conflict', 'not_voting']

class Legislator_VoteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Legislator_Vote.objects.all().select_related('vote', 'legislator')
    serializer_class = Legislator_VoteSerializer
    filter_class = Legislator_VoteFilter

class LawViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Law.objects.all().select_related('bill')
    serializer_class = LawSerializer
    filter_fields = ('bill', 'uid', 'ad', 'data')

class BillViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Bill.objects.all().prefetch_related('proposer')
    serializer_class = BillSerializer
    filter_fields = ('uid', 'ad', 'data')

class Legislator_BillViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Legislator_Bill.objects.all().select_related('bill', 'legislator')
    serializer_class = Legislator_BillSerializer
    filter_fields = ('legislator', 'bill', 'role')

class StandpointViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Standpoint.objects.all()
    serializer_class = StandpointSerializer
    filter_fields = ('title', 'vote', 'pro')

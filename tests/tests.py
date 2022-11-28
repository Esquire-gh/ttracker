from rest_framework import status
from rest_framework.test import APITestCase

from log.models import Log
from project.models import Project
from .factories import (
    ProjectOwnerFactory,
    ProjectParticipantFactory,
    ProjectParticipantTwoFactory
)


class TestProjectPermissions(APITestCase):

    def setUp(self):
        self.project_owner = ProjectOwnerFactory()
        self.project_participant = ProjectParticipantFactory()
        self.project_participant_two = ProjectParticipantTwoFactory()
        self.random_user = ProjectParticipantFactory()

        self.home_url = 'http://localhost:8000/api/projects/'

        self.project_1 = Project.objects.create(
            title="Project A",
            description="A project using django as backend",
            project_owner=self.project_owner,
            start_date="2022-11-01",
            end_date="2023-11-01"
        )

        self.project_logs_url = f'{self.home_url}{str(self.project_1.id)}/logs/'

        self.test_project_log = {
            "description": "A task for a particular project",
            "time_started": "2022-11-15T22:41:21.328Z",
            "time_ended": "2022-11-16T22:41:21.328Z",
        }

    def test_any_user_creates_project(self):
        test_project_data = {
            "title": "New Project 1",
            "description": "First project",
            "participants": [self.project_participant.id, ],
            "start_date": "2022-11-11",
            "end_date": "2022-11-15"
        }
        self.client.force_authenticate(user=self.random_user)
        response = self.client.post(
            self.home_url, test_project_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_only_project_owner_updates_project(self):
        test_project_update_data = {
            "title": "New Project 1 UPDATED",
            "description": "First project",
        }
        self.client.force_authenticate(user=self.project_owner)
        self.product_detail_url = f'{self.home_url}{str(self.project_1.id)}/'
        response = self.client.patch(
            self.product_detail_url, test_project_update_data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_only_project_participants_can_see_project_logs(self):
        self.project_1.participants.add(self.project_participant)
        self.client.force_authenticate(user=self.project_participant)
        response = self.client.get(
            self.project_logs_url, )

        self.assertEqual(self.project_1.participants.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_random_users_cannot_see_project_logs(self):
        self.client.force_authenticate(user=self.random_user)
        response = self.client.get(
            self.project_logs_url, )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_only_project_participants_create_project_logs(self):
        self.project_1.participants.add(self.project_participant)
        self.client.force_authenticate(user=self.project_participant)
        response = self.client.post(
            self.project_logs_url, self.test_project_log, format="json")

        self.assertEqual(self.project_1.participants.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_project_logs_start_time_not_in_the_future(self):
        invalid_project_log_data = {
            "description": "A task for a particular project",
            "time_started": "2023-11-15T22:41:21.328Z",
            "time_ended": "2023-11-16T22:41:21.328Z",
        }
        self.project_1.participants.add(self.project_participant_two)
        self.client.force_authenticate(user=self.project_participant_two)
        response = self.client.post(
            self.project_logs_url, invalid_project_log_data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_project_logs_end_time_not_less_than_start_time(self):
        invalid_project_log_data = {
            "description": "A task for a particular project",
            "time_started": "2022-11-22T22:41:21.328Z",
            "time_ended": "2022-11-16T22:41:21.328Z",
        }
        self.project_1.participants.add(self.project_participant_two)
        self.client.force_authenticate(user=self.project_participant_two)
        response = self.client.post(
            self.project_logs_url, invalid_project_log_data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_random_user_cannot_create_logs(self):
        self.client.force_authenticate(user=self.random_user)
        response = self.client.post(
            self.project_logs_url, self.test_project_log, format="json")

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_participants_cannot_update_logs_of_others(self):
        participant1_log = Log.objects.create(
            project=self.project_1,
            creator=self.project_participant,
            description="I worked on the creation of the store api",
            time_started="2022-11-15T22:41:21.328Z",
            time_ended="2022-11-15T23:50:21.328Z"
        )
        project_log_update_data = {
            "description": "Changed Log",
            "time_started": "2000-11-15T22:41:21.328Z",
            "time_ended": "2000-11-16T22:41:21.328Z",
        }
        self.project_1.participants.add(self.project_participant)
        self.project_1.participants.add(self.project_participant_two)
        project_log_detail_url = f'{self.home_url}{str(self.project_1.id)}/logs/{participant1_log.id}/'
        response = self.client.put(
            project_log_detail_url,
            project_log_update_data,
            format="json"
        )

        self.assertEqual(self.project_1.logs.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


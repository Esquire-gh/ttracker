import factory
from django.contrib.auth import get_user_model
from faker import Faker

from project.models import Project

User = get_user_model()

fake = Faker()


class ProjectOwnerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = fake.first_name()
    last_name = fake.last_name()
    email = factory.Sequence(lambda n: 'person1{}@example.com'.format(n))
    username = factory.Sequence(lambda n: "user1_%d" % n)
    is_active = True


class ProjectParticipantFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = fake.first_name()
    last_name = fake.last_name()
    email = factory.Sequence(lambda n: 'person2{}@example.com'.format(n))
    username = factory.Sequence(lambda n: "user2_%d" % n)
    is_active = True


class ProjectParticipantTwoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = fake.first_name()
    last_name = fake.last_name()
    email = factory.Sequence(lambda n: 'person4{}@example.com'.format(n))
    username = factory.Sequence(lambda n: "user4_%d" % n)
    is_active = True


class RandomUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = fake.first_name()
    last_name = fake.last_name()
    email = factory.Sequence(lambda n: 'person3{}@example.com'.format(n))
    username = factory.Sequence(lambda n: "user3_%d" % n)
    is_active = True


class ProjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Project

    title = 'Project A'
    description = 'A project about django'
    project_owner = factory.SubFactory(ProjectOwnerFactory)
    participants = factory.RelatedFactory(
        ProjectParticipantFactory)
    start_date = '2022-11-12'
    end_date = '2022-11-12'


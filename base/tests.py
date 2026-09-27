from django.test import TestCase

from .models import Message, Room, Topic, User


class CoreModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='ada',
            email='ada@example.com',
            password='test-password-123',
        )
        self.topic = Topic.objects.create(name='Engineering')
        self.room = Room.objects.create(
            host=self.user,
            topic=self.topic,
            name='Backend Engineering',
            description='API design discussion',
        )

    def test_topic_and_room_string_representation(self):
        self.assertEqual(str(self.topic), 'Engineering')
        self.assertEqual(str(self.room), 'Backend Engineering')

    def test_message_preview_is_limited_to_fifty_characters(self):
        body = 'A' * 75
        message = Message.objects.create(user=self.user, room=self.room, body=body)
        self.assertEqual(str(message), body[:50])

    def test_room_accepts_participants(self):
        self.room.participants.add(self.user)
        self.assertTrue(self.room.participants.filter(pk=self.user.pk).exists())

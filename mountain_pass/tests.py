from django.test import TestCase
from mountain_pass.models import MountainPass, Tourist, MountainPassImage


class MountainPassModelTest(TestCase):
    """ Test module for MountainPass model """

    def test_string_representation(self):
        mountain_pass = MountainPass(title="test")
        self.assertEqual(str(mountain_pass), mountain_pass.title)

    def test_verbose_name_plural(self):
        self.assertEqual(
            str(MountainPass._meta.verbose_name_plural), "Mountain passes")


class TouristModelTest(TestCase):
    """ Test module for Tourist model """

    def test_get_full_name(self):
        tourist = Tourist(first_name="Михамл",
                          middle_name='Юрьевич', last_name='Лермонтов')
        self.assertEqual(Tourist.get_full_name(
            tourist), 'Лермонтов Михамл Юрьевич')

    def test_string_representation(self):
        tourist = Tourist(first_name="Михамл",
                          middle_name='Юрьевич', last_name='Лермонтов')
        self.assertEqual(str(tourist), 'Лермонтов Михамл Юрьевич')


class MountainPassImagetModelTest(TestCase):
    def test_string_representation(self):
        image = MountainPassImage(title='test')
        self.assertEqual(str(image), image.title)

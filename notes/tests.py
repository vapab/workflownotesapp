from django.test import TestCase
from django.urls import reverse
import pytest
from notes.models import Note

def test_homepage_access():
    url = reverse('home')
    assert url == "/"

@pytest.fixture
def new_note(db):
    note = Note.objects.create(
        title='Pytest',
        description='Tutorial on how to apply pytest to a Django application',
        published=True
    )
    return note

def test_search_notes(new_note):
    assert Note.objects.filter(title='Pytest').exists()

def test_update_note(new_note):
    new_note.title = 'Pytest-Django'
    new_note.save()
    assert Note.objects.filter(title='Pytest-Django').exists()

@pytest.fixture
def another_note(db):
    note = Note.objects.create(
        title='More-Pytest',
        description='Tutorial on how to apply pytest to a Django application',
        published=True
    )
    return note

def test_compare_notes(new_note, another_note):
    assert new_note.pk != another_note.pk
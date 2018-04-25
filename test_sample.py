import pytest

def who_da_man():
    return 'Greg'


def test_who_da_man():
    assert who_da_man() == 'Greg'

def test2_who_da_man():
    assert who_da_man() == 'lj'

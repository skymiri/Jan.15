import pytest
from hangman import reveal_letters, all_letters_found


def test_show_letters_vancouver():
    assert reveal_letters("Vancouver", ["A", "V"]) == "V A _ _ _ _ V _ _"
    assert reveal_letters("Vancouver", ["a", "v"]) == "V A _ _ _ _ V _ _"


def test_show_letters_tim():
    assert reveal_letters("TIM", ["G", "V"]) == "_ _ _"


def test_show_letters_pizza():
    assert reveal_letters("PIZZA", ["A", "I", "P", "Z"]) == "P I Z Z A"


def test_all_letters_found():
    assert all_letters_found("PIZZA", ["A", "I", "P", "Z"]) is True


def test_all_letters_found_and_more():
    assert all_letters_found("PIZZA", ["A", "I", "P", "Z", "K", "T"]) is True


def test_not_all_letters_found():
    assert all_letters_found("VANCOUVER", ["A", "V"]) is False

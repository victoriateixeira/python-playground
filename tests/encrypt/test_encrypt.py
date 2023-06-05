from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(234567, 2)

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("abcdef", "2")

    assert encrypt_message("random", 7) == "modnar"
    assert encrypt_message("abcdef", 3) == "cba_fed"
    assert encrypt_message("abcdef", 2) == "fedc_ba"


# def test_message_is_string():
#     with pytest.raises(TypeError, match="tipo inválido para message"):
#         encrypt_message(234567, 2)


# def test_key_is_number():
#     with pytest.raises(TypeError, match="tipo inválido para key"):
#         encrypt_message("abcdef", "2")


# def test_key_higher_than_message_length():
#     assert encrypt_message("abcdef", 7) == "fedcba"


# def test_key_is_odd():
#     assert encrypt_message("abcdef", 3) == "cba_fed"


# def test_key_is_even():
#     assert encrypt_message("abcdef", 2) == "fedc_ba"

# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 22:36:59 2025

@author: Equinox
"""
import sys
import os

# Adds parent folder to Python import path to correctly import logic
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from logic import handle_translation_input, handle_quiz_input

# By testing handle_translation_input() and handle_quiz_input() we are
# effectively testing create_numerals_list(), purify_input(), lat2dec(),
# dec2lat(), letter_conversion(), digit_conversion().
# (Only logic.py function untested is randomize())


# Latin To Decimal Tests

# Valid Tests


def test_valid_3999_number_latin_to_decimal():
    result = handle_translation_input("MMMCMXCIX", "Latin to Decimal")
    assert result == "Result: MMMCMXCIX is 3999"


def test_valid_multiple_C_X_latin_to_decimal():
    result = handle_translation_input("MMCCCLXXXIX", "Latin to Decimal")
    assert result == "Result: MMCCCLXXXIX is 2389"


def test_valid_max_repeat_with_5s_latin_to_decimal():
    result = handle_translation_input("MMMDCCCLXXXVIII", "Latin to Decimal")
    assert result == "Result: MMMDCCCLXXXVIII is 3888"


def test_valid_max_repeat_without_5s_latin_to_decimal():
    result = handle_translation_input("MMMCCCXXXIII", "Latin to Decimal")
    assert result == "Result: MMMCCCXXXIII is 3333"


def test_valid_4s_repeat_latin_to_decimal():
    result = handle_translation_input("MMMCDXLIV", "Latin to Decimal")
    assert result == "Result: MMMCDXLIV is 3444"


def test_valid_5s_repeat_latin_to_decimal():
    result = handle_translation_input("MMMDLV", "Latin to Decimal")
    assert result == "Result: MMMDLV is 3555"


# Invalid tests


def test_invalid_latin_to_decimal_symbols_input():
    result = handle_translation_input("$%#@!", "Latin to Decimal")
    assert "Invalid input" in result


def test__invalid_latin_to_decimal_numbers_input():
    result = handle_translation_input("1234", "Latin to Decimal")
    assert "Invalid input" in result


def test_invalid_number_XL_and_XC_latin_to_decimal():
    result = handle_translation_input("MXLXCII", "Latin to Decimal")
    assert "Invalid input" in result


def test_invalid_number_two_C_before_M_latin_to_decimal():
    result = handle_translation_input("CCM", "Latin to Decimal")
    assert "wrongfully used" in result


def test_invalid_number_two_X_before_C_latin_to_decimal():
    result = handle_translation_input("XXC", "Latin to Decimal")
    assert "wrongfully used" in result


def test_invalid_number_two_I_before_X_latin_to_decimal():
    result = handle_translation_input("IIX", "Latin to Decimal")
    assert "wrongfully used" in result


def test_invalid_number_three_C_before_M_latin_to_decimal():
    result = handle_translation_input("CCM", "Latin to Decimal")
    assert "wrongfully used" in result


def test_invalid_number_three_X_before_C_latin_to_decimal():
    result = handle_translation_input("XXC", "Latin to Decimal")
    assert "wrongfully used" in result


def test_invalid_number_three_I_before_X_latin_to_decimal():
    result = handle_translation_input("IIX", "Latin to Decimal")
    assert "wrongfully used" in result


def test_invalid_number_four_I_after_V_latin_to_decimal():
    result = handle_translation_input("VIIII", "Latin to Decimal")
    assert "wrongfully used" in result


def test_invalid_number_four_X_after_L_latin_to_decimal():
    result = handle_translation_input("LXXXX", "Latin to Decimal")
    assert "wrongfully used" in result


def test_invalid_number_four_C_after_D_latin_to_decimal():
    result = handle_translation_input("DCCCC", "Latin to Decimal")
    assert "wrongfully used" in result


def test_invalid_number_four_I_latin_to_decimal():
    result = handle_translation_input("IIII", "Latin to Decimal")
    assert "wrongfully used" in result


def test_invalid_number_four_X_latin_to_decimal():
    result = handle_translation_input("XXXX", "Latin to Decimal")
    assert "wrongfully used" in result


def test_invalid_number_four_C_latin_to_decimal():
    result = handle_translation_input("CCCC", "Latin to Decimal")
    assert "wrongfully used" in result


def test_rule_3_IC_latin_to_decimal():
    result = handle_translation_input("IC", "Latin to Decimal")
    assert "rule #3" in result


def test_rule_3_XM_latin_to_decimal():
    result = handle_translation_input("XM", "Latin to Decimal")
    assert "rule #3" in result


def test_rule_3_IM_latin_to_decimal():
    result = handle_translation_input("IM", "Latin to Decimal")
    assert "rule #3" in result


def test_invalid_number_VM_latin_to_decimal():
    result = handle_translation_input("VM", "Latin to Decimal")
    assert "wrongfully used" in result


def test_invalid_number_repeated_V_latin_to_decimal():
    result = handle_translation_input("VVI", "Latin to Decimal")
    assert "wrongfully used" in result


def test_invalid_number_repeated_L_latin_to_decimal():
    result = handle_translation_input("LLI", "Latin to Decimal")
    assert "wrongfully used" in result


def test_invalid_number_repeated_D_latin_to_decimal():
    result = handle_translation_input("DDI", "Latin to Decimal")
    assert "wrongfully used" in result


def test_invalid_number_VIX_latin_to_decimal():
    result = handle_translation_input("VIX", "Latin to Decimal")
    assert "wrongfully used" in result


def test_invalid_number_DCM_latin_to_decimal():
    result = handle_translation_input("DCM", "Latin to Decimal")
    assert "wrongfully used" in result


def test_invalid_number_XIIX_latin_to_decimal():
    result = handle_translation_input("XIIX", "Latin to Decimal")
    assert "wrongfully used" in result


def test_invalid_number_CXXC_latin_to_decimal():
    result = handle_translation_input("CXXC", "Latin to Decimal")
    assert "wrongfully used" in result


def test_invalid_number_MCCM_latin_to_decimal():
    result = handle_translation_input("MCCM", "Latin to Decimal")
    assert "wrongfully used" in result


def test_invalid_number_IXI_latin_to_decimal():
    result = handle_translation_input("IXI", "Latin to Decimal")
    assert "wrongfully used" in result


def test_invalid_number_XCX_latin_to_decimal():
    result = handle_translation_input("XCX", "Latin to Decimal")
    assert "wrongfully used" in result


def test_invalid_number_CMC_latin_to_decimal():
    result = handle_translation_input("CMC", "Latin to Decimal")
    assert "wrongfully used" in result


def test_invalid_number_IXV_latin_to_decimal():
    result = handle_translation_input("IXV", "Latin to Decimal")
    assert "wrongfully used" in result


def test_invalid_number_XIVM_latin_to_decimal():
    result = handle_translation_input("XIVM", "Latin to Decimal")
    assert "wrongfully used" in result


def test_invalid_number_IVD_latin_to_decimal():
    result = handle_translation_input("IVD", "Latin to Decimal")
    assert "wrongfully used" in result


def test_invalid_number_out_of_range_latin_to_decimal():
    result = handle_translation_input(
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "Latin to Decimal",
    )
    assert "Invalid input" in result


# Decimal to Latin Tests

# Valid Tests


def test_valid_3999_number_decimal_to_latin():
    result = handle_translation_input("3999", "Decimal to Latin")
    assert result == "Result: 3999 is MMMCMXCIX"


def test_valid_trail_of_8s_decimal_to_latin():
    result = handle_translation_input("3888", "Decimal to Latin")
    assert result == "Result: 3888 is MMMDCCCLXXXVIII"


def test_valid_trail_of_3s_decimal_to_latin():
    result = handle_translation_input("3333", "Decimal to Latin")
    assert result == "Result: 3333 is MMMCCCXXXIII"


def test_valid_trail_of_4s_decimal_to_latin():
    result = handle_translation_input("3444", "Decimal to Latin")
    assert result == "Result: 3444 is MMMCDXLIV"


def test_valid_trail_of_5s_decimal_to_latin():
    result = handle_translation_input("3555", "Decimal to Latin")
    assert result == "Result: 3555 is MMMDLV"


# Invalid Tests


def test_invalid_negative_number_decimal_to_latin():
    result = handle_translation_input("-5", "Decimal to Latin")
    assert result == "Invalid input"


def test_invalid_symbols_decimal_to_latin():
    result = handle_translation_input("32a", "Decimal to Latin")
    assert result == "Invalid input"


def test_invalid_float_number_decimal_to_latin():
    result = handle_translation_input("3.2", "Decimal to Latin")
    assert result == "Invalid input"


def test_invalid_zero_number_decimal_to_latin():
    result = handle_translation_input("0", "Decimal to Latin")
    assert result == "Invalid input"


def test_invalid_out_of_range_number_decimal_to_latin():
    result = handle_translation_input("10000000000000", "Decimal to Latin")
    assert result == "Invalid input"


# Test Quiz Tests

# Correct Answer Tests


def test_quiz_correct_answer():
    message, streak = handle_quiz_input("MMCCLXIV", "2264", 3)
    assert "correct" in message
    assert streak == 4


def test_quiz_correct_answer_99_streak_fire_message():
    message, streak = handle_quiz_input("MMDCXIV", "2614", 99)
    assert "correct" in message
    assert "FIRE" in message
    assert streak == 100


def test_quiz_correct_answer_15_streak_roll_message():
    message, streak = handle_quiz_input("MMMCCCXXXIII", "3333", 16)
    assert "correct" in message
    assert "roll" in message
    assert streak == 17


# Wrong Answer Tests


def test_quiz_wrong_answer():
    message, streak = handle_quiz_input("XIX", "21", 3)
    assert "wrong" in message
    assert streak == 0


def test_quiz_wrong_answer_on_fire_message_gone():
    message, streak = handle_quiz_input("CXCI", "111", 105)
    assert "wrong" in message
    assert "FIRE" not in message
    assert streak == 0


def test_quiz_wrong_answer_on_roll_message_gone():
    message, streak = handle_quiz_input("MMDCXXVI", "3641", 17)
    assert "wrong" in message
    assert "roll" not in message
    assert streak == 0


def test_quiz_wrong_answer_repeat_question_number():
    message, streak = handle_quiz_input("25", "25", 3)
    assert "wrong" in message
    assert streak == 0


def test_quiz_wrong_answer_repeat_question_numeral():
    message, streak = handle_quiz_input("MMMDCXIV", "MMMDCXIV", 42)
    assert "Invalid input" in message
    assert streak == 0


def test_quiz_wrong_answer_negative_decimal():
    message, streak = handle_quiz_input("MCXI", "-1111", 7)
    assert "wrong" in message
    assert streak == 0


def test_quiz_wrong_answer_letters():
    message, streak = handle_quiz_input("XIV", "fourteen", 1)
    assert "Invalid input" in message
    assert streak == 0


def test_quiz_wrong_answer_zero():
    message, streak = handle_quiz_input("M", "0000", 1000)
    assert "wrong" in message
    assert streak == 0


def test_quiz_wrong_answer_random_letters():
    message, streak = handle_quiz_input("15", "XVandstuff", 1)
    assert "wrong" in message
    assert streak == 0

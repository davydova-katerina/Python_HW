import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [(" skypro", "skypro")])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    (" ", ""),
    ("   ", ""),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol", [
    ("Skypro", "S"),
    ("Skypro", "y"),
    ("Skypro", "r"),
])
def test_contains_positive(input_str, symbol):
    assert string_utils.contains("Skypro", "S") == True
    assert string_utils.contains("Skypro", "y") == True
    assert string_utils.contains("Skypro", "r") == True


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol", [
    ("Skypro", "T"),
    ("Skypro", "1"),
    ("Skypro", "x"),
])
def test_contains_negative(input_str, symbol):
    assert string_utils.contains("Skypro", "T") == False
    assert string_utils.contains("Skypro", "1") == False
    assert string_utils.contains("Skypro", "x") == False


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol", [
    ("SkyPro", "S"),
    ("SkyPro", "k"),
    ("SkyPro", "P"),
])
def test_delete_symbol_positive(input_str, symbol,):
    assert string_utils.delete_symbol("SkyPro", "S") == "kyPro"
    assert string_utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert string_utils.delete_symbol("SkyPro", "P") == "Skyro"


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol", [
    ("SkyPro", "Z"),
    ("SkyPro", "1"),
    ("SkyPro", ""),
])
def test_delete_symbol_negative(input_str, symbol,):
    assert string_utils.delete_symbol("SkyPro", "Z") == "SkyPro"
    assert string_utils.delete_symbol("SkyPro", "1") == "SkyPro"
    assert string_utils.delete_symbol("SkyPro", "") == "SkyPro"
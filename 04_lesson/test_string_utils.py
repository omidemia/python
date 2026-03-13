import pytest
from string_utils import StringUtils

string_utils = StringUtils()


# ========== TESTS FOR None HANDLING ==========
@pytest.mark.negative
def test_capitalize_none():
    """Проверка capitalize с None"""
    with pytest.raises(AttributeError):
        string_utils.capitalize(None)


@pytest.mark.negative
def test_trim_none():
    """Проверка trim с None"""
    with pytest.raises(AttributeError):
        string_utils.trim(None)


@pytest.mark.negative
def test_to_list_none():
    """Проверка to_list с None"""
    with pytest.raises(AttributeError):
        string_utils.to_list(None, ",")


@pytest.mark.negative
def test_contains_none():
    """Проверка contains с None"""
    with pytest.raises(AttributeError):
        string_utils.contains(None, "a")


@pytest.mark.negative
def test_delete_symbol_none():
    """Проверка delete_symbol с None"""
    with pytest.raises(AttributeError):
        string_utils.delete_symbol(None, "a")


@pytest.mark.negative
def test_starts_with_none():
    """Проверка starts_with с None"""
    with pytest.raises(AttributeError):
        string_utils.starts_with(None, "a")


@pytest.mark.negative
def test_end_with_none():
    """Проверка end_with с None"""
    with pytest.raises(AttributeError):
        string_utils.end_with(None, "a")


@pytest.mark.negative
def test_is_empty_none():
    """Проверка is_empty с None"""
    with pytest.raises(AttributeError):
        string_utils.is_empty(None)


@pytest.mark.negative
def test_list_to_string_none():
    """Проверка list_to_string с None"""
    with pytest.raises(AttributeError):
        string_utils.list_to_string(None, ",")


# ========== TESTS FOR capitalize() ==========
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("123abc", "123abc"),
    ("04 апреля 2023", "04 апреля 2023"),
    ("тест", "Тест"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("   ", "   "),
    (" ", " "),
    ("123", "123"),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# ========== TESTS FOR trim() ==========
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("  hello world", "hello world"),
    ("    python", "python"),
    ("   04 апреля 2023", "04 апреля 2023"),
    ("  тест", "тест"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    (" ", ""),
    ("    ", ""),
    ("skypro   ", "skypro   "),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


# ========== TESTS FOR to_list() ==========
@pytest.mark.positive
@pytest.mark.parametrize("input_str, delimeter, expected", [
    ("a,b,c,d", ",", ["a", "b", "c", "d"]),
    ("1:2:3", ":", ["1", "2", "3"]),
    ("раз два три", " ", ["раз", "два", "три"]),
    ("тест", ",", ["тест"]),
    ("", ",", []),
    ("1,2,3", ",", ["1", "2", "3"]),
])
def test_to_list_positive(input_str, delimeter, expected):
    assert string_utils.to_list(input_str, delimeter) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, delimeter, expected", [
    ("", ":", []),
    ("   ", ",", ["   "]),
])
def test_to_list_negative(input_str, delimeter, expected):
    assert string_utils.to_list(input_str, delimeter) == expected


# ========== TESTS FOR contains() ==========
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "y", True),
    ("SkyPro", "o", True),
    ("hello world", "o", True),
    ("12345", "3", True),
    ("тест", "е", True),
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "U", False),
    ("", "a", False),
    ("hello", "", False),
    ("   ", "a", False),
    ("SkyPro", "sky", False),
])
def test_contains_negative(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


# ========== TESTS FOR delete_symbol() ==========
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("hello world", "o", "hell wrld"),
    ("aaaaa", "a", ""),
    ("тест", "е", "тст"),
    ("12345", "3", "1245"),
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("", "a", ""),
    ("SkyPro", "z", "SkyPro"),
    ("   ", " ", "   "),
    ("test", "", "test"),
])
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


# ========== TESTS FOR starts_with() ==========
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "Sky", True),
    ("hello world", "h", True),
    ("12345", "1", True),
    ("тест", "т", True),
])
def test_starts_with_positive(string, symbol, expected):
    assert string_utils.starts_with(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "P", False),
    ("SkyPro", "sky", False),
    ("", "a", False),
    ("hello", "", False),
    ("   ", "a", False),
])
def test_starts_with_negative(string, symbol, expected):
    assert string_utils.starts_with(string, symbol) == expected


# ========== TESTS FOR end_with() ==========
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "o", True),
    ("SkyPro", "Pro", True),
    ("hello world", "d", True),
    ("12345", "5", True),
    ("тест", "т", True),
])
def test_end_with_positive(string, symbol, expected):
    assert string_utils.end_with(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", False),
    ("SkyPro", "SKY", False),
    ("", "a", False),
    ("hello", "", False),
    ("   ", "a", False),
])
def test_end_with_negative(string, symbol, expected):
    assert string_utils.end_with(string, symbol) == expected


# ========== TESTS FOR is_empty() ==========
@pytest.mark.positive
@pytest.mark.parametrize("string, expected", [
    ("", True),
    (" ", True),
    ("    ", True),
])
def test_is_empty_positive(string, expected):
    assert string_utils.is_empty(string) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, expected", [
    ("SkyPro", False),
    ("hello world", False),
    ("123", False),
    ("тест", False),
    ("04 апреля 2023", False),
    ("  a  ", False),
])
def test_is_empty_negative(string, expected):
    assert string_utils.is_empty(string) == expected


# ========== TESTS FOR list_to_string() ==========
@pytest.mark.positive
@pytest.mark.parametrize("lst, joiner, expected", [
    (["a", "b", "c"], ", ", "a, b, c"),
    (["Sky", "Pro"], "-", "Sky-Pro"),
    (["1", "2", "3"], ":", "1:2:3"),
    (["раз", "два", "три"], " | ", "раз | два | три"),
    ([1, 2, 3], ", ", "1, 2, 3"),
    (["тест"], ", ", "тест"),
])
def test_list_to_string_positive(lst, joiner, expected):
    assert string_utils.list_to_string(lst, joiner) == expected


@pytest.mark.negative
@pytest.mark.parametrize("lst, joiner, expected", [
    ([], ", ", ""),
    ([], "-", ""),
    ([""], ", ", ""),
])
def test_list_to_string_negative(lst, joiner, expected):
    assert string_utils.list_to_string(lst, joiner) == expected


# ========== INTEGRATION TEST ==========
def test_all_methods_integration():
    """Интеграционный тест: использование нескольких методов вместе"""
    text = "   hello,world,test   "
    
    trimmed = string_utils.trim(text)
    listed = string_utils.to_list(trimmed, ",")
    joined = string_utils.list_to_string(listed, " | ")
    capitalized = string_utils.capitalize(joined)
    
    assert trimmed == "hello,world,test   "
    assert listed == ["hello", "world", "test   "]
    assert joined == "hello | world | test   "
    assert capitalized == "Hello | world | test"
    
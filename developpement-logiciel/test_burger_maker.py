# test_burger_maker.py
import pytest
from unittest.mock import patch, mock_open
from burger_maker import (
    get_order_timestamp,
    GetBun,
    get_bun_v2,
    calculate_burger_price,
    getMeat,
    GET_SAUCE,
    get_cheese123,
    AssembleBurger,
    SaveBurger,
    MAIN,
    INGREDIENT_PRICES
)

def test_get_order_timestamp():
    """Test that get_order_timestamp returns a string."""
    timestamp = get_order_timestamp()
    assert isinstance(timestamp, str)

@patch('builtins.input', return_value='sesame')
def test_get_bun(mock_input):
    """Test that GetBun returns the correct bun type."""
    bun = GetBun()
    assert bun == 'sesame'

@patch('builtins.input', return_value='sesame')
def test_get_bun_v2(mock_input):
    """Test that get_bun_v2 returns the correct bun type."""
    bun = get_bun_v2()
    assert bun == 'sesame'

def test_calculate_burger_price():
    """Test that calculate_burger_price returns the correct price."""
    price = calculate_burger_price(['bun', 'beef', 'cheese'])
    expected_price = (INGREDIENT_PRICES['bun'] + INGREDIENT_PRICES['beef'] + INGREDIENT_PRICES['cheese']) * 1.21
    assert price == expected_price

@patch('builtins.input', return_value='beef')
def test_get_meat(mock_input):
    """Test that getMeat returns the correct meat type."""
    meat = getMeat()
    assert meat == 'beef'

def test_get_sauce():
    """Test that GET_SAUCE returns the correct sauce combination."""
    sauce = GET_SAUCE()
    assert sauce == 'ketchup and mustard'

@patch('builtins.input', return_value='cheddar')
def test_get_cheese(mock_input):
    """Test that get_cheese123 returns the correct cheese type."""
    cheese = get_cheese123()
    assert cheese == 'cheddar'

@patch('builtins.input', side_effect=['sesame', 'beef', 'cheddar'])
def test_assemble_burger(mock_input):
    """Test that AssembleBurger returns the correct burger description."""
    burger = AssembleBurger()
    assert 'sesame bun + beef + ketchup and mustard + cheddar cheese' in burger

@patch('builtins.open', new_callable=mock_open)
def test_save_burger(mock_open):
    """Test that SaveBurger correctly writes to a file."""
    burger = 'sesame bun + beef + ketchup and mustard + cheddar cheese'
    SaveBurger(burger)
    mock_open.assert_called_with('/tmp/burger.txt', 'w')

@patch('builtins.input', side_effect=['sesame', 'beef', 'cheddar'])
@patch('builtins.open', new_callable=mock_open)
def test_main(mock_open, mock_input):
    """Test that MAIN orchestrates the burger creation process correctly."""
    MAIN()
    mock_open.assert_called_with('/tmp/burger.txt', 'w')


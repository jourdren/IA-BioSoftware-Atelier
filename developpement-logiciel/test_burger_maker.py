# test_burger_maker.py
import pytest
from unittest.mock import patch, mock_open
from burger import BurgerMaker, INGREDIENT_PRICES

def test_get_order_timestamp():
    """Test that get_order_timestamp returns a string."""
    burger_maker = BurgerMaker()
    timestamp = burger_maker.get_order_timestamp()
    assert isinstance(timestamp, str)

@patch('builtins.input', return_value='sesame')
def test_get_bun(mock_input):
    """Test that get_bun returns the correct bun type."""
    burger_maker = BurgerMaker()
    bun = burger_maker.get_bun()
    assert bun == 'sesame'

def test_calculate_burger_price():
    """Test that calculate_burger_price returns the correct price."""
    burger_maker = BurgerMaker()
    price = burger_maker.calculate_burger_price(['bun', 'beef', 'cheese'])
    expected_price = (INGREDIENT_PRICES['bun'] + INGREDIENT_PRICES['beef'] + INGREDIENT_PRICES['cheese']) * 1.21
    assert price == expected_price

@patch('builtins.input', return_value='beef')
def test_get_meat(mock_input):
    """Test that get_meat returns the correct meat type."""
    burger_maker = BurgerMaker()
    meat = burger_maker.get_meat()
    assert meat == 'beef'

def test_get_sauce():
    """Test that get_sauce returns the correct sauce combination."""
    burger_maker = BurgerMaker()
    sauce = burger_maker.get_sauce()
    assert sauce == 'ketchup and mustard'

@patch('builtins.input', return_value='cheddar')
def test_get_cheese(mock_input):
    """Test that get_cheese returns the correct cheese type."""
    burger_maker = BurgerMaker()
    cheese = burger_maker.get_cheese()
    assert cheese == 'cheddar'

@patch('builtins.input', side_effect=['sesame', 'beef', 'cheddar'])
def test_assemble_burger(mock_input):
    """Test that assemble_burger returns the correct burger description."""
    burger_maker = BurgerMaker()
    burger = burger_maker.assemble_burger()
    assert 'sesame bun with beef, ketchup and mustard, and cheddar cheese' in burger

@patch('builtins.open', new_callable=mock_open)
def test_save_burger(mock_open):
    """Test that save_burger correctly writes to a file."""
    burger_maker = BurgerMaker()
    burger = 'sesame bun with beef, ketchup and mustard, and cheddar cheese'
    burger_maker.save_burger(burger)
    mock_open.assert_called_with('/tmp/burger.txt', 'w')

@patch('builtins.input', side_effect=['sesame', 'beef', 'cheddar'])
@patch('builtins.open', new_callable=mock_open)
def test_main(mock_open, mock_input):
    """Test that main orchestrates the burger creation process correctly."""
    main()
    mock_open.assert_called_with('/tmp/burger.txt', 'w')


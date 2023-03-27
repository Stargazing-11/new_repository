import pytest
from arthimetic import ArithmeticOperations

class TestArithmeticOperations:
    @pytest.fixture
    def arithmetic(self):
        return ArithmeticOperations()

    def test_add(self, arithmetic):
        # arrange
        x, y = 1.0, 2.0
        expected_output = 3.0

        # act
        actual_output = arithmetic.add(x, y)

        # assert
        assert expected_output == actual_output

    def test_subtract(self, arithmetic):
        # arrange
        x, y = 3.0, 2.0
        expected_output = 1.0

        # act
        actual_output = arithmetic.subtract(x, y)

        # assert
        assert expected_output == actual_output

    def test_multiply(self, arithmetic):
        # arrange
        x, y = 2.0, 3.0
        expected_output = 6.0

        # act
        actual_output = arithmetic.multiply(x, y)

        # assert
        assert expected_output == actual_output

    def test_divide(self, arithmetic):
        # arrange
        x, y = 6.0, 2.0
        expected_output = 3.0

        # act
        actual_output = arithmetic.divide(x, y)

        # assert
        assert expected_output == actual_output

        # assert zero division error
        with pytest.raises(ZeroDivisionError):
            arithmetic.divide(2, 0)

    def test_add_with_invalid_input(self, arithmetic):
        # arrange
        x, y = "1", 2
        expected_error = TypeError

        # assert
        with pytest.raises(expected_error):
            arithmetic.add(x, y)

    def test_subtract_with_invalid_input(self, arithmetic):
        # arrange
        x, y = "1", 2
        expected_error = TypeError

        # assert
        with pytest.raises(expected_error):
            arithmetic.subtract(x, y)

    def test_multiply_with_invalid_input(self, arithmetic):
        # arrange
        x, y = "1", 2
        expected_error = TypeError

        # assert
        with pytest.raises(expected_error):
            arithmetic.multiply(x, y)

    def test_divide_with_invalid_input(self, arithmetic):
        # arrange
        x, y = "1", 2
        expected_error = TypeError

        # assert
        with pytest.raises(expected_error):
            arithmetic.divide(x, y)

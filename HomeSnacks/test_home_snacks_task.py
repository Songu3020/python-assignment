from unittest import TestCase
class TestLength(unittest):
    def test_generate_numbers(self):

        result = generate_numbers()

        assert isinstance(result, list)

        assert len(result) == 10
        
        for num in result:

            assert 1 <= num <= 50


#!/usr/bin/env python3
""" Module for test_util"""
import unittest
from typing import Mapping, Sequence, Any, Dict
from parameterized import parameterized
from utils import access_nested_map
from unittest.mock import patch, Mock
from utils import get_json
from utils import memoize


class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence, expected_result: Any) -> None:
        """ test for nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), "Key 'a' not found in nested map"),
        ({"a": 1}, ("a", "b"), "Key 'b' not found in nested map")
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping, path: Sequence, expected_error_msg: str) -> None:
        """ test for nested_map exception"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), expected_error_msg)


class TestGetJson(unittest.TestCase):

    @patch('utils.requests.get')
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, mock_get: Mock, test_url: str, test_payload: Dict[str, Any]) -> None:
        # Create a mock response object
        mock_response = Mock()
        # Set the return value of the json() method of the mock response
        mock_response.json.return_value = test_payload
        # Set the return value of the mock_get() method
        mock_get.return_value = mock_response

        # Call the get_json function with the test_url
        result = get_json(test_url)

        # Assert that the mocked get method was called exact
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):

    class TestClass:
        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()

    def test_memoize(self):
        # Create an instance of TestClass
        test_instance = self.TestClass()

        # Patch the a_method method of TestClass
        with patch.object(test_instance, 'a_method') as mock_a_method:
            # Call the a_property method twice
            result1 = test_instance.a_property()
            result2 = test_instance.a_property()

            # Assert that a_method was only called once
            mock_a_method.assert_called_once()

            # Assert that the results are correct
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)


if __name__ == "__main__":
    unittest.main()

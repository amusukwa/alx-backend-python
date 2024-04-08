#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient
from typing import List, Dict


class TestGithubOrgClient(unittest.TestCase):

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, mock_get_json: Dict) -> None:
        github_client: GithubOrgClient = GithubOrgClient(org_name)

        # Assert that get_json is called once with the correct URL
        expected_url: str = f"https://api.github.com/orgs/{org_name}"
        github_client.org()

        mock_get_json.assert_called_once_with(expected_url)

    def test_public_repos_url(self):
        # Define the known payload
        payload = {"repos_url": "http://example.com/repos"}
        
        # Mock the org property of GithubOrgClient
        with patch.object(GithubOrgClient, 'org', new_callable=PropertyMock) as mock_org:
            # Set the return value of the mocked org property
            mock_org.return_value = payload
            
            # Instantiate GithubOrgClient
            client = GithubOrgClient("test_org")

            # Assert that the result of _public_repos_url is the expected one
            self.assertEqual(client._public_repos_url, "http://example.com/repos")        


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3
""" Module for test_client """
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient
from typing import List, Dict


class TestGithubOrgClient(unittest.TestCase):
    """ Class GithubOrgClient with tests for client.py """

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, mock_get_json: Dict) -> None:
        """ Function for testing GithubOrgClient.org """
        github_client: GithubOrgClient = GithubOrgClient(org_name)

        # Assert that get_json is called once with the correct URL
        expected_url: str = f"https://api.github.com/orgs/{org_name}"
        github_client.org()

        mock_get_json.assert_called_once_with(expected_url)

    def test_public_repos_url(self):
        """ Test for GithubOrgClient._public_repos_url """
        # Define the known payload
        payload = {"repos_url": "http://example.com/repos"}

        # Mock the org property of GithubOrgClient
        with patch.object(GithubOrgClient, 'org', new_callable=PropertyMock) as mock_org:
            # Set the return value of the mocked org property
            mock_org.return_value = payload

            # Instantiate GithubOrgClient
            client = GithubOrgClient("test_org")

            # Assert that the result of _public_repos_url is the expected
            self.assertEqual(client._public_repos_url, "http://example.com/repos")

    @patch('client.get_json')
    @patch.object(GithubOrgClient, '_public_repos_url', new_callable=PropertyMock)
    def test_public_repos(self, mock_repos_url, mock_get_json):
        """ Test for GithubOrgClient.public_repos """
        # Define the known payload
        repos_payload = [{"name": "repo1"}, {"name": "repo2"}]

        # Set the return value of the mocked _public_repos_url
        mock_repos_url.return_value = "http://example.com/repos"

        # Set the return value of the mocked get_json
        mock_get_json.return_value = repos_payload

        # Instantiate GithubOrgClient
        client = GithubOrgClient("test_org")

        # Call the public_repos method
        repos = client.public_repos()

        # Assert that get_json and _public_repos_url were called once
        mock_get_json.assert_called_once()
        mock_repos_url.assert_called_once()

        # Assert that the list of repos is what we expect from the chosen payload
        self.assertEqual(repos, ["repo1", "repo2"])

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """ Test for GithubOrgClient.has_license """
        # Instantiate GithubOrgClient
        client = GithubOrgClient("test_org")

        # Call the has_license method with the provided inputs
        result = client.has_license(repo, license_key)

        # Assert that the result matches the expected result
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()


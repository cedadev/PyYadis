#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `yadis_server` package."""

__author__ = """Philip Kershaw"""
__contact__ = 'philip.kershaw@stfc.ac.uk'
__copyright__ = "Copyright 2018 United Kingdom Research and Innovation"
__license__ = "BSD - see LICENSE file in top-level package directory"



import unittest
from click.testing import CliRunner

from yadis_server import yadis_server
from yadis_server import cli


class Testyadis_server(unittest.TestCase):
    """Tests for `yadis_server` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'yadis_server.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
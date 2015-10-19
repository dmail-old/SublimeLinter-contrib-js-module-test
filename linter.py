#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Damien
# Copyright (c) 2015 Damien
#
# License: MIT
#

"""This module exports the JsModuleTest plugin class."""

import json
from SublimeLinter.lint import NodeLinter, util

class JsModuleTest(NodeLinter):

    """Provides an interface to js-module-test."""

    syntax = ('javascript')
    executable = 'system-test'
    cmd = 'system-test'
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 0.1.0'
    regex = r'^[\s\S]*$'
    multiline = True
    line_col_base = (1, 1)
    tempfile_suffix = '-'
    error_stream = util.STREAM_BOTH
    # http://www.sublimelinter.com/en/latest/linter_attributes.html#selectors
    # could use selectors on jshint to auto run this linter when it's a test file
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = r'\s*/[/*]'

    #def cmd(self):
    #     return self.executable

    def split_match(self, match):
        self.word_re = None

        #with open('data.json', encoding='utf-8') as data_file:
        #data = json.loads(data_file.read())
        # I can just read the console output and decide if there is an error or not
        # the regex should be pretty easy to perform considering I own the output behaviour

        if match:
            # match, line, col, error, warning, message, near
            return match, 0, 0, True, False, "macthed", None

        return match, 0, 0, True, False, "unmatched", None



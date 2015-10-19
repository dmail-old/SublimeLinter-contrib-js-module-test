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

from SublimeLinter.lint import NodeLinter, util


class JsModuleTest(NodeLinter):

    """Provides an interface to js-module-test."""

    syntax = ('javascript')
    #executable = 'system-test'
    cmd = 'system-test'
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 0.1.0'
    regex = r''
    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = None
    error_stream = util.STREAM_BOTH
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

        if match:
            # match, line, col, error, warning, message, near
            return match, 0, 0, True, False, "macthed", None

        return match, 0, 0, True, False, "unmatched", None



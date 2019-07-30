import sys
import simplejson

from .base import BaseResolver
# from pytempl.templ.output import RED, YELLOW, pcprint, wcolour
# from pytempl.templ.utils import file_exists


class JSONLint(BaseResolver):

    EXIT_INVALID_FILE = 1
    EXIT_INVALID_JSON = 2

    _files = []
    """Files to lint"""

    @staticmethod
    def arguments() -> list:
        return [
            (['--file', '-f'],
             {'default': [],
              'dest': 'files',
              'help': 'Files to lint',
              'nargs': '+',
              'type': str})
        ]

    def run(self):
        self.determine_files().lint()

    def determine_files(self):
        """
        Determine JSON file to lint
        :return:
        """
        self._files = self._args.get('files', [])
        return self

    def lint(self):
        """
        Perform linting action
        :return:
        """
        print('linting')
        # if not self._files:
        #     return
        # for file in self._files:
        #     if not file_exists(file):
        #         pcprint("File issue: {} does not exist.".format(wcolour(file, colour=YELLOW, ecolour=RED)), colour=RED)
        #         sys.exit(self.EXIT_INVALID_FILE)
        #     with open(file) as json_file:
        #         try:
        #             simplejson.load(json_file)
        #         except simplejson.JSONDecodeError as ejd:
        #             if len(self.app.pargs.files) > 1:
        #                 pcprint(file, colour=YELLOW)
        #             pcprint("JSON object issue: {}".format(wcolour(ejd.msg, colour=YELLOW, ecolour=RED)), colour=RED)
        #             sys.exit(self.EXIT_INVALID_JSON)
        #         except Exception as e: #pylint: disable=W0703
        #             if len(self.app.pargs.files) > 1:
        #                 pcprint(file, colour=YELLOW)
        #             pcprint("JSON object issue: {}".format(wcolour(e, colour=YELLOW, ecolour=RED)), colour=RED)
        #             sys.exit(self.EXIT_INVALID_JSON)
        return self
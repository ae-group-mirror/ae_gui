# THIS FILE IS EXCLUSIVELY MAINTAINED by the project aedev.project_tpls v0.3.59
""" setup of ae namespace package portion gui: helper functions and base application classes for GUI applications. """
# noinspection PyUnresolvedReferences
import sys
print(f"SetUp {__name__=} {sys.executable=} {sys.argv=} {sys.path=}")

# noinspection PyUnresolvedReferences
import setuptools

setup_kwargs = {
    'author': 'AndiEcker',
    'author_email': 'aecker2@gmail.com',
    'classifiers': [       'Development Status :: 3 - Alpha', 'Natural Language :: English', 'Operating System :: OS Independent',
        'Programming Language :: Python', 'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9', 'Topic :: Software Development :: Libraries :: Python Modules',
        'Typing :: Typed'],
    'description': 'ae namespace package portion gui: helper functions and base application classes for GUI applications',
    'extras_require': {       'dev': [       'aedev_project_tpls', 'ae_ae', 'anybadge', 'coverage-badge', 'aedev_project_manager', 'flake8',
                       'mypy', 'pylint', 'pytest', 'pytest-cov', 'pytest-django', 'typing', 'types-setuptools'],
        'docs': [],
        'tests': [       'anybadge', 'coverage-badge', 'aedev_project_manager', 'flake8', 'mypy', 'pylint', 'pytest',
                         'pytest-cov', 'pytest-django', 'typing', 'types-setuptools']},
    'install_requires': ['ae_base', 'ae_files', 'ae_paths', 'ae_updater', 'ae_dynamicod', 'ae_i18n', 'ae_core', 'ae_console'],
    'keywords': ['configuration', 'development', 'environment', 'productivity'],
    'license': 'GPL-3.0-or-later',
    'long_description': ('<!-- THIS FILE IS EXCLUSIVELY MAINTAINED by the project ae.ae v0.3.101 -->\n'
 '<!-- THIS FILE IS EXCLUSIVELY MAINTAINED by the project aedev.namespace_root_tpls v0.3.22 -->\n'
 '# gui 0.3.115\n'
 '\n'
 '[![GitLab develop](https://img.shields.io/gitlab/pipeline/ae-group/ae_gui/develop?logo=python)](\n'
 '    https://gitlab.com/ae-group/ae_gui)\n'
 '[![LatestPyPIrelease](\n'
 '    https://img.shields.io/gitlab/pipeline/ae-group/ae_gui/release0.3.115?logo=python)](\n'
 '    https://gitlab.com/ae-group/ae_gui/-/tree/release0.3.115)\n'
 '[![PyPIVersions](https://img.shields.io/pypi/v/ae_gui)](\n'
 '    https://pypi.org/project/ae-gui/#history)\n'
 '\n'
 '>ae namespace package portion gui: helper functions and base application classes for GUI applications.\n'
 '\n'
 '[![Coverage](https://ae-group.gitlab.io/ae_gui/coverage.svg)](\n'
 '    https://ae-group.gitlab.io/ae_gui/coverage/index.html)\n'
 '[![MyPyPrecision](https://ae-group.gitlab.io/ae_gui/mypy.svg)](\n'
 '    https://ae-group.gitlab.io/ae_gui/lineprecision.txt)\n'
 '[![PyLintScore](https://ae-group.gitlab.io/ae_gui/pylint.svg)](\n'
 '    https://ae-group.gitlab.io/ae_gui/pylint.log)\n'
 '\n'
 '[![PyPIImplementation](https://img.shields.io/pypi/implementation/ae_gui)](\n'
 '    https://gitlab.com/ae-group/ae_gui/)\n'
 '[![PyPIPyVersions](https://img.shields.io/pypi/pyversions/ae_gui)](\n'
 '    https://gitlab.com/ae-group/ae_gui/)\n'
 '[![PyPIWheel](https://img.shields.io/pypi/wheel/ae_gui)](\n'
 '    https://gitlab.com/ae-group/ae_gui/)\n'
 '[![PyPIFormat](https://img.shields.io/pypi/format/ae_gui)](\n'
 '    https://pypi.org/project/ae-gui/)\n'
 '[![PyPILicense](https://img.shields.io/pypi/l/ae_gui)](\n'
 '    https://gitlab.com/ae-group/ae_gui/-/blob/develop/LICENSE.md)\n'
 '[![PyPIStatus](https://img.shields.io/pypi/status/ae_gui)](\n'
 '    https://libraries.io/pypi/ae-gui)\n'
 '[![PyPIDownloads](https://img.shields.io/pypi/dm/ae_gui)](\n'
 '    https://pypi.org/project/ae-gui/#files)\n'
 '\n'
 '\n'
 '## installation\n'
 '\n'
 '\n'
 'execute the following command to install the\n'
 'ae.gui package\n'
 'in the currently active virtual environment:\n'
 ' \n'
 '```shell script\n'
 'pip install ae-gui\n'
 '```\n'
 '\n'
 'if you want to contribute to this portion then first fork\n'
 '[the ae_gui repository at GitLab](\n'
 'https://gitlab.com/ae-group/ae_gui "ae.gui code repository").\n'
 'after that pull it to your machine and finally execute the\n'
 'following command in the root folder of this repository\n'
 '(ae_gui):\n'
 '\n'
 '```shell script\n'
 'pip install -e .[dev]\n'
 '```\n'
 '\n'
 'the last command will install this package portion, along with the tools you need\n'
 'to develop and run tests or to extend the portion documentation. to contribute only to the unit tests or to the\n'
 'documentation of this portion, replace the setup extras key `dev` in the above command with `tests` or `docs`\n'
 'respectively.\n'
 '\n'
 'more detailed explanations on how to contribute to this project\n'
 '[are available here](\n'
 'https://gitlab.com/ae-group/ae_gui/-/blob/develop/CONTRIBUTING.rst)\n'
 '\n'
 '\n'
 '## namespace portion documentation\n'
 '\n'
 'information on the features and usage of this portion are available at\n'
 '[ReadTheDocs](\n'
 'https://ae.readthedocs.io/en/latest/_autosummary/ae.gui.html\n'
 '"ae_gui documentation").\n'),
    'long_description_content_type': 'text/markdown',
    'name': 'ae_gui',
    'package_data': {       '': [       'img/flag_en.png', 'img/filter_off.png', 'img/bubble_arrow.png', 'img/help_icon.png',
                    'img/help_circled.png', 'img/edit_item.png', 'img/leave_item.png', 'img/cut_node.png',
                    'img/list_view.png', 'img/flag_es.png', 'img/add_item.png', 'img/tap_pointer.png',
                    'img/delete_item.png', 'img/open_node_info.png', 'img/export_node.png', 'img/filter_on.png',
                    'img/copy_node.png', 'img/enter_item.png', 'img/app_tour.png', 'img/icon_view.png',
                    'img/save_item.png', 'img/close_popup.png', 'img/import_node.png', 'img/drag_item.png',
                    'img/flag_de.png', 'img/paste_node.png', 'img/send_item.png', 'img/light_1/filter_off.png',
                    'img/light_1/bubble_arrow.png', 'img/light_1/help_icon.png', 'img/light_1/help_circled.png',
                    'img/light_1/edit_item.png', 'img/light_1/leave_item.png', 'img/light_1/cut_node.png',
                    'img/light_1/list_view.png', 'img/light_1/add_item.png', 'img/light_1/tap_pointer.png',
                    'img/light_1/delete_item.png', 'img/light_1/open_node_info.png', 'img/light_1/export_node.png',
                    'img/light_1/filter_on.png', 'img/light_1/copy_node.png', 'img/light_1/enter_item.png',
                    'img/light_1/app_tour.png', 'img/light_1/icon_view.png', 'img/light_1/save_item.png',
                    'img/light_1/close_popup.png', 'img/light_1/import_node.png', 'img/light_1/drag_item.png',
                    'img/light_1/paste_node.png', 'img/light_1/send_item.png', 'loc/es/Msg.txt', 'loc/de/Msg.txt',
                    'loc/en/Msg.txt', 'snd/added.wav', 'snd/edited.wav', 'snd/filter_on.wav', 'snd/leave_item.wav',
                    'snd/enter_item.wav', 'snd/deleted.wav', 'snd/debug_save.wav', 'snd/touched.wav',
                    'snd/filter_off.wav', 'snd/debug_draw.wav', 'snd/error.wav']},
    'packages': [       'ae.gui', 'ae.gui.loc', 'ae.gui.img', 'ae.gui.snd', 'ae.gui.loc.es', 'ae.gui.loc.de', 'ae.gui.loc.en',
        'ae.gui.img.light_1'],
    'project_urls': {       'Bug Tracker': 'https://gitlab.com/ae-group/ae_gui/-/issues',
        'Documentation': 'https://ae.readthedocs.io/en/latest/_autosummary/ae.gui.html',
        'Repository': 'https://gitlab.com/ae-group/ae_gui',
        'Source': 'https://ae.readthedocs.io/en/latest/_modules/ae/gui.html'},
    'python_requires': '>=3.9',
    'url': 'https://gitlab.com/ae-group/ae_gui',
    'version': '0.3.115',
    'zip_safe': False,
}

if __name__ == "__main__":
    setuptools.setup(**setup_kwargs)
    pass

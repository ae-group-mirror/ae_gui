""" test constants """
import os
from unittest.mock import patch

import pytest

from ae.base import os_path_join, os_path_relpath, write_file
from ae.paths import PATH_PLACEHOLDERS

from ae.gui.utils import PORTIONS_IMAGES, PORTIONS_SOUNDS


@pytest.fixture
def tst_tmp_path(tmp_path) -> str:
    return str(tmp_path)


PORTION_IMG_COUNT = len(PORTIONS_IMAGES)
TST_IMG_COUNT = 1
tst_image_name = 'tst_img_file'


@pytest.fixture
def tst_ado_image_files(tst_tmp_path):
    """ provide test files with properties. """
    old_ado_path = PATH_PLACEHOLDERS['ado']
    file_root = os_path_join(tst_tmp_path, 'img')

    file_ext = '.xy'
    file_without_properties = os_path_join(file_root, tst_image_name + file_ext)
    file_content = "test file content"

    write_file(file_without_properties, file_content, make_dirs=True)

    file_properties = {'light': 0, 'height': 1.5}
    properties = []
    fn = file_root
    for name, value in file_properties.items():
        fn = os_path_join(fn, name + '_' + str(value))
        os.mkdir(fn)
        properties.append((name, value))
    file_with_asc_properties = os_path_join(fn, tst_image_name + file_ext)
    write_file(file_with_asc_properties, file_content)

    fn = file_root
    for name, value in reversed(properties):
        if name == 'height':
            value *= 2.0
        fn = os_path_join(fn, name + '_' + str(value))
        os.mkdir(fn)
    file_with_desc_properties = os_path_join(fn, tst_image_name + file_ext)
    write_file(file_with_desc_properties, file_content)

    # patch ae.paths.app_docs_path to set PATH_PLACEHOLDERS['ado'] to tmpPath in ae.core.AppBase._init_path_placeholders
    with patch('ae.core.app_docs_path', return_value=tst_tmp_path):
        yield (os_path_relpath(file_without_properties, tst_tmp_path),
               os_path_relpath(file_with_asc_properties, tst_tmp_path),
               os_path_relpath(file_with_desc_properties, tst_tmp_path))

    PATH_PLACEHOLDERS['ado'] = old_ado_path


PORTION_SND_COUNT = len(PORTIONS_SOUNDS)
TST_SND_COUNT = 1
tst_sound_name = 'tst_snd_file'


@pytest.fixture
def tst_ado_sound_files(tst_tmp_path):
    """ provide a fake sound file without properties. """
    old_ado_path = PATH_PLACEHOLDERS['ado']
    file_root = os_path_join(tst_tmp_path, 'snd')

    file_ext = '.xy'
    file_without_properties = os_path_join(file_root, tst_sound_name + file_ext)
    file_content = "test file content"

    write_file(file_without_properties, file_content, make_dirs=True)

    with patch('ae.core.app_docs_path', return_value=tst_tmp_path):
        yield (os_path_relpath(file_without_properties, tst_tmp_path), )   # tuple of sound file name(s)

    PATH_PLACEHOLDERS['ado'] = old_ado_path

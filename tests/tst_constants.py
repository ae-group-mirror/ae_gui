""" test constants """
import os
import shutil

import pytest

from ae.base import TESTS_FOLDER, in_wd, write_file

from ae.gui.utils import PORTIONS_IMAGES, PORTIONS_SOUNDS


PORTION_IMG_COUNT = len(PORTIONS_IMAGES)
TST_IMG_COUNT = 1
image_file_name = 'tst_file'


@pytest.fixture
def image_files_to_test():
    """ provide test files with properties. """
    with in_wd(TESTS_FOLDER):
        file_root = 'img'
        file_ext = '.xy'
        file_without_properties = os.path.join(file_root, image_file_name + file_ext)
        file_content = "test file content"
        file_properties = {'light': 0, 'height': 1.5}

        os.mkdir(file_root)
        write_file(file_without_properties, file_content)

        properties = []
        fn = file_root
        for name, value in file_properties.items():
            fn = os.path.join(fn, name + '_' + str(value))
            os.mkdir(fn)
            properties.append((name, value))
        file_with_asc_properties = os.path.join(fn, image_file_name + file_ext)
        write_file(file_with_asc_properties, file_content)

        fn = file_root
        for name, value in reversed(properties):
            if name == 'height':
                value *= 2.0
            fn = os.path.join(fn, name + '_' + str(value))
            os.mkdir(fn)
        file_with_desc_properties = os.path.join(fn, image_file_name + file_ext)
        write_file(file_with_desc_properties, file_content)

        yield file_without_properties, file_with_asc_properties, file_with_desc_properties

        shutil.rmtree(file_root)


PORTION_SND_COUNT = len(PORTIONS_SOUNDS)
TST_SND_COUNT = 1
sound_file_name = 'snd_file'


@pytest.fixture
def sound_files_to_test():
    """ provide a fake sound file without properties. """
    with in_wd(TESTS_FOLDER):
        file_root = 'snd'
        file_ext = '.xy'
        file_without_properties = os.path.join(file_root, sound_file_name + file_ext)
        file_content = "test file content"

        os.mkdir(file_root)
        write_file(file_without_properties, file_content)

        yield file_without_properties,  # tuple of file name(s)

        shutil.rmtree(file_root)

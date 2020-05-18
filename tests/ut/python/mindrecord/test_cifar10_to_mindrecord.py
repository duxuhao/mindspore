# Copyright 2019 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""test cifar10 to mindrecord tool"""
import os
import pytest
from mindspore.mindrecord import Cifar10ToMR
from mindspore.mindrecord import FileReader
from mindspore.mindrecord import MRMOpenError, SUCCESS
from mindspore import log as logger

CIFAR10_DIR = "../data/mindrecord/testCifar10Data"
MINDRECORD_FILE = "./cifar10.mindrecord"


def test_cifar10_to_mindrecord_without_index_fields():
    """test transform cifar10 dataset to mindrecord without index fields."""
    cifar10_transformer = Cifar10ToMR(CIFAR10_DIR, MINDRECORD_FILE)
    cifar10_transformer.transform()
    assert os.path.exists(MINDRECORD_FILE)
    assert os.path.exists(MINDRECORD_FILE + "_test")
    read()
    os.remove("{}".format(MINDRECORD_FILE))
    os.remove("{}.db".format(MINDRECORD_FILE))

    os.remove("{}".format(MINDRECORD_FILE + "_test"))
    os.remove("{}.db".format(MINDRECORD_FILE + "_test"))


def test_cifar10_to_mindrecord():
    """test transform cifar10 dataset to mindrecord."""
    cifar10_transformer = Cifar10ToMR(CIFAR10_DIR, MINDRECORD_FILE)
    cifar10_transformer.transform(['label'])
    assert os.path.exists(MINDRECORD_FILE)
    assert os.path.exists(MINDRECORD_FILE + "_test")
    read()
    os.remove("{}".format(MINDRECORD_FILE))
    os.remove("{}.db".format(MINDRECORD_FILE))

    os.remove("{}".format(MINDRECORD_FILE + "_test"))
    os.remove("{}.db".format(MINDRECORD_FILE + "_test"))


def test_cifar10_to_mindrecord_with_return():
    """test transform cifar10 dataset to mindrecord."""
    cifar10_transformer = Cifar10ToMR(CIFAR10_DIR, MINDRECORD_FILE)
    ret = cifar10_transformer.transform(['label'])
    assert ret == SUCCESS, "commit failed"
    assert os.path.exists(MINDRECORD_FILE)
    assert os.path.exists(MINDRECORD_FILE + "_test")
    read()
    os.remove("{}".format(MINDRECORD_FILE))
    os.remove("{}.db".format(MINDRECORD_FILE))

    os.remove("{}".format(MINDRECORD_FILE + "_test"))
    os.remove("{}.db".format(MINDRECORD_FILE + "_test"))


def read():
    """test file reader"""
    count = 0
    reader = FileReader(MINDRECORD_FILE)
    for _, x in enumerate(reader.get_next()):
        assert len(x) == 3
        count = count + 1
        if count == 1:
            logger.info("data: {}".format(x))
    assert count == 16
    reader.close()

    count = 0
    reader = FileReader(MINDRECORD_FILE + "_test")
    for _, x in enumerate(reader.get_next()):
        assert len(x) == 3
        count = count + 1
        if count == 1:
            logger.info("data: {}".format(x))
    assert count == 4
    reader.close()


def test_cifar10_to_mindrecord_illegal_file_name():
    """
    test transform cifar10 dataset to mindrecord
    when file name contains illegal character.
    """
    filename = "./:no_ok"
    with pytest.raises(Exception, match="File name should not contains"):
        cifar10_transformer = Cifar10ToMR(CIFAR10_DIR, filename)
        cifar10_transformer.transform()


def test_cifar10_to_mindrecord_filename_start_with_space():
    """
    test transform cifar10 dataset to mindrecord
    when file name starts with space.
    """
    filename = "./ no_ok"
    with pytest.raises(Exception,
                       match="File name should not start/end with space"):
        cifar10_transformer = Cifar10ToMR(CIFAR10_DIR, filename)
        cifar10_transformer.transform()


def test_cifar10_to_mindrecord_filename_contain_space():
    """
    test transform cifar10 dataset to mindrecord
    when file name contains space.
    """
    filename = "./yes  ok"
    cifar10_transformer = Cifar10ToMR(CIFAR10_DIR, filename)
    cifar10_transformer.transform()
    assert os.path.exists(filename)
    assert os.path.exists(filename + "_test")
    os.remove("{}".format(filename))
    os.remove("{}.db".format(filename))

    os.remove("{}".format(filename + "_test"))
    os.remove("{}.db".format(filename + "_test"))


def test_cifar10_to_mindrecord_directory():
    """
    test transform cifar10 dataset to mindrecord
    when destination path is directory.
    """
    with pytest.raises(MRMOpenError,
                       match="MindRecord File could not open successfully"):
        cifar10_transformer = Cifar10ToMR(CIFAR10_DIR, CIFAR10_DIR)
        cifar10_transformer.transform()


def test_cifar10_to_mindrecord_filename_equals_cifar10():
    """
    test transform cifar10 dataset to mindrecord
    when destination path equals source path.
    """
    with pytest.raises(MRMOpenError,
                       match="MindRecord File could not open successfully"):
        cifar10_transformer = Cifar10ToMR(CIFAR10_DIR,
                                          CIFAR10_DIR + "/data_batch_0")
        cifar10_transformer.transform()

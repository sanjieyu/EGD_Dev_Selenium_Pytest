# Author:Yi Sun(Tim) 2023-9-23

import pytest
import allure
from unittest import TestCase


class BaseTest:

    @classmethod
    def setup_class(cls):
        class_name = cls.__name__
        if class_name.startswith('Test'):
            feature_name = class_name[4:].replace('_', ' ')
            allure.dynamic.feature(feature_name)

    def setup_method(self, method):
        """方法设置时自动设置story和title"""
        method_name = method.__name__
        if method_name.startswith('test_'):
            story_name = method_name[5:].replace('_', ' ')
            allure.dynamic.story(story_name)

            if method.__doc__:
                allure.dynamic.title(method.__doc__.strip())
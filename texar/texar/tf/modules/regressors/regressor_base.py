# Copyright 2019 The Texar Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Base class for Regressors.
"""

from texar.tf.module_base import ModuleBase

__all__ = [
    "RegressorBase"
]


class RegressorBase(ModuleBase):
    """Base class inherited by all regressor classes.
    """

    def __init__(self, hparams=None):
        ModuleBase.__init__(self, hparams)

    @staticmethod
    def default_hparams():
        """Returns a dictionary of hyperparameters with default values.
        """
        return {
            "name": "regressor"
        }

    def _build(self, inputs, *args, **kwargs):
        """Runs regressors on inputs.

        Args:
          inputs: Inputs to the regressor.
          *args: Other arguments.
          **kwargs: Keyword arguments.

        Returns:
          Regression output.
        """
        raise NotImplementedError

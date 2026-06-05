# Copyright 2025 DeepMind Technologies Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""MuJoCo Playground."""
from mujoco_playground._src import dm_control_suite
from mujoco_playground._src import locomotion
from mujoco_playground._src import manipulation
from mujoco_playground._src import registry
from mujoco_playground._src import wrapper
# pylint: disable=g-importing-member
from mujoco_playground._src.mjx_env import MjxEnv
from mujoco_playground._src.mjx_env import render_array
from mujoco_playground._src.mjx_env import State
from mujoco_playground._src.mjx_env import step

# pylint: enable=g-importing-member


def __getattr__(name):
  if name == "wrapper_torch":
    from mujoco_playground._src import wrapper_torch  # pylint: disable=g-import-not-at-top

    return wrapper_torch
  raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


__all__ = [
    "dm_control_suite",
    "locomotion",
    "manipulation",
    "MjxEnv",
    "registry",
    "render_array",
    "State",
    "step",
    "wrapper",
    "wrapper_torch",
]

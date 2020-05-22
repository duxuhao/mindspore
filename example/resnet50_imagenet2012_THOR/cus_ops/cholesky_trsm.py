# Copyright 2020 Huawei Technologies Co., Ltd
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
from mindspore.ops.op_info_register import op_info_register
"""CusCholeskyTrsm"""

@op_info_register("""{
    "op_name": "CusCholeskyTrsm",
    "imply_type": "TBE",
    "fusion_type": "OPAQUE",
    "async_flag": false,
    "binfile_name": "choleskytrsm.so",
    "compute_cost": 10,
    "kernel_name": "CusCholeskyTrsm",
    "partial_flag": true,
    "attr": [
 
    ],
    "inputs": [
        {
            "index": 0,
            "dtype": [
                "float32"
            ],
            "format": [
                "DefaultFormat"
            ],
            "name": "x1",
            "need_compile": false,
            "param_type": "required",
            "shape": "all"
        }
    ],
    "outputs": [
        {
            "index": 0,
            "dtype": [
                "float32"
            ],
            "format": [
                "DefaultFormat"
            ],
            "name": "y",
            "need_compile": false,
            "param_type": "required",
            "shape": "all"
        }
   ]
}""")
def CusCholeskyTrsm(input_x, output, kernel_name):
    """CusCholeskyTrsm"""
    return

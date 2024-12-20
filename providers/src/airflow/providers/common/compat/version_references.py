# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from __future__ import annotations

from packaging.version import Version

from airflow import __version__ as AIRFLOW_VERSION

AIRFLOW_V_3_0_PLUS = Version(Version(AIRFLOW_VERSION).base_version) >= Version("3.0.0")
AIRFLOW_V_2_10_PLUS = Version(Version(AIRFLOW_VERSION).base_version) >= Version("2.10.0")
AIRFLOW_V_2_9_PLUS = Version(Version(AIRFLOW_VERSION).base_version) >= Version("2.9.0")
AIRFLOW_V_2_8_PLUS = Version(Version(AIRFLOW_VERSION).base_version) >= Version("2.8.0")

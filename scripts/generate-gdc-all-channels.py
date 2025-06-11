###############################################################################
#
# Authors: Tom Kralidis <tomkralidis@gmail.com>
#
# Copyright (c) 2025 Tom Kralidis
#
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
#
###############################################################################

import requests

ALL_CHANNELS = []

GDCS = [
    'https://wis2-gdc.weather.gc.ca/collections/wis2-discovery-metadata',
    'https://wis2.dwd.de/gdc/collections/wis2-discovery-metadata',
    'https://gdc.wis.cma.cn/collections/wis2-discovery-metadata'
]

CHANNELS = (
    'cache/a/wis2',
    'origin/a/wis2'
)

PARAMS = {
    'f': 'json',
    'limit': 100000
}

for gdc in GDCS:
    url = f'{gdc}/items'
    response = requests.get(url, params=PARAMS).json()

    for feature in response['features']:
        for link in feature['links']:
            channel = link.get('channel', '')
            if channel.startswith(CHANNELS):
                channel = '/'.join(channel.split('/')[4:])
                ALL_CHANNELS.append(','.join([feature['id'], channel]))

for channel in sorted(set(ALL_CHANNELS)):
    print(channel)

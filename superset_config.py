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

# ---------------------------------------------------------
# Superset specific config
# ---------------------------------------------------------
import os
from datetime import timedelta

# Flask App Builder configuration
# Your App secret key will be used for securely signing the session cookie
# and encrypting sensitive information on the database
# Make sure you are changing this key for your deployment with a strong key.
# You can generate a strong key using `openssl rand -base64 42`.
SECRET_KEY = '1nL1FJMYHYNbOUGurxxzeuPgxrIISJVIGzViZVLGmE8wRlXw7EhTJMpF'

# Custom Security Manager
# Points to the custom security manager class defined in superset/security/manager.py
# CUSTOM_SECURITY_MANAGER = 'superset.security.manager.SupersetSecurityManager'

# Custom Security API
# Points to the custom security API class defined in superset/security/api.py
# Note: The actual class name is SecurityApiCustom, but it's aliased as SecurityApi
# AUTH_API = 'superset.security.api.SecurityApi'

# JWT Configuration
# Set the duration for access tokens
JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=24)
# Set the duration for refresh tokens (optional, but recommended)
JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)

# Other Superset configurations can go here...
# For example:
# ROW_LIMIT = 5000
# SUPERSET_WEBSERVER_PORT = 8088
# MAPBOX_API_KEY = 'YOUR_MAPBOX_API_KEY'
# ENABLE_PROXY_FIX = True
# SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://user:password@host:port/dbname'
# CACHE_CONFIG = { 'CACHE_TYPE': 'redis', ... }
# FEATURE_FLAGS = { 'EMBEDDED_SUPERSET': True }

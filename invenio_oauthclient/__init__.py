# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015-2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Advanced usage docs."""

from .ext import InvenioOAuthClient, InvenioOAuthClientREST
from .proxies import current_oauthclient

__version__ = "2.0.1"

__all__ = (
    "__version__",
    "current_oauthclient",
    "InvenioOAuthClient",
    "InvenioOAuthClientREST",
)

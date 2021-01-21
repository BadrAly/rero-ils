# -*- coding: utf-8 -*-
#
# RERO ILS
# Copyright (C) 2021 RERO
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Define relation between records and buckets."""

from __future__ import absolute_import

from invenio_db import db
from invenio_pidstore.models import RecordIdentifier
from invenio_records.models import RecordMetadataBase


class OperationLogIdentifier(RecordIdentifier):
    """Sequence generator for OperationLog identifiers."""

    __tablename__ = 'operation_log_id'
    __mapper_args__ = {'concrete': True}

    recid = db.Column(
        db.BigInteger().with_variant(db.Integer, 'sqlite'),
        primary_key=True, autoincrement=True,
    )


class OperationLogMetadata(db.Model, RecordMetadataBase):
    """Operation log record metadata."""

    __tablename__ = 'operation_log_metadata'


class OperationLogOperation:
    """Enum class to list all possible operations."""

    CREATE = 'create'
    UPDATE = 'update'

'''
Client.Processor.* tests.
'''
import pytest

from plaid.errors import InvalidRequestError

from tests.integration.util import (
    create_client,
    SANDBOX_INSTITUTION,
)


def test_processor_token():
    client = create_client()

    # get processor token
    response = client.Sandbox.processor_token.create(
        SANDBOX_INSTITUTION)
    assert response['processor_token'] is not None

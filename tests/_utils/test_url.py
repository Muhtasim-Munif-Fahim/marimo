# Copyright 2026 Marimo. All rights reserved.
from __future__ import annotations

import pytest

from marimo._utils.url import is_url


@pytest.mark.parametrize(
    "url",
    [
        "http://foobar.dk",
        "https://example.com/path/to/file.py",
        "ftp://foobar.dk",
        "http://10.0.0.1",
        "http://localhost",
        "http://localhost:8/macros.tex",
        "http://127.0.0.1:8/macros.tex",
        "http://127.0.0.1:80/macros.tex",
        "http://127.0.0.1:8000/macros.tex",
        "http://127.0.0.1:65535/macros.tex",
        "https://example.com:8/notebook.py?raw=true#cell",
    ],
)
def test_is_url_valid(url: str) -> None:
    assert is_url(url)


@pytest.mark.parametrize(
    "url",
    [
        "http://foobar.d",
        "example.com",
        "notebook.py",
        "http://127.0.0.1:/macros.tex",
        "http://127.0.0.1:123456/macros.tex",
        "http://127.0.0.1:port/macros.tex",
    ],
)
def test_is_url_invalid(url: str) -> None:
    assert not is_url(url)


def test_is_url_public() -> None:
    assert is_url("http://example.com:8", public=True)
    assert not is_url("http://10.0.0.1:8", public=True)

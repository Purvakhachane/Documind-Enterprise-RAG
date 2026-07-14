"""Minimal imghdr shim for environments missing the stdlib module.

Provides a lightweight `what()` implementation used by Streamlit to detect
image types. Only recognizes common formats (PNG, JPEG, GIF, BMP, TIFF).
"""
from __future__ import annotations

from typing import Optional, Union


def what(file: Union[str, bytes, bytearray], h: Optional[bytes] = None) -> Optional[str]:
    """Return a string describing the image type, or None if unknown.

    This mirrors the stdlib `imghdr.what` behaviour enough for Streamlit's
    needs.
    """
    data = None

    if h is not None:
        data = h[:32]
    else:
        if isinstance(file, (bytes, bytearray)):
            data = bytes(file)[:32]
        else:
            try:
                with open(file, "rb") as f:
                    data = f.read(32)
            except Exception:
                return None

    if not data:
        return None

    if data.startswith(b"\x89PNG\r\n\x1a\n"):
        return "png"
    if data[:3] == b"\xff\xd8\xff":
        return "jpeg"
    if data[:6] in (b"GIF87a", b"GIF89a"):
        return "gif"
    if data.startswith(b"BM"):
        return "bmp"
    if data[:4] in (b"II*\x00", b"MM\x00*"):
        return "tiff"

    return None

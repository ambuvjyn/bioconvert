import bz2
import gzip

import pytest

from bioconvert.bz22gz import BZ22GZ
from bioconvert import TempFile


@pytest.mark.parametrize("method", BZ22GZ.available_methods)
def test_conv(method):
    # generate a fake sequence
    content_ref = b"atgc" * 50
    # Compress it
    bz2_string = bz2.compress(content_ref, 9)
    # Generate two tmp file
    bz2_file = TempFile(suffix="bz2")
    gz_file = TempFile(suffix="gz")
    # Write the bz2 file with compressed fake sequence
    with open(bz2_file.name, "wb") as bz2_to_write:
        bz2_to_write.write(bz2_string)

    # Convert bz2 to gz
    converter = BZ22GZ(bz2_file.name, gz_file.name)
    converter(method=method)

    # gunzip result file
    with gzip.open(gz_file.name, "rb") as gz_to_read:
        content = gz_to_read.read()

    # check conversion
    assert content == content_ref

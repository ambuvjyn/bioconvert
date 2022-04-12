from bioconvert.io.fasta import Fasta

import pytest

from . import test_dir

ids = [
    "SRR2749800.1",
    "SRR2749800.2",
    "SRR2749800.3",
    "SRR2749800.4",
    "SRR2749800.32097426",
    "SRR2749800.32097427",
    "SRR2749800.32097428",
    "SRR2749800.32097429",
]
comments = [
    "HWI-ST1253F_0122:4:1101:1135:2068 length=50",
    "HWI-ST1253F_0122:4:1101:1181:2160 length=50",
    "HWI-ST1253F_0122:4:1101:1334:2074 length=50",
    "HWI-ST1253F_0122:4:1101:1311:2108 length=50",
    "HWI-ST1253F_0122:4:2316:20484:101349 length=50",
    "HWI-ST1253F_0122:4:2316:20706:101287 length=50",
    "HWI-ST1253F_0122:4:2316:20569:101322 length=50",
    "HWI-ST1253F_0122:4:2316:20631:101330 length=50",
]
values = [
    "TNGATTGAGGTGACAGTTTCTGAGTTAAACTGCAGATCGGAAGAGCACAC",
    "TACGTTTATAGTTTAATGGGCCAATAATTGGTCAGATCGGAAGAGCACAC",
    "ANGGTGCTTGGACTACATATGGTTGAGGGTTGTACTGAAGATCGGAAGAG",
    "ATTCGACAGTAAGAAGAACAAATCGTGTAATCTGCAGATCGGAAGAGCAC",
    "TTCGNGCTTGGACTACATATGGTTGAGGGTTGTAGGAAAGATCGGAAGAG",
    "AAAANTCAGTTTGGGCGCGTCAGCATTGTTTTGGAGATCGGAAGAGCACA",
    "TTGGNTCTGCTAGGGTGCTATGAAATCTCTCCCAGATCGGAAGAGCACAC",
    "GAAGNCACGGTCGCCATATGAAAGGTGCTATGGTAGATCGGAAGAGCACA",
]


def test_load():
    infile = f"{test_dir}/data/fasta/sample_v4.fasta"
    reader_fasta = Fasta(infile)

    for fasta_entry, id, comment, value in zip(
        reader_fasta.read(), ids, comments, values
    ):
        assert fasta_entry["id"] == id
        assert fasta_entry["comment"] == comment
        assert fasta_entry["value"] == value

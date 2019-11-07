#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `yapq` package."""

import pytest

from yapq import Yapq

def fn(a, b):
    return a + b


def test_yapq(monkeypatch):
    yapq = Yapq()
    res1 = yapq.enqueue(fn, 5, 3)
    res2 = yapq.enqueue(fn, 2, 3)

    yapq.start()

    assert res2.get() == 5
    assert res1.get() == 8

    yapq.stop()

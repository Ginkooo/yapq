#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `yapq` package."""

import pytest


from yapq import Yapq

def fn(a, b):
    return a + b


def test_yapq(monkeypatch):
    yapq = Yapq()
    yapq.start()
    result = yapq.enqueue(fn, 5, 3)
    assert result.get() == 8
    yapq.stop()

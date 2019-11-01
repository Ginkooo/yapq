#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `yapq` package."""

import pytest


from yapq import yapq


def test_yapq():
    yapq.start()
    fn = lambda a, b: a + b
    result = yapq.enqueue(fn, 5, 3)
    assert result.get() == 8
    yapq.stop()

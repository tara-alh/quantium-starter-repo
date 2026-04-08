import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import app


def test_header_present():
    layout = app.layout
    assert any("Pink Morsels" in str(child) for child in layout.children)


def test_visualisation_present():
    layout = app.layout
    assert "sales-line-chart" in str(layout)


def test_region_picker_present():
    layout = app.layout
    assert "region-filter" in str(layout)
""" test existence of this package project docstring and version number. """
from ae.gui.__init__ import __doc__, __version__


def test_docstring():
    assert __doc__
    assert isinstance(__doc__, str)


def test_version():
    assert __version__
    assert isinstance(__version__, str)
    assert __version__.count(".") == 2

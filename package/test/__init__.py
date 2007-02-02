import unittest
from igraph.test import basic, games, foreign, structural, flow, \
    spectral, attributes, cliques, decomposition
from igraph import *

def suite():
    return unittest.TestSuite( \
        [basic.suite(),
	 games.suite(),
	 foreign.suite(),
	 structural.suite(),
	 flow.suite(),
	 spectral.suite(),
	 attributes.suite(),
	 cliques.suite(),
	 decomposition.suite()] \
    )
    
def test():
    runner = unittest.TextTestRunner()
    runner.run(suite())
    
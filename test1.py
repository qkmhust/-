import numpy as np
from dezero import Variable
from dezero.utils import plot_dot_graph

x0 = Variable(np.array(1.0))
x1 = Variable(np.array(1.0))
y = x0 + x1

x0.name = 'x0'
x1.name = 'x1'
y.name = 'y'

txt = plot_dot_graph(y, verbose=False)
print('txt:', txt)
# =============================================================================
# Run this code and you will get a file named add.png in the current directory.
# Open the file with an image viewer to see the graph.
# =============================================================================


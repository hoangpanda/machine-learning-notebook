import pandas as pd
import numpy as np


class TreeNode(object):
  def __init__(self, ids=None, children=[], entropy=0, depth=0)
    self.ids = ids
    self.entropy = entropy
    self.children = children
    self.depth = depth
    self.split_attribute = None
    self.order = None
    self.label = None

  def set_properties(self, split_attribute, order)



df = pd.read_csv('weather.csv', index_col = 0, parse_dates = True)

X = df.iloc[:, :-1]
#print(X)
y = df.iloc[:, -1] # decision


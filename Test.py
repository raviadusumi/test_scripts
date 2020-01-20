from __future__ import absolute_import, division, print_function, unicode_literals
import numpy as np
import pandas as pd
from pandas_datareader import data as pdr 
import matplotlib.pyplot as plt
import seaborn as sns
sns.set() #switches to seaborn defaults
import fix_yahoo_finance as yf
try:
  import tensorflow.compat.v2 as tf
except Exception:
  pass

tf.enable_v2_behavior()

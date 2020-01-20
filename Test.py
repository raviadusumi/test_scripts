from __future__ import absolute_import, division, print_function, unicode_literals
import numpy as np
import pandas as pd
from pandas_datareader import data as pdr 
import matplotlib.pyplot as plt
import seaborn as sns
sns.set() #switches to seaborn defaults
import fix_yahoo_finance as yf
try:
  # Use the %tensorflow_version magic if in colab.
  %tensorflow_version 2.x
except Exception:
  pass
import tensorflow as tf

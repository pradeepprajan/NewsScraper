# importing the libraries
import pandas as pd
import numpy as np
import time
import NewsScraper.mainstream as FD
import NewsScraper.digital_only as FD2

fe_list = FD.financial_express(1,1)
great_game_india_list = FD2.great_game_india()

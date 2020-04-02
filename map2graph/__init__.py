'''
A program to extract the roads within a bounding box 

Coordinate structure
  Lat London: 55.3781° N,
  Longitude London: 3.4360° W


Author: Dan Ellis
'''


import requests, json
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

string2coord


class bbox:
  ''' 
  A class to convert input into a bounding box
  input styles: 
    # bounding box as a string format
    ('(49.82380908513249,-10.8544921875,59.478568831926395,2.021484375)') string 
    
    # items each as strings
    ('52.146397, -3.492074','52.646397, -2.492074') str:str 
    
    # a bouni
    (latmin, lonmin, latmax, lonmax) float:float:float:float # this is already the bounding boxformat
    ((lon,lat),(lon,lat)) list(float,float),list(float,float)
    
  
  def :

def bb_coord(c1:List,c2:List):
  ''' 
  Returns a the bounding boxes between both corner coordinates
  '''

def boundingbox(latmin:float, latmax:float, lonmin:float, lonmax:float):
  ''' 
  Returns a the bounding boxes between both corner coordinates
  '''
  return (latmin

class GetGraph:
  def __init__ ( 

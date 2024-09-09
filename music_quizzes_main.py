import pandas as pd
import random

### READS SPREADSHEET ###
def read_data(tab_name):
    data = pd.read_excel("data/music_spreadsheet.xlsx", sheet_name=tab_name)
    return data
### RETURNS KEY AND DIATONIC SCALE ###
def diatonic_scale():
  df = read_data("Diatonic Scales")
  n = random.randint(0,len(df.index)-1)
  key = df.loc[n]['NOTE'] + ' ' + df.loc[n]['MAJOR/MINOR']
  answer = df.loc[n]['SCALE']
  return [key, answer]
### RETURNS KEY AND PENTATONIC SCALE ###
def pentatonic_scale():
   df = read_data("Pentatonic Scales")
   n = random.randint(0,len(df.index)-1)
   key = df.loc[n]['NOTE'] + df.loc[n]['MAJOR/MINOR']
   answer = df.loc[n]['SCALE']
   return [key, answer]
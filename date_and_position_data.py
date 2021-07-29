# -*- coding: utf-8 -*-
"""
@author: Jacob Oppelt
"""

#set counter for text file
text_file=0

data=[]

while text_file < 71:
    data.append(str(text_file)+'\n')
    text_file+=1

while text_file < 100 and text_file  >  70: #set open lower bound for counter
  f = open("00%s.txt" % text_file, "r") #opens .txt file as "f"
  lines = f.readlines() #reads f line by line and sets equal to lines (I think...)
  n=0 #Starts a counter for each line so that we can refer to previous ones later
  line_array=[] #Creates an empty list of the lines to be built
  for line in lines: #Not sure if I even need to do this
      line = line.strip() #Removes extra spaces?
      if line=="See http://www.SolarMonitor.org for images and": #Just looking for this one consistent phrase throughout the files
          data+=line_array[n-4]+line_array[n-2]
          break #No need to keep going through file if found
      else:
          line_array += lines #Keep looking through file and building line_array
          n+=1 #Go to next line
  f.close() #Close file cause thats a good thing to do?
  data.append(str(text_file)+'\n')
  text_file+=1 #Go to next file

while text_file < 1000 and text_file >=  100: #set open lower bound for counter
  f = open("0%s.txt" % text_file, "r") #opens .txt file as "f"
  lines = f.readlines() #reads f line by line and sets equal to lines (I think...)
  n=0 #Starts a counter for each line so that we can refer to previous ones later
  line_array=[] #Creates an empty list of the lines to be built
  for line in lines: #Not sure if I even need to do this
      line = line.strip() #Removes extra spaces?
      if line=="See http://www.SolarMonitor.org for images and": #Just looking for this one consistent phrase throughout the files
          data+=line_array[n-4]+line_array[n-2]
          break #No need to keep going through file if found
      else:
          line_array += lines #Keep looking through file and building line_array
          n+=1 #Go to next line
  f.close() #Close file cause thats a good thing to do?
  data.append(str(text_file)+'\n')
  text_file+=1 #Go to next file

while text_file >=  1000 and text_file < 7505: #set open lower bound for counter
  if text_file == 2244: #Niether of these messages exist. 2243=aug30,2006 and 2246=aug31,2006
      text_file+=1
  if text_file == 2245:
      text_file+=1
  else:
      f = open("%s.txt" % text_file, "r") #opens .txt file as "f"
      lines = f.readlines() #reads f line by line and sets equal to lines (I think...)
      n=0 #Starts a counter for each line so that we can refer to previous ones later
      line_array=[] #Creates an empty list of the lines to be built
      for line in lines: #Not sure if I even need to do this
          line = line.strip() #Removes extra spaces?
          if line=="See http://www.SolarMonitor.org for images and": #Just looking for this one consistent phrase throughout the files
              data+=line_array[n-4]+line_array[n-2]
              break #No need to keep going through file if found
          else:
                  line_array += lines #Keep looking through file and building line_array
                  n+=1 #Go to next line
      f.close() #Close file cause thats a good thing to do?
      data.append(str(text_file)+'\n')
      text_file+=1 #Go to next file

with open("dates_positions_data.txt","w") as file:
    file.writelines(data)

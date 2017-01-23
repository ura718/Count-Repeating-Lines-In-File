#!/usr/bin/python


#
# Use the msg log file and count up the lines per minutes.
# Basically identify how many lines fall into the same minute and print it out
# e.g:
#  read log file example
#  hours:minutes:seconds
#  11:22:01
#  11:22:10
#  11:23:05
#
#  output in hours:minutes
#  11:22, 2  <- indicates 2 lines are found at 22 minute
#  11:23, 1  <- indicates 1 line is found at 23 minute
#
#





file = 'msg'
with open(file, 'r') as f1:
  f1_lines = f1.readlines() 
  




# array that will hold time by minutes
array_min=[]




for i in f1_lines:


  # remove newline and then split line to make list
  i = i.strip().split()     


  # split line by column 0 - 3 (this column holds "month, day, hrs:min:sec") 
  t = i[0:3]                


  # t[2].split(':'), takes second column in list t and splits it by ':' colon
  # [0:2], out of 3 columns takes only first 2
  # ':'.join, this just joins the first 2 columns by ':' colon
  # assign output time with hour and minutes but no seconds 
  t_hm = ':'.join(t[2].split(':')[0:2])


  # time is same but without seconds
  t = ' '.join(t[:2]) + ' ' + t_hm

  # append output to array
  array_min.append(t)




# setup empty hash
result = {}



# counts how many items in array are identical and prints the count of those elements in hash
for item in array_min:
    try:
      result[item] += 1     # create hash key and increment value by 1
    except KeyError:
      result[item] = 1      # if key does not exist then create it and set value to 1

   

# print key and value, sorted by key
for k,v in sorted(result.items()):
    print "%s, %s" % (k,v)



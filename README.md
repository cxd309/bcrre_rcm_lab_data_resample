# BCRRE Remote Condition Monitoring Lab - Data Resampling
*Author: Chris Davis, email: cxd309@student.bham.ac.uk*

## Introduction
This is a resample of the data taken during the MSc Remote Condition Monitoring Labs.
The aim being to make it easier for some student to work with the datasets on their
computers.

### Information for Students
If you use these in your final reports you should detail exactly which dataset is being
used. The method used to resample the data will impact the data itself and you should
write how it will be affected in your report. The detail on method used is all explained
below and if you need more information you can always ask.

## Method
The python file 'resample.py' was created and uses the pandas package to interact 
with the .csv input files.

There are two methods for downsampling
* simple
* average

Both use downsample with a ratio n from the captured data frequency of 2kHz.
For example, to downsample to 100Hz, a ratio n=20 is used.

The chosen frequencies to resample at are:
* 1000Hz (n=2)
* 500Hz  (n=4)
* 250Hz  (n=8)
* 200Hz  (n=10)
* 100Hz  (n=20)

### simple downsampling

To downsample the programme takes a ratio n 
it then selects every nth line from the original file.
For instance to downsample from 2000Hz to 1000Hz
the ratio is 2 (n=2) so the programme selects rows 1, 3, 5, 7, etc.

### average downsampling
To downsample the programme takes a ratio n 
it then groups every n lines from the original file
and takes an average of those.
for instance to downsample from 2000Hz to 1000Hz
the ratio is 2 (n=2) so the programme groups and averages
rows 1&2, 3&4, 5&6, 7&8, etc.


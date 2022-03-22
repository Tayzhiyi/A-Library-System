LOAD DATA INFILE '/Users/bryanwonggy/Library/Mobile Documents/com~apple~CloudDocs/b/nus/y1s2/bt2102/assignment 1/LibBooks.txt'
INTO TABLE Book  
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

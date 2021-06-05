#How many employees does the city have?
uniq salaries.csv | wc -l
#33184

#How many full-time workers are there in the file?
cut -d, -f5 salaries.csv | grep F | wc -l
#31090

#How many part-time workers are there in the file?
cut -d, -f5 salaries.csv | grep P | wc -l
#2093

#How many people work for the police department?
cut -d, -f4 salaries.csv | grep POLICE | wc -l
#13416

#How many of them are detectives?
cut -d, -f3-4 salaries.csv | grep POLICE | grep DETECTIVE | wc -l
#989

#Which department has the most employees?
cut -d, -f4 salaries.csv | sort | uniq -c | sort -n | tail -1

# 13414 POLICE deparment

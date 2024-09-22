from textanalysis.textanalysis import count

count_verbs = count("Awholetext.txt", ['are', 'am', 'is', 'was', 'were', 'been', 'being'])

print(count_verbs)
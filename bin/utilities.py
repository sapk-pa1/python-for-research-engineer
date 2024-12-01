import sys 
import csv


def collections_to_csv(collection, num=None): 
    if num ==None: 
        num = len(collection) 
    writer = csv.writer(sys.stdout)
    writer.writerow(["Word", "Count"])  # Write header
    for word, count in collection.most_common(num):
        writer.writerow([word, count])

# Importing Functions
from thoughtspot_tml import Worksheet
from pathlib import Path
from thoughtspot_tml import Table, View, SQLView, Worksheet
from thoughtspot_tml import Answer, Liveboard
import yaml
import os

# Paths of repo
n = int(input("Specify the env you want to work with 1.ts-migration 2.program-kpis\n"))
if n == 1:
    path = "/Users/arunnandam/Documents/WorkSpace/Fixes/dw-tspot-migration"
elif n == 2:
    path = "/Users/arunnandam/Documents/WorkSpace/Fixes/dw-tspot-program-metrics"

target_folders =  ["answer", "liveboard"]
def add_filter(file_path, i):
    if i == "answer":
        file = Answer.load(path=file_path)
        if (file.answer!=None):
            if (file.answer.tables[0].name == "Fact Metrics" and file.answer.search_query != None and "[Status]" not in file.answer.search_query):
                print("Added status filter for ", file.answer.name)
                file.answer.search_query = file.answer.search_query.strip() + " [Status] = 'finished' "
                file.dump(path=file_path)
            else:
                print("No changes made to ", file.answer.name)
    elif i == "liveboard":
        file = Liveboard.load(path=file_path)
        for i in file.liveboard.visualizations:
            if (i.answer!=None):
                if (i.answer.tables[0].name == "Fact Metrics" and i.answer.search_query != None and "[Status]" not in i.answer.search_query):
                    print("Added status filter for ", i.answer.name)
                    i.answer.search_query = i.answer.search_query.strip() + " [Status] = 'finished' "
                    file.dump(path=file_path)
                else:
                    print("No changes made to ", i.answer.name)
            else:
                print("Null Viz: ", i.id)

for i in target_folders:
    sub_path = os.path.join(path, i)
    print(f"Current directory: {sub_path}")
    for filename in os.listdir(sub_path):
        file_path = os.path.join(sub_path, filename)
        if os.path.isfile(file_path):  # Check if it's a file and not a subdirectory
            try:
                print(f"\nProcessing file: {filename}", sep='\n')
                add_filter(file_path, i)
            except Exception as e:
                print(f"Error reading {filename}: {e}")


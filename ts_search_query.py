from thoughtspot_tml import Worksheet
from pathlib import Path
from thoughtspot_tml import Table, View, SQLView, Worksheet
from thoughtspot_tml import Answer, Liveboard
import yaml

# Load a worksheet from a .worksheet.tml file
ws = Answer.load(path=Path("answer/Program KPIs v2.04526251-40c0-4c39-b199-b31cdf86347b.answer.tml"))

print(ws.answer.tables[0].name)
if (ws.answer!=None):
    if (ws.answer.tables[0].name == "Fact Metrics" and ws.answer.search_query != None and "[Status]" not in ws.answer.search_query):
        print("Added status filter for ", ws.answer.name)
        ws.answer.search_query = ws.answer.search_query.strip() + " [Status] = 'finished' "
        ws.dump(path="answer/Program KPIs v3.0823d8e1-3da6-41e6-8c0a-3abd9f6295e9.answer.tml")
    else:
        print("No changes made to ", ws.answer.name)
# ws.answer.search_query = "[Dealership Name] [Dealer Group Code] [Dealer Group].''autonation inc.'' [The Date] = ''last 1 month'' sort by [Dealership Name] [formula_Avg Length of Loan] [formula_Utilization] [Implementation Status] != ''churn'' [formula_String Date] [Status] = ''finished'' "
# ws.dump(path="answer/AutoNation_KPIs_Last_Month_sftp.34f40735-1584-445c-9637-49a57f2b6dc6.answer.tml")

# print(ws.liveboard.visualizations)

# for i in ws.liveboard.visualizations:
#     print(i.id, sep='\n')
#     if (i.answer!= None ):
#         if ( i.answer.search_query != None and "[Status]" not in i.answer.search_query ):
#             #print("Added status filter\n")
#             #i.answer.search_query = i.answer.search_query.strip() + " [Status] = 'finished' "
#             #ws.dump(path="liveboard/Volvo Car USA.a924117d-3dba-4fcd-9193-ad3c26ddfd9b.liveboard.tml")
#             print("No Status filter found\n")
#         else:
#             print("Status Filter Found\n")

from flask import Flask, request, jsonify
import os
import pandas as pd
import re
import json
import pymongo
from flask_cors import CORS
from functools import reduce

myclient = pymongo.MongoClient("mongodb+srv://medalfever:kuvpot-zyzsu3-Doqmes@cluster0.fvidjpo.mongodb.net/")
mydb = myclient['MSCs']

app = Flask(__name__)


CORS(app)


def projectMeta(projectId):
    import requests
    from bs4 import BeautifulSoup
    url = 'https://www.ncbi.nlm.nih.gov/bioproject/%s/' % projectId
    page = requests.get(url)
    with open("text.xml", "w") as handle:
        handle.write(page.text)
    htmlfile = open("text.xml", 'r', encoding='utf-8')
    htmlfile = htmlfile.read()
    soup = BeautifulSoup(htmlfile, 'lxml')
    
    try:
        summary = soup.find(id="DescrAll").text
    except:
        summary = soup.find(class_="Description").text
        
    year = int(re.findall("Registration date: [0-9]{1,2}-[A-Za-z]{1,5}-([0-9]{4})", soup.text)[0])
    sample = int(soup.find(id="SRA Experiments").text)
    try:
        name = soup.find(class_='Title').h3.text
    except:
        name = soup.find(class_='Title').h2.text
    link = "Unknown"
    for x in soup.find_all(class_="CTtitle"):
        if x.text == 'Publications':
            link = "https://www.ncbi.nlm.nih.gov" + x.find_next(class_="RegularLink").attrs['href']
            
    return {
        "ProjectId": projectId,
        "Summary": summary,
        "SampleCount": sample,
        "LinkToPaper": link,
        "Year": year,
        "ProjectName": name,
        'ProjectLink': f'https://www.ncbi.nlm.nih.gov/bioproject/{projectId}/'
    }

def sra_result(projectId, fpath="MSC_Sra_files"):
    
    import os
    import pandas as pd
    import xml.etree.ElementTree as ET
    
    if not os.path.exists(fpath):
        os.mkdir(fpath)
    
    if not os.path.exists(f"{fpath}/{projectId}_sra_result.xml"):
        os.system(f"esearch -db sra -query {projectId} | efetch -format xml > {fpath}/{projectId}_sra_result.xml")
    if not os.path.exists(f"{fpath}/{projectId}_SraRunInfo.csv"):
        os.system(f"esearch -db sra -query {projectId} | efetch -format runinfo > {fpath}/{projectId}_SraRunInfo.csv")
    root = ET.parse(f'{fpath}/{projectId}_sra_result.xml').getroot()
    res = []
    for exp in root.findall("EXPERIMENT_PACKAGE"):
        exp_id = exp.find("EXPERIMENT").attrib['accession']
        try:
            exp_title = exp.find("EXPERIMENT/TITLE").text
        except:
            exp_title = "None"

        try:
            sample_title = exp.find("SAMPLE/TITLE").text
        except:
            sample_title = "None"

        try:
            study_title = exp.find("STUDY/STUDY_TITLE").text
        except:
            study_title = "None"
            
        try:
            library_name =  exp.find("EXPERIMENT/DESIGN/LIBRARY_DESCRIPTOR/LIBRARY_NAME").text
        except:
            library_name = "None"
            
        for run in exp.findall("RUN_SET/RUN"):
            res.append({
                "ex_RunId": run.attrib['accession'],
                "ex_ExperimentId": exp_id,
                "ex_ExperimentTitle":exp_title,
                "ex_SampleTitle": sample_title,
                "ex_StudyTitle": study_title,
                "ex_LibraryName": library_name
            })
        
    s1 = pd.read_csv(f"{fpath}/{projectId}_SraRunInfo.csv").sort_values('Run').reset_index(names= 'S1')
    s2 = pd.DataFrame(res).sort_values('ex_RunId').reset_index(names = 'S2')
    return pd.concat([s1, s2], axis=1).to_json(orient='records')

@app.route("/")
def main():
    return 'Hello, world'

@app.route("/getInfo/<projectid>")
def hello_world(projectid):
    return sra_result(projectid.strip())

@app.route("/projectInfo/<projectid>")
def hello_tree(projectid):
    return projectMeta(projectid.strip())

@app.route("/upLoad", methods = ['GET', 'POST'])
def getJSON():
    content = request.get_json()
    try:
        author = content['author']
    except:
        author = 'Unknown'
    content = content['data']
    pid = content[0]['ProjectId']

     #save results files to local
    with open(f"MSC_results/{pid}_{author}.json", 'w') as handle:
        json.dump(content, handle)

    #update sample table
    mydb['samples'].delete_many({'ProjectId': pid})
    mydb['samples'].insert_many(content)

    #update projects table
    mydb['projects'].delete_many({'ProjectId': pid})
    demensions = ['Source', 'Marker', 'Treatment', 'Condition', 'Species']
    body = hello_tree(pid)
    for dim in demensions:
        body[dim] = reduce(lambda x, y: x + y, [ item[dim] if type(item[dim]) != str else [item[dim]] for item in content ])
        body[dim] = list(set(body[dim]))
    mydb['projects'].insert_one(body)
    
@app.route("/dashboard")
def listinfo():
    ss = list(mydb['projects'].find({}, {'_id': 0}))
    return {
        'count': len(ss),
        'data': ss
    }

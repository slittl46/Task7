#import beautifulsoup and request here
from bs4 import BeautifulSoup
import requests
import json
import numpy
from flask import Flask, render_template, jsonify, serialize

app = Flask(__name__)

@app.route("/")
def displayJobDetails():
    
    responseJSON = requests.get('https://raw.githubusercontent.com/gaganj007/beautifulSoup/main/jobDetails.json?token=GHSAT0AAAAAABTRM2XHP3DJVMZWTYZGGXGEYS7EBTQ')
    my_json= json.loads(responseJSON.text)
    return render_template('index.html', final_json= jsonify(my_json))
    


#function to get job list from url 'https://www.indeed.com/jobs?q={role}&l={location}'
def getJobList(role,location):
    url = 'https://www.indeed.com/jobs?q={role}&l={location}'
    url = url.replace("{role}",role)
    url = url.replace("{location}",location)
    # Complete the missing part of this function here 

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    jobTitle = soup.find('h2',class_='jobTitle').text
    companyName = soup.find('span',class_='companyName').text
    jobSnippet = soup.find('div',class_='job-snippet').text
    salarySnippetContainer = soup.find('div',class_='salary-snippet-container').text

    jobDetails = [
        {
            "Title": jobTitle,
            "Company": companyName,
            "Description": jobSnippet,
            "Salary": salarySnippetContainer
        }
    ]



    jobDetails = json.dumps(jobDetails)

    return jobDetails


#save data in JSON file
def saveDataInJSON(jobDetails):
    #Complete the missing part of this function here
    print("Saving data to JSON")

    with open("jobDetails.json","w") as file:
        for i in jobDetails:
            file.write(i)
    
    file.close()



#main function
def main():
    # Write a code here to get job location and role from user e.g. role = input()
    print("Enter role you want to search")
    role = input()
    print("Enter location you want to search")
    location = input()
    
    print("Role: "+role+" Location: "+location)
    print(getJobList(role,location))
    saveDataInJSON(getJobList(role,location))
    # Complete the missing part of this function here
   
    
if __name__ == '__main__':
    main()
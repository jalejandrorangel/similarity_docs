import boto3

def startJob(s3BucketName, objectName):
    response = None
    client = boto3.client('textract')
    response = client.start_document_text_detection(
    DocumentLocation={
        'S3Object': {
            'Bucket': s3BucketName,
            'Name': objectName
        }
    })

    return response["JobId"]

def isJobComplete(jobId):
    client = boto3.client('textract')
    response = client.get_document_text_detection(JobId=jobId)
    status = response["JobStatus"]

    while(status == "IN_PROGRESS"):
        response = client.get_document_text_detection(JobId=jobId)
        status = response["JobStatus"]

    return status

def getJobResults(jobId):

    pages = []
    client = boto3.client('textract')
    response = client.get_document_text_detection(JobId=jobId)
    
    pages.append(response)
    nextToken = None
    if('NextToken' in response):
        nextToken = response['NextToken']

    while(nextToken):

        response = client.get_document_text_detection(JobId=jobId, NextToken=nextToken)

        pages.append(response)
        nextToken = None
        if('NextToken' in response):
            nextToken = response['NextToken']

    return pages
def get_textPdf(s3BucketName, documentName):

    jobId = startJob(s3BucketName, documentName)
    
    if(isJobComplete(jobId)):
        response = getJobResults(jobId)
    text = []
    for resultPage in response:
        for item in resultPage["Blocks"]:
            if item["BlockType"] == "LINE":
                text.append(item["Text"])
    return text

#s3BucketName = "text-demo-peor-equipo"
#documentName = "test.pdf"
#text = get_textPdf(s3BucketName,documentName)
#print(text)

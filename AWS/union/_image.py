import boto3

def get_textImage(s3BucketName,documentName):

    textract = boto3.client('textract')

    # Call Amazon Textract
    response = textract.detect_document_text(
        Document={
            'S3Object': {
                'Bucket': s3BucketName,
                'Name': documentName
            }
        })

    #print(response)

    # Print detected text
    text = []
    for item in response["Blocks"]:
        if item["BlockType"] == "LINE":
            text.append(item["Text"])
    return text

#s3BucketName = "text-demo-peor-equipo"
#documentName = "ttt.png"

import boto3
import os

class TableCreationOps:
    dynamodbclient = boto3.client('dynamodb', aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
                                       aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
                                       region_name=os.environ.get('AWS_DEFAULT_REGION'))

    def checkifexist(self,tablename):
        existing_tables = self.dynamodbclient.list_tables()['TableNames']
        if tablename not in existing_tables:
            return True
        else:
            return False

    def createtable(self, tablename,primarykey,sortkey):

        self.dynamodbclient.create_table(
        TableName=tablename,
        KeySchema=[
            {
                'AttributeName': primarykey,
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': sortkey,
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': primarykey,
                'AttributeType': 'S'
            },
            {
                'AttributeName': sortkey,
                'AttributeType': 'S'
            }

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )



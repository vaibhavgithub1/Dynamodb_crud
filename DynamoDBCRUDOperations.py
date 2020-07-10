import boto3
import os

class DynamoDBCRUDOps:
    dynamodbclient = boto3.client('dynamodb', aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
                                  aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
                                  region_name=os.environ.get('AWS_DEFAULT_REGION'))


    def addItem(self,tablename,id,age):
        try:
            res = self.dynamodbclient.put_item(TableName=tablename,
                                  Item={"id": {"S": id}, "age": {"S": age}})
        except Exception as e:
            print("Error Occured ", e)

    def updateItem(self,tablename,id,age,name):
        try:
            res = self.dynamodbclient.update_item(TableName=tablename,
                                     Key={"id": {"S": id},"age": {"S": age}},
                                     UpdateExpression="set name=:n",
                                      ExpressionAttributeValues={
                                          ':n':str(name)
                                      },
                                     ReturnValues="UPDATED_NEW")
        except Exception as e:
            print("Error Occured ", e)

    def deleteItem(self,tablename,id,age):
        try:
            self.dynamodbclient.delete_item(TableName=tablename,
                               Key={"id": {"S": id},"age":{"S": age}})
        except Exception as e:
            print("Error Occured ", e)

    def readItem(self,tablename,id,age):
        try:
            res=self.dynamodbclient.get_item(TableName=tablename, Key={"id": {"S": id},"age": {"S": age}})
            return res["Item"]
        except Exception as e:
            print("Error Occured ", e)




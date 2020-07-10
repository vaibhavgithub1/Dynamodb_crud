import Dynamodb_CRUD_Ops
from TableCreationOps import TableCreationOps
from DynamoDBCRUDOperations import DynamoDBCRUDOps
from dynamodb_json import json_util as json


if __name__ == '__main__':
    try:
        # tablename="emp"
        # primarykey="id"
        # sortkey="age"

        # create table
        # table=TableCreationOps()
        # table.createtable(tablename,primarykey,sortkey)

        # add item
        #dbobj=DynamoDBCRUDOps()
        # dbobj.addItem("emp","25","27")

        # delete item
        #dbobj=DynamoDBCRUDOps()
        #dbobj.deleteItem("emp","25","27")

        # update item
        dbobj=DynamoDBCRUDOps()
        dbobj.updateItem("emp","25","27","xyz")

        # read item
        #dbobj=DynamoDBCRUDOps()
        #print(json.loads(dbobj.readItem("emp","25","27")))






    except Exception as e :
        print("Error Occured ",e)


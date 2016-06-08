import boto3

dyndb_client = boto3.client('dynamodb', region_name='eu-central-1')

tablesToDelete = ['ProductCatalog', 'Forum', 'Thread', 'Reply']

for tableName in tablesToDelete:
    print('Will try to delete table %s.' % tableName)
    try:
        dyndb_client.delete_table(TableName=tableName)
        print('Table %s successfully deleted.' % tableName)
    except ResourceNotFoundException as ex:
        print('Table %s does not exist. Nothing to do.' % tableName)



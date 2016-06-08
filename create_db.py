import boto3

dynamodb = boto3.resource('dynamodb', region_name='eu-central-1')
dyndb_client = boto3.client('dynamodb', region_name='eu-central-1')
tables = []

tableName = 'ProductCatalog'
print('Checking if table %s exists.' % tableName)
try:
    description = dyndb_client.describe_table(TableName=tableName)
    print('Table %s already exists. \n %s' % (tableName, description))
except ResourceNotFoundException as ex:
    print('Table %s does not exist. Creating table.' % tableName)
    table = dynamodb.create_table(
        TableName = tableName,
        AttributeDefinitions = [
            {
                'AttributeName' : 'Id',
                'AttributeType' : 'N'
            }
        ],
        KeySchema = [
            {
                'AttributeName' : 'Id',
                'KeyType' : 'HASH'
            }
        ],
        ProvisionedThroughput = {
            'ReadCapacityUnits' : 10,
            'WriteCapacityUnits' : 5
        }
    )
    print('Creation of table %s was successful' % tableName)
    tables.append(tableName)

tableName = 'Forum'
print('Checking if table %s exists.' % tableName)
try:
    description = dyndb_client.describe_table(TableName=tableName)
    print('Table %s already exists. \n %s' % (tableName, description))
except ResourceNotFoundException as ex:
    print('Table %s does not exist. Creating table.' % tableName)
    table = dynamodb.create_table(
        TableName = tableName,
        AttributeDefinitions = [
            {
                'AttributeName' : 'Name',
                'AttributeType' : 'S'
            }
        ],
        KeySchema = [
            {
                'AttributeName' : 'Name',
                'KeyType' : 'HASH'
            }
        ],
        ProvisionedThroughput = {
            'ReadCapacityUnits' : 10,
            'WriteCapacityUnits' : 5
        }
    )
    print('Creation of table %s was successful' % tableName)
    tables.append(tableName)

tableName = 'Thread'
print('Checking if table %s exists.' % tableName)
try:
    description = dyndb_client.describe_table(TableName=tableName)
    print('Table %s already exists. \n %s' % (tableName, description))
except ResourceNotFoundException as ex:
    print('Table %s does not exist. Creating table.' % tableName)

    table = dynamodb.create_table(
        TableName = tableName,
        AttributeDefinitions = [
            {
                'AttributeName' : 'ForumName',
                'AttributeType' : 'S'
            },
            {
                'AttributeName' : 'Subject',
                'AttributeType' : 'S'
            }
        ],
        KeySchema = [
            {
                'AttributeName' : 'ForumName',
                'KeyType' : 'HASH'
            },
            {
                'AttributeName' : 'Subject',
                'KeyType'       : 'RANGE'
            }
        ],
        ProvisionedThroughput = {
            'ReadCapacityUnits' : 10,
            'WriteCapacityUnits' : 5
        }
    )
    print('Creation of table %s was successful' % tableName)
    tables.append(tableName)

tableName = 'Reply'
print('Checking if table %s exists.' % tableName)
try:
    description = dyndb_client.describe_table(TableName=tableName)
    print('Table %s already exists. \n %s' % (tableName, description))
except ResourceNotFoundException as ex:

    print('Table %s does not exist. Creating table.' % tableName)
    table = dynamodb.create_table(
        TableName = tableName,
        AttributeDefinitions = [
            {
                'AttributeName' : 'Id',
                'AttributeType' : 'S'
            },
            {
                'AttributeName' : 'ReplyDateTime',
                'AttributeType' : 'S'
            },
            {
                'AttributeName': 'PostedBy',
                'AttributeType': 'S'
            }
        ],
        LocalSecondaryIndexes = [
            {
                'IndexName' : 'PostedBy-index',
                'KeySchema' : [
                    {
                        'AttributeName' : 'Id',
                        'KeyType'       : 'HASH'
                    },
                    {
                        'AttributeName' : 'PostedBy',
                        'KeyType' : 'RANGE'
                    }
                ],
                'Projection' : {
                    'ProjectionType' : 'KEYS_ONLY'
                }
            }
        ],
        KeySchema = [
            {
                'AttributeName' : 'Id',
                'KeyType' : 'HASH'
            },
            {
                'AttributeName' : 'ReplyDateTime',
                'KeyType' : 'RANGE'
            }
        ],
        ProvisionedThroughput = {
            'ReadCapacityUnits' : 10,
            'WriteCapacityUnits' : 5
        }
    )
    print('Creation of table %s was successful' % tableName)
    tables.append(tableName)
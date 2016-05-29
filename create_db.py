import boto3

dynamodb = boto3.resource('dynamodb', region_name='eu-central-1')

tables = []
tableName = 'ProductCatalog'

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

tables.append(tableName)

tableName = 'Forum'

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

tables.append(tableName)

tableName = 'Thread'

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
        }
    ],
    ProvisionedThroughput = {
        'ReadCapacityUnits' : 10,
        'WriteCapacityUnits' : 5
    }
)

tables.append(tableName)

tableName = 'Reply'

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
        }
    ],
    ProvisionedThroughput = {
        'ReadCapacityUnits' : 10,
        'WriteCapacityUnits' : 5
    }
)
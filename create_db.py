import boto3

dynamodb = boto3.resource('dynamodb', region_name='eu-central-1')

tables = []
tableName = 'ProductCatalog'
print 'Creating table: %s' % tableName

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
print 'Creation of table %s was successful' % tableName
tables.append(tableName)

tableName = 'Forum'
ptint 'Creating table %s' % tableName

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

print 'Creation of table %s was successful' % tableName
tables.append(tableName)

tableName = 'Thread'
print 'Creating table %s' % tableName

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
print 'Creation of table %s was successful' % tableName
tables.append(tableName)

tableName = 'Reply'
print 'Creating table %s' % tableName
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
        #{
        #    IndexName = 'PostedBy-index',
        #    KeySchema = [
        #        {
        #            'AttributeName' = 'Id',
        #            'KeyType'       = 'HASH'
        #        },
        #        {

        #        }
        #    ],
        #}

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
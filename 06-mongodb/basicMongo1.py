import pymongo


def insert_data():
    """Insert data to mongodb"""
    client = pymongo.MongoClient('localhost', 27017)
    db = client.get_database("tnidatabase")
    # insert_one
    # rs = db.students.insert_one({'id':'785444', 'name':'Somchai'})
    # print('Inserted one document: {}'.format(rs.inserted_id))

    # insert_many
    rs = db.students.insert_many([
        {'id': '4521', 'name': 'somsak'},
        {'id': '84754', 'name': 'Wimol'},
        {'id': '78787', 'name': 'Sirisak'}
    ])
    print('Inserted: {}'.format(rs.inserted_ids))


if __name__ == '__main__':
    insert_data()

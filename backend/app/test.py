import api.database as db
def format_for_json(lst) -> list:
    output = []
    columns = db.database_get_columns("jobpost")
    for i in range(len(lst)):
        record = lst[i]
        dic = {}
        for j in range(len(record)):
            print("key:",columns[j])
            print("value:",record[j])
            dic[columns[j]]=record[j]
        output.append(dic)
    return output



lst =[('0001', 'Saleperson', 'Sale', 'On Site', "We're hiring saleman, come in pls", "datetime.datetime(2025, 4, 29, 11, 54)"), ('0002', 'Software Engineer', 'Engineer', 'Remote', "We're hiring engineer, come in pls", "datetime.datetime(2025, 4, 29, 11, 55)")]
print(format_for_json(lst))
#[('0001', 'Saleperson', 'Sale', 'On Site', "We're hiring saleman, come in pls", datetime.datetime(2025, 4, 29, 11, 54)), ('0002', 'Software Engineer', 'Engineer', 'Remote', "We're hiring engineer, come in pls", datetime.datetime(2025, 4, 29, 11, 55))]

#into  {records: [{"id":"0001", "title":"Saleperson", "department":"Sale",...}, {"id":"0002",...}]}

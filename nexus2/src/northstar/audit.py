import json
import os

AUDIT_FILE = "audit.json"


class AuditRecord:
    def __init__(self, customer_id, actor_id, reason):
        self.customer_id = customer_id
        self.actor_id = actor_id
        self.reason = reason



class Auditor:
    def __init__(self):
        self.records = []

        if os.path.exists(AUDIT_FILE):
            with open(AUDIT_FILE, "r+") as file:
                for line in file:
                    dict = json.loads(line.strip())
                    record = AuditRecord(**dict)
                    self.records.append(record)

    # Adds a record to the internal list
    def add_record(self, record: AuditRecord):
        self.records.append(record)

        with open(AUDIT_FILE, "a+") as file:
            file.write(json.dumps(record.__dict__) + "\n")
            


    # returns all records as a list of dictionaries
    def get_all(self):
        list_of_record_dicts = []

        for record in self.records:
            list_of_record_dicts.append(record.__dict__)

        return list_of_record_dicts

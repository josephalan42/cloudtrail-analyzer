import json

def extract_events(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)

    records = data.get("Records", [])
    events = []

    for record in records:
        event_name = record.get("eventName", "Unknown")
        user_identity = record.get("userIdentity", {})
        user_name = user_identity.get("userName", "Unknown")
        source_ip = record.get("sourceIPAddress", "Unknown")

        event = {
            "eventName": event_name,
            "user": user_name,
            "sourceIP": source_ip
        }

        events.append(event)

    return events

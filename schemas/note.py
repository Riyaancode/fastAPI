def notEntity(item) -> dict:
    return {
        # "id": str(item["_id"]),
        "title": str(item["title"]),
        "description": str(item["description"]),
        "important": str(item["important"])
    }

def notEntityList(items) -> list:
    return [notEntity(item) for item in items]

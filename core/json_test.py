import json

content = "this is the content"

json_data = {
    "content": content

}

final_json_data = json.dumps(json_data)

print(final_json_data)
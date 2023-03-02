import json

def calculate_client_value(client_number: int) -> str:
    total_value = 0
    result_str = ""
    try:
        with open('database/insurance.json') as file:
            data = json.load(file)
            insurances = data[f"{client_number}"]
            for k, v in insurances.items():
                total_value += int(v)
                result_str += k
                result_str += " : "
                result_str += v
                result_str += "<br>"
            result_str += f"Total client value : {total_value}"
            return result_str
    except Exception as e:
        print(e)
        return ""
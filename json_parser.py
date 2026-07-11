import json
import pandas as pd

def run_json_extraction_engine():
    print("--- AgenticFlow Tech: Autonomous JSON Extraction Engine ---")
    
    # Simulating a complex incoming JSON data payload from a live web server
    raw_json_payload = """
    {
        "status": "success",
        "timestamp": 1783800000,
        "data": {
            "batch_id": "ERR_LOG_990",
            "records": [
                {"timestamp_offset": 0, "device_id": "DEV_A", "reading": 12.4},
                {"timestamp_offset": 5, "device_id": "DEV_B", "reading": 15.8},
                {"timestamp_offset": 10, "device_id": "DEV_A", "reading": 19.2},
                {"timestamp_offset": 15, "device_id": "DEV_C", "reading": 22.1}
            ]
        }
    }
    """
    
    print("[INFO] Parsing raw incoming JSON payload...")
    
    # 1. Loading the JSON data string into a python dictionary
    parsed_data = json.loads(raw_json_payload)
    
    # 2. Extracting deep nested structures automatically
    records_list = parsed_data["data"]["records"]
    batch = parsed_data["data"]["batch_id"]
    
    print(f"[SUCCESS] Target data batch '{batch}' successfully isolated.")
    
    # 3. Structuring the isolated records into a data frame
    df = pd.DataFrame(records_list)
    
    # 4. Processing automated calculations on the nested data
    df["normalized_reading"] = df["reading"] * 1.05
    
    print("\n[METRIC REPORT] Structured JSON Array Output:\n")
    print(df.to_string(index=False))
    print("==========================================================")

if __name__ == "__main__":
    run_json_extraction_engine()

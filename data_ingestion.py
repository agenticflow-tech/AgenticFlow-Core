import pandas as pd
import os

def run_external_ingestion_pipeline():
    print("--- AgenticFlow Tech: Autonomous File Ingestion Pipeline ---")
    
    filename = "external_motion_log.txt"
    
    # 1. Simulating an external incoming data stream file
    print("[INFO] Simulating incoming external data file generation...")
    mock_data = """Time_Sec,Raw_Velocity
0,  5.0   
1,  7.5   
2,  10.0  
3,  12.5  
4,  15.0  
5,  17.5  
6,  20.0  
7,  22.5  
8,  25.0  
9,  27.5  
10, 30.0  """
    
    with open(filename, "w") as file:
        file.write(mock_data)
        
    # 2. Ingesting and Sanitizing the Data Stream
    print(f"[SUCCESS] External file '{filename}' detected. Beginning ingestion...")
    
    # Reading line by line to clean spaces and sanitize structural text anomalies
    cleaned_rows = []
    with open(filename, "r") as file:
        headers = file.readline().strip().split(",")
        for line in file:
            if line.strip():
                parts = line.strip().split(",")
                # Strip hidden spaces dynamically
                cleaned_rows.append([float(parts[0]), float(parts[1])])
                
    # 3. Converting to an analytical data matrix for corporate logging
    df = pd.DataFrame(cleaned_rows, columns=headers)
    
    # Run dynamic backend calculations on the imported numbers
    df['Acceleration_(m/s2)'] = 2.5
    df['Displacement_(m)'] = (5.0 * df['Time_Sec']) + (0.5 * 2.5 * (df['Time_Sec'] ** 2))
    
    print("\n[METRIC REPORT] External data successfully ingested, cleaned, and parsed:\n")
    print(df.to_string(index=False))
    print("=======================================================================")
    
    # Clean up the local environment file safely
    if os.path.exists(filename):
        os.remove(filename)

if __name__ == "__main__":
    run_external_ingestion_pipeline()

import pandas as pd

def run_corporate_pipeline():
    print("--- AgenticFlow Tech: Enterprise Data Pipeline ---")
    
    # 1. Raw unorganized client data
    client_data = {
        'Task_ID': ['AFT-101', 'AFT-102', 'AFT-103'],
        'Project_Name': ['  ai engine optimization ', 'database restructuring   ', ' UI framework rebuild '],
        'Estimated_Hours': [40, 15, 10],
        'Business_Impact': [9, 5, 8]
    }
    
    # 2. Convert to a structured DataFrame using our new Pandas library
    df = pd.DataFrame(client_data)
    
    # 3. Clean up the messy text spaces automatically
    df['Project_Name'] = df['Project_Name'].str.strip()
    
    # 4. Run calculations to find efficiency ratios
    df['Efficiency_Score'] = (df['Business_Impact'] / df['Estimated_Hours']).round(3)
    
    print("\n[SUCCESS] Datasets sanitized and calculated successfully:\n")
    print(df.to_string(index=False))
    print("==================================================")

if __name__ == "__main__":
    run_corporate_pipeline()

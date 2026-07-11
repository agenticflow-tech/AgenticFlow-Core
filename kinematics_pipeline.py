import pandas as pd

def simulate_kinematics():
    print("--- AgenticFlow Tech: Kinematics Data Pipeline ---")
    
    # Define initial parameters (SI units)
    initial_velocity = 5.0  # u in m/s
    acceleration = 2.5      # a in m/s^2
    time_intervals = list(range(0, 11))  # t from 0 to 10 seconds
    
    # Lists to store our calculated physics metrics
    velocities = []
    displacements = []
    
    # Data Processing Loop: Apply kinematics equations
    for t in time_intervals:
        # Final Velocity: v = u + at
        v = initial_velocity + (acceleration * t)
        velocities.append(v)
        
        # Displacement: s = ut + 0.5 * a * t^2
        s = (initial_velocity * t) + (0.5 * acceleration * (t ** 2))
        displacements.append(s)
    
    # Organize calculations into an enterprise data matrix
    motion_data = {
        'Time_(s)': time_intervals,
        'Initial_Vel_(m/s)': [initial_velocity] * len(time_intervals),
        'Acceleration_(m/s2)': [acceleration] * len(time_intervals),
        'Current_Vel_(m/s)': velocities,
        'Displacement_(m)': displacements
    }
    
    # Convert to a DataFrame for structured analytical layout
    df = pd.DataFrame(motion_data)
    
    print("\n[SUCCESS] Kinematics motion data compiled successfully:\n")
    print(df.to_string(index=False))
    print("==================================================")

if __name__ == "__main__":
    simulate_kinematics()

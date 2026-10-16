
# B4: Continuous Discharge Analysis

voltages = [12.6, 12.5, 12.5, 12.3, 12.1, 11.9, 12.0, 11.8, 11.6, 11.5, 11.5, 11.2]
 
current_start = 0   
current_length = 1  
best_start = 0
best_length = 1
 
for i in range(1, len(voltages)):
    if voltages[i] < voltages[i - 1]:
        current_length += 1
    else:
        current_start = i
        current_length = 1

    if current_length > best_length:
        best_length = current_length
        best_start = current_start
 
started_at = voltages[best_start]
ended_at = voltages[best_start + best_length - 1]
 
print("Longest continuous drop:", best_length, "minutes")
print("Started at:", started_at, "V")
print("Ended at:", ended_at, "V")

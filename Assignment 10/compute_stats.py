import sys
import statistics

#Takes The Values From The Data Coming From Standard Input And Computes Basic Statistics That Are Read In 
#1) Average value
#2) Minimum value
#3) Maximum value
#4) Median value
def my_stats():
    values = []
    for line in sys.stdin:
        try:
            value = float(line.strip())
            values.append(value)
        except ValueError:
            continue
    
    if not values:
        print("No Valid Data Found")
        return

    min_val = min(values)
    max_val = max(values)
    avg_val = sum(values) / len(values)
    median_val = statistics.median(values)

    print(f"Min: {min_val}, Max: {max_val}, Average: {avg_val}, Median: {median_val}")

if __name__ == "__main__":
    my_stats()

import sys
# sys.stdout = open('./input.txt', 'w')
file = open('./day-2/input.txt', 'r')
# file = open('./day-2/test.txt', 'r')
reports = file.readlines()

def is_safe(levels):
    
    # Check if levels are either all increasing or all decreasing
    increasing = all(levels[i] < levels[i + 1] for i in range(len(levels) - 1))
    decreasing = all(levels[i] > levels[i + 1] for i in range(len(levels) - 1))
    
    # Check if any two adjacent levels differ by at least one and at most three
    valid_difference = all(1 <= abs(levels[i] - levels[i + 1]) <= 3 for i in range(len(levels) - 1))

    return (increasing or decreasing) and valid_difference
    

# Part 1 - Count the number of safe reports
safe_reports = 0

for report in reports:
    levels = list(map(int, report.split()))
    if is_safe(levels):
        safe_reports += 1

print(safe_reports)

# Part 2 
safe_reports = 0

def is_report_safe(report):
    levels = list(map(int, report.split()))
    
    if is_safe(levels):
        return True
    
    # Check if removing one level makes the report safe
    for i in range(len(levels)):
        if is_safe(levels[:i] + levels[i+1:]):
            return True
    
    return False

for report in reports:
    if is_report_safe(report):
        safe_reports += 1

print(safe_reports)

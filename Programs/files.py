import os, os.path
import datetime

def find_details(DIR, files, recursion):
    details = []
    for name in os.listdir(DIR):
        if os.path.isfile(os.path.join(DIR, name)):
            details.extend(list(os.path.splitext(os.path.join(DIR, name))))
            file_name = os.path.basename(name)
            stat = os.stat(os.path.join(DIR, name))
            dates = [stat.st_atime, stat.st_mtime, stat.st_birthtime]
            dates = [datetime.datetime.fromtimestamp(date) for date in dates]
            size = stat.st_size
            details.append(file_name)
            details.extend(dates)
            details.append(size)
            files[name] = details
            details = []
        elif recursion == 'Y' or recursion == 'y':
            find_details(os.path.join(DIR, name), files, recursion)
        else:
            pass
    return files

def number_of_file(files):
    number_of_files = len(files)
    return number_of_files

def number_of_extension(files, extension):
    number_of_extension = len([file for file in files if files[file][1] == extension])
    return number_of_extension

def size(files):
    if not bool(files):
        raise NameError
    largest_size = -1
    smallest_size = float('inf')
    largest_file = ''
    largest_location = ''
    smallest_file = ''
    smallest_location = ''
    for file in files:
        if files[file][6] > largest_size:
            largest_file = files[file][2]
            largest_location = files[file][0]
            largest_size = files[file][6]
        if files[file][6] < smallest_size:
            smallest_file = files[file][2]
            smallest_location = files[file][0]
            smallest_size = files[file][6]
    largest = [largest_file, largest_location, largest_size]
    smallest = [smallest_file, smallest_location, smallest_size]
    return (largest, smallest)

def modify(files):
    if not bool(files):
        raise NameError
    recent_modified_time = datetime.datetime.min
    recent_modified_name = ''
    recent_modified_location = ''
    for file in files:
        if files[file][4] > recent_modified_time:
            recent_modified_time = files[file][4]
            recent_modified_location = files[file][0]
            recent_modified_name = files[file][2]
    return (recent_modified_name, recent_modified_location, recent_modified_time)
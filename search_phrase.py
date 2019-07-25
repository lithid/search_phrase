import os
import sys

if __name__ == "__main__":
    phrase = sys.argv[1]
    dir_collection = []
    file_name_collection = []

    collection = {}

    for root, dirs, files in os.walk(os.getcwd()):
        for dir in dirs:
            j = os.path.join(root, dir)
            if phrase in dir.lower():
                if "/." not in j:
                    dir_collection.append(j)

        for file in files:
            j = os.path.join(root, file)
            if phrase in file.lower():
                if "/." not in j:
                    file_name_collection.append(j)

            if os.stat(j).st_size == 0:
                continue
            with open(j, 'r', encoding='latin-1') as f:
                file_collection = []
                line = f.readline()
                count = 1
                while line:
                    if phrase in line:
                        if "/." not in j:
                            file_collection.append("Line: (%s) %s" % (str(count), line.strip()))
                    line = f.readline()
                    count += 1

            if len(file_collection) > 0:
                collection[j] = file_collection

    if len(dir_collection) > 0:
        print("##############################")
        print("Dir names:")
        print("##############################")
        for dir in dir_collection:
            print(dir)

    if len(file_name_collection) > 0:
        print("\n##############################")
        print("File names:")
        print("##############################")
        for file_name in file_name_collection:
            print(file_name)

    if len(collection) > 0:
        print("\n##############################")
        print("Files found phrase:")
        print("##############################")
        for collect_file in collection:
            print(collect_file + ":")
            for cf in collection[collect_file]:
                print(cf)
            print("")

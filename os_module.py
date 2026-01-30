import os

def create_new_dir(new_dir):
    current_dir = os.getcwd()

    try:
        path = os.path.join(current_dir, new_dir)
        os.mkdir(path)
        os.chdir(path)
        status = True
        print(f"Dir created at {path}")
    except:
        print(f"Seems like directory named '{new_dir}' already exist")
        status = False
    finally:
        return status
    

def create_file(file_name):
    try:
        file = open(file_name, "w")
        print("File created!")
    except:
        print("Something went wrong!!")
    finally:
        file.close()



dir = input("Enter the name of directory you want to create: ")
creation_status = create_new_dir(dir)

while(creation_status == False):
    dir = input("Enter some other name of the directory: ")
    creation_status = create_new_dir(dir)
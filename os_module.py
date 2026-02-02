import os

def create_new_dir(new_dir):
    '''
    Create a new directory
    @return: true if directory id successfully created
    @return: false in case of error
    '''
    current_dir = os.getcwd()

    try:
        path = os.path.join(current_dir, new_dir)
        os.mkdir(path)
        os.chdir(path)       # change the current path to new dir
        status = True        # dir created successfully
        print(f"Dir created at {path}")
    except:
        print(f"Seems like directory named '{new_dir}' already exist")
        status = False        # dir with the same name already exist
    finally:
        return status
    

def create_file(file_name):
    '''
    Create new empty file
    '''
    try:
        file = open(file_name, "w")
        print("File created!")
    except:
        print("Something went wrong!!")
    finally:
        file.close()



dir = input("Enter the name of directory you want to create: ")            # taking directory name from the user
creation_status = create_new_dir(dir)                                      # if status is true then dir is created

while(creation_status == False):                                           # if status is false
    dir = input("Enter some other name of the directory: ")                # ask user to enter new unique name of directory
    creation_status = create_new_dir(dir)

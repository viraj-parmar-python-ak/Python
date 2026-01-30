def create_file(file_name):
    try:
        file = open(file_name, "w")
        print("File created!")
    except:
        print("Something went wrong!!")
    finally:
        file.close()



def create_multiple_files(num):
    for i in range(num):
        try:
            file = open(f"new_file{i}.txt", "w")
        except:
            print("Something went wrong!!")
            print(f"{i} files created!")
            break
        finally:
            file.close()
    print(f"{num} files created!")


def append_file(file_name, content):
    try:
        file = open(file_name, "a")
        file.writelines(content)
        print("Content updated in the file!")
    except:
        print("Something went wrong!!")
    finally:
        file.close()

def add_content_to_file(file_name, content):  
    try:
        file = open(file_name, "w")
        file.writelines(content)
        print("Content added to the file!")
    except:
        print("Something went wrong!!")
    finally:
        file.close()


def read_file(file_name):
    try:
        file = open(file_name, "r")
        print(file.read())
    except:
        print("Something went wrong!!")
    finally:
        file.close()



create_file("Viraj")
create_multiple_files(2)

lines = ["This is first line\n", "this is second line\n", "this is third line\n", "this is the last line\n"]
add_content_to_file("Viraj.txt", lines)

read_file("Viraj.txt")

append_file("new_file0.txt", lines)
append_file("new_file0.txt", lines)
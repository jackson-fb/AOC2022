from read_input import read_input


class File:
    def __init__(self, name, filesize):
        self.name = name
        self.filesize = filesize


class Directory:
    def __init__(self, parent, name):
        self.name = name
        self.children = {}
        self.files = {}
        self.parent = parent
        self.size = 0

    def add_file(self, file):
        self.files[file.name] = file

    def add_child(self, directory_name):
        self.children[directory_name] = Directory(self, directory_name)


def print_dir(directory, numIndents):
    indents = "" + numIndents * "\t"
    numIndents += 1
    indents_plusone = "" + numIndents * "\t"
    print(indents + "\\" + directory.name)

    for subdirectory in directory.children.values():
        print_dir(subdirectory, numIndents)

    for file in directory.files.values():
        print(f"{indents}\t{file.name} {file.filesize}")


def get_dir_size(directory):
    size = 0
    # calculate size
    for file in directory.files.values():
        size += file.filesize

    for subdirectory in directory.children.values():
        size += get_dir_size(subdirectory)
    directory.size = size
    return size


def get_subdirs_under_100000(directory):
    subdirs = []
    for subdir in directory.children.values():
        subdirs += get_subdirs_under_100000(subdir)
        if subdir.size < 100000:
            subdirs.append(subdir)
    return subdirs


def get_subdir_to_delete(directory, minimum):
    #get smallest that's above x
    smallest = directory
    for subdir in directory.children.values():
        newdir = get_subdir_to_delete(subdir, minimum)
        if newdir.size < smallest.size and newdir.size > minimum:
            smallest = newdir
    return smallest


if __name__ == '__main__':
    lines = read_input('../day7/input.txt')
    split_lines = [line.split(' ') for line in lines]

    home = Directory(None, "/")
    currentDir = home
    del split_lines[0]
    for line in split_lines:
        if line[0] == "$":
            if line[1] == "cd":
                if line[2] == "..":
                    currentDir = currentDir.parent
                elif currentDir.children[line[2]] is not None:
                    currentDir = currentDir.children[line[2]]
                else:
                    print("Attempted to go to unknown directory!")
            elif line[1] == "ls":
                print("ls")
            else:
                print(f"unknown command! {line}")

        elif line[0] == "dir":
            currentDir.add_child(line[1])

        elif line[0].isnumeric():
            currentDir.add_file(File(line[1], int(line[0])))

    print_dir(home, 0)
    print("done building tree!")
    print("calculating directory sizes")
    print(get_dir_size(home))
    small_subdirs = get_subdirs_under_100000(home)
    total = 0

    empty_space = 70000000 - home.size
    free_space_required = 30000000 - empty_space

    print(f"Need 30000000 free, current free space: {empty_space}, need {free_space_required} more")
    smallest_deletion_target = home
    for subdir in small_subdirs:
        total += subdir.size


    print(f"p1 total: {total}")
    smallest_deletion_target = get_subdir_to_delete(home, free_space_required)
    print(f"Directory to delete identified: {smallest_deletion_target.name}: {smallest_deletion_target.size}")

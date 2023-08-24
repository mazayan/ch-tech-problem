import os


class File:
    """A class to represent a File and operations performed on said file"""

    def __init__(self, file_path) -> None:
        """Construct file path attribute for the File object"""
        self.file_path = file_path

    def is_directory(self) -> bool:
        """Check if inputted file path is a directory"""
        if os.path.isdir(self.file_path):
            return True
        return False

    def file_exists(self) -> bool:
        """Check if file path exists"""
        if os.path.exists(self.file_path):
            return True
        return False

    @staticmethod
    def sort_dict_values_desc(dictionary) -> dict:
        """
        Takes Dictionary and sorts entries based on values in descending order
        In the lambda, the value is extracted and sorted from the tuple [(key,value),..]
        """
        # takes tuple  from dic.items() and extracts the value
        return dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))

    @staticmethod
    def get_max_values(sorted_dic, max_values) -> list:
        """Returns top values specified in max_values from the sorted dictionary"""
        return list(sorted_dic)[:max_values]

    def file_iterator(self) -> dict:
        """Iterates over given file and creates a dictionary of valid key value pairs"""
        dic = {}
        with open(self.file_path) as f:
            for line in f:
                try:
                    (key, val) = line.split()
                    if "http" not in key:
                        raise ValueError
                    dic[key] = int(val)
                except ValueError:
                    print(f"Unable to process line: {line}")
            f.close()
        return dic


def main():
    """
    Parses through a file in the format <url><white space><long value> and
    returns a given number of URLs where the long value is in descending order
    """
    max_values = 10
    file_path = File(input("Please enter the file path\n"))
    if not file_path.is_directory() and file_path.file_exists():
        dic = file_path.file_iterator()
        if dic == {}:
            print("File is empty. No large values to return")
        else:
            file_path.sort_dict_values_desc(dic)
            sorted_dic = file_path.sort_dict_values_desc(dic)
            urls = file_path.get_max_values(sorted_dic, max_values)
            for entry in urls:
                print(entry)
    else:
        print("Unable to locate the file: ", file_path.file_path)


if __name__ == "__main__":
    main()

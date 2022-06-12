import sys, os, random, string, uuid
import py7zr

class RomCompressor:

    def __init__(self, input_dir, input_file_extension, output_dir, output_file_extension):
        self.input_dir = input_dir
        self.input_file_extension = input_file_extension
        self.output_dir = output_dir
        self.output_file_extension = output_file_extension


    def __gen_rand_uuid(self):
        return uuid.uuid4().hex[-10:]

    
    def __is_each_path_valid(self, path_list):
        ''''''
        #is_path_invalid_lambda = lambda path : !os.path.isdir(path)
        is_each_path_valid = False

        print("path_list: ", path_list)

       
        '''
        for path in path_list:
            if os.path.isdir(path):
                print("%s is a valid path!" % path)
            else:
                print("%s is an invalid path!" % path)
        '''
            

        if path_list:
            valid_paths = list(filter(lambda path : os.path.isdir(path), path_list))
            is_each_path_valid = len(path_list) == len(valid_paths)

        return is_each_path_valid

    
    def __compress_files(self, input_dir, output_dir):

        rand_prefix = self.__gen_rand_uuid()

        output_prefix = ''.join(("compressed-", rand_prefix[-10:]))
        output_root_path = os.path.join(output_dir, output_prefix) 
        print("TODO - mkdir output root path: %s" % output_root_path)

        print("making directory %s" % output_root_path)
        os.makedirs(output_root_path, exist_ok=True)

        if os.path.isdir(output_root_path):

            for root, dirs, files in os.walk(input_dir):
                relative_path = os.path.relpath(root, input_dir)
                output_relative_path = os.path.join(output_root_path, relative_path)
            
                print("making directory %s" % output_relative_path)
                os.makedirs(output_relative_path, exist_ok=True)
                
                if os.path.isdir(output_relative_path): 
                    for file in files:
                        file_tuple = os.path.splitext(file)
                        file_name = file_tuple[0]
                        file_ext = file_tuple[1]

                        if file_ext and self.input_file_extension == file_ext:
                            #print(file)
                            #print(os.path.join(root, file))

                            output_file = f'{file_name}{self.output_file_extension}'
                            print("output file: %s" % os.path.join(output_relative_path, output_file))


    def start_compressor(self, custom_input_dir=None, custom_output_dir=None):
        final_input_dir = ""
        final_output_dir = ""

        # support overriding the default input/output locations
        if None != custom_input_dir:
            final_input_dir = custom_input_dir 
        else:
            final_input_dir = self.input_dir 

        if None != custom_output_dir:
            final_output_dir = custom_output_dir 
        else:
            final_output_dir = self.output_dir

        if self.__is_each_path_valid([final_input_dir, final_output_dir]):
            self.__compress_files(final_input_dir, final_output_dir)
            print("All paths are valid!")
        else:
            sys.exit("Error: one or more paths are invalid.")



def print_usage():
    print('\n'.join(('usage: romcom.py input_dir input_file_extension output_dir',
        'example usage: romcom.py /home/user/roms ".nes" /mnt/backup/nes/roms',
        'all arguments are required')))


def main():
    print("Welcome to RomCom!")
    print_usage()
   
    if len(sys.argv) != 4:
        #print_usage()
        sys.exit("Error: invalid arguments")


    input_dir = sys.argv[1]
    input_file_extension = sys.argv[2]
    output_dir = sys.argv[3]
    output_file_extension = ".7z"

    compressor = RomCompressor(input_dir, input_file_extension, output_dir, output_file_extension)
    compressor.start_compressor()

    #output_directory = os.path.join(output_root,

    #print(traverseDirectory(sourceDirectory, output_directory))

if __name__ == '__main__':
    main()

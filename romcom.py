import sys, os, random, string, uuid
import py7zr

class RomCompressor:

    def __init__(self, input_dir, output_dir):
        self.input_dir = input_dir
        self.output_dir = output_dir


    def __compress_files(self, input_dir, output_dir):

        rand_prefix = self.__gen_rand_uuid()

        output_prefix = ''.join(("compressed-", rand_prefix[-10:]))
        print("TODO - mkdir output root path: %s" % os.path.join(output_dir, output_prefix))

        for root, dirs, files in os.walk(input_dir):
            for file in files:
                print(os.path.join(root, file))


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
    print('\n'.join(("usage: romcom.py input_dir output_dir", 
        "'input_dir' and 'output_dir' are required")))
    #print(usage)


def main():
    print("Welcome to RomCom!")
   
    if len(sys.argv) != 3:
        print_usage()
        sys.exit()


    source_directory = sys.argv[1]
    output_directory = sys.argv[2]

    compressor = RomCompressor(source_directory, output_directory)
    compressor.start_compressor()

    #output_directory = os.path.join(output_root,

    #print(traverseDirectory(sourceDirectory, output_directory))

if __name__ == '__main__':
    main()

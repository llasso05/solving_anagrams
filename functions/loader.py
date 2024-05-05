import sys

# reading dict function 
def read_dictionary(file_name):
    try:
        with open(file=file_name) as in_file:
            # loading text
            loaded_text = in_file.read().strip().split('\n')
            # lower casing 
            loaded_text = [x.lower() for x in loaded_text]
            return loaded_text
    except IOError as e:
        print(f'{e} \n error opening {in_file}. terminating program',
              file = sys.stderr)
        sys.exit(1)
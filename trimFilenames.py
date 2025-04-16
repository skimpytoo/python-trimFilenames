import functools
import os
import pprint
import sys
import getopt
import shutil
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('trimFilenames.log'),
        logging.StreamHandler()
    ]
)

USAGE = "trimFilenames.py -i <inputDir> -t <Numner of trim chars:7> -d"

def trim_files(input_dir, trim_num, dryrun):
    # Use os.path.join() for all path operations to ensure cross-platform compatibility
    logging.info(f"Starting file trimming process in directory: {input_dir}")
    logging.info(f"Trim settings: characters={trim_num}, dryrun={dryrun}")
    
    files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]
    logging.info(f"Found {len(files)} files to process")
    
    for file in files:
        trimmed_name = file[trim_num:]
        if not dryrun:
            try:
                trimmed_full_path = os.path.join(input_dir, trimmed_name)
                orig_full_path = os.path.join(input_dir, file)
                os.rename(orig_full_path, trimmed_full_path)
                logging.info(f"Successfully renamed: {file} -> {trimmed_name}")
            except Exception as e:
                logging.error(f"Error renaming {file}: {str(e)}")
        else:
            logging.info(f"Dry run: Would rename {file} -> {trimmed_name}")
    return

def main(argv):
    input_dir = ''
    trim_num = 7
    dryrun = False

    try:
        opts, args = getopt.getopt(argv, "hi:t:d", ["iDir=", "trim=", "dryrun"])
    except getopt.GetoptError:
        logging.error("Invalid command line arguments")
        logging.error(USAGE)
        sys.exit(2)
        
    for opt, arg in opts:
        if opt == '-h':
            logging.info(USAGE)
            sys.exit()
        elif opt in ("-i", "--iDir"):
            input_dir = arg
        elif opt in ("-d", "--dryrun"):
            dryrun = True
        elif opt in ("-t", "--trim"):
            trim_num = int(arg)
            
    logging.info(f"Input directory: {input_dir}")
    logging.info(f"Number of chars to trim: {trim_num}")
    logging.info(f"Dry run mode: {dryrun}")

    if input_dir == '':
        logging.error("Input directory (-i) is required")
        sys.exit(2)

    if not os.path.exists(input_dir):
        logging.error(f"Input directory does not exist: {input_dir}")
        sys.exit(2)

    trim_files(input_dir, trim_num, dryrun)

if __name__ == "__main__":
    main(sys.argv[1:])

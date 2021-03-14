import argparse
import glob
import logging
import fileinput
import sys


# Init and configure logger
logger = logging.getLogger('multifiles_replace')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

fh = logging.FileHandler("multi_replace.log")
fh.setFormatter(formatter)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)


# Reading command line agruments
logger.debug('Reading command line arguments')

parser = argparse.ArgumentParser(description='Search and replace a string in multiple files',
                                 usage='py %(prog)s -s kek -r pek -f D:\work\*.xml [-d]')

parser.add_argument('-s', '--search',  
                    required=True,
                    help='Line which will be replaced')

parser.add_argument('-r', '--replace',
                    required=True, 
                    help='Line to replace by')

parser.add_argument('-f', '--files',
                    required=True,
                    nargs='+',
                    help='File list to perform search and replace. Wildcards are allowed.')

parser.add_argument('-d', '--dry', 
                    action='store_true',
                    default=False,
                    help='Dry run. If option is set tool performs only search w/o file modification')

args = parser.parse_args()

logger.info('===================== Replacement parameters =====================')
logger.info('Search string: %s', args.search)
logger.info('Replace string: %s', args.replace)
logger.info('Dry run: %s', args.dry)

# args.files contains a raw user input, we need to valiadate it and resolve wildcards in paths
logger.debug('Raw file list: %s', args.files)
logger.debug('Starting validation of file list')

resolved_files = []

for file in args.files:
    logger.debug('Raw file argument: %s', file)
    file_list = glob.glob(file)
    logger.debug('glob result: %s', file_list)
    resolved_files += file_list

resolved_files.sort(reverse=False)

unique_files = []
for item in resolved_files:
    if item in unique_files:
        continue
    unique_files.append(item)

logger.debug('File list validation is finished, there is a final list')

for file in unique_files:
    logger.debug('File to process: %s', file)

if args.dry:
    logger.info('================== Dry run, perform search only ==================')
else:
    logger.info('====================== Perform replacement ======================')

stat_replaces = 0
stat_modified_files = []

for line in fileinput.input(files=unique_files, inplace=not args.dry):
    entr_count = line.count(args.search)

    if entr_count > 0:
        logger.debug('Entry found in: %s, line No: %d, cound: %d', fileinput.filename(), fileinput.filelineno(), entr_count)
        stat_replaces += entr_count
        stat_modified_files.append(fileinput.filename())
        logger.debug('Line before replace: %s', line.strip())
        line = line.replace(args.search, args.replace, entr_count)
        logger.debug('Line after replace: %s', line.strip())
        if not args.dry:
            logger.info('Modified file: %s, line %d', fileinput.filename(), fileinput.filelineno())
            sys.stdout.write(line)

stat_unique_modified_files = set(stat_modified_files)

logger.info('============================ Summary =============================\n')
logger.info('Total number of replacements: %d', stat_replaces)
logger.info('Number of modified files: %d\n', len(stat_unique_modified_files))
logger.info('============================ Finish =============================')
logger.info('Please, find log file for exact list of replacements')

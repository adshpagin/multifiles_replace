# Multi-files Replace tool
A simple script which performs search-and-replace in a group of files.
Basically, tool does the same as shell script like:

    sed -i 's/kek/pek/g' /home/*.xml

Tool is devoted to user which have no access to shell commands like `sed` and `awk`. Also tool may have more verbosity then regular shell scripts.
## Features
* Matches a specified pattern to each line of the file and if matched replaces it with specified string
* Work with a list of files, so several files can be processed by one execution
* Counts a number of matches/replacements. In case of several files are processed the tool counts sum of replacements by all files
* Counts a number of modifed files
* Dry run mode for search only without files modification
* Verbose log which contains lines before and after replacement for debug
## Installation
* Download file: https://github.com/adshpagin/multifiles_replace/blob/master/multifiles_replace.py
* Clone repo
## Execution
The only tool script is `multifiles_replace.py`. It should be executed as a regular Python script. 
### Parameters

    -s, --search    Search pattern. Regexp are currenlty unsupported.
    -r, --replace   A string to replace matched search pattern.
    -f, --files     A white spaces separated list of files to perform search and replace. Wildcards are supported.
    -d, --dry       Execute tool in dry run mode which performs only search without actual replacement and file modification.

See next section for execution examples.
## Usage example
Displays a help message

    $ py multifiles_replace.py -h

Searches pattern `kek` and replaces it by string `pek` in all xml files in "D:\Work" directory.

    $ py multifiles_replace.py -s kek -r pek -f D:\Work\*.xml
    
Searches pattern `kek` and replaces it by string `pek` in three specified files located in different directories.

    $ py multifiles_replace.py -s kek -r pek -f D:\Work\config.xml D:\Temp\settings.yaml D:\node.json

Dry run mode. Searches pattern `kek` in all xml files in "D:\Work" directory, but do not replace anything. Files are not modified.

    $ py multifiles_replace.py -s kek -r pek -f D:\Work\*.xml -d

## Logs
Log file with a name `multi_replace.log` is written in the current directory where the tool is executed.
## Limitations
* Regexp are currently unsupported
* Alfa version, tested manually and roughly

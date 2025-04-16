# trimFilenames

A Python utility tool that removes a specified number of characters from the beginning of filenames in a given directory.

## Features

- Removes specified number of characters from filenames
- Cross-platform path handling
- Dry run mode for testing
- Comprehensive logging
- Unit test coverage
- Command-line interface

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/trimFilenames.git
cd trimFilenames
```

2. Ensure Python 3.x is installed on your system

## Usage

```bash
python trimFilenames.py -i <inputDir> -t <trim_chars> -d
```

### Arguments

- `-i, --iDir`: Input directory (required)
  - Specify the directory containing files to be renamed
- `-t, --trim`: Number of characters to trim (optional, default: 7)
  - Specify how many characters to remove from the beginning of each filename
- `-d, --dryrun`: Dry run mode (optional)
  - When enabled, shows what would be renamed without making actual changes

### Examples

1. Basic usage:
```bash
python trimFilenames.py -i ./myfiles
```

2. Specify trim length:
```bash
python trimFilenames.py -i ./myfiles -t 5
```

3. Dry run mode:
```bash
python trimFilenames.py -i ./myfiles -d
```

## Logging

The tool generates detailed logs in `trimFilenames.log` with:
- Timestamps
- Operation details
- Success/failure information
- Error messages

## Testing

Run the test suite:
```bash
python -m unittest test_trimFilenames.py
```

Tests include:
- Dry run functionality
- Actual file renaming
- Different trim lengths
- Empty directory handling

Test logs are written to `test_trimFilenames.log`.

## Example

Input files:
```
0100 - Document1.txt
0100 - Document2.txt
0100 - Document3.txt
```

After running with default settings (trim=7):
```
Document1.txt
Document2.txt
Document3.txt
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
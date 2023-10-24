# Async File Processing with Pydantic

This repository showcases a quick and dirty asynchronous approach to processing large text files, leveraging the power of Python's `asyncio` and `aiofiles` libraries. The primary objective is to efficiently read, process, and write data, and in this specific example, the code takes a newline-delimited text file of users, processes each line with simulated delays, validates and transforms the data using `Pydantic`, and then writes the processed data to a new file.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Features

- **Asynchronous File IO**: Uses `aiofiles` to perform non-blocking file read and write operations.
- **Data Validation**: Utilizes `Pydantic` for data validation and transformation.
- **Progress Tracking**: Incorporates `tqdm` for visual progress tracking.
- **Efficient Batching**: Processes data in chunks for optimized performance.
  
## Installation

1. Ensure you have Python 3.7 or newer installed.
2. Clone this repository: git clone https://github.com/peelnpunch/async-file-processing.git
3. Navigate to the project directory and install required packages: `cd async-file-processing` and `pip install -r requirements.tx`



## Usage

1. Place your newline-delimited text file named `users.txt` in the root directory.
2. Run the main script:
3. Check the `processed_users.txt` for the processed output.

## License

This project is open source and available under the [MIT License](LICENSE).



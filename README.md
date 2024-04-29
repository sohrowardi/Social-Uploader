# Social Media Content Uploader

## Overview
This project aims to automate the process of uploading content to various social media platforms. It consists of Python scripts that create folders for each platform and upload content to them using respective API keys.

## Directory Structure
- **config.json**: Contains API keys for different social media platforms.
- **create_folders.py**: Python script to create folders for each platform.
- **upload_content.py**: Python script to upload content to respective social media platforms.
- **README.md**: This file, providing an overview of the project.

## Usage
1. Clone the repository to your local machine.
2. Update the `config.json` file with your API keys for each social media platform.
3. Run the `1_create_folders.py` script to create folders for each platform.
4. Place your content (images, videos, etc.) in the respective folders.
5. Run the `2_write_tags.py` script to generate a `tags.json` file with default titles and empty tags. You can then manually edit this file to add tags for each file.
6. Run the `3_upload_content.py` script to upload the content to the respective social media platforms.

Note: Make sure to follow the API usage guidelines of each social media platform and use the tool responsibly.


## Contributing
Contributions to improve and extend this project are welcome! Feel free to fork the repository, make your changes, and submit a pull request.

## Disclaimer
This project is a personal endeavor and not affiliated with any social media platform. Use it responsibly and in accordance with the terms of service of each platform.

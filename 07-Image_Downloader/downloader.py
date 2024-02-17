import os
import requests


def get_extension(image_url: str) -> str | None:
    # Create a list of popular extensions to check for
    extensions: list[str] = ['.png', '.jpg', '.jpeg', '.gif', '.svg']

    # Check that the extension exists inside the URL
    for ext in extensions:
        if ext in image_url:
            return ext


def download_image(image_url: str, name: str):
    """Download the image from any given url"""

    # Attempt to get the correct image extension from an url
    if ext := get_extension(image_url):
        # Create the full path
        full_path = os.path.join(os.getcwd(), f'{name}{ext}')
    else:
        raise Exception('Image extension could not be located...')

    # Check if the name already exists
    if os.path.isfile(full_path):
        raise Exception('File name already exists...')

    try:
        # Get the image as bytes and write it locally to our computer
        image_content: bytes = requests.get(image_url).content
        with open(full_path, 'wb') as handler:
            handler.write(image_content)
            print(f'Downloaded: "{full_path}" successfully!')
    except Exception as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    # Get the user input for the download
    input_url: str = input('Enter a url: ')
    input_name: str = input('What would you like to name it?: ')

    # Download the image
    print('Downloading...')
    download_image(input_url, name=input_name)

import os
import requests


def get_extension(image_url: str) -> str | None:
    """Get the file extension from the image URL."""
    extensions: list[str] = ['.png', '.jpg', '.jpeg', '.gif', '.svg']

    for ext in extensions:
        if ext in image_url:
            return ext

    return None


def download_image(image_url: str, name: str):
    """Download the image from the given URL and save it with the provided name."""
    try:
        # Attempt to get the correct image extension from the URL
        ext = get_extension(image_url)
        if not ext:
            raise Exception('Image extension could not be located.')

        # Create the full path
        full_path = os.path.join(os.getcwd(), f'{name}{ext}')

        # Check if the file already exists
        if os.path.isfile(full_path):
            raise Exception('File name already exists.')

        # Get the image as bytes and write it locally to our computer
        image_content = requests.get(image_url).content
        with open(full_path, 'wb') as handler:
            handler.write(image_content)
            print(f'Downloaded: "{full_path}" successfully!')

    except requests.exceptions.RequestException as e:
        print(f'Error downloading image: {e}')

    except Exception as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    try:
        # Get the user input for the download
        input_url = input('Enter a URL: ')
        input_name = input('What would you like to name it?: ')

        # Download the image
        print('Downloading...')
        download_image(input_url, name=input_name)

    except KeyboardInterrupt:
        print('\nDownload process interrupted by the user.')

    except Exception as e:
        print(f'An unexpected error occurred: {e}')

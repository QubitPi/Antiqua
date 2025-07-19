import requests


def get_book_txt_by_url(url: str):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text

    except requests.exceptions.RequestException as e:
        print(f"Error retrieving the file: {e}")


if __name__ == "__main__":
    print(get_book_txt_by_url("https://www.gutenberg.org/files/6342/6342-8.txt"))

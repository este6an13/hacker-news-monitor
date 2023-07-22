# Hacker News Monitor

This program uses the [Official Hacker News API](https://github.com/HackerNews/API). The objective of the program is to print to console the title and the URL of the top and best HN stories that have a score greater than a given threshold. This threshold can be modified by the user. By default is set to `50`. The stories are printed only once to console and this is guaranteed by the `ids.txt` file which contains the IDs of already printed stories. The `ids.txt` file won't grow in size indefinitely, since the program removes old stories IDs. An extra feature was added so that the user can define a set of keywords they might be interested in. The program will print to console those items containing those keywords in the title or in the URL, without taking into account the defined threshold.

## Project Structure

The project consists of the following files:

- `main.py`: Python script for getting the top and best HN stories.

### Input Data:

- `ids.txt`: Text file containing the IDs of already printed stores.

## Usage

1. Run the `main.py` script.

## Dockerization

```bash
docker build -t hacker_news_monitor .
docker run --rm hacker_news_monitor
```

## Contributing

Contributions to this project are welcome! Feel free to fork the repository, make changes, and submit pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

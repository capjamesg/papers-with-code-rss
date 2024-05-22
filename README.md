# Papers with Code RSS Feed

This tool generates RSS feeds for task pages on [Papers with Code](https://paperswithcode.com).

There is a hosted version of this tool available at `https://jamesg.blog/pwc/?url=`, which you can use to make requests for task pages. The url structure is:

```
https://jamesg.blog/pwc/?url=/task/<task_name>
```

Responses are cached for 15 minutes.

## How to Set Up Locally

To set up this tool locally, first clone this repository and install the required dependencies:

```
git clone https://github.com/capjamesg/papers-with-code-rss
cd papers-with-code-rss/
pip3 install -r requirements.txt
```

You can then run the application using the following code:

```
python3 app.py
```

The tool will run on `localhost:5000`.

## License

This project is licensed under an [MIT license](LICENSE).

## Contributing

Seen a bug? Have a feature to add? Feel free to file an issue or a PR!

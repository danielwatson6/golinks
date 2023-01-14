# golinks

**TL;DR**: Type `go + [tab]` in your browser, and type your custom shortcuts for any link. If it doesn't exist, you will be redirected to a page to create it.

## Credit

I basically stole everything from [this blog post](https://iafisher.com/blog/2020/10/golinks).

## Install local server dependencies

```
virtualenv .env
source .env/bin/activate
pip install -r requirements.txt
```

## Install chrome extension

- Go to `chrome://extensions/`
- Press the "load unpacked" button and add the `chrome_extension` dir in this repo

**TODO(danielwatson6)** need to update `manifest.json` to `"manifest_version": 3`

## Workflow

Start the server with this command:
```
./goserver.sh
```

This will launch a daemon, so feel free to close the shell. To stop the daemon, `./goserver.sh` will create a file called `PIDFILE` containing the pid of the daemon. So you can stop it with `kill -9 $(cat PIDFILE)`, for example.

To not type `http://` or be redirected to Google Search:
- Go to Chrome Settings > Search Engine > Site Search
- Add a search engine (name it `golinks`, with shortcut `go`, and with this URL: `http://localhost:5000/go/%s`)
- Now type `go` and press tab to navigate :) go-tab isn't quite go-slash, but it's good enough!

**TODO(danielwatson6)** add basic UI and endpoints for listing/editing/deleting golinks. Right now, this can be done manually by editing the `links.json` file.

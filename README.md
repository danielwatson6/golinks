# golinks

Personal go/ links

## Credit

I basically stole everything from [this blog post](https://iafisher.com/blog/2020/10/golinks).

## Install local server dependencies

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

**TODO(danielwatson6)** add daemon feature

## Install chrome extension

- Go to `chrome://extensions/`
- Press the "load unpacked" button and add the `chrome_extension` dir in this repo

**TODO(danielwatson6)** need to update `manifest.json` to `"manifest_version": 3`

## Workflow

Start the server with this command:
```
./goserver.sh
```

To not type `http://` or be redirected to Google Search:
- Go to Chrome Settings > Search Engine > Site Search
- Add a search engine (name it `golinks`, with shortcut `go`, and with this URL: `http://localhost:5000/go/%s`)
- Now type `go` and press tab to navigate :) go-tab isn't quite go-slash, but it's good enough!

## Adding new links

If a golink is not found, the 404 page will allow the user to register it.

**TODO(danielwatson6)** add basic UI and endpoints for listing/editing/deleting golinks

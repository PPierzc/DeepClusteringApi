# DeepClusteringApi
An API serving the deep clustering model

A simple flask server that is used to serve the model compiled in Keras.

## Run
`python3 app.py`

starts a server on `localhost:3000`.

## API

| Method | Path | Data | Response |
|--------|------|------|----------|
| POST   | /    | A Nx67x67 matrix with N ICA topographies| Array of cluster Ids |

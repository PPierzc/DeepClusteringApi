# DeepClusteringApi
An API serving the deep clustering model

A simple flask server that is used to serve the model compiled in Keras.

## Install
`git clone https://github.com/PPierzc/DeepClusteringApi.git`

`pip3 install -r requirements`

## Run
`python3 app.py`

starts a server on `localhost:3000`.

## API

| Method | Path | Data | Response |
|--------|------|------|----------|
| POST   | /    | A Nx67x67 matrix with N ICA topographies| Array of cluster Ids |

## Heroku Usage
The repository is ready to be launched in heroku. Simply fork the project and link it to heroku.

## Things to add
* Training clustering model
* Display clusters
* Auto-artefact detection
* Display topography cluster relation

## Contribution
Fork the repositiory, create a pull request with a full description of changes added.

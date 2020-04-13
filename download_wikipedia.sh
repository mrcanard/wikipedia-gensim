#!/bin/bash

LATEST_URL_DUMP="https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2"

OUTPUT_FILENAME="DATA/IN/$(basename ${LATEST_URL_DUMP})"

# Test que le fichier n'est pas déjà présent afin de ne pas faire de
# travail de téléchargement inutile
#  -L, --location      Follow redirects
#  -o, --output <file> Write to file instead of stdout
#  -C, --continue-at <offset> Resumed transfer offset
curl -L -o ${OUTPUT_FILENAME} -C - ${LATEST_URL_DUMP}


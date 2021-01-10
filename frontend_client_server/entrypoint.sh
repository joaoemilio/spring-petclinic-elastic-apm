#!/bin/bash -e
echo "Loading source maps"
chmod 0666 /source_maps/*.map

exec "$@"


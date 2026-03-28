
HOST_DIR="customer-analytics/results"
CONTAINER_NAME=$1

if [ -z "$CONTAINER_NAME" ]; then
    echo "Usage: ./summary.sh <container_id_or_name>"
    exit 1
fi

mkdir -p "$HOST_DIR"

docker cp "$CONTAINER_NAME":/app/pipeline/data_raw.csv "$HOST_DIR"/
docker cp "$CONTAINER_NAME":/app/pipeline/data_preprocessed.csv "$HOST_DIR"/
docker cp "$CONTAINER_NAME":/app/pipeline/insight1.txt "$HOST_DIR"/
docker cp "$CONTAINER_NAME":/app/pipeline/insight2.txt "$HOST_DIR"/
docker cp "$CONTAINER_NAME":/app/pipeline/insight3.txt "$HOST_DIR"/
docker cp "$CONTAINER_NAME":/app/pipeline/summary_plot.png "$HOST_DIR"/


docker stop "$CONTAINER_NAME"
docker rm "$CONTAINER_NAME"

echo "Results copied to $HOST_DIR and container $CONTAINER_NAME removed."
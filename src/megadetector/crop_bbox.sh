python ../../../cameratraps/classification/crop_detections.py \
    s3_images/sphinx_creek/predictions_raw.json \
    s3_images/sphinx_creek/crops/ \
    --images-dir s3_images/sphinx_creek/ \
    --threshold 0.8 \
    --threads 50 \
    --logdir "s3_images/sphinx_creek/crops/"

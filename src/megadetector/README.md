# MegaDetector
The 2 commands in `predict.sh` will run the MegaDetector predictions on the images in `/images` and output `src/megadetector/test_output.json`.

You must clone the yolov5, cameratraps, and ai4eutils repos for the codebase to work. The directory structure assumes these are cloned into a parent folder to this c4c repo (e.g. `YERC/c4c`, `YERC/ai4eutils`, etc.). Instructions were followed from the [MegaDetecor readme](https://github.com/microsoft/CameraTraps/blob/main/megadetector.md#using-the-model) just for this POC. I did not follow exactly, as I did not use a Conda environment (Pyenv instead). I initially tried only pulling the individual files needed to run the `cameratraps/detection/run_detector_batch.py` file but it was a lost cause given the dependency web in the codebase between all of the repos. The simplest solution for now is to clone all 3 and run that batch predictions file seamlessly. 

The downside of cloning all of the repos is that they will need to be cloned to build the Docker container. But, once built, it should run easily. The repos are  7MB, 15MB, and 277MB. 

## S3 Image Predictions
To download images in S3 bucket, run from the `c4c/src/megadetector` dir:
- `python s3_predictions.py`

This script will create (if not existent) a local folder named the value of `LOCAL_DIR` and download recursively each file in `S3_DIR`. To change these values, just edit the script manually. This is a quick and dirty way to get some images to check MegaDetector predictions on. To run predictions on these, run from the `c4c/src/megadetector` dir:
- `export PYTHONPATH="$PYTHONPATH:../../../cameratraps:../../../ai4eutils:../../../yolov5"`
- `python ../../../cameratraps/detection/run_detector_batch.py "md_v5a.0.0.pt" "s3_images/sphinx_creek" "s3_images/sphinx_creek/s3_predictions_output.json" --output_relative_filenames --recursive`
  - change the 2nd argument to the name of the local directory containing the S3 image files. In this case, it is "s3_images/sphinx_creek".
  - change the 3rd argument to the desired output path/file location. In this case, it is "s3_images/sphinx_creek/s3_predictions_output.json".
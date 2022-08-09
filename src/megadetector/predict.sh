# Run from /megadetector dir
export PYTHONPATH="$PYTHONPATH:../../../cameratraps:../../../ai4eutils:../../../yolov5"
python ../../../cameratraps/detection/run_detector_batch.py "md_v5a.0.0.pt" "../../images" "test_output.json" --output_relative_filenames --recursive
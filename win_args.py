"""
A skeleton python script which reads from an input file,
writes to an output file and parses command line arguments
"""
import argparse
from data_prep import data_prep, get_num_classes
import os


def create_yolo_yaml(
    num_classes,
    yaml_template="yolov5/models/yolov5l_template.yaml",
    new_filename="yolov5l.yaml",
):
    f = open(yaml_template, "r")
    new_file = open(new_filename, "w")

    for line in f.readlines():
        # print(line)
        line = line.format(num_classes=num_classes)
        new_file.write(line)

    print(f"created {new_filename}")
    new_file.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument(
        "--dataset",
        type=str,
        default="https://app.roboflow.com/ds/Dv93XN7uls?key=4FIOQLCvWt",
        help="url to dataset",
    )

    args = parser.parse_args()
    print(args.dataset)

    print(os.path.isfile(args.dataset))

    # if not args.dataset == "-1":
    #     data_prep(file_url=args.dataset, filename="tomatoes.zip")
    # yaml_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.yaml")
    # num_classes = get_num_classes(yaml_path=yaml_path)
    # print(f"num_classes: {num_classes}")

    # create_yolo_yaml(
    #     num_classes=num_classes,
    #     yaml_template="yolov5/models/yolov5l_template.yaml",
    #     new_filename="yolov5/models/yolov5l_v1.yaml",
    # )


if __name__ == "__main__":
    main()
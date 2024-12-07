import task_distill
import sys


arguments = [
    "task_distill.py",
    "--teacher_model=./models/bert-base-uncased",
    "--student_model=task_distill_output_try",  # ./models/TinyBERT_General_4L_312D",
    "--data_dir=./glue_data/CoLA",
    "--task_name=cola",
    "--output_dir=task_distill_output_try",
    "--max_seq_length=128",
    "--train_batch_size=32",
    "--num_train_epochs=10",
    # "--aug_train",
    "--do_lower_case",
]


def main():
    sys.argv = arguments
    # print(sys.maxsize)
    task_distill.main()


if __name__ == "__main__":
    main()

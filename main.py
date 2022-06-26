import argparse
import torch
import scoring

def main():
    parser = argparse.ArgumentParser(description="model parameters")
    parser.add_argument('--output_dir', type=str, default="output/", help='Output directory path to store checkpoints.')

    opt=parser.parse_args()
    scorer = scoring.Scorer(opt)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


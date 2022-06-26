#samsum
#python test_rouge.py --c summaries/bart_large.txt --r summaries/golden.txt
#bert-score -r data/golden.txt -c test_output.txt --lang en --rescale_with_baseline

#python test_rouge.py --c ../annotator/bart/summaries/origin_samsum.txt --r ../annotator/bart/summaries/origin_samsum.txt
#bert-score -r summaries/golden.txt -c ../annotator/bart/summaries/origin_samsum.txt --lang en --rescale_with_baseline

#dialogsum
python test_rouge.py --c summaries/dialogsum_bart_large.txt --r data/dialogsum/golden.txt
bert-score -r data/dialogsum/golden.txt -c summaries/dialogsum_bart_large.txt --lang en --rescale_with_baseline


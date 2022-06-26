from transformers import AutoTokenizer
import torch
from bert_score import score
import torch.nn as nn
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class Scorer(nn.Module):
    def __init__(self, opt):
        super(Scorer,self).__init__()
        self.opt=opt
        self.tokenizer = AutoTokenizer.from_pretrained('gpt2-large')
        self.tokenizer.pad_token = self.tokenizer.eos_token

    def sim(self,cands, refs):
        P, R, F1 = score(cands, refs, lang="en", verbose=True)

        return F1


    def fluency(self,cands):
        encodings = self.tokenizer(cands, return_tensors="pt").to(device)
        input_ids = encodings.input_ids
        nlls = []
        for i in range(0, input_ids.size(1), self.stride):
            begin_loc = max(i + self.stride - self.ppl_max_len, 0)
            end_loc = min(i + self.stride, input_ids.size(1))
            trg_len = end_loc - i  # may be different from stride on last loop
            input_ids =input_ids[:, begin_loc:end_loc].to(device)
            target_ids = input_ids.clone()
            target_ids[:, :-trg_len] = -100

            with torch.no_grad():
                outputs = self.model(input_ids, labels=target_ids)
                neg_log_likelihood = outputs[0] * trg_len
            nlls.append(neg_log_likelihood)
        ppl = torch.exp(torch.stack(nlls).sum() / end_loc)

        return 1 / ppl
import os
import json
import argparse
import pdb
from tqdm import tqdm
from timeit import default_timer as timer
from nltk.parse.corenlp import CoreNLPDependencyParser

args = argparse.ArgumentParser(description='Process dir name')
args.add_argument('textfile_name', type = str, help = 'The text file you are going to parsing!')
args.add_argument('jsonfile_name', type = str, help = 'The json file you are going to save your parsing results!')
args.add_argument('port', type = str, help = 'The json file you are going to save your parsing results!')
args = args.parse_args()

textfile_name = args.textfile_name 
jsonfile_name = args.jsonfile_name 
port = args.port

parser = CoreNLPDependencyParser(url='http://localhost:{}'.format(port))


with open(textfile_name, "r") as file_writer:
    sentences = []
    for line in file_writer:
        sentences.append(line.split("\n")[0])

all_words = []
all_relations = []
ferr = open(jsonfile_name + '.err', mode='w')
with open(jsonfile_name, mode='w') as fjson:
    for sent in tqdm(sentences):
        each_json = {}
        each_json['sent'] = sent
        
        # print('----------------------')
        # sttime = timer()

        t = list(parser.parse(sent.split(), properties={'tokenize.whitespace': 'true'}))  

        # print('time for parser.parse(): {} seconds'.format(timer() - sttime))

        dot = t[0].to_dot()
        original_item = dot.split('\n')[4:-1]
        split_item = []
        for each in original_item:
            s = each.split(" ")
            split_item.append(s)
        
        # sttime = timer()

        three_item = []
        four_item = []
        for each in split_item:
            if len(each)==3:
                three_item.append(each)
            elif len(each)==4:
                four_item.append(each)

        words = {}   # index: word
        for each in three_item:
            index = int(each[0])
            word = each[2].lstrip("(")
            word = word.rstrip("]")
            word = word.rstrip("\"")
            word = word.rstrip(")")
            words[index] = word

        words[0]='root'

        all_words.append(words)
        
        if len(words) != len(sent.split()) + 1:
            ferr.write(sent + '\n')

        each_json['words'] = words

        relations = []
        for each in four_item:
            each_relation = []
            index1 = int(each[0])
            each_relation.append(index1)
            index2 = int(each[2])
            each_relation.append(index2)
            relation = each[3].lstrip("[label=")
            relation = relation.lstrip("\"")
            relation = relation.rstrip("\"]")
            each_relation.append(relation)
            relations.append(tuple(each_relation))

        all_relations.append(relations)
        each_json['relations'] = relations
        jsonobj = json.dumps(each_json)
        
        # print('time for extracting relations from parser result: {} seconds'.format(timer() - sttime))

        # sttime = timer()

        fjson.write(jsonobj + '\n')

        # print('time for writing result to json: {} seconds'.format(timer() - sttime))
        
ferr.close()
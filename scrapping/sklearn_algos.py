

def create_index_dict():
	unigram_file=open("unigrams_neurosynth.csv","r")
	bigram_file=open("bigrams_neurosynth.csv","r")
	

	ugrams=""
	for l in unigram_file:
		ugrams+=l
	ugrams_list=ugrams.split(",")


	bigrams=""
	for l in bigram_file:
		bigrams+=l
	
	bigrams_list=bigrams.split(",")



	index=0
	all_words_index_dict={}
	for unigram in ugrams_list:
		if not all_words_index_dict.has_key(unigram):
			all_words_index_dict[unigram]=index
			index+=1
		else:
			print unigram

	for bigram in bigrams_list:
		if not all_words_index_dict.has_key(bigram):
			all_words_index_dict[bigram]=index
			index+=1
		else:
			print bigram

	df = open("neuro_synth_all_words_dictionary.txt","w")
	df.write(str(all_words_index_dict))

	return all_words_index_dict


#summary is a dictionary of words:counts
def get_vector_for_all_genes(summary_file):
	import ast
	import sklearn

	all_terms_index_dict = create_index_dict() #This has already been saved in a file, to avoid excessive computation
	total_terms=len(all_terms_index_dict)


	print "All words dict created"
	input_file=open(summary_file,"r")
	summaries_counts_vector=[]
	for line in input_file:
		if line!="\n":
			line=line.split("\t")
			gene_id=line[0]
			gene_name=line[1]
			summary=line[2]
			summary= ast.literal_eval(summary)

			counts=[0]*total_terms
			for each_term,each_count in summary.items():
				try:
					term_index=all_terms_index_dict[each_term]
					counts[term_index]=each_count
				except:
					print "Dictionary Error, new term introduced"

			summaries_counts_vector.append(counts)

	from sklearn.feature_extraction.text import TfidfTransformer
	transformer = TfidfTransformer()	
	tfidf = transformer.fit_transform(summaries_counts_vector)
	all_weights=tfidf.toarray()


	opfile = open("tfidf_for_gene_entrez_allsummaryterms2.txt","w")
	ipfile = open(summary_file,"r")


	row=0
	for line in ipfile:
		if line!="\n":
			line=line.split("\t")
			gene_id=line[0]
			
			gene_name=line[1]
			tfidf_weights=all_weights[row]

			summary=line[2]
			summary= ast.literal_eval(summary)
			weight_dict={}

			for each_term in summary:
				term_index=all_terms_index_dict[each_term]
				term_weight=tfidf_weights[term_index]
				weight_dict[each_term]=term_weight

			row+=1
			import operator
			weight_dict = sorted(weight_dict.items(), key=operator.itemgetter(1))[::-1]
			opfile.write(gene_id+"\t"+gene_name+"\t"+str(weight_dict)+"\n\n")







get_vector_for_all_genes("gene_and_neurosynth_word_frequency.txt")

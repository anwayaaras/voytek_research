import ast

def get_ngrams_neurosynth(words_file):
	unigrams=open('unigrams_neurosynth.csv','w')
	bigrams=open('bigrams_neurosynth.csv','w')
	ngrams=open('ngrams_neurosynth.csv','w')


	filep = open(words_file,'r')
	for line in filep:
		allwords=line.split(',')

	garbage,nunigrams,nbigrams,nngrams=0,0,0,0
	for word in allwords:
		split_words=word.split(' ')
		if split_words==[]:
			garbage+=1
			continue
		elif len(split_words)==1:
			nunigrams+=1
			unigrams.write(word+",")
		elif len(split_words)==(2):
			nbigrams+=1
			bigrams.write(word+",")
		else:
			nngrams+=1
			ngrams.write(word+",")
	print garbage,nunigrams,nbigrams,nngrams

	unigrams.close()
	bigrams.close()
	ngrams.close()
	filep.close()







"""
Assumes summary is a string. Filters based on neurosynth terms. Returns a list of all the neurosynth terms in the summary
"""
def get_filtered_words(summary,word_freq_dictionary):
	import nltk
	from nltk.corpus import stopwords
	stop = stopwords.words('english')

	words = summary.split(' ')
	words = [w.lower() for w in words]
	words = [w for w in words if w not in stop]

	unigram_file = open('unigrams_neurosynth.csv','r')
	bigram_file = open( 'bigrams_neurosynth.csv','r')

	for l in unigram_file:
		unigrams = set(l.split(','))
	for l in bigram_file:
		bigrams = set(l.split(','))

	
	
	for i in range(len(words)-1):
		unigr = words[i]
		bigr = words[i]+" "+ words[i+1]
		
		if word_freq_dictionary.has_key(unigr):
			word_freq_dictionary[unigr]+=1
		else:
			if unigr in unigrams:
				word_freq_dictionary[unigr]=1


		if word_freq_dictionary.has_key(bigr):
			word_freq_dictionary[bigr]+=1
		else:
			if bigr in bigrams:
				word_freq_dictionary[bigr]=1

	#Have to take last word into consideration
	unigr = words[-1]
	if word_freq_dictionary.has_key(unigr):
		word_freq_dictionary[unigr]+=1
	else:
		if unigr in unigrams:
			word_freq_dictionary[unigr]=1

	return word_freq_dictionary


#get_ngrams_neurosynth('neurosynth_terms.csv')
# summary='Alpha-2-macroglobulin is a protease inhibitor and cytokine transporter. It inhibits many proteases, including trypsin, thrombin and collagenase. A2M is implicated in Alzheimer disease (AD) due to its ability to mediate the clearance and degradation of A-beta, the major component of beta-amyloid deposits. [provided by RefSeq, Jul 2008]', u'Is able to inhibit all four classes of proteinases by a unique trapping mechanism. This protein has a peptide stretch, called the bait region which contains specific cleavage sites for different proteinases. When a proteinase cleaves the bait region, a conformational change is induced in the protein which traps the proteinase. The entrapped enzyme remains active against low molecular weight substrates (activity against high molecular weight substrates is greatly reduced). Following cleavage in the bait region a thioester bond is hydrolyzed and mediates the covalent binding of the protein to the proteinase', u'A2M (Alpha-2-Macroglobulin) is a Protein Coding gene. Diseases associated with A2M include alpha-2-macroglobulin deficiency and alzheimer disease. Among its related pathways are Signaling by GPCR and Rho GTPase cycle. GO annotations related to this gene include enzyme binding and growth factor binding. An important paralog of this gene is CD109.', u'The protein encoded by this gene is an endocytic receptor involved in several cellular processes, including intracellular signaling, lipid homeostasis, and clearance of apoptotic cells. In addition, the encoded protein is necessary for the A2M-mediated clearance of secreted amyloid precursor protein and beta-amyloid, the main component of amyloid plaques found in Alzheimer patients. Expression of this gene decreases with age and has been found to be lower than controls in brain tissue from Alzheimer patients. [provided by RefSeq, Jan 2010]', u'Endocytic receptor involved in endocytosis and in phagocytosis of apoptotic cells. Required for early embryonic development. Involved in cellular lipid homeostasis. Involved in the plasma clearance of chylomicron remnants and activated LRPAP1 (alpha 2-macroglobulin), as well as the local metabolism of complexes between plasminogen activators and their endogenous inhibitors. May modulate cellular events, such as APP metabolism, kinase-dependent intracellular signaling, neuronal calcium signaling as well as neurotransmission', u'Functions as a receptor for Pseudomonas aeruginosa exotoxin A', u'LRP1 (Low Density Lipoprotein Receptor-Related Protein 1) is a Protein Coding gene. Diseases associated with LRP1 include compartment syndrome and cerebral amyloid angiopathy. Among its related pathways are Signaling by GPCR and Disease. GO annotations related to this gene include calcium ion binding and protein complex binding. An important paralog of this gene is LRP1B.', u'CPAMD8 belongs to the complement component-3 (C3; MIM 120700)/alpha-2-macroglobulin (A2M; MIM 103950) family of proteins, which are involved in innate immunity and damage control. Complement components recognize and eliminate pathogens by direct binding or by mediating opsonization/phagocytosis and intracellular killing, and A2M is a broad-spectrum protease inhibitor (Li et al., 2004 [PubMed 15177561]).[supplied by OMIM, Mar 2008]', u'CPAMD8 (C3 And PZP-Like, Alpha-2-Macroglobulin Domain Containing 8) is a Protein Coding gene. Among its related pathways are Signaling by GPCR and Signaling by GPCR. GO annotations related to this gene include serine-type endopeptidase inhibitor activity. An important paralog of this gene is CD109.', u'This gene encodes a protein that interacts with the low density lipoprotein (LDL) receptor-related protein and facilitates its proper folding and localization by preventing the binding of ligands. Mutations in this gene have been identified in individuals with myopia 23. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2013]', u'Interacts with LRP1/alpha-2-macroglobulin receptor and glycoprotein 330', u'LRPAP1 (Low Density Lipoprotein Receptor-Related Protein Associated Protein 1) is a Protein Coding gene. Diseases associated with LRPAP1 include myopia 23, autosomal recessive and rare isolated myopia. Among its related pathways are Reelin signaling pathway and Signaling events mediated by the Hedgehog family. GO annotations related to this gene include heparin binding and low-density lipoprotein particle receptor binding.', u'This gene encodes a member of the alpha-macroglobulin superfamily. The encoded protein acts as an inhibitor for several proteases, and has been reported as the p170 antigen recognized by autoantibodies in the autoimmune disease paraneoplastic pemphigus (PNP; PMID: 20805888). Alternative splicing results in multiple transcript variants. [provided by RefSeq, Feb 2012]', u'Is able to inhibit all four classes of proteinases by a unique trapping mechanism. This protein has a peptide stretch, called the bait region which contains specific cleavage sites for different proteinases. When a proteinase cleaves the bait region, a conformational change is induced in the protein which traps the proteinase. The entrapped enzyme remains active against low molecular weight substrates (activity against high molecular weight substrates is greatly reduced). Following cleavage in the bait region a thioester bond is hydrolyzed and mediates the covalent binding of the protein to the proteinase (By similarity). Displays inhibitory activity against chymotrypsin, papain, thermolysin, subtilisin A and, to a lesser extent, elastase but not trypsin. May play an important role during desquamation by inhibiting extracellular proteases.', u'A2ML1 (Alpha-2-Macroglobulin-Like 1) is a Protein Coding gene. Diseases associated with A2ML1 include noonan syndrome 1 and paraneoplastic pemphigus. GO annotations related to this gene include serine-type endopeptidase inhibitor activity and peptidase inhibitor activity. An important paralog of this gene is CD109.', u'Is able to inhibit all four classes of proteinases by a unique trapping mechanism. This protein has a peptide stretch, called the bait region which contains specific cleavage sites for different proteinases. When a proteinase cleaves the bait region, a conformational change is induced in the protein which traps the proteinase. The entrapped enzyme remains active against low molecular weight substrates (activity against high molecular weight substrates is greatly reduced). Following cleavage in the bait region a thioester bond is hydrolyzed and mediates the covalent binding of the protein to the proteinase', u'PZP (Pregnancy-Zone Protein) is a Protein Coding gene. Diseases associated with PZP include oophoritis. Among its related pathways are Cell adhesion_Plasmin signaling. GO annotations related to this gene include serine-type endopeptidase inhibitor activity and endopeptidase inhibitor activity. An important paralog of this gene is CD109.', u'This gene encodes a glycosyl phosphatidylinositol (GPI)-linked glycoprotein that localizes to the surface of platelets, activated T-cells, and endothelial cells. The protein binds to and negatively regulates signalling by transforming growth factor beta (TGF-beta). Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2014]', u'Modulates negatively TGFB1 signaling in keratinocytes.', u'CD109 (CD109 Molecule) is a Protein Coding gene. Diseases associated with CD109 include fetal and neonatal alloimmune thrombocytopenia. GO annotations related to this gene include serine-type endopeptidase inhibitor activity. An important paralog of this gene is C3.', u'A2MP1 (Alpha-2-Macroglobulin Pseudogene 1) is a Pseudogene. Diseases associated with A2MP1 include alzheimer disease.'
# result={}
# for s in summary:
# 	result=get_filtered_words(s,result)
# print result

"""
The function returns the frequency of neurosynth words for the genes in the summary file. The format of the summary file is expected to be as follows:
1	alpha-1-B glycoprotein	[<summary_string>]

"""

def gene_to_neurosynth_bowords(summary_file,output_file):
	output_file = open(output_file,'w')
	input_file=open(summary_file,'r')

	for line in input_file:
		if line!="\n":
			line=line.split("\t")
			gene_id=line[0]
			gene_name=line[1]
			summary=line[2]
			summary=summary[1:-1]
			
			summaries=summary.split("u'")
			result={}
			for s in summaries:
				if s!="":
					result=get_filtered_words(summary,result)

			output_file.write(gene_id+"\t"+gene_name+"\t"+str(result)+"\n")


	output_file.close()
	input_file.close()





#gene_to_neurosynth_bowords('genecards_scrapped.csv','gene_and_neurosynth_word_frequency.txt')

def histogram_from_dict(word_count_dict):
	import pylab as pl
	import numpy as np

	d = word_count_dict
	X = np.arange(len(d))
	pl.bar(X, d.values(), align='center', width=0.5)
	pl.xticks(X, d.keys(), rotation='vertical')
	ymax = max(d.values()) + 1
	pl.ylim(0, ymax)
	pl.show()

def gene_and_diseases(gene_and_neurosynth_word_frequency_file, diseases_terms_file, opfile_name):
	"""
	for the gene_and_neurosynth_word_frequency_file generates a file which has frequency of only tne words Containing diseases_terms_file for every gene
	"""

	input_file = open(gene_and_neurosynth_word_frequency_file,"r")
	terms_file = open(diseases_terms_file,"r")
	output_file = open(opfile_name, "w")

	my_terms= set()
	for line in terms_file:
		line = line.strip()
		line = line.split("\r")
		for each_word in line:
			my_terms.add(each_word)


	print my_terms
	for line in input_file:
		if line!="\n":
			diseases = dict()
			line=line.split("\t")
			gene_id=line[0]
			gene_name=line[1]
			summary=line[2]
			summary= ast.literal_eval(summary)
			for each_term,each_count in summary.items():
				if each_term in my_terms:
					diseases[each_term]=each_count

			output_file.write(gene_id+"\t"+gene_name+"\t"+str(diseases)+"\n")

	input_file.close()
	terms_file.close()
	output_file.close()

def word_genes_frequency(word,gene_word_freq_file):
	input_file = open (gene_word_freq_file,"r")
	gene_count_dic={}

	for line in input_file:
		if line!="\n":
			line=line.split("\t")
			gene_id=line[0]
			gene_name=line[1]
			summary=line[2]
			summary= ast.literal_eval(summary)
			if word in summary:
				gene_count_dic[gene_name]=int(summary[word])


	print gene_count_dic
	try:
		histogram_from_dict(gene_count_dic)
	except:
		print "Error: Count dictionary is empty- Not a single gene has the word"



				





if __name__ == "__main__":
	#word_count_dict=dict([('metabolism', 0.38044555264343449), ('important', 0.30043825906932131), ('gene', 0.29211488458069568), ('concentration', 0.28626825151789598), ('potential', 0.2818447626376811), ('sensitivity', 0.27346916153770212), ('substrate', 0.23288262812707056), ('plays important', 0.21939551956277462), ('act', 0.20962248261079161), ('important role', 0.20502547994069051), ('regulation', 0.19426485079550787), ('receptor', 0.19022277632171725), ('plays', 0.17887114926347156), ('involved', 0.16852250136376051), ('role', 0.16688319431058982), ('binding', 0.1652664991111909), ('pathways', 0.15163985654986503), ('include', 0.14742831807761028), ('coding', 0.1447024151331768)])
	#histogram_from_dict(word_count_dict)

	#gene_and_diseases("results_gene_and_neurosynth_word_frequency.txt", "neurosynth_diseases_term_set.csv", "results_gene_versus_diseases.txt")

	word_genes_frequency("alzheimer","results_gene_and_neurosynth_word_frequency.txt")


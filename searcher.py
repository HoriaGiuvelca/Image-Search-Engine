import numpy as np 
import csv

class Searcher:
    def __init__(self, indexPath):

        self.indexPath = indexPath
    
    def search(self, queryFeatures, limit = 10):

        results = {}


        with open(self.indexPath) as f:

            reader = csv.reader(f)


            for row in reader:
                #se parseaza imaginile si feature-urile si se calculeaza "chi-squared distance" intre ele
                features = [float(x) for x in row[1:]]
                d = self.chi2_distance(features, queryFeatures)

                #facem update la dictionarul de rezultate, cheia fiind ID-ul imaginii, iar valoarea este distanta fata de imaginea query
                results[row[0]] = d

            #close the reader
            f.close()
        
        #sortam rezultatele, astfel incat distantele mai mici ajung in capul listei
        results = sorted([(v, k) for (k, v) in results.items()])

        #return our results
        return results[:limit]
    
    def chi2_distance(self, histA, histB, eps = 1e-10):
        
        d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps) for (a, b) in zip(histA, histB)])


        return d
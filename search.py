from colordescriptor import ColorDescriptor
from searcher import Searcher
import argparse
import cv2
import matplotlib.pyplot as mpl


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required = True, help = "Path-ul catre fisierul 'baza_de_date'")
ap.add_argument("-q", "--query", required = True, help = "Path-ul catre imaginea care se doreste a fi 'cautata'")
ap.add_argument("-r", "--result-path", required = True, help = "Path-ul catre fisierul cu poze")
args = vars(ap.parse_args())


cd = ColorDescriptor((8, 12, 3))


query = cv2.imread(args["query"])
features = cd.describe(query)


searcher = Searcher(args["index"])
results = searcher.search(features)

#afiseaza query-ul
query = cv2.resize(query, (1366, 768))
cv2.imshow("Query", query)

#afiseaza rezultatele
for(score, resultID) in results:
    result = cv2.imread("./" +  resultID)
    result = cv2.resize(result, (1366, 768))
    mpl.figure()
    cv2.imshow("Result", result)
    cv2.waitKey(0)
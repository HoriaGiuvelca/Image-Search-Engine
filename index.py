from colordescriptor import ColorDescriptor
import argparse
import glob
import cv2


ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = True,
	help = "Path-ul catre directorul care contine pozele")
ap.add_argument("-i", "--index", required = True,
	help = "Path-ul catre fisierul 'baza_de_date'")
args = vars(ap.parse_args())

# selectarea numarului de "bins" pentru histograma
cd = ColorDescriptor((8, 12, 3))


output = open(args["index"], "w")


for imagePath in glob.glob(args["dataset"] + "/*.jpg"):
	imageID = imagePath[imagePath.rfind("/") + 1:]
	image = cv2.imread(imagePath)


	features = cd.describe(image)
    

	features = [str(f) for f in features]
	output.write("%s,%s\n" % (imageID, ",".join(features)))
    

output.close()
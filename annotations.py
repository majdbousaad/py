elementToAnnotations = {1 : [25, 55], 2 : [25,35, 55], 3 : [35 ,45], 5 : [75, 15, 25]}

def getAnnotationToElements():
    annotationToElements = dict()
    for element in elementToAnnotations.keys():
        for annotation in elementToAnnotations[element]:
            annotationToElements.setdefault(annotation,[]).append(element)
    return annotationToElements


print(getAnnotationToElements())

def getUsefulAnnotations():
    annotationToElements = getAnnotationToElements()
    usefulAnnotations = list()

    for annotation in annotationToElements.keys():
        elements = annotationToElements[annotation]
        if len(elements) > 1:
            usefulAnnotations.append(annotation)
    return usefulAnnotations


print(getUsefulAnnotations())

def getCommonAnnotations(e1, e2):
    commonAnnotations = list()
    annotationsOfE1 = elementToAnnotations[e1]
    annotationsOfE2 = elementToAnnotations[e2]
    for annotation in annotationsOfE1:
        if annotation in annotationsOfE2:
            commonAnnotations.append(annotation)
    return commonAnnotations

print(getCommonAnnotations(1, 5))

#for question 5
def getCommonElements(a1, a2):
    annotationToElements = getAnnotationToElements()
    commonElements = list()
    elementsOfA1 = annotationToElements[a1]
    elementsOfA2 = annotationToElements[a2]
    for element in elementsOfA1:
        if element in elementsOfA2:
            commonElements.append(element)
    return commonElements


def getElementsSimilarity(e1, e2):
    commonAnnotationsLen = len(getCommonAnnotations(e1, e2))
    return commonAnnotationsLen/ (len(elementToAnnotations[e1]) + len(elementToAnnotations[e2]))


print(getElementsSimilarity(1, 3))


def getAnnotationGraph():
    listOfTuples = list(tuple())
    annotationsList = list(getAnnotationToElements())

    for i in range(0, len(annotationsList)):
        for j in range(i + 1, len(annotationsList)):
            a1 = annotationsList[i]
            a2 = annotationsList[j]
            listOfTuples.append( ( a1, a2, len(getCommonElements(a1, a2)) ) )
    return listOfTuples


print(getAnnotationGraph())


# Gets and Returns the sentences from the sentences.txt file
def get_sentences():
    sentences = open("./sentences.txt", "r").readlines()
    return sentences

__all__ = ["get_sentences"]


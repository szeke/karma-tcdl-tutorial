

def blAggregationUri(recordId):
    #return getTextHash(recordId)
    return recordId


def blSourceResourceUri(recordId):
    return blAggregationUri(recordId)+"/sourceResource"


def blAgentUri(lastFirst):
    str = lastFirst.strip().replace('.','').lower()
    list = str.split(',')
    if len(list) == 2:
    	str = list[1] + " " + list[0]
	return "person/" + str.replace(' ','')


def blCleanAgent(name):
	return name.strip().replace('.','')


def blTopicN(topic, index):
	list = topic.split('/')
	return list[index].strip()

def blTopic1(topic):
	return blTopicN(topic,0)


def blTopic2(topic):
	return blTopicN(topic,1)
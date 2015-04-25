## topics_general-sample.csv

### PyTransforms
#### _topic1_
From column: _Topic-general_
>``` python
return blTopic1(getValue("Topic-general"))
```

#### _topic2_
From column: _Topic-general_
>``` python
return blTopic2(getValue("Topic-general"))
```

#### _topic1_uri_
From column: _topic1_
>``` python
return blTopicUri(getValue("topic1"))
```

#### _topic2_uri_
From column: _topic2_
>``` python
return blTopicUri(getValue("topic2"))
```

#### _source_resource_uri_
From column: _BL Record ID_
>``` python
return blSourceResourceUri(getValue("BL Record ID"))
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _source_resource_uri_ | `uri` | `dpla:SourceResource1`|
| _topic1_ | `skos:prefLabel` | `skos:Concept1`|
| _topic1_uri_ | `uri` | `skos:Concept1`|
| _topic2_ | `skos:prefLabel` | `skos:Concept2`|
| _topic2_uri_ | `uri` | `skos:Concept2`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `dpla:SourceResource1` | `dct:subject` | `skos:Concept1`|
| `dpla:SourceResource1` | `dct:subject` | `skos:Concept2`|
| `skos:Concept1` | `skos:narrower` | `skos:Concept2`|

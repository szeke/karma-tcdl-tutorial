## authors-people.csv

### PyTransforms
#### _source_reseource_uri_
From column: _BL Record ID_
>``` python
return blSourceResourceUri(getValue("BL Record ID"))
```

#### _author_uri_
From column: _Author-Persons_
>``` python
return blAgentUri(getValue("Author-Persons"))
```

#### _author_clean_
From column: _Author-Persons_
>``` python
return blCleanAgent(getValue("Author-Persons"))
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _author_clean_ | `skos:prefLabel` | `edm:Agent1`|
| _author_uri_ | `uri` | `edm:Agent1`|
| _source_reseource_uri_ | `uri` | `dpla:SourceResource1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `dpla:SourceResource1` | `dct:creator` | `edm:Agent1`|

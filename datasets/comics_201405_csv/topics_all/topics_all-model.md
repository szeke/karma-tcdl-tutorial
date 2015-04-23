## topics_all.csv

### PyTransforms
#### _aggregation_uri_
From column: _BL Record ID_
>``` python
return blAggregationUri(getValue("BL Record ID"))
```

#### _source_reseource_uri_
From column: _BL Record ID_
>``` python
return blSourceResourceUri(getValue("BL Record ID"))
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _BL Record ID_ | `dct:identifier` | `edm:ProvidedCHO1`|
| _Date of Publication_ | `skos:prefLabel` | `edm:TimeSpan1`|
| _Place of Publication_ | `skos:prefLabel` | `edm:Place1`|
| _Publisher_ | `dct:publisher` | `edm:ProvidedCHO1`|
| _Title_ | `dct:title` | `edm:ProvidedCHO1`|
| _aggregation_uri_ | `uri` | `ore:Aggregation1`|
| _source_reseource_uri_ | `uri` | `edm:ProvidedCHO1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `edm:ProvidedCHO1` | `dc:date` | `edm:TimeSpan1`|
| `edm:ProvidedCHO1` | `dct:spatial` | `edm:Place1`|
| `ore:Aggregation1` | `edm:aggregatedCHO` | `edm:ProvidedCHO1`|
| `ore:Aggregation1` | `edm:dataProvider` | `xsd:British Library`|

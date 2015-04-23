
README - Metadata subsets from the British Library


GENERAL INFORMATION ABOUT THE DATASETs

The British National Bibliography (BNB) 'subject themed' datasets are a set of .csv tables on a chosen theme. These tables provide different views of the theme, split by different entities including subject topics, people and places.

Each entry in a table contains the identifier (BL Record ID) for the full metadata record held in the British Library's BNB catalogue at http://bnb.bl.uk


TABLES

briefList.csv
a brief citation-like listing of all items on the subject theme. Includes BL Record ID, Author, Title, Place of publication, Publisher, Date of publication and ISBN.

titles.csv
a listing of book titles + Date of publication, Place of publication, Publisher, Physical Description, Part of series, Number in series, ISBN and BL Record ID.

authors_any.csv
a list of authors of all types, personal or institutions + Book title, Date of publication, Place of publication, ISBN and BL Record ID.

authors_persons.csv
a list of personal authors + Book title, Date of publication, Place of publication, ISBN and BL REcord ID.

authors_organisations.csv
a list of instutions as authors + Book title, Date of publication, Place of publication, ISBN and BL REcord ID.

authors_conferences.csv
a list of conferences + Book title, Date of publication, Place of publication, ISBN and BL REcord ID.

dewey_classification.csv
a list of Dewey classification numbers + Book title, subject topics, Date of publication, Place of publication, ISBN and BL REcord ID.

topics_all.csv
a list of all types of subject topic + subject class, Book title, Date of publication, Place of publication, ISBN and BL REcord ID.

topics_people.csv
a list of people as a subject topic + subject class, Book title, Date of publication, Place of publication, ISBN and BL REcord ID.

topics_organisation.csv
a list of organisations as a subject topic + subject class, Book title, Date of publication, Place of publication, ISBN and BL REcord ID.

topics_conferences.csv
a list of conferences as a subject topic + subject class, Book title, Date of publication, Place of publication, ISBN and BL REcord ID.

topics_general.csv
a list of general subject topics + subject class, Book title, Date of publication, Place of publication, ISBN and BL REcord ID.

topics_places.csv
a list of places as a subject topic + subject class, Book title, Date of publication, Place of publication, ISBN and BL REcord ID.


FORMAT OF THE DATA

Header row: The first row is a header row containing the name of the value e.g. Place of publication

Repeating values: Some cells may contain repeats of values separated with a delimiter e.g. 'London ; New York' in Place of publication. The two places are separated with the delimiter ';'

Multiple facets: Some cells may contain multiple facets separated with a delimiter e.g. 'Accounting / Standards' in topic_general where the sub facet is separated with the delimiter ' / '

Import issues: BL Record IDs are 9 digits long and begin with at least one 0 (zero). Some import utilities may strip these. In Excel, for example, it is possible to format the BL Record ID column to correct this by choosing ‘Format cells/Number/Custom/ and choosing 0 (zero) as the format option. Enter 9 zeroes into the box and any IDs that are missing the leading zeroes will be corrected.


SUPPORTING INFORMATION

Data cleaning: The metadata in the tables has come from the British National Bibliography. Cataloguing rules and procedures have changed over time so there may be some variations in the detail of each entry. Some cleaning of the data has been carried out to remove unnecessary punctuation from the entries; however, given the varying nature of the original cataloguing records there may be some instances where this has not been successful. In many cases these examples will be obvious because they will occur at the beginning of the table, prior to the beginning of the alphabetical listing.

Punctuation issues: We have attempted to clean most punctuation issues, however in some cases such as dates there may be characters that provide information. For example, ‘c.’ = approximate, square brackets or ‘?’ = an unconfirmed date.

Character set issues: The raw bibliographic metadata is held in a library character set format, MARC8. We have exported the csv files as UTF-8 but depending on which utility you use to import or analyse the data, there may be some instances where there are character set problems. These may be circumvented if Unicode UTF-8 is an import option for the data format.

Dewey-classification table: Dewey classification subject information and summaries can be found at http://en.wikipedia.org/wiki/List_of_Dewey_Decimal_classes


For further information or to comment, please contact metadata@bl.uk.













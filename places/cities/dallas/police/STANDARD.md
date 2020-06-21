Crime Department Open Data Standard! 
====================================

This document defines the format and structure of the files that comprise a City Crime Dataset

Term Definitions
================

This section defines terms that are used throughout this document.

- **Dataset** - A complete set of files defined by this specification reference. Altering the dataset creates a new version of the dataset. Datasets should be published at a public, permanent URL, including the zip file name.
- **Record** - A basic data structure comprised of a number of different field values describing a single entity (e.g. transit agency, stop, route, etc.). Represented, in a table, as a row.
- **Field** - A property of an object or entity. Represented, in a table, as a column.
- **Field Value** - An individual entry in a field. Represented, in a table, as a single cell.
- **Required** - The field must be included in the dataset, and a value must be provided in that field for each record. Some required fields permit an empty string as a value (denoted in this specification as empty). To enter an empty string, just omit any text between the commas for that field.
- **Optional** - The field may be omitted from the dataset. If an optional column is included, some of the entries in that field may be empty strings. To enter an empty string, just omit any text between the commas for that field. Note that an omitted field is equivalent to a field that is entirely empty.
- **Conditionally required** - The field or file is required under certain conditions, which are outlined in the field or file description. Outside of these conditions, this field or file is optional.
- **Service day** - A service day is a time period used to indicate route scheduling. The exact definition of service day varies from agency to agency but service days often do not correspond with calendar days. A service day may exceed 24:00:00 if service begins on one day and ends on a following day. For example, service that runs from 08:00:00 on Friday to 02:00:00 on Saturday, could be denoted as running from 08:00:00 to 26:00:00 on a single service day.

Dataset Files
=============

This specification defines the following files:

- **csv**: CSV files should have the headers on the first line and rows delimited by a comma. 


File Requirements
=================

The following requirements apply to the format and contents of the dataset files:

- All files must be saved as comma-delimited text.
- The first line of each file must contain field names. Each subsection of the Field definitions section corresponds to one of the files in a Police Incident Dataset and lists the field names that may be used in that file.
- All field names are case-sensitive.
- Field values may not contain tabs, carriage returns or new lines.
- Field values that contain quotation marks or commas must be enclosed within quotation marks. In addition, each quotation mark in the field value must be preceded with a quotation mark. This is consistent with the manner in which Microsoft Excel outputs comma-delimited (CSV) files. For more information on the CSV file format, see http://tools.ietf.org/html/rfc4180. The following example demonstrates how a field value would appear in a comma-delimited file:
- Original field value: Contains "quotes", commas and text
- Field value in CSV file: "Contains ""quotes"", commas and text"
- Field values must not contain HTML tags, comments or escape sequences.
- Remove any extra spaces between fields or field names. Many parsers consider the spaces to be part of the value, which may cause errors.
- Each line must end with a CRLF or LF linebreak character.
- Files should be encoded in UTF-8 to support all Unicode characters. Files that include the Unicode byte-order mark (BOM) character are acceptable. See http://unicode.org/faq/utf_bom.html#BOM for more information on the BOM character and UTF-8.


Field Types
===========

This section defines the different field types allowed into the crime department of datacity

- **incident_address** (String)
- **lat** (Numeric)
- **lon** (Numeric)
- **date** (String)

Field Definitions
=================

- **incident_address:** Address of where the incident occurred
- **lat:** Laitude of the incident
- **lon** Longitude of the incident
- **date** Date and Time of the incident. 
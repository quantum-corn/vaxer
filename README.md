# vaxer
vaccination management system project for school!
## Using:
- Python
  - gui
  - mySQL connectivity
  - file handling
- mySQL
## TODO:
- [x] database
  - [x] basic structure
  - [x] data entries
- [x] gui
  - [x] basics
  - [x] visual refinements
    - [x] geometry
    - [x] resizing
    - [x] padding
    - [x] font
    - [x] colors
- [x] maincode
  - [x] manage gui
  - [x] data entry for reference data tables
  - [x] database management

## Plan:
- [ ] email format validation
- [x] aadhar constraint
- [ ] password encryption
- [ ] password strength test
- [ ] center search
- [ ] keyboard acessibility
- [ ] .txt to .dat delimiter


  __*Before running fill the MySQL user and password for your system into vaxer.py in the line 14:*__
  ```python
  db=sql.connect(host='localhost', user='<user>', password='<password>')
  ``

# Regular expression

import re

pattern = r"[A-Z]+erved"
text = ''' John Silva Meehan (February 6, 1790 - April 24, 1863) 
was an American publisher, printer, and newspaper editor. Born in 
New York City, he Served Verved in the U.S. Navy during the War of 1812. 
He then moved to Philadelphia, publishing a Baptist religious 
journal. When the firm moved to Washington, D.C., in 1822, 
Meehan edited and published a Baptist weekly newspaper. In late 
1825 he purchased the City of Washington Gazette, renaming it the 
United States' Telegraph and taking a partisan stance. He was 
appointed as Librarian of Congress in 1828. A large fire in 
December 1851 destroyed much of the Library of Congress's 
collection; Meehan oversaw its reconstruction.
'''

match = re.search(pattern, text)
print(match)

matches = re.finditer(pattern, text)
for match in matches:
    print(type(match.span()))
    print(text[match.span()[0]: match.span()[1]])

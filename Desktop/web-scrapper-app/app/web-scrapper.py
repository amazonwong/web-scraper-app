iimport requests
from bs4 import BeautifulSoup #note that the import package command is bs4

# ISSUE REQUEST

r = requests.get("https://www.gutenberg.org/ebooks/author/65")

# PARSE RESPONSE

raw = r.text
soup = BeautifulSoup(raw)
titles = soup.find_all("span", "title")
for i in range(0, 9): #we want to see only span tags labeled "titles"
  print(titles[i])

#> <span class="title">Sort Alphabetically</span>
#> <span class="title">Sort by Release Date</span>
#> <span class="title">See also: Wikipedia</span>
#> <span class="title">The Complete Works of William Shakespeare
#> <span class="title">The Tragedy of Romeo and Juliet</span>
#> <span class="title">Hamlet, Prince of Denmark</span>
#> <span class="title">Macbeth</span>
#> <span class="title">Hamlet</span>
#> <span class="title">Beautiful Stories from Shakespeare</span>

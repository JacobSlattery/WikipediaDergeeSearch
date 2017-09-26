# wikiHitlerSearch
Based on the idea of 7 degrees of separation, this game predicts that in any given wikipedia article 
there is a series of jumps one can make to reach Hitler's page in only 3 clicks.
The program excepts the url of a wikipedia article and sifts through the data looking for links to other articles
and whether they are Hitler's article. If none of them link to Hitler, the program requests each link and searches those sites as well. 
The process is repeated once again and, if it has made it to the third degree, likely has thousands of links to search through.

The code can be easily modified to seach for any other article, or to even go a 4th and 5th degree in. I've yet to find an article that made
it past the 3rd degree.

# wikiHitlerSearch
Based on the idea of 7 degrees of separation, this game attempts to prove that in any given Wikipedia article there is a series of clicks the user can make to Hitler's page with a maximum number of jumps being 3. The program excepts the URL of a Wikipedia article and sifts through the data looking for links to other articles and whether they are Hitler's article. If none of them link to Hitler, the program requests each link and searches those sites as well. The process is repeated once again and, if it has made it to the third degree, likely has thousands of links to search through.

The code can be easily modified to search for any other article or to go a higher number of degrees in, though it will take a lot longer to calculate.
I've yet to find an article that made it past the 3rd degree.

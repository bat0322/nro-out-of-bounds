# Non-Recording Option at Dartmouth College
## Is it just false advertising?

### What did I build and why?
This term I am taking a class called Sports Analytics, a QSS class. I am taking this class purely out of interest and it is not involved in my major plans or minor plans whatsoever. As such I figured this would be a great time to exercise the Non-Recording Option, lonng touted by admissions officers and deans as one of the great parts of Dartmouth, to take this interesting class without worrying about its effect on my GPA. What a perfect fit!

Alas, it was not to be. I was aware that some classes did not allow enrollees to exercise the NRO, as it had happened to me before. I went to check the list, and yes there it was. NRO Out of Bounds. I scrolled through the list and was amazed at just how many classes were listed as NRO Out of Bounds. Were there even any classes that NRO In Bounds??? I figured a good metric for this would be to count the number of enrollees in NRO OOB classes and see what fraction that represented of total enrollees. A student would be counted for each class they were enrolled in, so a student enrolled in three classes would be counted as three "enrollees".

This small project obviously arose out of spite, but also out of interest in the technologies I could use. I had long had an interest in webscraping but I had never actually explored it, so I figured this would be a great opportunity. So to answer my question, I wrote a Python script to digest the information and run the analysis needed. I used BeautifulSoup and Selenium as tools to get the data from the pertinent Dartmouth websites, and wrote some auxiliary code to handle some smaller functionality, namely creating a CSV of department names and subject codes.

### What did I learn?
This project gave me a chance to learn a lot about webscraping and the associated technologies. I got relatively familiar with BeautifulSoup and Selenium and how they could make HTML palatable and manipulate webpages, respectively. I also learned that some webpages (cough cough timetable) don't make for easy analysis due to unnecessary obfuscation. I also learned a bit more about Python scripting beyond my relatively minor experience beyond CS1. 

### What didn't work?
As mentioned above, some of Dartmouth's websites are not the best for webscraping as the sites are messy and convoluted. Also there is a frustrating lack of symmetry between different Dartmouth sources. For example, the department names as listed on timetable are not the same as listed on the NRO Out of Bounds site. It was relatively few, so I just went directly into the CSV I had generated and edited the department names that did not match. Also the timetable listings were not easily ingestible, so I just copy and pasted those listings and generated csv (hence the csv script). 

### Things I didn't get to
I had wanted to also explore some data visualization in Python using pandas, but I was not able to get to that point early enough in the process. I also wanted to do a loop to look at all four terms that have data available on timetable, but again ran out time (though this should be a relatively quick extension). If the Registrar's Office also wanted to give me data extending back into the past I could have also found the change over time in fractional NRO OOB stats.

### Conclusion
When my script is run it spits out an answer of 0.45308199615724154, meaning that 45.31% of enrollees are in classes that they cannot NRO, which seems to me a high proportion given how much it is touted in our admissions literature. Also, this is a lower bound, as students also cannot typically NRO classes in their major, and can only NRO one class in their minor. Personally, I would call this false advertising, but I'll leave that assessment up to you.

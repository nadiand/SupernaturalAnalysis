import AO3
import argparse

def scraping(start):
    end = str(int(start)+2)
    time_range = "%s-%s weeks" % (start, end)
    search = AO3.Search(fandoms="Supernatural (TV 2005)", revised_at=time_range)

    f = open("spn_data.txt", "a", encoding="utf-8")

    while search.page <= 50: # Limiting the number of scraped fics in order to not get kicked out of the website
        search.update()
        for w in search.results:
          
            work = "%s\t%s\t%s\t" % (w.title, str(w.date_updated), w.language)
            if not w.tags is None:
                work += "%s\t" % '; '.join(w.tags)
            if not w.characters is None:
                work += "%s\t" % '; '.join(w.characters)
            if not w.relationships is None:
                work += "%s\t" % '; '.join(w.relationships)
                
            try:
                if not w.summary is None:
                    work += "%s\t" % w.summary
                else:
                    work += "N/A\t"
            except:
                work += "N/A\t"

            # We scraped the comments as well, but those were not used in the analysis
            fic = AO3.Work(w.id)
            fic.load_chapters()
            comments = fic.get_comments(100)
            try:
                if not comments is None: 
                    work += '; '.join([comment.text for comment in comments])
            except:
                work += "N/A"

            work = work.replace("\n", "")
            f.write(work + "\n")
        
        search.page += 1

    f.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='none')
    parser.add_argument('start', type=str)

    args = parser.parse_args()
    scraping(args.start)

# Suppose you have obtained the following video data via a database query or REST API query
video_data = [{'title': 'Learn Python in 10 hours', 'views': 500_603, 'years': 2,
               'likes': 2091, 'click-through rate': 42.6, 'duration': 592, 'average view duration': 115},
              {'title': 'Quick Python course for data scientists', 'views': 302_794, 'years': 2,
               'likes': 1988,'click-through rate': 33.8, 'duration': 176, 'average view duration': 42},
              {'title': 'Complete Tutorial for Python Pandas Data Science', 'views': 2_402_334, 'years': 4,
               'likes': 55_498,'click-through rate': 65.4, 'duration': 82, 'average view duration': 33},
              {'title': 'Complete Tutorial for Python NumPy', 'views': 675_770, 'years': 3,
               'likes': 20_728, 'click-through rate': 46.9, 'duration': 65, 'average view duration': 26},
              {'title': 'Comprehensive Tutorial for Python Beautiful Soup Web Scraping', 'views': 230_821, 'years': 3,
               'likes': 6851,'click-through rate': 34.7, 'duration': 75, 'average view duration': 24},
              {'title': 'Real-World Python Machine Learning Tutorial', 'views': 199_689, 'years': 3,
               'likes': 5848,'click-through rate': 28.5, 'duration': 100, 'average view duration': 31},
              {'title': 'Python Classes: everything you need to know', 'views': 161_845, 'years': 2,
               'likes': 5529,'click-through rate': 23.2, 'duration': 34, 'average view duration': 9},
              {'title': 'Object Oriented Programming in Python', 'views': 233_498, 'years': 2,
               'likes': 8166,'click-through rate': 33.8, 'duration': 47, 'average view duration': 13},
              {'title': 'Learn Python - Full Course for Beginners', 'views': 38_003_572, 'years': 4,
               'likes': 927_483,'click-through rate': 24.0, 'duration': 267, 'average view duration': 47},
              {'title': 'Python tutorial #2: How to Use If Else Statements', 'views': 2_212_307, 'years': 4,
               'likes': 47_667,'click-through rate': 28.0, 'duration': 20, 'average view duration': 8},
              ]

while (search_term := input('Search videos (Enter \'q\' to quit): ')) != 'q':
    recommends = []
    views_per_year_min = 100_000  # minimum views per year
    likes_per_year_min = 2000 # minimum likes per year
    ctr_min = 30.0  # minimum click-through rate
    avg_dur_ratio_min = .25  # minimum ratio of average view duration to video duration

    for video in video_data:
        for (k, v) in video.items():
            if k == 'title' and v.lower().find(search_term.lower()) >= 0:
                avg_dur_ratio = (video['average view duration'] / video['duration'])
                avg_dur_ratio = round(avg_dur_ratio, 2)
                views_per_year = video.get('views') // video.get('years')
                likes_per_year = video.get('likes') // video.get('years')
                if views_per_year >= views_per_year_min and video['click-through rate'] >= ctr_min \
                        and avg_dur_ratio >= avg_dur_ratio_min and likes_per_year >= likes_per_year_min:
                    recommends.append(video)

    if len(recommends) > 0:
        print('Videos to recommend:')
        for video in recommends:
            print(video['title'])
    else:
        print('Videos meeting recommendation criteria not found.')
        # or recommend videos meeting another set of recommendation criteria

print('Bye!')

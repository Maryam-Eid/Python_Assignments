# 1
def get_score(**subjects):
    for key, value in subjects.items():
        print(f"{key} => {value}")


get_score(Math=90, Science=80, Language=70)
get_score(Logic=70, Problems=60)


# 2
def get_people_scores(*name, **subjects):
    if subjects:
        if name:
            print(f"Hello {name[0]} This Is Your Score Table:")

        for key, value in subjects.items():
            print(f"{key} => {value}")
    else:
        print(f"Hello {name[0]} You Have No Scores To Show")


get_people_scores("Osama", Math=90, Science=80, Language=70)
get_people_scores("Mahmoud", Logic=70, Problems=60)
get_people_scores(Logic=70, Problems=60)
get_people_scores("Ahmed")

# 3
scores_list = {
    "Math": 90,
    "Science": 80,
    "Language": 70
}


def get_the_scores(*name, **subjects):
    if subjects:
        if name:
            print(f"Hello {name[0]} This Is Your Score Table:")

        for key, value in subjects.items():
            print(f"{key} => {value}")
    else:
        print(f"Hello {name[0]} You Have No Scores To Show")


get_the_scores("Osama", **scores_list)
get_the_scores("Osama")
get_the_scores(**scores_list)

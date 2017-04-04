import movie_details
import fresh_tomatoes
# importing movie_details as the parent class which
# contains all the instance methods and variables
# importing fresh_tomatoes to create HTMP webpages

iron_man = movie_details.Movie(
    "Iron Man 1",
    "A billionaire industrialist and genius inventor, "
    "Tony Stark (Robert Downey Jr.), "
    "is conducting weapons tests overseas, but terrorists "
    "kidnap him to force him to "
    "build a devastating weapon. Instead, he builds an "
    "armored suit and upends his "
    "captors. Returning to America, Stark refines the "
    "suit and uses it to combat crime and terrorism",
    "https://upload.wikimedia.org/wikipedia/en/7/70/"
    "Ironmanposter.JPG",
    "https://www.youtube.com/watch?v=XWWd6p2JHKo")
# print(iron_man.storyline)

iron_man_2 = movie_details.Movie(
    "Iron Man 2",
    "With the world now aware that he is Iron Man, "
    "billionaire inventor Tony Stark (Robert Downey Jr.) "
    "faces pressure from all sides to share his technology "
    "with the military. He is reluctant to divulge the secrets "
    "of his armored suit, fearing the information will fall "
    "into the wrong hands. With Pepper Potts (Gwyneth Paltrow) "
    "and Rhodey Rhodes (Don Cheadle) by his side, Tony must "
    "forge new alliances and confront a powerful new enemy.",
    "https://fromthefourthrow.files.wordpress.com/2014/02/"
    "iron-man-2-cast-collage-movie-poster-gb2425.jpg",
    "https://www.youtube.com/watch?v=BoohRoVA9WQ")
# print(iron_man_2.title)

iron_man_3 = movie_details.Movie(
    "Iron Man 3",
    "Plagued with worry and insomnia since saving New York "
    "from destruction, Tony Stark (Robert Downey Jr.), now, "
    "is more dependent on the suits that give him his Iron "
    "Man persona -- so much so that every aspect of his life "
    "is affected, including his relationship with Pepper "
    "(Gwyneth Paltrow). After a malevolent enemy known as "
    "the Mandarin (Ben Kingsley) reduces his personal world "
    "to rubble, Tony must rely solely on instinct and "
    "ingenuity to avenge his losses and protect the people he loves",
    "https://images-na.ssl-images-amazon.com/images/M/MV5B"
    "MTkzMjEzMjY1M15BMl5BanBnXkFtZTcwNTMxOTYyOQ@@._V1_UY1200_"
    "CR105,0,630,1200_AL_.jpg",
    "https://www.youtube.com/watch?v=oYSD2VQagc4")
# print(iron_man_3.storyline)

avengers_1 = movie_details.Movie(
    "The Avengers",
    "The agency is a who's who of Marvel Super Heroes, with Iron "
    "Man, The Incredible Hulk, Thor, Captain America, Hawkeye and "
    "Black Widow. When global security is threatened by Loki and "
    "his cohorts, Nick Fury and his team will need all their "
    "powers to save the world from disaster.",
    "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers"
    "2012Poster.jpg",
    "https://www.youtube.com/watch?v=eOrNdBpGMv8")

avengers_2 = movie_details.Movie(
    "Avengers: Age Of Ultron",
    "When Tony Stark (Robert Downey Jr.) jump-starts a dormant "
    "peacekeeping program, things go terribly awry, forcing him, "
    "Thor (Chris Hemsworth), the Incredible Hulk (Mark Ruffalo) "
    "and the rest of the Avengers to reassemble. As the fate of "
    "Earth hangs in the balance, the team is put to the ultimate "
    "test as they battle Ultron, a technological terror hell-bent "
    "on human extinction. Along the way, they encounter two "
    "mysterious and powerful newcomers, Pietro and Wanda Maximoff.",
    "http://images6.fanpop.com/image/photos/37300000/Avengers-2-"
    "Age-of-Ultron-the-avengers-37328228-380-500.jpg",
    "https://www.youtube.com/watch?v=tmeOjFno6Do")

captain_america_1 = movie_details.Movie(
    "Captain America: The First Avenger",
    "Set predominantly during World War II, Captain America: The "
    "First Avenger tells the story of Steve Rogers, a sickly man "
    "from Brooklyn who is transformed into super-soldier Captain "
    "America and must stop the Red Skull, who intends to use an "
    "artifact called the Tesseract as an energy-source for world domination.",
    "https://smurfdok.files.wordpress.com/2011/07/captain-america-"
    "movie-2011-photo-1-l.jpg",
    "https://www.youtube.com/watch?v=JerVrbLldXw")

captain_america_2 = movie_details.Movie(
    "Captain America: The Winter Soldier",
    "After the cataclysmic events in New York with his fellow "
    "Avengers, Steve Rogers, aka Captain America (Chris Evans), "
    "lives in the nation's capital as he tries to adjust to modern "
    "times. An attack on a S.H.I.E.L.D. colleague throws Rogers "
    "into a web of intrigue that places the whole world at risk. "
    "Joining forces with the Black Widow (Scarlett Johansson) and "
    "a new ally, the Falcon, Rogers struggles to expose an ever-"
    "widening conspiracy, but he and his team soon come up against "
    "an unexpected enemy.", "http://cdn3-www.comingsoon.net/assets/"
    "uploads/1970/01/file_"
    "589355_captain-america-2-winter-soldier-character-poster.jpg",
    "https://www.youtube.com/watch?v=7SlILk2WMTI")

captain_america_3 = movie_details.Movie(
    "Captain America: Civil War",
    "Political pressure mounts to install a system of accountability "
    "when the actions of the Avengers lead to collateral damage. The "
    "new status quo deeply divides members of the team. Captain America "
    "(Chris Evans) believes superheroes should remain free to defend "
    "humanity without government interference. Iron Man (Robert Downey Jr.) "
    "sharply disagrees and supports oversight. As the debate escalates into "
    "an all-out feud, Black Widow (Scarlett Johansson) and Hawkeye "
    "(Jeremy Renner) must pick a side.",
    "http://www.desktopimages.org/pictures/2015/1126/1/captain-america-3"
    "-civil-war-marvel-superhero-action-fighting-1cacw-warrior-sci-fi-"
    "avengers-poster-background-354820.jpg",
    "https://www.youtube.com/watch?v=YqcfOKaIwqY")
# captain_america_3.run_youtube_trailer()

# create a list of all the movie objects defined above
movie_list = [
    iron_man,
    iron_man_2,
    iron_man_3,
    avengers_1,
    avengers_2,
    captain_america_1,
    captain_america_2,
    captain_america_3]

# calling fresh_tomatoes method to create a HTML webpage with these movies
fresh_tomatoes.open_movies_page(movie_list)

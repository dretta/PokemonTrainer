Pokemon Trainer is Machine Learning extension of Twitch Plays Pokemon Battle Revolution.

Development (To-Do) Plan:

* Data Retrieval: Implemented example stream to image sequence, will be revisited later in development.

* Pre-processing 1 (Image to Text): WIP

* Pre-processing 2 (Text to Feature)

* Model Training

* Model Testing

* Integration (optional)

* Refactoring/Extras?

Requirements (will move this to requirements file):

* A Linux Distribution, Ubuntu is recommended

* Python 3 (This is a python project after all...)

* Streamlink ( https://github.com/streamlink/streamlink )

* Curl (`sudo apt install curl`)

* ffmpeg ( https://ffmpeg.org )

* Others as they're added to the project...


Q&A:

* What is Twitch Plays Pokemon? (abbreviated as TPP)

Short Answer: Pokemon games where the input is "crowd-sourced"
Long Answer: https://en.wikipedia.org/wiki/Twitch_Plays_Pokemon

* What is TPP Battle Revolution?

A specific TPP game. Unlike most other Pokemon games, this one is similar to an 2-player arcade fighter game,
but with Pokemon. Pokemon are randomly generated for 3-vs-3 battles, players choose a side and collectively
choose their actions.

* How is Pokemon Trainer an extension of TPP Battle Revolution?

My goal for Pokemon Trainer is to create a new mode for TPP Battle Revolution. This mode is similar to the other TPP
games such that players will be working together against a "CPU". However this CPU will actually be making its
decisions based off a machine learning algorithm.

* How do you plan on doing this?

Initially I need data to work with, there are currently two sources I can use. First is the TPP match details API,
second is the live stream itself. However both of these are not programmer friendly data. Pre-processing the data will
be needed (especially the latter source).

At this point I should have access to the Pokemon that are being used in a battle, and all the attributes that come
with them. From here the situation of the match being the features for the ML model and the moves (or pokemon change)
being the labels. With the right classification algorithm, the AI should be able to be 'trained' in selecting the
right actions.

With an experienced AI, it should be ready to do battle with other players! However integrating this with TPP might be
a challenge. It's not just I'm unfamiliar with the entire TPP backend (I don't believe it's open sourced), but TPP
development might come with it's own problems, technical or otherwise. Because of this, I consider integration to be
an optional development plan. I'll somehow create to 'test' the model, I'm putting more thought into this.

* Why does something here seem strange?

Well to tell you the truth, I'm just winging this. I don't have much formal education on AI/ML and I'm working with
some of this software for the first time. I don't know if this is completable or not, but I'll sure try.

* What's with the unrelated pieces of code?

The structure of this project was made in https://github.com/kennethreitz/samplemod please note that some sample
code still exists here.

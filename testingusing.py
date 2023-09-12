import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import joblib

global tfidf 
tfidf = joblib.load("tfidf.joblib")
global pac
pac = joblib.load("pac.joblib")


sample = [
    '''
  Mittleman’s research indicates that this characterization of the educational gender gap is critically lacking in specificity. It is, in fact, straight males who tend to be mired in a scholastic morass. And the considerable academic progress that young women have charted since the advent of second-wave feminism has been largely restricted to the heterosexuals among them.

Benefit of adding sexuality questions to surveys
Mittleman was able to reach his striking research findings thanks to a move during President Barack Obama’s second term to add questions about sexual orientation to a trio of federally funded, nationally representative surveys. These major annual surveys — which focus on health, drug use and crime victimization — provided the sociologist with information regarding nearly half a million Americans’ diplomas.

Additionally, the National Center for Education Statistics’ High School Longitudinal Study posed questions about sexuality for the first time to the cohort it followed between 2009 and 2017. From this, Mittleman mined a trove of data including 15,270 students’ high school and undergraduate transcripts. 

The three surveys of American adults consistently indicated that gay men are far more likely than straight men to have graduated from high school or college, with just over half of gay men having earned a college degree, compared with about 35 percent of straight men. Some 6 percent of gay men have a Ph.D., J.D. or M.D. — a rate 50 percent higher than that of straight men. Mittleman found that gay men’s considerably higher levels of educational attainment hold even after taking into account differences in men’s race and birth cohorts. What’s more, gay men’s college graduation rate dramatically bests even that of straight women, about one-third of whom have a bachelor’s degree.

The longitudinal survey showed that compared with their straight male peers, gay males earned higher GPAs in high school and college, enrolled in harder classes, took school more seriously, had more academically minded friends and had a much lower rate of ever dropping out for a month or more. In stark contrast, these performance disparities were largely reversed when comparing lesbians with straight girls. Most strikingly, 26 percent of lesbians reported at least one dropout period, compared with 15 percent of heterosexual females.

The U.S. lesbian population’s overall college graduation rate, which ranged between 41 percent and 47 percent in the three survey studies, is significantly higher than that of straight women. But Mittleman found this advantage was limited almost entirely to white lesbians, and among women born more recently, gay women’s educational edge has eroded.  

Historically, girls have received better grades than boys. But during much of the 20th century, societal constraints — including the predominant expectation that young women would become wives and mothers and not pursue careers — suppressed their graduation
''']

new_vec = tfidf.transform(sample)
print(pac.predict(new_vec))
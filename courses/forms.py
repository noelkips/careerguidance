from django import forms

# iterable
QUESTION_1_CHOICES = (
    ("1", "practical, athletic, straightforward, a nature lover, curious about the physical world"),
    ("2", "inquisitive, analytical, scientific, observant, logical, precise"),
    ("3", "creative, intuitive, imaginative, innovative, sensitive, an individualist"),
    ("4", "friendly, helpful, idealistic, insightful about people, outgoing with others, understanding"),
    ("5", "self-confident, assertive, sociable, persuasive, enthusiastic, energetic"),
    ("6", "organized, accurate with details and numbers,  methodical, conscientious about facts, efficient")
)
QUESTION_2_CHOICES = (
    ("1",
     "fix electrical things, solve mechanical problems, pitch a tent, play a sport, read a blueprint, operate tools "
     "and machinery"),
    ("2",
     "think abstractly, solve math problems, understand physics theories, do complex calculations, use a microscope, "
     "interpret formulas"),
    ("3",
     "sketch, draw, paint, use intuition, play a musical instrument, write stories, poetry, music, develop new ideas"),
    ("4",
     "teach or train others, express your feelings clearly, lead a group discussion, mediate disputes, work well in "
     "groups or teams"),
    ("5", "initiate projects, convince people to do things your way, sell things or promote ideas"),
    ("6",
     "work well within an authority system or organization, write reports, keep accurate records, use a computer "
     "terminal")
)

QUESTION_3_CHOICES = (
    ("1", "work outdoors, be physically active, work with your hands, build things"),
    ("2", "explore ideas, use computers, work independently, perform lab experiments, read scientific or technical, "
          "analyze data"),
    ("3", "solve problems in original ways, read fiction, plays, poetry, act, entertain,  take photographs"),
    ("4",
     "help people with their problems, lead groups, use communication skills, teach or train others, provide support"),
    ("5", "make decisions affecting others, give speeches or talks, debate, take risks, organize and lead others"),
    ("6",
     "follow defined procedures, make charts, tables and graphs, work with numbers, classify and organize information")
)
QUESTION_4_CHOICES = (
    ("1", "riding, gardening, playing, reading inventions, exploration of new things"),
    ("2", "solving puzzles, adventuring, reading about facts, watching tutorials, exploring"),
    ("3", "acting, dancing, chatting, watching, drawing, designing things"),
    ("4", "teaching, reading, guiding others, travelling"),
    ("5", "reading business related books, watching business related programs, politics, walking"),
    ("6", "party planning, hosting, reading accounts related articles")
)
QUESTION_5_CHOICES = (
    ("1", "engineer, technician, surveyor, equipment operator, pilot, driver"),
    ("2", "solving puzzles, adventuring, reading about facts, watching tutorials, exploringany job relating to "
          "computing, data analyst,actuarial consultant, network operatiion related jobs, risk manager, archaeologist"),
    ("3", "actor/ actress, author, artist, musician, designer, wedding planner"),
    ("4", "teaching, counselor, public health officer, coach, librarian, Nurse"),
    ("5", "consultant, politician, procurement officer, project manager"),
    ("6", "accountant, bank manager, auditor, finance manager, police, receptionist, office manager")
)
QUESTION_6_BEST_SUBJECT = (
    ('1', 'maths'),
    ('2', 'english'),
    ('3', 'kiswahili'),
    ('4', 'chemistry'),
    ('5', 'physics'),
    ('6', 'biology'),
    ('7', 'religion'),
    ('8', 'business studies'),
    ('9', 'agriculture'),
    ('10', 'history and government'),
    ('11', 'geography'),
    ('12', 'computer studies'),
    ('13', 'home science'),
)


# creating a form
class QuestionsForm(forms.Form):
    question_one = forms.ChoiceField(choices=QUESTION_1_CHOICES)
    question_two = forms.ChoiceField(choices=QUESTION_2_CHOICES)
    question_three = forms.ChoiceField(choices=QUESTION_3_CHOICES)
    question_four = forms.ChoiceField(choices=QUESTION_4_CHOICES)
    question_five = forms.ChoiceField(choices=QUESTION_5_CHOICES)
    Five_Which_subject_do_you_like = forms.ChoiceField(choices=QUESTION_6_BEST_SUBJECT)
    Six_Which_subject_do_you_like = forms.ChoiceField(choices=QUESTION_6_BEST_SUBJECT)
    Seven_Which_subject_do_you_like = forms.ChoiceField(choices=QUESTION_6_BEST_SUBJECT)



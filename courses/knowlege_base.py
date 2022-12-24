
# knoledge base
from django.shortcuts import render

def consult(request):
    #This function defines the knowledge base for different careers
    #Input:
    #     one: first question that define user's personality
    #     two: second question that define user's personality
    #     third: third question that define user's personality
    #     fourth: fourth question that define user's personality
    #     five: 5th question that define user's personality
    #     sub_1: first subject that user likes
    #     sub_2: second subject that user likes
    #     sub_3: third subject that user likes
    #OUTPUT:
    #     Dictionary:
    #            has career type
    #            recommended courses (between 1 and 10 depending on the course) or
    #            empty is none match

    #defines rules for realistic careers
    context = {}
    courses = {}
    if request.GET:
        one = int(request.GET['question_one'])
        two = int(request.GET['question_two'])
        three = int(request.GET['question_three'])
        four = int(request.GET['question_four'])
        five = int(request.GET['question_five'])
        sub_1 = int(request.GET['question_six'])
        sub_2 = int(request.GET['question_seven'])
        sub_3 = int(request.GET['question_eight'])
    a = (one == 1 and two == 1 and three == 1 and four == 1 and five == 1) or (
                one == 1 and two == 1 and three == 1 and four == 1 and five) or (
                    one == 1 and two == 1 and three == 1 and four and five == 1) or (
                    one == 1 and two == 1 and three and four == 1 and five == 1) or (
                    one == 1 and two and three == 1 and four == 1 and five == 1) or (
                    one and two == 1 and three == 1 and four == 1 and five == 1) or (
                    one == 1 and two == 1 and three == 1 and four and five) or (
                    one == 1 and two == 1 and three and four == 1 and five) or (
                    one == 1 and two and three == 1 and four == 1 and five) or (
                    one and two == 1 and three == 1 and four == 1 and five) or (
                    one == 1 and two == 1 and three and four and five == 1) or (
                    one == 1 and two and three == 1 and four and five == 1) or (
                    one == 1 and two == 1 and three and four == 1 and five) or (
                    one == 1 and two and three and four == 1 and five == 1) or (
                    one and two and three == 1 and four == 1 and five == 1) or (
                    one and two == 1 and three == 1 and four == 1 and five) or (
                    one and two == 1 and three == 1 and four and five == 1) or (
                    one and two == 1 and three and four == 1 and five == 1)

    #difines rules for investigative careers
    b = (one == 2 and two == 2 and three == 2 and four == 2 and five == 2) or (
                one == 2 and two == 2 and three == 2 and four == 2 and five) or (
                    one == 2 and two == 2 and three == 2 and four and five == 2) or (
                    one == 2 and two == 2 and three and four == 2 and five == 2) or (
                    one == 2 and two and three == 2 and four == 2 and five == 2) or (
                    one and two == 2 and three == 2 and four == 2 and five == 2) or (
                    one == 2 and two == 2 and three == 2 and four and five) or (
                    one == 2 and two == 2 and three and four == 2 and five) or (
                    one == 2 and two and three == 2 and four == 2 and five) or (
                    one and two == 2 and three == 2 and four == 2 and five) or (
                    one == 2 and two == 2 and three and four and five == 2) or (
                    one == 2 and two and three == 2 and four and five == 2) or (
                    one == 2 and two == 2 and three and four == 2 and five) or (
                    one == 2 and two and three and four == 2 and five == 2) or (
                    one and two and three == 2 and four == 2 and five == 2) or (
                    one and two == 2 and three == 2 and four == 2 and five) or (
                    one and two == 2 and three == 2 and four and five == 2) or (
                    one and two == 2 and three and four == 2 and five == 2)

    #difines rules for artistic careers
    c = (one == 3 and two == 3 and three == 3 and four == 3 and five == 3) or (
                one == 3 and two == 3 and three == 3 and four == 3 and five) or (
                    one == 3 and two == 3 and three == 3 and four and five == 3) or (
                    one == 3 and two == 3 and three and four == 3 and five == 3) or (
                    one == 3 and two and three == 3 and four == 3 and five == 3) or (
                    one and two == 3 and three == 3 and four == 3 and five == 3) or (
                    one == 3 and two == 3 and three == 3 and four and five) or (
                    one == 3 and two == 3 and three and four == 3 and five) or (
                    one == 3 and two and three == 3 and four == 3 and five) or (
                    one and two == 3 and three == 3 and four == 3 and five) or (
                    one == 3 and two == 3 and three and four and five == 3) or (
                    one == 3 and two and three == 3 and four and five == 3) or (
                    one == 3 and two == 3 and three and four == 3 and five) or (
                    one == 3 and two and three and four == 3 and five == 3) or (
                    one and two and three == 3 and four == 3 and five == 3) or (
                    one and two == 3 and three == 3 and four == 3 and five) or (
                    one and two == 3 and three == 3 and four and five == 3) or (
                    one and two == 3 and three and four == 3 and five == 3)

    #difines rules for social careers
    d = (one == 4 and two == 4 and three == 4 and four == 4 and five == 4) or (
                one == 4 and two == 4 and three == 4 and four == 4 and five) or (
                    one == 4 and two == 4 and three == 4 and four and five == 4) or (
                    one == 4 and two == 4 and three and four == 4 and five == 4) or (
                    one == 4 and two and three == 4 and four == 4 and five == 4) or (
                    one and two == 4 and three == 4 and four == 4 and five == 4) or (
                    one == 4 and two == 4 and three == 4 and four and five) or (
                    one == 4 and two == 4 and three and four == 4 and five) or (
                    one == 4 and two and three == 4 and four == 4 and five) or (
                    one and two == 4 and three == 4 and four == 4 and five) or (
                    one == 4 and two == 4 and three and four and five == 4) or (
                    one == 4 and two and three == 4 and four and five == 4) or (
                    one == 4 and two == 4 and three and four == 4 and five) or (
                    one == 4 and two and three and four == 4 and five == 4) or (
                    one and two and three == 4 and four == 4 and five == 4) or (
                    one and two == 4 and three == 4 and four == 4 and five) or (
                    one and two == 4 and three == 4 and four and five == 4) or (
                    one and two == 4 and three and four == 4 and five == 4)

    #difines rules for enterprising careers
    e = (one == 5 and two == 5 and three == 5 and four == 5 and five == 5) or (
                one == 5 and two == 5 and three == 5 and four == 5 and five) or (
                    one == 5 and two == 5 and three == 5 and four and five == 5) or (
                    one == 5 and two == 5 and three and four == 5 and five == 5) or (
                    one == 5 and two and three == 5 and four == 5 and five == 5) or (
                    one and two == 5 and three == 5 and four == 5 and five == 5) or (
                    one == 5 and two == 5 and three == 5 and four and five) or (
                    one == 5 and two == 5 and three and four == 5 and five) or (
                    one == 5 and two and three == 5 and four == 5 and five) or (
                    one and two == 5 and three == 5 and four == 5 and five) or (
                    one == 5 and two == 5 and three and four and five == 5) or (
                    one == 5 and two and three == 5 and four and five == 5) or (
                    one == 5 and two == 5 and three and four == 5 and five) or (
                    one == 5 and two and three and four == 5 and five == 5) or (
                    one and two and three == 5 and four == 5 and five == 5) or (
                    one and two == 5 and three == 5 and four == 5 and five) or (
                    one and two == 5 and three == 5 and four and five == 5) or (
                    one and two == 5 and three and four == 5 and five == 5)

    #difines rules for convectional careers
    f = (one == 6 and two == 6 and three == 6 and four == 6 and five == 6) or (
                one == 6 and two == 6 and three == 6 and four == 6 and five) or (
                    one == 6 and two == 6 and three == 6 and four and five == 6) or (
                    one == 6 and two == 6 and three and four == 6 and five == 6) or (
                    one == 6 and two and three == 6 and four == 6 and five == 6) or (
                    one and two == 6 and three == 6 and four == 6 and five == 6) or (
                    one == 6 and two == 6 and three == 6 and four and five) or (
                    one == 6 and two == 6 and three and four == 6 and five) or (
                    one == 6 and two and three == 6 and four == 6 and five) or (
                    one and two == 6 and three == 6 and four == 6 and five) or (
                    one == 6 and two == 6 and three and four and five == 6) or (
                    one == 6 and two and three == 6 and four and five == 6) or (
                    one == 6 and two == 6 and three and four == 6 and five) or (
                    one == 6 and two and three and four == 6 and five == 6) or (
                    one and two and three == 6 and four == 6 and five == 6) or (
                    one and two == 6 and three == 6 and four == 6 and five) or (
                    one and two == 6 and three == 6 and four and five == 6) or (
                    one and two == 6 and three and four == 6 and five == 6)

    #difines rules for specific realistic careers
       # this follows the fact that one belong to realistic career but differs in subjecs
    if (a and sub_1 == 6 and sub_2 == 1 and sub_3 == 5) or (a and sub_1 == 6 and sub_2 == 5 and sub_3 == 1) or (
                a and sub_1 == 5 and sub_2 == 6 and sub_3 == 1) or (a and sub_1 == 5 and sub_2 == 1 and sub_3 == 6) or (
                a and sub_1 == 1 and sub_2 == 6 and sub_3 == 5) or (
                a and sub_1 == 1 and sub_2 == 5 and sub_3 == 6) or (a and sub_1 == 6 and sub_2 == 1 and sub_3 == 4) or (
                a and sub_1 == 6 and sub_2 == 4 and sub_3 == 1) or (
                a and sub_1 == 1 and sub_2 == 6 and sub_3 == 4) or (a and sub_1 == 1 and sub_2 == 4 and sub_3 == 6) or (
                a and sub_1 == 4 and sub_2 == 6 and sub_3 == 1) or (
                a and sub_1 == 4 and sub_2 == 1 and sub_3 == 6) or (
                a and sub_1 == 6 and sub_2 == 1 and sub_3 == 11) or (
                a and sub_1 == 6 and sub_2 == 11 and sub_3 == 1) or (
                a and sub_1 == 1 and sub_2 == 6 and sub_3 == 11) or (
                a and sub_1 == 1 and sub_2 == 11 and sub_3 == 6) or (
                a and sub_1 == 11 and sub_2 == 1 and sub_3 == 6) or (
                a and sub_1 == 11 and sub_2 == 6 and sub_3 == 1) or (
                a and sub_1 == 6 and sub_2 == 1 and sub_3 == 7) or (a and sub_1 == 6 and sub_2 == 7 and sub_3 == 1) or (
                a and sub_1 == 1 and sub_2 == 6 and sub_3 == 7) or (a and sub_1 == 1 and sub_2 == 7 and sub_3 == 6) or (
                a and sub_1 == 7 and sub_2 == 1 and sub_3 == 6) or (a and sub_1 == 7 and sub_2 == 6 and sub_3 == 1):
            career_type = "Realistic career type"
            course_1 = "Physical Education & Recreation"
            course_2 = "Physical Education & Sports"
            course_3 = "Exercise And Sport Science"
            course_4 = "Cosmetology & Beauty Science"
            course_5 = "Health Promotion & Sports Science"
            course_6 = " Medicine & Bachelor Of Surgery,  Dental Surgery"
            course_7 = "Agriculture and human ecology extension"
            course_8 = "Food Science& Technology"
            course_9 = "Food security, Nutrition and dietetics "
            course_10 = ''
     #difines rules for specific realistic careers
       # this follows the fact that one belong to realistic career but differs in subjecs
    elif (a and sub_1 == 1 and sub_2 == 5 and sub_3 == 11) or (a and sub_1 == 1 and sub_2 == 11 and sub_3 == 5) or (
                a and sub_1 == 11 and sub_2 == 1 and sub_3 == 5) or (
                a and sub_1 == 11 and sub_2 == 5 and sub_3 == 1) or (
                a and sub_1 == 5 and sub_2 == 1 and sub_3 == 11) or (
                a and sub_1 == 5 and sub_2 == 11 and sub_3 == 1) or (
                a and sub_1 == 1 and sub_2 == 5 and sub_3 == 7) or (a and sub_1 == 1 and sub_2 == 7 and sub_3 == 5) or (
                a and sub_1 == 7 and sub_2 == 1 and sub_3 == 5) or (
                a and sub_1 == 7 and sub_2 == 5 and sub_3 == 1) or (
                a and sub_1 == 5 and sub_2 == 1 and sub_3 == 7) or (a and sub_1 == 5 and sub_2 == 7 and sub_3 == 1):
            career_type = "Realistic career type"
            course_1 = "Bachelor Of Tech. Education (Mechanical Engineering Option)"
            course_2 = "Bachelor Of Tech. Education ( Building Construction Option)"
            course_3 = "Bachelor Of Tech. Education ( Electrical & Electronic Option)"
            course_4 = ''
            course_5 = ''
            course_6 = ''
            course_7 = ''
            course_7 = ''
            course_8 = ''
            course_9 = ''
            course_10 = ''
     #difines rules for specific realistic careers
       # this follows the fact that one belong to realistic career but differs in subjecs
    elif (a and sub_1 == 1 and sub_2 == 5 and sub_3 == 4) or (a and sub_1 == 1 and sub_2 == 5 and sub_3 == 4) or (
                a and sub_1 == 4 and sub_2 == 1 and sub_3 == 5) or (
                a and sub_1 == 4 and sub_2 == 5 and sub_3 == 1) or (
                a and sub_1 == 5 and sub_2 == 1 and sub_3 == 4) or (
                a and sub_1 == 5 and sub_2 == 4 and sub_3 == 1):
            career_type = "Realistic career type"
            course_1 = " Microprocessor Technology And Instrumentation"
            course_2 = "Computer &Electronic Systems"
            course_3 = "Automotive Technology /Mechanical technology"
            course_4 = "Electronic & Computer Engineering /Electronics"
            course_5 = "Building & Civil Technology / Building Construction"
            course_6 = " Applied Bioengineering / Applied Optics & Lasers"
            course_7 = "Medical Engineering /Biomedical Engineering"
            course_8 = "Renewable Energy, Environmental Physics, Biofuels Technology"
            course_9 = "Mechanical Ventilation & Air Conditioning"
            course_10 = "Industrial Technology"

     #difines rules for specific realistic careers
       # this follows the fact that one belong to realistic career but differs in subjecs
    elif (a and sub_1 == 2 and sub_2 == 4 and sub_3 == 1) or (a and sub_1 == 2 and sub_2 == 1 and sub_3 == 4) or (
                a and sub_1 == 4 and sub_2 == 1 and sub_3 == 2) or (
                a and sub_1 == 4 and sub_2 == 2 and sub_3 == 1) or (
                a and sub_1 == 1 and sub_2 == 2 and sub_3 == 4) or (
                a and sub_1 == 1 and sub_2 == 4 and sub_3 == 2) or (
                a and sub_1 == 2 and sub_2 == 4 and sub_3 == 5) or (a and sub_1 == 2 and sub_2 == 5 and sub_3 == 4) or (
                a and sub_1 == 4 and sub_2 == 5 and sub_3 == 2) or (
                a and sub_1 == 4 and sub_2 == 2 and sub_3 == 5) or (
                a and sub_1 == 5 and sub_2 == 2 and sub_3 == 4) or (
                a and sub_1 == 5 and sub_2 == 4 and sub_3 == 2) or (
                a and sub_1 == 3 and sub_2 == 4 and sub_3 == 1) or (
                a and sub_1 == 3 and sub_2 == 1 and sub_3 == 4) or (
                a and sub_1 == 4 and sub_2 == 1 and sub_3 == 3) or (
                a and sub_1 == 4 and sub_2 == 3 and sub_3 == 1) or (
                a and sub_1 == 1 and sub_2 == 3 and sub_3 == 4) or (
                a and sub_1 == 1 and sub_2 == 4 and sub_3 == 3) or (
                a and sub_1 == 3 and sub_2 == 4 and sub_3 == 5) or (a and sub_1 == 3 and sub_2 == 5 and sub_3 == 4) or (
                a and sub_1 == 4 and sub_2 == 5 and sub_3 == 3) or (
                a and sub_1 == 4 and sub_2 == 3 and sub_3 == 5) or (
                a and sub_1 == 5 and sub_2 == 3 and sub_3 == 4) or (
                a and sub_1 == 5 and sub_2 == 4 and sub_3 == 3):
            career_type = "Realistic career type"
            course_1 = " Mechanical Engineering / Production Engineering /  Industrial Engineering"
            course_2 = "Civil Engineering/ Manufacturing Engineering"
            course_3 = "Petroleum Engineering /Marine Engineering"
            course_4 = " Electrical And Electronic Engineering /   Petroleum Exploration"
            course_5 = "Aeronautical Engineering / Aerospace Engineering"
            course_6 = " Industrial & Textile Engineering / Energy Engineering"
            course_7 = "Mechatronic Engineering / Electrical & Communication Engineering"
            course_8 = "Chemical & Process / Mechanical / Production Engineering"
            course_9 = "Mining Physics / Mining & Mineral Processing Engineering"
            course_10 = "Civil /Structural Engineering /Agricultural & Bio-Systems Engineering"

     #difines rules for specific realistic careers
       # this follows the fact that one belong to realistic career but differs in subjecs
    elif a and sub_2 and sub_2 and sub_3:
            career_type = "Realistic career type"
            course_1 = "Electrical & Electronic’s Engineering"
            course_2 = "Physical Education & Recreation"
            course_3 = "Physical Education & Sports"
            course_4 = "Dental Surgery"
            course_5 = "Medicine & Bachelor Of Surgery"
            course_6 = "Electrical And Electronic Engineering"
            course_7 = "Instrumentation And Control Engineering"
            course_8 = "Microprocessor Technology And Instrumentation"
            course_9 = "Telecommunication & Inform. Technology"
            course_10 = "Mechanical Engineering"


     #difines rules for specific invesigative careers careers
       # this follows the fact that one belong to invesigative career but differs in subjecs
    elif (b and sub_1 == 1 and sub_2 == 5 and sub_3 == 6) or (b and sub_1 == 1 and sub_2 == 6 and sub_3 == 5) or (
                b and sub_1 == 6 and sub_2 == 1 and sub_3 == 5) or (
                b and sub_1 == 6 and sub_2 == 5 and sub_3 == 1) or (
                b and sub_1 == 5 and sub_2 == 1 and sub_3 == 6) or (
                b and sub_1 == 5 and sub_2 == 6 and sub_3 == 1) or (
                b and sub_1 == 1 and sub_2 == 5 and sub_3 == 11) or (
                b and sub_1 == 1 and sub_2 == 11 and sub_3 == 5) or (
                b and sub_1 == 11 and sub_2 == 5 and sub_3 == 1) or (
                b and sub_1 == 11 and sub_2 == 1 and sub_3 == 5) or (
                b and sub_1 == 5 and sub_2 == 1 and sub_3 == 11) or (
                b and sub_1 == 5 and sub_2 == 11 and sub_3 == 1) or (
                b and sub_1 == 1 and sub_2 == 5 and sub_3 == 7) or (
                b and sub_1 == 1 and sub_2 == 7 and sub_3 == 5) or (
                b and sub_1 == 7 and sub_2 == 1 and sub_3 == 5) or (
                b and sub_1 == 7 and sub_2 == 5 and sub_3 == 1) or (
                b and sub_1 == 5 and sub_2 == 1 and sub_3 == 7) or (
                b and sub_1 == 5 and sub_2 == 7 and sub_3 == 1):
            career_type = "Investigative career type"
            course_1 = "Software Engineering / Software Development"
            course_2 = "Information Technology / Business Information Technology"
            course_3 = "Computer Science / Networks & Communication Systems"
            course_4 = 'Communication & Computer Networks'
            course_5 = 'Applied Physics & Computer Science'
            course_6 = 'Engineering Physics / Business Computing'
            course_7 = 'Computer Security & Forensics'
            course_7 = ' Information Security & Forensics'
            course_8 = 'Cloud Computing & Information Security'
            course_9 = 'Statistics & Information Technology'
            course_10 = 'statistics & Computer Science  '

    #difines rules for specific invesigative careers careers
       # this follows the fact that one belong to invesigative career but differs in subjecs
    elif (b and sub_1 == 1 and sub_2 == 4 and sub_3 == 6) or (b and sub_1 == 1 and sub_2 == 6 and sub_3 == 4) or (
                b and sub_1 == 6 and sub_2 == 1 and sub_3 == 4) or (
                b and sub_1 == 6 and sub_2 == 4 and sub_3 == 1) or (
                b and sub_1 == 4 and sub_2 == 1 and sub_3 == 6) or (
                b and sub_1 == 4 and sub_2 == 6 and sub_3 == 1) or (b and sub_1 == 1 and sub_2 == 4 and sub_3 == 5) or (
                b and sub_1 == 1 and sub_2 == 5 and sub_3 == 4) or (
                b and sub_1 == 4 and sub_2 == 1 and sub_3 == 5) or (
                b and sub_1 == 4 and sub_2 == 5 and sub_3 == 1) or (
                b and sub_1 == 5 and sub_2 == 1 and sub_3 == 4) or (
                b and sub_1 == 5 and sub_2 == 4 and sub_3 == 1):
            career_type = "Investigative career type"
            course_1 = "Biological Science / Biochemistry/  Botany / Zoology  "
            course_2 = "Microbiology /  Biochemistry & Molecular Biology"
            course_3 = "Cellular & Molecular Biology, / Biotechnology and Biosafety"
            course_4 = 'Molecular Biology & Forensic Technology'
            course_5 = 'Biotechnology, Industrial Biotechnology, Medical Microbiology'
            course_6 = ' Industrial & Applied Chemistry /Forensic Science / Environmental Chemistry'
            course_7 = ' Medical Biochemistry / Medical Biotechnology'
            course_8 = 'Conservation Biology/ Forensic Biology'
            course_9 = ' Industrial Chemistry / Polymer Chemistry / Analytical Chemistry'
            course_10 = 'Engineering Physics / Technical & Applied Physics '

    #difines rules for specific invesigative careers careers
       # this follows the fact that one belong to invesigative career but differs in subjecs
    elif (b and sub_1 == 2 and sub_2 == 4 and sub_3 == 6) or (
                b and sub_1 == 2 and sub_2 == 6 and sub_3 == 4) or (
                b and sub_1 == 4 and sub_2 == 2 and sub_3 == 6) or (
                b and sub_1 == 4 and sub_2 == 6 and sub_3 == 2) or (
                b and sub_1 == 6 and sub_2 == 2 and sub_3 == 4) or (
                b and sub_1 == 6 and sub_2 == 4 and sub_3 == 2) or (b and sub_1 == 2 and sub_2 == 5 and sub_3 == 6) or (
                b and sub_1 == 2 and sub_2 == 6 and sub_3 == 5) or (
                b and sub_1 == 5 and sub_2 == 2 and sub_3 == 6) or (
                b and sub_1 == 5 and sub_2 == 6 and sub_3 == 2) or (
                b and sub_1 == 6 and sub_2 == 2 and sub_3 == 5) or (
                b and sub_1 == 6 and sub_2 == 5 and sub_3 == 2):
            career_type = "Investigative career type"
            course_1 = "Environmental Science / Animal Science / Animal Products Technology"
            course_2 = "Forestry / Crop Improvement And Protection"
            course_3 = "Leather Technology /  Soil Science (And Plant Nutrition)"
            course_4 = 'Nutraceutical Science And Technology / Energy & Environmental Technology'
            course_5 = 'Applied Aquatic Science / Fisheries And Oceanography'
            course_6 = 'Maritime studies / Marine Biology& Fisheries'
            course_7 = ' Utilization And Sustainability Of Arid-Lands (Usal)'
            course_8 = "Climate Change Adaptation/Sustainable Development"
            course_9 = 'Climate Change Adaptation/Sustainable Development '
            course_10 = 'Agricultural Biotechnology / Animal Health, Production and Processing'

    #difines rules for specific invesigative careers careers
       # this follows the fact that one belong to invesigative career but differs in subjecs
    elif (b and sub_1 == 2 and sub_2 == 1 and sub_3 == 11) or (
                b and sub_1 == 2 and sub_2 == 11 and sub_3 == 1) or (
                b and sub_1 == 11 and sub_2 == 1 and sub_3 == 2) or (
                b and sub_1 == 11 and sub_2 == 2 and sub_3 == 1) or (
                b and sub_1 == 2 and sub_2 == 1 and sub_3 == 11) or (
                b and sub_1 == 2 and sub_2 == 11 and sub_3 == 1) or (
                b and sub_1 == 3 and sub_2 == 1 and sub_3 == 11) or (
                b and sub_1 == 3 and sub_2 == 11 and sub_3 == 1) or (
                b and sub_1 == 11 and sub_2 == 1 and sub_3 == 3) or (
                b and sub_1 == 11 and sub_2 == 3 and sub_3 == 1) or (
                b and sub_1 == 3 and sub_2 == 1 and sub_3 == 11) or (
                b and sub_1 == 3 and sub_2 == 11 and sub_3 == 1) or (
                b and sub_1 == 2 and sub_2 == 1 and sub_3 == 7) or (
                b and sub_1 == 2 and sub_2 == 7 and sub_3 == 1) or (
                b and sub_1 == 7 and sub_2 == 1 and sub_3 == 2) or (
                b and sub_1 == 7 and sub_2 == 2 and sub_3 == 1) or (
                b and sub_1 == 2 and sub_2 == 1 and sub_3 == 7) or (
                b and sub_1 == 2 and sub_2 == 7 and sub_3 == 1) or (b and sub_1 == 3 and sub_2 == 1 and sub_3 == 7) or (
                b and sub_1 == 3 and sub_2 == 7 and sub_3 == 1) or (
                b and sub_1 == 7 and sub_2 == 1 and sub_3 == 3) or (
                b and sub_1 == 7 and sub_2 == 3 and sub_3 == 1) or (
                b and sub_1 == 3 and sub_2 == 1 and sub_3 == 7) or (
                b and sub_1 == 3 and sub_2 == 7 and sub_3 == 1) or (
                b and sub_1 == 2 and sub_2 == 5 and sub_3 == 11) or (
                b and sub_1 == 2 and sub_2 == 11 and sub_3 == 5) or (
                b and sub_1 == 11 and sub_2 == 5 and sub_3 == 2) or (
                b and sub_1 == 11 and sub_2 == 2 and sub_3 == 5) or (
                b and sub_1 == 2 and sub_2 == 5 and sub_3 == 11) or (
                b and sub_1 == 2 and sub_2 == 11 and sub_3 == 5) or (
                b and sub_1 == 3 and sub_2 == 5 and sub_3 == 11) or (
                b and sub_1 == 3 and sub_2 == 11 and sub_3 == 5) or (
                b and sub_1 == 11 and sub_2 == 5 and sub_3 == 3) or (
                b and sub_1 == 11 and sub_2 == 3 and sub_3 == 5) or (
                b and sub_1 == 3 and sub_2 == 5 and sub_3 == 11) or (
                b and sub_1 == 3 and sub_2 == 11 and sub_3 == 5) or (
                b and sub_1 == 2 and sub_2 == 5 and sub_3 == 7) or (
                b and sub_1 == 2 and sub_2 == 7 and sub_3 == 5) or (
                b and sub_1 == 7 and sub_2 == 5 and sub_3 == 2) or (
                b and sub_1 == 7 and sub_2 == 2 and sub_3 == 5) or (
                b and sub_1 == 2 and sub_2 == 5 and sub_3 == 7) or (
                b and sub_1 == 2 and sub_2 == 7 and sub_3 == 5) or (b and sub_1 == 3 and sub_2 == 5 and sub_3 == 7) or (
                b and sub_1 == 3 and sub_2 == 7 and sub_3 == 5) or (
                b and sub_1 == 7 and sub_2 == 5 and sub_3 == 3) or (
                b and sub_1 == 7 and sub_2 == 3 and sub_3 == 5) or (
                b and sub_1 == 3 and sub_2 == 5 and sub_3 == 7) or (
                b and sub_1 == 3 and sub_2 == 7 and sub_3 == 5) or (
                b and sub_1 == 2 and sub_2 == 6 and sub_3 == 11) or (
                b and sub_1 == 2 and sub_2 == 11 and sub_3 == 6) or (
                b and sub_1 == 11 and sub_2 == 6 and sub_3 == 2) or (
                b and sub_1 == 11 and sub_2 == 2 and sub_3 == 6) or (
                b and sub_1 == 2 and sub_2 == 6 and sub_3 == 11) or (
                b and sub_1 == 2 and sub_2 == 11 and sub_3 == 6) or (
                b and sub_1 == 3 and sub_2 == 6 and sub_3 == 11) or (
                b and sub_1 == 3 and sub_2 == 11 and sub_3 == 6) or (
                b and sub_1 == 11 and sub_2 == 6 and sub_3 == 3) or (
                b and sub_1 == 11 and sub_2 == 3 and sub_3 == 6) or (
                b and sub_1 == 3 and sub_2 == 6 and sub_3 == 11) or (
                b and sub_1 == 3 and sub_2 == 11 and sub_3 == 6) or (
                b and sub_1 == 2 and sub_2 == 6 and sub_3 == 7) or (
                b and sub_1 == 2 and sub_2 == 7 and sub_3 == 6) or (
                b and sub_1 == 7 and sub_2 == 6 and sub_3 == 2) or (
                b and sub_1 == 7 and sub_2 == 2 and sub_3 == 6) or (
                b and sub_1 == 2 and sub_2 == 6 and sub_3 == 7) or (
                b and sub_1 == 2 and sub_2 == 7 and sub_3 == 6) or (b and sub_1 == 3 and sub_2 == 6 and sub_3 == 7) or (
                b and sub_1 == 3 and sub_2 == 7 and sub_3 == 6) or (
                b and sub_1 == 7 and sub_2 == 6 and sub_3 == 3) or (
                b and sub_1 == 7 and sub_2 == 3 and sub_3 == 6) or (
                b and sub_1 == 3 and sub_2 == 6 and sub_3 == 7) or (
                b and sub_1 == 3 and sub_2 == 7 and sub_3 == 6):
            career_type = "Investigative career type"
            course_1 = "Law and related courses"
            course_2 = ""
            course_3 = ""
            course_4 = ''
            course_5 = ''
            course_6 = ''
            course_7 = ''
            course_7 = ''
            course_8 = ''
            course_9 = ''
            course_10 = ''

    #difines rules for specific invesigative careers careers
       # this follows the fact that one belong to invesigative career but differs in subjecs
    elif (b and sub_1 == 1 and sub_2 == 6 and sub_3) or (
                b and sub_1 == 1 and sub_2 and sub_3 == 6) or (
                b and sub_1 and sub_2 == 1 and sub_3 == 6) or (
                b and sub_1 and sub_2 == 6 and sub_3 == 1) or (
                b and sub_1 == 6 and sub_2 and sub_3 == 1) or (
                b and sub_1 == 6 and sub_2 == 1 and sub_3) or (b and sub_1 == 5 and sub_2 == 6 and sub_3) or (
                b and sub_1 == 5 and sub_2 and sub_3 == 6) or (
                b and sub_1 and sub_2 == 5 and sub_3 == 6) or (
                b and sub_1 and sub_2 == 6 and sub_3 == 5) or (
                b and sub_1 == 6 and sub_2 and sub_3 == 5) or (
                b and sub_1 == 6 and sub_2 == 5 and sub_3):
            career_type = "investigative career type"
            course_1 = "Biomedical science"
            course_2 = "Science laboratory technology"
            course_3 = "Dental technology"
            course_4 = ' Medical psychology'
            course_5 = 'Radiography'
            course_6 = 'epidemiology and biostatistics'
            course_7 = ' Biostatistics'
            course_8 = ""
            course_9 = ''
            course_10 = ''

    #difines rules for specific invesigative careers careers
       # this follows the fact that one belong to invesigative career but differs in subjecs
    elif b and sub_1 and sub_2 and sub_3:
            career_type = "Investigative career type"
            course_1 = "Molecular Biology & Forensic Technology"
            course_2 = "statistics & Computer Science"
            course_3 = "Dental technology"
            course_4 = 'Applied Aquatic Science / Fisheries And Oceanography'
            course_5 = "Forestry / Crop Improvement And Protection"
            course_6 = 'Cloud Computing & Information Security'
            course_7 = ' Biostatistics'
            course_8 = "Engineering Physics / Technical & Applied Physics"
            course_9 = 'Animal science'
            course_10 = 'Software Engineering / Software Development'

     #difines rules for specific artistic careers careers
       # this follows the fact that one belong to artistic career but differs in subjecs
    elif (c and sub_1 == 1 and sub_2 == 4 and sub_3 == 6) or (
                c and sub_1 == 1 and sub_2 == 4 and sub_3 == 6) or (
                c and sub_1 == 4 and sub_2 == 1 and sub_3 == 6) or (
                c and sub_1 == 4 and sub_2 == 6 and sub_3 == 1) or (
                c and sub_1 == 6 and sub_2 == 4 and sub_3 == 1) or (
                c and sub_1 == 6 and sub_2 == 1 and sub_3 == 4) or (c and sub_1 == 5 and sub_2 == 6 and sub_3 == 4) or (
                c and sub_1 == 5 and sub_2 == 4 and sub_3 == 6) or (
                c and sub_1 == 4 and sub_2 == 5 and sub_3 == 6) or (
                c and sub_1 == 4 and sub_2 == 6 and sub_3 == 5) or (
                c and sub_1 == 6 and sub_2 == 4 and sub_3 == 5) or (
                c and sub_1 == 6 and sub_2 == 5 and sub_3 == 4) or (
                c and sub_1 == 1 and sub_2 == 4 and sub_3 == 13) or (
                c and sub_1 == 1 and sub_2 == 4 and sub_3 == 13) or (
                c and sub_1 == 4 and sub_2 == 1 and sub_3 == 13) or (
                c and sub_1 == 4 and sub_2 == 13 and sub_3 == 1) or (
                c and sub_1 == 13 and sub_2 == 4 and sub_3 == 1) or (
                c and sub_1 == 13 and sub_2 == 1 and sub_3 == 4) or (
                c and sub_1 == 5 and sub_2 == 6 and sub_3 == 4) or (
                c and sub_1 == 5 and sub_2 == 4 and sub_3 == 13) or (
                c and sub_1 == 4 and sub_2 == 5 and sub_3 == 13) or (
                c and sub_1 == 4 and sub_2 == 13 and sub_3 == 5) or (
                c and sub_1 == 13 and sub_2 == 4 and sub_3 == 5) or (
                c and sub_1 == 13 and sub_2 == 5 and sub_3 == 4):
            career_type = "Artistic career type"
            course_1 = "Apparel and Fashion Technology"
            course_2 = "Clothing Textile and Interior Design"
            course_3 = "Fashion Design and Marketing"
            course_4 = ' Fashion Design & Textile Technology'
            course_5 = 'Fashion Design & Marketing'
            course_6 = 'Textile and Apparel'
            course_7 = ' Textile Technology and Applied Fashion Design'
            course_8 = "Interior Design"
            course_9 = ''
            course_10 = ''

    #difines rules for specific artistic careers careers
       # this follows the fact that one belong to artistic career but differs in subjecs
    elif (c and sub_1 == 14 and sub_2 == 2 and sub_3) or (
                c and sub_1 == 14 and sub_2 and sub_3 == 2) or (
                c and sub_1 == 2 and sub_2 == 14 and sub_3) or (
                c and sub_1 == 2 and sub_2 and sub_3 == 14) or (
                c and sub_1 and sub_2 == 14 and sub_3 == 2) or (
                c and sub_1 and sub_2 == 2 and sub_3 == 14) or (c and sub_1 == 14 and sub_2 == 3 and sub_3) or (
                c and sub_1 == 14 and sub_2 and sub_3 == 3) or (
                c and sub_1 == 3 and sub_2 == 14 and sub_3) or (
                c and sub_1 == 3 and sub_2 and sub_3 == 14) or (
                c and sub_1 and sub_2 == 14 and sub_3 == 3) or (
                c and sub_1 and sub_2 == 3 and sub_3 == 14):
            career_type = "Artistic career type"
            course_1 = "Music (and related degrees)"
            course_2 = ""
            course_3 = ""
            course_4 = ''
            course_5 = ''
            course_6 = ''
            course_7 = ''
            course_8 = ""
            course_9 = ''
            course_10 = ''

    #difines rules for specific artistic careers careers
       # this follows the fact that one belong to artistic career but differs in subjecs
    elif (c and sub_1 == 1 and sub_2 == 4 and sub_3 == 5) or (
                c and sub_1 == 1 and sub_2 == 5 and sub_3 == 4) or (
                c and sub_1 == 4 and sub_2 == 1 and sub_3 == 5) or (
                c and sub_1 == 4 and sub_2 == 5 and sub_3 == 1) or (
                c and sub_1 == 5 and sub_2 == 1 and sub_3 == 4) or (
                c and sub_1 == 5 and sub_2 == 4 and sub_3 == 1) or (
                c and sub_1 == 1 and sub_2 == 11 and sub_3 == 5) or (
                c and sub_1 == 1 and sub_2 == 5 and sub_3 == 11) or (
                c and sub_1 == 11 and sub_2 == 1 and sub_3 == 5) or (
                c and sub_1 == 11 and sub_2 == 5 and sub_3 == 1) or (
                c and sub_1 == 5 and sub_2 == 1 and sub_3 == 11) or (
                c and sub_1 == 5 and sub_2 == 11 and sub_3 == 1):
            career_type = "Artistic career type"
            course_1 = "Architectural Studies"
            course_2 = "Architecture"
            course_3 = " Quantity Surveying"
            course_4 = 'Surveying Technology'
            course_5 = 'Landscape Architecture'
            course_6 = ''
            course_7 = ''
            course_8 = ""
            course_9 = ''
            course_10 = ''

    #difines rules for specific artistic careers careers
       # this follows the fact that one belong to artistic career but differs in subjecs
    elif (c and sub_1 == 1 and sub_2 == 2 and sub_3 == 5) or (c and sub_1 == 1 and sub_2 == 5 and sub_3 == 2) or (
                c and sub_1 == 5 and sub_2 == 1 and sub_3 == 2) or (c and sub_1 == 5 and sub_2 == 2 and sub_3 == 1) or (
                c and sub_1 == 2 and sub_2 == 1 and sub_3 == 5) or (c and sub_1 == 2 and sub_2 == 5 and sub_3 == 1) or (
                c and sub_1 == 1 and sub_2 == 3 and sub_3 == 5) or (c and sub_1 == 1 and sub_2 == 5 and sub_3 == 3) or (
                c and sub_1 == 5 and sub_2 == 1 and sub_3 == 3) or (c and sub_1 == 5 and sub_2 == 3 and sub_3 == 1) or (
                c and sub_1 == 3 and sub_2 == 1 and sub_3 == 5) or (c and sub_1 == 3 and sub_2 == 5 and sub_3 == 1):
            career_type = "Enterprising career type"
            course_1 = "BA in (Planning)"
            course_2 = "Built Environment (Urban & Regional Planning)"
            course_3 = "Urban & Regional Planning"
            course_4 = 'Urban & Regional Planning'
            course_5 = 'Urban Design & Development'
            course_6 = ' Spatial Planning'
            course_7 = ''
            course_8 = " "
            course_9 = ''
            course_10 = ''

    #difines rules for specific artistic careers careers
       # this follows the fact that one belong to artistic career but differs in subjecs
    elif (c and sub_1 == 1 and sub_2 == 2 and sub_3 == 6) or (
                c and sub_1 == 1 and sub_2 == 6 and sub_3 == 2) or (
                c and sub_1 == 2 and sub_2 == 1 and sub_3 == 6) or (
                c and sub_1 == 2 and sub_2 == 6 and sub_3 == 1) or (
                c and sub_1 == 6 and sub_2 == 1 and sub_3 == 2) or (
                c and sub_1 == 6 and sub_2 == 2 and sub_3 == 1) or (
                c and sub_1 == 1 and sub_2 == 2 and sub_3 == 11) or (
                c and sub_1 == 1 and sub_2 == 11 and sub_3 == 2) or (
                c and sub_1 == 2 and sub_2 == 1 and sub_3 == 11) or (
                c and sub_1 == 2 and sub_2 == 11 and sub_3 == 1) or (
                c and sub_1 == 11 and sub_2 == 1 and sub_3 == 2) or (
                c and sub_1 == 11 and sub_2 == 2 and sub_3 == 1) or (
                c and sub_1 == 1 and sub_2 == 2 and sub_3 == 4) or (
                c and sub_1 == 1 and sub_2 == 4 and sub_3 == 2) or (
                c and sub_1 == 2 and sub_2 == 1 and sub_3 == 4) or (
                c and sub_1 == 2 and sub_2 == 4 and sub_3 == 1) or (
                c and sub_1 == 4 and sub_2 == 1 and sub_3 == 2) or (
                c and sub_1 == 4 and sub_2 == 2 and sub_3 == 1) or (c and sub_1 == 1 and sub_2 == 2 and sub_3 == 7) or (
                c and sub_1 == 1 and sub_2 == 7 and sub_3 == 2) or (
                c and sub_1 == 2 and sub_2 == 1 and sub_3 == 7) or (
                c and sub_1 == 2 and sub_2 == 7 and sub_3 == 1) or (
                c and sub_1 == 7 and sub_2 == 1 and sub_3 == 2) or (
                c and sub_1 == 7 and sub_2 == 2 and sub_3 == 1) or (
                c and sub_1 == 1 and sub_2 == 3 and sub_3 == 6) or (
                c and sub_1 == 1 and sub_2 == 6 and sub_3 == 3) or (
                c and sub_1 == 3 and sub_2 == 1 and sub_3 == 6) or (
                c and sub_1 == 3 and sub_2 == 6 and sub_3 == 1) or (
                c and sub_1 == 6 and sub_2 == 1 and sub_3 == 3) or (
                c and sub_1 == 6 and sub_2 == 3 and sub_3 == 1) or (
                c and sub_1 == 1 and sub_2 == 3 and sub_3 == 11) or (
                c and sub_1 == 1 and sub_2 == 11 and sub_3 == 3) or (
                c and sub_1 == 3 and sub_2 == 1 and sub_3 == 11) or (
                c and sub_1 == 3 and sub_2 == 11 and sub_3 == 1) or (
                c and sub_1 == 11 and sub_2 == 1 and sub_3 == 3) or (
                c and sub_1 == 11 and sub_2 == 3 and sub_3 == 1) or (
                c and sub_1 == 1 and sub_2 == 3 and sub_3 == 4) or (
                c and sub_1 == 1 and sub_2 == 4 and sub_3 == 3) or (
                c and sub_1 == 3 and sub_2 == 1 and sub_3 == 4) or (
                c and sub_1 == 3 and sub_2 == 4 and sub_3 == 1) or (
                c and sub_1 == 4 and sub_2 == 1 and sub_3 == 3) or (
                c and sub_1 == 4 and sub_2 == 3 and sub_3 == 1) or (c and sub_1 == 1 and sub_2 == 3 and sub_3 == 7) or (
                c and sub_1 == 1 and sub_2 == 7 and sub_3 == 3) or (
                c and sub_1 == 3 and sub_2 == 1 and sub_3 == 7) or (
                c and sub_1 == 3 and sub_2 == 7 and sub_3 == 1) or (
                c and sub_1 == 7 and sub_2 == 1 and sub_3 == 3) or (
                c and sub_1 == 7 and sub_2 == 3 and sub_3 == 1):
            career_type = "Artistic career type"
            course_1 = "Arts / BA in (Design))"
            course_2 = "Film And Animation / Tech (Design)"
            course_3 = " Gaming & Animation Technology"
            course_4 = 'Journalism and related courses'
            course_5 = 'Graphic, Communication, & Advertising'
            course_6 = 'Applied Communication'
            course_7 = 'Fine Art / Linguistic /  Literature'
            course_8 = "Arts/Science (Community Development)"
            course_9 = 'Broadcast Journalism/ Production'
            course_10 = 'Drama, Theatre Studies, Performing Arts, Theater Arts, Film Technology'

        #difines rules for specific artistic careers careers
       # this follows the fact that one belong to artistic career but differs in subjecs
    elif (c and sub_1 and sub_2 and sub_3):
            career_type = "Artistic career type"
            course_1 = "Music (and related degrees)"
            course_2 = "Apparel and Fashion Technology"
            course_3 = "Landscape Architecture"
            course_4 = 'Architecture'
            course_5 = 'Film And Animation / Tech (Design)'
            course_6 = 'Fine Art'
            course_7 = 'Clothing Textile and Interior Design'
            course_8 = "Arts"
            course_9 = ''
            course_10 = ''

    #difines rules for specific social careers careers
       # this follows the fact that one belong to social career but differs in subjecs
    elif (d and sub_1 == 1 and sub_2 == 2 and sub_3) or (d and sub_1 == 1 and sub_2 and sub_3 == 2) or (
                d and sub_1 == 2 and sub_2 == 1 and sub_3) or (d and sub_1 == 2 and sub_2 and sub_3 == 1) or (
                d and sub_1 and sub_2 == 1 and sub_3 == 2) or (d and sub_1 and sub_2 == 2 and sub_3 == 1):
            career_type ="Social career type"
            course_1 = "Education arts"
            course_2 = "Education science"
            course_3 = ""
            course_4 = ''
            course_5 = ''
            course_6 = ''
            course_7 = ''
            course_8 = ""
            course_9 = ''
            course_10 = ''

    #difines rules for specific social careers careers
       # this follows the fact that one belong to social career but differs in subjecs
    elif (d and sub_1 == 10 and sub_2 == 2 and sub_3 == 7) or (
                d and sub_1 == 10 and sub_2 == 7 and sub_3 == 2) or (
                d and sub_1 == 2 and sub_2 == 10 and sub_3 == 7) or (
                d and sub_1 == 2 and sub_2 == 7 and sub_3 == 10) or (
                d and sub_1 == 7 and sub_2 == 10 and sub_3 == 2) or (
                d and sub_1 == 7 and sub_2 == 2 and sub_3 == 10) or (
                d and sub_1 == 10 and sub_2 == 3 and sub_3 == 7) or (
                d and sub_1 == 10 and sub_2 == 7 and sub_3 == 3) or (
                d and sub_1 == 3 and sub_2 == 10 and sub_3 == 7) or (
                d and sub_1 == 3 and sub_2 == 7 and sub_3 == 10) or (
                d and sub_1 == 7 and sub_2 == 10 and sub_3 == 3) or (
                d and sub_1 == 7 and sub_2 == 3 and sub_3 == 10) or (
                d and sub_1 == 11 and sub_2 == 2 and sub_3 == 7) or (
                d and sub_1 == 11 and sub_2 == 7 and sub_3 == 2) or (
                d and sub_1 == 2 and sub_2 == 11 and sub_3 == 7) or (
                d and sub_1 == 2 and sub_2 == 7 and sub_3 == 11) or (
                d and sub_1 == 7 and sub_2 == 11 and sub_3 == 2) or (
                d and sub_1 == 7 and sub_2 == 2 and sub_3 == 11) or (
                d and sub_1 == 11 and sub_2 == 3 and sub_3 == 7) or (
                d and sub_1 == 11 and sub_2 == 7 and sub_3 == 3) or (
                d and sub_1 == 3 and sub_2 == 11 and sub_3 == 7) or (
                d and sub_1 == 3 and sub_2 == 7 and sub_3 == 11) or (
                d and sub_1 == 7 and sub_2 == 11 and sub_3 == 3) or (
                d and sub_1 == 7 and sub_2 == 3 and sub_3 == 11):
            career_type = "Social career type"
            course_1 = "Biblical Studies"
            course_2 = "Bible and Theology"
            course_3 = " Pastoral Theology"
            course_4 = 'Church Management & Leadership'
            course_5 = 'Church Educational Ministries'
            course_6 = 'Christian Education'
            course_7 = ' Divinity'
            course_8 = ""
            course_9 = ''
            course_10 = ''

     #difines rules for specific social careers careers
       # this follows the fact that one belong to social career but differs in subjecs
    elif (d and sub_1 == 3 and sub_2 == 2 and sub_3 == 11) or (
                d and sub_1 == 3 and sub_2 == 2 and sub_3 == 11) or (
                d and sub_1 == 2 and sub_2 == 11 and sub_3 == 3) or (
                d and sub_1 == 2 and sub_2 == 3 and sub_3 == 11) or (
                d and sub_1 == 11 and sub_2 == 3 and sub_3 == 2) or (
                d and sub_1 == 11 and sub_2 == 2 and sub_3 == 3) or (
                d and sub_1 == 3 and sub_2 == 1 and sub_3 == 11) or (
                d and sub_1 == 3 and sub_2 == 1 and sub_3 == 11) or (
                d and sub_1 == 1 and sub_2 == 11 and sub_3 == 3) or (
                d and sub_1 == 1 and sub_2 == 3 and sub_3 == 11) or (
                d and sub_1 == 11 and sub_2 == 3 and sub_3 == 1) or (
                d and sub_1 == 11 and sub_2 == 1 and sub_3 == 3) or (
                d and sub_1 == 3 and sub_2 == 6 and sub_3 == 11) or (
                d and sub_1 == 3 and sub_2 == 6 and sub_3 == 11) or (
                d and sub_1 == 6 and sub_2 == 11 and sub_3 == 3) or (
                d and sub_1 == 6 and sub_2 == 3 and sub_3 == 11) or (
                d and sub_1 == 11 and sub_2 == 3 and sub_3 == 6) or (
                d and sub_1 == 11 and sub_2 == 6 and sub_3 == 3) or (
                d and sub_1 == 3 and sub_2 == 5 and sub_3 == 11) or (
                d and sub_1 == 3 and sub_2 == 5 and sub_3 == 11) or (
                d and sub_1 == 5 and sub_2 == 11 and sub_3 == 3) or (
                d and sub_1 == 5 and sub_2 == 3 and sub_3 == 11) or (
                d and sub_1 == 11 and sub_2 == 3 and sub_3 == 5) or (
                d and sub_1 == 11 and sub_2 == 5 and sub_3 == 3) or (
                d and sub_1 == 3 and sub_2 == 4 and sub_3 == 11) or (
                d and sub_1 == 3 and sub_2 == 4 and sub_3 == 11) or (
                d and sub_1 == 4 and sub_2 == 11 and sub_3 == 3) or (
                d and sub_1 == 4 and sub_2 == 3 and sub_3 == 11) or (
                d and sub_1 == 11 and sub_2 == 3 and sub_3 == 4) or (
                d and sub_1 == 11 and sub_2 == 4 and sub_3 == 3) or (
                d and sub_1 == 3 and sub_2 == 2 and sub_3 == 7) or (
                d and sub_1 == 3 and sub_2 == 2 and sub_3 == 7) or (
                d and sub_1 == 2 and sub_2 == 7 and sub_3 == 3) or (
                d and sub_1 == 2 and sub_2 == 3 and sub_3 == 7) or (
                d and sub_1 == 7 and sub_2 == 3 and sub_3 == 2) or (
                d and sub_1 == 7 and sub_2 == 2 and sub_3 == 3) or (d and sub_1 == 3 and sub_2 == 1 and sub_3 == 7) or (
                d and sub_1 == 3 and sub_2 == 1 and sub_3 == 7) or (
                d and sub_1 == 1 and sub_2 == 7 and sub_3 == 3) or (
                d and sub_1 == 1 and sub_2 == 3 and sub_3 == 7) or (
                d and sub_1 == 7 and sub_2 == 3 and sub_3 == 1) or (
                d and sub_1 == 7 and sub_2 == 1 and sub_3 == 3) or (d and sub_1 == 3 and sub_2 == 6 and sub_3 == 7) or (
                d and sub_1 == 3 and sub_2 == 6 and sub_3 == 7) or (
                d and sub_1 == 6 and sub_2 == 7 and sub_3 == 3) or (
                d and sub_1 == 6 and sub_2 == 3 and sub_3 == 7) or (
                d and sub_1 == 7 and sub_2 == 3 and sub_3 == 6) or (
                d and sub_1 == 7 and sub_2 == 6 and sub_3 == 3) or (d and sub_1 == 3 and sub_2 == 5 and sub_3 == 7) or (
                d and sub_1 == 3 and sub_2 == 5 and sub_3 == 7) or (
                d and sub_1 == 5 and sub_2 == 7 and sub_3 == 3) or (
                d and sub_1 == 5 and sub_2 == 3 and sub_3 == 7) or (
                d and sub_1 == 7 and sub_2 == 3 and sub_3 == 5) or (
                d and sub_1 == 7 and sub_2 == 5 and sub_3 == 3) or (d and sub_1 == 3 and sub_2 == 4 and sub_3 == 7) or (
                d and sub_1 == 3 and sub_2 == 4 and sub_3 == 7) or (
                d and sub_1 == 4 and sub_2 == 7 and sub_3 == 3) or (
                d and sub_1 == 4 and sub_2 == 3 and sub_3 == 7) or (
                d and sub_1 == 7 and sub_2 == 3 and sub_3 == 4) or (
                d and sub_1 == 7 and sub_2 == 4 and sub_3 == 3) or (
                d and sub_1 == 3 and sub_2 == 2 and sub_3 == 12) or (
                d and sub_1 == 3 and sub_2 == 2 and sub_3 == 12) or (
                d and sub_1 == 2 and sub_2 == 12 and sub_3 == 3) or (
                d and sub_1 == 2 and sub_2 == 3 and sub_3 == 12) or (
                d and sub_1 == 12 and sub_2 == 3 and sub_3 == 2) or (
                d and sub_1 == 12 and sub_2 == 2 and sub_3 == 3) or (
                d and sub_1 == 3 and sub_2 == 1 and sub_3 == 12) or (
                d and sub_1 == 3 and sub_2 == 1 and sub_3 == 12) or (
                d and sub_1 == 1 and sub_2 == 12 and sub_3 == 3) or (
                d and sub_1 == 1 and sub_2 == 3 and sub_3 == 12) or (
                d and sub_1 == 12 and sub_2 == 3 and sub_3 == 1) or (
                d and sub_1 == 12 and sub_2 == 1 and sub_3 == 3) or (
                d and sub_1 == 3 and sub_2 == 6 and sub_3 == 12) or (
                d and sub_1 == 3 and sub_2 == 6 and sub_3 == 12) or (
                d and sub_1 == 6 and sub_2 == 12 and sub_3 == 3) or (
                d and sub_1 == 6 and sub_2 == 3 and sub_3 == 12) or (
                d and sub_1 == 12 and sub_2 == 3 and sub_3 == 6) or (
                d and sub_1 == 12 and sub_2 == 6 and sub_3 == 3) or (
                d and sub_1 == 3 and sub_2 == 5 and sub_3 == 12) or (
                d and sub_1 == 3 and sub_2 == 5 and sub_3 == 12) or (
                d and sub_1 == 5 and sub_2 == 12 and sub_3 == 3) or (
                d and sub_1 == 5 and sub_2 == 3 and sub_3 == 12) or (
                d and sub_1 == 12 and sub_2 == 3 and sub_3 == 5) or (
                d and sub_1 == 12 and sub_2 == 5 and sub_3 == 3) or (
                d and sub_1 == 3 and sub_2 == 4 and sub_3 == 12) or (
                d and sub_1 == 3 and sub_2 == 4 and sub_3 == 12) or (
                d and sub_1 == 4 and sub_2 == 12 and sub_3 == 3) or (
                d and sub_1 == 4 and sub_2 == 3 and sub_3 == 12) or (
                d and sub_1 == 12 and sub_2 == 3 and sub_3 == 4) or (
                d and sub_1 == 12 and sub_2 == 4 and sub_3 == 3) or (
                d and sub_1 == 3 and sub_2 == 2 and sub_3 == 8) or (
                d and sub_1 == 3 and sub_2 == 2 and sub_3 == 8) or (
                d and sub_1 == 2 and sub_2 == 8 and sub_3 == 3) or (
                d and sub_1 == 2 and sub_2 == 3 and sub_3 == 8) or (
                d and sub_1 == 8 and sub_2 == 3 and sub_3 == 2) or (
                d and sub_1 == 8 and sub_2 == 2 and sub_3 == 3) or (d and sub_1 == 3 and sub_2 == 1 and sub_3 == 8) or (
                d and sub_1 == 3 and sub_2 == 1 and sub_3 == 8) or (
                d and sub_1 == 1 and sub_2 == 8 and sub_3 == 3) or (
                d and sub_1 == 1 and sub_2 == 3 and sub_3 == 8) or (
                d and sub_1 == 8 and sub_2 == 3 and sub_3 == 1) or (
                d and sub_1 == 8 and sub_2 == 1 and sub_3 == 3) or (d and sub_1 == 3 and sub_2 == 6 and sub_3 == 8) or (
                d and sub_1 == 3 and sub_2 == 6 and sub_3 == 8) or (
                d and sub_1 == 6 and sub_2 == 8 and sub_3 == 3) or (
                d and sub_1 == 6 and sub_2 == 3 and sub_3 == 8) or (
                d and sub_1 == 8 and sub_2 == 3 and sub_3 == 6) or (
                d and sub_1 == 8 and sub_2 == 6 and sub_3 == 3) or (d and sub_1 == 3 and sub_2 == 5 and sub_3 == 8) or (
                d and sub_1 == 3 and sub_2 == 5 and sub_3 == 8) or (
                d and sub_1 == 5 and sub_2 == 8 and sub_3 == 3) or (
                d and sub_1 == 5 and sub_2 == 3 and sub_3 == 8) or (
                d and sub_1 == 8 and sub_2 == 3 and sub_3 == 5) or (
                d and sub_1 == 8 and sub_2 == 5 and sub_3 == 3) or (d and sub_1 == 3 and sub_2 == 4 and sub_3 == 8) or (
                d and sub_1 == 3 and sub_2 == 4 and sub_3 == 8) or (
                d and sub_1 == 4 and sub_2 == 8 and sub_3 == 3) or (
                d and sub_1 == 4 and sub_2 == 3 and sub_3 == 8) or (
                d and sub_1 == 8 and sub_2 == 3 and sub_3 == 4) or (
                d and sub_1 == 8 and sub_2 == 4 and sub_3 == 3) or (
                d and sub_1 == 3 and sub_2 == 2 and sub_3 == 14) or (
                d and sub_1 == 3 and sub_2 == 2 and sub_3 == 14) or (
                d and sub_1 == 2 and sub_2 == 14 and sub_3 == 3) or (
                d and sub_1 == 2 and sub_2 == 3 and sub_3 == 14) or (
                d and sub_1 == 14 and sub_2 == 3 and sub_3 == 2) or (
                d and sub_1 == 14 and sub_2 == 2 and sub_3 == 3) or (
                d and sub_1 == 3 and sub_2 == 1 and sub_3 == 14) or (
                d and sub_1 == 3 and sub_2 == 1 and sub_3 == 14) or (
                d and sub_1 == 1 and sub_2 == 14 and sub_3 == 3) or (
                d and sub_1 == 1 and sub_2 == 3 and sub_3 == 14) or (
                d and sub_1 == 14 and sub_2 == 3 and sub_3 == 1) or (
                d and sub_1 == 14 and sub_2 == 1 and sub_3 == 3) or (
                d and sub_1 == 3 and sub_2 == 6 and sub_3 == 14) or (
                d and sub_1 == 3 and sub_2 == 6 and sub_3 == 14) or (
                d and sub_1 == 6 and sub_2 == 14 and sub_3 == 3) or (
                d and sub_1 == 6 and sub_2 == 3 and sub_3 == 14) or (
                d and sub_1 == 14 and sub_2 == 3 and sub_3 == 6) or (
                d and sub_1 == 14 and sub_2 == 6 and sub_3 == 3) or (
                d and sub_1 == 3 and sub_2 == 5 and sub_3 == 14) or (
                d and sub_1 == 3 and sub_2 == 5 and sub_3 == 14) or (
                d and sub_1 == 5 and sub_2 == 14 and sub_3 == 3) or (
                d and sub_1 == 5 and sub_2 == 3 and sub_3 == 14) or (
                d and sub_1 == 14 and sub_2 == 3 and sub_3 == 5) or (
                d and sub_1 == 14 and sub_2 == 5 and sub_3 == 3) or (
                d and sub_1 == 3 and sub_2 == 4 and sub_3 == 14) or (
                d and sub_1 == 3 and sub_2 == 4 and sub_3 == 14) or (
                d and sub_1 == 4 and sub_2 == 14 and sub_3 == 3) or (
                d and sub_1 == 4 and sub_2 == 3 and sub_3 == 14) or (
                d and sub_1 == 14 and sub_2 == 3 and sub_3 == 4) or (
                d and sub_1 == 14 and sub_2 == 4 and sub_3 == 3):
            career_type = "Social career type"
            course_1 = "In Kiswahili (With It)"
            course_2 = "In Kiswahili"
            course_3 = " Kiswahili and Geography"
            course_4 = 'Kiswahili and Communication'
            course_5 = 'Guidance and Counselling'
            course_6 = ''
            course_7 = ' '
            course_8 = ""
            course_9 = ''
            course_10 = ''

     #difines rules for specific social careers careers
       # this follows the fact that one belong to social career but differs in subjecs
    elif (d and sub_1 == 11 and sub_2 == 2 and sub_3 == 6) or (
                d and sub_1 == 11 and sub_2 == 6 and sub_3 == 2) or (
                d and sub_1 == 2 and sub_2 == 11 and sub_3 == 6) or (
                d and sub_1 == 2 and sub_2 == 6 and sub_3 == 11) or (
                d and sub_1 == 6 and sub_2 == 11 and sub_3 == 2) or (
                d and sub_1 == 6 and sub_2 == 2 and sub_3 == 11) or (
                d and sub_1 == 11 and sub_2 == 3 and sub_3 == 6) or (
                d and sub_1 == 11 and sub_2 == 6 and sub_3 == 3) or (
                d and sub_1 == 3 and sub_2 == 11 and sub_3 == 6) or (
                d and sub_1 == 3 and sub_2 == 6 and sub_3 == 11) or (
                d and sub_1 == 6 and sub_2 == 11 and sub_3 == 3) or (
                d and sub_1 == 6 and sub_2 == 3 and sub_3 == 11) or (
                d and sub_1 == 7 and sub_2 == 2 and sub_3 == 6) or (
                d and sub_1 == 7 and sub_2 == 6 and sub_3 == 2) or (
                d and sub_1 == 2 and sub_2 == 7 and sub_3 == 6) or (
                d and sub_1 == 2 and sub_2 == 6 and sub_3 == 7) or (
                d and sub_1 == 6 and sub_2 == 7 and sub_3 == 2) or (
                d and sub_1 == 6 and sub_2 == 2 and sub_3 == 7) or (d and sub_1 == 7 and sub_2 == 3 and sub_3 == 6) or (
                d and sub_1 == 7 and sub_2 == 6 and sub_3 == 3) or (
                d and sub_1 == 3 and sub_2 == 7 and sub_3 == 6) or (
                d and sub_1 == 3 and sub_2 == 6 and sub_3 == 7) or (
                d and sub_1 == 6 and sub_2 == 7 and sub_3 == 3) or (
                d and sub_1 == 6 and sub_2 == 3 and sub_3 == 7):
            career_type = "Social career type"
            course_1 = "Special Needs Education(With IT)"
            course_2 = "Special Needs Education"
            course_3 = "  Special Education"
            course_4 = 'Arts with Special Needs Education'
            course_5 = 'Science with Special Needs Education'
            course_6 = ' Ed (Special Needs Education) – Secondary Option'
            course_7 = ' '
            course_8 = ""
            course_9 = ''
            course_10 = ''

     #difines rules for specific social careers careers
       # this follows the fact that one belong to social career but differs in subjecs
    elif (d and sub_1 == 1 and sub_2 == 2 and sub_3 == 6) or (
                d and sub_1 == 1 and sub_2 == 6 and sub_3 == 2) or (
                d and sub_1 == 2 and sub_2 == 6 and sub_3 == 1) or (
                d and sub_1 == 2 and sub_2 == 1 and sub_3 == 6) or (
                d and sub_1 == 6 and sub_2 == 1 and sub_3 == 2) or (
                d and sub_1 == 6 and sub_2 == 2 and sub_3 == 1) or (d and sub_1 == 1 and sub_2 == 3 and sub_3 == 6) or (
                d and sub_1 == 1 and sub_2 == 6 and sub_3 == 3) or (
                d and sub_1 == 3 and sub_2 == 6 and sub_3 == 1) or (
                d and sub_1 == 3 and sub_2 == 1 and sub_3 == 6) or (
                d and sub_1 == 6 and sub_2 == 1 and sub_3 == 3) or (
                d and sub_1 == 6 and sub_2 == 3 and sub_3 == 1) or (d and sub_1 == 1 and sub_2 == 2 and sub_3 == 5) or (
                d and sub_1 == 1 and sub_2 == 5 and sub_3 == 2) or (
                d and sub_1 == 2 and sub_2 == 5 and sub_3 == 1) or (
                d and sub_1 == 2 and sub_2 == 1 and sub_3 == 5) or (
                d and sub_1 == 5 and sub_2 == 1 and sub_3 == 2) or (
                d and sub_1 == 5 and sub_2 == 2 and sub_3 == 1) or (d and sub_1 == 1 and sub_2 == 3 and sub_3 == 5) or (
                d and sub_1 == 1 and sub_2 == 5 and sub_3 == 3) or (
                d and sub_1 == 3 and sub_2 == 5 and sub_3 == 1) or (
                d and sub_1 == 3 and sub_2 == 1 and sub_3 == 5) or (
                d and sub_1 == 5 and sub_2 == 1 and sub_3 == 3) or (
                d and sub_1 == 5 and sub_2 == 3 and sub_3 == 1) or (
                d and sub_1 == 1 and sub_2 == 2 and sub_3 == 11) or (
                d and sub_1 == 1 and sub_2 == 11 and sub_3 == 2) or (
                d and sub_1 == 2 and sub_2 == 11 and sub_3 == 1) or (
                d and sub_1 == 2 and sub_2 == 1 and sub_3 == 11) or (
                d and sub_1 == 11 and sub_2 == 1 and sub_3 == 2) or (
                d and sub_1 == 11 and sub_2 == 2 and sub_3 == 1) or (
                d and sub_1 == 1 and sub_2 == 3 and sub_3 == 11) or (
                d and sub_1 == 1 and sub_2 == 11 and sub_3 == 3) or (
                d and sub_1 == 3 and sub_2 == 11 and sub_3 == 1) or (
                d and sub_1 == 3 and sub_2 == 1 and sub_3 == 11) or (
                d and sub_1 == 11 and sub_2 == 1 and sub_3 == 3) or (
                d and sub_1 == 11 and sub_2 == 3 and sub_3 == 1) or (
                d and sub_1 == 1 and sub_2 == 2 and sub_3 == 4) or (
                d and sub_1 == 1 and sub_2 == 4 and sub_3 == 2) or (
                d and sub_1 == 2 and sub_2 == 4 and sub_3 == 1) or (
                d and sub_1 == 2 and sub_2 == 1 and sub_3 == 4) or (
                d and sub_1 == 4 and sub_2 == 1 and sub_3 == 2) or (
                d and sub_1 == 4 and sub_2 == 2 and sub_3 == 1) or (d and sub_1 == 1 and sub_2 == 3 and sub_3 == 4) or (
                d and sub_1 == 1 and sub_2 == 4 and sub_3 == 3) or (
                d and sub_1 == 3 and sub_2 == 4 and sub_3 == 1) or (
                d and sub_1 == 3 and sub_2 == 1 and sub_3 == 4) or (
                d and sub_1 == 4 and sub_2 == 1 and sub_3 == 3) or (
                d and sub_1 == 4 and sub_2 == 3 and sub_3 == 1) or (d and sub_1 == 1 and sub_2 == 2 and sub_3 == 7) or (
                d and sub_1 == 1 and sub_2 == 7 and sub_3 == 2) or (
                d and sub_1 == 2 and sub_2 == 7 and sub_3 == 1) or (
                d and sub_1 == 2 and sub_2 == 1 and sub_3 == 7) or (
                d and sub_1 == 7 and sub_2 == 1 and sub_3 == 2) or (
                d and sub_1 == 7 and sub_2 == 2 and sub_3 == 1) or (d and sub_1 == 1 and sub_2 == 3 and sub_3 == 7) or (
                d and sub_1 == 1 and sub_2 == 7 and sub_3 == 3) or (
                d and sub_1 == 3 and sub_2 == 7 and sub_3 == 1) or (
                d and sub_1 == 3 and sub_2 == 1 and sub_3 == 7) or (
                d and sub_1 == 7 and sub_2 == 1 and sub_3 == 3) or (
                d and sub_1 == 7 and sub_2 == 3 and sub_3 == 1):
            career_type ="Social career type"
            course_1 = "Political Science/ Public Administration & Leadership,  Public Policy & Administration"
            course_2 = "Human Rights, Conflict Resolution  and related , Justice And Peace"
            course_3 = " Penology, Correction, & Administration"
            course_4 = ' Emergency Management, Humanitarian Assistance'
            course_5 = 'International Relations,Diplomacy, Sociology And Technology'
            course_6 = 'Gender ,Women, Development Studies, Sustainable Human Development ,Policy Studies'
            course_7 = ' Child & Youth Studies, Childcare And Protection'
            course_8 = "Social Communication, Public Management, Social Work , Sociology & Religion"
            course_9 = 'Philosophy, /Counselling Psychology & related / Criminology $ related'
            course_10 = 'Anthropology, Medical Social Work'

     #difines rules for specific social careers careers
       # this follows the fact that one belong to social career but differs in subjecs
    elif (d and sub_1 == 10 and sub_2 and sub_3 == 2) or (
                d and sub_1 == 10 and sub_2 == 2 and sub_3) or (
                d and sub_1 == 2 and sub_2 == 10 and sub_3) or (
                d and sub_1 == 2 and sub_2 and sub_3 == 10) or (
                d and sub_1 and sub_2 == 10 and sub_3 == 2) or (
                d and sub_1 and sub_2 == 2 and sub_3 == 10) or (d and sub_1 == 10 and sub_2 and sub_3 == 3) or (
                d and sub_1 == 10 and sub_2 == 3 and sub_3) or (
                d and sub_1 == 3 and sub_2 == 10 and sub_3) or (
                d and sub_1 == 3 and sub_2 and sub_3 == 10) or (
                d and sub_1 and sub_2 == 10 and sub_3 == 3) or (
                d and sub_1 and sub_2 == 3 and sub_3 == 10):
            career_type ="Social career type"
            course_1 = " History"
            course_2 = "History And International Studies"
            course_3 = " History & Archaeology"
            course_4 = ''
            course_5 = ''
            course_6 = ' '
            course_7 = ''
            course_8 = ""
            course_9 = ''
            course_10 = ''

     #difines rules for specific social careers careers
       # this follows the fact that one belong to social career but differs in subjecs
    elif (d and sub_1 and sub_2 and sub_3):
            career_type = "Social career type"
            course_1 = "History and related)"
            course_2 = "Political Science/ Public Administration & Leadership"
            course_3 = "Special Needs Education(With IT)"
            course_4 = 'Kiswahili and related'
            course_5 = 'Church Management & Leadership'
            course_6 = 'Education science'
            course_7 = ''
            course_8 = ""
            course_9 = ''
            course_10 = ''

     #difines rules for specific enterprising careers careers
       # this follows the fact that one belong to enterprising career but differs in subjecs
    elif (e and sub_1 == 1 and sub_2 == 6 and sub_3 == 4) or (e and sub_1 == 1 and sub_2 == 4 and sub_3 == 6) or (
                e and sub_1 == 4 and sub_2 == 1 and sub_3 == 6) or (e and sub_1 == 4 and sub_2 == 6 and sub_3 == 1) or (
                e and sub_1 == 6 and sub_2 == 1 and sub_3 == 4) or (e and sub_1 == 6 and sub_2 == 4 and sub_3 == 1) or (
                e and sub_1 == 1 and sub_2 == 6 and sub_3 == 5) or (e and sub_1 == 1 and sub_2 == 5 and sub_3 == 6) or (
                e and sub_1 == 5 and sub_2 == 1 and sub_3 == 6) or (e and sub_1 == 5 and sub_2 == 6 and sub_3 == 1) or (
                e and sub_1 == 6 and sub_2 == 1 and sub_3 == 5) or (e and sub_1 == 6 and sub_2 == 5 and sub_3 == 1):
            career_type ="Enterprising career type"
            course_1 = "Agri Business Management"
            course_2 = "Agribusiness Management (& Trade), & Marketing (With IT)"
            course_3 = "Agricultural Economics & Resource Management"
            course_4 = 'Agricultural Economics(With IT)'
            course_5 = 'Agribusiness Management & Marketing'
            course_6 = ' Agribusiness,  Food Industry Management'
            course_7 = 'Agricultural Economics , Rural Development'
            course_8 = "Agribusiness Management "
            course_9 = 'Agribusiness Economics , Food Industry Managements Economics ,'
            course_10 = 'Enterprise Development, Entrepreneurship'

     #difines rules for specific enterprising careers careers
       # this follows the fact that one belong to enterprising career but differs in subjecs

    elif (e and sub_1 == 1 and sub_2 == 6 and sub_3 == 2) or (
                e and sub_1 == 1 and sub_2 == 2 and sub_3 == 6) or (
                e and sub_1 == 2 and sub_2 == 1 and sub_3 == 6) or (
                e and sub_1 == 2 and sub_2 == 6 and sub_3 == 1) or (
                e and sub_1 == 6 and sub_2 == 1 and sub_3 == 2) or (
                e and sub_1 == 6 and sub_2 == 2 and sub_3 == 1) or (e and sub_1 == 1 and sub_2 == 6 and sub_3 == 3) or (
                e and sub_1 == 1 and sub_2 == 3 and sub_3 == 6) or (
                e and sub_1 == 3 and sub_2 == 1 and sub_3 == 6) or (
                e and sub_1 == 3 and sub_2 == 6 and sub_3 == 1) or (
                e and sub_1 == 6 and sub_2 == 1 and sub_3 == 3) or (
                e and sub_1 == 6 and sub_2 == 3 and sub_3 == 1) or (e and sub_1 == 1 and sub_2 == 4 and sub_3 == 2) or (
                e and sub_1 == 1 and sub_2 == 2 and sub_3 == 4) or (
                e and sub_1 == 2 and sub_2 == 1 and sub_3 == 4) or (
                e and sub_1 == 2 and sub_2 == 4 and sub_3 == 1) or (
                e and sub_1 == 4 and sub_2 == 1 and sub_3 == 2) or (
                e and sub_1 == 4 and sub_2 == 2 and sub_3 == 1) or (e and sub_1 == 1 and sub_2 == 4 and sub_3 == 3) or (
                e and sub_1 == 1 and sub_2 == 3 and sub_3 == 4) or (
                e and sub_1 == 3 and sub_2 == 1 and sub_3 == 4) or (
                e and sub_1 == 3 and sub_2 == 4 and sub_3 == 1) or (
                e and sub_1 == 4 and sub_2 == 1 and sub_3 == 3) or (
                e and sub_1 == 4 and sub_2 == 3 and sub_3 == 1) or (e and sub_1 == 1 and sub_2 == 5 and sub_3 == 2) or (
                e and sub_1 == 1 and sub_2 == 2 and sub_3 == 5) or (
                e and sub_1 == 2 and sub_2 == 1 and sub_3 == 5) or (
                e and sub_1 == 2 and sub_2 == 5 and sub_3 == 1) or (
                e and sub_1 == 5 and sub_2 == 1 and sub_3 == 2) or (
                e and sub_1 == 5 and sub_2 == 2 and sub_3 == 1) or (e and sub_1 == 1 and sub_2 == 5 and sub_3 == 3) or (
                e and sub_1 == 1 and sub_2 == 3 and sub_3 == 6) or (
                e and sub_1 == 3 and sub_2 == 1 and sub_3 == 5) or (
                e and sub_1 == 3 and sub_2 == 5 and sub_3 == 1) or (
                e and sub_1 == 5 and sub_2 == 1 and sub_3 == 3) or (
                e and sub_1 == 5 and sub_2 == 3 and sub_3 == 1) or (
                e and sub_1 == 1 and sub_2 == 7 and sub_3 == 2) or (
                e and sub_1 == 1 and sub_2 == 2 and sub_3 == 7) or (
                e and sub_1 == 2 and sub_2 == 1 and sub_3 == 7) or (
                e and sub_1 == 2 and sub_2 == 7 and sub_3 == 1) or (
                e and sub_1 == 7 and sub_2 == 1 and sub_3 == 2) or (
                e and sub_1 == 7 and sub_2 == 2 and sub_3 == 1) or (e and sub_1 == 1 and sub_2 == 7 and sub_3 == 3) or (
                e and sub_1 == 1 and sub_2 == 3 and sub_3 == 7) or (
                e and sub_1 == 3 and sub_2 == 1 and sub_3 == 7) or (
                e and sub_1 == 3 and sub_2 == 7 and sub_3 == 1) or (
                e and sub_1 == 7 and sub_2 == 1 and sub_3 == 3) or (
                e and sub_1 == 7 and sub_2 == 3 and sub_3 == 1) or (
                e and sub_1 == 1 and sub_2 == 11 and sub_3 == 2) or (
                e and sub_1 == 1 and sub_2 == 2 and sub_3 == 11) or (
                e and sub_1 == 2 and sub_2 == 1 and sub_3 == 11) or (
                e and sub_1 == 2 and sub_2 == 11 and sub_3 == 1) or (
                e and sub_1 == 11 and sub_2 == 1 and sub_3 == 2) or (
                e and sub_1 == 11 and sub_2 == 2 and sub_3 == 1) or (
                e and sub_1 == 1 and sub_2 == 11 and sub_3 == 3) or (
                e and sub_1 == 1 and sub_2 == 3 and sub_3 == 11) or (
                e and sub_1 == 3 and sub_2 == 1 and sub_3 == 11) or (
                e and sub_1 == 3 and sub_2 == 11 and sub_3 == 1) or (
                e and sub_1 == 11 and sub_2 == 1 and sub_3 == 3) or (
                e and sub_1 == 11 and sub_2 == 3 and sub_3 == 1):
            career_type = "Enterprising career type"
            course_1 = "Records Management, Business And Management,  Marketing With It, Business Administration"
            course_2 = "Secretarial,  Office Management, Office Administration, Tourism Management"
            course_3 = "Human Resource Management, Business And Information Technology"
            course_4 = ' Business Innovation And Technology Management, Business Leadership'
            course_5 = 'Hospitality And Tourism Management, Institutional Management, Restaurant Management'
            course_6 = 'Procurement And Contract Management, Supply Chain Management,Supplies Management'
            course_7 = 'Logistics, Marine Business Management, Strategic Management '
            course_8 = "Entrepreneurship, Small Enterprises Management, Small Business Management"
            course_9 = 'Civil Aviation Management, Co-Operative Management'
            course_10 = 'Health Services Management,  International Business Management, Hospitality Management'

        #difines rules for specific enterprising careers careers
       # this follows the fact that one belong to enterprising career but differs in subjecs

    elif (e and sub_1 == 10 and sub_2 and sub_3 == 2) or (
                e and sub_1 == 10 and sub_2 == 2 and sub_3) or (
                e and sub_1 == 2 and sub_2 == 10 and sub_3) or (
                e and sub_1 == 2 and sub_2 and sub_3 == 10) or (
                e and sub_1 and sub_2 == 10 and sub_3 == 2) or (
                e and sub_1 and sub_2 == 2 and sub_3 == 10) or (e and sub_1 == 10 and sub_2 and sub_3 == 3) or (
                e and sub_1 == 10 and sub_2 == 3 and sub_3) or (
                e and sub_1 == 3 and sub_2 == 10 and sub_3) or (
                e and sub_1 == 3 and sub_2 and sub_3 == 10) or (
                e and sub_1 and sub_2 == 10 and sub_3 == 3) or (
                e and sub_1 and sub_2 == 3 and sub_3 == 10):
            career_type = "Enterprising career type"
            course_1 = " History & Economics"
            course_2 = ""
            course_3 = ""
            course_4 = ''
            course_5 = ''
            course_6 = ' '
            course_7 = ''
            course_8 = ""
            course_9 = ''
            course_10 = ''

         #difines rules for specific enterprising careers careers
       # this follows the fact that one belong to enterprising career but differs in subjecs
    elif (e and sub_1 and sub_2 and sub_3):
            career_type = "Enterprising career type"
            course_1 = "History & Economics"
            course_2 = "Entrepreneurship, Small Enterprises Management"
            course_3 = "Small Business Management"
            course_4 = 'Agri Business Management'
            course_5 = "Records Management, Business Administration"
            course_6 = 'Business And Management'
            course_7 = "Agricultural Economics & Resource Management"
            course_8 = ""
            course_9 = ''
            course_10 = ''

    #difines rules for specific enterprising careers careers
       # this follows the fact that one belong to enterprising career but differs in subjecs
    elif (f and sub_1 == 1 and sub_2 == 6 and sub_3 == 11) or (
                f and sub_1 == 1 and sub_2 == 11 and sub_3 == 6) or (
                f and sub_1 == 6 and sub_2 == 11 and sub_3 == 1) or (
                f and sub_1 == 6 and sub_2 == 1 and sub_3 == 11) or (
                f and sub_1 == 11 and sub_2 == 1 and sub_3 == 6) or (
                f and sub_1 == 11 and sub_2 == 6 and sub_3 == 1) or (
                f and sub_1 == 1 and sub_2 == 5 and sub_3 == 11) or (
                f and sub_1 == 1 and sub_2 == 11 and sub_3 == 5) or (
                f and sub_1 == 5 and sub_2 == 11 and sub_3 == 1) or (
                f and sub_1 == 5 and sub_2 == 1 and sub_3 == 11) or (
                f and sub_1 == 11 and sub_2 == 1 and sub_3 == 5) or (
                f and sub_1 == 11 and sub_2 == 5 and sub_3 == 1) or (
                f and sub_1 == 1 and sub_2 == 4 and sub_3 == 11) or (
                f and sub_1 == 1 and sub_2 == 11 and sub_3 == 4) or (
                f and sub_1 == 4 and sub_2 == 11 and sub_3 == 1) or (
                f and sub_1 == 4 and sub_2 == 1 and sub_3 == 11) or (
                f and sub_1 == 11 and sub_2 == 1 and sub_3 == 4) or (
                f and sub_1 == 11 and sub_2 == 4 and sub_3 == 1) or (
                f and sub_1 == 1 and sub_2 == 6 and sub_3 == 7) or (
                f and sub_1 == 1 and sub_2 == 7 and sub_3 == 6) or (
                f and sub_1 == 6 and sub_2 == 7 and sub_3 == 1) or (
                f and sub_1 == 6 and sub_2 == 1 and sub_3 == 7) or (
                f and sub_1 == 7 and sub_2 == 1 and sub_3 == 6) or (
                f and sub_1 == 7 and sub_2 == 6 and sub_3 == 1) or (f and sub_1 == 1 and sub_2 == 5 and sub_3 == 7) or (
                f and sub_1 == 1 and sub_2 == 7 and sub_3 == 5) or (
                f and sub_1 == 5 and sub_2 == 7 and sub_3 == 1) or (
                f and sub_1 == 5 and sub_2 == 1 and sub_3 == 7) or (
                f and sub_1 == 7 and sub_2 == 1 and sub_3 == 5) or (
                f and sub_1 == 7 and sub_2 == 5 and sub_3 == 1) or (f and sub_1 == 1 and sub_2 == 4 and sub_3 == 7) or (
                f and sub_1 == 1 and sub_2 == 7 and sub_3 == 4) or (
                f and sub_1 == 4 and sub_2 == 7 and sub_3 == 1) or (
                f and sub_1 == 4 and sub_2 == 1 and sub_3 == 7) or (
                f and sub_1 == 7 and sub_2 == 1 and sub_3 == 4) or (
                f and sub_1 == 7 and sub_2 == 4 and sub_3 == 1):
            career_type = "Conventional career type"
            course_1 = "Actuarial Science, Mathematical Sciences, Mathematics & Physics"
            course_2 = "Mathematics, Mathematics And Finance, Mathematics & Economics"
            course_3 = " Mathematics & Computer Science, Economics & Business Studies"
            course_4 = 'Industrial Mathematics, Financial Engineering'
            course_5 = 'Data Science,  Mathematics & Business Studies'
            course_6 = 'Data Science & Analytics, Banking And Finance'
            course_7 = 'Mathematics & Modelling Processes'
            course_8 = "Statistics & Programming, Statistics,  Economics, Applied Statistics"
            course_9 = 'Economics & Sociology, Financial Economics'
            course_10 = 'Applied Economics, Economics & Statistics, Operations Research'

        #difines rules for specific convectional careers careers
       # this follows the fact that one belong to convectional career but differs in subjecs
    elif (f and sub_1 == 1 and sub_2 == 2 and sub_3 == 11) or (
                f and sub_1 == 1 and sub_2 == 11 and sub_3 == 2) or (
                f and sub_1 == 2 and sub_2 == 11 and sub_3 == 1) or (
                f and sub_1 == 2 and sub_2 == 1 and sub_3 == 11) or (
                f and sub_1 == 11 and sub_2 == 1 and sub_3 == 2) or (
                f and sub_1 == 11 and sub_2 == 2 and sub_3 == 1) or (
                f and sub_1 == 1 and sub_2 == 3 and sub_3 == 11) or (
                f and sub_1 == 1 and sub_2 == 11 and sub_3 == 3) or (
                f and sub_1 == 3 and sub_2 == 11 and sub_3 == 1) or (
                f and sub_1 == 3 and sub_2 == 1 and sub_3 == 11) or (
                f and sub_1 == 11 and sub_2 == 1 and sub_3 == 3) or (
                f and sub_1 == 11 and sub_2 == 3 and sub_3 == 1) or (
                f and sub_1 == 1 and sub_2 == 2 and sub_3 == 7) or (
                f and sub_1 == 1 and sub_2 == 7 and sub_3 == 2) or (
                f and sub_1 == 2 and sub_2 == 7 and sub_3 == 1) or (
                f and sub_1 == 2 and sub_2 == 1 and sub_3 == 7) or (
                f and sub_1 == 7 and sub_2 == 1 and sub_3 == 2) or (
                f and sub_1 == 7 and sub_2 == 2 and sub_3 == 1) or (f and sub_1 == 1 and sub_2 == 3 and sub_3 == 7) or (
                f and sub_1 == 1 and sub_2 == 7 and sub_3 == 3) or (
                f and sub_1 == 3 and sub_2 == 7 and sub_3 == 1) or (
                f and sub_1 == 3 and sub_2 == 1 and sub_3 == 7) or (
                f and sub_1 == 7 and sub_2 == 1 and sub_3 == 3) or (
                f and sub_1 == 7 and sub_2 == 3 and sub_3 == 1):
            career_type = "Conventional career type"
            course_1 = "Business Administration In Accounting"
            course_2 = "Accountancy & Financial Management"
            course_3 = "Accounting/Accountancy"
            course_4 = ' Accounting And Finance'
            course_5 = ''
            course_6 = ' '
            course_7 = ''
            course_8 = ""
            course_9 = ''
            course_10 = ''
     #difines rules for specific convectional careers careers
       # this follows the fact that one belong to convectional career but differs in subjecs
        # BIO ,LANG CHEM\PHY
    elif (f and sub_1 == 1 and sub_2 == 2 and sub_3 == 4) or (
                f and sub_1 == 1 and sub_2 == 4 and sub_3 == 2) or (
                f and sub_1 == 2 and sub_2 == 4 and sub_3 == 1) or (
                f and sub_1 == 2 and sub_2 == 1 and sub_3 == 4) or (
                f and sub_1 == 4 and sub_2 == 1 and sub_3 == 2) or (
                f and sub_1 == 4 and sub_2 == 2 and sub_3 == 1) or (f and sub_1 == 1 and sub_2 == 3 and sub_3 == 4) or (
                f and sub_1 == 1 and sub_2 == 4 and sub_3 == 3) or (
                f and sub_1 == 3 and sub_2 == 4 and sub_3 == 1) or (
                f and sub_1 == 3 and sub_2 == 1 and sub_3 == 4) or (
                f and sub_1 == 4 and sub_2 == 1 and sub_3 == 3) or (
                f and sub_1 == 4 and sub_2 == 3 and sub_3 == 1) or (f and sub_1 == 1 and sub_2 == 2 and sub_3 == 5) or (
                f and sub_1 == 1 and sub_2 == 5 and sub_3 == 2) or (
                f and sub_1 == 2 and sub_2 == 5 and sub_3 == 1) or (
                f and sub_1 == 2 and sub_2 == 1 and sub_3 == 5) or (
                f and sub_1 == 5 and sub_2 == 1 and sub_3 == 2) or (
                f and sub_1 == 5 and sub_2 == 2 and sub_3 == 1) or (f and sub_1 == 1 and sub_2 == 3 and sub_3 == 5) or (
                f and sub_1 == 1 and sub_2 == 5 and sub_3 == 3) or (
                f and sub_1 == 3 and sub_2 == 5 and sub_3 == 1) or (
                f and sub_1 == 3 and sub_2 == 1 and sub_3 == 5) or (
                f and sub_1 == 5 and sub_2 == 1 and sub_3 == 3) or (
                f and sub_1 == 5 and sub_2 == 3 and sub_3 == 1):
            career_type = "Conventional career type"
            course_1 = "Range management"
            course_2 = "Wildlife Enterprise Management"
            course_3 = "Wildlife Management(and conservation)"
            course_4 = ' Environmental Resource Management'
            course_5 = 'Environmental Science & Technology'
            course_6 = ' Natural Resources Management '
            course_7 = ' Environmental Planning & Management'
            course_8 = "Soil Environment And Land Use Management"
            course_9 = 'Forest Resources Management'
            course_10 = 'Coastal and marine resource management'


     #difines rules for specific convectional careers careers
    #     this follows the fact that one belong to convectional career but differs in subjecs
    #     math, phy, relg / geo
    elif (f and sub_1 == 1 and sub_2 == 7 and sub_3 == 4) or (
                f and sub_1 == 1 and sub_2 == 4 and sub_3 == 7) or (
                f and sub_1 == 7 and sub_2 == 4 and sub_3 == 1) or (
                f and sub_1 == 7 and sub_2 == 1 and sub_3 == 4) or (
                f and sub_1 == 4 and sub_2 == 1 and sub_3 == 7) or (
                f and sub_1 == 4 and sub_2 == 7 and sub_3 == 1) or (
                f and sub_1 == 1 and sub_2 == 11 and sub_3 == 4) or (
                f and sub_1 == 1 and sub_2 == 4 and sub_3 == 11) or (
                f and sub_1 == 11 and sub_2 == 4 and sub_3 == 1) or (
                f and sub_1 == 11 and sub_2 == 1 and sub_3 == 4) or (
                f and sub_1 == 4 and sub_2 == 1 and sub_3 == 11) or (
                f and sub_1 == 4 and sub_2 == 11 and sub_3 == 1):
            career_type = "Conventional career type"
            course_1 = "Real Estate, Property Management"
            course_2 = "Land Administration"
            course_3 = ""
            course_4 = ''
            course_5 = ''
            course_6 = ' '
            course_7 = ''
            course_8 = ""
            course_9 = ''
            course_10 = ''
     #difines rules for specific convectional careers careers
    #       this follows the fact that one belong to convectional career but differs in subjecs
    #       math, geo / bio, chem / phy
    elif (f and sub_1 == 1 and sub_2 == 11 and sub_3 == 4) or (
                f and sub_1 == 1 and sub_2 == 4 and sub_3 == 11) or (
                f and sub_1 == 11 and sub_2 == 4 and sub_3 == 1) or (
                f and sub_1 == 11 and sub_2 == 1 and sub_3 == 4) or (
                f and sub_1 == 4 and sub_2 == 1 and sub_3 == 11) or (
                f and sub_1 == 4 and sub_2 == 11 and sub_3 == 1) or (
                f and sub_1 == 1 and sub_2 == 6 and sub_3 == 4) or (
                f and sub_1 == 1 and sub_2 == 4 and sub_3 == 6) or (
                f and sub_1 == 6 and sub_2 == 4 and sub_3 == 1) or (
                f and sub_1 == 6 and sub_2 == 1 and sub_3 == 4) or (
                f and sub_1 == 4 and sub_2 == 1 and sub_3 == 6) or (
                f and sub_1 == 4 and sub_2 == 6 and sub_3 == 1) or (
                f and sub_1 == 1 and sub_2 == 11 and sub_3 == 5) or (
                f and sub_1 == 1 and sub_2 == 5 and sub_3 == 11) or (
                f and sub_1 == 11 and sub_2 == 5 and sub_3 == 1) or (
                f and sub_1 == 11 and sub_2 == 1 and sub_3 == 5) or (
                f and sub_1 == 5 and sub_2 == 1 and sub_3 == 11) or (
                f and sub_1 == 5 and sub_2 == 11 and sub_3 == 1) or (
                f and sub_1 == 1 and sub_2 == 6 and sub_3 == 5) or (
                f and sub_1 == 1 and sub_2 == 5 and sub_3 == 6) or (
                f and sub_1 == 6 and sub_2 == 5 and sub_3 == 1) or (
                f and sub_1 == 6 and sub_2 == 1 and sub_3 == 5) or (
                f and sub_1 == 5 and sub_2 == 1 and sub_3 == 6) or (
                f and sub_1 == 5 and sub_2 == 6 and sub_3 == 1):
            career_type = "Conventional career type"
            course_1 = "Community Resource Management"
            course_2 = "Resource Conservation"
            course_3 = "Event & Convention Management"
            course_4 = 'Hydrology & Water Resources Management'
            course_5 = ''
            course_6 = ' '
            course_7 = ''
            course_8 = ""
            course_9 = ''
            course_10 = ''
    
     #difines rules for specific convectional careers careers
       # this follows the fact that one belong to convectional career but differs in subjecs
    elif (f and sub_1 and sub_2 and sub_3):
            career_type = "Conventional career type"
            course_1 = "Land Administration"
            course_2 = 'Hydrology & Water Resources Management'
            course_3 = 'Forest Resources Management'
            course_4 = "Wildlife Management(and conservation)"
            course_5 = 'Accounting And Finance'
            course_6 = "Actuarial Science"
            course_7 = 'Mathematical Sciences, Mathematics & Physic'
            course_8 = 'Economics & Sociology'
            course_9 = ' Financial Economics'
            course_10 = "Event & Convention Management"
    else:
            career_type = " No career type matching "
            course_1 = "You may need to go back and answer the question 1-5 correctly"
            course_2 = "You can contact us in case you find any challenge getting your career"
            course_3 = ""
            course_4 = ''
            course_5 = ''
            course_6 = ' '
            course_7 = ''
            course_8 = ""
            course_9 = ''
            course_10 = ''
    context = {
            'career_type': career_type,
            'course_1': course_1,
            'course_2': course_2,
            'course_4': course_4,
            "course_3": course_3,
            "course_5": course_5,
            "course_6": course_6,
            "course_7": course_7,
            "course_8": course_8,
            "course_9": course_9,
            "course_10": course_10,
        }
        
    return render(request, "consult/consult.html", context)
    
# to do
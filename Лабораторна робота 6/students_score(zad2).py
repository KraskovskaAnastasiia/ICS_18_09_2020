course_settings_dict_test = {
    'max_amount_of_marks_for_individual_project': 100,
    'max_mark_per_one_lab': 10,
    'amount_of_labs_in_course': 10,
    'total_amount_for_auto_mark': 95
}


class Student():

    def __init__(self, student_name, course_settings_dict):
        self.student_name = student_name
        self.course_settings_dict = course_settings_dict

        #початкова кількість спроб здачі лабораторної роботи та індивідуального проекту
        self.lab_tries = 0
        self.ind_project_tries = 0

        #початкові оцінки за лабораторну роботу та індивідуальний проект
        self.total_lab_marks = 0
        self.total_individual_marks = 0

    #додаємо оцінку за останню спробу здачі лабораторної роботи
    def add_mark_for_last_lab_try(self, mark):
        self.total_lab_marks += mark

    #додаємо кількість спроб здачі індивідуального проекту
    def add_amount_of_tries_to_pass_lab(self, amount, mark):
        self.lab_tries = amount
        self.add_mark_for_last_lab_try(mark)

    #додаємо кількість спроб здачі індивідуального проекту
    def add_amount_of_tries_to_pass_ind_project(self, amount, mark):
        self.ind_project_tries = amount
        self.add_mark_for_last_ind_project_try(mark)

    #додаємо оцінку за останню спробу здачі індивідуального прокту 
    def add_mark_for_last_ind_project_try(self, mark):
        self.total_individual_marks += mark

    def get_student_report(self):
        amount_of_marks = self.total_lab_marks + self.total_individual_marks
        is_auto_mark = False

        if amount_of_marks >= self.course_settings_dict['total_amount_for_auto_mark']:
            is_auto_mark = True

        result_turple = (amount_of_marks, is_auto_mark)
        return result_turple

#додаємо студента
student = Student("Настя", course_settings_dict_test)

#приймаємо дані з консолі, які будуть введені користувачем щодо кількості спроб лабораторної роботи та оцінки за останню лабораторну роботу
amount_of_tries = input("Кількість спроб лабораторної роботи: ")
last_lab_mark = input("Оцінка за останню лабораторну роботу: ")

student.add_amount_of_tries_to_pass_lab(int(amount_of_tries), int(last_lab_mark))

#приймаємо дані з консолі, які будуть введені користувачем щодо кількості спроб індивідуального проекту та останточну оцінку за індивідуальний проект
amount_of_ind_tries = input("Кількість спроб індивідуального проекту: ")
last_ind_mark = input("Оцінка за останню здачу лабораторного проекту: ")

student.add_amount_of_tries_to_pass_ind_project(int(amount_of_ind_tries), int(last_ind_mark))

#виводимо користувачу загальні оцінки та його(її) автоматичну оцінку
result_turple = student.get_student_report()
print('Загальні оцінки: ' + str(result_turple[0]) + ' Автоматична оцінка: ' + str(result_turple[1]))
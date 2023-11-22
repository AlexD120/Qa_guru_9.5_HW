import os

import pytest
from selene import browser, have,be
from selene.support.shared.jquery_style import s, ss

def test_practice_form():
    browser.open('/')
    s('.pattern-backgound').should(have.exact_text('Practice Form'))

    first_name = browser.element('#firstName')
    last_name = browser.element('#lastName')
    date_of_birth = browser.element('#dateOfBirthInput')


    """Заполняем Name"""
    first_name.should(be.blank).type("Alex")
    last_name.should(be.blank).type('Davydov')

    """Заполняем Email"""
    s('#userEmail').should(be.blank).type('AlexDavydov92@gmail.com')

    """Заполняем Gender"""
    s('#gender-radio-1').double_click()

    """Заполняем Mobile"""
    s('#userNumber').type('8005553535')

    """Заполняем Date of Birth"""
    s('#dateOfBirthInput').click()
    s('.react-datepicker__month-select').click().type('June').press_enter()
    s('.react-datepicker__year-select').click().type('1992').press_enter()
    s('.react-datepicker__day--020').click()

    """Заполняем Subjects"""
    s('#subjectsInput').should(be.blank).type('Russia')

    """Заполняем Hobbies"""
    s('#hobbies-checkbox-2').click()

    """Подгружаем Picture"""
    s('#uploadPicture').send_keys(os.path.abspath('tests/image/selfies.jpeg'))


    #first_name.should(have.exact_texts('Alex'))
    #last_name.should(have.text('Davydov'))
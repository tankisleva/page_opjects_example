import os

from fw.model.pages import practice_form


def test_student_registration_form():
    practice_form.given_opened()

    # WHEN
    practice_form.type_firstname('World')
    practice_form.type_lastname('Peace')
    practice_form.type_email('qwe@mail.com')

    practice_form.select_gender('Male')

    practice_form.type_phone_number('9177121162')

    practice_form.click_on_datepicker()
    practice_form.pick_month('April')
    practice_form.pick_year('1986')
    practice_form.pick_day(16)

    practice_form.type_subject('English')

    practice_form.select_hobby('Sports')

    practice_form.scroll_to_address()
    practice_form.type_address('Some address')

    practice_form.upload_picture('img.png')

    practice_form.select_state('NCR')
    practice_form.select_city('Delhi')

    practice_form.submit()

    # THEN

    practice_form.assert_fields(
            'World Peace',
            'qwe@mail.com',
            'Male',
            '9177121162',
            '16 April,1986',
            'English',
            'Sports',
            'img.png',
            'Some address',
            'NCR Delhi'
    )
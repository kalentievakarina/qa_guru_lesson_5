from selene import browser, have, be, query, command, by
import os

def test_user_form():
   browser.open('https://demoqa.com/automation-practice-form')

   #browser.get(query.title)
   browser.element('#firstName').should(be.blank)
   browser.element('#firstName').type('M').press_enter()
   browser.element('#lastName').should(be.blank)
   browser.element('#lastName').type('M').press_enter()
   browser.element('#userEmail').should(be.blank)
   browser.element('#userEmail').type('new@email.com').press_enter()
   browser.element('[for="gender-radio-2"]').click()
   browser.element('#userNumber').should(be.blank)
   browser.element('#userNumber').type('1234567890')
   browser.element('#dateOfBirthInput').click()
   browser.element('.react-datepicker__month-select').click()
   browser.element('.react-datepicker__month-select').click().element(by.text('July')).click()
   browser.element('.react-datepicker__year-select').click().element(by.text('1996')).click()
   browser.element(by.text('15')).click()
   browser.element('#subjectsInput').type('commerce').press_enter()
   browser.element('[for="hobbies-checkbox-2"]').perform(command.js.scroll_into_view).click()
   browser.element('#currentAddress').type('takay-to street, 92')
   browser.element('#stateCity-wrapper').element('#state').click().element('#react-select-3-option-0').click()
   browser.element('#stateCity-wrapper').element('#city').click().element('#react-select-4-option-0').click()

   browser.element('#submit').click()


# Result

   browser.element('.table').should(have.text('M M'))
   browser.element('.table').should(have.text('new@email.com'))
   browser.element('.table').should(have.text('Female'))
   browser.element('.table').should(have.text('1234567890'))
   browser.element('.table').should(have.text('15 July,1996'))
   browser.element('.table').should(have.text('Commerce'))
   browser.element('.table').should(have.text('Reading'))
   browser.element('.table').should(have.text('takay-to street, 92'))
   browser.element('.table').should(have.text('NCR Delhi'))
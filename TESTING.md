# Manual and Automated Testing

This section of the documentation comprises of various manual and automated tests and online validators to check the quality of my code and also to check the functionality of the project.

See User Story:
[USER STORY: Testing]([#34](https://github.com/Robrowno/django-raceway/issues/34))

## Table of Contents

- [Manual Testing](#manual-testing)
- [HTML Validation](#html-validation)
- [CSS Validation](#css-validation)
- [JS Validation](#js-validation)
- [Python Validation](#python-validation)
- [Lighthouse Performance](#lighthouse-performance-testing)
- [Devices/Browsers](#device-and-browser-testing)
- [Known/Unresolved Bugs](#current-known-and-unresolved-issues)


---

## Automated Testing


---

## Manual Testing

### Home/Index/Middle-Navigation
| Test | Method | Expected Outcome | Result |
| - | - | - | - |
| Django Raceway Logo/Home Link | Click on Logo at top of Page | Redirect to the home page | PASS |
| Carousel | Click on chevrons either side of carousel | Moves to next image slide in correct direction | PASS |
| Booking Link | Click on middle nav link | Opens Trackday Booking Page | PASS |
| Cars for Hire Link | Click on middle nav link  | Opens Car Hire Page | PASS |
| Tuition Link | Click on middle nav link  | Opens Tuition Page | PASS |
| Experiences Link | Click on middle nav link  | Opens Experiences Page | PASS |
| Contact Link | Click on middle nav link  | Opens Contact Page | PASS |
| About Page Link | Click on middle nav link  | Opens About Page | PASS |
| Gallery Modal Click | Click on a modal image in the Gallery | Expands image when clicked | PASS |
| Gallery Modal Next | Click on chevrons either side of the image | Moves to next image slide in correct direction | PASS |
| Gallery Modal Close | Click on the 'x' at the top of the image | Closes image model | PASS |


### Footer/Mailchimp
| Test | Method | Expected Outcome | Result |
| - | - | - | - |
| Policies Link | Click on link | opens the Policies page | PASS |
| FAQs Link | Click on link | opens FAQs Page | Pass |
| Up-Arrow button | Click on up-arrow button | Takes you to the top of the page | PASS |
|  |  |  |  |
|  |  |  |  |


### Booking Page/Booking Detail
| Test | Method | Expected Outcome | Result |
| - | - | - | - |
| Trackday Display | check Trackdays are rendering on the page by clicking on the 'booking' tab in the middle nav | Expect to see a list of upcoming trackdays, with details including base price displayed | PASS |
| Hide Trackday in Basket |  |  |  |
| Button change when Trackday in basket |  |  |  |
| Request Trackday Button |  |  |  |
| Availability counter update |  |  |  |
| Booking Button change when full |  |  |  |
|  |  |  |  |


### Tuition/Experiences and Detail Pages
| Test | Method | Expected Outcome | Result |
| - | - | - | - |
| Tuition Page | Click on tuition tab | Opens tuition page where you will see list of tuition packages displayed | PASS |
| Experience Page | Click on experiences tab and | Opens experiences page where you will see list of experiences displayed | PASS |
| Tuition Detail |  |  |  |
| Experience Detail |  |  |  |
| Quantity adjustments |  |  |  |
| Booking button |  |  |  |
|  |  |  |  |


### Trackday Request
| Test | Method | Expected Outcome | Result |
| - | - | - | - |
| Submit Button | Submit form without filling out any required fields | Form validation will prevent it from sending and alert the site user | PASS |
| Submit Button | Submit with one required input filled in only | Form validation will prevent it from sending and alert the site user | PASS |
| Email input | Try to enter an invalid email address or random numbers, words etc.  | Form will not send and user will be informed to enter a valid email address | PASS |
| Date input | Try to enter a past date or today's date | JS Alert will inform the user to enter a date no sooner than today | PASS |
| Number of spaces | Try to enter an incorrect number outside of the specified min and max | Form validation will prevent it from sending and alert the site user | PASS |
| Submit Complete Form | Submit a valid form via the submit button | Return to home page and inform user of successful submission with a success toast | PASS |
| Database | Check output of submission in the database | All filled out information should be strored correctly in the database | PASS |



### Contact
| Test | Method | Expected Outcome | Result |
| - | - | - | - |
| Submit Form | Attempt to submit blank form with nothing filled in | Form validation will prevent form from sending and alert user to which input needs filling in | PASS |
| Submit Form | Attempt to submit with just one input filled in  | Form validation will prevent form from sending and alert user to which input needs filling in | PASS |
| Email input | Try to enter an invalid email address or random numbers, words etc.  | Form will not send and user will be informed to enter a valid email address | PASS |
| Submit Valid Form | Submit a complete and valid contact form | Page redirects to a success version of the same page, informs the user it sent successfully | PASS |
| Return Home Button | Click on button | Redirects back to the Home page | PASS |
| Database | Check output of submission in the database | All filled out information should be strored correctly in the database | PASS |



### Profile
| Test | Method | Expected Outcome | Result |
| - | - | - | - |
| Profile Link | Check appearance when logged out | Profile page is not accessible to users not logged in | PASS |
| Profile Link | Check appearance and click on link when logged in | User will be redirected to their profile page | PASS |
| Edit Button |  |  |  |
| Save Button |  |  |  |
| Input fields |  |  |  |
|  |  |  |  |
|  |  |  |  |


### Authentication
| Test | Method | Expected Outcome | Result |
| - | - | - | - |
| Sign Up | Create an account | You will be asked to verify your account and sent an email to verify it | PASS |
| Verification Email | Click on email link to verify account | Upon click, you will be redirected to the site where it will be confirmed that your account is verified | PASS |
| Login | Login with a registered account | Redirected to homepage and informed you are logged in | PASS |
| Remember me checkbox | Click on remember me checkbox button before loggin in | You will not need to login next time you visit the site | PASS |
| Forgot Password |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

### Basket and Checkout
| Test | Method | Expected Outcome | Result |
| - | - | - | - |
| Basket Link | Click on Basket link in top nav | Redirects to basket page | PASS |
| Checkout Link | Have nothing in the basket and check basket icon for visibility  | If nothing is in the basket, the checkout page will be hidden | Pass |
| Basket Page with no items | Click on basket page with nothing in the basket | Item counter reads as 0 and user is informed that there are no items in the basket, summary is blank | PASS |
| Item in Basket |  |  |  |
| Multiple items in Basket |  |  |  |
| Delete Item in basket |  |  |  |
| Summary total Calculator |  |  |  |
| Summary VAT calculator |  |  |  |
| Checkout Button (Basket Page) |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

### Management
| Test | Method | Expected Outcome | Result |
| - | - | - | - |
| Management Link |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

### Other
| Test | Method | Expected Outcome | Result |
| - | - | - | - |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

---

## HTML Validation

### /templates 

| File | Result |
| -------- | ------ |
| base.html  | |
| main-nav.html  | |
| includes/base.html | |
| includes/toast_error.html  | |
| includes/toast_info.html  | |
| includes/toast_success.html  | |
| includes/toast_warning.html | |
| 404.html | |

### /trackdays

| File | Result |
| -------- | ------ |
|  experience-detail.html | |
|  experiences.html | |
|  trackday-detail.html | |
|  trackday-list.html | |
|  trackday-request.html | |
|  tuition-detail.html | |
|  tuition.html | |
|  includes/increment_decrement.html | |

### /profiles

| File | Result |
| -------- | ------ |
| edit-profile.html  | |
| profile.html  | |

### /home

| File | Result |
| -------- | ------ |
| about.html  | |
| contact.html  | |
| faqs.html  | |
| index.html  | |
| policies.html  | |
| management.html  | |

### /checkout

| File | Result |
| -------- | ------ |
| basket.html  | |
| checkout-success.html  | |
| checkout.html  | |


### /cars

| File | Result |
| -------- | ------ |
| car-hire.html  | |


### Current HTML Errors/Issues/Explanations:

- 

---

## CSS Validation


### /static/css

| File | Result |
| -------- | ------ |
| base.css  | |


### /trackdays/css

| File | Result |
| -------- | ------ |
| booking-detail.css  | |
| exp_detail.css  | |
| experiences.css  | |
| trackday-request.css  | |
| trackdays.css  | |
| tuition-detail.css  | |
| tuition.css  | |

### /profiles/css

| File | Result |
| -------- | ------ |
| profiles.css  | |

### /home/css

| File | Result |
| -------- | ------ |
| about.css  | |
| contact.css  | |
| index.css  | |

### /basket/css

| File | Result |
| -------- | ------ |
| basket.css  | |
| checkout.css  | |
| success.css  | |

### cars/css

| File | Result |
| -------- | ------ |
| cars.css  | |



### Current CSS Errors/Issues/Explanations:

- 


---

## JS Validation

### static/js

| File | Result |
| -------- | ------ |
| base.js  |  |

### trackdays/js

| File | Result |
| -------- | ------ |
|  |  |
|  |  |

### profiles/js

| File | Result |
| -------- | ------ |
| profile.js |  |

### home/js

| File | Result |
| -------- | ------ |
| base.js  |  |

### checkout/js

| File | Result |
| -------- | ------ |
|  |  |
|  |  |


### Current JS Errors/Issues/Explanations:

- 


---

## Python Validation

### /django_raceway


| File | Result |
| -------- | ------ |
| settings.py |  |
| urls.py |  |


### /trackdays

| File | Result |
| -------- | ------ |
| admin.py |  |
| models.py |  |
| tests.py |  |
| urls.py |  |
| views.py |  |



### /profiles

| File | Result |
| -------- | ------ |
| admin.py |  |
| models.py |  |
| tests.py |  |
| urls.py |  |
| views.py |  |



### /home

| File | Result |
| -------- | ------ |
| admin.py |  |
| models.py |  |
| tests.py |  |
| urls.py |  |
| views.py |  |



### /checkout

| File | Result |
| -------- | ------ |
| admin.py |  |
| contexts.py |  |
| models.py |  |
| tests.py |  |
| urls.py |  |
| views.py |  |



### /cars

| File | Result |
| -------- | ------ |
| admin.py |  |
| models.py |  |
| tests.py |  |
| urls.py |  |
| views.py |  |



### Current Python Errors/Issues/Explanations:

- 
- 
- 

---

## Lighthouse Performance Testing

- Lighthouse Testing was performed in an incognito tab to ensure no external chrome add-ons were affecting the test.
- Results of the Lighthouse Performance testing below:




---

## Device and Browser Testing

- Browsers Tested:
    - Google Chrome
    - Safari

- Devices Tested:
    - MacBook Pro
    - Apple iPhone 12 Pro
    - iPhone 14 Pro
    - iPhone X
    - iPad Pro



### Responsiveness

- The site has been tested down to screen widths of 300px and up to screen widths of 2560px
- The site is fully responsive between these viewport widths

---


## Current known and unresolved issues

- 
- 
- 
- 


--- 

[Return to Top](#manual-and-automated-testing)